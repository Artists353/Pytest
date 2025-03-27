import pytest 

def num():
    assert 1 + 2 == 2

@pytest.fixture
def prepare_data():
    return {'Name': 45, 
            'Jonh':  67,
}


def test_prepare_data():
    assert prepare_data['Name'] == 47
    assert prepare_data['Jonh'] == 67
    