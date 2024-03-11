# tests/test_magazine.py

from magazine import Magazine
import pytest

def test_magazine_init():
    magazine = Magazine("Magazine 1", "Category 1")
    assert magazine.name == "Magazine 1"
    assert magazine.category == "Category 1"

def test_magazine_name_type():
    with pytest.raises(TypeError):
        Magazine(123, "Category 1")

def test_magazine_name_length():
    with pytest.raises(ValueError):
        Magazine("", "Category 1")

def test_magazine_category_type():
    with pytest.raises(TypeError):
        Magazine("Magazine 1", 123)

def test_magazine_category_length():
    with pytest.raises(ValueError):
        Magazine("Magazine 1", "")

def test_magazine_name_change():
    magazine = Magazine("Magazine 1", "Category 1")
    magazine.name = "New Magazine Name"
    assert magazine.name == "New Magazine Name"

def test_magazine_category_change():
    magazine = Magazine("Magazine 1", "Category 1")
    magazine.category = "New Category"
    assert magazine.category == "New Category"
