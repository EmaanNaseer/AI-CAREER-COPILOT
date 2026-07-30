from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    "mysql+pymysql://4GTLqHmL8qxFxG8.root:FJJWMWwOptzc8AKO"
    "@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {"ca": r"C:\Users\PMLS\Desktop\AI-CAREER-COPILOT\isrgrootx1.pem"}
    },
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
