from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from Config import config

if config.DBType == 'sqlite':
    # 使用SQLite数据库
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{config.DataBase}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
else:
    # 使用MySQL数据库
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{config.UserName}:{config.Password}@{config.Host}:{config.Port}/{config.DataBase}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_size=5, pool_timeout=30, pool_recycle=1)
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    session = scoped_session(SessionLocal)
Base = declarative_base()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.remove()
