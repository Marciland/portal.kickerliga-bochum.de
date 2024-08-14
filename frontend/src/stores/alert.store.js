import { defineStore } from "pinia";

export const useAlertStore = defineStore({
  id: "alert",
  state: () => ({
    alert: null,
  }),
  actions: {
    error(message) {
      this.alert = { message, type: "alert-danger" };
    },
    info(message) {
      this.alert = { message, type: "alert-info" };
    },
    clear() {
      this.alert = null;
    },
  },
});
