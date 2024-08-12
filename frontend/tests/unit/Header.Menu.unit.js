import { addOffset, flipDropdownArrow } from "@/components/Header/Menu";

describe("addOffset", () => {
  it("sets the left style of the menu element based in target id", () => {
    const offSet = 100;

    const event = { target: { id: "test", offsetLeft: offSet } };
    const menu = document.createElement("div");
    menu.id = "test-menu";
    document.body.appendChild(menu);

    expect(menu.style.left).toBe("");
    addOffset(event);
    expect(menu.style.left).toBe(`${offSet}px`);

    document.body.removeChild(menu);
  });
});

describe("flipDropdownArrow", () => {
  it('adds flipped-arrow class when event type contains "show"', () => {
    const event = {
      type: "show",
      target: { classList: { add: vi.fn(), remove: vi.fn() } },
    };

    flipDropdownArrow(event);

    expect(event.target.classList.add).toHaveBeenCalledWith("flipped-arrow");
    expect(event.target.classList.remove).not.toHaveBeenCalled();
  });

  it('removes flipped-arrow class when event type does not contain "show"', () => {
    const event = {
      type: "hide",
      target: { classList: { add: vi.fn(), remove: vi.fn() } },
    };

    flipDropdownArrow(event);

    expect(event.target.classList.remove).toHaveBeenCalledWith("flipped-arrow");
    expect(event.target.classList.add).not.toHaveBeenCalled();
  });
});
