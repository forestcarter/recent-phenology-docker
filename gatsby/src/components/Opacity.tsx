import React from "react"
import CustomCard from "./CustomCard"

export default function Opacity(props: any) {
  const { opacity, setOpacity } = props
  return (
    <CustomCard title="Opacity" gridArea="content2">
      <input
        id="slide"
        type="range"
        min="0"
        max="1"
        step="0.1"
        value={opacity}
        onChange={e => {
          setOpacity(e.target.value)
        }}
      />
    </CustomCard>
  )
}
