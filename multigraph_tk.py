#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Oct 18 14:38:07 2016.

@author: lashkov

"""

import os.path
import random
import re
import sys
import tkinter as tk
from math import factorial
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


def joke():
    """Шутка юмора :-)"""
    joke_txt = [
        "There are 10 types of people in the world: those who understand binary, and those who don't\n",
        "If at first you don't succeed; call it version 1.0\n",
        "I'm not anti-social; I'm just not user friendly\n",
        'My software never has bugs. It just develops random features\n',
        'Roses are #FF0000 , Violets are #0000FF , All my base belongs to you\n',
        'In a world without fences and walls, who needs Gates and Windows?\n',
        "Hand over the calculator, friends don't let friends derive drunk\n",
        "I would love to change the world, but they won't give me the source code\n",
        'Enter any 11-digit prime number to continue...\n',
        "The box said 'Requires Windows 95 or better'. So I installed LINUX\n",
        'A penny saved is 1.39 cents earned, if you consider income tax\n',
        'Unix, DOS and Windows...the good, the bad and the ugly\n',
        (
            'A computer lets you make more mistakes faster than any invention in human history - with the possible'
            ' exceptions of handguns and tequila\n'
        ),
        'The code that is the hardest to debug is the code that you know cannot possibly be wrong\n',
        'UNIX is basically a simple operating system, but you have to be a genius to understand the simplicity\n',
        'Ethernet (n): something used to catch the etherbunny\n',
        'C://dos C://dos.run run.dos.run\n',
        "You know it's love when you memorize her IP number to skip DNS overhead\n",
        'JUST SHUT UP AND REBOOT!!\n',
        '1f u c4n r34d th1s u r34lly n33d t0 g37 l41d\n',
        "Alcohol & calculus don't mix. Never drink & derive\n",
        'How do I set a laser printer to stun?\n',
        'There is only one satisfying way to boot a computer\n',
        'Concept: On the keyboard of life, always keep one finger on the escape button\n',
        "It's not bogus, it's an IBM standard\n",
        'Be nice to the nerds, for all you know they might be the next Bill Gates!\n',
        'The farther south you go, the more dollar stores there are\n',
        'Beware of programmers that carry screwdrivers\n',
        (
            'The difference between e-mail and regular mail is that computers handle e-mail, and computers never decide'
            ' to come to work one day and shoot all the other computers\n'),
        (
            "If you want a language that tries to lock up all the sharp objects and fire-making implements, use Pascal "
            "or Ada: the Nerf languages, harmless fun for children of all ages, and they won't mar the furniture\n"),
        'COFFEE.EXE Missing - Insert Cup and Press Any Key\n',
        (
            'Programming today is a race between software engineers striving to build bigger and better idiot-proof '
            'programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning\n'),
        'LISP = Lots of Irritating Silly Parentheses\n',
        (
            "The beginning of the programmer's wisdom is understanding the difference between getting program to run"
            " and having a runnable program\n"),
        "Squash one bug, you'll see ten new bugs popping\n",
        'Everytime i time i touch my code, i give birth to ten new bugs\n',
        'boast = blogging is open & amiable sharing of thoughts\n',
        (
            'We are sorry, but the number you have dialed is imaginary. '
            'Please rotate your phone 90 degrees and try again\n'),
        'Cannot find REALITY.SYS. Universe halted\n',
        "If it weren't for C, we'd all be programming in BASI and OBO\n",
        'Bad command or file name! Go stand in the corner\n',
        'Bad or corrupt header, go get a haircut\n',
        'Unrecognized input, get out of the class\n',
        'Warning! Buffer overflow, close the tumbler !\n',
        'WinErr 547: LPT1 not found... Use backup... PENCIL & PAPER\n',
        'Bad or missing mouse driver. Spank the cat? (Y/N)\n',
        'Computers make very fast, very accurate mistakes\n',
        'Best file compression around: "rm *.*" = 100% compression\n',
        'Hackers in hollywood movies are phenomenal. All they need to do is "c:\\> hack into fbi"\n',
        'BREAKFAST.COM Halted...Cereal Port Not Responding\n',
        'I survived an NT installation\n',
        'The name is Baud......James Baud\n',
        'My new car runs at 56Kbps\n',
        'Why doesn\'t DOS ever say "EXCELLENT command or filename!"\n',
        'File not found. Should I fake it? (Y/N)\n',
        "Cannot read data, leech the next boy's paper? (Y/N)\n",
        'CONGRESS.SYS Corrupted: Re-boot Washington D.C (Y/n)?\n',
        'Does fuzzy logic tickle?\n',
        (
            'Helpdesk : Sir, you need to add 10GB space to your HD , '
            'Customer : Could you please tell where I can download that?\n'),
        'Windows: Just another pane in the glass\n',
        "Who's General Failure & why's he reading my disk?\n",
        'RAM disk is not an installation procedure\n',
        'Shell to DOS...Come in DOS, do you copy? Shell to DOS...\n',
        'The truth is out there...anybody got the URL?\n',
        'Smash forehead on keyboard to continue.....\n',
        'E-mail returned to sender -- insufficient voltage\n',
        "Help! I'm modeming... and I can't hang up!!!\n",
        'All wiyht. Rho sritched mg kegtops awound?\n',
        'Once I got this error on my Linux box: Error. Keyboard not attached. Press F1 to continue\n',
        (
            "Once I got this error on my Linux box: Error. Mouse not attached. "
            "Please left click the 'OK' button to continue\n"),
        'Press any key to continue or any other key to quit...\n',
        'Press every key to continue\n',
        (
            "Helpdesk: Sir if you see the blue screen, press any key to continue. "
            "Customer : hm.. just a min.. where's that 'any key'..\n"),
        'Idiot, Go ahead, make my data!\n',
        'Old programmers never die; they just give up their resources\n',
        'To err is human - and to blame it on a computer is even more so\n',
        '(001) Logical Error CLINTON.SYS: Truth table missing\n',
        'Clinton:/> READ | PARSE | WRITE | DUMP >> MONKIA.SYS\n',
        '(D)inner not ready: (A)bort (R)etry (P)izza\n',
        'Computers can never replace human stupidity\n',
        'A typical Yahoo! inbox : Inbox(0), Junk(9855210)\n',
        '(A)bort, (R)etry, (P)anic?\n',
        'Bugs come in through open Windows\n',
        'Penguins love cold, they wont survive the sun\n',
        'Unix is user friendly...its just selective about who its friends are\n',
        'Artificial intelligence usually beats real stupidity\n',
        'Bell Labs Unix -- Reach out and grep someone.\n',
        'To err is human...to really foul up requires the root password.\n',
        'Invalid password : Please enter the correct password to (Abort / Retry / Ignore )\n',
        'FUBAR - where Geeks go for a drink\n',
        "I degaussed my girlfriend and I'm just not attracted to her anymore\n",
        'Scandisk : Found 2 bad sectors. Please enter a new HD to continue scanning\n',
        'Black holes are where God divided by zero\n',
        'Hey! It compiles! Ship it!\n',
        'Thank god, my baby just compiled\n',
        'Yes! My code compiled, and my wife just produced the output\n',
        'Windows 98 supports real multitasking - it can boot and crash simultaneously\n',
        'Zap! And there was the blue screen !\n',
        'Please send all spam to my main address, root@localhost :-)\n',
        'MailerD(a)emon: You just received 9133547 spam. (O)pen all, (R)ead one by one, (C)heck for more spam\n',
        "A: Can you teach me how to use a computer? B: No. I just fix the machines, I don't use them\n",
        'PayPal: Your funds have been frozen for 668974 days\n',
        '1-800-404 : The subscriber you are trying to call does not exist\n',
        '1-800-403 : Access to that subscriber was denied\n',
        'Error message: "Out of paper on drive D:"\n',
        "If I wanted a warm fuzzy feeling, I'd antialias my graphics!\n",
        'A printer consists of three main parts: the case, the jammed paper tray and the blinking red light\n',
        '"Mr. Worf, scan that ship." "Aye Captain. 300 dpi?"\n',
        'Smith & Wesson: The Original Point And Click Interface\n',
        'Shout onto a newsgroup : It echoes back flames and spam\n',
        'Firewall : Intruder detected. (A)llow in (D)eactivate the firewall\n',
        'Real programmers can write assembly code in any language\n',
        'Warning! Perl script detected! (K)ill it , (D)eactivate it\n',
        'Firewall : Do you want to place a motion detector on port 80 ?\n',
        'Helpdesk: Sir, please refill your ink catridges Customer : Where can i download that?\n',
        'All computers run at the same speed... with the power off\n',
        'You have successfully logged in, Now press any key to log out\n',
        'Sorry, the password you tried is already being used by Dorthy, please try something else.\n',
        'Sorry, that username already exists. (O)verwrite it (C)ancel\n',
        'Please send all flames, trolls, and complaints to /dev/toilet\n',
        "Shut up, or i'll flush you out\n",
        'Cron : Enter cron command \\ Now enter the number of minutes in an hour\n',
        'We are experiencing system trouble -- do not adjust your terminal\n',
        'You have successfully hacked in, Welcome to the FBI mainframes.\n',
        "I'm sorry, our software is perfect. The problem must be you\n",
        'Never underestimate the bandwidth of a station wagon full of tapes hurling down the highway\n',
        'Webhost livehelp: Sir you ran out of bandwidth, User: Where can I download that?\n',
        "If Ruby is not and Perl is the answer, you don't understand the question\n",
        'Having soundcards is nice... having embedded sound in web pages is not\n',
        'My computer was full, so I deleted everything on the right half\n',
        'You have received a new mail which is 195537 hours old\n',
        'Yahoo! Mail: Your email was sent successfully. The email will delivered in 4 days and 8 hours\n',
        "I'm sorry for the double slash (Tim Berners-Lee in a Panel Discussion, WWW7, Brisbane, 1998)\n",
        'Ah, young webmaster... java leads to shockwave. '
        'Shockwave leads to realaudio. And realaudio leads to suffering\n',
        'What color do you want that database?\n',
        "C++ is a write-only language. I can write programs in C++, but I can't read any of them\n",
        'As of next week, passwords will be entered in Morse code\n',
        'earth is 98% full ... please delete anyone you can\n',
        'A typical yahoo chat room: "A has signed in, A has signed out, '
        'B has signed in, B has signed out, C has signed in, C has signed out.."_\n',
        'When someone says "I want a programming language in which '
        'I need only say what I wish done," give him a lollipop\n',
        'Warning! No processor found! Press any key to continue\n',
        'Failure is not an option. It comes bundled with your Microsoft product\n',
        'NT is the only OS that has caused me to beat a piece of hardware to death with my bare hands\n',
        'Warning! Kernel crashed, Run for your lives !\n',
        'NASA uses Windows? Oh great. If Apollo 13 went off course today '
        'the manual would just tell them to open the airlock, flush the astronauts out, and re-install new one\n',
        'JavaScript: An authorizing language designed to make Netscape crash\n',
        "How's my programming? Call 1-800-DEV-NULL\n",
        'Yes, friends and neighbors, boys and girls - my PC speaker crashed NT\n',
        "root:> Sorry, you entered the wrong password, the correct password is 'a_49qwXk'\n",
        'New linux package released. Please install on /dev/null\n',
        'Quake and uptime do not like each other\n',
        'Unix...best if used before: Tue Jan 19 03:14:08 GMT 2038\n',
        'As you well know, magic and weapons are prohibited inside the cafeteria -- Final Fantasy VIII\n',
        'Man is the best computer we can put aboard a spacecraft...'
        'and the only one that can be mass produced with unskilled labo\n',
        'Unix is the only virus with a command line interface\n',
        'Windows 95 makes Unix look like an operating system\n',
        "How are we supposed to hack your system if it's always down!\n",
        'God is real, unless declared integer\n',
        "I'm tempted to buy the slashdot staff a grammar checker. What do they do for 40 hours a week?\n",
        'Paypal : Please enter your credit card number to continue\n',
        'It takes a million monkeys at typewriters to write Shakespeare, '
        'but only a dozen monkeys at computers to run Network Solutions\n',
        'Please help - firewall burnt down - lost packet - reward $$$\n',
        'If Linux were a beer, it would be shipped in open barrels so that anybody could piss in it before delivery\n',
        'Thank you Mario! But our princess is in another castle\n',
        'Perl, the only language that looks the same before and after RSA encryption\n',
        'Norton: Incoming virus - (D)ownload and save (R)un after download\n',
        "I had a dream... and there were 1's and 0's everywhere, and I think I saw a 2!\n",
        'You sir, are an unknown USB device driver\n',
        "C isn't that hard: void (*(*f[])())() defines f as an array of unspecified size, "
        "of pointers to functions that return pointers to functions that return void\n"]
    showinfo(';-)', random.choice(joke_txt))
    return


def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
    The Savitzky-Golay filter removes high frequency noise from data.
    It has the advantage of preserving the original shape and
    features of the signal better than other types of filtering
    approaches, such as moving averages techniques.
    Parameters
    ----------
    y : array_like, shape (N,)
        the values of the time history of the signal.
    window_size : int
        the length of the window. Must be an odd integer number.
    order : int
        the order of the polynomial used in the filtering.
        Must be less then `window_size` - 1.
    deriv: int
        the order of the derivative to compute (default = 0 means only smoothing)
    Returns
    -------
    ys : ndarray, shape (N)
        the smoothed signal (or it's n-th derivative).
    Notes
    -----
    The Savitzky-Golay is a type of low-pass filter, particularly
    suited for smoothing noisy data. The main idea behind this
    approach is to make for each point a least-square fit with a
    polynomial of high order over a odd-sized window centered at
    the point.
    Examples
    --------
    t = np.linspace(-4, 4, 500)
    y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
    ysg = savitzky_golay(y, window_size=31, order=4)
    import matplotlib.pyplot as plt
    plt.plot(t, y, label='Noisy signal')
    plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
    plt.plot(t, ysg, 'r', label='Filtered signal')
    plt.legend()
    plt.show()
    References
    ----------
    .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
       Data by Simplified Least Squares Procedures. Analytical
       Chemistry, 1964, 36 (8), pp 1627-1639.
    .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
       W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
       Cambridge University Press ISBN-13: 9780521880688
    """
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order + 1)
    half_window = (window_size - 1) // 2
    # precompute coefficients
    b = np.mat([[k ** i for i in order_range] for k in range(-half_window, half_window + 1)])
    m = np.linalg.pinv(b).A[deriv] * rate ** deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs(y[1:half_window + 1][::-1] - y[0])
    lastvals = y[-1] + np.abs(y[-half_window - 1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve(m[::-1], y, mode='valid')


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Multigraph')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        self.fra = tk.Frame(self, width=660, height=525)
        self.fra.grid(row=0, column=0, padx=5, pady=5)
        fra2 = tk.Frame(self)
        fra2.grid(row=1, column=0, pady=10)
        self.tx = tk.Text(fra2, width=80, height=8)
        scr = tk.Scrollbar(fra2, command=self.tx.yview)
        self.tx.configure(yscrollcommand=scr.set, state='disabled')
        self.tx.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu()

    def menu(self):
        m = tk.Menu(self)  # создается объект Меню на главном окне
        self.config(menu=m)  # окно конфигурируется с указанием меню для него
        fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Файл', menu=fm)
        # формируется список команд пункта меню
        fm.add_command(label='Открыть XVG', command=self.xvg_open)
        fm.add_command(label='Сохранить статистику', command=self.save_stat)
        fm.add_command(label='Сохранить график', command=self.save_graph)
        fm.add_command(label='Выход', command=self.close_win)
        rm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Настройки', menu=rm)
        rm.add_command(label='Сброс', command=self.sbros)
        rm.add_command(label='Легенда', command=self.legend_set)
        rm.add_command(label='Сетка', command=self.grid_set)
        rm.add_command(label='Сглаживание', command=self.smoth_set)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация', 'Отображение графиков по данным xvg-файлов')


class Graph(Gui):
    def __init__(self):
        super().__init__()
        self.legend = False
        self.grid = False
        self.smoth = False
        self.fig = None
        self.headers = []
        self.nparrays = []
        self.files = []

    @staticmethod
    def convert(s):
        if s != ' ':
            s = s.strip()
            trans = {r' ': r'\ ', r'\xx\f{}': r'\xi ', r'\xl\f{}': r'\lambda ', r'\xD\f{}': r'\Delta '}
            for grace, tex in trans.items():
                s = s.replace(grace, tex)
            s = re.sub(r'\\S([^\\]+)\\N', r'^{\1}', s)
        else:
            s = r'\ '
        s = '$' + s + '$'
        return s

    def xvg_stat(self, x, y, lab):
        """Большая ложь т.е. статистика"""
        y_min = min(y)
        y_max = max(y)
        y_mean = y.mean()
        x_min = x[np.argmin(y)]
        x_max = x[np.argmax(y)]
        self.tx.configure(state='normal')
        self.tx.insert(tk.END, 'Статистика для {0:s}:'.format(
            lab) + '\nМинимальное значение y = {0:.3f} при x = {1:.2f}'.format(
            y_min, x_min) + '\nМаксимальное значение y = {0:.3f} при x = {1:.2f}'.format(
            y_max, x_max) + '\nСреднее значение y = {0:.3f}'.format(
            y_mean) + '\nСтандартное отклонение y = {0:.3f}'.format(
            np.std(y)) + '\nКвартили: y (25%) = {0:.3f}, y (50%) = {1:.3f}, y (75%) = {2:.3f}\n\n'.format(
            np.percentile(y, 25), np.percentile(y, 50), np.percentile(y, 75)))
        self.tx.configure(state='disabled')

    def save_stat(self):
        opt = {'filetypes': [('Текстовые файлы', ('.txt', '.TXT')), ('Все файлы', '.*')]}
        sa = asksaveasfilename(**opt)
        if sa:
            letter = self.tx.get(1.0, tk.END)
            try:
                with open(sa, 'w') as f:
                    f.write(letter)
            except FileNotFoundError:
                pass

    def cmd_open(self):
        for n in range(len(sys.argv) - 1):
            xvg_file = sys.argv[n + 1]
            if not xvg_file:
                return
            try:
                fname = open(xvg_file, 'r')
                n = 0
                header = []
                for line in fname:
                    if (line[0] == '@') or (line[0] == '#'):
                        header.append(line)
                        n += 1
                fname.close()
                with open(xvg_file, 'r') as fname:
                    nparray = np.loadtxt(fname, skiprows=n)
                if not header:
                    header = "Header not found"
                self.nparrays.append(nparray)
                self.files.append(xvg_file)
                self.headers.append(header)
                print('Информация:\nСтолбцов данных: {0:d}\nCтрок данных: {1:d}\nНомер графика: {2:d}'.format(
                    nparray.shape[1], nparray.shape[0], len(self.nparrays)))
            except UnicodeDecodeError:
                continue
            except ValueError:
                continue
            try:
                self.print_graph()
            except AttributeError:
                pass

    def xvg_open(self):
        opt = {'filetypes': [
            ('Файлы XVG', ('.xvg', '.XVG')), ('Все файлы', '.*')]}
        xvg_file = askopenfilename(**opt)
        if not xvg_file:
            return
        try:
            fname = open(xvg_file, 'r')
            n = 0
            header = []
            for line in fname:
                if (line[0] == '@') or (line[0] == '#'):
                    header.append(line)
                    n += 1
            fname.close()
            with open(xvg_file, 'r') as fname:
                nparray = np.loadtxt(fname, skiprows=n)
            if not header:
                header = "Header not found"
            self.nparrays.append(nparray)
            self.files.append(xvg_file)
            self.headers.append(header)
            showinfo('Информация', 'Столбцов данных: {0:d}\nCтрок данных: {1:d}\nНомер графика: {2:d}'.format(
                nparray.shape[1], nparray.shape[0], len(self.nparrays)))
        except UnicodeDecodeError:
            showerror('Ошибка!', 'Неверный формат файла!')
            return
        except ValueError:
            showerror('Ошибка!', 'Неверный формат файла!')
            return
        try:
            self.print_graph()
        except AttributeError:
            pass

    def labels(self):
        label, subtitle, name_x, name_y = ' ', ' ', ' ', ' '
        for line in self.headers[0]:
            if line.find(' title ') != -1:
                i = line.index('"')
                j = line.rindex('"')
                label = line[i + 1:j]
            elif line.find(' subtitle ') != -1:
                i = line.index('"')
                j = line.rindex('"')
                subtitle = line[i + 1:j]
            elif line.find(' xaxis  label ') != -1:
                i = line.index('"')
                j = line.rindex('"')
                name_x = line[i + 1:j]
            elif line.find(' yaxis  label ') != -1:
                i = line.index('"')
                j = line.rindex('"')
                name_y = line[i + 1:j]
        return label, subtitle, name_x, name_y

    def legend_set(self):
        self.legend = bool(askyesno('Техническая легенда', 'Отобразить?'))
        try:
            self.print_graph()
        except AttributeError:
            pass

    def grid_set(self):
        self.grid = bool(askyesno('Cетка', 'Отобразить?'))
        try:
            self.print_graph()
        except AttributeError:
            pass

    def smoth_set(self):
        self.smoth = bool(askyesno('Сглаживание по Савицкому-Голаю', 'Отобразить?'))
        try:
            self.print_graph()
        except AttributeError:
            pass

    def print_graph(self):
        if self.headers is None:
            return
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.tx.configure(state='normal')
        self.tx.delete('1.0', tk.END)
        self.tx.configure(state='disabled')
        self.fig = Figure()
        self.fig.suptitle(self.convert(self.labels()[0]), style='oblique', fontsize=16, fontweight='bold')
        ax = self.fig.add_subplot(111)
        if self.labels()[1] != ' ':
            ax.set_title(self.convert(self.labels()[1]))
        ax.set_xlabel(self.convert(self.labels()[2]))
        ax.set_ylabel(self.convert(self.labels()[3]))
        ax.grid(self.grid)
        for i, nparray in enumerate(self.nparrays):
            legends = []
            name_fail = " "
            for line in self.headers[i]:
                if line.find('legend "') != -1:
                    k = line.index('"')
                    l = line.rindex('"')
                    legend = self.convert(line[k + 1:l])
                    legends.append(legend)
                if line.find('yaxis  label') != -1:
                    o = line.index('"')
                    p = line.rindex('"')
                    name_fail = self.convert(line[o + 1:p])
            num_f_leg = nparray.shape[1] - len(legends) - 1
            num_empty_leg = 1
            while nparray.shape[1] - len(legends) - 1:
                if num_f_leg == 1:
                    legends.append(name_fail)
                else:
                    legends.append(name_fail + '_' + str(num_empty_leg))
                    num_empty_leg += 1
            x = nparray[:, 0]
            for j in range(0, nparray.shape[1] - 1):
                y = nparray[:, j + 1]
                if len(self.nparrays) == 1:
                    lab = legends[j]
                else:
                    lab = os.path.splitext(os.path.basename(self.files[i]))[0] + ':' + legends[j]
                ax.plot(x, y, label=lab)
                self.xvg_stat(x, y, lab)
                if self.smoth:
                    ysg = savitzky_golay(y, window_size=31, order=4)
                    ax.plot(x, ysg, label=lab + r'$\ filtered$')
        if self.legend:
            ax.legend(loc='best', frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fra)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.fra)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

    def sbros(self):
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.legend = True
        self.grid = False
        self.nparrays = []
        self.files = []
        self.fig = None
        self.headers = []
        self.tx.configure(state='normal')
        self.tx.delete('1.0', tk.END)
        self.tx.configure(state='disabled')

    def save_graph(self):
        if self.fig is None:
            showerror('Ошибка!', 'График недоступен!')
            return
        sa = asksaveasfilename()
        if sa:
            try:
                self.fig.savefig(sa, dpi=600)
            except FileNotFoundError:
                pass
            except AttributeError:
                showerror('Ошибка!', 'График недоступен!')
            except ValueError:
                showerror('Неподдерживаемый формат файла рисунка!',
                          'Поддреживаемые форматы: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff.')


def win():
    graph = Graph()
    joke()
    if len(sys.argv) > 1:
        graph.cmd_open()
    graph.mainloop()


if __name__ == '__main__':
    win()
