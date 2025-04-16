# Folder specific for Image examinations from James-Webb Space Telescope.

>[!IMPORTANT]
>Again currently (April 16, 2025), the code works just fine.
>Currently (April 18, 2024), there is no problem, code is working fine.

>[!WARNING]
>On April 14, 2024, the code, and filtering/querying functions returned the following time-out error (both in Google Colab and Python 3.12 in Windows 11 environment):
>
>requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='mast.stsci.edu', port=443): Max retries exceeded with url: /api/v0/invoke (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x000001E853866C60>, 'Connection to mast.stsci.edu timed out. (connect timeout=None)'))

MAST_downloader file is filtering and downloading specific JWST MIRI images, in this case, to one's Google Drive folder. This is recommended to be used in Google Colaboratory Service. 
