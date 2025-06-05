import sqlite3
from domain.group import Group

class GroupRepository:
    def __init__(self, conn):
        self.conn = conn
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                materia TEXT,
                estilo TEXT,
                administrador_id INTEGER
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS group_participants (
                grupo_id INTEGER,
                usuario_id INTEGER
            )
        """)
        self.conn.commit()

    def add(self, group):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO groups (nome, descricao, materia, estilo, administrador_id)
            VALUES (?, ?, ?, ?, ?)
        """, (group.nome, group.descricao, group.materia, group.estilo, group.administrador_id))
        self.conn.commit()
        group.id = cursor.lastrowid

        # Adiciona o criador como participante
        cursor.execute("""
            INSERT INTO group_participants (grupo_id, usuario_id) VALUES (?, ?)
        """, (group.id, group.administrador_id))
        self.conn.commit()

        return group

    def find_by_id(self, group_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, nome, descricao, materia, estilo, administrador_id FROM groups WHERE id = ?
        """, (group_id,))
        row = cursor.fetchone()
        return Group(*row) if row else None

    def find_by_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT g.id, g.nome, g.descricao, g.materia, g.estilo, g.administrador_id
            FROM groups g
            JOIN group_participants gp ON gp.grupo_id = g.id
            WHERE gp.usuario_id = ?
        """, (user_id,))
        rows = cursor.fetchall()
        return [Group(*row) for row in rows]

    def search(self, termo, estilo=None):
        cursor = self.conn.cursor()
        query = """
            SELECT id, nome, descricao, materia, estilo, administrador_id
            FROM groups
            WHERE (nome LIKE ? OR descricao LIKE ? OR materia LIKE ?)
        """
        params = [f"%{termo}%", f"%{termo}%", f"%{termo}%"]

        if estilo:
            query += " AND estilo = ?"
            params.append(estilo)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [Group(*row) for row in rows]

    def delete(self, grupo_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM group_participants WHERE grupo_id = ?", (grupo_id,))
        cursor.execute("DELETE FROM groups WHERE id = ?", (grupo_id,))
        self.conn.commit()

    def find_participating_but_not_admin(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT g.id, g.nome, g.descricao, g.materia, g.estilo, g.administrador_id
            FROM groups g
            JOIN group_participants gp ON gp.grupo_id = g.id
            WHERE gp.usuario_id = ? AND g.administrador_id != ?
        """, (user_id, user_id))
        rows = cursor.fetchall()
        return [Group(*row) for row in rows]

    def add_participant(self, grupo_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 1 FROM group_participants WHERE grupo_id = ? AND usuario_id = ?
        """, (grupo_id, user_id))
        if cursor.fetchone():
            return False  # já participa
        cursor.execute("""
            INSERT INTO group_participants (grupo_id, usuario_id) VALUES (?, ?)
        """, (grupo_id, user_id))
        self.conn.commit()
        return True

    def user_participates(self, grupo_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT 1 FROM group_participants
            WHERE grupo_id = ? AND usuario_id = ?
        """, (grupo_id, user_id))
        return cursor.fetchone() is not None
