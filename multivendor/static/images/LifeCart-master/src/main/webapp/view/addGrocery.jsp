<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="ISO-8859-1">
		<title>Add Grocery</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<!-- Bootstrap CSS -->
		<link rel="stylesheet"
			href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"
			integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
			crossorigin="anonymous">
	</head>
	<body class="bg-info text-center">
		<div class="container-fluid bg-dark">
			<header class="d-flex flex-wrap justify-content-center py-3 mb-4">
				<a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-light text-decoration-none navbar-brand">
					LifeCart
				</a>
				<ul class="nav nav-pills">
					<li class="nav-item"><a href="/" class="nav-link">Home</a></li>
					<li class="nav-item"><a href="/addGroceries" class="nav-link active" aria-current="page">Add Groceries</a></li>
					<li class="nav-item"><a href="/groceries" class="nav-link">Back to Groceries</a></li>
					<li class="nav-item"><a href="/logout" class="nav-link">Logout</a></li>
				</ul>
			</header>
		</div>
		<div class="p-5 m-4 border border-dark">
			<h1 class="heading">Add Grocery</h1>
			<form:form method="post" action="/setGroceries" modelAttribute="Grocery">
				<div class="p-3">
					Name :
					<form:input path="name" type="text" name="name" />
				</div>
				<br>
				<div class="p-3">
					Cost Price :
					<form:input path="costPrice" type="text" name="costPrice" />
				</div>
				<br>
				<div class="p-3">
					Sell Price :
					<form:input path="sellPrice" type="text" name="sellPrice" />
				</div>
				<br>
				<div class="p-3">
					Quantity :
					<form:input path="quantity" type="text" name="quantity" />
				</div>
				<br>
				<input class="btn btn-dark text-light" type="submit" value="Submit">
			</form:form>
		</div>
	</body>
</html>