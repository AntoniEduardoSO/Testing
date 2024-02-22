from application import app, login_manager

from flask import render_template, request, redirect, flash, session, url_for, Response, jsonify, make_response
from flask_login import user_unauthorized, login_user, login_required, logout_user, current_user, user_logged_out
from application.api.models.usuario import User, RegisterForm, LoginForm
from application.backend.dashboard import dashboard_valores
from application.backend.home import verificar_login
from application.backend.cadastro import verificar_cadastro

@login_manager.unauthorized_handler
def unauthorized():
    return render_template("nao_autorizado.html")


@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(id_usuario))


@app.route('/', methods=['POST', 'GET'])
def home():
    if 'flash_displayed' not in session:
        flash("Sistema ainda em desenvolvimento.", "info")
        session['flash_displayed'] = True
    
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        if verificar_login(form):
            session.pop('_flashes', None)
            flash("Login feito com sucesso.", "message")
            return redirect(url_for('dashboard'))
        


    return render_template("home.html", form = form)



@app.route('/cadastro', methods = ['POST', 'GET'])
def cadastro():
    form =  RegisterForm()

    if verificar_cadastro(form):
        flash("Cadastro feito com sucesso.", "message")
        flash("")
        return redirect(url_for('home'))
    
    return render_template('cadastro.html', form = form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():
    main_usuario = current_user


    return render_template("dashboard.html")