'''
اكتب برنامج لاستخراج النطاق domain من ترويسة بريد الكتروني
'''

mail_header = 'From msaad@iugaza.edu.ps Sat Dec  21 09:14:16 2019'
at_pos = mail_header.find('@')
space_pos = mail_header.find(' ', at_pos)
print(mail_header[at_pos + 1:space_pos])
