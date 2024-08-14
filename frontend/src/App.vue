<script setup>
import { onMounted, onUnmounted } from "vue";
import { resizeMain } from "@/App";
import * as bootstrap from "bootstrap";
import {
  AlertComponent,
  FooterNavbar,
  FooterCopyright,
  HeaderLogo,
  HeaderMenu,
} from "@/components";

onMounted(() => {
  window.addEventListener("load", resizeMain);
  window.addEventListener("resize", resizeMain);
});
onUnmounted(() => {
  window.removeEventListener("load", resizeMain);
  window.removeEventListener("resize", resizeMain);
});
</script>
<template>
  <header>
    <HeaderLogo />
    <!-- <HeaderMenu /> -->
  </header>
  <main>
    <AlertComponent />
    <router-view />
  </main>
  <footer>
    <FooterNavbar />
    <FooterCopyright />
  </footer>
</template>
<style>
.header-text {
  text-align: center;
  color: white;
  text-transform: uppercase;
  font-family: sans-serif;
  font-weight: bold;
  line-height: 1.25;
}
@media (min-width: 601px) {
  .header-text {
    text-align: start;
  }
}
</style>
