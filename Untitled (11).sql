CREATE TABLE [parEsp] (
  [id_paraula] integer PRIMARY KEY,
  [paraula] nvarchar(255),
  [id_nivel] int,
  [audio] VARBINARY(MAX)
)
GO

CREATE TABLE [parEng] (
  [id_paraula] integer PRIMARY KEY,
  [paraula] nvarchar(255),
  [id_nivel] int,
  [audio] VARBINARY(MAX)
)
GO

CREATE TABLE [frsEsp] (
  [id_frase] integer PRIMARY KEY,
  [frase] text,
  [id_nivel] int,
  [audio] VARBINARY(MAX)
)
GO

CREATE TABLE [frsEng] (
  [id_frase] integer PRIMARY KEY,
  [frase] text,
  [id_nivel] int,
  [audio] VARBINARY(MAX)
)
GO

CREATE TABLE [usuaris] (
  [id_usuari] int PRIMARY KEY,
  [nom] nvarchar(255),
  [contrasenya] nvarchar(255),
  [email] nvarchar(255)
)
GO

CREATE TABLE [nivel] (
  [id_nivel] int PRIMARY KEY,
  [nivel] nvarchar(255)
)
GO

ALTER TABLE [parEng] ADD FOREIGN KEY ([id_paraula]) REFERENCES [parEsp] ([id_paraula])
GO

ALTER TABLE [frsEng] ADD FOREIGN KEY ([id_frase]) REFERENCES [frsEsp] ([id_frase])
GO

ALTER TABLE [frsEsp] ADD FOREIGN KEY ([id_nivel]) REFERENCES [nivel] ([id_nivel])
GO

ALTER TABLE [parEsp] ADD FOREIGN KEY ([id_nivel]) REFERENCES [nivel] ([id_nivel])
GO

ALTER TABLE [frsEng] ADD FOREIGN KEY ([id_nivel]) REFERENCES [nivel] ([id_nivel])
GO

ALTER TABLE [parEng] ADD FOREIGN KEY ([id_nivel]) REFERENCES [nivel] ([id_nivel])
GO
