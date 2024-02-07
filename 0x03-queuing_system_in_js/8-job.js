import kue from 'kue';
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Job is not an array');
  }
  for (const job_info of jobs) {
    const job = queue.create('push_notification_code_3', job_info);

    job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
      .on('process', (process, data) => console.log(`Notification job ${job.id} ${process}% complete`))
      .save();
  }
}

export default createPushNotificationsJobs;
