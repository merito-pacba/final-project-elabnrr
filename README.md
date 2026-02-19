Azure Cloud-Native Smart Meal Planner
A web-based application built with Flask and Azure SQL Database that allows users to plan their weekly meals and automatically generate a consolidated shopping list. This project was developed as a final requirement for the Programming and Architecture of Cloud-Based Applications course.

1. Features
Dynamic Meal Selection: Fetches meal names, calories, and categories directly from an Azure SQL Database.
Automated Shopping List: Intelligently sums ingredients and quantities across multiple selected meals.
Cloud-Native Design: Fully compliant with Azure App Service deployment and environment variable configuration.
Responsive UI: A modern, mobile-friendly interface styled with custom CSS.

2. Tech Stack
Backend: Python / Flask
Database: Azure SQL (Relational DB)
Frontend: HTML5, CSS3, Jinja2 Templates
Deployment: Azure App Service (Linux)

3. Hard Requirements Met
The following project requirements have been implemented:
Framework: Written in Flask.
Hosting: Configured to work in Azure App Service.
Data Storage: Uses an Azure SQL Database to read meal data.
Security: No database configurations are hardcoded; all credentials are provided via environment variables.

4. Environment Variables 
To run this application, you must set the following environment variables (locally in a .env file or in the Azure Portal):
DB_SERVER Your Azure SQL Server
DB_NAME The name of your database (e.g., smp)
DB_USER Your database admin username
DB_PASSWORD Your database admin password

5. Deployment to Azure
This application is configured for deployment to Azure App Service.
Ensure the Networking settings of your Azure SQL Server allow access from "Azure services and resources" to enable communication between the web app and the database.
