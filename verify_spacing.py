"""
Verify that the hexagonal grid has correct 50-meter spacing between points
"""
import json
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    Returns distance in meters
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in meters
    r = 6371000
    
    return c * r

def verify_spacing():
    """Verify spacing between sample points"""
    with open('/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa/points.json', 'r') as f:
        points = json.load(f)
    
    print(f"Total points: {len(points)}")
    print("\nVerifying spacing for first few points...")
    
    # Check horizontal spacing in first row
    if len(points) >= 2:
        dist = haversine_distance(
            points[0]['lat'], points[0]['lon'],
            points[1]['lat'], points[1]['lon']
        )
        print(f"Horizontal spacing (point 0 to 1): {dist:.2f} meters")
    
    # Find first point in second row (will have offset)
    # Second row should start after we've gone through first row
    first_row_lat = points[0]['lat']
    second_row_idx = next(i for i, p in enumerate(points) if p['lat'] != first_row_lat)
    
    # Check vertical spacing between rows
    if second_row_idx < len(points):
        dist = haversine_distance(
            points[0]['lat'], points[0]['lon'],
            points[second_row_idx]['lat'], points[second_row_idx]['lon']
        )
        print(f"Diagonal spacing (row 1 to row 2): {dist:.2f} meters")
        
        # Expected diagonal distance in hexagonal grid
        expected = 150.0  # Should be ~150m for hexagonal pattern
        print(f"Expected spacing: {expected:.2f} meters")
        print(f"Difference: {abs(dist - expected):.2f} meters")
    
    # Check row offset (second row should be offset by dx/2)
    first_row_count = sum(1 for p in points if p['lat'] == first_row_lat)
    print(f"\nFirst row has {first_row_count} points")
    
    # Sample diagonal verification
    print("\nSample distance calculations:")
    for i in range(min(5, len(points)-1)):
        dist = haversine_distance(
            points[i]['lat'], points[i]['lon'],
            points[i+1]['lat'], points[i+1]['lon']
        )
        print(f"  Point {i} to {i+1}: {dist:.2f} meters")

if __name__ == '__main__':
    verify_spacing()

