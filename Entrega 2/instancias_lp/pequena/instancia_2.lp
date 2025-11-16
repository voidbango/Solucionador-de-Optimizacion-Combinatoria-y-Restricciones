/* Funcion objetivo consistente con modelo */
max 10 X_1_1_DAY + 2 X_1_1_NIGHT + 2 X_1_2_DAY + 6 X_1_2_NIGHT + 2 X_1_3_DAY + 10 X_1_3_NIGHT + 8 X_1_4_DAY + 6 X_1_4_NIGHT + 10 X_1_5_DAY + 9 X_1_5_NIGHT + 2 X_2_1_DAY + 1 X_2_1_NIGHT + 6 X_2_2_DAY + 7 X_2_2_NIGHT + 9 X_2_3_DAY + 8 X_2_3_NIGHT + 8 X_2_4_DAY + 5 X_2_4_NIGHT + 8 X_2_5_NIGHT + 4 X_3_1_DAY + 6 X_3_1_NIGHT + 10 X_3_2_DAY + 8 X_3_2_NIGHT + 5 X_3_3_DAY + 6 X_3_3_NIGHT + 3 X_3_4_NIGHT + 3 X_3_5_DAY + 3 X_3_5_NIGHT + 10 X_4_1_DAY + 9 X_4_1_NIGHT + 7 X_4_2_NIGHT + 7 X_4_3_DAY + 5 X_4_3_NIGHT + 6 X_4_4_DAY + 7 X_4_4_NIGHT + 10 X_4_5_DAY + 6 X_4_5_NIGHT + 7 X_5_1_DAY + 8 X_5_1_NIGHT + 6 X_5_2_DAY + 5 X_5_3_DAY + 2 X_5_3_NIGHT + 10 X_5_4_DAY + 2 X_5_5_DAY + 5 X_5_5_NIGHT + 9 X_6_1_DAY + 2 X_6_1_NIGHT + 4 X_6_2_DAY + 1 X_6_2_NIGHT + 5 X_6_3_DAY + 7 X_6_3_NIGHT + 10 X_6_4_DAY + 8 X_6_4_NIGHT + 4 X_6_5_DAY + 4 X_6_5_NIGHT + 1 X_7_1_DAY + 8 X_7_1_NIGHT + 8 X_7_2_DAY + 1 X_7_2_NIGHT + 8 X_7_3_DAY + 1 X_7_3_NIGHT + 1 X_7_4_DAY + 7 X_7_4_NIGHT + 7 X_7_5_DAY + 3 X_7_5_NIGHT ;

subject to

/* Restricciones */
X_1_1_DAY + X_2_1_DAY + X_3_1_DAY + X_4_1_DAY + X_5_1_DAY + X_6_1_DAY + X_7_1_DAY = 3 ;
X_1_1_NIGHT + X_2_1_NIGHT + X_3_1_NIGHT + X_4_1_NIGHT + X_5_1_NIGHT + X_6_1_NIGHT + X_7_1_NIGHT = 3 ;
X_1_2_DAY + X_2_2_DAY + X_3_2_DAY + X_4_2_DAY + X_5_2_DAY + X_6_2_DAY + X_7_2_DAY = 3 ;
X_1_2_NIGHT + X_2_2_NIGHT + X_3_2_NIGHT + X_4_2_NIGHT + X_5_2_NIGHT + X_6_2_NIGHT + X_7_2_NIGHT = 3 ;
X_1_3_DAY + X_2_3_DAY + X_3_3_DAY + X_4_3_DAY + X_5_3_DAY + X_6_3_DAY + X_7_3_DAY = 3 ;
X_1_3_NIGHT + X_2_3_NIGHT + X_3_3_NIGHT + X_4_3_NIGHT + X_5_3_NIGHT + X_6_3_NIGHT + X_7_3_NIGHT = 3 ;
X_1_4_DAY + X_2_4_DAY + X_3_4_DAY + X_4_4_DAY + X_5_4_DAY + X_6_4_DAY + X_7_4_DAY = 3 ;
X_1_4_NIGHT + X_2_4_NIGHT + X_3_4_NIGHT + X_4_4_NIGHT + X_5_4_NIGHT + X_6_4_NIGHT + X_7_4_NIGHT = 3 ;
X_1_5_DAY + X_2_5_DAY + X_3_5_DAY + X_4_5_DAY + X_5_5_DAY + X_6_5_DAY + X_7_5_DAY = 4 ;
X_1_5_NIGHT + X_2_5_NIGHT + X_3_5_NIGHT + X_4_5_NIGHT + X_5_5_NIGHT + X_6_5_NIGHT + X_7_5_NIGHT = 3 ;
/* C3: disponibilidad consistente con modelo */
 X_2_5_DAY <= 0 ;
 X_3_4_DAY <= 0 ;
 X_4_2_DAY <= 0 ;
 X_5_2_NIGHT <= 0 ;
 X_5_4_NIGHT <= 0 ;
