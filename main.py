import json
import requests
from app.helpers.github_auth import GithubAuth
repository = 'cciac-847463407359'
repo = 'mercadolibre/{}'.format(repository)
branch = 'master'
GithubAuth.get_install_token()
def disable_admins():
    r = requests.put(
        'https://api.github.com/repos/{}/branches/{}/protection'.format(repo, branch),
        headers={
            'Accept': 'application/vnd.github.luke-cage-preview+json',
            'Authorization': 'Token {}'.format(GithubAuth.get_install_token()),
            'repos_url': 'https://api.github.com/orgs/mercadolibre/repos'
        },
        json={
            "restrictions": None,
            "required_status_checks": {
                "strict": True,
                "contexts": [
                    'continuous-integration',
                    'workflow'
                ]
            },
            "enforce_admins": False,
            "required_pull_request_reviews": {
                "dismissal_restrictions": {
                "users": [],
                "teams": []
            },
                "dismiss_stale_reviews": True,
                "require_code_owner_reviews": False,
                "required_approving_review_count": 1
            }
        }
    )
    return r.json()
