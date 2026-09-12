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
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcKwjLTQeWxPSoePnxAuQd21WN7DFqbTk1SWET9CQJq5Yc_NUhykV9byFhNQeVBcyxbTNCceDdPXrlR41eGt4Ey65koA8HYYUqBEnuj3v6958SD10w8AOKFbpU5_u9WD2zH9tPIx0wZxSwaWjHlhqiIHFlceuUuAJ6SLecOQeyQH1o_8fGhrQpDXDwst5Mk7YMB6KR-tQFEfeNhJMcGCBgGAHCbqE9FqYm5KHz7d3G53niFrrzlhoUSAHUj_9AE_KxzpSqIsfsH6Hk4ABBcyPDS4HJd1hJuIF0IS67WAqO24GA0BU-_bJpFp9bTkA3eG_FTyr-VQ-M651RBPz3B7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=OM9NT6RSrrPZqhqRVgJFchsKcoy24t1B89anOdCPRH2oLIj-zrZaFSB3Ix1UhYyfjw6bwi_yJ_ACR0DUVQHCcjHRvzG-l5obYWJxpJGqjA-vkUbi9KDjinWB-PfhXI5I_XIE-l2m08Q9OEz9-qV41u8MQWLxKbP2YEnAu-1DuA4v4EG-LDB3xdAmUBYu55QblcuvVh0dx-AnniPcxJrtkJl1OlL273bj6UKYMhQIvP28DJB6o7_M8g0OgmvTHyHEr6lkq46xK8I_Cm0PGPvOFz3-jbWqczqzMNPiJD_GsY3do3zom245OLju5DD6cNeFlU2hIuuwvpqiXuNPH1xf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=OM9NT6RSrrPZqhqRVgJFchsKcoy24t1B89anOdCPRH2oLIj-zrZaFSB3Ix1UhYyfjw6bwi_yJ_ACR0DUVQHCcjHRvzG-l5obYWJxpJGqjA-vkUbi9KDjinWB-PfhXI5I_XIE-l2m08Q9OEz9-qV41u8MQWLxKbP2YEnAu-1DuA4v4EG-LDB3xdAmUBYu55QblcuvVh0dx-AnniPcxJrtkJl1OlL273bj6UKYMhQIvP28DJB6o7_M8g0OgmvTHyHEr6lkq46xK8I_Cm0PGPvOFz3-jbWqczqzMNPiJD_GsY3do3zom245OLju5DD6cNeFlU2hIuuwvpqiXuNPH1xf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufymGUcxqqr6P0265ZaWiOUi3Cs-B_FvCbEFyoVmgon1uRjhAxt2W2SmwNNy0YoXKb_XVZFamZomgqvdmhFbGrINYWwx9wWg2-nDL1dPf4KgCfy6pO33PUtnrkjL5gmReg9orIMBkRMm2c9cS9ZpOcd5Q-4lX04KUZHSs7w1dJu-F5z5_HPTiTA0EpwIwoLUDSyk_hT6n7HYkKjHN_AHBR2EALVhsCx1Vh6eV6pst1iThEpU1zzZedKclvLzEHY98mKheQlGem12X1FgCo-Jn72spjE-W_zG9hauTqpx1igaMnsFA8V2iKd-jXxj_nw8qhoxCqNHS4HkhrNMtVrVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ed57uHAALtMuPixeoYpXOJXLBrsD7WhBZL4zQO5_n2F5x8TXmhyx-QTTCFYuFkJMODASEEpPGpxf53QDSGnuRt0GFNY1EBhuGQD3WFb6z5rspbUyuDj8LIfBKOwEViLU7AUTuiOBYN0_3Si85MQ_qRlAEf5qHY0zWyEg_r1neIyMIgFLxjaszPYhWCw2qkFQSVIvDCpFc6mxj5zXgZ1ZzvROU2XWibSBEhnzO68gtUK89_rgCf7Gjbwy_PO9moyInNUVlVQZxXyvPUoXr5f9u2C7AcbW722dk7PMX2duMRrWnMZ635W535tKZHvpty3Hb_aKwZQ7Cy3PxNw3cRMEW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ed57uHAALtMuPixeoYpXOJXLBrsD7WhBZL4zQO5_n2F5x8TXmhyx-QTTCFYuFkJMODASEEpPGpxf53QDSGnuRt0GFNY1EBhuGQD3WFb6z5rspbUyuDj8LIfBKOwEViLU7AUTuiOBYN0_3Si85MQ_qRlAEf5qHY0zWyEg_r1neIyMIgFLxjaszPYhWCw2qkFQSVIvDCpFc6mxj5zXgZ1ZzvROU2XWibSBEhnzO68gtUK89_rgCf7Gjbwy_PO9moyInNUVlVQZxXyvPUoXr5f9u2C7AcbW722dk7PMX2duMRrWnMZ635W535tKZHvpty3Hb_aKwZQ7Cy3PxNw3cRMEW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jMYMJsO6wuNVPxml3v3J-tEPzl2x8H43ZpDU8AdQuH5rPNuzhuNRyL0BLnTP62wbcgKiH-zEox5dYM3O5ceHBilbHbnd40460ttrrs_oixaAfP5dfd5to6PalYyks2pZ6AWwcYrchMF1IDU1grpuIKyE22TzZiSeKd2BU6nyqb4GVNf02Au5AYIYHqE-jXzPU7mPgu0RGCknzLoD6gopZMWvVGZNVEJYKyuB8oX0Th1s9J2_WzCT3s39VdR4BwgZFRXVUdM0zkYqs6TcAYdE66IsWaR9kkbBHKvfrRfFW38PxMwBtPnqib4c5d1wqF_G0cWRlua4b_yNlKxn9Vfr8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=jMYMJsO6wuNVPxml3v3J-tEPzl2x8H43ZpDU8AdQuH5rPNuzhuNRyL0BLnTP62wbcgKiH-zEox5dYM3O5ceHBilbHbnd40460ttrrs_oixaAfP5dfd5to6PalYyks2pZ6AWwcYrchMF1IDU1grpuIKyE22TzZiSeKd2BU6nyqb4GVNf02Au5AYIYHqE-jXzPU7mPgu0RGCknzLoD6gopZMWvVGZNVEJYKyuB8oX0Th1s9J2_WzCT3s39VdR4BwgZFRXVUdM0zkYqs6TcAYdE66IsWaR9kkbBHKvfrRfFW38PxMwBtPnqib4c5d1wqF_G0cWRlua4b_yNlKxn9Vfr8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxpJ60aTc1VZ6tYdp6SUvz02oqKSrC9377oBccecTD3bRmvtbyl0muPF7vGfG296lavMEi7pdtrMJoQ44Kx9adlElbZTaYdxW5IYzvdBcYhmohChlhT-RzV2m2W5OXU1CvkJxr6ECH7EczWZoVgAZSWyag9qAp232gtlA8le4HOnH2DfgU4ECLmco43UqPHvlcWdxy7IPhxezqxa-BSOUmwuO5n25skEB11YVu-Ov4YKS9kwdC6ivHVsMY36psS6E7lyYJEDfQFyzhPlIwAofInh0-DcpPOm5XwEtzpf27hhsBLdxDc4Oi9yV7fYruv_uA8OpbapC8EnprCKzD2-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTqENFgoA_En8sDsNMbxgrdoZqf645q5l7e6AXOrkHmPiSmJAgtdfLiYEczaSigtKvnIiL3ptj9ijz8Za-_yQZbtC6ZvKMtC0slCRAyPz0QIAUZI6oJ5cQiGNcVja6QXQHENRkdUv77bML1j6uinYpMFIOWWSZYfFy4FTuhnK_pVNvjTs-5K5qYPhJublBhWrmstRMrpFv1p9qwqaV_CKdcFVhpyzkrPLKdLh_kroZWw4mV8OdIhb8GYrhk-0wbj6fPE91ZlbwmF2UQvU2jmxlU8A4gU7ZEbIT3X5yzi8ywipFa6vJdlETztfYm7waF5Ga30DAEBgHZnHKcnBXN4jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=s5N_ve3fZ5DC7qU4RECmtMaq4v4TTc8Zl-5Uf1mWGofwqzEGDTEirPC1FYJ6fry-FLWtjZ41Aw0IVEO3HKZTTDA55-Z-EPne-gEBPW2GHg1GR6fBC_E8Sz5X2nMRb8E5JED-Qi4zvo8OinNWytWtPQCgxLonqHaoe-0xMLvVrsz602tvPyKEC07vDAMFe0bWnATLSnwcPfKn49zSo6WYtEI4Py12C_tXxTVTvfxuJM3imp3nHo-VwtlBig8R98cUmye5wPmrAtgQtvVe8dSNOqVw_jrkhuGPeG5lKZ_foeq8d6DU8kY8DOUUP4rftF9RYQ_-RsDwSTuEEIkE0GPtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=s5N_ve3fZ5DC7qU4RECmtMaq4v4TTc8Zl-5Uf1mWGofwqzEGDTEirPC1FYJ6fry-FLWtjZ41Aw0IVEO3HKZTTDA55-Z-EPne-gEBPW2GHg1GR6fBC_E8Sz5X2nMRb8E5JED-Qi4zvo8OinNWytWtPQCgxLonqHaoe-0xMLvVrsz602tvPyKEC07vDAMFe0bWnATLSnwcPfKn49zSo6WYtEI4Py12C_tXxTVTvfxuJM3imp3nHo-VwtlBig8R98cUmye5wPmrAtgQtvVe8dSNOqVw_jrkhuGPeG5lKZ_foeq8d6DU8kY8DOUUP4rftF9RYQ_-RsDwSTuEEIkE0GPtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbU7846FMz7ifCR42si2GE8RAMLKYGJnpr7tfeNUfqxULpFcjNUiSx26XUwEshAtw0YARbeypeXKQ6sZ3y2ACYo1eEuvfYKZyFrPoVPmoVJz06h5O7X4JVk1oc68A7lwJCuB49fTGMqFQ3NoCtSC5vuf7RPzobw7Fslq6EpkVQHH5kEfAf4yJeoA6P8F7R9xvyjlZJtmDXWVEjJ61V_2jGImktXHzqi0YI9W5ynkygzauSGoKUePX6STlZXhBzFegF1PUAfWpCki1dW77FFP8yzEVqokwslmmbQf06wqPidPE6weNh2JdRC5zmMz110amNflcCEI0MaoDrwX8h_kRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3JUK-0HT1lpQNbmxCU88AtsgrgT_eUanDqMZ_aYFnPyit6wmgj1ah1jheeZGdg8yz1u0MrAY68KyXa6Yz1Bxecg5IuiovI0tbQbE8aiyz4FMhy4QtuU4n32qvrTD_8i5TDNfCrhlxK3eRSPrfi2418XgxorcOm1RvEfHE0fE3-St3q6P_lmhL-kSQ5R04JVhw5FgcWtRxqoBwvw6E_cS3inuTvpMn4-8VGYIbAb9VpOslY7LxiAYA5nDXEpoCIq6WiYM6W54IB0JM9pQo33qslVZvy8QHMMsSh73ltCFMrELNQ_30iGNzv4ldJ_uV6BhsdVdT742roJrDmS_Ij93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNAxaDwAIfMQfCIg-jq4D8Q34zLazZg8cRKxGGU9qrTY77fUWu2ivQYFqF1Xd62BinetT-0UccHcWp0yIkJgQ9zu9QwnESDDfmL9qzP808EVMkfrQruLXsi2hYDzKM624vfE2CFLAkh0cq_N-V8ZXW6LrMKEhi1W8FkcCpI-K_e1Jso18JOpZFE3qeyd8DmtVIw0bO1K9XzPy095lOrg33Z22Atr8QG5o0zxM3WeUXXWUlL7q5Gz3jdt8q-vvvB8-8p9IlfNlO34LMhpBEjO6ugxFoxFvjmMRudmaBJXeYtoAx6fMPmXbp4JP8r1oE0qZ3q7T695SsXgq9AJYgfzhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DRLtpFfxnoyu_sOSaj-1KQnT-rd3svl_D9LmI0PXYTVXBCR-f4ybmqMICYAzToSJ6MsuZ2cs6aVWtlBhGRufMkd4rne_X8ZZSmL3WZo0iJ6PBYYz8N3rN9pnQlePMaZ52LSKGDa-utvZggNoZrXlD1s1Oejd9GQDjm2f5T82SWi9M50xD5tO_kTKjJbsVT5KZd_B3CYxPoTyNnyCV4p2WBOuuzOrLnHTAjs1l2G5ReVH6k1_AYLqtT8pJ6sYEq8Yxty9WnCta_MUwATueYaNtvzLjVSsMJ-lHgCcyJv4Ux_9fsg5TpGVUJoLB20NLu88_UR2N04gwj-Jjegjz-c7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DRLtpFfxnoyu_sOSaj-1KQnT-rd3svl_D9LmI0PXYTVXBCR-f4ybmqMICYAzToSJ6MsuZ2cs6aVWtlBhGRufMkd4rne_X8ZZSmL3WZo0iJ6PBYYz8N3rN9pnQlePMaZ52LSKGDa-utvZggNoZrXlD1s1Oejd9GQDjm2f5T82SWi9M50xD5tO_kTKjJbsVT5KZd_B3CYxPoTyNnyCV4p2WBOuuzOrLnHTAjs1l2G5ReVH6k1_AYLqtT8pJ6sYEq8Yxty9WnCta_MUwATueYaNtvzLjVSsMJ-lHgCcyJv4Ux_9fsg5TpGVUJoLB20NLu88_UR2N04gwj-Jjegjz-c7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=M1o5o8lmc2uZkGfJ-gQNjSbo-ecwBy0CFnE4bCXVklcuG78XRAFN9NJWgPEChstQUIVW3Elk1QGPCBoDbkG6deatyvXJBp6FNWHuUX9ARqPQIDcq2PcDxNJcROocJxv2ZUYSlKxvBlcd_g9qowijGmG2Rt_E7NqEpRNAfYy7stC5SDB2VetxqCUA0rHRhKb8PVtxVr3NFBPGQ0kmEhmlMQ1EK6tDyvUaIJn89XVLUp3CDCGb5DKVG0_Z8NHFMht1TRMBocmFjX6UGQUxa8257Nl1nfUvqm0olcFkGwlRktSN_FnwqJlMfmersILJXjW0EeAtnKxiErqYkWGe2slkDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=M1o5o8lmc2uZkGfJ-gQNjSbo-ecwBy0CFnE4bCXVklcuG78XRAFN9NJWgPEChstQUIVW3Elk1QGPCBoDbkG6deatyvXJBp6FNWHuUX9ARqPQIDcq2PcDxNJcROocJxv2ZUYSlKxvBlcd_g9qowijGmG2Rt_E7NqEpRNAfYy7stC5SDB2VetxqCUA0rHRhKb8PVtxVr3NFBPGQ0kmEhmlMQ1EK6tDyvUaIJn89XVLUp3CDCGb5DKVG0_Z8NHFMht1TRMBocmFjX6UGQUxa8257Nl1nfUvqm0olcFkGwlRktSN_FnwqJlMfmersILJXjW0EeAtnKxiErqYkWGe2slkDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=clZbrW9KCWQV8LRigHfQTrBoOwJk1gNBvrP9g-NI58s7zmK-fvw8qAEDiwgYLg5Dr35ly-a-PxcICf-Y2x_9ma3HCPA4B71oMv5JqNWpUxT0lH8e4KqlKZ84C3EoBEzdgnrQ7x9ULFTJrFWx0BFfnY9VRcHdbEfHA0jNA5bsgfUVRAHIMzm3tPs5WAcibTLSI_yjubdfVSIJaNcUJMD4Zt3miSE49NazwrJhK302OCKV_twsSWmcmBDawQJE8ZD6p_bGf-29axvd6W6Vf79dV1c6ATb6vK01w8NapI1pnyczxFnxJsbzZ3MXQR8Pi8DlVFBWbIMGTXvNRqCeTXJmcA6DdNF-emGsFQa2DYlQquUgp1LD47YFYXDGBtPFOpa76FtV8x8Zzzt_GE6BHhgQei45ETfYje16KBViieXIWwTPv_re4ZwaV95UouCZfUsEQBR_Yh1bNsoe5fCOLbT7Up0z9QWASclBB-FOGnRpaxQLY_McCBWkg5837bCtFc5EdC8d625QPqrziImp4RsKZH8wKEMONvXsD5dr0jiZKQAbTlnCMkcuk9Ue9AWXPWv99d1m-ui8ypusia0KKf14tYNSSfPHRoFqIspnDPXH9nkHMNKDSXlJ0UnHvUO9Nl8o1ikn3DynKkPQ39pDjX9_LbufnEkCD8EzpbMxOS-rfy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=clZbrW9KCWQV8LRigHfQTrBoOwJk1gNBvrP9g-NI58s7zmK-fvw8qAEDiwgYLg5Dr35ly-a-PxcICf-Y2x_9ma3HCPA4B71oMv5JqNWpUxT0lH8e4KqlKZ84C3EoBEzdgnrQ7x9ULFTJrFWx0BFfnY9VRcHdbEfHA0jNA5bsgfUVRAHIMzm3tPs5WAcibTLSI_yjubdfVSIJaNcUJMD4Zt3miSE49NazwrJhK302OCKV_twsSWmcmBDawQJE8ZD6p_bGf-29axvd6W6Vf79dV1c6ATb6vK01w8NapI1pnyczxFnxJsbzZ3MXQR8Pi8DlVFBWbIMGTXvNRqCeTXJmcA6DdNF-emGsFQa2DYlQquUgp1LD47YFYXDGBtPFOpa76FtV8x8Zzzt_GE6BHhgQei45ETfYje16KBViieXIWwTPv_re4ZwaV95UouCZfUsEQBR_Yh1bNsoe5fCOLbT7Up0z9QWASclBB-FOGnRpaxQLY_McCBWkg5837bCtFc5EdC8d625QPqrziImp4RsKZH8wKEMONvXsD5dr0jiZKQAbTlnCMkcuk9Ue9AWXPWv99d1m-ui8ypusia0KKf14tYNSSfPHRoFqIspnDPXH9nkHMNKDSXlJ0UnHvUO9Nl8o1ikn3DynKkPQ39pDjX9_LbufnEkCD8EzpbMxOS-rfy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nXsqTT-O-7yVVCHKHRYXu1wwGO5oJq7qEvwHpVDytwZQdTImKT4MmpZgcDX8ILyh8LokTUUCfL7gBDkj8d8ZKigRuBuOnODdCDOQm412GQpgYHhqzycpgQuxo18nNg7v0ugtisTuWEAiuVEMqIHfpddyOe9cWe9nxFMm1BAvvlaNfQ0oriQwb0gLks5yRV-AFgPEvNnqAc-et3WBajLUK3K3A7WLGXBW8lpPy0QABf5xAX-ROatFIIAYeuRQY471TQQCEyUaHAkqYW3uUz75qB4ON33N4gEBLw44hXQVP9ZaQJuxY1Mf1bLC6IHV-hW63-ADChgePQEIcUcT_iS0C1b6I-S1yd7I8Jecv4wk7AJgT09hkhpIjHw-sskWUdZtB6_O-UwIBzCVkL0fhccJUDYT9wrqB8uGxyjpAdQUHI1raSnPdDXw-MtY7osM3dpSfVWHEBzaxTqSha9qhoVzKiccmFQ-Dxd03YcRRPUOYs_LVChLEjYNkMaDFxikYk2JN2vCpXADYC4d5khqb3mqO34pvzzvf1w8mJ7Bh-lL4KFaIptzpFfJjEJ6iO0Tq7-8w51fXbEwdbCM5Xi-1HAYV9zg1cS0UPR5l4bEhVvr3Qs7hDCoVjma5JNYD9Y6k53il0ePp5J0L_yNLUNoxiOzCEY_0HWPfjSJgqlJ0TJYfbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nXsqTT-O-7yVVCHKHRYXu1wwGO5oJq7qEvwHpVDytwZQdTImKT4MmpZgcDX8ILyh8LokTUUCfL7gBDkj8d8ZKigRuBuOnODdCDOQm412GQpgYHhqzycpgQuxo18nNg7v0ugtisTuWEAiuVEMqIHfpddyOe9cWe9nxFMm1BAvvlaNfQ0oriQwb0gLks5yRV-AFgPEvNnqAc-et3WBajLUK3K3A7WLGXBW8lpPy0QABf5xAX-ROatFIIAYeuRQY471TQQCEyUaHAkqYW3uUz75qB4ON33N4gEBLw44hXQVP9ZaQJuxY1Mf1bLC6IHV-hW63-ADChgePQEIcUcT_iS0C1b6I-S1yd7I8Jecv4wk7AJgT09hkhpIjHw-sskWUdZtB6_O-UwIBzCVkL0fhccJUDYT9wrqB8uGxyjpAdQUHI1raSnPdDXw-MtY7osM3dpSfVWHEBzaxTqSha9qhoVzKiccmFQ-Dxd03YcRRPUOYs_LVChLEjYNkMaDFxikYk2JN2vCpXADYC4d5khqb3mqO34pvzzvf1w8mJ7Bh-lL4KFaIptzpFfJjEJ6iO0Tq7-8w51fXbEwdbCM5Xi-1HAYV9zg1cS0UPR5l4bEhVvr3Qs7hDCoVjma5JNYD9Y6k53il0ePp5J0L_yNLUNoxiOzCEY_0HWPfjSJgqlJ0TJYfbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IFnKq82Qdk7bPCN_QaC9D4Mq8PjnbUzGZZyilEIRXDSVz9qoMyTyY1qEHoWYe3dfjStO-b_nA-H4rneFl2r3Bhma_vZVrBk9JHD8sP83i62RMVI2eb1FFqGhSZgwu63Pk_N5LICKe_O7kGkpRLKZ5OW44wVXmuLJFZnk9shl5rX5TOs-fEthN1lTAP75Z5b6xH-tWqJm45dVCTzUVsRNyBBPHOvvvUacRhurJfNg4VrfckNOo5e2xzaBBAk_kzRXcroIiFwlpixaXoqt8WYANAIQ0TAnphbSRM4gHWVmMG9jrGjtNrTnSScuKPx0suadFmCd1twHbK5vku_Q7QWidQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=IFnKq82Qdk7bPCN_QaC9D4Mq8PjnbUzGZZyilEIRXDSVz9qoMyTyY1qEHoWYe3dfjStO-b_nA-H4rneFl2r3Bhma_vZVrBk9JHD8sP83i62RMVI2eb1FFqGhSZgwu63Pk_N5LICKe_O7kGkpRLKZ5OW44wVXmuLJFZnk9shl5rX5TOs-fEthN1lTAP75Z5b6xH-tWqJm45dVCTzUVsRNyBBPHOvvvUacRhurJfNg4VrfckNOo5e2xzaBBAk_kzRXcroIiFwlpixaXoqt8WYANAIQ0TAnphbSRM4gHWVmMG9jrGjtNrTnSScuKPx0suadFmCd1twHbK5vku_Q7QWidQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXwtYvPiCBxNO0ppCeht_SX44eCqpbsOgbpJMQX937oUp2ywHBSJifOqcIbO7UncKudJLSWOF1rxY1tx6bwrHj4iGS04n5hUZ8oTtxDLWK_T_37VC24KLdJ2tIH7S0gJQcSUTJtmxs-tZrYSORDJHN-f4fmDfA4oHvasKC_RmoHTm44IBShNSFKW5VB0cBIdA-uIBuSdpmvTnLJnVm5M1gahRjWXNF0Vdmgl8e5-avT_3pZx4qiwczeyLWNXigtuM2UC6NMN2Pk0QpSkvxh0MFTvkgX1WMgpNi1ltsmhSKs3vfgv4ryMy3v_E5AyCop77g8LTkD3rLLJO0jK-2zq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bhW2XHsPdxtdre1GwvSyKlz2a617p1Fp_lqbKx2DYTTDqT8d-Lt2lBT6T5jLAYqVzeHCR4dg9xWEpvOACUzmPTp2uZ9HrC1rhmYJzAtxpgoESp2Mnr6EjfjxOw-Od4jKqP60BH8_oXPCr0k9F1KjtFWWdsDJQ8BjcurdDgcVVW3c-Zmbfa6hSjl2WNZ988QREzOqAXm1m07UOIfss0BipGUnT0k-7Q4wSpKBO7ScDDpsAVbnYQfH4DmXAiiVqgwmBzL7lpmnNTNWICOwrjFitDQouHG8ZFNDp9oGsNTYRtsnqnSAeMMm9crLchx0aszLGAHzKSKz0GO3UcxbTDmSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bhW2XHsPdxtdre1GwvSyKlz2a617p1Fp_lqbKx2DYTTDqT8d-Lt2lBT6T5jLAYqVzeHCR4dg9xWEpvOACUzmPTp2uZ9HrC1rhmYJzAtxpgoESp2Mnr6EjfjxOw-Od4jKqP60BH8_oXPCr0k9F1KjtFWWdsDJQ8BjcurdDgcVVW3c-Zmbfa6hSjl2WNZ988QREzOqAXm1m07UOIfss0BipGUnT0k-7Q4wSpKBO7ScDDpsAVbnYQfH4DmXAiiVqgwmBzL7lpmnNTNWICOwrjFitDQouHG8ZFNDp9oGsNTYRtsnqnSAeMMm9crLchx0aszLGAHzKSKz0GO3UcxbTDmSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=QGaI8N_LyvxlwQK87m87_GeojpW52ul-t8OMq9b_dwAvCePoTsxLooG-AQQozrLa2futU9iP2mjq3-RfrDjfld47fiaglpeCONFHNVURT2olHrYkdSLu2w_jFD4Sjg168mKRIvJB8bPhYMjTB1V3_P7TJRDIbM6l4uUU1yNGxWIHdlVEj9Wc3GT3nUvtys23nqGHcXCSUT9RfDQ-G0ENvOtxyaRfpjaXYXwfzwdNS2BUf19mPvk0AmZ5dQJ_2J2aMp5bCwGfc2TLNYnQbHtVYPvvHdZ_UHIKERjOEGhwf53lMmhfyPhuclZuds_iiEid5O4GwOFLdtChWadCgXevTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=QGaI8N_LyvxlwQK87m87_GeojpW52ul-t8OMq9b_dwAvCePoTsxLooG-AQQozrLa2futU9iP2mjq3-RfrDjfld47fiaglpeCONFHNVURT2olHrYkdSLu2w_jFD4Sjg168mKRIvJB8bPhYMjTB1V3_P7TJRDIbM6l4uUU1yNGxWIHdlVEj9Wc3GT3nUvtys23nqGHcXCSUT9RfDQ-G0ENvOtxyaRfpjaXYXwfzwdNS2BUf19mPvk0AmZ5dQJ_2J2aMp5bCwGfc2TLNYnQbHtVYPvvHdZ_UHIKERjOEGhwf53lMmhfyPhuclZuds_iiEid5O4GwOFLdtChWadCgXevTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkFPZZhAk3jQwC3IMOliiCFY4dsMRRwajQphXAR0g_iV7CAjaGuwc4jtZqsCGBOTLrL3lxxdAIfShAEmNammdFeo_KUBYSKVSkpwZHnHKrgB1dZqx8AGt7aOuYTaGiLR6jPQPA50489Q9UsUwqObEJsC__mNYoLA_6-WvJWaOsyw8QV3ErZ_zstUvOZ4VWCe3AJtjOWJhav0rGv2Gdp48tkScY2WmwCbBIFE5G8NWixkd9kSxkG5AMzR_h5uWuhYvpKrCrMXrwhDn_iVrZakYWSXNuOiKaKBHIGShizrWx2LyZrvVZR8bUzUcoAuuD8dghaKXEKPpwSL6aYj4orMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx7OeQS2nBRF5nNs9nbJo0Na6LSuJjs2jyhJJWkAxwzlBumkOf5idymOCX71xOtntNneJUXajJuuIv5xsi4aVNCcfRGHQeYoIZWPpnC_cuBhlEyAL23OMxMbe-IYs3RUrTSx3zVHg490ThRyrWBPb3lLu3826TZEcboCp43JDxpcIswm4_K3HtW85pTm0IBzS2eETva2hn7EQSL7pgFyMORnU2fs1c7IWRfz2mLLfHfYpUGw7nLxTs3LLm-u2LHEQhhlqQo6bA8bPzM-9clDNchtVuP2jmS4yV2WH3vJpI_5PIkEfb16Bd5m22_GoQz-JVQ8VRCzioY6FUP-bszpWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWQtJVIKkfe6dpZwonQ7S0ImIxvstuEsL77uhJ-xmaRRKJB0ufwB-hGCh-V7r-DWsIR4671YtQC80rUrr1O7o8DUfChfc5qcvySbEnFHO_LPnijNHlFHA2l-IEJDY15X6pCB0iyB-u9r5ErStHx3VYygoBh4zqtGbV52lVRXMMRbexeC_9tsEDel8B7duuc8nEr4FRmXbLyBzvjUEbnqiY8KuSLNR5wG-iNifx39pBZX7oE7-xrEKv0VmrffPFdE9TEKsHoRwizK2OzYkRuXyuOTwugbjWjk5XqKtNY9oOFloI067eL3Y7-IyVnQj9VHhVDSbbqxsxgN1LH7POyhDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am1CuP7usXW64Ih7xhM38RDtIp1R0lMHIo5Z3UQwLzaGjhG-tYXsqN3R27KAIvy4GlimOx0BypaR6u6PyGsGSe-nzXYcvrOY7g3wIhuLqyXt2XP6Oqp7YPts16XD7YwcGGED6xioOKSGWOWk8fb97sASL8OYVkuUjTSUdCW6XcXVWutQZ5zt7vcPu_oE0r0MMNa5E-Bbefqr-t57IhJAv68GMCPENMBce_8u9hUZlfXymgNRgblKb--PbvS1pJR29n6zReKCB1dKoDlq3AIgZXQ7Wc760TzjMexjzwoyBVx2c97STR7te6AIQHh-yrJpn6FOaNd0gbAWBq17EtZbNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMGZ-o6FXk8624euj5RN7lijQsmWDX6Fwwj2mwzhZ6d-_xzv72bPkkOjHP42Q_vr2nH5TZstStj6a2-53lZZBT5KDkIYXVKJYsfpbNwUI9A2KDzUWWTDC9vHIvQ8rsEWA3FIV3fbKB3xKVFISM3---LY_XKoQJiN8JqVc1VlpbftAAZT9WnTQyDNOK8BSpiKaFAfphE7mK26V7v6AqmaH65WpKV4RYZfY7e6RxtkBIVeDmTrVSgkHS54zWEp8guUQFi_6s8lYuCSS-AgcecnMVB6G3YWT_h5QaHfEphJce-VIhanwEngCV3vZbRd-hM0cTYmwuO90cxztmcAhA-reQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFSJQ3v8eZ3JBL2Wk5Btypne8PURmLEzQGKxK_xknKrogcsxY0KZYnumt8SAHmh1il4jCwjdbMUdPG6Dt6-dr6jEx4m6DYil4yZgd9a4xRC3dSmJf3jOm5PDmbaxcNz1uHtoL6EC8Z0kgTrbf1iM7c-CmTrKeRghWa3K3-pmgTLWeBixFV6WpaWA4V9Bd70oe7Q6gyNpIAW-vAdJmL68OB_rHNw2bVWxSZYBy31LfHrvdx0mVaeFNmf-ajtJn4eq2LPI99jr3mlACmSklpePj8f8gPZxSznYtQMIACO4Xx6LzC2Gu9dgKkYJ1jm9qWCEYKaHqaTcVU-ozjpU8pgfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V75-hsWqxW_UW5BYP-nKCuCMYjM5bp470LMd6PsJxkOHk4J62O3OgB3khJpD_gLBT7_u2q9Cxnbb8ygeEu7WE7vz0pCJwgsg9c6tYawbWWD1ddN5fOdzyjqlp6Zf_cABP5uLK--DjV2M19ljfYzYJWThBbE2TD_5nk5wf4UPsCtNzA4HUq_cYJS6NZfAKVHQ-SeRAGLXaFp17sqZ7i8K4ZEz1v5mXG0CWPIcLLR1J7PZPoVwfIOIo5DTc6-VG69gb0mvkD3vBEugfJZRJ45k7QP8gN8VCrIccTX-6-b1HGfAszDTV_XbCBArf_W0pyEMNy37oflro-DzfGMNUMRIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuPkafRmWDM_kWS_gxhrMW9bkke4rW0p8dVtTLd1cZgcj2n2ziC6iRwVrPQMfBf8nHwL-tWpCo5SFfkSLUCag0aeuUf1jOEzi2F6Cfnatz7zYhvGtdy5BwfQCZ_botH4z6eJqkWdKiZxtQf5N_Xbt8bw_0SyrP3rJXXfuhRVAX6pq_bFAugPLZqAVm8Wnokc2cPeXnjOmUjScd09jRUQxh23jfzhE9ukB0t3_VsjdbcC19IYwyZKcLuJKSvnC31sZB5yIvjZGsUgTeadBX5HF4PL1DBSW5VoSTLyCpFG0Hoi47tYktUIu_ZmaUjetVrKcHLxK8GGkphdLz_qmWWjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKCq2pUZrQV7QXe6t1wtCQ-1eUXYisgCQKjH6CXeGTTg_sjse1B615o9n50ymyiF9UtwtkltMGcSxJdX4fsNYsS411ACchNB99FRofEuGXR6FuWxRc6b5UnZ70tGj-SiRDU_fFAv2xBuNBbW_dkHiDpxxMyP1ngsfpUOlO73LHMd9lW24NLC7TLWDBve6XDmRG9Jw_UBrvJF0gTeKlvbEVAuxoQvjaeKt_YkFb7HZ-bc3FQ6l35T0qjytJHDK_unPkzbX0tgX0iH5Hkkl4ujnK7b_2rvq4YUabQjbzjRaIWA_fIafff9NlQMbRAu9TzXr9iBGd-5d3otMde1CkIf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqzlEblebVDFiGM5eldNVCfnsa14a-zmDvT0hWdfrKCjtMgiDng7vILB9UXu0nIM37K1JDQWTKo3B4hLX9QNPmJe9JzX9xvWPpKmrPUbR0Fqrv2i-RGKnYjmT5fcIjyNkuwdpRBnUZyIG3td4wjKAg2byIwcncAemXYlsCsFUFn6AzSHHwFP8IYVsw9luvRkbafHpBjJ7bL-GZPWtprLGNd-l2iCBNF_fve-wRbfhkVG7r0kUE0lKIExT5DKc9cMY7pq7BEkhYuytmq4i7esaPYJeUlepZoj6ilD89sA0YdCFM-IS8hR6z6j9ATRPjLUNHXFZmBHdCtv23LlKYFkZg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=kT5RFaVj22fvoAOzqb4SBs7rsTCtCSIofi5xRyTLwH2nc6u8Wo0utBzVpQsNpuSMyjyxHapITIwHgS7aQ2u4xePwOr36mK8rsmbkIsmk90TlBv4op7wJhClX1M1xGK23k4QV89dz_C-4bdV17I0Z_9DjOekOb34Iw0oWlSCb8E2apG82nos4x1WFsdae5A2aueVbvALOz0PnEYOj8hVhIv8o0_MmwhrfTSZtuAifIK9oLujUhAq6CiYCcHOVt7dwci2CMTe_QOxa0pZHnbqPZ1KP7y88SfahkrEfD0qFi_-jFdNmhvTJ0TazLK4MquzL4GwImWdxXft5wtGd3FpYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=kT5RFaVj22fvoAOzqb4SBs7rsTCtCSIofi5xRyTLwH2nc6u8Wo0utBzVpQsNpuSMyjyxHapITIwHgS7aQ2u4xePwOr36mK8rsmbkIsmk90TlBv4op7wJhClX1M1xGK23k4QV89dz_C-4bdV17I0Z_9DjOekOb34Iw0oWlSCb8E2apG82nos4x1WFsdae5A2aueVbvALOz0PnEYOj8hVhIv8o0_MmwhrfTSZtuAifIK9oLujUhAq6CiYCcHOVt7dwci2CMTe_QOxa0pZHnbqPZ1KP7y88SfahkrEfD0qFi_-jFdNmhvTJ0TazLK4MquzL4GwImWdxXft5wtGd3FpYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq21mktvxwxKEbm-Twrt9dFJ603vgPOl-c9exYJyJUPYo51UC5TlLjet0QixwBYrDC7Dby1_UtbGUiSWrjQpazASBA2lRLIvE2rxmvXgCssXq7Wb6dsl6xO3CUlfvi8lA7bRlF3aG_1wnc95kkTB2t9Tlfudwd_Excv7opeVh1CL46DqEenbYjfrvQ1Swk2tIni9Mi0_on0vAgm2i1nEDQ3oaN0HNSm6cxTOViknlglFfZs9zIX5-G8ko6kEF3ee3_H9YRxx3l1DMe8OLmGdbOG00v60hGjOUchqTxLiaw_Zh0yB5JgD4iS41b0m6MpAQfd43LEojZY-I0jnur6kIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYLo4P5-q3dEboljCf4rx6x5s32CT-j-6LEZLaiFQG4VhvJIZ250rR2ir04pklVuL6L_XfmqUlwWe57-ACOaMbSIv6iKqpYeGkYtKO3dZ-wIziLgegR1dytxweyaZchXQCeWaHaeBZDkQvFl4usnncUF2OqGLxVky1kXdKyAvzX2PaGC7WeXl4QYSh0aUikz7FvgPVEiMnwi8stPrNsELmpGKdk2OrMbuu6NgBhH-M_Se7T8nlKcB2YI9EjD9OuvXJEfj1gj87q8MVllXLmgT7ZIFUeSJYruFyY4sf0zGXabODhH2wBy9KIGCTwbM3Z3zRZHuq8utUZ0lpneGXWh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=bMOD-f5LlO3oj6CXFLmIL2QkAPezl3t7NCsDonD35mYM4LGMd-lrZTlMxd203_YLbuKVXrOEGGS15csxBz9tOeRu0M2M4xQs52ZfEW0Z_35B-ROJ7iLeiJVfYr8A-sXzpzCJk1YPGkpntgaGUTLGQX2v8QlL8146cOH92D3vN-6ikJXFn2xwVu-4LkAa85PZRErTQWTs2eKxbJxmnmpCExYk4VYa22zJ2TG7tdivQA2SaclkrKVXU8gbRBGMOsEGmLqjEHfWJgihiziQ2ZS4Q9ywMdxjXNkiI0lUPYIuGvYn067ySyj_gLXjo7sZX9CctSDPzJhhCgkjJ3rMLgdzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=bMOD-f5LlO3oj6CXFLmIL2QkAPezl3t7NCsDonD35mYM4LGMd-lrZTlMxd203_YLbuKVXrOEGGS15csxBz9tOeRu0M2M4xQs52ZfEW0Z_35B-ROJ7iLeiJVfYr8A-sXzpzCJk1YPGkpntgaGUTLGQX2v8QlL8146cOH92D3vN-6ikJXFn2xwVu-4LkAa85PZRErTQWTs2eKxbJxmnmpCExYk4VYa22zJ2TG7tdivQA2SaclkrKVXU8gbRBGMOsEGmLqjEHfWJgihiziQ2ZS4Q9ywMdxjXNkiI0lUPYIuGvYn067ySyj_gLXjo7sZX9CctSDPzJhhCgkjJ3rMLgdzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=UqeRUYlwittyqOdG11BPlAFgsDEbvvubRI8xjOe55pYSw97iwjJW5wOlC-0zpaAEXEogkI3ciBCn9__UDrgGUug-JKChw8V_iB5WGcn3zn-gCv6VecEyLhKKRaSOSTmGk8QKJ53Lu_sm1e5wRcAxQXBVL9VIGg211I2cXNpHV0f88N79nKceRQqmR2lLTs64oYH8UvVx0OIZN9e2YNcjBkSXP9X9k91gK4sxwOyYFOe5_dw6T_2zO8J9uqI-O9kmbN8MpWz9A6NXMvrGp1nmzIWPG22JVBQwmvp8vr2tZz0OKDdSJFoSPRjB-KLj8NVBQ__eTIuXL6qLvX1ldECd8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=UqeRUYlwittyqOdG11BPlAFgsDEbvvubRI8xjOe55pYSw97iwjJW5wOlC-0zpaAEXEogkI3ciBCn9__UDrgGUug-JKChw8V_iB5WGcn3zn-gCv6VecEyLhKKRaSOSTmGk8QKJ53Lu_sm1e5wRcAxQXBVL9VIGg211I2cXNpHV0f88N79nKceRQqmR2lLTs64oYH8UvVx0OIZN9e2YNcjBkSXP9X9k91gK4sxwOyYFOe5_dw6T_2zO8J9uqI-O9kmbN8MpWz9A6NXMvrGp1nmzIWPG22JVBQwmvp8vr2tZz0OKDdSJFoSPRjB-KLj8NVBQ__eTIuXL6qLvX1ldECd8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcm0Ta6eyfRtzjVMgTamFufa0n1TLRce5WD5yjez6HTatOZp-Y_E6d87nFCCUL5QKsj1YPF0yhL1Sx7RZPqf2WmxlNLVNYTXv6natFP8ORadxqJm7r31JaodOOvwB7qVSGwaxwge2R8ey7RWh3hD29negMpChZXhf_GAm7nxTtuiZxdwo4Hm-s0GjNhlijxVg_JSpj3Pj35cD5cwGNhoOJvKvAlxbJTAltf7B3clGQ6vyc721SbM-3HIzOTzTVKGeZiK3Hq4b4oz-hbPF4tqLdj4vguWMqrPdk2XbDlf6rNTvOu7ZGj_WzNDhPJEGao5hLZjWWBu2O3fS_a8Y6hkmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzB5bYp0d_R7OYX-qnRTaNzV8F9SgcFOcnULC7bOr1sDPLNUaI3ct1uGbuMV1QldXGiajndma2pzW3a7zp1DlRExU4yVGPQyA4gm3ccVbaiZvD-2wliG9dkwSm8L5U1rwHcoikbry06hQ-Gzw0mllTfURXOqVd3-ELzLjGAqWIFieFH1fB8BOfQuuMLnwCub3oKV1mu8H5R0b2drIOXDolF213WRfceaSLtgCTRCMLskvetbh_r7RDWvCOEKqAsQ0bZ6uxsiWaVUOXpXUdN1nj7YQ61909J2K7cHuhQFzAJnuu8FT5QQNjcX_TN0H1faUddfX6tZQnnJVu1yHC0XQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faTCKAMj-fE58Dehof-wp14p71kmncLj8b59q35oBIlumLY6HueSS4fTEm2o9SptTynmW3TMx9VcLgIcnXfeodSCe-MqBmL4DEH9hMHE9FOEsh-wxCxFf1KJrehyZnXugI0fCXhFTq_OIh_HqBB_SabmErsakSbEzV2XiBlcIJQ9IEXfbjAWp_DLyRd7CEzLkbrUR9BqLnsOmEDGMWiKyai8V6Jhd_nRz3vb-IrPYKhsJ6XtnF0pWYxjhP2inL9EF6-SP5mmc9splzwSA0dlMxek699u7e5jPN31LW2v8TgBmdqQg7DNyghg_CVxkffiZTINssVoHNdtjAsjqLHqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXo8y6vGRjStT7AGldKcMwH0g7cjfzSEQ4bwPHS9Ans5ikdkgOY_DAGAelxXW34Z48xQ1wZAfuXEMayc27_ybPnoVlqjn4OoII7yg0cKIeEPOiY0_Z671TAkp7ZlK7vrB7eaJra4eGpqLW_cdZ6CIKMBu_ZvY1FMJZ9zAmW-MY6ptamDmZ_s5ft5QMX5N_TNvGcAKf0BFcV3xeOrcV-Kd8oI2t16bZyd-Gvteij-2EZDv2asY4zHhbZ3JTF9onXuht62FI4qv9qz4ZOTXQ0uh-cCveXc3Muef_GHPsq-TrcFmzyxUwnYSHPyKaDnI9ODO4RnT3vh5zdrSBE8KQGpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNl5PAQvAacLvN4Ci9A0HaDLdvoWxwBXb0SuiSheJZlUjXq1fRKomegvqhJJl0VxihtVZyc00kLTHUka9A078DAIwD2rdK7NEAGMeZW39mYAEHMWJGWRwIGqUcmDzTKSa-rVfqZ0yTGlr1AjMRloXt0IcxeFMT4DnDjXatQKxcjXNe7CeUJW6-93gofQ8q9BbPBW03e9B1kUdLf2MkrcXTrBXqAL-2JKfrTm7eqbBqLgzYHVcMSEP_Y4d1lqOT-RbIEdEhNqIeuLg1aJzcOuwDimw1ES72iNOLIiGij20cR-SL1VqZNFZdrVKhig5zrG2P0fztr1aPGUSBZLjl1NSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXUX_MrxQjy62SPlZW3sGgjfRQeIKvHiKRCpm81dmdqZYUyyKOOUOFM8S3qD3BGrTeD_kRHwE6T_pJ1TUoKqKAxLPubaxWbKU2mTGSgslSxnBFpKUod7q-yKtv2VqPyHtG2zhsSswTr2j3GOVlGgbthdwhYCVe_zWsVnR3F92K8LJA2LOWgS_iO20GbE7VShhidIkXF2bX643vhLgDHQTPnKF01ezGPTqpu5Gi-J6dBZuy4GA-Oh4L-7WZAyWspTTV5nB15QOK71S_GjZTLtT8PchmHU1XusSTMp0ou_xmX1Rm0k7mYN-QD2kbDufVY75xqbXJBR1GlLPZLLuSKuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJGNC_tfdI1pNXjrLy2cvKl20rT20MbcFiSiVZ8BfvsFnZZTwWgeZDRGdmAZqenosDKp9fYI7ee04ae7i9mNEhtWCseVx9XCmKyKtZDrJvfpnEV6D1cwXubkRmGnheYAchjKgutqDq5KOI0Okbkiq6E77vTdxkIMSBjIK95CiJhA-lNIIvV9CAQdwsfIwzWK9T0T9IR1lNlb7MzBKUV3NPF6mFvNPkd6nahEWxEgEfj-uufnHbKFLFF9AXzDuV0xngQR8Hj7tcAzoZtJ4-Rr1ED6CW4KK8J8qluvDfDJTyvqArZxbfbkGmQP-j9UaoJS8eC_zDq5FZZXwSox235f_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=OArBnCOSytZ4V_iuNwTiCrnr6mfaGzYj8eYr_gSf0_3v6xEcTIJOIbfuVqb4D_E5sRnjlimtIJnME8SRIp_8O2Hjn6jpFDqISxyYdYIB87MYSMnJ2EiVb3A0B45sKt0QWuLkmoL08IIEPDyzMkZaSIPkxUYKAnEsCUsNRkaLjNnpUCXH_sdxehb9eziRnnDjMl3M1M8FqeZak4W_92xSKy-qVjKfTp3RcGcGCcWqWEcpCf6UsBAUl-Vl28dL90rAk2bigEme6lpLvPEYgEzyfgpqLRSOUjl96B_o8ZtSadcG_sa0VyGJ3O48nUx57OCF9KhO6pl8wBJpfTYdhyK_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=OArBnCOSytZ4V_iuNwTiCrnr6mfaGzYj8eYr_gSf0_3v6xEcTIJOIbfuVqb4D_E5sRnjlimtIJnME8SRIp_8O2Hjn6jpFDqISxyYdYIB87MYSMnJ2EiVb3A0B45sKt0QWuLkmoL08IIEPDyzMkZaSIPkxUYKAnEsCUsNRkaLjNnpUCXH_sdxehb9eziRnnDjMl3M1M8FqeZak4W_92xSKy-qVjKfTp3RcGcGCcWqWEcpCf6UsBAUl-Vl28dL90rAk2bigEme6lpLvPEYgEzyfgpqLRSOUjl96B_o8ZtSadcG_sa0VyGJ3O48nUx57OCF9KhO6pl8wBJpfTYdhyK_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_DGQphEDR3KcVRv_dWRrEsgGYXtQ0EFuI9qRv8LdHltvcFY0ScqdYyJLTqHENvH2MsSutKebXRDihuyJ81BONFuocouv8QJAJFRi90H-BaoYcC1FeXiPtXMgLNlukuO_j9rwS4_dSHSTsIHuS5_Cz1RqngZ4v0BjtNq2WEfu846aLkpGA1kG3s9z8arMGdMXfXk1uKd-90I_Ui4sXANSCULOR6tYDUnzbqHHz9jCicZeJPMn6oFmknoeQFmD__-oEHSjnwzAG_WEz8EdCXHAxE5hCYeXFlcHRj49-998WJWVt6cH8jqzdlQQ6a7cS7smb3w_oq4MtCTvdfVlYWCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Ix54yCua8rFiz_Gyk439C7Fjlhe4DbNQAq8A6cg8m-aEItNtgOmAVVTlbGNJz7jwGzIWL1u31upUVOzydQgVTZG7Iu40Qh8y7ujCPzSxwLbXyUFmkAkAhgYXVSx6BoBQGu5GuRQFo5c138CaNONCnRohxzaxwwyOa6u5zC6qB7oipRF4x02jarR65E5Wf7OVRDV1Dblkv5mcyNqaPhPI4bR2D0ANAiP3nSPTmzKU684xcOu7mr0Q-KlOKB-cjMAErM6pxYy4j0PtT7lWLZ5t4dH-oMr7X2qgEh5AXSXTss2aK3fvOjpbggxldCy9mgbJbMixjpjO-hnMjYKK6Fu3BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Ix54yCua8rFiz_Gyk439C7Fjlhe4DbNQAq8A6cg8m-aEItNtgOmAVVTlbGNJz7jwGzIWL1u31upUVOzydQgVTZG7Iu40Qh8y7ujCPzSxwLbXyUFmkAkAhgYXVSx6BoBQGu5GuRQFo5c138CaNONCnRohxzaxwwyOa6u5zC6qB7oipRF4x02jarR65E5Wf7OVRDV1Dblkv5mcyNqaPhPI4bR2D0ANAiP3nSPTmzKU684xcOu7mr0Q-KlOKB-cjMAErM6pxYy4j0PtT7lWLZ5t4dH-oMr7X2qgEh5AXSXTss2aK3fvOjpbggxldCy9mgbJbMixjpjO-hnMjYKK6Fu3BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Zxe9ZzWrvwfatf8MOKzH9JO1UF1vO-Z57mnyGAPQca-U1I-QJsosprHwPn_okCEYHM3JHKgKSDbC8pam2ro4T6MYAFWDuTcMQccqc29hret7C5VZaYoIsY2pBdwGP9x0vZvHj_th9G5kyC_QG7sh0tpeWmn5s9KCZLw8D60e0uNGN98Meyzgdx2XCK9U8uMoGud8Lhz7Kif49CNjxMgoKjKX7HEKyTNoywu_8nkW5WEnxmDQXZq1Nz9Hbi2phn2Yi_M_kKpzk61mkWSVMOhUOtH1PfqSSvna1fAo9OPlXkM0Gusl0CC8jYeGycYDBjv8yC6mheawwaNnnzW7F9apig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Zxe9ZzWrvwfatf8MOKzH9JO1UF1vO-Z57mnyGAPQca-U1I-QJsosprHwPn_okCEYHM3JHKgKSDbC8pam2ro4T6MYAFWDuTcMQccqc29hret7C5VZaYoIsY2pBdwGP9x0vZvHj_th9G5kyC_QG7sh0tpeWmn5s9KCZLw8D60e0uNGN98Meyzgdx2XCK9U8uMoGud8Lhz7Kif49CNjxMgoKjKX7HEKyTNoywu_8nkW5WEnxmDQXZq1Nz9Hbi2phn2Yi_M_kKpzk61mkWSVMOhUOtH1PfqSSvna1fAo9OPlXkM0Gusl0CC8jYeGycYDBjv8yC6mheawwaNnnzW7F9apig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHr0ScT8Mu2rflSLTOpCR0kEhe3eeEI-Iuw8U0DcsPHMJwJzu07Gt9rDBxu0C6JFBfLJ0bc0LyLX1mV50JczoEHyQFroYSRtVlx-PB9Pqyn5Pnw5sCJnl9y5fA46vpjysWV-lFG4CaP9344DS3FCSaSNMlBUg4uMplMb8HAO0J3dZ3lBgzE8-wS7TcVTzaegCfmQQWrMKMUIcKnCogjWjYGvk4qnUTyUm6YyGFBV8Y_ubu6ZIzsbBuBQCRmeEMVR77jGltwaGD3pmgRp2DLluvtAKUNyMBM-AaABcdKH2um9PguiPdj-4pbXPjZg7jGU48iwmbS9ig9aNc7pYpEj2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3iXBpk353bXUnNCA6KON8TdYCi0dmWWKltGUV7dqGEDJNpAAVhP3VzY8O6VuBtZfqPU23QZn5zI8PiC58X49Wr6Cb1E_1lz4D2MxyekrTpPVTtQ8qWCo7PwayH5Z-ETfWaLZAq0lYs-2yG31nXadZXrrwZaQ_LEW0HTQ-JL1neQPmWtYuD6-q7HHnY1uMG5hfcho0v0WDU5ZO05vh_YVQV7QP27QDzRyqa8ZLkkf45XmO5xSugfkpGjk6uLEy0Roi74SH5629uMX3Ycoj0mMrCVVJorA3--aHwcrLYIrEDuPXG7YDxHJJrzLjs6fDG2HZMiFz0nCQl4Lzo5vnAFJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=rL_0TYwpLn5qXYbiBO-kqgoo94DngGqpy6BR1Be48z93HiG6ZBE7PF4ePj1RVguMNhOtSDhJd6zsLmdlJ83-ubSwEJXksQZJIygx6WgwK2NtOJd9sWfLi_xGHDYAaOmPuEPhYETyEr3nYQE-fxINygnFiQXwve5ZcqhvCh5KCtUpBdqEPEJZi78OBQ3g-J2L43hb6T6X0tdgB5WQxgLMLNbUHnXY0bJcdLfvVzJ7jKrDTmzbFWNuk4kDgSYqLQnZXeaL01CNcd6FG91_AYof7PU1e4Se63L3DxEKsN_MN76mPYPCGch6ozBkPkajKH-j0T4q8vzg2rPV7q9fK1TtmjvG9DwRh-5arq9ewOCZRImKaK8M_EU_Ow1kAyAc0_QBydQ3dHo-uzOkFLVjBtkL3eTvS-P2mCKXcmpPJQz0rPt3sjVstqxxfoE5yLBCiZMlbCqqaJwKGwJyqBBp4l3qeutIV8wTnTl19EQGFHnWIXboVhq_eNyaT36uOxENKM5WZaShj9d8Gqmc-LKcTgb8cczwuvwuI5oRJNPYa8OPlqtfDapRerUBhcKuliBVTOyzFt7CRaocFbIlf6nZcJRLA_sTtNtPA3PM8sxMqiTfb5IAvN2lburOXmqX2ruASe884iAaRZM-PDBkN1tAuyQ07q3ESDFQDDvsaejhSjyKooE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=rL_0TYwpLn5qXYbiBO-kqgoo94DngGqpy6BR1Be48z93HiG6ZBE7PF4ePj1RVguMNhOtSDhJd6zsLmdlJ83-ubSwEJXksQZJIygx6WgwK2NtOJd9sWfLi_xGHDYAaOmPuEPhYETyEr3nYQE-fxINygnFiQXwve5ZcqhvCh5KCtUpBdqEPEJZi78OBQ3g-J2L43hb6T6X0tdgB5WQxgLMLNbUHnXY0bJcdLfvVzJ7jKrDTmzbFWNuk4kDgSYqLQnZXeaL01CNcd6FG91_AYof7PU1e4Se63L3DxEKsN_MN76mPYPCGch6ozBkPkajKH-j0T4q8vzg2rPV7q9fK1TtmjvG9DwRh-5arq9ewOCZRImKaK8M_EU_Ow1kAyAc0_QBydQ3dHo-uzOkFLVjBtkL3eTvS-P2mCKXcmpPJQz0rPt3sjVstqxxfoE5yLBCiZMlbCqqaJwKGwJyqBBp4l3qeutIV8wTnTl19EQGFHnWIXboVhq_eNyaT36uOxENKM5WZaShj9d8Gqmc-LKcTgb8cczwuvwuI5oRJNPYa8OPlqtfDapRerUBhcKuliBVTOyzFt7CRaocFbIlf6nZcJRLA_sTtNtPA3PM8sxMqiTfb5IAvN2lburOXmqX2ruASe884iAaRZM-PDBkN1tAuyQ07q3ESDFQDDvsaejhSjyKooE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbPwK0KrD1tS6TToFDjqsImjQvQwMYeAxphgFYBbTXFj-fVS1qgNwaKqcPldog_Tl1pKiSmzojpSJ47cf04vHTYysWuM6Z_iolHPX6xpD2WFx7TDw183qaRZKYBQUfNylMmsUxeRG0H59CVO_wBjFlHUfocpBK_IoW3ijrwFu0kmNWwK3bT7fVvM0gARNk5uenLhDZE3PpK2EMLPdcQjZmmHFPGC1HA1-uyX8McbvXij0nRdhgVZR-nvM1WF7lj3SrTvMsZmZ7pM4_0I2L5DHfPwzUa6wZvooA8Cw_XEY2ApLT-MrKybqGQ5-zqdKAV171PgNsJqajM7J7Bp4rX20g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=JSXlDVRsaKRjsrmelN_uWC6Q7q5NlWoHocOJHIpeTSg45EdS9yuusATAfkZUN7Ve_i06uKFRu1liQ8MTc3bVVYWjDrBj66wYb8J4Dx3jJ0zUziLjHzicJXZq38M9DykWj_12fUgb-tn7boevqzlFzQnFPqdz7MAj3SB96ytMgtxDEI-YX1xNgvVaWygYyDCUDLG8MSrWPmB2nywmmGCiur2yZLpIrWZBJNC0eXGsVH9_wUMCN-60VcqjoMWYH2t8XVNvFeORjeXMoAFFLtoopnUjS2fyZti8vNl7RqzUWgR1-OKhXPenHiIZ1Bx3bGwVzJLjoH65iKYMsFkMFTqK7ITNg7_n6PsD-bfzVhmP5j3QhTaAWARgS7xRfQgKwKEXcRTITkaNGJ3ur4YP-Sw-KVutfaDwqPSjs8fRR6NQsv5nQhd24-7R8q9FMFxLk5uKDugK-VAzJiQ-7CZMp2jrBYUJzwk49-TP6NFKyPjuOyEnuMGryHqGxNd8zMlpuLKJ_s7XRRx1I2sKZ70cUNI-VdIXKmLk2_p7bexeiTTNlpz4VJtjvLC0b7LRkD7Y2YT6ozFKLO-_Q9kppCq744uZDfbjGHADhNTKEf38Rvi7QK8jtefeLWPHbJVLkwnsK8yxBxsEmTkGZ-uP_wgGpXU-rFkbCmC_02JNU-uwxmswFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=JSXlDVRsaKRjsrmelN_uWC6Q7q5NlWoHocOJHIpeTSg45EdS9yuusATAfkZUN7Ve_i06uKFRu1liQ8MTc3bVVYWjDrBj66wYb8J4Dx3jJ0zUziLjHzicJXZq38M9DykWj_12fUgb-tn7boevqzlFzQnFPqdz7MAj3SB96ytMgtxDEI-YX1xNgvVaWygYyDCUDLG8MSrWPmB2nywmmGCiur2yZLpIrWZBJNC0eXGsVH9_wUMCN-60VcqjoMWYH2t8XVNvFeORjeXMoAFFLtoopnUjS2fyZti8vNl7RqzUWgR1-OKhXPenHiIZ1Bx3bGwVzJLjoH65iKYMsFkMFTqK7ITNg7_n6PsD-bfzVhmP5j3QhTaAWARgS7xRfQgKwKEXcRTITkaNGJ3ur4YP-Sw-KVutfaDwqPSjs8fRR6NQsv5nQhd24-7R8q9FMFxLk5uKDugK-VAzJiQ-7CZMp2jrBYUJzwk49-TP6NFKyPjuOyEnuMGryHqGxNd8zMlpuLKJ_s7XRRx1I2sKZ70cUNI-VdIXKmLk2_p7bexeiTTNlpz4VJtjvLC0b7LRkD7Y2YT6ozFKLO-_Q9kppCq744uZDfbjGHADhNTKEf38Rvi7QK8jtefeLWPHbJVLkwnsK8yxBxsEmTkGZ-uP_wgGpXU-rFkbCmC_02JNU-uwxmswFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9gt1tCZrx87EtrAg1uzCj1rZ7c57vBo9Wl46bOG10DJrtKJRTFcIfsGYPJwi-4eIf94rPXn1GDwJVAA0eWVet8cGacLy-oiEKcqtLIgD1952ZRz1GN6y0thxDxx0GFl0TdlSrhr0S4zkErKihise1z-LzQbWXrxDYXvGWl65RPJITje85EAzmDKKNVRRpDlBwmf7zFzQnFsenWv6qXRDbKV8KsLW7eGQAp_fSkkOwjMt4dWztUOqI0p3zythrVg4xQGzblI2kDY20EfLkhpB4eSrEGoLhvRtZ8BHpcLMv6s_wVV2W7JHhsUvlT-OXnhfwrYDwoBfpTB43fKVu8BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqssrljCQp5NiQMBA9obc_FmDuVdOGYlxCawm3GJydfSW1_aRVPAnEcu-ktF2y4WHtIS0wpqP-_x2D0Y-0DoxwAdtdMGpuFa7LDiCQ1xdGX-ouKdlRc9YcdBEZZLR-flbausKXs9HjoIOIdnjdNuMh8JnfmtI_mNdbgZWJNam8ssuMwrjjw-gq2Am5cX1s10j6UoGQtXw0AIwPZz2gHSGVRhRBKUIQHvGj3lrlVW4jGFJy9P6CH0VqzaenZKOH3jxuu8z8R-YVdTAxR6-KZiboE8EQJ-HfTaPC4T5cbbDVpUlONFphETgAFdZZyNNcC9GEOl-RE2rkEogrEk8-09LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqUmdEjbjacy6CkkEKsMM2BXv1-FCMtZJ3qdlSmeCkwFeWSxXm5s-8ft5U3yWhks8vTlKvKRVH1zYUtiUYeTIoVR9JoYsAQAZnzfwY_t0ILO4BjOlxoLb_kDDLfG7bIP8fL063Mu3BKM6JEyO_-2D5WfLOKIXHNukUODxQCdguIdXoLymeyCmawahxymgmbk1cp2R9WY4gxqV6PhRhWRnc-eJcAJh1XCsudbJF2y54WjSPIHOf2waocJMzlYoPm1nANSKl_Skh4FjOM1jgvWlTY3CEsqLQbHw3Jt4gevGk2KGtnYzTMoKA2_hWcXRYs2fbk58XufgHevRSRBPQWHZg.jpg" alt="photo" loading="lazy"/></div>
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
