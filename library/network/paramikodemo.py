# ****************************************************************分割线****************************************************************
# todo paramiko

# 准备工作（SSH连接WSL）
# ①卸载重装SSH
# sudo apt-get remove openssh-client
# sudo apt-get install openssh-server
# ②修改配置
# sudo vim /etc/ssh/sshd_config
# Port 22
# PasswordAuthentication yes
# AllowUsers fantasy
# ③重启SSH服务
# sudo service ssh restart
# ④PowerShell测试
# ssh fantasy@127.0.0.1

# ****************************************************************分割线****************************************************************
# todo SSH连接（密码）

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 把要连接的机器IP添加进know_hosts中
# ssh.connect(hostname="127.0.0.1", port=22, username="fantasy", password="123456")
#
# bash = "pwd"
# stdin, stdout, stderr = ssh.exec_command(bash)  # 运行bash的返回值必须写成stdin, stdout, stderr
# print(stdout.read().decode())
# ssh.close()

# ****************************************************************分割线****************************************************************
# todo SSH连接（密钥）

# 准备工作
# ①客户端ssh-keygen生成公钥（id_rsa.pub）和私钥（id_rsa）
# ②上传公钥到服务器并加权
# scp id_rsa.pub fantasy@127.0.0.1:/home/fantasy/.ssh
# chmod 600 authorized_keys
# ③测试
# ssh fantasy@127.0.0.1

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# key = paramiko.RSAKey.from_private_key_file(filename="C:/Users/Administrator/.ssh/id_rsa", password="")  # 加载本地私钥
# ssh.connect(hostname="127.0.0.1", port=22, username="fantasy", pkey=key)
#
# bash = "pwd"
# stdin, stdout, stderr = ssh.exec_command(bash)
# print(stdout.read().decode())
# ssh.close()

# ****************************************************************分割线****************************************************************
# todo SFTP（密钥）

# import paramiko
#
# transport = paramiko.Transport(("127.0.0.1", 22))
# key = paramiko.RSAKey.from_private_key_file(filename="C:/Users/Administrator/.ssh/id_rsa", password="")
# transport.connect(username="fantasy", pkey=key)
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# sftp.put("C:/Users/Administrator/.ssh/id_rsa", "/home/fantasy/id_rsa")
# sftp.get("/home/fantasy/id_rsa", "C:/Users/Administrator/Desktop/id_rsa")
# transport.close()
# sftp.close()
