# INF1407 — ProgWeb  
Trabalho Final — Site de Gerenciamento de Jogadores

## Escopo do Projeto
Este projeto foi desenvolvido para a disciplina **INF1407 — Programação Web**, com o objetivo de criar um site dinâmico em **Django** para o gerenciamento das estatisticas de jogadores de truco na PUC.  

O sistema permite o cadastro, listagem e gerenciamento de jogadores.  

O foco foi explorar os principais recursos do Django, incluindo:
- Estruturação de **models** e **migrations**  
- Criação de **views** e **templates**  
- Integração com banco de dados  
- Rotas organizadas com URLs nomeadas  

---

## Funcionalidades Implementadas
-  **Cadastro de jogadores e partidas** com informações básicas  
-  **Listagem de jogadores e partidas** em páginas dedicadas 
-  **Rank de jogadores** em páginas dedicadas 
-  **Edição e remoção de jogadores e partidas (só admin)** diretamente pelo sistema  
-  **Autenticação básica** de usuários (login/logout)  
-  **Interface responsiva** baseada em templates do Django  
-  **Botão Home** botão com a logo do site

---

## Manual do Usuário

1. **Página de Login**  
   - Permite que o usuário se registre para poder fazer alterações no banco de dados do site.
   - Caso o usuário esqueça sua senha o mesmo pode redefinir sua senha, um email será enviado para a troca da senha.
   - Quando o cadastro é finalizado automaticamente é criado um jogador com o nome daquele usuário cadastrado

2. **Home**  
   - Na tela home o usuário poderá cadastrar uma nova partida e informar suas estatisticas, observar o rank atual dos jogadores.  
   - Aqui é a primeira vez que vemos o botão home (logo do site), quando o usuário clicar na logo do site, em qualquer outra pagina, será levado novamente para a pagina home. 
   - Ao clicar no próprio nome no canto superior direito, o usuário consegue editar as informações do seu perfil.
   - Por último temos o botão "sair" para o usuário sair da sua conta.

3. **Ranking de Jogadores**   
   - Pode ver as estatisticas de jogadores ja cadastrados.
   - Vê por ordem quem é o jogador que mais venceu atualmente.

4. **Criar uma partida**  
   - Usuário primeiro preenche quem é o adversário ja cadastrado no banco que jogou a partida contra.
   - Posteriormente preenche as informações da partida.

5. **Editar Jogador/Partida(Apenas admin)**  
   - Admin pode editar informações de um jogador / partida.  
   - Admin pode apagar jogadores ou partidas


---

## O que funcionou
- Todas as principais funcionalidades descritas no escopo foram **testadas e aprovadas**.  
- Fluxo de cadastro, edição e exclusão de jogadores funcionando corretamente.    
- Sistema está coerente e executando como esperado.  

---

## O que não funcionou
- A remoção de jogadores e partidas foi implementada com redirecionamento, mas **não pôde exibir um pop-up de confirmação**, já que seria necessário o uso de **JavaScript**.  
- Fora essa limitação, todas as demais funcionalidades funcionaram corretamente.  

---

##  Observações Finais
O projeto foi concluído conforme os requisitos da disciplina.  
Todas as funcionalidades principais foram implementadas com sucesso, e o site encontra-se estável e utilizável.  
Apenas a ausência de JavaScript limitou a experiência da remoção de jogadores, mas isso não prejudica o funcionamento do sistema.  

---