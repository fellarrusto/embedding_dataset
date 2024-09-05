$(document).ready(function() {
  // Funzione per caricare una nuova pagina PDF casuale
  $('#newPageBtn').click(function() {
    $.ajax({
      url: 'php/getRandomPdf.php',
      type: 'GET',
      success: function(data) {
        // Rimuovi i tag <br /> e formattalo con ritorni a capo
        const formattedText = data.replace(/<br\s*\/?>/gi, "").trim();
        $('#textArea').text(formattedText);
      },
      error: function() {
        alert('Errore nel caricamento del PDF');
      }
    });
  });

  // Funzione per inviare i dati
  $('#submitBtn').click(function() {
    const anchor = $('#domanda').val().trim();
    const positive = $('#risposta').val().trim();

    // Controllo semplice per evitare invio di dati vuoti
    if (!anchor || !positive) {
      alert('Tutti i campi devono essere compilati.');
      return;
    }

    $.ajax({
      url: 'php/submit.php',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ anchor: anchor, positive: positive }),
      success: function(response) {
        alert('Dati inviati con successo');
        // Resetta i campi dopo l'invio
        $('#domanda').val('');
        $('#risposta').val('');
        $('#textArea').text('Testo della pagina qui...');
      },
      error: function(xhr, status, error) {
        console.log('XHR:', xhr);
        console.log('Status:', status);
        console.log('Error:', error);
        alert('Errore durante l\'invio dei dati: ' + error + '\n' + xhr.responseText);
      }
    });    
  });
});
