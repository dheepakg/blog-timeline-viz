const svg = d3
  .select(".canvas")
  .append("svg")
  .attr("width", 900)
  .attr("height", 600);

svg
  .append("circle")
  .attr("cx", 200)
  .attr("cy", 300)
  .attr("r", 40)
  .attr("fill", "grey")
  .on("mouseover", function (d) {
    tip
      .style("opacity", 1)
      .html("Something")
      .style("left", d.pageX - 25 + "px")
      .style("top", d.pageY - 75 + "px");
  })
  // we hide our tooltip on "mouseout"
  .on("mouseout", function () {
    tip.style("opacity", 0);
  });

var tip = d3
  .select("body")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);
