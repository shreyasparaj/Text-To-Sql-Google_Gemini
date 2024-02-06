import sqlite3

# Connect to SQLite
connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()

# Create the PATIENT table with an additional PATIENT_ID column
table_info = """
CREATE TABLE PATIENT(
    PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25),
    ROOM VARCHAR(25),
    DISEASENAME VARCHAR(25),
    DATE_OF_ADMIT VARCHAR(10)
);
"""
cursor.execute(table_info)

# Manually insert 100 patient records with date in dd-mm-yyyy format
patient_data = [
    ('John Smith', '101', 'Flu', '01-01-2024'),
    ('Jane Doe', '102', 'Fracture', '02-01-2024'),
    ('Michael Johnson', '103', 'Appendicitis', '03-01-2024'),
    ('Emily Davis', '104', 'Pneumonia', '04-01-2024'),
    ('Christopher Wilson', '105', 'Migraine', '05-01-2024'),
    ('Amanda Taylor', '106', 'Sprained Ankle', '06-01-2024'),
    ('Robert Brown', '107', 'COVID-19', '07-01-2024'),
    ('Jennifer Miller', '108', 'Bronchitis', '08-01-2024'),
    ('Daniel Martinez', '109', 'Kidney Stones', '09-01-2024'),
    ('Sarah Jackson', '110', 'Concussion', '10-01-2024'),
    ('William White', '111', 'Diabetes', '11-01-2024'),
    ('Olivia Harris', '112', 'Hypertension', '12-01-2024'),
    ('Matthew Thompson', '113', 'Asthma', '13-01-2024'),
    ('Ella Garcia', '114', 'Gastritis', '14-01-2024'),
    ('David Hernandez', '115', 'Rheumatoid Arthritis', '15-01-2024'),
    ('Sophia Martinez', '116', 'Common Cold', '16-01-2024'),
    ('Joseph Johnson', '117', 'Ear Infection', '17-01-2024'),
    ('Lily Davis', '118', 'Stomach Flu', '18-01-2024'),
    ('Andrew Smith', '119', 'Allergies', '19-01-2024'),
    ('Grace Wilson', '120', 'UTI', '20-01-2024'),
    ('Carter Brown', '121', 'Influenza', '21-01-2024'),
    ('Chloe Taylor', '122', 'Gallstones', '22-01-2024'),
    ('Benjamin Miller', '123', 'Arthritis', '23-01-2024'),
    ('Zoe Davis', '124', 'Cystic Fibrosis', '24-01-2024'),
    ('Ethan Johnson', '125', 'Sinusitis', '25-01-2024'),
    ('Natalie Harris', '126', 'Hernia', '26-01-2024'),
    ('Jackson Thompson', '127', 'Meningitis', '27-01-2024'),
    ('Avery Garcia', '128', 'Ulcerative Colitis', '28-01-2024'),
    ('Logan Hernandez', '129', 'Eczema', '29-01-2024'),
    ('Emma Martinez', '130', 'Lung Cancer', '30-01-2024'),
    ('Mason Jackson', '131', 'Gout', '31-01-2024'),
    ('Ankit', '133', 'Aids', '01-02-2024'),
    ('Shreyas', '133', 'Thyroid Disorder', '02-02-2024'),
    ('Madison Brown', '134', 'Tuberculosis', '03-02-2024'),
    ('Liam Taylor', '135', 'Migraine', '04-02-2024'),
    ('Abigail White', '136', 'Rheumatoid Arthritis', '05-02-2024'),
    ('Elijah Davis', '137', 'Fracture', '06-02-2024'),
    ('Grace Garcia', '138', 'Common Cold', '07-02-2024'),
    ('James Smith', '139', 'Pneumonia', '08-02-2024'),
    ('Ava Harris', '140', 'Appendicitis', '09-02-2024'),
    ('Logan Hernandez', '141', 'Stomach Flu', '10-02-2024'),
    ('Sophia Taylor', '142', 'Diabetes', '11-02-2024'),
    ('Caleb Johnson', '143', 'Kidney Stones', '12-02-2024'),
    ('Isabella Thompson', '144', 'Concussion', '13-02-2024'),
    ('Lucas White', '145', 'Hypertension', '14-02-2024'),
    ('Avery Miller', '146', 'Gastritis', '15-02-2024'),
    ('Ella Jackson', '147', 'Asthma', '16-02-2024'),
    ('Jackson Brown', '148', 'Rheumatoid Arthritis', '17-02-2024'),
    ('Aria Taylor', '149', 'Common Cold', '18-02-2024'),
    ('Mia Garcia', '150', 'Ear Infection', '19-02-2024'),
    ('Liam Davis', '151', 'Stomach Flu', '20-02-2024'),
    ('Harper Martinez', '152', 'Pneumonia', '21-02-2024'),
    ('Oliver Smith', '153', 'Appendicitis', '22-02-2024'),
    ('Emma Wilson', '154', 'Allergies', '23-02-2024'),
    ('William Hernandez', '155', 'Gallstones', '24-02-2024'),
    ('Charlotte Thompson', '156', 'Influenza', '25-02-2024'),
    ('Liam Davis', '157', 'Hypertension', '26-02-2024'),
    ('Ava Taylor', '158', 'Sprained Ankle', '27-02-2024'),
    ('Oliver Brown', '159', 'Migraine', '28-02-2024'),
    ('Sophie Johnson', '160', 'Concussion', '29-02-2024'),
    ('Noah White', '161', 'Diabetes', '01-03-2024'),
    ('Chloe Garcia', '162', 'Pneumonia', '02-03-2024'),
    ('Ethan Taylor', '163', 'Bronchitis', '03-03-2024'),
    ('Aria Hernandez', '164', 'Kidney Stones', '04-03-2024'),
    ('Mia Smith', '165', 'Stomach Flu', '05-03-2024'),
    ('Liam Davis', '166', 'Common Cold', '06-03-2024'),
    ('Olivia Wilson', '167', 'Appendicitis', '07-03-2024'),
    ('Elijah Brown', '168', 'Influenza', '08-03-2024'),
    ('Avery Taylor', '169', 'Gastritis', '09-03-2024'),
    ('Logan Smith', '170', 'Ear Infection', '10-03-2024'),
    ('Emma Davis', '171', 'Rheumatoid Arthritis', '11-03-2024'),
    ('Jackson Garcia', '172', 'Allergies', '12-03-2024'),
    ('Ava Johnson', '173', 'Pneumonia', '13-03-2024'),
    ('Liam Thompson', '174', 'Fracture', '14-03-2024'),
    ('Sophia White', '175', 'Common Cold', '15-03-2024'),
    ('Noah Wilson', '176', 'Gallstones', '16-03-2024'),
    ('Mia Hernandez', '177', 'Kidney Stones', '17-03-2024'),
    ('Oliver Davis', '178', 'Appendicitis', '18-03-2024'),
    ('Isabella Taylor', '179', 'Influenza', '19-03-2024'),
    ('Lucas Smith', '180', 'Rheumatoid Arthritis', '20-03-2024'),
    ('Aria Garcia', '181', 'Gout', '21-03-2024'),
    ('Liam Brown', '182', 'Common Cold', '22-03-2024'),
    ('Avery Wilson', '183', 'Pneumonia', '23-03-2024'),
    ('Olivia Hernandez', '184', 'Gastritis', '24-03-2024'),
    ('Elijah Thompson', '185', 'Ear Infection', '25-03-2024'),
    ('Emma Taylor', '186', 'Allergies', '26-03-2024'),
    ('Jackson Davis', '187', 'Appendicitis', '27-03-2024'),
    ('Ava Smith', '188', 'Influenza', '28-03-2024'),
    ('Liam Garcia', '189', 'Stomach Flu', '29-03-2024'),
    ('Sophia White', '190', 'Rheumatoid Arthritis', '30-03-2024'),
    ('Noah Brown', '191', 'Common Cold', '31-03-2024'),
    ('Chloe Taylor', '192', 'Pneumonia', '01-04-2024'),
    ('Ethan Hernandez', '193', 'Appendicitis', '02-04-2024'),
    ('Aria Davis', '194', 'Gastritis', '03-04-2024'),
    ('Mia Thompson', '195', 'Kidney Stones', '04-04-2024'),
    ('Liam Smith', '196', 'Influenza', '05-04-2024'),
    ('Olivia Wilson', '197', 'Common Cold', '06-04-2024'),
    ('Elijah Garcia', '198', 'Pneumonia', '07-04-2024'),
    ('Avery Taylor', '199', 'Allergies', '08-04-2024'),
    ('Emma Hernandez', '200', 'Stomach Flu', '09-04-2024'),
]

# Insert the data into the PATIENT table
cursor.executemany('INSERT INTO PATIENT (NAME, ROOM, DISEASENAME, DATE_OF_ADMIT) VALUES (?, ?, ?, ?)', patient_data)

# Display all records with patient IDs
print("The inserted records are:")
data = cursor.execute('SELECT * FROM PATIENT')

for row in data:
    print(row)

# Close connection
connection.commit()
connection.close()
