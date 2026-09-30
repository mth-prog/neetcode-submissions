# Group Anagrams

**Problema:** dado um array de strings `strs`, agrupar as que são anagramas entre si e retornar os grupos.

**Exemplo:**
```
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
→ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## Estratégia: Assinatura de frequência como chave

Anagramas têm exatamente as mesmas letras nas mesmas quantidades. Então dá pra gerar uma **assinatura** de cada string contando suas letras — e usar essa assinatura como chave de um dict. Strings com a mesma assinatura caem automaticamente no mesmo grupo.

```python
res = defaultdict(list)

for s in strs:
    count = [0] * 26                      # 26 contadores, um por letra do alfabeto
    for c in s:
        count[ord(c) - ord('a')] += 1     # incrementa a posição da letra

    res[tuple(count)].append(s)           # agrupa pela assinatura

return list(res.values())                 # só os grupos, sem as chaves
```

**Como o `res` fica no final:**
```
res = {
    (1,0,0,0,1,0,...,1,...): ["eat", "tea", "ate"],    # a=1, e=1, t=1
    (1,0,0,0,0,0,...,1,1,...): ["tan", "nat"],         # a=1, n=1, t=1
    (1,1,0,0,0,0,...,0,1,...): ["bat"],                # a=1, b=1, t=1
}

list(res.values())  →  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## Conceito: HashMap

Um **hashmap** guarda pares **chave → valor** e acha qualquer chave em **O(1)**: passa a chave por uma função de hash que aponta direto pra posição na memória — não varre a coleção.

**É o padrão que mais aparece em problema de array/string** — quase sempre a pergunta cai em um destes moldes:

| A pergunta | Estrutura | Problema |
|---|---|---|
| "já vi esse valor antes?" | `set` de visitados | Contains Duplicate |
| "quantas vezes aparece?" | `dict` contador | Is Anagram |
| "em que índice está?" | `dict` valor → índice | Two Sum |
| "quem tem a mesma assinatura?" | `dict` chave → lista | **Group Anagrams** |

Aqui o molde é o **agrupamento**: cada chave guarda uma *lista* de tudo que caiu nela.

A sacada é que **a chave não precisa ser um elemento do array** — ela pode ser algo que você *calcula* a partir dele. As strings `"eat"` e `"tea"` são diferentes, mas a contagem de letras das duas é idêntica, então a assinatura vira o denominador comum. Agrupar deixa de ser "comparar todo mundo com todo mundo" e passa a ser "calcular a chave e jogar no balde certo".

Tempo O(n · k) — `n` strings de tamanho até `k`, cada uma percorrida uma vez. Espaço O(n · k) pros grupos. Ordenar cada string também funcionaria como assinatura (`sorted("eat") == sorted("tea")`), mas custaria O(n · k log k); o array de 26 posições tem custo fixo.

---

## As linhas-chave

### `count[ord(c) - ord('a')] += 1` — a letra virando posição

`count = [0] * 26` cria uma lista de 26 zeros, uma casa por letra: `a` na posição 0, `b` na 1, ..., `z` na 25. Falta converter a letra nesse número, e é o que o `ord()` faz — ele devolve o código numérico do caractere:

```python
ord('a')   # 97
ord('c')   # 99
ord('z')   # 122
```

Os códigos não começam em zero, então subtrair `ord('a')` **desloca a escala** pra alinhar com os índices da lista:

```python
ord('a') - ord('a')   # 97  - 97 = 0    → posição 0
ord('c') - ord('a')   # 99  - 97 = 2    → posição 2
ord('z') - ord('a')   # 122 - 97 = 25   → posição 25
```

**Montando a assinatura de `"eat"`:**
```
c='e'  → ord('e')-ord('a') = 4   → count[4] += 1   → [0,0,0,0,1,0,...,0]
c='a'  → ord('a')-ord('a') = 0   → count[0] += 1   → [1,0,0,0,1,0,...,0]
c='t'  → ord('t')-ord('a') = 19  → count[19] += 1  → [1,0,0,0,1,0,...,1,...,0]
                                                      ↑       ↑       ↑
                                                     a=1     e=1     t=1
```

E é aqui que os anagramas se encontram — **a ordem das letras não muda o resultado**, porque cada uma só incrementa a sua casa:
```
"eat" → soma nas casas 4, 0, 19  →  (1,0,0,0,1,0,...,1,...,0)
"tea" → soma nas casas 19, 4, 0  →  (1,0,0,0,1,0,...,1,...,0)   ← idêntico
"ate" → soma nas casas 0, 19, 4  →  (1,0,0,0,1,0,...,1,...,0)   ← idêntico
"bat" → soma nas casas 1, 0, 19  →  (1,1,0,0,0,0,...,1,...,0)   ← diferente, grupo próprio
```

### `res[tuple(count)].append(s)` — a assinatura virando chave

Duas coisas acontecem nessa linha, e cada uma resolve um problema.

**1. `tuple(count)` — porque lista não pode ser chave.** Chave de dict precisa ser **imutável** (hasheável): o hash é calculado uma vez e define onde o par mora, então se a chave pudesse mudar depois, ele apontaria pro lugar errado. `list` é mutável, `tuple` não:

```python
d = {}
d[[1, 2, 3]] = "x"     # TypeError: unhashable type: 'list'
d[(1, 2, 3)] = "x"     # funciona
```

`tuple(count)` é o mesmo conteúdo, só congelado — e é isso que o torna usável como chave.

**2. `defaultdict(list)` — porque a chave ainda não existe.** Na primeira vez que uma assinatura aparece, não há lista pra dar `.append()`. O `defaultdict(list)` já define qual é o **padrão** de uma chave nova: uma lista vazia.

```python
res = {}                    # dict normal
res[chave].append(s)        # KeyError!  ← a chave nem existe ainda

res = defaultdict(list)     # o padrão de chave nova é []
res[chave].append(s)        # funciona: cria [] e já dá append
```

**Executando para `["eat", "tea", "tan", "ate", "nat", "bat"]`.** Cada chave é o `tuple(count)` inteiro, com os 26 números — apelido de `A`/`B`/`C` só pra caber na linha:

```
A = 1 nas posições 0(a), 4(e), 19(t)    → (1,0,0,0,1,0,...,1,...,0)
B = 1 nas posições 0(a), 13(n), 19(t)   → (1,0,...,1,...,1,...,0)
C = 1 nas posições 0(a), 1(b), 19(t)    → (1,1,0,...,1,...,0)
```
```
s="eat"  → chave A  → chave nova   → res = {A: ["eat"]}
s="tea"  → chave A  → já existe    → res = {A: ["eat", "tea"]}
s="tan"  → chave B  → chave nova   → res = {A: ["eat", "tea"], B: ["tan"]}
s="ate"  → chave A  → já existe    → res = {A: ["eat", "tea", "ate"], B: ["tan"]}
s="nat"  → chave B  → já existe    → res = {A: [...], B: ["tan", "nat"]}
s="bat"  → chave C  → chave nova   → res = {A: [...], B: [...], C: ["bat"]}
```

Note que o agrupamento nunca compara duas strings entre si — cada uma só calcula sua chave e é depositada. O `"bat"` fica sozinho no grupo dele sem precisar de checagem nenhuma.

No fim, `list(res.values())` descarta as assinaturas (elas eram só o meio pra agrupar) e devolve **as listas**: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`.

---

## Intuição rápida

> Anagramas têm a mesma "impressão digital" de letras.
> Conta as letras → congela em tuple → usa como chave do dict, e o agrupamento sai de graça.
