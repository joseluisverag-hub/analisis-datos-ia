SELECT COUNT(*) AS total_filas FROM titanic;

SELECT
    Sex,
    AVG(Survived) AS tasa_supervivencia
FROM titanic
GROUP BY Sex
ORDER BY tasa_supervivencia DESC;

SELECT
    Pclass,
    AVG(Survived) AS tasa_supervivencia
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;

SELECT
    Sex,
    Pclass,
    AVG(Survived) AS tasa_supervivencia
FROM titanic
GROUP BY Sex, Pclass
ORDER BY Sex, Pclass;

SELECT
    Embarked,
    AVG(Survived) AS tasa_supervivencia,
    COUNT(*) AS total_pasajeros
FROM titanic
GROUP BY Embarked
ORDER BY tasa_supervivencia DESC;