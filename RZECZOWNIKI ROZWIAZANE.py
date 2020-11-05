import sqlite3
import random
from sqlite3 import Error
from typing import List
from datetime import date
from datetime import datetime

import sys
sys.setrecursionlimit(6000)

#def staty():
    #czas sesji, procent poprawnych, ilosc nauczonych, ilosc nienauczonych w bazie, ile prob,

def ile_nauczonych_dzis():
    database = r"C:\sqlite\db\pythonsqlite211.db"
    data = jakadata()
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM algorytm WHERE data_nauczenia=? ", (data,))
    row = cur.fetchall()
    ile_nauczonych_dzis = len(row)
    return ile_nauczonych_dzis

def ile_dodanych_dzis():
    database = r"C:\sqlite\db\pythonsqlite211.db"
    data = jakadata()
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM words WHERE adding_date=? ", (data,))
    row = cur.fetchall()
    ile_dodanych_dzis = len(row)
    return ile_dodanych_dzis



def czy_nauczone(nr):
# warunki: starsze niz iles, 10 z rzedu dobrze, golden-shot (5 z rzedu dobrze i starsze niz 20 dni)
    id = nr[2][0]
    row_algorytm = odczyt_z_bazy_algorytm(id)

    data_wpisania = nr[2][9]
    format_str = '%d/%m/%Y'  # The format
    po_konwersji_data_wpisania = datetime.strptime(data_wpisania, format_str)
    data_nauczenia = jakadata()
    po_konwersji_data_nauczenia = datetime.strptime(data_nauczenia, format_str)
    diff = po_konwersji_data_nauczenia.date() - po_konwersji_data_wpisania.date()

    ile_pop_z_rzedu = row_algorytm[0][4]
    ile_niepoprawnych = row_algorytm[0][3]
        #kiedy nauczone: starsze niz 2 tyg. i 8 pop. z rzeu, 24 poprawne z rzedu, starsze niz miesiac i 6 pop z rzedu i zero niepop
    if (ile_pop_z_rzedu>6 and diff.days>12) or ile_pop_z_rzedu>23 or (ile_pop_z_rzedu>4 and diff.days>29 and ile_niepoprawnych < 1) :
        return True
    return False



def test():
    czy_nauczone(a)

def losowanie_slowka():
    prawdopodobienstwo = random.randint(1, 8)

    if prawdopodobienstwo == 7:
        min = 0
        max = 1
    if prawdopodobienstwo == 8:
        min = 0
        max = 2
    if prawdopodobienstwo == 1:
        min = 0
        max = 3
    if prawdopodobienstwo == 2:
        min = 3
        max = 7
    if prawdopodobienstwo == 3:
        min = 5
        max = 16
    if prawdopodobienstwo == 4:
        min = 9
        max = 31
    if prawdopodobienstwo == 5:
        min = 16
        max = 56
    if prawdopodobienstwo == 6:
        min = 20
        max = 100
    kszksz = odczyt_z_bazy_algorytm_wlasciwy(min, max)
    if kszksz == None:
        nauka()
        return
    else:
        return kszksz

x = 0
yyy = 0
def nauka():
    global x
    global yyy
    nnn = str(losowanie_slowka())
    jezyk1 = ("language_1")
    jezyk2 = ("language_2")
    a = odczyt_z_bazy(jezyk1, jezyk2, nnn)
    b = random.randint(0,1)
    c = abs(b-1)
    primary_key_slowka = str(a[2][0])
    temp_row_algorytm = odczyt_z_bazy_algorytm(primary_key_slowka)
    #ten caly if ponizej do wyjebania, zostal zastapiony czyms innym, ale niech zostanie, moze do niego wroce
    if temp_row_algorytm == []:
        dane_do_wprowadzenia = [primary_key_slowka, 0, 0, 0, None, None]
        wprowadz_do_bazy_algorytm(dane_do_wprowadzenia)

    x += 1

    wpisane = input(a[b])


    if wpisane.lower() == "wprowadz":
        print('Wprowadz jezyk oraz kategorie. Mozesz dokonac zmiany podczas pracy programu wpisujac "Reset"')
        global z_jakiego_na_jaki_temp
        z_jakiego_na_jaki_temp = z_jakiego_na_jaki()
        global kat
        kat = jaka_to_kategoria()
        glowniejszy()
