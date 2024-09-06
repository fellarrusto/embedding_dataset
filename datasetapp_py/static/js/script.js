$(document).ready(function() {
    $('#newPageBtn').click(function() {
      $.ajax({
        url: '/random-pdf/',
        type: 'GET',
        success: function(data) {
          const formattedText = data.text.replace(/<br\s*\/?>/gi, "").trim();
          $('#textArea').text(formattedText);
        },
        error: function() {
          alert('Errore nel caricamento del PDF');
        }
      });
    });
  
    $('#submitBtn').click(function() {
      const anchor = $('#domanda').val().trim();
      const positive = $('#risposta').val().trim();
  
      if (!anchor || !positive) {
        alert('Tutti i campi devono essere compilati.');
        return;
      }
  
      $.ajax({
        url: '/submit/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ anchor: anchor, positive: positive }),
        success: function(response) {
          alert('Dati inviati con successo');
        },
        error: function(xhr, status, error) {
          alert('Errore durante l\'invio dei dati: ' + error);
        }
      });    
    });
  });
  