# I used many emojis to get the program more user friendly like in lines 5 and 10 and 52 and 82
# Also if read all the text you'll find plenty of creativity

print(' ')
print('▁▂▃▄▅▆▇█ 𝙇𝙤𝙖𝙙𝙞𝙣𝙜…')
start = input("Type: 'Hello' to start... ")
print(' ')

if start.lower() == 'hello':
    print('✯ ≫ ∘ ❀  Welcome User ❀ ∘ ≪ ✯')
else:
    print('See you latter ( ͡❛ ͜ʖ ͡❛)')
print('')

first_task = str(input('You were in a private jet with your friends, but the airplane felt in the Saara Desert. '\
                       '\nYou woke up in the middle of the plane wreckage and you find your backpack with a few things inside. '\
                        '\nThe first two things you look at are a MAP and a CELLPHONE. '\
                        '\nWhich do you pick first? '))
if first_task.lower() == 'cellphone':
    print('')
    choice_one = input('The phone is dead. You look around, you can only see sand and dust everywhere.'\
                       '\nThen you hear from close range a voice yelling “Help” you go CHECK or IGNORE? ')
    if choice_one.lower() == 'check':
        print('')
        check = str(input("You find a man. It's the pilot. He is verry injured."\
                           '\nYou know that if you help him, you probably will slow down to find a place to stay,'\
                            '\nwater and you probably end up dying of starvation or dehydration, because'\
                                '\nnow you need to worry about you and him at the same time.'\
                                    ' \nDo you LET HIM die there or HELP HIM? '))
        if check.lower() == 'help him':
            print('')
            print('You decided to help him. After four days walking for long miles without water and food, '\
                  "\nyou become insane. The pilot die after 2 days. You feel guilty because you couldn't help him anyway."\
                    '\nYou pass out, thinking about all the tragedy you experienced...')
            print(' ')
            print('GAME OVER 💀')
        elif check.lower() == 'let him':
            print('')
            print('\nYou felt so guilty letting him die, that you become depressed and could move forward.'\
                  '\nYou get even sad and just give up to try to get out of this situation...')
            print(' ')
            print('GAME OVER 💀')
    elif choice_one.lower() == 'ignore':
        print('')
        ignore = str(input('You ignored him and you followed your path. You check your bag after a few miles.'\
                         '\nYou see again a map and also a compass. Do you get the MAP or the COMPASS? '))
        if ignore.lower() == 'compass':
            print('')
            print('Now you can locate yourself. After walking north for two days and a half, you finally find a city called'\
              '\nTimimoun. There you find water, a place to stay and you can charge your phone to ask for help. You survived.')
            print(' ')
            print('CONGRATULATIONS, GAME OVER, YOU SURVIVED ° ᗜ °')
        elif ignore.lower() == 'map':
            print('')
            map = str(input('Looking at the map you realize that you are close to a small city or province nearby called Gardaia.'\
                                '\nYou decide to go to this city in Argelia. So, you assume you are close to Argelia and maybe you can talk to someone.'\
                                '\nDo you decide to FOLLOW the map or LOOK at the plane wreckage for supplies? '))
            if map.lower() == 'follow':
                print('')
                follow = str(input('You walk for two days trying to find the city. You failed. You look again at your bag. You find a water '\
                      '\nbottle with 1 liter of water. You also find a switchblade. \nYou will find a SATELLITE PHONE with battery'\
                        '\nand COMPASS. Which do you choose? '))
                if follow.lower() == 'compass':
                    print('')
                    compass = str(input('Now you can locate yourself. After walking north for two days and a half, you finally find a city called'\
                          '\nTimimoun. There you find water, a place to stay and you can charge your phone to ask for help.'\
                            '\nYou survived. '))
                    print('')
                    print('CONGRATULATIONS. YOU SURVIVED. GAME OVER ° ᗜ °')
                elif follow.lower() == 'satellite phone':
                        print('')
                        satellite1 = str(input('You can make a call to the nearest police department, but they can only speak Algerian Arabic, you can'\
                                         '\ntalk to them very well. The connection fails. You are completely lost. n\You look at the horizon and see a'\
                                            '\nsandstorm approaching. Do you RUN or HIDE behind a big rock? '))
                        if satellite1.lower() == 'run':
                            print('')
                            print('You try your best. But you become disoriented by the sand and fall into a hole and break your leg. Your'\
                            "\npain is so intense that you can't even move. You pass out and only wake up in the hospital in Argelia."\
                            '\nYou are glad that you survived the accident. But you were just dreaming the federal government found'\
                                '\nyour body with the black box from the airplane, so you were very lucky not a hero. ')
                            print('')
                            print('GAME OVER, SORRY CHAMP (ᗒ ᗣ ᗕ)')
                        else:
                            if satellite1.lower() == 'hide':
                                print('')
                                print('The storm gets you. You wait and wait. The storm takes a long time to pass. You decide to move. You'\
                                '\nwalk disoriented by the sand and fall into a hole and break your leg. Your pain is so intense that you'\
                                "\ncan't even move. You pass out and only wake up in the hospital in Argelia. You are glad that you survived"\
                                    '\nthe accident. But you were just dreaming the federal government found your body with the black box'\
                                        '\nfrom the airplane, so you were very lucky not a hero.')
                                print('')
                                print('GAME OVER, SORRY CHAMP (ᗒ ᗣ ᗕ)')
            elif map.lower() == 'look':
                print('')
                print('Looking at the plane wreckage for supplies you find a Cerastes Cerastes a venomous snake native to the '\
                        "\ndeserts and semi-deserts of Northern Africa and the Middle East. It's not your lucky day. You got bitten "\
                        '\nby the snake and you got dizzy, you fell on the ground and there you stay...')
                print('')
                print('GAME OVER 💀')
