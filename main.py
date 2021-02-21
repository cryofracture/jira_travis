import os
# from tenable.io import TenableIO
import csv
import pandas as pd
from atlassian import Jira
from dotenv import load_dotenv
load_dotenv()
jira = Jira(
    url=os.environ['JIRA_URL'],
    username=os.environ['JIRA_USER'],
    password=os.environ['JIRA_PASS']
)

# url="https://cyofracturejira.atlassian.net/rest/api/2/issue"

#auth=HTTPBasicAuth("taylor.acree@gmail.com", os.environ['JIRA_PASS'])

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }
#print(url)
#print(jira.password)
#print(jira.username)
logfile = os.environ['LOG_PATH'] + "/" + "weblog.csv"
from itertools import islice
with open(logfile, 'r', newline='') as logfile:
    number_of_issues = 10
    for line in islice(logfile, 20):
        #line = logfile.readline()
        with open('newweblog.csv', 'a', newline='') as outfile:
            outfile.write(line)
logfile = 'newweblog.csv'

def reviewWebLog(logfile):
    with open(logfile, newline='') as csvlogfile, open('badcodes.csv', 'a', newline='') as csvout:
        #reader = csv.reader(csvlogfile, delimiter=',', quotechar='|')
        writer = csv.writer(csvout, delimiter=',', quotechar='|')
        #head = [next(csvlogfile) for x in range(10)]
        df = pd.read_csv(csvlogfile, names=['IP','Time','URL','Status'])
        for index, row in df.iterrows():
            ip = row['IP']
            url = row['URL']
            status = row['Status']

            if status != "200":
                writer.writerow(row)

    with open('badcodes.csv') as trimmed_errors:
        head_lines = csv.reader(trimmed_errors, delimiter=',')
        next(head_lines)
        for line in head_lines:
            #print(line[3])
            if line[3] == "404":
                new_issue = jira.issue_create(fields={
                    'project': 
                    {
                        'key': 'TEST'
                    },
                    'issuetype': {
                        "name": "Task"
                    },
                    "assignee": {
                        # "name": f"{os.environ['JIRA_NAME']}"
                        "id": f"{os.environ['JIRA_USERID']}"
                    },
                    'priority': {'name': 'High'},
                    "timetracking": {"originalEstimate": "1h 30m"},
                    'summary': f"IP {line[0]} recieved HTTP Error code: {line[3]}",
                    'description': f'{line}'
                })
                print(f"JIRA Issue {new_issue['key']} created.")
            elif line[3] == '206':
                new_issue = jira.issue_create(fields={
                    'project': 
                    {
                        'key': 'TEST'
                    },
                    'issuetype': {
                        "name": "Task"
                    },
                    "assignee": {
                        # "name": f"{os.environ['JIRA_NAME']}"
                        "id": f"{os.environ['JIRA_USERID']}"
                    },
                    'priority': {'name': 'High'},
                    "timetracking": {"originalEstimate": "1h 30m"},
                    'summary': f"IP {line[0]} received Partial-success issue code: {line[3]} = CDN Investigation Needed",
                    'description': f'{line}'
                })
                print(f"JIRA Issue {new_issue['key']} created.")
            elif line[3] == '302':
                new_issue = jira.issue_create(fields={
                    'project': 
                    {
                        'key': 'TEST'
                    },
                    'issuetype': {
                        "name": "Task"
                    },
                    "assignee": {
                        # "name": f"{os.environ['JIRA_NAME']}"
                        "id": f"{os.environ['JIRA_USERID']}"
                    },
                    'priority': {'name': 'Low'},
                    "timetracking": {"originalEstimate": "30m"},
                    'summary': f"IP {line[0]} received Partial-success issue code: {line[3]} Edge Server Investigation Needed",
                    'description': f'{line}'
                })
                print(f"JIRA Issue {new_issue['key']} created.")



reviewWebLog(logfile)