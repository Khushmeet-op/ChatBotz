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
    message = Column(Integer)
    ha_id = Column(Integer)

    def __init__(self, chat_id, message, ha_id):
        self.chat_id = chat_id
        self.message = message
        self.ha_id = ha_id
        
Data.__table__.create(checkfirst=True)

def users():
    nah = SESSION.query(Data).all()
    SESSION.close()
    return nah

def hmm_id(message_id: int):
    try:
        pro_id = SESSION.query(Data).get(str(message))
        return int(pro_id.chat_id), pro_id.ha_id
    finally:
        SESSION.close()
