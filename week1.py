import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def read_data(file_path: str) -> pd.DataFrame:
    """读取 CSV 文件，失败时记录日志并抛出明确异常。"""
    logger.info(f"开始读取文件：{file_path}")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"读取成功，行数：{len(df)}")
        return df
    except FileNotFoundError:
        logger.error(f"文件不存在：{file_path}")
        raise
    except pd.errors.EmptyDataError:
        logger.error(f"文件为空或格式不正确：{file_path}")
        raise


def filter_data(df: pd.DataFrame, column: str, value: str) -> pd.DataFrame:
    """按指定列和值筛选数据。"""
    return df[df[column] == value]


def count_rows(df: pd.DataFrame) -> int:
    """返回行数。"""
    return len(df)


if __name__ == "__main__":
    data = read_data("sales.csv")
    filtered = filter_data(data, "region", "华东")
    print(f"筛选后行数：{count_rows(filtered)}")
