import requests
import pytest


# ===== БИЗНЕС-ЛОГИКА =====
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def is_prime_number(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


# ===== UNIT-ТЕСТЫ =====
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)


@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (4, False),
    (1, False)
])
def test_is_prime(number, expected):
    calc = Calculator()
    assert calc.is_prime_number(number) == expected


# ===== API-ТЕСТ =====
def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "name" in data
 
 