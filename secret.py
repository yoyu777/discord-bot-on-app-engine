# Import the Secret Manager client library.
from google.cloud import secretmanager

# Create the Secret Manager client.
secretmanager_client = secretmanager.SecretManagerServiceClient()

def get_discord_token(project_id,secret_id):
    latest_secret_version=secretmanager_client.access_secret_version(
        name=f'projects/{project_id}/secrets/{secret_id}/versions/latest'
    )

    discord_bot_token = latest_secret_version.payload.data.decode("UTF-8")

    return discord_bot_token