# Import the abstract base class module
from abc import ABC, abstractmethod

# Define the EnemyFactory abstract base class
class EnemyFactory(ABC):
    
    # Define an abstract method that must be overridden by any subclass
    @abstractmethod
    def create_random_enemy(self):
        pass
