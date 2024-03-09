=============================
Core Web Application for Sales and Cost Analysis
=============================

A Django-based web application designed to empower employees with real-time access to sales and cost metrics, enhanced by AI-driven analytics for insightful decision-making.

Features
========

1. **Dashboard**: A visualization interface displaying key performance indicators (KPIs) for immediate insight into sales and cost metrics.

2. **Team Board**: An interactive platform for employees to collaborate on team tasks, enhancing productivity and teamwork.

3. **AI Analytics**: Leveraging the OpenAI API, this feature generates detailed analytical reports on sales, costs, and market conditions, providing a competitive edge in strategic planning.

Installation
============

To get started with the Core Web Application, ensure you have Python 3.12 or higher installed. Then, follow these steps:

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/moebuschris/core-web-application.git
   cd core-web-application

2. Install the project dependencies using Poetry:

.. code-block:: bash

   poetry install

3. Initialize the database (adjust the command according to your DB setup):

.. code-block:: bash

   python manage.py migrate

4. Run the development server:

.. code-block:: bash

   python manage.py runserver

Usage
=====

After installation, you can access the web application by navigating to `http://localhost:8000` in your web browser. Here's how to get started with each feature:

- **Dashboard**: Login with your employee credentials to view the latest KPIs on the dashboard.
- **Team Board**: Access the Team Board from the main menu to collaborate with your colleagues.
- **AI Analytics**: Generate sales and cost reports through the 'Analytics' section in the application.

Contribution
============

We welcome contributions to the Core Web Application project. Please refer to the `CONTRIBUTING.rst` file for more details on how to submit issues, propose changes, and contribute to the codebase.

License
=======

MIT License

Authors
=======

- cGray

Acknowledgments
===============

- Thanks to OpenAI for providing the API used in the AI Analytics feature.
