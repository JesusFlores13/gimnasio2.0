from sqlalchemy import created_engine, MetaData

engine = create_engine("mysql+pymsql://root:@localhost:3307//test.db")
meta = MetaData()

conn = engine.connect()
