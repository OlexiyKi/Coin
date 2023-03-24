from sqlalchemy.orm import Session
from sqlalchemy import select
import alch_engine
import model_db

from tbbot import send_warn



def find_trand():
    # with Session(alch_engine.engine) as session:
    #     statement = select(model_db.RateHistory).order_by(model_db.RateHistory.id.desc()).limit(4)
    #     username = session.scalars(statement).all()
    #     print(username)
    con = alch_engine.engine.connect()
    stmt = select(model_db.RateHistory).order_by(model_db.RateHistory.id.desc()).limit(4)
    rez = con.execute(stmt).fetchall()[::-1]
    print (rez[0])
    if rez[3][3] <= rez[2][3] <= rez[1][3] <= rez[0][3]:
        send_warn()

#find_trand()