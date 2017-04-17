PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "quote" ("id" INTEGER NOT NULL PRIMARY KEY, "content" TEXT NOT NULL, "date" DATETIME NOT NULL);
INSERT INTO "quote" VALUES(1,'An egg asks his neighbor:
- Why do you have hair?
- Because I''m a kiwi!','2017-03-21 14:54:52.705976');
INSERT INTO "quote" VALUES(2,'Yay, a really hilarious one here!','2017-03-26 14:57:03.362013');
INSERT INTO "quote" VALUES(3,'Today it''s pee day!','2017-03-14 14:55:57.225965');
COMMIT;
