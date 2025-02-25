import pygame
from helpers import screen
from constants import *
from helpers import from_text_to_array
from helpers import read_comment_from_user
COLORS = {
    "BLACK": BLACK,
    "WHITE": WHITE,
    "GRAY": GREY,
    "LIGTH_GRAY": LIGHT_GRAY
}


def is_image(content):
    if content.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        return True
    return False


class Post:
    def __init__(self, user_name, location, description, likes_counter, comments):
        self.user_name = user_name
        self.location = location
        self.description = description
        self.likes_counter = likes_counter
        self.comments = []

    def likes(self):
        self.likes_counter += 1

    def comment(self, comment):
        self.comments.append(comment)

    def display(self):
        self.display_user_name()
        self.display_location()
        self.display_like()
        self.display_description()

    def display_user_name(self):
        user_name = font.render(self.user_name, True, BLACK)
        screen.blit(user_name, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def display_location(self):
        location = font.render(self.location, True, BLACK)
        screen.blit(location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

    def display_like(self):
        likes_counter = font.render(self.likes_counter, True, BLACK)
        screen.blit(likes_counter, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def display_description(self):
        description = font.render(self.description, True, BLACK)
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_comments(self):
        new_comment_text = read_comment_from_user()
        new_comment_text = Comment(new_comment_text)



class ImagePost(Post):
    def __init__(self, user_name, location, description, likes_counter, comments, content):
        self.image = content
        super().__init__(user_name, location, description, likes_counter, comments)

    def display_post_img(self):
        post_image = pygame.image.load(self.image)
        post_image = pygame.transform.scale(post_image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(post_image, (POST_X_POS, POST_Y_POS))

    def display(self):
        self.display_post_img()
        super().display()


class TextPost(Post):
    def __init__(self, user_name, location, description, likes_counter, comments, content):
        self.text = content
        self.new_text = []
        self.color_tx = (0, 0, 0)
        self.background_color = (0, 0, 0)
        super().__init__(user_name, location, description, likes_counter, comments)

    def process_text(self):
        self.new_text = from_text_to_array(self.text)

    # def text_color(self):
    #     color_tx = input("Which color you want to use: BLACK, WHITE, GREY, or LIGHT_GREY")
    #     if color_tx.upper() not in COLORS:
    #         print("There is no color like that, try another one: ")
    #         return self.text_color()
    #
    #     self.color_tx = COLORS[color_tx.upper()]
    #
    # def background_text_color(self):
    #     background_color = input("Which color you want to use: BLACK, WHITE, GREY, or LIGHT_GREY")
    #     if background_color.upper() not in COLORS:
    #         print("There is no color like that, try another one: ")
    #         return self.background_text_color()
    #     elif COLORS[background_color] == self.color_tx:
    #         print("If you choose this color you want see the text, try another one: ")
    #         return self.background_text_color()
    #
    #     self.background_color = COLORS[background_color.upper()]

    def display_post_text(self):
        # self.text_color()
        # self.background_text_color()
        text_surface = font.render(self.text, True, BLACK, WHITE)
        text_rect = text_surface.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
        screen.blit(text_surface, text_rect)

    def display(self):
        self.display_post_text()
        super().display()

class Comment:
    def __init__(self, comment_text):
        self.comment_text = read_comment_from_user()





def main():
    global background, font
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load(BACKGROUND_IMG)
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.Font(None, 20)
    running = True

    post = ImagePost("USER_NAME", "LOCATION", "DESCRIPTION", "LIKES_COUNTER",
                     "COMMENT", RONALDO_IMG)


    # Display the background, presented Image, likes, comments, tags and location(on the Image)
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    post.display()
    # Update display - without input update everything
    pygame.display.update()
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
