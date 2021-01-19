# New Year CTF 
We are Ch4mpi0n5 team and we got the 5th place in this competition.
Team Members:
- Abanob Medhat
- Mohammed Saleh
- Hussein EL Sayed

This CTF competition was held on 24th Dec 2020 by Cybertalents.
It was good competition, so enjoy our writeup.

## WEB 

### STASHED (easy 50pts)

![sh1](https://www7.0zz0.com/2021/01/19/23/972324946.png)
When I saw the home page , I figured out the type of the challenge . it is **SSRF** challenge.
in the description mentioned the robots.txt file. so first of all i tried to see it but, it was forbidden.
so, i tried to know who the application work --> it was take a url and make request and print the result in the page.
I tried to access the file ,but it wasn't work.
Finally, I used some SSRF Payloads like: http://127.0.0.1/robots.txt or http://localhost/robots.txt but, it was some filttering prevent these payloads.
I searched a little and found this payload: http://0.0.0.0/robots.txt.
It worked perfectly.
![sh2](https://www8.0zz0.com/2021/01/19/23/188479020.png)
the robots gived us some file called: super_secret_flag_for_new_year_ctf. 
our final payload for the flag: http://0.0.0.0/super_secret_flag_for_new_year_ctf .
![sh3](https://www8.0zz0.com/2021/01/19/23/988337241.png)

### Note Checker (hard 200pts)
![note1](https://www3.0zz0.com/2021/01/19/23/627519718.png)
![note2](https://www3.0zz0.com/2021/01/19/23/261163395.png)
This was very good challenge and we enjoyed solving this one.
As you can see this looked **SQL INJECTION** Challenge. from the previous screenshoots we get that there was some filttering on the input and we couldnot enter more than 20 character and if we entered more than 20 characters ,it will trim the other characters that came after the 20th character. 
Also we found that there was some filtter prevent the white spaces and we skipped it using this : /**/

so first we successed to break the query and know the number of coloumns the table has.
we used this payload: 'order/**/by/**/4--+
![note3](https://www3.0zz0.com/2021/01/19/23/275971645.png)
it was 3 coloumns.After this point we took some time to break the final filtter (the 20 character limit). 
After some searching time , we found that there is something called **parameter polluation**. it made us to send our payload splitted with & and the server concate it in the other side. 
After some tries , we made the correct payload: q='union/**/select/**/&q='a',sql,'a'&q=from(sqlite_master)&q=limit/**/1,1--+
![note4](https://www12.0zz0.com/2021/01/19/23/820734671.png)
Wow we had the coloumn and table names  secret(flag). 
so our final payload was :q='union/**/select/**/&q='a',flag,'a'&q=from(secret)&q=--
And we got the flag as shown.
![note](https://www12.0zz0.com/2021/01/19/23/502076450.png)

### leaf (hard 200pts)
![leaf1](https://www8.0zz0.com/2021/01/19/23/384527060.png)
This was the last one. at the beginning we tried everything and nothing worked and the challenge was not clear to us , specially when you read the description that was talking about a car we need to find its VIN number and this car was in city in Germenay.
In the next day I think they gave us hint , it was github link of some sort of list that had APIs paths.
so i tried to bruteforce using this list and I found this path to Car API: /leaf/api/car.
![leaf2](https://www12.0zz0.com/2021/01/19/23/709408822.png)
It had a VIN NUMBER and some other attributes like : latitude, longtitude and I think this realted to the description about the location of the car.
The flag was the VIN Number , I tried the VIN in the picture and didn't work and remebered the decription that the last 3 digits of the number I had to bruteforce them to get the correct VIN number. 
The paramters of latitude and longtitude were indication of the place of the car and searched for the city in Germany I think was called Becham.
I found that its latitude is 52 and longitude is 8. 
,so using intruder I bruteforced all vales from 000 to 999 in the last 3 digits and found that one that almost like the required latitude and longitude.
![leaf3](https://www3.0zz0.com/2021/01/20/00/273055686.png)
Done this was the correct VIN number and this was our flag.
![leaf4](https://www3.0zz0.com/2021/01/20/00/116444937.png)

**Finally Special Thanks to my teammate Mohammed Saleh who helped me in this writeup**
