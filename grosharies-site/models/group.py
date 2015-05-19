#this model represents a Group in our system

from google.appengine.ext import ndb

class Group(ndb.Model):
	GroupName = ndb.StringProperty(required=True)
	GroupAdmin = ndb.StringProperty(required=True)

	@classmethod
	def checkIfGroupNotExists(self,group_name,admin_name):
		q = Group.query(Group.GroupName == group_name, Group.GroupAdmin == admin_name).get()
		if q:
			return False
		else:
			return True
			
	@classmethod
	def getAllUsersFromGroup(self,group_name,admin_name):
		q = Group.query(Group.GroupName == group_name, Group.GroupAdmin == admin_name).get()
		if q:
			return q
		else:
			return None