# HHS Challenge - Semantic Search Engine

### Abstract
We aim to connect people with the health care plan that best serves their needs. Current recommenders such as healthcare.gov and StrideHealth are a skin on top of the complicated mess that is health plan data. Users are shown options that match their basic demographic and medical history. To go a step further, we’re building a faceted search engine that learns. Think Google + Amazon. Think PageRank + Facets. Powered by combined healthcare data, third party reviews from sources like Yelp and other sources users are able to search more simply yet more completely than ever before.  As the search engine grows in popularity, so will the matching ability of the results. Each pause and click on the website is captured and fed to a Learn to Rank algorithm.  We are taking health care to a new level that brings the users closer to finding the healthcare they need.

### Problem
 The ACA insurance marketplace has been problematic for consumers since its inception. It is difficult to choose a suitable ACA plan, as it is not possible to view multiple plans together. Providers are not always in network. Plans are simply a filter on the existing data, and not matched to patients' needs.

### End-to-end solution
In a survey, we ask the user a series of questions on their demographics, their preferences for certain particular providers, and a subset of their existing medical conditions. The output of the form is routed to elasticsearch, which contains data about all ACA plans, providers, drugs, and third-party resources such as Yelp and vitals.com. The highest-ranked plan is returned to the user in a results page. The user have access to a series of filters that narrow down various plans, and they can select one that best fits their needs.

The user's interactions on the results page are all collected via a clickstream collector. Over time, more user-plan interactions are collected. Along with survey answers, the clickstream data allow us to build a model (say logistic regression) that predicts the best plan for future users.

All parts of the system is scalable. Elasticsearch and the machine learning backend could be scaled easily.

### Open source
The plan is to open-source the architecture of this end-to-end healthcare recommendation engine so that others can built on it. While there could be issues regarding certain bad actors trying to manipulate the system, we think the semantic search engine is a worthwhile improvement over the existing system.





