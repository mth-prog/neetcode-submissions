# Two Sum

**Problema:** dado um array `nums` e um `target`, retornar os **índices** dos dois números que somam ao target.

**Exemplo:**
```
nums = [2, 7, 11, 15], target = 9
→ [0, 1]  (2 + 7 = 9)
```

---

## Estratégia: HashMap de índices

Construir um dicionário `{valor: índice}` para todos os elementos. Depois percorrer o array calculando o `diff = target - n` e verificar se ele existe no mapa.

```python
indices = {}

for i, n in enumerate(nums):
    indices[n] = i

for i, n in enumerate(nums):
    diff = target - n

    if diff in indices and indices[diff] != i:
        return [i, indices[diff]]
return []
```

**Mapa gerado para `[2, 7, 11, 15]`:**
```
indices = {2: 0, 7: 1, 11: 2, 15: 3}
```

---

## Detalhando cada parte

**`enumerate(nums)`** → transforma a lista em pares `(índice, valor)` a cada iteração. Sem ele, você precisaria de um contador manual.

```python
nums = [2, 7, 11, 15]

# sem enumerate
for i in range(len(nums)):
    print(i, nums[i])

# com enumerate — equivalente, mais limpo
for i, n in enumerate(nums):
    print(i, n)

# saída em ambos os casos:
# 0 2
# 1 7
# 2 11
# 3 15
```

**`diff = target - n`** → o valor que precisamos encontrar para completar a soma.

**`if diff in indices`** → busca a **chave** no dicionário (não o valor). O(1) por ser HashMap.

**`indices[diff] != i`** → garante que não estamos usando o mesmo elemento duas vezes. Ex: `target = 4, nums = [2, 3]` — o diff de `2` é `2`, mas não podemos usar o mesmo índice `0`.

**`return [i, indices[diff]]`** → `i` é o índice atual; `indices[diff]` é o índice do complemento encontrado anteriormente.

---

## Complexidade

- **Tempo:** O(n) — dois loops lineares separados
- **Espaço:** O(n) — o dicionário armazena todos os elementos

---

## Intuição rápida

> "Para cada número, o complemento que falta é `target - n`.  
> Guarda todos no mapa primeiro, depois busca o complemento em O(1)."

