NJURA/
│
├── venv/
│
├── migrations/
│
├── instance/
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── seed.py
│
├── blueprints/
│   │
│   ├── auth/
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── __init__.py
│   │
│   ├── public/
│   │   ├── routes.py
│   │   └── __init__.py
│   │
│   ├── super_admin/
│   │   ├── routes.py
│   │   ├── company.py
│   │   ├── subscriptions.py
│   │   ├── users.py
│   │   ├── audit.py
│   │   └── __init__.py
│   │
│   ├── company_admin/
│   │   ├── routes.py
│   │   ├── dashboard.py
│   │   ├── products.py
│   │   ├── distributors.py
│   │   ├── territories.py
│   │   ├── routes_management.py
│   │   ├── reports.py
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   ├── distributor/
│   │   ├── routes.py
│   │   ├── dashboard.py
│   │   ├── fsr.py
│   │   ├── outlets.py
│   │   ├── orders.py
│   │   ├── visits.py
│   │   ├── deliveries.py
│   │   ├── reports.py
│   │   └── __init__.py
│   │
│   ├── fsr/
│   │   ├── routes.py
│   │   ├── dashboard.py
│   │   ├── outlets.py
│   │   ├── visits.py
│   │   ├── orders.py
│   │   ├── route_plan.py
│   │   ├── profile.py
│   │   └── __init__.py
│   │
│   ├── api/
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── outlets.py
│   │   ├── visits.py
│   │   ├── orders.py
│   │   ├── distributors.py
│   │   ├── reports.py
│   │   └── __init__.py
│   │
│   └── errors/
│       ├── handlers.py
│       └── __init__.py
│
├── middleware/
│   ├── auth.py
│   ├── company_context.py
│   ├── permissions.py
│   ├── subscription.py
│   └── roles.py
│
├── services/
│   ├── auth_service.py
│   ├── company_service.py
│   ├── distributor_service.py
│   ├── product_service.py
│   ├── outlet_service.py
│   ├── visit_service.py
│   ├── order_service.py
│   ├── report_service.py
│   ├── dashboard_service.py
│   ├── gps_service.py
│   ├── notification_service.py
│   └── analytics_service.py
│
├── models/
│   ├── base.py
│   ├── company.py
│   ├── subscription.py
│   ├── role.py
│   ├── permission.py
│   ├── role_permission.py
│   ├── user.py
│   ├── territory.py
│   ├── route.py
│   ├── distributor.py
│   ├── distributor_user.py
│   ├── fsr.py
│   ├── outlet.py
│   ├── outlet_category.py
│   ├── product_category.py
│   ├── product.py
│   ├── product_price.py
│   ├── visit.py
│   ├── visit_note.py
│   ├── order.py
│   ├── order_item.py
│   ├── delivery.py
│   ├── dashboard.py
│   ├── notification.py
│   ├── audit_log.py
│   └── __init__.py
│
├── utils/
│   ├── constants.py
│   ├── helpers.py
│   ├── validators.py
│   ├── permissions.py
│   ├── geo.py
│   ├── pagination.py
│   └── responses.py
│
├── static/
│   │
│   ├── css/
│   │   ├── auth/
│   │   ├── public/
│   │   ├── super_admin/
│   │   ├── company_admin/
│   │   ├── distributor/
│   │   ├── fsr/
│   │   └── shared/
│   │
│   ├── js/
│   │   ├── auth/
│   │   ├── company_admin/
│   │   ├── distributor/
│   │   ├── fsr/
│   │   └── shared/
│   │
│   ├── img/
│   │
│   ├── icons/
│   │
│   └── uploads/
│
├── templates/
│   │
│   ├── layouts/
│   │   ├── base.html
│   │   ├── auth_base.html
│   │   ├── public_base.html
│   │   ├── super_admin_base.html
│   │   ├── company_admin_base.html
│   │   ├── distributor_base.html
│   │   └── fsr_base.html
│   │
│   ├── auth/
│   │   ├── login.html
│   │   ├── forgot_password.html
│   │   ├── reset_password.html
│   │   └── change_password.html
│   │
│   ├── public/
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── pricing.html
│   │   ├── contact.html
│   │   └── features.html
│   │
│   ├── super_admin/
│   │   ├── dashboard.html
│   │   ├── companies.html
│   │   ├── create_company.html
│   │   ├── subscriptions.html
│   │   ├── users.html
│   │   ├── audit_logs.html
│   │   ├── settings.html
│   │   └── profile.html
│   │
│   ├── company_admin/
│   │   ├── dashboard.html
│   │   ├── products.html
│   │   ├── create_product.html
│   │   ├── distributors.html
│   │   ├── territories.html
│   │   ├── routes.html
│   │   ├── reports.html
│   │   ├── analytics.html
│   │   ├── settings.html
│   │   └── profile.html
│   │
│   ├── distributor/
│   │   ├── dashboard.html
│   │   ├── notifications.html
│   │   ├── outlets.html
│   │   ├── orders.html
│   │   ├── order_details.html
│   │   ├── deliveries.html
│   │   ├── reports.html
│   │   ├── settings.html
│   │   └── profile.html

│   │
│   ├── fsr/
│   │   ├── dashboard.html
│   │   ├── today_route.html
│   │   ├── outlets.html
│   │   ├── outlet_details.html
│   │   ├── visit.html
│   │   ├── orders.html
│   │   ├── create_order.html
│   │   ├── profile.html
│   │   └── history.html
│   │
│   └── errors/
│       ├── 403.html
│       ├── 404.html
│       └── 500.html
│
├── config.py
├── app.py
├── run.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md