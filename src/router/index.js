import { createRouter, createWebHistory } from "vue-router";
import { Index } from "@/pages";

export const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: "/", component: Index }],
});
