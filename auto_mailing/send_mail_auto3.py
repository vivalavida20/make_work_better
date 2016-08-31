# -*- coding: utf-8 -*-
#이메일 자동전송 프로그램입니다.
# 출처: http://naelshiab.com/tutorial-send-email-python/

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import pandas as pd

#엑셀 파일 불러오기
mail_file =  pd.ExcelFile('email_lists.xlsx')
mail_chunk = mail_file.parse('Sheet1')
#series 객체로 쪼갬
mail_series = mail_chunk['Email']
name_series = mail_chunk['Name']
text_series = mail_chunk['Text']
title_series = mail_chunk['Title']

#리스트 객체로 변환
mail_list = pd.Series.tolist(mail_series)
name_list = pd.Series.tolist(name_series)
text_list = pd.Series.tolist(text_series)
title_list = pd.Series.tolist(title_series)

#bcc 리스트 엑셀 파일 불러오기
bcc_file = pd.ExcelFile('bcc_list.xlsx')
bcc_chunk = bcc_file.parse('Sheet1')
bcc = pd.Series.tolist(bcc_chunk['bcc'])

fromaddr = #'받으실분'

#헤더 만들기
def make_msg(i):
    toaddr = mail_list[i]

    COMMASPACE = ', '
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = Header(s=title_list[i], charset='utf-8')
    msg.attach(MIMEText(text_list[1], 'plain', _charset="utf-8"))

    return msg.as_string()

#메일보내기
def send_mail():
    Port = 587
    Server = 'smtp.gmail.com'

    print(Server + ":" + str(Port) + "connecting...")
    try:
        server = smtplib.SMTP(Server, Port)
        print("Server Connected")
        try:
            server.starttls()
            try:
                server.login(#EMAIL_ADDRESS, #Password)
                print("Login Success")
                try:
                    for i in range(len(mail_list)):
                        try:
                            server.sendmail(fromaddr, [mail_list[i], bcc], make_msg(i))
                            print("make_msg success")
                        except:
                            print("make_msg unsucceed")
                    print("Mail Sended")
                except:
                    print("Sending Mail Failed")
            except:
                print("Login Failed")

        except:
            print("[Error] Failed to send mails")
        finally:
            server.quit()
    except:
        print("[Error] Could not Connect.")
        return False

send_mail()
