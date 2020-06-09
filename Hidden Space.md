I wasn't used to fronesics chellanges when I tried this one

But I decided to give it a try and I solved it :D

It was very fun experience

So let's begin :D

The first thing you see in the chellange is the discription which says `NASA website has been hacked but no defacement found after attack. can you see any suspicious things?` and a .pcap file with it

![image 1](https://imgur.com/D4Czq0Y.png)

I downloaded the pcap file and used tcpdump from the terminal to take a look inside with command `sudo tcpdump -r Hidden+Space.pcap`

![image 2](https://imgur.com/brbh5Mc.png)

It was a very long file, so obviously it'll need some filtering

As I saw the sender IP was in the third field I wanted to see if there's an IP that repeated a lot of times

So i used this command to filter with sender IP `sudo tcpdump -r Hidden+Space.pcap | cut -f 3 -d " " | sort | uniq -c`

The output was as the following

![image 3](https://imgur.com/QLnfhuh.png)

There was only 2 IPs which seemed one of them (192.168.0.200) is a web server because the port was referred to as http, while the other one (192.168.0.137) was obviously the attacker's IP

I tried to filter with attacker's IP to see what kind of requests he was sending, first I looked for GET requests with command `sudo tcpdump -r Hidden+Space.pcap | grep GET`

![image 4](https://imgur.com/WxBrXtx.png)

I noticed that the attacker was bruteforcing the directories, for many GET requests he sent, but with another look at the file without filtering I found that the server was responding with **404 Not Found**

So I looked for a POST request in case the attacker found some form he can exploit with command `sudo tcpdump -r Hidden+space.pcap | grep POST` but no result, so he didn't do any post requests

![image 5](https://imgur.com/PfPqoVM.png)

I tried to look if any directory replied with `200 Found` status with command `sudo tcpdump -r Hidden+space.pcap | grep "1.1 200"`, And I found only 1 response with status 200
![image 6](https://imgur.com/MIUkUlb.png)

I filtered again with time stamp to see the request sent before it, as it was sent in time 23:33:09.552984 I aproximated it to tenth part second `sudo tcpdump -r Hidden+Space.pcap | grep "23:33:09.55"`
![image 7](https://imgur.com/dRjgOso.png)

And I found the required file :D

In order to read the response which contains the page source code I used wireshark, I used filter `http.response.code == 200` and it appeared

![image 8](https://imgur.com/3O1l4jY.png)

And when I read the source code I found !

Don't be silly the past was all the easy part , too early to get the flag yet :D

There was long encrypted string which seemed to be encrypted with Base64

![image 9](https://imgur.com/oaBM6T4.png)

When I tried to decrypt it with Base64 I got a very strange string

![image 10](https://imgur.com/VNNXd9u.png)

At this moment I was really confused, WTH would this encryption be if it's not Base64 ?

I kept thinking too much till I was about to give up when this idea raise on my mind like `why don't I try to encrypt each line alone with base64 again, I may find something..`

So, I gave it a try, and I found two things:

1- the encryption was for an image that's why it gave me a bad encryption

2- the flag !
![image 11](https://imgur.com/4UDGdke.png)

And solved :D
