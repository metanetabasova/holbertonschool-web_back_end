# Node.js Basics

Bu layihə Node.js mühitində təməl anlayışları, fayl sistemi ilə işləməyi, modulları və konfiqurasiya alətlərini (Babel, ESLint) öyrənmək üçün hazırlanmışdır.

## 📋 Struktur və Fayllar

- `database.csv` - Tələbə məlumatlarını özündə saxlayan CSV faylı (ad, soyad, yaş, ixtisas).
- `package.json` - Layihə asılılıqları (dependencies) və script-ləri idarə edən fayl.
- `babel.config.js` - ES6+ sintaksisini cari Node.js versiyasına uyğunlaşdıran Babel konfiqurasiyası.
- `.eslintrc.js` - Kod stili və standartlarını (Airbnb base) yoxlayan ESLint konfiqurasiyası.
- `0-console.js` - STDOUT-a mesaj çıxaran təməl funksiya.
- `0-main.js` - `0-console.js` faylını test etmək üçün icra olunacaq fayl.

## 🚀 Quraşdırılma

Layihəni işə salmazdan əvvəl lazımi paketləri yükləmək üçün terminalda aşağıdakı əmri icra edin:

```bash
npm install

