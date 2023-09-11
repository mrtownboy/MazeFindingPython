from turtle import *
"""
    graph for Hampton Court Maze
    """
graph={
'A' :['B','C'],
'B' :['A'],
'C' :['A','D'],
'D' :['C','E'],
'E' :['D','F'],
'F' :['E','G'],
'G' :['F','H'],
'H' :['G','I'],
'I' :['H','J'],
'J' :['I','K'],
'K' :['J','L'],
'L' :['K','M'],
'M' :['L','N','R'],
'N' :['M','O'],
'O' :['N','P'],
'P' :['O','Q'],
'Q' :['P'],
'R' :['M','S','JB'],
'S' :['R','T'],
'T' :['S','U'],
'U' :['T','V'],
'V' :['U','W'],
'W' :['V','X'],
'X' :['W','Y'],
'Y' :['X','Z'],
'Z' :['Y','AA'],
'AA':['Z','BA'],
'BA':['AA','CA'],
'CA':['BA','DA','FA'],
'DA':['CA','EA'],
'EA':['DA','HB'],
'FA':['CA','GA'],
'GA':['FA','HA'],
'HA':['GA','IA'],
'IA':['HA','JA'],
'JA':['IA','KA'],
'KA':['JA','LA'],
'LA':['KA','MA'],
'MA':['LA','NA'],
'NA':['MA','IB','OA'],
'OA':['NA','PA'],
'PA':['OA','QA'],
'QA':['PA','RA'],
'RA':['QA','SA'],
'SA':['RA','TA'],
'TA':['SA','JB','UA'],
'UA':['TA','VA'],
'VA':['WA','UA'],
'WA':['XA','VA'],
'XA':['WA','YA'],
'YA':['XA','ZA'],
'ZA':['YA','AB'],
'AB':['ZA','BB'],
'BB':['AB','CB','DB'],
'CB':['BB','FB'],
'DB':['EB','BB'],
'EB':['DB'],
'FB':['CB','GB'],
'GB':['ZZ','FB'],
'HB':['EA','IB'],
'IB':['HB','JB','NA'],
'JB':['R','KB'],
'KB':['JB','LB'],
'LB':['KB','MB'],
'MB':['LB','NB'],
'NB':['MB','OB'],
'OB':['NB'],
'ZZ':['GB']
}

"""
    graph for Chevening House Maze
      """

graph1= {
'A':['1'],
'1':['2','A'],
'2':['3','1'],
'3':['4','2'],
'4':['5','3'],
'5':['6','4'],
'6':['7','5'],
'7':['8','6'],
'8':['9','8'],
'9':['B','8'],
'B':['9','10','14'],
'14':['B','15'],
'15':['16','14'],
'16':['17','15'],
'17':['L','16'],
'L':['17','K','18'],
'18':['19','L'],
'19':['20','18'],
'20':['21','19'],
'21':['H','20'],
'H':['21','G','22','42'],
'G':['F','H'],
'F':['G','45'],
'45':['46','F'],
'46':['47','45'],
'47':['48','46'],
'48':['49','48'],
'49':['E','48'],
'E':['57','50','49'],
'50':['51','E'],
'51':['52','50'],
'52':['53','51'],
'53':['54','52'],
'54':['D','53'],
'D':['13','54','55'],
'13':['11','12','D'],
'12':['13','C'],
'11':['13','C'],
'C':['10','11','12'],
'10':['B','C'],
'K':['L','M','26','27'],
'27':['28','K'],
'28':['29','27'],
'29':['30','28'],
'30':['31','29'],
'31':['32','30'],
'32':['M','31'],
'M':['32','K','33'],
'33':['34','M'],
'34':['35','33'],
'35':['J','34'],
'J':['35','36','37'],
'36':['J','40'],
'37':['J','38'],
'38':['39','37'],
'39':['Z','38'],
'40':['41','36'],
'41':['I','38'],
'42':['H','I'],
'43':['44','I'],
'I':['41','42','43'],
'44':['43'],
'22':['23','H'],
'23':['22','24'],
'24':['25','23'],
'25':['24','26'],
'26':['25','K'],
'55':['D','56'],
'56':['57','55'],
'57':['56','E'],
'Z':['39']
}

"""
    graph for Own Maze
    """

