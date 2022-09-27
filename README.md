# Application for articles

## 1. Functionality

**View articles**

To view all articles, visit the

    /articles

To see certain topic, visit the

    /articles/<str art_topic>

where's \<str art_topic\> can take "Web", "IT" and "NN" values.

To view limited amount of articles, visit the

    /articles/<str art_topic>?number=<int number>

**Check available topics**

To check available topics, isit the following endpoint in docs:

    /cgeck_topic/{topic_name}

**Add articles**

To add article, visit the following endpoint in docs:

    /articles/add

Be attentive, your article must pass originality level. Besides, there may be no space in the database.

## 2. Tests

Package name of the chosen testing module: PyTest.

**How to run tests**

Go into root directory and run the following:

    pytest tests.py
