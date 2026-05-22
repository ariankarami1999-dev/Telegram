<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/QpzIRx6W7kpfbSUkGfBpe9d8FAl2Zx1zv4ndjG-oQ77b7khfY79b3-oZGHJCl4PtGS_pz3XEW6Xtsp5GL4IPszB5B5XQWesp0AVVZnNoP4AybYabeEVKCr0Eq93PV56raYJh4Uitk5zbwf8iNhygMSIrW_V1QmhczYiox0QOBzsxv45NAqQa9M3f5fjyOrjjTf3U9JWdLGKf6ZLpOJvGkODfNLv2nKKTPyAqkNFu9Br8hgyc1aMyKaiGE9Ft_gMm8m0mbcF7H8BQyWveiOlYd4NZQ2RoTAFL__E6ICO9MTeQLF-Mc5WtUzM2VZvi-Q-DECC0xw_Tilfo5NUa5KIK7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 16:07:16</div>
<hr>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeHsoWlsjBaCxS0Zb9CT2iJcjdHUJaT8WLZMuBPFHbV1XA-GIKypcmIhuEMgPmIPTq0rzIowHna2JtPEt3zG9C9tuQsxy3k6BFmAcwbREUJhhV_NrzJw2-XTwOjr28D5tc971A1tKF-uv7mOdJGUsXtl6jj0xOi6BCCurr5gEOjjh2oy2-LMzDLnxDpHiJRC-HHbBtHFru5R2WWVkm3Uw3e018iC-vH2r7FqJdbk0NW218amFuWbgjo4HpkU-TS_C_WCaNawCoB_7m8H66Zu53oUnPwUMgCl1exIhiprbz8w2KbG3FqiVp5xqMh2X0QTPuFYxNEwnLigKrlwPxWHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDY9fhlzeqbIqjc8bW5cIJ7mU6dfLgpTJDcZNqZWMWImWFVJ6GV0A4Bg0XEA4IXYA8BSR8KKR7IrkqskKaIMtTsvN8eDJMb4TnecWqFymTHXBkNNTyCpEBuVCi2gNd-XNAAcD0MRm2NN05fixJQ7tI-6stDURnNd-CPIaMggOyjv5_1ou1frg4pBuoJU-DNkwG_EORn5kf4TPOQWE195GSlmFrngfOIS2h_gSetnHUXoGNCC2hn8qoNDCLdhPnTUnMIfXGstonoqypvJ59Sfsj538Jrf2JX6oFjwxMzqvbJC_IfUcrEau6ybdVADK3DrC_cVD8rohBhNl1UOwzyORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IgB1tVVnG9iXSKW6QDOsaHHSC7YLROVI4rgM8f55EY2TQNBFW2g_5Xwzg5MlbDZd-l5-nFJylxO965fkA9HKnBNj5TZtEnsjLdg00g6viF1uJ420BPhRGQnNdwgzhkIlOYcY-pbvIsKGZWrvuutxY_wNCbVHphYsrW-5iDFddEGsQ41brZsnxF_pRzT1n7-DYYmWPY3r2D0gX1t8XdS4gCLzaBVFAhYrK0IU-BF17nqGI-DMPVOlmrVrxSXcAR3Omul4bkmXcU1WrCdPauhvrYCFopYE8F6rsG4MBtJ71c7BYtJLmgFd1mV2b7xpH7XewLV6qIWwcHQtgSq2OCkGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IgB1tVVnG9iXSKW6QDOsaHHSC7YLROVI4rgM8f55EY2TQNBFW2g_5Xwzg5MlbDZd-l5-nFJylxO965fkA9HKnBNj5TZtEnsjLdg00g6viF1uJ420BPhRGQnNdwgzhkIlOYcY-pbvIsKGZWrvuutxY_wNCbVHphYsrW-5iDFddEGsQ41brZsnxF_pRzT1n7-DYYmWPY3r2D0gX1t8XdS4gCLzaBVFAhYrK0IU-BF17nqGI-DMPVOlmrVrxSXcAR3Omul4bkmXcU1WrCdPauhvrYCFopYE8F6rsG4MBtJ71c7BYtJLmgFd1mV2b7xpH7XewLV6qIWwcHQtgSq2OCkGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_DSpBnwP3Oes85QVPsMo3KtRfciq14s2uMiU5ZsUF8j_9Q8U6zSuT7rbu9krRrx1K2kR0kf6i_kT_xskdHduQ_6a5U6f_W9JytZxe6WnT57AC8oxpwGYcO2IDp4CRYgHvav46bavNn326zHjZv8TnsCwLLzQRQgJMEPUSq9SpnHByWSfVUybrcDj-h6IdXLVZ1ftYwpJk4_8CmFtwiRzAeEZKAXubMVcUJZRbdZwItR4g--KPKObZS9a_659uXb3cgWI6D73KHB2Xl9hUUuDVtF307I-s5ptYJlgm50ddqCEsI7kx5AzsFAky-WTro7IYDNK4X62YWNrVNnm_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez4sFC-qYN3nZf7--oU6_euP2kZmhUpUBAoYwVFEBBvbd24LJW0A6ctDe5TrgQeQah3oUg4F-hXLyVeT1SZ5LsQTpXaaQaPpA2uBu0C95AkdjV77U3P-L9bp0RCOO2-FbWPIkATw4sj37xsb-auRdhQwFe-lXA73zNxXGb9NI9ueAIYXLWURX3nHUiOOc3XgQHDgOSnBwgTl6Q0BkPZv4nH8-q6lbXgJWx043MEvw0krnLxcO0x4nEdeGqWXZdE5naIUwgRDyjrIFkUAYJGtGeLjyK6YzJ_ENcKTRgwg3duy0Gti0X1kWlHDjpmifoazTY9x0xApmDXhrszH-VTU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej_7Cjz9PU9oY6nkhsgxdwMZbHtLfzs05JTAanIKt1RsCzYa_ElgtLFAXj4SrkMogtbuQXiUxRiwXJo4xIi-LsNZZtkn7fpZtikV7byNhheOxOWg_dravqeaa7JkkJuOl0GUf1ZX-YAWhLtuM5J8pv341yZknJJK93AfSDUsVXvNyI2t_k_3idJc0bXg7UjC8jbeKi1Q07HSVC5ZZEb_pE1TzfnI9MxLRUS-_m0begQQUoA-kdTxvCvSt-LeThqGT6gd_-lsWKBWacYSSgbV69dkojkM9Ckr76XL-Qm4uouNaCNsY-WUFJS5v-VJAIX5L_PV2LONimy9rMngszb9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL_sg6kSG8cEPjr5gEyKUhq5ORFlax7nG5r0I1PQJ0RbtdwNyk3Q4JExnl0ksUhHGaWxgqzklEea3hJolXuKWT1nsDiv5zvJyHJ-LVuMTduI0fxB8ioCYIqNKqUKVdevWZwBAb_7q0xE8tx5k8n4sT7MnZQrdh2ieyFdfdil9aMbpw4YIzrkBuksw0JPfiOxhGdUTS4HnmGPbioVOhnKfaV3Ln5CsSbc0YCZYraEMb1AJlXyC0cncayYnlHPChuCTR3OhXPv_0c4tnOmc2woo4XsoHVe2I8arL7p69k7HQazvlt0FrQfnbfnkwaEL3CTDgp0Qkdkdh1ljnDLGukDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPH3zqNiDzrVSiNWya6T24cFXwSwc3CeLkK2zeWkU_eIlQhwrvDJYfr4mMbEJEM8VJzljH90leNqOf6xpzvSiYeaVL3Kj4RS4CK3Nw4Lm5lQR15EinqKyU4XScYnY04Oah9n9IOFq72evTZsg5CrZVDUUZXG0FKvz9capUNlc7XKpNzMkHu5KyN6KZdpDF_Ju_7UTgL9xCCYtikeixs7JFB0CWAt0JutCXW3OdpIerQcfEGMATfxUZoK98YUIot0-VId3HzWo8M9OY7PhLfTPCQV4oPhCAU-vgu8rVG-BhWyxsAG5e0i32txb3WQnjUra4ZPjX8qV3uBl_09ULzZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrf3fiyXRAJzLYZXB3JlpM-gsJHwvMh8JJY-71coaC4H1TGV7R4ZNtwYfg7YiN1jpRW4YhlBFt6cwatn5nRV5e-t7t1M51EVGGEb605Mm1V9cCGN_GpYSLAgQNlgF-D_atvkPnOwrjHMcVBjTltl7-Or5dp4v-aNGEqNocQ2SsQ_TQtcHWokyhFr-2XYsqEKa7MoPNPSumLIJ9C_uSULcfh-4EB6ef1EcKiD84-SfY2r128Lm2hB9Zeoe_GcU18BVe5luG5vlXDDFJjeesREoBmzQZoqINFwuKHwMUTX1Jw9EUeVFMaKZh3gww_kQddd2kdfNl4JNEU6nPcROOL7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyRX_HzEaNuVSvuqvelCY-Y_RncpqDf5jJjzQHImyo38gbe8nzqYXfLGW5LSJOJ1NY_tnkav3uV__1L8K8I937q_3CWODfxDMpraU-QLMGr5alHlI49FbxZ2bKiDXr5qswUYnWzTok2b5J7gH74TPPy2vBwM-hq65TmQabPBCRjEOSjQVLGu72BPGk0PdtQ5uHVAlO9Wbzko8944Y2m4fuaz7c_aPWNrbt3yyg-bj7fhdWsUopwpETx0Wk9ON211EgVYN0PdlQbq8mARuQnAWC7XAxzRU-e_slIvj2Qh406ZICXBVCTtqINktUiYN7YtnNvLSwBcLykREqaHksh-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5YZO4QWyBmwIx1OBwr6MZYNttEbn3fxR2WMYSfJUm8NWzg7GboVt087ULL5Mqlo7dxFm_2OoF54SOenJyeSY1cQ5HysiPPjrHdHzuzFmDS82yJKIDPwvESJhZ9rgGXTDPff5z91JWWvaz8Y9WJDTJhgr7lMNHhnmy4wWzycYpP9qihkOUGdZbgKXJ0r6-2XLWYkNAECVa63-JwOOQhdhzxkuzZ_MB_DXb7sWk9PUsCZhyt-kiXr7Zmf6T8nEKobgWuVrE76p4G_Z7M32Qcfm6Ek9jqIBq14x8TdtJdzj-vnoVFxXGyLURKnShVmTXGwWdLZyNxVOMgXamAqiqJ9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=uJfi6ye0LGhvBDawl5r1o8VHPnE4Im_2nGHB_NilF81GpeWZyjvVaAyw-uhzMwcEXj193HO52FuunURZWFyyYoxUfwGaMmcDWvlzyu2hymIL0czj1f2bhZHsLRtXBI-lherQ_qOos5CiaKL_Pbb5wboSZuco_S5SwLGcjJ6fb9HSOCwFi2qVCEikVc7gtezy4kiWxSTBc3t6LLPwLqfKolnt_vr0ucj2TTU-LOQYRDVLUcXfHYiDo2FtaT1C0Y4ZYJKTAemSWldyEFyTcRXOdfhrk7cNjX2-9vyYQRta75aVHj_ew0Q4I09Xx9ncOOyA1u9-0YgNhVR4QaVUnFjA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=uJfi6ye0LGhvBDawl5r1o8VHPnE4Im_2nGHB_NilF81GpeWZyjvVaAyw-uhzMwcEXj193HO52FuunURZWFyyYoxUfwGaMmcDWvlzyu2hymIL0czj1f2bhZHsLRtXBI-lherQ_qOos5CiaKL_Pbb5wboSZuco_S5SwLGcjJ6fb9HSOCwFi2qVCEikVc7gtezy4kiWxSTBc3t6LLPwLqfKolnt_vr0ucj2TTU-LOQYRDVLUcXfHYiDo2FtaT1C0Y4ZYJKTAemSWldyEFyTcRXOdfhrk7cNjX2-9vyYQRta75aVHj_ew0Q4I09Xx9ncOOyA1u9-0YgNhVR4QaVUnFjA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=cGz3Yx-cVT5Qa7iJbmCRU5nZxxoyHyjqYTbCgzNYz9mvuA5EePqizfxnlwXZWwPSFg-iOocQdI2y15lHF_79l9xJ8e3iuA4X-aBM_TVicq3VNFrJqSR4uUc7C1i3LnZHVWhFTX2ijD1_Cy98sqxUjv80Kbk26axjg3jsPCZXeNQ5OBu_PjYqC5gHDvDmEd9jrzo2Y0SCbJoZctYfu9HDLqIHzcrs7Or1XK7bYaeY3vD0wDa5DmjY9wxaF8jyG53mR-TcD8xql05e32vCR8GSU6D44aq2o46AiIFREpWe6bis4lsofXdLAWBL7J1cDKQlb75AfJuRWmlyYUGqxccGWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=cGz3Yx-cVT5Qa7iJbmCRU5nZxxoyHyjqYTbCgzNYz9mvuA5EePqizfxnlwXZWwPSFg-iOocQdI2y15lHF_79l9xJ8e3iuA4X-aBM_TVicq3VNFrJqSR4uUc7C1i3LnZHVWhFTX2ijD1_Cy98sqxUjv80Kbk26axjg3jsPCZXeNQ5OBu_PjYqC5gHDvDmEd9jrzo2Y0SCbJoZctYfu9HDLqIHzcrs7Or1XK7bYaeY3vD0wDa5DmjY9wxaF8jyG53mR-TcD8xql05e32vCR8GSU6D44aq2o46AiIFREpWe6bis4lsofXdLAWBL7J1cDKQlb75AfJuRWmlyYUGqxccGWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=swvfdt6ZPWBoyvG2ApOBZ2k7fj7AbfkvE1ygMzOeAc2CDPr23SoAVgQhxeqhUpWKH1r5Zes5GdfLHuHTmsxGQaYXO229gdh_GJKtSMX_Ult_066iVgzMGkK_hK3faC0bSbOW8P0TRWPmF097Zyzmf4F____YvrkJjrsi2f78f8CRBk1Fk9riu8rjL1Aoa3lZ9RiUrqtFXKQHNcM4Uxl6TAJ6UcoW2U_iIwnsYagFE9QEVyWW1jyYIbbdb6T1U0x_n1W7EyTn7RMUHKGonV30Rhsa3bSv3oViFGHueQdjOdaAXREfWi_cT5ALNOPFV_quWZh9zAUi4iSYlK1z2TYAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=swvfdt6ZPWBoyvG2ApOBZ2k7fj7AbfkvE1ygMzOeAc2CDPr23SoAVgQhxeqhUpWKH1r5Zes5GdfLHuHTmsxGQaYXO229gdh_GJKtSMX_Ult_066iVgzMGkK_hK3faC0bSbOW8P0TRWPmF097Zyzmf4F____YvrkJjrsi2f78f8CRBk1Fk9riu8rjL1Aoa3lZ9RiUrqtFXKQHNcM4Uxl6TAJ6UcoW2U_iIwnsYagFE9QEVyWW1jyYIbbdb6T1U0x_n1W7EyTn7RMUHKGonV30Rhsa3bSv3oViFGHueQdjOdaAXREfWi_cT5ALNOPFV_quWZh9zAUi4iSYlK1z2TYAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvfgVSYa4RiOncI3q6_vye3N1CCWXysNQchoXlpAuDRy-7VFJ9pb3lFGgyIgwME4edXWAppFaue1maGDGFvqwUOGVr8unhsGz16MtFTiNwS9VQop6qf_OKpvsciDqvri1j2dE-g0xQa6VvzIjjwjcwyn0mqcbc0trfKlNx9JubyDbs0YNMgVOXznOiINdI0vlJlUVJEgroz71UjALEPqSU2GUt43XdfWExBXoxTXMs2ZC7pIqJl_udf_FDSPJTjo2KYpm6W35a_VqPjX0uuPAc3vPk-6Lzp5XM3Jw2FBTopuYqOfdE1n6V-h2l5_UFPaG6kJV7ueJ_ArCart4eJ-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=IUiLrcxb1LHUWHOZLoLUUHbWR3ve66ZmDWBY6KjjOH85jJSNVH89r7PfpOf6APcGt8uPkMFfp4yNBrUFY8IV2CxzVB53hTdGFkSwttY64HAGIMyyWVUzo9enzZICrochz-Xb9vlZoH0b4WbhA9VC72L4UGfhyeG-8E6wXSmMoS8Ovz7NNdvgHPRAbbU1xds8h3vMhHhOKLilnYd-SqRAa4jz5-RqjckMRf9M5OhYlvtay4talEAdlfuqf63G0ncDihqxNV1YsBJqnDc4MxXTjCYT8-XA2KVi7MGmfapuKGpl2su4fgKJmxZ2vRtxnynrFPDW59LlN6enlyZxqoSVkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=IUiLrcxb1LHUWHOZLoLUUHbWR3ve66ZmDWBY6KjjOH85jJSNVH89r7PfpOf6APcGt8uPkMFfp4yNBrUFY8IV2CxzVB53hTdGFkSwttY64HAGIMyyWVUzo9enzZICrochz-Xb9vlZoH0b4WbhA9VC72L4UGfhyeG-8E6wXSmMoS8Ovz7NNdvgHPRAbbU1xds8h3vMhHhOKLilnYd-SqRAa4jz5-RqjckMRf9M5OhYlvtay4talEAdlfuqf63G0ncDihqxNV1YsBJqnDc4MxXTjCYT8-XA2KVi7MGmfapuKGpl2su4fgKJmxZ2vRtxnynrFPDW59LlN6enlyZxqoSVkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=uCZgiCqbbCLCFquSwHqkk1vEj-DNYUMpseH1kojhmn-aA54hMmnY0WBcCx_bUy9jyH4qvLA_86bQ5Po0ote_1k6BleiJvZGGrm_PiSgS2VNUbAWR6mtz-AQePhSrdKgmxhYPhh7mbOtizbLiz6yAeX7QwysEPXO6YeLkt9smlA6_OkwJY8hJSH4lgNyLsouHXT49q6KWI6DUbJe2H-oKu7xg-dlBdztmyk1tEf99RF1x0vQYz5bWNmKU_7w72tOT3ccubbtocSBTDZ64MWbvmNV16tK8SLhfdfCad8X5ACAGiBN3rup-OWWeKunXyyOETSDtefhrweEcOb6TKmMrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=uCZgiCqbbCLCFquSwHqkk1vEj-DNYUMpseH1kojhmn-aA54hMmnY0WBcCx_bUy9jyH4qvLA_86bQ5Po0ote_1k6BleiJvZGGrm_PiSgS2VNUbAWR6mtz-AQePhSrdKgmxhYPhh7mbOtizbLiz6yAeX7QwysEPXO6YeLkt9smlA6_OkwJY8hJSH4lgNyLsouHXT49q6KWI6DUbJe2H-oKu7xg-dlBdztmyk1tEf99RF1x0vQYz5bWNmKU_7w72tOT3ccubbtocSBTDZ64MWbvmNV16tK8SLhfdfCad8X5ACAGiBN3rup-OWWeKunXyyOETSDtefhrweEcOb6TKmMrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdO-yK9iD8JWb9aY2Rvs1tKK1QpXbpoFBn9AVJoq5qfeTqvql6x02inQJ9nBW88Gd9INR_vSZITiZQy2Iepif_Rgj-jgCybasdbvdK7O8GEpWzrd-XBdFQIWfWw0P8tEwNjZ4CI7ZH_q7vVZ-mfMaGjEodjTztEaiGy4Hs6RoB8GcnZNZsIzHaoBWg05AVtk7P6r56rb71xZJDtCcrwzfK7da2ZthrHJnbklsq_1dCWtSZxnX_fz-MMqLKBJZ4LEppefDY1s8R9S6lOg2oLVq68CUdmKGfq7Pgu4y56VHni1ION6sBPxDH2NtoIhnmVUJc2k-M7-t9_XzEXChQnwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU6F3HM96iqWY6xsWRzRB_Yw2Gp_tzexNx6yI-gybRactYozbgx69kpSdlC2B1f1X5eli04K3fYQaXORGsUz4e7lhz18-ZwIQemYCSc_vbl8B7j9lCW4UZNk03j3eDToPKmDcZpcmbV1N_o_tLAUDsISv23D3B4plkpPxpdFUBXbfr5fLibLDgoFbJq4JTyQIZKAbYoTMAt9HehUBIeT4Ga1eDjMGC9hrSY83SxN_tefxN_AcbA5bxMbRDK5pLW_Hp_pPegNGJ_1Xoi_tZCnCTrX_bKcCtw6YItuvI-0OY_POo-ctgOCh2SSX6iAWuf1fplqr_qTbE7LNfteIwHVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRI305oqTefUXpnpeNxPfz4WUwQio_p7fZel50RYUpj3qmX_ko5qBXBb0eNNI1c85ihLv4fUhMBp3vkn6p1d-joYfsY7zGjWwtTa04yOwllZkNwnT9hDrJV1FTqGe6B1CEMPMSetZzFkePhS_iIvi8xUHpXC28z2o3I0qdpYPEzF6_gdGgRqQCl0eSZCbwtTZoViHN3l2kXYEhfvYH_WFNjS9AIuO6oWbAVRse2o-9xBKXpderRWVh-Cwz-ofHdXTSkprOHw2eqYcWTxTbWrGGNdTAX66wBhd7WlYywPRB-m88cCFxyoKJPteWcm7mi8cOSQ2MpscQMz5QST-TUbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrRqoWOxn9LSTnN6Zyvzo9HlP2wIuZv9qt6MeZ2q4MmdW7vP787oFO4K_URUFq_D6T2RF2RASL9pFa5Ldl9vnHgGDqPkCCDW5w4G3GvXx5duq5dESSLkrWabOq_zHwpKidVu_1-e7SMyZHWLcLQEaHXbygJsrL-CcF1iy33cr8EzG9x3nrt1XFmM8wbTuGpHxCZqA4n1Gwg04X_Sp2lcUhOS2okJwSu77opRrw7ZnURBLrEC7Cecc35e6uCDsyKe4px0wMeeAPStn3__E4Wt3fOxdJx4911c6qBFuMOH6i43actXEFrGIPjQzMb0o03kmlqtt16mWAuXIiZwOkGb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hN0pR1jOEBJwaurQs6dWBEh6g_01fYJbijsiAScgHx5PMC4lAn-mOv0GyLS5gbG8OVSologLP1v5ll1QQbfOD9aRPyYNLZAoWFS3i6ofupJ2xp61UkrGIlnfJClXmxNDj3X5muCaWcR1v2X1ldlDAVeOXOtTG8hdtQ5SJfBd6Iu7T1s23JtmPRWFPPEy92kCQIiKVN2lAXG_62DLFqZg1tprUABHXcAETqOEEIaxf3zKH_6dwr1ar30tL4-yqm4AhqttpfY8jMXGlMmaDEjGMFhKjRJxY6uC_WdEu0JubUsD9X3Xwma9XSjLsfIgCaWVJUeprruN2hM52Bzz0ztJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SR7JUe8AoUMzH6MGPl5oa1b0pbLeSWIjc3NA7y4NDu4vY3Vxa76dz-DJfRIaMsLG1epIluh3ne4BkpK-sySzPZX3Z_g0c66qFcww3KhUkgwCq35aE4t7EZCDw_kd4pDXWhE2qeQt1VsKhiHAKibnt7wOSR2LoVi9GAbRe-Nocbdluenn_l7909ouxrqCuNM9SwNW51JR6xfvB9WR8o81R2KBkDb2Dz0qDmY0cUJp_xqxpugTdjPrndLwANmlVQOQjq1hrEfh1-hRyX3ZpIuMlPNfUBX1wKYeugP9bbmRrpxPvbYhYiNNZEJ4ZzMXfoNu96myOFQ1ule_86Uagc0fUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/es0WHjw7KVOwLS6bBgb3SeKm9j8hwP172T4IkKoDoB_CFBo_UQQ3g6a4W0HXRTWZGIGFJ8cMZsrEkFKKNytsn8kbdfQ6FHF5omI7_bI7IVNN2I1itUJperyixA4WZ_YH19l-Sh-Na_cSIdAVDJYDBkvcvkP2_rmXjvG9Ra59s_JQB5MJTdmdtjD_q324M-dQNB9h3vM-orwWb9IWO26VYbDWUszpsOEVu1ngZFsKT46fUEhdANAuwZWq4_IbqMITKe9kXUoQ7CRwEk0IK_-L6qykIiGOwK3tjBGqggBgfqLAfD6iz0YUOPfjbpVO0Uk2d02YHcwtAr1A1fvinkkV-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=KpQ-YUpWl4x56m__UerCFhTheodQFOlaBbUrvmkF9cWMyCsOvQF-zIGL6zV0yBoaO3jku_XvmNqZpRbWGY_9o_smgFGZMplzJ25pWKcuVrUKjhA6RCFGUeNQz9e5sSJVawK8E3-TyHBwpYSxDF3UgqrCctg8GG-2GFnSNUkjTzuGw7TwE30ffy_tHChuOOn02oY39wr5fs_MNDhZrMBkOXS83_21xzpSLie9W1TvJJXGXJMa1NCRfI8l1iUmBRNr2RMV2SXKg5boqbBpfhzuq-dJ49RpcmA01Rke2Wo8FtwIQF9MxwLYzgTTF41wEoos81egAVL_C9y8TEfk8TTWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=KpQ-YUpWl4x56m__UerCFhTheodQFOlaBbUrvmkF9cWMyCsOvQF-zIGL6zV0yBoaO3jku_XvmNqZpRbWGY_9o_smgFGZMplzJ25pWKcuVrUKjhA6RCFGUeNQz9e5sSJVawK8E3-TyHBwpYSxDF3UgqrCctg8GG-2GFnSNUkjTzuGw7TwE30ffy_tHChuOOn02oY39wr5fs_MNDhZrMBkOXS83_21xzpSLie9W1TvJJXGXJMa1NCRfI8l1iUmBRNr2RMV2SXKg5boqbBpfhzuq-dJ49RpcmA01Rke2Wo8FtwIQF9MxwLYzgTTF41wEoos81egAVL_C9y8TEfk8TTWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3NRX66bajE2A6sCjNzEB1YJxtYIjxLyWreqZfb00LkLZZvykBkq2R6fLz1aT4x8eQ3hsmLbjYLWiazHx4YrDy7ToLdc7K-bc_xtpM-KwVHfgK098JtwFKfabONBpGFluDYpJrBYevmRWhNbTyoQXYmTdgtcJV5p-IWwkNiTQ4A7ttqk1qArQJW19obYHfs5T77qKE0zzobjjbycB2M-lndmA31DvHT6G7DnjMyH_NMf4FfaBAgT6oA19PXTBF-lqjXVehFpkUZ15l5_e5U6IzIjhIFSFrhmucLPiutOkE4X1ZJS-LCcq5i_y-mCc9AbaOJo2Wks2l0ZCoV_f64loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIKsECol1r5_YJdCP1qz3FgIDy2RuFLVnd5bFhtD5hurGTROYiPXaZgFrq1MKfGO-LlEgF-vLBGE0tOI1Eyphf8AtQY-eIHZvQZblE9pUHfEuVPQ3Bo6Lvnmbpc_6bGFVQlrKcjad3MRGhEkU0-89YB0Up1PM47mNaNGceXcUHMQmN8kcPWEqnD7LSicj9rMXknjM9sxi2yieySDIpiQ67Uc13z6JHw8frMQHU6X4L3j5CgI0l5f06gjhmaaN4yHjsKylTI6fiuiqP7Iqjvdc5cZC5MfJ_dRU2mCSJMqtvIhY4XcBfRUuxQeGTe_qR5TycGRM1ULiSozXoAQccxecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwMXFcBl0b9GvOEYIuSrFENWq_HCOvL5pRCEKBy6IzAP_1MZEF7uvJwYiV-WK6_B3SV044hHXWIa_NeLsfaYk3YnuK3TjoQ6dS8G5a8J9VcA9Xt8PY14IJUBGc2J_KhDPl1FM-yMD6X3T-GLLpFzWqHMgFzXNBL9k72saFRmdQbTlk7CLwXwFkBGAWHDH5JGML9kYPwT4DNOJXkKPPUfRAOeqmCgJcKEhfXt6Vdi8qTmpx3XOLFzQOr621JB4bFfDbqJp72ZwHSsjUhmbroGu7XEyPXguO9PkKy_EZk9k2DmxlBe_YVDyeHhw_NuKafYbXiMcku2P2MER0JIxnMwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjwD7ojd8h3mGEsSQjsPnS0VHCVhK46_6TNgvTh6RdGU5IKHG3diWXdvw4Vokfz2vhN20zar3Yz2029VU9JXcjFDGeBxkpzVrK1So-b1cRAYqyzQtme5njKI5aU_G7x5R52pODQ7VKJTfws34ciOUgloq5iaEuQDkkX57AL8RrYAiDhVDEWHHzna0I0xhiWaMelCCynx2N5PQaPywRf7zRXp9Q-TG7SyB5iZupJrRqqyNH_gguoFvFvBvz8WJwrtaf416sDGA3Xr-LPEUqJiL19H9UFcP9VtiPrRr7ciNwTxJ2mroSN2qr4yaPshKnomftnDGE9z4dYi_ijYAUyHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=K1IgzQD1ONPNxbSZznf4EVUb5czV7spuCz05LDzomhFixeXi7xhmRSM6TAQAuhoPmhQ1LLt9xMq5flyl-z9yZp0-f1nRX-9UY7sIU3Sun5HLwk1-2BlO1AYo2logN48QlM3dcY8rh7G19s55MOYu8Co5YTS913T34UJyRKs7cQUJk8NfnaMGX0ZthBsmm3wOxI4UeQmYVMaZTl0zoVjmXDx12ua-pYNiTdJSxQIT_NZ7Qk1rT04j2MhXuwF--OTunvcYKOTSZSLR-yc2rVm2Kjf6-cYaShTJUIkNDFQx2aj6ETiILvUxc9ZXpDX7CbqLnthUzc5824L3Ckafe7YYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=K1IgzQD1ONPNxbSZznf4EVUb5czV7spuCz05LDzomhFixeXi7xhmRSM6TAQAuhoPmhQ1LLt9xMq5flyl-z9yZp0-f1nRX-9UY7sIU3Sun5HLwk1-2BlO1AYo2logN48QlM3dcY8rh7G19s55MOYu8Co5YTS913T34UJyRKs7cQUJk8NfnaMGX0ZthBsmm3wOxI4UeQmYVMaZTl0zoVjmXDx12ua-pYNiTdJSxQIT_NZ7Qk1rT04j2MhXuwF--OTunvcYKOTSZSLR-yc2rVm2Kjf6-cYaShTJUIkNDFQx2aj6ETiILvUxc9ZXpDX7CbqLnthUzc5824L3Ckafe7YYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFSV7OsOzX8O2azn2H9UCmFXdz7nZC_eF-odxV24Ono05QKxB-jjQ0PziQFkCuuxxfsjsC9fmUP2xDWBkmyz_VQIq2bIYkRYZEeOHHG8mPjAbHftgCdSt5CN_qT-DnWrfqcT4dDEZKuag1klRimhVap78g3hVes4j0Ps-reeYohNJcxQp48D2JeLh52DhbIu3bDv3GsniRd7iFgZh5Mxc07r5ek8P0jLDWsimagHw1bFWWOTDdgMdTmZYuNyVY--naWIgh8bIH6bh18S5lDUsb2RmwOhYWtMWJwHsHDusQZUWZ4sN007FdM0O-621gQsyVdgvNiJrS7vD6YVtWKKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTDXcTCHr1_8Uz4nCkh78U45wW3A_vqa6aoOjjle81NwPdRXNoxEXIkyqTtIZZ9VIEQH71Lg7MFwjCSEzwfgG5WljDdXttkeL2kzo3YJP5GlMwgQSSPT6l8-FcAWq9ajd7QDB5gORd6jSZHkB4IpnIfeK12WqRX89s2Cn2BrWuXmc5Z0n5MddCi8dsDsGRe_pAVz7PLQ_OX1ecAlnQEtXA8x5SCi732sUfor31dXbQDeISR5SZipNvw4h5y76xIyddjG1ly5gPxqSdDfAbGjwnyQPsPGW68yrZnFzeIaPEmvE0VxotCe8tJmj6ltR-9sIhWTGQy-Fedz4rL3P38Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWBKS_hXObLpOIxDSMGnSToDankFAzrGJOwb8HtAVHBl7rInFRAzV4BG-5cEYtf8r_kt5_-YKJ88X2e9SVRuppqfc8Qd_-bVyiUJcF2kXjOswU12ZngYPHr0Vse7PXCUCa_UuSYPztIKQQS908M0l8UVrI1T9iajLImU5KO23IHvA89WlrIRUCZ_X7CuzGcYvVltihdcC82vv9cLoeNsscsTwGomIyyZtLgBw85bsA0XVJZ4U9-rZoiLOT2Hth7vroetwNa4Hzku_fKr4RT_dXvH7Y8vslj-lJnoz50zzgKG_aYiEy9GP7OVtUnvk65d4WBG-ntK_ycsbnqqXthaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5zT7QXT7cK-VWpBcyKe2MHKsS5DNa0Kp4Z7cflUSKdllzawdLJZw20SMHbeXEkw6AZV4GDDAijBl_ESLYeGqVqd_MZn24sKKc7H6-FgmA2jYdkZ7hPu_pASA8fF7nG1YXA1snLKU5qbpZs8Xqou53a--EEOH042yxXD00wf7qlr3X3FnzlTmvXpZuw8yOL--_WNqp7L9VHhWh2kDf0r_aAtWh5oU0y3spNGk0yc8ws4i01GN6EKh1XCCxffhcgwiSFM7-g07uhGgeusQo7KVKhfG3L1vSgEKNin_DizOnNyZMAo1cBPnDhQsVEAVngMwcbMkjqflh2QpbSW4N-fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1fBDYSAAHQWADjuqTqphgcEVtw29A7vSmPs13ZiHwqcw5-qhyTi7DESQJiyZ-pmu_na5AMJjwDXGfFUQzSOgshQuUp2CrE1qIhX83H2YXFhwzu45-40kwqBj_K2RvgWFlVnNu7unbm5pLntPrC7lJ1cikfzJmIIa2Nt1CCAL8A3yXEGwQFKa123D5mknKf2RC3-idPhxDTM-p_hJLf1mKJf3DAeZeXBczqUwCo9-AISoVIiABOPkAzRPTaxD10QWbEQhaAAGkLps5xM155DlL1CaWrxmuJ1ChcuZYnJ-l5VrPm4-sd9u5xuG4lAL052s2oOdx8jPxgUa8YIMC2CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=F6hgPJO4K49IH3Akyp1nC8sRsfs-bXI9DtdIsjjPsWC27eWRNhHwZhq8EuO6pBGscs2IJO6fHFD4XIJybx20MtHPwt2fc-s15evhhaOkLhcf2IWnIqj_Py1YLT6bd7XzEyy92mXduUCIaGVDANlJSAmjbiIi-wB1WMo11IM3YFK1uAwyGFkLgZf4Ar01NtfhGYmFYy2sD9SDLch56uJEjllGDTCrdYqKA-9Rk19fo8uCHCLs3pE5mwj3_aTBfEHySgwOAKhT-BYXSAEy6USvyrSuS6H1alox-Bmbd9A5xLuD5oO-8UjZfudIYbCuimgX73HEmjjhERTdQfCtS2scNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=F6hgPJO4K49IH3Akyp1nC8sRsfs-bXI9DtdIsjjPsWC27eWRNhHwZhq8EuO6pBGscs2IJO6fHFD4XIJybx20MtHPwt2fc-s15evhhaOkLhcf2IWnIqj_Py1YLT6bd7XzEyy92mXduUCIaGVDANlJSAmjbiIi-wB1WMo11IM3YFK1uAwyGFkLgZf4Ar01NtfhGYmFYy2sD9SDLch56uJEjllGDTCrdYqKA-9Rk19fo8uCHCLs3pE5mwj3_aTBfEHySgwOAKhT-BYXSAEy6USvyrSuS6H1alox-Bmbd9A5xLuD5oO-8UjZfudIYbCuimgX73HEmjjhERTdQfCtS2scNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=jQCvTyqyo3pTmEfRqqfDLEQ0mBse-fuk5m-JUoqY5zZ7SbE6Xp2vJCh8mScrxUh1Jq4FqzcRKYP3uXWZrFyIr7WQKGHVrVraZaviFQw6KVIz-kbC9UYmSRiX3zUjiL8Oc_sAvXwro87uVf8D7UmAtK3H-aa9ipThS3tgYK2X6YhaOCILv_DrXdY9E_b7vryr6D3Tm8FRXp_eKpfR6iH5mJRynZ94Oca98W6gUp5c9MIAfWpEiYG4C-fE8_Cc9ZZcd-ieRri1BdWryVopf3Hp0FNcgE2XyMGT9LQ-BTU5l1aCSf515sbeOD01PVDCBdIupx2-3jURZotShmiIs4IPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=jQCvTyqyo3pTmEfRqqfDLEQ0mBse-fuk5m-JUoqY5zZ7SbE6Xp2vJCh8mScrxUh1Jq4FqzcRKYP3uXWZrFyIr7WQKGHVrVraZaviFQw6KVIz-kbC9UYmSRiX3zUjiL8Oc_sAvXwro87uVf8D7UmAtK3H-aa9ipThS3tgYK2X6YhaOCILv_DrXdY9E_b7vryr6D3Tm8FRXp_eKpfR6iH5mJRynZ94Oca98W6gUp5c9MIAfWpEiYG4C-fE8_Cc9ZZcd-ieRri1BdWryVopf3Hp0FNcgE2XyMGT9LQ-BTU5l1aCSf515sbeOD01PVDCBdIupx2-3jURZotShmiIs4IPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDgKWsInlfxmb6Ptvx5hr77Hy7rRn0yRMCXdlAaYm4HDfRCL3JB05iX9fc92M-7BET02mU6T9NmOMs7LusyjOwftAsOIs7bz8Hauj9O9no8EoSqFMPxiek5920TN7Qoak93XFeNYhzvpHEF-w4lKEGgos39DS59aJIlEXqBxgxmkgfzXObkDqFitj_min4IUy6PC3kZE21xVPjqsnOq4Gi1Cr4uYdATxSQmOjCtoGhk-RnQnjbEatDXMrOsNff3x7k7eVdtN9_08Gr3hYexKOOMEyCrxj_FawW8R6FPi_k6306I2xN8UKB-4h1DZQYv8fD0ZUTSFt8cgxmiEWCuv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDw34xPWqpKBUOoD8uvtuN4v7ADkphUEz_6c1mRL4YHexRk4jkMV5YeSU5sNhP7hi8GcPmiPXZ2GhA6wlsPS7fsO_Wu4B2Z71RxWdLhE6m3J4qahnQEiG9lgKNY5BcNKwATdVMRiaZw16IpkZ1OMA2zr8icjPbw_chedTgirzH1B2rXPFSH1LhdvGLjuzgDy0IwFVFPfWo6MLHtPacP3GhHhFgsrGoO2n1u0jkIn3hqCQda1JbqrPTmJmbiaETEA6Rx8By7YEAEB4S9nZSwSg4MJHKazEYnEOivZjsZqZbZhItBBPsUuqEOKW1yLZp2YYPEom44iPeFsl4inkYteLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRcJzX4iP0nWCjSnihEA8l4-wYxOK06mUthl10kz5Xz54SMM132TCRiTw37ZuK-p1J8hwOjI4ZKx7C-iWMoUqwxW9FHIvwkhabB3KH_jYUm8EDkAySSdLjyu5Cgi86TKlzsnydoducnfHcBy5VB-1Jr5baVrTdWyF7Ag0AgseLaC3WTvJeuaLrUN1mQx6pwbe1e_e5DQnoPAQ8yw-aUdcJraKp4LjRskC-aHxCdDx7nB33pctPx4aD42SKV7k03DOucBEZQsWtxyS9YJ_NEE2Y_2hIKo8hCRpcIUHLT8Iku5Pfaiv2y-9Am-74ist-5zMw0_W60cL3W-6dMUD8tosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHouGgcvglJ9x9pqvfGI6rNTu_Z6FOZUgLF0aXQgHUo8eRXQeb26-ZzejigKQXE1L9GK48LRDEJnHcFB2kpA_955bk8Ztlknm7wYIi10wjRWSReu6Nee_ZKlwV7Z6MMcyqJfbNBOh4gc7Qo5bOiH0rRwRLNmpnJHCEtFgrM4LcGG1Ofjejv2nfdk2y5DOPXo6cGNVPfCM2-kux3RU1cAMvPrEOOhBJaY1FoYos0kHITyxjFIgaU7f5T6FT5DoRSvLn4PwF_mECzxta5h9yuiJ4WE0UtwORLFwrnVXry6FlVSUrY5SXjiEj5XzkRm1O_w8SU19FiO5wAe3kS4A93mHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=jRkJdIkqow0k8AZ5Ap826ncUgZ4wWtwsYJL5lJOFJqy3tTzGwJrKXtVuVi8cZTmWiRXgB106qeI7lG9oTo8wU3j3peRT6QyWY5eCyha4zwMnBYVe7m5Vpit3ZfkPsrvwkg1aIkbKTb05C0tSu0YqcRO4lm-a1zadsfmKTxCB8NyRt24ZJSziriR5al8qqVyUWH622eap6gJ1bA8rkHZdg4iVHKpKDXoxo2MCaFxCDRggBBkwPFmO2YRydfHcld4yQDjzDE4tjhQnqhmNk-jEvuBF5uoKMvSKnLaPRi7cYq-OuxoUntLHFoIxpNszEeSNNbdZi62TSpnrFiaUTnuQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=jRkJdIkqow0k8AZ5Ap826ncUgZ4wWtwsYJL5lJOFJqy3tTzGwJrKXtVuVi8cZTmWiRXgB106qeI7lG9oTo8wU3j3peRT6QyWY5eCyha4zwMnBYVe7m5Vpit3ZfkPsrvwkg1aIkbKTb05C0tSu0YqcRO4lm-a1zadsfmKTxCB8NyRt24ZJSziriR5al8qqVyUWH622eap6gJ1bA8rkHZdg4iVHKpKDXoxo2MCaFxCDRggBBkwPFmO2YRydfHcld4yQDjzDE4tjhQnqhmNk-jEvuBF5uoKMvSKnLaPRi7cYq-OuxoUntLHFoIxpNszEeSNNbdZi62TSpnrFiaUTnuQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=fZpN1J-8wppKK88hn-O8mh90quZogA2Qqn5ZPt34cFV1xG1urZmzk3MYGVYoppQPdhGq9amiqjqgj-Z_nM8cAbALmFXVIUVhMcifvCz7lgKI30MYS6GMuHYBbcLLkYYwXFS2Bzjjh3XK5BOF8KpUcQObKT5VIqjQrR2qSvn6pts-FzpOyn2lp7Uno037dN-cniAx_Htuao7fCHfCe1MKwYD4XxUT1zYICNplX-sbzTV4KisqYC62jMSGghRa_y3bDGLtoXPev5lwfXKQ7mpQELwvavJ6OkCk7yLpOvoPxrYAdiLwIJMliULu7XCuQcu2VsPppyyme7nb17GxTJlE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=fZpN1J-8wppKK88hn-O8mh90quZogA2Qqn5ZPt34cFV1xG1urZmzk3MYGVYoppQPdhGq9amiqjqgj-Z_nM8cAbALmFXVIUVhMcifvCz7lgKI30MYS6GMuHYBbcLLkYYwXFS2Bzjjh3XK5BOF8KpUcQObKT5VIqjQrR2qSvn6pts-FzpOyn2lp7Uno037dN-cniAx_Htuao7fCHfCe1MKwYD4XxUT1zYICNplX-sbzTV4KisqYC62jMSGghRa_y3bDGLtoXPev5lwfXKQ7mpQELwvavJ6OkCk7yLpOvoPxrYAdiLwIJMliULu7XCuQcu2VsPppyyme7nb17GxTJlE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI3n-a8XSJc_peLAq44LwBfN62RBZYVX38v5h11xx5sNfdiV3gQ9x1NOXV_xE6dE6U1Llidhm4_Dq6bJgQisvpY-CaQR_B69Fb_jtXYFjtAV2dkydq5foDzxo9KKYb9Mfq85FdOPeOtfmZJ-zo76gRG3M8WN1rKcDVGh8CujnimWTNHV5C6_jKIUO_VafNZE6jvvbB53VLVhXd0XHaPZLlrpD55hNXY_bAKl1a3vhgSq6nIjPDRB_i306W7CiRWPM3jk-tjXkgr0h4yb7AwylyMVE4810RKwU6FwUqtFpaoPua6wDMsVP-0NyX2Sa95uecHKo8eeoTQwCzIgf1Yq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnMCdMLfsThGQXufX-atUedrwAoedmUXuph0Roh__gDlFhx0HaB-mZAOTlxcz4I0sWJX-b03BywXWKlTAFVfijIVnGezZYpN29XtW7pgMpsw5YFpzKpVWydrjR4AZ9rWoIKhbfUGDf2E7aWVaRlFZMtowe7yjm5MSifn7tbvZOF-MBPs_DZS9x8NMm82-JBanvg1-bHcaXOgmQRAWBNG5njrNuJB2Z3VyhmsPhUZzs8mWrkMw6Ysq_pTH3TQWNRf6roYpInRT4AjRYimzSEmbQ6_NIKUKUt4bwsHqsmMbQRF-IDV6SJ5fiiMNLE42BM2E0X2XCw4kCprGENVVn7xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ZbrGt-BAIoZv_ZscrIcg1Ap-XdhJMD228ko4-ZBtTO25c53E6KEoi_r5D_Qbv_8cIjkY9M5aAEO9Fbqole_kmZ5Dww_fz-T-jJInEhZjQEOZNjWNWgncdb6HhKkZGW2JZodJ4YQvEvdlt4e3MlElxnJQfieUmd-BpI2KObqIWvviQ8RYO_O0vHrxwD4jkB-FRLKw5i4hufZZ-I9VyH-suvRnGk0iaqEwsU6B52WSwqJsH6VQ4u3G3yC-SY2mSsWQA_k63Otnp093LiXPrhocVPhU_XpE2qlk-Dv6re4r82jws4frbpFf8W5RxX65JrSJxgvA1y87Lvtpnz5F-oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSlKKUMFcwpJlSsjgdKtQ4S21DSMasRD6QvBL5yoTx1eM8-X9E2mNLSmrYU3F7T0IJBH9j51EhB8b93y7QjQVAnXQ74nLtzLg2JR96jgsc2Aie9a42_p-iIiE4Ou0Ndt47J_FqGVWF5yoVSf3qWnitzQXidM3zkO_YfdveY8oY_USrO9WdAnvWsZjyjTw3ws-yF2tbpMhjI4-OIp_Br5icXIU958JzgVrrIger51JBW3BMJy1JnL8jc6G5iqnmhZhYD2exZetDfJhLpeesnCk5pXq-10Y3Jz2TKVht8hxQ-nhhuYN9iu49-XYJrQqDvl9IIpsl9XOgLlbXqwtNGyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=g7U9Uwtoq39jMzeL6wUhH8AWrXgKLD8JwMaGb6pEJ1ljmt4tLHfWhx3g4diIf7ffP-X4tOubM_TdbMyk4ZojaZ7Y2Zmxso8u8wzk_h446meJ8JH7CmJxAi_pZyrVCKETjaoF6bZzXYPZ-vd1BZPVIFnnNsekgB0u5x9NqQEzPQ78EzM-t0nVgWGMbrtdM5hEewtiZg-xcRTI2YuIvZFT8rn3ZKayYHawWF85An2QS0RJuSflvENuTatgSqF7FOQVpuwzos3vH-VZNKI6pRoaU7ubDXQQMB1Ugrpopj20Tux-xgO2ftnv6iZdiuYPU8N27cM5SbSNJjoUCYwmVJjpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=g7U9Uwtoq39jMzeL6wUhH8AWrXgKLD8JwMaGb6pEJ1ljmt4tLHfWhx3g4diIf7ffP-X4tOubM_TdbMyk4ZojaZ7Y2Zmxso8u8wzk_h446meJ8JH7CmJxAi_pZyrVCKETjaoF6bZzXYPZ-vd1BZPVIFnnNsekgB0u5x9NqQEzPQ78EzM-t0nVgWGMbrtdM5hEewtiZg-xcRTI2YuIvZFT8rn3ZKayYHawWF85An2QS0RJuSflvENuTatgSqF7FOQVpuwzos3vH-VZNKI6pRoaU7ubDXQQMB1Ugrpopj20Tux-xgO2ftnv6iZdiuYPU8N27cM5SbSNJjoUCYwmVJjpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7ZF9rFABr4yEmG1hxDZ4CN_Qmd4zxfG3Z7qfeQ2HUOgA78WCNayOVJtzUEDz6pyY1VGjR8EuZO7JSTssEj4T-lMPYtPj1KBdL53JOcuWfpiV5YgeHd77PbfYXMxBfpo58GUXbf1E_s2OBjvDN9Ycu6Qyva7hCRMAplZg_FOTvL-gCk8rupQKvyzXCcM_uhhvKTVBJGcrwH1YRWW1wy6G2Tcy1oWbl6TKLA8uw8fykHAEK6J2_W5zYkSUuCPg1Lh7KKlg8lPsCM3_0fzVfomrQBvPduAbnTP3Uk89tYtckC6MBrVLARHEdbN3WWBKL7FC7QBcbU3yTgq7D1RorbWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkFbTBE19TFbxp4f0kEpTgXj2RK0hs-c8Z-t0LcssaKMkz070JlEYzNewVw_TRBClX5TXA06ROMOsxeqZsvGJpCZR2hw5wI1GWR5uo7P4qUCwtw-fbWMGtJHOnJCOrUSyRDeQc8-G_ICaqGKFRP1r-hR0dx7se4zspL_sSSn2cOQ08cyuK1_v16YodyPo7fslN600H5yHextDzENESCJmNOj6ZnKCT6BV5o8PyX8TKJrtzKNgjci-XEd38KJqQUmnr53CRrL3mWIidJqEydnetZMk3GYW3QZ1U5oq18EKlKDuSfTtfL_zD2UcyQaj1SqJzvZcJAcT-f9ahol__A0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=DRYW3Uf1EuTuqPJfDQz2k7ZuNHygV3CbIv_YWAlHki3I7SI-7xbWJ9iZOGWPbL_yXF85C_9dtntYhpVPehibCvk0blgeQliH3OTHUk30Mrny2A0DwAWsQMcH7t7I4-jdw996Lw4n4l9mktkuxm3u4qGXLgHXN_ASPr7TyQC6bO7XVGRf50w3VIRdLYr3LIy9176pVY3oPuJaENR9Q3e9Lr6Q-STkxAfwYv-t0ok5cKm4bnUqgiJGL7QR2rHv1YbYZ3ByeCw5UoKL2wZ4e0T-5FNVZPoJhtCteroNaa1Uw9FeogxTXwoQzkiNIRQ2VqybEWrvUzdnwJJxMwXlR3EvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=DRYW3Uf1EuTuqPJfDQz2k7ZuNHygV3CbIv_YWAlHki3I7SI-7xbWJ9iZOGWPbL_yXF85C_9dtntYhpVPehibCvk0blgeQliH3OTHUk30Mrny2A0DwAWsQMcH7t7I4-jdw996Lw4n4l9mktkuxm3u4qGXLgHXN_ASPr7TyQC6bO7XVGRf50w3VIRdLYr3LIy9176pVY3oPuJaENR9Q3e9Lr6Q-STkxAfwYv-t0ok5cKm4bnUqgiJGL7QR2rHv1YbYZ3ByeCw5UoKL2wZ4e0T-5FNVZPoJhtCteroNaa1Uw9FeogxTXwoQzkiNIRQ2VqybEWrvUzdnwJJxMwXlR3EvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoTqvSw9x2Aqqc9jsx5T5AS-NXlP_M4AUx2usOagh1_3fVtO9667OC13f4ssirUnqFNP342GlENhF6AD2BMMw-6BdUGs7UyGwYSYyJkAE4Q3D9pop62O3xastfelyzWAbSlMMq3-WfGsJdb8UBh71y6vj4WhcKDqPIXCxGvZ_dIdlVTj14223Afto_Fp-d5koaQBgR5qBtMSPmJYLCqINEFDy8zJqPj6Lh3yQ7r8wUfuQn90UB7IIu7MGHVOnR7gSeqpCkY7ak1dNdLndBIaKdtzcBA-2xNAjWBqg_UdUsEm3pAlOsDkgrVkJcvjicExPgMAgWtqnXV0066D6j7cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Ax_ypmjkR-MsI9qM94T-SF2U9-NNwIs90ycE4B5gdR7tKJ8jc3qeJw0KrajAKAc742vdim-RXQ-LD4MBEd5dNe09apuLbrqycghMMBLSOR5UfQT9qpB_fi2rYJm9N_s7uA8EBxiwPldm2YKrKhz_ioiHLv97--gRkAY2BwGXkBkC6ZhvQJA8niD_RzG3qZ0Bsa3sfhhI0J0StYeGE20X5f3vPX_mWG41TUD8rSvVkwtogbx0k0_dBtpDQZeJk36BQfF54te-iFb4CZ6pj2hkx7bLd9SU7v8JDCO5xGaZDeCmS5C_BnK_p2yxBFeWNKGl1kN1wVfIT8sTAZXbPPCzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Ax_ypmjkR-MsI9qM94T-SF2U9-NNwIs90ycE4B5gdR7tKJ8jc3qeJw0KrajAKAc742vdim-RXQ-LD4MBEd5dNe09apuLbrqycghMMBLSOR5UfQT9qpB_fi2rYJm9N_s7uA8EBxiwPldm2YKrKhz_ioiHLv97--gRkAY2BwGXkBkC6ZhvQJA8niD_RzG3qZ0Bsa3sfhhI0J0StYeGE20X5f3vPX_mWG41TUD8rSvVkwtogbx0k0_dBtpDQZeJk36BQfF54te-iFb4CZ6pj2hkx7bLd9SU7v8JDCO5xGaZDeCmS5C_BnK_p2yxBFeWNKGl1kN1wVfIT8sTAZXbPPCzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=WVU1tBWuP4L6MKTh1eLfvIsQ2WGqHlBmnqFKQE6acX9vDYT3-5OvHVuU7o4p9P4FtvtVxXd6OzznYmIGQ8wz5S0vaswOyrvj9ID78zQMFAkiSUEPdsxc_IeRD1ajVpegGxy_O-ZmvqpdijY3ffn8-hTHikyZQH5SQz-IJM3nayMMCDAPc_T9w2l_dRc35FauN3ZZgaanmvEekhe95BZjuphG6sHM5FLOCdJnNpSm_J2ps_d7POms8yc9aBWHKNcp2bZF1ZqfrXL1PJgTkHmHxA7JAKHZWLts7fhUGrfZ6usv1q9qMlWPst4Nq_5170V4UvkSq0HbFCibQeVWbAkM_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=WVU1tBWuP4L6MKTh1eLfvIsQ2WGqHlBmnqFKQE6acX9vDYT3-5OvHVuU7o4p9P4FtvtVxXd6OzznYmIGQ8wz5S0vaswOyrvj9ID78zQMFAkiSUEPdsxc_IeRD1ajVpegGxy_O-ZmvqpdijY3ffn8-hTHikyZQH5SQz-IJM3nayMMCDAPc_T9w2l_dRc35FauN3ZZgaanmvEekhe95BZjuphG6sHM5FLOCdJnNpSm_J2ps_d7POms8yc9aBWHKNcp2bZF1ZqfrXL1PJgTkHmHxA7JAKHZWLts7fhUGrfZ6usv1q9qMlWPst4Nq_5170V4UvkSq0HbFCibQeVWbAkM_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=uuhUp4lkFaoA-OIbimk1MoxNwx_Llvrtvq4jMHRzzPu_o4PnwjCCwgnIapFRMde02DPdXM1C9YR7RbmnEAkoq6yqKZ3ruKyj7giJ9uXqYqIAJF3W0RcwyvdBOYjjOPbALo9Bs6_cK3uFqciE5RYf0lLrd6IN1fuXAIAjdLpq_ONieoKYBtO2xiu5Mf_rVLWeCjJs6jddUkT--MUxHXAGvaz1LPIpk2G2Yqvnur1vvByGqMdh__MrxpqA-YHmuHAFQl6MM4C0umJkOqATw4CHm4kZbOJZ18mdC32SJpvQwt8dPidGCSawurgGDpXGoCtZj22Pk8tikI7h2LPueBddbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=uuhUp4lkFaoA-OIbimk1MoxNwx_Llvrtvq4jMHRzzPu_o4PnwjCCwgnIapFRMde02DPdXM1C9YR7RbmnEAkoq6yqKZ3ruKyj7giJ9uXqYqIAJF3W0RcwyvdBOYjjOPbALo9Bs6_cK3uFqciE5RYf0lLrd6IN1fuXAIAjdLpq_ONieoKYBtO2xiu5Mf_rVLWeCjJs6jddUkT--MUxHXAGvaz1LPIpk2G2Yqvnur1vvByGqMdh__MrxpqA-YHmuHAFQl6MM4C0umJkOqATw4CHm4kZbOJZ18mdC32SJpvQwt8dPidGCSawurgGDpXGoCtZj22Pk8tikI7h2LPueBddbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=ZeZcbX7lVKpoDo83y8Sh4iW4Mfd4ZC8f8-s-U0uZZxeQz63GmDYI4GnXwYPRkZhUdhrLUTFUAWqMypxqxlbp3skwWdS8mvwRbaJmToHspT53mGdwMc-p6iOzyebXSL8mzjvRamk1UKrASG0yv3nhPt_xbkMI57Bby4tADPJVaIsJcYB0cQcEQKS_LYY9WEFepEluB4buJudOAhVL56buwg1ahZxI8fLDqx6OYkW_H-U6VnprWLKI6j-UKmSkuqBjd2mNZdjAzRGH3dw25C48RMg27zdbxo5qZeHR_rx9K8S64kdRjEVKEzoE0qit0qXc7LSNGXjJisub_2gx-J6XXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=ZeZcbX7lVKpoDo83y8Sh4iW4Mfd4ZC8f8-s-U0uZZxeQz63GmDYI4GnXwYPRkZhUdhrLUTFUAWqMypxqxlbp3skwWdS8mvwRbaJmToHspT53mGdwMc-p6iOzyebXSL8mzjvRamk1UKrASG0yv3nhPt_xbkMI57Bby4tADPJVaIsJcYB0cQcEQKS_LYY9WEFepEluB4buJudOAhVL56buwg1ahZxI8fLDqx6OYkW_H-U6VnprWLKI6j-UKmSkuqBjd2mNZdjAzRGH3dw25C48RMg27zdbxo5qZeHR_rx9K8S64kdRjEVKEzoE0qit0qXc7LSNGXjJisub_2gx-J6XXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=e_ySwjVgFQCLP11UAtypMXEuamwvA71qXIcDQyMUNG8-awg1aaEJLVn0jxLHHxHxurLVQ_DQgsL9dg6anNV01yx994vNvaYYvGtwEOv0wPe75cadLYpI3bUs_Yc_nsAOBUG8BtfM4681W5q-R_GQBGm5x99Mosvc9g9AAUJ9ZBS3GHpDnuzUeaqv_0rDlOg87I-3RYeGAmMG9ssXGqhWO5XRMG1YT5pk5b5N6HbZZwW35RxOGngo1XibTsjAD-rEFqOo08xkNMRP9aBrEb_jMoJv5aBr5GKf8njtnPdB1x59h2rG-5cClomxPx6V06sOYIfbdb2vAJWbHitk_tHIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=e_ySwjVgFQCLP11UAtypMXEuamwvA71qXIcDQyMUNG8-awg1aaEJLVn0jxLHHxHxurLVQ_DQgsL9dg6anNV01yx994vNvaYYvGtwEOv0wPe75cadLYpI3bUs_Yc_nsAOBUG8BtfM4681W5q-R_GQBGm5x99Mosvc9g9AAUJ9ZBS3GHpDnuzUeaqv_0rDlOg87I-3RYeGAmMG9ssXGqhWO5XRMG1YT5pk5b5N6HbZZwW35RxOGngo1XibTsjAD-rEFqOo08xkNMRP9aBrEb_jMoJv5aBr5GKf8njtnPdB1x59h2rG-5cClomxPx6V06sOYIfbdb2vAJWbHitk_tHIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZgOOpdmKv6qKx1Ll0TF4TmwEzxClAQPhCZ6Kuuo6zGUj-wpL4EKsz89VEjma6iLa2eQINHTKSJD2BREkyGf2EIgaupzj8r0KiAWb4il2iCGYLfjndyA_FP8RLxqqgPPmjVOY8Y8gKPenl2XhhJ_p7zeMiofvVgCB7t7DMlof3qMjAQzxrnd9axuF7tBs_XnmMuOsQfFHazR-Fu8ZUl8vRgabLx8Q185UB0K6D_dtRjL43ec28NrZWC2hEP5ANvgFyP5QtiRd11fDYnJuCJjICCBcX6_fzK84LKewRsz84vIlylkZZVa-yCGpMDH0MZyPZgSZgTk8IVhum_VPP4SlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux-tUHlJbkPMVAjVUYyOb_iP5VQ6XsAI6z5i0tmSFGiDjfGjQbEikLcC2S0UfTiUdnfRn47pTbBRIs0myQgsqaWJdZ7IJ_3HOUuCP5akvToRnVNLmnq258EY2yJoGxkVYwLQDFz5NtO3km5qk7jgll_Bil9rLLjhWdg5RcSjPZJN3jI6hxY1Z7hK-Tau68vCKSvMzZCrkHsHt3NP3T2v7P1Bfzzl8ROzV4_IG_Lx6Nr-TjjI9yp7OPXnFoaHCVPTVK0BxEYzQssoGCwLd5oCvQGNov0KLXxypIS88P1QoEnfF3o4BhKBry7wvaD73LiTWJKRmWwcLv-TWNNejvrAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpQlU5UnlG8XmcDtkvxl910pSOaxchxwOe94L1B6Uj076I8msFVnIdx2hlUpZZ9iaxr0ar_KpNov23ljU5HpTZH5BTbgVLVV5Zr_l8nYWzFBgoNzGAI7a9qYe3QnwPFz7_0GAiEQijhwfd0T7dJsWIdnGLq5titYECbpme-YMCEgKOJyB4yRKxImENXXBZUsI0MJ5fxmtkj51jRpWWl2D5gVfI0uznWpJmwnSLCVYYSkzfd6M0YgrFCttUERQ0h_qxSp5IR0EO6sO16ctMqzLpkCYlWyFbsBoz2WZDaF5Uu32ijQ5VE_bFSzCwME0CxwZ4yFXbnQptBxKbA8FO_DzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=iLS0hPJ1wV6jaD4Twnos3MHVHzM8rb2ZW_19duhBXkXiN6765toOPnhJjMuY81fWJSY05G-dIIhECJcBQvaNLiGiLti2klJAkFWV1UHm5LWHyaacMtUrrQq-Rn7btCEqcxStfpfAVOUqdJCBbqdbLSf8aTvuYy1GAM30Bx-X8U5rgYyC-fisJYmopAqdK68yhju6NbAMVIDdTIyCzhEB2rm_OyMJ1cSzOJRCROlVM8liJ6fw5mOpbW6PJix5j2-2Pc-T0Oy5sdNiNbVnSrkx2VbNdTyTu0P3rz0KnVnED3eqrjJ__DGU3mHcCzI7HK_6tsEZCEVdkaOLp4EtuYN4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=iLS0hPJ1wV6jaD4Twnos3MHVHzM8rb2ZW_19duhBXkXiN6765toOPnhJjMuY81fWJSY05G-dIIhECJcBQvaNLiGiLti2klJAkFWV1UHm5LWHyaacMtUrrQq-Rn7btCEqcxStfpfAVOUqdJCBbqdbLSf8aTvuYy1GAM30Bx-X8U5rgYyC-fisJYmopAqdK68yhju6NbAMVIDdTIyCzhEB2rm_OyMJ1cSzOJRCROlVM8liJ6fw5mOpbW6PJix5j2-2Pc-T0Oy5sdNiNbVnSrkx2VbNdTyTu0P3rz0KnVnED3eqrjJ__DGU3mHcCzI7HK_6tsEZCEVdkaOLp4EtuYN4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=XXQs4syjWPVjcmx1-Jl-jkzw18-bkdETBQn5_x6XMeA3occF_5NLmldQwQ2OgUJlpUKVMU_e4UX7-eOPiZUVp8Rircinu0Cl7KrkTBl2k4Vpguy5aYCw0gJZzFAW1N2Lj4GGBfhREo4CUdgSmRJ-hcMGdV-v4kERGoEqWWhYosJJEQGiqZ6spiBozO5gO60vjiHw51BM0zky2xjikngmMej5ew5tUgZwciR3J4ZvCm_JiA7gwzH2doe43K056xphFy4hrsOOUBRsn8itH-ZZHM8TkKNpogTwlvkDTN5flcuv1rf_B1UgRDThCbtjP9PCBHSRu1WdBXoa_X7WMcPd4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=XXQs4syjWPVjcmx1-Jl-jkzw18-bkdETBQn5_x6XMeA3occF_5NLmldQwQ2OgUJlpUKVMU_e4UX7-eOPiZUVp8Rircinu0Cl7KrkTBl2k4Vpguy5aYCw0gJZzFAW1N2Lj4GGBfhREo4CUdgSmRJ-hcMGdV-v4kERGoEqWWhYosJJEQGiqZ6spiBozO5gO60vjiHw51BM0zky2xjikngmMej5ew5tUgZwciR3J4ZvCm_JiA7gwzH2doe43K056xphFy4hrsOOUBRsn8itH-ZZHM8TkKNpogTwlvkDTN5flcuv1rf_B1UgRDThCbtjP9PCBHSRu1WdBXoa_X7WMcPd4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=QyDl1dpUHEVuIKS3w8QkGbjaSFMpQjXUIoF3p9bVu3geGkjbglWfERX7O0kn8Y2eyco3Bz0vavxKLEyo1XD77iCE7e-uoATXAanhHdsox0m75UQdr_T1m-0yPl3fpwNvszCdPM-catcykJMRxb2Av2jmbHJU2wz5uVYYIAA7cUis2STnf7wtusrPOY_FlgGrAQDMWxf2dukYXMlJVfyuuzigfPrEI0cggCDV45OcfMbiBE_3KIaMlsR6E2ceYzDqlNQDTN0SGR7-dxys0Wf7_DB3UBX8I04PnLMJRf2IF6TLJDJoAG3e2LSKZFrwtVBsju8_-lAbujBC_FxmvUBthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=QyDl1dpUHEVuIKS3w8QkGbjaSFMpQjXUIoF3p9bVu3geGkjbglWfERX7O0kn8Y2eyco3Bz0vavxKLEyo1XD77iCE7e-uoATXAanhHdsox0m75UQdr_T1m-0yPl3fpwNvszCdPM-catcykJMRxb2Av2jmbHJU2wz5uVYYIAA7cUis2STnf7wtusrPOY_FlgGrAQDMWxf2dukYXMlJVfyuuzigfPrEI0cggCDV45OcfMbiBE_3KIaMlsR6E2ceYzDqlNQDTN0SGR7-dxys0Wf7_DB3UBX8I04PnLMJRf2IF6TLJDJoAG3e2LSKZFrwtVBsju8_-lAbujBC_FxmvUBthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-9sIYQrvvEkKhL4MBhpVEdGpxilGBN6AQQHgwm27eYqZKDganJvZ-2I755XEt2HLG68YOmI2AGAD8zYS5tiqgj9zBJWpF3-co9atQa0e1x4vvXSh1q0s3jLBXFlizHZPpJjftpjzGVM9Lml4okTdG0_On38Lim-J7cGKvmQe92wskcLY9ETywSVS4_Nkrn_O0ybuEo1c4rVvKw4ZW01sPPOt3Gin1weJ_zLfqakZCIvfn7jD-gfcMWIdfeRzOQr7DNG9-Jbj_q3B1cxKhtDyQDC9Wm2MyBZTa5yDXmU0Zyws2MGiTbm7TAkGlVGsHMPRo9_A7lp4jvGqcKRMeTi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Dv94iez2SGBDQxyo64TsUWIBXqY9RKeTMGKLZ_DBGmDZxkhe9U3WGo90-UY2SlVYJioW0tSfm3zUVgXyyFjPgulam7T-atGZnyY6pGvRB-7YaEs_lCqWJ92kI9f0qSe3_qfBVa67e58Dj5vNx_O0neMXSY8yz_SB8TF1Fup8Yxupc8XsyId2H6a_6N_fxAPJboVt6b6cn9mWmErOl_q2Q2puF0UjXDmae6jeK_3nh-ZvNanRYwPvdp0EHTvKU2xywobo0gBd2ABI7a7RxygPRHv9komUOdkNBs4NYVisDX_YHTcbWQVZD4XN5cPEPTmI08aiDld1L1P2PfzhHuHlWzbIyo7SdR0l0FA3m_Lhv7HcQaltnagcb7qmqIrhgipl_BBXAp4gaOaQtmK5qEKRfC8jX8XUvxfJHfSZq3xSXwRmQJP3nx_djEqSNRvnEafQIN1db_FikJo4Soo2zjTdfRG3WSnPcrw7qflj7awE60BzcyTZIgi9PJ1uZ_t1Wi8Y3DQKmEYQWFs5SaSmN9OCV2G38EzNV3bud5sH2KYeiqsud7NFzPEgNTT5CY1TavVByJM6y0r6uC6BH5Toax-SArJ7CyZrQ47FzT97oi-WagahzN29c10lvUN2AwlDAD4LqT-3wj8ZYyqmKoFs39IPdslsn8GOp68rnq5YnFygwec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Dv94iez2SGBDQxyo64TsUWIBXqY9RKeTMGKLZ_DBGmDZxkhe9U3WGo90-UY2SlVYJioW0tSfm3zUVgXyyFjPgulam7T-atGZnyY6pGvRB-7YaEs_lCqWJ92kI9f0qSe3_qfBVa67e58Dj5vNx_O0neMXSY8yz_SB8TF1Fup8Yxupc8XsyId2H6a_6N_fxAPJboVt6b6cn9mWmErOl_q2Q2puF0UjXDmae6jeK_3nh-ZvNanRYwPvdp0EHTvKU2xywobo0gBd2ABI7a7RxygPRHv9komUOdkNBs4NYVisDX_YHTcbWQVZD4XN5cPEPTmI08aiDld1L1P2PfzhHuHlWzbIyo7SdR0l0FA3m_Lhv7HcQaltnagcb7qmqIrhgipl_BBXAp4gaOaQtmK5qEKRfC8jX8XUvxfJHfSZq3xSXwRmQJP3nx_djEqSNRvnEafQIN1db_FikJo4Soo2zjTdfRG3WSnPcrw7qflj7awE60BzcyTZIgi9PJ1uZ_t1Wi8Y3DQKmEYQWFs5SaSmN9OCV2G38EzNV3bud5sH2KYeiqsud7NFzPEgNTT5CY1TavVByJM6y0r6uC6BH5Toax-SArJ7CyZrQ47FzT97oi-WagahzN29c10lvUN2AwlDAD4LqT-3wj8ZYyqmKoFs39IPdslsn8GOp68rnq5YnFygwec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRZDXa1g5joZdAeBAM-id5cDR8Cq8yMFT7c4ttTuM43JqRK6ufMimT5hwABDV0B__2qb6DxeH6F4faD4lGwVdFK7xSKZljyf3P2m1TBSgkqrfj5RmIo35F87-ZT0a2RgFlMXvNNNX4m5tFzWuMsGCW5ISShvvpp7DEIdiGnZ_MYHTFt5u-HQniA8Qo29jDmzQ_6KJgIsBfiB8jWZQR0nCfdLkKH8UMWyJcuC7g0SfOcgJ_lhAwlFkX-hSyuwMZVBYTE52t2xpB4YPhYPDY0aj_EAZm_wrus-AiILjXYsx_oEZ5ENPEy8m6JjqteJI7s7GR8WMHlcLWyT0RWVC65mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=MRyA6S8kCaaPVDbSfql6qu5DZ_t6p3v-7ZlbM1vTpNtu1B0EEgZw8F5xgCgXk_H49g-9jf7sbLGjp9qMNNxT--gJlkHBaJTl-eHP8NziuCnYRGcLUvfhjMJ-vwa-lKOluS48fIFxEaM4jOI3yq1wVJHfwjcB0awklGxk0ARaLae0Y6lNGzikisFArnUD5oApe75y5ljTuiDMfZTVafw3cPbjglJ3KOQa01vfjeAeSYEWmsVLjoENzPXJmoQDZ-HrdhDbc-czasHP6U-2Npq2l_RomAYwMrxzsFL7kgn2Dgl9aBetjtsd3vmxuF8R3QOut58w7QqxYT00RTDS1fkHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=MRyA6S8kCaaPVDbSfql6qu5DZ_t6p3v-7ZlbM1vTpNtu1B0EEgZw8F5xgCgXk_H49g-9jf7sbLGjp9qMNNxT--gJlkHBaJTl-eHP8NziuCnYRGcLUvfhjMJ-vwa-lKOluS48fIFxEaM4jOI3yq1wVJHfwjcB0awklGxk0ARaLae0Y6lNGzikisFArnUD5oApe75y5ljTuiDMfZTVafw3cPbjglJ3KOQa01vfjeAeSYEWmsVLjoENzPXJmoQDZ-HrdhDbc-czasHP6U-2Npq2l_RomAYwMrxzsFL7kgn2Dgl9aBetjtsd3vmxuF8R3QOut58w7QqxYT00RTDS1fkHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z86rk8NXR_wFpN1Ir0toEeJElSt6AquMDbwCJi3qOdOK4c7m63PYegtfsUN1A3XflgVsYt0bbaXtuCyR1ijUR4cAanvSxVujMWNbrFSHm0om_KH8fhOaZCaDktdg66J4CQsAEOJEFbmtQYBmh7wc6x0EpC2DzEpp3Ji0U7hDpCcs-yC9O8qpvnTVKbwVqxpKGYocQgdowbcx0wP3Ueaejtxdhr8ePTxnSMDrYfcq2PmfwVI7gRF9cZMdAxUio9OOF7_NkbwV331O6atFJ5pm3AuYkPlXUPRZTwJq6lTT785uYVqotq6ICcWdTVrTIpTpOMZUULSNXdCDbcjkk3BXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhY_4EagBM8BJe8ydqGMeRRE8VisjtteTJF72fTOxCojN3Y4bO0nveSTIrqgSw72t4Z7ixn_bLglpmmASSJGW_h72WiLMl4kgrFeBxkT-4cRjcFJvOQokxP0pAAUS0I8Iymh0FhnF5H4ZNo7dNUsVZ5pMO7Yaqv138MarlYo6DuwSZA33CGAgsP9l9NGFu-mOqTCBYxqFGNQSM5ea9Ao7t7Xk0VElOpn98cpCKEm7o6y8THKbtHA8Wbknaeu08UdcTV3wD0Qyt--X0QyJWhIEnBdAX4AidsfUHpmy2pz1bIlv93WqYzPwgH0IZmNmK1R6L-FlxedSED8wGe6WuDXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NemqRZmSej3M4N2rIdIi2PuEn3FyuxuEFAAIx-ZK_mNXPyF6fImaHSlnBL9-filmEbV2udNdio8mPae4GZVJ4DYUqToRyoE67PRoptisrhtg7MyJ1OlFsi83xQ0DdZeH-XSbmx9ZRUjXwdTsz9AenqU48a16CyqxZ26Oj6tb8m4ROH3pOZR_DhEpssDPdaYQAYW4HL9A7EPxMo_470cFgu_Ifp1QkDzgYTGT1VGfMwYjGQKlUK9heKk-BdfG4oPWOoDWnPW0zXEn86mofO1yMVb17pvGJCQvTjV9DX0qn8PI78pNUFkP2-mXt5hCP8e28A7jtsvQo4yEa9_VS_sBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRWZgGTaNkTLK58PTrYH43xV468ItYBtaSxEemAs62oiQjgeuawxWFqlSYZxC9Kc7CSzq_6nrfsGU-1QCN_llgItBcKneD7y8T1jifAwZUnVFzCopEWf9FzKN7d8hvk3_62_wArvODYTBeDjEHgswiUZvV93BWrK2U2XFbRM2Bh3r1P7LX8n4YzlukjyzMb4oqJE4MnIm5xkeAGl_6bFZ0khK1fMPq97pyxfjLeK5Sinkea_M6QEEodZnalvfzG89nYL-JWasdnF7IxE93wn_neBvH52FMysl02rPj5jXIu1nC4r6NKmt-DsNoJb9_RBWxeaHTzRugmarNYdSoxY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ7wx_KXIqn_zsFMqJgi7M_gpujErkH9g1ZIhrEX2RI81GJ8rq2-459yyA3YzaJqpaW8_cU5H7A5hd3ARjnQqiMYs7KXDGr7I7rWeUOt6TF8TXOM37Dn3vZYhk3de35MVyVgbvZDS3PHqg3qonr6P-HE3tqB14Dsu6f-t3Tb5EHBTcNIn3jLJGw0PRP688C6B0y071PCe84goge-rRw-Jy8fpzSKmsIpHVSKfPjCTv-XgGCbOBqjOOLlL2x7XhayOThT-daCot6RVtnwTPBVMy1BYPadFMY7v0GhSc64-CHs4J-B71v1-Va8UnazCblyiKg0yBgMKGsro9Wshs2Z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwcahv1SHNOiLHozCEkiBtSg-54DaLI65wHelaZSYz3P802Qsjjp9a85PcoN-to0HeIWfLcX6KC0Xu0DDOWGhTsZR8Dl2zisltxQjPozCB0ZA4cdJTjwmLJvoQw1PO5iW-RT_hujC7F6lWUAhuxwupw6SpVyfr19sDmWmMf07dZsuInukToH4S876ikJyYZChhxj483O22-LUtGJfHNN9Jl9S4xOhd5JUsOuncTaqGP_uyRSCATfIazH1svmXlCcZWxLXGK31blBCQQ8YHTJK0DtglCq_ePoZCA6Uz_8dJjTYTvjZBd9L1a0yGKbVVoqy5mOrsIDbUUgJivAHAAIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
