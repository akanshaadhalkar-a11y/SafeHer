// main.js - handles geolocation and send alert request (with CSRF)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function sendAlert(userId, messageEl, statusEl){
  statusEl.textContent = 'Getting location...';

  if(!userId){
    statusEl.textContent = 'Please select your name.';
    return;
  }

  const msg = messageEl.value || 'I need help. Please reach out!';

  function postPayload(lat, lng){
    statusEl.textContent = 'Sending alert...';
    const payload = { user_id: userId, message: msg, lat: lat, lng: lng };

    fetch('/api/send_alert/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify(payload)
    }).then(r => r.json()).then(data => {
      if(data.ok){
        statusEl.textContent = 'Alert sent successfully.';
      } else {
        statusEl.textContent = 'Error: ' + (data.error || 'Unknown error');
      }
    }).catch(err => {
      statusEl.textContent = 'Failed to send alert: ' + err;
    });
  }

  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(pos => {
      const lat = pos.coords.latitude;
      const lng = pos.coords.longitude;
      postPayload(lat, lng);
    }, err => {
      statusEl.textContent = 'Location not available. Sending without location...';
      postPayload(null, null);
    }, { enableHighAccuracy: true, timeout: 10000 });
  } else {
    statusEl.textContent = 'Geolocation not supported. Sending without location...';
    postPayload(null, null);
  }
}

// Attach DOM listeners
document.addEventListener('DOMContentLoaded', function(){
  const sendBtn = document.getElementById('sendBtn');
  if(sendBtn){
    sendBtn.addEventListener('click', function(){
      const userSelect = document.getElementById('userSelect');
      const msgEl = document.getElementById('alertMsg');
      const statusEl = document.getElementById('status');
      const userId = userSelect.value;
      sendAlert(userId, msgEl, statusEl);
    });
  }
});
