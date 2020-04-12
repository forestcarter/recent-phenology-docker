import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import Map from "../components/Map"
import Container from "../components/Container"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <Container>
      <Map />
    </Container>
  </Layout>
)

export default IndexPage
