import canvas
import speech as sp
from time import sleep

sleepfor = 0.1

canvas.set_size(1000,600)
canvas.draw_image('_Image_3', 0, 0, 1000, 600) 



for i in range(4):
  canvas.draw_image('Fisted_Hand', 10, 150*i)
  sleep(sleepfor)


for i in range(5):
  canvas.draw_image('Fear_2', 140*i+150, 450)
  sleep(sleepfor)


for i in reversed(range(4)):
  canvas.draw_image('Raised_Fist', 850, 150*i)
  sleep(sleepfor)


for i in reversed(range(5)):
  canvas.draw_image('Fear_1', 140*i+150, 0)
  sleep(sleepfor)


canvas.set_fill_color(0.40, 0.80, 1.00 )
text = "Happy fathers day!"
size = 110
fnt = 'Avenir-LightOblique'
canvas.draw_text(text, 150, 200, fnt, size)
sp.say(text, 'en-US', 0.2)
