def calcular_descuento(monto_compra, porcentaje_descuento=10):
    """
    Calcula el descuento a aplicar a un monto de compra.

    Parámetros:
      monto_compra (float): El monto total de la compra.
      porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorno:
      float: El monto del descuento calculado.
    """
    descuento = monto_compra * porcentaje_descuento / 100
    return descuento

# Ejemplo de uso 1
monto_compra = 100
descuento = calcular_descuento(monto_compra)
monto_final = monto_compra - descuento

print(f"\n**Ejemplo 1**")
print(f"Monto de la compra: ${monto_compra}")
print(f"Descuento aplicado: {calcular_descuento.__defaults__[0]}%")  # Accedemos al porcentaje de descuento predeterminado
print(f"Monto del descuento: ${descuento}")
print(f"Monto final a pagar: ${monto_final}")



