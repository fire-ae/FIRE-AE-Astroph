import ads

def ret(query_terms: [list, str], list_int=[], cite=False, loca=""):
    """ 
    Provides titles, publication year, and citation count according to the query_terms
    If a list_int is provided, retrieves abstracts for the selected items 
    If cite is True, prints BibTex formatted citation for the selected entry
    
    :param query terms: search query terms to look up in NASA ADS
    :param list_int: int or list of integers to retrieve title and abstracts
    :param cite: printing bibtex formatted citation of the selected items
    :param loca: location for the .bib file to append selected titles' BibTex entries
    """
    
    # Constructing the query
    
    sq = ads.SearchQuery(q=query_terms, 
                             fl=['title', 'abstract', 'year', 'citation_count', 'bibcode'], # field limits
                             sort="year", # sorting according to the publication year
                             max_pages=1) # max 50 items with max_pages 1
    sq.execute()
    i = 0
    for item in sq:
        i = i + 1
        if list_int == []: # This gives the quick look, without printing abstracts
            print(i, item.title, "Pub. year: ", item.year, "# of cit.", item.citation_count,'\n')
        if type(list_int) == list:
            if i in list_int:
                print(i, item.title, "Pub. year: ", item.year, "# of cit.", item.citation_count, '\n', '\n', item.abstract, '\n')
        elif (type(list_int) == int) & (i == list_int):
            print(i, item.title, "Pub. year: ", item.year, "# of cit.", item.citation_count, '\n', '\n', item.abstract, '\n')
            break
    if cite == True:
        print("Citations")
        print("---------")
        i = 0
        for item in sq:
            i = i + 1
            if type(list_int) == list:
                if i in list_int:
                    if loca != "":
                        with open(loca, 'a', encoding="utf-8") as k:
                            k.write(str(ads.ExportQuery(item.bibcode, format='bibtex').execute()))
                            k.write(" \n")
                            print(ads.ExportQuery(item.bibcode, format='bibtex').execute())
                    else:
                        print(ads.ExportQuery(item.bibcode, format='bibtex').execute())
            elif (type(list_int) == int) & (i == list_int):
                if loca != "":
                    with open(loca, 'a', encoding="utf-8") as k:
                        k.write(str(ads.ExportQuery(item.bibcode, format='bibtex').execute()))
                        k.write(" \n")
                        print(ads.ExportQuery(item.bibcode, format='bibtex').execute())
                break
