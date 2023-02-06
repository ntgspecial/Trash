import streamlit as st
from CheckSMTPAccess import *
import logging

st.set_page_config(page_title='Check SMTP Access',page_icon=':wave:',layout='wide')
st.title('Check SMTP Access') 

Hosts = ["smtp-mail.outlook.com", "smtp.office365.com"]
Ports = [587, 25, 465]

Host=st.selectbox('Host',Hosts)
Port=st.selectbox('Port',Ports)
Check=st.button('Check Access')
if Check:
    if CheckSmtpServer(Host, Port):
        st.success("SMTP server is accessible With "+Host+':'+str(Port))
        logging.info("SMTP server is accessible With "+Host+':'+str(Port))
    else:
        print("SMTP server is not accessible")
