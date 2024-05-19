"""Module to retrieve Astrophyics Data System of NASA data for literature reviewing"""

import ads # The necessary package for NASA ADS API

ads.config.token = '##YOUR TOKEN HERE##'
# Look at here https://ads.readthedocs.io/en/latest/#getting-started to generate your TOKEN
# Also check https://ads.readthedocs.io/en/latest/#rate-limit-usage for query rate limit

# Example uses

query = ["JWST","disk","exoplanet"]

# Print titles and year, citation_counts, Quick look to the query results
> litrevlib.ret(query) 

# Print the 3rd in the list's title, year, citation count, abstract
> litrevlib.ret(query, 3) 

# Print the 3rd and 4th in the list's title, year, citation count, abstract
> litrevlib.ret(query, [3,4]) 

# Print the 3rd in the list's title, year, citation count, abstract and its citation in BibTeX format
> litrevlib.ret(query, 3, cite=True) 

# Print the 3rd in the list's title, year, citation count, abstract and its citation in BibTeX format and appends it to the .bib file specified in "locat"
> litrevlib.ret(query, 3, cite=True, loca= locat) 
