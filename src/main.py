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


class MainpageHandler(webapp2.RequestHandler):
    def get(self): # /
        self.templateValues = {}
        self.templateValues['title'] = 'jQuery Events Tutorial'
        template = jinja_environment.get_template("base.html")
        self.response.out.write(template.render(self.templateValues))
        
app = webapp2.WSGIApplication([('/.*', MainpageHandler)], debug = True)
    


