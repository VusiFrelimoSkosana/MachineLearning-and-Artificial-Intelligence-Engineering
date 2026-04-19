DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
	std_id SERIAL PRIMARY KEY,
	Age INTEGER CHECK (age >=0 AND age<=120) NOT NULL,
	firstName VARCHAR(355) NOT NULL,
	surname VARCHAR(355) NOT NULL,
	phoneNumber VARCHAR(355) NOT NULL,
	idNumber VARCHAR(355) NOT NULL,
	country VARCHAR(355) NOT NULL,
	nativeLanguage VARCHAR(355) NOT NULL,
	race VARCHAR(355) NOT NULL
);

INSERT INTO customers (Age,firstName,surname,phoneNumber,idNumber,country,nativeLanguage,race) 
VALUES 
(21,'Vusi','Skosana','0655189268','9801205873082','RSA','isiNdebele','black'),
(23,'Thabo','Maseko','0725188268','0005105873082','RSA','isiZulu','black'),
(25,'Thuli','Masango','0735188068','0205105873082','RSA','isiNdebele','black');

SELECT * FROM customers;