import os # Importing the "os" module for system manipulation, such as "cls", "pause", "color" and "exit"

os.system('color 1f') # Changes the background text color to blue with white letters

to_do_list = []

def main(op = 0):

    print('\n' + 10 * '-' + 'TASK LIST' + 10 * '-')
    print('\n1 - Incluir nova tarefa')
    print('2 - Ver lista de tarefas')
    print('3 - Excluir tarefa salva')
    print('4 - Sair\n')
    print(29 * '-' + '\n')

    op = input('Digite o número da opção desejada: ')
    
    os.system('cls')
        
    if op == '1' or op == '2' or op == '3' or op == '4':
    
        op_task(op)
        
    elif op == '' or op == ' ' or op != '1' or op != '2' or op != '3' or op != '4':
        
        print('\nOpção inválida, digite novamente\n')
        os.system('pause')
        os.system('cls')
        main(op = 0)
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')

def op_task(op):
    
    while True:
        
        if op == '1':
            
            task = input('\nDigite a tarefa a ser adicionada: ')            
            to_do_list.append(task)
            os.system('cls')
            main(op = 0)
            break

        elif op == '2':
            
            print('\nSua lista de tarefas: ')
            print(f'\n{to_do_list}\n')
            os.system('pause')
            os.system('cls')
            main(op = 0)
            break

        elif op == '3':
            
            print('\nSua lista de tarefas: ')
            print(f'\n{to_do_list}\n')
            task_to_be_removed = input('Digite a tarefa a ser removida: ')
            to_do_list.remove(task_to_be_removed)
            os.system('cls')
            main(op = 0)
            break

        elif op == '4':

            print('\nSaindo...\n')
            os.system('pause')
            os.system('cls')
            break
        
        
        else:
            
            print('\nErro!!! Favor entrar em contato com o suporte!\n')
            os.system('pause')
            os.system('cls')
            break
        
    os.system('exit')
       
main(op = 0)