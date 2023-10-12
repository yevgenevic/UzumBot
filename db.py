import psycopg2

db_config = {
    'dbname': 'ke_bot',
    'user': 'postgres',
    'password': '1',
    'host': '172.17.0.2',
    'port': 5432
}

connection = psycopg2.connect(**db_config)
cursor = connection.cursor()


def create_table():
    create_ostatki_tabel_url = '''
        CREATE TABLE IF NOT EXISTS url_ostatki (
            id serial primary key,
            name varchar(100) unique,
            url varchar(300)
        )
    '''

    create_prodaja_tabel_url = '''
            CREATE TABLE IF NOT EXISTS url_prodaja (
                id serial primary key,
                name varchar(100) unique,
                url varchar(300)
            )
        '''
    create_table_ostatki = '''
            CREATE TABLE IF NOT EXISTS ostatki (
                id                       varchar(50),
                naimenovanie             varchar(255),
                shtrixkod                varchar(255),
                sku                      varchar(255),
                id_tovara                varchar(255),
                k_otpravke               varchar(255),
                v_prodazhe               varchar(255),
                vozvrat                  varchar(255),
                brak                     varchar(255),
                sebest_suma              varchar(255),
                stoimost_prodazhi        varchar(255),
                obshchii_ostatok         varchar(255),
                obshchaya_summa_ostatkov varchar(255),
                sebest_summa_summa       varchar(255),
                stoimost_prodazhi_summa  varchar(255),
                ostatak_na_sklade        varchar(255),
                ostatak_na_sdh           varchar(255),
                ostatak_na_fotostudii    varchar(255),
                ostatak_na_sklade_summa  varchar(255),
                dostupno_k_otpravke      varchar(255),
                status                   varchar(255),
                created_at               varchar(255)
            )'''

    create_table_prodaja = '''
        create table if not exists prodaja (
        Status                     varchar(255),
        Data_sozdaniya             varchar(255),
        Data_polucheniya           varchar(255),
        Nomer_zakaza               varchar(255),
        Shtrixkod                  varchar(255),
        SKU                        varchar(255),
        Naimenovanie               varchar(255),
        Kategoriya                 varchar(255),
        Kolichestvo                varchar(255),
        Vozvraty                   varchar(255),
        Vyruchka_sumy                varchar(255),
        Vyruchka_s_vychetom_komissii varchar(255),
        Komissiya_marketpleysa     varchar(255),
        Cena_sumy                  varchar(255),
        Sebestoimost_sumy          varchar(255)
    ) '''

    cursor.execute(create_table_prodaja)
    cursor.execute(create_table_ostatki)
    cursor.execute(create_prodaja_tabel_url)
    cursor.execute(create_ostatki_tabel_url)
    connection.commit()


def create_ostatik(name: str, url: str):
    select_query = "SELECT * FROM url_ostatki WHERE name = %s"
    cursor.execute(select_query, (name,))
    data = cursor.fetchone()
    if not data:
        query = "INSERT INTO url_ostatki (name, url) Values (%s, %s)"
        cursor.execute(query, (name, url))
        connection.commit()
    else:
        query = "UPDATE url_ostatki SET url = %s WHERE name = %s"
        cursor.execute(query, (url, name))
        connection.commit()


def select_url_prodaja(name: str):
    query = "SELECT url FROM url_prodaja WHERE name = %s"
    cursor.execute(query, (name,))
    data = cursor.fetchone()

    return data


def select_url_ostatki(name: str):
    query = "SELECT url FROM url_ostatki WHERE name = %s"
    cursor.execute(query, (name,))
    data = cursor.fetchone()

    return data


def create_prodaja(name: str, url: str):
    select_query = "SELECT * FROM url_prodaja WHERE name = %s"
    cursor.execute(select_query, (name,))
    data = cursor.fetchone()
    if not data:
        query = "INSERT INTO url_prodaja (name, url) Values (%s, %s)"
        cursor.execute(query, (name, url))
        connection.commit()
    else:
        query = "UPDATE url_prodaja SET url = %s WHERE name = %s"
        cursor.execute(query, (url, name))
        connection.commit()

def select_ostatki_vse():
    query = "SELECT url FROM url_ostatki WHERE name = 'vse'"
    cursor.execute(query, )
    data = cursor.fetchone()
    return data


def select_prodaja_vse():
    query = "SELECT url FROM url_prodaja WHERE name = 'vse'"
    cursor.execute(query, )
    data = cursor.fetchone()
    return data

create_table()
