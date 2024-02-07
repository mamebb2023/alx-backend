import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const getResult = promisify(client.get).bind(client);
  const result = await getResult(schoolName);
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
