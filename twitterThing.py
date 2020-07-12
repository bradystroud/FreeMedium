# Imports
import tweepy
import webbrowser
import pyperclip as pb

#Passwords and stuff idk
auth = tweepy.OAuthHandler("H07fh19J1pGWArifdPyKsQ99D", "Z7IJuk5R1BafyZH1Urcrp5WLv0gC7P7TBIlXkxxDxD4McTuL25") #These wont work dont try and use them 
auth.set_access_token("900251723767336961-JjsEBlMVGTYCSR7gUf8nR6RlEGXmwZx", "2vFoKfUowvKlYf53BAORlN5JrbRrkVxAnl2LrRzPPSfIz")
api = tweepy.API(auth) # API

#gets URL in clipboard, sends tweet, returns tweet ID
def tweetURL():
    clipboard = pb.paste() #gets clipboard
    print(clipboard) 
    id = api.update_status(clipboard).id # Sends tweet, gets the tweet ID as status
    return id # calls getMessage func with status

#gets tweet and deletes it. opens tweet contents(URL) in default browser
def getMessage(statusId):
    request = api.get_status(statusId).text # gets tweet using the statusId
    print(request) # prints tweet text
    webbrowser.open_new_tab(request) # tries to open body in default browser
    api.destroy_status(statusId) # deletes tweet

#Main
def main():
    newTweetID = tweetURL() #Tweet ID, return value from tweetURl()
    print("TWEET ID: " + str(newTweetID)) # print status
    getMessage(newTweetID)

if __name__ == "__main__":
    main()
