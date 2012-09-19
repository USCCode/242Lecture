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

    def render(self, afile):
        "Render the given file"
        template = jinja_environment.get_template(afile)
        self.response.out.write(template.render(self.templateValues))
    
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'Datastore Tutorial'
        self.templateValues['posts'] = Post.all().filter('stars >=', 3)
        key = db.Key.from_path('Post',3) ## Get the key for ID=4
#        self.templateValues['chosen'] = db.get(key).content #Get Post
        self.templateValues['chosen'] = self.request.path
        self.render('base.html')
        
    def post(self): # / 
        content = self.request.get('theContent')
        stars = int(self.request.get('stars'))
        if (content != ''):
            newPost = Post(content=content,stars=stars)
            newPost.put()
        self.redirect('/')
        
class SplitHandler(MyHandler):
    def get(self):
        path = self.request.path.split('/')
        self.templateValues = {}
        self.templateValues['title'] = 'Split Test'
        self.templateValues['posts'] = path
        self.render('split.html')
        

app = webapp2.WSGIApplication([('/split/.*', SplitHandler), 
                               ('/.*', MyHandler)], debug = True)
    


