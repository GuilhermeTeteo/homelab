import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Transfere uma chave SSH para as chaves autorizadas de uma lista de servidores.')
    parser.add_argument('-u', '--username', type=str, help='Nome de usuário para login no ssh.')
    parser.add_argument('-s', '--servidores', type=str, help='Caminho para a lista de servidores')
    parser.add_argument('-c', '--chave',type=str, help='Caminho para a chave')
    args = parser.parse_args()

    with open(args.servidores, 'r') as servidores:
        for i in servidores:
            servidor = i.strip()            
            comando = f"ssh-copy-id -i {args.chave} {args.username}@{servidor}"
            try:
                exec = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if exec.stdout:
                    print(exec.stdout)
                    print(f"Chave transferida para o servidor {servidor}\n")
                if exec.stderr:
                    print(exec.stderr) 
                    print(f"Ocorreu um erro ao transferir a chave para o servidor {servidor}.\n")

            except Exception as err:                  
                print(err)

if __name__ == '__main__':
    main() 