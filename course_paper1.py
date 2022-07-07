import filecmp
from tkinter import *
from tkinter.messagebox import *
import os
from time import strftime
import Pmw

time1 = ''
prevSec = ''
mins = 20
secs = 0
hours = 0
running = True

def view():
    win = Toplevel(root)
    win.title('Final results')
    win.geometry('200x200')
    def line(text):
        values = open(text, "r", encoding='UTF-8')
        lines = values.read()
        return lines

    st = line("tests/student.txt")
    final1 = line("tests/Final_results1.txt")
    final2 = line("tests/Final_results2.txt")
    final3 = line("tests/Final_results3.txt")
    final4 = line("tests/Final_results4.txt")
    final5 = line("tests/Final_results5.txt")
    final6 = line("tests/Final_results6.txt")
    Label(win, text='Student:'+'\n'+st, font='16').place(x=10, y=10)
    Label(win, text='Results:', font='16').place(x=100, y=10)
    Label(win, text=final1+'\n'+final2+'\n'+final3+'\n'+final4+'\n'+final5+'\n'+final6, font='16').place(x=100, y=30)

def about():
    Pmw.initialise()
    Pmw.aboutversion('1.0')
    Pmw.aboutcopyright('All rights reserved.')
    Pmw.aboutcontact(
        'Student: Iryna Kupets\n' +
        'Group: FLPL-12\n' +
        'email: iryna.kupets@gmail.com'
    )
    about = Pmw.AboutDialog(root, applicationname='Japanese Grammar & Vocabulary Testing Program')

def help():
    process = os.popen('hh.exe paper.chm')
    r = process.read()
    process.close()

