import React, { Component } from "react"
import L from "leaflet"
import "leaflet.vectorgrid"
import "leaflet-basemaps"
import "../common/basemaps.css"
import { basemapsRaw } from "../common/functions"

class Map extends Component {
  componentDidMount() {
    this.map = L.map("map", {
      center: [32.1874446, -110.9185017],
      zoom: 6,
    })

    //Add Basemaps
    this.map.addControl(
      L.control.basemaps({
        basemaps: basemapsRaw.map(({ url, metadata }) =>
          L.tileLayer(url, metadata)
        ),
        position: "bottomleft",
        tileX: 0,
        tileY: 0,
        tileZ: 1,
      })
    )

    //Configure Map
    this.map.doubleClickZoom.disable()

    //Add Elements
  }

  componentDidUpdate(prevProps) {}

  render() {
    return <div style={{ gridArea: "map" }} id="map" />
  }
}

export default Map
