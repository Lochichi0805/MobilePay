from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key = True)               # Line 用戶ID
    nick_name = Column(String)                            # Line 用戶Name
    image_url = Column(String(length=256))                # Line 用戶頭貼
    created_time = Column(DateTime, default=func.now())   # Line 用戶建立時間