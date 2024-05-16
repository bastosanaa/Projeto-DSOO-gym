# Projeto de gerenciamento da academia BodyLab

 <img align="left" height="120" src="https://media.tenor.com/_2_XVT9p3RsAAAAi/excercise-sport.gif">
 
    Trabalho para a disciplina Desenvolvimento de Sistemas Orientado a Objetos
    Realizado em parceria por Ana Luiza Bastos e Camila Prim.
    Implementação em Python. 🐍
    
<br>
<br>

# Entidades

- <p>O<strong> cadastro de pessoas</strong> representa os diferentes tipos de indivíduos presente nesse sistema (alunos e professores) e para cada tipo será feito da seguinte forma:</p>
        <p><strong>Alunos:</strong>  nome, número de telefone, email, plano, matrícula,turno, ficha</p>
        <p><strong>Professores:</strong> nome, número de telefone, email, turno, CREF</p>

- <p>O<strong> cadastro do turno</strong> é formado pelo turno matutino, vespertino e noturno.</p>

- <p>O<strong> cadastro da ficha</strong> é formado por professor responsável, número de repetições, número de séries e uma lista de treinos pré-estabelecida.</p>

 <img align="right" height="150" src="https://media.tenor.com/DUZkeoIdXjwAAAAi/gym-fitness-centers.gif">

- <p>O<strong> cadastro da matrícula</strong> é formado pelo id da matrícula, pelo plano escolhido pelo aluno, data de início e término, data de vencimento da matrícula e mensalidade.</p>

- <p>O<strong> plano</strong> é uma classe enum, que só terá os tipos de planos: Gold, Silver e Diamond</p>
	      <i><strong>O plano é apenas um tipo por aluno</strong></i>

- <p>O<strong> turno</strong> é um classe enum, que terá os períodos possíveis de treino</p>
	 <i><strong>Poderá ser escolhido apenas um, tanto para professor quanto para aluno.</strong></i>

# Controlador
- <p>O <strong>controlador de aluno</strong> será responsável por mostrar os treinos contidos nas fichas do aluno e a matrícula do mesmo, retirar ou adicionar o aluno por turno, calcular a quantidade de aluno por turno e calcular aluno por turno</p>

- <p>O <strong>controlador da ficha</strong> será responsável por inserir o número de repetições e séries, inserir e retirar o treino da ficha, inserir o professor encarregado daquela ficha e calcular qual ficha é a mais utilizada.</p>

- <p>O <strong>controlador de matrícula</strong> vai definir o plano e a mensalidade baseada no plano escolhido, a data de início, a data de vencimento do pagamento e a data de término e calcular qual o plano mais vendido.</p>

- <p>O <strong>controlador de professor</strong> vai inserir e retirar o professor do turno (matutino, vespertino e noturno) e gerar um relatório de qual turno tem mais professores</p>


# Telas
- <p>A <strong>tela do aluno</strong> será um menu no qual o usuário irá escolher qual opção ele deseja: mostrar os treinos contidos na fichas e detalhes da matrícula.</p>

- <p>A <strong>tela da ficha</strong> será um menu no qual o usuário irá escolher qual opção ele deseja: inserir o número de repetições e séries, inserir e retirar o treino da ficha, inserir o professor encarregado daquela ficha.</p>

- <p>A <strong>tela da matrícula</strong> será um menu no qual o usuário irá escolher qual opção ele deseja: escolher o  plano, inserir a data de início, a data de vencimento do pagamento e a data de término.</p>

- <p>A <strong>tela do professor</strong> será um menu no qual o usuário irá escolher qual opção ele deseja:  inserir ou retirar turno do professor e calcular o número de professores em um turno escolhido pelo usuário.</p>

# Divisão do trabalho
<img align="right" height="120" src="https://private-user-images.githubusercontent.com/74038190/243199547-42077049-1939-493e-9a19-47ca5db36643.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTU4MTc1NzEsIm5iZiI6MTcxNTgxNzI3MSwicGF0aCI6Ii83NDAzODE5MC8yNDMxOTk1NDctNDIwNzcwNDktMTkzOS00OTNlLTlhMTktNDdjYTVkYjM2NjQzLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE1VDIzNTQzMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg3MjcyYTYxOGQxZjI4Y2QzNjY4NDUwMzE5YTVmMWYzZjUxNzM1NjkxZTI2MTVkZDQ3YmU1ODQyMzU3YTMwMjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.4ibGFUCXT48cVVDD2bX5KIa_he5t5ddL4CrNlkM3C14">

- <p>Dado que existem quatro entidades no contexto do nosso projeto, cada uma com implementações específicas, é prudente distribuir a responsabilidade entre a dupla, de modo que cada uma assuma o desenvolvimento de duas entidades.</p>
- <p>Ana Luiza Bastos ficará responsável pelas entidades <strong>Professor e Ficha</strong></p>
- <p>Camila Prim ficará resonsavél pelas entidades<strong>Aluno e Matrícula</strong></p>
