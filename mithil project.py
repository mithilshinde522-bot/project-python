MAX_CARS = 5

cars = [
    {"id": 1, "name": "Maruti Swift", "type": "Hatchback",
     "rent": 1500.0, "available": True},
    {"id": 2, "name": "Hyundai Creta", "type": "SUV",
     "rent": 2500.0, "available": True},
    {"id": 3, "name": "Honda City", "type": "Sedan",
     "rent": 2200.0, "available": True},
    {"id": 4, "name": "Tata Nexon", "type": "SUV",
     "rent": 2000.0, "available": True},
    {"id": 5, "name": "Toyota Innova", "type": "MUV",
     "rent": 3000.0, "available": True}
]

rental = {}


def display_cars():
    print("\n========== AVAILABLE CARS ==========")
    print(f"{'ID':<5}{'Car Name':<22}{'Type':<15}{'Rent/Day'}")
    print("-" * 60)

    for car in cars:
        if car["available"]:
            print(
                f"{car['id']:<5}{car['name']:<22}"
                f"{car['type']:<15}Rs.{car['rent']:.2f}"
            )


def rent_car():
    print("\n========== RENT A CAR ==========")

    customer = input("Enter Customer Name: ")

    try:
        car_id = int(input("Enter Car ID: "))
    except ValueError:
        print("Invalid Car ID!")
        return

    for car in cars:
        if car["id"] == car_id:

            if not car["available"]:
                print("\nSorry! This car is already rented.")
                return

            try:
                days = int(input("Enter Number of Days: "))
            except ValueError:
                print("Please enter a valid number of days.")
                return

            if days <= 0:
                print("Number of days must be greater than zero.")
                return

            total = car["rent"] * days

            rental[car_id] = {
                "customer": customer,
                "days": days,
                "total": total
            }

            car["available"] = False

            print("\n========== RENTAL DETAILS ==========")
            print("Customer Name :", customer)
            print("Car           :", car["name"])
            print(f"Rent/Day      : Rs.{car['rent']:.2f}")
            print("Days          :", days)
            print(f"Total Amount  : Rs.{total:.2f}")
            print("\nCar rented successfully!")
            return

    print("\nInvalid Car ID!")


def return_car():
    print("\n========== RETURN CAR ==========")

    try:
        car_id = int(input("Enter Car ID: "))
    except ValueError:
        print("Invalid Car ID!")
        return

    for car in cars:
        if car["id"] == car_id:

            if car["available"]:
                print("\nThis car is already available.")
            else:
                car["available"] = True
                print("\nCar returned successfully!")

            return

    print("\nInvalid Car ID!")


def search_car():
    print("\n========== SEARCH CAR ==========")

    try:
        car_id = int(input("Enter Car ID: "))
    except ValueError:
        print("Invalid Car ID!")
        return

    for car in cars:
        if car["id"] == car_id:
            print("\nCar ID       :", car["id"])
            print("Car Name     :", car["name"])
            print("Car Type     :", car["type"])
            print(f"Rent/Day     : Rs.{car['rent']:.2f}")

            if car["available"]:
                print("Status       : Available")
            else:
                print("Status       : Rented")

            return

    print("\nCar not found!")


def main():
    while True:
        print("\n====================================")
        print("         CAR RENTAL SYSTEM")
        print("====================================")
        print("\n1. Display Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Search Car")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid choice!")
            continue

        if choice == 1:
            display_cars()

        elif choice == 2:
            rent_car()

        elif choice == 3:
            return_car()

        elif choice == 4:
            search_car()

        elif choice == 5:
            print("\nThank you for using Car Rental System!")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()
