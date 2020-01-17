import sqlite3
import random
from sqlite3 import Error
from typing import List


import sys
sys.setrecursionlimit(6000)

def test():
    print(odczyt_z_bazy_algorytm_wlasciwy(0,2))

    for x in range(1, 61):
        dane_do_wprowadzenia = [x, 0, 0, 0, None, None]
        wprowadz_do_bazy_algorytm(dane_do_wprowadzenia)

def losowanie_slowka():
    prawdopodobienstwo = random.randint(1, 6)

    if prawdopodobienstwo == 1:
        min = 0
        max = 4
    if prawdopodobienstwo == 2:
        min = 4
        max = 7
    if prawdopodobienstwo == 3:
        min = 7
        max = 16
    if prawdopodobienstwo == 4:
        min = 16
        max = 31
    if prawdopodobienstwo == 5:
        min = 31
        max = 56
    if prawdopodobienstwo == 6:
        min = 56
        max = 100
    kszksz = odczyt_z_bazy_algorytm_wlasciwy(min, max)
    if kszksz == None:
        losowanie_slowka()
    else:
        return kszksz



def nauka():

    nnn = str(losowanie_slowka())
    #nnn = 2
    jezyk1 = ("language_1")
    jezyk2 = ("language_2")
    a = odczyt_z_bazy(jezyk1, jezyk2, nnn)
    b = random.randint(0,1)
    c = abs(b-1)
    #print(a[2])
    primary_key_slowka = str(a[2][0])
    temp_row_algorytm = odczyt_z_bazy_algorytm(primary_key_slowka)
    #print(temp_row_algorytm)
    if temp_row_algorytm == []:
        #print("pusto")
        dane_do_wprowadzenia = [primary_key_slowka, 0, 0, 0, None, None]
        wprowadz_do_bazy_algorytm(dane_do_wprowadzenia)
    wpisane = input(a[b])

    #dane_do_wprowadzenia = [temp_row_algorytm[1],temp_row_algorytm[2],temp_row_algorytm[3],temp_row_algorytm[4],temp_row_algorytm[5]]


    if wpisane.lower() == "wprowadz":
        print('tudoszlo')
        print('Wprowadz jezyk oraz kategorie. Mozesz dokonac zmiany podczas pracy programu wpisujac "Reset"')
        global z_jakiego_na_jaki_temp
        z_jakiego_na_jaki_temp = z_jakiego_na_jaki()
        global kat
        kat = jaka_to_kategoria()
        glowniejszy()

    if wpisane == a[c]:
        temp_row_algorytm = odczyt_z_bazy_algorytm(str(primary_key_slowka))
        temp_row_algorytm[0] = list(temp_row_algorytm[0])
        temp_row_algorytm[0][2] = str(int(temp_row_algorytm[0][2]) + 1)
        temp_row_algorytm[0][4] += 1
        temp_row_algorytm[0] = tuple(temp_row_algorytm[0])
        dane_do_wprowadzenia = [temp_row_algorytm[0][1], temp_row_algorytm[0][2], temp_row_algorytm[0][3], temp_row_algorytm[0][4],
                                temp_row_algorytm[0][5], temp_row_algorytm[0][6]]
        update_bazy_algorytm(dane_do_wprowadzenia)
        nauka()

    else:
        print('\n','ZLE, poprawna odpowiedz to:', a[c].upper(), '\n')
        print( a[b],' - ',a[c].upper(),'\n')

        temp_row_algorytm = odczyt_z_bazy_algorytm(str(primary_key_slowka))
        #print(temp_row_algorytm)
        #print(dane_do_wprowadzenia)
        #dane_do_wprowadzenia = [primary_key_slowka, None, None, 0, None, None]
        dane_do_wprowadzenia = [temp_row_algorytm[0][1], temp_row_algorytm[0][2], temp_row_algorytm[0][3], 0, temp_row_algorytm[0][5], temp_row_algorytm[0][6]]
        #print(dane_do_wprowadzenia)
        update_bazy_algorytm(dane_do_wprowadzenia)
        #print()
        nauka()


        return

def update_bazy_algorytm(algorytm):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)
    alg = algorytm
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
#cur.execute("SELECT * FROM algorytm WHERE prawidlowo+nieprawidlowo<? AND prawidlowo+nieprawidlowo>? AND nauczone<1", (max,min,))
    cur.execute("SELECT * FROM algorytm WHERE prawidlowo+nieprawidlowo<? AND prawidlowo+nieprawidlowo>=? AND (nauczone <1 OR nauczone IS NULL)", (max,min,))
    row = cur.fetchall()
    if len(row) > 0:
        temp_random_row = random.choice(row)

        return temp_random_row[1]
    else:
        nauka()


def odczyt_z_bazy(jezyk1, jezyk2, prikey):
    database = r"C:\sqlite\db\pythonsqlite211.db"
    conn = create_connection(database)

    sql = ''' INSERT INTO words (language_1,language_2,language_3,adding_date,rzeczownik,category)
                  VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute("SELECT * FROM words WHERE "+jezyk1+"=? is not null and "+jezyk2+"=? is not null AND id=?", (jezyk1, jezyk2, prikey))
    rows = cur.fetchall()
    temp_random_row = random.choice(rows)
    #print(temp_random_row[1])
    slowo_pl = temp_random_row[1]
    slowo_obcy = temp_random_row[2]
    #print(temp_random_row)
    return slowo_pl, slowo_obcy, temp_random_row


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
    poczatek_de = str(a[0]) + str(a[1]) +str(a[2])
    poczatek_het = str(a[0]) + str(a[1]) + str(a[2]) + str(a[3])
    if poczatek_de.lower() == 'de ' or poczatek_het.lower() == 'het ':
        b = 'yes'
        return b



def jakadata():
    from datetime import date
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

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, create_words_table)
        create_table(conn, algorytm)
        #test()
        nauka()

    else:
        print("Error! cannot create the database connection.")




if __name__ == '__main__':
    main()
