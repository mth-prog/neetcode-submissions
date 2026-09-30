# Contains Duplicate

**Problema:** dado um array `nums`, retornar `True` se algum valor aparecer mais de uma vez.

**Exemplo:**
```
nums = [1, 2, 3, 1]  →  True   (o 1 repete)
nums = [1, 2, 3, 4]  →  False
```

---

## Estratégia: Set de visitados

Percorrer o array mantendo um `set` dos números já vistos. Se o número atual **já estiver no set**, é duplicado → `True`. Se não, adiciona e continua.

```python
set_nums = set()

for num in nums:
    if num in set_nums:
        return True
    set_nums.add(num)     # depois do if: senão o próprio número se acusaria
return False
```

**Passo a passo para `[1, 2, 3, 1]`:**
```
num=1 → 1 not in set()        → set_nums = {1}
num=2 → 2 not in {1}          → set_nums = {1, 2}
num=3 → 3 not in {1, 2}       → set_nums = {1, 2, 3}
num=1 → 1 in {1, 2, 3}  ✓     → return True
```

---

## Conceito: `set` em Python

Um `set` é uma coleção de **valores únicos e sem ordem**. Adicionar um valor que já existe simplesmente não faz nada.

```python
s = set()          # set vazio (cuidado: {} cria um dict, não um set)
s.add(1)
s.add(2)
s.add(1)           # ignorado, o 1 já está lá
print(s)           # {1, 2}   ← só 2 elementos

1 in s             # True   → busca O(1)
```

**É essa unicidade que resolve o problema.** Dá até pra usar como one-liner — se o set encolheu, alguém foi descartado por ser repetido:

```python
nums = [1, 2, 3, 1]
set(nums)                      # {1, 2, 3}  ← o 1 duplicado sumiu
len(set(nums)) != len(nums)    # 3 != 4  →  True
```

> O loop com `return True` no meio ainda é melhor: **para no primeiro** duplicado, sem montar o set inteiro.

---

## Por que `set` e não `list`?

O caminho até chegar no set:

| Ideia | Como | Tempo |
|---|---|---|
| dois ponteiros | `i` contra todo `j = i+1` — loop aninhado | O(n²) |
| ordenar | `nums.sort()`, duplicado vira vizinho | O(n log n) |
| **set de visitados** | `in` por hash | **O(n)** |

O `set` usa hash internamente → `in` é O(1) independente do tamanho, e a estrutura **já recusa repetido por natureza**. Na `list` o mesmo `in` varre elemento a elemento, O(n), e o loop aninhado vira O(n²).

Custo: O(n) de espaço. O `sort` gasta O(1) de espaço, mas **modifica o array original**.

---

## Intuição rápida

> `set` só guarda valor único.
> "Se o número **já está** no set, ele apareceu antes → duplicado."
