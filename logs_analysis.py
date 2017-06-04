import psycopg2

def get_connection_info():
    
    user = input("Enter username: ")
    password = input("Enter password: ")
    
    return user, password

    
def main():
    
    user, password = get_connection_info()
    conn = psycopg2.connect("dbname=news user={0} password={1}".format(user, password))
    
    cursor = conn.cursor()
    
    cursor.execute("select title, cnt from (select title, count(*) as cnt from articles a join log l on l.path = '/article/' || a.slug group by title order by cnt desc) x limit 3")
    
    results = cursor.fetchall()
    
    print(results)
    
    title, count = results[0]
    
    print(title)
    print(count)
    
    conn.close()


if __name__ == "__main__":
    main()