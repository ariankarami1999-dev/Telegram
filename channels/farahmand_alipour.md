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
<img src="https://cdn4.telesco.pe/file/UHPl2Pzps7c7roELAhMrygRmK4TU06RACKTaQHxelLCG-gdFdzNq5XzDdyKyc7BPEhmU1dub7bS4fBZQqIrMmQHkLDT6LKL8TriqyrfALHkZW8dtXOcpSFJdsXeE8TW86BPWn8RiG8aFQSjB5WibhmRdOQ3lRtji2wELsw5NyoX-lV3a8QzuVCLme2qYL_CQP7p8PBulVrP2WTlvDJI1WkOtHbzirsV3fYvFBL_Cwq5Y4hKn26adF02ZTomqsOb3nxlYK_lU_VLvWR89nisWk8-KbxOxEj3NJknCIePbXRc7E9r2ssMGNib-jllRJ9o4yXhBW-JZLwOpYJSNaC9a0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 23:00:44</div>
<hr>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O_P8FgYAWG_ZGb4OV0jTGyO9mi_-EgVs9H0vFYMHam4dkX5d18lRjpGvMqQcuYK26R0i34BOkmWaZhx4tFKNu09me43hHhGTITALR2e1RZ9KGAAlz29AryzVKmB0hxTTxQ3rUia7Bg9T6IQ0Dk6KePIvq7FwgAaYxz6JYmZehuoXRmITyEx-Ntkd92ubPZuuKKmt_dCblKWdchIQ1GtW5jajfeeZqlj-sexx3twu-xONLm8CJRcHrj783XuquPOVD77uTEhO4LUpvyOlcqiPdJBbOVVkjxlkJW5ZbjrjFBlfL6nTyozUClCzMzX34nH8Bs_0GTFG8I5a-way_vim0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O_P8FgYAWG_ZGb4OV0jTGyO9mi_-EgVs9H0vFYMHam4dkX5d18lRjpGvMqQcuYK26R0i34BOkmWaZhx4tFKNu09me43hHhGTITALR2e1RZ9KGAAlz29AryzVKmB0hxTTxQ3rUia7Bg9T6IQ0Dk6KePIvq7FwgAaYxz6JYmZehuoXRmITyEx-Ntkd92ubPZuuKKmt_dCblKWdchIQ1GtW5jajfeeZqlj-sexx3twu-xONLm8CJRcHrj783XuquPOVD77uTEhO4LUpvyOlcqiPdJBbOVVkjxlkJW5ZbjrjFBlfL6nTyozUClCzMzX34nH8Bs_0GTFG8I5a-way_vim0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=G-Nx71w-SIhYKCRIVaz_jLz4ywzplB2DtDEZdRsFm8qD2mc_vlCMVgsLBhjbSHSXL8hBBvyAJJutcdbBHFp3h1un-cVyBeNDFrEbSJu1wUG1MZsz7a4bMujzWfuxWNte-o_ihVwNJNC9ORk9zBZwcrA2ewmIOhOBOIsthJc2R4I8ps7pJt0qFW7zUrKgfhAls71xLvpGfmZ9a15CZnCKETmEzrhK3HrSLhAkjZT-u3od398PseBfiuWHRHtr-46pNnD30xxrvDSThAe8njCpiA-2G5z4gFgHbHtSZLvAZXho3iH6yfEUgLHJ_H3ZsP2nDma2oNYr2tpiqWXxa_H872blfyF7kAuqPQRqIl4S4kMVjf0j12sSg6yedQxnBf4p6d33JA1b50BQMIu6QuW5AmbL1Vebgn50lqn_h8GJI54r0a7B7FfX3w2yfaNyqizECeZmP_AjcY5e671lzrZDUcWDS-JaAcj3doyfywpNGbyTSh7SV0JuXLoOltX06st2STxqGnIgVBwWXgtIle0chJZjSchplG53NWbzaIrks-V0eG6IhkbmuzuAELh8gzGFC_D3DIlycS4ZcgZqeLTDZMgUGL2sS-3y3qXFZRwtX8XQR7HeCCYNw1tHP-djU0GZdUonkjrV42le_2CE2kGRkH6hsxpM87-Air8ACjojZr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=G-Nx71w-SIhYKCRIVaz_jLz4ywzplB2DtDEZdRsFm8qD2mc_vlCMVgsLBhjbSHSXL8hBBvyAJJutcdbBHFp3h1un-cVyBeNDFrEbSJu1wUG1MZsz7a4bMujzWfuxWNte-o_ihVwNJNC9ORk9zBZwcrA2ewmIOhOBOIsthJc2R4I8ps7pJt0qFW7zUrKgfhAls71xLvpGfmZ9a15CZnCKETmEzrhK3HrSLhAkjZT-u3od398PseBfiuWHRHtr-46pNnD30xxrvDSThAe8njCpiA-2G5z4gFgHbHtSZLvAZXho3iH6yfEUgLHJ_H3ZsP2nDma2oNYr2tpiqWXxa_H872blfyF7kAuqPQRqIl4S4kMVjf0j12sSg6yedQxnBf4p6d33JA1b50BQMIu6QuW5AmbL1Vebgn50lqn_h8GJI54r0a7B7FfX3w2yfaNyqizECeZmP_AjcY5e671lzrZDUcWDS-JaAcj3doyfywpNGbyTSh7SV0JuXLoOltX06st2STxqGnIgVBwWXgtIle0chJZjSchplG53NWbzaIrks-V0eG6IhkbmuzuAELh8gzGFC_D3DIlycS4ZcgZqeLTDZMgUGL2sS-3y3qXFZRwtX8XQR7HeCCYNw1tHP-djU0GZdUonkjrV42le_2CE2kGRkH6hsxpM87-Air8ACjojZr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=UwVFFRoPaI-sUCE8a2FZpjJQtfm_yK6iJlHAA0tusOnM8-Tl3vEGsHdMx9l9m_J-HbpAQPnz2rqWS7e2mQPkwagm1Kw0A3QuU6_9xhtq6aagGeWLk_xHIjaOq0TSszYaUtchZJzEvbF4gKF7LB6HSMr1F_Ui0xKXqlgQEvaO_gFBAlYo3E0AS5-_9t7Cs_r0aVNouwDebN7LzyzuN8t76Se2Fyit7BORB0-v6cgQvi6duVte7LAiTPrtnqEajsSDkz2_4nTnwSIkfBcyh_hOAskRTgBwfJErac6n2aNBzO2O1kMpYGyrubxEdamQ95jkQgnH4h4C9-Gv6fKqhrMyvo4GKhvJO034l2UlkLzUs9PPnJqGKGlkvvjaOpn72RqIqlGDSfMTb7r0R8EkLhJ-Jgymty5jNeOJKIvger0YsTR6h__GDadafLr6NZma9PSzXiOv_rl6rsZyc32m2uQZWhKZ6f2KUWiIWBRl5bTI6QEn9Q3Eaq67jbvaPqkPzF7abZUtAy4wUqiT7JSL9Y11smPNMIWpwZ-6K9LmEbCgVTVJT3psRdlx6qU07SspF3GMH0zxHRxodJpfK32l0F_330BaZZ_7HMwhx3PvC1pLWFLlO0iBxN742POitn1iwG62iAQ68oOnwfp_VV_BHLSFVszmnNSbNBmneEv4uVh_gVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=UwVFFRoPaI-sUCE8a2FZpjJQtfm_yK6iJlHAA0tusOnM8-Tl3vEGsHdMx9l9m_J-HbpAQPnz2rqWS7e2mQPkwagm1Kw0A3QuU6_9xhtq6aagGeWLk_xHIjaOq0TSszYaUtchZJzEvbF4gKF7LB6HSMr1F_Ui0xKXqlgQEvaO_gFBAlYo3E0AS5-_9t7Cs_r0aVNouwDebN7LzyzuN8t76Se2Fyit7BORB0-v6cgQvi6duVte7LAiTPrtnqEajsSDkz2_4nTnwSIkfBcyh_hOAskRTgBwfJErac6n2aNBzO2O1kMpYGyrubxEdamQ95jkQgnH4h4C9-Gv6fKqhrMyvo4GKhvJO034l2UlkLzUs9PPnJqGKGlkvvjaOpn72RqIqlGDSfMTb7r0R8EkLhJ-Jgymty5jNeOJKIvger0YsTR6h__GDadafLr6NZma9PSzXiOv_rl6rsZyc32m2uQZWhKZ6f2KUWiIWBRl5bTI6QEn9Q3Eaq67jbvaPqkPzF7abZUtAy4wUqiT7JSL9Y11smPNMIWpwZ-6K9LmEbCgVTVJT3psRdlx6qU07SspF3GMH0zxHRxodJpfK32l0F_330BaZZ_7HMwhx3PvC1pLWFLlO0iBxN742POitn1iwG62iAQ68oOnwfp_VV_BHLSFVszmnNSbNBmneEv4uVh_gVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=N1yI_mjZs3V91ytcBlN0NM7tyhArW8fulE4fgdq3uKz4lTneOxP6YUc7YkGf9BJ5p82GMQyOFoN2g8aT1-eQhu_1HbdF431SenHCfqQxmapWOvlmXLNoYmLYmzjNq1ow1RdS4vLMX4BuCeLy5F9gzuaG7w-XkhCTI_luvw2NA4kIdrfOwzuORNZV-Mfgqw8fyAVCH5C9xiOBayMUbFULXrlzRdfkWQGk2qJcm8owTxU63eFsjRtLc_QPI-oKp0g0DpX847h8Ah8yAqEQS5hpojnFaK3BSekpLgVfZcYRB5_tYQLm0fTqxHdMVLQcraSJxqDFv9PGbe6DDmMEAl-bhCQVGpQpD22UBd42FOQEgsIiCschlzxw9F30F75kI21Up9HuyxhjAGRX4UJ8VxHb0uaSqYyevg8kTEL09eOe4OT35-KnXP1-DggOeB03Kb7UAS3WFHlrCqRCcURUj-dehjvF6Gr2J1tqiWjawG3g1AiDwvJKlI9ngbNSNjAYX0iVjZ7_AoTLR-w6UEIVLWaChOHo3l359iqBeBBqPhIq5r6OiM_XyatRVdH7aMYHS__GhpE55gleFSX_CjoYuLmy6-_XeUWB4Va8Zmt7JCADeBq9uLP4ibnhTk0rzhE4rxqyzzWc1dwZDEAE3wUZvWf270tJZCgwro3IHdv8iEVb1tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=N1yI_mjZs3V91ytcBlN0NM7tyhArW8fulE4fgdq3uKz4lTneOxP6YUc7YkGf9BJ5p82GMQyOFoN2g8aT1-eQhu_1HbdF431SenHCfqQxmapWOvlmXLNoYmLYmzjNq1ow1RdS4vLMX4BuCeLy5F9gzuaG7w-XkhCTI_luvw2NA4kIdrfOwzuORNZV-Mfgqw8fyAVCH5C9xiOBayMUbFULXrlzRdfkWQGk2qJcm8owTxU63eFsjRtLc_QPI-oKp0g0DpX847h8Ah8yAqEQS5hpojnFaK3BSekpLgVfZcYRB5_tYQLm0fTqxHdMVLQcraSJxqDFv9PGbe6DDmMEAl-bhCQVGpQpD22UBd42FOQEgsIiCschlzxw9F30F75kI21Up9HuyxhjAGRX4UJ8VxHb0uaSqYyevg8kTEL09eOe4OT35-KnXP1-DggOeB03Kb7UAS3WFHlrCqRCcURUj-dehjvF6Gr2J1tqiWjawG3g1AiDwvJKlI9ngbNSNjAYX0iVjZ7_AoTLR-w6UEIVLWaChOHo3l359iqBeBBqPhIq5r6OiM_XyatRVdH7aMYHS__GhpE55gleFSX_CjoYuLmy6-_XeUWB4Va8Zmt7JCADeBq9uLP4ibnhTk0rzhE4rxqyzzWc1dwZDEAE3wUZvWf270tJZCgwro3IHdv8iEVb1tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=YM-UQsKGGwPksj7VgmFPT4sbskYooj_3FufmY61YIpcwVsh5aqz44kzVxbyYZGE2dTmxBgWxmz2ew3I6Gn_6qmYsUnkhTfD4QjyM1sUkX5dJ7zlMfQdp7vZDkIudOLYVM2-Hy_rKBpx1PtnozleYyTP9hEhlj6RXySMz3CKaEbZQvOKsQSc8Kho4oFaR34ISwcE2bWad4Seki4YgOA8FP-1FnjsnYyozBUEhAVfiXa0GfCvDI_wRFjmRD8xL_-HWpqjwzIKhXUawZhrlNXA_B4blXISZM-iWdTfzVX2odubAeN3KPDrrnW1QyrbtDvSv6K_JAeXvr5Q2-rPhZ_EVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=YM-UQsKGGwPksj7VgmFPT4sbskYooj_3FufmY61YIpcwVsh5aqz44kzVxbyYZGE2dTmxBgWxmz2ew3I6Gn_6qmYsUnkhTfD4QjyM1sUkX5dJ7zlMfQdp7vZDkIudOLYVM2-Hy_rKBpx1PtnozleYyTP9hEhlj6RXySMz3CKaEbZQvOKsQSc8Kho4oFaR34ISwcE2bWad4Seki4YgOA8FP-1FnjsnYyozBUEhAVfiXa0GfCvDI_wRFjmRD8xL_-HWpqjwzIKhXUawZhrlNXA_B4blXISZM-iWdTfzVX2odubAeN3KPDrrnW1QyrbtDvSv6K_JAeXvr5Q2-rPhZ_EVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=YjSg62da7QU4wFqGmJwu6oea8h8yUqMVh2C4dIbbMzpSlsKpmNDAj3COcdvumzczFVPLPLF02jyIGWNd1SDmVLEGDgWwoDesp9nNpOgtSMjpKTcQpmaLL6myzaaVvrV_pxDyqvH8_Fwb239-VNlVblXKCsP-8yGIW7gTkkSfQsrWBhnlhoyvRmJX5g-I-9OKB_J0jpgVTlNKmer7WE5ae1D49GDeT7Bx8yhXykX61GtvsLNCv5ltUtq3MVoJ--jYUvVYZgoIoO1AsS2ZNQOjFRgCpIElMEmgdXQ1oecK7Z4nLGb9QX4fIngUecZYfczPEg-gj5wyWttL299qxnsL3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=YjSg62da7QU4wFqGmJwu6oea8h8yUqMVh2C4dIbbMzpSlsKpmNDAj3COcdvumzczFVPLPLF02jyIGWNd1SDmVLEGDgWwoDesp9nNpOgtSMjpKTcQpmaLL6myzaaVvrV_pxDyqvH8_Fwb239-VNlVblXKCsP-8yGIW7gTkkSfQsrWBhnlhoyvRmJX5g-I-9OKB_J0jpgVTlNKmer7WE5ae1D49GDeT7Bx8yhXykX61GtvsLNCv5ltUtq3MVoJ--jYUvVYZgoIoO1AsS2ZNQOjFRgCpIElMEmgdXQ1oecK7Z4nLGb9QX4fIngUecZYfczPEg-gj5wyWttL299qxnsL3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=WfrE9CNhraif-J-FjHSnJ0Y-4-izn7su4RCSveNNtXOIcYPnt4g4KmhVIEpC1rwiHtdLE6eg2g6_MUbSeZ29fo7Ve0HsdNgizIMX-UzKEZDe8axSEXQeYa3-RxuBC0JNuFeOv9yME6NA7ym-XWYrhlZxOENZYXC0huOJyuHn1Yq3y_i1lpC3FnPAm4pV9Mef52cK3uWspj0Djj9lZ2QaHuVtpt5fIs7yfXt9DxlZRO0474s_hFCQChxlBYaJd2SvZ3ie2dwUr4q9oC397iQ8v57IPClFlguKa3sx7Oq1taLnLALr3l7NRGyghTJrZAGWfzDELOWjveGk4QgLsdGFiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=WfrE9CNhraif-J-FjHSnJ0Y-4-izn7su4RCSveNNtXOIcYPnt4g4KmhVIEpC1rwiHtdLE6eg2g6_MUbSeZ29fo7Ve0HsdNgizIMX-UzKEZDe8axSEXQeYa3-RxuBC0JNuFeOv9yME6NA7ym-XWYrhlZxOENZYXC0huOJyuHn1Yq3y_i1lpC3FnPAm4pV9Mef52cK3uWspj0Djj9lZ2QaHuVtpt5fIs7yfXt9DxlZRO0474s_hFCQChxlBYaJd2SvZ3ie2dwUr4q9oC397iQ8v57IPClFlguKa3sx7Oq1taLnLALr3l7NRGyghTJrZAGWfzDELOWjveGk4QgLsdGFiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=iPYrBE3IEnMrnwdRR1MloqIbYIW_kHxjEyBKdywp0qIjErUOlvHx8E5HcfM9UwyKQj61WtuGcYDYqfvTvGFqR2Ti_gGhoDhFQ1ZENkKf6X9TdeC_KPweZvNDgHCujPHp6hJ_iYj1oHPyRR4dRK_xsNFMX2Rx6P6UEMDUlLmjzq05dWpGkocMrpnoltDRKkFt3uBgLv-drffIjAMUS-1BHr-wF3ousj0jhpP1TmLqC9N6NmRBdt60Hf0nIcWB-k8g5o24KkrZii_dm0zl58a7oMAgi2i-QfOudxVcTmwuZX3UOG1eHfh93gANvRKdspoqua9U8GXIGDfTI7swnLxLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=iPYrBE3IEnMrnwdRR1MloqIbYIW_kHxjEyBKdywp0qIjErUOlvHx8E5HcfM9UwyKQj61WtuGcYDYqfvTvGFqR2Ti_gGhoDhFQ1ZENkKf6X9TdeC_KPweZvNDgHCujPHp6hJ_iYj1oHPyRR4dRK_xsNFMX2Rx6P6UEMDUlLmjzq05dWpGkocMrpnoltDRKkFt3uBgLv-drffIjAMUS-1BHr-wF3ousj0jhpP1TmLqC9N6NmRBdt60Hf0nIcWB-k8g5o24KkrZii_dm0zl58a7oMAgi2i-QfOudxVcTmwuZX3UOG1eHfh93gANvRKdspoqua9U8GXIGDfTI7swnLxLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Zb9MzQKF-U4RnHfiFDOIy7qVrvAaEJ3wEB1XlC_KviHjPXANmo4mDKl1noX79JE49yrM2yt9ugZBo2m8B4sF7fzCoD8WnbUaIEj2Vybo4_kkYPeriCVRgdK8g5uAyKOfosvLj8uXFktACDAWC3zkjOwPKdZ1CFEPVjiPuGzzoWqVDz6gaTbuIMXBXo56LAmuazhibbhZkT5yJ55dMHJZmeuVSB9l1Q3Psc2iqnHfXU__6zUW0b8jYrJ3IVp34xKzTOjP9KIusU7onMFcsOqR2x7sjvivZAORU7W_kS9ecNAk-BgghpCwQeXpxdit0rkyGjU3WpqHa-hZl_9ResLhIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Zb9MzQKF-U4RnHfiFDOIy7qVrvAaEJ3wEB1XlC_KviHjPXANmo4mDKl1noX79JE49yrM2yt9ugZBo2m8B4sF7fzCoD8WnbUaIEj2Vybo4_kkYPeriCVRgdK8g5uAyKOfosvLj8uXFktACDAWC3zkjOwPKdZ1CFEPVjiPuGzzoWqVDz6gaTbuIMXBXo56LAmuazhibbhZkT5yJ55dMHJZmeuVSB9l1Q3Psc2iqnHfXU__6zUW0b8jYrJ3IVp34xKzTOjP9KIusU7onMFcsOqR2x7sjvivZAORU7W_kS9ecNAk-BgghpCwQeXpxdit0rkyGjU3WpqHa-hZl_9ResLhIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l95tdnU3Ab3vJA_JeekoYZvgE7YKsTBbrkB2uY-yyFyOVJXpmf9aCu_JJcgnFj84Rpc5yVZqBJyhMCEbRuPHTRRSpktZvPuKR0vXcm-qgmedzdnyLdS6hIH6HFxyhg4QC6KGMhTYv1fWRQqWqPh1eM5wTVnMkSp43xWl76EEw91Zun0mkX3MFSc3BTlw7tZuWVabRzF-wNTcC5JD3kQrCdy_v2LGtlfIj9pxWdorp_dO6Rv4t-ooWUIPJXppB6zuTtFgFGdadDGatXHskrqgpr8ZnXEINZZHvZy0rN_J9Zlt73m50i_6uTcdX4OKqPSbUssX_tjldJkMkl_SpW-NAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l95tdnU3Ab3vJA_JeekoYZvgE7YKsTBbrkB2uY-yyFyOVJXpmf9aCu_JJcgnFj84Rpc5yVZqBJyhMCEbRuPHTRRSpktZvPuKR0vXcm-qgmedzdnyLdS6hIH6HFxyhg4QC6KGMhTYv1fWRQqWqPh1eM5wTVnMkSp43xWl76EEw91Zun0mkX3MFSc3BTlw7tZuWVabRzF-wNTcC5JD3kQrCdy_v2LGtlfIj9pxWdorp_dO6Rv4t-ooWUIPJXppB6zuTtFgFGdadDGatXHskrqgpr8ZnXEINZZHvZy0rN_J9Zlt73m50i_6uTcdX4OKqPSbUssX_tjldJkMkl_SpW-NAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=e4zxNQduaJxXq9QRz55tLwMkhOYollYxKFasRLlfPvMdhNRnsb_WfcIHIz45iGpDt_eFo47gW_PRfqeQnrSIaO8KJFDFLdRGdk7D9G8UykbZSYsLH7ewl1MNd7jYQVQNdBy7ZB07N87PlAVxjFZsBE6CSJnv5dO0L2TLR3f9u74QU-tiLeqc7S_h5JLOlG-6qIadHFaffhOItBCqH2uDlvUBZek5ON0bKqMARnEF8YuHxH4SkdmMizzsRmC-5emc6X42XdbCFJooOEfNDslHeP2GHWh64wriNVZQBTs9yEmfX29R1ZCgLzfI4RPiGOj5oPPIbuNMgrVblaqP-ezmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=e4zxNQduaJxXq9QRz55tLwMkhOYollYxKFasRLlfPvMdhNRnsb_WfcIHIz45iGpDt_eFo47gW_PRfqeQnrSIaO8KJFDFLdRGdk7D9G8UykbZSYsLH7ewl1MNd7jYQVQNdBy7ZB07N87PlAVxjFZsBE6CSJnv5dO0L2TLR3f9u74QU-tiLeqc7S_h5JLOlG-6qIadHFaffhOItBCqH2uDlvUBZek5ON0bKqMARnEF8YuHxH4SkdmMizzsRmC-5emc6X42XdbCFJooOEfNDslHeP2GHWh64wriNVZQBTs9yEmfX29R1ZCgLzfI4RPiGOj5oPPIbuNMgrVblaqP-ezmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=hooWfh5wIFNQpNfSkOmqx9QJb-eAZNwW3-jcJnO_WYc-u0FGNjMU41qXPQNVxqr8TSHY7skti2rWm6iYOLcBR2g54-bSYBvog89vSJLQUm_wx1vMkIAyG_ry_KqI0RW43upYR-HJc-LGle-SVRVgHjz1-biITwCVAVQ9eSP4R7AL_p3lY0sRPe3Jfx23FB26FBXygs5j8SeM-RFh_Bm3ANn627GccVsrpbCuAhXDm6N3S3lPon9CxzXkM3hxlNRGKliQzYJvUqFKO67081ZXGSeoBKmF--SU-Q1_bp2SsbRtaPerzQdkaUE2CSUbJi8QxC7pUbP1eIj0V4-BLtoReA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=hooWfh5wIFNQpNfSkOmqx9QJb-eAZNwW3-jcJnO_WYc-u0FGNjMU41qXPQNVxqr8TSHY7skti2rWm6iYOLcBR2g54-bSYBvog89vSJLQUm_wx1vMkIAyG_ry_KqI0RW43upYR-HJc-LGle-SVRVgHjz1-biITwCVAVQ9eSP4R7AL_p3lY0sRPe3Jfx23FB26FBXygs5j8SeM-RFh_Bm3ANn627GccVsrpbCuAhXDm6N3S3lPon9CxzXkM3hxlNRGKliQzYJvUqFKO67081ZXGSeoBKmF--SU-Q1_bp2SsbRtaPerzQdkaUE2CSUbJi8QxC7pUbP1eIj0V4-BLtoReA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dJ0rXeK4nxB30Kjl580PP5XntgPAE4GXYmBA5kk96OZS4jS8F4b_X_brN0EsLcOM9Lnc4Wlz5M_Qt8qSjbc6nM3iGHLrM5ouUwYbd-d6AalZciN_NddyK6tjkYClMm2LHU89prcGC30YvTkrLy9hGDm-iusJOgJzgSc7QXSC5M236IhAcXBVrIuHNWLzdL8dAVzyx2XTOWRIZ-_GnLMI_e6FoyInFSwEJDR1nwwGeZ95pgbGPd0NyvtmuZXP2n6I2L65S5I-5AHTk-ihS26a23PYXyHWFdq3ZMLWo4gr_JoMhkMP61qwJcamjttdrnkJSwCS0XklRk-7Wlkxt9T_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dJ0rXeK4nxB30Kjl580PP5XntgPAE4GXYmBA5kk96OZS4jS8F4b_X_brN0EsLcOM9Lnc4Wlz5M_Qt8qSjbc6nM3iGHLrM5ouUwYbd-d6AalZciN_NddyK6tjkYClMm2LHU89prcGC30YvTkrLy9hGDm-iusJOgJzgSc7QXSC5M236IhAcXBVrIuHNWLzdL8dAVzyx2XTOWRIZ-_GnLMI_e6FoyInFSwEJDR1nwwGeZ95pgbGPd0NyvtmuZXP2n6I2L65S5I-5AHTk-ihS26a23PYXyHWFdq3ZMLWo4gr_JoMhkMP61qwJcamjttdrnkJSwCS0XklRk-7Wlkxt9T_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3fwfUXPsFv082cqWDL3QuH44Qnv71HlMUfZdiuS3GRiOaXmbInUDb9XrgOoBfEi5djnmt3IkcEmVQwP_1qGDtOqVjzqI0U7NKR5_qDhkfgdeV-cXsyMFMPbi6XBiciShxRguOXs28i-zJA1dopb5JChecA3wobeGFOXZGnlD2x3_FmYOgi3bpwYIdZk8yPQTIJDUAFn3V21OsboEDmB_kdFlHqLzE4ZC1cR629KAPzl8DsaWSzo9-c5JJVeEKmjjWOg9KHsBJw9937b7pNr16NE3CfvLJzB4gX4I17S4FXmMcCp9JC0YliJCrZ9Fi538nWR-6bs_V54SVR0P0swIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=S6Za3HOP5VWhkSB8Rz3yx4NEMW84KP-BoQ9IrdGwd7GRjW4F-2iakPQoVojLnBoLV173Rf1OmFndFsoct_3RSqGsIDwwv25FqXfwvE3F6DOS-Bp9qu7DDeCPkIo_1m6YaYpWgzxSkras1cztJjR5PV8gOcUOHyUee8g3hGUIX-vYnqtmgzB3ov4L5A6rYOSdrCv0vk-bHPXvLC2VjqbNz5_ISOlbqROq1oBWAlBMoZ1rDQnQkS6CKdmqN3-QmAbsG7pWHZQdqMB5WYMrLFnpC-QjUzK0gPUHeiA_XtVo3OxBncWhJuUD3I4y8drwSZlM6_g_cbi63F7HU8sXOi8SUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=S6Za3HOP5VWhkSB8Rz3yx4NEMW84KP-BoQ9IrdGwd7GRjW4F-2iakPQoVojLnBoLV173Rf1OmFndFsoct_3RSqGsIDwwv25FqXfwvE3F6DOS-Bp9qu7DDeCPkIo_1m6YaYpWgzxSkras1cztJjR5PV8gOcUOHyUee8g3hGUIX-vYnqtmgzB3ov4L5A6rYOSdrCv0vk-bHPXvLC2VjqbNz5_ISOlbqROq1oBWAlBMoZ1rDQnQkS6CKdmqN3-QmAbsG7pWHZQdqMB5WYMrLFnpC-QjUzK0gPUHeiA_XtVo3OxBncWhJuUD3I4y8drwSZlM6_g_cbi63F7HU8sXOi8SUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sLJ2lwvZlVE-xC1_Yk0kZ5CMxdk9BFHV4FG-UGwBOHm1K34vIdsAE0bAF4eRwHiBTLILcYBkrNwUxFq1iOpf1RvfJwq6E-KgH8U4VBAOjIPrtWawarOkHS2ajeXFvHi4BfihCFeUshdXt0vubUela8-PJLgciC7bzb5nBrV6ts1pJxLqKftEmu8HWzSlEpoXGloaR_Ooa08iB74gcEdwh6NwVxhICDCgtCtE_LcYVXCFMiNjELCG51ZMuluTAbDd48PCgREygsZR8Av8tROLF26f9Hs2CZPWOGb8XwxfPVbJuMU7u9ixfgEC66tt_V1IS9XOgneZLHizYoGPsXn0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=sLJ2lwvZlVE-xC1_Yk0kZ5CMxdk9BFHV4FG-UGwBOHm1K34vIdsAE0bAF4eRwHiBTLILcYBkrNwUxFq1iOpf1RvfJwq6E-KgH8U4VBAOjIPrtWawarOkHS2ajeXFvHi4BfihCFeUshdXt0vubUela8-PJLgciC7bzb5nBrV6ts1pJxLqKftEmu8HWzSlEpoXGloaR_Ooa08iB74gcEdwh6NwVxhICDCgtCtE_LcYVXCFMiNjELCG51ZMuluTAbDd48PCgREygsZR8Av8tROLF26f9Hs2CZPWOGb8XwxfPVbJuMU7u9ixfgEC66tt_V1IS9XOgneZLHizYoGPsXn0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqbKvAuZW8u0iMox6YKQ-TdsWREd1HddZBdu6N-8Wqbb6agUJ1PwOtXig_2pT2Pz2eTEll-faXzRV5kjJUu6bkPxTg3FUTU74tEm1NkVTduJBr08UM1NbI61_Vyr5cXFhnhalSF6q_G_1EJ2wlamho_tnsYQt2cHCLKejHIft7fem63jsUQwtv2jLZihXKiP_qw6PdUrnd8rk4yGkHT-PcMy8leXk4j6lRMxSymK_XttkxRo394UQG-eiKYf9awNFJiQ-0NxWYbojoGSw_Oz9XfxBgOrPxSYuruNQB6R4vnBN_js-P7W-7RTd_qlR_-FiAbAyE6nsoyyg87EHcvx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t27PatjRYgNjmD-RaTX4N6pcQMAfAswjQ_Y1TgCGi_Tjc3SCDi9vD-LQpkGcxQhVlMHrVAbcoWUHiOlAnBFctkveIrz3U1dBJAMe3qYozE76CBt7L0DD8DvAk7CvumtWXjG3pEOpVIYQimHi3yfYTCF02wulwPo-U8OM28HxEi0porPCVe63WTPNhUZvP0qc67p9MQ9GHP8IsJzrTOj3XU2ktXbsrR0pHLXkYQRbwzlSXKFVmO4IlgMCPqOpq1rCEy3Ih95Z987cTr8cx5E1sIpfUHhqRaZjBXwms2I8hbelduqOHiJOmuUsBjdNOgbEq1bTrhfvnwRNshjzATMcZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SnVl2zj7dUicxpiWfaguwiYS2S8LQJuJmeGwIyUDhfjg1gU6Oh6bkHa3DL1VppmboBuIAqqfqSP1Ehlv7x4auAyFIgT9RycDkByQ5nul_yHLZccDd37D3okBjHrsxyLIPJG3Sv1aNFB1uZmCvKfBdZQfK3fwIpnPysPl6pxr4aFDT-zjtke_5NpU87swM08naazKqpLBWGoza3Sjn5QyCPwJsxEB6siCzqIgkybNjjQz27JXA-nh9Z7_V3tfXdTjHrzNP90WnZWfYoS6VFGKSCsjN_0KXcBtDyIGWkkaiDJLDytyuAUikV6mJFSq8bwdYWh6BnVqOxsnIkEaij2DXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=SnVl2zj7dUicxpiWfaguwiYS2S8LQJuJmeGwIyUDhfjg1gU6Oh6bkHa3DL1VppmboBuIAqqfqSP1Ehlv7x4auAyFIgT9RycDkByQ5nul_yHLZccDd37D3okBjHrsxyLIPJG3Sv1aNFB1uZmCvKfBdZQfK3fwIpnPysPl6pxr4aFDT-zjtke_5NpU87swM08naazKqpLBWGoza3Sjn5QyCPwJsxEB6siCzqIgkybNjjQz27JXA-nh9Z7_V3tfXdTjHrzNP90WnZWfYoS6VFGKSCsjN_0KXcBtDyIGWkkaiDJLDytyuAUikV6mJFSq8bwdYWh6BnVqOxsnIkEaij2DXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktznZPe5ZLNbpfKMjm2wnqsKMXytpE9xPNkyict74TtMgY_Iut8IwGBR8tSnHyE_DPEzBMyC_TXX9v4wWFJFvVy8BRZUxqjNCIi1bSQ5R0HWPJQHVWRI3U5wVGJVw0EkLsBSkW4NUsSOlVxm_2Kt3oXVs1quIQgSYujFswecLHCO5Cr6nbFxcwOb_S_CddO0WW2qjNK-DU3N-KJNDgcmJ30OYweUSsJKbRzxAZnXqnKwlGWwf5xgzuKQci0cjFQaX7Z8t2NT43RUanNjNuXww-rBVEsf2ANPMNV5SZgRkIpSspgOC0F8ty2qEWIK-5cO5luwya1RT08KUWrtRNdhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVtbSBIaeX5BWB1oBmxsLsIPih_fpMVkxThKGhqHwSKkqDjxdWetww9hDJZSm625wUC-ilYHdudpfGdDFgimgM5YahjhnUDAjDf0XEMStI3XJDyfw7QwM9eIuGybtyJifC_URcgxG86vVIsPfTiWaRdwQ-YeNqkQvXWSRFPuo8jYxg6O8eAvwH1BisSLagWglqbmmW_a4mpM8OdzyUYWp-Gl62mxv3GCiW9JRVWL3YkmZ5ZiQV3MSgnzYrxwWP4FdGtfFMUedM0nEush-pC3ZecEPjtaSdAVa8SPrqj1tYwgXjD_C-vlxl3ldzW-0WegEBgFGvPkSG7lSmX7lWJ7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkrEbmxcif86oYOP2oNvrv-axvdO6aaJXG3J17Xzqeyc-RFv4iHWhkzfPkOuo5L0faudrq6KISqSU4lrKI0uAh2yMcdhcdSqwDjq8VWWQybiCOPhqPKjurCvvsWVAMahkCKyTk9F62wtKKUsxkP3PbCV5LlReLPjV-RkYJVZc6Ca1KfV6M1LsTgqRzGVagjgjUbyNQC33IoWbfR7cjKYei8nE2-nJrEZ3n-Eoot7dL8m7vLzRUEZkFx4nxpBaZVmR-VotxwUv5OjkvKffe4yvvC9E3RsNfpPlmUA6XiWc_5m-5gLZaiLGwTpIjhgZkL5x0Ixd2SV7ZNSYv1f41w4zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CnPtiIn4yLOQeqT8CPvtYL_JBS83-LXd6jZ01pkHjYMUFAz3EHKN5d0m7eCpJxi-8NquRS7LDDNNGKszD2iLNheKpHeXAuKRwqTS7iPH7aZXkTn2b74Fb1oQnOq2aCp5pyDlWNiZdvhNYARtUWq9dBdPGW4QJWE-pPn8XwzI1E-UcVsKYdLZFq3KM03EV-hxhZ_bL_T0m7gHlGGF6bVUf6PDMo3hLPk82oXolhy0wPhN4k00ju0S8gRXbHYKQK_wmTOQXpExUmCGry8Ox1NBE1TQNVkkQrJehFgRyJsqA0RAMLMa89nmLJDbqCtbAb1qu0CWiBvjZwxYRwRnLDUchg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CnPtiIn4yLOQeqT8CPvtYL_JBS83-LXd6jZ01pkHjYMUFAz3EHKN5d0m7eCpJxi-8NquRS7LDDNNGKszD2iLNheKpHeXAuKRwqTS7iPH7aZXkTn2b74Fb1oQnOq2aCp5pyDlWNiZdvhNYARtUWq9dBdPGW4QJWE-pPn8XwzI1E-UcVsKYdLZFq3KM03EV-hxhZ_bL_T0m7gHlGGF6bVUf6PDMo3hLPk82oXolhy0wPhN4k00ju0S8gRXbHYKQK_wmTOQXpExUmCGry8Ox1NBE1TQNVkkQrJehFgRyJsqA0RAMLMa89nmLJDbqCtbAb1qu0CWiBvjZwxYRwRnLDUchg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=PSeqtOPxT7ooDBD-1_2DEAhY29YlFouUw6rBf4-52MhWzfQRS8kqdjI55gKRj7ciZv6uppakIlK6TtKB67OVSdm1ODh9C31emh75G8nGC1YpoYAN9SHeN2OIhMorEeJ5sGV2TA9c9H3c79INVeOBpTQbuki5Lym1P274NsLwAmdg6-9ByP6JjG4qZxl6O_8DcY08_4niee-KuHOBIpiWrngI1rGpp-vKmECVryT3xoqfrfoaO6R7i1wcXyBg1R1ogrVdDanlUF214cBO_-Dj5fmF3TZxKxF3NzuaHWIfshMfdauC8eSv6_BMqJYz8bhNFXdNYfceAyxHUcq-YlYflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=PSeqtOPxT7ooDBD-1_2DEAhY29YlFouUw6rBf4-52MhWzfQRS8kqdjI55gKRj7ciZv6uppakIlK6TtKB67OVSdm1ODh9C31emh75G8nGC1YpoYAN9SHeN2OIhMorEeJ5sGV2TA9c9H3c79INVeOBpTQbuki5Lym1P274NsLwAmdg6-9ByP6JjG4qZxl6O_8DcY08_4niee-KuHOBIpiWrngI1rGpp-vKmECVryT3xoqfrfoaO6R7i1wcXyBg1R1ogrVdDanlUF214cBO_-Dj5fmF3TZxKxF3NzuaHWIfshMfdauC8eSv6_BMqJYz8bhNFXdNYfceAyxHUcq-YlYflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=P4oYlYfwzJrg7V3EjUNBKI3Boz4aQzx5OFGnIloICdvGK8Ph6U2iP4ua7gyZgd5DCZ-ax3GIeqca-jlve3gfy7jgIJofKkwvmw8nYA0I5nT1ektNfFyy8pGseQDzra_8iAEg_VxZuR3tC72_pAWWBNHYWqt6-SZfWKm_UYXUBpqw9gfvjZ2uHZpsitO_pTcWW9cfKOzO9U5k4k6PdIVuVWHpf8Vjy7n87A4nbhjktHIA2OChucTEAlVjLK8VZN7EvvekG7CcrSCjhZ8ZF-muCBTy173iYkLHfRHvxWi2HgQQrIAOFUbpSxelIotddRi1FbZc7UPTikrrb33BXX8btZpUA_GyZmKLrL-M0ILIdRoV9WXCTfmb-xDkBVIhRMC7tB9ZxBY_ppzBePsIfMcLziEhkCMGIiM9GW39BM-Cp4OyUIZoGlYrquX5oiiH8-1uP6BvriP6eZglwMdqnTto9YQ9BqbRbQJOT9K7AnLl_x4NSBUaKs_RyXQixQuPA4Dnc-DFBEH5dTORqP5pXvj5zdy_-KVO9OMzM_j_-ZPUKAg0b4VcWmNm0uAVB5Z2XpmhpQFCt0infdRmvtxga4SiswYtxYJ_sOXyPXUbuybK6MobXoVW8MuQ3rs7cu5frVcJSNh6UlMvKt1KwIpKKBpxGhFsOlZurg57aHCNaTfIoZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=P4oYlYfwzJrg7V3EjUNBKI3Boz4aQzx5OFGnIloICdvGK8Ph6U2iP4ua7gyZgd5DCZ-ax3GIeqca-jlve3gfy7jgIJofKkwvmw8nYA0I5nT1ektNfFyy8pGseQDzra_8iAEg_VxZuR3tC72_pAWWBNHYWqt6-SZfWKm_UYXUBpqw9gfvjZ2uHZpsitO_pTcWW9cfKOzO9U5k4k6PdIVuVWHpf8Vjy7n87A4nbhjktHIA2OChucTEAlVjLK8VZN7EvvekG7CcrSCjhZ8ZF-muCBTy173iYkLHfRHvxWi2HgQQrIAOFUbpSxelIotddRi1FbZc7UPTikrrb33BXX8btZpUA_GyZmKLrL-M0ILIdRoV9WXCTfmb-xDkBVIhRMC7tB9ZxBY_ppzBePsIfMcLziEhkCMGIiM9GW39BM-Cp4OyUIZoGlYrquX5oiiH8-1uP6BvriP6eZglwMdqnTto9YQ9BqbRbQJOT9K7AnLl_x4NSBUaKs_RyXQixQuPA4Dnc-DFBEH5dTORqP5pXvj5zdy_-KVO9OMzM_j_-ZPUKAg0b4VcWmNm0uAVB5Z2XpmhpQFCt0infdRmvtxga4SiswYtxYJ_sOXyPXUbuybK6MobXoVW8MuQ3rs7cu5frVcJSNh6UlMvKt1KwIpKKBpxGhFsOlZurg57aHCNaTfIoZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UBY-3tACafUl3JBb3_WV8Jc0s-6q0C3EfYp-hS_O00yv74CxtTfNugtWrata_4amxJWbzbZUtDsE_Sc7L2slDAPsBce7b-LlAL0N7YhxdhsTOl8V88JvVfpCzg0vdHQNxXObli4u-O9ibX5WHBz-EH37p6GTwuBed2dE738QpHBOeKvB4ZPRMx1dAm-j1Zx0sm6_6HwfFRZJoInyq_qXYjrsFz64tFaubqGumwi32r9X3NVAK-QJ7YesDjJTouAnFk7CpL8-gYQTZgDExalV89DuAXQnitTz3fLuTQUMtYo2SwSwiXpG7rP9kqyolm5tZ_UEj1z1RkCdDjGrK7GaClIJXNDtPSqQnHIglnlOoDmKU0DTY6hpKFcHJBo9C8OFY9sha5SYaLgH2votyVhvm-fXTIY8GXHCktWtbrvqxsL700md-0s10LjB6M3HfHDBg9hf4N5itGL2McM4vdePG9_18qMAoGYa2fnA9L5CEN8iXhDEYMh6WADqogTdhPwSkfQWe7CzTx-58RlTDOm_NXV8t2Zz0ROJCW62BnvI7ID7OboupNjtk_3Y52d6dCU34stPHo_kejEnUXXo0Xe_iU5COchmb9_EsqyFf7dYg33cO-DPFRUCw2LRyEoqDGdhBnN3ykwxNltwIqdndNSOwja2eHSAK3jyurwNK15kmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UBY-3tACafUl3JBb3_WV8Jc0s-6q0C3EfYp-hS_O00yv74CxtTfNugtWrata_4amxJWbzbZUtDsE_Sc7L2slDAPsBce7b-LlAL0N7YhxdhsTOl8V88JvVfpCzg0vdHQNxXObli4u-O9ibX5WHBz-EH37p6GTwuBed2dE738QpHBOeKvB4ZPRMx1dAm-j1Zx0sm6_6HwfFRZJoInyq_qXYjrsFz64tFaubqGumwi32r9X3NVAK-QJ7YesDjJTouAnFk7CpL8-gYQTZgDExalV89DuAXQnitTz3fLuTQUMtYo2SwSwiXpG7rP9kqyolm5tZ_UEj1z1RkCdDjGrK7GaClIJXNDtPSqQnHIglnlOoDmKU0DTY6hpKFcHJBo9C8OFY9sha5SYaLgH2votyVhvm-fXTIY8GXHCktWtbrvqxsL700md-0s10LjB6M3HfHDBg9hf4N5itGL2McM4vdePG9_18qMAoGYa2fnA9L5CEN8iXhDEYMh6WADqogTdhPwSkfQWe7CzTx-58RlTDOm_NXV8t2Zz0ROJCW62BnvI7ID7OboupNjtk_3Y52d6dCU34stPHo_kejEnUXXo0Xe_iU5COchmb9_EsqyFf7dYg33cO-DPFRUCw2LRyEoqDGdhBnN3ykwxNltwIqdndNSOwja2eHSAK3jyurwNK15kmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uRQdV5-6qTbO8xTsCz7XuTlGkGOhT7NiZxE1zPKNNNDRlJFIZSvc1rOkzKHWaTHOE4fauPaMkWI43P8LfBbcdH96NZdgEUSKW9DY6tyW1szPMhl4b8JSF8Y8FrnM_3-tE5ldah6VOU-X0WBfVy6TBgszGioIwRJ66oSogsIVWZeYsUIL7CSQstT5IwMjdLoF_NG_KONMU1r1hvxBimdG6_XjlYLR5iP7qiW3RspAcWbZYSqU50ARWYHogVYRwDyoGU4ysertPDMV4wrle58gzxGMPR4R2QtcvYjIdNEPW3sipyCJBiuPwkhG21YRLR87A5NiKfAp7NCwJZ9gTE0RLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uRQdV5-6qTbO8xTsCz7XuTlGkGOhT7NiZxE1zPKNNNDRlJFIZSvc1rOkzKHWaTHOE4fauPaMkWI43P8LfBbcdH96NZdgEUSKW9DY6tyW1szPMhl4b8JSF8Y8FrnM_3-tE5ldah6VOU-X0WBfVy6TBgszGioIwRJ66oSogsIVWZeYsUIL7CSQstT5IwMjdLoF_NG_KONMU1r1hvxBimdG6_XjlYLR5iP7qiW3RspAcWbZYSqU50ARWYHogVYRwDyoGU4ysertPDMV4wrle58gzxGMPR4R2QtcvYjIdNEPW3sipyCJBiuPwkhG21YRLR87A5NiKfAp7NCwJZ9gTE0RLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp8dkau2NlFyCQZEbErNZyMHEuPpK_XohJrG88zdYTZVGRJTOJ1l7-CMWeSl_j12ijW4OKxOG8mz-Sw2VRjs4wkgT2unQzLAes_-oVfgACzh5KzJTcMdO1Z8Ix3jIHC1rQi7l10Oe9OaZuJpmYY0PIp7qYuOa45iceBG_dZxuE4kvHz25qWsFY3hucgUMHlL9E8IyrW4npeiggxIO0r6cWMV3XfuI4O1M39quw7zYsr8EwL5S-sxDHJkxxAGvQw2VmGgCy4t8RX2A4HYLgQdzxVOMstUNdfO1bEjgIxtHmAOGD_R8MvR6VHDDCfXwOxTGZpdv8qhbVKchoCAGZQHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=PDZ4d91bUkIyPFv179BCz0xF-l6BxShyG4QQHWdjnItHepRyXewFGqLa94QGPvfsy6Q0KxzSyXPBQC-yrQDzSsL9TZp3Be_nIY3mihp4xFH8sSQpV_ctuT1Ep13OP7BsbFMB5mo6pep_NHqXn4-kYKjkZ8l1Qhc8mi1XleqTdAOi6bkQ5ohnef7NxOKNTIDWFAyriY08OyYCWRlRiikGWY5cB3_xbSmP51uIFrg2ogNRVIHOQFiqNjS4o0kzIBq8pXt7q2ysHUqB6WhSIH_pKYiytxcaw7qai1JTlGteRIXpzkPJ0FCnV_BTun3dQ-VvMIYFqdEZpkdOgtwFPQ3-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=PDZ4d91bUkIyPFv179BCz0xF-l6BxShyG4QQHWdjnItHepRyXewFGqLa94QGPvfsy6Q0KxzSyXPBQC-yrQDzSsL9TZp3Be_nIY3mihp4xFH8sSQpV_ctuT1Ep13OP7BsbFMB5mo6pep_NHqXn4-kYKjkZ8l1Qhc8mi1XleqTdAOi6bkQ5ohnef7NxOKNTIDWFAyriY08OyYCWRlRiikGWY5cB3_xbSmP51uIFrg2ogNRVIHOQFiqNjS4o0kzIBq8pXt7q2ysHUqB6WhSIH_pKYiytxcaw7qai1JTlGteRIXpzkPJ0FCnV_BTun3dQ-VvMIYFqdEZpkdOgtwFPQ3-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H-uu5pB5YMMdX7SsXdAZ_IkeRE_LMW3Kif5g7SXXXBf-EqLPyUJ_LcPcYIFmwx0_tvJdoaDcxM2_6GnzqQ9IVVl69fh-XDM2c1hcMWd22HDkoqKx8U4UBtXmhUC1zoVOpSxDlgS7_YZwMGZnfas8PwBMRJ_pR9aUOABzokVbf3PrljJiKi5Nw0qlMBgxQBNMqkWlBk6MXRjKBqaRRQRPytuXwhxwIC1AY8NXtrFh4qBDX6dnaJAuQ40gLpLICux5WNEtPbYGDvfGUhTL4oeqsdJ-GarsXVZjM5RE3HTbxfM8E7TlK8Pbmy7DRVKHiskkfw2dOyefnVGRZ229EdrujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H-uu5pB5YMMdX7SsXdAZ_IkeRE_LMW3Kif5g7SXXXBf-EqLPyUJ_LcPcYIFmwx0_tvJdoaDcxM2_6GnzqQ9IVVl69fh-XDM2c1hcMWd22HDkoqKx8U4UBtXmhUC1zoVOpSxDlgS7_YZwMGZnfas8PwBMRJ_pR9aUOABzokVbf3PrljJiKi5Nw0qlMBgxQBNMqkWlBk6MXRjKBqaRRQRPytuXwhxwIC1AY8NXtrFh4qBDX6dnaJAuQ40gLpLICux5WNEtPbYGDvfGUhTL4oeqsdJ-GarsXVZjM5RE3HTbxfM8E7TlK8Pbmy7DRVKHiskkfw2dOyefnVGRZ229EdrujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX5B7UfPOXBPT8tAK5RIcrI-MqZyGMC28hed__SkKlGO1hB2ySzqC8evnb80W8BPdKf4vomWSluq8PDbca6yStwyfJ38HTjJX_rHu9sRt63RztG9X6hP0NIphDALOOp1BHlW49eUq2dhCnzIr8TkPiz8sIUbEMa0Axu8LU-vUroBS4qn4UQ3TBNzymaaMxrKpW-0JBnr4lUwoRTdPXlcEVcx0BXx1vw8ZihMIDdC8iq2mSJro_dUsHX6f1ihV_IFX-FloVS4Y2QAH28HSwqsy6zAQFcz0ssNjTqup_MYn6_jhKerQrNyplTt0A-vuV95azgVilhNMA-1z-z9eLY8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP2sh5CHF8sCbLHLGHsdItnyGsY7s43LeQ0FvKAy5hKZRzDvIxIMORtq9qKXMAg9HNIgUjHm9TTo80C_hmFbQKCFQACb3W83RCDutosMC8g478thfm4OK1WcMLMavZIl0SHdrysmRKpgufd0boPylw2lxPt3nOtXs-82I3v4xfhmictb9yG4it6MPRvIIQt8mIJb5SGN-85QYwjmm-_h0iJRjJWX493USVB8JOi7Dxlpg_uaH3VVCeifKSG0M7adPdZyL3oZe54LmSgSC1NcPAonWN-WnXI2cgys3jltIqvD6Xu70O-ZeeIFPcNhpCSj79Pd1I-beHDWy5JWphe2Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfLaTmS5owF0CwFWfxveUIKEzcHti8U252BkfO71G8IFysqYuuUl93INTiIi5Hb71QaCr72hcsgvkuLnXDcH_5dZFyN8SVT1U2PrY46FwVkaxiDczkmXqf3JvM7lOUSH-_hO6g_1OP5X3oKiFOrYhumO4dqPideuT3g5EmYh33jfWAj06XdO6xloAm0A0rHn2PindAI666fs_QiYAl5BsvgsIQFX6DIjjPKf_o54IbKCdvbOJbeh3lMpJdQKZW4sFRwM1HQy7acrx-C20hzmj14lWTmyYmolK_1G5l4G_TItEwwd3JwMQ1iAlvY-QFwQZgTvpKu8vk7BYdyLgr4mjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8_eth60lB8MKJDY5CI8uZ498pOl7vakzKuQp3hqqNkTwI8KYyU5OyGzal1Lt5SQMn8UOpnQec7OIcz3nXdjf0p7Z3_gtVeGBcfBeiVDCxpwEPtZhX73yIHUi6k9C4PWmZdGUW0tWSvEqvSyg0xnJyCOsAW7VpDajx3VGRO-JPi0Mw_OBitSewZkCtaKHcdrZLdU4nBuXcHkhDjy7PiseQDDcI-nwMFyn2A82wG53DsB_NGEcVyTmbUDTAQHOaCq58lT1uNo2K29m9CJoGxbHyN6bcXAuwgjumejQnBcaBUuBxcIYL2OKJvpAkSG9hAqyFJFZL6t4n5UyMqWeNqqGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsDu0OQzj3lnLT6ZH93YWL0yBFSpdRc2IOcjvzODSewZ3uDybDjLKhPAOxWLpHoUDmjT0oT1aV6Y2dKmwpcxOv51vlFFiREodbKi0G6Q55iLTjtSlA8OGg9vQjNQGCPV1flJddLekyIgCQnPUBoJfxtsCMdsLTwQ0xPs7dDWPVjFX73A4n678YqhEqPJbpkkxzirZY0uEX9e-Rnl9tEmsig4b-O5WzoQ6mM6P_Bxkr_aLEBmwOHDebRDyhpqiFYRce3vdiBhE-AfVQIJHtNYO8fRjb4LsYlo3QGWPtVc5noaPXyuijaqzUcbcG4ZX8wjLpKdD6p6XH65P1fjGQfpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9INX_a7FwSPRClVEqnN7Jkk8LvC8qrcaDQwGOFiBaOrX_JgQ49OtuD3eShgAtoFBKGiRCJaAnslbSJcMt3SPNpT02-RhAuPJjALQsvFXcEZO2o6eS8SEiqm0mrQlN5vNCpUR5LCbRYN1YkX2Y8hfZ8BDfuznjH35wrz9fF3ls_p3-AAqR67TUMoyvTcp0StU_Mf-xg-sx7zDJCzUACQiQUgO6Crhvl0Ekf66XwHV2nD70WPsv6KUlVAaBL4Aa7gg8Bg0BPOraAcV5X-ymL8V7M2TyVw5dn1GqumPC2Lc5TWReF_P8DvW566s3BXY8bGd9OYmDbQTFF2qrca5edleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmFaeUhP-rlmG9f8dg4gsKhtk-M_sivjaJwetpTXW7vXkRM2E0qAT-fYT4mKljnpeXKO6fjdAHbSNuvy13ha2yxqVK8Oc94LJUaYm9JuKuUdcmox8BCZ7DzA-Jsk-PgZQkobnav5FBPgM2vG1GM4AutqPqSDAvZdUEWcFtWnf71UcphTyjPfmjbQRIDEOgKoiP3yObobmYnSQt2OUYnpDwHZcHLISks3KI7aZps568KCcKkmAZBtlAsiytizY47M3cMzxWvSRe1QjBGthppblH-if7O5XkJBb9lzzOxs-NVM1TYKA_mt9r9pscG3ULaVTaormx3aNUH1E7PqtLaudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PAp0DiezwZmPKSN_Fqpww3si2pForGo8gzg1LCN7-pcGgrr9JUr6diVznZyipIKJiXWxe7NvQFUxSC3AYRu_d5wLWhWyF5tdWQ4xNq2Dmf6UtFobfICht3Uy4UWDuq0wvUrPYa1bjEpDUeUGCy-hJkJpWZvnFTQmq60SBrPeZfT-EiPKjGjAVMTe6zHrLDZx1O-8NPmDaSnRI5Sb7T1h-5uXgihnlg3FydkWxuYUJ4WTydnbJ31I9iXVk87rLzIOLGMNSMQP-22VRmGb9HUY_KFSQmmvuWthIkBXdahVgwF52JuaJWLSvMSQDRlztpC1GcoTV6McKg4NkDFYNACbow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS7roJq86AbUEmOyXXuTTml3XNuYykWQsqR3jxg08WuVfa6Q9NomMyJ4YOdPjz_M1VJ6y5KSb9eB58C9L7qYw2Wg6nSbm873iHBROD4Sgl4s_P4zZtOUq-84JN4LSuKDWGkMiCANT9otsE2YiuaC04lkfrDrjc-VYYGpRwCotZcLEA-8WSpl85J7b2_Xml6ucKMwuV9DXX8ngPRPeCeiCoeMkGkOor_e_ssTzrcAKJmAqQKr_f-wk36Zx7_mdKo9djrD7KZu4c8S2fhWfbw2XlzIdlGfTohzTJjAhBtn18A_e9H2WHiIBcjT9uqLKs5xPMWWfxCruebUSdDu5vmHlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkuANR-6gpkAchuQ82uTDGHtiMmaOgYoVwTDl6V4A9o2xcz1CnqhGA41KtDsciO1QNlCn5JRN6Rpp67Mlg9oi1WO7jTitxmwOULXHJxV0SQKkLOTQUuvIlTUhW7ZwwIg8ZzObrGV--VycO2D7y8kqaotR3soV4S6bnfpM01w9BCqlWlLB7LeebVIYqZa9LWDNjS6GJHyLwj2v8JFASYed9wWMlrx5U9os8tEalpOgNR3EQEaI_V5-9ymS5MDqAj0jutJjq84DOOu-o06P7WBfsauaxbtYX_7XYlOBu_I8dnYGcK8603tGix8_ajPIJJis2kkvk-3Y7-uUqrLpIa5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=lHtSJnUXXjdv7tRK3Kpam9LKxkhDc0y4lEHZBsnb7k4XDQF4YgUF0UjT3TMceUQDF3oaI_Q__HjsGue6ym5dgBP5jCtDkyORH121eMChXKp_C7QzOIPmoSbDj0Jd_LwWF4r6KUWGI6MNjyXlRB6gBoERwD1IPp-itQuqxP3z1FFb_zvQ86JBwbvTzW-bkpf7rH9kMQRLyIXOfm9jcEvGYVyxuQyFs3EnMlq_Yl90APZlrA-uMLQa0oYuwNuywZMJIrjXHKVpGTgl_FzjpCly7xQs7pcByxZ5DCBg-79In_Ib6JmzFuuvJUQilCKilIvG6iWstQDXdhBAvn31Av5gwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=lHtSJnUXXjdv7tRK3Kpam9LKxkhDc0y4lEHZBsnb7k4XDQF4YgUF0UjT3TMceUQDF3oaI_Q__HjsGue6ym5dgBP5jCtDkyORH121eMChXKp_C7QzOIPmoSbDj0Jd_LwWF4r6KUWGI6MNjyXlRB6gBoERwD1IPp-itQuqxP3z1FFb_zvQ86JBwbvTzW-bkpf7rH9kMQRLyIXOfm9jcEvGYVyxuQyFs3EnMlq_Yl90APZlrA-uMLQa0oYuwNuywZMJIrjXHKVpGTgl_FzjpCly7xQs7pcByxZ5DCBg-79In_Ib6JmzFuuvJUQilCKilIvG6iWstQDXdhBAvn31Av5gwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jcufDMrQliY_Yd6AGYv7_R6J5eqJ45pRH1KAZ5HiP5MRMxHvqTYDP8S3WVXWdvzjwhRu36Ec1yLtwMvO1CcdJRgbSXwuwOTvpg5btKtl5Dtl0nozTz1NEPvXZsyv7dUja4wDD9xpCBfZBpHk_KndT3KkOjLO5L7bnr6KRpC6b4c2ozDZwhzTn4J4ZcE3nhPWrCQyY8QWFEm95ByKo-3RB9Snk103KbY8ztP2hGFX8SJN_ZoDPRhCKsmD8tzVlia0RRY5tZaPdzwgfvei7dTHW07jsWa9w8Hl202oHdkxIeHg5gLFRDdh4C4cq3tNwH8Yq274g-YhXx2amhbZX0084g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jcufDMrQliY_Yd6AGYv7_R6J5eqJ45pRH1KAZ5HiP5MRMxHvqTYDP8S3WVXWdvzjwhRu36Ec1yLtwMvO1CcdJRgbSXwuwOTvpg5btKtl5Dtl0nozTz1NEPvXZsyv7dUja4wDD9xpCBfZBpHk_KndT3KkOjLO5L7bnr6KRpC6b4c2ozDZwhzTn4J4ZcE3nhPWrCQyY8QWFEm95ByKo-3RB9Snk103KbY8ztP2hGFX8SJN_ZoDPRhCKsmD8tzVlia0RRY5tZaPdzwgfvei7dTHW07jsWa9w8Hl202oHdkxIeHg5gLFRDdh4C4cq3tNwH8Yq274g-YhXx2amhbZX0084g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsdpee5o3YNNtCU_5DIgdtBnzjyCS1UC2eH8XsCx3Zb7qaQJOwQnCKKWZ5ZYnC0jpDCjfY7F_4adkSYjP7h5LhQCf9TAIxkRcFDIW7hWyMDIj0ELOie5XX4-WP2-GlMk5ryGBxlYwNWTOpplMYi7tSSCIdPFcGhK2r5gUdRgD00CZwEu5EZM7azK4joOUyJcafyZL_NgZ6fqDKnLMl_jRwKmbHoD-784WXPvGidsosbfNULDViA2zvwQwkcktqJEne-u_T_jpdLQ2Z1C3dBD_AU_d60bkdFqiE6m-aXNvnMBT0cCVmV1d37-SEJMF8fZo-hdtnUbekqRQCt1Ei0aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVT-2CyOjV54BrxYoFG7isrV2wXSqFNNTHpocSkfrZubKG9Hwbq7Um4GzaRekBPp6L5ZrkKC4hVV8bY91AGd3iIcunAHuNkB5cwB8bSo-q-DsCRMS7Nr5dVDzU37WwsVGkExpbXXXVHHSIE1O20a7Ls5QM_qqufg-7WepCtfKOFQTv-DnO3SWYeQRxPRz8V4GA8jLpux6RbZiL4hnA0uCXQJoz_vt38qGn1LEVd9tn_9G_83tBZp_fb1MsxPgx_dj8I_SEywyqP-XAToMdYihVuktXOdeOJUykGoVWVVQW8oPlMM9Fhm6Vwx7VSrsI-HjWZJWe9ZxIRWO0v6wbVYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g29m1sGZO0rJ5_chmxVklhtpIor-KFzC6o2LsZMR_nfQcbW7exolqLoF_3NCY3Z96DkI8yr9d80-ijF-GRYZ2oIGv7k146lS0XzzDDVPjWsH-P6E0hERvj6U29Q1AcAyDu4tACRMuJ3MjRbDEhfugKOIZknFMQSUUSj10_FOYhOEt0zNd-tfSVU7VrYjYSDGa81xoWlmqfxdZs7nFt-JwZ1UTQdVKNxD_c7J0W521Y80cG-JF4E19TCxKfCKD1lH0ZNSkDpivxatAF8VF03OxriNP-ZoPOhI6sysvcXuP10xrHGknm1VkMcbJdR5qofU_5yTnrZXuewZ0RvvCwZ8Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjehTxorgY1LyDIwTjFlJ3EFhPuUT01TkDBW_ODVINUW7dZ5vxJ55ZIVg7HjQJDpcw49-Uzl_2E2LyasEfxbmLyvn5dSSjO7kkGGpPqVdZ79WJIGM8PjWgIRIOvAtab89ca4at-j2Lic7pTa99U94sSqgmSQq3-LWhXU1YzjyIpav1BHE7YFdtZ6ztxH0scXASpnQjX62rINXwfZmO61edL2DT8Qzhhg8JmFzlInjhrRcv_pOwRyyCY0rzlonOUY0moBDZ_sFu08v973Z43dfwN0cwZF4vpTCHkjCzeLOC4lo1XlX_Ey6WfX-umWCdq5ptsREwNXWkcLNyuthjbIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgTuaN6cgVrcES2OHTNFrThPcO4UuQf3qc40-ZkaMmBpIgFLirBW9mK6sSwHgP-T17Z3qDEuTC9r0EAF9-ss0AkVtsz0EPKx7GnE0fVf8gPhBakGaNK_bkYmkWghX0ctUnjjWjFgc3_fkqo2a0e8ZTX7EZyhNxYVRaYitnCaOtqBIsZpvNsNWjXHxKAETxkQ5FsATVem0SZ1BlK0A92r3vqrlJ6k_LmdYE_Z0MpNqZ7DgsNRqoZLJ5fWXZfhFYX8K5O6h6rCjc3U6_2tlrZkkkp3RcHx63zn9MxlcosG5-hapEdM_LdPLfwiQsK2o82W4kwtZb9dR13j41Op8anpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvw_JIDocneLEeJgzUDG3QaBfvY9EWj9SlLvx_hw40gGYpGTnpYb3-RQrTNAkCCEuafAa6KKUNH-m0dPKIfW8w5n_zT3LnIeLmbUs0PPfpcSkHFCxzkdnsxhkQdxykNxcRMPoycYi7x2VGLVe__0iFAomCghHvfknzRkM0YtqRbIkBskBm4Afqx677IZRVrUpPlM5XcpfWmizFYf1-WZlxO6ZTBYU3CP5VBWAHYUCqUY13FQwVEQrVAMU3MSTT-aJHpg4QMJk8si73FyhSeRthH4ZJ4OiC9e_tbFYt9uZc3VrwkwpXTcItf2orkNWAo4bXaOO3EKnX104it8a8gAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiMfrEAHIlNTOTCug0bEg3qJd1IEO5pfohJ45sAAchcMYOQkD7eYQeS-ZSpymn382mb0H1jrSPMBXUbwwR0bUPXIXdq1aT-Gxidr6Bh0s6_otTaAYCZdXVsSM3ynlsYTTPHXTpwBwgTZes-Quc4rN08WNciIGICm4-qPOfMuCsedP8SG8VLaFFdSfN2bDGGk31QX9U5DgQd62QqxquNIXVXxXGKJRUkd7LUabHq-UB1gy2mfQV3xHJ0OHMdOywhn7cdE2XqOWOAgwvoQNWYhh84EIH_zj2N3xtz0V_xejtI4_fWft7DzEnUCJ7LPxrkxkbz24GCFyd6wIut2q_hzeQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=rG0vdycwNA1ojSvolAGdki1suZqMtxlzJDZHEY75bG2K_kSKXGGiTe_9VsAyQWx8TQbVgZQl90fon8Hf7eiok9Wu1_BfUDFqxyK8VyWu6WiJmK58_o29JDKo9H8DYkgAhy5gP4UN57dcsFinSx5TmHLL4eQHCoQEzNdJ0zBJF99qJ4Dgco_0HcBjZrcGNnhvn8ttxrRGBRZwy1Dx_twc25vW09L3m2DZR56pj0NAH8wDpMcJEB6O8obBW6ngM_ODaEtUEhqsLXWXv--a5cr0vdoP8HHomswCY_q67_AX3QSw8mELlYIGBi1zZ9SIlBCPukvOmr6lgy2qJXY97DyNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=rG0vdycwNA1ojSvolAGdki1suZqMtxlzJDZHEY75bG2K_kSKXGGiTe_9VsAyQWx8TQbVgZQl90fon8Hf7eiok9Wu1_BfUDFqxyK8VyWu6WiJmK58_o29JDKo9H8DYkgAhy5gP4UN57dcsFinSx5TmHLL4eQHCoQEzNdJ0zBJF99qJ4Dgco_0HcBjZrcGNnhvn8ttxrRGBRZwy1Dx_twc25vW09L3m2DZR56pj0NAH8wDpMcJEB6O8obBW6ngM_ODaEtUEhqsLXWXv--a5cr0vdoP8HHomswCY_q67_AX3QSw8mELlYIGBi1zZ9SIlBCPukvOmr6lgy2qJXY97DyNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_3h-rY--Lmsc4TBNn7VKWWJ0_obH1u0kkd3Dm18Pzjp50DFWixPoS1BpgLJYlCJVavTpspNCM7tgAOwdTVSTAFIiGpZcuyhIT8fQGltAOGON-WdQXt6jZHOX9SVfSsEpWSGv2fPbpRrPr80SI5-fHwcelOl8Q2QgtBeX-50qsP-olYb72-fOMbx0mSfilVZs5ist-y22AwIFPLHi4tSKV2aULxxT9tPTCzcxrv6vaQvSUJrlUDFO460O9-yxFJNVtTj4dwCtHD9AusPq5NfouIbE7nYLUYcgHW5rGTh54s3IDioeDQqDmH6Oil2hf5jlUVRjfoGjsZyw3GUfaIDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GzmL26hBvJeb0O4vcGn4ueowadqqAcEvrJajf4lSSS2FAtPq1EpxwaUUQDzrjzJV-_efmYD-1IznD1-m5jX0QT4mgTJETKg6cEvIe_XSHyhMikCFQyuekca3WFi4fhVrygBXzJ--7KS_CxfhhHOhHJEz8iqpmWjgzEmfs0iq7o1c07svLRQfOxIDt23u1_cphYZsBMUWVXV6Rt2QFmDxnm-Vds7WY-gLgaIoMiOf_2zSZqWapizC6DQ8INIjgmivd8KQijPxmtkQIsAEWBmqFRGKmqHzseStCj0z95Vx5JVtYgDnWLX9ivnJwDKDNlE_JxdBoxs-LEksOLPDlaZOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=GzmL26hBvJeb0O4vcGn4ueowadqqAcEvrJajf4lSSS2FAtPq1EpxwaUUQDzrjzJV-_efmYD-1IznD1-m5jX0QT4mgTJETKg6cEvIe_XSHyhMikCFQyuekca3WFi4fhVrygBXzJ--7KS_CxfhhHOhHJEz8iqpmWjgzEmfs0iq7o1c07svLRQfOxIDt23u1_cphYZsBMUWVXV6Rt2QFmDxnm-Vds7WY-gLgaIoMiOf_2zSZqWapizC6DQ8INIjgmivd8KQijPxmtkQIsAEWBmqFRGKmqHzseStCj0z95Vx5JVtYgDnWLX9ivnJwDKDNlE_JxdBoxs-LEksOLPDlaZOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=m7SRX5b4TE9wNQNTgLCrmiMiLiaM6ubEwRQvnwV8L3UbuApOVJkM4qDJt1SY0e7v5U6zpcL9XXLc5Pc7lcbzZGPLz-T8mEn15Pl-7i_MsY_0jbp_NK2kyK0LUH1vhewhRPNcGRaY_sN0_02cfyRR4jaaJuaeoGPwYni10BHkGmVJz7HFk8Pu29J3xg5e4nhRSyf_SSbvLsPVfVaU0PA8TI5k0iCptAviB4nkeZmupDbYA5SCsjERxnzVgohiG2G1OlHfNxX-HczKv-AVy9yrFJkm28YTuNAhuTD2j2sfr3DDW8cOCTuZQuRXGAobORzzkV7lszwwgHxIdqRP_RUKGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=m7SRX5b4TE9wNQNTgLCrmiMiLiaM6ubEwRQvnwV8L3UbuApOVJkM4qDJt1SY0e7v5U6zpcL9XXLc5Pc7lcbzZGPLz-T8mEn15Pl-7i_MsY_0jbp_NK2kyK0LUH1vhewhRPNcGRaY_sN0_02cfyRR4jaaJuaeoGPwYni10BHkGmVJz7HFk8Pu29J3xg5e4nhRSyf_SSbvLsPVfVaU0PA8TI5k0iCptAviB4nkeZmupDbYA5SCsjERxnzVgohiG2G1OlHfNxX-HczKv-AVy9yrFJkm28YTuNAhuTD2j2sfr3DDW8cOCTuZQuRXGAobORzzkV7lszwwgHxIdqRP_RUKGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6d0s9IuCUzzlpEThQhlXBNvO-YpVRzuBaezaM61-0z1b5-GgSFAcICWAQ8kAkKzSWvgum3uW-0liMGLwF8DKz4irIZrRsbrA_KsQ2Q6fhuBMM34956Ie2UXkwIvPe6X_Zkjuqp1IBydELarIbqxAlmPf1ooHe66rfvifNhSBGUIEWQuyHF9yL_hJzi9kNTar4p5t84ro--3jlhM0jK7MALoy8iitGI4QMwLN-DaeSQLvFW0_S_qnIJBKFaHn0ULtlTijogdbnWmugBnh1Nr6EjOkQnTCpapkU-fGJXKqpQk96jLCiqxiZCFypOzPzlAxbxHSY2b3oWH2pGlASkN7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Ks-pZ_Eov-JpiNTfOtGisSnuTIkGqyD56fHVOkIMGz8tf2UzKnKoD2hPCfbWqoY_iTlF55NHhNnSfRyGFLbtnys1r5Gw-Hf5LtH8mPpJTz4eLjPiwiNWtldkK_e9s9nYxSipNkX3C7QKUQ0uABB838s9OQgezIKosSlU0bbNS35SiUcSkkYWwOghEjFWnINq811qe8TJJwv-2QVVyEq2H251sq46Y8RYOLdTeyVyVp9mfU8ugPMJ4X4826IIgeLzPohG3mxQ_x44h6QMJBgm-j9PtYvvXEwoIcp1iWB8Nr6wRA6otbQvs1J_ykGlhIYgleDMeNodqQB-xi2YSycw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EX8MPzMGedliUvSEYc6d9qQN1VjnF9k6OV1YU1aACk7-5Y1MgCYAjCZJpSUIyseHgTTA1w6BmDeH4fJ0T-uLw8BwNHjGtTaRNS9Kgjvi4eD-q8sBdIDabtD-oi-9oMexhh2iBJOytGLUid81X0cnlx5zmFQBcmL9xNyIOz0tzO7ooW5m3csQGPZWcfRpiqtTaW7OqqWPW_hBT1xJORX1bXjARXK7uhzBG8IWsYdfBDbfEfFXdDJbqHwhyHnBCBB9vdSv59C5QFjqveBdwCdohRavjND11t7z_374aZq6oQdjYM0XdIEvTWjc1DnCzLB8z5dFEwuYO7knPinw163EOWmA5IBwa78EtdKSkNzI4f0x1maMdR9UywSwRu6K3pep-twaRKf9PYTyxTTu7dWS5PuVEGE3bwHhYrQkUhMgzJUt9_4newu3xTBNE8GoAFi7QoHlNtR2lTBTm_4bbBohLAySf_VgCtx2ZKSwqoHHZYMmndgDR8Th1dCo-_7WHcKHWLM12geulpLWkvvseffE9Fw6Eqog4B1rMhEbK8sWPvHD_UpMQPPvKE_Y48JitCrHaCpVe6vkvP4KgrK1Uv37qNZl__UK9YZAodqGNy8zF9W91g4ymXMKQrj7pMaYejpUQ8DSV0FVoEy6gvuSQVPUJJe1VYkn6TJMkH3WurILYhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EX8MPzMGedliUvSEYc6d9qQN1VjnF9k6OV1YU1aACk7-5Y1MgCYAjCZJpSUIyseHgTTA1w6BmDeH4fJ0T-uLw8BwNHjGtTaRNS9Kgjvi4eD-q8sBdIDabtD-oi-9oMexhh2iBJOytGLUid81X0cnlx5zmFQBcmL9xNyIOz0tzO7ooW5m3csQGPZWcfRpiqtTaW7OqqWPW_hBT1xJORX1bXjARXK7uhzBG8IWsYdfBDbfEfFXdDJbqHwhyHnBCBB9vdSv59C5QFjqveBdwCdohRavjND11t7z_374aZq6oQdjYM0XdIEvTWjc1DnCzLB8z5dFEwuYO7knPinw163EOWmA5IBwa78EtdKSkNzI4f0x1maMdR9UywSwRu6K3pep-twaRKf9PYTyxTTu7dWS5PuVEGE3bwHhYrQkUhMgzJUt9_4newu3xTBNE8GoAFi7QoHlNtR2lTBTm_4bbBohLAySf_VgCtx2ZKSwqoHHZYMmndgDR8Th1dCo-_7WHcKHWLM12geulpLWkvvseffE9Fw6Eqog4B1rMhEbK8sWPvHD_UpMQPPvKE_Y48JitCrHaCpVe6vkvP4KgrK1Uv37qNZl__UK9YZAodqGNy8zF9W91g4ymXMKQrj7pMaYejpUQ8DSV0FVoEy6gvuSQVPUJJe1VYkn6TJMkH3WurILYhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzrcUfvk08LwMum14SwpOOSY9RSIcPFEHCDHr0TxWV0HL8NwUAC-6xRWgIEAHFeKMp3FrvOBop5yc35P7TIxJiynTxc5U09g_INXT-TEmgY8L3m7XQ1nlIqNEEdDgUZvxA-xt04CgkBS2crCf4bXDLLgRLX_ekL2dB92_aRNBnvFAE5AzCs04-0604J1QDLez0Pq6HmFiFIasaDsgYUxPy_mmnz7fItDasfyQ6x_GTtuaETS0nXL8Ty4lC_-NC_sP3HIRGvSAQJT6Fe1R0nBuppj4AjSG2HxNOqba7ZJ7XVYF3nKoObQqxiPo79N6_8vh8AH-yePQj-kFmPWDyPchw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=FFcYr-zXGtarJKbJM2A5D1NaGN2jPOx8iUPohKp4kb55j53j_GHlWAuiWMa6MlkwmlJRGzPXMh4l0fRE8TZeiM_8c1tSQa-6d3OpPso1UzbmLrlOratr_tVjjOUMw73e0_F0wJ01-KproJQzSN8ArkgK_-cXqGwr8df3iXJyCXjLLiWGTAlDqNbGUXcEGieyCOXMd-nthZMgGCkZvi_zD5ZGohSWGYtDUhnrGw29MWQKH-WDc1Ztw2Q4PWrC2cWvUXmYHb7AwSBahcwK3wVlPAfEia4DhjBqp_Ys2NbmoVcvquc0KsS9vxb8u0msyGlTAWHijIei_pJ_rWExtZn4FklzrGTJabOg7cyGTZNyjByacoUZQ5cr4aYhf6V5x6Assj9Ku1alnVPrl9agkZTHruKk_CJjN6DYWwFOuv7u5vg0a_nNJfTa5JSjrK2hKhS58o4ZpBpALFdKeSIai3p1lUN6fgwMrMVdcwqUeUFMhRFlXusl00g525JMuIuhylsA7qkT0oCTyawK1WDoKnPI7lOSxMLc1qPNto4YUj1d5qufKR2VftSoqio2T9_O4IJn-i6Fva5OS4wgAaILOhkO7ZPGLhzza44cKTEJMt1sFdojTjXqgcf4UXhM0okjb8IH0_z_pZ7-1fxrPiMfr3VKAHYxOn05I8tp7q3RVI2eUo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=FFcYr-zXGtarJKbJM2A5D1NaGN2jPOx8iUPohKp4kb55j53j_GHlWAuiWMa6MlkwmlJRGzPXMh4l0fRE8TZeiM_8c1tSQa-6d3OpPso1UzbmLrlOratr_tVjjOUMw73e0_F0wJ01-KproJQzSN8ArkgK_-cXqGwr8df3iXJyCXjLLiWGTAlDqNbGUXcEGieyCOXMd-nthZMgGCkZvi_zD5ZGohSWGYtDUhnrGw29MWQKH-WDc1Ztw2Q4PWrC2cWvUXmYHb7AwSBahcwK3wVlPAfEia4DhjBqp_Ys2NbmoVcvquc0KsS9vxb8u0msyGlTAWHijIei_pJ_rWExtZn4FklzrGTJabOg7cyGTZNyjByacoUZQ5cr4aYhf6V5x6Assj9Ku1alnVPrl9agkZTHruKk_CJjN6DYWwFOuv7u5vg0a_nNJfTa5JSjrK2hKhS58o4ZpBpALFdKeSIai3p1lUN6fgwMrMVdcwqUeUFMhRFlXusl00g525JMuIuhylsA7qkT0oCTyawK1WDoKnPI7lOSxMLc1qPNto4YUj1d5qufKR2VftSoqio2T9_O4IJn-i6Fva5OS4wgAaILOhkO7ZPGLhzza44cKTEJMt1sFdojTjXqgcf4UXhM0okjb8IH0_z_pZ7-1fxrPiMfr3VKAHYxOn05I8tp7q3RVI2eUo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmSkZH9AXbs0XE7uTFNWWuYSHSyH_pAqVuBPzhBJcRpg_a8PgUetCamBd-qh5fYRbS1_cXoflyRpA5uxWGLLBuwJuqq7mbRhPA0yCYs1ZfcZGbZjyPX7Ipwl6H98DhcPaVhWnkrs2ubpwwCBDfznWDqCAtesIbCofk9jK90kan9HSHZkRp-n4TdR1yUCzMtDjG9jStwkhRcIin5qbPOBXWdm_71NFR_TipCtKBi-auo4XSqhP50Im4P9cEP_e7fdHsgZdnAA996m5nfDLAMdmvqonFLp2jdJegdzqPNTMWJ0T19GZJONlDX4N36yrWh-y9g29TbPBks9AQjpKjCzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEqmaK2wwIG8Hco6aEVfCkbm77x4UHVrrTLIseemcz1BlSA-4PcrLq-P4nV5g9QLS60X9yza61-GckxV9eSZLROWAeM-ukG7qJ8axzixSdn_fKoxC64c2yZ4zKDGOYoMmlN7nStbkd7rxYifBVy7PvMBOH5MHL-rPru-iFHb57ERZ26xIViKRr9Wh8Pz7etsAaFMGfNUl2Ka1ruDaKoXZmdkR_6ae7_a7NGYNcQ9qP8SU8g0SCNeVZZM0YHtYdAmpXsZXbzq5V9Y1ZZbU2Dz2mBFLTodxn0oZl4wQbOeYa8Z9F3Z8MmjXrbrnCLNuoXqxWAxOaUJFglLssaq7iOoXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucMcqZLrQZOs0VeWXEtB59_I4fp9fv4Cpe65e_rc7mzjHQzqUoiKYBnhI0XgKbLuie1Zc1_VvpJaWFRdMnhQ02ONrb4M1MkPGn_5c8-IL2MKUGnWSNkyASISwNzB-iEeAjKcM8OcYFf4_pl8pIVLZjl_juWEVxOwCqBIl3Dj0Du11vJJVJSsvDtCPplw8tOmcRuT0CNitYMMlhMLuqFie_gmuAtWK72Q2xS0N6zmxeURVtz9zTYQS9aREjTLHRddkIVUJqU2YkpX9VgJCh34zZQ69kCYvDExGYPHyp8aIsj-oMmuwq2RaxulfDGXQ9zxuzYe9wt-KZd7SgDuqz-sEQ.jpg" alt="photo" loading="lazy"/></div>
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
