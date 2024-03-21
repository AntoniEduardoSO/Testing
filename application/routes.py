from datetime import timedelta
import datetime
from application import app, login_manager, db
from flask import render_template, request, redirect, flash, session, url_for, Response, jsonify, make_response
from flask_login import user_unauthorized, login_user, login_required, logout_user, current_user, user_logged_out
from application.api.models.usuario import User, RegisterForm, LoginForm
from application.api.models.sessoes import Sessoes
from application.api.models.escola import Escola
from application.api.models.agenda import Agenda
from application.backend.dashboard import dashboard_valores
from application.backend.home import verificar_login
from application.backend.cadastro import verificar_cadastro
from application.backend.sessao import checar_sessao_expirada
from application.backend.agenda import api_agenda_backend, agenda_form
from werkzeug.utils import secure_filename
from sqlalchemy import and_
import os

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("nao_autorizado.html")


@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(id_usuario))


@app.before_request
def atualizar_dt_inicio():
    if not current_user.is_anonymous and request.method == "POST":
        user = current_user
        if user:
            sessao = Sessoes.query.filter_by(user_id=user.id_usuario).first()
            if sessao:
                app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=60)
                sessao.dt_inicio = datetime.datetime.now()
                db.session.commit()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['POST', 'GET'])
def home():
    
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        if verificar_login(form):
            session.pop('_flashes', None)
            session.permanent = True
            session.modified = True
            flash("Sistema ainda em desenvolvimento.", "info")
            flash("Login feito com sucesso.", "message")

            
            return redirect(url_for('dashboard'))
        


    return render_template("home.html", form = form)



@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastro():
    form =  RegisterForm()

    if verificar_cadastro(form):
        flash("Cadastro feito com sucesso.", "message")
        return redirect(url_for('home'))
    
    return render_template('cadastro.html', form = form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    user =  current_user
    session = Sessoes.query.filter_by(user_id=user.id_usuario).first()
    db.session.delete(session)
    db.session.commit()
    logout_user()

    flash('Desconectado!', 'info')
    return redirect(url_for('home'))


@app.route('/configuracao_usuario', methods=['GET', 'POST'])
@login_required
def configuracao_usuario():
    main_usuario = current_user

    if request.method == 'POST':


        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            flash("Nenhum arquivo enviado", "error")
            return redirect(request.url)
        
        if not allowed_file(file.filename):
            flash(f"Utilize os tipos corretos: .jpg, .png, .jpeg, .gif", "error")
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            main_usuario.foto = secure_filename(f"usuario_{main_usuario.id_usuario}_foto.png")

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], main_usuario.foto)

            file.save(file_path.replace("\\","/"))

            db.session.commit()
            flash("Imagem enviada com sucesso!", "message")

    return render_template('configuracao_usuario.html', main_usuario = main_usuario)

@app.route('/usuarios', methods=['POST', 'GET'])
@login_required
def usuarios():
    main_usuario = current_user
    usuarios = User.query.filter(User.id_usuario != main_usuario.id_usuario).all()

    if request.method == "POST":
        atributo = request.form['atributo-search']

        print("Atributo: " +  atributo)
        filtro = request.form.get("filtro-search")

        if atributo == "Setor":
            usuarios = User.query.filter(and_(User.id_usuario != main_usuario.id_usuario, User.setor_escola == filtro)).all()
            # usuarios = User.query.filter(User.id_usuario != main_usuario.id_usuario and User.setor_escola == filtro).all()

        elif atributo == "Nome":
            usuarios = User.query.filter(and_(User.id_usuario != main_usuario.id_usuario, User.nome.ilike(f"%{filtro}%"))).all()

        elif atributo == "Todos":
            usuarios = User.query.filter(User.id_usuario != main_usuario.id_usuario).all()


    return render_template('usuarios.html', main_usuario=main_usuario, usuarios=usuarios)


@app.route('/usuarios/<int:id_usuario>', methods=["GET", "POST"])
@login_required
def usuario(id_usuario):
    main_usuario = current_user
    usuario = User.query.filter(User.id_usuario == id_usuario).first()

    if request.method == "POST":
        cargo = request.form["Status"]

        usuario.status = cargo
        db.session.commit()


    return render_template('usuario.html', main_usuario=main_usuario,  usuario = usuario)



@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():
    main_usuario = current_user


    return render_template("dashboard.html", main_usuario=main_usuario)



@app.route('/dashboard/semap', methods=["POST", "GET"])
@login_required
def semap():
    main_usuario = current_user


    return render_template("semap.html")

@app.route('/dashboard/semap/listasetores', methods = ["POST", "GET"])
def listasetores():
    main_usuario = current_user

    return render_template("listasetores.html", main_usuario = main_usuario)


@app.route('/dashboard/semap/modificarsetor/<int:id>')
@login_required
def modificarsetor(id):

    return """ <h1>olaaa</h1> """




@app.route('/dashboard/semap/agenda', methods=["POST", "GET"])
@login_required
def agenda():

    main_usuario = current_user

    if request.method == "POST" and agenda_form():
        flash('Agenda adicionada com sucesso', "message")


    else:
        flash('Agenda não foi possível de ser feita', "error")
         

    return render_template("agenda.html", main_usuario=main_usuario)


@app.route('/dashboard/semap/testes', methods = ["POST", "GET"])
@login_required
def teste():
    main_usuario = current_user

    return render_template("teste.html")


@app.route('/escolas', methods = ["POST", "GET"])
def escolas():
    main_usuario = current_user

    escolas = Escola.query.all()


    return render_template("escolas.html", escolas = escolas)




@app.route('/api/agenda/<string:data>', methods=["GET"])
def api_agenda(data):
    return api_agenda_backend(data)