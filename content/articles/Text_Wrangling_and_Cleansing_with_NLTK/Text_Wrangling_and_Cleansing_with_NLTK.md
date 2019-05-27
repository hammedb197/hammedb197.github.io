Title: Text Wrangling and Cleansing with NLTK
Date: 2019-04-21 7:25:50
Category: Blog
Tags: python, nltk, text preprocessing, NLP
Slug: Text Wrangling and Cleansing with NLTK

Text processing is done in order to put text in a readable format for a machine. Text preprocessing is a very important part of our text…

----------

**Text Wrangling and Cleansing with NLTK**

![](https://cdn-images-1.medium.com/max/800/0*j9FKv2WnvVFNxU5Q.jpeg)


Text processing is done in order to put text in a readable format for a machine. Text preprocessing is a very important part of our text classification task, it helps us understand our data better and get better insight from the data.

![](https://cdn-images-1.medium.com/max/1200/0*V-a-_0P2fd21-N3h.png)


Text preprocessing includes the following:

1. Tokenization
2. Lemmatization
3. Stemming
4. Stopword removal

Before we start our text preprocessing the first step is to load our data from its data source. Data source include CSV, HTML, XML, Database, JSON, NoSQL, PDF and so on. Data from the data source can be parsed using various python parsers like import CSV, import HTML parser, import json. Snippet below shows how you can read a file in CSV and JSON format.
**Text Cleansing**
Once we have parsed the text from our data sources, the challenge is to
make sense of raw data. Our aim is to remove all the noise surrounding the text.
**Tokenization**
This is the process of splitting large raw text into many pieces. A token is a minimal unit that a machine can understand. A text could be tokenized into sentences and words. In sentence tokenization, each sentence is seen as a unit likewise in word tokenization.
Tokenization can come in different ways but the most common one is the word tokenization. In word tokenization texts are broken than into words which serves a the minimal unit. Tokenization modules in nltk include:
- word_tokenizer
- sent_tokenizer
-punkt_tokenizer
- Regexp_tokenizer
-TreebankWord_Tokenizer
Customized to tokenization could be done using regex_tokenize, Tokenization could also be done using split from regex
re.split(‘/W+’, string).
word_tokenize
**Stemming**
Stemming is the process of cutting down the branche of a tree to
its stem. So basically stemming is the breaking down of a token to its basic form. A typical example is the use of **eat** in a sentence which has other variations like eating, eaten, eats, and so on.
In nltk we can use LancasterStemmer, SnowballStemmer, PorterStemmer, the major difference between the trio is that Lancaster algorithm is very aggressive so sometimes it over stem certain words while PorterStemmer is less aggressive. SnowballStemmer is language designed, it can be used in several languages. To import each of these stemmers you type from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer.
Text before stemming
here I’ll be using SnowballStemmer:
Text after stemming
We are creating different stemmer objects and applying a stem() method on the string.
**Lemmatization**
Lemmatization is a more complex way of converting all the grammatical
forms of the root of the word. Lemmatization uses context and part of speech to determine the inflected form of the word. Lemmatization uses WordNet which is like a dictionary to search for the context, then transform. So if you are interested in getting the context of the word it’s better to use lemmatization.
As you can see this is better than stemming, the next step is the removal of stopwords.
**Stopword removal**
This is simply removing the words like ‘the’, ‘is’, ‘are’ that occur commonly across a corpus. Stop word removal is an important preprocessing step for some NLP applications, such as sentiment analysis, reaction check and so on.
**Conclusion**
I hope that this tutorial will help to get started with Text preprocessing. I love feedback please let me know what you think, hit the clap button and share with friends and colleagues.
Thanks for reading!
**Resources:**
[Natural Language Processing: Python and NLTK by Iti Mathur, Nisheeth Joshi, Deepti Chopra, Jacob Perkins, Nitin Hardeniya](https://www.amazon.com/Natural-Language-Processing-Python-NLTK-ebook/dp/B01MROO3VA)
[**pandas.DataFrame.apply - pandas 0.24.1 documentation**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
[*Objects passed to the function are Series objects whose index is either the DataFrame's index () or the DataFrame's…*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)[pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
You can have access to the dataset here [http://zindi.africa/competitions/sustainable-development-goals-sdgs-text-classification-challenge](http://zindi.africa/competitions/sustainable-development-goals-sdgs-text-classification-challenge).

