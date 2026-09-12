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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EXlpZLmcpbyw3RsYxNXNErnXTEI3JeErXvwFCA0H0UFtCEziVZ9ri0TPtIYeJ5twhxAymV9LjEERvqG-xBOw_nNmvZSm9qiiGT-JUxgDQYWVCepEGVFmit06dvZZfG_N1Dm7puel-d_wbJRJbjcj3dp8oO6zzUB8-k6OjU3biVu9BuQyqfxTdVWbYd0TExwlPsE1BkWpKQ28inAxo9P4SpZgu6uiX-OuNlXACZtykj5rLHueF5pq-s5W5tYXeibo-i8FzBPGBHz7KVMsQ4u47kJFWtk5jZymWD6UoJvrwh0YMEJXiUvbgROxTdZEpwf-9u7E8prz0SJpVMsQTqeBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EXlpZLmcpbyw3RsYxNXNErnXTEI3JeErXvwFCA0H0UFtCEziVZ9ri0TPtIYeJ5twhxAymV9LjEERvqG-xBOw_nNmvZSm9qiiGT-JUxgDQYWVCepEGVFmit06dvZZfG_N1Dm7puel-d_wbJRJbjcj3dp8oO6zzUB8-k6OjU3biVu9BuQyqfxTdVWbYd0TExwlPsE1BkWpKQ28inAxo9P4SpZgu6uiX-OuNlXACZtykj5rLHueF5pq-s5W5tYXeibo-i8FzBPGBHz7KVMsQ4u47kJFWtk5jZymWD6UoJvrwh0YMEJXiUvbgROxTdZEpwf-9u7E8prz0SJpVMsQTqeBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIv13W5STLY7-JP2-hDNkZxjvAf_Pm3CTr6U9puBeoreetJxRfcUvXq9vihz7Rb48k2eWkmU_kDf4BmxkNKMVecmsuV0bsd_vUq8YfOiAillejhRfem9jMs0HN9ni6d-cZulNk9obpA8buxjKpy33u66tXEHTATysJ3PnNWZyoroZzsdHN55eCicTj2WyyJjM9PHsVMgweVWZxyXtj_C4VBiKzhXytqAZFD8spd1lyqmD9v4ver2adeLIlzHjjosMeFV5IH68fKBHdlb2nX-UNAHL67LusxKlMgtPwHhPH-qMTDrjPnJh2ujplMJ0wZpjKZA50cdul8v2YLQ72JfgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lZKlCcsf9Hk5EQifpqWNi9G4fqhrYuqr8JylknxrF4GkTElhe9BRu2taTLmU9-uKeT6xKRnGZpwo631xxuEvCOvX6bM16xUnPpOi4eAygPcAi_gkiIIEcMJn5bQcu6-siXZ4MgmcRHZtTGQH_JVU-uXdzaZpqcFlGVSMDxfMfSrDfqo8MfXA7hZmb0jnA3mnYSXPXZcGCqUlHu-N00nuikTZvqxqXosSy3RJMRrBwnWVtSztJgUJ2lPRqTpwqgBJuRDeXSvWv5zcBPYizb-4ME08XpJBly-glnNozRlrDH37FjwTmrj8KG5A9gUH7BbOQUXmlVhK_uVuiWqKrK6VljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lZKlCcsf9Hk5EQifpqWNi9G4fqhrYuqr8JylknxrF4GkTElhe9BRu2taTLmU9-uKeT6xKRnGZpwo631xxuEvCOvX6bM16xUnPpOi4eAygPcAi_gkiIIEcMJn5bQcu6-siXZ4MgmcRHZtTGQH_JVU-uXdzaZpqcFlGVSMDxfMfSrDfqo8MfXA7hZmb0jnA3mnYSXPXZcGCqUlHu-N00nuikTZvqxqXosSy3RJMRrBwnWVtSztJgUJ2lPRqTpwqgBJuRDeXSvWv5zcBPYizb-4ME08XpJBly-glnNozRlrDH37FjwTmrj8KG5A9gUH7BbOQUXmlVhK_uVuiWqKrK6VljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vwjhSFdbafD3HpKACnE6SlReYjSUG8YIxNKbFwyJ_eVCws1pUUxCe0WB3UDpiAy6qJkxeO40MYo7mMHM2Ajxe4dLrRyokBjnC9dvwpOUx4wT0YcPb0qdSXrZvXOlG63lhT36D9KPOr1p7wTFDk2YVyzgdZrVuNn7aonkkDZ7neSs984YhgpQ0CMwA9K8RCawSaIqFc32fu72S7LPh1iMMT_7diD5nxAu2U1Xk6sMfL34StyIJ8vFTFB38CbJoAS1c8PRDTN8bujVP6BlTgHo3_d2cb_Fi9XiqoML3ju5gcthZCW5i6Q0pKkuQB7Uy-0atwLPyRR-y2MXPbIVc9-PUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vwjhSFdbafD3HpKACnE6SlReYjSUG8YIxNKbFwyJ_eVCws1pUUxCe0WB3UDpiAy6qJkxeO40MYo7mMHM2Ajxe4dLrRyokBjnC9dvwpOUx4wT0YcPb0qdSXrZvXOlG63lhT36D9KPOr1p7wTFDk2YVyzgdZrVuNn7aonkkDZ7neSs984YhgpQ0CMwA9K8RCawSaIqFc32fu72S7LPh1iMMT_7diD5nxAu2U1Xk6sMfL34StyIJ8vFTFB38CbJoAS1c8PRDTN8bujVP6BlTgHo3_d2cb_Fi9XiqoML3ju5gcthZCW5i6Q0pKkuQB7Uy-0atwLPyRR-y2MXPbIVc9-PUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYExzWWE1uIsj0V0gRiI7OEjijN_b44WNxHseassDCiS8emad3oxDJo-5fqpwqeZ67cyhitY0ZICJWuuL-5kjyAI17BJaRz32INUGkVq-XfTJ9I5B9crD_9yFiSla-8jWBBFLZ6wuVRSqDp70Aw674QZGDizNxlraGHAdvcBE6knnNQH9ZFO3kJbVokc4QeFrwpg5P8GS43M-Dx-ZEEqkzhgkN_OCcFy-HDGStJizzjeciuRPopfmg01E8dkfqyjiAuZlfhpjhdx0ogI1ScqhQlCQkzZiDZ87C70_DO1lgmaMcSc_NSwgIEjm9r4x3MaYu0ilfA1CPG87Da19pT7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ru8ILAivOL-K9CoXTNdUgQGHDtZx356kBCX2wn_3T4SjqNQn66n3QnwUlC2R2DeCljo4KKkvQ0TsNyYcussVnqS3OkphLdfwzwK2yw25MNMsKmNpRLdAGEg9cdAz4rFffFJXK0jk8NMw0qH9XIOO1tuC9ydWhny04nIfu2kOydMCNG4dDSsJvmy0udZjrA2zZnVv1GJBrGp6kcl6xZSFBq3IztTjoVidGMAb3YoxtR9J_0kIkcj1EqT1XO1QmzIMfhEABBKQjv75n3CfzH73u5fmBnCrK5myBPHvpOjbu9Cm4mlrH-tS2wu7bKaYJ8vjMieWDq7p8BQIQC4_grQzYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dm3sJ8YxTvglaM-5ighiq83cS9QFbENWVo_iWmywrcc1gO02O8ACkFgoQzwlrsyudfZa6vApSBs3txnxD_LFiC0-TtSlKhsb1-WTfb5Z1EzuE4NM2u6wKtLagDvKpqZH0V205mWkRn1Emke9Rf0W987xzidioH-HcsJzexBv8gOUijGHD-3oN7YxfnkQJ4E13zHTjnWdIF3E0aflL3nRjSteQqoLbLyHZtBOH6ssjmP2xtGu9hns_lclBA2EAP1VfepSKK05WPI9EjUHLZ1JEmZnvBMT7k4NqrpIJH_RMLKygWJBFwsi_mBD3Ykev-iAkjvBwFbPB72Z66vcEcz9ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dm3sJ8YxTvglaM-5ighiq83cS9QFbENWVo_iWmywrcc1gO02O8ACkFgoQzwlrsyudfZa6vApSBs3txnxD_LFiC0-TtSlKhsb1-WTfb5Z1EzuE4NM2u6wKtLagDvKpqZH0V205mWkRn1Emke9Rf0W987xzidioH-HcsJzexBv8gOUijGHD-3oN7YxfnkQJ4E13zHTjnWdIF3E0aflL3nRjSteQqoLbLyHZtBOH6ssjmP2xtGu9hns_lclBA2EAP1VfepSKK05WPI9EjUHLZ1JEmZnvBMT7k4NqrpIJH_RMLKygWJBFwsi_mBD3Ykev-iAkjvBwFbPB72Z66vcEcz9ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5xm7Lv2XkKiMca5wkGoTjoHfd4vnFBknbpbHCH_KTrr5Xv63FK-j5yUq3zkHOLiAXhpcG78_jILH9Sy3i1Gag-B5Da9ntTEib31rEKixUsj6sgxG3jcE0xXZ6TVUE6-YMAc_Mb4bGuXfcBjaNd_MNLbJkX_3OuxeasTSyyH9tFPCK-jDMRush61KKkhwJ3P9y5XcDlkA8rCXO1HFN2bbrqiMF8nhRaqKGDpt-Z7RSkzlw72r6mkwrUwj85gp2D3OWlNbs1g0Jro9UGifwOSY47ulXe3KI_uehih6Uj9HsK1qxgvon1ZXo2x9tFoHI4Z8aq2dc9Pi_uExsF-wHBekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-1YF-75cPcWLr19s54Swa5AxvpWwLFNHJJmxzAjl7wo8F4Wok4go5Z2D6YXMf92BNoA0oTmIQHsLvsZ36ZLPhiOn7vD7C6LVMK33J_OzYcG6ip22ve2-uI5mnP47EOJsdrsVIfluLWsNU8gWNff2q4VRbMK3-360t5fc2LDAh4F1gL3fsO-bnl9eCp9N6xWD1tYwxxaHiCKIwI_yxthjpOVw_P3x7aigVqWDZaLlflgPonUTUQzzgKZG-G1rzNjurFmciQlkm3Gu_8ZFMnGxynhs4dkRicxJkO1O6533sabQXcvoMtp-Dsvq1sRz4-Of0jDME0fSv-OqTMltS_KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOkgVXI9LOF9neVYiO09PO_sUI7AeQwkUyAXDl9MN1YDbKXOKvLa-mEsUiVeqPCtGbJI1XcWH1U8kkZedtGOmLFH3EbDm8cDUVE_65mQLzL8q6TH1tRRXRBEHyf3wgGnbpm1rx800kLhdSnxC1g_5LUr0_X04hubSAqbptX_PS3C4mdFMbauy766s6SiKQ9nplCHePtLgAyNjP7DlvAax0-7RIhZQrSzh3_2GO2LhS_COiELPXlEgrAxdGDF7u0Naey7QMZqs-yWrhzIM2a2NhKjA6BzAqoAfGbRk7JgdnT3HtLZmOEAWvujSXhLMZbRjzgMPtvnsON8va-a0vmolg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ESSvQY7sA6y4cSIHK6nZsHDLImA-aLSaCFPS3G2Ql1fKXQOesUd1Nq9SKzzy-O2GA3gSgErHjXTEkURY5bJmxqiIp7l7lf2BY_FppLDnd8wIFeUoQCz57itiSDrUHqFxm5ZLd9dk7DdmGghOlfBXuX4f80XTgYf7T3vvYCuzyJxI2gZay_eCP5iXQLnKf3DhH_w-8MP9b-t9hq-fR0edsTmQ0lOTU9bO8n_5ISGQJC2CdwzN9t1dStq1yPy_K1fnQTUsvrkKdpiJWtEOUqjRS1nfOG83Fugrm_H_v1zQvbz8my8bc-hVRxYI0LtoCd4Iru_Mcv5t1lxaNEdBgUws2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ESSvQY7sA6y4cSIHK6nZsHDLImA-aLSaCFPS3G2Ql1fKXQOesUd1Nq9SKzzy-O2GA3gSgErHjXTEkURY5bJmxqiIp7l7lf2BY_FppLDnd8wIFeUoQCz57itiSDrUHqFxm5ZLd9dk7DdmGghOlfBXuX4f80XTgYf7T3vvYCuzyJxI2gZay_eCP5iXQLnKf3DhH_w-8MP9b-t9hq-fR0edsTmQ0lOTU9bO8n_5ISGQJC2CdwzN9t1dStq1yPy_K1fnQTUsvrkKdpiJWtEOUqjRS1nfOG83Fugrm_H_v1zQvbz8my8bc-hVRxYI0LtoCd4Iru_Mcv5t1lxaNEdBgUws2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=LQVhvxiBBmx83PI552f5schLf1XVeC15z8qOdxjn5HdYhEBfJjzt1HQk2MiqL5qvxbS_h1Ybn2wRMbjJMg4_I8aPZMjVuUjc9E5wWkBP9gpfz5DAX6pjA479kq-wWtpqOS3rcxYR4BX_FR1HtzhnnKPJY1Iy7h41rQtsfkm3A5c6GntXBPt3UR1MxdsVBw0PRGX32z_3bk0XhbVrS0ftivK4489dk2nFIV72YS4U8zSTZ9nbotA5Yl1mn5GTOLQJMDmcW-vQlvTClFOdJLggzb48UgczfJkPziJxCkWBMDR_N-044gy45355uskGYGmhggiAUgNaPeZHluonBWy62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=LQVhvxiBBmx83PI552f5schLf1XVeC15z8qOdxjn5HdYhEBfJjzt1HQk2MiqL5qvxbS_h1Ybn2wRMbjJMg4_I8aPZMjVuUjc9E5wWkBP9gpfz5DAX6pjA479kq-wWtpqOS3rcxYR4BX_FR1HtzhnnKPJY1Iy7h41rQtsfkm3A5c6GntXBPt3UR1MxdsVBw0PRGX32z_3bk0XhbVrS0ftivK4489dk2nFIV72YS4U8zSTZ9nbotA5Yl1mn5GTOLQJMDmcW-vQlvTClFOdJLggzb48UgczfJkPziJxCkWBMDR_N-044gy45355uskGYGmhggiAUgNaPeZHluonBWy62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=kanbi4PV6CpURZOuEQAAwQu6cv9pDo0-IS-TraquqzEdWYKyN9QEeFS7zGpTaEiKWlkKJkC_cnjz7Ek7B8PekA-OHXkyWZKMGHb5VbmwEynjLQfXf82DPPPUJ7rmBk5O0fxcmTeHsrNJBBcwc4XDGwtSYGOnGV9UNPl3GCjSFY8hAJ4jhPuqe1tvgzuQfmLX6_GKmNRvFKhr9WyAngz9r39RVrAcr3J1PDaaaV2GbFrPh9Fpe003SeeCGqCyQQPz_kA_Oycv2nCmOJYo6ZYaYyM7upA3GsQeVh7zdRnK_plJKdYSywYcwByXuG2X9JScS16U4qyvrfa2ugzE8HerLT-qPMaV4XK-Lv6QOcd2VCJlqCOqk-40AwnVrmZTR6eTGybrs3tMWSLtxSvEwfaRVDlmjla3440rRQZ6JFdbVrYkAihbKhBG1ZBn45t4g_Zps2ztVp3VFl55XzR5qS1eskti-lBaEmKlFZl0JIpjJf9QqbU-rCq0V06Weq-Y1dRCw_BSOnrtPobDQkhwm0Omt360vWwIOfpMalJhiPNM4TFrP4o-R8GMUzctkPj0X3lUmbrQ1PN4mJsXdrMzpoA9Ehab-p4Eb8CvoaXWivL9dUkyAI5AlHojoDnADlBE5Ryb33sld3wL-Y-QDCiUyN8FN0lArFh25GEAMQMBbbqZpC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=kanbi4PV6CpURZOuEQAAwQu6cv9pDo0-IS-TraquqzEdWYKyN9QEeFS7zGpTaEiKWlkKJkC_cnjz7Ek7B8PekA-OHXkyWZKMGHb5VbmwEynjLQfXf82DPPPUJ7rmBk5O0fxcmTeHsrNJBBcwc4XDGwtSYGOnGV9UNPl3GCjSFY8hAJ4jhPuqe1tvgzuQfmLX6_GKmNRvFKhr9WyAngz9r39RVrAcr3J1PDaaaV2GbFrPh9Fpe003SeeCGqCyQQPz_kA_Oycv2nCmOJYo6ZYaYyM7upA3GsQeVh7zdRnK_plJKdYSywYcwByXuG2X9JScS16U4qyvrfa2ugzE8HerLT-qPMaV4XK-Lv6QOcd2VCJlqCOqk-40AwnVrmZTR6eTGybrs3tMWSLtxSvEwfaRVDlmjla3440rRQZ6JFdbVrYkAihbKhBG1ZBn45t4g_Zps2ztVp3VFl55XzR5qS1eskti-lBaEmKlFZl0JIpjJf9QqbU-rCq0V06Weq-Y1dRCw_BSOnrtPobDQkhwm0Omt360vWwIOfpMalJhiPNM4TFrP4o-R8GMUzctkPj0X3lUmbrQ1PN4mJsXdrMzpoA9Ehab-p4Eb8CvoaXWivL9dUkyAI5AlHojoDnADlBE5Ryb33sld3wL-Y-QDCiUyN8FN0lArFh25GEAMQMBbbqZpC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=p0ZL4orfsRoixs7JdadA0WPOluQtPtx3akH_LGvGmy7AcuzJm__hS0M6eNApHh6VQqIx3oOc8qlOH1vUY6Kt2bKfcBV0SCrDSS0g7oF7paIJPrRvV56c8rjVygidQrNehXMRz1CwHUeJFnFqqc7PoLxUu3kKPbuKkH-IP_QHHa7CCEu6xKOIX-oxfSPvfUU4GEr_QsoMfY3lVRdFwSvbYXtHSu0UuEGNemREYtEndzkSN04NVCTQwjUqF74COV0h0vG23alrGunE7IEW0DwXFg9IfPjjIVpjWG5-PDpd5T-fzBc3mxyAQg3xo406XIQoOGd2Q1oQ1R1DXb7VoUaHR5v9UnuMYwbLhIq7Sajm2kfdjRnn9lHGx_8-F5qyiyMktVioVAgO0dbU0cTE0w6PUHd1cZOFLPyV_Jv4Vo_BbVCRuRFCjkKwuKegcfzy0d2wynl3wEHOADHrHM98NZZyplo5ZzPY_72glGetl9LHmlmlJfksDY5d8znkdHOocRl8DSDInXOSJZEkgwsBZwc97-Orf-uTdwDaSCqc1rci1OU4Viab2NHdZDQ7BIEx_tLYc5w1K7FXnXeVJkS6j3utst_tW_SKYG6dg8baG29ZMJnGhtfLF6Khl-Alqj6pZqzDW-SqLZ_ZUvo2-TSY0du_pu_y2r16Ds9RQ1DLltRHqAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=p0ZL4orfsRoixs7JdadA0WPOluQtPtx3akH_LGvGmy7AcuzJm__hS0M6eNApHh6VQqIx3oOc8qlOH1vUY6Kt2bKfcBV0SCrDSS0g7oF7paIJPrRvV56c8rjVygidQrNehXMRz1CwHUeJFnFqqc7PoLxUu3kKPbuKkH-IP_QHHa7CCEu6xKOIX-oxfSPvfUU4GEr_QsoMfY3lVRdFwSvbYXtHSu0UuEGNemREYtEndzkSN04NVCTQwjUqF74COV0h0vG23alrGunE7IEW0DwXFg9IfPjjIVpjWG5-PDpd5T-fzBc3mxyAQg3xo406XIQoOGd2Q1oQ1R1DXb7VoUaHR5v9UnuMYwbLhIq7Sajm2kfdjRnn9lHGx_8-F5qyiyMktVioVAgO0dbU0cTE0w6PUHd1cZOFLPyV_Jv4Vo_BbVCRuRFCjkKwuKegcfzy0d2wynl3wEHOADHrHM98NZZyplo5ZzPY_72glGetl9LHmlmlJfksDY5d8znkdHOocRl8DSDInXOSJZEkgwsBZwc97-Orf-uTdwDaSCqc1rci1OU4Viab2NHdZDQ7BIEx_tLYc5w1K7FXnXeVJkS6j3utst_tW_SKYG6dg8baG29ZMJnGhtfLF6Khl-Alqj6pZqzDW-SqLZ_ZUvo2-TSY0du_pu_y2r16Ds9RQ1DLltRHqAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XlBaoNUBhrNX1EcEWadfPKukGeYs9BlVzdK2Rye5vahiFsbufWRW2055KaYMIhnZQDHlPgOKuFVXTI-IBV4apnxh1DbEF22dGcQn-GuwiYin7JWdCnouw2dVefwW-pC_ydRb5wsSkHoXLmyXjv9bYqh0yDAoXcZupmApB9oF6UXfXJMT9-oUFjn-Qmp-SatuqyTgcC8HG4aOIFQqxaYK2_HRpcN7Apnby2pBWKfkYegTvrnzxZ5if2fDQ36xnl3qwFHnD-Vpyhx6rvvja7yOZdx9yzUKUlbvwyaeK1UDYA0euld2DhAcPjXqhyqYrKLKTsi4riPMoSwSLjbEKch3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XlBaoNUBhrNX1EcEWadfPKukGeYs9BlVzdK2Rye5vahiFsbufWRW2055KaYMIhnZQDHlPgOKuFVXTI-IBV4apnxh1DbEF22dGcQn-GuwiYin7JWdCnouw2dVefwW-pC_ydRb5wsSkHoXLmyXjv9bYqh0yDAoXcZupmApB9oF6UXfXJMT9-oUFjn-Qmp-SatuqyTgcC8HG4aOIFQqxaYK2_HRpcN7Apnby2pBWKfkYegTvrnzxZ5if2fDQ36xnl3qwFHnD-Vpyhx6rvvja7yOZdx9yzUKUlbvwyaeK1UDYA0euld2DhAcPjXqhyqYrKLKTsi4riPMoSwSLjbEKch3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxrZNBGOd5tzPVNRQ10bJe7GafEDttSsh97Eys4iDfHgR6VXbNKIrMlbCsZhO0KeTCkqwGCWGzmo50WSIlNvYNQuyZFWKApQnjOfNhWy6bA7XgFR8capT4pz0zMN4P9Xl_RCwAtPDhRrBWkNF5L06l6-EIFjPQ0qcGuW-drtnqMSIjSrgMFaoU2gfLTnv07wsu8lyAIHdiLREMqK1bLLrNi47j7750wnrQ_cjz8WI9LdllOrVpZsxMqnhfBoiypiGJnrbxW2o63_pk28x5V4lBC01SYIZPp0uSCb59LpcV43k8Na513dZO3nNCv1H8tAtzFLXaMGbk8J9qPxt2ooWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VNH7qBIkvPwpN-P2zw2NTjwJ94efACtQTybC27kW_G0HEyOLHR2ZL7pBNpTrX7US23d8xGWijung5ProSJm4id4puZTbqZObUyYoCOsyjPDLUKB5_xSuWuMiugVBS2Y3IkptqBBZrWYa0HSqRQys9077wvYioqncYb1FIxXozSBFRcuDu19lZtlCe2eq3sBcjxLiRiAyNdxD0jjtiqxaz8-k7iLX5oG2JVmzTJJ5nnL3D32WQFsYblC1PpU4zYC6UYgDj7f9cWl2CatIyOJU61MrQOnPHf8kZ0zJCg4b4PK--pK1hQ6cxSUuDggjbUt7BbydoWWc40YAA_qIMaqIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VNH7qBIkvPwpN-P2zw2NTjwJ94efACtQTybC27kW_G0HEyOLHR2ZL7pBNpTrX7US23d8xGWijung5ProSJm4id4puZTbqZObUyYoCOsyjPDLUKB5_xSuWuMiugVBS2Y3IkptqBBZrWYa0HSqRQys9077wvYioqncYb1FIxXozSBFRcuDu19lZtlCe2eq3sBcjxLiRiAyNdxD0jjtiqxaz8-k7iLX5oG2JVmzTJJ5nnL3D32WQFsYblC1PpU4zYC6UYgDj7f9cWl2CatIyOJU61MrQOnPHf8kZ0zJCg4b4PK--pK1hQ6cxSUuDggjbUt7BbydoWWc40YAA_qIMaqIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=rOmj8nApjp_z5DONEfrv6vA7XyVGyRCVcQ3pJS-5PUJg-ZgiQST9FdnQgv5aY-qJiSbYHLty8IWTxMCWGuH2_r23jwttaUNdMVtzN8fAJbPJpddpFQ4TTPdekFtWSKapWQ-Aa6nE3dPmEbgrdQvO3-SqyDqTwdG3gVqeEdEEREMvoHaVg3s_aflrgP1m_R9b6gdRP36MrwTYJ7bTu1suwZ4B68M9LWelDkKRZY5UNnhCeGKK6BtvqkAslNj-PPNFWZtAmLypDZxA9wVLxqRevkM1iZuKiDaMg2AoSDP4eoO27VHoZ0A8lvM7eRiZcE-rjfntZI_poGfgvxZY2H07nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=rOmj8nApjp_z5DONEfrv6vA7XyVGyRCVcQ3pJS-5PUJg-ZgiQST9FdnQgv5aY-qJiSbYHLty8IWTxMCWGuH2_r23jwttaUNdMVtzN8fAJbPJpddpFQ4TTPdekFtWSKapWQ-Aa6nE3dPmEbgrdQvO3-SqyDqTwdG3gVqeEdEEREMvoHaVg3s_aflrgP1m_R9b6gdRP36MrwTYJ7bTu1suwZ4B68M9LWelDkKRZY5UNnhCeGKK6BtvqkAslNj-PPNFWZtAmLypDZxA9wVLxqRevkM1iZuKiDaMg2AoSDP4eoO27VHoZ0A8lvM7eRiZcE-rjfntZI_poGfgvxZY2H07nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTB3QseZ3VURCpUA6ZbwiJ3gZc36BtvYsjTwb7hCZ8rWkO_Oe6-uNFTZptn3AQa3RsnWLScN0_VK7CUKmMjKn28J7CsbGLGOHdniM2iYkPIZi4pPaAr3aPgSmWQo9i2-R8eUJdrRNSzW-H2CZ_PYE9rLJF3hRbdlr5tpSphT0EZqGORygG-rP8QiQBXGq3WyV9_eykqMEXPCK80RvaZh6EftXoS8fysa0NsM2J7Jw9k7laN1rfVDvPTlh15KcVO8A7uz0gqt3ZMAuODWTKYgEjM2P68fPuP-E8qyg9zQ1hcX_hAfv35vEa7Bul2GUCbDZheGqnpKWMHB2IIwEAW01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIt5r4mGjUI1dfP49J2800EFiJ1WhlY3Lh6tdR7FV601fFCWHIoiDd8jiz2iEOkRNPD5YdHnxS_R5-p5owE_r-9U0kTB31P3OH-aJHyvz3tyUKWms3PWvCx4mMB1AEVL7mLuni3YWsdV0BgXWo8nE8jbpFKYT8GhCA6Yofbzzmhk5yWObletj4FNmphg_ZxbCjyEMu7gGgyNrb2RFM0xH0QN_C_WZMiU7agyPgAn1QMavHb_DyAQhFQTaw82AfMYGlxLVX1Jy1stE1j8NayBkCsdCHEi-t0C1oW7gw2NEaw3PMcZdihleT4uXQu2Q_7EayL27KtsZEHkqKXDEhxFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhNIgoLIjKj7FFu46I-aqCIoUJu1nWoYuspFdvHj2scOFrotLidEbuiM-Ibu4tTR3C_c4BoQ6jmNe36FjYtQeCbkLK9gPg1OmXJoN6PvYDYX-xJ4QgfkCqv0JoHqcYOeID1pMj6_IPvw_28m8mRyiceYz0Xox2IeciBwOxMS056mAsSWTYSMI_t9nhD3yaPM8CzA5CDwGvNHqPFqPDATUCgw9UUzFteFBnzMbn57jLOa52ngJpinL78bry_pTc1-jzGRzjlae18btu0WTKYdjCaVVSVOzUTlWsKsbHRhBqwtk-gB7iDVPVh4wz--fChAyDt5UW_kcZQZv3JGsnR_8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT47Whi9PJhSgo8UQftfn2pG_I9UQLM5NY3FBsXZociv3mczW6JEsMl5EPKM_bpW1mZHsBpXC0jJbY2khnc4xngfUubpWOuFMOmTu6w1efz-Xyqfs-vXzPCx6QvK3JyvfCmN9R3Nk0rhHKFEfzWU-UdoYt9FvdI4F59RNZWNgyw6rH_SPpoJKplFQjWQVyLCtWmHeChsdd4F9FGSFhgqxvhi-MUmX6_9QIEsu1BCtA4K_V-WMInuXDYVvljTXetDdvSxopAvbA909tnl_jPX_U7VfqV_ro6ey_ftAp73AJHH_UI0QygXOx1Ujhi31QE801G2pIOeO5Sh_Loy1WrDcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO20e3WQsnNB-XD4xaC-DNzTHz9UWMT_S-IB8b09zwJO2uquQFhPGvcKBlaw3HusHhMbRqULMsGCQxwaYPBm_Q2NV5uHuMEnQXwf7oGgD_m__33fourSLFR9-PqDnwUg4MsTpHe6E8oti6tNaP2puMYP6D5gzvrDocW9npvW-uCo0DmZ005_H-i3853OyUBSTqA9yfDVa6VryOh4j65yKJYX0IYjeC2q18D021a-qtsN_EkeLRkjCa6hKCBJKfqdgjgAMSZWT5qJZwpTvbG7n-VahqGu4kf991Iw7ImrdB2Hoo8YC3h-gyJhZFtBIlKNEcxyK_O-LlhzQxK0DIyb-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNf6a2oX0QR1oACPbFZwxhk3tk7wrmPYkKCSygolXbKArVTJ8XER8YM0naZKFWSqEk81O-1SnEgOT5zmfv5eJ6biCMMBmIzp1ZAdxsC9YRUCH-HT8nPn1e7BvuzVYzV3Kpbm65nLbcWzd0JpjH9NTluGGG-Stw7CM7za5bryfpHMvK0KynS53imGUw1Rf03njzz4Fqr068zrt30dZTSyXG0Q4mlvb2Lop7xeo44pIkmEn0uvZOXY1Kx3K4dM3zNIDQBl5r-mg0PZjxinhRfUnuYN6BZX4G7AI2vozjJwHbjEqXJYkRPmsNhhkHg61as0AvKjRde6q4xsZ__mht_RRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntx5Fdckhpeeif23ohEXS4K0diFCO-ZWjT-5oJ2gq5rq-AA8UjdsIIob1hgtUu6pxf9P7CgLI3dGgEdRxQb_GfBYJXK3QBdzitkrx68p4YkKDPIMisk2RKkbNSsQwTCMFVV5JOeJN-mjVvea5_oniWVJps92pCxzI4YjqK-YIOSUbzP_MKpPRXS3az6zhEb_-B0yj6HTjHpBr05_uJckqFpefJznp0T6hDN4FPKvD3irJU8bWW0ErXN1TGy57zT8nbqj4voZfFfoqQFdwwZJwXKsncc_Wxf-fvkXdM8x4CJMJ0oz3moJ7QbH_LY9hLUKGQZSzy7JdQCRGChqCXWCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kiaAcJWFxSmyzTxKOTINjWt33dTl94Qp3jQUFmaJBFDon5llax_ujBupttShW5HBWRVxlwzav8EJwB4y-UBf3GVATnwSZEHA4okyq5qZdLb2ZLs2pyp94xIaDLpjqIlBaVeLzjjC_FHtDAnI5jLqXEBSDXAwauF-UDpMmtY2ouh10eOVcjFzy02ZzkKn28MRVoTT7tSbO0WHo6RJ7-9nMKq5hbD23Gca3UEhSeLKcmKmGRouRYOTfNvdQ4o0QHuAKlUUoQ2Y1t0x3iXSL5LkTjK4nWPyxsGldNsyLyC_5C-1-WA3AR6dfR0m4_834FzpNBxg-fc_5oW-vfQoRaUHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c11IGvOB-pvxGNdMGHKneLQaBw7rFE-9eBFxDtzH8LYju_SYDzpvAhzcoDtsrMvCuGwzabOr-sdnJcm-utWbZjS-hgKwjtZX7bMb2x2gcAPykJ-mJsMiDT5cYmbeFZVisfXCaSEnqV8V7csqyNnxO96DLU7W1Qv3IhmS5cmNpnRyDJk8LohBo9WR-Nm66_E5JoxFkLwykAFL4sEK3l9hv0KBvNsmFVVfidaRx80uMsONKgsQIJpuK8k3JRmWxEpM-jNNVV4Pnzz-OUciS-mGoeAPaKxJf9AFZ2laO_LIuL-ukV1QU_DwNbTGDbxlEp4Ghg571NjFLY4Nshyszaneeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuWdOEBIa00lBmUcWBu0x2aoQxvROODHC5O7RbXPrm4kSO9AZgVpRlZGHFLmAdmmlmgOzariL1IXLmRozg5cjIKyosHJ4NAh0Bs9riA1CbYT7AvPTIxCChG_bBV1XwVcestTVoxz3puGmq862dw7Q_hrgkQ8ccL48Qn7mtwmfX1_-8SHpHiIIQL_a4E5sYsk1pvpNm1b4Cv8oWWq3DaPvtel2ToWFFkoF38UWdM_Whv3nv9hE6AUzf6hZA7Z5sD4pGptscEGssQp6zB6wnyKHqb00YyGQuRFytu3K5cmZNMeBJ35XLP_vbRaA8vD8ibdimlYj3uBVe0Hb9Q7_8l6FQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=CH4_P3aMDVf89X9BI3xU9pwv8BLtxJn_TPMRBw3Q9TgKKfm1yHC2fkI8asnmSxR_NOv33IADC7p1v8y0Nfr1QfcKAOsXyY3OkxTYQAOs2VODdNFJm9GDUEVnwlhMqHavfG3RmPtWhs-GlW99HAXhH3ZW6Y-niAmPsVPTtvbjnzS7-xycnFWbc_ixd8vihEZzTwQCTop_HkfYpyXWxtlBpJSU9QmOiXU-TkAyqNP5BQO7rfafQACO_YJFfv-7gKH5yftTxbfDH38dlOycYkpkdUgbUxE0vs7kdLndHXbgkWCjJTN9U3XKWH0jJGZfUk_Bw7r_34T3KYIzhL09rrZKJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=CH4_P3aMDVf89X9BI3xU9pwv8BLtxJn_TPMRBw3Q9TgKKfm1yHC2fkI8asnmSxR_NOv33IADC7p1v8y0Nfr1QfcKAOsXyY3OkxTYQAOs2VODdNFJm9GDUEVnwlhMqHavfG3RmPtWhs-GlW99HAXhH3ZW6Y-niAmPsVPTtvbjnzS7-xycnFWbc_ixd8vihEZzTwQCTop_HkfYpyXWxtlBpJSU9QmOiXU-TkAyqNP5BQO7rfafQACO_YJFfv-7gKH5yftTxbfDH38dlOycYkpkdUgbUxE0vs7kdLndHXbgkWCjJTN9U3XKWH0jJGZfUk_Bw7r_34T3KYIzhL09rrZKJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lorLUTEuMWRpgtbujdHF-wHUnYCY3YrgU5S5E45SjhXMuA_kuO9VXTOXndjQrRFL3bjXWb14yhgnGZCtTljHK9ZTnKQRKegluie_a1OK-4dgicJHnyVMlYRnnAQqRMiJRbeJ9mLS-YqI7iUcyp2W6l9J67YLXXSBeA0QB0PjwTILTnneNdABnVj1bnvqeSTT7xIVyL-SvPtciqtxu8MX_sK5IubtjXvAzhI2WmyLyDA-6d6tolWH-unwfBuA-MLX3Nd2T9Juax7KCD0aWrANpuK647SDTyUaYRQbYTv1zbF_LQcd-fT1h4MSxbXR_-5wFRc4KNhdIjWwbMlGUJD1pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD8u2DvfNoZlFmmhqd3NBWcNRdldCSPN7v_IDUl5Tz8daRDp-CEMnieNGm3yFD1HuwxpYDgAxymAd2QwpWQqthuBAe_Wtjm7WAPE5LtxU8FXYumHmWCfhLtXc3JKy4_b6L-A3cAXyiE-8sm6kaBXJhfI8vd6dqj9xIrltvDFEnHtC4AzDatwZ1QgthTfejA6fbd3-FTXoBVEOIInQy4EK_bQK0kb1wEvvT8fNGHygcKtaXneDuw9Awpe79gtfd8xgvSTaEY1oTbx2lU42dI8Ex8wtOpflOBPdRKR1iadYHbTCcbZ4clVPd3yh3q3l4Gbz7xMJtWBVTlhIPb16KbOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HR4ZBQJJq5G3g_9kNa6rbt7gzUNgdAZFIA76Lp76fRza5CrBax-ajOzYlvPR5snJGx1yGkFeaFZK1Z-EAh8SY91Pen4xbRNFs0LstLiz646-06-w4TcWnA1BDqIyDHaPQ2aexwg54qxx85u2CMBe06RhyXkn9Gcal4P_R3Djj5g06M5iSJ-6kXETWvuY3qoZBOdvBqzcQJBm4dyD7-vwZfbMJRosy4BhhFQvEfWQKf9BmDxIMEZbZTW6fMBoaxQpEcuRiI4BGduhS2yWAKU2ehBl-__0QNpMep5QQfsivj_XWjfZSbCgwtNhvngsKY1PH4k18AegpoT-m7e2g9GQ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=HR4ZBQJJq5G3g_9kNa6rbt7gzUNgdAZFIA76Lp76fRza5CrBax-ajOzYlvPR5snJGx1yGkFeaFZK1Z-EAh8SY91Pen4xbRNFs0LstLiz646-06-w4TcWnA1BDqIyDHaPQ2aexwg54qxx85u2CMBe06RhyXkn9Gcal4P_R3Djj5g06M5iSJ-6kXETWvuY3qoZBOdvBqzcQJBm4dyD7-vwZfbMJRosy4BhhFQvEfWQKf9BmDxIMEZbZTW6fMBoaxQpEcuRiI4BGduhS2yWAKU2ehBl-__0QNpMep5QQfsivj_XWjfZSbCgwtNhvngsKY1PH4k18AegpoT-m7e2g9GQ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=q1V7ZHN35u9EGRwPXYEhF3_7Ah5cv1Vh4aSs2aCbNXh022ozgkURFRvR2v_jQI-BwsSM5qXkLO7FhJdDd6DC4fbZ6AbFXSKtnKInPA7f5j_OVmExfPdTTxstXqLxqci_GqPPP_6Nu6ZEx1kjs9H6gEoB0oaDaZBvjOSwPSjiTenrisf57gkt8Pwn2pbCBU0xGjmJqogGghon0F0xbwaJ4SSPgX9QuPD5utTdngH8b927S5ViVNJdSUNgJFy3_iurfuP1okT-jLC0BkVpCSik-ebXyTKO5rXh5nbOeScNyiL0gDmNSjedU_iE8ESWWLJPRBIxvzNWIrwiABWMbcBAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=q1V7ZHN35u9EGRwPXYEhF3_7Ah5cv1Vh4aSs2aCbNXh022ozgkURFRvR2v_jQI-BwsSM5qXkLO7FhJdDd6DC4fbZ6AbFXSKtnKInPA7f5j_OVmExfPdTTxstXqLxqci_GqPPP_6Nu6ZEx1kjs9H6gEoB0oaDaZBvjOSwPSjiTenrisf57gkt8Pwn2pbCBU0xGjmJqogGghon0F0xbwaJ4SSPgX9QuPD5utTdngH8b927S5ViVNJdSUNgJFy3_iurfuP1okT-jLC0BkVpCSik-ebXyTKO5rXh5nbOeScNyiL0gDmNSjedU_iE8ESWWLJPRBIxvzNWIrwiABWMbcBAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T39m3CflZswAXHBoeNOdp996hW1su1PRvSK-iOLZw0PZH3MQZac5Q6Fnkd5qVxGynRkarM9pUODO60_MhkmgVAKqFmGn0ILvckLiMN3R4G88Txhszatt50sNGM_fJbMGG2hgNPd2UBbaI4VcAUaaL9i_KHPM-eDW1Qv9UA5ucOQe0fUkkvMXHx9Lpie1642aASm0TGyDWqrRps29xu16pBw00MBBKLfjCsUTxrJEyWmEJYqZVqyfaAaTp3hywi31DsiZngvjGGQ0_hbJoUuSX7xyDMmAD9qssrYIUmVIq9EcN0GmAbq4zJk9pQvepTJte7EM4-kYOoUWIEGuvDFW1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5Z4sEcvsWmvcJ7_n-qbtzqgYn4QS_UFlGGeCuBaNaBzus24IlHnivw4nJXTl7dv1480D64XLYfqZFoy3A3LNSrAvyPSEkE97odYcvR_iY6u6pPIM-GJ_yMyG-lmbv06KHq8EeU7kt1ZNkgBP9AezGltpcrBO3U_z1ujUIBpKT7nMy0TOBZDNoEvWLnaLStKCohdH7l2QLKn0BQv67tCSxm0NzDj0lDw_Sjai25lEkzgNu8JNgwTJBZAGrzmfPIExnuB0j8xDFMEqUiWoEYu6mlcupbTmNhzdO4IaWRe8dZ3W3hlfKBFdCg1MIqf9UVvFdGsGPuC_QhoNLWaUNwmdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTlVTnGgzWlH9ayC89S_hbHCN5lRThnyyNA5BSebO8yNpHaRorDVBcErkqKkcc4VX3YnsBDt5MDFx7nWQqG9zQgqQpe9GfA3a2TospSjJugP0XSqzGVGxuswETRhMDBH5olr3mV-KNTBSmwGfPJfc6K-YcuddKELF-8fN4Q1k0WFhYhxGTPgboeBGDaJdqdm7vzWoIcFsMjQWkgojcBd4EGgmZ6wvfr-k0T55pch7EiROBMsl3d45xLyJob_EgBolAr_X-Cj--jSHzzTuJae2AIH-sYl2A65MvmbsAM5ywiWK57vmAdpRqWxZqCmt8A3AtKQrAiwSSVxZCNjSWfVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkzZDR7Z6npGJVEkGa1exklZt9xbjmRTFkqjZDrZ5XwrPrIyrKuEl-QFktDU_dlm9A7MrvsNWPZ0xLtRzxHAwtyL3TdQlVpc1Q4MfLc_pqWnf0BWF2NnITaXVhkjexAcIIYQDM9vYvNa2ns8baJkmdPo_4Nx7s3JgOGTuVcIh3PyHoeNO_N_-eXbxJJ_kBCWyUenkscgdaiZBA0WocGL14lB0BdtvbZ4IuYMazJY-TpSBO49c0EYt3aPa1O4Kv_DO09s0-rAQQz-10WZh0qUP_9dpBt1ae9b820y1zhOT5Jun64NkANqAWodHvKGYNosTQ-U3JVoy61wh8j6-DjqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz3cZez3xu0WkWHQ3tfctl-NuakkmsjGV7ymqalV14QruS6WVEFbYgoz96txHCtofkHp0GwYef49x0I_Taqhc7r1z8Llv-Bly2C-HN43ERBTtkAtpd-92YQIai_39J-uE3ECjApNgtOwkbaoj8JqHQPgamc43yrR6x0m1D2zKcffOM5E-369vwVJDefvo8WJDrdGuXMEmkXC-S4an1yAVm1xuIlnuKgN1Xl9V6c4eIkSgKMHUM8NmM-ZhhbNM0SBdkfHlXHVoSkTdzZoXr26NvdG14EUs7zpKY4UjlB0rtUin05vxTtlEPO9kQFqT0HnNdb9B3ic2L9dRjPTdizJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKjArX7MYXRAFob6oEO7ONMip-gtNiBwf7Tf5eMwduxXKFjXzqXriNt-3P93Q5cRWqpIWxVav_-pKsGbaOqsRdUIc0tFQVVRcx3WEjydo06KhyyXQFfmOnxxIsEfbxQxIGkrWNlpdOwxAEfaSd147V4XprZ_yMn6hiZsPM2z_rX8cMOer5vOhpOHWZ30frBQ_3IWMPE4TUE8hyog5-IBHbk19I-bR9UP-W6c8iSa4-Jh9YS8u4sVi-xNgb97mhugX-E8BMIj-CZn91hdDojY1FfdI1--YeN9jFgQxXvzHcGLebiCP9LgxKFxpRZ1HDx4NRdm8u-1wTL0S07PTFhOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoqXz7m4JunbXpVKnZgYVUvcLQzjktsXHTV_7UbcoHftIhFIt7tzSBY26tyo8Vkt2tRt8DYl0Nnfcl8ye20hz83UCxe8FA6LGa85AFHMPi-FiJRO63nQiAe3_KLlX2Bl3nFg1TBx6bTx3cyNS2n-oIfq8s3lrMfB1nTpe7zA3HG-KV5xVeaLhgWCIMNFDnttpS4LqM3qVUMTFtan8K33QCzfnDAhk9P4NhaoBAA8pi7G36AKKaCpDVedwvzQYlP0RvDRrw4cL-QibTqKUpx0R6pQnN6K2DQmwu_8HYcYpLYnMQIxyU0cs_a0FyBknysXIQ-Rs1F4ITOGGis8SjR7EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PRtRMjlD3LKh6x_LcWxWQHbxpik-y7J6Z_diBHdsHNTaKJMD_nUcMCCJYO9gAab1adetpFbAwi4WKXYek_eyKTEfm9_PPIOAL3e4GehukVhOaH1IKpok1Icsit7qj5F4AsiQO7kgwICieC2A0lMonLRV9_Jn4sbzZDaPnQ1I7kQIq6UJQWfgI4CsdKJKENZQfj1LpEuM-rHG-6pdgFYUv9nkZ6Ni0LVxUTRCsZE43UT6sJNKdjs4Oa4_n3ioH70epg3HUsihqD8wWuqGEq4WM6_FvIPFsiimPkdsdONbRaovfl2saUMr83ghXNwBnjlZ7cAOYJ3KgGpxhpeQ7UNGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PRtRMjlD3LKh6x_LcWxWQHbxpik-y7J6Z_diBHdsHNTaKJMD_nUcMCCJYO9gAab1adetpFbAwi4WKXYek_eyKTEfm9_PPIOAL3e4GehukVhOaH1IKpok1Icsit7qj5F4AsiQO7kgwICieC2A0lMonLRV9_Jn4sbzZDaPnQ1I7kQIq6UJQWfgI4CsdKJKENZQfj1LpEuM-rHG-6pdgFYUv9nkZ6Ni0LVxUTRCsZE43UT6sJNKdjs4Oa4_n3ioH70epg3HUsihqD8wWuqGEq4WM6_FvIPFsiimPkdsdONbRaovfl2saUMr83ghXNwBnjlZ7cAOYJ3KgGpxhpeQ7UNGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB2JEk7IkogN9uj8Gh1Ku11b-Fyqr695ydWgDjqQNTJodqpt3aoBC7hovNIW8nnoW5QiBwA5ZxxZeN56L8yErCqXN0jf1aT0naV9YX-hy1BD9epr3S2HgMPaYrs8CDNv1TgDfYGdNvbF_LvcoEsVT1rSv96XzSlVCnYyNsq1hdgndjQMZ1OYf62NUmWlf_j1ft9pNpM_ZgH2Txvf0dzjr18yqHMp-jmNDQl46HPJw_qMxlb51yKE3qnT_MZG5LylGSDLes41IcKUAGylv-REnn_YDDTDHoyJaNEgVIuABHPZGT6QCkaNTMapcUSRirDfmSmHq8nC2E9X1xxfSEHMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FffyTszOhzH3EZTeuZp7QCrEO4_WPQYpHahdI-yyPpXM1sORGhukxi9q82TTD-ryQdgINePNkM3e_iEM5MjPO0qxmR60R6EK1rgopFa97ISqRcrZuBY5khpbQUKd1goAnc1kfoR39w1E_sNgOZXYXpDr8tbl1HvZ4A7tQU1Rm9P38UGbTU2BZ-ubvUionDrC_wnnnNt2SBAQC_mXuWLwSdVTcPcoG_vFEdOWY66g30_mUgiAXoceTdLdSiVH3azSdSwfm1LW72lvvMuT8rxUSlxgjuN8xUlxbaO543jU9cLafr9uBjkFXyE66uyjDI2sQ8ZgutGtWEB4R4VsN0F1qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FffyTszOhzH3EZTeuZp7QCrEO4_WPQYpHahdI-yyPpXM1sORGhukxi9q82TTD-ryQdgINePNkM3e_iEM5MjPO0qxmR60R6EK1rgopFa97ISqRcrZuBY5khpbQUKd1goAnc1kfoR39w1E_sNgOZXYXpDr8tbl1HvZ4A7tQU1Rm9P38UGbTU2BZ-ubvUionDrC_wnnnNt2SBAQC_mXuWLwSdVTcPcoG_vFEdOWY66g30_mUgiAXoceTdLdSiVH3azSdSwfm1LW72lvvMuT8rxUSlxgjuN8xUlxbaO543jU9cLafr9uBjkFXyE66uyjDI2sQ8ZgutGtWEB4R4VsN0F1qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=UBbApNmrR7Pg0FOMU4zuep3a1gsIyTbB89Ny0-ZXhR6p6rwwyqNc6hld-41LtVURdY64cK-5o0ForwGD4fFjM-zTuxZcUu94ms4XPvuxP9j6zQQAamtFu64aJwRbRLz2_5wKb84pm0tHqMXiYpCsnSxW3pUHrk6QL1ruAIPPsgV5Oh6tOceQZVj6jgM-uaSDhsF4Y-ticiWBQDv9QWBZgiBDSMymCGLIAf9REadZaPIBxXyxqbdrxouarw4SsUHuiRPYAiWxoojCB0uq1zmN5PkZCvyfPU_nitRQFYDyLAurTOzIZjfLFowrU_3VBP0SpVq5DhTJJOLVAg9uUounwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=UBbApNmrR7Pg0FOMU4zuep3a1gsIyTbB89Ny0-ZXhR6p6rwwyqNc6hld-41LtVURdY64cK-5o0ForwGD4fFjM-zTuxZcUu94ms4XPvuxP9j6zQQAamtFu64aJwRbRLz2_5wKb84pm0tHqMXiYpCsnSxW3pUHrk6QL1ruAIPPsgV5Oh6tOceQZVj6jgM-uaSDhsF4Y-ticiWBQDv9QWBZgiBDSMymCGLIAf9REadZaPIBxXyxqbdrxouarw4SsUHuiRPYAiWxoojCB0uq1zmN5PkZCvyfPU_nitRQFYDyLAurTOzIZjfLFowrU_3VBP0SpVq5DhTJJOLVAg9uUounwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlZXvGQ4dx5nKrqQpMnxbkMqJs01r7R-mZdBPdITi7Bhgktr_FS0UoB66V7mtHo25tkiomgf4Bjf9YPeK-m4JWaKG2DlyoqNxANenKZ1lf1AZsxZ3ZiL3UiznfiVxwegFc_cBZL8AOmVfsWGbqP6j6_6cZTHEMLuMlkirttz7umXs1H9_JVjw-AiJe8odNiOrGvhTeVTuqxbPX4dnu8W4Q2_jl-uR0IC43X29hKUPucHcUOZ6bdIC77PlkWNfgqBlq8BkZqSX-N2GYQ2FEXCC20Z_0PrTpKdbkluD1vNcd79RW6SeSM7T0zieM6YIwPf7xNd9qZCtxf7MUVEGWNJeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJYCwqHVhX1duWG2Ob494q9PyIDmKLn38mZHEwDBZqxWhKSgQbF7BvCcidTWU0YxtDm7OtD7UBQ3EvHtrY5LQL2LZ9ExdR6rMe--oj1J7ARjQvgfEG0GmF97ttBYC-vtg6JjR542g5laoyXGoYFNtbiwtXGubhcck8uBgg_s0ADj_GXnSn6FBpkn3wSsWscdf0JMQQE7KybBiXaDSYI2ErTe2-IQFKRahOQaYJbAHi97YoK1gdjwl5rCiibbEyuWa2Cn3IBs1-IxcLh1DVZkTivmrSgxjARnUHWGw3Hf6wbqkL5uBxh3GXL4e1tt3yqNJH0cDdnxEcZm5z7QhtbRuA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=krNN3WmehPy5jc8FGSLxJmT2hLVTqQfb3kjaviqKd1e2JK6D6bKy3gIloDVSx84HQNayTZ9Khk_MLi4ljnc_ncZ0xpOQ4772xhCslRT8vVrW5itn9PHhClxZa82y6-QjjgtKe1aXzuav0ykGm60t725tZNGwuYGCjUrZeHoiqo3iHjHFoi9cTCxenWqkH6UWY_DK36MbnN6PrJsbUWwNeSBbkg0Cn_ZV7rDhQnto-0nJlHlUgdZ2u4X9uTMPOymqe9tUe2L2M_I1y68hEuk4gayg9sWj-VZfl93n_Jolp4PGd-xxRuBXqv7by5d76w0a8rBBLSkq3LzN6GdtvpuyOGbLmYdoWg1dGCVUNwVKGWQL3iQZ8fad-pbxepR-Oa5HQs8PPLZs2AFkx9YRMjw180rbNFhAZh6uEOTrrV5RFHM4pd78mQdwDTEli-U1t6VzZPTEmcRJEaIUvmKHAQUhFSondgzB0b4DwgnS84-dNaGG8Uy6TN3ZCr8GZ-K4yZKUW_D26IegiAaFC8kH7jxYSgegDv6X2_97xyx9474Waw03UUGitOWo8X7mxVwo7omMmY6y7fHj1xTo1srssVVQktKwzSE2Cf-HzwcB1pAs3wHGcLi1EE8zOysEHUA5YJaZ2HLpLxO-YFSb0uLdl895M_PnWJHEYNmAWAZp9-2x2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=krNN3WmehPy5jc8FGSLxJmT2hLVTqQfb3kjaviqKd1e2JK6D6bKy3gIloDVSx84HQNayTZ9Khk_MLi4ljnc_ncZ0xpOQ4772xhCslRT8vVrW5itn9PHhClxZa82y6-QjjgtKe1aXzuav0ykGm60t725tZNGwuYGCjUrZeHoiqo3iHjHFoi9cTCxenWqkH6UWY_DK36MbnN6PrJsbUWwNeSBbkg0Cn_ZV7rDhQnto-0nJlHlUgdZ2u4X9uTMPOymqe9tUe2L2M_I1y68hEuk4gayg9sWj-VZfl93n_Jolp4PGd-xxRuBXqv7by5d76w0a8rBBLSkq3LzN6GdtvpuyOGbLmYdoWg1dGCVUNwVKGWQL3iQZ8fad-pbxepR-Oa5HQs8PPLZs2AFkx9YRMjw180rbNFhAZh6uEOTrrV5RFHM4pd78mQdwDTEli-U1t6VzZPTEmcRJEaIUvmKHAQUhFSondgzB0b4DwgnS84-dNaGG8Uy6TN3ZCr8GZ-K4yZKUW_D26IegiAaFC8kH7jxYSgegDv6X2_97xyx9474Waw03UUGitOWo8X7mxVwo7omMmY6y7fHj1xTo1srssVVQktKwzSE2Cf-HzwcB1pAs3wHGcLi1EE8zOysEHUA5YJaZ2HLpLxO-YFSb0uLdl895M_PnWJHEYNmAWAZp9-2x2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHs-VI-R2J-tO2qTiJjG0GHulb2xyeqDTuLnnO3nmda3PpbHsr8TrHsTcB68HvkEgIogFYJwAbGXrcbjDUuouepxgKsIk4_uOo_Pb7u7BMQwaYgsFCHRAf_8gmt3Csjj2AexroZwH7Z5rwG3eKgL3eUpyrPQcc7iOmQ8ySjySWCY5PKF55s8iON5e_rmw5pMrqruc_yoU5ZeJLZL4cRWb8PkkAR6ESpLBMmPcH1HqmjYcVJ3shuDLqtkwWTXAqFhq1WUhm0Qt2zRdAspPUP92k8CeRzTzYL_UWcBisEsjjqsR4gGOflNE1Tp5lJEPcbWWX5VFV7-hkR2fjoL4NNj_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ZdbNlxxlhHeg5NAnnDfoMchSAsJfwKYfkI3GCKWK3eIaR6VK3o7c41LRvEXE93ZZspf0y93f4hKnn-DQwCxJR-mRtSqK86D5bOr0vzliAaolrOX6XLb2nhdrRzF3zfZ7AvQwzhJc6EtVB35_CqrNzw9caf2L-RYYGOV6SX8EWC50FBf-uz5fGyB5YI0V4RjqijV8tnMAaBDqz_9wfyD6UWaLdIKErSD8aB4Mxyz2py_VYQ8l_D53nsvMd93GgUcz-AhErycgEWFEP1eXQriwZxroqFjzJmrIWzJWi1Iu3xXutBIhN72mTFE90vo_7l3YlBtyPJzk98nZjjwBPZJvDr16vpMf6BPM3dnHw4BXp40pm0VgHBWqgzua8W9DdMcBuU5uuhmrO536uUoSOWVDdk-EdPBDMDSKz_GE85R3sYwwiWyGSAyH6exiTCMr1yo33XSdHpjOREvY20jN11SZh21aEAnAympZmGZ9Cv75kGQ762zif6VLmx0Bo3QS9fDjAkDqysASDOe-Bo1JEcvuhiPBcKWXY64w5petWYUCULEDeR1QeIXCH_ol7fDZGRVgIJAVv--t6_mMOyudA8uc_CzraL__hGYKPjh14FP3VJbRdnm3k0cceyKqxqodsrbXS39do8VQACIVGS20s5_xRbxbwTE1miClhHhnxbDIjl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=ZdbNlxxlhHeg5NAnnDfoMchSAsJfwKYfkI3GCKWK3eIaR6VK3o7c41LRvEXE93ZZspf0y93f4hKnn-DQwCxJR-mRtSqK86D5bOr0vzliAaolrOX6XLb2nhdrRzF3zfZ7AvQwzhJc6EtVB35_CqrNzw9caf2L-RYYGOV6SX8EWC50FBf-uz5fGyB5YI0V4RjqijV8tnMAaBDqz_9wfyD6UWaLdIKErSD8aB4Mxyz2py_VYQ8l_D53nsvMd93GgUcz-AhErycgEWFEP1eXQriwZxroqFjzJmrIWzJWi1Iu3xXutBIhN72mTFE90vo_7l3YlBtyPJzk98nZjjwBPZJvDr16vpMf6BPM3dnHw4BXp40pm0VgHBWqgzua8W9DdMcBuU5uuhmrO536uUoSOWVDdk-EdPBDMDSKz_GE85R3sYwwiWyGSAyH6exiTCMr1yo33XSdHpjOREvY20jN11SZh21aEAnAympZmGZ9Cv75kGQ762zif6VLmx0Bo3QS9fDjAkDqysASDOe-Bo1JEcvuhiPBcKWXY64w5petWYUCULEDeR1QeIXCH_ol7fDZGRVgIJAVv--t6_mMOyudA8uc_CzraL__hGYKPjh14FP3VJbRdnm3k0cceyKqxqodsrbXS39do8VQACIVGS20s5_xRbxbwTE1miClhHhnxbDIjl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvkuyFG2JJF7URVQCx7FjQDtgheyRhRXftINt6kkxd7bfiKnKm2vA9iT2NVbrAUfR7jUVMG_nhtRLQQ8HLsWx0GA7WAtQolIi9VFlx4JwsBwyxmET6YBBJnZj3VfEC5W3M_28rw3ZbNde_Q1e3QW8CojWd1T1_xfmXrcOOL3vhU200OZqMExRzA3viQoaiUDaxA-GRGI3__TrV4xjt5zu6u_jG7nLx_NQOaYIx4BiH5EROKtbxRGo50F5sE4TdwRFPUp4J48dZdn8V07lWISVYwUGVRMFYzqqMDN62ZnBEA3C4bK6Ms4nDaDbpyPfooC2sLjjYK8nb3Io3KGuvZgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_7QCd9k2pH3AtF3aKhA9PJmNxixz70VOvWC1tZ-Ryr1jy9YR93YkH4ngeKi5xgQWHh0qiuZej8OQdz7_5xq1YvGxS2qnml0BoKbPkvITTulefCJQK0Fbn592HdP4VCxXvOnhPLkmAqECsMCWIOhv6MhGV9ny4z_KJNG2aY6lFixp0xoraglrge9irW6C0tS19e4tK4sGJOZikcBmBoRSE2GrhMG71AlYTirkAIWSIaLCxt7LVwT99jQe_Peu8UTCJdMWW0VF6UmruX7ajcl9Rtb_IwuQp4kODdoq3lztbSeDUYjG4Bzz3uRLPdYoEPq0eM9nt9Gv1IoHS4jUNHIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfaM8eQJddSVpB-yG52gNo1gakE_mOy2RTxdHsEDtRjmIug0sc4wS8baqqeJnBunOPYJ4otDPC2qMCeCrVgp19uYrTtQ6sfiQLN1Px9mWYaf5tGA-8zy7nwh7tEyA3lmNuEtxXqSNnEu3mlNA9u0obctVUSk0YaenZKe0qz_D32IHuzN3N6Soc_MGTI_BoYe8AYwheJSsC3LYTuK0Llq7RjJYJvdoCcHRMh3jBz6B6C80INri1vn_KHbeTnHIn_ljwjppjfWI-b2RI3VtapX8dUJyF-3O_Ly6XxkDrSMOmmrkuBJ6yuJcWMiF_tqyzP8rA6xQsyz0Z6Ci1f-EsGzlA.jpg" alt="photo" loading="lazy"/></div>
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
