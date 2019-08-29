
import paramiko

NOME_DA_CHAVE = 'ssh-key.pem'

key = paramiko.RSAKey.from_private_key_file(NOME_DA_CHAVE)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

opts = {
    'hostname': '52.39.88.131',
    'username': 'ubuntu',
    'pkey': key 
}
client.connect(**opts)

commands = [

    'sudo apt update -y',
    'sudo apt install -y apache2',
    'sudo service apache2 start'
    'sudo echo "hello, world" > /var/www/html/index.html'
    
]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(
        stdout.read().decode(),
        stderr.read().decode()
    )