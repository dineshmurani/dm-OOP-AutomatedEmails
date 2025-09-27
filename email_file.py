import yagmail

email = yagmail.SMTP(user='pythoncourse1@gmail.com', password="python_pro_course_1")
email.send(to='ypddjuio@yomail.info',
           subject='Hi there!',
           contents="Hi, This is the body of the email!\nDinesh",
           attachments='design.txt')