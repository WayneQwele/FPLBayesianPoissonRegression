

# a list of useful functions for data manipulations

import pandas as pd

def clean_and_convert_data(filename: str):
    """ 
    This function preps and cleans the save CSV files. 
    """
    # Read the CSV file into a DataFrame
    game_df = pd.read_csv(filename)

    # List of columns to convert to string dtype
    fields_to_convert = ['name', 'position', 'team']

    # Convert specified columns to string dtype
    game_df[fields_to_convert] = game_df[fields_to_convert].astype('string')

    # Convert 'kickoff_time' and 'kickoff_date' columns to datetime dtype
    game_df['kickoff_time'] = pd.to_datetime(game_df['kickoff_time'])
    game_df['kickoff_date'] = pd.to_datetime(game_df['kickoff_date'])
    

    # Rename 'row_count' to 'matchgames'
    game_df = game_df.rename(columns={'row_count': 'matchgames'})

    return game_df


def total_point_correction(row: int):
    '''
    To correct issue with -ve points which is not condusive to my model, It is
    to be used when capping total_points from our final model.
    '''
    if row <0:
        result = 0
    else:
        result = row
    return result


