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
              join log l
                on l.path = '/article/' || a.slug
            group by title
            order by cnt desc
        ) x
        limit 3
        """)
    
    results = cursor.fetchall()
    
    print("\nMost popular articles:\n")
    
    for title, count in results:
        print("\"{0}\" - {1} views".format(title, count))


def print_top_authors(cursor):
    """Print the 3 most popular authors."""
    
    cursor.execute("""
        select name, cnt from (
            select aut.name,
                   count(*) as cnt
              from articles a
              join log l
                on l.path = '/article/' || a.slug
              join authors aut
                on a.author = aut.id
            group by aut.name
            order by cnt desc
        ) x
        limit 3
        """)
    
    results = cursor.fetchall()
    
    print("\nMost popular authors:\n")
    
    for name, count in results:
        print("{0} - {1} views".format(name, count))


def print_days_with_error(cursor):
    """Print the days that had more than 1% error."""
    
    cursor.execute("""
        select day, cnt_error / total
        from (
            select date_trunc('day', time) as day,
                   sum(case when status <> '200 OK' then 1 else 0 end) as cnt_error,
                   count(*) * 1.0 as total
              from log
            group by day
        ) x
        where cnt_error / total > 0.01
        order by day
        """)
    
    results = cursor.fetchall()
    
    print("\nDays with high amount of error:\n")
    
    for day, percent in results:
        print("{0:{dfmt}} - {1:.{prec}}% errors".format(day, percent * 100, dfmt='%B %d, %Y', prec=3))


def main():
    
    user, password = get_connection_info()
    conn = psycopg2.connect("dbname=news user={0} password={1}".format(user, password))
    
    cursor = conn.cursor()
    
    print_top_articles(cursor)
    print_top_authors(cursor)
    print_days_with_error(cursor)
    
    conn.close()


if __name__ == "__main__":
    main()