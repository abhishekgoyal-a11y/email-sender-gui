from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import math
from functools import partial
from threading import *
# Size of Path

def directory_size(path):
    size_name = ['B', 'Kb', 'Mb', 'Gb']
    size = [0, 3, 6, 9, 12]
    for i in range(len(size)):
        if i < len(size_name)-1:
            if size[i] < len(str(os.path.getsize(path))) <= size[i+1]:
                return str(int(os.path.getsize(path)/int(math.pow(10, size[i])))), str(size_name[i])
        else:
            if size[i] < len(str(os.path.getsize(path))) <= size[i+1]:
                return str(int(os.path.getsize(path)/int(math.pow(10, size[i])))), str(size_name[i])
# checking the id

def check(ids):
    lists = []
    extension = ['@gmail.com', '@bennett.edu.in']
    for i in range(len(extension)):
        if ids.endswith(extension[i]):
            lists.append(True)
        else:
            lists.append(False)
    return lists

# content of email


def sendmailcontent(FROM, PASSWORD, SMTP_NUM, PORT_NUMBER):
    fromaddr = FROM
    toaddr = to_email_id_textbox.get()
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject_textbox.get()

    # string to store the body of the mail
    body = text_area.get("1.0", "end")

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    if all_file != None:
        for filename in all_file:
            if filename != '':
                attachment = open(filename, "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition',
                             "attachment; filename= %s" % filename)
                msg.attach(p)
    # status bar update text
    status_text.set("Mail Sending...")
    status.update()
    try:
        # creates SMTP session
        s = smtplib.SMTP(SMTP_NUM, PORT_NUMBER)
    # office365
        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, PASSWORD)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()

        # text and file remove
        to_email_id_textbox.delete("0", "end")
        subject_textbox.delete("0", "end")
        text_area.delete("1.0", "end")
        for i in file_labels:
            i.destroy()
        for j in file_label_delete_buttons:
            j.destroy()
        for k in file_size_list:
            k.destroy()
        file_labels.clear()
        file_label_delete_buttons.clear()
        all_file.clear()
        file_size_list.clear()

        # status bar update text
        status_text.set("Mail Sent")
        status.update()
        time.sleep(5)
        status_text.set("")
    except Exception as e:
        print(e)
        status_text.set("Mail Not Sent")
        status.update()
        time.sleep(2)
        status_text.set("")
total_file_size=0

def sendmail_threading():
    print("start")
    t1=Thread(target=sendmail)
    t1.start()
    print("stop")
# sending mail
def sendmail():
    global total_file_size
    fromaddr = from_email_id_textbox.get()
    EMAIL_NUM_ID = ['EMAIL_ID_A', 'EMAIL_ID_B', 'EMAIL_ID_C']
    for i in range(3):
        if fromaddr in os.environ.get(EMAIL_NUM_ID[i]).split(','):
            EMAIL_NUM = i
    toaddr = to_email_id_textbox.get()
    # receiver id checking
    if len(toaddr) != 0:
        if True in check(toaddr):
            for path in all_file:
                total_file_size+=os.path.getsize(path)
            # file size checking 
            if total_file_size<35000000:
                # subject check
                if len(subject_textbox.get()) == 0:
                    subject_status = messagebox.askyesno(
                        title='SUBJECT IS EMPTY', message='Do you want to procced')
                    if subject_status:
                        sendmailcontent(os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[0], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(
                            ',')[1], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[2], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[3])
                else:
                    sendmailcontent(os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[0], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(
                        ',')[1], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[2], os.environ.get(EMAIL_NUM_ID[EMAIL_NUM]).split(',')[3])
            else:
                messagebox.showinfo(title='FILE SIZE EXCEED', message='Delete some file , only 35mb file size can send')
            total_file_size=0
        else:
            messagebox.showerror(title='INVALID RECIPIENT ID',
                                 message='Please check your recipient id!')
    else:
        messagebox.showinfo(title='RECIPIENT ID',
                            message='Please enter at least one recipient id')

