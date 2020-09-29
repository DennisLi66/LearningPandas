import pandas as p;
import numpy as n;

#Panel deprecitaed - find alternative?

def createPanel():
    l1 = [{'dbNumber':'1','Title':'Sailor Seas'},
          {'dbNumber':'2','Title':'Beyond the Jungle'},
          {'dbNumber':'3','Title':'Jumping Jacks'},
          {'dbNumber':'4','Title':'Scissor-Man'}];
    l2 = [{'dbNumber':'1','Author':'Jack Williat'},
          {'dbNumber':'1','Illustrator':'Emma Kilpers'},
          {'dbNumber':'2','Author':'Jesse Heisenberg'},
          {'dbNumber':'3','Author':'Flemmings Croshaw'},
          {'dbNumber':'4','Author':'Miles Pellings'}]
    general = p.DataFrame(l1),
    authors = p.DataFrame(l2),
    totality = p.DataFrame({'general':general,'authors':authors});




createPanel();

