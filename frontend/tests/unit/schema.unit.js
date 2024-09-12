import validSchema from "@/components/schema";

describe("Schema", () => {
  let baseFields;

  beforeEach(() => {
    baseFields = {
      key: "header.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
      "mk-field1": "John Doe",
      "mk-field2": "Jane Doe",
      field1: "Jane Smith",
      ...Array.from({ length: 16 }, (_, i) => ({
        [`field${i + 2}`]: "Valid Name",
      })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
    };
  });

  it("should validate with all valid fields", async () => {
    await expect(validSchema.validate(baseFields)).resolves.toBeDefined();
  });

  it("should fail on invalid JWT", async () => {
    const fields = { ...baseFields, key: "invalid.token" };
    await expect(validSchema.validate(fields)).rejects.toThrow(
      "Kein gültiger Schlüssel!"
    );
  });

  it("should fail on empty mk", async () => {
    const fields = {
      ...baseFields,
      "mk-field1": "",
      "mk-field2": "",
    };
    await expect(validSchema.validate(fields)).rejects.toThrow("MK notwendig!");
  });

  it("should fail on missing mk", async () => {
    const fields = {
      key: "header.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    };
    await expect(validSchema.validate(fields)).rejects.toThrow("MK notwendig!");
  });

  it("should fail on empty key", async () => {
    const fields = { ...baseFields, key: "" };
    await expect(validSchema.validate(fields)).rejects.toThrow(
      "Autorisierung notwendig!"
    );
  });

  it("should fail on missing key", async () => {
    const fields = {
      "mk-field1": "John Doe",
      "mk-field2": "Jane Doe",
    };
    await expect(validSchema.validate(fields)).rejects.toThrow(
      "Autorisierung notwendig!"
    );
  });
});
