import bpy, bmesh, math

from .batch import c_batch

class c_batches(object):
    def __init__(self, vertexGroupsCount):
        
        def get_batches(self):
            batches = []
            #boneSetIndex = -1
            currentVertexGroup = -1

            numOfBatches = 0
            for obj in bpy.data.objects:
                if obj.type == 'MESH':
                    numOfBatches += 1

            curBatch = 0
            #while curBatch <= numOfBatches-1:
            for curBatch in range(numOfBatches):
                batchFound = False
                for obj in bpy.data.objects:
                    if obj.type == 'MESH':
                        obj_name = obj.name.split('-')

                        if int(obj_name[0]) == curBatch:
                            batchFound = True
                            obj_vertexGroupIndex = int(obj_name[-1])
                            print('[+] Generating Batch', obj.name)
                            
                            if obj_vertexGroupIndex != currentVertexGroup:      # Start of new vertex group
                                currentVertexGroup = obj_vertexGroupIndex
                                cur_indexStart = 0
                                cur_numVertexes = 0

                            if 'boneSetIndex' in obj:
                                obj_boneSetIndex = obj['boneSetIndex']
                            else:
                                obj_boneSetIndex = -1

                            batches.append(c_batch(obj, obj_vertexGroupIndex, cur_indexStart, cur_numVertexes, obj_boneSetIndex))
                            cur_indexStart += batches[len(batches)-1].numIndexes
                            cur_numVertexes = batches[len(batches)-1].numVertexes
                            #curBatch += 1
                if not batchFound:
                    print(" - Batches Error: Could not create batches in order as batch number", curBatch, "is missing! Expect unpredictable results!")

            return batches

        self.batches = get_batches(self)
        self.batches_StructSize = len(self.batches) * 28