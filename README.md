# Free Medium Articles Bot
Open Medium articles for free

[Medium's](http://medium.com) paywall can be easily bypassed by tweeting or DMing the link and opening the shortened twitter URL 

I created a program flow diagram which outlines the processes used.

<img src="https://imgur.com/download/ztws9BS" alt="Flowchart" width=490>

To use the program, just copy a Medium link and run the program.

For even more automation, create a Automator script that runs it, so all you need to do is click on the automation or search it in Spotlight.

```applescript
on run {input, parameters}
	tell application "Terminal"
		activate
		do script with command "python twitterThing.py "
	end tell
end run
```
