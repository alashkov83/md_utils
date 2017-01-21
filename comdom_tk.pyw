#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Nov  1 23:02:39 2016.

@author: lashkov

"""

import abc
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring

import matplotlib
import numpy as np

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from periodictable import formula


def joke():
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
        'Ah, young webmaster... java leads to shockwave. Shockwave leads to realaudio. And realaudio leads to suffering\n',
        'What color do you want that database?\n',
        "C++ is a write-only language. I can write programs in C++, but I can't read any of them\n",
        'As of next week, passwords will be entered in Morse code\n',
        'earth is 98% full ... please delete anyone you can\n',
        'A typical yahoo chat room: "A has signed in, A has signed out, B has signed in, B has signed out, C has signed in, C has signed out.."_\n',
        'When someone says "I want a programming language in which I need only say what I wish done," give him a lollipop\n',
        'Warning! No processor found! Press any key to continue\n',
        'Failure is not an option. It comes bundled with your Microsoft product\n',
        'NT is the only OS that has caused me to beat a piece of hardware to death with my bare hands\n',
        'Warning! Kernel crashed, Run for your lives !\n',
        'NASA uses Windows? Oh great. If Apollo 13 went off course today the manual would just tell them to open the airlock, flush the astronauts out, and re-install new one\n',
        'JavaScript: An authorizing language designed to make Netscape crash\n',
        "How's my programming? Call 1-800-DEV-NULL\n",
        'Yes, friends and neighbors, boys and girls - my PC speaker crashed NT\n',
        "root:> Sorry, you entered the wrong password, the correct password is 'a_49qwXk'\n",
        'New linux package released. Please install on /dev/null\n',
        'Quake and uptime do not like each other\n',
        'Unix...best if used before: Tue Jan 19 03:14:08 GMT 2038\n',
        'As you well know, magic and weapons are prohibited inside the cafeteria -- Final Fantasy VIII\n',
        'Man is the best computer we can put aboard a spacecraft...and the only one that can be mass produced with unskilled labo\n',
        'Unix is the only virus with a command line interface\n',
        'Windows 95 makes Unix look like an operating system\n',
        "How are we supposed to hack your system if it's always down!\n",
        'God is real, unless declared integer\n',
        "I'm tempted to buy the slashdot staff a grammar checker. What do they do for 40 hours a week?\n",
        'Paypal : Please enter your credit card number to continue\n',
        'It takes a million monkeys at typewriters to write Shakespeare, but only a dozen monkeys at computers to run Network Solutions\n',
        'Please help - firewall burnt down - lost packet - reward $$$\n',
        'If Linux were a beer, it would be shipped in open barrels so that anybody could piss in it before delivery\n',
        'Thank you Mario! But our princess is in another castle\n',
        'Perl, the only language that looks the same before and after RSA encryption\n',
        'Norton: Incoming virus - (D)ownload and save (R)un after download\n',
        "I had a dream... and there were 1's and 0's everywhere, and I think I saw a 2!\n",
        'You sir, are an unknown USB device driver\n',
        "C isn't that hard: void (*(*f[])())() defines f as an array of unspecified size, of pointers to functions that return pointers to functions that return void\n"]
    showinfo(';-)', random.choice(joke_txt))
    return


class Gui(metaclass=abc.ABCMeta):
    def __init__(self, root):
        self.root = root
        self.root.minsize(width=925, height=605)
        self.root.maxsize(width=925, height=605)
        fra1 = ttk.Frame(self.root)
        lab1 = ttk.LabelFrame(fra1, text='Первый домен', labelanchor='n', borderwidth=5)
        lab1.grid(row=0, column=0, pady=5, padx=5)
        but1 = ttk.Button(lab1, text='Добавить диапазон а.о.', command=self.seg1)
        but1.grid(row=0, column=0, padx=10)
        but12 = ttk.Button(lab1, text='Сброс', command=self.sbros_1)
        but12.grid(row=0, column=1, padx=10)
        lab2 = ttk.LabelFrame(fra1, text='Второй домен', labelanchor='n', borderwidth=5)
        lab2.grid(row=1, column=0, pady=5, padx=5)
        but2 = ttk.Button(lab2, text='Добавить диапазон а.о.', command=self.seg2)
        but2.grid(row=0, column=0, padx=10)
        but22 = ttk.Button(lab2, text='Сброс', command=self.sbros_2)
        but22.grid(row=0, column=1, padx=10)
        lab3 = ttk.Label(fra1, text='Прогресс:')
        lab3.grid(row=3, column=0, columnspan=4, pady=5)
        s = ttk.Style()
        s.configure('My.TButton', font=('Helvetica', 10), foreground='red')
        but3 = ttk.Button(fra1, text='Остановить!', style='My.TButton', command=self.stop)
        but3.grid(row=2, column=0, columnspan=2, pady=10)
        self.pb = ttk.Progressbar(fra1, orient='horizontal', mode='determinate', length=240)
        self.pb.grid(row=4, column=0, columnspan=2)
        self.fra2 = ttk.Frame(self.root, width=660, height=515)
        fra3 = ttk.Frame(self.root)
        fra1.grid(row=0, column=0)
        self.fra2.grid(row=0, column=1)
        fra3.grid(row=1, column=1)
        self.tx = tk.Text(fra3, width=78, height=5)
        scr = ttk.Scrollbar(fra3, command=self.tx.yview)
        self.tx.configure(yscrollcommand=scr.set)
        self.tx.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)

    @staticmethod
    def about():
        showinfo('Информация', 'Построение зависимости расстояния\nмежду центрами масс доменов белка от времени МД')

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.root.destroy()

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def seg1(self):
        pass

    @abc.abstractmethod
    def seg2(self):
        pass

    @abc.abstractmethod
    def sbros_1(self):
        pass

    @abc.abstractmethod
    def sbros_2(self):
        pass


class App(Gui):
    def __init__(self, root):
        super().__init__(root)
        self.s_array = None
        self.nparray = None
        self.stop_flag = False
        self.run_flag = False
        self.segment_1 = []
        self.segment_2 = []
        self.fig = None
        self.canvas = None
        self.toolbar = None

    def xvg_stat(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет не закончен!')
            return
        if self.nparray is None:
            showinfo('Информация', 'Статистика недоступна')
            return
        try:
            t = self.nparray[:, 0]
            r = self.nparray[:, 1]
        except NameError:
            showinfo('Информация', 'Данные недоступны')
            return
        r_min = min(r)
        r_max = max(r)
        r_mean = r.mean()
        t_min = t[np.argmin(r)]
        t_max = t[np.argmax(r)]
        showinfo('Статистика', 'Минимальное расстояние между доменами равно: {0:.3f} А\nпри t= {1:.2f} пc.'.format(
            r_min, t_min) + '\nМаксимальное расстояние между доменами равно: {0:.3f} А\nпри t= {1:.2f} пc.'.format(
            r_max, t_max) + '\nСреднее расстояние между доменами равно: {0:.3f} А'.format(r_mean))
        self.tx.insert(tk.END, '\nСтатистика:\nМинимальное расстояние между доменами равно: {0:.3f} А\nпри t= {1:.2f} пc.'.format(
            r_min, t_min) + '\nМаксимальное расстояние между доменами равно: {0:.3f} А\nпри t= {1:.2f} пc.'.format(
            r_max, t_max) + '\nСреднее расстояние между доменами равно: {0:.3f} А'.format(r_mean))

    def save_data(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет не закончен!')
            return
        if self.nparray is None:
            showinfo('Информация', 'Данные недоступны')
            return
        try:
            t = self.nparray[:, 0]
            r_a = self.nparray[:, 1]
        except NameError:
            showinfo('Информация', 'Данные недоступны')
            return
        r_n = r_a / 10
        n_nparray = np.column_stack((t, r_n))
        sa = asksaveasfilename()
        if sa:
            try:
                np.savetxt(sa, n_nparray, delimiter='\t', fmt=['%d', '%.3f'])
            except OSError:
                showerror('Ошибка!', 'Не удалось сохранить {0:s}'.format(sa))

    def save_log(self):
        sa = asksaveasfilename()
        if sa:
            letter = self.tx.get(1.0, tk.END)
            try:
                with open(sa, 'w') as f:
                    f.write(letter)
            except FileNotFoundError:
                pass

    def save_graph(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет не закончен!')
            return
        if self.fig is None:
            showerror('Ошибка!', 'График недоступен!')
            return
        sa = asksaveasfilename()
        if sa:
            try:
                self.fig.savefig(sa, dpi=600)
            except FileNotFoundError:
                return
            except AttributeError:
                showerror('Ошибка!', 'График недоступен!')

    def _graph(self):
        self.fig = None
        self.fig = Figure()
        ax = self.fig.add_subplot(111)
        x = self.nparray[:, 0]
        y = self.nparray[:, 1]
        ax.set_title('COM distance vs. time')
        ax.set_ylabel('COM distance, A')
        if (max(x) - min(x)) > 10000:
            ax.set_xlabel('Time, ns')
            x /= 1000
        else:
            ax.set_xlabel('Time, ps')
        ax.plot(x, y, color='black')
        ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fra2)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.fra2)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

    @staticmethod
    def _cmass(str_nparray):
        mass_sum = float(str_nparray[:, 3].sum())
        mx = (str_nparray[:, 3]) * (str_nparray[:, 0])
        my = (str_nparray[:, 3]) * (str_nparray[:, 1])
        mz = (str_nparray[:, 3]) * (str_nparray[:, 2])
        c_mass_x = float(mx.sum()) / mass_sum
        c_mass_y = float(my.sum()) / mass_sum
        c_mass_z = float(mz.sum()) / mass_sum
        return [c_mass_x, c_mass_y, c_mass_z]

    def open_pdb(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        opt = {'filetypes': [('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
        pdb = askopenfilename(**opt)
        try:
            with open(pdb, 'r') as f:
                self.s_array = f.readlines()
        except FileNotFoundError:
            return
        else:
            showinfo('Информация', 'Файл прочитан!')
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.segment_1 = []
        self.segment_2 = []
        showinfo('Внимание', 'Диапазоны а.о. доменов обнулены!')
        self.pb['value'] = 0
        self.pb.update()
        self.fig = None
        self.tx.delete('1.0', tk.END)

    def stop(self):
        if self.run_flag:
            if askyesno('Прервать?', 'Вы точно хотите прервать расчет?'):
                self.stop_flag = True

    def seg1(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        chain_name_1 = askstring('Первый домен', 'Имя цепи: ')
        if chain_name_1 == '' or chain_name_1 is None:
            chain_name_1 = ' '
        r_num_start_1 = askinteger('Первый домен', 'Номер первого а.о.: ')
        r_num_end_1 = askinteger('Первый домен', 'Номер последнего а.о.: ')
        if (r_num_start_1 is None) or (r_num_end_1 is None):
            return
        for s_1 in range(r_num_start_1, r_num_end_1 + 1):
            self.segment_1.append((chain_name_1, s_1))
        print(self.segment_1)

    def seg2(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        chain_name_2 = askstring('Второй домен', 'Имя цепи: ')
        if chain_name_2 == '' or chain_name_2 is None:
            chain_name_2 = ' '
        r_num_start_2 = askinteger('Второй домен', 'Номер первого а.о.: ')
        r_num_end_2 = askinteger('Второй домен', 'Номер последнего а.о.: ')
        if (r_num_start_2 is None) or (r_num_end_2 is None):
            return
        for s_2 in range(r_num_start_2, r_num_end_2 + 1):
            self.segment_2.append((chain_name_2, s_2))
        print(self.segment_2)

    def sbros_1(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        self.segment_1 = []

    def sbros_2(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        self.segment_2 = []

    def trj_cycle(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчет уже идёт!')
            return
        self.run_flag = True
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.tx.delete('1.0', tk.END)
        t_array = []
        r_array = []
        xyzm_array_1 = []
        xyzm_array_2 = []
        self.nparray = None
        self.fig = None
        if self.s_array is None:
            showerror('Ошибка!', 'Не загружен файл!')
            return
        self.pb['maximum'] = len(self.s_array)
        n = 0
        model_flag = False
        self.stop_flag = False
        while n < len(self.s_array):
            s = str(self.s_array[n])
            if s.find('t=') != -1:
                t = float(s[s.find('t=') + 2:-1])
                t_array.append(t)
            elif s[0:5] == 'MODEL':
                model_flag = True
            elif (s[0:6] == 'ATOM  ') and ((s[21], int(s[22:26])) in self.segment_1):
                xyzm_1 = [float(s[30:38]), float(s[38:46]),
                          float(s[46:54]), round(formula(s[76:78]).mass)]
                xyzm_array_1 = np.hstack((xyzm_array_1, xyzm_1))
            elif (s[0:6] == 'ATOM  ') and ((s[21], int(s[22:26])) in self.segment_2):
                xyzm_2 = [float(s[30:38]), float(s[38:46]),
                          float(s[46:54]), round(formula(s[76:78]).mass)]
                xyzm_array_2 = np.hstack((xyzm_array_2, xyzm_2))
            elif s[0:6] == 'ENDMDL' or (s[0:3] == 'END' and model_flag is False):
                try:
                    xyzm_array_1.shape = (-1, 4)
                except AttributeError:
                    showerror('Ошибка!', 'Данные для первого домена не собраны!')
                    showinfo('Внимание', 'Диапазоны а.о. доменов не обнулены!')
                    self.pb['value'] = 0
                    self.pb.update()
                    self.run_flag = False
                    return
                try:
                    xyzm_array_2.shape = (-1, 4)
                except AttributeError:
                    showerror('Ошибка!', 'Данные для второго домена не собраны!')
                    showinfo('Внимание', 'Диапазоны а.о. доменов не обнулены!')
                    self.pb['value'] = 0
                    self.pb.update()
                    self.run_flag = False
                    return
                c_mass_1 = self._cmass(xyzm_array_1)
                c_mass_2 = self._cmass(xyzm_array_2)
                r = (((c_mass_1[0] - c_mass_2[0]) ** 2) + ((c_mass_1[1] -
                                                            c_mass_2[1]) ** 2) + ((c_mass_1[2] -
                                                                                   c_mass_2[2]) ** 2)) ** 0.5
                self.tx.insert(tk.END,
                               'Координаты центра масс первого домена: C1 ({0:.3f} A, {1:.3f} A, {2:.3f} A)'.format(
                                   c_mass_1[0],
                                   c_mass_1[1],
                                   c_mass_1[2]) +
                               '\n' +
                               'второго домена: C2 ({0:.3f} A, {1:.3f} A, {2:.3f} A)'.format(
                                   c_mass_2[0],
                                   c_mass_2[1],
                                   c_mass_2[2]) +
                               '\n' +
                               'расстояние между доменами: {0:.3f} A\n'.format(r))
                r_array.append(r)
                del xyzm_array_1
                del xyzm_array_2
                xyzm_array_1 = []
                xyzm_array_2 = []
                if self.stop_flag:
                    break
            self.pb['value'] = n
            self.pb.update()
            n += 1
        self.run_flag = False
        if len(r_array) > 1:
            if len(t_array) == 0:
                t_array = list(range(0, len(r_array)))
            self.nparray = np.column_stack((t_array, r_array))
            print(self.nparray)
            self._graph()
        elif len(r_array) == 0:
            showerror('Ощибка!', 'Данные не собраны!')
        elif len(r_array) == 1:
            try:
                self.canvas.get_tk_widget().destroy()
            except AttributeError:
                pass
        showinfo('Внимание', 'Диапазоны а.о. доменов не обнулены!')


def win():
    root = tk.Tk()
    root.title('Comdom')
    app = App(root)
    m = tk.Menu(root)  # создается объект Меню на главном окне
    root.config(menu=m)  # окно конфигурируется с указанием меню для него
    fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Файл', menu=fm)
    # формируется список команд пункта меню
    fm.add_command(label='Открыть PDB', command=app.open_pdb)
    fm.add_command(label='Сохранить график', command=app.save_graph)
    fm.add_command(label='Сохранить данные', command=app.save_data)
    fm.add_command(label='Сохранить LOG', command=app.save_log)
    fm.add_command(label='Выход', command=app.close_win)
    rm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Запуск', menu=rm)
    rm.add_command(label='Запуск...', command=app.trj_cycle)
    rm.add_command(label='Статистика', command=app.xvg_stat)
    m.add_command(label='Справка', command=app.about)
    joke()
    root.mainloop()


if __name__ == '__main__':
    win()
