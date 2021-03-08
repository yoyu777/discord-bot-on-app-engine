# Discord Bot on App Engine Demo

This is the code repository for Discord Bot on App Engine Demo.

## Video Tutorials

This collection of tutorials demonstrate how to create a Discord Bot on Google Cloud using Python:
1. Creating a Discord Bot on App Engine: https://www.youtube.com/watch?v=aczvOQ6S6sA
2. Using Secret Manager to Manage Tokens: https://www.youtube.com/watch?v=wb4RU5rpooQ
3. Hosting a Poll Bot: https://www.youtube.com/watch?v=wUdZKMeLG4w

Github repo: https://github.com/yoyu777/discord-bot-on-app-engine

## How to use it

1. Create a Google Cloud account: https://cloud.google.com/
2. Install `gcloud SDK` for Google Cloud: https://cloud.google.com/sdk/docs/install, and initialise it.
3. Follow the App Engine Quickstart, either [node.js](https://cloud.google.com/appengine/docs/standard/nodejs/quickstart) or [Python](https://cloud.google.com/appengine/docs/standard/python3/quickstart), to create a Google Cloud project. 
4. Clone this repository and, in the terminal, change to the `default`(for node.js) or `python` directory.
5. Deploy the Discord bot using the following commands
```
gcloud app create --project=[YOUR_PROJECT_ID]
gcloud app deploy
```
> Important: if you deploy the python bot before you deploy the node.js bot, remove the `service` line in app.yaml

## Useful Links

### Creating a Discord Bot on App Engine
- Node.js discord.js documentaition: https://discord.js.org/#/
- Python discord.py Quickstart: https://discordpy.readthedocs.io/en/latest/quickstart.html
- Creating a Bot Account: https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro (applying to both node.js and Python)
  
### Using Secret Manager to Manage Tokens
- `google-cloud-secret-manager`: https://googleapis.dev/python/secretmanager/latest/index.html
- Secret Manager Product Quickstart: https://cloud.google.com/secret-manager/docs/quickstart#secretmanager-quickstart-python

