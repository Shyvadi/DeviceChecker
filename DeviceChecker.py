import time
import mysql.connector
import datetime


# Work with Python 3.6
import discord

# Welcome to Ataku's Device Checker Bot for RDM. Follow the instructions in README to setup completely.
# Welcome to Ataku's Device Checker Bot for RDM. Follow the instructions in README to setup completely.
# Welcome to Ataku's Device Checker Bot for RDM. Follow the instructions in README to setup completely.
# Welcome to Ataku's Device Checker Bot for RDM. Follow the instructions in README to setup completely.
# Welcome to Ataku's Device Checker Bot for RDM. Follow the instructions in README to setup completely.


TOKEN = ''  # Token for the Bot

YourDiscordID = ''  # The ID of YOUR Discord Account (Allows only you to start the bot)
                                      # Start the bot with !start

Phone1_uuid = ""
Phone2_uuid = ""
Phone3_uuid = ""
Phone4_uuid = ""
Phone5_uuid = ""
# I will add a different method of adding more phones later but for now this bot supports 5 - Ataku

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        print(message.author.id)

        if message.author.id == YourDiscordID:
            sock = 1
            print("it works!")
            d1 = "About to check device..."
            d2 = "About to check device..."
            d3 = "About to check device..."
            d4 = "About to check device..."
            d5 = "About to check device..."

            d1_broke = False
            d1_error_message = True
            d2_broke = False
            d2_error_message = True
            d3_broke = False
            d3_error_message = True
            d4_broke = False
            d4_error_message = True
            d5_broke = False
            d5_error_message = True

            fmsg = await client.send_message(message.channel, 'Device 1: '+d1+'\n'+'Device 2: '+d2+'\n'+'Device 3: '
                                             + d3 + '\n'+'Device 4: '+d4+'\n'+'Device 5: '+d5)
            while sock == 1:

                time.sleep(5)

                # PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE
                # PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE
                # PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE
                # PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE PART 2 HERE

                # ONLY EDIT user, password, host, port, database AND THE database name IN THE query BELOW
                cnx = mysql.connector.connect(user='', password='',
                                              host='', port='',
                                              database='')

                cursor = cnx.cursor()

                # Replace sentence with database name below EDIT NOTHING ELSE
                query = "SELECT uuid, last_seen,instance_name FROM [ENTER DATABASE NAME HERE, REMOVE BRACKETS].device"

                cursor.execute(query)

                sep = '-----------------------------'

                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # Literally so delicate you could break everything :(
                for (uuid, last_seen, instance_name) in cursor:
                    print("{}, {} ".format(
                        uuid, last_seen, instance_name))
                    times = time.time()
                    int(times)
                    print("THE CURRENT TIME IS: " + str(times) + "\n\n\n\n")
                    int(times)

                    if uuid == Phone1_uuid:
                        i1 = instance_name

                        if last_seen > (times - 400):
                            d1 = 'Device is broken FIX'
                            if d1_broke is True and d1_error_message is False:
                                await client.send_message(message.author, "Device 1 is Broken!")
                                d1_error_message = True
                            d1_broke = True

                            if last_seen > (times - 100):
                                d1 = "Device is currently experiencing a error"
                                d1_broke = False

                                if last_seen >= (times - 50):
                                    d1 = "Device is currently experiencing a delay"
                                    d1_broke = False

                                    if last_seen > (times - 30):
                                        d1 = "Device is Online"
                                        d1_broke = False
                                        d1_error_message = False
                                        print("Device 1 is up")

                    elif uuid == Phone2_uuid:
                        i2 = instance_name
                        if last_seen > (times - 400):
                            d2 = 'Device is broken FIX'
                            if d2_broke is True and d2_error_message is False:
                                await client.send_message(message.author, "Device 2 is Broken!")
                                d2_error_message = True
                            d2_broke = True

                            if last_seen > (times - 100):
                                d2 = "Device is currently experiencing a error"
                                d2_broke = False

                                if last_seen >= (times - 50):
                                    d2 = "Device is currently experiencing a delay"
                                    d2_broke = False

                                    if last_seen > (times - 30):
                                        d2 = "Device is Online"
                                        d2_broke = False
                                        d2_error_message = False
                                        print("Device 2 is up")

                    elif uuid == Phone3_uuid:
                        i3 = instance_name
                        if last_seen > (times - 400):
                            d3 = 'Device is broken FIX'
                            if d3_broke is True and d3_error_message is False:
                                await client.send_message(message.author, "Device 3 is Broken!")
                                d3_error_message = True
                            d3_broke = True

                            if last_seen > (times - 100):
                                d3 = "Device is currently experiencing a error"
                                d3_broke = False

                                if last_seen >= (times - 50):
                                    d3 = "Device is currently experiencing a delay"
                                    d3_broke = False

                                    if last_seen > (times - 30):
                                        d3 = "Device is Online"
                                        d3_broke = False
                                        d3_error_message = False
                                        print("Device 3 is up")

                    elif uuid == Phone4_uuid:
                        i4 = instance_name
                        if last_seen > (times - 400):
                            d4 = 'Device is broken FIX'
                            if d4_broke is True and d4_error_message is False:
                                await client.send_message(message.author, "Device 4 is Broken!")
                                d4_error_message = True
                            d4_broke = True

                            if last_seen > (times - 100):
                                d4 = "Device is currently experiencing a error"
                                d4_broke = False

                                if last_seen >= (times - 50):
                                    d4 = "Device is currently experiencing a delay"
                                    d4_broke = False

                                    if last_seen > (times - 30):
                                        d4 = "Device is Online"
                                        d4_broke = False
                                        d4_error_message = False
                                        print("Device 4 is up")

                    elif uuid == Phone5_uuid:
                        i5 = instance_name
                        if last_seen > (times - 400):
                            d5 = 'Device is broken FIX'
                            if d5_broke is True and d5_error_message is False:
                                await client.send_message(message.author, "Device 5 is Broken!")
                                d5_error_message = True
                            d5_broke = True

                            if last_seen > (times - 100):
                                d5 = "Device is currently experiencing a error"
                                d5_broke = False

                                if last_seen >= (times - 50):
                                    d5 = "Device is currently experiencing a delay"
                                    d5_broke = False

                                    if last_seen > (times - 30):
                                        d5 = "Device is Online"
                                        d5_broke = False
                                        d5_error_message = False
                                        print("Device 5 is up")

                cursor.close()
                cnx.close()

                datetime.datetime.now()

                datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

                await client.edit_message(fmsg, new_content='Device 1: '+d1+'\n\n'+'**Current Work: '+i1 +
                                                            '\n'+sep+'\n\n''**Device 2: '
                                                            +d2+'\n\n'+'**Current Work: '
                                                            +i2+'\n'+sep+'\n\n'+'**Device 3: '+d3+'\n\n' +
                                                            '**Current Work: '+i3+'\n'+sep+'\n\n' +
                                                            '**Device 4: '+d4+'\n\n'+'**Current Work: '+i4 +
                                                            '\n'+sep+'\n\n'+'**Device 5: '+d5+'\n\n'+'**Current Work: '
                                                            +i5+'\n\n**Last Update: '+str(datetime.datetime.now()))
                print("was the messaged edited?")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
