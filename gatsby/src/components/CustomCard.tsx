import React from "react"

export default function CustomCard(props: any) {
  const marginTop = ["content1", "content2"].includes(props.gridArea)
    ? "20px"
    : "0"
  const innerStyle = props.innerStyle || {}
  return (
    <div
      style={{
        border: "1px solid lightgrey",
        borderRadius: "8px",
        marginBottom: "auto",
        marginTop,
        width: "100%",
        textAlign: "center",
        gridArea: props.gridArea,
        ...props.style,
      }}
    >
      <h5
        style={{
          margin: "0 auto",
          padding: "0.25rem 0 0.25rem 0",
          backgroundColor: "rgb(34, 118, 172)",
          borderRadius: "8px 8px 0px 0px",
          color: "white",
        }}
      >
        {props.title}
      </h5>
      <div
        id={props.id || props.title}
        style={{
          padding: "0.2rem",
          overflow: "auto",
          borderTop: "1px solid lightgrey",
          ...innerStyle,
        }}
      >
        {props.children}
      </div>
    </div>
  )
}
