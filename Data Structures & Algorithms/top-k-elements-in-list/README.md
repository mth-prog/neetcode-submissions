# Top K Frequent Elements

**Problema:** dado um array `nums` e um `k`, retornar os `k` elementos **mais frequentes**.

**Exemplo:**
```
nums = [1, 1, 2, 2, 3], k = 2
→ [2, 1]      o 1 e o 2 aparecem 2x cada; o 3 só 1x, fica fora
```

---

## Estratégia: contar, ordenar pela frequência, tirar do fim

Duas perguntas diferentes, duas estruturas. Primeiro *"quantas vezes cada número aparece?"* — isso é dict contador. Depois *"quem são os maiores?"* — e dict não tem ordem útil pra isso, então a contagem é despejada numa lista de pares e ordenada.

```python
indices = {}

for num in nums:
    indices[num] = 1 + indices.get(num, 0)   # .get(num, 0) → primeira vez vale 0, sem KeyError

arr = []
for num, freq in indices.items():
    arr.append([freq, num])                  # freq PRIMEIRO — é por ela que o sort vai ordenar

arr.sort()                                   # crescente: os mais frequentes vão pro FIM

res = []
while len(res) < k:
    res.append(arr.pop()[1])                 # pop() tira do fim (o maior); [1] pega o num do par
return res
```

**Como as estruturas ficam** (`nums = [1, 1, 2, 2, 3]`):
```
indices = {1: 2, 2: 2, 3: 1}        ← num → quantas vezes

arr     = [[2, 1], [2, 2], [1, 3]]  ← [freq, num], na ordem que o dict entregou
arr.sort()
arr     = [[1, 3], [2, 1], [2, 2]]  ← menos frequente na frente, mais frequente no fim
                            ↑
                      o pop() come daqui pra trás
```

### O par é `[freq, num]`, invertido em relação ao dict

O dict é `num → freq`, mas o par gravado na lista é `[freq, num]`. A troca é de propósito: `sort()` ordena pelo **primeiro** elemento, e quem manda na resposta é a frequência.

```
dict dá                 gravamos                 arr fica
(num=1, freq=2)    →    arr.append([2, 1])       [[2, 1]]
(num=2, freq=2)    →    arr.append([2, 2])       [[2, 1], [2, 2]]
(num=3, freq=1)    →    arr.append([1, 3])       [[2, 1], [2, 2], [1, 3]]
                                     ↑  ↑
                                  freq  num      ← o num vira carona
```

O `num` só viaja de carona porque é ele que a resposta pede de volta. Se o problema pedisse as frequências, bastaria ordenar `indices.values()`.

---

## Conceito: HashMap

Um **hashmap** guarda pares **chave → valor** e acha qualquer chave em **O(1)**: passa a chave por uma função de hash que aponta direto pra posição na memória — não varre a coleção.

**É o padrão que mais aparece em problema de array/string** — quase sempre a pergunta cai em um destes moldes:

| A pergunta | Estrutura | Problema |
|---|---|---|
| "já vi esse valor antes?" | `set` de visitados | Contains Duplicate |
| "quantas vezes aparece?" | `dict` contador | Is Anagram |
| "em que índice está?" | `dict` valor → índice | Two Sum |
| "quem tem a mesma assinatura?" | `dict` chave → lista | Group Anagrams |
| "quem aparece mais?" | `dict` contador + ordenar | **Top K Frequent Elements** |

Aqui o molde é o contador **mais um segundo passo**: o dict responde *quanto*, mas não responde *quem é o maior* — dict não se ordena. Então a sacada é **mudar de estrutura no meio do caminho**: a contagem sai do dict e vira lista de pares, onde a ordenação existe.

E a chave da nova estrutura é a **frequência**, não o número. É o que decide a resposta que vai na frente do par.

Tempo O(n log n), dominado pelo `sort()` — a contagem é O(n) e o `pop()` é O(1) por elemento. Espaço O(n).

| Ideia | Custo |
|---|---|
| ordenar os pares (aqui) | O(n log n) |
| heap de tamanho k | O(n log k) |
| bucket sort por frequência (freq ≤ n) | O(n) |

---

## As linhas-chave

```python
arr.sort()
res.append(arr.pop()[1])
```

