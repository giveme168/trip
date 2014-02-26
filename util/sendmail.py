#/usr/bin/env python
# -*- encoding=utf-8 -*-

import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText

class CCSendMail:
    def __init__(self,host="smtp.qq.com",username='839783834@qq.com',password='guo2919802'):
        self.__smtp=smtplib.SMTP(host)
        self.__subject=None
        self.__content=None
        self.__from=None
        self.__to=[]
        self.__style='html'
        self.__charset='gb2312'
        self.username = username
        self.password = password
        self.fromAlias='Igame'
        self.from2='Igame@chinacache.com'
        
    def close(self):
        try:
            self.__smtp.quit()
        except Exception ,e:
            pass   
    def setFromAlias(self,alias):
        self.fromAlias=alias
    def setStyle(self,style):
        self.__style = style
    def setFrom2(self,from2):
        self.from2=from2
        
    def setSubject(self,subject):
        self.__subject=subject
        
    def setContent(self,content):
        self.__content=content
        
    def setFrom(self,address):
        self.__from=address
        
    def addTo(self,address):
        self.__to.append(address)
        
    def setCharset(self,charset):
        self.__charset=charset
        
    def send(self):
        try:
            #self.__smtp.set_debuglevel(1)
            
            #login if necessary
            if self.username and self.password:
                #pass
                #self.__smtp.starttls() #only for gmail
                self.__smtp.login(self.username,self.password)
                
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = self.__subject
            aliasB6=base64.encodestring(self.fromAlias.encode(self.__charset))
            if len(self.from2)==0:
                msgRoot['From'] = "=?%s?B?%s?=%s"%(self.__charset,aliasB6.strip(),self.__from)
            else:
                msgRoot['From'] = "%s"%(self.from2)
            msgRoot['To'] = ";".join(self.__to)
            
            
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
            
            msgText = MIMEText(self.__content, self.__style,self.__charset)
            msgAlternative.attach(msgText)

            self.__smtp.sendmail(self.__from,self.__to,msgRoot.as_string())
            return True
        except Exception,e:
            print "Error ",e
            return False
        
    def clearRecipient(self):
        self.__to = []
    
    def sendHtml(self,address,title,content):
        self.setStyle('html')
        self.setFrom("<%s>"%self.username)
        if not isinstance(content,str):
            content = content.encode('gb18030')
        self.addTo(address)
        self.setSubject(title)
        self.setContent(content)
        ret = self.send()
        self.close()
        return ret
    
    def sendMoreHtml(self,addressList,title,content):
        self.setStyle('html')
        self.setFrom("<%s>"%self.username)
        if not isinstance(content,str):
            content = content.encode('gb18030')
        for address in addressList:
            self.addTo(address)
        self.setSubject(title)
        self.setContent(content)
        ret = self.send()
        self.close()
        return ret

def main():
    send=CCSendMail()    
    send.sendMoreHtml(['yu.guo@chinacache.com'],u'CCDH测试',u'测试测试测试是测试')
    #send.sendMoreHtml(['shengli.zhang@webluker.com','lihai.zhang@webluker.com','lebing.zhou@webluker.com'],u'邮件测试',u'测试，谢谢')
    
if __name__=='__main__':
    main()
