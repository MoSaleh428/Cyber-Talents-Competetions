This is write up for web security CTF organized by cybertalents in 19 November 2020

I achieved 8th in the CTF with solving all the challenges

Some of the challenges in the CTF was repeated in previous challenges so there's no point in repeating them again so I'll just mention the previous write ups for them

My friend Abanob Medhat Contributed with writing RCE Me and readable write ups so credits goes to him

So let's begin :)



## icoan (100pts):
[https://n33rdz.github.io/Blog/Egypt-National-CTF-2020-Cybertalents/](https://n33rdz.github.io/Blog/Egypt-National-CTF-2020-Cybertalents/)



## R3cova (100pts):
[https://medium.com/sud0root/ctf-writeups-sudan-national-ctf-2020-web-challenges-writeups-5b3d183e93c3](https://medium.com/sud0root/ctf-writeups-sudan-national-ctf-2020-web-challenges-writeups-5b3d183e93c3) 



## r34lity(200pts):
[https://ouahabs.github.io/2020/cybertalents-algeria-quals-2020-writeup/](https://ouahabs.github.io/2020/cybertalents-algeria-quals-2020-writeup/)



## Bean (50pts):

I opened the page to find a picture of Mr. Bean in the index page.. nothing else

![image 1](https://i.imgur.com/yQmJgxS.png)

As there's nothing in the page itself nor in its source code I ran directory brute force using dirsearch tool

The brute force found a directory named /files/ .. I navigated into it to find that it contains the files of /etc/ directory in linux

![image 2](https://i.imgur.com/tkjTLhS.png)

Nothing was interesting in the directory itself.. and I got stuck on what to do here

Until I noticed that the server running the website is Nginx, which is known for the Nginx alias traversal vulnerability

![image 3](https://i.imgur.com/ORrYbSe.png)

I navigated into /files../ to find if the vulnerability exists and it was :)

![image 4](https://i.imgur.com/uuO0uGx.png)

Now I can navigate anywhere in the server.. so I went too /file../home/flag.txt and got the flag

![image 5](https://i.imgur.com/7J6n03r.png)



## Upgrade (50 pts):

The web page had an upload functionality and saying that there's system upgrade and it asks me to upload source file

![image 1](https://i.imgur.com/h3hOSIM.png)

I made a file named source and zipping it in a file named file.zip and uploaded it

![image 2](https://i.imgur.com/VnrHzJI.png)

The site has revealed me some files and it ran cat command to read the source file content

I went to see what's in the robots.txt file and I found the location of the flag

![image 3](https://i.imgur.com/NQDbb8q.png)

I thought of many things like uploading something other than zip file or injecting os command payload in source file name but none worked

So I thought of.. maybe it's related to links

If I uploaded a source file linked to the flag then It'll read the flag file

I searched a lot on how to put link file in zip file *because it wouldn't do this normally*, and I found that I can use --symlinks option to zip link files

So I made a link from source file to /home/flag and zipped it

![image 4](https://i.imgur.com/jyMiyz7.png)

Uploading the zip file

![image 5](https://i.imgur.com/PmzALtG.png)

Challenge solved..



## Notebook (100pts):

The web page had a file upload functionality to upload a note and a place to print some info about the uploaded note

![image 1](https://i.imgur.com/w0KgtOZ.png)

It also contained a sample file to download and see how the uploaded file should be

![image 2](https://i.imgur.com/xuBop2d.png)

Uploading the sample file to see how it's printed

![image 3](https://i.imgur.com/5F3bahY.png)

And I got (Title, sub, Description) info of the sample file, The title value was `DocX!`

So to exploit this I knew there's some xxe vulnerability with docx files.. but never tried it actually, and here's my chance :D

I googled for the vulnerability and found this blog [https://doddsecurity.com/312/xml-external-entity-injection-xxe-in-opencats-applicant-tracking-system/](https://doddsecurity.com/312/xml-external-entity-injection-xxe-in-opencats-applicant-tracking-system/)

The docx is actually a zip file that contain some xml files

So to exploit this.. I unziped the docx file and tried to search for which file contained the `DocX!` string, and I found it in docProps/core.xml

![image 4](https://i.imgur.com/eszcWa8.png)

I opened the file with text editor and injected xxe payload in it `<!DOCTYPE bruh [<!ENTITY bruh SYSTEM "file:///etc/passwd">]>`

And called the entity `&bruh;` in title field

![image 5](https://i.imgur.com/nB44CKH.png)

Returning the modified core.xml file to the sample.docx

![image 6](https://i.imgur.com/rL3kXzs.png)

And upload again

![image 7](https://i.imgur.com/DcPmOIc.png)

I can read the files now :)

A hint was given in the challenge description that the flag is in home directory 

![image 8](https://i.imgur.com/pkcoQAx.png)

So I changed the core.xml file to read in the payload from `file:///etc/passwd` to `file:///home/flag` and repeated the previous steps again

![image 9](https://i.imgur.com/gjVO9AB.png)

And uploaded the docx file

![image 10](https://i.imgur.com/O0FQkgp.png)

BOOM, I got the flag :)



## Limited (100pts):

I entered the web page to find a text `Do you think you can get in?!` with input field and a button named pwn, well.. lets see if I can

![image 1](https://i.imgur.com/OiGn7rY.png)

I checked the source of the page to find hidden anchor tag contains src.txt 

![image 2](https://i.imgur.com/v2mocC8.png)

I went there and found the source code

![image 3](https://i.imgur.com/hUNfgQf.png)

All the past was the easy part.. the coming is the trouble

The source code has a variable contains some blacklisted words

It takes the q post parameter which we found in the index page and checks if it contains any of the blacklisted words

->If it match.. it just echoes with image

->If it didn't match.. it checks for the length if it's more than 40

  -> If it is more than 40.. it just says `Length is too long`

  -> If not it append it to the query `SELECT $q||flag from Flag` notice that $q is the post parameter then it returns the result of the query row by row.. the two pipes `||` by default in mysql means or .. but in this case when need it to mean concatenate

Enough of analyzing the code and let's try to exploit it

I made local database to try the payloads locally and see the outputs with fake flag

![image 4](https://i.imgur.com/sKmopY5.png)

It works.. now let's see what happens if I put empty string `''` as input

![image 5](https://i.imgur.com/RvydAIc.png)

This returns nothing..

One of the hints the organizers gave for this challenge is `do you know what is Server SQL Modes` so I searched for it in google and read this documentation [https://mariadb.com/kb/en/sql-mode/](https://mariadb.com/kb/en/sql-mode/)

I knew that to set sql mode you just need to enter `SET sql_mode='some_mode';`

I didn't know which mode to use there are many.. So i returned to read the source code again to find blacklisted string `pipes_as_concat` which is one of sql modes

I tried it locally and it worked

![image 6](https://i.imgur.com/25aayQp.png)

So That is what I need

But since it's blacklisted I need alternative for it

Little search.. many alternatives, I choosed the shortest one to not exceed the length limit.. which is `ansi`

![image 7](https://i.imgur.com/7rFwhV9.png)

It works too, So let's try to simulate the server side query

![image 8](https://i.imgur.com/sovpKq4.png)

Everything seems to bee fine now.. lets send the payload

![image 9](https://i.imgur.com/p9vznfF.png)

But the server had other opinion :(

It doesn't trigger any of the errors in the code neither replies with the query result

I thought it is because of some non-disclosed restriction for the single quotes so I tried to inject some simple payload that prints hello

![image 10](https://i.imgur.com/43Q3Qu9.png)

It's clear now I can't print strings, but it's not a problem.. I can print numbers :)

So replaced the empty double single quotes in the payload with 1

![image 11](https://i.imgur.com/tEBojuX.png)

And I got the flag :)


## Home Blog (100pts):

When I entered the page it contained a blog with index page contains image with word DEMO shaking in it

![image 1](https://i.imgur.com/KhHVMqF.png)

The blog had 4 pages (Home, About, Services, Contact)

Navigating into them nothing was interested in the content.. but the url was interesting

![image 2](https://i.imgur.com/EzR82qA.png)

The url contained a get parameter named after the blog page like `?file=about`

It seems like it reads the file from somewhere.. That's propably LFI

I tried to read index.php page and I found the php source code

![image 3](https://i.imgur.com/hHU79a9.png)

```
<?php
  $file = $_GET["file"];
  if(preg_match("/^\s*\/|^\s*http:\/\/|^.*?\.\..*?$/", $file)){echo "<center><h3>HOME</h3></center>";}
  if(!empty($file)){
    if(!preg_match("/^\s*\/|^\s*file:\/\/|^.*?\.\..*?$/", $file)){
      $page =  file_get_contents($file);
      if($page){
        echo $page;
      }else{
        echo "<center><h3>HOME</h3></center>";
      }
    }
  }else {
    echo file_get_contents("home");
  }
?>
```

But's clear now that it reads the file using `file_get_contents()` function

But it validates the input using preg_match with regex in it and if it matcs.. it kicks you out

![image 4](https://i.imgur.com/0QkW8yp.png)

I got notice of it doesn't check the letters case when it checks for file wrapper

So I bypassed it by changing it to File:// instead of file://

![image 5](https://i.imgur.com/jC6YBUU.png)

I searched for the flag in most common places it could be and found it in File://home/flag

![image 6](https://i.imgur.com/Q90bs3L.png)

And I got the flag :)


## Echo Tango Sierra (100pts):

The web page looked like a profile with picture, name, description and last active time and some other things

![image 1](https://i.imgur.com/b5pePMu.png)

When I first opened the web page I noticed that it loaded then refreshed again.. that's wierd

I checked the the burp suite to find that it set 3 cookies then refreshed again to load the profile information from it

![image 2](https://i.imgur.com/XwhZbVM.png)

The 3 cookies are (profile_id, _user_session, profile_info)

The Interesting one was the profile_info that was base64 encoded

`Tzo0OiJVc2VyIjozOntzOjE0OiIAVXNlcgB1c2VybmFtZSI7czoxNjoiTGltYSBDaGFybGllXzAxMSI7czoxMzoiAFVzZXIAaXNBZG1pbiI7YjowO3M6NjoiYWN0aXZlIjtzOjExOiIxNjA1OTc1NDIwCiI7fQ==`

I decoded it to get the following

`O:4:"User":3:{s:14:"Userusername";s:16:"Lima Charlie_011";s:13:"UserisAdmin";b:0;s:6:"active";s:11:"1605975420";}`

It's php serialized object

Firstly I changed the boolean value of UserisAdmin to 1 but it only changed the description and the picture, nothing else..

![image 3](https://i.imgur.com/QuzMhp0.png)

I was thinking about php insecure deserialization but unfortunately I didn't have source code to do so

A hint they gave for the challenge to check the time, which is active parameter

I thought it's php code injection, but it wasn't

It was OS command injection worked

I changed its value to `1605975420;echo hello;` , also I changed the length value *which is the length of the parameter value string* from 22 to not get server error, encoded it and send again

And it worked

![image 4](https://i.imgur.com/qPUIQsB.png) 

Now let's execute more interesting command like `1605975420;cat /etc/passwd/;` , again changed the length again, encode and send

![image 5](https://i.imgur.com/JdL92Ef.png)

And I got the flag in it :)



## Mr. Agent (200pts):

Going into the link directly I found this page

![image 1](https://i.imgur.com/v2t24W8.png)


So it's website for some wine company with many pages in it

I ran directory brute force using dirsearch tool and navigated into the pages with burp suite proxieng the requests

After I made sure all the pages requested along with the robots.txt I found in directory brute force

![image 2](https://i.imgur.com/30N6V31.png)

![image 3](https://i.imgur.com/pkJnNmO.png)

I noticed something in the requests.. most of the pages had no cookies and suddenly at the end I got a cookie

![image 4](https://i.imgur.com/6gLFSSL.png)

I returned to burp proxy http requests to see when did I get it and found it was set when I navigated policy.php page

![image 5](https://i.imgur.com/BIb0ZrS.png)

I made two requests.. one with the file name in the cookie and the other without the cookie and sent them to burp comparer to see the difference

![image 6](https://i.imgur.com/jzLdOvK.png)

Ok I'm sure now it's reading something and know where it's displayed, let's try something more interesting by setting the cookie value to /etc/passwd

![image 7](https://i.imgur.com/Le9Qyhr.png)

And I got the content of it :)

I know previously from robots.txt content that the flag is in /etc/flag_48cbe4247cc8f7937ff091f257b4e160.txt .. so let's get it

![image 8](https://i.imgur.com/JRQ1n9E.png)

bruh.. I hit WAF

I returned to see the challenge description it had nothing important.. but the challenge name made sense.. along with the hint the organizers gave for the challenge "At some point mr agent would help you" .. it became clear that I'm going to use user agent

So i searched in google for user agent with lfi and found that I can get rce by two methods which are close the same

the first is to inject php payload in user agent such as `<?php echo hi;?>` and read /proc/self/environ file which stores the environment of the current session

Once it read the php code stored in the file it'll execute it

but.. unfortunately I couldn't read this file

So I tried the second method which is reading the /var/log/apache2/access.log .. the apache server logs .. and it'll just do the same

![image 9](https://i.imgur.com/bAVahKE.png)

And I got the flag

I didn't inject the payload in user agent so I think someone already injected the payload and it was stored in the file so when I read it again it got executed

Or the challenge was just to read the logs file considering it enough to pass it

Either of them.. it worked
