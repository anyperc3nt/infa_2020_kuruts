FPS = 60
FPSscale=FPS/60

#mouse settings (grad per pixel)
mouse_sensivity=1

#screen settings
Xscreensize=800
Yscreensize=800

#model settings
Xmodelsize=800
Ymodelsize=800
scale=Xscreensize/Xmodelsize
scale=1

#настроки физики
player_r=23 #радиус игрока
atime=16 # время разгона в кадрах
playervelmax=19


k0=0.1 #коэффициент вязкого трения при pow=1 k0=0.04 примерно нормальный 
pow=0.7

#настройки врагов
enemyvmax=13

#graphics settings
motionblur_force=225 #от 0 до 255
motionblur_brightness=190 #от 0 до 255
motionblur_blurforce=10 #красивые результаты от 7 до 17 примерно

#скейл констант по фпсу. ничего не менять, они нужны чтобы константы менялись так, чтобы при изменении фпс физика не менялась
#не до конца доработано, но вообще, кому нужно менять фпс?
atime*=FPSscale
playervelmax/=FPSscale
k0/=FPSscale
motionblur_force=int( (motionblur_force/255)**(1/FPSscale)*255 )