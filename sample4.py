import urllib2

for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line:
        print line
        
import smtplib

msg = '''\\
    ... From: Me@my.org
    ... Subject: testin'...
    ...
    ... This is a test '''
    
server = smtplib.SMTP('localhost')
server.sendmail('weizhan2668@gmail.com','weizhan8668@gmail.com', msg)
server.quit()