#tutaj nizej zmienic, zeby bylo wpisane.lower i a[c].lower, ale nie zmeiniam teraz, zeby nie zjebac
    if (a[3] == 'yes') and (a[1].startswith('het ') is True and c == 1 and wpisane.lstrip('de .') == a[1].lstrip('het .')) or (a[1].startswith('de ') is True and c == 1 and wpisane.lstrip('het .') == a[1].lstrip('de .')):

            print('wpisales odwrotnie')
            print('\n', 'Otrzymales 0.5 punktu za niepelna znajomosc rzeczownika. Uzywaj poprawnie DE i HET:', a[c].upper(), '\n')
            print(a[b], ' - ', a[c].upper(), '\n')
            yyy += 1
            czy_nauczone(a)
            temp_row_algorytm = odczyt_z_bazy_algorytm(str(primary_key_slowka))
            temp_row_algorytm[0] = list(temp_row_algorytm[0])
            temp_row_algorytm[0][2] = str(int(temp_row_algorytm[0][2]) + 0.5)
            temp_row_algorytm[0][4] += 0.5
            if czy_nauczone(a) == True:
                korekta_liczby_nauczonych = ile_nauczonych_dzis() + 1
                print('                     Nauczone!')
                print('                     Liczba dzisiaj dodanych slowek: ', ile_dodanych_dzis())
                print('                     Liczba dzisiaj nauczonych slowek:', korekta_liczby_nauczonych)
                temp_row_algorytm[0][6] = jakadata()
                if temp_row_algorytm[0][5] == None:
                    temp_row_algorytm[0][5] = 1
                else:
                    temp_row_algorytm[0][5] += 1
            temp_row_algorytm[0] = tuple(temp_row_algorytm[0])
            dane_do_wprowadzenia = [temp_row_algorytm[0][1], temp_row_algorytm[0][2], temp_row_algorytm[0][3],
                                    temp_row_algorytm[0][4],
                                    temp_row_algorytm[0][5], temp_row_algorytm[0][6]]
            update_bazy_algorytm(dane_do_wprowadzenia)
            if x % 10 == 0:
                print('                     Sprawdzono', x, 'slowek')
                print('                     Poprawnie wpisano', ((yyy * 100) / x), '% slowek')
    elif wpisane == a[c]:
        yyy += 1
        czy_nauczone(a)
        temp_row_algorytm = odczyt_z_bazy_algorytm(str(primary_key_slowka))
        temp_row_algorytm[0] = list(temp_row_algorytm[0])
        temp_row_algorytm[0][2] = str(int(temp_row_algorytm[0][2]) + 1)
        temp_row_algorytm[0][4] += 1
        if czy_nauczone(a) == True:
            korekta_liczby_nauczonych = ile_nauczonych_dzis() + 1
            print('                     Nauczone!')
            print('                     Liczba dzisiaj dodanych slowek: ', ile_dodanych_dzis())
            print('                     Liczba dzisiaj nauczonych slowek:', korekta_liczby_nauczonych)
            temp_row_algorytm[0][6] = jakadata()
            if temp_row_algorytm[0][5] == None:
                temp_row_algorytm[0][5] = 1
            else:
                temp_row_algorytm[0][5] += 1
        temp_row_algorytm[0] = tuple(temp_row_algorytm[0])
        dane_do_wprowadzenia = [temp_row_algorytm[0][1], temp_row_algorytm[0][2], temp_row_algorytm[0][3], temp_row_algorytm[0][4],
                                temp_row_algorytm[0][5], temp_row_algorytm[0][6]]
        update_bazy_algorytm(dane_do_wprowadzenia)
        if x % 10 == 0:
            print('                     Sprawdzono', x, 'slowek')
            print('                     Poprawnie wpisano', ((yyy*100)/x), '% slowek')

    else:
        #if a[7] == 'yes':
           # mystring = "I like chemistry"
          #  if "like" in mystring:
         #       print("Word is in sentence")
        #    else:
       #         print("Word is not in sentence")
        print('\n','ZLE, poprawna odpowiedz to:', a[c].upper(), '\n')
        print( a[b],' - ',a[c].upper(),'\n')
        temp_row_algorytm = odczyt_z_bazy_algorytm(str(primary_key_slowka))
        temp_row_algorytm[0] = list(temp_row_algorytm[0])
        temp_row_algorytm[0][3] += 1
        temp_row_algorytm[0] = tuple(temp_row_algorytm[0])
        dane_do_wprowadzenia = [temp_row_algorytm[0][1], temp_row_algorytm[0][2], temp_row_algorytm[0][3], 0, temp_row_algorytm[0][5], temp_row_algorytm[0][6]]
        update_bazy_algorytm(dane_do_wprowadzenia)
        if x % 10 == 0:
            print('                     Sprawdzono', x, 'slowek')
            print('                     Poprawnie wpisano', ((yyy*100)/x), '% slowek')
        nauka()
        return
    nauka()