graph2= {
'A':['B','C'],
'B':['A','F'],
'C':['A','D'],
'D':['C','E'],
'E':['NN'],
'F':['B','G'],
'G':['F','H'],
'H':['G','J'],
'I':['G'],
'J':['H','K'],
'K':['J','L'],
'L':['K','M','P'],
'M':['L','N'],
'N':['M','O'],
'O':['N'],
'P':['L','Q','R'],
'Q':['S','P','T'],
'R':['P'],
'S':['Q','Y'],
'Y':['S','MM'],
'T':['U','FF','Q'],
'U':['T','AA','V'],
'V':['U','W','X'],
'W':['V','X'],
'X':['V','W'],
'AA':['BB'],
'BB':['CC','EE'],
'CC':['BB','DD'],
'DD':['CC'],
'EE':['BB'],
'FF':['T','GG'],
'GG':['FF','HH'],
'HH':['GG','II'],
'II':['JJ','KK','Z'],
'JJ':['II'],
'KK':['II','LL','OO'],
'LL':['KK'],
'NN':['E'],
'MM':['Y'],
'OO':['KK'],
'Z':['II']
}

""" BFS Algorithm """

class MyQUEUE:  # Just an implementation of a queue.
    def __init__(self):
        # Initialises the queue to an empty queue.
        self.holder = []

    def enqueue(self, val):
        # Appends item val onto the end of the queue.
        self.holder.append(val)
        print('enq: ',self.holder)

    def dequeue(self):
        # Pops the head off the queue and returns it value.
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]
            print('deq: ',self.holder)
        except:
            print('deq: ',self.holder)

        return val

    def IsEmpty(self):
        # Returns True if the queue is empty.
        result = False
        if len(self.holder) == 0:
            result = True
        return result


def BFS(graph, start, end):
    # Traverses the graph using a Breadth First Search starting
    # from the start node with end being the goal node. Uses a
    # queue to store the nodes that are current leaves at the
    # fringe of the search.

    q = MyQUEUE()  # make an empty queue first
    q.enqueue([start])  # add the start node onto the queue

    while q.IsEmpty() == False:
        path = q.dequeue()
        last_node = path[len(path) - 1]
        print(path)
        if last_node == end:
            print("VALID_PATH : ", path)
        for link_node in graph[last_node]:
            if link_node not in path:
                new_path = []
                new_path = path + [link_node]
                q.enqueue(new_path)


def draw_maze_line(turtle, room_size, go_right, pen_up, segments):
    """ Draw a line in a maze in segments.

        The parameter room_size is the width of a square room
        in the maze in pixels. If go_right = 1, the line will
        be drawn to the right, otherwise to the left. If
        pen_up = 1, then the first segment will be drawn with
        the pen_up (i.e. it will be blank), then the second
        segment with the pen down and so on. If pen_up = 0,
        it will draw the first segment, and skip over the
        second and so on. The parameter segments is a list of
        numbers indicating the length in rooms for each segment.
    """

    # Skip to next line over
    turtle.up()
    if go_right:
        turtle.right(90)
        turtle.forward(1 * room_size)
        turtle.right(90)
    else:
        turtle.left(90)
        turtle.forward(1 * room_size)
        turtle.left(90)
    turtle.down()

    # Draw the line in segments
    for s in segments:
        if pen_up:
            turtle.up()
        turtle.forward(s * room_size)
        if pen_up:
            turtle.down()
        pen_up = not (pen_up)


