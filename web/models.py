from sqlalchemy import Column, DateTime, Integer, MetaData, Table

metadata = MetaData()


t_results = Table(
    'results', metadata,
    Column('actual_result', Integer),
    Column('predicted_result', Integer),
    Column('Timestamp', DateTime)
)
