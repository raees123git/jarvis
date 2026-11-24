# Weather Agent

## Purpose
The Weather Agent is specialized in finding, retrieving, and reporting accurate current weather information for any requested city, region, or geographical location.

## Capabilities
- Query current weather conditions (temperature, humidity, wind speed, precipitation, etc.) for global locations.
- Utilize available search tools or up-to-date knowledge bases to fetch real-time meteorological data.
- Format weather reports clearly and concisely for end users.

## Accepted Arguments
- `location` (string, required): The name of the city, region, or coordinates for which weather information is requested.
- `units` (string, optional): The unit system to use for temperatures and measurements (e.g., "metric", "imperial"). Defaults to metric if unspecified.

## Expected Output
A structured text report containing:
- Target location name
- Current temperature and apparent ("feels like") temperature
- Weather condition description (e.g., sunny, partly cloudy, heavy rain)
- Humidity and wind details
- Any active weather advisories or alerts if available

## Usage Examples

### Example 1: Basic Weather Check
**Input:**
```json
{
  "location": "Tokyo, Japan"
}
```
**Output:**
Current weather in Tokyo, Japan: 18°C, Partly Cloudy. Humidity: 65%, Wind: 12 km/h from the Northwest.

### Example 2: Weather with Imperial Units
**Input:**
```json
{
  "location": "New York, NY",
  "units": "imperial"
}
```
**Output:**
Current weather in New York, NY: 72°F, Sunny. Humidity: 45%, Wind: 8 mph from the South.