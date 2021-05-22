# -*- coding: utf-8 -*-
import sqlite3
import random
from sqlite3 import Error
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from gtts import gTTS
import os
from playsound import playsound
import os.path
from pathlib import Path
from os import listdir
from os.path import isfile, join
from random import randrange
import time
import googletrans
from googletrans import Translator
from google_trans_new import google_translator
from tkinter import ttk
from tkinter.messagebox import showinfo

####DO ZROBIENIA:
    #konwersja mp3 do bitow, zeby nie zapisywac
    #wybor kazdego jezyka swiata
    #zaznaczanie niewlasciwych tlumaczen

listajezykow = googletrans.LANGUAGES
print(googletrans.LANGUAGES)


values = listajezykow.values()
values_list = list(values)
print(values_list)


translator = google_translator()
translate_text = translator.translate('Hola mundo!', lang_src='nl', lang_tgt='en')
print(translate_text)


class gierka:
    language = 'nl'



    def random_line():
        mypath = "img/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        a = random.choice(onlyfiles)
        b = os.path.splitext(a)[0]

        #stare i chujowe, to wyzej bierze z nazwy jotpegow
        #lines = open('dodane.txt').read().splitlines()
       # myline = random.choice(lines)
       # print(myline)
        return b

            #wyjebalem sejwowanie jako osobne pliki, teraz sejwuje jako jeden tymczasowy i usuwa i dziala w kazdym jezyku
    def tts(slowko, jezyk):
        jezyk = gierka.language
        gierka.mytext = translator.translate(slowko, lang_src='nl', lang_tgt=jezyk.format())
        #return

        if jezyk == 'en':
            gierka.mytext = translator.translate(slowko, lang_src='nl', lang_tgt='en')

        if jezyk == 'de':
            gierka.mytext = translator.translate(slowko, lang_src='nl', lang_tgt='de')

        if jezyk == 'nl':
            gierka.mytext = slowko

        if jezyk == 'pl':
            gierka.mytext = translator.translate(slowko, lang_src='nl', lang_tgt='pl')


        #mytext = slowko
        ####BARDZO WAZNE PONIZEJ USUNAC KOMENTARZ
        #language = 'nl'
        #if gierka.language == 'en':
        #print(gierka.mytext)


        #adres = ('sounds/{}.mp3'.format(gierka.mytext))
        adres = 'sounds/rozwiazanie.mp3'.format()
        myobj = gTTS(text=gierka.mytext, lang=gierka.language, slow=False)
        #if os.path.isfile(adres) == False:
        #    print('yo')

    #    my_file = Path("{}".format(adres))
    #    if my_file.exists() == False:
     #       myobj.save(adres)
     #       print('ks')
        myobj.save(adres)

        # file exists
        playsound(adres)
        os.remove(adres)


    #def klik():
     #   for widget in frame.winfo_children():
      #      widget.destroy()
       # frame.pack_forget()
        #okienko()


    def okienko():
        #global czy
       # def klik():
      #      for widget in frame.winfo_children():
      #          widget.destroy()
       #     frame.pack_forget()
            #okienko()

        window = Tk()
        def lewy():
            if gierka.czy == 0:
                n = 'Ja, super!'
                gierka.tts(n, gierka.language)
                gierka.czy = None
                ramka()
                return

            if gierka.czy == 1:
                n = 'Nee. Probeer opnieuw'
                gierka.tts(n, gierka.language)
                return


        def prawy(event=None):

            if gierka.czy == 1:
                #global czy
                n = 'Ja, super!'
                gierka.tts(n, gierka.language)
                gierka.czy = None
                ramka()
                return
                #okienko()

            if gierka.czy == 0:

                n = 'Nee. Probeer opnieuw'
                gierka.tts(n, gierka.language)
                return


       # def losowanieslow():

        #    a = gierka.random_line()
         #   a2 = gierka.random_line()
          #  if a2 == a:
           #     a2 = gierka.random_line()
            #if a2 == a:
             #   a2 = gierka.random_line()
            #if a2 == a:
             #   a2 = gierka.random_line()
           # if a2 == a:
            #    a2 = gierka.random_line()

          #  ktoreslowko = randrange(2)
          #  print(randrange(2))
           # return a,a2,ktoreslowko

        def setanylanguage():
            gierka.language = value_to_key(cb.get())
            print(gierka.language)
            ramka()
            return

        def setnl():
            gierka.language = 'nl'
            ramka()
            return

        def setang():
            gierka.language = 'en'
            ramka()
            return

        def setde():
            gierka.language = 'de'
            ramka()
            return

        def setpl():
            gierka.language = 'pl'
            ramka()
            return

        def ramka():
            ktoreslowko = randrange(2)
            print(randrange(2))

            gierka.czy = ktoreslowko

            #self.czy = None
            frame = Frame(window)
            for widget in frame.winfo_children():
                widget.destroy()
            frame.place_forget()
            #frame.grid_forget()
            frame.place(x=20, y=50)
            a=gierka.random_line()

            #obrazekLabel2.unbind('<Button-1>')


            slowkoLabel = Label(frame, text='{}'.format(a))
            slowkoLabel.grid(row=2, column=1)


            image = Image.open("img/{}.jpg".format(a))
            image = image.resize((250, 250), Image.ANTIALIAS)
            obrazek = ImageTk.PhotoImage(image)

            ###teraz zamiast tego jest button
            obrazekLabel = Label(frame, image=obrazek)
            obrazekLabel.image = obrazek
                #linia ponizej jako komentarz (test)
            obrazekLabel.grid(row=1, column=1)

            lewyButton = Button(window, text='LEWY', image=obrazek, command=lewy)
            lewyButton.grid(row=3, column=1)



            a2 = gierka.random_line()
            if a2 == a:
                a2 = gierka.random_line()
            if a2 == a:
                a2 = gierka.random_line()
            if a2 == a:
                a2 = gierka.random_line()
            if a2 == a:
                a2 = gierka.random_line()

            slowkoLabel2 = Label(frame, text='{}'.format(a2))
            slowkoLabel2.grid(row=2, column=2)

            image2 = Image.open("img/{}.jpg".format(a2))
            image2 = image2.resize((250, 250), Image.ANTIALIAS)
            obrazek2 = ImageTk.PhotoImage(image2)

            #####teraz zamiast tego jest button
            obrazekLabel2 = Label(frame, image=obrazek2)
            obrazekLabel2.image = obrazek2
                ###linia ponizej dodana jako komentarz (test)
            obrazekLabel2.grid(row=1, column=2)
            #obrazekLabel2.bind('<Button-1>', prawy)

            prawyButton = Button(window, text='PRAWY', image=obrazek2, command=prawy)
            prawyButton.grid(row=3, column=2)

            if ktoreslowko == 0:
                gierka.tts(a, gierka.language)
            if ktoreslowko == 1:
                gierka.tts(a2, gierka.language)

            #gierka.czy = None
           # obrazekLabel2.bind(on_click)
            #time.sleep(5)



            #def czydobrze(ccc):
               # return




            ######button przeniesiony na dol, zeby z kompa dalo sie lepiej grac
        #nastepnyButton = Button(window, text='nastepny')
        nastepnyButton = Button(window, text='niderlandzki', command=setnl)
        nastepnyButton.place(x=300, y=360)

        nastepnyButtonAngielski = Button(window, text='angielski', command=setang)
        nastepnyButtonAngielski.place(x=380, y=360)

        nastepnyButtonEs = Button(window, text='niemiecki', command=setde)
        nastepnyButtonEs.place(x=460, y=360)

        nastepnyButtonPl = Button(window, text='polski', command=setpl)
        nastepnyButtonPl.place(x=560, y=360)

        nastepnyButtonAny = Button(window, text='Come on nigga', command=setanylanguage)
        nastepnyButtonAny.place(x=560, y=500)

        #cb = ttk.Combobox(window, values=[ "January","February","March", "April"])

        selected_language = tkinter.StringVar()

        cb = ttk.Combobox(window, textvariable=selected_language)
        cb['values'] = values_list
        cb.place(x=500, y=420)

        def month_changed(event):
            msg = f'You selected {cb.get()}!'
            showinfo(title='Result', message=msg)

        def language_changed(event):
            gierka.language_value = f'{cb.get()}'
            print(gierka.language_value)
            value_to_key(gierka.language_value)

        def value_to_key(a):
            for key, value in listajezykow.items():
                if value == a:
                    print(key)
                    return key

        #cb.bind('<<ComboboxSelected>>', month_changed)
        cb.bind('<<ComboboxSelected>>', language_changed)

        print(cb.get())
      ##  search_age = cb.get()
        #for name, age in listajezykow.items():
         #   if age == search_age:
          #      print(name)


        #ramka()







       # load = Image.open("img/aap.jpg")
        #render = ImageTk.PhotoImage(load)
       # img = Label(self, image=render)
       # img.image = render
       # img.place(x=0, y=0)

        window.title("Nauka slowek dla dzieci")
        window.geometry('800x600')
        window.mainloop()
    def wpisywanie():
        lan_1: str = input("Slowko po holendersku:")
        lan_2: str = input("Slowko po polsku:")
        rzecz: str = input("Jaka to czesc mowy?")



    #do sprawdzenia ta funkcja
    def wprowadz_slowo(slowa):
        database = r"C:\sqlite\db\kid.db"
        conn = create_connection(database)

        sql = ''' INSERT INTO words (language_1,language_2,language_3,adding_date,rzeczownik,category)
                  VALUES(?,?,?,?,?,?) '''

        cur = conn.cursor()
        cur.execute(sql, slowa)
        conn.commit()
        conn.close()
        #print('                     Liczba dzisiaj dodanych slowek: ', ile_dodanych_dzis())
        return cur.lastrowid

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(conn, create_words_table):
        """ create a table from the create_table_sql statement
        :param create_words_table:
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_words_table)
        except Error as e:
            print(e)


    def main():

        database = r"C:\sqlite\db\kid.db"
        create_words_table = """ CREATE TABLE IF NOT EXISTS words (
                                            id integer PRIMARY KEY,
                                            language_1 text,
                                            language_2 text,
                                            sentence_1 text,
                                            sentence_2 text,
                                            sound1 text,
                                            sound2 text,
                                            sound3 text,
                                            sound4 text,
                                            language_5 text,
                                            category text,
                                            pic1 text,
                                            pic2 text,
                                            movie1 text,
                                            movie2 text,
                                            rzeczownik text,
                                            irregular_verb text,
                                            adding_date text,
                                            taken_from_language text
                                        ); """
        algorytm = """ CREATE TABLE IF NOT EXISTS algorytm (
                                                id integer PRIMARY KEY,
                                                id_slowka integer,
                                                prawidlowo integer,
                                                nieprawidlowo integer,
                                                ile_poprawnych_z_rzedu integer,
                                                nauczone text,
                                                data_nauczenia text,
                                                i_p_z_rz_2 integer,
                                                utrwalone text,
                                                data_utrwalenia text,
                                                ostatecznie_utrwalone text,
                                                data_ostatecznego text
                                            ); """

        user = """ CREATE TABLE IF NOT EXISTS user (
                                                id integer PRIMARY KEY,
                                                data text,
                                                ile_razy integer,
                                                prawidlowo integer,
                                                nieprawidlowo integer,
                                                ile_poprawnych_z_rzedu_temp integer,
                                                ile_poprawnych_max integer,
                                                ile_nauczonych text
                                            ); """

        conn = gierka.create_connection(database)

        if conn is not None:
            gierka.create_table(conn, create_words_table)
            gierka.create_table(conn, algorytm)
            gierka.create_table(conn, user)
            #test()
            #random_line()
            #tts('heb je honger')
            gierka.okienko()

        else:
            print("Error! cannot create the database connection.")




if __name__ == '__main__':
    gierka.main()
