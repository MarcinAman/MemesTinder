CREATE TABLE Memes (
    MemeID integer NOT NULL CONSTRAINT Memes_pk PRIMARY KEY AUTOINCREMENT,
    Source varchar(256) NOT NULL,
    Alt varchar(256) NOT NULL
);

-- Table: Viewiers
CREATE TABLE Viewiers (
    ViewerID integer NOT NULL CONSTRAINT Viewiers_pk PRIMARY KEY AUTOINCREMENT,
    Name varchar(256) NOT NULL,
    Surname varchar(256) NOT NULL
);

-- Table: Views
CREATE TABLE Views (
    ViewID integer NOT NULL CONSTRAINT Views_pk PRIMARY KEY AUTOINCREMENT,
    Result integer NOT NULL,
    ViewerID integer NOT NULL,
    MemeID integer NOT NULL,
    CONSTRAINT Views_Viewiers FOREIGN KEY (ViewerID)
    REFERENCES Viewiers (ViewerID),
    CONSTRAINT Views_Memes FOREIGN KEY (MemeID)
    REFERENCES Memes (MemeID)
);