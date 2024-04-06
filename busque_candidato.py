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
    
    elif menu == 2:
        def buscar(candidatos, e, t, p, s):
            candidato_ideal = []
            for escolhido, resultado in candidatos:
                notas = resultado.split('_')
                e_nota = int(notas[0][1:])
                t_nota = int(notas[1][1:])
                p_nota = int(notas[2][1:])
                s_nota = int(notas[3][1:])
                if e_nota >= e and t_nota >= t and p_nota >= p and s_nota >= s:
                    candidato_ideal.append(escolhido)
            return candidato_ideal
        e = int(input('Insira nota mínima necessária para entrevista: '))
        t = int(input('Insira nota mínima necessária para teste teórico: '))
        p = int(input('Insira nota mínima necessária para teste prático: '))
        s = int(input('Insira nota mínima necessária para soft skills: '))

        candidato_ideal = buscar(candidatos, e, t, p, s)
        if candidato_ideal:
            print('Candidato(s) aprovado(s): ')
            for candidato in candidato_ideal:
                print(candidato)
        else:
            print('Não existe candidato apto para essa vaga')
    
    elif menu == 0:
        print('Fechando programa.')
        break
    else:
        print('Digite uma opção válida!')
  
        

            
            
            
