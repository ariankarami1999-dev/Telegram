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
<img src="https://cdn4.telesco.pe/file/BfD5Scqb9-lcxgvvsVgL11eeyjZEiEPfFq6aJzYmBaHPtRZw8IkbdBZz9nPD2E6Ai4wgxOO7C6nbPu5uL73MravNhUYyR8-Rw7NyEn7V31dxihfY_Zea8qfiut3M9gMFXua-ZExgkVx1eWolWjAipX3N3r5Lg-t0uqYlm47eGpfPzufKhxa7Gmgsrnlhcyualh2tJWW7zH_i9NOwNQKUs96_Cp9lgSCNmQ2xEQMuT-AgfUewVV2bubCeyiJQDHC4b-5r8ExaCt-pVgFivzopkmcxbs8mH5UckaCYnpnMu_WEr-TOaOX_oQBayCGuK5EgqQPEl9JCRKdfcX61HxXpBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 01:58:36</div>
<hr>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr93pZ93BxNI0WPtUhfrzpKxs3_iegEwlCbmFmx9CJ4yI_KYIQkXb2lXdta6lYEMHh2zIm982g5QCkeTEn9jA6G87W87FOC-vcJFYzwsUWTw3qO17Sq4wt20gxZ5mgugwCyuAVGHIWsTN28N0CXuvOrkTc8-pTQwa9X-2HFfl87Gq58KjENkpxLa5YWROn5jir-ouOTHvxR-IoAJtgZOg7tojpcGdOstmJCRQkW0Qo44uSR0cPcVFS6M1SeMrVEARZOr2OISA7m92FgM1FA6Zdf9pfXa36XsD7I9Jr7Hd6jZP_Pmuv7e-m1boZCpaCEmUT4AZJW_tBvaVJ9YMQLScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGv_j1T_iXNnisShCviaVYqKNW1AgHN5WQbdyKfcYrgTmOipc5TjQVJ6kbcZM_igyH54K9oHiIQwUvhPWCAoYrC2zeAt0F9BorNIm5CNUpw7LD4sQ4P62U62-1GR7-1hX4eKmDEN6RT48TXQp-EQhDXi7l21vDahuToqtp0G63QAPDlDHEtTg7gG99cP5ziJioy6h2unaCdOTJhOlzNViIz-m2roTwIobhGcZyYBHeIk3jf4SpnKH6SoTvM9IthBjJtA_VWu2E_XFeaPSVFb3FtApqBdZvE1cQs9Xnj40jrwAzfL_D1FEjLkpoplH2aXpfC54Hz0gQ8QBomX21VKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23803">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/23803" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PesvnlNFfCpRVsZyVaJjVATP-CvR9dAca3u2qPcPQiV2d4VTcpUpTMIRAZO-FSnDR0RXfd7z9sXL9q9-NXXIzrQ2Oq94DW26VRuOd9vUXnw17iKpcANNHkKlJP7hgsBr_XvEt7GQxV1Y5KpHDTb1plwsof9qWfxkOAhGSYc8ZnOy68EUMiDJZs3IUhC9dVAcZ19_yZLVQ465xmAk3OobusXZ9iajGlImm6BQwXJLqDbm_1y4JR2ZdN9fLhEEWpex2mk1sDX0H1szjue5aq8UP_3MEuXgogFWmu7NpfIW9cO0_fw6J7Amyx-lgs669E4UtRU_BpaHD5bOBGczIO45Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3rwiXBtF6Ek42FtDB1V5kk_o2FgkT4yyBxIM7HLHIVCfGVALzxuX7fRSMn_NnZyawoFksGtu3e3bpbj9arSKjl7eO52aSjzQly2Z9KDrE380nBPjLGQ2g0TYIaQ0a44GK7pTwi4nGTG340V3VQXSvtcihem_vr1EE1RiElAhdecghNqbEx5ZmFsi06K1-p08CV-BWK-L6zNryuMMqT4UhS3V3daqY5-VJ_3Ea9BVtHZOdeGO3KaCb-rHddGLni9ihb8XS6vZeEHgHR482ygzXQeMsjolZIDNxjX8lD5SA6X5u2R06MnlIV3fN5Xqbvr6Msa8ZuDZHRKTJ1JM949rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlcelT-g190CRsxqAS_XLFuyRMORZA8_YCQtw6BMbHxnucZ3xf4VQglX5VZGnM8P-BQUs5EcHaQjp3TMCAN8eUYwIOTfY-_sibf_p1YHaUTi6rhnocn-mXBbDA8fSkvY8HyP1jrGbtLynuFTVhhcAFu8avbevOMCQRdHZpwCSigkQor64PdmK957XcWzTrcQBCJE9t-UbS2IXm2FTZ7veYfIIBHFVKE2tz4erSxMh1qAxSf9PSJxBNN9595Pgid8o50NZEp0dgBBtNntOJMLTeQsS19EL5uYL38DgA_2OuwX0I4cm8a_7BaRQdmIfW3r1NpNGRO_L6ax5Qjt43iYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQi4fzsQjBWSUbQasUl0BADV9lXlqqCC6pVraB4FbmHNF3F1OR7mccT3lFge11UCY_eIOEVPRdpL0AHPM3TRIVWx3gT0jwqodqhj9ojk_u8r0HhF27WvtmkZLZYFVnwf5w_8qIPRQswMgzFZiAEaVQHOGJFM2qHwOBVEkWP3-IVBfshQGIBMoHMfSf-fNLXqWPqN9OQeBrZhSHjOzF4k7DfuITFmDVZBu24TtE-C4BEQswePszg5AxsUFvpvFtCsN0bRIxJRTeK3HlIDcVJ6cFurV86cr8t0gHdPwXPFQgiXtD3Br8BaMrYNCgvQFmn_U9Hh6bA9kargVUdT8G5QJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRvl_94ZC_XerG7pDEN09BUoUiMQcqJGdM1zjhXL2pSUJ7KJMYyJI5MusZaHLX3HFoxBOFKpdrlxysHj-7Ys_3RHSBXcBSgmrsRrYjlFri1SyEgqCnB3fmBfF-a3Kw29GDisMSiGi3r70PAVUPU3VVc66FBGvU5-uuXnFLI53p3yRWjxP5gTpik6lUyasOgEJsafV1Fg2l00L5L_25AOTyM1ZFxiu1dg9W6_T_lqCIrxiWc3TWRso1I6KbTHLTADexBy9bRKwzOzR-yfAqoNG_mEBJ8-lr-s6ovPdcoIgi_8QKNVkqy5-XsBgUl8Y9YZOhW9TPXY7qrRRhXbFVbXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aE1hjhM2jnt2dCxM_Y2kdjquqhNwc4Jq1DNSm6YR2u6yKen87cZkeXyyvxXoR1c5ojNK6HnerkmsfWeNlcS0qCkMNJMjsSThDsDEbMLUaeDwsKk5P7nKDdWRwEdcMgdlXn8HS68A22wkUYo8b6Ee18YOd0Vb3v_3jUPayXfVQDcYBUyOgf9dHqdHVY2Ga7bJgNVwa9okE6vYgiXj5Y9RawDS1e-tNQflb2rmfImOrubMQVUtj8NCSEFTtX2EvoUi1BsG6TEpmCSuM3Mfzi81phBk4LIRzrBqOv1csgDgMe6od2aeQNKe4W1kF0qPds9ywsgovroQi_RuLDrOWF-W3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaW3ygb42RPTmKXrcwg7GS1Qu0mhI-2cVNR-JpscKgjaPKvFYbigVdFA8r_EbDAC7SW-6PAWoDezVV5yfJvyDMtR315AcgKf33TE38uZPCoS_cbqgC7GQkrRgXof9D-Ajp1WSUsNi0mCtvbYigL6WffxZ33PwnUaTOj6sIrhSRzmcD5frnyHCobwBPzlUAQyReU5Oijd428PYzCrkIpSkq6feUOjy3CyWNZwUZ9AhcVMhEqqJdWOdAECYjJJ1CluZfEbEHMfZ-k4XCyHDyD_4ZuXcbaA8lh3TPZmTevW2AypnhwJUjdsnKsWPzFGCj7mB9Ui66faGfTT734mYGJTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsZM8hCPmo-cuCOHvstd-PDqTpb6HYjlPYWiL-Tj8Nea0MtyQ0o0F7x89GP_usovq9klTsdBWgaFIsMEM4vV8ul7SMbULRC3ziLT12tOy8-ROfQ3cs4AOavJ4TrkJr0sMbLEKtidnlTp2e30FY8J91UOe6BvpHAkptufNjEe7fR1S0LPA3BArVM8SG_Oeq-7LwDO59g6Rgnx62rNAhw-sM8EakUNtiuPJGLgP7fEvEKpsavr21C1hh7SViNU1C_1rsWrV94G6gr8cLaIn3hY8wkcw9nccS98ok1Zf1u4uNKThh2WMsdrdqSIq10hTEwaYfH7Aj0WtlwWVe5gOBuwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYm_EAJc9fJ2EUEGiYpYdEon9WpzAnIIKxj3QBscuMRylcu-VU4gUQqsseQtj7Nix0rSuAEzBUgK2D_CXLrIZAe0MWrOkbL6J8E5f3ywPcsKvmVIsmD7IHWEx-2OJqldVFIN1jxWryykafyGXgqqZ98c9ubndVIsD1ARq6BU32JykgmqOSF7snusSpolX2JpylDhwODp-HfAwozAPqvHnJEHCwyiUS7Qhxk0WneyfneAKYaPnYCrWmPa3NfcFXS6mZNfKMk5HrmdU2IRRI5XbdTE5ZIbwmwkZfJBpGu6OZi88A_5f3Sk76GjaupL_qwMUkGY6PYHfzCSaYINiOpwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2XNJRL6Mh4LfT_oS3too-ZZsX-ShqijxuBtdtucUgifnZByPM70g7BdSO4-OlAaC8O9_rTW_dKAGP9Uzdi02ommtQKbyY9AbPilYPdSdWBtnjBnU9IDN5p9XcsKu_reHSPjLjXO_ln5kLgkeB46QTH44Od-QAfUOrfcyiarfjd3HwMsFKZY6m8tGSvrNzb1-ktYOYtd3Ow4UR_tiK6VYJ_uBvDpJRX94MUmqahE34OMCOo7M85fK2D3mpCEDpDymzBTOf6X3CNiIoVYdJ3ZbSqbF0RfaaLQnTKB3f6U_x8kydxddR2Wpm1fxd0N6LBStzGQVjzf6BesNJ1uDxuD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl_VhYZaan1JHisEsSbdy4hKd6dK9oFmlFxhWxEq6BqdgqE6eYfR1AR35-c2cj38Xu6wh6S1ZqxakjNT-A-ZUw3huiRMC8mKl3KacYUdqGuCuADNJSzPNDrq7JsYv9VBMUmhxujU8GxbA3ubivNHUGTemgCSkF-LPVUMutybPEuPir29G--Xsbd2F2dy-7X8ku3GWLTmBGSbkgFzbeJfnlFQDT6PviQPRSkXgx0FkGQQDPkT6QRCbhzfkBOnjF7KW9jRZeDdAsBVW7kCw3SFtn0cQ3xVVr67n2YcIoozGCRIYnGCtr8yhMJzhMLucx5ct676SV9dbk7st0REJ6YLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH9zYfI95X9y-6Rd0EqqmCVmE4jmjcKa0M8TxckwSuejq0HG15L9QhRyJJ_zlZJWDfPevGZwEmGYlaJRzmY1SlHHWCGdT2fMzdYnXlckCgkhfgCbmj-UupH1aWx1lKgO-P39NI56VGJ0dhnN7i1wVQtVVWrT61v0NqvKvO1gHlRjP-Zu4rdn6oByAyKMNsEmUogfirMy3hxpVSLRXafHKSMh3U_IXiDVF3L3mfAm0eu6NkERcD6T9wluPvma61EB_R0e1RbvvRgJneRPkuEyQr3AHW26W3Zs2x1ZzDnFdRAj3JPEKN-F4a2NUWrSpNn--rGopS25rFxDBWRLL_aP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABvpTG4nX94hpg88y4LF4yuX5_G7iOEHFJ3YLSGXgXQWPv33S8peRq9Ja2Y9gQXm7RIBM7Zksoq7NSdgPQbf8mbVKIefBpHArp-SLtgcVKF6B-5_CpReDE-eZAjIhbqatZ4eEzPy6gayPlvd-xmUxJx2qwm9IRsVKS1s_c1YYyXYubVJbzp9Gek76ARORt79vg6nQ1D7Z8jmh5vsa7XbZQWnt4Fv9a3rkMp8prKDaiUdA9goIDcAxD-KEi2tPJnW4rJnpaGlIqnFxR47fHeV-4w-MUzYuw1JtbCcRuDJTwWIF2Wtyau5ld1DOoRf7Zhxbumg_o0Jo3x74cTh50_vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuzcbyZTiTFmIQS9qV_vHs7lIiT3hXiqjVxUHXhbU0N4Q-g8j373tor5vH0acheTN5I0HdvHoODelcyprs0w6i_3Fxyt1_BNcH3rP7Vie2Lib_LIRW6TH4OwiPOHUYAIAKo99V26yshoFUJ2vSEEoAfL9vWgcbw50CxRRwkwFi7y41pv6_AZQWzflhXEWJUC2KllShuIB5d1Rc3tw-hgrAKVAW29jzc3Pu1p6Q3M3J86Si7B3cklioRol1XYucPAJy5I-jz0Lwa7CvVmWMZeQThihHgj7d20IRkcw26fMtpZMB_oPnHf-SAwnLqjWU211uvNLZ2u19h050eGZTcChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSeoEXCOW4DMF_CgfbIVSt7Ihd3ts0LJ2NYdPFnhvHi1mFlFkwV4YCVefYwWVwjcoHsjQQANIM6qJZjxpwsUA2F6mjzwls7w-Vk9aelVuT5gbURHbZN3iRUsGsqnRnel0XZB9WYE7P36bcNkn10xcOhCHAXOyNTqQaVRnnvTaIDvwAVeWMoQJRgFL-d3S1OWbXifZLTlZ-rLT9c68Pz2aVknhPOa_IxItQSXgDfz9gWWsdsnh6sGfrc1o8Nuet_6po-adwyjMM0AqB5grqPlD7tFxl8YTK3MYVXs_FRLI8gXHchF15mXIm0eWELM2z1mrOlAdaQUqI0SRKttEYLFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3TlWDNZD0KvQE9xGJEfb90JtzKZaeVZgp_nsqqL4adLJnWDW7oR5YIblI8vxCsZ9xou3_w4u631MAX5dakO4h4_gXtSnFzthPoLq15BSBTex0-vAynq7wuQ9wyLxHSNYIfGmgO1hIgLcZVowsUBmEHr_RMFvz4dVSFDYFX1AwbgIXxekoYHHo8166GE90KxZ6v1eoWvtfeshR0uQhII1MS3yoUv2EYzyFPnMEFrxFVlm33U8-DalHPK5fpFQArhxuH5MFnFikrkS8pqUC_3jBF2RADxUxUlEt46Lao1jsrkS7U6L0fdtS2N127FIPzP8OIcQFZh4R2sKvzNHAA0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqY2b05oKTJLQbc8daifDEybBcuBgdHbnTy0oDYIPiLKWlV-iip13POtvdwLfPn3gdQDURQpDmZcD548LZAESAWtSE_7iL7_qKXAO-eKzjU5fDepXmxEqLDGAqnW33misfbGvSKzTVUym8omK-yZ0ah9h7f4RINLX8OIifzivC_KA60aYeq_ETlkYhSgr94GLZaF_5JSAnyDQuyfOnia4N2Ci-ZA-03YRL1WGOyswNW6KuAewMIJXwopeLkLkwiJ0Te0Y37ToZohqIHzSsCZ1QHXASYqYgFZb3C7iLm9QqF2PdccFRqnHOfdz17rJkahyR0CfzXhNmg8HMas5wLK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23777" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4nrKQXTQnS3pPwHGyddFG1ZUi4CH_XLCVON7X0P2FZJtTTtNAS9xiFNnFPhP-hxF9nBMffLwi6wQdx4Ehw9KgZDzMdl8HT8TPAjClibCPpR_Nn8WlEczTudwl4uDCnFGLwvvx_MSfWlsVdEG8jRAgR3grSF7fidax6HkzuM4pGVsVTH5c33yehRuC-HFtVWGEby6A85NZRKi_uBJ6ZWjR9VbRgCnMThjZo3mZHIj3q9N7A5BCWrTN8Lg7hLjFKFXw4WIvXbJd-vcaCXuDhAiMxoZaNsFdfWwb3wMmnpLD3kqRgubr5RsiANBOkwRPpP63CLEnKIJTDuEv3BTJ9cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVbvmUk4BuZBUO2lE7wIKJXJ7jw4cE9wZKf0RTs1A-ic2idWufRDDi5BYsGf6lrZ_UYDG4T55MD9c1s-gN7qk5XERNyqbk_8I3kTiYa0TaZGIL7xoci-wfEibFMBXDJLo9dNBEbuJYqqUxYImCSh1eWFsk-7-NKW_f4bdbUthK35-DvMYy2HBwwTg_6of_BSRX9eeUEIvUqCrOq4Vm1rxMX1ZvwaimRtzMLvccpnPTNgneqwqrhIENTPdOa-bbtFhGI0Ar1bqevOL9NxpblUMNscW8HqECSx_33Fi4_HnAGgTJNh46FFZStFUcIl28L_IejY2-KEXFuL82wlfEv-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15l-U_3vSKH-RWfyJTvoCWJkE54EqsJV2YC-gkeDpGVgPqH9-6NZr0IZHw5a0TKtLpwRHQM3ih_DX9HUobbmKx1ZqwfYPWC5cZhfSiwusOJlBPYyO-bzzxULwBoJIPwyd8GAulN55Pku8-ocUOAxAMmClbWQxRHDG1jXW5MocKkRCavfH15utwztWiskhNWipyW-SWXUcgwIMf37RESW1XWTdmCb5OZmQYf8XelNgkv0EYRaAb8loPwlKmDnWtSyqFrvloANREUWqEFuOiFRyKWCR5RPzCXj015IUi1YrG8hhS0ahnJMtWB8xFJUwrr9d0kcVsj2_oD3YmqGh0h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2lpRaC8vVtWlBzA6yVYT9KKzTJP_ttJVjk_l3ofDUuHpScuArnaSANXB9Lj9kArDyi1G5QP97byhIHB0OZIuEa4MPPgw5mLkjbLivVWZnaFZpA6Fiu_j0rtzNtztZ7Xacz0nrc-Jy7_LJpTWPh8PDSGBA1jk2Ek8LeyyAuQDug-bw0oUgOfv42Fu5HKZRF4n5LJ-trO9K4oSWjHQ_dEuWbqBnM3whZ2spivyVxZjHRhAQQpiGp5imIJesrZ8SpFZ3MZq6x8U2sAf8Auqnd74m9LrxulfU0o7GUroEADli02RDxO31YEZTdNrCkstZEttR6if-nxwNG48cst-0PntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHf4Aoy3nZYKkLjz6NiT7FNiUU7xAEf8mUHj3j-Lw0N0jxLEZ2hxNco0nZYeXtgzzSvFlpG6UvSl8Ql7g55hEMDGmSVXfzEJfDm4epeICBjvgzoGDc0BQrBpkVPzEPNU-4Z9_wRgi7TyM4AyhHLY6NoDOWeAJ-cV2GJy8bGsEFJnUKGNCKA3hnWICU0vLENzS5oWqK-zuGPWzfc1b1oQdOlFArJvk1YMHo5j2Fdoc_qxhSaOD107SSAxaGS9yBYulQbvVWvumw9jL5eu4tdmJAOVMxkEA1gVwSg4xAp-aaWoae--tK1layTPCucVrkpu_dvfe6yJAH9F1oqiSVTzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuIYY5Mvmd6O0-fKw_RyiauPd4BiUW8rmtGkZQz_tDtGjts1vr2ZOyw9hiJnJSnfgqrpiAvHYd5Z5d1xWS8kT_taDktvOxkJ_kqaU7hHFuUe6IRCBrZ1X7zKzfytAUaAguyS1pDuIc3NoFL7jZ6-K-GdA0lau3eTju7KV-SNu30gEEw1RvNdX0Eb66hWeukmm2uof-EgNlTfSsEnCEMS2mlRpPddRpYWqkXaD20kfpxFizAZOd8W-zspaq1fhmvkZB5AG8n3PFd5nJSfXyVc94LxuxqAsKXb2n0PiaGxqAIGUhrolbvpIPdzouTvJVTsXL7F_JZn7zft73SfXpHKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o03nm1bKaTDPED9m_B6IlmXg8AngadIBaNV9ot-kx3tWnbXIvjsiUUqXYTJkI5rQFY9u-GPuPCaVourUabo3B9Y9Tqu4WnMUGMhMTCH81NN-KxzXS63HQHzM8poMcFp7Mo2-uN7kbICmL0-cPV13SMktmbp7u8msoBL9S2qW_H5Xk5zZBZ_1EjguOxTn2TmNy70qILFIKm6qa2Z-rx18v7TBLAV7IEvlXlqR8LeoRVE_CxQqJ8qaA-zXrg57LXKqfhk3V5KdFxPEuPgiywjOURF83Eigts22mFfKhqBjMMUA63nsTgXk74QXBHaEO-qZdwxc0HPJ_lSv2edcTME_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUVrrt4Ol7Z3FYenRbwJYYFVS8ceTcOIxAKNxvRt5lUC7A0FBqQz5GHrTpZeC6Dc3WZeqohNvhlzk1AQL8ro2JVywobtMZt3z3SmJyd-NBgiuEE0puglT5KGepg23gFbYZD6lyC4OW0D9GcjAAKSE2N_FFajhwb-pANl2vkgMAvIXNRLzrfgfLaXHi2AumDqjNcXU7COMrtMVIsDMd3C9opVZWKzJrMMw1NhlTLdi4PP1f8-pZI_GcxZzLi7L2AVlm3ITQDhv62kJPrZXy5osKPT5NLFv-q2jGGWM5t9q9AJWZG-99rEhS4RfUtrPcolediSSCKXZhIYa7lTDVlqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPGf_q06iIWe-zRBu4_FlCYFzmhEJFN7XsoaDdRH79VJ_Y3xKz-DWBf2UAocVpf15emp_Prhlv09Wg-ic3GKfdNIhWQ_cF1pn6xtdH2fLwzNkoVOI67oRW-vOZ0sMhe15dbZ_76ifCvIyBevgfdZs6BH9GeLykcaFrD3sH-5fBIhkfg4keXyx1H6WUyMB13TEU0EuLZjIR3Bv81hSgJVTB6BZbN8RQV-m1F5HL2wKDHyDFJgozaDhMlA4wqVQiIhboci-VFXhCGhiBsGh4pUsy1vnhTlX0bhPIxQ3c4UFxPhltPiIROEXTQMP66Q_eOoetuIinezRaD5fRI6ocg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-t8Q4MP19lUSQr7m4T_8oPJpu8SVI0XYENrd8FEwYlyohq34tvpQlm9bKLgcbb3BEdiq5z9nPnYyWHM0kNxu--da6y60qHZATqxYw3aH652c_OdQAzWzfUabjtTnMVJn0Pg9u_MPC38Iw6uU9l4rGY3juY8NVxpX3oukkv2IZG1Dl1rsvWXrsCB70FqoocoXyu0JZ-VrbWTUCxxlSw6gY5AieXwrtXnD-Sblru2tZLufT9_0kZco3miL85rKS6_6uyh6zelCRy32OuRBrBaE3SXMc16WFZjsIK0GTi2FUml_M6EAuSAGQ0LiYX-txdckqwTLC_Rk6dBcCl8UUev1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQTmxZVMnrJSLDDangbY8G9LGoRpBsvS75ph6f_wIEVR-XhdzIDKS-nCs7gfKwSWcncb3WdQwiacTNTSOkX6uSyVb4coeP20WiInB_htpAjAYJvzKmVQ5nhOXKs_M9ERMpxyYZRHX9X5DQm-kCShEFzUzsq8ULfPuDI7d6foN3wLz-X4laKrYBYfcBJJgFvB0PweFuGVwCqDoN9dZH4uHLAD_VDV-_bWyf7ht-vEcCdpRZ16rXzWsxMb0oNqHHtW2Ih2zzVxjk-WjrlDwazJxRGtronKe6W58CDneeOHFGkkOhCQGYNT47luK30VClPmCKcsHSZ4xl4Lh6vdKDpdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkmXc4wEBjYqrf9PAdo8nxcdzTXnoAw96hui7W7EaeIWWX0Y6-bR-yAiJX-o2-6yNVQXr9pXMAY45SYJKK465Ti98DmBlfAKKFNjCh9BUoUd2BAYJGFKNe5KHX_Hj0ZlvJaRkPTxE35CxNJi0FhCKHENnNQ9nAICWmHoeMpfM5M90zG4z4PZXS48MfoqnSaGj5UxzQ2ChHzXdd9kTVgPxgTuYd3RGdk9A_EOUts8I3dSiggp95KkQH0org6395wqeAwHHu7MsHoZkRxJiJBK6m6pmBggNdhrYCXKXcmRIFD-GzoGrxzBOnZysqCfeimifjstpAZXJTXxYfJXmsErzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbDatxMB8qOs2p4cCG4Yh7R1Twf5_bIqB1IwwAIGk2K_ZMr8qT5mXt7PVaRmXYVwqBnM0masUL6buPAnkUD_tIyR8I1ESEqEJaXhcrdNifluYBnflXdbdtX2pCHrxI5LiZe9HfpH-q9d3OcFl2Hv8PuOjrj_7_W9wMWxacAmEZov4HeYYrTw_2TXwWiaDpqwdmE4SedOHHs3IhDEppGJwI2yZXiYqdYW3tEXefuoJTWiK4v6fwJCBZRwaUSafFfT_Hq8YtBZutOXSBnNglIss3W2wvWcMrVI-Nx9fEpJ-wUQBRMNkWu85lR4NF3_e5EtWtNvN4gUW57UHw6P2mwSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgVmE2OFab5rggMsBRT16fRsc-ieJGOrfO836bKQdsYAaaMnIimmySU_fVvIqFKSiZS_GVbXa4OdzmU2_KzipBJVjbStkLPVyaXcK8DJtRG6x3igroTE7Ntmrbu9j5_93Psu3PSvF_Iu1vWm3Cic-lrY861NTfLk6emHd09ZoxjfT5UHkjs_4s2wtcFfKlNB7_ASjHgQdRhVYyAoQiYv1Im0As8wrLXBQmHnFbgwIgxHJ3xaZ_5ChYGicpCbVM4hNoiW7XxhayVGh80dai1CvmFLfIFvcXXE4FXZbZ_ohIz8QIRMY51tYUTeBkHW3uxn2iADFvytaSy9Zf88zt2dDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qauOmjFN9dS5vb52TclvjDuOmYDrYWITPgbPTk9HCmEJYse_HcGbSPhtUBok5Ttr_19DggLB44ixr4YoIacteJSD51Zzp9ZIkTBJMK-G_uPEj8xrI8fqpNgCZz3k1iLIw6ZYjezGXNxYNBwqe5Qe__VafdK4Ce5elZKsAiEH2t9AA6R5PwL2QeF61UMGRTpwaDZBXuofAYMpGw87E4oaO4dUxRiffvddUJnJGnOVD9f6Xjt9ZqkJSJ5IPl1FTk3B_VBiChlGB6k1ix_RpSiavLObMPw2Kf9V1PSXg-yvh4BAmWzfDUXoWfFikpOvprZ-kOd0g4qhoLOM6EbkLlYimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ5VN-HWewHEAsjjtVp6-3ffA3bqHenMILdgZA6HkI-CfaAynEjObm3qGlCUod0YSPiho_wjr2_dTon96GMqL8mTz9tEEChB_bmZ38JjrCs6OkiMdL9Bw_GUCxBolxYQimIU4GZM4TIOtihE1dtQGgaM2KxJ_6wQIs6aj5XKxFn0ogWhvodAkczsobWTpZkv-9PRKNiOBOTzywR_SGL3y4QtgunG5DIR5Zl5m-55jXgrHEatpQFivtr9wcrJgXfUkmKU7sMrRlNFaMkAkMUlDzC8oFO_8emYofgq0QWmiGYIgF0nREns9BqwDMJ4acfJket27zhsUYit54Y2gmOAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzFwNgiPGnROG-A5-GQONUilT7kG56Nc_9-a7mo4oy5A72CVk4CbKrlHG21xowi5bWQzwGjLlI04OzBkJkNQeJBT6tzjdODyM5RNppCDg_X_B8qaSJNG53o0GKFKYBv5dJlX3QntHe1kC4FeNh52kXLmTbIWkdtyNLnH44Z0qDXXzhF8quQdt3Nmo8RsnuvXwJgSnrHoCc-bBdstX345BnG_2qaqYK3490g2y_WYBa6gsMnnXvLnoKAw2tjY470Mpr3rPWdatlA4zwLHeuIgHSZNQ4yCm4A0GlXm2eI-N4pl0SmGVRh_SufNCnmwJs2LhTk7pPziDo4_LubmlTtCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSlRU_GOAS_dQSF1bOFsnkvxAmyaYhkWWmzxNK-OFde3IXwz07L1Li0BURj4gdd6SvYjGA4vbWplU2CaVMkCxz2Zj-idThYbfJ5qdLEOLuKxdaXgjHx6bvWobuxyhSLW-fKPimTUBkyv_lFGTueW_Bm5aSuF-RjRQOK5TxsZf3uv1U3RWkJZjDBIEsnlepFvT3B8Mqv2v7I4YzOqh7_cziJ6BnRHfwEmwDRhMu3qGWEB8wCTxVPE9YjF5bh2luJnxdcZposN4FML0btp7uw2GfkMSMP5dyvXsKxCEILstjnWNRlanDiUP4-6ARF2Ga6JZFafOb9Ysk--UjjC9RD1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNf50UQK9djnm6g6_23JKAvBr0hs7cT0Vq38k4Ao2xzTE0Pu8ByblO-Ew5hRwePgc0je2Bw0HinrRxpmKAmX3_WMEbaHYQjXkTo69kHAgsd0w2xx6kW62X9BsDti4Ur1-9ETWNXUbpO-ic6rYFqhGpNazk8Vc-3NQoSuEonB8OXsMND1Sz21pXaIGsTcGtusePR4SwCnM6y0_Wpv72ZPUOAtV4al8P4l4pFAHMWxjI2Qsv8yXbPjL2YTBzR72L_W2T60s3jXGDrCuKjT8WiMxuttd3C1zkZruqnp6PIAKnpC8Aveq0LyLaC4XJX3S0XdCInHM2vz7pnERVjEH5jfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXwQXZTauFImdurTRxRRRzusASuabi9KVN2E51h7nZM5KWH545cWuLk5t7Nu--9r0DNOJ3GxQWNsfnts5GH5Gd-3ZoT-yBFUdw5YZiDqugItEg7t-hTR4YL2HGTfW6b-b0ZiM_bgrLgKmPN4fWWWv4f8Wte8WKWKBQ4m1HMSe-mg4LxF_FzW5kv-TwwgKTFgy21bIW5Pp6h-yf8vwhof2XVLFKKmBXDG52SHu-bNrdZ--3bWujziqVSd1dxlfij1u-I8hSDe9bCo8SI_7vJGnZngP18OpP7mygJFJllBn2DrUKCBh_6mKlXdm0oj1vWCUGDb-5wlxP_QAifaKM8C_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkEI4Ezd-AD029QMn10F6FfRE5ZA5qRF7AHN12Dckb5wwKFv-yZOPczfpam6vyIr6zqGsksYtd9g81X98tgyAW7NDovGszq9GnEJNyOy-rYz7OA5Nip7hPgkt3Y8DRJL9ozEyDQYrU9K0yFZDs4Nkh9i86GA5GRyK9sHne45cItZEwNPH5ZwjXcAEXu9w-dNOCen6o6XJD2NJ5G2rqyFv5TDh2SMe1BuQIdpEELQf9w1g2ldI15_3EZheWoZRptVjSTFf-zE6XOm9AcPTxeeEtvWWGfrv2ovBaBm7VOsqjsOKsbU9d0wVQo_W7VVY1hK2sNgadXIqQAvoafaMXlFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyLZzXzCa4DRlAoNMQNA3PsQZRhRG-nIBkF3tl-NftmGN1VfT53jKORYsAQJchypTOEzIQaC2mRMpStZhEwI_EnMHWKwtN-MHL4D4Z3-lyLBRiBEPs6ne4bSGJb2_hPAvkJlARcyWcxg7T8ACc5LI8EWCIPROwgoAsmVcR2F58zXz6HkkR4E_TnJVOiEPJRObrj3JyJiDH8GNnqPPzeoBCgU64UioPaTlxkcq8aLV8kilsCFkS2G04M5OXgBEp6RnXZh9z-Zcb1JKyADy7bZAHx01PqiN1pZ7BSX7h7zaYVJ9u03pd6w-68qMCPf5DYebBCvQGj6texJHfNsykZ1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=oVl1_RGGhxEw5yrc5GCckGJyzWX_Ww7ymM8k0FWJKPoWNTTNGf1DM4zSgt0PAkU1iiEn4FvQyCnVdvO4RjFdC0yZJehbKjHDRX-FATOvDV90VeAJlU2h3UXiq6OM-O_6mQp0_8yIMDXiFErZnquylMEnvsEhU5DKzQOHqMm7MT5mHZ2tILac79hCJ-6eejzLU-H22htgn6R9mQGn369EYTSVY6pE6mGoD8aPQ1gPjmsGr_YBrfIA0hemT7UxJQc1O0KGmTid3NsAaUpG-_P_Gn1XK2Fgmw13bgwncFbpOLNPhoImIc7KQeVEJKWEVciV2ODo0Bn1tafT_-y-J1Jetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=oVl1_RGGhxEw5yrc5GCckGJyzWX_Ww7ymM8k0FWJKPoWNTTNGf1DM4zSgt0PAkU1iiEn4FvQyCnVdvO4RjFdC0yZJehbKjHDRX-FATOvDV90VeAJlU2h3UXiq6OM-O_6mQp0_8yIMDXiFErZnquylMEnvsEhU5DKzQOHqMm7MT5mHZ2tILac79hCJ-6eejzLU-H22htgn6R9mQGn369EYTSVY6pE6mGoD8aPQ1gPjmsGr_YBrfIA0hemT7UxJQc1O0KGmTid3NsAaUpG-_P_Gn1XK2Fgmw13bgwncFbpOLNPhoImIc7KQeVEJKWEVciV2ODo0Bn1tafT_-y-J1Jetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4eN9CNrOYZmfPd_jqRqbC-XHpFZ1O0zEgGRoiMA8r2dh57YNmKB1lrOeYQXhZS5CysSBUfrHx8ImrzQ74_YCeBT744oLhfzJ5A1UHTzJNNiaELO6Zi8lMJH-V_N7qqsOonPAG_9vZB5xdIpxa14ROOWEu-f5rfSZsrEroJKzJh7MN8etuPwEFaHhacjHrt6tT6QIHksW0_Ty9gIwsaCYw9iLszaxoLJe3PDdnpdFCZ7cgLj1PeEmKaaz_Kw3QZVHB6XlrqM2kNiYKCmLBx5EM8sgW7Dc1Vin1_nrCHzgd35as3M1m0gdHqYqmBkYlHzfGrXUmCM1yd19Dbb4e3qOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzJlBw4Z27wE8hoTWxvMBdEHU9q-zxAafEUBjjzNjbSdVQKe8k6sIJWIBL5C1QBXDt_cm-rWHIhipF16bCBHgdo_GfQooHIjy-hGxXmSu7KgHduo1aS03WpHETAqUjNayxwJjIGOPRBlnAJCN4A-LPXh-mYb1IPCGBrtU7UBtHZvSfChQIQLymbtkd0mGcjDiGKNiCVr8YLpGi293Wigz3YSqJb0frW2VskFqoDvMoNWM5YGZmI4NTss3OAtvXyh_QBrGPP14_SBPajz3Qf216CVXRAirvBnC5KorKJmAxrpL4oIG_iily5wljoXpZXqKCn0atCOpTdrkioRNCZiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyNQm5gkYV2ozeNgoeMR2xUb0hLMzyPXKSqWSzNTOt7n9DDR6H1F96htd4k0OpXqX9qAgAFqojfEnS4iejBDXUTtV4FD5HDpjniDXtd8hVs0EzaftVELm_5LKeSg_EZ04jV-2Rizp_xTgKQ0U96DZN7IMvMMzygw1oZo5HTJ5nx3b4RqMC2Dt_U1eUhghb0oO_re78f1N4543vk5fcRBtGrvS-NZKZs4yTACgCTfKIiynxd40xleNQa4fsTkJjJzUoQtb3EbkUba_69OSb4NRwcP25BjTmLle82A3-v0WvSQoDfRGc9AytMi4btJPPaz3Moh6SGT6ygLvKfppLJfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=mfO8GW8wVI_bQlP7DxQlmiVoJCHoJz1__AyszYP0FKPfiJK4BH7Z2aZD-8kFcN-8sWpKkz8iXQxBooGJ_HybKgxLuSdIYAnPH412SAXHlg39rTZbl02XJvpzlTypJKeT1Cr1Jpgi1-y4oWMn3-MvfWVzR-f0ALzsFhsWoehEUby9SfsFF97NRlCsc6W09ykwJaH2EOJImiqbZTXs0ViOAKkAEnwQKZAMGnCgD0nu05JaaeseeEWGeBTtsaHLxBrVuaaFvjbIqXnXEv34wsx-tcWAJkgCdcUZHa1y7xnQD9o94NBilZE3va3WHjfMWB6pdb1NsnAOO0tJMTg3ac5ncA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=mfO8GW8wVI_bQlP7DxQlmiVoJCHoJz1__AyszYP0FKPfiJK4BH7Z2aZD-8kFcN-8sWpKkz8iXQxBooGJ_HybKgxLuSdIYAnPH412SAXHlg39rTZbl02XJvpzlTypJKeT1Cr1Jpgi1-y4oWMn3-MvfWVzR-f0ALzsFhsWoehEUby9SfsFF97NRlCsc6W09ykwJaH2EOJImiqbZTXs0ViOAKkAEnwQKZAMGnCgD0nu05JaaeseeEWGeBTtsaHLxBrVuaaFvjbIqXnXEv34wsx-tcWAJkgCdcUZHa1y7xnQD9o94NBilZE3va3WHjfMWB6pdb1NsnAOO0tJMTg3ac5ncA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6MzjAKDR6_ZXkfwXJ9AAxkr3blklqwNT5aR1qLX61shiLuqAR5ixkMP3RwOUX80t4c4YHvQR4RjwxKq2dvFK4FYEl-SCtBWPK2aIdWVfyj20oacBDQ_G98faK1dybOCPe6-e9nkKt0QI_Xl_xc41hG8HyjWJtVVJWqjDsbATUDvWjjqBloa7zwOD9Mj_4HsgAkjIB99eSrrncFxTzNm4iY8-RovWoiOUhf1pgJgLOXoJKzJK6wRDd7s2Q9-aCznbTDuv51JLYCOVsNImyOiK9cUKYTF4EkziM4AKhxZD8QqUpY3Gkt-UNW4JzWMIDqoz_sw1yxfJ4Hq7WEsecYdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gobxdfNodYnoSYSoCjBOoJ5F3DX5uuPaXLZvLYVkYaIHrjEipqbLlk3XwnZ-VUa2hCNU523X99UE58LA_BXsc0F-5Z47jBNTFZc8qKoJMxH3iTKyQO89Pp5rFF4mKNbxx6XD6QFEdP_N6CbVPHzZld24B8Cm-9D6Vu_hydrF7UxqVh1XKy0TuB6p7MQVRVSqkG8fJM3TnyhgbjZblB69u3_NhtFxoSeePl64UN7Rv9ZIjN2FHoxNQYumSd8LX2JUBLOOLmqbkbhXAqOuVnXrhEwCkIj9_EHo1MCHzPS4MtJKxwbklZNB8JZ_u_qMiaWN-Px35fkXnhlnAJ9tuLV8Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23739" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmNnECtljgIED_ts7IUDtT4Ln8QcPeIikysCQ_ycB4dRLH-PZzw0N2mAbjN-xY6nfh1ulP3g6XSabR8ZLYvXOIlUGiM9nSv0o-3MYC7zlFS8y4SAZQcvuhuaEvISCLQqqMBSeoVfvUPXRPbTL-UN2skHyXhPSAx_vMNy2dyU6qj7WgUTn66CfuHxxkc7G4z8I7J9d3i0vP08ImUSK1Oj8onFUJWSIaKG7vnwmwz29kSgh_rYbc4_VG6vrvvnHFJcli2p9XGS1_924YkAZp2FtZgydln-jX4I0ntp_53V5mL0jHbqf0JcxisB4sD4AZB9MHHuKPSNS-O6HXOsJf9cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Z38VjVjf0QArM3EhGhkfXWM9Y38CqbYmSaADj2eH2tKkxK0yUOsqpd9yUHasnYPEd0WwNn2fGCjdYlM6M8GHn87-Nxm_tIOAM59UkUEv4ZLAILJyqERrUQ2dpC1bWxbVzogywD5mlaDkBFlSn-PI0Oaw9pliivobtndRnZrj7tVV3nrN5zA-1RcNDr43d3xtysSLaguQt-LwiFOKC0xYKJE53iYvHoxrvw5FXQHbOqJtI4mMCvh_CEkLGMUMgJEkMpWDfCeCjg6FAKpILAzY_zCbkhMfzXl1rTIoeB92NWOu1yyjmAJUhdfcnLuJTt1g0vOOrK_D9bnJXUfczhgEAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=Z38VjVjf0QArM3EhGhkfXWM9Y38CqbYmSaADj2eH2tKkxK0yUOsqpd9yUHasnYPEd0WwNn2fGCjdYlM6M8GHn87-Nxm_tIOAM59UkUEv4ZLAILJyqERrUQ2dpC1bWxbVzogywD5mlaDkBFlSn-PI0Oaw9pliivobtndRnZrj7tVV3nrN5zA-1RcNDr43d3xtysSLaguQt-LwiFOKC0xYKJE53iYvHoxrvw5FXQHbOqJtI4mMCvh_CEkLGMUMgJEkMpWDfCeCjg6FAKpILAzY_zCbkhMfzXl1rTIoeB92NWOu1yyjmAJUhdfcnLuJTt1g0vOOrK_D9bnJXUfczhgEAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=UgicZH8TzscyD_ru3_355pjEm61cEhqEctIk1G_2VTm1FfV4FGQANuvfqOCLqh-n5HNI5d2nU-OIRIbLi9kQDaOMbhjI9aK9yxbnGYyrGOKiz8iONbrw8MWXsLvfxqODarBttYFoW_0t17PRHwbh9BO2MUFYl__Fc6FP0l01zlX7hGC6Ug6E58FglfLg7GPRSe99VZymw6Gbpy2umI0tfOz59nBcNELLlhG2InfAJqXiBbWMwrvtwg123pLC5edX2WVBBfAMfodYU2EoiO7nVUQ7NgJRhbPeKzmyFlX_s_T58qluLYZWWmxU_SmcPWH-rpZrfnz5LxEMXvXXjGewhwKJTwknmU0m_S-aebG8tgcYTS9xaWj97AFpsbwYxSKYDoMp6g0Yl01hcnkMEd5PCNYFavxGfK4o75UmwWCMJNnChL9BwjaS4DsYqh0HdTK1vcaWekZI4LV6iSjRf2oWykx7-ZTD0WyUcmJjqOs369BNBNoDT0qyQLCAL01adythSGnBexYeGvvGZAIJ6xSJnDCIOWwAAjci56_9ch1vukwXDQFECFh_Qj4Z_w65nNeLHpudUOeS4vAxlZIVccC15L6Mpxl-D2D0ekVkUr1O1ahky84ZHwxscPKkS_9exUiY0ptTIEj4psNRIO5U5vPNtNV8usEEhQzL-We4LZwEPNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=UgicZH8TzscyD_ru3_355pjEm61cEhqEctIk1G_2VTm1FfV4FGQANuvfqOCLqh-n5HNI5d2nU-OIRIbLi9kQDaOMbhjI9aK9yxbnGYyrGOKiz8iONbrw8MWXsLvfxqODarBttYFoW_0t17PRHwbh9BO2MUFYl__Fc6FP0l01zlX7hGC6Ug6E58FglfLg7GPRSe99VZymw6Gbpy2umI0tfOz59nBcNELLlhG2InfAJqXiBbWMwrvtwg123pLC5edX2WVBBfAMfodYU2EoiO7nVUQ7NgJRhbPeKzmyFlX_s_T58qluLYZWWmxU_SmcPWH-rpZrfnz5LxEMXvXXjGewhwKJTwknmU0m_S-aebG8tgcYTS9xaWj97AFpsbwYxSKYDoMp6g0Yl01hcnkMEd5PCNYFavxGfK4o75UmwWCMJNnChL9BwjaS4DsYqh0HdTK1vcaWekZI4LV6iSjRf2oWykx7-ZTD0WyUcmJjqOs369BNBNoDT0qyQLCAL01adythSGnBexYeGvvGZAIJ6xSJnDCIOWwAAjci56_9ch1vukwXDQFECFh_Qj4Z_w65nNeLHpudUOeS4vAxlZIVccC15L6Mpxl-D2D0ekVkUr1O1ahky84ZHwxscPKkS_9exUiY0ptTIEj4psNRIO5U5vPNtNV8usEEhQzL-We4LZwEPNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHf2h9NzYPMz4akFF11WT5gNXLWcTkLDI2x15I_d3q75MhGAaerpaAz6-fhfrt6ITQOVJrV_aCsdtN9OlXoKnTRFO120P9cqx-O4R_dl-nd7NMtc_jsVYmxsuDiKYq7CkksO3C009Hr2ytrOt9VtS3SVT3p9hxkLbQAezBuYJKpyOUUskW4dV3CQQ4z5FToUiupkPBz6244UaWBwyIcswYDiHjzWLoZmf0TOeR2588-C7G4Nr-GHArPoNp4wq1PpkoGMsANU0VtKKV3irreffCJaZFLkaGDD0mIWFyGoQHacxHVEHObOkx5a9XYii9R-b1r15vRdA8gLhJEyVddesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr_VzgaY_bAxpTjKH6f4ZISyinGLJHFqM918B7pnTwzJeZ6nfdnpiSL-UsBjV-lCysUyx9X9a1we-rIgSiuCaCEOWga73c4i0sGzkKB3TvSxdoQZaBPvCZuWwGugeNx47WYOj4ZUAh07gT5lX3gABSSaQ2H8LY9frBd2VZWqFi8UhBVbmtORiTjcJNMoV5_sM5uVP_8LdLw4nWX6Uo9ph4acmqEaegDFP5MFPTBHoPi4Vq_1xr6w0r6OCCMVLw6CMOT5qWZcIIJDC8wdycY_y2oARJYnlVUcekIi1VEYn_gB1DFfxE3NXrvpRrFdpGJKPlRjLWee_gBInbh2BCfV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MirvARDPETdRusJoUd8327_SvWPxDuyIC4_j_HjkgMSwd6n-s2knUORokaK5Kyz_cJo6PoNMmDIdoU_8-CWZ-Rn4g9lFlEVAfGujEpyoaBXHHNqo7Scm3yezJ0CSvzcvjY9o92OD6SzG5iZSfTe1yKxi9TxcRhM4zUzod4nkmMHFGB3EK2WFdkM0sPeKBwz3CvBP8K744YAACP2T4WQYbV7qgReLVG7ffMd7eHm8AJix8tQulh-ECyLTL1AP_UpxZAHPl5_CvHbpLnVXvbZAyVff9Myf7SwInM3EWfceI7xrCv6vddHzu-xZ4W2WsQvLtZGgMnIe1SUhrDhmozAdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoifSmAhN3hF8vHrgI75I8iQb0mUBH5MoAkDM2cknOq_7WCpe15NbVmhrSilZkgros4XImhJ76cXpk0t7UmUN7ziHAd7bOCxoTtq3lgGBtikPTVaMl-1OGAfdocuozdgn5Fs9y-5LQfjZVQ8wuiSpvz-quU58f6cK1aZkXBThwQow2XYyFwuYJ8Dll2kExcIegaiEmA5-L1BZYWy3-XfOOPXUbkGbRXC9zbsPYvMHFfQps-kh1Xf52TO4wZ0fzkOGEdH7rL1TTdIS7jol6crui5qgV9qnWgn5gzP_BkFl4npesfTHrIRyUxYl_3W1Z7ne0PM-hWjyRBosix4mspj_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW76ia9_ZLBMrsrhE9QdWhU-DE8JlCdmgVp3g4pVZqgK67fvciiJ6JNUhkE1KnPtwwDA6MDtIk1mHsdRwMXD-e2-4cNvmp2W5ubdzQWtyHHs5mU3X1jV34gKWL7CesKF-14QuFruqmhEFvftKdVIJdCkEYqiMdXymsWBsZCT-Q5OBJG3jCWDuK1nEGi2Oz0iTEty9UEsaqqkTQjY4b7xhJeVudvVaufvoEz4kjfD_S7J3yHM_H-ZLmhPlFFa4NmHJXnL4iySBCzEH80OXIdCmEjRP1yZFoZsDXesWFOeIZYR-9Iw0TNCY9Q3xpDaRyRCJSBLpKfQifDoOTsYLCuMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihb-AnW_Gy2x_6PXrHXDsk7NzDlOBesr_U7TxLIK6Lcz27EuQZVBkKVdabCrBabRS9Set_AT-tXtFEMy7G7gFWvdQHRdJn3z0qoLzxjO_ME4bZvCCcqd2vg43A5eSUV5QzPjO60S-fd4ReHVckilCF2EQnGplxXCd_x6mfBWAZOi_q5cB8nsiPflr4kwnuREocT7pf3FZj9i1Y4WxJM4LR9O3auAQBCvo_xITjBYquUa3tXZ1cT9vWQuYSDe0adXQcea6ZsU1MbuONmCN5ew3yVxcx9uHpIP7P5pWJMSCbC5sLF9GLooL3BYEjTqUoa2BV7aK21Vd0a83GSX9DrvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5jtNxYBKqYF4i6M2qgvaCHjxKXz_pNQ_pSN8V14rRWvA6G6h2a7qfzvLOjVZRHf6vYK8bh5aLTWXuKBBDLrMXqpTP7vC9G8hdEXLZrE1EznbEmtNt61lBx4KDFUHzGeK4lyBlst40iXMctSFfGNitUU05ohTWvGI9U9BNe8pfx1IT7tA-770xMj8r_ZKi1K12K9Tfz5TpHZmwYyjybCaX1WAMCgOswO4Idypwh3xIlzGRYhrrnHIKq45mWLnrK145KdrbwObmJbjXhG6EHIqbJxnzLdkD7SXBH1_8Fr49pDCj6cAPxCeKCLSaw-VV3817rS3GJPTcgApk83iOaiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUDoLn9mR-v48xEzoorBHGp9ipNJchTsrY_R4nidX2R7hE2Br1cb5g-C52lXKjAn-QXT8HpKpA1uA3tMEz39eLE620ltKEB2sNpq8M0fC1-GOhGwZqn3hn6HTTd1WpntLJt1qhCKtyAuBmarWMIF0Q8zk3uVJUsQ8btG8TiG7TYLtH18trEfr-fsZDv95Xouc3XAXqIa8lMASaOuc4XhHu5K41ObO2EhAw9zg9g6eNjM8OHqRpmkCJ7Jo01oySQP5iGk0judsDcU7zZRKkQzdbJ_o5pkGWxI5SyBCAmtUTniqkAVMCy29-JdUoBMKgB_HzMVS5BLmHIsYwU42-fK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=t4kNAXoqHfbFQ7i4fWTPeX0kP8-yrGEyr1odX2bX-YWsdBh8gb4wEHYuNgjuaMu69i0sbEsNtRZpPJfEzUBqqUzfacL4uUUZxlkthtuJS-GIixlels-Smnec9NWRothtfbyFrzgYvb2_Ato5SrtNAwd1bKreMDo_sqkV9EuhubigzpM0isdXoRoHwrf6DQO5bLHVoMfrIRerFYkmw3EJW5QB--PXA7rY8DWaw07VIa6TN0vGocjg0gZ4HS1QkH-w7hTGA2qZdXdf-Az8Ua6WHP38EspO1vDgjQlT13gT6fuqiEXe86UjB0b3L80P4X_G4nE4YlFRTY1IZGiNiqv7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=t4kNAXoqHfbFQ7i4fWTPeX0kP8-yrGEyr1odX2bX-YWsdBh8gb4wEHYuNgjuaMu69i0sbEsNtRZpPJfEzUBqqUzfacL4uUUZxlkthtuJS-GIixlels-Smnec9NWRothtfbyFrzgYvb2_Ato5SrtNAwd1bKreMDo_sqkV9EuhubigzpM0isdXoRoHwrf6DQO5bLHVoMfrIRerFYkmw3EJW5QB--PXA7rY8DWaw07VIa6TN0vGocjg0gZ4HS1QkH-w7hTGA2qZdXdf-Az8Ua6WHP38EspO1vDgjQlT13gT6fuqiEXe86UjB0b3L80P4X_G4nE4YlFRTY1IZGiNiqv7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=BwcVUK8fEvjPfpYpreTavQCT3rCyZBVbQ1vZDuwRwahVyEa5Rw0khzaif43y7UcyyyTnV27-tsI0Y5kS65FoZQjN6iR1r9J-VWfrgNE6EKwh94tuTW38V09CW8Yzz5AwCQSg7yjLLEqEpuV7O7THfsuKQr7T-gga2WnEMRUY7_KtlTQvqcwMcdVM2L9cmntkmK5foKpZE1kPi0w8SKMDGiM65ZNrW8HJZ0L6nTG0KFnL1zKpImVD0QAKbr_THMg0j-APVeNHmfDkK-aUTF2OcgqzyuQ1nVBcGHLWThsBEPrbKGn3CBWh2PUiMtcXHt4PL4311NiRfMkpx80ZYW-Gsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=BwcVUK8fEvjPfpYpreTavQCT3rCyZBVbQ1vZDuwRwahVyEa5Rw0khzaif43y7UcyyyTnV27-tsI0Y5kS65FoZQjN6iR1r9J-VWfrgNE6EKwh94tuTW38V09CW8Yzz5AwCQSg7yjLLEqEpuV7O7THfsuKQr7T-gga2WnEMRUY7_KtlTQvqcwMcdVM2L9cmntkmK5foKpZE1kPi0w8SKMDGiM65ZNrW8HJZ0L6nTG0KFnL1zKpImVD0QAKbr_THMg0j-APVeNHmfDkK-aUTF2OcgqzyuQ1nVBcGHLWThsBEPrbKGn3CBWh2PUiMtcXHt4PL4311NiRfMkpx80ZYW-Gsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdXNMIYUvtNfDel4r_Q4fhHPl3Viw79aY2iR8CpuGuWeEPTnmLwwtpJ3GQZU89_0o3lCj1UPXncfrr2Ot8N6lAfJqw6pFXOIG9DndyQX39LzS79m3huvg3tGN8gDFDWGbwHPYMnsV6Si5aR4F6Nv0JUGZbEp-KbBJhAv0uq-nu4iNx1AAkcIKcmOVsD6UHVEYl7gl5988sfKV2FSnoqhbx3GpNWKk6tkO75orRqEe5CDRsKvhG-wLCpBz6ql_Uo-SzrVMXbG-8k2yramrECKsj7WTrrtrCnAkL7uTmgUhV0iO-FJi6e4_PjrXxi8VE3ylAPaKGwABgbYj3WXhPO3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=OOFwfyRbn52aYMuUv9VTkUI5PtfkwUy2_9gPMsh4zqM1Vk_BGvf2CJKuZfW0YQzqh2kWsT017YZX9UAZI9QVJOaN1QmLFA6JOdWiLwWCQAYCpgoeOs1AHjvBLukQlXT3c-SwTmkqF5yFQ5wPyRTB16rTIY3l7ZitOaNc4aORysTf8yYGxbEDRlZXNSeygHoTscmYT8-vPrz3hJVVp-Lpg8-dyP4yOTBLyymYaZXSlcVwGAQ1j6D8U31bG_xtQrVag1FndLSfQ4AFLvMR_-_90-n3Q3-MeiuJ9H6O6vvs-cV2Gt8mNbxN9N_2oaFjGN6RYsj0QkD36f5yUjxop8L-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=OOFwfyRbn52aYMuUv9VTkUI5PtfkwUy2_9gPMsh4zqM1Vk_BGvf2CJKuZfW0YQzqh2kWsT017YZX9UAZI9QVJOaN1QmLFA6JOdWiLwWCQAYCpgoeOs1AHjvBLukQlXT3c-SwTmkqF5yFQ5wPyRTB16rTIY3l7ZitOaNc4aORysTf8yYGxbEDRlZXNSeygHoTscmYT8-vPrz3hJVVp-Lpg8-dyP4yOTBLyymYaZXSlcVwGAQ1j6D8U31bG_xtQrVag1FndLSfQ4AFLvMR_-_90-n3Q3-MeiuJ9H6O6vvs-cV2Gt8mNbxN9N_2oaFjGN6RYsj0QkD36f5yUjxop8L-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOPscfWnT2mJ4zLsqd3enHD7C6gN3H5iYFdWvpU9cMkwm5AMTqsvZoq3kmoPyRsKLRADzYrhn4U1Bl5-SSpkXbZylVypPoLNCmIx7LRN7w4Jd0VpfeZ1umfjE8EIxkE-YugoXf3Ln0X7nbSAa1nSaKYlwbTNi7zALzsWDD8u25T9io6xaczbTFwIOTekLujg24rj2TTq9ehmRp066VsT8dIHrLc2pTTqLKmxgyy-IhIk5jFNQkvKNwgyihOaf5bVnbq-xpNXVVt40nXmzz-bHI5wCUqsN-XyFOCkSqqfNMmmQzhIL3mJ124st71K-RzoRCVYKgrNDShSzijliZYtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbmyDIEER35MR7NCzuBEmaZoVVUTvrxylGWd5iCbq1Xpj38qLAlsJ_cuVjubBss6-9uE8Kvpz4eSmWvviRHMjT5HEBWePHKy0WvrX29t673RszxcV1EFCdcqB5rFBn6wDzVfSUS2yPHVPahQ-FKuM3Qs5pL4ovHWijQeOl6PYlGcYQ9YQXRRuyNOnWmwz-A69bkGfQKrHN5VsyBf_1adLgYcCdmIzuIKb1pkuWidEZjj2TtJAO-_PFpMQ7zxgfP-I8ITtjOJPKS5AmFB_75j2eiaInKlUV7UwDH78IAcDpPfDN8eTViGs0BcAQvVneMCAh77R5U0OLMkMDWVdN0rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE7mGrWDVqlpZenDRokIvG44R4vFq69YiTR_P4f5HdtW2OBSTCt8pRqQfCr39at03OCp03v-YXl9znpwb1abHTq_mIKvGAeD-ADmetNRNbKEatTlWam5ikdc75Lvx2ZL9suTJpbejhT1ZSkJv8Q2q-0uVpTTwzA8azJ9ZsGTcUK0OL29j3Rm_88LIs3MpFCFhKCI_Sf1t56iOK6ZTS0EFllMEdbwixRAMtvwoY98gjnQ-CzNcUIur-9hKSbzNOTPCNQkAGx003vN3AxFk1jyb3SJLH_dheX7zF9qQHTkUSB8GpPq_BxOxOc86BKVJRd-TT02pzJvB7u1ENXi02trNAv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE7mGrWDVqlpZenDRokIvG44R4vFq69YiTR_P4f5HdtW2OBSTCt8pRqQfCr39at03OCp03v-YXl9znpwb1abHTq_mIKvGAeD-ADmetNRNbKEatTlWam5ikdc75Lvx2ZL9suTJpbejhT1ZSkJv8Q2q-0uVpTTwzA8azJ9ZsGTcUK0OL29j3Rm_88LIs3MpFCFhKCI_Sf1t56iOK6ZTS0EFllMEdbwixRAMtvwoY98gjnQ-CzNcUIur-9hKSbzNOTPCNQkAGx003vN3AxFk1jyb3SJLH_dheX7zF9qQHTkUSB8GpPq_BxOxOc86BKVJRd-TT02pzJvB7u1ENXi02trNAv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAGlqX4uTmh2_X9J4gFPQ_3qCrOnyHy-iBhaj1abKapoSrr0H9lBbN5nfDVCY9OWUhz8-i8-cwy6xkQfNUT4kDAs_0oVZod1BrNZ91CQaRNe8OgRrpr3h4vVxywInrLTairL2k5Vn1zLbvG2qtZSKmaQz93LELDtD43E_kyQ2nFjyRPqNirFT0Ci5y7nqBxKfU3jUgo3YgD2PS69g5Aq6RUc-QI4UpdINO0Z5PblCcR68qLIBYzJNUWUTTEyyFenJNuiroHYh8ZSyFBoy3JN4YQcMu0MrluJi5PvL7bCE9EsUhwGzfZd6d1P3KW0JypEYlWSkh45I4uLYGigwbtw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W6SDfsGsH8kWc0k5OE67UbziailggQfD-xJuEPSwhrdYn1MyqUl9GHycW_Ha0afV9zfmMsIosNfMVlUC7nbrlzC5tzpNpdZXmaseLbpInZ29QKHURIlqX4GVD_cTvynKPgMplMyoYkrk_oQ-22yuyaIm0bnPL4kSlDUAeG8CAT7C6OQF_EirOeblukGNrZzACXWy-5dJJYIARcLItC62VM0uV3sOOrHesnVUSd9YutZMiMgWt07I9ASGGDyuTEq8Vo_1tzM4h3w_IfTU1nJ8qCBZ9S-s4U09aF1prTnhtY8KPRYfPXGhEhgxf7WnSkbs_yud7w55-zX_mz27cNcd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fyV76OpQtEK5KUxZgrp7_PJovv_ZWRzUrLJa4aysyBkMjHkAfBrmEVkzZnTuVA6WRJ_rvvAQ0x5DnJOj4t_l87EQ1xlcueEA6P9Ql0HYFKGBKdHu0ldkgLXP_FsMboa6_ansQqCNlw7MXjINtMfvwmbTYRqVfcCDLzlUcREvho5FOsGvRogwx0RsQCEpAmIR2Ubh_-G6Hcs0QY-n2jobl3STdHeleQgF9281w-8OQinzSYQ4OPMlAljI2gQl6ZKuUfyQlAz-FFxSB1AY8mMmlQKwLKWIi4gK_RH64Vem15T_amCMSszam8irw8zFCaZpH3PoKk7uKft0vzw8m2dMLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7ZAlrIG81_euG7xltjpKbn8x3pRkBMTNz6E3hX8w9iwbOsmBztUPnpvRdTrHR_inYcG0XwzBes3PvhTnG2bzbrkFML0XzZWslbiBY6peTpAesppnVVP1o3CdQo9Il1zSd1U8GEfCp4MYMLH761qqufMJOXc1cGJ1sTb-yVjvbLdbI0Nde7HEsV46lazRVD4g2VYcoCdsF1ur-FLh8BWn6q4rgoO0rmYUhhHAcMTN3ojq_k-IBAwoqAdiSnMuSrcVjJX2s0X02G8hUEDiPgkeNm4y5DItR5MYjsf3L6PEl7s7k2zBvOlmTvl9dCUz0i7gCfPl5R1uiQK9R3w9MZnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llzlDkWIDZmiSNiQxoQvSduiU-e8iKY5znhgAtDJ826asEticAbMZIKvghHuyjhtqGyW7ARGl-A2XVKwvr22lQZ2GaCo673XHX6b0_SeNVn81zctmWp-u4En_jATuGZZI5kC4Pm5hAhfK4qIbNqYHL2Lfgz8EyZzuXBUKGs8N_MyIzSdJoZNwdodWfn6S0NSeY8Id9xa5DAUaaKSdut8BJG78epRG4X9jO9ujbORvUQcFy_hdyGV_eRD7HwCj0NoIrsSHS2MFklk1HQvLRT4Y16o-IGVzWcr4X2Px3UAW9z_LFhZaHPbZU-AQWmgSbHvVa4VrmMDMW56Tj4Hd7ajdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/casEcia9qCnNsNgAA90YW1ei0-ucLzUszTcatBMLKSOFdEZQwWcqiSFnJjkTKISS6tD8mpMx8vEz7OvPMAYOeipuPjZkrJFd_ICwYm5Q10jbFZh-hKXNvDLzWqK2eFKSiIoEqilYkGJwpXqi1MV9Q2jub87XCEPPdsPayaXWqKgQxYD9R-lk76xGa30RdZnA39rAMTZgboAn471Ceji98Hw2DLGczdF4H5Qhh_dMDPviv1WEPXVftfkbljsVpENs6NjReKPTbm4ZRdbws8WQI-Z9nu7p8z0L3ujG8__3Q9yKxv_xwxQSdd8csKgFXsWrVv7yiTr9Wp4SQoteupUrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWDzSIPlw8nsHiWm-OXxE-Nn_8br3hbDBD0wh9ymFaOePN-jX08GlSzDE1o4Od3zoxh4hh6xvsgbNyxBt7X4UYW70XRz5VuaS-9po9jlVmQ7Ngqj3o6WIfO5ClQkPFSSs206YfWWybxYrbMxC2RdcgDXiJVAZlQg9duOVwppW_NOhDuscTVQZ0C2geLdH4O3eV1Sh-6_K_4VBBjdBxm_EBaAtI5PMXHec7pUo5fudve87c1WTk9YN5X_t4G79EvpuP8WikAMKOP52noCBGCFFGuqGze5gTnYdakWeYmw03GlSV4kqLOSXANLwmCZ1JHrZHXNlGzG7GlRJutASR05Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE9Z8oIMnbi3DxlPeeu4izN8pgXw9syiCwJpMVURwDMYd_q9vwUly-Ro2A198G5yJOkCVeMgndz3LJ4EBCvvKNWZGkxUlGgPhOC7eCRedAnfvsuzfuh1we1aLHs_b6HjhwWIX8bmIFuaKfHi5qf4209Mjtea95K3eCWShdfDn5k7b4HoihbeiSkbY-D_IZgFDbWBrCCMdVoFDpwwGfJxF8NsGY8KBNrMBjzDQL_h-YAC0zfi4OK-Kk-pjNVoTpOPkMezOlZjGw6MGSTtUokUw5YZZSDkxqt3iBtyXZEbaNIgQnAgetdmgyC4no7EB5hF8ss9d5Ha5PK78XyJMk9Dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g09zqaKuHGMo5rj_xXT0gg8CVfX9sfUTrboS1YL_mdX0fXVOnKQ-FRPOH3RDE8oP4YQw3bTLOd1YTnd1bKPaLfRZFCi4YTLwsPQIZIROhtyi94HYP-NoeFmER7YpMZSENX0o2GFpRpLzWQwtzocSHhapJhQtBJ4gu0Ms7Yg4i72f5qairmeVqbFz3t7NSv93tBiBdIFH72vfj0bePYURvRqCiPMZCAI5KCdN3XmrjruNrn54NkDtanWZNjvt98jqu6B9C4-a5_buXO3-63y_dc8D0v9Lq4O59fvuBH3ADKFfr1eJcJgwrqokxUuo0vIyV5ZcT5DPKchZmauL7-VuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upA0yCoYXRz0ze5t3zjYmCJjoO2eWMaX0KkmbrGd2yradFRNZ0bEA_-oEzv7eYbQCLXY75m0ilARmwBY3hAoK5Z5yNS7YRhGAVxVc47TL4QFwd9afVx9qOP2kxA2HC3yyd0oxASRC7C9CGQrtSdp6LEkfWYywl-rOtu6wdX2u6g7L18-uVcbz4RGlvLdINhZE8_4D_uNZgJjFRui6uWoyh_ua-g8d5FsSim-lnxzR4VtLssu3T9cr0eAHa78bGxx7SHXb5VY0hU-UD-csuCSD34iLk3--MpJWC16Fpr-65tzCQVCch_20Ptt5s5HadMk2CRFdcB6v0kNQXJhTHwJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOBZqb56_NluyIPMUcQRiWXrA3trFaOtw_Q6NKEd-hEzXFfVWThxCYKf98Cx_4lTan3Pba0F0QgGDCB3YjNoIYeK9BJrS5spQZxIMhUOajfj1zTtocvN2FbmTg1cUNUhxpM-JPCxZTR702TlPVB-8-LsLw-1k2x_JjsJjc0h4Lh3GuTaw2UIRoiafzrDoYQVo1SJ_xAbOC3BWNRaNRJOlIEdVcbkeReNor2MAvTK6lBOUkugIlBKjbobxNOf8sDiAsdf6SMX_AFAXBmXe3_owxQREl5adjV3ujtGNJEHiW8oahEqhDUgPUaEmYLAxRLmO00u8RswcWiXtTaRpTcQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFU38KABlttMldTwCx0FidJFa9Z-yEn2VAuKIzybLe5Dn0oNYV5e-_t1JLMjtzgT1vxdVLxPDLx8HBoP22F9hXAy__CX_S0a2FY8f-_t_vU_YsyuXYTOOjEkzlz913cMVzg6DEVVpCA6_qUwj-pc1k66t9uRxDeiAfl2A_B66vCigUH_efLJ3bZ6b4xX9zB3RotuaeK8mrNWJAFEY2j_Xn-Q467_JXhdgoEgrjPks2UOljYTiUITbit-_ESdu3E4lLAohM77Cv9soHIugCcUF7TGeLRnjalteZQ8OhgGFu4gMDY9BuNx37nXuEJIV5tO2QLkDZPVFA7VEiL_7qt7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozYfMK8Rc5XpdNXdDVhQOLCgXfwhddHC9f1j3VYkagHMHd_5vsTiAB1i12ek_2-fTvHHLlDItvM2yQAMmsvEZ-4eJHCSON6fgtO_0GNqTLyEnTFdk86ePPt4HHJUZnxt_kwctIRbvEQf-RlHleghjEtJO5Ry7oYMoZsl06YMfV9JRuex3NlBTxX_qU5kx4sXf227PDvThArFVLJxr-5QxaXfV0fAZ9_h7OXLZo1NKy7ZXpdCWEqwCP5zKOXd_Vqwu8UMbMJyGHUD7ZjBlYKuHKjXAK7bVFvBddA4FdRZ8GeTsVa8VPMRRkZ4XnhQWeS1T4K2ayfB7RIed5mtyjEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2DPeTLZBT_jF1clpaO5Z4erI55omhE9ZdX6HIG239PzbCVSBOmQ1YrqaRDtYn3aOfHQAf279vwMzEki2q7jSUVYz_LXauIiD7N45snXCKIqUu1ZzfBxMqsPZ8ryl91AMjyjyw6sjsG7RzOnQZE7H7yHGAzts-DYAXu04cDqfEPqBcJlJyWbwmdt_utrrjt0u2KqSzVGEMUUOiPANxyeYt02V-Kwm5_wZqST07wDjl8RB6iT3Y1Rj8Uhm82XMZaVKP4NiEwYmgGHCNqvN6shb_vNpKEUFzEEqgZCcdPRyArkGgQyjoRMOOGM3ZE2w80Bfkap3z65oo-Fx-vuoyYpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZdQDbi7ZVi3q9wMz6hEHjADo7HocEfJodBO2OlgckUKkxPBialDYYJ86jlqcEF90xRnz5GX9vTYLKRDxHdP6L9AxwjVE7JCZS7uwj44haMffpA5VdlFklmYmMLknZpQxUu0SNA7-QJY5m1XSl3oknW_7M9r2OSAfTVDoHeiIUrjdXnqMVChyjfQGg53Sh0Xou8bpe8zY-O0mVJHd2Kfe9Cn9gKaqZBSR6myfSgR0aZT0VVYtvrrai-hAyyU_aPCq_O-o-Qrm_VAycnudNtPfYmxnjlLJpqcszEjZ7UIBiQTi6ws3JUfo9XmD7olv4tTnufWHTdnE_OUfCt5BYVPDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvfiiJyvLbnloNawtWmcohgZqAIO07SCrFlyVqGr_bwPTPZhjWXH1EEGOu18IobpaAj6LXy-Roq8WPiYON2Us8_U9N37JrnmWm1jL5NQowf5HJebfkH7zSfC-dtwmvhFM1o3Rhcl6tpmCIAK86bSCvoYJexGhK_sK7vnSKI1e8S9ZaYfis5-aCAxXBeVp91F9sR6zgszvQ5F8KgckCxB1WlY8_-CVeubRh4UuSTCTt6sbTS3DMAnRmC8-MKTAgxTdZrpSm66_H6ooXwfGLQ_2BQELMFUUnbgncGVqvWGSeuBwbjhkwvl47-opAva0J3nNCls0VzZwQdtIyt0rcsYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
