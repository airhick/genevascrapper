"""
Generate a hexagonal grid of points covering Geneva city, Switzerland
Points are equidistant at 150 meters from each other
Only includes points within Geneva city boundaries (approximate)
"""
import json
import math

# Geneva city approximate polygon boundary (following actual city shape)
# This approximates Geneva's shape along the lake and city borders
GENEVA_CITY_POLYGON = [
    (46.1950, 6.1350),  # Northwest
    (46.1980, 6.1300),  # North
    (46.2050, 6.1350),  # Northeast  
    (46.2100, 6.1400),  # North-central
    (46.2150, 6.1450),  # Northeast lake
    (46.2150, 6.1550),  # East along lake
    (46.2100, 6.1600),  # Southeast
    (46.2050, 6.1580),  # South
    (46.2000, 6.1520),  # Southwest
    (46.1950, 6.1480),  # West-central
    (46.1950, 6.1400),  # West
    (46.1950, 6.1350),  # Close polygon
]

# Bounding box for initial grid generation
GENEVA_BOUNDS = {
    'min_lat': 46.195,
    'max_lat': 46.215,
    'min_lon': 6.130,
    'max_lon': 6.160
}

# Spacing between points in meters
SPACING = 150

def point_in_polygon(lat, lon, polygon):
    """
    Check if a point is inside a polygon using ray casting algorithm
    """
    x, y = lon, lat
    n = len(polygon)
    inside = False
    
    p1_lat, p1_lon = polygon[0]
    for i in range(n + 1):
        p2_lat, p2_lon = polygon[i % n]
        if y > min(p1_lat, p2_lat):
            if y <= max(p1_lat, p2_lat):
                if x <= max(p1_lon, p2_lon):
                    if p1_lat != p2_lat:
                        xinters = (y - p1_lat) * (p2_lon - p1_lon) / (p2_lat - p1_lat) + p1_lon
                    if p1_lon == p2_lon or x <= xinters:
                        inside = not inside
        p1_lat, p1_lon = p2_lat, p2_lon
    
    return inside

def meters_to_degrees_lat(meters):
    """Convert meters to degrees latitude (approximately 111,320 meters per degree)"""
    return meters / 111320.0

def meters_to_degrees_lon(meters, latitude):
    """Convert meters to degrees longitude (varies by latitude)"""
    return meters / (111320.0 * math.cos(math.radians(latitude)))

def generate_hexagonal_grid():
    """
    Generate hexagonal grid points covering Geneva city
    In a hexagonal grid, each point has 6 neighbors at equal distance
    Only includes points within the city polygon boundary
    """
    points = []
    points_filtered = []
    
    # Calculate center latitude for longitude conversion
    center_lat = (GENEVA_BOUNDS['min_lat'] + GENEVA_BOUNDS['max_lat']) / 2
    
    # Convert spacing to degrees
    dy = meters_to_degrees_lat(SPACING)
    # For hexagonal grid, vertical spacing between rows is SPACING * sqrt(3)/2
    dy_hex = meters_to_degrees_lat(SPACING * math.sqrt(3) / 2)
    dx = meters_to_degrees_lon(SPACING, center_lat)
    
    # Calculate bounds in terms of grid coordinates
    min_lat = GENEVA_BOUNDS['min_lat']
    max_lat = GENEVA_BOUNDS['max_lat']
    min_lon = GENEVA_BOUNDS['min_lon']
    max_lon = GENEVA_BOUNDS['max_lon']
    
    # Generate grid
    row = 0
    current_lat = min_lat
    
    while current_lat <= max_lat:
        # Alternate rows are offset by dx/2 for hexagonal pattern
        offset = (dx / 2) if row % 2 == 1 else 0
        current_lon = min_lon + offset
        
        while current_lon <= max_lon:
            # Only add point if it's within the Geneva city polygon
            if point_in_polygon(current_lat, current_lon, GENEVA_CITY_POLYGON):
                points_filtered.append({
                    'lat': current_lat,
                    'lon': current_lon
                })
            current_lon += dx
        
        current_lat += dy_hex
        row += 1
    
    print(f"Generated {len(points_filtered)} points within Geneva city boundaries")
    return points_filtered

def save_points_to_json(points, filename='points.json'):
    """Save points to JSON file"""
    with open(filename, 'w') as f:
        json.dump(points, f, indent=2)
    print(f"Saved {len(points)} points following Geneva city boundaries to {filename}")

if __name__ == '__main__':
    points = generate_hexagonal_grid()
    save_points_to_json(points, '/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa/points.json')

