'''
MAKSIM KONDRASHOV - 40%
EDWARD BIKMETOV - 40%
KIRILL BYCHKOV - 60%
'''
from random import *
from tkinter import *
from math import *
# 90% создано на мобильных устройствах

d = dict()
def s_info():

	inf = """
НАРОД - 1 житель платит 
в год налог от заработанных им 
100 д.е., потребляет 1 ед зерна
ЗЕМЛЯ - с 1 земли приходит 10 ед зерна
КАЗНА - за 1 д.е. можно купить 
1 ед зерна + траты на случайные события
АРМИЯ - увеличивает шенс 
победы при войне
ИССЛЕДОВАНИЕ ЗКМЕЛЬ - 
шанс увеличить владения, перемотка хода
(PS: не рекрутируйте слишком много солдат,
поддердивайте разумный уровень налогов,
зерна, солдат и земли, это отражается на
вероятности событий и уровне смуты)
	
	"""
	i_ww = Tk()
	i_ww.title('ПРАВИЛА')
	inf1 = Label(i_ww, text=inf)
	inf1.grid(column=0, row=0)

d['Казна'] = 1000
d['Смута'] = 0
d['Народ'] = 100
d['Земля'] = 5
d['Зерно'] = 100
d['Армия'] = 15


def tax():
	''' налоговые манипуляции'''
	global line_tax
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
	''' начатт игру заново'''
	global c
	d['Казна'] = 1000
	d['Смута'] = 0
	d['Народ'] = 150
	d['Земля'] = 5
	d['Зерно'] = 100
	d['Армия'] = 15
	c = 0
	next()
def updateinfo():
	''' обновление информации'''
	global sum_zerno
	global tx
	global lands
	global line_rr
	global dat
	global mn
	global zn
	try:
		sum_zerno.destroy()
		lands.destroy()
		line_rr.destroy()
		mn.destroy()
		dat.destroy()
	except:
		www='ok'
	dat = Label(m_ww, text=str(c)+' год')
	dat.grid(column=0, row=0)
	sum_zerno = Scale(m_ww, orient='horizontal', from_=-d['Зерно'], to=floor(d['Казна']/2))
	sum_zerno.grid(column=1, row=3)
	lands = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	lands.grid(column=1, row=4)
	line_rr = Scale(m_ww, orient='horizontal', from_=-floor(d['Казна']/100), to=floor(d['Народ']*0.5))
	line_rr.grid(column=0, row=7)
	for i in d.keys():
		if d[i] < 0 or not str(d[i]).isdigit() : 
			d[i] = 0
	mn = Label(m_ww, text='Казна: '+str(d['Казна'])+' | Зерно: '+str(d['Зерно'])+'\nСмута: '+str(d['Смута'])+' | Народ: '+str(d['Народ'])+'\nЗемля: '+str(d['Земля'])+' | Армия: '+str(d['Армия']))
	mn.grid(column=0, row=1)
	
def ver1():
	''' вероятность подавления'''
	g = []
	for i in range(round(0.01*d['Казна'])+d['Армия']):
		g.append(1)
	for i in range(d['Смута']+floor(d['Народ']*0.005)):
		g.append(0)
	f = choice(g)
	if f == 0:
		end()
	else:
		d['Смута'] = 10
		d['Казна'] = floor(d['Казна']*0.25)
		d['Армия'] = floor(d['Армия']*0.25)
		next()

def end():
	''' выход/заново'''
	s_ww = Tk()
	s_ww.title('ПОРАЖЕНИЕ')
	tx = Label(s_ww, text='В аашей стране \nподнялось восстание')
	tx.grid(column=0, row=0)
	btn_next1 = Button(s_ww, text='ВЫЙТИ' , bg='blue', fg='white', command=ext )
	btn_next1.grid(column=0 , row=2)
	btn_next2 = Button(s_ww, text='начать\nзаново' , bg='red', fg='black', command=lambda:[restart(), s_ww.destroy()])
	btn_next2.grid(column=1 , row=2)
	
