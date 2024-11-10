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


if __name__ == "__main__":
    air_quality = AirQuality()
    countries = air_quality.get_countries()
    df_countries = air_quality.process_countries()
    print(df_countries.head())
