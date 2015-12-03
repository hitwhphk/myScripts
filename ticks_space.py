# -*- coding: utf-8 -*-



import numpy as np
from Tkinter import *

import matplotlib.ticker as mpticker
import matplotlib.transforms as mtrans
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
class math(object):
    def __init__(self,parent,*args,**kwargs):
        self.parent = parent
        frameToolbar = Frame(self.parent)
        frameToolbar.pack(fill = X,expand = 0,side = TOP)
        frame = Frame(self.parent)
        frame.pack(fill = BOTH,expand = 1,side = TOP)
        figure = Figure()
      
        
        self.canvas = FigureCanvasTkAgg(figure,master = frame)
        toolbar = NavigationToolbar2TkAgg(self.canvas,frameToolbar)
        toolbar.update()
        self.canvas.get_tk_widget().pack(fill=BOTH,expand = 1)
        self.axe = figure.add_subplot(111)
        self.axe.grid(True)
        
        image = np.uint8(np.random.rand(10,10))
        self.axe.imshow(image)
        
        self.axe.set_xlabel('Hours')

        self.axe.xaxis.set_major_locator(ScaledLocator(dx=0.5))
        self.axe.xaxis.set_major_formatter(ScaledFormatter(dx=0.5))
        
        self.canvas.show()
        
        

class ScaledLocator(mpticker.MaxNLocator):
    """
    Locates regular intervals along an axis scaled by *dx* and shifted by
    *x0*. For example, this would locate minutes on an axis plotted in seconds
    if dx=60.  This differs from MultipleLocator in that an approriate interval
    of dx units will be chosen similar to the default MaxNLocator.
    """
    def __init__(self, dx=1.0, x0=0.0):
        self.dx = dx
        self.x0 = x0
        mpticker.MaxNLocator.__init__(self, nbins=9, steps=[1, 2, 5, 10])

    def rescale(self, x):
        return x / self.dx + self.x0
    def inv_rescale(self, x):
        return  (x - self.x0) * self.dx

    def __call__(self): 
        vmin, vmax = self.axis.get_view_interval()
        vmin, vmax = self.rescale(vmin), self.rescale(vmax)
        vmin, vmax = mtrans.nonsingular(vmin, vmax, expander = 0.05)
        locs = self.bin_boundaries(vmin, vmax)
        locs = self.inv_rescale(locs)
        prune = self._prune
        if prune=='lower':
            locs = locs[1:]
        elif prune=='upper':
            locs = locs[:-1]
        elif prune=='both':
            locs = locs[1:-1]
        return self.raise_if_exceeds(locs)

class ScaledFormatter(mpticker.OldScalarFormatter):
    """Formats tick labels scaled by *dx* and shifted by *x0*."""
    def __init__(self, dx=1.0, x0=0.0, **kwargs):
        self.dx, self.x0 = dx, x0

    def rescale(self, x):
        return x / self.dx + self.x0

    def __call__(self, x, pos=None):
        xmin, xmax = self.axis.get_view_interval()
        xmin, xmax = self.rescale(xmin), self.rescale(xmax)
        d = abs(xmax - xmin)
        x = self.rescale(x)
        s = self.pprint_val(x, d)
        return s   


if __name__ == "__main__":        

    root = Tk()       
    test = math(root,)
    root.mainloop()
