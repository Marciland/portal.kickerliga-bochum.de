import { resizeMain } from "@/App";

describe("", () => {
  let header;
  let footer;

  beforeEach(() => {
    header = document.createElement("header");
    footer = document.createElement("footer");

    document.body.appendChild(header);
    document.body.appendChild(footer);
  });

  afterEach(() => {
    if (document.body.contains(header)) {
      document.body.removeChild(header);
    }
    if (document.body.contains(footer)) {
      document.body.removeChild(footer);
    }
  });

  it("resizeMain should set CSS custom properties for header and footer heights", () => {
    const headerOffsetHeight = 66;
    const footerOffsetHeight = 666;
    Object.defineProperty(header, "offsetHeight", {
      value: headerOffsetHeight,
    });
    Object.defineProperty(footer, "offsetHeight", {
      value: footerOffsetHeight,
    });

    const setPropertySpy = vi.spyOn(
      document.documentElement.style,
      "setProperty"
    );

    resizeMain();

    expect(setPropertySpy).toHaveBeenCalledWith(
      "--header-height",
      `${headerOffsetHeight}px`
    );
    expect(setPropertySpy).toHaveBeenCalledWith(
      "--footer-height",
      `${footerOffsetHeight}px`
    );
  });

  it("does not set header without header, but sets footer property", () => {
    document.body.removeChild(header);

    const headerOffsetHeight = 66;
    const footerOffsetHeight = 666;
    Object.defineProperty(footer, "offsetHeight", {
      value: footerOffsetHeight,
    });

    const setPropertySpy = vi.spyOn(
      document.documentElement.style,
      "setProperty"
    );

    resizeMain();

    expect(setPropertySpy).toHaveBeenCalledTimes(1);
    expect(setPropertySpy).not.toHaveBeenCalledWith(
      "--header-height",
      `${headerOffsetHeight}px`
    );
    expect(setPropertySpy).toHaveBeenCalledWith(
      "--footer-height",
      `${footerOffsetHeight}px`
    );
  });

  it("does not set header without header, but sets footer property", () => {
    document.body.removeChild(header);

    const headerOffsetHeight = 66;
    const footerOffsetHeight = 666;
    Object.defineProperty(footer, "offsetHeight", {
      value: footerOffsetHeight,
    });

    const setPropertySpy = vi.spyOn(
      document.documentElement.style,
      "setProperty"
    );

    resizeMain();

    expect(setPropertySpy).toHaveBeenCalledTimes(1);
    expect(setPropertySpy).not.toHaveBeenCalledWith(
      "--header-height",
      `${headerOffsetHeight}px`
    );
    expect(setPropertySpy).toHaveBeenCalledWith(
      "--footer-height",
      `${footerOffsetHeight}px`
    );
  });

  it("does not set footer without footer, but sets header property", () => {
    document.body.removeChild(footer);

    const headerOffsetHeight = 66;
    const footerOffsetHeight = 666;
    Object.defineProperty(header, "offsetHeight", {
      value: headerOffsetHeight,
    });

    const setPropertySpy = vi.spyOn(
      document.documentElement.style,
      "setProperty"
    );

    resizeMain();

    expect(setPropertySpy).toHaveBeenCalledTimes(1);
    expect(setPropertySpy).toHaveBeenCalledWith(
      "--header-height",
      `${headerOffsetHeight}px`
    );
    expect(setPropertySpy).not.toHaveBeenCalledWith(
      "--footer-height",
      `${footerOffsetHeight}px`
    );
  });
});
