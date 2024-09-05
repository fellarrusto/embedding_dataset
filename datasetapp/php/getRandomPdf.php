<?php
require 'vendor/autoload.php';

use Smalot\PdfParser\Parser;

$files = glob('../pdfs/*.pdf');
$randomFile = $files[array_rand($files)];

$parser = new Parser();
$pdf = $parser->parseFile($randomFile);
$pages = $pdf->getPages();
$randomPage = $pages[array_rand($pages)]->getText();

echo nl2br($randomPage);
?>
