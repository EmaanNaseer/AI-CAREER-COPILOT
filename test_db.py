from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://4GTLqHmL8qxFxG8.root:FJJWMWwOptzc8AKO"
    "@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {"ca": r"C:\Users\PMLS\Desktop\AI-CAREER-COPILOT\isrgrootx1.pem"}
    },
)

try:
    with engine.connect() as conn:
        print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:")
    print(e)
