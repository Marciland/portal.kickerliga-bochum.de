const resizeMain = () => {
  const header = document.querySelector("header");

  if (header) {
    document.documentElement.style.setProperty(
      "--header-height",
      `${header.offsetHeight}px`
    );
  }

  const footer = document.querySelector("footer");
  if (footer) {
    document.documentElement.style.setProperty(
      "--footer-height",
      `${footer.offsetHeight}px`
    );
  }
};

export { resizeMain };
