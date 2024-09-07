## 解答：

##### **步驟 1：啟動 MariaDB 並檢查狀態**
```bash
sudo systemctl start mariadb
sudo systemctl status mariadb
```

##### **步驟 2：進行安全設置**
```bash
sudo mysql_secure_installation
```
根據提示完成 root 密碼設置，並刪除匿名用戶。

##### **步驟 3：創建新用戶**
```sql
CREATE USER 'project_user'@'localhost' IDENTIFIED BY 'YourPass123';
```

##### **步驟 4：分配權限**
```sql
GRANT ALL PRIVILEGES ON *.* TO 'project_user'@'localhost';
FLUSH PRIVILEGES;
```

##### **步驟 5：驗證權限**
```sql
SHOW GRANTS FOR 'project_user'@'localhost';
```
