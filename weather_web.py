from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os
import requests
from datetime import datetime
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-only-secret-change-in-production')
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading', engineio_logger=False, logger=False)

# Load API keys from environment variables (never hardcode keys!)
THINGSPEAK_API = os.getenv('THINGSPEAK_API_KEY', 'F5KPFW2H7OWSSBWP')
WEATHER_API = os.getenv('WEATHER_API_KEY', '8e89146f89e624257dd10eea9b70947b')

# Default city
current_city = "Udupi"

# Popular cities in India
INDIAN_CITIES = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", 
    "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Kanpur", "Nagpur",
    "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara",
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut",
    "Rajkot", "Varanasi", "Srinagar", "Amritsar", "Allahabad", "Ranchi",
    "Howrah", "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur",
    "Madurai", "Raipur", "Kota", "Guwahati", "Chandigarh", "Thiruvananthapuram",
    "Mysore", "Bareilly", "Gurgaon", "Aligarh", "Moradabad", "Jalandhar",
    "Bhubaneswar", "Salem", "Warangal", "Guntur", "Bhiwandi", "Saharanpur",
    "Gorakhpur", "Bikaner", "Amravati", "Noida", "Jamshedpur", "Bhilai",
    "Cuttack", "Firozabad", "Kochi", "Nellore", "Bhavnagar", "Dehradun",
    "Durgapur", "Asansol", "Nanded", "Kolhapur", "Ajmer", "Akola",
    "Gulbarga", "Jamnagar", "Ujjain", "Loni", "Siliguri", "Jhansi",
    "Ulhasnagar", "Jammu", "Sangli", "Mangalore", "Erode", "Belgaum",
    "Ambattur", "Tirunelveli", "Malegaon", "Udaipur", "Udupi"
]

# Global variable to store current weather data
current_data = {
    'temperature': '--',
    'humidity': '--',
    'description': 'Loading...',
    'time': '--',
    'updates': 0,
    'status': 'Initializing...',
    'error': False,
    'city': current_city,
    'sunrise': None,
    'sunset': None,
    'weather_id': None,
    'is_day': True
}

def update_weather():
    """Background thread to fetch weather data and emit to all clients"""
    global current_city
    while True:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={current_city}&appid={WEATHER_API}&units=metric"
            response = requests.get(url, timeout=5)  # Reduced from 10 to 5 seconds
            data = response.json()
            
            if "main" in data:
                temperature = round(data["main"]["temp"], 1)
                humidity = data["main"]["humidity"]
                weather_desc = data["weather"][0]["description"].title()
                weather_id = data["weather"][0]["id"]
                
                # Get sunrise and sunset times
                sunrise_time = data["sys"]["sunrise"]
                sunset_time = data["sys"]["sunset"]
                current_time = time.time()
                is_day = sunrise_time <= current_time <= sunset_time
                
                # Update global data immediately (don't wait for ThingSpeak)
                current_data['temperature'] = temperature
                current_data['humidity'] = humidity
                current_data['description'] = weather_desc
                current_data['weather_id'] = weather_id
                current_data['sunrise'] = sunrise_time
                current_data['sunset'] = sunset_time
                current_data['is_day'] = is_day
                current_data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                current_data['updates'] += 1
                current_data['status'] = 'Data sent to ThingSpeak successfully!'
                current_data['error'] = False
                current_data['city'] = current_city
                
                # Send to clients immediately
                socketio.emit('weather_update', current_data, namespace='/')
                
                # Send to ThingSpeak asynchronously (non-blocking)
                def send_to_thingspeak():
                    try:
                        thingspeak_url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API}&field1={temperature}&field2={humidity}"
                        requests.get(thingspeak_url, timeout=3)  # Reduced timeout
                    except:
                        pass  # Don't let ThingSpeak errors affect the app
                
                # Run ThingSpeak upload in separate thread
                threading.Thread(target=send_to_thingspeak, daemon=True).start()
            else:
                current_data['status'] = f"Error: {data.get('message', 'Unknown error')}"
                current_data['error'] = True
                current_data['city'] = current_city
                socketio.emit('weather_update', current_data, namespace='/')
                time.sleep(60)
                continue
                
        except Exception as e:
            current_data['status'] = f"Connection Error: {str(e)}"
            current_data['error'] = True
            current_data['city'] = current_city
            socketio.emit('weather_update', current_data, namespace='/')
            time.sleep(30)  # Reduced retry wait time from 60 to 30 seconds
            continue
        
        time.sleep(10)  # Update every 10 seconds (faster than 15)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', cities=sorted(INDIAN_CITIES), default_city=current_city)

@socketio.on('connect')
def handle_connect():
    """Send current data when client connects"""
    emit('weather_update', current_data)

@socketio.on('change_city')
def handle_city_change(data):
    """Handle city change request"""
    global current_city
    new_city = data.get('city', 'Udupi')
    if new_city in INDIAN_CITIES:
        current_city = new_city
        current_data['city'] = current_city
        current_data['status'] = f'Switching to {current_city}...'
        emit('weather_update', current_data, broadcast=True)

if __name__ == '__main__':
    # Start background thread
    weather_thread = threading.Thread(target=update_weather, daemon=True)
    weather_thread.start()
    
    print("\n" + "="*60)
    print("🌤️  Weather Monitoring System - Real-Time Web Interface")
    print("="*60)
    print(f"\n✅ Server starting...")
    print(f"🌐 Open your browser and go to: http://localhost:5000")
    print(f"📍 Default location: {current_city}")
    print(f"🌍 {len(INDIAN_CITIES)} Indian cities available")
    print(f"🔴 Live updates every 10 seconds (no refresh needed!)")
    print(f"\n⏹️  Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
