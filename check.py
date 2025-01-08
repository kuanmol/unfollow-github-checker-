import requests

# Replace with your GitHub API token
GITHUB_TOKEN = "your_personal_access_token"
GITHUB_USERNAME = "your_github_username"

# GitHub API URLs
BASE_URL = "https://api.github.com"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_following(username):
    """Fetch users you are following."""
    url = f"{BASE_URL}/users/{username}/following"
    following = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        following.extend([user['login'] for user in response.json()])
        url = response.links.get('next', {}).get('url')  # Handle pagination
    return following

def get_followers(username):
    """Fetch users following you."""
    url = f"{BASE_URL}/users/{username}/followers"
    followers = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        followers.extend([user['login'] for user in response.json()])
        url = response.links.get('next', {}).get('url')  # Handle pagination
    return followers

def find_non_followers():
    """Find users you follow but who do not follow you back."""
    print("Fetching data...")
    following = set(get_following(GITHUB_USERNAME))
    followers = set(get_followers(GITHUB_USERNAME))
    not_following_back = following - followers
    print("\nUsers not following you back:")
    for user in not_following_back:
        print(user)

if __name__ == "__main__":
    find_non_followers()
