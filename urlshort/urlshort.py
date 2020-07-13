from flask import render_template,request,redirect,url_for,flash,abort,session,jsonify,Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort',__name__)

#function to display Homepage
@bp.route('/')
def home():
    return render_template('home.html',codes=session.keys())


#function to display URL Page using POST requests and redirecting back to home if method='GET'
@bp.route('/your-url',methods=['GET','POST'])
def your_url():
    if request.method=='POST':
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        
        if request.form['code'] in urls.keys():
            flash('Short Name has already been taken. Please select another name.')
            return redirect(url_for('urlshort.home'))        
        
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename) 
            f.save('/home/pratik/flask_projects/url-shortener/urlshort/static/user_files/'+full_name)
            urls[request.form['code']] = {'file':full_name}  


        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
            session[request.form['code']] = True
        return render_template('your_url.html',code=request.form['code'])  
    else:
        return redirect(url_for('urlshort.home'))

#function to redirect based on availability and repitition of keys(code)
@bp.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static',filename='user_files/'+urls[code]['file']))
    return abort(404)

#custom error handling page for 404
@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#converting session keys into json
@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))

#function to display Login Page
@bp.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

#function to display Registration Page
@bp.route('/register')
def register():
    return render_template('register.html')

