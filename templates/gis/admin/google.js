{% extends "gis/admin/openlayers.js" %}
 
{% block base_layer %}new OpenLayers.Layer.Google("Google Base Layer", {
    'type': G_NORMAL_MAP, 
    'sphericalMercator': true
});
 
{% endblock %}
 

{% block controls %}
 
{{ block.super }}
 
if (!wkt) {
    var zoomLevel = 14;
  
    // Try W3C Geolocation method (Preferred)
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            {{ module }}.map.setCenter(new OpenLayers.LonLat(
                position.coords.longitude, position.coords.latitude
                ).transform(
                    new OpenLayers.Projection("EPSG:4326"),
                    new OpenLayers.Projection("EPSG:900913")
                ), zoomLevel);
        }, function() {
            // Location could not be found (probably denied by user)
        });
    } else if (google.gears) {
        // Try Google Gears Geolocation
        var geo = google.gears.factory.create('beta.geolocation');
 
        geo.getCurrentPosition(function(position) {
            {{ module }}.map.setCenter(new OpenLayers.LonLat(
                position.longitude, 
                position.latitude), zoomLevel);
        }, function() {
            // Location could not be found (probably denied by user)
        });
    } else {
        // Browser doesn't support Geolocation
    }
}
 
{% endblock %}
