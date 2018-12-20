/************************************************************************************
   File: page_s.c (serial)

   The following process is apllied to a page in PGM format (P5: binary):
     -- filter
     -- encryption
     -- prepare to upload

   Input files:   xx.pgm (page in pgm format)
   Output files:  xx_fil.pgm    filtered page
                  xx_enc.pgm    encrypted page

   Compile the program toogether with filter.c, encrypt.c and prepare_up.c
***********************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <string.h>

#include "pixmap.h"
#include "filter.h"
#include "encrypt.h"
#include "prepare_up.h"

/*************************              MAIN                  **********************/
/***********************************************************************************/

void main(int argc, char **argv)
{
  char name[100];
  int i;

  // pages: original, filtered and encrypted
  page page_ori,page_fil,page_enc;

  // time calculation
  struct timeval t0,t1;
  double tex1,tex2,tex3,tex;

  if (argc != 3)
  {
    printf ("\nUSE: program page(.pgm) limit\n");
    exit (0);
  }

  // Reading the input page: only gray scale pages in .pgm format
  if (load_pixmap(argv[1], &page_ori) == 0)
  {
    printf ("\nError reading the input file: %s\n\n",argv[1]);
    exit (0);
  }

  /* Page processing: generate new pages filtered and encrypted      */
  /**********************************************************************************************************/
  printf("\n --> Processig page: %s (%d x %d). Limit: %.1f\n",argv[1],page_ori.h,page_ori.w,atof(argv[2]));
 gettimeofday(&t0, 0);
 generate_filtered_page(&page_ori,&page_fil,atof(argv[2]));
 gettimeofday(&t1, 0);
 tex1 = (t1.tv_sec - t0.tv_sec) + (t1.tv_usec - t0.tv_usec) / 1e6;
 printf("\n     Filtering the page: serial ex. time = %1.1f ms", tex1*1000);

  gettimeofday(&t0, 0);
  generate_encrypted_page(page_fil,&page_enc);
  gettimeofday(&t1, 0);
  tex2 = (t1.tv_sec - t0.tv_sec) + (t1.tv_usec - t0.tv_usec) / 1e6;
  printf("\n     Encrypt page: serial ex. time = %1.1f ms", tex2*1000);

gettimeofday(&t0, 0);
prepare_up(page_enc);
gettimeofday(&t1, 0);
tex3 = (t1.tv_sec - t0.tv_sec) + (t1.tv_usec - t0.tv_usec) / 1e6;
printf("\n     Prepare the upload: serial ex. time = %1.1f ms\n", tex3*1000);

tex=tex1+tex2+tex3;
printf("\n     TOTAL: serial ex. time = %1.1f ms\n", tex*1000);

  /* Write pages in disk                                        */
  /*********************************************************************************/
 strcpy(name,argv[1]);
 name[strlen(name)-4]='\0';
 strcat(name,"_fil_ser.pgm");
 store_pixmap(name,page_fil);

  strcpy(name,argv[1]);
name[strlen(name)-4]='\0';
  strcat(name,"_enc_ser.pgm");
  store_pixmap(name,page_enc);

  // Free memory of images
  free_page(page_ori);
  free_page(page_fil);
  free_page(page_enc);
}
