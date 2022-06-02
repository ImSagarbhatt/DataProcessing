import os
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, date
from zipfile36 import ZipFile


# get the file name
def get_latest_file(ti):
    file_name = "SS"+date.today().strftime("%y%m%d")+".zip"
    ti.xcom_push(key="filename", value=file_name)


# download the zip file
def download_zip(ti):
    file_name = ti.xcom_pull(
        key="filename", task_ids='get_latest_file')
    url = 'https://idxdata3.co.id/Download_Data/Daily/Stock_Summary/'
    print(file_name)
    download_link = url+file_name
    r2 = requests.get(download_link)
    zip_path = f"/home/gorapid/work/data-processing/datafiles/{file_name}"
    open(zip_path, 'wb').write(r2.content)
    ti.xcom_push(key="zip_path", value=zip_path)


# extract the zip file
def extract_zip(ti):
    zip_path = ti.xcom_pull(
        key="zip_path", task_ids='zip_download')
    zip_path = download_zip()
    with ZipFile(zip_path, 'r') as zipobj:
        zipobj.extractall('/home/gorapid/work/data-processing/datafiles/')


# read the extracted file
def read_extract_file(ti):
    file_name = ti.xcom_pull(
        key="filename", task_ids='get_latest_file')
    extract_file = file_name.replace('zip', 'DBF')
    os.system(
        f"dbview /home/gorapid/work/data-processing/datafiles/{extract_file}")


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 3, 5),
    'depends_on_past': False,
    'retries': 0
}


dag = DAG(
    dag_id="read_zip",
    default_args=default_args,
    schedule_interval="@once",
    catchup=False
)


get_latest_file = PythonOperator(
    task_id='get_latest_file', python_callable=get_latest_file, dag=dag)
zip_download = PythonOperator(
    task_id='zip_download', python_callable=download_zip, dag=dag)
zip_extract = PythonOperator(
    task_id='zip_extract', python_callable=download_zip, dag=dag)
read_file = PythonOperator(
    task_id='read_file', python_callable=read_extract_file, dag=dag)

# dependencies of tasks
get_latest_file >> zip_download >> zip_extract >> read_file
