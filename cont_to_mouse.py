import pyautogui
import pygame
import sys

pygame.init()
pygame.joystick.init()

# Check if a joystick/controller is connected
if pygame.joystick.get_count() < 1:
    print("No joystick detected.")
    sys.exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Set up mouse variables
mouse_speed = 150
left_button_down = False

# Set up scrolling variables
scroll_speed = 50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # Left mouse button
                left_button_down = True
                pyautogui.mouseDown(button='left')
            elif event.button == 1:  # Right mouse button
                pyautogui.click(button='right')
            elif event.button == 4:  # Left trigger
                pyautogui.hotkey('ctrl', 'c')  # Copy
            elif event.button == 5:  # Right trigger
                pyautogui.hotkey('ctrl', 'v')  # Paste
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:  # Left mouse button
                left_button_down = False
                pyautogui.mouseUp(button='left')

    # Get joystick axes for mouse movement
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    # Move mouse
    pyautogui.moveRel(x_axis * mouse_speed, y_axis * mouse_speed)

    # Handle mouse dragging
    if left_button_down:
        pyautogui.moveRel(x_axis * mouse_speed, y_axis * mouse_speed)

    # Get joystick axes for scrolling
    scroll_axis = joystick.get_axis(3)  # Assuming the second joystick's vertical axis is axis 3

    # Handle scrolling
    if abs(scroll_axis) > 0.1:  # Adjust the threshold as needed
        scroll_amount = int(scroll_axis * scroll_speed)
        pyautogui.scroll(-scroll_amount)  # Negate the scroll amount to flip the direction

# Clean up
pygame.quit()