import argparse

def main():
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

    
if __name__ == '__main__':
    main()
