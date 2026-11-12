import pandas as pd

def load(path):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None

def report(df):
    print("行数",df.shape[0],"列数",df.shape[1])
    print("每列空缺：")
    print(df.isna().sum())

if __name__ == "__main__":
    df = load("practice/data/sample.csv")
    if df is not None:
        report(df)