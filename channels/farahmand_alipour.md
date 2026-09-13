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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpWCayyCDAcWeSRoAR-75XxigAGnv03rHykX05dJFvbJ6GNXLc-pYVME54ma_1VlicHZ0AwQc4gxuCMxFIN_YrZHninfH00q0QP1j_DRdD0rVoTmx1Ktx8gQJXnRT4Ez98XV70YgIjeKw8jpAfteTUR_HgdrWozt41aDh0lMRMZin_Y93Sxg2h8Yb-Wj9zd6PPz3oSuYWBtn9ICgJyx3cKIFW9QGmEjnaoBYLzWxv388PsgoQEJ2nI8-I1Pc3xHsHeav0-QtBK3Qq8OjeKv5MLcqO9MllLnadsnyXD0P6TbiRqZ0TUTPzRTEM6NwtarJlxZ9EtASKKbDCenqGkHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLiQ4FBokT3AOJ4itMQfY3E0ZLuauYCwXNfTRPZNjSzB2FoHYFw7lOXisV6DKzkhxKU7JOyyR0KnLMOQGTWqzXkJIkv5tpQBQtEfO0DkC4IRu55R3QAFtupFUc8QmDPtyASVZM0_OjUb1rXSnunjXUf97bHrgQ4W89t-MQGmVHiIS0W9LRqA11m9Oj8mhSTwcs26wkhqqgWjhIrCnQuOW6SCQqU1Y8b3z8OeDQW9MlcppnJYthWRjybNBdQRy9cNWyUPGMSFjSQZ7CPx_0OK0DHj727kZ5lvgS3_FArDk5hLqQhJL-pFXRM9lal9VANNNNqk6M5XQnB0pAUH2-cTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=NsTOySuvLmtYRQ9ffGBUDW8wzzCmu_P74KE14oWbMi7r1RSSkKOhN-hJqIrDnXrLZKLnlJIedf0fm_AzKOtQCn2xId8JhexyUZcnHeXRshykEcY0A7rlnwinmEX5lBJwB2V6cud4gDC25MpKKZ-GQtfxRv1DEhpX0afwDifTAwcqgYEf3Y_rD28ZrDOeYEtWUCsSK2AdyQUF1WahtiqYzon2S8t-GF_g4DY9f0GHJaBq2cV5j0zBh7iiS5Hbg_VfrAS6jdHJqDDHZrjMbVqcAT9eGpOjvig9UUnrmZxCNsi5lwPbE2WFgAK6BHbDakIi_varp9A59mTllFsTcPubgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP7VO6RdBJ9OxLlg-59rkfY8SRB88j2_IoYISTco_qZpJMXHBykjn6gVqNUaJtNpLkPk574xHefMb5e9Z5m2u16ffQ3F2n8RKylF7DVl_2QXUz-TS46bxk2kN6iDjljREUrPM6DwgrljTutYlAeiVFTYw6iHUjREVYFWRD5dzrMhJIoKJiixH-Cbtm8HNYFS-xuQTFWaJnoGkTQ0oOaDytYZLOD5Hhr_-_EVw53s-CRLCPtQREazGfkgfQjjBsGm2G2d8ADIjYtJk1X1YwMXds7h9T95UtQq11iiv7sn373fNubci-P3tPGG4KmPNlZQJzx6hyOoo9OUn3XpMW0Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VBL28rYvvjxTICiTgIqJpP8q0SC4nFdHFQGWyIleEkaM0y_q1EabY8vMgMZeKW-akG00Mcl4WplQujLJlOAFuHeXe5MK2KjmGes9aterRq1VmZVyoc3ur3e6WDDDoeYTPgYL-ENItfJi7BKSZQ6CTKLe9OBpaReXdLmgEr4N3rmdo8gfuZnmmBmLWPcuS0xkOtQztJg0wErzb-03BIbwc2XbX9WYsXsm8k5XwqoNZpn0ybiDE7JDfHCGCm6PHwXJYqEPuYttPcFdRSHMnwQSqe817beN6HOCDVkXbid4n3laln9VaQMOK16npuY3WY2vb3olkMpwH1J_HSZB1C69Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=VBL28rYvvjxTICiTgIqJpP8q0SC4nFdHFQGWyIleEkaM0y_q1EabY8vMgMZeKW-akG00Mcl4WplQujLJlOAFuHeXe5MK2KjmGes9aterRq1VmZVyoc3ur3e6WDDDoeYTPgYL-ENItfJi7BKSZQ6CTKLe9OBpaReXdLmgEr4N3rmdo8gfuZnmmBmLWPcuS0xkOtQztJg0wErzb-03BIbwc2XbX9WYsXsm8k5XwqoNZpn0ybiDE7JDfHCGCm6PHwXJYqEPuYttPcFdRSHMnwQSqe817beN6HOCDVkXbid4n3laln9VaQMOK16npuY3WY2vb3olkMpwH1J_HSZB1C69Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n29t8gjZQjuybNXBEN5v5XCnd42lvLlz_Ei0e4K2IXVMb95KU6T22oywkGQNKYguzgMnb009ER8SSHqclneZpltgOcchj3CDmk-PNyobHu64SqEL5J3GMWmvvjg1vJUr7E1L5hKFSWY-BQRjqdZAukcultXa0usWqKUJaDaPFX5zlMbY_zfK2WJDB5LvFHKoqOFaWwmhuDJtoh5SQTqcNeJ1aP9GeAcOBz-vDOL7Bm_ZN1GwucFBXWYKtOmZ4PG-fwM2EvsbZTFiJjleRiSsB9k3RMbzSgAGJJdanSGL7q6pqVo1KKwVS0sh7MEetIoCCFbJRF-269sM7SAK3V7ahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=me0RhBivwmWn85qpoDrTbVAVaaGTW9oPHSRAdlPPdYUXZU93pvnRLqHrAyCMUp62mC8SoouHTtovNLu8pf5r6JUSARcpC2OV0F5xpq5Ju1Q0OVTTqWsWGqVoyde-8CCrArcPHQaKALq-b5R0xSuWPNEBTBL2R2L9Z_zEXM8u7AgvmRuZqi70SMx8usGyEWWTtO5ZLED9ryH11w-u68HoI2rvJclcaPes3k3bp3HHQtk04MU5JN_A2rIXhEsZW9J5VU3hL4ME8U2AWOzLT0hD6uBxTfjYUs-LyG-kN6VIS82RdjOdMc7r4w1j6mv8dqHa1XsBiIhvbFmMZriikmqM0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=me0RhBivwmWn85qpoDrTbVAVaaGTW9oPHSRAdlPPdYUXZU93pvnRLqHrAyCMUp62mC8SoouHTtovNLu8pf5r6JUSARcpC2OV0F5xpq5Ju1Q0OVTTqWsWGqVoyde-8CCrArcPHQaKALq-b5R0xSuWPNEBTBL2R2L9Z_zEXM8u7AgvmRuZqi70SMx8usGyEWWTtO5ZLED9ryH11w-u68HoI2rvJclcaPes3k3bp3HHQtk04MU5JN_A2rIXhEsZW9J5VU3hL4ME8U2AWOzLT0hD6uBxTfjYUs-LyG-kN6VIS82RdjOdMc7r4w1j6mv8dqHa1XsBiIhvbFmMZriikmqM0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=H1dvdKMhyz9SZvP5gTqZEzHSqvtVCTJ-6wRnCYEbPHeu2jdw4XlGHl-YO5OUHjrAUCKHTzJtwHLBamHsth9S_G3NRY8ItjHtcmFF91W91gzWPemrjaToPnhMK2JkvP2chEo7NlTnuWXNGhOeDAaiR7vt-e8BGhcwlCQnIa-e2jQlB4QxYxajSeyjG7GRgf9lCMCxKrzb4x5Rbi_xyTwuKYaLbW_5-ghTjMze90XTlzuLbrztjIWzvaZGJClP6LYZe97bblK8HlvJC8hxHycdAb5mOjpqZVIc1PmltBl4VfqrrUrbBzpd65l9V40ob4kOE4vvgXaJV9f2iTThfR02Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=H1dvdKMhyz9SZvP5gTqZEzHSqvtVCTJ-6wRnCYEbPHeu2jdw4XlGHl-YO5OUHjrAUCKHTzJtwHLBamHsth9S_G3NRY8ItjHtcmFF91W91gzWPemrjaToPnhMK2JkvP2chEo7NlTnuWXNGhOeDAaiR7vt-e8BGhcwlCQnIa-e2jQlB4QxYxajSeyjG7GRgf9lCMCxKrzb4x5Rbi_xyTwuKYaLbW_5-ghTjMze90XTlzuLbrztjIWzvaZGJClP6LYZe97bblK8HlvJC8hxHycdAb5mOjpqZVIc1PmltBl4VfqrrUrbBzpd65l9V40ob4kOE4vvgXaJV9f2iTThfR02Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLSkpJJTNPvFisdqwVrBKrmDekE8WqjWQY2vmcF-tZw6eBwEPoMBcxSdzC2xYXRmyEoGR7aLywZf0vbCBSEtWPwENvx2-fnKl_rfM7Xa_kh5zutB1wdHQOG2pxcNyJ0jcL-XLAx3xJP-Qq-AdosxAOmQW5bgU9Fib2UB2ncUYN9rBzdsjV8XeSAoSXGIief0KbnsqmNmS4ZZ9G61580Yw_wu1iLstij9UljhcDDYd4KjCRXscDE8jfTbyiOXM_HKg0jZS5tIdor7axO6HD_BpWJWK2_fGhSmUEyH_8IfAZvUFjP9-nQBszZClFQ28gBt16xoOvZ3T_Gs-ndV7Ktqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5Hrna141aglEeSzw17ClK24EctLAdHMBxd3-ZbmLHjky86_LpBA70gd2jkaJJndHXTXM0wePjn1YwghoZPvW7wcD0l07dvmVuWEoxhy64EJ-DLicHookhMQjgUj5J39gm5OGd9v03OzZpbZejgWrp1eHyMba-_j2LpDfzKKGiUwpyaD5V6you5D-Qc2PPSokUQYQ0C3K_h7ZS3-ZuBntTgsxcP5V0bcclsyCriL4hRFukNW4axSzPKO-W7lozJ-xGicjcxSxEpU3qJC3D2okmet-xM2gmrUEua3IYxSf79r7YlrqlavpmG9HZ5W18K1Fr_E9KXVO7AyAt321PcYrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cHfL3k-gCNaas-HQwxXGx_MZpUPsCiNhBpNwGr-xSc9CWUgCWUqvX9BinkJp5YiKum-mOPD89XXLZ2G3QQ-KsWcgyG7JYC4GO8jhGo9NVaxdrVx8o_hSGrVeE5fiGqGFBkfDiuMhBvWOngHhffZQsydVCh0ZUrDcNBqU404LSMSDq4TB7iqmXRPNdoXP1-T4ROnSvhfYfZllja5vMMtjT5rfMZHi1TWl25zE2wX_KIImcNGyDcau5tdJIrW4-7KhTe6I4R7Wy06eFrHuxBDdT3ite4Y3hQwdFhL6cPUClpQG2nEToYs4m8WyQSDAeXZR2Yt9ysA2-qK3LpREdd-9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cHfL3k-gCNaas-HQwxXGx_MZpUPsCiNhBpNwGr-xSc9CWUgCWUqvX9BinkJp5YiKum-mOPD89XXLZ2G3QQ-KsWcgyG7JYC4GO8jhGo9NVaxdrVx8o_hSGrVeE5fiGqGFBkfDiuMhBvWOngHhffZQsydVCh0ZUrDcNBqU404LSMSDq4TB7iqmXRPNdoXP1-T4ROnSvhfYfZllja5vMMtjT5rfMZHi1TWl25zE2wX_KIImcNGyDcau5tdJIrW4-7KhTe6I4R7Wy06eFrHuxBDdT3ite4Y3hQwdFhL6cPUClpQG2nEToYs4m8WyQSDAeXZR2Yt9ysA2-qK3LpREdd-9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzaTijLZU9u7mlXned5QK3t2-sdtIpw1ByB-_loPbbSouVoWrVzHZEj5a1h3qtTx37mWnxxgl4SjbPgB4v8rY_LXctmzwK21y37MDoVZeuuA82eaFOQkXOHCLSxCCsr9_TmyS4kutdy8QcMfrldKHR1W2-nfjn9KZlU2p4em6S6M4gyEL7eLS9Tt5OORIIncQEwsreXvtgx1frZ0jIbcL_SGC9j2az-zpuIob3f7Kw93ynyHrnhEO1j3aZfriRxPWA1G4lQ0IQXAz1AV_tTu0dmzMCLM4hPSLNuiVHy8eHlIppfXeel6sYFR28YwNElpBYQTgQfcvubb4JpKo-rGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saxmNWCqiQ0OjvOrpAHvYsTik7ocvO--yX7iEA9irgrJ8szen6pOecUk1njq7YboykJMzmLha-wwXStPQuJAA3YYxWJ_I21TcKW9E5P62_BrY0BrkAFDZU_ZBhV9mJFHWKez4sF5JrUr_BEoQ6hBYkbHI-cOjZFVmZO3At8kHkQq9cdIEs1U06OKXnhqcPJ0Y90k_U4CeowU2tiAnE3QeFJHdS5t9rvcKMTwc9B-k3c_PUwgUBuV1autFtEdhiIqYgCbkAHL4BwSi-VptnCtNGV7GXGEcfu2KFV2cCeSf3RhUqtJdyphrxNaXrYfnVhWWD2NGfdY09RAFzKjxDHyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLBWQiQlUXlDikSfPNVWQVHKMXf5JI-Q6H9o1rZLIb5ErktI4RJROp669sATTC7mKG1g6E52lCw2oc0rjRFnYK6UE2WzUYTpSYiFmkFvaHv_wcPPMxjCdU40Yc5xvuTqel8n3bD0vXHLEI6_GrfeB9ffD2Ec0yJ50voTE1How5Oubok474cY7KDfRz4Y1cfzxJn_AKaF40VQ5wBr4PQ2jzTaLLVYmG3OoMR_CMx_ofaT_nj6mHX-vcYNRfk_Q74Q0amfpKbsRmYXbF0e1ny_69Qw-Zxsi8r4JruBamaXV4OS9o9JGcwRseuDxrJPxwYfggQY7mjmeoBf4qxO-EauZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=B_0Yvzeb6UdyWthacmJZtdLNvHAWKmQjrh1w5WwLXkpqXispTiCtgvka_CtShGZnzmdmuy0z0YFBgkoNpcb3bnOG3w_LPYM_WjXBF7cILim9akg8EuuXYi_bCWn49A4WOzT3t4kTS_gV6X0y_2jFuM7epYomgixkZ69md6qcpXnqzF71kzN_DYLaUeTbaz0-WBRTWCRFT5iSNRs6aE37c6VzkpRji5GxJUBjx87wMbIdh72Az3S8GNgyQ5HOFVRpEtt-kYyGQWgC6AqTi5tK-SoNPgx1teUt1e_DfciVlhcUYelJUHWwueO7OrSHFNKh3Nja8AsR8hq1RmQFilE6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=B_0Yvzeb6UdyWthacmJZtdLNvHAWKmQjrh1w5WwLXkpqXispTiCtgvka_CtShGZnzmdmuy0z0YFBgkoNpcb3bnOG3w_LPYM_WjXBF7cILim9akg8EuuXYi_bCWn49A4WOzT3t4kTS_gV6X0y_2jFuM7epYomgixkZ69md6qcpXnqzF71kzN_DYLaUeTbaz0-WBRTWCRFT5iSNRs6aE37c6VzkpRji5GxJUBjx87wMbIdh72Az3S8GNgyQ5HOFVRpEtt-kYyGQWgC6AqTi5tK-SoNPgx1teUt1e_DfciVlhcUYelJUHWwueO7OrSHFNKh3Nja8AsR8hq1RmQFilE6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=qsToXLfGJnWjb9ZHBDnAeMLYAnFewwfnScC0AoOcCzMh91qTSwLnpJahJrsTxIZ-JI1rrYFY5VB5vQovfEUhru93BssF9Yx2JbUwzZiYQRV7pwbsWaNDF5TL_xp5aGjNs1cU-bDebWofbrEOLBAjR50QQ0aGhiEolk_-1cMzxpJnAiFgyUgFEZRSSqrFNw5tKs33pgT6QZ2041vDx7O2CtX3FPP8gOQsm-y4L3-QxqWs6oqccM18EOq-EMihddBwjtekqSr9m3nPHjRuik6kYiEfCvV-p_r3kB9q9IXvzFNUypVUEjlJVPU-lpxR9u9s4SKGfKnpOVR58RakSY2nJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=qsToXLfGJnWjb9ZHBDnAeMLYAnFewwfnScC0AoOcCzMh91qTSwLnpJahJrsTxIZ-JI1rrYFY5VB5vQovfEUhru93BssF9Yx2JbUwzZiYQRV7pwbsWaNDF5TL_xp5aGjNs1cU-bDebWofbrEOLBAjR50QQ0aGhiEolk_-1cMzxpJnAiFgyUgFEZRSSqrFNw5tKs33pgT6QZ2041vDx7O2CtX3FPP8gOQsm-y4L3-QxqWs6oqccM18EOq-EMihddBwjtekqSr9m3nPHjRuik6kYiEfCvV-p_r3kB9q9IXvzFNUypVUEjlJVPU-lpxR9u9s4SKGfKnpOVR58RakSY2nJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=KvG8v13TXMwf2OJI9yvd6OL7qE9m8i8WdOzhtNBtAJay1QmMp13kpDnFsHULJjeDbmujeocVKc_C8Yi_uFfruon3_r6VvoFSMeC_DEcItqUl4l5vR4his-tWXdy7J5IdkMaA81ormqg4d4i24NeXm_o1Ruf3Nc1k7ecVMQbQZRR9rST0MuSixjCqvZj21rs3fq8XQkrvLkw1GcDVsCd4j8jtDUqjx3OPN49BRWXoj8MyoxKL_sIAyWVMbElZ4VrcMfvQ7mEmsoSHrTxZfkhL7eau_x38XOdjq9BjdS20LRhAAdJcy70zVY3ot8XMWFLP-OuRiFTo8h33gWvUH32SjQczmjDUOhRLf4HqS5S7pr17z5VmmnnRdtTUhT1u__onmOULtlPLcbmUQdrticKsd9Q7MFQ1T7evIPVbte92qtWcljjzQNQOHkLs3zD8BlFfeUNhID_wB9as25VwohKC1VGxpnavgHcwRcPqbL_XE9Bd6h6x0Jbwfu1gmCxCOZX_kjANrplejCV9CzbBepMXSLQIH44jm5rcjsaH8zQnDbA575b58Khikw2lYo_TD4E1spvEArzyEYQ3jaoT6zinyaBwl3sm9Yb7g8BS1OY_FP4NytRHWO3EZhHDeVPBtt4PN3qBdyXlN0VpPYUFlrJ-c45jB2GIwOmIkRh8u9orRW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=KvG8v13TXMwf2OJI9yvd6OL7qE9m8i8WdOzhtNBtAJay1QmMp13kpDnFsHULJjeDbmujeocVKc_C8Yi_uFfruon3_r6VvoFSMeC_DEcItqUl4l5vR4his-tWXdy7J5IdkMaA81ormqg4d4i24NeXm_o1Ruf3Nc1k7ecVMQbQZRR9rST0MuSixjCqvZj21rs3fq8XQkrvLkw1GcDVsCd4j8jtDUqjx3OPN49BRWXoj8MyoxKL_sIAyWVMbElZ4VrcMfvQ7mEmsoSHrTxZfkhL7eau_x38XOdjq9BjdS20LRhAAdJcy70zVY3ot8XMWFLP-OuRiFTo8h33gWvUH32SjQczmjDUOhRLf4HqS5S7pr17z5VmmnnRdtTUhT1u__onmOULtlPLcbmUQdrticKsd9Q7MFQ1T7evIPVbte92qtWcljjzQNQOHkLs3zD8BlFfeUNhID_wB9as25VwohKC1VGxpnavgHcwRcPqbL_XE9Bd6h6x0Jbwfu1gmCxCOZX_kjANrplejCV9CzbBepMXSLQIH44jm5rcjsaH8zQnDbA575b58Khikw2lYo_TD4E1spvEArzyEYQ3jaoT6zinyaBwl3sm9Yb7g8BS1OY_FP4NytRHWO3EZhHDeVPBtt4PN3qBdyXlN0VpPYUFlrJ-c45jB2GIwOmIkRh8u9orRW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=VWQ7HwaGfUPd5_O4JwVc0bY4AH6TCQlwBT_dKboXSHnMKlXF2E3Wpm1FNCNGDcy5hU4ELWHtsclqVfBOR2VtGLM-EvjyEDbO9tJ1Ao4gjXs3Kq-Bnid4yoGiVfQ7_7USVnqn1NewDnFU9WrplHNqFWUKjorhV8xyPFWIHPPG7SH7N9lBWqK1zruS7cr5VCIVLWf26MiSkWZ9VtwuF0m3fFbdUYO3ITXN_L3vcClqA0PEh1i_qLMUZXsWrz8pPzC8_gD6R8sD-hVG2H2gjaUCrb805xJE8vTM9g1wq5Z8ycKlDoL-gHOGXw-G9OcEiV8dFN6cw3QZE8HnomQGGYwxnK4v9OlqpNHDFPUxP4Loe43FJASsIGlKsaOAAWnmyAT8PNHRxAcGntgGgRUfVkBC69DOKPsXBKbd8dBjjFFdWVUhSzJ2_rgf4ic-hn4RqFfkB3dWr8eE6vQxo5NEma9V2RR7oHTvc58p4TxePbkbTtas6VOPU6BRLlSX2_0KkqM55r4s_d0xZH3RMM12NM9aCOpyV2jMqgdHPoH_vC3hh3c2tXFrLs9CaWrYqhs_S6nlPiza98DgtkAJLTC_OqCfXBj4Se8PXtNewtoEhX5szqOaDl81bB6xZO5ABUxX1VqKVJ7iieoCkZvT9q3uqorNGu-P0C5nPazyAlfF_N5g2yE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=VWQ7HwaGfUPd5_O4JwVc0bY4AH6TCQlwBT_dKboXSHnMKlXF2E3Wpm1FNCNGDcy5hU4ELWHtsclqVfBOR2VtGLM-EvjyEDbO9tJ1Ao4gjXs3Kq-Bnid4yoGiVfQ7_7USVnqn1NewDnFU9WrplHNqFWUKjorhV8xyPFWIHPPG7SH7N9lBWqK1zruS7cr5VCIVLWf26MiSkWZ9VtwuF0m3fFbdUYO3ITXN_L3vcClqA0PEh1i_qLMUZXsWrz8pPzC8_gD6R8sD-hVG2H2gjaUCrb805xJE8vTM9g1wq5Z8ycKlDoL-gHOGXw-G9OcEiV8dFN6cw3QZE8HnomQGGYwxnK4v9OlqpNHDFPUxP4Loe43FJASsIGlKsaOAAWnmyAT8PNHRxAcGntgGgRUfVkBC69DOKPsXBKbd8dBjjFFdWVUhSzJ2_rgf4ic-hn4RqFfkB3dWr8eE6vQxo5NEma9V2RR7oHTvc58p4TxePbkbTtas6VOPU6BRLlSX2_0KkqM55r4s_d0xZH3RMM12NM9aCOpyV2jMqgdHPoH_vC3hh3c2tXFrLs9CaWrYqhs_S6nlPiza98DgtkAJLTC_OqCfXBj4Se8PXtNewtoEhX5szqOaDl81bB6xZO5ABUxX1VqKVJ7iieoCkZvT9q3uqorNGu-P0C5nPazyAlfF_N5g2yE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=fgfspMXyP3_s-Lbp8RKWO5scHAnDUltrL7BY1ZMWsEQfKfrVG5VcnHmSEGdlfnYnGBhB-B5W7scBGc5G2ol0JDPpqdMdBDZt5GZ0ti50fW8RP8by0oJFIDnzgqm_hQ4TA5r0F4C4qmxCzk3SJhe8MIX7fh4u017qxPRNPSZ_giEH99y70npTs0MGm2yIfszmNbl78xf4XSfQro8yP2QtMIFmTTPpdBbVPM4ZkbL55iztVtzterLNCjr2D_-GPNLvxb4TXHzckkGrQ38uPeQczqGT_b9kbyVhtkwfRJQvR1zF2V6h9v38UppF7BO-SrMJmDomwfY4N4JdILHNNiFblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=fgfspMXyP3_s-Lbp8RKWO5scHAnDUltrL7BY1ZMWsEQfKfrVG5VcnHmSEGdlfnYnGBhB-B5W7scBGc5G2ol0JDPpqdMdBDZt5GZ0ti50fW8RP8by0oJFIDnzgqm_hQ4TA5r0F4C4qmxCzk3SJhe8MIX7fh4u017qxPRNPSZ_giEH99y70npTs0MGm2yIfszmNbl78xf4XSfQro8yP2QtMIFmTTPpdBbVPM4ZkbL55iztVtzterLNCjr2D_-GPNLvxb4TXHzckkGrQ38uPeQczqGT_b9kbyVhtkwfRJQvR1zF2V6h9v38UppF7BO-SrMJmDomwfY4N4JdILHNNiFblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgjDQTVvRghkwuZFe6j1c8u9b8foVBIjpgVIJ1dUQw8JvJrV8Vvcr2SzDAdCQU66AsF2W9qf7ED6aaXxjNrAIcrlI2lEIO1VUoWKZ1kI3oYnHMxWIiu7HDg97ECdusSiqJIwjMa7klqLJ4RKi0vmHrjJqDNqASoBTDIdfmlh4vNkbJcLfNu59FihtO-PCSl2Tk48UDVfvUnMdiqGzbz0PtnodTO0t4pMYBeainGdnMw_KU5h6Jh1t5O26RsRbf_FhFWe3Q1ItBHU0qZYsifxdhC0c9DqRYdYD5BMPhWzBitDSNQ_0FyCPYxfRXXlFYUdoJztVvkGPnoH1moBR8yiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RkNTwTzoX6DIMVPI7ROjNjExe2rYhF1E-3yEoV08vjk2BXERPtDiHdX_cmrq14fYJBLgp7xPxlbSnLvMdgFPtbGlwcRqoiUWLRdv4GGIqPkJb4k4pleRddhwwRz_yqIDHgJGxcucCKk0nVD28pm1L0Hw363hrEhCxoL1lA9id5L2EkDm5dce2ToK-mJd8bcmSp6wUxqn-JNW6xT1VOMp2o2o2SH1-UGFuO2U589uopv-V8b1w72oMDpx4DtYdZkquiRYqYuuv9nbjlhgQUMNbWOJ6YJ4CYcrW7vqbEiS8sazcBisq2Q-DgkOQQG0WBgQmIlp_GmSXm0hxyFPRijPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=RkNTwTzoX6DIMVPI7ROjNjExe2rYhF1E-3yEoV08vjk2BXERPtDiHdX_cmrq14fYJBLgp7xPxlbSnLvMdgFPtbGlwcRqoiUWLRdv4GGIqPkJb4k4pleRddhwwRz_yqIDHgJGxcucCKk0nVD28pm1L0Hw363hrEhCxoL1lA9id5L2EkDm5dce2ToK-mJd8bcmSp6wUxqn-JNW6xT1VOMp2o2o2SH1-UGFuO2U589uopv-V8b1w72oMDpx4DtYdZkquiRYqYuuv9nbjlhgQUMNbWOJ6YJ4CYcrW7vqbEiS8sazcBisq2Q-DgkOQQG0WBgQmIlp_GmSXm0hxyFPRijPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=CkwwTUqKlfclbbXSTSlkhQr-gECF3GA_ViA-ZhlcnBslJFQySyzXK-saJESFOYvPH-zz5H2mK46tR6Pd2fcnB4DZqO6XG91Cv9qhYsHtbFW061NJ6ka9KRpfcTAE8rMKq_xhT6l-_rnTTQD7erzolSV71YiyKF7wzAGMZznKcvDNB6nm40ximSN_c3j29TGEPOxGsEIA1p6wLpeMbAM7hb5tJqL5ML1OZc4PnGUfWzjFq-lGwSYajtNhbUZX0Zp1fEJ7pQMgXNrFYNYy0r9_jhz76KZ3IBM4ZC10HKiLRvsmZFLf23ZsOS6ociD8dwOEUtZs00HoW7W_nJ56I4rgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=CkwwTUqKlfclbbXSTSlkhQr-gECF3GA_ViA-ZhlcnBslJFQySyzXK-saJESFOYvPH-zz5H2mK46tR6Pd2fcnB4DZqO6XG91Cv9qhYsHtbFW061NJ6ka9KRpfcTAE8rMKq_xhT6l-_rnTTQD7erzolSV71YiyKF7wzAGMZznKcvDNB6nm40ximSN_c3j29TGEPOxGsEIA1p6wLpeMbAM7hb5tJqL5ML1OZc4PnGUfWzjFq-lGwSYajtNhbUZX0Zp1fEJ7pQMgXNrFYNYy0r9_jhz76KZ3IBM4ZC10HKiLRvsmZFLf23ZsOS6ociD8dwOEUtZs00HoW7W_nJ56I4rgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzhw6iG4zilumiKbMPTgp8pHAx5Rf1kZJNrS8Jtroek02QmLWRT58YYwVa5_EzrFN_pQP4aivr9fksTxtGYmubLeD-9mSZF3Vw1izT0tWjczRlxx2ALSnUvS2Zmyd64HPwOFB-at5mFGqcYNEWmn5WExOhuqAdzA3VIDBla4We9etjsP65-zGg5HfcXpP5_5U9N2do0a3UXTvUQVAYpCFuktduma5o6WWRQBNVChwdwUf1KIsLWa6aes_V2_MQ9hC1Mxkxyjr0mLb2N7ITnF6Gukkjrjc0fcrULvGYPufNmeu-9Nhpt6DpojHDN8duXNBwE7BK6SPiyHZ36BN7vFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZMDPFR2e-kpub_Ks2k5DQ9CEkX87SL-icRfz__52LkEqJOT6KEu1Z9LzZ85Y8o_c1XTC8vzOn2kVf0uCa4IGI-PtJDzdUojPvTTyTOIDJl4e7HyI0xRX9uTjB16yupQ-vb2jss9T8EJ-EGC5PosQ33uJNUDqiPiDA297mFxAHPJ1LDdNsseIBK1u8efkZfSyvOoBuO00vIgu0s7BYJFy77W1TRN23NR6oV2kBl3de47aLXS4drEpOIeadBJdwl5FaZrC-3IMcEHIj8gJMKTbi8A_8jPjMR_BpDuoLufsrE3Ag6AVcaRBkYBuQGr0wV62dlLSdOf-9OoeAu_C4RVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyBENZsZRntedRhGcuMF2JEDUyKHxHCBO6_LRtHNeKAuooyRoBRfsXxNMOjZqACDjdHqpwiCERxLDNxVx9Lg5hxzoSDHz0I1WWjf6q4t1qXlAoLFNR4gH6XVthiaismuJM32TSMctzLcdLx4kJrtIgRlTM_85q33jOyiZ4jnhUciNDyMV0ez_kJf4fa2LewEDTGxwyuipBnHPyNq-ehZJhaffJapp2XCDr-68ktRwSr9VChSiKMXj9vKuKpuLK8ZCrTRnn1frlN28X2B0CGBietUWzq0R3i7e1-jj4DlZkY1nM1LyZ1V7dQB7s-SEmVoVOdEH59ZZ5Bj0uP_1fCwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsoZG2iO_kbAH8Ywze4c5fqWLM1av9VG_szFjSd5qQ9tnz72FOzxlKeXFR_1rTms6PQCKYsdoyIZUxf3mwRuD9VDrW_9KT0nrEzaNhT-95WcBrvmCmYBeu_UPkfEbibSDQfEigoCzp7XJdVyV0yfm4EQHVBQe_IzU1N7q0bMyuzPPpIqvsgNWbqkzRgopea63D612QGfmt9y9bDdqs-ZJMtuxCi5cYvmzaMO75K5UZdlr2j1ePs_q4aC95fI3JXlREcfektUNV9V6-xlV_MwzqXknua6wOq7KA2pbdjnpvAosgWeYmuwyXMEiUJgQ7BacyTsVXC2IWHmbA88W0VLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njye192KW3VuwWOLKnr6PLIrzDP3P6uPICSQJ5FFeFGiOMkVXyPa9zp0XX_NtsPKH5MreP--zttF1iMXlC-t5sPx207Gjxr6RV0_igaHZqY9e7NhjNNwHjoj4MZTwrkoaUPPYUziJBKOAkhpahtzKkw_8let_XspSY7MHmKjSAmo9nDCOMqVv_pectPK9o0R1WQu8BPpqJ3ydI3XpPfruVA6eMwesX9YZKWt9slacLmbfIJ6qj1J_oNlm-0u8rqohme-HxtDUP2sqfXJxlyrrETMkRmPNpBblTUEAZ9_ZZ-76Y6RfbzEwN6FK5-Og2IFPKX5yUqhzUhRRP00Z27jzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQxWCXSALidbVcEW8eucQeVfucYCbA11g1gni-xJv_NWKHO4qVNZPyRA4zfzhOr3hgOeZK0p-0EEu0hukW_6VsdAKPIxU8JOJQBRM0DO63Rxfdqp1xXSWmsPOyPuU8gfAlMoJClWA59GRrUBd28FcNpLh8gBVw1v_VOUTSEbFEE6QtOCXSAd7YBsbXOpp0aePKm2mnxKOB9XRWaw0qUVkFI-E1EBHD1jxGSlEUEo0jJms5hXnmbI88Oe_5iQFGTpLyxzTCzagcOp4pZivBSPS_Mtag8rRnYdOOimXe_NrngO1LNkEQ2gQ3u9GDCM1tI6tadzA9LqgNL9jBY_fVViKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je6YWdD0EOJllRbelqY4uwo0TVx4h3qCdA1sl3KQpN7IP1NNZzTCqV9m0qlUsc_0Ja8Bmev951nmZUP4bSY5SQYObONQeEOWrqrDfYCwy5Lka3IeagIai-5LP7WhZCQzSez3FFrotEd2vfF92wZ6yabgVZUdMjAdbORy9Az1ITqTP2PgkplgoOMXS-ns5BxpqYLhWi6FA-4D3i77U9f6uj4EEo1J73CWMGwNa1RNaAoVW16dCHcHWra6pw8DnSpFVhThBkDcPUda-LXqMjkWFNZz-Jk0xjkxhfg7uVYsfM67gJhykcYKlc4Wbv-N-mHzQA5BpWGCpJOGbZiikl_8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D40a0T7vl0v4oGQnATlNOgF83PvErNzhlWEIrAHdP-fyUgvFjjJhjJHm0-k0KrwQfOESYEXMayA2zXkQs0QRcawFXRn6-EiZVJLksjQzOgLxYIL8Y2NUMZ7p1HfBq1EuXVEUyHR7E_EYzttZ1Iz74mgkg4ZcTdcqRjnR5NXoiQ6aRZcvBiNiWcV7Bin1JtHvQ11omGa6f5cpBkrEJtXGe4B-1Iwp7PxSLsDJC2I3CsbbOBWhQCUPC_Dushjj_Ey0xaURJWivWz5k0ObAsf5qMfUbNZ82_BVT-Cf9FHBND7cZoZLyilUKvDUJSZKDko5ZG07PX_qND1n_Wb7yI9kGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nX1HYXO-MZmXgWkOA7Sj1dWYxfbZKQNDTmXCC0OX6jNr5gn8iJiY8Ol9q1ldt38e5IQrPkpaCoCwvTPw0iqnWYTk87anoM3PM4gUHYwElHilg2frmdG-IF5_eooXZgdu690WxDwzMSWThRqN0ZFmcQzNv2l-0potuQ-RFXeqKwrZWqLl60W7fIJwro9K0ngts5Xy9ra9TeLYRtf9nsUVErOpP5hZZlU5vRI1yC6kBCmi9PAEiTHbM2swbS9vjsCBssn1tpvtYkTUPBgZbWjErCbPjrZtqZOaOoKMRseWDQNYXYpuBJ_yPzTA93Tp2y-BlcGiDD3kIGpfJukp33oF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8qKL_Omw8idj7cyT1HHyyjnGhRriD9OE9amLMVUKhWRsxz_zqP2QHbnJpH6Jhtw06QCR684ukRyDpPt37KxwpOIzjI2nMDcEvo6AQwYV4z-xTMkbkvOr6qqXCM9rTNJ88hv9dgIU1y1CRGc5gLj0uDoQxGw_Y_e7O1ddS07EMWlGehsMXHF86NeC4H6p5H0Rlk-3rUFnf5L5BGlZNG9Pc7YF41t8o6_AQaWmxIXjaYrJGuO0P_f6HuV-JYsIwe4J9GYsJvlpsyNVeL3UdceaLpTIvRUswBF2g1yvKVvgYr1HsvVuafHaITwSZcTOXmTYj_furLXjMzXvi1ujiQp1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=v8fP3TuhCXuvNoVoInlbsYlJpzcTOmiqyor4PvsFUs4piL_YMUTzvptjD-YTdkzxXWpz4AmD3Vnte9chnDbRV6sQV1Goheb2dx1xEfjAyLpBdOz8CSdy4kDEjeZtxuwLcHZFug6b_dg9Oonspa8yqJNNGbyzD-ETtuLF7OX5dpvIxKBq8Nk9V0m-rRjKR6PhOorRUfN86zf5Fg5Bad9jjYal40o-INCGp6hoDneB4e63J6AxVMudyBNE8vEoUjqkAERhhRjIguL4OPqy_z-sR902FpgXjkbpeU82EXP4Q5dcBQke1N1tuw_Yur1wQR1QHwzk-H81IE1Zhlrg-Dn4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=v8fP3TuhCXuvNoVoInlbsYlJpzcTOmiqyor4PvsFUs4piL_YMUTzvptjD-YTdkzxXWpz4AmD3Vnte9chnDbRV6sQV1Goheb2dx1xEfjAyLpBdOz8CSdy4kDEjeZtxuwLcHZFug6b_dg9Oonspa8yqJNNGbyzD-ETtuLF7OX5dpvIxKBq8Nk9V0m-rRjKR6PhOorRUfN86zf5Fg5Bad9jjYal40o-INCGp6hoDneB4e63J6AxVMudyBNE8vEoUjqkAERhhRjIguL4OPqy_z-sR902FpgXjkbpeU82EXP4Q5dcBQke1N1tuw_Yur1wQR1QHwzk-H81IE1Zhlrg-Dn4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nofg1TfLkjqNQXzrcUY1PUPZtqND9FFEB16K65SQbdatGA_hGwP4gOl38MBspGaWFqnRD6MHKVI6oItaqB8iJsGoFyXLUWIV7o9uGUbjq9CQl674FAA6XC_2Kz7PAMvEswmumQJNp0CHosAnSzfFVry_CL881d2i7DL4sxSgyMkoRSzO06pxAFJ6xpLlxxVGmwsFeBv2p3nXxdFbFahd0U_kIjEXp6vwZc_iWdpdgMmdWt8NYJ8KFkiAY80y9BuGad5njD4UlP0M6Fx20NqFFjzTwUbUhVi4BtSuqMoPh8tMyD7oCYO0FAH5CZx01PWAsqHjuFKeQxjOmjRZcpPeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAzkkh4TuBerjh96GKJlhAGZiFwc3UZnTjLRayg4XEgUhzc4Z9tKaFTtdvwyLbZM5hjmKr5u19Hl-pTe4QcPJAoBJRSBC-dAcIUKqBv_YjHctsg1KB4WC20Ydmo3ttXms2PznlbX7kJEL2YiH1151W4yOWIIu5oxe261y9MyDu_DuYYJqxsgyqezU6aKy19EB8PY-rl6xQoV0Ab4nf5kFXcJePUvXgPiVHf5Vc7WX90vXqUI6qUkIN73ERqIKYZ11M4rYENXBzu5gJLK-O1Shsp_kfU7otBfTvHywqCjLer7XFLzEdUJQAgIyImFsy8ZU6mMff3G9nCnsYQ4QphbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=NgOOYWu5bxW5Jvyeu-cGX0lDAjysvtAP1dteElSDTheOhhB6fiSmmtjBtmW1ERHF1rmnlNV211dzCIyXZJiravYEvb3z2HDCDDOAt3YkFi5tQfP9uhPCeVxlox46BRmXVgWi0puLUWg0SMMOvMUyn8SCQ9pQR9JoukUMFWJ7dDXDMabrXQnZ_VK4iY-ce8sLsCv-jF_y8_w7Re3ODDCg6QltcIUn6iqthfIUu8FcUknD0gazDbe6B4jIPGeo962-WB6w0BzAlwb7Dg7e9d98o8vJSCOcxMU-h0eC0_Vs5q9ZJO0SWyR1ni26FTX9RCC3dgxTv6Sdx_bo7AEFnRLNFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=NgOOYWu5bxW5Jvyeu-cGX0lDAjysvtAP1dteElSDTheOhhB6fiSmmtjBtmW1ERHF1rmnlNV211dzCIyXZJiravYEvb3z2HDCDDOAt3YkFi5tQfP9uhPCeVxlox46BRmXVgWi0puLUWg0SMMOvMUyn8SCQ9pQR9JoukUMFWJ7dDXDMabrXQnZ_VK4iY-ce8sLsCv-jF_y8_w7Re3ODDCg6QltcIUn6iqthfIUu8FcUknD0gazDbe6B4jIPGeo962-WB6w0BzAlwb7Dg7e9d98o8vJSCOcxMU-h0eC0_Vs5q9ZJO0SWyR1ni26FTX9RCC3dgxTv6Sdx_bo7AEFnRLNFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YoGu_RMx2sZqPol_iKEbATojLXvehZdYCS8CCeQcExGy_vyTJDI24Bb7BpOfFo2hkyn0J9iyA3WuNWFF3NGjy3A59QvJw_FYxjhDS0jT6PmFApT1irXXD5WXBF30i-AGQ6mPcWt5zgaOSgg_39tabivUiDmxJN4qEB5Z9CcmuhN30m5woBpSrORaIkRiqqg5pTPOG_kCNUQZeVzVjJZsTd76Y719k1__PpaZlMvsXB0U3UUpuvrTx0UhYjF-cWmdhwL-O0AfW4LRZK4HVzM8Pr7NM4LyNJOEv2xpfo8iEg8Pg-n7oi1qnfFI-qcTMHM26-GLVyMyTyPHxFVanbuDcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=YoGu_RMx2sZqPol_iKEbATojLXvehZdYCS8CCeQcExGy_vyTJDI24Bb7BpOfFo2hkyn0J9iyA3WuNWFF3NGjy3A59QvJw_FYxjhDS0jT6PmFApT1irXXD5WXBF30i-AGQ6mPcWt5zgaOSgg_39tabivUiDmxJN4qEB5Z9CcmuhN30m5woBpSrORaIkRiqqg5pTPOG_kCNUQZeVzVjJZsTd76Y719k1__PpaZlMvsXB0U3UUpuvrTx0UhYjF-cWmdhwL-O0AfW4LRZK4HVzM8Pr7NM4LyNJOEv2xpfo8iEg8Pg-n7oi1qnfFI-qcTMHM26-GLVyMyTyPHxFVanbuDcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR2nUiXP0fUcKPGUqGmT6w1v2tQeLduV8w2w2c4KfcaG7QttRNoe0Kvxty9gpHmMCrD27iv2VgPrwTYeizCGDdV9Ce-Jbgd8637WwThVRZcLTkBWbiWmwCsSSrhBSMU1kyXEYGg58jdoju-YfPHgfccZFIjv-1bzUe8hPbBSXIm8ROjbdfXR0cnrfwlF7YNM0jhCCYJa-_2_gMnbrjA-fcJpnt9yyGT7wvZGmAQYSRmzzraU0w6cXLTipqrrS9CeY3w2nutOW8iOoiFogiD0pBA2c5Q4DypFOAekD_8ShFtlgOjH15Mv_bTmYR41i1HhgyWNRIgV5rCC-WEvMWsdNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlNB8fqkQuo5bH56UNEefm8vphygSgRTvsm2UXGhkv8SL8db2LleT0tLxHRJ2epJWUEVmpBtw23vpNJi0EaFgeqd5BcAYxe24Ii3TN740Pryv2xPrxNI9pnA6A3jdXIu9Vji6MF6cR6R5bX8XC3xiclMDItHVCOX-hsGuLIpAB9YytjncoapF1E3e2M0U1ItF7S63AaXvsSncwhjd47_R-s3plUv_SOUyOBcZNmRTU8VSmtxLEI9vqQvShXAEJyjwMhcZonkRJDWeo1ko00sz9uT7w-GPyUbAk1QIM3lM6H3QTOlieDeTq8OIRrDhTsDy-ezo8AwaHKkkJdT9arUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXXuMRGSy2xrf6lM5_N8YqtNtOQDMBRO0mSXeQPPyLAZTdVFzeOzKZCXinep41Hx7JgREi7l-uMuj9PnI-lycuVMxQMv_XOXucX_iGp9sNLXZj19ukXUr_Md1xJg0YMcRLq719NNuAhhwt2xA0qNvAX3fKA4-yOT7HB9TWTZrIt4SBU9ERVKp_PGYZ-6Cin32Tb5MCp-4IAR-SpNp6-nWaMix1uY1nWTIm6Vs4qCMJZ0-OGae4xP1akbGQpEW1dD4ncGp9AxdO5I27-9NKduDa6wkYnn1OeCyPNFlqPtpVvfxSJ3ze-HedQiqcI3WdqkJqmEFvlvndzE5ot5Nq0NUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPhDsNoqdtUShblzCNQO0LRCJGWsTagYwFtspnprl3SvX4dPfElBJK9IozedXvVPzHaXg0gsAbtOYlavmrvLYudK4TVTnIhoqZdZEH_fIeyKEnDyXANzOJ4O7r_pOMkAvXCXNhgD83ALOEURg_atOND74u-B_L9siAG0YdqLTgC7wCKGwYhEmTVcuZOCrrcprZCtJbrLO7ZC0NCF0KwZHKk4LJAUDBiJikyfLDUSpu1CdMK01Lf8LEYH9I7__QzELVwkJ4h_Y61hThyWxK1l9ETsEdZCBr0xUdf5C7Cl8CZOclKUcp5T7VFCnSryYpW4TGEkWDKoXrB409_c5lWPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1QOeogaaYDhhpGW-2rNLLW2z09OBCFzY3E_PjiBZYJ7GkuCo9yMEGme0Zm8RFiPfI3Ud75seS4K_IMQHyq4n-lTk_TdVYlbbPGvo8mfFLGxE_OvYRT6eKs5lZLQ_Xf2xW2wpaCvXFMafuUAXJn93fph9DHg95t7LVCo1NBJyE-5xDdpWaV2EbC8Phvs7HcDvPIlwa7LDOFYSdGTEx1a86_mug9yUyw5t0BhxbZzFvsAhQDfFMTlkr4g2wGCB5EwKgTv3K9ANxJ1nGmtXUVpFvp5sOPcfkHbJJMnt_PEivmEkotMaYN_mspYTRts1u5bqt_0-Y6X3Gl6oDRbVHZEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc0Ib0GU70KtnT7g4lZhV3kOQ8L5lvs0aomzojYDrrtjyp4gBHLgfoMaTCC1bFlK1BZEn-N4XnfOBfg4nCWxUbCEc5HJg1Z7khrbP342fy2-CLWjAz9yC_i8doxkTiPAN4V4QPf1Hmap_ueQBkd5oDa07JjvVtvxVvYahzByZ10SeVk61s_Xlqci5sKmX4eKyA46eJBueLuTcLqPP2jWfKvyRahd1WOU9Sy5twYl6Cduv191FnFVQL0wSmyu_sR9jx2ZjXVpxg-JfumvbN0flfXe6OcWAYACwqNMXWXSlE-5VV9SsNPwDogoQRC6Rv8jUH9f6iBoSIs85vXP94IH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoEAt9_LpF7VnnCVdCSm66Dxfpoy6rWl2b9zdiH5BGAn7xyGkqoYoiA5OPTlEKBltR8iGdEQo6Ogt5Hl1aHIm3Zd98JA-tf39nSQ6rQtTsGbavEQXrKuoT3fkM48073wJIJfZiPm6-LaTYRFC2k8aMImAb41gXbmZFZrgHL1kFaEJ-zXH2cTjIn_lDBNwlGM3wNHmcYZJhspi-8GmPTTkjqcllkOSdZ4CxXelyjt6EJY4R0-mLBcS8kqSSWeCDBVRx8BFcdRjBWdiENwvs4TZuvXJD8EFsw2ZK-ZG30Tpkp2FVp5CZusfdMQ-m5HXe-kLC1gYJrIJMgE4uedPZeoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKEGnKIw_jjhRvp_y_-BtGk0lPT-2-UyVArCTgMXveMkzb5Fit5CbfcJSLwxStfKXPb3DIKk6294HzJzKKdxJypwPmSO0fdM1GCjz56Cf3G29yRYfF2zeqXiTFQdwpTAop4mZFFjOt7hCB7wdo3wK39dFsHvwnRKD35CFDhmFQXuol5h0YsoMAJJjbBN0faKNE5PkVZbRdbDMlfX8ZMB2KKDSUF1GuemZH6S2YEhFrARVXXJugNAUE9upK03JN_3P5OqAKa-gwrMuG5AA98n-BJEpA1_lHZhz5tYrSOxCDq5EkHERAlqEHAND_W3zAYSsB_ikYs6GxnBLqwj9UTN1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=FguOh3XX_bLoL5fjTQDwr-BV05PAKS--EU5Huhtyzepld9hTuge3Oh9r3-gZE4yLDruJY4cvvGvrGYABjRUp5g-7rdpOWhZci9Rcuy5TXfH6OYFVVyf160Dj0tvVTCUauRr3PCzRN1ApAGQZWASAi3NxqFjai-74EKPOHEfxHFjm1P8VsOo5BaEmx5bEJEbBgxZr8maj83Q-wTRedxlnuMzsf4dUiJ0-jzfxEt-KsJY_E6U_7R36-Tw2UoKqfaAlnFB8nz3P6RA9KAIPv7MjPO82KxHxqGDTho-P_6mYVk662msswy67Qup8srynunoiLk4TtjOVxtkll5Rlyqn8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=FguOh3XX_bLoL5fjTQDwr-BV05PAKS--EU5Huhtyzepld9hTuge3Oh9r3-gZE4yLDruJY4cvvGvrGYABjRUp5g-7rdpOWhZci9Rcuy5TXfH6OYFVVyf160Dj0tvVTCUauRr3PCzRN1ApAGQZWASAi3NxqFjai-74EKPOHEfxHFjm1P8VsOo5BaEmx5bEJEbBgxZr8maj83Q-wTRedxlnuMzsf4dUiJ0-jzfxEt-KsJY_E6U_7R36-Tw2UoKqfaAlnFB8nz3P6RA9KAIPv7MjPO82KxHxqGDTho-P_6mYVk662msswy67Qup8srynunoiLk4TtjOVxtkll5Rlyqn8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0DL1Oap3WDFQyT857qw_iL_3QQHPSJDg7wR3gjaHM8cLPkZy3S6p0KAktVbYitMvC_-eqvCk_nxV9rAFrUVALMl_cuoy8wQ5KKAK8SlFn5V0TjUlrcHSmMUIJYn3RtOLAnOAvrrkBt-zF8SooJwm-Ne6i6UYizaQcv4dfJjAeQ1k_3xyJrXrHYmXUH-XIypnVsQ1JLRAH4LOrgFWExzE9lHEy6L_BiVKppnX1hkO4TpNfb1Lqcdv3477_Pu_MGRJmAqdluqcS2tm-Y8q9u6Td5t1ix_pjvZHPghAi013a1E70JTBnd34Aj_MFnf0THZWgO9lzDy9m99TXvzHjf1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DeWTI-BodL0qXi0CorMqOXuCPJmUTFYCuLocmTIT58ncobsDLTTb-QDILjYE5xnLIiS3ZoooCj4yyH6gY10qFUwhSgXGUSJLg1MWW-l5XI7uQo-eh8YSSn7ltXbPILO32Qgw0BUaDLkkmbiKWEhqEf0qFEgB5uM9s5Ya6FjQmGZlvkqtxvhyPd05t60Hy7FN4CvGGshrVvcj0QYKLKIbhk3TNivPpfG43k3VUV-HZK6vy6xRJujtFl7sNzjJMahgFRPxqJsYLCka0Vu8yXNVYX8sZdh_MFnHGmRLxgEdKgmD-AF6rce4jmCOAXv8-tLSub4kKp7zDtRpfeS2XL5GXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=DeWTI-BodL0qXi0CorMqOXuCPJmUTFYCuLocmTIT58ncobsDLTTb-QDILjYE5xnLIiS3ZoooCj4yyH6gY10qFUwhSgXGUSJLg1MWW-l5XI7uQo-eh8YSSn7ltXbPILO32Qgw0BUaDLkkmbiKWEhqEf0qFEgB5uM9s5Ya6FjQmGZlvkqtxvhyPd05t60Hy7FN4CvGGshrVvcj0QYKLKIbhk3TNivPpfG43k3VUV-HZK6vy6xRJujtFl7sNzjJMahgFRPxqJsYLCka0Vu8yXNVYX8sZdh_MFnHGmRLxgEdKgmD-AF6rce4jmCOAXv8-tLSub4kKp7zDtRpfeS2XL5GXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=BZ1k8Tw5sGwM0x7uPYeVHXusrUr3HWlDAmHUPUcWvi9ls6-YqUlZfNGox0EjENOHm2mNrDITPUbHBmN3yvB3StAot64VrzWxnEkDAq5Pcp5U92Q-dR943dDXXDFRVXoNdHwJETvpOAc2EVhb2PBdzqwZbMN5Eg6DUt-7zgxKNUfzOX0T6JVnW2rIl0a7BsZLQoA_K7xSTMEBkytHaCc2wgPVhwJTSdCr_BtlymkCC2msnJvF2Q7rf-3ldxE_xkr4liHNkmozJXbUb8gsuDarKizEJFKAm3L7TLxHiFfA9VoL4v9ytJqyg_SgJJL4pIuViSgRjCsewuWH5OZwLCPgEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=BZ1k8Tw5sGwM0x7uPYeVHXusrUr3HWlDAmHUPUcWvi9ls6-YqUlZfNGox0EjENOHm2mNrDITPUbHBmN3yvB3StAot64VrzWxnEkDAq5Pcp5U92Q-dR943dDXXDFRVXoNdHwJETvpOAc2EVhb2PBdzqwZbMN5Eg6DUt-7zgxKNUfzOX0T6JVnW2rIl0a7BsZLQoA_K7xSTMEBkytHaCc2wgPVhwJTSdCr_BtlymkCC2msnJvF2Q7rf-3ldxE_xkr4liHNkmozJXbUb8gsuDarKizEJFKAm3L7TLxHiFfA9VoL4v9ytJqyg_SgJJL4pIuViSgRjCsewuWH5OZwLCPgEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaS9Kj0vilWJh9AA0xB20HJKnDTkyHKGX9UGHNhTwaJ5L1uAWP9a31jdnTiUqGNfxxWARzDNOrZvvPWJdLWrOX15-b8dw3ShtgkGmxgUSKOGK18nJNV_-uUJdNfN5y5QMCQEoLRu8R-q6K1eayEQxGSK_ZlmZc1_qTHbXSeIMyUEGLPUWZvCm78FMy_35zs9M_wXfrBbHYcbnu3GmxQGZFQ66QgR5968KnLmmBYADfMNtktRo0E4MLsm6J3pgt8-rbGP8Qr-sune6KVllZCTG1Qy9uS1-atx1zWj7RzV0avtIN3DWkqAXpMGcXGMTYkkUO6jQdpTdH69tGV67ZNtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAcjObYj51so9V0NJioHHzB-UDHoHENXG72jMjpzRr0yRAL9gVTBK4gE7jjGtexf5-VeOvXywrhpRQngnFxVuysrREku0As0W5b-vJyArktM3AAwYBT7UM0wK0SWj1rAOwBPxqWYkwaL_Bb2f23RdUD7QjORsSbhgKmJIRR55vUDEou0_DgVv8AJ_rLBD1rUlqUDQUZeEDqxwBgZChJL9aPBGKZyLn08RWZEk1XQo_UtXrhLP6ymifEIBztxr06m8IRPMLD041vcStopz7xGysqS33lJvurZP4xKZOs3jJba5aGU2FNmF76ELySdxVpRQB2Fw2KIqIZ98-h2_wKQGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=BJZyBWfTtYula6DkU8Ro5FSAOcXqBQ7F8w_vQrGKmoWsjEX8TYG439dWj3b3yFaDLAbYu47225Jr7jUf-FLdgROB9f0oX_6y4QmZfh9rkRKNPSvLiEXq2kooc8aGcoNu9yisqRPV6tvAzUioUKKAhuTj4ki_0rwlCLfGQTqwFJAX5xeOAawIZHQ1sOVZfJgwwkd69N5dmKR7imKMv8UWWPwuJK-R0z7C9SCzbiZMxUo6lIbHZnHxdvq2TkEI6ZVmtJnyTrb7R6kU4eHnSdANAjE0t8QooHb5_w2W_-1AHuy8YvrtK0jBMiIkQ6MY4icOQQxt9w9rjNQTAmQq0lllkLSRzCPFZLVBUOKXfzsIt9R7efRZideS5tGmxuvkm8rZqaP9b7fRkqVSh19I8dITehq5RsnIzZzPYO8PGW-VBi1HXwVMPhWbfsZ7Jv6_HkU9MrvxPqNBSOZS_R2Adsd_p0e9mFXr1DUHp1jDADn1HGoxiy4JK4BYL1kPB02r3LySLcyR0gUbTk--1ZQavrzrW5XSEc6TkrArJLoE-ep3X3kAZ5WCONriWXKK1p7sQUAalNRv4zhgowxTtuFtfz8NR8mVPKmuvH_dYwXCkJFpgL3tsL2YehTofqMxEsXdozQ-TJP2jEhHHup6d6eNJcCpYYzO8t7i0sqMw_Iax3qG6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=BJZyBWfTtYula6DkU8Ro5FSAOcXqBQ7F8w_vQrGKmoWsjEX8TYG439dWj3b3yFaDLAbYu47225Jr7jUf-FLdgROB9f0oX_6y4QmZfh9rkRKNPSvLiEXq2kooc8aGcoNu9yisqRPV6tvAzUioUKKAhuTj4ki_0rwlCLfGQTqwFJAX5xeOAawIZHQ1sOVZfJgwwkd69N5dmKR7imKMv8UWWPwuJK-R0z7C9SCzbiZMxUo6lIbHZnHxdvq2TkEI6ZVmtJnyTrb7R6kU4eHnSdANAjE0t8QooHb5_w2W_-1AHuy8YvrtK0jBMiIkQ6MY4icOQQxt9w9rjNQTAmQq0lllkLSRzCPFZLVBUOKXfzsIt9R7efRZideS5tGmxuvkm8rZqaP9b7fRkqVSh19I8dITehq5RsnIzZzPYO8PGW-VBi1HXwVMPhWbfsZ7Jv6_HkU9MrvxPqNBSOZS_R2Adsd_p0e9mFXr1DUHp1jDADn1HGoxiy4JK4BYL1kPB02r3LySLcyR0gUbTk--1ZQavrzrW5XSEc6TkrArJLoE-ep3X3kAZ5WCONriWXKK1p7sQUAalNRv4zhgowxTtuFtfz8NR8mVPKmuvH_dYwXCkJFpgL3tsL2YehTofqMxEsXdozQ-TJP2jEhHHup6d6eNJcCpYYzO8t7i0sqMw_Iax3qG6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGiHQT9lZR-NCk_VKW_W6JReO9Ir6z6c1-uTs2DyN6pP_2V5muePPCdtMmV5poBPxFgMq3S0tBtOu916lLEKl0z67na706ycDeaUdJeqyHLgZcvQoZNSSj_UMKzJma-VFIbADjhR1N2c9KUAl0VSjPvG9VPDMpLEl0m11FGcXckL-RDZUVYfgW6sMekc1mCUZ4bITPK62BQm8mNt97lIIJdeLicBc0mFnxeWJUNYd54Yd6xZ2gfwWEtHSXXJ_JAPGWdy1ySL2LqXiliAZH5mYO9yu5N2RdO68Bd0ghJgZ6vkuwqu5oKPK-pA9Zo9fTLPmQQ3DZjf7QG-IcMqWTLRzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oebEXZ5b0tkDO5IxLvx016FoSlsUSfYAMG6kpwJ2-V-LEOL4I7oCumvLerg6LeMvvHejT0JL8Ng6M2KX9lrHIrOZbWnVyGvyuCIOqSvAl_xEOmi7NUCP_7NY2-TX1kiID2D4ENF61HlohH_o8gquOQlQmsacJ7K6BFWNteP-PkeLvcY209O8ds651cyI3psPH0vFYQeKsXvhMYLu4VlXbzg9_7F0s5bfLezySv0Xeek_JsuCb75UvYIa1SOqciqMo7R_7GOjeOD2tarIbkbyXhwvwD4EE4-QyEmURXY2ljM2kwX9Z9C7LSO8eTx_RUuxFLYR5gxFsR1_TD0wIlTH6bPi1KEdgam4cH13QHbLboXSooV5uBx7opyouL-VzsJKxnK6tJduFs6GAgHsG0d-aDIFanzY2fq6K6b5s6I8_AQs6S9TtFKz1_Jj_F3qKQPuMUB64eJwVtnx7WXuiWJU0cw6L7RMCQdyy8lJy9o4oAVKml19A_0VjFwoJlQq3hGRhHs8bGzaOG1jBgNqXaOfWmyainvoRDJIH8v_yJOMB5gBV0LFI3vot-G3W5PDi9eviqH_Kg_lMQY_67g_b40MkUqMfUhAZMEUPdvQrdpz64QIOUsk5HB4dRZCo6prtqCqGmDFNMW-aZCZ6xDiH0xZXywhbtY6Fnzl654DSZs6Kj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oebEXZ5b0tkDO5IxLvx016FoSlsUSfYAMG6kpwJ2-V-LEOL4I7oCumvLerg6LeMvvHejT0JL8Ng6M2KX9lrHIrOZbWnVyGvyuCIOqSvAl_xEOmi7NUCP_7NY2-TX1kiID2D4ENF61HlohH_o8gquOQlQmsacJ7K6BFWNteP-PkeLvcY209O8ds651cyI3psPH0vFYQeKsXvhMYLu4VlXbzg9_7F0s5bfLezySv0Xeek_JsuCb75UvYIa1SOqciqMo7R_7GOjeOD2tarIbkbyXhwvwD4EE4-QyEmURXY2ljM2kwX9Z9C7LSO8eTx_RUuxFLYR5gxFsR1_TD0wIlTH6bPi1KEdgam4cH13QHbLboXSooV5uBx7opyouL-VzsJKxnK6tJduFs6GAgHsG0d-aDIFanzY2fq6K6b5s6I8_AQs6S9TtFKz1_Jj_F3qKQPuMUB64eJwVtnx7WXuiWJU0cw6L7RMCQdyy8lJy9o4oAVKml19A_0VjFwoJlQq3hGRhHs8bGzaOG1jBgNqXaOfWmyainvoRDJIH8v_yJOMB5gBV0LFI3vot-G3W5PDi9eviqH_Kg_lMQY_67g_b40MkUqMfUhAZMEUPdvQrdpz64QIOUsk5HB4dRZCo6prtqCqGmDFNMW-aZCZ6xDiH0xZXywhbtY6Fnzl654DSZs6Kj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4WfyQAjcH1tCno1nzKI1kRY3xjeqBz8NWB-JP17Yj-O_yDL24eq8IH86PJyziq6yr4soIJW2JbuBIUotHJp80HxMa4cNTiCYuICOv3e3JPLKUB_d2xQVDZPVuU3oFodW_JCXSv2DarC6a-ckAVFVpMdgkSngtDxlDvHoGeqEZZ3TmPDMyIqFgWUY-oWb0pcknx9kK0SYvcUiDfdOwmGZdSYlEAHAfF4v-oDUjz9O0C3vif7lPsma69B75WRAuUzNmbu1thGdYsppZKXfFO9VzwjZ4DywZtEhSE7PUy3Ayvvkrgf-hYc2a8XTeJfiVX3aV7ZGhMznfIJa7gO1xdGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egCKmoDvJOjIWMnn-zzG7hVl8nQ5g8iyShHoXhs8HDnwrfaAig-mQ5d4BjlnNJcVPKCNuI1eiIpFiQjZNzqjnKZm7Iaf_DnUAEyLFpQZuOy4VHxSWNXExW40dTEsj3GpXfuLQZWYh_MaTDWENSDtWWfoP-JbXEuS7h5uEs67LIbC1kSWafMSjWIFI-vhvfm6UAKHHe8DcupRJKaI_SvaA0yQbeVTsxzZ9DhrKGQyXspwYieHcV823cEY15GyQkGBISJZxM1ab3r_E-oXyBNYNggG2CuN9tDN85nQpxcAunxk8vtqNv20kPOR5JyZ8OqCQp5BSyI4jCF6nsqU2KJI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoRkjxPEaP6x0-R3KCRvUyL4M_8bH0S4VRwq_B8GQwk_WjZnZuZK-j51oqEKy4fHvvrd9US0PlQJeqpHtxBN9bXUexsDrAX1u57K9fOTkNAR-Ia6CbWFMcL7OINnK3BHj-d2H5dh7Q0SYxuEUkuQa-iWJSUOAvY65f0LG4LKCI5aB_Go0a6DC9y8OPaB9_Vf8diL_1qDGekxkONKxgZirY72SGJ2UFx0YwK1cWzYigFMJamFWYTVBMMt9HHnueO2B4_deP1kGPyZzuXnUWUeNG5zlJOw6I-O0F-GhKEpg0mjZvUHzpWchjL_YUblxTOc0nKEUCwiJkFkWG16WSldzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
