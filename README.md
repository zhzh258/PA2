# PA2
### Name
Zhaozhan Huang
### BU Id
U03088498
### How to find my answers in the code ###
1. Search `### TODO 3 - ANSWER ###` for the start of my code for TODO 3
2. Search `### TODO 3 - ANSWER END ###` for the end of my code for TODO 3


## TODO 1
```python
myTransformation = scalingMat @ translationMat @ rotationMatU @ rotationMatV @ rotationMatW 
```

## TODO 2
`class TODO2_MyCat(Component)` is my model.

### There are 11 objects in my model:
- 1 * body: Cube()
- 4 * leg: Cube()
- 3 * tail: Cube()
- 1 * head: Sphere()
- 2 * ear: Cone()

### Model Structure
    - body 
        - leg1
        - leg2
        - leg3
        - leg4
        - tail1 - tail2 - tail3
        - head
            - ear1
            - ear2

### self.componentList
```python
self.componentList = [body, leg1, leg2, leg3, leg4, tail1, tail2, tail3, head]
```

### How did I Do The Rotation Correctly
- I added a parameter called `rotateBy=` to `class Cube()` in `Shape.py`. 
- This param can be {-3, -2, -1, 1, 2, 3}. For example, if `rotateBy=2`, it means that during the rotation, the current object should rotate by its local maximal `y`
- So `rotateBy=-3` is equivalent to the original `limb=True`
- I did this by applying a different `PrerotationMat` and `PostrotationMat` to every `rotateBy`


## TODO 3
See the code

## TODO 4
### Joint Behavior User Interface
- `1`: Select/Deselect body
- `2`: Select/Deselect leg1
- `3`: Select/Deselect leg2
- `4`: Select/Deselect leg3
- `5`: Select/Deselect leg4
- `6`: Select/Deselect tail1
- `7`: Select/Deselect tail2
- `8`: Select/Deselect tail3
- `9`: Select/Deselect head

### How did I limit the angles
I applied `Component.setRotateExtent()` to each component to set a lowerbound and a upperbound for their angle. 

## TODO 5
### Poses User Interface:
- `a`: raise tail (all 3 tails)
- `b`: droop tail (all 3 tails)
- `c`: run (front)
- `d`: run (back)
- `e`: raise hand and raise head

> The rotation angle by pressing `a` everytime is 1 degree. It can be set to 30 degree if needed.

### TODO 6
- I used two `Sphere` to respectively represent the sclera and the pupil.
- I used the `Sketch.unprojectCanvas(x, y, u)` to retrieve the coord of mouse (x,y,z) in 3D world coordinate. Then I do a projection to find the correct coord of `pupil.currentPos`