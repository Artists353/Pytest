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


#Моки и заглушки (monkeypatch, unittest.mock)
#Позволяют подменять функции и переменные во время тестирования.  
def get_api_data():
    return {"result": 42}

def test_api_mock(monkeypatch):
    def mock_data():
        return {"result": 100}

    monkeypatch.setattr("test_example.get_api_data", mock_data)
    assert get_api_data()["result"] == 100

#Ожидание исключений (pytest.raises)
#Иногда мы хотим проверить, что код действительно вызывает ошибку.
def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


#Маркировка тестов (@pytest.mark)
#Позволяет запускать определённые группы тестов.
@pytest.mark.slow
def test_heavy_computation():
    import time
    time.sleep(5)
    assert 2 + 2 == 4

#Параметризация тестов (@pytest.mark.parametrize)
#Позволяет запускать один и тот же тест с разными входными данными.
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0)
])
def test_addition(a, b, expected):
    assert a + b == expected