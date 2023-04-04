<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="ISO-8859-1">
		<title>Home Page</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<!-- Bootstrap CSS -->
		<link rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"
			integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
			crossorigin="anonymous">
	</head>
	<body class="bg-info">
		<div class="container-fluid bg-dark">
			<header class="d-flex flex-wrap justify-content-center py-3 mb-4">
				<a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-light text-decoration-none navbar-brand">
					LifeCart
				</a>
				<ul class="nav nav-pills">
					<li class="nav-item"><a href="/" class="nav-link active" aria-current="page">Home</a></li>
					<c:if test="${username eq null}">
						<li class="nav-item"><a href="/login" class="nav-link">Login</a></li>
						<li class="nav-item"><a href="/register" class="nav-link">Register</a></li>
					</c:if>
					<c:if test="${username ne null}">
						<li class="nav-item"><a href="/logout" class="nav-link">Logout</a></li>
						<li class="nav-item"><a href="/groceries" class="nav-link">Buy Groceries</a></li>
					</c:if>
				</ul>
			</header>
		</div>
		<div class="container align-items-center p-3">
			<c:if test="${username ne null}">
				You are logged in as: ${username}
			</c:if>
			<c:if test="${username eq null}">
				You are not logged in.
			</c:if>
		</div>
		<div class="container align-items-center border-top p-3">
		<c:if test="${username ne null}">
				<a class="text-light" href="checkout" style="display:block;">My orders</a>
				</c:if>
			<c:if test="${username ne null and isAdmin eq true}">
				Admin controls :
				<a class="px-2 text-light" href="viewOrders">View Orders</a>
				<a class="px-2 text-light" href="viewInventory">View/Update Inventory</a>
				<a class="px-2 text-light" href="viewCustomers">View Customers</a>
				<a class="text-light" href="addGroceries">Add Groceries</a>
			</c:if>
		</div>
	</body>
</html>