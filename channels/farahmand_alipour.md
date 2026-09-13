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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 22:38:00</div>
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
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpWCayyCDAcWeSRoAR-75XxigAGnv03rHykX05dJFvbJ6GNXLc-pYVME54ma_1VlicHZ0AwQc4gxuCMxFIN_YrZHninfH00q0QP1j_DRdD0rVoTmx1Ktx8gQJXnRT4Ez98XV70YgIjeKw8jpAfteTUR_HgdrWozt41aDh0lMRMZin_Y93Sxg2h8Yb-Wj9zd6PPz3oSuYWBtn9ICgJyx3cKIFW9QGmEjnaoBYLzWxv388PsgoQEJ2nI8-I1Pc3xHsHeav0-QtBK3Qq8OjeKv5MLcqO9MllLnadsnyXD0P6TbiRqZ0TUTPzRTEM6NwtarJlxZ9EtASKKbDCenqGkHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLiQ4FBokT3AOJ4itMQfY3E0ZLuauYCwXNfTRPZNjSzB2FoHYFw7lOXisV6DKzkhxKU7JOyyR0KnLMOQGTWqzXkJIkv5tpQBQtEfO0DkC4IRu55R3QAFtupFUc8QmDPtyASVZM0_OjUb1rXSnunjXUf97bHrgQ4W89t-MQGmVHiIS0W9LRqA11m9Oj8mhSTwcs26wkhqqgWjhIrCnQuOW6SCQqU1Y8b3z8OeDQW9MlcppnJYthWRjybNBdQRy9cNWyUPGMSFjSQZ7CPx_0OK0DHj727kZ5lvgS3_FArDk5hLqQhJL-pFXRM9lal9VANNNNqk6M5XQnB0pAUH2-cTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TJNKk4uR5Rbk8rjtnE0wjKd5EcZMxBUX9crOzD-BsDARLpoI_PRQP8GlQbQYqXjElo2zWCVuyJ-dKHuxIrLqF8kwGa8KstCZvNl2arvuzDzoIyZHQjg5MLIORUFJURKSJmhU2jQwn8Xztls74mr0LVeqxzLcexnUQ1npPiz2iyvn46XcvUShgg_TViFcqsNsxWJxef_tFpyLOxUytautg5JJYonYq20Qmw0C6DtUaMxudEUUk3ajEKhXF2gc31_C0Wj8I_tiuBqPJBxGaVzzePyDe9LT3dtLNHNaM2YEXCaLOUH3E9mV0X3jS9CUipcOv918hRuSBhWJWJmPrSfsmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TJNKk4uR5Rbk8rjtnE0wjKd5EcZMxBUX9crOzD-BsDARLpoI_PRQP8GlQbQYqXjElo2zWCVuyJ-dKHuxIrLqF8kwGa8KstCZvNl2arvuzDzoIyZHQjg5MLIORUFJURKSJmhU2jQwn8Xztls74mr0LVeqxzLcexnUQ1npPiz2iyvn46XcvUShgg_TViFcqsNsxWJxef_tFpyLOxUytautg5JJYonYq20Qmw0C6DtUaMxudEUUk3ajEKhXF2gc31_C0Wj8I_tiuBqPJBxGaVzzePyDe9LT3dtLNHNaM2YEXCaLOUH3E9mV0X3jS9CUipcOv918hRuSBhWJWJmPrSfsmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hBInyXot6FcTpEqKO_DZKmJf28kW8SzkUPjNjmn0H-al0pWdM3EDIAGdXYBym-0Z-wNP7cbYUkQ9lGudmMBvkKq0cJGfGPCbEqbZYCgqvZd_WoIyYlZzKorE-72xZ9BQIYrrdfwnFNLJJiwv1oqTpQGD90wU1xF_Mj1eD0G78KIolUM993sMdJ_SA_JN5A0yz0eWCrc2VQa1-2xZRh94ck-0neezhUaRgaPdRhbG7I8frZFymvED4WkIyFnynoiqCCrvP22csQ9wK2gAtGGN2z2dD9tMMHcyGsHSwmLwgDq-k1LlYTGbs6UOL66-7hDJFksL7zGjpQZqeqgrzDNNTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hBInyXot6FcTpEqKO_DZKmJf28kW8SzkUPjNjmn0H-al0pWdM3EDIAGdXYBym-0Z-wNP7cbYUkQ9lGudmMBvkKq0cJGfGPCbEqbZYCgqvZd_WoIyYlZzKorE-72xZ9BQIYrrdfwnFNLJJiwv1oqTpQGD90wU1xF_Mj1eD0G78KIolUM993sMdJ_SA_JN5A0yz0eWCrc2VQa1-2xZRh94ck-0neezhUaRgaPdRhbG7I8frZFymvED4WkIyFnynoiqCCrvP22csQ9wK2gAtGGN2z2dD9tMMHcyGsHSwmLwgDq-k1LlYTGbs6UOL66-7hDJFksL7zGjpQZqeqgrzDNNTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys8Ds9ucE2Tb0g7a1jkolUaOKN6r9JRlUlreoyFcBJCvkZztx6tAwY_mf4IUYOLoHNVOdIHQ8r23-BCQL6dHgc5tbhAR_fxgQzvOSFTiJzEGaJ7DqwX4esjjyKhA28Wj3bpbvLFKR4LruliyJxIUXD3x5abapQ6Nv0i14TgakLfSibeoHV0O9ItMcNmkM7WCYqP_YiLWc5u9z5yGSQRIDhS-_gqKmfesmq5sX38ohFVwjFZFRT6or-JE4-E3-FqyK9me6XexlOVUT9p5QnpqCuKKbYvA1gejZbvwhevxh6x_0EdBP_P1bwJLn6D5M36DZdOCIWX7-vTHJKobmZp__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsmXJNO2P58ytIpWFTvxnxB2ZY-RswEe7dX9VqDHpZXDg_GEYr6ISmdO4CIVyYP1qvftQz0Brw5bkucIrDQ2LNbDZXhxBOQbvMUYzvpdrJJigUVwWIxCEXKoijAGifmAfLGgfnfaGVSv62FV1Yta4gUZrgQupcqjXT8PdTTy-n2ROg64Vlu-kk1XpqaXUGvcI8AQHwFtAWVqVS1k6AtArleztmUPNG-_NPIm7nVALB37l9mtS-aJSBuf4bBWavxWfPKM3NMX2Tp3QTLQw8IJhxu8ql3n_RngMu-tLF7rNkpvrDhdaDT7gMFQDTjh4UzaHex8ll9fQlmi1Y9SN24i0Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VLudGyBqPRSH9sGzRlQlhMrH133cR7A7fjMr1RScRQI2ToQXMpVE0I18Lkc5A0CWw2wDXrhhgNkkgEK7ahbPilqShfI2Hm4wV1uXdh06aWse2E3J5e47A4OBoeZvQyOdQ46hMDQs18HJAZgz1V4P1LOBagDQaNDPJWYS-xH9BuQf8it9Yt2qa1kdjNoPBG71_77KLrun3mmgxhIXiWVzl10387mmrweBDs7kPok5iuVCIbADRkRiNoJNUpDsF9n55jQa15eU4mqAD_TMZ88r5OJiBBn_oMTlKJ0eoMa8fEY-nLk_YDZuGpoLA9CvC3U_3_m6EQJgGE6y-MWVYwFPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VLudGyBqPRSH9sGzRlQlhMrH133cR7A7fjMr1RScRQI2ToQXMpVE0I18Lkc5A0CWw2wDXrhhgNkkgEK7ahbPilqShfI2Hm4wV1uXdh06aWse2E3J5e47A4OBoeZvQyOdQ46hMDQs18HJAZgz1V4P1LOBagDQaNDPJWYS-xH9BuQf8it9Yt2qa1kdjNoPBG71_77KLrun3mmgxhIXiWVzl10387mmrweBDs7kPok5iuVCIbADRkRiNoJNUpDsF9n55jQa15eU4mqAD_TMZ88r5OJiBBn_oMTlKJ0eoMa8fEY-nLk_YDZuGpoLA9CvC3U_3_m6EQJgGE6y-MWVYwFPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TUfFTIVX_mteqbFn5xVtsk7vp_XXyYr_VCVqx87FGn9ZH0JxhC2qXZcXUD_CXWt1KCqcUAPRGs1md3-r7ramGI_XzT77SFFAHFyDBiI0o43SmQc5OGjnsXrypgRlTfAmSsNXmG23rKTUTj0r06aFzYUyH8AYQyFfKQghNRClkG9ishJh_f70SkQWS-Qz3mKWDw91RpfMDiJ8o5A78CqJhr3DBZuskPyTnpBxjkVhhI8VsN4liip06FQPTfcdC6PthtrrWVqHPA5jSm0TCXMMsiJccDKfpaeldnpAngMD6M1j-SCeqPOY8C-HOQUIs6n_o3ryTK7zX_sur-uFy66w3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TUfFTIVX_mteqbFn5xVtsk7vp_XXyYr_VCVqx87FGn9ZH0JxhC2qXZcXUD_CXWt1KCqcUAPRGs1md3-r7ramGI_XzT77SFFAHFyDBiI0o43SmQc5OGjnsXrypgRlTfAmSsNXmG23rKTUTj0r06aFzYUyH8AYQyFfKQghNRClkG9ishJh_f70SkQWS-Qz3mKWDw91RpfMDiJ8o5A78CqJhr3DBZuskPyTnpBxjkVhhI8VsN4liip06FQPTfcdC6PthtrrWVqHPA5jSm0TCXMMsiJccDKfpaeldnpAngMD6M1j-SCeqPOY8C-HOQUIs6n_o3ryTK7zX_sur-uFy66w3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BuKqkgOllHH25nRWsO1V5vfzIMgizX5ZzKBrli23IiuXJzsaeMDPTaxFN5qWm1T_ui4UWOHWixEYrgvUIueMw7ylyrDI7BjLB0y2M2cmTsC8c80GDX5PPpJslMPVS9pmhri4tUv8IRIRiRKf--T2-d1IhImyMkbbTAbcMaw0NmGdkjwqT971rKAXuwdhHq3qlYb39DwheuEXMFE1iMsS1hExgIpFEiOvb-frfsNQOtCPYT6VPpbUSSF1iSRrHyVA23_AZHZnioRKtCGd1XF28Ap80ZXM6-GEyI-8AfmWdhndX44JgPVCgsD-DfOwFQ1d3HY16QDTlUbrW5ZUK1XZVIX6Al9H3VxDpoGFjLxJgsnfz6Si_IxnSpg4ukrlTQh5y1KiBRypRGqXRAueRk0olDVvgdFP7ps1alj_Mz_7jA667LjW9jm9sMtbVY4JJfrH_vonNeV356CdQzd-0XgxrY1kNd4hqg74qXGYt_lQ0sSk6KPk94dGzn_mpcIJ2BkFdA3N3Gcn-blLWJq2lzfAAyhzuX-_8Echz2msEvZk9tpCO2O9KZBXrbfPjxPdQWcMfCGygkMY_m4BmonU2Q1Itoz6juMpC34nleJIaTwFPmaRkhnUOSNkfyQgiKfwdLzfR-jxykEImphAVUWpnaIsnslGhqX1W4uPqv66bXGtMe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BuKqkgOllHH25nRWsO1V5vfzIMgizX5ZzKBrli23IiuXJzsaeMDPTaxFN5qWm1T_ui4UWOHWixEYrgvUIueMw7ylyrDI7BjLB0y2M2cmTsC8c80GDX5PPpJslMPVS9pmhri4tUv8IRIRiRKf--T2-d1IhImyMkbbTAbcMaw0NmGdkjwqT971rKAXuwdhHq3qlYb39DwheuEXMFE1iMsS1hExgIpFEiOvb-frfsNQOtCPYT6VPpbUSSF1iSRrHyVA23_AZHZnioRKtCGd1XF28Ap80ZXM6-GEyI-8AfmWdhndX44JgPVCgsD-DfOwFQ1d3HY16QDTlUbrW5ZUK1XZVIX6Al9H3VxDpoGFjLxJgsnfz6Si_IxnSpg4ukrlTQh5y1KiBRypRGqXRAueRk0olDVvgdFP7ps1alj_Mz_7jA667LjW9jm9sMtbVY4JJfrH_vonNeV356CdQzd-0XgxrY1kNd4hqg74qXGYt_lQ0sSk6KPk94dGzn_mpcIJ2BkFdA3N3Gcn-blLWJq2lzfAAyhzuX-_8Echz2msEvZk9tpCO2O9KZBXrbfPjxPdQWcMfCGygkMY_m4BmonU2Q1Itoz6juMpC34nleJIaTwFPmaRkhnUOSNkfyQgiKfwdLzfR-jxykEImphAVUWpnaIsnslGhqX1W4uPqv66bXGtMe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=T5Ky049nFT9FRN__UBqtxklxlCNfpPFi2ZEEWB_Wrlsl3wlQjHK-G5sr7zLtGBf-NpfzPJ718IznQTVY6a_chBwFqGDCQ8uZ_VPPN8_n-UhgMQEW7JqKI3Qk6ne6kzxBQmfAJ1RY1rx2NBA-1V5ezDKpxUhJLQNNruXzvcxFSV120kvKVyaiXAmyDxy3TrizPk2tCvQMQCH_Epy3C1kdreH_jC9QEtTzeBzMr9X6NZ_UytGMd-USXQ2mAjwDGOdhMnm3M2MIT29JVSJ1D1kqUOrLgjiBNUWHvkkrBSJPUUYQYeZOJG1k9LsFVQv973fp_RfRqWu5v370vN1pTGDxR7Nd2Vz_cG_7o-tIVBZz9ssN5nog22FVBRBrPrYEBkDDr2Yrcw4bjWQaStERhuHX_BPCSSxn0KxhxJ7HZj-z_8JGtt9iMMJ_d856_cXFyCl-c5XDy4j3RqyQryn7D0Vpq5Dj5GVIwKJhBr5bt4my1bafY68YK2HwVcKlZgmr_NlWmU2PVrkPM_1m0o-YSnEWwmfYlGEos01_vReZE1YoZ2JyxWI_4O9X-Wx_NpD3xHXPn_xr6F8H3ZpdW5Hc3s5YdHvfelEAwuwqB85Nkzs7V2l5C0gQ8lf8wcyBZ6lo0aIu4qrUxgrl_KUQT_3o5ixGsPd9dCIxjwXAO02tNEamhTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=T5Ky049nFT9FRN__UBqtxklxlCNfpPFi2ZEEWB_Wrlsl3wlQjHK-G5sr7zLtGBf-NpfzPJ718IznQTVY6a_chBwFqGDCQ8uZ_VPPN8_n-UhgMQEW7JqKI3Qk6ne6kzxBQmfAJ1RY1rx2NBA-1V5ezDKpxUhJLQNNruXzvcxFSV120kvKVyaiXAmyDxy3TrizPk2tCvQMQCH_Epy3C1kdreH_jC9QEtTzeBzMr9X6NZ_UytGMd-USXQ2mAjwDGOdhMnm3M2MIT29JVSJ1D1kqUOrLgjiBNUWHvkkrBSJPUUYQYeZOJG1k9LsFVQv973fp_RfRqWu5v370vN1pTGDxR7Nd2Vz_cG_7o-tIVBZz9ssN5nog22FVBRBrPrYEBkDDr2Yrcw4bjWQaStERhuHX_BPCSSxn0KxhxJ7HZj-z_8JGtt9iMMJ_d856_cXFyCl-c5XDy4j3RqyQryn7D0Vpq5Dj5GVIwKJhBr5bt4my1bafY68YK2HwVcKlZgmr_NlWmU2PVrkPM_1m0o-YSnEWwmfYlGEos01_vReZE1YoZ2JyxWI_4O9X-Wx_NpD3xHXPn_xr6F8H3ZpdW5Hc3s5YdHvfelEAwuwqB85Nkzs7V2l5C0gQ8lf8wcyBZ6lo0aIu4qrUxgrl_KUQT_3o5ixGsPd9dCIxjwXAO02tNEamhTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=GSGHfG5hll7ueQNwPyacj5tKO7mzuMixobP58Ua2GTA0RNI4zY4w2PVZplPK7YF5XfvW95vydTAdq1C27EdzBIq7akqhHs5x5hibQyGMn71cATmf8Z4Y5krmeBI-wuL6KwPzLl2ocvochOFBV_zKc-38nWzCNZ5sUdjoXipCiyatwvcMLeWmolBxPCuG5PCPwlzwc-1f55olDVEwuyYDls-wo2PYtNVJxdcjs4ancvDtYHczcGAxS5pxNqn1APROiulhEnoHdsIcaXzdfAzryyWq-aVIDeHT6zBFw-Gf0wNX3ahXdf_9izwdQPJ1vx-mJPThO9WCsrG4APH8jSaWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=GSGHfG5hll7ueQNwPyacj5tKO7mzuMixobP58Ua2GTA0RNI4zY4w2PVZplPK7YF5XfvW95vydTAdq1C27EdzBIq7akqhHs5x5hibQyGMn71cATmf8Z4Y5krmeBI-wuL6KwPzLl2ocvochOFBV_zKc-38nWzCNZ5sUdjoXipCiyatwvcMLeWmolBxPCuG5PCPwlzwc-1f55olDVEwuyYDls-wo2PYtNVJxdcjs4ancvDtYHczcGAxS5pxNqn1APROiulhEnoHdsIcaXzdfAzryyWq-aVIDeHT6zBFw-Gf0wNX3ahXdf_9izwdQPJ1vx-mJPThO9WCsrG4APH8jSaWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdrXnrbg-0Q0q10qxpBxhh2jIIKeENzQxT09kt6VJEbbyAObe3S07SDT-eDFatcDkDkW7JFIlmxFk764-lecjvPv143-t7OxRnZg6al5mrZtN1K1Rplpq61oHbcPgK8W6dt7y3FKPjDoaA12NR3Qi_cHP_0V30SSUlwpqBRW1HHMcj2NTpino8QQoL05w_yvK5GP9s6jtbm-CcvkeW6jf_FHh7yIP9DBwYzqqQoyGe0H0a4N21DstMMTrREH--fUM-VpDQADLWmIrbSrUa9rfCyHVQaNK73dUfnY776mNjdUoqCDpMG5mhfhPibYG5fqgm4ggprKA__FUX8nxUjvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=rkei6yIuc5u4I2frIrAgkNiSf48qxEy2neg8zJFrzBihacltXJnabOObetDJ4o7ZALn-MLiSfW7kf_C6p8ma4aSJloAgNkmY3T_N8_VtLoMgeHQFuWzDmARZ3MvkRx4AFGxmniYSPQIEIpd60DXOwkQOzycOpwkrPmdkPjaSZ82m-b1HgSjMNvY9SKSa8l-jQqLo7jL025QyeqzKG3WkfG7Y5ogV-tz7qx0oQKhtemWw2yMAhiDgEN4DFAlAON2FRnTzqmqmfhciBlclo4DA4vPuG_Yoha068A1iJ5LjCv7oLrXOGwSVanAlL1D0P_jHk9BvekMEh8t-xO8ze6Bmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=rkei6yIuc5u4I2frIrAgkNiSf48qxEy2neg8zJFrzBihacltXJnabOObetDJ4o7ZALn-MLiSfW7kf_C6p8ma4aSJloAgNkmY3T_N8_VtLoMgeHQFuWzDmARZ3MvkRx4AFGxmniYSPQIEIpd60DXOwkQOzycOpwkrPmdkPjaSZ82m-b1HgSjMNvY9SKSa8l-jQqLo7jL025QyeqzKG3WkfG7Y5ogV-tz7qx0oQKhtemWw2yMAhiDgEN4DFAlAON2FRnTzqmqmfhciBlclo4DA4vPuG_Yoha068A1iJ5LjCv7oLrXOGwSVanAlL1D0P_jHk9BvekMEh8t-xO8ze6Bmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TFxIK60Kih_JS3KXAs-aWeKuWgomtAyFXriCj2g3mq8ZN6q4xWAHnHgba7mi-tpts-13iTZdRM1TKIHMeWjZkYthX0ZnHNI9ZvYKm_OmWT-rYaxrzqz-DynCRzJz8iZl3QXYuZgVc8lTUeVPyfdMo_gX2q-D_As_NsUg9jRCiz8I-tkIpNXA1Ef7h2u5V78JWAEYlUjeC1OORY0x1ilxhChLmFgDEmm_bp0vcCFiDi1SyzW2L6TcUKwkGCBJYlkqk7D61M1aPTK26S0N74pI9ld_tktEjjjsS17QlvGd60cWN444pIuVae5eSLtoa7M6tW6Pnf_K7dztpj_NIjKoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=TFxIK60Kih_JS3KXAs-aWeKuWgomtAyFXriCj2g3mq8ZN6q4xWAHnHgba7mi-tpts-13iTZdRM1TKIHMeWjZkYthX0ZnHNI9ZvYKm_OmWT-rYaxrzqz-DynCRzJz8iZl3QXYuZgVc8lTUeVPyfdMo_gX2q-D_As_NsUg9jRCiz8I-tkIpNXA1Ef7h2u5V78JWAEYlUjeC1OORY0x1ilxhChLmFgDEmm_bp0vcCFiDi1SyzW2L6TcUKwkGCBJYlkqk7D61M1aPTK26S0N74pI9ld_tktEjjjsS17QlvGd60cWN444pIuVae5eSLtoa7M6tW6Pnf_K7dztpj_NIjKoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSRAQPfOF0gtGvHdpgcbqhCJveT2K6H-1RkSX6CaJj5sBht9M68mjORiMyv_54OYT7noDsfDskA8CBMg0XLEnlbavaume8TTQRC_HY7wK1rFHTyU5tji5OxsPGpIRJ1LuUqKp4FsYvzEWV62tIybUcAvwNZk01D-XqKE9UY4Q6mJeghffXA6aZXe5BTOLsSmn474ik0AlMX4Q3RNuGjX-wnbTwhKSfPw85P5FNMaxGd_icw3zb5MzMR91RjwuqkZS9uG3D6UjqoUqkwNEqEPealwhs2sd4xp8jcFfcc8LCy-YFBxVrq7RPdAPUgvaynreiJLClWRKuH3DNz5-tHnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C36wly7IHTjcRggleGnPwsWoOuvzn503NSMDWn1iBKWsCVK_w1ux5v6blD0ADeIP9MqVDoS2-Cvg_j6pOQ_LIA2zxtyLEQ3HiqCFhT3DWvpvpOmTCT4qAlItVd6n2Q2LxvOe5IKa97fCmUQU7dKKHv94zIvexe5w_DICT2ukiBb0y6-L8jD4wixC5BASahOB5USZQ7Pey-7_TKhzKIeQg56TCnUCw_LFbddsqyKr_YcpGMDVNMH4Ja4QLbCTjt0zn1sbgc9F8l6Dl3BL1NV8TgIq2wf_mDTCdpHfGvLhKSZpLZrs2IO6c99h9WLhTz45O2rOAXOkSKk1BTpJ0k9WPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiK_89SqufOT12SPflvc3lXBIh4h1VR-j0hA3uhuhSk-T31jeb8O38x69KcUsczlNji3v82WI5SWQLDfDJL5uOFrh5UerS-VR3JzcHNEG8EmmY7JBsW5397Cm4hJUxruLHGgmbPV3vR5mMTUKJ6UM9HWZBbX_rUJXw-zKia-0CAKBSaRK-kaOzV3BfSkxtfkgXfcNhfMiukXMEHO0_BZra4rhA9CeGGPS4ht0fJllTOc5SGNJhXpzOznzK7gO-xAj4bYFWDGzNmADmCu0fG7SKWQa0f60nJ9RhCVooYREXn-c3LalJlUD9TThC6X3dR_mbWIRuVuwRnzHe39A2QdEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N61AE_UDJ4KsnrIUGpAqVGddeDlXWXRarRgHydNVxZl0pHoBtRzIJfIdNifyKMYbX1F6i4H4-q5p8kNRvR2MafgKg3fw9T1XmaTTsLDdVu1fYhYBF0S33ZMYc_cghKIIgEV-XB3_BZ7rphDWvAPCI41WIxOIPJPJbu2GBQtABTVou9eJTa4W1vrh7Ug-Y7C3cKVCS_Qw1M42FNy_hbkyte_7h_tz66_GRZ6DECrtXv1H_x0ccJa43Xh8mYNeFoNr9LCo-c4rglmNu67gyfjP7ekHZoqjiBMIaoyRRyMevHveR9j8qsie2CcCBIDmjC8w56xEdm5HYw6EaF7Gk8OB_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUm8G_DU8kDttX-tjIVUI5B3qhO6CxM56CTGabTbFgDehNqLWBfM_8umxLfUXqIWLw_F5cEfwChNUE-3BpQdMvCjrhdEK9pHRnbJ0qZolfnWn2OSjc10WA-_Oww1h7vzZ2UgWBsWU2XRLqt4vBM53IyJLPjYxWg-YxeAc8RTM_-1UeYTKfj6Fn7qwFdJErvZeP_y0zGoUIWlHlcNwS_ZN47YfuiL7OyuWIU_Kwpeo9aKBFH13DTnNaO0oAe1dDanZ7uZFGZnFnHEbCjA8onRFWJaKrHXpjOLJBFmi2E3C2CpVYA-GuEFNvIt9_aqhnMoD-Wd7f5L6p1H7y3IyTFW9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIOrHu4ctZUKyTzlJbaxzx3_O7JajYc7CzIgR3CUsL77wFYqt3_VLZPicGqpD7qah6jau9J0alRlvdR80T-Z7gYK9vVbywe4Es1KiMa6AS1CLeBfb1Ck2ybExyt3lvrdFv_yx3hkZjdfF1Rf9NwzhPzQDbJsFK_-p-pVoGsZceggHfrLXUJtarHUWQzGuAeZe6uXMKiqMiMg4A-bHa3C4ZcAlHbjxijTRMST_E2H-QEnRZHhnwvQAq6HbgRsh6oF8nWIffRXB5J2zp1S31oFytJS6Keehg62HztSJ5ZpcleWtCmxoLs7MR8VLS93UHFIqioumoqdjFJN1r_-bstbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANWnQqkX5iezxMQJQjs2zAjoCTmLY5VoG1D8_7wWqPZ4g8bX8wxaKA8_DGHAu-tTt6ynvWspfy4-dKOBGnv-utXioCYp34c7QYjlay0RkmsIKj_Wf1mil6mehdfjD7DTFdwAfmLGdHd7LhsHO7g0YoNJEtZM8XEydKGDVQqkev9qJsVqZiptT6J_C6MyG_QNnay2ms4lB_S61Obs9ASrYf1s4Zn64WGL9qJldVtjDB8JF8CVLvRmhpU2wHFHAvlxd96E1cZLpVt7oJepLo-Vi4gABa0Cf-eY7OnDyoS8JkezFvxfSMbuCINj3RdtDYCAbdK1MK3axafHLwjqMFHKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1ojNNHpgT3yM3PRXOp3q1_uLJ8fdED5Wo4v8Jdpd1NuhQmyipomJP5NJdjmmnfHN4m21NgatZ49YxcSI-UwaGgezrMzyIRwQYueBAbuMFD8LCykCHhAJlole5gnuYfk_PuilkVGQROu-RWWUrqnCqTB0v3rzym4lJf_uZbyRqhFK_Fi5TbJDZB9_DJjDIqHVj0lGpGRL-EZYrUMZqI76jM0vLsAPlqx-Q-gAGcKSmkNf0junHPeWZFZ7zkmQkwFrXPZ1VkX5__iSBLH0rMoQngkgeLBsNdaUHgmdl1p7FcOwgmnvtDAevbCLbx3laK0XS4LBrg8cgqvUFoYBKcnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcJf1xnfegeNyyDWVvmiO5ihYRb7pX9cimRp6LIr3rumkjDFeMg4eWEvd58rPOKGuz-QcvatyOd9OO-5z9jig8qod8UeZL8l6iz4VfSgVaG1smqvcsG1kEoY9Utk-_9J2a9Gjvt5iZDtFm5dnLcKgHtXCPo-fXA1jSPse2RIcxzxiLoQG8ljxp-BEME7ZgMWoPagRPVS3Im6EijtxQ1VOWXxc7DOLyGwbrpkE_ck97596g9QDkO1gw2V6gi9TM1Z8VQJ6tuCqqsHT8f_jwiptq6SpFQxX7kLEvGYLzq17l75CKo4ojG55phwnBY3waXH7ZNdfAGWQh7fvKj8HpAH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mC9JoWn_nZF0q8zvs8YmaCtMdfxM6Rarfsg-T6NhoTzoA7Rci26XGOwqZsKN4moivNrWalEf74ouVGgqjebCKMvjdaiW23_pTEmJUUfzb9gyUCOZqAcR1tCJbdGdlJ_l2lcb_3NCTY9TfzLL1ilf1Tkrh7_UosFuS7Px1H55pEk1-ZwBTajSW5Guci53eRzHbJXGGb9jCQlN5kkADCu8_9zL3yQs-9QZ_WGb2bFsRCEqNdsmye0GbG10ozyX_OxLM3l2xDFv1xVtIQv53Gh6EUqXhYrJw9FwGw2hw9i9aN1zJYCFequDRIRm8EvazZc5JUWU5LgqbD_FPbsC89DQPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ie550ACEPFJFV6eFisrPthGyUNiRLefi8MxjiNkQP0p_4zetczOqrcfy2DQjETf4Y7ExtUc48CEPaN-iwiwSnxf8VCiXVIur0NDLJASorRH9caquLoHKh5iyUtqZspPq_o2RP5VBW3h5168YGQZuk6jvROG15p9sa092S6jl1ulpjL5RmyXWeW_s2qEI_A96vZA776tHLFRabEPfwiZ7rlMLc1Ttxp_8qL2Lm4k3BMBE-o4aCiGtY-XM8rz9EJ7yIRRJDSXYiJ10TTuEWJYsu2e_LuoRYUsfkRlVjESbUPvijQDuduxM8x3PDGRMPocs6IB0PTq7jYoOOuBmpfi52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ie550ACEPFJFV6eFisrPthGyUNiRLefi8MxjiNkQP0p_4zetczOqrcfy2DQjETf4Y7ExtUc48CEPaN-iwiwSnxf8VCiXVIur0NDLJASorRH9caquLoHKh5iyUtqZspPq_o2RP5VBW3h5168YGQZuk6jvROG15p9sa092S6jl1ulpjL5RmyXWeW_s2qEI_A96vZA776tHLFRabEPfwiZ7rlMLc1Ttxp_8qL2Lm4k3BMBE-o4aCiGtY-XM8rz9EJ7yIRRJDSXYiJ10TTuEWJYsu2e_LuoRYUsfkRlVjESbUPvijQDuduxM8x3PDGRMPocs6IB0PTq7jYoOOuBmpfi52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goh8fsjxv6llMkn2390fHvAqXz8dWFogoChgNuoW8kWAL5BQirLQc7Ld3UM0G2kc9Gf_YkgvSGdzm2h61e4wKVVQpR3Z_dNmvFPLY56ez0W1BC4obB1OodLkaAA-i0xfiMqskiCe1qera2s0ubm3BSEQW8t_QFA6jKelgGy8xfasTLVHy01N67dFspALuvfi9jtt_TkxG1oKb4LxyNFwkzuoy0WJkbdNJVgnWva9GdL2Aa2ip7vcOMB1PLl_S7ZkL-LwJu0R7JaPDe3aHneSfFbR85YSMkbPs4qmic6bAAv4Ysu1_7t-FVqYXR3Dpd2JhQgtVE6y09SlXhs_7sx1bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmWPZLat2BAgmfyUfHagE0j189uJLfb24mkKMuB6MlLaOGzKYn4AodSQczROIQzdIqXgHoee8evM9BPpw3fowbQlptExgVA59tn18kEgkIqQ1GFgvpnswkMEnvQc7926nNdY3cLNtfjk1W9dJlRbPAqQy6GZPr9SDaLl05QJelKlYCsTSmRYtpxkDUZTETLGClWRzLYDRaXidphS8AUv-tljW-XKByNw_H135nViFaHK4cNTep_WptvrL9XQOkj7ZuD_5PkTaDDVLwYWGBPXNCrmc6yjqZyr-tTyfCbropwKM5cl_s4DEtDMp-4OD0MqL6WmIUlf8VgFafFjr1x9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=AxwS2eCZ7UC5K4wcFwx-vzcdhTKdS3VWiG9F_7RicEpyvq0AONeK1LXx1EcaCa-od8mWyKPvlj1p3JRFF4qkXdAcY3v2NK3Ba2a47O8KcwzZLNYOwjJ07O0T_P4fNrnrXJGb2JrZbfJKWlysdiJ1GsNc5mp3Gh0hDALGV8Xt8ZOWFW5pIIsCyaP57YNVGTqEjeRiNe4G2Hot474T1U5oodMrcqeeGv4VpC8-8tE41mYzOkHDBz3txqK-V-TBSHfhiIZCgmckb2ok7SI0Rf7zWLXrlCFgl56kPK2pOt1JrnyA_z3J36WSRKcYOYLYdGeio_MQQtCtfaK6ZvvzA62L_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=AxwS2eCZ7UC5K4wcFwx-vzcdhTKdS3VWiG9F_7RicEpyvq0AONeK1LXx1EcaCa-od8mWyKPvlj1p3JRFF4qkXdAcY3v2NK3Ba2a47O8KcwzZLNYOwjJ07O0T_P4fNrnrXJGb2JrZbfJKWlysdiJ1GsNc5mp3Gh0hDALGV8Xt8ZOWFW5pIIsCyaP57YNVGTqEjeRiNe4G2Hot474T1U5oodMrcqeeGv4VpC8-8tE41mYzOkHDBz3txqK-V-TBSHfhiIZCgmckb2ok7SI0Rf7zWLXrlCFgl56kPK2pOt1JrnyA_z3J36WSRKcYOYLYdGeio_MQQtCtfaK6ZvvzA62L_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=QEo6lLNZDo_blNF10aA_mtoD1Ste623VqIAbGPMRKClwYHTMVNa7wUSBRPCG8aXK5VLgFUk8qYjtOh_3-ZZzawBi7rmx9PkZBAjBwsvKgfg78TTfMdyyPGAiiRSlV5pZ00gS3PifsgVqarZ2UL5o0ck6jjyKK4wZn3YdVEMMlRxOT-j7uQgtFRXCE3fKwwN-F5ZdWRs0ahjpa4P7LrFqQT7f-QE6jyLZc9pUCSiz3PpkUvulAWz60_H0LLg7MVdioh2eWhqBhJVyx4LWgvatXnh5pBXsIXoLfFvhel8NAPB9Nyr_nRELBnwHqOkwsiRBY0oxGDsitkqsPuUEtsi5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=QEo6lLNZDo_blNF10aA_mtoD1Ste623VqIAbGPMRKClwYHTMVNa7wUSBRPCG8aXK5VLgFUk8qYjtOh_3-ZZzawBi7rmx9PkZBAjBwsvKgfg78TTfMdyyPGAiiRSlV5pZ00gS3PifsgVqarZ2UL5o0ck6jjyKK4wZn3YdVEMMlRxOT-j7uQgtFRXCE3fKwwN-F5ZdWRs0ahjpa4P7LrFqQT7f-QE6jyLZc9pUCSiz3PpkUvulAWz60_H0LLg7MVdioh2eWhqBhJVyx4LWgvatXnh5pBXsIXoLfFvhel8NAPB9Nyr_nRELBnwHqOkwsiRBY0oxGDsitkqsPuUEtsi5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO_bSPnWS4OUYkQbJqbo9lZgc96USfyjDzCoBXNLKvp7_SdXJgUqkMvegM2OnOZWa1SxGXWd-E8fPNF8el1d_s7DtESwOTEN6KZy831SSFz5fVXDbTzU8b-ruNmjLiDcttBLyO9jry3hykoUsJn8Ot_VTg5ZP7P629Gphbh-54ZWY3MFZeT6EmLW3JnSCUewfF6JqPx4D6jFU2STI7ZkYD_hjbglVyTclHyqRB0NCrMbeaEuT8E9zjgPc-_5Ui7AXBMrJda2L44e01UNkutqUkhrTMceOCloFzZCA01DYcVBbt3BJD9Y3mlbagOkodukZEfpnih8xVY_t5fdWMOBKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTlhANUnAdIpnOuHTb7FjSioeZdI-FyZJf8NDb0muXlpAG3yY2jzX4xrZ4Il81JqMwLVzMvHqaK9HWjwz68-EoolmwBlqMq6z3544Sj4sfui62reL40BhZTTvep6EEzM3C4lf25wv6L4BKuoLvz_mbxyVMTJbCZCNdrkXgPSFeqXrmM69gixIFDBOCMtiuc5i1rrl9ZrwbuzBNoUGeXWD2wUzMnSOxU0qYug6fXhSl10tzEl4bcIizSlv7qu9ushvsJkYnCEOQ8X98XjRQZQiaAKP-tib5-z3HrftTNHDTmcoCvyk0LyeLrpx5Y85HaChswDtFF_YRlg2tJYg2dN8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE_gdMdsd8fK9n_S0X0vAbfwYBUtAU5H3zqO649PsDe-wQt3GqK-XTxk6yh5jZIlEmB-y9el4ImcPeesafUJlGvU8K9SS6eQ213vPmNd0E6Rab3zeMNG4nllB5sIRLq5R1nZ_nuGzRqLpDhR2CfpMcxGsmZgVyExJFuFXfXz5BiC_co9wE0i9QJtgLowoMFBvQ2evSQo_qFyvh9MfoCEXRLJAwHZmxeyXbPYGw7za4n_uf4W84cE0Eu2gWLMazdSFj2vVLDXGzQ27Jojv_b7esZ7RD94K_Ef5hzP47Hd7Yipe2dHmyWDNcGB-IL0vZ9nvv1gQaWa2jNNr-AKF3k4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1tvJln2jWln4uc-jYLLQ9OsBHYlZ1lSPaTOy5SMUqJ4nMCFoRR3_tJ60DP4DmEQvadMsH0G86zVbOvhG-MsbuvQmeVIXvOhUPkl4QHs5AdIwbwjf8MjGz989XyQRckxXrwwOFaIKGAEn5lAAiAL3M6x-_MIo-3FiUKjAz7N82cnfhwOQ1p9UeGxmGwyrxAlv1xutBYZTCxQiKdZ4LdzorT51_eJ3z_EP-Idg4172l6cEjCLeTG6VrNRgz11L01J-vHiA4fVc8Xx_z7teFn-7qeq-GIWA8_Vodry2uL2cloAhHsFGzKvqC_6iIB3Bvofh6h_gRYtrk97GzNEyvsppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4cBTEqF4b7fUIziJbQjfNDMXQWvO-JnfP31-Hb09teUn9Zwi7FdaUTaJgapw_gAdDbh4xYKcGtA30HIvcPQ0E3m5RGi8UkobsQXx4SUL0mQCWMwwDuuBzbZmTha0sOhlNzoBsjJCJX0gXkm5fRC-8SmS2fFIhsXiqqCwkk2emi-zSQJnxDAoLiydNnIyGXKd1RXO119nNi89AMss1_IjxudSAnEvJSx1cZ0WakZ1SmtMvIdu2aKug3y841g9_VUxI4Yj0RLSLy9dbDm8Gs-mr47nCJ0vMcpSsI9Yj3DoWUGNuj5N5stlYiobBXe7eJkgM_6QDr8TWmvL6WI3RXrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri3h8vcrVFnlIsEobkWxJq8JsTBofR1IQ-URnhqw6EORA0nTGfLXVXt8MyDNlqaPClLcekJ3mBOO4AABIKV6RcZVjwEfO39eoAff1OCMpGVtywXBDXTsnPWbbNUJCvMd8tCklV7jw_yBFAB-E2JAmhthLL8UaWa8NRI-CBOYZdSa1hLijAZMaFQ7INB6pisVg4CNpYTEykHF9agnjJvDqPA4qjMuktzQjb7iQD7WZYc6y1C8fxKpPsccwivQMTiEJB-Ai8i2t7aiN1yHLojqH1F40kcDt4xZ3yw1Dm2OVMi-wg3fgggGptzilhavW1sD5W1waSF_Oso-oeuWLGMbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyFwGe89aPPXVhcU4g5WIBaiIZAKhxoF_73BcE-ck8ugQ-tiiL0u-F-sqC-9dCSSjQ0iOeVkDJFxD5eTnyAtTYO-IQYVCfLnx7u3ExVaISYCcfa9xqHN2xhQUF6pZu_OlP2oaVNXp24ar9KAlEZbdJSOCYcefGaTvGd87cysOlkXdHtNIVnSHyF9XqqLvhSMOPFDbdWXCkylF8Req3PI99P6Qrv1TYx0m3kARC-h_wRZCTDPbgOeC62Ih2RaKeF1EH8tn_9N4mEQzVZ8qRpC9erRi3_RzTE5QkM4jhvHLSr6MW-XsjSJXX1wxWr4vLa7jM-qkzOUAP5s0uEH-NKNwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IkUW8iXnnWKpAZp_emkOXtTtFJO0VoBdEMwsfQXnYFr3LxHjQRn4o5bzz6HnKcBT6ksNqN8kBUzpIf9psXPqDOvBg9fgGRfsHuy_yH7wPXXPK9M4gyeaqS8-s7sM7lJgQiI4PPmhhbOMBsc5_IXqdpzOKbN4lNMRGuYXmq-97Q1FcwVJeO5qV-5PTrUki1-Z84qGRaZEcJ8Ui0G9Y-gF22GDCbD__NeazfAtTNg9ibjR9Nz55pHgk8niUuucAyb149Z691F5zTqsWJmD3rafFlvt4ETF13pbQdJ-UQpFzy6dOzbZomUljkH0czuceW-_QOf7jdXziBDk71ADdRvcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IkUW8iXnnWKpAZp_emkOXtTtFJO0VoBdEMwsfQXnYFr3LxHjQRn4o5bzz6HnKcBT6ksNqN8kBUzpIf9psXPqDOvBg9fgGRfsHuy_yH7wPXXPK9M4gyeaqS8-s7sM7lJgQiI4PPmhhbOMBsc5_IXqdpzOKbN4lNMRGuYXmq-97Q1FcwVJeO5qV-5PTrUki1-Z84qGRaZEcJ8Ui0G9Y-gF22GDCbD__NeazfAtTNg9ibjR9Nz55pHgk8niUuucAyb149Z691F5zTqsWJmD3rafFlvt4ETF13pbQdJ-UQpFzy6dOzbZomUljkH0czuceW-_QOf7jdXziBDk71ADdRvcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJiAH5PYzwaAUlS3xVVDjmZq9CRinoQpPZt-lTU5t1eTZSF53fCZWO5iYDJGAOaFq9Ip7w0iCuBzXnrnzghVzuFFIAboPuQSH59-45xNK_tUANClr8WCNjaJL9qYyYEhEXdyxxn1Yrr466AcvfUf7eYXHD12bZHlbalBehOx6_IJ6S3qODelHAPUUeYMzz_WOJLm1ri21x9Q566HX7ikN6GmdbcifDCLYZ4hoRkFEOQb5dnh8oM7ylPNoBH5eR3dYp9e8TOltS6rS7GRMKHLaMcqx4xks4EPWiUhq3ghxnVVsrHl2F4RdBc__aAHY8qv53OP2gHGDzZDoI6dYPafmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ADspk8VSdW_mkVT7YftSFquQzcrWdyabdAQGZYJAorBD8qk0RT4UsZDg7FQmR4Z-yNLbbBnOfXFgZ_oLcXUE5uV6nwXVPTW4ORswakT1O9hZq1GO52FID9ZTFMg4Q89MrDW8f3wVZfnOmnw3c5wiqWq2vWw5Fbd5HS7jeFmLXoI8_nPRejiVTf5WA8baTOqcnIbXk-6iLzpFVd2KwOk_2ow6kRJ9sNKMonTR05aoRA-f5lF0s7Q4PqP1nxdI810or1gbu58DmvzSf7_KqpV8eRge02TWD8z8eBchzF1tgovqMH4bs_RQ1w-f3MWr3N_ui8lIM1Q78GVhERCQMSIQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ADspk8VSdW_mkVT7YftSFquQzcrWdyabdAQGZYJAorBD8qk0RT4UsZDg7FQmR4Z-yNLbbBnOfXFgZ_oLcXUE5uV6nwXVPTW4ORswakT1O9hZq1GO52FID9ZTFMg4Q89MrDW8f3wVZfnOmnw3c5wiqWq2vWw5Fbd5HS7jeFmLXoI8_nPRejiVTf5WA8baTOqcnIbXk-6iLzpFVd2KwOk_2ow6kRJ9sNKMonTR05aoRA-f5lF0s7Q4PqP1nxdI810or1gbu58DmvzSf7_KqpV8eRge02TWD8z8eBchzF1tgovqMH4bs_RQ1w-f3MWr3N_ui8lIM1Q78GVhERCQMSIQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=B56o40Hca6k9OFS7KfHJ5WlbS5sbzYmjZySzSutcOXMHN3OZKD_B9CXcpQBv4t0EKvMgzqQeuXvmABNxaFywER0yOwqPz4tg-1cSvIVfsQlTSYWSrWO2tnae3SEh1W14XxfnJtRWJbYllhtifYe8KE9dtkeB5YYlIW-EupmLTmyrsHmVD5t93eZLeHX7Fv_Qg5R-Zns32DpdGuWKc_xVwd-tCY38W7yA_7HC-yX-tQhA5EWJ_ijpQJiWoC80ciKLhscSHcHq8BZKYO1oEV2yPsAvnRV1M64ZHWxmbD3tgDqgPJ9BEdl4H2pZuvX45lCci-eHHQqsg4aGGtIvdBxLtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=B56o40Hca6k9OFS7KfHJ5WlbS5sbzYmjZySzSutcOXMHN3OZKD_B9CXcpQBv4t0EKvMgzqQeuXvmABNxaFywER0yOwqPz4tg-1cSvIVfsQlTSYWSrWO2tnae3SEh1W14XxfnJtRWJbYllhtifYe8KE9dtkeB5YYlIW-EupmLTmyrsHmVD5t93eZLeHX7Fv_Qg5R-Zns32DpdGuWKc_xVwd-tCY38W7yA_7HC-yX-tQhA5EWJ_ijpQJiWoC80ciKLhscSHcHq8BZKYO1oEV2yPsAvnRV1M64ZHWxmbD3tgDqgPJ9BEdl4H2pZuvX45lCci-eHHQqsg4aGGtIvdBxLtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kui1i-qQoFp08mg8WOQdZodPu82w9fa3b6C7veHX5GwPEpN8r92dKBFe7FNXEOCV_NI9argkIdjvx3KWt8ozOUZFuf2M5knfsmTCGWEIzsh-ZZnjSIBsauVNHgxfsNw6d-EJNkXguRk-_XJ3FrTmNtsxIClH8_8fwAUIwJzeVHQmBL2wSMww9exGYk4Z90827ZrvJZJg8Pj2weKjQ6djWoE_WZCdB5lhBgHS01Q1giQxfh6LqZcznnahvOMa4uxqrqKNWhP-5gkHlQCCwGbhpt4aKAdV7dW9kMI_zwa5-iHhCifPjC42niSaw110Iix9rb9xqWeZx7SQnIXKbcoMvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFz12qjjWJsHanqK49Vu9S9Jr7vv9yOdAEAVMc_Ky5PX9OzOq4p6AiDwYVdTvjUNDThJp4Yq_3iGyyk7NhQQwEk9xEjmXVrw_ZhM11zWCtjHm_qh3yOr6yvkdS0TCN5GAlup8k8t-9_TSm_L6Mkof3kJRveNJ-M2LA1qwqagffkoTAn2uat9LwwSh06WqNWCaRLhfsj5RPcnYHoM12haUlFC8LxNYnCdMtd9Ss8ZanjTDCe-QD3yslwV7SHwoG433apkbcYVMG1k7l_Lhf0zq6LFZlQDvpP6rAxFzqzYnqrMQMON19k3VQnUwYkN-zakoACMgtpFlhnPf_YriCMb6g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=soP9ac7Y-CcQAhJD9a8zzE_NHIrWw1flymRDE7mnecrz3x6zmJTq5Jti9c-oo_ZYw-gR9S0ZtunmqFh59L52EAOE7ZF_9P8KYmw1xdGWt3z-sZMT_ZkoI6ikiUMTax2lkfcs5V7bcf1-_1VP_PvBEheZGbKLproZ5v4p8Eg88ylPu1DTYedvF1JTJL_wbX3RtZ8Y6U91A60gvPBvfDvo131VLRsOGzJcSVcb5qViOx79mR1y8Wq5hMeXIW2wnb4FS758RhDrOe09A_Um9o095f5NV25JNp3G81oTp-YShsehBI6i0Psv8G_Z6qqVilvoQVkWr5qHF2j85KPFhOy2IggeJBVv4nZRw2p33BuzHZAoulf5bpUs4qw6U7ZIhTZK3YdQ6QhVdL7b69QIwnuRAGTTTgJfHU7bUhJXfn5P_4Nm2DBSOOz2r-UM75S5mXKkQHoxLeVOxDkMFd0kipJcW5MAGB1OuMFRz3TtQ0A9Ao_ADhTsOsG74ObsxlVp_YrqPKpSSgREx7AB_o09cZU4cVI9DXv1DxVCgxSpRYKhBZShtyX6MxrP5rfwNAub5ZymOHiqSRbRxyrguUDjLil0r-0RG7Y3KCxJYiHIqZRQVwQaf7Alx118nxz57rMhkLWnDkrMlajp2-EoxgmYz9T4u69ilQd97n9pt8ejqE-FZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=soP9ac7Y-CcQAhJD9a8zzE_NHIrWw1flymRDE7mnecrz3x6zmJTq5Jti9c-oo_ZYw-gR9S0ZtunmqFh59L52EAOE7ZF_9P8KYmw1xdGWt3z-sZMT_ZkoI6ikiUMTax2lkfcs5V7bcf1-_1VP_PvBEheZGbKLproZ5v4p8Eg88ylPu1DTYedvF1JTJL_wbX3RtZ8Y6U91A60gvPBvfDvo131VLRsOGzJcSVcb5qViOx79mR1y8Wq5hMeXIW2wnb4FS758RhDrOe09A_Um9o095f5NV25JNp3G81oTp-YShsehBI6i0Psv8G_Z6qqVilvoQVkWr5qHF2j85KPFhOy2IggeJBVv4nZRw2p33BuzHZAoulf5bpUs4qw6U7ZIhTZK3YdQ6QhVdL7b69QIwnuRAGTTTgJfHU7bUhJXfn5P_4Nm2DBSOOz2r-UM75S5mXKkQHoxLeVOxDkMFd0kipJcW5MAGB1OuMFRz3TtQ0A9Ao_ADhTsOsG74ObsxlVp_YrqPKpSSgREx7AB_o09cZU4cVI9DXv1DxVCgxSpRYKhBZShtyX6MxrP5rfwNAub5ZymOHiqSRbRxyrguUDjLil0r-0RG7Y3KCxJYiHIqZRQVwQaf7Alx118nxz57rMhkLWnDkrMlajp2-EoxgmYz9T4u69ilQd97n9pt8ejqE-FZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-szT2CrDonSxRmhOaPW64eQtm7SMgd8TvHCCgVFziIqEm8SxzEoFYuLyVk63q2XugR5p6grQDtLyJAyITogH9bb_fbFjSuOlywu9uhG_jW1rY6Q6-RoVBbli6SbSV2l77jvUQLCVX9as0GD7-83y4AH6UUVMPiErNaWMbsIB-6b7G2uaSFZro_aRE2_xQDnKOfYcfXvOMYKI_SodFdNilOvgVMUkCcAcq0s1EuCiDY8OVm9zDybguT0kwzbzewiCzymJ1qaahCDBFbAL22B2cMlz398gJuqBddSd1aKCpK2D1oqg2XTb-Urtgr3BzsUrViRD_hLrLDivgNSuuporQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=X_3Z3HAwIn96Y0HrcYx1m99aNe-9V88zRHf2WIAMABbDmsWiCfWpW1UymNzmX-hgPD4jmWgepMfJOfyWj412Rv8QyMFnr2-xWG8t-FTtexlL_AFTSNNaGUCSpeKuQDv5tlztpvRHJqM9kJszLUOpk4eOkyOIOMdT2sB89-FKBVeg1CKk283CW6lplmNej7yy3n6VPmsGijMZpHZiRS6HgFCG1nU0-wPU0zRKuAivccuZJtsINbVtpnczPpj1aA8l4oZlIUU_xgTKHsscMQIbtj0QONywMgCgXLexCiZXPo9tEyGe97cawxM9mVQDEVRaXwvyW1yItTVB9JMENDvN94s5_PXJFa12cfPIfCgPu2TC8v2AhINlveK-K5lXTYteTa_LbzVYFCxp3jbLOEhe4qACHqoXHuENOKODHJS_yqghw0rWfqf5H9bFirO-Cf0Hc9BQVsr3xxKEpGMO7bSQNWWojEFUyYQ80eplfyPA3pMwG7_dBI4-YjoocQiD9T69RUaBnwEfVtcOVZ5UghiY4_LgM_t_rlH3TSzJYj1zPWdQznHwxx9ItdM7THlaMt4pDdBQO8k-z8pN3HrmhulW75D8Dz35fqI279wD6ctORwYrU7M5OimGfHLxRbhGt1cTHo0Y8EC1AxZdAnIj10nyJKqjEuoasCBamgumuyKX4UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=X_3Z3HAwIn96Y0HrcYx1m99aNe-9V88zRHf2WIAMABbDmsWiCfWpW1UymNzmX-hgPD4jmWgepMfJOfyWj412Rv8QyMFnr2-xWG8t-FTtexlL_AFTSNNaGUCSpeKuQDv5tlztpvRHJqM9kJszLUOpk4eOkyOIOMdT2sB89-FKBVeg1CKk283CW6lplmNej7yy3n6VPmsGijMZpHZiRS6HgFCG1nU0-wPU0zRKuAivccuZJtsINbVtpnczPpj1aA8l4oZlIUU_xgTKHsscMQIbtj0QONywMgCgXLexCiZXPo9tEyGe97cawxM9mVQDEVRaXwvyW1yItTVB9JMENDvN94s5_PXJFa12cfPIfCgPu2TC8v2AhINlveK-K5lXTYteTa_LbzVYFCxp3jbLOEhe4qACHqoXHuENOKODHJS_yqghw0rWfqf5H9bFirO-Cf0Hc9BQVsr3xxKEpGMO7bSQNWWojEFUyYQ80eplfyPA3pMwG7_dBI4-YjoocQiD9T69RUaBnwEfVtcOVZ5UghiY4_LgM_t_rlH3TSzJYj1zPWdQznHwxx9ItdM7THlaMt4pDdBQO8k-z8pN3HrmhulW75D8Dz35fqI279wD6ctORwYrU7M5OimGfHLxRbhGt1cTHo0Y8EC1AxZdAnIj10nyJKqjEuoasCBamgumuyKX4UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En_PqCh7Da1T3cniqDbZaqgPcXEPVDLQd_Vkx6TGF40BBMzlfOxdhqoARt45a13w5BJapCEE-aVU7icfsB6_CLrhmlAmmYC3wnble4n7ZXa-SdUSjfdis-Srki8uQubB8Aq0IaREbxi4BQq7oa2_pyJ3twtSK41cXlFgja-c2hcLKute27WBqqkJmLU2tmZmRpnLAa7h7HiviY92wmrfUt293SKH0iVFCQoR-qbXtgxLtp0ueuKS-5Ut7gstVFg1IGmhG5e7QFqPXnJJEiUBq1f10_Penb5iRZXSe7QZ5xhLna6xiBKTB9SsvMjvND3lzPq4iuO-wowdbF6dZ5GsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE-uH0pfAQCVbxk5BoYVp4ymogU7vhD55dOG2ydX8_Zne8n1ZWNPNlhhu_ZjSrFARJranszS3mCYbGDnyaO6BdjWV6CnCi99rJ3z6a5OwFNYOvBXRqdoatpPZoktG1Arx3KWJdE5b1f8PlYmXyGDIzPsIhyRMABEWxVGmKsi1lxw0pxjc6DabtLUXG7w-Ou06GT_jwSBcAKpY22RnB0cNx2ZAptcdos-Eiiqgrgzhl4q1v2AlsJX4F0Jz9TblHuJ18eV7iUAgxiDCcLmjJfxPHvekOLHjRsGOz7VXdq-hkHXqXpP3LVB-zDmdFxg9vzqyA7tGjgkYTH-yof9RBVHEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3-D_XcOOvoNALSgMYs7Fzuq2CNMmUBi6HLl_q-_RvPmYqyQn2AiQ-1ac_2z0R9g_Lrf1gkls-W8sjYfQ26D-d9SO_oXMQ-t9bTPcoaZND27lihpCY_cgfBcXy0jzs_utFgiU-v0pAnvzi7WMtjPXlhGI0yUs8WRk9BNXg_DmynmcSnqUhLhNX1lMBAYo-RBrbHnXvuxBbbBb82W1byLGgcElp5SUtnNVTw8JRLz1uDJBzYv1jGLN2r00y_M3GDE4FaS-ZFp7dH_ggjJlDlwOcMM-yZJ86QU1NONgW-nwjQbHaveU-u4Ybcib1fSJTJxWZuqGcagAxWr2tcokoRzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
