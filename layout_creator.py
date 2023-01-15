from PyQt5.QtWidgets import QSizePolicy, QLabel
from PyQt5 import QtWidgets


class LayoutCreator:
    def __init__(self, checkbox_input_ans):
        self.checkbox_input_ans = checkbox_input_ans

    def create_layout_with_players(self, player, widget, lbl_first):
        lbl_first.setText(str(player.name + '\nСчёт: ' + '\n' + str(player.get_score())))
        layout_with_player_data = QtWidgets.QGridLayout(widget)
        if not self.checkbox_input_ans:
            btn_true = QtWidgets.QPushButton(widget)
            btn_true.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            layout_with_player_data.addWidget(btn_true, 1, 0, 1, 1)
            btn_true.setText('✅️️️')
            btn_false = QtWidgets.QPushButton(widget)
            btn_false.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            layout_with_player_data.addWidget(btn_false, 1, 1, 1, 1)
            btn_false.setText('❌')
            lbl = QLabel(widget)
            lbl.setText(str(player.name))
            lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            layout_with_player_data.addWidget(lbl, 0, 0, 1, 2)
            return btn_true, btn_false, lbl_first
        else:
            btn_ans = QtWidgets.QPushButton(widget)
            btn_ans.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            layout_with_player_data.addWidget(btn_ans, 1, 0, 1, 1)
            btn_ans.setText('Ответить')
            lbl = QLabel(widget)
            lbl.setText(str(player.name))
            lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            layout_with_player_data.addWidget(lbl, 0, 0, 1, 2)
            return btn_ans, lbl_first
