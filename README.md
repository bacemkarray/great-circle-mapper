# ✈️ Great Circle Mapper (ICAO Edition)

This is a lightweight GUI tool for visualizing great circle flight paths between any number of global airports using their **ICAO codes**.

### 🔍 What it does
- Lets you input a series of ICAO airport codes (e.g., `CYYZ-KJFK-EGLL`).
- Fetches each airport's coordinates using the public [`airportsdata`](https://pypi.org/project/airportsdata/) library.
- Displays a **satellite map** with airport markers and great circle routes between consecutive airports using the **Google Maps Static API**.
- Built with **Tkinter** for the UI and **Pillow** for image rendering.

---

### 🧪 Example
Enter:
```
CYYZ-KJFK-EGLL
```
And the app will show:
- A red great circle path from CYYZ → KJFK → EGLL.
- Marker pins for each airport.

---

### 🚀 How to run

1. **Clone this repo**  
   Or download the `.py` files.

2. **Install dependencies** (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up a Google Maps API key**:
   - Follow this guide: https://developers.google.com/maps/documentation/maps-static/get-api-key
   - Paste your API key into the `mapRequest` function in `greatCircleMapper.py`:
     ```python
     api = "YOUR_API_KEY_HERE"
     ```

4. **Run the app**:
   ```bash
   python greatCircleMapper.py
   ```

---

### 📦 Dependencies
- `airportsdata` — Global airport metadata
- `requests` — For fetching the map image
- `pillow` — For displaying images in Tkinter
- `tkinter` — Built-in GUI framework

---

### 🧠 Notes
- Only ICAO codes (e.g., `KLAX`, not `LAX`) are supported.
- The final leg is drawn between the **last two airports** entered.
- You can enter as many airports as you like, separated by `-`.

---

### ⚖️ License
This project is educational and non-commercial. All map imagery is served via Google Maps under their [terms of service](https://mapsplatform.google.com/terms/).
