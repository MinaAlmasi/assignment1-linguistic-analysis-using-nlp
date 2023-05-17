# Extracting linguistic features using spaCy
Repository link: https://github.com/MinaAlmasi/assignment1-linguistic-analysis-using-nlp

This repository forms *assignment 1* by Mina Almasi (202005465) in the subject *Language Analytics*, *Cultural Data Science*, F2023. The assignment description can be found [here](https://github.com/MinaAlmasi/assignment1-linguistic-analysis-using-nlp/blob/main/assignment-desc.md). 

The repository contains code for extracting linguistic features of text files. Concretely, the folllowing information is extracted from each text file: 
1. Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
2. Total number of *unique* PER, LOC, and ORGs

## Data 
The analysis is run on the [USEcorpus](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457) which is a collection of essays (1489 in total) written by Swedish university students. If you wish to read more about the dataset, please look at the ```readme.md``` in the ```in``` folder.

## Reproducibility 
To reproduce the results, please follow the instructions in the [*Pipeline*](https://github.com/AU-CDS/assignment-1---linguistic-analysis-using-nlp-MinaAlmasi#pipeline) section. 

## Project Structure 
The repository is structured as such:

```
├── README.md
├── assignment-desc.md
├── in
│   ├── USEcorpus             <---   data located here!
│   │   ├── a1
│   │   │   ├── 0100.a1.txt
│   │   │   ├── ...........
│   │   ├── a2
│   │   │   ├── ...........
│   │   ├── ...
│   │   │   ├── ...........
│   │   ├── c1
│   │   │   ├── ...........
│   └── readme.md
├── out                        <---   CSV files from analysis located here 
│   ├── a1.csv
│   ├── a2.csv
│   ├── ...
│   └── c1.csv
├── requirements.txt 
├── setup.sh                   <---    run to install reqs & dependencies in env
├── run.sh                     <---    run to activate env, run linguistic analysis
└── src
    └── extract_features.py    <---    script to run linguistic analysis
```

For simplicity, all subdirectories and files are not shown. The USEcorpus contains exactly 14 folders containing a varying number of text files. Each folder has a corresponding CSV file (e.g., folder a1 with file a1.csv) with the linguistic analysis performed. The CSV file for each folder is structured as such:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

## Pipeline
The pipeline has been tested on Ubuntu v22.10, Python v3.10.7 ([UCloud](https://cloud.sdu.dk/), Coder Python 1.77.3). 
Python's [venv](https://docs.python.org/3/library/venv.html) needs to be installed for the pipeline to work.

### Setup
Before running the script, please run setup.sh in the terminal:

```
bash setup.sh
```
This script will create a virtual environment ```env``` and install necessary packages along with the spaCy model "en_core_web_md" (see [docs](https://spacy.io/models/en) for more info).

### Running the Analysis
To run the linguistic analysis, type the following in the terminal: 
```
bash run.sh
```

This will save 14 CSV files in the [out](https://github.com/MinaAlmasi/assignment1-linguistic-analysis-using-nlp/tree/main/out) folder (one for each subdirectory).

## Author 
This repository was created by Mina Almasi:
- github user: @MinaAlmasi
- student no: 202005465, AUID: au675000
- mail: mina.almasi@post.au.dk