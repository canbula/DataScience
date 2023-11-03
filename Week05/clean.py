from typing import Any
import numpy as np
import pandas as pd
import os


class Clean:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file, delimiter=",", header=0)

    def __enter__(self):
        print("Cleaning started!")
        # replace all empty cells with NaN
        self.df.replace("", pd.NA, inplace=True)
        # drop rows if all values are NaN
        self.df.dropna(how="all", inplace=True)
        # remove the rows if all values are duplicated
        self.df.drop_duplicates(inplace=True)
        # reset the index
        self.df.reset_index(drop=True, inplace=True)
        # parse the age column as numeric, so replace non-numeric values with NaN
        self.df["age"] = pd.to_numeric(self.df["age"], errors="coerce")
        self.df["math_score"] = pd.to_numeric(self.df["math_score"], errors="coerce")
        self.df["reading_score"] = pd.to_numeric(
            self.df["reading_score"], errors="coerce"
        )
        # replace NaN with mean / median / mode
        self.df["age"].fillna(self.df["age"].median(), inplace=True)
        self.df["math_score"].fillna(self.df["math_score"].median(), inplace=True)
        self.df["reading_score"].fillna(self.df["reading_score"].median(), inplace=True)
        # convert the age column to int, and math_score and reading_score to float
        self.df["age"] = self.df["age"].astype(int)
        self.df["math_score"] = self.df["math_score"].astype(float)
        self.df["reading_score"] = self.df["reading_score"].astype(float)
        # drop rows if any value is NaN
        self.df.dropna(how="any", inplace=True)
        # reset the index
        self.df.reset_index(drop=True, inplace=True)
        # drop id column as it is not needed
        self.df.drop("id", axis=1, inplace=True)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning finished!")

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.df


if __name__ == "__main__":
    file_path = f"{os.path.dirname(os.path.realpath(__file__))}/dirty_data.csv"
    with Clean(file_path) as clean:
        clean_df = clean()
    print(clean_df)
