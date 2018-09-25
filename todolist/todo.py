''' TodoItem Class that can be added and search '''

import datetime

last_id = 0

class TodoItem:

	def __init__ (self, content, tags=''):
		self.content = content
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def search(self, filter):
		return filter in self.content or filter in self.tags


class TodoList:

	def __init__ (self):
		self.items = []

	def new_todo(self, content, tags=''):
		self.items.append(TodoItem(content, tags))

	def _find_todo(self, todo_id):
		for item in self.items:
			if(todo_id == item.id):
				return item
		return None

	def modify_content(self, todo_id, content):
		item = _find_todo(todo_id)
		if item:
			item.content = content
			return True
		return False

	def modify_tag(self, todo_id, tags):
		item = _find_todo(todo_id)
		if item:
			item.tags = tags
			return True
		return False

	def search(self, filter):
		return [ item for item in self.items if item.search(filter) ]