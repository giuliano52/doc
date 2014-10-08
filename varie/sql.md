SQL
===

#SQLITE

per il passaggio con parametri (utile per inserire caratteri come ' < 
```php
$db = new SQLite3('mysqlitedb.db');

$db->exec('CREATE TABLE foo (id INTEGER, bar STRING)');
$db->exec("INSERT INTO foo (id, bar) VALUES (1, 'This is a test')");

$stmt = $db->prepare('SELECT bar FROM foo WHERE id=:id');
$stmt->bindValue(':id', 1, SQLITE3_INTEGER);

$result = $stmt->execute();
var_dump($result->fetchArray());
```

#MYSQL / MARIA DB 

## Backup e Restore
per fare il backup di un database:

    mysqldump database_name > nomefile.mysql
    mysqldump -u root -p database_name | bzip2 > nomefile.mysql.bz2

per il restore:

    mysql nome_database < backup.mysql
