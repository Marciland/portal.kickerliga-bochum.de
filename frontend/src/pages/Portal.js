import { useAlertStore } from "@/stores";

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

const handleResponse = async (alertStore, response) => {
  if (response.ok) {
    return alertStore.info("Daten wurden erfolgreich übermittelt!");
  }
  if (response.status === 401) {
    return alertStore.error("Ungültiger Schlüssel!");
  }
  if ([400, 404].includes(response.status)) {
    let body = await response.json();
    return alertStore.error("Es ist ein Fehler aufgetreten:<br>" + body.detail);
  }
  alertStore.error(response.status);
};

const sendRequest = async (entries) => {
  const alertStore = useAlertStore();
  const url = "https://marciland.net/kickerliga-bochum/api/team/create";
  const requestOptions = createRequestOptions(entries);

  await fetch(url, requestOptions)
    .then((response) => handleResponse(alertStore, response))
    .catch((error) =>
      alertStore.error("Das sollte nicht passieren!<br>" + error)
    );
};

export { getPlayers, createRequestOptions, sendRequest };
