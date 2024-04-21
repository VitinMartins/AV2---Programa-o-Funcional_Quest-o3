#Função INNER JOIN pedida no trabalho (I) - gera o código do inner join entre as tabelas GAMES,VIDEOGAMES,COMPANY
generate_inner_join = lambda: "INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console " \
                              "INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company"

#Função SELECT pedida no trabalho (II) - gera o comando select nos atrbutos envolvidos
generate_select_query = lambda attributes: f"SELECT {', '.join(attributes)} FROM GAMES {generate_inner_join()}"


consulta_sql = generate_select_query(['GAMES.title', 'COMPANY.name_company'])
print("Consulta SQL gerada:")
print(consulta_sql)