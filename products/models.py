from django.db import models


#table CategoryModel
#Column category_name
#Column2 created_at


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Categoty'
        verbose_name_plural = 'Categories'

class ProductModel(models.Model):
    products_name = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    descriptions = models.TextField()
    image = models.FileField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.products_name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

#DOMASHKA

class NewsCategoryModel(models.Model):
    category_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'NewsCategory'
        verbose_name_plural = 'NewsCategories'

class NewsModel(models.Model):
    title_name = models.CharField(max_length=90)
    title_text = models.TextField()
    category = models.ForeignKey(NewsCategoryModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title_name}"

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"

class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    user_product_quantity = models.IntegerField(default=0)
    user_add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user_product})"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

def sum(self):
    return self.quantity * self.products_price
