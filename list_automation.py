from faker import Faker
import pandas as pd
from datetime import datetime
import random

def generate_hourly_worker_leads(num_contacts=1000):
    fake = Faker()
    job_categories = ['Restaurant', 'Retail', 'Hospitality', 'Warehouse', 'Healthcare']
    availability = ['Morning', 'Evening', 'Night', 'Weekends', 'Flexible']
    
    contacts = []
    for i in range(num_contacts):
        contact = {
            'id': fake.uuid4(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'phone': fake.phone_number(),
            'preferred_job': random.choice(job_categories),
            'availability': random.choice(availability),
            'location': fake.city(),
            'experience_years': random.randint(0, 5),
            'last_contact': fake.date_between(start_date='-30d', end_date='today'),
            'text_opt_in': random.choice([True, False]),
            'application_status': random.choice(['New', 'Contacted', 'Interview', 'Hired'])
        }
        contacts.append(contact)
        
        # Add print statement to see progress
        if i % 100 == 0:
            print(f"Generated {i} contacts...")
    
    df = pd.DataFrame(contacts)
    
    # Save to CSV
    csv_filename = 'workstream_contacts.csv'
    df.to_csv(csv_filename, index=False)
    print(f"\nGenerated {num_contacts} contacts and saved to {csv_filename}")
    
    # Display first few records
    print("\nFirst few records:")
    print(df.head())

if __name__ == "__main__":
    generate_hourly_worker_leads()
