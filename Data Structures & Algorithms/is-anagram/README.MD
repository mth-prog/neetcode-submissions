# Is Anagram

**Problema:** dadas duas strings `s` e `t`, retornar `True` se `t` for um anagrama de `s` (mesmas letras, qualquer ordem).

**Exemplo:**
```
s = "amj"
t = "jam"  →  True

s = "rat"
t = "car"  →  False
```

---

## Estratégia: Mapa de frequência (HashMap)

Construir um dicionário de contagem para cada string e comparar os dois. Se forem iguais, são anagramas.

```python
if len(s) != len(t):
    return False

countS, countT = {}, {}

for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)

return countS == countT
```

**Resultado dos dicts para `"amj"` / `"jam"`:**
```
countS = {"a": 1, "m": 1, "j": 1}
countT = {"j": 1, "a": 1, "m": 1}
countS == countT  →  True
```

---

## Detalhando a linha-chave

```python
countS[s[i]] = 1 + countS.get(s[i], 0)
```

| Parte | O que faz |
|---|---|
| `s[i]` | pega a letra na posição `i` da string |
| `countS.get(s[i], 0)` | busca o valor atual da chave; se não existir, retorna `0` |
| `1 + ...` | incrementa a contagem em 1 |
| `countS[s[i]] = ...` | salva/atualiza a chave no dicionário |

---

## Por que o `==` entre dicts funciona?

Em Python, `dict == dict` compara **chaves e valores** — não tamanho. Dois dicts são iguais se tiverem exatamente as mesmas chaves com os mesmos valores.

---

## Complexidade

- **Tempo:** O(n) — um único loop pelo tamanho da string
- **Espaço:** O(k) — onde `k` é o número de caracteres únicos (no máximo 26 para letras do alfabeto)

---

## Intuição rápida

> Anagrama = mesmas letras, mesma quantidade.  
> Conta a frequência de cada letra nas duas strings e compara os mapas.