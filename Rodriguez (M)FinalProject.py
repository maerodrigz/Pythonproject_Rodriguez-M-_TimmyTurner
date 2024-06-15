import turtle

turtle.pensize(10)
turtle.color("black")

def hair():
    turtle.penup()
    turtle.goto(-250, 80)  #starting
    turtle.pendown()
    turtle.fillcolor("#6E4227")
    turtle.pensize(10)
    
    turtle.begin_fill()
    turtle.setheading(45)
    turtle.circle(-500,35)
    
    turtle.setheading(217)
    turtle.forward(120)
    
    turtle.setheading(25)
    turtle.circle(-350,85)
    
    turtle.setheading(157)
    turtle.circle(550,60)
    
    turtle.setheading(273)
    turtle.forward(200)
   
    turtle.setheading(140)
    turtle.forward(100)
    
    turtle.setheading(100)
    turtle.circle(-1100,14.5)
    turtle.end_fill()
    
def hat():
    
    turtle.penup()
    turtle.goto(-253, 70) 
    turtle.pendown()
    turtle.fillcolor("#7A3758")
    
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.circle(-1100,7)
    turtle.setheading(80)
    turtle.circle(-20,170)
    turtle.setheading(275)
    turtle.forward(75)
    turtle.end_fill()
    
def hat2():
    turtle.penup()
    turtle.goto(-240,-198)
    turtle.pendown()
    turtle.fillcolor("#B3446E")
    
    turtle.begin_fill()
    turtle.setheading(200)
    turtle.forward(50)
    turtle.setheading(185)
    turtle.circle(-60,100)
    turtle.setheading(80)
    turtle.circle(-700,17)
    
    turtle.penup()
    turtle.goto(-291,-35)
    turtle.pendown()
    
    turtle.setheading(87)
    turtle.circle(-1000,14.5)
    turtle.goto(-240,-198)
    turtle.end_fill()
    
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-350,-250)
    turtle.pendown()
    turtle.circle(25)
    turtle.end_fill()

def face():
    turtle.penup()
    turtle.goto(-163,-262)
    turtle.pendown()
    turtle.fillcolor("#FFBC91")
    
    turtle.begin_fill()
    turtle.setheading(180)
    turtle.circle(55,250)
    turtle.setheading(295)
    turtle.forward(110)
    
    turtle.setheading(345)
    turtle.circle(260,250)
    turtle.goto(-163,-262)
    turtle.end_fill()
    
def body():
    turtle.penup()
    turtle.goto(-80,-410)
    turtle.pendown()
    turtle.fillcolor("#B3446E")
    
    turtle.begin_fill()
    turtle.setheading(175)
    turtle.forward(100)
    turtle.setheading(275)
    turtle.forward(90)
    turtle.setheading(2)
    turtle.forward(100)
    
    turtle.setheading(280)
    turtle.circle(-450, 35)
    turtle.setheading(150)
    turtle.circle(55,100)
    turtle.setheading(0)
    turtle.forward(140)
    turtle.setheading(65)
    turtle.forward(60)
    
    turtle.setheading(80)
    turtle.circle(-30,185)
    turtle.setheading(260)
    turtle.forward(48)
    turtle.setheading(0)
    turtle.forward(100)
    
    turtle.setheading(100)
    turtle.circle(45,100)
    turtle.setheading(80)
    turtle.circle(550, 32)
    
    turtle.penup()
    turtle.goto(50,-480)
    turtle.pendown()
    turtle.setheading(3)
    turtle.forward(100)
    turtle.setheading(92)
    turtle.forward(70)
    turtle.goto(-80,-410)
    turtle.end_fill()
     
