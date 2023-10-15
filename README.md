# PONDR Protein Sequence Automation

This project contains a script that automates the process of uploading protein sequences to PONDR (Predictor of Natural Disordered Regions) and downloading the results.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed Python 3.x
* No need of prior knowledge of Python.
* You have a stable internet connection

## Installing Libraries
To install the necessary Python libraries, run the following command:

    pip install selenium 
    pip install pyautogui

## Using PONDR Protein Sequence Automation
To use the script, follow these steps:
* Store all your protein sequences, in FASTA format, within one text file, ensuring a line separates each sequence. For guidance, refer to the 'example-sequence-analyse.txt' file.
* Name the protein sequences file as 'sequence-analyse.txt' (without qoutes ;)
* Run the scripts using the command:

    python pondr_automation.py

Note: The sequence-analyse.txt and python scripts should be in same folder.

The script will upload each protein sequence to PONDR, and automatically saved the results in pdf format.

## Troubleshooting
If you encounter any issues while using the script, please check your internet connection and ensure that the PONDR website is currently accessible.

## License
This project uses the following license: MIT License (https://opensource.org/license/mit/)

## Sequences used in example-sequence-analyse.txt
https://www.rcsb.org/structure/8HBK
https://www.rcsb.org/structure/8KH4
https://www.rcsb.org/structure/8CI1
https://www.rcsb.org/structure/8EQ6
