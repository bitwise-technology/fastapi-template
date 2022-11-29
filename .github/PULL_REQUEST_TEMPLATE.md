# Contribuição

## 📝 Descrição

Escreva um breve resumo sobre sua funcionalidade ou problema corrigido descrevendo com detalhes do que se trata o Pull Request.

## 🧑‍💻 Tipo de alteração

- [ ] ✨ Nova funcionalidade
- [ ] 🐛 Solução de bug
- [ ] ♻️ Refactor
- [ ] 📚 Documentação

## 🧐 Motivo e contexto

Descrição do por que o pull request é necessário.

<!--
EXEMPLO

Essa feature é necessária pois ela será o ponto de entrada para o registro do usuário na plataforma da BW.

OU PARA BUGS

Devido a propriedade X não estar sendo validada no endpoint de signup do usuário, o backend estava retornando SERVER INTERNAL ERROR para o usuário final.

```golang
// Snippet from code where the bug is happen
type User struct {
	name string
	gender string
	phone string // <-- This required field was not been validated
}
```
-->

## 📚 Novas dependências

Motivos que fizeram ser adicionadas novas dependências no projeto.

- [Nome da dependência com o link para a documentação](): Motivo pelo qual foi escolhida tal dependência.

<!--
EXEMPLOS DE COMO ESTRUTURAR AS INFORMAÇÕES DESSA SEÇÃO

- [firebase-sdk](https://firebase.google.com/docs/admin/setup?hl=pt-br): Realizamos uma busca para escolher a melhor API para Singup de usuário na internet, e aparentemente o firebase utiliza sua própria biblioteca para realizar esse trabalho, veja aqui o link do spike the escolha de serviço.

- [Fiber](https://docs.gofiber.io/): Para construir a nossa camada de web-framework, escolhemos essa biblioteca pois aparentemente ela é a mais rápida do mercado e: x, y e z.

CASO NÃO HAJA NOVAS DEPENDÊNCIAS ESTRUTURE COMO NO EXEMPLO ABAIXO
- Não se aplica
-->

## ✅ Checklist

- [ ] Comentei meu código, especialmente em áreas difíceis de entender;
- [ ] Testes de unidade novos e existentes funcionaram localmente com minhas alterações;
- [ ] Novas dependências foram adicionadas;

## 🧪 Como testar

Descreva como testar as funcionalidades ou correções, forneça instruções de como rodar os testes e liste todos os detalhes relevantes.

## 📺 Screenshots & demo

Mostre screenshots, vídeos ou gifs da funcionalidade rodando no seu ambiente de desenvolvimento se necessário.

<!--
Obrigado pela sua contribuição 💜
Por favor, preencha todas as informações corretamente.
-->
