require(["esri/config",
    "esri/Map",
    "esri/views/MapView",
    /*'esri/Graphic',
    'esri/layers/GraphicsLayer',*/
    'esri/layers/FeatureLayer',
    'esri/WebMap',
    'esri/widgets/Legend',
    "esri/widgets/Bookmarks",
    "esri/widgets/Expand",
    "esri/widgets/TimeSlider"
], function (esriConfig, Map, MapView, FeatureLayer, WebMap, Legend, Bookmarks, Expand, TimeSlider) {

    esriConfig.apiKey = 'AAPKdd1e5fb46d0947a382567461358b9a6dRuT09zSFDKSYeLnqZks-JZEi0EsBsx8dyKCdLGaA5X1OHHxhRfHyzeffQG373y_u';

    const map1 = new WebMap({
        portalItem: {
            id: "febedf0b3c0b45b39aeadeb8ea375b82"
        }
    });

    const view1 = new MapView({
        container: "viewDiv", //div element
        map: map1,
        zoom: 3, //zoom level
        center: [-95.050671, 49.921828] // longitude, latitude

    });

    let legend = new Legend({
        view: view1,
        map: map1
    });

    view1.ui.add(new Expand({ view1, content: legend }), "top-left");

    // Specify the widget while adding to the view's UI
    const bookmarks = new Bookmarks({
        view: view1,
        // allows bookmarks to be added, edited, or deleted
        editingEnabled: true,
        visibleElements: {
            time: false // don't show the time (h:m:s) next to the date
        }
    });

    const bkExpand = new Expand({
        view: view1,
        content: bookmarks
    });

    view1.ui.add(bkExpand, "top-right");

    // get timeslider settings from the webmap & create timeslider, add it to the view UI
    TimeSlider.getPropertiesFromWebMap(map1).then(
        (timeSliderSettings) => {
            const timeSliderDiv = document.createElement("div");
            timeSliderDiv.id = "timeSliderDiv";

            const timeSlider = new TimeSlider({
                ...timeSliderSettings, // imported settings from webmap
                view: view1,
                container: timeSliderDiv
            });
            view1.ui.add(timeSlider, "bottom-left");
        }
    );

    view1.when(function () {
        const layer = map1.layers.getItemAt(0);
        bookmarks.on("bookmark-select", (event) => {
            let hurricaneName = event.bookmark.name.toUpperCase();
            layer.featureEffect = {
                filter: {
                    where: "Name = '" + hurricaneName + "'"
                },
                excludedEffect: "grayscale(100%) opacity(30%)"
            };
        });
    });
});

