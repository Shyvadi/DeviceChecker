import time
import mysql.connector
import datetime
import config
# MADE BY ATAKU

#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE
#DO NOT TOUCH THIS FILE ANYMORE

# Work with Python 3.6
import discord
i1 = [] # dont mind this :3
TOKEN = config.TOKEN

YourDiscordID = config.YourDiscordID

editedmsg = ""
Phone_uuids = config.Phone_uuids
# Add phone uuids like: ["phoneuuid1", "phoneuuid2"] etc etc
devicecount = 0
for i in Phone_uuids:
    devicecount = devicecount+1
    i1.append("")

# Add as many phone ids as you want :) - Ataku

client = discord.Client()



def initial_msg(deviceids):
    initialmsg = ""
    fmsg = []
    deviceids_length = len(deviceids)
    for i in range(deviceids_length):
        fmsg.append(["\nDevice ", i, " About to check device..."])
        initialmsg += (fmsg[i][0]+str(fmsg[i][1]+1)+fmsg[i][2])

    return fmsg, initialmsg


def errormsg(numberofdevices):
    d_broke = []
    d_error_message = []
    numberofdevices_length = len(numberofdevices)
    for i in range(numberofdevices_length):
            d_broke.append("0")
            d_error_message.append("1")

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
            d_broke, d_error_message = errormsg(Phone_uuids)
            while sock == 1:


                time.sleep(5)
                try:

                    cnx = mysql.connector.connect(user=config.user, password=config.password,
                                              host=config.host, port=config.port,
                                              database=config.database)

                    cursor = cnx.cursor()

                    cursor.execute("SELECT uuid, last_seen,instance_name FROM "+config.database+".device")
                except:
                    time.sleep(10)
                    print("MYSQL CONNECTION ISSUE")
                    print("MYSQL CONNECTION ISSUE")
                    print("MYSQL CONNECTION ISSUE")
                    print("MYSQL CONNECTION ISSUE")
                    print("MYSQL CONNECTION ISSUE")
                    cnx = mysql.connector.connect(user=config.user, password=config.password,
                                                  host=config.host, port=config.port,
                                                  database=config.database)

                    cursor = cnx.cursor()

                    cursor.execute("SELECT uuid, last_seen,instance_name FROM " + config.database + ".device")
                    print("MYSQL CONNECTION FIXED")
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
                            i1[i] = instance_name

                            if last_seen > (times - 12000):
                                BOT_MSG[i][2] = ': :no_mobile_phones:'
                                if d_broke[i] == "1" and d_error_message[i] == "0":
                                    await client.send_message(message.author, "Device " + str(
                                        BOT_MSG[i][1] + 1) + " is Having Trouble!!")
                                    d_error_message[i] = "1"
                                d_broke[i] = "1"

                                if last_seen > (times - 400):
                                    BOT_MSG[i][2] = ": :warning:"
                                    d_broke[i] = "0"

                                    if last_seen > (times - 30):
                                        BOT_MSG[i][2] = ": :white_check_mark:"
                                        d_broke[i] = "0"
                                        d_error_message[i] = "0"
                                        print("Device is up")

                cursor.close()
                cnx.close()

                datetime.datetime.now()

                datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
                for i in range(Phone_uuids_length):
                    editedmsg += (
                    BOT_MSG[i][0] + str(BOT_MSG[i][1] + 1) + BOT_MSG[i][2] + '(' + i1[i] + ')' + '\n' + sep)
                try:
                    await client.edit_message(fmsg, new_content=editedmsg + '\n\n**Last Update: ' + str(
                        datetime.datetime.now()) + "**\n:no_mobile_phones: Means dead")
                except:
                    time.sleep(5)

                    try:
                        await client.edit_message(fmsg, new_content=editedmsg + '\n\n**Last Update: ' + str(
                            datetime.datetime.now()) + "**\n:no_mobile_phones: Means dead")
                    except:
                        time.sleep(20)
                        try:
                            await client.edit_message(fmsg, new_content=editedmsg + '\n\n**Last Update: ' + str(
                                datetime.datetime.now()) + "**\n:no_mobile_phones: Means dead")
                        except:
                            time.sleep(60)
                            print("IF YOU SEE THIS THERE IS A CONNECTION ISSUE SOMEWHERE")
                            print("IF YOU SEE THIS THERE IS A CONNECTION ISSUE SOMEWHERE")
                            print("IF YOU SEE THIS THERE IS A CONNECTION ISSUE SOMEWHERE")
                            print("IF YOU SEE THIS THERE IS A CONNECTION ISSUE SOMEWHERE")
                            print("IF YOU SEE THIS THERE IS A CONNECTION ISSUE SOMEWHERE")
                            await client.edit_message(fmsg, new_content=editedmsg + '\n\n**Last Update: ' + str(
                                datetime.datetime.now()) + "**\n:no_mobile_phones: Means dead")



@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
