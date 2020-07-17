import psycopg2
import datetime
import sys
import os

wd = os.getcwd()
d = datetime.datetime.now()
db = d.strftime("%b%d%Y").lower()
filename = 'output-' + d.strftime("%Y-%m-%d-%H%M").lower() + '.csv'

# Connect to postgres database

print(f'''
Connecting to postgres database {db} ...
''')

conn = psycopg2.connect(host="localhost",database=db, user="postgres", password="")

cur = conn.cursor()

print(f'''
Exporting data to /data/processed/{filename} ...
''')

cur.copy_expert(f"COPY (SELECT filing_id, form_type, filer_committee_id_number, committee_name, report_code, coverage_from_date, coverage_through_date, col_a_total_individual_contributions, col_a_individual_contributions_unitemized, col_a_pac_contributions, col_a_candidate_contributions, col_a_candidate_loans, col_a_total_receipts, col_b_total_receipts, col_a_total_disbursements, col_a_cash_on_hand_close FROM fec_campaign_summaries) TO '{wd}/data/processed/{filename}' WITH (FORMAT CSV, HEADER, DELIMITER ',');", sys.stdout)