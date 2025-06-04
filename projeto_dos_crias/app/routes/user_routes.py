# app/routes/user_routes.py

from flask import Blueprint, request, render_template, redirect, session, url_for

def create_user_routes(user_use_case):
    user_bp = Blueprint('user', __name__)

    @user_bp.route("/criar-perfil", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            user_use_case.register(name, email, password)
            return redirect("/login")
        return render_template("register.html")

    @user_bp.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            user = user_use_case.login(email, password)
            if user:
                session["user_id"] = user.id
                return redirect("/inicio")
            return render_template("login.html", error="Credenciais inválidas")
        return render_template("login.html")
    

    @user_bp.route("/inicio")
    def inicio():
        if "user_id" not in session:
            return redirect("/login")
        return render_template("home.html")

    @user_bp.route("/perfil", methods=["GET", "POST"])
    def perfil():
        if "user_id" not in session:
            return redirect("/login")

        user_id = session["user_id"]
        user = user_use_case.find_by_id(user_id)

        if request.method == "POST":
            user.name = request.form["name"]
            user.email = request.form["email"]
            user.faculdade = request.form["faculdade"]
            user.cursos = request.form["cursos"]
            user_use_case.update_user(user)
            return redirect("/inicio")

        return render_template("perfil.html", user=user)


    return user_bp
