from db_connect import db
from datetime import datetime, date
from sqlalchemy import CheckConstraint
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 

author_book = db.Table(
    "author_book",
    db.Column("author_id", db.Integer, db.ForeignKey("author.id"), nullable=False),
    db.Column("book_id", db.Integer, db.ForeignKey("book.id"), nullable=False),
    extend_existing=True
    )

class Author(db.Model):
    __tablename__ = 'author'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    author_name = db.Column(db.String(30), nullable=False)
    
    author_book = db.relationship("Book", secondary=author_book, backref=db.backref("author_b", lazy="select"))
    
    def __init__(self, author_name):
        self.author_name = author_name

class Book(db.Model):
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(30), nullable=False)
    publication_date = db.Column(db.Date)
    page = db.Column(db.SmallInteger)
        # check isbn is 10 or 13 length
    isbn = db.Column(db.String(13), db.CheckConstraint('length(isbn)=10 or length(isbn)=13'), unique=True)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(300))
    copies_owned = db.Column(db.SmallInteger, db.CheckConstraint('copies_owned >= 0'), nullable=False)
    present_owned = db.Column(db.SmallInteger, db.CheckConstraint('present_owned >= 0'), nullable=False)  ###
    image = db.Column(db.String(200))
    
    book_rent = db.relationship("Rent", backref="book_r", lazy="select")
    book_comment = db.relationship("Comment", backref="book_c", lazy="select")
    
    def __init__(self, title, publisher, author, publication_date, page, isbn, description, link, image, book_status_id, copies_owned, present_owned):
        self.title = title
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.page = page
        self.isbn = isbn
        self.description = description
        self.link = link
        self.copies_owned = copies_owned
        self.image = image
        self.book_status_id = book_status_id
        self.copies_owned = copies_owned
        self.present_owned = present_owned


class Member(db.Model, UserMixin):
    __tablename__ = 'member'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow)
        # check email contains @
    member_email = db.Column(db.String(255), db.CheckConstraint('member_email LIKE "%@%"'), nullable=False, unique=True)
    member_password = db.Column(db.String(88), nullable=False)
    rent_count = db.Column(db.SmallInteger, db.CheckConstraint('rent_count <= 5 and rent_count >= 0'), default=0)
    availability = db.Column(db.String(20), default='available')
    
    member_rent = db.relationship("Rent", backref="member_r", lazy="select")
    member_comment = db.relationship("Comment", backref="member_c", lazy="select")
    
    
    def __init__(self, name, member_email, member_password, rent_count, availability):
        self.name = name
        self.member_email = member_email
        self.member_password = member_password
        self.rent_count = rent_count
        self.availability = availability
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
            # password_hash was defined at Users model
        self.password_hash = generate_password_hash(password) # came from werkzeug
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Rent(db.Model):
    __tablename__ = 'rent'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False) 
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False) 
    rent_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    
    def __init__(self, book_id, member_id, rent_date, return_date):
        self.book_id = book_id
        self.member_id = member_id
        self.rent_date = rent_date
        self.return_date = return_date
        
class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, db.CheckConstraint('score >= 0 or score <= 5'), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, book_id, member_id, title, content, score):
        self.book_id = book_id
        self.member_id = member_id
        self.title = title
        self.content = content
        self.score = score
