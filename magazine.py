from article import Article

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise TypeError("Name and category must be strings")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must not be empty")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        return [author for author, count in author_count.items() if count > 2]

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    @classmethod
    def top_publisher(cls):
        magazines = cls.all_magazines()
        if not magazines:
            return None
        return max(magazines, key=lambda magazine: len(magazine._articles))
