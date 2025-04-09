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