import os
import pandas as pd
import numpy as np


def convert_result_to_df(results):
    """Converts the JSON response from the API to a pandas DataFrame.
    Args:
        results (dict): The JSON response from the API.
    Returns:
        pandas.DataFrame: The data from the JSON response, converted to a DataFrame.
    Raises:
        ValueError: If the input is not a dictionary or does not contain 'elementList'.
        TypeError: If 'elementList' is not a list.
    """
    if not isinstance(results, dict):
        raise ValueError("The input results must be a dictionary.")
    
    if 'elementList' not in results:
        raise ValueError("The input dictionary must contain the key 'elementList'.")
    
    if not isinstance(results['elementList'], list):
        raise TypeError("The 'elementList' must be a list.")
    
    df = pd.DataFrame(results['elementList'])
    return df

def concat_dfs(df, total_df):
    """Concatenates the current DataFrame with the total DataFrame.
    Args:
        df (pandas.DataFrame): The current DataFrame to concatenate.
        total_df (pandas.DataFrame): The total DataFrame to concatenate with.
    Returns:
        pandas.DataFrame: The concatenated DataFrame.
    Raises:
        ValueError: If either of the inputs is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a pandas DataFrame.")
    
    if not isinstance(total_df, pd.DataFrame):
        raise ValueError("The input total_df must be a pandas DataFrame.")
    
    total_df = pd.concat([total_df, df], ignore_index=True)
    return total_df

def save_df_to_csv(df, province):
    """Saves the DataFrame to a CSV file.
    Args:
        df (pandas.DataFrame): The DataFrame to save.
    Returns:
        None
    """
    os.makedirs('./datasets', exist_ok=True)
    df.reset_index()
    df.to_csv(f'./datasets/all_rent_{province}.csv', index=False)
    return None

def load_data():
    df = pd.read_csv('./datasets/all_rent_asturias.csv')
    return df
   