def eyes():
     
     turtle.pensize(7)
     turtle.penup()
     turtle.goto(190,-80)
     turtle.pendown()
     turtle.fillcolor("white")
     turtle.begin_fill()
     turtle.circle(75)
     turtle.end_fill()
    
     turtle.penup()
     turtle.goto(40,-120)
     turtle.pendown()
     turtle.begin_fill()
     turtle.circle(75)
     turtle.end_fill()
     
     turtle.color("#167DC1", "#167DC1")
     turtle.penup()
     
     turtle.goto(20,-66)
     turtle.pendown()
     
     turtle.begin_fill()
     turtle.setheading(170)
     turtle.circle(35,235)
     turtle.setheading(81)
     turtle.circle(75,47)
     turtle.end_fill()
     
     turtle.color("black")
     turtle.penup()
     turtle.goto(26,-68)
     turtle.pendown()
     turtle.circle(75)
     
     turtle.color("#167DC1", "#167DC1")
     turtle.penup()
     
     turtle.goto(167,-25)
     turtle.pendown()
     
     turtle.begin_fill()
     turtle.setheading(170)
     turtle.circle(35,235)
     turtle.setheading(81)
     turtle.circle(75,47)
     turtle.end_fill()
     
     turtle.color("black")
     turtle.penup()
     turtle.goto(176,-28)
     turtle.pendown()
     turtle.circle(75)
     
def eyebrows():
     
     turtle.penup()
     turtle.goto(-165,-40)
     turtle.pendown()
     turtle.fillcolor("#432A12")
     
     turtle.begin_fill()
     turtle.setheading(35)
     turtle.forward(140)
     turtle.setheading(300)
     turtle.forward(40)
     turtle.setheading(215)
     turtle.forward(150)
     turtle.goto(-165,-40)
     turtle.end_fill()
     
     turtle.penup()
     turtle.goto(0,60)
     turtle.pendown()
     
     turtle.begin_fill()
     turtle.setheading(360)
     turtle.forward(120)
     turtle.setheading(269)
     turtle.forward(35)
     turtle.setheading(181)
     turtle.forward(120)
     turtle.goto(0,60)
     turtle.end_fill()
     
def mouth():
     
      turtle.pensize(7)
      turtle.fillcolor("#FFBC91")
      
      turtle.begin_fill()    
      turtle.penup()
      turtle.goto(121,-188)
      turtle.pendown()
      
      turtle.color("#FFBC91", "#FFBC91")
      turtle.goto(85,-170)
      
      turtle.color("black", "#FFBC91")
      turtle.setheading(270)
      turtle.circle(35, -80)
      turtle.circle(15,-70)
      turtle.circle(35,-80)
      turtle.circle(5,-10)
      turtle.end_fill()
      
      turtle.setheading(30)
      turtle.forward(80)
      
      turtle.setheading(250)
      turtle.circle(-170,135)    
      
      turtle.setheading(250)
      turtle.circle(130,50)
      
      turtle.setheading(300)
      turtle.circle(250,25)
      
      turtle.setheading(333)
      turtle.circle(150,65)
      
def insidemouth():
                      
           turtle.penup()
           turtle.goto(60, -320)
           turtle.pendown()
           turtle.fillcolor("#892135")
           
           turtle.begin_fill()
           turtle.setheading(310)
           turtle.forward(43)
           
           turtle.pensize(3)
           turtle.setheading(204)
           turtle.circle(-150, 45)
           
           turtle.setheading(149)
           turtle.circle(-250,25)
           
           turtle.setheading(125)
           turtle.circle(-130,52)
           
           turtle.setheading(298)
           turtle.circle(170,46)
           
           turtle.setheading(260)
           turtle.circle(65,80)    
           turtle.setheading(350)
           turtle.circle(75,30)
           turtle.end_fill()
           
def toungue():
           
           turtle.pensize(7)
           turtle.penup()
           turtle.goto(-10,-358)
           turtle.pendown()
           turtle.fillcolor("#E9677D")
          
           turtle.begin_fill()
           turtle.setheading(88)
           turtle.circle(70, 107)
           
           turtle.pensize(3)
           turtle.setheading(300)
           turtle.circle(180,37)
           turtle.end_fill()
           
           turtle.pensize(7)
           turtle.penup()
           turtle.goto(-123.55,-161.32)
           turtle.pendown()
           
           turtle.setheading(250)
           turtle.circle(130,50)
           
           turtle.setheading(300)
           turtle.circle(250,25)
           
           turtle.setheading(333)
           turtle.circle(150,65)
           
         
