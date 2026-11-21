class Head:
    def __init__(self, eyes, nose, mouth, ears):
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
        self.ears = ears

class Torso:
    def __init__(self, head, chest, abdomen, right_arm, left_arm):
        self.head = head
        self.chest = chest
        self.abdomen = abdomen
        self.right_arm = right_arm
        self.left_arm = left_arm

class Arm:
    def __init__(self, shoulder, bicep, elbow, wrist):
        self.shoulder = shoulder
        self.bicep = bicep
        self.elbow = elbow
        self.wrist = wrist

class RightArm(Arm):
    def __init__(self, shoulder, bicep, elbow, wrist, right_hand):
        super().__init__(shoulder, bicep, elbow, wrist)
        self.right_hand = right_hand

class LeftArm(Arm):
    def __init__(self, shoulder, bicep, elbow, wrist, left_hand):
        super().__init__(shoulder, bicep, elbow, wrist)
        self.left_hand = left_hand

class Hand:
    def __init__(self, palm):
        self.palm = palm

class RightHand(Hand):
    def __init__(self, palm, right_fingers):
        super().__init__(palm)
        self.right_fingers = right_fingers

class LeftHand(Hand):
    def __init__(self, palm, left_fingers):
        super().__init__(palm)
        self.right_fingers = left_fingers

class Leg:
    def __init__(self, waist, thigh, knee, shin, ankle):
        self.waist = waist
        self.thigh = thigh
        self.knee = knee
        self.shin = shin
        self.ankle = ankle

class RightLeg(Leg):
    def __init__(self, waist, thigh, knee, shin, ankle, right_foot):
        super().__init__(waist, thigh, knee, shin, ankle)
        self.right_foot = right_foot

class LeftLeg(Leg):
    def __init__(self, waist, thigh, knee, shin, ankle, left_foot):
        super().__init__(waist, thigh, knee, shin, ankle)
        self.lef_foot = left_foot

class Foot:
    def __init__(self, heel, sole, toe):
        self.heel = heel
        self.sole = sole
        self.toe = toe

class Human:
    def __init__(self, head, torso, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
    

normal_right_foot = Foot('Normal Heel', 'Normal Sole', 'Normal Toes')
normal_left_foot = Foot('Normal Heel', 'Normal Sole', 'Normal Toes')
small_right_foot = Foot('Small Heel', 'Small Sole', 'Small Toes')
small_left_foot = Foot('Small Heel', 'Small Sole', 'Small Toes')
big_right_foot = Foot('Big Heel', 'Big Sole', 'Big Toes')
big_left_foot = Foot('Big Heel', 'Big Sole', 'Big Toes')

normal_right_leg = RightLeg('Normal Waist', 'Normal Thigh', 'Normal Knee', 'Normal Shin', 'Normal Ankle', normal_right_foot)
normal_left_leg = LeftLeg('Normal Waist', 'Normal Thigh', 'Normal Knee', 'Normal Shin', 'Normal Ankle', normal_left_foot)
small_right_leg = RightLeg('Small Waist', 'Small Thigh', 'Small Knee', 'Small Shin', 'Small Ankle', small_right_foot)
small_left_leg = LeftLeg('Small Waist', 'Small Thigh', 'Small Knee', 'Small Shin', 'Small Ankle', small_left_foot)
big_right_leg = RightLeg('Big Waist', 'Big Thigh', 'Big Knee', 'Big Shin', 'Big Ankle', big_right_foot)
big_left_leg = LeftLeg('Big Waist', 'Big Thigh', 'Big Knee', 'Big Shin', 'Big Ankle', big_left_foot)

normal_right_hand = RightHand('Normal Palm', 'Normal right Fingers')
normal_left_hand = LeftHand('Normal Palm', 'Normal left Fingers')
small_right_hand = RightHand('Small Palm', 'Small right Fingers')
small_left_hand = LeftHand('Small Palm', 'Small left Fingers')
big_right_hand = RightHand('Big Palm', 'Big right Fingers')
big_left_hand = LeftHand('Big Palm', 'Big left Fingers')

normal_right_arm = RightArm('Normal Shoulder', 'Normal Bicep', 'Normal Elbow', 'Normal Wrist', normal_right_hand)
normal_left_arm = LeftArm('Normal Shoulder', 'Normal Bicep', 'Normal Elbow', 'Normal Wrist', normal_left_hand)
small_right_arm = RightArm('Small Shoulder', 'Small Bicep', 'Small Elbow', 'Small Wrist', small_right_hand)
small_left_arm = LeftArm('Small Shoulder', 'Small Bicep', 'Small Elbow', 'Small Wrist', small_left_hand)
big_right_arm = RightArm('Big Shoulder', 'Big Bicep', 'Big Elbow', 'Big Wrist', big_right_hand)
big_left_arm = LeftArm('Big Shoulder', 'Big Bicep', 'Big Elbow', 'Big Wrist', big_left_hand)

normal_head = Head('Medium Eyes', 'Medium Nose', 'Medium Mouth', 'Medium ears')
small_head = Head('Small_eyes', 'Small Nose', 'Small Mouth', 'Small Ears')
big_head = Head('Big_eyes', 'Big Nose', 'Big Mouth', 'Big Ears')

normal_torso = Torso(normal_head, 'Normal Chest', 'Normal Abs', normal_right_arm, normal_left_arm)
small_torso = Torso(small_head, 'Small Chest', 'Small Abs', small_right_arm, small_left_arm)
big_torso = Torso(big_head, 'Big Chest', 'Big Abs', big_right_arm, big_left_arm)

normal_human_1 = Human(normal_head, normal_torso, normal_right_arm, normal_left_arm, normal_right_leg, normal_left_leg)
small_human_1 = Human(small_head, small_torso, small_right_arm, small_left_arm, small_right_leg, small_left_leg)
big_human_1 = Human(big_head, big_torso, big_right_arm, big_left_arm, big_right_leg, big_left_leg)
franky_1 = Human(big_head, small_torso, normal_right_arm, big_left_arm, normal_right_leg, big_left_leg)