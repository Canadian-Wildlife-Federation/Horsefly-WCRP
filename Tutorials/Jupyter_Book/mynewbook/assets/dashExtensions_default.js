window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, context) {
            return context.props.hideout.includes(feature.properties.name);
        },
        function1: function(feature, context) {
            return context.props.hideout.includes(feature.properties.name);
        },
        function2: function(feature, context) {
            return context.props.hideout.includes(feature.properties.name);
        },
        function3: function(feature, context) {
            return context.props.hideout.includes(feature.name);
        },
        function4: function(feature, context) {
            return context.props.hideout.includes(feature.name);
        },
        function5: function(feature, context) {
            return context.props.hideout.includes(feature.name);
        }
    }
});