# Workstream Lead Management System

A HubSpot integration solution for managing job applicant data, demonstrating marketing automation capabilities for high-volume hourly worker recruitment.

## Features

- 🔄 **HubSpot CRM Integration**: Automated contact syncing with custom properties for recruitment
- 📊 **Custom Fields Implementation**: 
  - Preferred Job
  - Availability
  - Experience Years
  - Application Status
- 📱 **Contact Management**: Handles 1000+ contact records with recruitment-specific data
- 🔍 **Lead Tracking**: Monitors application status and candidate progression

## Technical Implementation

- **HubSpot API Integration** using Python
- **Custom Property Creation** for recruitment-specific fields
- **Batch Contact Processing** with error handling
- **Data Validation** and cleaning procedures

## Project Structure

```bash
├── data_analysis.py          # Data analysis utilities
├── list_automation.py        # List automation functions
├── hubspot_sync.py          # HubSpot integration script
├── workstream_contacts.csv   # Mock contact data
└── .env                     # Environment configuration
