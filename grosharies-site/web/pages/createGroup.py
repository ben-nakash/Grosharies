#from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

from models.group import Group
from models.user import User
import webapp2

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		g_id = None
		if (Group.checkIfGroupNotExists("Habanai 30","Ilya") is True):
			group = Group()
			group.GroupName = "Habanai 30"
			group.GroupAdmin = "Ilya"
			g_id = group.put()
			group = Group()
			#group.GroupName = "Habanai 30"
			group.GroupUsers = "Ben"
			#group.GroupAdmin = "Ilya"
			g_id = group.put()
			#g_id = group.key.id()
			#if(User.checkIfUserNotExists("Ilya") is True):
			user = User()
			user.email = "Ilya"
			user.GroupID = group.key.id()
			user.put()
		
		#user1 = User()
		#user1.email = "Elad"
		#if (g_key is None):
		#	user1.GroupID = None
		#else :
		#	user1.GroupID =g_key
		#user1.put()
		
		
#		user = User.checkUser()
#		if not user:
#			template_params['loginUrl'] = User.loginUrl()
#		else:
#			template_params['logoutUrl'] = User.logoutUrl()
#			template_params['user'] = user.email()
		
		html = template.render("web/templates/createGroup.html", template_params)
		self.response.write(html)
#		user = users.get_current_user()
#
#		if user:
#			self.response.headers['Content-Type'] = 'text/plain'
#			self.response.write('Hello, ' + user.nickname())
#		else:
#			self.redirect(users.create_login_url(self.request.uri))

		#self.response.write('Hello world!')

app = webapp2.WSGIApplication([
	('/createGroup', IndexHandler)
], debug=True)
