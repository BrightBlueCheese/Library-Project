from flask import Flask, redirect, request, render_template, jsonify, session, flash, url_for
from db_connect import db, cur, conn
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, date
from models import author_book, Author, Book, Member, Comment, Rent
    # User Authenticate
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin, login_user, LoginManager, logout_user, current_user, login_required 
    # Advanced Text Manager
from flask_ckeditor import CKEditor 

from forms import BookCommentForm, SignupForm, SigninForm, SearchForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:060600@127.0.0.1:3306/elice_library"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:060600@localhost/elice_library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'JHVB8723jbhDSFUHi7hknsmbchjsa73Q87)LK;DF0-(PORKJ1' 

db.init_app(app)

migrage = Migrate(app, db)
ckeditor = CKEditor(app)

    # Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app) # need to pass in the var app into the manager
login_manager.login_view = 'login'

@login_manager.user_loader # load the user when we loghed in
def load_member(member_id):
    return Member.query.get(int(member_id)) # get the id from the Model

@app.context_processor
def datetimer():
    today = datetime.utcnow()
    return dict(today=today)


@app.route('/')
def main():
    page = request.args.get('page', 1, type=int)
    sql = """select b.id, avg(c.score) from book as b left join comment as c on b.id = c.book_id group by b.id order by b.id"""
    cur.execute(sql)
    scores = cur.fetchall()
    author = Author.query.filter(Author.author_book.any(id=Book.id)).all()
        # group_concat!!
    sql = """select b.id, group_concat(a.author_name separator ' ') as b_authors from author a 
            join author_book ab on a.id = ab.author_id
            join book b on ab.book_id = b.id group by b.id order by b.id;"""
    cur.execute(sql)
    b_author = cur.fetchall()
    conn.commit()
    try:
        # scores = Book.query.join(Comment, Comment.book_id == Book.id, isouter=True)
        book_list = Book.query.order_by(Book.id.desc()).paginate(page=page, per_page=8)
        
    except:
        flash("No Book Information In The Database.")
        book_list = None
        scores = None
        b_author = None
    return render_template('main.html', 
                           book_list=book_list,
                           scores=scores,
                           page=page,
                           b_author=b_author)

@app.route('/book/<int:id>')
def book_info(id):
    book = Book.query.get_or_404(id)
    try:
        sql = f"""select b.id, avg(c.score) from book as b left join comment as c on b.id = c.book_id where b.id = {id}"""
        cur.execute(sql)
        score = cur.fetchone()
        
        sql = f"""select group_concat(a.author_name separator ' ') as b_authors from author a 
            join author_book ab on a.id = ab.author_id
            join book b on ab.book_id = b.id where b.id = {id} group by b.id order by b.id ;"""
        cur.execute(sql)
        the_b_author = cur.fetchone()
        the_b_author = the_b_author[0]
    except:
        flash("Something Is Wrong.")
        book = None,
        score = None
        the_b_author = None
    
    return render_template('book_info.html',
                           book=book,
                           score=score,
                           the_b_author=the_b_author)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = None
    form = SignupForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(member_email=form.member_email.data).first()
        if member is None:
            password_hash = generate_password_hash(form.password_hash.data, "sha256")
            member = Member(member_email=form.member_email.data,
                            name=form.name.data,
                            member_password=password_hash,
                            rent_count=0,
                            availability='available')
            db.session.add(member)
            db.session.commit()
        
        name = form.name.data
        form.member_email.data = ''
        form.name.data = ''
        form.password_hash.data = ''
        
        flash("Successfully Signed Up!")
    
    member_list = Member.query.order_by(Member.id)
    return render_template("signup.html",
                           form=form,
                           name=name,
                           member_list=member_list)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(member_email=form.member_email.data).first()
        if member:
            if check_password_hash(member.member_password, form.password.data):
                login_user(member)
                flash("Successfully Signed In.")
                return redirect(url_for('dashboard')) 
            else:
                flash("Invalid Password. Please Try Again...")
        else:
            flash("There Is No Such User Data.")
    return render_template('signin.html', form=form)
    
