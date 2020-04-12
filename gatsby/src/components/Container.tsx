// @ts-ignore
import styled from "styled-components"

const Container = styled.div`
  margin-right: 1.25rem;
  text-align: center;
  height: 100%;
  background-color: #fff;
  display: grid;
  grid-gap: 20px;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr;
  grid-template-areas:
    "map content1"
    "map content2"
    "map content3"
    "map content4";
`
export default Container
