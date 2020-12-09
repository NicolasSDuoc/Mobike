const locations = [
    { lat: -33.441846, lng: -70.543656 },
    { lat: -33.443908, lng: -70.547427 },
];


function initMap() {
    const myLatLng = { lat: -33.4462428, lng: -70.5891139 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: myLatLng,
    });

    var marcador;
    var iconBase = "http://maps.google.com/mapfiles/kml/shapes/cycling.png";
    for (var i = 0; i < locations.length; i++) {
        marcador = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i].lat, locations[i].lng),
            map: map,
            title: "Estacionamiento Mobike",
            icon: iconBase,
        });

        //	instancia una nueva ventana informativa
        var ventanaInfo = new google.maps.InfoWindow();

        google.maps.event.addListener(marcador, 'click', (function(marcador, i) {
            return function() {
                const url = "{% url 'bicycle' %}"
                const info = "<a href='/bicycle/ " + i + "'" + "class='btn btn-primary'" + " >" + "Ver bicicletas" + "</a>";
                // establece el contenido de la ventana informativa
                ventanaInfo.setContent(info),
                    //abre la ventana informativa
                    ventanaInfo.open(map, marcador);
            }
        })(marcador, i));

    }
}