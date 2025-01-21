def dollars_to_dirhams(dollars):
    """
    Convertit un montant en dollars americains (USD) en dirhams marocains (MAD).

    Le taux de conversion utilise est de 1 USD = 10.02 MAD (au 20/01/2025).

    Args:
        dollars (float): Le montant en dollars a convertir.

    Returns:
        float: Le montant equivalent en dirhams marocains.
    """
    return dollars * 10.02  # as of 20/01/2025

def meters_to_kilometers(meters):
    """
    Convertit une distance en metres en kilometres.

    1 kilometre equivaut a 1000 metres.

    Args:
        meters (float): La distance en metres a convertir.

    Returns:
        float: La distance equivalente en kilometres.
    """
    return meters / 1000

