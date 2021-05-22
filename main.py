from random import *
from tkinter import *

from math import *

d = dict()

c = """
Правила:
НАРОД - 1 житель платит в год налог от заработанных им 100 д.е., потребляет 1 ед зерна
ЗЕМЛЯ - с 1 земли приходит 10 ед зерна
КАЗНА - за 1 д.е. можно купить 1 ед зерна + траты на случайные события
"""

d['Казна'] = 1000
d['Смута'] = 0
d['Народ'] = 100
d['Земля'] = 5
d['Зерно'] = 100

#def 
#print(c)
def tax():
	global line_tax
	#global c
	t = line_tax.get()
	if  25 < t:
		d['Смута'] += 1*round(t/10)
	elif t <= 5 and d['Смута'] > 0:
		d['Смута'] -= 1
	
	d['Казна'] += t*d['Народ']
	
die = 0
def ext():
	exit()
def restart():
	#global s_ww
	#global l_ww
	global c
	#s_ww.destroy()
	#l_ww.destroy()
	d['Казна'] = 1000
	d['Смута'] = 0
	d['Народ'] = 150
	d['Земля'] = 5
	d['Зерно'] = 100
	c = 0
	next()
def ver1():
	
	g = []
	#global l_ww
	for i in range(round(0.01*d['Казна'])):
		g.append(1)
	for i in range(10):
		g.append(0)
	f = choice(g)
	
	#f = choice([0, 1, 1])
	if f == 0:
		end()
	else:
		d['Смута'] = 10
		d['Казна'] = floor(d['Казна']*0.25)
		#l_ww.destroy()
		next()

		


def end():
	#global s_ww
	s_ww = Tk()
	s_ww.title('ПОРАЖЕНИЕ')
	
	#s_ww.geometry('200x100')
	tx = Label(s_ww, text='В аашей стране \nподнялось восстание')
	tx.grid(column=0, row=0)
	btn_next1 = Button(s_ww, text='ВЫЙТИ' , bg='blue', fg='white ', command=ext )
	btn_next1.grid(column=0 , row=2)
	btn_next2 = Button(s_ww, text='начать\nзаново' , bg='red', fg='black', command=lambda:[restart(), s_ww.destroy()])
	btn_next2.grid(column=1 , row=2)
	
def smuta(s):
	if 25 < s :
		d['Казна'] -= round((s*d['Казна'])/250)
	if 60 <= s < 100:
		d['Земля'] -= round((s*d['Земля'])/250)
		d['Народ'] -= round((s*d['Народ'])/250)
	if s > 99:
		s_ww = Tk()
		s_ww.title('ВОССТАНИЕ')
		#s_ww.geometry('200x100')
		tx = Label(s_ww, text='В вашей стране \nподнялось восстание')
		tx.grid(column=0, row=0)
		btn_next1 = Button(s_ww, text='подавить' , bg='blue', fg='white', command=lambda:[ver1(), s_ww.destroy()] )
		btn_next1.grid(column=0 , row=2)
		btn_next2 = Button(s_ww, text='сложить полномочия' , bg='red', fg='black', command=lambda:[end(), s_ww.destroy()])
		btn_next2.grid(column=1 , row=2)
		

def default_changes():
    global die
    global line_tax
    if d['Народ'] < 1 or d['Земля'] < 1:
    	end()
    #d['Казна'] = d['Казна'] + d['Народ']
    if d['Зерно'] >= d['Народ']:
    	d['Зерно'] = d['Зерно'] - d['Народ'] + d['Земля']*10
    	die = 0
    else:
    	
    	d['Смута'] += 10*round((d['Народ'] - d['Зерно'])/d['Народ'])
    	d['Зерно'] = 0
    	die += 1
    if die > 1:
    	d['Народ'] -= ceil(0.05*d['Народ'])
    if d['Смута'] > 25:
    	smuta(d['Смута'])
    t = line_tax.get()
    if d['Зерно'] >0.9*d['Народ'] and 25 < d['Смута'] < 40 and t < 50:
    	d['Народ'] += floor(d['Народ']*0.2/(d['Смута']+t+1))
    elif d['Зерно'] >0.9*d['Народ'] and d['Смута'] <= 25 and t >= 13:
    	d['Народ'] += round(d['Народ']*0.35/(d['Смута']+t+1))
    elif d['Зерно'] >0.9*d['Народ'] and d['Смута'] <= 25 and t < 13:
    	d['Народ'] += ceil(d['Народ']*0.55/(d['Смута']+t+1))
    
	

