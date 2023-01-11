# python-discord-webhook

This is a simple class that sends a webhook message to Discord by default, looking like the following:

![](https://github.com/Vrozax/python-discord-webhook/blob/images/webhook_template.jpg?raw=true)

To obtain the webhook address, go to channel settings -> integrations -> create webhook
![](https://github.com/Vrozax/python-discord-webhook/blob/images/integrations.jpg?raw=true)

Examples of using webhooks:
-  sending messages on a specific channel.
-  sending messages from a bot that collects live information.



To edit the appearance of embed message types, review the parameters on the page:
https://discordapp.com/developers/docs/resources/channel#embed-object

and edit the lines with this code snippet:
 ``` 
 
 data["embeds"] = [
            {
                "description":description,
                "title": title
            }
        ]
```
