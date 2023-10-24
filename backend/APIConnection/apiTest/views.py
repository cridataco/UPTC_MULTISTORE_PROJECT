from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import ProductTest, Inventory
import json

inventory = Inventory()


class ProductAPI:

    @staticmethod
    @csrf_exempt
    def receive_and_create_product(request):
        if request.method == 'POST':
            product_data = json.loads(request.body)

            # Descompone el objeto JSON en sus atributos
            product_id = int(product_data.get('prod_id'))
            product_name = product_data.get('prod_name')
            product_reference = product_data.get('prod_ref')

            date_str = product_data.get('release_date')
            release_date = datetime.strptime(date_str, "%Y-%m-%d")

            product_description = product_data.get('prod_description')
            product_keywords = product_data.get('keywords')
            product_ratings = product_data.get('ratings')

            product = ProductTest(product_id, product_name, product_reference, release_date, product_description)
            product._prod_key_words = product_keywords
            product._prod_ratings = product_ratings

            inventory.add_product(product)

            print(product.__str__())

            return JsonResponse({'message': 'SIUUUUUUUUUU!'})

    @staticmethod
    @csrf_exempt
    def get_product(request, prod_id):
        if request.method == 'GET':
            # Busca el producto en la lista de productos del inventario
            product = inventory.get_product(prod_id)

            if product is not None:
                # Devuelve el producto como JSON
                return JsonResponse(product.__dict__, safe=False)
            else:
                return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    @staticmethod
    @csrf_exempt
    def update_product(request, prod_id):
        if request.method == 'PUT':
            # Carga los datos del producto desde el cuerpo de la solicitud
            product_data = json.loads(request.body)

            # Crea un nuevo objeto ProductTest con los datos actualizados
            new_product = ProductTest(
                prod_id=int(product_data.get('prod_id')),
                prod_name=product_data.get('prod_name'),
                prod_ref=product_data.get('prod_ref'),
                release_date=datetime.strptime(product_data.get('release_date'), "%Y-%m-%d"),
                prod_description=product_data.get('prod_description')
            )
            new_product._prod_key_words = product_data.get('keywords')
            new_product._prod_ratings = product_data.get('ratings')

            # Intenta actualizar el producto en el inventario
            if inventory.update_product(prod_id, new_product):
                return JsonResponse({'message': 'Producto actualizado con éxito'})
            else:
                return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    @staticmethod
    @csrf_exempt
    def delete_product(request, prod_id):
        if request.method == 'DELETE':
            print(len(inventory.products))
            # Intenta eliminar el producto del inventario
            if inventory.delete_product(prod_id):
                print(len(inventory.products))
                return JsonResponse({'message': 'Producto eliminado con éxito'})
            else:
                return JsonResponse({'error': 'Producto no encontrado'}, status=404)
