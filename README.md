#timein

A silly gadget so I can stop googling what time it is in a city to see if my friends are up yet.

Requires an API key from Mapquest to lookup Latitude and Longitude by City:
http://www.mapquestapi.com/geocoding, export this as an env_var: `TIMEIN_LAT_LONG`

Also requires an API key from http://api.timezonedb.com, to translate lat+long into a timestamp.
export this as an env_var `TIMEIN_TZDB_KEY`

# Install it
```
1. git clone https://github.com/snixon/timein.git
2. cd timein
3. python3 setup.py install
```

# Example

```
$> timein berlin
The time in Berlin, (CEST) is 2019-05-02 07:57:53
```