import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, render_template, request, redirect, url_for
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import io
import base64
from scipy.stats import norm


class AnalyzeRents:
    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file
        self.df = pd.read_csv(
            self.csv_file,
            names=[
                "title",
                "area",
                "rooms",
                "price",
                "location",
                "to_be_deleted",
            ],
            dtype={
                "title": str,
                "area": str,
                "rooms": str,
                "price": str,
                "location": str,
                "to_be_deleted": str,
            },
        )

    def clean_df(self) -> None:
        self.df.dropna(how="all", inplace=True)
        self.df.drop_duplicates(inplace=True)
        self.df.reset_index(inplace=True, drop=True)
        self.df.drop(columns=["to_be_deleted"], inplace=True)
        self.df["area"] = self.df["area"].apply(lambda x: int(x.split(".")[0]))
        self.df["rooms"] = self.df["rooms"].apply(
            lambda x: int(x.split("+")[0].split(".")[0])
        )
        self.df["price"] = self.df["price"].apply(
            lambda x: int(x.replace(".", "").replace("TL", ""))
        )
        self.df["location"] = self.df["location"].apply(
            lambda x: x.replace("Merkez", "").strip()
        )


app = Flask(__name__)
matplotlib.use("agg")


def init_app():
    analyze_rents = AnalyzeRents("manisa_yunusemre.csv")
    analyze_rents.clean_df()
    global df
    df = analyze_rents.df
    print(df.head())
    print(df.info())


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html",
        title="Data Visualization Web Application",
        data_table=df.to_html(),
        price_histogram=price_histogram(),
        area_histogram=area_histogram(),
        rooms_histogram=rooms_histogram(),
        price_by_area=price_by_area(),
        price_by_rooms=price_by_rooms(),
        price_by_area_and_rooms=price_by_area_and_rooms(),
        stats=get_stats(),
        frequency_table_of_locations=frequency_table_of_locations(),
    )


def get_stats():
    return {
        "average_price": f"{np.round(np.mean(df['price'])):.0f} TL",
        "average_area": f"{np.round(np.mean(df['area'])):.0f} m2",
        "average_rooms": f"{np.round(np.mean(df['rooms'])):.0f}",
        "min_price": f"{np.min(df['price']):.0f} TL",
        "max_price": f"{np.max(df['price']):.0f} TL",
        "min_area": f"{np.min(df['area']):.0f} m2",
        "max_area": f"{np.max(df['area']):.0f} m2",
        "min_rooms": f"{np.min(df['rooms']):.0f}",
        "max_rooms": f"{np.max(df['rooms']):.0f}",
        "median_price": f"{np.median(df['price']):.0f} TL",
        "median_area": f"{np.median(df['area']):.0f} m2",
        "median_rooms": f"{np.median(df['rooms']):.0f}",
        "mean_price": f"{np.mean(df['price']):.0f} TL",
        "mean_area": f"{np.mean(df['area']):.0f} m2",
        "mean_rooms": f"{np.mean(df['rooms']):.0f}",
        "std_price": f"{np.std(df['price']):.0f} TL",
        "std_area": f"{np.std(df['area']):.0f} m2",
        "std_rooms": f"{np.std(df['rooms']):.0f}",
    }


