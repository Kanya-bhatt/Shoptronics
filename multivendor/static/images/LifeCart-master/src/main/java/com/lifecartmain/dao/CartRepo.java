package com.lifecartmain.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.lifecartmain.models.Cart;

public interface CartRepo extends JpaRepository<Cart, Long>{
	@Query("SELECT e.id, e.prodID, e.quantity, e.username FROM Cart e where username=?1")
	List<Object[]> findAllByUsername(String username);
	
	@Transactional
	@Modifying
	@Query("DELETE FROM Cart WHERE username=?1")
	void delete(String username);
	
	@Modifying
	@Transactional
	@Query("DELETE FROM Cart WHERE id=?1")
	void deleteItem(long id);
}
