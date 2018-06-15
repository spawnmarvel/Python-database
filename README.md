# sqlite3 using Python 3
sqlite
<br>
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

Orm:
<br>
https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm

Helpful links:
<br>
http://zetcode.com/db/sqlitepythontutorial/
<br>
http://pythoncentral.io/advanced-sqlite-usage-in-python/
<br>
https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm

