class Head:
    def __init__(self, eyes, nose, mouth, ears):
        self._eyes = eyes
        self._nose = nose
        self._mouth = mouth
        self._ears = ears
    
    @property
    def eyes(self):
        return self
    
    @eyes.setter
    def eyes(self, new):
        print("Can't be modified.")
    
    @property
    def nose(self):
        return self
    
    @nose.setter
    def nose(self, new):
        print("Can't be modified.")
    
    @property
    def mouth(self):
        return self
    
    @mouth.setter
    def mouth(self, new):
        print("Can't be modified.")
    
    @property
    def ears(self):
        return self
    
    @ears.setter
    def ears(self, new):
        print("Can't be modified.")

class Torso:
    def __init__(self, chest, abdomen):
        self._chest = chest
        self._abdomen = abdomen
    
    @property
    def chest(self):
        return self
    
    @chest.setter
    def chest(self, new):
        print("Can't be modified.")
    
    @property
    def abdomen(self):
        return self
    
    @abdomen.setter
    def abdomen(self, new):
        print("Can't be modified.")

class Arm:
    def __init__(self, shoulder, bicep, elbow, wrist, hand):
        self._shoulder = shoulder
        self._bicep = bicep
        self._elbow = elbow
        self._wrist = wrist
        self.hand = hand
    
    @property
    def shoulder(self):
        return self
    
    @shoulder.setter
    def shoulder(self, new):
        print("Can't be modified.")
    
    @property
    def bicep(self):
        return self
    
    @bicep.setter
    def bicep(self, new):
        print("Can't be modified.")
    
    @property
    def elbow(self):
        return self
    
    @elbow.setter
    def elbow(self, new):
        print("Can't be modified.")
    
    @property
    def wrist(self):
        return self
    
    @wrist.setter
    def wrist(self, new):
        print("Can't be modified.")
    

class Hand:
    def __init__(self, palm, fingers):
        self._palm = palm
        self._fingers = fingers
    
    @property
    def palm(self):
        return self
    
    @palm.setter
    def palm(self, new):
        print("Can't be modified.")
    
    @property
    def fingers(self):
        return self
    
    @fingers.setter
    def fingers(self, new):
        print("Can't be modified.")

class Leg:
    def __init__(self, waist, thigh, knee, shin, ankle, foot):
        self._waist = waist
        self._thigh = thigh
        self._knee = knee
        self._shin = shin
        self._ankle = ankle
        self._foot = foot
    
    @property
    def waist(self):
        return self
    
    @waist.setter
    def waist(self, new):
        print("Can't be modified.")
    
    @property
    def thigh(self):
        return self
    
    @thigh.setter
    def thigh(self, new):
        print("Can't be modified.")
    
    @property
    def knee(self):
        return self
    
    @knee.setter
    def knee(self, new):
        print("Can't be modified.")
    
    @property
    def shin(self):
        return self
    
    @shin.setter
    def shin(self, new):
        print("Can't be modified.")
    
    @property
    def ankle(self):
        return self
    
    @ankle.setter
    def ankle(self, new):
        print("can't be modified")

class Foot:
    def __init__(self, heel, sole, toe):
        self._heel = heel
        self._sole = sole
        self._toe = toe
    
    @property
    def heel(self):
        return self
    
    @heel.setter
    def heel(self, new):
        print("Can't be modified.")
    
    @property
    def sole(self):
        return self
    
    @sole.setter
    def sole(self, new):
        print("Can't be modified.")
    
    @property
    def toe(self):
        return self
    
    @toe.setter
    def toe(self, new):
        print("can't be modified")

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

normal_right_leg = Leg('Normal Waist', 'Normal Thigh', 'Normal Knee', 'Normal Shin', 'Normal Ankle', normal_right_foot)
normal_left_leg = Leg('Normal Waist', 'Normal Thigh', 'Normal Knee', 'Normal Shin', 'Normal Ankle', normal_left_foot)
small_right_leg = Leg('Small Waist', 'Small Thigh', 'Small Knee', 'Small Shin', 'Small Ankle', small_right_foot)
small_left_leg = Leg('Small Waist', 'Small Thigh', 'Small Knee', 'Small Shin', 'Small Ankle', small_left_foot)
big_right_leg = Leg('Big Waist', 'Big Thigh', 'Big Knee', 'Big Shin', 'Big Ankle', big_right_foot)
big_left_leg = Leg('Big Waist', 'Big Thigh', 'Big Knee', 'Big Shin', 'Big Ankle', big_left_foot)

normal_right_hand = Hand('Normal Palm', 'Normal right Fingers')
normal_left_hand = Hand('Normal Palm', 'Normal left Fingers')
small_right_hand = Hand('Small Palm', 'Small right Fingers')
small_left_hand = Hand('Small Palm', 'Small left Fingers')
big_right_hand = Hand('Big Palm', 'Big right Fingers')
big_left_hand = Hand('Big Palm', 'Big left Fingers')

normal_right_arm = Arm('Normal Shoulder', 'Normal Bicep', 'Normal Elbow', 'Normal Wrist', normal_right_hand)
normal_left_arm = Arm('Normal Shoulder', 'Normal Bicep', 'Normal Elbow', 'Normal Wrist', normal_left_hand)
small_right_arm = Arm('Small Shoulder', 'Small Bicep', 'Small Elbow', 'Small Wrist', small_right_hand)
small_left_arm = Arm('Small Shoulder', 'Small Bicep', 'Small Elbow', 'Small Wrist', small_left_hand)
big_right_arm = Arm('Big Shoulder', 'Big Bicep', 'Big Elbow', 'Big Wrist', big_right_hand)
big_left_arm = Arm('Big Shoulder', 'Big Bicep', 'Big Elbow', 'Big Wrist', big_left_hand)

normal_head = Head('Medium Eyes', 'Medium Nose', 'Medium Mouth', 'Medium ears')
small_head = Head('Small_eyes', 'Small Nose', 'Small Mouth', 'Small Ears')
big_head = Head('Big_eyes', 'Big Nose', 'Big Mouth', 'Big Ears')

normal_torso = Torso('Normal Chest', 'Normal Abs')
small_torso = Torso('Small Chest', 'Small Abs')
big_torso = Torso('Big Chest', 'Big Abs')

normal_human_1 = Human(normal_head, normal_torso, normal_right_arm, normal_left_arm, normal_right_leg, normal_left_leg)
small_human_1 = Human(small_head, small_torso, small_right_arm, small_left_arm, small_right_leg, small_left_leg)
big_human_1 = Human(big_head, big_torso, big_right_arm, big_left_arm, big_right_leg, big_left_leg)

franky_1 = Human(big_head, small_torso, normal_right_arm, big_left_arm, normal_right_leg, big_left_leg)

print(f"{franky_1.head.__dict__}")
print(f"{franky_1.torso.__dict__}")
big_human_1.head.ears = 'Orion'
print(f"{franky_1.head.__dict__}")