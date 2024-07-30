from datetime import datetime

import sqlalchemy as sa

from app.models import Base


class DateMixinBase(Base):
    __abstract__ = True

    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)
