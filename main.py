import discord

# Import the Secret Manager client library.
from google.cloud import secretmanager

# GCP project in which to store secrets in Secret Manager.
project_id = "discord-bot-demo-304514"

# ID of the secret to create.
secret_id = "discord-bot-token"

# Create the Secret Manager client.
secretmanager_client = secretmanager.SecretManagerServiceClient()

response=secretmanager_client.access_secret_version(
    name=f'projects/{project_id}/secrets/{secret_id}/versions/1'
)

# Print the secret payload.
#
# WARNING: Do not print the secret in a production environment - this
# snippet is showing how to access the secret material.
discord_bot_token = response.payload.data.decode("UTF-8")


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(discord_bot_token)
