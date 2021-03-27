#A function to darkern/lighten colors in matplotlib
def adjust_lightness(color, amount=0.5):
    #Import color modules
    import matplotlib.colors as mc
    import colorsys
    #Check what type of color this is
    try:
        c = mc.cnames[color]
    except:
        c = color
    #Convert color to easy to work with type
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    #Return the adjusted color
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])
