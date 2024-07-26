<script setup>
import { ref } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";

import validSchema from "@/components/schema";

const isSubmitting = ref(false);

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

const submit = async (entries) => {
  isSubmitting.value = true;

  let payload = {
    mk1: entries["mk-field1"],
    mk2: entries["mk-field2"],
    players: getPlayers(entries),
  };

  const requestOptions = {
    method: "POST",
    headers: {
      Authorization: `Bearer ${entries.key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  };

  try {
    let response = await fetch(
      "https://marciland.net/kickerliga-bochum/api/team/create",
      requestOptions
    );
    if (!response.ok) {
      console.log(response.status); // todo handle 400, 403 422 and 5XX
    }
  } catch (error) {
    console.log(error); // todo display error
  }

  isSubmitting.value = false;
};
</script>
<template>
  <Form
    class="form-container"
    :validation-schema="validSchema"
    @submit="submit"
  >
    <Field
      name="key"
      as="input"
      type="text"
      class="field-input"
      style="width: 200px"
      placeholder="Schlüssel zur Autorisierung"
    />
    <ErrorMessage name="key" style="margin-bottom: 25px" />
    <div class="field-container">
      <div v-for="i in 2" :key="i" class="field">
        <Field
          :name="`mk-field${i}`"
          as="input"
          type="text"
          class="field-input"
          :placeholder="`Name des MK${i}`"
        />
        <ErrorMessage :name="`mk-field${i}`" />
      </div>
    </div>
    <div class="field-container">
      <div v-for="i in 18" :key="i" class="field">
        <Field
          :name="`field${i}`"
          as="input"
          type="text"
          class="field-input"
          placeholder="Name des Spielers"
        />
        <ErrorMessage :name="`field${i}`" />
      </div>
    </div>
    <button
      class="btn bg-dark kickerliga-link"
      type="submit"
      :disabled="isSubmitting"
      style="margin-top: 25px"
    >
      Abschicken
      <span
        v-show="isSubmitting"
        class="spinner-border spinner-border-sm mr-1"
      ></span>
    </button>
  </Form>
</template>
<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - var(--header-height) - var(--footer-height));
  margin-top: 30px;
  margin-bottom: 30px;
}
.field-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 1329px;
}
.field {
  display: flex;
  flex-direction: column;
  text-align: center;
}
.field-input {
  margin: 5px;
}
.field-input::placeholder {
  text-align: center;
}
@media (min-width: 601px) {
  .field {
    padding: 10px;
  }
}
</style>
