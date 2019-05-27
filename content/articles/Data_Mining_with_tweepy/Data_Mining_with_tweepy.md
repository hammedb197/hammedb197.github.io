Title: Data Mining with tweepy
Date: 2019-04-21 7:25:50
Category: Blog
Tags: python, tweepy, sentiment analysis, twitter
Slug: Data Mining with tweepy

Beautiful is better than ugly.

----------

**Data Mining with tweepy**

> Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Originally published in [The Zen Of Python](https://www.python.org/dev/peps/pep-0020/#id3) by Author Tim Peters .
![](https://cdn-images-1.medium.com/max/2560/1*uPK8hMIxQK6cvzw93mfyHA.jpeg)


Tweepy is a Python library for accessing Twitter API. It is cool for simple automation. In this tutorial , I will be covering how to get tweets from our timeline. What we will be needing for this tutorial include:

1. Python3
2. pip
3. Jupyter Notebook (for interactive section)
4. Tweepy

5. Twitter account.
The first step is to download python 3.7 visit [here](https://www.python.org/) and download the interpreter that correspond with the os on your laptop.
Install python3 interpreter on your computer, remember to tick add to system path during your installation.
Getting interesting ?
Now open your terminal or command prompt
Type pip install tweepy or sudo apt install python3-pip for linux users then pip install tweepy
After this install our jupyter notebook

![](https://cdn-images-1.medium.com/max/800/1*FGrQDDWwk2MUHvbBCHYzlg.png)


Let’s go to our workspace now
Open your terminal or CMD and type jupyter notebook to start our interactive section

![](https://cdn-images-1.medium.com/max/800/1*vZnWOPbS8LHjC2NTJq8Smw.png)


Your browser should open automatically

![](https://cdn-images-1.medium.com/max/800/1*J4vtkPxFgEYnPtGFaaTMxQ.png)


Let’s start work
Now we will need to import Tweepy

![](https://cdn-images-1.medium.com/max/800/1*mh1L7DSwYgZGEDp3OfN5_A.png)


run with shift + enter, immediately a new cell will pop out
**Getting Twitter Credentials**
Now we need to create a twitter account, go to [apps.twitter.com](https://apps.twitter.com/) and sign in with your account. Create a Twitter application and generate a Consumer Key, Consumer Secret, Access Token, and Access Token Secret.
**The next thing to do is to create variables for your credentials and enter into your new cell as shown below :**

![](https://cdn-images-1.medium.com/max/800/1*w5AubUcNxoyRjE09ETa5mg.png)


Note: your consumer key,consumer secrets, access token,access token secret should be kept private.
Press shift + enter again to run your interactive section, after pressing this a new cell will pop
**Getting Tweets**
You can get recent tweets from account you follow recently by entering the following into your new cell as shown below:

![](https://cdn-images-1.medium.com/max/800/1*-I3N-aX42Xy8_Z5-dFsR_g.png)


This will download your timeline tweets and print each in the console.
**Now let’s get the number of followers and People you followed recently**

![](https://cdn-images-1.medium.com/max/800/1*mUwiqw4PwTlcvM5vkRgW4w.png)

    The result is:
    h_bushroh
    244
    david_faniyi
    Moustapha_6C
    mbao_01
    OauNacoss
    pyconcharlas
    DjangoGirlsPyUK
    pyconindia
    elonmusk
    FrontendMasters
    Elishatofunmi
    intelaiiot
    DurexNG
    nextdeegit
    PrincesOluebube
    gitlab
    Djangotarkwa
    pykidsghana
    pydataghana
    instadeepai
    forloopoau

my username is h_bushroh, I have 244 followers and list of people shown include list of people I followed recently.
**How to save data gotten from twitter as csv**
This can be done using pandas, a python library.

![](https://cdn-images-1.medium.com/max/800/1*fr3mwDxYyWqpKoh4ekzAVg.png)


This will save our fetched data to in csv format.
**Things you can do with fetched data**
Twitter Sentiment analysis
Auto follow and auto tweet Twitter bot.
**Conclusion**
I hope that this tutorial will help to get started with data mining using tweepy.
I love feedback please let me know what you think  and share this post with friends and colleagues.
Thanks for reading!


