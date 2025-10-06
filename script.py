
# 2. Create requirements.txt
requirements = """selenium==4.15.0
beautifulsoup4==4.12.2
requests==2.31.0
lxml==4.9.3
"""

with open(f"{project_name}/requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements)

# 3. Create .gitignore
gitignore = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
*.log

# OS
.DS_Store
Thumbs.db

# Scraped Data (optional - remove if you want to commit CSV)
# *.csv

# ChromeDriver
chromedriver
chromedriver.exe
"""

with open(f"{project_name}/.gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore)

# 4. Copy the main scraper script
with open("twine_scraper.py", "r", encoding="utf-8") as f:
    scraper_content = f.read()

with open(f"{project_name}/twine_scraper.py", "w", encoding="utf-8") as f:
    f.write(scraper_content)

# 5. Copy the sample CSV
with open("sample_scraped_profiles.csv", "r", encoding="utf-8") as f:
    csv_content = f.read()

with open(f"{project_name}/sample_scraped_profiles.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)

# 6. Copy the technical documentation
with open("Technical_Documentation.md", "r", encoding="utf-8") as f:
    doc_content = f.read()

with open(f"{project_name}/Technical_Documentation.md", "w", encoding="utf-8") as f:
    f.write(doc_content)

print("✓ requirements.txt created")
print("✓ .gitignore created")
print("✓ twine_scraper.py copied")
print("✓ sample_scraped_profiles.csv copied")
print("✓ Technical_Documentation.md copied")
