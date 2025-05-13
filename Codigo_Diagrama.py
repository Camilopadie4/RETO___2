classDiagram
direction TB
    class Cliente {
	    -Nombre_completo: string
	    -Id: int
	    +Seleccionar_Lavado(tipo: String)
    }
    class Estacion_Lavado {
	    +Id: int
	    +rodillos: List~~
	    +dispensador_Agua: Dispensador_Agua
	    +Sensores: List~~
	    +dispensador_Jabon: Dispensador_Jabon
	    +ActivarSensores()
	    +AplicarAgua()
	    +SecarVehiculo()
	    +AplicarJabon()
	    +IniciarRodillos()
    }
    class Sistema_pago {
	    +Monto: Double
	    +Tipo-de-pago: String
	    +ProcesarPago()
    }
    class Sensor {
	    +Estado
	    +Tipo
	    +Ajustar_Configuracion_Lavado()
	    +Detectar_Vehiculo()
    }
    class Rodillo {
	    +Estado: Boolean
	    +Material: string
	    +Activar_rodillo()
    }
    class Dispensador_agua {
	    + capacidad: Double
	    +Dispensar_agua()
    }
    class Dispensar_jabon {
	    +cantidad-Disponible: Double
	    +tipo_Jabon: String
	    +Dispensar-jabón()
    }
    class Pago_efectivo {
	    +billetes_Recibidos: List
	    +validar_Billetes()
    }
    class Pago_electronico {
	    +tarjeta: string
	    +procesar-transferencia()
    }
    class Autolavado {
	    + Nombre_empresa: string
	    +Propietario: string
	    +Ubicacion: string
	    +realizarPago(cliente: Cliente, monto: Double)
	    +IniciarLavado(vehiculo: Vehiculo)
    }
    class Vehiculo {
	    +placa: string
	    +tipo_de_vehiculo: string
	    +ingresar_Autolavado()
    }
    class Automovil_2["Automovil"] {
	    +#placa: string
    }
    class Camioneta {
	    +#placa: string
    }
    class Camioneta_3["Camioneta"] {
	    +#placa: string
    }
    class Servicios_adicionales {
	    +Lavado_Motor: lavado_motor
	    +Pulido: pulido
	    +Encerado: encerado
	    +seleccionar_servicio()
	    +ejecutar_servicio()
    }

    Autolavado "0" -- "1" Cliente
    Autolavado -- "2" Sistema_pago
    Cliente "1" -- Vehiculo
    Estacion_Lavado "5" --* "15" Sensor
    Estacion_Lavado "4" --* "10" Rodillo
    Estacion_Lavado "2" --* "6" Dispensador_agua
    Estacion_Lavado "2" --* "4" Dispensar_jabon
    Sistema_pago --|> Pago_efectivo
    Sistema_pago --|> Pago_electronico
    Autolavado --* "1" Estacion_Lavado
    Vehiculo --|> Automovil_2
    Vehiculo --|> Camioneta
    Vehiculo --|> Camioneta_3
    Autolavado "1" --* "3" Servicios_adicionales

	class Autolavado:::Aqua
	class Autolavado:::Pine
	class Autolavado:::Peach
	class Autolavado:::Ash

	classDef Aqua :, stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
	classDef Pine :, stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
	classDef Peach :, stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
	classDef Ash :,stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
