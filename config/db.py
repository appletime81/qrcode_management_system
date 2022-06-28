from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://apple@192.168.1.199:3306/factory_file_management')
meta = MetaData()
conn = engine.connect()