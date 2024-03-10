# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [    # Ciudad 1
        [    # Semana 1
            {"día": "Lunes", "temperatura": 25},
            {"día": "Martes", "temperatura": 34},
            {"día": "Miércoles", "temperatura": 30},
            {"día": "Jueves", "temperatura": 14},
            {"día": "Viernes", "temperatura": 18},
            {"día": "Sábado", "temperatura": 26},
            {"día": "Domingo", "temperatura": 24}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 76},
            {"día": "Martes", "temperatura": 79},
            {"día": "Miércoles", "temperatura": 83},
            {"día": "Jueves", "temperatura": 81},
            {"día": "Viernes", "temperatura": 87},
            {"día": "Sábado", "temperatura": 89},
            {"día": "Domingo", "temperatura": 93}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 77},
            {"día": "Martes", "temperatura": 81},
            {"día": "Miércoles", "temperatura": 85},
            {"día": "Jueves", "temperatura": 82},
            {"día": "Viernes", "temperatura": 88},
            {"día": "Sábado", "temperatura": 91},
            {"día": "Domingo", "temperatura": 95}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 75},
            {"día": "Martes", "temperatura": 78},
            {"día": "Miércoles", "temperatura": 80},
            {"día": "Jueves", "temperatura": 79},
            {"día": "Viernes", "temperatura": 84},
            {"día": "Sábado", "temperatura": 87},
            {"día": "Domingo", "temperatura": 91}
        ]
    ],
    [    # Ciudad 2
        [    # Semana 1
            {"día": "Lunes", "temperatura": 62},
            {"día": "Martes", "temperatura": 64},
            {"día": "Miércoles", "temperatura": 68},
            {"día": "Jueves", "temperatura": 70},
            {"día": "Viernes", "temperatura": 73},
            {"día": "Sábado", "temperatura": 75},
            {"día": "Domingo", "temperatura": 79}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 63},
            {"día": "Martes", "temperatura": 66},
            {"día": "Miércoles", "temperatura": 70},
            {"día": "Jueves", "temperatura": 72},
            {"día": "Viernes", "temperatura": 75},
            {"día": "Sábado", "temperatura": 77},
            {"día": "Domingo", "temperatura": 81}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 61},
            {"día": "Martes", "temperatura": 65},
            {"día": "Miércoles", "temperatura": 68},
            {"día": "Jueves", "temperatura": 70},
            {"día": "Viernes", "temperatura": 72},
            {"día": "Sábado", "temperatura": 76},
            {"día": "Domingo", "temperatura": 80}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 64},
            {"día": "Martes", "temperatura": 67},
            {"día": "Miércoles", "temperatura": 69},
            {"día": "Jueves", "temperatura": 71},
            {"día": "Viernes", "temperatura": 74},
            {"día": "Sábado", "temperatura": 77},
            {"día": "Domingo", "temperatura": 80}
        ]
    ],
    [    # Ciudad 3
        [    # Semana 1
            {"día": "Lunes", "temperatura": 90},
            {"día": "Martes", "temperatura": 92},
            {"día": "Miércoles", "temperatura": 94},
            {"día": "Jueves", "temperatura": 91},
            {"día": "Viernes", "temperatura": 88},
            {"día": "Sábado", "temperatura": 85},
            {"día": "Domingo", "temperatura": 82}
        ],
        [    # Semana 2
            {"día": "Lunes", "temperatura": 89},
            {"día": "Martes", "temperatura": 91},
            {"día": "Miércoles", "temperatura": 93},
            {"día": "Jueves", "temperatura": 90},
            {"día": "Viernes", "temperatura": 87},
            {"día": "Sábado", "temperatura": 84},
            {"día": "Domingo", "temperatura": 81}
        ],
        [    # Semana 3
            {"día": "Lunes", "temperatura": 91},
            {"día": "Martes", "temperatura": 93},
            {"día": "Miércoles", "temperatura": 95},
            {"día": "Jueves", "temperatura": 92},
            {"día": "Viernes", "temperatura": 89},
            {"día": "Sábado", "temperatura": 86},
            {"día": "Domingo", "temperatura": 83}
        ],
        [    # Semana 4
            {"día": "Lunes", "temperatura": 88},
            {"día": "Martes", "temperatura": 90},
            {"día": "Miércoles", "temperatura": 92},
            {"día": "Jueves", "temperatura": 89},
            {"día": "Viernes", "temperatura": 86},
            {"día": "Sábado", "temperatura": 83},
            {"día": "Domingo", "temperatura": 80}
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
