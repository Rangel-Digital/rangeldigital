app_name = "rangeldigital"
app_title = "Rangel Digital"
app_publisher = "Jeremy Rangel"
app_description = "Addons for rangeldigital"
app_email = "jeremy.rangel@rangeldigital.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rangeldigital/css/rangeldigital.css"
# app_include_js = "/assets/rangeldigital/js/rangeldigital.js"

# include js, css files in header of web template
# web_include_css = "/assets/rangeldigital/css/rangeldigital.css"
# web_include_js = "/assets/rangeldigital/js/rangeldigital.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rangeldigital/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "rangeldigital/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "rangeldigital.utils.jinja_methods",
# 	"filters": "rangeldigital.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rangeldigital.install.before_install"
# after_install = "rangeldigital.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rangeldigital.uninstall.before_uninstall"
# after_uninstall = "rangeldigital.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "rangeldigital.utils.before_app_install"
# after_app_install = "rangeldigital.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "rangeldigital.utils.before_app_uninstall"
# after_app_uninstall = "rangeldigital.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rangeldigital.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rangeldigital.tasks.all"
# 	],
# 	"daily": [
# 		"rangeldigital.tasks.daily"
# 	],
# 	"hourly": [
# 		"rangeldigital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rangeldigital.tasks.weekly"
# 	],
# 	"monthly": [
# 		"rangeldigital.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "rangeldigital.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rangeldigital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rangeldigital.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["rangeldigital.utils.before_request"]
# after_request = ["rangeldigital.utils.after_request"]

# Job Events
# ----------
# before_job = ["rangeldigital.utils.before_job"]
# after_job = ["rangeldigital.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"rangeldigital.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

web_include_css = ["/assets/rangeldigital/css/style.css",
                    "/assets/rangeldigital/css/meanmenu.css",
                   "/assets/rangeldigital/css/responsive.css",
                   "/assets/rangeldigital/css/owl.carousel.min.css",
                   "/assets/rangeldigital/css/responsive.css",
                   "/assets/rangeldigital/css/swiper-bundle.min.css",
                   "/assets/rangeldigital/css/magnific-popup.css",
                   "/assets/rangeldigital/css/animate.css",
                   "/assets/rangeldigital/css/custom.css",
                   ]

web_include_js = [
                    
                   


                    "/assets/rangeldigital/js/script.js",

                        "/assets/rangeldigital/js/jquery-3.7.1.min.js",
                    "/assets/rangeldigital/js/bootstrap.min.js",
                    "/assets/rangeldigital/js/meanmenu.js",
                    "/assets/rangeldigital/js/swiper-bundle.min.js",
                    "/assets/rangeldigital/js/jquery.counterup.min.js",
                    "/assets/rangeldigital/js/wow.min.js",
                    "/assets/rangeldigital/js/magnific-popup.min.js",
                     "/assets/rangeldigital/js/pace.min.js",
                    "/assets/rangeldigital/js/nice-select.min.js",
                    "/assets/rangeldigital/js/isotope.pkgd.min.js",
                    "/assets/rangeldigital/js/jquery.waypoints.js",
                     "/assets/rangeldigital/js/script.js",
                     "/assets/rangeldigital/js/simple-notify.min.js?v2.01",
                     "/assets/rangeldigital/js/helpers.js?v2.01"
                    ]


app_include_css = [
    "/assets/rangeldigital/css/backend.css"

]

app_includes_js =[
    "/assets/rangeldigital/js/backend.js"
]