import pandas as pd
import pickle


def clean_momentum_data(filename, col):
    '''
        This function will take the filename of a csv containing data (one variable) on a bunch of stocks and
        and separate that data into dataframes that contain the returns for a single PERMNO. This data will be saved
        in the Monthly Returns folder.

        Input: filename of dirty data csv, names of columns to use, placed in a list

        Output: csv of returns for single PERMNO
    '''

    dirty_data = pd.read_csv(filename, index_col=['LPERMNO', 'datadate'], usecols=col, parse_dates=True)

    dirty_data = dirty_data.unstack(level=0)

    # Forward fill any NaNs
    dirty_data.fillna(method='ffill', inplace=True)

    all_securities = dirty_data.columns.values.tolist()  # Creates list of tuples (Variable name, PERMNO).


    for security in all_securities:
        filename = 'Monthly Returns/' + str(security[1]) + '_monthly_return.csv'
        dirty_data[security].to_csv(filename, index_label='datadate', header=['trt1m'])

    return


# Create Return CSVs - for use with Momentum portfolio construction.
file = 'MR.csv'
col = ['trt1m', 'LPERMNO', 'datadate']
clean_momentum_data(file, col)


# # Now, let's save the pairings between PERMNO and company name - just for our reference later on
# df = pd.read_csv('MR.csv', index_col=['datadate'], )
# with open('permno_company_pairs.txt', 'wb+') as file:


