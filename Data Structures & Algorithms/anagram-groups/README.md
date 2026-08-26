# Group Anagrams

**Problema:** dado um array de strings `strs`, agrupar as que são anagramas entre si e retornar os grupos.

**Exemplo:**
```
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
→ [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

---

## Estratégia: Fingerprint de frequência como chave

Anagramas têm exatamente as mesmas letras nas mesmas quantidades. Então a ideia é criar uma **assinatura única** (fingerprint) para cada string baseada na contagem de letras — e usar essa assinatura como chave de um dicionário para agrupar.

```python
res = defaultdict(list)

for s in strs:
    count = [0] * 26                      # array de 26 posições, uma por letra
    for c in s:
        count[ord(c) - ord('a')] += 1     # incrementa a posição da letra

    res[tuple(count)].append(s)           # agrupa pela assinatura

return list(res.values())
```

---

## Detalhando cada parte

**`defaultdict(list)`** → dicionário que cria automaticamente uma lista vazia para chaves novas — é como setar o **padrão** do próximo item. Sem ele, você precisaria checar se a chave existe antes de usar `.append()`:

```python
# sem defaultdict — mais verboso
if key not in res:
    res[key] = []
res[key].append(s)

# com defaultdict(list) — já sabe que o padrão é lista vazia
res[key].append(s)
```

**`count = [0] * 26`** → lista com 26 zeros, um para cada letra do alfabeto (a=0, b=1, ..., z=25).

**`ord(c) - ord('a')`** → converte a letra para o índice correto no array:
```
ord('a') = 97
ord('c') = 99
ord('c') - ord('a') = 2  →  posição 2 no array (terceira letra)
```

**`tuple(count)`** → converte a lista para tuple porque **listas não podem ser chaves de dicionário** (não são hasháveis), tuples sim.

**Fingerprint de `"eat"` e `"tea"`:**
```
"eat" → count[4]+=1, count[0]+=1, count[19]+=1 → (1,0,0,0,1,0,...,1,...,0)
"tea" → count[19]+=1, count[4]+=1, count[0]+=1 → (1,0,0,0,1,0,...,1,...,0)
```
Mesma assinatura → mesmo grupo. ✓

**Como o `res` fica ao final para `["eat","tea","tan","ate","nat","bat"]`:**
```
res = {
    (1,0,0,0,1,0,...,1,...,0): ["eat", "tea", "ate"],   # a=1, e=1, t=1
    (1,0,0,0,0,0,...,1,1,...): ["tan", "nat"],           # a=1, n=1, t=1
    (1,1,0,0,0,0,...,0,1,...): ["bat"],                  # a=1, b=1, t=1
}

# list(res.values())
→ [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## Complexidade

- **Tempo:** O(n · k) — onde `n` é o número de strings e `k` o tamanho da maior string
- **Espaço:** O(n · k) — para armazenar todos os grupos

> Mais eficiente que ordenar cada string (`O(n · k log k)`), pois o array de 26 posições tem custo fixo.

---

## Intuição rápida

> Anagramas têm a mesma "impressão digital" de letras.  
> Conta as letras de cada string → transforma em tuple → usa como chave do dict para agrupar automaticamente.
