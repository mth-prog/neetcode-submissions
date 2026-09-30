# Two Sum

**Problema:** dado um array `nums` e um `target`, retornar os **índices** dos dois números que somam ao target.

**Exemplo:**
```
nums = [2, 7, 11, 15], target = 9
→ [0, 1]      porque nums[0] + nums[1] = 2 + 7 = 9
```

---

## Estratégia: HashMap de índices

Montar um dicionário `{valor: índice}` com todos os elementos. Depois, para cada número, calcular o que **falta** para chegar no target (`diff`) e perguntar ao mapa se esse valor existe.

```python
indices = {}

for i, n in enumerate(nums):
    indices[n] = i                                # valor → índice

for i, n in enumerate(nums):
    diff = target - n                             # o que falta pra fechar o target

    if diff in indices and indices[diff] != i:
        return [i, indices[diff]]
return []                                         # nenhum par serve
```

### O primeiro loop monta o mapa invertido

`enumerate(nums)` entrega os pares **`(índice, valor)`** a cada volta, sem precisar de contador manual:

```python
for i, n in enumerate([2, 7, 11, 15]):
    print(i, n)       # 0 2 / 1 7 / 2 11 / 3 15
#       ↑  ↑
#       i  n  →  i = índice, n = valor
```

Mas a gravação no dict **troca os dois de lugar**: `indices[n] = i` usa o `n` (valor) como chave e o `i` (índice) como valor.

```
enumerate dá        gravamos           dict fica
(0, 2)        →     indices[2] = 0     {2: 0}
(1, 7)        →     indices[7] = 1     {2: 0, 7: 1}
(2, 11)       →     indices[11] = 2    {2: 0, 7: 1, 11: 2}
(3, 15)       →     indices[15] = 3    {2: 0, 7: 1, 11: 2, 15: 3}
```

É por isso que **os valores do array viram chaves**:
```
nums    = [2, 7, 11, 15]      ← lista: índice → valor
indices = {2: 0, 7: 1, 11: 2, 15: 3}
           ↑     ↑
         valor  índice        ← dict: valor → índice (invertido!)
```

**E por que guardar o índice?** Porque é isso que o problema pede de volta — a resposta é `[0, 1]`, não `[2, 7]`. O índice vai junto de carona só pra poder ser devolvido no final. Se o enunciado pedisse os *números*, um `set` dos valores já resolveria, sem dict nenhum.

---

## Conceito: HashMap

Um **hashmap** guarda pares **chave → valor** e acha qualquer chave em **O(1)**: passa a chave por uma função de hash que aponta direto pra posição na memória — não varre a coleção.

A sacada aqui é **qual informação virou chave**. A lista já responde "qual o valor do índice 2?", mas a pergunta do problema é a inversa: *"existe o número 7 em algum lugar, e onde?"*. Então o mapa é construído invertido — valor como chave, índice como valor:

```python
nums = [2, 7, 11, 15]

7 in nums                    # True, mas custa O(n) — varre a lista
nums.index(7)                # 1, também O(n)

indices = {2: 0, 7: 1, 11: 2, 15: 3}
7 in indices                 # True em O(1)
indices[7]                   # 1 — o índice vem de graça junto
```

**É o padrão que mais aparece em problema de array/string** — quase sempre a pergunta cai em um destes moldes:

| A pergunta | Estrutura | Problema |
|---|---|---|
| "já vi esse valor antes?" | `set` de visitados | Contains Duplicate |
| "quantas vezes aparece?" | `dict` contador | Is Anagram |
| "em que índice está?" | `dict` valor → índice | **Two Sum** |
| "quem tem a mesma assinatura?" | `dict` chave → lista | Group Anagrams |

Como cada busca é O(1), os dois loops somados ficam O(n) — contra O(n²) da força bruta, que compara cada par. O custo é O(n) de espaço pro mapa.

---

## A linha-chave

```python
if diff in indices and indices[diff] != i:
    return [i, indices[diff]]
```

| Parte | O que faz |
|---|---|
| `diff in indices` | procura `diff` nas **chaves** do dict (nunca nos valores) → existe esse número no array? |
| `indices[diff]` | em que índice ele está |
| `!= i` | esse índice não é o meu próprio |
| `return [i, indices[diff]]` | devolve os dois **índices** |

### `diff in indices` valida a CHAVE, não o valor

Essa é a parte que mais engana. O `in` num dicionário percorre **somente as chaves** — ele nunca olha o outro lado do par:

```python
indices = {2: 0, 7: 1, 11: 2, 15: 3}

list(indices.keys())     # [2, 7, 11, 15]   ← é SÓ aqui que o `in` procura
list(indices.values())   # [0, 1, 2, 3]     ← o `in` nunca chega aqui
```

E como o mapa foi montado invertido, as chaves são os **números do array**. Então `diff in indices` pergunta *"existe um número igual a `diff`?"* — não tem nada a ver com índice:

```python
7 in indices             # True   → existe o número 7 no array
3 in indices             # False  → não existe o número 3

0 in indices             # False  ← pegadinha! o 0 está no mapa...
0 in indices.values()    # True   ← ...mas como VALOR (índice do 2), não como chave
```

O `0` está no dicionário e ainda assim `0 in indices` dá `False`: ele mora do lado errado do par. Pra olhar os valores você teria que pedir explicitamente, com `.values()` — e aí a busca voltaria a ser O(n), porque `.values()` é varrido um por um.

### `!= i` evita usar o mesmo elemento duas vezes

Se `n` é metade do target, o `diff` é o próprio `n` — e o mapa devolve o índice dele mesmo. Sem essa checagem, `2 + 2 = 4` passaria usando um único `2`.

```
nums = [2, 3], target = 4      →  indices = {2: 0, 3: 1}

i=0  n=2  diff = 4-2 = 2  → 2 in indices? sim, indices[2] = 0
                          → 0 != 0 ? NÃO  → não serve, continua
i=1  n=3  diff = 4-3 = 1  → 1 in indices? não  → continua
→ return []                    resposta certa: não existe par
```

> O `and` também protege: ele só avalia `indices[diff]` **se** a chave existir. Na ordem inversa daria `KeyError`.

### `return [i, indices[diff]]` devolve posições, não números

```
nums = [2, 7, 11, 15], target = 9

i=0  n=2  diff = 9-2 = 7  → 7 in indices? sim, indices[7] = 1
                          → 1 != 0 ? sim  → return [0, 1]
                                                   ↑  ↑
                                    índice atual ──┘  └── índice do complemento
```

`[0, 1]` são **posições**. Os números somados são `nums[0] + nums[1] = 2 + 7 = 9`. Retornar `[2, 7]` seria a resposta errada.

**Quando a resposta não está no começo:**
```
nums = [4, 5, 6], target = 11  →  indices = {4: 0, 5: 1, 6: 2}

i=0  n=4  diff = 7  → 7 in indices? não          → continua
i=1  n=5  diff = 6  → sim, indices[6] = 2, 2 != 1 → return [1, 2]
```

---

## Intuição rápida

> Para cada número, o que falta é `target - n`.
> Guarda todos no mapa `valor → índice` primeiro, depois busca o complemento em O(1).
