use animales;

create table if not exists PERRO(
	ID_PERRO INT not null primary key auto_increment,
	ID_RAZA VARCHAR(60) not null,
	IMAGEN VARCHAR(200) not null
);

create table if not exists RAZA(
	ID_RAZA VARCHAR(60) not null primary ,
	DESCRIPCION VARCHAR(200)
);

/*---------------------------------------------------------------------
 *	RESTRICCIONES DE LLAVES FORANEAS 
 *--------------------------------------------------------------------*/

alter table PERRO 
	add constraint FK_POSEE_RAZA
	foreign key (ID_RAZA)
	references RAZA(ID_RAZA)

	