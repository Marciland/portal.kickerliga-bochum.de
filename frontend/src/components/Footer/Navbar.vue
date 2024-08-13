<script setup></script>
<template>
  <div class="navbar bg-dark" style="align-items: stretch">
    <div name="meta-section" class="navbar-item">
      <h3>META</h3>
      <ul style="list-style: none">
        <li class="footer-list-item">
          <a
            class="kickerliga-link"
            href="https://kickerliga-bochum.de/praesidium/"
            >Präsidium</a
          >
        </li>
        <li class="footer-list-item">
          <a
            class="kickerliga-link"
            href="https://kickerliga-bochum.de/impressum/"
            >Impressum</a
          >
        </li>
      </ul>
    </div>
    <div name="contact-section" class="navbar-item">
      <h3>KONTAKT:</h3>
      <div>Frank Otto</div>
      <a class="kickerliga-link" href="mailto:info@kickerliga-bochum.de"
        >info@kickerliga-bochum.de</a
      >
    </div>
    <div name="community-section" class="navbar-item">
      <h3>COMMUNITY</h3>
      Damit sich MK&rsquo;s nachhaltig für Spiele verabreden können, muss man
      unserer
      <a
        class="kickerliga-link"
        href="https://discord.gg/HzsRCKt"
        target="_blank"
        rel="noopener"
        >Community beitreten</a
      >.
    </div>
  </div>
</template>
<style scoped>
.footer-list-item {
  position: relative;
  padding-bottom: 10px;
}
.footer-list-item:before {
  content: "";
  position: absolute;
  border-right: 2px solid grey;
  border-bottom: 2px solid grey;
  width: 10px;
  height: 10px;
  top: calc(50% - 4px);
  left: -20px;
  transform: translateY(-50%) rotate(-45deg);
}
.navbar-item {
  padding: 20px;
  flex: 0 0 100%;
  max-width: 100%;
}
.navbar-item h3 {
  font-size: 1.5rem;
}
@media (min-width: 601px) {
  .navbar-item {
    flex: 1 1 33%;
    max-width: 33%;
  }
}
</style>
