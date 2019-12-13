
import sqlalchemy as db
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from collections import defaultdict

#from . import app_config
import pathlib


APP_DB="app.db"
APP_PATH=pathlib.Path(__file__).parent
APP_DB_PATH=APP_PATH.joinpath(APP_DB).resolve()

DB_SQLITE = "sqlite:///{}".format(APP_DB_PATH)

Base = declarative_base()
 
class Pages(Base):
    __tablename__ = 'app-pages'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    page_id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(255), nullable=False)
    page_subname = db.Column(db.String(400), nullable=False)
    page_description = db.Column(db.String(800), nullable=False)
    page_url = db.Column(db.String(255), nullable=False)
    page_type = db.Column(db.String(255), nullable=False)
    page_configured = db.Column(db.Boolean(), default=False)
 
 
# Create an engine that stores data in the local directory's
engine = db.create_engine(DB_SQLITE)
Base.metadata.create_all(engine)


#PAGE_DASH_CONTROLS1 = db.Table('page-dash-controls1', db_METADATA,
#                db.Column('page_id', db.Integer()),
#                db.Column('page_name', db.String(255), nullable=False),
#                db.Column('page_url', db.String(255), nullable=False),
#                db.Column('page_block_header', db.String(50), nullable=False),
#                db.Column('page_block_configured', db.Boolean(), default=False),
#                db.Column('page_block_enabled', db.Boolean(), default=True),
#                db.Column('page_block_number', db.Integer(), nullable=False),
#                db.Column('page_block_widget', db.String(255), nullable=False), #CHART TABLE ETC
#                db.Column('page_block_blox_function', db.String(255), nullable=False),
#)


#########################################################################################################################
def create_session():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def close_session(session):
    session.close()
    return

def query_to_dict(rset):
    result = defaultdict(list)
    for obj in rset:
        instance = inspect(obj)
        for key, x in instance.attrs.items():
            result[key].append(x.value)
    return result



def create_page(page_id, page_name, page_subname, page_description, page_url, page_type, page_configured):
    create_sessionX = create_session()
    new_page = Pages(page_name=page_name, page_subname=page_subname, page_description=page_description, page_url=page_url, page_type=page_type,page_configured=page_configured) 
    create_sessionX.add(new_page)
    create_sessionX.commit()
    close_session(create_sessionX)
    return

def configure_page(page_id, page_name, page_description, page_url, page_block_header, page_block_configured, page_block_enabled, page_block_number, page_block_widget, page_block_blox_function):
    return

def page_details():
    details_session = create_session()
    page_all = details_session.query(Pages).all()
    page_all_df = pd.DataFrame(query_to_dict(page_all))
    close_session(details_session)
    #pages_all_df = pd.read_sql(session.query(Pages).all().statement,session.bind) 
    return page_all_df

def page_configuration_details(page_id):
    details_session = create_session()
    page_by_id = details_session.query(Pages).get(page_id[0])
    page_detail_dict = {
                        'page_id': page_id,
                        'page_name': page_by_id.page_name,
                        'page_subname': page_by_id.page_subname,
                        'page_description': page_by_id.page_description,
                        'page_url': page_by_id.page_url,
                        'page_type': page_by_id.page_type
                        }

    close_session(details_session)
    return page_detail_dict

def page_list():
    return

def update_current_page():
    return

def get_current_page():
    return