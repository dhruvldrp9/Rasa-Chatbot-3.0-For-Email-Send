# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        
        email = "akshitpatel1732@gmail.com"
        SendEmail(email,"Rasa Chatbot","This is a test mail from Rasa Chatbot.")
        # tracker.get_slot("subject"),
            # tracker.get_slot("message")
        dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(email))
        return []

def SendEmail(receiver_email,subject,message):

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "patel.dhruv13656513@gmail.com"
    password = "mlnqhedtnqncbnrs"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
    
    
    # instance of MIMEMultipart
    # msg = MIMEMultipart()

    # # storing the senders email address
    # msg['From'] = fromaddr

    # # storing the receivers email address
    # msg['To'] = toaddr

    # # storing the subject
    # msg['Subject'] = subject

    # # string to store the body of the mail
    # body = message

    # # attach the body with the msg instance
    # msg.attach(MIMEText(body, 'plain'))

    # # open the file to be sent
    # # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
    # # attachment = open(filename, "rb")
    # #
    # # # instance of MIMEBase and named as p
    # # p = MIMEBase('application', 'octet-stream')
    # #
    # # # To change the payload into encoded form
    # # p.set_payload((attachment).read())
    # #
    # # # encode into base64
    # # encoders.encode_base64(p)
    # #
    # # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # #
    # # # attach the instance 'p' to instance 'msg'
    # # msg.attach(p)

    # # # creates SMTP session
    # # s = smtplib.SMTP('smtp.gmail.com', 587)

    # # # start TLS for security
    # # s.starttls()


    # # Authentication
    # try:
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #         server.login(fromaddr, "Vinod@123")
    #         server.sendmail(
    #             fromaddr, toaddr, msg.as_string()
    # )
    #     # s.login(fromaddr, "Vinod@123")

    #     # # Converts the Multipart msg into a string
    #     # text = msg.as_string()

    #     # # sending the mail
    #     # s.sendmail(fromaddr, toaddr, text)
    # except:
    #     print("An Error occured while sending email.")
    # finally:
    #     # terminating the session
    #     server.quit()
    # return True