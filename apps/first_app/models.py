from django.db import models
# Create your models here.
class PizzaManager(models.Manager):
    def validate_pizza(self, postData):
        # Original validation logic applies
        # Name must be present and at least 2 characters long
        # Description must be present and at least 8 characters
        # price must be present
        print(postData)
        # 2. create errors dictionary
        errors = {}
        # 3. validate post information
        if len(postData['name']) == 0:
            errors['name'] = "Name must be present"
        elif len(postData['name'])<2:
            errors['name'] = "Name must be at least 2 characters long"

        if len(postData['price']) == 0:
            errors['price'] = "Price must be present"
        
        if len(postData['description']) == 0:
            errors['description'] = "Description is required"
        elif len(postData['description']) < 8:
            errors['description'] = "Description must be at least 8 characters long"
        print(errors)
        # 4. If errors exist, package them in a dictionary
        if len(errors):
            result = {
                'errors': errors
            }
            return result
        # 5. If no errors, create the pizza here and add to the dictionary
        else:
            pizza = self.create(name = postData['name'], description = postData['description'], price = postData['price'])
            result = {
                'the_pizza': pizza
            }
            return result

class Pizza(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PizzaManager()