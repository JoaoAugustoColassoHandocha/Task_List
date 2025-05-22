import os

os.system('color 1f')

def main(op = 0):

    print('\n' + 25 * '*' + 'TASK LIST' + )
    print('1 - Incluir nova task')
    print('2 - Ver lista de tasks')
    print('3 - Excluir task salva')
    print('4 - Sair')
    print(25 * '*' + '\n')

    op = int(input('Digite o número da opção desejada: '))
    
    os.system('cls')
    
    if op == '' or op == ' ' or op != 1 and op != 2 and op != 3 and op != 4:
        
        print('\nOpção inválida, digite novamente\n')
        os.system('pause')
        os.system('cls')
        main(op = 0)
        
    elif op == 1 or op == 2 or op == 3 or op == 4:
    
        task(op)
        
    else:
        
        print('\nErro!!! Favor entrar em contato com o suporte!\n')
        os.system('pause')
        os.system('cls')

def task(op):

    to_do_list = []

    while True:
        
        if op == 1:
            
            task = input('\nDigite a tarefa a ser adicionada: ')            
            to_do_list.append(task)
            os.system('cls')
            main(op = 0)

        elif op == 2:
            
            print('\nSua lista de tarefas: ')
            print(f'\n{to_do_list}\n')
            os.system('pause')
            os.system('cls')
            main(op = 0)

        elif op == 3:
            
            print('\nSua lista de tarefas: ')
            print(f'\n{to_do_list}\n')
            task_to_be_removed = input('Digite a tarefa a ser removida: ')
            to_do_list.remove(task_to_be_removed)
            main(op = 0)

        elif op == 4:

            print('\nSaindo...\n')
            os.system('pause')
            os.system('cls')  
            break
        
        else:
            
            print('\nErro!!! Favor entrar em contato com o suporte!\n')
            os.system('pause')
            os.system('cls')
            break
      
main(op = 0)