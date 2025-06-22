# Turtle Crosswalk Project

This Python application utilizes the `turtle` module to create an interactive simulation of a turtle crossing a road. 
The turtle represent a pedestrian and the application simulates traffic, allowing the user to navigate the turtle crossing the road while avoiding cars.

## Key Features

**Game Setup with Turtle Graphics:**
  - The game uses the `turtle` module to create a graphical window where the simulation takes place. The screen is set up with a specified width and height.

**Turtle Class for Pedestrians:**
  - The `Turtle` class defines the behavior of the turtle (pedestrian) that will cross the road. The turtle can move forward and change direction based on user input.

**Car Class for Traffic Simulation:**
  - The `Car` class defines the behavior of cars that move across the screen. The cars can be generated at random intervals and move from one side of the screen to the other.

**Game Logic and Collision Detection:**
  - The main game loop updates the screen, moves the turtle and cars and checks for collisions between the turtle and the car. If a collision occurs, the game can end or reset.

**User Controls:**
  - The application can include user controls to start the simulation, reset the game or adjust settings.

As the turtle successfully crosses the road and reachs the top of the screen, the game's difficulty level increases. With each successful crossing, the speed of the oncoming cars increases, creating a more challenging environment for the turtle.
The Player must navigate the turtle with greater precision and timing to avoid collisions, making the game progressively more exciting and demanding.