def smuta(s):
	''' определение параметров смуты'''
	if 25 < s or d['Армия']/d['Народ'] > 1:
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
    ''' основные изменения'''
    global die
    global line_tax
    d['Казна'] -= 10*(d['Армия'] - ceil(d['Народ']*0.075))
    if d['Народ'] < 1 or d['Земля'] < 1:
    	end()
    if d['Зерно'] >= d['Народ']:
    	d['Зерно'] = d['Зерно'] - d['Народ'] + d['Земля']*10
    	die = 0
    else:
    	d['Смута'] += 10*round((d['Народ'] - d['Зерно'])/d['Народ'])
    	d['Зерно'] = 0
    	die += 1
    if d['Армия']/d['Народ'] > 1:
    	d['Смута'] += round(d['Армия']/d['Народ'])
    t = line_tax.get()
    if t > 50:
    	d['Народ'] -= ceil(0.01*d['Народ'])
    	d['Смута'] += round(t/20)
    if t < 16 and d['Смута'] >= round(10/(t+1)) and d['Зерно'] > 0.9*d['Народ']:
    	d['Смута'] -= round(10/(t+1))
    elif t < 16 and d['Смута'] > 0 and d['Зерно'] > 0.9*d['Народ']:
    	d['Смута'] = 0
    if t > 90:
    	die += 0.5
    	d['Смута'] += round(t/10)
    if die > 1:
    	d['Народ'] -= ceil(0.03*d['Народ'])
    if d['Смута'] > 25:
    	smuta(d['Смута'])
    if d['Зерно'] >0.9*d['Народ'] and 25 < d['Смута'] < 40 and t < 50:
    	d['Народ'] += floor(d['Народ']*0.2/(d['Смута']+t+1))
    elif d['Зерно'] >0.9*d['Народ'] and d['Смута'] <= 25 and t >= 13:
    	d['Народ'] += round(d['Народ']*0.35/(d['Смута']+t+1))
    elif d['Зерно'] >0.9*d['Народ'] and d['Смута'] <= 25 and t < 13:
    	d['Народ'] += ceil(d['Народ']*0.55/(d['Смута']+t+1))

def pokupka_zerna():
	''' покупка зерна'''
	global sum_zerno
	j = sum_zerno.get()
	if j > 0:
		d['Казна'] -= 2*j
		d['Зерно'] += j
	else:
		d['Казна'] -= round(0.5*j)
		d['Зерно'] += j
	updateinfo()

def recrut():
	'''набор солдат '''
	global line_rr
	r = line_rr.get()
	if r < 0:
		d['Армия'] -= r
		d['Казна'] += 100*r
	else:
		d['Армия'] += r
		d['Народ'] -= r
		d['Смута'] += ceil(50*(r/d['Народ']))
	updateinfo()

def issledovanie_zemel():
	'''Сколько хотите потратить на исследования? ( 100 д.е. - 20% шанс получения 1 земли)'''
	global lands
	f = lands.get()
	e = 0
	d['Казна'] -= f
	for i in range(int(0.01*f)):
		e += choice([0, 0, 0, 0,1])
	ln = Label(m_ww, text='исследование\n земель')
	ln.grid(column=0, row=4)
	next()
	lands = Scale(m_ww, orient='horizontal', from_=0, to=d['Казна'])
	lands.grid(column=1, row=4)
	d['Земля'] += e
	d['Народ'] += 10*e
	updateinfo()
	mn.grid(column=0, row=1)
	l_ww = Tk()
	l_ww.title('РАССШИРИТЬ ГРАНИЦЫ')
	btn_next1 = Button(l_ww, text='Присоединено\nтерриторий:\n'+str(e) , bg='green', fg='white', command=lambda:[ l_ww.destroy()] )
	btn_next1.grid(column=0 , row=2)
def zj():
	global zernoj
	jl = zernoj.get()
	d['Казна'] -= jl
	d['Зерно'] += jl
	updateinfo()

