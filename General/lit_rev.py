"""Module to retrieve Astrophyical Database System of NASA data for literature reviewing"""

import ads # The necessary package for NASA ADS API

ads.config.token = '##YOUR TOKEN HERE##'
# Look at here https://ads.readthedocs.io/en/latest/#getting-started to generate your TOKEN
# Also check https://ads.readthedocs.io/en/latest/#rate-limit-usage for query rate limit


# Initial query according to the parameters defined below

papers = ads.SearchQuery(q=['exoplanet', 'JWST', 'disk'], # Query terms
                         fl=['title', 'year', 'citation_count'], # Field limit to query
                         sort='year', # Sorting results according to this field
                         max_pages=1  # Page limit, max 50 entry for a page)

# Following look prints the title, publication year, and citation count of the items queried

i = 0 # This makes a rank/sort number, so we can then retrieve that entry specifically after the same query
for paper in papers:
    i = i + 1
    print(i, paper.title, ", Pub. year: ", paper.year, ", # of cit.", paper.citation_count, '\n')

# Following function makes the same query as above, and only retrieves the specified entry orders
# like 1 for retrieving the first item's title, publication year, citation count AND its abstract.

def abs_int(list_int: [list, int]):
    """ After seeing a query result, prints desired title's abstracts right below them
    
    :param list_int: int or list of integers to retrieve title and abstracts
    """
    papers = ads.SearchQuery(q=["exoplanet", "JWST", "disk"], fl=['title', 'abstract', 'year', 'citation_count'], sort="year", max_pages=1 )
    i = 0
    for paper in papers:
        i = i + 1
        if type(list_int) == list:
            if i in list_int:
                print(i, paper.title, "Pub. year: ", paper.year, "# of cit.", paper.citation_count, '\n', '\n', paper.abstract, '\n')
        elif (type(list_int) == int) & (i == list_int):
            print(i, paper.title, paper.year, paper.citation_count, '\n', '\n', paper.abstract, '\n')
            break
