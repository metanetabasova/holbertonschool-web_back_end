# ES6 Basics - JavaScript Yenilikləri və Tapşırıqlar

Bu layihə, JavaScript-in **ES6 (ECMAScript 2015)** versiyası ilə gələn ən vacib yenilikləri, sintaksis dəyişikliklərini və müasir proqramlaşdırma prinsiplərini öyrənmək və tətbiq etmək üçün hazırlanmışdır. Layihə çərçivəsində test mühiti (Jest), kod keyfiyyəti yoxlanışı (ESLint) və yeni sintaksisin köhnə mühitlərdə işləməsi üçün Babel konfiqurasiya edilmişdir.

## 🚀 Layihənin Quraşdırılması (Setup)

Layihəni yerli mühitinizdə işə salmaq üçün aşağıdakı addımları növbə ilə yerinə yetirin:

### 1. Node.js Quraşdırılması (v20.x.x)
Terminalda (Home directory) aşağıdakı komandaları icra edərək Node.js-in 20-ci versiyasını quraşdırın:

```bash
curl -sL [https://deb.nodesource.com/setup_20.x](https://deb.nodesource.com/setup_20.x) -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
