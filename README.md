# personal-attack-classifier

This repository documents the process of building an `NLP` personal attack classifier from lab devlopment to `API` serving.

It is a personal take on the Wikipedia detox project's work on building machine learning models for detecting personal attacks and aggressive tone in user and article talk page comments.

Wikipedia detox project achievement is outlined in [__Ex Machina: Personal Attacks Seen at Scale__](https://arxiv.org/abs/1610.08914)

*Reference : Wulczyn, Ellery; Thain, Nithum; Dixon, Lucas (2016): [Wikipedia Detox](https://meta.wikimedia.org/wiki/Research:Detox)*

## Repository 

The repository is divided in two directories:

1. `Training a personal attack classifier` : Detailled ipython Notebook on end-to-end NLP modeling process using LSTM
2. `Serving an attack classifier with django` : Code to serve the trained model using django rest framework

## Requirements

This project uses the following Python libraries


* `Tensorflow` : For deep learning modelisation
* `Django REST Framework` : For deployment serving purposes
* `flashtext` : For fast text processing
* `Unidecode` : For text formatting

## Install
 Run in Terminal/Command Prompt:

```
git clone https://github.com/timtonthat/personal-attack-classifier.git
cd personal-attack-classifier/Serving\ an\ attack\ classifier\ with\ django/
python3 -m virtualenv venv
```
In UNIX system: 

```
source venv/bin/activate
```
In Windows: 

```
venv\Scripts\activate
```
Download trained model's weights, run:
```
git lfs pull
```

To install all of the required packages to this environment, simply run:
```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the app will be able to run.

## How to use the app
Run this app locally by:
```
cd attack_classifier_api
python manage.py runserver
```
Open http://127.0.0.1:8000/attack_classifier/classify_text in your browser.
