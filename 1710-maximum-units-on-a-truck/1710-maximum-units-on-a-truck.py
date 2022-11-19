class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda boxTypes: boxTypes[1], reverse = True)
        
        total_unit = 0
        left_boxes = truckSize
        
        for box_count, unit in boxTypes:
            if box_count <= left_boxes:
                total_unit += (unit*box_count)
                left_boxes -= box_count
            
            else:
                total_unit += (unit*left_boxes)
                left_boxes -= left_boxes
            
            if left_boxes == 0:
                return total_unit
            
        return total_unit