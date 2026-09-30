# CLAUDE.md

Repo de submissions do NeetCode (sincronizadas automaticamente). O trabalho manual aqui é **escrever/manter os READMEs de cada problema** — anotações de estudo em português, feitas pra **revisar depois**: relembrar o conceito e reentender o código sem ter que resolver o problema de novo.

O `README.md` da raiz é gerado pela integração do NeetCode — não editar.

## Onde fica

```
Data Structures & Algorithms/<problema>/README.md    ← extensão .md minúscula
Data Structures & Algorithms/<problema>/submission-N.py
```

## Esqueleto do README

Cinco seções, nessa ordem:

**1. Cabeçalho**
````markdown
# <Nome do problema>

**Problema:** enunciado em 1 frase.

**Exemplo:**
```
entrada  →  saída      (com o porquê ao lado)
```
````

**2. `## Estratégia: <nome da abordagem>`**
Parágrafo curto explicando a ideia, o código com comentários inline (`← ...` ou `# ...` explicando o *porquê*, não o *o quê*) e o estado final da estrutura de dados.
Se alguma transformação não é óbvia (ex: montar um mapa invertido), abrir uma `###` aqui mostrando ela **acontecendo passo a passo**, não só o resultado.

**3. `## Conceito: <nome do conceito>`**
A ideia **transferível**, nomeada de forma genérica — `HashMap`, não "dict"; `Two Pointers`, não "while i < j". É a seção que serve pros *próximos* exercícios, não só pra esse.
Incluir a tabela de moldes abaixo (copiada, com o problema atual em negrito), e fechar com uma frase de complexidade — sem seção `Complexidade` separada.

**4. `## A linha-chave`** (ou `## As linhas-chave`)
A linha densa do código, destrinchada:
- tabela `| Parte | O que faz |`
- uma subseção `###` por token que engana, cada uma com exemplo executável isolado
- **trace de execução** iteração por iteração
- **contraexemplo** ao lado de toda pegadinha

**5. `## Intuição rápida`**
Blockquote de 2 linhas. A frase que você quer lembrar batendo o olho.

## Tabela de moldes (copiar em toda doc)

Copiar **inteira** em cada README, com o problema atual em negrito. O valor dela é reconhecer o molde num problema novo, então ela precisa estar em qualquer doc que você abra — sem link pra arquivo externo, revisão é abrir um arquivo só.

```markdown
| A pergunta | Estrutura | Problema |
|---|---|---|
| "já vi esse valor antes?" | `set` de visitados | Contains Duplicate |
| "quantas vezes aparece?" | `dict` contador | Is Anagram |
| "em que índice está?" | `dict` valor → índice | Two Sum |
| "quem tem a mesma assinatura?" | `dict` chave → lista | Group Anagrams |
```

## Regras

**Explicar por que o código tem a forma que tem**, ligando à exigência do enunciado. Ex: o dict do Two Sum é `valor → índice` porque o problema pede índices de volta — se pedisse os números, um `set` bastaria. É o tipo de coisa que não se recupera lendo o código depois.

**Todo trace precisa exercitar o ramo interessante.** O exemplo do enunciado costuma acertar de primeira e esconder o mecanismo. Então: letra repetida, par que não existe, resposta que só sai na 2ª iteração. Se o trace todo cai no mesmo caso, acrescentar um segundo com o caso oposto.

**Toda pegadinha vem com contraexemplo ao lado**, não só com a afirmação:
```python
0 in indices             # False  ← o 0 está no mapa...
0 in indices.values()    # True   ← ...mas como valor, não como chave

d[[1, 2, 3]] = "x"       # TypeError: unhashable type: 'list'
d[(1, 2, 3)] = "x"       # funciona
```

**Não comparar as submissions entre si, nem citar `submission-N`.** A doc resume o exercício e seus conceitos, não o histórico de tentativas. Abordagem alternativa entra como *ideia sem dono* — uma linha de tabela (`ordenar → O(n log n)`), nunca uma seção `Alternativa: submission-10.py`.

**Não parafrasear o código em prosa.** Se a frase só traduz a linha pra português ("`set_nums.add(num)` → adiciona o número ao set"), corta: o código já disse. Explicar só o que *não* está visível — ordem que importa, erro evitado, custo escondido.

**Tamanho não é problema se o volume for exemplo executável e trace.** É problema quando é prosa. Doc de 150 linhas cheia de trace se lê rápido; 60 linhas de parágrafo, não.

**Rodar os exemplos antes de commitar.** Todo `# saída` escrito na doc é conferido de verdade (`python3 -c ...`) — inclusive mensagens de erro, que mudam entre versões.

## Referências

`two-integer-sum/README.md` e `anagram-groups/README.md` são as mais completas — usar como modelo.

## Escrita

Português informal, 2ª pessoa. Tabelas > listas quando houver comparação. Setas (`→`, `←`) e blocos de código pra tudo que for estado ou fluxo. Negrito no termo que carrega a ideia, não em frase inteira.
