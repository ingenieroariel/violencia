po.image = function() {
  var image = po.layer(load, unload),
      url = "about:blank";

  function load(tile) {
    var element = tile.element = po.svg("image"), size = image.map().tileSize();
    element.setAttribute("preserveAspectRatio", "none");
    element.setAttribute("width", size.x);
    element.setAttribute("height", size.y);
    element.setAttribute("opacity", 0);

    if (typeof url == "function") {
      tile.request = po.queue.image(element, url(tile), function(img) {
        delete tile.request;
        tile.ready = true;
        tile.img = img;
        element.removeAttribute("opacity");
        image.dispatch({type: "load", tile: tile});
      });
    } else {
      tile.ready = true;
      element.setAttributeNS(po.ns.xlink, "href", url);
      image.dispatch({type: "load", tile: tile});
    }
  }

  function unload(tile) {
    if (tile.request) tile.request.abort(true);
  }

  image.url = function(x) {
    if (!arguments.length) return url;
    url = typeof x == "string" && /{.}/.test(x) ? po.url(x) : x;
    return image.reload();
  };

  return image;
};
