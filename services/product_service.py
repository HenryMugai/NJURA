"""
Product Service

Handles business logic related to
products and product pricing.
"""

from sqlalchemy import or_

from database.db import db
from models import Product, ProductPrice


class ProductService:
    """
    Product management service.
    """

    # =====================================================
    # Product Retrieval
    # =====================================================

    @staticmethod
    def get_all(company_id):
        """
        Returns all company products.
        """

        return Product.query.filter_by(
            company_id=company_id,
            is_deleted=False
        ).order_by(
            Product.name.asc()
        ).all()

    @staticmethod
    def get_by_id(product_id):
        """
        Returns a product by ID.
        """

        return Product.query.filter_by(
            id=product_id,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_code(company_id, product_code):
        """
        Returns a product by code.
        """

        return Product.query.filter_by(
            company_id=company_id,
            product_code=product_code,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_sku(company_id, sku):
        """
        Returns a product by SKU.
        """

        return Product.query.filter_by(
            company_id=company_id,
            sku=sku,
            is_deleted=False
        ).first()

    @staticmethod
    def get_by_category(company_id, category_id):
        """
        Returns products belonging
        to a category.
        """

        return Product.query.filter_by(
            company_id=company_id,
            product_category_id=category_id,
            is_deleted=False
        ).order_by(
            Product.name.asc()
        ).all()

    @staticmethod
    def search(company_id, search_term):
        """
        Searches products.
        """

        return Product.query.filter(

            Product.company_id == company_id,

            Product.is_deleted == False,

            or_(

                Product.name.ilike(
                    f"%{search_term}%"
                ),

                Product.product_code.ilike(
                    f"%{search_term}%"
                ),

                Product.sku.ilike(
                    f"%{search_term}%"
                ),

                Product.barcode.ilike(
                    f"%{search_term}%"
                ),

                Product.brand.ilike(
                    f"%{search_term}%"
                )

            )

        ).order_by(

            Product.name.asc()

        ).all()

    # =====================================================
    # Product Creation
    # =====================================================

    @staticmethod
    def create(data):
        """
        Creates a new product.
        """

        product = Product(

            company_id=data.get("company_id"),

            product_category_id=data.get(
                "product_category_id"
            ),

            name=data.get("name"),

            product_code=data.get(
                "product_code"
            ),

            sku=data.get("sku"),

            barcode=data.get("barcode"),

            description=data.get(
                "description"
            ),

            brand=data.get("brand"),

            unit_of_measure=data.get(
                "unit_of_measure",
                "Piece"
            ),

            pack_size=data.get(
                "pack_size"
            ),

            weight=data.get("weight"),

            image_url=data.get(
                "image_url"
            ),

            minimum_order_quantity=data.get(
                "minimum_order_quantity",
                1
            ),

            reorder_level=data.get(
                "reorder_level"
            ),

            tax_percentage=data.get(
                "tax_percentage",
                16.00
            ),

            notes=data.get("notes")

        )

        db.session.add(product)
        db.session.commit()

        return product

    # =====================================================
    # Product Update
    # =====================================================

    @staticmethod
    def update(product, data):
        """
        Updates a product.
        """

        for field, value in data.items():

            if hasattr(product, field):

                setattr(
                    product,
                    field,
                    value
                )

        db.session.commit()

        return product

    # =====================================================
    # Product Status
    # =====================================================

    @staticmethod
    def activate(product):

        product.product_status = "Active"
        product.is_active = True

        db.session.commit()

        return product

    @staticmethod
    def deactivate(product):

        product.product_status = "Inactive"
        product.is_active = False

        db.session.commit()

        return product

    @staticmethod
    def discontinue(product):

        product.product_status = "Discontinued"

        db.session.commit()

        return product

    @staticmethod
    def delete(product):

        product.soft_delete()

    # =====================================================
    # Product Pricing
    # =====================================================

    @staticmethod
    def add_price(data):
        """
        Creates a product price.
        """

        price = ProductPrice(

            company_id=data.get("company_id"),

            product_id=data.get("product_id"),

            selling_price=data.get(
                "selling_price"
            ),

            minimum_selling_price=data.get(
                "minimum_selling_price"
            ),

            maximum_selling_price=data.get(
                "maximum_selling_price"
            ),

            currency=data.get(
                "currency",
                "KES"
            ),

            effective_from=data.get(
                "effective_from"
            ),

            effective_to=data.get(
                "effective_to"
            ),

            notes=data.get("notes")

        )

        db.session.add(price)
        db.session.commit()

        return price

    @staticmethod
    def get_current_price(product_id):
        """
        Returns the active price for a product.
        """

        return ProductPrice.query.filter_by(

            product_id=product_id,

            price_status="Active",

            is_deleted=False

        ).order_by(

            ProductPrice.effective_from.desc()

        ).first()

    @staticmethod
    def price_history(product_id):
        """
        Returns pricing history.
        """

        return ProductPrice.query.filter_by(

            product_id=product_id,

            is_deleted=False

        ).order_by(

            ProductPrice.effective_from.desc()

        ).all()

    # =====================================================
    # Statistics
    # =====================================================

    @staticmethod
    def total(company_id):

        return Product.query.filter_by(

            company_id=company_id,

            is_deleted=False

        ).count()

    @staticmethod
    def active(company_id):

        return Product.query.filter_by(

            company_id=company_id,

            product_status="Active",

            is_deleted=False

        ).count()

    @staticmethod
    def discontinued(company_id):

        return Product.query.filter_by(

            company_id=company_id,

            product_status="Discontinued",

            is_deleted=False

        ).count()