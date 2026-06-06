import boto3

dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('Employee')  

table.put_item(
    Item={
        'emp_id': 1,
        'name': 'Bhakti Jadhav',
        'age': 21,
        'salary':50000
    }
)

table.put_item(
    Item={
        'emp_id': 2,
        'name': 'Shreyash Jadhav',
        'age': 26,
        'salary':70000
    }
)

table.put_item(
    Item={
        'emp_id': 3,
        'name': 'Priya Sharma',
        'age': 25,
        'salary':60000
    }
)

table.put_item(
    Item={
        'emp_id': 4,
        'name': 'Radhika Saha',
        'age': 29,
        'salary':50000
    }
)

print("Item inserted successfully!")