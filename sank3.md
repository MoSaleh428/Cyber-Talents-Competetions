So lets begin :D

This one was a web chellange

The first thing you see is the link to [the chellange](http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/) with a phrase **understand the snake**

![picture 1](https://imgur.com/zLLvjIu)



I set my Burp Suite scope to the chellange link

And lets get into the chellange link

I saw see a blank page written in it **the snake around you somewhere**

I didn't give attention to what is written and started directory bruteforce with my burp and a few moments i saw a robots.txt file

Directly went there and found it has one dissalowed path `/index.py`

![picture 3](https://imgur.com/Nbxq7V7)


Here I found the snake :D

But still not the flag yet

I went to the file and download it

the file contains the following python code

```
import requests

req = requests.post("http://thwebsite/path/", headers={"content-type":"application/x-www-form-urlenc", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})
```

Ok this code seems to need a little modification to fit our needs

First I changed the url to the chellange url

And second the content type missing some letters, it should be `application/x-www-form-urlencoded` .. the last 4 letters were missing (oded)

I modified it and it became like this

```
import requests

req = requests.post("http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/", headers={"content-type":"application/x-www-form-urlencoded", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})
```

I used the python in interactive mode simply by writing `python3` in terminal to give me more comfort

so I imported the requests module `import requests` and entered the second part of the code

I wrote `req.content.decode()` to see the response 

**And finally the response was !!!**

The same page containing **the snake around you somewhere** :\

So there's another trick



At first moment I thought it might be a trick with the logic of flag parameter so I changed it to flase `data={"flag":"flase"}` and tried to send the request without the parameter but still the same


I thought it may be something with Auth header

this is probably to be MD5 hash

I checked it with hash-identifier tool and it confirmed that it is MD5

so I went to crack it in some rainbow table site

it the hash cracked successfully! :D

the value of the hash was *guest*



So it came on my mind like .. why dont I change it with *admin* ?

so I hashed the word *admin* with MD5 and it was `21232f297a57a5a743894a0e4a801fc3`

I substituted the new hash with the old one and send the request again

**And Bingo!!**

the response was:

`FLAG{ReqUest_heaDers_&_PyThon}the snake around you somewhere`

And I got the flag :D
