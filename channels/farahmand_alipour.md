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
<img src="https://cdn4.telesco.pe/file/SmdkMa1BE8t-Z0kToAMQMT78zqVPV30_jblgNgVlf4xti6PJfvjM5BkXTuySyMEzcjOZ0Yy2V-wpZc-incsQueR7TQjB_eO2_qltZ3XyRH7ZdCUQH6iCMfrpKeMeaCshh2Cp-UZTIVF8MicW61fTbRAWfIiGC5AR8sFyTe4QLsPF905sChdG5yF9Sheuui15ituDdO7_sCmgHLeT2LROHCvwHQ1_x_7T1U79HqjvnFwQtP1rKK9HR6TO_rUZjwLk7yuA3dJgVsLbL4A7T8gF8-mnX690I2L9WsIEZuCtgky2twYhOCgfMvsSeHrrOq6Bb6A0aHK1i82sTUEvwT-KTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
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
<div class="tg-footer">👁️ 502 · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpWCayyCDAcWeSRoAR-75XxigAGnv03rHykX05dJFvbJ6GNXLc-pYVME54ma_1VlicHZ0AwQc4gxuCMxFIN_YrZHninfH00q0QP1j_DRdD0rVoTmx1Ktx8gQJXnRT4Ez98XV70YgIjeKw8jpAfteTUR_HgdrWozt41aDh0lMRMZin_Y93Sxg2h8Yb-Wj9zd6PPz3oSuYWBtn9ICgJyx3cKIFW9QGmEjnaoBYLzWxv388PsgoQEJ2nI8-I1Pc3xHsHeav0-QtBK3Qq8OjeKv5MLcqO9MllLnadsnyXD0P6TbiRqZ0TUTPzRTEM6NwtarJlxZ9EtASKKbDCenqGkHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLiQ4FBokT3AOJ4itMQfY3E0ZLuauYCwXNfTRPZNjSzB2FoHYFw7lOXisV6DKzkhxKU7JOyyR0KnLMOQGTWqzXkJIkv5tpQBQtEfO0DkC4IRu55R3QAFtupFUc8QmDPtyASVZM0_OjUb1rXSnunjXUf97bHrgQ4W89t-MQGmVHiIS0W9LRqA11m9Oj8mhSTwcs26wkhqqgWjhIrCnQuOW6SCQqU1Y8b3z8OeDQW9MlcppnJYthWRjybNBdQRy9cNWyUPGMSFjSQZ7CPx_0OK0DHj727kZ5lvgS3_FArDk5hLqQhJL-pFXRM9lal9VANNNNqk6M5XQnB0pAUH2-cTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Kekk1TBEjUHrGh4-A6olldUW2Kg-rowRt5bkJkQpqkNndwAqlBdIzhZjqJZo5qgc9FCGTRNW2JZz3KJZpTTXzIbJwAi2G2JdPLZlLmnGHgwlIs1ZtdOnPxAfMuYHnSqLn-qs7DjkZ6nEtv8CwWY4Z9RDnyA18jeJZvbxhmUXDQ5L2hmNdlu_gwUIyd1dqa898ZSYRpt8epVgvZlrD6h5ZO_Cd3f2VpknHi3SJRJ51Zh4k6yVivYLs42xut4TuSOjWvW14LTjOKdhAhA_sPJwbuCqhTN_J2jigdI9isuIpjCsAnjMtC5p4GqlSY3EWIjbwiZH5Ycogz_YuFteJVDiQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Kekk1TBEjUHrGh4-A6olldUW2Kg-rowRt5bkJkQpqkNndwAqlBdIzhZjqJZo5qgc9FCGTRNW2JZz3KJZpTTXzIbJwAi2G2JdPLZlLmnGHgwlIs1ZtdOnPxAfMuYHnSqLn-qs7DjkZ6nEtv8CwWY4Z9RDnyA18jeJZvbxhmUXDQ5L2hmNdlu_gwUIyd1dqa898ZSYRpt8epVgvZlrD6h5ZO_Cd3f2VpknHi3SJRJ51Zh4k6yVivYLs42xut4TuSOjWvW14LTjOKdhAhA_sPJwbuCqhTN_J2jigdI9isuIpjCsAnjMtC5p4GqlSY3EWIjbwiZH5Ycogz_YuFteJVDiQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2sHxMrLdWhorBJ6_j1UIKDRu7PLefDuch3OUnZkuZhXrl9HeZZaakhM9zc2pmlUx6KBtNNV5mlzExpyDWRiAdMyKR2sUt0P99OSBo4nQgLG8ijg-ZVURWADd9KXl7lWyupLSb30GVnxkgw-p4vE5Yb0avXt5Wf5qcxg2cP9ZyEAN7IOZ3RePMeAEJr0JpIQtbOp_jPM_yvuOiuSz1EuFGtRP5UDzMKOe0cbZ6i1VK0JoG3AQBScXIE16y86wfPFVykuYSpbsDAFXPEMTtpyk7DErLnqui4RCVA8M1gFtWBddMmzEGMp559UGQMCxMpbbfS-e-_jrheY_OXtDRvctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mBfDFpgNQjAMMY__B2Rzi48s43A05zyZSDyU0WbQ53ebViyeMpklf_VOZNOoF0mdm8Sh0o9Uu18HL3XU9HmoASVg-cK5y5kK6I57I-jt2YHSMJhr66ZTj8FT207-CTFDt0dh0MHNEBphTuPRi0KIiy1j74ftECRoxLPIqHbSatssJ9UL0_UQ8MjD_2JFkIluEzqkrNCaS3gvVTPImnoF8yLXJRl6pj71S9dPI8ywjKf-ky77rEsFCPeJIor64blN9Gyrt_xBROxA_kU8cC2Yt_Db4icS2YaiGuZJQV-juwcPdGx6GBv2GZhsISxk8JDvrcqHWtAtZmB0zrqvHKFwMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=mBfDFpgNQjAMMY__B2Rzi48s43A05zyZSDyU0WbQ53ebViyeMpklf_VOZNOoF0mdm8Sh0o9Uu18HL3XU9HmoASVg-cK5y5kK6I57I-jt2YHSMJhr66ZTj8FT207-CTFDt0dh0MHNEBphTuPRi0KIiy1j74ftECRoxLPIqHbSatssJ9UL0_UQ8MjD_2JFkIluEzqkrNCaS3gvVTPImnoF8yLXJRl6pj71S9dPI8ywjKf-ky77rEsFCPeJIor64blN9Gyrt_xBROxA_kU8cC2Yt_Db4icS2YaiGuZJQV-juwcPdGx6GBv2GZhsISxk8JDvrcqHWtAtZmB0zrqvHKFwMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=E3d4sqYGjGgE6yU4MiJk0gETQbEypcbnkBR9gNQqn2HQGQPlqb2_tHWEOxVXwc4ixhnF9T7FdzPoUwC3RncpShUjol9jLuLzR3nb1S071bq5ttzCcWqBvFiCp0wFmQG8HyeKzT1XRgv-JkFGX0a4OBVMpiueui4DiGWCqUU-iQsLlsrQNGkZYaUejAFFk-1X6z6jMaKfTamTlogAMcOYjfXGI-qUHn78iV9hgAXG1tmMTZG2vffLMkGNCEtZctNXJ-a7vQSzUqk8gEnzuhxyOVSPYDMXmJAjsGfmN4x64ukUmgb547-Hgpl7QlZV0gNMl9Q3uJlvEy7Ajqhi_DIX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=E3d4sqYGjGgE6yU4MiJk0gETQbEypcbnkBR9gNQqn2HQGQPlqb2_tHWEOxVXwc4ixhnF9T7FdzPoUwC3RncpShUjol9jLuLzR3nb1S071bq5ttzCcWqBvFiCp0wFmQG8HyeKzT1XRgv-JkFGX0a4OBVMpiueui4DiGWCqUU-iQsLlsrQNGkZYaUejAFFk-1X6z6jMaKfTamTlogAMcOYjfXGI-qUHn78iV9hgAXG1tmMTZG2vffLMkGNCEtZctNXJ-a7vQSzUqk8gEnzuhxyOVSPYDMXmJAjsGfmN4x64ukUmgb547-Hgpl7QlZV0gNMl9Q3uJlvEy7Ajqhi_DIX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qK3RngWlUOXWjrqO5f46zNAUQNUsILOs8WxiMWZLq9TqvbBoi9HfEzR3Aw0gNc9e0piEfta3dl-nJ7a3lpSaHDt7Cu3IONzCCL8Y-cFl_V0oSV2UWEO3ETLbbxf_jrflvRkFzi1bgQ7lTxO1Qu_1CjPrNlnA4umKJiKAzRHrXBLZh2RjRlNhVgxskpfc-b61gnF5ped1aqF00kOtZthRz-l79n1saD9TZ9VkY4EbrTbXAJn58sDWYtvPZ4odl_CCCFsYIdKm_LduWB6v0pLb_RZNRHhDpyabeIQiP_LO3dkbGkiI3qqzPHLEdSkpySmk7j8APv_5J-fFc3BJSjeYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjMDqy8n2QjKuWK7BIu0mRt86fmXQ1A7HAWe-6obVJptk6XuoFGqL0I2lskftEQrcYsvi9o1yAlrkAtJFMF02vtx8yGp6Y9cC3O6TFNOK7THPFS1duPjVRV0_7ot9HRKyEFfmH0l6Oeu-V-MzY1oi_ce5Kd2LiSFQSNo6JXpUATLy5zagM5kJXo_4hD7YFT_4GJUa2Vm6yzvK5D0xmQRUpqlWb6XBr4wdaLUvP3BK6kEzoRGvOeFJ-skP0QrRjGpGgdG_bxlS4_X3HeqD0rjxGCVBrwLor4DSrQSSkrRrpqexwIRyIzi-jNgIs8Tsf8W6tJKR23Y6pBsIxavo27v5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rY0yGY8zrpal93N9EBh-EbeUd_NqXwCMk8Dso69Gk5-r9w_Vy8pQXVelbJE3Iz4r2yaV6QSlkF4VUl8zRTuV0owultrJIJJz__-AiphiJiPwHvgFHIAlkOHUyzRvtr3lbSqRt1hdp1sQJ3Aa_7owklXcWS_tKafDHstJ3bayubj-WEtxybeHKwyPznM71kqSrXN-tPdPNPGM3ETKf9jaYxTLYMzRFZk37bRDUxHxUGU26pO0mDECK0vJZyTpfh53fXwVRrRnnhQwJtR-vckCi3o6y6qv6e3CiHNHQa8duKTL-8F68lxeikM0X4U3DjJtqDTwqZ_v5P0pIYhAJ8uHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rY0yGY8zrpal93N9EBh-EbeUd_NqXwCMk8Dso69Gk5-r9w_Vy8pQXVelbJE3Iz4r2yaV6QSlkF4VUl8zRTuV0owultrJIJJz__-AiphiJiPwHvgFHIAlkOHUyzRvtr3lbSqRt1hdp1sQJ3Aa_7owklXcWS_tKafDHstJ3bayubj-WEtxybeHKwyPznM71kqSrXN-tPdPNPGM3ETKf9jaYxTLYMzRFZk37bRDUxHxUGU26pO0mDECK0vJZyTpfh53fXwVRrRnnhQwJtR-vckCi3o6y6qv6e3CiHNHQa8duKTL-8F68lxeikM0X4U3DjJtqDTwqZ_v5P0pIYhAJ8uHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWmHIXDFaNLdfn_jvf_MVd6GvKHLJx4IjyDiIHPtgaXeZ6bC5kqSibvFgVtl1Ht-7pifPpweT4Nygd8WWNQn_o1PLNmw6CL4Odj8iXvWp-isxOOxD8OjNaJ6IKaEsoOPJZC1JzkLFc-0bpm6hO4SP032itSAFthEyZViJqKqkvZ6tbUkiwRY_jaI4RDHIaKOHM4XHIhV1kPuYhWraEdHHGEd_42PSDudBdw31s-weKoSwpYqviSp5-u1XxjxDSx1pIGyKPjRP1YQdcyZfbZ_lxBOyUSYWsvMjFYit4kUo_30TfumDpQFCNaRsiqNHkqWbscaqH0v8w7YIpx_7uWfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuVRFJ3UIEuKGRcYOYun6pPLrVw4T--vBFDE5aKDgWROQX2uEB-YBC2Wlz8kpK0q-cGmf16Le2pB9EZqShLjw1N7_PboXHl71mI4Tcw9AisLgWXdQUxpI9ddwGuLlabLgFgP8zg-FB0NJnBMqIamwQFxeP54u-okLwVF41fkcRo3j4bachiMVQx8ZXr5tZFBf6coaV8vg9DiGJpSFkG3ORRUTKMeXgPTlm0cSBJNuNFRjxqikMe_4Auy2UtXbIPjJtYrW1mzJIiAO7b7PUQDYkKh2pMTL_hTzctpNjEvg1PPCAtkTYdb9fSnyWHeOR1adchZY_ZaBF6O7ewg1NUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkbKnDfQPYF36BDhCt2E_iDHvl4unFhitNPLZKZXaxj7b_O-XjOw_WZWuLEnQbGheReuVyvsQeWBGOcNdIKJW-hM-pn6CC5wBvTQEAhUvddQL2P_5rz5a_fkHzZ1Qga9t3auwAoEmzog9u5MJS993nsGdMzPHkaBrj4mYVFUlyuNoqpI2pKEVVvMbB5q3xKIC_ydrQsBzR_yq1fTrrPrqlBeQz3YrdK9LrNCWpg1ILX-wK49EgYoNFqBNUYLwgLxfQkxeZSjfPFryMhHahM-lX_i4_zQI71Ijtk3jgZm1httwnIWkhSHzPaMlTYiaCEm1ZVRXZGdcgywa2dbQG0J8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=J5zU99Gsa31pmbIdAT2VsYcd_hYNGexo4wtNJgQuXYiRFcvm_73mzKzaZEaDjXgMtsN8XbaVAZ4fWoI7x-vJhodBvENqPwIQ3YPca4kj6yIzwx-ZB0q03LUE_EwSALve0Nv7H_FPUY5B3agkzZ6msgyZ4IRyDFeQFglz2PpTKUwhp1JwK4n2qJnJNauE7PsUf7gslbQVJK-r0YDCZLRTrmOJQXkiV3kfqFrMlpyl2f6zLcTyFhM0jDDNRmsxQNCqcOM0aW6n2ywHWgMPQ3-k1Fe3XK7M9lj6ANSk8OWkHylsLpx9-czGwZl2SNcvu2m4M5f9YqoC2HyyfgnQ4uHPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=J5zU99Gsa31pmbIdAT2VsYcd_hYNGexo4wtNJgQuXYiRFcvm_73mzKzaZEaDjXgMtsN8XbaVAZ4fWoI7x-vJhodBvENqPwIQ3YPca4kj6yIzwx-ZB0q03LUE_EwSALve0Nv7H_FPUY5B3agkzZ6msgyZ4IRyDFeQFglz2PpTKUwhp1JwK4n2qJnJNauE7PsUf7gslbQVJK-r0YDCZLRTrmOJQXkiV3kfqFrMlpyl2f6zLcTyFhM0jDDNRmsxQNCqcOM0aW6n2ywHWgMPQ3-k1Fe3XK7M9lj6ANSk8OWkHylsLpx9-czGwZl2SNcvu2m4M5f9YqoC2HyyfgnQ4uHPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Eyn_shncrcvkGkVc9F2azmilYeg-Jz1zTaLG3EpFHX9EbTMKhiDKIgVPmzfoywtnRPs5ADb5KCinhUOyoYW0Ib-dCtON9YqdCs5voUEBRY0m5aokRHRV8Wtt9pXG7IoRQtcRcDL8GwDZyEPmUbpoXIDF2BA3fsvwg49R6xj5OeYVYaFVoITlBxlfFZQ9y4KBxM2oEfw-je00WtO6Dg2dfhq9JmBP3Mi-fdzRqjerw18RrNKfUMS459MVYCkw2F_1lPI-ZYJBa5Q7Awo8oVvwvlD5i8f0xN5Dk689su3fooTU0QmqNG9ly2FvgPqN-TdtOBEuVvQjP4KuiJWj3lo_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Eyn_shncrcvkGkVc9F2azmilYeg-Jz1zTaLG3EpFHX9EbTMKhiDKIgVPmzfoywtnRPs5ADb5KCinhUOyoYW0Ib-dCtON9YqdCs5voUEBRY0m5aokRHRV8Wtt9pXG7IoRQtcRcDL8GwDZyEPmUbpoXIDF2BA3fsvwg49R6xj5OeYVYaFVoITlBxlfFZQ9y4KBxM2oEfw-je00WtO6Dg2dfhq9JmBP3Mi-fdzRqjerw18RrNKfUMS459MVYCkw2F_1lPI-ZYJBa5Q7Awo8oVvwvlD5i8f0xN5Dk689su3fooTU0QmqNG9ly2FvgPqN-TdtOBEuVvQjP4KuiJWj3lo_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Y0ITCT3bFcr3rd7_f_QAl5S2aRg-b-jMAxBlrocKWCkgJxPLcS3eR3_5-I-SxTSM2do9JngIrvl2wq1BCZRdjKMNuBz8JlBSeqQrYB_rzuPca_9kHXtN-F-hB7lE02dV0crmEYZP4vTBQw2Q_cQ2bcYxZiizrPaRQ4lTyKHkNnJ7ROWOZbXiNpOJyrx33DiFNnaBmsRMwDBpqikY2RfOLVyvbfhfn6o7Ut8RxU9f8pHLrUPzuUm2uhPTXKMIdtMDHWtzaLm9TN8jxJf_naMuOIANuShz8vmQfgixx5G8VLqDDGkmCek0bAlolqmFd4TEjFQczD5okYERjl4ic-XexrkXkTIneAO-QkcC6KL48u6qxm4ZwtxJ6MpvQhrL5vCU97YCdqnqSsX-5N1UAHXCcThjsfKdd46nwQuZiZ_sv88Lywe-U1vggJxdk0uwCIGCYF9hBQAja36yKb-9Z69t0Z8ErfeAoYCWSj3O6P7oojgkhSJxFuaBa2H0XCcp8SMSbvoxIuTJqJLltgnHH7lLJg72rP1dtrHVLn8pea6h4XiSYu50NylKSuTBEGRzkoeCynsPgxa2GrRmq2VQrf2CfPDPjKs5qd8hDh_dHS33-R3EsrzQ95gWVnFSl0iMtP2m34yANajeFswYxWFzdYoNwbxVnqZPCa_-8X1IrtxUMA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Y0ITCT3bFcr3rd7_f_QAl5S2aRg-b-jMAxBlrocKWCkgJxPLcS3eR3_5-I-SxTSM2do9JngIrvl2wq1BCZRdjKMNuBz8JlBSeqQrYB_rzuPca_9kHXtN-F-hB7lE02dV0crmEYZP4vTBQw2Q_cQ2bcYxZiizrPaRQ4lTyKHkNnJ7ROWOZbXiNpOJyrx33DiFNnaBmsRMwDBpqikY2RfOLVyvbfhfn6o7Ut8RxU9f8pHLrUPzuUm2uhPTXKMIdtMDHWtzaLm9TN8jxJf_naMuOIANuShz8vmQfgixx5G8VLqDDGkmCek0bAlolqmFd4TEjFQczD5okYERjl4ic-XexrkXkTIneAO-QkcC6KL48u6qxm4ZwtxJ6MpvQhrL5vCU97YCdqnqSsX-5N1UAHXCcThjsfKdd46nwQuZiZ_sv88Lywe-U1vggJxdk0uwCIGCYF9hBQAja36yKb-9Z69t0Z8ErfeAoYCWSj3O6P7oojgkhSJxFuaBa2H0XCcp8SMSbvoxIuTJqJLltgnHH7lLJg72rP1dtrHVLn8pea6h4XiSYu50NylKSuTBEGRzkoeCynsPgxa2GrRmq2VQrf2CfPDPjKs5qd8hDh_dHS33-R3EsrzQ95gWVnFSl0iMtP2m34yANajeFswYxWFzdYoNwbxVnqZPCa_-8X1IrtxUMA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=EUi8AVBz-dFMCifeI5DxRNBEGqvNIu35KvgzaZ0J1zeQCHr7DwuvlRxUASyF6YdTzgHXW0bJPsIZMu6Cyh12kUho3uB8QLYVNu5YlItz-voXy0abypkA4giSK3UIThPWExGFM5qAzvTqDgeefFGyBrcW7GARtWvuIBGF5w5IwILwSA0tn8Wi2DBcB5M94ED4H6wtvKn7ehyv14h4i8Q1FPfuEZI7e4HpoLawW9Fah3VTXYq1dd37W8opPR2Ado-FoUqk9DPhSR8IOQulXkap9hZqWCcGd9yqhhQKiJZBbeFmAetiuXhvgpuacoa5IgRQ4P2sbr6yRRA4SrDpaJhfGmzeRyKVJxsd6shzqd6f33mdmsyENU7ZGrvdx5tvukvpWGu1-N-74G_a3Hxo5j2bUqwHX1ilKfMNjwqh-wclwZjWtgFRTzgjUQOVMqi1H-SMHzJWQ2yyE6fuIQKBUBKhKNUz0KBxSl24OZScSlGnl-fVMKYV1EAceDneaLCgEJZ9No4TAvUaocOfkj0xnl6a8TBEug0gH65tjrWooNcZin-F_qCOU0WnpvTSvS0FogDwLwEI65PKhaybyGaEJDVUgLjLELESmYEBsPiy_AVp2VAlDGX9NP0a_LU6QGRpPNFUVE2O6qPR24Ywjwl78XV45D6xocvymkyafCQTTa1OgdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=EUi8AVBz-dFMCifeI5DxRNBEGqvNIu35KvgzaZ0J1zeQCHr7DwuvlRxUASyF6YdTzgHXW0bJPsIZMu6Cyh12kUho3uB8QLYVNu5YlItz-voXy0abypkA4giSK3UIThPWExGFM5qAzvTqDgeefFGyBrcW7GARtWvuIBGF5w5IwILwSA0tn8Wi2DBcB5M94ED4H6wtvKn7ehyv14h4i8Q1FPfuEZI7e4HpoLawW9Fah3VTXYq1dd37W8opPR2Ado-FoUqk9DPhSR8IOQulXkap9hZqWCcGd9yqhhQKiJZBbeFmAetiuXhvgpuacoa5IgRQ4P2sbr6yRRA4SrDpaJhfGmzeRyKVJxsd6shzqd6f33mdmsyENU7ZGrvdx5tvukvpWGu1-N-74G_a3Hxo5j2bUqwHX1ilKfMNjwqh-wclwZjWtgFRTzgjUQOVMqi1H-SMHzJWQ2yyE6fuIQKBUBKhKNUz0KBxSl24OZScSlGnl-fVMKYV1EAceDneaLCgEJZ9No4TAvUaocOfkj0xnl6a8TBEug0gH65tjrWooNcZin-F_qCOU0WnpvTSvS0FogDwLwEI65PKhaybyGaEJDVUgLjLELESmYEBsPiy_AVp2VAlDGX9NP0a_LU6QGRpPNFUVE2O6qPR24Ywjwl78XV45D6xocvymkyafCQTTa1OgdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=b1VkysTEcptByspU9FHFVkCu02_QVKai59mCDmQXYDu1VQKloKMZI6mBnjjtTQCW-GX3nOm7CRjYQJCgJTPg6T4xlFNH80dxmEHo0C10f-h1I9yF45yV7FEc_M5xUUoRAU5NbyQJN8c7eZqqyaOZm9kMGR7D7rfP5rqu4S7s6JxTGJY5qLauRxbLpZVzE-HmJyVPQ_r7Nfi1Pd3NwGbkpjUmglDJZF65_i3H0ojdEElvzpPR0IcDrcVaAHkI4lh0TfFXryJzrtxhocnmxYk7iFvsjV2pWNF-kgQxetSac8Z66pVYHOaTzg16cwHyDv3GH8f7D7mPyrAlFiggdWU1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=b1VkysTEcptByspU9FHFVkCu02_QVKai59mCDmQXYDu1VQKloKMZI6mBnjjtTQCW-GX3nOm7CRjYQJCgJTPg6T4xlFNH80dxmEHo0C10f-h1I9yF45yV7FEc_M5xUUoRAU5NbyQJN8c7eZqqyaOZm9kMGR7D7rfP5rqu4S7s6JxTGJY5qLauRxbLpZVzE-HmJyVPQ_r7Nfi1Pd3NwGbkpjUmglDJZF65_i3H0ojdEElvzpPR0IcDrcVaAHkI4lh0TfFXryJzrtxhocnmxYk7iFvsjV2pWNF-kgQxetSac8Z66pVYHOaTzg16cwHyDv3GH8f7D7mPyrAlFiggdWU1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOSTEoHZG9vAySoBVfeLPJVZRViAMm_nplEpZInv29OoWpQU-ZIcUQmq89FvpYqMED3GXE-v7qt5euIdkgbDSxkCrgDQFgZTizIiFUCmCPVWnHD41VmxRTZZ-3iajxlYs6weaJC0L3Q2xIizLmfrDpXJk71YkO5TcFpeoFTdZHEVI_dYp8VjFuMoP9MtPfyMkI1R5XDz__-4OSm2bWjjZ3efemKCqyinae5QwW1hQizagxECLjKQBSTTJPzial8CXVImngKxkuNlOgTCYS9R0mD_C4ojCEKLZMbAdZV5N54TOOafBID02-YxPiDGdCT9ncB6NF4sp051l8ibAd_VaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bMh0cy0hoZdieGGMkj7LgwpcwmARCtHumwU-u7mO-rFTTT47SKU9mI9B0Zp5_OeLoIQmu-RWqXdFAPzzyX69SSOcendIjHPKKqK_kW3FnK7o7_LnfePlEZ99sy3VC997khVT6EPIaP_PSH2mUeFs7rbC0ICmp8XlQMTQ8zHGRD-41BdpkSUWZxI99fd-9JpOuVvFZcOtt6AsT16aRIbkSNTdt40Ti6GWmuMoH3Pjhy-YpZRlVLCjqNH3kz_OtVYrbJazWlSnJ3OM1Vd6mlFu63CbewGeYDzq5JuiGTD2BVjQYgBG7kRy8omZomycjQDnQmV5D3OIy4jm-zi-F_fQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bMh0cy0hoZdieGGMkj7LgwpcwmARCtHumwU-u7mO-rFTTT47SKU9mI9B0Zp5_OeLoIQmu-RWqXdFAPzzyX69SSOcendIjHPKKqK_kW3FnK7o7_LnfePlEZ99sy3VC997khVT6EPIaP_PSH2mUeFs7rbC0ICmp8XlQMTQ8zHGRD-41BdpkSUWZxI99fd-9JpOuVvFZcOtt6AsT16aRIbkSNTdt40Ti6GWmuMoH3Pjhy-YpZRlVLCjqNH3kz_OtVYrbJazWlSnJ3OM1Vd6mlFu63CbewGeYDzq5JuiGTD2BVjQYgBG7kRy8omZomycjQDnQmV5D3OIy4jm-zi-F_fQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=mfIN10RswoZ5BcUs5uNQJWYEKSrF24eg00n1GZJY6TQeayvkNFqcNbRRPcR22Opt6WPothHO9S-nUcc6EH13UXnMS7vByPpXStFpeHGjaJCI5pccirtTMxrCHGWesj3-gXUaPV9ALw3ghCplSzXXVUhhbcu1AOA2OcJYNb8cmks_4m_k8yXpSbWA-MnlIYUfRZAqFEwINjoLwLBCzX1mvuEy_Ip7dzlzihBofu_AHl2Wqjhend_JId1pTpq4AZmMAraBg47tLlWljRJmNdQaHTvZMGDqXH90ub8LBzEZ0LBR3MMx6qXiqscOiZZQu3tL8Y0myex8fcf6qMVOix3Jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=mfIN10RswoZ5BcUs5uNQJWYEKSrF24eg00n1GZJY6TQeayvkNFqcNbRRPcR22Opt6WPothHO9S-nUcc6EH13UXnMS7vByPpXStFpeHGjaJCI5pccirtTMxrCHGWesj3-gXUaPV9ALw3ghCplSzXXVUhhbcu1AOA2OcJYNb8cmks_4m_k8yXpSbWA-MnlIYUfRZAqFEwINjoLwLBCzX1mvuEy_Ip7dzlzihBofu_AHl2Wqjhend_JId1pTpq4AZmMAraBg47tLlWljRJmNdQaHTvZMGDqXH90ub8LBzEZ0LBR3MMx6qXiqscOiZZQu3tL8Y0myex8fcf6qMVOix3Jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am9It-3Ak9Qb6DtQq7WpuCaWixyx_mj9VWt2TwEAnwwmX41Zrk_x0aVXL7vCcruZiBD9VygAFWoNwH5d5y-WXsuVjwsNa2OiM35AxUtl6EtB4imrAyWZ5k4fUoTOsPrV2NlRtzQvLQC7l8wdNLl3G405QETtCBcse19auoN5pf3LtWIHv8MmZgbJrSH6VqfUqeeFUQsEf2WBXnq59W1pD1XWzC750K1a24TgmlUYw8r7Wzsvm9e5McOlsm5qWBq8ObUFg8uFOwQzJHxFRbqm4cCbdUdu_FaQ0eJa0K_b6rgUirE2u6ttH2BUjlDrTCYsZcK21TZ3dHRBwKpttyxAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5SP868ysXThkVGX2XZMm4DjBVqzs6Ijbs0lU4Xgeu1asxC031NC44YX8cPyTzP5S7ZntHkwkJfXK_NVNqdoKb_KrjFjltNrExMLtBQ9q0EIbgK-OH7UZBKC7YlFA_Xmf7S7b6BwuThqofCsl2ltYc02O0ckUdoB_bRuTz2qnVpm5q3XS6L6cfnsL6JnV5f03R1bPf6JBQJDm3RH1dY5HqPo4gZdt89klpVs9TCjQt6Uteo68E6cd4rTOKco1cHvTwH7Hfi17oHBcnxehBhMnuFPl3PtvXRY7sDEpgdwZKrWTmkKW0I85N9U8M2WMDSN1binGSzHiOEPOl5YOEDc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFVozv0DaRCM3urHqdrByK6DbLuEQEQ70FFUF3qjx00_1sVQudITiAg8tlsdYTCo2ztYVOW8NTGr55Y89X8tU7-lWSl5Q0Ofvm-9v2_4fj26SkkQNiXAr3A47LYj-bs4vwNW6b8Arno4s20314UjjRESEHo9wikFL1gDmsgIBqFTV_K8SamSrn22E5CHJP4x3kAhtsMGL_PmzkBRHHBBB_bKRxAEjNg3v8lncXJodwBBdjiJb2f6yeZSn2dbQ_Nr47Nucw51xDPSYaDGWCuxvNNBccTpKtsJa1GrW600vUnYDSzSPIu36arVSt3ty9MQ5oW-j48ir-3LmOwiqAmCAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niPSEIA79-ls9HqGz2lIo-LvHMWQpFRcim0I-Gmn8Un1G7tH5sccZ3UrVl8a7dYqqGsjoAx2e3mgjfgwqxiNdPaRh1b6ds0M-e7gGy7Y7ralB0mmobjC4VETSVwGabpFWjZI7Ln48jj4RS1JSGPESBeSCBQcX2in6FHIGYQV-io7iDmzBaxUyV6OMn2Hw5J45PNvDNTsl0lYob_nklASSXVnbfnnLQIwT66fKVleg_cDTs4grcn0Bsjysrdz2KqaCSeeZZbkeLCXLcw_rmV291XwEMPZePD_47uG8dGNXQ0MhSl44TEWvO7i9SX466HQ7iS6ZRlwp6LoKanA0Kllfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brio_9ezqYV9-j3DzDcwl5VP8sl6yIO74qdIHOI0O5SLZJT56cjPX-1fTvz-SrZF1qY2-R286H2oU_GoqB-99YaZtX6ucZTcJNFoV82zNpHk4tDX26jyqHUmsZBIFb3blU0hIRNgiILvOdOPXIpJ6rCH4vZ3AZnAMofMWhR78kJwjy9wSPYGz36CFrDcZ0KJuGVj4lW76p8-E5OBUWwKnh2j_U893F8snZzNvDZFlIPf0d0Fg1AXvDDR0FqORk-PHkj4pbtjp3F3Ih6So9y1KEED6AsBp5T7fJ-fjSD1hVFuMhl_k3TWgR_-1f5ZP-d7NMYMX5nrP2oKrM-GDYyxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1UJOySrI84PIhdsk1YcpiZQwq-xFe7LOeZd-Wm6uCesqvaATjouzomc1Hukc6j0QkdXOdb0lWAyERdE5JxtBoRrO-rpb-UOt_qnstlrY06I2wsi6TEq3msYWClMfeKD8iaarMSzF6JPJM-x1MOuLkrGqNWlqEMC6HKTm3IMAh-EdGFtSrzDiUc4_CsKbDcHPs-34sBho0oNjP7xwMDw5M3uWYRNWHn8arFniHoTwrf9YlIUfPLgW4-9nM2T_vQhwAvI_MnK5i34NCTlFchXiPc94fv533nUcxMWCwb-6UR8wY2cSD5spTARavzu-vCDhH5tUlcP-_mfxNDYNKdfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6P7L57k-fkGjK64oqil2KSW107fEZppKO4GF0Cq1-zG1lRWpCN_WP53MMkDJjzYqoLlALpPXfmYZh5joppHejaQGHeVH23gGxT1p_neIgJDJBTp8jsehd0o8drdcU8Ah4edbwMfsjI7HYyCsnjPXmxA1vrWoPBqG3-Ej9KF5wyFVUM-FvIZ5tRevtTqHpltD3bZwJZtpG_A56DmfqpTVgrRwkrSAAFFO5FEKawWjBeCOWCyRav4kojVTFVzMVzo65wIm9SDV42a5WcCLeGVekCn-6jcEKfyb47V_gNTztDCIK42P-TyMqSX4pnyZddsuLKI5YIeNCqoIgdELQp1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWC44a-OrQTaf3yeSsLwYd8eRU8QzFQ6KbkvVjbk69dCSLz3YFpyiXewzEg75Ta8Q9aB7Bh_CrnAlF_75-XywMKIugdD5CI_U7qJdGWWZGZ0io1Q3fqo8SZN6MxhNzZQ4ive2kmiTRwcTICMUR7_H467UhguZDk8h3sw-mvocxUzuFZ7q75ib1vO8SfRhCPXSiHCAbfwMlZmcvkdtxRXe_C407W5q0ASRR23U5PEfmbQP2Q-HCl9j4Qg0vClERTN9eBLeYKrBMhskv8mZBrZ6bj1NLq7fAje2imVPRuNZJY_ZUz6IFc7aLL2c0JCQTJFXcEjWbFGazfTceRGE-iKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujU57P6Nl_vRqfcL04uk8S7lphWpUMAMwJ29qeoiueT3qbVOteTTUpwVyfqRIfjWpKSLOzFh3L87ueWzW0MUG31qPFqfrDc_d1LckB5_QstbDWY2856PS8KktXoMYlNDz4QpAkBYme4A1npgc7Zl8vYkDqC6cPPPT8TBdkxk0vclqE3O62T8AAD-FPok9tOLloSefuVV1GZlLGjpGujOtwtOFvFxjZ5RyjKEbpW-iKIPmJD2OEuc0dUNJmVZJLrjsvfcirnCa5t22TAIUWrca8_TtpJ9xZNp00j0BoT2UebzBTPfAkvxrO38manBQKitPbbJBbfHKO-NSx4cagW6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaJSNTJ7L_OX1xz6wi8vLi41dpsYYVNHB6C_B4rgxk2LAWSm-CSbWIi-xPw0ogoAtR3jH38q79L2BU61cxpH2GLtMzSXR2BquRR1m5xwmYKBPc0zf4Re57GisPgxHTsCeMfpzTgkleNeFpe5K9klQSGmr1NUfNgozlTyOSalB25MuLX2erIHRPgmqGZAot5Vaestmv_nERqqP8askctrqWLqVCeSHGKms1whoWhel52F8WJ0Z5XdpdRLowg5AQRGXMEdQXKg_97LmAmW5H-T8rsrqoID_tjCE3wON4xBmbbY1cbyvTV1A54ldkMCiXQMJggbLK-wcia75wfpE0B80Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=q0btZDWPvT8DzOt809lKe82Yr6w8pngEudCN8Fu1c7dz8tNei9q4oba1t00Y34fPwAeN_eL_0b_qZRk4ZDpfjgv8-GJDCniMvTbVfSofylcAugtSsrVRrWfoX4y_85LdQ_h_ZJ7OHXaxOCeXcI6FW2AVsNIFeLqg6EzMvXdeDk5FBnjjqUneUN8lOTPhzG8nKQHi_AP-Bat_VEKLYVYb5r2iu-X36zz35fz5pc49DIwr9wbvhOvU_P-q7upn1Yi3MidzgPF6ip-kWwGCbakYg8sDOOQzwiBbRQ7b5MKkR7uU45DCw500cLHV7D0PTmGMnOtNXhphdwgEMxzNnh8QmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=q0btZDWPvT8DzOt809lKe82Yr6w8pngEudCN8Fu1c7dz8tNei9q4oba1t00Y34fPwAeN_eL_0b_qZRk4ZDpfjgv8-GJDCniMvTbVfSofylcAugtSsrVRrWfoX4y_85LdQ_h_ZJ7OHXaxOCeXcI6FW2AVsNIFeLqg6EzMvXdeDk5FBnjjqUneUN8lOTPhzG8nKQHi_AP-Bat_VEKLYVYb5r2iu-X36zz35fz5pc49DIwr9wbvhOvU_P-q7upn1Yi3MidzgPF6ip-kWwGCbakYg8sDOOQzwiBbRQ7b5MKkR7uU45DCw500cLHV7D0PTmGMnOtNXhphdwgEMxzNnh8QmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3sW-d59uQKxrfK3HIp_YYxMu3f-LXo1olO5Fu8syFzZNh9qelQJlMZxZ7CCIZzjvNWmCY9rESfK1YJJPRROz-A1IDM8i2Wh1GIRIGMvQKAc2v8FkTiTj8HvN4YYfUfuIP4A2FViAKXxEZfFtvMks8DqPUduJ_f0zDukjcg3QuRwE0_US78RZB3U0xuJ2uhvhPEICdHF8ijrLyLagfnl6_3Na5EhJJ8x3RDiEVBUm8Dsma9aUTXFpXKbrMrsJA3LsLl7FS4Ys6Q9Wgvs8lADocvHH1WGEv99BZvmmugOHoStRih9leM867pLypZEWa9xkX7qb2dicrNAV6F89G7c7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9HbQyIbQe2lK7HlU5lJPKPfKFJBd4XvUaISPmmKkC6WtcaFW7j7sCTg4IbqUvIIZYBNNosmoynkvQNN5BgJWmEyxLanMCYykNsM8M2rxzM8QaIQriYySpTkj8ZTiPCcS8jhbkvWgUplSv8rQh3jbacm3bYlZsOvnZPJUU0WxlaV6FpkvhCW6I8Vbpk41bvXVyOgDy1FvgtIz2B3M1-UoSlTPlur4Puq_BCsM_KxP-m-OeuE1rOiVEEjKmdBsT2bH1pO_N24mtaZ8-I36ZC3QuV-P4-BVqMLTFoSOFK_PLdHLsKCWePm-gfcpodP0VeRdK2A7Uyh20kTfZC78GFpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=mI6mxln6VVUf5wpm8mTYXw1kT4K-6rBxYhEg_C0BdctEk9rHSvIuCp6lWUNXxA3F8j9UBT1r3FQbWZhtuteWFf0VKTzewJYdoCaPQbWrdrA6-ICnIYI-yFa9sun8_e4DZUt8M8smybjwI6XUDAgPCJCS7QbuLBtggvXZJQhaDHdrZh2h02TbLTlnDSHpZs7z27fpQoKq4S_Cq4wASwj8JBRCz8MwFrVTLxfJTXPBAzJhMkSbp4hZUoR2dJmJjK59CHBfBmFS-hy3mPUcQlhEllngYRJoJDkSmTEIrX8Dh2KnhXS0_7ZxTcWiuWpM-nxck6WIc1HQAUwnW8V-DGJ1tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=mI6mxln6VVUf5wpm8mTYXw1kT4K-6rBxYhEg_C0BdctEk9rHSvIuCp6lWUNXxA3F8j9UBT1r3FQbWZhtuteWFf0VKTzewJYdoCaPQbWrdrA6-ICnIYI-yFa9sun8_e4DZUt8M8smybjwI6XUDAgPCJCS7QbuLBtggvXZJQhaDHdrZh2h02TbLTlnDSHpZs7z27fpQoKq4S_Cq4wASwj8JBRCz8MwFrVTLxfJTXPBAzJhMkSbp4hZUoR2dJmJjK59CHBfBmFS-hy3mPUcQlhEllngYRJoJDkSmTEIrX8Dh2KnhXS0_7ZxTcWiuWpM-nxck6WIc1HQAUwnW8V-DGJ1tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=R9OVBWrZQ2t1h-ezc7xe7pTAW9gjXEQxD4ntTH7Qajv-6jGyAL--7vAvdNrvAqwzuucrpkgniUVAM49-jelCaWleXrxPi2Hx2YllejVQWQlaHR0Iv7ZqgGov5ptIUuhHXrIINbRBe_IkiaIOfkDUHm7pZ3ZXHXySl8ojR9bog1MOsqpywB-szHy-XFCBRhSgwD1zYwO29_wDUHY6vXCIPe4cIaPHlYICkvdpbHV_5Iz3asoVbvPOfCRpAisTnWSYB7A7S4-cM_wEeZeYbaJr0dKGWCDA5YE54LkSXtaODJFHVxM6D_Ej6zVUHexbGq-5t9qYpmeC6uqeK_II6wi4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=R9OVBWrZQ2t1h-ezc7xe7pTAW9gjXEQxD4ntTH7Qajv-6jGyAL--7vAvdNrvAqwzuucrpkgniUVAM49-jelCaWleXrxPi2Hx2YllejVQWQlaHR0Iv7ZqgGov5ptIUuhHXrIINbRBe_IkiaIOfkDUHm7pZ3ZXHXySl8ojR9bog1MOsqpywB-szHy-XFCBRhSgwD1zYwO29_wDUHY6vXCIPe4cIaPHlYICkvdpbHV_5Iz3asoVbvPOfCRpAisTnWSYB7A7S4-cM_wEeZeYbaJr0dKGWCDA5YE54LkSXtaODJFHVxM6D_Ej6zVUHexbGq-5t9qYpmeC6uqeK_II6wi4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaYoA4QElO0sNReS3RZLSiQc8zf8gYsIGogbPXNOhRQHS6-ksyYBj8Z7DLq2f6mUn5D4579yNGKRH940yovrcO4KfumioQigf43M4XC3aU5Mes45rR1-pdgdygn3YcQFfPEvudWLB4TVu3MDxVd44ScMp67Qle3TKzYMRIR3Zx2aPAWSMhFxzx7j_kYq_rHOiYDBNCMoT4nOdGK2PKyaRrgqzgmQ8bkqhh_eFro9InCucIlN4W_ILbX_vqDOsOWKsMMmapo6lnMqhPXELfQeTWVXxyF6V1NwVvvkuSQxkC7HulRHXt5_4EQENhDX_i6vi-U2CLBAbdgyyZlw1DgguA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMjmSCdK3aaYwVFmCc67TuvAMRrktGAqnr_1nCzQQl7AGUMX2r0L0tl5C2Hh7tJOpqBeLBqHlJB-gdcIHiMcuPawDdy_m2xh5hn9puXHTaIy27jjRAuwP6sJF2woL_NpE9W93rQkqYyzFJdsBAXJXhMqAk0pXMz42n1Cv9S4vqyJdw8ryh1r7Fkpj8ovb4XWh_lMIGVKK8hfZfPAot6GJViCx3f1NylNqmHlZiDOvwcTMmNqzYgaHra3Li8kkFUf9nIDuoO1KTWmgFUtZhqxemqQkk1ZR3lDXDoNUYjCc6D2YJCh2doclUSQ71pZaQpXWp8HcQ6GKgGc7yQvBn0WhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSbUq1ULd9BNlD5JRQmpaazmlyJcj3Yf2Vg4VzNcKfrECII42akxJg6rtl4G9SBubTB2xdE8MfQCcOeFODthYa5E0bZYnDEvHYT4cjpLkszW_NmZv-BUf3o7Drm3Flh5RlF-ycu5-dgcKBvy6V8AbOAAD-E_-o-b5jz80bDnBJ3mAg3OsOohwEQrGvJAQMCue6prZNgxEXf0jCZeimcxnmEJm3P9syG1Z_tAVKgzo4IZfIK99SeohAUWjOiuJmyBt9OPpqFd2QJ2t5eKuwFlgdaGKsnCvfATNmgq-oBVgJf_tsC_iPdNJvxmaDc05k2pPsHSfS7M117xhJRFMHtkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9r3zjpr6eu0AO01s-IU_meGUVCZJCLoy9C3SadWaXUChqD_7E_9926ZJUoKPhydJtgMZyrDC9EvQYygqXuD1GscrTdPs62_4jzP2uU0V_PI5P-M_xEwjK2K63MjwdjXN9mlpKt_GaF-_1X7bfVe-ZYJEf-7rC9ONVxGBB2ErEWWM8CnhHfWrWHR_47u7UPkV0bF3-H9MjgdNE9ukjBvztr1Y7PXUI3P5h2-UnbChaQzSTLMI78ZeNyaLANb3QfZ8EJ7UdqZfULovpubx0EVdFQocLlPIojjiw9rgWSeY06vC6MwRkdml1gWKweTlmJXlrXO4hV_uf34HPhUzrPArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-xp-4Vlqys3GTLrJtgSDtzeVP0FY_B9fdF-fUR4MuGjCXzumEenrZYUjCRyaua5xBDNogPxOObhYsyPjEfwy0SwUX-HszUzM7VZ65tJe1Di733PVbcSvIPGbOGbrfeEuZ6PcxFKFlUgbIS6kdsn07xozGoBUMxU42bmUgUmgfdDJBJwlA5hRrS5kF-gs-BRZVCJcYdR8xwmmZeudf_i5fPdvw4UI6S3NPBMwmRa24SPLSFPgi9oBbzq9aIYCnXmbu3DU3kLeqYyPphY1TbkHuj8l7MZDANZY5uIB4Zj3Jqk4bR2wZF1G-9UWCzr10pfLvY3ivhHfu6d6mMTVWvkkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBr3gSoFvRNfwZDfuErzDCTN9tDj_BKCJb5Maax2T_6CNgaYOzN6i56mTcZrmTwLLQWdd5bL0SQZxgFIDTXfz-WXqaMaic6fSDGEDlIzCKlNRYH8yPTz0T7z2ANsIfTf21xzj81cLccPJBvNX0R3s1cULzRqUrYhNo9PTg-yt0vNsIMdOah22fLgstp77jokLrgttXtwpgV9kXFEajARuHHqhJ0Q-uCUjQ-eTuEnQm8_HvkysPmGU8ka81f8HQpH_fNK0EHk3BPMHLI1IICLXlu7wpwClBoliUKVjb97ddSh_Olr3djh3iRXXzC6-O3kIoxvSbg4YBnLHj-fZ3KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0iqlPyT_UjmL_MtDIc1cViCQK2fOBEA5e0lwAiDg2oC-lNdd4Yf8uiYHk_DAcReWbuLGe7rQ5yXxnBi1AAejpuQh4Kclez9r1XOc5dXpaJkd9ibJJHZGp5DLplhDYNChMJXqAkOd2tbUE-SoRjVrZe_BFhFPfXM1110UD7LyPqhkdv1_T_awa89j1SKgCGFFvFn3g0iHrFUnJh3-f0FcwevUvP49O51_1gZecFErq8M6sdozfy6R79xQ6VS44aWzQ9yxU-SfrIpZ4X4eKQKK-DEsix8wr7ljAtGVFWqDH9u2nikXkgny9Ln3Sw-gR6nMKYPebANjFx4M3QX7rrzvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=U7iwj9VFMwax-e0rm3hK3o1ip1XKPHwP_jCd8tLHz3z5pBQVfqztUZ42XsHc4pcdxP3Z0tENvgnbGixLJq_4cNVO1qbJPX8UIsop5dD6rpEse6thPp6Wfx4oHi9wnq6cX-7GeyNqxbzI9PuyCobxsgzWkwjv8I_7Ou_i-eoxwOnZGtb3iNOlfY70x_m_mSrV6UEI6ntfvFtA9L4zPM4Zgy2cZWqyTl6mOhlYD7yhlxDZiozOVmNA_84MFk_4XwvlIHnxqMd5Y_8sR3zPjHtjbiXZjcuoLJrE_0Wf03hGMB5E35Y-7OO5cdsTJo5a5lnp704rOweEOVQYXqCptFp5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=U7iwj9VFMwax-e0rm3hK3o1ip1XKPHwP_jCd8tLHz3z5pBQVfqztUZ42XsHc4pcdxP3Z0tENvgnbGixLJq_4cNVO1qbJPX8UIsop5dD6rpEse6thPp6Wfx4oHi9wnq6cX-7GeyNqxbzI9PuyCobxsgzWkwjv8I_7Ou_i-eoxwOnZGtb3iNOlfY70x_m_mSrV6UEI6ntfvFtA9L4zPM4Zgy2cZWqyTl6mOhlYD7yhlxDZiozOVmNA_84MFk_4XwvlIHnxqMd5Y_8sR3zPjHtjbiXZjcuoLJrE_0Wf03hGMB5E35Y-7OO5cdsTJo5a5lnp704rOweEOVQYXqCptFp5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/old-HAoNn-NMx1n7v2mUwHRz8aKt-MseOR7P7_dgAc2OGQB3NrV7XzNTsXMA2sB-Bo2Ryle8-ywdDuVKPJtV1DBrDqRPoe4ohIbeQGc-67jjimHT_nai_iuThNW_owIyUj72TfV5nUtmuYOK2aum7wiaRSyyjttY8pDNVxfMWGJ8VRX-TvZtg8gz3NpgSTKIVHFaAYFAAZuv5HBxVoJeBsKiN7AwDplLthOJd0OujIhC4qoEvlY6v92C5WqVSCYtL5dfD0m5T-SKxP0Hu6oYrWuaX-FaFf2roNFtFcznNBXfTFIOJBMEKQCXTU8Wfu7cg83RDdN2p7UeJ22kJQrQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=STUlUrYmsp7eECHGmfC9ZPoGuSbOnUeAlHEROo15hDZUg1WlxdggJUP6hbm15zTcxokultNaSmF_yo0ZNL_GC2CYhOnVhuyLL6hkTyKJHFAA3msQesL2t3aDc6DSvmHDBdsd1ajGbgt8wPu2ucBQFiX9DfXRXX5rG7ECO1FNMWWF5-cpbZheQmmnQcQpBY7SJikwxDaBvCYhg93MrLPQTXOmpoki0Bn4suY4h3lhef839naWTQRgRCYp2T_GGcT6tnA5294AIV-4mkbObTXMvLt1W9k4QFELeu0Bj2LdPUcppze0GUK3oLKAeSGi_7KzjeAme63nTe3VRSaFdtbcOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=STUlUrYmsp7eECHGmfC9ZPoGuSbOnUeAlHEROo15hDZUg1WlxdggJUP6hbm15zTcxokultNaSmF_yo0ZNL_GC2CYhOnVhuyLL6hkTyKJHFAA3msQesL2t3aDc6DSvmHDBdsd1ajGbgt8wPu2ucBQFiX9DfXRXX5rG7ECO1FNMWWF5-cpbZheQmmnQcQpBY7SJikwxDaBvCYhg93MrLPQTXOmpoki0Bn4suY4h3lhef839naWTQRgRCYp2T_GGcT6tnA5294AIV-4mkbObTXMvLt1W9k4QFELeu0Bj2LdPUcppze0GUK3oLKAeSGi_7KzjeAme63nTe3VRSaFdtbcOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=uu33H1lcxNFdm1J2S2_S57UwGXvIAH9eyWWpRjUHaepWFpHP30akWl00TM0AA5NcOaXUhAAvWaTYQi_6clqTY8z32KGWc2jO6VdghzNBy4MC33Y2Hvb31eS-zePKyJzYPLU3cm0DjjSB5LE2WdvNvVDpOHJMtIhydMtp7SjePYuE2UXRknPyXR6Jzzwvuo3TIEJxe5h917InDppu09TdZ_dpAldM4SnyNJHHorxJ74yvgsIDy9FrMhBwPUaBE9gHscGPOJpXtvbBY12Hh8izT9zaBIP4seZ9YzObUsD95qly0v4jJxAORxLgz2KFRPTVxh996kdaIfxvzTio2kp8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=uu33H1lcxNFdm1J2S2_S57UwGXvIAH9eyWWpRjUHaepWFpHP30akWl00TM0AA5NcOaXUhAAvWaTYQi_6clqTY8z32KGWc2jO6VdghzNBy4MC33Y2Hvb31eS-zePKyJzYPLU3cm0DjjSB5LE2WdvNvVDpOHJMtIhydMtp7SjePYuE2UXRknPyXR6Jzzwvuo3TIEJxe5h917InDppu09TdZ_dpAldM4SnyNJHHorxJ74yvgsIDy9FrMhBwPUaBE9gHscGPOJpXtvbBY12Hh8izT9zaBIP4seZ9YzObUsD95qly0v4jJxAORxLgz2KFRPTVxh996kdaIfxvzTio2kp8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI2H8jFTMy8QR_C0LVUFIKW5Rp9Kw_zruVAfBdAFxQHkskVr06OrSIm9LFtCWZkFvs9tmMRNU3gjVtCClqG7DE2YmZvKtvC_Wq2fni26nZFYetc0xh4fVafNOLqIU9xhOWXmhsdHkUxZpCUUDUpl3BAt_5Ky8ZD4dQQmNDGPbXTfIUGr9PupIRi5smqAzsXZTcO75VIoxE7_wEM8Qipz8IGWSUSHJnbjdp-DYBHvEMj0q5h-gBJ6ykTWitAkeaPUVjqBrNPAMR3oRvqjcuHg4GuG-ADDdX8HxKl4N-eEeMJIHDUJNjlwSZTR4HTN9XCCqT7ogywlI8JK0W9DOEHVtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgSthrGyIBzBi3h0CPqEYgvEEW11GW7zHmc3o2QnNsWEZlv4rU2_fisXx9cPeeDyEPQBqhzBM2lEROqRMp_MHXv_SDtrkv6r_zhumxpB65mtLE4OAUQtWB1ZWx2R8C9H0-kkIB0AHU3XWzktjiO1JSxCM3WANI3OdJDuxpB1wdBYd7zdMeEC2FBlKNTMZQ-0raW8JsI1oJfFB-COo2cfGm7FnWhlXzvPRH_-gTifma326XkHom6whZ2NUlwTtstTBvbk-2Xu1ANM9VBA7xEgtb8NP-M3_Fif2oKGsyfBFQrh2bLaMYTebrXo2HcrEgYpsvx0xWfVLTHK6Vs4N3AhlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oGdou5gOV-sMaZIy3eBXQgSPymFA4eGGtVHqnLCdZxQdAb6ZQ-wXHCNkGCTyMPvBXui8qpiyIRBE0IbV2zLvriJJ-XVcM4KWeoBFzOm80D6mglX6pj24VLzh6x9lDvhjC9TRXv5YqHS9YU-1MMqsDpcEc3hMhsUETr3sZWXqxSIuMaeV-bK7JVSvPjSsYLahqXLsWsTgJwuCKX-817Q2lL73xn8sXGZ-0MaaUgFKslfYeJPj_vjhzSWmNv-F7BlUdRRQOT9zWXqwKLlj-3_4P2eQjHiqt9QF0H3Q8RQBFBX1ejCmWppRPd75EAaZ8G4S29UXo9DJVV_8Nzj7hbGCJQ15yKkmIGYJMb1VZ9doJYuZW5XOFbEa3AZ0i0PEbtOJhw5fyrV7I88Jw0vyEdkvwa0plA0AYloPxGk8bAWvjN-cyA0xcnhy24b8zOrElzK3d8juJ9W4Lji7Y8-2lMp2k9pVidZJ744OaXOnKQgmPmalJEk_qc1D08b3CGY5KNseHOREGhtlDRKHoxn84m7sIAauWQlYJLYBJPNMaqRoSNVB9LSG9hCRaSkOWdP4PBkErGPNgaxhHqzHEF840cCYj9i4bmMbo-OqOtzEUtCG_owThi7BJE4XQcUf8YMSOtHCfx2dRctRAa8kTxNLkdWgdIQ8_PAt9NayXNkGVMGTFs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oGdou5gOV-sMaZIy3eBXQgSPymFA4eGGtVHqnLCdZxQdAb6ZQ-wXHCNkGCTyMPvBXui8qpiyIRBE0IbV2zLvriJJ-XVcM4KWeoBFzOm80D6mglX6pj24VLzh6x9lDvhjC9TRXv5YqHS9YU-1MMqsDpcEc3hMhsUETr3sZWXqxSIuMaeV-bK7JVSvPjSsYLahqXLsWsTgJwuCKX-817Q2lL73xn8sXGZ-0MaaUgFKslfYeJPj_vjhzSWmNv-F7BlUdRRQOT9zWXqwKLlj-3_4P2eQjHiqt9QF0H3Q8RQBFBX1ejCmWppRPd75EAaZ8G4S29UXo9DJVV_8Nzj7hbGCJQ15yKkmIGYJMb1VZ9doJYuZW5XOFbEa3AZ0i0PEbtOJhw5fyrV7I88Jw0vyEdkvwa0plA0AYloPxGk8bAWvjN-cyA0xcnhy24b8zOrElzK3d8juJ9W4Lji7Y8-2lMp2k9pVidZJ744OaXOnKQgmPmalJEk_qc1D08b3CGY5KNseHOREGhtlDRKHoxn84m7sIAauWQlYJLYBJPNMaqRoSNVB9LSG9hCRaSkOWdP4PBkErGPNgaxhHqzHEF840cCYj9i4bmMbo-OqOtzEUtCG_owThi7BJE4XQcUf8YMSOtHCfx2dRctRAa8kTxNLkdWgdIQ8_PAt9NayXNkGVMGTFs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2Q5LLMe8KK4iCiSTVV_b7Wclk650wiH2GqlwR5goq22pubWJ85eXIPNA1nMklguQrJvp39wD05fMU2xD59tyR4orh739run11EuhDwSkEycNmotGmmnvCKKCzHl2072dJffX5VsG-mIoV3akmQNKSk0HIcOnWY8qElmNWpZCg6RTrHKAwQLIDxE7NyRCt1kkiLA2v5YIqzheWveFsDc-b36FJ_1jyCnC8zqPBKubF7e0vVB7PyfydQ9YUcyGQklU1HUlJarIGdrBZmrrg78cGVPcoLL1WzH0wCJXXuk_6-oKlVDiSct73o845_qp2R2Ql3Y9r9UkErpI6YKYTcxwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=XtjX4iKL8Eq9WLqvjp02hte9kobX937DpIo73oPjj5CS7lw4Ui7LH3SCCukHEH1AcmZ3HmOMU_lhDmWi8cKMBiTlR-hYl4bniOSxbASvgo3kMx1XqHZYzUOxraeeDgKbvBOxW0gLR22N3Y1YlYeKdhRZfAfEWmaNm9cHgPO2y6eWUGG-EueAOa7RCOdLQvI3UlIWKU3ug7rrWoeWy40rN8UdrVBWNZHje-v4faJqzLeSqzWzMKxFbfMsu71Y6Q0miWwh97k37T-tiR2cqsbrz1xrHrUFvpUc_4Hn5ScG_ydOcAqxs2RejoGCI_8yrw12rz_JbPQ1Cy-E7VYNRMP90EUy92trm5nl1-_fxqmtGj1CGd0E96Exg9cDy8yKjaU9MTfkSLOUMWeN9NpOQQhw--W9OA7aXHODDPM2hPMdP5LthTnndgFIAj_SZZ0JgjtJcOq9fx0dRcUvdGvaVo_yYFGtrY7Gs70hNhLStdYJyvUC2skZ_0CVn28skRjIGfMAxT1DOQY6C-e050GC0vyrY55ZCtcakHFpeW3jOguX2Bnh2JV6soFQ7RXRGKnEmeHYzydSAM8WbB1Zk_BPLDx2t6Ysll3sk0Ylj_ghCFQMLA2ke8hgMtRKjmk-YBL9ZEaOYygonyWs-1jYv65pQ3ZkflmW1JLla_rnReezyO0OhpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=XtjX4iKL8Eq9WLqvjp02hte9kobX937DpIo73oPjj5CS7lw4Ui7LH3SCCukHEH1AcmZ3HmOMU_lhDmWi8cKMBiTlR-hYl4bniOSxbASvgo3kMx1XqHZYzUOxraeeDgKbvBOxW0gLR22N3Y1YlYeKdhRZfAfEWmaNm9cHgPO2y6eWUGG-EueAOa7RCOdLQvI3UlIWKU3ug7rrWoeWy40rN8UdrVBWNZHje-v4faJqzLeSqzWzMKxFbfMsu71Y6Q0miWwh97k37T-tiR2cqsbrz1xrHrUFvpUc_4Hn5ScG_ydOcAqxs2RejoGCI_8yrw12rz_JbPQ1Cy-E7VYNRMP90EUy92trm5nl1-_fxqmtGj1CGd0E96Exg9cDy8yKjaU9MTfkSLOUMWeN9NpOQQhw--W9OA7aXHODDPM2hPMdP5LthTnndgFIAj_SZZ0JgjtJcOq9fx0dRcUvdGvaVo_yYFGtrY7Gs70hNhLStdYJyvUC2skZ_0CVn28skRjIGfMAxT1DOQY6C-e050GC0vyrY55ZCtcakHFpeW3jOguX2Bnh2JV6soFQ7RXRGKnEmeHYzydSAM8WbB1Zk_BPLDx2t6Ysll3sk0Ylj_ghCFQMLA2ke8hgMtRKjmk-YBL9ZEaOYygonyWs-1jYv65pQ3ZkflmW1JLla_rnReezyO0OhpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJBmq_YnXzZlQDX7fLGn3b3szsJ59eoUXiTOguInruQ4QrhQJrfNf9KyjMRtV1-ONN5UUuuqXcuUgDFzZ3tSe28xbXsJS6LRItOLAxXULXgOhmboEWHTtq_Uh9leq-PXWxuY658c64b_gSbRJripJT1_shznDHyJsS-pylqL7XxchpLkvIFMx1ielFrHdqkpSZQl0THtJ2IpiEPaCBQJhwKwiySrpaKw_WkDnpgfKEwKdnEGXWlrR0b2tBa1RdYdhl99jOP24oWD7x48WrpGntxJwHuj2z7jzRKVVmjWGmL_x93hIzg-dXi9Pp9tWCzmHuUD2ZnC6ias-seOVCKZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnwGCy1SupEP7oT3cLBq9PUVl2RUXNXd9heJHVBuHQQHpXoYGslu06STyaYlgb-v8fkZq46RiyVQJ_ceRenSeqm9sePPdzV-gKtZVLk_DC77bzDgT5p1q8A4JL0AqLrMVQp62y3txq_FbUqkQIv33OgH4x14hzmcdjZxvfn6NI6w1i8aKZAOKTOXpFq8emzStJSuhQ_wVPtDLsvgdwlGc0nOncwrwAR79xJw3F6ocerRO1y35APSwBZLmvqg4NAdJcJw7dQHIUM-kNWjRIp_rYAXcPPm7mfQQ09v_eC-1kP2N0ZzhQYCXdPueLhCat9t37goDfK4enY9vE2ryxUvpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V56nkpMkPfqweDeU-Nj6tyhb9OSfMWnQqsI3CV116pdW5PkGMF92AL7VLDqQvO5dcW09uPC6c6l3KK50egFfIYdWODFyAwUfj2qyDYM8XxkZKuvhbj7jJyVmyckVT_kXDC4Zr-T8LSizF99VnCmgeyGh457iW9sNlAO8NjR_ewq27GBBdi3jyg5SLOFV4FrzdXt2-0I9TTDmxnmT9RMrgfWw72EO53kZoutIl_N5urVZ40pNd_fcd6tu8IDzEVMIaIHfjcQs_W5K-fQve7cXPZlBs2Gtd4MPKQPgfLMYGf21PSNOaDZWVzHFJUhLNGqTTzMrxGZC2pc6UEKNK_4j-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
