import pygame
import pygame.font


class Scoreboard():
    def __init__(self, screen, stats):
        #score visualization
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.stats = stats

        # text settings
        self.text_color = (223, 194, 194)
        self.font = pygame.font.SysFont("dejavusansmono", 30)

        #renders the score box 
        self.prep_score()


    def prep_score(self):
        #renders the score box

        #round the score e.g.  10000 -> 10,000
        round_score = round(self.stats.score, -1)
        score_str = str("Score: " + str("{:,}".format(round_score)))
        self.score_img = self.font.render(score_str, True,
                                          self.text_color, None)

        #creates the score rectangle
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 5 # show the full score
        self.score_rect.top = 10

    def show_score(self):
        #draws the score
        self.screen.blit(self.score_img, self.score_rect)
