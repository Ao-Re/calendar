init:
    $ import time
    $ from datetime import datetime

define c = Character("Carley")
define c_unknown = Character("???")
image carley happy = "Carley/Carley_Happy.png"
image carley neutral = "Carley/Carley_Neutral.png"
image carley sad = "Carley/Carley_Sad.png"

# <a href="https://www.freepik.com/free-vector/futuristic-technological-wallpaper_10987662.htm#query=futuristic&position=9&from_view=search&track=sph">Image by coolvector</a> on Freepik
image bg = "bg.jpg"

define persistent.user_name = ""
default temp_name = ""

transform halfsize:
    yalign 0.2
    zoom 0.75

transform headleft:
    linear 0.09 xalign -12.0

transform headcenter:
    linear 0.09 xalign 0.0

label start:
    scene bg
    with Pause(1)

    $ renpy.sound.play(filename="audio/start.wav", relative_volume=0.2)

    show text "Connecting..." at truecenter with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    if not persistent.user_name:
        call new_user
    else: 
        call old_user

    while True:
        show carley neutral at headleft, halfsize

        menu: 
            c "How can I help you?"

            "Tell me a joke":
                show carley sad at headcenter, halfsize
                "I'm sorry, I still haven't learned to create a joke.."
                show carley happy at center, halfsize
                "Maybe next time?"

            "I need to change my name":
                call change_name

            "What's the current time?":
                call show_time
            
            "Set a schedule":
                call set_schedule
            
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

    show carley happy at center, halfsize

    c "I see, welcome [persistent.user_name]"

    return

label old_user: 
    show carley happy at center, halfsize

    c "Welcome back, [persistent.user_name]"

    return

label change_name: 
    show carley neutral at headcenter, halfsize

    c "What should I call you?"

    $ temp_name = renpy.input ("You can call me", length=12)
    $ temp_name = temp_name.strip()
    $ persistent.user_name = temp_name
    
    show carley happy at center, halfsize

    c "I will call you [persistent.user_name] from now"

    return

label show_time: 
    show carley neutral at headcenter, halfsize

    $ current_time = time.asctime(time.localtime())

    c "Currently it's [current_time]"

    return

label set_schedule:
    show carley neutral at headcenter, halfsize

    c "Okay, let's set up a schedule"

    $ date = renpy.input ("Date (1-31)", length=2)
    $ month = renpy.input ("Month (1-12)", length=2)
    $ start_time = renpy.input ("Start time (hh:mm)", length=5)
    $ end_time = renpy.input ("End time (hh:mm)", length=5)
    $ sched_st = datetime.strptime("{date} {month} 2022 {start_time}".format(date=date, month=month, start_time=start_time), '%d %m %Y %H:%M')
    $ sched_ed = datetime.strptime("{date} {month} 2022 {end_time}".format(date=date, month=month, end_time=end_time), '%d %m %Y %H:%M')
    $ note = renpy.input ("Note", length=20)

    show carley happy at center, halfsize

    c "So you want to make a schedule from [sched_st] till [sched_ed] with the following notes: [note]"

    return


label close_program:
    show carley sad at headcenter, halfsize

    c "See you next time, [persistent.user_name]"

    return