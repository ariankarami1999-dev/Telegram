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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg4vBLwJ5e6BSn_QnbOQVUXyyvFSzsuEde9fMWhVvishV0AE7fSUpY0NGBBLH__uXVfKDSvQJ5rnYoQlZk-w0r2euyFNucx4fqdQ4l3hlvbpHnyOP05yG9cOvYOtI4u5F8JAFWvOeTRAXL8A1iSDE9zSJF43riJaAhRYO0WlQ3VRdH9irULGin_teD9SofD47iQWPiT9dtdhK6QAGiZ4jZRijEsc7vA-lS7qCLG4xOJEBiwV_yuL-WCKgBSNTs9DA45kIsjBcaOTyEx2AlRMsNuMGOope6xCE6KXPLuici7QpN1ynQyjEdFmuaXI6UYnCeHS7nx0XVBfzXMu_NuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ99USyvGhOYA53cANt1qJDNkOFRmNL2Ot-xEQiFVlnzuUXeSZvH5MJlOwU2-zTZFvUgldlznWJ2nbMldCizAzvuOuucaLVe8RBc5KmOOHi34jdK1vXKiWu27pdLeQ-LLeN6lEp2irA6IMQZ4utzqT7DvV8G1jXMTaM8pWbTGLbjs8eV_-NbeE7KP-wKwGac0aZC2eDXiSKyDgQBKPsyjrwWEVdqpUMNlQw0uDNEUlKPa1w_r3oThUmsxFtShR2qX06WynxsHSS9He8ubtPitcjAutPtE7hDiByeEzTYwupH7jUVcxJrN9Fz3dXU_0Kui0KMwK7Nf6z7lIFU8Tf3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nApOFO_sYBbSFk_Pva2Q4q7gwvAAYI9OyV0x3qbYPJqgT8Ps6wT1lNSTQYg45fCXUSCz21s6MTYF80hPHEaA5f8vEMRUdqhwngRynlP8N0l9mn9UqI1jrdwsTG9zafDbQXhzhtEzaWTyoqfxJgjrNvwCr0MeV3kBXf89BJXjX8K76v0UOvONPOfGi-kdmKBKn_05jhuRU26p3zh_pxEoA8TM1hLQCPYzltZezoPrqoIyxNPgSgbWPNlSogriC7JoRXodoFi0bq4i3GUSlgsj-2DHMyicKlQE7dcsIpWUR6RFPwTVTMo4_WdgKRBwZQcuHy2lYZVuynQg5B2qPJhcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3fGNcp_ivrtnTPGV2mH9qSVIhLCb6xho4xLDmmYju3O3lDBIc0-9KyJd5nejcwfpNg4uDksrpbAGAnV2zEr1mjcT-esXOO_3LMlSzfHEltrsPB2KpXWDWRmGGWK00P3RVuaTrBDRW10fBBakJyJI9jtbJeKBv6dxtk_UWxV8finwRlvwActZUSD_22uD5P9B8W4U_dGUDB-PGm_gJ3yOZKxb1LJdX647lNRMIoE3GW_J9GH8hflf2sNK3MgylsWZ_-F1JispIfKKzjP3Z28q7Cn8NxVtQD37tEEp3c4ss1z3xBkfckSo1SQWCmJJyqVyIVasLt3PqY-hXQhVQW92g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcHflUBQBkS0ovX6xWDvoG59eNnbpxSEiV5916uIAHKkZSP0ScUjpDl4dv-5-N183t_5scp320xFPy_4p-GBCiDLbYBKSQZvFLLyy2A4413IUO_uPbfXPgsDOWJ8g0__6DOuA623ooAFofsJKkx6FWJ6Yv6Um7WadhnTEScprtsplRNA--E0UapT7ArhNuI1qzv11IpoynHtuLJQMwVC55YtQIwxPOd2sHM2LU6OZiiaVdgklbQPC5KOHOnXvImHEWP2qQ7COiGJI3Gt-JBh_vXkd1hPFPkh9zgKyvnqurvf_MRECvIP8MTJDqi0FRN0zpsPZa6cPSs-3zYuOpVCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=lS8WN7uLLy5b2oX43I-6YQupNzQ7smezXfUS4XzX7R4kFWH3UhWinaTHg_jhujxfGD737MPrFXqfgUjZUz5IxXEEm4rJw5rukVUx7TtD-I2WlIs1LxWRIJwwX7u9DnXLsyFt65HzFbYVkrjXOb36HO3tRYSZNT8NE_P8tDVwzBieypqFHifQfX_8rGpQGzG3kzYbcPA1oVK7_2XUPtYGHttNbGMb-pDghGcMbu9L0lvznlvP12j1ubDgnxYG6BQ9TpIEJdLn384Uqm3uLNQovJkmDTzgGvNytepa3peoKVxaOAdfBtA9LzltOlolUuOLNknyq07OnkiixGfSxBoxRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=lS8WN7uLLy5b2oX43I-6YQupNzQ7smezXfUS4XzX7R4kFWH3UhWinaTHg_jhujxfGD737MPrFXqfgUjZUz5IxXEEm4rJw5rukVUx7TtD-I2WlIs1LxWRIJwwX7u9DnXLsyFt65HzFbYVkrjXOb36HO3tRYSZNT8NE_P8tDVwzBieypqFHifQfX_8rGpQGzG3kzYbcPA1oVK7_2XUPtYGHttNbGMb-pDghGcMbu9L0lvznlvP12j1ubDgnxYG6BQ9TpIEJdLn384Uqm3uLNQovJkmDTzgGvNytepa3peoKVxaOAdfBtA9LzltOlolUuOLNknyq07OnkiixGfSxBoxRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9WDrmxR69nacbZj4X_MX7oY7FMjR8OMYScy3ULJoLavYphkfeW_qPLPe2C7GLsJqgwLuV3VOPh56QY2qH6HaPu3LvIYQkH8b3PADKchLinLOk_DkOTVJK0Jngq12fC1Asrqi8oNNi0dvOzD5jnINGIoS4ybz_e0Tl3ft1MIoRwKI2jux1rr3HIhEvuREB2S7CB7MsYiclWRpPwRRQDnZVOSwR4AGCzV37Nm1wCmQSirIPTtrvFnsybQ7e9Tcei90hwhbAIKYC8EZ9TPBeMYL0mp1r_LzjtVcvfLP-GIoT6MHrwfa9kHCA6-hakmrNJDCi5gYOwPs1Cln-1vjFs5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=vckIFbrN-P-ziZ7DaPS7wBRZ9ef4k9Ta5dudBWTfEM1clriSZQui1RsZalc5n6n_7CvbsJOY27gcM9j9Gb_X-fzuWMzeRoGuFGYuiS6DqzsH_7cfgDMXk7JQqjsKdzacg39bQAF4qm4YPo6mODs1kpqz1G5mjzhG-ELrph6Ol1tx6O0fXobNtvxcBME3tEjsFUmtFJYwGdKE8X1H-A84srqtLEzFArxuHyYUQY1Ys_aZbfe1S1GLMub3q08fl0BuMynXJQ0zehC66ma5OUDoLTUhTpaJ9Ih6g2e-m5u6ZXWMv4yxJPIfLEwPW7LLuyOeXubHfxNE_t0cg-aPVodbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=vckIFbrN-P-ziZ7DaPS7wBRZ9ef4k9Ta5dudBWTfEM1clriSZQui1RsZalc5n6n_7CvbsJOY27gcM9j9Gb_X-fzuWMzeRoGuFGYuiS6DqzsH_7cfgDMXk7JQqjsKdzacg39bQAF4qm4YPo6mODs1kpqz1G5mjzhG-ELrph6Ol1tx6O0fXobNtvxcBME3tEjsFUmtFJYwGdKE8X1H-A84srqtLEzFArxuHyYUQY1Ys_aZbfe1S1GLMub3q08fl0BuMynXJQ0zehC66ma5OUDoLTUhTpaJ9Ih6g2e-m5u6ZXWMv4yxJPIfLEwPW7LLuyOeXubHfxNE_t0cg-aPVodbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCLvKdbfZwUKDusPr7KabTaG7FCufB0HQAA1_PlEri4c6JmoiUJzN4i5756N8lAc5WfWsS1L27kTiL304mfa70cj08eqPyl2pAjCPL-jQPyl8Vbsb83UpDlrsEjsZJeTFtjr1bGG1KyoEo0ZkP9wYRQeqhxFYS6N_LYT0ECgbpqlHOf7vfd28pc9I1obh7jZCAOb6zYJPRRkMS9wmxsjC0ZE-IzgC5UN_WYhrsjIwBD70j1M7y6JFl0-9LCJ2rI4obf2Ly_iTp8iyDmjCMG2JBYkJm4rj_G4RAB1jaGpx4o_hHB9vmMwwKl7U3_IjR3b-7fKHRgfvLXdogcE7ic8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCIVQElwGvif36Gt-pe8Jl64JORjbVoZYiApau17GKRYkRtGfAdVM4gz4B9ScgOMOdbjghxjlBMm2awHVmLqK0AdMrYH46l_5X07-rnPIS62IuE9UfqFeL991AdbHh9FRQ_etU1t3oHidMQ952sGU9vEg-ow8iHyjYGO63FVG1NR3HxAHZKpV48gAVjUOGDtrhwWas3FtbkNOjEqfR5BsJDW4I6IP99txjmPixZ2SzTEZCbVEkz86gXLCiWljJuR60dzaWuRYJuQSAZAZKIXQ3giEQfeQDwaQnibZqAjQ-G-3SIHCwCK9ABsNbMxjY8eBYgoHPvKuTN2uKm-EsLJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geomUDSnfib7qmMPkfw3rjdHIPehTBWC49xC2bQJgx-RzlxE60AaMDBWvbF1C0pllWuTXPtzq1oArWmU1cIqK5xsarBBgDg1BaaMhlj2paRCuR7YN5TkcYlXz9vzqweoMbcZAwOvXHqMfhhY6I6-MvKZlY94eZbpy_OzeHjxejcCHCjvDaoZtkOcYw-aDKIsWSQcQqDejJaFO_P2pc38AgLjICKFeJM_pCgHz7Hnp12AfCRcSEw7j_1sF7vmDeauvtL8vuJa2bUMt5JdwQIgBsGxLxWDEfD7GqE-B5NlNYWbRst9Xs9pXA5jhNTZP-_kzA3HtJrBhyUXC9yrhxqKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=ICCK4YkFKFvc3GvMrwv8Prqp6LGNF-OXwyRbVE3DFCViT078xNI-iBVjEz2XUl9AB_QLQeAyqLA3zulQlgC0Wno2llEd2zuLVwFYzcJr-kJz8oJ9BBpTowzThpAbmbBoyHbfzlTanaQTxeXFFIab12NZifJ2yClkbkv6v09apeWAOpVfQ7LJnLoXMvUjUo46yywX94G4poq0sDAjSfKHBwcFru4ArgRhnOiZGzUBYzclYnwii1RKZt2Wc8gaiESpTHBaC7VsYc6zisr8OFg5Fn2dD5tdxUV8_p5MmJNwq9_vyJZl64dmtpM8xOrQNN-VkaiSqwwOiYNEca_4ZCwIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=ICCK4YkFKFvc3GvMrwv8Prqp6LGNF-OXwyRbVE3DFCViT078xNI-iBVjEz2XUl9AB_QLQeAyqLA3zulQlgC0Wno2llEd2zuLVwFYzcJr-kJz8oJ9BBpTowzThpAbmbBoyHbfzlTanaQTxeXFFIab12NZifJ2yClkbkv6v09apeWAOpVfQ7LJnLoXMvUjUo46yywX94G4poq0sDAjSfKHBwcFru4ArgRhnOiZGzUBYzclYnwii1RKZt2Wc8gaiESpTHBaC7VsYc6zisr8OFg5Fn2dD5tdxUV8_p5MmJNwq9_vyJZl64dmtpM8xOrQNN-VkaiSqwwOiYNEca_4ZCwIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=vneAbe73CtQ7l13AvGw3gYv0GgcZIUDEAIgazFn7a1cGYpqvjHaVyf0Zt7cPzzDtGGTzESE5UDKjOxQFqRgHyUdwFbCI7AYGHtyGkriY4vlAaGTn7lpl5yNlp__ER0XFJgufuiaiN2ODk65OVkywyYkNCm7joyhoX3-kJn0xiesIqiCRbssUiftChlQ_Wjdzo2upu8CNeJHzFHov7dHANrkzihmsclPxUN-_4T7g8pHT7XQ0DNOJN_mZyx3C8UOKA0MKYMXCvg5f4T2iEyeIqRPZ79avFOysHktxPlEalSp1wu9VI-4NXUCegWQcOP3iK0_CTPqWsRm96bhbcu09_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=vneAbe73CtQ7l13AvGw3gYv0GgcZIUDEAIgazFn7a1cGYpqvjHaVyf0Zt7cPzzDtGGTzESE5UDKjOxQFqRgHyUdwFbCI7AYGHtyGkriY4vlAaGTn7lpl5yNlp__ER0XFJgufuiaiN2ODk65OVkywyYkNCm7joyhoX3-kJn0xiesIqiCRbssUiftChlQ_Wjdzo2upu8CNeJHzFHov7dHANrkzihmsclPxUN-_4T7g8pHT7XQ0DNOJN_mZyx3C8UOKA0MKYMXCvg5f4T2iEyeIqRPZ79avFOysHktxPlEalSp1wu9VI-4NXUCegWQcOP3iK0_CTPqWsRm96bhbcu09_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gp85fnzjGROtjnCd5H51cXedhfreNjwYbeRje_Z_B27D9gGY6r0AQlnF1iwGsrD7_UZcrGOtgApb717qdv3Oy9bUL6zhxT-FnufEJtaCR__LAT_n_ZdMw1pbgOzQULXNqTPU2db-RmX1F5Iso25JaUUIItWlRnHl_O6Biu252BXpeN0hc5oFNn2Z0q-XF2TlZXsHRoZUdBjUFAAD3ec8U94KLi1YAnW_pl1vuvEsWIEDJE-eVkepOUa6_2Mn7S8ZrjJY6tT7dEeVIaMIp91jIjfAFfqWqwqwy2THQjzuNlEymh8dEIFIFWSHWpH9uirXMb1JNvfCfI5iteJBForR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aa4ctC0giJYgpezrdOGJ2Im9nttARK6av7D8rgze4lbK5AKqVOAOA6za1qSCwBmvSsplRviuiYnKL_NLGkyHCtuVmcXhCSSzCa-oW77Zq-YZAklpAEPPWNeU8Xw-eULIM9prgPvv8xwN_RNpIx_JW6-_DWFsbH3ZvJv1FD1Rj8DBMTgwnBeLboOA3KipbeCuQ2_a5Nx30fN9u_73K6WbMZW6obaUgNxUdMTIZ4FlNJbS9qaPrPyHOeIEeQ08Y_Or5eW7NCMZPmjoY4_B2J0H1F21Rkdso9ivovxhDe5vVTpeL4ITSetrY0YAvwcuxli6AnLKGc4UPzU7BnyzqG3YTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFpo1Buby7a2oEXUfBf9vejOx41qVVFFy_gv8JnVk_j7W_xGe4O0M2G2g-qA34adWdzZPVUO3X1NPddGKCThNOIM46EA7JNoS-GoNbcspINiZtGvpSOz9gTojdqMm9nXrPV0GOvqt0em2ZNROaFunaIn5vSTd0CjFd40aNw1mUf7P6PE2t5U2BhiiXjCloz8kYF74eWVSFZzg4g7BxcObI6bS_ER4Uvt0MKelWcCQTR_4Gaz6EgSGm_DVkT5q8Nh9Tyn21S-sgR0w138UOetqnpO8D0IaSPFfNa0MpkcUOW9a525ZhIzp90OgEUAFbSvWqaI22f-8zOv_P6oOdG7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7FeO7KMhppBB2wfqEsW1IN_NOqd3dTDYmQbWRkYd9Ykd5mvz7lqSk8S7aqN4zwZfFQPSweEnT1Cymlm-IKsuOMwLwEAvIVNOHJKBv1gWMuCbptVicfgM2EkSnAKYaaaftHH6PFAHPzBTf2nDVoPttunlI-DZTWbGiVYgO0N6k_tH0ggWsDugGn-D8JsDm-Cgh4aiYwpwDYr8FGGhTxFvzBY-PuY-mRUBICNiuegiVqooj_EOzmBPS4vW2Uj7HQ8lP15hz_u3N1Z9OV44NJAZ2pWbDkHFnos32VLgN_tKCO7Z2v9UsO7y8AbNTOwnZIp2h_66LH1WY2bD16J5ZvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdfb166IZZrRQET8ihoblW-Zz22bWLxco-R6fgEHY5wXsszJ281XxzNUbVf07QhUisRsA59BXUAnh20s3L--RrVDaxsu-ksSWFaZLARlXpoxaITlPavHHNxPRgLKnGI5T6ZKKkbwGf35oTzQHCpq1CB36LOcbwkrfjgTWw3Ow0hGoOg3PbIZH6nDSCSF16YHvCxtLHRQ5tNtvt6_Arb1tN4cV9qlYIwGSHXCBSGMKSysDunYkXcfi60g2fa1Ml875vlPy9f-Oc9hhr-uhxIhTyNkr_eZpg4CpC0A3EhLh3iFH4opxUfNtkifxyYqQ6Y30vR0vZLwmnVsQBcDAbqv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boZ6uFV8INrqZVFjW2xAYSuUed2dSGEnhH19YjBxGd_6QKQ677vmWzapDl82HKeVyrVB1x4cV1HfzYiqBzIMTeXhUpDw7L4YD5Gq8rupdEYYU22q2HLVnzQT9qXvyV3hFVgJHc8bwHUATWXKUEx2CKg7az6eo1zdqzL2oouwMSHoUtuAG8vpogUhBU7i_7wsxR4Hr1jshcBjVNi-5I0IebsZSg7ZEHkD952Nt-yAo6eYgabxjtmb_F_9iskxspw_RMlV69BICpwojL7lTsqavp4F1EiSoK3CEGhHBX8z-dfnBAa7j82c18b9pSlk35j2SfcoowYbexsRVUKSPnmj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgY-kbRTkuYhnwGZgmxxCCfUjXEoLIEtIir2ECZ8SwOgMiQQATC2Udu-QNTySVIpQfRq6nNbcQtRPowBC3EXjFPM1dlxYW0BT8lUcL-6uwkurklIhVHtTnZLdhtqqFYzdmm9ioianyKck8pzZHKQ3iEtFLVhFQ3D22wujKcgLHbC2w3fiqbyMUXkEb63Xted86GgQahlSwqptHyqcX1z1dg6vuKreILvedOVucRzyYzQu0y64UraMDKvLAlbPehFUQCSydyn4QUrhtYLu3Sda24GCyGwBQeWuZlfGZYxiuPcE6beN1AUl8RByJGKzNUGpFb682ihkELTUy_yAPqtbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnK-jrlIbzgbZuybQv82VmmxzZiEV0_qfLmP8Yb0Na8kMNNkzj5tJvJtTIRhl__nsMtPxe2U9H4oPdDGgzZ1UzdggEcfWCnCyXqRz4EWgl-JeRdlbqazjQEJCpB3B2Dczi5Sc7ZkPAdPfI0rhqCzbhwbcUqalQzOr1kRn0XRaLLsMCQtf6lu-Sw3O7zLbjM0Ex3pzdYpJ26oJss8m78jC-mtOkFOzIEpv5Dwky1BymTjfPrZA0-FPvvWQukSXJBxcEZJ_CNRE-Uxh-g_8JcNMOvxEcx1a6ybyT58Rv6WoZscTu2ZiQuyooHpc5cxsIz8ezRhz-GHogQhxnm2HYSk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy4Ae5fCdtjH0GR8iW-pi_VD8T_DJ2jCW0xRvcXEWxHvu5th5YJCaemBRccr_rdLLwJ4S-Z05YyPMrsaQAhaftnBIikzx4wLezJ_LwrFpyeKWB-AuIoR50ADyegC6unuomJiGxh08vU9Bpqtk_eNxoYey12sAi__PVRU3HwWM-VkUJxt8aJUKVr1WMeCiZhOdEnJ5pYUh6IFR2PFFbMW9mUAWUCJqZOpsTfkgfuKwF2amNN83BjkiJjyBTBhYKigZQCzClwDqne8ZnHIfOoGFpIFx38arFFkLxURFNzUwZjVM8XuTFWJ5vblTdMsX2u8BKltDmOt0QnwRuvLPJtxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo8M_XVFzT7NNJfUsBD0yNDni6EMLPeXz0QRfV650yUq9JNOB56Q8i4PH-cpmMnLYFvkj67eY7eNuIRLzI2YeljI3aGkdurGCt8jWEknSK13Ka2mCUGha2HLtik92z_FdXnE_UotoZkCKMKey4U2WKpNATJ1N3OqcCbk5KxOUJeTZdgfqP6fcIiEiQrOy39-II7TUlxJy0JenY9_Qp28Qgz8UlI_EA4E7OXrBg9bdgeoUoaXE5UlXPe0tC2OKYAf3sV4pbhbA9cCxDL0FXgKnbqjBHlAQicCycBhJFHMzjex0y2e_8DKIy4ZMztXi6OBYa5FEadKJ79YSxlJ4n3iNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMnVf1hDV7EOw8hBpUleVHFmZbYGh77HpPxXTOIjLGSuBNxf_EqQINrmiRsWV9HGwzytAkg3hnV1xCIoEJAnqFHRw6sDQ_AnE_QgZtbB30XzifOXCqh-qvpIavSweUrGhvP-c0_mlmL_pyR399BQlOUzoU0oO602fZoTfM9dIGuWr3OUpRGIXkNd711X5DpSW_BtR-6t47_vIjfi97AYL7IIi2FbJ9dHhT1l_rAYzgyu_wLLJx_4sp37mp3DryTQ1V5ih1UPuBwfzucejMJnsdYjCb5LGTFjiuFSNQz5eu0nOIbw_risM5dMFx1YAXXeCQgetr7QTfJxvZq7XnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff4bh196aS6_648_wO-YbdzngmdVkG2CUs1jhgYdCpjxr3uSAyfqjwwT0NzuAEeF7fsbzjUqw6fsPT-szntjAH_v1dir2w8KTrD5tRiDJW5ZSFoqdUzl2xDyUCTbKy4OLUtyGISkdqqR1PV7UxuATnS1Kj5UcRlv_VF_BRg4vrcbG19eFCbH4viv8Ubp4ae7gws10m9uKsjCZRMMq0CbZSotGodblTkwW112CpB0eoLooP0-vPGBgAnoymybUghdIEsAD4fQAeU4LzpTrwv0gsQdeicN8NJx1JDJf2pERwE80qLJOBSc7lmhcBldThQNubndqvOvSRqUDKdF1ZDuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=eXQaMc25-EZM0CRpZ5FycEQa9IWRkc-0ZGVj2_cwGM-6rh_VIpdBBs3GEKt1jtzvbBFgV4wUbyzxbxRibVGL13P2CznmWeb7nW4Q-Ox_YrAWOjIF01iW9USzd-4Zn7usMEnpmyb71AlSsCt5R4aqgTGodnn3avVeDIaLJjMIe22qW46AjbtR3W5Ry2k-2bg7RzC8nNGuD-GbdDPftss4kbpsYxie1G2Cz-fjuykawMwpWdPA7C10RLbnOTs8wJ9jlvtmpqcyzFEE3bhLXskcutM_Giowv8-0eU9H_oLWrGlu0zk57-Ah1klkhvtWXsXCwbcwQwfnpKy6_z3CQr6G5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=eXQaMc25-EZM0CRpZ5FycEQa9IWRkc-0ZGVj2_cwGM-6rh_VIpdBBs3GEKt1jtzvbBFgV4wUbyzxbxRibVGL13P2CznmWeb7nW4Q-Ox_YrAWOjIF01iW9USzd-4Zn7usMEnpmyb71AlSsCt5R4aqgTGodnn3avVeDIaLJjMIe22qW46AjbtR3W5Ry2k-2bg7RzC8nNGuD-GbdDPftss4kbpsYxie1G2Cz-fjuykawMwpWdPA7C10RLbnOTs8wJ9jlvtmpqcyzFEE3bhLXskcutM_Giowv8-0eU9H_oLWrGlu0zk57-Ah1klkhvtWXsXCwbcwQwfnpKy6_z3CQr6G5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBBQSDOkgLB1H7pOYJ2EhYnCbHra5mos-mIpgvQBuL68Xvd6_69MNod2YJZXbxtuYM_ixywkqkDNDxlEV4JpfrrvFzrWMtEiVanJbdjHho7hp9B0cNd8UvbDs66juJOJ8qZ0a65bvGhh934YuevCqFg_QNNACXl9NljM0-pl9-kFXqJZcs-ZtZXnOnoqKjnnVvUvmktU8kgwfdIS10AERkeFSawaXmjEfP_QClJp4cYaGG7BolIxfDJhB3b--Mn9Yqfi1QP_G2orh1MnHIkC3kH6T6EGaR6A0TjvFWedyclMUjjgKnfVSiWKAjmJWRDCkJ8GyMDA1-eX0O33a2eY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad1YR_91Rbyag2YfSWUIAAMKjgwroaw4L5L7ghluLFcJeua7SBUsa6GjUZFKyAaV0fQoa6rqdpO0sS08xXK0X8pAZbHOnCJkajSo4rRRCn_tEdc-Ba4tZ__NDzqRvF1izZi7Q_V0ksgcJWRgaSr1KUAFNr125mq-fiLutNKxwxRnv2f5vgiRqWMlCLeEjT1jvaOfVn6bVUBU50qdLSiVjcqTtR4b_GsNnWdVjf4n8Wsb5Y8GpJvF1LWxOULBRJgNmSQ9GPJfXd562ifh8D7ChUelcs0yB3VjPctzG_TNB7K-6eFQnfj9ZYUDya-siyLT3qJoagStzqGusk0udY4bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc5zcuiReqPoyoaY3lYjl-6qtcTSPDYJn7nVx6fpBOJxDRf8R-evYb-2rB8GwLf81uJs1wNWVuM2kKRJ1rBPckk_Tb4BJMa49Owf6m8NDBVeyElEkrP4YreZ3npTYEOyCrMSTHI1Q3dR7OGfCkiFe1rFyMkDgOAKydaa_-dTCaI2fzCIOfV_Qc6SulWA1Zygys5CTvs_Z-q1GqVr1buBWzVrOhgkVkiQWzxCJvGe13FOna38RS9JGzkY7js5BeNMXrFASFDQn7EKSwLuiUGazKZsGpUQaGmZyd8BbTKE2DvMwTf9I351hV8HVtVgl89-h7eHXBVu4uApHbQ1XKuaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmnFIR_bQkyYZkmLqfVijCbpWm3UTJe9RDA-W9lcW-OhnKbavphUvxnPCrot_OyJd5rM_5fvPY3-Gh7Rscnk_6h_P0nfi3oudgJa6sh0UYdIzpiC7AbBQ8scd6b_zFHM0vMmb6X6CC9H1SEkCNTUGlQSVtUsjLsB1JStp50ZMwQ3220epAisvAjAn0k3tgGOWbMiytz16e65eUSa73iUKbpJDRrQPDlsFGCz5jym9HT9y-2ISF_KZZJ8o6311JWdr4Sa8RomMGtv3iXKba03bT-B9Wciae243gbYxtW3Lfsd5i84oHgHXIyilA72iNSt5F723ck9-l41BPuztbLOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCWbUZz_R8u0iAny-4CPqyWqJdWmlVKEHKPWR4pgoNSjrWL_8g0xiwBexQ-CKjAV7XSQda2oLUK6VvjvONteMfxRqhBIZkb5rU6wzy1DTxzAYhKfCZ9cGnOMgHKyGK_7UUY5sKztwG1ciXnLisq6Wo5Q-kJ2nYiDmgRdoVlD8_9QcbQdoxrkO-eUDPXc-rrazIgORZq4G6oH8h2yvyWF1ee7LaY8_sFeV3nHPcOHtFg-Ar4wagzMO2AmwfELyL1Q1hV7m_T-YIx25S_IlyhYAqr9EcFD3z8cDl2AvtJkWkhu6UXhK8khmvZtfBeuMRpUFYicKcdu7qmlazRF3LjW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6s2OxTMlZE8E39vPBYz6PhBxK5lBEVCY4g01CRIptUnGWo_Np85ncz_yLwbviV39eobuEjzDU9sKa8OLtbq3jpTjy4wAHenjgCYFCXVtdznoFXLKvW8FvYh0p6yCweRuQcv7K4C04BY8dHj6KXZo5aFIWCeQQ16OrU0n5ruWHu4Ekp5Zbri5b3W6M8q4ZEVKqmlKBHkHY0jueK-7Mgb8c-8Jug_K6evSgryy_4ujcYzbEYDMmYI9urf2H9PhRuyMvdsHa8zazmybHvAAKnl4JXAl0HJMeAFjo9GTSbfw_S9X4HPx41_JTbgyhVFALPvJL4eRYczuRFIvAP_Jgo_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdV0XKG_1etBuwYYj8dgZZ-xUPilW5P9WWsnOybHmsyfslHPVLAHlKhWNPmFlq93QCKNdFkopK0ts-av7j_T8pALAuStwG2j4qq6Tu0x3-8XCKuwwFYSn7Bu8212FZNX1myahXnxhGT6kqZRKWZ40faQLZhN4XG4epN-R0BWSehMjt7QxiZh0-jwwPQQsGTB0ewgxPNWMIjrLtyc0xOSz4TdCV-RHp5cXIzVIOgeDC7KFDi_IFc1Y-pZMKPiTO0TGxcoyEIZpgr0l1juBiSLmL0Ky9rI_i6S37ggsu2Tkv2K3zxzWEerR-AH8dJ-IT5KVIGtoHnx3qCu-shMYxJCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTtnImvJMd-6n7Evb5xhlmnZevINVnn7dVeQyEuwMUbSuaqNgSl-3wKIQ7PZ467E-EbDGuFq-sbY3i-CmXLzfZoQXdEixo9ub8IT9VU9X8K2ENNntpu-PseFGcHLPuxqTc5cEouUR_Wi3HbQfncS-2Imxiv1vM9LiOpgTdL3sbgSbmuT3a4Jo4iuFZ4DR37qewykdW9jBizDvumQCBd63QenPy3PyVkQ0OxgaB19LBNbqqIYp9DFTBWrucmv9Ea2srjKFblmJ2wcsCX3-W0bOu247lx1w_siWxu6rW_eD-7h7-eYiKc6ETK2ZAdHCewcnGbGl8uVI43ufuhjZwL73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEoZq0kj_4D9q4FUo5unDigc1WS3cMz1yLIXJ6A3naWTrpWKYAGdVcVB2GOKO-frXKUFCq51D4Mf4BPRszZh4ihxOcObwA5_S9W_Cy60CfHSUNuDURNV59C7JJGGSptfimYII8cUbBIAuiqpqGyU-NXwi6jTzpk3cTif2gAXH_BQxLJKuZsfatPMTR2gDXDecnhncK7qvr0Wtmn9WaKL9wkVuLis6_Ys75V_DuN9W0-_-2tlr9aUnmOXkDBAc_bw00wfYb6QXYeyoNmQFAmH9dZ7Vo-Ct1Cq8Ysmz4wQVzl09bncadgGx3Qdd7MebzVTwQdTOrCEXm2wawIxDuv8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuurfHa7UQwOKLBKtCEJg48uKVLm2Dx-2EIKxI1dpnuK9MzxKBWkkVLrzxs0ADg-JYemP5UvdfeETZphUgjR0kxzjKjTjAlK5kwx8dwZKJiDk9H61UgYUOjdHFKVEmoJ6XACeEBy9W1orUk7gQlus5srAR5C-UqVKy_ZQ_T18yxloHfxkso6l_DqPC7G8sOIxTw5nhxiZTs3iwrlyxrNJyhnxp2XUEXmDlu-jeiaoQoc57gv8AY161NqpRPKIljBPo8HpqM4e8u4WQ8hiBTlapDEGdRe8ohbxSpKWV5bhbd2p8tLtNouXc6HkexmlyKhO3wyl6ZbVl_i7keVqsKXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK-RTdjInVOeoDtvK9RMnzjW4XAO7DQmW1NMbuD_99aU28FhUWtxBXY0QbhrK9gMo8bpmeKze6Ic5XiaUeYB-VKed72bHXC867SaHR_1Bu3n3EXJ-m94Lb0x28Ix3jVLATMAu-WE062U0aLkQEnYJ5nn21wJaYBot1G-3U9lA4NsCIeBxDI8Ju1XiRV4FGFTMyH-faoTtSyL2fPoi24SSBMRDlh2SEIhiAzF4wFxkBXv3Vgcggjc74_TVAAi7pp01jbTXYCbg9MUhA1dqkYx0XkCA-sHAxoB-MarRoj8OcUXdxkqzrw0GMCqeKArE5Y6ZJXEB0JLPDKd3mqWRRF2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAh7unE6AtwOzXxr_uNUYke_cAeKmjsCPZiP3Tm_WhCVqPN7nP1wppFD_aqQW606xitvJ_NdvLso8d9SBy_XMXEw0X9Rcr2BSqHmc1qGp938hr4G99rRWfZk0WXrMdMcR-pUtHeEc6n_FIpqxqDyAl1u4_ZQJqqwDENMhHNr2kWDt6b1oXMHUacOq0Lx9TaAUrSiasENrV_-Nfw2p3AR2bwtjUhQUrtmalDsJc1hhwWhJ0TRU_vTexSiGMz-u051d8GQ9E84SSxBzyet9mUCjd7MaSnIX9CecoYHwlZ1kKAXPtFWQWxUFdA2C3KmjyeG0iVaL0p8m2cwJxkm_3odDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikU1HCUL9NdbIj48lEQLhTP9hOUVB7n4XyoykrN7vusMrFAcRKVUN5X6Wb9m-abNzZEemU1DQPPzt8_pOe1rGjwmXHp6_rMcqf4nImFxgPQQru7hoG6ojiyvNis_6zYadHrmkCRIgtpEsYK9mwdtIKIP0IVtTkoY1NIbYU8zs5qJOt93cHeh6pKxqCnF-nfp0VBkbaNvnwNDtQcjr4S7mu3m3QriDYX4SHL7NKrWRR7EbbhSojbu3kaJ9f_kNiA8IpiuBRzfnzji6r36O2RpFTH4GN1HfviQiT90Uj6tTJAqfqrRPt43JcaIERAHEOCaaBLvIf3XvyBuDWGJG0_Hbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI0ceau6TzA5AhhLc4B21uZ8iHCY_Pl0Cg3vy9yln8j-0syQwveq2d5Vul-ICpQ4JFod26USHUf08bUysA5W0_YRAZETPM7Elmx-f4Bx5_3dWpUp19KodvZ-p7x6KC-qBl0j-oQf_ASVEvZ3fSZwjq0tYNmTn8e1_-NGF030Jy4giHbh6nvBMCr7sZn_Ujj81-5gFhS7BO21u_0GkIQQdKzJEqTlMuJducG_XD0ij2dWmX5aqKoLmQ0DronZiioShnDy3JOzNh2k-jXUVyJFzvKhEtWWJTJmKl0c0MFOVDTDJchP5f6u9-bR2-ZCDtBTPeh6veVAlDALgnGJYOG2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNoZoTdawhVPCDPOZlPPN4Ur1l2MNFJ0y-MeiEiN-o7mnjPDPxgAVSkygwJgfpEqdOTINdogrwfyBaCjRMQJMqG24alxV3GehoZVQDeYVa3v3TbR2BAlW02UmWUfRKqpBm7NOQbxHiXD7NbbMKIQ578VANYGAh8IB70qqK8W6fYFFd_HVftsWem9vtF4aSQq-RDqP2WMhSFwDFPXK01dg7tb_gJOgD2DSImHDM9SAfpEp58E9MrlM8wf4b660-HNnlHhIVqBGiXT3KZU9hijC5kU5tEcYkIe886w05XzDoZ5o7-4AVkGPMEDaTNrfaZ2qNu3PiQY2ZNE20k4kLZ4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-0lxUX1W39qB7nhuglGKKYurWjAeT-mQsKzYJ5DW_natEpRByDjm1sDAPwogkx3SXVJOPzQ2wQEXjpq9xwmixn1YemqvDutryTpRjcsEUFGzAw0rklW4Fil_UBNFPhh_cE7ssHtgo8wo7jIdA_EEdx9Dr8PrQJEXf8igEpjrj9la3p5ofNnlxD78wQcasvAT1IhhMzZqD2iv_UtgLJZQAaV7XTampvOvONKgQ7mAvkIFKKXxUl3ORPlccbSU36aDPxZg9aqNFpneLmCf_Yd1cbmnpLAVF96sntix4w7ZiPqhYbjqVTiQTUhM4e9BumXU5Fwm_FDY-skONpXq5iLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3jJm1nXnUHAz6-bfnsQ7jmRkTQ7uX1ODpJFza1Zn7QmOynVxMm33cSGOhYuugOXabXcQMd1zqEP0iPlARxPe68j75uaUMYrygM7lbk0bIO_Ua9SbNaXFFtGoaroByOLWLE_Bw9WqxhAPMe_w-fVKUZY80yHFu2tOUs-uKW99zTfYj9Brf6Y6w8PpnEfNC93ZYM2DivRSnTaBfkkJgTAv0VP0fTIOJQKkMDFt6EYjqynVwjv6hA7jhEsUDX_QrLU_RKXqOOW7vsYZ6-6Pf0agzlslVLNWgTxfUOTXiLcHLqDyjpbCtRmJQWn64NkUMVsutLClWWh53KZkvasjGLpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIdBU7Wwr5kcq_gJ0ZhN3TpQZ_-bHKex0atJFupvz7bi_hJyDBKUcsJWnDooIlG0SVrTKk9YK7YwD8xZZoB-xbRbEPMs9BKUZ1V_eRM-_YMg5QE_1fEb5WOvwjtj9kL8K6KRgqlgucmCLXdf5slrGuAUa2ppQVzk5DMhfuVtOgYaFDbbZfJacHiW0BB3zjm2rjq2DePYvv2oBMrevH6qS553wBg29d78VVjKvPThQZg0X6gCI23KmgR02l58YiYHnDUVzd_uQi6XfIHPkDx0HUZ9R6AuKS9zCyll4iXy5EX8kuoV5KbuXdgaOors3C4oBRfSXKUKwDu6-IrU1mdUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXnyfNoRE-bWp6ZkSOyfOcb6DZM8jjguBRSmPGusmwx7Uw_fjoyDZwLXVVDSI1h0lBgDEKI7goq1UN95pzNLzHFWrWwVxZO_zWj8WMuzkiU8Y_nLBdlZC-grgWMNdvSFnXQiasftZRGr-lDhSMD8Nvxe0pIgouQyH5ZX3mlkA8P4a_o7B0Ilz11ioyKPNR4ftS_JzT04v3mJ8f2L-WOOVsk_oFuUbwI8C9u03ZygPpdaHKVN1WzBYHffpwP6KzDe8A8tqUZ0Xo7nvx1IGtX2zwd_475Hqk-OLXI9iq0HbydQORqoW4F3SNtcHCrHBTC9XPnfuccRJG9Pnj3zOpnaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr2CVEu6Y7IpJrCWnzw801UXO6Br-EKnUr0lKqaZVK2w-SShdkcAXLpXWoV8X5L0pQ3-CrPu0tHEaY1zfxquufSqHiW0S0tqE81MCz0xG0LUKEwg8ugnUyLh83FkKQ3zEBSleBZyDIcqxFyz73A8j7i78-DNVU_jNKY93OyEXUGMx-oZE4yNFz9JD7ehDoy7ihrL4kdIRXXSXe3xXZkBKcYiSTcfYBqgiHGQAQMhSnqulFu9N5KOQ_sn4Ym9R_fvWaT3qwaoRSvlMF3r4-ceBPdULqZ4JnbHeq79XA0BQ--Lu3tE-sF_Tost7hFb-KuSqrBQpiEqlxuxKYEKLS7jRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLvOYI6XQGAqxUVsZnUguW031AJbqA_ZdUmH5VXage_H7njxctilBy_mrqqu7gdyEGBI75awbRQATpPbXy-80jacO5UUCj3EzCU1yenLeHIUehiSpQynZQhArrFdtAkh1_zuedC_Gu60C0E9rjk4YjMK-HUnCylOpLRPsKZzjV1-Qoomfrbc5JrAW6PrFWlh8VuwlpDNNzecpV6XPBqWyOykdX9VR6m2R7h1k3kVVJhnyBBNx_SG2OksXN5PEvXHIT18bZAQqp-cZaO4E0HqBErfKseIa1wAyDVBBLM9RR5CukXSJXLspg-crNypxPliQaBsRWAi-qnainMeBg8QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=o8iQ9QN_aWdz1E-hKJLkURXppzuvEe_Gn5InYHpwszjK3lUfPVETWo2eOcjIfajeyinANuVHunHhm-VAbW5uDkLRdAfvtLQiJyQooi7YJdAMZHqy4rMqV_Oy_JDnAIVEQwUhVkXBVrUqYM8P_N1T_2L-h6S8R_vPdno2OgD1izIq_iCgmmKq2bv8LSoVDTHxEN1K2wF1fsGDZyRXjjBOmgc5k4musuYplgtQx0-46oR3v2DHpVwhv6CaMGXqw4xAOPoLQUePJGjFA3AAJD8hisUk6ztATjQ4xO9cDWJ-2dRzk_2xcVX5hpsF2jFwDL715cEywf6HY1Zn2CXUg-c-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=o8iQ9QN_aWdz1E-hKJLkURXppzuvEe_Gn5InYHpwszjK3lUfPVETWo2eOcjIfajeyinANuVHunHhm-VAbW5uDkLRdAfvtLQiJyQooi7YJdAMZHqy4rMqV_Oy_JDnAIVEQwUhVkXBVrUqYM8P_N1T_2L-h6S8R_vPdno2OgD1izIq_iCgmmKq2bv8LSoVDTHxEN1K2wF1fsGDZyRXjjBOmgc5k4musuYplgtQx0-46oR3v2DHpVwhv6CaMGXqw4xAOPoLQUePJGjFA3AAJD8hisUk6ztATjQ4xO9cDWJ-2dRzk_2xcVX5hpsF2jFwDL715cEywf6HY1Zn2CXUg-c-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgBGKbTC_zuPRAZ13CLcHIwQcwoDmhN2BwE3yO6IUg6-kg2awO3zp1wYL_XmPTcU7FIg84j6MFleegFvVhB1oBuCLhIMTkkcjQYGqv9YD-7uxf4EMn3v76U2IAGb44DFwtfckMHBu6cr67cJOMBaZtcaf_v_aaAC9DUyvfApYfzhlK4se2mFAt93BMLAR1CthmgGjun_d3yyrJ4XpyZ6imNvQUfq_3ambWdctnrJT9exwJ0aWkK7mIQM7nn51EtLIR3Tymy10dZyY5yGUn_bnXKLaNC6VEqy6ge9DdOwthYxoS3G0pH30-tuWUa5rJYBQrWw-1lTOpc-JOPjT_he6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wm2k5aghxQ86T2ePl9Jc6p-YTZv3PIqvk5H0JVZzTHq0sCmzxBZP6VsEnsFXwjY_U2MRDA8_IS0qCa6xbvBR-L-eSprg_JbPi4ZysbwHEnoQD3yD_5K-sbFJh_0Low0LlPWJ7E4kV0LFxPG9qhoGqJeypvDn76AhsI0arFGToGvjmDpwdd1-Siv9KIn4FV9TssROyWBye91qCCgJDnejVmt4Eh81U4r9GqU8pz3r8zSOSlo9wt7jGDU3Kw-lmTTAzbhdaLZ8HF-asuC3blYkJXeFrzuUYUEF3tYM5fJFb3PcF7KXWUJzzCkliluF1p-XOizo6uYsZB-Ptze8df-2Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYVOjlMp_DGqbdNjpjZ_O2HKl5Qa9YHEYgDShTTeiSnWIltve6GwMfMols3zpJPoG1A1q-WgJWWh81Xu-Qrd-OqrgxLVZVk517ESujzUSlIWtp6zjoly2gRr10xddckKwaLCoPjuZ6O4lbXOaB0W8ciLAU-11_k9y_XAWuEgSe8eDz918FSroGIIm9apCKW_LxKppiA_cGMEwuykr95-D0OQiH0MwLgYoEqQ6dB6Qici3-dNT4u0W03_as3kD7IgeFsAmQW8FF4HbC-rQN4sZT458e1f1UHBEsRW-PXe113jEUNNPXUMeyQYr3JfsD3plNoneqUk5nc_w_zUc_i3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O43IJqVVziCahcCQuXlM-1dMPNpXh9FVjvr9ATnAH-O4gqPY6MiCG0KYoOyMXFuZsU_2_rRP1ADaaW5z-ZdD7I8B4YnjDMCp-Gz1OBKOIIYwh9Q67mWvAhgLKkKqz1dxVuAghrkoIq9ll46jdTRLgv_-BmjAH4MMr4j0-JoFU-XXFrhNO5K8CUomKdWTTcydX0q3nd8gln1kMPhcRp0R_UzAVFgyRbxBhfmvAeD58Wg6suCsyQnq9JYqRJ1mQLlSvaNmoVzuzOzO5cAkTSFJr08oU26aSQt0RalE6_1cU_siNhwJe-BkLv1-2S4iP2BVTUJNJAfEwvF1Rz46Cf5wLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBnyxjLBkOVYOzP7KGU-B0n804CtkY3GqUyunIbvDBsv-1xG8W2hngvMOmEf0kK74l5PF9f5OA5lopwgi8ihLXzuFh2qzBAXUwrKKEWMRAhzzgm3pWPipEMWvbKWkyfLyGDLqE1qnP1V640xJbEMH7_1YGSOxHJjrEsUpS1vS2cgxL6jMlotDXOwYQ9ovMgK1_m-SBIdIuo-dSKprPbIvzVswbgzH_IIbVkSCbrpBAHLOyRmF5twxfbkm1yFnXtOm0E9mg7b4ZHH7vun1fn8ArqCUMPdvDorBz6VMNMZEWVVdG1weCSrXIkNRhUvzWMlNInmiJ1yI-aYh4Uau9L36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=fBsUT6puG3K22EXoYOdcrKHfZgYFc-33izhY474d8FR50qgsT21Kwxp0zCx_wJAQmlLUqpH2YGWryR7vctTwDIh8u-r3Ov5DKcuAgXSeGMPQHvb2mGqlddfS_9KGmdNXU-E2D840Ua1Rkk5IWGVYWZu43-3ebglHVlUd26nnI7_VcmURlWjpPc8ft_GthZYum0Uiz47L5NxQPftXVdkZ28L2heUVjcyzUqRC4sMi60zvha1bsj63jL3AYNKI82iwQYQIgMLtcbz3bFwB33H77EBHPnRitTURkPSTxdLs5cJz29nDOPSLpPkr5hQ7zaFAXqsfhiRUqTfkKImo66FkQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=fBsUT6puG3K22EXoYOdcrKHfZgYFc-33izhY474d8FR50qgsT21Kwxp0zCx_wJAQmlLUqpH2YGWryR7vctTwDIh8u-r3Ov5DKcuAgXSeGMPQHvb2mGqlddfS_9KGmdNXU-E2D840Ua1Rkk5IWGVYWZu43-3ebglHVlUd26nnI7_VcmURlWjpPc8ft_GthZYum0Uiz47L5NxQPftXVdkZ28L2heUVjcyzUqRC4sMi60zvha1bsj63jL3AYNKI82iwQYQIgMLtcbz3bFwB33H77EBHPnRitTURkPSTxdLs5cJz29nDOPSLpPkr5hQ7zaFAXqsfhiRUqTfkKImo66FkQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB0Rq7cmN-Mbj9Ugk7OIpsix4q93xm2WHvyFYF99Zfx9KoDRFgwlZEDY8iScwbg8UNi7Fei0sxdXANl5uBup3S76YhMwJlx-2r1UQuYlTSzGLsu76hA-NlNtdyhcc1nHi7_xhtSai7cwruiXv61hffxBGNdy4QzLmSuVfWGSgzINWWEJHyrdLxXvC3plh_hHjsNODkUITEPfGEWi9Q0GhNTYP5iW_qFCbPn-qLnEcVMfe-an8R8st7B5MdYWfhLQoz3kxjwMPzFxhkF7I06oxBYx5_Wb_JkVPfyLvbdey6KsJEamZUJNJkjEMXowWczczbKNXGb-ZvhTp4-w4iqZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgXnmivuP0UmHug8GmL5l5mmuCzNxlzaOt-aOx9GfGxauN6YjRLCxXCp8wZ4U5lxdVV5dEba09D9B-P3aLghsW5QEw5mISwBKT-6_zehsizbJcCyolPSxnWPs9fc8yzVwjEZJg-TgEC_qsiSwlTcNm3nFJEi97wmnnEEsKoWDsF_hx1H3lrUg1JAlDeaHffuVmEknMdH_5ikdrX0UDSUmNLEAD4A9uIe_m6nMQmcf3q8QWIJaQoalC5W-c-8jFVbdIf3eKxh0wckBHpWmjkLrRPfIggJqN8JSnrdLVFzdylsggi1cmJXj5bTVuzGEJNAKUIabM4amBDQJzMl-c-0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=C3HtXpISm5l6_LFEoivp7uBqmvwqeTQODYKGMiJwF79xc09if3mFxrCJPjPBLUZAn5S2iDOH6-8UIZojFxi6wXoIp8Tdkb7iD4DbxIafkLnkdxxb8gV75sQLMhkr6_4tOVce1M7AiLNFaDN5_R-199mI2DFnIqcPqQzKGaQW3IfduGTQ37VXsuTszc383DVjJS-dmRn8UYYRYkPuA7ITdl7mSXht5hB90IKdZTOdgC3jviy9BvXdYAk1go63NP1M5k1tZsca1lHESrofLXQFhTbzfTFtAlyqVJPCuXdV4l6MZCedXcUyrfV6xzv4TfWgeHsb_Oft4HaexusfyBmnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=C3HtXpISm5l6_LFEoivp7uBqmvwqeTQODYKGMiJwF79xc09if3mFxrCJPjPBLUZAn5S2iDOH6-8UIZojFxi6wXoIp8Tdkb7iD4DbxIafkLnkdxxb8gV75sQLMhkr6_4tOVce1M7AiLNFaDN5_R-199mI2DFnIqcPqQzKGaQW3IfduGTQ37VXsuTszc383DVjJS-dmRn8UYYRYkPuA7ITdl7mSXht5hB90IKdZTOdgC3jviy9BvXdYAk1go63NP1M5k1tZsca1lHESrofLXQFhTbzfTFtAlyqVJPCuXdV4l6MZCedXcUyrfV6xzv4TfWgeHsb_Oft4HaexusfyBmnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLnMAKNtJSx6L4yNH7DLxlq6LBzCP08_ndyTgrGgcD0K-cY-c1jN0-5eahv1VjwcPqXSaIOGstlaR3Fld7BJEPkwD6DAndU2pueWnPucHOV8ByHvoI8-iCGv2Ox5sXl4onxwNvzOm4dEeeoLxjnix23H9J-f_xkY8WqdNkxRJB3lF3pL3GOF4jQmTugf7A1Ikp2cTpWO9_rm8jKDtC-6cRUJLV9_C7MZhelf6LzcpdPoZcMbtgqjxUZ0x_3F28vhRTeueBMJbs9wDFuvV2L_27syw-vzS6k6fKqyecT8OcN53xQ-GyN5dXIwLUw6piHIlcZgpCJ2Y4lRiVssr1GrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxrz9e1j1GSVfMHNsGE9nC7r875Q9hfWhErdjoDLTS1VmGGZC7H84c5wWxx9o1ATMyQDLV467ug9Ewz3jkzIkyGXdCxXN1WMQMN-m0G1vbCJd0sIOeMBlPds7YDgLfVtkJCqvoRED7IcyUoPFSbn0jJT6pj2XbFgjwVgKkT8r6zZj20BmnsFpyoyR-SlOZaG-c8DFp8QLz9FrMUvCycDFMQSoTeDwyt88ukeivbW3uNcCGerFQ7AdrDrG9eMVifWgzPR46NDlhPhZQbg5rRPp5wIwm52KZAnjbvFx7qYMRyDzqdvBQxuowT8AgzFzlWLmIsCgtVYYLQjYxA811KmBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA-f5gDHdyiur4ST8B1ETUIGoUwxmjyVOEqhD-8VOEzMWqaCL0O6x6mrrhjAoICnFTOGTiuy-Mnhdafvozole8G6zHkkd3h_xAKDzgdn-ZNqWCm1XlKwsahQ4DnTJ0Uui5LVOtlUl_7hegjmw4bP0_KtcTrhcvBKUfth7q9LKsUuuVawrt57thXbDIWMDlmfX5xPNMuXCWzz5Uar7HJzuHVDUu-xPnG65QEXjsiBfXcT8nzKFgL-CIx06emHq-qRgl_C-AuYHt0c3kGBiKUoCjzexoT2dndIMfLP6RI95114d323ZkaIO5ql-RrtoV4QnkDjw-ycSH0pSXkQRQk_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgM03y8V5fFRQTl8cx6miod5kwIPfsuVdWmXwHrURwy9HdlCqsYsVOVtBFax4UbC0jwX2mDHrlDIFAumuWmSS_F578E-iVFrdvbGG9QjFU-WBjo9Be4Kp-dbJVEgatMilQ35j-8FsPh9PpcDcV2RAHP4ZMOcf2MvYIoQPdw_y79LZnUZFsxe3lc8VcpATbjOa1kQd-NUzbDZ_nNIEucYbbEinuKj_0-O1fWG4My4jU6WO5vcwNoYBqTpXBHBK7MjO7BxkewAuV_n2G_6OB29oJc7GsSRB_4_LkUEBusretJiMsf7AJI02HYx2j2CMMRQ9-1uZDGXSkVyOSnCK7o58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=WQGwELxM0pimaC2MmeJoamFNqQLkI6QyjlwH9lofLaithKW_T-IZgG71pViwx7o1EO9pF_fDSyyckU9vJ9qXi-10UyD-urgsutCFrKcVHowbqJNO6TSfbZv46V9Ibon8jT6XodZYmYGDuqP5TFk7rg6eW6zyzChyffM0Xoa2JGOQyYpMMs0mLEKXFMw7j7zTnR5Y6U1P_jkrVUW8WS8ZfxOloUngt9zdIGxWfRhhnt-6hnWD4aAnv1cugR1BOW-q2CUS4WU-5re4aDZQSIVP8iMw3MiTiXfyuk7cGZq2jq0m6x5jvK5ivHAtHO0vsOAKSWfuKm98HpKRV0HCVnvMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=WQGwELxM0pimaC2MmeJoamFNqQLkI6QyjlwH9lofLaithKW_T-IZgG71pViwx7o1EO9pF_fDSyyckU9vJ9qXi-10UyD-urgsutCFrKcVHowbqJNO6TSfbZv46V9Ibon8jT6XodZYmYGDuqP5TFk7rg6eW6zyzChyffM0Xoa2JGOQyYpMMs0mLEKXFMw7j7zTnR5Y6U1P_jkrVUW8WS8ZfxOloUngt9zdIGxWfRhhnt-6hnWD4aAnv1cugR1BOW-q2CUS4WU-5re4aDZQSIVP8iMw3MiTiXfyuk7cGZq2jq0m6x5jvK5ivHAtHO0vsOAKSWfuKm98HpKRV0HCVnvMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqvK-q0WqycUpG91IvS-tkCTa9XggWhlO5qWfuUR7Ja8FjoQzjxBWZNXqJbesAmFX7fCllmKXmKCLokDf6sWRzxCvwYF9mDPBYup79m4tNGx98j_SPVK1WRA4ZC1OpmbjdN5MXVuwc0NsUviWv_ExvEwdxxJTzHCnkdMJd4CyQPEflCDl9L09Rm34F1uB9Ct0Qw8ccHilcKl0T33Yb1IO3E2GytARezn5yZ581woFCSwPPZoOFwQ13wm6XeHaPwTOjpLOOEeoa5bifJkyA-scsMpPepUh9KYecTzg6rNNtKrCkfaDnzbNHlMXtfGw7zZt151PUvcEhD8I3iJf54iGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-W6gVLn-2WbyJzlzP_u2vQtuw7YdlU42vxRHHY5PQY4pTbaxV93HHH9zqau9AYlR-ce-6-oD5LZSisNUPXm17Ige1ci1FI7vMuRJylFnFK-MQwUnqMmF9KJykFWrlu9Deq0iKTCZD9MI-7CYaEYelWnt48JEsPlGh6Y10nB8YLwy8KX5LbMKL7dGqJusSTYcKZcjpQvRZiVvvrrXij2Ih1iCso_sflErAzMsyA6D6W9WSV5-JGSZqM4GTozERcyA7Nirkxxi-RCy5TSX6kqUVpkN_HkOG11uyEH0XHxrhHc75KfVeRn810IXUtDvd2bKNDg9q7omdXv4WjdDtOiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTZlk1Cmxu1OQvlDirmtT_Sa-sMyuACVExyZ6iELR0FxFNdBOo-nvHg0EpM3CZ9WQap7Ddc3lcGPRvWlDApXqP4Geihyhv6rL8RD22pHLdBzyNfjodg5p9J6W8mMo98PMxWnAM58Gn4PJPznUrHcjuiQxg4Gu4lXVdXB4pqT9ujPOZCkAbg24v_AoWMsQikiVCVVhQtCDTki-KwlSpKIoWRl95B9X1R4qy9s910jDT3gi3g9V7qtgGqssmWMEaYvp6KuA93qytzVWbfabXUCo3sq8ytTsF0glKJ15ya05WIGTx4f8Q-4-fcqFO407o6r8R1TF9jua8YBfDCklLNOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBdB2KOVnkGmsBbwhUhfB-N9g3N0NkB20EKBxQeORffHnhPQ9dnWHXKxAafNg5kJUd49ircww620voKh-yArlXSvxsNq5ZIWKB78l6Z32tJg_l_1rq2brHVWejBodSQDjdj7YtZc5xuGDnkCIdIAFPzsjgzIYLIme2yOdxAOn74AehXxJaXvqMrXTQkMTU8i3qtZ7PTakLYPESbwuFfrt2YSnunUOvbyXdPmHytG-ikN0yH-3EUgoEufiDsQCOBoSEqVswDt7Lpmo8GXS9Cof22hmDz4AYJL7J-IsnFo_uqxO4EE2P6xXyZ3xRpHMLXgmfgzkjhX2F8tPdBsqzFeHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=wBU7XysDpDyhp0FsGZnJjlVYnOowpms0sKVc6LCLly5-2a3_DMPRPgO_l65DOb0go1-3fRf60nMYBsZGFNNE3-ysDO9kd0npFlqQgcqKdDZawqIQB_uMfrQf5CanwL9bZRSo1XOBzsN2kEffzRM9poiwjPugUCGzb4DHEVVkOEWCiuA8ODRXoQZq_xC-wKGJ5WokS9C-pS1VBuf1iMaGp_Y3bV0RV1y039KPQPT2M5Pd26xXrh-R71m0fVSrMsDOCXyXqMMZWUcCgrtSlUCS1o-L_nDkV438ClFDhLVynSizBDQn_FzZTuVF7YYI_YXOBAuEg4wKQrMOhHIHPEWTHZbV7xQgsWq7By_7xF196D2FljTNkzHuLYkCKi-PQS9EMpJ7RlaZ21H7AFPUnnQ-orSruU71zcdFKUlSj9sdPmlNfRjlbX2VYYl48CC2YtuT2w_19AA9GSyo3F-uNrfKNpZ3I2WgYAS2NeFgjeuDiOILPOQ0sFZDD2XM-htzSSutrRHdEApUx1uCc1CYvMvBjVCT9u85T52G3kO15m12JbeQUpG2B2qrFLypUYn9TzlkMBXacnABd_6gxnyK9Yi9uY2_dxMb8CMYjz2dA4vAbTbYyZH2EpMWDEjPkZi_b29fezesRZVv_dlaspTxsV78kBm4esETlU-SOhW9abg2tZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=wBU7XysDpDyhp0FsGZnJjlVYnOowpms0sKVc6LCLly5-2a3_DMPRPgO_l65DOb0go1-3fRf60nMYBsZGFNNE3-ysDO9kd0npFlqQgcqKdDZawqIQB_uMfrQf5CanwL9bZRSo1XOBzsN2kEffzRM9poiwjPugUCGzb4DHEVVkOEWCiuA8ODRXoQZq_xC-wKGJ5WokS9C-pS1VBuf1iMaGp_Y3bV0RV1y039KPQPT2M5Pd26xXrh-R71m0fVSrMsDOCXyXqMMZWUcCgrtSlUCS1o-L_nDkV438ClFDhLVynSizBDQn_FzZTuVF7YYI_YXOBAuEg4wKQrMOhHIHPEWTHZbV7xQgsWq7By_7xF196D2FljTNkzHuLYkCKi-PQS9EMpJ7RlaZ21H7AFPUnnQ-orSruU71zcdFKUlSj9sdPmlNfRjlbX2VYYl48CC2YtuT2w_19AA9GSyo3F-uNrfKNpZ3I2WgYAS2NeFgjeuDiOILPOQ0sFZDD2XM-htzSSutrRHdEApUx1uCc1CYvMvBjVCT9u85T52G3kO15m12JbeQUpG2B2qrFLypUYn9TzlkMBXacnABd_6gxnyK9Yi9uY2_dxMb8CMYjz2dA4vAbTbYyZH2EpMWDEjPkZi_b29fezesRZVv_dlaspTxsV78kBm4esETlU-SOhW9abg2tZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL0GCt8nl0zdSql37UTLYW_9zOTipaEZCyqTbLiprv9KmJeCAVQcNOU7P3q01XnlH4uF0KjvUhMMV04OuEJctw4slf2CrSTm9Ab50iXlP_TNoK-pvajbVcX6s9B1ec-T3ugew_oKQ2Y2sJDBWowFW0D30TCQmM6xp2gLC1_URvbnwQlVIusgLfnJdhE6WZr6_XSSGc4QxQRC8rAQfZSNJ_0cmBdhPOCXurFK4Qd8V0Z5VCW1vnTVqeepRwqYOz2pzBGkTjJmRSqu6klhGBrqzMc-Fk8G2Z52dqB7rbHgCwz300EIgPQ0SzWo7VkumhLGs8D04zpCQaQ2CSwbpBf8fql8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL0GCt8nl0zdSql37UTLYW_9zOTipaEZCyqTbLiprv9KmJeCAVQcNOU7P3q01XnlH4uF0KjvUhMMV04OuEJctw4slf2CrSTm9Ab50iXlP_TNoK-pvajbVcX6s9B1ec-T3ugew_oKQ2Y2sJDBWowFW0D30TCQmM6xp2gLC1_URvbnwQlVIusgLfnJdhE6WZr6_XSSGc4QxQRC8rAQfZSNJ_0cmBdhPOCXurFK4Qd8V0Z5VCW1vnTVqeepRwqYOz2pzBGkTjJmRSqu6klhGBrqzMc-Fk8G2Z52dqB7rbHgCwz300EIgPQ0SzWo7VkumhLGs8D04zpCQaQ2CSwbpBf8fql8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGfgoh0BE2KF225KfMZFW0p90XeF5g5Qq4cEJ3Do5ye5zO9ZVSCdZ8oOZyDL_-qxxu-WUvpS-t8194dgeckeUBjuF8HHpBinc4lPzVkge9BDn3gSklyTy94dx1aB6BTrrjGOzQAkIeU7TCPut6iugzwQ9a-Y5dHokKIHvtBozJiE5A1zz4qwH6J3tUKuCrj1YebIsu3l1l0Z5qLMGnW1kAXLW19NfNiMgAUbYWWjY9KXUs9nRUFyiPjH8MirnL6vR0kTFcWWevT_xt_qi4ba3gqutJ2ZgZv-DZZta2gGMLMUCQbrAxVKmLbWpK6gJXDf_Mn0KIWhoCv-ZX0U9X4_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=TSIAgp6IUthTL5SJObyiodJVOULX8f2g-PezdWlnhd6nMVx2HHCYznx01UDXZ9rDXeimKaG66LkdLWIjJuTOS8pHIQ7DktfJgeLWc5ovQ0Q3D7_jgFaj1X4TR2BapW3uTTNcjM2HWqCFaa8YF_11kGnhwEbq3134qn9rklJXvl-BToT-kAboPuUXos9N8NHheMlG7syx5Ch2OMGMBYbZzTKK90ETjHVWUAHemMOSpoKwpzLpiVtqSI9LuuO7mhvMczHPk3LV8MQcFTBAbH0AcGHoNhGwVWbe1K-_vcqTUVA2u3QAR3I4II_SFLw01rc8Yog9Lc4_4OQVOMr6ZpqyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=TSIAgp6IUthTL5SJObyiodJVOULX8f2g-PezdWlnhd6nMVx2HHCYznx01UDXZ9rDXeimKaG66LkdLWIjJuTOS8pHIQ7DktfJgeLWc5ovQ0Q3D7_jgFaj1X4TR2BapW3uTTNcjM2HWqCFaa8YF_11kGnhwEbq3134qn9rklJXvl-BToT-kAboPuUXos9N8NHheMlG7syx5Ch2OMGMBYbZzTKK90ETjHVWUAHemMOSpoKwpzLpiVtqSI9LuuO7mhvMczHPk3LV8MQcFTBAbH0AcGHoNhGwVWbe1K-_vcqTUVA2u3QAR3I4II_SFLw01rc8Yog9Lc4_4OQVOMr6ZpqyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW7dM7BAaym6RWeBAXCr2qJnEFZzQRiC5vXt-FDz80am4QHoyLQFsPgGVIEqkVTifELvfKEOeTD9gFALJodvd5UQl42kfn81vJR-gMIeEAStqNGJOxc0vTI14tnOhnNOSnuQxYfSzrZdr1YOk4q3CvVADRrPJHB9qsnZfaezfqfTL3mN8YQ-dUIbcDrpaKzNMz7bcEfHwttHIPNjp3U9TDw7AUIHNPhRVRlBp9uRDtkyaVHSjPSnsbDP2_H3FxAGJXOUDNE9_x0cn9yV7n84aAKkQq8YORD-2_28NjKJ07y7spwc6OoTGJ_JzI_Hz5tXUDhdGSU2rO3jrAEhU2fmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