def Test1():
    win = Toplevel(root)
    win.title('Test 1')
    win.geometry('700x500')
    f = open("tests/test1.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font=14, justify=LEFT).place(x=20, y=20)

    q = [Entry(win, textvariable="", bg='snow2')]
    q[0].place(x=510, y=50)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[1].place(x=510, y=85)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[2].place(x=510, y=120)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[3].place(x=510, y=155)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[4].place(x=510, y=190)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[5].place(x=510, y=225)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[6].place(x=510, y=260)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[7].place(x=510, y=295)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[8].place(x=510, y=330)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[9].place(x=510, y=365)

    def get_entry_data():
        with open('tests/results1.txt', 'w', encoding='UTF-8') as results2:
            results2.write(q[0].get() + '\n'
                                    + q[1].get() + '\n'
                                    + q[2].get() + '\n'
                                    + q[3].get() + '\n'
                                    + q[4].get() + '\n'
                                    + q[5].get() + '\n'
                                    + q[6].get() + '\n'
                                    + q[7].get() + '\n'
                                    + q[8].get() + '\n'
                                    + q[9].get())
            results2.close()
        res2 = filecmp.cmp('tests/results1.txt', 'tests/answers1.txt')
        if res2 == 0:
            open('tests/Final_results1.txt', 'w').write('Failed')
        else:
            open('tests/Final_results1.txt', 'w').write('Passed')

        result2check = open('tests/Final_results1.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result2check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=500, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()
    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=600, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=300, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def Test2():
    win = Toplevel(root)
    win.title('Test 2')
    win.geometry('600x500')
    f = open("tests/test2.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font=14, justify=LEFT).place(x=20, y=20)

    q = [Entry(win, textvariable="", bg='snow2')]
    q[0].place(x=400, y=50)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[1].place(x=400, y=85)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[2].place(x=400, y=120)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[3].place(x=400, y=155)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[4].place(x=400, y=190)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[5].place(x=400, y=225)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[6].place(x=400, y=260)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[7].place(x=400, y=295)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[8].place(x=400, y=330)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[9].place(x=400, y=365)

    def get_entry_data():
        with open('tests/results2.txt', 'w', encoding='UTF-8') as results2:
            results2.write(q[0].get() + '\n'
                                    + q[1].get() + '\n'
                                    + q[2].get() + '\n'
                                    + q[3].get() + '\n'
                                    + q[4].get() + '\n'
                                    + q[5].get() + '\n'
                                    + q[6].get() + '\n'
                                    + q[7].get() + '\n'
                                    + q[8].get() + '\n'
                                    + q[9].get())
            results2.close()
        res2 = filecmp.cmp('tests/results2.txt', 'tests/answers2.txt')
        if res2 == 0:
            open('tests/Final_results2.txt', 'w').write('Failed')
        else:
            open('tests/Final_results2.txt', 'w').write('Passed')

        result2check = open('tests/Final_results2.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result2check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=400, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()
    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=500, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=200, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def Test3():
    win = Toplevel(root)
    win.title('Test 3')
    win.geometry('1100x500')
    f = open("tests/test3.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font=14, justify=LEFT).place(x=20, y=20)

    def line(text):
        radiobut_values = open(text, "r", encoding='UTF-8')
        lines = radiobut_values.read().split('.')
        return lines

    lines3_1 = line("tests/Radio3_1.txt")
    lines3_2 = line("tests/Radio3_2.txt")
    lines3_3 = line("tests/Radio3_3.txt")
    lines3_4 = line("tests/Radio3_4.txt")
    lines3_5 = line("tests/Radio3_5.txt")
    lines3_6 = line("tests/Radio3_6.txt")
    lines3_7 = line("tests/Radio3_7.txt")
    lines3_8 = line("tests/Radio3_8.txt")
    lines3_9 = line("tests/Radio3_9.txt")
    lines3_10 = line("tests/Radio3_10.txt")

    qr1_1 = []
    choice3_1 = IntVar()
    for i in range(len(lines3_1)):
        qr1_1 = Radiobutton(win, text=lines3_1[i], font=14, variable=choice3_1, value=i)
        qr1_1.place(x=400 + i * 220, y=50)

    qr2_1 = []
    choice3_2 = IntVar()
    for i in range(len(lines3_2)):
        qr2_1 = Radiobutton(win, text=lines3_2[i], font=14, variable=choice3_2, value=i)
        qr2_1.place(x=400 + i * 220, y=85)

    qr3_1 = []
    choice3_3 = IntVar()
    for i in range(len(lines3_3)):
        qr3_1 = Radiobutton(win, text=lines3_3[i], font=14, variable=choice3_3, value=i)
        qr3_1.place(x=400 + i * 220, y=120)

    qr4_1 = []
    choice3_4 = IntVar()
    for i in range(len(lines3_4)):
        qr4_1 = Radiobutton(win, text=lines3_4[i], font=14, variable=choice3_4, value=i)
        qr4_1.place(x=400 + i * 220, y=155)

    qr5_1 = []
    choice3_5 = IntVar()
    for i in range(len(lines3_5)):
        qr5_1 = Radiobutton(win, text=lines3_5[i], font=14, variable=choice3_5, value=i)
        qr5_1.place(x=400 + i * 220, y=190)

    qr6_1 = []
    choice3_6 = IntVar()
    for i in range(len(lines3_6)):
        qr6_1 = Radiobutton(win, text=lines3_6[i], font=14, variable=choice3_6, value=i)
        qr6_1.place(x=400 + i * 220, y=225)

    qr7_1 = []
    choice3_7 = IntVar()
    for i in range(len(lines3_7)):
        qr7_1 = Radiobutton(win, text=lines3_7[i], font=14, variable=choice3_7, value=i)
        qr7_1.place(x=400 + i * 220, y=260)

    qr8_1 = []
    choice3_8 = IntVar()
    for i in range(len(lines3_8)):
        qr8_1 = Radiobutton(win, text=lines3_8[i], font=14, variable=choice3_8, value=i)
        qr8_1.place(x=400 + i * 220, y=295)

    qr9_1 = []
    choice3_9 = IntVar()
    for i in range(len(lines3_9)):
         qr9_1 = Radiobutton(win, text=lines3_9[i], font=14, variable=choice3_9, value=i)
         qr9_1.place(x=400 + i * 220, y=330)

    qr10_1 = []
    choice3_10 = IntVar()
    for i in range(len(lines3_10)):
        qr10_1 = Radiobutton(win, text=lines3_10[i], font=14, variable=choice3_10, value=i)
        qr10_1.place(x=400 + i * 220, y=365)

    def get_entry_data():
        with open('tests/results3.txt', 'w') as results3:
            results3.write(str(choice3_1.get()) + '\n'
                           + str(choice3_2.get()) + '\n'
                           + str(choice3_3.get()) + '\n'
                           + str(choice3_4.get()) + '\n'
                           + str(choice3_5.get()) + '\n'
                           + str(choice3_6.get()) + '\n'
                           + str(choice3_7.get()) + '\n'
                           + str(choice3_8.get()) + '\n'
                           + str(choice3_9.get()) + '\n'
                           + str(choice3_10.get()))

            results3.close()
        res3 = filecmp.cmp('tests/results3.txt', 'tests/answers3.txt')
        if res3 == 0:
            open('tests/Final_results3.txt', 'w').write('Failed')
        else:
            open('tests/Final_results3.txt', 'w').write('Passed')

        result3check = open('tests/Final_results3.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result3check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=700, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()
    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=900, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=350, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def Test5():
    win = Toplevel(root)
    win.title('Test 5')
    win.geometry('800x500')
    f = open("tests/test5.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font = 12, justify=LEFT).place(x=20, y=20)

    def line(text):
        values = open(text, "r", encoding='UTF-8')
        lines = values.read().split('.')
        return lines

    lines5_1 = line("tests/drop5_1.txt")
    lines5_2 = line("tests/drop5_2.txt")
    lines5_3 = line("tests/drop5_3.txt")
    lines5_4 = line("tests/drop5_4.txt")
    lines5_5 = line("tests/drop5_5.txt")
    lines5_6 = line("tests/drop5_6.txt")
    lines5_7 = line("tests/drop5_7.txt")
    lines5_8 = line("tests/drop5_8.txt")
    lines5_9 = line("tests/drop5_9.txt")
    lines5_10 = line("tests/drop5_10.txt")

    tkvar1 = StringVar()
    choice1 = lines5_1
    tkvar1.set(lines5_1[0])
    popupMenu1 = OptionMenu(win, tkvar1, *choice1)
    popupMenu1.config(width=20)
    popupMenu1.place(x=500, y=50)

    tkvar2 = StringVar()
    choice2 = lines5_2
    tkvar2.set(lines5_2[0])
    popupMenu2 = OptionMenu(win, tkvar2, *choice2)
    popupMenu2.config(width=20)
    popupMenu2.place(x=500, y=90)

    tkvar3 = StringVar()
    choice3 = lines5_3
    tkvar3.set(lines5_3[0])
    popupMenu3 = OptionMenu(win, tkvar3, *choice3)
    popupMenu3.config(width=20)
    popupMenu3.place(x=500, y=130)

    tkvar4 = StringVar()
    choice4 = lines5_4
    tkvar4.set(lines5_4[0])
    popupMenu4 = OptionMenu(win, tkvar4, *choice4)
    popupMenu4.config(width=20)
    popupMenu4.place(x=500, y=170)

    tkvar5 = StringVar()
    choice5 = lines5_5
    tkvar5.set(lines5_5[0])
    popupMenu5 = OptionMenu(win, tkvar5, *choice5)
    popupMenu5.config(width=20)
    popupMenu5.place(x=500, y=210)

    tkvar6 = StringVar()
    choice6 = lines5_6
    tkvar6.set(lines5_6[0])
    popupMenu6 = OptionMenu(win, tkvar6, *choice6)
    popupMenu6.config(width=20)
    popupMenu6.place(x=500, y=250)

    tkvar7 = StringVar()
    choice7 = lines5_7
    tkvar7.set(lines5_7[0])
    popupMenu7 = OptionMenu(win, tkvar7, *choice7)
    popupMenu7.config(width=20)
    popupMenu7.place(x=500, y=290)

    tkvar8 = StringVar()
    choice8 = lines5_8
    tkvar8.set(lines5_8[0])
    popupMenu8 = OptionMenu(win, tkvar8, *choice8)
    popupMenu8.config(width=20)
    popupMenu8.place(x=500, y=330)

    tkvar9 = StringVar()
    choice9 = lines5_9
    tkvar9.set(lines5_9[0])
    popupMenu9 = OptionMenu(win, tkvar9, *choice9)
    popupMenu9.config(width=20)
    popupMenu9.place(x=500, y=370)

    tkvar10 = StringVar()
    choice10 = lines5_10
    tkvar10.set(lines5_10[0])
    popupMenu10 = OptionMenu(win, tkvar10, *choice10)
    popupMenu10.config(width= 20)
    popupMenu10.place(x=500, y=410)

    def get_entry_data():
        with open('tests/results5.txt', 'w', encoding='UTF-8') as results5:
            results5.write(str(tkvar1.get()) + '\n'
                           + str(tkvar2.get()) + '\n'
                           + str(tkvar3.get()) + '\n'
                           + str(tkvar4.get()) + '\n'
                           + str(tkvar5.get()) + '\n'
                           + str(tkvar6.get()) + '\n'
                           + str(tkvar7.get()) + '\n'
                           + str(tkvar8.get()) + '\n'
                           + str(tkvar9.get()) + '\n'
                           + str(tkvar9.get()))
            results5.close()
        res5 = filecmp.cmp('tests/results5.txt', 'tests/answers5.txt')
        if res5 == 0:
            open('tests/Final_results5.txt', 'w').write('Failed')
        else:
            open('tests/Final_results5.txt', 'w').write('Passed')

        result5check = open('tests/Final_results5.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result5check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=500, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()
    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=700, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=250, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def Test6():
    win = Toplevel(root)
    win.title('Test 6')
    win.geometry('1100x500')
    f = open("tests/test6.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font=14, justify=LEFT).place(x=20, y=20)
    f1 = open("tests/list6.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f1), font=14, justify=LEFT).place(x=800, y=20)


    Label(win, text="1)", bg='snow2').place(x=480, y=40)
    Label(win, text="2)", bg='snow2').place(x=480, y=80)
    Label(win, text="3)", bg='snow2').place(x=480, y=120)
    Label(win, text="4)", bg='snow2').place(x=480, y=160)
    Label(win, text="5)", bg='snow2').place(x=480, y=200)
    Label(win, text="6)", bg='snow2').place(x=480, y=240)
    Label(win, text="7)", bg='snow2').place(x=480, y=280)
    Label(win, text="8)", bg='snow2').place(x=480, y=320)
    Label(win, text="9)", bg='snow2').place(x=480, y=360)
    Label(win, text="10)", bg='snow2').place(x=480, y=400)


    q = [Entry(win, textvariable="", bg='snow2')]
    q[0].place(x=500, y=40)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[1].place(x=500, y=80)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[2].place(x=500, y=120)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[3].place(x=500, y=160)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[4].place(x=500, y=200)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[5].place(x=500, y=240)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[6].place(x=500, y=280)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[7].place(x=500, y=320)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[8].place(x=500, y=360)
    q.append(Entry(win, textvariable="", bg='snow2'))
    q[9].place(x=500, y=400)
    q.append(Entry(win, textvariable="", bg='snow2'))



    def get_entry_data():
        with open('tests/results6.txt', 'w') as results6:
            results6.write(q[0].get() + '\n'
                                    + q[1].get() + '\n'
                                    + q[2].get() + '\n'
                                    + q[3].get() + '\n'
                                    + q[4].get() + '\n'
                                    + q[5].get() + '\n'
                                    + q[6].get() + '\n'
                                    + q[7].get() + '\n'
                                    + q[8].get() + '\n'
                                    + q[9].get())

            results6.close()
        res6 = filecmp.cmp('tests/results6.txt', 'tests/answers6.txt')
        if res6 == 0:
            open('tests/Final_results6.txt', 'w').write('Failed')
        else:
            open('tests/Final_results6.txt', 'w').write('Passed')

        result3check = open('tests/Final_results6.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result3check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=700, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()
    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=900, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=350, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def Test4():
    win = Toplevel(root)
    win.title('Test 4')
    win.geometry('1100x500')
    f = open("tests/test4.txt", encoding='UTF-8').readlines()
    Label(win, text="\n".join(f), font=14, justify=LEFT).place(x=20, y=20)

    def line(text):
        values = open(text, "r", encoding='UTF-8')
        lines = values.read().split('.')
        return lines

    lines7_1 = line("tests/Box4_1.txt")
    lines7_2 = line("tests/Box4_2.txt")
    lines7_3 = line("tests/Box4_3.txt")
    lines7_4 = line("tests/Box4_4.txt")
    lines7_5 = line("tests/Box4_5.txt")
    lines7_6 = line("tests/Box4_6.txt")
    lines7_7 = line("tests/Box4_7.txt")
    lines7_8 = line("tests/Box4_8.txt")
    lines7_9 = line("tests/Box4_9.txt")
    lines7_10 = line("tests/Box4_10.txt")

    qr1_1 =[]
    choice7_1_1 = IntVar()
    choice7_1_1.set(0)
    qr1_1 = Checkbutton(win, text=lines7_1[0], font=14, variable=choice7_1_1, onvalue=1, offvalue=0)
    qr1_1.place(x=400 + 0 * 220, y=60)
    choice7_1_2 = IntVar()
    qr1_1 = Checkbutton(win, text=lines7_1[1], font=14, variable=choice7_1_2, onvalue=1, offvalue=0)
    qr1_1.place(x=400 + 1 * 220, y=60)
    choice7_1_3 = IntVar()
    qr1_1 = Checkbutton(win, text=lines7_1[2], font=14, variable=choice7_1_3, onvalue=1, offvalue=0)
    qr1_1.place(x=400 + 2 * 220, y=60)

    qr2_1 = []
    choice7_2_1 = IntVar()
    qr2_1 = Checkbutton(win, text=lines7_2[0], font=14, variable=choice7_2_1, onvalue=1, offvalue=0)
    qr2_1.place(x=400 + 0 * 220, y=95)
    choice7_2_2 = IntVar()
    qr2_1 = Checkbutton(win, text=lines7_2[1], font=14, variable=choice7_2_2, onvalue=1, offvalue=0)
    qr2_1.place(x=400 + 1 * 220, y=95)
    choice7_2_3 = IntVar()
    qr2_1 = Checkbutton(win, text=lines7_2[2], font=14, variable=choice7_2_3, onvalue=1, offvalue=0)
    qr2_1.place(x=400 + 2 * 220, y=95)

    qr3_1 = []
    choice7_3_1 = IntVar()
    qr3_1 = Checkbutton(win, text=lines7_3[0], font=14, variable=choice7_3_1, onvalue=1, offvalue=0)
    qr3_1.place(x=400 + 0 * 220, y=130)
    choice7_3_2 = IntVar()
    qr3_1 = Checkbutton(win, text=lines7_3[1], font=14, variable=choice7_3_2, onvalue=1, offvalue=0)
    qr3_1.place(x=400 + 1 * 220, y=130)
    choice7_3_3 = IntVar()
    qr3_1 = Checkbutton(win, text=lines7_3[2], font=14, variable=choice7_3_3, onvalue=1, offvalue=0)
    qr3_1.place(x=400 + 2 * 220, y=130)

    qr4_1 = []
    choice7_4_1 = IntVar()
    choice7_4_1.set(0)
    qr4_1 = Checkbutton(win, text=lines7_4[0], font=14, variable=choice7_4_1, onvalue=1, offvalue=0)
    qr4_1.place(x=400 + 0 * 220, y=165)
    choice7_4_2 = IntVar()
    qr4_1 = Checkbutton(win, text=lines7_4[1], font=14, variable=choice7_4_2, onvalue=1, offvalue=0)
    qr4_1.place(x=400 + 1 * 220, y=165)
    choice7_4_3 = IntVar()
    qr4_1 = Checkbutton(win, text=lines7_4[2], font=14, variable=choice7_4_3, onvalue=1, offvalue=0)
    qr4_1.place(x=400 + 2 * 220, y=165)

    qr5_1 = []
    choice7_5_1 = IntVar()
    qr5_1 = Checkbutton(win, text=lines7_5[0], font=14, variable=choice7_5_1, onvalue=1, offvalue=0)
    qr5_1.place(x=400 + 0 * 220, y=200)
    choice7_5_2 = IntVar()
    qr5_1 = Checkbutton(win, text=lines7_5[1], font=14, variable=choice7_5_2, onvalue=1, offvalue=0)
    qr5_1.place(x=400 + 1 * 220, y=200)
    choice7_5_3 = IntVar()
    qr5_1 = Checkbutton(win, text=lines7_5[2], font=14, variable=choice7_5_3, onvalue=1, offvalue=0)
    qr5_1.place(x=400 + 2 * 220, y=200)

    qr6_1 = []
    choice7_6_1 = IntVar()
    qr6_1 = Checkbutton(win, text=lines7_6[0], font=14, variable=choice7_6_1, onvalue=1, offvalue=0)
    qr6_1.place(x=400 + 0 * 220, y=235)
    choice7_6_2 = IntVar()
    qr6_1 = Checkbutton(win, text=lines7_6[1], font=14, variable=choice7_6_2, onvalue=1, offvalue=0)
    qr6_1.place(x=400 + 1 * 220, y=235)
    choice7_6_3 = IntVar()
    qr6_1 = Checkbutton(win, text=lines7_6[2], font=14, variable=choice7_6_3, onvalue=1, offvalue=0)
    qr6_1.place(x=400 + 2 * 220, y=235)

    qr7_1 = []
    choice7_7_1 = IntVar()
    qr7_1 = Checkbutton(win, text=lines7_7[0], font=14, variable=choice7_7_1, onvalue=1, offvalue=0)
    qr7_1.place(x=400 + 0 * 220, y=270)
    choice7_7_2 = IntVar()
    qr7_1 = Checkbutton(win, text=lines7_7[1], font=14, variable=choice7_7_2, onvalue=1, offvalue=0)
    qr7_1.place(x=400 + 1 * 220, y=270)
    choice7_7_3 = IntVar()
    qr7_1 = Checkbutton(win, text=lines7_7[2], font=14, variable=choice7_7_3, onvalue=1, offvalue=0)
    qr7_1.place(x=400 + 2 * 220, y=270)

    qr8_1 = []
    choice7_8_1 = IntVar()
    choice7_8_1.set(0)
    qr8_1 = Checkbutton(win, text=lines7_8[0], font=14, variable=choice7_8_1, onvalue=1, offvalue=0)
    qr8_1.place(x=400 + 0 * 220, y=305)
    choice7_8_2 = IntVar()
    qr8_1 = Checkbutton(win, text=lines7_8[1], font=14, variable=choice7_8_2, onvalue=1, offvalue=0)
    qr8_1.place(x=400 + 1 * 220, y=305)
    choice7_8_3 = IntVar()
    qr8_1 = Checkbutton(win, text=lines7_8[2], font=14, variable=choice7_8_3, onvalue=1, offvalue=0)
    qr8_1.place(x=400 + 2 * 220, y=305)

    qr9_1 = []
    choice7_9_1 = IntVar()
    qr9_1 = Checkbutton(win, text=lines7_9[0], font=14, variable=choice7_9_1, onvalue=1, offvalue=0)
    qr9_1.place(x=400 + 0 * 220, y=340)
    choice7_9_2 = IntVar()
    qr9_1 = Checkbutton(win, text=lines7_9[1], font=14, variable=choice7_9_2, onvalue=1, offvalue=0)
    qr9_1.place(x=400 + 1 * 220, y=340)
    choice7_9_3 = IntVar()
    qr9_1 = Checkbutton(win, text=lines7_9[2], font=14, variable=choice7_9_3, onvalue=1, offvalue=0)
    qr9_1.place(x=400 + 2 * 220, y=340)

    qr10_1 = []
    choice7_10_1 = IntVar()
    qr10_1 = Checkbutton(win, text=lines7_10[0], font=14, variable=choice7_10_1, onvalue=1, offvalue=0)
    qr10_1.place(x=400 + 0 * 220, y=375)
    choice7_10_2 = IntVar()
    qr10_1 = Checkbutton(win, text=lines7_10[1], font=14, variable=choice7_10_2, onvalue=1, offvalue=0)
    qr10_1.place(x=400 + 1 * 220, y=375)
    choice7_10_3 = IntVar()
    qr10_1 = Checkbutton(win, text=lines7_10[2], font=14, variable=choice7_10_3, onvalue=1, offvalue=0)
    qr10_1.place(x=400 + 2 * 220, y=375)

    def get_entry_data():
        with open('tests/results4.txt', 'w') as results7:
            results7.write(str(choice7_1_1.get()) + str(choice7_1_2.get()) + str(choice7_1_3.get())+ '\n'
                           + str(choice7_2_1.get()) + str(choice7_2_2.get()) + str(choice7_2_3.get())+ '\n'
                           + str(choice7_3_1.get()) + str(choice7_3_2.get()) + str(choice7_3_3.get())+ '\n'
                           + str(choice7_4_1.get()) + str(choice7_4_2.get()) + str(choice7_4_3.get())+ '\n'
                           + str(choice7_5_1.get()) + str(choice7_5_2.get()) + str(choice7_5_3.get())+ '\n'
                           + str(choice7_6_1.get()) + str(choice7_6_2.get()) + str(choice7_6_3.get())+ '\n'
                           + str(choice7_7_1.get()) + str(choice7_7_2.get()) + str(choice7_7_3.get())+ '\n'
                           + str(choice7_8_1.get()) + str(choice7_8_2.get()) + str(choice7_8_3.get())+ '\n'
                           + str(choice7_9_1.get()) + str(choice7_9_2.get()) + str(choice7_9_3.get())+ '\n'
                           + str(choice7_10_1.get()) + str(choice7_10_2.get()) + str(choice7_10_3.get()))
            results7.close()
        res7 = filecmp.cmp('tests/results4.txt', 'tests/answers4.txt')
        if res7 == 0:
            open('tests/Final_results4.txt', 'w').write('Failed')
        else:
            open('tests/Final_results4.txt', 'w').write('Passed')

        result4check = open('tests/Final_results4.txt', 'r')
        Label(win, text='Result:', font='16').place(x=10, y=450)

        Label(win, text=result4check.read(), font='16').place(x=100, y=450)

    btn_next = Button(win, text='Check', command=get_entry_data)
    btn_next.place(x=700, y=450)

    def close_local():
        if askyesno(" Exit ", " Do you want to quit? "):
            win.destroy()

    btn_check = Button(win, text='Close', command=close_local)
    btn_check.place(x=900, y=450)
    clock = Label(win, font=('fixed', 16), bg='white smoke')
    clock.place(x=350, y=450)

    def tick():
        global prevSec, time1, secs, mins, hours, running
        if running:
            newSec = strftime("%S")
        else:
            newSec = ''
            prevSec = ''
        if newSec != prevSec:
            prevSec = newSec
            secs = secs - 1
            if secs < 0:
                secs = 59
                mins = mins - 1
                if mins < 0:
                    mins = 59
                    hours = hours - 1
                    if hours < 0:
                        hours = 0
                        mins = 0
                        secs = 0
                        clock.destroy()

        time2 = '%02d:%02d:%02d' % (hours, mins, secs)
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        clock.after(200, tick)

    tick()

def win_try():
    win = Toplevel(root)
    win.title('Select a test')
    win.geometry('500x500+500+100')
    Button(win, text="Start Test1", command=Test1).place(x=100, y=50, height=50, width=100)
    Button(win, text="Start Test2", command=Test2).place(x=300, y=50, height=50, width=100)
    Button(win, text="Start Test3", command=Test3).place(x=100, y=150, height=50, width=100)
    Button(win, text="Start Test4", command=Test4).place(x=300, y=150, height=50, width=100)
    Button(win, text="Start Test5", command=Test5).place(x=100, y=250, height=50, width=100)
    Button(win, text="Start Test6", command=Test6).place(x=300, y=250, height=50, width=100)

def close_win():
    if askyesno(" Exit ", " Do you want to quit? "):
        root.destroy()

root = Tk()
root.title('Japanese Grammar&Vocabulary Testing Program')
root.iconbitmap('Landmarks-Japan.ico')
root.configure(background='gray80')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 250
h = h - 250
root.geometry('500x500+{}+{}'.format(w, h))

bg_image = PhotoImage(file="Nihongo.png")
x = Label(image=bg_image)
x.grid(row=0, rowspan=15, column=4)

Label(text="First name:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
name = Entry()
name.grid(row=0, column=1, sticky=W + E, padx=10)

Label(text="Last name:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
surname = Entry()
surname.grid(row=1, column=1, sticky=W + E, padx=10)
Label(text="Group:").grid(row=2, column=0, sticky=W, padx=10, pady=10)
group = Entry()
group.grid(row=2, column=1, sticky=W + E, padx=10)
def allow_entry():
    start_but = Button(text='Start', state='disabled', command=win_try)
    x = name.get()
    y = surname.get()
    z = group.get()
    if x and y and z:
        start_but['state'] = 'normal'
        with open('tests/student.txt', 'w') as s:
            s.write(str(x) + ' '
                           + str(y) + '\n'
                           + str(z))
            s.close()
        Label(text="Welcome " + str(x) + " " + str(y)+ '\n' + "and good luck!", fg='black', bg='gray80', width=28, height=10).grid(row=4, rowspan=5,
                                                                                                       column=0,
                                                                                                       columnspan=3,
                                                                                                       sticky=W,
                                                                                                       padx=10, pady=10)

    else:
        start_but['state'] = 'disabled'
        Label(text = "Please enter the required information\nand retry", fg= 'red', bg='gray80').grid(row=4, rowspan=5, column=0, columnspan=3, sticky=W, padx=10, pady=10)
    start_but.grid(row=3, column=1, sticky=W, padx=10, pady=10)

s_but = Button(text='Submit', command=allow_entry).grid(row=3, column=0, sticky=W, padx=10, pady=10)


mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="View results", command=view)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close_win)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_separator()

mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.mainloop()
