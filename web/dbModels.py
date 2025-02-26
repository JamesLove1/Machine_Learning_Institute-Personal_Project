from typing import Optional

from sqlalchemy import DateTime, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class Results(Base):
    __tablename__ = 'results'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='results_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    actual_result: Mapped[Optional[int]] = mapped_column(Integer)
    predicted_result: Mapped[Optional[int]] = mapped_column(Integer)
    Timestamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
