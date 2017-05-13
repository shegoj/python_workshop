#  Python For Linux Admin [ May 2017]

This guide provides simple practical steps to learning and using Python, as a Linux administrator. It will take about an hour to complete

---

## 

You will try out different excercises using Python to implement various Devops tasks

---

## Intended Audience

Users with basic understanding of Linux, Git, Bash.

---

## Requirements

Ensure the following is installed and working

- create 1 AWS EC2 Instances and ensure you are able to connect to each one of them via Putty
- create a git account on Github to push your code.

**DO NOT PROCEED UNTIL THESE ARE PRESENT**

---

## Intro

- Python is a versatile programming language commonly used by Linux admin. It is popular for its  rich set of libraries and non-steep learing curve

---

###  Task 1: Prepare your Linux server Python

- Connect to AWS Server
- Update yum, install git 
- Configure name and email
- Create a repo in github, call it 'python_repo'
- Check if Python is installed. We will be using Python 2.x
- Confirm your Python version

#### Update yum, install Jenkins and Java (OpenJDk 1.8.0)

    sudo yum update -y
    sudo yum install wget -y
    sudo yum install git -y

#### configure name and email

    git config --global user.name "Olu Mike"
    git config --global user.email "shegoj@yahoo.com"

#### Create a repo in github, call it 'python_repo'

    Log on to you github account and create a repo --  (python_repo)


#### Check if Python is installed

    type `python`. This takes you to Python prompt . Use ctrl+d to quit. You can also get the version with python --version




### Task 2. Simple Tasks in Python ( via python prompt).

- add 2 + 3 + 4
- print "Hello, welcome to the workshop" in Python 
- Set a variable _name, set it to your name, then update greeting to include your name . e.g "Hello, Mike. Welcome to the workshop"
- Ask for participant name and then display as print "Hello,Mike. Welcome to the workshop"
- Now exit python prompt. Implement the above as a complete script [LABEL 1]
- Update the script to pick name up as a argument instead of prompting for it.   [LABEL 2]


#### add 2 + 3 + 4

    python
    2+3+4

#### print "Hello, welcome to the workshop"

    print 'Hello, welcome to the workshop'

#### Set a variable _name .....

    _name='Mike'
    print 'Hello', _name, 'welcome to the workshop'


#### Ask for participant name .....

    _name=raw_input('WHAT IS YOUR NAME? ')
    print 'Hello', _name, 'welcome to the workshop'


#### Now exit python prompt. Implement the above .....

    USE ctrl+d 
    create a directory: mkdir -p ~/development/python && cd  ~/development/python
    create a file label1.py . Copy content of  LABEL 1 from code.txt
    use python label1.py to run the code
    you could also run it by making the file and executable (chmod +x label1.py) , then execute (./label1.py)

#### Update the script to pick name up as .....
    create a file label2.py . Copy content of  LABEL 2 from code.txt
    use python label2.py Michael to run the code
    you could also run it by making the file and executable (chmod +x label2.py Michael) , then execute (./label1.py Michael)


### Task 3. Working with functions.

### Simple Interest calculation and persistence
- Use python to calculate simple interest with principal = 50, time, 2, rate 15 . Formular is (p*t*r/100)
- Write every computed data to disk --- P=50 t=2 r=15 I=20.0


#### Use python to calculate simple interest with principal = 50, time, 2, rate 15 . Formular is (p*t*r/100)
    create a file label3.py . Copy content of  LABEL 3 from code.txt
    (./label3.py 50 2 15)

#### Write every computed data to disk --- P=50 t=2 r=15 I=20.0
    create a file label4.py . Copy content of  LABEL 4 from code.txt
    (./label4.py 50 2 15)
    open data.txt

### Task 4. String,list, dict and files. 

- split string ("ec2-user: x :1000:1000:Cloud user:/home/ec2-user:/bin/bash") into list using ":" as delimiter. The display the list. Do this in Python prompt
- display first and last elements of the list.  
- replace the third element of the list with '000000000' and check that has successfully been replaced.
- again using string ("ec2-user: x :1000:1000:Cloud user:/home/ec2-user:/bin/bash"), and  ":" as a delimiter,use a loop to iterate over the elements



#### split string ("ec2-user: x :1000:1000:Cloud user:/home/ec2-user:/bin/bash") into list using ":" as delimiter. ....
    user_info="ec2-user: x :1000:1000:Cloud user:/home/ec2-user:/bin/bash".split(':')
    user_info

#### display first and last elements of the list.
    user_info [0]


#### replace the third element of the list with '000000000' and check that has successfully been replaced.
    user_info [2] 
    user_info [2] =  "000000000"
    user_info [2]


#### use a loop to iterate over the elements
    for iterator_  in "ec2-user: x :1000:1000:Cloud user:/home/ec2-user:/bin/bash".split(':'):
    	print iterator_

### Task 5. woorking with files.
- open /etc/passwd file and display all the records in there
- display only record that matches ec2-user record
- Now write this as a complete script which accepts user-id , and display the user-id,name and home direcotry, if a match is found



#### open /etc/passwd file and display all the records in there
    with open ('/etc/passwd','r') as f:
    	for line in f:
    		print line

#### open /etc/passwd file and display all the records in there
    with open ('/etc/passwd','r') as f:
    ...	for line in f:
    		 if ( line.split(':') [0] == 'ec2-user'):
    		 	print line


#### Now write this as a complete script  [I'll leave that to you ]



### Task 6. More on Interacting with Linux Apps and Files.

- display ALL os envrionment variables
- Now display ALL of them as 'key', 'value'
- display 'hostname' variable value
- Add a new os local variable, call it TUTORIAL, set it to WORKSHOP. Then extract it via Python



#### display ALL os envrionment variables
    >>> import os
    >>> print os.environ

#### Now display ALL of them as 'key', 'value'
    >>> import os
    >>> for k, v in os.environ.items():
    ...     print "%s=%s" % (k, v)


#### display 'hostname' variable value
    >>> import os
    >>> print os.environ.get('HOSTNAME')

#### display 'hostname' variable value
    use ctrl+d to eit Python prompt
    export TUTORIAL=WORKSHOP
    python
    >>> import os
    >>> print os.environ.get('TUTORIAL')


## Summary

We have looked at basics of Python Language. We shall now be using it to perform Admin tasks



##Todo [ For next class]
- Adapt email.py script to send and email to your account. Also improve it to send  accept "send to address" 
- Improve the script to send an attachment if one is provided.



