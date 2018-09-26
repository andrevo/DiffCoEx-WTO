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



double bicor(list<Pair> subSample);

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
	  corrcoefAverageFull[i][j] = bicor(completeSample);
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


double bicor(list<Pair> subSample)
{

  double xmed;
  double ymed;
  // double xRank;
  // double yRank;
  // double xTies;
  // double yTies;
  double xVals[sampleSize];
  double yVals[sampleSize];
  int i = 0;
  for (list<Pair>::iterator it = subSample.begin(); it != subSample.end(); it++)
    {
      xVals[i] = (*it).x;
      yVals[i] = (*it).y;
      i++; 
    }
  
  for (int i = sampleSize - 1; i > 0; --i)
    {
      for (int j = 0; j < i; ++j)
	{
	  if (xVals[j] > xVals[j+1])
	    {
	      double xTemp = xVals[j];
	      xVals[j] = xVals[j+1];
	      xVals[j+1] = xTemp;
	    }
	}
    } 
  for (int i = sampleSize - 1; i > 0; --i)
    {
      for (int j = 0; j < i; ++j)
	{
	  if (yVals[j] > yVals[j+1])
	    {
	      double yTemp = yVals[j];
	      yVals[j] = yVals[j+1];
	      yVals[j+1] = yTemp;
	    }
	}
    }

  xmed = xVals[sampleSize/2-1];
  ymed = yVals[sampleSize/2-1];

  double xad[sampleSize];
  double yad[sampleSize];
  for (int i = 0; i < sampleSize; i++)
    {
      xad[i] = abs(xVals[i]-xmed);
      yad[i] = abs(yVals[i]-xmed);
    }

  for (int i = sampleSize - 1; i > 0; --i)
    {
      for (int j = 0; j < i; ++j)
	{
	  if (xad[j] > xad[j+1])
	    {
	      double xTemp = xad[j];
	      xad[j] = xad[j+1];
	      xad[j+1] = xTemp;
	    }
	}
    } 
  for (int i = sampleSize - 1; i > 0; --i)
    {
      for (int j = 0; j < i; ++j)
	{
	  if (yad[j] > yad[j+1])
	    {
	      double yTemp = yad[j];
	      yad[j] = yad[j+1];
	      yad[j+1] = yTemp;
	    }
	}
    }

  double xmad = xad[sampleSize/2-1];
  double ymad = yad[sampleSize/2-1];

  double u[sampleSize];
  double v[sampleSize];
  double wx[sampleSize];
  double wy[sampleSize];


  i = 0;
  for (list<Pair>::iterator it = subSample.begin(); it != subSample.end(); it++)
    {
      xVals[i] = (*it).x;
      yVals[i] = (*it).y;
      u[i] = (xVals[i]-xmed)/(9*xmad);
      v[i] = (yVals[i]-ymed)/(9*ymad);
      if (abs(u[i]) < 1)
	{
	  wx[i] = pow(1-pow(u[i], 2), 2);
	}
      else
	{
	  wx[i] = 0;
	}
      if (abs(v[i]) < 1)
	{
	  wy[i] = pow(1-pow(v[i], 2), 2);
	}
      else
	{
	  wy[i] = 0;
	}
      //  cout << xVals[i] << "\t" << u[i] << "\t" <<  wx[i] << "\t" << yVals[i] << "\t" << v[i] << "\t" << wy[i] << "\n";
      i++;
      
    }
   
  double normx = 0;
  double normy = 0;
  for (int i = 0; i < sampleSize; i++)
    {
      normx = normx + pow((xVals[i]-xmed)*wx[i], 2);
      normy = normy + pow((yVals[i]-ymed)*wy[i], 2);
    }
  normx = sqrt(normx);
  normy = sqrt(normy);
  //  cout << "Normalization factor: " << normx << "\t" << normy << "\n";    
  
  for (int i = 0; i < sampleSize; i++)
    {
      xVals[i] = (xVals[i]-xmed)*wx[i]/normx;
      yVals[i] = (yVals[i]-ymed)*wy[i]/normy;
	
    }
  
  double bicor = 0;
  for (int i = 0; i < sampleSize; i++)
    {
      bicor = bicor + xVals[i]*yVals[i];
    }
  //cout << "bicor: " << bicor << "\n";
  return bicor;
}
