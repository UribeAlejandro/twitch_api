# Standard Library Imports
import json
import os

# Third Party Imports
import requests

__all__ = ["get_access_token", "get_stream", "get_charity_campaign"]


def get_access_token():
    # TODO: Properly set the scope of the token, it must include channel:read:charity, so far not working, to be fixed on twitch dev console # noqa
    __url_token = "https://id.twitch.tv/oauth2/token"
    __client_id = os.environ.get("CLIENT_ID")
    __client_secret = os.environ.get("CLIENT_SECRET")

    __form_urlencoded = f"client_id={__client_id}&client_secret={__client_secret}&grant_type=client_credentials&scope=channel:read:charity"  # noqa

    __req = requests.post(__url_token, data=__form_urlencoded)

    if __req.status_code == 200:
        res_content = json.loads(__req.content)
        access_token = res_content["access_token"]
        token_headers = {
            "Authorization": f"Bearer {access_token}",
            "Client-Id": __client_id,
        }

        return token_headers
    else:
        raise Exception("Error: ", __req.status_code)


def get_stream(token_headers: dict, **kwargs):
    __url_stream = "https://api.twitch.tv/helix/streams"
    __req = requests.get(__url_stream, headers=token_headers, params=kwargs)

    if __req.status_code == 200:
        res_content = json.loads(__req.content)
        return res_content
    else:
        raise Exception("Error: ", __req.status_code)


def get_charity_campaign(user_id: int, token_headers: dict):
    __url_charity = "https://api.twitch.tv/helix/charity/campaigns"
    __req = requests.get(
        __url_charity, headers=token_headers, params={"broadcaster_id": str(user_id)}
    )

    if __req.status_code == 200:
        res_content = json.loads(__req.content)
        return res_content
    else:
        raise Exception("Error: ", __req.status_code)
