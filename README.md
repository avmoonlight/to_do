O projeto oferecido pelo professor propõe uma implementação Web Service de um TO-DO (organizador de tarefas),  

# Banco de dados:

Para funcionar na nossa aplicação, o banco de dados deverá ser criado nesse modelo, lembrando que para esse código só funciona o MySQL workbench:

```sql
CREATE DATABASE to_do;

USE to_do;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    prioridade ENUM('Baixa', 'Média', 'Alta') NOT NULL,
    concluida ENUM('sim', 'não') NOT NULL,
    imagem VARCHAR(255)
);
```

---

# Integração Front e Back end:

Para utilizar o nosso gerenciador de tarefas, será necessário apenas apostar em uma abordagem intuitiva de cadastro, edição e exclusão de tarefas. 

## Passo a passo:

### URL QUERY:

Para ativar sua url query, será necessário ligar o app.py, assim, entre na venv e digite app.py. Assim que estiver ativo:

![image.png](attachment:e3ac0bfa-5601-4077-8b99-0f579880d611:image.png)

Assim é como aparece quando estiver ativo, para abrir exatamente nosso gerenciador de tarefas, adicionem na url, o seguinte texto:/tarefas

Ou [clique aqui](http://127.0.0.1:5000/tarefas). 

### Possíveis erros:

1. Erro pelo database não estar criado ou inegrado:
    
    ![image.png](attachment:94a6e586-578b-481e-b835-e508039c9682:image.png)
    
    Esse erro pode acontecer por coisas muito simples:
    
    1. Tente startar seu banco de dados, pelo xampp;
    2. Certifique-se que foi criado o banco de dados e que ele está integrado no código app.py;
    3. Certifique-se de que está integrado.

------------------------------------------------------------------------------------------------------------------

# Pesquisa projeto To_do

# Bibliotecas:

# ORM:

## Definição:

Object-Relational Mapping (ORM) é uma técnica que ajuda a conectar o desenvolvimento de aplicativos orientados a objetos com bancos de dados relacionais. Ele é feito por meio de uma ferramenta, geralmente uma biblioteca ou framework, que facilita o uso do banco de dados.

## Como funciona o ORM:

As ferramentas ORM definem como os dados são mapeados e acessados, economizando tempo de desenvolvimento. Também facilitam a adaptação de novos membros, pois muitos projetos usam as mesmas ferramentas. 

NÃO PODE USAR E RODA EM DJANGO

---

# Comparando as demais bibliotecas sobre

1. mysql-connector-python:
    1. Oficial do MySQL, fornece uma interface simples para se conectar ao MySQL e executar consultas SQL. É bem estável e recomendado pela Oracle. 
    2. Durante os testes, achei muito complicado o manuseio, pesquisei muitas vídeo aulas e não tirei aprendizado, e pelo fato de ter encontrado poucos exemplos em documentação oficial, apesar de ser levemente intuitivo e parecido com o pymysql, achei melhor optar pelo pymysql, por ser mais simples 
    3. https://pypi.org/project/mysql-connector-python/
2. MySQLdb (ou mysqlclient)
    1. Biblioteca muito antiga, muito mais eficiente.
    2. achei a complexidade alta, mas foi uma segunda opção de teste. tudo o que foi pesquisado, achei diferente, porém achei mais simples as vídeo aulas de pymysql. 
    3. https://pypi.org/project/mysqlclient/

---

# PYMYSQL:

A documentação é simples e intuitiva, com exemplos muito claros e comuns, achei simples, as aulas desse eram básicas e simples. 

https://pymysql.readthedocs.io/en/latest/

P.S. é difícil se perder em uma documentação extremamente simples

## REFERÊNCIAS DO CRUD:

https://youtu.be/5PIjIbnWhd8?si=KcOZNfZ9S9a8Lkzf - Atualizar e excluir

https://youtu.be/o-xgjWPmV7w?si=ejHKBRVNcv_wzNdj - Inserir registros

https://youtu.be/jMmI8kApT8E?si=CB6ovQ2xi8aJr796 - Tutorial de como realizar. Está em hindi, foi mais difícil deixar certinho os exemplos e as construções das coisas.

https://youtu.be/XHZ7E1q1UoY?si=exOv_KsXrH1SgMl1 - Explicação resumida

# EXPLICAÇÃO DE COISAS ESPECÍFICAS DO CÓDIGO:

## PYMYSQL:

Pymysql é uma biblioteca para conectar e interagir com bancos de dados MySQL, permitindo executar consultas SQL e manipular resultados.

### Itens específicos do código:

1. get_db_connection(): Cria e retorna uma conexão com o banco de dados MySQL, e ele usa as configurações necessárias para a conexão: Ex.: MYSQL_HOST, MYSQL_USER
2. conn.cursor(): Cria um cursor que é utilizado para fazer as consultas no banco de dados
3. cursor.execute(——): Executa os comandos que funcionam no mysql (INSERT, SELECT, UPDATE E DELETE)
4. conn.commit(): Confirma alterações no banco de dados
5. conn.close(): Fecha a conexão quando ela não é mais útil. 

## WERKZEUG (werkzeug.utils e secure_filename):

Werkzeug é uma biblioteca que oferece ferramentas para o Flask. A função secure_filename garante que o nome do arquivo enviado (como uma imagem) seja seguro para o armazenamento no sistema de arquivos

### Itens específicos do código:

1. secrure_filename(imagem.filename): Deixa o nome do arquivo seguro, tirando ou trocando caracteres que podem dar problema, como espaços e símbolos. Isso evita riscos de segurança.

---

# Coisas extremamente específicas:

## Imagem no banco de dados ser um varchar:

1. Quando você faz upload de uma imagem, você não salva o arquivo no banco de dados, mas sim o caminho ou URL dele. Esse caminho é guardado no banco, geralmente em um campo do tipo `VARCHAR(255)`, já que o caminho do arquivo não costuma passar de 255 caracteres.
2. Arquivos BLOB ficariam muito grande e pesam muito