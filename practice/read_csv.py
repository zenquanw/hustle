import pandas as pd

def load(path):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    # try:
    #     df = pd.read_csv(path)
    #     return df
    # except FileNotFoundError:
    #     print(f"Error: The file at {path} was not found.")
    #     return None
    # except pd.errors.EmptyDataError:
    #     print("Error: The file is empty.")
    #     return None
    # except pd.errors.ParserError:
    #     print("Error: There was a parsing error while reading the file.")
    #     return None
    for enc in ("utf-8","gbk"):
        try:
            return pd.read_csv(path,encoding=enc)
        except FileNotFoundError:
            print(f"找不到文件:{path}")
            return None
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"读取出错：{e}")
            return None
    print (f"utf-8和gbk都读取不了：{path}")
    return None

def report(df):
    print("行数",df.shape[0],"列数",df.shape[1])
    print("每列空缺：")
    print(df.isna().sum())


    print("\n字段类型：")
    df.info()                       # info() 自带打印，别套 print

    print("\n数值列统计：")
    print(df.describe())

    print("\n各部门条数（含空缺）：")
    print(df["部门"].value_counts(dropna=False))

    print("\n金额大于 100 的记录：")
    print(df.loc[df["金额"] > 100, ["姓名", "金额"]])

    print("\n金额最高的 3 条：")
    print(df.sort_values("金额", ascending=False).head(3))


if __name__ == "__main__":
    df = load("practice/data/sample_gbk.csv")
    if df is not None:
        report(df)


