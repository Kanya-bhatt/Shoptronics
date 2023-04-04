package com.lifecartmain.models;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Cart {
	@Id
	@GeneratedValue
	long id;
	String username;
	long prodID;
	int quantity;
	public Cart() {
		super();
		this.username = null;
		this.prodID = -1;
		this.quantity = 0;
	}
	public Cart(String username, long prodID, int quantity) {
		super();
		this.username = username;
		this.prodID = prodID;
		this.quantity = quantity;
	}
	public Cart(long id, long prodID, int quantity, String username) {
		super();
		this.id = id;
		this.username = username;
		this.prodID = prodID;
		this.quantity = quantity;
	}
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public long getProdID() {
		return prodID;
	}
	public void setProdID(long prodID) {
		this.prodID = prodID;
	}
	public int getQuantity() {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
}
