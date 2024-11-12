# IMG2PDF Project

This project, IMG2PDF, is a Django web application that converts images to PDFs. It uses Celery for background task management and Redis as a message broker to handle asynchronous PDF generation, ensuring smooth and efficient processing.

Attribution

>I originally followed a guide on Medium for this project and adapted it for my own learning and development.
>The project was successfully set up, and I made the necessary adjustments to get it running smoothly.
>Special thanks to the author of the guide for providing a solid foundation for this application.

Tech Stack

    Backend: Django, Celery, FPDF
    Message Broker: Redis
    Database: Default Django DB (SQLite or any configured DB)
    Frontend: Basic HTML, CSS (can add JavaScript for better UX)

Features

1. Image Upload: Users can upload images to be converted.
2. Asynchronous Processing: Conversion to PDF happens in the background using Celery.
3. Real-time Progress Tracking: The user is notified when PDF generation is in progress.
4. Downloadable Output: Users can download the generated PDF.

Installation

1.Clone the Repository

    git clone https://github.com/abynxv/IMG2PDF.git
    cd IMG2PDF

2.Create a Virtual Environment

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Required Packages

    pip install -r requirements.txt

4.Run Migrations

    python manage.py migrate

💡 Start Redis Server
    
    redis-server
🚀 Start Celery Worker

    celery -A image_to_pdf_project worker --loglevel=info
🌐 Run Django Server

    python3 manage.py runserver

![Screenshot from 2024-11-11 17-17-41](https://github.com/user-attachments/assets/cc449532-83dc-43f5-aaaa-bdd585ffc129)
![Screenshot from 2024-11-11 17-17-52](https://github.com/user-attachments/assets/303b873d-e6bc-41bf-acb6-8c869d519b38)
![Screenshot from 2024-11-11 17-19-24](https://github.com/user-attachments/assets/304f55f8-96d0-4753-aee4-ef9a53d04fb5)


