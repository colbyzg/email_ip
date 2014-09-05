email_ip
======

# Description:
This is a very simple script I put together to email my current external (DHCP) IP address to myself. I'm using requests to pull IP info from a URL in JSON format. Then it is emailed to my GMail account using smtplib. This script runs daily via cron.

# Usage:
<pre>
# ./email_ip.py 
To: receiver@somewhere.com
From: sender@somewhere.com
Subject: Current Home IP is: 1.1.1.1 on 07-13-2014
</pre>