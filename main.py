from app import *
from datetime import datetime, date
import pymysql
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

# This file is to connect table book and table author together with author_book
# N:M

with app.app_context():
    b1 = Book.query.filter(Book.id==1).first()
    a1 = Author.query.filter(Author.id==1).first()
    b1.author_b.append(a1)
    
    
    b2 = Book.query.filter(Book.id==2).first()
    b3 = Book.query.filter(Book.id==3).first()
    b4 = Book.query.filter(Book.id==4).first()
    b5 = Book.query.filter(Book.id==5).first()
    b6 = Book.query.filter(Book.id==6).first()
    b7 = Book.query.filter(Book.id==7).first()
    b8 = Book.query.filter(Book.id==8).first()
    b9 = Book.query.filter(Book.id==9).first()
    b10 = Book.query.filter(Book.id==10).first()
    b11 = Book.query.filter(Book.id==11).first()
    b12 = Book.query.filter(Book.id==12).first()
    b13 = Book.query.filter(Book.id==13).first()
    b14 = Book.query.filter(Book.id==14).first()
    b15 = Book.query.filter(Book.id==15).first()
    b16 = Book.query.filter(Book.id==16).first()
    b17 = Book.query.filter(Book.id==17).first()
    b18 = Book.query.filter(Book.id==18).first()
    b19 = Book.query.filter(Book.id==19).first()
    b20 = Book.query.filter(Book.id==20).first()
    b21 = Book.query.filter(Book.id==21).first()
    b22 = Book.query.filter(Book.id==22).first()
    b23 = Book.query.filter(Book.id==23).first()
    b24 = Book.query.filter(Book.id==24).first()
    b25 = Book.query.filter(Book.id==25).first()
    b26 = Book.query.filter(Book.id==26).first()
    b27 = Book.query.filter(Book.id==27).first()
    b28 = Book.query.filter(Book.id==28).first()
    b29 = Book.query.filter(Book.id==29).first()
    b30 = Book.query.filter(Book.id==30).first()
    b31 = Book.query.filter(Book.id==31).first()
    b32 = Book.query.filter(Book.id==32).first()
    
    a2 = Author.query.filter(Author.id==2).first()
    a3 = Author.query.filter(Author.id==3).first()
    a4 = Author.query.filter(Author.id==4).first()
    a5 = Author.query.filter(Author.id==5).first()
    a6 = Author.query.filter(Author.id==6).first()
    a7 = Author.query.filter(Author.id==7).first()
    a8 = Author.query.filter(Author.id==8).first()
    a9 = Author.query.filter(Author.id==9).first()
    a10 = Author.query.filter(Author.id==10).first()
    a11 = Author.query.filter(Author.id==11).first()
    a12 = Author.query.filter(Author.id==12).first()
    a13 = Author.query.filter(Author.id==13).first()
    a14 = Author.query.filter(Author.id==14).first()
    a15 = Author.query.filter(Author.id==15).first()
    a16 = Author.query.filter(Author.id==16).first()
    a17 = Author.query.filter(Author.id==17).first()
    a18 = Author.query.filter(Author.id==18).first()
    a19 = Author.query.filter(Author.id==19).first()
    a20 = Author.query.filter(Author.id==20).first()
    a21 = Author.query.filter(Author.id==21).first()
    a22 = Author.query.filter(Author.id==22).first()
    a23 = Author.query.filter(Author.id==23).first()
    a24 = Author.query.filter(Author.id==24).first()
    a25 = Author.query.filter(Author.id==25).first()
    a26 = Author.query.filter(Author.id==26).first()
    a27 = Author.query.filter(Author.id==27).first()
    a28 = Author.query.filter(Author.id==28).first()
    a29 = Author.query.filter(Author.id==29).first()
    a30 = Author.query.filter(Author.id==30).first()
    a31 = Author.query.filter(Author.id==31).first()
    a32 = Author.query.filter(Author.id==32).first()
    a33 = Author.query.filter(Author.id==33).first()
    a34 = Author.query.filter(Author.id==34).first()
    a35 = Author.query.filter(Author.id==35).first()
    a36 = Author.query.filter(Author.id==36).first()
    a37 = Author.query.filter(Author.id==37).first()
    a38 = Author.query.filter(Author.id==38).first()
    a39 = Author.query.filter(Author.id==39).first()
    
    
    b1.author_b.append(a2)
    b2.author_b.append(a3)
    b3.author_b.append(a4)
    b4.author_b.append(a5)
    b5.author_b.append(a6)
    b6.author_b.append(a7)
    b7.author_b.append(a8)
    b8.author_b.append(a9)
    b9.author_b.append(a10)
    b10.author_b.append(a11)
    b11.author_b.append(a12)
    b11.author_b.append(a13)
    b12.author_b.append(a14)
    b13.author_b.append(a15)
    b14.author_b.append(a16)
    b15.author_b.append(a17)
    b15.author_b.append(a18)
    b15.author_b.append(a19)
    b16.author_b.append(a20)
    b16.author_b.append(a21)
    b16.author_b.append(a22)
    b17.author_b.append(a23)
    b18.author_b.append(a24)
    b19.author_b.append(a25)
    b20.author_b.append(a26)
    b21.author_b.append(a27)
    b21.author_b.append(a28)
    b22.author_b.append(a29)
    b23.author_b.append(a30)
    b24.author_b.append(a31)
    b25.author_b.append(a32)
    b26.author_b.append(a33)
    b27.author_b.append(a34)
    b28.author_b.append(a35)
    b29.author_b.append(a36)
    b30.author_b.append(a37)
    b31.author_b.append(a38)
    b32.author_b.append(a39)
    db.session.commit()
    
    # b1 = Book.query.filter(Book.id==1).first()
    # a1 = Author.query.filter(Author.id==1).first()
    # b1.author_b.append(a1)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # bs1 = Book_status(1, 1)
    # bs2 = Book_status(2, 2)
    # bs3 = Book_status(1, 1)
    # bs4 = Book_status(1, 1)
    # bs5 = Book_status(2, 2)
    # bs6 = Book_status(1, 1)
    # bs7 = Book_status(2, 2)
    # bs8 = Book_status(1, 1)
    # bs9 = Book_status(1, 1)
    # bs10 = Book_status(2, 2)
    # bs11 = Book_status(1, 1)
    # bs12 = Book_status(1, 1)
    # bs13 = Book_status(2, 2)
    # bs14 = Book_status(1, 1)
    # bs15 = Book_status(1, 1)
    # bs16 = Book_status(2, 2)
    # bs17 = Book_status(1, 1)
    # bs18 = Book_status(2, 2)
    # bs19 = Book_status(1, 1)
    # bs20 = Book_status(1, 1)
    # bs21 = Book_status(2, 2)
    # bs22 = Book_status(1, 1)
    # bs23 = Book_status(1, 1)
    # bs24 = Book_status(2, 2)
    # bs25 = Book_status(1, 1)
    # bs26 = Book_status(2, 2)
    # bs27 = Book_status(1, 1)
    # bs28 = Book_status(1, 1)
    # bs29 = Book_status(1, 1)
    # bs30 = Book_status(1, 1)
    # bs31 = Book_status(2, 2)
    # bs32 = Book_status(1, 1)
    
    # db.session.add(bs1)
    # db.session.add(bs2)
    # db.session.add(bs3)
    # db.session.add(bs4)
    # db.session.add(bs5)
    # db.session.add(bs6)
    # db.session.add(bs7)
    # db.session.add(bs8)
    # db.session.add(bs9)
    # db.session.add(bs10)
    # db.session.add(bs11)
    # db.session.add(bs12)
    # db.session.add(bs13)
    # db.session.add(bs14)
    # db.session.add(bs15)
    # db.session.add(bs16)
    # db.session.add(bs17)
    # db.session.add(bs18)
    # db.session.add(bs19)
    # db.session.add(bs20)
    # db.session.add(bs21)
    # db.session.add(bs22)
    # db.session.add(bs23)
    # db.session.add(bs24)
    # db.session.add(bs25)
    # db.session.add(bs26)
    # db.session.add(bs27)
    # db.session.add(bs28)
    # db.session.add(bs29)
    # db.session.add(bs30)
    # db.session.add(bs31)
    # db.session.add(bs32)
    
    # bs1 = Book_status.query.filter(Book_status.id==1).first()
    # bs2 = Book_status.query.filter(Book_status.id==2).first()
    # bs3 = Book_status.query.filter(Book_status.id==3).first()
    # bs4 = Book_status.query.filter(Book_status.id==4).first()
    # bs5 = Book_status.query.filter(Book_status.id==5).first()
    # bs6 = Book_status.query.filter(Book_status.id==6).first()
    # bs7 = Book_status.query.filter(Book_status.id==7).first()
    # bs8 = Book_status.query.filter(Book_status.id==8).first()
    # bs9 = Book_status.query.filter(Book_status.id==9).first()
    # bs10 = Book_status.query.filter(Book_status.id==10).first()
    # bs11 = Book_status.query.filter(Book_status.id==11).first()
    # bs12 = Book_status.query.filter(Book_status.id==12).first()
    # bs13 = Book_status.query.filter(Book_status.id==13).first()
    # bs14 = Book_status.query.filter(Book_status.id==14).first()
    # bs15 = Book_status.query.filter(Book_status.id==15).first()
    # bs16 = Book_status.query.filter(Book_status.id==16).first()
    # bs17 = Book_status.query.filter(Book_status.id==17).first()
    # bs18 = Book_status.query.filter(Book_status.id==18).first()
    # bs19 = Book_status.query.filter(Book_status.id==19).first()
    # bs20 = Book_status.query.filter(Book_status.id==20).first()
    # bs21 = Book_status.query.filter(Book_status.id==21).first()
    # bs22 = Book_status.query.filter(Book_status.id==22).first()
    # bs23 = Book_status.query.filter(Book_status.id==23).first()
    # bs24 = Book_status.query.filter(Book_status.id==24).first()
    # bs25 = Book_status.query.filter(Book_status.id==25).first()
    # bs26 = Book_status.query.filter(Book_status.id==26).first()
    # bs27 = Book_status.query.filter(Book_status.id==27).first()
    # bs28 = Book_status.query.filter(Book_status.id==28).first()
    # bs29 = Book_status.query.filter(Book_status.id==29).first()
    # bs30 = Book_status.query.filter(Book_status.id==30).first()
    # bs31 = Book_status.query.filter(Book_status.id==31).first()
    # bs32 = Book_status.query.filter(Book_status.id==32).first()
    
    # b1.book_status_b.append(bs1)
    # b2.book_status_b.append(bs2)
    # b3.book_status_b.append(bs3)
    # b4.book_status_b.append(bs4)
    # b5.book_status_b.append(bs5)
    # b6.book_status_b.append(bs6)
    # b7.book_status_b.append(bs7)
    # b8.book_status_b.append(bs8)
    # b9.book_status_b.append(bs9)
    # b10.book_status_b.append(bs10)
    # b11.book_status_b.append(bs11)
    # b12.book_status_b.append(bs12)
    # b13.book_status_b.append(bs13)
    # b14.book_status_b.append(bs14)
    # b15.book_status_b.append(bs15)
    # b16.book_status_b.append(bs16)
    # b17.book_status_b.append(bs17)
    # b18.book_status_b.append(bs18)
    # b19.book_status_b.append(bs19)
    # b20.book_status_b.append(bs20)
    # b21.book_status_b.append(bs21)
    # b22.book_status_b.append(bs22)
    # b23.book_status_b.append(bs23)
    # b24.book_status_b.append(bs24)
    # b25.book_status_b.append(bs25)
    # b26.book_status_b.append(bs26)
    # b27.book_status_b.append(bs27)
    # b28.book_status_b.append(bs28)
    # b29.book_status_b.append(bs29)
    # b30.book_status_b.append(bs30)
    # b31.book_status_b.append(bs31)
    # b32.book_status_b.append(bs32)
    
    # setattr(b1, 'book_status_id', bs1.id)
    # setattr(b2, 'book_status_id', bs2.id)
    # setattr(b3, 'book_status_id', bs3.id)
    # setattr(b4, 'book_status_id', bs4.id)
    # setattr(b5, 'book_status_id', bs5.id)
    # setattr(b6, 'book_status_id', bs6.id)
    # setattr(b7, 'book_status_id', bs7.id)
    # setattr(b8, 'book_status_id', bs8.id)
    # setattr(b9, 'book_status_id', bs9.id)
    # setattr(b10, 'book_status_id', bs10.id)
    # setattr(b11, 'book_status_id', bs11.id)
    # setattr(b12, 'book_status_id', bs12.id)
    # setattr(b13, 'book_status_id', bs13.id)
    # setattr(b14, 'book_status_id', bs14.id)
    # setattr(b15, 'book_status_id', bs15.id)
    # setattr(b16, 'book_status_id', bs16.id)
    # setattr(b17, 'book_status_id', bs17.id)
    # setattr(b18, 'book_status_id', bs18.id)
    # setattr(b19, 'book_status_id', bs19.id)
    # setattr(b20, 'book_status_id', bs20.id)
    # setattr(b21, 'book_status_id', bs21.id)
    # setattr(b22, 'book_status_id', bs22.id)
    # setattr(b23, 'book_status_id', bs23.id)
    # setattr(b24, 'book_status_id', bs24.id)
    # setattr(b25, 'book_status_id', bs25.id)
    # setattr(b26, 'book_status_id', bs26.id)
    # setattr(b27, 'book_status_id', bs27.id)
    # setattr(b28, 'book_status_id', bs28.id)
    # setattr(b29, 'book_status_id', bs29.id)
    # setattr(b30, 'book_status_id', bs30.id)
    # setattr(b31, 'book_status_id', bs31.id)
    # setattr(b32, 'book_status_id', bs32.id)
    # db.session.commit()

    

    

    
    # con = pymysql.connect(host='localhost', user='root', password='060600', db='elice_library', charset='utf8')
    # cur = con.cursor()
    
    # sql = "select b.title, a.author_name from book b join author_book ab on b.id = ab.book_id join author a on ab.author_id = a.id"
    
    # cur.execute(sql)
    
    # result = cur.fetchall()
    
    # for x in result:
    #     print(x)
    
    ###################
    
    # engine = create_engine('mysql+pymysql://root:060600@localhost/library', echo = True)
    # Session = sessionmaker(bind = engine)
    # session = Session()
    
    # for x in session.query(Book, Author).filter(author_book.book_id == Book.id, author_book.author_id == Author.id).order_by(author_book.book_id).all():
    #     print(x)
    
        # 특정한 book id의 저자만 표출하기
        # select a.author_name from author a join author_book ab on a.id = ab.author_id join book b on ab.book_id = b.id where b.id = 1;