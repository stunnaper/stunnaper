import unittest
import pygame
import random

# Set up display dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Bird properties
bird_x = 50
bird_y = 200
bird_size = 20
bird_velocity = 0
gravity = 0.5

# Pipe properties
pipe_width = 50
pipe_velocity = 2
pipe_gap = 150
pipe_list = []

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.circle(screen, red, (x, y), bird_size)

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, black, pipe)

def collision(pipe_list, bird_x, bird_y):
    for pipe in pipe_list:
        if pipe.collidepoint(bird_x, bird_y):
            return True
    if bird_y > height or bird_y < 0:
        return True
    return False

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            bird_velocity = -10

    # Update bird position
    bird_y += bird_velocity
    bird_velocity += gravity

    # Generate pipes
    if len(pipe_list) == 0 or pipe_list[-1].x < width - 200:
        pipe_height = random.randint(50, height - pipe_gap - 50)
        upper_pipe = pygame.Rect(width, 0, pipe_width, pipe_height)
        lower_pipe = pygame.Rect(width, pipe_height + pipe_gap, pipe_width, height - pipe_height - pipe_gap)
        pipe_list.append(upper_pipe)
        pipe_list.append(lower_pipe)

    # Move pipes to the left
    for pipe in pipe_list:
        pipe.x -= pipe_velocity

    # Remove pipes that have moved off screen
    if pipe_list[0].x < -pipe_width:
        pipe_list.pop(0)
        pipe_list.pop(0)
        score += 1

    # Check for collision
    if collision(pipe_list, bird_x, bird_y):
        running = False

    # Draw everything
    screen.fill(white)
    draw_bird(bird_x, bird_y)
    draw_pipes(pipe_list)

    # Display the score
    text = font.render(f"Score: {score}", True, black)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

class TestFlappyBird(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_collision_with_pipes(self):
        # Create a test case where bird collides with a pipe
        test_pipe = pygame.Rect(50, 50, pipe_width, height - pipe_gap - 50)
        test_pipe_list = [test_pipe]

        # Test collision
        self.assertTrue(collision(test_pipe_list, bird_x, bird_y))

    def test_collision_with_boundary(self):
        # Create a test case where bird is out of boundary
        test_pipe_list = []

        # Move the bird out of bounds
        bird_y = -10

        # Test collision
        self.assertTrue(collision(test_pipe_list, bird_x, bird_y))

    def test_no_collision(self):
        # Create a test case where there is no collision
        test_pipe_list = []

        # Test collision
        self.assertFalse(collision(test_pipe_list, bird_x, bird_y))

if __name__ == '__main__':
    unittest.main()
