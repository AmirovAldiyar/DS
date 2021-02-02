CREATE TABLE "movie"(
	"id" int,
	"plot_outline" varchar,
	"length" int,
	"year" timestamp,
	"title" varchar,
	"company" int,
	PRIMARY KEY ("year", "title", "id")
);

CREATE TABLE "production_company"(
	"name" varchar, 
	"address" varchar,
	"id" int,
	PRIMARY KEY ("name", "address", "id")
);

CREATE TABLE "genre"(
	"id" int PRIMARY KEY,
	"name" varchar
);

CREATE TABLE "person"(
	"id" int,
	"name" varchar,
	"bday" timestamp,
	PRIMARY KEY ("id", "name", "bday")
);

CREATE TABLE "quote"(
	"text" varchar,
	"quote_id" int PRIMARY KEY
);

CREATE TABLE "action"(
	"role" varchar,
	"person_id" int, 
	"movie_id" int,
	"id" int PRIMARY KEY
);

CREATE TABLE "classifies_as"(
	"movie_id" int,
	"genre_id" int
);

CREATE TABLE "procudes"(
	"pc_id" int,
	"movie_id" int
);

CREATE TABLE "has"(
	"movie_id" int,
	"quote_id" int
);

CREATE TABLE "voices"(
	"person_id" int, 
	"quote_id" int
);

