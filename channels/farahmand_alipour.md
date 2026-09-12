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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 03:06:01</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=upNem35VqoejIgomeXGaB4aVC8czAGzg-SaG-1KwvV0BT5qoO3MZ2Z-kBFVoRThpKCQ0qMBmnfwdHUYdowr3l8EPbA7VZNBCpyj2BR-dlVwmPKrXw15o9vC3XOslFr9kwwoKRUorAUWReXQzQNwVSI7aGNd0EkwwZGkhXCe45-HzqzVJ6PjbENyjEyAwCCMYiARFCqHMZoLrI51Dr7YbrjOLxMI5oEMasJY2F_5RbJHo9-eN_TgAb0IxupcA013t3jQsVg2APLSOlav_HuD3w4-C1MDS0KdbDgjmYNJep1B-OgB-ftN8VcQlnJsdBBtfoe12YZn2WCOK5dNBiaz6UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=upNem35VqoejIgomeXGaB4aVC8czAGzg-SaG-1KwvV0BT5qoO3MZ2Z-kBFVoRThpKCQ0qMBmnfwdHUYdowr3l8EPbA7VZNBCpyj2BR-dlVwmPKrXw15o9vC3XOslFr9kwwoKRUorAUWReXQzQNwVSI7aGNd0EkwwZGkhXCe45-HzqzVJ6PjbENyjEyAwCCMYiARFCqHMZoLrI51Dr7YbrjOLxMI5oEMasJY2F_5RbJHo9-eN_TgAb0IxupcA013t3jQsVg2APLSOlav_HuD3w4-C1MDS0KdbDgjmYNJep1B-OgB-ftN8VcQlnJsdBBtfoe12YZn2WCOK5dNBiaz6UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qWt4o3SyulkHZOiZYU5OnwANIayJIIoBt1XAtUnb-8wGjsMmKNmfrc2Q-clD2t-yZ-gOLavjLjGIK8qUjFqPVRc0CB998zofrkfYXewbk35wRGc2LRMN43rbifAa0Es_w-uEajgldUu_gVAuu2DJqIKrobcTrTfYcrtCgdpQkOFW_0S3HgHjRi9pbWROzHkhsadN92HlZzZ35QzV_ezIfdGWOGVb_xNbcjxlLzhoQ4ngL7RCbIH4WX9zVmthUdWAyWOu1ST044MFofX8pj7nIxHpexDyCtzu0t8rgLCtz6DFICzK9rVBzhcKZgcrnxu0hsUWdyHezr5SeTgE-BWQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qWt4o3SyulkHZOiZYU5OnwANIayJIIoBt1XAtUnb-8wGjsMmKNmfrc2Q-clD2t-yZ-gOLavjLjGIK8qUjFqPVRc0CB998zofrkfYXewbk35wRGc2LRMN43rbifAa0Es_w-uEajgldUu_gVAuu2DJqIKrobcTrTfYcrtCgdpQkOFW_0S3HgHjRi9pbWROzHkhsadN92HlZzZ35QzV_ezIfdGWOGVb_xNbcjxlLzhoQ4ngL7RCbIH4WX9zVmthUdWAyWOu1ST044MFofX8pj7nIxHpexDyCtzu0t8rgLCtz6DFICzK9rVBzhcKZgcrnxu0hsUWdyHezr5SeTgE-BWQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqs2olDKueWvoe3PFSdDNTuUKheP0s2N02ZPJvtlOXossRtVnCvYQjZEq0g8ksY9FXxst4rZ9u1hltDc4q5vr7fSLnS-6EzfNHaBNhr5I-PCqxPhujsJFGEa6i8MFAlM5ep9ygio7QPEvQnc3SG5lHO9OoG2ffo3Fw5B0s2EBgekfvLUe7D31j7VoczcBqRPU3LPl8mqAMl2u-ZI99z5CNLpta8JFlMDc6X4gW1TIsYKpkVGtlZp2tgIcnRJSz6CXXYTVhao6HWmIxqmcAjAUUsWOBCnhui_yfJMI88jcEbFhXVYVrGjtIOrGRzwAuu82N3qrfw_ac8pxe_4b-Ul3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjuEJ8tR-peoi3SejGPC7OBaidFOGgml99JOp-8sE--sZHOIEgxQK7PDi1CrSGzxH2gBlhMiShPb4zTRnbu_CKVDYnQX5aQWP3haHOAVqaYqHc4HmMuCMWjLZyKPLg3_HI2OwDSZsN-qxDVUGXqbY4Sg3CogUxixXD19gfFCYie-0jHgRGn-s2BSzI9ATU2kZSaUsBmHIwDhm3hqIurbC68yiXqLg3jaIfVd5rOEwRbry0lWlvlS-4AiQrYiYZecS7ovXM5AN517MaFcRD7m8rX-lYMeiXbmI28dHRqvn6c-Ipq2fZnL0yMrPDAX8fnlXZsxloXdwjTHA3RuAXdFeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fdMUlE2ZWdFD0QeVwJUTyG1R12rfLsxEJD9mfD14UsboRYMXmNapkPw74rE4017EaEFSocEdQCNuyudzqt_Lu62Pk56XADUq5eCSjEntfjeYuNWby1o_sbxCXv37DJG7u_BfinUpW9nf2C2AMmCilMa67sHTVLerfyCmBNFYgjdRB41ySGoeybMMdoiyUKNOdbXlmNJPMtpuOGSmb7oRb0p_k1yM0esBGBbGws0FtpyU1QO5oej7NUu8Kg6o-eLaCB_tQbtKC2XeSZpRb-5Ua0TewHaqe1y5_IfvClnVVbcz-LkYF25P2S0fS7r8EXJ3gcBDAfXv2dkg-kuW5OvHvlomW8zm1DPjGwEafwsELbhPoMQCi0kRk6TojNQ3uGmX6cCkcvnkrQs93QShjVt0j51K7MHhn-2ohhylrClewDgvoUqhVf_W-HGcsA-4pTsvj8PJ2gFtqFzvJASfAeDBhVVA4f3-ZOHxtEuLo3qKjyI_aJuYid3dUBqUWi7jYkj4JzaLXtqcTg7xsWRhmEBXkhvgKcU6Ye4Pm6yp7byOjiq7Vn7h8MZYiq7CmFoxQv3pSA8KVqt6_KVVtkvxI1TEcsBpnUNlxBMf7k_pCP5jUUsMhKUMetRpqE2CkBRPhpfBIPN38WUbCx_QvamFRxpi4PFLRBe0r9Jzvt6XJd8UGbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fdMUlE2ZWdFD0QeVwJUTyG1R12rfLsxEJD9mfD14UsboRYMXmNapkPw74rE4017EaEFSocEdQCNuyudzqt_Lu62Pk56XADUq5eCSjEntfjeYuNWby1o_sbxCXv37DJG7u_BfinUpW9nf2C2AMmCilMa67sHTVLerfyCmBNFYgjdRB41ySGoeybMMdoiyUKNOdbXlmNJPMtpuOGSmb7oRb0p_k1yM0esBGBbGws0FtpyU1QO5oej7NUu8Kg6o-eLaCB_tQbtKC2XeSZpRb-5Ua0TewHaqe1y5_IfvClnVVbcz-LkYF25P2S0fS7r8EXJ3gcBDAfXv2dkg-kuW5OvHvlomW8zm1DPjGwEafwsELbhPoMQCi0kRk6TojNQ3uGmX6cCkcvnkrQs93QShjVt0j51K7MHhn-2ohhylrClewDgvoUqhVf_W-HGcsA-4pTsvj8PJ2gFtqFzvJASfAeDBhVVA4f3-ZOHxtEuLo3qKjyI_aJuYid3dUBqUWi7jYkj4JzaLXtqcTg7xsWRhmEBXkhvgKcU6Ye4Pm6yp7byOjiq7Vn7h8MZYiq7CmFoxQv3pSA8KVqt6_KVVtkvxI1TEcsBpnUNlxBMf7k_pCP5jUUsMhKUMetRpqE2CkBRPhpfBIPN38WUbCx_QvamFRxpi4PFLRBe0r9Jzvt6XJd8UGbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oQHXeQdRENkGiHKEyV-X9NrEaeCjo1TZ9gkVYj61qFqMJnXCPMQUewpCs_UlUlSazHdeCQb4Rn52Piox7SkrakqGSGIfh0Tk2uwwFtwutilWkngnHqnbZAY0vf6YV3Z-mei4zw7PHwDWIAPHb9V7MARfZ5eS54h8HNtddg--gYL8w9lY1v4obzqJfmYPRP4sVHgFWs0uAEw-boYrKz-7QFb2yO1LsUdCQOxv2JIGK7PlAkQ75YR8ou69FE9zfo2krpWg7xDC299M1k9eXXcuB2krumkavLuTn_9QAEqYZAikpcEFhnvfPtckUMPt6_ALqR0Khsazy__TdwmA1EE7vitFhJ27btMchXKpDDlA_T_pZqtLKDhP7hj4sEIwKw5obyidOg67_38O6ioZUSekcWuW3-Qq6uF6T5JbjFY3w0Ty8VpmlQeNDQJCF7d1ig9JqhIf7z4c2j4kHtHXQgsmx_l9BIt2rB_Q3qVpx-lrq3yVHYxRNBdUbJxenSi9Ah2-a6_hsBU_PPXVismOdMqM5MvBq87c4VM_7lSeGw9ethbMv4FmJpEIr_mlUCy9iaEEkqaxz9grXN2Y5NdbmwrYm8sGQSeQSoeX8IDU45CcgCsB34k7KOxwsyWeAvczTEF4pVNmw8y3UfAkzi4zRDCD7ATWDUItUCoL7_3l3L30QLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=oQHXeQdRENkGiHKEyV-X9NrEaeCjo1TZ9gkVYj61qFqMJnXCPMQUewpCs_UlUlSazHdeCQb4Rn52Piox7SkrakqGSGIfh0Tk2uwwFtwutilWkngnHqnbZAY0vf6YV3Z-mei4zw7PHwDWIAPHb9V7MARfZ5eS54h8HNtddg--gYL8w9lY1v4obzqJfmYPRP4sVHgFWs0uAEw-boYrKz-7QFb2yO1LsUdCQOxv2JIGK7PlAkQ75YR8ou69FE9zfo2krpWg7xDC299M1k9eXXcuB2krumkavLuTn_9QAEqYZAikpcEFhnvfPtckUMPt6_ALqR0Khsazy__TdwmA1EE7vitFhJ27btMchXKpDDlA_T_pZqtLKDhP7hj4sEIwKw5obyidOg67_38O6ioZUSekcWuW3-Qq6uF6T5JbjFY3w0Ty8VpmlQeNDQJCF7d1ig9JqhIf7z4c2j4kHtHXQgsmx_l9BIt2rB_Q3qVpx-lrq3yVHYxRNBdUbJxenSi9Ah2-a6_hsBU_PPXVismOdMqM5MvBq87c4VM_7lSeGw9ethbMv4FmJpEIr_mlUCy9iaEEkqaxz9grXN2Y5NdbmwrYm8sGQSeQSoeX8IDU45CcgCsB34k7KOxwsyWeAvczTEF4pVNmw8y3UfAkzi4zRDCD7ATWDUItUCoL7_3l3L30QLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDkRpLT5f2D_l_faztGiGS30UwTlaks57J6jivfW6vgoRc_Nyg8GbVESLq8KFQ32oJfhpPqUhViWAvOINQJm76aUmfwWms3D4OfpHIbnwIqC5YuCmUaT2gCr1uv9GMF27l6WrGUdo4eliJqBKm1zvNgqLKFTJnwCgBu9hSW2qIRArPB5WZF4NpyKGleLO8PnsQ6BJ2_EBGwrTM7B2oWtC4MdsyWZJphjEIT1SnkZm0eBcnWUb6waYZRBrmman8rkdhg2bkm-RMzzsCUA_bn2PrOjhU_owox_x3JD4T6iu5PZoxFKiOP1NxtflwTM11enXJGOdW4xvfVR_qQuBmrlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=YDo6vMYMuEIypIjLMBdSho6XgvCqGAzc-CMIXIy_xLSDC1ePupqvoA9MrP2pyKkpBTUakqLx0cTw0Zhm03YCumDDYHZ7hFbmKr2jZXbeZmKDisPGKeVpK_OzBlxrIi21knzXBpD80ePBlimnDDM96B5fNhumkE7lmXeWbEuhzhNFAglT-1AnfSSyXlmqbKX7x9y6pHhYjUX3XZhMOg3YQ12tH7DOHAA2EFtIMToAB8PG7-J-uZqxVdwiu6A2nwbc8acg6pZCW7bUPaU6aSyrzI_3kKJlZQhyYkONDzapxzJ3NR12DBdvXSBaAx2ZJPbjtIs655-m6BubYuLqiAK-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=YDo6vMYMuEIypIjLMBdSho6XgvCqGAzc-CMIXIy_xLSDC1ePupqvoA9MrP2pyKkpBTUakqLx0cTw0Zhm03YCumDDYHZ7hFbmKr2jZXbeZmKDisPGKeVpK_OzBlxrIi21knzXBpD80ePBlimnDDM96B5fNhumkE7lmXeWbEuhzhNFAglT-1AnfSSyXlmqbKX7x9y6pHhYjUX3XZhMOg3YQ12tH7DOHAA2EFtIMToAB8PG7-J-uZqxVdwiu6A2nwbc8acg6pZCW7bUPaU6aSyrzI_3kKJlZQhyYkONDzapxzJ3NR12DBdvXSBaAx2ZJPbjtIs655-m6BubYuLqiAK-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeBMWhCqp37_zbvgPNuxm1h_fgaL_VwyK9CiqEo_IBw_4QTiQbd4A4oauo-XsgQlp-01rGeoyKHdFb9gnlajfhOBvIUQaW_xci8Q_j7CMzAt-ywuvr-sCBfGy2lfRuw2NoUS-MqJA11oqbHWL7qiLb7b0SCdPti0z9xXjiKhXeMIXsfwWPqf520pKMhYjSmuDzITyrPLNaB7_ln-TirbX9NqBG3htH5a3UGoVEkV7SYUpeqxOTMM2JXVeIum_DXc7KYTj8hnwg2_PrXEN4XY-iVw3Mmzj861v4pKR4XJU-8fIC_SR5pERSEG4enuBNiLS7TlTwwU4VOI38BZfWNETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMIByjBuza_Qe2vgMIG3eMg3CJb1r6gU5fzLYJgbax3D7gzIIiAULBXqEZPSJyxBhsr4vLkGMxrNIptrk-FJEwujnNi6c7TD2mPgJm5F2QjmJQOK8kcjU_Uck42SFuVIc1m10nxoEfSSRglzlQA8CxWY3DWApOL-vfRmN9k9ZVC8xMeD9280x1QlvankdVa_WO4ovAvmTrj71LSaY2oiw3JXpdJSlAG4DP4BnMg-jJSAsZ1oI382icQsKuvs7sYYtRGO72elqkCPAWsJTMGxXw-5TINMys0wmpia_jeUhZ8bdFBRZbozBK5PCQg3BD7YOJhfDgltw8z9eSdJUXBUuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIrxbArwrF-t_CTituExmejR7jNetDE6-_EYdakPRm3BiMrY_y0RHUgNfjB_V5os7MsuvoWlSzaOsaHHmEU9SEBw90CRZLaogH-ftptzHc1sA7pFQAuBa3e1dVdHe1OcwK1OrgZ5jp5BXwsaps_9GRNfwVnWaRZpkYNlN-_JisfkTOIpARowG0fz6p4Y8Uztg050ZPEMBfImFmcieCZdoOFkQWkXpC6pvlXcYWHy0XDCqZ1YM6WQkt2vHHezw7WgcER5gYuDZkQbMOyW1dc_zkM_5rboUC9QGdWjN8mZhctkmnR3SBBIcX2cURHQldc9wuwVqd9n8crWwv_yM7Xe-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkjGEeD_Cfdk3Qv9CORyYPZ55J19boO4frR0fZRRPeAf5m0zxXktCrncuqxzdXTxTkCYepSmISVIA2bAXrXUxt9XnhpOCfihAPkknqz87-Nu4txhhIpELE7-lr1Znw93fO8WyIqllvDZY-1ZoQ1i1CZXClXADKGZ1x__2l4axwf9zRf27qYsn-6aofcpYMPtI3viWtDzy_s6Vk0ZLDccNzTeuqBzvyzUIkJ42M7ylBm-ZxsLFiG7flfAr33N01zZRie1LdCJwd7DvaXoYN6YNN3wmNTWz5NgfJsK0kay8IdjyFzVU7N3vkKP2cHTz5HaixLtk6Oi46-_v6zWNhwQiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx6D88yIj_XPlZkPZs5aR3clD62SM_r7iuWcg68Cl5GpExL9PXKx0bRRUYHmHaVlzJFKg0xy9vHnjymIFvMdLgz1AQHGU_r6brzQQW6NxWSz0zWkJLDBNLSuAhZ6TKdZo9A36vqmur0Wg_DZxJmOyHl0lcZP8SEQZ4hPzJNZIhBFHkx_aFYKkGgsXPbwIobmk3oxOlo3iaRDE2mbq1VmxCU2vBkvdxRLVJJlBljJ17HkdOMi--hnRaLy4do4ucAFvg8AUBikkWceDI1PrX5AgmaRIY0YFzYeLo-jTgmMXD7BHJ-LKx_Z2cFIGG4lR65E7dIDEiAFlmzv7z_pmdn2MA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=oOro-gavEDwPIuQ28ORtnnNZaGDL-vVRWssxUj_eXdAwK_FgGcWQWeYOURxPP94KxGOupJvwvOdyIhOxYBBW0VfAn-DrLnjelIHs8hZxmle0rmK3UZ_WleqawEeYB3ttcBuYud0QEbeq2YiYzzcyTBstttcpCF63f8ujebLOPEyQFDcOzg3oFvUzF8jP92355jiV6B8iuFqYR78BhIJy51yj7v2F6kXB5HqN2YuN_EvXo08mv_ygyl-ntox5uuByVSZDk8eIx-irPTxfu3kcSqoc3_kgQuEskuANsaaZSy-nbMcbmbaTZ1uAPLY9l_1gw7sIjC5GRfRNfdof62evyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=oOro-gavEDwPIuQ28ORtnnNZaGDL-vVRWssxUj_eXdAwK_FgGcWQWeYOURxPP94KxGOupJvwvOdyIhOxYBBW0VfAn-DrLnjelIHs8hZxmle0rmK3UZ_WleqawEeYB3ttcBuYud0QEbeq2YiYzzcyTBstttcpCF63f8ujebLOPEyQFDcOzg3oFvUzF8jP92355jiV6B8iuFqYR78BhIJy51yj7v2F6kXB5HqN2YuN_EvXo08mv_ygyl-ntox5uuByVSZDk8eIx-irPTxfu3kcSqoc3_kgQuEskuANsaaZSy-nbMcbmbaTZ1uAPLY9l_1gw7sIjC5GRfRNfdof62evyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=c972hTO5EmKTK7GEaDheY1-W4D3WVrFh4UetxxLUeSdTN6YEXNIrXcSXqPvchMmLvzJRSwcAnxDvKyxfnKk7Yuz_t-tm9w-3tcKcoeylFWq36ACnR6-g78OIZslbxh_MehPjTcnHSV3Muk93BJUxd-kdHjVgnKg9QhXL40hZ1d-QuzHsvXGSIrrpoOLcMw1WcSncHCHBYAddIDY4Fi8WOMATABWtQOO4YJUrVnZ8qXy5SwefHGoBykSJd8H2py7U0tNV6YWzWDNxnGEt66st6Ios9GUXEHcd0gLd_V3stUlt--5Azb9LCU57QIXB1ue2suxfa3-OcCLAh7BxZEuxyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=c972hTO5EmKTK7GEaDheY1-W4D3WVrFh4UetxxLUeSdTN6YEXNIrXcSXqPvchMmLvzJRSwcAnxDvKyxfnKk7Yuz_t-tm9w-3tcKcoeylFWq36ACnR6-g78OIZslbxh_MehPjTcnHSV3Muk93BJUxd-kdHjVgnKg9QhXL40hZ1d-QuzHsvXGSIrrpoOLcMw1WcSncHCHBYAddIDY4Fi8WOMATABWtQOO4YJUrVnZ8qXy5SwefHGoBykSJd8H2py7U0tNV6YWzWDNxnGEt66st6Ios9GUXEHcd0gLd_V3stUlt--5Azb9LCU57QIXB1ue2suxfa3-OcCLAh7BxZEuxyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzW2SdK4ywavu_OU2W1cIGOoRSX8e7br_JQMt1I-Dplz17FQ7FWeoSwnlGo2ZhrkBEWfKhc0M-ZFGXdPZwqzHX3pYSmqkorfyqW_kwrDAfHkoQfM0Y9b8Ki-LZL-IlKT4x6hzVeOl_9kWxlzOxVGzESsTfY_71IDzmXmnISrHzRGkEpU8eJrjoXZ69Jnqw5BWnSG3wjx3eFeYOgz1mlhwe9AIZFggkyd_1DLURjU53mgAazbLbM23nttnBGIt2606nGiaK1zYtankVL5PbYeKm7ylsKB53US07weEghg5nO8TEXfhUI-ZOdjzgc3Z-6dlPjSxoXwmu4svgmzl9SK-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4m3PVq8Doh577sQGWKGw0XSOKrBZJD8TV4VTH2hFb8Q0_0g-j9mE7oSQjH0X_bNLdGsWxxo1ajQS65SkZwhTvOcDQIWZgu00LFd60sTZw7ZnnsArqjl4kTAgHuEaLJcY-quLFfeJhuA1Ric0jy7oRvdv0-WIfoiVcBKC-SV5sg0zyFpwpqaGyTA1CRC2Bri8Jwz0fyf0ADSFjOIS6ZeEtNkQqjUpko-_yrzDLHDJLuPfUgdT_xkRJNZmBjn0m5KQQzn_47_hw82E94TeKSP_n61q7fuyDnhgsRhxD4QRPwYiHm0HXiTGwIVrHpqVq3o3Jfe739nmlvy3cciIhBG6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9UMTP6CPMZp4Oh2LXNQBYbYNR41Clz5EaQBbpmToEEOaYehOcAroudkpkUgcpXjcbB45BdG8MR13sDE_rGcFv13KkxbIiepE6885erQm641G1W_oUwHZc0d8Rh-0kXvYG9wo7clyyRT3bCQeB2x6oRbkWRRD-x4mYWYyl2rr9twH5SSsXRtziZ3NmN0S7KLVxP0UzpKSEk3mnIefjX8bi-1wisCVhqYSMPOQd0xG_JFHRyQaSX2x4fbqvLVboaEI7tTL9uUTJMe6N13uyyOgbJ9w-ai_nO661fn34dIlGdLlT6fZ_V-_ZUuGmZ6xBC3GGZFG35U-Y8rSD3onUcbYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ovcfFFyJl_qKcCj80WC5QtjSbcT_E5QDM0AAt2s3MzqLxIlcnPR3-0BHO3h6hu9uS_4xj9RpfJuIOBG3YILIkfMMMKMgPGdDaCpY-5FvNz3XlVLobYP59Ms5IXk7uSIIoqzDihGokWrGhAggtNRBr1zs0F5TibK6nRKZgh_TMbc76ySD2WgUBQpxhCqXe-3HBIob8dMowVbOBgR02KWmWn2bZ0MhKzFkEbSZSQ-FXg2XfiY_pOWGWy5JHxnH-mPGElmbm2p5aLxta9i4Qjdg0hpcq0EvE6998PBjigBL9mze_lgeNUdw_ob0GI0IZgbN7XtLRarn2JROOVge66GHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ovcfFFyJl_qKcCj80WC5QtjSbcT_E5QDM0AAt2s3MzqLxIlcnPR3-0BHO3h6hu9uS_4xj9RpfJuIOBG3YILIkfMMMKMgPGdDaCpY-5FvNz3XlVLobYP59Ms5IXk7uSIIoqzDihGokWrGhAggtNRBr1zs0F5TibK6nRKZgh_TMbc76ySD2WgUBQpxhCqXe-3HBIob8dMowVbOBgR02KWmWn2bZ0MhKzFkEbSZSQ-FXg2XfiY_pOWGWy5JHxnH-mPGElmbm2p5aLxta9i4Qjdg0hpcq0EvE6998PBjigBL9mze_lgeNUdw_ob0GI0IZgbN7XtLRarn2JROOVge66GHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thIilpX4_jq-qGBglsdRgp5ZqFNMoDkI49drDBPo7VuDVClrGqOrHcsiOQOmo_YxTnk3Q1ZY_1apLNpbdhs4m9e4QAuteeRR3MOg86fG14BmejGyKyXJSQAMovKva9iyQH2p8tWfWQHTmDje7w_Jz5bV1u2Gsm2TIc3IziBH0DM2iK_KrLBFMju8xpl9Bbp8or3_YNwZx9m-u5vBplVxsHQXkeEjDjmhtF7EdqQl_wo3kwXYzDbnNL7VI6J2vyiYZxWB4o0QA_Dnekhk7tw5-2X2pbEMVAAH0S4gUyrbnaTXzDOwR5gyRcU428nIO4rroQRA-tONZXC33xz3MxJVJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNOZcXQzf6IqAJpWiI5xTmW4s7Qqs-74CBNohJGBXoKQn1Jqe3IL5k0zZAN1PH-RCgymNblggGXdTZPCmv0vQ82SOi3xvCFY33OCl_reUwvOFvwR3wHYtLS_7meDli6eGMuYEm3bIqNLqPYZ34UIMZzH4UjtFzMCamG_MY4I_eMTuHTPUmcG9SGT9H3pP7tVH9r9nDu5809iE0de9uMEnyFX_cyBbGPfIp8U1Q742c4b8YPgE3d8_F1ugrqaSG-wycDD4JyQ0booKUTmBxVqSS4JovshEJxmUwe1KVJ44DnA2BC8JZW6ZRaaA-3OzOJ47F__jAO_spIfSem5o95Zsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=N46UVbVioRR-0cwQPylTDDvCLKe56vzeMarVMQUco0r6a49jY9ZimpJtzDPGeVfHHE-P3NxbQ_bsT4YcoZy6Qd4SiRVJ-lDY3MahdzYZsoCKRqSFC4OIWRjFWyFMguYA5774apoYjw2uPvpd86hh5G4ufbEhJZYeAZQ3Nw5EYX9_nhtmSGiVOPauMeDmQmfetqViTqe8JV-kIjkpPmAVz2zZQVoGqW4tRho3jLiX842uFiVNHWVv6JAw2FP0fiiiln3La5rvnOhVtZfZ1aelWE4cgX04mZM6wg9_QuKJu5I5EJ3sSfXXLsD5X3zv4xTChKxcQoNjRgDsZYycHkJz2Q2-obSWalI0kFSWM9ipgKla03It93pKWRQ9ij5c--QoZKIdcAdIC1YkcXn9t7LOlRfgsAaOLRQEJZisJeCPDnrYGbNLlNh9_gy3DBvrQM_jeQjYRZCSl7EO5ByQxugwgG2uEUAVIHevYmFnbPczA8sMBW5sOyzN7MYZL9NbnfgQnGNRZTQ8a__VNTr3eXzI8001SWgrFn6sVmNImaAakmhhrdIAkLJbIaCkdyc3ITCXw99B2yICvZnksOCjCiF64EU6WVPTlvLnrLYYZri1XER4Z9OPKl6I9Xg6SRbwEHUCMGdFBheG8mCHsLycq8r3dU5drb04l8EkYFSJ965yT94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=N46UVbVioRR-0cwQPylTDDvCLKe56vzeMarVMQUco0r6a49jY9ZimpJtzDPGeVfHHE-P3NxbQ_bsT4YcoZy6Qd4SiRVJ-lDY3MahdzYZsoCKRqSFC4OIWRjFWyFMguYA5774apoYjw2uPvpd86hh5G4ufbEhJZYeAZQ3Nw5EYX9_nhtmSGiVOPauMeDmQmfetqViTqe8JV-kIjkpPmAVz2zZQVoGqW4tRho3jLiX842uFiVNHWVv6JAw2FP0fiiiln3La5rvnOhVtZfZ1aelWE4cgX04mZM6wg9_QuKJu5I5EJ3sSfXXLsD5X3zv4xTChKxcQoNjRgDsZYycHkJz2Q2-obSWalI0kFSWM9ipgKla03It93pKWRQ9ij5c--QoZKIdcAdIC1YkcXn9t7LOlRfgsAaOLRQEJZisJeCPDnrYGbNLlNh9_gy3DBvrQM_jeQjYRZCSl7EO5ByQxugwgG2uEUAVIHevYmFnbPczA8sMBW5sOyzN7MYZL9NbnfgQnGNRZTQ8a__VNTr3eXzI8001SWgrFn6sVmNImaAakmhhrdIAkLJbIaCkdyc3ITCXw99B2yICvZnksOCjCiF64EU6WVPTlvLnrLYYZri1XER4Z9OPKl6I9Xg6SRbwEHUCMGdFBheG8mCHsLycq8r3dU5drb04l8EkYFSJ965yT94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub9Hf2JSgfE8NeeDnRQB7YorkG9AJ1Euoav1_N9MP0n3NbsBERqg-ofuEKvxLnEpEbYHpXrPk7lmBnDztDaZ9rEH7iPx-dtSOKn7iLzBfrIZzBNJTHCaUagFiK3Zrny508UdjSF42Q06s-FxkqCLqTrlL6Rjv5iqsxoeJNcAE9X4NOSbpllyJ5LMkXII_2f4yy1fA2UxtJmQ2fBgDs-IBLqr896pIObNIWRV4awc9t4Es2COBqplP0la4zkSacOFinW_U4pmxLqZZtpII0-6swalaCQUBN3-g3XqrHZumY82C52CBioQnIuyrfSyTCVi-wGwJU3a-H-Ou9HUzfYnpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=bHGOOguX-6TvEa-Yp2PiAonRFhT1KVZNbaXyQRv5isZx8l-sMSkx8KxbEI2ETZCg0vpSE4mVOAU2gCYaM1WVZrbnwicFYN9503AMenkYiY9IpKxYwhwLZa5sb-NI72CI1nG8JOOSZ33ABmAgyYcIv30uX96V_jIezndphGdScCdL8KR1xsUooLnCn3ecFmi0WcDcET5hhE43C0xwz8Jf-2ZZesd6aJinEK7soVbSxRC-wVP8vcETBCI8tqG_lLuhFy46-bUR2hbG01_LIpgM5pn4Xma30wyXKtwF9wNqKliaO76KJkzPeNEp4ur9QT2lrSt4laqrUIOR7dxSJIyTCTEExTTC-7fcvVPguu-PbvpxmjhE3SdRoxaVZK12O8EswVZJQ5p-GrI69gUQfys1q94yApGFEaFrztAMXeLnNQb4DQJ4oPb_dWEWYTbbFXa2NX0wvhygZuxfqnQbdPBlszX-aUPUSEf_CA6TzxuGQJKs4QiMGRuv2iZjazjlIsvL7K9ubNmp0hekuGf_KobbiXAaPcER66QZAIlrspc0YBkZABUtDA7iV8Y-CtxchYXt0klszdLb8WRlqkO9O8W9Iplupq0XCgaf6wlqCpCrEy9NgapQJZfVrsOThQgMS-rn2a1IMZwbCrc_P-84VjLwmevVNApm57pQZLGuSyQt1HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=bHGOOguX-6TvEa-Yp2PiAonRFhT1KVZNbaXyQRv5isZx8l-sMSkx8KxbEI2ETZCg0vpSE4mVOAU2gCYaM1WVZrbnwicFYN9503AMenkYiY9IpKxYwhwLZa5sb-NI72CI1nG8JOOSZ33ABmAgyYcIv30uX96V_jIezndphGdScCdL8KR1xsUooLnCn3ecFmi0WcDcET5hhE43C0xwz8Jf-2ZZesd6aJinEK7soVbSxRC-wVP8vcETBCI8tqG_lLuhFy46-bUR2hbG01_LIpgM5pn4Xma30wyXKtwF9wNqKliaO76KJkzPeNEp4ur9QT2lrSt4laqrUIOR7dxSJIyTCTEExTTC-7fcvVPguu-PbvpxmjhE3SdRoxaVZK12O8EswVZJQ5p-GrI69gUQfys1q94yApGFEaFrztAMXeLnNQb4DQJ4oPb_dWEWYTbbFXa2NX0wvhygZuxfqnQbdPBlszX-aUPUSEf_CA6TzxuGQJKs4QiMGRuv2iZjazjlIsvL7K9ubNmp0hekuGf_KobbiXAaPcER66QZAIlrspc0YBkZABUtDA7iV8Y-CtxchYXt0klszdLb8WRlqkO9O8W9Iplupq0XCgaf6wlqCpCrEy9NgapQJZfVrsOThQgMS-rn2a1IMZwbCrc_P-84VjLwmevVNApm57pQZLGuSyQt1HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPIjfK-fDmyk5KIZt-blb4d9UFitmDSPmYkNeaQHGVWWHH69iR2823KiHD6-SqJhsz6aTEjivsUO7BPLooazArYk6NI41F8S-uN4n7PeueRPiUnAt6FQ1eFaGqnMe9hUioe5lt3QS5hNCTukqtWps9VSS9hbjXr4KVcsAR-XkYJGncnqGdMuZhap1H04tCk0mslcvIY_GCYC1vaciJQZLUpJPKB2qMrOny-P8DcEjo80_LtwI4ZCb6QgVqrjSqGwSZHd4NAAw2w_TKD4uSfHymvCHXIz_eL_qW8-AZW3MLku97d0EQzdB--DxDe6BQd232RBJc3EFo9BgArjqSQzXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUeLZPyhDN5xQbUluBCWDkXmRMAxl337JdqzmcDXCWF4G_CfwD5lp_CCky_smDTnGU1bGQBijaW1Rk5oi_nYe73tI0P-yjLMsMndfTecr7WoY0PZVDHJ4EmabLZt3xIDGyQmcVkGRpz4A9RpOXvuPToTXBysJfSCxA4W_ekU_XJVkQB3oQLz66jhRlektn3oFSTfJw_OFHzV067nNBk3bx0tAFuWkW83ZYDJdHb3k2_sger3hfDcpTzDLThV-j74CWIhqSs96Jl_WU7V9b-XCKHyHJwjI69HYqbhzkJsMSFGBuhyYUT-4YSUAqfgDx9pglsAEnD8tLuplU9SP2siNg.jpg" alt="photo" loading="lazy"/></div>
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
