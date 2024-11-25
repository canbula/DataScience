from credentials import API_KEY
import requests
import json
import pandas as pd


class AirQuality:
    def __init__(self):
        self.base_url = "https://api.openaq.org/v3"
        self.headers = {"accept": "application/json", "X-API-KEY": API_KEY}
        self.countries = []

    def fetch_countries(self):
        i = 1
        while True:
            url = f"{self.base_url}/countries?limit=100&page={i}"
            response = requests.get(url, headers=self.headers)
            data = response.json()
            countries = data["results"]
            if not countries:
                break
            self.countries.extend(countries)
            i += 1
        return self.countries

    def get_countries(self):
        try:
            with open("countries.json", "r") as json_file:
                data = json.load(json_file)
                self.countries = data["results"]
        except FileNotFoundError:
            self.countries = self.fetch_countries()
            with open("countries.json", "w", encoding="utf-8") as json_file:
                json.dump({"results": self.countries}, json_file, indent=4)
        return self.countries

    def process_countries(self):
        countries = self.get_countries()
        df_countries = pd.json_normalize(countries)

        df_countries["datetimeFirst"] = df_countries["datetimeFirst"].apply(
            lambda x: pd.Timestamp(x, tz="UTC")
        )
        df_countries["datetimeFirst"] = pd.to_datetime(
            df_countries["datetimeFirst"], utc=True, errors="coerce"
        )
        df_countries["datetimeLast"] = df_countries["datetimeLast"].apply(
            lambda x: pd.Timestamp(x, tz="UTC")
        )
        df_countries["datetimeLast"] = pd.to_datetime(
            df_countries["datetimeLast"], utc=True, errors="coerce"
        )

        df_countries["time_diff"] = (
            df_countries["datetimeLast"] - df_countries["datetimeFirst"]
        )

        df_countries["parameter_count"] = df_countries["parameters"].apply(len)

        df_countries["parameter_names"] = df_countries["parameters"].apply(
            lambda x: [i["name"] for i in x]
        )

        df_countries.to_csv(
            "countries.csv",
            index=False,
            columns=[
                "code",
                "name",
                "datetimeFirst",
                "datetimeLast",
                "time_diff",
                "parameter_count",
                "parameter_names",
            ],
        )

        return df_countries

    def fetch_locations(self, country_id: int, parameter_id: int) -> list:
        """Method that fetchs the locations from API"""
        i = 1
        locations = []
        while True:
            url = f"{self.base_url}/locations?countries_id={country_id}&parameters_id={parameter_id}&limit=100&page={i}"
            response = requests.get(url, headers=self.headers)
            data = response.json()
            try:
                results = data["results"]
            except KeyError:
                break
            if not results:
                break
            locations.extend(results)
            print(f"Page {i} fetched\r", end="")
            i += 1
        return locations

    def get_locations(self, country_id, parameter_id):
        try:
            with open(f"{country_id}_{parameter_id}_locations.json", "r") as json_file:
                data = json.load(json_file)
                locations = data["results"]
        except FileNotFoundError:
            locations = self.fetch_locations(country_id, parameter_id)
            with open(
                f"{country_id}_{parameter_id}_locations.json", "w", encoding="utf-8"
            ) as json_file:
                json.dump({"results": locations}, json_file, indent=4)
        return locations

    def process_locations(self, country_id, parameter_id):
        locations = self.get_locations(country_id, parameter_id)
        df_locations = pd.json_normalize(locations)
        return df_locations

    def fetch_measurements(self, sensor_id):
        i = 1
        measurements = []
        while True:
            url = f"{self.base_url}/sensors/{sensor_id}/measurements/daily?limit=100&page={i}"
            response = requests.get(url, headers=self.headers)
            data = response.json()
            try:
                results = data["results"]
            except KeyError:
                break
            if not results:
                break
            measurements.extend(results)
            print(f"Page {i} for sensor id {sensor_id}\r", end="")
            i += 1
        return measurements

    def get_measurements(self, sensor_id):
        try:
            with open(f"{sensor_id}_measurements.json", "r") as json_file:
                data = json.load(json_file)
                measurements = data["results"]
        except FileNotFoundError:
            measurements = self.fetch_measurements(sensor_id)
            with open(
                f"{sensor_id}_measurements.json", "w", encoding="utf-8"
            ) as json_file:
                json.dump({"results": measurements}, json_file, indent=4)
        return measurements

    def process_measurements(self, sensor_id):
        measurements = self.get_measurements(sensor_id)
        df_measurements = pd.json_normalize(measurements)
        df_measurements["period.datetimeFrom.utc"] = df_measurements[
            "period.datetimeFrom.utc"
        ].apply(lambda x: pd.Timestamp(x, tz="UTC"))
        df_measurements["period.datetimeFrom.utc"] = pd.to_datetime(
            df_measurements["period.datetimeFrom.utc"], utc=True, errors="coerce"
        )
        df_measurements["period.datetimeTo.utc"] = df_measurements[
            "period.datetimeTo.utc"
        ].apply(lambda x: pd.Timestamp(x, tz="UTC"))
        df_measurements["period.datetimeTo.utc"] = pd.to_datetime(
            df_measurements["period.datetimeTo.utc"], utc=True, errors="coerce"
        )
        df_measurements["value"] = pd.to_numeric(
            df_measurements["value"], errors="coerce"
        )
        df_measurements.to_csv(
            f"{sensor_id}_measurements.csv",
            index=False,
            columns=[
                "period.datetimeFrom.utc",
                "period.datetimeTo.utc",
                "value",
            ],
        )
        return df_measurements


if __name__ == "__main__":
    air_quality = AirQuality()
    countries = air_quality.get_countries()
    df_countries = air_quality.process_countries()
    print(df_countries.head())
    locations = air_quality.get_locations(155, 2)
    df_locations = air_quality.process_locations(155, 2)
    print(df_locations.head())
    print(df_locations.columns)
    pm25_sensors = []
    for location_id in df_locations["id"]:
        sensors = df_locations[df_locations["id"] == location_id]["sensors"]
        sensors = sensors.values[0]
        for sensor in sensors:
            sensor_id = sensor["id"]
            parameter = sensor["parameter"]
            if parameter["name"] == "pm25":
                pm25_sensors.append((location_id, sensor_id))
    for location_id, sensor_id in pm25_sensors:
        print(location_id, sensor_id)
        df_measurements = air_quality.process_measurements(sensor_id)
        input("Press enter to continue")
