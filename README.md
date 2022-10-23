# Application for articles

## Launch instruction

**1. Start web application**
Clone the repository

Install requirements

Execute the following command:

    uvicorn app.main:app

**2. Start gRPC server**

Go into grpc_files directory and execute the following command:

    python3 server.py

**3. Start RabbitMQ**

Go into root directory and execute the following command:

    docker compose up

## 1. Business cases

Users can view and add articles. When user tries to add article, he must pass originally level. Also the DB has to have free space for new articles.

## 2. Functionality

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

**Check for subscribe status**

To check if subscribe of a user is expired, visit the following:

    /check_subscribe/{user_id}

Available users ids:
* 0  (Active)
* 1  (Expire)
* 2  (Active)
* 3  (Active)

To extend subscrib for current user, visit the following:

    /extend_subscribe/{user_id}

**Use gRPC for sum evaluation**

To use gRPC route, visit the following:

    /check_grpc?n1=<int number>&n2=<int number>

**Use RabbitMQ to check publications**

Business case consists of two services: the first one is the news feed for readers and the second is links base. Both services react to a new published article. The goal of news feed is to show subscribed users announcements about recently published articles. The goal of the links base updater service is to update articles reference base.

News fed works only for users with active subscribe. See the "Check for subscribe status" above to see which user has active subscribe by default.

To publish new article visit the following route:

    /publish_new_article

To check message for user, visit the following route:

    /check_for_article?user_id=<int number>

See the "Check for subscribe status" above to see available users id.

To see request to update links base, visit the following route:

    /check_for_article_links

## 3. Tests

Package name of the chosen testing module: PyTest.

**How to run tests**

Go into root directory and run the following:

    pytest tests.py
