# ph_showcase

## Introduction

Given a list of candidates and a list of projects, find the best candidate for every project. A [candidate](./data/candidates.csv) has an ID, a name and a description of his working experience. A [project](./data/projects.csv) has an ID, a name, a title (the expected job of candidates) and a requirement (expected skills). The title and requirement are optional attributes.

The main idea is (1) search the expected job in candidate's description and calculate the corresponding bm25 score, and (2) calculate semantic similarity between the candidate's description and job's requirement. We then have title scores and description scores respectively. We sum them and return the candidate with the maximum score.

## Keysteps:

1. pip install requirements.txt
2. python -m spacy download en_core_web_lg
3. python server.py

We setup a RESTful API (server.py) and a running example is given in main.py
