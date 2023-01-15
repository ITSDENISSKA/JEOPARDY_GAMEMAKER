import sqlite3


class DataBase:
    def __init__(self, file_name):
        self.connection = sqlite3.connect(file_name)
        self.cursor = self.connection.cursor()

    def add_players(self, list_of_players):
        players = [name[0] for name in self.cursor.execute("""SELECT name FROM users""").fetchall()]
        for player in list_of_players:
            if player not in players:
                self.cursor.execute("""INSERT INTO users(name) VALUES(?)""", (player,))
                self.cursor.execute("""INSERT INTO games(id,count, wins, scores)
                     VALUES((SELECT id FROM users WHERE name = ?), 0, 0, 0)""", (player,))

            player_id = self.cursor.execute("""SELECT id FROM users WHERE name = ?""",
                                            (player,)).fetchall()
            number_of_game = self.cursor.execute("""SELECT count FROM games WHERE id = ?""",
                                                 (player_id[0][0],)).fetchall()
            if len(number_of_game) == 0 or number_of_game[0][0] is None:
                number_of_game = [(0,)]
            self.cursor.execute("""UPDATE games SET count = ? WHERE id = ?""",
                                (number_of_game[0][0] + 1, player_id[0][0]))
        self.connection.commit()

    def get_data(self):
        try:
            table_elementsreferences = sorted(
                self.cursor.execute("""SELECT id, count, scores, wins FROM games""").fetchall())
            for index in range(len(table_elementsreferences)):
                table_elementsreferences[index] = list(table_elementsreferences[index])
                table_elementsreferences[index][0] = \
                    self.cursor.execute("""SELECT name FROM users WHERE id = ?""",
                                        (table_elementsreferences[index][0],)).fetchall()[0][0]
                table_elementsreferences[index] = tuple(table_elementsreferences[index])

            return table_elementsreferences

        except Exception:
            return "Error"

    def close_database(self):
        self.connection.close()

    def add_score(self, player):
        old_score = self.cursor.execute(
            """SELECT scores FROM games WHERE id=(SELECT id FROM users WHERE name = ?)""", (player.name,)).fetchall()[
            0][0]
        self.cursor.execute("""UPDATE games SET scores = ? WHERE id = (SELECT id FROM users WHERE name = ?)""",
                            (player.score + old_score, player.name))
        self.connection.commit()

    def add_win(self, player):
        old_wins_count = self.cursor.execute(
            """SELECT wins FROM games WHERE id=(SELECT id FROM users WHERE name = ?)""", (player.name,)).fetchall()[
            0][0]
        self.cursor.execute("""UPDATE games SET wins = ? WHERE id = (SELECT id FROM users WHERE name = ?)""",
                            (old_wins_count + 1, player.name))
        self.connection.commit()
