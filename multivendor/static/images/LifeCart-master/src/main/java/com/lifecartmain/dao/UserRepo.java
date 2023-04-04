package com.lifecartmain.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.lifecartmain.models.User;

public interface UserRepo extends JpaRepository<User, String>{
	@Query("select count(*) from User where username=?1 and password=?2")
	public int userExists(String username, String password);
	
	@Query("select isAdmin from User where username=?1")
	public boolean isAdmin(String username);
}
