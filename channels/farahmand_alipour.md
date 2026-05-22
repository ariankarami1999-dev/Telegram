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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 13:48:30</div>
<hr>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeHsoWlsjBaCxS0Zb9CT2iJcjdHUJaT8WLZMuBPFHbV1XA-GIKypcmIhuEMgPmIPTq0rzIowHna2JtPEt3zG9C9tuQsxy3k6BFmAcwbREUJhhV_NrzJw2-XTwOjr28D5tc971A1tKF-uv7mOdJGUsXtl6jj0xOi6BCCurr5gEOjjh2oy2-LMzDLnxDpHiJRC-HHbBtHFru5R2WWVkm3Uw3e018iC-vH2r7FqJdbk0NW218amFuWbgjo4HpkU-TS_C_WCaNawCoB_7m8H66Zu53oUnPwUMgCl1exIhiprbz8w2KbG3FqiVp5xqMh2X0QTPuFYxNEwnLigKrlwPxWHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDY9fhlzeqbIqjc8bW5cIJ7mU6dfLgpTJDcZNqZWMWImWFVJ6GV0A4Bg0XEA4IXYA8BSR8KKR7IrkqskKaIMtTsvN8eDJMb4TnecWqFymTHXBkNNTyCpEBuVCi2gNd-XNAAcD0MRm2NN05fixJQ7tI-6stDURnNd-CPIaMggOyjv5_1ou1frg4pBuoJU-DNkwG_EORn5kf4TPOQWE195GSlmFrngfOIS2h_gSetnHUXoGNCC2hn8qoNDCLdhPnTUnMIfXGstonoqypvJ59Sfsj538Jrf2JX6oFjwxMzqvbJC_IfUcrEau6ybdVADK3DrC_cVD8rohBhNl1UOwzyORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_DSpBnwP3Oes85QVPsMo3KtRfciq14s2uMiU5ZsUF8j_9Q8U6zSuT7rbu9krRrx1K2kR0kf6i_kT_xskdHduQ_6a5U6f_W9JytZxe6WnT57AC8oxpwGYcO2IDp4CRYgHvav46bavNn326zHjZv8TnsCwLLzQRQgJMEPUSq9SpnHByWSfVUybrcDj-h6IdXLVZ1ftYwpJk4_8CmFtwiRzAeEZKAXubMVcUJZRbdZwItR4g--KPKObZS9a_659uXb3cgWI6D73KHB2Xl9hUUuDVtF307I-s5ptYJlgm50ddqCEsI7kx5AzsFAky-WTro7IYDNK4X62YWNrVNnm_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez4sFC-qYN3nZf7--oU6_euP2kZmhUpUBAoYwVFEBBvbd24LJW0A6ctDe5TrgQeQah3oUg4F-hXLyVeT1SZ5LsQTpXaaQaPpA2uBu0C95AkdjV77U3P-L9bp0RCOO2-FbWPIkATw4sj37xsb-auRdhQwFe-lXA73zNxXGb9NI9ueAIYXLWURX3nHUiOOc3XgQHDgOSnBwgTl6Q0BkPZv4nH8-q6lbXgJWx043MEvw0krnLxcO0x4nEdeGqWXZdE5naIUwgRDyjrIFkUAYJGtGeLjyK6YzJ_ENcKTRgwg3duy0Gti0X1kWlHDjpmifoazTY9x0xApmDXhrszH-VTU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej_7Cjz9PU9oY6nkhsgxdwMZbHtLfzs05JTAanIKt1RsCzYa_ElgtLFAXj4SrkMogtbuQXiUxRiwXJo4xIi-LsNZZtkn7fpZtikV7byNhheOxOWg_dravqeaa7JkkJuOl0GUf1ZX-YAWhLtuM5J8pv341yZknJJK93AfSDUsVXvNyI2t_k_3idJc0bXg7UjC8jbeKi1Q07HSVC5ZZEb_pE1TzfnI9MxLRUS-_m0begQQUoA-kdTxvCvSt-LeThqGT6gd_-lsWKBWacYSSgbV69dkojkM9Ckr76XL-Qm4uouNaCNsY-WUFJS5v-VJAIX5L_PV2LONimy9rMngszb9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL_sg6kSG8cEPjr5gEyKUhq5ORFlax7nG5r0I1PQJ0RbtdwNyk3Q4JExnl0ksUhHGaWxgqzklEea3hJolXuKWT1nsDiv5zvJyHJ-LVuMTduI0fxB8ioCYIqNKqUKVdevWZwBAb_7q0xE8tx5k8n4sT7MnZQrdh2ieyFdfdil9aMbpw4YIzrkBuksw0JPfiOxhGdUTS4HnmGPbioVOhnKfaV3Ln5CsSbc0YCZYraEMb1AJlXyC0cncayYnlHPChuCTR3OhXPv_0c4tnOmc2woo4XsoHVe2I8arL7p69k7HQazvlt0FrQfnbfnkwaEL3CTDgp0Qkdkdh1ljnDLGukDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPH3zqNiDzrVSiNWya6T24cFXwSwc3CeLkK2zeWkU_eIlQhwrvDJYfr4mMbEJEM8VJzljH90leNqOf6xpzvSiYeaVL3Kj4RS4CK3Nw4Lm5lQR15EinqKyU4XScYnY04Oah9n9IOFq72evTZsg5CrZVDUUZXG0FKvz9capUNlc7XKpNzMkHu5KyN6KZdpDF_Ju_7UTgL9xCCYtikeixs7JFB0CWAt0JutCXW3OdpIerQcfEGMATfxUZoK98YUIot0-VId3HzWo8M9OY7PhLfTPCQV4oPhCAU-vgu8rVG-BhWyxsAG5e0i32txb3WQnjUra4ZPjX8qV3uBl_09ULzZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrf3fiyXRAJzLYZXB3JlpM-gsJHwvMh8JJY-71coaC4H1TGV7R4ZNtwYfg7YiN1jpRW4YhlBFt6cwatn5nRV5e-t7t1M51EVGGEb605Mm1V9cCGN_GpYSLAgQNlgF-D_atvkPnOwrjHMcVBjTltl7-Or5dp4v-aNGEqNocQ2SsQ_TQtcHWokyhFr-2XYsqEKa7MoPNPSumLIJ9C_uSULcfh-4EB6ef1EcKiD84-SfY2r128Lm2hB9Zeoe_GcU18BVe5luG5vlXDDFJjeesREoBmzQZoqINFwuKHwMUTX1Jw9EUeVFMaKZh3gww_kQddd2kdfNl4JNEU6nPcROOL7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyRX_HzEaNuVSvuqvelCY-Y_RncpqDf5jJjzQHImyo38gbe8nzqYXfLGW5LSJOJ1NY_tnkav3uV__1L8K8I937q_3CWODfxDMpraU-QLMGr5alHlI49FbxZ2bKiDXr5qswUYnWzTok2b5J7gH74TPPy2vBwM-hq65TmQabPBCRjEOSjQVLGu72BPGk0PdtQ5uHVAlO9Wbzko8944Y2m4fuaz7c_aPWNrbt3yyg-bj7fhdWsUopwpETx0Wk9ON211EgVYN0PdlQbq8mARuQnAWC7XAxzRU-e_slIvj2Qh406ZICXBVCTtqINktUiYN7YtnNvLSwBcLykREqaHksh-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=DfXrmMP3BgSvyS_MtZp2hG4puF1irqhOgl3i0gTA3_H9BxhnU-uSYrcy0iuFDJS9PaJfMpAn5xUHI9ke9cEAOLvtlwEw0zL3hsIgRKZnlESd3UcDJYl_FFGZKrNtIjVWOwK_piI7ZmxZlgDbJjexDl1BQdB_2EW_DmYmd0qzYpJFkecL7TKjWfbGClsDI9KdoZe5aKsxBqRPGdIwDJjKjcjWrCuuqBmDmjEhSi6e5SLTNBnNJltzjs-cBw9KHW9S6QAvgXtuA0SJYjGCmmIeCyJ1kYY_6q8UCfOR4IvNl7jJXGW5IfxZSVW3zC40sgOHPTRVLpmZsDvvu2PIC6ItyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=DfXrmMP3BgSvyS_MtZp2hG4puF1irqhOgl3i0gTA3_H9BxhnU-uSYrcy0iuFDJS9PaJfMpAn5xUHI9ke9cEAOLvtlwEw0zL3hsIgRKZnlESd3UcDJYl_FFGZKrNtIjVWOwK_piI7ZmxZlgDbJjexDl1BQdB_2EW_DmYmd0qzYpJFkecL7TKjWfbGClsDI9KdoZe5aKsxBqRPGdIwDJjKjcjWrCuuqBmDmjEhSi6e5SLTNBnNJltzjs-cBw9KHW9S6QAvgXtuA0SJYjGCmmIeCyJ1kYY_6q8UCfOR4IvNl7jJXGW5IfxZSVW3zC40sgOHPTRVLpmZsDvvu2PIC6ItyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urh-aH7X0qDLo_wPPHCRU2TlvQsGPDfz6YoEuBL1VmDz7_RWp1istOt4v8Oen0deBUFBawHJJNouRVPjlV1AOfJC7ht320KiwI51s7tz1vmXn8tGrR2zJG5tnO0lK8tcKhnmVf17mimrfL-BjogmoR7-qqL_QSod7J8PVfNo5C0vtuxG21QZ_xWGymPn7mTVDRFa0shFxv7p5WIa-OGkgtZDSnquU_sdiKQu0oS1qLMVEJ60Rn7SkevVzE91qHhmYdO7hM_tIV6x6hLxgL8-D7IxtwY6-2ONuEiJd-jOpwS96W6n-0aYe5igyd9QGMD66H5Rxq05rD8zSHB9gVzWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nmniCmzVZT1fBZscaulNG39N6zsp9MVeKCezMswxPZcc0yDaRzqoR0GynlP5KMoFgFfZtxma0McA2sdS7vidwiisAcoTlj9Hc_Cqn2DSAqbfP809VEx-cqnewAoqobEwIA4n8Z1jGzSiQe2QnyHevIPyCOzzg1x2AVjcn8knCxnhfx5mAr0EcE9IEtROOPSPAI-3axvgvYvQc_0b_8P9uNg1sxWiYxqfYfQycLR3pV2kInw5bgVekkVSG-JVPcjpwLWKZNHHcXYkj-g75_7Qcs14KUlXBZ6sVSZYP7px4EIrI6xkPjbE8s9NiKVnUhgza85dXkdeKB87U2Npl0ywaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=nmniCmzVZT1fBZscaulNG39N6zsp9MVeKCezMswxPZcc0yDaRzqoR0GynlP5KMoFgFfZtxma0McA2sdS7vidwiisAcoTlj9Hc_Cqn2DSAqbfP809VEx-cqnewAoqobEwIA4n8Z1jGzSiQe2QnyHevIPyCOzzg1x2AVjcn8knCxnhfx5mAr0EcE9IEtROOPSPAI-3axvgvYvQc_0b_8P9uNg1sxWiYxqfYfQycLR3pV2kInw5bgVekkVSG-JVPcjpwLWKZNHHcXYkj-g75_7Qcs14KUlXBZ6sVSZYP7px4EIrI6xkPjbE8s9NiKVnUhgza85dXkdeKB87U2Npl0ywaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S55VTpEpQuMBqqJI7ylsDfY88PIYgA1ujMaf7hG9aalobfB_bgq00iJXt_0UHsDGJlT4MQVfBgQFHfdwW3ZJc_rXk62jTZ4KVFnz8XbVS4ldk4fq5tgorF-zt_Zw_kw_B8Sfo74wkTyt5jhNCWmEoyxzXQSWYXuGXz8iXdCCZSpGUEx6jTEBO23w_1Fdu4M0B_DDycDdg3OqYMjYhuR1ij9mFOi7CrNS48fkf-di9_6zMYgRCamxpRdFAkGQ_sesF1EOoI1Da18pPHxi4yT0Ozy9Z5HebrIkQSwYsZq9MzwZ9Xd9fz7KA5I8LwJNsXRKxZVrbpUDbsADY1WmP3Zw_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=S55VTpEpQuMBqqJI7ylsDfY88PIYgA1ujMaf7hG9aalobfB_bgq00iJXt_0UHsDGJlT4MQVfBgQFHfdwW3ZJc_rXk62jTZ4KVFnz8XbVS4ldk4fq5tgorF-zt_Zw_kw_B8Sfo74wkTyt5jhNCWmEoyxzXQSWYXuGXz8iXdCCZSpGUEx6jTEBO23w_1Fdu4M0B_DDycDdg3OqYMjYhuR1ij9mFOi7CrNS48fkf-di9_6zMYgRCamxpRdFAkGQ_sesF1EOoI1Da18pPHxi4yT0Ozy9Z5HebrIkQSwYsZq9MzwZ9Xd9fz7KA5I8LwJNsXRKxZVrbpUDbsADY1WmP3Zw_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0CuHFwYpqzNk9KzMBfVvVm31NkGStnMqMKRp9usgue42IZD086gE_hb3NkmqeyvH3CIcmUS-t65r9ueOP2J44ekRG2s5AyoGrIy5aY5jI3pFwkGE2GxuGqxONrwc9G0RvtOFBN15fmyiRW9uSoSZvAcIPDcHDtbtqgiomRgew-tez1JJS8V2hjbP_f_ZOO3im_LTcvM7FZ9VHhpPhxcN6yv_fIRQSOxDs2Mwoh6bqOiPStzkBVz2d3oTIT2_-3gO1jAaNDN6_rMk9Gomj1vIXa1o9SQsVTk9_JVYVEZduuWdr26xsnLN9j91yJ1Mb_4klDnqqV38j0S4feoshzJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrRqoWOxn9LSTnN6Zyvzo9HlP2wIuZv9qt6MeZ2q4MmdW7vP787oFO4K_URUFq_D6T2RF2RASL9pFa5Ldl9vnHgGDqPkCCDW5w4G3GvXx5duq5dESSLkrWabOq_zHwpKidVu_1-e7SMyZHWLcLQEaHXbygJsrL-CcF1iy33cr8EzG9x3nrt1XFmM8wbTuGpHxCZqA4n1Gwg04X_Sp2lcUhOS2okJwSu77opRrw7ZnURBLrEC7Cecc35e6uCDsyKe4px0wMeeAPStn3__E4Wt3fOxdJx4911c6qBFuMOH6i43actXEFrGIPjQzMb0o03kmlqtt16mWAuXIiZwOkGb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C073jBLaNrdZo5PWtSOmwX3qgO0b-abQsE8L4AD_zKw_S-4Seis0fPBQrTksQHcKb7oIbMLhorlQtfIOibPK5KgE0C_SCHIBwN-PrB1PMw2unpWxS3j4BHDXqPt6qkN-dB5NAlmdt2gVX46VyPV38bjHk2ZF9MGGoCHy-Z3ybzqYnHO_6uivoz4um5fG_Dv7dVw69G4t0cDAH87wnuPwZWoL7wTYUDZWV3cRuvhuwcrr5OjuoPLnJwNH856AZelXVi2Y_g98pMieRn534hL8QX1FfWl_ZimaDK1jLEpNxxV2iCMTZ3_zGS9QTYeOEp0dOEtqaVeSv5aRiZEs7N141w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um6MzQndTDcPFtJ_7_JBK4CFXPu7kEuFaWph-QP-RdCXoLjNwHEa4--vZuMEzmmqiUZCRzMDMI55NPZ2xVHLgDn3IhYKtRWZ9NjnEzewwnm4aUetpSUFce9bA1Tqbvv3iXBDgZKCCKajlKJ7swFQgPm5Chd5LLuZiBoSbaBd34qlqvUQHCFgXkbWMxlKHj2B4P6eqik2qQvq-hzTtXImLPfDWyWpE12XqnaFsQIr7NPW4CMOUFYhAE_5hH3-dtMAWsGaJ3b5fCua6GxVOtvMEhF281IPQqJsUywQm953uB3n6l8fevlandZqxRObOMX0R1TcvdiT65K6fpX8Ceq48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/es0WHjw7KVOwLS6bBgb3SeKm9j8hwP172T4IkKoDoB_CFBo_UQQ3g6a4W0HXRTWZGIGFJ8cMZsrEkFKKNytsn8kbdfQ6FHF5omI7_bI7IVNN2I1itUJperyixA4WZ_YH19l-Sh-Na_cSIdAVDJYDBkvcvkP2_rmXjvG9Ra59s_JQB5MJTdmdtjD_q324M-dQNB9h3vM-orwWb9IWO26VYbDWUszpsOEVu1ngZFsKT46fUEhdANAuwZWq4_IbqMITKe9kXUoQ7CRwEk0IK_-L6qykIiGOwK3tjBGqggBgfqLAfD6iz0YUOPfjbpVO0Uk2d02YHcwtAr1A1fvinkkV-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3NRX66bajE2A6sCjNzEB1YJxtYIjxLyWreqZfb00LkLZZvykBkq2R6fLz1aT4x8eQ3hsmLbjYLWiazHx4YrDy7ToLdc7K-bc_xtpM-KwVHfgK098JtwFKfabONBpGFluDYpJrBYevmRWhNbTyoQXYmTdgtcJV5p-IWwkNiTQ4A7ttqk1qArQJW19obYHfs5T77qKE0zzobjjbycB2M-lndmA31DvHT6G7DnjMyH_NMf4FfaBAgT6oA19PXTBF-lqjXVehFpkUZ15l5_e5U6IzIjhIFSFrhmucLPiutOkE4X1ZJS-LCcq5i_y-mCc9AbaOJo2Wks2l0ZCoV_f64loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kskBScICm3hPoC_rnFb3zsMIjy9pPymcyxM-vLZQ3TxHZTJzDY8QkPpbE7aVTiHtia6vqMPqqGpkEJkDFunRRoLia8Ae_C1m2EViBmMh7AspoXkgAXXtauubDBs6ZSkfWU_4OMfCL9SgQAyNHbInfzNE91UbwKcKPUH0BdItkZWKST4M-b4holkdWBs-Q9rlQ1WS4KjmJYnFrPkUB7QqTqU-PIDu5veS8kpa1NMcjPH5tbAo1nGMwaBrJmGfXkFmoOjFySmsGfXJakfJfaLkvlak5bexhC61raZc2Vvb3wTg7VzjSlZpcC7EMQGKwDVQmtZgecKr2yjwnucpyUTMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SInCdffEPolbx1YdIBuTTYtvGdaG4xRvhfeJAIrE2Y0S7UkBe6pYeE3LAH9YKdRAOrf_XwGYvXniCHrUx3uE4qUM_FT_PsYHdB65xdbcnOl7XzCIuRByji81fzRslYo0u1Z8zX1n-s_a6ww2SdmkkznQEGazBquxftVXWAaepHU-LAM1-8L2763ywFpi8hB4A_TDxfVr-GMJF39Ii5qPqdt6IiYAhvKKvQAuxOtFc5TsK9ZkJWMfb-mWyGXwLMIbs97ZRZzMCBbNM7zlfOxcv6DY14OsBNIWjvBbJJSb56TqcK9H1beygXJ4mMwxdghWW5ikWT7C90NGlUAaxrRtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LApi7Nl2VTho4f1qNImxkLgLixDMeLX8xsJ_c1_U2sI0oEg9NeVXg2tn5pSLeU9scgCGInbOUSeDnCRjmkp3ydjF1oobQZUA65xsqOS86WszFnX3KoT0dYB9t5PR3Lendyw2g0sHeQMi8Nl1PId4P6ARr10db-65jLVEdhLSLQA8dx05Nm3ZyAK9pgeCHO5zYH0pOF8ifthvwrKJJfpqASx8lGdsUvKU4wqnirly7Pz6g4e7z4v4SY1Pk7gcoACpgK3oHdPvagKvYwYFX3CG6quot7uPivKqBhY7jbLZ4UvmIElOhMcJHXQmYV_5-qV2DCPUkA-8IVNbDDTFe2EA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=jc-mq5UedwWUXhq3x1PUqilek-8ykL68CAJLCzTvVAJ6yyJ_aGaKXf5HgEk7xNSJXqcxcW-ZBBk_GK59XbF-2LZU-dr2AY95Mw5j8jpoO7ImJsa_Mvl7ImWAmG4Qwy1KVOacA2Qs_DO0XGE6JFNmGz1Z9s9pB7-4AQHbBBjQbG1CNiZapDoAITI6GNooDBMrVfzSMdsJIF70PNY-6LDwAF5ZZb4lMv9dyucaw3Pu-bkubqHoI5lP12BpVCEJ7J_1HphKI0KshNqbDL45ZPBWxjic-phP45Ii0-49BZH6TdRidyaJFHHazzMDja_wkw5FM9ypFqUui2BV4n5PmKTsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=jc-mq5UedwWUXhq3x1PUqilek-8ykL68CAJLCzTvVAJ6yyJ_aGaKXf5HgEk7xNSJXqcxcW-ZBBk_GK59XbF-2LZU-dr2AY95Mw5j8jpoO7ImJsa_Mvl7ImWAmG4Qwy1KVOacA2Qs_DO0XGE6JFNmGz1Z9s9pB7-4AQHbBBjQbG1CNiZapDoAITI6GNooDBMrVfzSMdsJIF70PNY-6LDwAF5ZZb4lMv9dyucaw3Pu-bkubqHoI5lP12BpVCEJ7J_1HphKI0KshNqbDL45ZPBWxjic-phP45Ii0-49BZH6TdRidyaJFHHazzMDja_wkw5FM9ypFqUui2BV4n5PmKTsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJZykZWOQn_Hup03vvznkoKFe8Vh9wc0uhzGI8rryhON9jnJC8GFSyY9H0pkSozNQkWU3p9C9kltP3l-h2UbKB6tIAMtGaHf09kusrEqbqt2Z6U2P4Jb23fn197zeTsodQw01awjKmzAZaL7aCfqMMpKeIkUffu1FJgd1r8NaZXKF2etByT_NEPipRO-XFhYaPJwoidd3X6iPlFb5AwCZ1Rr9YEN-C81kO0ksgriOv5F_1hmph_WKmoe2SQmP27czZtR9-yqNg6T1roWUNCZ9B4aEXU8eAtmyMolUV116cp4y_cGOPCadzMfyTtehwT4dBF1GzV3M0IIGm9dEn5byQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTDXcTCHr1_8Uz4nCkh78U45wW3A_vqa6aoOjjle81NwPdRXNoxEXIkyqTtIZZ9VIEQH71Lg7MFwjCSEzwfgG5WljDdXttkeL2kzo3YJP5GlMwgQSSPT6l8-FcAWq9ajd7QDB5gORd6jSZHkB4IpnIfeK12WqRX89s2Cn2BrWuXmc5Z0n5MddCi8dsDsGRe_pAVz7PLQ_OX1ecAlnQEtXA8x5SCi732sUfor31dXbQDeISR5SZipNvw4h5y76xIyddjG1ly5gPxqSdDfAbGjwnyQPsPGW68yrZnFzeIaPEmvE0VxotCe8tJmj6ltR-9sIhWTGQy-Fedz4rL3P38Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6LTC0jt8HJb2TCm1RoRG0IhwgRUrO3HCLZAU-VjTQGSzkNhiVhbcfMorOAO_8c63gWlkluFW9R5kQUgWUPjFVeufAi6R_bFIeVI56JAVsWiCJLsXt-m39WnPC0rPi6fLCkx_pP1nOBqFk_WRq02kOjR7Fgi13bQyLWOy9y2fXvJnk73cQBGpBd5FuyYvQcaU-gOM2SCe98ue5aerfxMpGgpM0KTs-510Tm8xi3IBdAxDOCjS2R2BdW78r6j_K8ZkVQyFc8WNPv2jCTTpdawdhahKpnZCl3xGsSrZYNXeRDJ2Dn0rg47gu6zUOy9xA8J6aHuVr3ZV2_IHs21twt3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5zT7QXT7cK-VWpBcyKe2MHKsS5DNa0Kp4Z7cflUSKdllzawdLJZw20SMHbeXEkw6AZV4GDDAijBl_ESLYeGqVqd_MZn24sKKc7H6-FgmA2jYdkZ7hPu_pASA8fF7nG1YXA1snLKU5qbpZs8Xqou53a--EEOH042yxXD00wf7qlr3X3FnzlTmvXpZuw8yOL--_WNqp7L9VHhWh2kDf0r_aAtWh5oU0y3spNGk0yc8ws4i01GN6EKh1XCCxffhcgwiSFM7-g07uhGgeusQo7KVKhfG3L1vSgEKNin_DizOnNyZMAo1cBPnDhQsVEAVngMwcbMkjqflh2QpbSW4N-fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZmu5dk2Bn-c-kQ4p8R3t8IXGNNWp2hmlmPSQaET9QAHvorRjsg2Tmx__6XdH67ocp26cLR1a3ke6BuTqpCBpzVQ7ageUdtdheURFeNWks9QvnUyU3PuCX4L80yW4bk5znsBnKPs4NHiAUJYGH14by5BtbAG67VBXSUvbtxoajsvs8NV1cvBQZ63fGCf3q2G8lmV3soo81ZFHgJVU_VVfYLDi_HHS6t10pDT9JC3-7b4BKaBKMdXTtrjqEtMGE1UBSevdL8Qc_IatkaA4Ipk7c1SZ-Nyu9p7kjFb-ZT-vixqMwSVPj7hlYbrEFVQq-TCP0jKtFVyF5cepVsxvUSJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp6ClBnD0K9q6HcECw7UeyBawvAPcSzQvaaNz7nHgQuvSF9okNvU32XAT5dKPgD0f8y-Ib-Ew2z0h6epTt2vYTsYkt4nM6bBKChVi45qqGXpJlQRVuGEN1JHcu5Eh5peQ1Tgc84tDkJC7e9DSOGX4I9swe07spfPxot9dfolmPDUoqQxiWtI6shMeQZU5k7LEb6KtigGb2SRpb0xHAGP6-Sj4ENW0DT4uoHXbgSh8eFmee78ubiXNhTZ_ofnwqoxEKg5bFwYc1WoZTH1orqxiyvMLGAPyvevBuoiHPrSoNDp_Kbck6o_VeCDcPAyOCEVqMD7Fc1ia9grWBEhxor9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpYrMh4j_c1zefnkS1D9n9ykHGItt4hWSrCItjwiy0nkoViiTmJar3YbMZrA92blnfD7CXDU7lZAcGvZ3Vkp1UliFSZQzA-OY2FDneaevw5t0Jrac6dDTPLokkfdTXDhYFN17OZ-fBuMp99Hp6y31SNYlNCT7vV3-zbTYAxZtNQ7YHQ9lywO4evIJj7mTn3oXs5vHtuxWZKIsP-4xl70o4J_AXtv-YqgqAL-ersNXES9WT6WDYAfczjGFwOWqIYM4b0GsAgIBQX7zncMmlMAQ61JvWxhqHvs-xlTN_mzHqIu6a6KDgsEaJeHuggpeRFTn1HAgO8xoVLmjaNCNo7tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuBCisShCIo-F9HlvbWgeA65jrD7k0iryI-U-pC5bgxuCiH-h060MAPCHWFnm5ZdS8hFLWCzaOvnN0HkBW-AV6jCHp354e8lS5NFSMHYbFRJlPsToM9xQisC7X6D4mHd105gTBRi8f2pmItLNtiVeNrd6Wg3nLhZUBpDucVFgFrJx-W2ibp0sQQ4tsUHhVdrzTnKWPkQBCPhhUYSr6DiBRN5vK7QgFRaXadyjJfKyE-4myyzZXiMMrETtVLsxZMvH1BxX8yTiQAKx4VHbAL7S0mnMhmEGWI0mKBru1_N10xfdzX084kw1VSIp44bRstOcTwYgCaD4nAfcc4numfL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-y0ZOd2C2Z29s24X90DxSNvFIEHCzXGvY3BivQlU8ZKvFvzEBF0ZcIgmhlDB8YD1SxIm96sVnKwu2XIMJrYR7iUswyw6UlyvqZisOYPgi6y3j5bH_Wj6_1cQMNab4o41C9Lb9UYRDFXe8cXDWIJ9ZqoL-HSohbADc1FOTnuI0vwQlb1FICT0qqWP9uXV6SUGTB8Ncje2pXg59B3zY980cFkKndz7bLJz0KnlnL_Pvt-KCJz--WaB-izAhHAJEI0WSMzYejpvtejJrPN4pK5SO5dbOqAsD2pEHH0NiOrXqm4MtqGfvn81Axhm7AUlgMr6gGobNKXs_jb7gHgp9hMcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=wADKt-mvCR-W1Lv6_6Ae-IZj0fHJtpM3MMqak6qg2f2UqXKH0QsJ7dLLG9qjMS1D_Kji0v7i9CJROz8WB6UahEMpzNe60-4YUqdP7Ft7r8lzrLK2d_MgWC0EWyee6avLDjOMrga-6mI6tDIRQNp1BfEQIFpLMHlPY62dGfWmRrWUk_af5zfXrmDKsqikS1LWrsmw0fCYls1dlTQFUHlDVBGWpzq_vOpQ6nazKPZHai-qCIN_wW5cg6RDi3ucTccGNhryKMN5umuYbNf5p51gTEliEbv0Gjq6MZbRi4oOKN7MBJFejj0BnlSJdJ-8gs1hHkvMmc4kBDxuEI6jXaOwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=wADKt-mvCR-W1Lv6_6Ae-IZj0fHJtpM3MMqak6qg2f2UqXKH0QsJ7dLLG9qjMS1D_Kji0v7i9CJROz8WB6UahEMpzNe60-4YUqdP7Ft7r8lzrLK2d_MgWC0EWyee6avLDjOMrga-6mI6tDIRQNp1BfEQIFpLMHlPY62dGfWmRrWUk_af5zfXrmDKsqikS1LWrsmw0fCYls1dlTQFUHlDVBGWpzq_vOpQ6nazKPZHai-qCIN_wW5cg6RDi3ucTccGNhryKMN5umuYbNf5p51gTEliEbv0Gjq6MZbRi4oOKN7MBJFejj0BnlSJdJ-8gs1hHkvMmc4kBDxuEI6jXaOwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=b_ak8DPUlkeovNFjZIq-tl-BIdlcG3C7X-59Tq3hJd3WLflRvmysbo7A8i-FblcLxKpF5CkBKZ0ltl7Q-5zyu12kIvfZN555hyUFxPMcdGtm2zLk59U6baFdc8WPjcUZeTtpUw06logQbUAKW4zGGq-sBYJCEEyrZKGzOfcSiyYJ-OQKavgxcPqxoLGuW4HuOvSyTmavUIaDLxIxR10auMGQHqszK5zMsmCAqExvCB3ZA5_cwWTlmT-tKbd5pLgm4ktdE6Kjd0nd935vPb_5BOk8bteQo-cRTMZ6dpegVrjpYCrxv-IfVnl0tEdIxOwlw-X8oap0NOZBx9xi4ch83Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=b_ak8DPUlkeovNFjZIq-tl-BIdlcG3C7X-59Tq3hJd3WLflRvmysbo7A8i-FblcLxKpF5CkBKZ0ltl7Q-5zyu12kIvfZN555hyUFxPMcdGtm2zLk59U6baFdc8WPjcUZeTtpUw06logQbUAKW4zGGq-sBYJCEEyrZKGzOfcSiyYJ-OQKavgxcPqxoLGuW4HuOvSyTmavUIaDLxIxR10auMGQHqszK5zMsmCAqExvCB3ZA5_cwWTlmT-tKbd5pLgm4ktdE6Kjd0nd935vPb_5BOk8bteQo-cRTMZ6dpegVrjpYCrxv-IfVnl0tEdIxOwlw-X8oap0NOZBx9xi4ch83Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGa79LD6uTrv3_h69zyiMquZ8Q_aj4AbPQVy7aRctCZIvzwH6ZbxpmwywPAXK_isFB_TIrFw-2_wmlHsnQWrIJyftCFlLioKqdnxkdT22Up0rlEsrwgvWM4XNDrwiLY9h9KIK6eE_4lZm4NWTbsyJvyWNYNY99v-cbOSYlmjzs0AHm63cBdhGo1we248KRr563dYeosd2_IVohbXc5cqbXI-rvJ5jfJR4OJDvSvHe4V9bcMVZ7gIdtIHY12yEKW3hWUWVlm5xSURnWNgIY88f6elDs6MINcEhy2biv5Nx45cicPHcCfkRhKOYC42Hy2WdGbgaJC8bGPzfJwuJCMUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENiU2iY7I-FbRofOP3fHDv3cd94v0RgVW7ieYmDds7A6AjARZUguy3WBe2QnPZSu4Zw10UBe2wXq9Hbhg1he_hdmZTVcHNktw6o7bTLPj-o6yiZRjxj-OX2bOnqNAV4fnr-B25FKAKXfmTfkbvKMtQRx25QdPDsUTRrAUPXCPF31jRqa0w8kbetWwX94lbaujre6MOkVFYYosN32P4NfOG45rFVrHDTMjCobSkosLHpDdln8x9Wc_yJymjmVPI_Vw-VP5O8hw_0-Cv4WkJH4sRUfkPug2wAxfZk2D4OZVWm6h-4R3xc-cBASaBqJbgflygWpbAhOk2o34nt_mfVGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrVouopV76ugPHm_Gv-t0Zcutv2CKX9F9ZayWGRUy02c8pftWgBCOepY2GdR1VPchXgdRM9VCEw-wB-nTjFkxk71wFSVP2xmTl1jKadHJdnHSW1OFvfMHXevLSV-OVyAd7tmvpvXTMmWJPe86QZ2fBknNAErFeSTjHg2D6v3_ULR9TXTuimuPVzJqyVMMca0WGq9Py6eJckoXp6lgpPoViF1KMiSXvCYdMFMh5Ng6QM7hvi9BMMvidotO3FkSrrUAhSSu7Gtta9Un9qzNmcjVd9cWpsjSSA2O2RkTkehrHOL8BSboUqpe6Low9qYLT6PSugvFCzfPWKU4fLxlbxIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLUGrTOeHQ-FVG9r5GUgagsx_8FQJLFpg_JNYh8zKETdHlHSqjy4ku-Lh1Fw_f51m1rklh-Gq6Vh3xJSYiP6zSmURCBmVxaieVPkNw6IZKx4gZYWYYAEV_WpPK0KAz6ziu3N4vczpJSK1NV4_zQcUW7IULcuJrufuhsCobRhf2pgk8EajrmDJbIdvgDc5tgkAe48EbU3OAgjWUxfrRz4PlMqRtR4WVUeTAbF4LZ5PhibXo8bGkA0QWwl1jfg5LlUZYC3UQVfT12BVDXRywXTmXi86TjbFMH39NiRCJVtJiTHlWqD6foyR2ze_mHME0Yvl6GmnVlicBDQfb2M8zoIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=oIQCl6ws5EXL73qATtQWvL4iGSI5xharGCabILAgGhSibe2iyRUxMBUpcy4thJzdc_iQkNDZY3-0vl_ePJMpe7dxi0UFp3yGinvhmdIsfn0Kgq-aFGrq0Yc5K613ATLhFtJfTpTtB2n2oDaTzCV2xYSZkE3gaVESXUhGhj4R8jLqTCDjNm81jzX1ubX4Vl45iqAzrP22zzAxUkqqAx5pG5aELKD_qz7Z3Ol5SLbOy79SqmWTBSzP1xl96zhIzvWW8TwcBGAy1_fv7qIwfDggW5mtYKEPrW1sg1eWJozT3HAx4-4p7LojKs2FannvoWzihfA89sxFYL4SLE_ZBVSxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=oIQCl6ws5EXL73qATtQWvL4iGSI5xharGCabILAgGhSibe2iyRUxMBUpcy4thJzdc_iQkNDZY3-0vl_ePJMpe7dxi0UFp3yGinvhmdIsfn0Kgq-aFGrq0Yc5K613ATLhFtJfTpTtB2n2oDaTzCV2xYSZkE3gaVESXUhGhj4R8jLqTCDjNm81jzX1ubX4Vl45iqAzrP22zzAxUkqqAx5pG5aELKD_qz7Z3Ol5SLbOy79SqmWTBSzP1xl96zhIzvWW8TwcBGAy1_fv7qIwfDggW5mtYKEPrW1sg1eWJozT3HAx4-4p7LojKs2FannvoWzihfA89sxFYL4SLE_ZBVSxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQTA4_s6fkSqFFEp3Y1XuA4ZAxMmpR9DkYljWCvZkgX7o4gJshm08OyHo0QruVaPToLZatWQv0c4w8D86s3sFrL66yWlHiQRetnkQhIKJO3dR6ByTS3rBBQEMc0TMLPQut9GGIScpX209LStyPKpm_e-50uSCtyXERqwUvf53RIJgRYNScjzoI77cOYpE7EgGK45nILFCcDaFHjFKDIWdAudrLQD0-BTrfQeeIht7NSST1Bkzl3FDDmx1-lxozlkutwBTmH9eJZDt5Ry72Gg_HTKT3DDr8NrugG6Q8DMQKpH--P3BoEacPxgUXil0z4e-bTbUCxtDm8qaOEAw0K1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etj15dbN6m1B_FlhWinChP_dBmqOK4oph6h9Cc9UtPB3LZr_nKCFobkG9XRIkfTRH4FBKeldkTJjb9mjPqdWFFF4dqmNyyoku4a9qGPMA4hsElyHm1czbSTcLqkQXeEImmAqDEsP0rBfaU3NXf27Xjl8b3QXJHV4iHl2rqDzYqTb3hKAPvjmJqPPz4nMyIP9H2dATfXmgkC-yDWsOW9xU155cApH_3U6W7WnMxNVZsi34cUP29v0MtkAprlRqKcAbIEKf878B21ejas0W7HDHZk0-PVus3ZEsrmM7gbWPfhkunivHIQIOsgavK9XP6iaaEC-6h3da0L8Z4T_3Kh0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=saL9v6Q6sUkMVaDgfnKYSwZ1iL38UXDuEOrSlEcYKAIRpb0zvcO3EHcjnA6_lvxNPLgQONh5lEUapq9WWup79hcEA62rg48N6ihuyBaY1FIWzVaxwYR38tuvje_o3WGTLlD66nAWi1x5XYkELdc2zvBGxRSpaFZTML1Fnj2QY3SN4PH7qr3N2wQ8mwvOyDj0a9C4sMeCzF4zXPD0pbtT36sDjyh740nQ9YBlO6pFXRlSzVKQZYe_BV60V_AluLAvHaUYyTCBPW_vrbMyupSNI7EdLonlFGu6xxBjZXLRRFIbyl3_RLywoY1butRLrspB07ngA_v5grW8VtfOs1MmzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=saL9v6Q6sUkMVaDgfnKYSwZ1iL38UXDuEOrSlEcYKAIRpb0zvcO3EHcjnA6_lvxNPLgQONh5lEUapq9WWup79hcEA62rg48N6ihuyBaY1FIWzVaxwYR38tuvje_o3WGTLlD66nAWi1x5XYkELdc2zvBGxRSpaFZTML1Fnj2QY3SN4PH7qr3N2wQ8mwvOyDj0a9C4sMeCzF4zXPD0pbtT36sDjyh740nQ9YBlO6pFXRlSzVKQZYe_BV60V_AluLAvHaUYyTCBPW_vrbMyupSNI7EdLonlFGu6xxBjZXLRRFIbyl3_RLywoY1butRLrspB07ngA_v5grW8VtfOs1MmzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfM8C92CsHgETmWqjeI-Ey6zWnuSmmYw-owQysT_bIkX22cCK4Y-zZy3EwkH7gx2QcBTUnK_TqLR_LIVj4vJonWDQzoqV7jdrrpcRwM9m_StXZILXN4mB_ZjbUvakj2D1ok7AIlD_b9HjlSdCTxNhzM17Iwg4tP_KqpRucdW6ix8wn8-SKJ5AkGbhcVDfuPYVYsn7FMHUbHBmb06DjfrTbxpAvCZWMHxgkmuH9qQes9lVVMPjdyOzrprcFC_69VEs64ZfpFIcAWqU-GkeYFHrS5cHNIAxiIibD5jwWEnwoqnw6bPpCJBUyMX-GjAhRakGUNDnfK4L6-b1kKDvKP9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=EFoiURHACyICps6EqIRCImfJ6Luc6fUZOfYwPNe6j4oFNMDeM00ZmHqZecZ__15nnBe2FrW3abE4PfdftOc-y2D2PaRDZS6XAODbR5awFFb9Omh4HTown0u0gyJiK-yaxCJraRVsV9RCTtQfZmjDSRlBDF5GgqvUnVD_ORZjhbrgJNFmuC_5LVMAnDYmeQNlByojqqBP5U7iRVrF5kzwwECDVPrJPpxEw4eiZSgMoOY4MAPeE4iB_rhxqEHSYYgcZrBQCZT5iu5ooB8GqSmAKNMLpcUoPES8y9sCBNqKh8t8rbOa5GEJBMfbCLSX1Pw7mFNpWtCzEvAecd_3lzwx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=EFoiURHACyICps6EqIRCImfJ6Luc6fUZOfYwPNe6j4oFNMDeM00ZmHqZecZ__15nnBe2FrW3abE4PfdftOc-y2D2PaRDZS6XAODbR5awFFb9Omh4HTown0u0gyJiK-yaxCJraRVsV9RCTtQfZmjDSRlBDF5GgqvUnVD_ORZjhbrgJNFmuC_5LVMAnDYmeQNlByojqqBP5U7iRVrF5kzwwECDVPrJPpxEw4eiZSgMoOY4MAPeE4iB_rhxqEHSYYgcZrBQCZT5iu5ooB8GqSmAKNMLpcUoPES8y9sCBNqKh8t8rbOa5GEJBMfbCLSX1Pw7mFNpWtCzEvAecd_3lzwx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=phXpQ3AEtE-Mz2YE8nVwhaX4hOFu_K2SDwEHC7F4yl_Xqq-9FA-tV7bPxh5StY-xm6nv-s-6RFvYATbsxtxA5e5y1nhhcQAKHwnG66yybwYTdSoXFXCfrfoqYh2JhqsmZFYm0CrWgJ9xtADX_6WwjJOssaKG-FPRDEnS5nEx5GMchKF4d0rst_JX88pFjt9V2TmieXN1C2bfHbb6xMb6SFlYEt7F1YR6MpWMKLNCL33wCNgoFfk4cDFEN2oSHr5-LKENiiH1CUnAsNgsffVhfJkZxbq8ifMOottIC-xlHD7dBJxR61xqUVJrQEWYKzPnDBCZ0NNc-rl2F7X8Fn4knQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=phXpQ3AEtE-Mz2YE8nVwhaX4hOFu_K2SDwEHC7F4yl_Xqq-9FA-tV7bPxh5StY-xm6nv-s-6RFvYATbsxtxA5e5y1nhhcQAKHwnG66yybwYTdSoXFXCfrfoqYh2JhqsmZFYm0CrWgJ9xtADX_6WwjJOssaKG-FPRDEnS5nEx5GMchKF4d0rst_JX88pFjt9V2TmieXN1C2bfHbb6xMb6SFlYEt7F1YR6MpWMKLNCL33wCNgoFfk4cDFEN2oSHr5-LKENiiH1CUnAsNgsffVhfJkZxbq8ifMOottIC-xlHD7dBJxR61xqUVJrQEWYKzPnDBCZ0NNc-rl2F7X8Fn4knQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=CG7wdLprlQcw22tby0HZIBgN3UY2aRV5vk0CnjwGSHlT2fHppmbgg6GnYFTT9BcnpPKbaH68Len-QJez2APP-2KfgNV_fp6z7qvOxNRR4gcSKBTOPEU-2UNj6GR19hxl9VUIJBMEr94X9IDwViw5owMAr4KNjoFkjPuwZ97r78OZZm3hXSC4cMWsJVO7Vl0ydipM1SIfpxryIUxWwlBnOwqj5-GmHSgSvdGxaDSvOLQnKycxGmvzu-x1mG1cyRIGO4VyWggc3XxQQO79xl2o-Akgj-59hRLDwNJjxZKDbH881IjuvfDO37pynvXEzQnZqj90v-OE6XA8qUhALWNnYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=CG7wdLprlQcw22tby0HZIBgN3UY2aRV5vk0CnjwGSHlT2fHppmbgg6GnYFTT9BcnpPKbaH68Len-QJez2APP-2KfgNV_fp6z7qvOxNRR4gcSKBTOPEU-2UNj6GR19hxl9VUIJBMEr94X9IDwViw5owMAr4KNjoFkjPuwZ97r78OZZm3hXSC4cMWsJVO7Vl0ydipM1SIfpxryIUxWwlBnOwqj5-GmHSgSvdGxaDSvOLQnKycxGmvzu-x1mG1cyRIGO4VyWggc3XxQQO79xl2o-Akgj-59hRLDwNJjxZKDbH881IjuvfDO37pynvXEzQnZqj90v-OE6XA8qUhALWNnYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=Sn6aUvdRj9J1dtByY_32FgPesFe6LuDfbRnIegjwTst2dcuqakNch1WifHpVs7UcCfws7wvGfcz0aOOhn1bHEsxzpLh4twIMGIOJIbHPUpQJOm-id2XQOx_yGNZmvmGlU976s1z3FhlGw7bjsQyA01U2sJwdrbfRMFzGkw90bg7TK5PHukh8fTXI1hBlD0AF8zdCBudIgV8ktMk1WX8KIE1NBcSa3mwlvxEh5afPO5MQ13EXC2C8y4P_aN4By_tdABCJHgkAeMo8Bgd3r3ApfPTPxZu_Z-OLLHtMH8Ro8MB0gOlxOczAJuUiNw2gfjD0x8qPJCwwd0yjAyfXLEGBTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=Sn6aUvdRj9J1dtByY_32FgPesFe6LuDfbRnIegjwTst2dcuqakNch1WifHpVs7UcCfws7wvGfcz0aOOhn1bHEsxzpLh4twIMGIOJIbHPUpQJOm-id2XQOx_yGNZmvmGlU976s1z3FhlGw7bjsQyA01U2sJwdrbfRMFzGkw90bg7TK5PHukh8fTXI1hBlD0AF8zdCBudIgV8ktMk1WX8KIE1NBcSa3mwlvxEh5afPO5MQ13EXC2C8y4P_aN4By_tdABCJHgkAeMo8Bgd3r3ApfPTPxZu_Z-OLLHtMH8Ro8MB0gOlxOczAJuUiNw2gfjD0x8qPJCwwd0yjAyfXLEGBTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=RfiLNrqR2NzSYV2RGsunwXsoGtXCyjPzto9JaP7I6SfNzTKPmR_zbvp63CQGBQxe7cV-Lqz0qUIj_uUzjeIPPM4ZUGrfFG1CXyTUKe45FptiKIUvcWKQ8ptFDUgA33ioyRHDnxjj29TfRUKCDwbZUyddfGNEWA0UTqtdPZ51_GVBfmDBiLAE2hN6xVBVORiq5cMvC1WTXAQ7z4H_mHkwt2yhtDhuhLlSSnQ10uw1ZdjWXvIxMB9HN7WCkleOoyK6kiDfScC5fIjoGqM0ysyQRpGjnKPHYDB-E0tdKD1zsYk3GwsKYnMoposQTmj-MgS_AMV41iII4U27P38T2OAlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=RfiLNrqR2NzSYV2RGsunwXsoGtXCyjPzto9JaP7I6SfNzTKPmR_zbvp63CQGBQxe7cV-Lqz0qUIj_uUzjeIPPM4ZUGrfFG1CXyTUKe45FptiKIUvcWKQ8ptFDUgA33ioyRHDnxjj29TfRUKCDwbZUyddfGNEWA0UTqtdPZ51_GVBfmDBiLAE2hN6xVBVORiq5cMvC1WTXAQ7z4H_mHkwt2yhtDhuhLlSSnQ10uw1ZdjWXvIxMB9HN7WCkleOoyK6kiDfScC5fIjoGqM0ysyQRpGjnKPHYDB-E0tdKD1zsYk3GwsKYnMoposQTmj-MgS_AMV41iII4U27P38T2OAlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5XRdLtyREH0sA4TgNNWutBOZFdfi-RDAuEbyjlWvlTl5zHoUAFTHexmSX-F8UQ6TXfsC1Z-VEuv_ubhXovHllBEIL1MtSuswohk3poOyynqxZhDjtUCF7p7UN5Lc8fZSTE1CVeG-vWdNS32440uKYihb-Hp18PZrgH_Kn9XxQa86rBhrhXBh_eNCy1lrC7jebmP9qJYNyQq_Mu5Dh6gmGJNIvgAWQ9Fdp8RW9oCYtgQm-url2opw4fAtkzbULsnYVWFbVFiERYUX0Fb53PUtyCHR2RI3lKnYHkHHYFw2kGZoKaM_lPWkYuYCgaCC6-7Ip0zWjnILGfRjSGdi8Y5Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVQPVgX_a-MiLzktTrXjOiVdO-Q0Aavz9_DkZ5OllfnVKrWFL9FPvOYgBofd9UpZTCgwuSzQIWYrNQYQzS-_jZ5S8XXH7Ba-j0zIJdHpx4Mf1zmcqnmmJT1jE63tQfLZ3nPIEAX_zHpyY3LL_yamBzdbD_3cXZH5etZeiyJx2EqEYhtk096h1z2pUYloneN_RzQA0IFvi9u8s8EI5g_SK-rf63X2uCQYlncR5e0Fe5jc16PtGS5TNVpnOyGCEh8tUSJf6AQXCE6FfYi-PhUrDckPoq4MgOHOUL1CFsYM6siQL38nFl6qPY65X8kgBX0b7bXW4s8sIQEZFvAd0VOjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-Djpm-EQrWgIRMSXVvEAW7qApO49KRnkEQq4bZCBczDPpvVqVHK6v3hqJEdCpHAHx30Udjqaxo7xZguiKwroK0Mlze15XZUQC_Z4ODZuib8qWRLsKXNSFMD8nIvzUZNoWHLFx-yTAlGR1zrD4nusxe8kAQGA7Ns1gG6IUqolZeitPS4JSgq2lxH7FedSz5grGXVr1rTRG8Ll94UzDK5bDBlejkiXcykyYPQOoIfqyoz421EQd-qQeGZ-J7l6pWjt7ivOC9J9wxSy89AhYh7oq2mOdk1MfIITH08hIsKbnqJtDO449ooUzQJzVM6MhjQIuKG2TgrQiRZdFzG-Z7F6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=SpAgBb5pQvLraf6Opg1ZBvcAN9wP5og4mGnwm-WBCpwcWJm6JkM7tj6HfoVjsEsyrN_xhGYdU92q5a1yolp3yiwSWE0HYh7fcuLyT_vRrO7w_IDgkFSJg3d_HUWMRk13C0dy5it5ztknAXjJHKiiuWq-GayrCwmF2UoC_26_DU-jvlZ6kQUy1BjK6hhEK9H6jJ7QdwJ8RrLOsSfDat5F490C4Qak5LQa-w_P1NabaRELDVVphb4bjkOUOibwGvEJ5rqCKpTBfDxszPBx1BlvdK3xWXzfYvRPBtyBwvkwBqd7DEY6TjbKFpcHwzBrO_4xucZ9-F0BOCgb59ftHoxj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=SpAgBb5pQvLraf6Opg1ZBvcAN9wP5og4mGnwm-WBCpwcWJm6JkM7tj6HfoVjsEsyrN_xhGYdU92q5a1yolp3yiwSWE0HYh7fcuLyT_vRrO7w_IDgkFSJg3d_HUWMRk13C0dy5it5ztknAXjJHKiiuWq-GayrCwmF2UoC_26_DU-jvlZ6kQUy1BjK6hhEK9H6jJ7QdwJ8RrLOsSfDat5F490C4Qak5LQa-w_P1NabaRELDVVphb4bjkOUOibwGvEJ5rqCKpTBfDxszPBx1BlvdK3xWXzfYvRPBtyBwvkwBqd7DEY6TjbKFpcHwzBrO_4xucZ9-F0BOCgb59ftHoxj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=R-g-wIUW9gQj62Fpn31IZuzGtDUvYety-K66f8VUBMZFvDMO6s0MchhlgQlpZ8uGxhkgtnZGqDgEDmD2Mw0eHbQUSt1DVLu0yZuTyDJiod8KdKMAaVfU0rOybYYNT1yJ-rAelZRRcMp0lNjcqNAO_u3Fvwshq-6_2XCMo85TmzJRzUFjMZdP08ss13pCZvUYMM8Ez3JRPoxyTQBNj4T-uS1Lj-8m-NTamopasd1Ao4Aw9NQCymIYv41wQV68BheOxvJNtmXyjjFcNPMlzFOHoscsuSH9vi194oI5nt7CfPLUnuNQusCgQfVw71kiug-mEMbfR6vUh55JIENAo2q2Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=R-g-wIUW9gQj62Fpn31IZuzGtDUvYety-K66f8VUBMZFvDMO6s0MchhlgQlpZ8uGxhkgtnZGqDgEDmD2Mw0eHbQUSt1DVLu0yZuTyDJiod8KdKMAaVfU0rOybYYNT1yJ-rAelZRRcMp0lNjcqNAO_u3Fvwshq-6_2XCMo85TmzJRzUFjMZdP08ss13pCZvUYMM8Ez3JRPoxyTQBNj4T-uS1Lj-8m-NTamopasd1Ao4Aw9NQCymIYv41wQV68BheOxvJNtmXyjjFcNPMlzFOHoscsuSH9vi194oI5nt7CfPLUnuNQusCgQfVw71kiug-mEMbfR6vUh55JIENAo2q2Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Ci7OiDgRJicZsqFUQLMNZgqZ7bueF7nQkdg2pFK15TAfxvFlTYKFi25TN_jEcg9IgINfUetmPlLa0elKiu7vXphJ5DmKiYz8o3d58eeDJxRm7saiXZL8yiHgSPiH2V2pwXzoVDCGtsCuh2pHBn4ti5XE1htYztrUDvr50NvrNcTo2zJMw0-HpJUuydTmcwXixcmRRXZcyVMOmC-ipIt8oD-WY8nHqGWARtr8aRrRbB3dpqHeVyCv-vWVX2tcITLZP_LUfrRVg9Ga4Crt-Yoi4lW1r69HyppSdhBPj0nQiSZCwRj3aJ_43dsc3PdInusVb_28YOZ27YYWiaXsK5x5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=Ci7OiDgRJicZsqFUQLMNZgqZ7bueF7nQkdg2pFK15TAfxvFlTYKFi25TN_jEcg9IgINfUetmPlLa0elKiu7vXphJ5DmKiYz8o3d58eeDJxRm7saiXZL8yiHgSPiH2V2pwXzoVDCGtsCuh2pHBn4ti5XE1htYztrUDvr50NvrNcTo2zJMw0-HpJUuydTmcwXixcmRRXZcyVMOmC-ipIt8oD-WY8nHqGWARtr8aRrRbB3dpqHeVyCv-vWVX2tcITLZP_LUfrRVg9Ga4Crt-Yoi4lW1r69HyppSdhBPj0nQiSZCwRj3aJ_43dsc3PdInusVb_28YOZ27YYWiaXsK5x5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpYbPyM6mFr4AeqE1Eu_8uetmVkrWYkHXTjyIVzFdnJ0xKPfMKfH8xyCeWaO3rfJzbAn5nXuV9AK1YpdzpE0D4cIKtgYc_YWXlCkSUUwtPVGW0FBkMDf4scQyXK_Bhd2mgz3s4bbtmjMiHzlYovaTVoJIMtnJP0tTixRUiz33n_dPw4WEi0eFM7ZJbNfNW-rde_CtKg5XzFktrewSiomwuOxOsVYnuOVEC_ZiRu2Ws2nnGUuRmVzZRVYl_Z-YLVrQ6-7_soPyYpFILqGkyNuCh2yLFCY0irjK3tyQe6wgRGG5JQwoiQzSv41DNR9dNr6QISN6a_AwhwG3LHzeGSj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=kJqK3CW7BniIVf0VZQj435DcEnUgJXxjLXO5NOwX0BBk9S1OEX-5S57c0iABj2x-CAMCzHvac12q8H33knu8vIhTbNQpYCy8vC6i6xrfJMGQBQbJw7OXExrbCkvXgjGwv7VdwD_5mtH60w0IDo03FO38byY03m633BPd4U-V2fqGggUpI5Q4NJUWg8Y1gNha4oKhOZvOtw5-Hs3VMtk0MTzPUbWUmSVFjoHNz2KVu05YY7zWnQ0uNI6rxOuy5AKrOR6igro30Mkrch4vo-z9rxKBpVDoRSgQ5GbYWlrswKLzc7G-NW7iuuMMQ4CE-oIeZFO_bggMuUTPVNZqOXjT80Jw7EUxQrE5gkAZL15KVjwTL0ICzCcpy4bjWpeiCX0Hs8YTlNLT_E55LXvAmQ8-ovlXLBBkOw4yvvzR_8yAsbVlwJ9IsS_qIN4OOs6omZz3KNDaLAoSMgwmFU6p_A28Qi42tA7WvGhJOQt4LedY7wNJix08oHa1rNYKLwkY35lheBgq-8PRLq5v80wwRQtKHCV10ET3heLp8QD4l8PLcvKYK8rJ085BU6x3_HNETHOt6naO_lcwAARhBgvGAhnJPNYgWkO_W6DJox1wv6LarnQmbdKhCYcvUmCr_ce3glZLMxTkksZwp-oVQM4-tgcOLTNsg4-WDw-oLk1Docnskss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=kJqK3CW7BniIVf0VZQj435DcEnUgJXxjLXO5NOwX0BBk9S1OEX-5S57c0iABj2x-CAMCzHvac12q8H33knu8vIhTbNQpYCy8vC6i6xrfJMGQBQbJw7OXExrbCkvXgjGwv7VdwD_5mtH60w0IDo03FO38byY03m633BPd4U-V2fqGggUpI5Q4NJUWg8Y1gNha4oKhOZvOtw5-Hs3VMtk0MTzPUbWUmSVFjoHNz2KVu05YY7zWnQ0uNI6rxOuy5AKrOR6igro30Mkrch4vo-z9rxKBpVDoRSgQ5GbYWlrswKLzc7G-NW7iuuMMQ4CE-oIeZFO_bggMuUTPVNZqOXjT80Jw7EUxQrE5gkAZL15KVjwTL0ICzCcpy4bjWpeiCX0Hs8YTlNLT_E55LXvAmQ8-ovlXLBBkOw4yvvzR_8yAsbVlwJ9IsS_qIN4OOs6omZz3KNDaLAoSMgwmFU6p_A28Qi42tA7WvGhJOQt4LedY7wNJix08oHa1rNYKLwkY35lheBgq-8PRLq5v80wwRQtKHCV10ET3heLp8QD4l8PLcvKYK8rJ085BU6x3_HNETHOt6naO_lcwAARhBgvGAhnJPNYgWkO_W6DJox1wv6LarnQmbdKhCYcvUmCr_ce3glZLMxTkksZwp-oVQM4-tgcOLTNsg4-WDw-oLk1Docnskss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyOmQ8KBv-uh0vZvCLGjsglY3cmx53bf1ueqnf3fpipjhVHq_Fs2O3yuJQMU66z0902qSdDwrLHkpt-HALUaUSwJkkOvfBkGM_IzHfxUfrCMfetv1FGnSQQW08QYCFCLKPOEgQGANnM7xGLBD0Ds7mVZVdStiE58Qf4xPeVr0keOybndPRpjle6k_GYxuJENpBMt-Qfp6Q23DQxEqZ4pgOlmmPZSK1QYTKZGZFJ4MBAZUsMTZIPYycgtVnay5J8mkaAa7wPbrG5BK9ptUqJQxw0so09ycg9Q5Dg8vEOv2l8LiQtE63kfVgb1VSdVkZL1s0Bu1pBMM6eZV8erAo4OHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=OnCZqMhx0mV8q6y0GNvOiE0YPv6hxpsGZzKbzfoUT3oN-KmE_-Pys3Mi0ogphru7aQ6QhsEOwXZ9-ClkuWAtOdHrtUNo20fQndqbkX8aFXbagUf0J9di5kiCfUPPM51KO21tIb1GdwMZSWLxzMZ1U0tru3JeITHDzcU83-R9P9JEj6aC5CU68BP0DePHXC4L8eO2C0Qz5sk8ADlZ0Wz10pKWnQOV5DX96hmjBW3_lcWs2Awq3l8J35IsCvyXZjsXYJwVDvRShZGzJm9oBdAFhfvOkQDI929y2S03TROAA4YN6D-0SIeP_TUfGcHrQkm3tSXktj-e6NbyDNUxEeDOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=OnCZqMhx0mV8q6y0GNvOiE0YPv6hxpsGZzKbzfoUT3oN-KmE_-Pys3Mi0ogphru7aQ6QhsEOwXZ9-ClkuWAtOdHrtUNo20fQndqbkX8aFXbagUf0J9di5kiCfUPPM51KO21tIb1GdwMZSWLxzMZ1U0tru3JeITHDzcU83-R9P9JEj6aC5CU68BP0DePHXC4L8eO2C0Qz5sk8ADlZ0Wz10pKWnQOV5DX96hmjBW3_lcWs2Awq3l8J35IsCvyXZjsXYJwVDvRShZGzJm9oBdAFhfvOkQDI929y2S03TROAA4YN6D-0SIeP_TUfGcHrQkm3tSXktj-e6NbyDNUxEeDOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM_Tl5TfgHNjUgmubIXXYGN5hmruscun6AnKGzjtJn7f9dTMtHbrVaND6dGR2ocEx5NX3qq6AEW1_8tziEboKb9OQ8fZte6ve0QStDki5sYDBuZykmTmA5G-4EGaW7ejIB7ItF4zRgHvu-Yn6s7tqHKS7oCGhUzN_ceI5XgOSs0ej1TVhzZ48U98oNEd2t0uG0sZ7dlTumhwZXjaG3E8z4F0Cc9RYC0B2_wUk9vNLcxyfZsIwRFUGJ8_pLoWuEPVTLyJTQcVda79L0kl8UmkogmY0NfbjiWTYlisllL8Vm-PugM0CrQqzHwexxBlNFfXjjoX2UNcJ4-hOXC2dd99xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui399YquzlHxBdgU9Hn9tJGvmTt4GcVNrspjiAdOdJXEZywK4ahufiWLnKb31qSI-1_30xbLyPhsDygn5xCxQDipAJl3wOwXJVnzxcqO48tTaN9qc0ThNLFHqKHijJg7EfhDDXxhwSyzQuubIBaQTLnapNXOdW597GR8dspkF1ui0NtltTZSElbfPME7sLHx2ikUgYcdUoFehcdm8cLycnhB5W73PNtxGScrc2GPC8FXhID7OanxtRCdGoXSJsZrhfkpk6EFAt9KNqhOe4JsdyIXDRK98LPi-gIr7ojq8l-qBLwkz-lTI7F3wlOS7aTiX1Yod8L9oB_zQzg_CdtqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuFV7horTqsZ10EzVluGy_AA-z1ps9olrxjAYL4XaM6PiiTytZ_DsD1aEqoZh5dAM3EFzesO_hitaPTj4qSELgl58lEHeBckCwjDHkqJBMdtfGv0OPWr-MZTMKcj1kTzSGGy7tlrfYB96sS77CHx3ury3LaH9wZxklvaH5Xb34yDeXvl2WfFxjAhvNHhe-CjT8guyxVf9WieZljwOkgh1aZzFKtpuHRlPEiLEVkuPfUm8yvlt6OxptzEnIq49sCgU0nWy57T-TEPFHfGD_GSWKlDf8K8ZEW6rzWbtkUQlLlilGXgYGEXrPFbK_sgpmpg6qm3IJxDTrfcfRFHlaVF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYr73x7NZoduqYtQQDH5MSydIXvHCanVUtQK2vovkOCQCleWEvm-fFsUomHzJF1Hj3qTsZ4HDVFCF4v790xxfhj83noiy3lT3NEtbL5sGItOdMt5zxn3RWP3ML7yuPtTj9c_G43Gleoes3FKbZ-JnVefpt1Z7bBBBvG-tEuKcSiq_cVmfd428LQwHnUnz_BuduPxnAfsyEtYWg-43v0E8_eRr7zEU9ehgHMBDECWw-6YS1ZIeu_wSkVXJFICKBuZlnXuGW-5HvhZt6OOUDdht4YmMGJ89S3uViWTyPY0NeIat9SUJYRpceaAJd8OewlOChBPUzaghu6JAVTCmf_VxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jviVEqy5QjV38LVDjPWYYncSWd7ztJq6sUuLjp9U3D0PQS8mE5sIWYXQuKGvfmNU1dEj7EX-1j7nJtu6cqCxkxLP2Z8zukVBa0EfmFp3l4DC4t5QIUtsBtijFN76ArPI84jgPMWXx07LuCderN8n2W1M8egbyyDlkAZdYn1SSu_ToTkKrUMbn-aVQWGUADRLbyXfn-oXLIrQzL2d6xROpfxQDH5YGWXHnLnjqbhXVZEhhyqLAAPtbm8iTkClSPWpqPx08Frg2_8vI_5c_0Xp-J2H1pUZj-eqe_ajHZoaD4yR4vcEeGtdzeaVm8zuaDrzdbW35sgA8QSd2eFWSE1x4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd5s1d6o2F2puXYzH_y4aGgl_P8vQ4Ax4K8OStWrF14LwmqTTUkIhybYrbjXj0MzwaBiPxAklnQDNiFXmM5CyBdgPcpUkN6A1cxA411Tg-X_vA-ECaoH7CA-sLmtKOWSf2sRYhMcpviAAeakqR0M4LBKdG6bk_BSu1mE7o255uXKSPEIWQrvWBErdIEWlmB6KjvZTY6K1_Kh8qkGltRtUvfTP3KMHII3InHMFZnPbVf3Q2Fx1l0kVOCnubihSLfdIoGN-G_LdZeZ8gC0KJTv0OO78FDeRdIQmKpWjzyKdXFUraN8sedLzyBh-n__hH8qdFkjw27Tu2W_4KZiHbVpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqrrtz56jDyuKUuCgdiXusCG2e_fnkEXUf47i0r3qCyQUdnHBZ7hDyYPEtKZ97zPK9acPbV_OUcKWch9TA4FxeExpbOPZJ1T6OHePqdUR0BtrhdMRQfhkOp2OpXfDU9-GlNWK0dQtodDHjt11o3sTAeRj3A4T2E_f1UlyxgtMX0_39iGlUaUMMBa1OkQIpg6QSwavxrURDJDgbtDJit-Qsj0kAOMFfXKg-rhJmzeH730abHihsFHkdUP012sPTDvIbfUfT7tXIF4z8r28idBOLxqrGNbvqrUHDNKnbyEyXvF2pWmARgOicV5sKSf4R8aGjO-4VrOmXCUiFH3RSPSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
