from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy. orm import mapper, sessionmaker


class Tipo(object):
    pass


# -----------------------------------

def loadSession():
    """ """
    engine = create_engine('oracle://conocer:conocer@192.168.1.5:1528/DSBC',
            echo=True)

    metadata = MetaData(engine)
    tipo = Table('tipo', metadata, autoload=True)
    mapper(Tipo, tipo)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(Tipo).all()
    res[1].tipo_id
 
