const svg = d3
  .select(".canvas")
  .append("svg")
  .attr("width", 900)
  .attr("height", 600);

const graph = svg.append("g").attr("width", 500).attr("height", 400);

graph
  .append("rect")
  .attr("x", 0)
  .attr("y", 0)
  .attr("width", 900)
  .attr("height", 500)
  .attr("fill", "#fff1e5")
  .attr("stroke", "black")
  .attr("stroke-width", 3);

graph
  .append("circle")
  .attr("cx", 200)
  .attr("cy", 200)
  .attr("r", 40)
  .attr("fill", "grey");
