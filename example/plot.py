# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
# read and add font files
font_files = font_manager.findSystemFonts(fontpaths=['../fonts'])
for font_file in font_files:
    print (font_file)
    font_manager.fontManager.addfont(font_file)

# force matplotlib to use the new fonts
plt.rcParams['font.family'] = 'HersheyTex_Book'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'HersheyTex_Book'
plt.rcParams['mathtext.it'] = 'HersheyTex_Book'
plt.rcParams['mathtext.bf'] = 'HersheyTex_Book'

# some minor tweaking to match the aesthetics
plt.rcParams['figure.dpi'] = 300
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.rcParams['lines.linewidth'] = 0.5
plt.rcParams['axes.linewidth'] = 0.45
plt.rcParams['legend.frameon'] = False
plt.rcParams['xtick.major.width'] = 0.5
plt.rcParams['ytick.major.width'] = 0.5
plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['figure.facecolor'] = 'white'

# plotting
xs = np.linspace(-5, 5, 100)
ys = np.exp(-xs**2)

plt.plot(xs, ys, c='k')
plt.yscale('log')
plt.title('My quantity: $e^{-\\xi^2}$')
plt.xlabel('$\\xi$')
plt.ylabel('$\\log{\\{\\exp{(-\\xi^2)}\\}} = -\\xi^2$')

plt.savefig('plot.svg', bbox_inches='tight')
# %%
