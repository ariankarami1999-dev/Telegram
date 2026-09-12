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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=eldDmqOHp8xFJVQurCxXZYxfkWoJyaV28HdGPP-bUMFBZ1ktgGigTktoTkwB0mYmQZPfQt4Hj0N5xWNPyzgTf7or21djyRQbxRSSB7nm820gecN4bnIbBDqijuceKKU88Eidr19MTVwbv6UEFqMeJMFfrT81LkO93KJTSyAO-es84dsOxxCpj5T-zc_DwF-3SUakEHL9eo8qrPORPw_53vSMtZcaRfk1iF0F0oDwU2ctbVZm7vg05wHHipfc4l8b2x1rwH1VwmbcKyLP1zjIq_WsfojweubUxV03zBMJlt7aVA6e7W7FbINbqiS_kG-tDuUpwsBTeunJulbwkN2nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=eldDmqOHp8xFJVQurCxXZYxfkWoJyaV28HdGPP-bUMFBZ1ktgGigTktoTkwB0mYmQZPfQt4Hj0N5xWNPyzgTf7or21djyRQbxRSSB7nm820gecN4bnIbBDqijuceKKU88Eidr19MTVwbv6UEFqMeJMFfrT81LkO93KJTSyAO-es84dsOxxCpj5T-zc_DwF-3SUakEHL9eo8qrPORPw_53vSMtZcaRfk1iF0F0oDwU2ctbVZm7vg05wHHipfc4l8b2x1rwH1VwmbcKyLP1zjIq_WsfojweubUxV03zBMJlt7aVA6e7W7FbINbqiS_kG-tDuUpwsBTeunJulbwkN2nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwHL1gs-O5GCGE6Yxx7hD1jnc7_lXeHKb3I3KABODYP-dJMSgBGm5hD7b-uDi0ePQd_hCjfu0CVbh9_q8H8001HzkY4Iht_vrVdElTYJGq37x7Si-u2q5h1PvqhaqsuZplkY-MmRaNlduQnR3d2fyJ86uJtq6zL9vFjog2N5WDHZtlFDclV-fMEbdilLWRCsaJF6xFiI5jGuNf-3ovOI7sHpotWcdupxQe5l7ZFUgcJ_un4lYItsvXDNNIsix3Ob0I7PisAdkajS6iyVLS9MAqqD1EgUVSqJkM7a-Ikg3m-tVp2ptGhi_QzCgt4i_6dhvx3jdXMQAZknOaJm6ygZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ra_2O9Iq9fuQgBiYH5HJPYKdZRoKsxrQUH6YpWv-CdOokOw7KSHo1bQKBHgUTVf9vADVaFu31F6dsEZkb94O2yuxxt2Vbr8ZZvOTpFfDSYLDzQTl4_nfIUpHFyIB4sfwnjPH-yt3-qEsQ335gZq9eu-ZZw_hDW6yh-R99dw0nZK_wxVhoTE2mkKMFqSVmAS2-sf3gYRvQmVVjAcKmxjrR2JPUVaq5yXgFlj1kEmmjNUahFGyoseqGFEc_25YudM7_k7236Z-7YiFOgLCUpy1F9AJx2biLW2mtgpl7K7juZR2X-SOc0ibnoF_HaCogT8IltdxJExdGXp7S1UCPBmcDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Ra_2O9Iq9fuQgBiYH5HJPYKdZRoKsxrQUH6YpWv-CdOokOw7KSHo1bQKBHgUTVf9vADVaFu31F6dsEZkb94O2yuxxt2Vbr8ZZvOTpFfDSYLDzQTl4_nfIUpHFyIB4sfwnjPH-yt3-qEsQ335gZq9eu-ZZw_hDW6yh-R99dw0nZK_wxVhoTE2mkKMFqSVmAS2-sf3gYRvQmVVjAcKmxjrR2JPUVaq5yXgFlj1kEmmjNUahFGyoseqGFEc_25YudM7_k7236Z-7YiFOgLCUpy1F9AJx2biLW2mtgpl7K7juZR2X-SOc0ibnoF_HaCogT8IltdxJExdGXp7S1UCPBmcDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Z6ccG4B-9F1Nl2OqvVnHpqoxxF1uqBwYHWy6s2TubxNjvi8Ubp4nXg1lmPyEtOWHt-Q-FXt_2CINyo6LJ0bG2TMc52lizA-F2AwN8h1XWW0vaNe2EisBzS4Qt3rxrwWvr8_UnJCAxLbrHO4Ck0KbfaAQb-E86j6HuJsxemJeUQ686dElyBxxbfTvW_tBv2H3rxFY4oOWvvoGc8iy9ipp8LkzaSymJYnb1C05yv4S_3UOhJhwiyOB8enbUvkNy6_ms0_59ASMVMJm6pP0QZgoTxwMp6xUq5ZQMeb8da25iNDu3e9mH7ZqMuWCC-pXKHWSZWSMlVCYWvueHTppRJeS0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Z6ccG4B-9F1Nl2OqvVnHpqoxxF1uqBwYHWy6s2TubxNjvi8Ubp4nXg1lmPyEtOWHt-Q-FXt_2CINyo6LJ0bG2TMc52lizA-F2AwN8h1XWW0vaNe2EisBzS4Qt3rxrwWvr8_UnJCAxLbrHO4Ck0KbfaAQb-E86j6HuJsxemJeUQ686dElyBxxbfTvW_tBv2H3rxFY4oOWvvoGc8iy9ipp8LkzaSymJYnb1C05yv4S_3UOhJhwiyOB8enbUvkNy6_ms0_59ASMVMJm6pP0QZgoTxwMp6xUq5ZQMeb8da25iNDu3e9mH7ZqMuWCC-pXKHWSZWSMlVCYWvueHTppRJeS0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPWyVq_Katy1jEigTG6f5PY3H1twS7sUyxEZ_7nFoWAF1ZE0lUdnj-cIlkAp3EZJFKwoKKZixBYODLSr0y28v6KbFVMhNCenkhdaHBwYOzhQR21gvZ1rP7554UdCtbaQw0tDlARhAKH4MZ9ic2pSo6F_4bXyiBI_oyQskXdDVRr5G-nnMkrXKc01Tr0guDEBiiwJK3CE85JwsgdsgNDjyhLqdFaxjV3OxLue0cqrRU7Xi1I-ljHxsHjusrcRHc3fMshW5mX59T4-by-wGXY0E7pJcm6gML-5U6L_lg7OqWIn3HWwTpEIPgPz3hbNYT1KYeZkrNjVzkMQ4KUtPkAuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ac1ND2mQHRslu4PKWwywanXcxY8YdzZ9zcQSbuPd6pqyX2_4Hl8fkIfunaG2TYcBv2HYsRwSIckB1uIH6lIXhM_AWMKuWhiTL5pnScpC3PfjDTi-i8DvOsEi5J6zKBoncQN-AVpY80FBozEqRqieu3aNYogttCPltrpUS_8Y3TBwtFwEI4C4WFb0VLqN6tBEJP8bdKQn4yr7NBSFTpx1WY6yEXm174-kWxSqUrgbgEpa800RgRmSD9Vbq13MCYAnoX1Aun05AfDdjrUI4bmZt6wpiR5_o40jyOWVayuO3SKvjC2a4gtu7tcc3K1H63lt2Xb4q0UfcwHVVPkTZ-v1MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=H3_irZLZbbHlD-h3GXn-OnacxGEPqbnGbPd1g8Px8ys4Q5Kk22xwEs_t8bll9vhIta5SYWRfqN__vYP3Cq6UoHt32qrH77yJmvVz9zj4mJPcd_YfmfYnrYdLoeMQ3kHM0R6xDuBybjaJJcmx8Lj6Ko9Ek5-RJx4Cp6wiYP5jPYe3tJIZIqtM2gEIhYWHLpB0U8TIfWNOYZ7fgOYRLbFNNC2ZmQJoflodfVJ3-EE7p5vDULJywfdxBXFGYXIjPkzuCtThvYuBGns1Rizi6XjJ7hWl05iDJxJHlgsnJuBkooTRyPuUMSprZn9WOYVeFmVRFcAZg9r0_aW-3uvZ8bJQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=H3_irZLZbbHlD-h3GXn-OnacxGEPqbnGbPd1g8Px8ys4Q5Kk22xwEs_t8bll9vhIta5SYWRfqN__vYP3Cq6UoHt32qrH77yJmvVz9zj4mJPcd_YfmfYnrYdLoeMQ3kHM0R6xDuBybjaJJcmx8Lj6Ko9Ek5-RJx4Cp6wiYP5jPYe3tJIZIqtM2gEIhYWHLpB0U8TIfWNOYZ7fgOYRLbFNNC2ZmQJoflodfVJ3-EE7p5vDULJywfdxBXFGYXIjPkzuCtThvYuBGns1Rizi6XjJ7hWl05iDJxJHlgsnJuBkooTRyPuUMSprZn9WOYVeFmVRFcAZg9r0_aW-3uvZ8bJQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuL6YOgomZ6znbV-J8dK81Bwba7o0YZzxDqVoxMJ4x9uzG9-tdvVi23HKEfueQxEo3CYGPReDWxxMTUek6m1br25UzFTZivptsUBZMZiBxR8Uj6oyOAVImEtRAee-ZN-X71vW6h9pMfx7KVCu1S2Ru5ImZgnn7H81-EdfpF5SZscQJDsElnl6gLqYtOgO1JDhCkp7aHxzq-hpYFCYP69aeAbKJsj_DLnGoMDM7I5FpX8y-BZinnO4pNHMRHgkvo9j5ALBVy48HP_l2c7o0H9GwsKFg5cJYwnEeQC1kooKrFDhQaZ3Qz0W7FPGklBehZO_6ndc5p2b2YnO7JYAX6dBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWqo5uceArY9zF8PfDiNCEGWXmpbeJiuZKzvineVrBpF2xj0t_072b5K5KL3cdMrgnLz4c2ezvgcbxx8I52M716qwGgwNjGnzJAYsxm57RzCEerkgOzv0xRZ7EBCEd-6q350Wub-EJhb6fYitU0H-s-uCrjlTMhgr9i6w3WRTnZMR4QdZY-ldGHAoxT4p0GUeTII7ex-A4aUrHgu0FmbCcCpt4HdXcd8BO7Sk88SQXrsuI1bXZ26h33vJpvn_G0YdEOTODRTM98kmYl0DVUHy4p0LQoOCeCxSA2MbacDlZruqLoVxW1nIUrk6JWBHCvW-fkAkkCqY81JnmwzShxvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqj0muIi2zgzI0chFqIDayV9Kiu3wNBZx3sHr8KwymUMtKGMp2aJxSV8DPiEOHSg1JLccmJt9arixDH5AMouahozC5Qe5BfIDbxqTpRPy1iUtxFW6Hn80VEi3tpYgnLxNn_zGacSg_9lbnlmqGnwAiXr0XNJnOh2y0wTnKOs3lbE_ZK1Hq3XxoW-X-oZlM2zPgJ0ZU4JmkXhLxsuQy5QC9d9GVhtMLrbw96m5dQtgKup0hvoCCh73dSoKBuYG0_ChKnTCeBQppgkLUe52hrFOIGxYNOQIa_VVANZ_rxtGNfnMasM4ChIZMKZyfaRpeXj-16Eg_hRqpOBNrr8MYt1qg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=I301h-tWPnEL9s7mPNJxQ73QVvMc7Z7Tcn4P0V_NNk_gFslmpRIvkwIksk_Auc3phoVCfml-fp3HeZpWN5OvxNZxSNzhlkwXi1W89kAYtq_3jB4ndZgg3MxcfS_wDYfK1TS72Z8VB9jIwgRcma63Uo9AHPrYXjzp3t45QiiRSgD-lSm05qhp4x68GyQTeddf70V2dkwqYr7I-SAZA4FjmI7q79VVemqgdrsBva5GCj-BG9aolMUGLNRZJtX4SKrPW3s1Fkj2W5NeDqcii7I6qZ7xADVXc-bibjEMJi9S0VBpaP8SunR-mEx-JqulUKhpUZVA6X-qCv0oWE9GRYO5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=I301h-tWPnEL9s7mPNJxQ73QVvMc7Z7Tcn4P0V_NNk_gFslmpRIvkwIksk_Auc3phoVCfml-fp3HeZpWN5OvxNZxSNzhlkwXi1W89kAYtq_3jB4ndZgg3MxcfS_wDYfK1TS72Z8VB9jIwgRcma63Uo9AHPrYXjzp3t45QiiRSgD-lSm05qhp4x68GyQTeddf70V2dkwqYr7I-SAZA4FjmI7q79VVemqgdrsBva5GCj-BG9aolMUGLNRZJtX4SKrPW3s1Fkj2W5NeDqcii7I6qZ7xADVXc-bibjEMJi9S0VBpaP8SunR-mEx-JqulUKhpUZVA6X-qCv0oWE9GRYO5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=aqwiaL2U6iAVA5GeuM58e2baLCI77Vk2esdEYSLZpyy3rJ8rXMaz4wkyjG_xC2Wjz5sfYEBBAt3dKNkgVXdAnn6tUdtvDXFyopMrtYWa-vJUB_s-2DOArAM2bj1CV1MM1rmcVy-McPdh72gko09P3nBsBjT7qariSJtcXZPKsyS2M_foLTgqu-tkmjPRFcU3qNIjN8CvIv7P3IRMqpc4uZHFyK1caa7b00CEOgAAoncLmUzzz29YTbIgww4KGI8c1Qpx7AzVaWQRM0Szd8VslhEDma9twLPR6c_VuFfkG08LQl-0dJ_-JfmfEKl5V956_T8v_IVV8YxrzJAtO3tyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=aqwiaL2U6iAVA5GeuM58e2baLCI77Vk2esdEYSLZpyy3rJ8rXMaz4wkyjG_xC2Wjz5sfYEBBAt3dKNkgVXdAnn6tUdtvDXFyopMrtYWa-vJUB_s-2DOArAM2bj1CV1MM1rmcVy-McPdh72gko09P3nBsBjT7qariSJtcXZPKsyS2M_foLTgqu-tkmjPRFcU3qNIjN8CvIv7P3IRMqpc4uZHFyK1caa7b00CEOgAAoncLmUzzz29YTbIgww4KGI8c1Qpx7AzVaWQRM0Szd8VslhEDma9twLPR6c_VuFfkG08LQl-0dJ_-JfmfEKl5V956_T8v_IVV8YxrzJAtO3tyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AQDkdWJqCW_IDldEfXibb1QxOqOT8df_HdYXekm_ER9NKINibeuSdOkr1ilQX4tsoP0xS2xaIwMRf1Iq0DBMVNCRVXliUJ0wGZsbtgpQr8UC4aWnvb3LV-zZ_PN_DxBO14IKwkD0DCtyNGT7zgxlZVIdH6sX-eOrDQIUYxftlnHMwOPSIoCucq4OpJ5VEA1IzNn1yYaFgdbfhbTx9YKsgd2CSmVpWzqMeB29v74csyf8Vk0nNLYGpd5RkkzEUGWn8HdsLrc6OZWjxDT5lg5EYBxJj4cFhFb9T0QkRYDZ6PjJy9h2n6nTBeWgi9VORMTIwcDRyDPPfJhyUe7hfM4tVKUh7LE-cFF0ZPc1vCa8sy0XWzcMmoilwZ1bebPr36-117lSHm-3JAagTd82C4yg6F6cFNFRCXMm-QVM3KGU36LBtl7hA4gl9bdpHejmfQZvVnUk_dGYiTINE47HQoiucFbW2f3t_4IwfbwA1V5opDftnaMtLK4P6MrOQ3tf8WWu-yf-vZs3jtM80HaWXUCu-Ii_WMcvjvOJmDMkCsZb6nvMS7mZzFqXqT7pr5478hUhfVaw9biw2sy7Lz3MrTXtrqgkWgWQijalWu75m-3zEW8-gz4usoMMKq591ovGtXEQOHmdLFYQaRbQEEx88hmFgapOlEMkHESox43GUIXn-J0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=AQDkdWJqCW_IDldEfXibb1QxOqOT8df_HdYXekm_ER9NKINibeuSdOkr1ilQX4tsoP0xS2xaIwMRf1Iq0DBMVNCRVXliUJ0wGZsbtgpQr8UC4aWnvb3LV-zZ_PN_DxBO14IKwkD0DCtyNGT7zgxlZVIdH6sX-eOrDQIUYxftlnHMwOPSIoCucq4OpJ5VEA1IzNn1yYaFgdbfhbTx9YKsgd2CSmVpWzqMeB29v74csyf8Vk0nNLYGpd5RkkzEUGWn8HdsLrc6OZWjxDT5lg5EYBxJj4cFhFb9T0QkRYDZ6PjJy9h2n6nTBeWgi9VORMTIwcDRyDPPfJhyUe7hfM4tVKUh7LE-cFF0ZPc1vCa8sy0XWzcMmoilwZ1bebPr36-117lSHm-3JAagTd82C4yg6F6cFNFRCXMm-QVM3KGU36LBtl7hA4gl9bdpHejmfQZvVnUk_dGYiTINE47HQoiucFbW2f3t_4IwfbwA1V5opDftnaMtLK4P6MrOQ3tf8WWu-yf-vZs3jtM80HaWXUCu-Ii_WMcvjvOJmDMkCsZb6nvMS7mZzFqXqT7pr5478hUhfVaw9biw2sy7Lz3MrTXtrqgkWgWQijalWu75m-3zEW8-gz4usoMMKq591ovGtXEQOHmdLFYQaRbQEEx88hmFgapOlEMkHESox43GUIXn-J0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=p9RBvLnsO0se5uQWN2J9tZBIgcnflQrcz1DdWSE1QKlOUgs4-WKBzgIdNIQtKiEnnP7ZphXXeuCOPFH-iDC_EbC1y6B6gpcx7dxhAS_y0rl4VaktVsSNquUAmGgYLZBqHgINmZoLjYWb0Ad13zc-Mqw1XOzFb-re1g_vnXW3QsS7GJkATRK58ksKmoTJvEi8ejgtHjMejpwIGcBDaxdXpFV338YyxcZvFtxGbPbhL7QIEbRYNKeYTRGMBkddmD9Y5eMWbDAkpYIOKqtz30b81zFGmCJQFJ7ar_I-avDhp7_5UiLi6rYlMf5RZ0htwCOt8KIoo8Lp2splO64XRjgmVDPtfq9eRuKxEh4jvuIBrsSGBj58I43NgRwrzG0ulgnR-4Q_Zoi65lLSmjo9JhXj_jRAkHFgPP0QQ8bi8HYSvwVb38clICPq0bMiY9Ew5wGKWiVPIJQkG5Qe2mEiUMP8CaD0ZGY8uI47163QGzyLZaheKgZg78QwemYgNANcMJasCnGq920m_0TmOav9nOwUNlANw9ZkEPw-Zm5e3CL6b7k6mWpj-T00ZxWhjMSgSM-rMHZJRfbJpfe6rTnhe-Lvo19a7KVi8G2AzdkzKjTx7eriZmBC7UGoI9_0NUEMWbu0cf_XBPkQRYd5zC89sWEu7Fg-Wu1jX9Sn07yzBTbHjxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=p9RBvLnsO0se5uQWN2J9tZBIgcnflQrcz1DdWSE1QKlOUgs4-WKBzgIdNIQtKiEnnP7ZphXXeuCOPFH-iDC_EbC1y6B6gpcx7dxhAS_y0rl4VaktVsSNquUAmGgYLZBqHgINmZoLjYWb0Ad13zc-Mqw1XOzFb-re1g_vnXW3QsS7GJkATRK58ksKmoTJvEi8ejgtHjMejpwIGcBDaxdXpFV338YyxcZvFtxGbPbhL7QIEbRYNKeYTRGMBkddmD9Y5eMWbDAkpYIOKqtz30b81zFGmCJQFJ7ar_I-avDhp7_5UiLi6rYlMf5RZ0htwCOt8KIoo8Lp2splO64XRjgmVDPtfq9eRuKxEh4jvuIBrsSGBj58I43NgRwrzG0ulgnR-4Q_Zoi65lLSmjo9JhXj_jRAkHFgPP0QQ8bi8HYSvwVb38clICPq0bMiY9Ew5wGKWiVPIJQkG5Qe2mEiUMP8CaD0ZGY8uI47163QGzyLZaheKgZg78QwemYgNANcMJasCnGq920m_0TmOav9nOwUNlANw9ZkEPw-Zm5e3CL6b7k6mWpj-T00ZxWhjMSgSM-rMHZJRfbJpfe6rTnhe-Lvo19a7KVi8G2AzdkzKjTx7eriZmBC7UGoI9_0NUEMWbu0cf_XBPkQRYd5zC89sWEu7Fg-Wu1jX9Sn07yzBTbHjxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=eprjO7A1xm_GVxxXsF1jr3_9qKA0RKVZrOzKXyvS2pKtneWV7xFKvh29QvAHuWjn_bYZlNhI_vqOJm5U7TzeNfvXwYcSsPx9qawNKhktPXQ_Qqj1y0PFrEMWPoB7b1EjhKacbnDm_o96xQkxVsW27caD1ow0lAiOivDYUNkck26639-37ZyytNWPn0a9YzCjFpaXdEKo7Az2R4FoyQIj3FChqRaKFmOnFz_rt5MRDjq0brTcNPdY44hjci23GYjfGE7Q6Z-NgKPoD2-EE42LmduhSk5nqIeJcJ-0A6OS9ndZ0TGUbrpWgoRlmatKTF8lgs4RU3ih1qtLMezBRG-TTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=eprjO7A1xm_GVxxXsF1jr3_9qKA0RKVZrOzKXyvS2pKtneWV7xFKvh29QvAHuWjn_bYZlNhI_vqOJm5U7TzeNfvXwYcSsPx9qawNKhktPXQ_Qqj1y0PFrEMWPoB7b1EjhKacbnDm_o96xQkxVsW27caD1ow0lAiOivDYUNkck26639-37ZyytNWPn0a9YzCjFpaXdEKo7Az2R4FoyQIj3FChqRaKFmOnFz_rt5MRDjq0brTcNPdY44hjci23GYjfGE7Q6Z-NgKPoD2-EE42LmduhSk5nqIeJcJ-0A6OS9ndZ0TGUbrpWgoRlmatKTF8lgs4RU3ih1qtLMezBRG-TTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwdXpgwnCES9Z3ZwRd6GV53RA6MDzYe6D6xYNQsIBB4gGirsbDFhMBPaQ8rZ6cULVoB3U12SfS27YbWlPxd2oZO8EZtu_ze3dEFsOdBqb4dMp4AP3EjdCuyk7E1w-yqMmb3UEoiTSvpK6J5FUBXWsX_xr0BlZgyet3A2olyZ_US5HL2zAzOKrwX3cHYrc3D5fgdNqAh_uFd71Q34hkiVcAsYCg_ekTOUSyVVEXzNHcd-swiGT9u7_xDq3XgLW2n7WU5pvoO5SZLIyKDRKhFVz3QuCnpxeK22rxmRp441QjHRpkRFJB-mzy6HSy4cUB0Hdc1mXyZN-Sx94lWRzKVw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=agmN4IXxeFMPrAiLkr6vxSyZyAdkl0L32-GZNNakdF_Q9PtZAaje_jVXHerNTzuytfOPmdyGMZXHbn9uVRjzUfKDsN40eAltibjMBYD3SIHqwY5VTfl4-uSwVPSFXQgBkxX18xrW084NB_JW0X6eOzq4sLQeN6LqAss0lxrr2zogNxOOa_5UFNyZ_EkqmoIo5cwL4MYFVMORxHmtoSeQ9x_Hnj9ZfTWangbYs2AdE_8qPmMqt2Dz2Xbo7ODfUzFtUreZIQsdZQccY1iYREUscdhU9JWw34Zz40nc7dGyZUhJLPSSGU7qMtBReD7TNZagwpast9kOSOvqGZNog1q-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=agmN4IXxeFMPrAiLkr6vxSyZyAdkl0L32-GZNNakdF_Q9PtZAaje_jVXHerNTzuytfOPmdyGMZXHbn9uVRjzUfKDsN40eAltibjMBYD3SIHqwY5VTfl4-uSwVPSFXQgBkxX18xrW084NB_JW0X6eOzq4sLQeN6LqAss0lxrr2zogNxOOa_5UFNyZ_EkqmoIo5cwL4MYFVMORxHmtoSeQ9x_Hnj9ZfTWangbYs2AdE_8qPmMqt2Dz2Xbo7ODfUzFtUreZIQsdZQccY1iYREUscdhU9JWw34Zz40nc7dGyZUhJLPSSGU7qMtBReD7TNZagwpast9kOSOvqGZNog1q-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=NsBpHdEdGTsD1hZNtHJE5woEbwateVdnFs_XcR4tKy8xyIsv4Aka3pkuXQoRWzws_rcrm5zzhyTD1UU8-gidv5_w6yTRuk14ajWr3OZ3laXwVGFR3tu_omdBoenT3uXyuUpwdpz_voF5PFJRNG1CR8skQTI4_vKlXrDUNZDbtye580zr7r3Etwrnj0ofa4LUlOxqkpJ2hHhOf37YZeXgNQCHrSfUvGD7BGACyjoDiPbOaggmZrpCyl3Vfx68eSJuheMNLnQQJWpiLMDofR4dV0n9uvTfA2JQlB-uihj3oFHSrE2sxYVXqd2M0-uJZY7ZI2zHsSz5IVZMlsArBM8uNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=NsBpHdEdGTsD1hZNtHJE5woEbwateVdnFs_XcR4tKy8xyIsv4Aka3pkuXQoRWzws_rcrm5zzhyTD1UU8-gidv5_w6yTRuk14ajWr3OZ3laXwVGFR3tu_omdBoenT3uXyuUpwdpz_voF5PFJRNG1CR8skQTI4_vKlXrDUNZDbtye580zr7r3Etwrnj0ofa4LUlOxqkpJ2hHhOf37YZeXgNQCHrSfUvGD7BGACyjoDiPbOaggmZrpCyl3Vfx68eSJuheMNLnQQJWpiLMDofR4dV0n9uvTfA2JQlB-uihj3oFHSrE2sxYVXqd2M0-uJZY7ZI2zHsSz5IVZMlsArBM8uNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SekQ-En51ZPIU1jmhll5tlqPJHWg7qDeiCuor0ZO0J_yBnKXBpbcbka0NHFj1C-t4kVBq4jkT5ku7_ssfrS-JryKKG8b5bVj7qmDRAZ_kNtD6kxJyd7UBekftcaiIa1zJbuFLfhYw-6qr6Sjt7AbHG-38c5gMHWeJ5FuEsv_qtpYXZ-R3fMiFh0J1FkP2mWXiKWdVYClKQEGYhV4JDc9-rsiNMY8hSrtQrWDIxANULtHJGPer7cUD0dYGpXW567S0-gwuyXD-oaTtVME9MDnup-HE8YoF4PtrNEs1Z8JJE4Y932jxTIMBtsSM0uFrW7LqeAZLOZGlJFz3O6axI0ZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7gwndh_domAqJEv5bndjHkEQFOQtN8vkn_00moPehF2bSa-Ghmw2wW3S6lhey0ReEzeZY9XGAGBrxmSeDHV1Vd5vzopeXkVzkPD8fbhX2QOu0yJ1a8abWln3gTZDEXoqKA78di-EcfRTC2MkPRZ5wdjAIJ8-4yp_Ek_dIpPrBgOagKEbHIMumeIyWftaA2FfJwF0W31VTu5OFOhF-EgmtqIPpUN9b9T54FXvIJetHOZxBoCDHeIDqukiVm800R0emRhze6e-A2Ze2dil89IfYdo3ZKhySJnnkan9PRE5YjXpnjjzOycHm-Bqdpp1EDxsG7sRDfREMKDKPrTLRDjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipfG7QWS6Ejp3lV-oudP5bvcahfE1pEQaldgvOs4GozE5riXo10LTjG5ilXyneFU0XCx1KK3yuRb97XYNmSoQGsFcrujNT2K2ys-iB90H1oqCZDDdK92-tfgTTw-4Wc3ykFycmNfkMi09QKnESA3B7QH35_2EhO66H4MS853jiOy3Ka4ohsdGVD_sG-oAQEqnMsI3xdM0e-eLHcPi9CDNYZzYK7yHdwS5k_6mg_-iEbxBVv9VjTcTFF3roo_E4P8nAZ4z4zp2hBCKw2-S8SiGB_CbDjKgzqvHsbRqPaEOUDidpP--ALxLT98KG97sBO7D4Upt36d3lizpcIQud582A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR70OCDCKwGRPxkAjJ7UX-AjVg6pu-8CbXZJ9hPTdtmCDuULiAW0xwLHZ8BBzVJrw-wLSLcu4EcNHEFn4GXeTKzU0BZHgXMg_nsxdwypBIdFKIEEyPuI-Jlf6HWRyU7Q2aCzBlcNa06LqEoXkk61PhverFe2aC4fDEbXPRMx0bRMO3682aJGAvHim_vZ4mwel85dl-ScCKAOgeez26qnu2CBO8lfvvGmPpyBvwPquD9pxQz_pUAQEyShdDl0XCvMkuGdlJDi4e1x67LfwrLhQDWo9t83j4OFMnG4u3yAWiKk6fQGD15q3tediS29Qh7otNDv2lcTPgu2SCqYxrI44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reoopMsxzecDP_oTOWPij9ach6FZnnpdiwAG9aV4IY4EMdLOIoFO2WRQkPL6MqpcTVFfBvpAB99wBikV_muW3EWgTIOoG2CF5C1qexLL0KnHeYrfLD0s4jiUHqDW9eCM6KSJRbsWi91n9pc36zHS4aogB3xKyKADjiMQLpHhjeovm3p8-UOOzldq6Nc3qLEXl7RibF2Z_N6A31tGd1KrZR5t4EXdBQd45jnm_mI_iHNwLwvzyGVRXcL-_8VcJlx6CAMn_gIerxCjdx-2s1I31QknKFIf72A73xPVIYzbRPfCF0Dy8WqhOCnj8cCaCBnET84JibRzlxPgZO9k9G41Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGF3j3Qh_dyX6bddGQp1GWVAirHvTYjnXoCwaGj_Dw-5RCwbQkF_C9E_LxXZXVYlRIK91155n4O3HQhB15o2674BlWGRwbxMoLo5hdTzAPIMx1-CX8AiArjzFEMJUTiVxwlXMdeVm7mSxUglWf45Y6wx0vC9Nd5VDmcluqmvYLdTTawISwW101J4JE8fLriHk2gmaRuWNPu2T7D9MIzrE9X4m9GIFICJP89Z_gT6yMDU9Sz8Bouyomfzhbp0fEcdLjo5eTxjGhFEFzdKAXtqc2-m_Pr2qSKdooUrqnfW4f6yb0WpikQYv8vW1P18LyrSLZL6w2xa8iXpQLyasD37iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6fozS4V_EXDab_OpgsN0gAQbuqPjGTsuWmg-tIPl3YkuHlecN6GvyXQ6ktNDQJnDT71keuUuedGuJyxrk2znj06VN0uoEHtW8K8UE2Ld-o5heAAkWYWxAAAExL6M5SW9NMZ-iQBmVxUMOcLhsrxTFw6irei6aOMqfoA8uT79yYoSkEd-l0PghkEsds4fwapqjvXBhSCSWf25CTQ1SdSOrkClUx-JmsklgQfhAPz0hVs94wjajpI_ZBTi5SXmGO5wnhCf-0S3ei27l9wjYdylzJFDp7g0lKLToUNE0ZNZPEbcSs8-JQ-KVpy9RSJ2blppmkFcpQKnMO3Z2r5xu_Zug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7yzNd1bTnco2M9D26_ZdqmibaKKWdgdheMaLgNxZcjwAVScAUO9jjIisX5e30wlRPijO85s_Gn7rMqUEJQMp_8mFBfseqde5Tj_dI7UuwKIhXixBa8cpghNm6AkxkMeUsWYBOPQnVIs3oiDSuqeEGzC6AapVq1_B0K2KADmI_Nd8ZB_bA-1Z2fghSdUfbDKiYHs31cKGB0K7sZXgKDqJKiiVzg51zH52PFZGGkeAKIKV9TzE-6J0Av6RcEyDtUfLPKp_ovzvPrnsDflb4bPdoLAWjgBMHhbnihbnzfL_g1MKcgipC3exbu63WK9x-9XyctQu6GziZpdI6qfEk4f9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNGgoZMEf1BSnXwcs_6dbDZyT6FmDw7VRt3mW34h-FwdjONZfVbplcKQUcCmDDPhuYMpDB8hu7S4oDYYxqXRIJ0Xd1PcFoWG9V_Ap9D-S7KMqKYMZF6LgMXG-tNfE59baJ3NFcFub2NLH5vfjeyUVGlhGnTkQ5yhiKHesoLQjR2dGhBpNHlqn3f2OBzyZJneAU0nqtIoDxIFnxXMrN8wR6BTlORZA8JL-p-aG6VDXNeBkMjnyEHkwS_yjwNkc0lKGl65uUoMTHwj-zyU-SUqUCNYPFi3LD0dKu2KhEFexWYqzgiRFJWGNfYSSWfdbQRl9g-yR6m-4ji2gnFmL_FZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJtmiCqJyJHjE5tJGYgPl75gFI5o7p6gI0ztTX13m22WrHAShkPXC3di_-DX3eHViIL0EJfgwGHxM5plbcV34zQa0N1X5n6uOn9BAU1TL7OVQRURCTcFV6rAYA0R8DlPACKRaHNMC1ThG1HcrRKZ_19QIchCSMpbY6ns_cHJSfQlvMxZun2gYpJtpfTOd-3sG7P5ZOSfuFu4p0xTlmnET7CjN7LMBclpCdsvzUe8U5pGytAwzdqXcLZ0niSXlCRhZsBroLdxhQeED9B3OU5doCqkj0ILDysIlGQMv73QHjV2Uy8sKsx261lKQ97uOhMxZUPHBN5IFpQAH6lhkHUVbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GHLnO0fnWMCIbIu4sytWHdsAz5-Ync7Bqe9WcTjAjShaP6A98i6J5ol5oIeQddrrwSBGkLKxct2OdtIT5A5YDxxmPDeI0bBV2QmjZtnkOPqVDV36GmxwL3xxkCGUF-iYyrtfUmlmqBAhfnEVeZ2eXpdyx18PIsH2bUQ-d2dMl4ZCIT6u4pRg_h6TsQlt8Z7Gmnd2vechw5Y7Air1sdlg5jYgvVDPz6q-vMR8Ug8xNs7PCiIKD_ZVbaakzCEQ2pzC1jxfzJKomUkYI4HQFDDSP-wRR6B_oerfIKRuYJkcYvlNrRwfR-xwWEOglcQDJKBPVXVJqcWCiSyqUwG89lY2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=GHLnO0fnWMCIbIu4sytWHdsAz5-Ync7Bqe9WcTjAjShaP6A98i6J5ol5oIeQddrrwSBGkLKxct2OdtIT5A5YDxxmPDeI0bBV2QmjZtnkOPqVDV36GmxwL3xxkCGUF-iYyrtfUmlmqBAhfnEVeZ2eXpdyx18PIsH2bUQ-d2dMl4ZCIT6u4pRg_h6TsQlt8Z7Gmnd2vechw5Y7Air1sdlg5jYgvVDPz6q-vMR8Ug8xNs7PCiIKD_ZVbaakzCEQ2pzC1jxfzJKomUkYI4HQFDDSP-wRR6B_oerfIKRuYJkcYvlNrRwfR-xwWEOglcQDJKBPVXVJqcWCiSyqUwG89lY2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbx-gAs9xpkzh-A0FfJ10QmzRt9_sZ4yr_WgOkLPWnFrgNCpmJEp9FHQr3zXyiKspPvqXmZIJG-jgssl77i1IE4whCWBF4WQGZmOQBcqu422J0TQiPNoFWA9mAWWWMQ9oKMtQbQkjDy3gaCvH9hK0SK5fw1bQN3Aq2HjDVitPzEm1szsubkCctInG4pJ86YqQbTVTIbV7RjTtHHGSWux_w34DBXoKy9lgsq5P1iTsYiC2YoWczxub8YYZGr1w5iHIEP-MLe1UvQEiIoalH1b_KKFUiQ_YdzIqTdhgQvLD1yKz6OHBxbOtyBiGx_W_h349pNoaCLYTjU2djygqM7S7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ72zP6gkhK1AbcAgBVVBrMdQ5dlzFFeFrUu7WO0XeTCnhpwSQT9YRevdPQ55amQhWozQ0HQkc5o1Huf0maJobNO0n5VFXqk02phYCCG3YvlUKURCVAfz9cFEZwAk-PluhCWERLa4rU01jn7oh-UvWhdx8vQ8d532UOTNTKJ-ZWEOkzWD6WPxDIEb-l2BVUvqGHDTRwxQEVoN4O-7XdC218Jv7JcF0tW20IOuGf8-p32_wv0IYtgMiHdpRcqMwGW6amJtogML5VEDwLqILi9Yle1bCJ4ZADPUCnHqnTQE3e_Um7c-w-eudTnQkUxTY9tN41BEEmqDyUGCIxJjZ-1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=CXNnhptthVxyGg8e3VObi8CWkJjocLdNxd1AuEQfOj9zbqhRSAaM8MqQWrDdKsbYkcW9tKtgbhULktwEKQB4nhA69R0jM01y2-MKCnBDn2Zr69WAO4e7b8FkMO4bdV4HnNk5olunYc5lzKvAy7BfBoKINsmFLQbF-wAMhCEZDStC6QXiwUN1SBp_sc8jPR5pCrziX6LfgI2ddxMM490nS4yEWuGF2bTimXMu7wEjJPkGiiOyt2FBx4yIO3rwI10gxvusLq04gwNjEigzs8leZ1hUCjRglwJC0aXQgH3ucqLBNWw-Mng3QAOUbyhKMpkTOvlCbMtORCOY2M8Pyxbn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=CXNnhptthVxyGg8e3VObi8CWkJjocLdNxd1AuEQfOj9zbqhRSAaM8MqQWrDdKsbYkcW9tKtgbhULktwEKQB4nhA69R0jM01y2-MKCnBDn2Zr69WAO4e7b8FkMO4bdV4HnNk5olunYc5lzKvAy7BfBoKINsmFLQbF-wAMhCEZDStC6QXiwUN1SBp_sc8jPR5pCrziX6LfgI2ddxMM490nS4yEWuGF2bTimXMu7wEjJPkGiiOyt2FBx4yIO3rwI10gxvusLq04gwNjEigzs8leZ1hUCjRglwJC0aXQgH3ucqLBNWw-Mng3QAOUbyhKMpkTOvlCbMtORCOY2M8Pyxbn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=T7Ijw4s5pUAcPaNnvn_NywytN6NHYyao2vbVuokQGSCStiHsArki7uaGmTkrrrMic0zwznTGW2rq2iFziUJIEjehp33oCgtZkbuufvuSxtxoE_9Hh7h8oeQpPT_z8jWIUZdZIjz3bDeSVSMUlx7CxAoaaK6y05e1DD8UjMCRk5wNSuLmgiZ142TE9wd5yaS-Q5lQVs521GZbH-VrtsrOIxWx2TADoB0r4OYJTgpWUgt2LpJ72fuvDqlmaEzpQwl0Oj9p7M2UbgaEiIfO3cN3ccrIvaflW3kqD39dwwpnP-0c2do2tEy64bmbFCAfg13U8cmz2Lw3zMogOLkbXwg_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=T7Ijw4s5pUAcPaNnvn_NywytN6NHYyao2vbVuokQGSCStiHsArki7uaGmTkrrrMic0zwznTGW2rq2iFziUJIEjehp33oCgtZkbuufvuSxtxoE_9Hh7h8oeQpPT_z8jWIUZdZIjz3bDeSVSMUlx7CxAoaaK6y05e1DD8UjMCRk5wNSuLmgiZ142TE9wd5yaS-Q5lQVs521GZbH-VrtsrOIxWx2TADoB0r4OYJTgpWUgt2LpJ72fuvDqlmaEzpQwl0Oj9p7M2UbgaEiIfO3cN3ccrIvaflW3kqD39dwwpnP-0c2do2tEy64bmbFCAfg13U8cmz2Lw3zMogOLkbXwg_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVdx33kksMn1RCHKnMzo0-AhysW-DX6ob0Ya93dnRglvjobPJAyqtyHgMCLKSkzVp_3tI3WR2UZoKZJfYhcM-NM87scePfefuZBR2-C0jA0q3p2wyqzTw8TpZaeK1AhcjM0zRRGC9X_EvByuBCsTSE3GqxYFO-Xqc8hjAf0zv9t5qLhep5zWzulUUURPBnBGFdVS30Tc9lKeXgVMm6p17ue3eJg5Ou0IDK-16T6jp6vuZ1tLop4HHeOzRYCj7y5S9AwjZM7iswajMKreCAYhackmvJC2_2VWAI-ANPYyylFATrLTfYwgG5QirgsL5jlvSp7QXTJWJ5HrzO4kNL4XWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKr_1z5_4AbpOtZ4Eq_SlPL3mxp3n5hzIiT41AQlow627AQ3g9rmlogmMCKA8vAMgXATfv59rCX6pUzgp00ZwM7Z1hefuPzEnBVZxA_qJ4m7_7g5ouxryiBxydVkBqzR4WO1TSyB2n190lJ7ASeu0MOtfwEuUfs6XXnj3lur1mQMcsj_sCesedDk1c6hdF1me6gsjupy3wvguqbmP4cvVIj1VqnGeVBPOGPBuKS4lc7AJk6JDdha0Fpt3C4J015Os-WaYGpkagmzs28TLsXFcxuQ5cez3cr6vCrrwbYd-_pUnBEwDN-R8Rx_vlqoYA-rGJ9LrHz6R8HTmjbO57aNSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J27pTCOrkaQR7cketYefUDb-yNZGJWM6vbkG8xOjOttN2j_vQ_oXxcFgfHHHMjcx7myjbqKqa64U3d3ZJAHSPMKUbcjpJdIKg7xC8gLTLgfRIMpO_nAINoEr_ivPkzSGNj4Xm_KNw7B-VwaDJRS-ffDffxADNEw-REH40I7ahKtcormxta5RmCxO2ryTNP5yqFRO1ze2hbl_HKe1TcHNthe5H-xt_eE_DH8_I2c9Y_pG-C3VEHUtdWjOgOcjNLTk1rLIhY0DLXK0IyTFtswyA1JkUQGilA04b2xF67skfq5dIvlypGaV1i-NLhW-HggIJru9ZOmmL8P4AQQnVQH5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-uf6u0o73QYmxSg1LLhNU1CAHfjD6QCh3SdXd8ffwzsdGBcEm76szsvK-Oj9etL_LNTbMITUt8Ua_wfGWKkkiVuo6gXFVPZbxFDjOcjUgd1qhwyF0g8WwIJiXKys0cGuFkTiSEaCnzeKwZXHtL203gn2Wi6yaqufyRIZJW4XwBOREQ8frbLQBzGi4eK1r9coXYmxVi2mpSlh7k4I6qxAInjTI7eAUnQImZ1ffKuozF6NKMNBYT0u0gBg5M-X7-4AxzZig1aXkLxnP1rVXZlBTywcY85P8_vZOI9BusCyLEJmx7pWdS1SsK2stTGKyaWgv1-l_ScRm1dHbMHaOwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4Pk0C97G_-Q-_N4A5Y1my5AAvfkpY9AU9UFY-G3aIsjR2yvfnguBOykOPW_uw7YMacZ2MEp_j359g-T3CMe5kej3l1akVy2Nfr0C-RTdb96I5CRVfGYPbzYgCIrNWHMlUQfYEAQtJ5Efirj5wZoe8VHm1O-m27bOQb7sFXRoqemtcoHr7o_hZFRhZXT-v09Hrz-2CeI5n40cjjXy6GcaVR0BQwDWhav8dEOVFhiDHrqyfTeWwJY5a1IPBxDSHhpHa09PkICWQdpNnhVodXDp-OrfMrQhOF1FFYfP2yBLZ5t89rfIONAoTC24gbbPRLzUqlWmPKUQ22W04ucZW4vIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhmV2sooKUZpH2kzGK7B8chIVQJnB4Z-jaoqEulo2CaSm0KA61ebjv5dbCYNllLWhfQ2DMCPkYOU8O-pfcx5ybq_mKcRrhzJeZTU29WZhUY_TL9QMZNnXhxoMJndBT2FgbAtV3oLnBwHt_Nuk29_a1ZvFLyLxce89XtlA6SFJL7YvXoDeLMG3tEFL8JEXnVoS4mSrblk3CbNHwaSB6W6abYSoWKEOBv79cnqi42-aGXPL5ZtrTOfUSGiWW78cMtgOY-FsrMZ4A6jNL6b5Hqn7aqjGjfVneqivwlV-gPkm0_XbN-nS9WltkzdeuuF3TfBbemVJ8-top4V8W8CpNAxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaFyKN6MJ4uUZgINPoWMce2R7TefSW1gKrW3cUDWqhVwzS0flkJ5-zeatqY6xwgrMPBOADlUXjN3ldzXqpzw8fl0H1mhkpE9jBYnIY2fiQIQ3gGzHFBWYUu27rdDzxDHhVLnZwDyaNNRrmEf-DZ09rBI82ITM4hl1ITinfB96yz9yOyd0Lq8hnDUxBcE4JWymaiAw4ICjDJiG1ir9hU1QYH-d-Pf1APnWyLAGA8cwDxCCFLKwwASIzq0Hd3Z8RWX-CTloOa0s-HRp1Lhl0IISO6xSoIaCP3hvALdAOvuqnMloU1fuZ1gO6mgJyuT-PTctZDfx5WvVEFUmK3tNHHa9w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=ISsgk629ALGTABhkkgF3vVzsXQ6hg1gT9Ue8-s6u4GVSV4uJVaxSYSqSDv-igxrEIHSIGHosZ2L9lrLbYTGs5ZZ6-6zhnzk19GrUwpMwq9l3t7EQnWoRFtlLtSvhi7A_G8vbkzu3jTincQzGoebhtYZ_rFQk4yx_GVej2bxd_L_uZrwdgxUH3T-g50KlWXbMZ-rh7zUMD7c5t8y2hk6lzRCUTxDhjRFlwKM9n6gHjLuiSo4t-vXpAOp2IaKzzf7RN03PIVpQPK36kv_Fc7CAbgqJMFHldP3S13liKo4fo5g8n_TSzMcRl2SVyHTmcuYDVes2Vj3n0FUtKq0qw5Aj5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=ISsgk629ALGTABhkkgF3vVzsXQ6hg1gT9Ue8-s6u4GVSV4uJVaxSYSqSDv-igxrEIHSIGHosZ2L9lrLbYTGs5ZZ6-6zhnzk19GrUwpMwq9l3t7EQnWoRFtlLtSvhi7A_G8vbkzu3jTincQzGoebhtYZ_rFQk4yx_GVej2bxd_L_uZrwdgxUH3T-g50KlWXbMZ-rh7zUMD7c5t8y2hk6lzRCUTxDhjRFlwKM9n6gHjLuiSo4t-vXpAOp2IaKzzf7RN03PIVpQPK36kv_Fc7CAbgqJMFHldP3S13liKo4fo5g8n_TSzMcRl2SVyHTmcuYDVes2Vj3n0FUtKq0qw5Aj5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwkxpGx71KJYFudRpQB5TVKVhC7qDg2aH60jZpb6oTtG_aHqHYBnCiW65NV8YfIuTOTQDgSfaJXBqZI-6bmvWxzkf2lkyo5yDZ4FHUSFAZm0zSwBvtz2gA0Wf5Zi0eBflnMdUcQa8M3evZFCxqfusc1V_QWaT0f2QB1R4o1R5oVUuDgVqUmdLlRIUhNdMUHjFkQ8jtBq8w5cIz45XdYVfsG55WWs5tZ0Fvj9IY2XYdncz7-AFEHDVJZQJk8MnnmixAZU9DrzeQU1xPcEKLmnzDGSVOlWWGfgO6TjpT9ntAndAZqhaeug6TBcrv8WksihB9fw4YeLXSibcXrrxsW3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=jjQk6yZxa2y7aqXFQKoRTxIuVP4jBp1QA4_gMDtG-EZRS-CUlzfEpK_CIRvme1avNT_MJwc3DjbRdNPnFX6BNlLlg3LMPAZkCDS_1T1Hl7Q-1V6kFEK-m8JhOOWqJXMubLSpe7xtJA-Smf-F7szUvBL1cxC4IGOK056WC9cwuAhbgWzHqMQzs5Y4ltg8qKhj2nR7I69qCWmVUZPVQmdmiexX3uuted3B4_wYGWyf56lvxDXmYiANT8_utPGQRaPtEmX0sPeHNJFCugSu6ddtMnm5CHipPbDOeVduagtszQ6-2zXfHmdoD3opeCnoSYVbXALi33WZoRghU4eZXHA7gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=jjQk6yZxa2y7aqXFQKoRTxIuVP4jBp1QA4_gMDtG-EZRS-CUlzfEpK_CIRvme1avNT_MJwc3DjbRdNPnFX6BNlLlg3LMPAZkCDS_1T1Hl7Q-1V6kFEK-m8JhOOWqJXMubLSpe7xtJA-Smf-F7szUvBL1cxC4IGOK056WC9cwuAhbgWzHqMQzs5Y4ltg8qKhj2nR7I69qCWmVUZPVQmdmiexX3uuted3B4_wYGWyf56lvxDXmYiANT8_utPGQRaPtEmX0sPeHNJFCugSu6ddtMnm5CHipPbDOeVduagtszQ6-2zXfHmdoD3opeCnoSYVbXALi33WZoRghU4eZXHA7gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=mI9dmfM-TUvxg8DlYba3A7_HHnuLfSa5QGRUxvK9AmLx06cKV4kWFCsUaKYXoi_cRSC6mBgWtAfmlvsmEJEzSoc8srHDw26usmbqDjNjQqOtH8xv9W1ze70dg9dvleDPVwIOn7g-btUqF8yRyMqiinjyP9HC1XGKPmddY-FebAvNyKlJJTe0sc5pU8jGzbgkMQqfUKj9zyrk5PWxhgY-5LanTshWxli77-8IqWOzqUdYII_DWud6Yq58mOCx_OYVdp9tnWM9M2a6PlqbYOIYFYiNf8S94nrJ4mhAWgIEyXEJ8rHBl0rGrXlY-lkdy1KJIo3JFOoq6VdPkqjHdsv_Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=mI9dmfM-TUvxg8DlYba3A7_HHnuLfSa5QGRUxvK9AmLx06cKV4kWFCsUaKYXoi_cRSC6mBgWtAfmlvsmEJEzSoc8srHDw26usmbqDjNjQqOtH8xv9W1ze70dg9dvleDPVwIOn7g-btUqF8yRyMqiinjyP9HC1XGKPmddY-FebAvNyKlJJTe0sc5pU8jGzbgkMQqfUKj9zyrk5PWxhgY-5LanTshWxli77-8IqWOzqUdYII_DWud6Yq58mOCx_OYVdp9tnWM9M2a6PlqbYOIYFYiNf8S94nrJ4mhAWgIEyXEJ8rHBl0rGrXlY-lkdy1KJIo3JFOoq6VdPkqjHdsv_Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txDq1HRAtkTUcOf6c6tMJc3SzxWwnJfGTs_kzaGktHQHCb4GnH1YNzi-k9JLLHBtBDR5GrpTC8yDIZy9JbUgFGaS-Ota-iQFlVZSVb2niBAxC9AngWk8jbV699LuAqv0wGZ7IeEPVArAedZ7uJ32uOMTp51K-gTwrKCteqrJfIY-YDGIIABqOhABSwDDCEBhXvm9Ex4kZH2k_g62STJH0Zt_C2APmVi5XPIBMYe0y54WN-ZecFU4IF6TphfxEYG-clAScVNeLlf2QbEZCWR2kNn6vy5z2IzvnREd_4DZaJN6JeyOAJWdbBjMhe_UOn9OIDhBYjcqLMU3NbGuTQ_WPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG2pwrcIWcxAszvDJfEg1hCCZ-fweRjg30uKb1452KH1utCnCJ341S5HpE9SQ1h3yAhb4qMZZ1atVJd0DjKKWYP9fywlm8HgCB8HOB4bBsfC7wqN119nm_mq8xbIILEWw11f7ec_xo_ngU-nFk3WoEqE46oZIPFJWl_QsbaOyt74Wu-WeU5rQzwAdIVeDYkGDarc1pI_A4o_o7ElEdbchX0q9VXSHaoMyj4hYmFwyJwLAUDuDDitRQqb5FQ1GA_z2sa6cmwzqIZUU6UXCh9UF7SoZHcVw-ToJkDr6qQt_fKc8Q_e0VzFcIGpRzpqZB5-Nrcv-u9bV2ijkBKPLDdUDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tSDPLvz5kR1YAw5zrGLZqkmDBzddNCkGRS7OKGprbLe7r7jYKp0r2bV38FAfczP448i_BvQ6RbjktwCONZIbyZrc2a1hOq2HCsB0pEj20s3ukfFB6tHzrEYQZR-HgbGRsgoNTcH6g-X96kWeMyW7nnVD5hrIPji-0DU1B_uYQWmiBBR1K7qD3lzrEdAOJ8XPLXcvIyMQ_a6ew4aW6s_237m4oU4ulCwo2YeitFkK3F-C9e1jGf2ktAd0JHDynaUJs_KwbEWhlTh6dBaB4gvwRXdSoIXjfhpCmTsAfnUluwxcostCtokHsEXkuco0TeI2NX_k6gdIfwInVsUgAWVy0rej3hD43-9vN81erIhB7Px7v9I19tVPzkp0kUSB_ANwzeiLvcuu6c5ZAelSShSOPYW2EqKGUQK5GOzjQnup6c0zA3nfVGfdxURuQdQgO6vBljT91rgKZnVx_t0ORFgNB6ICjXodtPI4-eQSkLV4kUSgQjOXRczJHhmK33DeQS3HILNWaVgGRvyxGsU_wRIPi6xD5lrVu0bK1jkzgdShBqTw5_j_2-PtedQxp4MYp1USlOhLdmEiNrVO89064qA_6YhXvS2tX4ehwrBH88ZbLJtvxqmRUSyJfU960WYIQNJlrLZ7cmvgPdqsk72X05s45E7-nw7occ_pJO48BECNYpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tSDPLvz5kR1YAw5zrGLZqkmDBzddNCkGRS7OKGprbLe7r7jYKp0r2bV38FAfczP448i_BvQ6RbjktwCONZIbyZrc2a1hOq2HCsB0pEj20s3ukfFB6tHzrEYQZR-HgbGRsgoNTcH6g-X96kWeMyW7nnVD5hrIPji-0DU1B_uYQWmiBBR1K7qD3lzrEdAOJ8XPLXcvIyMQ_a6ew4aW6s_237m4oU4ulCwo2YeitFkK3F-C9e1jGf2ktAd0JHDynaUJs_KwbEWhlTh6dBaB4gvwRXdSoIXjfhpCmTsAfnUluwxcostCtokHsEXkuco0TeI2NX_k6gdIfwInVsUgAWVy0rej3hD43-9vN81erIhB7Px7v9I19tVPzkp0kUSB_ANwzeiLvcuu6c5ZAelSShSOPYW2EqKGUQK5GOzjQnup6c0zA3nfVGfdxURuQdQgO6vBljT91rgKZnVx_t0ORFgNB6ICjXodtPI4-eQSkLV4kUSgQjOXRczJHhmK33DeQS3HILNWaVgGRvyxGsU_wRIPi6xD5lrVu0bK1jkzgdShBqTw5_j_2-PtedQxp4MYp1USlOhLdmEiNrVO89064qA_6YhXvS2tX4ehwrBH88ZbLJtvxqmRUSyJfU960WYIQNJlrLZ7cmvgPdqsk72X05s45E7-nw7occ_pJO48BECNYpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGWKNqHBiSDCj3v0VI1RDMpfsf-Lq762Pvpvx6BQrbZ3e0MHW9-bWpUsv7KNegLWWurtuwlrD1Tkkqv-IB-cgyWK3fONGIv9RDMtg_Aw6BmUCGQhUi4gNgJwJhT7daBSoTAaect9FatZJ4mQxEfufqtRUl_rQcN7CfeBGQSnt-AOA5GI8vlvTYHszHUFfGfgkoiGZxUOGmKuN66HsTLbds4gIlIcjv4Y1p2aPV33PMFFnfdGLKb5SYZa4SFKFRCMfbzuhTStzQTJ5KrViP3usuyg-6-XRd3KJXM6M0R1ujGOZQRvK-rbu6Ihj-oVQ4zb-ij6KJfV67Mdi9B0_CiDlg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IjEnRIVHnNJ9uiTAd227X3E8k8zN4kw130DR4oOhdWovaqJOijbY-7KRt7OHb4xTp9hfAIxkdOA5QxJa1pFS3yDL1cf4lazcCsgCWS4QVmTqbwXq8agtsuD_6ooIW0Rn9l--ylNQQmfkt71Rtcr-d-wz9hcJ1MUlKBuNSbGHvoky1mDaorvxJX4v-XZqkqAoTh17d4JeWXi0lLCFV88ByIXYTpRhSfKGHSE4-VMC1htqSVw2wYmtw6vHQ0_zHOzzjUG6spK_WGRuo-mZ0Wli_P7U3jyidBMpQD8QVu1TVZ45LHbkViYsOzKUT-1Z-VWsgv3KbW7kSdNGvHpZrSBh3kwJ3a4Ql64-Wd4aAWL4hEeW062vU64neMiRub03zkfdx16Ah58qedX0zQ_g3R9VAanLPPjhrTQ_S9GWTZgQmyA4VEv20jKLnjMbyOpyR-dBtviw2EGNvh2JEkfKK7U1bqPULoor3h73h8DgOomeRmxpcBt-F3QHx9graADxQ4R0kriv97Jli08xjB0TREubl9JBMSn3fvVV24VUWL1G9EPbW9nWgwuKDCynnmGahw4R74RIdJJBVAUQ4iTItn28T3yXcHqXa0tIBNGikIRsKfsbCiQ12sqZ3LVdHbIxyKyrLgkpXUx1dkhmPu5Yk2Zd5nL5cl4n74I7iZiYoqASd0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IjEnRIVHnNJ9uiTAd227X3E8k8zN4kw130DR4oOhdWovaqJOijbY-7KRt7OHb4xTp9hfAIxkdOA5QxJa1pFS3yDL1cf4lazcCsgCWS4QVmTqbwXq8agtsuD_6ooIW0Rn9l--ylNQQmfkt71Rtcr-d-wz9hcJ1MUlKBuNSbGHvoky1mDaorvxJX4v-XZqkqAoTh17d4JeWXi0lLCFV88ByIXYTpRhSfKGHSE4-VMC1htqSVw2wYmtw6vHQ0_zHOzzjUG6spK_WGRuo-mZ0Wli_P7U3jyidBMpQD8QVu1TVZ45LHbkViYsOzKUT-1Z-VWsgv3KbW7kSdNGvHpZrSBh3kwJ3a4Ql64-Wd4aAWL4hEeW062vU64neMiRub03zkfdx16Ah58qedX0zQ_g3R9VAanLPPjhrTQ_S9GWTZgQmyA4VEv20jKLnjMbyOpyR-dBtviw2EGNvh2JEkfKK7U1bqPULoor3h73h8DgOomeRmxpcBt-F3QHx9graADxQ4R0kriv97Jli08xjB0TREubl9JBMSn3fvVV24VUWL1G9EPbW9nWgwuKDCynnmGahw4R74RIdJJBVAUQ4iTItn28T3yXcHqXa0tIBNGikIRsKfsbCiQ12sqZ3LVdHbIxyKyrLgkpXUx1dkhmPu5Yk2Zd5nL5cl4n74I7iZiYoqASd0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgvWj1pxq9MbKiqUYMsHccOknJ0oRImfjZdH4m80Mla8ITl0xFSqK8dsL1KdwCt_erzDBAbA3GsesLUb7PuAHmjWGGjw7wfZQhZVDLW3JiMjyO7b5x4vwOxEo8unCX3dpdY41GceW7PFURvEKDAs52l53GmwzjoXpLp-TdrYuGso9KS47RZswBiN0AfUSzPftw_nl0F6vrYeqEHj4HCRIrDPAdKNWI6Y-xiHzxvQ9_6Ot00IaVUwQg5Y-qQyqQnveVs2z5MBSqe4qHgBGACoPa0156rVNRUlBavOy_T2qfC0A6j2h4weT2C55iXzosXIfMDQSkb2lnj6SE7ZUO92cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh6VHqpYoC3i7krQSGVrQ40brBcfExQRzBiL7KwyK3ykF5CiHpv8MawNJx16bzigYZZgY8IcW740sjXL6h4gdCaTlc99_1hkyVyl3oI33BsBKo9ftapCaetD9Pg1fwDLijZNvx_vfdkzpOQrMaFXHCg1cPYG08I0KTLO22wi-ObzF7hvli1Xa8UXMVHxfS1i5Fsv-Vpmme3b6S_gLftTWwjrTzVl4trV_wykDx9VgbqH3CN4p_yQVUEErW-1bgSMjDZvyPFONsJK27AOHrHBMmfad0ZUxaXtX_qbuiHXfla7PiNbBFIPyqOAZFhxAgN0oUbmfAy-fgtu2LcYNAiBWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmNFA29nBjwH4pal8WAHDyfbbCD5hLZxI-Z-V8tGkFd2eJ1q47Yggc7SOEwSg53dr8dQW9JlR6OJDUs6kK5XJMkS2p18NQArGLoGcSw6QqbHm_eKFbCBiUCMY3JYQCwsCrFAispIda_jCOLDrwKUxUp_RycFfY66QfcyI8Rk_JvuNQxtsehG5wR_8ZnuYLNqXg6oKLOlvTfGZY41qI_rW4WCeRynKNA7yhCxKPeGF4bzCziZPZDVgIqBSebDSeiig813SGgVBvo0iaipvphNtDMneU2RSXzqJoKb6xcYZi7UWw-4N0EQz1QJHyeKbX81w19du4K_9CjVUs5iF4ymfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
