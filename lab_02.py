# Import the "arcade" library
import arcade

# Open up a window
# From the "arcade" library, use a function called "open_window"
# Set the window title to "The village"
# Set the dimension (width and height
arcade.open_window(600, 600, "The village")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 200, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.csscolor.GREEN)

# Draw a hill with an arc
# Arc is centered at (350, 200) with a width of 500 and height of 300
# The start angle is 0, and ending angle is 180.
arcade.draw_arc_filled(350, 200, 500, 300, arcade.csscolor.DARK_OLIVE_GREEN, 0, 180)

# Draw a road
# Rectangle center of 0, 70
# Width of 1199, and height of 70
arcade.draw_rectangle_filled(0, 70, 1199, 70, arcade.csscolor.GRAY)

# Draw a road line
# Line start x 0, and end x 599
# Line Start y 70 and end y 70
arcade.draw_line(0, 70, 599, 70, arcade.csscolor.WHITE, 3)

# Draw 8 smaller lines
# Line Start y 105, and end y 105
# Line start x 0, and end x 50
# Rest of the lines with a 20 gap between every line
# Except the first line all of them have a 60 start x and end x between them
arcade.draw_line(0, 105, 50, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(70, 105, 130, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(150, 105, 210, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(230, 105, 290, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(310, 105, 370, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(390, 105, 450, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(470, 105, 530, 105, arcade.csscolor.WHITE, 3)
arcade.draw_line(550, 105, 599, 105, arcade.csscolor.WHITE, 3)

# Draw 8 smaller lines
# Line Start y 35, and end y 35
# Line start x 0, and end x 50
# Rest of the lines with a 20 gap between every line
# Except the first line all of them have a 60 start x and end x between them
arcade.draw_line(0, 35, 50, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(70, 35, 130, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(150, 35, 210, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(230, 35, 290, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(310, 35, 370, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(390, 35, 450, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(470, 35, 530, 35, arcade.csscolor.WHITE, 3)
arcade.draw_line(550, 35, 599, 35, arcade.csscolor.WHITE, 3)

# Draw a apartment building
# Draw a rectangle
# Center of 155, 300
# Width of 220 and height of 350
arcade.draw_rectangle_filled(155, 300, 220, 350, arcade.csscolor.DIM_GRAY)

# Draw windows
# Draw a rectangle
# Center of 80, 430 and for each window there's a 50 gap between them
# Width of 30, and height of 30
arcade.draw_rectangle_filled(80, 430, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(80, 380, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(80, 330, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(80, 280, 30, 30, arcade.csscolor.WHITE)

# Draw windows
# Draw a rectangle
# Center of 130, 430 and for each window there's a 50 gap between them
# Width of 30, and height of 30
arcade.draw_rectangle_filled(130, 430, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(130, 380, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(130, 330, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(130, 280, 30, 30, arcade.csscolor.WHITE)

# Draw windows
# Draw a rectangle
# Center of 180, 430 and for each window there's a 50 gap between them
# Width of 30, and height of 30
arcade.draw_rectangle_filled(180, 430, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(180, 380, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(180, 330, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(180, 280, 30, 30, arcade.csscolor.WHITE)

# Draw windows
# Draw a rectangle
# Center of 230, 430 and for each window there's a 50 gap between them
# Width of 30, and height of 30
arcade.draw_rectangle_filled(230, 430, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(230, 380, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(230, 330, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(230, 280, 30, 30, arcade.csscolor.WHITE)

# Draw a door
# Rectangle center of 160, 160
# Width of 50, and height of 70
arcade.draw_rectangle_filled(160, 160, 50, 70, arcade.csscolor.WHITE)

# Draw a house
# Rectangle center of 500, 200
# Width of 120, and height of 130
arcade.draw_rectangle_filled(500, 200, 120, 130, arcade.csscolor.DIM_GRAY)

# Draw a roof for the house
# Triangle is made of these three points:
# (440, 265), (560, 265), (500, 300)
arcade.draw_triangle_filled(440, 265, 560, 265, 500, 300, arcade.csscolor.DARK_RED)

# Draw two windows
# Window 1 Center of 470, 220
# Window 2 center of 530, 220
# Width of 30, and height of 30
arcade.draw_rectangle_filled(470, 220, 30, 30, arcade.csscolor.WHITE)
arcade.draw_rectangle_filled(530, 220, 30, 30, arcade.csscolor.WHITE)

# Draw a circle window
# Circle Center of 500, 280
# Size of 10
arcade.draw_circle_filled(500, 280, 10, arcade.csscolor.WHITE)

# Draw a Door
# Rectangle center of 500, 155
# Width of 30 and height of 40
arcade.draw_rectangle_filled(500, 155, 30, 40, arcade.csscolor.WHITE)

# Draw a tree with polygon as top
# Rectangle center of 300, 180
# width of 30 and height of 100
arcade.draw_rectangle_filled(300, 180, 30, 100, arcade.csscolor.SIENNA)
# Polygon with a list of points
arcade.draw_polygon_filled(((300, 300),
                            (280, 260),
                            (270, 220),
                            (330, 220),
                            (320, 260),
                            ),
                           arcade.csscolor.DARK_GREEN)

# Another tree with a trunk and circle for top
# Rectangle center of 380, 180. Width of 30 and height of 100
arcade.draw_rectangle_filled(380, 180, 30, 100, arcade.csscolor.SIENNA)
# Circle center of 380 and height of 250. Size of 50
arcade.draw_circle_filled(380, 250, 50, arcade.csscolor.DARK_GREEN)

# Draw a cloud
# Circle center of 100, 500. Size of 40
arcade.draw_circle_filled(100, 550, 40, arcade.csscolor.WHITE)
# Circle center of 140, 550. Size 50
arcade.draw_circle_filled(140, 550, 50, arcade.csscolor.WHITE)
# Circle center of 180, 540. Size of 40
arcade.draw_circle_filled(180, 540, 40, arcade.csscolor.WHITE)
# Circle center of 170, 580. Size 30
arcade.draw_circle_filled(170, 580, 30, arcade.csscolor.WHITE)

# Draw a sun
# Circle center of 580, 580. Size 40
arcade.draw_circle_filled(580, 580, 40, arcade.color.UROBILIN)

# Sun rays
arcade.draw_line(590, 590, 480, 590, arcade.color.UROBILIN, 3)
arcade.draw_line(590, 590, 590, 490, arcade.color.UROBILIN, 3)
arcade.draw_line(580, 580, 500, 560, arcade.color.UROBILIN, 3)
arcade.draw_line(580, 580, 560, 500, arcade.color.UROBILIN, 3)
arcade.draw_line(590, 590, 500, 500, arcade.color.UROBILIN, 3)

# Finish Drawing
arcade.finish_render()

# Keep the window up until someone closes it
arcade.run()