def draw_hampton_court_maze(tracer_on, colour, room_size,
                            line_width, start_x, start_y):
    """ Draws a stylised version of the Hampton Court Maze """

    # create a turtle for drawing the maze
    turtle1 = Turtle()
    turtle1.hideturtle()
    turtle1.name = 'Hampton Court Maze Drawing Turtle'

    turtle1.reset()
    turtle1.speed('fastest')
    tracer(tracer_on)

    turtle1.color(colour)
    turtle1.width(line_width)

    # Start at bottom right, one row down pointing to the right (east)
    turtle1.up()
    turtle1.goto(start_x, start_y)
    turtle1.down()

    # Draw horizontal lines in zig zag fashion, first right to left,
    # then left to right, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [9, 1, 9])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 18])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 8, 2, 6])
    draw_maze_line(turtle1, room_size, 1, 1, [3, 3, 3, 2, 2, 2])
    draw_maze_line(turtle1, room_size, 0, 1, [5, 2, 1, 3, 4, 1, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [1, 18])
    draw_maze_line(turtle1, room_size, 0, 0, [1, 16, 1])
    draw_maze_line(turtle1, room_size, 1, 1, [5, 6, 5, 1])
    draw_maze_line(turtle1, room_size, 0, 1, [2, 2, 1, 3, 2, 5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 2, 4, 2, 4, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [4, 2, 3, 1, 2, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [19, 1])

    # Now at top right one column outside maze, re-orient pointing up (north)
    turtle1.left(90)

    # Draw Vertical lines in zig zag fashion, first top to bottom,
    # then bottom to top, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [11])
    draw_maze_line(turtle1, room_size, 1, 1, [2, 3, 2, 3])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 1, 1, 4])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 4])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 5])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 5, 3])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 1, 5])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 3, 1, 2])
    draw_maze_line(turtle1, room_size, 0, 1, [8])
    draw_maze_line(turtle1, room_size, 1, 0, [2, 5])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 3, 3])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 1, 7, 1])
    draw_maze_line(turtle1, room_size, 0, 1, [7])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 1, 2, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 1, 5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [5, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [1, 1, 2, 1, 2, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [4, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [11])

    #Apply BFS over the graph of Hampton Court Maze
    BFS(graph, 'A', 'ZZ')

    #Navigating a turtle agent for tracing path in Hampton Court Maze.
    turtle2 = Turtle()
    turtle2.penup()
    turtle2.goto(60, -140)
    turtle2.speed('fast')
    turtle2.pendown()
    turtle2.color("red")
    turtle2.width(2)
    turtle2.left(90)
    turtle2.forward(10)
    turtle2.left(90)
    turtle2.forward(180)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(140)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(80)
    turtle2.left(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(180)
    turtle2.right(90)
    turtle2.forward(80)

    update()


def draw_chevening_house_maze(tracer_on, colour, room_size, line_width, start_x, start_y):
    """ Draws a stylised version of the Hampton Court Maze """

    tracer(tracer_on)

    # create a turtle for drawing the maze
    turtle1 = Turtle()
    turtle1.hideturtle()
    turtle1.name = 'Chevening House Maze Drawing Turtle'
    turtle1.reset()
    turtle1.speed('fastest')
    turtle1.color(colour)
    turtle1.width(line_width)

    # Start at bottom right, one row down pointing to the right (east)
    turtle1.up()
    turtle1.goto(start_x, start_y)
    turtle1.down()

    # Draw horizontal lines in zig zag fashion, first right to left,
    # then left to right, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [11, 1, 11])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 9, 3, 9])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 7, 3, 9])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 9, 2, 6])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 8, 2, 5])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 3, 4, 6])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 4, 5, 2])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 2, 4, 3])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 3, 2, 2])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 2, 1, 2, 6])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 5, 1, 1, 1, 8])
    draw_maze_line(turtle1, room_size, 1, 0, [2, 10, 2, 1, 4, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [1, 2, 2, 1, 2, 5, 2, 1, 4])
    draw_maze_line(turtle1, room_size, 1, 1, [8, 3, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 1, 3, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [3, 3, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [5, 1, 5, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [6, 1, 6, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [6, 3, 6, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [8, 1, 8, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [19, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [21, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [23, 1])

    # Now at top right one column outside maze, re-orient pointing up (north)
    turtle1.left(90)

    # Draw Vertical lines in zig zag fashion, first top to bottom,
    # then bottom to top, and so on

    draw_maze_line(turtle1, room_size, 0, 0, [23])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 11, 1, 9])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 9, 1, 9])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 7, 1, 9])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 7, 3, 5])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 5, 3, 5])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 5, 1, 5])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 4, 1, 4])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 2, 3, 2])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 2, 1, 2])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 3, 6, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 2, 5, 5, 2, 1, 2])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 1, 2, 5, 6, 2, 2])
    draw_maze_line(turtle1, room_size, 1, 1, [3, 5, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 1, 2, 2, 3])
    draw_maze_line(turtle1, room_size, 1, 1, [4, 4, 1, 2, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [4, 1, 4, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [11, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [5, 2, 6, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [7, 1, 7, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [7, 3, 7, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [9, 1, 9, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [21, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [23])

    #Apply BFS over the graph of Chevening House Maze

    BFS(graph1, 'A', 'Z')

    # Navigating a turtle agent for tracing path in Chevening House Maze.
    turtle2 = Turtle()
    turtle2.penup()
    turtle2.goto(20, -230)
    turtle2.speed('fast')
    turtle2.pendown()
    turtle2.color("red")
    turtle2.width(2)
    turtle2.left(90)
    turtle2.forward(50)
    turtle2.left(90)
    turtle2.forward(180)
    turtle2.right(90)
    turtle2.forward(160)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(140)
    turtle2.left(90)
    turtle2.forward(120)
    turtle2.left(90)
    turtle2.forward(80)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.right(90)
    turtle2.forward(120)
    turtle2.right(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(160)
    turtle2.left(90)
    turtle2.forward(140)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(120)
    turtle2.right(90)
    turtle2.forward(120)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(100)
    turtle2.left(90)
    turtle2.forward(120)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(180)
    turtle2.right(90)
    turtle2.forward(180)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(200)
    turtle2.right(90)
    turtle2.forward(160)
    turtle2.right(90)
    turtle2.forward(40)
    turtle2.right(90)
    turtle2.forward(120)
    turtle2.left(90)
    turtle2.forward(120)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(100)
    turtle2.right(90)
    turtle2.forward(140)
    turtle2.right(90)
    turtle2.forward(140)

    update()

def draw_own_maze(tracer_on, colour, room_size,
                            line_width, start_x, start_y):
    """ Draws a stylised version of the Hampton Court Maze """

    # create a turtle for drawing the maze
    turtle1 = Turtle()
    turtle1.hideturtle()
    turtle1.name = 'Hampton Court Maze Drawing Turtle'

    turtle1.reset()
    turtle1.speed('fastest')
    tracer(tracer_on)

    turtle1.color(colour)
    turtle1.width(line_width)

    # Start at bottom right, one row down pointing to the right (east)
    turtle1.up()
    turtle1.goto(start_x, start_y)
    turtle1.down()

    # Draw horizontal lines in zig zag fashion, first right to left,
    # then left to right, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [9, 1, 9])
    draw_maze_line(turtle1, room_size, 1, 0, [2, 1, 11, 1, 4])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 8, 2, 6])
    draw_maze_line(turtle1, room_size, 1, 0, [2, 2, 3, 2, 7, 1])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 2, 3, 6, 3, 4])
    draw_maze_line(turtle1, room_size, 1, 0, [7, 4, 6, 2])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 5, 1, 6, 1, 4, 1])
    draw_maze_line(turtle1, room_size, 1, 1, [2, 8, 1, 7, 1])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 5, 1, 5, 1, 5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 2, 4, 2, 4, 4])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 4, 2, 3, 1, 2, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [9,1,9,1])

    # Now at top right one column outside maze, re-orient pointing up (north)
    turtle1.left(90)
    #
    # # Draw Vertical lines in zig zag fashion, first top to bottom,
    # # then bottom to top, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [11])
    draw_maze_line(turtle1, room_size, 1, 1, [2, 9])
    draw_maze_line(turtle1, room_size, 0, 1, [6,1,4])
    draw_maze_line(turtle1, room_size, 1, 1, [11])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 1, 9])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 1, 9])
    draw_maze_line(turtle1, room_size, 0, 0, [0, 11])
    draw_maze_line(turtle1, room_size, 1, 1, [8,1,2])
    draw_maze_line(turtle1, room_size, 0, 1, [1,1,9])
    draw_maze_line(turtle1, room_size, 1, 0, [0,6,1,4])
    draw_maze_line(turtle1, room_size, 0, 0, [0,7,1,3])
    draw_maze_line(turtle1, room_size, 1, 1, [9,1,1])
    draw_maze_line(turtle1, room_size, 0, 1, [5,1,5])
    draw_maze_line(turtle1, room_size, 1, 0, [0,2,1,5,1,2])
    draw_maze_line(turtle1, room_size, 0, 0, [2, 9])
    draw_maze_line(turtle1, room_size, 1, 0, [0,2,1,7,1])
    draw_maze_line(turtle1, room_size, 0, 0, [0,11])
    draw_maze_line(turtle1, room_size, 1, 0, [0,1,1,1,0,8])
    draw_maze_line(turtle1, room_size, 0, 0, [0,11])
    draw_maze_line(turtle1, room_size, 1, 0, [11])

    #Apply BFS over the graph of Chevening House Maze
    BFS(graph2, 'A', 'Z')

    # Navigating a turtle agent for tracing path in Own Maze.
    turtle2 = Turtle()
    turtle2.penup()
    turtle2.goto(60,-140)
    turtle2.speed('fast')
    turtle2.pendown()
    turtle2.color("red")
    turtle2.width(2)
    turtle2.left(90)
    turtle2.forward(10)
    turtle2.left(90)
    turtle2.forward(140)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(140)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(60)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(40)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(40)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(80)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(60)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.right(90)
    turtle2.forward(20)
    turtle2.left(90)
    turtle2.forward(20)

    update()

if __name__ == '__main__':

    done = False
    while not done:
        done = True
        maze = input("Select maze (1 to 3): ")  # get user input
        #Validating user input and calling the maze function
        if maze == '1':
            draw_hampton_court_maze(1, "blue", 20, 4, 250, -160)
        elif maze == '2':
            draw_chevening_house_maze(1, "blue", 20, 5, 250, -250)
        elif maze == '3':
            draw_own_maze(1, "blue", 20, 4, 250, -160)
        else:
            print("Incorrect input - must be number between 1 and 6.")
            done = False

    exitonclick()

