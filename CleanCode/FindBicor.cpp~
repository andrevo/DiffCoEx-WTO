#include <ctime>
#include <stdio.h>
#include <cmath>
#include <iostream>
#include <list>
#include <fstream>
#include <cstring>
#include <stdlib.h>

using namespace std;

//Parameters depending on input file

const char* expDataFile = "ExpData.txt"; //Name of expression data file
const int sampleSize = 198; //Number of data points per gene (normally number of individuals from which data is collected, corresponds to columns in the expression data text file)
const int numberOfGenes = 25698; // Number of distinct genes for which there is expression data (corresponds to rows in expression data)



struct Pair;


struct Pair
{
  double x;
  double y;
  double xRank;
  double yRank;
};



double spearman(list<Pair> subSample);

int main()
{
  srand(time(NULL));

  ifstream inStream;
  ofstream outStream;
  
  double expressionValues[sampleSize][numberOfGenes];
  string geneName[numberOfGenes];
  
  inStream.open(expDataFile);
  
  if(inStream.is_open())
    {
      char temp[4000000];
      int i = 0;
      while(!inStream.getline(temp, 4000000).eof() && i < numberOfGenes)
	{     
	  inStream >> geneName[i];

	  for (int k = 0; k < sampleSize; k++)
	    {
	      inStream >> expressionValues[k][i];

	    }

	  i++;
	}

    }
  

  double corrcoefAverageFull[numberOfGenes][numberOfGenes];

  for (int i = 0; i < numberOfGenes; i++)
    {
      cout << i << "\n";
      for (int j = 0; j < numberOfGenes; j++)
	{

	  list<Pair> completeSample;
	  for (int k = 0; k < sampleSize; k++)
	    {
	      Pair newPair;
	      newPair.x = expressionValues[k][i];
	      newPair.y = expressionValues[k][j];
	      completeSample.push_back(newPair);
	    }
	  corrcoefAverageFull[i][j] = spearman(completeSample);
	}
    }

  

  outStream.open("RhoAndVarFull.txt");
  for (int i = 0; i < numberOfGenes; i++)
    {
      for (int j = 0; j < numberOfGenes; j++)
	{
	  outStream << geneName[i] << "\t" << geneName[j] << "\t" << corrcoefAverageFull[i][j] << "\n";
	}
    }

 outStream.close();
   

 outStream.close();
}


double spearman(list<Pair> subSample)
{
  double xRank;
  double yRank;
  double xTies;
  double yTies;

  for (list<Pair>::iterator it = subSample.begin(); it != subSample.end(); it++)
    {
      xRank = 1;
      yRank = 1;
      xTies = -1;
      yTies = -1;
      for (list<Pair>::iterator jt = subSample.begin(); jt != subSample.end(); jt++)
	{
	  if ((*jt).x < (*it).x)
	    {
	      xRank++;
	    }
	  if ((*jt).x == (*it).x)
	    {
	      xTies++;
	    }

	  if ((*jt).y < (*it).y)
	    {
	      yRank++;
	    }
	  if ((*jt).y == (*it).y)
	    {
	      yTies++;
	    } 
	}
      
      (*it).xRank = xRank + xTies/2;
      (*it).yRank = yRank + yTies/2;

    }
  double averageRank = (double(subSample.size())+1)/2;

  double spearmanNum = 0;
  double spearmanDen1 = 0;
  double spearmanDen2 = 0;

  for (list<Pair>::iterator it= subSample.begin(); it != subSample.end(); it++)
    {
      spearmanNum = spearmanNum + ((*it).xRank-averageRank)*((*it).yRank-averageRank);
      spearmanDen1 = spearmanDen1 + pow(((*it).xRank-averageRank),2);
      spearmanDen2 = spearmanDen2 + pow(((*it).yRank-averageRank),2);
    }

  spearmanDen1 = sqrt(spearmanDen1);
  spearmanDen2 = sqrt(spearmanDen2);
  
  return spearmanNum/(spearmanDen1*spearmanDen2);
  
  
  
}
