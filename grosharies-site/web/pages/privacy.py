from google.appengine.ext.webapp import template
from models.group import Group
from models.user import User
from models.list import List
import webapp2

class PrivacyHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		user = None
		if self.request.cookies.get('session'):
			user = User.checkToken(self.request.cookies.get('session'))
			template_params['isUser'] = 'true'
		if not user:
			template_params['isGuest'] = 'true'
			html = template.render("web/templates/privacy.html", template_params)
			self.response.write(html)
			return
			
		template_params['userEmail'] = user.email
		
		groupsNames = Group.getAllGroupsNames(user.email) 		
		if groupsNames:
			template_params['userGroups'] = groupsNames
		
		html = template.render("web/templates/privacy.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/privacy', PrivacyHandler)
], debug=True)
