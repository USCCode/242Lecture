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

class Comment(db.Model):
    text = db.StringProperty()

class MainpageHandler(webapp2.RequestHandler):
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'jQuery Events Tutorial'
        self.templateValues['comments'] = Comment.all()
        template = jinja_environment.get_template("base.html")
        self.response.out.write(template.render(self.templateValues))
        
    def post(self):
        logging.info('Got a POST')
#        self.abort(500)
        text = self.request.get('text')
        logging.info('Got a POST text=%s=' % text)
        c = Comment(text=text)
        c.put()
        self.response.out.write("DONE")
        
    def delete(self):
#        self.abort(500)
        text = self.request.get('text') # SO, it seems that the DELETE does not accept any arguments.
                                        # I don't know if that is a webapp2 thing, or that is part of 
                                        # the HTTP specification. 
        logging.info('Got a DELETE text=%s=' % text)
        query = Comment.all().filter('text =', text)
        for c in query:
            logging.info("Deleting %s" % c.text)
            c.delete()
        self.response.out.write("DONE")
        

app = webapp2.WSGIApplication([('/.*', MainpageHandler)], debug = True)
    


