
// Function allowing to get value from attribute name 'data-json' home.html
// 'data json' is alimented by django context['mapbox_url'] dict value
function loadJson(tag, key_name) {
    return JSON.parse(document.querySelector(tag).getAttribute(key_name));
}

// Function allowing to get value context['mapbox_url']['url']
function getUrl(data) {
    return data.url;
}

var jsonData = loadJson('#map', 'data-json');
var t_url = getUrl(jsonData);
var geojsonFeature = loadJson('#map', 'data-geojson');

var map = L.map('map').setView([46.50, 2.21], 5);

function setStyle(feature) {
    switch (feature.properties.activity) {
        case 'yes': return {
            weight: 2,
            color: "#0275d8"
        };
        case 'no': return {
            opacity: 1,
            color: "#ff0000"
        };
    }
}

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'border rounded border-3 border-light bg-light'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h6 class="ml-1 mt-2 text-secondary"><b>Groupe local</b></h6>' + (props ?
        '<p class="ml-1 mr-1 text-dark"><b><span class="text-primary">' + props.name + '</span></b> (' + props.insee_code +').'+
        '<br><b><span class="text-primary">75 </span></b> membres.</p>'
        : '<p class="ml-1 mr-1 text-dark">Survolez une commune</p>');
};

info.addTo(map);

var geojson;

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.6
    });

    // if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    //     layer.bringToFront();
    
    info.update(layer.feature.properties);
}



function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature,
    });
    //does this feature have a property named nom?
    // if (feature.properties && feature.properties.nom) {
    //     layer.bindPopup(feature.properties.nom);
    //}
}



function setFilter(feature, layer) {
    return feature.properties.activity==='yes';
}

geojson = L.geoJSON(
    geojsonFeature, {
        filter: setFilter,
        style: setStyle,
        onEachFeature: onEachFeature
    }
).addTo(map);

// L.geoJSON(
//     geojsonFeature, {
//     style: function (feature) {
//         switch (feature.properties.activity) {
//             case 'yes': return {
//                 weight: 2,
//                 color: "#5cb85c"
//             };
//             case 'no': return {
//                 opacity: 0,
//                 color: "#ffffff"
//             };
//         }
//     },
//     onEachFeature: onEachFeature
// }
// ).addTo(map);



var tiles = L.tileLayer(t_url, {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);





