# cds-language_Assignment_4

***Assignment for language analytics class at Aarhus University.***

***2021-03-15***


# Network analysis: creating reusable network analysis pipeline

## About the script

This assignment is Class Assignment 4. The purpose of this assignment was to create reusable network analysis pipeline or command-line tool, which enables the script to be run from the command line. This command-line tool takes a given weighted edgelist dataset, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB", and performs a simple network analysis. In particular, it builds networks based on entities appearing together in the same documents, creates a network visualization and a data frame showing the degree, betweenness, and eigenvector centrality for each node.

## Methods



## Repository contents

| File | Description |
| --- | --- |
| data/ | Folder containing input data for the script |
| data/abcnews-date-text.rar | archived headlines dataset |
| output | Folder containing files produced by the scripts |
| output/weekly_sentiment.png | a plot displaying 7-days rolling average of sentiment scores |
| output/monthly_sentiment.png | a plot displaying 30-days rolling average of sentiment scores|
| output/combined_sentiment.png | a plot displaying 1, 7, 30  and 365-days rolling averages of sentiment scores |
| src | Folder containing the scripts |
| src/sentiment.py | Sentiment analysis script |
| LICENSE |  A software license defining what other users can and can't do with the source code |
| README.md | Description of the assignment and the instructions |
| create_sentiment_venv.bash | bash file for creating a virtual environmment |
| kill_sentiment_venv.bash | bash file for removing a virtual environment |
| requirements.txt | list of python packages required to run the script |


## Data

The dataset for the project was created during the following process:
- Named individuals were extracted from a 'fake_or_real_news' dataset using ```spaCy```
- The co-occurrence of the named individual pairs were counted and saved as weight variable

The column structure of the CSV file is the following:
| Column | Description |
| --- | --- |
| nodeA | named individual 1 |
| nodeB | named individual 2 |
| weight | degree of co-occurrence of named individuals in a dataset |


## Intructions to run the code

Code was tested on an HP computer with Windows 10 operating system. It was executed on Jupyter worker02.


__Steps__

Set-up:
```
#1 Open terminal on worker02 or locally
#2 Navigate to the environment where you want to clone this repository
#3 Clone the repository
$ git clone https://github.com/Rutatu/cds-language_Assignment_4.git 

#4 Navigate to the newly cloned repo
$ cd cds-language_Assignment_4

#5 Create virtual environment with its dependencies and activate it
$ bash create_network_venv.sh
$ source ./network/bin/activate

``` 

Run the code:

```
#6 Navigate to the directory of the script
$ cd src

#7 Run the code with default parameters
$ python network.py

#8 Run the code with self-chosen arguments
$ python network.py

#9 To remove the newly created virtual environment
$ bash kill_network_venv.sh

#10 To find out possible optional arguments for the script
$ python network.py --help

 ```

I hope it worked!


## Results






I hope it worked :)
