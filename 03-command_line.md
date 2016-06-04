# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Mkdir – make directory, ls – lists file in a directory, ditto – copy files, cat –view contents of any file, xargs – execute arguments, cp – copy files or directory , find- find files, grep – find things inside files, apropos – displays list topics in man pages, exit – exit the shell 


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  - lists directory
`ls -a`   - lists all files including hidden files
`ls -l`  - displays the long format listing
`ls -lh`  - lists files in human readable format
`ls -lah`  - lists all files including hidden files in human readable format
`ls -t`  - lists newest files first
`ls -Glp`  - lists files and directories in long format with directories with /

> > `ls`  - lists directory, `ls -a`   - lists all files including hidden files, `ls -l`  - displays the long format listing, `ls -lh`  - lists files in human readable format, `ls -lah`  - lists all files including hidden files in human readable format, `ls -t`  - lists newest files first, `ls -Glp`  - lists files and directories in long format with directories with /

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -c, ls-d, ls -l, ls -t, ls -1 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs reads an input delimitted with commas or space and executes the command asssociated. For example, if I type "ls -a | xargs -n 3" then it first gets list of all the files and directories. Each file is separated by a comma. Thus, it displays the input arguments after 3 spaces and print them in 1 line. Hence, the given command displays all files in the directory with 3 files in each row.

 