def update_bazy_algorytm(alg):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("UPDATE algorytm SET prawidlowo=?,nieprawidlowo=?, ile_poprawnych_z_rzedu=?,nauczone=?,data_nauczenia=? WHERE id_slowka = ?", (alg[1],alg[2],alg[3],alg[4],alg[5],alg[0]))
    conn.commit()
    conn.close()
    return

def wprowadz_do_bazy_algorytm(algorytm):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    sql = ''' INSERT INTO algorytm (id_slowka,prawidlowo,nieprawidlowo,ile_poprawnych_z_rzedu,nauczone,data_nauczenia)
                      VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, algorytm)
    conn.commit()
    conn.close()
    return

def odczyt_z_bazy_algorytm(primary_key_words):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    cur = conn.cursor()
    temp_primary_key = primary_key_words
    cur.execute("SELECT * FROM algorytm WHERE id_slowka=? ", (temp_primary_key,))
    row = cur.fetchall()
    return row

def odczyt_z_bazy_algorytm_wlasciwy(min, max):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM algorytm WHERE ((prawidlowo+nieprawidlowo)<? AND (prawidlowo+nieprawidlowo)>=?) AND (nauczone <1 OR nauczone IS NULL)", (max,min,))
    row = cur.fetchall()
    if len(row) > 0:
        temp_random_row = random.choice(row)
        return temp_random_row[1]
    else:
        nauka()

def odczyt_nauczonego_slowka(min, max):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM algorytm WHERE ((prawidlowo+nieprawidlowo)<? AND (prawidlowo+nieprawidlowo)>=?) AND (nauczone <1 OR nauczone IS NULL)", (max,min,))
    row = cur.fetchall()
    if len(row) > 0:
        temp_random_row = random.choice(row)
        return temp_random_row[1]
    else:
        nauka()

def odczyt_z_bazy(jezyk1, jezyk2, prikey):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM words WHERE "+jezyk1+"=? is not null and "+jezyk2+"=? is not null AND id=?", (jezyk1, jezyk2, prikey))
    rows = cur.fetchone()
    #temp_random_row = random.choice(rows)
    #print(rows)
    temp_random_row = rows
    if temp_random_row is not None:
        slowo_pl = temp_random_row[1]
        slowo_obcy = temp_random_row[2]
        czy_rzecz = temp_random_row[7]
        return slowo_pl, slowo_obcy, temp_random_row, czy_rzecz
    else:
        nauka()

def jaka_to_kategoria():
    global kategoria
    kategoria = input("Jaka to kategoria?")
    if kategoria == (''):
        kategoria = None
    return kategoria

def z_jakiego_na_jaki():
    global z_j_na_j
    z_j_na_j = input("Z jakiego jezyka na jaki? Wprowadz '2to1' dla NL -> PL; Wprowadz '3to1' dla ANG -> PL")
    return z_j_na_j

def sprawdz_czy_to_nl_rzeczownik(wiatrackie_slowo):
    a = wiatrackie_slowo
    c = len(a)
    if c > 3:
        poczatek_de = str(a[0]) + str(a[1]) +str(a[2])
        poczatek_het = str(a[0]) + str(a[1]) + str(a[2]) + str(a[3])
        if poczatek_de.lower() == 'de ' or poczatek_het.lower() == 'het ':
            b = 'yes'
            return b
    return

def jakadata():
    dzisiejszadata = date.today()
    datapokonwersji = dzisiejszadata.strftime("%d/%m/%Y")
    return datapokonwersji

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


create_words_table = """ CREATE TABLE IF NOT EXISTS words (
                                        id integer PRIMARY KEY,
                                        language_1 text,
                                        language_2 text,
                                        language_3 text,
                                        language_4 text,
                                        language_5 text,
                                        category text,
                                        irregular_verb text,
                                        rzeczownik text,
                                        adding_date text,
                                        taken_from_language text
                                    ); """


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

def glowny_ekran():
    if z_jakiego_na_jaki_temp == "2to1":
        lan_2: str = input("Slowko po holendersku:")
        if lan_2.lower() == 'reset':
            main()
        if lan_2.lower() == 'nauka':
            nauka()
        lan_1: str = input("Slowko po polsku:")
        czy_to_rzecz = sprawdz_czy_to_nl_rzeczownik(lan_2)
        confirmation: str = input("Czy slowa zostaly wpisane poprawnie? Wprowadz 'N/n jesli para slow jest nieprawidlowa.")
        if confirmation.lower() == "n":
            print("lipa")
            glowny_ekran()

        else:
            global slowa
            lan_3 = None
            slowa = [lan_1, lan_2, lan_3, jakadata(), czy_to_rzecz, kat]
            return slowa
    if z_jakiego_na_jaki_temp == "3to1":
        lan_3: str = input("Slowko po angielsku:")
        if lan_3.lower() == 'reset':
            main()
        if lan_3.lower() == 'nauka':
            nauka()
        lan_1: str = input("Slowko po polsku:")
        czy_to_rzecz = None
        lan_2 = None

        confirmation: str = input("Czy slowa zostaly wpisane poprawnie?")
        if confirmation.lower() == "n":
            print("lipa")
            glowniejszy()
        else:

            slowa = [lan_1, lan_2, lan_3, jakadata(), czy_to_rzecz , kat]
            return slowa


def wprowadz_slowo(slowa):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)

    sql = ''' INSERT INTO words (language_1,language_2,language_3,adding_date,rzeczownik,category)
              VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, slowa)
    conn.commit()
    conn.close()
    print('                     Liczba dzisiaj dodanych slowek: ', ile_dodanych_dzis())
    return cur.lastrowid




def glowniejszy():
    a = wprowadz_slowo(glowny_ekran())
    dane_do_wprowadzenia = [a, 0, 0, 0, None, None]
    wprowadz_do_bazy_algorytm(dane_do_wprowadzenia)
    glowniejszy()


def main():

    database = r"C:\sqlite\db\pythonsqlite211.db"
    create_words_table = """ CREATE TABLE IF NOT EXISTS words (
                                        id integer PRIMARY KEY,
                                        language_1 text,
                                        language_2 text,
                                        language_3 text,
                                        language_4 text,
                                        language_5 text,
                                        category text,
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

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, create_words_table)
        create_table(conn, algorytm)
        create_table(conn, user)
        #test()
        nauka()

    else:
        print("Error! cannot create the database connection.")




if __name__ == '__main__':
    main()
