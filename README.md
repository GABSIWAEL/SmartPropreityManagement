Smart Property Management
Overview
Smart Property Management is a web-based application that allows users to control and monitor various aspects of their properties, such as houses, gardens, farms, and more. The project is built using Flask for the backend and HTML/CSS/JavaScript for the frontend. It is designed to run on a Raspberry Pi, enabling physical control over connected hardware components via GPIO pins.

Features
User authentication and session management
Control and monitor different property sections (e.g., house, garden, farm)
Toggle lights, activate/shutdown systems and cameras
Real-time interaction with hardware connected to Raspberry Pi GPIO pins
Prerequisites
Raspberry Pi with Raspbian OS
Python 3.x
Flask
RPi.GPIO library
Flask-SocketIO (optional, for real-time communication)
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/yourusername/smart-property-management.git
cd smart-property-management
Install dependencies:

bash
Copier le code
pip install Flask RPi.GPIO Flask-SocketIO
Set up your hardware:

Connect your hardware components (e.g., lights, cameras) to the Raspberry Pi GPIO pins.
Ensure proper and safe connections as per your hardware specifications.
Configuration
Update Flask secret key and valid credentials:

In app.py, update the secret_key and valid_credentials as per your requirements:


app.secret_key = 'your_secret_key'
valid_credentials = {'yourusername': 'yourpassword'}
Modify GPIO pin configurations:
In app.py, modify the GPIO pin configurations to match your hardware setup.

Running the Application
Start the Flask server:


python app.py
Access the application:
Open a web browser and navigate to http://<your_raspberry_pi_ip>:5000.

Project Structure
app.py: Flask application and route definitions
templates/: HTML templates for different pages
index.html: Main dashboard page
Other HTML files for different sections (farm, garden, etc.)
static/: Static files (CSS, JavaScript)
Usage
Login:

Navigate to the login page and enter valid credentials.
Navigate through the property sections:

Use the navigation bar to access different sections (house, garden, farm, etc.).
Control hardware components:

Use the buttons on each page to activate/shutdown systems and toggle lights.
View camera feeds and control cameras (if connected).
Example JavaScript Functions
Example functions in index.html to interact with hardware via GPIO pins:


<script>
    function activateSystem() {
        fetch('/activate_system').then(response => alert('System activated!'));
    }

    function shutdownSystem() {
        fetch('/shutdown_system').then(response => alert('System shut down!'));
    }

    function toggleLights() {
        fetch('/toggle_lights').then(response => alert('Lights toggled!'));
    }

    // Additional functions for specific rooms
    function activateSalon() {
        fetch('/activate_salon').then(response => alert('Salon activated!'));
    }

    function shutdownSalon() {
        fetch('/shutdown_salon').then(response => alert('Salon shut down!'));
    }
</script>
Contributing
Feel free to submit issues or pull requests for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Creator: Wael Gabsi
Special thanks to the Flask and Raspberry Pi communities for their support and resources
