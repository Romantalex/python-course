import unittest2
from Lesson_9_game import Allcards

class Testgame_pytest:

    def setUp(self):
        self.gameclass = Allcards()
        self.play1 = self.gameclass.get_values()
        self.play2 = self.gameclass.get_trump()
        self.play3 = self.gameclass.get_trump_values()
        print('Start test!')

    def tearDown(self):
        print('Finish test!')

    def test_trump(self):
        self.assertTrue(self.play2 in self.play3)

    def test_playerscards(self):
        self.play4 = self.gameclass.user_cards()
        self.play5 = self.gameclass.comp_cards()
        self.play6 = self.gameclass.first_turn()
        self.assertTrue(self.play6.keycard in self.play4) or (self.play6.keycard in self.play5)

    def test_turn(self):
        self.play7 = self.gameclass.play_game()
        self.assertTrue(self.play7.first_player == 'user') 