/* C4: consistente con modelo (<= 2) */
X_1_1_DAY + X_1_1_NIGHT <= 2 ;
X_1_2_DAY + X_1_2_NIGHT <= 2 ;
X_1_3_DAY + X_1_3_NIGHT <= 2 ;
X_1_4_DAY + X_1_4_NIGHT <= 2 ;
X_1_5_DAY + X_1_5_NIGHT <= 2 ;
X_2_1_DAY + X_2_1_NIGHT <= 2 ;
X_2_2_DAY + X_2_2_NIGHT <= 2 ;
X_2_3_DAY + X_2_3_NIGHT <= 2 ;
X_2_4_DAY + X_2_4_NIGHT <= 2 ;
X_2_5_DAY + X_2_5_NIGHT <= 2 ;
X_3_1_DAY + X_3_1_NIGHT <= 2 ;
X_3_2_DAY + X_3_2_NIGHT <= 2 ;
X_3_3_DAY + X_3_3_NIGHT <= 2 ;
X_3_4_DAY + X_3_4_NIGHT <= 2 ;
X_3_5_DAY + X_3_5_NIGHT <= 2 ;
X_4_1_DAY + X_4_1_NIGHT <= 2 ;
X_4_2_DAY + X_4_2_NIGHT <= 2 ;
X_4_3_DAY + X_4_3_NIGHT <= 2 ;
X_4_4_DAY + X_4_4_NIGHT <= 2 ;
X_4_5_DAY + X_4_5_NIGHT <= 2 ;
X_5_1_DAY + X_5_1_NIGHT <= 2 ;
X_5_2_DAY + X_5_2_NIGHT <= 2 ;
X_5_3_DAY + X_5_3_NIGHT <= 2 ;
X_5_4_DAY + X_5_4_NIGHT <= 2 ;
X_5_5_DAY + X_5_5_NIGHT <= 2 ;
X_6_1_DAY + X_6_1_NIGHT <= 2 ;
X_6_2_DAY + X_6_2_NIGHT <= 2 ;
X_6_3_DAY + X_6_3_NIGHT <= 2 ;
X_6_4_DAY + X_6_4_NIGHT <= 2 ;
X_6_5_DAY + X_6_5_NIGHT <= 2 ;
X_7_1_DAY + X_7_1_NIGHT <= 2 ;
X_7_2_DAY + X_7_2_NIGHT <= 2 ;
X_7_3_DAY + X_7_3_NIGHT <= 2 ;
X_7_4_DAY + X_7_4_NIGHT <= 2 ;
X_7_5_DAY + X_7_5_NIGHT <= 2 ;
/* C5: prohibir turno night->morning */
X_1_1_NIGHT + X_1_2_DAY <= 1 ;
X_1_2_NIGHT + X_1_3_DAY <= 1 ;
X_1_3_NIGHT + X_1_4_DAY <= 1 ;
X_1_4_NIGHT + X_1_5_DAY <= 1 ;
X_2_1_NIGHT + X_2_2_DAY <= 1 ;
X_2_2_NIGHT + X_2_3_DAY <= 1 ;
X_2_3_NIGHT + X_2_4_DAY <= 1 ;
X_2_4_NIGHT + X_2_5_DAY <= 1 ;
X_3_1_NIGHT + X_3_2_DAY <= 1 ;
X_3_2_NIGHT + X_3_3_DAY <= 1 ;
X_3_3_NIGHT + X_3_4_DAY <= 1 ;
X_3_4_NIGHT + X_3_5_DAY <= 1 ;
X_4_1_NIGHT + X_4_2_DAY <= 1 ;
X_4_2_NIGHT + X_4_3_DAY <= 1 ;
X_4_3_NIGHT + X_4_4_DAY <= 1 ;
X_4_4_NIGHT + X_4_5_DAY <= 1 ;
X_5_1_NIGHT + X_5_2_DAY <= 1 ;
X_5_2_NIGHT + X_5_3_DAY <= 1 ;
X_5_3_NIGHT + X_5_4_DAY <= 1 ;
X_5_4_NIGHT + X_5_5_DAY <= 1 ;
X_6_1_NIGHT + X_6_2_DAY <= 1 ;
X_6_2_NIGHT + X_6_3_DAY <= 1 ;
X_6_3_NIGHT + X_6_4_DAY <= 1 ;
X_6_4_NIGHT + X_6_5_DAY <= 1 ;
X_7_1_NIGHT + X_7_2_DAY <= 1 ;
X_7_2_NIGHT + X_7_3_DAY <= 1 ;
X_7_3_NIGHT + X_7_4_DAY <= 1 ;
X_7_4_NIGHT + X_7_5_DAY <= 1 ;
/* C6: consistente, define W_if correctamente */
/* C7 */

