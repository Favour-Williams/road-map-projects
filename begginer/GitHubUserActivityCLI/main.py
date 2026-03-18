import argparse
import requests

def main():
    try:


        parser = argparse.ArgumentParser(description='GitHub User Activity CLI')
        parser.add_argument('username', type=str, help='GitHub username to fetch activity for')
        args = parser.parse_args()

        username = args.username
        url = f'https://api.github.com/users/{username}/events'

        print(f'Fetching activity for GitHub user: {username}')
        print(f'API URL: {url}')

        if username:
            print(f'Username provided: {username}')
        else:        
            print('No username provided. Please provide a GitHub username.')



        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        events = response.json()

        if not events:
            print(f'No activity found for user: {username}')
            return

        print(f'Activity for user: {username}')

        CURRENT_SUPPORTED_EVENTS = (
            "PushEvent",
            "IssuesEvent",
            "WatchEvent",
            "PullRequestEvent",
        )
        for event in events:
            event_type = event.get('type', 'Unknown Event')
            repo_name = event.get('repo', {}).get('name', 'Unknown Repository')
            if event_type in CURRENT_SUPPORTED_EVENTS:
                print(f'- {event_type} in {repo_name}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data from GitHub API: {e}')
            
    

    
if __name__ == '__main__':
    main()
