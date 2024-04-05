candidatos = [
    ['canditado 1', 'e5_t10_p8_s8'],
    ['candidato 2','e10_t7_p7_s8'],
    ['candidato 3','e8_t5_p4_s9'],
    ['candidato 4','e2_t2_p2_s1'],
    ['candidato 5','e10_t10_p8_s9']
]
texto = (f'''
   Soluções & Inovações para o seu dia a dia
==============================================
            Como deseja continuar?
      1 - Adicionar candidato a lista.
      2 - Buscar candidato ideal.
      0 - Sair.    
=> ''')

while True:
    menu = int(input(texto))
    if menu == 1:
        nome_candidato = input(f'''
==============================================
    Informe o nome do candidato:
=> ''')
        entrevista = input(f'''
==============================================
    Informe a avaliação da entrevista(e):
=> ''')
        teste_teorico = input(f'''
==============================================
    Informe a avaliação do teste teórico(t):
=> ''')
        teste_pratico = input(f'''
==============================================
    Informe a avaliação do teste prático(p):
=> ''')
        teste_skills = input(f'''
==============================================
    Informe a avaliação das soft skills(s)):
=> ''')
        resultado = f'e{entrevista}_t{teste_teorico}_p{teste_pratico}_s{teste_skills}'
        candidatos.extend([[f'{nome_candidato}', f'{resultado}']])
        for i in range(len(candidatos)):
            print(f'Candidato {i+1}')
            print(f'Nome: {candidatos[i][0]}')
            print(f'Resultado: {candidatos[i][1]}\n')
            print('********************************\n')
            
  
        

            
            
            
