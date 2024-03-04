{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyO5NOyDkxWL6dzh34teUmi1"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["!pip install matplotlib\n","!pip install uszipcode\n","import matplotlib as plt\n","import pandas as pd\n","import os\n","\n","from google.colab import drive\n","drive.mount('/content/drive')"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"c-WPo4OvT_rk","executionInfo":{"status":"ok","timestamp":1709586833892,"user_tz":300,"elapsed":42798,"user":{"displayName":"Thomas Suchecki","userId":"00331142334902318229"}},"outputId":"2e26e8d5-aa6c-497f-8f55-94ab9d409860"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (3.7.1)\n","Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.2.0)\n","Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (0.12.1)\n","Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (4.49.0)\n","Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.4.5)\n","Requirement already satisfied: numpy>=1.20 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.25.2)\n","Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (23.2)\n","Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (9.4.0)\n","Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (3.1.1)\n","Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (2.8.2)\n","Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n","Collecting uszipcode\n","  Downloading uszipcode-1.0.1-py2.py3-none-any.whl (35 kB)\n","Requirement already satisfied: attrs in /usr/local/lib/python3.10/dist-packages (from uszipcode) (23.2.0)\n","Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from uszipcode) (2.31.0)\n","Collecting pathlib-mate (from uszipcode)\n","  Downloading pathlib_mate-1.3.2-py3-none-any.whl (56 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.0/57.0 kB\u001b[0m \u001b[31m3.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hCollecting atomicwrites (from uszipcode)\n","  Downloading atomicwrites-1.4.1.tar.gz (14 kB)\n","  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n","Collecting fuzzywuzzy (from uszipcode)\n","  Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)\n","Collecting haversine>=2.5.0 (from uszipcode)\n","  Downloading haversine-2.8.1-py2.py3-none-any.whl (7.7 kB)\n","Requirement already satisfied: SQLAlchemy>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from uszipcode) (2.0.27)\n","Collecting sqlalchemy-mate>=1.4.28.3 (from uszipcode)\n","  Downloading sqlalchemy_mate-1.4.28.4-py2.py3-none-any.whl (77 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.1/77.1 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hRequirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy>=1.4.0->uszipcode) (4.10.0)\n","Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy>=1.4.0->uszipcode) (3.0.3)\n","Collecting SQLAlchemy>=1.4.0 (from uszipcode)\n","  Downloading SQLAlchemy-1.4.52-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.6/1.6 MB\u001b[0m \u001b[31m17.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hRequirement already satisfied: prettytable in /usr/local/lib/python3.10/dist-packages (from sqlalchemy-mate>=1.4.28.3->uszipcode) (3.10.0)\n","Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->uszipcode) (3.3.2)\n","Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->uszipcode) (3.6)\n","Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->uszipcode) (2.0.7)\n","Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->uszipcode) (2024.2.2)\n","Requirement already satisfied: wcwidth in /usr/local/lib/python3.10/dist-packages (from prettytable->sqlalchemy-mate>=1.4.28.3->uszipcode) (0.2.13)\n","Building wheels for collected packages: atomicwrites\n","  Building wheel for atomicwrites (setup.py) ... \u001b[?25l\u001b[?25hdone\n","  Created wheel for atomicwrites: filename=atomicwrites-1.4.1-py2.py3-none-any.whl size=6942 sha256=961fa0180eda158c12a491bbd314e5ab83f9acd37d9b9ae79ea4f5627ecfdc62\n","  Stored in directory: /root/.cache/pip/wheels/34/07/0b/33b15f68736109f72ea0bb2499521d87312b932620737447a2\n","Successfully built atomicwrites\n","Installing collected packages: fuzzywuzzy, SQLAlchemy, pathlib-mate, haversine, atomicwrites, sqlalchemy-mate, uszipcode\n","  Attempting uninstall: SQLAlchemy\n","    Found existing installation: SQLAlchemy 2.0.27\n","    Uninstalling SQLAlchemy-2.0.27:\n","      Successfully uninstalled SQLAlchemy-2.0.27\n","\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n","ipython-sql 0.5.0 requires sqlalchemy>=2.0, but you have sqlalchemy 1.4.52 which is incompatible.\u001b[0m\u001b[31m\n","\u001b[0mSuccessfully installed SQLAlchemy-1.4.52 atomicwrites-1.4.1 fuzzywuzzy-0.18.0 haversine-2.8.1 pathlib-mate-1.3.2 sqlalchemy-mate-1.4.28.4 uszipcode-1.0.1\n","Mounted at /content/drive\n"]}]},{"cell_type":"code","source":["wd_path = '/content/drive/MyDrive/ursp688y/Exercise5'\n","os.chdir(wd_path)"],"metadata":{"id":"Md5wSQIkUA6z","executionInfo":{"status":"ok","timestamp":1709586837506,"user_tz":300,"elapsed":149,"user":{"displayName":"Thomas Suchecki","userId":"00331142334902318229"}}},"execution_count":3,"outputs":[]},{"cell_type":"code","execution_count":5,"metadata":{"id":"8c34TADYRgns","executionInfo":{"status":"ok","timestamp":1709586849124,"user_tz":300,"elapsed":128,"user":{"displayName":"Thomas Suchecki","userId":"00331142334902318229"}}},"outputs":[],"source":["import pandas as pd\n","import csv\n","import matplotlib.pyplot as plt\n","import numpy as np\n","from uszipcode import SearchEngine\n","import seaborn as sns\n","sns.set_style('ticks') # Set a default style for this Python session\n","\n","# Function to filter by project status\n","def filter_by_project_status(data, proj_status):\n","  mask = data['STATUS_PUBLIC'] == proj_status\n","  return mask\n","  #print(proj_status)\n","\n","# Function to add join csv files and to add zipcode information\n","def housing_function(housing_projects_info, ward_info, project_status):\n","  housing_projects_with_pops_props = pd.merge(housing_projects_info, ward_info, left_on='MAR_WARD', right_on='NAME')\n","\n","  housing_projects_with_pops_props = pd.merge(\n","      housing_projects_info, ward_info[['NAME','POP100','HU100']],\n","      left_on = 'MAR_WARD',\n","      right_on = 'NAME'\n","  )\n","\n","  # Creates the Zipcode column in the data frame.\n","  housing_projects_with_pops_props[\"Zipcode\"] = \"00000\"\n","  # eng is for zipcode finder\n","  eng = SearchEngine()\n","\n","  # For loop to populate the Zipcode column with accurate zipcodes for each project.\n","  # It iterates row by row to take the last 5 digits of the full address which\n","  # contain the zipcodes for each project\n","  for i, r in housing_projects_with_pops_props.iterrows():\n","    holder = r['ADDRESS']\n","    length = len(holder)\n","    zipcodes = holder[length - 5:]\n","    zipcodeSTR = str(zipcodes)\n","    # if statement to ensure the last five digits are the zipcode.\n","    if(zipcodes.isnumeric()):\n","      housing_projects_with_pops_props.at[i, 'Zipcode'] = zipcodeSTR\n","    # if statement is to catch the one address that did not include zipcode. I tried\n","    # to import and use the uszipcode locator funtion which is commented out below, but\n","    # I couldn't figure out how to actually retrieve the zipcode from the data structure.\n","    if(zipcodes.isnumeric() == False):\n","      missing_zipcode = eng.by_coordinates(r['LATITUDE'], r['LONGITUDE'], 1)\n","      housing_projects_with_pops_props.at[i, 'Zipcode'] = '20001'\n","      # housing_projects_with_pops_props.at[i, 'Zipcode'] = missing_zipcode\n","      # print(missing_zipcode.zipcode)\n","\n","  return housing_projects_with_pops_props\n","\n","def graph_function(ddff):\n","  ddff[ddff[\"STATUS_PUBLIC\"] == p_status]\n","  ddff.to_csv('test_file.csv', index=False)\n","\n","  zip_counts = ddff['Zipcode'].value_counts()\n","  zip_counts\n","\n","  names = zip_counts.index\n","  counts = zip_counts.values\n","\n","  sns.countplot(ddff, x='Zipcode', order=df['Zipcode'].value_counts().index)\n","\n","  ax = sns.barplot(ddff, x = 'Zipcode', y = zip_counts, errorbar = None)\n","  ax.set(\n","    xlabel='Zipcode',\n","    ylabel='Number of Projects'\n","  )\n","  plt.legend(title= \"Housing Projects in Washington D.C. by Zipcode\", frameon=False)\n","  plt.xticks(rotation=60)\n","  for i in ax.containers:\n","    ax.bar_label(i,)\n","  sns.despine()"]}]}