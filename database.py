from sqlalchemy import (
    Column,
    String,
    Integer
)
from ChatBot import (
    SESSION,
    BASE
)

class Data(BASE):
    __tablename__ = "Data"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id
        
Data.__table__.create(checkfirst=True)

def users():
    nah = SESSION.query(Data).all()
    SESSION.close()
    return nah
