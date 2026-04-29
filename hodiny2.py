import math, tkinter as tk, datetime as dt
win = tk.Tk()
win.title("Hodiny")
canvas = tk.Canvas(win, width=800, height=800, bg="white")
canvas.pack()

s1 = 400
s2 = 400
kratka_ruc = 75
dlha_ruc = 150
polomer_cisla = dlha_ruc + 5
hrubka_h = 3
hrubka_s = 1

for i in range (1, 13):
     uhol = math.radians(i*30-90)
     x = s1+175*math.cos(uhol)
     y = s2+175*math.sin(uhol)
     canvas.create_text (x, y, text = str (i), font = ("Arial", 16 , "bold"))
     canvas.create_oval (s1-200 , s2-200, s1+200, s2 +200 , outline = "black", width = 3)

rucicka_h =  canvas.create_line(s1,s2 ,s1 + dlha_ruc * math.cos(uhol_minuta), s2 + dlha_ruc*math.sin(uhol_minuta),width= hrubka_h, fill = "black")
rucicka_m =  canvas.create_line(s1, s2,s1 + kratka_ruc * math.cos(uhol_hodina),s2 + kratka_ruc * math.sin(uhol_hodina),width=hrubka_h, fill="black")
rucicka_s =  canvas.create_line(s1, s2,s1 + dlha_ruc * math.cos(uhol_sekunda),s2 + dlha_ruc * math.sin(uhol_sekunda),width=hrubka_s, fill="black")

def draw():
    cas = dt.datetime.now()
    print(cas.hour, cas.minute, cas.second)
    uhol_minuta = math.radians(cas.minute * 6 - 90)
    uhol_hodina = math.radians(cas.hour * 30 + cas.minute * 0.5 - 90)
    uhol_sekunda = math.radians(cas.second * 6 - 90)
    canvas.after(1000, draw)

draw()
win.mainloop()