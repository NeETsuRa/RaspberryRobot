<html>
  <head>
    <title>Raspberry Pi Robot Control</title>
	<link rel="stylesheet" type="text/css" href="css/MainSite.css">
  </head>
  <body>
	  <h1>Diplomska Naloga: Raspberry pi robot</h1>
	  <h2> 	Mentor: doc. dr. Andrej Taranenko <br>
			Kandidat: Nejc Ravnjak
	  </h2>
	  <h3>Dobrodošli na spletni strani Diplomske naloge Nejca Ravnjak. Spletna stran služi za kontrolo Robota.
	  Natancne podatke kako lahko zgradite in sprogramirate svojega robota lahko preberete v diplomski nalogi.</h3>
	  
	  <input type="button" value="Kontrola Robota" onclick="client.html" class="btn btn-primary">
      <input type="button" value="Samostojno delovanje" onclick="FullControll.html" class="btn btn-primary">
      <br><br>
      <input id="shutdown_button" type="button" value="Izklop Robota" onclick="sys_shutdown();" class="btn btn-danger">
      <input id="reboot_button" type="button" value="Ponovni zagon Robota" onclick="sys_reboot();" class="btn btn-danger">
  </body>
</html>
