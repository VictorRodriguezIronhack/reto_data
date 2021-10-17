![cobify](https://camo.githubusercontent.com/a70f459b10d2ba6cdc24f887af992e6b522797b3f631dcfd21ac64d80bedaf88/68747470733a2f2f6b616d6973657461732e636f6d2f696d6167652f626f726461646f732f436f62692d42617263656c6f6e612d39322d7061726368652e676966)
# Cobify
Given some data from a motor vehicle startup company, the objective is to determine which type of gas is better; e10 or SP98. After analysis the data, the conclusion reached was that even though SP98 is more expensive than E10, the E10 gets consumed faster, therefore being more expensive in the long run.  
![gas_consume](https://github.com/DiegoCefalo/reto_data/blob/main/img/Screenshot_1.png)

## Some Analysis
Here we can see that there is a spike in gas consumption at low distances and low speeds, this might be attributed to the possibility that these trips were mostly in the city, where the movement  might be limited by traffic and travel distances might be short. They might not be moving too much, but just having the engine runing  makes the consumption skyrocket while not moving (the consumption is measured in litres per 100 kilometres).  
![distance](https://github.com/DiegoCefalo/reto_data/blob/main/img/distance.jpg)
![speed](https://github.com/DiegoCefalo/reto_data/blob/main/img/speed.jpg)  
However, when we graph speed vs distance, we can see that most trips do not surpass 60 km/h, and the ones that do, have a considerable greater distance, which means that these entries were recorded after going through the highway.  
![distance_speed](https://github.com/DiegoCefalo/reto_data/blob/main/img/distance_speed.jpg)
On another note, we have 4 variables that affect the consumption slightly, yet we have to take into consideration the sum of all this factors.  
When the AC is on, the consumtion is higher as expected.  
![AC](https://github.com/DiegoCefalo/reto_data/blob/main/img/AC.jpg)
When it is raining, the consumtion is higher, which might be because rain usually accentuates traffic.  
![rain](https://github.com/DiegoCefalo/reto_data/blob/main/img/rain.jpg)
When it is snowing, the consumtion is higher because the engine needs to be warmed up before driving.  
![snow](https://github.com/DiegoCefalo/reto_data/blob/main/img/snow.jpg)
And viceversa, when it is sunny, the engine doesnt need to be warmed up, therefore it consumes less.  
![sun](https://github.com/DiegoCefalo/reto_data/blob/main/img/sun.jpg)

Also, we can tell which variables are more correlates to consumption thanks to this heatmap:  
![corr](https://github.com/DiegoCefalo/reto_data/blob/main/img/CorrHeatmap.jpg)

## API
A small API was created to access the data. Mysql was used to store the data and the "sqlalchemy" library was used to load the data into the database.
## Use of the API
    It runs on python Flask and for now it only works as a local server. The endpoints are:
* http://localhost:5000/ : This is just a test to check if the server is running. It returns "Hello World"
* http://localhost:5000/collection : Returns all the entries in the database as a json
* http://localhost:5000/entry?(params) : It requires the id of the entry as a parameter (e.g. id=4) and returns a json with the selected entry.
* http://localhost:5000/e10 : Returns all the entries with gas_type e10 in the database as a json
* http://localhost:5000/sp98 : Returns all the entries with gas_type e10 in the database as a json

 ## Used libraries
 * [Pandas](https://pandas.pydata.org/docs/)
 * [Numpy](https://numpy.org/doc/stable/)
 * [Seaborn](https://seaborn.pydata.org/)
 * [Matplotlib](https://matplotlib.org/stable/index.html)
 * [Regular Expressions](https://docs.python.org/3/library/re.html)
 * [Selenium](https://www.selenium.dev/documentation/)
 * [SQLalchemy](https://www.nltk.org/)
 * [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 * [Dotenv](https://pypi.org/project/python-dotenv/)