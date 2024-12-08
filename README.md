# Magazine-Article-Author Management System

This is a Python-based system that manages the relationships between Authors, Magazines, and Articles. The system allows authors to contribute articles to magazines, track those contributions, and categorize them by topic areas. It also provides functionality to retrieve the magazine with the most articles.

## Features

### Author
- Authors can create articles, and each article is linked to the author.
- Authors can view the list of magazines they’ve contributed to.
- Authors can retrieve a list of unique topic areas from the magazines they’ve written for.
- Authors can add articles to magazines using the `add_article(magazine, title)` method, where the magazine is an instance of the `Magazine` class and the title is a string.

### Magazine
- Magazines can store articles.
- Magazines can list their contributors (authors).
- Magazines can return the list of titles for articles written for them.
- Magazines can return a list of authors who have written more than two articles for the magazine.
- The system can retrieve the magazine with the most articles using the `top_publisher()` method.

### Article
- Articles are associated with both an author and a magazine.
- Articles have a title that must be between 5 and 50 characters long.
- Articles are linked to both the author and the magazine upon creation.

## Requirements

- Python 3.x
- pytest (for running tests)

## Classes Overview

### Article

Represents an article written by an author and published in a magazine.

#### Properties:
- `author`: The author of the article.
- `magazine`: The magazine in which the article is published.
- `title`: The title of the article (must be between 5 and 50 characters).

#### Methods:
- `__init__(author, magazine, title)`: Initializes an article with an author, magazine, and title. The article is added to both the author's and magazine's lists of articles.
- `all`: A class attribute that stores all created articles.

---

### Author

Represents an author who writes articles for different magazines.

#### Properties:
- `name`: The name of the author.
- `articles()`: A list of articles written by the author.
- `magazines()`: A list of unique magazines the author has contributed to.

#### Methods:
- `__init__(name)`: Initializes an author with a name.
- `add_article(magazine, title)`: Creates and adds an article to the author’s list of articles and the magazine's list of articles.
- `topic_areas()`: Returns a unique list of topic areas (categories of magazines the author has written for). Returns `None` if the author has no articles.

---

### Magazine

Represents a magazine that publishes articles from different authors.

#### Properties:
- `name`: The name of the magazine.
- `category`: The category or topic area of the magazine (e.g., Fashion, Architecture).
- `articles()`: A list of articles published in the magazine.
- `contributors()`: A list of authors who have written articles for the magazine.

#### Methods:
- `__init__(name, category)`: Initializes a magazine with a name and category.
- `article_titles()`: Returns a list of the titles of all articles written for the magazine. Returns `None` if the magazine has no articles.
- `contributing_authors()`: Returns a list of authors who have written more than two articles for the magazine. Returns `None` if there are no authors with more than two publications.
- `top_publisher()`: Returns the magazine with the most articles. Returns `None` if there are no articles.

## Running Tests with pytest

To run the tests, you can use `pytest`. It will automatically discover and execute all tests within the tests directory or any files that start with `test_` or end with `_test.py`.

### Install pytest

If `pytest` is not already installed, run the following command:

pip install pytest

## **Contributing**
We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Clone your fork to your local machine.
3. Create a new branch to work on your changes.
4. Make your changes and ensure the code works as expected.
5. Commit your changes and push them to your forked repository.
6. Create a pull request from your fork to the main repository.
7. We will review your changes and, if everything looks good, merge them into the main branch.

---

## **License**
This project is licensed under the MIT License.

---

## **Note**
This system is designed to help manage articles written by authors and published in magazines, with basic validation for article titles, authorship, and magazine contributions. You can extend this system by adding more functionality or improving the design as needed.
