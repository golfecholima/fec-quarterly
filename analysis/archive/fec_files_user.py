import os
import pandas

print(
    '''
    1. Go to https://www.fec.gov/data/filings/?data_type=efiling
    2. Set a date range for the quarter you\'re interested in
    3. Click 'Export' in the top right corner
    4. Save the file in fec-2019-q3/data/source/
    '''
)

file = input('''Paste the name of the FEC file you downloaded here ...
>''')

committees = input('''Paste a comma separated list of committee IDs here ...
>''').split(',')

print(
    '''
    Enter a comma separated list of the report types you want to include.
    
    For a list of possibilities visit: https://www.fec.gov/campaign-finance-data/report-type-code-descriptions/
    
    ''')

report_types = input('''Report types (comma separated) ...
>''').split(',')

# df = pandas.read_csv('../data/source/' + file) #USE IN DEV IPYNB
df = pandas.read_csv('data/source/' + file) #USE IN PROD

# Limit to only competitive races
competitive = df[df['committee_id'].isin(committees)]

# Limit to selected reports
# List of report_types here: https://www.fec.gov/campaign-finance-data/report-type-code-descriptions/
select_reports = competitive[competitive['report_type'].isin(report_types)]

files = list(select_reports['file_number'])

print(files)