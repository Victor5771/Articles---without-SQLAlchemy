class Article:
    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine

        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise TypeError("Author and magazine must be instances of Author and Magazine classes")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

