SELECT
    COUNT(ID) COUNT
FROM
    ECOLI_DATA
WHERE
    GENOTYPE & 5         -- 0101
    AND NOT GENOTYPE & 2 -- 0010

/*
예를 들어 GENOTYPE 값이 6이면? 2진수로 0110

→ 비트연산자를 이용해서 풀면 쉽다는 것을 알고나서 좀 허탈했다.
→ 나는 2진수로 바꿔서(conv), 해당 값이  **1* 이 아니고(and),
*1** 이거나 ***1 이면 select해서 count해라 고 하려고 했었음.

비트연산자 문제 참조한 곳
https://velog.io/@whtjd999/SQL-%EB%B9%84%ED%8A%B8%EC%97%B0%EC%82%B0%EC%9E%90
*/