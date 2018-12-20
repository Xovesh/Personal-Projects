
/************************************************************************************
     File: encrypt.c

        Generates the encrypted page
***********************************************************************************/

#include "pixmap.h"
#include <omp.h>
void encrypt (unsigned char *v1, unsigned char *v2)
{

 int encryptionmatrix[2][2]={{21,35},{18,79}};
 unsigned char s1 = *v1;
 unsigned char s2 = *v2;
 *v1 = (encryptionmatrix[0][0]*s1 + encryptionmatrix[0][1]*s2)%256;
 *v2 =(encryptionmatrix[1][0]*s1 + encryptionmatrix[1][1]*s2)%256;

}


void generate_encrypted_page(page in_page, page *out_page)
{
 unsigned char v1, v2;
 generate_page(out_page,in_page.h,in_page.w,BLACK);
int j;
int i;
#pragma omp parallel for private(i,j,v1,v2) schedule(static, 1)
 for(i= 0; i<in_page.h; i+=1){
    for(j=0; j<in_page.w; j+=2){
        v1 = in_page.dat[i*in_page.w+j];
        v2 = in_page.dat[i*in_page.w+j+1];
        encrypt(&v1, &v2);
        out_page->dat[i*in_page.w+j] = v1;
        out_page->dat[i*in_page.w+j+1] = v2;
        }
}
}
