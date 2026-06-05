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
<img src="https://cdn4.telesco.pe/file/qeghiE8jeUaI8iy7zxIkIG0DnkQ3UgsNuSCjJ2lwj8uOgij4MwKXcJK7gT4TA29EGphsBdLksGURx2IoiQzq_ScWSecjUzg6EOFPGiEHO3Zs5ZWma1jYXre2Va82CO_pQ1caR4nH7fEIY-ZovabaB6OvpJX7sYmScLjup-95iPuAZL1h3uHTHCR_9MLHX0xYns1e5nmu9doYWDXZKCrHATJB4JTL7H-dDqFos3eRjqkNpxNXbpfKnpNciYVms_GOOkKb_Fv8hYuYRR8SfYxxLXlaODCgBSyhErSFs1KIn-3NUFgUK_hGbQDpXO4AFq3M6skobeWEu0l5Zq373IA9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-65319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=oq1yiUYWk0tXzPgDmmNZvta8dbPt2sBoxhu50D02uGZsBenyTT-FurOnx5o8PYKm3_OjV_8krKMudC9RY4n678Ti8LFAzF2-iagNcfFloHlP2eeZ8sABNe980e0oX_s5fVY46z1unySdiYt7pFLXaQt99kwaRqmyoN1jYIsGb-j3rLrNO9Rv4wF0iH9wldX8pTRgT7J7d7QytawhLsbHSbsrz2vQBENxjo-TUny_i2YlfP8hN0QTf1Vxgy-CB6m8nwPFhDjeoqrXqwdNbmZle3Q8s2rhx36fhtXmekb9tNdcYfeUqL_7rxEaJHkxj6Q_zBEJpZbUPYg-ZiZyUP_NEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهروند کفن‌پوش اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65319" target="_blank">📅 17:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A4R2AsnA1FwKqgsMerlpwj5RkB7sTtp_bKkAfYNG1qDvd_DbyvHEyF_rk6yicSG9hdRHOmh7uO_EqgJG08lEFGzGUiD5waY62mel4Bm86Pn8YMq1ywpTvOUQKk6HzmU1RaihPh9AkdFOkJ7w2auN7dQGuO-avm3KTXAyYIWtNe6-MCOtCu7984wwkeVZupmDDVEI5hM8p-32-gxG5Xw-Krn8mJQDwdS85IklDdMvIQpROSAfpHne9VWN8HK0YnAh9t4arIhbITNWoSuk22SPsiMT6so8LcHm99BT0A2-1nEvm8Xx6Frf2CWSRJ4OUlapo1gwj-m-4-r87hVx7UQpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cDi66_mNSLcCd3J2g1GblkjelDaquKpVGgGb-qbv0O3-OAciAM-Dn6NF17O9xr0qlgaSLe833oIv5YBg6Mx0bDbmtLSLmGffMGFtU8kFwV-I4ijy05uaTgWp621KCIfv4x9Tp1ygBUfw9QLJhW3j52ryN242FyEMNfb9r3bfzlGsuCD9esxb_9QvUwLfSM0s_5NBuvhuJ0o1WyEj-Q6o82K0ZsfAUCpiiJLCGru8110VJZqqpoZP9Vu6f6lppdZGQgFi262BweqO9_YziNHIW7ytGlaWNlOEoKu2XNGroB72ZpS6V6qyq2vuoepfzfLL4OJr3fT-FbqaEA7D46BFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nT_GuD1h8D6GxcagBaznAHidqU4rfFGtGufPxumde6Ku_l9qKgsCbohHR-DNRTrRVwnu83T5U1nHYNaGt5Q1VSphvZZDduqksx-Rryp27VZpbD_CoU7mt5p7Anj-bN5Gs2KXv0LKfWMaFR67PUbLdysv3b8IR8cyvFxDBIwAr54MCYTa79N-BF-Dnjh9mQ2fIdVKhVnjVL5HnkJUb8cy0H87YjCeeDwB3CCgYfOz8rOD0BiWJDBgT9ZZtbQCewkiFymyZXNyeG85QDF0Udh8XStlJWwSXF25zwsaYjJTaiIHP1LjbEUp-1yNi7pZM2iulmKIV2sJeupNOPlVQpnCJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65315" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65314">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9A-v9wbyl0UxMfufyme9Y7dV1xIX79ALbikF1noLO03NUWlb9Qlk8IlTSaXaObeLBoFf8Mt6KnDABYPwVBomTIAaip7DuypKKQlPPsAMvy16n2rr6tQXZcko6DCvxF_U-FVS3sClxRqNNE1x37uKft1sKSsfFT-JiJmZAh3NUjkC3-Tb8S5ce9P-oVfQlYMKWvDzYuIY3YkBlPTcXWcB_8JwGMKKaZgQtoyuqz-4ZGl3C4_EZMMVWd-jyrN_RiZrQvUt9b90LPf-0OJ3RQz9lYyYW-lSF_2JzVXRQTX1_EPSjQTwOjj5ffcpAXC-dBZcTaUJ33Fulqy_ZHm-Re1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
خبرگزاری العربیه : ایران رسما به پاکستان اعلام کرده که با انتقال بخشی از ذخایر اورانیوم غنی شده به یک کشور ثالث که مورد توافق هر دو طرف (ایران و آمریکا) باشد موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65314" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=CxPpmPp5VR5wpLIOGaNYEHL33_14XYMlG6X-YevKUQIuxdrPsvvEXa18F6xM0Xp0RnySsDI-2CQb2ksqxp2o-ADYlmxZxF9FeJbLuLD9k3uGnlMzlaupkP2birkbJ4EDbXBRZ58Rgz2N6hplpyjTFMkN-grHvUurXjLGoO-bapXQErm8fXKkRDKbCDkiry2LqdujxdzjZ-5jJRo5tOA9KHh_8WD4J4udaoK7CmLPLbKlpvyWSRemnTeClAY1zb7kQKbkljI_Opm1w2pRMb8ctLQWTb4F-MgfUJlzSE5mAQp_20-jeAlYninKRAPIXuOd-hyNO7KP_OqH7EFYPPzBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیصر خواننده لس‌انجلسی برای خوشحالی عرزشی‌ها پیک میبره بالا
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65313" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxq8wiJouZdUybB-E-_oW64PQsAD9ODxyxcZQdLjL9rh1RnueRu97bK6rF-todr1iZLKCopQ2QrQDtagnHXMx4Ga_7jqfLOVw_JMLWqF15ZJhPMKYOQpSz0KQv8l6NzRx_jvKqKIHRCybBtqjQfSC86lXmX-L5D-UFJb48NGExYm2Tu03ur6DWOFyTnV7tYQf-j2cQthIg5ICeR6XNtOl4nUEFBM0bJMApryZ-IMiszpgNHyOt2-Z1vQEEsy3D54T0sIzoeKzyvL0J8lDiK2pz8rKo8EX3bZtX7hT6er2oWRJSQuLqEFE-dVAhnbCG3T34EorRSjV3nzJxK_nHGMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت‌کوین رسما به زیر ۶۲٬۰۰۰ دلار سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65312" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5ff9567a.mp4?token=hnfVR3DZNbnj4EYJTPUWjMZdrP6Mj8EIW4AZo5BoAk158XPnaOXbZnuzKJu2jK7ZCE-40MAZcbuawi9XcxDtHHIkh3I75quGyROX2q6Y6qRxhjwP_9HwRn4pYlBKsfHwaaNGQEuMS3jYFqL5j_spASkIs8fjFgrMjRUwMrTvjeenPpAmdAcQGmRPKFNUCmVUfXhitJ-XqkNCHyDZ-epSNZQL1ZgYXr1JwvodgETl1MnJj1ou9TDOaOUytrmxyVliw9pepiRO1S_SHwsXy8_iKvY7MmzatF2qaKdkf9SZ_1CPhBgeexGN3Wmfve8T2wPEwp-3mDMuHooD2_V2LsqEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محمدرضا هلالی مداح حکومتی با زبان چینی برای عید غدیر!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65309" target="_blank">📅 13:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7d22fc01.mp4?token=K6NOwj2MmwidB69elEj1Zt0TUnl1ePiAeeSw3DIskRkh41f3EQVyz_A2dI3FgB3GD6tnkBGflY258l3zV59e6fgzLB5vG9FbYlEhLM1L7c98gLw0-8SZbC3FUfOzYl6i2iBz0Z0Mvir6O1d42MKp94OJbV4H1Q-IYs-vhzuZRK2h9XWOftKgk0qmxUO0aKrja3JmEV4lxKXwAMgOw7btPonVZw1zh6exh9jfUrUwvaMYmgB193OxGP_9OKOAfmGyfzwD6_LUrH8mwXekU-3y5QpNUjo0hUvWDPnc4Mm2PEXxuB2-kHKxQ7DS9Nin2u39K57GRmKSxP2OJ8AbwojpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: عملیات خشم حماسی پدر، همسر و فرزند مجتبی خامنه‌ای را کشت.
🇺🇸
ترامپ: من فرد مورد علاقه او نیستم، اما احتمالاً او یک حرفه‌ای هست
در برخی زمینه‌ها آوازه خوبی داره، برخی‌ ازش بد میگن اما خب درباره من هم بد میگن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65308" target="_blank">📅 09:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پرسرعت وصله
👌
👌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65307" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65306" target="_blank">📅 01:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=J4HXdAOYDOUWE0-LG5seD5Wwpw8u94YnJAUFQv40SjgrNspW5wyF0HSDQTY2bSvpV4nBwRNbuz3cIgZKXcgQEy0TpYlXnMCHIBJYCv1cTeBEpdpVi4OLDukMmSVSWvHcD3oPFszS-eP9-2EJV7ReUgdcPW-KdSqZwqW8qeSo4l1TJOCuS3tI5Fr0kuv24WkrRPiBFTE4pIqqMFSIFmNwfMgkS6UNybGDgkBwLA75ZJRu3xBCd7ZwJrxMLj_FxpS0kj9OM0InlA4_AKVgUrQUpunRDLCBakbl_e9q1EpTzpiMDpznLlS6TlzU3O4GWMdWA4_BKbif6hIJRLA2MQ2Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم. من محترمانه رفتار می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65305" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=Ap6140bYd5a3sFYWYPUgJ7T9p1EesHVwr8kZho0Yuvtd-MX9wfVVR6nMTsk9hgXaWF_LcBDUhH0K8wP9jd6fuGozwwnBnXY4wsAw0Wmmbrgu8KIoWVEm24fcQeOc9OT1NAcjytVvmzwBG9uEZXNQfPSASGRZmRbVu5FDo4yotifOw2UqlbnECBWUMjR45SeST0NCwIpSZd4eUK166q26i_Fr3W6YnZKk7fFg8bvKJyfs2Rws3SHDnDdKtApxzHgmBnXN2RMPFJRov6kELql7Yph_QOu6niK5t8L5WdhjyUcKcWWXXjkxp2vxa2RaPUhUfGDbaxx28SN8_FUQwVyvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران: تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65304" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=H930gsDod75IUkNhCfJP02QgtkOoOmuo5_GJ-8RvsctnmoWcEQpp7yrwjSnVqGcckJ2v77DkXvLVoUQPWxseBPoaBZ_z25afQh5MmEQakepR8EWVWOjX_vy3YQyiOmQ7WmLWYrfKYMv8UjotkGJ4UmMHqO2QRKdwQhH7BYJtzgELdBybfl9q-IqKQZrILzbyTBeaviiJ3QWr1d9wJ3SgTPo9xuCArnn6w8Ut2doIw-mItC6EsEnbYQxsv0xJ52daHXgTP0E4cpd2Qa3fJPbvXUaRSQtBpXSx71LEyQJly39WcW0eCK2yHKyo6nLVJvPI2DIsUwD4iTO3ygLwt0b97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65303" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=WV0N_F45SE9PO6ElXZc4Fzmc7glKZ9QydKt8LgifxREzhBmdcDZHwmjkvny94HjB2DNJNZORpQ-BL3IopxkoIN96stJ0SsXCx9IiLpAdxkNwNRPnYh8oUGv8lRrfYyItMwmTPeVCFHiWTemlLR0dRZ_5-NH1ZkQPOmyMPTSXsXirweyRLHqxU8lhUXVTNzOVutLPIYBfgZYuCj4CAWq3ayTAvs0seR1HR2trYB-1KxTAH-Kt-nSVHEbw3BIaFms2YAoPSKKx4_GmHwZxLaS0SS57SgLkomk-2fRDxyE0mSwsMdtfXwBWUxsZ9A2P6xSnFkinXa_fglEukmEhiV06yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65302" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsiWpIoiWa59JCirB-yWGcp1RYcec4qOhsHaCDZI-ACRkhio3gHWYx8LQYrYEWCAVmMFKzKPZwQoalFkVx2uBAjapbw3dnM72phchMMKQ2jo8PoVLK8yMvCwvp3olmdsPTAguLub27THsX9UGLzBvzsWRsFFf80JzT5qqfW0He2fosXL9TXhp0KlWYP2ePhQ84w0N7qwY_vcRe3xqKTI0mrFGgOWqxWBleBVTRu0AFTRJHwISY6JSnaUu8W12RtgZBGiiR8HQzktoxBwtj1TxTsaep-0WyyHGuTSvxkLizv-HMtInhWl2gRdVxwGLFNmx0Zpm7GRJvdOkkML7722WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSpLB7R954pqKR3nK0GbeGDKpAeTShzqNCzb5Bkem596pQ1aEmK5Mc4TZRozoL3wxbObScv7xkCEWcxD8FU3r2Rc0pcMYWfob4F1MKzs9Ft-EdD8BqDbyehStx_QLhU42SeDTW-tECbH1vtSmmGMTjdgYjN5QeEdTPlw2NjY7hstg3iBrQKrisQYYqoBFj5-D8lb_L_N8KInGRR6SuxjF5KVRM0I0Q4N7QD8qeusUi0Y9DLe1yTqg0uSht98LHzMHV2RTsyScbmYWQxYnjR8AKN98DTYQUKUsKHVg8JSgyPbr_AMvqGyl8HtQ8N6ZI6ykNLOmW5JNmUNCQMxa84iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfrizdD68wa2hOQBybBr3-Y3FP_-58u58RN_kbPIB336EdzA_UTNT9AqwhUJ7yJje1MToPSNDouwvBq1NgofvmGnJHnTvpNg2D8inywZ75ha49nVGMfDSJEVaGRsGLGTfu8rIbX7Gmm-Hmmap_wJclB9L66ILZDp1wquy7DLrDK5aun7yzlLZWHg5L8E_a1_3octbGEeA0NxkzET1V5A_Ch0E85errdajrcpltWOA1zxIAUStSkspzx1w1Pq1MBxKoJSpBTZ88PY9RaVi0x4-MrGRChPudx5Btr_NJt7zSFCZFaqHzsrn7udFkUqC6BnypNdHIMm6FqbV2vQQm5VOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSo4X-5sYbkaY8d4YEFFd6MYxi1wG4krphBs_FBxMonj8ZVDfrobKDgiFNrhL9t7OuIUk06L8E3CvCG89CMD6mB4NWJHXwZ84sckAPZM-HAM5oic2UxYxb_ZXwzsU7ZgY4oGF91gkLUi-tmqFlBSRhg-x10IsI42Es3OAYN7lHkZGhRlO-3bn-jzUo1hbihsZWSUcUcuBNQZnOA0VRJVUVoxqrQE6aRghBReKV76jKUP0qbh84xYHkdDHPjJt3j44mZMEJP5Xg_KPtY0bizRrwrUV0db-W1BciyJE2aTqTugTMvDSMqCB0MgzM88P4pys7MBB5235XHgs65M7WWgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvQE3J5Wz5OkuLSfJlrU04JrQ2Ku465OF1KAO_tGey3fxcom9LYUpNkA49hFZW8D_e-6yaPR-btc2yXyt17M-e38cO1V5Pe0TlGCo__O0XUiuz_DmURnlWUAn06PGl3a2047WgqYSuDITj5yaPYmBj3235pGdjToWrOAnoP_Fgb2IbGK7YlQEsPgh_OkJHbtLgl5Sk3PexEfE4AXJ8DhKiOC9NQeZlF65ohKzIw_8zYkP1Fc1DI-uUnocA3ub2tTL5Lo2fDsPMGXJiTkHgf2q-Yco_SZAc-R0dl2ZwKPGKGoNMfPst4pc4WQloLy-5bfZdhhRw4TNAoaoDUZCNiATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=brCWb1AGxAvYt1GV_K508mK0e8Ny9ICLphmhn8CSjLiJhjnuXeEprPPLdU6At7UxtqNwPF6JtqgrkTu_p1Ca7QcwDXtWXCYVUEn3vlaIpHI0mrKEYjTz0g9FglUR1ER5h53T4U-i--Ouq4l6wY63dHSPGZK_x46d4xlDGi68w0sHBNU1iY2rbcfl-843UTqpQ-dHrUNKkbYTgEss07CwauJCk0bwZnFgF9umvZsDJm-p78Apk5UYvkD6iqKyKMTaxXZe6qd3lhHstpUGLPCUChNkCns5E6ciWYYXtxHK4Y55nVVt9fG_mG4p6jHLt-ERkQGItUmW_VurUGKPGzaFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=brCWb1AGxAvYt1GV_K508mK0e8Ny9ICLphmhn8CSjLiJhjnuXeEprPPLdU6At7UxtqNwPF6JtqgrkTu_p1Ca7QcwDXtWXCYVUEn3vlaIpHI0mrKEYjTz0g9FglUR1ER5h53T4U-i--Ouq4l6wY63dHSPGZK_x46d4xlDGi68w0sHBNU1iY2rbcfl-843UTqpQ-dHrUNKkbYTgEss07CwauJCk0bwZnFgF9umvZsDJm-p78Apk5UYvkD6iqKyKMTaxXZe6qd3lhHstpUGLPCUChNkCns5E6ciWYYXtxHK4Y55nVVt9fG_mG4p6jHLt-ERkQGItUmW_VurUGKPGzaFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=UXvyoaTcUrNrOVQ0SH__MHUv1CmDXhwumgAdsbxjU6cyatQNbjyZQwlv4vI2Z3Rvd_ArfGR4xR2LTLg7i0aii8cSNLNSZpdukm1AaMkw7dN8xJV2IeUfceeeqnfUqdMGFObhFk2Aa5QdEQ74-aqzVxo2SXK1BFquA_JOq7UwzZTNRUXD_J9h3jGWSbuAsme6p05v2DjgP_jIh9xkdkcwnIrMh2VmN4TnyO499bgciITcG6vrh3ZDc8CdcdMAI6kcK6MCMvStXauK2wd4Cer6K8e3zSwk05SFnGirThl8oBjOZbsiNhQbFhbDli0biV1tCXXhMC82EcnMmo8vYTwkPGLBk54dijCwwyIO0PQvZP9F-yWrMTSRgTKEv-bn_ftUx5kvcEmayS1aZOBjkS779qi2NYei1hO9E4Hs2aySqj57zEDYW44hTNBqbQSnJi_DzoGxE8FsbMUXqPfco8r0ad_GigVqtC_a922FLDBJ18DtN1uB3JDGwo6Q1G8GCAiMhu4iaEEtp4Y7pnNIWEVAhjfF9JNgxKzQncj5WNKEgeFwt94k2o89qXO3D5A7OwtOsgUg8p06sDLKAKJjDD_wykwZDm4qm6J9fVY89SfkRYdivQCR_iNxXyFDN9F-HGDno2JKoi2aSwzT4_xLhJpPAnSGd3Ncgi97maVFOpWk7n0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=UXvyoaTcUrNrOVQ0SH__MHUv1CmDXhwumgAdsbxjU6cyatQNbjyZQwlv4vI2Z3Rvd_ArfGR4xR2LTLg7i0aii8cSNLNSZpdukm1AaMkw7dN8xJV2IeUfceeeqnfUqdMGFObhFk2Aa5QdEQ74-aqzVxo2SXK1BFquA_JOq7UwzZTNRUXD_J9h3jGWSbuAsme6p05v2DjgP_jIh9xkdkcwnIrMh2VmN4TnyO499bgciITcG6vrh3ZDc8CdcdMAI6kcK6MCMvStXauK2wd4Cer6K8e3zSwk05SFnGirThl8oBjOZbsiNhQbFhbDli0biV1tCXXhMC82EcnMmo8vYTwkPGLBk54dijCwwyIO0PQvZP9F-yWrMTSRgTKEv-bn_ftUx5kvcEmayS1aZOBjkS779qi2NYei1hO9E4Hs2aySqj57zEDYW44hTNBqbQSnJi_DzoGxE8FsbMUXqPfco8r0ad_GigVqtC_a922FLDBJ18DtN1uB3JDGwo6Q1G8GCAiMhu4iaEEtp4Y7pnNIWEVAhjfF9JNgxKzQncj5WNKEgeFwt94k2o89qXO3D5A7OwtOsgUg8p06sDLKAKJjDD_wykwZDm4qm6J9fVY89SfkRYdivQCR_iNxXyFDN9F-HGDno2JKoi2aSwzT4_xLhJpPAnSGd3Ncgi97maVFOpWk7n0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCxkKa9VvAUhnWcAOTokwGNq0Qq7Y5dsmBQRItrp1TWuz5S8C299L-MeE52q-xcflV3EQksQMEvGYE5_VokOXPbKqyAG-BCQzK8z9SH6pVtsd3AHUdBeHbFZBCuXHm8yat711AW0xTPRN1jokMQ7R_YXY3eSw1xcXycQpqlHX6NpQZyGajPTUgRXuWqdKwwM_So5zWS9O9_Y2zuAvjbBCBBzm41arBuFQ8cmdnGPUNkKdoNUoIKVy0sYRW9K6WTR4x0EdBM2DJqb8jDX4OY_yOZniga8mWFAok99OAwERtBxW9l0MvfAGC10dWd-EtII8AHDpuNdXZF0LjYKe16a9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=fStrIDAsWMrWuLFlFHsEFTdnyZoFizpTs6sjWCeMU8vXtQL_jgGT9CIoKrVcHj60FFICrfQmNjkhA4aGK4lfLsMv8YG7PaQ7hKpc6PHW3Sl4GRZYwcmp6a2evzzGgoRabiEQLbbEkzHMQ353eTfuiLzRZfwkr8aSA5Lv5LzIno5qrBCzb5gWAI2BmlH5z5nCk6-QXdlKMKwmv4cz0b33mMfVogBFfJVE4tzvyhUiHvEA01ueSWMnLmRRrgp6zPwcNHccJRWbBW40auzXoZaFaW1z-LccfqbpeyP3LRWvUfs1aEKJrmxhEvy6R8olAjs_HFoQAq5uGHLOr5MNeGvYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=fStrIDAsWMrWuLFlFHsEFTdnyZoFizpTs6sjWCeMU8vXtQL_jgGT9CIoKrVcHj60FFICrfQmNjkhA4aGK4lfLsMv8YG7PaQ7hKpc6PHW3Sl4GRZYwcmp6a2evzzGgoRabiEQLbbEkzHMQ353eTfuiLzRZfwkr8aSA5Lv5LzIno5qrBCzb5gWAI2BmlH5z5nCk6-QXdlKMKwmv4cz0b33mMfVogBFfJVE4tzvyhUiHvEA01ueSWMnLmRRrgp6zPwcNHccJRWbBW40auzXoZaFaW1z-LccfqbpeyP3LRWvUfs1aEKJrmxhEvy6R8olAjs_HFoQAq5uGHLOr5MNeGvYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTN9tF9HyBfd9cZIDPuo-FGNe3rLPy-o9Yehjh6e5nsjV_9vCDDCjk0kT-_3yw9CJoonXk5MmMACOm9Vy9etlh2pkp5Z8Ou7R-QWAiOoJOE9HxBAoA6H2w0kt2bEcBRtcU4aiKHmrVq6H4KyQMTlQasC7lMKx8FkiQ7eTbVJDUHBUVeK43QKu3PWke7rcyEr2CgwHKbtWfsTl5mJEclHygRI68k5UBMvi5rPNy6OTUST3ZFVLp-HG-AMPgK5IL2yO5d43f_2mZne85fEbfyD8sJTRJx3-sCgvtckLzV6uSQuLzO7rapqRQmZkuBD7G1Php0F7GKFC6ioeCugVt-tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ooSsT5OPPFZ8_jDzzvOpYITrmceRQc1ZRaCXJCAj3weyFsgRBjv2P4mArCASixQ342a3_Ws_g9yiv6XRYzVjBqg7v9-yta-1_oidq9bq9g8MF6eAYNOkAEpHbcxA5zZztb6_3GId_KRwQY7ZjH2kca3v-YxyHfS_g35wFfkKnLnBIwjqjG68JaRMfmYn6kCaFEwGTH3v4yuvHCSc9cFGOcvogQGsHMi5U9SofzxrOkz6NDZzFIMOqg25aIWcA4ukhCFLhgFUDmfi6xGvARq5vXui9oVvuoICJEQe4Qbuo_nZldB-KCFJE48SjlAh5zUksEEJqrk1xFJygXtzNqHmYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ooSsT5OPPFZ8_jDzzvOpYITrmceRQc1ZRaCXJCAj3weyFsgRBjv2P4mArCASixQ342a3_Ws_g9yiv6XRYzVjBqg7v9-yta-1_oidq9bq9g8MF6eAYNOkAEpHbcxA5zZztb6_3GId_KRwQY7ZjH2kca3v-YxyHfS_g35wFfkKnLnBIwjqjG68JaRMfmYn6kCaFEwGTH3v4yuvHCSc9cFGOcvogQGsHMi5U9SofzxrOkz6NDZzFIMOqg25aIWcA4ukhCFLhgFUDmfi6xGvARq5vXui9oVvuoICJEQe4Qbuo_nZldB-KCFJE48SjlAh5zUksEEJqrk1xFJygXtzNqHmYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn0FIVvKpO9fjmkTey-7QIzz8ALv0cbeI3iEDPlFOd7yEA_pTyn72XejaWEgEgHwkDJTdCf0Jz_alWK1PPBCr501FWMo7UZ1rMr4G8WpoXZnd28MX-3aNwyWMvBe5GIl9b2oSkiRY65IpoIRfT6VQGyCqSKyGy66spTyBD5hLVAtpheaoxv0E3AVa6dDAJvJ8k13b4AQUJsTEI0mNfLZTwlk15z3N3nHB8WxdLr8YbDjNypokVw6Jdh2sqd5k7ONT7VIFAF9zCwlGHiexjG3jwh_S9t42UmArOsyadBPw-tczWoS_7GhfsiogFuSwTA7SpfdP8GPFUnYDjU2C7k1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=NUSlXG56OwYz-TwdYn5ZahNOgJS-VfqClTRS2COZQHxylQkeiGrRYFuPdMDluSVd0pxm1wnFNvEFHGMD5XD0dHO7EhpJ2Lv6smATyxBbthwppZfHHsbADwOxk2BI45l4u8AjGID9uqPluBUgLiMrkSUFKHio1JxIIP9igmWTi-uPqw5gc0oG41W6NpSP7dYsKSFPxGcSbCevPvB9uoOVw_u_mqerwRKu58yL2RQ29jqP-dkosnDOotOnhrPsUtZ5IAsLtvu9gmnIMMgrDXc4ja2JYD5xwjXRs5uBnVgcyoWZhzW12X424JrfwrXxLugZXWSA097VOq9Z3ryT0fXrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=NUSlXG56OwYz-TwdYn5ZahNOgJS-VfqClTRS2COZQHxylQkeiGrRYFuPdMDluSVd0pxm1wnFNvEFHGMD5XD0dHO7EhpJ2Lv6smATyxBbthwppZfHHsbADwOxk2BI45l4u8AjGID9uqPluBUgLiMrkSUFKHio1JxIIP9igmWTi-uPqw5gc0oG41W6NpSP7dYsKSFPxGcSbCevPvB9uoOVw_u_mqerwRKu58yL2RQ29jqP-dkosnDOotOnhrPsUtZ5IAsLtvu9gmnIMMgrDXc4ja2JYD5xwjXRs5uBnVgcyoWZhzW12X424JrfwrXxLugZXWSA097VOq9Z3ryT0fXrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=lgUxttyWWvt8tlTR99yzFHIZQkWe2gxrcYqEcisbow0YL7knd1KsEDHMroIa5r5Qn0XxZifGKPV67ise0V9TQb8Zbb-pLmSdZYGH4s6zc4lCBpdn4xkZ93Co7cLWKn5Z2pWMEgxutRfuk-0tx8z6r8saFZATTC_J_OfEt8187xiRAir-HI1-KknPphNtEVk0tm6O1MJ1PLIH7szzNSZQw6CMrVDy8Pbqv--0qARhysJQiLXokREFcMMq40mkO5H-uL6wE5iggfeGXdUXvFlLe3ol7XKvma0r12KAkCsCXmfn7lmeGIAM_cxUBLmqhub8vtGC9ZMfP7sDzU_Tg2xCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=lgUxttyWWvt8tlTR99yzFHIZQkWe2gxrcYqEcisbow0YL7knd1KsEDHMroIa5r5Qn0XxZifGKPV67ise0V9TQb8Zbb-pLmSdZYGH4s6zc4lCBpdn4xkZ93Co7cLWKn5Z2pWMEgxutRfuk-0tx8z6r8saFZATTC_J_OfEt8187xiRAir-HI1-KknPphNtEVk0tm6O1MJ1PLIH7szzNSZQw6CMrVDy8Pbqv--0qARhysJQiLXokREFcMMq40mkO5H-uL6wE5iggfeGXdUXvFlLe3ol7XKvma0r12KAkCsCXmfn7lmeGIAM_cxUBLmqhub8vtGC9ZMfP7sDzU_Tg2xCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku3a74_bRPdpzDfPQ-eGzOHLPozJ8D2oGhSLtC0ExoJoXx7JlMNS43Ld_faNELBHp2NuGj7rzNSPCdlVu2u5DMhAxw7dnQvmuffEUJGXQb0xOs4nqWaSO5hL8hDmoNRy9a4hYjHNgpVtymvpOZCenZ_GBaF0taXXDCU7eTNsASpw3aCdjrj_Uf28bJf7ThvVWSGg0Hv0ntjY2d6DcqqK8q_rUnsGNi_pFuzSZ2Hf2pMr1KP3EiIFxJxBe7c3SpKFgk8KBiyf8R5prqBq0PhOamqQ8oMHLFMm7rv41hO9Vi9cSeLo7HNzsGNTa6kEQRhSn0YoNg_1fHjSICZwDsQNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=MwOFlU32SwyI1oooY-ULUyn9IXY-Tg70SQBSyDg5TobhJiCiBSkdg9vIqbFSCpliX1H0QK1v81dr8UOkKCWBeG0O7B70CS7g8SWnpKgpzfp-bURO0fVu5GqlXGc-LGRUsyunq9fC_hMWgoH8NR4u9ueU-sjydLPKUZNuxeYjn0d5y_djX7cRrA6j5Ejn42Ttyt0g0oUFpqwDFGA2FFs_w1IaTCdNxbWK4kFmPNRLTO4Qc4KfUvXxbA00QBFtp-5Ub6wtyIUq9ZrgdXxQA1zS89-CEj-G_TVfB-NY1nERlyf-BS4m5OsHqZsFA4ortsui1G6tYNCW-KS9_AkQ0E8t7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=MwOFlU32SwyI1oooY-ULUyn9IXY-Tg70SQBSyDg5TobhJiCiBSkdg9vIqbFSCpliX1H0QK1v81dr8UOkKCWBeG0O7B70CS7g8SWnpKgpzfp-bURO0fVu5GqlXGc-LGRUsyunq9fC_hMWgoH8NR4u9ueU-sjydLPKUZNuxeYjn0d5y_djX7cRrA6j5Ejn42Ttyt0g0oUFpqwDFGA2FFs_w1IaTCdNxbWK4kFmPNRLTO4Qc4KfUvXxbA00QBFtp-5Ub6wtyIUq9ZrgdXxQA1zS89-CEj-G_TVfB-NY1nERlyf-BS4m5OsHqZsFA4ortsui1G6tYNCW-KS9_AkQ0E8t7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni5KGlt9OQDDu3ytW4TX8JdbjFcf-aYGMIl4o1qsdfcdk3dEkaztLyEl7kS7A60cr81wfQoEg-oQyU62TG1pPlNcihV3b8QuR6BV7GZB9U-bzF8F-TclL7h6NYXjkcQcEvoCa7cLMiapRDHaiDxhqkY3dbSBeM8fFzsenNRPXvQSJLxDAJFQp_sTLp1Q80r5bEm-ZN8Z93oSjW76VpHANgO_DbGZQHS0ECi2j1dQ8jSPPRUgKWP7sk3b78r0h-LUQIBwvTIvmTYQOX5FJFHVNevjGoxwh6IaIk-6bEPTuivlZwY1X63Hz5YLzF_8ZimoqoqwHz7jPH71Vfcumatfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=K3K9IX6QLCWWYOkhd_7EbRgUvQrjp9mL16LD-NszvWJzvAqG6vhZQD0pU_x6R0MViEuREIScYrGaTcqnNeAHsM2skCupazIwvaowDr_2AOZMjD9dOhFB4sgGZbmk1p1fxZ8LMDm4VZDO0ngZKLcYoh6V-q6ozN_Bnh_43ZHBEaqPQCEkPGquKuFquYJvYuSI4U0Y3LpdWvG-2fX6Nkb5_OyKuWh2H1XkGktVprz0f0vCO2-47ZuVnXjh0ukg3fb5n5BBZWYzYce97p8YJAPPl6AFcrYN68UxrS9uz1koNothAzv5MHOxkzSQZn6x7Nkaja-p90Jx9ai-dbwhaKx3uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=K3K9IX6QLCWWYOkhd_7EbRgUvQrjp9mL16LD-NszvWJzvAqG6vhZQD0pU_x6R0MViEuREIScYrGaTcqnNeAHsM2skCupazIwvaowDr_2AOZMjD9dOhFB4sgGZbmk1p1fxZ8LMDm4VZDO0ngZKLcYoh6V-q6ozN_Bnh_43ZHBEaqPQCEkPGquKuFquYJvYuSI4U0Y3LpdWvG-2fX6Nkb5_OyKuWh2H1XkGktVprz0f0vCO2-47ZuVnXjh0ukg3fb5n5BBZWYzYce97p8YJAPPl6AFcrYN68UxrS9uz1koNothAzv5MHOxkzSQZn6x7Nkaja-p90Jx9ai-dbwhaKx3uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=Ku1tGBHJ_1ZOUF9gvhgxqZlYDKb94Jr6QjKkzrTx0NdCcqqKGbbcsd4QJFFqQ_TtDLqyGwpAhUiWq_aJhBxMMoermz7aebosU4VuGuP8nFFUaxuBV5AyrP0WPnzJv7eI43uuGbwK2oLUTKBD36k6-rSb4awjj2YruVPq5bik3GupW1dlFJdMxDGXqunlkiKBjs0OeGho--64iWwf0nvltaQQc9OsSFL70vboSxp_CR7ymrhOBf8g_nQ6Ks5WYyuQRdx461VQGkVN2y5LdoTU3Ua9dlNUmB9RAT-5NFNi9kE4VvfMzjCJHJD2ITFTuKY9jehdmd5st1M6ZMD4tCv-1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=Ku1tGBHJ_1ZOUF9gvhgxqZlYDKb94Jr6QjKkzrTx0NdCcqqKGbbcsd4QJFFqQ_TtDLqyGwpAhUiWq_aJhBxMMoermz7aebosU4VuGuP8nFFUaxuBV5AyrP0WPnzJv7eI43uuGbwK2oLUTKBD36k6-rSb4awjj2YruVPq5bik3GupW1dlFJdMxDGXqunlkiKBjs0OeGho--64iWwf0nvltaQQc9OsSFL70vboSxp_CR7ymrhOBf8g_nQ6Ks5WYyuQRdx461VQGkVN2y5LdoTU3Ua9dlNUmB9RAT-5NFNi9kE4VvfMzjCJHJD2ITFTuKY9jehdmd5st1M6ZMD4tCv-1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Ac7aewpNeo597srH7YmugLkgbjdxCFrI7gMYV8CinFDVxyheIkZaCGCRhP1ixNTU-hdMhR2nld1YUSMvHTH40ewBHqNgK4Jal2M95QSoJbL-IKKom_W8ew9RxbjGfI7pdr79u3uGiJ6WcYmSGzu6w0emx-gfxDQSCQ9UP6nN9Q4rmrK70e5DM4YcLsaMclBpTVU9Pd0nWkf5O12MT7peUr10pZvWEQDr6W2qIq_RooCWdXIfds8Uqw6Xm70TOoEOizOJ36orauKpYkJYQ12AYztPNGpAApMPELAu996CE-Y6AZ0YkaZRPd8xJRkAVefPgLdOnfl1cbglCxQb0B7CWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=Ac7aewpNeo597srH7YmugLkgbjdxCFrI7gMYV8CinFDVxyheIkZaCGCRhP1ixNTU-hdMhR2nld1YUSMvHTH40ewBHqNgK4Jal2M95QSoJbL-IKKom_W8ew9RxbjGfI7pdr79u3uGiJ6WcYmSGzu6w0emx-gfxDQSCQ9UP6nN9Q4rmrK70e5DM4YcLsaMclBpTVU9Pd0nWkf5O12MT7peUr10pZvWEQDr6W2qIq_RooCWdXIfds8Uqw6Xm70TOoEOizOJ36orauKpYkJYQ12AYztPNGpAApMPELAu996CE-Y6AZ0YkaZRPd8xJRkAVefPgLdOnfl1cbglCxQb0B7CWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=vUrSYuVHFnuJwgEdW_EK7sE5FpjeB2pEhp9p1MO7y9GNYSqdENEkC23y5Tytw5a8ehqidfplTYsMvAAP7XMWBT-NswP-_jrX-TMVW241g2OVHWRqPh7Z758U2sdXEy9Nm9Z6WnkKWMC9OchkPz2l4wF7c_yaLzFnFchUtntmOeCTklsmCqH6m29RnWgZUGpvcQHP1Vm1fk0hqZHj5-aNpaztDJ8xpSv1n5TbZ4OzjK5gi0iBSMGGQ9bv7T3P3pRKw8OEZoDjZ_wmDqx71g90DQqNvDzlUTUanWoLRXaNKZwavt8qAG0YfnZy6xFCSLJh8UEgEYG9wAxdlazgmV-TyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=vUrSYuVHFnuJwgEdW_EK7sE5FpjeB2pEhp9p1MO7y9GNYSqdENEkC23y5Tytw5a8ehqidfplTYsMvAAP7XMWBT-NswP-_jrX-TMVW241g2OVHWRqPh7Z758U2sdXEy9Nm9Z6WnkKWMC9OchkPz2l4wF7c_yaLzFnFchUtntmOeCTklsmCqH6m29RnWgZUGpvcQHP1Vm1fk0hqZHj5-aNpaztDJ8xpSv1n5TbZ4OzjK5gi0iBSMGGQ9bv7T3P3pRKw8OEZoDjZ_wmDqx71g90DQqNvDzlUTUanWoLRXaNKZwavt8qAG0YfnZy6xFCSLJh8UEgEYG9wAxdlazgmV-TyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-g7eEamH962I42tP2Fmz0TDVUmkxC4-DvZ6dukqLajmTzJI1sadF_Z1zBxtSgCI9PspOaAX9cjzQ1ObLYAUgFwpJXvwFA_tBPQYVBt3hbcsxPEcChjwCmmRS4C91gjrpGC7S0RYoDi5NvPJnUYKTrMtPCznUhEaV-bFAaKV4OM939CQPtwAnICjwMHJ9WrXh7L-kIoTPDHHgMfYcdR7MmzFsqp9cmDJAqLDj6ojQ7b3XESiIByankDbrKhLPujv4uBX7ZTcIiqFPQXg7g_c8N7yr5q0jwWzbz2Dl3JFT7q1CllFsu_jb_Ne_AgnxG6kDMu3wr7h6TgjMNnudxqIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJKqpc3dRk41PUf3KiS9utlv14rkoVuK5h-d98QH_bEMkC-0F04YzUas6wngPj-P3p-5gIUfpg4Mavg1Z5aBFUy4hE0Q1Hs8ssLf1LuukQW16b68qASea68rUEHg2vY91FnAINeDQGkPfjJnX8ehCYYZ7e4Kz5S6f6NdxFWvwu0rp2eTPlKjeOYx7ODLCrR4uuA6SphdLFUvdvag1qcdcE0PCJDjRYHTwvcaScTSzp3c_LCC0-ksD-JDgXsXGUULaQxUl4zJlc3QEdRtqsMGPOLcpY2w340tqgytPYv2CEkXFI0uUSsUvUaZz_9oDHY8_L3Nkjfoh-HI8VlIFJw5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8qws4QLd-jz_c31wfR7uLjXZB4E977TtWck_zilWOTiyGJx4Zh897u1Rp654tIXBgOjOgWiz3YviyVr5hg2Kijv1ojN-MXn_Gs2zWfVO5r-BZONWjGUwFiKBrFrkRd6Vr6vxN_3ta2Mk1YZxHm-wU_BlT0tsClIsKCw5u20tAkN0ZAmPE2SkNggKU2030oq_veOyeJFIeun8F_Nekf8lZsyalh3HK_Ay8XlysDhIYmQnEU1LYXZlV980jNSOWDHDRQ6Id01VpTKSQ4NQhyV1wHmpY4VkBdeXbxnabI48E0uwUUVa60iTuvUti0D-yUzthawIA4GSJr5PrthM4KbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrgOtr-7_OzppcxfiVtGaKwYMbKB8sZjMIMgdY2U0lnaK8_kvvyb2G2AtwCqTiV0R4Us3p29TGdZMx58i_nYFgGvg3W-qq3WspFGR4usY6O_lIAvf9TxYB3KxTyu1AsMW2QxhFz45ixb9tc6EhRb8OmXXbd3bjQ-df0mtk1pfH2TK6l5XDwyrml1qu8g8hAqzOAA84hkNR6rusmZY3h0cyuY5uafxntBqhStwhzQFOxXR2_5_J5wZd2r57F0FVd6aJaOMlTX68NNjURJLHLSf_Rtg7IFZTJgA48B3Be1u39HusjHlaNFLa9nhiOfYbcAaED8XUoqIIFpEeDbG1-cJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ1qJQ1j6Miq99c2Y40kRjeS9MhN4gUokLgNjE_TleKY7gaqlGPYyngVHD78HQzhevaEA8-fFWA9e5h2xQiAKrktkaJO2qex3rbzjSszvNUsAk9bIlEES5oHkSjACy7XKYNvRhF0bBuCpvBJvAXmNyRJmeajxBIerrtsxLdp4TPe0hd_huL7rKdSXLNk7oRqMCAOz7Zr16-S_1rYSLg_nc5OrOyTDzrnc7Eqkld1Jpq90nfTH8dRn8NyTgtpndwJpg_H7X-ouPtQw0nhiMwSkDv1zt0WEugCFWlXTxl1HRFFvAOPlVjSS3_EDhNgd2L-SW4ANsqvisGJwoO2QF3dHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=HWcTTavVv7CVCmtu2GWoG9QQ-GS46yymmV5WuKWszPgs_JeXt0YFze3vomShOeRD00Tf2O9Aa-vKEdxurpMpYVVGcxWdrYeobVVC8RocBmnmW72UglHzYw4oAXMfm41mfQf296QFN50_OJxgMXUv96OBt92I0t5OeiIg9kciy9YTN1k2Oz0D6uENuRh05Yioi1xGVoTzXqtkZKAAyce35uq5hsOeoJkttsujCsBJLjex16hbH_0baeYGlwr66DaVogU3UEtHJH56gikSRNNRLLh9RZaoLOcHvq4Ayv5GX257Zm66ZXIxm8vMqior50pD1EJiipZStXmLSoFAk4QSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=HWcTTavVv7CVCmtu2GWoG9QQ-GS46yymmV5WuKWszPgs_JeXt0YFze3vomShOeRD00Tf2O9Aa-vKEdxurpMpYVVGcxWdrYeobVVC8RocBmnmW72UglHzYw4oAXMfm41mfQf296QFN50_OJxgMXUv96OBt92I0t5OeiIg9kciy9YTN1k2Oz0D6uENuRh05Yioi1xGVoTzXqtkZKAAyce35uq5hsOeoJkttsujCsBJLjex16hbH_0baeYGlwr66DaVogU3UEtHJH56gikSRNNRLLh9RZaoLOcHvq4Ayv5GX257Zm66ZXIxm8vMqior50pD1EJiipZStXmLSoFAk4QSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSPrPMvZcTUdqQ8zSJFDbjWdsL6JH-9ozNABPW6eUhPgC75qrbhxKeSGR9QJut54h64I-X0YfOycVcAks2NrO1-5yEerN0mpMWXmff9C4Pr7yiPm1QSKy1TpccMRXJwVSFqUIM6RYVK8jJfo54iBTvIaU7oHZd6rdMI6OvRW92Mq7xjmA09yQZrkwrSG34uMoU21ceshszVJ_aT513g08bJ0GMQzTBsAJmHL0ApllopfEF_k2431yC5zqY7rcbtszRE7hR9txlSIARBTWKTbYVc_bfC_g5koIY0qJAWA115HibN3PlLDXib5axnuojkSIdp_iFFUwtKTKbAE_wcGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMkD95z4_MfvQ-454OhDjICWeMdOpvJsf8VhgkGrKxqpBHbX4Py9CfN4XppkBEAsgvuNWphfKK7KWHuKThHOJSn7GSWLXZUNEZc54CIJpCYZM1SvpSv-sG0ZAIfOE8lXbXEoDOjSSfBHL2jz8secNldvpRVhp0Qa6m9UPY-jqBfuboe0va_77x-TmruVaT3O13a_pyq6cLC-pOqJ5Of-sZ4mZ8FrYQwALT505vPML9c8BT33QyTW52jh4jiZ-Yu8Zb0QRzow_PnnslGURTGBl4W1r6hypjtnqcJ_0oi1BQ0rCxnc6xkLEUEG2CIq9ZFX0ldVYDOgVh80bCopFrbiCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbmr1p1aLKufbRnGBFU_JK-7Wi2vCKdOOGuQj6usq2wqOZcinaL-duCyPPUPrDJxx1gT1yJHSe_uRbUDhqHGhtAArBYscRb884uYxuV0HENN4O5OExU_ra6SajrH3IbjqCh95rd4QNjkXCRLgANjDbytw6-Uyj1S2wTwLAmUho2V4lqzC9VvTm5zQ3Xk2R8cd4kmd0PGLL0SDx_IQAqkjvHfj7kqGuAALMvU-XoXU876ZaJRre34CjeWQyVZ5VXe7Yn_xOdWnX_LhOYjxg2Iqq4qe9lsP1YNOBgWJkpqchBgjRckO4u92SyHWS236Ae6w7gAKWW22XqhEyPNcTYQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfmO9HSVC22FVQV7xFjKNfX8Lz7x4pzW1U92NhKyyQe2klqKHq1ucRYZgyHpFaxyNkl7A42R454vZlSLVLPEA20uojHecz6dG4pKeKxKactyuxwEIIGmNQAhiP6Rd6jEOPTI4AMmHh7YSkWPPfeu23-GpBxdfwHhSylIrMEPpiPglKeOT8s_ger7VoARKDTWwpNfbyQ4X4tgX8r2NSSHxq1_VVNzKBPp9wHqTWPsj4FOTcsaRXoyHn0k9Oe6qK3Pm5FOGH4sw90R9JOPH7qJPz2dNFjxBdMJ1tRiMf5BjZvE4wSN4wSR2hVcGeLJZSqkgKAxp2tE71GI0d-eo1hKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPKKw34Gkx6Ul860oo22uXAqV6cFpT0P2x66Qze-jFmSBK43RpBsKjEassLdvvuK5wympVQCvOPWtdoGYcFgtJwz7QkA_-w1EDGSRKrB5E8oYSdJN37LPkjprnEoJiaPwPWQChhRRhCBK0clDPI3SQn6PIVG-cutVmzigDC8JGpjDefpcRUinWWOuc0OMtkzrdK7h6RH0Pk_a_bNbDi4AegqXPv6SyNMM1-eDAr35s31gKXCE9scSyFf0UEEXisoXJuAD4vfGGbmN4OzaObwaWIwCmBPd4gmc1LftaywT5m1zfCqAzfwrcvaaEK5Gmxz1wHABjTqHS-IUNBhcPPlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkZNgyFqIheZYplngWuUd6Q0s9Y4I2ciC_HdHD-N40hyPvmcgL3HRir0DN7VBfcsdsZdHhoJOnBYrU-NaCXsiyWmv0dL0ru6fxHZXRhLe0PsZRhdTHl29lEFlkh1Z5-uj3bJGjUgnrTzhE1hosYKdU6_8_7kL6UFZIi_ClAAF7ypTthTgoKvSuPMbIhtKx6Ax8_kc_UuwYXppp5Ord4BPLY0dEefNF8nK9MMQkWOuZErKZsA2IoK0aZtgMWSvWAhztL4Sq7UfcRYvXZxGAw77OAQDgYT77Lsurnbd8UpLbUzs-LqJArWGKexbuTgz3SO1vEyxKQtx3r3j7e5rNzXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=MLxmrSt6qmJlYhaN-3NGKfXGFhW8n9WWOnxrAco7kmrXWNBhmsKOr8FpfPrGfb0IgmfRrP-lwUumhiVlWcYQcTS-w9VqHVV0MF4aRu8A78JXnFajK6_gNR4SA0Q7jxLCXcwi-crkbjo5rAQ6v1uEn0Ob47vdjbnftrMawL1H8Ngwkcj-u9MNw53IoK3wkwFD_eeviF7zWHbyH6g-oUuq9rDI_gurhD_U26zDN8CJGBm53HpedlwURKl5oDnEhYyb9lEQOdy3ElsgsGFeEBqEgSeEJojQCxX8OW49CQp6Q0SF0Z7klv6v74MdvWxd3W8NdMIiCpWSlCvJ4CkAFzOkYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=MLxmrSt6qmJlYhaN-3NGKfXGFhW8n9WWOnxrAco7kmrXWNBhmsKOr8FpfPrGfb0IgmfRrP-lwUumhiVlWcYQcTS-w9VqHVV0MF4aRu8A78JXnFajK6_gNR4SA0Q7jxLCXcwi-crkbjo5rAQ6v1uEn0Ob47vdjbnftrMawL1H8Ngwkcj-u9MNw53IoK3wkwFD_eeviF7zWHbyH6g-oUuq9rDI_gurhD_U26zDN8CJGBm53HpedlwURKl5oDnEhYyb9lEQOdy3ElsgsGFeEBqEgSeEJojQCxX8OW49CQp6Q0SF0Z7klv6v74MdvWxd3W8NdMIiCpWSlCvJ4CkAFzOkYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DRpXE0j5P1SD9fu701NeOKvX1flam4rWfCIql_85Wztb7kHHuHV7P60ipruQ94Xpi0ZuZ91FT9vBkox5nb6qHHt-YDdln3MVM6sz0tvtvUX-btmAbOgHlFDtBTC5jI-eklVpBdNAx2F-49451OT3lSh8pqo_qpPNZX_nEs13rOHI-lnWTewoMJCzXrHrnhwxYkXCPGOKH8CiiM_-qEuFmOiDNqRxZS9GPv_iX2Q2rFuw9iLmFHzBkR2nhaiRR1wPq4fLiQpg4UbVFiGPiVp2LJ3ZfbWroyUnnWAF1D7wqQr6VtwVUYhnSE1X_Q_GJVhTugIwfvZsldXLDmyhhSRdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=DRpXE0j5P1SD9fu701NeOKvX1flam4rWfCIql_85Wztb7kHHuHV7P60ipruQ94Xpi0ZuZ91FT9vBkox5nb6qHHt-YDdln3MVM6sz0tvtvUX-btmAbOgHlFDtBTC5jI-eklVpBdNAx2F-49451OT3lSh8pqo_qpPNZX_nEs13rOHI-lnWTewoMJCzXrHrnhwxYkXCPGOKH8CiiM_-qEuFmOiDNqRxZS9GPv_iX2Q2rFuw9iLmFHzBkR2nhaiRR1wPq4fLiQpg4UbVFiGPiVp2LJ3ZfbWroyUnnWAF1D7wqQr6VtwVUYhnSE1X_Q_GJVhTugIwfvZsldXLDmyhhSRdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=JcCsfZiHy18eqUE7g_Bag5VgpsyyjMwHQkKWJcYBUsyg84TtNdDUsOZAf3Ah0qAEt2CUZYfOVrp8zRg_YIfUUrqbUofyQkYsBvF1KY6qUVvXlgPGlH7-g2fDqM3xpkqkPdjPd4uQiZvRYE72UdSqV6zVA5oBWJGpM78y9tzWrRKVhNp2jNf8nksGNMbj_07ldVJQxxh1p_Ipra1USjcFsAl3lFJ6pX5XEy3fR06O2CKlm8V_1WbHXfydygx14vlmufXZBqHqlLUpri5n4ziTEWogHe3lOORWLAej2FeCAkENlpPOPyepNULqfLlo5sFgO68ZHCnep7tf3UCuGI5alA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=JcCsfZiHy18eqUE7g_Bag5VgpsyyjMwHQkKWJcYBUsyg84TtNdDUsOZAf3Ah0qAEt2CUZYfOVrp8zRg_YIfUUrqbUofyQkYsBvF1KY6qUVvXlgPGlH7-g2fDqM3xpkqkPdjPd4uQiZvRYE72UdSqV6zVA5oBWJGpM78y9tzWrRKVhNp2jNf8nksGNMbj_07ldVJQxxh1p_Ipra1USjcFsAl3lFJ6pX5XEy3fR06O2CKlm8V_1WbHXfydygx14vlmufXZBqHqlLUpri5n4ziTEWogHe3lOORWLAej2FeCAkENlpPOPyepNULqfLlo5sFgO68ZHCnep7tf3UCuGI5alA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_n2_Obdu1GJNC5LPSKpLgQ0E5cRhbKoWT9T97PnR4uzGqL8sbzCe9H1BVdMcwaljqltWt07LxBZbPdZCz8vSamJJdBNm4xlwAFItyN9HE6I779ih58KCwV46Byxsunb3cTqVyIXQ0ug3XpT7ZxiSMBpJ-lujlOcuJI3fzTt7CIwD5paQoisT6KJyf1iBHq9BbQ3xRhfbe3cEtGkKmx1EZicfUobtJh3ocVZP2eA1y0GdiOMC2t5rg1pT4r8Lr-DY1m4pctBPZ46e-2nJaRzRtVkpv1q7oKw-Dbb_64MWObU4mJfv8xg06bwSjpHHVRUzIz7sZlHgho7G9sZ3Ae5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=ec9U8WYShovI49kscrXnQ8_eJ3LQmRfYmrvTQ2tcNktDRyI-tHMX9ESoHkdT9s84XfrL8qn5aX8YK_ywbHFYshCQ7XwRC7EfmKRF4yUDsWAeQZZeWIz9u5VxnaFuXloZNVu78u-glw_2D1BOxvg8zkQPzAQL8X0om8bk3m-ses7NNuNtHVkhE35P_JSP3WML1lThOEWQBBKKOnVTXF5HVBlCHA6e9e1MynSJ8YcP_ONzN7puqhFBJalfbhX-tc8flnbLyiv1gvMLsAJ3YenuoTNov9ScwDPEZjn8s6HAxVKN4mjLieWgr9spSJ2Olcy1XinlU5eC9YQtSff1WCDVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=ec9U8WYShovI49kscrXnQ8_eJ3LQmRfYmrvTQ2tcNktDRyI-tHMX9ESoHkdT9s84XfrL8qn5aX8YK_ywbHFYshCQ7XwRC7EfmKRF4yUDsWAeQZZeWIz9u5VxnaFuXloZNVu78u-glw_2D1BOxvg8zkQPzAQL8X0om8bk3m-ses7NNuNtHVkhE35P_JSP3WML1lThOEWQBBKKOnVTXF5HVBlCHA6e9e1MynSJ8YcP_ONzN7puqhFBJalfbhX-tc8flnbLyiv1gvMLsAJ3YenuoTNov9ScwDPEZjn8s6HAxVKN4mjLieWgr9spSJ2Olcy1XinlU5eC9YQtSff1WCDVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=fw2L8ldbg0FVP42xnnZsFejEPPh7qZ82PlLvxM7ywB2FP2MKsYD5XL6O5F1KiC6r2QIz01hD9C1F1rS-pA0828Pa8FXAcuItES5tRd08vSU4EECe-c0453yBeg37-DtGKhiby82k70O6KHDi26zP732JrJhdf0Mgxb1A2iQoVQd-3JU7G18qt_POdjeCaAZSJ4ZxsIryJisRXchCmlk0E-2FHd2omi1zLjoNAIS623bFL8Z1FFJ6YljvN6Cx-7myugSzs6mHWFW8MT8Pf3TBg8JCHvhcFag53YczkI9pXNL23Xbm_orErKv2eV8dLFcZEE3fvKajKzKbUht_cDiCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=fw2L8ldbg0FVP42xnnZsFejEPPh7qZ82PlLvxM7ywB2FP2MKsYD5XL6O5F1KiC6r2QIz01hD9C1F1rS-pA0828Pa8FXAcuItES5tRd08vSU4EECe-c0453yBeg37-DtGKhiby82k70O6KHDi26zP732JrJhdf0Mgxb1A2iQoVQd-3JU7G18qt_POdjeCaAZSJ4ZxsIryJisRXchCmlk0E-2FHd2omi1zLjoNAIS623bFL8Z1FFJ6YljvN6Cx-7myugSzs6mHWFW8MT8Pf3TBg8JCHvhcFag53YczkI9pXNL23Xbm_orErKv2eV8dLFcZEE3fvKajKzKbUht_cDiCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=SSdbL3m_yas-32nGlVXsEaZBCSHXmB94Uzb_PjDQ5a4d75ngA2uvyr609xn6ZG-0woNGpaGxO9cE8XP3Q7sOyPUvrl4gL7EaRR3DxDmPppL4aY9anseIFTP7GjEmBtUPC3mAKetu2qREY0TRQCuKeWNcSGF0KeJ75WiIpu3etaVxeZMHRlKMRLz9bF_XfD7qrBxb0LvlA8Tpa2qLXHtyBLuG22YQN4-Hwcsjvs8FLzjevK-qn34qIsPpS6n_1RmavpTlnBQPkdkL0H3ARcraVq6Ygel1MLYu7_FkOP7fINHI4YrxfQiELbaiBu2N0Wtd3Y8jlZaoLgoVzi2yOH8M3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=SSdbL3m_yas-32nGlVXsEaZBCSHXmB94Uzb_PjDQ5a4d75ngA2uvyr609xn6ZG-0woNGpaGxO9cE8XP3Q7sOyPUvrl4gL7EaRR3DxDmPppL4aY9anseIFTP7GjEmBtUPC3mAKetu2qREY0TRQCuKeWNcSGF0KeJ75WiIpu3etaVxeZMHRlKMRLz9bF_XfD7qrBxb0LvlA8Tpa2qLXHtyBLuG22YQN4-Hwcsjvs8FLzjevK-qn34qIsPpS6n_1RmavpTlnBQPkdkL0H3ARcraVq6Ygel1MLYu7_FkOP7fINHI4YrxfQiELbaiBu2N0Wtd3Y8jlZaoLgoVzi2yOH8M3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=jtFGhrKHHjc4mZdwMbiJGXyQb68QOHbek6Cry_3DZ9ut6bvUAkdks459T1cL2XqY9oT0Oi7enmNhwXrPcRc8jLaukiSgwHnjiuBroMV9bg9vHkeQxh2ACdJC0As5OAAxmk5mPqzFMR3tQmBJohV1aZBBamqodxDaD-FEzB7JOvqb33ZAPkue_PilY5Lv8mBmQU-FftgNSc_r_KNzuz6aQInb66pz6Sq54xEQjLFcGYTvflUCU0IdNvvYVHC9dhbH5OHPr6_NMbDBHXMtvW5tM41IDt3mjh2gE0wkOq142LgL3q7SiIifz9V4UhLh-hkolgI4hgShnj_ws9iR1odbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=jtFGhrKHHjc4mZdwMbiJGXyQb68QOHbek6Cry_3DZ9ut6bvUAkdks459T1cL2XqY9oT0Oi7enmNhwXrPcRc8jLaukiSgwHnjiuBroMV9bg9vHkeQxh2ACdJC0As5OAAxmk5mPqzFMR3tQmBJohV1aZBBamqodxDaD-FEzB7JOvqb33ZAPkue_PilY5Lv8mBmQU-FftgNSc_r_KNzuz6aQInb66pz6Sq54xEQjLFcGYTvflUCU0IdNvvYVHC9dhbH5OHPr6_NMbDBHXMtvW5tM41IDt3mjh2gE0wkOq142LgL3q7SiIifz9V4UhLh-hkolgI4hgShnj_ws9iR1odbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3dFoevCw-Jz6l2WVAEoQjvVgFbikt2NldBrTStTciCd5XyyrzE-VoXYG6s28IcGfcynML_Gcv-Dp2Bp5Hrys9gnydTw8R6yV0VzfouKSNvIm5TGhoVr7rA2UbUMu9piOZ-yZlZv0ePZ5U4GjLeaR2KpsKNbyz39k2zRqwkN1Dg49NgxlYMCKWgV0-k_2GX4_Ox5jzKZ279CiSTuRIofSRlm4PdtnXng4eT2ebsntcRoxb9eFOuin2yvaOLFz2FdpQMv8zAY_5Xf15SKrnQbKMXfktpPqWvgvlFER-o99c_c8zM_4qkqleWAxKrhir7RXuJRNu6MTw-4PUPQ5BlH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H9s3KiVwA1OJxotjrO-whur0x3zuICydYDtJtF1xgWB-SSANCc6tmV4KLPU_ZL6MocKDgoYoEspQO1Y1P0CAGtSSJ3ayU4xzjaz6EGD7roi378X1ch4K5vZI7SXV_5G_4CJtkCKnRzDI7NJqF2adRjAIE8FBzUrMdKP4gwgqsCEQ-Nv-VBffXOLIOc3f9YY04D5VFov3aEzXarJjLWkW6k6t4aQRhkLEOFMmu2CAfzH-jzAC9sfFmhGIgrHQQbR9WzsUsfeQQ2DlwXOnZM1T5R-QHZ1urhU-vE5qosb3hMxCDyqAjvVmVAm1vj6s9RoSMfKhIUBNqGO7p6GBHRXiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS4EgdyWWQVKNUQuzNRwViYoe_8XYPfBjJMZvAViwo3XvjYKAjNbxRBNCiFvJqAVKrL6gsdGdtnnOiGs3bJRz42xRYyjP-YohcSDCXzXfUmRGUTwwptqRZWIZVivm-OPViLftkNC0j2qjQY15rijXAMBwzn3_oczKucdMEckeobYD2vMxsBFK3oUTj-wkjTyByHTsejPS_XnYpsT3FKo0ZyfKiZWJLPxvukjFJwPMMidCJBoGgQr2HUZPcryUugWKxUiXK0UrI6QqQy7iRCOSzpJjUFOboBQ0aSp_oWlBQT1GT--9b4PSVZefTHiyvnE46tohawmy0csyRxX1ZyhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FF81qtoG2DLB-tVaKQJW5fY_ax8JuZjT1tDkN-m1CoGNB6HlpOxjCSl5W5rusFoehVM7kRoRl5SMq-JmYhm0bRTKlBsfbKGs0tADPCuTKAF5jy63VUZrlJ2JdKMiAGxW6HiA_EwBepRZvTMDH-N76H9KJ_QPz44_qP0-eYG6Ql3S2B6sMsawJYpVfNmEWnStO1dA43V0_DCAvLyE9Ci8o60x8wVrgYTAXOfYMJy2jFODwzgbYIK9fBAMv1l_gSGfQcU1d9ipst2viVTKGr8dwNbT5FcjS6DxLvnOC8hsSUnjsM5q8W9wugRt82_Ze8NoS5JVb8O3pCrSeRiSlsmSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyKfo8jRYsQgKxaaGwEuz_AkQ21BYdad7FI2CNgkd7alGOgiQEtrnXLjlx2NZbIn-rB-MDa4uRV7HXediITGCE0e08g19RpPaWQGdzaQNK-J-3F2NpBVaWLmtVVaILfaW9UhEuY8WsY5C1x1dioFKmIBwS4qhm73XxvYSqpggDREVM4DL5fUYuNolsO9N4XdoYNXh2jfKQYf3Qszw-bf2j2cLz8iXyQf6RV_x5LhNxx7DGNaKt7PqQBSrOGgFk8n_NVoezBc7iWLBfXo_P2BxiLA5imOi0IY0IjLrNofE7Tpwaa6MALfJdqf0S3cD_PhOCJoFV3bR9FiIjLSJzlDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m33pcDHu2xiVXJWOYpJZglOUJrFtm1aepfbsPghYIeRRGO_UW20P1ycX_5czNTKuyPQdXzR9E5pwqXUTPuJV7-ybXg4V4mFCwKqWnJz3MHnrU_DSe9jlE-_LlWpueZAKSYN1rwXg7Wc6pgUeYlhCYA8iUJJcCDuOP9jw8Xne5FXYTaJqJvO2SRxmEH-i73wnMfz3RDHyi1BTu99Fa1Ss3QstMTmQEbR1YzPBNpxNSyq1igAo33SaTrxtmWokdBYatHQoxv_l3jZNfEwCNUXoy7e7ojXitFeWlPu45N6OLRNYONkeJl-Cit5B9g02Sy4zRy3Ehjn25erCiJ8bDRq26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2vila6kirz9QovY_Hkbik1LjY956raoqAI49ls5Y8IbhzIXEjVWV3C1hF0Tnb8RAiy4Ab77yx4KjoSG50AgiFGtmZUfusPRvb6sAAagUbEIhJGuDcIK3kezZCPeBm7eq5CHylrbOH70SpXEFPYddNWMl4wNIxHUac39o4Il-IH7kxbKn_Co1suPM2mlN4Avp4CKcUx_inFYJhDeaKokr9BufpdZgn6qE_A5xYjpz4Gz6cpMJMXf3VS6aQ5sJrsrLpEmjtxueKM6V4ARnXMaJA10-F-gzvwpwRh80Ef7G20Zcer6JcCEVbu6b4f2yrTOlpmCyvEUsz7doMf6wylIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgOxnA7yYafQc775BFF89EuACBzIUzG1kYvjhOoXfk2qenbaUrcgqHWOsWhNiQKkApWp20KE417MinsVVJVmbD4lk6c_CDsdIk4oogLcnx_pW5HMJUPzaqZNibqkIt6pXsrwu6ssTJRiCqjQnYH0h0IP9uQNzPyKM58CwDAcuHbEB-stZW1odREfIGbf8usbLeG-eBkKHbu7R8lUQ_T0Q6kc66b2sI2SsLHwhLtLCPfMt4AaBuXil-Onm8lyq9_3xsaSws1MRwtYhjqXCLc1TEtUwkXpO0Z3_Z_jQjTE7BwV0Jwz_99YYlIwyRCxFvkai550g3baDSXWWB-6a3_jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzU5hE2K_bm7diMsDilVt8vr_b8VyBN4q4C5oEM0wsFUxsydjo3U1fUxcbiO7kfBYU6VD9AQrkaAKUKstqyFRLug7flkX-awmQy00zS9-NsiJitDbz2uA8ZMNWhi-wqxvepTA0Z17-FP-trefuYVmj4qq0w4Aov_s5ma4wot_AAyJ8N-rOKc0PDNhMUGkmxOq3NDFEEJhb2ypanNgMhPaTxKK5jIYPt7q2DZz80JHf6Tkyu6Vq3mdJ9LOJyAFLqRwa-kEN_sUjzGK-5GBb0jeXazitDW1OWVA_c5sK4GY_93k602WbDn0JfyKHCu7NZqKemyX2Wf657klpJaxxKuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=S0D7-2jyvV-4cVWN6mR0MOTBDLS_LPZWtvZexe8ILMm-OsZlZYZWWveI4koTaUz__VYZXnIKKyj-7mKAZ8PllSO9QIz9ezuMDImMOCoZTs7hQFJaQhGUm1YjS8tMyF-G8kWTkl0kSvkWUHP0zmTSHUJeq702KE9jO_egWEVNOj-xGauPkSdV0IM_pr97mQgCSkZ1FtErRP8kcXQGu-PWTfUfOuIVEW1l3W1b8debYSga6XBdpw6OlnUaNZlD_YTKUQbM-I6oYkkqyWEReEhAGnDGIzEmD9u3YCIdIzY_4iuyjaxIi5hsJ7Ckj8j1O8XyZ77zc1Tdm47K5eplcZwPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=S0D7-2jyvV-4cVWN6mR0MOTBDLS_LPZWtvZexe8ILMm-OsZlZYZWWveI4koTaUz__VYZXnIKKyj-7mKAZ8PllSO9QIz9ezuMDImMOCoZTs7hQFJaQhGUm1YjS8tMyF-G8kWTkl0kSvkWUHP0zmTSHUJeq702KE9jO_egWEVNOj-xGauPkSdV0IM_pr97mQgCSkZ1FtErRP8kcXQGu-PWTfUfOuIVEW1l3W1b8debYSga6XBdpw6OlnUaNZlD_YTKUQbM-I6oYkkqyWEReEhAGnDGIzEmD9u3YCIdIzY_4iuyjaxIi5hsJ7Ckj8j1O8XyZ77zc1Tdm47K5eplcZwPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICEcgKwCwZP3QtehFUgDt16z3mMRuT3EfCionY3UsajRl_WkJrk2hpywxeelKLQO7ge4PeB0KPowyejRflMIaxlK5aoVLu5MvYtEoL7UURPxHwV3dZCMJ1QYyB7xRCpdOLNt7aMbjyktaNBcwztCQsQpmO15n6QAzgUZpw3vIOOEkLqVPxPmxNzLxT9Mjwzo0--amh2UaFAwe5m9LcPMy_3gP_cCQmL3tzlyjGmBSjZXEU2GNrniIseUyLY6kjevztn_c10dKembk0ZrnbS3Dcx6AoGscJDxKQiaqQr8V9CP5PgPGCs_8w15jNsRJzyjxmopLI-WRiocyTtiEAxJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtROa9wBTkmRnpu7RydC7HvZ_wjN7o1Z8xyR_RAgFJ18VfhSVv6sXJXeIFD50DPkdS316vz02atqw2wFznlRDU8I39gakqGXYMPhQ7v1QorvooGGk3iGUAObHuXjCt9NmBQfsQTYL1ymyW-ey7GgOGFm7WNsyFpvGAnNXwRtAYUwgxKLffeX4Gqx4pWV4gRRDNt8mAfTQwyPnHfURqw_LkokTamWT9UOtyqET_5Fp_xIBvbtfnFszgpUa2NzFBYRkPPqqTMA3VNh9ok_tjLPoKA1plaElqmE41k9wh0uWWHW54vB_rwKXy62qu5PHuaLhjG8QTStY8fALIjSIwUhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obcfPMTcq0CAgx9NWZegFMc1LBSvT12Q0BvV0p6mejwRv1uqq3NQa9fqHCrPmBJQ1ggdsXb1_aPlOe4_eXX1Uu6TmYCeHi1X9V8T1ZVauhe-aVC2Xqf8JyP4UP8sbv1otPyfBO43W0zDQT2PhDdvB80lJJF2IzUPTJ1gMrHkJ3n6QNKVZZptWaJi3B3qYgpdjJVPgpeRQsy38ZTIUm3hwLNmVRVGxJxtpXT18kw3o-RH7uF05AfOlMrwRbxehiOsw2VzmVfXTXFxpH8NLgM95DQkxdzujDfxHx3JcvmYUjdt8Cm5j9ljIy5QUXG7v6pdEwun4XMKvKXoBbSY52r8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6lfgqnkH9OQRx_Z7i23IROCqLu84u4n5j74Xofdqq9o7HYDLHx0GxflCRZ_FQawVECNi15mjMu6wBbfS37kj_HU6vb5rpiRhx47FSP1Lx4dERxEhhgvT81aR2yRvAKJZF4T6ODMmkAuw_D9ffFYPhb42aUQ8rAbcEPZS5QlRHEOMRZGTgol5Pe-Z3k3uwNZh2zbdYLdfQR-Sw2gmT-9VK-ECXAiAs6_dALrt4S1xWV4wVb1fwKTH8RrkIU9oW_Czsmuo_HFOwwS0rheKeXWYnXGqylFdetVtuAjwLvYAZN9I0RR_Bk6av4OilxodqJNfhAJi07ylJNHa5gl-Xs0lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=Y_LRyqB3XPwJmVJ-RUSPXcEAq_KTA8TWj_m0455K_7ASn_U1LaoGHixPyAQr13zeywSP3yDhBxVzMASk42w8JFLvOCpV4584sSiF81AI2Q5xwoBLvhHKEr0eY83SamzHA-vUpuRAvKe6Yc0pMSML8CwkDno4NlXqS_YzvWJABBG3XEXTjXEHkD2oEbL2RassKQuhDHn5UrOE7d5t5L71tTF2h1plSCYgb7BTVvjpNzHkBeMzxlsUfEanPbfE9Vvvahpgv285tZxuPJwCeYj6mlHW58oFst2b3FqceHPVugPwztqrX08zSz_XM-MKBD2e6K31dynMBU4LMvK5x-6umw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=Y_LRyqB3XPwJmVJ-RUSPXcEAq_KTA8TWj_m0455K_7ASn_U1LaoGHixPyAQr13zeywSP3yDhBxVzMASk42w8JFLvOCpV4584sSiF81AI2Q5xwoBLvhHKEr0eY83SamzHA-vUpuRAvKe6Yc0pMSML8CwkDno4NlXqS_YzvWJABBG3XEXTjXEHkD2oEbL2RassKQuhDHn5UrOE7d5t5L71tTF2h1plSCYgb7BTVvjpNzHkBeMzxlsUfEanPbfE9Vvvahpgv285tZxuPJwCeYj6mlHW58oFst2b3FqceHPVugPwztqrX08zSz_XM-MKBD2e6K31dynMBU4LMvK5x-6umw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW2cNsWQUz7PUU9JBj9H_jvisc941n3VAwmxDA_tbc6KuL2MBjmhMApvtcHKxYOFe-aFrr1Hz-DRr9vdAvuZ9XsuFWqMyWaSYOBMOQMhWl4L_ncbhHoNGROfDEaPOmwwGShPHJoQjc85g79x6_zPsXOTgD5uKM224IhpOEbcZmKQ0fsTbC41AvC3rmvd69jdSk-mEFqWBzxw4FpE4Hq87jjb1ww0p0IK6HQmnj3viHW3gtR6t-6kJuhG2hH_003NDokF0zfBjm4JFr1q1V7Mhy9158jwTb-EnQuiW24YVOxHAksELE0qiXtuwfnIf4wEIlmLR-1NiydMmoOHTvP78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
