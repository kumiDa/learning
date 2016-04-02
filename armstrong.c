#include <stdio.h>
	main()
	{
		int a,b,c;
		printf("enter the number to check:");
		scanf("%d",&a);
		if(a>=0)
		{
			if((a*a*a)==a)
				return 1;
			else
				return 0;
		}
	}	
