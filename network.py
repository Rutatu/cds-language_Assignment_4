#!/usr/bin/env python

'''
Assignment 4: Network analysis

This command-line tool will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, like we did in class.

The script is able to be run from the command line.
It can take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"
For any given weighted edgelist given as an input, this script can be used to create a network visualization, which is saved in a folder called viz.
It also creates a data frame showing the degree, betweenness, and eigenvector centrality for each node. It saves it as a CSV file in a folder called output.


positional arguments: 
    folder_name      folder name where csv file is located
    csv_name         full csv file name
    
optional arguments:
    --weight WEIGHT  cut-off point to filter data based on a certain edge weight

'''


## Importing libraries

# System tools
import os

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 
from tqdm import tqdm

# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# Drawing 
import matplotlib.pyplot as plt
import networkx as nx


# Command-line interface
import argparse



## The main script


if __name__ == "__main__":
    
    # instantiating the ArgumentParser  object as parser 
    parser = argparse.ArgumentParser()
    # adding positional arguments
    parser.add_argument("folder_name", help="folder name where csv file is located")
    parser.add_argument("csv_name", help="full csv file name")
    # adding optional arguments
    parser.add_argument("--weight", help="cut-off point to filter data based on a certain edge weight", type=int)
      
    # parsing the arguments
    args = parser.parse_args()
        
    # reading the file
    input_file = os.path.join(args.folder_name, args.csv_name)
    data = pd.read_csv(input_file)
    
    
    
    
    
    # if the user input optional argument '--weight', execute this bit
    if args.weight:
        
        # filter data based of the weight input
        filtered = data[data["weight"]>args.weight]
        
        ### Creating a network visualization and saving to .png file
        
        # creating a graph object called G
        G = nx.from_pandas_edgelist(filtered, "nodeA", "nodeB", ["weight"])
        # creating a viz folder to save network visualization 
        os.mkdir("viz")
        # defining the path for the visualization
        outpath_viz = os.path.join('viz','network.png')
                       
        # defining options for network visualization
        options = {
            'node_color': 'blue',
            'node_size': 80,
            'width': 3,
            'arrowstyle': '-|>',
            'arrowsize': 10,
        }
        
        # drawing a network and saving it
        pos = nx.draw_networkx(G, arrows=True, **options)
        plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")
        
        
        ### Calculating centrality measures and saving to .csv file
    
        # degree (the number of edges connected to the node)
        degree = dict(G.degree(G.nodes()))    
        # betweenness centrality
        betweenness = nx.betweenness_centrality(G)
        # eigenvector centrality
        eigenvector = nx.eigenvector_centrality(G)
    
        # merging dictionaries into a dataframe
        df = pd.DataFrame({'degree':pd.Series(degree), 'betweenness':pd.Series(betweenness), 'eigenvector':pd.Series(eigenvector)})
        #defining .csv file name
        out_file_name = "networks.csv"
    
        # creating an output folder to save networks.csv file
        os.mkdir("output")
        # defining full filepath to save networks.csv file 
        outfile = os.path.join("output", out_file_name)
    
        # saving a dataframe as .csv
        df.to_csv(outfile)  
        
        # displaying a code status message to the user
        print("Done! Have a nice day")
    
    
    
    
    
    
    # execute this bit, if the user did not input optional argument
    else:
        
         ### Creating a network visualization and saving to .png file
        
        # creating a graph object called G
        G = nx.from_pandas_edgelist(data, "nodeA", "nodeB", ["weight"])
        # creating a viz folder to save network visualization 
        os.mkdir("viz")
        # defining the path for the visualization
        outpath_viz = os.path.join('viz','network.png')
                       
        # defining options for network visualization
        options = {
            'node_color': 'blue',
            'node_size': 80,
            'width': 3,
            'arrowstyle': '-|>',
            'arrowsize': 10,
        }
        
        # drawing a network and saving it
        pos = nx.draw_networkx(G, arrows=True, **options)
        plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")
        
        
        ### Calculating centrality measures and saving to .csv file
        
    
        # degree (the number of edges connected to the node)
        degree = dict(G.degree(G.nodes()))    
        # betweenness centrality
        betweenness = nx.betweenness_centrality(G)
        # eigenvector centrality
        eigenvector = nx.eigenvector_centrality(G)
    
        # merging dictionaries into a dataframe
        df = pd.DataFrame({'degree':pd.Series(degree), 'betweenness':pd.Series(betweenness), 'eigenvector':pd.Series(eigenvector)})
        #defining .csv file name
        out_file_name = "networks.csv"
    
        # creating an output folder to save networks.csv file
        os.mkdir("output")
        # defining full filepath to save networks.csv file 
        outfile = os.path.join("output", out_file_name)
    
        # saving a dataframe as .csv
        df.to_csv(outfile)
        
        # displaying a code status message to the user
        print("Done! Have a nice day")
    
    

