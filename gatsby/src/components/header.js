import PropTypes from "prop-types"
import React from "react"
import { Link } from "gatsby"

const Header = ({ siteTitle, desc }) => (
  <header
    style={{
      background: `#2276AC`,
      marginBottom: `0rem`,
      height: "97px",
      paddingLeft: "20px",
    }}
  >
    <div
      style={{
        width: "fit-content",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      {/* <BannerImage /> */}
      <h2 style={{ margin: 0 }}>
        <Link
          to="/page-2"
          style={{
            color: `white`,
            fontFamily: "Helvetica Neue",
            textDecoration: `none`,
          }}
        >
          {siteTitle}
        </Link>
      </h2>
    </div>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
