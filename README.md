# sqlite3 / Flask-SQLAlchemy and Postgres using Python 3
sqlite
<br>
Situations Where SQLite Works Well
<br>
https://www.sqlite.org/whentouse.html
<br>

Embedded devices and the internet of things, Application file format, 
Websites, Data analysis, Cache for enterprise data, Server-side database, Data transfer format, 
File archive and/or data container, Replacement for ad hoc disk files, Internal or temporary databases
<br>
# sqlite
create, insert, select, update and delete
<br>
Integrity:
<br>
sql_create = "create table if not exists holder(id INTEGER PRIMARY KEY AUTOINCREMENT, title text check(length(title) <= 15) NOT NULL,  note text NOT NULL, published DATETIME NOT NULL)"
<br>
Index:
<br>
sql_index = "create index holder_id_index on holder (id)"

<br>
param:
<br>
Valid SQLite URL forms are:
<br>
sqlite:///:memory: (or, sqlite://)
<br>
sqlite:///relative/path/to/file.db
<br>
sqlite:////absolute/path/to/file.db
<br>

# Orm, Object-relational mapping:
<br>
https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
<br>
http://flask-sqlalchemy.pocoo.org/2.3/

<br>
Helpful links:
<br>
http://zetcode.com/db/sqlitepythontutorial/
<br>
http://pythoncentral.io/advanced-sqlite-usage-in-python/
<br>
https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm

# Postgres
<br>
See code and import psycopg2 / (env) pip install psycopg2
