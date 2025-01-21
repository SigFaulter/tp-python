def add(a, b):
    """
    Effectue l'addition de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxieme nombre.

    Returns:
        float: La somme des deux nombres.
    """
    return a + b

def subtract(a, b):
    """
    Effectue la soustraction de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxieme nombre.

    Returns:
        float: La difference entre les deux nombres.
    """
    return a - b

def multiply(a, b):
    """
    Effectue la multiplication de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxieme nombre.

    Returns:
        float: Le produit des deux nombres.
    """
    return a * b

def divide(a, b):
    """
    Effectue la division de deux nombres.

    Args:
        a (float): Le numerateur.
        b (float): Le denominateur.

    Raises:
        ValueError: Si le denominateur est egal a zero.

    Returns:
        float: Le resultat de la division.
    """
    if b == 0:
        raise ValueError("Division sur 0 est impossible")
    return a / b

