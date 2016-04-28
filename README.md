# HHS Challenge (Bayes Hack 2016) - Semantic Search Engine

- Team: Innocent Bayestanders
- Members: Ron Cordell, Konniam Chan, Chris Dailey, Marjorie Sayer, Safyre Anderson
- Mentors: Jimi Shanahan, David Portnoy
- Date: April 26, 2016

### Abstract
We aimed to connect people with the health care plan that best serves their needs. Current recommenders such as healthcare.gov and StrideHealth are a skin on top of the complicated mess that is health plan data. Users are shown options that match their basic demographic and medical history. Close to nothing is done to communicate the details of the plan in understandable laymens terms or why a plan is selected for that user. To go a step further, we’re building a faceted search engine that learns. Think Google + Amazon; PageRank + Facets. Powered by combined healthcare data, third party reviews from sources like Yelp and other sources users are able to search more simply yet more completely than ever before.  As the search engine grows in popularity, so will the matching ability of the results. Each pause and click on the website is captured and fed to a Learn to Rank algorithm.  We are taking health care to a new level that brings the users closer to finding the healthcare they need.

### Problem
 The ACA insurance marketplace has been problematic for consumers since its inception. It is difficult to choose a suitable ACA plan, as it is not possible to view multiple plans together. Providers are not always in network. Plans are simply a filter on the existing data, and not matched to patients' needs. We propose adapting the lessons from consumer web giants, Google and Amazon, to the insurance marketplace.

### End-to-End Solution

#### Overview:

The system consists of a web application with two stages. In the first stage, we ask the user a series of questions about their demographics, their preferences for certain particular providers, and a subset of their existing medical conditions. Additionally, we provide a free-form text box for users to enter key words--for example, "acupuncture", "alternative medicine", "oncology"--which will be loosely matched to descriptions tied to each plan. Each ACA plan contains information about their providers, network coverage, drugs, and third-party resources such as Yelp and Vitals.com. The highest-ranked plan is returned to the user in a results page. The user have access to a series of filters that narrow down various plans, and they can select one that best fits their needs.

In the second stage, the user's interactions on the results page are all collected via a clickstream collector. Over time, user click behavior statistics such as dwell times, mean recipricol rank (MRR), detail expansions are collected, stored, and processed into training data for our learn-to-rank (LETOR) algorithm. The LETOR algorithm is the key differentiator between our framework and existing frameworks: the system gets smarters as more users interact with it.

#### Backend:

*Data*
[The core data is publicly available as of late 2015 and consists of machine readable JSON files.](data/README.md)

*ElasticSearch*
The ElasticSearch cluster was created using bare metal servers from IBM's Softlayer Infrastructure-as-a-Service. The cluster consisted of 6 CentOS 7 servers with 8 GB RAM and 100 GB SSDs each connected via passwordless SSH. One server acted as the ElasticSearch master node, while the remaining 5 held the data. The ElasticSearch engine is easily adaptable to new servers by simply added new servers and server hostnames to the configurations. Though in our implementation, there data were only stored as one copy, ElasticSearch is capable of storing multiple copies of the data for disaster recovery.

*ClickStream Data and Machine Learning*
Clickstream data is captured with [snowplow](https://github.com/snowplow/snowplow). User-interaction events, such as actions to expand plan descriptions and clicks to provider websites are captured in this platform, and forwarded to a S3 bucket for storage. Users' response to the survey questions and the plan details can be captured in the same S3 bucket as well.

Once all the data have come through the system, we can use machine learning to rank suitability of plans. A sample table (with logs processed and joined), might look like the following:  
  
| Age | Gender | Existing Medical Condition | Plan Premium | Co-Pay | HMO/PPO | Click Plan Link (y/n) |
|-----|--------|----------------------------|--------------|--------|---------|-----------------------|
| 50  | F      | Type II Diabetes           | 100          | 20     | HMO     | 1                     |
| 50  | F      | Type II Diabetes           | 150          | 20     | HMO     | 0                     |
| 50  | F      | Type II Diabetes           | 200          | 0      | PPO     | 0                     |

Any classifier can be used to predict the probabiliy of a link click. Logistic regression would be great starting point for a baseline model. More sophiticated algorithms like random forest could be used as well. As clickstream accumulate beyond a few GB's, we can use Spark to handle the computations. The ML model can be recomputed daily, and fed back into the ElasticSearch cluster to aid the ranking efforts in the web app.

#### Frontend
*Web Framework and UI*  
[Flask](http://flask.pocoo.org), a python web framework based on Werkzeug and Jinja 2, was used in this application. Flask is a lightweight framework, with a plethora of extensions that allow for application features such as form validation, object-relational mappers, and programmatic rendering of HTML. The UI is a barebones setup currently with some [Bootstrap](http://getbootstrap.com) elements. It is straightforward to expand on the design and make it more user-friendly.

### Open source
The plan is to open-source the architecture of this end-to-end healthcare recommendation engine so that others can built on it. While there could be issues regarding certain bad actors trying to manipulate the system, we think the semantic search engine is a worthwhile improvement over the existing system.

### Future Work
*ASR*  
ASR (automatic speech recognition) can be used to aid input from the user. The target demographic for ACA often only has one computing device (smartphone). ASR allows queries to be more easily and enables the best user experience.




