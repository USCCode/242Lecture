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
import json
import urllib2
from google.appengine.api import urlfetch
from google.appengine.api import images

class Pin(db.Model):
    title = db.StringProperty()
    picture = db.BlobProperty(default=None)

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainpageHandler(webapp2.RequestHandler):
    def get(self): 
        self.templateValues = {}
        self.templateValues['title'] = 'URL Fetch Demo change'
        template = jinja_environment.get_template("base.html")
        aPin = Pin(title="Test pin")
        url = "http://www.sc.edu/Banners/CockysReadingExpress.jpg"
        aPin.picture = db.Blob(urlfetch.Fetch(url).content)
        #aPin.put()
        self.response.out.write(template.render(self.templateValues))

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        pin = Pin.all()
        first = pin.get()
        logging.info("Got %s" % first.title)
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(first.picture)
        img = images.Image(first.picture)
        h = img.height()
        w = img.width()
        
app = webapp2.WSGIApplication([('/image.*', ImageHandler),
                                ('/.*', ImageHandler)], debug = True)
    


