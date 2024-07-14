<script setup>
import { onMounted, onUnmounted } from "vue";
import * as bootstrap from "bootstrap";
import {
  FooterNavbar,
  FooterCopyright,
  HeaderLogo,
  HeaderMenu,
} from "@/components";

const resizeMain = () => {
  const header = document.querySelector("header");
  const footer = document.querySelector("footer");

  if (header && footer) {
    document.documentElement.style.setProperty(
      "--header-height",
      `${header.offsetHeight}px`
    );
    document.documentElement.style.setProperty(
      "--footer-height",
      `${footer.offsetHeight}px`
    );
  }
};

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
    <HeaderMenu />
  </header>
  <main>
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
