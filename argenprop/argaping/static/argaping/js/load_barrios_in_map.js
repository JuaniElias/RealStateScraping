function show_mapa() {

    const map = L.map('map').setView([-32.935, -60.67],13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        zoomSnap: 0.25,
        minZoom: 12,
        maxZoom: 15,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        className: 'map-tiles'
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

    info.onAdd = function () {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    info.update = function (props) {
        this._div.innerHTML = (props ? '<h3>' + props.name + '</h3>' : '<h3>Pasa el mouse por arriba</h3>');
    };

    info.addTo(map);

    function style() {
        return {
            fillColor: '#212529',
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


    let checkbox = document.getElementById("cbxTipoOperacion");
    let state = 'alquiler'

    // Add an event listener to the checkbox
    checkbox.addEventListener('change', function()
    {
        if (this.checked) {
            // if the checkbox is checked, show venta on the map
            state = 'venta'
            reload_data(data_venta_json)
        } else {
            // if the checkbox is not checked, show alquiler on the map
            state = 'alquiler'
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
                        let currency = "$"
                        if (state === 'venta'){
                            currency = "U$D"}
                        e.layer.bindPopup("<b>Precio promedio: </b>" + currency + promedio + "<br><b>Mínimo: </b>" + currency + minimo + "<br> <b>Máximo: </b>"+ currency + maximo + "<br><b>Propiedades encontradas: </b>" + cantidad).openPopup();
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
