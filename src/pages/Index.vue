<script setup>
import { ref } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";

import validSchema from "@/components/schema";

const isSubmitting = ref(false);

const submit = (entries) => {
  isSubmitting.value = true;
  console.log(entries);
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
    <ErrorMessage name="key" />
    <div class="field-container">
      <div v-for="i in 20" :key="i" class="field">
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
    <button type="submit" :disabled="isSubmitting">
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
}
.field-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.field {
  display: flex;
  flex-direction: column;
  text-align: center;
  padding: 2px;
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
