import requests

def get(url):
    api_url = 'https://api.staging.openconceptlab.org'

    ocl_api_token = '57ce8e00f2461a844f428f92dafa26ce3ea0c115'  # add API token from your user account -- all PEPFAR sources are open, so any API token will work

    ocl_api_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token %s' % ocl_api_token
    }

    r = requests.get(api_url + url, headers=ocl_api_headers)
    r.raise_for_status()
    result = r.json()
    return result