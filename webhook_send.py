import requests  # dependency
from urllib import request
import urllib


class webhook_send:
    def __init__(self):
        pass

    def send_message(self, username, avatar_url ,url_webhook, content,description, title):
        url = url_webhook

        data = {
            "content": content,
            "username": username,
            "avatar_url":avatar_url
        }


# for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object

        data["embeds"] = [
            {
                "description":description,
                "title": title
            }
        ]

        
        
        result = requests.post(url,json=data)
        
        #If you want to send an additional file, uncomment the following two lines. Remember that sending a file may extend the time it takes to send the webhook!
        
        #files={'upload_file': open('files_path','rb')}
        #result = requests.request("POST", url, json = data,files=files)

         

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(
                result.status_code))