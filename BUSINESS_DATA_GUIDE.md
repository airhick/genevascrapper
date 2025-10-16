# 🏢 Business Data Integration Guide

## Overview

The Geneva Hexagonal Grid now includes **business data integration**, allowing you to export a CSV file containing:
- Grid point coordinates
- Companies/businesses at each point
- Contact information (phone, website)
- Business details (name, type, address)

---

## 🚀 Quick Start

### Option 1: Free (No API Key) - OpenStreetMap Data

1. Open: `http://localhost:8000/index_with_businesses.html`
2. **Leave API key field empty**
3. Click "🔍 Fetch Business Data"
4. Wait for progress bar to complete
5. Click "📥 Download CSV with Businesses"

**Pros:**
- ✅ Free, no API key needed
- ✅ No rate limits
- ✅ Open data from OpenStreetMap

**Cons:**
- ⚠️ May have less data than Google
- ⚠️ Contact info might be limited

### Option 2: Google Places API (More Data)

1. Get Google API key (see below)
2. Open: `http://localhost:8000/index_with_businesses.html`
3. Enter API key
4. Click "🔍 Fetch Business Data"
5. Download CSV

**Pros:**
- ✅ Comprehensive business data
- ✅ Better contact information
- ✅ Ratings and more details

**Cons:**
- ⚠️ Requires API key setup
- ⚠️ May have usage costs

---

## 🔑 Getting a Google Places API Key

### Step-by-Step:

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/

2. **Create a Project**
   - Click "Select a project" → "New Project"
   - Name it (e.g., "Geneva Grid Business Data")
   - Click "Create"

3. **Enable APIs**
   - Go to "APIs & Services" → "Library"
   - Search and enable:
     - ✅ **Places API**
     - ✅ **Geocoding API** (optional but helpful)

4. **Create API Key**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy your API key

5. **Secure Your Key (Important!)**
   - Click "Edit API key"
   - Under "API restrictions":
     - Select "Restrict key"
     - Enable only: Places API, Geocoding API
   - Under "Application restrictions":
     - Choose "HTTP referrers"
     - Add: `http://localhost:8000/*`
   - Save

6. **Enter Key in Application**
   - Paste key into "Google Places API Key" field
   - Click "Fetch Business Data"

### Free Tier:
- Google offers $200 free credit per month
- Places API: $17 per 1000 requests
- For 166 grid points = ~$2.80
- Well within free tier!

---

## 📊 CSV Output Format

### Columns:

| Column | Description | Example |
|--------|-------------|---------|
| `Grid_Point` | Point number in grid | 1, 2, 3... |
| `Grid_Latitude` | Grid point latitude | 46.195 |
| `Grid_Longitude` | Grid point longitude | 6.135 |
| `Business_Name` | Company/business name | "Café du Lac" |
| `Business_Type` | Type of business | "restaurant", "shop" |
| `Address` | Street address | "Rue du Rhône 15" |
| `Phone` | Phone number | "+41 22 123 4567" |
| `Website` | Website URL | "www.cafedu.lac.ch" |
| `Business_Lat` | Business location lat | 46.1952 |
| `Business_Lon` | Business location lon | 6.1353 |

### Sample CSV:
```csv
Grid_Point,Grid_Latitude,Grid_Longitude,Business_Name,Business_Type,Address,Phone,Website,Business_Lat,Business_Lon
1,46.195,6.135,"Café Geneva","cafe","Rue du Rhône 10","+41 22 123 4567","www.cafe-geneva.ch",46.1951,6.1352
1,46.195,6.135,"Boulangerie Suisse","bakery","Rue du Rhône 12","+41 22 234 5678","N/A",46.1952,6.1353
2,46.195,6.13649,"UBS Bank","bank","Place Cornavin 3","+41 22 345 6789","www.ubs.com",46.1951,6.1365
```

---

## 🔍 How It Works

### Search Process:

1. **For each grid point:**
   - Searches within 75-meter radius
   - Finds all businesses/POIs
   - Collects contact information

2. **Data Sources:**
   
   **OpenStreetMap (Free):**
   - Uses Overpass API
   - Searches for:
     - `shop` tags (stores, shops)
     - `amenity` tags (restaurants, cafes, banks)
     - `office` tags (companies, offices)
   - No API key required
   
   **Google Places:**
   - Official business directory
   - Comprehensive contact info
   - Verified phone numbers
   - Official websites
   - Requires API key

3. **Progress Tracking:**
   - Shows real-time progress bar
   - Displays current point being processed
   - Total businesses found counter

---

## 📈 Expected Results

### For 166 Grid Points (150m spacing):

**Typical Results:**
- **Downtown Geneva:** 500-800 businesses
- **Residential Areas:** 100-300 businesses
- **Mixed Areas:** 300-500 businesses

**Business Types Found:**
- 🍽️ Restaurants & Cafes
- 🏪 Retail Stores
- 🏦 Banks & Financial Services
- 🏢 Offices & Companies
- 🏥 Medical Services
- 🏨 Hotels & Accommodations
- 🎨 Cultural & Entertainment
- 🔧 Services & Repairs

---

## 💡 Use Cases

### 1. **Market Research**
```
Identify business concentration areas
Find underserved locations
Analyze competitor distribution
```

### 2. **Sales & Marketing**
```
Build contact lists for area
Plan sales routes
Identify potential clients
```

### 3. **Urban Planning**
```
Analyze business density
Study commercial patterns
Plan zoning changes
```

### 4. **Real Estate**
```
Assess area commercial value
Identify business clusters
Evaluate location quality
```

