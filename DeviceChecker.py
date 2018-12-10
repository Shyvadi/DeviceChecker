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




Phone_uuids = ["", ""]
# Add phone uuids like: ["phoneuuid1", "phoneuuid2"] etc etc

editedmsg = "" # IGNORE THIS DO NOT CHANGE IT
devicecount = 0  # IGNORE THIS DO NOT CHANGE IT
for i in Phone_uuids:
    devicecount = devicecount + 1

# Add as many phone ids as you want :) - Ataku

client = discord.Client()


def initial_msg(deviceids):
    initialmsg = ""
    fmsg = []
    deviceids_length = len(deviceids)
    for i in range(deviceids_length):
        fmsg.append(["\nDevice ", i, " About to check device..."])
        initialmsg += (fmsg[i][0] + str(fmsg[i][1] + 1) + fmsg[i][2])

    return fmsg, initialmsg


def errormsg(numberofdevices):
    d_broke = []
    d_error_message = []
    numberofdevices_length = len(numberofdevices)
    for i in range(numberofdevices_length):
        d_broke.append(False)
        d_error_message.append(True)

    return d_broke, d_error_message


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

            BOT_MSG, initialmsg = initial_msg(Phone_uuids)

            fmsg = await client.send_message(message.channel, initialmsg)
            while sock == 1:

                d_broke, d_error_message = errormsg(Phone_uuids)

                time.sleep(5)

                cnx = mysql.connector.connect(user='', password='',
                                              host='', port="",
                                              database='')

                cursor = cnx.cursor()

                query = "SELECT uuid, last_seen,instance_name FROM DATABASENAME.device"

                cursor.execute(query)

                sep = '-----------------------------'

                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # DO NOT TOUCH BELOW
                # Literally so delicate you could break everything :(
                for (uuid, last_seen, instance_name) in cursor:
                    editedmsg = ""
                    print("{}, {} ".format(
                        uuid, last_seen, instance_name))
                    times = time.time()
                    int(times)
                    print("THE CURRENT TIME IS: " + str(times) + "\n\n\n\n")
                    int(times)
                    Phone_uuids_length = len(Phone_uuids)
                    for i in range(Phone_uuids_length):

                        if uuid == Phone_uuids[i]:
                            i1 = instance_name

                            if last_seen > (times - 2000):
                                BOT_MSG[i][2] = ': Device is broken FIX'
                                if d_broke[i] is True and d_error_message[i] is False:
                                    await client.send_message(message.author, ("Device ", BOT_MSG[i][1], "is Broken!"))
                                    d_error_message[i] = True
                                d_broke[i] = True

                                if last_seen > (times - 100):
                                    BOT_MSG[i][2] = ": Device is currently experiencing a error"
                                    d_broke[i] = False

                                    if last_seen >= (times - 50):
                                        BOT_MSG[i][2] = ": Device is currently experiencing a delay"
                                        d_broke[i] = False

                                        if last_seen > (times - 30):
                                            BOT_MSG[i][2] = ": Device is Online"
                                            d_broke[i] = False
                                            d_error_message[i] = False
                                            print("Device is up")

                cursor.close()
                cnx.close()

                datetime.datetime.now()

                datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
                for i in range(Phone_uuids_length):
                    editedmsg += (BOT_MSG[i][0] + str(BOT_MSG[i][1] + 1) + BOT_MSG[i][
                        2] + '\n\n' + 'Current Work: ' + i1 + '\n' + sep + '\n\n')

                await client.edit_message(fmsg, new_content=editedmsg + '\n\n**Last Update: ' + str(
                    datetime.datetime.now()) + "**")
                print("was the messaged edited?")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
