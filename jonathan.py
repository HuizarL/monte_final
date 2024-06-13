import discord 
import os  
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

load_dotenv() 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
token = str(os.getenv('TOKEN')) 

print(f'This is my Ec2_metadata.region:', ec2_metadata.region)
print(f'This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))

@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}')

	if message.author == client.user: 
		return

	if channel == "rodney": 
		if user_message.lower() == "hi": 
			await message.channel.send(f"Hey! {username}") 
			return
		elif user_message.lower() == "do that lil dance you be doing":
			await message.channel.send(f'Gotchu gang')
			goku_griddy_gif_url = "https://tenor.com/view/goku-fortnite-griddy-fortnite-griddy-fortnite-dance-gif-26487780" 
			await message.channel.send(goku_griddy_gif_url)
		elif user_message.lower() == "tell me a joke": 
			await message.channel.send(f'why did jaycob cross the road?')
		elif user_message.lower() == "why":
			await message.channel.send(f'idk man ask someone else')
		elif user_message.lower() == "show me ethan":
			await message.channel.send(f'https://tenor.com/view/dog-gif-25785258')
		elif user_message.lower() == "nah the other one":
			await message.channel.send(f'Yup my fault')
			weekend_emote_gif_url = "https://tenor.com/view/peter-griffin-popular-vibe-fortnite-fortnite-dance-family-guy-gif-5744247130420082937"
			await message.channel.send(weekend_emote_gif_url)
		elif user_message.lower() == "say hi to logan":
			logan_gif = "https://tenor.com/view/greetings-hello-logan-logan-gif-27636571"
			await message.channel.send(logan_gif)
		elif user_message.lower() == "do the rick thing":
			await message.channel.send(f'allo')

client.run(token)