export const basemapsRaw = [
  {
    url:
      "//{s}.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
    metadata: {
      attribution:
        "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community",
      subdomains: ["server", "services"],
      label: "ESRI Topo",
    },
  },
  {
    url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    metadata: {
      attribution:
        "Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012",
      label: "OSM",
    },
  },
  {
    url:
      "//server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    metadata: {
      attribution:
        "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
      label: "ESRI Imagery",
    },
  },
  {
    url:
      "//{s}.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    metadata: {
      attribution: "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
      maxZoom: 16,
      subdomains: ["server", "services"],
      label: "ESRI Gray",
    },
  },
]

export const windowExists = typeof window !== "undefined"

const hostName = "localhost"
const protocol = windowExists ? window.location.protocol : "http:"

export const flaskUrl = `${protocol}//${hostName}/int/`

const fetchHelper = async (path: string, body: any) => {
  const result = await fetch(`${flaskUrl}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  })
  return await result.json()
}

export const fetchDates = async (path: string, setFunction: any) => {
  const results = await fetch(`${flaskUrl}${path}`)
  const data = await results.json()
  setFunction(data.result.dates)
}

export const colors = [
  [-13000, 100, 100, 100],

  [-4000, 202, 0, 32],
  [-2000, 244, 165, 130],
  [0, 255, 255, 255],
  [500, 224, 244, 220],
  [1000, 199, 233, 180],
  [1500, 162, 219, 184],
  [2000, 127, 205, 187],
  [2500, 96, 193, 181],
  [3000, 65, 182, 196],
  [3500, 55, 150, 190],
  [4000, 44, 127, 184],
  [6000, 40, 90, 166],
  [8000, 37, 52, 148],
]
