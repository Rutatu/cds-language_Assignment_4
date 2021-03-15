# cds-language-analytics_Assignment_4

***Assignment for language analytics class at Aarhus University.***

***2021-03-15***


# Network analysis

The purpose of this assignment is to create reusable network analysis pipeline or command-line tool, which enables the script to be run from the command line. This command-line tool will take a given weighted edgelist dataset, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB", and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, create a network visualization and a data frame showing the degree, betweenness, and eigenvector centrality for each node. It will create 'viz' folder for network.png visualization file and 'output' folder for networks.csv data file.


# About this repository:

This repository is a subset taken from cds-language environment on worker02. The 'data' folder contains 'weighted_edgelist.csv' file which is to be used as an input for the command-line tool. You can use any other dataset which satisfies the requirements mentioned above. The script is defined in network.py file. Also, there are two bash files: 'create_networks_venv.sh' for creating the environment with its dependencies (requirements.txt ) and 'kill_networks_venv.sh' file for removing the environment. 



# Instructions to run the code:

Here are the instructions for runing this script in terminal on worker02:

##1 Preparation 

   - Open terminal on worker02
   - Navigate to the environment where you want to clone this repository, e.g. type: cd cds-language
   - Clone the repository, type: git clone  
   - Navigate to the newly cloned repo, type: cd cds-language-analytics_Assignment_4 
   - Create virtual environment with its dependencies, type: bash create_networks_venv.sh
   - Don´t close the terminal to continue with the instructions below 
   
##2 Execute the script

   - To run the code, type: python network.py data weighted_edgelist.csv
   - To get information about the input arguments, type: python network.py --help 
   - OPTIONAL: there is an otional --weight argument.  To include it, add: --weight as the last argument followed by a number of your choice, e.g. --weight 300
   - Script will take a while to run (faster with --weight argument), so have a short break.
   - It should create 'viz' folder with network visualization in it and 'output' folder with .csv file in it. You should get a message when the script is done running.
   - To remove the newly created networks environment type: bash kill_networks_venv.sh

I hope it worked :)
