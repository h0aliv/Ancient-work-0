from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from random import *
#theme: battle campaign clicker, recruit soldier to capture the world.
#Feature: Added a campaign map, which will upadate once the player capture enought barracks. Recruiting soldier will show the arming image.
#Feature: To battle system, which will subtract the amount of soldiers a player has entered from the total amount to have a chance capture recruiters or barracks.
#the amount of captured things depends on how many soldier the player put in.

class ImageSwitch(QMainWindow):

    def __init__(self, image1, image2):
        super().__init__()
        # setting up varibles
        self.triggered = 0
        self.capcamp = 0
        self.of = 15
        self.progress = 0
        self.count1 = 0
        self.count2 = 0
        self.add1 = 0
        self.add2 = 0
        self.c1 = 125
        self.t1 = 500
        self.c2 = 600
        self.amount = 0
        self.map1 = QPixmap('map1.jpg')
        self.map2 = QPixmap('map2.jpg')
        self.map3 = QPixmap('map3.jpg')
        self.map4 = QPixmap('map4.jpg')
        self.map5 = QPixmap('map5.jpg')
        self.map6 = QPixmap('map6.jpg')
        self.image1 = image1
        self.image2 = image2
        self.use_image_one = True
        self.setupUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_amount)
        self.update_amount()
        self.timer.start(100)
    def setupUI(self):

        #setting up menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&Menu')
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        reset_action = QAction('reset', self)
        reset_action.triggered.connect(self.reset)
        file_menu.addAction(reset_action)
        file_menu.addAction(exit_action)

        #setting up layout and buttons etc
        self.frame = QFrame()
        vertical_lay = QVBoxLayout()
        layout = QHBoxLayout()
        layout1 = QHBoxLayout()
        lvl_lay = QVBoxLayout()
        title_lay = QHBoxLayout()
        lvl_cost = QVBoxLayout()
        battle_layout = QVBoxLayout()
        self.frame.setLayout(vertical_lay)
        self.setCentralWidget(self.frame)

        top = QPushButton('recruit soldiers')
        layout.addWidget(top)
        self.lvl1 = QPushButton('recruiter + 1')
        lvl_lay.addWidget(self.lvl1)
        self.lvl2 = QPushButton('???')
        lvl_lay.addWidget(self.lvl2)
        layout1.addLayout(lvl_lay)
        layout1.addLayout(lvl_cost)

        self.label = QLabel()
        self.label.setPixmap(self.image1)
        layout.addWidget(self.label)
        self.result_label = QLabel()
        layout1.addWidget(self.result_label)
        self.title = QLabel('Conquering Clicker')
        title_lay.addWidget(self.title)
        self.title1 = QLabel('Press recruit to start')
        title_lay.addWidget(self.title1)
        self.cost1 = QLabel(str(self.c1))
        lvl_cost.addWidget(self.cost1)
        self.cost2 = QLabel('500')
        lvl_cost.addWidget(self.cost2)
        self.troops_entry = QLineEdit()
        self.troops_entry.setText("0")
        battle_layout.addWidget(self.troops_entry)
        self.battle_button = QPushButton("To battle!")
        battle_layout.addWidget(self.battle_button)
        self.battle_result = QLabel('a battle takes at least 50 soldiers')
        battle_layout.addWidget(self.battle_result)
        self.news = QLabel('captured barracks: 0')
        battle_layout.addWidget(self.news)
        self.map = QLabel()
        self.map.setPixmap(self.map1)
        battle_layout.addWidget(self.map)
        vertical_lay.addLayout(title_lay)
        vertical_lay.addLayout(layout)
        vertical_lay.addLayout(layout1)
        vertical_lay.addLayout(battle_layout)
        top.clicked.connect(self.switch_image)
        top.clicked.connect(self.clicked)
        self.lvl1.clicked.connect(self.activate_lvl1)
        self.lvl2.clicked.connect(self.activate_lvl2)
        self.battle_button.clicked.connect(self.to_battle)
    def update_amount(self):

        #upadte display
        self.repaint()
        self.result_label.setText("soldiers total: {0} soldiers recruited per sec: {1:10.2f}".format(self.amount, self.add2 + self.add1))
        self.cost1.setText("cost: {0}".format(self.c1))
        self.cost2.setText("cost: {0}".format(self.c2))
        if self.progress >=5:
            self.news.setText('you conquer the world!!!')
        else:
            self.news.setText('Captured barracks: {0}  News: In order to occupy the land u need to capture {1} barracks'.format(self.capcamp,self.of))
        if self.triggered == 1:
            self.lvl2.setText("barracks +5")
        self.map_progress()
    def clicked(self):

        #cookie clicking function
        self.amount += 100
    def increase_amount(self):

        #upadate total soldiers count
        self.amount += self.add1 + self.add2

    def activate_lvl1(self):

        #function button 1
        if self.amount >= self.c1:
            self.amount -= self.c1
            self.c1 = self.c1 * 1.1 // 1
            self.add1 += 1

            if self.triggered == 0:
                self.timer1 = QTimer()
                self.timer1.timeout.connect(self.switch_image)
                self.timer1.timeout.connect(self.increase_amount)
                self.timer1.start(self.t1)
                self.triggered = 1

    def activate_lvl2(self):

        # function button 2
        if self.amount >= self.c2:
            self.amount -= self.c2
            self.c2 = self.c2 * 1.1 // 1
            self.add2 += 5
            if self.triggered == 0:
                self.timer1 = QTimer()
                self.timer1.timeout.connect(self.switch_image)
                self.timer1.timeout.connect(self.increase_amount)
                self.timer1.start(self.t1)
                self.triggered = 1


    def switch_image(self):
        #clicker image switch function
        if self.use_image_one:
            self.label.setPixmap(self.image2)
            self.use_image_one = False
        else:
            self.label.setPixmap(self.image1)
            self.use_image_one = True
        self.repaint()
    def map_progress(self):
        #update campaign map progress function
        if self.progress == 0:
            self.map.setPixmap(self.map1)
        elif self.progress == 1:
            self.map.setPixmap(self.map2)
        elif self.progress == 2:
            self.map.setPixmap(self.map3)
        elif self.progress == 3:
            self.map.setPixmap(self.map4)
        elif self.progress == 4:
            self.map.setPixmap(self.map5)
        elif self.progress == 5:
            self.map.setPixmap(self.map6)
    def quit_program(self):
        qApp.quit()
    def reset(self):
        #Reset Function
        self.c1 = 50
        self.t1 = 500
        self.c2 = 500
        self.add2 = 0
        self.add1 = 0
        self.amount = 0
        self.timer1.stop()
        self.triggered = 0
        self.progress = 0
        self.capcamp = 0
        self.of = 15
        self.using_image_one = True
        self.label.setPixmap(self.image1)
    def to_battle(self):
        #battle system main codes
        self.troops = int(self.troops_entry.text())
        self.count1 = 0
        self.count2 = 0
        if self.troops >= 50 and self.amount >= self.troops:

            self.amount -= self.troops
            self.troops -= 49

            for n in range(self.troops):
                self.chance = randint(0,1000)
                if self.chance > 970 and self.chance < 985:
                    self.add1 += 1
                    self.count1 += 1
                elif self.chance > 996:
                    self.add2 += 5
                    self.count2 += 1
            self.capcamp += self.count2
            if self.capcamp >= self.of:
                self.of += 10
                self.capcamp = 0
                self.progress += 1
            self.battle_result.setText("{0} recruiters and {1} barracks are captured in this battle".format(self.count1, self.count2))
            if self.triggered == 0:
                if self.count1 > 0 or self.count2 > 0:
                    self.timer1 = QTimer()
                    self.timer1.timeout.connect(self.switch_image)
                    self.timer1.timeout.connect(self.increase_amount)
                    self.timer1.start(self.t1)
                    self.triggered = 1

        else:
            self.battle_result.setText("no enough troops")

app = QApplication([])
i = QPixmap('white.png')
i2 = QPixmap('white_melee.png')

window = ImageSwitch(i, i2)

window.show()

app.exec_()