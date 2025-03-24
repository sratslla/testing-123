import os
import pandas as pd

WIKI_REPO = f"https://x-access-token:{os.getenv('GITHUB_TOKEN')}@github.com/{os.getenv('REPO_NAME')}.wiki.git"

# Clone the Wiki
os.system("git clone " + WIKI_REPO + " wiki")
os.chdir("wiki")

# Load branch data
df = pd.read_excel("../branches.xlsx")

# Convert DataFrame to Markdown table
md_table = df.to_markdown(index=False)

# Write to Wiki page
wiki_page = "Branch-Report.md"
with open(wiki_page, "w") as f:
    f.write("# Branch Report\n\n")
    f.write(md_table)

# Commit and push
os.system("git add .")
os.system('git commit -m "Updated branch report in Wiki"')
os.system("git push")

print("Branch report updated in Wiki.")
