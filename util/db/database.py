from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.sql.schema import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.exc import *
from util.db.database_setting import DATABASE_SETTING
import os.path


Base = declarative_base()
dbpath = os.path.join(DATABASE_SETTING['path'], DATABASE_SETTING['dbname'])
conn_str = 'sqlite:///' + dbpath
engine = create_engine(conn_str)
DbSession = sessionmaker(bind=engine)
session = DbSession()
conn = Connection(engine)

def create_all_table():
    Base.metadata.create_all(engine)

def addRecord(tableObject):
    session.add(tableObject)
    result = ''
    try:
        session.commit()
        result = 'Success'
    except NoForeignKeysError as e:
        session.rollback()
        result = 'Fail'
    except DBAPIError as e:
        session.rollback()
        result = 'Fail'
    finally:
        return result



def deleteRecord(tableObject):
    session.delete(tableObject)
    session.commit()

def rollback():
    session.rollback()

def get_all(tableclass):
    return session.query(tableclass)

def get(tableclass,id):
    return session.query(tableclass).filter_by(id=id)[0]

def altertable(tablename,columnname,columntype,length,nullable=False,defaultvalue=False):
    altersql = 'alter table %s add %s %s(%s)' %(tablename,columnname,columntype,length)
    if nullable:
        altersql = altersql + ' null'
    print('alter sql is %s' % altersql)
    conn.execute(altersql)
    conn.close()




