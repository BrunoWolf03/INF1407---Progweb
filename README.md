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
-  **Cadastro de jogadores** com informações básicas  
-  **Listagem de jogadores** em páginas dedicadas 
-  **Rank de jogadores** em páginas dedicadas 
-  **Edição e remoção de jogadores** diretamente pelo sistema  
-  **Autenticação básica** de usuários (login/logout)  
-  **Interface responsiva** baseada em templates do Django  
-  **Botão Home** botão com a logo do site

---

## Manual do Usuário

1. **Página de Login**  
   - Permite que o usuário se registre para poder fazer alterações no banco de dados do site.
   - Caso o usuário esqueça sua senha o mesmo pode redefinir sua senha, um email será enviado para a troca da senha.

2. **Home**  
   - Na tela home o usuário poderá cadastrar um novo jogador e informar suas estatisticas, observar o rank atual dos jogadores e acessar a tela do admin caso tenha permissão.  
   - Aqui é a primeira vez que vemos o botão home (logo do site), quando o usuário clicar na logo do site, em qualquer outra pagina, será levado novamente para a pagina home.  

3. **Ranking de Jogadores**  
   - Botão **"Novo Jogador"** para criar um novo jogador com suas estatisticas.  
   - Pode adicionar outros jogadores já existentes.  
   - Pode remover jogadores já existentes.

4. **Criar Novo Jogador**  
   - Usuário pode cadastrar as informações do novo jogador.  
   - O novo jogador criado vai diretamente para a base de dados do site.  

5. **Deletar Jogador**  
   - Usuário pode apagar as informações do jogador.  
   - O jogador vai ser removido diretamente da base de dados do site.  

6. **Administrador**  
   - Na tela de admin o usuário com permissão terá acesso a todas as funcionalidades que a tela de admin do django funciona.  
---

## O que funcionou
- Todas as principais funcionalidades descritas no escopo foram **testadas e aprovadas**.  
- Fluxo de cadastro, edição e exclusão de jogadores funcionando corretamente.    
- Sistema está coerente e executando como esperado.  

---

## O que não funcionou
- A remoção de jogadores foi implementada com redirecionamento, mas **não pôde exibir um pop-up de confirmação**, já que seria necessário o uso de **JavaScript** (não permitido neste trabalho).  
- Fora essa limitação, todas as demais funcionalidades funcionaram corretamente.  

---

## 📌 Observações Finais
O projeto foi concluído conforme os requisitos da disciplina.  
Todas as funcionalidades principais foram implementadas com sucesso, e o site encontra-se estável e utilizável.  
Apenas a ausência de JavaScript limitou a experiência da remoção de jogadores, mas isso não prejudica o funcionamento do sistema.  

---