# General Tools beneficial in the process of Astrophysics Research

> [!NOTE]
> #Literature Review Assisting Tool in Astrophysics
> 
> [lit_rev.md] and [litrevlib.py]

> [!WARNING]
> New papers and preprints are rapidly being published and quickly recorded in ADS database, hence query results may change daily.

> [!WARNING]
> This is not fool-proof. The user is responsible for, i.e., not putting a NumPy array for a string formatted path variable.

  * Arguably, it will benefit people with low-end PC and easily distracted mind, as it will not require to open a browser to look for interesting articles' abstracts.
  * It completely uses NASA ADS simple query, and selectively retrieves abstract of that query later with a custom function.
 
     - If only provided with query terms:
         - It queries NASA ADS and returns title, publication year, citation count (and also bibcode) of 50 entries [manually editing max_pages in the query construct will increase this, but not recommended]
     - If an integer or list of integers are provided besides query terms:
         - It will query the previous query terms, but only prints selected ranks in the entries via integer or list of integer provided, and prints title, publication year, citation count AND abstract of the entry
     - If cite is set to True:
         - It will print BibTex formatted citation of the selected entry(ies)
     - If loca is set to a .bib file:
         - The resulting BibTex entry from the previous query will be appended to the set .bib file.
