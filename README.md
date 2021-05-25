# cds-language_Assignment_4

***Assignment for language analytics class at Aarhus University.***

***2021-03-15***


# Network analysis: creating reusable network analysis pipeline

## About the script

This assignment is Class Assignment 4. The purpose of this assignment was to create reusable network analysis pipeline or command-line tool, which enables the script to be run from the command line. This command-line tool takes a given weighted edgelist dataset, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB", and performs a simple network analysis. In particular, it builds networks based on entities appearing together in the same documents, which enables us to examine relationships among entities. Moreover, it creates and saves a network visualization and CSV file showing the degree, betweenness, and eigenvector centrality for each node.

## Methods

The problem of the task relates to creating a reusable network analysis pipeline. To address this problem, I have used ```NetworkX``` and ```Graphviz``` packages, which are suitable for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. First, using a simple dataframe with nodes and their weights as an input, I have created and saved a network graph with a 'spring model' or 'neato' layout. Afterwards, I have calculated the following centrality measures: degree (the number of edges connected to the node), betweenness centrality and eigenvector centrality. Lastly, I have merged centrality measures dictionaries into a ```pandas``` dataframe
and saved as CSV file. As a result, this defines a reusable pipline to perform network analysis on any other dataframe (see 'Data' section below).



## Repository contents

| File | Description |
| --- | --- |
| data/ | Folder containing input data for the script |
| data/fake_or_real_news.zip | archived dataset used to extract named individuals |
| data/weighted_edgelist.csv | input dataset for the script |
| output/ | Folder containing CSV files produced by the scripts |
| output/network_measures_all_weights.csv | calculated centrality measures of all nodes |
| output/network_measures_weights_500.csv | calculated centrality measures of the nodes with a weight higher that 500|
| src | Folder containing the script |
| src/network.py | Network analysis script |
| viz/ | Folder containing PNG network graphs produced by the script |
| viz/network_viz_all_weights.png| network graphs including all nodes  |
| viz/network_viz_weights_500.png| network graph including the nodes with a weight higher that 500 |
| LICENSE |  A software license defining what other users can and can't do with the source code |
| README.md | Description of the assignment and the instructions |
| create_networks_venv.bash | bash file for creating a virtual environmment |
| kill_networks_venv.bash | bash file for removing a virtual environment |
| requirements.txt | list of python packages required to run the script |


## Data

__Data preprocessing__

The dataset for the project was created during the following process:
- Named individuals were extracted from a 'fake_or_real_news' dataset using ```spaCy```
- The co-occurrence of the named individual pairs were counted and saved as a 'weight' variable

__Data structure__

The final column structure of the CSV file is the following:
| Column | Description |
| --- | --- |
| nodeA | named individual 1 |
| nodeB | named individual 2 |
| weight | degree of co-occurrence of named individuals in a dataset |

This script should be able to take any similarly structured dataset with identical column names as an input.


## Intructions to run the code

Code was tested on an HP computer with Windows 10 operating system. It was executed on Jupyter worker02.

__Code parameters__

| Parameter | Description |
| --- | --- |
| directory  (dir) | Directory where CSV file is located |
| node_size (node) | Node size in a network graph. Default = 20 |
| font_size (font) | Named entities font size in a network graph. Default = 10 |
| weight (w) | Cut-off point to filter input data based on a certain edge weight (degree of nodes co-occurence). If not entered, all weights are included |


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
$ bash create_networks_venv.sh
$ source ./networks/bin/activate

``` 

Run the code:

```
#6 Navigate to the directory of the script
$ cd src

#7 Run the code with default parameters (including all edge weights)
$ python network.py -dir ../data/weighted_edgelist.csv

#8 Run the code filtering input data based on a certain edge weight
$ python network.py -dir ../data/weighted_edgelist.csv -w 500

#9 Run the code with all self-chosen arguments
$ python network.py -dir ../data/weighted_edgelist.csv -node 10 -font 5 -w 500 

#10 To remove the newly created virtual environment
$ bash kill_networks_venv.sh

#11 To find out all possible arguments for the script
$ python network.py --help

 ```

I hope it worked!


## Results

This assignment showed how ```NetworkX``` can be used to perform a simple network analysis on entities appearing together in the same documents. The resulting script can be used as a reusable pipeline to perform similar network analyses on similar datasets. Such analyses can inform us about the underlying structure and dynamics of the relationships between individuals.

