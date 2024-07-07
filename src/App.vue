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

const flipDropdownArrow = (event) => {
  if (event.type.includes("show")) {
    event.target.classList.add("flipped-arrow");
  } else {
    event.target.classList.remove("flipped-arrow");
  }
};

onMounted(() => {
  window.addEventListener("load", resizeMain);
  window.addEventListener("resize", resizeMain);
  const spieltage = document.getElementById("spieltage");
  spieltage.addEventListener("show.bs.dropdown", flipDropdownArrow);
  spieltage.addEventListener("hide.bs.dropdown", flipDropdownArrow);
  const ergebnisse = document.getElementById("ergebnisse");
  ergebnisse.addEventListener("show.bs.dropdown", flipDropdownArrow);
  ergebnisse.addEventListener("hide.bs.dropdown", flipDropdownArrow);
});
onUnmounted(() => {
  window.removeEventListener("load", resizeMain);
  window.removeEventListener("resize", resizeMain);
  const spieltage = document.getElementById("spieltage");
  spieltage.removeEventListener("show.bs.dropdown", flipDropdownArrow);
  spieltage.removeEventListener("hide.bs.dropdown", flipDropdownArrow);
  const ergebnisse = document.getElementById("ergebnisse");
  ergebnisse.removeEventListener("show.bs.dropdown", flipDropdownArrow);
  ergebnisse.removeEventListener("hide.bs.dropdown", flipDropdownArrow);
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
