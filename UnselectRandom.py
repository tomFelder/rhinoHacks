import rhinoscriptsyntax as rs
import scriptcontext
import random

def RandomUnselect():
    ids = rs.SelectedObjects(False, False)
    if not ids: return
    
    if len(ids) == 1: return 
    
    if scriptcontext.sticky.has_key("RandomUnselect_percent"):
        percent_default = scriptcontext.sticky["RandomUnselect_percent"]
    else:
        percent_default = 50
    
    percent = rs.GetInteger("Percent to deselect", percent_default, 1, 99)
    if not percent: return
    
    objs = random.sample(ids, int(percent*len(ids)/100))
    
    rs.UnselectObjects(objs)
    
    scriptcontext.sticky["RandomUnselect_percent"] = percent

if __name__=="__main__":
    RandomUnselect()