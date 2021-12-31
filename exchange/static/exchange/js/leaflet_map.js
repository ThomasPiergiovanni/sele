
// Function allowing to get value from attribute name 'data-json' home.html
// 'data json' is alimented by django context['mapbox_url'] dict value
function loadJson(tag) {
    return JSON.parse(document.querySelector(tag).getAttribute('data-json'));
}

// Function allowing to get value context['mapbox_url']['url']
function getUrl(data) {
    return data.url;
}

var jsonData = loadJson('#map');
var t_url = getUrl(jsonData);

var map = L.map('map').setView([48.85, 2.35], 12);

var tiles = L.tileLayer(t_url, {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

