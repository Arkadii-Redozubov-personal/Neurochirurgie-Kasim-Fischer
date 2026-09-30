<?php
/**
 * Server-side contact form handler for Neurochirurgie Fischer
 * Sends notification to the clinic (kontakt@my-bandscheibe.de)
 * and an automatic confirmation receipt to the patient.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');

// Only allow POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed']);
    exit;
}

// Support both JSON body and standard Form Data
$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!is_array($data) || empty($data)) {
    $data = $_POST;
}

// Honeypot anti-spam check (if bot filled hidden field)
if (!empty($data['website_url']) || !empty($data['hp_field'])) {
    echo json_encode(['success' => true, 'message' => 'Nachricht gesendet!']);
    exit;
}

// Extract and sanitize fields
$name = isset($data['user_name']) ? trim(strip_tags((string)$data['user_name'])) : '';
$email = isset($data['user_email']) ? trim((string)$data['user_email']) : '';
$standort = isset($data['standort']) ? trim(strip_tags((string)$data['standort'])) : '';
$message = isset($data['message']) ? trim(strip_tags((string)$data['message'])) : '';

// Validation
if (empty($name)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Bitte geben Sie Ihren Namen ein.']);
    exit;
}

if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Bitte geben Sie eine gültige E-Mail-Adresse ein.']);
    exit;
}

if (empty($message)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Bitte geben Sie eine Nachricht ein.']);
    exit;
}

// Clinic recipient
$toClinic = 'kontakt@my-bandscheibe.de';

// Format location name nicely if provided
$locationName = match (strtolower($standort)) {
    'moenchengladbach', 'mönchengladbach' => 'Mönchengladbach (Bismarckstr. 106)',
    'viersen' => 'Viersen (Theodor-Heuss-Platz 10)',
    'duesseldorf', 'düsseldorf' => 'Düsseldorf (Schadowstr. 74)',
    default => !empty($standort) ? htmlspecialchars($standort) : 'Nicht angegeben'
};

$currentDateTime = date('d.m.Y, H:i') . ' Uhr';

// -------------------------------------------------------------
// 1. Email to Clinic
// -------------------------------------------------------------
$clinicSubject = '=?UTF-8?B?' . base64_encode("Neue Kontaktanfrage über my-bandscheibe.de: {$name}") . '?=';

$clinicBody = "Neue Nachricht über das Kontaktformular auf my-bandscheibe.de:

";
$clinicBody .= "Name:     {$name}
";
$clinicBody .= "E-Mail:   {$email}
";
$clinicBody .= "Standort: {$locationName}
";
$clinicBody .= "Datum:    {$currentDateTime}

";
$clinicBody .= "Nachricht:
";
$clinicBody .= "--------------------------------------------------
";
$clinicBody .= "{$message}
";
$clinicBody .= "--------------------------------------------------

";
$clinicBody .= "Hinweis: Sie können direkt auf diese E-Mail antworten, um dem Patienten zu schreiben.
";

$clinicHeaders = [
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    'From: =?UTF-8?B?' . base64_encode('Webseite Neurochirurgie') . '?= <kontakt@my-bandscheibe.de>',
    'Reply-To: ' . $email,
    'X-Mailer: PHP/' . phpversion()
];

@mail($toClinic, $clinicSubject, $clinicBody, implode("
", $clinicHeaders));

// -------------------------------------------------------------
// 2. Auto-reply confirmation to Patient
// -------------------------------------------------------------
$patientSubject = '=?UTF-8?B?' . base64_encode('Ihre Anfrage bei der Praxis für Neurochirurgie Dr. med. Fischer-Rahimov') . '?=';

$patientBody = "Sehr geehrte Damen und Herren,
";
$patientBody .= "vielen Dank für Ihre Kontaktaufnahme.

";
$patientBody .= "Wir haben Ihre Nachricht erfolgreich erhalten und werden Ihr Anliegen schnellstmöglich bearbeiten.

";
$patientBody .= "Zusammenfassung Ihrer Angaben:
";
$patientBody .= "• Name:     {$name}
";
$patientBody .= "• E-Mail:   {$email}
";
if (!empty($standort) && $standort !== 'Nicht angegeben') {
    $patientBody .= "• Standort: {$locationName}
";
}
$patientBody .= "• Datum:    {$currentDateTime}

";
$patientBody .= "Wichtiger Hinweis:
";
$patientBody .= "Dieses Kontaktformular ist nicht für dringende medizinische Notfälle bestimmt.
";
$patientBody .= "In akuten Notfällen wenden Sie sich bitte direkt telefonisch an unsere Praxis oder an den ärztlichen Bereitschaftsdienst unter der bundesweiten Rufnummer 116 117 (ohne Vorwahl).

";
$patientBody .= "Mit freundlichen Grüßen,
";
$patientBody .= "Praxis für Neurochirurgie
";
$patientBody .= "Dr. med. Kasim Fischer-Rahimov & Kollegen

";
$patientBody .= "Standorte:
";
$patientBody .= "• Mönchengladbach: Bismarckstr. 106, 41061 Mönchengladbach | Tel: 02161 678 2683
";
$patientBody .= "• Viersen: Theodor-Heuss-Platz 10, 41747 Viersen | Tel: 02161 678 2683
";
$patientBody .= "• Düsseldorf: Schadowstraße 74, 40212 Düsseldorf | Tel: 02161 678 2683

";
$patientBody .= "E-Mail: kontakt@my-bandscheibe.de
";
$patientBody .= "Internet: https://my-bandscheibe.de
";

$patientHeaders = [
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    'From: =?UTF-8?B?' . base64_encode('Praxis für Neurochirurgie Dr. Fischer-Rahimov') . '?= <kontakt@my-bandscheibe.de>',
    'Reply-To: kontakt@my-bandscheibe.de',
    'X-Mailer: PHP/' . phpversion()
];

@mail($email, $patientSubject, $patientBody, implode("
", $patientHeaders));

echo json_encode([
    'success' => true,
    'message' => 'Ihre Nachricht wurde erfolgreich gesendet!'
]);
