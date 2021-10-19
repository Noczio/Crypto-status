import pandas as pd
from resources.save import save_to_disk


def is_integer(n) -> bool:
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.drop(["Unnamed: 0", "#", "Last 7 Days", "Unnamed: 10"], axis=1)
    cleaned_df = cleaned_df.dropna()

    for index in cleaned_df.index:
        value = cleaned_df.loc[index, "Name"]
        new_value_list = []
        for char in value:
            if is_integer(char):
                break
            new_value_list.append(char)
        cleaned_df.loc[index, "Name"] = "".join(new_value_list)

    return cleaned_df


def save_info(df: pd.DataFrame) -> None:
    columns = list(df.columns.values)
    for index in df.index:
        crypto_name = df.loc[index, "Name"]
        data = dict(df.loc[index, columns])
        for key, value in data.items():
            print(key, value)
        print("")
        path = ".\\results"
        save_to_disk(path, crypto_name, data)


def run():
    url = "https://coinmarketcap.com/"
    table = pd.read_html(url)
    df = table[0]
    crypto_df = clean_df(df)
    save_info(crypto_df)
    input("Type any key to exit ... ")


if __name__ == "__main__":
    run()
