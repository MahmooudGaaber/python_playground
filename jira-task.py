from jira import JIRA

#jira search query
jql_query = 'project = "Tuba" ORDER BY created DESC'

# define the connection between my app and jira 
def setupConnection():
      jiraOptions = {'server': "https://trytuba-eg.atlassian.net/"}
      global  jira 
      jira = JIRA(
      options=jiraOptions, 
      basic_auth=(
            "m.gaber@tubahealth.com", 
            "ATATT3xFfGF0rjkyFYqu8XTY9IRJv7qNAZV_an7I2-UXfa8NRzb0L9cR1RaAUUdLUZ2M_fUVW0OUV0FYd6amhaTWB21_l4nIfoWxlBYbrNRkvdvb_wf5AeRffiJ9yy1uq15qsc_LUVQy0Rm2--5arPMgiNcG98Ky4SOZLEZrPc3xXcfLgLSTHh8=CBB2B909"
            )
      )

def getTickets():
      issues = jira.search_issues(jql_query, maxResults=3)
      for issue in issues:
            print(f"Key: {issue.key} | Summary: {issue.fields.summary} | Status: {issue.fields.status.name}")


setupConnection()
getTickets()