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

def onlyLoggedin(method):
    def _onlyLoggedin(*args,**kw):
        logging.info('decorator')
        self = args[0]
        self.user = users.get_current_user()
        if self.user:
            self.templateValues = {}            
            self.templateValues['login'] = ('%s <a href="%s">Logout</a> ' 
                                            % (self.user.nickname(), users.create_logout_url('/')))            
            method(*args, **kw)
        else:
            self.redirect('/')
    return _onlyLoggedin


class MyHandler(webapp2.RequestHandler):

    def render(self, afile):
        "Render the given file"
        template = jinja_environment.get_template(afile)
        self.response.out.write(template.render(self.templateValues))
        
    def setupUser(self):
        self.user = users.get_current_user()
        if self.user:
            self.templateValues = {}
            self.templateValues['login'] = ('%s <a href="%s">Logout</a> ' 
                                            % (self.user.nickname(), users.create_logout_url('/')))
        else:
            self.redirect('/')
            return False
        return True
    
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'Organization'
        
        user = users.get_current_user()
        if user:
            self.templateValues['login'] = ('%s <a href="%s">Logout</a> ' 
                                            % (user.nickname(), users.create_logout_url('/')))
        else:
            self.templateValues['login'] = ('<a href="%s">Login</a>' % users.create_login_url(self.request.uri))        
        self.render('base.html')
        

class BlogHandler(MyHandler):    

    @onlyLoggedin        
    def get(self): # /blog
        logging.info('in get bloghandler')
        self.templateValues = {}
        self.templateValues['title'] = 'Blog'
        logging.info('here we are')
        self.render('base.html')    

        
class PostHandler(MyHandler):

    def get(self): # /post
        self.templateValues = {}
        self.templateValues['title'] = 'Post'
        logging.info('here we are')
        self.render('base.html')            
            

        
app = webapp2.WSGIApplication([('/blog.*', BlogHandler),('/post.*', PostHandler),
                               ('/.*', MyHandler)], debug = True)
    


