import rhinoscriptsyntax as rs
from Rhino import *
from Rhino.Commands import *
from Rhino.DocObjects import *
from scriptcontext import doc

def CopyObjectsToLayer():
    objs = rs.ObjectsByType(16, select=False)	#get all polysurfaces in model

    if objs:
        layer_objs = []	#empty list to store objs to be copied to own layer

        rs.EnableRedraw(False)		#disable redraw to speed up script

        #start of for loop
        for i in range(len(objs)):
            obj = objs[i]				#get polysurface at current index
            
            if objs:
                # Add the new layer if necessary
                if( not rs.IsLayer(obj) ): rs.AddLayer(obj)
                # Copy the objects
                newObjectId = rs.CopyObjects(obj)

                # Set the layer of the copied objects
                [rs.ObjectLayer(id, obj) for id in newObjectId]
                # Select the newly copied objects
                rs.SelectObjects( newObjectId )
            
                current_layer_index = doc.Layers.CurrentLayerIndex
                for selected_object in selected_objects:
                    selected_object.Attributes.LayerIndex = current_layer_index
                    selected_object.CommitChanges()

        #end of loop

        rs.EnableRedraw(True)	#enable redraw to finalize operation
        

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
  #call function defined above
  CopyObjectsToLayer()