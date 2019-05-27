Title: Recommender System made easy with Scikit-Surprise
Date: 2019-04-21 7:25:50
Category: Blog
Tags: python, scikit-surprise, recommenders system
Slug: Recommender System made easy with Scikit-Surprise



A recommender system is a subclass of information filtering system that seeks to predict the “rating” or “preference” a user would give to…

----------

**Recommender System made easy with Scikit-Surprise**

![](https://cdn-images-1.medium.com/max/800/0*U5XCg4kAJTynDzNb.png)

https://www.offerzen.com/blog/how-to-build-a-content-based-recommender-system-for-your-product

- Collaborative filtering
- Content-based filtering
- Hybrid recommender system

In this tutorial, I’ll be focusing on Collaborative filtering. In Collaborative filtering, the model learns from the user’s past behavior, user’s decision, preference to predict items the user might have an interest in.
Scikit-Surprise is an easy-to-use Python scikit for recommender systems, another example of python scikit is Scikit-learn which has lots of awesome estimators. To install surprise, type this on your CMD/Terminal

    pip install scikit-surprise

**Preprocessing**
The first thing is to preprocess our data. We have to check the shape, description, a number of unique value, columns and analyze to get more insights from our data.
loading data with pandas
from the snippet above you can I see I loaded my data with pandas then check the first few rows. We have four columns *userId, moveId, rating and timestamp,* and checked the value counts of *rating.* From here we can see rating of 4.0 has highest value counts. This means more people rated the movie 4.0 has shown in the plot below.
Now I have to check the number of null value in my data.
To load a dataset from a pandas dataframe, you will need the `**load_from_df()**` method. You will also need a `**Reader**` object, but only the `rating_scale` the parameter must be specified the default rating_scaale is (2,5). The dataframe must have three columns, corresponding to the user (raw) ids, the item (raw) ids, and the ratings in this order.
The next step is splitting our dataset in train and test set in a ratio of 75%:25%
I will train with trainset and test with testset.
I’ll be using the famous SVD algorithm, as popularized by [Simon Funk](http://sifter.org/~simon/journal/20061211.html) during the Netflix Prize. SVD is a Matrix Factorization techniques are usually more effective because they allow us to discover the latent features underlying the interactions between users and items.
**Evaluation**
Singular vector decomposition (SVD) shown here employs the use of gradient descent to minimize the squared error between predicted rating and actual rating, eventually getting the best model.
You can perform Cross-validation and heavy hyperparameters tuning with surprise to get more accurate predictions.
I love feedback please let me know what you think  and share this post with friends and colleagues. You can get access to the full code [here](https://github.com/hammedb197/Recommender-surprise)
Thanks for reading!
Resources :
[**Recommender system - Wikipedia**](https://en.wikipedia.org/wiki/Recommender_system)
[*The majority of existing approaches to recommender systems focus on recommending the most relevant content to users…*](https://en.wikipedia.org/wiki/Recommender_system)[en.wikipedia.org](https://en.wikipedia.org/wiki/Recommender_system)
Data source: [https://grouplens.org/datasets/movielens/100k/](https://grouplens.org/datasets/movielens/100k/)
Link to surprise documentation: [https://surprise.readthedocs.io/en/stable/index.html](https://surprise.readthedocs.io/en/stable/index.html)