def price_histogram():
    fig = plt.figure(figsize=(12, 5))
    sns.histplot(x="price", data=df, kde=True)
    plt.xlabel("Price [TL]")
    min_price = int(5000 * (np.min(df["price"]) // 5000))
    max_price = int(5000 * (np.max(df["price"]) // 5000 + 1))
    plt.xlim(min_price, max_price)
    plt.xticks(rotation=0, ticks=range(min_price, max_price, 5000))
    plt.ylabel("Count")
    plt.title("Histogram of Prices")
    plt.grid(True)
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def area_histogram():
    fig = plt.figure(figsize=(12, 5))
    sns.histplot(x="area", data=df, kde=True)
    plt.xlabel("Area [m2]")
    min_area = int(50 * (np.min(df["area"]) // 50))
    max_area = int(50 * (np.max(df["area"]) // 50 + 1))
    plt.xlim(min_area, max_area)
    plt.xticks(rotation=0, ticks=range(min_area, max_area, 50))
    plt.ylabel("Count")
    plt.title("Histogram of Areas")
    plt.grid(True)
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def rooms_histogram():
    fig = plt.figure(figsize=(12, 5))
    sns.histplot(x="rooms", data=df, kde=True)
    plt.xlabel("Rooms")
    min_rooms = int(1 * (np.min(df["rooms"]) // 1))
    max_rooms = int(1 * (np.max(df["rooms"]) // 1 + 1))
    plt.xlim(min_rooms, max_rooms)
    plt.xticks(rotation=0, ticks=range(min_rooms, max_rooms, 1))
    plt.ylabel("Count")
    plt.title("Histogram of Rooms")
    plt.grid(True)
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def price_by_area():
    fig = plt.figure(figsize=(12, 5))
    sns.scatterplot(x="area", y="price", data=df, hue="rooms")
    plt.xlabel("Area [m2]")
    min_area = int(50 * (np.min(df["area"]) // 50))
    max_area = int(50 * (np.max(df["area"]) // 50 + 1))
    plt.xlim(min_area, max_area)
    plt.xticks(rotation=0, ticks=range(min_area, max_area, 50))
    plt.ylabel("Price [TL]")
    min_price = int(5000 * (np.min(df["price"]) // 5000))
    max_price = int(5000 * (np.max(df["price"]) // 5000 + 1))
    plt.ylim(min_price, max_price)
    plt.yticks(rotation=0, ticks=range(min_price, max_price, 5000))
    plt.title("Price by Area")
    plt.grid(True)
    x = df["area"].values.reshape(-1, 1)
    y = df["price"].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color="red")
    plt.text(
        0.05,
        0.90,
        f"y = {model.coef_[0][0]:.0f}x + {model.intercept_[0]:.0f}",
        transform=plt.gca().transAxes,
        bbox=dict(facecolor="yellow", alpha=0.8),
    )
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def price_by_rooms():
    fig = plt.figure(figsize=(12, 5))
    sns.scatterplot(x="rooms", y="price", data=df, hue="area")
    plt.xlabel("Rooms")
    min_rooms = int(1 * (np.min(df["rooms"]) // 1))
    max_rooms = int(1 * (np.max(df["rooms"]) // 1 + 1))
    plt.xlim(min_rooms, max_rooms)
    plt.xticks(rotation=0, ticks=range(min_rooms, max_rooms, 1))
    plt.ylabel("Price [TL]")
    min_price = int(5000 * (np.min(df["price"]) // 5000))
    max_price = int(5000 * (np.max(df["price"]) // 5000 + 1))
    plt.ylim(min_price, max_price)
    plt.yticks(rotation=0, ticks=range(min_price, max_price, 5000))
    plt.title("Price by Rooms")
    plt.grid(True)
    x = df["rooms"].values.reshape(-1, 1)
    y = df["price"].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.plot(x, y_pred, color="red")
    plt.text(
        0.05,
        0.90,
        f"y = {model.coef_[0][0]:.0f}x + {model.intercept_[0]:.0f}",
        transform=plt.gca().transAxes,
        bbox=dict(facecolor="yellow", alpha=0.8),
    )
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def price_by_area_and_rooms():
    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(df["area"], df["rooms"], df["price"])
    ax.set_xlabel("Area [m2]")
    ax.set_ylabel("Rooms")
    ax.set_zlabel("Price [TL]")
    ax.grid(True)
    x = df[["area", "rooms"]]
    y = df["price"]
    model = LinearRegression()
    model.fit(x, y)
    xx, yy = np.meshgrid(
        np.linspace(np.min(df["area"]), np.max(df["area"]), 10),
        np.linspace(np.min(df["rooms"]), np.max(df["rooms"]), 10),
    )
    zz = model.intercept_ + model.coef_[0] * xx + model.coef_[1] * yy
    ax.plot_surface(xx, yy, zz, alpha=0.5)
    ax.text2D(
        0.05,
        0.95,
        f"z = {model.coef_[0]:.0f}x + {model.coef_[1]:.0f}y + {model.intercept_:.0f}",
        transform=ax.transAxes,
        bbox=dict(facecolor="yellow", alpha=0.8),
    )
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


def frequency_table_of_locations():
    location_counts = {}
    for l in df["location"]:
        if l in location_counts:
            location_counts[l] += 1
        else:
            location_counts[l] = 1
    sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)
    top_5 = sorted_locations[:5]
    other = sorted_locations[5:]
    new_location_counts = {}
    for l in top_5:
        new_location_counts[l[0]] = l[1]
    other_count = 0
    for l in other:
        other_count += l[1]
    new_location_counts["Other"] = other_count
    df_location_counts = pd.DataFrame.from_dict(
        new_location_counts, orient="index", columns=["Count"]
    )
    fig = plt.figure(figsize=(12, 5))
    plt.pie(
        df_location_counts["Count"],
        labels=df_location_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Frequency of Locations")
    img = io.BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode("utf-8")


if __name__ == "__main__":
    with app.app_context():
        init_app()
    app.run(debug=True)