### 5. **Service Delivery**
```
Plan delivery routes
Optimize service areas
Identify coverage gaps
```

---

## 🛠️ Technical Details

### API Endpoints Used:

**OpenStreetMap Overpass API:**
```
https://overpass-api.de/api/interpreter
```

**Google Places Nearby Search:**
```
https://maps.googleapis.com/maps/api/place/nearbysearch/json
```

### Search Parameters:
- **Radius:** 75 meters per grid point
- **Delay:** 100ms between requests (rate limiting)
- **Categories:** All business types

### Performance:
- **166 points × 100ms delay = ~17 seconds**
- Plus API response time
- Total: ~30-60 seconds for full grid

---

## 🚨 Important Notes

### Rate Limiting:
- **OpenStreetMap:** No strict limits, but be respectful
- **Google Places:** 
  - Free tier: $200/month credit
  - Monitor usage in Google Cloud Console

### Data Privacy:
- All data is publicly available
- No personal/private information
- Business contact info is public domain

### CORS Issues:
- Google API has CORS restrictions
- Production use requires backend proxy
- Current implementation uses CORS proxy
- For production: Set up your own backend

### API Key Security:
- ⚠️ **Never share your API key publicly**
- ⚠️ **Restrict key to specific domains**
- ⚠️ **Enable only needed APIs**
- ⚠️ **Monitor usage regularly**

---

## 📋 Troubleshooting

### Problem: No businesses found
**Solutions:**
- Check internet connection
- Verify API key (if using Google)
- Try OpenStreetMap mode (no key)
- Check browser console for errors

### Problem: API key error
**Solutions:**
- Verify key is correct
- Check API is enabled (Places API)
- Check restrictions aren't blocking localhost
- Wait a few minutes after key creation

### Problem: Slow fetching
**Solutions:**
- Normal for many points
- Reduce grid size (use higher spacing)
- Be patient - shows progress bar
- Consider using saved results

### Problem: CORS errors
**Solutions:**
- Use OpenStreetMap mode (no CORS)
- Current proxy handles Google CORS
- For production: Use backend server

---

## 🔄 Workflow Examples

### Example 1: Quick Free Export
```
1. Open index_with_businesses.html
2. Leave API key blank
3. Click "Fetch Business Data" 
4. Wait 30 seconds
5. Download CSV
6. Open in Excel/Google Sheets
```

### Example 2: Google Places Export
```
1. Get Google API key (5 minutes)
2. Enter key in field
3. Fetch business data
4. Get comprehensive results
5. Download enriched CSV
```

### Example 3: Custom Analysis
```
1. Fetch business data
2. Download CSV
3. Import to GIS software (QGIS)
4. Analyze business distribution
5. Create heat maps
```

---

## 📊 Data Analysis Tips

### In Excel/Google Sheets:
1. **Filter by business type** to find specific industries
2. **Sort by grid point** to see clustering
3. **Count businesses per point** for density analysis
4. **Extract phone numbers** for contact lists

### In Python/R:
```python
import pandas as pd
df = pd.read_csv('geneva_grid_with_businesses.csv')

# Count businesses per grid point
business_density = df.groupby('Grid_Point').size()

# Find most common business types
top_types = df['Business_Type'].value_counts()

# Extract all phone numbers
phones = df[df['Phone'] != 'N/A']['Phone'].tolist()
```

### In GIS Software:
1. Import CSV with coordinates
2. Create point layer for businesses
3. Join with grid points
4. Create heat maps
5. Analyze spatial patterns

---

## 🎯 Best Practices

### Before Fetching:
- ✅ Test with small grid first
- ✅ Check API key works
- ✅ Estimate costs (if using Google)
- ✅ Plan data usage

### During Fetching:
- ⏳ Be patient - shows progress
- 📊 Monitor business count
- 🔄 Don't refresh page
- 💾 Keep browser tab open

### After Download:
- 💾 Save CSV backup
- 🔍 Validate data quality
- 📈 Analyze results
- 📝 Document findings

---

## 🚀 Next Steps

### Current Features:
✅ OpenStreetMap integration (free)  
✅ Google Places integration (API key)  
✅ Business name, type, address  
✅ Phone and website extraction  
✅ Progress tracking  
✅ CSV export  

### Possible Enhancements:
- 📸 Business photos
- ⭐ Ratings and reviews
- 🕐 Opening hours
- 💰 Price level
- 📍 Multiple search radii
- 🎯 Business category filtering
- 📊 Built-in analytics
- 🗺️ Visual business markers on map

---

## 📞 Support Resources

### API Documentation:
- **Google Places:** https://developers.google.com/maps/documentation/places/web-service
- **OpenStreetMap:** https://wiki.openstreetmap.org/wiki/Overpass_API
- **Overpass Turbo:** https://overpass-turbo.eu/ (test queries)

### Community:
- **Stack Overflow:** Search "Google Places API"
- **OSM Forum:** https://forum.openstreetmap.org/

---

## 📝 Summary

**🎉 You can now export a CSV with:**
- ✅ All grid points (lat/lon)
- ✅ Businesses at each point
- ✅ Company names
- ✅ Phone numbers
- ✅ Websites
- ✅ Addresses
- ✅ Business types

**Two Options:**
1. **Free:** Use OpenStreetMap (no API key)
2. **Premium:** Use Google Places (API key required)

**Access:** http://localhost:8000/index_with_businesses.html

---

**Last Updated:** October 16, 2025  
**Version:** 1.0 with Business Data Integration

