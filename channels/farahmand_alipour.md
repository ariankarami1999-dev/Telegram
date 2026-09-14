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
<img src="https://cdn4.telesco.pe/file/FyqkbHXTB7hEcEEh7q1Bfyjd5vurG1-U2CcRrw7cwtSYn0TTprKlSPCL70ZChMuGU5HPO7SneWYrO8_2U4TI7FsEeDT8rSiJkAkZw_kXu1ZoIZs-RTDbtRC24ug5t_L_eGvhDUWZwUVzdh1hTtblE-_V5LNz0bF9mZ4nlcTH4XoxH6zyQaVvRjzpJE-60XIvq5xCaPWN4E6ND1ob7AVUC1fyoSxkVAk1WG2nJTjMss51lVVLW13I-w67W4PwBQx8tEJ-7OMH9MiMeA2QEpqsfFA7IbXfehTBXEHgqS97zTbJ207ip0w7j8MBy-_sFnofHE0uIgZhmGNLp-KhORE9RA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 06:03:05</div>
<hr>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=QNOzv4lEOIQAVcabo1_AznbYoMOjF_aHjfzQaxObD3nnNLRXIzk7Wki1Y_CW2Vopj_iB9KpQWhy8LqaNshUChGp9YgTfLTxYDbF95cKcpQn5FPQiLqsMObQRsAw-qyrJkvvq449Tm8h6ys5Cut_HGcG0pbzpydO674whTJRSgQPM851RtcgndTiMR6RYSGA_1jin-J70YK74CjwNeNYMUvSga_klNw6DGyipjxsh6_uhV820lHUGj6e2Fvn6EtM9VROKcUQT1wpO5ZD7GlKVCdnVDRCpiG7Z0rch0EA8TqLy2SUDpk20I_JjfVORcNamIYLs4l40j_9rCKao2UidYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=QNOzv4lEOIQAVcabo1_AznbYoMOjF_aHjfzQaxObD3nnNLRXIzk7Wki1Y_CW2Vopj_iB9KpQWhy8LqaNshUChGp9YgTfLTxYDbF95cKcpQn5FPQiLqsMObQRsAw-qyrJkvvq449Tm8h6ys5Cut_HGcG0pbzpydO674whTJRSgQPM851RtcgndTiMR6RYSGA_1jin-J70YK74CjwNeNYMUvSga_klNw6DGyipjxsh6_uhV820lHUGj6e2Fvn6EtM9VROKcUQT1wpO5ZD7GlKVCdnVDRCpiG7Z0rch0EA8TqLy2SUDpk20I_JjfVORcNamIYLs4l40j_9rCKao2UidYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpWCayyCDAcWeSRoAR-75XxigAGnv03rHykX05dJFvbJ6GNXLc-pYVME54ma_1VlicHZ0AwQc4gxuCMxFIN_YrZHninfH00q0QP1j_DRdD0rVoTmx1Ktx8gQJXnRT4Ez98XV70YgIjeKw8jpAfteTUR_HgdrWozt41aDh0lMRMZin_Y93Sxg2h8Yb-Wj9zd6PPz3oSuYWBtn9ICgJyx3cKIFW9QGmEjnaoBYLzWxv388PsgoQEJ2nI8-I1Pc3xHsHeav0-QtBK3Qq8OjeKv5MLcqO9MllLnadsnyXD0P6TbiRqZ0TUTPzRTEM6NwtarJlxZ9EtASKKbDCenqGkHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=SWXqdlREqaLSv94BmRbd5wCCdKdsuN9R3Fx_4_tpPhzJrTxoBaVZm50tq-GYYoK7mC0xDqfrzuiZphFh3r3gHnxTBT9vaelmLarskCfWNL-nk_TFjVrRUrLGvSQCCiktyFsSDQ1sOCOyfNt2NTLMoYF5NfcOr45-7vBbxlRYM53q3nS8yPJEqDXoQFYO0yey2NiAmhGRHGxsz5fttIRzzp9gKKUD7vidNRrHBrpkF9FJ7R0yng9sip0A__2k3tMfISEsJyHjfGQ_0gFKlnwlRe6Zikqa6aBrbmrCgYEHXw3rIgPz4WMEFRGHEZ_9ABi8VJPcrO4_hWSPADd6U9I3Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=SWXqdlREqaLSv94BmRbd5wCCdKdsuN9R3Fx_4_tpPhzJrTxoBaVZm50tq-GYYoK7mC0xDqfrzuiZphFh3r3gHnxTBT9vaelmLarskCfWNL-nk_TFjVrRUrLGvSQCCiktyFsSDQ1sOCOyfNt2NTLMoYF5NfcOr45-7vBbxlRYM53q3nS8yPJEqDXoQFYO0yey2NiAmhGRHGxsz5fttIRzzp9gKKUD7vidNRrHBrpkF9FJ7R0yng9sip0A__2k3tMfISEsJyHjfGQ_0gFKlnwlRe6Zikqa6aBrbmrCgYEHXw3rIgPz4WMEFRGHEZ_9ABi8VJPcrO4_hWSPADd6U9I3Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MCz5fuixZbFRY04sKam__XcwJ8SSd_1zakgaGELQ8sLAoDugvI2NZHdmSLvTytX8cvxlMumtC09xlo0Q0xTbdL4gDFZAw3YN8Y53TuT5HB0qG32qtU3quzDdG2VWRB06wXyGuJQ_N0dUE2KuVzak2pNTuCyUsjhfijaxRkSTt47EKS2F8cSHCTXZiDf-HL2hITReXIpwrFHlLfM54x5wsHjzEFOLONtwrkgx5m5hcGjULdRyH48WxFYKIHHvudI-Q577FKdUJingFqmC_j1c75Pbbz-DlA47nYrRCL5UysNNXunaSYHdJs5p7fqPmKaM-nN-ZN16kiv9jcSg3XDh2jTf524py1LNSpacBM2Eyu52mVYQgVQpbH47GbAX27xIOzuxi1D-GiYTlFqsvja89T4N8hh3X6u2WF-1NVd0qBWwK-_7qmknCGl5_vbTnO3VxLV8xcu2SvNstNxdCAKlNzPv-CXr_4ZeWxx5LvH6C2wDttLTC6Q8BC8npc-Ojnn1L1422zVgZUovL7BY3NG-jqWmPqWDNcqgMuJ7_Oo-LYf-OOeafrOyA6tRQD1S5cqEGDgqT39AEz6Z4kVWFx6euadwRqhcjOm3W0vOIt3s5B-92uYWiWuJgm6g_7aEXk-J79OVnd1gGYF5O9NeplqHEvQ3K8qSyQEtf6cdXbnqGqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MCz5fuixZbFRY04sKam__XcwJ8SSd_1zakgaGELQ8sLAoDugvI2NZHdmSLvTytX8cvxlMumtC09xlo0Q0xTbdL4gDFZAw3YN8Y53TuT5HB0qG32qtU3quzDdG2VWRB06wXyGuJQ_N0dUE2KuVzak2pNTuCyUsjhfijaxRkSTt47EKS2F8cSHCTXZiDf-HL2hITReXIpwrFHlLfM54x5wsHjzEFOLONtwrkgx5m5hcGjULdRyH48WxFYKIHHvudI-Q577FKdUJingFqmC_j1c75Pbbz-DlA47nYrRCL5UysNNXunaSYHdJs5p7fqPmKaM-nN-ZN16kiv9jcSg3XDh2jTf524py1LNSpacBM2Eyu52mVYQgVQpbH47GbAX27xIOzuxi1D-GiYTlFqsvja89T4N8hh3X6u2WF-1NVd0qBWwK-_7qmknCGl5_vbTnO3VxLV8xcu2SvNstNxdCAKlNzPv-CXr_4ZeWxx5LvH6C2wDttLTC6Q8BC8npc-Ojnn1L1422zVgZUovL7BY3NG-jqWmPqWDNcqgMuJ7_Oo-LYf-OOeafrOyA6tRQD1S5cqEGDgqT39AEz6Z4kVWFx6euadwRqhcjOm3W0vOIt3s5B-92uYWiWuJgm6g_7aEXk-J79OVnd1gGYF5O9NeplqHEvQ3K8qSyQEtf6cdXbnqGqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLiQ4FBokT3AOJ4itMQfY3E0ZLuauYCwXNfTRPZNjSzB2FoHYFw7lOXisV6DKzkhxKU7JOyyR0KnLMOQGTWqzXkJIkv5tpQBQtEfO0DkC4IRu55R3QAFtupFUc8QmDPtyASVZM0_OjUb1rXSnunjXUf97bHrgQ4W89t-MQGmVHiIS0W9LRqA11m9Oj8mhSTwcs26wkhqqgWjhIrCnQuOW6SCQqU1Y8b3z8OeDQW9MlcppnJYthWRjybNBdQRy9cNWyUPGMSFjSQZ7CPx_0OK0DHj727kZ5lvgS3_FArDk5hLqQhJL-pFXRM9lal9VANNNNqk6M5XQnB0pAUH2-cTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=qwzwirakdzK-QsCx0IcjeXuLwxMkMvE7UvqkBs6MBs5edraJvHCgv__ZAJlIlin0rvMNnkptGH4Q0kCXEer4QHrkwhlhCTBfhtgnTFOz_hw-a4DQGeU3lInUJCjeuk6HTB17zwavnxf7kJyhGG__DF6gwPr7pV7mjFuHhXHMjcet9pM_9O2sW_YMOg3I77vZ3PgIFJ8IYxphd5YwEFkfI1uybJMzww2dSP0XeX4MtXOwnje4AedKx-43P8RMPJ6lNQxeF-Fg4YEqx9FvdAor4FRWwTNG3QUHySpITyP37hRtHZHhAW43i3-X6y41XO8hf-MeyX8JhXtQ2tWstkRWzWhCTwFyIIyb7ygycdC84cD98osXqKv4iDGHYClrs6K-0JjXAryKtZCQo_-OItCEos19fqCioXPH2LuSXkxBaEoGUOjLBXGzP23Hwcnvs-AOZEj94us9RVNpYnPNuhfBL4_QLA7z66F2EN7L53L6FvpawNlkoW3F7swhmlQ9Gby-bc0WtaAf6iHBzy2GQB9V5VfEyTicqrv7K67I6q_1QXiiXxawMgDb046wwy4gV4ecABCgw-caq9Df1G6NHXu3zte9_Sj5hhF_35QE-1t6gj2Gli9bP2UGILlceQazVeCf5lQfAa51XzfPn7GoGdHE4eHbrzlRIj_KP8JaPSSK-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=qwzwirakdzK-QsCx0IcjeXuLwxMkMvE7UvqkBs6MBs5edraJvHCgv__ZAJlIlin0rvMNnkptGH4Q0kCXEer4QHrkwhlhCTBfhtgnTFOz_hw-a4DQGeU3lInUJCjeuk6HTB17zwavnxf7kJyhGG__DF6gwPr7pV7mjFuHhXHMjcet9pM_9O2sW_YMOg3I77vZ3PgIFJ8IYxphd5YwEFkfI1uybJMzww2dSP0XeX4MtXOwnje4AedKx-43P8RMPJ6lNQxeF-Fg4YEqx9FvdAor4FRWwTNG3QUHySpITyP37hRtHZHhAW43i3-X6y41XO8hf-MeyX8JhXtQ2tWstkRWzWhCTwFyIIyb7ygycdC84cD98osXqKv4iDGHYClrs6K-0JjXAryKtZCQo_-OItCEos19fqCioXPH2LuSXkxBaEoGUOjLBXGzP23Hwcnvs-AOZEj94us9RVNpYnPNuhfBL4_QLA7z66F2EN7L53L6FvpawNlkoW3F7swhmlQ9Gby-bc0WtaAf6iHBzy2GQB9V5VfEyTicqrv7K67I6q_1QXiiXxawMgDb046wwy4gV4ecABCgw-caq9Df1G6NHXu3zte9_Sj5hhF_35QE-1t6gj2Gli9bP2UGILlceQazVeCf5lQfAa51XzfPn7GoGdHE4eHbrzlRIj_KP8JaPSSK-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GSIIlMUBhkGu1oAQTlIzDMNEBHJ73T4KF8395zer-_7Rj5ICWWh2gX9_j1WvTNaoPe5aMCeXiven-3GtmQiX9BJTCZm8wqzkr0MpXusONr_5CdmD8_rKvuqJS6XGDzfVJvdTOkd8wOtItHLGAavYsodmzERRuOVzi0b2w1pab8K9373P7r1Gt-RIKNjbbfVBqnKI1OVcXECXk013Pa2UdGEAGNdJwh3upslP9eHPnqd7zrWLkwWvl9rOlqiaznE9rWAQBJ36EzL8sL-xChlrjaPFRBr6oN4APxRWqwtH59leDmKTj1XxZTUTGIdOhiFrOdo7Y-wQUV1u5aOy8Ch8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GSIIlMUBhkGu1oAQTlIzDMNEBHJ73T4KF8395zer-_7Rj5ICWWh2gX9_j1WvTNaoPe5aMCeXiven-3GtmQiX9BJTCZm8wqzkr0MpXusONr_5CdmD8_rKvuqJS6XGDzfVJvdTOkd8wOtItHLGAavYsodmzERRuOVzi0b2w1pab8K9373P7r1Gt-RIKNjbbfVBqnKI1OVcXECXk013Pa2UdGEAGNdJwh3upslP9eHPnqd7zrWLkwWvl9rOlqiaznE9rWAQBJ36EzL8sL-xChlrjaPFRBr6oN4APxRWqwtH59leDmKTj1XxZTUTGIdOhiFrOdo7Y-wQUV1u5aOy8Ch8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bNJDqkiGPE1DI9PZjhv87y7Hk3m5K6-b8oHFry9U_16Y-aGD3QZwGk5v5GKMzvHhDtaqy9uZmPaWHuOUqa6qbnbRxqH2oBMYtBkUY5biQJmXhSEorYYauj2ijWd10wlWA60ruB9GwfymJczWcLc23rAO0BUJHjRlfwLfiKzgkVWIL_jYRCcLuo5AWC0nN7Z9XE9T0oqv7g5sXbD2O0VZEpBxv1JwTCB_FlMZBJok8QihrvR7PvKUgYl0r-TZ06joozEpaxxd6oEkoFkXMQMVX2eFBAom_5q0DVXqA0UCq-7bzQWDdutj4OGamclyMEbSrxoQNJfWDN1Q3UAyqsjYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=bNJDqkiGPE1DI9PZjhv87y7Hk3m5K6-b8oHFry9U_16Y-aGD3QZwGk5v5GKMzvHhDtaqy9uZmPaWHuOUqa6qbnbRxqH2oBMYtBkUY5biQJmXhSEorYYauj2ijWd10wlWA60ruB9GwfymJczWcLc23rAO0BUJHjRlfwLfiKzgkVWIL_jYRCcLuo5AWC0nN7Z9XE9T0oqv7g5sXbD2O0VZEpBxv1JwTCB_FlMZBJok8QihrvR7PvKUgYl0r-TZ06joozEpaxxd6oEkoFkXMQMVX2eFBAom_5q0DVXqA0UCq-7bzQWDdutj4OGamclyMEbSrxoQNJfWDN1Q3UAyqsjYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=T5wa_EJScGIJzBjVgVSlhBgS9qudRu9NNtH7-aBYY6Ma3CdWlEViYFSD8ntVLj3uDt6pYV2NU2sKD8y6cs53l7ouUpYjJFSwVlq1ntbXDoNcR5-vwwlN6tjyQB-a69nseFq_9pGokrYS0YK3C8ZM93GT2ywXgTSmVGdQTTM4fEVM07ut9ykMISeNU9fgddF6w2GpBHB0SPCfSHN9vzGD2aTkyrdFwfKCuk27IAaLpgjDTrZtGX5RFKx1EsUA18QzXS42U9ehUb-WyGmmHJGQd5ek8rRMwg4vKTmGlntmIG9tgoZErwIOFiAT3RebJ1gdKWot3ItbWipofdm8BDTbdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=T5wa_EJScGIJzBjVgVSlhBgS9qudRu9NNtH7-aBYY6Ma3CdWlEViYFSD8ntVLj3uDt6pYV2NU2sKD8y6cs53l7ouUpYjJFSwVlq1ntbXDoNcR5-vwwlN6tjyQB-a69nseFq_9pGokrYS0YK3C8ZM93GT2ywXgTSmVGdQTTM4fEVM07ut9ykMISeNU9fgddF6w2GpBHB0SPCfSHN9vzGD2aTkyrdFwfKCuk27IAaLpgjDTrZtGX5RFKx1EsUA18QzXS42U9ehUb-WyGmmHJGQd5ek8rRMwg4vKTmGlntmIG9tgoZErwIOFiAT3RebJ1gdKWot3ItbWipofdm8BDTbdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=buBuUm2sxTityrfvhzNZc-EbSpXpHsiNrOcKRKXb5ANAZmeKzlSYrAvi0MO55ofKATAKb8w8fKL7MHz9v1FVubJRfwOnogrhAOI0s-XH6YLRJu-hJW5iOyBgIJ2vc756z7Q853mnSt9esRQYXchpOHx8FbxxHT_W4rTuNpEuTSDeQIeq8Si_H_KUEEg_sDuGxP3qlaCsl5OX6TmECpEez3LXrFS6OrlqOFpnjmEwbT5JMouyNO5acumCOKZBVuISLrqWyJUp3GD17NdjBVRA0hhP61X_fJk9_WIpTyyeZC01x_yMGfce97wXgOxbV8k6riRknw5jKtOTbtsWP8ku7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=buBuUm2sxTityrfvhzNZc-EbSpXpHsiNrOcKRKXb5ANAZmeKzlSYrAvi0MO55ofKATAKb8w8fKL7MHz9v1FVubJRfwOnogrhAOI0s-XH6YLRJu-hJW5iOyBgIJ2vc756z7Q853mnSt9esRQYXchpOHx8FbxxHT_W4rTuNpEuTSDeQIeq8Si_H_KUEEg_sDuGxP3qlaCsl5OX6TmECpEez3LXrFS6OrlqOFpnjmEwbT5JMouyNO5acumCOKZBVuISLrqWyJUp3GD17NdjBVRA0hhP61X_fJk9_WIpTyyeZC01x_yMGfce97wXgOxbV8k6riRknw5jKtOTbtsWP8ku7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KIjaQgH_-ZMO4y6bbrnL66ccnNcL39GDZ5NnAgT4oLQlOe3_DT8buPXWyYaeNvU_63sawmDt-bOqEmLTF-5Yg1K9Xp_JhI7b8nuL-8vJb_1hzKoOE6AKayQ6biPY5Bl1ou1wjqoEFXIImneQUF1vZed0EvAJov__8eeFcdrN_T76suCajIQf6LkUM2V2JrloMj-536i3Tewz3wUkIatCgo0w12Z470ST3gM0zxW62OCRx7yUMvgLZJufBktS9MifUvQjZqV660YBeGqdfoLQTZM0y8QnGdgRoIZeftQW_j3IGAdr2rrAF-1axktdvoAQ-OpV19nx_NP3u5qJzpgKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KIjaQgH_-ZMO4y6bbrnL66ccnNcL39GDZ5NnAgT4oLQlOe3_DT8buPXWyYaeNvU_63sawmDt-bOqEmLTF-5Yg1K9Xp_JhI7b8nuL-8vJb_1hzKoOE6AKayQ6biPY5Bl1ou1wjqoEFXIImneQUF1vZed0EvAJov__8eeFcdrN_T76suCajIQf6LkUM2V2JrloMj-536i3Tewz3wUkIatCgo0w12Z470ST3gM0zxW62OCRx7yUMvgLZJufBktS9MifUvQjZqV660YBeGqdfoLQTZM0y8QnGdgRoIZeftQW_j3IGAdr2rrAF-1axktdvoAQ-OpV19nx_NP3u5qJzpgKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP7VO6RdBJ9OxLlg-59rkfY8SRB88j2_IoYISTco_qZpJMXHBykjn6gVqNUaJtNpLkPk574xHefMb5e9Z5m2u16ffQ3F2n8RKylF7DVl_2QXUz-TS46bxk2kN6iDjljREUrPM6DwgrljTutYlAeiVFTYw6iHUjREVYFWRD5dzrMhJIoKJiixH-Cbtm8HNYFS-xuQTFWaJnoGkTQ0oOaDytYZLOD5Hhr_-_EVw53s-CRLCPtQREazGfkgfQjjBsGm2G2d8ADIjYtJk1X1YwMXds7h9T95UtQq11iiv7sn373fNubci-P3tPGG4KmPNlZQJzx6hyOoo9OUn3XpMW0Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=SZd3m0z8aqR8BYlcxG1NY1LLQLyz9Ddpbv9qF4UovNUUFqEGAiyrRDNy5jKhCL7cTOq0G0k0uxpadRr12rcdK2nq1maD74qZER0X1a_UyTxODVXxA5Cvq9TzxZVtz7_plW7FwTnKNAcHbSd5SopYoVGkCpa-uZ2b3gwenmoIqdPLiwb6WswZcDQ_AdVvSZyumSktZLUykPk9b-59SfY4OOf39Q7PtHV_vX7Ue24qIMpgGo0GNLm4m845BoPOpRlcTqAO7DdjCAl28Lv-w73blHDsri2VnRg-aF9wfrcjC_PHkd2B6HZ0x9BeYb1sq9Ai40EUgzQc1e7HIC91keC38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=SZd3m0z8aqR8BYlcxG1NY1LLQLyz9Ddpbv9qF4UovNUUFqEGAiyrRDNy5jKhCL7cTOq0G0k0uxpadRr12rcdK2nq1maD74qZER0X1a_UyTxODVXxA5Cvq9TzxZVtz7_plW7FwTnKNAcHbSd5SopYoVGkCpa-uZ2b3gwenmoIqdPLiwb6WswZcDQ_AdVvSZyumSktZLUykPk9b-59SfY4OOf39Q7PtHV_vX7Ue24qIMpgGo0GNLm4m845BoPOpRlcTqAO7DdjCAl28Lv-w73blHDsri2VnRg-aF9wfrcjC_PHkd2B6HZ0x9BeYb1sq9Ai40EUgzQc1e7HIC91keC38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mBtIF90H8ApO_yaTIrUqPeVsEdIvkzru-ZyY0eP7ekuHRJDKuGjLOAAncRokBBEh4OguhLMmffeI1OOrIVDOfK9BQ22urf8Hv7b5ukH06Omz09BJ1sdvqpVMgdyHJ1FuhdiYOcfkCjxGKUctZ-PZdVVlHDBlN7JQpfftxYrG-Fhfg_M_pIFxgy0AijGnV8nQ7nasZr5JR5zeUorot3vYcsK1qRcfhH2sw8AMs90ykG0F0yaFDab25_0XZGCELFvL-4GG3fGOovSj9CxAYpuuYn6DzLwoCjpWjSo_4YlLhE5vvtzdyAajJLLj_m_uHgKrWmLca_wWne31sDnMxc565w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mBtIF90H8ApO_yaTIrUqPeVsEdIvkzru-ZyY0eP7ekuHRJDKuGjLOAAncRokBBEh4OguhLMmffeI1OOrIVDOfK9BQ22urf8Hv7b5ukH06Omz09BJ1sdvqpVMgdyHJ1FuhdiYOcfkCjxGKUctZ-PZdVVlHDBlN7JQpfftxYrG-Fhfg_M_pIFxgy0AijGnV8nQ7nasZr5JR5zeUorot3vYcsK1qRcfhH2sw8AMs90ykG0F0yaFDab25_0XZGCELFvL-4GG3fGOovSj9CxAYpuuYn6DzLwoCjpWjSo_4YlLhE5vvtzdyAajJLLj_m_uHgKrWmLca_wWne31sDnMxc565w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HkwZy3FAYufq-nLvArHmrHS5rM9GApcx9dVDSZlzs4unJ1oWYBYTfVXGMZntXjV3GVsDHCU5kJci60TZhk0X2Xvfcf6rVFUTkBgVuFQq8qGy2mYyjWsJslTrJPdyVNGhI-SHy-pIodkdk5Jx8GAWiphT4E7_InxpLTKTX3eCe2rMr3IzxWEcPNo_cUwRhbZCOxy4479X9ExG55tlGf_74vF4yU32gWfPPt_acibzQ8x9d_cGbpYnmtVaaHtt1fc2O39U_CheNpQ8ZjHU3GTJv186LokoiIrEwc7J7AhIOA0_5ei_e7ciL_TZImLcdDMrycdjtRQ9KiiL06rgaxRwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HkwZy3FAYufq-nLvArHmrHS5rM9GApcx9dVDSZlzs4unJ1oWYBYTfVXGMZntXjV3GVsDHCU5kJci60TZhk0X2Xvfcf6rVFUTkBgVuFQq8qGy2mYyjWsJslTrJPdyVNGhI-SHy-pIodkdk5Jx8GAWiphT4E7_InxpLTKTX3eCe2rMr3IzxWEcPNo_cUwRhbZCOxy4479X9ExG55tlGf_74vF4yU32gWfPPt_acibzQ8x9d_cGbpYnmtVaaHtt1fc2O39U_CheNpQ8ZjHU3GTJv186LokoiIrEwc7J7AhIOA0_5ei_e7ciL_TZImLcdDMrycdjtRQ9KiiL06rgaxRwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSEYJvcqAfZP-5zFj_A1qpYXiI2bPn6iHoWVwrQoN9Wh5gauN4uJ04ysatc4iz8yLxsup48TTO-7Vf23J-pe4_vypvgtXfrM_q8b2HCQ6DVQWaVrFHfQZwH_TSaKRkrISu54slm9inRTwl5Dz612sf7BFqFoJoCoQk_gjiqmJtqrqkMBqibg8Au-kLBlVAZCdJ1gWJ6UAYAYc1Z3EgRp4IYwfNx31DsYTlAKBsj9DwMIzm-hiim5kt138s46sfuk9CuDL_ptuYf9DR2TA-sEtKNF2KFuFCPcUkGqHdrEP5_V6J3rOaV-iziGmyrg94ptyLXu0-i2xcV8nLINbW2LUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nf5fVtD6GtTJ3kTpDHijYxrPEpEjTK4zbuFCO6WBVKadcMCiRFCDnOqaF4fXULSU23gcmrSiB3J8C4D8TmNzS-W4EzJp6kDKqb7Mg5gva4XR82iBKuUNg00a6cme9z6_0TvO-eEmlLRZ2Vzb8uS_THgOQKan7RqdApurA6_p1xticm-HI_6LwN2nL0vcfsMDqtBTmFwh63fcq_KfL0tMhxI8lkO_aO1psqM3Bns5LpYuGbhHTo5YtvNoo68Sy9ihMAjwmk6ED_Nm61V5lkxImB8dbkyYmJU6a4rLB74fxDpqUdgVXqxrqcx9msN025ljO-2Vt-ED94ut1QVq0QJ-vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nf5fVtD6GtTJ3kTpDHijYxrPEpEjTK4zbuFCO6WBVKadcMCiRFCDnOqaF4fXULSU23gcmrSiB3J8C4D8TmNzS-W4EzJp6kDKqb7Mg5gva4XR82iBKuUNg00a6cme9z6_0TvO-eEmlLRZ2Vzb8uS_THgOQKan7RqdApurA6_p1xticm-HI_6LwN2nL0vcfsMDqtBTmFwh63fcq_KfL0tMhxI8lkO_aO1psqM3Bns5LpYuGbhHTo5YtvNoo68Sy9ihMAjwmk6ED_Nm61V5lkxImB8dbkyYmJU6a4rLB74fxDpqUdgVXqxrqcx9msN025ljO-2Vt-ED94ut1QVq0QJ-vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=q6uwRa06SKCuRdjX5xj29s0i9ueCxuCHPKvOuxj7Io13nng3_-MduG8UTl-Ybzhiy90FYYl5fNZmswy6n971VX7CwVS_LSUexA93T-OBCt60PquP7PK2XN6pz9N0UmP9p0mEs3W1Ey7b9PEMbZlOuHtX3H1c6h6ipdLDiIjfpQCHI2pTjW8sqz6oJvUVJdxphBsLnMz1gDPHYKPV2JdNGquOWk6Q0QS0KGpbbvLJ3RYuZ_ybjkHDsqwBfTIrsu92ffdaZOYEvLTJ3i_fVggq6-imJascXhhkoHwpsk3yxjWesgmh8VjG4CDU1hgFoQofELA3Gl6i9QOiLwomlNL1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=q6uwRa06SKCuRdjX5xj29s0i9ueCxuCHPKvOuxj7Io13nng3_-MduG8UTl-Ybzhiy90FYYl5fNZmswy6n971VX7CwVS_LSUexA93T-OBCt60PquP7PK2XN6pz9N0UmP9p0mEs3W1Ey7b9PEMbZlOuHtX3H1c6h6ipdLDiIjfpQCHI2pTjW8sqz6oJvUVJdxphBsLnMz1gDPHYKPV2JdNGquOWk6Q0QS0KGpbbvLJ3RYuZ_ybjkHDsqwBfTIrsu92ffdaZOYEvLTJ3i_fVggq6-imJascXhhkoHwpsk3yxjWesgmh8VjG4CDU1hgFoQofELA3Gl6i9QOiLwomlNL1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3Xu38PaM0w9g02Igg36oNzzBkww6IIqM4FrZgbJ0qi7pu2hyvkHSwjgrnX60HOuUZRtjmW9PPNaS86HhJagXlgYu2yQy5tB5qRsND7IKjt8SxwM62OdV7w7igvFxJ6xZvLB84GN5Opc20MZTatO7d5P6u6_KYZzR-oVufKpng-9X3ypIv97KVzoVVQ9_YwH-VNI82O6fipU3UQiMCdNwRtd3Zl99zBEdXryP230aw0H8MPsEz1GEep66eVwwNiUP_oTGbVgz_IGkmUA3vfGbpQ-eE1-BIPjsAGvaYIaLk-N2cbWHBS2mtmgJiDlOPJ1Gf83-tSD9n4nq1UMHIvFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3iAlwXM7JDvQXi-tzRMOk0jNyDoY6oA535atH5OsiKdcbNrxtTVWGYv1AoUsoDoVXBN3ACg3-o9FbTaPyjV8ApzUd8upjHA9WzyExU1oCTV5q4GIpL0Wjn41Po5r6VwrHa8_J5jCrR7LXYDohnKH4iWd2h9BJ8qWDiEnfgwuruHr7DYZ-2HCviiJs_q7nFTCscQcG-JIrx-zqeJgJSVxgPMby4CsIlnKXpdzyxNv44ggpTr873WVyQTsgg77JvKkWc4Awpnh2WjY_09pC_LlRppUlaRYUd1-_Z2XK-1uI1B7TGLAomlpSQWOQPIu5FI78R_x8uqTGwzCoiFCwllOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=unSaYwZiynlUmMbwe9HPEAnrr5zX3B_MTFOGXB_p0eEOA9eBXGVucLXYVSkR1CJ2bMy08o7mbRdaM6j0ojWDvs0-uO1IaVy40KU4Cp8TRc2sf4dgYoAer10v0DsKVMlHLOYmGtbQnv0qofsY-cufz3131-zN6z5ZC5VDARIRJmI6ZI00KxptP_0PSuDaXJlSwKcYEkHvh6WXJ9XP0TIwIQOa2o3K2kHLiRFAQCfB8aHw5F5lDwfvklaJz3QNehsmeso0hYzNMpXin09lmRqdmCwwWLuwuCPajH08nmLAB4-gX5YsnFU_pQlwZYHmWZVXbTscKo_RnyP87fb2jcIIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=unSaYwZiynlUmMbwe9HPEAnrr5zX3B_MTFOGXB_p0eEOA9eBXGVucLXYVSkR1CJ2bMy08o7mbRdaM6j0ojWDvs0-uO1IaVy40KU4Cp8TRc2sf4dgYoAer10v0DsKVMlHLOYmGtbQnv0qofsY-cufz3131-zN6z5ZC5VDARIRJmI6ZI00KxptP_0PSuDaXJlSwKcYEkHvh6WXJ9XP0TIwIQOa2o3K2kHLiRFAQCfB8aHw5F5lDwfvklaJz3QNehsmeso0hYzNMpXin09lmRqdmCwwWLuwuCPajH08nmLAB4-gX5YsnFU_pQlwZYHmWZVXbTscKo_RnyP87fb2jcIIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4QGcPHsvTYUUXw2pdbZ7evPY2p1aALMJfY_iRixXXNlTPzXhawoCwQwlzBXcAkYn_WjkKestJrJdQm5PqX4DOcUntxQSOPaF5HCaPpjxyjkcsFvth_08onIyeZDehqYrhGuKWCL-diJDSoFr8Hv9jlhl-H1LnwsI_WlctAIBl82RNDfwlr25PiOxftNTIUllgK54XF-ITJwO7aaPYFoMITbIm2scTwL-mrzorm7bti5OftHCGFpkyA1RQuAKPn0r9KQhiyskPAR0mZrdEfscwW9HLy5hSAJeZko6MoCfyWhIUl8d4OON83y6mGAbtwzYHADF6-NbN0yJzxQ8hBbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9899XTPO9nU9LBxvZS6mCWSXmceeVwalEWeRxzfiftYpFXrrewkg1iSnN9RKmNcZhufXey0_W6g1aKHG_UYbL20NhgEAeRNqgkGIalaWVBl337nfItv3eNxA6dipUlB8Rz79xBPsnYtcW6CM_6XEzOxyFtJE85Y4dCcebTwj3y9TgIdXg1VgY4GlQHm-L0kajPhcXdPRehfdFo8Bgh-v1hbYc7nDCxhgDqJFD0I1proPqtsiY4QQnbBsqE9tCtvqhB4-ucsFdHBSBB856NnegP5Dcq0FEHzxpEpPoVTYwEsW8zDIlE7UBtqTHoW9zq59D7G0XmCHbDKQsuS1MkcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFn5-sBMgC0rmQF6WqqMNneExuBbXpsS2KZoozshyOUqrJPY75BLlbYinkAF8eLTU_NKiyK4C0j5mwE5YiLRJ0NF9txTMxpcGZUaj15QZeaWpl3NHiN94ewLti5CK6p4h6vilJCMCQ7htUgtX-aCYFoOupRRo3K7SgT0mi96w8HtYTc4v-Qz2rOK8PGkV-5hVdA8RePMGhfyeWm-GJh43aWyOjfQJIJTmq7OFFGvPNOCEe7SwTR18k-KMf7YgiZ84YOrbaLQyLaDiwecx9e-nXkb2HuiXrDfOmb8VwugVkelUcqwwFANa9ABEIjV9o6Mg4CkmjqxoUPVSaU5C4nTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ChIe4ME06IvoQhjoTeSHdwg6Ot9YCPkbRgiHS4glliSnDzZ4-AWtdELWi4x40kSJRsryY6yJXSk3Z41fRVQT7pd1oYpCqWO6bIYJL9rCmzNwWk3J95w9mDhaPMPdnL7AYdEYXGRzcXlOl8J2vyHvCwX73NgxcraocTFj3y3mjnL3JGj8UxxDgJWbsEtdsENonZhNjXEXm9ArrsZl5-teM0nldBfliPoH9mtjJWva4a4wDoWUtQr-hXgjgpp0aUiVHMH7OJVP33mymf-mQBpv_W5YQD9cSXvTMKCHSzYqWHK3kJUacruvzPrWe81N1wCKAaQq6Itjy4XlxXQqV7fLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ChIe4ME06IvoQhjoTeSHdwg6Ot9YCPkbRgiHS4glliSnDzZ4-AWtdELWi4x40kSJRsryY6yJXSk3Z41fRVQT7pd1oYpCqWO6bIYJL9rCmzNwWk3J95w9mDhaPMPdnL7AYdEYXGRzcXlOl8J2vyHvCwX73NgxcraocTFj3y3mjnL3JGj8UxxDgJWbsEtdsENonZhNjXEXm9ArrsZl5-teM0nldBfliPoH9mtjJWva4a4wDoWUtQr-hXgjgpp0aUiVHMH7OJVP33mymf-mQBpv_W5YQD9cSXvTMKCHSzYqWHK3kJUacruvzPrWe81N1wCKAaQq6Itjy4XlxXQqV7fLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bcMmy2IWWP2RY9ikaJJ7mXRiIluuo4fZ_z6xF6v9FXP5SAVjWV6rE6pNLequfA7TaK2B8H8k3y8SFVYH1rfLZVWjnum1LxWSKkrzmNlJIVZT4quWYR2X1CxgGO05vrajGbVW4uBN_fl1JpFkuZSDYDIwRbbirhVm1-My38k7VuPcN2QCQjoj4G_Y5yRidT6k_Fyv6haHFHMcDn3uOltfNdTYKTAdFiCUcGP0NP1IXxbphuMhyNFDl8iexR8OE5UOYdJ8DlSiVd83els4R7hsvpkGAHs0UgeFtps3odQtVWdXBTTuQp_CQderj3aL34QD_d1WNskKV_S66HXurj_N9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bcMmy2IWWP2RY9ikaJJ7mXRiIluuo4fZ_z6xF6v9FXP5SAVjWV6rE6pNLequfA7TaK2B8H8k3y8SFVYH1rfLZVWjnum1LxWSKkrzmNlJIVZT4quWYR2X1CxgGO05vrajGbVW4uBN_fl1JpFkuZSDYDIwRbbirhVm1-My38k7VuPcN2QCQjoj4G_Y5yRidT6k_Fyv6haHFHMcDn3uOltfNdTYKTAdFiCUcGP0NP1IXxbphuMhyNFDl8iexR8OE5UOYdJ8DlSiVd83els4R7hsvpkGAHs0UgeFtps3odQtVWdXBTTuQp_CQderj3aL34QD_d1WNskKV_S66HXurj_N9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vCCJ-Yvjk3pGCXkBSw0K08X-iVOlLLUmBNCTTZx0tjNuBLZgo914ggDGwMEDy2vo5AjPsGBW6Ch8PV67qD6WLp8hvBB6iDcQVg6veaGqnw9aQFUQyzVBIsX-pb_T6jWFRTmbjihSI3NY0NTpWWjyKBsXEer4oUuQlkxT1Ec0EQQTaZdq89_RVcYIBfuYcTMOE8lObKPqn6j8lwNYLBzsjVxNFjaeB2fMU7s4Gnn8LG6NNz15-fSL3UnKYuIIX_aQzcKvrp1I7WYsCmlnBx0bcu-UKQRArgpHe8RbXLEiyXt5uW8_kqkx4jpGxEzWDTBtJqd_8fyn6k3bVK_cq3JAYwKDrsKWQuxts1CFljwft6JDK0-AdN9hVoVoUiipG_pFpx3RDuUK2R8eRoW4YLfRG_PEwCUgbJIIEu4Ts8pZmvvX0rQIr0s7LmPsDhTClx8XwX0p61WMjU76PgJzww1fcM3vsbP0rAje2OjuZyAyg9N2KP3Ax9yIZ1UNKjCbVUL-L63kHfV87-Av8V_Rg5lEm-_HiufCQkQyUH0AcYW0UkRw1T-ZVwFm7ivqP6XQSTU4Bj6ANC1DPaADMVAnnvMblJvvHu1dhvkO-3Ii3NLlvFjt6aCYgNEqR38tMLlM1_UpJ-7Adq0LaLilySSvkznOBo40AO6bjFSvQvmcEJoDtqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vCCJ-Yvjk3pGCXkBSw0K08X-iVOlLLUmBNCTTZx0tjNuBLZgo914ggDGwMEDy2vo5AjPsGBW6Ch8PV67qD6WLp8hvBB6iDcQVg6veaGqnw9aQFUQyzVBIsX-pb_T6jWFRTmbjihSI3NY0NTpWWjyKBsXEer4oUuQlkxT1Ec0EQQTaZdq89_RVcYIBfuYcTMOE8lObKPqn6j8lwNYLBzsjVxNFjaeB2fMU7s4Gnn8LG6NNz15-fSL3UnKYuIIX_aQzcKvrp1I7WYsCmlnBx0bcu-UKQRArgpHe8RbXLEiyXt5uW8_kqkx4jpGxEzWDTBtJqd_8fyn6k3bVK_cq3JAYwKDrsKWQuxts1CFljwft6JDK0-AdN9hVoVoUiipG_pFpx3RDuUK2R8eRoW4YLfRG_PEwCUgbJIIEu4Ts8pZmvvX0rQIr0s7LmPsDhTClx8XwX0p61WMjU76PgJzww1fcM3vsbP0rAje2OjuZyAyg9N2KP3Ax9yIZ1UNKjCbVUL-L63kHfV87-Av8V_Rg5lEm-_HiufCQkQyUH0AcYW0UkRw1T-ZVwFm7ivqP6XQSTU4Bj6ANC1DPaADMVAnnvMblJvvHu1dhvkO-3Ii3NLlvFjt6aCYgNEqR38tMLlM1_UpJ-7Adq0LaLilySSvkznOBo40AO6bjFSvQvmcEJoDtqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=BCESDBNmQM7NTl89S1yIKr-s0jApIAINdJCOW4SLCDL6nEfNaBMXFCncEhHHp0hk7aU5dJHBTlzXbbavOatDeLlcpY1VbbowegRnbR1jKD01cPi8h6LG190N1WjNysie9DYFT-NZ4DJZVeBVrJZInDtFumwKRqAmUkma_dtgX1xBySOWYqasrg8PqSaQ08kCOhshkYzd1cM2FZcQ6fSlb-ypM_swq3WDgWbMx8Cn4QlMsKCZ8GobGdfpyEVITbhttAhbnzBCB4XSfANeggg4NYFIIH_GVEIWfK2tG0k-9OIEHMcEbQsovYi8pO6gDU7sosgDjbcVVsBEXzQTZ3ZK2Udeha8Llp0qk4ersNRFWEAEiyLn-aryYGvbbVbL7on3vj17x5pGju01dd3yL3ZDsW_UhgBCl8dxHOHCv3x1LdGlSVvY_15J8BimzVXlFkYslWejR4OvI2L5jOE4xmwOV5OTzLEirsBY_Du-6ST7b6KXrelmKRWN5JR5lnsWv9odNNMRftH-uFi0GqQjcMqVW0buJojAdyVwLZb3EOi3mRQZ2jJsjBfayR2Ld-xd2JoBTNclmXKzOhVkZrBldFLiRRBGe8RxeA04YuXx7_ZZRs0Ca3CrYMIRyxvYrMNIwvnUI06KgLTAy94VdaWqWoaHUVthkE1c6G33LzlFX3QV1pU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=BCESDBNmQM7NTl89S1yIKr-s0jApIAINdJCOW4SLCDL6nEfNaBMXFCncEhHHp0hk7aU5dJHBTlzXbbavOatDeLlcpY1VbbowegRnbR1jKD01cPi8h6LG190N1WjNysie9DYFT-NZ4DJZVeBVrJZInDtFumwKRqAmUkma_dtgX1xBySOWYqasrg8PqSaQ08kCOhshkYzd1cM2FZcQ6fSlb-ypM_swq3WDgWbMx8Cn4QlMsKCZ8GobGdfpyEVITbhttAhbnzBCB4XSfANeggg4NYFIIH_GVEIWfK2tG0k-9OIEHMcEbQsovYi8pO6gDU7sosgDjbcVVsBEXzQTZ3ZK2Udeha8Llp0qk4ersNRFWEAEiyLn-aryYGvbbVbL7on3vj17x5pGju01dd3yL3ZDsW_UhgBCl8dxHOHCv3x1LdGlSVvY_15J8BimzVXlFkYslWejR4OvI2L5jOE4xmwOV5OTzLEirsBY_Du-6ST7b6KXrelmKRWN5JR5lnsWv9odNNMRftH-uFi0GqQjcMqVW0buJojAdyVwLZb3EOi3mRQZ2jJsjBfayR2Ld-xd2JoBTNclmXKzOhVkZrBldFLiRRBGe8RxeA04YuXx7_ZZRs0Ca3CrYMIRyxvYrMNIwvnUI06KgLTAy94VdaWqWoaHUVthkE1c6G33LzlFX3QV1pU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=idogT_Wkf6UpcMIKQMXVJuE8q5OB7BSVBFX3udpr_RmX_umC_Ddb7J0GYfeBB7acrEahY2n-TCSD-pFVoq4tOx4DE01yT5lbb0g8vmITG1f0JKr4G_HBy2pTRggeiKr5AC2vqeFk6ciGYt8xL9bh3XTjs505qzcc6wEmPpTfJnWPVaJy5PSEKqgY4gmac7wZxJ0HveSNFPRunH1PYN5nvh7fpPuyA-0w5DXAgSzT1fRO1HNs0VFNuqCTeTRoEhMk0WJdnwJUNqUiFxSUKAnl1t4rVy9d-kHKKkuWnD-As3QNt1MVCPe-jnrgayKUMRJkQyGZxOn20tp2Cb9xVzoAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=idogT_Wkf6UpcMIKQMXVJuE8q5OB7BSVBFX3udpr_RmX_umC_Ddb7J0GYfeBB7acrEahY2n-TCSD-pFVoq4tOx4DE01yT5lbb0g8vmITG1f0JKr4G_HBy2pTRggeiKr5AC2vqeFk6ciGYt8xL9bh3XTjs505qzcc6wEmPpTfJnWPVaJy5PSEKqgY4gmac7wZxJ0HveSNFPRunH1PYN5nvh7fpPuyA-0w5DXAgSzT1fRO1HNs0VFNuqCTeTRoEhMk0WJdnwJUNqUiFxSUKAnl1t4rVy9d-kHKKkuWnD-As3QNt1MVCPe-jnrgayKUMRJkQyGZxOn20tp2Cb9xVzoAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7AN0rY7FlXiBe8TiPXULEZiX0kODuntKFAozNx_caONeW9DOMmwjp6FIng2G78mOG4mGR10kgxvteL5RCxy-fYJ8GUjWbHr63O6EARmxhkZ5ijzgIoBZzUeqLCuOtVOoIsOzTJlNYTqVV1KBAqWHo_em02H4yF8eqYpSWSI4B_o9SiPJOHl3HjFuKZbeMISNz6rMKlS0mS5iKjrWQwyUTM-c9AqWYIcneVP4p3acY-eqB_IFDhV3TN9bl8tQFiQ4LIFeeBLld95NcB1GTAZGnjNlEElfGxU6CHLWwU4jqlNXIQj-NQdAvU5d8K_QQgkeTdztvoK7diq3ADFm-hXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oK_yvDwBC-jc2Up1NQBQzpY2dE8PzYE25HT4mhsCa6o1mjzk1Q5bux7Ed-3gJ_PTVARAA3dj9F_pKK9lmd4YP4dGW-MECLtow0N6Oy0j4lszgx-QFAasZBHsPrkbcFpqxo_HLuyTd5p929dylhRej3hbvrFkwx5zO7NCqTbfZ1f9HzM2G1xuvPEfwOs6o7ERqeaCBp_1X9HheByUggs16Ou5-BO3MO6sRZZtg0APMt97XOPuMHKKxvfSlHkXOfF7fW1wbws9jQPT0iMBQYPMYCtW8uXjlXGLdzmF8xYPJwlYhGNVWgGS7k9YAp9-GzPOcqGwAeph_EHf_MzZabfWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=oK_yvDwBC-jc2Up1NQBQzpY2dE8PzYE25HT4mhsCa6o1mjzk1Q5bux7Ed-3gJ_PTVARAA3dj9F_pKK9lmd4YP4dGW-MECLtow0N6Oy0j4lszgx-QFAasZBHsPrkbcFpqxo_HLuyTd5p929dylhRej3hbvrFkwx5zO7NCqTbfZ1f9HzM2G1xuvPEfwOs6o7ERqeaCBp_1X9HheByUggs16Ou5-BO3MO6sRZZtg0APMt97XOPuMHKKxvfSlHkXOfF7fW1wbws9jQPT0iMBQYPMYCtW8uXjlXGLdzmF8xYPJwlYhGNVWgGS7k9YAp9-GzPOcqGwAeph_EHf_MzZabfWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=rnSgblG1K021rXo6sJv_BoS_Emgr_xYqJdUtLyVM741Cb-NRmTWetL9jIxLhIQtM0V2W51c1L9PSsuVE4YPhpA_PjlgYUpk08rR79-vB0mdt3OPG4yEKkpxVpxc2fLEwa3QLzDMNtjBoqX7ZO1dFbYmUl5lzpuRM7tlcHTJZNGQ2G5mRMyKJVAiECawjRfFINBFpAQ5PZUm4gnOAbmMNzyZb5YY8k_5yxqlQhCLJZDfq_wDAxOZOR70L1CtLYio4YkqSWIZnve2F0fTFSHqaLx8Tmd68pBiEjp6o4rbHymb1dOVR2Xb-xmrIKIf0vz_M0VhOWmBqhEYJ6kn9Ozff0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=rnSgblG1K021rXo6sJv_BoS_Emgr_xYqJdUtLyVM741Cb-NRmTWetL9jIxLhIQtM0V2W51c1L9PSsuVE4YPhpA_PjlgYUpk08rR79-vB0mdt3OPG4yEKkpxVpxc2fLEwa3QLzDMNtjBoqX7ZO1dFbYmUl5lzpuRM7tlcHTJZNGQ2G5mRMyKJVAiECawjRfFINBFpAQ5PZUm4gnOAbmMNzyZb5YY8k_5yxqlQhCLJZDfq_wDAxOZOR70L1CtLYio4YkqSWIZnve2F0fTFSHqaLx8Tmd68pBiEjp6o4rbHymb1dOVR2Xb-xmrIKIf0vz_M0VhOWmBqhEYJ6kn9Ozff0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdyqBZqC_zWIvsrhou6CCHdLsBtZ4UhJWoSwJ6ZpasAd3R7-8ZPUQOAyFJz-uXslgtSuQiBuYTTJYzA40KTLrfWlBjpj_2anadsn6ESwLEEx9pNIXSaTf-hhEMwEFnuj38EWJsAQhhsU4KmIh9SFijlb9Q2ZmX3IARe3yoyXEGGmNYgyQ2ene9ggRXdUqYUXgRCNmh_QXAE2PAFgJykqmjOJcNkX2Bm2JgZp5W-I5pXkY_xDGRqvPmEaD-iGYBr_JmBrlj-bUQmXKEnXtg3ObfBj0r_9dM_v-8454KXO5VZZTcVItHMdKgqo4x9tSkV-J-hACt-u3vUFuwrRRbYH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaiVbnCboy9m6txYWej8LH7OwD_aLeesfaf9bMm6Q6gGw7t-nWtGUgXkqq0mOZmm424OdvdSHm-yNF3sjx2gbhsHG48P9Jd2RUxNe2hADIRyl1p6ZNqisFE0vUIkb46mCdeydfo7trR4eKMtY2LS0dOpT-Yh4p05cNWuJUZIC9fHqWbru4p97jTfA3Z2LJYvJNfScmSXm4AuXTYBun6KwE60M9oWzXOIadihEAkL6nv2wBCHC4Bh3WqS6hpCm79jEx263RVYJNSMsrmDZ7PKakyWgHk4OhQbQJN5VOMaExAgKrMlV1qNhLJOZrvPZx1ndGf3sRaCVHN4RzzUjJB5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXbofFoIUElEgtjVgXIBFm4dN355Y33WflMji6IaRxBbEU8Kmv0ks6M_3EUaiZgWiEJ3gR_Jaf21LnOhFxZkH0zTOwz87jwmyaLbC7e8HP6PYBuHcuGSHnwxZrhsKVfYn5MqxoJaQ5M6TB7zA1nOzCqe5CiaEXlCjTAROy1F8mSgyuNrHqWEzRwn114DLYF6RfSqwYVETdiw3tfHV62mypqxNXqvNvVgOhb1BE1upjrkqvEdb7I_R4mYT3VxWOR103zSZvQK5DKOXqXH2gZDqdoFP52rD1r7-ai_Z-gKbKj_2M_s9IoKZ4YjYzaK438AUB3-uung2grXpJ2kGPGlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfmq9c7gtBXdueXzBlCscH0Fq6TqhjYdJHtO8GDE6akhiYB_VTYgICJJvNRmc8clX16xCNqLLwGPHHI6aWI-4MnhYtke-4lDKC0l4aamYFRWD5jGe1rhY0gNMyUApKnq72183c_FmVO0Nc9dn_AkFWYwrpluBOCz96xsHCbjM8JfVoMqwaQXkaX0JiJNNLvzmht1WYCJUvo1gp20KgSHskt_FZFFnBl8FUMqPcy97DzjCRw5miv0YiVARQD29rBp02jmZ6nUZpBFewp0QfNkyR0-xhHAAIwcokxdRFSd8C-VlMNPutCKBVWyVTJmwjpA5JW3unC53-mqEIdVMU8AyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnK899rWvImB0WfaO--xTGIRK8_Sy3zwYuHCsYxkbvI1fWL5w6R0EtQMhOj_FsKbSga56OnlmSNscHLufj5YgqTb23FlisipOvukHOv5vIF1Z1fXoA5YlJlxrYagD_gBocMbalcEjVAucptfX3jst-UtZOlChz8HHCjWS3rlKJy4oDlwP45Y6aDzAFM-2WkcILwbObAshlQEQ-wsTLMVpN1mzFS-GldifGUZdTy8yZsY2qb3x1k5aJuCkta9pSZOr5I7dfEA5k3R0de8LgrnoLnKDbY7chZXxpGlie6_XtQbIEXzfbT9E6E0WhO7cGpFkoM6rUeGvu7QkCVDVKx9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAAldEVMEFaU3ItZu259afFs5apxAfLx1aVZNVcpdmuqz2eYopGdrNFiME9gCQhh4UYwPeb_5xzAyM3oDI_zw48rTYOtVABfDZ7OjjXDpq7u-X5V-WkJoEb5CSMUDiaL-_8qJqmJgSjFjJh4uHBZIZRl360Q6RUx3hjjpysTwoW2_-BJeeRri3cw5Uw2C-yIta16Mv0zCKHBf3HRn6dCtpb_HP3FuYmeZnTMDVAOLxobmS6XR2kDm_NsWgD98_dME5MGYfp3591K9l9HBBvR3GZaqsxwdIvUBeyzaJbypbAipr82Y61Vz5hAziV08dyNHCYndNy_0DrDKDEr7LUUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFD795t3DCNqs8ffRfQJda-yXUqbSXe6D9v_VZOKBR06D2XfM47rau_Rw2m4EuOKcolwwsOCu-l9F2q5wHF3sA6fqus4-TxQfingVW9T_cF3lK3Yg3W4XL1HJKU1aj4X4HmTQefVrPqb-eAe4rmdAftDWjW5EHSEwqcoxOIA9RuprONcbiEK_C7UCGxZIVu2Dbpj9nTTKNuVYDudM8Qwyaj3EM_pjpneawGA_9JZg9F0oWpGnkENOXJsJBnVUlRPSahTK2NQ6f9YV01XxdKfnBlD7Eh1G9TyY1tQUIuJbkD6zxva6B8dyKWY-PK-QddXy4cqPM0_7igwddpbTp8MMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNxZWcRSD_aS0mVBu93xVylIOdZ_YPJN5-TLDV_z0LywZ2RDAM7uCCxXyED0F5rilQdTEsQOBBen5BSA5qM4H19P150s8j_Y6_wwD89B742eJZ0zUQvtHgeDLf7G0ifWP10sidYuksD2sLldLreimr-4HKNwN07Q34ViE8Kn_L_PSyx_fZHbtJhqVbW74ti7kYOXkKeLPNXnokZAuycJOoKO1bzFXymVEpAjFrhUn4aXKlgFghR7CI1CdSMkGSzf6iyD6G2BsB05QGYsxDfEwDQu8lIV9fn2jN_V3snQ_OqzfIrFyOso1LluFwAvGMTuM1VM36RkgtW957kZFux2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKzONYnt35g3Ey11cRomub4G2ZRFX0RMHRi8rkAh-JL9YfX1sNDZfp3NwwGbKnQQg3skQmE-3OV5_QrmVVp_ClzRHKIdXiABcac83BYWib0iTPUV_nl-2lChdaypx3RBHXs7dzYKXB0CZTGyl8z_cY0d_Umqv8tBDugA2PTucriwDDgvOvdVfnDseJLvJuw8_taDh0EckHDEJnINM3qGKz9IwuJhG5D9WB7mPpoKwxdoSVWkikPxfg8w3FmRUBfD8IB7WdF4OIXwzvwW3RozpascQj0OPOWdaoXMawwMbtLjyUmgywOsmEcgUZRrTOAAdYoaa25VFWnb21YsoA88sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPEuwWqvYIhHO6VMkP6Q6aXgwBbifwpnT4T4Yw0qBAUoyjR48iveFJXcXpx5kCn42MIE1jD82PYUHxgQdtoMxeLhsqnda7wrkmxYxTNUcLfkJDp8zLMgEMOSjQEsGgzYvlHmAUfPHzMaqICemG1nRg8uvUV8kqP9eD5P0cxzrW6Ef1JVrBRTL7CW62N8jC1E47FapBmJG4rkFB4fL6Lghy-u84KbUbRPFNP-Gmsjzskr3UrP1DYqIZ80Vj3fs8Yx0845MQH9R7QF_ek_5FF5jEhjEsG7oyk03bEk0OYR72ryK5C27hzzBbNb2II2NOlCqkboakwQJ6LSx_LjFWf5cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r6oPoXDpZ9jP8zxAYZpeZde17w61jzdmYMhU1_hWwpsKRN5FWjdUfwcfVZ-EdZ1zxp7IUspcSau-e8q98bY6glHClThHnQNE7fXF5h0C1roZQo7tgFiiqs4XQxMpTCjx4HSTs1mDl9Uunpi_synxDaAm0ODLWciLxjzgTv01tE7xEtko-Wwz29rjXoFD5-hb6nilU3u4ypW4AvODElULR621clMFPDp0McADkqTeGdozP6NIZ5w997jZQujxrXVRSEj6ricnRdgysoBh6O41uK6f5h48HPb3ovhaeVRozKwV0tS3LyY1qsW0Wpmgxe1gRYVamAK1lA94R6pkPiihnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r6oPoXDpZ9jP8zxAYZpeZde17w61jzdmYMhU1_hWwpsKRN5FWjdUfwcfVZ-EdZ1zxp7IUspcSau-e8q98bY6glHClThHnQNE7fXF5h0C1roZQo7tgFiiqs4XQxMpTCjx4HSTs1mDl9Uunpi_synxDaAm0ODLWciLxjzgTv01tE7xEtko-Wwz29rjXoFD5-hb6nilU3u4ypW4AvODElULR621clMFPDp0McADkqTeGdozP6NIZ5w997jZQujxrXVRSEj6ricnRdgysoBh6O41uK6f5h48HPb3ovhaeVRozKwV0tS3LyY1qsW0Wpmgxe1gRYVamAK1lA94R6pkPiihnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO6ddsaryC56F1VwYwTgh9XU5oFpGBhj2FrFdF2eE_0Teqrob4zCiAjo-_Ktag7JdFFulXYAv9rcrMJ9Clr9UX5S7QSr7CDmhfJhzAbjribu5WGfwvgyYlC6slJr2aLt9Se6XWJrrcE5T37-TLGGW843LU7tPreul1T2e8PnyIpZy8xGqgH7i7BU-KLZyf8GOPfjhH5cWfPWhA0tvFe-OfCN_eO3wO5HrxHmXsHxFacxBsXLhL19oUY4kbjcblqiqZPdQ4zNteAYBonBk2qgs6F1CKn4aaO-z36Cz6YzeJE3d0M8LSDZ52OxIc9xhvlZNptaWsxSBd09SR2bpnyVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf_z-WLPbSOgflnhmIpHmrGMP7Cb-ZtR3ROaU2IiF5SkAOCHTA_eE89RhQ9YglVUbQCui7ief6WSr3yemohCOH9GmhomZuRsESyXGS-qZWeTdTXr4U_tVSrd8EMhjCA0WrqVUD8IlniMcnBldyLgO4u2sLBNkN6qIlO7S10VqRDHrvraoN_SnYUkOInLnG2yvdvXZV8e40PnOzIXt6INOGM_pQEW1HmJVpdUGjP7kHVqixB_MX0dii0g2Ap6zitvk0rEy5GVmzk15kLOtKjeh0QBIPFQ1Vtq4A_oHCQ2G73EGUaXCyAiGp-LSBrOipFbu5-z8M2DblXL29u_xt8NYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=XjULRvJsnd6KLK4fiaiHDd-2opb2PIOTKt21ferI-Py4_ns64tPjFcn9DJ6YGbe3n-BgSGveFyz29BB9XyKoRSL_nVCpEODnno_fous-lCz-luDsX_nDg4XccuZJBjNbufE3nFNG86FTjfnblDi-HKdr1OSB0XlRqfuEoSmvJEdFosiTY-_rtJTG6OR0PkHTOpp8wVwTj9yX5T9QNbpvXt7fU38_uK0RAKEL6j4LVU5ZcXpnpDSuEisjtRCgU07Df0UOknqxwKQhRnxYXfdHd3iS3pkJjQ_AZpxp7WxleM74DcO6PBgVK4PO2TcRLdIqhRtRBoUxCNrkeNq0bVKUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=XjULRvJsnd6KLK4fiaiHDd-2opb2PIOTKt21ferI-Py4_ns64tPjFcn9DJ6YGbe3n-BgSGveFyz29BB9XyKoRSL_nVCpEODnno_fous-lCz-luDsX_nDg4XccuZJBjNbufE3nFNG86FTjfnblDi-HKdr1OSB0XlRqfuEoSmvJEdFosiTY-_rtJTG6OR0PkHTOpp8wVwTj9yX5T9QNbpvXt7fU38_uK0RAKEL6j4LVU5ZcXpnpDSuEisjtRCgU07Df0UOknqxwKQhRnxYXfdHd3iS3pkJjQ_AZpxp7WxleM74DcO6PBgVK4PO2TcRLdIqhRtRBoUxCNrkeNq0bVKUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dYmzjQs0N4oJ4Hpq-oyNiOg3zeF6oODi1stfDfXGiqVeFepD2jyHyO0HXkO42Qd-sZf-5r0hqJOAQrQf6wCxYU2afpXfQ_oiFjyn3UVkhLYyf8MkY7EM3dMYE19xViMZ2t6gbCO3nwC0Mck7ndXoBI4rBZ4UjpGOeMTRR-zXpxCJrVGcxt4jDbsRWbkJ96mS6B10kPiQiAwIKff-bzZD77-VtR_UxZLGQoeOz0jw7XujzUGlGNdvOMms7d8lynhxJCK0e266D4F48RcB_3RgmMo-vSytvkJqKw7t1EWhx1RSh3L3N84hwFrVy5b7rgNmr-OYMfsvp6DI7RB-gHVf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dYmzjQs0N4oJ4Hpq-oyNiOg3zeF6oODi1stfDfXGiqVeFepD2jyHyO0HXkO42Qd-sZf-5r0hqJOAQrQf6wCxYU2afpXfQ_oiFjyn3UVkhLYyf8MkY7EM3dMYE19xViMZ2t6gbCO3nwC0Mck7ndXoBI4rBZ4UjpGOeMTRR-zXpxCJrVGcxt4jDbsRWbkJ96mS6B10kPiQiAwIKff-bzZD77-VtR_UxZLGQoeOz0jw7XujzUGlGNdvOMms7d8lynhxJCK0e266D4F48RcB_3RgmMo-vSytvkJqKw7t1EWhx1RSh3L3N84hwFrVy5b7rgNmr-OYMfsvp6DI7RB-gHVf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWak5odFQqZaPkkqVMP2yGl-BR3BdWcclJ6DP1GO00oQpcPWtwz4mQ5WD3K6qft0MsvafoPlT8e3yUYb9GunTDlK-i7ZuUBLPSvKZmsCBmPeJ4WROBeslcm6SfO26envf7EAXvyFDRuYAdwFcWzqAjgJENghWPzOuI665rCstP-Ji9hnix51qrAko2IF3bdX9ZQJqNF3CsA0CjLIrEjXkejF8KLpRqLMlvLj55QvU3TYwaKuNuWgbhAKnE7VbfU5s3sdUP4MNRLaxnRAUrIZNdU6bQyfI9amYiAgAxAJv88XJraoZcHtGI8f4m4UcITJWoBPDQ06UFjK88OV_9JtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlNB8fqkQuo5bH56UNEefm8vphygSgRTvsm2UXGhkv8SL8db2LleT0tLxHRJ2epJWUEVmpBtw23vpNJi0EaFgeqd5BcAYxe24Ii3TN740Pryv2xPrxNI9pnA6A3jdXIu9Vji6MF6cR6R5bX8XC3xiclMDItHVCOX-hsGuLIpAB9YytjncoapF1E3e2M0U1ItF7S63AaXvsSncwhjd47_R-s3plUv_SOUyOBcZNmRTU8VSmtxLEI9vqQvShXAEJyjwMhcZonkRJDWeo1ko00sz9uT7w-GPyUbAk1QIM3lM6H3QTOlieDeTq8OIRrDhTsDy-ezo8AwaHKkkJdT9arUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okHNmGdnXcA8JOdrsjvnVBWfx_P6S7f_x6Otq0ec5dkB_mZ3dNEuOfzldBCizRs4wmjTH6SO7JghHFHybpRT9JX8XA2fMFWh2FzAbwEz9Bi77mbNJe_KQstyhnewat689nYjln1dFVP3l9euQuoLyymtx5WsDJ0c21piCzX9Zqwue3IYzaiHOXQdnRVmr2JCWSksUKSZPDGItQTnmqrKwi2YgEdbD_k0V8Og7AFghUcuDf3bk2WHLMElJ28EWfEu_GmEc3VsaRPusxLtxT7cwNVjy1_pwkQMj7Xnqv6Fpw2x5q-DZPs39EO8J_d3cEco98BzgNPr3-zlZqSZLW4trA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6lRtiuLXMJQhKDNfGu8Nryg6BkLn9sioFGCZNW1TBuVrs7e2u9LTJSaLVJJ746ASPLOFuCs9Dw9rpFCCtM68ZxbXRDeOXzeeae5_pS-KUdGcEfcwvpZehHRf4xC5-lSxU0v3YFDyWjeRiER5YYnksS3L5Kvul2Jt_FZIMaKY9mC04-i-FC2FHJTnKmGaRr66alyGgXGISC8bJyPZZ2obveImRDU9inouXSfTXT917DdN1AM4NejuLvtZB4981tOgv92gApcRkzhRmL9ZVgQ9ifsnCf0-yjKEf8orZDUkdijBuhjhFrBBme6U3wPXBMkXl6FY026gXxRDbS865uGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2BWQ6ukGlsxJunYbOrUb1BFaC_ApAjhAj1u6USjr7rmK_aMJxUmyHJGC91_cbPxtlEc90J3RWH1DKgNZg2xmllVAn5CgzGUKF4RgoWfkQsyC005-6LHXP8zg0_0MfddRSwV-fyibt9cL42HPGWgTvx7JXwWfbAYVYkA-CxRRXrJ3uebJ_kPVhslU4qa292FLSHk8sbWNDriddAsxl0jhyNE8TsxH-sib7j3yv6vRogBfHaM9_V8LA2-ur_h0BgxeXCpRhZUE5IySQXVvnR5wzah7ajDUikG-aCf_Yk0qQREHJydufur-z2NFSt5NqPtDuBNJ1DO8BT5r76p0SjZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFuck-mz0cWESlSiV176_mwpm9opjoP9BDw2ZyJk76Agpl2W2Wj_81XjqDNn7gz56FWi8X8tQoN5tDEmo4javQJAL4Ba-re8hmbPRqv1rlEqZ1VctMORu4bH6TBWCey0c8mKsH3V36i80he87GeT6bLW60zMRnVsu6FCTxvZIIgtxTIZ8LmAllB8ylpWfGfqIMeZtfafUO_75pAaJSuX9ZoYs8ddEK67L-bRyn-MZnG5GaLOM2k_kCHmry_XPaPpE7QpvgPNckG49Yl53pbs32mot75xgBRzl9cVNrjrIyvc9d3PbFV2OUsOCEKZmIRF_UneQXQFG87W54OWuVtOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs9yvNnACJdTESupO4UBRksfa8f5W0hQIz6oSZe3pyDLoVcEVlKBkHeiNq6BBWyOd1VKUHLCQdRmvTsan95oi5-jwnt-F7oENvWig9ToLe-XHtQg9ZPK7J6Kd-DgezP5SurCv4_SL2ZhjdMjP0PH7rkQeNnMgiTV5XRsJfaGK5g2wI0eHFdti14iylm6oJ_aRVAbK-PGngef86vgsLNK6SZ2g_arMPqEe7ouvwb49E36BSiwJcRGmQOV1vLSZWPi0AMpri8kJWBejcIbNAR7D0CVKl6YgSIOmLpfhRtC9wd9iOLRxPj-mLCnrFZB7BqN_D__2QTPO9wzJ0-4M9KfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXg8AeguJCCqObpOMYSd8gNKtwViS3-KxnZB_i_3QJF2uwbZMTWU5O2tCdUcxCVcjzkiblksO0by_XgIddZMnIBuzXY7Q7LR-UXmJspfsUgZykshxHsC5-RudbEm1ZfR8FyB7tlzroxdmiVayMm9_Dc2QaW19vr17z43q3uasyyojqvaGy8Tp45OVMb-5g6Ti3ofQw1tjZJ7cyrPe3OBRpL-MJfzgHlwlu4QAQU5vBVdbUar4qMfj3N9SwVM9o99INOIpC3rRleW7exeRiltfbGEEFU7-zul8m78jKPuILBh7FcZqfe-mM_2XS0Lt1U8OeKMXy_XiilE0tY9QzmuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=hG52MZw7yuhszxvTUUpLYGCvwVNSR1EYEnaxptkUAT23FXhvU9uH-7KKkVkDUyxCPbWg6KC7LwinTAXbWDOZZbwQZNAMFV_4kIDcK4wWkfvzIg1BJsBqvXE1w2ss51dbGVySm_LnbjgV8TucoZ_DKo82_DDIOXJlD_zlW3cCK1Dy9CsQKXJSWezQiP2SIr0lGmWM2IND0YqENZXM1ULMz87Bg9S2EWtJ4R2hVav52r5dZ4s6gYWoFN5oU9KOguM3GRt-_5vd-H2Vo512xd7rjr4ImMD-Yl24URLH-LSWwQU84MED7cThc-m954S-hurBjCrhYYU4bj0_EdTZtqmgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=hG52MZw7yuhszxvTUUpLYGCvwVNSR1EYEnaxptkUAT23FXhvU9uH-7KKkVkDUyxCPbWg6KC7LwinTAXbWDOZZbwQZNAMFV_4kIDcK4wWkfvzIg1BJsBqvXE1w2ss51dbGVySm_LnbjgV8TucoZ_DKo82_DDIOXJlD_zlW3cCK1Dy9CsQKXJSWezQiP2SIr0lGmWM2IND0YqENZXM1ULMz87Bg9S2EWtJ4R2hVav52r5dZ4s6gYWoFN5oU9KOguM3GRt-_5vd-H2Vo512xd7rjr4ImMD-Yl24URLH-LSWwQU84MED7cThc-m954S-hurBjCrhYYU4bj0_EdTZtqmgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuDN1mWp2r9BMOAqno-Ug_56a80TZ0zpiFi4ps3JrJshSdoMT3gBFtxP-DFmfUVe0xJAObXb_YGTe-Ga_91x2Vh_q2Swsmb9qxfCW0Mq1bBUsYqzOJEsJpd4C5n7NgNf8JN2IbHUQc6CNtrKjByT5yXzYGpmIA2bDlLZdScZmcR8urA5J0bhwL2Fd1049jSR3cS-0GrIKAs1sEh6aFVGWtReEegM4l6ASHvxJ7LuWLEiMIta9HmJwxApRBpbMmsMc6UvkEkVsOJX1NOv8ZlCsluQpwI_Q6rUqz0WVrK_GkHv44ravdUZJWsMXfWwALCjhXz9PbA7_BYf-wopeUB8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=r5PN-MlPXU1GTdyuruMZRx8HFCsa2jkKomdQOPhMNtINBZyxZ3iBKqWrqGW4Iq-6z-bEA0GGll0Ckk1lcfFxByV89-N6BjVjZGgeJ5qvAGbnihTguiGYGr10vhU_oLMFR_f7gz-OWK-qhqSwAwhjvGdfmI2Aa9N_rMou_pWI7eJiPyy4yjWmTDeUaCMZmh3wLtIji4s5JOtMDJsbzEx-80qH-O1mBDt795l7y5D4HmCa-2MFVr8okk_Abn-v2Fvpjxc-PQqiQmoE3bRJ2djE7m9ZWFv8qE6Q__cWHjv0wpFglPU6AnGrXkhuPaUsWf2kgi1xoUR4BjuDewHY8uZMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=r5PN-MlPXU1GTdyuruMZRx8HFCsa2jkKomdQOPhMNtINBZyxZ3iBKqWrqGW4Iq-6z-bEA0GGll0Ckk1lcfFxByV89-N6BjVjZGgeJ5qvAGbnihTguiGYGr10vhU_oLMFR_f7gz-OWK-qhqSwAwhjvGdfmI2Aa9N_rMou_pWI7eJiPyy4yjWmTDeUaCMZmh3wLtIji4s5JOtMDJsbzEx-80qH-O1mBDt795l7y5D4HmCa-2MFVr8okk_Abn-v2Fvpjxc-PQqiQmoE3bRJ2djE7m9ZWFv8qE6Q__cWHjv0wpFglPU6AnGrXkhuPaUsWf2kgi1xoUR4BjuDewHY8uZMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ZHjMzqyklGFB61GupPvvp3zbeFHtDXgbirQCWv-W8s7pDXgZt7FJXZ9L5myyCRYEPHuuEYLSudQHZD3oQdGKWWRNnNsTWyMBZWwtP8x-Nr2ttFaTYl-jUxN0p022EJ-H7KOFkYQDdPHB6VN4ubJEUDluR91DYRranbuoQdGDFFwWim3HKXwupCj0eYfUiAchhotPv0vqCjLhSuM76DmYqKd6CQf_vYFI1byoxK9p0pxYkZXl1KX4giV7TwNTFyMqPpU-QdUa_Rwz9zuxm8fGTjCBMidWd8_TciTpWyLRWcCNr1KH16QfJsmRieJL68NrA0MgACUApJ7O8xWS9o5l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ZHjMzqyklGFB61GupPvvp3zbeFHtDXgbirQCWv-W8s7pDXgZt7FJXZ9L5myyCRYEPHuuEYLSudQHZD3oQdGKWWRNnNsTWyMBZWwtP8x-Nr2ttFaTYl-jUxN0p022EJ-H7KOFkYQDdPHB6VN4ubJEUDluR91DYRranbuoQdGDFFwWim3HKXwupCj0eYfUiAchhotPv0vqCjLhSuM76DmYqKd6CQf_vYFI1byoxK9p0pxYkZXl1KX4giV7TwNTFyMqPpU-QdUa_Rwz9zuxm8fGTjCBMidWd8_TciTpWyLRWcCNr1KH16QfJsmRieJL68NrA0MgACUApJ7O8xWS9o5l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcUcCQhKA3Jm8Z0Fa5MqgAVn4k0m3fKBPHrnz5QZc_GRCi2fd7l2kWVU9XD3_48_BHbs87IHmfrxl-m_-GIe7-sMiIVuqBqwYMK1suV2--JeP5105pFUtiM6fhd0qn938Kq-rutniqy0ysrt7kGPRmuplU3MhVVZNDCeW3yahrQ8q0xqWDdJKDa5kEe2Lay23LYVjL_TWiOA3_6dAtMA5PgUfT5qqyqshmGQaxIRSFYuQke82DVJHb9hOwnqiDT5BRkC0ItY5ZCJFxrG6MBKCMTBwrYr7gnYzBIo1GNvVlN6gunk_zs6UYGj9xII4--J2DtvCrJmshA8mulL09QA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4Pa6Uu9Qh9-YS8fi6-9Iz9bv4vwSiCrqs7A6e0gl92hEtTurF3Lzle2l9nscvUDKCAudO-O_kTQYcd49lGl2xRmKDfq7eWrVlvEV47MHnxFyYLeIzBbul0db7WIuq5d-cQ0Y_AssnICCCfc2tOaGA0Y7pj5dROGVZLT38Wi15oUiO1G6DC5nSChtrn2yE1w8mjSuw7DWihxVF3HyTS7ZS07gXELWOqqEKxAMNY8PQJMd2_M8L1FJQuLogU0_gdreO8wHJafmZreTp2wVpPiFGeiWmqOTdbClGcvMR4agN40qa45X18q1eQwDooxSuTRiONq6egWKI_pJ53MkW6G0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=REILhx1tY5npKSG_cF_3PcbZq6Vn_-DHhul3yOHAC5W9jgyXkbUpmNwgg_aHuADBxL42BE_pxqD2-YtjpanqnvVM3yG0mxpNGRrxICKaKVxVWT-L1aW8voW6PerNp6D8WUJ2Bj7uV4vbMRNvXCeMOCJlHV_XSXAltIq70ShB_7PS1kCUtO0B3tTwTGutpLvgeYRx-_zXCjwC1zr1-UuNOxB4n5Mndw3JvMBGF6N_yHTsCG-dPBdSYUvxTYTkVovEXfklnGMMeARt2zHwEgJmlICRrEJALLI6zX9FFOFmON6uOC5FXzLzH8EwR-dadWFqIWvGSJMpaxK-nFrMSUfOYX_GrbPfVJv5INmMLtOAl55tGI8HO0XO8aJJkT9xM8Qe0WG7BIjNne99OZD8pU81cVL_JmBkkaNn69bpciMVOb7BC-vTFsoIvK7pcu53Smk0VVQJ7NsZMnRb4mP-wfPSidfyqErMIr3jsAEarrftQ2uVdjnn5PXsYo2VG6DJIK_TwvNw4uWOzxM1rpLiGW_r64FfFoJK8k4P2xc0-EenCXzr3tkpkim482QUyx9KucXOe6nLEbK4T1C-4WmdakkMuCw-iOChP5aYj4HkvYSO7xhkkm0AMBvK9vMWO0n5G_7Q-M4oc1e1CyRM7Xlmt7Car1PLhd7bDyUxWA3wwD3i2w0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=REILhx1tY5npKSG_cF_3PcbZq6Vn_-DHhul3yOHAC5W9jgyXkbUpmNwgg_aHuADBxL42BE_pxqD2-YtjpanqnvVM3yG0mxpNGRrxICKaKVxVWT-L1aW8voW6PerNp6D8WUJ2Bj7uV4vbMRNvXCeMOCJlHV_XSXAltIq70ShB_7PS1kCUtO0B3tTwTGutpLvgeYRx-_zXCjwC1zr1-UuNOxB4n5Mndw3JvMBGF6N_yHTsCG-dPBdSYUvxTYTkVovEXfklnGMMeARt2zHwEgJmlICRrEJALLI6zX9FFOFmON6uOC5FXzLzH8EwR-dadWFqIWvGSJMpaxK-nFrMSUfOYX_GrbPfVJv5INmMLtOAl55tGI8HO0XO8aJJkT9xM8Qe0WG7BIjNne99OZD8pU81cVL_JmBkkaNn69bpciMVOb7BC-vTFsoIvK7pcu53Smk0VVQJ7NsZMnRb4mP-wfPSidfyqErMIr3jsAEarrftQ2uVdjnn5PXsYo2VG6DJIK_TwvNw4uWOzxM1rpLiGW_r64FfFoJK8k4P2xc0-EenCXzr3tkpkim482QUyx9KucXOe6nLEbK4T1C-4WmdakkMuCw-iOChP5aYj4HkvYSO7xhkkm0AMBvK9vMWO0n5G_7Q-M4oc1e1CyRM7Xlmt7Car1PLhd7bDyUxWA3wwD3i2w0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Y9RM3xWcVxdNctMg30nxj7HHh70pYEamtClA7mUPoSupOvJIf2juzqEkx21Yi8h_4RGQ-z3YTNcBLhyyxLzdFRhmQ_1T6Xno0nUdToKsJ-7R-uFnp-OXtChtQAcPPTau_UZMJYWrSBkoQvGSGPYoABxPxq0HBmtJrtsIsJbeI_YtKAAx_mPq-ezUZHiWIkPkmJZMsNa-Pz0UD972u8eZ7vD7FpjaEI21Y2il-vSlSjiMK5r7AnMp6UNIBaSoghzRQ5FrMF5ruY0SAiYbAZwSH5HGywD8bokafPXBOTtJgEByMuvgLkivMEy97s_xPFNoFi8U1po8g3-SmdcsSrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cAfLI0pU-WWP_nhgT7CEA3cNSL5f4oTsJ2yBMQR1VGUP_qMe_FzkCDjoYN62zavIE5lmAVdfhLQQA88VRXt4dfsORM9rl1mbgjxwcJrRNSrAakNvyqF1LAoA3RbXcr3wN4OwpYW3FMH6eQKJ_c-G0sIGrGauAjSRtDUrKaW1oMnFnTH5mKH_8nqsKEVSOzWenOo6SLDykKI0Aacsf8tbHeM4eTw74ZNfcH0LoL7SgbgPZTMKqQ-9WRPEuAINAfEa_82OZz1F3iEwv4tLgx_KZ2fQLRAfMKoAOY9vQKJ8cjHwFgR8NRQlbpD78UFuTSPnWNMX5j9mZM7vGdS2DKLRJUpC3hUqBI1bpVemc4NABlYBmd4qTGrgMKtDQF8GwbvM96kib_Z9Hl5yFDbACZ7IkzMYO4Ag9rQhaF9MJ7M1I6zGrw7a3PXVVENuoBbdUroy1Bb3ANoGGxPMsDacXdX8P2a4aKZhuTfpDDSod1pWeHkuhUCMaI2ATSMDa4QAmgAtJFBWqWDFQxLqvJ3RESNfAxFu-JFlJE9_QJC-RJhp2pF-6gAkvNJYHuOCmqsmWvmBCzrop98FfwJmmir6Y-idIlX4nSJ8qRiGLAoIo9smsd9feZw1YoeUl3suMb_bSWxsPDVD_aXdiyhBqe8PMKKxTE2e1Z6qr3-2zN-loiL8WNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cAfLI0pU-WWP_nhgT7CEA3cNSL5f4oTsJ2yBMQR1VGUP_qMe_FzkCDjoYN62zavIE5lmAVdfhLQQA88VRXt4dfsORM9rl1mbgjxwcJrRNSrAakNvyqF1LAoA3RbXcr3wN4OwpYW3FMH6eQKJ_c-G0sIGrGauAjSRtDUrKaW1oMnFnTH5mKH_8nqsKEVSOzWenOo6SLDykKI0Aacsf8tbHeM4eTw74ZNfcH0LoL7SgbgPZTMKqQ-9WRPEuAINAfEa_82OZz1F3iEwv4tLgx_KZ2fQLRAfMKoAOY9vQKJ8cjHwFgR8NRQlbpD78UFuTSPnWNMX5j9mZM7vGdS2DKLRJUpC3hUqBI1bpVemc4NABlYBmd4qTGrgMKtDQF8GwbvM96kib_Z9Hl5yFDbACZ7IkzMYO4Ag9rQhaF9MJ7M1I6zGrw7a3PXVVENuoBbdUroy1Bb3ANoGGxPMsDacXdX8P2a4aKZhuTfpDDSod1pWeHkuhUCMaI2ATSMDa4QAmgAtJFBWqWDFQxLqvJ3RESNfAxFu-JFlJE9_QJC-RJhp2pF-6gAkvNJYHuOCmqsmWvmBCzrop98FfwJmmir6Y-idIlX4nSJ8qRiGLAoIo9smsd9feZw1YoeUl3suMb_bSWxsPDVD_aXdiyhBqe8PMKKxTE2e1Z6qr3-2zN-loiL8WNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVlTM_DHK7QPnHBkPvF3t3xwKkfWzQrJA7j_iCw6zOMVkBYtoslRDdpcHQ2fvkZdRwARMdiRr48COcqU1mxpVONyI8XDlzo6RnkfMraIGk2MXoUvoDzBJ7KJzYepnsHsCRXdXUzqc-nvH5LRuoAqHfRanF6YDeSYGWRxqESX--tuGD9hjlDjGA60l992yM4RLFlMIRuWvoYO-63P_KurPC79WIsZIpPLEIrd8USJTcouwDbZrKwXFkU5l-AUq7gl6TJ64rT2cYo6k72pJ_yUShHr8F1LQMBM27NXokagBvd5R3-plyJfuoLmQlsB8A6B-vofy_VixXlMjeaFrOizPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMjgRc8FnJDulXSG3JG5L0WQCQn4l6Vv0GS1g9RBkgMkdpNaizXoxq_BVgiTAPYZvRbtZHV9VHDTvxz8_RPUSZVQsNYyvKyk_LHUG64SyKGNoLORzPksgi8ruosxocXS3-g_8SILptpSaSU9CWjCz8sanH-Gmd_F2iCSYdNfu42Es4xbKOQzetHkIkpnF2Qej6Ys9GQhjV3pDRKZuEtVuJrnvLPis-K_wyOnLsd5guU0Mh8gP7r9lDn_wpSgISeECUZ1V6AxxoUANhTFYTqEUca_WzGdxGCQ-xTNAB8w5AXTOXa8Z6wjTAp60KSE0HEDiYxhmKWn57uTlPqrcMh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTALzsbJS2oAW29OzAbBUwxQVVkFyvq-m1b2aXG4RLPXeVmkijv3U3yl_aLpcCG6qMVplCqE-UCpVkGoUk04X0Xnbr-ZHbNsROK7ow3pb5NSO0DeBkTPCRif60uB9b9CAOvc5wO63HZJC5iNRZ2mn_NSwGt8gvj1rRjP8N57mEDvtr-Qslis56KTymZQSew6kZ_Y2lIkZOcMXhm7SfHJoiQeBWuol6UFEeqRrSQxqGVE3RiI5F4vlbrQ8ZlYqE9cz1kSUgS1uPD6fewl-E9NxwlNdixY-3EuhxPmZC_2ihSNwMqpByjBkhPbLiQ0V0IGDoZZ7XKkl8Gk2-4AighCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
