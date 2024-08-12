import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  test: {
    environment: "jsdom",
    include: ["**/*.unit.js"],
    coverage: {
      provider: "istanbul",
      exclude: [
        "dist",
        "**/index.js",
        "**/main.js",
        "**/*.vue",
        "vite.config.js",
      ],
      all: true,
    },
  },
});
