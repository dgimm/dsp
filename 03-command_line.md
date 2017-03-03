# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > show current working directory path = pwd  
creating a directory = mkdir
deleting a directory = rm =r
creating a file = touch
deleting a file = rm
renaming a file = mv
listing hidden files = ls -a
copying a file from one directory to another = cp
selecting all files in a directory = *
listing files in long format = ls -l
printing unique lines = uniq

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` = lists all files and directories in a directory
`ls -a`  = lists all contents in a directory including hidden files
`ls -l`  = lists all files in a directory in long format
`ls -lh` = lists all files in a directory in long format with file size
`ls -lah` = lists all contents in a directory including hidden files with file size
`ls -t`  = lists all files by modification time
`ls -Glp` = lists all files in long format without owner name and directories with /

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > My favorites are -u, c, m, r and d.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs builds and executes command lines from standard input on one or more times with initial arguments.
As an example, the following command "$ echo 1 2 3 4 | xargs" will print 1 2 3 4 using xargs.

 

