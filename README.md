#Forecasting Hollywood: Can Movie Revenues Be Predicted?
###Python code and Data Set developed as part of first mini-project for Applied Machine Learning Course.

##Group Members
Faiz Khan, Muntasir Chowdhury, Kashif Javed


##Overview
This Read Me manual describes the overall requirements and working of the Project Code and how it can be executed to regenerate the same results. For more details about the Project please consult the project report being submitted.

##Requirements
All the code has been developed in Python 2.7 and following Python libraries are used. Documentation links for all these imported libraries can be found in the Project Report in the references section. 

1. BeautifulSoup
2. unicodecsv
3. lxml
4. numpy
5. scipy
6. scikit-learn

The libraries can also be installed using 
pip install beautifulsoup4 unicodesv lxml numpy scipy scikit-learn

##Note About Path
For running each Python scripts developed in the project, scripts's directory should be the current directory. Besides that no change is required in the modules because all the paths used within the scripts are relative to its location. experiments.py is the main script used to generate all test data which can be modified to supply different values for the paramters and it runs all the implemented algorithms on the dataset using those parameters.

## Scripts and Modules
There are several scripts available, each fulfills a specicif purpose. Following are different Python scripts/modules included in the project along with their brief description:

###Learning Modules (src\):

1. feature_lib.py:
    This module contains various functions which are being used to generate feature from the raw data. For example it has functions to determine if the movie was released in a hot season or not, generate average Rotten Tomatoes and IMDB ratings for actors, directors, producers and writers etc.

2. experiments.py:
    This is the main module which calls all the underlying module for extracting features from the raw data, generating data dictionaries for actors, directors, producers and writers and generating final features data set. It then calls functions present in K-Fold module by providing different values for the input parameters like number of partitions, learning rate etc.
3. combine.py:
    This module combines all the all the raw datasets collected in the mining/scraping/filtering stage to come up with a single raw dataset.
4. k\_fold\_validator.py:
    This module splits the input dataset into k different partitions. Besides that it contains functions for running each learning algorithms (Regression, Gradient Descent, Ridge and Lasso) on these k partitions keeping one out for testing purpose. 
5. feature_generator.py:
    This module calls various functions present in feature\_lib.py to generate features from the raw data and then combines those features to generate final dataset used in various learning algorithms. Besides that it also creates data dictionaries for actors, directors, producers and writers present in the raw data using feature_lib.py functions.
6. ridge_lasso.py:
    This module contains two functions for Ridge Regression and Lasso Regularization. These functions are implemented using the Ridge and Lasso functions available in scikit-learn library.
7. regression.py:
    This module contains various basic regression functions to learn weight vector if we have feature matrix and target vector. Besides that it also contains Least Square Error and Mean Square Error functions to determine error using certain values for the weight.
8. regression_predictor.py:
    This module calls the closed form regression algorithm using the whole dataset as the training set and gives Mean Square Error.
9. grad_predictor.py:
    This module simply calls the grad\_descent function present in grad_descent.py module to learn weights using Gradient Descent method using the whole dataset as the training set. After determining the weights it calculates the Mean Square Error using that weight vector on the whole dataset.
10. grad_descent.py:
    This module contains the actual implementation of Gradient Descent method which takes training set, initial weights, learning rate and number of iterations as input and returns the final weight vector after running the Gradient Descent algorithm.
    
####Data Download Scripts (src\downloaders):

1. download\_imdb\_pages.py:
    This module was used to download IMDB movie pages for all the movie names (links) present in a csv file generated by imdb_urls.py
2. download\_the_numbers.py:
    This module was used to download html pages from The-Numbers which contains list of all the movie titles by starting from page containing list of movie names starting with A and going on till Z.
3. download\_the\_numbers\_movie\_pages.py:
    Using the list of movie names generated in download\_the\_numbers.py module, this module downloads the movie pages from The Numbers website for those movies.
4. imdb_urls.py:
    This module uses the list of movie names generated from The Numbers website and then creates a list containing links for corresponding IMDB movie pages.
    
###Data Filter Script (src\filters):

1. revenue\_only\_data.py:
    This module uses the data parsed from The Numbers web pages and then generate a raw dataset with only those rows which contains values for the raw features.
    
Parser Scripts (src\parsers):

1. parse\_imdb\_cast_crew.py:
    This module parses the downloaded IMDB web pages and extracts movies Cast and Technical Crew data for all the movies.
2. parse\_imdb\_ratings.py:
    This module parses the downloaded IMDB web pages and extracts Audience Rating for all the movies.
3. parse\_rotten\_tomato_ratings.py:
    This module extracts the Rotten Tomatoes rating for the final movies list by parsing the pages downloaded from The Numbers website.
4. parse\_the\_numbers.py:
    This module parses all the alphabetic movie list pages downloaded from The Numbers website and creates the initial list of movie along with most of the raw features like Release Data, Budget, Revenue etc.
