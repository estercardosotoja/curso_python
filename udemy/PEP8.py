"""
PEP8 - Index of Python Enhancement Proposals - Index de Aprimoramento de Python
https://www.python.org/dev/peps/
"""
"""
    -   O que são PEP's?
    São arquivos que apresentam propostas de melhoria para a Linguagem Python
    
    A PEP 8 é Style Guilde for Python Code
              Guia de Estilo para codigo em Python
              
    Regras mais utilizadas
    1) O pycharm vem com padrão de reconhecimento de palavras em inglês.
        - Para o PyCharm reconhecer palavras em ingles 
        File-Setting - Inspections - Proofreading - Desmarque Typo
    
    2) Identação (Organização do código)
        -Utiliza 4 espaços para cada codigo dentro de blocos como funçõe, condicionais, classes, dentro outros.     
        #Exemplo (Condicionais)
        if x < 10:
            if y > 10:
                y = 5
        4 espaços para identar código.

    3)  Linhas em Branco:
        a)    Sempre finalizar o código com uma linha branca
        b)    Para declarar funções deve se ter duas linhas em branco
            #Exemplo 
                def x():
                    pass
                
                
                def y():
                    pass

    4) Importação:
    - Se você deseja fazer a importação de duas bibliotecas importe uma por vez logo no inicio do programa;
    (Após os comentários iniciais e antes da declaração da primeira veriável/função;
    #Exemplo 
        //Author Ester
        
        
        import x
        import y                          obs: nunca juntas ex:. import x,y
        
        
        
        def x()
            ....

    5) Uso de espaços:
    - Nunca utilize espaços antes ou depois de chaves, colchetes ou parenteses
    - Use um espaço antes e depois de declarar um variavel ou usar um operador do tipo  < , > , ==. dentre outros.
    #Exemplo:
    
    def x():        // Não pode "x ():"
        pass
       
       
    y = 10          // Não pode y=10;
    
    6) Nomeclatura de variaveis:
        - Utilizar letras Minusculas separadas por underline(_)
        - Utilizar letras Maisculas separadas por underline(_)
        - Utilziar palavras começando por letras Maiusculas.
        
        # EX:

        idadeJoao = 17
        idade_Joao = 17
        IDADE_JOAO = 17
        
        Modo errado -> idadejoao =17
        
"""
