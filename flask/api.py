# @app.route('/export-csv', methods=['POST'])
# def export_csv():
#     # Assuming you have the data ready to be written to the CSV file
#     data = [
#         ['Name', 'Age', 'City'],
#         ['John', '25', 'New York'],
#         ['Emily', '30', 'Los Angeles'],
#         ['David', '35', 'Chicago']
#     ]

#     # Start the Celery task
#     task = csv_writer_task.apply_async(args=[data])

#     # Return the task ID as the response
#     return f"CSV export task initiated. Task ID: {task.id}"


# @app.route('/download-csv/<task_id>', methods=['GET'])
# def download_csv(task_id):
#     result = csv_writer_task.AsyncResult(task_id)

#     if result.ready():
#         # If the task is completed, send the CSV file as a response
#         file_path = 'export.csv'
#         try:
#             return send_file(file_path, as_attachment=True)
#         finally:
#             # Delete the CSV file
#             if os.path.exists(file_path):
#                 os.remove(file_path)
#     else:
#         # Task is still in progress, send a message indicating the status
#         return 'CSV export task is still in progress. Please try again later.'


# if __name__ == '__main__':
#     app.run()