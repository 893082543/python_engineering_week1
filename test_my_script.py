import pandas as pd
import pytest

from week1 import count_rows, filter_data, read_data


def test_read_data_normal():
    """正常情况：文件存在且格式正确。"""
    df = read_data("test_sample.csv")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_filter_data_no_match():
    """边界情况：筛选条件没有任何匹配。"""
    df = pd.DataFrame({"region": ["华东", "华北"], "amount": [100, 200]})
    result = filter_data(df, "region", "华南")
    assert len(result) == 0


def test_read_data_file_not_found():
    """异常情况：文件不存在时应抛出 FileNotFoundError。"""
    with pytest.raises(FileNotFoundError):
        read_data("this_file_does_not_exist.csv")
