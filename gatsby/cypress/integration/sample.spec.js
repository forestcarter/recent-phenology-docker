///<reference types="cypress"/>

describe("HydroSource", () => {
  beforeEach(() => {
    cy.visit("page-2/")
  })

  it("has a title", () => {
    cy.contains("HydroSource App")
  })
  it("selects two counties", () => {
    cy.wait(3000)
    cy.get("#map").click(200, 200)
    cy.get("#map").click(240, 240)
  })
})
