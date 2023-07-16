class coche:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas
        
    def agregar_puerta(self):
        self.num_puertas +=1
        
    def main():
        micoche = coche(num_puertas=4)

        micoche.agregar_puerta(2)

        print("El munero de puertas del coche es de ", micoche.num_puertas)

    
    main()