<script setup></script>
<template>
  <div class="header-row">
    <div class="header-col header-image">
      <a href="https://kickerliga-bochum.de/">
        <img
          class="header-logo-size"
          src="https://kickerliga-bochum.de/wp-content/uploads/2019/01/klb_logo.png"
          alt="Kickerliga Bochum"
        />
      </a>
    </div>
    <div class="header-col header-text">
      <a
        style="font-size: 48px; color: inherit; text-decoration: none"
        href="https://kickerliga-bochum.de/"
        >Kickerliga Bochum</a
      >
      <div style="font-size: 20px; text-align: inherit">
        Tischfussball in Bochum
      </div>
    </div>
  </div>
</template>
<style scoped>
.header-row {
  background-image: url("https://kickerliga-bochum.de/wp-content/uploads/2019/01/cropped-klb.jpg");
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  padding: 28px;
}
.header-col {
  display: inherit;
  flex-direction: column;
  align-items: center;
  flex: 0 0 100%;
}
.header-logo-size {
  max-width: 300px;
  max-height: 120px;
}
@media (min-width: 601px) {
  .header-row {
    flex-direction: row;
  }
  .header-col {
    align-items: flex-start;
    justify-content: center;
    flex: 1 1 50%;
  }
  .header-image {
    max-width: fit-content;
    margin-top: -16px;
    margin-bottom: -16px;
    margin-right: 10px;
  }
}
</style>
