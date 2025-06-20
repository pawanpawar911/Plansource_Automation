from faker import Faker

class FakeData:
    fake = Faker()
    
    firstName = fake.first_name()
    lastName = fake.last_name()
    
    name_with_middle = fake.name()
    middleName = name_with_middle.split()[1]

    ssn = fake.ssn()
    
    fake_add = fake.address()
    address = fake_add.split('\n')[0]
    
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()    
    country = fake.country()
    email = fake.email()   
    
    sp_firstName = fake.first_name()
    sp_lastName = fake.last_name()
    
    name_with_middle = fake.name()
    sp_middleName = name_with_middle.split()[1]
    
    sp_ssn = fake.ssn()
    
    gender = fake.random_element(elements=('Female'))
    
    relationship = fake.random_element(elements=('Spouse', 'Child', 'Student', 'Disabled Dependent', 'Domestic Partner', 'Child of Domestic Partner'))
    