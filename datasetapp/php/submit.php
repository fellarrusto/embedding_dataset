<?php
header('Content-Type: application/json');

try {
    $db = new PDO('mysql:host=mysql_local;dbname=dataset_db', 'user', 'userpassword');

    // Riceve i dati dalla richiesta POST
    $data = json_decode(file_get_contents('php://input'), true);
    $anchor = $data['anchor'];
    $positive = $data['positive'];

    // Preparazione ed esecuzione della query di inserimento
    $query = $db->prepare('INSERT INTO dataset (anchor, positive) VALUES (?, ?)');
    $query->execute([$anchor, $positive]);

    // Restituisce una risposta con stato 200 OK
    http_response_code(200);
    echo json_encode(['message' => 'Dati inseriti con successo']);
} catch (PDOException $e) {
    // Gestione dell'errore e invio di una risposta con stato 500
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
