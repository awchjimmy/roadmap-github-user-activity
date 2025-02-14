import sys
import requests

def analysis(activities):
    for activity in activities:
        if activity['type'] == 'PushEvent': # push commits
            print('- Pushed {0} commit to {1}'.format(1, activity['repo']['name']))
        elif activity['type'] == 'CreateEvent' and activity['payload']['ref_type'] == 'repository': # create repos
            print('- Created repository {0}'.format(activity['repo']['name']))
        elif activity['type'] == 'WatchEvent': # star repos
            print('- Starred {0}'.format(activity['repo']['name']))
        

def main():
    # get username
    username = ''
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print('Usage: python github-activity.py <username>')
        return
    
    try:
        # make request
        endpoint = 'https://api.github.com/users/{0}/events'.format(username)
        resp = requests.get(endpoint)
        resp.raise_for_status()

        # analysis
        analysis(resp.json())
    except Exception as e:
        print('Something went wrong when making request to Github API.')
        print('Could not find the user or other issues.')

if __name__ == '__main__':
    main()
