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

    @bp.route("/meus-grupos")
    def meus_grupos():
        if "user_id" not in session:
            return redirect("/login")
        
        user_id = session["user_id"]
        grupos = group_use_case.list_by_user(user_id)
        return render_template("meus_grupos.html", grupos=grupos)

    @bp.route("/buscar-grupos", methods=["GET"])
    def buscar_grupos():
        if "user_id" not in session:
            return redirect("/login")

        termo = request.args.get("q", "")
        estilo = request.args.get("estilo", None)

        grupos = group_use_case.search_groups(termo, estilo)

        # Dicionário: grupo.id => True se já participa, False caso contrário
        participando = {}
        user_id = session["user_id"]
        for grupo in grupos:
            participando[grupo.id] = group_use_case.user_is_participant(grupo.id, user_id)

        return render_template(
            "buscar_grupos.html",
            grupos=grupos,
            termo=termo,
            estilo=estilo,
            participando=participando
        )

    @bp.route("/grupo/<int:grupo_id>/deletar", methods=["POST"])
    def deletar_grupo(grupo_id):
        if "user_id" not in session:
            return redirect("/login")

        grupo = group_use_case.find_by_id(grupo_id)
        if not grupo or grupo.administrador_id != session["user_id"]:
            return "Acesso não autorizado", 403

        group_use_case.delete(grupo_id)
        return redirect("/meus-grupos")

    @bp.route("/grupos-participo")
    def grupos_participo():
        if "user_id" not in session:
            return redirect("/login")

        user_id = session["user_id"]
        grupos = group_use_case.get_participating_but_not_admin(user_id)
        return render_template("grupos_participo.html", grupos=grupos)

    @bp.route("/grupo/<int:grupo_id>/entrar", methods=["POST"])
    def entrar_grupo(grupo_id):
        if "user_id" not in session:
            return redirect("/login")
        
        user_id = session["user_id"]
        group_use_case.enter_group(grupo_id, user_id)
        return redirect(f"/grupo/{grupo_id}")

    return bp
