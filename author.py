class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        categories = []
        for article in self._articles:
            categories.append(article.magazine.category)
        return list(set(categories)) if categories else None
