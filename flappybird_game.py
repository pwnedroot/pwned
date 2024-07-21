import pygame
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 255, 0)
GRAVITY = 0.25
FLAP_SPEED = -5
PIPE_WIDTH = 50
PIPE_GAP = 150
HIGH_SCORE_FILE = "high_score.txt"  # File to store high score

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def flap(self):
        self.velocity = FLAP_SPEED

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), self.radius)

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100)
        self.top_height = self.gap_y - (PIPE_GAP // 2)
        self.bottom_height = SCREEN_HEIGHT - (self.gap_y + (PIPE_GAP // 2))
        self.width = PIPE_WIDTH
        self.speed = 3

    def update(self):
        self.x -= self.speed

    def off_screen(self):
        return self.x < -self.width

    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, SCREEN_HEIGHT - self.bottom_height, self.width, self.bottom_height))

# Function to display game over message
def game_over_message(screen, font):
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    play_again_text = font.render("Press Space To Play Again", True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 + 20))

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    bird = Bird()
    pipes = []
    frame_count = 0
    score = 0

    font = pygame.font.Font(None, 36)

    # Load high score from file
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0

    clock = pygame.time.Clock()

    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Save high score to file before quitting
                with open(HIGH_SCORE_FILE, "w") as file:
                    file.write(str(high_score))
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_over:
                        bird.flap()
                    else:
                        # Reset game if space is pressed after game over
                        bird = Bird()
                        pipes = []
                        score = 0
                        game_over = False

        screen.fill(BACKGROUND_COLOR)

        if not game_over:
            # Update bird
            bird.update()
            bird.draw(screen)

            # Generate pipes
            if frame_count % 100 == 0:
                pipes.append(Pipe())
            # Update pipes
            for pipe in pipes:
                pipe.update()
                pipe.draw(screen)
                if pipe.off_screen():
                    pipes.remove(pipe)
                    score += 1

            # Collision detection
            for pipe in pipes:
                if bird.x + bird.radius > pipe.x and bird.x - bird.radius < pipe.x + pipe.width:
                    if bird.y - bird.radius < pipe.top_height or bird.y + bird.radius > SCREEN_HEIGHT - pipe.bottom_height:
                        if score > high_score:
                            high_score = score
                        game_over = True

            # Check if bird hits top or bottom of screen
            if bird.y - bird.radius < 0 or bird.y + bird.radius > SCREEN_HEIGHT:
                if score > high_score:
                    high_score = score
                game_over = True

            # Display scores
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            screen.blit(high_score_text, (10, 40))

        else:
            # Display game over message
            game_over_message(screen, font)

        pygame.display.flip()
        clock.tick(60)
        frame_count += 1

    pygame.quit()

if __name__ == "__main__":
    main()
