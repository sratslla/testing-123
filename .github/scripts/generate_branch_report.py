import os
import pandas as pd
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Fetch branches data from GitHub API
def get_branches():
    url = f"https://api.github.com/repos/{REPO_NAME}/branches"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# Fetch branch details (owner, created_at, last_updated)
def get_branch_details(branch_name):
    url = f"https://api.github.com/repos/{REPO_NAME}/commits/{branch_name}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    commit_data = response.json()
    
    owner = commit_data['commit']['committer']['name']
    created_at = commit_data['commit']['committer']['date']
    last_updated = commit_data['commit']['committer']['date']  # Same for last update
    return owner, created_at, last_updated

# Collect branch data
branches_info = []
for branch in get_branches():
    branch_name = branch["name"]
    owner, created_at, last_updated = get_branch_details(branch_name)
    branches_info.append([branch_name, owner, created_at, last_updated])

# Convert to DataFrame
df = pd.DataFrame(branches_info, columns=["Branch Name", "Owner", "Created At", "Last Updated"])

# Save to Excel
df.to_excel("branches.xlsx", index=False)
print("Excel file generated successfully.")
