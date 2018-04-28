# all imports

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# definicion del motor de la base y la metadata

oracle_db = create_engine('oracle://conocer:conocer@192.168.1.5:1528/DSBC')
conexion = oracle_db.connect()
resultado = conexion.execute("select sysdate from dual")


app = Flask(__name__)  # crea la aplicacion


@app.route('/')
def index():
    titulo = 'CoCo - Base de Conocimiento'
    return render_template('index.html', titulo=titulo)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
