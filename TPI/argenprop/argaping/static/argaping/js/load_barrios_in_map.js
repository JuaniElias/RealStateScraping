function show_mapa(barriosDataJSON) {
    let barrioFeature;

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

    // Solo mostrar los barrios que se consiguieron datos
    const matchedBarriosLayer = L.layerGroup();
    loadGeoJSON().then(barriosRosarioGEOJSON => {
      // Do something with myData here, such as passing it to another function.
        barriosRosarioGEOJSON.features.forEach(function(feature) {
            const selectedBarriosNames = barriosDataJSON.map(function(barrio) {
              return barrio.barrio__nombre;
            });

          if (selectedBarriosNames.indexOf(feature.properties.name) !== -1) {
            barrioFeature = L.geoJSON(feature,{
            style: style,
            onEachFeature: onEachFeature
             }).on('click', function (e) {
                const barrio = barriosDataJSON.find(item => item.barrio__nombre === e.layer.feature.properties.name)
                const promedio = barrio.average
                const minimo = barrio.minimo
                const maximo = barrio.maximo
                e.layer.bindPopup("Precio promedio de alquiler: $" + promedio + "<br>Precio mas bajo: $" + minimo + "<br>Precio mas alto: $" + maximo).openPopup();
                });
            matchedBarriosLayer.addLayer(barrioFeature);
          }
        });
    }).catch(error => {
      // Handle any errors that occurred while loading the GeoJSON file.
      console.error(error);
    });

    // Add the matchedBarriosLayer to the map
    matchedBarriosLayer.addTo(map);

}
