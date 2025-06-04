from flask import Blueprint, render_template, request, redirect, session

def create_group_routes(group_use_case):
    bp = Blueprint("group", __name__)

    @bp.route("/criar-grupo", methods=["GET", "POST"])
    def criar_grupo():
        if "user_id" not in session:
            return redirect("/login")

        if request.method == "POST":
            nome = request.form["nome"]
            descricao = request.form["descricao"]
            materia = request.form["materia"]
            estilo = request.form["estilo"]
            admin_id = session["user_id"]
            grupo = group_use_case.create_group(nome, descricao, materia, estilo, admin_id)
            return redirect(f"/grupo/{grupo.id}")

        return render_template("criar_grupo.html")

    @bp.route("/grupo/<int:grupo_id>")
    def ver_grupo(grupo_id):
        grupo = group_use_case.get_group(grupo_id)
        if not grupo:
            return "Grupo não encontrado", 404
        return render_template("grupo.html", grupo=grupo)

    return bp
