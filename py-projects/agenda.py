import os

os.system('clear')

AGENDA = {}


AGENDA['Daniel'] = {
    'tel':'+5511984598475',
    'email':'daniel.b@solyd.com',
    'empresa':'bosch',
}

AGENDA['Henrique'] = {
    'tel':'+5511984874475',
    'email':'henrique.b@solyd.com',
    'empresa':'CNH',
}


def mostra_contato(contato):
    print('Nome: ', contato)
    print('Telefone: ', AGENDA[contato]['tel'])
    print('E-mail: ', AGENDA[contato]['email'])
    print('Empresa: ', AGENDA[contato]['empresa'])
    print('-='*40, '\n')


def mostra_agenda():
    for contato in AGENDA:
        mostra_contato(contato)


def buscar_contato():
    nome = input('BUSCAR : ').capitalize()
    mostra_contato()
   


def add_editar_ontato(contato, telefone, email, empresa):
    AGENDA[contato] = {
    'tel': telefone,
    'email': email,
    'empresa': empresa,
    }
    print(f'Contato {contato} adicionado/editado com sucesso')
    print('*'*30)


def excluir_contato(contato):
    AGENDA.pop(contato)


add_editar_ontato("Matheus", '49998745475', 'matheus@solyd.com', 'Tempest')
excluir_contato('Daniel')
mostra_agenda()