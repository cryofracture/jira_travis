# Jira_Travis: Review web server log file/database and create Jira tickets

Sample data with a few http error codes included. The container will pull the top XX lines from the main log csv, and write non 200 HTTP status code lines to a new file.

Using the atlassian-python-api module, issue creation is simplified.

# Deploy Proof of Concept processor container to docker hub

Once the build succeeds, travis ci will build and push new docker container image to docker hub.