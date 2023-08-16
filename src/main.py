# Third Party Imports
from dotenv import load_dotenv

# docformatter Package Imports
from src.utils.endpoint_handler import get_access_token, get_charity_campaign, get_stream

load_dotenv()

if __name__ == "__main__":
    game_headers = {
        "type": "live",
        "game_id": "22848",  # Red Dead Redemption
    }
    token_headers = get_access_token()

    res = get_stream(token_headers, **game_headers)

    user_id = res["data"][0]["user_id"]

    res = get_charity_campaign(user_id, token_headers)

    print(res)
