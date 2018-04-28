from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. orm import sessionmaker


engine = create_engine('oracle://conocer:conocer@192.168.1.5:1528/DSBC',
        echo=True)
Base = declarative_base(engine)


class Aqui_tipo(Base):
    """"""
    __tablename__ = 'tipo'
    __table_args__ = {'autoload':True}


# -----------------------------------

def loadSession():
    """ """
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(Aqui_tipo).all()
    print(res)
 
