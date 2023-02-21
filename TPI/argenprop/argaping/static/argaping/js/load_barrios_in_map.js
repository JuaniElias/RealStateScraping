function show_mapa() {

    const map = L.map('map').setView([-32.935, -60.68], 13);
    const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    function loadGeoJSON() {
      return fetch('Barrios_de_Rosario.geojson')
        .then(response => response.json())
        .then(data => {
          return data;
        })
        .catch(error => {
          console.error('Error loading GeoJSON file:', error);
          throw error;
        });
    }


    const info = L.control();

    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    info.update = function (props) {
        this._div.innerHTML = (props ? '<h4>' + props.name + '</h4><br />' : '<h4>Pasa el mouse por arriba</h4>');
    };

    info.addTo(map);

    function style() {
        return {
            fillColor: '#ADA2FF',
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }

    function highlightFeature(e) {
        const layer = e.target;

        layer.setStyle({
            weight: 5,
            color: '#FFF8E1',
            dashArray: '',
            fillOpacity: 0.7
        });
        layer.bringToFront();
        info.update(layer.feature.properties);
    }

    function resetHighlight(e) {
        barrioFeature.resetStyle(e.target);
    }

    function onEachFeature(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight
        });
    }


    var checkbox = document.getElementById("cbxTipoOperacion");

    // Add an event listener to the checkbox
    checkbox.addEventListener('change', function()
    {
        if (this.checked) {
            // if the checkbox is checked, show venta on the map
            reload_data(data_venta_json)
        } else {
            // if the checkbox is not checked, show alquiler on the map
            reload_data(data_alquiler_json)
        }
    });

    let barrioFeature = undefined;
    function reload_data(data) {
        map.eachLayer(function(layer) {
        if( layer instanceof L.GeoJSON )
           map.removeLayer(layer);
        });
        const matchedBarriosLayer = L.layerGroup();

        loadGeoJSON().then(barriosRosarioGEOJSON => {
            // Solo buscar los barrios que se consiguieron datos
            barriosRosarioGEOJSON.features.forEach(function (feature) {
                const selectedBarriosNames = data.map(function (barrio) {
                    return barrio.barrio__nombre;
                });

                if (selectedBarriosNames.indexOf(feature.properties.name) !== -1) {
                    barrioFeature = L.geoJSON(feature, {
                        id: 'barrioFeature',
                        style: style,
                        onEachFeature: onEachFeature
                    }).on('click', function (e) {
                        const barrio = data.find(item => item.barrio__nombre === e.layer.feature.properties.name)
                        const promedio = barrio.average
                        const minimo = barrio.minimo
                        const maximo = barrio.maximo
                        const cantidad = barrio.cantidad
                        e.layer.bindPopup("AVG: $" + promedio + "<br>MIN: $" + minimo + "<br>MAX: $" + maximo + "<br>CANT: " + cantidad).openPopup();
                    });
                    matchedBarriosLayer.addLayer(barrioFeature).addTo(map);
                }
            });
        }).catch(error => {
            // Handle any errors that occurred while loading the GeoJSON file.
            console.error(error);
        });
    }
    //La primera vez se carga alquiler solo después se maneja con el checkbox
    reload_data(data_alquiler_json);
}
