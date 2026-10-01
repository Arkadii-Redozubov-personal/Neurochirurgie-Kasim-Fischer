<?php
/**
 * CMS Auto-Publish Proxy Endpoint
 * Triggers GitHub Actions workflow dispatch securely from the server
 */

header('Content-Type: application/json; charset=utf-8');

// Allow POST requests only
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Nur POST-Anfragen sind erlaubt.']);
    exit;
}

$configFile = __DIR__ . '/publish-config.php';
if (!file_exists($configFile)) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Serverkonfiguration fehlt (publish-config.php nicht gefunden).'
    ]);
    exit;
}

require_once $configFile;

if (!defined('GH_PUBLISH_TOKEN') || empty(GH_PUBLISH_TOKEN)) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'GitHub-Token auf dem Server ist nicht konfiguriert.'
    ]);
    exit;
}

// Trigger GitHub Actions repository_dispatch
$ch = curl_init('https://api.github.com/repos/Arkadii-Redozubov-personal/Neurochirurgie-Kasim-Fischer/dispatches');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . GH_PUBLISH_TOKEN,
        'Accept: application/vnd.github.v3+json',
        'User-Agent: Praxis-Kasim-Fischer-CMS',
        'Content-Type: application/json'
    ],
    CURLOPT_POSTFIELDS => json_encode(['event_type' => 'publish_cms']),
    CURLOPT_TIMEOUT => 20
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($curlError) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Verbindungsfehler: ' . $curlError]);
    exit;
}

// GitHub returns 204 No Content on successful repository_dispatch
if ($httpCode === 204 || ($httpCode >= 200 && $httpCode < 300)) {
    echo json_encode([
        'success' => true,
        'message' => 'Signal gesendet! Die Website wird in ~2 Minuten aktualisiert.'
    ]);
} else {
    http_response_code($httpCode ?: 500);
    echo json_encode([
        'success' => false,
        'error' => 'GitHub API-Antwort (' . $httpCode . '): ' . $response
    ]);
}
