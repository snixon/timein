import argparse
import requests
from timein import CONFIG
from datetime import datetime


def arguments():
    """Collect our arguments"""
    parser = argparse.ArgumentParser(description="Check the time in a city")
    parser.add_argument("location", nargs='?', help="Location to lookup the time of")
    args = parser.parse_args()
    return args


def geoCode(location):
    LAT_LONG_KEY = CONFIG["LAT_LONG_KEY"]
    url = "http://www.mapquestapi.com/geocoding/v1/address?key={}&maxResults=1&location={}".format(
        LAT_LONG_KEY, location
    )
    req = requests.get(url)
    if req.status_code != 200:
        return req.text
    else:
        res = req.json()
    return res["results"][0]["locations"][0]["latLng"]


def timezone(location_dict):
    TZDB_KEY = CONFIG["TZDB_KEY"]
    url = "http://api.timezonedb.com/v2.1/get-time-zone?key={}&format=json&by=position&lat={}&lng={}".format(
        TZDB_KEY, location_dict["lat"], location_dict["lng"]
    )
    req = requests.get(url)
    if req.status_code != 200:
        return req.text
    else:
        res = req.json()
    return res


def main():
    args = arguments()
    if args.location:
        timedata = timezone(geoCode(args.location))
        print(
            "The time in {}, ({}) is {}".format(
                args.location.capitalize(), timedata["abbreviation"], timedata["formatted"]
            )
        )
    else:
        print(
            "The local time is {}".format(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )


if __name__ == "__main__":
    main()
