def introduction_page() -> str:
  message = ''' 
    Sistema Musical

    * Cadastrar música - 1
    * Criar playlist - 2
    * Sair - 5
    '''
  print(message)
  command = input("Comando: ")
  
  return command