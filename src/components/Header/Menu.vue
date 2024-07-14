<script setup>
import { onMounted, onUnmounted } from "vue";

const addOffset = (event) => {
  const menu = document.getElementById(event.target.id + "-menu");
  menu.style.left = event.target.offsetLeft + "px";
};

onMounted(() => {
  const spieltage = document.getElementById("spieltage");
  spieltage.addEventListener("show.bs.dropdown", addOffset);
  const ergebnisse = document.getElementById("ergebnisse");
  ergebnisse.addEventListener("show.bs.dropdown", addOffset);
});
onUnmounted(() => {
  const spieltage = document.getElementById("spieltage");
  spieltage.removeEventListener("show.bs.dropdown", addOffset);
  const ergebnisse = document.getElementById("ergebnisse");
  ergebnisse.removeEventListener("show.bs.dropdown", addOffset);
});
</script>
<template>
  <nav
    class="navbar bg-dark navbar-expand-md"
    style="display: flex; justify-content: center; padding: 0px"
  >
    <button
      class="navbar-toggler"
      data-bs-toggle="collapse"
      data-bs-target="#menu-container"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div
      id="menu-container"
      class="collapse navbar-collapse header-menu header-text"
    >
      <ul>
        <li>
          <a href="https://kickerliga-bochum.de/">Home</a>
        </li>
        <li>
          <a
            id="spieltage"
            class="dropdown dropdown-arrow"
            role="button"
            data-bs-toggle="dropdown"
            href="#"
            >Spieltage</a
          >
          <ul id="spieltage-menu" class="dropdown-menu">
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/spieltage-1-liga/"
                >Spieltage 1. Liga</a
              >
            </li>
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/spieltage-2-liga/"
                >Spieltage 2. Liga</a
              >
            </li>
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/spieltage-3-liga/"
                >Spieltage 3. Liga</a
              >
            </li>
          </ul>
        </li>
        <li>
          <a
            id="ergebnisse"
            class="dropdown dropdown-arrow"
            role="button"
            data-bs-toggle="dropdown"
            href="#"
            >Ergebnisse</a
          >
          <ul id="ergebnisse-menu" class="dropdown-menu">
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/fixtures-results/"
                >Ergebnisse 1. Liga</a
              >
            </li>
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/ergebnisse-2-liga/"
                >Ergebnisse 2. Liga</a
              >
            </li>
            <li class="dropdown-item">
              <a href="https://kickerliga-bochum.de/ergebnisse-3-liga/"
                >Ergebnisse 3. Liga</a
              >
            </li>
          </ul>
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/tabellen-2/">Tabellen</a>
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/mannschaften/">Mannschaften</a>
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/bochum-cup/"
            >Bochum Cup 2020 / 2021</a
          >
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/titeltrager/">Titelträger</a>
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/statuten/">Statuten</a>
        </li>
        <li>
          <a href="https://kickerliga-bochum.de/ewige-tabelle/"
            >Ewige Tabelle</a
          >
        </li>
      </ul>
      <div style="display: none">Suche?</div>
    </div>
  </nav>
</template>
<style scoped>
.navbar-toggler {
  padding: 8px;
  border: 0px;
}
.navbar-toggler:focus,
.navbar-toggler:active,
.navbar-toggler-icon:focus {
  outline: none;
  box-shadow: none;
}
.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255, 0, 0, 1)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}
.header-menu {
  background-color: rgb(38, 42, 46);
}
.header-menu > ul,
.header-menu > ul > li > ul {
  margin-bottom: 0px;
  padding-left: 0px;
  list-style: none;
}
.header-menu > ul > li > a:hover,
.header-menu > ul > li > ul > li > a:hover {
  background-color: #e80000;
}
.header-menu > ul > li,
.header-menu > ul > li > ul > li {
  font-weight: normal;
  text-align: start;
  padding-top: 0px;
  padding-bottom: 0px;
}
.header-menu > ul > li > a,
.header-menu > ul > li > ul > li > a {
  text-decoration: none;
  color: inherit;
  display: flex;
  padding-left: 10px;
  padding-top: 8.75px;
  padding-bottom: 8.75px;
}
.dropdown-menu {
  background-color: rgb(33, 37, 41);
  color: inherit;
  position: static;
  float: none;
  padding: 0px;
  border: 0px;
  margin: 0px;
}
.dropdown-item {
  color: inherit;
  padding-left: 0px;
  padding-right: 0px;
}
.dropdown-arrow {
  outline: none;
}
.dropdown-arrow::after {
  display: inline-block;
  width: 0.6em;
  height: 0.6em;
  margin: 0.1em 0 0 0.4em;
  vertical-align: middle;
  content: "";
  border: 0.3em solid;
  border-width: 0 0.15em 0.15em 0;
  transform: rotateZ(45deg);
}
.flipped-arrow::after {
  transform: rotate(225deg);
  margin: 0.4em 0 0 0.4em;
}
@media (min-width: 768px) {
  .header-menu > ul {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  .header-menu > ul > li > a,
  .header-menu > ul > li > ul > li > a {
    padding-left: 10px;
    padding-right: 10px;
  }
  .dropdown-menu {
    position: absolute;
  }
}
</style>
