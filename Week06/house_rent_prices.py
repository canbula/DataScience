import os
import time
import random
import numpy as np
import pandas as pd
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import (
    ChromeDriverManager,
)  # pip install webdriver-manager
import logging


class HouseRentPrices:
    def __init__(self, city: str, town: str, csv_lifetime: int = 1200) -> None:
        self.city = city.lower()
        self.town = town.lower()
        self.csv_lifetime = csv_lifetime
        self.csv_file = f"{self.city}_{self.town}.csv"
        self.df = None
        self.logging_init()
        logging.info(f"City: {self.city}")
        logging.info(f"Town: {self.town}")
        logging.info(f"CSV Lifetime: {self.csv_lifetime}")
        logging.info(f"CSV File: {self.csv_file}")
        if self.csv_exists() and not self.csv_is_old():
            logging.info("Reading CSV")
            self.df = pd.read_csv(self.csv_file)
        else:
            logging.info("Updating CSV")
            self.df = self.update_csv()

    def logging_init(self) -> None:
        logging.basicConfig(
            format="%(levelname)s @ %(asctime)s : %(message)s",
            datefmt="%d.%m.%Y %H:%M:%S",
            level=logging.INFO,
            force=True,
            handlers=[
                logging.FileHandler(f"{self.csv_file[:-4]}.log", mode="w"),
                logging.StreamHandler(),
            ],
        )

    def csv_exists(self) -> bool:
        return os.path.exists(self.csv_file)

    def csv_is_old(self) -> bool:
        return (time.time() - os.path.getmtime(self.csv_file)) > self.csv_lifetime

    def update_csv(self) -> None:
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        # navigator.userAgent
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        link = f"https://www.sahibinden.com/kiralik-daire/{self.city}-{self.town}?pagingSize=50"
        try:
            browser.get(link)
            logging.info(f"Link: {link} opened")
        except Exception as e:
            logging.error(e)
            browser.close()
            return
        input("Press Enter to continue...")
        time.sleep(2 + random.random())
        house_list = []
        next_page = True
        page_limit = 200
        page_count = 0
        while next_page and page_count < page_limit:
            logging.info(f"Page: {page_count} / {page_limit}")
            houses = browser.find_elements(
                by=By.CSS_SELECTOR, value=".searchResultsItem"
            )
            for h in houses:
                if h.get_attribute("data-id") is None:
                    continue
                else:
                    logging.info(f"House: {h.get_attribute('data-id')}")
                    title = h.find_elements(
                        by=By.CSS_SELECTOR, value=".searchResultsTitleValue"
                    )
                    title_text = title.find_elements(
                        by=By.CSS_SELECTOR, value=".classifiedTitle"
                    )
                    infos = h.find_elements(
                        by=By.CSS_SELECTOR, value=".searchResultsAttributeValue"
                    )
                    price = h.find_elements(
                        by=By.CSS_SELECTOR, value=".searchResultsPriceValue"
                    )
                    location = h.find_elements(
                        by=By.CSS_SELECTOR, value=".searchResultsLocationValue"
                    )
                    try:
                        house_list.append(
                            {
                                "id": h.get_attribute("data-id"),
                                "title": title_text[0].text,
                                "area": int(infos[0].text),
                                "room": int(infos[1].text.split("+")[0]),
                                "price": int(
                                    price[0].text.replace(".", "").replace("TL", "")
                                ),
                                "location": location[0].text.replace("\n", " "),
                            }
                        )
                    except Exception as e:
                        logging.error(e)
                        continue
                    finally:
                        continue

            time.sleep(2 + random.random())

            next_link = browser.find_elements(by=By.CSS_SELECTOR, value=".prevNextBut")
            next_page = False if len(next_link) == 0 else True
            for n in next_link:
                if n.get_attribute("title") == "Sonraki":
                    link = n.get_attribute("href")
                    next_page = True
                    page_count += 1
                else:
                    next_page = False
        browser.close()

        df = pd.DataFrame(house_list)
        df.to_csv(self.csv_file, index=False)
        return df


if __name__ == "__main__":
    city = "manisa"
    town = "yunusemre"
    h = HouseRentPrices(city, town)
    # print(h.df.head())
