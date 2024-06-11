import aiohttp
import asyncio
import os
from aiohttp import ClientSession
import config


async def download_avatar(session, url, download_path, display_name):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(os.path.join(download_path, f"{display_name}.png"), 'wb') as f:
                    f.write(await response.read())
                    print(f"Downloaded avatar for {display_name}")
            else:
                print(f"Failed to download avatar for {display_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


async def download_all_avatars(token, download_path="avatars"):
    async with ClientSession() as session:
        headers = {'Authorization': f'Bearer {token}'}
        response = await session.get('https://slack.com/api/users.list', headers=headers)
        users_response = await response.json()

        if not users_response['ok']:
            print("Error getting users list:", users_response.get('error', 'Unknown error'))
            return

        users = users_response['members']

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        tasks = []
        for user in users:
            if not user.get('is_bot', False):
                user_id = user['id']
                # display_name = user.get('profile', {}).get('display_name', user_id)
                # temporary let's use email as display name
                email = user.get('profile', {}).get('email', 'unknown')
                avatar_url = user['profile']['image_512']  # Adjust image size as necessary
                tasks.append(download_avatar(session, avatar_url, download_path, email))

        await asyncio.gather(*tasks)


# Replace with your Slack API token
api_token = config.TOKEN
# Run the asynchronous download task
asyncio.run(download_all_avatars(api_token))
