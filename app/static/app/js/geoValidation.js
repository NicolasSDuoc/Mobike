const locations = [
    { lat: -33.441846, lng: -70.543656 },
    { lat: -33.443908, lng: -70.547427 },
    { lat: -33.441539, lng: -70.562217 },
    { lat: -33.446522, lng: -70.563894 },
    { lat: -33.452564, lng: -70.528735 },
    { lat: -33.427082, lng: -70.616987 },
    { lat: -33.430677, lng: -70.623567 },
    { lat: -33.438215, lng: -70.607535 },
    { lat: -33.435869, lng: -70.593358 },
    { lat: -33.462222, lng: -70.610673 },
    { lat: -33.456644, lng: -70.593217 },
    { lat: -33.465243, lng: -70.589107 },
    { lat: -33.453813, lng: -70.621725 },
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
                const info = "VER ESTACIONAMIENTOS";
                // establece el contenido de la ventana informativa
                ventanaInfo.setContent(info),
                    //abre la ventana informativa
                    ventanaInfo.open(map, marcador);
            }
        })(marcador, i));
    }
}