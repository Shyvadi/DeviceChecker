# DeviceChecker
Simple yet effective Device Checker for RDM (Written in python for Discord)

WHAT IT DOES:
- Posts updates for phone status every 5 seconds without spamming messages (edits a single one)
- Private messages the initiator of Device Failure

REQUIREMENTS:
- Discord.py (install with "python3 -m pip install -U discord.py")
- mysql connector (https://dev.mysql.com/downloads/connector/python/)
- Discord Bot with token ready and has read & write permissions
- 5 iPhone uuids (currently hard coded for 5 devices)
- RDM Database
- Your Discord ID (right click on your account name after typing something, click copy ID)

STEPS TO CONFIGURE BOT:

- 1: Make sure you have python 3.6 installed (Python 3.7 Will NOT work)
- 2: open DeviceChecker.py with your text editor application
- 3: Change the TOKEN to the token listed from your BOT
- 4: Change YourDiscordID to YOUR Discord ID (see how to get it in requirements)
- 5: Change the 5 Phone_uuids to 5 iPhone uuids
- 6: Scroll down until you see PART 2 HERE
- 7: Change the user, password, host, port and database to your RDM details. (database being the name of the database)
- 8: Change the query below "cursor = cnx.cursor()" to your database name
- 9: Save as DeviceChecker.py
- 10: If you are on Windows, run DeviceChecker.bat, otherwise start with "python DeviceChecker.py" while in the directory
- 11: REMEMBER TO HAVE THE BOT ON A SERVER FIRST

STEPS TO START BOT:
- 1: Once you have the py file running, simply type !start in the channel you would like the bot to post the updates
REMEMBER IT NEEDS READ/WRITE PERMS
