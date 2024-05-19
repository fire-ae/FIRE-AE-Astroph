Module to retrieve Astrophyics Data System of NASA data for literature reviewing

Loads the required library
> import litrevlib # Stored custom functions
> import ads # The necessary package for NASA ADS API

Sets the configuration for your token:

>ads.config.token = '##YOUR TOKEN HERE##'

> [!IMPORTANT]
> Look at here https://ads.readthedocs.io/en/latest/#getting-started to generate your TOKEN
> Also check https://ads.readthedocs.io/en/latest/#rate-limit-usage for query rate limit

# Example uses

The following part sets the query terms
> query = ["JWST","disk","exoplanet"]

The following use cases show the capabilities of this library.

* Print titles and year, citation_counts, Quick look to the query results
    > litrevlib.ret(query) 

* Print the 3rd in the list's title, year, citation count, abstract
    > litrevlib.ret(query, 3) 

* Print the 3rd and 4th in the list's title, year, citation count, abstract
    > litrevlib.ret(query, [3,4]) 

* Print the 3rd in the list's title, year, citation count, abstract and its citation in BibTeX format
    > litrevlib.ret(query, 3, cite=True) 

* Print the 3rd in the list's title, year, citation count, abstract and its citation in BibTeX format and appends it to the .bib file specified in "locat"
    > litrevlib.ret(query, 3, cite=True, loca= locat) 
