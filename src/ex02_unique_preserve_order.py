"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.

    Ejemplo:
    - [3, 1, 3, 2, 1] -> [3, 1, 2]

    Requisito:
    - No modifiques la lista original.
    """
    seen = set()
    unique_values = []
    for value in values:
        if value not in seen:
            unique_values.append(value)
            seen.add(value)
    return unique_values
    raise NotImplementedError("Implementa unique_preserve_order(values)")
