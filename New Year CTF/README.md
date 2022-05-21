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
When I saw the home page, I figured out the type of the challenge. it is **SSRF** challenge.
in the description mentioned the robots.txt file. so first, I tried to see it but, it was forbidden.
so, i tried to know who the application work --> it was take a URL and make request and print the result in the page.
I tried to access the file, but it was not work.
Finally, I used some SSRF Payloads like: http://127.0.0.1/robots.txt or http://localhost/robots.txt but, it was some filtering prevent these payloads.
I searched a little and found this payload: http://0.0.0.0/robots.txt.
It worked perfectly.
![sh2](https://www8.0zz0.com/2021/01/19/23/188479020.png)
the robots gave us some file called: super_secret_flag_for_new_year_ctf. 
our final payload for the flag: http://0.0.0.0/super_secret_flag_for_new_year_ctf .
![sh3](https://www8.0zz0.com/2021/01/19/23/988337241.png)

### Note Checker (hard 200pts)
![note1](https://www3.0zz0.com/2021/01/19/23/627519718.png)
![note2](https://www3.0zz0.com/2021/01/19/23/261163395.png)
This was very good challenge and we enjoyed solving this one.
As you can see this looked **SQL INJECTION** Challenge. from the previous screenshots we get that there was some filtering on the input, and we could not enter more than 20 character and if we entered more than 20 characters, it would trim the other characters that came after the 20th character. 
Also, we found that there were some filters prevent the white spaces and we skipped it using this: /**/

so first we succeed to break the query and know the number of columns the table has.
we used this payload: 'order/**/by/**/4--+
![note3](https://www3.0zz0.com/2021/01/19/23/275971645.png)
it was 3 columns. After this point we took some time to break the final filter (the 20-character limit). 
After some searching time, we found that there is something called **parameter pollution**. it made us to send our payload split with & and the server concatenate it in the other side. 
After some tries, we made the correct payload: q='union/**/select/**/&q='a',sql,'a'&q=from(sqlite_master)&q=limit/**/1,1--+
![note4](https://www12.0zz0.com/2021/01/19/23/820734671.png)
Wow we had the column and table names secret(flag). 
so our final payload was: q='union/**/select/**/&q='a',flag,'a'&q=from(secret)&q=--
And we got the flag as shown.
![note](https://www12.0zz0.com/2021/01/19/23/502076450.png)

### leaf (hard 200pts)
![leaf1](https://www8.0zz0.com/2021/01/19/23/384527060.png)
This was the last one. at the beginning we tried everything, and nothing worked, and the challenge was not clear to us, especially when you read the description that was talking about a car we need to find its VIN number and this car was in city in Germany.
In the next day I think they gave us hint; it was GitHub link of some sort of list that had APIs paths.
so I tried to brute force using this list and I found this path to Car API: /leaf/api/car.
![leaf2](https://www12.0zz0.com/2021/01/19/23/709408822.png)
It had a VIN NUMBER and some other attributes like :latitude, longitude and I think this related to the description about the location of the car.
The flag was the VIN Number, I tried the VIN in the picture and did not work and remembered the description that the last 3 digits of the number I had to brute force them to get the correct VIN number. 
The parameters of latitude and longitude were indication of the place of the car and searched for the city in Germany I think was called Becham.
I found that its latitude is 52 and longitude is 8. 
, so using intruder I brute forced all vales from 000 to 999 in the last 3 digits and found that one that almost like the required latitude and longitude.
![leaf3](https://www3.0zz0.com/2021/01/20/00/273055686.png)
Done this was the correct VIN number and this was our flag.
![leaf4](https://www3.0zz0.com/2021/01/20/00/116444937.png)

**Finally, Special Thanks to my teammate Mohammed Saleh who helped me in this writeup**
