# 🌦️ IoT Weather Monitoring System

<div align="center">

**A modern, real-time weather monitoring web application with stunning animations and intelligent day/night awareness**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-4.5+-black.svg)](https://socket.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Configuration](#configuration) • [Technical Details](#technical-details)

</div>

---

## 📖 Overview

IoT Weather Monitoring System is a sophisticated, production-ready web application that provides real-time weather data visualization for 89 Indian cities. Built with Flask and Socket.IO, it features a modern glassmorphism design, intelligent day/night detection, and breathtaking animated backgrounds that adapt to current weather conditions.

### ✨ Key Highlights

- **Real-time Updates**: Live weather data refreshed every 10 seconds
- **Intelligent Design**: Weather-aware backgrounds and day/night contextual icons
- **Stunning UI**: Glassmorphism design with 6-layer animated backgrounds
- **Fully Responsive**: Optimized for all devices with 8 breakpoints
- **IoT Integration**: Automatic data logging to ThingSpeak cloud platform
- **Production Ready**: Clean, optimized codebase with error handling

---

## 🎯 Features

### Core Functionality

- 🌍 **89 Indian Cities** - Comprehensive coverage of major cities across India including Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune, and more
- ⚡ **Ultra-fast Updates** - Real-time weather data refresh every 10 seconds using Socket.IO polling transport
- 🌡️ **Temperature Monitoring** - Precise temperature tracking in Celsius with large, readable display
- 💧 **Humidity Tracking** - Real-time relative humidity percentage monitoring
- 🌤️ **Weather Conditions** - Detailed weather status with descriptive text

### Smart Features

- 🌙 **Day/Night Detection** - Intelligent icon system that displays sun during daytime and moon during nighttime based on actual sunrise/sunset times
- 🎨 **Dynamic Weather Backgrounds** - 12+ unique gradient backgrounds that automatically change based on weather conditions:
  - Clear skies (day/night variations)
  - Cloudy weather (scattered/overcast)
  - Rainy conditions (drizzle/rain/heavy rain)
  - Snowy weather
  - Thunderstorms
  - Special conditions (mist, fog, haze)
- ✨ **Multi-layer Animations** - Six beautifully orchestrated animation layers:
  - Floating cloud decorations with drift effects
  - Sparkling particles with random delays
  - Rotating geometric shapes
  - Flowing wave patterns
  - Pulsing radial gradients
  - SVG cloud texture overlays

### User Experience

- 🕒 **Live Clock** - Real-time clock display updating every second
- 🎯 **Easy Navigation** - Intuitive city selector dropdown with alphabetically sorted cities
- 📱 **Fully Responsive** - 8 responsive breakpoints (1399px, 1199px, 1023px, 767px, 599px, 479px, 379px, landscape mode)
- 🎭 **Glassmorphism Design** - Modern frosted glass aesthetic with backdrop blur effects
- 💪 **Enhanced Readability** - Bold typography (800 weight) with dual text shadows for optimal visibility
- 🔄 **Auto-reconnect** - Handles connection loss gracefully with user-friendly error messages

### Technical Features

- 📊 **IoT Data Logging** - Automatic data transmission to ThingSpeak platform for analytics and historical tracking
- 🚀 **Non-blocking Architecture** - ThingSpeak logging runs in separate daemon thread to prevent UI blocking
- ⚠️ **Robust Error Handling** - API timeout protection (5s), graceful fallbacks, user-friendly error messages
- 🔒 **Secure Configuration** - Flask SECRET_KEY for session security
- 📡 **Stable Transport** - Polling-based Socket.IO connection for maximum reliability

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for API access)

### Step-by-Step Setup

1. **Clone or Download the Project**
   ```bash
   cd IOTminiProject
   ```

2. **Install Required Packages**
   ```bash
   pip install flask flask-socketio requests
   ```

3. **Verify Installation**
   ```bash
   python -c "import flask, flask_socketio, requests; print('All dependencies installed successfully!')"
   ```

---

## ⚙️ Configuration

### API Keys