else:
    if first_task.lower() == 'map':
            print('')
            choice_nine = str(input('Looking at the map you realize that you are close to a small city or province nearby called Gardaia.'\
                                '\nYou decide to go to this city in Argelia. So, you assume you are close to Argelia and maybe you can talk to someone.'\
                                '\nDo you decide to FOLLOW the map or LOOK at the plane wreckage for supplies? '))
            if choice_nine.lower() == 'follow':
                    print('')
                    choice_nine = str(input('You walk for two days trying to find the city. You failed. You look again at your bag. You find a water '\
                      '\nbottle with 1 liter of water. You also find a switchblade. \nYou will find a SATELLITE PHONE with battery'\
                        ' and COMPASS. Which do you choose? '))
                    if choice_nine.lower() == 'compass':
                        print('')
                        choice_ten = print('Now you can locate yourself. After walking north for two days and a half, you finally find a city called '\
                          '\nTimimoun. There you find water, a place to stay and you can charge your phone to ask for help.'\
                            '\nYou survived. ')
                        print('')
                        print('CONGRATULATIONS. YOU SURVIVED. GAME OVER ° ᗜ °')
                    else:
                        if choice_nine.lower() == 'satellite phone':
                            print('')
                            satellite = str(input('You can make a call to the nearest police department, but they can only speak Algerian Arabic, you can'\
                                         '\ntalk to them very well. The connection fails. You are completely lost. n\You look at the horizon and see a'\
                                            '\nsandstorm approaching. Do you RUN or HIDE behind a big rock? '))
                            if satellite.lower() == 'run':
                                print('')
                                print('You try your best. But you become disoriented by the sand and fall into a hole and break your leg. Your'\
                                "\npain is so intense that you can't even move. You pass out and only wake up in the hospital in Argelia."\
                                '\nYou are glad that you survived the accident. But you were just dreaming the federal government found'\
                                '\nyour body with the black box from the airplane, so you were very lucky not a hero. ')
                                print('')
                                print('GAME OVER, SORRY CHAMP (ᗒ ᗣ ᗕ)')
                            elif satellite.lower() == 'hide':
                                    print('')
                                    print('The storm gets you. You wait and wait. The storm takes a long time to pass. You decide to move. You'\
                                    '\nwalk disoriented by the sand and fall into a hole and break your leg. Your pain is so intense that you'\
                                    "\ncan't even move. You pass out and only wake up in the hospital in Argelia. You are glad that you survived"\
                                    '\nthe accident. But you were just dreaming the federal government found your body with the black box'\
                                        '\nfrom the airplane, so you were very lucky not a hero.')
                            print('')
                            print('GAME OVER, SORRY CHAMP (ᗒ ᗣ ᗕ)')
            elif choice_nine.lower() == 'look':
                print('')
                print('Looking at the plane wreckage for supplies you find a Cerastes Cerastes a venomous snake native to the '\
                        "\ndeserts and semi-deserts of Northern Africa and the Middle East. It's not your lucky day. You got bitten "\
                        '\nby the snake and you got dizzy, you fell on the ground and there you stay...')
                print('')
                print('GAME OVER 💀')