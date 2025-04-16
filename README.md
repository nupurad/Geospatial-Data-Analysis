This project explores spatial data processing, querying, and visualization using multiple GIS technologies. The objective was to simulate real-world spatial workflows by collecting, storing, querying, and rendering geospatial points related to the USC campus.

1. Spatial Data Collection

13 locations from around the University of Southern California campus were selected and their coordinates were noted for further analysis.

2. KML file creation

    a) Using a local IDE like VSCode, a KML file (Keyhole Markup Language) was created by adding the 13 locations as placemarks. Verified locations using Google Earth. 
    b) Calculated the four nearest locations from the USC campus to a personal location (23rd Street Cafe).
    c) Computed and visualized a 'convex hull', which is a convex polygon that encloses all 13 locations.
Code and screenshot of results provided.

3. OpenLayers Visualization

Leveraged OpenLayers (a JavaScript API) to view the 13 locations in a browser. Modified sample JavaScript code store points in 'localStorage' which were then retrieved for visualization, using OL markers.
Code and screenshot of results provided.

4. Spirograph Curve 

    a) Computed a Spirograph curve with the 'Tommy Trojan' statue at USC as the center, using the equations:
            x(t) = (R+r) * cos((r/R)*t) - a * cos((1+r/R)*t)
            y(t) = (R+r) * sin((r/R)*t) - a * sin((1+r/R)*t)
       with: R = 36, r = 9, a = 30.
    
    b) Generated a .kml file using the spirograph curve, and visualized using Google Earth.

    c) Converted the KML file into a 'shapefile'. Uploaded and visualized the shapefile using ArcGIS Online.
Code and screenshot of results provided.

