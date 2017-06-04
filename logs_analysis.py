import psycopg2

def get_connection_info():
    """Get connection information from user input."""
    
    user = input("Enter username: ")
    password = input("Enter password: ")
    
    return user, password

    
def print_top_articles(cursor):
    """Print the 3 most popular articles."""
    
    cursor.execute("""
        select title, cnt from (
            select title,
                   count(*) as cnt
              from articles a
              join log l on l.path = '/article/' || a.slug
            group by title
            order by cnt desc
        ) x
        limit 3
        """)
    
    results = cursor.fetchall()
    
    print("\nMost popular articles:\n")
    
    for title, count in results:
        print("\"{0}\" - {1} views".format(title, count))


def main():
    
    user, password = get_connection_info()
    conn = psycopg2.connect("dbname=news user={0} password={1}".format(user, password))
    
    cursor = conn.cursor()
    
    print_top_articles(cursor)
    
    conn.close()


if __name__ == "__main__":
    main()