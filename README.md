# cmpt-371 group project


In this Mini Project you will practice applying your Socket Programming knowledge. You have two options to either build a simple web/web proxy server or implement your high performing transport layer protocol. You will practice:

Socket Programming
Connection Management
Protocol Implementation & Analysis
Estimated Required Time: Total of 6-15 hours per person*
*Based on level of previous practice with python socket programming and the involved protocols, and the choice of the project.

You have the option to choose between two project choices. Option one which is implementation of a web server is the easier, but more well-defined project. The first options includes a bonus optional deliverable, and the second option, which is your choice of reliable transport protocol needs further planning and specification on your side, and therefore has 2 bonus points incorporated to its total grade. The total MP grade of option one is out of 20 [+2 bonus points] and option two is out of 22, which means possibility of 10% bonus points on both items, but with different ways of earning them.

Reminder: Step one was your team selection, which you already have submitted. So, what we will explain here will start from Step Two for both options.

 

Option One: Web & Web Proxy Servers
Step Two (10 points):

(a) You have seen socket programming at the end of Module (2) and will code simple TCP and UDP client and servers in IS(3) and IS(4) using socket programming. In the first part of your mini project, using what you learned about socket programming, and HTTP protocol, create your simple web server. (7 points)

At this step, your web server will handle one HTTP request at a time, and implements the following messages for all of the relevant methods to the client:

Code	Message
200	OK
304	Not Modified
400	Bad request
404	Not Found
408	Request Timed Out

(b) To test your web server, copy test.html Download test.htmlin the same directory of your web server. Then find out the IP address of your machine, and port used in the code for web server and type the following in your web browser:

http://IP_ADDRESS:PORT/test.html
Edit your test file, or send the request properly to test your implementation for different message scenarios. Print screen, or cut and past output and document your test procedures. (3 pts)

Step Three (8 point):

(a) For the second part of your mini project, think about a web proxy server. What is different in request handling in a proxy server and a web server that hosts your files? Write down the detailed specifications you come up with for a minimal proxy server only using the knowledge you have from module (2) slides 29-34 (2 points), and implement them (4 points).

(b) Decide the test procedure to show the working of your proxy server. Does this need possible changes at the client side? If your answer is yes, you are not required to implement them, but need to describe and find alternative ways to test your server side functionality.
Print screen, or cut and past output and document your test procedures to show. (2 points)

Bonus: Step Four (2 points):

(a) For the bonus part of your mini project, extend your web server (from step two) to its multi-threaded version, capable of handling multiple requests simultaneously. You can implement this with your main thread listening for clients at a fixed port. When your server receives a TCP connection request from a client, the TCP connection to serve the client should happen through another port. Each TCP connection requested is handled in a separate thread. (1 point)

(b) Decide the test procedure to show the multi-threaded nature of your server. Print screen, or cut and past output and document your test procedures to show. (1 point)

