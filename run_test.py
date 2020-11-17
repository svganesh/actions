import os
import subprocess

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

output = None
git_diff = None
try:
    diff_str = os.system("diff --exclude=.git -ruN main current").decode("utf-8").splitlines()
except Exception as e:
    diff_str = None
print(diff_str)

