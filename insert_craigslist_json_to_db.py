##
# Uploads craigslist job output json to wordpress db

import hashlib
import json
import os

import mysql.connector


JOBS_FILENAME = "jobsBoard/jobsBoard/jobs2.json"

# order:
# ID, post_content, post_title, post_name, guid,
SQL_TEMPLATE_POSTS = """
REPLACE INTO `Q53_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`,
 `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`,
  `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`,
   `post_type`, `post_mime_type`, `comment_count`) 
   VALUES (%s, 'craigslist_scraper', CURDATE(), CURDATE(), %s, %s, '', 
   'publish', 'closed', 'closed', '', %s, '', '',
    CURDATE(), CURDATE(), '', 0, %s, 0,
     'job_listing', '', 0)
"""
SQL_TEMPLATE_POST_META = "REPLACE INTO `Q53_postmeta` (`post_id`, `meta_key`, `meta_value`) VALUES (%s, %s, %s)"
META_KEYS = [
    {
        "meta_key": "_apply_link",
        "scraper_json_key": "url",
    },
    {
        "meta_key": "geolocation_lat",
        "scraper_json_key": "lattitude",
    },
    {
        "meta_key": "geolocation_long",
        "scraper_json_key": "longitude",
    },
]


def load_jobs_from_file():
    with open(JOBS_FILENAME, "r") as fp:
        jobs = json.load(fp)
        jobs = filter(lambda x: x["title"] != "", jobs)
        return list(jobs)


def job_json_to_post_vals(job_dict):
    description = job_dict["description"]
    post_id = hashlib.md5(description.encode('utf-8')).hexdigest()
    title = job_dict["title"]
    job_dict["post_id"] = post_id
    return post_id, description, title, post_id, post_id


def job_json_to_meta_vals(job_dict):
    sql_values = []
    for key_dict in META_KEYS:
        my_tuple = (job_dict["post_id"], key_dict["meta_key"], job_dict[key_dict["scraper_json_key"]])
        sql_values.append(my_tuple)
    return sql_values


def insert_jobs_to_wordpress(cnx, jobs_dicts):
    job_values = list(map(job_json_to_post_vals, jobs_dicts))
    meta_values = list(map(job_json_to_meta_vals, jobs_dicts))
    flattened_meta_values = [item for sublist in meta_values for item in sublist]

    with cnx.cursor() as cursor:
        cursor.executemany(SQL_TEMPLATE_POSTS, job_values)
        cursor.executemany(SQL_TEMPLATE_POST_META, flattened_meta_values)


def create_db_cnx():
    config = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'database': os.environ['DB_DATABASE']
    }
    return mysql.connector.connect(**config)


def main():
    jobs = load_jobs_from_file()
    with create_db_cnx() as cnx:
        insert_jobs_to_wordpress(cnx, jobs)
        cnx.commit()


if __name__ == "__main__":
    main()