The application uses two external APIs:

1. **OpenWeatherMap API** - For real-time weather data
   - Current Key: `8e89146f89e624257dd10eea9b70947b`
   - Get your own: [OpenWeatherMap API](https://openweathermap.org/api)

2. **ThingSpeak API** - For IoT data logging
   - Current Write Key: `F5KPFW2H7OWSSBWP`
   - Get your own: [ThingSpeak](https://thingspeak.com/)

### Updating API Keys

Open `weather_web.py` and update these variables:

```python
WEATHER_API_KEY = "your_openweathermap_api_key"
THINGSPEAK_API_KEY = "your_thingspeak_write_key"
```

### Server Configuration

Default settings in `weather_web.py`:
- **Port**: 5000
- **Host**: 0.0.0.0 (accessible from network)
- **Update Interval**: 10 seconds
- **API Timeout**: 5 seconds
- **Debug Mode**: Enabled (disable for production)

---

## 💻 Usage

### Starting the Server

1. **Navigate to Project Directory**
   ```bash
   cd IOTminiProject
   ```

2. **Run the Application**
   ```bash
   python weather_web.py
   ```

3. **Access the Web Interface**
   - Local: `http://localhost:5000`
   - Network: `http://your-ip-address:5000`

### Using the Application

1. **View Current Weather**: Upon loading, weather data for Lucknow (default city) is displayed
2. **Change City**: Select any city from the dropdown menu at the top
3. **Monitor Updates**: Weather data automatically refreshes every 10 seconds
4. **Observe Animations**: Watch the dynamic backgrounds change with weather conditions
5. **Check Time**: Live clock displays current time in the header

### Stopping the Server

Press `Ctrl + C` in the terminal to gracefully shutdown the server.

---

## 📁 Project Structure

```
IOTminiProject/
│
├── weather_web.py              # Flask backend server (157 lines, 6.8 KB)
│   ├── Flask app configuration
│   ├── Socket.IO setup (threading mode)
│   ├── Weather data fetching (OpenWeatherMap)
│   ├── ThingSpeak IoT integration
│   ├── WebSocket event handlers
│   └── Background update thread
│
├── templates/
│   └── index.html              # Frontend interface (1279 lines, 46 KB)
│       ├── HTML structure
│       ├── CSS styling (glassmorphism design)
│       ├── Responsive media queries (8 breakpoints)
│       ├── JavaScript weather logic
│       ├── Socket.IO client integration
│       └── Animation definitions (6 layers)
│
└── README.md                   # Project documentation (this file)
```

**Total Project Size**: ~55 KB (production-ready, no dead code)

---

## 🔧 Technical Details

### Architecture

```
┌─────────────┐         ┌──────────────┐         ┌─────────────────┐
│   Browser   │◄────────┤ Flask Server │────────►│ OpenWeatherMap  │
│  (Socket.IO)│  Polling│  (threading) │   API   │      API        │
└─────────────┘         └──────────────┘         └─────────────────┘
                               │
                               │ Daemon Thread
                               ▼
                        ┌──────────────┐
                        │  ThingSpeak  │
                        │   Platform   │
                        └──────────────┘
```

### Technology Stack

**Backend**:
- **Flask 2.0+** - Lightweight WSGI web framework
- **Flask-SocketIO 4.5.4** - WebSocket integration with fallback to polling
- **Requests** - HTTP library for API calls
- **Threading** - Asynchronous data logging

**Frontend**:
- **HTML5** - Semantic markup structure
- **CSS3** - Advanced styling with animations, transitions, gradients
- **JavaScript (ES6+)** - DOM manipulation, Socket.IO client
- **Socket.IO Client 4.5.4** - Real-time bidirectional communication

**APIs & Services**:
- **OpenWeatherMap API v2.5** - Current weather data
- **ThingSpeak REST API** - IoT data logging platform

### Key Components

**Backend (`weather_web.py`)**:
- `update_weather()` - Background thread that fetches weather data every 10 seconds
- `send_to_thingspeak()` - Non-blocking IoT data transmission (3s timeout)
- `handle_connect()` - Emits current weather data when client connects
- `handle_city_change()` - Broadcasts city changes to all connected clients

**Frontend (`index.html`)**:
- `getWeatherIcon()` - Returns contextual emoji based on weather ID and day/night
- `updateBackground()` - Changes background gradient based on weather conditions
- `changeCity()` - Emits city change event to server
- `updateClock()` - Updates time display every second

### Performance Optimizations

- ✅ Non-blocking ThingSpeak requests (separate daemon thread)
- ✅ Efficient 10-second update intervals (50% faster than previous 15s)
- ✅ API timeout protection (5s for weather, 3s for IoT)
- ✅ Polling transport for stable connections
- ✅ Minimal DOM updates (only changed elements)
- ✅ CSS transform animations (GPU-accelerated)

### Responsive Breakpoints

| Breakpoint | Screen Width | Target Device         | Temperature Size |
|------------|-------------|-----------------------|------------------|
| Desktop XL | 1400px+     | Large monitors        | 120px            |
| Desktop L  | 1200-1399px | Standard monitors     | 100px            |
| Desktop M  | 1024-1199px | Small monitors        | 90px             |
| Tablet L   | 768-1023px  | Tablets (landscape)   | 80px             |
| Tablet P   | 600-767px   | Tablets (portrait)    | 70px             |
| Mobile L   | 480-599px   | Large phones          | 64px             |
| Mobile M   | 380-479px   | Standard phones       | 58px             |
| Mobile S   | <380px      | Small phones          | 52px             |

---

## 🎨 Weather Conditions Supported

The application intelligently handles **12+ weather categories**:

| Weather ID | Condition        | Day Icon | Night Icon | Background Color |
|------------|------------------|----------|------------|------------------|
| 800        | Clear Sky        | ☀️       | 🌙         | Blue/Dark Blue   |
| 801-802    | Few/Scattered    | 🌤️       | ☁️         | Light Blue/Gray  |
| 803-804    | Overcast         | ☁️       | ☁️         | Gray             |
| 300-321    | Drizzle          | 🌦️       | 🌧️         | Blue-Gray        |
| 500-504    | Rain             | 🌧️       | 🌧️         | Dark Gray        |
| 511        | Freezing Rain    | 🌨️       | 🌨️         | Steel Blue       |
| 520-531    | Heavy Rain       | ⛈️       | ⛈️         | Dark Blue-Gray   |
| 600-622    | Snow             | ❄️       | ❄️         | White-Blue       |
| 200-232    | Thunderstorm     | ⛈️       | ⛈️         | Dark Purple      |
| 701        | Mist             | 🌫️       | 🌫️         | Light Gray       |
| 711        | Smoke            | 🌫️       | 🌫️         | Gray-Brown       |
| 721        | Haze             | 🌫️       | 🌫️         | Yellow-Gray      |
| 731        | Dust             | 🌫️       | 🌫️         | Brown-Gray       |
| 741        | Fog              | 🌫️       | 🌫️         | Gray             |
| 751        | Sand             | 🌫️       | 🌫️         | Tan-Gray         |
| 761        | Dust             | 🌫️       | 🌫️         | Brown            |
| 762        | Volcanic Ash     | 🌫️       | 🌫️         | Dark Gray        |
| 771        | Squalls          | 💨       | 💨         | Gray             |
| 781        | Tornado          | 🌪️       | 🌪️         | Dark Gray        |

---

## 🌍 Supported Cities

**89 Indian Cities** including:

Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad, Surat, Jaipur, Lucknow, Kanpur, Nagpur, Indore, Thane, Bhopal, Visakhapatnam, Pimpri-Chinchwad, Patna, Vadodara, Ghaziabad, Ludhiana, Agra, Nashik, Faridabad, Meerut, Rajkot, Kalyan-Dombivli, Vasai-Virar, Varanasi, Srinagar, Aurangabad, Dhanbad, Amritsar, Navi Mumbai, Allahabad, Ranchi, Howrah, Coimbatore, Jabalpur, Gwalior, Vijayawada, Jodhpur, Madurai, Raipur, Kota, Chandigarh, Guwahati, Solapur, Hubballi-Dharwad, Tiruchirappalli, Bareilly, Mysore, Tiruppur, Gurgaon, Aligarh, Jalandhar, Bhubaneswar, Salem, Warangal, Guntur, Bhiwandi, Saharanpur, Gorakhpur, Bikaner, Amravati, Noida, Jamshedpur, Bhilai, Cuttack, Firozabad, Kochi, Nellore, Bhavnagar, Dehradun, Durgapur, Asansol, Rourkela, Nanded, Kolhapur, Ajmer, Akola, Gulbarga, Jamnagar, Ujjain, Loni, Siliguri, Jhansi, Ulhasnagar, Jammu, Sangli-Miraj & Kupwad, Mangalore, Erode, Belgaum, Ambattur, Tirunelveli, Malegaon, Gaya, Jalgaon, Udaipur, Maheshtala, Udupi (default)

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Server won't start / Port already in use
```bash
# Solution: Kill existing Python processes
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
```

**Issue**: Weather data not updating
- Check internet connection
- Verify OpenWeatherMap API key is valid
- Check if API rate limit exceeded (free tier: 60 calls/minute)

**Issue**: CSS/JavaScript changes not appearing
- Perform hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
- Clear browser cache
- Try incognito/private browsing mode

**Issue**: WebSocket connection errors (ERR_CONNECTION_REFUSED)
- Server automatically falls back to polling transport
- Ensure Flask-SocketIO is installed: `pip install flask-socketio`
- Check firewall/antivirus settings

**Issue**: ThingSpeak data not logging
- Verify ThingSpeak API key is correct
- Ensure ThingSpeak channel exists and is configured
- Check ThingSpeak rate limits (free tier: 1 update per 15 seconds)

---

## 🔐 Security Considerations

- ⚠️ **Debug Mode**: Set `debug=False` in production deployment
- 🔑 **Secret Key**: Change Flask `SECRET_KEY` for production use
- 🛡️ **API Keys**: Store keys in environment variables for production
- 🔒 **HTTPS**: Use reverse proxy (nginx/Apache) with SSL certificate for production
- 🌐 **CORS**: Configure proper CORS policies for cross-origin requests

---

## 🚀 Deployment

### For Production Deployment:

1. **Disable Debug Mode** in `weather_web.py`:
   ```python
   socketio.run(app, host='0.0.0.0', port=5000, debug=False)
   ```

2. **Use Production Server** (gunicorn):
   ```bash
   pip install gunicorn eventlet
   gunicorn --worker-class eventlet -w 1 weather_web:app --bind 0.0.0.0:5000
   ```

3. **Set Environment Variables**:
   ```bash
   export WEATHER_API_KEY="your_key"
   export THINGSPEAK_API_KEY="your_key"
   export SECRET_KEY="random_secure_string"
   ```

4. **Configure Reverse Proxy** (nginx example):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
       }
   }
   ```

---

## 📊 Browser Compatibility

| Browser         | Version | Support |
|-----------------|---------|---------|
| Chrome          | 90+     | ✅ Full  |
| Firefox         | 88+     | ✅ Full  |
| Safari          | 14+     | ✅ Full  |
| Edge            | 90+     | ✅ Full  |
| Opera           | 76+     | ✅ Full  |
| Mobile Safari   | iOS 14+ | ✅ Full  |
| Chrome Android  | 90+     | ✅ Full  |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenWeatherMap** - For providing comprehensive weather API
- **ThingSpeak** - For IoT data logging platform
- **Socket.IO** - For real-time bidirectional communication
- **Flask** - For the excellent Python web framework
- **Font Awesome** - For weather icon inspiration

---

## 📧 Contact

For questions, suggestions, or issues, please open an issue on the repository.

---

<div align="center">

**Made with ❤️ for IoT and Real-time Applications**

⭐ Star this repository if you find it helpful!

</div>
