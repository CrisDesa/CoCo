from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('oracle://conocer:conocer@192.168.1.5:1528/DSBC',
        echo=False)
Base = declarative_base(engine)


class Conocimientos(Base):
    """"""
    __tablename__ = 'conocimiento'
    
    CONOC_ID = Column(Integer, primary_key=True)
    SOFT_ID = Column(String)
    TIPO_ID = Column(String)
    TEMA = Column(String) 
    SOLUCION = Column(String)
    LINK = Column(String)
    COMENTARIOS = Column(String)

    def __init__(self, CONOC_ID, SOFT_ID, TIPO_ID, TEMA, SOLUCION, LINK,
            COMENTARIOS):
        """"""
        self.CONOC_ID = CONOC_ID
        self.SOFT_ID = SOFT_ID
        self.TIPO_ID = TIPO_ID
        self.TEMA = TEMA
        self.SOLUCION = SOLUCION
        self.LINK = LINK
        self.COMENTARIOS = COMENTARIOS

   # def __repr__(self):
   #     """"""
   #     return "<Conocimientos - '%s': '%s' - '%s'>" % (self.TIPO_ID, 
   #             self.SOFT_ID, self.TEMA)


def loadSession():
    """"""""
   #  metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(Conocimientos).all()
    print(res[0].TIPO_ID)
