from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    techcrunch_id = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    date_published = Column(Date)
    title = Column(String)
    url = Column(String)
    text = Column(String)

    author = relationship("Author", back_populates="articles")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    url = Column(String)

    articles = relationship("Article", back_populates="author")
