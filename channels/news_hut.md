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
<img src="https://cdn4.telesco.pe/file/LP84syQkixBjY2HgrjZmL23Lf9f_T2CL_5XYZ2pi2UwzHAnG1YmR3exAiZ2g-4YA8BmhPaTbrr7IuOh2M_MLR1xWvg9BicYjp9dZ76VQ0jatZIGpfxdj-0-b7VXjTaUAu-GT3yZ3C55NgtgbkOBq7V5XGLjzfjm7RR8aB9igjTpMPzRI8jLJazoleiMlX7oeqtobxE_hDP2pKfz75F1T6Bnwh4MYm0yz0cDcvnDibXw0lEmFh-dFhq7i5aqtbX5TXAyM7R9HXvNqT48mlBKYB1N3yfRSII8ruHZ8tSDyco0GBPEphfU6CRwwF4TkW3w6jJyGrWG0UnrDzV1t3bt0Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=k5RPYTXIoyW1ITx9SGMwNn79iNX6JYUTZZ7Vm5icJwSORYU4MmRlxv5Y3YUm-oEx8wCed9NRvGceaaru0t4qvJKL-miEdKQuxoxA25RyuTYLCFL2AojB322VhyLUoxSCswqpUP5aBb8-AxITMhiK2IpmRKCWHmmeI6QDWM9pZakp1oor1o4qrC9VTSXcsXzF41YaEy_azbzJ_trucuCpXxQRcIVSO16Cj_pLwmdQPlgc1XXEYnnrqbIrFVgVfJ6fypn_FE9_A9wcY22A2-pGmvE7y-3YELdTIdfRdE8F6LuYzaAfft8bFGN3TOjrKwzotIdGussGGS_w8eg6hVhqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=k5RPYTXIoyW1ITx9SGMwNn79iNX6JYUTZZ7Vm5icJwSORYU4MmRlxv5Y3YUm-oEx8wCed9NRvGceaaru0t4qvJKL-miEdKQuxoxA25RyuTYLCFL2AojB322VhyLUoxSCswqpUP5aBb8-AxITMhiK2IpmRKCWHmmeI6QDWM9pZakp1oor1o4qrC9VTSXcsXzF41YaEy_azbzJ_trucuCpXxQRcIVSO16Cj_pLwmdQPlgc1XXEYnnrqbIrFVgVfJ6fypn_FE9_A9wcY22A2-pGmvE7y-3YELdTIdfRdE8F6LuYzaAfft8bFGN3TOjrKwzotIdGussGGS_w8eg6hVhqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=G4MuFoRjX2hHxtjgTH9f6fh400sUz73o-HDNwLK1F70TxPVfMUArY2Utpu5DQwoRAEzGa0di4HNmqPnwh2DIHcJfCt6CuKzkQcV9UUvnXRVXo9vKIn4ohJX2S99cENwLC1XD6q5IpnJwL3QDXxF0V-n_TUwqrnRqOD-Zz7lWFbRdQG34WcjVu2Nq5vUV9aFdMjxvXtiAZWPCWIbmxGdhH77WSo-V8E0Gl2Md8glRL3dvrNc6omQ8y6aooy-HtuKTbkT0TUmvhk9kO3xyrA7YrPIYFH286xDFnc2KOcPSDYgwUv6M3ZTPRojsDUxRC_pUZ74PB_PDBsHNyRSu2pY8ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=G4MuFoRjX2hHxtjgTH9f6fh400sUz73o-HDNwLK1F70TxPVfMUArY2Utpu5DQwoRAEzGa0di4HNmqPnwh2DIHcJfCt6CuKzkQcV9UUvnXRVXo9vKIn4ohJX2S99cENwLC1XD6q5IpnJwL3QDXxF0V-n_TUwqrnRqOD-Zz7lWFbRdQG34WcjVu2Nq5vUV9aFdMjxvXtiAZWPCWIbmxGdhH77WSo-V8E0Gl2Md8glRL3dvrNc6omQ8y6aooy-HtuKTbkT0TUmvhk9kO3xyrA7YrPIYFH286xDFnc2KOcPSDYgwUv6M3ZTPRojsDUxRC_pUZ74PB_PDBsHNyRSu2pY8ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVmg_gR4y1yriq7JLA71eDENl7McMb6TwM0Pakaaly1N33SIbar7rucDsetA4oUxnNFZBgWOl7Iy0O-o6cEvNJt6_IorlyheP-HSU8nWt5l1vaeUpUPg95lOjYvO9Tn6rsWROYj9UzmXfQ17BSo1AS1jv94QuNAyrgz_R3NaK0VCy1hOr1NJ0a2335ATJvddJPX4EbXH7N4M6oDU7Lf0a5KF6jizJb5z6X-nrbd8wmsJ7JAlbSUxTJUwv32J3LRcj4KTNilk8dOsTCVCHIixXDUgYilrdOe-6v1wcb-JzUChF4rcnGwZYD7assKd0Ps7WIcPwa6SSttioKjQvW8z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2qqpW4KoBVgiCVEOdNYgKCNcsSplf57OqQlhqRLADRdmd6KVloqq7I0eJpw_rNjh3QwCKn9HWSwxEoCm2e646zDU8j9lGpdzWwfem9wZEGijzZFJSSorelMdhuxKfFJErncIMBG1bgFXC83SV5GU5BJVdnvKW7F8Emxg11dnjdr7-FuPwl_w7lrbMfkk1E7ujCyRUv-jXIOOAMCSEx83iRN1YtjMRZ-uqrxhC7YL0wUdCor3heZf6qpGEcJ-EajwLPsCLNLbv8BAVhRkN9vJpLtV5R35z1YrC52Bx9FDXS624KMA_Oct_jUD3CRmCEfiws8YhEVqwj5OGS9Ferpimro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2qqpW4KoBVgiCVEOdNYgKCNcsSplf57OqQlhqRLADRdmd6KVloqq7I0eJpw_rNjh3QwCKn9HWSwxEoCm2e646zDU8j9lGpdzWwfem9wZEGijzZFJSSorelMdhuxKfFJErncIMBG1bgFXC83SV5GU5BJVdnvKW7F8Emxg11dnjdr7-FuPwl_w7lrbMfkk1E7ujCyRUv-jXIOOAMCSEx83iRN1YtjMRZ-uqrxhC7YL0wUdCor3heZf6qpGEcJ-EajwLPsCLNLbv8BAVhRkN9vJpLtV5R35z1YrC52Bx9FDXS624KMA_Oct_jUD3CRmCEfiws8YhEVqwj5OGS9Ferpimro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=YMu-3nNoLscIGaDkK8_uL7d6gAqSiRSCOL47oLsUXXnKYtdxQQnS1cjb0GUTQ85zb0zTrqAMcuft4jgqjhkuU8fPJmIgmPNXo9Tok3S71VHSm2CXS2SRiOB6lZtkGVD_GYi-bFLdd7twrNXI09u35nDGWT9etwHF9WEhh2Zq6cOL9O71BtAmpXAD_Eqwe1K3mjyK8VKjpsUYV5T7e3u3kNe0e9S3cmDNc82xbKI1a16uzcmxSiXBshsV8MMQkX4VCJCxQoPWafgJ6NvbsIz07plVcYE5KqWMw-f1BBNfDIlvaGABA9-d6kbJgFzDxHaNmLlfdNn6iSxeOl4lMLkzKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=YMu-3nNoLscIGaDkK8_uL7d6gAqSiRSCOL47oLsUXXnKYtdxQQnS1cjb0GUTQ85zb0zTrqAMcuft4jgqjhkuU8fPJmIgmPNXo9Tok3S71VHSm2CXS2SRiOB6lZtkGVD_GYi-bFLdd7twrNXI09u35nDGWT9etwHF9WEhh2Zq6cOL9O71BtAmpXAD_Eqwe1K3mjyK8VKjpsUYV5T7e3u3kNe0e9S3cmDNc82xbKI1a16uzcmxSiXBshsV8MMQkX4VCJCxQoPWafgJ6NvbsIz07plVcYE5KqWMw-f1BBNfDIlvaGABA9-d6kbJgFzDxHaNmLlfdNn6iSxeOl4lMLkzKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=grbQ3w8dC_rVYANqlj5MVg600NVeWA67rQp4yOjiFyT5GK2uwWao3Xwz_UuWX1d-1KYYqCrQufjTfrlRly_01c1wUl6667w_XFYUf4qEzPfC6ZWzFTwkUnzdRDA-QsDUemms3gGNaprCua7UZU3yVog9YYrQNlCPTTrA5wvXDMDxwqG8KwzZeLfxnL6C7Ppv9b3YJpo46kRP5CcKedQPrUhm6ShjfMNrlwMgiod6vepNFKL5vQBbOan1SN3aFPNDTH3rYVEZKvRrYI_cA1JkauqENjstJ-GNHHLAta-K0-5Jdk8Pl7sjf9shgSv9U_uZSF88g4gjG9K9pAKWYXokJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=grbQ3w8dC_rVYANqlj5MVg600NVeWA67rQp4yOjiFyT5GK2uwWao3Xwz_UuWX1d-1KYYqCrQufjTfrlRly_01c1wUl6667w_XFYUf4qEzPfC6ZWzFTwkUnzdRDA-QsDUemms3gGNaprCua7UZU3yVog9YYrQNlCPTTrA5wvXDMDxwqG8KwzZeLfxnL6C7Ppv9b3YJpo46kRP5CcKedQPrUhm6ShjfMNrlwMgiod6vepNFKL5vQBbOan1SN3aFPNDTH3rYVEZKvRrYI_cA1JkauqENjstJ-GNHHLAta-K0-5Jdk8Pl7sjf9shgSv9U_uZSF88g4gjG9K9pAKWYXokJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=aeF_7O3dihB1mxPYO7aQdPmLEjWAF2Kxa1Zb4U2hGjiO5JeN7ziF1FgcahiG17a_r_9aC6fLXTXLmi-NfEMNxy8lKMvJn_8xUcBYK_fbr1EXZLl_6OfKhu8MciXWLVi-KwXXLXosjLS-hdtMIIIC5ZKnOa_MVOq82KXmqvcWz-l279oDrF5OTEHnw8Y9gubX-4SgTmTap1lwm0Rn5lN6QjMctEDf_mV4RPMMPcNhuoDqBiBF4St3XnBlzoF9084oeFW9Fp-AMajC87B3Y2S2VI1csy23ZkHHDm4YQZCMrMA5ALLfyZnlRTz2arKUZFUfgm8xgoC-GUt9bg5YyGJl9bGgkQbydpWCV_Jn-TS_WUGPhOaK9ImhkR-1ycyRXJlVLw48sJkqccmvyhn5k6Dx-TjspNUaPYSPYUKHqxn2SBK3UZUmN-NRAN3BLDae7aNLlDf7g3rkSDbjG2iZIFarVFX3EpAAthQqrCNnGW_rx9yDMGC57jprUaveVfqQdvTzFL1LEXyRwD4HTv62MPrdv7wYETgU__li1U1nNfZ2SLzc56NPqXZsVkYE2gWK-8PVdm00ayRNwXA5tIhzkKOmJ33Zso0QmzOYkGPiH7th4ynBktVECKqvCNM4wAB1sPU0V8l2oUiHylIqTfl1WoIqhLSS3PErSZJy_YE3OkY1IoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=aeF_7O3dihB1mxPYO7aQdPmLEjWAF2Kxa1Zb4U2hGjiO5JeN7ziF1FgcahiG17a_r_9aC6fLXTXLmi-NfEMNxy8lKMvJn_8xUcBYK_fbr1EXZLl_6OfKhu8MciXWLVi-KwXXLXosjLS-hdtMIIIC5ZKnOa_MVOq82KXmqvcWz-l279oDrF5OTEHnw8Y9gubX-4SgTmTap1lwm0Rn5lN6QjMctEDf_mV4RPMMPcNhuoDqBiBF4St3XnBlzoF9084oeFW9Fp-AMajC87B3Y2S2VI1csy23ZkHHDm4YQZCMrMA5ALLfyZnlRTz2arKUZFUfgm8xgoC-GUt9bg5YyGJl9bGgkQbydpWCV_Jn-TS_WUGPhOaK9ImhkR-1ycyRXJlVLw48sJkqccmvyhn5k6Dx-TjspNUaPYSPYUKHqxn2SBK3UZUmN-NRAN3BLDae7aNLlDf7g3rkSDbjG2iZIFarVFX3EpAAthQqrCNnGW_rx9yDMGC57jprUaveVfqQdvTzFL1LEXyRwD4HTv62MPrdv7wYETgU__li1U1nNfZ2SLzc56NPqXZsVkYE2gWK-8PVdm00ayRNwXA5tIhzkKOmJ33Zso0QmzOYkGPiH7th4ynBktVECKqvCNM4wAB1sPU0V8l2oUiHylIqTfl1WoIqhLSS3PErSZJy_YE3OkY1IoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=CgGIxUT4h0eVW7tXD8iCif-GTqm_pXfqaadut1s3AqdMJg1_y9GuFwjWBL0dhe8vvCyoO1e5UBu7URRpoVWuEU-SrfO6R5I8SLMUmg9ycyHfdoFTSYpuJtOj-0EaP-BHim_GtjT54I4kYXKGljx_00PP_uitW7HPBXNUJYbhLU1g8CtMV0waNYwqIYJi-Gt_P8UxU3CMgFFFi97zEda0N3VGai7-G5af_3pJ4b6a0x-lvuuxbbp1iU11VzxBwn69jZDal11dwpWmB-5QH0Vo3ijXLhT9IecsaMiPe4YEyak1G0A4so7atMbbsYyUZ9v2F31UfOsR3XoYEydtnSZeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=CgGIxUT4h0eVW7tXD8iCif-GTqm_pXfqaadut1s3AqdMJg1_y9GuFwjWBL0dhe8vvCyoO1e5UBu7URRpoVWuEU-SrfO6R5I8SLMUmg9ycyHfdoFTSYpuJtOj-0EaP-BHim_GtjT54I4kYXKGljx_00PP_uitW7HPBXNUJYbhLU1g8CtMV0waNYwqIYJi-Gt_P8UxU3CMgFFFi97zEda0N3VGai7-G5af_3pJ4b6a0x-lvuuxbbp1iU11VzxBwn69jZDal11dwpWmB-5QH0Vo3ijXLhT9IecsaMiPe4YEyak1G0A4so7atMbbsYyUZ9v2F31UfOsR3XoYEydtnSZeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=lBJlyjgGwQ7sgztRiJ7pZoWn--g6Mt41ZfXr08PFkQfSU3QE62QI7A7esEad3OqEOCPgrsZoUk1PyEkIpYaBuzZUJvAITpB_zzJHYXlugvY37J9Yseren2Jmd1CGcevoeM0qbZbnJbX8CP5P0cHWrs_pcMYdP_w8IK90oTGRE90CB92KBAJC0cQgP9fW0M-WePSH6FYZxDT6wnl0NW4StkrfSoec65Nr9TZxApPsicil8CJPhcGosZghNPixsQhqdVTXLni9vlltrcbWlDcDBiIS9_T2Ba2ql_WJ28jtuAWoZBTH5LzN96ZWycMrFA2ku1uw6rEbkLHrZ34P1UFeWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=lBJlyjgGwQ7sgztRiJ7pZoWn--g6Mt41ZfXr08PFkQfSU3QE62QI7A7esEad3OqEOCPgrsZoUk1PyEkIpYaBuzZUJvAITpB_zzJHYXlugvY37J9Yseren2Jmd1CGcevoeM0qbZbnJbX8CP5P0cHWrs_pcMYdP_w8IK90oTGRE90CB92KBAJC0cQgP9fW0M-WePSH6FYZxDT6wnl0NW4StkrfSoec65Nr9TZxApPsicil8CJPhcGosZghNPixsQhqdVTXLni9vlltrcbWlDcDBiIS9_T2Ba2ql_WJ28jtuAWoZBTH5LzN96ZWycMrFA2ku1uw6rEbkLHrZ34P1UFeWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=X_BPJr49TyuehEWFHsznXfqNz1WmsO42NwfJvNn9rE_rm73SvSsfpVfiU08G0QLxl9ED2fFYnIcr0PD9GLDifGMiZPuuRU1jrg3fkd3wqFCFLxnNc0XSoKhodPu50IGcqNKOZAPv7SoV_yNBv3Qkf2UiZXvkT3niYHluCx7o98pO97ROZOGwj0CXbHbqKP18Je0YU5p0xDnXUlophVDRjzlI2Ab9hm-zZ4Eg85qG7MUWP6O3xYLtqSC-qYgHOZqnPqn3Ga03xuAtQXD4DGmko6wwoZux3V8rhEq02LqqYnOlHyT1PVMVlvmlen7zJrzTH-xJh7N-B8sqd1Q7gUgCTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=X_BPJr49TyuehEWFHsznXfqNz1WmsO42NwfJvNn9rE_rm73SvSsfpVfiU08G0QLxl9ED2fFYnIcr0PD9GLDifGMiZPuuRU1jrg3fkd3wqFCFLxnNc0XSoKhodPu50IGcqNKOZAPv7SoV_yNBv3Qkf2UiZXvkT3niYHluCx7o98pO97ROZOGwj0CXbHbqKP18Je0YU5p0xDnXUlophVDRjzlI2Ab9hm-zZ4Eg85qG7MUWP6O3xYLtqSC-qYgHOZqnPqn3Ga03xuAtQXD4DGmko6wwoZux3V8rhEq02LqqYnOlHyT1PVMVlvmlen7zJrzTH-xJh7N-B8sqd1Q7gUgCTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=NXUufTkOyrjrLz7OFnMgNgz0p-OY-1Y4hwn9IZkBdXz8naGyFhCB7rwmqmGzl_YqaBHuZn2MIY9xP5zLS7xNm-5oBic2B-tLFI_2rEqxvubt077OZnVCUM1fi6QUPIqcb-TQDAAe6G3Yq5saRVwsQoNLOYRiLKrg-OtmesLgzHBGtwQvvPoRnnnF2ifUGYpeuAejp-2nzM5Oq_a6ieQV37dYC_eSTYEgWFaN3-FG6W5XOieceQO2ZCFHSOer77-G2_w5Vp11xKGL1TI40H9yCAC__kYAOb_fxs98jSBxJs4N52VbNZPk8JtNeeEdzHQiHIXfGfvZpRIfXgo4EnNffw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=NXUufTkOyrjrLz7OFnMgNgz0p-OY-1Y4hwn9IZkBdXz8naGyFhCB7rwmqmGzl_YqaBHuZn2MIY9xP5zLS7xNm-5oBic2B-tLFI_2rEqxvubt077OZnVCUM1fi6QUPIqcb-TQDAAe6G3Yq5saRVwsQoNLOYRiLKrg-OtmesLgzHBGtwQvvPoRnnnF2ifUGYpeuAejp-2nzM5Oq_a6ieQV37dYC_eSTYEgWFaN3-FG6W5XOieceQO2ZCFHSOer77-G2_w5Vp11xKGL1TI40H9yCAC__kYAOb_fxs98jSBxJs4N52VbNZPk8JtNeeEdzHQiHIXfGfvZpRIfXgo4EnNffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1UluoE1fIeU3E_Z8BaSNzkxCQFPtAShm8_FnGCUbt8wlv32Hjkz8KLbFhF0b-hgSVdfrGNVY0R_O4G6wSeqVMQi-G8EvOn9erXh4rnXfpJ1S_m6JYwcLv_V9V3UuvCwXrqXJ49_ClQEVm18s_FeK8U5XEL7zBPKU-dhcQmLHsJQDLlFMP6kPjFLTIqsgzPeCPviWOeInIK796cCGoidqG1T1muXRl2RTV7UhzsV6CZDuMOlKn0-RKkMQMpmnThCpLe0dsVA4uZ55RUZuBHW9JC-nisU9aiZswW0sdlSBmqEKLrhHQLpzXfriQeWBngael-VNOxG37GbJh4SA_iLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx75gObLxRAJ53hwe1kJR9pSwWovj9nfS5ay0foUR3LcUy8affv8TnDcEcG0CWwQM4Eql29lmL5msxyVHvGHxsfzOHeY2VbKOLL5J-3oR-by8Z1dnuwqsbMKAYawR7CS9JVYofwRQf9UVQH_0rDWJopTG_kt3fc_bHY4Ly3P644cydhPb6SxKkRRqO0wBtvAa2kyzqzaAo8l1WChpnAVhSEd2ruC889XD4Ci1jhu5XIlaa57wiQhblN8B2PiEPC_Cw6hx3q5Mw5iD1C4wwhmjXEmJ8PvxWv35JVXFOljY3-w_BaIPco5uSKzVhi4mAEODyBa7OOmqczjCXGKbc73Gf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx75gObLxRAJ53hwe1kJR9pSwWovj9nfS5ay0foUR3LcUy8affv8TnDcEcG0CWwQM4Eql29lmL5msxyVHvGHxsfzOHeY2VbKOLL5J-3oR-by8Z1dnuwqsbMKAYawR7CS9JVYofwRQf9UVQH_0rDWJopTG_kt3fc_bHY4Ly3P644cydhPb6SxKkRRqO0wBtvAa2kyzqzaAo8l1WChpnAVhSEd2ruC889XD4Ci1jhu5XIlaa57wiQhblN8B2PiEPC_Cw6hx3q5Mw5iD1C4wwhmjXEmJ8PvxWv35JVXFOljY3-w_BaIPco5uSKzVhi4mAEODyBa7OOmqczjCXGKbc73Gf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=mnfAWjUCwsBltOs4t4_1t61NCKTfW-qa8z6wpVMzQpU24-PGBnZ-g4sK7gJMd6CNVv_AH3mBFpgUiS3hcIS5eAsAijoTOhYDUXvJdFX9WI60KyP64JpddY9kyYelxs0p7KAEO4a03MbZPysnEtp4pV1sd7rSWSTkl3JhLJOn6HbnIV2KByPiYFhm0glOQlNrdfzNGvGUpekPqeoJOsIxNIG-0C5ToWwfpkBmV7mC7EQ8miHbW3cqdrHmormEoKZ-kQufUGYyzvwzaARDohdPeaRXonHV-oiYj_l645fSCguXBMQoUH7Gmz9MzWHElKTdnQVTW_tiVQIWs4KztjE-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=mnfAWjUCwsBltOs4t4_1t61NCKTfW-qa8z6wpVMzQpU24-PGBnZ-g4sK7gJMd6CNVv_AH3mBFpgUiS3hcIS5eAsAijoTOhYDUXvJdFX9WI60KyP64JpddY9kyYelxs0p7KAEO4a03MbZPysnEtp4pV1sd7rSWSTkl3JhLJOn6HbnIV2KByPiYFhm0glOQlNrdfzNGvGUpekPqeoJOsIxNIG-0C5ToWwfpkBmV7mC7EQ8miHbW3cqdrHmormEoKZ-kQufUGYyzvwzaARDohdPeaRXonHV-oiYj_l645fSCguXBMQoUH7Gmz9MzWHElKTdnQVTW_tiVQIWs4KztjE-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/po2b2gf0qMuyYpObaeOByn_gzPlDu9at-8n4a7hFPBBhwgGpZ1rW-st7n6zyLJ030qCrrNQVkWbAj4HRdIBjq42ebZ6oASRAqezakZ-oT5B6NE8Op3IemTbnUii5-z91QBu2hh0K9pUqAY8UpEi4z2c84fMOk7ClCIDtkZmBcpX3jVyoSToF7tnCoNhAMSPBcw6K12fEJfLYdIhdQDizpahOXADNl5Mw8VgUZNO76KY7dr2d3FgrFY1pfkLfWBZInDPjseuuuQXtixOVBj-L114nQ8fcuUfT1gZsDpm5cKrQa2PK04TrehscsHHh6iIUl5inL_t_gaTWN-BG8MLVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4GFBCOvTAfQfvN1oGux-0QDOCkrO8E0EkP9xDjqAzF9vEPAtNhspvzAoxyoarzBCbkPaeyB75bwWUda_U_O1DG7EKHM6w__iIC_2xSELmBsQKGeDKySuqTyuFNWFWEN0Sl1rJwxqJb4y9oh94WQWL054EMwQ0y9P00k81E1fAN-NNdvDOLU0wTDRbu0QhYeCLXnazOZLczPE24xAUgh1sZo99gzH81-8gc9tlhaiskvNW11ccaAWTIXi1UaqDJrsBO354SsLF0_wasUmY7zULZsafVnyptg0boN7uRGfpUSuwV3MTMU8d7sGfLKXTNRaZRXecZ_xMyijOvZItIsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZTKDKWWDsHesVkiZ-k9gzQtzJpk7OLUT0NS16qj5TwCf7O1Pc_XhmSj131eSmCZ6yjUkr6VyI8KQvbKB14FjvOm5hTP5yOkusNyzOYT4zMMdZp1ltP-lK-EuV6xulE6w50aeBfBYDQ6cxMclUs4Ldxzq82k_Za1l3c-q22GqYDSWrDEzHzZfZzkMFsqYWwc04CWA1sHh0gwhskW-erHBnSH5V-7C5-PEp93k90Ob4h_RSmFHsoHaEJV_JjDW5NjDwmxSW2SgFAKuRgnuD7fCNXgpp8v8v9_NHasujjYnsvZtl9WghA5hfVA0onpa1zd88t3jZ_asazT9xfU9yDHu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_FyrzLWP8sN1EZLXn0tRgFbMXPByNL-u_Tm17RZWj0x2vTAxO4OYnkQAWeRFKosnWOrg0-OgLyAS5Xbzjs5sjN3lMMnRuXyiM01tqQQCX2bBzYHpL89jbOtSdqRqyjp7tLcD3oi3UudyOSWd5CzhvTgydVTL9HWibrhsjx4whg5wnyRoEj0cLTFDOPqGv9_S1NMD2o-yYeJ-mn992yG9aliuEUKyFZVlOvFeXqYBxWEAfx7Je4uO7lorNr4YZuGad-MSGeBBuKZEci7gSygLNdgxWvYW3TzOMdGHo8BgTpLZMIsCWGQ0wl-FwM7meVYGABDVT-aE64PutWA5bIs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWo3MLBoJlLaqk657NyWrma6CHqFeWuHr4OuQa_1qquQLqPHW-Q4P_GDMVRJnz5-oWJSUlGxpyaQvAiQ-AS05YUtRWqIER2pYavd9spyflrOeJM2ndWlnilLn8WH1rLRsw7seuXntOqFs3ztZqXc_x5EFO_7OrHTjac5UJPWEMEdgQ4bVrG1KNcdvAc3xq-Smoz094EQUoLXXMbYlDi69HuP97lMS3XmLWgLDSivE1_eD9c-dwi98N92GjcQlEos4Ag5PgvNG-an1SX-5qMQaV0erxfUPrGRWqlzhCLc4ZblLpApElTwhgT9nuVJtNdFsnWqdEpCPwqbils5-YErjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaoFcsOpEMS_ghTwfZI-8CNbUQjL2QtRV304VMwH5IKgwAfPJLySOeVciHLshzscsDoWNN6yJXvgEJ4yj5l1Ykcy_xvA2GT94d0fd4hyCQ54t7i6_nPmIr5DcGmHUSVOzroMKqFqDdvbecDhO8L16upCa87CqKJDNp74SEd6OCp1j3SQCNruHddTYPMPue5oG0PyF1ewtPxSQ7ey8b_1qaSjfDZXixwootGVuabC2r4IYAFwqPTShbWutwKkexCIVGa0_S0LnBNT8WGrFV4sIOr1m7NVfMBmQnpkRDNchjhoBNpljTDUtLxoGsZRV7MOzzEFB-uzGUjHd-ImcS2RbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqSPpzwDdqKNWHN7TTmwnoV9HKjAP2xw7-WfZ9Jipg2rXo17J2dj7AkSWloQ-3VOEyDqDwKHIqauyrpKXLIxJQQGsvNUvr541sAi-hyCu1CQGjGi1I4G4uxTlhUDsPrvxbfwdOsvhP8J1I3sTazB4_URyednQJkeS-a3Gi4pZZFBpc1M3yUPUoJ9DUYfM7pyNTPJRJk-sj9hmQzXoOJFHaDcwuQZLuaq3NTtkWslM2YuIliJx6JnzVdoUA0XjUHk8oOF5I5KoecossoXzYT-jCG6hWXOunF7UjZzxwB8mbtvU1z6jryMi3x05NUv3Q9u-hvhDS7CfHxSQhWpmYb3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=uDs_hMw5MvYVAi6oFUlFNIvBJy63HoFNIWek2438XhOK2iC2bsEV6IvS54wxXfOaFVkvVkmgN-Kx8_Jk2HxoxHsWQT94YC6PkhF2JBHpwMPn9-Mr9c38C7_nfFlsSjnSzybS0k6o6XykNB1y_ZfjZuuU1HiqgrJxXJXmNSgtZPWvgmZx8rsIByWdt3mSii_xvcx3J1_8MLuW6wLj-8sWwJErBx_tvXeY0wQ9LMd9bpY1j8uTsO_6gJS1IPKRUQI74wcSwb5-EgHgPA7XkIzvcIb0ZNBmsN2Wdo9h61sYrqoqYfOb8u5sLB0SoszXSrFwnOkC5BHKAOaaqIJe_8ViLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=Dy6HyaZeFOgJ7xoi2cPdwU2wqH29jEwUerY4SFIpcl-vMKL2f2WBIVfxQ0_dlvN1rPIYKBRJuRJaqSyyuQeHmenCL69kUHek717T_Die2m6tpr8dR4vlGjKna0LIaCTeynqIRQq6y3z0VtMQPUcnyDoDAZa0U2n7FGuZPCZRc4fU-82yAjyaZh-UwB6Mw_WYkLNDrQZVOSgME5gpKCQ46B3b1EXUkMNUpJ70gpX0V_xSkO-IcLqI0ExH6Ce-o2GZv2BnWS3e51RvY9efgDtpxpzQuf3BoTQ7Y9gaZsWIqN0Xp6UPEUiW_koroZJy_JO2ce9mElkpvaQJWf_WPvYZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1jXhcYJ4FY-62Y1EDt47Uwfe0M0KpKsAFEmyBZRbcLgPRK0GiAHPlJ67A6EhruGxIgOpPAmHlRZX4nEZuLRcblCjucjHnMMmIl7ZhcwfQSOXY_7mfBAE0EjwC7GOaHEGpP9SI7RBEd3jdUjNp1kIGi2fPXBBCs3Wz8pD5PMiueZgznBw7TxgtNjLHkrce5xho6wXnwr9Own_Fb7v0ZNepnvwLaLf7AbZWJPQzEeqgZcETSbz4nsjGHKrAP1SGv1QeVZOCE23S47kxBW7gNL_BVaTPJY56xvwIAPtG89LG6eR3cD3FEp-aeV7ApIjapguQwK4e21lkq8GhSU0MB5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=AodPMVCX0R5w0ldoYkrWVw9576f1gYMNQJiOl0VJQ3S3QM-fya5bdOCKLHjbOA3G6-ZbZnXrSyxcB_9kU7ADNUGAb17XKLn8ChXG3cv6l_NB-YEr64tZMjCo4NVwagHQXxtErhPLx2eQcAzjVx_xo8pQ7-ijpASRgLkEikby5c1LPI-PlLiBKJi5UgwdREs8npXSkF2FRFyKoYJU3miuNzcQ8UC7eTI3K0T6v-lhMIgxGOfEoUiPKXmyQiaYdKHSCJ8EGe5IIuIXAvitEUbL3maBhnPNjiSFw9KsxVibNtN5h46PkZp-s3AihNo3nGgLhNMiyW0xkurr5zrNJSWlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=M6RNUzYQJSqzpEXK2EIq5TvtimRDD8oPUQZmJVnqLOf_-GGOqnsmz5d5QkYEqh9E1gL3T7WzXHxYzoRNBcnVc3T1U0wG35F8uY1XeBShWZcHGk1ta-WNYHVWWYy9X50pTn0MY3pBWWx03hoaOr4gMEeanzc1MXavKia_HZ_J914GncIMAdSiFLMVsdQnAKGMQ1VjhY38kl7U5Y-50cWzPwgroHvDHxmEiNod1GGvAwr5iVc5jkXDSICugpgyBIvXo7YC9IHmCDgFVC8FFOCnlGoLkaDc9mPM8kxoHSeIVua9Bf0L3CZjzRduk0DQP1AxskI4g9aG1HrMZrId4esQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJtYSQ2UN9cv4SC_t26uZM6OaQISuKa5sJUu4ZdwN2UTRHmVIXgfI3fEp4xeAhxtlDQe3uPCFeo2PNCM_KYi8sIxwW-vyatOifs8pRPWhMKY2LWSpYxFhja0Rw9_d1iBE8kcMZrkaKI7B5U-2i63IIsbi_MDVf8Jp5j0bLKhDzHfMdm3Sw26PbILgXLQv472bFJoKmHXe9IBdXIyFeWdXb0ghQUIjQse1dQRmiYbYVFQuo9YsW1qrKixuWGLDmvWVvOLdZNRrw_9xV8jyFcZ2sD0j21n7Geiu_fCnwLftAc64YmnopMLMkCfEOzlELQWreFQTenQX1kdkJbKUAXKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=ofLQutWYocIOGQ1HcsJgl1v0xb0QIuqHghtKJx8x4vcWXfL86tUzpdYlF9d_SppVxj7wwZatawP_6Tk7GAqTm7-cDjrvsZx2BtKV9kpyl44p-KXvSi8qXWBah1kVOqwkn9Ja7nfU0gI5NC0rHjktkSdd1MxJ2M5WHR4XrJtsEnHEwMEs-a74Oc6kstQJZzfzAkhqQCr44RpSf93B0MqfqJZ12IeJdH3bzZj8ww2HO6tChxXZbErnqXl2sbr3BoSNyr34Glc14hdGyL33tt-xw6Hmkcs5lw-Cnn-lav-L_0wIVvQ4tGmvOnzlCHX8zBb9Fo_5sKJpCIMoUrsg3FOvvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6-hk9kqnac494h7rZ_igKR6EMxlgh1Exv5dJljPOX4aqp0NsmywfmqGVLVCnYPDrlzzceQ5nSqCoF0aQLqn4wHWCWAtTsienQjl0uU417UPUO7PV3rkRaL7KXDCqBaWwaPi3lraqVyzswkESBZUtkCI1IsphYAsL1mPMFxgibnLaiB6AJlAazKHdUFaBd6tNtofJnAeAgJPkQwuN6l-jMsqxiYLXXsOQDmOTcidvXyOSFIL98TyC4LJ9yIFCWQGnv9DyAOEGLiXMhrd3UtgevTqjykXnJ48mtPQa4BI3TsgOQzDEl1ID74qsHInfRtMSU-vTukwOXsS7v8PNRu28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=WjRnHUgH4K4P0yukQvQXTb0_N91yQvdrAjJ5vnH21Yds3ADJgcfxUv46i76D8wcWFRtg-ghzswH7iqDk6JgJ4b6i2wuG0-LPxnve9bJw_J07tPDWNdrT2iIp2KSljiSFai1rNcc_RkZ4JJ-j_G7uRUEfUVu5-mZwoKhQFyL8XJ1SAojnM1OKbVAwKluLN9CW_apf8yEJsnojS-BPIbRfVvpH7_DxvCUCwjWMIfKrdptRVsO7Qa7B_oAV1uMPdk996EZK5ynYXtf0qso79aS8jCF6u7xCVurUSS62bLhNPFuQ-JjTxfJ1zfVctUGsllAUGzuxBTdyF7ZMOc2ZMUK9zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEupD3KIIlW_tZ1FCuBW0WxKD7eJwKPtTkN-Ke45HrhHXXGMC2hi1w0mD90QBBXB3x4EpCSlTvDtmzCOamgqHlSjKrAJtn4nXs_xVUfn7z9i72HO6G6-GkUfvzK2fu0YmZCmrdXOBdL-S7BAjP-_pZqRNDpGdOHwHhn3W-bjACyO11sLlGrp82tJUIDZXRYyr_4mmygp-717IXAiIRnbJkHkOTYCiCDJNmg1_lfxL6Kk-LgnocqUGkQDNpo--kTypa2VEP7iRRF4hgsDPpKJSEeLGllGuWjkf-AHCvMh34kxwqiB_HJKlhkj60DWkTza0-APu0rW2s1i34CHo29lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W49GKGbeuapW5zcWzEE-2YTHViuKYdi9A7wFlWYiEAviztJsYEUNkizMobrbyogsjSbUyVp1thBKAF8ejyQ_UVAX5y_uYKd4OfeYfRFP_rrxSGlXWcMWYmkZNhpIm0hQT1Cm-43oIuuzHjabmRP_vFXxN-K5qtU6tsotugmgXIXtMw_3cVJ-zhy9K3bfTv3WFMyDOfonJ54kj1Gpn6gH9tKVznm8C1F4Jdcuh16jpp-HaL1CscneQKdVmmLwLFSTCljFZxmcdUHdBR7rYDQYt1jqeiHSbJV8PuRwQOdel2lisHFBra_rHfXzqvte4Vdh-0GNCAwx3dzzr5Js-5-0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l52JGgqcO9vMjtHLSdws7PoBCi3IWA_VIqs0AOfM2ZYiBrOBPPoj5Kh7BdWOuD7IOTv7wkuXIX0-m6_uk_zxHFitwY8cX_HMtazljKmFH0CGcsh4SCc5zmHkV12N0oQSbf4dyj7LIdofJbuorlvuKBUhdD4HQhSja7CfUpupVh7nr-gXOAwPJjblpzG7YDWX0SvUkKVqNxFTt3Gg4Qis0g-7Qt_7v8qVOYsVQe_KUnAUr0hrZSsWFoaCNc59xcnHhE6YxW2lwAiKBwxTkCGZe6PWhz0WFzQ5PiH6bTqhoba0aoHBQXzI7r_K3Ckmtjvt8n9jPwUq1zEhHHAYLf2nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=gumrA6l_YGhSJv0vjpFfuQDvlrqYZf9uMsOqZDjmW086pQnNubiHZ3BqaUwXHeuCdEhCCeNHddLBCI7KPhVrCxVD7Kaz0-wY1k3Spzbq39_Qh48-ArWWsYVKRp5eExOPLuUuIve_M57TlLOGYNY4VMHDauTl1l6GFtNKidXJynwvYfIcZ7b--o1RT11ZKz90ujBx8wG-ar0mqVagUnbMHavswrTdO7rrij7nycaNGBcdJktu-YPZpHccW2s3BbHW3FFk4y9uMJIN1M7-TYZs5gk0DkMsDDSyRO_czAkvKaXgFv1qbioyaw2pFT--VAYDiRXeXMgD_mnqnNb7MVpLIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=gumrA6l_YGhSJv0vjpFfuQDvlrqYZf9uMsOqZDjmW086pQnNubiHZ3BqaUwXHeuCdEhCCeNHddLBCI7KPhVrCxVD7Kaz0-wY1k3Spzbq39_Qh48-ArWWsYVKRp5eExOPLuUuIve_M57TlLOGYNY4VMHDauTl1l6GFtNKidXJynwvYfIcZ7b--o1RT11ZKz90ujBx8wG-ar0mqVagUnbMHavswrTdO7rrij7nycaNGBcdJktu-YPZpHccW2s3BbHW3FFk4y9uMJIN1M7-TYZs5gk0DkMsDDSyRO_czAkvKaXgFv1qbioyaw2pFT--VAYDiRXeXMgD_mnqnNb7MVpLIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFzUjiBznEaDJLG6AokOAadLMEBrU2fjZh0Iwd-htt8OUBVjrxS3NTbLznSG6JWrFr2xihpD_K8T45wfdudRTlufaTPYQyjiZ7Ayk8QF93L7pGdS4RJ2SO2UOMSBPtvITPmzeZtu5RChN1DrF9_yCJU4004nRKPre4oqJm-ZUY7XaVqvQo5Qxv-raQ2hc_r7jryYxQGOMhiW-JapInNfIovAfqpwpt-Jn-j5cwgLqAdIlsEAcONF2m9uD9yQiXZfPVQhjYD86vXcS0Ae3RfJEDjd6tEuk34958Iocx_P9SmCzEGzjCTDRGUOSD0jTwK631JB6LATghmezGiUwEDLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrVmrzPROIQ5_DcH1afUQJ860sHvJWRxC2NAnmVEN38YuZQhyGHwdssPuNjJOftQhAc_gSydkz3ikt3tvtM1lR993GAS8f3CRPi5ME1ZlRwAQ4AKWK5zFcaZzJzgKNgfUiVxSQEIlOf3lUTzVREtJ9N_Ow-j1f4kELu3ztRUfGgsbX8oaHSJFpvPfsQOgmbj7J_pmdAzZ3-0feJ4z8qQ--dSiQeQEe9cNGscDHwUrK1jCrnv_wXt1LrqKUz5uqaPV1NuDDTWZAelVWm_MRS3X6p628SzOP7TmAYSoSve-MABW8z9LVIeE4BmODBdS1TTc0Mg6My3qd4bNVSfsNNoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOzxxosEZQRWl-eCZk1wJnbkK3McMacC_gaokCEtOC7uYMDyNgMsHlaMp_-KSj7IbGAa1AinHQaI990WRHfg-GfOuJIuksjRhGzRwWuza9tUZW65w6VxoJmQXqEhRTwADCUkUqHmG8F_yuN-wkh-FgG0dzAsakpWACfzTdB9jwByCIF36vrm2lk5P5Yvu5rOh8EInR1riE698Tubam8ImAAyWsu27zLWBexuJfyL5wO9JYyhwZH6OeIUjzeQTf1MJEplEFfarTl4GUT3zYGkyA8T-5zVMn_dKikf6Sw5jL_Nb8IPG2G7GhQvaEy2JtODDjU2dgX9MmUoQXCu1IdXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=Ly8whxoQpXW1u-aXmaSyEKbV0l70olJWJ2MzsgK9WWTilrfkF4XiMaxqa-LxZKVnQ_mjhKRM2tQaFl5HTXm9l24IPSNaNKfzr0joYQVcEONv_qYVa9RBy_93XuYN2NbuwJOB4vmYM4MAvmrIJf_bNIvhy3808MxUJgG7haJGRWT7D3f4izfAnVM7SK4y9RufHe9CiXiarcmWZnWrZ9dIA7ozKwTs2zJOzhowxfKiP0ArQsgm8svBGR3kAUwGcFglHc6DIxPQVvWI0sEIEL4UEwj5jDaMHSg0OuFvmTNl1RERjkKeT-aRkV37IKSQXvRSx3U2BOGAEflX9GElLfGeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=Ly8whxoQpXW1u-aXmaSyEKbV0l70olJWJ2MzsgK9WWTilrfkF4XiMaxqa-LxZKVnQ_mjhKRM2tQaFl5HTXm9l24IPSNaNKfzr0joYQVcEONv_qYVa9RBy_93XuYN2NbuwJOB4vmYM4MAvmrIJf_bNIvhy3808MxUJgG7haJGRWT7D3f4izfAnVM7SK4y9RufHe9CiXiarcmWZnWrZ9dIA7ozKwTs2zJOzhowxfKiP0ArQsgm8svBGR3kAUwGcFglHc6DIxPQVvWI0sEIEL4UEwj5jDaMHSg0OuFvmTNl1RERjkKeT-aRkV37IKSQXvRSx3U2BOGAEflX9GElLfGeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=AD65lDwQtlcX-wukvvzEwiulpvjdqD9eFrq7Xshp1k1lhpNDaZWVYSjfKoYZQbtvsDe48wLQFcgGcTmITWPB1Jet8ZKVW_Q_ETWm4f_9M_AqP7NspW-I1Q7oKjpoRMLMqBhlEoRe2ZEAogYDtVMhVlHj9VKyZDGTPM_8Nj-XcrCnJNQNyAIslmg1fD2naRC0h_OVNAP9mYIUmKjHKAXTm8TmzPf-4jRrTOMZbShv_3uoiEgx4w7TS8-lj1ywciaZbfh1l2221fRocq3dtjR15iV63jhrvAJD4SeA7sK7WUq07YrEQ2cYDJeU4I75KFM26sG8Pd19vM6bGmGEiql64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=AD65lDwQtlcX-wukvvzEwiulpvjdqD9eFrq7Xshp1k1lhpNDaZWVYSjfKoYZQbtvsDe48wLQFcgGcTmITWPB1Jet8ZKVW_Q_ETWm4f_9M_AqP7NspW-I1Q7oKjpoRMLMqBhlEoRe2ZEAogYDtVMhVlHj9VKyZDGTPM_8Nj-XcrCnJNQNyAIslmg1fD2naRC0h_OVNAP9mYIUmKjHKAXTm8TmzPf-4jRrTOMZbShv_3uoiEgx4w7TS8-lj1ywciaZbfh1l2221fRocq3dtjR15iV63jhrvAJD4SeA7sK7WUq07YrEQ2cYDJeU4I75KFM26sG8Pd19vM6bGmGEiql64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=re4rYjy106nIYVFFKQ42UPyV1Qbf9HQQc9oiR4R_SaszcwCdkzBmGQ_2nfvaAMMjokQhJWwRRKu_9JqbddEzLOvd09BuIN7Kti5qS__duyG7a6CF6KouEHaalzytVsK_s1WjslpOMfp_DXe8XpcmGdREq7WmdPzXtZRPN5yCaGA8clWhuRU6LretvwW1OUafCgjjO7Li-aRLad7ax-D_KrycS4uuaP4YhafKac38D1QVS8G09kQs_2OVUKJf2UUrPSKbuhjiZZLlbAzOqffWYHIhruUmrWvJ_StWewIMZ-9TSCrmCVuZ2pKShgSwfgGsqwBwmeDZqE-_fbnNfw5c9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=re4rYjy106nIYVFFKQ42UPyV1Qbf9HQQc9oiR4R_SaszcwCdkzBmGQ_2nfvaAMMjokQhJWwRRKu_9JqbddEzLOvd09BuIN7Kti5qS__duyG7a6CF6KouEHaalzytVsK_s1WjslpOMfp_DXe8XpcmGdREq7WmdPzXtZRPN5yCaGA8clWhuRU6LretvwW1OUafCgjjO7Li-aRLad7ax-D_KrycS4uuaP4YhafKac38D1QVS8G09kQs_2OVUKJf2UUrPSKbuhjiZZLlbAzOqffWYHIhruUmrWvJ_StWewIMZ-9TSCrmCVuZ2pKShgSwfgGsqwBwmeDZqE-_fbnNfw5c9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=XGKqvbGUyZKOh9kiKXN9bCmChAoyBb8T49uHCReiHZlIe3aNB-fD-SKrmWngF5Flij8_YhsM3XPwvlJ9plb4wTQ14DH2V1GCCxQQPTjogZCA7cBLjn1pwVoaAqLq-U2rEjUXDU2-cOsEGQXL1Pmh8vcjR7QiZQDfRtxcxqRc8N2v0_B-s1ggiUCSYek6L96q3IAk5hvgqpOwCgZQxyO0FXh1CEOyGw8pKTBfv159N2XtxDpQfRKsucHjnNFOJFQNtRJe1CMlgq1tX6uj2aQFuWw3SRETAegBbBX3qBzA6gHHDjwegsI17WOOvroTP-YxmhsWa8D1aMGgpwT1V7gzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=XGKqvbGUyZKOh9kiKXN9bCmChAoyBb8T49uHCReiHZlIe3aNB-fD-SKrmWngF5Flij8_YhsM3XPwvlJ9plb4wTQ14DH2V1GCCxQQPTjogZCA7cBLjn1pwVoaAqLq-U2rEjUXDU2-cOsEGQXL1Pmh8vcjR7QiZQDfRtxcxqRc8N2v0_B-s1ggiUCSYek6L96q3IAk5hvgqpOwCgZQxyO0FXh1CEOyGw8pKTBfv159N2XtxDpQfRKsucHjnNFOJFQNtRJe1CMlgq1tX6uj2aQFuWw3SRETAegBbBX3qBzA6gHHDjwegsI17WOOvroTP-YxmhsWa8D1aMGgpwT1V7gzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2_3XjOg17J43a6EspqmdV3y2RcXg833sBTfEStmrXCbfncjhRwdaiz718wRXW-OEWEZ0w9yLyhrHWSXENFkBbZG5SY0TjynmsUGk9kjLR8bLpH66ijHaPemPgIEhBWu75dOh6TGnsREwb7EZeJU-1eqbQdVmBdmfrTn-wfMwwsrNIgyT49x1pN0v3jnUKDPC0JOeVIVQY4xYh32hFVjvkntWH10Wp3hPd1V9G5dLa8SD-kV3UaSutio1ziVnTUxMR_juXdBFiPE1BVaqQ2O0IpZBb3ojZOHadbK88Ba1QXwTtdWuA4e-3nkyOcll7ck7KvyujZ7U4WiaktnP1zsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=J7QolHzxR-iA3M8m4Jed6alKEaIGNEnpZD7H6w9bmSLBKvxKz8NkqVlrxMGI3ZG_4tKNzqSbhbIjiZh9X8uk_iHSjpzhCRKfA-T9K0A6w84ZLvsKDyWasa4CWssFMS38Spm013thtsSI397SXXdojxIspy6ka6Z5EqMRbwW0VLAHcxTHsLY-ymIxvYBoJ-ypAE4F_wh7tFJkNT-gIaZXKOUG-19I0moWlvXsdrhrp8DGO49UXIpdhB1ERiQry485MrxKOzfoCCFxTgn84XcIRsXhBDeZXMHfGwXHmVyHF-6yFuy3W0YdS5FSoFXZRWzPyCKt2sBTlsbBUfGE294nTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=J7QolHzxR-iA3M8m4Jed6alKEaIGNEnpZD7H6w9bmSLBKvxKz8NkqVlrxMGI3ZG_4tKNzqSbhbIjiZh9X8uk_iHSjpzhCRKfA-T9K0A6w84ZLvsKDyWasa4CWssFMS38Spm013thtsSI397SXXdojxIspy6ka6Z5EqMRbwW0VLAHcxTHsLY-ymIxvYBoJ-ypAE4F_wh7tFJkNT-gIaZXKOUG-19I0moWlvXsdrhrp8DGO49UXIpdhB1ERiQry485MrxKOzfoCCFxTgn84XcIRsXhBDeZXMHfGwXHmVyHF-6yFuy3W0YdS5FSoFXZRWzPyCKt2sBTlsbBUfGE294nTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=LNjH_PlBIk42YWkI4F6jOhQUgbiLWv87cR2IFzoHbepxR9Ot8bvPMyfpFthusunDFyLviRDWiiY5JCV-EOWyRq0-HnwOmg63bv1QPYFykjhGJKrvGHC3fgcesyZAabkzcwzk3CetYODn8K3DVgucP95_Tpfh_p0lZYK1nBxyqh4SItGKWoSj2IyTo12nSOXj1jH5Qt7r0HhV8v5XwODr6In1UdlhfUe1LXqqUB4bmGrLGCkyjvnRZHvkLORQx0FZGpQ6EK-X961xySODqBojtWs72eHz3HqReMJ5Lb8cunojCEYek4aGeil8Gb8OquOUbP5z5FoqoYa6-Vy3vbh-S3VdkeWWvxw7LKVNziOeEgRCujAE5KSBy4NLAQ68p_wqbwsZ2-hCeVTtlXOtLqPUP5lm8vSFLrIpjIPV1omzsE-5dnVjGw2YqM82XEAWd4TaLIvZs6BgAkcFeqpVro9niKh3rIlidFbKAn1cqR_ubeUAErLgXzghQAw7T1XaGe46avG9PKNk9iaiOhPf8a0mbJ8ttR5c3RrU6ECA_hNJ2on4ZZB0zjgL5TBT4n_Xesqex64HXCLmzKrf1uD2MnkDB1qvhLUI6c5AH94k7ShsMGmTFK8Z4nVX_KfKZ_uiEKBH-y5bYJHVZnk_MEnFJ_nFK58MEf6Gi2PUTzUQ_DrZXR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=LNjH_PlBIk42YWkI4F6jOhQUgbiLWv87cR2IFzoHbepxR9Ot8bvPMyfpFthusunDFyLviRDWiiY5JCV-EOWyRq0-HnwOmg63bv1QPYFykjhGJKrvGHC3fgcesyZAabkzcwzk3CetYODn8K3DVgucP95_Tpfh_p0lZYK1nBxyqh4SItGKWoSj2IyTo12nSOXj1jH5Qt7r0HhV8v5XwODr6In1UdlhfUe1LXqqUB4bmGrLGCkyjvnRZHvkLORQx0FZGpQ6EK-X961xySODqBojtWs72eHz3HqReMJ5Lb8cunojCEYek4aGeil8Gb8OquOUbP5z5FoqoYa6-Vy3vbh-S3VdkeWWvxw7LKVNziOeEgRCujAE5KSBy4NLAQ68p_wqbwsZ2-hCeVTtlXOtLqPUP5lm8vSFLrIpjIPV1omzsE-5dnVjGw2YqM82XEAWd4TaLIvZs6BgAkcFeqpVro9niKh3rIlidFbKAn1cqR_ubeUAErLgXzghQAw7T1XaGe46avG9PKNk9iaiOhPf8a0mbJ8ttR5c3RrU6ECA_hNJ2on4ZZB0zjgL5TBT4n_Xesqex64HXCLmzKrf1uD2MnkDB1qvhLUI6c5AH94k7ShsMGmTFK8Z4nVX_KfKZ_uiEKBH-y5bYJHVZnk_MEnFJ_nFK58MEf6Gi2PUTzUQ_DrZXR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI_gawSHFDVfZu7b9AQfIUasWdai1hfhq_8hY4gZ_yTRWnWhAzVC41_9FGeLpbFFxbGQ8PW3GayEGoxfLlIk4-JGkpYD9dZ5NQfNHh0ImOKqEBdaUW34VOhg_pNgIqw7jWlc5xbWc4hG8-X7X2A44IVq1C7aNhYxWzrVffdPEEMKtMfvphYuVsX1BAugr1XS7YpPCPLK3eIYZeN2urj00nvdFwEbie_sMXroKchMejZhBz7PCJaGXA8XZPb_l-LkeUygEkphJ_w7dAV_xYVUvmk-yOvrgCh8WtlvkhiNUlFpjyncgO5l-nzIQ3NDAlRTY2Kv4Haqq65ZkrZpN92UHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=MOmOwrkEp9a0suw3BfXoSDqXtd5lJzyaVGRqlERctT51ibbVz_1zEsNmPcy7dSWL9f-S6iv5yG_7Wf-86n8M661o7He_0HV9mcAaSsFEiPkmZ82pvp2_Xypa93g0Oqi_ZQUvKKId9WduJgS6ilKFOmoX18G9pGv8C4ccmn-iPQ1gnWzIcAbmQQM2CHQ_LjUtTQSxLKxO_s4TarvwJZWaI-Nn4TX7HImXvqa8qFxAoBFBi7bv6k0FZJSTvDDBonzfxfN8ohtTeQ9jNU_-_7oIy67nWqSA7iTHHfYuQCFxm9HZtgnX47RITdMIAl3YCGXCLY35uGQ5_vizBq36kdMoag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=MOmOwrkEp9a0suw3BfXoSDqXtd5lJzyaVGRqlERctT51ibbVz_1zEsNmPcy7dSWL9f-S6iv5yG_7Wf-86n8M661o7He_0HV9mcAaSsFEiPkmZ82pvp2_Xypa93g0Oqi_ZQUvKKId9WduJgS6ilKFOmoX18G9pGv8C4ccmn-iPQ1gnWzIcAbmQQM2CHQ_LjUtTQSxLKxO_s4TarvwJZWaI-Nn4TX7HImXvqa8qFxAoBFBi7bv6k0FZJSTvDDBonzfxfN8ohtTeQ9jNU_-_7oIy67nWqSA7iTHHfYuQCFxm9HZtgnX47RITdMIAl3YCGXCLY35uGQ5_vizBq36kdMoag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldmLoOlD_JR4iG7Ms0eHmxk7FRPao_UZbs6ddn08gw3OhHiHNUaR8qO-erCj2MbCc0omUftwWHKVTydctjmtiS03bY8mlttkDad0oNSTlOmk9oQhd6401H3jORxb2vyfKIy4x34BMbvp85wOLrZRQ52zaXWw5G7mds_Ets4IGQZvRegMzttovIXunq8LPGdqPqmH8blj_A5jqwoleH7TYnn644ubmUzoYIdEpHO6ErbPr9NH1gILgmxfecwzrzSR4aWSL7LoyMJ_XY4bQTHXdABX9-mRLs7cDJ3ExJ333kf2Jz6QhUektsdnH0XYog3TgC1O8dzBZotT5iDVSlJ0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=Q3t5r9Y6d56bmmrc2srNxEEjOsqbhGS8Ma-1EsFc3TgztvgdziyO7kkckjFxR58CNnzJKWjB-CpWh9yX9ndy91fp2BdxZEq4TVLL1TP3Ces_2EjRdTtBGVd8Ag8L3frCd6-jSJ7M_nG9na1DZQPhrJL1O1-CkCuXP_jKXCelzOR9Ow2rIys5knSRlIfLP1EDv6qN0cJRz_oWsJD9_nLoQYUne5A9h7Llj1hixw4GhyYi4QAV5DcMmTVScM8T7OROwFEadMQYRyvNriM9r7vh-76QzBnRlMdAzROKSgcLEHW60hg4l96DrUnzizHCSIwdiK-Eo8oxNkIt6W9pOM0khg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=Q3t5r9Y6d56bmmrc2srNxEEjOsqbhGS8Ma-1EsFc3TgztvgdziyO7kkckjFxR58CNnzJKWjB-CpWh9yX9ndy91fp2BdxZEq4TVLL1TP3Ces_2EjRdTtBGVd8Ag8L3frCd6-jSJ7M_nG9na1DZQPhrJL1O1-CkCuXP_jKXCelzOR9Ow2rIys5knSRlIfLP1EDv6qN0cJRz_oWsJD9_nLoQYUne5A9h7Llj1hixw4GhyYi4QAV5DcMmTVScM8T7OROwFEadMQYRyvNriM9r7vh-76QzBnRlMdAzROKSgcLEHW60hg4l96DrUnzizHCSIwdiK-Eo8oxNkIt6W9pOM0khg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=mW3nyRvRdAhf3R1NA2mfQm16zc0ETEKABRqpgXHQ0xIw7p1u9L1iCAFuCfcJUq7Aq7eeBQ_3eVNEFAcWfFnZB8Vv2FlCb8jHspVlBz8UZPVByEU7cD-WL-DxwhBV1wj4ksbi-ilo_x1_jEnGsW7A_gcsdvyDx8xljSw86KQnL5aRs2Z6NVrmkcxSZGdoS7sx_O4Ovp_llWmNAq8d2qoudEGUBmhTLvM7UfeMF_xTWv-_j9Zr-tYwtiIjTZ0mMgVu5XaeVawB807CZsRv39yFDkCDi7YYSA2Id-aXSqqUakO9Ut1MFWTht6y4K5L06d6D65glgB_SXcDXTucmWWtYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=mW3nyRvRdAhf3R1NA2mfQm16zc0ETEKABRqpgXHQ0xIw7p1u9L1iCAFuCfcJUq7Aq7eeBQ_3eVNEFAcWfFnZB8Vv2FlCb8jHspVlBz8UZPVByEU7cD-WL-DxwhBV1wj4ksbi-ilo_x1_jEnGsW7A_gcsdvyDx8xljSw86KQnL5aRs2Z6NVrmkcxSZGdoS7sx_O4Ovp_llWmNAq8d2qoudEGUBmhTLvM7UfeMF_xTWv-_j9Zr-tYwtiIjTZ0mMgVu5XaeVawB807CZsRv39yFDkCDi7YYSA2Id-aXSqqUakO9Ut1MFWTht6y4K5L06d6D65glgB_SXcDXTucmWWtYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=urO-wIiRm2vYBtJ_7A1fW3QcTAN0WVvkjcAPNG2Ut9wuvQ1TEu3eWzzgy8keceX1-n7Myr7o1hn6vGOlC5L6ZlpTTpRZZKNVE7smSGDrdlgUEembkM9FDhk9__rT88gMhgSdlt3lFl0mk6JBfrx_1shNl7hWMHm9iXcO1Piruo2Ozl6yLqpDbXQCdhyG0zlKub86ETNVkLkUcZgMVlwtYjtibrQ6h5-50x2o_KrKe5SsxIaeUxmt6H6A4-SQHjjUGdfGET_nyng8rlbI4cuiehYv9ZAVfXvefQ75IvN3cO3RA5zAJnagr-iNRBS841ec1rnIbFEsoY1GZtEuYQE3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=urO-wIiRm2vYBtJ_7A1fW3QcTAN0WVvkjcAPNG2Ut9wuvQ1TEu3eWzzgy8keceX1-n7Myr7o1hn6vGOlC5L6ZlpTTpRZZKNVE7smSGDrdlgUEembkM9FDhk9__rT88gMhgSdlt3lFl0mk6JBfrx_1shNl7hWMHm9iXcO1Piruo2Ozl6yLqpDbXQCdhyG0zlKub86ETNVkLkUcZgMVlwtYjtibrQ6h5-50x2o_KrKe5SsxIaeUxmt6H6A4-SQHjjUGdfGET_nyng8rlbI4cuiehYv9ZAVfXvefQ75IvN3cO3RA5zAJnagr-iNRBS841ec1rnIbFEsoY1GZtEuYQE3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=ZtuuFB909tjCcpzOkzwg7_VFKRaWZPtYootrfTD1A6UBVLdYEaY1uKHmaxK-JsDKUmvAyHwSBMZarYzol6tiqeTxDeuDDreZOj-njQg8pH0kd-OdBjHS2B6KGuyDoESwXp8jwoE4e88E-Ut4aoOe4zUT6SL9GXeIaapWP722Ld4vLAISVk9zSs8rcAdxYKh5HBnNCcy5VpwDG2BiaPG4A2RXkmtD7UxG27UxEg_6lGIAbPeuoi-bvt6rEWgCJxCd8YlhRPlHPRO5AvjqqC9UHdQx3ID9GWwHvuVDwV1GtH0u7_s6jwOMIPxPMDuSsrtmb0Ly_dsuHGlKDsy-xBx35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=ZtuuFB909tjCcpzOkzwg7_VFKRaWZPtYootrfTD1A6UBVLdYEaY1uKHmaxK-JsDKUmvAyHwSBMZarYzol6tiqeTxDeuDDreZOj-njQg8pH0kd-OdBjHS2B6KGuyDoESwXp8jwoE4e88E-Ut4aoOe4zUT6SL9GXeIaapWP722Ld4vLAISVk9zSs8rcAdxYKh5HBnNCcy5VpwDG2BiaPG4A2RXkmtD7UxG27UxEg_6lGIAbPeuoi-bvt6rEWgCJxCd8YlhRPlHPRO5AvjqqC9UHdQx3ID9GWwHvuVDwV1GtH0u7_s6jwOMIPxPMDuSsrtmb0Ly_dsuHGlKDsy-xBx35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdmQ67mDcYN8EzHA33nzGGTOXy3_hLGCl1J5zYT_OotDXAScONpNkc5fIgwAsgxvJKIQyBgjITrEXRDJR1R_WjjXu3TPMjB7fsDE5-XYL22hpln04_V9hu7X3SDQNg_4pfOF7omqFq88bBkh1tvsBZcNS5xR4XH740U0Pcld8JHUB_Af9FSnYEBOAxb4MdNQWikaOT9Y1ppArch8Jp3O0jgL7gpd5MHT4hI7D3YUesPSdZkixQ-uvqHypEnqlPfpO1Os5GVvcFzFOOK3DsSCLoe4ZHw9vnQdQV6vGuPgUFM3r2M_YM_hddGhNBJhwLfAU8nvZV095FiY8o2Oa2ni5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=sQHxgj24zfnfocMaYjgKrMKgZD8ZLqcu0qhJ7wJzDDzlCDE6zCsMth48GCXU9d1Hs_mlGX_RIq-CN1To26SETDDAJp7Mxe_IbwQZ_7k0r0d2hcyLoUT1DNMDc_Nw7ifAQo8TJ3DQ1Rr37uO6D4c8jKi37fX3Sac5zi2rho1acwq3gipMd-wsHyEQ6aQ_LBiOTnE_m24KJbmBTsyNTbLYmebfod7EA4VN2VTziHkAhfX485uiroJwMntg5lBnzTCin6p4C6zLeP3rskMqAuvHNxniyETOJ6TdqDLoyc-bAfTjNDpbYq52kK6z3IUE7WlQah3ZeDgFX1o_o2hU_o0_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=sQHxgj24zfnfocMaYjgKrMKgZD8ZLqcu0qhJ7wJzDDzlCDE6zCsMth48GCXU9d1Hs_mlGX_RIq-CN1To26SETDDAJp7Mxe_IbwQZ_7k0r0d2hcyLoUT1DNMDc_Nw7ifAQo8TJ3DQ1Rr37uO6D4c8jKi37fX3Sac5zi2rho1acwq3gipMd-wsHyEQ6aQ_LBiOTnE_m24KJbmBTsyNTbLYmebfod7EA4VN2VTziHkAhfX485uiroJwMntg5lBnzTCin6p4C6zLeP3rskMqAuvHNxniyETOJ6TdqDLoyc-bAfTjNDpbYq52kK6z3IUE7WlQah3ZeDgFX1o_o2hU_o0_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsR0Ee3vT9SSs-sAOjNljp9y99vs1k_hlqQX87GvK5fnICyCjz7EN18ESy1cKQIbgQrbGyp-gfG5spqm_2jAX7cbJnrW0ibhO2GqLkTqArLr2Rh2X9AI3dtuIFWciI2gBaj9BacDH3l5hUZ5PKmGN583PbHLoKrEoNdkd_NHnB_P6-Cmjw5pBXtPO8X29V2iXNBRy2_qTEJo7Fvn7wxk01rcfqNHZkBU_vF4t4zKdEl_q2PxqzjKqIksyIbXWskBsnLX_mw-VzgmjsQ2jESJVtNIPuBEPs6Xv4pTyNz18gUL4b-Ne8U4EgJ7nonqWi0QqWYsARpY9jjKY7HCMnAZNCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsR0Ee3vT9SSs-sAOjNljp9y99vs1k_hlqQX87GvK5fnICyCjz7EN18ESy1cKQIbgQrbGyp-gfG5spqm_2jAX7cbJnrW0ibhO2GqLkTqArLr2Rh2X9AI3dtuIFWciI2gBaj9BacDH3l5hUZ5PKmGN583PbHLoKrEoNdkd_NHnB_P6-Cmjw5pBXtPO8X29V2iXNBRy2_qTEJo7Fvn7wxk01rcfqNHZkBU_vF4t4zKdEl_q2PxqzjKqIksyIbXWskBsnLX_mw-VzgmjsQ2jESJVtNIPuBEPs6Xv4pTyNz18gUL4b-Ne8U4EgJ7nonqWi0QqWYsARpY9jjKY7HCMnAZNCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HZpV8DBq-oWfVulI3JpWuKyGvR4S4AZkvsxULQ9OVnQG5jCq85UCqk3vXFJ8655gy24T8fnRTAYrHyxZT7zkmsTielk4g3MexHvva_cPoIaljFLt0gyw84o2uJ21PVvyTJCG4KJvcWuW2wMvSbmJLqV0RWhlBeZ8tp6LgNqtrFfY-rtI9lLed2-URvz7pLue7PBBg2teDlfidYtDReckyZ7Ya6QCRk_37Ay0lExBM_F2uuhv_yP3EMeNmIWtDTI9pwu3FH3mpBDerVd1TqxCX7qSFkGZRyvqN9Zl4huulb24ZopdSwlo183DWj2bD7ojnziwx-LibSVP2ULo05OKVzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HZpV8DBq-oWfVulI3JpWuKyGvR4S4AZkvsxULQ9OVnQG5jCq85UCqk3vXFJ8655gy24T8fnRTAYrHyxZT7zkmsTielk4g3MexHvva_cPoIaljFLt0gyw84o2uJ21PVvyTJCG4KJvcWuW2wMvSbmJLqV0RWhlBeZ8tp6LgNqtrFfY-rtI9lLed2-URvz7pLue7PBBg2teDlfidYtDReckyZ7Ya6QCRk_37Ay0lExBM_F2uuhv_yP3EMeNmIWtDTI9pwu3FH3mpBDerVd1TqxCX7qSFkGZRyvqN9Zl4huulb24ZopdSwlo183DWj2bD7ojnziwx-LibSVP2ULo05OKVzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcjIceKDHf944ihKDu7TtysIfRjMZjSIDdewqQSeuK2dWx2Rvl7oX8GcendoufcQzL3IRa_toBhw_y_ujD8UByzN8bv_Ls4Px4yGyIUtrsamgnqOirdHwQcovHFffoGyLa1TjcArN2aEdBrO23rz-fXPdw9C6gx2VjVFg0jummJTHZUeieUf_mdZ1uWYMpsXv76amxAqg48q4uy61H2JTBmYYG2CXHTeVL04pR5dGaLZFulXx93PQglZdfieX0Wr9_dYOZtlnl6aSHCJA23vpYyUUkUFbuv-flVDfW164Ic3F3txBHgxnl3w0vyt4b1aTXnmj4bfAYdPlxgDggCNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_5GXpANlB8vumWF7VMtiz2jJOBH6rJlITGUJzeA3gnNDXk5Pltyz6KSfI0uKg5-FsroyjwQLslLyyN6ZY7GMDqwUBqRH5zkD9iK3OeuAQ0-_S_ktnPiSDHzbUOfc0wQQ-k9a6fPDQsVASb7cTgm_FPZcZ5yElSxN44xr1pD0IE3DZkmPD_NCWZ_-gT1ZS5eZuerC4mw6T7h7xBA-KSpSKPK7Pid6sAaj9CyBqBzCceAdNDLpore_gEryTAD3ZTQ7pkaL04C3nTh8BEvFKS9W_fjCJbDQPfXsDvnKupKzKL8qcTY5jgLiM_eLwodV7MQ_ipOARJ3sF1koW_LKFS_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=oeQ0QOMUhyJhDGx2gpWHcbuoaEHl3D-JmcEtBSf2LfyPWupaHHIqSH4Uf0ZBbJPwHDZKqa1ryMy6BBmu4-INlpP_CpHGIbXz3htqqofQ6lrpH4cyPQLxevPSElkbnYEH72WIWYD3p4aGHAgMtowYK2b4j2LxrfCrxgAfcEN170kftGw6vv50hCuahbvvvIt-_B6bCnLWYqSCeEdXxyXettLPLxP2T0bPp3B_lw1VPJ5JCaCm32WDXBzCILhjiA36j_JtmBZBGVziIAONNjAHqSDioTK6shzWaLhCvwryf7DTfStYKhWrwUAadSEltYB5zBOeyJiqOrXZIH3PduXDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=oeQ0QOMUhyJhDGx2gpWHcbuoaEHl3D-JmcEtBSf2LfyPWupaHHIqSH4Uf0ZBbJPwHDZKqa1ryMy6BBmu4-INlpP_CpHGIbXz3htqqofQ6lrpH4cyPQLxevPSElkbnYEH72WIWYD3p4aGHAgMtowYK2b4j2LxrfCrxgAfcEN170kftGw6vv50hCuahbvvvIt-_B6bCnLWYqSCeEdXxyXettLPLxP2T0bPp3B_lw1VPJ5JCaCm32WDXBzCILhjiA36j_JtmBZBGVziIAONNjAHqSDioTK6shzWaLhCvwryf7DTfStYKhWrwUAadSEltYB5zBOeyJiqOrXZIH3PduXDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdjyCpYphrE9cDDPXhppDQLgDievar7AwW5aJjdNbb35IXZ1T42jJT5Q7Ng7IcqbfWO2zTl2UFZuqB_-JFZ0onxaNBsSloJP4duDUbLXikCatm2U-GD9CJHj_Orf5XpmLtMSODO7IUWbtHEMnQNmiTXNEZ5PppguKVrqoLeR7gH8eRdYtGTmhbu367qBB_0bvHyjHTDuLMyoilR8v9MTUteGKL1suEKgWi8FAVihs7KcQblqMvEGnqBPhLxjZZOTduSGmlZtwJSfj5OyI1r3XX-byNO9YDuIdshdiEJgTx1PYz1g-yVAK5mHAaFQUfEoQBx-QRmZOnwgoXQlVHrejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=ESHzVBFLiSCbtf9c7QDGwH9AMQfOfR0zeedxXoYWEdRZQc_UbOQG_ZSfQk9fWlYICg2y0fm8hzTMIzfxqI5CGf0gEn5Ke3MjGnv48fYWaFfXiLjVmkO3arq_dzYVb_El4OQl3aeK6fAhnb33xD6kC_rjIbNrAWhYFIAwDkOrXrOSu3CWluC3fBOH2PzpRYU1-17dL1SdYyfS2nu-lhBD_aqWRTnM6k5Xm_Tb_NKMBoac3FKyMZYYAsqNaghl69Km5glm1-8PQwf8_Qs_A-f_kCz7uuX7U7htNo_tamyvWrrBsONm5_kPhLHa_yyj3MMkfD-CZRUOO4F0VCN24JZbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=ESHzVBFLiSCbtf9c7QDGwH9AMQfOfR0zeedxXoYWEdRZQc_UbOQG_ZSfQk9fWlYICg2y0fm8hzTMIzfxqI5CGf0gEn5Ke3MjGnv48fYWaFfXiLjVmkO3arq_dzYVb_El4OQl3aeK6fAhnb33xD6kC_rjIbNrAWhYFIAwDkOrXrOSu3CWluC3fBOH2PzpRYU1-17dL1SdYyfS2nu-lhBD_aqWRTnM6k5Xm_Tb_NKMBoac3FKyMZYYAsqNaghl69Km5glm1-8PQwf8_Qs_A-f_kCz7uuX7U7htNo_tamyvWrrBsONm5_kPhLHa_yyj3MMkfD-CZRUOO4F0VCN24JZbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72613" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a16936d012.mp4?token=QEluQU045L1cVsZPbG9B5gjSdWa152kxCf3o9bTV5ucTGMsGANpCjeu6Fkm0fyhz35vghjuzgkTDH-n9ZNML5Xx7SvvA0iDAywid-7gp1DMNQafsGGeDNVlcUXe6Z2zodDjTiRl3pJ0XbEka9wom8Fz2JI7TihhuhFOsUdvvVXViF2Qy_rpRDdhfPn-Ffqrsv5ZTY1UhYGJO-dFebbT2UzSL9uhsJg2n1C2UmOfaHvOKnUXZep0BIYphNW19DPr1Klyahw9RY4lTt2e9xdTflFKB4eVkn3oXnx-XiemMmwlQOv0SUTgLp7gYkdH5vcvEByd-1uqN04xsjP6brFNfZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a16936d012.mp4?token=QEluQU045L1cVsZPbG9B5gjSdWa152kxCf3o9bTV5ucTGMsGANpCjeu6Fkm0fyhz35vghjuzgkTDH-n9ZNML5Xx7SvvA0iDAywid-7gp1DMNQafsGGeDNVlcUXe6Z2zodDjTiRl3pJ0XbEka9wom8Fz2JI7TihhuhFOsUdvvVXViF2Qy_rpRDdhfPn-Ffqrsv5ZTY1UhYGJO-dFebbT2UzSL9uhsJg2n1C2UmOfaHvOKnUXZep0BIYphNW19DPr1Klyahw9RY4lTt2e9xdTflFKB4eVkn3oXnx-XiemMmwlQOv0SUTgLp7gYkdH5vcvEByd-1uqN04xsjP6brFNfZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی مملکت یه سری مهمونی میگیرن که توش با تم و استایل دهه هشتادی شرکت میکنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72611" target="_blank">📅 09:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxk7R_wcSNWPeUDCSXtnrjEmngZPKn8DAnLshc5w5ltZ77shxYIpsZ9gWdIS7uooBgH5VByUp9Jrr3FohFr_VojJBnBszE4MZ2bmD0nP1YfdKyY_TgPTPt7VbgOhhAEgpp7F2uq34TCUDaq6pab91bd3xtIRKhDBtilJGryo72OLK49RW1LZc946ajKwJpFqYLWQ-jIfs2shkMT7ScQ2B5eSekEM-KK_Girh3eEje_2-Fj10waTnl5N7k9ys31BXYS79MlGG8_UeSRis_PXAbXZ8Z1ku0Iyc-RtYT4_OI88d1YTyO274vJnece1r_xu4Vh_xJNPgSnM1n9m0yaPX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده با اعمال تحریم‌های جدید علیه بخش‌های خودروسازی، ریلی، تولیدی و فولاد ایران، دامنه «عملیات طرد اقتصادی» (Operation Economic Outcast) را گسترش داد؛ بخش‌هایی که به گفته واشنگتن، با کاهش درآمدهای نفتی ایران در پی محاصره دریایی آمریکا، اهمیت فزاینده‌ای یافته‌اند.
وزارت خزانه‌داری مجوزهای جدیدی برای اعمال تحریم‌های بخشی علیه صنایع خودروسازی و ریلی ایران صادر کرد و شرکت‌های بزرگ خودروسازی از جمله «ایران‌خودرو»، «سایپا»، «ایران‌خودرو دیزل»، «پارس‌خودرو»، «زامیاد» و دو شرکت «نیرو موتور» را در فهرست تحریم‌ها قرار داد.
همچنین تأمین‌کنندگان خارجی در اندونزی، امارات متحده عربی، ترکیه و هنگ‌کنگ به اتهام تأمین قطعات خودرو برای تولیدکنندگان ایرانی و کمک به حفظ شبکه‌های تدارکاتی بین‌المللی آن‌ها، تحریم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72610" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py6-hWAla69TAZ-TREJjL1xqDtT1d04pXqKRfOt3IpzYK7My2oMquHMwklFB-365gAH6al1_MEbe58koSsa8Si425pSzHSUECEkjIwL0Fq3TrFValdRiDod_h3H3cFz6qLvdMpYAn5Dy4u_2XTSpDRIuy-Ej9MtGBq-WcNg7djmjT4T_RCf9F-85jJzSsln04PvWRnL4aOMd-n2FtriruqvDtxKteOOZc1oCGczLyUIT3dfZEK-M1TyW5a1q6yYMv0q-YBoMbTlwHyRuvQ0ASDhVzWKPwEqzxkr8-aRVkW4-eUX1h1J-u9MYiRkkb1edYClUiKu_Yb5sGUIYOSojcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=f7u7dYQJsdjjIlQXMgQos3oTlqJ6dFxswVaW2QA7GYs_lHQJP9bKHqm_SKa2qzXv9qlhTIFk5nDng0E2bx35y70liRo3--9X5wIp550joFvRluGq5tSyUqkwwKtIub9qcAR_-DQsT_0OWM4SiMOoZZzwlSIAomiYMZIX8qlc9Omvz-OVP6uv1_o9nqaS6SVkxduAgX8smQSkhIH1AEOQ_gkEGVjaCLbARzvw2IjoMV3tE7mn5SLlmtmNjaFX2GdErE8BFvhZLH5hKh_wiILdImZ1_Vr-yKDUKyBX9WFD575xnOP_uRWMdTD96p0ACvI2BIvo6N_H8NF0v4izvkmuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=f7u7dYQJsdjjIlQXMgQos3oTlqJ6dFxswVaW2QA7GYs_lHQJP9bKHqm_SKa2qzXv9qlhTIFk5nDng0E2bx35y70liRo3--9X5wIp550joFvRluGq5tSyUqkwwKtIub9qcAR_-DQsT_0OWM4SiMOoZZzwlSIAomiYMZIX8qlc9Omvz-OVP6uv1_o9nqaS6SVkxduAgX8smQSkhIH1AEOQ_gkEGVjaCLbARzvw2IjoMV3tE7mn5SLlmtmNjaFX2GdErE8BFvhZLH5hKh_wiILdImZ1_Vr-yKDUKyBX9WFD575xnOP_uRWMdTD96p0ACvI2BIvo6N_H8NF0v4izvkmuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=OmA0Q681c7NIyr3OAYIRT1hdng_N8RhTwGWG4Kje19HI2io2hYybjiu03-aj8jJ3nEHlvXoSJbIvUEIqTyy5BXISshLUMk2i_iin6-0Y4ogZkb2pZ766Uqii0e7ZyIt7LfiSzTZiCI0ie6XTq1hX-Ji0mj1g2IcBAWaO-g900t7mFPUf-tI3UzUD1jj7blfLNMyXMpv81opRVisWBj9QPrboW_bydsepKx5PqPT_Y9bkQm72s2T2cS0zUUJjTjnmOc7vAk46yvOPbN2ap6fzqLxxOif3HmFFt-ijKht8aCAH4vLfv2Bb1-MrbMNJlXN-stb71WTU0G9f96ILOzbH6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=OmA0Q681c7NIyr3OAYIRT1hdng_N8RhTwGWG4Kje19HI2io2hYybjiu03-aj8jJ3nEHlvXoSJbIvUEIqTyy5BXISshLUMk2i_iin6-0Y4ogZkb2pZ766Uqii0e7ZyIt7LfiSzTZiCI0ie6XTq1hX-Ji0mj1g2IcBAWaO-g900t7mFPUf-tI3UzUD1jj7blfLNMyXMpv81opRVisWBj9QPrboW_bydsepKx5PqPT_Y9bkQm72s2T2cS0zUUJjTjnmOc7vAk46yvOPbN2ap6fzqLxxOif3HmFFt-ijKht8aCAH4vLfv2Bb1-MrbMNJlXN-stb71WTU0G9f96ILOzbH6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=YEo_p5DMbYm-kWPuZ7hh4TLdVf_CKqxbykfcUHxKdKB4zHD7psPW8lFm3pJra2cc46i--ueotHl6bTKMzcO7KTh6OowjfWGW2WRCX-lM3J2xFg7KmwLSLKpEKXJItC-TZ4d4Fpc9wmsXl4hi-zhVmx0MXqbnW00ndcpXGVtLR3qkXmgTE-9AzIzoxU1kTpKTRJSvoQAYijP6hmYSCDilED93PkXqlzCDn5zZ1RtFCn3cJE0YW_28WlOavpjcPiJxlxdI-NfeWSiRCpSIlg4e1v76_wFvEhVLsqDO3BgUahg7-MyQ1Xbn2kNkgrp5E5vB7PxByNt8OA7bTK8JeKJqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=YEo_p5DMbYm-kWPuZ7hh4TLdVf_CKqxbykfcUHxKdKB4zHD7psPW8lFm3pJra2cc46i--ueotHl6bTKMzcO7KTh6OowjfWGW2WRCX-lM3J2xFg7KmwLSLKpEKXJItC-TZ4d4Fpc9wmsXl4hi-zhVmx0MXqbnW00ndcpXGVtLR3qkXmgTE-9AzIzoxU1kTpKTRJSvoQAYijP6hmYSCDilED93PkXqlzCDn5zZ1RtFCn3cJE0YW_28WlOavpjcPiJxlxdI-NfeWSiRCpSIlg4e1v76_wFvEhVLsqDO3BgUahg7-MyQ1Xbn2kNkgrp5E5vB7PxByNt8OA7bTK8JeKJqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=Dl1a_oqMvEtEMxgjRW6KAvRtyQMVfXIG04X-Bu4FviDwqNJGluc6Syaf7_9GEyIOL4VwqJXzhq8I77CJdO1VdiDG_7UrD-kkgrfGgzQAmEUZvZ7pAYtiS6iytQW2XOXkkCrbB6DBJbVT0IQD8sz1egov8o20rfkB7gEdecJK9zH5Vajhzds8z_9hVbiq2eYsSmDSiBUipgeAG64gmX-JgPLM-MjBMQ2Dl8QkKQFcsZiLkCZKQP8h-z9Z6OhVlzNl9zzG6KNPWRJ29iPYwIYM-nSCx9na4PH5_XQF2KY9J5ocT1ZJs95NB4Yb30aJett1VtpEMp9uK08NwzRlo4bYvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=Dl1a_oqMvEtEMxgjRW6KAvRtyQMVfXIG04X-Bu4FviDwqNJGluc6Syaf7_9GEyIOL4VwqJXzhq8I77CJdO1VdiDG_7UrD-kkgrfGgzQAmEUZvZ7pAYtiS6iytQW2XOXkkCrbB6DBJbVT0IQD8sz1egov8o20rfkB7gEdecJK9zH5Vajhzds8z_9hVbiq2eYsSmDSiBUipgeAG64gmX-JgPLM-MjBMQ2Dl8QkKQFcsZiLkCZKQP8h-z9Z6OhVlzNl9zzG6KNPWRJ29iPYwIYM-nSCx9na4PH5_XQF2KY9J5ocT1ZJs95NB4Yb30aJett1VtpEMp9uK08NwzRlo4bYvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=GKw96TTMRwlKF5e7m0j2LiB5GbjFCg94s50cq1FouXAmDkDgXKmAaCQ3gbJu8XceGkGQOhkxJrmGcYhszI0FbHjzKWQ0we-Xs8lv9crZZ3rxChHWePAlt_zqrVonYTHC45A_5Z5U6z4_w4usFtPpsgTNSQX4GOujki0XyehKdujszn1o8ybQ3-bwFWpyk3Va0Ws_D7Xp0ewMz57LGqV272MoyrWgzD2WiY6-yP-k6xTUUV2J8oI7SBd89BojSTjatxWOqorEjXlXa-jiwkumWdJX7WHzf72SKbDYoT7KSs_Wo2EyZHdqiGtoiEbMRWHPbileZhOVKa_e8TBnj5z7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=GKw96TTMRwlKF5e7m0j2LiB5GbjFCg94s50cq1FouXAmDkDgXKmAaCQ3gbJu8XceGkGQOhkxJrmGcYhszI0FbHjzKWQ0we-Xs8lv9crZZ3rxChHWePAlt_zqrVonYTHC45A_5Z5U6z4_w4usFtPpsgTNSQX4GOujki0XyehKdujszn1o8ybQ3-bwFWpyk3Va0Ws_D7Xp0ewMz57LGqV272MoyrWgzD2WiY6-yP-k6xTUUV2J8oI7SBd89BojSTjatxWOqorEjXlXa-jiwkumWdJX7WHzf72SKbDYoT7KSs_Wo2EyZHdqiGtoiEbMRWHPbileZhOVKa_e8TBnj5z7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=fIlWPGv5Ndevgbi0VEt61wKLQ25y880SxOSqUu-oJqRqnTOicqI3V00NRc6n1mAjJr7jeKSPQZ1Bi2MpqK0vY0GZioWv4T50-SwrnlijsbvyUZuxpNCLJ3jNm5qYdO2goFOcD0z_J-c98a2ZAxinSMZ7_bBAsqTmTYIeJGFrGXOm0_zvMIeftgR8db3Al2fixLs98XU1BM8RNMHi89rhOwaNp41UPQt7R8vyxJdrTAraBxZ4f-g6RpLiRyF_Lzr3McsBttVHd3EcVx1uV6Fx6dcjCZQdgIDXk_l68ad_rQtl-ajDGz4MubJF9dGFekXh1nav_bWt7q7CStdvUD46gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=fIlWPGv5Ndevgbi0VEt61wKLQ25y880SxOSqUu-oJqRqnTOicqI3V00NRc6n1mAjJr7jeKSPQZ1Bi2MpqK0vY0GZioWv4T50-SwrnlijsbvyUZuxpNCLJ3jNm5qYdO2goFOcD0z_J-c98a2ZAxinSMZ7_bBAsqTmTYIeJGFrGXOm0_zvMIeftgR8db3Al2fixLs98XU1BM8RNMHi89rhOwaNp41UPQt7R8vyxJdrTAraBxZ4f-g6RpLiRyF_Lzr3McsBttVHd3EcVx1uV6Fx6dcjCZQdgIDXk_l68ad_rQtl-ajDGz4MubJF9dGFekXh1nav_bWt7q7CStdvUD46gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9wz8tyYP14o1a6_loR9P0KN_4rtKPlwzQWSVQcv0xiDcqOIGssUQ5LdeBiOSpGMML40upSwehe21Mz4sy7Ix2jQEK1YEV99ZeoRrOJs8eXBVZeT90oejQ4HxKezEgbaXMmm2hZ-x9YwS9zvzE847Dsi8YkcE3esCc-DSnre7VKEDJf-gIiK7Ep4Ttr0UOwhtj1JBfl7TyEqIhxHximZcQkj4sO_Vm9jIzBR6S8dn28VKUC8zsnNacuBu9JkIu_oDilaWLDDAYn__7sRG9_sePlEAnCfzGx4nt_NNzU4VsaXHuvv8jzSRlgJblJ2t4Aw1IfSCHn1WVaNgBGuN-G9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=OlE3g1xhLIgXjLpuLjJcsq09q9D3gcBNV1Z0lo3Na2-CpzIRkwomxCeS-EsnW4NIDjBHSLVAlLT_tQhZlFA_C7gRxIj7QUlrxj59UK38xFVa0UGQjUyAwqKV5roC1g49Ug53LaPIRnDiw4Rv3zXFQ0wWHU2GXiNPyOVMJZocLH69UmQWkBxr-DUlKjrBFoMhDU0tbwtEAPXKYOKeqymgZM_59n7Np4yzJEUTskMzQdJNm-rfvpU-ElmE4gntdKy5d7lTwK7GVU7I3yVd-fjxgmFKjUlA1LUtwfMKzm64i8uZYuwuOhEs_-6QTXSqoAADJ_0-7hWd2IPwXg9zKr2sOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=OlE3g1xhLIgXjLpuLjJcsq09q9D3gcBNV1Z0lo3Na2-CpzIRkwomxCeS-EsnW4NIDjBHSLVAlLT_tQhZlFA_C7gRxIj7QUlrxj59UK38xFVa0UGQjUyAwqKV5roC1g49Ug53LaPIRnDiw4Rv3zXFQ0wWHU2GXiNPyOVMJZocLH69UmQWkBxr-DUlKjrBFoMhDU0tbwtEAPXKYOKeqymgZM_59n7Np4yzJEUTskMzQdJNm-rfvpU-ElmE4gntdKy5d7lTwK7GVU7I3yVd-fjxgmFKjUlA1LUtwfMKzm64i8uZYuwuOhEs_-6QTXSqoAADJ_0-7hWd2IPwXg9zKr2sOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmNfm4mBgnP0hFuYT0h4YVlhADCYqvdZ0mYJehFGnp-904x4bGWmPQSGaHJ3AO6GadKtmo3mO3DB1R5A9eRLGQOSeXmVbp3LvMSW8O5gD8Awc3g0kf2mF0BYmoqzeNGXLH7d8wMhpUdyN3758tlytPBq1FFj56_8sTFg-XIAt4zywSDdFTaQQqLF5eR3Hu1YRR9oand2fMnVAiCysLaqcGDGmw9n2l-VwpEzGjGFMT5_GtDSCmKMNWLyQcHqpD1WaUFggmvbyaW_ltd7P5Y19Lm_ICbbGShDtyrSeRM9iJXDacjqAZvnn75iidYfyPDNHNoPdyNglidEj7uB4xgDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU4EEN7uzRrxf3nvcLOWxvWjhSFkqYpFjHRyuSQfpohAI5Wr_NeZqTsarP1OJoB77qBMO7QloAtglmsFP9JuOnEoTlJDZhLzcI4d-VlvMls7V0QHWFBhL6VtJo7KaOXZN0zgUmB1bdQ58OSOGoyTMRkmaC1yMfUtZB4cbCuWB-elHqMHfnLRcQM2r2DsRG3xkVlfQZ-DkdYtM4-dRQfFLE-w7tYUvGqRa4x7hWjjhsN--OmkG5-huFWqTqyGAw3en3P8EWRm63kgcRJjKiODykuf5S-CrqPERkQVaBE1pE_S645EMAy1-4lz1waHMdT-A--eI_QHj2DbmMPG5VERYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=Fhc84x3ZQ5eAPAr9fYkw0vikL5pO5Ex9yqrCyF3ael8glFXLVKBjlN84HZoywURA242orC8x9vdk-rR7Vy0zNBiiug265M00JtZg1GOt3xEjX5NAPelmsp3z-l6031JUKhO3qexE5znxSLoU66zSVxPt2YuVmhKZvbMoK_6TddaRH6Kzl-fCOW7QcCPNdzv3xZaZCDPyxmmNtXny5yPl1NtV_SPuABMn-E4CVpOOGzHVEEXTg-nNJMBRiVrJN6ITEeZ0n3LhqoWGq9JqO26ewmRA6wnJPMXWt8zR6zfylRuXzITI8cDM2KG-awbFmxZQgt5iQPjBcP786Zvrjd3ciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=Fhc84x3ZQ5eAPAr9fYkw0vikL5pO5Ex9yqrCyF3ael8glFXLVKBjlN84HZoywURA242orC8x9vdk-rR7Vy0zNBiiug265M00JtZg1GOt3xEjX5NAPelmsp3z-l6031JUKhO3qexE5znxSLoU66zSVxPt2YuVmhKZvbMoK_6TddaRH6Kzl-fCOW7QcCPNdzv3xZaZCDPyxmmNtXny5yPl1NtV_SPuABMn-E4CVpOOGzHVEEXTg-nNJMBRiVrJN6ITEeZ0n3LhqoWGq9JqO26ewmRA6wnJPMXWt8zR6zfylRuXzITI8cDM2KG-awbFmxZQgt5iQPjBcP786Zvrjd3ciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzHVUVoULcvsTwNWECv_z3uCcvfwBdL7Av0NWbx8fcpFZvsWQJu4wFSbYc4T5mq3aML3pYA_-gGXjPCzWb9f43jNIIX6nsH1NaqEDB5ogHenhsbP28hwLLvceIGlml4QjwF-0qa5JJtHnLCMtnbuAJNN8R8o4hyJt0CdK37Rb5XYyZtjtT6PcSspGNyMOuvkVtxppGWGtuvzwPRrB79nt0iPg6_WQ8OUJEaKw5sj5AHGe7IXHugSRlU0RVp0wHXl2li-pxPGA2Ti0FtxPKQFI0N-f34dw6fAS3tqHMwhn80Pu_fyUiigwBKTzKZ6jvJaWN3NaHbg3VoPMePpA0qEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
