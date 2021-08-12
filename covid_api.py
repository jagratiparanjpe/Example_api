import requests

def get_iso_data(date, iso, url):
    """
    extract data from api

    :param date:
    :param iso:
    :param url:
    :return:
    """
    url = url + 'date=' + str(date) + '&iso=' + iso
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    status_code = r.status_code
    res_data = r.json()['data']

    confirmed = 0
    deaths = 0
    recovered = 0
    l1 = [(item["confirmed"], item["deaths"], item["recovered"]) for item in res_data]

    for c, d, r in l1:
        confirmed = confirmed + c
        deaths = deaths + d
        recovered = recovered + r

    return [date, iso, confirmed, deaths, recovered]
