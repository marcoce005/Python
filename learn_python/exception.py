## exception = evento che si attiva quando il programma crash o va in errore

from weakref import finalize


try :                                                   ## il programma che va eseguito
    n = int (input ("\nInserire il numero:\t"))
    n2 = int (input ("\nInserire il numero:\t"))
    r = n / n2

                                            ## aggiungendo (as e) e stampando (e) ti da l'errore

except ValueError as e :                                              ## se l'input è sbagliato
    print (e)
    print ("\nInserire solo numeri non lettere o parole!\n")

except ZeroDivisionError as e :                              ## se si divide per 0
    print (e)
    print ("\nNon puoi dividere per zero!!!\n")

except Exception as e :
    print (e)                                      ## se ci sono altri errori
    print ("\nErrore, qualcosa e' andato storto\n")

else :                              ## se il programma funziona fa questo
    print ("\nRisultato = ", r)

finally :
    print ("\nContinua lo stesso")      ## fa continuare il programma