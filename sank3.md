So lets begin :D

This one was a web chellange

The first thing you see is the link to [the chellange](http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/) with a phrase **understand the snake**

![picture 1](https://imgur.com/zLLvjIu.png)

I set my Burp Suite scope to the chellange link

And lets get into the chellange link

I saw see a blank page written in it **the snake around you somewhere**

![image 2](https://imgur.com/zA1pWLu.png)

I didn't give attention to what is written (at least till I feel I'm stuck I may consider looking for hints) and started directory bruteforce with my burp and a few moments i saw a robots.txt file

Directly went there and found it has one dissalowed path `/index.py`

![image 3](https://imgur.com/Nbxq7V7.png)

Here I found the snake :D

But still early to celebrate .. I've to find the flag

I download the file

The file contained the following python code

```
import requests

req = requests.post("http://thwebsite/path/", headers={"content-type":"application/x-www-form-urlenc", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})
```

Ok.. this code seems to need a little modification to fit our needs

First I changed the url to the chellange url `http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/`

And second the content type missing some letters, it should be `application/x-www-form-urlencoded` .. the last 4 letters were missing (oded)

I modified it and it became like this

```
import requests

req = requests.post("http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/", headers={"content-type":"application/x-www-form-urlencoded", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})
```

I used the python in interactive mode by writing `python3` in terminal to give me more flexibility

I imported the requests module `import requests` and entered the second part of the code

`req = requests.post("http://ec2-18-184-241-234.eu-central-1.compute.amazonaws.com/snak3/", headers={"content-type":"application/x-www-form-urlencoded", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})
`

And entered `req.content.decode()` to see the response

### And finally the response was !!!

The same page containing `the snake around you somewhere` :\

There's something still missing

At first moment I thought it might be a trick with the logic of flag parameter so I changed it to flase `data={"flag":"flase"}` and tried to send the request without the parameter but still the same

I thought it may be something with **Auth** header

This is probably an MD5 hash

I checked it with hash-identifier tool and it confirmed that it is MD5

So I went to crack it in some rainbow table site

It the hash cracked successfully! :D

The value of the hash was **guest**

So I thought of why dont I change it with **admin** ?

I hashed the word **admin** with MD5 and it was `21232f297a57a5a743894a0e4a801fc3`

I substituted the new hash with the old one and send the request again

### And Bingo!!

the response was: `FLAG{ReqUest_heaDers_&_PyThon}the snake around you somewhere`

![image 4](https://imgur.com/V1BGi8T.png)

And I got the flag :D
