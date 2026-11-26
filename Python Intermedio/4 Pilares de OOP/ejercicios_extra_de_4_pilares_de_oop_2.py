from abc import ABC, abstractmethod

class User(ABC):
    actions = [
                'Create',
                'Read',
                'Update',
                'Delete'
            ]
    
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        self.role = self.get_role()
    
    @abstractmethod
    def get_role(self):
        if type(self).__name__ == 'AdminUser':
            return 'admin'
        elif type(self).__name__ == 'RegularUser':
            return 'regular'
        else:
            return False
    
    @abstractmethod
    def has_permission(self, permission):
        if permission not in User.actions:
            print(f"Invalid request. {permission} in not a valid action.")
            return False
        else:
            if permission.lower() != 'read':
                return False
            else:
                return True

class AdminUser(User):
    def __init__(self, user_name, user_password):
        super().__init__(user_name, user_password)
    
    def get_role(self):
        return super().get_role()
    
    def has_permission(self, permission):
        if permission not in User.actions:
            print(f"Invalid request. {permission} in not a valid action.")
            return False
        else:
            return True

class RegularUser(User):
    def __init__(self, user_name, user_password):
        super().__init__(user_name, user_password)
    
    def get_role(self):
        return super().get_role()
    
    def has_permission(self, permission):
        return super().has_permission(permission)

user1 = AdminUser(
    user_name = 'martin',
    user_password = '123',
)

user2 = RegularUser(
    user_name = 'bob',
    user_password = '123'
)

print(user1.__dict__)
print(user2.__dict__)

print(user1.has_permission('Create'))
print(user1.has_permission('Read'))
print(user1.has_permission('Update'))
print(user1.has_permission('Delete'))
print(user1.has_permission('Move'))

print(user2.has_permission('Create'))
print(user2.has_permission('Read'))
print(user2.has_permission('Update'))
print(user2.has_permission('Delete'))
print(user2.has_permission('Move'))