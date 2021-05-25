#!/usr/bin/env python

''' ---------------- About the script ----------------

Assignment 4: Network analysis: creating reusable network analysis pipeline


This command-line tool takes a given dataset and perform simple network analysis. In particular, it builds networks based on entities appearing together in the same documents.

 - The script is able to be run from the command line.
 - It can take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"
 - For any given weighted edgelist given as an input, this script can be used to create a network visualization, which is saved in a folder called 'viz'.
 - It also creates a data frame showing the degree, betweenness, and eigenvector centrality for each node. It saves it as a CSV file in a folder called 'output'.


positional arguments: 

    -dir,     --directory:         "Directory where CSV file is located"
    -node,    --node_size:         "Node size in a network graph. Default = 20"
    -font,    --font_size:         "Named entities font size in a network graph. Default = 10"
    
    
optional arguments:

    -w,       --weight            Cut-off point to filter input data based on a certain edge weight (degree of nodes co-occurence). If not entered, all weights are included
    
    
    
    
Example:

    including all edge weights:
        $ python Assignment_4_network.py -dir ../data/weighted_edgelist.csv 

    filtering input data based on a certain edge weight:
        $ python Assignment_4_network.py -dir ../data/weighted_edgelist.csv -w 500
        
    with all self-chosen arguments:
        $ python Assignment_4_network.py -dir ../data/weighted_edgelist.csv -node 10 -font 5 -w 500 
        
'''



"""---------------- Importing libraries ----------------
"""

# System tools
import os
import sys
sys.path.append(os.path.join(".."))

# Import pathlib
from pathlib import Path

# Data analysis
import pandas as pd
from collections import Counter
from itertools import combinations 


# NLP
import spacy
nlp = spacy.load("en_core_web_sm")

# Drawing 
import matplotlib.pyplot as plt
import networkx as nx


# Command-line interface
import argparse




"""---------------- Main script ----------------
"""


def main():
    
    """------ Argparse parameters ------
    """
    
    # instantiating the ArgumentParser  object as parser 
    parser = argparse.ArgumentParser()
    # adding positional arguments
    parser.add_argument("-dir" , "--directory", help= "Directory where CSV file is located")
    parser.add_argument("-node", "--node_size", type=int, default = 20, help="Node size in a network graph. Default = 20")
    parser.add_argument("-font", "--font_size", type=int, default = 10,  help="Named entities font size in a network graph. Default = 10")
    
    # adding optional arguments
    parser.add_argument("-w", "--weight", type=int, help="Cut-off point to filter input data based on a certain edge weight (degree of nodes co-occurence). If not entered, all weights are included")
      
      
    # Parsing the arguments
    args = vars(parser.parse_args())
    
    # Saving parameters as variables
    directory = args["directory"] # CSV file directory
    weight = args["weight"] # Cut-off point to filter data"node_size"]
    node_size =args["node_size"]
    font_size=args["font_size"]
    
    
    
    """------ Reading the file, creating output folders ------
    """
    
    input_file = os.path.join(directory)
    data = pd.read_csv(input_file)
     
        
    # creating a viz folder to save network visualization, if it does not already exist 
    if not os.path.exists("../viz"):
        os.makedir("../viz")
    
    # creating an output folder to save networks.csv file, if it does not already exist 
    if not os.path.exists("../output"):
        os.makedir("../output")
    
    
    """------ Code based on input arguments ------
    """
    
    # if the user input optional argument '--weight', execute this bit
    if weight:
        
        # filter data based of the weight input
        filtered = data[data["weight"]>weight]
        
        # execute function defined above       
        network(filtered, node_size, font_size)   
    
       
    # execute this bit, if the user did not input optional argument
    else:
        # execute function defined above
        network(data, node_size, font_size)
        
    
    
    """------ Final message to the user ------
    """
   
    print("Script was executed successfully! Have a nice day")

        
        
        

"""---------------- Function ----------------
"""

def network(dataframe, node_size, font_size):
    
    """ 
    Creates a network visualization, calculates centrality measure and 
    saves the outputs to created folders 
        
    """
    
    ### Network visualization
    
    print(f"\n[INFO] Creating network visualization...")
    # creating a graph object called G
    G = nx.from_pandas_edgelist(dataframe, "nodeA", "nodeB", ["weight"])
    # creating node positions for G using Graphviz
    pos = nx.nx_agraph.graphviz_layout(G, prog = "neato")
    # drawing and saving the graph with labels
    nx.draw(G, pos, with_labels=True, node_size = node_size, font_size = font_size)

    # defining the path for the visualization
    outpath_viz = os.path.join("..", 'viz','network_viz.png')
    # saving the plot
    plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")
    # printing that it has been saved
    print(f"\n[INFO] Network visualization with labels is saved in directory {outpath_viz}")
       
    ### Centrality measures 
    
    print(f"\n[INFO] Calculating centrality measures...")    
    # degree (the number of edges connected to the node)
    degree = dict(G.degree(G.nodes()))    
    # betweenness centrality
    betweenness = nx.betweenness_centrality(G)
    # eigenvector centrality
    eigenvector = nx.eigenvector_centrality(G)
    
    # merging dictionaries into a dataframe
    df = pd.DataFrame({'degree':pd.Series(degree), 'betweenness':pd.Series(betweenness), 'eigenvector':pd.Series(eigenvector)})
    #defining .csv file name
    out_file_name = "network_measures.csv"

    # defining full filepath to save networks.csv file 
    outfile = os.path.join("..", "output", out_file_name)
    # saving a dataframe as .csv
    df.to_csv(outfile) 
    
    # printing that it has been saved
    print(f"\n[INFO] Centrality measures CSV file is saved in directory {outfile}")
       
        
    
        
        
        
        
# Define behaviour when called from command line
if __name__=="__main__":
    main()

