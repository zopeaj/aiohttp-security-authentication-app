from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config.setting.settingConfiguration import settings

engine = create_engine(settings.POSTGRESQL_DATABASE_URL, echor=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