# delete individual file using button 
def individual_delete(a, b):
    for i in range(len(b)):
        try:
            if a.cget("text") in b[i]:
                file_labels[i].destroy()
                file_size_list[i].destroy()
                file_label_delete_buttons[i].destroy()
                file_labels.pop(file_labels.index(file_labels[i]))
                file_size_list.pop(file_size_list.index(file_size_list[i]))
                file_label_delete_buttons.pop(
                    file_label_delete_buttons.index(file_label_delete_buttons[i]))
                all_file.pop(all_file.index(all_file[i]))
        except:
            pass


# file work
global all_file
global file_labels
global file_label_delete_buttons
global file_size_label
file_labels = []
file_label_delete_buttons = []
all_file = []
file_size_list=[]

# asking for file
def addattachment():
    global filenames
    filenames = askopenfilenames(filetypes=[('All files', '*.*')])
    all_files(filenames)

# all files
def all_files(filenames):
    for i in range(len(filenames)):
        file_size, file_size_type = directory_size(filenames[i])
        if filenames[i] not in all_file:
            # file label
            file_label = Label(root, text=f'{filenames[i].split("/")[len(filenames[i].split("/"))-1]}',
                               bg='white', width=36, anchor="w", font=("Times", "13"))
            # file size label
            file_size_label = Label(root, text=f'({file_size}{file_size_type})',
                               bg='white', width=8, anchor="w", font=("Times", "13"))
            # file delete button
            file_label_delete_button = Button(
                root, text='X', command=partial(individual_delete, file_label, all_file))
            # appending part
            all_file.append(filenames[i])
            file_label_delete_buttons.append(file_label_delete_button)
            file_labels.append(file_label)
            file_size_list.append(file_size_label)
    for i in range(len(file_labels)):
        file_labels[i].place(x=485, y=56+i*30)
        file_size_list[i].place(x=812, y=56+i*30)
        file_label_delete_buttons[i].place(x=880, y=56+i*30)

        

# main fucntion start
if __name__ == "__main__":

    filenames = None
    root = Tk()
    root.geometry('920x600')
    root.title("Email Sender")
    root.wm_iconbitmap('emailsender.ico')
    root.maxsize(920, 600)
    root.minsize(920, 600)

    # from email work
    from_id = [
        os.environ.get('EMAIL_ID_A').split(',')[0],
        os.environ.get('EMAIL_ID_B').split(',')[0],
        os.environ.get('EMAIL_ID_C').split(',')[0]
    ]
    from_email_id_text = Label(
        root, text="From: ", font=("Times", "14", "bold italic"))
    from_email_id_text.place(x=20, y=10)
    from_email_id_textbox = ttk.Combobox(
        root, values=from_id, width=30, justify=LEFT, font=("Times", "14", "bold italic"))
    from_email_id_textbox.current(0)
    from_email_id_textbox.place(x=110, y=13)

    # to email work
    to_email_id_text = Label(
        root, text="To: ", font=("Times", "14", "bold italic"))
    to_email_id_text.place(x=20, y=50)
    to_email_id_textbox = Entry(
        root, width=32, font=("Times", "14", "bold italic"))
    to_email_id_textbox.place(x=110, y=50)

    # subject work
    subject_text = Label(root, text="Subject: ",
                         font=("Times", "14", "bold italic"))
    subject_text.place(x=20, y=90)
    subject_textbox = Entry(
        root, width=32, font=("Times", "14", "bold italic"))
    subject_textbox.place(x=110, y=87)

    # body text work
    scrollbar = Scrollbar(root)
    text_area = Text(root, width=57, yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area.place(x=10, y=124)

    # add attachment
    attachment = Button(root, text="Add Attachment", font=(
        "Times", "10", "bold"), command=addattachment)
    attachment.place(x=500, y=10)

    # file size exceed
    file_size_exceed = Label(root, text="(Attachment size not exceed 35 Megabytes)", font=(
        "Times", "12", "bold"), fg="red", bg="white")
    file_size_exceed.place(x=602, y=10)

    # sendmail button
    send_mail = Button(root, text="Send mail", font=(
        "Times", "10", "bold"), command=sendmail_threading)
    send_mail.place(x=260, y=530)

    # status
    status_text = StringVar()
    status = Label(root, textvariable=status_text, relief=SUNKEN,
                   anchor="w", fg="red", font=("bold"))
    status.pack(side=BOTTOM, fill=X)

    

    root.mainloop()