#'''
def pokupka_zerna():
	global sum_zerno
	
	d['Казна'] -= sum_zerno.get()
	d['Зерно'] += sum_zerno.get()
	mn = Label(m_ww, text='Казна: '+str(d['Казна'])+' | Зерно: '+str(d['Зерно'])+'\nСмута: '+str(d['Смута'])+' | Народ: '+str(d['Народ'])+'\nЗемля: '+str(d['Земля']))
	mn.grid(column=0, row=1)
	zn = Label(m_ww, text='покупка зерна\n(1 д.е. = 1 з): ')
	zn.grid(column=0, row=3)
	
	sum_zerno = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	sum_zerno.grid(column=1, row=3)
	lands = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	lands.grid(column=1, row=4)
#'''

def issledovanie_zemel():
    #t = 'Сколько хотите потратить на исследования? ( 100 д.е. - 20% шанс получения 1 земли)'
	global lands
	f = lands.get()
	e = 0
	d['Казна'] -= f
	for i in range(int(0.01*f)):
		e += choice([0, 0, 0, 0,1])
	d['Земля'] += e
	d['Народ'] += 10*e
	#d['Зерно'] += sum_zerno.get()
	mn = Label(m_ww, text='Казна: '+str(d['Казна'])+' | Зерно: '+str(d['Зерно'])+'\nСмута: '+str(d['Смута'])+' | Народ: '+str(d['Народ'])+'\nЗемля: '+str(d['Земля']))
	mn.grid(column=0, row=1)
	ln = Label(m_ww, text='исследование\n земель')
	ln.grid(column=0, row=4)
	next()
	lands = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	lands.grid(column=1, row=4)
	
	l_ww = Tk()
	l_ww.title('РАССШИРИТЬ ГРАНИЦЫ')
	#s_ww.geometry('200x100')
	##tx = Label(l_ww, text=t)
	#tx.grid(column=0, row=0)
	btn_next1 = Button(l_ww, text='Присоединено\nтерриторий:\n'+str(e) , bg='green', fg='white', command=lambda:[ l_ww.destroy()] )
	btn_next1.grid(column=0 , row=2)
	#btn_next2 = Button(s_ww, text='сложить полномочия' , bg='red', fg='black', command=lambda:[end(), s_ww.destroy()])
	#btn_next2.grid(column=1 , row=2)
def random_s():
	t =''
def upgrade():
	t = ''

print('Начало ( 0 год ):')
#stats(d)
c = 0

def next():
	global lands
	global c
	global mn
	
	dat = Label(m_ww, text=str(c)+' год')
	dat.grid(column=0, row=0)
	if c > 0:
		tax()
	lands = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	lands.grid(column=1, row=4)
	if c > 0:
		default_changes()
	#
	global sum_zerno
	
	sum_zerno = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	sum_zerno.grid(column=1, row=3)
	tx = Label(m_ww, text='налог (% от дохода):  ')
	tx.grid(column=0, row=2)
	
	v = Button(m_ww, text='купить', command=pokupka_zerna)
	v.grid(column=2, row=3)
	mn = Label(m_ww, text='Казна: '+str(d['Казна'])+' | Зерно: '+str(d['Зерно'])+'\nСмута: '+str(d['Смута'])+' | Народ: '+str(d['Народ'])+'\nЗемля: '+str(d['Земля']))
	mn.grid(column=0, row=1)
	zn = Label(m_ww, text='покупка зерна\n(1 д.е. = 1 з): ')
	zn.grid(column=0, row=3)
	c += 1
	
	


#'''
m_ww = Tk()
m_ww.title('ГОСУДВРСТВО')
w = m_ww.winfo_screenwidth()
h = m_ww.winfo_screenheight()
m_ww.geometry(str(h)+'x'+str(w))

line_tax = Scale(m_ww, orient='horizontal', from_=0, to=100)
line_tax.grid(column=1, row=2)
ln = Label(m_ww, text='исследование\n земель')
ln.grid(column=0, row=4)


next()


btn_lands = Button(m_ww, text='исследовать\n земли', command=issledovanie_zemel)
btn_lands.grid(column=2, row=4)
btn_upgrade = Button(m_ww, text='поднять рейтинг', command=upgrade)
btn_upgrade.grid(column=0, row=5)
btn_next = Button(m_ww, text='завершить ход' , bg='white', fg='black', command=lambda:[next(), mn.update()])
btn_next.grid(column=0 , row=7)


m_ww.mainloop()
#'''
