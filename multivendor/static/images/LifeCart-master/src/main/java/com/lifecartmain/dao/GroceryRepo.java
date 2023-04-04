package com.lifecartmain.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.lifecartmain.models.Grocery;
import com.lifecartmain.models.User;

public interface GroceryRepo extends JpaRepository<Grocery, Long>{
	@Transactional
	@Modifying
	@Query("update Grocery set quantity = ?1 where id = ?2")
	void update(int quantity, long prodID);
	
	@Query("select quantity from Grocery where id=?1")
	int getQuantity(long prodID);
	
	@Query("select sellPrice from Grocery where id = ?1")
	double getSellPrice(long prodID);
	
	@Transactional
	@Modifying
	@Query("update Grocery set quantity = ?1, name=?2, costPrice=?3, sellPrice=?4 where id = ?5")
	void update(int quantity, String name, double cp, double sp, long prodID);
}
