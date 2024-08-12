import { getPlayers, createRequestOptions, sendRequest } from "@/pages/Portal";

describe("getPlayers", () => {
  it("returns an array of players from the entries object", () => {
    const entries = {
      field1: "Player 1",
      field2: "Player 2",
      field3: "Player 3",
    };

    const result = getPlayers(entries);

    expect(result).toEqual(["Player 1", "Player 2", "Player 3"]);
  });

  it("returns an empty array when no players are found", () => {
    const entries = {};

    const result = getPlayers(entries);

    expect(result).toEqual([]);
  });

  it("skips over undefined or empty fields", () => {
    const entries = {
      field1: "Player 1",
      field5: "Player 5",
      field10: "Player 10",
    };

    const result = getPlayers(entries);

    expect(result).toEqual(["Player 1", "Player 5", "Player 10"]);
  });
});

describe("createRequestOptions", () => {
  let entries;

  beforeEach(() => {
    entries = {
      "mk-field1": "value1",
      "mk-field2": "value2",
      key: "someKey",
      field1: "Player 1",
      field2: "Player 2",
    };
  });

  it("creates the correct request options with a valid entries object", () => {
    const result = createRequestOptions(entries);

    expect(result).toEqual({
      method: "POST",
      headers: {
        Authorization: `Bearer ${entries.key}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mk1: entries["mk-field1"],
        mk2: entries["mk-field2"],
        players: [entries.field1, entries.field2],
      }),
    });
  });

  it("handles entries with no players correctly", () => {
    entries.field1 = null;
    entries.field2 = null;
    const expected = JSON.stringify({
      mk1: entries["mk-field1"],
      mk2: entries["mk-field2"],
      players: [],
    });

    const result = createRequestOptions(entries);

    expect(result.body).toEqual(expected);
  });

  it("removes quotes from the key correctly", () => {
    entries.key = '"key with quotes"';
    const keyWithoutQuotes = "key with quotes";

    const result = createRequestOptions(entries);

    expect(result.headers.Authorization).toEqual(`Bearer ${keyWithoutQuotes}`);
  });
});
