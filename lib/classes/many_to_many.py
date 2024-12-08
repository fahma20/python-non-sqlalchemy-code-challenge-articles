class Article:
    all = []  # To track all articles globally

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        # Track article globally
        Article.all.append(self)

        # Add article to author's list of articles and magazine's list of articles only if not already present
        if self not in author._articles:
            author._articles.append(self)
        if self not in magazine._articles:
            magazine._articles.append(self)

        # Add the magazine to the author's set of magazines
        author._magazines.add(magazine)

        # Add the author to the magazine's set of authors
        magazine._authors.add(author)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be an instance of Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # To store articles authored
        self._magazines = set()  # To store magazines this author has contributed to

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        # Return a unique list of magazines by converting set to list
        return list(self._magazines)

    def add_article(self, magazine, title):
        """Accepts a Magazine instance, and a title, creates an article, and associates it with the author and magazine."""
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        """Returns a unique list of strings with the categories of magazines the author has contributed to."""
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self._magazines))


class Magazine:
    all = []  # To keep track of all magazines globally

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []  # To store articles related to this magazine
        self._authors = set()  # To store authors who have written for this magazine
        Magazine.all.append(self)  # Add this magazine to the global list

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(self._authors)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Return authors who have written more than 2 articles for this magazine."""
        authors = [author for author in self._authors if len([article for article in author.articles() if article.magazine == self]) > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles."""
        if not cls.all or not any(magazine.articles() for magazine in cls.all):
            return None  # Return None if no articles exist in any magazine
        return max(cls.all, key=lambda magazine: len(magazine._articles))  # Return the magazine with the most articles

    def add_article(self, author, magazine, title):
        """Accepts author, magazine, and title to create and add an article to the magazine's list."""
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")

        # Create the article
        article = Article(author, magazine, title)

        # Add the article to this magazine and the author's list
        self._articles.append(article)
        self._authors.add(author)
