import psycopg2
import sys
import os

wd = os.getcwd()
filename = 'output1.csv'

conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="")

cur = conn.cursor()

cur.copy_expert(f"COPY (SELECT committee_name, election_state, election_district, col_a_total_individual_contributions, col_a_pac_contributions, col_a_candidate_contributions, col_a_candidate_loans, col_a_total_receipts, col_b_total_receipts, col_a_total_disbursements, col_a_cash_on_hand_close FROM fec_campaign_summaries) TO '{wd}/data/processed/{filename}' WITH (FORMAT CSV, HEADER, DELIMITER ',');", sys.stdout)