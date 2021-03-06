import discord

# Import the Secret Manager client library.
from google.cloud import secretmanager
from secret import get_discord_token
from sheets import get_question,record_answer,get_channel_id,get_question_prefix,get_question_suffix
from os import environ

project_id=environ['PROJECT_ID']
secret_id=environ['SECRET_ID']
discord_bot_token = get_discord_token(project_id,secret_id)

client = discord.Client()

def has_mentioned(mentions,id):
    for mention in mentions:
        if mention.id==id:
            return True
    return False


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel_id=get_channel_id()

    if message.author == client.user:
        await message.channel.fetch_message(message.id)
        return
    
    if message.channel.type.name=='private':
        if message.content.startswith('+question') or message.content.startswith('+Question'):
            if channel_id is None:
                await message.channel.send('Channel not set')
            else:
                question=get_question()
       
                if question is not None:
                    prompts=[
                        get_question_prefix(),
                        f'**{question}**',
                        '',
                        get_question_suffix()
                    ]
                await client.get_channel(channel_id).send('\n'.join(prompts))

        else:
            record_answer('Anonymous',message.content)

    if message.channel.id==channel_id and has_mentioned(message.mentions,client.user.id):
        record_answer(message.author.name,message.content)

client.run(discord_bot_token)
