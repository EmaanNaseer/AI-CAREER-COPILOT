from db import engine, Base
from models import User, Report

print("Starting...")

print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

print("Finished!")
