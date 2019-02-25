var map = new ol.Map({
    target: 'map',
    view: new ol.View({
        center: ol.proj.fromLonLat([-1, -1, 1.8164837, 42.7883379]),
        zoom: 12
    })
});

var baseSource = new ol.source.TileWMS({
    url: 'http://localhost/geoserver/china/wms',
    params: {
        'LAYERS': 'china:chinamap',
        'TILED': true
    },
    serverType: 'geoserver'
});

var baseLayer = new ol.layer.Tile({
    source: baseSource
});

map.addLayer(baseLayer);