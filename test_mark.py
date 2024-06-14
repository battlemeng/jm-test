import pytest

from utils.read_data import get_data

@pytest.mark.parametrize("name", get_data()['hero_list1'])
def test_parametrizee_01(name):
    print(name)




