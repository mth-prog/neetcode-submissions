# Contains Duplicate

**Problema:** dado um array `nums`, retornar `True` se algum valor aparecer mais de uma vez.

---

## Estratégia: Set de visitados

Percorrer o array mantendo um `set` dos números já vistos. Se o número atual **já estiver no set**, ele é duplicado → retorna `True`. Se não, adiciona e continua.

```python
set_nums = set()

for num in nums:
    if num in set_nums:
        return True
    set_nums.add(num)
return False
```

---

## Por que `set`?

| Estrutura | Busca (`in`) |
|-----------|-------------|
| lista     | O(n)        |
| **set**   | **O(1)**    |

`set` usa hash internamente → busca em tempo constante, independente do tamanho.  
`list` precisaria percorrer elemento a elemento.

---

## Complexidade

- **Tempo:** O(n) — um único passo pelo array
- **Espaço:** O(n) — no pior caso, todos os elementos entram no set antes de achar um duplicado

---

## Intuição rápida

> "Se o número **já está** no set, ele apareceu antes → duplicado."  
> Adiciona só depois de checar, senão o próprio número se detectaria como duplicado.
