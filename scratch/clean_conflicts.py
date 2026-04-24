import os
import re

def clean_conflict_markers(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to keep HEAD version (the block between <<<<<<< HEAD and =======)
    # and discard the block between ======= and >>>>>>>
    # Pattern: <<<<<<< HEAD\n(.*?)\n?=======\n?.*?\n?>>>>>>> [^\n]+
    # We use re.DOTALL to match across lines
    
    pattern = r'<<<<<<< HEAD\n(.*?)\n?=======\n?.*?\n?>>>>>>> [^\n]+'
    cleaned_content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    
    if cleaned_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        print(f"Cleaned {file_path}")
    else:
        print(f"No markers found in {file_path}")

files_to_fix = [
    r'c:\Users\mesfi\OneDrive\Documents\week0\Demo\app\main.py',
    r'c:\Users\mesfi\OneDrive\Documents\week0\Demo\scripts\README.md',
    r'c:\Users\mesfi\OneDrive\Documents\week0\Demo\notebooks\benin_eda.ipynb',
    r'c:\Users\mesfi\OneDrive\Documents\week0\Demo\notebooks\compare_countries.ipynb',
    r'c:\Users\mesfi\OneDrive\Documents\week0\Demo\notebooks\togo_eda.ipynb'
]

for file in files_to_fix:
    if os.path.exists(file):
        clean_conflict_markers(file)
    else:
        print(f"File not found: {file}")
