<div style=><img src="https://camo.githubusercontent.com/52d2ff8778b60261533a7dba8dd989c6893a519b/68747470733a2f2f692e696d6775722e636f6d2f315167724e4e772e706e67"/></div>

# Job Interview Technical Exercise Trial
# Gasoline type Recommendation

 <div style="text-align:center"><img src="img/banner.jpg" height=250 /></div>

 ## Introduction

 The goal of this repo is to submit a typical technical exercise requested during a hiring process.

 The scope of the exercise can be found in `scope.md`.

 ## Description
 The following considerations have been taken into account:

 * As described in the scope, this is the [dataset](https://www.kaggle.com/anderas/car-consume?select=measurements.csv) considered. This short dataset is based on cold start-up drives.
 * For price comparison, it has been considered that all gas stations provided unleaded 95 gasoline are E10 type (some may be E5).


 ## Repo Structure

 * `report.ipynb` : presentation of results and recommendations. Output product.

* `notebooks`:
    * `cleaning.ipynb`: notebook containing dataset cleaning.
    * `scraping.ipynb`: notebook containing gasoline prices scraping.
    * `exploration.ipynb`: notebook containing exploration of results and model training.

## Technologies and Environment

Python3 on Ubuntu 20.04

### Scraping
* __[Selenium](https://pypi.org/project/selenium/)__ (setup following [this](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/))
* __[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)__ 

### Cleaning
* __[Numpy](https://pypi.org/project/numpy/)__ 
* __[Pandas](https://pypi.org/project/pandas/)__ 

### Plotting
* __[Matplotlib](https://pypi.org/project/matplotlib/)__ 
* __[Seaborn](https://pypi.org/project/seaborn/)__ 





 