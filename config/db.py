# 1. 導入 sqlalchemy 部分的包
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2. 宣告 database url
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://apple@192.168.1.199:3306/factory_file_management"


# 3. 創建 sqlalchemy 引擎
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
)

# 4. 創建一個 database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. return an  ORM Model
Base = declarative_base()

