import os
from subprocess import check_output

print("Hello world")
print(os.environ['GITHUB_WORKFLOW'])
print(os.environ['GITHUB_ACTOR'])
print(os.environ['GITHUB_REPOSITORY'])
print(os.environ['GITHUB_EVENT_NAME'])
print(os.environ['GITHUB_EVENT_PATH'])
print(os.environ['GITHUB_WORKSPACE'])
print(os.environ['GITHUB_SHA'])
print(os.environ['GITHUB_REF'])
print(os.environ['GITHUB_HEAD_REF'])
print(os.environ['GITHUB_BASE_REF'])
print(os.environ['GITHUB_WORKSPACE'])
print(os.environ['GITHUB_SHA'])

