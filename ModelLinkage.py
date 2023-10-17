"""
Model our creature and wrap it in one class.
First version on 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

Modified by Daniel Scrivener 09/2023
"""

from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Cone
from Shapes import Cube
from Shapes import Cylinder
from Shapes import Sphere
import numpy as np
from GLUtility import GLUtility

### TODO 2 - ANSWER ###
'''
There are 11 objects in my model:
    1 * body: Cube()
    4 * leg: Cube()
    3 * tail: Cylinder()
    1 * head: Sphere()
    2 * ear: Cone()

    body 
        - head
            - ear1
            - ear2
        - leg1
        - leg2
        - leg3
        - leg4
        - tail1 - tail2 - tail3

'''
class TODO2_MyCat(Component):
    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        a = 1
        b = 0.6
        c = 1.5
        body = Cube(Point((0, 0, 0)), shaderProg, [a, b, c], Ct.GRAY, False)

        r = 0.1
        h = 0.5
        
        # pair = Component(Point((0,0,0)), None)
        leg1 = Cube(Point((a/2 - r, -b/2 - h/2, -c/2 + r)), shaderProg, [2*r, h, 2*r], Ct.WHITE, True, rotateBy=2)
        leg2 = Cube(Point((a/2 - r, -b/2 - h/2, c/2 - r)), shaderProg, [2*r, h, 2*r], Ct.WHITE, True, rotateBy=2)
        leg3 = Cube(Point((-a/2 + r, -b/2 - h/2, c/2 - r)), shaderProg, [2*r, h, 2*r], Ct.WHITE, True, rotateBy=2)
        leg4 = Cube(Point((-a/2 + r, -b/2 - h/2, -c/2 + r)), shaderProg, [2*r, h, 2*r], Ct.WHITE, True, rotateBy=2)

        h = 0.4
        r = 0.05
        tail1 = Cube(Point((0, b/2 - r, -c/2 - h/2)), shaderProg, [2*r, 2*r, h, ], Ct.SILVER, True, rotateBy=3)
        tail1.setDefaultAngle(-30, tail1.uAxis)

        tail2 = Cube(Point((0, 0, -h)), shaderProg, [2*r, 2*r, h,], Ct.ORANGE, True, rotateBy=3)
        tail2.setDefaultAngle(-30, tail1.uAxis)

        tail3 = Cube(Point((0, 0, -h)), shaderProg, [2*r, 2*r, h,], Ct.PINK, True, rotateBy=3)
        tail3.setDefaultAngle(-30, tail1.uAxis)

        r = 0.2
        h = 0.5
        head = Sphere(Point((0, b/2 , c/2 + 2*r)), shaderProg, [h, 2*r, 2*r], Ct.SILVER, True)
        ear1 = Cone(Point((r, r*1.5, 0)), shaderProg, [0.2,0.3,0.15], Ct.DARKORANGE4, False, True)
        ear2 = Cone(Point((-r, r*1.5, 0)), shaderProg, [0.2,0.3,0.15], Ct.DARKORANGE4, False, True)
        

        self.addChild(body)

        body.addChild(leg1)
        body.addChild(leg2)
        body.addChild(leg3)
        body.addChild(leg4)
        # body.addChild(pair)
        # pair.addChild(leg1)
        # pair.addChild(leg2)
        # pair.addChild(leg3)
        # pair.addChild(leg4)

        body.addChild(head)
        head.addChild(ear1)
        head.addChild(ear2)

        body.addChild(tail1)
        tail1.addChild(tail2)
        tail2.addChild(tail3)
        ### TODO 3 - ANSWER END ###

        ### TODO 6 - ANSWER ###
        R = 1
        r = 0.2
        sclera = Sphere(Point((0, 0, -4)), shaderProg, [R, R, R], Ct.WHITE, limb=False)
        pupil = Sphere(Point((0, 0, R + r)), shaderProg, [r, r, r], Ct.BLACK, limb=False)
        self.addChild(sclera)
        sclera.addChild(pupil)
        ### TODO 6 - ANSWER END ###

        self.componentList = [body, leg1, leg2, leg3, leg4, tail1, tail2, tail3, head]
        self.componentDict = {
            "body": body,
            "leg1": leg1,
            "leg2": leg2,
            "leg3": leg3,
            "leg4": leg4,
            "head": head,
            "tail1": tail1,
            "tail2": tail2,
            "tail3": tail3,
            "sclera": sclera,
            "pupil": pupil,
        }


        ### TODO 4 - ANSWER ###
        '''
        I use function Component.setRotateExtent() to set the limit on rotation angle. 
        '''
        leg1.setRotateExtent(leg1.vAxis, -10, 10)
        leg1.setRotateExtent(leg1.wAxis, -10, 10)
        leg1.setRotateExtent(leg1.uAxis, -45, 45)

        leg2.setRotateExtent(leg2.vAxis, -10, 10)
        leg2.setRotateExtent(leg2.wAxis, -10, 10)
        leg2.setRotateExtent(leg2.uAxis, -45, 45)

        leg3.setRotateExtent(leg3.vAxis, -10, 10)
        leg3.setRotateExtent(leg3.wAxis, -10, 10)
        leg3.setRotateExtent(leg3.uAxis, -45, 45)

        leg4.setRotateExtent(leg4.vAxis, -10, 10)
        leg4.setRotateExtent(leg4.wAxis, -10, 10)
        leg4.setRotateExtent(leg4.uAxis, -45, 45)

        
        tail1.setRotateExtent(tail1.uAxis, -40, 40)
        tail1.setRotateExtent(tail1.vAxis, -90, 90)
        tail1.setRotateExtent(tail1.wAxis, -70, 70)

        tail2.setRotateExtent(tail2.uAxis, -40, 40)
        tail2.setRotateExtent(tail2.vAxis, -90, 90)
        tail2.setRotateExtent(tail2.wAxis, -70, 70)

        tail3.setRotateExtent(tail3.uAxis, -40, 40)
        tail3.setRotateExtent(tail3.vAxis, -90, 90)
        tail3.setRotateExtent(tail3.wAxis, -70, 70)

        head.setRotateExtent(head.uAxis, -50, 50)
        head.setRotateExtent(head.vAxis, -50, 50)
        head.setRotateExtent(head.uAxis, -20, 20)

        ### TODO 4 - ANSWER END ###



class ModelLinkage(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 
    #
    # In order to simplify the process of constructing your model, the rotational origin of each Shape has been offset by -1/2 * dz,
    # where dz is the total length of the shape along its z-axis. In other words, the rotational origin lies along the smallest 
    # local z-value rather than being at the translational origin, or the object's true center. 
    # 
    # This allows Shapes to rotate "at the joint" when chained together, much like segments of a limb. 
    #
    # In general, you should construct each component such that it is longest in its local z-direction: 
    # otherwise, rotations may not behave as expected.
    #
    # Please see Blackboard for an illustration of how this behavior works.

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        linkageLength = 0.5
        link1 = Cube(Point((0, 0, 0)), shaderProg, [2, 0.2, linkageLength], Ct.DARKORANGE1)
        link2 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, 0.3], Ct.BLACK)
        link3 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE3)
        link4 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE4)

        self.addChild(link1)
        link1.addChild(link2)
        link2.addChild(link3)
        link3.addChild(link4)

        self.componentList = [link1, link2, link3, link4]
        self.componentDict = {
            "link1": link1,
            "link2": link2,
            "link3": link3,
            "link4": link4
        }

        ##### TODO 4: Define creature's joint behavior
        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural ways
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.