import picamera
import time
import keyboard
camera = picamera.PiCamera()
xpos = 0
ypos = 0
width = 640
height = 480
terminar = False
camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
while(terminar==False):
    if(keyboard.is_pressed('q')):
       terminar = True
    if(keyboard.is_pressed('up arrow')):
        ypos-=10
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
    if(keyboard.is_pressed('down arrow')):
        ypos+=10
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
    if(keyboard.is_pressed('left arrow')):
        xpos-=10
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
    if(keyboard.is_pressed('right arrow')):
        xpos+=10
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
    if(keyboard.is_pressed('+')):
        width+=10
        height+=int(10*480/640)
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
    if(keyboard.is_pressed('-')):
        xpos-=10
        height-=int(10*480/640)
        camera.stop_preview()
        camera.start_preview(fullscreen=False,window=(xpos,ypos,width,height))
camera.stop_preview()
