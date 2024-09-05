<?php
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename="dataset.jsonl"');
header('Pragma: no-cache');
header('Expires: 0');

try {
    // Connessione al database MySQL nel container Docker
    $db = new PDO('mysql:host=mysql;dbname=dataset_db', 'user', 'userpassword');

    // Esegui una query per ottenere tutti i record della tabella
    $query = $db->query('SELECT id, anchor, positive FROM dataset');
    $rows = $query->fetchAll(PDO::FETCH_ASSOC);

    // Crea il file JSONL (una riga per ogni record in formato JSON)
    foreach ($rows as $row) {
        // Codifica ciascun record in formato JSON
        echo json_encode($row) . "\n";
    }
} catch (PDOException $e) {
    // Gestione dell'errore
    echo "Errore durante il recupero dei dati: " . $e->getMessage();
    exit;
}
?>
