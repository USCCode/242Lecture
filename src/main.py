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

class MyHandler(webapp2.RequestHandler):

    def render(self, afile):
        "Render the given file"
        template = jinja_environment.get_template(afile)
        self.response.out.write(template.render(self.templateValues))
    
    def get(self):
        self.templateValues = {}
        self.templateValues['title'] = 'This is the title.'
        query = Post.all()
        self.templateValues['posts'] = query
        self.render('base.html')
        
    def post(self):
        content = self.request.get('theContent')
        newPost = Post(content=content)
        newPost.put()
        self.redirect('/')
        
    

app = webapp2.WSGIApplication([('/.*', MyHandler)], debug = True)
    


