import numpy as np
import pandas as pd
import os


def combine_csv_files_into_one_from_a_folder(folder: str, output_file: str) -> None:
    csv_files = [file for file in os.listdir(folder) if file.endswith(".csv")]
    df = pd.concat([pd.read_csv(f"{folder}/{file}") for file in csv_files])
    df.to_csv(output_file, index=False, header=False)


if __name__ == "__main__":
    combine_csv_files_into_one_from_a_folder("csv_files", "manisa_yunusemre.csv")
