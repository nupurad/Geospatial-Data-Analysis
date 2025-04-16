#importing necessary libraries
import math

#specified parameters
R, r, a = 36, 9, 30
#Tommy Trojan coordinates as the center
lat_center = 34.02050086066646
lon_center = -118.28544721911078

#spirograph curve point creation
points = []
t = 0.0
while t <= 20 * math.pi:  
    x = (R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t)
    y = (R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t)
    
    lat = lat_center + (x / 10000)  
    lon = lon_center + (y / 10000)
    
    points.append((lon, lat))
    t += 0.01

#building the spiro.kml file
with open("spiro.kml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    f.write('  <Document>\n')
    f.write('    <Placemark>\n')
    f.write('      <name>Spirograph Curve</name>\n')
    f.write('      <Style>\n')
    f.write('        <LineStyle>\n')
    f.write('          <color>ff800080</color>\n')  
    f.write('          <width>2</width>\n')
    f.write('        </LineStyle>\n')
    f.write('      </Style>\n')
    f.write('      <LineString>\n')
    f.write('        <coordinates>\n')

    for lon, lat in points:
        f.write(f"          {lon},{lat},0\n")

    f.write('        </coordinates>\n')
    f.write('      </LineString>\n')
    f.write('    </Placemark>\n')
    f.write('  </Document>\n')
    f.write('</kml>\n')

print("spiro.kml generated successfully!")

