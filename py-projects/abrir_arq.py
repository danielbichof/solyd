try:
    with open('email.txt', 'a') as arquivo:
        arquivo.write("mamamia@gmail.com")

except Exception as error:
    print('arquivo não existe')
    print(error)