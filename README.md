# Email sender GUI App
It is an email sender. This GUI can send text and bulk number of files (Max. Size 35Mb).The program can send via SMTP server.
# How it works
1. Before sending mail, you have to save email ,password and port number as a environment variable
2. After this, choose from which email you want to send 
3. Enter recipient Email
3. Enter Subject and Message ,and you can also add files
4. click on "send_mail" button
# How to set environment variable
Example for gmail


EMAIL_ID_A='your@gmail.com,your password,smtp.gmail.com,465'

Similarly for EMAIL_ID_B,EMAIL_ID_C

You can add atmost 3 email

Language:-python

Library:-SMTP, OS, time, threading ,email ,math ,functools

Framework:-Tkinter

# Main Window
![freesnippingtool com_capture_20200814144015](https://user-images.githubusercontent.com/58354473/90235281-a96c3100-de3e-11ea-942d-95d8c103cf71.png)
# Alert Pop-up Window
If subject is empty
![freesnippingtool com_capture_20200814145624](https://user-images.githubusercontent.com/58354473/90235356-cb65b380-de3e-11ea-8c6d-7757f883f606.png)If Recipient field in empty      ![freesnippingtool com_capture_20200814145601](https://user-images.githubusercontent.com/58354473/90235366-cc96e080-de3e-11ea-91b9-dd4342616e0b.png)
