# Troubleshooting Guide

## Issue: Red dots are not visible on the map

### Problem
When opening `index.html` directly (by double-clicking or drag-and-drop to browser), the red dots don't appear on the map.

### Cause
This is due to **CORS (Cross-Origin Resource Sharing)** security restrictions. Modern browsers block JavaScript `fetch()` requests to local files when the HTML is opened with the `file://` protocol.

### Solution

#### ✅ Solution 1: Use the startup script (Easiest)
```bash
cd "/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa"
./start_server.sh
```

This will:
- Start a local web server on port 8000
- Automatically open the map in your browser
- Display all 51,729 red dots

#### ✅ Solution 2: Manual web server
```bash
cd "/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa"
python3 -m http.server 8000
```

Then open your browser to: **http://localhost:8000/index.html**

#### ✅ Solution 3: Alternative Python server
```bash
cd "/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa"
python -m SimpleHTTPServer 8000  # Python 2
# OR
python3 -m http.server 8000      # Python 3
```

Then open: **http://localhost:8000/index.html**

### How to verify it's working

1. **Check the info panel**: The "Total Points" should show `51729` (not "Loading..." or "Error")
2. **Check the browser console**: 
   - Press F12 or Cmd+Option+I (Mac)
   - Look for messages like:
     ```
     Fetching points.json...
     Response received: 200
     Successfully loaded 51729 points
     Adding points to map...
     Added 51729 markers to map
     Map bounds fitted
     ```

3. **Visual check**: You should see red dots covering Geneva in a hexagonal pattern

### Common Issues

#### Port 8000 already in use
```bash
# Use a different port
python3 -m http.server 8001
# Then open: http://localhost:8001/index.html
```

#### Dots are too small
The dots are intentionally small (8px) to show the dense grid pattern. Zoom in to see them more clearly:
- Each dot is 8 pixels in diameter
- They have a white border and shadow for visibility
- Bright red color (#ff0000) for maximum contrast

#### Server won't start
Make sure Python 3 is installed:
```bash
python3 --version
```

If not installed, install Python from: https://www.python.org/downloads/

### Still Having Issues?

Check these:

1. **Is the server running?**
   ```bash
   # Check if server is running
   ps aux | grep "http.server"
   ```

2. **Is points.json present?**
   ```bash
   ls -lh points.json
   # Should show: -rw-r--r--  3.4M  points.json
   ```

3. **Regenerate the grid**
   ```bash
   python3 generate_hexgrid.py
   ```

4. **Browser console errors?**
   - Open browser DevTools (F12)
   - Check Console tab for errors
   - Check Network tab to see if points.json loads (should be 200 OK)

### Expected Behavior

✅ Map loads centered on Geneva  
✅ Info panel shows "51729" points  
✅ Red dots visible across Geneva area  
✅ Hexagonal pattern visible when zoomed in  
✅ Console shows "Added 51729 markers to map"  

### Contact / Debug Info

If dots still don't appear:
1. Open browser console (F12)
2. Take a screenshot of any errors
3. Check that you're accessing via `http://localhost:8000/` not `file://`

