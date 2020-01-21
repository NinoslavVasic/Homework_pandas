{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " #  A Whale off the Port(folio)\n",
    "\n",
    " In this assignment, you'll get to use what you've learned this week to evaluate the performance among various algorithmic, hedge, and mutual fund portfolios and compare them against the S&P 500."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import datetime as dt\n",
    "from pathlib import Path\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Cleaning\n",
    "\n",
    "In this section, you will need to read the CSV files into DataFrames and perform any necessary data cleaning steps. After cleaning, combine all DataFrames into a single DataFrame.\n",
    "\n",
    "Files:\n",
    "1. whale_returns.csv\n",
    "2. algo_returns.csv\n",
    "3. sp500_history.csv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Whale Returns\n",
    "\n",
    "Read the Whale Portfolio daily returns and clean the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SOROS FUND MANAGEMENT LLC</th>\n",
       "      <th>PAULSON &amp; CO.INC.</th>\n",
       "      <th>TIGER GLOBAL MANAGEMENT LLC</th>\n",
       "      <th>BERKSHIRE HATHAWAY INC</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2015-03-02</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-03</td>\n",
       "      <td>-0.001266</td>\n",
       "      <td>-0.004981</td>\n",
       "      <td>-0.000496</td>\n",
       "      <td>-0.006569</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-04</td>\n",
       "      <td>0.002230</td>\n",
       "      <td>0.003241</td>\n",
       "      <td>-0.002534</td>\n",
       "      <td>0.004213</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-05</td>\n",
       "      <td>0.004016</td>\n",
       "      <td>0.004076</td>\n",
       "      <td>0.002355</td>\n",
       "      <td>0.006726</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-06</td>\n",
       "      <td>-0.007905</td>\n",
       "      <td>-0.003574</td>\n",
       "      <td>-0.008481</td>\n",
       "      <td>-0.013098</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-25</td>\n",
       "      <td>-0.000285</td>\n",
       "      <td>-0.001291</td>\n",
       "      <td>-0.005153</td>\n",
       "      <td>0.004848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-26</td>\n",
       "      <td>0.008149</td>\n",
       "      <td>0.009162</td>\n",
       "      <td>0.012355</td>\n",
       "      <td>0.010434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-29</td>\n",
       "      <td>0.001254</td>\n",
       "      <td>0.002719</td>\n",
       "      <td>0.006251</td>\n",
       "      <td>0.005223</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-30</td>\n",
       "      <td>-0.001295</td>\n",
       "      <td>-0.002211</td>\n",
       "      <td>-0.000259</td>\n",
       "      <td>-0.003702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-05-01</td>\n",
       "      <td>-0.005847</td>\n",
       "      <td>-0.001341</td>\n",
       "      <td>-0.007936</td>\n",
       "      <td>-0.007833</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1060 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            SOROS FUND MANAGEMENT LLC  PAULSON & CO.INC.   \\\n",
       "Date                                                        \n",
       "2015-03-02                        NaN                 NaN   \n",
       "2015-03-03                  -0.001266           -0.004981   \n",
       "2015-03-04                   0.002230            0.003241   \n",
       "2015-03-05                   0.004016            0.004076   \n",
       "2015-03-06                  -0.007905           -0.003574   \n",
       "...                               ...                 ...   \n",
       "2019-04-25                  -0.000285           -0.001291   \n",
       "2019-04-26                   0.008149            0.009162   \n",
       "2019-04-29                   0.001254            0.002719   \n",
       "2019-04-30                  -0.001295           -0.002211   \n",
       "2019-05-01                  -0.005847           -0.001341   \n",
       "\n",
       "            TIGER GLOBAL MANAGEMENT LLC  BERKSHIRE HATHAWAY INC  \n",
       "Date                                                             \n",
       "2015-03-02                          NaN                     NaN  \n",
       "2015-03-03                    -0.000496               -0.006569  \n",
       "2015-03-04                    -0.002534                0.004213  \n",
       "2015-03-05                     0.002355                0.006726  \n",
       "2015-03-06                    -0.008481               -0.013098  \n",
       "...                                 ...                     ...  \n",
       "2019-04-25                    -0.005153                0.004848  \n",
       "2019-04-26                     0.012355                0.010434  \n",
       "2019-04-29                     0.006251                0.005223  \n",
       "2019-04-30                    -0.000259               -0.003702  \n",
       "2019-05-01                    -0.007936               -0.007833  \n",
       "\n",
       "[1060 rows x 4 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading whale returns\n",
    "whale_returns_csv = Path(\"Resources/whale_returns.csv\")\n",
    "# YOUR CODE HERE\n",
    "whale_returns_df = pd.read_csv(whale_returns_csv,index_col=\"Date\", infer_datetime_format=True, parse_dates=True)\n",
    "whale_returns_df.sort_values(\"Date\", ascending=True, inplace=True)\n",
    "whale_returns_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SOROS FUND MANAGEMENT LLC      1\n",
       "PAULSON & CO.INC.              1\n",
       "TIGER GLOBAL MANAGEMENT LLC    1\n",
       "BERKSHIRE HATHAWAY INC         1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Count nulls\n",
    "# YOUR CODE HERE\n",
    "whale_returns_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SOROS FUND MANAGEMENT LLC</th>\n",
       "      <th>PAULSON &amp; CO.INC.</th>\n",
       "      <th>TIGER GLOBAL MANAGEMENT LLC</th>\n",
       "      <th>BERKSHIRE HATHAWAY INC</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2015-03-03</td>\n",
       "      <td>-0.001266</td>\n",
       "      <td>-0.004981</td>\n",
       "      <td>-0.000496</td>\n",
       "      <td>-0.006569</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-04</td>\n",
       "      <td>0.002230</td>\n",
       "      <td>0.003241</td>\n",
       "      <td>-0.002534</td>\n",
       "      <td>0.004213</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-05</td>\n",
       "      <td>0.004016</td>\n",
       "      <td>0.004076</td>\n",
       "      <td>0.002355</td>\n",
       "      <td>0.006726</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-06</td>\n",
       "      <td>-0.007905</td>\n",
       "      <td>-0.003574</td>\n",
       "      <td>-0.008481</td>\n",
       "      <td>-0.013098</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-09</td>\n",
       "      <td>0.000582</td>\n",
       "      <td>0.004225</td>\n",
       "      <td>0.005843</td>\n",
       "      <td>-0.001652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-25</td>\n",
       "      <td>-0.000285</td>\n",
       "      <td>-0.001291</td>\n",
       "      <td>-0.005153</td>\n",
       "      <td>0.004848</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-26</td>\n",
       "      <td>0.008149</td>\n",
       "      <td>0.009162</td>\n",
       "      <td>0.012355</td>\n",
       "      <td>0.010434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-29</td>\n",
       "      <td>0.001254</td>\n",
       "      <td>0.002719</td>\n",
       "      <td>0.006251</td>\n",
       "      <td>0.005223</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-30</td>\n",
       "      <td>-0.001295</td>\n",
       "      <td>-0.002211</td>\n",
       "      <td>-0.000259</td>\n",
       "      <td>-0.003702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-05-01</td>\n",
       "      <td>-0.005847</td>\n",
       "      <td>-0.001341</td>\n",
       "      <td>-0.007936</td>\n",
       "      <td>-0.007833</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1059 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            SOROS FUND MANAGEMENT LLC  PAULSON & CO.INC.   \\\n",
       "Date                                                        \n",
       "2015-03-03                  -0.001266           -0.004981   \n",
       "2015-03-04                   0.002230            0.003241   \n",
       "2015-03-05                   0.004016            0.004076   \n",
       "2015-03-06                  -0.007905           -0.003574   \n",
       "2015-03-09                   0.000582            0.004225   \n",
       "...                               ...                 ...   \n",
       "2019-04-25                  -0.000285           -0.001291   \n",
       "2019-04-26                   0.008149            0.009162   \n",
       "2019-04-29                   0.001254            0.002719   \n",
       "2019-04-30                  -0.001295           -0.002211   \n",
       "2019-05-01                  -0.005847           -0.001341   \n",
       "\n",
       "            TIGER GLOBAL MANAGEMENT LLC  BERKSHIRE HATHAWAY INC  \n",
       "Date                                                             \n",
       "2015-03-03                    -0.000496               -0.006569  \n",
       "2015-03-04                    -0.002534                0.004213  \n",
       "2015-03-05                     0.002355                0.006726  \n",
       "2015-03-06                    -0.008481               -0.013098  \n",
       "2015-03-09                     0.005843               -0.001652  \n",
       "...                                 ...                     ...  \n",
       "2019-04-25                    -0.005153                0.004848  \n",
       "2019-04-26                     0.012355                0.010434  \n",
       "2019-04-29                     0.006251                0.005223  \n",
       "2019-04-30                    -0.000259               -0.003702  \n",
       "2019-05-01                    -0.007936               -0.007833  \n",
       "\n",
       "[1059 rows x 4 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop nulls\n",
    "# YOUR CODE HERE\n",
    "whale_returns_df = whale_returns_df.dropna().astype(float)\n",
    "\n",
    "whale_returns_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Algorithmic Daily Returns\n",
    "\n",
    "Read the algorithmic daily returns and clean the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Algo 1</th>\n",
       "      <th>Algo 2</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2014-05-28</td>\n",
       "      <td>0.001745</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-05-29</td>\n",
       "      <td>0.003978</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-05-30</td>\n",
       "      <td>0.004464</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-02</td>\n",
       "      <td>0.005692</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-03</td>\n",
       "      <td>0.005292</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Algo 1  Algo 2\n",
       "Date                        \n",
       "2014-05-28  0.001745     NaN\n",
       "2014-05-29  0.003978     NaN\n",
       "2014-05-30  0.004464     NaN\n",
       "2014-06-02  0.005692     NaN\n",
       "2014-06-03  0.005292     NaN"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading algorithmic returns\n",
    "algo_returns_csv = Path(\"Resources/algo_returns.csv\")\n",
    "# YOUR CODE HERE\n",
    "algo_returns_df = pd.read_csv(algo_returns_csv, index_col=\"Date\", infer_datetime_format=True, parse_dates=True)\n",
    "algo_returns_df.sort_values(\"Date\", ascending=True, inplace=True)\n",
    "algo_returns_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Algo 1    0\n",
       "Algo 2    6\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Count nulls\n",
    "# YOUR CODE HERE\n",
    "algo_returns_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Algo 1</th>\n",
       "      <th>Algo 2</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2014-06-05</td>\n",
       "      <td>0.004062</td>\n",
       "      <td>0.013285</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-06</td>\n",
       "      <td>0.001857</td>\n",
       "      <td>0.008284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-09</td>\n",
       "      <td>-0.005012</td>\n",
       "      <td>0.005668</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-10</td>\n",
       "      <td>0.004406</td>\n",
       "      <td>-0.000735</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2014-06-11</td>\n",
       "      <td>0.004760</td>\n",
       "      <td>-0.003761</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Algo 1    Algo 2\n",
       "Date                          \n",
       "2014-06-05  0.004062  0.013285\n",
       "2014-06-06  0.001857  0.008284\n",
       "2014-06-09 -0.005012  0.005668\n",
       "2014-06-10  0.004406 -0.000735\n",
       "2014-06-11  0.004760 -0.003761"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop nulls\n",
    "# YOUR CODE HERE\n",
    "algo_returns_df = algo_returns_df.dropna().astype(float)\n",
    "algo_returns_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## S&P 500 Returns\n",
    "\n",
    "Read the S&P500 Historic Closing Prices and create a new daily returns DataFrame from the data. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2012-10-01</td>\n",
       "      <td>$1444.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-02</td>\n",
       "      <td>$1445.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-03</td>\n",
       "      <td>$1450.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-04</td>\n",
       "      <td>$1461.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-05</td>\n",
       "      <td>$1460.93</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Close\n",
       "Date                \n",
       "2012-10-01  $1444.49\n",
       "2012-10-02  $1445.75\n",
       "2012-10-03  $1450.99\n",
       "2012-10-04  $1461.40\n",
       "2012-10-05  $1460.93"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading S&P 500 Closing Prices, sorting index\n",
    "sp500_history_csv = Path(\"Resources/sp500_history.csv\")\n",
    "# YOUR CODE HERE\n",
    "sp500_df = pd.read_csv(sp500_history_csv, index_col=\"Date\", infer_datetime_format=True, parse_dates=True)\n",
    "sp500_df.sort_values(\"Date\", ascending=True, inplace=True)\n",
    "\n",
    "sp500_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Close    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check Data Types\n",
    "# YOUR CODE HERE\n",
    "sp500_df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2012-10-01</td>\n",
       "      <td>1444.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-02</td>\n",
       "      <td>1445.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-03</td>\n",
       "      <td>1450.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-04</td>\n",
       "      <td>1461.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-05</td>\n",
       "      <td>1460.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-16</td>\n",
       "      <td>2907.06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-17</td>\n",
       "      <td>2900.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-18</td>\n",
       "      <td>2905.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-22</td>\n",
       "      <td>2907.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-23</td>\n",
       "      <td>2933.68</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1649 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              Close\n",
       "Date               \n",
       "2012-10-01  1444.49\n",
       "2012-10-02  1445.75\n",
       "2012-10-03  1450.99\n",
       "2012-10-04  1461.40\n",
       "2012-10-05  1460.93\n",
       "...             ...\n",
       "2019-04-16  2907.06\n",
       "2019-04-17  2900.45\n",
       "2019-04-18  2905.03\n",
       "2019-04-22  2907.97\n",
       "2019-04-23  2933.68\n",
       "\n",
       "[1649 rows x 1 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Fix Data Types\n",
    "# YOUR CODE HERE\n",
    "sp500_df['Close'] = sp500_df['Close'].str.replace('$', '').astype(float)\n",
    "sp500_df = sp500_df.dropna()\n",
    "sp500_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2012-10-01</td>\n",
       "      <td>1444.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-02</td>\n",
       "      <td>1445.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-03</td>\n",
       "      <td>1450.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-04</td>\n",
       "      <td>1461.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-05</td>\n",
       "      <td>1460.93</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             S&P500\n",
       "Date               \n",
       "2012-10-01  1444.49\n",
       "2012-10-02  1445.75\n",
       "2012-10-03  1450.99\n",
       "2012-10-04  1461.40\n",
       "2012-10-05  1460.93"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Rename Column\n",
    "# YOUR CODE HERE\n",
    "sp500_df = sp500_df.rename(columns={\n",
    "    \"Close\": \"S&P500\"\n",
    "})\n",
    "sp500_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2012-10-01</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-02</td>\n",
       "      <td>0.000872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-03</td>\n",
       "      <td>0.003624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-04</td>\n",
       "      <td>0.007174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-05</td>\n",
       "      <td>-0.000322</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-16</td>\n",
       "      <td>0.000509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-17</td>\n",
       "      <td>-0.002274</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-18</td>\n",
       "      <td>0.001579</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-22</td>\n",
       "      <td>0.001012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-23</td>\n",
       "      <td>0.008841</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1649 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              S&P500\n",
       "Date                \n",
       "2012-10-01       NaN\n",
       "2012-10-02  0.000872\n",
       "2012-10-03  0.003624\n",
       "2012-10-04  0.007174\n",
       "2012-10-05 -0.000322\n",
       "...              ...\n",
       "2019-04-16  0.000509\n",
       "2019-04-17 -0.002274\n",
       "2019-04-18  0.001579\n",
       "2019-04-22  0.001012\n",
       "2019-04-23  0.008841\n",
       "\n",
       "[1649 rows x 1 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate Daily Returns\n",
    "# YOUR CODE HERE\n",
    "sp500_daily_returns = sp500_df.pct_change()\n",
    "sp500_daily_returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2012-10-02</td>\n",
       "      <td>0.000872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-03</td>\n",
       "      <td>0.003624</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-04</td>\n",
       "      <td>0.007174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-05</td>\n",
       "      <td>-0.000322</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2012-10-08</td>\n",
       "      <td>-0.003457</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-16</td>\n",
       "      <td>0.000509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-17</td>\n",
       "      <td>-0.002274</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-18</td>\n",
       "      <td>0.001579</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-22</td>\n",
       "      <td>0.001012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-23</td>\n",
       "      <td>0.008841</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1648 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              S&P500\n",
       "Date                \n",
       "2012-10-02  0.000872\n",
       "2012-10-03  0.003624\n",
       "2012-10-04  0.007174\n",
       "2012-10-05 -0.000322\n",
       "2012-10-08 -0.003457\n",
       "...              ...\n",
       "2019-04-16  0.000509\n",
       "2019-04-17 -0.002274\n",
       "2019-04-18  0.001579\n",
       "2019-04-22  0.001012\n",
       "2019-04-23  0.008841\n",
       "\n",
       "[1648 rows x 1 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop nulls\n",
    "# YOUR CODE HERE\n",
    "sp500_daily_returns = sp500_daily_returns.dropna()\n",
    "sp500_daily_returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Combine Whale, Algorithmic, and S&P 500 Returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Concatenate all DataFrames into a single DataFrame\n",
    "# YOUR CODE HERE\n",
    "combined_daily_returns_df = pd.concat([whale_returns_df, algo_returns_df, sp500_daily_returns], axis=\"columns\", join=\"inner\")\n",
    "combined_daily_returns_df.sort_values(\"Date\", ascending=True, inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SOROS FUND MANAGEMENT LLC</th>\n",
       "      <th>PAULSON &amp; CO.INC.</th>\n",
       "      <th>TIGER GLOBAL MANAGEMENT LLC</th>\n",
       "      <th>BERKSHIRE HATHAWAY INC</th>\n",
       "      <th>Algo 1</th>\n",
       "      <th>Algo 2</th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2015-03-03</td>\n",
       "      <td>-0.001266</td>\n",
       "      <td>-0.004981</td>\n",
       "      <td>-0.000496</td>\n",
       "      <td>-0.006569</td>\n",
       "      <td>-0.001942</td>\n",
       "      <td>-0.000949</td>\n",
       "      <td>-0.004539</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-04</td>\n",
       "      <td>0.002230</td>\n",
       "      <td>0.003241</td>\n",
       "      <td>-0.002534</td>\n",
       "      <td>0.004213</td>\n",
       "      <td>-0.008589</td>\n",
       "      <td>0.002416</td>\n",
       "      <td>-0.004389</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-05</td>\n",
       "      <td>0.004016</td>\n",
       "      <td>0.004076</td>\n",
       "      <td>0.002355</td>\n",
       "      <td>0.006726</td>\n",
       "      <td>-0.000955</td>\n",
       "      <td>0.004323</td>\n",
       "      <td>0.001196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-06</td>\n",
       "      <td>-0.007905</td>\n",
       "      <td>-0.003574</td>\n",
       "      <td>-0.008481</td>\n",
       "      <td>-0.013098</td>\n",
       "      <td>-0.004957</td>\n",
       "      <td>-0.011460</td>\n",
       "      <td>-0.014174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-09</td>\n",
       "      <td>0.000582</td>\n",
       "      <td>0.004225</td>\n",
       "      <td>0.005843</td>\n",
       "      <td>-0.001652</td>\n",
       "      <td>-0.005447</td>\n",
       "      <td>0.001303</td>\n",
       "      <td>0.003944</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-16</td>\n",
       "      <td>0.002699</td>\n",
       "      <td>0.000388</td>\n",
       "      <td>-0.000831</td>\n",
       "      <td>0.000837</td>\n",
       "      <td>-0.006945</td>\n",
       "      <td>0.002899</td>\n",
       "      <td>0.000509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-17</td>\n",
       "      <td>-0.002897</td>\n",
       "      <td>-0.006467</td>\n",
       "      <td>-0.004409</td>\n",
       "      <td>0.003222</td>\n",
       "      <td>-0.010301</td>\n",
       "      <td>-0.005228</td>\n",
       "      <td>-0.002274</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-18</td>\n",
       "      <td>0.001448</td>\n",
       "      <td>0.001222</td>\n",
       "      <td>0.000582</td>\n",
       "      <td>0.001916</td>\n",
       "      <td>-0.000588</td>\n",
       "      <td>-0.001229</td>\n",
       "      <td>0.001579</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-22</td>\n",
       "      <td>-0.002586</td>\n",
       "      <td>-0.007333</td>\n",
       "      <td>-0.003640</td>\n",
       "      <td>-0.001088</td>\n",
       "      <td>0.000677</td>\n",
       "      <td>-0.001936</td>\n",
       "      <td>0.001012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-23</td>\n",
       "      <td>0.007167</td>\n",
       "      <td>0.003485</td>\n",
       "      <td>0.006472</td>\n",
       "      <td>0.013278</td>\n",
       "      <td>0.004969</td>\n",
       "      <td>0.009622</td>\n",
       "      <td>0.008841</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1043 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            SOROS FUND MANAGEMENT LLC  PAULSON & CO.INC.   \\\n",
       "Date                                                        \n",
       "2015-03-03                  -0.001266           -0.004981   \n",
       "2015-03-04                   0.002230            0.003241   \n",
       "2015-03-05                   0.004016            0.004076   \n",
       "2015-03-06                  -0.007905           -0.003574   \n",
       "2015-03-09                   0.000582            0.004225   \n",
       "...                               ...                 ...   \n",
       "2019-04-16                   0.002699            0.000388   \n",
       "2019-04-17                  -0.002897           -0.006467   \n",
       "2019-04-18                   0.001448            0.001222   \n",
       "2019-04-22                  -0.002586           -0.007333   \n",
       "2019-04-23                   0.007167            0.003485   \n",
       "\n",
       "            TIGER GLOBAL MANAGEMENT LLC  BERKSHIRE HATHAWAY INC    Algo 1  \\\n",
       "Date                                                                        \n",
       "2015-03-03                    -0.000496               -0.006569 -0.001942   \n",
       "2015-03-04                    -0.002534                0.004213 -0.008589   \n",
       "2015-03-05                     0.002355                0.006726 -0.000955   \n",
       "2015-03-06                    -0.008481               -0.013098 -0.004957   \n",
       "2015-03-09                     0.005843               -0.001652 -0.005447   \n",
       "...                                 ...                     ...       ...   \n",
       "2019-04-16                    -0.000831                0.000837 -0.006945   \n",
       "2019-04-17                    -0.004409                0.003222 -0.010301   \n",
       "2019-04-18                     0.000582                0.001916 -0.000588   \n",
       "2019-04-22                    -0.003640               -0.001088  0.000677   \n",
       "2019-04-23                     0.006472                0.013278  0.004969   \n",
       "\n",
       "              Algo 2    S&P500  \n",
       "Date                            \n",
       "2015-03-03 -0.000949 -0.004539  \n",
       "2015-03-04  0.002416 -0.004389  \n",
       "2015-03-05  0.004323  0.001196  \n",
       "2015-03-06 -0.011460 -0.014174  \n",
       "2015-03-09  0.001303  0.003944  \n",
       "...              ...       ...  \n",
       "2019-04-16  0.002899  0.000509  \n",
       "2019-04-17 -0.005228 -0.002274  \n",
       "2019-04-18 -0.001229  0.001579  \n",
       "2019-04-22 -0.001936  0.001012  \n",
       "2019-04-23  0.009622  0.008841  \n",
       "\n",
       "[1043 rows x 7 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Combined daily returns\n",
    "combined_daily_returns_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Portfolio Analysis\n",
    "\n",
    "#In this section, you will calculate and visualize performance and risk metrics for the portfolios.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Performance\n",
    "\n",
    "Calculate and Plot the daily returns and cumulative returns. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21a03393f08>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3kAAAFmCAYAAADQ71OyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOydd5glVZn/v1U3dZw8QxwYEEQQBBVR10VEDLuKYUXUn4Ku7q7CmsOquIRdgi6CogSVJElyHiTNkGYYJjA55+6ezun2zaHCOef3R51KN3XfDnT3nffzPPPMTFXdqnPrVp1zvudNihACBEEQBEEQBEEQRG2gTnYDCIIgCIIgCIIgiPGDRB5BEARBEARBEEQNQSKPIAiCIAiCIAiihiCRRxAEQRAEQRAEUUOQyCMIgiAIgiAIgqghSOQRBEEQBEEQBEHUEMHJbsBomDdvnli0aNFkN4MgCIIgCIIgCGJSWL9+/aAQYn6pfdNS5C1atAjr1q2b7GYQBEEQBEEQBEFMCoqiHCi3j9w1CYIgCIIgCIIgaggSeQRBEARBEARBEDUEiTyCIAiCIAiCIIgagkQeQRAEQRAEQRBEDUEijyAIgiAIgiAIooYgkUcQBEEQBEEQBFFDkMgjCIIgCIIgCIKoIUjkEQRBEARBEARB1BAk8giCIAiCIAiCIGoIEnkEQRAEQRAEQRA1BIk8giAIoiYRQuDSFZdiQ9+GyW4KQRAEQbylkMgjCIIgahKTm3h6/9NY07NmsptCEARBEG8pJPIIgiCImkRAAAAMbkxySwiCIAjirYVEHkEQBFGT2CLPFOYkt4QgCIIg3lpI5BEEQRA1iRBS5HESeQRBEMTBBYk8giAIoiZxLHkk8giCIIiDDBJ5BEEQRE1iW/IoJo8gCII42CCRRxAEQdQ0ZMkjCIIgDjZI5BEEQRA1CblrEgRBEAcrJPIIgiCImoQSrxAEQRAHKyTyCIIgiJqELHkEQRDEwQqJPIIgCKImIZFHEARBHKyQyCMIgiBqEie7pqDsmgRBEMTBBYk8giAIoqYhSx5BEARxsEEijyAIgqhJHEseI0seQRAEcXBBIo8gCIKoSZyYPEGWPIIgCOLggkQeQRAEUZNQ4hWCIAjiYIVEHkEQBFGTUJ08giAI4mCFRB5BEARRk5AljyAIgjhYIZFHEARB1DQk8giCIIiDDRJ5BEEQRE1C7poEQRDEwQqJPIIgCKImIXdNgiAI4mCFRB5BEARRkzh18jjVySMIgiAOLkjkEQRBEDUJWfIIgiAODoQQyKxe7SzuESTyCIIgiBqHiqETBEHUNrmNG9H+r99Eftu2yW7KlIFEHkEQBFGTcMEBkLsmQRBELcE1Df2/vwE8n3e3ZXMAAJZMTlazphwk8giCIIiaxOuuSS48BEEQtcHQPfcietttGLr7HnejXNQTmj5JrZp6kMgjCIIgahKvsGOCTWJLCIIgiPFCaJr1t+Hx0pD9vdC1yWjSlIREHkEQBFGT2JY8gJKvEARB1AylPDNskaeRyLMhkUcQBEHUJp55AIk8giCIWkF27oribpEij5PIcyCRRxAEQdQkXkseJV8hCIKoDRxXfMWzkdvumtTX25DIIwiCIGoSctckCIKoQUSxJc+27pG7pguJPIIgCKIm8SZeIZFHEMRU4bmW5/C157422c2YvjgazyPyKPFKESTyCIIgiJqELHkEQUxF9sb3YsvAFirtMlpKWfIoJq8IEnkEQRBETeKLyRMUp0EQxNTALulCpV1GiSOOPYlXONXJK2RcRJ6iKP+kKMpuRVH2KYryyxL7I4qiPCz3r1EUZZHcvkhRlJyiKJvkn7+MR3sIgiAIgrJrEgQxFbEteNQvjSOyv6eYPJfgWE+gKEoAwC0APg6gE8BaRVEWCyF2eA77NwAxIcRxiqJ8BcC1AL4s9+0XQpw21nYQBEEQhBdy1yQIYirChWV1qnVLXuvmAcw5vBEz5zdM/MVsd02KyXMYD0veGQD2CSFahBA6gIcAfK7gmM8BuEf++zEA5yi+aEmCIAiCGF8o8QpBEFMRW+TVer/03J+34v4r1kzAmQUQCDsxeXve7MV9T4WghWeQu6aH8RB5RwDo8Py/U24reYwQwgSQADBX7jtGUZSNiqIsUxTlzHIXURTl24qirFMUZd3AwMA4NJsgCIKoZahOHkEQU5GDReQBgODjn1yGa81o/szNYPlGAMD217sBANmGQ8hd08N4iLxSFrnCX7TcMT0AjhJCvBvATwA8oCjKjFIXEULcJoQ4XQhx+vz588fUYIKYzgjDQP/114PF45PdFIKY0pC7JkEQU5GDSeRNBNxotv7OW26gjteGECTyPIyHyOsEsNDz/yMBdJc7RlGUIICZAIaEEJoQIgoAQoj1APYDePs4tIkgapbkkiWI3nEn+q6/frKbQhBTGnLXJAhiKmIvQJmC+qVRYVdQsP/L7f8LisnzMB4iby2A4xVFOUZRlDCArwBYXHDMYgDfkP/+IoBXhBBCUZT5MnELFEU5FsDxAFrGoU0EUbM4/uYGDQ4EMVJI5BEEMVVwEq/w2k68MnH46+TZC3qK4BST52HM2TWFEKaiKN8D8CKAAIC/CiG2K4pyJYB1QojFAO4EcJ+iKPsADMESggDwYQBXKopiAmAALhJCDI21TQRR09iDQiAwue0giCkOuWsSBDEVIXfNMVIQFOY4bZC7po8xizwAEEI8B+C5gm2Xe/6dB3B+ic89DuDx8WgDQRwsCNMSeUpgXMpcEkTN4nXXpGLoBEFMFWyRV8sJobz978Sh2BeT/xMQ5K7pQLNEgphu2M7nKlnyCKISZMkjCGIqcjDUyZuIrJqes/v/Z+ddURRwctd0IJFHENMMwazBQSF3TYKoCIk8giCmIk7ilRrul95aQ551MQGV3DU9kMgjiOkGk4MCiTyCqIxnklHLblEEcbBwz/Z7sLJ75WQ3Y8zYFjyy5I2OdN7qz+NZQ15LXlMhkeeFRB5BTDOEYXVqikqvL0FUgix5BFFb3LP9Hjzb8uxkN2PMHAyJVybSkpfSrPuWyEmRZ1vyFBVcJ3dNG5olEgcNRm8vBHNXzba82omVj++bxBaNDp6Xq1Qk8giiIlQnjyBqCyYYcmZuspsxZuy+qZY9DCY0Js+JwZN/25ciS54PmiUSoyL9+goYXV2T3YwRwxIJ7P/EJ5F66WVn2+sP78HGpe2T2KrRIfLWACdMmrQSRCXIkkcQtYXJTWTN7GQ3Y8wcDHXyJja7pl0Xz1Z7riUPjNH8SEIij6ganjfR9bMr0fqF8ya7KSOGxeMQug42FJ3spowZnssDAIRBLgkEUQkSeQRRWzDBkDfzk92MMTNd3TX7b/gDdr//AyM69i1JvCL7eDe7piVrBLlsAiCRR4yCwbu3ofHsy8ASycluyojh0nwvjOnVoZaCa1Lk6bXr5kEQ4wG5axJEbcF4bbhrTtcSCtFbbwVPJAAA5uAg2r52AcyBgZLHTmwJBQtFXoJzN7sm4M75DnZI5BFVo3ekrX8EQpPbkCqwfbS9MXnTFeFY8kjkEUQlvJa8Wo59IYiDhZqx5GF6WvK8xB58CLn16xF78KGS+ytZ8qJ33onk0qWjv7h97iJ3TStIjyx5FiTyiKqR1nAokfrJbUgViLwURub0n+hx+7tQJ0YQFfFZ8sT0nUwRBGFBiVemD5UsebEHHkTq+RdGfW7F+bvQXdMqLUXJVyxI5BHVI98utXHG5LajCrgmBVENBOM6gpUseQRREZ8lj9H7QhDTGS44uOA1IfJqok6eolTcXSnxitB1CM5Hf+0CS54tKB1LHok8AEBwshtATEPk0oDa0Diiw81oFEqkDoGm4uMF5xi44QYooRBmfv7zCB911Hi21L2OHcdmTuMOVUKWPIIYGRSTRxC1gy2IasFd0+6bpnW/NExmFV7Bksd1HWBj+e7C97e3hALgWdg/yCGRR4wC621S65tGdPTeD/0jQgsX4rilS4r25TZtQvT2O5z/z//BD8aniQU4wqgWLHk5WUJhhJa8bFJHcjCHQ4+dOZHNIogphy+7JrlrEsS0xk5Wkmd5cMGhKtPXGW26ZtesigoaUOg6BBu7JU/xWPQCAOYt+iAwuBlCJ0seQO6axKiwXkylfmSWPAAwOjrKnMp9yVkqPaZWVULYqzpjWjmaGlRryXvkmjfx+G/XT2STCGLKU9OTKYI4CPDWlJvu1jw78cq0dtcchkqWPKFpwJgS4fkteVwAc4IKZh92MgKzjyF3TQmJPGIUWJ2TWoXIK4vqPoI8OXElGRx3zRoooVBtTF4mQW4LxMShM33KCihy1ySI2sFrjZ/ucXkHsyVPmCbA+ZiyndtF0AuLoQOAEqyjEgoSEnlE9ciVJ6WuYezn8gTusvTEWfJ4vnZKKFBMHjGVeO/f3otvvvDNyW5GSagYOkHUDl5LHom8iWfob/ej5fP/UnJfpaQqNuUsec7chY9hPlZwfcHdjJsI1rneWwc5FJNHVI8UecnQYcMfOkwMnOIReRNryZMir0IJhWhXGoGQilkLxkG8TiAk8oipxqaBTZPdhJKQyCOmO0ZXF+JPP415F1/sGy8PRryujdNd5E3lxCt9110HJRRC9C+3lj9oBJkxywlB7szHRi/yhBTJkH8LIdyyCsEIxeRJyJJHVI9cfdnDTxz+0PwwL5rHXXNCLXna8IlXHrrqTdx/+eoJa8N4IIRw3TXLiDyjtxfRv95V1MFWqllDELUIuWsS053ki0sweONNYLHYZDdl0qmpmDzbkjcFE0Ll1q1Hdu26ygeNxCuqnLumbi22izFY8jLcmi8m9SHrXAIQcpsRaaCYPAmJPKJqhKw3NZKHx46FK4vXkpdKjaFVw7TDFpvTvISCMAxnBa3cKlnn976P/t/+FkZnp297pSBoYmRs6t+E36///WQ3Y0LR29trxkrsq5NXw0WHidqFp61xsRYyQ4+VWrLk2SKPjcVlcYIQjDlZvMseIwSETGRXTqyVd9cc+3zMObNdH08IQGQBAHpdI8XkSUjkEVWTzMUBAIEReI4Mu5riESpsIkWe4x4wvQdKX8dbZiWNpSy318LvSpa8sfNqx6u4a9tdU3JgHg9YKoX9n/gkei67fLKbMj54Hnmy5BHTESfr9DQfu8YDisl7axCMDS+SOIcwDGTrFyCWKhP5VdaSZy0ijqUYuur8bS96A4pdMy9cX3VM3rq2ISz65bPojk/v56oQEnlE1RiGZZ1TMbzKG85d05sIhadSIwrmHQ2Ou+Y0L6HgvZ+OT3oBSpnfpf/PtyH1yitjboPR1YXcli1jPs90xJ5kTPcJRjlsV+D0ihWT3JLxwbbkhdQQWfKIaQmXYQzTfYFyPPBZ8tj07oPtEgpT0V0TpulbUC45L+McQjew+v1X4KWuk0qeZrjEK/ktW9D5/dHVRlalfFFsGeO5lgjVVx2Td/+adgDAqv3RUbVnqkIij6ge+TKpI7LkDeOu6V3J4RwslRlDwyq0w3HXLO5QJ8vCJYTA/g39yCZHvuIk8lbHqzQ0+Do1+3yVRHLsiSeQevHF0TXWw75zPoa2L315zOeZjtgDcq2KPAQC1t81kIUW8Iu8KTmZIohhcN01p9c7mdsRRf8tm8Z1fPWJPGN698FTOfGKYMxJ8Aag5HgghIAw/HMXMxZD9K67ne9Wbj7i9fBKLV06qjbai9n2315LHoKRqt01z73rKly484VK9dunJSTyiKpRmfUaBEZwrK+jKIFtyWNqCLuP/xLuumwd8unxX3G3V3VKDZR8gqyHw7HllU68cNs2bFvmxs4N5YcqCjX7fqoNDUUd70UvXYT3/O097oaC0wgO8Gx27A2vEp3pOJA88JZfdyKwB+SsOX738Y6td+CUe06ZUi6gY3GjmUrY71I4EJ6SkymCGA7bXbNSZuhSaC2tk/oe611p6B2posXIseB9h/NseidesQXrVOyXBDN9c7eSz5G05HnpufQy9F97LXIbN8nPlT4/H4eY7yKR53nOlFGUUJgx1Isj0gMT5k02WZDII6pGkS9uKUueYBzZTf3uSs5I/LoBbDz1B+g64izoGkcuPf5JH5w6eaVcXt6icXCgPYWX797hdEZDvZbVkplWA6K5KP7pgY9hRVd5VznhEXmFndHK7pUFA4Z/P+cCPPPWi7yrVl+Fc588Fwkt8ZZfe7xxRJ4xfvfxL5v/AmCKJAaxB/NatORNwckUQQyH7a5ZzTup7d2Llk99CtFbK6TAn2C07h4A47tgVJOJV8QU7GtN5sw1AJR+9mRMnhcWj8t/yIQsZS154yvyhBDgXDiWPCUYqTq7piI4ImwKjMHjDIk8ompsX+hSlrz8nhiGHtoNo8cSMCOx5HE1hOTMY9GQ6bU+w8Z/JcUpO1BiNXSklrzc1m3ov/76Ua/0PPfnLdi1uhfpuNX5mJpcydOtzr6/swMP7boWseV7yp6D56zvkQ8BhjlMJ1bQMQsuxmzJG03GqlXdqwCMTBjl9+yBOYVThdtCbDwnGPZgz8ste76FCCaD2GtE5NmQyCOmK3bW6Wpi8oweS2BlN2yckDaNhL49Vty2kRs/i1stJV6Z6u6a3lAae1zwHSMEmF7Qdvsz0u2/nKtuoZvnaFCcmDzFmTPadodAIFK1tVDlAmFmkLsmQSjCeoFLWfJ43uqEhbRO2bFwqaYjEe0qUQePc3DVyswUNlJy0/i/ZrwgZa+38xlpzEDb+ecjesedIyoCOhJscWfqVpvy/QmE1TqE+8tPsLmMydurtUM3PO4UHuGpzjkFzZ+/DTzv74D5OLhrmnLyMBrECLrP1s9+Dq1fOG/U1ygk9dprMPr7x+18E+GuOZVWdDlj2PSu7yLWuGhkxwuOz6zhePe+yReopbDfi1CARB4xPWEZa8FUGFU8v/Z4MIm107khFzHH0Tri7SOnfZ086UI0JTw4CihMUHfjuhvwQusL/oMYg64X1uKVv4/ixsmVPP84lDfwWvIcw4AiQ4nUCLRcdXWXFc4sS16NqTwSeURVCF2HIm14SomXQUjrlP2i2IlX9h73Rax4dG/xBzgHV0MAgACz0+pOhCXPdddMvfQSsrt2u/sKrtf+ne9Aa2ktf7JxsnKYOgPT9yGXttwYmfRvVyr0fyKvQQCI1zf4OtCY5lq/Aod8yDpf0j94CM7HLPLsCUc1KLLDH+kkeyxC0ovo2YnOiy5Gx7/9+7icD7AGp9kpMa7umlOpXlI+qWNozknYdsLXR3Q8EwwXvsJxyaNTVORRdk1imuPUj60iM/RUiCtSZHfG9IkRedPdkjeV+v0iCnIXvNy2FK93ve7bJjiHZroSoivdhVjWykypqKo8pnJ2zci7v466d3/D+vxPfor0smUjb6PiZtfk0tJoz0lDahipTHLk54LrrjmSxejpBIk8oiq4rkOodga+zqL9Qlql7GBrOxaOqSFo2RKZLRkHVyxLnsqsYyfCkue4azKG3iuvwuDtd7r7CuanmWXLkdu4ofy5xijy7AFYz2swMovRsvZ27IntwUCyDwCgGJUSr+TQNbsZQw2HIdrc6GwfyA54rwAA6L/uOvRcfoXnuuOQeMUY/YCts7e2wLZ509kArPiU6J13DnP0yHjHK624/g6G3DiKPHtQmQxLXm7bIPr+uMEdjOUoKUY4NEzJCYoHx5JH7prENEToumP1iD34IOKPPzGyz9kxT8rwpry0ZmLRL5/FY+uLx/OxoDDr2nwcyxbVkrtmpTp5WSOLe7ffO2ku/HYcZbJpITqOPBtgvNhyKgR0j8i7aOlF6El1Wf+Rc8Ryiw22K2X46H9E6OgPgWsaks89h+z68vOuonMEmqy/1WYw03+doBJGOu9fkDYHKidVUTm33DVHOP0Uuo7uX/wCeuf4vjfjDYk8ojo4B5d+mgovXimxRZ49aXSKkKsB6LlSSU8YBuedAgAIcGnJm4CYPLtTEaYBoevQulxrUSlRySvEEYxa5BWMt4YciPXsIM5bfB4W734aABDQyw/MWiqJXYfNAQDkQiF3O/OY/2QvZXR1Q9u3z908Du6a3riQka4W224VOq8s8sZ79ZllXUGa27q16s+bAwNFcTCRVB7NeSCfHv8kMpMh8nr2HoDRk8GjOx6xNsjBXSgjyZ07NeIIK+FY8shdk5iGeD0nks89j/gjj4zoczxn9fPlaqZ62dNnWQrvXdU24nZlVq6E1lrB2wWAIqTIqzIraCW8ZVBqReSV6vdv2ngTrlt3HZYeGF15gTEjxz3+4f/GSaf/PwjOihdpOfdVpErpKUQiC1D33n8DnIyXpU9fmHhly9I2VPxACRTbkqeonpg86++gGkLGU1M4v2MH9p75YcQfe8x3jtQrryB651+tz0p3TXOERga9swuJpxcjM8VrypLII6qDczAp8lQlUrzbtuTZ2TWlIBJKAHq+eJI1FOPYe/yXAACBUVjy9FwWmfjwiTqcTFEmgzAM6N2uyPOKiyCAhrMvA4tX6GzGWpRWXs7I53HCzDPQFLJEW5hbFk3o5V/Ljds3Qg8GAHDkwpbIiz3yCNibboC9sNOFKooTwwcAQlEh8vkxWSJ92bSqPM+wlrwy5+OMI9ZbvZvoQKYRHbObAQBabKiqz7J0GnvP/DD6fv0b33ZFurEYyXjV7RmOyRBMBwas0hZ7Bi33ZW7HrKojE3lTvfYcZdf0k1nzJrp+8pMp4c5X6/i9K0aH46opcbIXDvc5ezFvBJa8ob0tODHahgXNxeN5Obov+RWit99R8RiVW+MYH8f6ft4+slqRpzMdfZm+cWtLVdc+cACxh/0CvVLiFTvmO61XF1c2XthzhIVhORdhvLhkBec+C1pdsA4Lj/06QgvfD2NgmOyaBUlRBtqtRdNqMrHaCxgq4Lhretc0NI+xQNvfAgDIrlrtO0di8TMYuu8+66OCI8wNGCWSzJREWqjNoermFm81JPKIqhBCQPbdUNVIkc+1kMlEnLIEdipdRYWeL+7sTZ0jLF9MheXB9H1Vibx7f/59/OU7FwIAtKyBNx7b65Qk8GJnhRSmCWEYYAl38PTOretUIDBzIVi6/CR3tCKpcFU1lY3jtDln46iGE3D6zlk4rnsGACBki70CBre3oiH1Nhwdz4OruiPyBm/5E9RnX/U00Ha9UyE8FkkhV754bvQroF6RV022N2D4APPCdMw2+zcO4KEr36yqaDwAPJ08CVuPWgCmADxZnX++PblKvfyyb7st8vTU+FvyJkOEpOLynjN/rSH7WSlEb29H63lfdDKg8qleT0++CmE1POUF6VtBZsXrSD73PPp/e13N1EKcCAxu4IW2F0Ythld0rcBHH/0olncuH1M7WKHIS4ys3xF2Hz8CkXfEdy/A71+/GfOb60bcLp7NDtsWVSZo41WMEyxdeTHPdtesD9ZXLfJ+sfwX+NhjH5uUBY62L38FvVdc4XvnKtXJC8k8BYVjpjk0hI6LLoY5ODiBrS2e4wiz2JInhAAXCoTQIHgO9YF6J+Ol3fGWTbyiFyQesK29Vcz93PmUUmTJAwAk8tj5jhOt31u1E8H4+zyezYBLa7nKrZg8vcT8seR3sGs8D1U2MmTWvIn0G2+M6JwTAYk8ojo4h1DsrEYqmMnBNQYma9vZiVecOnm2ZUBRwQwOxji0llb0/+53EEJA1QX+eWYIx0VUpINRhLVlSA/6syFuG9yGlkSLpw0MSFh+0Il+d2Vu1ZP7semlDuxbX5xNURSIPO8k1tvp292GY5Esgf2dNvVvwrMtz5Y9zguLx53yDfbl7EKiASWEk1tnYn6qAQAQEqVFXnTtfhzbfCpOnHs2goFTkamrt9IYx2IFnbIr8rhWQuQNUyuv46KLEXv00ZL7/CKvekve2t61WNK2xH9OITD0t/vBypRO0DIGOBfIpUYX05cLh8CTqaLthsaczKZF2IOxWtBFyu9spqoTjYA1QOd37Ci7fzLcNQOGdHkZsJ4J7nlfSxG9/Xbkt29HaqnlRjQVMoJWwuuuSYlXXEvQ0F13Ifvm2kluzdTlzq134r+W/Rdean9pVJ/fNrgNgDVGAJZ4STz9dNXn4QWihyWTIxLnTh9fhaCZ0+i6//dl+rA3ViJRmkRoWpGVsRC71BIf4aJo8sUl2HP66cht2+5sM2Mx9F7za8fyYy/UNIWaqs6uaf+W5foswTliDz00qjJBw+HWj3Ov7VjySiw+BWXG8cI+K/PGSqRfew35nTvHvY0+CoS5YqqOJU+deRRCR59phe4IBVr8VmiJP6M+0OAuKthznGESrzjYyXmqWXhy5qEAK0i8AgAsbOUsEIbhJIIpzKnCs1nwTAaCcyhCIMI0pPQRLqSYtsirbMkbvOUWDN50s29bV7oLp9xzitM/TCQk8mqI5ItLRuzOMWo4d3yhVQUwDY7+Gzeg5+o1AIoTrwjHkmet6hl5ho6LL0L09jtgdndDlf3pISEFc+YsxKeO/DaMpF+E/L9n/x8+99Tn3A27/g7c+G4g41/NymesjkIN+FcvhWE4navR3g4IAe6JORJcOB2u88kKyU9s6+SFz1+IX77+y7KHJV9cgtxWa7Bv+/JXYPZZgtS+VkDeqoDs0FXZprAIlzyfPbjPWHgmZoRmwwhGwNNpCF0H597BQ3Z4atBnyds9P4j2Oc3g2cqrpdm1a5HfssXdsOFe4LrjACEK3DVHtkLrxOQxHd968Vv46bKf+vYb7e3ou/pqJP5eWjAzuUqnlYrprMBh4Tk4fsZ7kImESk5IbvvhMtx36aqSn7WtlHZmUMEYBGNQ5HPEU9W70bR+4byK5SEmQzA1Zq17O/eZDkQ7O8BN25JX2pJduApumm9tMp1qsd27bHfNg91N0Ts+lLOcH8wY3d1ILl2KwZw1tlRyuUzrabzZ82bJfQH5/tiLDH1XX43uX/wSuU3VTep4uqDf4hw8mYQZiyH1UnkBantrlKpTq7X3gWslfnvP83DzppvxvZe/V/LcQggIk4OlK/eBqszCzSrE5HmtgZkVVvbG/HZX5PVffz1i992H5IsvWsfLca4x1DjqmLxybvGpJUvQ+z//i8GbbhrVeUeCV6DbJRQqWfIK99nirlovmmoQnBctDoSY6ljyGs++FHXvvhCCMTCoAKy21AcaXEueImu/Fgj8wdtuR/t/fLtYSDsL4HDs1FEAACAASURBVP7fxujtLSu6fSUUTAFmdIAbbo1hFq63zqnrTibOQhHJM1nrnZLuzQEBtCXXlLxeEba7ph0KMrgPSHQVH5ZOFYlau3bwE3tHlkhpLJDIqxGMvn50/fCH6Pzhjyb0OoILJ/OeAqsMgBl1BxLHAua4a0rLgPyMnjMBu+Ay54hm3M8eMvM4qIoKkas8+cjt2I/ON2ZCDOz3b0/FIYSGUNg/QS3VSXgtFZwLZ8XJXojiFUSeYAzRXBTv6j4bH97/pbLHdf3wh2g7/3wAlk++CqBZdUVlQF4zKLOL2hODMMqIPGZnPuQ4fda7AKhgUStl8VDKHfCYnFhwNeAb5OMNCqLNDeDZLFJDg+jc5Q6mvusYht/at/gHyKey2PlGF7in+Gm1A025xCv2ZNPs7S29X96nkol7KnDC7I/hPXM/DvXQdwGpNATnEELg73/8Ldq3WSK2nAuo0ynLFcCeSy9D189+BtWu/zjMBKcU5b6fzWRkqmw03QWG9FB05C588kXhU1woeGPygKlteTQHBxG9++4JLURveqzl9gKcqbMJKVszHYk9+ii6fvgjhKWrYSXr7/898j0s//m/YjBb7DpnLw45LnkDllhk1bqNp9PondmIJScvArPPGY9j/49+hFWX/8o5b9Hn5KRVFLjmG9EkBv60Bz1XPe5sOzB3BjYdtQCqR1CmtRR6Ul3IGMULgkLT0HDmz6E2n1657WpYtjfhuMR5ye/cgX3/9FXEHnmw/EnkGGO/E7ZAaw43j1rklesDuOzTzWHc78aEV+RVKKFQzl1T2zXxIg+miXTDYcg0HOJsCrBAyeyaGU+dvHql3jEAOHO8gmLp2r69yO/c6XgxOaeyi6N76xcLgX0fORtdP/UvCts4iVeku6aZW+68dwDAvSLPLupcwl0T8IdzKDqDOTCA7IbKmT4dd82oFHk3vxe44aSi43g6U1T83R6XlBG4U48VEnm1gnx49ZaWYQ4c84WcCZ4KBbmU/2XVpeUob1gdsDAZUo1HQKubbe3PMyAga6iYJpSM1aHWKQLz6xbKY/znbM4EUZ93hVt03ftgHnkJtD1+kdK57R6YuRUIBP2PtbfwZui4j0NtPtzvrsmF8+47ft4lxoGu2U1Y/vYjwQ0DyzuX4x8OfB4n9X+o1E0qyTtnzcJHZ4TAcyaYyaHKFz2gWB26Y8lTikUez+fBs9Y9PRBtw9zIbHz0sPOhD1qDfCrrfseM7NDykTrfIH/6Iediwfz3Q2SzuOvHF+PhK35RdB0hBA4012HQG3OmBtCS/wBe+dseJBMei+EI3TXtjkzPl3aDsAcso690ULztb1+qBEclNNPqfBvmvMOy3qbTMA0du1cux/71xat1ekcHev7rR5bILUhBrre0wOjqdmLyRHr0WUrLWZPeagGSNxgauaxRqQQgOBs+SUKhJU8be4a71GuvIbtx4/AHjoJCkTeZLpvZDRuQXl4+Riv10svo/79ri+JAxxOfpwdj0PMmbv3BMqx5ZqLHjemB0HWAc9TnyyfFsPmnm9fh02sF8t0dRfvsBTs7ZlUJWosp1U7OWSqNHYfPhRkIIB+SlrF4HG+kBrB14QIk+8v0mVLkFcZfs2Ra7p8JABh8+hlsP3I+umc3Q/GIvDOfGsDvnnk72pJtRecWmga1cR4QnFm58dJDJfN/N6L3178u2p157kU0nvVLZF4egeuh7HZs18bGUOOoi6GXElXP7H8GB5LtozpfNQhWLPJKuWuW6q+EEMjvkPdqAheCBGN484xLseaMy51tESPsz+Atj0trnsQrqivy7EUjVuiWyTiEppVw17RFnnt/7MXf9Eul+0PHkqcoVuIVocGbeUWEvJY8f8y5jf2eeGNfFc3A4G23o+Pi/yx5Xef8ZoElrww8kykWtY7nGIm8MdGzP4F43/jVs5rS2A9x4csz3nDuTNoVBcgk/C9+Wq4UH+iwsvUJZmLt+37l7NfzJhQ7cx/nELLDbQoEnPPGC6wk5y07Al9+5UjftuC8t8PsbPNtM7Q4BM8WJW5xMmsGIqg7+Xw0nHWJzx1NCDejp/3KCVb8amw+6hCk6yMQhoGVLSM06XuYHbbEG9cYTJ0jIDt525Jnu7eUEnldP/kpMqssE39rTkPGzKEh2AxtYAAt82cio3hWqOR5ecAf27egYRFmNh8Dns3CyJeZnDOGbUfOx0tJj9VJUWFKF9J02nOdKusfmW2vI2wIZwLlNNeOcytj6bJF3kgtefbgYA+D4ToreylLJMAMA4uaTobWX7yi3vPdryP+zIvIvrLYY8mTq+fpNIRhOJY8NTMGcVNmorcvvg896fEpBD8SuuI5RGBl1FMRABd82PIlGVYHPdTkvKsD+/dDl4s25VzXKrLhXvRdecWwmfps8gbDr57ciqHMCPu5fqsfCgVKuz+9lRz46tfQ8e3vlN1vZ8KN3XvfhLWBxd2FFmEyx8V99+rKVmab9BtvYP8/f8opSVNzyEl4vbwvlZ6XgJ1jrMSijWrHP9suLSEp8ozqnj+eToHbY7v824zHkVcrlycoJ/LUoBz3FAUspWP39X9093lE3tv4+3HCsRejLVpcJoHnNUANA2pd5bpjclzjiRTMHqtfO5A8gId3PWx9H0PGAAbnyU/Y1hbvOf3bbIE2npY8k5u4evXVWNNT/ZheNR6BWalOnhOTx9zf1+zrcxZpqn2OqqGUJ0FIhIpEHucC73nHOTjnsAsAAPWIuO6atiWvwC04Y4QRDx0Kls+j7oyL3WtKS5fXXdNZnC9r7XITrzAmIITuE01KMAIBOSd2EiEUzD2kxxJLJBA57UKEFn0YqmbAaG+HGK7clG3Ji8UhhMATTY14taG+6DAjmUIqXe5ZJZFXNYOdKbRutqwbT1y3HvdfsXqYT9QIjCFV14Au6aqot7Vh5ztORPr16mp4MC6wratC4CnnsB9MFQrSsYLVNJkcI7VDrgwXWAb0nOmx5DFkPWLD7vSyOb9rx78c9UOnI/Fi9nZ7msUgWB6Aifgzf/etwnBNA4L1aPr0HwDIl18tiMkrEHlOClEPM0Pz8I6Z7wczDKSH/B1ezszhnu33jMjljiVTMHUGVbGODaghhJQwIgGrgwipETclsCT9yiuAFIFaaCZ6tSgURUWitx/5Y96PUONhnqOlu6ac2HKWgBAcAQQRCjb6MnOxAsFRMk5HUcFhnSud8bhTVOuuqaq4+c8M99zg3iOWSmHfj78LADD6yog8212zRAmOQrY8cit2nfIudG1d7bgIRxyRl4SZ0/D++Z9Gw+CM4g9r8rnPDDgiz16Z5Ok0YBpQmC3yRreKDBQvxJySOR6/6vx3XLL8Enzi8U8AAOJPPIm9Z31kQmPIOqIZhFQp8hQVgvNhkySsTJ2G/cd+FoD1zr1605/w5rHWs3fjxhura4CRR+eDl2HpjDpomZG5vz65sQsPrGnH75fuHv7g3q0Qy/4PQPkYl/FECDG28iSyrlN23bqSCXqG7r8f3b8otr5X0z5fTJ5puB4MZeKUjJ4e32f6rr4GemsrjI5i69V4kF2/vnzB76f+E2zLsxMqMO3fr056DVTMyCpfTYbie2dPNp0Ve1nTtNpFWJ5OO3VpTek67v09yrlL28kgeOFinr1AG2pEzzVrsGDBB5y2BtLueQMIQQ3WIber2BWVa3kowTCUUGORO6gXVQoVcA5TLtz+/PZrse8vApqhg9nWnhL3r7C9jsgTbkxenuVHVXam8DP74vuQNbMwq7TyP7Djfjx6wT8i8+bIF7dEqcQrJfoke5HAu8+x4qHy2LusYxlOuecUDOWtZ6BtyyCeuG79yMcS00REgZP1HADqzGJLHjMZ6sINmFd3hLWBu15e9mJh4fO5VP8Y1r3rR9AyOYQOf7f7fexsm542FoZMFOLEy6uNGOxIAULzibygGoYZUK3z2PfLe37O3djVVArBQ05GYP6JUDQTRnf3sPMbx5PJNMGTSVwxfy5+cMh8/zG6jshRH0bo0H/wbd/Vay0y7+ypnLxoPKgpkad3p/HCb9biuT9vdbLtTDTdu2OIbxl7PZyxomV0rDz189hw+GzkUkknQ1XiyZEHdvbs240XNrbhMzevQE+idOcthMddU1GRiburHYIJBGQsg4jKFaeCSY+hMSjSwmS5xrgvXVSzglZZQccQDtQ5HYnX3G72u1k087b1TzCkV73pmyQJTYNSN8O1IAJQmtxJvhCi2JInil+Nfzry33DqnI/AzOdheFbShBC4ZeMtuH7d9Xih7YWizxXCNQ3MFI67ZlAJ4guLfoyTZ/+jc4yRyiL9+grkNm+WDVYcq5IengUOK3tZqqcXpyz4JI6Z9T73AnZm02AIuVAAevIucGMfVCWAULABGU9WPUPzixXvJMSw768SAJMZP9NZjztECde+nv0J5GSm1YyRwUce/gi60tbvqisBzCoIzRi6+x4EOyyXIxYdQmjRWVBnLfK3iY/cXfPAM4/CmHk49r251BF5dWHLVZgnE8jIpD6BEot0znyCC3fQUV2RJwwTqhy8AtnRZ2DTc3lo+/ZB77QyxJ6afTvOTL3Hl1W194orYPb1DZsJFQCwYzEQb0dCSyCpjzzmJ9m+x5lMqEoQT/32KiRj7qQu+cKLvuMZ40izBujhGYCiIC9dXJINVur1quuCDezCa72LkI2EEM+NrA6iZjDZ3hGsgMbanGRqpUQeS+lILGkbt3i06K23Ytc7Ty4Zf+RFb2/H0P33F20/0GN5QSj19Rj6W/H+7Jo3kXh6MfRRCixrocLzDjEGZkhrQk93yUlg+ze/hZ7Lr3ASZCjSEjRRMUEHvnYBev77v4t3aGlg0/3Y86Wf4cAFF07ItQE43gl1I7Dk2Y+gqRcv+ATkWGOLElvk2UXKiy7LBX726Gbs6Pa/vyyVBrMn/AGPyLOvnc2CC47bttzmJIsB3BhAkS0YxwtibuuP/yQ+uOBzaArOgppyRZ4ix/FZ+4rHQSEXuJRIE1iZBFSCcyjSkhc55qMYMpoAAGfu/QJm5RegYyiJaNo6T9RJ1uGMvu6JCt5z+36GFWtBtFqXzYgukF3+um+bneHQqHIB6A8rfoOT10WRWrJk+INtfDF5ciGhxHVtN3Ovu2Z+l8ettYIXzd3b7wYA7IlZSUheunsHevYnkIkPP2Z9/5Xv4/UDy/DuhgBOa3DnS2FuWfK8fQQrmNsxk8GQC8txuZBcMsEPAD3hf84dbytehchz3DWB/RsGADDf8xJSw9ACAQhdd/qr9KuvYuc7TnSvaS8eJFOAGoISaoCiWyIPwyzaCc9vUK5WHstkEDridDTMP9nZlo4NIZnIYF5CIF0i/0S1pW3ye/ZU3F8TIu+rd5+PO9fejsSzLTil3nowMzH3gTYqpMNH+2ogO/pihvv/shnpB3bB6Ku+WHMhuc2bR53xTMsa0icZ2LFlFdQmK31suQxYhQM6ZwwPX/ELdDz1AL4mwoiXc4fi3JPVSEVy0H1ZBeMISFdDRcY0cSOA4yPuY+az5Bk6FO6+lDkug2BTSRglsoJZO912G4NugHROBs4KMDDd8CUc4fk8lKC/BlDwCNf9U3AUJV6xyqK7tCXanH+bmgZdN6HATd+bzsTwiQ1NaL8pgoH2VMVVM86sBCCqXMEMKMUlE3KxNDr+4z/Q9uWvwG6YYmdsU0PggkFVAkj29KIu0Ojsc74QABYIId5QB4BDiBwCahDhQD2yHquJWZCUhnn+v+/DZyG/ew+gBsDl/cjkPF1GwUDDGcfTN2zE1tcsUdeb6UU0H3X26+BAIAwEXZcGb0cJIRB5578gtOjMovMCI3PXbK57H+ac/T8Q/YCwV6jVEBBqAEsmkR2yJqv1gUaIwlV6p34G97lrCs4tv3otC1WK+1DO/36weLziu5vQXOt4PpND109+iv5rrwUAhLn1zqie7lipr3fOWxFmAo9+A9hwL3614le4dMWllY+3EQInbXUtb3Y8aGeruzjS9SN/EifLeq2ABax3KZOw2vb5o36Auvd+C/25/uosj33boMnEL4Fy73sBhhTZ4YAKzniRJ4EwTVcE5ZMVRV7f37Yg9UoHcvuiGA9iD1gJJAprmxUSf/RR9F11dZEYTMZTyAdCEKecCm1vcfp6e9U5+fzwC0kAkEvpPo+AwmdJmAymFM2K4DAL4kZYIgG9rQ2pJUuw5/0fsDYGpUVqHESeMAy0XXABMmuKLSEiV3AP027smS/zbwGGro3J+m0vXGltC/Gezo+DDVrP5+BttxdZV4UA8sEAjBJxqfYYaVuNFHnfeBkXsK5YDo+t78S371vn285TKQjHkiddxxMJ5/xmLofVPatx08ab8Nu1v5XtEo7I47mc734UeoikdA0LG0/Apxd+B8GMJy5Jeo0cNXioL44MAJhc4FJCjWBlSskYuYzjrll31IcwY66VpGV2wPJH2d8XB5feMqYozIZd6tly3TXPSpyOge1Wn1mNy+ZMswlf3X0ikj/4hS/L6aYB69/DWfnXPNOCgXb3HjXIrifd2jbiNnhFA5fZKs0SCcnstnhFnrZzF9QmSyxXev8cC5f83ZtmW/11rC+Llk0DJUtMAUDWyOK1jtewY2AbQgpQ7xFMdsZvb/K0wvhtbjIni2UibT0j5SzNRrJgXmr3/153TcebpvSCnhM2BMuDz/q3x5KnRJCra4bQdRhyISZ09IfQcM6V4Jrm6395MgFFDUIJ1aMhmXb22fc5tzOKzNoCTyPPb1mu/BNLp8HqZ4CF3BCcx66+FAte2YA//YnhjC1ueEbq5ZfR9rULsPvU06rywGu/8OsV9097kSeEwG93/QAnLZ4FnjEwN6ji5DoVKU/Gx7t/vgJCCAzevR257e5ql2AMOz/xTQxc/LFRXds0GJoDdszO2AL683v3oft/H0bfb0fm8pRZ86ZPwCmCYVH9ofjMwv/E/tUboNZZk8TCOjsAEHtyL7ouWYFYr7uPmQaYaeKQ7iwuQh2Mrhhav/Tl4nosnHsseQGkhjwxHgZHUCYRgZw8cP1EnFQfQLN80vQ8cyxqQjd8i3Z5WL+Z3r4ND/y0dNBrtN0NjjaH0mgINGNO+FCkOjswL3IEmgINYHnd508tNK1I5CmHLfR8pWJLXqHI81ro9LwG02D4h6YAPjsrBE3XcfLi7fjiqjngORU9+xNlAqOtaySGBiC4QKAg8YqX7r0t2HTUAiejGhTFcpsUlrssgw5VUZGPp6EqKoIM+OQ66Qcvo9F4MIREg3THE/bkuAHJrPvcFFry2vr3+f5vdHZY8RvSypTRAthw9CF44ZRjiwaaXMoAMzkMWSvRK2wAQDfzaPz4NWg+140DQaHFXa6mufsN8Lz1W/buW43NS59DrDeDbcuLUxX3/eY3aA5Yv6uSNDyFWQElEAZLJJEbsia6jYEZELxgoHFNeU5GVkVR3Ex18R6o8juHsp6AeM6x/9PnlrTO2HhrTuXTWWgtLU58VETI5Cce63F3UwPWHnMoDDl4dOwawpZXO5zrZdevtw7MxayB0cxjMDforydZiUQnFg65k1Y7UURvpz9j7RN7n8BDux4CACSj1oTKDFjPVFaKvEigHqGFH4DJTcS0KjLT9W5DRliLUWmzdEbZQnT5vISCKlY+sBH3XLISuQ3POPt7Lr0M+z/+CWuQzidckVciJi/WYVlSBz19ipc3n34Mj//68pL7SmJPpoexMmrSgltYTJprGnQ1BDNcB1EiZta2AiWff75on9HTg6H7/ub8P9/eifsvX43NL3c62wpFXs+vfgU9br0DiuAw7djYoSFora3I7y52iVUCsu/Wxu4yqXd0IrduPXouv6xoH3voIv+GVC827voI8pHZZc+Xig7ixgvPw+alzwO5OLDm1qIYnOEQzARXgkj0vx1ndJyLyBMngqVSGPj975F87jnfsa1z5+CVdy5CNlkc3mBbnFyRJ+PTylh5C7wS3fN4FuSYx5JnP2FGNou+jCWA7dhunkxCaBpCx/0DANW/+FRgtc5zd5xcwNx+V1WCENxEA69Hbr//nbbdihU1ADZUekEjn0n6PGcCagRcZzirOYIzm4NoH0wgZ1pzFE2pQ8eQZ7z2Fsou4a757b7z8A9dR1vXYSO35F174Ef4UvAHABRfuZ5N/ZugCIFDW8svqDGTY92zbXjsWleEN8lLD+zZX+ZTJfAKbvs7mcUWNruf8rpI5vfsRt0732mdpkJMni10bCtn81xr7hPvzWLT0nZsXHKg5OdsSzA3DagAwh51EGbhovZwT9HwkBoBN00nvCEnF4y4XsJSJQRYrkAgynmI14rlLLQOE5OnwJ1z2N+dCRMhNYxM3QxwXceOvq0AAHXm0Qg0HwoznvYtuFiWvACUUAPmDriLfvZ9jt6zA7HH/QtvXk+mcrXy0rEk1HAzeMgaM03DwFBXJ+pkv3tUl/vMDf7lVmj79kGYHHpbm7O9c9cQ9q4rnWAJwLDu69Ne5NkrHQuNQ8HlSv/b6gJIDbkvv55n4BkD+V1D0DwrMSJj3eDBNSNfDRJCQO+wzqFlTafPFPKB5zob1Uqiti+KyNv/GfrAYcMey+JxtH/jG+jylEvgBkNzsBENwWac3n8GzEHrXpQaVDJrrBWJ1+51BZy9whcJWB096+lDfsuWoqx3ggvnRVIVFRlPZiGRN93VFfly2LeiznY1zPstebrHkpNHTp43gMHB/hIiIoUH/ttNp6unBT5z1H/i40d8A/3btuGcwy/Apw7/AjgUq+C5nX5Z06CE/AGxevM8599CeLNrSlS/8DqQdDtGplkib57M4qlpBiJJDUxOfpMDOV/bbd949wQcgsPNrqkWi7zNi59E9+xmDMyQA68UeQJW4hsGDaoSgNCsFodCTfhe/mc4Vl8Ab0xeXLrSqYptNQwg54ltMwoseWsP+FeQLNcg1bXk6SH0zmoCVxVfJ3fH1jtwxdKrrOvKZ6nQddBgGtQ6f0Y2URDDqARCMOua0PKZz8Lo6QGWXAa+9i4AQNeOx/DSHX/CzpU9WPbAbl8hc6HrGLrnXgTkCrSiuvF01hcPgyUTSHRabaoPNgHceo+dOEpH43E3G5aiOqm1BXdrG4bzpuN6w4aGwKLRsunMATfGAgBye/dafvxykAnbGS6FOynaMn8m8nMX4uUN1oR+8R824fWHrUEmdv8DOPC1C5Betgyw07czAzrT0ZvpHVn/Y+SQybu/xTHN7wIARPs7IIT13ZVIBFesvALXrLkGAJAatPpUy5KnIDNY/H2rctns2wZD2BOSkfWZmuxnQwEVrdJNXtvgFplOPPWU1cZMBtCKLXmGKBVzWrzJ6OvH6w/cjbbNldNoexFOCsDiCZi3jEvf/u1QIs3QhgosiFoeeiAELRAG99S35LqO2MOPOK672s6d0Fr9CTG6fvRj9F1zDfTOLhg9Pdj96X+BljPRucvte0qtNqe37wI3+5E1t0CXk4WBP96Izu9+D9quEiLPzhJZLnFTFdiiMzBzVtE+s9VvrRvY2411s3+IriPPKnu+WI8Vo7175XJg433A8z+HsX0VtJbi5CHlG8WRal4I4XkX7YzVPO/vK4dkkoVkrFgc2JN0W+TZHgv2b2jGYsiudd3mGWP47ubHcchQt+88LOnOV3wxefL8ZjLqeEvMrZ9rbRsYgNIwF3Un/yuCh7/Xn0CiwPpicPf8M5SI8+8AgmDRveDg6FjVhlVPLMbmpc9h+bN7kR50f3tzqLSnUDYZc7wDACCg1kHIhd+ZAQXdgyknqz0THP9x7zqYsj/11fZzNJ4bvxYSISwwrHExZ5R/Djc8uxd7bn3c+exRmjW3UhrnY+jZZ7C5ZwMGsgPoSnfhU2sF3vOm9X7siRU/90ZeinZPYqoG+TjUDQ1h/6Z+mNEojGHK5HgXf7nsL0xWLPLi8v3P6J6cBekMgnOt31hUcNe052cpw/ptI/XWO9u/fD1yaQOGXtod0CvyAAUhT78Y5tY5NI8g5Yb7XeoDTeCG6VqY5XGFYlRPL4YWvwHC9Je5Evk81BlHQjB3Ox9hTB6E5qmPZ20zhI6gGkaurglPrGmFLq3tSqQZAMBifpGnxxNQAiHwSAPmDnr65YLERmY058z1MQJ3zVjfEIKBCAJqCIJzJPp6IQTHrL4hKPVzwAKqNf8UAiyRQMMZH0LTp34PI+p+56f/sAlL7ihT7koIX/b4Ukx7kZfRPCZXT8yOV+QBcGu5eV5SnpSdszJyUaa3p9B/yyZobQloGRNMThpYRgPPm+i+fCVSL5deGX7pjj9hy0t+V5vYI49Yq/Jl3ARLYZv8vUVDmWEiqCjQWR6cm0hvsSazvIS7pv1tZza7q+dbXrVETF3Yegn0PstqUDgxYAZz2qpARTbu7vfefyfVvDTv20G8Rs4fk+eNh7FFnm2B6Xp1g5NEBwCymaSTgRIAuNns/Lt3h9sx25kz7UGZ5zWgwJKnqY3u8dxKdf3R5iA+2GS1TQn4LQtZT8r8XFYD89TR03UdDcHDsOisH6NeARKDOQjDQM+hH0BixjGI5mSnIT/CmQDnHIrir5PnJShdGnOhIDgX2HzSt6HVzbEGLGHCkFZPVWZHnNV4FIJzj8P50U84gxoLBpGot7MnetrryRza3+bvnPrjBZOMeBw5412Yo34QAJA3QwgqYdQHmiE8HeCuoV3YLa1A9kBYZMkrTMEsBMyeHpiqghVvPxLxBus3yTXNhLZ3L7LrNwCtyx2B6ZxHLuakPTEGdv0px2014Hfd4MEIeDKJ3WusgU9VAojI5+2h3Q9Ba21FZr/8jX3umq7IM6E6sZp1eQ525WygdxuMXlnkvoK7plfk6butAcl2v7MteYcb8zHbtGJFP7jgs/jUkf+BlzY/5DvPL5ZeAr3D6l+0llYgG8VDjU3Ynx+CxjRoTKtoTcsaWTy17ykIzpD3iLwjGo7DnPCh4JyBm9LdsakRdUYj6nXrPUvKyR2T71K6r68oBXR/uheZTBwb+zdWFptCAH3bYOdAFboGeq8iiwAAIABJREFUYRjY99FzkFy61Hfo31v+jq/8/SsQQqBp3w48/9TPMO/AbmcFqXVgYdG1hKZBZBOYs64Os1OipLum4nZkRfRcOkK3V99F5V8lngPuceGcNeMcNP3z7xB/vaCcgqZDC4SgBUK+rIiDN96I3iuugLZzJ+rf+14AdiIml2Qmhz1HvhM8EbdKhcj+o7cl4aYzL+H6qw3GoKceRI5vh5az3iczOgiWSiK/e5fv2P7f/d61SMn23bv9Xpz75Lklb4fW2oqun/7MEbjC5DA97rXm4ACgBhGYWZyKn+X8E9F1K63+ec6CE0pey8K2pAI4sAr39N+Kh6/ehpZPfarCZwrOwBjiM9/m/x77LZHXGW3Bzqi7MGp7RyTTaeS2bkP6jTfc7yafM1v425ZPnskA6X50fOsbOHDh193yMR0dOLd1Fb7/6m2+a+c81l6fyJPiUUsnnMn5rIgllo2eXmdRU6mb4XuWCuNPDY8lT/UuuKkhaDwPJkx0b0xh1WOLse7+J3Hs673o3uaxLiZKu5/qBW6carDOJ5JFNg9TLuwIWIs3y3boaP78bfA0CUKEETntQmcRlguOsAjiCNYACCDXtRZYeXPR9bWWVqx6pgNLN85GTi5U279F08evhppX0X7Bv+ORL/4rAOCkuDsf2BEtTnqka9bvpEA4k/JGmSU6Nu80vPCXbdhyzuew7yNnl7wfzvfhHHmD4SePbHLSzZRyE13Tav2m7bEEbrnlKfz4iz+3Sk7Vy3nMCNylU7rV55iyVl1q7Ubk04ZvcdSLI/I0BkUBQh4LWlAEEdEFEldd62wzPG14x8z3gxsm3KLjUhQbBs5qCuJYaRbkhuUppHL/mB7mKho+8t+AOMrZZr8zynAxeVDADGshxxZ+GnQElTBy4Qj+vu4A9GQAzZ+/DaEjrP7TFnnbjpiH5ScsRC5mPa9qsAHzop5aogX3ufOGNWhdYrn3el1v2VAMEMDsZMiXQTUlE6wE1BB64h2IyWSBTU1Ho+mT/4fDGk/DrhNPQt9VV8NIZqDOOgFKqB68vw+4+lDAGMZSbRhFcbaFTH+Rl/a7C9os2+hPRW5K0eerU5KSP2aJQV5wAaO/uAMzBqyBMr93APmsAS7jyNI9g+AyWDuzobTP8/aXXsLLd/zZt23gppsQe+BBpKTrU9YzGe+7eSO6r1xV8lyA/wEUJkdQCUDjOaSNGLLt1vcvJfK4dDFt9Njj1zxtvXwN0lWOxa0XnhWsUhp502PJC0DLup25lnIfSEUOJlxIkWdaVgirhIK05Ok64HFR0xXbkmdte/rxFJ79s7uiu2V5u291UCjuCnC612Nit2PXpHuT0Ipj8nLc/b9dJ892vQUABCKI92fw0l07wAyOQNy919lsDgHPipOum5gXsTJFzQ8pSA7mkBnKYuc7LsSmU7/vdLYCmryHORjMqOiuqQpLnOVDQeg5E9E574QRmQ0BjggbApeT41Cwyfc5rprOCmGuvt5x8fGKPO9ibutm/3sST/ktMSyeQDT9X2gKLASEQADAeYt+jHMOv8B9/owcTG6i3rAESnmR53crSDz1Kszc+5Cvb0KyPoLoLOvzYdX6bfSWFrAF7wQvSIKjy1VVb9yt4/omXYQMIXyWPD1SD5ZIOnGQABA2d4LpuzGYG0TiKdcaBGa4q2O9W53V9DeOPhI7DzsGgLWKm1MUoGM1TJkVdLh4WgHgjeOPQMd2a9JhT74OTVq//x/afo4H9lrZIOfJmpEnZt3fVwgTm7dtBIvIuKh8DvlkN3ZvOwWLd3U797d33e3A7eeUbMPi/Ytx2RuXYU+8AznDP7kOqEGoagDcsBZ8eEME/7ru1/jG+qshhEBSLpSZdkzeYH/Rsxu85s9of+8H8fXnv47bt95e/mYkuy1XUwnjwloJ7+5G7/9e6Tt099BubI9uR+cN1+PMP15i3bPNqxyRt/LAmWjfPuQTeiKfR25XG+ZsrsN3nuNFdaeEVTcFAKCwYncXb73REQfCy+MKnwOh6744usjhZwAA0rc9AL2tDdn16xF75BFA16AHQsgHQmBDQ07hcr3Lck0eaqxD59wZUOrqYEb9izOvN8/Dvrl59GzdDK7rMINWP67nGYZ6rDGqlMgzonHYQluT1gOezgCG6VjyumY1oWtWE+KPPeaUArAtjdetuw5nPdGC7IbiOofR2+9A8tlnHdejgRd3ovv6N50x2OgZRPNn/wR19hlFnzU9Q29iIIeu3rmIqApCkeaiY23cDMkKjJ2rkOYLkJh1nLN/++B2X3KSkjATiQKRt2+Lda/Xt6/CBc+5WZ4V+bzlMmm0nX8+Ov7t3519H3r2aPxPx8WOl4C9aMRb1wF/PBX5ndZ4aAsf3bTdzfwiLOuJk3MTr7j9ajqZQjQXxVmJ06EaAPIJaK/cC0V6lSihRp/IK0wSY3KPxVjxuKAHIxisD0GAyUkiw9ygVRy72TNGmGUStGkFcakiVOdLIlWX545Ri0NAVYCTDrG8CXjO7VOEOAHhRWeCxaS7GzMREWE0Ioh55izkHuvAs68V155MPPmk+70cbybPAv/8t+G4rhw+2tICVVExNzQLAkDb3BkQULC6ZzXOeeQcrOxeCcC15IGbMLq6kTWzaJS3Ll9neQXZnjxlUQIAY3huaw+e2NCF5jSHwgXMEhm5Fel5kzPT+OhNl+Db254BT6edMJyKMbFJq79Ixq1+3Mhazx5TQ8hnhxd5TBNFwiDMQnh7l4DxpOvm2h/rdzKSzo4cCuhueS3by4cbJmYFFZzSEPAvxHlDMgActuA4KGoAmqdpw7lrOsXQFQXcsPprx1UVBo5qegcwayZCzEAg77+eEUujbXca7fNmIl0XRi5mL/6qmJV234nC+xw0A+hbvcv3HfvmvwcvbD8CC2IRfG7F4eja4cZ7ZmXOioASwucf/TTiPdZv01hnvUuzwlZCwR0v78Mrp10JJqzsnKJ3L1boYbTsXQYhGIzMEjy/clvRPeC6jnWLDi15f2ymvchL9ZfONHZ2osDMKlehM3lX9AhZ8LnUM5R6rQN9v1+P599c7Ftp0VutFye3pUW6a1o/dC6aGjZL23mLfoyPHVaQGUw3wGJDaOuxOk7D8yIYnWmfdcxpt+wdvZMJbjAEFRWmENB5DkKu5LIS7pp2ALfvjZKT34hMqW5kpStbgRla09wJjwoVnLn3M+aJz7NFXt60XtQ6WO2wiqHbMXn+yVVAWMe8fcbpOGHGGahD3heIu3tFr88iotTPcf/tOZVdHsF2++AlYvLyzLXUeUsoOOdTVLz+t13YvaYXXXtjaIi5D0k2m8Nc050g65rue4iSAzm0brUmaGEt4RF5sq6KrmFly3LHXSXocde03XvUrPUdcuGgx0VEgAuBejYAZou8iH+iPndIhz2YCU+dPK+4gcctJ1FQLy6VjuHk2Wfi0HpLzHgnhgoYmqS2bQzOgKEbVmbHaw4Fy8XRqNsir7S7Jh9w0wtzwZHb1YvAzCOh1FtiPdVodcSOyGtrhWHo4Aj46ufYFiWfJS+RQLIuDCEH2rTmqdkDIDt/LljSL/IaAiEYmWfRtK/HsioAYIqCdbv2O3UEFUWAJ63fMllfh/pAM4KHnYYGDciqKsCZ46JTSeQZ3ABTFSQa6tAmJ0lxMQtde2KYoRWLfJNb322BbsUgRRqDYNpGfGRtEDlVDqDZHLoGWtCUD4JnhCPyelbeAHStKxmPtGvIGqAG0inorKlgr4LmOYeBG5alMF/nLmTkzJxz33kgDGYyxAcHEVT9Fu9Zy6xssIoQeL3Tn8UO8Aimvm3gApgVno+IWg8WCDiTMV33L67Z3yt921/dbc2znK/H9N3YvXY5uMfqwfMauOzDwsyKyQuawpnkJp58CtzOPBjze14I04TR24uAEkJYrYdZIuZh/8Z+3HLRK75kQO0NITx36ttgFKSVb394Cba/pIHbi09yO6ufBZ7NIvbAgxi48SYoug4tEERWDQNCYO8HrbTbQgqqA3NnYG1/B3IBgYHBA0i/vsKZOBmyP0j29EBoGoygO6npbUlAz5n4+7p5SM5YBCXs/u5aLIU5kcNw2pyzkbdrq2UySAiG3YPWAtDmow/B5qMPsWLBZD9nyN8qwATOXStw4Ktf9X1nlk47sYO2FXNg436oTIGRkRbDfuu9EupRKITl3Gd327JO1MtXWQ1GoERKT6Z7EjL+0Miif02xMFf/8Yt47N8rx99zgyEx81jftk291iQqbLpZMwGABaz7mEsVC50ZiXq8P32Kk6jCXjRiHdut50ARCMw5Dl2XPIfMXy9H04a7se2kbyJbf7jvPJqMVQoqYTBVAQ8HfX2yns0i1taHX3Z/Cyeung9sfhja6hegzrLGRiXc5Bd5uQKRJ9xnOwi3H1KVIEyFQQhuDW2COxmugyn33ubjpWMMjXTBAnmRyGOOV4QQ1p9G6UUkPNYLpw+XlzR3u2EXv1t8PA7PfxCnJr8PcA6Dcfx1RSsMxqF73CbzeZlEw9OclnceC6VhPpS5x+N9+4Awguid2YgdR86HidnY2L8R/bl+PLjTSqbkxHwJAaHlMZQfwhHaIQgf/0kccvT78L6GAMKHnoLgwg+UvB+RU76E5s/9GdxkYFygSc/gtpsYvvoax+eWm+h99O++msOqKheAox73T/b/uXvPMMuu6lz3nSvvvCtXdVV3V+dWt1qtnJGQhBAGDCLKgDHHYAzGwLGxMXB9Ljj7co9t8OHAY+6xsTEYsA3GJlkCJIRQK6AstbrVOVdOO+8V5/2x1l6hquTr57n+4zN/1a6999orzDnm+Mb4xjd8AiPc0z03VavXcvn+Xz1Pt+XyvZPf49F2uA4atdBX9SKRMMcog0yuZfWIAyDu2ryHhhqD2vgeLiT1+6pQyc+P0mvz1PMBZEaFPPmuZ2WDNX194dyqpa4riGozOy9C5U8LAGoE9JtJqVNJCY9/2fDtGIFL18nO0/bCCj96wMdSC5T1AZx64quoag5f0cMee+uA6YF2lXa9hu/aPLtxiJmhndTcPJUoIHvo4CM8eCEse7EjOrMQCpavxZm8uF41wg8ntr42vJrIr3SFxb1n9/D5L/450pvGdw7y8F9/Zs25SNtm7853rXt/euM/PcjrzKxPjRxRFQbGkxR8aybcUA6/kGSGglaP4hVlnbpdTj/2CJ7rYp8IDen99/wt/3z8n+PvyCj17c13sVtu7Kg3F5eQTswpeNHz7TNDBO85PitzNQLXxVtaptMDn/8eafAeyEvzu10PTaj4MsB32+hWH9bVv4LQVjty0I4MfS3dGDdyog0lKoaOzsdfyVK/XCeIDYAiFKRMDPfKfBIlDSIgUY8cNlMNF53b9RBxTZ6LSClrKTL8zQFrA5cO3EKhcQZSTrnfdrJiGlaSydP1xGjIXm+zaHOT69A1O56G8OrIoEGQaqGQHnqPM+8ElGoJYOp0Olzd3hy/tttOT2eGIOjguQFLM1G9lVOn7tQRhSEKWtS2wQ+Y/l9/EWfy0sMJwnPWonngaGoM8hQhkATk5UwK5GXrWbae6MSqkgI1tqxqipIs1MQBrM8uIbuJgWs2l9lbvZ6bR98cnmq6r5ZwUFPPo93qwLNhY1vXrpF3KsigxfzpsDdlrdngYwc/wc6lMELbXBiOv/u7D/8uCzOhE+lHohjNfHheYe82gX3qNK3OCv9SKINMdpiZk+G8TSsr2guLPLRjPFaiCzAglWXq5gs0F6eBZBPJqxE18uP/EvcOXCpaPHniAtNzUYZTEIM8gO3lS7Gufi95z+BzlQq+7+JFdE3+DZDn+A5+lMGuGSotQ+Onu9/PP//ZU+hynQaqUYTdlGENRr5k0KdqXFG+mWWvTdvQqNVWOL8QbuiBo3H1869D83Vmeg2P3Q4Np8FvP/jbcVa1J6vddmzqYnPmNzWhY+YqKDKcgw09UZBdsVfiTB7Ajw+6XDhTT4SWAJHyqy0bTtdP01xaZPnCefh/boHnv8n5X3kf3/vQ3/Gdr7VZtnPcMf5OXrbh7fiKir+8TK28hZbrU3fquL7LZ576DPOdeXIRNUrd8XL0bbdh5wr03Dav+ziPPPAlvMVFlooVHtt2EX67BZHtCURYk/fFP/PR3v1/ANA9+FxysqvwgDszS1fA7Rt+gddt/iBOBPhr3/0utW99C4Cn7jlB4J5n9nSydo5WwufYWllmqbvEvi/u44cn7uPoUxZbxnbijuwHPdmTZjZdS9DthnPPdRFOKLzSWkXf7gWrPFUhkJILBRX1W/dy7t3vjlU4FVGgoFWozc0hbZvlvIHXDVUrz95/kNl7HqDhWLDz1RRe9vthralQcWpNbt/wC+yqXI3b7mXympzP6Tw/2kd3JCV0IiV+rc5Tm4b54vfuB0LgAyCFwPUD/ubAKWzPp/6d78Y91HqZcFkLbZYTAYD2TMh4sb2eSENKuS+1lBpLNgUlOobSRYmUZ+sL8wRRFuTAhQP80YNhTbCw69RcC7f1A2TkRPXA8M1P/Nv1Kx2xif2VCiKlvOtIE4lA92BHdUf8/4n+67hry0dwGy+eVfm5n7yEQAZ4EVjzOiqHzP0gQKlsRCmMMvPNRToPHWRu+EoubH1Dcg+CANf32Vm+ijdM/jqYJfz+SsYmr7TmyU2HczB/rMWhH7+At/m3McZC9WhhZHvZrW4r56bUErVIGVtKiSI0AukhgyDacT0GrfCYvpa0H+o2Vnn+vXvWzjKIVMXAm08CxsW2gx/t/bsre3lpPSBnRkFCN70vRpmhwOe7z04T3J/sIRUzEU/rthf524fP8HvfOcQXHzqNM5v4Ir/1o9/gidknSMM8vbqF4sv/kOJLPszrH3kphu3H9lmisthZJNeVqNHGHmfykATdEORdqdyGufcNDPdtYIOhMLDvDeSueOe698PYFgUXXJ9ASipOeH+uOiq54wnJT+5d4d4vJlTgkiP4reM/h7ESPtupsetp54Y40TqHMnIxU8uJoNILD09z7LFZHv/X0/zpE38a/78R2fzO2fOMK8uIQugjeU6AM722drAH8qSzji8k9TUgz3W8mFmlCJWB87vi7Fp7Kc+hB6fwnWyrqR7kCMwCq4cvfaQkrlV12r22Ci8iLJJq5bWzciW3jb0NXTGRUpInChQHHazAputm52NzKdzTXz3xXn5m4pfw0vV5+QF+cv3vMz+wb93AbV4rceBrX6G2ssL5/jIr+XBu9DdD/+WxFw7wnc99GG9hgSDVaunSk4OceTaiDscgL1ION6v0qQIlCrQs6BPkuyraSqJY2u+trXcPul36rQ1r/p8e/ylBnvT9WFmyMffiha5mSeX6N4R0jeUTkdOWEp3o1fH0UMszb34T3/iTP+CBv/tC3MzxXfe45B5IUVF6giJ+nm7TQYsegNu048Li+Dyl5Mzzi+sCiG/9j6f4qw+8jecGS/hLSygR1XR1jct6w+12ue/yS1jYmvRG63RdVEXF64E8rYC+4TLExa9bQzcSURFqs5Eu/I8yeSIEhX4URfHW0DX9hK6JAkESIWmlWhrUSjvD7wdJw2+ARquF7PUecxzSU1AhuxCV1gKKTO6pJoIMXVPJJQBHS2W04oh55BxJu4vQsyCv3YFu40vYtf+1biYPQI+8Vt8LqDaT37W7Npc0EuenW2/iBlFfJD80lAsRyJNCoeE0QscqGtLzGe3m1118jp8FeZBExQThnAqUuZiuaazK5Bl2mk6r0N9r2u0mCmBuaTw6XuiYtf9gH8wfpe228Vep5vkpYZ2uvowiE6N18o//GwePTfM3Jy6HjiTvlnFbd3Ph0D/xmXd/HfNEgZvUEX7xVEhjSifX/+nYP8V971qFaHPXIoqREAR6DufUKb7nzaEEClKmd5jw2pspuub5Uy8QKErS902RIPSYnufqFm5tBSWV8t1W3s+gOY4UCn5UbN2re2n2aFISglqyBgzFQggFIzfEt/MFvlc/Gmfy2q0uJ55YvzGu4ztJBh2YribBl3QEvTe8SDXOjCjJNl02WENcVL2WRq3O/Rdt5ltHnmR2OTT8yspGtszvZ9PKXmakwUI3D06Tx2ce51snvsWz88/iB36s8tmue9Ss7Znf1BQTTTF54+QH2G0K6r7DbSWN28sa80uzdOoOahCu8ZVGDsfukAuSdTG8kmRY8nYIDD//K+/gCx96L0w9iTz4bVoPP8yp9hhnpirMB3sAKOp9BIpCa2aZxy/7ECe2/zxn5o7x2O/9Ote/43Mcf+T7bFiChVKR/N43Yu27i8B1Y7u6t7yPK80r8RYXeXLrTuaLDqePnkJGds5XQBcaug/K8TAoWDt/Dr+X8V8VKXbOn+enW8eoGCEN66GTPwZg6jd+k6nfCpuRazM/4eayxYlnk3XVi6MEjs3RQ2Ek98A/HovrTwavfS+lV30qdk7afZsJWi28xYUw2CdN6mM305AqnmphG+Ha7jnpih4CucVi4iD5i+G83d9/Fa/e+F5qyw2ef7bD0cEmXudBhjeXmDm2xPQfhDRgszKOMAo0S5v48Uv+lHlvID6W3epy4olHueDZcQPuM7/0Kq4efCXXDIV1d36txnRfCbrhfeyBPB/BPzx+jt/59iEeObnEyte/jloN527QqNOu1yiKcJ23ouBqdy60lb2G47FsOVlH3+/amITrWFVclHKZ+sIcf/XBX+LogTBbfGz5GJrfC+7VOCoG8J3nkH5ov/69Tcg9ZYJxQ6HaSdR7AwSPb9mATz6u62osddlTCYNXSs3l3j2bqVvGmhqa4UaVbxz7Bs9NhwI+Xkdh/oyEQCC1EFT5W2/mxJkokBftd8fnmuz98DdxNTWknQETE3egTOxHdjrktDJ7qtex0m5RifamQMLS2R0o1T14hSirYWYzefWVrNhPugF4D+S5gYuiaPjSJ5BhyyRTsShq4fPUjCSg6nbWzwr57bXgz1tM7GjR9uI2DQA/46go0XqstVPPPlag9PnVrzyJkeolKvuSINXywjS1iJbY6Hp47hC3lcLPGh4h7TK1zLd3E4A4teElFKeWYvotCBY6C3z+M/CKTx7g2PIxzh56Erd9b5TJs2k89SQF2UfXb/HTpfXLc9YbzXYDt+XxVm+S+YF9FGwo2ND1NWqp8qA3HtnCLe5N3LF0A4HQeGHX23hq/3/F6OyhcN0HUZ1k3zciYZVOw2FjKbmuhtvEq9VwGx2uLA9z/ciW+L2jt708/ttzHDzHyWTylFVuqBZosZpob/i2n+y3qGiuGfse0lf50Zdf4NlTqX7EgQQR+mGBmaVPOl4XP3AJag3OvP0XaD3ySNz7OC/WDyQo0W9pQqesD6AIlYJWSQSwANvvkM8/i7dKoKfTaCFlgKqE985JJUwafRPo3W8zUy2D52FPZ0taAOYffYFapOnRFeF3f+aJPBP5XYi5Fu/4xgpH3v8RvG6yz9+8fCW1uTAgHCvMSx/Zt5XL8yojugh1CgKPjj6OIgXFpkrPRy4sNVn++jcy5+E2mxkm2Pr36T/hsA+/wKk7X4fru6zMv/gC89tLGFZI9TLb0WSM+rItPHeSxYc2cubK97JYDY1oI+LLLp49gxvzgTW2/knSULzWiiieqkl7aiUGebLt4UaovadYeObgIt/5zDPrStZOHQ0f9vlKHm95GRkV9q6XyTtw3xm++KVnEoWpbodbx97Klj2/iPTCnmvBjIehmHgyoKMkzm8rZ62pxfBF+Ft5Px0xjoy5iGry3PC91cIrTlSUG56qipQJyOsup/vshKPXA64n0X5i7jQLTkTTcZwMqFVXgTzVa6CQLD49sLN0TSsBWpaRzuRFm167DU5rXbpmpyPjGjnf89YVidDSmbxu4sA6jhtlm8LRWqwlSs/Rd2aj9hS+atJwGpn6sMDz0By5bkNnP3BxAwddSahdvUyeIMzk1bUlvOi+5PQsyGtbuVicps8pMN4OjX76vmlajqsGX8FrNv0qSJeZ2hY4ejcz7RkKfnKfrCvehT+fSPdq7YPoMslcFJc9xPL72Vy6k+331qgsLyF79B/ZoXIudJJVBNur28k5q2rAiBra5voZtjZljNVPL9pOXfqszDhMnHgAr5OIGvjdUMY6DfKmz59EESpqJNKiECCEEjsxvqIjajVU2VN9lZT0fm7b8PN4ih5n8nrR3Earyfm+Eh2h4aeaBGvRc1cKw2Fdnm9jT0/TsAwenp/in//v3+P0M08ye+oET9+T1C84QZLJE1IyPVCK59x6NZl+RBG3lArPnnuay5odBqNeO07KCVqMqHDCizK/agfj2BXcO/tWvOYS5xohnd3xbI6/75fZ80LoSHQ6Ljoy4+TpioEWZfI3mQpdv0hBFeQUwfN/EoIbPQjtreeZSNlmyEuykEPtMureOym+5nPkV/nU8908jeeeyTjbi+5FyfUKhfrMEvbKp5nXjvPIB3+b0j/eR96BTfOS8UUJQ0kWpd4+TjcKqm3Ib2Zz/iLaU1MQZWfPnTlD0MtMKWA2HZTyBKIQZgKOLM7GRqpmZ+3OmScfo5lL1vfSv2aFYA4/eZDd6m76zTGeeCitxBc+l9bhF6i89SNcc/wiBk/voETWSemxEUzhEjQa+PMLSNelZW3EGbySVlDhp1d+jAPX/xGB4zDltKnlDHZseAV3jP8isroloXxGFNUhM6RCN9suj6Vikhv39tHOj9CNMv6mFQLEVmkCqejMlxIhk5MPL/DjL/81R/IapcpOrh36WVYMlS2lfUwW9+ILgbuYqmnzPYxo+kgBhw6eYqS1SHulQffgQcqv+dnwY/UGU08fjqm97Shw6ETy+72Sh6DVoq1r/ODiSY5Holqdp5+m/uDD5CMbqCsmgeNw8if3E/g+Cw+FYFoIgR6tAb++zGzUTyzwp6jlDLxVe+Di3/wN5371/aweQdRku+qkGAxBnfmyhaeYcWuEx797KnkGC3NcvuH1VG/6b3D3R9cc85m5ZxCRWq9vq/TfH67J5XL4zPK5MeqjoZ1WIyG3gxdqFLwujqZURkwOAAAgAElEQVTgRAGf8YErqE6EfVPHSxezr+8mtpovYcAcje/NRCF8nm016pNrlTIgr7uqpVKartmzQ7ZvowgNX4b13QKXQTNcN4EM0NRkj3Dc9YPSXmsthbU5l/hqeU9mAraVFKPnlL+JQwdCWttypHMwtxweL63JqFYSmu/y0hyK1+Wj2lcw/BaKOkxRFWhAzgnbCaSdf1OmyjWESn62mamHXOgscN/eSU5WRvnDR/+QR/7x0xjeCTZbGs37f0zxQ3+KIYo03RXqYm0N7ouN//Hop3BWbHznKAcvegeVCNc5vkprJezxeORbP+IKP2ye3eeUcSJ69fZyhXE1DCycXTofgzIlQmTdhkvH63Dr0wEveS4gmKmz1OjGZRtpH8BXTbylJe49cy+feeddfPadP5cIr6xD19TRKHazPpKXeh36eUFSJ4dkdGsZkaJJSAkiAnmsUjv38cLn0+sJOT+P06zxwlg/y1bWd+uNnu+oKQZFPaQnF/UqEsnS5a34PUudgdWBvLYLKRaanxLaE9VRXjHxDsY3XI5z7hwn3vGONb9d1YZ49shhbh69i1I0KXPVrdwwcifjnQ1IYKZZQhFJQO6aoVcl96L3LGRA/qpfZqOhsMlQqLmL2H4LEQW1DU9Byg4CwS3bf43Fv/p+9jpehC6dHv8pQR6Ae/48n336szyQUrtaPYz6ArqlongnsZSIChYITj75U85+4RFUoeOXB1jedAu1M4u4qkqfMYLieCy1wgig17+JhpVMgKnFJBIWnJ1DiwyV5iq0I1UeO+pt04pqhpYOnV2r/hZRorRAhlSdSNmsN3Hn/zKhE5XuPsxtz9dZXgofaL3VpRRNaq/j0j2yTOG0Rlnvw5cShxR9RCh4s9keG74Ij2OmE3wywFByiSxtryVEy6VzLAF6rh32aYOIrhm04jqyoJk43ZO5QX74lwdRoo1DE6FUrO5bOD1H28n2MtPJ8vhVvxMXIAMUu/MZdU1SmbycliymoEfXfOzLnP/Ey6ktdZGrMnnp0uLG7Dn8dXjfWpQBdW2PspsYJc/1M7VIncWV+GiCsIZBeOF1+6oR1+TFv+0FaG6w7uILpI8XOOiKGQPkuIefCEHktLkY0zUtNUvHnR/cEhtaL7eJ6fFbAcinKDYFNcfW0n4stUBeEcwsbYVzjzLTnKHgJ9epb7yGQEnoMUbnLMJPNura0G4qxhA7ypcjmgVyy48jIpquDGzydtTkW8DlQ5dT7SbHsmyJMMJzcgYv4Zaxt7C1tD+5R2aRpzePIM8WEECQykR63bAYvrncxT51isO7L2LphWO8afI3qUbOiJASgRJL5ktFI2h12ZULgWfbT4zjU5ddwVm3Q720mUO7QidqqjbHs5uG+cnoVmbmEtkaPYp2K8UQ5EnpszI1zYEdE8xFap2tlWW+/NH/yr1fCEWWpJSoR7sxyBuut2kYBtIPHZl1hXfU8Dlooog/32VQK8Y1MdJJ5l5zKVwPqhPRVEXAbvU6rhv+WWb+4eMxyLM7TYL7H+KdPwjQPInj+aEab5A4Y30jt6OmKFtuJLQAMD1rEPg11CC0Ja6rowRd9m1LarH+e+N3ye94JULRQnnx1JL6u9OX8e3jRfyU99B2kvmgGEVqcyFg8YLz1HWNR15/KRBmBccXJWoqkDOx+EDsiBiKQVGvsnj2FFsK27hry0dYmJrG8Xcj9RyBAHlqidz1v4Z18ZsAqDnd2NY2O4ndOrPY4v6HH8o+jLmE1l63DB77x6/FDmOuk6o7jdbp0tEwW7qxth/PsMkHWQGino01RYD/wo9DoOa6+IGD13kE2y/SjeZp0GrxpOpxcriPojWMrphcv+HNNPpCgNAT4ehlrA2ZpUGNbA7X40p1BwpQiLJHdm6A1WPx9CLLU+exVUG5vI3NxT0wk9wbR1ORnS4bC7vpN0bh6L/GmTw9CPj5//4r/M0P/pjSl0KFSGtnyOborqyw+Pyp+DitpRX8lZVYgTwGec0m5zaM87ptH2WmGNY2NR94gEDRyEXOn6GYnKpcw3M/CjPmTpRlD3uFhuurZas0oz17nwXBDb+KMz/LcxNDTFXD+9O45/t0Hn8c+fQ/4L6QqFSLyOaaio7XeQQpA6QfRd+lwPUjZoATxHNAExqbihdRyI/ChSfWNA9/Yuoomh/Kt1tX/TKmEtpszywSyAA/8Biv7gufZy94Z6jk3S6OppLXVonNWFW0yM5W1BE2WJPh38ZQTJ9Wot9QVtE1Azd7bn6qpUivebnthsFU3bbDlj2yxaA5ih+4rDiJ+rIT2Ph+2Mbgx1/+ArMnw8DLn/zz4zElNz2aKaaP2bVRUqrJ+bSSo/A4/vgs//BHj2FH9ihwHcYaCxnQoKeEThorK+yY+wemq4+x9dnPolihf6SKEOT9m03TFTXzUkaZPICOqXOhEQb/rxt+LfuKOZoHnuRCXxFDtXCCLo3mvdl72lp77b3RPrOIevJB3NZ3cJyk556vmPieDNktP0n2pqIs4Orhs9xo6sx44T54WfltfOlfPg8kNXadpstMa4b3/mvArz20hfd8Scd3PbaU17Yo8VWD7uHDfPyhj4csAtdJVMDdtQJAqtTW0DXTQoeKUNlg6LHAlYKkOpzPBOld14/1AISerav1ZQjykqC/wG7U0bffwXPbL1v/Zookk1eKgt0FrQpSYl9mMdtexlLz6L6CLlY9Y0cgUzKufiHZi4YKIS25vzjO+fd/gE46sBWNQW0IpwOjuUk258IgizBC21JS++nqKp4wMJXsfdSEjvBlogIuA4KoXMVSBIvd83jSJa0BKP0FdMXC0kuoA1l1YXt5/RYm6fGfEuQFCtiayvGlI+TdF2+iW2m3MEyNnExAjmXDY//z7xmO+NxVLcf+jVdw9nMPQXWcl4//F0Y7W9AiXnL5otdz/pJEFtdNZXS05VYM8kxp4tR7EuwS7/gT+LVw0TTv/xH+qn4bvRojNXIM1G4kF4tC4DjYx5NIYn8k9z99MjSwaUpdq1HHTqF5TwY4IiVIIhTcVSCvB7zMDI0zwFITB8Fo+Yj8ALlrP8TCXz2LjBSZvFRNnhAKyE68SZt2MjNLWo7Bw4vICIRoQkdRO1yiliESBZBuNpNnKdl6CbOaQ6SKCBQtoQd0vCYyn2Ty0hthjwYjj/2Ef1n+fe65cBlylZpTesw9dR9+dy0loAfyui2XQqpRrNu10YURNwZ1avX4OlQCin0JoPRVM+5XE5+f76F6oK6XySPAlS7bSvt54+RvkDP6Mpm8QErOWy00JQHa2dEl6CmrKRqdXOgMXj/82vgTfUbSI7CquCx0NyO7NWbaM+SDVVEzPfmsECqql9Cj3VRmJflQpPwo2xSitakAW0pb6eskwiujSwI12rysKNI4kCqcHrI20siZuI0eOA24aeRNvHT0rvgzrRU75u+7warnG4TOdI8KJtBwihtjoOSnaMAvm/gvnBgs89jlH6LIPHurN9CJNs6mbnD/zH5mh0NqdC+D6/VtY2J5lO333szJYimmt60eUkpOP32Y3ff1ow/uQhcG45Fhdhp/j++eWwPyOs1GLPAgtBKNbtZ2aH4OU8ljqQXUmb3srlxNWQ838p95XAFTRxEqM8emWJmd5o/OfBDOngZguAa3PS3x2ja6ELEwBIS00Z7zmFdV+vovjt9TUPGd53DskKYn8eg3k41x9dgy38+wSNanLxVmZImDE8NxwEsEib1RjQKNqWzNwTNmaE+vOiLZPKvh5JNnrLlNiOTMjSggsvzYPWwphaIZ+80bsMvvo/yqP6c0/FamHmiiWGWEWcRbXKShJc+r1U7uwT0HnqXr1LMqARGteGF4iAd3bUSZPkwQOZvVoIvfo1NHX7GjjIXpl/EKHUxtfdujC+i88Ez8uiNWwgCGm5xPe2mBvcMvZ3joagrGABfsE1hqAW3HK9AmrqazFDogTiTUYxhZQFDoVxhSJP7IJRSUxF44ZhnZeR7FTfdQC2lJjqbGbW60C6mayz2vJhCC64dfy+3j7+D0CRln8gCeGdrMkepG+n/wLZ7d+25mgxGkleMLdx9k/lBCeWrXGjhnziCN0NZIKfn+Xx7ErTWojF6FIhQmypdht9u4U9MEQsOKHCFdMTk9cA0L8+E8PDIdHqPjddCiTF6dxIbtrFzJpuJF2LMznBso8/TmUaTn0T18GL9W4+TvPsHs3yzRnUtaqwD4lo3XfYjAOUzgJSCvu3AE6tO43YT9ke5zGjidpDY/Gku1BZzcXo7e9En08SvR9v8cx7e+Fjs/gi9dFu0LVHuCK72+ehLyXhdHVUPHNTX80T0xo6CqDzOijSf3NmJaGJHwhKbl8RpNulHbll4rgN6QpHrjRddhR/VJptMlkD5CevQZQ7Q6c8ybSVCj49XR1BwPvXCAx7/9T3ztE7/Fj77zL4iv/g6LU2sd43Y9AVqWbWcyeemh4nPu8DLzZxsEUZC31Wnw6QOfR41AQ9fPAqnWUpP7OEH5sZ0cemIGWRyIjhWQsyVNt5nJ5LWCxDnuUfaC1F662ErOf6EZ2iU9Cuy652dYKOUxhQleB086MfMCwK+1+Mrhr/DMfLi2Zapp+EUXRhk7+yR3bfkIb9xwK9pLfgOp5/EisbH5uVbmPAtBiZ9uMnE7D6Irglk/qcW74sQuPNePQV637bLSXuTQhgHyN32Eyi2/Q22+xbZiEuCNz1ExWXjhmYw4Wq/fIp4CMpuN1KSyDsiLRJ8CJ6zJ0/SYGaIAuZKRETqbXunG9WXKKmZVIEORn6C3lgTY9SaXDtzCrRvetub8ZRBkMnk9LQldMZBIrOoAK7pPxRhiUGxAk1mcIHwdUqUnfimpaxuKlK01xYAgQLnymsx3XbdO1RiNmUfD1ghGZzEWOyxoZZqWgSd0jFX+2Ws3fYDN+hgymnPCcwnUVMLBXcaXHqpQ2VW5mrHcVgJ/IRajE9WsSFX7f1eQ17BMHti1kY1HVF4f3PWin+vzVXRLpZiSzzYUk0v7b6HVPocXuGzOh46K4atQHo/+LsYbO8BgaUfSoNPrNVuUKJ4ZgzxDyaUiVYLFj70V55FQsEXIgO6p0/HxZBAgowh6D+Tp0cYghMLM//nxda/n0N3PcuvfvpwL9WShtxoNnp96In7tA7ZMORVCwZvLUlp7TqURONQX5jj102cAHyslyKFKnfyNH0YpDCFQ6CzMsTLbjoRXUmIpqMhoIeeC7EIa1BVEdO9VoZNXOlxiWuTMUKI6zOQlhj5vZR1lq78vbuINoOeMOEvV8mqZOrx0pqphNXh2Yijdq5JOOauYNqQmx3328Qc4/eUvsmZEErntlo0lUsDNCTNtdmTQvGY7EfkQJuWhJBsWqCZ1O6sy6XseuivWpWsGJFF5gEphU7Ymj4C20cVUXmSDFAnjN6+HapPp7Kcb2BT1xGkYNSvU9BGWp1tMnT9JfhVYUvJJNkcRSibqmSsNpd7r/b8nPtSm5EfURgFqPYeZqj0bX1bRI9qPHj3TipEc77KB29jrJ78NMJbfykhuEoFAN1U6DZep+iwSUAtDmc8iw4BJvOkIPUNBcUXWODZyJtvFIe4YfSUX993IYK43X6LgRrQp9Tb6ztAl3LHyekbMSUY23p45lpdSFAt8j9mnwsxOtzTIqza+l41XfZiBwk3h0e1n14C8r/z2h+IsrlB0zs9kKdOGKHL1UFgnZfga+/tvYWMuNP47pwxKTnjfHX+EsfNVLmvvxngo7KsWCHjDQwHKYg1dUXFTm7kIJCrJGt43fF3892TpYq4sjeFHxd8yaDOcywq3pMfr/bdzSWOCqjHEUCTYUHK6XOgv4dtPIqVNTk0ASX9lK825VdTwqGbasvtYLm7DzqXWYCAI7JM4K38eA2/HHaDthQGvfjORlS7ltnEF4cYtjRJn73uCjqETizqkDMXJI6Ei5EAzcUjVruTugzPUI9qQ02kRRAEgQ3isRPW3vb5p3mJ4j4yggsw5mPqqTEw0DNXiu96b6ZhhUK5SGOO1m95POZVdPfDYg2wrXcqGgSvRFIPj3kGazjIjG15C7spfoha1RwiiYIall5EpWfyZpWmuLxtcNbyBcio8vGLVsLv3UJn9enJCUcZKCoGMQNVGJ1mDQ1teydxgss4e/LHBKx9P7OiJvmHOlYZx9QILQ5fyw/tcbCtPAZViqjTgXw//E0vHno8pWz6CY4/PsXC+SakQzmM3cFiZmWLmwlnanMOM6nV1xcRhiiCKwtu+5NTTz9CYnaPiF7hry0e4fcMvcOPwndw4koiYTB9LGDin7z8UB0qV/rAu9e4nvs2BCwdip9SKgoJSukkmDxXfN3AvHIrqicPPainqfr3uEawCUn2dCvOjd1KKaoussctpb70DRYQZDFv6sV0RPbVu16PgdsKsnaITpECEHNmDGjmUqtDRFxM2x4z9MFLKmOGhKDrzf/ppnnzLm5l66EH8VfL5Qk2CeL1MXrenUhu4SBkyTjRFwwlsFoqJY2w7y+hqicOfifqIOg72d74UfrW5lkbmp5RoFSleFORpKZDT6yGr+AFCzaNELKW6m6Xfdusuew/r3LXlI/SbY3GtuiZ8ck5PVCQ5bq2bBL57ATVfSbJIdBK7OFwL56QXBcSEXqBl6BiKhRmAlr+ZbjortNKGf5rjq38XZtq8VM9maamUu4k9yA3sonDzxyhE/Se/+dC5DLvJVPLYOkj7CRQh0Eh8CXO2ybc+9aUY5LmuS19dQd16c/yZY6ezfW97I1B1ZqdPcGlrF5UokBsHPl11DV1zvUyeEj1OL3BRhIKpebS9ehT0D2jIeiYjuNLoxmqSiprd83qZPM8oslzdwU+P2TiRCq8RsVrSvSgDx0tYZ6uGRGJqJk0t/K3Lcq9CCxKfrOXVUKWRlJYAeioJ0CstsqLg3IqWFcKqBSfJm/2xcFvVGMFypgnMJJv41N6f4/SG29b4aZqic9XGtzGWD/0L1/cypTwtSngyQFNU9vW9hEv7b0X6iwxH+7taGCJIqaM2V/43BXkArqayrbadIfHiPSIsvQ9XSAqRQWx4dQatCQpaBfHUN2KZcgBVKPhmaBhdv42S6s1lqQUefvo0T3z/cTQvfOA1t0XeKMRo3lAt6hcSMHU+93bc+aQGp/VM0uOiudSI6ZpNS2e2HKaUITS0Penp1UOeb/GGhz7KE88lFNVOs4mzlIA+L5BZx02oeLNzuH7AP//gBDOnaihRFMEQku999s84e3yal1ZH44kHoJf3ouT7WayFkutnnz7D333iEV54vptZXEIoMV3Tkmu507loA9QUHU2JVD3VsBZHOk4mE1W2sjxtUcyhpDJ5I9ZIDFhaXi2zSaRBnqu7zFYKdN1kcaqrjMpOK/xdLXcjioTzp9Y2QO0pqbamT2OkQJ50JJqiY/d6IHXsmIagolBJgTxf0WnY2Uxey22j+yIuHE4PX0q8VJbJ1Cv4USRQISzMdfWAXKo9QpC6R6rQ4qP2GwbXFtTMfep4zfj1ittmY2EXHSvgJydU2l95iBJZ+qcsJU7epsIelBRNtZJPMjkFLRKJiIR4pGxRlEkmb/eBKhdZybOeWB7BiECeERlCdZWq4GRlD4PdFcbyO6gayW+9cfI3UIfDOX7vc6fJv+z3GSvuzJ63jDKfSDwZoAqdrp7MgUPW85nPK4Fk1EpsSRpwevYzOHqBbaVLw35AQFF46F4IlhWhMpbbSi5yrI4eTnqsOY0GygvRPenbjKnmMAuj3Dp0LVsqtyCDxXg99sbKzHRMB1YUjfxj2ai1qVTIqQXKej8VTY/PASDnqBhRHYDrjbBtKSrEj8D76R0lqi0YPHIg7KspbU42woizugrkpce+vpuYLO7GiOhTyDbD1sZ1PwuwsbCbHWeK3DH+Tm4dCyOxW2ZWKNgBgXsa6S9S1Kt0o/YIW0auQRNVcmqJiXxISSm1wpncP34jr9j8HqSerHFfWnj2yTjCCYC+IS4mOdc6zr1TXwagT88zaG1AejZefojv3hOCsEQkIFw/jWeeZu+Rc9y56QNUSdEeHZP3f+VJGlENoAy8eM1d0Xc5z/7w7uh4oUNT97rcvW8LimuT17x1ndm618ZQLLpCY2pglNODZcqFESy1wISeC8FF0OTswTMoQqUY9VVqyhodJwHDywthZr3nDPeZo8ggEUv66eGESlZSEjvhKuEx2iR7hxKkmgBHNSoTevYZN3e/NP671jC4dvYi2B4yXRxN4Kh6KNXeu3WWSU7alPR+upGo1MXnRph74TmCCORJAqT0OHD/NzCj2sGCVmF5Zorl3MXsqFaxtDxutF8rdk8hW0VKh+98+o8Ivvoo21ohE6DfHKPfGmc8nwgLPfBU4lh/7+sLPL3/A9hGmboW3pPnn36U9/7wvfF+notUUCdz/VzZtx+BoF65mFceuIu//p8H6La9OOummAlz5m+f38bhH/0oc8+G2iO4mklJzFNz5ql7K1xsKagipGq6MlSfdJrfxAsWmG5O01iYY9CroeVDB/wrQ5/nbvernG0fIde/AyVVnmC1kzVbOrWMG6ymJho8vGOCr/75/4WXchADGSBS60dVDA4/NMV9n/x0+D5u+BkRBnM9IZOASmATeHVM1YxtPoB9NsqIynVcy1TWVyUBlfHbvkPHa6FFKfGhKwbReyBPKthWP0YU9K37WbDqtQI2tSYBuKhybew431LOU/ZKzLWzge62l1Cor6/kQDU4vSkM1gkJVxxP9uZLjkbnF4E8b/hirtz0FnQtT6DoCGHgpDKL7cUlbmpcwftn3kIQ+HgpQRXNNPBT2a1DKw8j9DxXFzQUwPRkJog+bG1iu7IXvUdzTKlEeoHNmYOPxm1cOi2PXfODXDn4ivgzy9NZFldvnL3mo5w97vGJc+9lb9+NmfeEp2WAB4QtFFbX5PWYmH4UYMpr0PLqBDJAFYIVbynOvALUFmpsyE2wp3o9ipb1x0JgKJFC46lLf42jR/qQ3ewzTveidO2w1Cft+/jtXiBHklNzPKaENFtVaOip7H7HXkJTTNTUhDRWMb26fif0TTWTxZR/DSCVkJXQC14qQqFfD2Ifs6RWCCIBPnPV3g7QlX4chBSBn/GBbX0PvvSpGkOoQqNsDLDJGuKq6JkKofDTL32LB2+4js7zz9Na+f9ols5/EMgTQrxCCHFECHFcCLGm8lgIYQoh/j56/1EhxGTqvY9F/z8ihLjj3/ubShBg+i9OwQMwzSpnDj1KUc3R9bs4qQxJrU9NVL1k2C/DKIYp2yDwQuXIaGzIb+PH3znCyH0dthghoq7bJ8krAapQaXuhYXOjmrmcVmRkw81Ucnu5o6xhWQWazyTV8Md/+CQ7cn3s73spFX2Qk0NVfD10YjXFAGX9x2JEginamWTz6jRauKleHp5+muEgAYmKauDNzfLpbz3FhW+c4RuffCK+Nl2xqC/MYc959GkmuypJU1ojqtublaHD8PBX/xIZdKjVslQURShxJs8SVoa2AFCOotiq0NGjRdXVerVFTibLVC72Zb7bcmookcHv+i1GzbF4k2l52ToXPQU+FFXF1VQelClq7Sqd9H5NQxMGQumn6Gg0nLWcfWk7XGQplM/NoKVAnuaF5+lGWVivrkG0GenKIuVBC52ACc0GodDsZp103/VQpbIuXTOQPm7qHhpmP52ot5cQAomkoluoqah8N1VfpgkdIQSzrbMcarsM6UpYWxONjp9c57Gug6bobLAELUdHrTuUvWzWQSkm4OrivhsYNBNaQ9UcjltvVPQQFCmywbC1CWSXfGS8NAEDSxpbzJQSY3cHRvQsDbHWEALkBy5lz7zLTSOv547xX0zOSai4w6ER3dG10Ioj7ChfvupGhgZRSokvZRiJNpNn+PyWBznWTgIvl5qXxVROIAaVAkHQuZ+GpXHlYGKeLM2I619Kej83jb6J64fv5OrBV7Jyap6cWmTY2sSjb3871SAEwFYuPOYTzWWaAWwtbAMp12TygtJofGxVqMh6tn4hp1WjgvIi1cgZ7W0UgaKj9taC2Mi+Vkipde3QeVb7Qoc08HR0RcOmy2MLd9N0l1GkRF/POYM4y9+rfRBBhwFznBOdJnOr6nx6oziXBTdKaTsXb7yLycIkgT9PUeujlhK40CuT3Dr2Vm4YuZNBc4JqUwfVIF/aiKUWGDYTqoon+lHVahwoADDMIUzVYrYzxaMrR1mwL9DxmoyY/UjfZnrlGXQhCfxs788TziJtt835u97CbmcrpppnfCTl+PgGgXkas2BS0Kp00AiijIKumFz40f3Uvv0ddAxGrEnODFQIFAVpHyW/mqYfjYbnYSgWUraZKSucHBvFimzlRK4fe+Vz2LW/pNzsgfjwuUx6bRQ3ieb7bZdG141rYYasCZRUDWBrJukjW1YSp6lne2qF5P5VzRFu3fRWrht6DUoEwEw1G3jbWrwk87rvuvdTuvgtNAvj+JrJNZO3MnjjrzOgCoY0wVSuTl5Zoqz3sxzR1lWh0zo3jWdF2TIkXvPbzM6dJq/1ouFlFs+dZ1f/jeysXIkqVOYjRc8Rq8qAtQNF6SNwDuN0WigtyVgnqTP8UeubmfPMixVuGL6TPdWw92Cjsp3D+99HEO21OxqjvPmBACO6j1YEoiYMky3FPeypXo+v6PjOczQWn6E214z3vXwq2LG3egOzj2d1ArbMCNqtr1HSB1h2ZnnCfoaKplBSVXzp40qBrhhMGBYB03z9rz7J/F9+nKtZRJRCZ/B4foo/v+QnHFWPY5l9VI0BFrtTBDKgL0V9sysO3SDr+Akj8ZO8zFqVNFJFsqqicd/fvoAfCcj5qgAZlmcoQiVA0o4CGY5UQdoYSo7Anwv3UgTToyGtXci1dcYitR8LITLtVwA6XhtPeqhIqqN5PnX8AprSE9LS6dv3Gq6P6ssafta2dFouTnTdfUaWATIsxplrzWZokN3UPphTBPqeOykXx7hry0fYkNvJO+4VqEKnqFUZtssMWRvjIHh++8vYkA/ZSK5qIpvbkK0AACAASURBVFHj2m+A559NFJa//9nPMP9s0k/OdEbwUvvdVPs4M8e/R0kV9KkC1fYzIM8NfK7Y/GouGwhr6+vtlLKu9AjsKU4/FwZ6hCd46eKlmWvvLmUzngCGgOuKGteNvhFLmklrJ8KMLa62RuVdlSrFVS6SGs2dHlumQoGOXycgQCBpy1amhrIxt8KNQ7exr+8lGIrJhdYxTjVC7YkAP3w66cyXl7U96eF1QxXxXnZVygB34Uj0d5jJ64iAWbuOpRXiYAGA67fQFYsd+cRe5FaxLc65od2UeoFlZVW7h/7wuidL++J/VXNFeuH1glZB+iHgNBSDM60k6OsFklqKIt/J7c5kbt0gtAk9P1dKyc7KFZmfn33kSR6dGGDxLz6P015f3TY9/n+DPBFWEH4W+BlgD/AWIcSeVR97F7AspdwOfAr4ZPTdPcDPAXuBVwCfE+JFcvipoSkGQ+og/c76NJjeUIXGmfvuJqfmaPvdTHp2829+IM4czHZC9cuR/CQQgh99VUT76kb2QXvSizMQLS+i69jZSEfZGsRSBENDm+k8nwipLBye5pLyJLur1/CS0Teykrfwo1oKTTFw9bUGEoijWEqqDrG7MI/nJQ/a07tYInFiTKPC4WPPcM0fvpsgmnhKTDHN066vcHjmO2t+q8dL7kbFuLpiIoOVUFQkQ9dMoimGYuGv6mnS+y1VaGiRY6QQFjenM3le4GCUBjPfzfn97I4cgXOtI2hCjw3tapAHUPNDg6b1snbqJby8rFGp/QvaKjylCMG+8rWM5zbRrlyJY6xdCtLz2WmpbNG3oytmHEnWexQ+r9fwE0RPYEZZojKU58pciyuKRXJ08VpZRy9wXSRinXo6osxTAvJMow/H7dVrhu+P5UcQqYLediqKqGMhUJAIjjlQ8yWXDyQNgDspB2De9ak5s2zJj7IURPVxbnaer+7DN5KbzLyebT6DDPy4/+OWwi5uGXsLe0s7sCL6S0FZm7XMK4ljZLyIBLCiGAxsfM267/kD4Rx3g/UBIrKnRipxI/qSYyabxtbyCLWUsz85elPm69Uok3fH+Dt5/aZfw8+tPce+iEvfi8oNWuNsKe0j3yjwivF3ccvYWzirGXGWuWKEm0otsJgL2pS0IgqsoZ3UxMVxRiHM8q26d1oZTRgoQmE0uu8j5jAFBQJFQ4uyMGOlSzB6FFkvfK4zvs7JyVeyyB3owqAruqjmFbhY6BIKnSwA6q6KmPcbE1ySUxjUVTRFZ96Dp9o+5zpzNNzsd9OA4JK+m9lx2fuYLGxlY24jWlDDVHPMuwkIyeX7YyrxbRvexrgcR7n9jxnq3x/f394IRB8SP5PJM3LDmGoO11lB08Moa0898EL9EAtKB1UovKx/O9cOvTqes1ccM3jwuVAJ1YzoycNDSXsaTc2RG/8KV138MV698T3YihZTeiC0bRc+/GH2jb+Gl47dhRatGekvkm+vFWFw/C4dqUcgr8PusVt47bbfZKAQXt+QOcyQNcaguYFtbpaGPBR08epH49d2bjNXfeIfQ2aBb6MKjVFd485NH2QivxPmEhZBWVPoRAHJqjHMqze9j025pJD/2qFXM6AMsbGwm/HCTmw/69X5vhsLGwEZCfKTl76Tavk6JquT6LkKN5Y0ri9qXL7vk/SrFXJaiZUoC3Hl4B08ubSEY4U2Z9ga53UTr2dv+arw+QUeOa3E7LFzmd+fisSXrh16NS8bez2vmXhbLNbklUfJp+i/Z7UpaqmM51b/ESYKu9jX9xK2GJLbS4KrxiaxojYVl7uX8ItDfxEHhgp6iZtG3sxIbgJf+uyt3sDtw7eyKT8B0ibnzsb7YFlJbOSuylVsdRPnD2Cw7qFIj7xaoumuMBPtlwPmBnzp4UuBrphcN/warhi8Cueh40wWL+aO8bewq3IVUkr6p14OEp7Lhw5jQSvTDdo03VrshwDYkwU6fnYPDsxUy4MUyJNSUvd9vl9zOdmeRRUaN75pPJ7bdWucgJCuGYI8GBiPMkqo+KghTS+o84bJX2df301cWrmIfX03gVjroCupQKlAWSP93vVcPOmjKQqXv2aImgwSuqYwqFYTenizl1ULXLzAY/fSRopR38/CKsVpwx+g43czQlDuKiBsbXsZNw2E9mqyeCmuqvDGyQ/xqo3v4S1D7+HWsURgSkvfby2PNF38VALBm08YYucefYqlnyaiYZrMYafmi+23OWKGPlZRBafhZZz+R889ybTdZXNxb3TeybMNA6w+y9Mn49fbtaSOGkCrZ3UOynkPc5UvlKbNF9QBao21rbzUdZqhp+maEAaYW14dKX0E0A6acZAewF5OglOWWsAOOpxthUyxQIYq8T1ldFPAhnxCO12Za/PjG/+EVj7caz07pGv2fDLZWcZvRqwGxcDSLIp2FZtcyLDpBW/EF/D9DoZisKeYBKzTtsOXPmej2sfpsT0oq/2TsTDY2AtS191Fqvlh1ChgZOpFlCC8VlOxaAc+B5pRQgmopVTkhTAyWVNPKFg9sSEZcL49nWny7gceVXOES/peSqDezrD94nXxvfEfkcm7GjgupTwpQxT1NeC1qz7zWqBX9PR14DYRejavBb4mpbSllKeA49Hx/s1R0vt56eS7qbprG32vHmrNxooyeX4kmS+lxC1vjo3Mgn0+Pi5ATitlDNCKM8ewnpKflV7GYLSiSZ6OiKx0UnVzmoN7PhEV8GeT+gApJVIRKL0+QEJlJur/smJnKQa91K/Uk0mycO4Cbqqw1zNylFPR2YIxwM7JD7N06Stx6uEj6IELXTHwuw7VRmK0vGgDMqPIvWu70WdNEBo33GhkQZ5IavKEEBljlx6aoseNtEWwxL17NuN2OwgUVpw5vnHmU2jFLMjbmb+MiVxosGc7p3ECO3RcWB/kLRBmd/TIyb24+HJyiqDP6catLjLH77+Oa0oFrhm4gtHcljXvCz/VPFUx40ihERmuHrg2tLMosleXE9I1cz3hDOmgtlYpO7k+ucEdbCrsiPuh9UYgJW4K5KlCxe1EMvkipGtu7t9FWn6p46VAnjDD1gHR/H2+42fpmn5qM0Iw7x+hagxiiiqq0Bk0XpyC17sP6eF2pggaU4yrW6J+NeEaKmkFeiWWxehcZzqn4+9pepK1HbLWp1y3RRN98sZ13+u17khfWyPd8FQm92vFD4GYayTrolIZy4BsXcs6JUWtj92Vq6kYg6iKxkR/Mj969JTJwvoGNq8YCRW1L/lez/noShU4h6ma5LS1ztC4HEiCI4qWaUAPIVOgtz6He/VueomXlXVUqxwHr/JaGS8IKVdmd4TjW+/krKNybLhIW92Krhh0RBc9fzNtaZJDoq3K5DW7Tbxeryrps3vodraYKleUNyOlZNHX6Ep4rDHDfDfrlG8qJi0SLqpey4zdYslZRBOSfBDaxwta4gD1adnA2pbiPgpWsvlmnrV1Ew5BHHRouTUG85spaEWC7gIFbwqj/AuYkZjUOecMdjRnKnqR0bjmEsY3v5zj37gHACs/xpI9n6GSSaPAaDOJiJuVX8ZQE4qepRbwN1zMSCWMbW4tXcIrxt9FUbXYfH5tzUQnaOGiY6gW26wKk5UQFFhagYVueF9uHXsbt214G/0pYAuAppM//yO+efrPabhL5LUKv2U9gC50pu05vMBlR2EEU81xw8jrMFJM8YJqsmSHjtBEYRcFtcS1I9kgSmvlk5xuhhnullej6YZA6bH6DBeWHst8VpeNRHTL1LC0icz7051pVEVnwArXQMNPHM682U9fPvm8KjQujrIVUxEttn4+K95xLriAE7En5t2AFWeBqwZfwZ2bPsiu0mtpR4H5BXuRlqHy8GLSdkVbTuzeJXkDpI+lKJRyoQNlqamabncJQ80xlg/P+0T9KSSSqlHl2qFXM57fwcv6N1IywjkwpmWVSjMUYqDoBhT0CkKIMGO+cJCOF84LX3oZdfeqMcSFwTa7I1ZNxRjEFg6bF6+nrzOKrZlx9gMpWXGz98jtG6Me2cFe8NUe3sml/beGDIgUXVMiURWFjgTNbqMJDX/xcMwscETYfkqIBOSVR3tCarAc7RUDUWuXyeJethe3sKd6Heo6vT/VdFZYqGsUD7u+COuRhMr81BwIUpoHWdaWabXoeDZOYPPQ3DexAjWjzpwedv/N8fX2Ro99td4wlByO+uK5hjSI7ggLo6jipTJ5Y04SOBnLb2PQ2sSxetgnURUKbZHsoZWax7zaxJcBOf8U3spiJujX6L+Oc25yLjKlKF4xhsLn4oUZbsWbZmhVELavkwX8VaNNvvlkcv445LRiGAiWglo9jxYYa/QCFFT0oMiT+z8Y/0/t9QZO+Xwdr0EQ1XE2/Hqm3CaoJYwjU83jShl7kr4Mn04P8BirgOj0iRWklqNVDn1jr2sjSEBe0JpDRs3fFaFQ0ksUnCpdqWCpBaRiEMgAQ7knVi9vub165iAW7mv7PmfVZVbUcA1t2vvmuNygN05f2MDBVuJ/LnVfoGxUyaVaaeS1HBphEsMJZLzGJZIlNdWSyWtmAoaehJIZ+kb3zT/IXPNY5rcX7AtsK+3nouo1oGjkyMctVl5s/EeAvHEgvbufj/637meklB5QAwb+nd990ZEnu/DT/NzeMNUKllqgG0zFFBtX+jz/WC1u/jnfzXJuez03emPRnqZvVQ1UkBIEaXnhQupFRB5tepxPNVPt6EmNA0A5Jf3b8UNjo4nE+M4MhVQAexW3PidcdijH8AYSOoCzuIKdKqaWqop284fi1z849yU8z8lQGHp0TUWEEcThduJw22428tOO6ox0xQQpGRwIneeuF6l46f2Z++6l/14F+Mxek3L3JAPlHThtJZMJ1KqJ0/xk/WxsGMNjOSx0T8XOc8df+6zPmSH/fLJ0MdtLl+FGxniipa3JljipSN64WWRX+arM+65vk3rEqIoZNyo3oohNeeG56HpkTDoVKJQHrcyGUmqvat/g+5THwoib560CeUhcmd2IPddh0lAYs8aQSC7admPMaghkQDdVW6oJHYVE8n/Fz2aXOykqaICCPRACxP19N/Dqje9hsngxZ5sv3pYEiA0r8P9y997Rll3Vme9v7XzyPTeHqls5q6qUQQkFJARYTghssNsGQz9sjLuxabuHu+3utmljG2xsD+M2GINpE2whYxBBAiEhlEOVpCpJVSqVKoeb88k7rvfH3meHe6Vuj/d6vDH81l/3nnP2OXuvvfZcc37zm99Ea84jW4tUSsO8bd3/FWdHiloxnvN8lNF7bv4Hcdb8+r5drB7dYKI7DlrPZ1CueXuBx5cjKfaWi0EdU0kch1knlUmSAqJM3rIvKGgVtBQ9o7L5Fha8pF4hWPXbQgj294a1Ri2vxobiVrxo7s52XruYvTuKKaXNoVwYDLWiteMFLm/u/XOEEs57ZZWtAbg0qoMMpI8q1AzlpTu6Aaq6ivM/vu3mDHV5tnMeL3BQ1E2cH7+NocJGbuvfj+ZPoyk6LaXNAB9BXT5DXhFYSpbq5HZqPFTzeHhlkWZK7CCnmtTdRbxo5QulhyV7tYqvSiMFKtTrR2j7dfqtdeyPHPpT+WQTK2pZAGG8uJoQkhr+WTRpsKvyBpbtWaYaZ1GFRiADZpaeY/exZ1HU/hhtLcxOs2xEPQK9JocWH8183ZbZAVANcnqFyfZF5lI0Us/I82dfSNZZXiuiKQYXmuG+Yal5qlcnzs8l1eupGP0MW8Poem7NJtwKWujRs3FpJatQe6F5MjOPll7OgH3SypPr2YTqaiza06wrbGfP+Qq6YuAEHrP2HL1Gss4HWtn7ueiEQd5QbgMN2szb5zLvn9I3x7bRl4LZiCJpS8HkKhGBLdp8HOT1axrWKqd9ohnWeq7fFD5HaUGYAWs8g1C3fJfTrRpnbJ/jnXBtV4MsU2fCaNOKBG+mXMkj0/+EE9iYao79eoVR1lPzJU+0y2iMUvc7PDT1VQB0PZsRfXj+Xo42ZrH9VhxwdceSM535f9a1WUrZlqv735Z5v7yq3nvJzh6vKXrcSLypqAhhsmCH/oEv3Yzd0xSTAUPL1ATLaBpuWBjlpuYYF5phJregV1i2s7ZoamZ7DDo3vXANlzffzo7KVWwvX4GXiiglEqKaxKYI0BSDqS/8XRykdsgRSBln8nyhc+K+0F7pAmpB6DcMRk5pO1U2IFjLsFBTwa8Qakwx7o4WOm7gYygGS1PT/KMoYEa+UkHPBtLr1i3R8SW+yDNlz/PC8qHM++kstCUkuyezMvwTnVleWX4GCDPrR45/Jzk3zeKljaO83vihczj+u+GbDA0OZAKdckoN9dLem+n4LY6vhACJJkTM+gEouFVQyjTcBYqqwJ9+ak0940L7kfhv19/GcqT22W+NcdPIe1AiVdx+dRlN0XmlngBnfREY2K279hqn8dTENz1PuH62la9gW+0yfvXs5ayvvZLJJgLssnZS3/J2lqtJAKvK8HlPM4+aXo0ASaDUWGpOZ4Tz1IV6xld0gwSADhuSJO9pq/y1ucllbi1rbHnjBwBwmu1skNeYo2EkfpMQghP9z2IH4drN6WUC6fFE7lM4UkaBlcfF5klWvFZ8Hs82G3y5+DhNLfTLc6pFw1vmlVR94PRFjUUluWbbexEhBOsLydwUtB6MIHz+XGzc6BkPpGRFJgwDy1klIKQ1WYoYRvXAIshuiZnkxjkp+c7cEe69+Df8r8b/iSDvtSRuVjcde73P/EuODb9AiA8KIZ4VQsTNRbo9q7rDST3YdoT4FbUqllqgLToEEc3OlQGnDs3HTmjDXaadQhmNVdmKxc5kJkgIpB9/F0Ar+q2cVqTenmPak8ynaGQ5FPwUb76ckrA3lBymksv8ptBCY5nuYdX0GowXd7G7vJsNbpJt2ebvwknRNaUuqAwkG/u8t0Bbyhj5h9BBrLnhYukxBlFTdI6gk6VctYww5g4zOD5IDxA0IsejYvTHdVmQddRXnCzKmIuWmypU3jT8LqzSHRE9Jjxe3XZT/Nnzfm+MakPI2V5oJdz2QKziSQMnSqHxGs5t4or+t8S1CSK/NuPbjKirru8z7a1QNrKbiCM7qKlGr5pqYnczedFmVVgKN1sRqDH6qUgVM69DnN2UDHWyGUq8IK558fy1tYBp4RWBwGu12J9X4/+vuv5OlCg71vFbsQAAhDLYQoR0TQAlpex5cP77tDL0OwV/TKfprTCa34KPz4OTX+apuW+vOaf0aKcK7XP1eaQTOkl5rUR/lFkqru7tRGigupvNa43FiFr33PwPeHj6a/ygcjjz/orXjJ9rZcFBqDOZth/zTlbFVBEKIrB5uRium2o+ofuUCoNccI/zyPTdAMwsneb1xoH5B1GFiqZoTLZnOL8KCGlLh0aKGrajnNC1tpUvpxnI2L6suAtsNR4nGAzXxIC5Nos5ZlhcaL7KucZxVKFmitf/d8PKlTN1VBOdSVzpxHTlq6rXUDEGqETqsk2tzeXDk9StRRQh6DGzzo3fnKctYdnXqbkLmfdaqdowofSw5Kwt8j/VThxoveoRBOHm2RVtOVddWnNMd6yuBwPigOmy3lsYNfvRFINDjWm6wn2236SzKeDMDeEz2ogCU61Ww41qMqfbp2muqhlan78Mt3c7QgjqboN2kMz5luJWTm1MlEbfUtaxFEFbzuJ7DuaqLEPbq+N6LXqNQXSzuIZ10AlsptzETtachViOf97tcCGiMHXHZDtx2hb8DUihYSqbODj/fSZaJxgbugNN0al7bWZWKfm+ceDHM//PpiTYX5LHWVgV5LkXFYIoMJck2XeHEtrQNh6bvof7Ln6eydYpdpZ3xgJBG/MDXF/IgnrznanM/wUtudd7qtfSlC3ONcI6mprocMTWeLEd0JbQ8R169azdnC2pNCIb0fF9JE7sXOtCsJFt1CJQq0dsAWHG68Ucy2Z5JnKzHF28j3vOf5pDi9k+Z0upoPqec3/JvHopTy88Fb+mkNBeu2NmKXSWz9ouzy08QM1JnpWtpSt403DYn7EdjKKae+KMKoCTsvea0PgF879kvltWBLbaZvTie1lqXsdyFISaSpEVJ9t2pLZsMK2Frz2/8GB4fPT9w7lNtDrpmnmJORjan4N9oX0qrt+FEfkKgbYJX1ERhEqYPnmatsCVkh8qZ9ixM7wXg1YYrHspKqGuZSmTEO6h8RwKNaZixueuFnAipVF3epG+CEAKZBBn5LujZwAu1Fc4bUsumauw9dSLmfeXU/NiCJc3nXsfaddSNS/jlUio43zzGOcHEsZIWa0w7qxtOwDhs/3IaJLRbrgKIyPDsT94dOnJNbT1MwtPY0clFYpQUFNB3OzgdSj6VuY6FxmyNmB4RsbX7Fs4ypRIFHB9FR7xeuJM5IA5xpsGbkJhhRHDwvE7HG1c5OtnP4UvfYajzF53vfX4Grt6wh6UzzYcTs2H9sILHLZ3tvHjvJnbx96/BhTPq3mG1mfr3rUokE/3WuxQikXP5puTVFLJEW3Ri1u9ADiBGzMmAhmybgSCvMKa8pr6dCvulQnQabZCADhKsATNWSZ6s/vkpXtPseiGoPCgNY4vfU5dGKQZ9X811RwBMvYpAJq+wrJWR1MSH2e2c4GjneS8FUPnjtvPJ9elZO01wHWDP0WfGs6LlZ+li7XXPBe1mKqDXZWYquVm+ZvC13lg+nsIcy96NdkDH5v55wwbquHOU1x4MJOweK3xfyLIuwikOV7rgNVQd/wZEXYbrQCL/8JjAZBSfk5KeaWU8srXOxEvdbEB0JIr9JkjCCEITJnK5MlMc3Lbb9L0X9uR6vhNFlahZZIAmeIat1IPbdOZRLdUFjybx2b+GS9wyCt5GqleJWWjj2aEHlaMfi7vux09hXJ1HdcuGmX7bTopNLhrTM/Wj1CWfVzVSE2JrlHsq3DPuU9zz7lPAx6271DW+0IalypRhMKCHRqifnMsY0BFM3HUZjsXcNQQpQuDvAAhw4LXljOPDHx6jVLGIHhpOVi7SxsJ57YQ8fS3V5LzDRUQo0xeNUF2hTApkDhHgQyY6CQPlqV5seHsjjkzi4rE2Y5ChKJG2ccTtedZUp7CXzyD/cPf5UL+KVYPN7DRU5QNRShJJi/KJgZKeB/2VW+iGCGv3SxpF5VSkQw7q4K8QKJ25cNXZfIkAlck16EIBT/VZD6m8UV8hk7QIUhtXoqiomGBEt43s5U4dS2vRj29zoWKrJg0I2d9xWmw6GaDzrSoS3esWB2+d/HzPDt/P+rKAkvWYDRnqZ5rEUrbpTY6fgdJ8JrZ9u6YU8KN64Lfz6KylzkpWDjzBBfaobO44tnYMrzu3Ycb5IM6m1LFz7X0XAZKVJMXUBrYSCCDOAA9NPVIpApXY7p9hueWDtN5+Z9e85zs+gVsdzuzndAZ7gQuQsnx4szfxZ95sgZ+at27gcPcTOIIHCq9gBNddy0CPoa35Gj7HQattYixIgQX5GYCpYIqtFRelswmGV/qa8xp3Qsd6ll2oqCwMT/MDkth0Ah/r9BVqVNb9CgBZX2CQEpOzB5mOi3O0JgOQQRhUndXtThw0kFejiVnKRPQzOk+S6mMu1LN4ZPcI9u1Gdt5Gd+58Bnun/jimmto+WspVYtem9P1F8L+R0YRKSV1dRdLWrIGb3/Xz/HuP/sWAA9N/SMPTX0VM7A4ok1wqnaYw4sP4fpZL6KcG2Hhig+H87lyipZMgtPB3Hr27UyCpRe2n+OJ4Rd52f0utBfZGNXLdMeLr/wdteYUveYwulmmvSbIkyz6kgMLYdP1M40XeXL2Wyx0Jqn5Aa/WnmWqlYAOC04yD5PtzRwvX0e791bU0s/x1MJTvDrzIy40j3O2PceiDJ25QPq8MHuRZ7zvMTmfKMlOaEng9aD2DJ7M2h+jnUNGQZ7iO0x6Fg+0DiL6y2hWgcnOReruAo/NfJ0HJr7E+doED898m4a7hOvXeWo2AYjaRnarzovFGFSx1ALPy2O40d65go2MgLKjPX+G3Ziiagxl9umBrbs56Exzzg5YaWWzZV0aZ5e5UG7vQogQmJhsnaJXy4IpuZV63Bqhsar1TzqTF7JpdFpBh1dXQny5bp9gwc4GsMddjR/VXV5eqbFsr/C9ic/zg7mwtdF4cWdynii0TI9GtCYstUBHD5/pjt/h/prH0vH7OWN7saS9W4YXRsNA1JEF2n6D4ysHeLo2w7KbDfL2/cIgjR0r3H3mk1x0zuMGdpwNA/DT1D8pMUqRTLziUQuWKRa2YkSBu7XlYpjJEyJk3ACqJrhvxeOwOk11XbiHdctcjBQoU9azImqQDfI0YawJJKorP8IJJIZiUZ1NCF6rA1kAtVjkTG6Gs06A4TYpNLN7fyvFWKloOvPybzPZg0K5gjSv5LsXPsvzi4+x8+aEvq0pBm/Y/sE1vwkhnfDoQPI8uRKqYyWCaF9yA5snZ+/h5eXEp5jvyDgQ0lDQIh/hwNx9tPMj+OYg55svoyk6/XolUw6z76W/pmFBLcokq5Vuz77wvp1bfoKqOcSl5gqjuXFm3CmkdPGlR81ejGmIk62T1JwFtpb30xcBeefmPkO9/j1O11/ECWz2NrN069VMrFyhl2IqYlAjoMxP2XjXuo2AABUFx2myt5iA54bIMqhc6aF2BcMIQ/D1+TFuK+sMRFFel83VnM/ue51WmMlruYv4Cyfx5l5msprND334bZ+hp2DiBh55rRz2fBQCO6oN1RSDQEqc1GGBMLlYOc6uq94cvyaFQEvRj6982xjlbQkTqbfY4YmZrNCTpuhcXtkYzlMpoCmXeKrhcbg2z+7rkrZvq7PZlX0HeXl0gZZ1K0KEvnx3LHQmmaq9HNO1pXOBxdz/B8IrwEFgmxBikxDCIBRSWZ0K+Dbw3ujvdwIPydB6fxt4d6S+uQnYBhzg/+FIIwoSsKnH9DGloMTBhhvApksHeGbu+8y0z6H3fIRmhNymsyjPnPsK82/sUHMXMu0WpJRh869odFKocMefjyT0FSZbJznffIWyG/qQiAAAIABJREFUUmKummSTFKFwoT3PfETLGc5twlRzMTpTVsINqUs3tJ2VzANneKGxnGidZMpboZDqbSYMlXylgB20sIMWCj4dv07Z6OOGoXcSVJZQhUrHa7LiS/b13siWFJc9SCHBT858E6FWwoBHMaOC2rBPniBAtubJ670Zo+SllpQdoYZdxzS3CpmXUmYyecoqwZlcqjl6IH1aqWxrjznLRCvLV140sk5ht4+JXgwDsOfnf8DXznyC5xceoDLs03r0j5CtBZrr1ipQuYGNsao/SlyTF1EExUiZ2ef+B1PtU/GGLKXBK5OJU6cSMOBlxUuED6oeNQIO3IwiqeHO4ymJM60IhaCdRkjDTVrRwnnu+E4myDM1C0XVkRHKpnrJBhlIn5ZUeXT66zw9+x1AwS0qMZjgBG2Gag1UIXlUf4Tvi3vXOPbT+jwt1WHZW+Kc14dcWWEu6kE427zA8wsPZjK4zShjbEd9hIL/RVZqUr/InBsw01dENbZRsQd4snIZi5GTW/Nc3GgzzbsGA6tqHZuBFxvbUOpFIGXA9vUbqHuNODPk+A10VY/rBc60pyna8/zT2T9dc07nn/9DTA+aXjhHvgzo6+mwtZrQ/bQ7a3F/q6cXX2L2jRt5JP94/P5frvsqE5FTtxjV/+58wyZazQuxfUqPDm3mvUgVVGioaaTUWxt0N1JBRDcoPyCf5G07fxWnfJqcFtqenZYaO83VCGSYNOYwpURRprl3xWNm6RzPNn1OtGoEUiLb5/EVL6onygYrrr3MucI34v+lUs44+dvfMYYdKeqtOPNYvWW8lGx14HW4fs/bcI1rWV5FWzmy9DiTncSZWg4WcfHwRQV3Ipzbdblx7KCDBFZkFdtrc2Lxn+kdCe3nyLYKfv4OlsQ2pJFDkuPZhfvJ2WXaysNr5nGbpeIGDs66MgtKSFmeb53hG/Z36GbmTzVO8CeFz/NXw3eRU1cI6iEAeK4RnmsgffqXAhqteUp6LwVrgM7qeYuUAafsJU7XX+R0/SgXW8d5cOrLCLVIW1d4YvabtLw6hxcewk8JVgQonCldhRCCPfvHULR1HGoe4MnZezDKsL/8LeruIh3fZrHT4mDrfibOP8pCZ5IVZ56ZchK81vXWGtXhZmEMor1QJeDkxhxnLhFYeY2LUwqqkSg7LzpTdI7ey2xninsvfo7vT/1PzjePcXzlIG7g4OWy7AhLqcWgD8Cyk8c0NgJJxhXgQr+DXDpN2ehHCMGRpSf4xrm/4OeveyczuRqH2z7TGwRa7ia6ZKCjbQ9fShYch+0n7kbxLITII5E8NvN1Hlz4Bw7Of5+HFk9w78WvYOpRH0p1lLbIOrergwpbbwFKfO5WDvxW8pkl12HJqFLzoVI7g6KGz7Tj5ZhunOVUK53ZMTg18GpMpbTUAp4eznfDr2HLgCnV4UjDjrOF7R6fI8OPxd+wsdzk5YXDrIhhWm4N1+/gBjbfu/gFxvb0UegtIZEIbShDFZYIPLuY+l9S7AntgGEonNDP0mdujstOcpubCN9BQYRUaAJu/1AIaFhlBa03y9ZI99lNB5YQgnzdem5f+hhqNrAGqObO4EqJrhgMO8me95pBXqnIz5Y/yw3GpxmcfR7prRIJSvkkw7mNbGrppDN5eetVhDBpeiv0txu86T2JYMncs6/RMzcaAkGaTelK6Ftfib9ZihzLzhwvLSX7w1xuIxKJL31UoaCh4gY2ZxovIYTgQv8kG8+EbJMcbtwwPPw9sAs6h6YneGplGr3aVfUNbUjn3A95tfYM63NbMNU8E1JBs66mv2TjLSfzVisOcaL2XKb8QXOagBL5dwYbO9nA3H4NQHFdSqCuW+7U9bsDu856vorwOihoWF426DI0FzfFXHIDj/mo9OFCpwkpW9QTMZW6vklrIS04I3EbYYsDV3ZoPfZJmszR1lf5Frkq1vr1LERgpC99FFXgpQK2sK+0En/vi3v/hKHhXsY2b0zOk2y5zf5bNsFQAuwVR8Zwgmd5vTE+ugkpXGY9iR849A8nCR9dy7JAPrptP46WzFHfcKoXceFOLFfENdOz/iKHty7z8sYse2P1+H8d5EU1dr8G3A8cA+6WUh4VQnxMCNGt6v4C0CeEOAl8FPjt6NijwN3Ay8D3gQ9LKf/l3KRVo7FKvt9X23FWzCzmaRjholM7i+y/ZT2TyuU8UW8ihKAW8XlbqRoSAps9N18fFku6CY9ZUwwCLZm6ys4kGMgrdSoDeYQSGtNFe5KcYhH0ZJHEhtQSVUrVwFILtKJM01gzNMx9UXGn35ojSNE/8jK8JknAsVY2yyhME72QCvqQiAg9H8ptYKoQppZl0ODhtseB5We50Dwef152kgXjybBZueN3otqnABk4EQInCRoz5LUqadatJ5O/nU74YLpRHUVeydImO74bIYQRtXFVUOXmEhQjbC2QPOhls87BhYc4MHdf8tu5rFEpRmiiGknXd/sHmnov47uT0s/ijl3UVtEmvcBd08iyS5/t0jXVHRtoL77IM3P3cs/5v4wCGoPjd/1h2KgNUISk189SV3T0pDea72UcH03KTD2fgkLQTjZqJaoH1I3w3GzfjT+/4jZDtTMlaSerOkn205ceQphMtU9xrvkyoNBWE5qz77a5UXmOn9/4PNebf841/EMsvNAdX+r/Lt/tfYQnrupBs/azVNoS882VQHKi9hyLEcrtS4+234jO08HyXzvrFF/7yAEOtec52f8cttqi3x5B9TosuHUWOpPosy8wOP0sXuAiNAs9yqZP2W0avkRSiCmDUqpRy4mActlkye3275OUzSKGYuCr4byqxi6K/dUYBAI4nz9HK2gSCB/DaydonzvLm9/qUzHavLz8JEeWHuedN78dJTrWRpCrmCxWkg2yobY46s1y74XPMdkJnz/Ru5HgdQqmz+pHkYSOiqYYGKm1ma5bsP02DXc503LjwPyD2H6bk8UZEPDj5t2Z7z7TCGlN/Ub4bJzOT2BJiaa5BIDuG/jAqdYKP6p7aOoMflR/UPdWbSZOm5O9D9MwwjUilJ7MWlZzPh1MfjR1Fw9M/j1WtQc/3SzLq3Pj+ptQzd1ouWvjl7925hMcXX6C5XJiYxVfpWZNcNYJ6F15mY7fwlQt7GgOB8YewPnuR1jyDkBEjf+JX7+UQ8OfQbMuw1MtMDZgmNfyxmNP8cqGNo9OJzSobubs0MKD9F15JeXIViy1T/P3ex6MATg/cHADl2V7mXy5ROfg3/K15c/yzFyoznm89hKd3DCNziJCCIRQ6Pg1jq8c5Ez9JRy/w3KURXTRODj/PVyRbPpCFOkfH0At/SLfufDXHK8dRKao6ZVcuCcMzB1i9+UVFG0sNr9DW6v0FFs8Wnie044BUmI5NqWOz4/mn+TBhaOcHUgCzl+59t8hRHa7bRTXEURZMYHgwuUH0Pc2MPMavg+GeT1G+QMY5fdy63U/TWm0j67zPDWyjKt6HF58iG+c+3Oqg33cv5I4u/kimWes4GzAjOzZfD3JXC6WHNzaq4nysjrGYGMbezdvRGqhPekZmqPT08vZ6NFozJ/k3hUPFk+zbuIRrru9QE/5EkaWQnBptnGOo86T1MQGvOLP8uZquJ+q3jJCGjHLA8CNWlB0A8+WXgNknKkqFotoy0kmb2I5pNOKwKdcO4eM2izlOnVmTzzPMTvltAuDiwOzMfhlqjkcJXwmzjln6NFPs7zpOgLViEHFuxa+iaMltmJnzyv0KtcjhIbhKyy787S9BjV3npyWIxcpgxuMZer6FaEjUjVSEsn2a4a45MYxzu5+mvPDs2iKwbrCdtzAh55xFL8V9l4VAkOdZdOeQS75cJ7/8Mvvw+ivEKRozUaqPno1FdMOOjG7I5B+nC2M53zyEP7YeAziFY2E4VDzvTX7RqGvj379PLvzD6NIH5lioLzUmOOHudDOdgPEXmtL9njrFELJY5TezWWrCAMTuRFebwgUzFTtsA/0rKvEe7BQ19JURQTSeFEwZWDiBS6uET7XR0YPMzAf7lsmzhplS79cwFVyzMo+zGLWZe+dX+GUkgAAcy0doeQYrC6hTCeK7i29w9nGkUzQf/Oxs7iYsRDJkMyC0bZ8jSAvJUDYzW7FAHd7EdHnEEQBvRZk/TFFb5Fuju7h0fCW+PrkQywo2zJlPyqh/XW6TebTAaPv47QjEcUINF4qq3jK2tAhv2GUWS9plWZYGo5M1l4Q2NgyoowS8DPr3s4fXPcHFFNJGVcWqAzkmHryT5k+9g9olgWllOLlwC6u2f4yFyYf4sKJ7H4L0Ld+lJ58aOOVwKVYMpiMdDS0Vf350PM4arKWe/pSpVRqD5avMds5zzfO/jnLwQLuhlkO7H79kgf4P9QnT0p5n5Ryu5Ryi5Ty49Fr/1VK+e3o746U8l1Syq1SyqullKdTx348Om6HlPK1u4D/C8dZO+CMlRgXYSU3vdhTZqoaIos5rc7oth5++j/cTKEaFveX9naLhxMnRRRylHr76SmbLKTqC3TFAD35nSt/Mime1y2bnsEcir4do/xeFqNefsUoddsdDVnK9OIDYlqPbkZyr1HgKZrzOCQPXC5qWB1In+XOAsdT1BElZyKsBHkomS4BSXB0Ih+JakiPsd19nOos8eTsPXEGQHYSRNWXHhUtzAiaah5kQOB1CL0KSdCYpqz2ZFTv0ghau9NAek7slqZ7WkEo0hIqIEZBnqoyf+IhDjajfoB6irusClSzP/M/RoEzjcSQmaU8Ty+9zDNz94YKT10V0aiJcpfm+osbn6C6O5HnHVx/CceMM5lzcwMHU12VyfOzNXn6+CinR8DsGhHCQuLq6Qdio68gqfrZ4NZS0hlNmXGMBQFBqj2CIhSCZqqgPUKdrEjS3w5cul7eQoo+J5Fsf/Uu+peeiV8LpI+SuSbBpL8S9/jxfJuBq3sZsFqMv/VP2Pxzn1kj/vNo4QgP9jzDmd4XMQ3JxOj16UoHIEH22n4noWvKgILj83oYzsnaId49nOf9g+/nyMhjrFhzDLrrUf0OS26HB6e+zMjE02y88CPcwEbRcih6uNkebrZ5uulRUAfRCz8dTUBYS4IMMPMaSxF335MuuqaGSLPi8KYTLa5+4csYUW3K4YUf0j74t8y+0+TOPb9FIEDzmkkgK22M7ddT1BxeWnqMo8tPYKpmvNZcqaGbKj/Rk1Up9VVJw1sKG/2aFchVMwFbd8wpNR6vhoGY3+1nKZN7IKSkFWXznl94IKS/Rc/fi4uPMOsXeGrlbu4fC2kuveoKJ+rHWHKWuHf+LIcWQtpXSS/T9hpMF1fQADXqwdml4FxZ+xus2RcY0U7hR05oPaIwLtrTHF85wOLCSzRy4EfHGoGRWcsLn/scALOdc/jSI1+t4os0iNahYkaKo1aRH03dxfML3foohY7Rw91nPsmp+gs8Nf8jnp7ppy5bTBlbmY1qE7qiQ8PbwuxJx5AQZQk0VeVibzh30wNXM75yCcu9A3zs51SOjEmmUrVuz8x+lwfPf4EzjZfYe8MN1HMGz8x9l1eXn8bRXfzI4VaCZT7/ls/Ta/Wi3LSXDbfMcGPhAhLJ3Wc+yUvLT7M0tA9ZSUA5V3U4UriP/zH4LT5WuJvFSFtMiHBvUFJKnShFrnJaCCW1uYvEfuwav8hg6wTD0wco91uoegJWDQxt5Iy5g5udpzkVoRJ5JyDnOujFn0TLXUtLT6kAVseRShYYbef6iTA5FODvbv87PnrlR7EKOkKBPcf+HkWtoKh9jG7ZwMaP/U5s6y5Zv4OJwSRrNTY+RNtL9ob8pl2ZIM9XJM+7bRaOfZmOk+xhruJw3kho5r5UGfupdyB0C9TQ6etfeoqXd/0Fww//Nhd+9AnKS68igUIrdJb3Xreet287z2XnpygPOPzjrReZGZiNKYIbxCtYcpAdM222nn2EpdQeKrH51vm/4gcTX0Q1L8c36kDAqdohfN9GLbUwlkNwtdaZQUtRawvNSVRzD1ruZgq2g+E28DCYaZ/j2fn7QZjk11do5MO2NgudSZbUZe6f+CKH2ocYKRxnrh7e+67M/xN+SPvs35pjbGuR0rqteFGmLC8VXl5+kpdXnuL8YBNTM9l07TWcWO+i5d6AkwKAFBQUPV03K6kOVLjxPTuQOY8T60J11orRT12tEfRsDcWfIkBS1cPvunHvGxmsDGD1VPBSzIK0WvHq9gjp4MKX/hrdg86Bz8COS3Givcy3EhGLUm16TV2rZpjROQV4QuF8X+J0n/Z6+OGWx/nGub/gBxN/jy9seldRf83BSIlRG0VbtSedH38LZ+3XBiOFEOzoTc7tqreuQzc0RMS0cvVJHC0lyudL5vKhPW96NQpaAVURBIHLke0+3sY6M6ULEHh4vk1ZK69preSX8vjR/TaLWR/KqjeYHrzA4YWHOLr8JGqkP2CYKxiT4d4fSMlyUSAKd3Cm9m1etb/Jr499HHX/HvpayzH4bSlKRiHZXkXlrvuSQkrVO6EwhvMXtJdwekt4fhtTyaGngjwvcDCkQbpDmlSjPVUbjgHZ7ugqSnczeekZka6LHQPf4Zo8X2izioEfzldOY9ZTorMM6DRdPNJB3goy6t+roLCjdwt7+vdgWSmfTTi847eu4ILxKoXjD0evCVpP/SXtZz+POrwbX0DPgbvoOfogj1eeiw/1fYf8QF/syyrSxcxrHGj6dPwWmr5KL8IoECgBm0/+T8YmHqHSn86WK7i5EEBypYPQVD66uMwdjbXsHjJH/f9o5CydsbdtBGDel2ilZEEVqlWkHwovKDdcB8C6nb1oUfp575v24fUprJhn42Pyg2EGaMPmUY4tH8zwrBUjNHxu4FBNGZiiblIZzCGEQFH7aIg+nMBmi5+lhDRkfo1MbRD1z9D7diIDD7MQOfTLM3hqcqsK0aYfEOA2n+KFyS/H76m5PMI0yefuZF17Fwf6buL5hQdj5LBuRUXlQZsNW6sYInQwuql3OmlUQKGvaOOIKqaaQyg+ntOOap0gqM+gCz3mfQMIN5VW911aj/4RmnKU1cMLHDRFjXq6KXzob78KmoZ59C4mI1ECPZfcv1svu4LrrkiaQuqaQImCt65QQaFUYsmf4GzjSJwVhaSOrZsJNJQ2DCac6uG+cb4+9v3s+aV6KnZHN+AxVIvAszE2buDVMUGpFX7Wl2GQt2Snag8Chx6Zj2tGAKyUUIOCiJEwCJ34bJCnItOZvOiR1XIGLa9OzUmQv3bgYEe0FQn0rJzEKCcOpC999FR7DSEE35x9NDauUhGYb/kQFAbh8vdiXfJ2PC9b95iP5J5+f8/72LZdZ75/XzdpiRH1VOyqbbV9L3bqbAmlZud16ZrPLfwgptV+8c2fZd+2nZTbfWi+HTeaN3wfNZC4gY2m5ih4LRy/g41OMwANF7pzK7WIrulHQV63DUAY5BmqwblBKLamqHhzFG+8kStPTzH8zD/jTRyMjXyggO628KOLVFUTBnZgm6sR2/AeBBgoqmCkkhUK2Dx0NYqxk919FkQtUl5rLj6w+b9wZHCCurFE73D0rBrpzLzgOOF6b3l1Gt5SfP87fguh5NhfnaVthvfU2rCLw8vP88DMvXS8GTyZ0IOXnTlkPmzhqkbBVxAh7APBWfYd+Rz5iksQBXG2FVKvW16Nw4s/olxbopGDfJSdyznZrHTte9lnKtdTJieTZ3pl9mEA9rzl69wy9t+Ztc/wauMAl52dplfcgmZtQyJ5dv77rHhNPGlQtNpIVWcxyvx0M3n5kdC+2rqIM3kAMz02itegXt1E01zm2fFHOTYuaJAFLzS7xoI/j6IGrBtfj2pYnG0cxYuyxUHkxEnpsKtvFw+96yF+ds/PkR9w6CuHzo5EQmCzUNrO2SChwBulHO8rP8fIwEneesNPJLVI0VoVaoomJQpIgtAZiqTW05k8I29w+cw3GVh4EVVTKPVXEZHIRd/oVlZyG9BJ7kHOgWIjpfSsJUHe+J5xpLrKmRUKdtQIXCDoy/VR0Atc/tYNvO2X97L+DUlGpO9tt1AcqcTCT7df8hN0zGRNl6p5VD/JUlqXvz1j6/quXaB57QwLs49RbKUyaarNid5F3Iie7yNQe0I7JrRWdF3zDKy/EiFtelZOUWyGQVexETqpSrmP8h0/BkDtpkvwNEnbgFxrloG5Q+RLDrcpD7Bh5iTrpp/lmbn7uNh8FSewkYpNx2+ykpfo+ZvQ9SbIgCVnhlcf/88oBQVjKQwKC0qBUiP8bamoFJuTCGGiWZdhOg10pwFoPDx9F6fqh0GYbO/bwWcHxvi4/RiFX9qGNE2WnVmkgLE7/208D05gY/ttbt5xK4ZicMdH9vFTv3k15Q9+O3b6y2aO6fYZzteO8PDlc1iqxRvGr+W2D36Q/D6ZEXURAqSS1BtKKcnluy0RNFp5nwU/vJamaHHVlvVIgrhpudCz2TerUkZ1wudoxcvul6sbnadriQMZZGTj4+/bdRluEEnopwDhQmOJppMVM1EjgE+o8Me3/hqN9/1K5v2GtYwb2AT4aH06A1pWXVXZn4C8SmSHzzz6Oxx/+g/Z+9JnebHts+isLeMQCPb0JVS9qyKAX/Xs6Hx8lkrhXEz/4D/y6rEHOTgeAldNb4WCVkLBQ/o208VX0N9sg5A8++9vwHcbjJXWKgovmS6FxlkASr0Frnzuk0y/+M/Yx+8FJHPGEMdrBzmy9BjXvWsfg4Mu5Xf8PjgNmm4bX0psvYnQx9k39G3Or7+b4+UJ+n/j1zE8PyOYM9VKwG6bbCbvohPE+yCAGtkxv+s/tBbwekv4bgtDsTCCVEmT18AQViYhkHSSiI5Pq8yKsNG5FzOikvMIHId2Paobjs5x7+6b+Mkdqzu3gWGpNGSBlldHSp/b3r8bRU1soCoDrN7I3glBvhD+bRgJEN9bPE++bLDx777Is1/4tfh1f+YI3sUDlMb3kobK7t5yHxdboSif5zVRCgW0iHmlBA5GTouTG0YqyFuZOgBG+H/vwkF2nLgbvZgOAhXalYTx0msWuLpj80dzWUG01eNfZZBn++5rvn7pPgutaPDDmstLjkTrTW0w5QpXjobp6J6BZNO89NYwMs6PFNj4W9fRMROHemRzuKFt2L0HN7CZaCZNaHUrNGKeb1MsVPmK96e0Hv8zTEWjMhBu3gPjJdZfcikLnUlKanKzOl4DnyT46BpIJ6JV6noZ99QPyfUauFOHkZ0LoXMZjXx301dHUI1LMNgYv6cVLIQQ6KKMLspUtu2j4zd5YelhALbZIeIt/AZDm0ooapgdi5G3ToKY3f7hv+KyrS1c3wsV5BQfxw6DPERI11w9VCep+dgZHCaoTWDl1wqmtv0mulDCTBWQL1cQq3rTmPlkU7HyJoODvXEBsqEpiAixf3r2O9xz7tMMFAZY1xNuOqtrySDkzwPov/Yo5BLHaqQwwpHCSb6U/1r8mhesDfKcyOkwFAvpdShv2k5j+xhFO1J4kh6qUHnVToJ+A5+cMGilfKm0aqCQIpbmD0eQ4fwrQiFIKTt1HfpiWecHNYfCmUN0fUYJtOzwuh1zhm0f+03kdYn4QSA9rFI2+Kj7jSTrKBS4+oPw0ZdBCemOrpI19G90JT+/Uuentvw4u67qRwqVCVcyP3uS9rFQvMSPEL620OMgzwkkPY3G69I1N84tw7qrYHgfV45ew/j6YbRmDhH4CCUHCCzXRwkCnKCDpuTQVAMnaLP95DdZd/FhrnG+RHUxylQLNao/8DFzGrVAjxoP++iGhqEaPLtd4SMfVNl56HmMDeMM1lsUnKjupiuMo4SZPD+ao0ZPGYTgcxv/LHP+ZyM5blsq9I0VyVfyHFt+hgcmvwRAta+KUXg7fWYrFeStnQtXc5lTW3z1it+jPBKuq1JaxEDA49UneWT6n1hWNnPF6SmUoFsv6IIwGddf5o6ePXxm689jvPW/gjCR3gRe+2EUVY9/d8GZRTdMuO4jqNeHm5cfycFrSkQlHywju1m+coljy09xtnEUo/w+BmsNvvPObzIcPRd518lkaqrveXf4HaWfZefEPIWeCl6UtZqaegzPCx3ym3pGucpvMGw2yAmfkZUmJSmxWwZmz2+g5W7BKISy9cWRQQJNp7Ec1uN2oue0smUHHR3yeRdSdKpAhc9d+/u850+u5HuXfY7TfaFiaxpIARiMmAzVkokQgu1vegMAzS2hc9gFQrpBiqqosP5q+K+L9P3bf0huT9Cin1lcEhCgb90glSDgz2fnuePy2+LXm2YYsAglAWKEUqAV2Qez/IvohZ9kcHtynlouR+7KEOxSS8WQNaJuAmFS6O3j0Oh7eCC4NPwuJDkbDDfhowUpE2vmdYSx1gVoR+stXb/Tv67Epv0DbPjkf49fUxQFK6+jqCFDJj+6iY4RzlNBwsCGEgHJvdALhcz6GN86gLmrg61D/9JKPM+e4jIxqtNqhYGUhxKLOyiRSIkcGKfau4VOtG0NzB1in3iQ0alQzEZYFubmzex65Rjl7SGg1zHgmgO/z96jn0coMDwezT8hqPfE7Df55rm/QEaCWt0+NQUB8/mQ9q4FAYppoUR1dt6ZhymeDLPmutsgVxAo3X3CraG7jTio9xWFL139SfYOhI78lXe+h637L0fpDamJ9Z5Bxi7ZgBpR4lZ6bY53DvLx6z/O/e+8n4Ie2u6SWebgxjA71FuJaGBSEoiwFk5TNO7cfie7fqwvm8kTgmCVwJweBW6qouIGLu1KaEvm1UWGyyWk9GMFVcXI1tSrhTxqMfQnVoIs60VTjMwe6qYyeek9IMiHc3O8Zz3V8VEcsVaVWfVsloKsUrdhJufyxT//Ze64MSt+1N3T1u26hPyOISyrP9NaxhtLlCK7Dbv7F+cYnT7LwMJLSKDxGvXPILik/xIOHv1t6k//cXxv1WheFUVjsRT6p2Znha0n/4n1l+zFKL+XVqBR0MoMmmMETpNAgVJE2Ty3ewi1XUMRCpOtU5lfnNaabDhzF1cd/EMqg31ozjkKp+84f1qXAAAgAElEQVTHORaKS+UaCWC15/r1vOtjt7Nv3524KthzzxG05pkqvsDXLv1jPsVbuU9cgiZ0et9wXRxMdUe3VhSgLbJ7vy1h3kl+S+1mXaMQJ2gv4fdX8L0ok5dyaxy3jkkehVQmT+s2j+uuyXQLBQU3cJAR2yHtGsqOgx2xvYKIZbJlxxsYqaztvrZxXz+b9g1xdPkg5zsn2X71MNt2z8TsMYmPNZCspVxU6mSaia2yInbg5eNv5Beu+/Ca36hu2I8vBAe2C75ztWC4NJr0wXTDIE+N7KwShJm88LdlLEY08dB/Qnnm8zGg2616UlKsvGLVYsSrY/Z8GNXYw6ZN+8HKUmxfa/yrDPJeazhnH6O6uQehCBoBIMAaSpztfLnChihoyPUkG8/+N6/nw5+9Ja5x0nKJIRjbGjpj45dejUDGEvoARj5yAv02qm4wPNSDP/8KMpBUBqNi5pyKYeVZSDVpdmsX0FhGUUNpCIDzdrjZnNsQOQbCwT5+L3pflc4zf41WNdBTjktX4ljRd6IXbqXPT9BV0wo/pwQegaKzc+8uPG2EjgyPuWM57BdTtyfpX19C0UYwSu+Oj0/TNS950zhmTwHHd8NMHj6+3QpRCCEIGlmFMwC9nQRXm/704+Frprnmcx2/gaaoYaaqi+Ao2eVYqCRBumLoqIUSD03dxcNTX8M0dYQWcfwJWFHrDOWHuGTjZiz9jbTkWvl1tfgujOLPoA6G4gG5/ftBCHJajqpZxVlFXVo9nMgYKkJFem1yo+v41IfuoeR0Od9BKAlsO/EmU4roka1UJi/dzkKQrVMRBMgUbKWgEthO6v8I6bR03vzof2J84pE48BOBR6n+NAB2+QQ9P/Z2xgYS1TBf+hTKWbrHzt6tTEdiIPPOfAj3pvo+2aWsM/yni8f57cUlyPfRu3UIs7NEAMyeO4DeiuqWIhCiKYL4WrWlVxlotKjW17aMANg9uQC7fxJ+5TFQFHoG84BgvqcnpD6X/g2m56PKJJOn6nncoM0u8QA7Jr5LdbTKllP3ACC7mTz8sKWFUmTZmcWXHqom4pqQqb5orldRZKwoGxSIMJPXbc9wQg8dz0Zpc+bz52ov8rUzn+DWO0cZ3FDGKBV5cenhuD7x1l/aze3v384W6wnoiYK816Cu7h3Yy6ITAS1vvgUUf5U4i0CvFplun0bRRnnjl74S339fepjCo6zO8UfX/B7XX/fbMHY5ir4xPloRatwDad6eD+fhto+hjodOTzeTZ1guCIk5PhhT+vJ9Pbyy8gwTrVcRIkeguPQNbIuzgGVdy9aXDo/wjt+6gkuPfZvN8yvkqmVE9zmQAaV33Rn+HW102yvLjOSbjN88z+DV62ksdRBCoFmXItQSl9++ge03bgddh9YCLy4+yqnOKY4MPcqW8Utx37nIv6ksZjJ5AJ7qoOkqlpYquI+CvAcnv8L3L36B9VErB6Ub5BpRSxQz2g+6fY5YZSMUlb5142yfCtHU3prHtfs7kGrvM7wzmf9Cj4kW0YPu23cfJ9d1UPRxFCNC8EWOdlRDLJQSqrGFofEkCNSKBYb/239j07e/hTYwQGUwj5a7DqP0HnRLw8iX+FJwa/z5nA2BqtKc+zTf2P27pMD18PvMtRkVPwrMVvfKAlDV7GtCEdw2fYzLz0xR6Omjbbpsml3mBl9h86UDfG9HimVi6gSp9WHli1iqhaPB0EK47/jCASGZGLVw6yEI4EuBH2XiN+VCe9rfM8I7t7+TL/5UCJ5KAYPeRKbmpzvGiqHz10p1WBYje8mn6tOuPZGih0ZBXtcOF1FwozoZ1Q8QlglI6vf8Mso79lO55QZuePw3ufrgH1LcvxejHSkgOnWMaO83Kx/kzEaNjtFg38Aezv7xj/GB68Nm60alilX9KHa+j7xlMbIl9AN2/cy7efunfwchBP25VKmCovLRj7yf9/zRFQyMRMJyUoIQIfgQjfH+MdpBskcrqMgguWYhBJqatDXypY/Ynufpue/yueo/ogglQ6/vUiTTxztnHiGQkjOr6I26kqVue6mSkXQ2t/z+S/jKjQP8+k0fobdgcuCyx1g9zhfznM1nAWXLSvZ3Q1MyznB3XPUHv8Gd//ljWNsGEUKJg1WAa0avWfP51JfT1Je50F4r9C6EwnWj12GYAlVP7ctRkFelxMn1DY5uXEGNbN2/v/LXUdQ+6l4bVag0vCUWXv0GvgLFKHMz6yxCpEbeVXHtjgW1jcCl1JxANyw+/KHsM1tcyFJZAUzNxCtadF76Cs5Dv4enBqzkZrnPuo7T+TH6830IIehVtLjXXNNdyegBNESdwy0vFv3zAwfHS9qLqJG/ZgctArtGsHQav7eC77XQFRMzxdpw3TqWyMeJDel1ELFfGD5n6Zo8TQnFaWTEdlCNVOuFWodOhJr7ekB+0CZ/zTUIba0tK1YtfuzD+2kPN6n1hTY6P7IuAR2kT2EopS4fgbuGmUs0M3LZrPTqoVpFfOBP71T58ptVKoWhpPzJd1Hy+fg7dBmg6eqa6x3eMsn6GxfAKDCcH0qCPNPkiZlv8tz8A/ziH17LVeJJND9AL9xObnA9jF3B/278qwzyXquRnn34y2j9fShdB1kIiv1Jc22jWiZohUZHya1t1Bl/LkVnK46FQaI5tJWRXC3Tt86K0rpBRI/76R2RwxIE5MsGmqliWBqarrDkJ4tk+dAXyfWd4xf+4Jp48s+LBu/b8l+4sH8ca2cvxugieB3Uvqjx6Ogok8VwgTbdlRhh7S6RTi65TjMKPkXgMzN0NftGKjR6fhZX2wjAzs5+2l6DljuNYWn0jhZRtKTIWZFZJ0YtlfF9F00x0KSPYzcBgRQg7RrOKt623k5Sx+a2bSilEloqWOuOLtKhK2ZStLyKvlqsVHlu/gEenPwKQtNRixXsoMVM5yyGpiFSge/zO5YZyA+QzxnkxeYw0E8NScCdv3sTN//iLfFrG+76R3YeDZWKRooj2Gpy7avRNAA7ReEMcBCqipLPUx2K1FADB0OxwvsaLdJyRAVppoI8Q0tl8lbTNZFhp9loKEJFcdI1e1HaP6VO1v10rjWD5pwNX4scmN6eBOgIpMeOa7I0w393+b9j1p3h62c/xaKXpcQAYGUnUvHtkCNjVVB7etCj+6h57bg2sUvpaItmnIXSV46g+wFbp//XRcLd0TMUIWpBBSFUrj78BVCUmK6pajlUvYAtHZRtN6FWKrj6FkQkBCAIM5FC+hg5DUSOl5ee5pWV51E0ZY36W4YPAlgRXej8oED3WtR9h7vPfJIzEd3pP9y2g+Yb3sktHwybYI/lws16cFPUV7KcINJfvvl/YOY0tl69Dv0tvwuX/2I4T2JtJi/tzOk9JYrbIypwhMgLILd+CFdT0N7gY+3alQryfMbVw4hCHwykmtYauxFq1MvK83h6/occmPsec24TK5qHrlqrrxogA8rrO2x+2xz6NT+DjIK4Qk8KdAnAjUyl2hvWH/b0VbnyRNJ3TevrZWRLhf6F8BlTSyWcUrgeaqPj7Pk3ESqqhWv5qo0e79h4ksKQQ2nAwnNSNRqqwjU/vYXtVw3T97a34G7cwbGVpzhUforHN/8zAFfLDjlkJpPXHUKIjFx1N1u+YE+w4s6zaWQxmofwXIa3humz6v4d9Fl9cSbvtSi2QlHYOrvM2184xSf2f4j1H3ofN189ywMTX+K5+R9Q3bIFfvpv4D13IYSgGq3tjuFyzfvfixAGev42zMqvIITC5e//TQBGtlbIlXTKo8kzq5dKKIaBtT08v8pADiFMFLUX3VAxNCWzP+YdiVOp8Ldv2MZspY6vwNKBv2Llwd8Jr9fKUvBmimcJIh7Vanv8eqM0voHhWgvFMlEk7JpaoBAd37CSLKJqahlblysUsDQLWxfk7AbIgEIutI21gTzKckgd80WOzfvD5+LdQy02l77J1Vs2sqN3B5e985f5hxsVFAlqw8YYX8fmv02yjQCjxXB/a6eXxZv+I0JNZqo3lWFQhcRVA/yotqo/10CJomMtCFByXfstKfRWGfuLv2TTpz/Fhv/8G4x+4hMoUS9IwwkzeQBCKWJH6n9berIiIFa3vkxqKEJh/a6oJYH1+n7Ktr5t9FYr9G0Kv0vItV7RUH6IOklwpAgFmRHDEOhRkKcpGn7gs27PHs42jtIqRHtOSlhFy60NpOwX/oHvL9QyIGZ3pNXO3ZSIR5rBUKrmuWFbPz975XosXaW1LsmexdmWQDJlJcHFgdKDcd1tfCWmSfvZL3Dh+A95ZjxsbD4+uAXNMDDGsnVPv7nhU1SttS0euqP4Ez/Gd3f/NRdbL/C1M5+IgTpIKMxv+tDvM/CBD8Sve52XASiM1VnpCTi4eznel/usMNN9rj3LDye/yoOTX8aaP4uvQMUMz+1U4yzu0mm8+eOsf3lVSyeRQBeGkeO+9z2aebt/yWOgMUXv4qpAu9pLqR1A4LEzyh7v3zZDT9GhGjWw327k6auHc970VtDVpIwFRXLOkXFtqOudw0+1lilEAG5T1mh+7zdp1k4i8zkCN0xa9KS0CHy7hqlYCKGwNH+Y1iN/zPpdb0OzrkUxwr0qU5MnNDzpIukqsibror3UxrHDGZGKz4ZbFkJ7qL1+OHPbB3+VN38gpPT29Pcm/YmFpJxeH5HNszQrBjis3NqEAcC3fuuNfPGXwv3eS9nKilVl3g4BKqswjLAsSlGrknyKrtpVRbf9NgOXFSiO2NC3jX+84y4q3fWpqlxsvcrJ+vMoikCrVrHsEBDT1+2CDdfCavGWVeNfZZC3ekgpQdPQR4YRkbMmBFjVZHM0ykWCqGOukn/9yDxXTqJ6bTDicVtltlZbKCQLTY8M3v/N3nfHSVaVaT/nnBsrV3VX5zh5hmEiMwMDQxocEBEGFkkqoiuKhFVQP8Puqrt+htV1d82rq36roi5iFiOwoAgCikqSzCRgcuzu6q6qG74/zjk3VN2qrurpme7Rfn4/HbpuTue84Xmf1y2LmpATOC0uc8klIIRg0dpO9C9uwcDxLWhbvdiLChC7DKUtj0TW5yeTmI5N2y/CvOwytF51HJJnLII+dw702XwAV7u68LMTn8CmP96M/aN+Yaw2ug/62D6Mxn0nzzT5Ay/EueMx+tA+gAAlIajAoGPH6CYo4qVs6+fG6K92fBtPHHgA/V/5r9D9oMkELEEnVShgFQughMISmc9DdpgPrBX8SYUwhsHvfx/ZSy6qus8y0qFRHU7EBAUAyWwLnh36A/YWXwRRVbCUn5pWdcMzyPZ1LcDTfcNoM9sAykCdEkaciuJlYqOtL4XFp/m1kYQQEBGN6ox3YkzxnamdY5vx0xe+FNpHyfadPIv5k1/74iUAgAOlnUhr+RAlISEcurFAs2wtIJtLSNjJY64doq1SQuF10oSfyXMC63gRd9cFsfbAJsNYLOoZaSDiabs22rvD6f1Tek+DTtOwXcujrQShxiKGCDMLEALCGFRRj6XYY2AukMECOEw4vfqjiCnCMbBeEOfvH8OprAcKQGbDASCNbUgNbwNLp0EAlO1RaHoWcbMDRVpE7tqb0P6e9yB35ZVQT17N7wkhXp88PcY58NvHXsKmkWdAGW9sHgSpyCKb4rl9eQOF+sa/AYEKFy6YKOLOxjW876arsHz9BgDAyz75Obz28jcivYD3xFLEfTdZCcs6V/k7PvmtngMWRdfMm37tiEpVJFYnAZRBiAymEOT6+vCNDZvQcXpK/gSAG1WzEg8AfSd5kxW/Fyq05KUgrAtq/BXYf/AxbBp+BJR1eM5uMsvHs0KsHcR1QakLPWUB+QVwRcQ1lvHHU8WxYAtaGctyI9rIpUEFlX7b0BNg2YCgCDiFLtMmKGf5wMQqDbZ4HjI6kkiHnwcNdMdd+8bLsfK1nH2wtvdk/GhjRceeKCcPxHvmwXss0aIXsKZlK15+BR+rcl09ePstt+GqC96Bn1z0E6/urCqTJ2CI8X9UXMviq6/DkpwB+vQd0Do6gaWXAfM55TTbwb9/m1oYSPOsLiEMREStc705XPPZ07HxphV4zQdPgpkL9JpKh8+dZ7zFZWsUWojXxOmasVQCp8zhGR+HAspLj4AO82xTJV3zF/O/jAe6b/HuWRQuee8qXPlhvzak5z/+Az2f+xyU1lZsagd2pYG215wNlEdx3UF/3GO6GnKS9VgChsIzedR1oJWHocd0LG9bjg+u+zDSIw9g9JFv4YK1f0bfcUI0TXfw8vjXwAz+HrXH2jEshgp37z4o7Z3Q110cOt+eJB/zQ07eovNB3u/PVWp3FxZv24WefYdQZgb2pUoYygzh3MyHsLb3T2COFE5wQ7VpZjIBoqpInnEGspddCpZMghhCiKg8DCNjeu9OSQQRYxVGGWvjc/PmLBcRm7e6HXNWtqGlO0ytj0J69hww2wEDwQ8v+GFomUIVHDIqatODmTwATNhLClFguRb6j1+GsatXoJQWlLLA3KSZ1d8V4KKsxFByq5WT7UDbpxLxA+RBBgM1FJw8pxX/cjGfQ5OqH0hyBKuoBAfbzB1wXAffUm/Fz3Lf8gJD3rVoOqwXHkDmiVvwx27eBL5D2EAsqaEoxKseLvwMj8fCAVz5nvd/42b03/x19PzTB4FsCVmdO+tjgX68UhQluX49spf5DKi1r+7DyNjrsHx1BjmTj3ufP5di03sv887DJRR7ii+AEIpYsRyia24d2orh53+C0d98Am1DBdy78we4/UXeyuGr53zVy+xoWgw5wx9Xh0ygfT+QLI7CGK3I8LX4iu59mUHMTs+GnnoKremyd45KKoPEIR7gemn0GSDQXkAKo8gp2yptCtXNJZQExuwRr673QBxgiuo5eTnRPuf5oYfhloa54ibVYJcLcIZeAtVMKOaJPi284v0pOzYcyO/Ody7HvvsulIWTV9TSwJu500tZdSZPIt83gHYREGlpy8KWLTeIg0x3AvssBy+MPAPWz51hRhmICKwmU9UUYgDYNTuLp+fzeSwY+ktpKewZ5fbOyL4nQTUNyVb+nFnWH8ulU1tyRmFcfRvwri2AkUKr2Yr8pZfz9RPhAAXLZKEKVpGqM2DtDcA1v0E9HJNOHqGyGF5It8LF7J/9FEpLCyiTTh6Bmg5MgKk4Emt4NFvJR3vmAJDK+oMMy/gG8co5Ot4w20+jG2n+4LVRPhCoXV1Y+OQTiK/hRua6S+fhuHXdmH9iJ9a/8SQMuTylThwLsdV8nZ1PfBW7hzdBWZKEXZiNhFDVNBcfh1k//jGUVh69VLu7YFMXH9pwL6yyP+DMffa7iI3thht4jGYsPIG8+MQ+zGlNwCJxL+2+Y3QTUsK4ax9Ieb89sv9uxFeE078slfKa4yrEQVlwsm2hLlqqUF9kxbDMutbTDZaojjRIaX1KaIgiENo26d9/oqpQMr4RiNZZIDICKuyufCwPwhiYU8aIG3bkHVrboQCkkxeu9Rwq78UTBzj90XJKcP1KYdiaf87plSfALJaxr7gdjDBktEBm1cjDdR3sL9zl/cYCDgZ1ATsw8bZYIyCBiBQlDCTgsMroekusNbQOwO8MURh6tLegt53Xj9JA9HXh+Zegpc0/NwmViRoSUl2DYCQqM14KEPMnGc0T7FCwr1eBxhb6dE2M4f7dt2HP2IvQ1APiXP1r2b/Id5pHLwrz6TVDQSzNJ/K4fM5p7mRY9hgoVbB/ZAteMp6FuWQJUmdvgD53LhJ/x2vLiEu48+u6PJMHQFGSIGCgcKqzFBXtMiRds6QSxFYv8sRfdDs6aqbmcmjbuNHfnWrg7M6ncMXAw1X0QQk74p1sDTxXlapQOtqRVr6KMfteADwbKyPD/mTv0zX74geA/pND+zzzTA3zn/k2YrGNWJB6EUsEzZqqg9CFU5LtiEGlNop6FgSOnx5OtHmTfTLnR7+ZXcSwzscOJt5XJZMBc1z8cOtn8MCuH0ER68fW8Po2QgjaTu3D7/b8HPnTA+qj0slL+O9mIh3+fitpgqk8X7cj3Y3B9GD4JlZmaQWkESozO0EQApzStgUtC9eEd0UZ4mrcy5RoJHrK7P/iF/Dzf/wCvveWgPPT1Yt5RRcsETbW2/pTsNUSbGpFClAA/HopJdAMBWbAudZy4VY8wWCIojGcOq815JqZJUBNJHHOIu7oVNI1WczA0G1vRWnzPRi9/7MwUyoOGSKrGT0sI9+XRDLnv9MsnUbyzDMAAGM6wfXXKogN5oDhXThrLKAMrDKsv+QK/9z0JHfyxKPW7QI0U8HXXv41rOpYBaPThPX8XWDxgKGz/h+BBecBC3lz+rSexrA4FXvPXhCtuv9ai9ECnekoVCwigb6s5sqV6Ns3hCXbdsMhGn65eie2LS5j0Pg98pQh7jl5CBmjLFZtS8Tbgf4tP0di+EUYs2dDFeJVJbUMk1U7bvHWGL645kZsauF1domsgbOvXlw3kyeh9fQgXiyBApiVmVW1fDjnz2kUDCxkSAfUqynzasNLJvw+doH1dRbt9EsUMBz62wpk8kos3PMW4E4gqfiu+7Kt+Pnw5zGy/z6URM2W5TrYnhjGrQf+C7dnH0CZuFXfuEerFogpMW8MB4ARYadbEewJb5uVKxE74QQQQvC9C76HtMo3kgFpALh7+y2R27KYifmZvSBO2WNj3LWUorR2KQghuOBvB5A+yFkO6UQKFLze2wwEDEricbPWVrxQeAr7SnycXtG+wgvaqUp4XNzZoaP9gAvmEhzXG85OKhn/b1OP47Te0/DQzoew9dBWbw5hqRRKB7fg5y98GY8eesSjpQOAWzEAWPahkCOvUg0j1igUcQ0HEgBjip/Jc/j9e37oEaAostui3zLAnV4JykiIvggAlutCJogV27cri6MKyiUhdKYoQCcXuSJqbScvCDOd9Bh4jFIkWw38tuRCefmZoWAvLYv+zrFoJw/gvseOkR34QdIfo9J6Gi5s/HDrZ7Drz98EVBXpPn6/yUJfkEs6zCV7FDTbD5i+vdt6w/WY/8jDoPHweMGyWWiibzAhhAc0W8LMgEock06e7F5QEo6CCxdaLzcagpk8FgsUfes64qs70PPRdaB1Bs903ve0g4YgzfQgFnACFLFvVgyrD9YCbePHnPXNm2EefzwAwOyiMO74CAbn8Qk4XlEfofb2IrF+PeKnrMPbT3g7WP/CUO8SV2PIdIWpkPEYfylmP/cDULuE/TsKKO4vglARdXEd7BzdjLhwKHsW5KATn1JDCMHusoNtgirFkkm4IpPHnBLcQ3zgscX2xAnTl9woOpNa/ZpJJw8IqyoFQU1+bdmRURBVAUsHslA9y0Bl0bg4ZFusDWAU1C6h4Joe1xwIRKVqoCvRhTG1Okovsy1lpwQ3IGtuBTJc5rJlWLVpO/YUuYpdu5C5BQBKGazSwVB9QhAEBG7gPC0tAab7AzkjCoBqwwWBwd6LuLsOoOhgZL834BHdn+jaFy4GU6r3JXtVKRGc9nSmwoiZdw7Q6itBtI/xqOjvZ+3BoU4dC576Bui238IY/Rpeft4ybBl+HHduvxmGZoNQ12seff+wBZJW8OW27+OTHd8A3vqxqmPLLIU8LRl02XLgD3hm0/fw4NZvQqmoMVRkbQZxvX6O3Fhm0IwBUKUbJEK4idSgawJALG5AtinoT41f6MxPRMPizC5ktLFQVi0IJyK4EaJrMhVIdCCp/ACUfhHbtt+FHY99znNSZIRYZnIH1a18jOpfG9rn7JP60fPSPThjyz/grPQn0WMmoWduAFU6oIvrJJSgRQgGwBVO3is/xZu+ikhtptUfG5ldREnj28rAGpLcyRuzR+DCBU1x56T3i1/A3N9yQYyB5Sux4V/fgcGVgeymzLzF2zwjI54Jv6fBTB4ApPI8M6WoEawMVj2+E0JQFIIY8v59/eytVeshVe0AAvBqvSpVA73zi8Vw46tPxfI+37BqufqN6P/v/1e17vGnd+Pxs34Ml0QEGyJgBoJkSqY9tCzVanqvl6oxLO/L4htv9B3VWJGAmTH+LgFQ1bBxrCZygDWK4p++DmvHw+hN9uLPLXuxZ/v/4pb0f457bpXwKLHWKDCyGyxgVCuqillLlvnXZSRgMhNFsUmW7EVrrz/GGnP4nE6D0exMH3DZNwCdr5fSUhiSmbxCIVDn44MQwsf3SicvYNB1fuADGH7tmwAAepnBZgAVDgghFMsT/DpUyw7XtRnVTl77uWdg9qYfg8CFNjggFDaBIrNw56tur1r/VUtWjhuErAW1sxMdBwtoLUdv73T794MS5knTA+FMrazJA3jtuaxZDhre6YhpCIAndrVbDwd4g3NeUQuUOsiWPRHNttvjLfjkqkex7b0r4RBJ+yewkMB/r30Y21sKnBpXSdesGAekSI2EOod/1wdivn1y2Zu7ser3H428plazFbOSfLyjozxA/8SB+7FzbHPk+jCEHUaVEFNAMiXa+xPI7+Uq43kxLlY6ebLbiNrlj0E9n/k0AKBgCtZEBQPlYFcaLYcA3QIyFe0VWCA4ZOgJnN57OizXwlB5yAsQJs9aD+ICB8t7ADdM9ZbCKPI9cQC4Fdn9UZKBpvNzOxAn3MkTdMIM4fOTTfaDFAO6FMyB0tWJYJAhltaqgv1lwMvkxW2/7nDYyfs2Y3D8jLBfokDjcc8RVRkDYxSvevcqLDkjrIA/+ttPofTsHSCZ6DmfM4VcXHP7NfhJIJCX0vi7MGaPgNq8r3QsxZ+zrCV81XtOgCvbS9nVPgQhBDQiYMUyGWhl/p0VhqrFASOvt6G1phvEc3WIvMgAnc2ryUPImauXyg0i2cKNrMqoAtL8BbjtuPtw9ylPQpMCLVa0kEQl+jeuhtvNkJjd7/224tP/jYFbb8Upy+fjPS9fgBNntYS2obqO3s9+BvqsQSxqWYS/X/55jAUog+xdN6Hz7HDUPi5etrU3noONZ9sAAcpFG4QoKNjD2FfcgbI1gg5Ri5Fpj+GN14aN3vtGbPyhINSikkkQcUwFAN3HpctdVRHLKpy6KKjpOHoAACAASURBVP+ZkSpHbszyP/ooYxcAiGZg/eObsfq57ZyuqVDIZ6209KElzSd/kxIwwtBitIAwBcwpA4Rh0+//HZt38VS2O87jX9O5BuUo4RWRRSs7RRAaaM6e8CcVtbcX6WQai595FmMHN6M3Pj8kFeyO7q/qiSaz0ERRwEr+AKa2dEPVwoM1QUQmyDNQXKgye+1YvsEsjK1gJk/VlNDkKOvoO+fyd7Jr4Zyqw3S0p/DY/nv9Hy7+f8Crvur92V16Fqfc+25Y2IpCWkdiZDvmP/l1xNYMIn/i5f6xFAvMsIFyAT88UMZOy4Wiq/hOy+34efbekGCAhKzLU2SEU2TyiqX92L7/DyhqFGY6PABrAaeWU1tFBiamQDFPhBrfAGJFqPNW0jVV33hLJA0QkcUdzNeO6oVQI5sUhDTs7IACXiVdE1oM0FNgpoPMA9/CvYt2YG3XWtx87s2hfk0AoJAyoCWBjuNDv2u9vej9zL9h7prnQLuWgMSSIMJZMQLUxnxeGLWuw+fOxYJmTV24cJBpDYg/2EVYMsgigjgkleYCEOBCGGo7z7ZRXYeS9Z2feKaiHsbL5PmZ+ngm/M7TiixCIpeDkUiG99Uevu4gCHwnTwpx2MzFrLMvwRmvfzfwpruBi75U0yH3Riham+pfCSWXg7FwYdXvlFEMdPD5JGfkMLCktWqdINRg0CcRvndMoUi28Hsl2wG1C0epf+svYRZdkJjpOV8xLUz/yaXCf79z1Tvx6Q2fxmvP/A6OFy0ImsH/vvJ7uHPri0B5DBjexftCClDGwAKGi6qbvCZPfN/LU89i/ZX+/UqdfiK6TtwPfZ7fh7YSaT2NYTNATY4wjADu2Ls0+tnKUgslz59DRiRumMw0EIqz5o7gZYeehWHZIcojjcjknbpuCZLX8npTlslAE3XrRbWMpF49fqhMxQdP/iBev/j1Na+zFoimYQHVsazaXwIAxAcC9faERlLyAU7t9DJ5dsmvWQ4EceMrl1Vt97fnvR7fWvklfHXlP+CAUpHJC1CbiwEChONyo9aKaLYtDeTH9z7uBW+fzrSgHGjFYRGE2spEoZIS2zqfj6tbW/3rT+YMJIe31fzm2zUT5z78nOfk2RFCWR5OvBZY9w5gzZtDgTqZESWMeWNjNs6vxaGAEei3bIiMkdrBnSOzVEbyLC6ipP37P+G2V7Qi1xueo4v97aAA8vvdqpKDYFD8xN61WNK6xBsHpJOXPv98xE/l7SRM20ZO1E8DqLLlNFqoCuIXHAKIANz+BMCYCkvoMqRFHXhBOxhy8kaSDHN+8QuvPvT407qx/nWLqmwky6VwxDwVc30b6SnaCW9EDswLjWbyaCwGt8Q/cplJznXFPcaPhDO0HcXHvg2qRieFeBsEFwdLYeGbtJ6GFHKT4juJLP+ezCS/nrb+lJfRLDuN+RAAoM+bh77dv0Wuw8C8VR3jb4Bj1MnzOLyiWXgwhexn8khVdL4RyDo+p/REeEH3CiDRjmte/Q685ryrQYWT55Ybe0CxOa3ovWEtSOClpKYJ8/jFUBnFm0+bDWOcl3SgJY5CIDqm5rLIdIYn6YQQgEidey46L36Fp9QFAA9v/znu2/1DLN26ExkjYIQeH65hCIImkyCiBwwjgCNbLDAFakc7iB12jCoj7gB/Fk5FJssqhxt3R4IpnqIiURQvsgpwddOeAT6Y9rSn8ckzPgmVqWC5LJhdhG4NofOl50EkfTTivIKYl52Hq1b9bdXvVJDhy07R60cFAE42XFfX+5//ibahAsgLf0BW74QZ6B1Ix0aq6g4LwsklKMEVNNrC9ocAujWkHAYAlFQbLkRG5CmFIZxTvbjfpwaKiB/RDfz5wH1wXBuqooSUM1vb+f3UO/lgbPb7AQiJbDqLxw8EON+KFsqUEMaglYfgEGA4G+jBt+jc0OSpKTYUMzyIBzOWlTVyQCCTJ508EZlkjosxVUFRUdDaGz5nVdB2KGQmnh9TN1UUy+J8rIgIWMUEmVQDGQVDh2LMR7zlZJxy2euqt41CRF1YJaSTF6xTqnLyACDRhhyzcMl7FKQXa6CEYmnep33IbFA52cFpbBEOc+KMl4Em0sBxG0FNAyv/8K/IbP8MtIAz2tYtsnpyPJWGEnNRYkXksn4WqW/bHXCEI7x0fS8IAboX5cGEAewSUkU1qQmvJs/P5DFNh5kKqOFtDFNSKGW46hOfw/KXn+//+PqfANeHlekkCCGYk+EGUlrzv+OFG1djxTmnAF3LgSWvqnmKsjG9pVWLSE0Ebz/h7fjShi9hQW4Bzr3meJxx9/VIH3gW686vnriD2UoakbnMtMUA4jvbRlzFnJN/i9Z9j4O53KiR71JSD59/pWLikvwSnNx7Gh593aN45Zobm76uTLwdbbYNWGPA83eH2AGUKSBKYOwgJETXVDrCWUrSvQzpgVGQRHUNpURKS3l0TaCatifRk+iJ/H3uPb9G75d4HboqghipEdGuwXPyCFTmYrCX01glEwdApKojAOgByr0uqP1FJZrNAQAb52zETStvqrm8HtTu7qpMlsSliy/F6O+/jIP7n+QiXoFlwSyyFF4BuJMnnRNGAoHyeLVD+5I2G5s7LIxqQxhShkLLyoF5fSzwLduijrtMqp2mjM4dk8f3PI5Rcd8eae1CwfKDG5ZiAloceMt9wOt/XrUPgNM1g8jNycIFMBZsCUT95xsFczl3al1BNay0YUJQTU4lVk20x/332HOWKfWdPMG2KlstMAPMmlRClOd0dmL945ux7ilff+HUE/4G7/zEPSHxKACgs/j8Z5bccJ8B+EFRAJjdMg+MMqzt4iwPLRDsVYTNm3PLSB/c5O9Ac9A9L+M7X7RcVXdZcFxICYIDcVH3bBVRtAtIidYwZ847H2QsENQnDoiqeoH/bGccPfOzVXagBQWu6AkdPOw+ZHhJARAO3DSYySOKAohMHqvx3YTXj96vzHBWZo1npWd5Th4VTl46H8M5b1qMMwNBLJlIKkVktGshvmY1lt33S1z+gbWe4zgejkknj4mbHs/xFyDI66YBuuZEQE0DQz94E7TMrvCCZa8GbvyzZ0CZGROlZ29HcdejEzvQBNCZNlAIRDuMmIFMW3jg1SrU0uas5APOkjN7sOyMVZj73DPoPFiomhROufx1yHVzesyKc/px8sXcIKKaxidsgPfZEV+0SxmU9o6qTB5Vo2+8LMI+VOJRHmYFVbRqZPICH5c/KPB1ddNAzwJeizP7+Pk4rZdHo5IvexlWXXwcTjmF3wevbrN2GaYHJx3xOYjrK7tFMC0gJNEaNpbMxbxPj7Wd9+HSqP8BlmFVRam2F17AQ3t+CXXWqBfRGd50JyijMGPhQUOBL0e9tyhknWOil5Wioiwio3Z5GLnzT+fLpSNGCR7dfw9u3fyvUFUFIARvmPU7rGzP4uyLxfcj5Xojst2plixOyW9CSd0M9dyIyJGIcjkEYK2BLEPF+6UpNhQj/K4oAYNMIRFOXrspLkVExQRtgjkuDgq6dL4vXI8l6wN8A0a8LzEFkgJAIpy8yiho0ADSFR1GQke640wYFYXQNcFqcJsCcJiUjvbf/xbTz+ZLih3SPUg7Lu7dsg3XF6uf0bAQ9RnuOgHY+Lka56MAN/wRWPt3ILqB9KFNgPVkiJbaPsjfaQIXuP4h31nUbYypw0gFskhtex6GLZy8jsE0rv38mcgsno3UaacDAIxEgxlPwHeIE23wIrSKgYRodXPShbMxb3X1uxfPZMN0TSMNtEZnfQgI3rrirQB41t47dMR7F4WRMqcgWaR+m5VGoTHNOw9COfFn5Z/+HcedUu2MBN/NoJMkkeuKw0yooXc2HajvoKbv5CXU8PtLlMYzkw1BGrWj+4FH/gfsuPP882Cs6vwNZnh0TbWjM7QMc9YDb/ltzWcKACk95QmvALUzeSd0nOA5+UEo+bznqKl57kwmR0UvxGD9pesi2VXEwu9+BNrAgH+8Gsp7wdomU7A+Pr7h36LXPUykzjkHidNPi1yWSXRh9pofoFDYBgpWs86SEQZLzDFFu+g5AfFYR3Cl6g0df/wYVsI13XYga1jO+eOBLejfVoSt4Dl5ex/36LWHtAT2Wv67YeUG+H+0Hwf0R7dCMJXwc2FJDbk3LsId6fsj149C5uKL0feVL3u9g+tm8gK4bP5leOUsXjM6N8PfXcIY0oUi2rItyIlA/NDz7/THePgBA6WzA7plQ4lQLK1EfNAPflXWNwY1JaSY2z+f/M/Y0L8Bp/X470tZBObY8DBKwRp8lWLjTSvAhA01ZI9ViYUVHACizGhfkr9H1AWGrQNQRRYumW0FGwv06hQUbmmry/kdbqWTp8IlfE4qOoH6WTvm0efdgJNcK+MWBU1oS6gV9PdI1GABSrpmMKDwg5M/5gk9AfCCngAwe0UbjHhA2EY4ecH2IlF43b9+Fpf988f94zbISpRo/K5MI8iLNLryGN0zGurD5gffJublUcMAS6ehz6koZiQklMFIpeLY+ditVeo3RxKEEJQ1/xz0mBmqyQCqa4tmr8jjN99+GpqhYNH6s/H8f3yWL8iHJ841G1+FNRt5JLsyak5EFoyBwpERCkXlaqYvVRg9WvQLSF0LrmPjjpe+Bp3FkXR8HnItumbo41IU3nhXnQen/DQ0w0Rf71Jc+v6PomuBHx0hhKD/1edh+J57sA2AKowatz67gx9OrzZ4ZM1h2SlB0fyJRjGijSNneAcs6yCUQNZvn8HgjlQMjm4Zzw49jPNu/B5eeONH+I+uDVCCeKxCUYlosB0LP3vpSyjao1iKS33DjzHsLD6CrYdeQM+qHhiLlwC/h5fJC0IVg2BWH8Pp+o+A9HvkVfL/p9VOLmEq1rS+ALR9Hjj1tdXLhSNwWt8ZWDH/OGwFrzuoDCKoig1ihN9NNZBNroxQAgG6pjAGgk6eI841PxB28jRhRFZeSZCK0QhdM7Qt1WDEFH8yagQNZPIs8X4HJ84Ws8WbPDwH5BX/Bjz3v0j99B0Aqse1h3Z8H6nkbMT7++tHt+KixkTc96IK6AFxglh7FmbhKdiKCbT6BvGB45/FQ+k/4b300tDuHC0cjKCahv7Pfw7rf/lT9C1eioYhKYTJTn+iV3QksiXs3jrU3H2vAQKCVR2r8MiVj/AMEjMwZo9F0oSjsO3QQ9hZ3g6tLTpzM1kgNTJD3vKI53vCuQNYuDZcS5gKOXmmZ0wmKuiayXgG1XJLhwFKuaP3yLeBsYOgJ1wFPBQ490onT7RQAFyonRWOPCFA+6K6h1OpiqIKWBRQHHhiXJU4Z+AcnDNwDobid4QyHEGwuXNx28CJuG+tCeAeX7U46OxVvC+0lpMXQLwzB2wBlvaP39NqIsi99jW1F2oJUNWFC4vX+YTen+hMXtEuehmory7Yihu382fg1qj7G37m3fif6+bgvlt/GvrdDvrI+STAtcBgSeG8CFshrfNnc6h0CAfZMDrLedguhR2Q47fGcbYyegbXL7++6ndzdhaFewMtn2oElyUIIdDmzAFGORuobiYvgKyRxYfXfRgfXvdh/0dKkRkt4tzVp8M+dBA2oQAhIeElJkoNqoIdEdiaB/p2Ay3ds1FSAM1C1bsZes+F7ZozcvjE6Z8IrZcQwkatQwWU+wKCbsIZl49xyLYi6JouzJYYPv1KigfnEbySMijgrb5adD4maZlkyMmTGbvV53OhoHlr2sXvFXRNaDBz/PsaDUTpdUf3ssFukBnQYCYPCDiaNTL/QZCIGm++gP8TDCgwwXrzGCl13jF5vTat/z5XspWaxTGZyaPCqTPmCI85KJAio00TzOQRRcGsn/8M2UsvHX9l1I4cHjEECjxjsXioJiMK8bSO89+2HMef3gO1v98zZkmidp+YShhruRooIxSOKG4jTGTyKgxmGiGyAgDMseCWC2jbtR9WYTcYAttVfAjdL/4KA8e3hKk9qgqmUmx46Gc48/HN0ISh2rNoMWiEoSajYqWyaNCdHT8qFmXwUUFHLTslaKYfjVSM2s/dKWwK/T1GnSoqQgllAAqowgAxeRDHAaEUqUQ4S8hoArZrYcQ6CFtmEuRzpBRL27pBNt+H2b2DgJBGlrVDwZogrTLSJR0R4lOcq2+AcL4qa1S95fw8FuQXwezz1d0qnTyeyQvvI3gPo+iaqbyJ/uNbkE+L1idi0qLiXAxKEUuFDTZJ6aXScRX33YgFnTweObty0ZW4caWgpEVc+7tWvQtZPQuFKjDialVdWF2w8TMkriozeUHFMhVZIwuNav7zaJkNtC8WG1W/xyW3hJcKz0I3GohkwM8+jKkI9QtkmQwyB5+FYo+F1qcxB1aKuwIXvvv9KBpcHjqZjKYuLttwLnJd3ZHLItG/ltd59p2EYCYvLjJ5Td33WpDTgrinsvYn6r2LQsJQ8NLoc+jOHpmgXvqCC/j5RWTqxoMeU5HrCjvcIScvSNfUwhlWbZzapglBMYDhHUDLHJCBU0KLKscF2QwdAJSOxmpMKkEpQykpevuNMx8nzzoLsVWrIpel4jo+vexiuLP4OMYCdE3/YBWtVyKEXkLLCcHxV56G1a/og2oeZVsB8Ix7yRahgcx1pfCKzOQVygWvpu3xXAEb578Nv5j9PPTBaOfYtTJY07kGBS1MO3MC362e9A1hKRZNYtX3Qzp5APB/e76I/2y/FdvhAk6AGRMhnBXEPZfdg1Ud1c+YVijjKh0dUDo70f737625LxqLg4zsxnD5ABcnmSBkAHXPZz4Dt1zmTh7CwU357lYFOyLwj69huOEahvZEJ3aJW1aZ4QkKr9RzgNpa8jj9iS3o3TcEtS/gUOh8TJHlUWWihcpOXNfFqAOAAfcspihqBApRkC5ZGLb8OjU9nYRS8suabEHTNeIqTr18vt8cvIquqcMUc4AWELxSQECF/RjKXjZYkwfw/noAQLXxXaB6dE3XdUN0TSbmaXklrE42VjJ4GiSTTBjHpJNHdIb0Kwahz+ETWSiTVWGw7hl7EXvGXmxq/0o2O+5ky7JZmCtWoOtj1aqARxJq3p+8Ze1We43BV6JnfhaxlAaqaVC7ufFVMzoRAUuOytYQioKySBiB2tFeZfxTQ0HXB05C1wfCNArX5aIb8+cvxZlPbIFBiKd+6Vb0npr/zLfxiuuWhgYtaRxQFzAse9wIjFQ92777Qdzx0tdh5cd38hSqYOxPN6P42He9gU1m8iyXYHCxT9dUI3sGCRx4MvSn7VrV8sAoAoT3bzMFJdQsFgHKkEqGxURaVAP7SzsR7+jBVZ8QdDyZeaK8N9ail/aCMea3NxAOazA7p1W+00q46XEkbdYzamrcP2k8Mwaa9qkPwV5SAKCqNhSzkq7pByeijG3GKM67binaWwWdJO3X5AFA1qyu+ZI1r3JClxOHFnDyIKSR37nqnXjD4jd45y8RP4Ubpq9Z9Br8+rJfc0Pt9B4sPq0Jx6UR4RVFniO/vhGLR4xbzdYQjQdAIDMYocg5xO9rR3u1hHoUZO/EykweSyYx99nvYfnTXw6t353oRm+KU7lnLV+Fgskn2CV9YaGoCYMy4LiN/J0OZfKEgvEkZfKCSInatKgMco0d8H+aiBY3g84P/V/Me/CByGz6RBCsvaMB4ZUqumYTFKeGIW/1cRcBhODpg7/HCyM8jVNF11QM7E0BJQZoETXBjeDhKx9GJs8DvqSByHwttCUNfPcta/G6NTww5jsFPNPIfxStVEQz+kYYQy3dSax6ZTVV9KghO+hZemqN6Hcwk1ewCh4FreyUUKQlPDM4NK7GwaOtz+Mr+e/DEgJHwebUZjxQry2cB6NSgAk8CCHv+171IH6Yu4urPgZooZYTnVGjqRSM446re46h9TUNc+/6XyTPOKP2OqYBpTSKn7zwBewe21ZzvXEhWRuFAopPPe05ecHAsnx3lc7xM3mjBsHOLEGL0eKrxlY5edV0zSgQpiBWskAAJDr9b5DE+Bhib/0xrB2PghoOnEAdZdHmxUPBqZtRBt0NCCCC96gm8LUz7Br9catbKACu0ETQAroEClwool1HcDymWuNjmcb2YOzhb6G1o4Hxos69cxF28loq2vPQek6emPcrBV8mG8ekkwcCJNf1+NL8wcHHi9jyf+/cfjPu3H7z5J+ComDgm99A4pSTx195EpHt9Q1pJugO66+qVnCrBW1wAEBzxsrcedxAUIiCnS4fgKjI5Eknb6SwHdbuJ0FMA9RQqttUuDbcUgFL/uWf0XrttTBmd8ByeEalSslUIijwIWpHNNEgfjwnXKqeuYTXsTWirqpQBeXNv0bp2V/wDBsAS9R+lUGxIECJimrDMfCd70Dr74ez9zmA+E3ibdeq4rJbpAQiQjhUFt5aYwAlMCsU2xRC8WLhGXSfeCpyXcKYCWTyPBD4mbyITJJSadCxsJMXCfkMajwjTwSJMiAWaD8inPI12Q60DhVAFbcqkxeka9bLqGgDA2DpNOInnYTsFZd7EfFcplqV0AvyeD/IGk5//+mzIib1QJS3TwgxBDF3VTsWnDj+5OuhAbomxPjlwMHPXvgyfvkil9tvNVurnQ+5vwhHvHUYOPfh5xBLNpadJ6Yw4BRAD1BNiKJAi6kwrbBa2HXLrsN/n/3f3t9l8SmRWt/tYSHg5GWkk3f4mbwqJ6/JTJ6/nyMzZRJFAUtNjqgLACiB948E6JpJLYnkhg3o/MhHvONOOqQYV5zXuP1x3524d9f3veO5Vgn2fs52MBUTv5tHcN11DEouF7m7RiCVBA+XWbOyP4vWmKCFkwpjAvCCZ/03fx2zfvqTwzrWUcNb/wRXBHaCQirBcT/YQiGYySuLOTqpRYsoPfje9fjVO08HwJNtt7be7jc7D8w3yaSfMba7ucMby1c/b0qo9216cBU4Y11YGDsHALyMYyXmP/gABr/7nchlEwVhDCZTxqV2jrufwDxd2rIFTFUwvz0Zyi5SXQcxjJAS8XjIGlmPFlutrhmka9Zx8oStw9Jpr6QD8Gvc3JFtGL3/05jXmwkJr5QLO7Dgya+DmQHFd8JACEEuFqChZnhgSdp7thJNT6zK5Ll+ywYlMB/OibUCtujlGciONxOw0lMxlDfdBbNesF7ut8YYKdU1g0qu8r/ll8XqzJHS7jUrexFPMo5NJ0/C65UR/A3Vv/0FoXvegCfCIT/CykbB9aAPihqmJib3bJ6LnjCiokT5ZEEUBrWj3XtR9+57BKP3/lvNGgW3uB3O8BawVAr5v7sBZm+nN4FUcrElQsIrGv/I+7/+NfR95cvjRrwlXTM1yh2oTPv4BnpCTeCGNzO8428ZLnr3P2HeiaeASRVVy0Z+MAsRWEJ7pppSYS4+DrHVq+EURkDp77Br+BkAMpNXOYCNeXl6t7gNI3d/CO7YARBCoVQMPK7r4sWRZxALtgsI1OSF9q1owLq3A/Or5c9ZZfa2gq4Z7P/kH0c6eTUmOc/ZJECsBbE8v9/yeQ2mclj9/HZQxYWeCdNstIAzW8/YTpx8MuY9cD+UXA4d73sftCx37lraomktjutU1J5wSptEZuMFEdcxyQNGA8IrTJc0FQeHyntQcjhNsjPeWaXY5e+v+jmkRbAnnWxAXQh+3ZJDwnRNQBgGlcYCZaHMovwGYB8BJy8jIslMR1yotdLJyORVvA8yk1erGXmt7WvJ8E83hMTIAnTNhJZAz6c+icyFG/nCI+HkCZEtRLQLAGMYvu16FH7FnUyVqnAJwcH44d1XadDSceiTjUBSWqkXMQ5kmMU4xVIp6LMay5xPCygy+BUMHoVr8spS5bkikwfUdvLaUgb6W/gyOZbIgGawvjRhxmA7nNHS28G/vUwmusxEiq98acOXcMt5t8C1EwAITsheCKB2Ju9IQTdj2PDYpvFXrIeAk1V+8UWYhoZf3HhqaBUaT0Bpa2vom3zTkjcho2d4w3e571rqmpTWt5fkdqoaUptU9PB5KLoaUoJmw7vRteP+0FjDKAMoRTrmPyOa4t+T5fJ3qVyjpKdyZrPgYNUrBuE4FhTRt7FojyKtxOC6PJMXEltpInFBY8IZq+cYMr80KQqydr5yDgWAy97/UQzuOoAaHUsA+E5ePN3YvD1RHJPCKxI0poLGFGTO84VC/B6JfABbd8VVNdUbj0UM9rVjr70dOjNDRvvfZ2xYB4r4xjjba8LJa4auSRQFllvmdMYxQZ1TGK+hkH2xxL/BvmxBuPvvAyz/w4/l8ig/KxwC15fXnX3HHV4WKETXFAOfkstBWRtu9hx5zsLZHNhzECfc/E20DYw/IQ+mB7Ezx9+bvsVL0Ld4Ce56Gy9S1kf3gxACJaPD3l+EVsOYoPE4nJECN4DFPbHdcpUju//QM2AaF79JJ3QUDmzhCxgDq9j37uILKDoFxFOBCJ80WhkNvvT83/Xviz63ymCApGtGri03Gqcmz5fmBNQYev6mHYXEy7xopMzAykzerNt+jP/9163i8PVr8mpBEfvM9/RFLnfhegaaR9cMZPKi6H+TRZPzT7IBY9NUgAPVwkPXL78ely+4PLyujPhGjGUtMQUlAOl4g1kM4di4JCylDXDDwBmpL8XxdyfciKE7PlH7nTgcvP5nwAsPAkxBa08CbQMptPYcfh1cZSZPtlFo/L2LyOpMZwRoYEF1zWBrEMD/PicVsperXv3cKp1t+bfsXThRSIO2kiY+EchMEvPemSBTqEFDcpqZHK4IBJFQTZ6PjngHLMfCcweew6g16gWZbGGYp/Tx26F4bRdEsLB7zgDw0DCc4Z0w1W7YzkEQZiBparABsBo0NVmXN5geRFusDYxuhu24iKvctpDO6ERRFUAbBzQWA90z8Xo8oGJ+cZxIRy5/w/WwDhxoiAJ8w/IbcMPyG/j5KSoAu0pdk5gmz2yPJzAjbEGiqqCBujYtHmaPZOJ57A7YMezgTu7yBa5NIQpAKWJqGeWiC+JYnjjhweIuxJQULCW6Drgyk5da8igGl6zHZteCIuiaQ+V9aDW6Pdpx8L7SJgJWu84hSQAAIABJREFUsr1PXSYDpVxdvYat7DWJF/NgcAzrnL8QC7fvjdzOB7/eWKa597FZHNNOHlEout4Xrv2SzQaXruc1JKsvqN0D7lhEPJXCdmcMKtVDL/jnbzoFo6XxJX41oUbYDF2TUArbtcCI4tVDUVUBTSTgyFCFrGGrkcnLve7K0GCQaOnAsIgS0oCTp/UEJvuQclJzr6rMKBKgIQcPiB78Uzq/p6lhXteZuWAO9n/7KbBstDNL43G4hQJcy/KMYGqXQ5RU27FgwYKZFFTfwOBMKKkarF4U9SyJIP1CTKQkyOkfZ3KoikhJA79eTR4bz8mT+xZqYW/7LYJmpFdLqchIuH8OQWpIo1L2ABDTdGiWjWwNJw+uG5A/D7ZQ4Iis8WpQZbFhNJDJs1MmsB2wRb+8eWv4+9BqtoYa6oYR8Yy8LEODjqp83gTYX9wfPu1MBuUdO+puHjcSGALgHolMXrobSPOIvRFX8ap3nzApu62VyWuWrnmsUESC9VM0xpuOA2FhC+AI1eRJRGXyIvA/5/0POuNNUKEj4Dl5k5DJk+8GbUB4pRZyr7sSpa1bkLvqqsM+n8kAFSJXtTJ5Z/adiQ898CH86LkfAfD7zBHRgzVljJ9tOG/WeXhwx4OejZBrSWP37W+FWxqG+b6vwHZ2QCEqKKOwARA9esxN62loVPPGQEYIbLiIa/wcDieT918b/gsDqYGmtqGxmHensiONN66uh6jskNrd7WkmNIPWZDuALVVzGCEELJ2GPTwcvaGEsD+IokANOHleOYWYXxZ1LMEDj/0ZAHCodADkuTvF9gHaL2WAZeHAN2+Get5K6A7xbLHhPQ8D8Tm+zViF8O/5bl6a5MD26JoF6xCAbphMZNuDc3kTrQWY7OFax64klMJFbVtZzinSybvlvFtC2zaCslOEmZk8mn4UjmknLwqaoeC6/zxzqk/jiEEzTJSdMTgIR0ljmoJYA4Wn+ry5IKbJaQGNgjHYbhmMqKDCsFNU3pfJEal3WZtFa0wGqXPPDf2dbu/GAYdTIGrSNYP9oRqQqg5tO8HJnhIa4p13ZVpgHwQyopjcXJCD+b7o3jyAHyFyhoe9ejDFtaCafvSq6BTQ3rsGhRIfqEJZVUK9yNGO0U0wRg5iywgfWOMBNUPPwGa04ahxlQpppapmlJNX4SxVLQ7W5EUtV3hvPsKEklSopyX17nfDAhgA5uc70XL3vdBaooU/XLjQhDFmgz+3oJMXpdY4nqhA02ggk0fEBOUQFzd+84f1nfTsALD0CuDEt1QvkzRb0mg20l9vx0jYoWPp9PgTlFweRe89RtAR64CpmE0Lr0xViuYn274IQgjehHWNbRAweGgsht5kLz5+6sdxeu/podWOSE2ehNaYk3dcS+NiGbUgRSYmQ+1a0jVZkK5ZIbwy7vkkk+g+yqJs9cAMHRgDaMDJC2a322JtWJZfhtueuw2AX1s0kNfw531Af7a+uBsAXDj3Qrx88OXY9Udu/KuaBndkNwBee2m5Y9DdhFcfT/Xoe7moZREsx/KcbEoB2EBSP3wn78TOE5veRjp5Jz+9DbHi4WURJZrtdVYPvZkBDGNLVSYP4Aqbzmh9xzScyVM9a0wybWSGjWoa5NJDo7uQFv2Tg4FmRhicAm+PpRx6CW6snY8xioLSnqdR2PYJjF4eVtyVqMzk5YXDa6GMmGhJJcXJTIXbv1SpZns1Aj+TV2f8H4euCfDAuOM6yJv5qgDaeHBRxqg1jGx64rXIjeAvzsn7SwehFGVnrLZYyThQcjnM/dXdoMkmmhVTCn20AEZUKKIgR5Efl+x1IwfkGnTNSiRbO2HZXIXSJeMLr7Bmzhf8PrVcfTUSZ9ZWzorCPZfd46mMAQAzSiht2QLXPtDQ9nLwsIeGgCS/Lhc2BpeeBIg+5kV7FO1zTsXmp/lxWq95M0Z+8xuxAwrCKG7Z9C/o33MQ7QeGUBStQuIBYQaPrZlIVtM1a51bTeM9TG0ML5I0wfHomtHHZrkslHwehPBMKKkIAlBQOHCayqgwTYdmO2DZTORyFy50weG33LCTRyip0SpikumaDWTy5ATlEHd8YSDKgAs/H7mo62P/gt2f+xy03upG2lFwhZNnui5euTDc+zC+bh1ovL6sfurcV2D4V79G6/XXNXS86YhL5l+CdT3rGn7vPIN4iqj/I6V9zSURgzQmESA7Z/CcuutNOhrM5E0GpFx8I32vxoNKVZiK6dfkgQSy5UdGXfVIQ4vFq528inHwZf0vw8d/z5suy95frpCqN5TG5nVDMbw5IUj9MxQD+8gYYnA8Z6RWJu+6ZeFxRQrgxFQdSTWJt654a0PnMlmQ9Vvp0fpNq5vCOA5J5rJLYSyq3yOyal8RtEKWzsDatbvu5jJTRVQVqqagKBw5pkkWD7zllPD5VLH9PsfBuT84njr7toAKNV+qaYjbLuw9T6El9obI8wjaH65jIdPGmTpP2/djmcbHroJw8mIKH1sS8YDAVBOOcyN0TZnJq/esXHAnL8qmYC0tyF5+ecRWHNsO3Id9LsXlibc1fN4TwYyTdwzCYW7N7FcjaFbFjTAGYpegKcwz+uUA4IkwyKxQgxm3WKoVtiP7cdXIEgWjNOM0CY5C29tvanqbSmUvojko3P0hTzJ7PMgJwRkaApIiAkZcsMCE55YBZqRAKHccYyecgOyVr8X+r32dT4CM4dyHnwMADBkmiFsCoIRUN5WuLuTffhPS556LPV/4ojzbuudWK0PjjU9Rj6FOLRi/ODFh1xhgW97wBmQuugj4wgIAgNoeziBTQsHAGqpD8E5JUECDEtFhuDCoFBfhRoqsyavZc63hLFiDoArQdhxwch2DxMvkHV5GzFy6FH1f+ELT27360BDa8seHfstcuNEX5agBloij97Ofafp40wmGYmAwPdjw+u1mHM+PHEAuQvb9aKBZ4YdQPbNZ22lv5rtrGhE1eUcKHl1zkvrWprSUL94Uoa55rMFIpoB9AEPtzMVZ/Wd5Tp7M5JVEfWVl7W49eO2HApklUzGxLV2EXnSQlL1MjcbupZTjj+kK7rvivobPY7IgHYLJxHgOSecHPtD0vqLmd5pJjy/kwnwnj6kKAFFGU7E/oqqeiRHsgRj8JhSqeGZE8c8/gLXzPgCvAjEM6CXuIA6VarRQCDp55TFkWnkm74nUH9G+ZxY6E/NQEMrPcYXP/Uqgb3QzIlK+k1fnOTQovGK7dqSA17x7f1P3HCyngLFiAaxJllqzOLbVNf9KsVN/EU+M/O7oHZBSuFYJKhSP8qfIKI+cB1Gfrlm1y1gOjsNpBC6t4eQFDZUpEjzwBtAGnUwvkzc85NW4maoOJUClLcEAmBKiCHqUB0JD0SWVUKj2GDTLghqs3SMErVdfzTn8h5tdqFeTN24mT/xbw4Gkpgm1ou/P5e9bgw1v5BQtRlnTdVFqZxeUfL7m5Ou6LnTGn5crKEFSXbOWkxdFdTksEAJcex+w9NKaqwQzeUcT2UsvhdlaRHZufYGVGfgYSGSw/rFNyOeaoLlPIpjrgjXznQel2etlZo9kJk/jTt65N7wDZ1z15iN3HEy+k3fdsuvwN7kl/I9gAKjpGs7pgUQXb//DSG0aeVeiC4tbeDNnWZN37bJrQQltThhHZP2CTpyhGBhRirCJ47EWamXyKsHEPGlMgsruRCADtwDQev31E96P0tEBc+VKAOM4F03Csxei6vy6usKtFOpsTxQlVK/utSiTTbtVFSqVc1ZQRyCgrhlwdtSOVhDCHUZi6NDKPKh/sJaTF7AxXHvU66N7zRnvwuNbv4s/7b0LO8e24FBpL7IaH4fdlG8DNCOe1mgmj19U7Zo813Xhum6oFUaj6FEMDOw+CKI3n8BoBsfmiPVXjmKiiF17nj9qxyOMAXYJCjE9Z06XfG3pqIgPgsYajEowxXfyamUlJ5G3PmF49QON1fh5NXmHhiBTY5pqAgFp4idsA21FO8yuDNAew4MmQXKkiOzYwZCTF0ZjdM3aaMTJq1+T1wxVItcVR66L3ydKaNMDZPbyy5C56MKajr8Lx9unIgxcTWcgpE4m70gauzXAhMF4uJm8ZqHk8xg4azzlrxmEQaAHFHOnO0K1r3UixUHafmXd9GFDOHkLTzl9cvcbAXPZMmSvuBzmihWTsr8L514IjAnavp6CP8ZOgzlpAkjPGcD+326CWkPZUOKs/rPw2N7HvEzehoEN2DCwoaljyYAly/hzpqmYGGIjKNEytK441J4EWLqxOVXSNU1tau69dPJa3vxm5A+Doj737rtQ2rYNz71sQ4ha+dn1n60jtNUAJN0ywj7I33ADWsYR//EC2YoiMnnid8k+Cjh5UiDNpQQOAahb4eRRBlkx2f2pT8Ley+cZqhtQ93HmUmeuRnA2kMlz7DHvv5VcC7SxETx16EEAwL7idqQ0Xo8fagvVhA2idncDhIDVqOtvZH/BTN6EnDwthuzuA6DGke2TN+PkHYMwYvE69VVHAITCtUtgVPFeZlVETDMiCpEdKXEloiZolY6ka9ao55p0WfsJQE5YzWbynOFhzy5gjAG67+QdcinKT+2PlvJnLEQ7oARQRlvhWKNeRLMS5vIVOHDrd6DPnRO5fPUFF+PBHwaaxHavBF76k/fnwNIVuP+730L/kmXVGyfagI7jgfXvj75gj9I0sWc1ESePMAYSq2OsiEmp5BRhJISqHCXQTKW6jYS306P/rskJ82hn8mYwAdQTJ5qOCLZQqPOtsEQCc++7FzSRmHwRlqM4ftNYDB3vi24dM2EcdyFwcBuw+k3AM7/kvx0rLTQqoHW2ANgEjdV38i6edzFGrVEsammwHqwOgk6cSlXc2noHbk/fj1v6zkfs+sbFJiRd01Cn1smbDLaH2tEBMBYKip7ac2qdLcaHJ9wWQSVmyeT4egbSxtHUkFolqehnR1TVt9UIwVg2hti+QlULhaL4b2PRIi8QSwwDZIwH9V++NLp23AkE+1344jpKSw5mWf6tYm9xOwaSi8Wph9lNjSK2YgXm3vNrKK21nWsyjsBYUF2z0X6rIchSlwmUIjWDGSfvGESuuwcHd+88ascjjAJ2CYyoXuZGF5mthB6H6wKa66II3pOpUchMXt2OkVMMSatoNNoSNKh2H3gM7bklsHAQhuY7edQpY3QISOYiPm4SblzK4EK1gDKtfV/TF25EfM3qmvLL6664CuuuuMr/4Y13hpZ3z1+Im/7nx9GDJFOBa+pwy+Ug3sgE2LGkeveETWyArAOZGS7ZhVAwRI8pcOwaGckpaHLNpJNXg648g2mEY8y4JwFjbDwjQslNsrrbtfcDOx+vu0qtgNS0AmXAKTdO9VlMCliczz86rf8upPU0rl8+cUpiEDQerv8biY1hR3l300E9mckzJpHi2Ay8soBJqMckqgq1q6upxt3j7lPSLSfohLq2cKBUNdTOyVJEJltm8jQtUJ5DMNaa5E5ewGFlNVo6BZlQtMa1y0zeoT2PIm5t9veZy8Eo8XMkLIN9Jb/tT5VieBOo5+ABQNfHPoY9n/1szfUICOBiwpk8aec1yhKbKGacvGMQJ118BdZcdNnROyBjIpOngkq6pnR6KAVvetOcuiYHj/m4U5+wqw0Z5WqQNx2sE9t78AncsulfcHLPHKjCySs5ReRKL2GP0R9OHgVVKoOZPAC6a2G0TgSWENJcf50Ig3XCNY/BZuj18K7NgFJNG6OETqBXWX1I2mnRHg1NApqpoDRaQ357CqjBTp5f96PJJxEtKj2DaYO66kTTEJKCZZpHv565bSH/Xw0sePSRKaFH/zWDaAyOa4+byZvUY1KC3BvegNgq3uvSUAwUrMI4W1VDxisMbWpr8iarjs5YfBxgTbwNRBXktzRBh8ctc3EyoqpeWx8AKMtsWoCuKYNHBASlfBp4emcoQForYBsMNNUq7ZA1eYcO/hn5M/xMMjUMxKUWhHESRpVuuI4FQhXOkjpCiJ+4BvET19Rdx8XEa/LQpN7DRDHj5B2DoIyNL7k+iSCUZ/Io9TN5qu7T4FwbkBo+zfSzcwmna7psGvfbknLPjWbyIsRACKNQdA0P7fkldo5tw2xlPvagP9L4IoSEBkHXdREnLobq9XOZSlAS/rcWzGhVwiPh5ElDvOiMontwtverHlNg1Sj6nopMjdKTwhVdb0X/rEWI6H43g+kEydY8RnoDelHierTmKQJRp+lYVhfSuT+2MroShBBYzhg0NvlKkZVIv3wA1j4+t7f/n3d6v5uKOSHWxpTTNaVw0SQpq3Z99KOTsh8PMrs2USdUOnlKOJNXdsM9AYmqetOkAoreOctRvvfpKnXNyFMMtjap5eTJeXvhAPLXXhtaljfi6Nw/hH3pbrjUhHNwG1h2sCqTN3z7PwBOGfjo0VFhPZyaPMIooKqT2jMxCjNO3gzGh8jk0UAmj0q1SI8WJDN5jTt5Dt2BB3b+CDRfXwTCOO7wm+VOFJLvThvN5AWEZ4iIgLmUQVc0PDv0RwAUbeZ+PIkKiqBX8uOGo9yuizix4U5TJ28iwitBUEKbaoTeCORkQYpDyK86zfs9mTPq0DWnoCaPKtifLmNwOggMzaA+ppiuOXDrrWgqiygFo46wPPdfDTThHB1jtN0gLBSh4cg7ecnTeiN/NxQjROdrFLIW3fwLqMkDjgA9r1E2TQ24IqvIM3X+PkoOV8b05lNV9fojqyBoGZiPHQAqm6FHIWg/1bQVxGWoerVbYuRyWP7wI9jS8Wds1hbBPrQZLDtYlclzR3bVudLJhVTXnHhNHjviVE1gxsmbQQPwM3mKV0dEVL+5NP8P0QC1idRzRywL4/bbMPbq2qpuc379K7DE0eu3VAnSZCaPUAoSi8EtFEK/KZ7wiotMrAxTU0NOXjCrF8rwOQ5yGsGKOe0Tv4gjicM0ehhpvoXCeJB0TX3kELT+Pu/3dZfMg23XyMRMhbrmMarU99eIzEV/g4Pf+S7iJ544Jcc3j1/c3AYTCLrNoA4u+ybw8C1AbtZUn8mEYSnWlLKNTcWcUMaDEQJGSR116SMLLxs+TYNxUX0Jm9uBGCvisdA+ehJCIEW+M0yBqetAEUg4NpIbNqC8Yyee7MgBW8QqNRzNkP00Dl2zUvAFAJQsrxs+Pr8T/T/5CuyuFbBnndpwr8UjAamu6bjOxOiadPx66cnADDF+BuNDZPIAQKE87c683iyCo02ap2singIBQOv0NlLb2qaWctRkJg+I6EtFKTRvkFOhtuUx94R2ZNsbuC7XBSuX0JKdOke3LqRzNEHVwSNJ19R1GooaaqYCMxH9rk1FJo+I0OWEJogZHFXEVizHwiefgNYbnaWYbpDG2nSkax6TyPQBp73zmM7kuebUnruhGBMa6yglU5bFAwI91SaJrjnpOMxMXuqcs9Fy9dVoe/vbQ8HOxa3hwBIhfoN0AgKlpQVtN74tRBOVitGVaCST54h5m0Y8a9bCnTytvx8AYL30B7xhzvvBUkc+E1YLcv6eqJNHFLWppMhEMZPJm8G4kJk8AFAp/6i8D1sOChOJHCczfFN1chrYHgn4mbzGP0YWi8PGHmgia8RUFYqqQjHPAFV6kb/hHLQnk9GCCBW+kuu6cEslkKOQ1p8QDrNWiRFWc2KYKKjD6Sd6W3QdYPRGR9/RkjSYGSdvBpMOSddstG/pDP7iQdIG0LzuyaRhojV5jBAYEdmdowU/kzdNx2npeE1QIZqoKtrefhMAwNqzp3oFGcAlxEsLkUBtanD+YpQh+bKXQe3qDB8jaD/VcEZlJo9F0DWVHO9npw1wJ+/A4j7sUl+a0rlT2m8TrcnLXXklrHPOnuzTqsKMkzeD8RHI5EknT/Z4o1oJNgB77zOc092EM8KSPDpDlOnr5HnGUhMNK2Xkb/72vTBKFvrW94BRBYqxnO8ylareqFYfLteFUypx+eJpCJnBnSgN6Ehk8ohwOOMDneOsGTyRoz9ZOJKecoyKOcxg+kJmpkkTLW1m8JcNlo0D26fu+CabuPCKPkXtE4BgTd50zeTxf9xJ6OEZdY09//Hv2Pvlr0Bpb0cuqaM4ArBgf7rA/MUIQ8+nP1W1j6D9VEsgxgt6qtX2ABNtXmgiif5vfROZziQu2fQt9CSje+4dLbguV9ecyHvNKfhN0vAngGkampjBtAKhgFWRyVNlpLiE4Z+/E7FVnej94heakuvWZvG+aaRjcJJPePIgB71GWygA/qSgOC5m7z4ApmpQxqWb1LhvjgO3WAyrU00nHGaT6CNSkyf65OmzG6fWHXWZeQQK2o9hCtgMpimmsbrmDKYGSmZqKf8ZI4O42rzwC6OAqU2dg6Xk81DyeY8qON3gzR+TUW8ZEew0ly1Dz6c/BcKYp3RaKzBZs4VC0H6qEVCV2yYTmapliqBrEkYRW74cnR1z8I8n/eOki7Y1C6muOZ3n8JlM3gzGBWE0kMnzWyfwZQrcsYNQshnETzqpqf0ueMUr8TutFSecNTViBg3hMDJ5EkRRQBlD8tBm9G27E8CZ4+5j3u8exN4vfAF7v/Rlvs9pmsnza/ImRtckhBy5mry5A41vMgVRWhl5nRLKyfLXAgdfOPrHPcrIm3nsHt091adx1OG1UJgRXpmBgJmMw5lCvuY1S6/BZfOb7+875XTNeBxz7/n1lB1/fBxeoDW0p3GcFRYbRnnbA1CtOwG8HoA/fzHCam4fDFITJXq+l6ItZgT7gAnhlclqYzEZCAqvTL4NM3mYvmc2g+kDxuCWRwAAMSaohlJwRaTtXdtuereEEKzesHZyzvEIYUKZvEonT1UAQrDqDx8ff2MxULNkEkQLUBy0v+CavMmma4p/lVwTkespFF7R2BQ48Bd85ugfcwrwnfO/g50jO6f6NI4+ZloozKACsWQCw5i6gEfOyCFn5JrejlICbQrG52MGh8mmCWGc+0xiWYw99AloJwz4v4l5rB5lMSS8UuMYLak04ALxbHUmz1y+DOmNG2EuOb7u+QE+tfNII9hCYTrX1c84eTMYF4RSOIdeAgBktTbxmxhYhPokbGsqTu3IQ9a2HEYmD4yNr97oRcDciN8wjWvyDo8qcmbfmcjo1YP64WAkQWE4ADUbH96mgm6xpnMNXrfodbhq8VVH/dh/LZioYXmsw8vkVSr9zuCvFnrCxDC4wAWZxkZpJRZ3paesfcIxgSjbYaIQmTL74IvRy1Oizr1tYeDwwsmrk2UL2U81Mnk9PQYO3PYttLz2uqplLJFA10c/Uu/MAXAG1NGqnTxcdc2jhRknbwbjgzHAGoMzshtqPM9/k86P+KBcq/lM3rEArxl6E+qalXUwSjY7fqYoysmg09/JO1yqyLXLrp3Ec+FQMhlYQzaI0sTAOxV98ijDO1a946gfdwZ/BVBVZC6/DIlTT53qM5nBNAGN8folm9hQjiE5hg9uPPLiFMc0hJ0wUTZNEIQSDN32VsApA4ig1kaIvEgnr55KdtB+qhXwJpoNa9NdIMrbmj9xAZZMTnjbZkEI8WryZpy8GRzT8KRiD70I6jl5YqFQSnL/QjN5+tw5MBYvhj57dsPbyExe8uyzkTjtNCTWr0f5xRqRsUq4NTJ501V45TBr8o4EWuNtcFBubqMZOtAM/oJACEHn+98/1acxg2mE/8/evcfpXOf/H3+8Z4YZ5xxGYQjjbMwMTaTIOERbyqkY+jp1sIuyFCux/WzrULaNzmWzq4OuUVq0bVFCTm2FyDAY7FiDChWmIYz374/ruj7NZY7M6ZqZ5/12m5u53p/35/N5f663z3XN6/M+eXs2XDAXCSrGRdGlYBX4xCsXzlzWuZzumjm15GUc7pJNS5szI3AWs2v6I4MB627Ju5LZNYuK/rKRPLt48pD73wyzCRmnu2bpbMkrd801NFryLkGhoXnexxvkBYSEcFX/fhhjcu8OmMXmjPv478QrBfcUsaAYAwEVL++Lwp9nxxIRyS9vS541ivBKFWcZo8Ifk+dsz/B9n3HilWx383bXNCb7oSue42Q3MYs/8k684s9/P5Scd1OK3cVT7taoixlabbxrnpTW7ppXwhmTl/GJ1ZW0FGXoAuCvi6E7Aa0fBaEhzar7dHUVESnrAkLcf+7ZAmnyEb/htK4VRHfN3P5OyTw8w9uSl9MEas7fLzkFcN6GgxIW5KXbdL9uySs576YUu3RPS57Ph0lg6e6ueSW8gY/JOFg8j096bHbdNf0oiMqo9u9/T2C1alS9/fbiLoqjag//XM9IRKS4mEDDuaALBdLgI36kCGfX/PXh6ZUFeTkFkc5kfiUkyNPsmlLq2J+PY+15Ai/+2mpXuXNnAqtXp+aIEcVXMD/jzGiXsY96bh8CWX1Q+0y84r8teaFjM8+GJSIi/iW4cgXKnS3H+ZSvuXB4C9C5uIsk+ZXFZChXfKg8ThCX1cQrOXfXdI/Jy2nmy4BKlSAoKNPEdf4q4+yaasmTUsJizM/YDP9tgmrWpNnnm4qxTP4noGLmljxzBd0HjU9LXrn8F0xERMqsoErBpJ+3pH7xUnEXRQpKUa6Tl9+JV3II8qrecQfBLVsSWPky1rctRhkXQ/fnMXn+28Yofqli2/oE1SoZN2Fxccbk+bTkXcGHQIbWvwA/HZMnIiIlQ0CFoCv7LhK/5ax5WFCza+Zle4aJV/LWkufprplTS15wMBVat85jQYufM+u8xuRJaVL97qiCeWJUimU5Ju8KnpCVhDF5IiJSMgRUDMpyJmcpwbx/JxTIOnmXP/GKdzxajmPyQnJvySuJrLVYa/16TJ7/lkz8kgkwvsGLZJL1mLzcvllzGZOnlryioafcIlJKlQ+rQrk66olTmlx11wDKN2zIVXcNyP/Bch2T5/k3iwf9ObbkBefeklfSeLtrajF0kTImq5a8vA5o9k1SS15Rqv+3v1G+oWbmFJHSqcrNYVS5OYzjc4q7JFJQytWpQ/iKjwrmYHmeeCVDd808jcnzPKQuRUEeBmd2TXXXFClDnNmhCnBMnoK8wle5c6fiLoJcWmTbAAAgAElEQVSIiEixyG0CkayGlTjdNU0O3TWDgiAoqNS15AFaQkGkrDEBAYSOH0+ljEFDXhdDz2adPH9abFxERETKGO/fMVkshp5TSx64u2yWtiDPO7umgjyRMqbW737r8zq3J2TV4waRun49V8UNyrjTr79qTJ6IiIgUmywmefEk5dZl0YSElKrumsZoTJ6IeOUS5AWFhtLoncW+id6JVwIC3N0dRERE8unqx/9Ihaio4i6GlDTO3zGZZ9csiy15WC2GLiKQ9+6aGXhb/9SKJyIiBaXGkCHFXQQpiZxJwDN318xpTB6UvpY8oEQshq4gT6QoXEGQ5514RZOuiIiISHFyZgm/mMWYvNy6awYH52EdvpLFG+T5c0tevt5xY0wNY8wnxpgkz7/Vs8k33JMnyRgzPEP6WmPMHmPMNs9P7fyURwpPw/eWFNw0vWXQFT3n8Twd0qQrIiIiUqxM5vV8va1YeemuWZpa8rzX7e9j8vJbskeBT621TYFPPa99GGNqAP8P6AC0B/7fJcHgPdbaaM/P9/ksjxSSCq1bU75hw+IuRsl1JU+wPGPy1JInIiIixSuLIC+P3TUDqlQhICSk0EpW1AwGay3WWr9uyctvd80+QKzn99eBtcDkS/L0Aj6x1v4AYIz5BLgVcOXz3CIlh8bkiYiISAlVvn4YAJVjY520vLbkXT3lUeyFC4VWtqKWcXbN0jwm72pr7VEAa+3RbLpb1gMOZXid4knz+ocxJh14D5hhM47ozMAYMwoYBdCgQYN8FlukiHk/BMqVu4x9NCZPREREil+5evVo9p/PCahWzUlzZtfMpTUruHHjQi1bUfO2YFpKeEueMWYVcE0Wm6bm8RxZhbjeQO4ea+1hY0wV3EHeUOCNrA5irZ0PzAeIiYnJMhAU8VfGGEInTKBybJfL2cn9T7CCPBERESlegVdd5fPa6a4ZUHbncfTnMXm51oq1tkd224wx3xlj6nha8eoAWY2pS+HXLp0AYbi7dWKtPez597Qx5m3cY/ayDPJESrpavx11eTt4xuQFlFOQJyIiIv7F6a7px61ZhcFkaL/y5yAvvyV7H/DOljkcWJ5FnpVAT2NMdc+EKz2BlcaYIGNMLQBjTDmgN5CQz/KIlBoakyciIiL+qsy25GXoo1iag7wngVuMMUnALZ7XGGNijDGvAXgmXPkz8JXn5wlPWjDuYO8bYBtwGPhbPssjUnoYza4pIiIi/slZJy+XiVdKm4wtef7cipmv0NtaewLonkX6ZuD+DK//Dvz9kjw/A9fl5/wipZp34hW15ImIiEghC3vpRcrVqZPn/N5WrNyWUChtSkp3zbJVKyIlidOSdxkzcoqIiIhcgSrdul3eDp5Yp8y15JmSEeT5b8lEyjjjnXhFLXkiIiLiZ5zumn7cZbEwlJSWPP8tmUhZ523J0+yaIiIi4mecdfLKWEteRv4c4Kq7poi/0pg8Ac6fP09KSgpnz54t7qKI+L2QkBDCwsIoV07d3EUKmzO7Zlkbk1dCumuWrVoRKUk0u6YAKSkpVKlShYYNG/p8sYiIL2stJ06cICUlhUaNGhV3cUTKjLLckufPQZ7/lkykrAvwrpOnIK8sO3v2LDVr1lSAJ5ILYww1a9ZUq7dIEXG6a/pxl8XCUFKWUFCQJ+KnvH/UB6glr8xTgCeSN7pXRIpOWV0MPePnjD9/5ijIE/FXTndNjckTERER/+INcPy5NaswqCVPRPLHO/GKWvKkmM2cOZPWrVsTGRlJdHQ0X3zxBQDnzp1j/PjxhIeH07RpU/r06UNKSoqzX2BgINHR0URERHDHHXfw008/Odt27txJt27daNasGU2bNuXPf/4z1loAvvvuO3r37k1UVBStWrXitttuy7Jc3uN7f5KTk1m4cCEPPvigT77Y2Fg2b94MQMOGDRkwYICzbcmSJYwYMQKAhQsXEhoaStu2bWnatCm9evVi06ZNWZ57+vTpGGPYt2+fkzZ37lyMMc65AL7++muMMaxcudJnf2MMjzzyiPP66aefZvr06T55oqKiGDx4cKZzP/PMM7Ro0YI2bdoQFRXFww8/zPnz553ra9OmjfOejBs3DoARI0ZQsWJFTp8+7Rzn97//PcYYjh8/nuX7+eSTTzrvX0xMjLPf5s2biY2NZeXKlU7eypUr07x5c6Kjoxk2bJhPeZOTk4mIiMh0HSNGjGDJkiWZ0vfu3cttt91GkyZNaNmyJQMHDuS7777LlE9EipcT5GlMnl/y35KJlHWeB0WaXVOK0+eff84HH3zA1q1b+eabb1i1ahX169cH4LHHHuP06dPs3buXpKQk+vbtS//+/Z1grUKFCmzbto2EhARq1KjBiy++CMCZM2e48847efTRR9m7dy/bt29n06ZNvPTSSwA8/vjj3HLLLWzfvp1du3Y5wcalvMf3/jRs2DBP17R582Z27tyZ5bZBgwbx9ddfk5SUxKOPPkr//v1JTEzMMm+bNm2Ij493Xi9ZsoRWrVr55HG5XHTq1AmXy+WTHhwczD//+U8nwLpUYmIiFy9eZN26dfz8889O+iuvvMLHH3/Mf/7zH3bs2MFXX31F7dq1OXPmjJNnzZo1znvy3HPPOelNmjRh+fLlAFy8eJE1a9ZQr149Z/ul7+ejjz7qbPv+++/56KOPfMrYq1cvJ29MTAyLFi1i27ZtvPHGG1leU16cPXuW22+/ndGjR7Nv3z4SExMZPXo0x44du+JjikjhKLOza2qdPBHJDxPgbcnTVOBSfI4ePUqtWrUI9jxsqFWrFnXr1iUtLY1//OMfzJ07l8BA91PckSNHEhwczOrVqzMdp2PHjhw+fBiAt99+m5tuuomePXsCULFiRV544QUnmDt69ChhYWHOvpGRkQV6TRMnTmTWrFm55uvatSujRo1i/vz5WW7v27evEzQdOHCAatWqERoa6my31rJkyRIWLlzIxx9/7DMhSFBQEKNGjWLu3LlZHvvtt99m6NCh9OzZk/fff99JnzlzJi+//DJXXXUVAOXLl+fRRx+latWquV7P4MGDWbx4MQBr167lpptuIigob3+cTZo0iRkzZuQpb368/fbbdOzYkTvuuMNJ69q1a5YtgSJSvJzF0MtYS56WUBCR/PFOvKKWPPH40792suvIqQI9Zqu6Vfl/d7TOdnvPnj154oknaNasGT169GDQoEF06dKFffv20aBBg0zBRUxMDDt37qR79+5OWnp6Op9++in33Xcf4O6qed111/nsFx4eTmpqKqdOnWLs2LEMGjSIF154gR49ejBy5Ejq1q2bqWxnzpwhOjoagEaNGrF06dI8XfPAgQN56aWXfLpaZqddu3a8+uqrWW6rWrUq9evXJyEhgeXLlzNo0CD+8Y9/ONs3btxIo0aNCA8PJzY2lg8//JD+/fs728eOHUtkZCR/+MMfMh178eLFfPLJJ+zZs4cXXniBwYMHc/r0aVJTU3NdHqBr165O4D18+HAmTJgAQNOmTVm+fDk//vgjLpeL//u///Npncv4fgJMmTKFQYMGAe4gfenSpaxZs4YqVark9rZdsYSEhEz/N0TEP9WrXI/fNPoN7Wq3K+6iFBuNyRORy6cxeeIHKleuzJYtW5g/fz6hoaEMGjSIhQsXYq3NclaxjOneoKFmzZr88MMP3HLLLZnyXMoYQ69evThw4AAPPPAAu3fvpm3btll218vYvdAb4OV0XK/AwEAmTZrE7Nmzc71+b9fT7MTFxREfH8+yZcvo16+fzzaXy0VcXJyT79Ium1WrVmXYsGE+XSoBvvrqK0JDQ7n22mvp3r07W7du5ccff8z0vnnHxDVs2NBn7GDG7preAM+rf//+xMfH88UXX9C5c2efbZd21/QGeF7Tpk0rktY8ESkZygWWY87NcwirEpZ75lIkY3dNf55dUy15Iv5Ks2vKJXJqcStMgYGBxMbGEhsbS5s2bXj99de5++67OXjwIKdPn/Zp2dm6davT1c4bNJw8eZLevXvz4osvMm7cOFq3bs26det8znHgwAEqV67sHKtGjRoMGTKEIUOG0Lt3b9atW+czYUp2atasyY8//uiT9sMPP1CrVi2ftKFDhzJ79mxat875Pf36669p2bJlttvvuOMOJk2aRExMjE+rZnp6Ou+99x7vv/8+M2fOdBbqvvT9Gj9+PO3atWPkyJFOmsvlYvfu3c4Yw1OnTvHee+9x//33U6lSJf773//SqFEjevXqRa9evejduzfnzp3L9b0Bd7DZrl07hg8fTkDA5T3n7datG3/84x/5z3/+c1n7XY7WrVvz2WefFdrxRUTyy+ehoVryRORyBTduRHDz5pRvnHPXLJHCtGfPHpKSkpzX27Zt49prr6VSpUoMHz6chx9+mPT0dADeeOMN0tLS6Natm88xqlWrxnPPPcfTTz/N+fPnueeee9iwYQOrVq0C3C1+48aNc7otrl69mrS0NABOnz7N/v37adCgQZ7Ke/3117Nx40a+/fZbwD3Jyi+//OJMFuNVrlw5JkyYwLx587I91meffcb8+fN54IEHss1ToUIFnnrqKaZOneqTvmrVKqKiojh06BDJyckcPHiQAQMGsGzZMp98NWrUYODAgSxYsABwT4jy7rvv8s0335CcnExycjLLly93WgGnTJnC6NGjnZlKrbWXtfh3gwYNmDlzJmPGjMnzPhlNnTqVOXPmXNG+eTFkyBA2bdrEv//9bydtxYoV7Nixo9DOKSJypTQmT0QuW7m6dWm8fFnuGUUKUWpqKg899BA//fQTQUFBNGnSxJmIZPbs2UycOJFmzZoREBBAixYtWLp0aZbdV9q2bUtUVBTx8fEMHTqU5cuX89BDDzF27FjS09MZOnSos/TBli1bePDBBwkKCuLixYvcf//9XH/99Xkq79VXX82zzz7LbbfdxsWLF6lcuTIulyvLVqv77rsvU/fDxYsXs2HDBtLS0mjUqBHvvfdeji15gNMlMyOXy5Wp++aAAQN4+eWXGTp0qE/6I488wgsvvADAunXrqFevns+slzfffDO7du3i6NGjjB49mrS0NDp06EBwcDCVK1fmpptuom3btk7+jGPyIiMjM812+dvf/jbL67h0TN6tt96aaWbT2267zWdymbzas2ePz2Q63glnfvvb3zJ+/HgA6tev78zmOn78eMaPH0+5cuWIjIzk2WefvexziogUhpKyTp7JbbyBP4qJibEZ1yESESmtEhMTcw0yRORXumdEpDAtSlzEk1+6H4C9esur3Fj3xmIrizFmi7U2Jqtt/tvGKCIiIiIi4qf8uSVPQZ6IiIiIiEgeaDF0ERERERGRUqSkLIbuvyUTERERERHxIyVl4hUFeSIiIiIiIpdJLXkiIiIiIiIlnMbkiYhIqRAYGEh0dDQRERHcfffdzkLlgLMu3u7du520tWvX0rt3b59jjBgxgiVLlgAQGxvLpcvgpKWlcc8999CmTRsiIiLo1KkTqampAKSkpNCnTx+aNm1KeHg4v//97zl37pxzLmMM//rXv5xj9e7dm7Vr12Z5LdOnT6dFixZERESwdOnSHK/76aefdvJGRUU5682dO3eO8ePHEx4eTtOmTenTpw8pKSlZHiPjtTZs2JABAwY425YsWcKIESOc1x999BExMTG0bNmSFi1aMHHixBzLJyIiRU9j8kREpFSoUKEC27ZtIyEhgfLly/PKK68421wuF506dSI+Pj5f53j22We5+uqr2bFjBwkJCSxYsIBy5cphraV///707duXpKQk9u7dS2pqKlOnTnX2DQsLY+bMmbme49ChQyxatIgdO3awbdu2HBdYf+WVV/jkk0/48ssvSUhIYN26dXjXlX3sscc4ffo0e/fuJSkpib59+9K/f3/ysu7s5s2b2blzZ6b0hIQEHnzwQd566y0SExNJSEigcePGuR5PRESKj8bkiYhIqdC5c2f27dsHQGpqKhs3bmTBggX5DvKOHj1KvXr1nNfNmzcnODiY1atXExISwsiRIwF3q+LcuXP5+9//7rQoRkVFUa1aNT755JMczxEUFMSpU6dITU0lKCiIsLCwbPPOmjWLl156iapVqwJQrVo1hg8fTlpaGv/4xz+YO3cugYHuL/eRI0c6Zc3NxIkTmTVrVqb0OXPmMHXqVFq0aOGUdcyYMbkeT0REilbGlryMv/uboOIugIiI5NFHj8K3Owr2mNe0gd88maesFy5c4KOPPuLWW28FYNmyZdx66600a9aMGjVqsHXrVtq1a3dFxbj33nvp2bMnS5YsoXv37gwfPpymTZuyc+dOrrvuOp+8VatWpUGDBk6wCTBt2jSmTZvGLbfcku05goODufrqq+nfvz8rVqwgODg4y3ynT5/m9OnThIeHZ9q2b98+GjRo4AR/XjExMezcuZPu3bvneJ0DBw7kpZde8ik7uFvyHnnkkRz3FRGR4qfZNUVEpFQ4c+YM0dHRxMTE0KBBA+677z7A3VUzLi4OgLi4OFwuF5D9k82cnnhGR0dz4MABJk2axA8//MD1119PYmIi1tos97s0vXPnzgCsX78+23Pcd999zJ07l27dujFkyBAuXrzInDlzePHFF3M8dl625bRPRoGBgUyaNInZs2fnmldERPybP4/JU0ueiEhJkccWt4LmHZOX0YkTJ1i9ejUJCQkYY0hPT8cYw5w5c6hZsyY//vijT/4ffviBWrVq5XieypUr079/f/r3709AQAAffvghUVFRvPfeez75Tp06xaFDhwgPD+fEiRNO+tSpU5k5cyZBQVl/ta1atcppKXzooYcYM2YMe/bscSZU8apatSqVKlXiwIEDmcbFNWnShIMHD3L69GmqVKnipG/dupU77rgjx+vzGjp0KLNnz6Z169ZOWuvWrdmyZQtRUVF5OoaIiBQPteSJiEiptWTJEoYNG8bBgwdJTk7m0KFDNGrUiA0bNtC0aVOOHDlCYmIiAAcPHmT79u1ER0dne7yNGzc6geG5c+fYtWsX1157Ld27dyctLc0JxNLT03nkkUcYMWIEFStW9DlGz549+fHHH9m+fXuW54iMjOStt94C3GPgVq1aRXBwMPXr18+Ud8qUKYwdO5ZTp04B7sBy/vz5VKpUieHDh/Pwww+Tnp4OwBtvvEFaWhrdunXL03tXrlw5JkyYwLx585y0SZMmMWvWLPbu3QvAxYsXeeaZZ/J0PBERKTolZUyegjwREblsLpeLfv36+aQNGDCAt99+m+DgYN566y1GjhxJdHQ0d911F6+99hrVqlVz8t5+++2EhYURFhbG3Xffzf79++nSpQtt2rShbdu2xMTEMGDAAIwxLF26lHfffZemTZvSrFkzQkJCspy8BNytedktZ/DGG2/w5ptvEhkZSZcuXZg4cSLp6elZBlOjR4+ma9euXH/99URERNClSxcnqJw9ezYhISE0a9aMpk2b8u677zpLSQDcdtttHDlyJMf377777uPChQvO68jISObNm8fgwYNp2bIlERERHD16FID333+fxx9/PMfjiYhI0SgpLXkmL1M++5uYmBh76RpLIiKlUWJiIi1btizuYoiUGLpnRKQwLU1ayuOb3A/ePrnrE66pdE2xlcUYs8VaG5PVNrXkiYiIiIiI5IEWQxcRERERESmlFOSJiIiIiIiUcCVlTJ6CPBERERERkTxQd00REREREZFSJGNLnoI8ERERERGRUkTdNUVEpMQ5ceIE0dHRREdHc80111CvXj3ndcaFyJOSkujduzfh4eFcd911dO3alXXr1gGwcOFCQkNDnf2io6PZtWsXycnJVKhQgejoaFq1asWwYcM4f/58luXI7fgPPvhgpn1OnjzJsGHDCA8PJzw8nGHDhnHy5EkAn3NHRUVx4403smfPHp/9f//731OvXj0uXrzopGV3roxiY2Np0KABGZcn6tu3L5UrV/bJN3fuXEJCQpwyAaxduxZjDP/617+ctN69e7N27Vrn9bFjxyhXrhyvvvqqz/FSU1MZPXo04eHhtG3bluuuu46//e1vma7X++NdXL5hw4Z07tzZ51jR0dFEREQ4ZapWrZrPvqtWrQLcXZYeeeQRZ7+nn36a6dOnM3PmTCdvYGCg8/tzzz3nc57s3s+GDRty/PjxTOkfffQRMTExtGzZkhYtWjBx4sRMeURECpsWQxcRkRKtZs2abNu2jW3btvG73/2OCRMmOK8DAtxfH2fPnuX2229n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RIqSZtcUEZESzeVyERcXB0BcXBwulytTng0bNjh5IiIiiIyMBOCrr74iNjaW0NBQgoKCuOeee1i3bl3RFV5ERKQQqCVPREQKRG4tboXhxIkTrF69moSEBIwxpKenY4xhzpw5PvmstVnun126iIhISaQxeSIiUuItWbKEYcOGcfDgQZKTkzl06BCNGjViw4YNPvk6derEO++8A8CuXbvYsWMHAB06dOCzzz7j+PHjpKen43K56NKlS5Ffh4iISEHQEgoiIlLiuVwu+vXr55M2YMAA3n77bZ+0MWPGcOzYMSIjI3nqqaeIjIykWrVq1KlTh9mzZ9O1a1eioqJo164dffr0yXSe5557jrCwMFJSUoiMjOT+++8v1OsSERG5EiWlJc+UxK40MTEx1jtrm4hIaZaYmEjLli2Luxi5Sk9P5/z584SEhLB//366d+/O3r17KV++fHEXTcqYknLPiEjJ9PX3XzPso2H0btyb2Z1nF2tZjDFbrLUxWW3TmDwREcm3tLQ0unbtyvnz57HW8vLLLyvAExGRUqektOQpyBMRkXyrUqUK6mEhIiJlhb8Hef5dOhERERERET/j70soKMgTERERERHJA82uKSIiIiIiUoqUlDF5/l06ERERERERP6EgT0RESo2lS5dijGH37t1OWnJyMhEREQVy/HvuuYfmzZsTERHBvffey/nz5wvkuCIiIgXJ211TY/JERKTEc7lcdOrUifj4+EI5/j333MPu3bvZsWMHZ86c4bXXXiuU84iIiBQEb7DnrxTkiYhIjlJTU9m4cSMLFizINshLS0tj4MCBREZGMmjQIDp06OAsqeByuWjTpg0RERFMnjw5y/1vu+02jDEYY2jfvj0pKSmFdj0iIiJXyttd099b8rROnohICbFm4Xy+P3igQI9Z+9rGdB0xKsc8y5Yt49Zbb6VZs2bUqFGDrVu30q5dO588L730EtWrV+ebb74hISGB6OhoAI4cOcLkyZPZsmUL1atXp2fPnixbtoy+fftmea7z58/z5ptv8uyzzxbMBYqIiBQkTwOexuSJiEiJ5nK5iIuLAyAuLg6Xy5Upz4YNG5w8ERERREZGAvDVV18RGxtLaGgoQUFB3HPPPaxbty7bc40ZM4abb76Zzp07F8KViIiI5E9JmXhFLXkiIiVEbi1uheHEiROsXr2ahIQEjDGkp6djjGHOnDk++ay1We6fXXpW/vSnP3Hs2DFeffXVfJVZRESksJSUIM+/SyciIsVqyZIlDBs2jIMHD5KcnMyhQ4do1KgRGzZs8MnXqVMn3nnnHQB27drFjh07AOjQoQOfffYZx48fJz09HZfLRZcuXTKd57XXXmPlypW4XC4CAvTVJCIi/kmza4qISInncrno16+fT9qAAQN4++23fdLGjBnDsWPHiIyM5KmnniIyMpJq1apRp04dZs+eTdeuXYmKiqJdu3b06dMn03l+97vf8d1339GxY0eio6N54oknCvW6RERErkRJaclTd00REcnW2rVrM6WNGzfO+T0hIQGAkJAQ3nrrLUJCQti/fz/du3fn2muvBWDIkCEMGTIkx/NcuHCh4AotIiJSyBTkiYhIqZeWlkbXrl05f/481lpefvllypcvX9zFEhERKRQK8kREpNSrUqWKsy6eiIhIaaUxeSIiIiIiIqVISRmT59+lExERERER8RMK8kREREREREoRb3dNBXkiIiIiIiKliII8EREp0WbOnEnr1q2JjIwkOjqaL774Amsto0aNolWrVrRp04bPP//cZ5+GDRvSpk0boqKi6NmzJ99++y0AsbGxNG/enOjoaKKjo/n+++8B+OWXXxg0aBBNmjShQ4cOJCcnO8eaPXs2TZo0oXnz5qxcubLIrltERORS3u6a/j7ximbXFBGRbH3++ed88MEHbN26leDgYI4fP865c+fYsGEDSUlJ7Ny5kzNnznD69OlM+65Zs4ZatWrx2GOPMWvWLJ577jkAFi1aRExMjE/eBQsWUL16dfbt20d8fDyTJ09m8eLF7Nq1i/j4eHbu3MmRI0fo0aMHe/fuJTDQv79cRUSklHLHeGrJExGRkuvo0aPUqlWL4OBgAGrVqkXdunUpX7483333HefPn6dixYpcffXV2R7j5ptvZt++fTmeZ/ny5QwfPhyAu+66i08//RRrLcuXLycuLo7g4GAaNWpEkyZN+PLLLwvuAkVERC5DSZl4RS15IiIlxE//2s+5Iz8X6DHL163EVXeEZ7u9Z8+ePPHEEzRr1owePXowaNAgunTpwtVXX82pU6cYMWIEixYtcgaiZ+WDDz6gTZs2zuuRI0cSGBjIgAEDmDZtGsYYDh8+TP369QEICgqiWrVqnDhxgsOHD3PDDTc4+4aFhXH48OECuHIREZHLV1KCPP8unYiI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\n",
      "text/plain": [
       "<Figure size 1080x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot daily returns\n",
    "# YOUR CODE HERE\n",
    "combined_daily_returns_df.plot(figsize=(15,6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21a03ac1688>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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HcG57a02zm10UPDnlpcvMBHn38wR4DGgt7V2e3FrO58rSNcH52dzGPgZeBLwcgXqnsB5ttcxnAHFT4vp8npgBc7g2Bqch5qvLu28RERErnTmlyxxERERERERERH5rVImkYiIiIiIiIiIKEgkIiIiIiIiIiIKEomIiIiIiIiICAoSiYiIiIiIiIgIChKJiIiIiIiIiAjgc7knUJhatWrZ4ODgyz0NEREREREREZFfjXXr1h2x1gYVdO+KDRIFBwcTGxt7uachIiIiIiIiIvKrYYzZXdg9bTcTEREREREREREFiUREREREREREREEiERERERERERHhCj6TqCBZWVmkpKSQmZl5uaciclXw9/enXr16+Pr6Xu6piIiIiIiIyBXuqgoSpaSkULlyZYKDgzHGXO7piFzRrLUcPXqUlJQUGjVqdLmnIyIiIiIiIle4q2q7WWZmJjVr1lSASKQEjDHUrFlTmXciIiIiIiJSIldVkAhQgEikFPT3IiIiIiIiIiV11QWJLrdJkybRsmVLwsPDiYyM5Pvvvwfg7NmzjB49mpCQEEJDQ+nVqxcpKSnudt7e3kRGRhIWFsZdd93FiRMn3Pe2bNnCrbfeStOmTQkNDeUf//gH1loADh48SM+ePYmIiKBFixbccccdBc4rt//cn+TkZGbPns2jjz7qUa9z587ExsYCEBwcTL9+/dz3Fi5cyLBhwwCYPXs2QUFBtG7dmtDQULp3787atWsLHHvChAkYY9i5c6e7bNq0aRhj3GMBbNiwAWMMy5Yt82hvjOHJJ590X7/00ktMmDDBo05ERASDBg3KN/bLL79Ms2bNaNWqFREREYwZM4asrCz3+lq1auV+Jo8//jgAw4YNo2LFiqSmprr7+fOf/4wxhiNHjhT4PF944QX384uKinK3i42NpXPnzixbtsxdNzAwkOuvv57IyEiGDBniMd/k5GTCwsLyrWPYsGEsXLgwX/mOHTu44447aNKkCc2bN6d///4cPHgwXz0RERERERGRi6UgUSl8++23fPrpp6xfv55NmzaxfPly6tevD8Czzz5LamoqO3bsIDExkd69e9O3b193sCcgIIC4uDji4+OpUaMGb7zxBgAZGRncfffdPPPMM+zYsYONGzeydu1aZsyYAcDzzz/P7bffzsaNG9m6das7WHG+3P5zf4KDg0u0ptjYWLZs2VLgvQED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iuzsbO677z73q+vXrVvHo48+io+PDzk5OTzwwAO0bdu2RPO95pprmD59OnfccQc5OTkEBgbicDgKzJoZMWJEvu1T8+fPZ/Xq1aSnp9OoUSM++uijIjOJAPeWsrwcDke+7Wf9+vXjzTff5L777vMof/LJJ3n99dcBWLVqFXXr1vV469gtt9zC1q1b2b9/P4888gjp6em0a9cOPz8/AgMDufnmm2ndurW7ft4zicLDw/O9bezhhx8ucB3nn0nUo0ePfG+Wu+OOOzwO5y6p7du3exxGnntg98MPP8zo0aMBqF+/vvtteqNHj2b06NH4+voSHh7O9OnTSz2miIiIiIiISHFMcefMlLgjY4KBT621+V69ZIz5LzDFWrvadf0/4C/W2nWF9RcVFWVjY2M9yhISEooNUoiIJ/3diIiIiIiISC5jzDprbVRB98pku1kJpAB59zjVA/ZdorFFRERERERERKQYlypItAQY4nrL2e+Ak9ba/cU1EhERERERERGRS6NMziQyxjiAzkAtY0wK8H+AL4C19i3gM+AOYCeQDgwvuCcREREREREREbkcyiRIZK0dVMx9C4wqi7FEREREREREROQXSRsOcWzfadre2eii+rlUbzcTEREREREREZFysHRmPAARXetTwf/CQz2X6kwiEREREREREREpR/8evYp9iccvuL2CRKXk7e1NZGQkYWFh/OEPfyA9Pd19LyYmBmMM27Ztc5etXLmSnj17evQxbNgwFi5cCEDnzp2JjY31uJ+ens69995Lq1atCAsLo0OHDqSlpQGQkpJCr169CA0NJSQkhD//+c+cPXvWPZYxhk8++cTdV8+ePVm5cmWBa5kwYQLNmjUjLCyMmJiYItf90ksvuetGREQwZ84cAM6ePcvo0aMJCQkhNDSUXr16kZKSUmAfedcaHBxMv3793PcWLlzIsGHD3Neff/45UVFRNG/enGbNmvHUU08VOT8RERERERGR36qAKhXcv+/acOSC+1GQqJQCAgKIi4sjPj6eChUq8NZbb7nvORwOOnToQHR09EWNMX36dK655ho2b95MfHw8s2bNwtfXF2stffv2pXfv3iQmJrJjxw7S0tIYP368u229evWYNGlSsWPs2bOHuXPnsnnzZuLi4mjbtm2hdd966y2+/PJLfvjhB+Lj41m1ahXOY6bg2WefJTU1lR07dpCYmEjv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uIM/xUk/eZZrG1ehWfvrSjVOYLX8mUR7tx8vso2CRKVw9OhRIiMjiYyM5Nprr6Vu3bru64oVK7rrJSYm0rNnT0JCQrjhhhvo0qULq1atAmD27NkEBQW520VGRrJ161aSk5MJCAggMjKSFi1aMGTIELKyCt43WFz/jz76aL42J0+eZMiQIYSEhBASEsKQIUM4efIkgMfYERER3HTTTWzfvt2j/Z///Gfq1q1LTk6Ou6ywsfLq3LkzDRo0wFrrLuvduzeBgYEe9aZNm4a/v797TgArV67EGMMnn3ziLuvZsycrV650Xx8+fBhfX19mzrcjINEAACAASURBVJzp0V9aWhqPPPIIISEhtG7dmhtuuIF///vf+dab+zNnzhwAgoOD6dixo0dfkZGRhIWFuedUtWpVj7bLly8HwBjDk08+6W730ksvMWHCBCZNmuSu6+3t7f791Vdf9RinsOcZHBzMkSNH8pV//vnnREVF0bx5c5o1a8ZTTz2Vr46IiIiIiIhcWeK+/BmAfYknSlQ/7fgZKlXzL/U4FatUwBg4nSdIdGDXySJaKEhUKjVr1iQuLo64uDj+9Kc/8cQTT7ivvbycjzIzM5M777yThx56iKSkJNatW8drr73Grl273P0MGDDA3S4uLo4WLVoAEBISQlxcHJs3byYlJYUPP/ww3xxK0n9BRowYQePGjUlKSiIpKYlGjRrxwAMPuO/njr1x40aGDh3K5MmT3fdycnKIiYmhfv367mBUaVSrVo01a9YAcOLECfbv35+vjsPhoG3btsTExHiU16tXj0mTJhXa94IFC/jd736Hw+HwKH/ggQeoXr06iYmJbNiwgaVLl3Ls2LF86839GTJkiPteamoqe/bsASAhISHfmB07dvRoe9tttwHg5+fHxx9/nC+gM378eHfdgIAA9++PP/54oesqTnx8PI8++igffPABCQkJxMfH07hx4wvuT0RERERERMrX2YxznD5xhtRjmQCkHs0sto21lrRjmQTW8Cv1eF7eXlSsUsEjk+jArlNFtyn1KFKkuXPn0r59e+6++253WVhYGMOGDStxH97e3tx4443s3bu3TPrfuXMn69at469//au77Pnnnyc2NpakpKR89U+dOkX16tXd11999RVhYWE88sgj+YIxJTFw4ECio6MB+Pjjj+nbt6/H/aSkJNLS0pg4cWK+/iMiIqha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+Pv788orrzBy5Eistezdu5eZM2cyZcqUIudSu3Ztpk+fztmzZ/Pde+utt/jyyy/54YcfiI+PZ9WqVVhrS7RGERERERERufIc23eamY+uZFfc4RK3OZOexe4tRwm94Rq8vC5uW1ijiCAefOUW/jCu7SXdYpaXgkQX4dSpU1SvXr1Ubdq3b8/evXs9yr755hsefPBB/vvf/xISEgLA/v37qVevnrtOq1atLmquBY17sZKSkkhLS2PixIkeQZ2L4XA4+Ne//kVKSop7vq1bt2bHjh1kZGRw8uRJKlasSGRkpDszaO3atdx0000ApKWlsWbNGmbNmuUOEgH06NGD6667jjlz5vDEE08wYcKEYj+7oKAgunbtynvvvZfv3uTJk5kxYwZVqjhPma9atSpDhw4tk2cgIiIiIiIil973n+zCWvj8rc18G5NUoja74g6Tc85e9FazXBX8fS462HQxrtoziQ5MnsyZhG1l2qdf82Zc++yzRdbJyMggMjKSzMxM9u/fz4oVK9z3kpKSiIyMdF+/9tprdOzY0aP90qVL6d27t/v6zJkz9OrVi5UrV9KsWTN3+RNPPMGtt97KTTfdRLdu3Rg+fDjVqjlT17755huPcX7++ed827jOd/64uevINW7cOAYMGJCv3dixYwvMfAJnQGfQoEF07NiR7du3c+jQIWrXrl3kPIqa+549ezhw4AA33ngj/fv3Z/78+YwZMwYfHx8iIyP58ccfycjIoF27doSGhrJ27Vpq166NtZb69esDsGjRInr06EHTpk2pUaMG69evp02bNgC88sor3HjjjYSGhnLfffcVOc9czzzzDL///e+5//773WWpqamkpqa6A3oiIiIiIiJydTt1JMMjg2j9st206d4g3+HSubKzc8g5Z9m8ci/VrqlI7eCSv9XsSnbVBokul9xtWgDffvstQ4YMIT4+Hvhlu1lBunTpwsGDB6ldu7ZH0MXX15ebbrqJWbNmMX36dHf58OHD6d69O0uXLmXx4sXMnDmTjRs3AtCxY0c+/fRTd91hw4YVOt/Cxs27jqL885//5J577nFf5z2TKDo6mpiYGLy8vOjbty8LFixg1KhRRfZX1Nyjo6Pp378/AAMHDmTEiBGMGTMGgJtvvpm1a9eSkZFB+/btCQ0NZfLkyQQFBbmziMAZuMo9v2jgwIE4HA53kKhOnTrceuutxQbU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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot cumulative returns\n",
    "# YOUR CODE HERE\n",
    "cumulative_returns = (1 + combined_daily_returns_df).cumprod() - 1\n",
    "cumulative_returns.plot(figsize=(20,10), title=\"Cumulative Returns over the Last 5 Years\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Risk\n",
    "\n",
    "Determine the _risk_ of each portfolio:\n",
    "\n",
    "1. Create a box plot for each portfolio. \n",
    "2. Calculate the standard deviation for all portfolios\n",
    "4. Determine which portfolios are riskier than the S&P 500\n",
    "5. Calculate the Annualized Standard Deviation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Box plot to visually show risk\n",
    "# YOUR CODE HERE\n",
    "cumulative_return_boxplot = cumulative_returns.boxplot(grid=False, rot=50, fontsize=8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SOROS FUND MANAGEMENT LLC      0.007842\n",
       "PAULSON & CO.INC.              0.006977\n",
       "TIGER GLOBAL MANAGEMENT LLC    0.010824\n",
       "BERKSHIRE HATHAWAY INC         0.012831\n",
       "dtype: float64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Daily Standard Deviations\n",
    "# Calculate the standard deviation for each portfolio. Which portfolios are riskier than the S&P 500?\n",
    "# YOUR CODE HERE\n",
    "whale_daily_std = whale_returns_df.dropna().std()\n",
    "whale_daily_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Algo 1    0.007988\n",
       "Algo 2    0.008466\n",
       "dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "algo_daily_std = algo_returns_df.std() \n",
    "algo_daily_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "S&P500    0.008111\n",
       "dtype: float64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sp500_daily_std = sp500_daily_returns.std()\n",
    "sp500_daily_std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PAULSON & CO.INC.              0.007023\n",
       "Algo 1                         0.007620\n",
       "SOROS FUND MANAGEMENT LLC      0.007895\n",
       "Algo 2                         0.008342\n",
       "S&P500                         0.008554\n",
       "TIGER GLOBAL MANAGEMENT LLC    0.010894\n",
       "BERKSHIRE HATHAWAY INC         0.012919\n",
       "dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Determine which portfolios are riskier than the S&P 500\n",
    "# YOUR CODE HERE\n",
    "volatility = combined_daily_returns_df.std() \n",
    "volatility.sort_values(inplace=True)\n",
    "volatility"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PAULSON & CO.INC.              0.111488\n",
       "Algo 1                         0.120967\n",
       "SOROS FUND MANAGEMENT LLC      0.125335\n",
       "Algo 2                         0.132430\n",
       "S&P500                         0.135786\n",
       "TIGER GLOBAL MANAGEMENT LLC    0.172936\n",
       "BERKSHIRE HATHAWAY INC         0.205077\n",
       "dtype: float64"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the annualized standard deviation (252 trading days)\n",
    "# YOUR CODE HERE\n",
    "annualized_std_252d = volatility * np.sqrt(252)\n",
    "annualized_std_252d.sort_values(inplace=True)\n",
    "annualized_std_252d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Rolling Statistics\n",
    "\n",
    "Risk changes over time. Analyze the rolling statistics for Risk and Beta. \n",
    "\n",
    "1. Calculate and plot the rolling standard deviation for the S&PP 500 using a 21 day window\n",
    "2. Calculate the correlation between each stock to determine which portfolios may mimick the S&P 500\n",
    "2. Calculate and plot a 60 day Beta for Berkshire Hathaway Inc compared to the S&&P 500"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21a03a31488>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Calculate and plot the rolling standard deviation for the S&PP 500 using a 21 day window\n",
    "# YOUR CODE HERE\n",
    "sp500_df.rolling(window=21).std().plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SOROS FUND MANAGEMENT LLC</th>\n",
       "      <th>PAULSON &amp; CO.INC.</th>\n",
       "      <th>TIGER GLOBAL MANAGEMENT LLC</th>\n",
       "      <th>BERKSHIRE HATHAWAY INC</th>\n",
       "      <th>Algo 1</th>\n",
       "      <th>Algo 2</th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>SOROS FUND MANAGEMENT LLC</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.653129</td>\n",
       "      <td>0.327728</td>\n",
       "      <td>0.898896</td>\n",
       "      <td>0.470156</td>\n",
       "      <td>0.915163</td>\n",
       "      <td>0.875512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>PAULSON &amp; CO.INC.</td>\n",
       "      <td>-0.653129</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.193595</td>\n",
       "      <td>-0.780559</td>\n",
       "      <td>-0.830635</td>\n",
       "      <td>-0.767196</td>\n",
       "      <td>-0.853201</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>TIGER GLOBAL MANAGEMENT LLC</td>\n",
       "      <td>0.327728</td>\n",
       "      <td>-0.193595</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.031632</td>\n",
       "      <td>0.052669</td>\n",
       "      <td>0.177653</td>\n",
       "      <td>0.131595</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>BERKSHIRE HATHAWAY INC</td>\n",
       "      <td>0.898896</td>\n",
       "      <td>-0.780559</td>\n",
       "      <td>0.031632</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.579663</td>\n",
       "      <td>0.945500</td>\n",
       "      <td>0.938546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Algo 1</td>\n",
       "      <td>0.470156</td>\n",
       "      <td>-0.830635</td>\n",
       "      <td>0.052669</td>\n",
       "      <td>0.579663</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.588982</td>\n",
       "      <td>0.740215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Algo 2</td>\n",
       "      <td>0.915163</td>\n",
       "      <td>-0.767196</td>\n",
       "      <td>0.177653</td>\n",
       "      <td>0.945500</td>\n",
       "      <td>0.588982</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.965884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>S&amp;P500</td>\n",
       "      <td>0.875512</td>\n",
       "      <td>-0.853201</td>\n",
       "      <td>0.131595</td>\n",
       "      <td>0.938546</td>\n",
       "      <td>0.740215</td>\n",
       "      <td>0.965884</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             SOROS FUND MANAGEMENT LLC  PAULSON & CO.INC.   \\\n",
       "SOROS FUND MANAGEMENT LLC                     1.000000           -0.653129   \n",
       "PAULSON & CO.INC.                            -0.653129            1.000000   \n",
       "TIGER GLOBAL MANAGEMENT LLC                   0.327728           -0.193595   \n",
       "BERKSHIRE HATHAWAY INC                        0.898896           -0.780559   \n",
       "Algo 1                                        0.470156           -0.830635   \n",
       "Algo 2                                        0.915163           -0.767196   \n",
       "S&P500                                        0.875512           -0.853201   \n",
       "\n",
       "                             TIGER GLOBAL MANAGEMENT LLC  \\\n",
       "SOROS FUND MANAGEMENT LLC                       0.327728   \n",
       "PAULSON & CO.INC.                              -0.193595   \n",
       "TIGER GLOBAL MANAGEMENT LLC                     1.000000   \n",
       "BERKSHIRE HATHAWAY INC                          0.031632   \n",
       "Algo 1                                          0.052669   \n",
       "Algo 2                                          0.177653   \n",
       "S&P500                                          0.131595   \n",
       "\n",
       "                             BERKSHIRE HATHAWAY INC    Algo 1    Algo 2  \\\n",
       "SOROS FUND MANAGEMENT LLC                  0.898896  0.470156  0.915163   \n",
       "PAULSON & CO.INC.                         -0.780559 -0.830635 -0.767196   \n",
       "TIGER GLOBAL MANAGEMENT LLC                0.031632  0.052669  0.177653   \n",
       "BERKSHIRE HATHAWAY INC                     1.000000  0.579663  0.945500   \n",
       "Algo 1                                     0.579663  1.000000  0.588982   \n",
       "Algo 2                                     0.945500  0.588982  1.000000   \n",
       "S&P500                                     0.938546  0.740215  0.965884   \n",
       "\n",
       "                               S&P500  \n",
       "SOROS FUND MANAGEMENT LLC    0.875512  \n",
       "PAULSON & CO.INC.           -0.853201  \n",
       "TIGER GLOBAL MANAGEMENT LLC  0.131595  \n",
       "BERKSHIRE HATHAWAY INC       0.938546  \n",
       "Algo 1                       0.740215  \n",
       "Algo 2                       0.965884  \n",
       "S&P500                       1.000000  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Correlation\n",
    "# YOUR CODE HERE\n",
    "correlation = cumulative_returns.corr()\n",
    "correlation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.8217749991632826e-05"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate Beta for a single portfolio compared to the total market (S&P 500)\n",
    "# YOUR CODE HERE\n",
    "covariance = combined_daily_returns_df['Algo 1'].cov(combined_daily_returns_df['S&P500'])\n",
    "covariance\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.316632424648712e-05"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "variance = combined_daily_returns_df['S&P500'].var()\n",
    "variance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.24899091459425748"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Algo1_beta = covariance / variance\n",
    "Algo1_beta"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Challenge: Exponentially Weighted Average \n",
    "\n",
    "An alternative way to calculate a rollwing window is to take the exponentially weighted moving average. This is like a moving window average, but it assigns greater importance to more recent observations. Try calculating the `ewm` with a 21 day half-life."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21a03cd4688>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# (OPTIONAL) YOUR CODE HERE\n",
    "\n",
    "sp500_df.ewm(span=21).mean().plot(figsize=(15,8), title='Exponentially Moving Average for S&P 500 for last 7 years')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sharpe Ratios\n",
    "In reality, investment managers and thier institutional investors look at the ratio of return-to-risk, and not just returns alone. (After all, if you could invest in one of two portfolios, each offered the same 10% return, yet one offered lower risk, you'd take that one, right?)\n",
    "\n",
    "Calculate and plot the annualized Sharpe ratios for all portfolios to determine which portfolio has the best performance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SOROS FUND MANAGEMENT LLC</th>\n",
       "      <th>PAULSON &amp; CO.INC.</th>\n",
       "      <th>TIGER GLOBAL MANAGEMENT LLC</th>\n",
       "      <th>BERKSHIRE HATHAWAY INC</th>\n",
       "      <th>Algo 1</th>\n",
       "      <th>Algo 2</th>\n",
       "      <th>S&amp;P500</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2015-03-03</td>\n",
       "      <td>-99.039430</td>\n",
       "      <td>-22.384799</td>\n",
       "      <td>-348.991178</td>\n",
       "      <td>-31.220432</td>\n",
       "      <td>-62.285868</td>\n",
       "      <td>-139.475410</td>\n",
       "      <td>-29.918055</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-04</td>\n",
       "      <td>56.206304</td>\n",
       "      <td>34.396259</td>\n",
       "      <td>-68.247037</td>\n",
       "      <td>48.676899</td>\n",
       "      <td>-14.084260</td>\n",
       "      <td>54.808746</td>\n",
       "      <td>-30.941363</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-05</td>\n",
       "      <td>31.208937</td>\n",
       "      <td>27.351933</td>\n",
       "      <td>73.444423</td>\n",
       "      <td>30.488649</td>\n",
       "      <td>-126.660549</td>\n",
       "      <td>30.632576</td>\n",
       "      <td>113.526526</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-06</td>\n",
       "      <td>-15.854456</td>\n",
       "      <td>-31.193865</td>\n",
       "      <td>-20.390623</td>\n",
       "      <td>-15.657028</td>\n",
       "      <td>-24.404527</td>\n",
       "      <td>-11.555478</td>\n",
       "      <td>-9.580000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-03-09</td>\n",
       "      <td>215.249052</td>\n",
       "      <td>26.385113</td>\n",
       "      <td>29.598531</td>\n",
       "      <td>-124.104251</td>\n",
       "      <td>-22.207788</td>\n",
       "      <td>101.617067</td>\n",
       "      <td>34.424564</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-16</td>\n",
       "      <td>46.430852</td>\n",
       "      <td>287.221900</td>\n",
       "      <td>-208.118030</td>\n",
       "      <td>245.101990</td>\n",
       "      <td>-17.418606</td>\n",
       "      <td>45.674409</td>\n",
       "      <td>266.579661</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-17</td>\n",
       "      <td>-43.267657</td>\n",
       "      <td>-17.239068</td>\n",
       "      <td>-39.219180</td>\n",
       "      <td>63.645785</td>\n",
       "      <td>-11.743194</td>\n",
       "      <td>-25.330060</td>\n",
       "      <td>-59.718436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-18</td>\n",
       "      <td>86.562513</td>\n",
       "      <td>91.248053</td>\n",
       "      <td>297.372237</td>\n",
       "      <td>107.029750</td>\n",
       "      <td>-205.755377</td>\n",
       "      <td>-107.737103</td>\n",
       "      <td>85.991553</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-22</td>\n",
       "      <td>-48.471969</td>\n",
       "      <td>-15.204313</td>\n",
       "      <td>-47.507188</td>\n",
       "      <td>-188.529393</td>\n",
       "      <td>178.796388</td>\n",
       "      <td>-68.414025</td>\n",
       "      <td>134.171162</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2019-04-23</td>\n",
       "      <td>17.486958</td>\n",
       "      <td>31.994509</td>\n",
       "      <td>26.721742</td>\n",
       "      <td>15.445304</td>\n",
       "      <td>24.341884</td>\n",
       "      <td>13.763808</td>\n",
       "      <td>15.358321</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1043 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            SOROS FUND MANAGEMENT LLC  PAULSON & CO.INC.   \\\n",
       "Date                                                        \n",
       "2015-03-03                 -99.039430          -22.384799   \n",
       "2015-03-04                  56.206304           34.396259   \n",
       "2015-03-05                  31.208937           27.351933   \n",
       "2015-03-06                 -15.854456          -31.193865   \n",
       "2015-03-09                 215.249052           26.385113   \n",
       "...                               ...                 ...   \n",
       "2019-04-16                  46.430852          287.221900   \n",
       "2019-04-17                 -43.267657          -17.239068   \n",
       "2019-04-18                  86.562513           91.248053   \n",
       "2019-04-22                 -48.471969          -15.204313   \n",
       "2019-04-23                  17.486958           31.994509   \n",
       "\n",
       "            TIGER GLOBAL MANAGEMENT LLC  BERKSHIRE HATHAWAY INC      Algo 1  \\\n",
       "Date                                                                          \n",
       "2015-03-03                  -348.991178              -31.220432  -62.285868   \n",
       "2015-03-04                   -68.247037               48.676899  -14.084260   \n",
       "2015-03-05                    73.444423               30.488649 -126.660549   \n",
       "2015-03-06                   -20.390623              -15.657028  -24.404527   \n",
       "2015-03-09                    29.598531             -124.104251  -22.207788   \n",
       "...                                 ...                     ...         ...   \n",
       "2019-04-16                  -208.118030              245.101990  -17.418606   \n",
       "2019-04-17                   -39.219180               63.645785  -11.743194   \n",
       "2019-04-18                   297.372237              107.029750 -205.755377   \n",
       "2019-04-22                   -47.507188             -188.529393  178.796388   \n",
       "2019-04-23                    26.721742               15.445304   24.341884   \n",
       "\n",
       "                Algo 2      S&P500  \n",
       "Date                                \n",
       "2015-03-03 -139.475410  -29.918055  \n",
       "2015-03-04   54.808746  -30.941363  \n",
       "2015-03-05   30.632576  113.526526  \n",
       "2015-03-06  -11.555478   -9.580000  \n",
       "2015-03-09  101.617067   34.424564  \n",
       "...                ...         ...  \n",
       "2019-04-16   45.674409  266.579661  \n",
       "2019-04-17  -25.330060  -59.718436  \n",
       "2019-04-18 -107.737103   85.991553  \n",
       "2019-04-22  -68.414025  134.171162  \n",
       "2019-04-23   13.763808   15.358321  \n",
       "\n",
       "[1043 rows x 7 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Annualzied Sharpe Ratios\n",
    "# YOUR CODE HERE\n",
    "sharpe_ratios = (combined_daily_returns_df.std() * 252) / (combined_daily_returns_df * np.sqrt(252))\n",
    "sharpe_ratios"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " plot() these sharpe ratios using a barplot.\n",
    " On the basis of this performance metric, do our algo strategies outperform both 'the market' and the whales?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x21a03cbf0c8>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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VwPQpEkTbr31VmfavHnzGD58OACzZ88mKiqKdu3aERMTQ+/evVm1alXAZT/11FOICNu3b3fKpk+fjog4ywL46aefEBGWLFniN7+I8MgjjzjPn332WZ566im/OvHx8dxxxx35lv2vf/2Lli1b0rZtW+Lj43n44YfJyclx1q9t27bONhk7diwAw4cPp3LlyqSmpjrt/OlPf0JEOHLkSMDt+fTTTzvbr0OHDs58q1evplu3bixZssSpW7VqVVq0aEFCQgJDhw71i3fXrl3ExsbmW4/hw4czb968fOVbt27l+uuvJzo6mlatWjFgwAAOHjyYr965pIlEqRL0zTffsGjRIn788Ud+/vlnli5dyiWXWEPEPf7446SmprJ161a2bdtGv3796N+/v5MQKlWqxNq1a0lOTqZ27dq89NJLAGRkZHDTTTcxfvx4tm7dyrp161i1ahUvv/wyAE8++STXXXcd69atY+PGjc4OLS9v+95HkyZNirVOq1evZsOGDQGnDRw4kJ9++olt27Yxfvx4+vfvz6ZNmwLWbdu2LUlJSc7zefPm0bp1a786iYmJdO7cmcTERL/yiIgIPvjgA2cnntemTZvweDwsX76c06dPO+WvvPIKn376Kd9++y3r16/nhx9+oF69emRkZDh1li1b5myT559/3imPjo5mwQJr5CaPx8OyZcto2PC3Acfzbs/x45379nHo0CE++eQTfPXu3dup26FDB+bMmcPatWt58803A65TcWRmZnLDDTcwevRotm/fzqZNmxg9ejSHDx8+6zaLQxOJUiVo//791K1bl4iICADq1q1LgwYNSE9P57///S/Tp08nJMS6H9uIESOIiIjgiy++yNdOp06d2Lt3LwDvvPMOV199Nb169QKgcuXKvPjii07C2L9/P40aNXLmjYuLO6fr9OijjzJlypQi63Xv3p1Ro0Yxc+bMgNP79evn7Jh37txJjRo1iIqKcqYbY5g3bx6zZ8/m008/9TsBHBoayqhRo5g+fXrAtt955x2GDBlCr169WLhwoVM+efJk/v3vf1OzpnUz1/DwcMaPH0/16tWLXJ877riDuXPnAvDll19y9dVXExpavAtfH3vsMSZNmlSsusF455136NSpEzfeeKNT1r1794A9mnNJL/9VFcrf/reBjftOndM2Wzeozl9vbBNwWq9evfj73/9O8+bN6dmzJwMHDqRr165s376dxo0b59uBdejQgQ0bNtCjRw+nzO128/nnnzNypHXT0A0bNnD55Zf7zdesWTPS0tI4deoUY8aMYeDAgbz44ov07NmTESNG0KBBg3yxZWRkkJCQAEDTpk2ZP39+sdZ3wIABvPzyy36HpQrSvn17Xn311YDTqlevziWXXEJycjILFixg4MCB/Pe//3Wmr1y5kqZNm9KsWTO6devGxx9/TP/+/Z3pY8aMIS4ujj//+c/52p47dy6fffYZW7Zs4cUXX+SOO+4gNTWVtLS0Ii9r7d69u5Pchw0bxkMPPQRATEwMCxYs4Pjx4yQmJvKHP/zBr5fhuz0BJkyYwMCBAwHri8D8+fNZtmwZ1apVK2qznbXk5OR8743SoD0SpUpQ1apVWbNmDTNnziQqKoqBAwcye/ZsjDEBr47xLffumOrUqcOxY8e47rrr8tXJS0To3bs3O3fu5J577mHz5s20a9cu4KEN30Mx3iRSWLteISEhPPbYY0ydOrXI9f/tzhKBDRo0iKSkJD788ENuueUWv2mJiYkMGjTIqZf38Fb16tUZOnSo3+EngB9++IGoqCguvfRSevTowY8//sjx48fzbTfvOYomTZr4ncvxPbTlTSJe/fv3Jykpie+++44uXbr4Tct7aMubRLyeeOKJUumVlAXtkagKpaCeQ0kKCQmhW7dudOvWjbZt2/LGG29w++23s3v3blJTU/2+of7444/OYQnvjunkyZP07duXl156ibFjx9KmTRuWL1/ut4ydO3dStWpVp63atWszePBgBg8eTN++fVm+fLnfSfKC1KlTh+PHj/uVHTt2jLp16/qVDRkyhKlTp9KmTeHb86effqJVq1YFTr/xxht57LHH6NChg1/vzO128/7777Nw4UImT57s/FAu7/Z68MEHad++PSNGjHDKEhMT2bx5s3PO59SpU7z//vvcfffdVKlShV9++YWmTZvSu3dvevfuTd++fcnOzi5y24CV0Nq3b8+wYcNwuc7se/i1117LX/7yF7799tszmu9MtGnThq+++qrE2i+I9kiUKkFbtmxh27ZtzvO1a9dy6aWXUqVKFYYNG8bDDz+M223d/eDNN98kPT2da6+91q+NGjVq8Pzzz/Pss8+Sk5PDnXfeyYoVK1i6dClg9VzGjh3rHOL54osvSE+3bg+UmprKjh07in1n0CuuuIKVK1dy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NycmJob33nvPb/j866+/nn379hW6/UaOHElubq7zPC4ujueee4477riDVq1aERsby/79+wFYuHAhTz75ZKHtqeDoMPLqgqHDyCt1bugw8koppUqVJhKllFJB0USilFIqKOckkYjIoyJiRKSu/VxE5HkR2S4iP4tIe5+6w0Rkm/0Y5lN+uYist+d5XuwzbyJSW0Q+s+t/JiK1ilqGUkqp0hN0IhGRS4DrgF99in8PxNiPUcC/7bq1gb8CVwIdgb96E4NdZ5TPfH3s8vHA58aYGOBz+3mBy1BKKVW6zkWPZDrwZ8D38q+bgTeN5VugpohcDPQGPjPGHDPGHAc+A/rY06obY74x1mVkbwL9fNp6w/77jTzlgZahlFKqFAWVSETkJmCvMSbvL5gaAnt8nqfYZYWVpwQoB6hvjNkPYP9fr4hlBIpzlIisFpHVhw8fLubaKRW8o0ePkpCQQEJCAhdddBENGzZ0nvv+IHDbtm307duXZs2acfnll9O9e3eWL18OwOzZs4mKinLmS0hIYOPGjezatYtKlSqRkJBA69atGTp0KDk5OQHjKKr9+++/P988J0+eZOjQoTRr1oxmzZoxdOhQTp48CeC37Pj4eK666iq2bNniN/+f/vQnGjZsiMfjccoKWpavbt260bhxY7/RgPv160fVqlX96k2fPp3IyEgnJijesPiHDx8mLCyMV1991a+9tLQ0Ro8eTbNmzWjXrh2XX345//nPf/Ktr/fh/ZFnkyZNnCFmvLy3DfDGVKNGDb95ly5dCljD3viOEfbss8/y1FNPMXnyZKeu9zYECQkJPP/8837LKWh7NmnShCNHjuQrL6mh9otMJCKyVESSAzxuBiYCgX7pE2jQHHMW5YWGVtx5jDEzjTEdjDEdoqKiimhWqXOnTp06rF27lrVr1/LHP/6Rhx56yHnuclkfv8zMTG644QZGjRrFjh07WLNmDS+88AI7d+502hk4cKAz39q1a2ndujUAzZo1Y+3ataxfv56UlBTefffdfDEUp/1ARo4cyWWXXcaOHTvYsWMHTZs25e6773ame5e9bt06hg0b5vcjR4/Hw/z587nkkkuchHUmatasycqVKwE4ceKE8+NCX4mJiVxxxRX57otS1LD47733Hr/73e+csc287r77bmrVqsW2bdv46aefWLx4MceOHcu3vt7H0KFDnWmpqans2WN9r/WOSOCrS5cufvP27NkTsAbC/OCDD/Lt9CdOnOjU9Q6xs3btWsaOHVvgehWlJIfaLzKRGGN6GmNi8z6AnUBTYJ2I7AIaAT+KyEVYvQPfcRMaAfuKKG8UoBzgoPeQlf3/Ibu8oLaUOq/MmTOHTp06cdNNNzllsbGxfjdtKkpISAgdO3Zk796956T97du3s2bNGv7yl784ZU8++SSrV69mx44d+eqfOnWKWrVqOc+XLVtGbGwso0ePzrfDLo5BgwY5Q+t/8MEH9O/f32/6jh07SEtLY9KkSfnaL2pY/MTERP7v//6PlJQUZ3vt2LGD77//nkmTJjkJPioqinHjxhUr3gEDBjB37lyn/TvuuKNY84WGhjJq1CimT59erPrBKMmh9s960EZjzHp+O8yEnUw6GGOOiMhC4H4RScI6sX7SGLNfRJYAU3xOsPcCJhhjjolIqoj8DvgOGAq8YNdZCAwDnrb/X+BTnm8ZZ7s+qmJ45vtn2Hxsc9EVz0DL2i0Z17F4O5xANmzYUOTw8XPnzmXFihXO82+++cZvemZmJt999x0zZsw4q/bz2rhxo3NYxct7iGXDhg3ExcWxY8cOEhISSE1NJT09ne+++86p692Z3nzzzTz++OPk5OQQFhZW7OX36NGDe+65B7fbTVJSEjNnzuQf//hHvva7dOnCli1bOHToEPXqObujAofF37NnDwcOHKBjx47Ozv/hhx9mw4YNxMfHO0kkEO/6er3wwgvOIa3bbruN4cOH8+ijj/K///2POXPm8NZbbzl1v/76a79533//fWeY/TFjxhAXF8ef//znYm+fs1GSQ+2X1O9IPsbqsWwH/gPcB2CMOQb8A/jBfvzdLgMYDbxmz7MD+MQufxq4TkS2YV0d9nRhy1DqfHfLLbcQGxvr9y0876GtSpUqAb/t3OrUqUPjxo2Ji4s7q/bzKs5w795DPTt27OC5555j1KhRgDVo5Mcff0y/fv2oXr06V155JZ9++ukZbYOQkBA6d+7M3LlzycjIoEmTJn7Tk5KSGDRoEC6Xi/79+/Pee+/5TS9oWPykpCQGDBgA+A/dn5f3HEWDBg2csryHtnzPi9SuXZtatWqRlJREq1at8g2ImffQlu+9WqpXr87QoUPznf84n5yzYeSNMU18/jbAmALqvQ68HqB8NRAboPwokO9uN4UtQ6mCBNNzKClt2rTxO48wf/58Vq9eXawTod6d2/79++nWrRsLFy70O4R1tu23adOGn376CY/H43xL93g8rFu3LuC4ZTfddJNzF8bFixdz8uRJ2rZtC1j3k69cuTI33HBDkevja9CgQdxyyy089dRTfuU///wz27Ztc3ob2dnZXHbZZYwZ4787CDQsfmJiIgcPHmTOnDkA7Nu3j23bttG6dWvWrVvnrO/EiROZOHFivhP8hRk4cCBjxoxh9uzZZ7SeAA8++CDt27d3tmFJKMmh9vWX7UqVscGDB7Ny5UoWLlzolHlvg1tcF198MU8//XTAGz6dTfvR0dG0a9eOSZMmOWWTJk2iffv2REdH56u/YsUK51t2YmIir732Grt27WLXrl388ssvfPrpp2e8Tl26dGHChAn5zjckJiby1FNPOe3v27ePvXv3snv3br96eYfF37JlC6dPn2bv3r3OvBMmTCApKYno6Gg6dOjAE0884Qxvn5mZWaz7yHvdcsst/PnPf6Z3795ntJ5g9WgGDBjArFmzznje4irJofY1kShVxipVqsSiRYt45ZVXuOyyy+jUqROTJk3iiSeecOrMnTvX7/LRVatW5WunX79+pKen5zucU5z2Z8+e7QxL36hRI1JSUpg1axZbt24lOjqaZs2asXXrVr8dnfewWnx8PI8//jivvfYa6enpLFmyxK/3UaVKFTp37uxckhtoWYGICI8++mi+G3olJSXlG4L/lltuCXjfe99h8Qsaut97eOu1117j6NGjREdHc/nll9OzZ0+eeeaZfOtb0KW41apVY9y4cYSHh+eLw3uOxPuYN29evjqPPPJIwEt2i1LQ9oyLi3PKHn744UKH2g+WDiOvLhg6jLxS54YOI6+UUqpUaSJRSikVFE0kSimlgqKJRCmlVFA0kSillAqKJhKllFJB0USiVAnzjlEVHx9P+/btnd+AFDU0edu2bYmLi6Nr165+P7bz/bX1xx9/TExMDL/++itbtmyhW7duJCQk0KpVK2fIki+//JK+ffv6xTR8+HDntwzdunXDe0l8Ycv1Hc48ISGBp59+mrx82w0UL+Qf/n3JkiVOm1WrVqVFixYkJCQwdOjQImOHwMPCz5gxgwcffNB5fu+99zoj7oI1TpbvSLrz589HRNi82RqHLTMzk5YtW7J+/XqnzrRp0/jjH/+Yb52967dr1y5EhBdeeMGZdv/99/v90v3Z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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualize the sharpe ratios as a bar plot\n",
    "# YOUR CODE HERE\n",
    "sharpe_ratios.plot( title='Sharpe ratios')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Portfolio Returns\n",
    "\n",
    "In this section, you will build your own portfolio of stocks, calculate the returns, and compare the results to the Whale Portfolios and the S&P 500. \n",
    "\n",
    "1. Choose 3-5 custom stocks with at last 1 year's worth of historic prices and create a DataFrame of the closing prices and dates for each stock.\n",
    "2. Calculate the weighted returns for the portfolio assuming an equal number of shares for each stock\n",
    "3. Join your portfolio returns to the DataFrame that contains all of the portfolio returns\n",
    "4. Re-run the performance and risk analysis with your portfolio to see how it compares to the others\n",
    "5. Include correlation analysis to determine which stocks (if any) are correlated"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Choose 3-5 custom stocks with at last 1 year's worth of historic prices and create a DataFrame of the closing prices and dates for each stock."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TSLA NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2018</td>\n",
       "      <td>334.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>344.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2018</td>\n",
       "      <td>337.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>347.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/12/2018</td>\n",
       "      <td>336.22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             TSLA NOCP\n",
       "Trade DATE            \n",
       "1/10/2018       334.80\n",
       "1/10/2019       344.97\n",
       "1/11/2018       337.95\n",
       "1/11/2019       347.26\n",
       "1/12/2018       336.22"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the first stock\n",
    "\n",
    "tsla_csv = Path(\"Resources/tsla_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "tsla_df = pd.read_csv(tsla_csv,index_col=\"Trade DATE\")\n",
    "tsla_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "tsla_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MSFT NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2018</td>\n",
       "      <td>87.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>103.60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2018</td>\n",
       "      <td>88.08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>102.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/12/2018</td>\n",
       "      <td>89.60</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             MSFT NOCP\n",
       "Trade DATE            \n",
       "1/10/2018        87.82\n",
       "1/10/2019       103.60\n",
       "1/11/2018        88.08\n",
       "1/11/2019       102.80\n",
       "1/12/2018        89.60"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the second stock\n",
    "msft_csv = Path(\"Resources/msft_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "msft_df = pd.read_csv(msft_csv,index_col=\"Trade DATE\")\n",
    "msft_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "msft_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>EVN NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2018</td>\n",
       "      <td>12.36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>11.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2018</td>\n",
       "      <td>12.29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>11.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/12/2018</td>\n",
       "      <td>12.24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            EVN NOCP\n",
       "Trade DATE          \n",
       "1/10/2018      12.36\n",
       "1/10/2019      11.53\n",
       "1/11/2018      12.29\n",
       "1/11/2019      11.49\n",
       "1/12/2018      12.24"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evn_csv = Path(\"Resources/evn_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "evn_df = pd.read_csv(evn_csv,index_col=\"Trade DATE\")\n",
    "evn_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "evn_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>AAPL NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>153.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>152.29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>150.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>153.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>154.94</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            AAPL NOCP\n",
       "Trade DATE           \n",
       "1/10/2019      153.80\n",
       "1/11/2019      152.29\n",
       "1/14/2019      150.00\n",
       "1/15/2019      153.07\n",
       "1/16/2019      154.94"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the forth stock\n",
    "aapl_csv = Path(\"Resources/aapl_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "aapl_df = pd.read_csv(aapl_csv,index_col=\"Trade DATE\")\n",
    "aapl_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "aapl_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>COST NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>210.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>210.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>209.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>211.03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>210.18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            COST NOCP\n",
       "Trade DATE           \n",
       "1/10/2019      210.64\n",
       "1/11/2019      210.51\n",
       "1/14/2019      209.00\n",
       "1/15/2019      211.03\n",
       "1/16/2019      210.18"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read the fifths stock\n",
    "cost_csv = Path(\"Resources/cost_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "cost_df = pd.read_csv(cost_csv,index_col=\"Trade DATE\")\n",
    "cost_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "cost_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>GOOG NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>1070.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>1057.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>1044.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>1077.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>1080.97</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            GOOG NOCP\n",
       "Trade DATE           \n",
       "1/10/2019     1070.33\n",
       "1/11/2019     1057.19\n",
       "1/14/2019     1044.69\n",
       "1/15/2019     1077.15\n",
       "1/16/2019     1080.97"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "goog_csv = Path(\"Resources/goog_historical.csv\")\n",
    "# YOUR CODE HERE\n",
    "goog_df = pd.read_csv(goog_csv,index_col=\"Trade DATE\")\n",
    "goog_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "goog_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MSFT NOCP</th>\n",
       "      <th>TSLA NOCP</th>\n",
       "      <th>EVN NOCP</th>\n",
       "      <th>AAPL NOCP</th>\n",
       "      <th>COST NOCP</th>\n",
       "      <th>GOOG NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>103.60</td>\n",
       "      <td>344.97</td>\n",
       "      <td>11.53</td>\n",
       "      <td>153.80</td>\n",
       "      <td>210.64</td>\n",
       "      <td>1070.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>102.80</td>\n",
       "      <td>347.26</td>\n",
       "      <td>11.49</td>\n",
       "      <td>152.29</td>\n",
       "      <td>210.51</td>\n",
       "      <td>1057.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>102.05</td>\n",
       "      <td>334.40</td>\n",
       "      <td>11.47</td>\n",
       "      <td>150.00</td>\n",
       "      <td>209.00</td>\n",
       "      <td>1044.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>105.01</td>\n",
       "      <td>344.43</td>\n",
       "      <td>11.45</td>\n",
       "      <td>153.07</td>\n",
       "      <td>211.03</td>\n",
       "      <td>1077.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>105.38</td>\n",
       "      <td>346.05</td>\n",
       "      <td>11.41</td>\n",
       "      <td>154.94</td>\n",
       "      <td>210.18</td>\n",
       "      <td>1080.97</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             MSFT NOCP   TSLA NOCP  EVN NOCP  AAPL NOCP  COST NOCP  GOOG NOCP\n",
       "Trade DATE                                                                   \n",
       "1/10/2019       103.60      344.97     11.53     153.80     210.64    1070.33\n",
       "1/11/2019       102.80      347.26     11.49     152.29     210.51    1057.19\n",
       "1/14/2019       102.05      334.40     11.47     150.00     209.00    1044.69\n",
       "1/15/2019       105.01      344.43     11.45     153.07     211.03    1077.15\n",
       "1/16/2019       105.38      346.05     11.41     154.94     210.18    1080.97"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Concatenate all stocks into a single DataFrame\n",
    "# YOUR CODE HERE\n",
    "all_stocks_df = pd.concat([msft_df, tsla_df, evn_df, aapl_df, cost_df, goog_df], axis=\"columns\", join=\"inner\")\n",
    "all_stocks_df.sort_values(\"Trade DATE\", ascending=True, inplace=True)\n",
    "all_stocks_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Trade DATE</th>\n",
       "      <th>MSFT NOCP</th>\n",
       "      <th>TSLA NOCP</th>\n",
       "      <th>EVN NOCP</th>\n",
       "      <th>AAPL NOCP</th>\n",
       "      <th>COST NOCP</th>\n",
       "      <th>GOOG NOCP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>103.60</td>\n",
       "      <td>344.97</td>\n",
       "      <td>11.53</td>\n",
       "      <td>153.80</td>\n",
       "      <td>210.64</td>\n",
       "      <td>1070.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>102.80</td>\n",
       "      <td>347.26</td>\n",
       "      <td>11.49</td>\n",
       "      <td>152.29</td>\n",
       "      <td>210.51</td>\n",
       "      <td>1057.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>102.05</td>\n",
       "      <td>334.40</td>\n",
       "      <td>11.47</td>\n",
       "      <td>150.00</td>\n",
       "      <td>209.00</td>\n",
       "      <td>1044.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>105.01</td>\n",
       "      <td>344.43</td>\n",
       "      <td>11.45</td>\n",
       "      <td>153.07</td>\n",
       "      <td>211.03</td>\n",
       "      <td>1077.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>105.38</td>\n",
       "      <td>346.05</td>\n",
       "      <td>11.41</td>\n",
       "      <td>154.94</td>\n",
       "      <td>210.18</td>\n",
       "      <td>1080.97</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Trade DATE   MSFT NOCP   TSLA NOCP  EVN NOCP  AAPL NOCP  COST NOCP  \\\n",
       "0  1/10/2019      103.60      344.97     11.53     153.80     210.64   \n",
       "1  1/11/2019      102.80      347.26     11.49     152.29     210.51   \n",
       "2  1/14/2019      102.05      334.40     11.47     150.00     209.00   \n",
       "3  1/15/2019      105.01      344.43     11.45     153.07     211.03   \n",
       "4  1/16/2019      105.38      346.05     11.41     154.94     210.18   \n",
       "\n",
       "   GOOG NOCP  \n",
       "0    1070.33  \n",
       "1    1057.19  \n",
       "2    1044.69  \n",
       "3    1077.15  \n",
       "4    1080.97  "
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reset the index\n",
    "# YOUR CODE HERE\n",
    "all_stocks_df.reset_index(inplace=True)\n",
    "all_stocks_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Trade DATE</th>\n",
       "      <th>MSFT NOCP</th>\n",
       "      <th>TSLA NOCP</th>\n",
       "      <th>EVN NOCP</th>\n",
       "      <th>AAPL NOCP</th>\n",
       "      <th>COST NOCP</th>\n",
       "      <th>GOOG NOCP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>103.60</td>\n",
       "      <td>344.97</td>\n",
       "      <td>11.53</td>\n",
       "      <td>153.80</td>\n",
       "      <td>210.64</td>\n",
       "      <td>1070.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>102.80</td>\n",
       "      <td>347.26</td>\n",
       "      <td>11.49</td>\n",
       "      <td>152.29</td>\n",
       "      <td>210.51</td>\n",
       "      <td>1057.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>102.05</td>\n",
       "      <td>334.40</td>\n",
       "      <td>11.47</td>\n",
       "      <td>150.00</td>\n",
       "      <td>209.00</td>\n",
       "      <td>1044.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>105.01</td>\n",
       "      <td>344.43</td>\n",
       "      <td>11.45</td>\n",
       "      <td>153.07</td>\n",
       "      <td>211.03</td>\n",
       "      <td>1077.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>105.38</td>\n",
       "      <td>346.05</td>\n",
       "      <td>11.41</td>\n",
       "      <td>154.94</td>\n",
       "      <td>210.18</td>\n",
       "      <td>1080.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>245</td>\n",
       "      <td>9/28/2018</td>\n",
       "      <td>114.37</td>\n",
       "      <td>264.77</td>\n",
       "      <td>11.48</td>\n",
       "      <td>225.74</td>\n",
       "      <td>234.88</td>\n",
       "      <td>1193.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>246</td>\n",
       "      <td>9/4/2018</td>\n",
       "      <td>111.71</td>\n",
       "      <td>288.95</td>\n",
       "      <td>12.11</td>\n",
       "      <td>228.36</td>\n",
       "      <td>234.68</td>\n",
       "      <td>1197.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>247</td>\n",
       "      <td>9/5/2018</td>\n",
       "      <td>108.49</td>\n",
       "      <td>280.74</td>\n",
       "      <td>12.01</td>\n",
       "      <td>226.87</td>\n",
       "      <td>235.61</td>\n",
       "      <td>1186.48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>248</td>\n",
       "      <td>9/6/2018</td>\n",
       "      <td>108.74</td>\n",
       "      <td>280.95</td>\n",
       "      <td>12.06</td>\n",
       "      <td>223.10</td>\n",
       "      <td>236.68</td>\n",
       "      <td>1171.44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>249</td>\n",
       "      <td>9/7/2018</td>\n",
       "      <td>108.21</td>\n",
       "      <td>263.24</td>\n",
       "      <td>12.00</td>\n",
       "      <td>221.30</td>\n",
       "      <td>241.46</td>\n",
       "      <td>1164.83</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>250 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Trade DATE   MSFT NOCP   TSLA NOCP  EVN NOCP  AAPL NOCP  COST NOCP  \\\n",
       "0    1/10/2019      103.60      344.97     11.53     153.80     210.64   \n",
       "1    1/11/2019      102.80      347.26     11.49     152.29     210.51   \n",
       "2    1/14/2019      102.05      334.40     11.47     150.00     209.00   \n",
       "3    1/15/2019      105.01      344.43     11.45     153.07     211.03   \n",
       "4    1/16/2019      105.38      346.05     11.41     154.94     210.18   \n",
       "..         ...         ...         ...       ...        ...        ...   \n",
       "245  9/28/2018      114.37      264.77     11.48     225.74     234.88   \n",
       "246   9/4/2018      111.71      288.95     12.11     228.36     234.68   \n",
       "247   9/5/2018      108.49      280.74     12.01     226.87     235.61   \n",
       "248   9/6/2018      108.74      280.95     12.06     223.10     236.68   \n",
       "249   9/7/2018      108.21      263.24     12.00     221.30     241.46   \n",
       "\n",
       "     GOOG NOCP  \n",
       "0      1070.33  \n",
       "1      1057.19  \n",
       "2      1044.69  \n",
       "3      1077.15  \n",
       "4      1080.97  \n",
       "..         ...  \n",
       "245    1193.47  \n",
       "246    1197.00  \n",
       "247    1186.48  \n",
       "248    1171.44  \n",
       "249    1164.83  \n",
       "\n",
       "[250 rows x 7 columns]"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Drop Nulls\n",
    "# YOUR CODE HERE\n",
    "all_stocks_df.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MSFT NOCP</th>\n",
       "      <th>TSLA NOCP</th>\n",
       "      <th>EVN NOCP</th>\n",
       "      <th>AAPL NOCP</th>\n",
       "      <th>COST NOCP</th>\n",
       "      <th>GOOG NOCP</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Trade DATE</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1/10/2019</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/11/2019</td>\n",
       "      <td>-0.007722</td>\n",
       "      <td>0.006638</td>\n",
       "      <td>-0.003469</td>\n",
       "      <td>-0.009818</td>\n",
       "      <td>-0.000617</td>\n",
       "      <td>-0.012277</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/14/2019</td>\n",
       "      <td>-0.007296</td>\n",
       "      <td>-0.037033</td>\n",
       "      <td>-0.001741</td>\n",
       "      <td>-0.015037</td>\n",
       "      <td>-0.007173</td>\n",
       "      <td>-0.011824</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/15/2019</td>\n",
       "      <td>0.029005</td>\n",
       "      <td>0.029994</td>\n",
       "      <td>-0.001744</td>\n",
       "      <td>0.020467</td>\n",
       "      <td>0.009713</td>\n",
       "      <td>0.031071</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1/16/2019</td>\n",
       "      <td>0.003523</td>\n",
       "      <td>0.004703</td>\n",
       "      <td>-0.003493</td>\n",
       "      <td>0.012217</td>\n",
       "      <td>-0.004028</td>\n",
       "      <td>0.003546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9/28/2018</td>\n",
       "      <td>-0.000350</td>\n",
       "      <td>-0.139015</td>\n",
       "      <td>-0.006061</td>\n",
       "      <td>0.003512</td>\n",
       "      <td>0.003761</td>\n",
       "      <td>-0.000979</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9/4/2018</td>\n",
       "      <td>-0.023258</td>\n",
       "      <td>0.091325</td>\n",
       "      <td>0.054878</td>\n",
       "      <td>0.011606</td>\n",
       "      <td>-0.000851</td>\n",
       "      <td>0.002958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9/5/2018</td>\n",
       "      <td>-0.028825</td>\n",
       "      <td>-0.028413</td>\n",
       "      <td>-0.008258</td>\n",
       "      <td>-0.006525</td>\n",
       "      <td>0.003963</td>\n",
       "      <td>-0.008789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9/6/2018</td>\n",
       "      <td>0.002304</td>\n",
       "      <td>0.000748</td>\n",
       "      <td>0.004163</td>\n",
       "      <td>-0.016617</td>\n",
       "      <td>0.004541</td>\n",
       "      <td>-0.012676</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9/7/2018</td>\n",
       "      <td>-0.004874</td>\n",
       "      <td>-0.063036</td>\n",
       "      <td>-0.004975</td>\n",
       "      <td>-0.008068</td>\n",
       "      <td>0.020196</td>\n",
       "      <td>-0.005643</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>250 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             MSFT NOCP   TSLA NOCP  EVN NOCP  AAPL NOCP  COST NOCP  GOOG NOCP\n",
       "Trade DATE                                                                   \n",
       "1/10/2019          NaN         NaN       NaN        NaN        NaN        NaN\n",
       "1/11/2019    -0.007722    0.006638 -0.003469  -0.009818  -0.000617  -0.012277\n",
       "1/14/2019    -0.007296   -0.037033 -0.001741  -0.015037  -0.007173  -0.011824\n",
       "1/15/2019     0.029005    0.029994 -0.001744   0.020467   0.009713   0.031071\n",
       "1/16/2019     0.003523    0.004703 -0.003493   0.012217  -0.004028   0.003546\n",
       "...                ...         ...       ...        ...        ...        ...\n",
       "9/28/2018    -0.000350   -0.139015 -0.006061   0.003512   0.003761  -0.000979\n",
       "9/4/2018     -0.023258    0.091325  0.054878   0.011606  -0.000851   0.002958\n",
       "9/5/2018     -0.028825   -0.028413 -0.008258  -0.006525   0.003963  -0.008789\n",
       "9/6/2018      0.002304    0.000748  0.004163  -0.016617   0.004541  -0.012676\n",
       "9/7/2018     -0.004874   -0.063036 -0.004975  -0.008068   0.020196  -0.005643\n",
       "\n",
       "[250 rows x 6 columns]"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daily_returns = all_stocks_df.pct_change()\n",
    "daily_returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Calculate the weighted returns for the portfolio assuming an equal number of shares for each stock"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Trade DATE\n",
       "1/10/2019         NaN\n",
       "1/11/2019   -0.004544\n",
       "1/14/2019   -0.013351\n",
       "1/15/2019    0.019751\n",
       "1/16/2019    0.002745\n",
       "dtype: float64"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate weighted portfolio returns\n",
    "weights = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]\n",
    "# YOUR CODE HERE\n",
    "portfolio_returns = daily_returns.dot(weights)\n",
    "portfolio_returns.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Join your portfolio returns to the DataFrame that contains all of the portfolio returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Trade DATE\n",
       "1/10/2019         NaN\n",
       "1/11/2019   -0.004544\n",
       "1/14/2019   -0.017834\n",
       "1/15/2019    0.001565\n",
       "1/16/2019    0.004314\n",
       "dtype: float64"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# YOUR CODE HERE \n",
    "cumulative_returns = (1 + portfolio_returns).cumprod() - 1\n",
    "cumulative_returns.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Trade DATE\n",
       "1/11/2019   -0.004544\n",
       "1/14/2019   -0.017834\n",
       "1/15/2019    0.001565\n",
       "1/16/2019    0.004314\n",
       "1/17/2019    0.009202\n",
       "               ...   \n",
       "9/28/2018    0.282896\n",
       "9/4/2018     0.312116\n",
       "9/5/2018     0.295310\n",
       "9/6/2018     0.291525\n",
       "9/7/2018     0.277232\n",
       "Length: 249, dtype: float64"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Only compare dates where return data exists for all the stocks (drop NaNs)\n",
    "# YOUR CODE HERE\n",
    "cumulative_returns.dropna(inplace=True)\n",
    "cumulative_returns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Re-run the performance and risk analysis with your portfolio to see how it compares to the others"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Risk\n",
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rolling\n",
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Beta\n",
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Annualzied Sharpe Ratios\n",
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualize the sharpe ratios as a bar plot\n",
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Include correlation analysis to determine which stocks (if any) are correlated"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# YOUR CODE HERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "file_extension": ".py",
  "kernel_info": {
   "name": "dev"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  },
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "nteract": {
   "version": "0.12.3"
  },
  "pygments_lexer": "ipython3",
  "version": 3
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
