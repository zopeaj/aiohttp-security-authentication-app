from sqlalchemy.orm import Session

from app.
from app.core.config.setting.settingConfiguration import settings
from app.db.base import Base

userService = UserService()

def init_db(db: Session) -> None:
    user = userService.
