import requests

token = "put token here"
un = "github username here"

# GitHub API URLs
BASE_URL = "https://api.github.com"
HEADERS = {"Authorization": f"token {token}"}

def get_following(username):
    url = f"{BASE_URL}/users/{username}/following"
    following = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        following.extend([user['login'] for user in response.json()])
        url = response.links.get('next', {}).get('url')  # Handle pagination
    return following

def get_followers(username):
    url = f"{BASE_URL}/users/{username}/followers"
    followers = []
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        followers.extend([user['login'] for user in response.json()])
        url = response.links.get('next', {}).get('url')  # Handle pagination
    return followers

def find_non_followers():
    print("Fetching data...")
    following = set(get_following(un))
    followers = set(get_followers(un))
    not_following_back = following - followers
    print("\nUsers not following you back:")
    for user in not_following_back:
        print(user)

if __name__ == "__main__":
    find_non_followers()
