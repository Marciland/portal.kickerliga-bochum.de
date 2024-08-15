<script setup>
import { storeToRefs } from "pinia";
import { useAlertStore } from "@/stores";

const alertStore = useAlertStore();
const { alert } = storeToRefs(alertStore);
</script>
<template>
  <div v-if="alert" class="custom-alert-container fixed-top mx-auto">
    <div class="m-3">
      <div class="alert alert-dismissable" :class="alert.type">
        <div v-html="alert.message"></div>
        <button @click="alertStore.clear()" class="close-button">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.close-button {
  background: transparent;
  border: none;
  color: #000;
  font-size: 24px;
  margin: 0;
  padding: 0;
  position: absolute;
  top: 7px;
  right: 10px;
  cursor: pointer;
}
.custom-alert-container {
  max-width: 500px;
  padding-top: 56px;
}
</style>
