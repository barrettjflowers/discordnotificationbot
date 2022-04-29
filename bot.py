import discord
#from etext import send_mms_via_email
from etext import send_sms_via_email

def main():

    TOKEN = ''

    client = discord.Client()

    @client.event
    async def on_ready():
        print('{0.user} logged in.'.format(client))


    @client.event
    async def on_message(message):
        username = str(message.author).split('#')[0]
        user_id = str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel.name)
        notification = client.get_channel(968275663909969951)
        print(f'{username}: {user_message} ({channel})')

        if message.author == client.user:
            return
        if message.channel.name == 'clipboard':
            
            
            #SMS
            phone_number = "PHONE NUMBER"
            message = user_message
            provider = "CARRIER"

            sender_credentials = ("EMAIL, "TOKEN/PASSWORD")

            send_sms_via_email(
            phone_number, message, provider, sender_credentials, subject=""
            )
            

            #Use this code for MMS, Disable SMS if MMS is prefered.
            """"
            #MMS
            file_path = "image.png"
            mime_maintype = "image"
            mime_subtype = "png"
            phone_number = "PHONE NUMBER"
            message = user_message
            provider = "CARRIER"

            sender_credentials = ("EMAIL", "TOKEN/PASSWORD")

            send_mms_via_email(
                phone_number,
                message,
                file_path,
                mime_maintype,
                mime_subtype,
                provider,
                sender_credentials,
            )
            """
            return
            
    client.run(TOKEN)

main()
