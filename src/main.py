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
    tags = db.StringListProperty()

class Tag(db.Model):
    name = db.StringProperty()
    
    def reallyDelete(self):
        """ALWAYS call this instead of tag.delete() """
        for post in Post.all():
            if self.name in post.tags:
                post.tags.remove(self.name)
        self.delete()

class MyHandler(webapp2.RequestHandler):

    def render(self, afile):
        "Render the given file"
        template = jinja_environment.get_template(afile)
        self.response.out.write(template.render(self.templateValues))
    
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'Datastore Tutorial'
        self.templateValues['posts'] = Post.all()
        self.templateValues['tags'] = Tag.all()
        self.render('base.html')
        
    def post(self): # / 
        content = self.request.get('theContent')
        if (content != ''):
            newPost = Post(content=content,tags=[])
            query = Tag.all()
            for tag in query:
                if self.request.get(tag.name) == 'on':
                     newPost.tags.append(tag.name)
            newPost.put()
        tagname = self.request.get('tagname')
        if (tagname != ''):
            newTag = Tag(name=tagname)
            newTag.put()
        self.redirect('/')
        
    

app = webapp2.WSGIApplication([('/.*', MyHandler)], debug = True)
    


