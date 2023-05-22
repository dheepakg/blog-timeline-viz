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
  .attr("cy", 300)
  .attr("r", 40)
  .attr("fill", "grey")
  .on("mouseover", function () {
    return tooltip.style("visibility", "visible");
  })
  .on("mousemove", function () {
    return tooltip.style("top", 300).style("left", 200);
  })
  .on("mouseout", function () {
    return tooltip.style("visibility", "hidden");
  });

var tooltip = d3
  .select("body")
  .append("div")
  .style("position", "relative")
  .style("display", "inline-block")
  .style("visibility", "hidden")
  .style("width", "120px")
  .style("background-color", "black")
  .style("color", "#fff")
  .style("text-align", "center")
  .style("border-radius", "6px")
  .style("padding", "5px 0")
  .style("position", "absolute")
  .style("z-index", "1")
  .text("a simple tooltip");
