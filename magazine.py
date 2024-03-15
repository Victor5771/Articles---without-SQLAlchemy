class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if self._articles:
            return [article.title for article in self._articles]
        else:
            return None

    def contributing_authors(self):
        if self._articles:
            authors_count = {}
            for article in self._articles:
                author = article.author
                if author in authors_count:
                    authors_count[author] += 1
                else:
                    authors_count[author] = 1
            return [author for author, count in authors_count.items() if count > 2]
        else:
            return None

    @classmethod
    def top_publisher(cls):
        if cls.all:
            return max(cls.all, key=lambda magazine: len(magazine.articles()))
        else:
            return None
