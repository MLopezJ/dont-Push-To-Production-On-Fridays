# dont-Push-To-Production-On-Fridays
A friendly bot that reminds us do not push to production on Fridays. The result can be found here: https://twitter.com/DontPushFridays .

## About
This is a bot who tweet every Fridays a friendly reminder for all the developers: "Don't  push to production". 

Is just a joke inspired in a serie of tweets into the dev community in Twitter. For example:
* https://twitter.com/cassidoo/status/1154809678607446016
* https://twitter.com/kvlly/status/1159797926731952129
* https://twitter.com/iamdevloper/status/1065892745246584832

The tweet contains the famous "Sign Bunny" ASCII meme, who is basically a rabbit holding a sign with the phrase "Don't push to production". 

## How it works
The project works by the interaction of two applications: the Twitter application and the Python application. Those application comunicate by an API provided by Twitter, so basically, the Python application create the ASCII art, authenticate to the Twitter application and then, make the post in the account. 

The Python application is hosted in Heroku, so, there with the help of a worker is executed the process every friday.

### Note
This project is using the Heroku Free server, so there are a limit of hour per month for the server. Always in the last week of the month, the total of the hours were consumed.