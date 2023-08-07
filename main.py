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


df = calculate_ratios(2000)
print(df)
