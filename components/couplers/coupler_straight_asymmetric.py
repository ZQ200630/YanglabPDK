import gdsfactory as gf

from YanglabPDK import YanglabUtils as Utils
from YanglabPDK import YanglabSections as Sections

from YanglabPDK.components.waveguides.straight import straight

@gf.cell
def coupler_straight_asymmetric(
    length: float = 10.0,
    gap: float = 0.27,
    width_top: float = 0.5,
    width_bot: float = 1,
    buffer: float = 3
) -> gf.Component:
    """Coupler with two parallel straights of different widths.

    Args:
        length: of straight.
        gap: between straights.
        width_top: of top straight.
        width_bot: of bottom straight.
    """
    c = gf.Component()

    top = c << straight(length=length, width=width_top, buffer=buffer)
    bot = c << straight(length=length, width=width_bot, buffer=buffer)

    dy = 0.5 * (width_top + width_bot) + gap
    top.dmovey(dy)
    c.add_port("o1", port=bot.ports[0])
    c.add_port("o2", port=top.ports[0])
    c.add_port("o3", port=top.ports[1])
    c.add_port("o4", port=bot.ports[1])
    c.flatten()
    return Utils.pos_neg_seperate(c)

if __name__ == "__main__":
    c = coupler_straight_asymmetric(length=10.0, gap=0.27, width_top=0.5, width_bot=1)
    c.show()