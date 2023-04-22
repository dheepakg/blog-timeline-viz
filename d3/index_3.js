const svg = d3
  .select(".canvas")
  .append("svg")
  .attr("width", 750)
  .attr("height", 450);

const LINE_ORIGIN = 65;
const TEXT_ORIGIN = 20;

const graph = svg.append("g").attr("width", 500).attr("height", 500);

graph
  .append("rect")
  .attr("x", 10)
  .attr("y", 10)
  .attr("width", 600)
  .attr("height", 600)
  .attr("fill", "#fff1e5");

d3.json("details_3.json").then((data) => {
  // Sclaing
  // Defines the year line
  const y = d3
    .scaleBand()
    .domain(data.map((item) => item.year))
    .range([10, 500])
    .paddingInner(0.2)
    .paddingOuter(0.2);

  // Defines position of dot
  const x = d3.scaleLinear().domain([1, 365]).range([65, 547.5]);

  // console.log(d3.extent(["2021-01-02", "2021-12-30"]));

  const lines = graph.selectAll("line").data(data);
  const texts = lines.select("text").data(data);
  const circles = lines.select("circle").data(data);

  texts
    .enter()
    .append("text")
    .text((d) => d.year)
    .attr("x", TEXT_ORIGIN)
    .attr("y", (d) => y(d.year) + 5)
    .attr("font-size", 20)
    .attr("font-weight", "Bold");
  // .attr("fill", "#5588ee");

  lines
    .append("line")
    .attr("x1", LINE_ORIGIN)
    .attr("y1", (d) => y(d.year))
    .attr("x2", 365 * 1.5)
    .attr("y2", (d) => y(d.year))
    .attr("stroke", "#add8e6")
    .attr("stroke-width", 10);

  lines
    .enter()
    .append("line")
    .attr("x1", LINE_ORIGIN)
    .attr("y1", (d) => y(d.year))
    .attr("x2", 365 * 1.5)
    .attr("y2", (d) => y(d.year))
    .attr("stroke", "#add8e6")
    .attr("stroke-width", 10);

  circles
    .enter()
    .append("circle")
    .attr("r", 4)
    .attr("cx", (d) => LINE_ORIGIN + d.day)
    .attr("cy", (d) => y(d.year))
    .attr("fill", "black")
    .attr("stroke-width", 1)
    .attr("stroke", "#ffff00");

  console.log(data[0].perm_url);
});
