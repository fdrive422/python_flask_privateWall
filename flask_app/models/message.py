from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user

class Message:
    dbName = 'private_wall_schema'
    def __init__(self, data):
        self.id=data['id']
        self.message=data['message']
        self.sender_id=data['sender_id']
        self.sender_name=data['sender_name']
        self.recipient_id=data['recipient_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def create(cls, data):
        query="INSERT INTO messages (message, sender_id, recipient_id, created_at, updated_at)"\
            "VALUES (%(message)s, %(sender_id)s, %(recipient_id)s, NOW(), NOW())"
        result=connectToMySQL(cls.dbName).query_db(query, data)
        print(result)
        return result

    @classmethod
    def delete(cls, data):
        query="DELETE FROM messages WHERE id=%(id)s;"
        result=connectToMySQL(cls.dbName).query_db(query, data)
        return result

    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['message'])<5:
            flash('*message must be more than five charaters', 'message_errors')
            is_valid=False
        return is_valid