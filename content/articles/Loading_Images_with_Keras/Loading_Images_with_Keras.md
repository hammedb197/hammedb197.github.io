Title: Loading Images with Keras
Date: 2019-04-21 7:25:50
Category: Blog
Tags: python, keras, image classification, deep learning, imagegenerator
Slug: Loading Images with Keras

Keras is a high-level API to build and train deep learning models. It runs on Tensorflow and Theano as backend.

----------

**Loading Images with Keras**

![](https://cdn-images-1.medium.com/max/800/0*90NS2eJLUrfzhzlL.png)


![](https://egghead.io/courses/fully-connected-neural-networks-with-keras)

----------

**Keras** is a high-level API used to build and train deep learning models. It runs on Tensorflow and Theano.
I’ll be using JupyterLab throughout this session. Working with real-life data involves more than loading inbuilt datasets from our various APIs. To load a dataset from Keras API you can load mnist dataset from `keras.datasets import mnist keras`
Load your train and test sets like this `(x_train, y_train), (x_test, y_test) = train_test_split()` .
The truth here is that it’s not always that easy when working with real-life data. In this tutorial, I’ll be taking you step by step on how to load your data with Keras.
The first thing is to have your CSV file containing your class name(category) and id. I’ll be showing the head of my CSV file now.

![](https://cdn-images-1.medium.com/max/800/1*gZ_DHzOqizQn9fHMhyZ7Xg.png)

![](https://cdn-images-1.medium.com/max/800/1*1xpCZbtZB_4lagHlEqDoGA.png)


number of categories
You might want to check the categories you have so as to learn more about what you are working with. Now we know we have 23 classes, the next step is to check the value counts for each category.

![](https://cdn-images-1.medium.com/max/800/1*AVbD9i6al6-SYB7asg0vYw.png)


value_counts
We can see the number of observations in each distinct category. The next step is to set the directory you want each category to be. I wrote a function that can get each value for each category.

![](https://cdn-images-1.medium.com/max/800/1*K2_yc6O2mGpFvh-xScO8hw.png)


After this I can go on and create my ‘base’ directory, then a ‘train’ directory, a ‘test’ directory.

![](https://cdn-images-1.medium.com/max/800/1*ls7SknEHadEaq_ZALVEm_A.png)


The first thing I did here is to import os. OS module allows you to interact with the underlying operating system that Python is running on.
After that, I defined the directory where I have my data(images) as `**original_dataset_dir**`**.** Now I can start creating my directories, `**os.mkdir()**` ****means ****create a directory, `**os.join()**` is trying to concatenate base_dir and ‘train’, the result from this will be ‘base_dir/train’, from train directory create earlier then I created a directory for each category I have. After running this our directory tree would be like this


    — base_dir
    ├── test
    │ ├── Acne-and-Rosacea-Photo
    │ ├── Actinic-Keratosis-Basal-Cell-Carcinoma-and-other-Malignant-Lesion
    │ ├── Atopic-Dermatitis-Photo
    │ ├── Bullous-Disease-Photo
    │ ├── Cellulitis-Impetigo-and-other-Bacterial-Infection
    │ ├── Eczema-Photo
    │ ├── Exanthems-and-Drug-Eruption
    │ ├── Hair-Loss-Photos-Alopecia-and-other-Hair-D
    │ ├── Herpes-HPV-and-other-STDs-Photo
    │ ├── Light-Diseases-and-Disorders-of-Pigmentation
    │ ├── Lupus-and-other-Connective-Tissue-d
    │ ├── Melanoma-Skin-Cancer-Nevi-and-Mol
    │ ├── Nail-Fungus-and-other-Nail-D
    │ ├── Poison-Ivy-Photos-and-other-Contact-Dermatit
    │ ├── Psoriasis-pictures-Lichen-Planus-and-related-d
    │ ├── Scabies-Lyme-Disease-and-other-Infestations-and-Bit
    │ ├── Seborrheic-Keratoses-and-other-Benign-Tumor
    │ ├── Systemic-D
    │ ├── Tinea-Ringworm-Candidiasis-and-other-Fungal-Infection
    │ ├── Urticaria-Hiv
    │ ├── Vascular-Tumor
    │ ├── Vasculitis-Photo
    │ └── Warts-Molluscum-and-other-Viral-Infection
    └── train
    ├── Acne-and-Rosacea-Photo
    ├── Actinic-Keratosis-Basal-Cell-Carcinoma-and-other-Malignant-Lesion
    ├── Atopic-Dermatitis-Photo
    ├── Bullous-Disease-Photo
    ├── Cellulitis-Impetigo-and-other-Bacterial-Infection
    ├── Eczema-Photo
    ├── Exanthems-and-Drug-Eruption
    ├── Hair-Loss-Photos-Alopecia-and-other-Hair-D
    ├── Herpes-HPV-and-other-STDs-Photo
    ├── Light-Diseases-and-Disorders-of-Pigmentation
    ├── Lupus-and-other-Connective-Tissue-d
    ├── Melanoma-Skin-Cancer-Nevi-and-Mol
    ├── Nail-Fungus-and-other-Nail-D
    ├── Poison-Ivy-Photos-and-other-Contact-Dermatit
    ├── Psoriasis-pictures-Lichen-Planus-and-related-d
    ├── Scabies-Lyme-Disease-and-other-Infestations-and-Bit
    ├── Seborrheic-Keratoses-and-other-Benign-Tumor
    ├── Systemic-D
    ├── Tinea-Ringworm-Candidiasis-and-other-Fungal-Infection
    ├── Urticaria-Hiv
    ├── Vascular-Tumor
    ├── Vasculitis-Photo
    └── Warts-Molluscum-and-other-Viral-Infection

Now you have your directory ready, the next step is to load data into the created directories. The next step is to split my train, test in the ratio of 0.75: 0.25 of the full dataset.

![](https://cdn-images-1.medium.com/max/800/1*HzeEsGVIEQL_wJrYRI-fDg.png)


I have defined my train_test ratio, I want to go ahead and load my data.

![](https://cdn-images-1.medium.com/max/800/1*TGmEnLEGiJ0qFqP9C9NqSw.png)


I imported shutil earlier, shutil module helps to automate copying files and directories. I am trying to copy images from the `**original_dataset_dir**`(train_src) to my destination(train_dst) using shutil, after this step, you should have your data loaded.
Let’s confirm if we have our data loaded.

![](https://cdn-images-1.medium.com/max/800/1*yoA-VEXKfIzMXNEbRy7Czg.png)


Now you have your data in appropriate directories, the next step is to load your data into ImageDataGenerator from Keras.

![](https://cdn-images-1.medium.com/max/800/1*Yg21ARJplVnc5rgzSh276Q.png)


ImageDataGenerator
We can now perform data augmentation on our data and build our Convolutional Neural Network.
Thanks for reading, I do appreciate feedbacks and corrections if any.
Happy Learning, remember to hit clap button, cheers !!!.

