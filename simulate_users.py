import requests
import time
import random

# Settings
NUM_USERS = 10000  # Number of users to simulate
DELAY = 0.1      # Delay between each user (in seconds)
BASE_URL = "http://127.0.0.1:5000"  # Your local Flask app

# Click bias: probability of clicking for each group
CLICK_PROB = {
    'A': 0.3,  # 30% of Group A users click
    'B': 0.7   # 70% of Group B users click
}

for i in range(NUM_USERS):
    try:
        # Step 1: Visit the homepage
        res = requests.get(f"{BASE_URL}/", allow_redirects=False)

        # Step 2: Follow redirect to landing page
        if 'Location' in res.headers:
            landing_url = BASE_URL + res.headers['Location']
            group = landing_url.split('/')[-2]
            user_id = landing_url.split('/')[-1]

            # Visit the landing page (simulates page view)
            requests.get(landing_url)

            # Step 3: Decide whether this user clicks the CTA (based on bias)
            if random.random() < CLICK_PROB[group]:
                requests.get(f"{BASE_URL}/click/{user_id}/{group}")

        time.sleep(DELAY)  # Small pause between users

    except Exception as e:
        print(f"Error on user {i}: {e}")
