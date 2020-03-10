import Lesson_9_game as game

play = game.Allcards()
play.get_values()
play.get_trump()
play.get_trump_values()
play.user_cards()
play.comp_cards()
play.first_turn()

print(play.play_game())