import os
import pandas

committees = ['C00665711','C00607515','C00012229']

df = pandas.read_csv('data/source/filings.csv')

compete = df[df['committee_id'].isin(committees)]

# only_competitive

q3 = compete[compete['report_type'].isin(['Q3'])]

files = list(q3['file_number'])

print(files)