"""audit_repo.py"""

import os
import sys
# import yaml

# Define default values for command line arguments
default_files = []
default_actions = []

# Get input parameters from command line arguments
if len(sys.argv) > 1:
    files = sys.argv[1].split(',')
    actions = sys.argv[2].split(',')
else:
    files = default_files
    actions = default_actions

# # Get input parameters from local configuration file, if it exists
# config_file = os.path.join('.github', 'repo_audit_config.yml')
# if os.path.isfile(config_file):
#     with open(config_file, 'r', encoding="utf-8") as f:
#         config = yaml.safe_load(f)
#         files += config.get('files', [])
#         actions += config.get('actions', [])

# Check if requested files exist in the local directory
for file in files:
    if os.path.isfile(file):
        print(f"File {file} exists in the local directory.")
    else:
        print(f"File {file} does not exist in the local directory.")

# Check if requested actions exist in the local directory
for action in actions:
    if os.path.isfile(f".github/workflows/{action}"):
        print(f"Action {action} exists in the local directory.")
    else:
        print(f"Action {action} does not exist in the local directory.")
