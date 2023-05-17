'''
Script for Assignment 1, Language Analytics, Cultural Data Science, F2023

The script contains several functions which serve to extract linguistic features from text files arranged hierarchically in folders. 
Concretely, the functions are designed to retrieve information about a text file's relative frequency of different parts of speech (POS tags) 
along with the total number of entities. The exact features to be extracted can be specified in the bottom. 

By default, the script will return the relative frequency of Nouns, Verbs, Adjectives and Adverbs per 10,000 words 
along with the total number unique Person's, Locations and Organisations. 14 CSV files for each folder containing .txt files will be saved in the "out" folder.

In the terminal, run the script by typing:
    python src/extract_features.py 

@MinaAlmasi
'''
# utils
import pathlib
import re

# data wrangling
import pandas as pd

# language model for extracting linguistic features
import spacy

def text_clean(text):
    '''
    Function to clean text prior to linguistic analysis.

    Args: 
        - text: text to be cleaned

    Returns: 
        - text: cleaned text 
    '''

    # remove meta data doc strings with regex
    text = re.sub("<.*?>", "", text)

    return text


def relative_freq_count(doc, word_class:str, n:int=10000):
    '''
    Function calculating the relative frequency of a particular word class per n words (defaults to n=10000 words). 
    
    Args: 
        - doc: SpaCy doc
        - word_class: word class from the universal POS tag set (https://universaldependencies.org/u/pos/)
            - ADJ, ADP, ADV, AUX, CCONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X
        - n: number of words to count relative frequency by. Defaults to 10000
    
    Returns: 
        - relative_freq: relative frequency of chosen word class.
    '''

    # count frequency of specified word class in doc 
    freq = len([token for token in doc if token.pos_ == word_class])

    # calc word class relative frequency per n words in doc 
    rel_freq = freq/len(doc) * n

    return rel_freq

def unique_ent_count(doc, ent_label:str):
    '''
    Function counting the number of unique entities of specified label (e.g., PERSON, LOC, ORG).

    Args: 
        - doc: SpaCy doc
        - ent_label: entity label to be counted

    Returns: 
        - unique_entities: number of unique entities 
    '''

    # make list of all entities with specified entity label (ent_label)
    entities = [ent.text for ent in doc.ents if ent.label_ == ent_label]

    # find unique ents 
    unique_entities = len(set(entities))

    return unique_entities


def linguistic_analysis(input_dir:pathlib.Path, output_dir:pathlib.Path, spacy_model, word_classes:list=["NOUN", "VERB", "ADJ", "ADV"], entities:list=["PERSON", "LOC", "ORG"]):
    '''
    Function which loads text files & performs linguistic analysis on a file at a time using a SpaCY model. Saves the analysis to a CSV file.
    Extracts the relative frequency of specified word classes and counts the number of unique specified entities.

    Args:
        - input_dir: folder which contains text files (.txt only)
        - output_dir: location where CSV file should be saved
        - spacy_model: spaCy model (should already be loaded using spacy.load())
        - word_classes: word classes  to count their relative frequency (following universal POS-tags). Defaults to NOUN, VERB, ADJ, ADV
        - entities: entity labels to count their unique instances folllowing the particular SpaCY model's ent labels. Defaults to PERSON, ORG, and LOC

    Returns: 
        - saves CSV file in desired output directory
    '''
    
    ## setup ## 
    nlp = spacy_model

    #create empty list for dataframes of each txt file
    data_txts = []

    # if output directory does not exist, create it 
    output_dir.mkdir(parents=True, exist_ok=True)

    # loop over files in input directory, create paths
    for file in sorted(input_dir.iterdir()):

        # if file is a txt file, perform the operations
        if file.is_file() and file.suffix == ".txt":
            # open file as text
            with open(file, "r", encoding="ISO-8859-1") as f: 
                text = f.read()

            # clean text
            text = text_clean(text)

            # create spacy doc for text
            doc = nlp(text)

            # create dataframe
            data = pd.DataFrame()

            # define filename for text 
            data["Filename"] = [file.name]

            # calculate relative frequency for each word class in list of word_classes given
            for word_class in word_classes:
                data[f"RelFreq {word_class}"] = [relative_freq_count(doc, word_class)]

            # count unique entities in list 
            for ent_label in entities: 
                data[f"Unique {ent_label}"] = unique_ent_count(doc, ent_label)
            
            # append dataframe to dataframes list 
            data_txts.append(data)

    # concatenate all dataframes to one  
    final_data = pd.concat(data_txts,  ignore_index=True)

    # save dataframe to csv to output directory using the folder name (input_dir[-2:])
    datapath = output_dir / input_dir.name
    final_data.to_csv(f"{datapath}.csv")

def subfolder_paths(input_dir:pathlib.Path):
    '''
    Function for extracting paths for subfolders in a directory

    Args: 
        - input_dir = parent directory which contains the subdirectories that you want to extract paths from 

    Returns: 
        - subfolder_paths = paths for all subdirectories 
    '''

    subfolder_paths = []

    for subfolder in input_dir.iterdir():
        if subfolder.is_dir():  # append only paths which are folders
            subfolder_paths.append(subfolder)

    # sort 
    subfolder_paths = sorted(subfolder_paths)

    return subfolder_paths


def main():
    # define paths 
    path = pathlib.Path(__file__) # define path to current file

    input_dir = path.parents[1] / "in" / "USEcorpus" # path.parents[1] = main folder 

    output_dir = path.parents[1] / "out"

    # define subfolders in input directory
    subfolders = subfolder_paths(input_dir)

    # load model 
    nlp = spacy.load("en_core_web_md")

    # iterate over folders, work on one at a time
    for idx, subfolder in enumerate(subfolders):
        print(f"[INFO:] Working on {subfolder.name} ({idx+1} out of {len(subfolders)} folders) ...")
        linguistic_analysis(subfolder, output_dir, nlp)


if __name__ == '__main__':
    main()