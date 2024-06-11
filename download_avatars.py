import requests
import os
import config

def download_slack_avatars(token, download_path="avatars"):
    # Getting the list of users
    users_response = requests.get('https://slack.com/api/users.list',
                                  headers={'Authorization': f'Bearer {token}'}).json()

    if not users_response['ok']:
        print("Error getting users list:", users_response.get('error', 'Unknown error'))
        return

    users = users_response['members']

    # Create a directory to save avatars
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Download each user's avatar
    for user in users:
        if not user.get('is_bot', False):
            user_id = user['id']
            # print(user)
            email = user.get('profile', {}).get('email', 'unknown')
            display_name = user.get('profile', {}).get('display_name', user_id)
            avatar_url = user['profile']['image_512']  # You can choose different sizes like image_24, image_32, etc.

            response = requests.get(avatar_url)
            if response.status_code == 200:
                with open(os.path.join(download_path, f"{email}.png"), 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded avatar for {email}")

            else:
                print(f"Failed to download avatar for {email}")


# Replace with your Slack API token
api_token = config.TOKEN

# Call the function to start downloading avatars
download_slack_avatars(api_token)
