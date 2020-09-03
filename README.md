# personal-attack-classifier

This repository documents the process of building an `NLP` personal attack classifier from lab devlopment to `API` serving.

It is a personal take on the Wikipedia detox project's work on building machine learning models for detecting personal attacks and aggressive tone in user and article talk page comments.

Wikipedia detox project achievement is outlined in [__Ex Machina: Personal Attacks Seen at Scale__](https://arxiv.org/abs/1610.08914)

*Reference : Wulczyn, Ellery; Thain, Nithum; Dixon, Lucas (2016): [Wikipedia Detox](https://meta.wikimedia.org/wiki/Research:Detox)*

## Repository 

The repository is divided in two directories:

1. `Build a personal attack classifier` : Detailled documentation on end-to-end NLP modeling process
2. `Serving a personal attack classifier` : REST API code to serve the trained model 

## Requirements

This project uses the following Python libraries


* `Tensorflow` : For deep learning modelisation
* `Django REST Framework` : For deployment serving purposes
* `flashtext` : For fast text processing
* `Unidecode` : For text formatting
