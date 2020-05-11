import os


sender = "akalbhor@delotte.com"
exchange_server = ""
port = mail_details.split("|")[2]
emails = mail_details.split("|")[3].split(";")

subject = "Autotest Report | " + db_comp + " | " + process_start_time
text_msg = "<p>Hi All,<br/><br/> &emsp; Auto Test has successfully completed its process and Please see the log file content from the Autotest run below: </p></br>" + full_table + "</br></br>Regards,</br><b>AutoTest DFTE</b>"
msg = MIMEText(text_msg, 'html')
msg['From'] = sender
msg['To'] = ','.join(emails)
msg['Subject'] = subject
# msg.attach(MIMEText(text_msg, 'plain'))
# msg.attach(MIMEText(body, 'plain'))
mail_body = msg.as_string()
# Send the message via exchange server
s = smtplib.SMTP(exchange_server, port)  # We need to provide the MSexchange server detail here
s.sendmail(sender, emails, mail_body)
# resultLabel.insert(INSERT,"Email has sent.")
s.quit()

hostname = "www.deloitte.com" #example
response = os.system("ping " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')

else:
  print (hostname, 'is down!')