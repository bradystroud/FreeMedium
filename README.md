# Free Medium Articles Bot
A bot that opens paid medium articles for free

I don't know why, but [Medium](http://medium.com) article's paywall can be easily bypassed by tweeting or DMing the link and opening the shortened twitter URL. This process is boring so I automated it. 

I created a program flow diagram which outlines the processes used.

<img src="https://imgur.com/download/ztws9BS" alt="Flowchart" width=490>

To use the program, just copy a Medium link and run the program.

OR

For even more automation, create a Automator script that runs it, so all you need to do is click on the automation or search it in Spotlight.
This is the AppleScript I created `on run {input, parameters}
	tell application "Terminal"
		activate
		do script with command "python3.8 twitterThing.py "
	end tell
end run`

The script tweets the link as the Twitter API's Direct Message features are trash and it was easier to simply tweet and delete.
