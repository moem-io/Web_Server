    var dataset = {
        nodes: [
            {name: "0_Hub", radius: "10", rgb: "#5f5f5f"},
            {name: "1_Node1", radius: "6", rgb: "#DD855C"},
            {name: "1_Node2", radius: "6", rgb: "#DD855C"},
            {name: "2_Node3", radius: "6", rgb: "#2793E8"},
            {name: "2_Node4", radius: "6", rgb: "#2793E8"},
            {name: "3_Node5", radius: "6", rgb: "#559900"},
            {name: "3_Node6", radius: "6", rgb: "#559900"}
        ],
        links: [
            {source: 0, target: 1, length: 10},
            {source: 0, target: 2, length: 10},
            {source: 1, target: 3, length: 50},
            {source: 2, target: 4, length: 50},
            {source: 3, target: 5, length: 100},
            {source: 4, target: 6, length: 100}
        ]
    };


    //Width and height
    var w = 800;
    var h = 800;

    var colors = d3.scale.category10();


    //Initial default force
    var force = d3.layout.force()
        .nodes(dataset.nodes)
        .links(dataset.links)
        .size([w, h])
        .linkDistance(function (links) {
            return links.length;
        })
        .charge([-1000])
        .start();

    //Create SVG element
    var svg = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

    //Create edges as lines
    var links = svg.selectAll("line")
        .data(dataset.links)
        .enter()
        .append("line")
        .style("stroke", "#ccc")
        .style("stroke-width", 1);

    // Create the groups under svg
    var gnodes = svg.selectAll('g.gnode')
        .data(dataset.nodes)
        .enter()
        .append('g')
        .classed('gnode', true);

    // Add one circle in each group
    var node = gnodes.append("circle")
        .attr("class", "node")
        .attr("r", function (d) {
            return d.radius
        })
        .style("fill", function (d) {
            return d.rgb;
        })
        .call(force.drag);

    // Append the labels to each group
    var labels = gnodes.append("text")
        .text(function (d) {
            return d.name;
        });


    force.on("tick", function () {
        links.attr("x1", function (d) {
            return d.source.x;
        })
            .attr("y1", function (d) {
                return d.source.y;
            })
            .attr("x2", function (d) {
                return d.target.x;
            })
            .attr("y2", function (d) {
                return d.target.y;
            });

        gnodes.attr("transform", function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        });
    });