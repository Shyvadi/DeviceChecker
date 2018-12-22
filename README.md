# DeviceChecker
Simple yet effective Device Checker for RDM (Written in python for Discord)

WHAT IT DOES:
- Posts updates for phone status every 5 seconds without spamming messages (edits a single one)
- Posts Current Device Task
- Private messages the initiator of Device Failure

REQUIREMENTS:
- Discord.py (install with "python3 -m pip install -U discord.py")
- mysql connector (https://dev.mysql.com/downloads/connector/python/)
- Discord Bot with token ready and has read & write permissions
- iPhone uuids 
- RDM Database
- Your Discord ID (right click on your account name after typing something, click copy ID)

STEPS TO CONFIGURE BOT:

- 1: Make sure you have python 3.6 installed (Python 3.7 Will NOT work)
- 2: open config.py with your text editor application
- 3: Change the TOKEN to the token listed from your BOT
- 4: Change YourDiscordID to YOUR Discord ID (see how to get it in requirements)
- 5: Change the Phone_uuids to iPhone uuids (AS MANY AS YOU WANT)
- 6: Change the user, password, host, port and database to your RDM details. (database being the name of the database)
- 7: Save as config.py
- 8: If you are on Windows, run DeviceChecker.bat, otherwise start with "python DeviceChecker.py" while in the directory
- 9: REMEMBER TO HAVE THE BOT ON A SERVER FIRST

STEPS TO START BOT:
- 1: Once you have the py file running, simply type !start in the channel you would like the bot to post the updates
REMEMBER IT NEEDS READ/WRITE PERMS
