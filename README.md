# HHS Challenge (Bayes Hack 2016) - Semantic Search Engine

- Team: Innocent Bayestanders
- Members: Ron Cordell, Konniam Chan, Chris Dailey, Marjorie Sayer, Safyre Anderson
- April 24, 2016

### Abstract
We aimed to connect people with the health care plan that best serves their needs. Current recommenders such as healthcare.gov and StrideHealth are a skin on top of the complicated mess that is health plan data. Users are shown options that match their basic demographic and medical history. Close to nothing is done to communicate the details of the plan in understandable laymens terms or why a plan is selected for that user. To go a step further, we’re building a faceted search engine that learns. Think Google + Amazon; PageRank + Facets. Powered by combined healthcare data, third party reviews from sources like Yelp and other sources users are able to search more simply yet more completely than ever before.  As the search engine grows in popularity, so will the matching ability of the results. Each pause and click on the website is captured and fed to a Learn to Rank algorithm.  We are taking health care to a new level that brings the users closer to finding the healthcare they need.

### Problem
 The ACA insurance marketplace has been problematic for consumers since its inception. It is difficult to choose a suitable ACA plan, as it is not possible to view multiple plans together. Providers are not always in network. Plans are simply a filter on the existing data, and not matched to patients' needs.

### End-to-end solution

#### Overview:

The system consists of a 2 stage web-based UI. In the first stage, we ask the user a series of questions on their demographics, their preferences for certain particular providers, and a subset of their existing medical conditions. Additionally, we provide a free-form text box for users to enter key words--for example, "acupuncture", "alternative medicine", "oncology"--which will be loosely matched to descriptions tied to each plan. Each ACA plan contains information about their providers, network coverage, drugs, and third-party resources such as Yelp and Vitals.com. The highest-ranked plan is returned to the user in a results page. The user have access to a series of filters that narrow down various plans, and they can select one that best fits their needs.

In the second stage, the user's interactions on the results page are all collected via a clickstream collector. Over time, user click behavior statistics such as dwell times, mean recipricol rank (MRR), detail expansions are collected, stored, and processed into training data for our learn-to-rank (LETOR) algorithm. The LETOR algorithm is the key differentiator between our framework and existing frameworks: the system gets smarters as more users interact with it.

#### Backend:

*Data*
The raw data were mostly provided in a machine-readable JSON format: the ACA data, CMS data.. (ron)

*ElasticSearch*
The ElasticSearch cluster was created using bare metal servers from IBM's Softlayer Infrastructure-as-a-Service. The cluster consisted of 6 CentOS 7 servers with 8 GB RAM and 100 GB SSDs each connected via passwordless SSH. One server acted as the ElasticSearch master node, while the remaining 5 held the data. The ElasticSearch engine is easily adaptable to new servers by simply added new servers and server hostnames to the configurations. Though in our implementation, there data were only stored as one copy, ElasticSearch is capable of storing multiple copies of the data for disaster recovery.

*ClickStream Data and Machine Learning*

#### Frontend

*UI*


### Open source
The plan is to open-source the architecture of this end-to-end healthcare recommendation engine so that others can built on it. While there could be issues regarding certain bad actors trying to manipulate the system, we think the semantic search engine is a worthwhile improvement over the existing system.





