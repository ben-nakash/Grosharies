#this model represents a Group in our system

from google.appengine.ext import ndb

class GroupLists(ndb.Model):
	ListID = ndb.IntegerProperty()
	GroupID = ndb.IntegerProperty()

	#get all the lists of the group
	@classmethod
	def getAllLists(self, group_id):
		lists =[]
		i=0
		query = GroupLists.query(GroupLists.GroupID==group_id).fetch()
		if query:
			for list in query:
				lists[i] = list.ListID 
				return lists
		else:
			return None
	
	#delete the group from the data store
	@classmethod
	def deleteGroup(self,group_id):
		query =GroupLists.query(GroupLists.GroupID==group_id).fetch()
		for group in query:
			group.key.delete()
		

	@classmethod
	def deleteList(self,list_id):
		query = GroupLists.query(GroupLists.ListID==list_id).fetch()
		for list in query:
			list.key.delete()
	
	@classmethod
	def addGroupList(self,group_id,list_id):
		groupLists = GroupLists()
		groupLists.GroupID = group_id
		groupLists.ListID = list_id
		groupLists.put()
			