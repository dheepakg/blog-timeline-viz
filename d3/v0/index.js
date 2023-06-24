const svg = d3
  .select(".canvas")
  .append("svg")
  .attr("width", 600)
  .attr("height", 600);

const graph = svg.append("g").attr("width", 500).attr("height", 500);

graph
  .append("rect")
  .attr("x", 10)
  .attr("y", 10)
  .attr("width", 500)
  .attr("height", 500)
  .attr("fill", "#f7d2ad");

d3.json("details.json").then((data) => {
  const lines = graph.selectAll("line").data(data);
  lines
    .append("line")
    .attr("x1", 25)
    .attr("y1", 25)
    .attr("x2", 365)
    .attr("y2", 25)
    .attr("stroke-width", 3)
    .attr("stroke", "grey");
});
