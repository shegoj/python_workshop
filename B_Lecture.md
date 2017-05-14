#  Python For Linux Admin [ May 2017]

This guide provides simple practical steps to learning and using Python, as a Linux administrator. It will take about an hour to complete

---

##  DAY 2



###  Task 1:Working with files and directories

- run the create_artifact script ( so create files and diectory you are going to be working with)
- list all the files in loggings directory ( shown in two ways)
- list all files that begin with bi_ loggings directory
- Now backup (copy) all files that begin with b_ loggings direcotry into /tmp/dump/b_ directory
- backup files older than 3  days into /tmp/dump/old directory 


- Update script to display summary of files copied ( i.e. name,  and size) (TODO)
- Update the script to email  you the summary.    (TODO)
- Configure scrpt to every 15 minutes.   (TODO)

#### run the create_artifact script ( so create files and diectory you are going to be working with)

    Copy content of  LABEL 1 from code2.txt
    cd ~/loggging

#### list all the files in loggings directory ( shown in two ways)

    Label 2
    Label 3

#### list all files that begin with bi_ loggings directory

    Label 4

#### Now backup (copy) files with b_

    Label 5

#### backup files older than 3  days into /tmp/dump/old 

    Label 6



### Task 2. Working with CGI.

- Create Hello World web Page in Python
- Update the script to accept a name  and say hello, "name".
- Update the script to accept last name anf include it in its greeting (TODO)
- Add a male/female button. and include choice greeting. e.g "Hello Mark, Andrew. You are a male. (TODO)
   


#### Create Hello World web Page in Python

    instal Apache (HTTPD) web server . sudo yum install httpd
    start httpd. sudo httpd start
    sudo vi /var/www/cgi-bin/hello.py   [LABEL 7] ]
    sudo chmod + x /var/www/cgi-bin/hello.py
    update AWS security to allow  HTTP in-bound access
    access http://yourip/cgi-bin/hello.py
    Also try [LABEL 8], use a differnt name this time

#### Update the script to accept a name  and say hello, "name".

    Label 9







## Summary

We have looked at basics of Python Language. There are few codes for you to explore before you take on a mini project. The project relates to using Google Map REST utility





