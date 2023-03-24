from sqlalchemy import Column, Integer, String, Float, ForeignKey
from alch_engine import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50))
    password = Column(String(50))
    email = Column(String(50))

    def __int__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'<User {self.username!r}>'

class Coin(Base):
    __tablename__ = 'coins'
    id = Column(Integer, primary_key=True, unique=True)
    coin_name = Column(String(50))

    def __int__(self, coin_name):
        self.coin_name = coin_name

    def __repr__(self):
        return f'<User {self.name!r}>'



class UserSelections(Base):
    __tablename__ = 'user_selections'
    id = Column(Integer, primary_key=True, unique=True)
    id_user = Column(Integer)
    id_coin = Column(Integer)

    def __int__(self, id_user, id_coin):
        self.id_user = id_user
        self.id_coin = id_coin

    def __repr__(self):
        return f'<User {self.name!r}>'



class RateHistory(Base):
    __tablename__ = 'rate history'
    id = Column(Integer, primary_key=True, unique=True)
    coin_name = Column(String(50))
    rate = Column(Float)
    date_rec = Column(String(120))
    time_rec = Column(String(120))

    def __int__(self, coin_name,rate, date_rec, time_rec):
        self.coin_name = coin_name
        self.date_rec = date_rec
        self.time_rec = time_rec
        self.rate = rate

    def __repr__(self):
        return f"<RateHistory {self.rate!r}>"



