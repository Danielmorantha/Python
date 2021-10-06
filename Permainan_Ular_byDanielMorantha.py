# by Daniel Morantha
# Game using python standard libary

import turtle
import time
import random


Jeda = 0.1
queue =[]

#Menghitung skor tertinggi
pen = turtle.Turtle()
pen.shape('square')
pen.penup()
pen.speed(0)
pen.color('White')

pen.hideturtle()
pen.goto(0,210)
pen.write("Skor: 0    Skor Tertinggi: 0   ",align='center',font=('Arial',25,'bold'))


# Membuat tampilan judul Permainan
window = turtle.Screen()
window.bgcolor('Black')
window.title('Permainan Ular by Daniel Morantha')
window.setup(width=600,height=500)
window.tracer(0)

#Selanjutnya, membuat kepala ular
Kepala_Ular = turtle.Turtle()
Kepala_Ular.speed(0)
Kepala_Ular.shape('circle')
Kepala_Ular.color('Beige')
Kepala_Ular.penup()
Kepala_Ular.goto(0,0) # default posisi kepala ular
Kepala_Ular.direction ='stop'

#Selanjutnya membuat makanan Ular
Makanan_Ular = turtle.Turtle()
Makanan_Ular.speed(0)
Makanan_Ular.shape('circle')

Makanan_Ular.color('green')
Makanan_Ular.penup()
Makanan_Ular.goto(0,150) # default posisi makanan ular



########################################################################
# ketika ular digerakan oleh function
def Gerak_Ular():
    if Kepala_Ular.direction == 'up':
        y = Kepala_Ular.ycor()
        Kepala_Ular.sety(y + 10)
    if Kepala_Ular.direction == 'down':
        y = Kepala_Ular.ycor()
        Kepala_Ular.sety(y - 10)
    if Kepala_Ular.direction == 'left':
        x = Kepala_Ular.xcor()
        Kepala_Ular.setx(x - 10)
    if Kepala_Ular.direction == 'right':
        x = Kepala_Ular.xcor()
        Kepala_Ular.setx(x + 10)


def ke_atas():
    Kepala_Ular.direction = 'up'


def ke_bawah():
    Kepala_Ular.direction = 'down'


def ke_kiri():
    Kepala_Ular.direction = 'left'


def ke_kanan():
    Kepala_Ular.direction = 'right'


def Tabrakan_Makanan():
    if Kepala_Ular.distance(
            Makanan_Ular) < 15:  # ketika pengguna memilih jarak 15
        Makanan_Ular.goto(random.randint(-290, 290), random.randint(-249, 249))
        """ Di sini kita menggunakan nomor acak untuk memindahkan makanan ular. rentang itu karena lebar dan tinggi layar  """
        Badan_Ular = turtle.Turtle()  # Semakin banyak makan, semakin lebar
        Badan_Ular.speed(0)
        Badan_Ular.shape('circle')
        Badan_Ular.color('yellow')
        Badan_Ular.penup()
        queue.append(Badan_Ular)
        return True
    return False


def Tabrakan_Garis():
    # Garis batas
    if Kepala_Ular.xcor() > 290 or Kepala_Ular.xcor() < -290 or Kepala_Ular.ycor() > 249 or Kepala_Ular.ycor() < -249:
        time.sleep(1)
        Kepala_Ular.goto(0, 0)
        Kepala_Ular.direction = 'stop'
        for segment in queue:
            segment.goto(1000, 1000)
        queue.clear()
        return True

    return False
def Tabrakan_Badan():
    # Garis badan
    for segment in queue:
        if segment.distance(Kepala_Ular) < 10:  
            time.sleep(1)
            Kepala_Ular.goto(0, 0)
            Kepala_Ular.direction = 'stop'
            for segment in queue:
                segment.goto(1000, 1000)
            queue.clear()
            return True
    return False


def Bertambah_Besar():
    # bertambah range body
    for i in range(len(queue) - 1, 0, -1):
        if i % 5 == 0:
            queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
            queue[i].color('green')
            continue
        queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
    if len(queue) > 0:
        queue[0].goto(Kepala_Ular.xcor(), Kepala_Ular.ycor())



#  ketika instruksi dengan string
window.listen()
window.onkeypress(ke_atas, 'Up')
window.onkeypress(ke_bawah, 'Down')
window.onkeypress(ke_kiri, 'Left')
window.onkeypress(ke_kanan, 'Right')

####################################################################################
    # Ulang Permainan
Skor = 0
Skor_Tertinggi = 0
while True:

    window.update()
    Gerak_Ular()
    if Tabrakan_Makanan():
        Skor += 10
        Skor_Tertinggi += 10
        if Skor > Skor_Tertinggi:
            Skor_Tertinggi = Skor
        pen.clear()
        pen.write('Skor:{}    Skor Tertinggi:{}  '.format(Skor, Skor_Tertinggi), align='center', font=('Arial', 25, 'bold'))

    if Tabrakan_Badan() or Tabrakan_Garis():
        Skor = 0
        pen.clear()
        pen.write('Skor:{}    Skor Tertinggi:{}  '.format(Skor, Skor_Tertinggi), align='center', font=('Arial', 25, 'bold'))
    time.sleep(Jeda)
    Bertambah_Besar()


# Menjaga pop up tampil di layar
window.mainloop()

# Daniel Morantha