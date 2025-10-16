# 🚀 Quick Start Guide

## View the Hexagonal Grid Map

### Simple 2-Step Process:

**Step 1:** Start the server
```bash
cd "/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa"
./start_server.sh
```

**Step 2:** The map will open automatically in your browser!

---

## Alternative: Manual Start

```bash
# 1. Navigate to project
cd "/Users/Eric.AELLEN/Documents/A - projets pro/TRASH/geneve hexa"

# 2. Start server
python3 -m http.server 8000

# 3. Open browser to:
http://localhost:8000/index.html
```

---

## What You Should See

✅ **Interactive map** centered on Geneva  
✅ **51,729 red dots** in a hexagonal pattern  
✅ **Info panel** showing point count  
✅ **50-meter spacing** between points (verified)

---

## Map Controls

- 🖱️ **Pan**: Click and drag
- 🔍 **Zoom**: Mouse wheel or +/- buttons  
- 📍 **Pattern**: Zoom in to see hexagonal grid clearly

---

## Currently Running

🟢 **Server Status**: Running on port 8000  
🌐 **URL**: http://localhost:8000/index.html  
📊 **Points**: 51,729 covering Geneva  
📏 **Spacing**: 50 meters (hexagonal)

---

## Need Help?

See `TROUBLESHOOTING.md` if:
- Dots don't appear
- Map doesn't load  
- Getting errors

---

## Stop the Server

Press `Ctrl+C` in the terminal where the server is running

