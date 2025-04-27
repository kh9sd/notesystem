from configparser import ConfigParser
import psycopg2

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        # In psycopg2, the with statement doesn't automatically close the database connection — only the transaction is closed
        # with psycopg2.connect(**config) as conn:
        #     print('Connected to the PostgreSQL server.')
        #     print(f"{conn=}")
        #     create_tables(conn)
        #     return conn

        conn =  psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        print(f"{conn=}")
        # create_tables(conn)
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def create_tables(conn):
    print(f"{conn=}")
    with conn:
        with conn.cursor() as cur:
            print(f"{cur=}")
            # execute the CREATE TABLE statement
            cur.execute(open("create_tag_table.sql", "r").read())
        # conn.commit()
    print("Done creating table")

if __name__ == '__main__':
    config = load_config()
    print(config)
    conn = connect(config)

    create_tables(conn)
