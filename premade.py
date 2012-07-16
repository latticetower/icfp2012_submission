def check_premade(level):

	contest1 = 	"""######
#. *R#
#  \\.#
#\\ * #
L  .\\#
######
"""

	contest2 =  """#######
#..***#
#..\\\\\\#
#...**#
#.*.*\\#
LR....#
#######
"""

	contest3 =  """########
#..R...#
#..*...#
#..#...#
#.\\.\\..L
####**.#
#\\.....#
#\\..* .#
########
"""

	contest4 =  """#########
#.*..#\\.#
#.\\..#\\.L
#.R .##.#
#.\\  ...#
#..\\  ..#
#...\\  ##
#....\\ \\#
#########
"""

	contest5 =  """############
#..........#
#.....*....#
#..\\\\\\\\\\\\..#
#.     ....#
#..\\\\\\\\\\\\\\.#
#..\\..    .#
#..\\.. ....#
#..... ..* #
#..### ### #
#...R#\\#\\\\.#
######L#####
"""

	contest6 =  """###############
#\\\\\\.......** #
#\\\\#.#####...##
#\\\\#.....*##. #
#\\#####\\...## #
#\\......####* #
#\\.######* #.\\#
#\\.#. *...##.##
#\\##. ..  *...#
#\\...... L#.#.#
###########.#.#
#\\..........#.#
##.##########.#
#R.#\\.........#
###############
"""

	contest7 =  """    #######
    ##    *#
     ##R  *##
      ##\\\\\\\\##
       ##....##
      ##..\\ . ##
     ## . L .  ##
    ##\\\\\\# #\\\\\\\\##
   ######   #######
"""

	contest8 =  """##############
#\\\\... ......#
###.#. ...*..#
  #.#. ... ..#
### #.   \\ ..#
#. .#..... **#######
#.#\\#..... ..\\\\\\*. #
#*\\\\#.###. ####\\\\\\ #
#\\\\.#.     ...## \\ #
#\\#.#..... ....# \\ #  
###.#..... ....#   ##
#\\\\.#..... ....#\\   # 
########.. ..###*####
#......... .........#
#......... ....***..#
#..\\\\\\\\\\ # ####.....#
#........*R..\\\\\\   .#
##########L##########
"""

	contest9 =  """        #L#######
        #*** \\\\ #
        #\\\\\\ .. #
#########.##    ##########
#.......\\ ..........*   .#
#*******\\......#....#\\\\ .#
###\\.\\\\\\...**..#....... *#
#*****\\\\  .\\\\..##     #\\.#
######### ....  ##########
        #       #
        ####*####      
        #.......#
#########  \\\\\\\\*##########
#*\\\\  **#     *..*\\ \\\\\\\\\\#
#.\\**\\*** .....**.# \\\\##\\#
#\\R......     .\\\\.. \\\\\\\\\\#
##########################
"""

	contest10 =  """#############################
#..........................\\#
#..\\\\###...#....        ###.#
#..\\*\\\\\\.. #.... ..##\\\\..\\#.#
#..\\*\\.... #.... ..#\\#....#.#
#...\\###.. #.... ....#....#.#
#... ..... ..... .####......#
#\\\\. #....           .......#
#... #..#. .....*\\ ##.......#
#.#....... ...#..  ....######
#. ...#... ...#.\\  ....#..* #
##........ ...#.. #....#.#\\\\#
#.....*... .....*\\#\\\\.....*.#
#.***.* .......*\\****.....#.#
#.\\\\\\.. ................   .#
#.#####    .######    ##### #
#....\\\\.................... #
#....****...#.##.....\\\\\\\\..\\#
#....\\\\\\\\...#.........*....\\#
#....\\\\\\\\...#.\\\\.    #\\###.\\#
#....     ..#.... ...#\\\\\\\\. #
#........ ..#.... ...#..... #
#........         ........#R#
###########################L#
"""

	flood1 = """###########
#....R....#
#.*******.#
#.\\\\\\\\\\\\\\.#
#.       .#
#..*\\\\\\*..#
#.#*\\\\\\*#.#
#########L#

Water 1
Flooding 8 
Waterproof 5
"""

	flood2 = """#######
#..***#
#..\\\\\\#
#...**#
#.*.*\\#
LR....#
#######

Flooding 5
Waterproof 3
"""

	flood3 = """############
#..........#
#.....*....#
#..\\\\\\\\\\\\..#
#.     ....#
#..\\\\\\\\\\\\\\.#
#..\\..    .#
#..\\.. ....#
#..... ..* #
#..### ### #
#...R#\\#\\\\.#
######L#####

Waterproof 10 
Flooding 10
Water 2
"""

	flood4 = """########################
#.....................\\#
#......*\\   ...........#
#......*... ......* ...#
#..   \\\\... .*..... ...#
#.. ....... ....... ...#
#.. ....... .\\\\.... ...#   ######
#.  ....      .....\\...#   #\\\\\\\\#
#\\\\\\......... .........#   #....#
###########     R      ########*#####
          #.......... ........***\\\\\\#
          #.......... ............**#
          #.......... ......... *.*\\#
          #....\\\\.... ....\\\\..... ..L
          #.....................****#
          #........\\*...............#
          #...........     .........#
          #.........................#
          ###########################

Water 1
Flooding 20
Waterproof 10
"""

	flood5 = """#########
#.*..#\\.#
#.\\..#\\.L
#.R .##.#
#.\\  ...#
#..\\  ..#
#...\\  ##
#....\\ \\#
#########

Water 2
Flooding 11
Waterproof 5
"""

	trampoline1 = """############
#..*.R..*..#
#..A....B..######
#....2.. ..#\\\\\\C#
#......* *.#\\\\\\1#
########L########

Trampoline A targets 1
Trampoline B targets 1
Trampoline C targets 2
"""

	trampoline2 = """     ######
     #....#
     #.**.#
     #.**.#
     #.**.#
######.\\\\.######
#**....*.......#
#\\\\....L\\\\\\....#
#A......*****..#
######R.....###########
     ###.....*.....\\\\\\#
       #\\\\\\\\#..1...\\\\\\#
       #\\\\\\\\#......\\\\\\#
       ################

Trampoline A targets 1
"""

	trampoline3= """#######################################
#****................#..1...\\\\\\\\\\\\\\B..#
#R.......##############################
#.. ..................................#
#.. ........       \\            ......#
#.. .*. ....**.*...#....... ..........#
#.. ... ....\\\\\\\\...#.A..... ..........#
#.. ... ....\\ .....#.......    *  \\\\..#
#.. ... ....\\......#....... ..........#
#.. ... ....\\......#....... ..........#
#.. ... ...........#................**#
#..\\\\\\\\\\...........#................\\\\#
########### ############## ############
#...*.................................#
#....*..................        ......#
#... .*....*.............. ..... .....#
#....*2*........########.. ..... .....L
#...*...*.......#\\\\\\#..... ...*.......#
#.....\\\\\\.......#\\\\\\#....**..***......#
#....    .......#\\\\\\#*................#
#...............#\\\\\\#*...**...*.......#
#...............#.....................#
######       ############## ### #######
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#######################################

Trampoline A targets 1
Trampoline B targets 2
"""

	horock1 = """horock1

#####L######
#....R....A#
#..........#
#\\.  #@\\ ..#
#\\...#*  ###
#\\.........#
#\\..*.@....#
####@@.  ..#
#....#.. ###
#....#..**.#
#.1..#  .\\\\#
############

Trampoline A targets 1
"""

	horock2 = """#################
#A       .@@@@@@#
#  ..    #*...*1#
#  .##########*##
#  ..@   \\\\\\\\#* #
#  ..#   #####*.#
#   .#####    * #
#LR .......   . #
#################

Trampoline A targets 1
Flooding 10
Water 0
"""

	horock3 = """#################
# \\\\\\\\#   *  *  #
#  ##   !!#..@. ####
#*    @...####.....#
#\\\\   \\@...........#
#\\  # .\\@    #  #.########
#\\  # ..\\@   #   ..      #
#\\  # .. \\@  #   ..      #
#\\  # *.. \\@    #######  #
#\\  # ###  \\@   #     #W #
### #       \\@  #     ##L#
#...#@@**@@**\\@ #
#R ..........!\\##
#################

Growth 25
"""

	beard1 = """##########
#**  \\\\\\\\#
#.R..    #
# \\  ..*\\#
#!   ..*!#
####   # #
#\\\\... # L
#\\\\.W... #
#\\\\.     #
##########

Growth 15
Razors 0
"""

	beard2 = """##############################
#R...........................#
#.........................W..#
#..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\..#
#............................#
#..*****.*\\...*...*...*****..#
#..*\\....*\\....*\\*..*.\\\\*\\\\..#
#..*\\....****..!*!......*....#
#..*\\....*\\....*\\*..*...*....#
#..*\\....*\\...*...*.....*....#
#............................#
#..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\..#
#................ ..... .....#
#................      W....L#
##############################

Growth 25
Razors 10
Flooding 20
"""

	beard3 = """        ################
        #*****#!!  1   #
        #..\\..#        #
#########\\\\\\\\ # .\\\\\\.  #
#.............# *      #
#.. .\\\\\\#..!..#\\**     #
#.. LW\\\\#W  ..##### ####
#..R\\\\\\\\#.. ..*\\*\\*W...#
#.......A.. ...\\.\\...\\\\#
#..........     **     #
############....\\.######
           #.....!#
           ########

Growth 10
Trampoline A targets 1
"""

	beard4 = """####################
#W\\\\!#\\\\\\**.\\#W\\\\\\W#
##*######..###..\\\\\\#
#.......\\.R ###...\\#
#####.###.#.......##
#.......#.#\\####.###
#\\\\##\\###\\#\\\\#...#.L
#\\##\\.###.####.#.#.#
#\\W#####.....###.W.#
####\\\\...\\\\\\...#.#.#
#W*######.######.#.#
#\\\\\\\\\\\\\\\\\\.........#
############\\###\\###
#\\\\.. *..........\\\\#
#W... #.........##W#
####################
"""

	beard5 = """           ##########
        ####..******####
      ###..  3ABCDEF...###
      ##                 ## 
     ###                  ##
    ###.....\\\\\\...\\\\\\.....###
    #..     \\\\\\ * \\\\\\      ##
    ##          *          ##
     ###       ***        ##
       #*****************##
       ###..............##
         ###...........##
           ####WR..W####
              ##L####
               .....
           ######  ######
          ##1\\! G##2 !\\H##
           ######  ######

Trampoline A targets 1
Trampoline B targets 1
Trampoline C targets 1
Trampoline D targets 1
Trampoline E targets 1
Trampoline F targets 1
Trampoline G targets 2
Trampoline H targets 3
Growth 5
Razors 0
"""
	
	if level == contest1:
		return 'LDRDDUULLLDDL'
	elif level == contest2:
		return 'RRUDRRULURULLLLDDDL'
	elif level == contest3:
		return 'LDDDRRRRDDLLLLLDURRRUURRR'
	elif level == contest4:
		return 'DUURDDDRDRDRRLUURUUULUDRR'
	elif level == contest5:
		return 'LLUURUUURUULRRRRRDDRRDDDDDLLRRUUUUULLLLLRDDDDDD'
	elif level == contest6:
		return 'RUULRRRRRRRRRRUUURRDDDDDLLLLLLLLLRRRRRRRRRUUUUULUURUUULULLULLLLLLDDRRRDULLLUULLLDRDLDDDDDDRRRRRRRR'
	elif level == contest7:
		return 'RDRRRDDDRDRRRLLLULULLDLDLLRRURR'
	elif level == contest8:
		return 'UURLLWWWWWWWRDDRRRRRURRLUULWRUURUUUULLULLLLLLUULLLLUUULLLLRRDDDDDDLDRDDDLLRRUUUULLDDUURRUUUUUURRDDDDDDDDDDRRRDDDDLLLLLDRRRRRRRD'
	elif level == contest9:
		return 'RLLURURRRDLDRRRRRRRRRRRRRULURRRRDDRRRRUULLLDLLULLLLLULLULDURUUUULLLLLULLRDUULDLLRRURRRURRRRRRRRRRRDDRRRRDUULLULLLLLLUUULLLLDLLRULU'
	elif level == contest10:
		return 'UUUUUUUULLUUDDRRUULURDLLLLLLLLRRDDLLLLLURUUULURUUUURRRUDLLUUURRRDRRRRLLUURRRRLLLLLLLLLLLLLLLLLLLDDLLLDRULLULDDDRLDDLLRRDDDDDLLDDRRRRRRDDLLLDDDRRRRULLLRRURRRRURRDDDRRRRRRRURURRRDLLDDRRRRRDDD'

	elif level == flood1:
		return 'LLLLDDRRLDRRDRRDLLUUURRRRRDDDD'
	elif level == flood2:
		return 'RRUDRRULURULLLDDLDL'
	elif level == flood3:
		return 'LLUURUUURUULRRRRRDDRRDDDDDLLRRUUUUULLLLLRDDDDDD'
	elif level == flood4:
		return 'RRRUUURRRUUUUULLLLLLLLLLLLLLDDRDLLLLLLLDDLDDRRRRRRRRRRRRUURDDDDDDDRRRRRDDURRRRRRRURRRRRDDDRRURWLUUUDRRULLULLRUWLUUULLLRRRDDDRRRRDDDR'
	elif level == flood5:
		return 'DUURDDDDRRDRRLUUURUULURDR'

	elif level == trampoline1:
		return 'RRLDDRRRUULDLLLURRRRRRDD'
	elif level == trampoline2:
		return 'ULLLLULDRRRRURRDLDRLLLLLLLLURULLLDDLULDLUURURRLUULLUULLDRD'
	elif level == trampoline3:
		return 'RRRRDDLDDDDDDDLRRRRRRRRDDDLLDDLRUURRUUUURUUUURRRRRRUURRRDDRRRRRRRRRRRRRLDDRLLDDDDDLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRLLLLLLLLLLUULLLLLLLLUUUULLDRDLDRRDRRRRUUUURRUUURUUURRRRRRRRRRRLUUUULLDDDLDLLLLLLLDDDDDRRRRRRRRRRRR'

	elif level == horock1:
		return 'RRDDRDLDDDLRLDRDDRRRULLUUUUUURRUUURRULDWRLURURRDUULLLLLUUUUURRRRU'
	elif level == horock2:
		return 'RRRRRRRRRRRRLLLLLLLLLLUUURRDURRRRRRLLLLLLLLLUUULLLRLLLLRLRRLLULLLLLLLLLLDDDDDD'
	elif level == horock3:
		return 'RRRRRRRRRRRRRLULULULULULULULURUURRDDRRRRRUUULLDRRRDDRRDDRRRRRRSDSDSULLLLLLLLLDDDDDLULLLDLULLLDLLLUUULLUUUUURUUURRRDDDDRDRDRRRRRDRRRURRRRRRRRRDDD'

	elif level == beard1:
		return 'RRRURRRDDDUULLLLLDLRRDDDLLLDDRURSRRRRRUR'
	elif level == beard2:		
		return 'DDRRRRRRRRRDDDRUUURRRRRRRRRRRRRRRRDDDLLRDDLDRDDLLLLLLLLLUULURDDDLLLLLLLLLLLLLLURUUUUWLDDWRRRRDDRRRUURRRURRRUDRRRRRURRLDDRRRRRRDDDDD'
	elif level == beard3:		
		return 'RRRRDRLLLLDDDDURRRRDUULLRRDDSDSDDRRRLLLLLUDLLRLDDDRRULLUULRULLUUUUULLRDLLLDLLDDLULLD'
	elif level == beard4:		
		return 'RDDDRLUUULLDDDDDDLLLLLRRRRRRRLLDDRRRDDLLLLLLLLLLLRRRRRRRRRRRUULLLLLLLLLLLRRRRRRRRUUUUUUUUURWLURRRLLLLLLRRRDDLLLLDDDDLRUULLLDLDDUURURRRUULLLLRUURRLLDDRRRRRRRRRDRRRRUUURRDLRRDLLDDDDDDDDDDRRLLUURRUUUUUR'
	elif level == beard5:		
		return 'SRRSURRULWRUULLULLLLULLURRUUURRRRRRRRDRRRRRRRDDRDLLRDDRLLLUUURDLDLRRDDDDLLLDD'
	return '' 