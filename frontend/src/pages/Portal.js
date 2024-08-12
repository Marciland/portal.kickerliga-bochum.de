const getPlayers = (entries) => {
  let players = [];

  for (let i = 1; i <= 18; i++) {
    let entry = entries[`field${i}`];
    if (entry) {
      players.push(entry);
    }
  }

  return players;
};

const createRequestOptions = (entries) => {
  let payload = {
    mk1: entries["mk-field1"],
    mk2: entries["mk-field2"],
    players: getPlayers(entries),
  };
  const key = entries.key.replace(/"/g, ""); // expect users to copy pasta

  return {
    method: "POST",
    headers: {
      Authorization: `Bearer ${key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  };
};

const sendRequest = async (entries) => {
  const url = "https://marciland.net/kickerliga-bochum/api/team/create";
  const requestOptions = createRequestOptions(entries);

  try {
    let response = await fetch(url, requestOptions);
    if (!response.ok) {
      console.log(response.status); // todo handle 400, 403 422 and 5XX
    }
  } catch (error) {
    console.log(error); // todo display error
  }
};

export { getPlayers, createRequestOptions, sendRequest };
