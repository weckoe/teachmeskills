from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite+pysqlite:///telegram_bot.db",
    echo=True,
    future=True
)
Session = sessionmaker(engine)
