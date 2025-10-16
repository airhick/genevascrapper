# Geneva Hexagonal Grid Mapping

A hexagonal grid mapping system for Geneva, Switzerland with points equidistant at 50 meters from each other.

## Overview

This project generates a hexagonal grid pattern covering the entire city of Geneva, where each point is exactly 50 meters away from its neighbors. The points are visualized on an interactive map with red dots.

## Features

- **Hexagonal Grid Pattern**: Points arranged in a true hexagonal pattern where each point has 6 neighbors at equal distance
- **50-meter Spacing**: Points are equidistant at 50 meters from each other
- **Coverage**: Complete coverage of Geneva (51,729 points)
- **Interactive Map**: Web-based visualization using Leaflet.js
- **Red Dot Markers**: Each grid point is displayed as a red dot on the map

## Files

- `generate_hexgrid.py`: Python script that generates the hexagonal grid points
- `points.json`: Generated JSON file containing all grid point coordinates
- `index.html`: Interactive web map displaying the grid points

## How It Works

### Hexagonal Grid Mathematics

In a hexagonal grid:
- Horizontal spacing between points: 50m
- Vertical spacing between rows: 50m × √3/2 ≈ 43.3m
- Alternate rows are offset by 25m horizontally (half the horizontal spacing)

This creates a pattern where each point has exactly 6 neighbors at 50m distance.

### Coordinate Conversion

The script converts meters to geographical coordinates:
- Latitude: ~111,320 meters per degree
- Longitude: Varies by latitude (111,320 × cos(latitude) meters per degree)

## Usage

### Generate Grid Points

```bash
python3 generate_hexgrid.py
```

This will create `points.json` with all grid coordinates.

### View the Map

**⚠️ Important**: Due to browser CORS restrictions, you need to serve the HTML via a web server.

**Option 1: Use the startup script (Recommended)**
```bash
./start_server.sh
```

**Option 2: Manual server start**
```bash
python3 -m http.server 8000
# Then open: http://localhost:8000/index.html
```

**Option 3: Direct file (may not work)**
- Open `index.html` directly - dots may not appear due to CORS restrictions

Once the map loads:
1. The map will automatically display all 51,729 points as red dots
2. Use mouse wheel to zoom, click and drag to pan
3. The hexagonal grid pattern will be clearly visible

## Technical Details

- **Total Points**: 51,729
- **Coverage Area**: Geneva bounds (lat: 46.150-46.250, lon: 6.080-6.210)
- **Grid Pattern**: Hexagonal offset coordinate system
- **Visualization**: Leaflet.js with OpenStreetMap tiles
- **Point Marker Size**: 6px diameter red circles

## Requirements

- Python 3.x (for grid generation)
- Modern web browser (for visualization)
- Internet connection (for map tiles)

## Browser Compatibility

The HTML visualization works in all modern browsers:
- Chrome/Edge
- Firefox
- Safari
- Opera

No additional dependencies or installations required for viewing the map.

# genevascrapper