def random_ivents():
	''' случайные события'''
	global line_tax
	t = line_tax.get()
	an = [0, 0, 1, 1, 6, 6, 6, 6, 6]
	for i in range(floor(t/20+1)):
		 an.append(2)
	for i in range(floor(5/(t+1))):
		 an.append(3)
	for i in range(round(0.002*d['Казна']/(d['Армия']+1)+1)):
		an.append(4)
	for i in range(ceil(10/(t+1))):
		 an.append(5)
	y = choice(an)
	if y != 6:
		r_ww = Tk()
		r_ww.title('СОБЫТИЕ')
		c = 'white'
		tt = '?'
		if y == 0:
			tt = 'УРОЖАЙНЫЙ ГОД\nЗерно +'+str(d['Земля']*5)
			d['Зерно'] += d['Земля']*5
			c = 'green'
		elif y == 1:
			tt = 'НЕУРОЖАЙНЫЙ ГОД\nЗерно -'+str(d['Земля']*5)
			d['Зерно'] -= d['Земля']*5
			c = 'red'
		elif y == 2:
			tt = 'КАЗНОКРАДСТВО\nКазна -'+str(round(d['Казна']*0.1))
			d['Казна'] -= round(d['Казна']*0.1)
			c = 'red'
		elif y == 3:
			tt = 'НАЙДЕН КЛАД\nКазна +'+str(round(d['Казна']*0.1))
			d['Казна'] += round(d['Казна']*0.1)
			c = 'green'
		elif y == 4:
			h = randrange(round(d['Народ']*0.03), round(d['Народ']*0.75))
			if h <= d['Армия']:
				rez = 'Победа!\Казна +'+str(round(0.75*d['Казна']*(h/d['Народ'])))+'\nАрмия -'+str(round(0.75*h))+'\nЗемля +'+str(round(0.5*d['Земля']*(h/d['Народ'])))
				d['Армия'] -= round(0.75*h)
				d['Казна'] += round(0.75*d['Казна']*(h/d['Народ']))
				d['Земля'] += round(0.5*d['Земля']*(h/d['Народ']))
				c = 'green'
			else:
				rez = 'Поражение!\Казна -'+str(round(0.85*d['Казна']*(h/d['Народ'])))+'\nАрмия -'+str(round(0.8*d['Армия']))+'\nЗемля -'+str(round(0.5*d['Земля']*(h/d['Народ'])))
				d['Армия'] -= round(0.8*d['Армия'])
				d['Казна'] -= round(0.75*d['Казна']*(h/d['Народ']))
				d['Земля'] -= round(0.5*d['Земля']*(h/d['Народ']))
				c = 'red'
			tt = 'НАПАДЕНИЕ\n\n результат:\n'+rez
		elif y == 5:
			tt = 'К ВАМ ПРИЕХАЛИ\nКУПЦЫ\nЗерно\n<-продать | купить ->'
			global zernoj
			zernoj = Scale(r_ww, orient='horizontal', from_=-d['Зерно'], to=ceil(0.008*d['Казна']+1)*100)
			zernoj.grid(column=0, row=1)
			c = 'blue'
			btn_next1 = Button(r_ww, text='OK' , bg=c, fg='white', command=lambda:[zj(), r_ww.destroy()])
			btn_next1.grid(column=0 , row=2)
		tx = Label(r_ww, text=tt)
		tx.grid(column=0, row=0)
		updateinfo()
		if y != 5:
			btn_next1 = Button(r_ww, text='OK' , bg=c, fg='white', command=lambda:[ r_ww.destroy()] )
			btn_next1.grid(column=0 , row=2)

def hd():
	global die
	d['Казна'] -= round(d['Казна']*0.25)
	d['Смута'] -= ceil(d['Смута']*0.15)
	die = 0
	updateinfo()

c = 0

def next():
	''' перемотка хода '''
	updateinfo()
	global lands
	global c
	global mn
	global line_rr
	if c > 0:
		tax()
	if c > 0:
		default_changes()
	global sum_zerno
	if d['Казна'] > d['Народ']*100:
		btn_hd = Button(m_ww, text='устроить\nпраздник\n'+str(round(d['Казна']*0.25)), command=lambda:[hd(), btn_hd.destroy()])
		btn_hd.grid(column=0, row=9)
	updateinfo()
	random_ivents()
	updateinfo()
	c += 1
	
m_ww = Tk()
m_ww.title('ГОСУДВРСТВО')
w = m_ww.winfo_screenwidth()
h = m_ww.winfo_screenheight()
m_ww.geometry(str(h)+'x'+str(w))
dat = Label(m_ww, text=str(c)+' год')
dat.grid(column=0, row=0)

line_tax = Scale(m_ww, orient='horizontal', from_=0, to=100)
line_tax.grid(column=1, row=2)
ln = Label(m_ww, text='исследование\n земель')
ln.grid(column=0, row=4)

tx = Label(m_ww, text='налог (% от дохода):  ')
tx.grid(column=0, row=2)
zn = Label(m_ww, text='рынок зерна\n(курс 1 к 2): ')
zn.grid(column=0, row=3)

updateinfo()
next()

btn_lands = Button(m_ww, text='исследовать\n земли', command=issledovanie_zemel)
btn_lands.grid(column=2, row=4)

rr = Label(m_ww, text='<- нанять | рекрутировать ->')
rr.grid(column=0, row=6)

v = Button(m_ww, text='сделка', command=pokupka_zerna)
v.grid(column=2, row=3)
btn_rr = Button(m_ww, text='набор в армию', command=recrut)
btn_rr.grid(column=0, row=5)

btn_next = Button(m_ww, text='завершить\nход' , bg='white', fg='black', command=lambda:[next(), mn.update()])
btn_next.grid(column=0 , row=8)
btn_inf = Button(m_ww, text='правила' , bg='yellow', fg='black', command=s_info)
btn_inf.grid(column=2 , row=0)
m_ww.mainloop()
