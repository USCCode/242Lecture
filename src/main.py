'''
Created on Sep 16, 2012

@author: jmvidal
'''
import webapp2
import jinja2
import os
import logging #for debugging.
from google.appengine.api import users
from google.appengine.ext import db

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class Post(db.Model):
    content = db.StringProperty()
    stars = db.IntegerProperty()

class MyHandler(webapp2.RequestHandler):
    
    def setupUser(self):
        self.user = users.get_current_user()
        if self.user:
            self.templateValues['login'] = ('%s <a href="%s">Logout</a> ' 
                                            % (self.user.nickname(), users.create_logout_url('/')))
        else:
            self.templateValues['login'] = ('<a href="%s">Login</a>' % 
                                            users.create_login_url(self.request.uri))
            
    def render(self,afile):
        template = jinja_environment.get_template(afile)
        self.response.out.write(template.render(self.templateValues))
        
class MainpageHandler(MyHandler):
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'Main Page'
        self.setupUser()
        self.render("base.html")
        
class BlogHandler(MyHandler):
    def get(self):
        self.templateValues = {}
        self.templateValues['title'] = 'Blog Page'
        self.setupUser()
        if not self.user:
            self.redirect('/')
            return
        self.render('base.html')

        
app = webapp2.WSGIApplication([ ('/blog.*', BlogHandler),
                                ('/.*', MainpageHandler)], debug = True)
    


