package com.lifecartmain.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import org.springframework.data.jpa.repository.Query;
import com.lifecartmain.models.Orders;

public interface OrderRepo extends JpaRepository<Orders, Long>{
	@Query("Select o.id,o.prodID,o.quantity,o.price,o.orderDate from Orders o where username = ?1 order by orderDate desc")
	List<Object[]> findAllByUsername(String username);
}
