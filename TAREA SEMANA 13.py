# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [    # Ciudad 1
        [    # Semana 1
            {"día": "Lunes", "temperatura": 29},
            {"día": "Martes", "temperatura": 24},
            {"día": "Miércoles", "temperatura": 32},
            {"día": "Jueves", "temperatura": 24},
            {"día": "Viernes", "temperatura": 18},
            {"día": "Sábado", "temperatura": 16},
            {"día": "Domingo", "temperatura": 14}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 26},
            {"día": "Martes", "temperatura": 19},
            {"día": "Miércoles", "temperatura": 23},
            {"día": "Jueves", "temperatura": 21},
            {"día": "Viernes", "temperatura": 37},
            {"día": "Sábado", "temperatura": 29},
            {"día": "Domingo", "temperatura": 33}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 27},
            {"día": "Martes", "temperatura": 31},
            {"día": "Miércoles", "temperatura": 35},
            {"día": "Jueves", "temperatura": 22},
            {"día": "Viernes", "temperatura": 28},
            {"día": "Sábado", "temperatura": 31},
            {"día": "Domingo", "temperatura": 25}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 25},
            {"día": "Martes", "temperatura": 18},
            {"día": "Miércoles", "temperatura": 20},
            {"día": "Jueves", "temperatura": 39},
            {"día": "Viernes", "temperatura": 14},
            {"día": "Sábado", "temperatura": 27},
            {"día": "Domingo", "temperatura": 21}
        ]
    ],
    [    # Ciudad 2
        [    # Semana 1
            {"día": "Lunes", "temperatura": 22},
            {"día": "Martes", "temperatura": 24},
            {"día": "Miércoles", "temperatura": 28},
            {"día": "Jueves", "temperatura": 20},
            {"día": "Viernes", "temperatura": 23},
            {"día": "Sábado", "temperatura": 25},
            {"día": "Domingo", "temperatura": 29}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 33},
            {"día": "Martes", "temperatura": 36},
            {"día": "Miércoles", "temperatura": 20},
            {"día": "Jueves", "temperatura": 32},
            {"día": "Viernes", "temperatura": 35},
            {"día": "Sábado", "temperatura": 27},
            {"día": "Domingo", "temperatura": 31}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 31},
            {"día": "Martes", "temperatura": 35},
            {"día": "Miércoles", "temperatura": 38},
            {"día": "Jueves", "temperatura": 20},
            {"día": "Viernes", "temperatura": 22},
            {"día": "Sábado", "temperatura": 26},
            {"día": "Domingo", "temperatura": 30}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 24},
            {"día": "Martes", "temperatura": 27},
            {"día": "Miércoles", "temperatura": 39},
            {"día": "Jueves", "temperatura": 21},
            {"día": "Viernes", "temperatura": 24},
            {"día": "Sábado", "temperatura": 27},
            {"día": "Domingo", "temperatura": 30}
        ]
    ],
    [    # Ciudad 3
        [    # Semana 1
            {"día": "Lunes", "temperatura": 20},
            {"día": "Martes", "temperatura": 32},
            {"día": "Miércoles", "temperatura": 34},
            {"día": "Jueves", "temperatura": 21},
            {"día": "Viernes", "temperatura": 38},
            {"día": "Sábado", "temperatura": 25},
            {"día": "Domingo", "temperatura": 12}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 29},
            {"día": "Martes", "temperatura": 21},
            {"día": "Miércoles", "temperatura": 33},
            {"día": "Jueves", "temperatura": 30},
            {"día": "Viernes", "temperatura": 27},
            {"día": "Sábado", "temperatura": 34},
            {"día": "Domingo", "temperatura": 21}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 21},
            {"día": "Martes", "temperatura": 1},
            {"día": "Miércoles", "temperatura": 35},
            {"día": "Jueves", "temperatura": 22},
            {"día": "Viernes", "temperatura": 19},
            {"día": "Sábado", "temperatura": 16},
            {"día": "Domingo", "temperatura": 23}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 28},
            {"día": "Martes", "temperatura": 30},
            {"día": "Miércoles", "temperatura": 32},
            {"día": "Jueves", "temperatura": 39},
            {"día": "Viernes", "temperatura": 26},
            {"día": "Sábado", "temperatura": 33},
            {"día": "Domingo", "temperatura": 10}
        ]
    ]
]

def calcular_promedio(suma_acumulada, total_acumulado):
    return round(suma_acumulada / total_acumulado, 2)

# Calcular el promedio de temperaturas para cada ciudad y semana.
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad += 1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 1
        suma = 0
        for dia in semana:
            suma += dia['temperatura']
        promedio = calcular_promedio(suma, len(semana))
        suma_promedio += promedio
        print(f'El promedio semana No. {no_semana} es: {promedio}')
    promedio_ciudad = calcular_promedio(suma_promedio, len(ciudad))
    print(f'El promedio mensual es: {promedio_ciudad}')
