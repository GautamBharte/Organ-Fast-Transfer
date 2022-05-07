var cy = cytoscape({
  container: document.getElementById('cy'),
  elements: [
//node and positions for
{ data: { id: 'Apollo_Hospital'},position: {x: 1100,y: 200}},
{ data: { id: 'Siddhi_Vinayak_Hospital'},position: {x: 800,y: 500}},
{ data: { id: 'Apex_Hospital'},position:{x: 500,y: 400}},
{ data: { id: 'Six_Sigma_Hospital'},position: {x: 100,y: 700}},
{ data: { id: 'Wockhard_Hospital'},position: {x: 1100,y: 1000}},
{ data: { id: 'Fortune_Hospital'},position: {x: 1300,y: 1100}},
{ data: { id: 'Lilavti_Hospital'},position: {x: 1400,y: 400}},
{ data: { id: 'Ashoka_Medicover_Hospital'},position: {x: 1200,y: 1200}},
{ data: { id: 'Supreme_Kidney_Hospital'},position: {x: 600,y: 600}},
{ data: { id: 'Lotus_Hospital'},position: {x: 500,y: 900}},

//edge
{data: {id: 'one', source: 'Apollo_Hospital', target: 'Lilavti_Hospital', "weight": 5.4}}, 
{data: {id: 'two', source: 'Apollo_Hospital', target: 'Siddhi_Vinayak_Hospital', "weight": 5.1}},
{data: {id: 'three', source: 'Siddhi_Vinayak_Hospital', target: 'Apollo_Hospital', "weight": 5.1}},
{data: {id: 'four', source: 'Siddhi_Vinayak_Hospital', target: 'Lilavti_Hospital', "weight": 2.6}},
{data: {id: 'five', source: 'Siddhi_Vinayak_Hospital', target: 'Apex_Hospital', "weight": 6.8}},
{data: {id: 'six', source: 'Siddhi_Vinayak_Hospital', target: 'Supreme_Kidney_Hospital', "weight": 1.9}},
{data: {id: 'seven', source: 'Siddhi_Vinayak_Hospital', target: 'Wockhard_Hospital', "weight": 3.3}},
{data: {id: 'eight', source: 'Apex_Hospital', target: 'Siddhi_Vinayak_Hospital', "weight": 6.8}}, 
{data: {id: 'nine', source: 'Apex_Hospital', target: 'Supreme_Kidney_Hospital', "weight": 2.2}},
{data: {id: 'ten', source: 'Apex_Hospital', target: 'Six_Sigma_Hospital', "weight": 3.1}},
{data: {id: 'eleven', source: 'Six_Sigma_Hospital', target: 'Apex_Hospital', "weight": 3.1}},
{data: {id: 'twelve', source: 'Six_Sigma_Hospital', target: 'Lotus_Hospital', "weight": 2.7}},
{data: {id: 'thirteen', source: 'Wockhard_Hospital', target: 'Siddhi_Vinayak_Hospital', "weight": 3.1}},
{data: {id: 'fourteen', source: 'Wockhard_Hospital', target: 'Supreme_Kidney_Hospital', "weight": 5}},
{data: {id: 'fifteen', source: 'Wockhard_Hospital', target: 'Lotus_Hospital', "weight": 2.9}},
{data: {id: 'sixteen', source: 'Wockhard_Hospital', target: 'Ashoka_Medicover_Hospital', "weight": 3.4}},
{data: {id: 'seventeen', source: 'Wockhard_Hospital', target: 'Fortune_Hospital', "weight": 1.9}},
{data: {id: 'eighteen', source: 'Wockhard_Hospital', target: 'Lilavti_Hospital', "weight": 3.5}},
{data: {id: 'nineteen', source: 'Fortune_Hospital', target: 'Ashoka_Medicover_Hospital', "weight": 1.1}},
{data: {id: 'twenty', source: 'Fortune_Hospital', target: 'Wockhard_Hospital', "weight": 1.9}},
{data: {id: 'twenty_one', source: 'Fortune_Hospital', target: 'Lilavti_Hospital', "weight": 9.2}},
{data: {id: 'twenty_two', source: 'Lilavti_Hospital', target: 'Apollo_Hospital', "weight": 5.4}},
{data: {id: 'twenty_three', source: 'Lilavti_Hospital', target: 'Siddhi_Vinayak_Hospital', "weight": 2.6}},
{data: {id: 'twenty_four', source: 'Lilavti_Hospital', target: 'Wockhard_Hospital', "weight": 3.5}},
{data: {id: 'twenty_five', source: 'Lilavti_Hospital', target: 'Fortune_Hospital', "weight": 9.2}},
{data: {id: 'twenty_six', source: 'Ashoka_Medicover_Hospital', target: 'Wockhard_Hospital', "weight": 3.4}},
{data: {id: 'twenty_seven', source: 'Ashoka_Medicover_Hospital', target: 'Fortune_Hospital', "weight": 1.1}},
{data: {id: 'twenty_eight', source: 'Supreme_Kidney_Hospital', target: 'Siddhi_Vinayak_Hospital', "weight": 1.9}},
{data: {id: 'twenty_nine', source: 'Supreme_Kidney_Hospital', target: 'Apex_Hospital', "weight": 2.2}},
{data: {id: 'thirty', source: 'Supreme_Kidney_Hospital', target: 'Lotus_Hospital', "weight": 2.3}},
{data: {id: 'thirty_one', source: 'Supreme_Kidney_Hospital', target: 'Wockhard_Hospital', "weight": 5}},
{data: {id: 'thirty_two', source: 'Lotus_Hospital', target: 'Six_Sigma_Hospital', "weight": 2.7}},
{data: {id: 'thirty_three', source: 'Lotus_Hospital', target: 'Supreme_Kidney_Hospital', "weight": 2.3}},
{data: {id: 'thirty_four', source: 'Lotus_Hospital', target: 'Wockhard_Hospital', "weight": 2.9}},


     




],




    layout:{
      name:"preset"
    },
    style:[
        {
            selector:"node",
            style: {
                "shape":"pentagon",
                height:"50px",
                width:"50px",
                "background-color":"blue",
                label:"data(id)"
            }
        },
        {
            selector: "edge",
            style: {
                "curve-style": "straight",
                 "width":"10",
                
                "line-color":"yellow",
                "line-opacity":"0.2",
                
            }
        },
        {
            selector: ".highlighted",
            style: {
                "background-color":"green",
                "line-color":"red",
                "line-opacity":"0.8",
            }
        },
    ]

});
cy.once("tap", "node", function (evt) {
    var sum=0.0;
    start = evt.target.id()
    console.log("source hospital has been set")
    cy.once("tap", "node", function (evt) {
    end = evt.target.id()
    console.log("destination hospital has been set")
    var dijkstra = cy.elements().dijkstra("#"+start, function (edge) {
        return edge.data("weight")
    }, false)
    //sum=sum+edge.data("weight");
    var total_length = cy.elements().dijkstra("#"+start, function (edge) {
        console.log( sum=sum+edge.data("weight"))
    }, false)
    // console.log(total_length);
    var bfs = dijkstra.pathTo(cy.$("#"+end))
    console.log(bfs);
    var x = 0
    let distToJ = dijkstra.distanceTo( cy.$('#'+end) );
    console.log(distToJ);
    var highlight = function () {
        var el = bfs[x]
        console.log(el);
        el.addClass("highlighted")
        if (x < bfs.length) {
            x++
            setTimeout(highlight, 500)
        }
    }
    highlight()


})


})


cy.once("tap", "node", function (evt) {
    start = evt.target.id()
    console.log("source hospital has been set")
    cy.once("tap", "node", function (evt) {
    end = evt.target.id()
    console.log("destination hospital has been set")
    var dijkstra = cy.elements().dijkstra("#"+start, function (edge) {
        return edge.data("weight")
    }, false)
    var bfs = dijkstra.pathTo(cy.$("#"+end))
    var x = 0
    var highlight = function () {
        var el = bfs[x]
        var sum
        el.addClass("highlighted")
        if (x < bfs.length) {
            x++
            setTimeout(highlight, 500)
        }
    }
    highlight()


})


})





