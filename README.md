# Splunk for processing machine data (commercial tool)
## 44517-01
## Team-07
## Developers and Participants
- Varun Goud Pulipalpula<br/>
- Bala Gopi Krishna Sabbineni<br/>
- Harshith Gudapati
## Links
- [Source_Repo](https://varungoud2930.github.io/Splunk/)<br/>
- [Issue_Tracker](https://github.com/varungoud2930/Splunk/issues)<br/>
- [Data_Source](https://www.kaggle.com/carlolepelaars/toy-dataset)
## Introduction
Splunk (the product) captures, indexes, and correlates real-time data in a searchable repository from which it can generate graphs, reports, alerts, dashboards, and visualizations.In this project we are finding count of cities, average age and maximum income for each state.
## V's of the data
#### This dataset is related to Toy Dataset. They are of 6 columns like City is the location of a person (Dallas, New York City, Los Angeles, Mountain View, Boston, Washington D.C., San Diego and Austin) ,Gender of a person (Male or Female), Age of a person (Ranging from 25 to 65 years), Income i.e., Annual income of a person (Ranging from -674 to 177175) and Illness: Is the person Ill? (Yes or No)
- Volume: The volume of my data is 5MB. It has 6 columns and 150001 rows. <br/>
- Variety: This is a very structured dataset which is available in CSV format. <br/>
- Velocity: The velocity of the dataset is high because data wil be changed every age people and data will updated for every city. <br/>
- Veracity: The data is not messy and it is cleaned.<br/>
- Value: We can easily find the Age and Income of a person.<br/>
- Link: https://www.kaggle.com/carlolepelaars/toy-dataset
## Big Data Problems

- Maximum : Bala Gopi Krishna Sabbineni
- Question: For all Cities, we will find the maximum of Income.
### Solution: 
      - Mapper Input:
      - Intermediate Pairs:
      Number, City, Gender, Age, Income, Illness
      - Mapper Output/Reducer Input:
      City, Income
      - Results:
    Austin	          132302
    Boston	          132348
    Dallas	          91479
    Los Angeles	      141249
    Mountain View	    177157
    New York City	    147170
    San Diego	        140190
    Washington D.C.	  107704

      


![Maximum Income](https://github.com/varungoud2930/Splunk/blob/master/Income%20-%20maximum%20for%20each%20city/Maximum_Income_graph.png)

- Average Age : Harshith Gudapati
- Question : For all Cities, we will find the average Age.<br/>
### Solution: 
     Mapper Input:
      - Intermediate Pairs:
      Number, City, Gender, Age, Income, Illness
      - Mapper Output/Reducer Input:
      City, Age
      - Results:
     Austin	              44.65123658
     Boston	              45.20262619
     Dallas	              45.06079058
     Los Angeles	        44.99533771
     Mountain View	  44.99556931
     New York City	  44.92291331
     San Diego	        44.97336611
     Washington D.C.	  44.80763547

      

![Average Age](https://github.com/varungoud2930/Splunk/blob/master/Average-%20Age/Average.png)

- Count of Cities : Varun Goud Pulipalpula
- Question : For all Cities, we will find the count of Cities.<br/>
### Solution: 
       Mapper Input:
      - Intermediate Pairs:
      Number, City, Gender, Age, Income, Illness
      - Mapper Output/Reducer Input:
      City, Count
      - Results:
    Austin	            12292
    Boston	            8301
    Dallas	            19707
    Los Angeles	      32173
    Mountain View	      14219
    New York City	      50307
    San Diego	      4881
    Washington D.C.	8120


![Count of Cities](https://github.com/varungoud2930/Splunk/blob/master/Cities-%20count/count_of_cities.png)

