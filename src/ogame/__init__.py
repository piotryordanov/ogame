import pandas as pd


def calculate_ratios(lm):
    ratios = {
        "lm": lm,
        "las_légers": lm / 100 * 75,
        "las_lourds": lm / 100 * 30,
        "gauss": lm / 100 * 10,
        "ions": lm / 100 * 10,
        "plasmas": lm / 100 * 5,
    }
    return pd.DataFrame([ratios])


def main():
    df = calculate_ratios(200000)
    print(df)


def trade():
    metal = 50
    deut = 15

    cri = (1.8 / 2.4) * metal + deut * 1.8
    print(cri)
