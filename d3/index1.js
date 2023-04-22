const svg = d3
  .select(".canvas")
  .append("svg")
  .attr("width", 750)
  .attr("height", 450);

const graph = svg.append("g").attr("width", 500).attr("height", 500);

graph
  .append("rect")
  .attr("x", 10)
  .attr("y", 10)
  .attr("width", 600)
  .attr("height", 600)
  .attr("fill", "#f7d2ad");

graph.append("text").text("2023").attr("x", 20).attr("y", 30);

graph
  .append("line")
  .attr("x1", 25 + 30)
  .attr("y1", 25)
  .attr("x2", 365 * 1.5)
  .attr("y2", 25)
  .attr("stroke", "grey")
  .attr("stroke-width", 3);
