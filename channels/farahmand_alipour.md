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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=OsAYqjT64qVs5LWLFe8tUwj2SbPsD2FkVbUa_ofD7Paq9mdPXLXY5Bp83U5N87ditCtmTLl3GftQGU46H2pHOq4o6sTiJfqcteBRnhJcMXqGk2ZqHalywvUIPzr7cYNmxfGe4QEdCIhC0HJobONY2Kyrehhq54vXjTtDsc8fJpdf_b66eW61R5-YjRy_hQDLL5gp-E9BO8qcVZeTU8MUJVilw9Jycz9lA0YPio7D-PWdP4Vih1aEok7z-stYNjc4jqWo4X8WJIdAlt_-HNFHWSGDa_M1xn9eSJIpKeZ0zNiItMet6HgOt5GIuEVbKqADGiNtJhR16EGdQwWTKmu8xEnRqNl5Ay9sDBQoU2pnLDiZrIKGukauB9nuNdWu9vBG04LFTc2HZSYVv8bRlsGDYimr7NazGvtrxEPsvTynPId-5s1Z6ym0lHgmWtY4hYcijynPc8d9QbBfzi5xgFtKHSyw6Gm6l9dq0-HXo_ZSHMHMQCfkfgZjqsPSDYXH5ACQjZqHuV6oHrqmxIS09_QWAQCWG_Z5dupQhA1NiKIxBZonQzGZPkZHeVTlm--EtfUVN4hHoBaJ_94ZrfIxuULOTCmdR9YGb759TT-p4conQ4qHPUKOBD_rC3mSpOM0GpA3C69YrVCO7HT8uVQ6bYIoHHM1xSoVcbNG-qpZO8Spacs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TEonFBqqy3-tByebG6qbIjTxMYlu7TCEY_Hfz-xr4Qo_F8K1xR0UIkc0tduMFVU8nQkG0sQ_RnbIsHcKc53wuHDbjKKH_dSxUXDi0MBNMYKcuxDwy-mX1_3UTefDAeVUnxwrazRuPfF0IKMycutkbvUdj01NnuqM-KsEXB5zD2rPuT2RwKdDGKrFYnvVICoehzx-MOVrjLsH_wmhxjetFU3j1lKXS7C3K8VMZZM5XiCVIxxkT2myRw_FYrj70V2jHbJDaekA9tlJ9MTtLTdBtlXaEqqoHna2wpxBgr5uo2-cpus0GhrFJEwEVojJ5SQvLBUkchn5NL3AN9vr7h-AHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=o3mJ9NESfIc4TzoK61A3JI4CW9b0Fq7dkeG5BGWHA8PO7J9XAIkMgVaRXaQW690bOGHbo0p-vGMxQhW6eZ-UWZUt9QOFiPx_dX_tbBZG8h8yJXkhsRV0lW45GRi6UdrRoPs4PnENJKsWrbkp_ZeL4ajam7iCQ9jDOjar72PEtiOw3nLOXRRA38sdIMXizXgCJh12v4L3phRlpA7eqXJ3Gcuf1-8Br3bPbHoVtnxakYC1OnHqdpLAl0cXzjqZQQug8AeC6ZVGfwir6PM8vEh7nfWmjsgkppBsiELpshUVwkSHA1dRnKgx1BDYd0xqHCNBXqQNVfQrdlKUqcUQ9dEdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=o3mJ9NESfIc4TzoK61A3JI4CW9b0Fq7dkeG5BGWHA8PO7J9XAIkMgVaRXaQW690bOGHbo0p-vGMxQhW6eZ-UWZUt9QOFiPx_dX_tbBZG8h8yJXkhsRV0lW45GRi6UdrRoPs4PnENJKsWrbkp_ZeL4ajam7iCQ9jDOjar72PEtiOw3nLOXRRA38sdIMXizXgCJh12v4L3phRlpA7eqXJ3Gcuf1-8Br3bPbHoVtnxakYC1OnHqdpLAl0cXzjqZQQug8AeC6ZVGfwir6PM8vEh7nfWmjsgkppBsiELpshUVwkSHA1dRnKgx1BDYd0xqHCNBXqQNVfQrdlKUqcUQ9dEdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Z7eJ3-OUqx3jU5vEX79hGLwayOEgtaxAZP5LHTrSzqc6F5GLZ2Y82TrJD0ZsQhRiIjknS7Oe1S4EP4nX1oM41KsNjaADrtSFGzZhREMaSMzvxAJ8H7yNq5pudJiP-_B_b2clmcvFvLKIYwi1uG19n_iZwbMeUtMnoVprlvQO-34LSHy3uqITmAMIi5jw7GAqLBoZDzg-T5om9sP6Bqj_p5NHZKZ9ASKO-rkIQXmnWKGPK9yflPTWWNRoa3tjT7B2Abuwd2RDkT7SRScxagt6Pe8AgUMOhKCRlADSHpSGyusQvyMTwPBl4BYyOMZNk6Haek02aqcJOsSJeveLwbWnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Z7eJ3-OUqx3jU5vEX79hGLwayOEgtaxAZP5LHTrSzqc6F5GLZ2Y82TrJD0ZsQhRiIjknS7Oe1S4EP4nX1oM41KsNjaADrtSFGzZhREMaSMzvxAJ8H7yNq5pudJiP-_B_b2clmcvFvLKIYwi1uG19n_iZwbMeUtMnoVprlvQO-34LSHy3uqITmAMIi5jw7GAqLBoZDzg-T5om9sP6Bqj_p5NHZKZ9ASKO-rkIQXmnWKGPK9yflPTWWNRoa3tjT7B2Abuwd2RDkT7SRScxagt6Pe8AgUMOhKCRlADSHpSGyusQvyMTwPBl4BYyOMZNk6Haek02aqcJOsSJeveLwbWnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAnNQgei2OYOo9j03iUB_pTDGYSWbBcFaJJO3-3hY80XNBpI5XaCJVnYB8PwXo-xGCQf-Zo7L2pMQQtjMK-_jUWnxfGOawKBPCvsOc3PJXWqhbsmqkQnGL2ZFJgJmLsmcz6e2pG4vh9CO4aN3MnXlxYZ7w2pCVbQRVWDc1TZYolJP_a4rd6h7enwu8WTZwhYrx86V5ySeQU40he0AEO2yORO1VVqcmOn5dWe0_z71CIOeXuzIMcYxD_ey2MmlZDfYnBcIpKVMKq-CkOLiy_OrlubOd-VePRh8gJWSXjhAtMywFYLA4Gd40xrL_KXKING_ojygQbeBvg1tuTOeMZR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Af8m5fFnuhpINfPfnJ7KIVrLJUfu7CquKB7cxPVLxTHDsD9jKM3mdJRt5IjipJjN0WnXFw06pPCOA549APHgBaBFZmYZU0aRBeACx5rWdy64nDeowfjkSvRurWtuPk27Z4E2ffnH47xtm4jSnZY-Mz6kD2fNiWQJB5hYPpxfS_j1wFCLfAM4plTu1zzXc2osYxNGbgrCJYEuf6P2_7erU7GUfdCL6JxgCkh51e97mmgseeT_3E6-A5cusGgakYrDSvAt9Tr1f0ojG3arSIPsBN2OrsscIqvrFLs_g3CWp-CVTo6a9RDk00znrmj0mGqiuCd5OjIHQt5JWRXj4Q5_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mBtIF90H8ApO_yaTIrUqPeVsEdIvkzru-ZyY0eP7ekuHRJDKuGjLOAAncRokBBEh4OguhLMmffeI1OOrIVDOfK9BQ22urf8Hv7b5ukH06Omz09BJ1sdvqpVMgdyHJ1FuhdiYOcfkCjxGKUctZ-PZdVVlHDBlN7JQpfftxYrG-Fhfg_M_pIFxgy0AijGnV8nQ7nasZr5JR5zeUorot3vYcsK1qRcfhH2sw8AMs90ykG0F0yaFDab25_0XZGCELFvL-4GG3fGOovSj9CxAYpuuYn6DzLwoCjpWjSo_4YlLhE5vvtzdyAajJLLj_m_uHgKrWmLca_wWne31sDnMxc565w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mBtIF90H8ApO_yaTIrUqPeVsEdIvkzru-ZyY0eP7ekuHRJDKuGjLOAAncRokBBEh4OguhLMmffeI1OOrIVDOfK9BQ22urf8Hv7b5ukH06Omz09BJ1sdvqpVMgdyHJ1FuhdiYOcfkCjxGKUctZ-PZdVVlHDBlN7JQpfftxYrG-Fhfg_M_pIFxgy0AijGnV8nQ7nasZr5JR5zeUorot3vYcsK1qRcfhH2sw8AMs90ykG0F0yaFDab25_0XZGCELFvL-4GG3fGOovSj9CxAYpuuYn6DzLwoCjpWjSo_4YlLhE5vvtzdyAajJLLj_m_uHgKrWmLca_wWne31sDnMxc565w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EdcCaL3u1XGlMZ3dQ8on9jRvqSnExVflINoTH4inuJrm2LoaZ_PQLqNd9mForvaKYwxSOpq-KhAzPYT4rbg8MG2x7_9fX0kjqbA7SrP7bimFdrI3nKKP-3gzJCMdi3hCFciqkzD-rAoSiXmT3Hl_fRKDQFWj5pQkfFOrFDRvn45DZbv7eZCqxRIL-YYMb5WSs_7u6GxdR-7_wPGJco_7bIf199fXg-qLu7DujhmfyYO6_OfMW5oaPqdNbFNWyBnjJvTNNy421fmnnOibL70eHN9IhqwI9itZZrdhmGrzrHRGmtTQAISz-KdEDJ21bSFfqKufv51GTR_yjOar90-oDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EdcCaL3u1XGlMZ3dQ8on9jRvqSnExVflINoTH4inuJrm2LoaZ_PQLqNd9mForvaKYwxSOpq-KhAzPYT4rbg8MG2x7_9fX0kjqbA7SrP7bimFdrI3nKKP-3gzJCMdi3hCFciqkzD-rAoSiXmT3Hl_fRKDQFWj5pQkfFOrFDRvn45DZbv7eZCqxRIL-YYMb5WSs_7u6GxdR-7_wPGJco_7bIf199fXg-qLu7DujhmfyYO6_OfMW5oaPqdNbFNWyBnjJvTNNy421fmnnOibL70eHN9IhqwI9itZZrdhmGrzrHRGmtTQAISz-KdEDJ21bSFfqKufv51GTR_yjOar90-oDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6YXfPSa5QYJ6K4mU-bK1ufZFfrOkQDJ4hpixnhITucA5sTjhPdz8USlyLBOH6n3N_w8UpZMMT4viNd-syo8mKmwmHQGX72NZth0_j2ktZTHVTB3HFTKiLWnCWnMoYF1ZenL5lDgKxY6PtHu9QpOUAP_AkmvIeFpu-rWSmhDa0TeN80JGZSeeHAm6lczfu98vJHgS0SjgtbY4OnBsNI9cJ5_hf4PtUlpEsmQxTlOx2VJhA1e_F90DPe3GZ58MqN09-iJ9E2g7zIexCNYQMDv1l-Rw_Wbn-N-Lo_zVX6CBs_WTwq37PqdPoCf3KVEYebQ5Cdv1WusHGz7gt2ddR2HmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=hgdh5ZALh1pxF9h7fCYpw2mJZd5MdCf5qajwc2rykoL3dNAQNtRe3lVRQtmAchTsM1ktpLdDggd-Xla2njD-qhezP0yYcrBQHBko6q5_mTmmuytoEXGMeO6nne8B4qz_EfKejiRsQn7sMzcXctuDngw6Myn-VFNS1ZgTOpn5SOEO_XnkmZVmvrafwQQwcL9kPO0OJ_1Y1tm-WEaV5BOBfMRmi4g_wdiziQp--H-Lr8Jt0uE2B2Id5R-x_5KwL_HVFlu3JUUH0daOLycu_QwZ83b_xJk2h4CLCPKrG-sxE_bcSc_CKgCtQIUs7ivgnR8BcZs-baQ5PPDJkNphwmjBpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=hgdh5ZALh1pxF9h7fCYpw2mJZd5MdCf5qajwc2rykoL3dNAQNtRe3lVRQtmAchTsM1ktpLdDggd-Xla2njD-qhezP0yYcrBQHBko6q5_mTmmuytoEXGMeO6nne8B4qz_EfKejiRsQn7sMzcXctuDngw6Myn-VFNS1ZgTOpn5SOEO_XnkmZVmvrafwQQwcL9kPO0OJ_1Y1tm-WEaV5BOBfMRmi4g_wdiziQp--H-Lr8Jt0uE2B2Id5R-x_5KwL_HVFlu3JUUH0daOLycu_QwZ83b_xJk2h4CLCPKrG-sxE_bcSc_CKgCtQIUs7ivgnR8BcZs-baQ5PPDJkNphwmjBpzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TXpTiUUaHYh7xovGeYyDXJj3gDDftUyKwR78xNRkmJqQ13zIItjSwL4qLulHxPqmH8FQjnjBic5keGpHRbefKaXaqsmN1lxc_mGwVgX1UjWqLM8OVZj-hGIjbJ1BGnAE6MFSye7qpxCrbqkS0n3aXrYFSnvlCAKMXct8XifTGi0OPmZCpb5dR37Jsn5PiJ3CCp6Rq1TDHX5HOVu7b-Usgd4S3LFgh67q2hDAws2uGQf2bh9oZUEt_GgHYoFc0LqsxTkqUsvomkCndpfiPCiUHQZdILV1UrOsTTeyApM-xwfkjybM7EoGlFmIctq8Btgct5siBhCxJNSx_ECqIwVJng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TXpTiUUaHYh7xovGeYyDXJj3gDDftUyKwR78xNRkmJqQ13zIItjSwL4qLulHxPqmH8FQjnjBic5keGpHRbefKaXaqsmN1lxc_mGwVgX1UjWqLM8OVZj-hGIjbJ1BGnAE6MFSye7qpxCrbqkS0n3aXrYFSnvlCAKMXct8XifTGi0OPmZCpb5dR37Jsn5PiJ3CCp6Rq1TDHX5HOVu7b-Usgd4S3LFgh67q2hDAws2uGQf2bh9oZUEt_GgHYoFc0LqsxTkqUsvomkCndpfiPCiUHQZdILV1UrOsTTeyApM-xwfkjybM7EoGlFmIctq8Btgct5siBhCxJNSx_ECqIwVJng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsD4Qcm_4sOFdBOmq3seDmgRQDdwOIK99FV_8PtAcUGt7o3fR4daeGe777GYdSRjc6PwR7ELTcRWEmUc8HkEyxu9yiF1qjkkMdtlMrnuIBbYs-cCKthv7oKg4tOCAnwcimV0FcDWtbV4cTxn-2i0byaboGmOpYVMi0kwZxVIMMnsb9KlEkWGjs3BSI40IWRPjj1-pxzhpL5cjrNbbjRDeURZLMC1tfNMJNQHro1SJom59S8LteXt4bvn7JIkiXIp_hz1A4-EeTHM_WucDlpjOq6GabR_0SnHGFI89581qsdh6SpW9hLHRkhyvJXYxjyMWYyuI_mtmDcA6GmGUsSq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djxOlTgX0flmgb5mKxzFV_fU3z-Zd8C_ztSZFR7QKGG0Pxzyzh_7cO0s32uzccPmZ-N7U_FJYGnEopk6ocjkbgrPQYLwQf2B_j7DJppxQc2JrHcYwwZx-i_GC97WnzXVpaJs-yd7Ykc3178J8qVhc9Hu-9BHFfRj8esj_WOpH_kdchU7Y2iuDQ_0KWTYk77K6C63aVsKW9ern1T2Qb93R60HbEqhERbtnBUzU-ebBbOlYRRVvtSP3pFtXHhoS9GA8FA970kvDLl16F5Pide_Y7UJkey7ZoMlUIrUwZTjYGKF0rt6_z_zbTvJnWbRHwCGlNyL7UsxmY3qTi8vq1bzhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Mby48IaDQxz3do4S2UzvHI_3izQ_0ufcBjnAKwAGRWJSBwtXkX2MhMppkU5ScfVai6ESFEhJH9M-c57TIsBePCR2nkb4eMxGW2frXsly3NIVhadkD2TfcItFmgf1WsUrzFyGs-zvLZkxcyKQYXEQOKH4zLpHw69PgLDHvJwN6ZOGW9KDuVinuoPa9XMYEdYtMsOGeOwtf1xBq4dRCHM2DMTHeGzExIoV400qCJDOXqcc80ObiA52lZQTS6PsA-Ljg-d6bqvyhWztQQq1WVeS7kgupPAxg861mp7QiYvUT8wS-iuwZHBABgaU6VwtWJ2hhsWoYZE9cupG6CMzyJAtuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Mby48IaDQxz3do4S2UzvHI_3izQ_0ufcBjnAKwAGRWJSBwtXkX2MhMppkU5ScfVai6ESFEhJH9M-c57TIsBePCR2nkb4eMxGW2frXsly3NIVhadkD2TfcItFmgf1WsUrzFyGs-zvLZkxcyKQYXEQOKH4zLpHw69PgLDHvJwN6ZOGW9KDuVinuoPa9XMYEdYtMsOGeOwtf1xBq4dRCHM2DMTHeGzExIoV400qCJDOXqcc80ObiA52lZQTS6PsA-Ljg-d6bqvyhWztQQq1WVeS7kgupPAxg861mp7QiYvUT8wS-iuwZHBABgaU6VwtWJ2hhsWoYZE9cupG6CMzyJAtuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqs2olDKueWvoe3PFSdDNTuUKheP0s2N02ZPJvtlOXossRtVnCvYQjZEq0g8ksY9FXxst4rZ9u1hltDc4q5vr7fSLnS-6EzfNHaBNhr5I-PCqxPhujsJFGEa6i8MFAlM5ep9ygio7QPEvQnc3SG5lHO9OoG2ffo3Fw5B0s2EBgekfvLUe7D31j7VoczcBqRPU3LPl8mqAMl2u-ZI99z5CNLpta8JFlMDc6X4gW1TIsYKpkVGtlZp2tgIcnRJSz6CXXYTVhao6HWmIxqmcAjAUUsWOBCnhui_yfJMI88jcEbFhXVYVrGjtIOrGRzwAuu82N3qrfw_ac8pxe_4b-Ul3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpHjTa1GixZGcqbXTmgE3JyTMOc5zzI9dWZVhNGfDMrcuev6aJzKiCgBkoE5PWtR7rUB9rWP3zX6oqOZjNmpdrjpQybZLlmB8W70A_wIu5eCZ8TVvMYfL-wj9Zmye13tA2AelWPHV6W8vI3GENRzAHWtdj-_DuxIvQh8RDCvoIojDARQgS4A7FQCzIHPHl5upjKlKtBtGxONIS6N3d_fdcdeMF8p78ZhcH_VQp1MxSqW8TzSIPaIs6wmZ1Bz9S8lvToWgPkNjRp4D8GoRixDyHMuJ3W7cAlHEOYmhazf7KmFt1_jpHC8cTmvqUc35YeS1pU5qfA0kbIGF3YTXwgiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-y8_OfC4WND3zdh8Dq90jr6_eTISIugg9PsUD-j0pI8-wJo36sjoZj8vf3q0C1V31YDwnbrSevDTfayLS41T24qFqIah2fax1ehoislaZ265Wi0nk6cNg4CDW-4GIyQgzPJAbpxWU-ax2qrSGmJe72RPU0a0BokbpnJRiBsKCs0FC3WGJnTFwxBMu7wlY3SAV1lCbHh1IQXClxQzdrUXHpcKO_QWH4K_ZjOR27XxAZOlITO-nKV03uaC0fr7hSGoMcoy2hvb4dHfPVGSew04nWVpChUOiwSQDGivPxUJ7Ae7OXXntpU0MmdH1x-MebMoIrsh903DBbd_Ua9qbvDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MgcJhyG6R15ZDBUVWUHrZB_zzCRWhTPZRzgLqbe5AbkwQtFNQAAzmd_2WxQ4jOfbwhQ0N2r4TaKPFmY6H8WAbU-_Xoysc6u9kMzge4iAw7mFZwo4qEdbIe1X040VtvPmeyAlaLHlSzvekC-6pQBYdDQzQQm-mtBlGusmL_enzf9weXnw32pSs05Sz86wZ5_0ttNcTybOYeB7R6OxXWMhdD2Y5ixoY6BhL9wboH0QyQvT1jmszXWUi7fvflZrS9WqmXlwezoMTyI4HaSJsq__JVIJF5i6FEhKGmQe-vPGlAv2MnRWdi8ShkMKYT6KIfUCqgErb_zpJh9la8lWCqnPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MgcJhyG6R15ZDBUVWUHrZB_zzCRWhTPZRzgLqbe5AbkwQtFNQAAzmd_2WxQ4jOfbwhQ0N2r4TaKPFmY6H8WAbU-_Xoysc6u9kMzge4iAw7mFZwo4qEdbIe1X040VtvPmeyAlaLHlSzvekC-6pQBYdDQzQQm-mtBlGusmL_enzf9weXnw32pSs05Sz86wZ5_0ttNcTybOYeB7R6OxXWMhdD2Y5ixoY6BhL9wboH0QyQvT1jmszXWUi7fvflZrS9WqmXlwezoMTyI4HaSJsq__JVIJF5i6FEhKGmQe-vPGlAv2MnRWdi8ShkMKYT6KIfUCqgErb_zpJh9la8lWCqnPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=AGdMK9rTdoc5db6voc4Bh351-vLFD9xl5uq_2x32BObROWwqd4ihjTm6FXJzAEd5-59i8DRCE9yU_SDdnnCd6aV6Y5Ad4gZwbG20-r4hqtExPGwi1ooMYMv9EnmKhsd30XcyB_Un0lFu1J0nstawOkVYE1kS2d5DCz-yjhodJZeontFqASOq_FYnnRhETEJBpKWHwQ8Xpkk2wSEQTawohAD8G1mwiekN72stBrCKXnjVNqUiJm2CobTAb6yN4d4S0TdYI4p5a628aYYaDbBZF5Aje0rK6mklg6n6SdjdXbj33gv9fiTRQYFQ-4z6bDvfys_3W4wiWCdfxgbpoAZHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=AGdMK9rTdoc5db6voc4Bh351-vLFD9xl5uq_2x32BObROWwqd4ihjTm6FXJzAEd5-59i8DRCE9yU_SDdnnCd6aV6Y5Ad4gZwbG20-r4hqtExPGwi1ooMYMv9EnmKhsd30XcyB_Un0lFu1J0nstawOkVYE1kS2d5DCz-yjhodJZeontFqASOq_FYnnRhETEJBpKWHwQ8Xpkk2wSEQTawohAD8G1mwiekN72stBrCKXnjVNqUiJm2CobTAb6yN4d4S0TdYI4p5a628aYYaDbBZF5Aje0rK6mklg6n6SdjdXbj33gv9fiTRQYFQ-4z6bDvfys_3W4wiWCdfxgbpoAZHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=QOYDDBD9r1NGEVqDOOT13wOwZrPqgbbtOfnSTSaQ5wCQx8BnH4bRLyFaQQW9sW-PqYYPfP_D521zsPq27lmD8EUPfdxYpdOGOOgyW3dHv-lR5QWx88fIyppnIxxJZXLRhyJFdFhTksqe7ycjlIP5w4-ciRYzhGlB7UtT5x2Ms5pPVGKwmEKij-gXPLBF4I7X9SCaLqDeJn6t3T1dGBm3J2VzyA4nfGxx22Xj2rieJ0GqZ6yUDtMZwdiofyp4x43bTXtdbYKEuqGFGLLWKyCzimoGGkkcOYeYk8LnIjiwSWKhYVNyBBLpZBjHZCV55Zjo7l66E_bcYrBj3vAFPzKEJaU7oOBirqM-gYeM9rI2U7aFbmymb7NHTmsUmQXwAVhISz9-Ez2WidtMrlq3o-eLK8BXnASeX3r2TsAQh_lwcSrDOa9X-N5pEGFPuUaOO5gQ7gbQzlCXyC5DG3dt8IQ2rQIRXJHUNiNq-xfek_kf8_djkh4R8rMmpBaq9_WhkB_YCPmTrD0e1crjVgvqy8QGJoL7s2S81EgGPasbQ0Hyg4dU_iXD5cxiNqPqFXXXatLB44mdzjlbWmTokdNc3d841gcFi5jM0xqeDCNmm6U6iwNgYgXNRlM4lk4d3E4NRq9iUVAIUR_sZ37kNQKV3h6dhwgOm5sZcTKDKEleiiIIP9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=QOYDDBD9r1NGEVqDOOT13wOwZrPqgbbtOfnSTSaQ5wCQx8BnH4bRLyFaQQW9sW-PqYYPfP_D521zsPq27lmD8EUPfdxYpdOGOOgyW3dHv-lR5QWx88fIyppnIxxJZXLRhyJFdFhTksqe7ycjlIP5w4-ciRYzhGlB7UtT5x2Ms5pPVGKwmEKij-gXPLBF4I7X9SCaLqDeJn6t3T1dGBm3J2VzyA4nfGxx22Xj2rieJ0GqZ6yUDtMZwdiofyp4x43bTXtdbYKEuqGFGLLWKyCzimoGGkkcOYeYk8LnIjiwSWKhYVNyBBLpZBjHZCV55Zjo7l66E_bcYrBj3vAFPzKEJaU7oOBirqM-gYeM9rI2U7aFbmymb7NHTmsUmQXwAVhISz9-Ez2WidtMrlq3o-eLK8BXnASeX3r2TsAQh_lwcSrDOa9X-N5pEGFPuUaOO5gQ7gbQzlCXyC5DG3dt8IQ2rQIRXJHUNiNq-xfek_kf8_djkh4R8rMmpBaq9_WhkB_YCPmTrD0e1crjVgvqy8QGJoL7s2S81EgGPasbQ0Hyg4dU_iXD5cxiNqPqFXXXatLB44mdzjlbWmTokdNc3d841gcFi5jM0xqeDCNmm6U6iwNgYgXNRlM4lk4d3E4NRq9iUVAIUR_sZ37kNQKV3h6dhwgOm5sZcTKDKEleiiIIP9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dNqkyfTLKLm7YRcSVZR-fVcfOrCyyGKfU5kYxkSA0DJPF3kJ_dNLxzwzo5LNzW57m9ESsFZqunIFJy-yOSlljpoe6WetExMQKDc357ugNaYgu3FjgaKogL6XCuLYDAziLM3hhHONKuGogzmFURK-IS4_NY-mAH088dWSrYPGS6WBk__mQ7hvJy5UzezXQikCXkd-2isX8z3wjSVI_ay2-pHmuxb5g5Yy-_2RHR_HxlCsqbztvn-dxnKREPLnnxld48JyZRox11wd6aPQovNSGXu6Va9hQlDHXr0C1a1NmVGgIjYKUMh8riyP2uBSnl0yUHMNg-7FrVF2-6drV6wY-J3jSVlWTytIROhTJS9kvAqSfqC5-TDuY2IRywmZWEnfQdGq9adD-Xbr6uFGUXoHDynA3tGQAe-Ald7aChTzrw4XzCqNZHkPRDzgjsVspk7d5XXvkXraRE74bfWBwNaZVB5yzQLwHyQunRkfz0983-bydKfUf6tZjKRJA40IwE-RKtbW7FOuU48dJV9YmOa3oJ6-n7ONM2RRZNKq9Ge5utPh5tE26SxICrpa-59PvTxzwdGYebAN1_-eEIIJPo_oJr6ofE258tZEBA733EQCZQOnQi-22bZjmqtv-Bavvv3VDtm-OT7ScMVMS6TNlr1qxuk2vS9EcDb7nSZ8wSPNYx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=dNqkyfTLKLm7YRcSVZR-fVcfOrCyyGKfU5kYxkSA0DJPF3kJ_dNLxzwzo5LNzW57m9ESsFZqunIFJy-yOSlljpoe6WetExMQKDc357ugNaYgu3FjgaKogL6XCuLYDAziLM3hhHONKuGogzmFURK-IS4_NY-mAH088dWSrYPGS6WBk__mQ7hvJy5UzezXQikCXkd-2isX8z3wjSVI_ay2-pHmuxb5g5Yy-_2RHR_HxlCsqbztvn-dxnKREPLnnxld48JyZRox11wd6aPQovNSGXu6Va9hQlDHXr0C1a1NmVGgIjYKUMh8riyP2uBSnl0yUHMNg-7FrVF2-6drV6wY-J3jSVlWTytIROhTJS9kvAqSfqC5-TDuY2IRywmZWEnfQdGq9adD-Xbr6uFGUXoHDynA3tGQAe-Ald7aChTzrw4XzCqNZHkPRDzgjsVspk7d5XXvkXraRE74bfWBwNaZVB5yzQLwHyQunRkfz0983-bydKfUf6tZjKRJA40IwE-RKtbW7FOuU48dJV9YmOa3oJ6-n7ONM2RRZNKq9Ge5utPh5tE26SxICrpa-59PvTxzwdGYebAN1_-eEIIJPo_oJr6ofE258tZEBA733EQCZQOnQi-22bZjmqtv-Bavvv3VDtm-OT7ScMVMS6TNlr1qxuk2vS9EcDb7nSZ8wSPNYx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=brF6xC6w9Knlr9QjMPuB3MA5cPhwTJBNots5Y8Z9swTQDqSPTT1075KkjCQZqLLrNzu1tMkzOPwY1Hoy-FO-OywPhnJTU-oXpPSwlxqn_4EjjLPcGRL8lVzZNyxnSFjZIcuFUlIONSL5aucVneVamjXinhUu6W4wp5eonYHx3qH-h__byfsQamiKm3Pd55_2r2w9zjHLvwYaXDVV7vUrC-dptkWJPHYQ-IfS6klgdqlKdPD4XAu3p6ezUIaGxX90abYN92WOEDIiAVIIpz3evyXHoSzXYsPdg2KfllKJp3gj5V1eO9uOaDoUnPhyCvd0DG8Zm6_1DkayGorAocp9_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=brF6xC6w9Knlr9QjMPuB3MA5cPhwTJBNots5Y8Z9swTQDqSPTT1075KkjCQZqLLrNzu1tMkzOPwY1Hoy-FO-OywPhnJTU-oXpPSwlxqn_4EjjLPcGRL8lVzZNyxnSFjZIcuFUlIONSL5aucVneVamjXinhUu6W4wp5eonYHx3qH-h__byfsQamiKm3Pd55_2r2w9zjHLvwYaXDVV7vUrC-dptkWJPHYQ-IfS6klgdqlKdPD4XAu3p6ezUIaGxX90abYN92WOEDIiAVIIpz3evyXHoSzXYsPdg2KfllKJp3gj5V1eO9uOaDoUnPhyCvd0DG8Zm6_1DkayGorAocp9_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va60gm9MJyLFpYK6dlwNeczHltE_adIJ1ktHjwE0Sv7G24_5lBIx1Kedjk6LPTzvhRIKZzpo8LASBL532wFdR474bb8INap8s4bbKS2gwaOherB3vriPrWWyNPLFDsbHn01oCUqpecdAB3bilex6lqlaEOp-ErxBDp1oZOO-cvLm7QLkdld08S4r6N3RCGKFk6QHcqbpo7FSAkocykEU2hrUbHKrSBQW-Gl_TSnt83QXjBbQ5A4VxaxjHzEaseTv5CwwIKMXEN0GcVLcc6GbHaASXGokJiEwXS-U82BQs89467t6r8R_qRzp52XVMYrvn6WHzLA7J6LPCpzvsSVweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ldOEX8C_Afcn45WluF8DzwcbJzJK3WZcOg7Iz3XLU1VOGw-QeidCRzE4OeWS2nE2qUUXL7YsIiruD2_1qlDMPMsbH9Njlam0JH3tLgC-cPDZoWTWjBlNz2NQC_pwWbn_HF0uUCIo-dmF5iDDsv5g_ItPTJr3H6unX4eyWPa5VofziINvRvoJu_1YT6ESJQTkV2nxoWoeA32HBfeKPfNzxsh311jcr4TfXtXv-R0Ba-2_amffMeFL5pkYVPkh1a118crT4oPC2Y0Rfj93oZiAsF27vRiH4dY1aLtO5U6pdHCIMycgeIUjIUndBUgzLTrGuKM6mqITioPG6ZgGuu1zKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ldOEX8C_Afcn45WluF8DzwcbJzJK3WZcOg7Iz3XLU1VOGw-QeidCRzE4OeWS2nE2qUUXL7YsIiruD2_1qlDMPMsbH9Njlam0JH3tLgC-cPDZoWTWjBlNz2NQC_pwWbn_HF0uUCIo-dmF5iDDsv5g_ItPTJr3H6unX4eyWPa5VofziINvRvoJu_1YT6ESJQTkV2nxoWoeA32HBfeKPfNzxsh311jcr4TfXtXv-R0Ba-2_amffMeFL5pkYVPkh1a118crT4oPC2Y0Rfj93oZiAsF27vRiH4dY1aLtO5U6pdHCIMycgeIUjIUndBUgzLTrGuKM6mqITioPG6ZgGuu1zKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E9l2Q0m8zRpbe5SzwOlhklmYLmdtjz6njWOLDvf2LjZ9La8MuI9h6qyJ9ZkkKbMh35G2N4PbhrTS0p5yckSfwKg6tB1Ib5yjdyYfVNnpbiKLMnVUe0tf734v2RkNyLxPTGzXpSPs4I-uWfD3iM2cM3QGPMQFIt9VbwCT9UF7Lb-FRfGV5qiwc0nkB_CKAi9rnZ1P5FxNZGEJ7E8o_XAqtuLDOo9AhFAowWGK4ZFv41GbAHRIlYENF52WOQG073F2DtzcuqStUk-9muuZSbokMz4AAyIOnZT3fhMpG5AH28ZZhnmnXkL5Ktv-4Yv59WdAuN0lCJrWrS_msbl-Oc-FFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=E9l2Q0m8zRpbe5SzwOlhklmYLmdtjz6njWOLDvf2LjZ9La8MuI9h6qyJ9ZkkKbMh35G2N4PbhrTS0p5yckSfwKg6tB1Ib5yjdyYfVNnpbiKLMnVUe0tf734v2RkNyLxPTGzXpSPs4I-uWfD3iM2cM3QGPMQFIt9VbwCT9UF7Lb-FRfGV5qiwc0nkB_CKAi9rnZ1P5FxNZGEJ7E8o_XAqtuLDOo9AhFAowWGK4ZFv41GbAHRIlYENF52WOQG073F2DtzcuqStUk-9muuZSbokMz4AAyIOnZT3fhMpG5AH28ZZhnmnXkL5Ktv-4Yv59WdAuN0lCJrWrS_msbl-Oc-FFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erO7L__vvypl23_nV8efPJGutmvNqZSq08LfKboQOFxjtzLkkaXiRU_oNymrZlpYuhslwAb4I7pkU3adKSrsuOPa3-hvW0gIG6N3bvLQbghNv78DNas9PHvHO0l9O8Dj4A3MXSDuh-6vgQToYGFWYiP9h230Qm5RsfWwwLpPPYAOsbjVDk-9Ak1pd7MRxNuQYXmJJ7SUeeWk68EaTrJwlTgPGExFs5loDcEv-HhlgA_JGUIqciv-FXKCtYyKk2rwQzmHpmbVE2sVKBRU7toTNOldN6fIvRBoVZRLMMZkfyiwh9Y4TmFL0vNT5WMNks4EmzgV1kfJnaK9n1d_qbIS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLYHBuq9KwPAVBGz9fjUlvnvSNatV5mxDXi46sR_WT41wRpvwNdAvJgnp3TJ6c5NzAiiabfeS3o_VHLJNlmd8ct6JmnzDq_ge28VqbUgzP9i5Xw1YkpqAU46dk6WqTW5UPiz0tp4-Sb3X6xWH9Bgb4zwZuU8c__ett0Z1m-U4mxq0XNoAyh-i462CgmUCbR0Kprabhlo477wdoFNEUvlvirBoKHA3GP_daT2QqTiGWH8sZEdHelHvrsBZwBo82-MnLKzIBMuxqTb7ZOd7msDwU40S85Dwhpv-Jz9v8zDYiS69TAZkd_KpPYONpI8tKQvmOBQ56mvRa5e32uwWGoHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMMrSk73Nyvn_LHfVPDebpuEweo5zJc1AedSWTlyfMgJ2CTdxnA86g2OqZt0WvYPxmmJGBbQPW2PRsjkdGAQ4xNe40OtS3JnoCmVq9wiwVbJfVxcbIukjlct8auiVb6SSO2CkxFclseMLR8Fy8ut5t3V8cnod2tRufBpyOJ3V9kYma-xz4_scRAe1KmiCUrv8XpFauyj1442aK0saKMN8nzyFj39oXtmdgqke5FBxxbD-fkKPsxUTgK90iLBnaM4GakcLNaUGFOc50U60I_BuwS2K0AX9kCtXhxN6zSHF4kERHMfha5uSabSVBbsxrQL3IZGkikioVcg4ULeaYkRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5JU6n_POrLWTteDaTI2v0CxLmAjX8zRD-JBu7ibZZp0_3tBoWUiMJCmyPuxUbcU5G7bgXfA-1m5YaCaLGTQX97x7USX9fsiUO7yWeMpoAV2ola3vC8a1SH2lE0vXDagh4w-3fUX6S2IibD51ITR_YxZ8o_fRP0VDxB1z5O4vmBaXx9jnXA-y5RJb-CUOjNrDrlqV7pGAc70-Nb-yf9z5dacl6h4m4ukAkTULGGwzVuU46_h7KiwxGV54kobUjJ6K1_wMjCmUZl9UuimPGQvB1FScEvgBrufi5sVNBLrwFxXxh7CmeX2ismMN1nXc0-M7IKkSQgml6TiN48PxrA8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfb-B_6ndNXahA4rhdML5SJBz9gm1AbFyGUy1xAKGABXNxDtzS9kCGo5eBGDBmgIIohWJ7hDGJXIXCivpkTgxvrbujAPFSFadIT-h3GWbo_EZ6-_qaTXRWfi9TIbRscel0kLLgGmnuX-MWSvVT34ceXMrhAdA_IXHYBvcJ5HC-qSTQju53xI2F5Mw6Xw3T9JwrPvZRS2WYkAqK5MF6sQwKjnJWusRD4PapGFkIX7vsL2V6vlwh4lsxPLXk1NmuJ4hb-jMeXVy7RZ3Q213GbBR7vxT1SOHPlUPW7KWR5MYjKYQysIPzD70ZliTCMZGJ35EEouNgHZ2DoW8o5qD6Bcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuN1gXShlI7v6-LfKh-UV35YAisadgs7y5jP6ZbkAzof3xCIT6Gkihtx0Bvwb08M3vv7YvkBXTgpBghRW9Cth9FpL0-AuCxx7dX1vFFCRaAQXPz-1cFwdEv0EHKO6IIO_axuypAzFjHZ64K-ZGXBmTpn1XA6PMDeLrRlt0-jqkgmji1Tkc0SM3nSAndcEhZG1fKwCYIFiwIVaE4UO5OP6wAVGKE9Dzpo0oJOFhxZOLMcIVGCJR3XxOyzeXr3668wgVpLyLDsIuNzHNDu1QQt8xe_QSntItntIeJ2n_ueF10k90kixZ90K3CYaBNlicaEgc9BKhW5-Z40Ui6hE6R_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emGCYATO5wWXno0G1-zjaC4BAR18vdoc64wTJ_DP-3K6vrT_XKFoLSW9b2xDZ4dYH-ESCdnm9RCUX0-uvKicRy_RlWmKBx2owTeoCBA6DEqEUJjHpSJ5XI20zWa1m6LHlo8TT58C4qPIsoTYiR3MdKotVeIy0Pbwaui2fi30HH29qPa_skc-iu1rrK2nrvvSVNT2oRW1-Q_rIfn96uvs0mZLL_oyamLPz6BMtKCQ0uW320OVgvwJx-MKdPfeioIwsJmgiPECJqDTk47ZgNwCmKaxvIMqflGeWplkZr6ZkjIIlPBLkmI_WaLQPTyh6C7WlvCXSXdFQ7ivt-Q3oG8aWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmaWyMlAbqqvnFFFjy87Ip5Fj1ntb_lXnhH9OimsFzNIyp8yY8qpfffHcZTCPqMB5AHRi9ox9eqnoiqwMhAnMiSuGgl0xpK7TcrNLHn0slMzXtUlDenq8uX702Dv0nMvAlMVbONc29aVLBIZaaVToMpill5miL7deHuNwnKO246zfpemAsmq3W5MJtImqLVF-rPD7hb997TPqzxRBCZL_TWDwumxIA6EfB9A7iFRB8eTURXaTJm9tMrM0BQXadotNq41kNTtsOLuLC_X6rRTArL8Z40jF6d5QqUVzTZgjlZCaUa7AGnXoWuOir4dI_zGFTl-S4pKn03GQ42USi3ADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGPIKZj7xILKl-rzRc-vdVXsNTzRwAvk92PLnJ8-ZIiVuhiivoUQl-ag0IDdal2zFp65pUMnWvKNnRcL9WToAx2ZN8MzrILYNWg7qpDj1x1Yaha5FYMbZyzPgOcNC5kuDVpIBzK4j0QVPLxpzupm_4tw8w9Y7ACs5r4n6ocHYKMhWh5vsmKZLKHMh4FYI2EtW0Wa5rfl6Xc19q-qsZOGbeh_D7iYEPtrpZDKNhiZx1WqQZG-flaW9DKmKWNMafI1K0rYscmSX64h8x3h-RjqYV8tFYqb66ZmIusekmtqW-IVXMPZRojTr9AzP7tn24KaR3jfqPakE17IF7gTTG9l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIF5xtrkG7Y7pacfGmwKKq1N6i6WSsVA6fIjQwLZ4bVVwzI6VbjbApVt74r9WyNzQ3YUA77YMHy_ZZOUbvghbN52psSnweXC2IVLAVBYBvgxZ0ybJgQfNgzo0-aLPYM0CzeUxw0xiIBWt7ied0ujLMB1hyn_5QWNfjAd_AiFrx1k5d3qQHi3-YnKS9nhacOsDYLLmjkmcyArJO0y6VqBhEWFGgQFEI3X5KXKybJiwhPB63zDhwtnLeHmCmHUbZa8GZiLf6p0vebz0aUL9bIaGku5-q_3KFJHQQeZEya0RwY_Iwk6kngg_txgzvs3JSH1ByTqQjnmjicJSz6IIi6z4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ucAZBdcVVPJ2DINoGA4MWUYCbmjRQpsJCa0IXuj6OJVXZv0qxvbL92e9t4KL79798F0_vD6Ils7ghjmaznoZnuvplQ3dq-GCfRiZVh3ugJhCNJHP-n30_NcFzYV1YkIcw_xcggPrPagz5k8_9UZvsdO5zGZlRBE7pNx3UK1AWYFQPuh0mQltqBqe6-4rl2WjWq_8UFDImCAkvwSwjtctB-BS2X9G2hykICRQeWPDdMHRwDNaWsS_Y2_YTf1FUUKXUSVRwhHOE0WImPonejACSIFE26C_vU-M4tzDautUTUXfKR97SpSXuk7uLu8mfG25uStAp97LGTQKosh6g9HW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ucAZBdcVVPJ2DINoGA4MWUYCbmjRQpsJCa0IXuj6OJVXZv0qxvbL92e9t4KL79798F0_vD6Ils7ghjmaznoZnuvplQ3dq-GCfRiZVh3ugJhCNJHP-n30_NcFzYV1YkIcw_xcggPrPagz5k8_9UZvsdO5zGZlRBE7pNx3UK1AWYFQPuh0mQltqBqe6-4rl2WjWq_8UFDImCAkvwSwjtctB-BS2X9G2hykICRQeWPDdMHRwDNaWsS_Y2_YTf1FUUKXUSVRwhHOE0WImPonejACSIFE26C_vU-M4tzDautUTUXfKR97SpSXuk7uLu8mfG25uStAp97LGTQKosh6g9HW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVWnUhwT9ERDSSnVoRxBMdYeyyoGWr7QYwHLBqjgdKFmsMUvqdDlqKJheuKpZbmZxTZm22PAEWVqsyotfv9YNdS9IZwwaDPoT-tUduB9wEaydMLJsAkC2cF_OVbCinii_fltM0LRNAq6k-ZQAS7WNoSvrqWTti7mjQTayLL3rtGBqkPH9vmh9ULI08M7X_ru6u5WYlfOX_yz-_vOUP8xkIUx5K2aXXs_jx12tTBcUumtz6uj7fNLBDfzkaiNneOqomm9J8-iuEfjrvCksoVcEaM0voIPAY1qJHN9_Fo8WCbnt287vizAQiS-xH_qfnsxOsKUFjVYvh1wlewiwj-FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnCxhZt1O7fbcPC2mclt8mpdmChvr07Q5Xzk9b2ctG5oow6TyQLJSbMbvkKB7W4a7huG0sE2G73FpSVt-eqCurbofgTTjn3uPi6tzYOQxsQIqCHjI9PC_eqoJriY6sY2vwN8SP_EgR2tVPeC5-rHyf6GuI1Nlh1iTO7Ra6AM1ewG6Rcbjv0nQfUjuXCaAHTqSs-llae6ERtgT6Wb7kt5YCNME56rr5hWCJmEqK0f20gEt46UyHsf4EdTJf9RCfx3Udk10sDsOVCOcNjbilDQnwZu_AK3BbRXeq6S0wnFUgOkbG4V0ehCB6z6-a6DdsnCHAJwsNYQGm3p1ZqfFfBIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WfGYuvGIQ2pQB9dFiEVyh554g3AEJ2OeZpwcQe2uZYbEwjMVjq5aPVeDixpioVvUIkdOnZRjUkzsoj5sriJB4TETb1r5Rgxknx81WSwZhfNnJsGYRG0hPcNATPy0EQJmNdS1fW6IFJHCpfo38uS3EA22tnwubHDNgipy98TA849H_gtcgQiQ4sj6aN1UObNeb9WZ2YWiP7FH0zJQoRn9Kr7rH0XQQwaSnvpcqUJ7QPGhc_l4lYBXP4ZlDLOJYmpxBL1YS6477g8nlZ0-pHkpQUAoYQBdcBbS_sOmhl-PAu-leVToROSF4KA37WuQvFAsKju-CugpoFtvSA5SPMteLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WfGYuvGIQ2pQB9dFiEVyh554g3AEJ2OeZpwcQe2uZYbEwjMVjq5aPVeDixpioVvUIkdOnZRjUkzsoj5sriJB4TETb1r5Rgxknx81WSwZhfNnJsGYRG0hPcNATPy0EQJmNdS1fW6IFJHCpfo38uS3EA22tnwubHDNgipy98TA849H_gtcgQiQ4sj6aN1UObNeb9WZ2YWiP7FH0zJQoRn9Kr7rH0XQQwaSnvpcqUJ7QPGhc_l4lYBXP4ZlDLOJYmpxBL1YS6477g8nlZ0-pHkpQUAoYQBdcBbS_sOmhl-PAu-leVToROSF4KA37WuQvFAsKju-CugpoFtvSA5SPMteLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=kszAYjdXULm3cVAo6Df5mhycobs52ho3uQG7WNnaw_V8NY_oLCjcnT7yiqfqZJVGR28DYmf7aozTciHOgPKFSiN7YCRvCWvN8fejckr-nnsX0J8sux5yp-i5L7Hp-MwDqZlP0rwhIzoystl5s08xCzdiemHz6pp1H-KMLSqKWlXBdmkAhIG7QIkSrc8aV2j20Y5OoRI6jULcVERoAko2mTuKmFrl1naPid_54kRNWP2qffyqs6gybsDzlNS3gKN0ErLxkCdaFX04Blmnrui6rCv6SGuVWH2trC4brP0WFCXKScGq63FlXniU7hExQzkAEgnFR7snU13Y9NlTwMMcQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=kszAYjdXULm3cVAo6Df5mhycobs52ho3uQG7WNnaw_V8NY_oLCjcnT7yiqfqZJVGR28DYmf7aozTciHOgPKFSiN7YCRvCWvN8fejckr-nnsX0J8sux5yp-i5L7Hp-MwDqZlP0rwhIzoystl5s08xCzdiemHz6pp1H-KMLSqKWlXBdmkAhIG7QIkSrc8aV2j20Y5OoRI6jULcVERoAko2mTuKmFrl1naPid_54kRNWP2qffyqs6gybsDzlNS3gKN0ErLxkCdaFX04Blmnrui6rCv6SGuVWH2trC4brP0WFCXKScGq63FlXniU7hExQzkAEgnFR7snU13Y9NlTwMMcQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-lckGq5cRzPrAp8XFVRnY-bJFckPNNsMgWuLBrOfjaQlboPBAOcpp7iV_vSeo5AtnvADMz7dFNJP9nk3JeDN-GGQj0y5d-nikaGGARaUIDHGRHVjvxEjy4QNOXZPMWQG1W9NUkISO9RKTBN5jlDGUf-tsjZ2KxgQECQRF3oMfWGfIpo-PX8iRRLyFAQbziMdC2X-g6qV4UBi3-ITzJ6iLyUw7RZ7i9GzSO6tSESx_nzmVhi0PepILRr0WbmXWiePxgFY-d_7vIjYp9btpkPpq7Vm-8yFG8SQ_4XWX0KH8ZCVegihbD4-qw8PENEWyoGLHpDXHvrXElO_Vb6tr3noQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlNB8fqkQuo5bH56UNEefm8vphygSgRTvsm2UXGhkv8SL8db2LleT0tLxHRJ2epJWUEVmpBtw23vpNJi0EaFgeqd5BcAYxe24Ii3TN740Pryv2xPrxNI9pnA6A3jdXIu9Vji6MF6cR6R5bX8XC3xiclMDItHVCOX-hsGuLIpAB9YytjncoapF1E3e2M0U1ItF7S63AaXvsSncwhjd47_R-s3plUv_SOUyOBcZNmRTU8VSmtxLEI9vqQvShXAEJyjwMhcZonkRJDWeo1ko00sz9uT7w-GPyUbAk1QIM3lM6H3QTOlieDeTq8OIRrDhTsDy-ezo8AwaHKkkJdT9arUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtZ-XsiIcuC_oVxzOJTTSTRxYnpGfZU1DWrtw6I2wRu3SaiA8ecMJdz6MfGbzVdrYmWlIWdpBpUKbQPumzuHQXmL3o_ixBQ70-6kJgIITSNCdmMcPrUZSiUoZuF1hcP7egZdT_UnJ1YcYkGh2fr1FWUUAUJef_DXcC_oBU-LgWIOVWRTKYwNNU2RFWSxEOpfpKESM0ag3xVVDmhqwfJwYntGJEGVDORBY-6YTDJj0L30nNZBUGpDixDhJEDdEytcGdFK-SMbH1rP_4IATMmXc1f_uzSH2TpgVNenCOqAjHTUGvqdTqogLDQiKPYhyCp_Tbzia8qAk8pXxz0qFFUYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6CSQVQl0UkdT_ZqGN5FG6zpYMBp0Gs3oGwP2zoVahjBQl5JJZaenG1WJJbXcgWPUOYqXU44kAsLV9Ylvv3wZ0CRfvUEe246Sf6x-ZaJv39a293YNGIcncYQMU0UsrzFHbD8jVmPiHtLZ6IJ948saaTRVtg_iUikIx3xLsEKgijD92EKAYMOYu4gR3cRqMxSdbAHMbh-mM9b_888ofqKP9EsSTUEqqCqjwxJUqqTOQokwX7POakO56cik8sxs14H3KqjX_z-_g9HIfGpnovjYKeu-vYG0D5LyEPhKOTQSZt3thT07l35_5B6mNx-VAp7mVBpxtE1-x_er0bu6HY1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNZDbhRr9aybDbjjCv4oPKbayWSH_axFG5lFv80ZcH715FU7W92TDlisdCbIgF9fguyUJSlMPcvs6BzeT-nMSenEUb3MFJIJ3P7275hPvFxKCmXJGZnLTIUsaG_nIK2q61D8FtU8v7EsGl-IKUIR2zinnurUsIv2JDJLgGaVwx8OXGGsoXnwPUgqgGIyEHGIUogtSG_fgU-N6uKBRYtGsr1o8shUffHOrqn3m4PfkqeQMIcYcqPAaaIFueS4GQjGgTDjeskoHlRD0RgufmDOlNQ28YvJTlkbITFCQPdDr7OcXXSKnWXGWBft9Gx3KRd6X_5pq5EwKVQph7Mj0EYHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc14bIePk_TPar3r42Qz2fi4gShPNiB1RNYtdDSZ8iR9ZGSNFv--oheVTnhpDgyNxq67rrMDeWGWa41O2kg8_S1Nth7_Mz-MLVCrLvtLGExYOwNzlEt7B8c4liyfMo_d5BcRFRv_ivCvZiXrO_BeUwRtdqV-r69yQUWcXW2s70-Pjno3GNN3IpRyBnhzb9h29xxcvxDjJKEctGOc_33OqVlH-QaZwS1j5jshkdqKXAoVE9IoMExgYl6czSaM0vPytXwBDbbs_46eqLIYFlRX47B_At9hmv3_lOGNtBC_wCxHkT-gRg-8jnbbPVdxGSjAijnyL8pjN_vtyJbBsciENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdX1mFNhlkoSuv4QX_U_yeY3JIJ-_kIhJePPaFb0JI-Oi9N6K8olroyELuFjTm4mm9QQHFJHeW7FB5nsYEAnCLAat6HQxK0c7-KDvfmw2nOPf6kCl6yOfKQz8HHO7ZgIlmsnpP1tml4-cEstODYvWeJR0crzahhVcJ3DiFsQ0h2HkF_jBtZFwuvz9TgD7IyUmxlvWikFo7N7caCdpGNtf4NrWfGufLiNJ-Jsz7b2XqlFiirfzMM0KHqsYUZxlgp8H6Ffmgfxv3X64yRiDTF8Af-XYFaxbdU9qEsFPi9e_v5vhP0oiWL8-gtewKQNMne7RkN2CWky-fsI5_hslmldOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANnA9S-qugSRSY9vseGD-PifuAWzZ_hHO2t17jGqZNe9JtTax9c4mFlYzlBaBHvNgw4p_Y4aQ91hu5k_Iug1VdxYOFhIIJPnft2iWcOmq58eBK7EQSuEdAA53wXbHCo-cKAa58fF31CWx24QIgmLSChHRkgV_xtf0Y0zrqy8mmtiG85m0YI_LaOlFqM1oQWN_uwdZOAMKeAC8KEhdx-nANLCOD08veYC4pzG8lpSU-sZn31zCrtrnCyE5nDsDq60Ljge7JKozGy5xYyHonFl0RPqEa5NTGwWuDhN8kQc3LL-de0bX3bGyVlKkJBFiArB5yezvYkSB1r2XJJRT7Y90A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=HR74prx_2FRyAeAu2-xieAb_tN4mhqAtLIcvCOWmI2ppfqcjD-75OnrIWkbfMY2evrZtbMaDuPkxoUhrcpi5ljDirjeVmBFbpO9HNoPZHqZqcC7VgsQjRDhqbxfijzX01XiAth-lOuLrgO3GXs44Ye8CyVSZqK019lfCA8urWrKy0pS1NoCTb7PYkGdjBBgQXXVa6a3GQm_nXG0LaZiD3uARAEc3BVM9rk9_R8-HKRGfq12WRzxQyEZVmOvAl6kPsUBPI9cRIjjEoCLhhHLJcLowA0aK0QZo3SXE3kphMIFWagZymwBj4L-lrBgIAgpKwWgocOfDpZHJ2eC1v4u54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=HR74prx_2FRyAeAu2-xieAb_tN4mhqAtLIcvCOWmI2ppfqcjD-75OnrIWkbfMY2evrZtbMaDuPkxoUhrcpi5ljDirjeVmBFbpO9HNoPZHqZqcC7VgsQjRDhqbxfijzX01XiAth-lOuLrgO3GXs44Ye8CyVSZqK019lfCA8urWrKy0pS1NoCTb7PYkGdjBBgQXXVa6a3GQm_nXG0LaZiD3uARAEc3BVM9rk9_R8-HKRGfq12WRzxQyEZVmOvAl6kPsUBPI9cRIjjEoCLhhHLJcLowA0aK0QZo3SXE3kphMIFWagZymwBj4L-lrBgIAgpKwWgocOfDpZHJ2eC1v4u54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWTCZxFElGdFB_9JbzcmzmsuFSTZWJL-xjl2B733UXj9D4B871ajc1oj-_gZDt0QsqHvY3wC7g52Z__hOhqSKqFSPHJlPIItpyurvBDpVNiOD7uMeIZDqPHnFQ_ntWvCw1FftqViV368FAyPEgnShKcszKMZTm6YCmWe0MHDqA7-T3Z7_PPDW9378BQyG-tSeuXbI0QeUnLH7TdoX8j6_ntv-ID1OmBbX25Gl428Y0UTZtpKh1pqdQQtEvO5QG0BexN7dqZ31fM_XrGfg_C8J9gMyWC9kGKuvVmawt5oo-8ton0JM-9LT-SZa49T5OjX89gneKY2tidn9cKRSILgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=P_YcKOiMaCWSDy-XsED98h15pxVNZ899CitM3IUEm85J_UBlkKBZMeRP6TBpoxbNy_1paKtRwenXQs0bM43J7qa88aFIFEowHCMdR_NWHZWeCn5NJx_hI9g88FXFTNmklFqTUWLHvfkVLScbgi9Ga70ZuHSf4xGSz8yM9j0gCpYGBimjNFX9iQ4KUufKzIDonhNgjbgpuTeVEr6c-ccddPjb4hz8zq7eV8pEymKzwiriemPimF9Vb9xo4TObbkonV4d-Oa0vsm4iXfRDOV81T2KONYHiXrT_jAkfMHAoaY9vkNIjHhOJbNyD02-eyYWz6fzf5db0hxZCeOa0YC2UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=P_YcKOiMaCWSDy-XsED98h15pxVNZ899CitM3IUEm85J_UBlkKBZMeRP6TBpoxbNy_1paKtRwenXQs0bM43J7qa88aFIFEowHCMdR_NWHZWeCn5NJx_hI9g88FXFTNmklFqTUWLHvfkVLScbgi9Ga70ZuHSf4xGSz8yM9j0gCpYGBimjNFX9iQ4KUufKzIDonhNgjbgpuTeVEr6c-ccddPjb4hz8zq7eV8pEymKzwiriemPimF9Vb9xo4TObbkonV4d-Oa0vsm4iXfRDOV81T2KONYHiXrT_jAkfMHAoaY9vkNIjHhOJbNyD02-eyYWz6fzf5db0hxZCeOa0YC2UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=P8-Psldszpe4L78R8t-N1JIwZVbIypDHu7KXt8F7c_yD9OTu5JJcZkf_1Z-nnPapHzIrqKv0IwaoTOQO2-6PWiD5w9naGGcaP_vC00Zb9aFYzhEyYjD297tCakUQoadtLaSJMa3DVmQP9A1xb6CBZ0Qr4CYxU-BeDCOFvQtBY18e3bHLKR9EcUBWNjRtZLmEL_HsNAxUS8GUagaG_dpMBHPLsPeCUpn1caONEuaJDoZUH7Q43nSKzCE57VUaI9VFGVfbPT9u7LTezl7ko5JEFGCh0IivqAi_xHR9WBNkqs4r7x-vTBmSFkHQk50zDruEU43bHe524zN6sAFaT8RVpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=P8-Psldszpe4L78R8t-N1JIwZVbIypDHu7KXt8F7c_yD9OTu5JJcZkf_1Z-nnPapHzIrqKv0IwaoTOQO2-6PWiD5w9naGGcaP_vC00Zb9aFYzhEyYjD297tCakUQoadtLaSJMa3DVmQP9A1xb6CBZ0Qr4CYxU-BeDCOFvQtBY18e3bHLKR9EcUBWNjRtZLmEL_HsNAxUS8GUagaG_dpMBHPLsPeCUpn1caONEuaJDoZUH7Q43nSKzCE57VUaI9VFGVfbPT9u7LTezl7ko5JEFGCh0IivqAi_xHR9WBNkqs4r7x-vTBmSFkHQk50zDruEU43bHe524zN6sAFaT8RVpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udJpwi2doQTvzDzL65lya5a3BextD9bQeduqDoSStqkUiG7WpufndSceQN0522P54xdrUNoXId4G4orIyLwt6UMgMc8UbEZid69pasxWV1CQlkGw-3maZaCTGS64EdtQgcFW1DIQPrBpu9tOYs71MOsHABj_8R0HKBVq5eR1GV0Z8AITh5tUAiLC-bsSDC01d0FGEp8_l9tBnQTU2FKh3cp9DYAPiDAH8b1frjJTk6UNSxyWpSOn9ukrSP4KNsB1RYSfhpa5tQOYMgPNlqqGbpddg7W2dIVerj_3Chjy1w7NqquR56TBoa1P_QowsA6G21iV7SytnQExf85WiMfV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKJHtCG6V7zfG-2FA2NmfrF7BYc1hILupQlA4J1P2SxAJbl_4PWBOcOM1YNArm0UnmwBJ89X-nznzjZVLyIS9eq7CbQPzONRh_AYAtYlTn-gK6LzCmFNqsG1LxwS7ReEJXgL_nMq-unFjNkK805gmJlBWfpKS8LXF8QXxCPQsVlcVUSUSq4ADvGfB9FWtKBbpRgbhIvbjsBbPfWTVSpCDXLoe3aObNbjr1Ao4uXlvvxiOTHrWReuTGJY53JvZMa5EbxI6EwW_z1_F5RHV5znohqAnawm1yDer-KLHY1M4KhyEu9rn_93jyeWbuF1JTjHwQ8BPkB-QicXuh-550trbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ndpLNvM9DKNHgo4jOubgB_CgAaaHLhuyuUlzoqjuwzj0BAHv6dmQuS3mW9FvbI9a2vNgne0yO68z1OIsp0-Lq686zq_WEPivuiDrk1PZj1ed5OpzKPAwcUUsFnthBuJUUXLnXNKOKwowGRYy5DejYyG_KvGJ40AFF0QYVT2nz9OhJS2BF9dX9Iv4EKs4XXjcYhN-JN4qbW80sRWduDMOH2cAOBHF6OLij1fAJea93Nx_96JxUZDzF5mH5Z4ahmVKtYfTPmsUeNsSjQyCeMGk-wEWTALsqUMiP2JHkxeivQut9PWfZtgrVj-wV6o6T6HwvxyobPC6QqZjtw98Fxl9JU_l5M96BiKVq_DjiakMxGg817DIwBfg1SaXEIZiifxrdMtHIq7N81VkI7oXzdmAXXkJI-VNUGl0k_88T2L-8ZU8PEZgzkM7fr2UrTc9caaUk0VySwepd0cceQohtX-cBpBWha9Nf4FNF6W8_Y5FRk86kdaYWwfHcRCWw8ZFNgTNgEJ4e3OcvG1o7QSXctCCKM7ya6ALjgyKzJ807fp3e_WW4xGS5XeJRcaOJMRKr8FkqS4yYU99FTHEzhOVfQcKcuCQW_ntYUNLq-eN-A9TAw3FbIO_K68qVnNK7ryjnAkP7EUfp9ffzrtkKoyN0XnKr8P9c5bz5ar5Age_-KcS3SM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ndpLNvM9DKNHgo4jOubgB_CgAaaHLhuyuUlzoqjuwzj0BAHv6dmQuS3mW9FvbI9a2vNgne0yO68z1OIsp0-Lq686zq_WEPivuiDrk1PZj1ed5OpzKPAwcUUsFnthBuJUUXLnXNKOKwowGRYy5DejYyG_KvGJ40AFF0QYVT2nz9OhJS2BF9dX9Iv4EKs4XXjcYhN-JN4qbW80sRWduDMOH2cAOBHF6OLij1fAJea93Nx_96JxUZDzF5mH5Z4ahmVKtYfTPmsUeNsSjQyCeMGk-wEWTALsqUMiP2JHkxeivQut9PWfZtgrVj-wV6o6T6HwvxyobPC6QqZjtw98Fxl9JU_l5M96BiKVq_DjiakMxGg817DIwBfg1SaXEIZiifxrdMtHIq7N81VkI7oXzdmAXXkJI-VNUGl0k_88T2L-8ZU8PEZgzkM7fr2UrTc9caaUk0VySwepd0cceQohtX-cBpBWha9Nf4FNF6W8_Y5FRk86kdaYWwfHcRCWw8ZFNgTNgEJ4e3OcvG1o7QSXctCCKM7ya6ALjgyKzJ807fp3e_WW4xGS5XeJRcaOJMRKr8FkqS4yYU99FTHEzhOVfQcKcuCQW_ntYUNLq-eN-A9TAw3FbIO_K68qVnNK7ryjnAkP7EUfp9ffzrtkKoyN0XnKr8P9c5bz5ar5Age_-KcS3SM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejkaMXQ4Ko7JN2SBNL-rccSEugzpzoW_OYG5ADk5RinrjKTWNlkVVyzBqIJ_A4q3DFXnezF1GCyugaGYor0Ui7jCdOoWei7LF--cmu_14jl5rLR06Z9U4F8e996iG9PiFJ3Aaf4nFrHTFDyUnaNXv3MeFAO54-83mrDLLk8mOm65Ws9gTovwqaR2UyxPEfivE0RvQQttvbDtiTXUA-c4jZiHgh0SxDC0MQd3KKk7JU9jikjQbElHIoBRdMNxrCk2lfI8_JK7uWqcpzunO1JiN0E3_92ULfYgPdShm5fXnxafUbCwA-UAVGsRW3L-cng1tI5Jqx9HRygZ4yNmjHZOVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=QpFaLp39WsQNwaNe_uElqHi71ynNq3F4m3cFG7zpadrK71LeIc7PWY9sDYR8qp8uIrCxTzXqkGE269GsefTn9k2hqGsbTuwETWr2fRC3VtO7Dq2aGl6qHOoSykCDhein1roDklT9qVp_SjbUSQMZH7nVp7EgmnUj7VfCxr52QBwftXbHD5B45CXtNFzKDP-uWfKNR_cDRW_OWQfan2D_78IdyE8lgE5SFqec6aTICn5ZOsRSZJrvgncEn3F6eBbCOxcuUeLLgVEod2DIc3qQw9ESnmKtDoWEnHihN38D9HO6qFScOfIfGPA0JDAoz27IQrV-YvkjHb8aypodxm0_TAIBgt4aYOQ-UCi4wCZ9RzKdRKyggRWzpfOgzDcbVsRnK6BcmpGbmubJFCpkiWRQxwGjad0QTOKesKcEG8zHSTHyrEyfFJVg-FFjU8K-YyBu3Tj7X-Aui7EqSf-i_qKMVntKLmzn-FfjOwzR-I1KoXSFKMinsOr7WUnbbQfmr2E-YTOqQ8LMDF3q7tC6fVJ3BvIJnetUmtsj-dWSHltqRT7HyapNP22MuMBC0NoctJIgrkqnCu2oj4VwpXxNTMVabWJT4o-llQTv57zz9DHlIZr6JKhjw1PRQ4GGKVjjvrjegQ4bi7YAxUDIr-L5QUE03kXydX2E8h7uidq0mCXCyxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=QpFaLp39WsQNwaNe_uElqHi71ynNq3F4m3cFG7zpadrK71LeIc7PWY9sDYR8qp8uIrCxTzXqkGE269GsefTn9k2hqGsbTuwETWr2fRC3VtO7Dq2aGl6qHOoSykCDhein1roDklT9qVp_SjbUSQMZH7nVp7EgmnUj7VfCxr52QBwftXbHD5B45CXtNFzKDP-uWfKNR_cDRW_OWQfan2D_78IdyE8lgE5SFqec6aTICn5ZOsRSZJrvgncEn3F6eBbCOxcuUeLLgVEod2DIc3qQw9ESnmKtDoWEnHihN38D9HO6qFScOfIfGPA0JDAoz27IQrV-YvkjHb8aypodxm0_TAIBgt4aYOQ-UCi4wCZ9RzKdRKyggRWzpfOgzDcbVsRnK6BcmpGbmubJFCpkiWRQxwGjad0QTOKesKcEG8zHSTHyrEyfFJVg-FFjU8K-YyBu3Tj7X-Aui7EqSf-i_qKMVntKLmzn-FfjOwzR-I1KoXSFKMinsOr7WUnbbQfmr2E-YTOqQ8LMDF3q7tC6fVJ3BvIJnetUmtsj-dWSHltqRT7HyapNP22MuMBC0NoctJIgrkqnCu2oj4VwpXxNTMVabWJT4o-llQTv57zz9DHlIZr6JKhjw1PRQ4GGKVjjvrjegQ4bi7YAxUDIr-L5QUE03kXydX2E8h7uidq0mCXCyxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMhQ5TXpgo_wskH2j68rJPS6EX5xbcFDAwVOTune8G77i7_ZEEMcoJGy8ZrS-dPjldrL-SXzEBCn3nZuMqr0KQY2SnLFvxBn2OjAyQGXUK8XaRMPROhOr6MNYEtjoMN1xbj-GkJOqcT97uW7Uk4zRooRr9dwfnBwuFv_GFrsPao4QCtRL0KDhAJFnVmDgrqsLAptovoIfCvLmBOXC7QOdCgCURur0QiSv-y3IcFDW721rpVtQQCoWvi6a_dd1Kgz3oi3UhwokwSehFPsPorGKaeZI1lZVJZGRKiXwSxbhqb6s2vBdqyrLfT5flyCzy7YaFyLoOGfnpAxnHUmV0zHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_MWRkMT5xZHj0ROd052qB5-BHKcm2Q_lgA3ucVtpFNDAHqcNKDILFvfH10yDzB7CSP5rHl5SwYgZpaPTsW6TuIekbQ6IWPPtyxJZwJ1tXRUlEU_2nodFIADBHvP_Dra-wYC2XSvfuAy9YrRRZk8IEUczjD1Ic4_rIh4tbYFQFasL2YAXvl6jmOUQjEPkmiSUvQqbIdD7rGys_anO55IF1jnqDdst0qiezBwmsMUqEWcsMFjwZ13jtCmJ6sgx3QnGMvsE3NIJ6buk5zcV5-UE2tQk9IW0wdzxC4tz4XECejtPzN3EvMZL7Vf2LP5Wl6J7gEEVf6TvXSKviQLTKUJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz1dKree8w8Ok2eXWGZiDf7lRfcq-WUJEzjqgGYD-1dCo3ANwU5EyVxAUZZdgQjVaOXxAsOFewY0L_Drv5m6f7YnmVZh2SDfowydY3qSJOZQyfRNQmYn25QDxKOogWf_v7noJinuzmRRmFrTyxWHZnCvHwUeoPeGJcOnBKMSWtrJ--RReJ_8OJTvkuEKcAa0uY4dUq3An7-LOtIwT5_XZWgxQsUlKH7hN43ZjbBn2trXLf3Rnj8-uh2XNCSx8FjIhZIEInHCMWrJHbqSG9DHpS4W9FJU5zwC5n-mW6J7G9Tfkk7ShWazUIccui0r7CNvi8uBQDCNUL2H06r5uuZ3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
