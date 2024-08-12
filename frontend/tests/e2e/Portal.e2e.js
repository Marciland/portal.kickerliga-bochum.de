describe("Portal", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("should show an error message for invalid key", () => {
    cy.get('input[name="key"]').type("invalid key");
    cy.get('input[name="key"]').blur();
    cy.get('button[type="submit"]').click();

    cy.get('span[role="alert"]')
      .should("exist")
      .and("contain.text", "Kein gültiger Schlüssel!");
  });

  it("should show an error message for invalid name on any player field", () => {
    cy.get('input[name="field1"]').type("invalid name");
    cy.get('input[name="field1"]').blur();
    cy.get('button[type="submit"]').click();

    cy.get('span[role="alert"]')
      .should("exist")
      .and("contain.text", "Kein gültiger Name!");
  });

  it("should show an error message for invalid name on any mk field", () => {
    cy.get('input[name="mk-field1"]').type("invalid name");
    cy.get('input[name="mk-field1"]').blur();
    cy.get('button[type="submit"]').click();

    cy.get('span[role="alert"]')
      .should("exist")
      .and("contain.text", "Kein gültiger Name!");
  });

  it("should show error messages for missing entries", () => {
    cy.get('button[type="submit"]').click();

    cy.get('span[role="alert"]').should("have.length", 3); // 3 = 2x MK + 1x key
    cy.get('span[role="alert"]').should("contain.text", "MK notwendig!");
    cy.get('span[role="alert"]').should(
      "contain.text",
      "Autorisierung notwendig!"
    );
  });
});
