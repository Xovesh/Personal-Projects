
/************************************************************************************
     File: prepare_up.c

       Contains the funtions used to prepare the upload of the page
***********************************************************************************/

#include "pixmap.h"
#include "upload.h"


/* Prepares the upload of the page                      */
/***********************************************************************************/

void prepare_up(page in_page) {

        for ( int i = 0; i<in_page.h; i=i+1){

                for (int j=0; j<in_page.w; j=j+1){
                        upload(in_page.im[i][j] , i, j, in_page.h, in_page.w);

                }
        }
}
