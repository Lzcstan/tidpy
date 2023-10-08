import tidpy

def test_greet():
    assert tidpy.greet("Alice") == "Hello, Alice!"
    assert tidpy.greet("Bob") == "Hello, Bob!"

def test_is_palindrome():
    assert tidpy.is_palindrome("radar") is True
    assert tidpy.is_palindrome("python") is False

def test_multiply():
    assert tidpy.multiply(3, 5) == 15
    assert tidpy.multiply(0, 10) == 0
    assert tidpy.multiply(-2, 4) == -8