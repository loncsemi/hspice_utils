import numpy as np
import pandas as pd
import os

class HspiceDataLoader:
    def __init__(self):
        pass

    @classmethod
    def load_mt(self, filepath:str, prnt:bool = False)->pd.DataFrame:
        """
        Load measurement data from a file and return it as a pandas DataFrame.

        Args:
            filepath (str): The path to the file containing the measurement data.
            prnt (bool, optional): If True, prints the number of signals found and the DataFrame. Defaults to False.

        Returns:
            pd.DataFrame: A DataFrame containing the measurement data.

        Notes:
            - Lines starting with '$' or '.' are ignored.
            - The first non-ignored line is assumed to contain variable names separated by commas.
            - Subsequent lines are assumed to contain data values corresponding to the variables.
        """

        data = {}
        variables = None
        with open(filepath, 'r') as file:
            for line in file:
                if '$' in line:
                    pass
                elif line[0] == '.':
                    pass
                elif not line[0].isnumeric():
                    variables = line.split(',')
                    variables = [var.split('#')[0] for var in variables]
                    for var in variables:
                        data[var] = []
                else:
                    for i, var in enumerate(variables):
                        data[var].append(float(line.split(',')[i]))
        data_df = pd.DataFrame(data)
        if prnt:
            print(f'Found {len(variables)} singals')
            print(variables)
            print(data_df.head())
        return data_df
    
    @classmethod
    def load_multiple_mt(self, folder:str, prnt:bool = False)->dict:
        data = {}
        for root, dir, files in os.walk(folder):
            for file in files:
                if 'mt' in file:
                    filename= file.split('.')[0]
                    path = root+'/'+file
                    data[filename] = self.load_mt(path)
        if prnt:
            print(f'Found {len(data.keys())} files with .mt ending')
            for key, value in data.items():
                print(key)
                print(value.head())
        return data 

    @classmethod
    def load_printtr(self, filepath:str, prnt:bool = False)->pd.DataFrame:
        """
        Load and parse a printtr file into a pandas DataFrame.
        The function reads a file containing simulation data, extracts the time and signal values,
        and returns a pandas DataFrame with the data.
        Args:
            filepath (str): The path to the printtr file to be loaded.
            prnt (bool):    Print found singal names
        Returns:
            pd.DataFrame: A DataFrame containing the parsed data with columns for time and signals.
        Example:
            >>> df = load_printtr('/path/to/printtr/file')
            >>> print(df.head())
        Notes:
            - Lines starting with '*' are ignored as comments.
            - Lines starting with 'x' indicate a new signal.
            - Lines with 13 leading spaces contain signal names.
            - Lines with numeric values contain time and signal data.
        """
        
        data = {
            'time': []
        }
        signal_count = 0
        signals = []
        with open(filepath, 'r') as file:
            for line in file:
                if '*' in line:
                    pass
                elif line[0] != ' ':
                    if line[0] == 'x':
                        signal_count += 1
                elif line[:13] == '             ':
                    signal = line.strip()
                    signals.append(signal)
                    data[signal] = []
                elif line[2].isnumeric():
                    if len(signals) == 1:
                        data['time'].append(float(line.split()[0]))
                    data[signals[len(signals)-1]].append(float(line.split()[1]))
        if prnt:
            print(f'Found {len(signals)} singals')
            print(signals)
        return pd.DataFrame(data)

    @classmethod
    def load_multiple_printtr(self, folder:str, prnt:bool = False)->dict:
        """
        Loads multiple '.printtr' files from a specified folder and returns their contents in a dictionary.
        Args:
            folder (str): The path to the folder containing the '.printtr' files.
            prnt (bool, optional): If True, prints the number of files found and their contents. Defaults to False.
        Returns:
            dict: A dictionary where the keys are the filenames (without extension) and the values are the contents of the files.
        """

        data = {}
        for root, dir, files in os.walk(folder):
            for file in files:
                if 'printtr' in file:
                    filename= file.split('.')[0]
                    path = root+'/'+file
                    data[filename] = self.load_printtr(path)
        if prnt:
            print(f'Found {len(data.keys())} files with .printtr ending')
            for key, value in data.items():
                print(key)
                print(value.head())
        return data       

