from credentials import API_KEY
import requests
import json
import numpy as np
import pandas as pd


class AirQuality:
    def __init__(self):
        self.__base_url = "https://api.openaq.org/v3"
        self.__headers = {"accept": "application/json", "X-API-KEY": API_KEY}
        self.__countries = []

    def __fetch_countries(self):
        i = 1
        while True:
            url = f"{self.__base_url}/countries?limit=100&page={i}"
            response = requests.get(url, headers=self.__headers)
            data = response.json()
            countries = data["results"]
            if not countries:
                break
            self.__countries.extend(countries)
            i += 1
        return self.__countries

    def get_countries(self):
        try:
            with open("countries.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                self.__countries = data["results"]
        except FileNotFoundError:
            self.__countries = self.__fetch_countries()
            with open("countries.json", "w", encoding="utf-8") as json_file:
                json.dump({"results": self.__countries}, json_file, indent=4)
        return self.__countries

    def process_countries(self):
        countries = self.get_countries()
        df_countries = pd.json_normalize(countries)
        df_countries.to_csv("countries.csv", index=False)
        return df_countries


if __name__ == "__main__":
    air_quality_obj = AirQuality()
    countries = air_quality_obj.get_countries()
    print(f"Total Countries: {len(countries)}")
    """
    input()
    for country in countries:
        print(country)
    """
    df_countries = air_quality_obj.process_countries()
    print(df_countries.head(10))
    print(df_countries.info())
