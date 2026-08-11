# Hospital Management System

patient_ids = []

patient_records = {}

class InvalidPatientInfo(Exception):
    pass

class Patient:
    def __init__(self, patient_id, name, age):
        if not patient_id or not name or age <= 0:
            raise InvalidPatientInfo("Invalid Patient Information!")

        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}")

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")

def add_patient():
    try:
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))

        patient = Patient(patient_id, name, age)

        patient_ids.append(patient_id)

        patient_records[patient_id] = {
            "Name": patient.name,
            "Age": patient.age
        }

        print("Patient added successfully!")

    except ValueError:
        print("Age must be a number!")

    except InvalidPatientInfo as e:
        print("Error:", e)

def schedule_appointment():
    patient_id = input("Enter Patient ID: ")

    if patient_id not in patient_records:
        print("Patient not found!")
        return

    doctor_name = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD/MM/YYYY): ")

    appointment = (
        f"Patient ID: {patient_id}, "
        f"Patient Name: {patient_records[patient_id]['Name']}, "
        f"Doctor: {doctor_name}, Date: {date}\n"
    )

    with open("appointments.txt", "a") as file:
        file.write(appointment)

    print("Appointment scheduled successfully!")

def save_records():
    with open("patients.txt", "w") as file:
        for pid, details in patient_records.items():
            file.write(
                f"{pid},{details['Name']},{details['Age']}\n"
            )

    print("Records saved successfully!")

def display_patients():
    if not patient_records:
        print("No patient records found!")
        return

    print("\nPatient Records:")
    for pid, details in patient_records.items():
        print(
            f"ID: {pid}, Name: {details['Name']}, Age: {details['Age']}"
        )

while True:
    print("\n----Hospital Management System ----")
    print("1. Add Patient")
    print("2. Schedule Appointment")
    print("3. Display Patients")
    print("4. Save Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        display_patients()

    elif choice == "4":
        save_records()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
