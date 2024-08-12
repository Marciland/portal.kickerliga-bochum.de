import { createRouter, createWebHistory } from "vue-router";
import { Portal } from "@/pages";

export const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: "/", component: Portal }],
});
