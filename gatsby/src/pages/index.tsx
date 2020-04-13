import React, { useState, useEffect } from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import Map from "../components/Map"
import Container from "../components/Container"
import { fetchDates } from "../common/functions"
import Opacity from "../components/opacity"
import CustomCard from "../components/CustomCard"

export default function IndexPage() {
  const [dates, setDates] = useState([])
  const [opacity, setOpacity] = useState(1)

  useEffect(() => {
    fetchDates("getdates", setDates)
  }, [])
  console.log(dates)

  return (
    <Layout>
      <SEO title="Home" />
      <Container>
        {dates.length > 0 && typeof window !== undefined ? (
          <Map dates={dates} opacity={opacity} />
        ) : null}
        <Opacity opacity={opacity} setOpacity={setOpacity} />
        <CustomCard
          style={{ marginBottom: "1rem" }}
          gridArea="content4"
          title="Description"
        >
          {" "}
          EMODIS data are obtained as 7 day composites. This viewer subtracts
          one composite from the subsequent week. These calculations result in
          positive values representing an increase in NDVI, negative values
          representing a decrease in NDVI, and zero representing no change. In
          the current symbology, red represents a decrease in NDVI, white
          represents small or no change, green represents an increase in NDVI,
          and blue represents a dramatic increase in NDVI.
        </CustomCard>
      </Container>
    </Layout>
  )
}
