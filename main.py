import turtle
import random

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  for i in range(4):
    myturtle.forward(width)
    myturtle.right(90)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.up()
  myturtle.goto(x_start, y_start)
  myturtle.down()
  myturtle.goto(x_end, y_end)

def drawCircle(myturtle=None, radius=0):
  myturtle.speed(0)
  myturtle.circle(radius, steps=1000)
  myturtle.speed(4)

def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates(-1, -1, 1, 1)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, 1, 0, -1)
  drawCircle(myturtle, 1)

def throwDart(myturtle=None):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)
  myturtle.up()
  myturtle.goto(x, y)
  myturtle.down()
  r = isInCircle(myturtle, 0, 0, 1)
  if (r==True):
    myturtle.color("blue")
  else:
    myturtle.color("red")
  myturtle.dot()
  myturtle.color("black")

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  if (myturtle.distance(circle_center_x,circle_center_y) <= radius):
    return True 
  else:
    return False

def playDarts(myturtle=None):
  player_a = 0
  player_b = 0
  for i in range(1,21):
    if (i % 2) == 0:
      throwDart(myturtle)
      r = isInCircle(myturtle, 0, 0, 1)
      if (r == True):
        player_a = player_a + 1
    else:
      throwDart(myturtle)
      r = isInCircle(myturtle, 0, 0, 1)
      if (r == True):
        player_b = player_b + 1
  if (player_a > player_b):
    print("Player A wins!")
  elif (player_a < player_b):
    print("Player B wins!")
  else:
    print("There was a tie!")

def montePi(myturtle=None, number_darts=0):
  inside_count = 0
  for i in range(1, number_darts+1):
    throwDart(myturtle)
    r = isInCircle(myturtle, 0, 0, 1)
    if (r == True):
      inside_count = inside_count + 1
  pie_four = inside_count / number_darts
  pie_guess = pie_four * 4
  return pie_guess


def trivia(myscreen=None, radius=0):
  correct_ans = 0
  print("It's time for a game of trivia! Respond using 1, 2, 3, or 4")
  print("Question 1: How many seconds are in one hour?")
  print("1) 1000")
  print("2) 360")
  print("3) 3600")
  print("4) 4250")
  guess_one = int(input("Enter 1, 2, 3, or 4: "))
  if (guess_one == 3):
    correct_ans = correct_ans + 1
  print("Question 2: Who has the most points in NBA history?")
  print("1) Steph Curry")
  print("2) Michael Jordan")
  print("3) LeBron James")
  print("4) Kareem Abdul-Jabbar")
  guess_two = int(input("Enter 1, 2, 3, or 4: "))
  if (guess_two == 4):
    correct_ans = correct_ans + 1
  print("Question 3: What animal has the highest blood pressure?")
  print("1) Giraffe")
  print("2) Bear")
  print("3) Shark")
  print("4) Zebra")
  guess_three = int(input("Enter 1, 2, 3, or 4: "))
  if (guess_three == 1):
    correct_ans = correct_ans + 1
  print("Here is a visual of your results!")
  myscreen.setworldcoordinates(-200,-200,200,200)
  visual = turtle.Turtle()
  for i in range(1, 4):
    if (correct_ans >= i):
      visual.color('green')
    else:
      visual.color('red')
    visual.begin_fill()  
    visual.circle(radius, 120)
    visual.end_fill()
  return (correct_ans/3) * 100
  
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)
    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    darty.clear()
    percent = trivia(window, 100)
    print("\nYou got a "+str(percent)+"% on the quiz! " )
    window.exitonclick()
main()
