# PatientsLikeMe

The details of the analysis can be seen in the jupyter notebook PLM.ipynb.
All the files required for the web-application can be found in this repository. The list of dependencies for the webapp are in requirements.txt.
The web-application is hosted on a Digital-Ocean droplet.

## Link to the web-application: http://167.71.144.110/

![](https://github.com/isuhail/PatientsLikeMe/blob/master/als1.PNG width=100)

## Project Overview

This project aims at providing a web-application to ALS patients where they could enter the symptoms they faced to understand the trend of the average variation of the ALS scores of the patients who faced similar kinds of symptoms. Advanced statistical modeling and natural language processing techniques have been used to group similar patients.   

## Data

The data about the ALS patients is distributed among four datasets. These datasets have been ptovided by PatientsLikeMe

1) user_ALSERS_score.csv
2) user_onset_date.csv
3) user_condition.csv
4) user_symptom.csv

## Usage

The web application consists of a webpage where the user can enter upto three symptoms he/she has faced.

Upon clicking submit, the web application will display the name of the group of symptoms, the patients like the user have faced. The group is decided based on the probability of a user belonging to every group. It will also display the trend of the variation of the average ALS Score within the population for these group of users.

NOTE: The data for ALS Scores for six groups is not available. In such a case only the group name will be displayed.

List of the groups:
1) 'Mental Health related issues',
2) 'Body part/muscle pain',
3) 'Headache/Speech issues',
4) 'Spasticity/ digestive issues',
5) 'Chest pain/hernia/ urination problems',
6) 'Blood pressure and heart problems',
7) 'Neurological/ vision and speech related issues',
8) 'Sensitivity issues',
9) 'Skin problems',
10)'Body balance/menstrual problems',
11)'Emotional issues',
12)'Infections/ excessive fat issues',
13)'Sore throat/ abdominal problems', 
14)'Sleep related problems', 
15)'Joint/neck pain'
]
## Approach 

This web application is built on a two step approach 

### 1) Latent Dirichlet Allocation (Topic Modeling)

The data from the user_symptom.csv dataset has been aggregated at the user level to get details of all the symptoms faced by a particular user. 
Natural Language processing techniques and LDA Modelling has been implemented on these symptoms to generate topics from this data such every user has a certain probability to belong to every topic.
The topic for which a user has the maximum probability is assigned to that particular user

### 2) Variation in Time trends of the ALS Score

Once we have a labelled dataset with all the topics from the given users, It is joined with the user_ALSERS_score.csv dataset.
This dataset is now split into smaller datasets based on the topic and the variation for the ALS Score has been plotted for every topic.
Once a user enters the details about the symptoms in the webapp, the topic for the user is generated based on the trained model.
Lastly, based on the topic the time trend obtained above is displayed.

## Future Scope

1) Improving the LDA model performance
2) Enhancing the names of the topics with the help of Subject matter experts
3) Collecting data for time trends for users belonging 6 topics for which data is completely unavailable
4) Scaling the web-application