| Parte | O que faz |
|---|---|
| `arr.sort()` | ordena **no lugar** e devolve `None` — por isso é uma linha solta, sem `arr = ` |
| | compara os pares elemento por elemento → ordena pela **freq** (posição 0) |
| `arr.pop()` | remove e devolve o **último** par, o de maior freq |
| `[1]` | indexa o par devolvido e pega o `num` |

### `sort()` compara lista por lista, da esquerda pra direita

Não existe "ordenar por frequência" no código em lugar nenhum — isso é consequência de a freq estar na posição 0 do par. Python compara o primeiro item de cada lista; só em caso de empate olha o segundo.

```python
sorted([[2, 1], [2, 2], [1, 3]])    # [[1, 3], [2, 1], [2, 2]]
#                                      ↑ freq 1   ↑ empate em 2 → desempata pelo num
```

**Contraexemplo — par na ordem `[num, freq]` quebra tudo:**
```python
sorted([[1, 2], [2, 2], [3, 1]])    # [[1, 2], [2, 2], [3, 1]]
#                                      ordenou pelo NÚMERO
#                                      o fim é [3, 1] → pop devolveria o 3, que só aparece 1x
```

É por isso que a ordem dentro do par é o ponto do exercício inteiro. Trocar `[freq, num]` por `[num, freq]` não dá erro — dá resposta errada em silêncio.

> `sort()` ordena no lugar e retorna `None`; `sorted()` retorna uma lista nova.
> ```python
> x = [3, 1, 2]
> print(x.sort())     # None   ← escrever `x = x.sort()` perderia a lista
> print(x)            # [1, 2, 3]
> ```

### `pop()[1]` ≠ `pop(1)`

Duas coisas totalmente diferentes, um caractere de distância. `pop()` sem argumento tira do **fim**; o `[1]` depois indexa **o que saiu**. Já `pop(1)` tira o elemento **do índice 1** da lista.

```python
a = [[1, 'a'], [2, 'b'], [3, 'c']]
a.pop()[1]          # 'c'          ← tira [3,'c'] do fim e pega a posição 1 DELE

b = [[1, 'a'], [2, 'b'], [3, 'c']]
b.pop(1)            # [2, 'b']     ← tira o par do MEIO e devolve o par inteiro
b                   # [[1,'a'], [3,'c']]
```

E `pop()` tirar do fim é o que torna ele O(1) — nada é deslocado. Com `pop(0)` (ordenando decrescente) cada remoção reindexaria a lista toda, O(n).

### Trace: `nums = [1, 1, 2, 2, 3]`, `k = 2`

Esse caso tem **empate de frequência**, que é o que faz o segundo item do par importar:

```
contagem   indices = {1: 2, 2: 2, 3: 1}
arr bruto  [[2, 1], [2, 2], [1, 3]]
arr.sort() [[1, 3], [2, 1], [2, 2]]

res = []           len(res)=0 < 2 → pop() = [2, 2] → [1] = 2 → res = [2]
                                    arr = [[1, 3], [2, 1]]
res = [2]          len(res)=1 < 2 → pop() = [2, 1] → [1] = 1 → res = [2, 1]
                                    arr = [[1, 3]]
res = [2, 1]       len(res)=2     → para
→ [2, 1]           o 3 nunca foi tocado: ficou no começo da lista
```

**Caso sem empate, resposta só na 2ª rodada** (`nums = [1, 2, 2, 3, 3, 3]`, `k = 2`):
```
indices = {1: 1, 2: 2, 3: 3}
arr.sort() → [[1, 1], [2, 2], [3, 3]]

pop() = [3, 3] → res = [3]
pop() = [2, 2] → res = [3, 2]
→ [3, 2]       sai em ordem decrescente de frequência, de graça
```

> **Pegadinha:** o `while` confia que existem pelo menos `k` números distintos. Se `k` fosse maior que `len(arr)`, a lista esvazia e o `pop()` estoura:
> ```python
> [].pop()        # IndexError: pop from empty list
> ```
> O enunciado garante `k ≤ número de distintos`, então não dá problema aqui — mas é a condição invisível que esse `while` está assumindo.

---

## Intuição rápida

> Conta num dict, despeja em lista de pares `[freq, num]` — **freq na frente, porque é por ela que o `sort()` ordena**.
> Ordenado crescente, os campeões ficam no fim: `pop()` pega o par, `[1]` tira o número de dentro.
