from github import Github

import os

github_acc_token = os.getenv('GH_ACC_T')
github_repo_name = os.getenv('GH_R_N')

secret_var = os.getenv("VAR")

gh = Github(github_acc_token)
print('github initialized')

repo = gh.get_repo(github_repo_name, lazy=False)

print('Var values', secret_var)

if not secret_var:
    print('Do something')
    repo.create_secret(secret_name="VAR", unencrypted_value='true')
    print('Secret updated')
else:
    print('Nothing to do')


