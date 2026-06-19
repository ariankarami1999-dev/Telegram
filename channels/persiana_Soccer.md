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
<img src="https://cdn4.telesco.pe/file/h8btISsDn1lLBnJInvFEzvG-MizRLxLn-DJYNzR6lCIq1SJ_Gogt9hoksvToT_jpF10XBgH6ZcekQph0q0T6hq5bHDDC_PupLi2N8DlxkBd5gIkBdPgARpBejZJVTFlSgUcib0MEnvPfCNfs1H_qOgKtoxcIckseYIJ6n_H6X8bMLBe-WWeVmbFH9v-8qqmxnOAphMKBMUKvO10JA8x2k9GwJ4u5TYQV8NEe-QiWKY8tK77yusrURvSeh7e-ASoCaIENI4CcP01f9s5NB_A3MpyBwsfyfRcMh3WvuWaCUyb_hxSmpWomh6JqEmlHTVAmTtpLAXvK8GqNPLTRDBvmgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZfE7YINPIsx8Yq4pwCm2fsHBBUXlprobv8g3pg5BAxmCmAUnlzZaV8n2M4LFkJ_AqYZIja6DVvqPcuYmdBKm7Gl_KNnIDGqYcmfWczkStwzUuP5u8smkXO5s-_P1aX3NsLScKVBtDsTctxbi7vbM-EQT_C0ebFqr-IJXlccz7uTdkOdNMtk7SyO_S0AyL1pLvPLgVMUZh2CSNVhTm96vM6IicOlxxHVvsZvNiqDJD5d2w-X5FXWnmrHMjLnZcWBc41KU5BxVxlbn-v_ihArTj1yn-GM_59aCK-vqNzmBxO_oftYFhkzogQoQTbJBK3nXZVp4vnmNkF87rRHG1AEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=E_bHzO09SHDJEgqhgJqFFQsxKx1Hm28-D0ssWX6fWAgd5JL01itUhMwn6MYUWpCwTpv3--aLtcJLyzuF1tK3ZE4tcHq8vpanwM_lD-2zK6LgFci-YkVIfv2-lB1sd844DsCE9JzODVtMbKFp_kgjkZdDF4-SKFYCgIG583PRv0XdjwJbAUnrHYHB4v_zTkmDB7hdljGE9FCOvBT_j74x_AUfSC4rT9SmAPl7doOz0b2DMQs0l2NGh5LRg7pr0gW7G3QFuyHGHl8pK5GRmqp_0Yb64Yp64OrnJwwyOWGX9DstJq1gyYZ5euSSqcLZlX1o_jAfo1mvTGwiOPueOrV-Zxy36Ki4YCu_3iz00L25Y_V_Cj3rpSvNbqExgydq6UbwwoKY5YRY6y-wH4XjVVJyiPDMu8J2PLr16PN335AhcKcI8JPqW6lRAzNXIjIsjiLOkTqICwzEOfhlwhFqKW1SwgdNGrfmb5Le2-UOzox4UOhOQ7-y64QSVOFTl0gXZllyC3f8iFr8QmvTkz1pupuaHRSgjhatreAq1XN4zBjtgx2WKpTurdHVXYw8NICRmYP2itPPZ06pO1Ue6QJWyTyz6xH8A6k8JwNflTE_xB6kzeP5COpPFk-G61I_zyhEAz-ZHB7WytJAAHGqaeAVX5iQOIMejDLm3rmjaBzKrLdx22U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=E_bHzO09SHDJEgqhgJqFFQsxKx1Hm28-D0ssWX6fWAgd5JL01itUhMwn6MYUWpCwTpv3--aLtcJLyzuF1tK3ZE4tcHq8vpanwM_lD-2zK6LgFci-YkVIfv2-lB1sd844DsCE9JzODVtMbKFp_kgjkZdDF4-SKFYCgIG583PRv0XdjwJbAUnrHYHB4v_zTkmDB7hdljGE9FCOvBT_j74x_AUfSC4rT9SmAPl7doOz0b2DMQs0l2NGh5LRg7pr0gW7G3QFuyHGHl8pK5GRmqp_0Yb64Yp64OrnJwwyOWGX9DstJq1gyYZ5euSSqcLZlX1o_jAfo1mvTGwiOPueOrV-Zxy36Ki4YCu_3iz00L25Y_V_Cj3rpSvNbqExgydq6UbwwoKY5YRY6y-wH4XjVVJyiPDMu8J2PLr16PN335AhcKcI8JPqW6lRAzNXIjIsjiLOkTqICwzEOfhlwhFqKW1SwgdNGrfmb5Le2-UOzox4UOhOQ7-y64QSVOFTl0gXZllyC3f8iFr8QmvTkz1pupuaHRSgjhatreAq1XN4zBjtgx2WKpTurdHVXYw8NICRmYP2itPPZ06pO1Ue6QJWyTyz6xH8A6k8JwNflTE_xB6kzeP5COpPFk-G61I_zyhEAz-ZHB7WytJAAHGqaeAVX5iQOIMejDLm3rmjaBzKrLdx22U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr93pZ93BxNI0WPtUhfrzpKxs3_iegEwlCbmFmx9CJ4yI_KYIQkXb2lXdta6lYEMHh2zIm982g5QCkeTEn9jA6G87W87FOC-vcJFYzwsUWTw3qO17Sq4wt20gxZ5mgugwCyuAVGHIWsTN28N0CXuvOrkTc8-pTQwa9X-2HFfl87Gq58KjENkpxLa5YWROn5jir-ouOTHvxR-IoAJtgZOg7tojpcGdOstmJCRQkW0Qo44uSR0cPcVFS6M1SeMrVEARZOr2OISA7m92FgM1FA6Zdf9pfXa36XsD7I9Jr7Hd6jZP_Pmuv7e-m1boZCpaCEmUT4AZJW_tBvaVJ9YMQLScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGv_j1T_iXNnisShCviaVYqKNW1AgHN5WQbdyKfcYrgTmOipc5TjQVJ6kbcZM_igyH54K9oHiIQwUvhPWCAoYrC2zeAt0F9BorNIm5CNUpw7LD4sQ4P62U62-1GR7-1hX4eKmDEN6RT48TXQp-EQhDXi7l21vDahuToqtp0G63QAPDlDHEtTg7gG99cP5ziJioy6h2unaCdOTJhOlzNViIz-m2roTwIobhGcZyYBHeIk3jf4SpnKH6SoTvM9IthBjJtA_VWu2E_XFeaPSVFb3FtApqBdZvE1cQs9Xnj40jrwAzfL_D1FEjLkpoplH2aXpfC54Hz0gQ8QBomX21VKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfdJzVc8MXguwoMBRh3BKg-Ks3pGkpOvxG5846RQQ1XrwaU23rd7EWRCna2Z0DDB7acu0KjHUYGtLJEOXFm04qD-RuIOG2OzTdwAcaXH2ows1BI2jKVzf2ZokCimsKEGhL5HoqLdF1sRJxYd5kGFMX9IE1_cOLtoubKgfkdCVmGOMNqjAnx-Vdgk_YKcQQyFHuen3Ce6vWVBVEU9a4Pw8DTMY6ByUrVd8uhIwrxE1k8aqbdQ-eYJg7LzHhVUCVtJJOKWgno5KOEhhmu4UHx4XhB9axtHbMqFr_VfnMJ-awzU8iqQb9yxnyOGegF5uf0OtD6lEToXd4ODR1eNzr3LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست.
⭐
اگرتوم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e28
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/23803" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=m5WskaPzanSm_PeZ5HTZ2CMgivt4jwR3qe_9JDfYddO1khaXdFKHrr63gvUbGEOCraIKkRXd_X6EGOzmPCMh7xG27dB8g_xLLzohC26F3pSLw2YdQLPp1hmqV9_GUOnImHnL8arJdXyqHHPRmpgkSwseRfdbSYBdESZbQyF2hCRNw82D0ifFxqSwfWhd_mFswRC2ZiaU3x5iUHd0AhFmXJ90Hc9-Zfl_3x_z_ExjeZFDppXesxZ8nRHOY0rK5KSlfFEb_Jl-Xn_l2rYxxsTFocCgKLO6XypEXYcxqbWqCzXaja4MjYE9Vs65xuXjGAY2e-8pRSvZnXBkrpV-T4DL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=m5WskaPzanSm_PeZ5HTZ2CMgivt4jwR3qe_9JDfYddO1khaXdFKHrr63gvUbGEOCraIKkRXd_X6EGOzmPCMh7xG27dB8g_xLLzohC26F3pSLw2YdQLPp1hmqV9_GUOnImHnL8arJdXyqHHPRmpgkSwseRfdbSYBdESZbQyF2hCRNw82D0ifFxqSwfWhd_mFswRC2ZiaU3x5iUHd0AhFmXJ90Hc9-Zfl_3x_z_ExjeZFDppXesxZ8nRHOY0rK5KSlfFEb_Jl-Xn_l2rYxxsTFocCgKLO6XypEXYcxqbWqCzXaja4MjYE9Vs65xuXjGAY2e-8pRSvZnXBkrpV-T4DL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PesvnlNFfCpRVsZyVaJjVATP-CvR9dAca3u2qPcPQiV2d4VTcpUpTMIRAZO-FSnDR0RXfd7z9sXL9q9-NXXIzrQ2Oq94DW26VRuOd9vUXnw17iKpcANNHkKlJP7hgsBr_XvEt7GQxV1Y5KpHDTb1plwsof9qWfxkOAhGSYc8ZnOy68EUMiDJZs3IUhC9dVAcZ19_yZLVQ465xmAk3OobusXZ9iajGlImm6BQwXJLqDbm_1y4JR2ZdN9fLhEEWpex2mk1sDX0H1szjue5aq8UP_3MEuXgogFWmu7NpfIW9cO0_fw6J7Amyx-lgs669E4UtRU_BpaHD5bOBGczIO45Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3rwiXBtF6Ek42FtDB1V5kk_o2FgkT4yyBxIM7HLHIVCfGVALzxuX7fRSMn_NnZyawoFksGtu3e3bpbj9arSKjl7eO52aSjzQly2Z9KDrE380nBPjLGQ2g0TYIaQ0a44GK7pTwi4nGTG340V3VQXSvtcihem_vr1EE1RiElAhdecghNqbEx5ZmFsi06K1-p08CV-BWK-L6zNryuMMqT4UhS3V3daqY5-VJ_3Ea9BVtHZOdeGO3KaCb-rHddGLni9ihb8XS6vZeEHgHR482ygzXQeMsjolZIDNxjX8lD5SA6X5u2R06MnlIV3fN5Xqbvr6Msa8ZuDZHRKTJ1JM949rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlcelT-g190CRsxqAS_XLFuyRMORZA8_YCQtw6BMbHxnucZ3xf4VQglX5VZGnM8P-BQUs5EcHaQjp3TMCAN8eUYwIOTfY-_sibf_p1YHaUTi6rhnocn-mXBbDA8fSkvY8HyP1jrGbtLynuFTVhhcAFu8avbevOMCQRdHZpwCSigkQor64PdmK957XcWzTrcQBCJE9t-UbS2IXm2FTZ7veYfIIBHFVKE2tz4erSxMh1qAxSf9PSJxBNN9595Pgid8o50NZEp0dgBBtNntOJMLTeQsS19EL5uYL38DgA_2OuwX0I4cm8a_7BaRQdmIfW3r1NpNGRO_L6ax5Qjt43iYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQi4fzsQjBWSUbQasUl0BADV9lXlqqCC6pVraB4FbmHNF3F1OR7mccT3lFge11UCY_eIOEVPRdpL0AHPM3TRIVWx3gT0jwqodqhj9ojk_u8r0HhF27WvtmkZLZYFVnwf5w_8qIPRQswMgzFZiAEaVQHOGJFM2qHwOBVEkWP3-IVBfshQGIBMoHMfSf-fNLXqWPqN9OQeBrZhSHjOzF4k7DfuITFmDVZBu24TtE-C4BEQswePszg5AxsUFvpvFtCsN0bRIxJRTeK3HlIDcVJ6cFurV86cr8t0gHdPwXPFQgiXtD3Br8BaMrYNCgvQFmn_U9Hh6bA9kargVUdT8G5QJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRvl_94ZC_XerG7pDEN09BUoUiMQcqJGdM1zjhXL2pSUJ7KJMYyJI5MusZaHLX3HFoxBOFKpdrlxysHj-7Ys_3RHSBXcBSgmrsRrYjlFri1SyEgqCnB3fmBfF-a3Kw29GDisMSiGi3r70PAVUPU3VVc66FBGvU5-uuXnFLI53p3yRWjxP5gTpik6lUyasOgEJsafV1Fg2l00L5L_25AOTyM1ZFxiu1dg9W6_T_lqCIrxiWc3TWRso1I6KbTHLTADexBy9bRKwzOzR-yfAqoNG_mEBJ8-lr-s6ovPdcoIgi_8QKNVkqy5-XsBgUl8Y9YZOhW9TPXY7qrRRhXbFVbXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aE1hjhM2jnt2dCxM_Y2kdjquqhNwc4Jq1DNSm6YR2u6yKen87cZkeXyyvxXoR1c5ojNK6HnerkmsfWeNlcS0qCkMNJMjsSThDsDEbMLUaeDwsKk5P7nKDdWRwEdcMgdlXn8HS68A22wkUYo8b6Ee18YOd0Vb3v_3jUPayXfVQDcYBUyOgf9dHqdHVY2Ga7bJgNVwa9okE6vYgiXj5Y9RawDS1e-tNQflb2rmfImOrubMQVUtj8NCSEFTtX2EvoUi1BsG6TEpmCSuM3Mfzi81phBk4LIRzrBqOv1csgDgMe6od2aeQNKe4W1kF0qPds9ywsgovroQi_RuLDrOWF-W3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaW3ygb42RPTmKXrcwg7GS1Qu0mhI-2cVNR-JpscKgjaPKvFYbigVdFA8r_EbDAC7SW-6PAWoDezVV5yfJvyDMtR315AcgKf33TE38uZPCoS_cbqgC7GQkrRgXof9D-Ajp1WSUsNi0mCtvbYigL6WffxZ33PwnUaTOj6sIrhSRzmcD5frnyHCobwBPzlUAQyReU5Oijd428PYzCrkIpSkq6feUOjy3CyWNZwUZ9AhcVMhEqqJdWOdAECYjJJ1CluZfEbEHMfZ-k4XCyHDyD_4ZuXcbaA8lh3TPZmTevW2AypnhwJUjdsnKsWPzFGCj7mB9Ui66faGfTT734mYGJTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKupMD-r6gVHQEi8E33ct3kPVkr_1HXbtS_h0fiFa-uNvutohXFJ4RmSrJ38-YjM0gkoejdBhhpBoGwCJMJ4UrPICYYmMXivJvF5fzzZXEmaoQuTJqjLKqPaxHed7L_9qoWBSstuk2c5Y3CXSH8COB58QDi1IMvrwdO6d2fNau382aVTvOsvwN1DbmQPlVdZGc0WTAMOjmD69hX8ePRcloPc350oalcWRrrh4mU9nGNFYlB_kFXmu0uMcmOdwqa0ONyyuf3272DCW3V69g5g4e0Qm4sqnj2QyOBc8ODmUj7z81IIv4nPtWwO0d1C0YqOxCDyNrjCKHYzXQMOagjrJCcaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKupMD-r6gVHQEi8E33ct3kPVkr_1HXbtS_h0fiFa-uNvutohXFJ4RmSrJ38-YjM0gkoejdBhhpBoGwCJMJ4UrPICYYmMXivJvF5fzzZXEmaoQuTJqjLKqPaxHed7L_9qoWBSstuk2c5Y3CXSH8COB58QDi1IMvrwdO6d2fNau382aVTvOsvwN1DbmQPlVdZGc0WTAMOjmD69hX8ePRcloPc350oalcWRrrh4mU9nGNFYlB_kFXmu0uMcmOdwqa0ONyyuf3272DCW3V69g5g4e0Qm4sqnj2QyOBc8ODmUj7z81IIv4nPtWwO0d1C0YqOxCDyNrjCKHYzXQMOagjrJCcaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsZM8hCPmo-cuCOHvstd-PDqTpb6HYjlPYWiL-Tj8Nea0MtyQ0o0F7x89GP_usovq9klTsdBWgaFIsMEM4vV8ul7SMbULRC3ziLT12tOy8-ROfQ3cs4AOavJ4TrkJr0sMbLEKtidnlTp2e30FY8J91UOe6BvpHAkptufNjEe7fR1S0LPA3BArVM8SG_Oeq-7LwDO59g6Rgnx62rNAhw-sM8EakUNtiuPJGLgP7fEvEKpsavr21C1hh7SViNU1C_1rsWrV94G6gr8cLaIn3hY8wkcw9nccS98ok1Zf1u4uNKThh2WMsdrdqSIq10hTEwaYfH7Aj0WtlwWVe5gOBuwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqwmEoaLrnPPdnj1Pr3wcXoY4PnnZMJtnT8xbQsB9h62cMQ-XJ0UL0hD4gvDI04CUtAuzY-8boY8aRAXBLUOADASiIkJnJgnFq5EuQ1sc1je8GQY9sgEz0crPjvsziqL_nnVfQvgrCWrTz1LJBLT9BKw1iX1el3FQTekqvhQTL2xG-9OmTzkefYRho76lzk1I1k_d9fUarFO7fg-aDAvlxPmIzOO5JQopyn3hTP3CVZoao9-R0W99VDIis5vmUhW93ZCsAECUiMMT-NeI4AmiPD-Wmv_IIywdsX8Q7F_5RB0QLlSDAM_lIIrgctyO6dsH2HFccy_FhzdaqBfUSeHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYm_EAJc9fJ2EUEGiYpYdEon9WpzAnIIKxj3QBscuMRylcu-VU4gUQqsseQtj7Nix0rSuAEzBUgK2D_CXLrIZAe0MWrOkbL6J8E5f3ywPcsKvmVIsmD7IHWEx-2OJqldVFIN1jxWryykafyGXgqqZ98c9ubndVIsD1ARq6BU32JykgmqOSF7snusSpolX2JpylDhwODp-HfAwozAPqvHnJEHCwyiUS7Qhxk0WneyfneAKYaPnYCrWmPa3NfcFXS6mZNfKMk5HrmdU2IRRI5XbdTE5ZIbwmwkZfJBpGu6OZi88A_5f3Sk76GjaupL_qwMUkGY6PYHfzCSaYINiOpwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2XNJRL6Mh4LfT_oS3too-ZZsX-ShqijxuBtdtucUgifnZByPM70g7BdSO4-OlAaC8O9_rTW_dKAGP9Uzdi02ommtQKbyY9AbPilYPdSdWBtnjBnU9IDN5p9XcsKu_reHSPjLjXO_ln5kLgkeB46QTH44Od-QAfUOrfcyiarfjd3HwMsFKZY6m8tGSvrNzb1-ktYOYtd3Ow4UR_tiK6VYJ_uBvDpJRX94MUmqahE34OMCOo7M85fK2D3mpCEDpDymzBTOf6X3CNiIoVYdJ3ZbSqbF0RfaaLQnTKB3f6U_x8kydxddR2Wpm1fxd0N6LBStzGQVjzf6BesNJ1uDxuD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl_VhYZaan1JHisEsSbdy4hKd6dK9oFmlFxhWxEq6BqdgqE6eYfR1AR35-c2cj38Xu6wh6S1ZqxakjNT-A-ZUw3huiRMC8mKl3KacYUdqGuCuADNJSzPNDrq7JsYv9VBMUmhxujU8GxbA3ubivNHUGTemgCSkF-LPVUMutybPEuPir29G--Xsbd2F2dy-7X8ku3GWLTmBGSbkgFzbeJfnlFQDT6PviQPRSkXgx0FkGQQDPkT6QRCbhzfkBOnjF7KW9jRZeDdAsBVW7kCw3SFtn0cQ3xVVr67n2YcIoozGCRIYnGCtr8yhMJzhMLucx5ct676SV9dbk7st0REJ6YLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=q2B00IyITiJfpMM49nCbpvmNsINy1a9lmNHtNDpjVJlicUAmJSUkVt6OXAOS1vm6DNf4Od_recsPncMhYwTfQ2CnA4XQjcKN4T3BKFiscp3tP8_AXiyEfFoPGzbNmcvE2DrFwGq3VjbAM_dtbRqjhApMP5S8p60FrbRY0l3R5726gnabaOX_hq6PLguTFEB5JF_6pvdTUiLfCXUvnN8PUnCqPtWrlMIWvA37Ka41AuUYbIRJwTJ43DFkkTdaQj6m_ZVJYeruXaT1vCDNFxHTg5r2lVNntaBiMjdKdURkyfaxZBJQaEOx_D7cO6_yY1529uSyddq6EpgCP0R00RjXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=q2B00IyITiJfpMM49nCbpvmNsINy1a9lmNHtNDpjVJlicUAmJSUkVt6OXAOS1vm6DNf4Od_recsPncMhYwTfQ2CnA4XQjcKN4T3BKFiscp3tP8_AXiyEfFoPGzbNmcvE2DrFwGq3VjbAM_dtbRqjhApMP5S8p60FrbRY0l3R5726gnabaOX_hq6PLguTFEB5JF_6pvdTUiLfCXUvnN8PUnCqPtWrlMIWvA37Ka41AuUYbIRJwTJ43DFkkTdaQj6m_ZVJYeruXaT1vCDNFxHTg5r2lVNntaBiMjdKdURkyfaxZBJQaEOx_D7cO6_yY1529uSyddq6EpgCP0R00RjXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH9zYfI95X9y-6Rd0EqqmCVmE4jmjcKa0M8TxckwSuejq0HG15L9QhRyJJ_zlZJWDfPevGZwEmGYlaJRzmY1SlHHWCGdT2fMzdYnXlckCgkhfgCbmj-UupH1aWx1lKgO-P39NI56VGJ0dhnN7i1wVQtVVWrT61v0NqvKvO1gHlRjP-Zu4rdn6oByAyKMNsEmUogfirMy3hxpVSLRXafHKSMh3U_IXiDVF3L3mfAm0eu6NkERcD6T9wluPvma61EB_R0e1RbvvRgJneRPkuEyQr3AHW26W3Zs2x1ZzDnFdRAj3JPEKN-F4a2NUWrSpNn--rGopS25rFxDBWRLL_aP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABvpTG4nX94hpg88y4LF4yuX5_G7iOEHFJ3YLSGXgXQWPv33S8peRq9Ja2Y9gQXm7RIBM7Zksoq7NSdgPQbf8mbVKIefBpHArp-SLtgcVKF6B-5_CpReDE-eZAjIhbqatZ4eEzPy6gayPlvd-xmUxJx2qwm9IRsVKS1s_c1YYyXYubVJbzp9Gek76ARORt79vg6nQ1D7Z8jmh5vsa7XbZQWnt4Fv9a3rkMp8prKDaiUdA9goIDcAxD-KEi2tPJnW4rJnpaGlIqnFxR47fHeV-4w-MUzYuw1JtbCcRuDJTwWIF2Wtyau5ld1DOoRf7Zhxbumg_o0Jo3x74cTh50_vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuzcbyZTiTFmIQS9qV_vHs7lIiT3hXiqjVxUHXhbU0N4Q-g8j373tor5vH0acheTN5I0HdvHoODelcyprs0w6i_3Fxyt1_BNcH3rP7Vie2Lib_LIRW6TH4OwiPOHUYAIAKo99V26yshoFUJ2vSEEoAfL9vWgcbw50CxRRwkwFi7y41pv6_AZQWzflhXEWJUC2KllShuIB5d1Rc3tw-hgrAKVAW29jzc3Pu1p6Q3M3J86Si7B3cklioRol1XYucPAJy5I-jz0Lwa7CvVmWMZeQThihHgj7d20IRkcw26fMtpZMB_oPnHf-SAwnLqjWU211uvNLZ2u19h050eGZTcChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSeoEXCOW4DMF_CgfbIVSt7Ihd3ts0LJ2NYdPFnhvHi1mFlFkwV4YCVefYwWVwjcoHsjQQANIM6qJZjxpwsUA2F6mjzwls7w-Vk9aelVuT5gbURHbZN3iRUsGsqnRnel0XZB9WYE7P36bcNkn10xcOhCHAXOyNTqQaVRnnvTaIDvwAVeWMoQJRgFL-d3S1OWbXifZLTlZ-rLT9c68Pz2aVknhPOa_IxItQSXgDfz9gWWsdsnh6sGfrc1o8Nuet_6po-adwyjMM0AqB5grqPlD7tFxl8YTK3MYVXs_FRLI8gXHchF15mXIm0eWELM2z1mrOlAdaQUqI0SRKttEYLFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3TlWDNZD0KvQE9xGJEfb90JtzKZaeVZgp_nsqqL4adLJnWDW7oR5YIblI8vxCsZ9xou3_w4u631MAX5dakO4h4_gXtSnFzthPoLq15BSBTex0-vAynq7wuQ9wyLxHSNYIfGmgO1hIgLcZVowsUBmEHr_RMFvz4dVSFDYFX1AwbgIXxekoYHHo8166GE90KxZ6v1eoWvtfeshR0uQhII1MS3yoUv2EYzyFPnMEFrxFVlm33U8-DalHPK5fpFQArhxuH5MFnFikrkS8pqUC_3jBF2RADxUxUlEt46Lao1jsrkS7U6L0fdtS2N127FIPzP8OIcQFZh4R2sKvzNHAA0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okL6IhEzKQqqtfstl4C30zrXq3MezdvldRuKyl3Pl_hNxSm8BjmhnlpK6Bet_4DrABWXiUdCtFB_bqg-PleaXibaW1jAXmlCyc4dLbUZQF4EP45fSAf5JiWlNRbiwnD4dzvgrl0B-sM-LQshVIefY2PJTnRvBx9qrqxptTbH7aLFLiCVRLTty1h28rCCRaRs3gVrapEp3g60caRbuCEU5vJhL218SGQTTqrmaAu3dsEQ5n_fbtqBqWJiVhKh7nKn_RG7jp9N6ePEc9BdyHB5cYqKcBEBnKQFptReFMPmdweKJlm1_7b5NCXzHTI9kkMsZV2CO0aBTVUODvB_Y1B9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqY2b05oKTJLQbc8daifDEybBcuBgdHbnTy0oDYIPiLKWlV-iip13POtvdwLfPn3gdQDURQpDmZcD548LZAESAWtSE_7iL7_qKXAO-eKzjU5fDepXmxEqLDGAqnW33misfbGvSKzTVUym8omK-yZ0ah9h7f4RINLX8OIifzivC_KA60aYeq_ETlkYhSgr94GLZaF_5JSAnyDQuyfOnia4N2Ci-ZA-03YRL1WGOyswNW6KuAewMIJXwopeLkLkwiJ0Te0Y37ToZohqIHzSsCZ1QHXASYqYgFZb3C7iLm9QqF2PdccFRqnHOfdz17rJkahyR0CfzXhNmg8HMas5wLK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1CTSavjWo7k2u1M0_7u32FSS6vOe2qSIM3MDchSjNWc_OIW4J2uHwERwFKiz155sYLndbz0AGLMsb6n35XgjYGTiMA29INZwb5oEzsFZvM3fcGqtMFVi_UE31CP2LMVdMDlQTaF62_OuqUzeF-Y2tBn2Vw7L8l9htcScrsnNkr94fTAyb_C2eTyKNt9qkWz7_wZIVefu9nCNWhV821wj-v579uRxgL_9BxmnhCMx4bvVHJJdfH0dQaDhZne8tX2NaQ4P9DUN9SM_mQ_sY80ocmO4P8FeNDdZ5xr_TPW9zPRyqCi3q5RvKXIzNEq3UUI-X2ilHE41CA5WVHvurUMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
🔥
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای‌سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هرپیش‌بینی، شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23777" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4nrKQXTQnS3pPwHGyddFG1ZUi4CH_XLCVON7X0P2FZJtTTtNAS9xiFNnFPhP-hxF9nBMffLwi6wQdx4Ehw9KgZDzMdl8HT8TPAjClibCPpR_Nn8WlEczTudwl4uDCnFGLwvvx_MSfWlsVdEG8jRAgR3grSF7fidax6HkzuM4pGVsVTH5c33yehRuC-HFtVWGEby6A85NZRKi_uBJ6ZWjR9VbRgCnMThjZo3mZHIj3q9N7A5BCWrTN8Lg7hLjFKFXw4WIvXbJd-vcaCXuDhAiMxoZaNsFdfWwb3wMmnpLD3kqRgubr5RsiANBOkwRPpP63CLEnKIJTDuEv3BTJ9cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=PBLVnYIc7bmLhqcvFTTYmcWX1YY_Y5chfbUwkUr_KuOfclWu0SQAQR6Ie-zFhZNnvQk5rq7bL4IZz8zkBGn2ySv8XChTOJKd9Bluc9irdkKmC6FmqWCBJpTfU9jWqT53MYyY-kOINDpl44xVjgRlTdOKzsQfmGwGWxGOsYRgGhKUyN6aC2qRrDau9udDaIcrzpvL8H19OnF4Pn2L1ClXTVL3T1c5jouJQ21MFkJ6GvLxIukHj7cz44fjsxIQU-FyjBlyE10PA1Hi7Q1OOJ3m38C8HqA4AB4q3wAWMbILJOR6JfxeQp_NzDcLGZsISDxjhpbQKxCUQXv0EFGDYlHkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVbvmUk4BuZBUO2lE7wIKJXJ7jw4cE9wZKf0RTs1A-ic2idWufRDDi5BYsGf6lrZ_UYDG4T55MD9c1s-gN7qk5XERNyqbk_8I3kTiYa0TaZGIL7xoci-wfEibFMBXDJLo9dNBEbuJYqqUxYImCSh1eWFsk-7-NKW_f4bdbUthK35-DvMYy2HBwwTg_6of_BSRX9eeUEIvUqCrOq4Vm1rxMX1ZvwaimRtzMLvccpnPTNgneqwqrhIENTPdOa-bbtFhGI0Ar1bqevOL9NxpblUMNscW8HqECSx_33Fi4_HnAGgTJNh46FFZStFUcIl28L_IejY2-KEXFuL82wlfEv-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15l-U_3vSKH-RWfyJTvoCWJkE54EqsJV2YC-gkeDpGVgPqH9-6NZr0IZHw5a0TKtLpwRHQM3ih_DX9HUobbmKx1ZqwfYPWC5cZhfSiwusOJlBPYyO-bzzxULwBoJIPwyd8GAulN55Pku8-ocUOAxAMmClbWQxRHDG1jXW5MocKkRCavfH15utwztWiskhNWipyW-SWXUcgwIMf37RESW1XWTdmCb5OZmQYf8XelNgkv0EYRaAb8loPwlKmDnWtSyqFrvloANREUWqEFuOiFRyKWCR5RPzCXj015IUi1YrG8hhS0ahnJMtWB8xFJUwrr9d0kcVsj2_oD3YmqGh0h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2lpRaC8vVtWlBzA6yVYT9KKzTJP_ttJVjk_l3ofDUuHpScuArnaSANXB9Lj9kArDyi1G5QP97byhIHB0OZIuEa4MPPgw5mLkjbLivVWZnaFZpA6Fiu_j0rtzNtztZ7Xacz0nrc-Jy7_LJpTWPh8PDSGBA1jk2Ek8LeyyAuQDug-bw0oUgOfv42Fu5HKZRF4n5LJ-trO9K4oSWjHQ_dEuWbqBnM3whZ2spivyVxZjHRhAQQpiGp5imIJesrZ8SpFZ3MZq6x8U2sAf8Auqnd74m9LrxulfU0o7GUroEADli02RDxO31YEZTdNrCkstZEttR6if-nxwNG48cst-0PntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHf4Aoy3nZYKkLjz6NiT7FNiUU7xAEf8mUHj3j-Lw0N0jxLEZ2hxNco0nZYeXtgzzSvFlpG6UvSl8Ql7g55hEMDGmSVXfzEJfDm4epeICBjvgzoGDc0BQrBpkVPzEPNU-4Z9_wRgi7TyM4AyhHLY6NoDOWeAJ-cV2GJy8bGsEFJnUKGNCKA3hnWICU0vLENzS5oWqK-zuGPWzfc1b1oQdOlFArJvk1YMHo5j2Fdoc_qxhSaOD107SSAxaGS9yBYulQbvVWvumw9jL5eu4tdmJAOVMxkEA1gVwSg4xAp-aaWoae--tK1layTPCucVrkpu_dvfe6yJAH9F1oqiSVTzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuIYY5Mvmd6O0-fKw_RyiauPd4BiUW8rmtGkZQz_tDtGjts1vr2ZOyw9hiJnJSnfgqrpiAvHYd5Z5d1xWS8kT_taDktvOxkJ_kqaU7hHFuUe6IRCBrZ1X7zKzfytAUaAguyS1pDuIc3NoFL7jZ6-K-GdA0lau3eTju7KV-SNu30gEEw1RvNdX0Eb66hWeukmm2uof-EgNlTfSsEnCEMS2mlRpPddRpYWqkXaD20kfpxFizAZOd8W-zspaq1fhmvkZB5AG8n3PFd5nJSfXyVc94LxuxqAsKXb2n0PiaGxqAIGUhrolbvpIPdzouTvJVTsXL7F_JZn7zft73SfXpHKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o03nm1bKaTDPED9m_B6IlmXg8AngadIBaNV9ot-kx3tWnbXIvjsiUUqXYTJkI5rQFY9u-GPuPCaVourUabo3B9Y9Tqu4WnMUGMhMTCH81NN-KxzXS63HQHzM8poMcFp7Mo2-uN7kbICmL0-cPV13SMktmbp7u8msoBL9S2qW_H5Xk5zZBZ_1EjguOxTn2TmNy70qILFIKm6qa2Z-rx18v7TBLAV7IEvlXlqR8LeoRVE_CxQqJ8qaA-zXrg57LXKqfhk3V5KdFxPEuPgiywjOURF83Eigts22mFfKhqBjMMUA63nsTgXk74QXBHaEO-qZdwxc0HPJ_lSv2edcTME_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=vTIcQJmyVbYseAu1WEpXiiu7VhDNaK4aC4kxlQPFo9NcAaMaHtzPgW0v_JET2zGKlTIQyKj5367Z4wtUFDOI8LQh36juq-pXHu8yDvax6LWnHeBKjkR2lnZvDuRAunET--YjUu52yIRoDIKb6znLR8x27uRgIv14NoY9XWxF0gp_rPYQMMPBHIxj2RX-Uw7Nwd2vc12B7tRjdApiT84IRrU1EFF3q4vtFn6phCVgkzeSlefxt5FTeiZvKS5P6LQu1oF-e3ftTMYQ4rUpPeXjTwnkMD8O_JM8yiVZaCyxhk7Q4AlPtJnKPKv_NEKEfDOLIOC5XChC5ednznh3XRneBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUVrrt4Ol7Z3FYenRbwJYYFVS8ceTcOIxAKNxvRt5lUC7A0FBqQz5GHrTpZeC6Dc3WZeqohNvhlzk1AQL8ro2JVywobtMZt3z3SmJyd-NBgiuEE0puglT5KGepg23gFbYZD6lyC4OW0D9GcjAAKSE2N_FFajhwb-pANl2vkgMAvIXNRLzrfgfLaXHi2AumDqjNcXU7COMrtMVIsDMd3C9opVZWKzJrMMw1NhlTLdi4PP1f8-pZI_GcxZzLi7L2AVlm3ITQDhv62kJPrZXy5osKPT5NLFv-q2jGGWM5t9q9AJWZG-99rEhS4RfUtrPcolediSSCKXZhIYa7lTDVlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxRgnke6WwB14phpJewNMYyPlo7wa-MW0TzLLcl_2V7HVct7UEe1FHWLRKB7D8Yyd_KxDQ334_Zzl31eeLs6zRe1Tnij37PjNIwIIRUZXxvNHclnETP_1RfCIyf_Td3wg6FEn1CA1H4jeHRi9uDPxHHejNRi38bdTg6bataWuSaD6PeMQ2SWTg8WrxnhOxb1de7c4GI9emy4qQFhDG2RW7hVUUhiNTW56Kar5hfq98gk5a51rmagKdjLIUkFz80JDdFaTugJavmzjylY-Y8vuEXnd7DmUAdPEMa0uaixW43F_Zbl9VTz7vBx0BXyNx6bQn4PM50nzrJzSZHYXK5wkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6IAQ7yJ2wxlC8WhqvNS2eBjTs4rm_Po-PxnThdY78yjgZava1FIx-YULz5mCW_qlMrsJPKRLJxMFlxaahBeVhXD7iV1SJ1BvKI48XOv4RRakDuuYhe-YjU06_Ygqko2P6Cj0uXwFD4udayQfjWodEsDwlzsen_l5TAuFDnCmYKaypsKnaPkldVVNxlIFjPumo-Q4_V9hCHYwDwWZqy4-j3IKFA2bxeBq1ZSs0uTybi-pU4Vc61ynGvzpjztgAzbfNt3-9A8NxXgEKoynZaTXpUBFtiS9JoEiJWb5q0s17VQWlLGj-k5ZBS-MiRhzC9qxsSG0Ed_RxZ9lEFqpVS9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQTmxZVMnrJSLDDangbY8G9LGoRpBsvS75ph6f_wIEVR-XhdzIDKS-nCs7gfKwSWcncb3WdQwiacTNTSOkX6uSyVb4coeP20WiInB_htpAjAYJvzKmVQ5nhOXKs_M9ERMpxyYZRHX9X5DQm-kCShEFzUzsq8ULfPuDI7d6foN3wLz-X4laKrYBYfcBJJgFvB0PweFuGVwCqDoN9dZH4uHLAD_VDV-_bWyf7ht-vEcCdpRZ16rXzWsxMb0oNqHHtW2Ih2zzVxjk-WjrlDwazJxRGtronKe6W58CDneeOHFGkkOhCQGYNT47luK30VClPmCKcsHSZ4xl4Lh6vdKDpdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLl3DZTxVGTE7vQFCgzAIZgwQ4Cy0obNDEQUjwNvvGjYKTomGCLPCiY3IDO-b-jYIfHZElV0CFjOMNi3ZamBRGNYg9Xz6Qa30LmZnaYrFSrusFAUiHk87PXSosMjbRZoTCj5DSv9vGaH1gU49-Xl5i6F_SvPRLaswI-scnWJUVFKImGmDZXmz_GhavH1zYK8E0Dm0Z1yFlgFgBW392EMRgHiq3XD7oSobEQoPDZXydApyIUo_EVBfVuZpp0twLWaD0xHLcwVrOxPCyd0fgEDS902Po_CkStmamoNO6jlYh_UOVtYT2HiTzsZ5psfFyLGMg_NbhG0B4iCWeH82Dnjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbDatxMB8qOs2p4cCG4Yh7R1Twf5_bIqB1IwwAIGk2K_ZMr8qT5mXt7PVaRmXYVwqBnM0masUL6buPAnkUD_tIyR8I1ESEqEJaXhcrdNifluYBnflXdbdtX2pCHrxI5LiZe9HfpH-q9d3OcFl2Hv8PuOjrj_7_W9wMWxacAmEZov4HeYYrTw_2TXwWiaDpqwdmE4SedOHHs3IhDEppGJwI2yZXiYqdYW3tEXefuoJTWiK4v6fwJCBZRwaUSafFfT_Hq8YtBZutOXSBnNglIss3W2wvWcMrVI-Nx9fEpJ-wUQBRMNkWu85lR4NF3_e5EtWtNvN4gUW57UHw6P2mwSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1Px5hiOwsHMHiuevJts7jKhlCq4L9cU8F6qMGFs0rbZf8_a92-BUBvCR31GVOfHTRQizATbxBu93IUboiQZiNBZcXa1-3mB47m8YiEnKxUxBL1-cPQ8J-WBnCA9v8D36-ZJiqqWmu5i7lPsgP6foCLtKJBnt__P3UF4aSD43Ac_mzXF4RXHshS3bRzAUnBOO7RDT12YWpa_kdytk2dH5Xetc6Osn7z3YAOxrrGvAdO378eaBHbQ52K1rtJ5mtvLGjPnbI8cy_nAottUBvK6fnaAo4HKwarL60zgdyNwCJu0Gf0AfXZ74EPH-ewldynEaGuBE4ew9CLl8a87b7mriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmCUoKzIqsAjoopU1NE17sZtTa2uECNtLOl2MTnLsumiJ14-hU34jvocss90wnSitsd8Sh7yu44KQ9i1jAp8a5nVUfrWIVRJU7wvrCrN1U8nysv8S9vNfnUY5LurO91cJUVH1aIWr3DutxFdaIB0_FHMBrazExrdseB75d_gmPMXgdMVCUh-1d0Rd6Jvz9bINrPoNAlWTp9bvd16TsNufVgZgE8l4y9v_gI3FsJt0VtIxaGqZaZ3sLCZMR4neF9ftMGfD5JsaxkNDmJjabxL2WpDw1HsOzMUm7Sxaawsr0wu8K7YY2Y8sz9Bz0Je16ujVgKB8twyY7hm2YgqA-WCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=EM0BHskm2Y9oaRFEG_lyQas7G4VxORJUjnbwkpPMedyR9CoKdHcWUJo8DHvcggDvXAf5bcIJB5V8OHFeBy4wUMPNCR7EVA0kGu5nVNDQbVgUAqAkSkxTNv3BVTeGCbNr1V4Dh043p5JbbL7KwRW7WHsd785cXfLd19gwiGMd0o1b6FqM3R8YeqvHvdM9esZkt3kQSvugejRLWm1twTH-mTkXrQDpXqksOv_NCZFu9UpUeZNcsw1WRJ8DP2yLnboYSODaL-5dkMQ3FTC8a8cNoKuPzg1LQLpAOCE7N0XNU2Vzk1WVwPbiR9A9D4ji-jZ3RfVACsgrikoNIM96JO7Fww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=EM0BHskm2Y9oaRFEG_lyQas7G4VxORJUjnbwkpPMedyR9CoKdHcWUJo8DHvcggDvXAf5bcIJB5V8OHFeBy4wUMPNCR7EVA0kGu5nVNDQbVgUAqAkSkxTNv3BVTeGCbNr1V4Dh043p5JbbL7KwRW7WHsd785cXfLd19gwiGMd0o1b6FqM3R8YeqvHvdM9esZkt3kQSvugejRLWm1twTH-mTkXrQDpXqksOv_NCZFu9UpUeZNcsw1WRJ8DP2yLnboYSODaL-5dkMQ3FTC8a8cNoKuPzg1LQLpAOCE7N0XNU2Vzk1WVwPbiR9A9D4ji-jZ3RfVACsgrikoNIM96JO7Fww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMuWAiRjXSHehKW1cGpXwHdwM8bitGHTo-M92cFinxEfe7uhugDq66YwbacM6cNKgPzrp8PA1GH0-uK3x26UQoaez3lS9S1JN2jNnqPZ-oNdOkZ1au4fB4P7DHsQorVJszmvOoVc_VkeS0lsPswUHQd8Zkuv3aHZim1gQIf3knyi8IJ7rmBZVDr7_fRfl-P6bqlpjayClQ14oheuWp-1D_pfi-72-cr3Oi2BVmh4xozHd992Q4KS2ie2XjEVTUk0e6ypkUQsCjZKb2NhudXQw47aL318lKaPEqMFe4iBdV71mo7ZqFn__d28rHNAsUJg4OMnVuKMZvJBaSi4cPhu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzFwNgiPGnROG-A5-GQONUilT7kG56Nc_9-a7mo4oy5A72CVk4CbKrlHG21xowi5bWQzwGjLlI04OzBkJkNQeJBT6tzjdODyM5RNppCDg_X_B8qaSJNG53o0GKFKYBv5dJlX3QntHe1kC4FeNh52kXLmTbIWkdtyNLnH44Z0qDXXzhF8quQdt3Nmo8RsnuvXwJgSnrHoCc-bBdstX345BnG_2qaqYK3490g2y_WYBa6gsMnnXvLnoKAw2tjY470Mpr3rPWdatlA4zwLHeuIgHSZNQ4yCm4A0GlXm2eI-N4pl0SmGVRh_SufNCnmwJs2LhTk7pPziDo4_LubmlTtCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siDdjqoiy1l0Tlo3QYMkAzqP0BJtIQXICF9smqfAyuPaXb6qfUgClYcNzGU6B70fdBNJgFPnVUE49splU4julWw1qonn6XZ2jgTnNOtfQM-JOsVBkLfcTLfBedUh-YaYghXo8wAjQtuoJQkRQhBCX8zhqt4Cay9qP4s-hGyr8_bWVUsm2D9FfACh4uBC_S9oEcJYfl1N4ClmR-OF_KnL82-rK4xgidWdjwHb9GnuWmZw1ulAO_cQ-yArlB-_3_6HOw4wsIcopGBaSvUFdf8HdGgJrCUvtyA9rXLrI3Wkxt4btxPlhkX_60O_GUDThm7AhZQaOWHscLRbj9fdwbXqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnC81saDbK7kgot9iYEV08bTrMvn2AMyivn9v5eEh7BVNngwNXYTs551FSB0ruubBMIS4WfjdR4z8kfrJ3Wnm919igmRE2BjSbmBrwdIRWGYUunSBsjtUlUYarkTVA55-14pyu-hHb8D0j9dv2P6lgrINyNtFXwpsAt9XEXyEOURP8OpoO-PCOMgAzcGKuBCjriIV-HmQfwUHqkUWL44kbL746atnjfEjXXR2IRAXZnUEh3ejjKpV4XzEhSJ6uOnBCdLbZ3Vh2qpiaTj9eEhpI_fVVgt45QRwjv9F6wvs8XNNvtEehAJeC3zwbu8_GO9jxEyKZsOBjAArfxkTs_c6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZubhVT_TS5xLLiSEvOFT6Rwg3YhKyWXoZijMFOe2TjykMnU2rFuV8JKNhdL0jIgcfF7DzsUVtdZot-U2yUo_JhWiA15MtV3wsKPUulAth1y-9goJMAdgxAFgtrUQftBVsspkvxHWmC4nnlSZe-N-brWl8qpjSpSTCc8NZ8brssG4ud774Si9naKTDSP8bLoAmG3JBPQhAoKHeiiBau7sGxJ6rxl_ccpgwoBuiAHByG-Vbt5jFPP61UcHEURWa57siLWlSc7aF93t91WmJlNulMYWuzcjYyf9mN5jhItShHrB139Y8mo8O4XLS9Oofi3zmfq6dra5YcnvnhOv7eiMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkEI4Ezd-AD029QMn10F6FfRE5ZA5qRF7AHN12Dckb5wwKFv-yZOPczfpam6vyIr6zqGsksYtd9g81X98tgyAW7NDovGszq9GnEJNyOy-rYz7OA5Nip7hPgkt3Y8DRJL9ozEyDQYrU9K0yFZDs4Nkh9i86GA5GRyK9sHne45cItZEwNPH5ZwjXcAEXu9w-dNOCen6o6XJD2NJ5G2rqyFv5TDh2SMe1BuQIdpEELQf9w1g2ldI15_3EZheWoZRptVjSTFf-zE6XOm9AcPTxeeEtvWWGfrv2ovBaBm7VOsqjsOKsbU9d0wVQo_W7VVY1hK2sNgadXIqQAvoafaMXlFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=a12vo344YKg55_fWYORzpexjRY3qry9OaWweimlSSMir89K-5PW-B-QzCH2b0Y0AXpja6Sf-aO2CTdUluLV4lJb7gSJXDxRioTG4-WvbrVRl9_fpdKc2g5gH7bQW9ZRPURDhBxVYp1kZvLVa363utzpxUdN6sY4Xvf42hPSiVHzROqALsxoRc8B6bvnGn6PqPck4rhKIRmW35RYSxBkcAkLXWOWsWywtl8GP6KODlaUkkga2Cw6bRVGOVt-OjMnQH75fWoVx6aAX60NuuEgnPhThtnxpwvBUy1i4RDmzn3OzaRicLyIa6x2ljZLeDqNg3kWgdKGmWGrniI3DEVIKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=a12vo344YKg55_fWYORzpexjRY3qry9OaWweimlSSMir89K-5PW-B-QzCH2b0Y0AXpja6Sf-aO2CTdUluLV4lJb7gSJXDxRioTG4-WvbrVRl9_fpdKc2g5gH7bQW9ZRPURDhBxVYp1kZvLVa363utzpxUdN6sY4Xvf42hPSiVHzROqALsxoRc8B6bvnGn6PqPck4rhKIRmW35RYSxBkcAkLXWOWsWywtl8GP6KODlaUkkga2Cw6bRVGOVt-OjMnQH75fWoVx6aAX60NuuEgnPhThtnxpwvBUy1i4RDmzn3OzaRicLyIa6x2ljZLeDqNg3kWgdKGmWGrniI3DEVIKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5rB3q3UOHX78ku-pdPkg2lut_vA4SsFO0lRVbH8qrdYHht4iFfY6JpY4vk2ezG3EohYMHvNmCmIiY8I9fK9jGXe-O3vE6fZfn8EOrCFPE2B2sCAkmeOBFi3i0w0DnB8ACszbX0_UWmBEELYXLHwcj-Jk39_qz2_bbhLbDflczaF8aEaKp9TVt5brLDK1qgKbKlpmmPooeakgSsw0ADhDP5R5xSjTqNokpjcGoUuv50L5_nJGthK651wujnJdbkBte6TrPWF29z1n4VRlkpYMFcFoAjWyP696RYFUmBA4bmDEFlCddaApAFxYf7BfB_P3e2V91c1Z7eGDIa4Lq-5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKaN_qswr7gcfvF0rGieu7mAZzIsYFmG6VhH0EKN94UwMyDhRMN8ovzOCule4t0oaj7OE3PM4Z4NsmWBDKdtSihc0uZANln3t9BZAuYT3rkj8185sXLZhntZDPcomURUaHPMK9l2KFjamwrO-z3CSKwhVCzBmPKepTsL3sl1ZF_7jsG6-ylzuYwXpM0uvAEifkc0s-BTzBTHgtqhlITU_727XaCN2nBxlf66i4aBEGn1ltTzAm78LbZU2p4WLmRkemz7WHwGNJySUiRrSODAB25MtpDjB0iVJmCReTrM_oM4qP-V9j7Vev5fpPZQn3tLtw_APiphyNl9cIA6cWNAsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyLZzXzCa4DRlAoNMQNA3PsQZRhRG-nIBkF3tl-NftmGN1VfT53jKORYsAQJchypTOEzIQaC2mRMpStZhEwI_EnMHWKwtN-MHL4D4Z3-lyLBRiBEPs6ne4bSGJb2_hPAvkJlARcyWcxg7T8ACc5LI8EWCIPROwgoAsmVcR2F58zXz6HkkR4E_TnJVOiEPJRObrj3JyJiDH8GNnqPPzeoBCgU64UioPaTlxkcq8aLV8kilsCFkS2G04M5OXgBEp6RnXZh9z-Zcb1JKyADy7bZAHx01PqiN1pZ7BSX7h7zaYVJ9u03pd6w-68qMCPf5DYebBCvQGj6texJHfNsykZ1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=hMo0on2rX7155K0sdOjE3q3X2wLTG-OpYrzbPcoC6wi6CO8-8fM0mXgj376KFlyya8iqmk_l6RYbyfgLpYKg5svyBzcB9MO8ntKysyV3zuZ051x2XCSTkhDQ26ONzr1TIm5hZtzTkZACoW2PVQ9PvnvvZi3VSofGWuzYv7Db7fxhdQtg6n5VswxMzOwQDsOj_PhwjFVmLeMxTVKXaeXVZ9bNFIn6EFgg9kL56aVR8bAzxxKTInNOUQXub2AfwV5m9PL8ifSzpm-KkB2XJq_9oAy-TQiD5W_9hnP_wEuUUcAt07T2Hzv1744ftimCJJs8UD1A_RrVlcy4C-w3_BpILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=hMo0on2rX7155K0sdOjE3q3X2wLTG-OpYrzbPcoC6wi6CO8-8fM0mXgj376KFlyya8iqmk_l6RYbyfgLpYKg5svyBzcB9MO8ntKysyV3zuZ051x2XCSTkhDQ26ONzr1TIm5hZtzTkZACoW2PVQ9PvnvvZi3VSofGWuzYv7Db7fxhdQtg6n5VswxMzOwQDsOj_PhwjFVmLeMxTVKXaeXVZ9bNFIn6EFgg9kL56aVR8bAzxxKTInNOUQXub2AfwV5m9PL8ifSzpm-KkB2XJq_9oAy-TQiD5W_9hnP_wEuUUcAt07T2Hzv1744ftimCJJs8UD1A_RrVlcy4C-w3_BpILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4eN9CNrOYZmfPd_jqRqbC-XHpFZ1O0zEgGRoiMA8r2dh57YNmKB1lrOeYQXhZS5CysSBUfrHx8ImrzQ74_YCeBT744oLhfzJ5A1UHTzJNNiaELO6Zi8lMJH-V_N7qqsOonPAG_9vZB5xdIpxa14ROOWEu-f5rfSZsrEroJKzJh7MN8etuPwEFaHhacjHrt6tT6QIHksW0_Ty9gIwsaCYw9iLszaxoLJe3PDdnpdFCZ7cgLj1PeEmKaaz_Kw3QZVHB6XlrqM2kNiYKCmLBx5EM8sgW7Dc1Vin1_nrCHzgd35as3M1m0gdHqYqmBkYlHzfGrXUmCM1yd19Dbb4e3qOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzJlBw4Z27wE8hoTWxvMBdEHU9q-zxAafEUBjjzNjbSdVQKe8k6sIJWIBL5C1QBXDt_cm-rWHIhipF16bCBHgdo_GfQooHIjy-hGxXmSu7KgHduo1aS03WpHETAqUjNayxwJjIGOPRBlnAJCN4A-LPXh-mYb1IPCGBrtU7UBtHZvSfChQIQLymbtkd0mGcjDiGKNiCVr8YLpGi293Wigz3YSqJb0frW2VskFqoDvMoNWM5YGZmI4NTss3OAtvXyh_QBrGPP14_SBPajz3Qf216CVXRAirvBnC5KorKJmAxrpL4oIG_iily5wljoXpZXqKCn0atCOpTdrkioRNCZiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyNQm5gkYV2ozeNgoeMR2xUb0hLMzyPXKSqWSzNTOt7n9DDR6H1F96htd4k0OpXqX9qAgAFqojfEnS4iejBDXUTtV4FD5HDpjniDXtd8hVs0EzaftVELm_5LKeSg_EZ04jV-2Rizp_xTgKQ0U96DZN7IMvMMzygw1oZo5HTJ5nx3b4RqMC2Dt_U1eUhghb0oO_re78f1N4543vk5fcRBtGrvS-NZKZs4yTACgCTfKIiynxd40xleNQa4fsTkJjJzUoQtb3EbkUba_69OSb4NRwcP25BjTmLle82A3-v0WvSQoDfRGc9AytMi4btJPPaz3Moh6SGT6ygLvKfppLJfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=E2GqwgZHri1xULDknQRpLovwV3LHNG4zDWOyDo_mkS-Zd8xoskcxzyMOg65GE2cBf_FSR9ARNa6ZXC37eHtE5eFHEorJyaedvWtssf-EUN2Pc6jV0OcdtQbMXJqcfslmy6NnCWLz2s_l9LvCWFrU1Fd-1TY6pMhSIbh9QY6eXQlxaF7A0S7fiqO3892-7u3fCrn_NXaEpYHlBOxi0muEF128_bkSVQenFaGtiR5eJ4a-tHor7I2BGm2isjuTPoCbWdFnhKuLfk2QFKLW1aJVtrLqX-zWmotjzgszYGv2pCe0mEd2j195fqGCDHHJZ__11bXlGlopLpkyNquTEDb6xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=E2GqwgZHri1xULDknQRpLovwV3LHNG4zDWOyDo_mkS-Zd8xoskcxzyMOg65GE2cBf_FSR9ARNa6ZXC37eHtE5eFHEorJyaedvWtssf-EUN2Pc6jV0OcdtQbMXJqcfslmy6NnCWLz2s_l9LvCWFrU1Fd-1TY6pMhSIbh9QY6eXQlxaF7A0S7fiqO3892-7u3fCrn_NXaEpYHlBOxi0muEF128_bkSVQenFaGtiR5eJ4a-tHor7I2BGm2isjuTPoCbWdFnhKuLfk2QFKLW1aJVtrLqX-zWmotjzgszYGv2pCe0mEd2j195fqGCDHHJZ__11bXlGlopLpkyNquTEDb6xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxlYJpLU_mbFpml5HDjcsuIjX5FXpcNYedBJPv2pqGG_KX4wehMgv24flt1KXbR7x3GVPrRtV26PrgclFV_H5FzQp7TzV77c0RZ2oOMu21hn6T-lM56kh85CQ6UoeDPVRMpWrk_hH9o9kuLqI7qQBVlaWuxmu3kgG0kCf0OlO1WHG0oT-8ccvz98taRRW_oOunqv8lJUYdKwpea5qjLULkDUMwcU4BIAh4Rh0l9Ik0e4cj0xb43AXg4YFsmUp8Zx8cwuMrNfY5vbpJGpQuAh5_YV-MXqgMI9qx4EkNKnu0xhki98VfPw-sLwUmkGQQo6br4y20CN4Ez-FSl5EGQduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQjD1m0mITVmBtuYlOqfB92jjgtuUNUz_57eO8lZqwosJSiF7mPwl-vb3Du2_GX8AfZEAJ4HZ8ImzXNldl-Zk41BMymsbTk1gHHgB4R4FHh9ANVPD0AJJA_RUq-40xFt7rkjDdJWcKU_6_hABb7Efgu7r9jYNeJ2KKL-smST3tHm0FrT-HHvbxcqBX0-ioiadCkFfGc33_0M0rEOxlaeS9bFBG-GHo-wTaQm0xrliMG75GMdG_8z-d5jPxpFwtwd8vGEbguFuBPglbU0SBnEeMDN4uJO2lghuycEQ6fE17EYLbKNE0vT-dfZEkSvotLmk-afTb3QG_yVn2FuCIqZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_ZJqyYs9t1FeNvOq09A6T8Z-UkHhN-yysLcFVtXfUrBVEvRTukYfd7bmVfVp523iElTp0eQXLrFv2g-B3bo67PbjG-G53U-tPrXWajG2bGGSeLBJiDeYdSNPu0JcFPX733HySYk8FZM5Gvl0MHwrTA0ibsd3II8JD7_HkTJLT3bUJRUQEvFocUr4F3G1ETK10dhCs074i1oI9dVWze7YnXfPDgtRX2hs4ptvmn2sFBkRO7er228Nt4bsGQ4JrZPkPp2w8iU9VapceQoOVzTH_iRpNDiu0gYS34U3rwh690xlbzAT76uZY4SGb_1BZXQyZU5L_s48NVqniOJuwCaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوووق جذااااب
سوئیس
و
بوسنی
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEbc9pqw83cQF0w4p7ruKQvfleTRqEVAlv9gOp0n3aLdbPu62m8C-WCrJQELE2UvOG5vcfU7WyKRyIDIgfoEujZ_eLcH-VPKMprvSw2vg1ena8AnxhLPpbN46--BN7HoaEB67xKh_2T8KXzc5q5zrBKfkuWD1_FvdoViAN8aVkWDqwr7FFr3pWN15PCctUy4LJLtBq_bk0aikedqsaHUV0JhNX7JFBCNefQ57CBqTOdTeZNM6GTGyNR4RYMNvRXx3usyqIL1aBNHCMkX4SDZaQFDWUEA0VeTQbfsCnP1Awkn4FLSBvUNNEtJOOtLn5-IikCXIBJ6-1BNNG29n39IKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=GuYTxTdMGlppBFU6K6_B0NHvGd1l-GmRewr6J3cRsn_1Anwq48t1BKNeiW8T0Cyl0_8G5fJ21ftDOhzenOip7l4qcoC9HS6dlRizqUj_eT1F7q8WoEBB2N6O8LslXH9-CDpR6J2-o1FB2yUc3zjifXTSdzsyN53mgGpo5QytVs212sK6YS3xXDFkYQOun8qIIdg-wiDfDLjZfjWNUjnsS11NhoTj8O69Ju6dR3HZ3cLtnIQlBkdBXWNdhtghKoi-lalO-Rp919cNPgzMQP_btpcoqc0YQXChokHBX3Sof9RqLnKBlkMSxgauW-6HHgFz7Vy5iLP44zREqyccBBN1BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=GuYTxTdMGlppBFU6K6_B0NHvGd1l-GmRewr6J3cRsn_1Anwq48t1BKNeiW8T0Cyl0_8G5fJ21ftDOhzenOip7l4qcoC9HS6dlRizqUj_eT1F7q8WoEBB2N6O8LslXH9-CDpR6J2-o1FB2yUc3zjifXTSdzsyN53mgGpo5QytVs212sK6YS3xXDFkYQOun8qIIdg-wiDfDLjZfjWNUjnsS11NhoTj8O69Ju6dR3HZ3cLtnIQlBkdBXWNdhtghKoi-lalO-Rp919cNPgzMQP_btpcoqc0YQXChokHBX3Sof9RqLnKBlkMSxgauW-6HHgFz7Vy5iLP44zREqyccBBN1BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=ai3WVB9mHk7AnLiFfD6IBx-x-fhYCieNEOve0bUJO4Sv19dkCkKOWcP8E3kqquq7gBo6jfNo0T1mMHzANXVNq6-lbs7roiujQq5A5ZktFcN8DoZI_kwwpAm2NU_ykTG8VFmWyHvfOEoi6gpipayXDWfAFJQZUY7NUFXdcRVxxUKk9u_CMZTwN8GbnsdvGBUTiFnqx36kEZRTi1v4X_Qwkp8WfYj_9iTPNlkTBk1ZCjS4x2GfX2oDm3yJT_HA7Z43qXmsrJiiaZuzSZNsMjVVZEcjjTzd0viUAGHvVPgdXo8zUCFLGkC_o0_Tjp9Mu7OFaTx36nh8hxQwx6e1Ab-sXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=ai3WVB9mHk7AnLiFfD6IBx-x-fhYCieNEOve0bUJO4Sv19dkCkKOWcP8E3kqquq7gBo6jfNo0T1mMHzANXVNq6-lbs7roiujQq5A5ZktFcN8DoZI_kwwpAm2NU_ykTG8VFmWyHvfOEoi6gpipayXDWfAFJQZUY7NUFXdcRVxxUKk9u_CMZTwN8GbnsdvGBUTiFnqx36kEZRTi1v4X_Qwkp8WfYj_9iTPNlkTBk1ZCjS4x2GfX2oDm3yJT_HA7Z43qXmsrJiiaZuzSZNsMjVVZEcjjTzd0viUAGHvVPgdXo8zUCFLGkC_o0_Tjp9Mu7OFaTx36nh8hxQwx6e1Ab-sXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=KzZSPHlY_0XgCO3rJdVPjzRW-eBPKODRT7lb-uaP6v-jCHdT7djgkcLZH4pTTk9xfwt_3J9htOYtej4v8bVEPQ319rrx8E8u9CCOSvK3fBVRvLLAdI_hPDIzPU-Z4rDmWEYcsbrA6DCR1mL6To-c0Hpt-V111sztHM3699hPJlRqa4ogwxHNUayJ7_kSz7VAvGeh6zf3c0Vsykzd9hkk5AHscJNuBVHjju5_4ig6k1mw_WJCX3JdyEQu9KdGBWDIM4BvLaLKwmNo2SVZAmkN-gNcczhYXswlhSqhajAa6N5e3EjuSjTbzc5yyzspN1cfAmUxfF4RAg2cTlaY3f-hOgMh-jKug2nJQCiFDzB5bVqMrymWLA1RWnqRmCax5A1kT6QMQIiI6vs4z5obW3U92YSSy-Ao3iCb_ou0hyGRsxVBxF_jS_SP7zpBDeZ19it2jHNA-UDt2gNrc1YB6L1jxgNRg_UpynWoPmfYskDnT41wUYAsRNaTz_Z8FMGO6jWlyp0oUBileKXEa0Mb9DK9Yoj7TuVJJqRCDyliNfP_obwPh_agLneZzix_cYqNkR6iYdpcFcSQfmq8t1I6WOcJ689qIeR4AyHQ-Mbww_dlLC5Ka7AKwR0DQN6jchmsRbSAnBiW2ZMD3HaJn1IH-lcvAYrZ2ePK8hnY_pNHF6jccA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=KzZSPHlY_0XgCO3rJdVPjzRW-eBPKODRT7lb-uaP6v-jCHdT7djgkcLZH4pTTk9xfwt_3J9htOYtej4v8bVEPQ319rrx8E8u9CCOSvK3fBVRvLLAdI_hPDIzPU-Z4rDmWEYcsbrA6DCR1mL6To-c0Hpt-V111sztHM3699hPJlRqa4ogwxHNUayJ7_kSz7VAvGeh6zf3c0Vsykzd9hkk5AHscJNuBVHjju5_4ig6k1mw_WJCX3JdyEQu9KdGBWDIM4BvLaLKwmNo2SVZAmkN-gNcczhYXswlhSqhajAa6N5e3EjuSjTbzc5yyzspN1cfAmUxfF4RAg2cTlaY3f-hOgMh-jKug2nJQCiFDzB5bVqMrymWLA1RWnqRmCax5A1kT6QMQIiI6vs4z5obW3U92YSSy-Ao3iCb_ou0hyGRsxVBxF_jS_SP7zpBDeZ19it2jHNA-UDt2gNrc1YB6L1jxgNRg_UpynWoPmfYskDnT41wUYAsRNaTz_Z8FMGO6jWlyp0oUBileKXEa0Mb9DK9Yoj7TuVJJqRCDyliNfP_obwPh_agLneZzix_cYqNkR6iYdpcFcSQfmq8t1I6WOcJ689qIeR4AyHQ-Mbww_dlLC5Ka7AKwR0DQN6jchmsRbSAnBiW2ZMD3HaJn1IH-lcvAYrZ2ePK8hnY_pNHF6jccA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHf2h9NzYPMz4akFF11WT5gNXLWcTkLDI2x15I_d3q75MhGAaerpaAz6-fhfrt6ITQOVJrV_aCsdtN9OlXoKnTRFO120P9cqx-O4R_dl-nd7NMtc_jsVYmxsuDiKYq7CkksO3C009Hr2ytrOt9VtS3SVT3p9hxkLbQAezBuYJKpyOUUskW4dV3CQQ4z5FToUiupkPBz6244UaWBwyIcswYDiHjzWLoZmf0TOeR2588-C7G4Nr-GHArPoNp4wq1PpkoGMsANU0VtKKV3irreffCJaZFLkaGDD0mIWFyGoQHacxHVEHObOkx5a9XYii9R-b1r15vRdA8gLhJEyVddesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr_VzgaY_bAxpTjKH6f4ZISyinGLJHFqM918B7pnTwzJeZ6nfdnpiSL-UsBjV-lCysUyx9X9a1we-rIgSiuCaCEOWga73c4i0sGzkKB3TvSxdoQZaBPvCZuWwGugeNx47WYOj4ZUAh07gT5lX3gABSSaQ2H8LY9frBd2VZWqFi8UhBVbmtORiTjcJNMoV5_sM5uVP_8LdLw4nWX6Uo9ph4acmqEaegDFP5MFPTBHoPi4Vq_1xr6w0r6OCCMVLw6CMOT5qWZcIIJDC8wdycY_y2oARJYnlVUcekIi1VEYn_gB1DFfxE3NXrvpRrFdpGJKPlRjLWee_gBInbh2BCfV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFSY-9BHvcoXWSIC0agsInsS22hf2vYDh_SAv72WSDp4bZlQr6c77racpNsG2_--82F9n3uUtztUzyJDONl75b8z5rHj8d7bLcxXvCCV2F4fPPsOOT0TK-T7bxzVbqCXWyel94wMcxush6vRw1srxOdRE2rR70f73-VTLWIHy_iJWGk2XJEuPpnopuVN0R9RhZlIbT2ryIZiTBpiM4obYgJ4FbcYx1oj3SFgN22Ys3Xsu41u--13h7ELHVN0ysL6fNJy5l5EG7u5O-GrSNu3j-uSSU-aZXVlSn-2oDoucy7DT1hbj-VFYsv4Ju7Vg-3JIZyqNT3uHN_JCKIkSBhm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAwhc7oCUSSP-WUkyRtugYpfqVy4J7LymEt_UIp6TRKlHuFgbuNUiEuD1A7yOBWrUJ0hXKmz-JXtNIAZfg1g1ABBpyGAJagxyvnWuCtbajBD6SoJWtb7X2E0fcaNWsMLfG-W-RWr9ZnzO25MIyOsBH4HlNlGJn5Agd7gvdCk-RcNNkR44NC-O8pizqMx8-fnpY45wiIAoh2E318vxmO3voYyb6AZJlbDr_YoAZpSlnJP9JqM7hoPYo4b2rZ6Jr-a4pZlE7rBvFmQzGrWgT64BsI1OJqwcBZ-B-dsxeh8IV4ekck8vAMLDGRGUKXLBksDxmnEOCrDhHX9ImuRBr6Mlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcWWto5h-NMdypRUFEfg_npobQpglpuVhDH4Ih8zFy1Fs1Z_Qp7B8K5_RyfShuupWDJ5M-A_quhW5k_K_GjBm_kAo0zHGMIf7JOZPxHVu86OKXMoKQzvIikTC0KD58gN5upDL_BaYI4tC6-hWEhPj8y9VYeMUV59_jS1Y6_wASGstVrJn944gf4PbZJywcwcW8BL7Dw7pXQR-cCZB6YJ1JUUSlzs8i30K36ndgJf0_lfYZmcPkgFhj2LpGyTfB4CLBKnHb5K-Djv2Ck4clfECZdVL8lI_T_BnWM6zML6tXQrTeEHkmHbwl5r97xP5PNL-s_4dT9X4SyA6FIt_bCyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihb-AnW_Gy2x_6PXrHXDsk7NzDlOBesr_U7TxLIK6Lcz27EuQZVBkKVdabCrBabRS9Set_AT-tXtFEMy7G7gFWvdQHRdJn3z0qoLzxjO_ME4bZvCCcqd2vg43A5eSUV5QzPjO60S-fd4ReHVckilCF2EQnGplxXCd_x6mfBWAZOi_q5cB8nsiPflr4kwnuREocT7pf3FZj9i1Y4WxJM4LR9O3auAQBCvo_xITjBYquUa3tXZ1cT9vWQuYSDe0adXQcea6ZsU1MbuONmCN5ew3yVxcx9uHpIP7P5pWJMSCbC5sLF9GLooL3BYEjTqUoa2BV7aK21Vd0a83GSX9DrvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUKG6ro6ugrtNleEsSpiV_NGAZsdjg_TXrSdBFddwdWqkBvv_M1Bz1_CN7UnoO3sjNwPEsUq_hTTl7Nt-UqqlrpQ13F8-XrYdq04UcWA45K84WNoeByIHZ0uff_yEIy-27CBvDisF26vVCPOwsSvbTzqJvFGVmPsZPqtacnFgNofaowZ4b56MDeZ5V1vrr8cScGkSry0y2ioJotoF_17hteeIGjvXxssNEIFKevYmey2y5E2YmjoEOAPXn5TzDzjw8z5OewmoUHJMuQF56bEeSLrCFlvqVFd7pPjwicQBLicf6QOdvJE_0sziNnTIwc2mP7GzKGV1m9TNQ-4QGVrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de9fZzXmU2-SHWpFm0YbjIrhFmnGqustgHULB40JKjHYQeMEbFh8TG28STygO9vi87FlvQQZA4oO-jBKt_JuRy3ppQBYh6ptNYef5NyKiW24zwS6Ue0vct38dSUvwJ2_cEyCaHuPf3Z--4UkyDNFJf1bsiSQkqTKV8fkFdWfUSmiDqAmrsSor9BkvPr6-LWhXV2A8FppfvaTnHP5Yc4vh3CRu_HG4bL7KC6hrNaU_xdgihqQNggZklgVRDPXSQxHjbwPgKVueloDnn2Sm_zUnVNbxlq55R7Y0dKYilmTU3w8RmLSLSuG2qtiIQNjDaTpuDAh02BK9kEkZgJZZLT0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=HshmGiKWq7c5e5KTE4zC1v75PI-FvjAqqFwjXURF-8rzxPLND7E9rENCpCo6nVX-udzULwnA7Ir8JCCyFWdcwkO7_J88pVSeQfW2K98Mms91oIWTw2e0kMgmtEAuoqr1JEt79YspMZgJ8GqyPjwtd70a_xkrJKuqmiOoDq2Lh7asUi3DO3G4Dj3jOVOVw-Yu7g69XrtQzWAVHwepme-g2WmsiTx220XHw1p0lmuCKUq9ibglw156Qn2uJCcqm8MsxmB9b1GTB6Uj3r0UN06aR2xp2WiVNTWyzdxzfLM8t0alJ5gdkoJn8y2YT3cklLtedOpsi5tRn4m_ZBU7EQpJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=HshmGiKWq7c5e5KTE4zC1v75PI-FvjAqqFwjXURF-8rzxPLND7E9rENCpCo6nVX-udzULwnA7Ir8JCCyFWdcwkO7_J88pVSeQfW2K98Mms91oIWTw2e0kMgmtEAuoqr1JEt79YspMZgJ8GqyPjwtd70a_xkrJKuqmiOoDq2Lh7asUi3DO3G4Dj3jOVOVw-Yu7g69XrtQzWAVHwepme-g2WmsiTx220XHw1p0lmuCKUq9ibglw156Qn2uJCcqm8MsxmB9b1GTB6Uj3r0UN06aR2xp2WiVNTWyzdxzfLM8t0alJ5gdkoJn8y2YT3cklLtedOpsi5tRn4m_ZBU7EQpJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=cXvbi4L9ML0Cbmvv5J11v4NepUrVJvKjAHiVsz7AjIbuKw5QgFV28wmNH4P2yPaY5RoQiPw0pZVi6PH8kf8ilinE9ydX5PPlxjN-6-AXiP2UNs8F_2aXvQGOAJ9zacW4fjWyB30-5_sK6s_GQdVeAAKgkBs5ge47c9p0tlYr7z323TbIvhmmftI-Lf4fRP7dMWpAHrSDfjfrB1QnIkywqZ8dbPii9Rsn9HjsPpBVrsgWRLMQUNqaEe6urOx8EJFzC2su6idJf6BtkfoNKl4_JNavHkiWQgRwkaJSKTseVvL7bLXq4n570vg8Uvj8S0js_UeALJG9NBloy5S45oGhMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=cXvbi4L9ML0Cbmvv5J11v4NepUrVJvKjAHiVsz7AjIbuKw5QgFV28wmNH4P2yPaY5RoQiPw0pZVi6PH8kf8ilinE9ydX5PPlxjN-6-AXiP2UNs8F_2aXvQGOAJ9zacW4fjWyB30-5_sK6s_GQdVeAAKgkBs5ge47c9p0tlYr7z323TbIvhmmftI-Lf4fRP7dMWpAHrSDfjfrB1QnIkywqZ8dbPii9Rsn9HjsPpBVrsgWRLMQUNqaEe6urOx8EJFzC2su6idJf6BtkfoNKl4_JNavHkiWQgRwkaJSKTseVvL7bLXq4n570vg8Uvj8S0js_UeALJG9NBloy5S45oGhMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=R9VeF4ygHVhPl16C-KMxQ2YFlLfl9rrbxsRfmSeySAJ4aL6KEGuqR1Wj9kExw1816gTBU8hq7AGMkJWZWy8zAWoAKlSBK2hXT-PqALrUKonI-y0SaNRMsucEw95oGqGmqvBMQLrhIIF4j9y9JTCdzpzeq4-s4mEFEuYAO1z98JWJQWuMfSQ5OsikzWc1wQF8zhoEY9HR5DndaQx6_nzAmyUxKMUhcILiYV7lyuI9pKXM4EiP1ntuB0trb2TGdZ17SzKrm-VLUtuv_PF8kWaS0iZPJhfXzjbhd8SdQAJz1CHyPEzHqThJdmxHS3JwvncHlbmPjfApYjC6zg_YkUC0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=R9VeF4ygHVhPl16C-KMxQ2YFlLfl9rrbxsRfmSeySAJ4aL6KEGuqR1Wj9kExw1816gTBU8hq7AGMkJWZWy8zAWoAKlSBK2hXT-PqALrUKonI-y0SaNRMsucEw95oGqGmqvBMQLrhIIF4j9y9JTCdzpzeq4-s4mEFEuYAO1z98JWJQWuMfSQ5OsikzWc1wQF8zhoEY9HR5DndaQx6_nzAmyUxKMUhcILiYV7lyuI9pKXM4EiP1ntuB0trb2TGdZ17SzKrm-VLUtuv_PF8kWaS0iZPJhfXzjbhd8SdQAJz1CHyPEzHqThJdmxHS3JwvncHlbmPjfApYjC6zg_YkUC0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQxMOrV5LQ0gCr6_4XVXkkGD5X3a1lrhuHK9mIV5lfJh8CA9mVFEOPnlCXqNNJ19tdOe3D0RL6dw4XZjj1UTxAI0f2cteTJkzIcuBWQGgfwMlMCdfcnWj2Dikl6KhZGTCa58nsd05QRM9MXdl6JMqL41YMR39cTzl4BZM6Za70c9BGDzUy5MGbxOSguczQX8yqjT-nCiCxjiPJOiMbmi8w1_I0H4aQOyeFWhx-GAlvki5nrqVguBQn2DGHEfOBn0yrbVIOUX5qg-tVrihfgFZT6sznuqJrHumF34nSNk3y5iV6B4Ar6_NAPZiGblquaSL2n-OvwkbLKZKOHIpQ4lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=FHrY9EkyfFgkgiJ_nX1aqkcevFOWyRasgAEvXvyCOtJNXULX1PWeTAIHPMt2UIDobrZBq3bX7keS_yL-4OvVULh4hwZRs3BqhOQ9eowe-ace-bmKcxk-1X95IBgyVEjX0vwvqzMUe9qYJ0OgyodMBXUdaAFS_lhHFaRrGN0Lyg-3uzFhp7v7auwsMsaMoucsijp4Rj6BNaTRdEfpAPiKfo2IxfqNnAeXnVQi6t9oXjV-P4YJmtyQxvELra07uIaswhe_4PdJwQ0yKabGXVKICwVVXWxu9MQpkTJAgGzrHhv_5l1HpdRYbz6nHfWdkFfNOCDYPamUDcZezXD4O7-A5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=FHrY9EkyfFgkgiJ_nX1aqkcevFOWyRasgAEvXvyCOtJNXULX1PWeTAIHPMt2UIDobrZBq3bX7keS_yL-4OvVULh4hwZRs3BqhOQ9eowe-ace-bmKcxk-1X95IBgyVEjX0vwvqzMUe9qYJ0OgyodMBXUdaAFS_lhHFaRrGN0Lyg-3uzFhp7v7auwsMsaMoucsijp4Rj6BNaTRdEfpAPiKfo2IxfqNnAeXnVQi6t9oXjV-P4YJmtyQxvELra07uIaswhe_4PdJwQ0yKabGXVKICwVVXWxu9MQpkTJAgGzrHhv_5l1HpdRYbz6nHfWdkFfNOCDYPamUDcZezXD4O7-A5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWYl7j4uh3g76s-y7JXjKmF3NW2AAsJ-ZqvQvjeuEF0foPYGOHBQdXr-I33I1CMXUrHz4MhUY8aJ4bNq3MTpOLaLR7dEW93GBKSLarmzxCKp_L9bf4qBQa2hNP45aU1Vnt46UdnqfT5cgd9j-hTtZjdeOPljSKe9rc0O_-oLB8bYcgIVJLv3OkfjtDE_AT_SfN0aVFO6ELYJ3F4lhfXmPrPVNJCCvHK7AJTzCUCxzbQH3YdrFrkS6aOotOvr4PdrKLOkUIOYwsznZxYHnN4gokyIzrueQZuujQZ2q-Mhaz7cX2JYU1MN11OENdjGy7qMF6ny2gSrFh4L67Kck5D2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgPtJek-tl13svGIjuWJ-K6fF4I_xi6zrYbKbrRoExkcAd_wppKl1hcOISqrcEUCKZdQYtlBRBAivOnnRlQHpzpLwxFYJDFvVaoj5erRkvZsGCeZEgz5mLnZpBB-4fCfS5pbZVXsqO7P5dQQa_6erRONs-T-k-loluDMvBBBz6Q7P0oZEaIv4CYS_g5ewK2s0Log_VDoL_tdhlPVMAGOD6yD0-PKAs2l1u3MDZJBiuz2sm2fkA_VwXd3cy9ST3xcnzwypkaET7OnU0FQ8EdOyG32m6AFK4n4AUfHPGnl9m17F3hXfI55p6F1BFFNX6ynN73uLLDrOKDC8ptWPQP0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE2oLnCUXoD7wlYW3uYh9VYY7OBBLal2Lb_twuCXg9gbkO_2ezLv4ItIqoCYtdzpfWkfV4vznF7nPWqq81BkWL-tEQRKqhccsgxtV5ZC5SgfQcN2wyGusd3T5_RUHqvzpbDxLJnRVmw6U5f59Itg7gqVw0PRqH3KOm07Dua9o-d6StGhizd6XQG-4iabAX0N7e8tcSP68jl0H1IP2lOoNN01UKCDxFs9y-aP1ZoC96N40rY-DZHezM0s3z7ilti_FA_OQFOzc5IKK0Z9mH8wSrXIoAtnZ_bzPxB483TwFZAwYk6GHYtUE4hgpNmmx0Jdd7-c1_af-i8DStS9sNJapcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE2oLnCUXoD7wlYW3uYh9VYY7OBBLal2Lb_twuCXg9gbkO_2ezLv4ItIqoCYtdzpfWkfV4vznF7nPWqq81BkWL-tEQRKqhccsgxtV5ZC5SgfQcN2wyGusd3T5_RUHqvzpbDxLJnRVmw6U5f59Itg7gqVw0PRqH3KOm07Dua9o-d6StGhizd6XQG-4iabAX0N7e8tcSP68jl0H1IP2lOoNN01UKCDxFs9y-aP1ZoC96N40rY-DZHezM0s3z7ilti_FA_OQFOzc5IKK0Z9mH8wSrXIoAtnZ_bzPxB483TwFZAwYk6GHYtUE4hgpNmmx0Jdd7-c1_af-i8DStS9sNJapcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf4MIolTNXUMQCYlNDDvOJXCuj4ERHw76T6zeaPQuHdjvpuLkDoJKjEsxIZjFKDwkSMysZ7dQyJ6edlL8T67vkeeRXD1IDxOMd0DJ5rwm0QAsHvpKU3q-UFGeB3mmnJby7YR_tA7ohpJg9QTLaLsD-dn0tIImMq1GA2vb_WIKUOadeoPYX1En-cMccNKG20_xtsyTbAGmrTOIR3cqIFWdcwQwuyEoQ5u_YGc1S1sVuO_qwyz3EERxsCfB3V7NrHcTp3WdhcD3xI1N0bGTpUp65MHagDQQO5hrUMQk1aFqdJUp-QkXocq2S38vP_pWzMXjxayZDU_JRB1KcNzGiXT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nhmSzYeZosEX2G4sfNFoS8DTBlfBqNcyoNm6_AGilRY7A9so3Cdy9a4wEsNLGGohA9o89B2wSPYT-KkYClXgwW5QqZ3XkfcIhuhfhEG2gHNpevxnCaAExs-LWKSIGsBRqkPNyTWg2xYLqUi6pYzrUl5RxKPRYTbo2LUS_TPJFCqLHJ1Tav6-vHLJXjUIcM9P83PG-j0BIC8GotfqMYOX47lkNmKEXnNujPvWns8bLyolitMvB49Kw2HeZguWkUxejNBHeg6HgmUjG7qy2uCLX83nvchWn_UVdZM9IMNK-9bdCA20ukMGFx9UlINcTdECY7g61NYi0CtkkzbEeiQQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5wupYlM_2mRGIakCtCeDEgJGDjAn-BdOJzZ5AupUNNLQm3eHzI6hEbSMLfCuf_uCNxpok4ddxq-28MxMOzlGR-YL5MRU8wExnX4Nnso3zQUwb6hfpy8w5xB9uXki38CNOb9o5MFAJUjMAie5Ek0uN7Nud7G-M0ka1wsAoffUiEU9fxOZR3Qt5twAee7cPsGXIkdisqQiccsSSL9DJAr-C3YsFMjzvjTbRI4MkDuzTv80eVgR1pd-1yRHMRaOSKr6VAa_ocjvjK6DWGgJ4UqlXqCTTPWdRu-ccRZiWNnOlXQpOJaxC745c_Ix3q8ZP3Ae2okujbBWjIzvocs3yVG-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7ZAlrIG81_euG7xltjpKbn8x3pRkBMTNz6E3hX8w9iwbOsmBztUPnpvRdTrHR_inYcG0XwzBes3PvhTnG2bzbrkFML0XzZWslbiBY6peTpAesppnVVP1o3CdQo9Il1zSd1U8GEfCp4MYMLH761qqufMJOXc1cGJ1sTb-yVjvbLdbI0Nde7HEsV46lazRVD4g2VYcoCdsF1ur-FLh8BWn6q4rgoO0rmYUhhHAcMTN3ojq_k-IBAwoqAdiSnMuSrcVjJX2s0X02G8hUEDiPgkeNm4y5DItR5MYjsf3L6PEl7s7k2zBvOlmTvl9dCUz0i7gCfPl5R1uiQK9R3w9MZnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkWG3_Hcawn0kSYkAYeLYHDQhO7OqJrWU2WFeiWiHnAKkuHrI8wJlAl_7VHK34OXE_uXYH-AgC2F1mTPpgvIMDCyr0wythBAX0LNrvqAOtJzC8jZ9PQ3jZvO8V67TVUhOopyeRZe6LIHzJ3_k1LRdkmSFcPNzQtZAdHqORDBJWtsRGnnlFWtbdTZsV6tcubtRUhuV2Xb2gkFvW4A6bbhhkHZiXYj8WF6ONiXIhukr-t0qNVcjY3i6_GwEBcuTqod9_bKb8ylmYLevRyzNG7fVebR_3ngy4JmnsdSbwG2edJH998gWx8KqXxs3coVrHKfpaSVj52aotyoZ2ay76Yl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/casEcia9qCnNsNgAA90YW1ei0-ucLzUszTcatBMLKSOFdEZQwWcqiSFnJjkTKISS6tD8mpMx8vEz7OvPMAYOeipuPjZkrJFd_ICwYm5Q10jbFZh-hKXNvDLzWqK2eFKSiIoEqilYkGJwpXqi1MV9Q2jub87XCEPPdsPayaXWqKgQxYD9R-lk76xGa30RdZnA39rAMTZgboAn471Ceji98Hw2DLGczdF4H5Qhh_dMDPviv1WEPXVftfkbljsVpENs6NjReKPTbm4ZRdbws8WQI-Z9nu7p8z0L3ujG8__3Q9yKxv_xwxQSdd8csKgFXsWrVv7yiTr9Wp4SQoteupUrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWDzSIPlw8nsHiWm-OXxE-Nn_8br3hbDBD0wh9ymFaOePN-jX08GlSzDE1o4Od3zoxh4hh6xvsgbNyxBt7X4UYW70XRz5VuaS-9po9jlVmQ7Ngqj3o6WIfO5ClQkPFSSs206YfWWybxYrbMxC2RdcgDXiJVAZlQg9duOVwppW_NOhDuscTVQZ0C2geLdH4O3eV1Sh-6_K_4VBBjdBxm_EBaAtI5PMXHec7pUo5fudve87c1WTk9YN5X_t4G79EvpuP8WikAMKOP52noCBGCFFGuqGze5gTnYdakWeYmw03GlSV4kqLOSXANLwmCZ1JHrZHXNlGzG7GlRJutASR05Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyDgzQGgWs1cWnzT9oFRJXTbY4vQFGwcFN14mep53fALgDnh7sMbafk7TDcXKRH1KjYPYaZK8KGepugifDbPXoIKG9EGI_a7QKjjIvwSelxPBj_TZNtVaGQaqLYg9JdXt5C3TFQfN1bO3-5vrhXoq6tgFYZj8cdDWo-wusYNwqlddxX4_myIUeHMcE6E1pWSGV3fH7vEzgc9FxUxz7JRrzIJxk_5EtevFXIf3mYQ-ff-5cWZZc97PITIl_Q1Ytf3evtDPbkAdowZveIGYiCR_Ttj9CR5SpWuUlog7fwayEEy4CBybBp87I4FNlxoFobl0O9jRzRvQxRWFyhkXjMoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g09zqaKuHGMo5rj_xXT0gg8CVfX9sfUTrboS1YL_mdX0fXVOnKQ-FRPOH3RDE8oP4YQw3bTLOd1YTnd1bKPaLfRZFCi4YTLwsPQIZIROhtyi94HYP-NoeFmER7YpMZSENX0o2GFpRpLzWQwtzocSHhapJhQtBJ4gu0Ms7Yg4i72f5qairmeVqbFz3t7NSv93tBiBdIFH72vfj0bePYURvRqCiPMZCAI5KCdN3XmrjruNrn54NkDtanWZNjvt98jqu6B9C4-a5_buXO3-63y_dc8D0v9Lq4O59fvuBH3ADKFfr1eJcJgwrqokxUuo0vIyV5ZcT5DPKchZmauL7-VuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upA0yCoYXRz0ze5t3zjYmCJjoO2eWMaX0KkmbrGd2yradFRNZ0bEA_-oEzv7eYbQCLXY75m0ilARmwBY3hAoK5Z5yNS7YRhGAVxVc47TL4QFwd9afVx9qOP2kxA2HC3yyd0oxASRC7C9CGQrtSdp6LEkfWYywl-rOtu6wdX2u6g7L18-uVcbz4RGlvLdINhZE8_4D_uNZgJjFRui6uWoyh_ua-g8d5FsSim-lnxzR4VtLssu3T9cr0eAHa78bGxx7SHXb5VY0hU-UD-csuCSD34iLk3--MpJWC16Fpr-65tzCQVCch_20Ptt5s5HadMk2CRFdcB6v0kNQXJhTHwJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOBZqb56_NluyIPMUcQRiWXrA3trFaOtw_Q6NKEd-hEzXFfVWThxCYKf98Cx_4lTan3Pba0F0QgGDCB3YjNoIYeK9BJrS5spQZxIMhUOajfj1zTtocvN2FbmTg1cUNUhxpM-JPCxZTR702TlPVB-8-LsLw-1k2x_JjsJjc0h4Lh3GuTaw2UIRoiafzrDoYQVo1SJ_xAbOC3BWNRaNRJOlIEdVcbkeReNor2MAvTK6lBOUkugIlBKjbobxNOf8sDiAsdf6SMX_AFAXBmXe3_owxQREl5adjV3ujtGNJEHiW8oahEqhDUgPUaEmYLAxRLmO00u8RswcWiXtTaRpTcQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFU38KABlttMldTwCx0FidJFa9Z-yEn2VAuKIzybLe5Dn0oNYV5e-_t1JLMjtzgT1vxdVLxPDLx8HBoP22F9hXAy__CX_S0a2FY8f-_t_vU_YsyuXYTOOjEkzlz913cMVzg6DEVVpCA6_qUwj-pc1k66t9uRxDeiAfl2A_B66vCigUH_efLJ3bZ6b4xX9zB3RotuaeK8mrNWJAFEY2j_Xn-Q467_JXhdgoEgrjPks2UOljYTiUITbit-_ESdu3E4lLAohM77Cv9soHIugCcUF7TGeLRnjalteZQ8OhgGFu4gMDY9BuNx37nXuEJIV5tO2QLkDZPVFA7VEiL_7qt7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd2DAV5op4FpqQcdXTMpoaC8HVP7gSF-bztFX4sGblRQ2EVeZ06rM2gBGmpQghbk5ScwKv1af65Mxn-wiWXFm_0afGVa8imP2B0OUJvBY_8f1NjkDQYC0OZLpIv4T879SxvkvI9a-cRhCSzE_WUr222sDOEoLeWHfWrot6OogeYzUjPu2IF-c0HklvVhNoLNG_croIwx8Czpu7n8_pq_6g79SXjdEVmYYIafQO0k8RPDFFZqBshT73C374qcFO5VJgft5_1QiUWj2ButNyll2zQ0fZZIiY_LJpwdE5_pbvutZgWSi-K_1bGolRwJY6Xztik1S0V5APqgpl1doBGJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJoO0icqUXwXKdtAGu8bysC4I7R1ANX-nljNipQMipADVTGUw7gzCHsUCEtyFmFkrRzES6HobmdzQ12bJX__MZ3UgOfcqbUHcvbYpXtFihGs54B6rJYpFLadajIzYVJcWd0vszlkz9-1g5yTjkxk4JnZWXE3-Us1qHTGIruOBLjb_7Mirn5XeHaLapIvgQWMs-Upnzy9zIie56tT-q3d8U-H3h_YQiMkxVXLkQ3hVDtyNE1KZrlokjtpqX84wb13PK-iSBb_Vhfm0dEFKtOOIYHET5a06iI9HIYv-5wYR3VpLGyspf9MysY-BY8eybQ2LjQ1ofl0mU4z4OMdt18c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzL9SlMm1jVpua9VZym-9YpUlV0IlJ6-vhA_EPB7EKLWYH7M85eMulEPZLoypGPu1tA3Qc6Lxp1uS4uFgyl14RTQc9IbXL6g19UfVqOcirQeJZG9HqvTuIHmDmYQ-d2Ms6xfqPy9ZvUTH6vy8oLy9QhLSskVZB-hR2S4H5A-OmV40GLYnobsQN9RcEJBvSqY14pjtGuwTe23TNp0Bs4DEwGDlGG-NWqC1-WkKJ26Nqcsk6BivMWQBW4ctNO7kfpQrSrP3iJ3MRQ3jyb0RTe9F8rz1McESZbZgoz3qCevczowYRgG86-Ulrzp3FRlgzSgpjNA0fBLaN9Nk3N1qCfZug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
