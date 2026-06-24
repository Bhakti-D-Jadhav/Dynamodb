
import boto3

# Connect once to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('Employee')
print("Table Status:", table.table_status)

# CREATE 
def create_employee():
    try:
        emp = {
            'emp_id': int(input("ID: ")),
            'name': input("Name: "),
            'age': int(input("Age: ")),
            'salary': int(input("Salary: "))
        }

        table.put_item(Item=emp)                # Adds the item to emp table
        print("Inserted")

    except ValueError:
        print("Error: ID, Age, Salary must be numbers")


#  READ 
def read_employee():
    try:
        emp_id = int(input("ID: "))

        response = table.get_item(Key={'emp_id': emp_id})
        item = response.get('Item')

        if item:
            print("Employee:", item)
        else:
            print("Not found")

    except ValueError:
        print("Error: ID must be a number")


# UPDATE 
def update_salary():
    try:
        emp_id = int(input("ID: "))
        salary = int(input("New Salary: "))

        table.update_item(
            Key={'emp_id': emp_id},
            UpdateExpression="SET salary = :s",
            ExpressionAttributeValues={':s': salary}
        )

        print("Updated")

    except ValueError:
        print("Error: ID and Salary must be numbers")


# DELETE 
def delete_employee():
    try:
        emp_id = int(input("ID: "))

        table.delete_item(Key={'emp_id': emp_id})
        print("Deleted")

    except ValueError:
        print("Error: ID must be a number")

# Read all
def read_all_employees():
    response = table.scan()
    items = response.get('Items', [])

    if items:
        for item in items:
            print(item)
    else:
        print("No employees found")

#  MENU 
while True:
    print("\n===== EMPLOYEE MENU =====")
    print("1. Create")
    print("2. Read")
    print("3. Update Salary")
    print("4. Delete")
    print("5. Read All")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_employee()

    elif choice == '2':
        read_employee()

    elif choice == '3':
        update_salary()

    elif choice == '4':
        delete_employee()

    elif choice == '5' :
        read_all_employees()

    elif choice == '6':
        print("Exited")
        break

    else:
        print("Error: Invalid choice, select 1-5")