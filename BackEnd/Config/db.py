from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:valencia13@localhost:3306/test"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_ufH5EzCu7rd_ch2xo92@mysql-8a660dd-valenciacerogpt.e.aivencloud.com:18374/defaultdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()