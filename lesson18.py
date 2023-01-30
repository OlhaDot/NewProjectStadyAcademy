import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="2222")

mycursor = mydb.cursor()
# 1
mycursor.execute("CREATE DATABASE IF NOT EXISTS `my_first_db`")
# 2
mycursor.execute("CREATE TABLE `my_first_db`.`student` (`id` INT, `name` VARCHAR(255))")
# 3
mycursor.execute("CREATE TABLE `my_first_db`.`employee` "
                 "(`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255),"
                 " `salary` INT(6))")
# 4
mycursor.execute("ALTER TABLE `my_first_db`.`student` "
                 "ADD PRIMARY KEY (`id`)")

# 5
sql = "INSERT INTO `my_first_db`.`student` (`id`, `name`) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)

sql = "INSERT INTO `my_first_db`.`employee` (`id`, `name`, `salary`) VALUES (%s, %s, %s)"
val = ("01", "John", "10000")
mycursor.execute(sql, val)

mydb.commit()

