import React, { Component } from "react"
import L from "leaflet"
import "leaflet.vectorgrid"
import "leaflet-basemaps"
import "../common/basemaps.css"
import "../common/legend.css"

import { basemapsRaw, colors } from "../common/functions"

class Map extends Component {
  componentDidMount() {
    const { dates } = this.props
    this.map = L.map("map", {
      center: [32.1874446, -110.9185017],
      zoom: 7,
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

    this.overlaymaps = {}

    dates.forEach(({ name }, ind) => {
      this[name] = L.tileLayer(
        `${window.location.protocol}//${window.location.hostname}/tiles4/${name}/{z}/{x}/{y}.png`,
        {
          enable: true,
          tms: true,
          opacity: 0.6,
          attribution: "",
        }
      )
      this.overlaymaps[name] = this[name]
      if (ind === 0) {
        this[name].addTo(this.map)
      }
    })

    //Configure Map2

    this.map.doubleClickZoom.disable()

    L.control.layers({}, this.overlaymaps).addTo(this.map)

    //Legend
    const getColor = d => {
      return `rgb(${d[1]},${d[2]},${d[3]})`
    }
    const legend = L.control({ position: "bottomright" })

    legend.onAdd = () => {
      const div = L.DomUtil.create("div", "info legend")
      let labels = []
      let from
      let to

      for (let i = 0; i < colors.length; i++) {
        from = colors[i]
        to = colors[i + 1]
        console.log(from, to)

        labels.push(
          '<i style="background:' +
            getColor(from) +
            '"></i> ' +
            from[0] +
            (to ? "&ndash;" + to[0] : "+")
        )
      }

      div.innerHTML = labels.join("<br>")
      return div
    }

    legend.addTo(this.map)
  }

  componentDidUpdate(prevProps) {
    if (this.props.opacity !== prevProps.opacity) {
      this.props.dates.forEach(({ name }) => {
        this[name].setOpacity(this.props.opacity)
        console.log(this[name])
      })
    }
  }

  render() {
    return <div style={{ gridArea: "map" }} id="map" />
  }
}

export default Map
