# Módulo para determinar la cantidad exacta a pedir (Lógica de Negocio)
def calcular_pedido(stock_actual, stock_minimo):
    # Si el Stock Actual es menor al Stock Mínimo, la cantidad a pedir es la diferencia
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual  
    # Si el Stock Actual es suficiente, la cantidad a pedir es cero
    else:
        return 0  

# Programa Principal
def main():
    # Matriz inicial con 5 artículos: [Código, Nombre, Stock Actual, Stock Mínimo]
    inventario = [
        ["A001", "Teclado Mecánico", 12, 15],
        ["A002", "Mouse Óptico", 25, 20],
        ["A003", "Monitor 24'", 3, 8],
        ["A004", "Memoria RAM 16GB", 30, 25],
        ["A005", "Disco Duro SSD 1TB", 5, 10]
    ]
    
    print("=== INFORME DE AUDITORÍA DE INVENTARIO Y PEDIDOS ===")
    print("-" * 55)
    
    # Recorrer la matriz para procesar los datos
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamado al módulo/función pasándole los datos numéricos correspondientes
        cantidad_a_pedir = calcular_pedido(stock_actual, stock_minimo)
        
        # Salida: Mostrar nombre del artículo y la cantidad exacta que debe ser solicitada
        print(f"Artículo: {nombre:<22} | Cantidad a pedir: {cantidad_a_pedir}")

if __name__ == "__main__":
    main()
