import requests


def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    parsed = response.json()
    
    if parsed["success"] and "data" in parsed:
        user_data = parsed["data"]
        username = user_data["login"]["username"]
        return username
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username = fetch_random_user_freeapi()
        print(f"username:{username}")
    except Exception as e:
        print("Failed to fetch:")
        print(str(e))


if __name__ == "__main__":
    main()