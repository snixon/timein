import argparse
import requests
from timein import CONFIG
from datetime import datetime


def arguments():
    """Collect our arguments"""
    parser = argparse.ArgumentParser(description="Check the time in a city")
    parser.add_argument("location", nargs="?", help="Location to lookup the time of")
    args = parser.parse_args()
    return args


def bing_search(location):
    key = CONFIG["BING_KEY"]
    url = "https://dev.virtualearth.net/REST/v1/TimeZone/query={}?key={}".format(location, key)
    req = requests.get(url)
    if req.status_code != 200:
        return req.text
    else:
        res = req.json()
    return res


def main():
    args = arguments()
    if args.location:
        timedata = bing_search(args.location)
        place = timedata["resourceSets"][0]["resources"][0]["timeZoneAtLocation"][0]["placeName"]
        zone = timedata["resourceSets"][0]["resources"][0]["timeZoneAtLocation"][0]["timeZone"][0]["convertedTime"]["timeZoneDisplayAbbr"]
        time = timedata["resourceSets"][0]["resources"][0]["timeZoneAtLocation"][0]["timeZone"][0]["convertedTime"]["localTime"].replace('T', ' ', 1)
        print("The time in {}, ({}) is {}".format(place, zone, time))
    else:
        print("The local time is {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == "__main__":
    main()