def teeth():
      
          turtle.penup()
          turtle.goto(-20,-250)
          turtle.pendown()
          turtle.fillcolor("white")
          
          turtle.begin_fill()
          turtle.setheading(260)
          turtle.circle(65,80)    
          turtle.setheading(350)
          turtle.circle(75,105)
         
          turtle.setheading(207)
          turtle.circle(-170,44)
          turtle.end_fill()
          
          turtle.penup()
          turtle.goto(50,-263)
          turtle.pendown()
          turtle.setheading(260)
          turtle.forward(60)
               
def pants():
	     
	     turtle.penup()
	     turtle.goto(75,-630)
	     turtle.pendown()
	     turtle.fillcolor("#13364B")
	     
	     turtle.begin_fill()
	     turtle.setheading(180)
	     turtle.forward(145)
	     
	     turtle.setheading(262)
	     turtle.circle(-450,16.8)
	     turtle.setheading(150)
	     turtle.circle(55,100)
	     turtle.setheading(0)
	     turtle.forward(140)
	     turtle.setheading(65)
	     turtle.forward(60)
	     
	     turtle.setheading(80)
	     turtle.circle(-30,185)
	     turtle.setheading(260)
	     turtle.forward(48)
	     turtle.setheading(0)
	     turtle.forward(100)
	     
	     turtle.setheading(100)
	     turtle.circle(45,100)
	     turtle.setheading(80)
	     turtle.circle(550,13)
	     turtle.end_fill()
	     
def righthand():
	     
	     turtle.penup()
	     turtle.goto(-180,  -403)
	     turtle.pendown()
	     turtle.fillcolor("#FFBC91")
	     
	     turtle.begin_fill()
	     turtle.setheading(175)
	     turtle.forward(120)
	     
	     turtle.setheading(40)
	     turtle.circle(45,80)
	     turtle.circle(10,80)
	     turtle.circle(45,80)
	     turtle.circle(5,5)
	     
	     turtle.setheading(150)
	     turtle.circle(75,60)
	     turtle.circle(10,80)
	     turtle.circle(20,80) 
	     turtle.setheading(2)
	     turtle.forward(35)
	     
	     turtle.setheading(200)
	     turtle.circle(65,60)
	     turtle.circle(10,80)
	     turtle.circle(20,80)
	     turtle.setheading(50)
	     turtle.forward(35)
	     
	     turtle.setheading(250)
	     turtle.circle(45,60)
	     turtle.circle(10,80)
	     turtle.circle(20,80)
	     turtle.setheading(95)
	     turtle.forward(28)
	     turtle.setheading(356)
	     turtle.forward(135)
	     turtle.goto(-180,-403)	
	     turtle.end_fill()
	     
def lefthand():
    	 
    	 turtle.penup()
    	 turtle.goto(147,-404)
    	 turtle.pendown()
    	 turtle.fillcolor("#FFBC91")
    	 
    	 turtle.begin_fill()
    	 turtle.setheading(5)
    	 turtle.forward(120)
  
    	 turtle.setheading(140)
    	 turtle.circle(-45,80)
    	 turtle.circle(-10,80)
    	 turtle.circle(-45,80)
    	 turtle.circle(-5,5)
    	 
    	 turtle.setheading(30)
    	 turtle.circle(-75,60)
    	 turtle.circle(-10,80)
    	 turtle.circle(-20,80)
    	 turtle.setheading(178)
    	 turtle.forward(35)
    	 
    	 turtle.setheading(340)
    	 turtle.circle(-65,60)
    	 turtle.circle(-10,80)
    	 turtle.circle(-20,80)
    	 turtle.setheading(130)
    	 turtle.forward(35)
    	 
    	 turtle.setheading(300)
    	 turtle.circle(-45,60)
    	 turtle.circle(-10,80)
    	 turtle.circle(-20,80)
    	 turtle.setheading(85)
    	 turtle.forward(28)
    	 turtle.setheading(182)
    	 turtle.forward(135)
    	 turtle.goto(147,-404)
    	 turtle.end_fill()
    	 	                    
body()
pants()     
righthand()
lefthand()
face()     
hat2()   
hat()
hair()
eyes()
eyebrows()
mouth()
teeth()
insidemouth()
toungue()

turtle.hideturtle()
turtle.done()