/* Declaración de variables binarias */
bin X_1_1_DAY, X_1_1_NIGHT, X_1_2_DAY, X_1_2_NIGHT, X_1_3_DAY, X_1_3_NIGHT, X_1_4_DAY, X_1_4_NIGHT, X_1_5_DAY, X_1_5_NIGHT, X_2_1_DAY, X_2_1_NIGHT, X_2_2_DAY, X_2_2_NIGHT, X_2_3_DAY, X_2_3_NIGHT, X_2_4_DAY, X_2_4_NIGHT, X_2_5_DAY, X_2_5_NIGHT, X_3_1_DAY, X_3_1_NIGHT, X_3_2_DAY, X_3_2_NIGHT, X_3_3_DAY, X_3_3_NIGHT, X_3_4_DAY, X_3_4_NIGHT, X_3_5_DAY, X_3_5_NIGHT, X_4_1_DAY, X_4_1_NIGHT, X_4_2_DAY, X_4_2_NIGHT, X_4_3_DAY, X_4_3_NIGHT, X_4_4_DAY, X_4_4_NIGHT, X_4_5_DAY, X_4_5_NIGHT, X_5_1_DAY, X_5_1_NIGHT, X_5_2_DAY, X_5_2_NIGHT, X_5_3_DAY, X_5_3_NIGHT, X_5_4_DAY, X_5_4_NIGHT, X_5_5_DAY, X_5_5_NIGHT, X_6_1_DAY, X_6_1_NIGHT, X_6_2_DAY, X_6_2_NIGHT, X_6_3_DAY, X_6_3_NIGHT, X_6_4_DAY, X_6_4_NIGHT, X_6_5_DAY, X_6_5_NIGHT, X_7_1_DAY, X_7_1_NIGHT, X_7_2_DAY, X_7_2_NIGHT, X_7_3_DAY, X_7_3_NIGHT, X_7_4_DAY, X_7_4_NIGHT, X_7_5_DAY, X_7_5_NIGHT ;

end