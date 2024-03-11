# tests/test_article.py

from author import Author
from magazine import Magazine
from article import Article
import pytest

def test_article_init():
    author = Author("John Doe")
    magazine = Magazine("Magazine 1", "Category 1")
    article = Article(author, magazine, "Article Title")
    assert article.title == "Article Title"
    assert article.author == author
    assert article.magazine == magazine

def test_article_title_type():
    author = Author("John Doe")
    magazine = Magazine("Magazine 1", "Category 1")
    with pytest.raises(TypeError):
        Article(author, magazine, 123)

def test_article_title_length():
    author = Author("John Doe")
    magazine = Magazine("Magazine 1", "Category 1")
    with pytest.raises(ValueError):
        Article(author, magazine, "")

def test_article_title_immutable():
    author = Author("John Doe")
    magazine = Magazine("Magazine 1", "Category 1")
    article = Article(author, magazine, "Article Title")
    with pytest.raises(AttributeError):
        article.title = "New Title"

def test_article_author_change():
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine = Magazine("Magazine 1", "Category 1")
    article = Article(author1, magazine, "Article Title")
    article.author = author2
    assert article.author == author2

def test_article_magazine_change():
    author = Author("John Doe")
    magazine1 = Magazine("Magazine 1", "Category 1")
    magazine2 = Magazine("Magazine 2", "Category 2")
    article = Article(author, magazine1, "Article Title")
    article.magazine = magazine2
    assert article.magazine == magazine2
