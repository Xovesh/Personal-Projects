/************************************************************************************
   File: filter.c

   Includes the functions required to filter the page.
***********************************************************************************/
#include <stdio.h>
#include <math.h>
#include "pixmap.h"
#include <omp.h>

#define NUM_IT 100
#define FILTER_SIZE 3

/*  Copy page in_page in page out_page */
/***************************************************/
void copy_page(page *in_page, page *out_page)
{
 int i,j;
#pragma omp parallel for private(j)
 for (i=0;i<in_page->h;i++)
  for (j=0;j<in_page->w;j++) out_page->im[i][j]=in_page->im[i][j];
}


/* Apply the filter to a page                            */
/***********************************************************************************/

double filter_page (page *in_page, page *out_page)
{
        //Local and general mimimum values
        int fMin = WHITE, lMin = WHITE;
        //Sum of the weights of the filter
        int filterSize = 9;
        //Sum of the original values of all pixels
        long total = 0;
        //Sum of the weighted values of pixels within the filter
        int lSum = 0;
        //Image pixels
        int dimensions = (in_page->h-2) *( in_page->w-2);
        //Indexes for iteration
        int i,j,i2,j2;
        //Declaration of the used filter
        int filter[FILTER_SIZE][FILTER_SIZE] = {
                {1,1,1},
                {1,1,1},
                {1,1,1}
        };

        //Iterating over picture excluding borders
        #pragma omp parallel for  private(j,i2,j2,lSum) reduction(min:fMin) reduction(+:total) schedule(guided)
		 for (i=1;i<in_page->h-1;i++){
                for (j=1;j<in_page->w-1;j++) {
                        //Iterating 3x3 around current pixel and adding weighted values(filter)
                        for(i2 = 0; i2 < FILTER_SIZE; i2++){
                                for(j2 = 0; j2 < FILTER_SIZE; j2++){
                                        //Add relative weighted value of current 3x3 position
                                        lSum += in_page->im[i+(i2-1)][j+(j2-1)] * filter[i2][j2];
                                }
                        }
                        //Assigned correspoding out value
                        out_page->im[i][j] = (lSum / filterSize);
                        //Update fMIn
                        if(out_page->im[i][j] < fMin) fMin = out_page->im[i][j];
                        //Reset local variables
                        lSum = 0;
                        //Added
                        total += out_page->im[i][j];
                }
        }
        printf("Current total = %ld ,current average = %f ,current min = %d \n",total,(double)total/(double)dimensio$
        //Returns full picture's average value - fMin
        return(double)total/(double)dimensions-(double)fMin;
}




/* generate the filtered page               */
/**************************************/
void generate_filtered_page ( page *in_page, page *out_page, float limit)
{

  generate_page(out_page,in_page->h,in_page->w,BLACK);
  copy_page(in_page,out_page);
  double temp =  filter_page(in_page, out_page);
  int count = 1;
  while (temp > limit){
        if(count % 2  == 0)
                temp = filter_page(in_page, out_page);
        else if(count % 2 == 1)
                temp = filter_page(out_page, in_page);

        count++;
        printf("%f is the current diff at iter %d\n",temp,count);
  }
   if(count % 2 == 0) copy_page(in_page,out_page);

  printf("%f is the final difference",temp);



}

		
