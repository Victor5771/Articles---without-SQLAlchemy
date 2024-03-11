# tests/test_author.py

from author import Author
from magazine import Magazine
import pytest

def test_author_init():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_author_name_type():
    with pytest.raises(TypeError):
        Author(123)

def test_author_name_length():
    with pytest.raises(ValueError):
        Author("")

def test_author_name_immutable():
    author = Author("John Doe")
    with pytest.raises(AttributeError):
        author.name = "Jane Doe"

def test_author_articles():
    author = Author("John Doe")
    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")
    article1 = author.add_article(magazine1, "Article 1")
    article2 = author.add_article(magazine2, "Article 2")
    assert author.articles() == [article1, article2]

def test_author_magazines():
    author = Author("John Doe")
    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")
    author.add_article(magazine1, "Article 1")
    author.add_article(magazine2, "Article 2")
    assert author.magazines() == [magazine1, magazine2]

def test_author_topic_areas():
    author = Author("John Doe")
    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")
    author.add_article(magazine1, "Article 1")
    author.add_article(magazine2, "Article 2")
    assert author.topic_areas() == ["Category 1", "Category 2"]