@app.route('/signout', methods=["GET", "POST"])
@login_required # from flask_login
def signout():
    logout_user()
    flash("Successfully Signed Out")
    return redirect(url_for('signin'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = SignupForm()
    id = current_user.id
    member_update = Member.query.get_or_404(id)
    rent = Rent.query.filter((Rent.member_id == id) & (Rent.return_date == datetime.min))
    if request.method == "POST":
        member_update.name = request.form['name']
        try:
            db.session.commit()
            flash("New Information Has Been Updated")
            return render_template('dashboard.html',
                                   form=form,
                                   member_update=member_update,
                                   rent=rent)
        except:
            flash("Something Is Wrong While Signing Up, Try Again...")
            return render_template('dashboard.html',
                                   form=form,
                                   member_update=member_update,
                                   rent=rent)
    elif request.method == "GET":
        return render_template('dashboard.html',
                               form=form,
                               member_update=member_update,
                               rent=rent,
                               id=id)

@app.route('/update/<int:id>', methods=["GET", "POST"])
@login_required
def update(id):
    form = SignupForm()
    current_id = current_user.id
    rent = Rent.query.filter((Rent.member_id == id) & (Rent.return_date == None))
    member_update = Member.query.get_or_404(id)  
    if id == current_id:
        if request.method == "POST":
            try:
                member_update.name = request.form['name']
                db.session.commit()
                flash("New Information Has Been Updated")
                return render_template('dashboard.html',
                                        form=form,
                                        member_update=member_update,
                                        rent=rent)
            except:
                flash("Something Is Wrong While Signing Up, Try Again...")
                return render_template('update.html',
                                    form=form,
                                    member_update=member_update)
        elif request.method == "GET":
            return render_template('update.html',
                                form=form,
                                member_update=member_update,
                                id=id)
    else:
        flash('Invalid Approach')
        return render_template('404.html')
    
@app.route('/delete/<int:id>')
def delete(id):
    member_delete = Member.query.get_or_404(id)
    current_id = current_user.id
    name = None
    rent = Rent.query.filter(Rent.member_id == current_id)
    form = SignupForm()
    if member_delete.rent_count == 0:
        try:
            cur.execute('set foreign_key_checks = 0;')
            cur.execute('delete from member where id = 1')
            cur.execute('set foreign_key_checks = 1;')
            conn.commit()
            logout_user()
            flash("Resigned Successfully.")
            return redirect(url_for("signup",
                                    form=form,
                                    name=name))
        except:
            flash("Somethig Is Wrong While Deleting The Member, Try Again...")
            return render_template("signup.html",
                                form=form,
                                name=name)
    else:
        flash("You Have To Return All The Books You Borrowed Before Resign.")
        return render_template('dashboard.html',
                                        form=form,
                                        member_update=member_delete,
                                        rent=rent)


@app.route('/comment/add/<int:id>', methods=["GET", "POST"])
@login_required
def add_comment(id):
    form = BookCommentForm()
    book = Book.query.get_or_404(id)

    if form.validate_on_submit():
        commenter = current_user.id
        comment = Comment(book_id=book.id,
                          member_id=commenter,
                          title=form.title.data,
                          content=form.content.data,
                          score=form.score.data)

        form.title.data = ''
        form.content.data = ''
        form.score.data = ''
        db.session.add(comment)
        db.session.commit()
        
        # flash("Book Review Submitted Successfully.")
        # sql = f"""select b.id, avg(c.score) from book as b left join comment as c on b.id = c.book_id where b.id = {id}"""
        # cur.execute(sql)
        # score = cur.fetchone()
        page = request.args.get('page', 1, type=int)
        comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
        return render_template('comments.html',
                           comments=comments,
                           page=page)
        
    return render_template('add_comment.html',
                            form=form)

@app.route('/comments')
def comments():
    page = request.args.get('page', 1, type=int)
    
    try:
        comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
        
    except:
        flash("No Comment Information In The Database.")
        comments = None
        
    return render_template('comments.html',
                           comments=comments,
                           page=page)
    
@app.route('/comments/<int:id>')
def comment(id):
    comment = Comment.query.get_or_404(id)
    return render_template('comment.html', comment=comment)

@app.route('/comments/delete/<int:id>')
@login_required
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    id = current_user.id
    page = request.args.get('page', 1, type=int)
    if id == comment.member_c.id:
        try:
            db.session.delete(comment)
            db.session.commit()
            comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
            flash("Your Review Was Deleted.")
            return render_template('comments.html', comments=comments)
        except:
            flash("There Was A Trouble While Deleting Your Review, Try Again...")
            comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
            return render_template('comments.html', comments=comments)
    else:
        flash("Unauthorized Approach.")
        comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
        return render_template('comments.html', comments=comments)

@app.route('/comment/edit/<int:id>', methods=["GET", "POST"])
@login_required
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    form = BookCommentForm()
    if form.validate_on_submit():
        comment.title = form.title.data
        comment.score = form.score.data
        comment.content = form.content.data
        
        db.session.add(comment)
        db.session.commit()
        flash("Your Review Has Been Updated.")
        return redirect(url_for('comment', id=comment.id))
        
    if current_user.id == comment.member_id:
        # the data we already typed in at the last time would be on the field
        form.title.data = comment.title
        form.score.data = comment.score
        form.content.data = comment.content
        return render_template('edit_comment.html', form=form)
        
    else :
        flash("Unauthorized Approach.")
        comments = Comment.query.order_by(Comment.id.desc()).paginate(page=page, per_page=15)
        return render_template('comments.html', comments=comments)


#book_info에서..
@app.route('/rent', methods=["POST"])
@login_required
def rent():
    if request.method == "POST":
        the_book_id = request.form.get('rent')
        
        member_id = current_user.id
        book_to_rent = Book.query.get_or_404(the_book_id)
        member_status = Member.query.filter(Member.id == member_id).first()
        sql = f"""select b.id, avg(c.score) from book as b left join comment as c on b.id = c.book_id where b.id = {the_book_id}"""
        cur.execute(sql)
        score = cur.fetchone()
        
        sql = f"""select r.id from book as b join rent as r on r.book_id = b.id join member as m on r.member_id = m.id where r.member_id = {member_id} and r.book_id = {book_to_rent.id} order by r.id desc limit 1"""
        cur.execute(sql)
        target_book = cur.fetchone()
        
        if target_book:
            target_book_id = target_book[0]
            target_rent = Rent.query.get_or_404(target_book_id)
        else: 
            target_rent = None

        if book_to_rent.present_owned >= 1 and member_status.rent_count <= 4 and member_status.availability == "available" and (target_rent == None or target_rent.return_date):
            try:
                book_to_rent.present_owned -= 1
                member_status.rent_count += 1
                rent = Rent(book_id=book_to_rent.id,
                            member_id=member_id,
                            rent_date=datetime.utcnow(),
                            return_date=datetime.min)
                db.session.add(rent)
                db.session.commit()
                flash("The Book Checked Out Successfully.")
                if member_status.present_owned >= 5 and member_status == "available":
                    flash("You Have Reached Your Limit of 5 Books.")
                    member_status == 'unavailable'
                    db.session.commit()
                    return render_template("book_info.html", 
                            book=book_to_rent,
                            score=score)
            except:
                return render_template("book_info.html", 
                            book=book_to_rent,
                            score=score)
                
        elif book_to_rent.present_owned == 0:
            flash("There Is No Book In Stock.")
            return render_template("book_info.html", 
                            book=book_to_rent,
                            score=score)
            
        
        # elif target_rent.return_date == datetime.min:
        #     flash("You have Already Checked Out The Same Book.")
        #     return render_template("book_info.html", 
        #                     book=book_to_rent,
        #                     score=score)
            
        elif member_status.rent_count >= 5:
            flash("Sorry, You Have Already Reached Your Limit : 5 Books")
            return render_template("book_info.html", 
                            book=book_to_rent,
                            score=score)
            
        elif member_status.availability == 'blocked':
            flash("You Have Passed The Return Date. Please Contact To Our Manager.")
            return render_template("book_info.html", 
                            book=book_to_rent,
                            score=score)
        
        else :
            flash("Somethin is Wrong. Try Again")
            return render_template("book_info.html", 
                                book=book_to_rent,
                                score=score)
            
@app.route('/return', methods=["POST"])
@login_required
def return_back():
    # book_to_return = Book.query.get_or_404(id)
    if request.method == "POST":
        the_book_id = request.form.get('return')
        book_to_return = Book.query.get_or_404(the_book_id)
        member_id = current_user.id
        member_status = Member.query.filter(Member.id == member_id).first()
        # rent_status = None
        
        sql = f"""select b.id, avg(c.score) from book as b left join comment as c on b.id = c.book_id where b.id = {the_book_id}"""
        cur.execute(sql)
        score = cur.fetchone() 
        zeroe = datetime.min
        sql2 = f"""select r.id from book as b join rent as r on r.book_id = b.id join member as m on r.member_id = m.id where r.member_id = {member_id} and r.book_id = {book_to_return.id} and r.return_date = '{zeroe}' limit 1"""
        
        cur.execute(sql2)
        target_book = cur.fetchone()
        conn.commit()
        if target_book:
            target_rent_id = target_book[0]
            target_rent = Rent.query.filter(Rent.id == target_rent_id).order_by(Rent.id.desc()).first()
        else :
            flash("Your Request Is Pending. Try It Later...")
            rent = Rent.query.filter((Rent.member_id == id) & (Rent.return_date == datetime.min))
            return render_template('book_info.html',
                                        book=book_to_return,
                                        score=score)
        
        if target_rent.return_date == datetime.min or target_rent != None:
            try:
                target_rent.return_date = datetime.utcnow()
                
                if target_rent.return_date != datetime.min:
                    book_to_return.present_owned += 1
                    member_status.rent_count -= 1
                    
                    return_term = (datetime.utcnow() - target_rent.rent_date).days
                    db.session.commit()
                    if return_term > 7:
                        member_status.availability = 'unavailable'
                        db.session.commit()
                        return render_template('book_info.html',
                                            book=book_to_return,
                                            score=score)
                        
                    flash("Your Book Returned Successfully.")
                    return render_template('book_info.html',
                                        book=book_to_return,
                                        score=score)
                else: 
                    flash("Please Try It Later.")
                    return render_template('book_info.html',
                                            book=book_to_return,
                                            score=score)
            except:
                flash("Something Is Wrong.")
                return render_template('book_info.html',
                                        book=book_to_return,
                                        score=score)
        else:
            return render_template('book_info.html',
                                        book=book_to_return,
                                        score=score)

    
    
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        page = request.args.get('page', 1, type=int)
        comment.searched = form.searched.data
        comment_list = Comment.query.filter( Comment.content.like(f"%{comment.searched}%"))
        comment_list = comment_list.order_by(Comment.title).paginate(page=page, per_page=8)
        return render_template('search.html',
                               form=form,
                               searched=comment.searched,
                               comment_list=comment_list,
                               page=page)

# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=False)
    # app.run(host='0.0.0.0', port='80', debug=True)
# pip freeze>requirements.txt
# pip install -r requirements.txt
# ssh에 아래 입력하면 개발자 모드 됨
# $env:FLASK_ENV="development"