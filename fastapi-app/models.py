from sqlalchemy import Column, Integer, String, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blogs.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    
    def __repr__(self):
        return f'{self.id} | {self.title} | {self.description} | {self.published}'
    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    