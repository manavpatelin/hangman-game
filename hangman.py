import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from ui_hangman import Ui_MainWindow
from datastore import Datastore

class MainWindow:
    def __init__(self):
         #------------ setup UI element -------------# 
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        #------------- INITIALIZE GAME VARIABLE-----------#
        self.db=Datastore()
        self.word = ""
        self.guessed_word = []
        self.misses = 0

        #---------------Initillize the ui with starting values--------#
        self.choose_word()
        self.display_guesses()
        self.display_gallows()
        self.signals()
         
    def show(self):
        self.main_win.show()

    def choose_word(self):
        self.word = self.db.get_word()
        self.guessed_word = ["_"]*len(self.word)
        print(self.word)

    def display_guesses(self):
        
        display_word = ""
        for character in self.guessed_word:
            display_word = display_word + character +" "
        
        self.ui.word_lb.setText(display_word)

    def display_gallows(self):
        file_name = (f"./assets/{self.misses}.png")
        gallow = QPixmap(file_name)
        self.ui.gallow_lb.setPixmap(gallow)

    def set_button_enabled(self,val):

        self.ui.a_btn.setEnabled(val)
        self.ui.b_btn.setEnabled(val)
        self.ui.c_btn.setEnabled(val)
        self.ui.d_btn.setEnabled(val)
        self.ui.e_btn.setEnabled(val)
        self.ui.f_btn.setEnabled(val)
        self.ui.g_btn.setEnabled(val)
        self.ui.h_btn.setEnabled(val)
        self.ui.i_btn.setEnabled(val)
        self.ui.j_btn.setEnabled(val)
        self.ui.k_btn.setEnabled(val)
        self.ui.l_btn.setEnabled(val)
        self.ui.m_btn.setEnabled(val)
        self.ui.n_btn.setEnabled(val)
        self.ui.o_btn.setEnabled(val)
        self.ui.p_btn.setEnabled(val)
        self.ui.q_btn.setEnabled(val)
        self.ui.r_btn.setEnabled(val)
        self.ui.s_btn.setEnabled(val)
        self.ui.t_btn.setEnabled(val)
        self.ui.u_btn.setEnabled(val)
        self.ui.v_btn.setEnabled(val)
        self.ui.w_btn.setEnabled(val)
        self.ui.x_btn.setEnabled(val)
        self.ui.y_btn.setEnabled(val)
        self.ui.z_btn.setEnabled(val)



    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        #control btn
        self.ui.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.new_word_btn.clicked.connect(self.new_word_btn)
        #letter btn
        for letter in "abcdefghijklmnopqrstuvwxyz":
            getattr(self.ui, f"{letter}_btn").clicked.connect(lambda checked, l=letter: self.letter_btn(getattr(self.ui, f"{l}_btn")))

    
    # ----- slots ----- #
    
    def new_word_btn(self):

        #get new word
        self.choose_word()
        self.display_guesses()

        #reset GUI
        self.misses = 0
        self.display_gallows()
        self.set_button_enabled(True)
        self.ui.result_lb.setText("")
    
    def letter_btn(self,button):
        
        #guess letter
        guess = button.text().lower()
        print(guess)

        #disable lettler
        button.setEnabled(False)
       
        #check if letter in word
        if guess in self.word:
            for index,letter in enumerate(self.word):
                if guess == letter:
                    self.guessed_word[index] = guess.upper()
            self.display_guesses()
            #check for win
            if "_" not in self.guessed_word:
                self.ui.result_lb.setText("!! Winner !!")
        else:
            self.misses += 1
            self.display_gallows()
            if self.misses == 11:
                self.ui.result_lb.setText(f"The word was {self.word.upper()}")
                self.set_button_enabled(False)

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())