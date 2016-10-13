from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection(object):
	def __init__(self, app, db):
		config = {
				'host': 'localhost',
				'database': db,
				'user': 'root',
				'password': '',
				'port': '3306'
		}

		DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'], config['database'])
		app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
		app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
		self.db = SQLAlchemy(app)
	def query_db(self, query, data=None):
		result = self.db.session.execute(text(query), data)
		if query[0:6].lower() == 'select':
			list_result = [dict(r) for r in result]
			return list_result
		elif query[0:6].lower() == 'insert':
			self.db.session.commit()
			return result.lastrowid
		else:
			self.db.session.commit()
def MySQLConnector(app, db):
    return MySQLConnection(app, db)