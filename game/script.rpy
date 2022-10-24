init:
    $ import time

define c = Character("Carley")
define c_unknown = Character("???")
image carley happy = "Carley/Carley_Happy.png"
image carley neutral = "Carley/Carley_Neutral.png"
image carley sad = "Carley/Carley_Sad.png"

# <a href="https://www.freepik.com/free-vector/futuristic-technological-wallpaper_10987662.htm#query=futuristic&position=9&from_view=search&track=sph">Image by coolvector</a> on Freepik
image bg = "bg.jpg"

define persistent.user_name = ""
default temp_name = ""

define slideleft = CropMove(1.0, "slideleft")
transform halfsize:
    yalign 0.2
    zoom 0.75

label start:
    scene bg
    with Pause(1)

    play sound "audio/start.wav"

    show text "Connecting..." at truecenter with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    if not persistent.user_name:
        call new_user
    else: 
        call old_user

    while True:
        show carley happy at center, halfsize

        menu: 
            c "How can I help you?"

            "What's the current time?":
                call show_time
            
            "I want to sleep...":
                jump close_program

    return

label new_user:
    show carley neutral at center, halfsize

    c_unknown "Welcome to your virtual space"
    c_unknown "I'm your virtual assistant, Carley"

    c "We haven't met before"
    c "May I know your name?"

    $ temp_name = renpy.input ("You can call me", length=12)
    $ temp_name = temp_name.strip()
    $ persistent.user_name = temp_name

    hide carley neutral
    show carley happy at center, halfsize

    c "I see, welcome [persistent.user_name]"

    hide carley happy

    return

label old_user: 
    show carley happy at center, halfsize

    c "Welcome back, [persistent.user_name]"

    hide carley happy

    return

label show_time: 
    scene bg
    show carley neutral at center, halfsize

    $ current_time = time.asctime(time.localtime())

    c "Currently it's [current_time]"

    hide carley neutral

    return

label close_program:
    show carley sad at center, halfsize

    c "See you next time, [persistent.user_name]"

    return