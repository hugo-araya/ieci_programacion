import arcade
 
Width = 500
Height = 700
Title = "Welcome to Arcade"
Radius = 100
 
arcade.open_window(Width, Height, Title)
 
arcade.set_background_color(arcade.color.BLUE)
 
arcade.start_render()
 
arcade.draw_circle_filled(
    Width/2 , Height/2 , Radius , arcade.color.PINK
)
arcade.finish_render()
 
arcade.run()