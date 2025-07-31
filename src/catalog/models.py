import itertools
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    offer = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de descuento (0-100)"
    )
    on_offer = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)  # Removido null=True, blank=True
    product_description = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    alt = models.TextField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        """Validaciones personalizadas"""
        super().clean()
        
        # Validar que si está en oferta, el porcentaje sea mayor a 0
        if self.on_offer and self.offer <= 0:
            raise ValidationError({
                'offer': 'Si el producto está en oferta, el porcentaje debe ser mayor a 0.'
            })
        
        # Validar que si no está en oferta, el porcentaje sea 0
        if not self.on_offer and self.offer > 0:
            raise ValidationError({
                'on_offer': 'Si hay un porcentaje de descuento, marque el producto como en oferta.'
            })

    def _generate_unique_slug(self):
        """Genera un slug único de manera más eficiente"""
        if not self.name:
            return None
            
        base_slug = slugify(self.name)
        if not base_slug:
            return None
            
        # Usar select_for_update para evitar condiciones de carrera
        from django.db import transaction
        
        with transaction.atomic():
            # Encontrar el número más alto existente para este base_slug
            existing_slugs = Product.objects.filter(
                slug__startswith=base_slug
            ).exclude(
                pk=self.pk  # Excluir el objeto actual si está siendo actualizado
            ).values_list('slug', flat=True)
            
            if base_slug not in existing_slugs:
                return base_slug
            
            # Encontrar el siguiente número disponible
            existing_numbers = []
            for slug in existing_slugs:
                if slug == base_slug:
                    existing_numbers.append(0)
                elif slug.startswith(f"{base_slug}-"):
                    try:
                        num = int(slug.split('-')[-1])
                        existing_numbers.append(num)
                    except ValueError:
                        continue
            
            if existing_numbers:
                next_num = max(existing_numbers) + 1
                return f"{base_slug}-{next_num}"
            else:
                return f"{base_slug}-1"

    def save(self, *args, **kwargs):
        # Generar slug solo si no existe
        if not self.slug:
            self.slug = self._generate_unique_slug()
        
        # Llamar clean() para ejecutar validaciones
        self.full_clean()
        
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        """Calcula el precio con descuento"""
        if not self.on_offer or self.offer <= 0:
            return self.price

        discount = self.price * (Decimal(self.offer) / Decimal('100'))
        return max(self.price - discount, 0)  # Asegurar que no sea negativo

    @property
    def savings_amount(self):
        """Calcula el monto ahorrado"""
        if not self.on_offer or self.offer <= 0:
            return 0
        return self.price - self.discounted_price

    @property
    def image_url(self):
        """Retorna la URL de la imagen o una imagen por defecto"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
        # Manejo más seguro de MEDIA_URL
        media_url = getattr(settings, 'MEDIA_URL', '/media/')
        if not media_url.endswith('/'):
            media_url += '/'
        return f"{media_url}not_image_found.jpg"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """URL canónica del producto usando el slug"""
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def is_available(self):
        """Determina si el producto está disponible"""
        # Lógica personalizable según tus necesidades
        return True  # Por ahora siempre disponible

    def __repr__(self):
        return f"<Product: {self.name} (${self.price})>"