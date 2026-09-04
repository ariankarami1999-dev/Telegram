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
<img src="https://cdn5.telesco.pe/file/o3U_RGU4cBMrjTx_VOKfs3bxtOVel8LeXrM1e7Yu3-x6Bgxjd84Fe-vPWfoqjD2p-HP2ylGY0XLePBVnc6htGsD2Cp26QHgOf5VqC17MIVF2LSRu3eqi4AOlFJow5du3lf2tTxCqZqdeNv9Pk8lCLn4X-kxZK5Sv1JRwXVcC9nbcE1algj1tnXwvmBS2dxt4h6Css1haMhopy-6p66Ioc5X8kDj9EECIB_5gDDGaY4H77xSPRwDgt3VXOoE7-SNWWhsvIO1tFcyeLAKmZKC2TwwbDTJcx055uUcBP7evxw8a01tIeHJEy_8ySLXuccahGREk1WS05Jn171NgXQ7BjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 428K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-105500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=hIWBsE4F1HG74LaJR3fZYq1_HAzABtbbr-PbjxXnfptKaDELOwPlVVjofuTNRkA4XiSkhTkm3VjsCaZzdaXIB6VQ4dQ2MtneYM6J1FzqF-I2oOsXG2W9MXrM7gnYgW4W9I6zLE_jB5CkxBKsLB4kpA4bNYkk7LMfJXzT6lxTIRvqX3Bon1UK2wR1vBhXkqWGdSOYKwCnwpJ4UkqVySHauLn43J_glRyAt3lDODu5DZgOp8e0FjWrLkBjXx4lVzrepsUUGV3lXaf5T6F4fCkWEHacc_XqauEmhXqBSzKVxa6xYwKB-xAE3pqVz_MnRqEjLJIgViIW6OS2yQf-e_S7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
بیژن طاهری سرپرست استقلال: بعد از 23 شهریور که بازی آسیایی را برگزار کردیم اگر سرمربی ما صلاح بداند بازیکنانمان را به تیم امید می دهیم/ در اردوی قبل پرسپولیس به تیم امید بازیکن نداد اما محرومش نکردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/105500" target="_blank">📅 16:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇷
❌
صالح‌حردانی بدلیل انجام برخی کارهای بی‌انضباطی خصوصا در بازی دربی، از سوی سهراب بختیاری‌زاده تا اطلاع ثانوی از حضور در تمرینات منع شده و احتمالا بازی روز یکشنبه مقابل آلومینیوم اراک غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/105499" target="_blank">📅 16:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD5hztz3TZ16twDQjj86PTmC_5SQszjO_g2eiKT338ws6RiWXWiBN1Qj-JNgKuDnni-wM9XgiM0sfzSb5HNwq3rPvP8OmpWvlVS2K95gV3KtKpxGQF_MoaQFJYIjnS-btrf4TADSGRr_ydy2m7AE5-lo6GTKhixr4ULrOOTdKUEroxYdlbN07YlCIKY_-VoAUTYopFlfZnI0qLXxFiX9hoyVU7rph31gEWfTZRWQuZO7btELp0IngCldTE9iNeSgj9TRpfN23vPkLuQlqlheVQzjqtic1w1-f_dk-Fgp-1ZKxCkygsVJJDWy572PFtPKy1T5ntw9HTBYifR_18mnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/105498" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhmV58yeRkUA8WAVEJXmG89Sg_kfyMpf86PFRvlMfA5AucMTnwSqr14321_aOmSduT8i9WXBO05SAhFN8k1rxCYhr7gM9y4VISeohIsXlzbkZNyP6QUzlU8gpa7t0fltpXYb4NQs2WbD-VI96U7LKuIyS8nFCzz8QPjuhNhB1_HBoLB7z_Say0hIwvBjBaGpdb7lutgugqMnQl02gQnw7Qu1FVqnqnbA826uXnQ9DpyQ1pIb2pmwT_1qDV-imjUSsXXs-COUx4-KKyoxLZthi1rYCzuI18tQjqnhbXOcRIckaEXtYhXjjFcQ9__NaZgvIHGZjtD96p2aPKKU0bwGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
ترکیب منتخب بازیکنان بدون‌تیم؛ چقدر ستاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/105497" target="_blank">📅 16:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👀
⁉️
🏆
توپ‌طلا رو باید بدن کوارتسخلیا یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/105496" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=lwVUfxLLHdiTQGmuDTRxSnuy9ELwTNkoyVIEGhm2F3R_3FGuRR8T7im4PXZqCrIDJJKrqhLlvG-fzmzbC52R6xH2PbB3T9mFV-pyhVlt0wTlh34CtX416ZUKGWPdxVYtV0PN0LVS8rbJkTXjtMVndqirVDVcqaPHTLDvDbJ8NzmG1yWXeQFi0YoJ6aG-yusUEVAFR_e6VT6c1t6vVXXsIU-X6zzOnyOKfVpfwqs5s8uaTz_CuVC2agEvutA5gWyri9sCduA5sDdiHJ5-EgP7qtWKNUg0dyOCVi0zwEaqDa3_MZ7EE5FujHOFF-HjGMp51aWPhnke3tgUgG-SmJOw-lbF7tva3531cXEidCSWqTYgYdujN5uWGyJdhpj93GdrKxjFX-luItKaOizopj6WSUl2excZMK_UuspN4MFyWcKrNj0Kxl8Zo6hhMbCiMTu2KWKSGmVFtvKFhZGjvZ98H0A7N7NUDAOGdfqOTLY4_X4NSgT-FBL_QJcqzdlqOYCG9riwy0RBpS8BbPAIkkPO3gAV5NixOV1Da7o3SnFDsXG4gahRxQ52YTCqSVjd4xHjclNb5C2FDKEzcMyx0eFSGDzk84iMD09jdlOxZiydNINM0_SgkMdKOYJiKTum61_YHhzIGBy5fKvlTpDqvAJAsywsM7pgLh7sLHz9g1yTCjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👍
همسر رشید مظاهری: شوهرم قبل از انتشار آن استوری خود برای من فرستاد و گفت که اگر حتی روزی به اعدام و زندان محکوم شوم، فدای یک تار موی ملت چون همین افراد من را معروف کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105495" target="_blank">📅 15:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=exoaFXDRE83Mot7SNHOlWoyaQi54gXwVDrVPL4NcAx51fAegfrz7WXLJVyX5e6EqjjpsNrPfiBHwgVJ77JLG_zr5Zh_E6NQwwBmuT0scIk08YTRYsuyWHZmL2NZ8jK7i0SL-iL-_CyYxCNT7vfOfcbXtCJuOK4b7gG1qqPKvZvbl-qP_PZL-qbq_ibcf6JL4Mfk0sEjYoXsg-rMZNWMAPJxxioAbpRHBI1Hv6Wvh5HzfDQYK6vs0kihHS1itPyzsqovBSPtKGjuJn1Gc5rvfVIKHbp7Y-A0nnMbeaySYb3k3uF44Of9TFajlPZtiLvyb1VGuEl5Ec4A0muk9uN7LVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
از یک دربی تا دربی بعدی...
💵
دلار: +۱۰۰,۰۰۰ تومان افزایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105494" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=U8zDWh8onfSbaxWpV0kJz6sS1WDfmMDa8HhsfUCLGtFpUwb4WY-7mCARcd5iWaW1iOH-q7zVfz9nt_GUqA287d3tzcII6yWKFe_S4vrjoYF2wA3FBOoomWSMYKl9ntC760m76uQgbt69mSeOZiPtK5n-dTBxzL6qC8loikcrqFLXL5rSzDXbijrGWxtqa6S4BCGDSImmEE1QDve0Q2VD4SL6kQN1eb0WNcRWGQ2sE52cNR0GhCJAyxkJMlwyqhc8oBHurnfWZbGkc6POczrhs4ry2MP4QAUqaebEt4ZI3bJhKdiDaimmTGoEvtuhh5ROWWfK0tgq8X5t9SfQJI-4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال به هیچ‌جای زندگیت نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105493" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=XFZHPGyEzPvkbeTnUousnuPI_1VOOIibBJX-ANw-ke004qfDVlWDo7pzq6zzUZLNBHKK5Ee3rz-s3MMwb-kKtQ1neWSBcu1Lmejs5n5LG6bnywSqmp16zuwVs-KtvZ385QVJpD_7ocYuEZQYyKGX6Rb-hzUU7O1WYy9Q6o-jlORcDIRHd3gCvm3TaujiXGVOhIGtS_ZGpEnA9rcOzmRMMkuFXM6lr9kO78w9HDxpFAx15qb6uBithgGZV1cxqs7kS9wmb0lYbmLLMCWpro9Ro30We7fH8DbaatUdnRUNRQUIYedpPFGfVL2YcwTRuzbmSFf3D_-tY5EPU-odJD5E0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وارث شماره ۱۰ آرژانتین که‌ خواهد بود؟
🇦🇷
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105492" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878e055f11.mp4?token=L6hjQyl77778a_i-m_2DE5XhsdPVvvopsSc5S3T1N4y1JJpbS6sxiU2hKNh0_hjWXftiUiFLSxu9oEs76dwp8GBVrxwdelT6jfbkqNEWc_kwqbiQLc0Ov6PHVT8GM_k3-BjQLvwuNxyBJbdWg0gKvlxSGK-cl1KHFPkaMZbnsJqwibknIgsn8vPeXsosOpky-MB5tJpUDU-f-ZpX7XcjYX9VPRaw8pLAzjQVvk4LsTlBji6tj1m8wFXpOKv61wd5iz2E7zaK7e7aNntW-68Js5CGPcX9EeSt4R2q8YIlQwzzZYXatM7NX_ASNW5axApQzKZ_Jxl5_kISHSekujsKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
برند Dyson یه مسواک ۵۰۰ دلاری ساخته که دوربین داره! با AI بین دندونا رو می‌بینه و خودش دقیقاً همون‌جا دهان‌شویه می‌پاشه، و تصویر زنده داخل دهنتونم روی گوشی نشون می‌ده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105491" target="_blank">📅 14:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز جذاب و دیدنی از پلن‌های مختلف استقلال و پرسپولیس در دربی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105490" target="_blank">📅 13:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105489" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105489" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtV6-fze1BceOfLA2o1-HF1dRSKuB_B5ew6L6rYXUXReyAuXrFbAjc8mPfwLOcVtS9blp6BuZH-h8dsso37jC0Mukz5MsedAnmYFS7gZFkaGuE2fvfWubt9482D__56482srjk-4nsNNjj3HE_plGQCLXj8nVwYn_T0bc79iavfG-R2eaAtmytuxdy2OZOXgRz44V352eKG1i9BXKeZ96awhV90RXZBRdhL8t92IyOOEJLINMrPlEY8ozNiDS-sx-DP5ypE6vDjRmz7o2ErKXKpW5Gq4UG3ccXXXMbnO5NBWV1186cmKqr5X1u4URUWKkzW2th4pqL5H5Mkgoxt1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105488" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=jiGl1YyuY_acXfiXeSE1AT1QP11Y70HA0hEM5JYKsvY-ZHSsL3Y1wbLlNIbWbQzNIH0TkUeLBt2b_i_yB2kmwcYFnR_bn0gp4p4dpJvSVhQCk0PyjlTwSlCtlgdS3ZPgRMBC5CEiCH1TaOW6ppbEZl_um5KA1hKB9rhsWtrqCE4C0dYnQA08siE90efY2TlcF7eH9rMkWFQhEY4Y8sYEOAV4bZDNOsKZKzMNWnBRXWNlc0MFzkSueRt_nhFqjJ0zBF__Hc_yayJUvcX6TdTvH09bxjWTOmQqswdQdkWykoVxNUUb4_a6TD05tNKvlnRiQv5tA8uGlYTGIJTBSEljFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
اسطوره معین دیشب به یاد بانو هایده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105487" target="_blank">📅 13:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtH-vggpyCgItwp7tu0JlR3yV2UPviLuU01BK3XvVDcEL_ig6veQgS1i5Fl3Qas3rpK4fuXpuYgxBxjaqavrqqEp_5KQ8W1DrqZKMd9dBwQokpfbosdFuPgNTxSzyJ9HdLPIG3IGJ_0rHOHSyy4Ch2bl_cCZvPJS-xtsBhYK6dicEyHvMxEyJ7CgHZubiLefjk-CqTugnOi5Lbn-lloDiOmiXPaKH44pROIFVm0dPA-CIytDXbYjAv0HVjbw2VL5Mm5Q3b2yj9VRvc33WVQ-MgWcG8MxuT5-Y4PhPaXN1ZLXz1_-01kw_9PqkaB19f_BVLoFqPJZQHQjSCGk275bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درصد برد ژابی‌آلونسو در تیم‌های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105486" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105485" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfZv_2lVVSZvCjb8hiRMduQGRafq0KEwbqYKXZLlGyE132F0JlSp5LGVXxQMF76ZKgOWdIss9k4uZWQq5UPJ8IHJpOwNBjvz-ov_Zw8ZjMwQ7jjsNwnsoDx4xMJr98cU_z2DaCEAIPkTinZfco5E-x3HAKsa8ZXGC_lcwK0_KOtlfxvHI2bsXn6rrP-cJC_WvySVpOu1wsCq1nqGYhdbr7e6qvqPFCVCeCqO9mpNUIyTQR8lK32B45klAXd_axK6C6wueC-gvXLNTxPDhcGws5Y0QoDMDAuLrnWNwr6AniQM2JagnJNkYXzgz4qC0boj6s6APLECiBWaXDiyKRRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
نگاهی‌بهترین‌گلزنان فعال در دنیای‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105484" target="_blank">📅 11:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👍
▶️
اجرای ترانه حماسی ‌"ای‌ایران" توسط اسطوره معین در کنسرت چند هزار نفری خودش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105483" target="_blank">📅 11:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEepEj0gkV0AmsDNW47diCY1H-MRNi4byn4JV3Sf2WTTV0AASzZ6DCZ6NI4UNY9WNv1jY4VZ9YEkcKsqZzF1fwRZJrARHooxpPslgi8fkl43brqMmufxd2JdVrRAahPf6Ebck8384vD3g7l7JRdbOE07O0yUDL7LVDZfqcHfZt4Tqqbwcu3F0srB-QEl156J44AaaszP1lkX7NUdkAL7BAzxea1lWQrlp9ORF58kVmyHJcFxwQcNvcWlI6m_fgWFkWJEC9mOXXkiJk849tS0UiXZaXFD3uqM9HkQP5qyxNSaL-O_JDv1al5YxdtBgLNEF_ZBWQoHPepaUCSFT6w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو دربارهٔ بازنشستگی لیونل مسی از تیم ملی:
صحبت کردن دربارهٔ مسی مسئلهٔ پیچیده‌ایه. چیز زیادی برای گفتن نیست. هیچ کلمه‌ای نمی‌تونه کیفیت او رو به‌ عنوان بازیکن توصیف کنه. او با ۳۸ یا ۳۹ سال وارد این جام جهانی شد و دقیقا همون‌طور بود که همه دیدیم.
او یکی از اون بازیکن‌هاییه که دلتنگ‌شون خواهی شد. مجبور خواهیم شد برای لذت بردن از این سال‌های آخرش بعضی بازی‌های MLS رو تماشا کنیم کاری که شخصاً زیاد خوشم نمیاد ازش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105482" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2EY2N2Ez4hPsTjCaBJnWtxvUSLZzgGkOTiepUfi9QBBOHo-NPCc_7X40pj9JdsJVUeqpOUWFvqGU5-drGlX05yFGa0DglkpaV9Zgysh2bTo27lFrSJSXohnBrPRl2fWdYWcSIq30duIWwSpLpNnQIQ3ZyJflvmGQKwwpjAVopEKGc51TPQXXgoox4geyRBmkEevU_NqFV5pUiQKhki_mZQZ3MIgXrHiaHihAtddIy9rgUSBPZ4RoYl-kBucsi2Uz7jBxf-cVKcKBAwTHKuOzxR1wCIN7kpLSwZfhBcBzqnkqcgfOC3t8p57PDsFOG76WgqYFtQNECeROGGouHSqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htpm7fWm7mKF0Kanh01Q08VId8HnGbeWmi6SvMQmikKTpHv8JpdB0v-ALksC3WP7W4rBn7ik0H4W2K02ZDG_4_ip2dkn2iLbuz1e95pKnpcjL9A0p8NI6HMyirAfIiVTZNkwzg0wdcpXjxKF3DrALyFkIyLRcYsFjhSJE8fsJ3K5mu-9LsIjxiE1XtPosWYVQPivsTcTSOfmWBUzJC4ZN1SY9UpHN4GqsoVBfso8QB8ZizlGsQmJsmukRkgfkf35Chc8YuB4fu7kcubxNv6cvptSJKITr5JPiI8Jf1PGjpX-U4LvLmvDfXbd9ut0jmSdANvoYUbWiexHpJXXebJGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCXf0n2anAqLxVFE2ldlSPytaBw5H_IJuzJ0cyJPUdKe7N5BmuN7KDWrVFfBtow2yQrmhuDViNECnlklhyBfEvrbyaSEPidQQ2mSouGccPjtpU5OLUjqDoFxlj157hgaEIyRTw28k5Uxj6vn3CdOymCQzy1-Z9QKSmDzyNB47q5qeSerGClmz-o6TPASCN5DnjvfSFchuM4ZB9d0jReCOvTO1oX4IMtOqAZNbOxEwM7xf51BJJSUljoceLB2He1E_EvEAKqC0DKZeOy9b1eZZJjkhGLlLTnkuxQJpK02Yt8JJnbTa1N1Gu8UAbrtrqSQ6yHRUjxbKryt91OQrtIcdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس جذاب در حاشیه دربی
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105479" target="_blank">📅 10:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👍
💥
عایشه‌گل دیشب رفته کنسرت معین و از لذت بی‌نهایت صدای اسطوره ایران بهره‌مند شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105478" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خولیان آلوارز در اتلتیکومادرید موندنی شد.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105477" target="_blank">📅 09:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
یادآوری تلخ‌ترین خاطره مشترک وریا و سیدجلال؛ خط خوردن از تیم ملی برای جام جهانی ۲۰۱۸؛ از خداحافظی زورکی کیروش برای سیدجلال تا غافلگیری وریا از خط خوردنش از تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105476" target="_blank">📅 09:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105474">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtG2f-G0nqFT2Q9AAbws032oSTd3-VAqaUxQ0ET1cF809zpRB0IQg0Nk9Surg_h0ZdPZf0cnAeYgDtPKv85MEHMW4fGD5HkGeBb2HcrBENs-v-yWxxYEc1VK2-d8rp8zuFdKPnbdRorzxtxORtA8MJVIT6zUNtJ_HX5yo_p8Yct48OaQKXFxtxEiQJLZYZVaowl-CQUHE7XbnT0jPNcpqCkwJrzIuLC5it0C6i9pE54PtFeHne_whGgva5BW9keuV9U5w4L9ydL8RYI3lQUMRtiFmfke9ONLkXD2DNVVDN659g1yykLj-39UZ1OHWLm15Q0Dxgq8h0mKDrplkCo-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وریا غفوری عزیز و همسرش
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105474" target="_blank">📅 09:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105473">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
⚠️
اوج قدرت صداوسیما مردمی در تمسخر و تحقیر رئیس جمهور بزرگترین کشور دنیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105473" target="_blank">📅 08:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105472">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105472" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105472" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105471">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQsK48TWshORhKCWUX8yZB5RQUPxOvLF0kNIyjXLIoMhNtY2ZBQRXPB2pKm9sblZVhnLNbH_L_hcMttgGcKxqCjeiVeC5kxkPvfrnBXbOErc8tEUJ_GHuus5rsyaP_7GDc0FLhNKcRFfh674bsrrM8pEalJe2rvXdOmVsku_4pWHMbIpsSqn1cpWh8ScPaTRUhpL6T558P12ZLKPht4nPUccBokfefwOLpFpjqJqDJ8vmNsZJqrsiG_4M9KDHRc8QZyTX08Qnznzj5sF9Y51VDU1m39kIVdXWXEdq72GUiaCA9yMmdlM2cYWNLc5tqIEcbjYWKotoz0Ir49GXMkDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105471" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105470" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=Bs0tcA4u6vClyM33-eYIjb1acncUZ6yopEAniurEF38OXIqDvYfCTjn_q6gJL-3wp6fMEE_0al88x3zpwHoUmHgucRNcC7o6zriLiC--TA_X829DP5BPpPd5t3vPmx7EQOA29fTnN0W-WAD9kzqTcCOXrMI3iBdibpqy_fZgmv78nZ6eRmyDaUhg1-lFKHqMTDDtNNYC7kfObrCB3G2mkZuDKn1sGH0Lh0DMwkQBHDNQnHRQPSRtXHKvSQUTXG5VMNaCqzJb01OR-ak95JgnTFyqzlCJ-Rkua0grc-FVeJqBo3fux57fGGNEnOcdSukRvdLEeupjR4zRo6iMbFCpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
واکنش‌ها به صحنه جنجالی دربی:
🇮🇷
بیژن‌طاهری سرپرست استقلال: کنعانی قشنگ انگشت خودشو فرو کرده و کشیده!
❌
میثاقی: بنظرم باید طول درمان بگیره!
🇮🇷
محسن‌خلیلی: صحنه خیلی قشنگیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105469" target="_blank">📅 01:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105468" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=hedfKV9w5p8sDGxhWl5qVBusM7s3BqEoB886j58NbERW84PwGPZewSOmVF7Anwp3XbwbD0tpjkY8zL1A3vPc1vuoH0-VEogrP2nkuoEAgLeXPlOEeZ2dy6DLjp2Vz9LlHQmBbkbJWORsu4sTmT5IqIuo2WX2GCaRlvE-m8HBCEcd0BAm6bfnYQxIOYiQa5afpuBgUr1Ii8HNqEO4F9c0n3tVfXfMMaW4GPADVjQa_9Yki5anLHu3JBoIImfgIijSjx4BLOFL4h2pLjSdo3x67wsXHFApPVLTwUVljmwRkVUBqEfglfRJyN8wDam6EQIu0UFZT8CuTM-e2hY1VbjCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=hedfKV9w5p8sDGxhWl5qVBusM7s3BqEoB886j58NbERW84PwGPZewSOmVF7Anwp3XbwbD0tpjkY8zL1A3vPc1vuoH0-VEogrP2nkuoEAgLeXPlOEeZ2dy6DLjp2Vz9LlHQmBbkbJWORsu4sTmT5IqIuo2WX2GCaRlvE-m8HBCEcd0BAm6bfnYQxIOYiQa5afpuBgUr1Ii8HNqEO4F9c0n3tVfXfMMaW4GPADVjQa_9Yki5anLHu3JBoIImfgIijSjx4BLOFL4h2pLjSdo3x67wsXHFApPVLTwUVljmwRkVUBqEfglfRJyN8wDam6EQIu0UFZT8CuTM-e2hY1VbjCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
📹
🇮🇷
🇮🇷
🟨
نظر اتاق VAR در دیدار دربی درباره صحنه درگیری کنعانی زادگان و آقاسی نظرش بر کارت زرد بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105467" target="_blank">📅 00:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=e1iekfPaOz8oMIDv1xWuJUtcPw6IeUBGPgiKAJ5Glb4_idUlrgAx_qTXc8tS2xtAbKZHrFFkgkF8i3OmlU6tnn4pjFZ0j11P56EUxI3n1T9PUjz4gOKWGEH3JLdMidTua85k2yFSQRhQHt2Cwh0Vc7VGDaXoNRIPtYPxs41GvE0QJlU_I6H824J3x77FGN8WPUEjaFEQRjeVIykxk_paVdO---xXX5zgoiv6tfUG44IE03cCCPRQhvmbzNz8M8dHz1vKmV1Fu5sd0C-xtbS7FgxZ2IeBaFAGtDt3Uch0tD67QVJ7_-eFPQuOoXKfiXSb-67wT-dIi06ltpGQeoDdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=e1iekfPaOz8oMIDv1xWuJUtcPw6IeUBGPgiKAJ5Glb4_idUlrgAx_qTXc8tS2xtAbKZHrFFkgkF8i3OmlU6tnn4pjFZ0j11P56EUxI3n1T9PUjz4gOKWGEH3JLdMidTua85k2yFSQRhQHt2Cwh0Vc7VGDaXoNRIPtYPxs41GvE0QJlU_I6H824J3x77FGN8WPUEjaFEQRjeVIykxk_paVdO---xXX5zgoiv6tfUG44IE03cCCPRQhvmbzNz8M8dHz1vKmV1Fu5sd0C-xtbS7FgxZ2IeBaFAGtDt3Uch0tD67QVJ7_-eFPQuOoXKfiXSb-67wT-dIi06ltpGQeoDdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
بیژن طاهری سرپرست استقلال: آدان دیگر به استقلال بر نمی گردد باشگاه هم پولش را می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105466" target="_blank">📅 00:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105465">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105465" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105464">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105464" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105463">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105463" target="_blank">📅 23:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105462">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇶🇦
رسمی؛ السیو رومانیولی از لاتزیو به السد قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105462" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105461">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=h6T0-SIJ7dLuO5bD9UCHOwwDRf49zQF54OUS7lLR7fT5v03b3JeKCBz9yqIhtvpNRTb2OqkhpOHt246CvYxB9p8uoAG9j41tFfk41kMXMaCQxGorcH7f2xVOvm1FwnYVVxse2ra1eDa3O4WdyATpm1_Cqo4x35HB_6blOyuff0mn5F93p7dpfSxUmsZqmxf_7lR1480KxJogwiqUuaNhCn82CWbJUgHsVrkjqg1JUuUBwxUfcvwJ74BY4mMAV7iQH6TgHdJs3Gz7bOtefq1Ws411CxGwkwxD3T5Qv36mhzrkSkAzopLK91ZfkEznZGbzdkYsUD2LUegCqcd8mqLE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
گابریل‌ژسوس بعد از حضور در تمرینات فلیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105461" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105460">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a60jM7wnTsgJa1miVNREvhm6LArC1yK5scqyzww5e1yGe3Uwsvs8nNA6dcD6UGkaAYuqSTebMLz7BdwwUm5AvD1YmxgeEsyz4xBGQESNdmmSduxGlIaalOg9nsTCzkZ3JYuPked68ox9QFFkEiXD_sb8jH95sCKYEfRNrCCLRBadDWPn_5y1-XuRn16VygVvy8npoE6Xof33O0BkaNrd2dsASfi6keu1XRCg28dlA-xF7K2CirAGsE_1ETT3e-PZMCYP_jIvfohjTdINewayEbWumIVBMlBW_RYYXazjjIumCRJU_tB7LZ7nnN19TQXoPWZ9s1c2m8eywLDY8PkYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105460" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بابک‌زنجانی از دزدان قهار مملکت: پیشنهاد ۲۰۰۰ میلیاردی خرید سایپا رو دادم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105459" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn4Op6ziUyAaZQ65ELMC9Ml904ZlxFRs1MULZ2_SqaMOg1jSoDqNqki3Dr5aPpUH6iW_ywBknSldh8G5zSXA4XFUUBob1WiQJEa4KrXi37k0Q6ae2UA9TyPr9QMAA_7VEjaXeeQqUuBp4GA9rjA8h95reoniO8Hyp6DDIPlPHPqqU-UUfvKCKPPX9Rga5FUXNQAlbXOMmmXsMxi8kcDaaq_EgI1_azLVpIU5_JuNrhkEF__UkRayPxtnlpeU4fzb-wJeYdkawEQXAxzwn049QnhAxESPt3IuaMr_BtFi3KMITQzgWDivNZcqafxc5lhum49q2JF6zStiD9wFMrquaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
💸
درآمد باشگاه بارسلونا برای اولین بار در تاریخ، از یک میلیارد یورو فراتر رفت.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105458" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=sjLGKtZzhjyRYj4CYfGcBmebOZ9zhXKBT8vQKZ5EWvbJyNXIVzoDIV9mI2ovPLsueVzsqeUMIl1FrADVtlatcwkI7yW-wP_Gm97DTYLSBdnbMrOLAJSllh-3kHgHrK6qSFX1IuhubCcmViGaw-F3eUGfenfizZSKlfvQQ9RIPBB5SkEJ7qQSyPo95tbSApfHnIIE1QTdjfxwcMmCYYG8ZmaroibTm4j1Z29oihisHuOB5nfRA3JH5i83SH5PMfd68BWob9gHn1yYY4BBVyK3hukr9mIq-pG48PhbmfME6N-aHjWqHmxt_Hi-NzzL_y6IGTXjezAXaqMqie5wXqpeiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
چنتا سوپرگل زده شده روی کار‌تیمی تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105457" target="_blank">📅 21:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
⚠️
دعوای خیابونی تو شیراز که یه دختر به ماشین پسرا زده بعد میخواسته در بره و ادامه داستان...
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105456" target="_blank">📅 20:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
یه‌گل‌بخودی جدید در پریمیرلیگ ایران در بازی فجر سپاسی و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105455" target="_blank">📅 20:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLD1AFPocMiTsXZFr0A5sJsPI5OVCHrS-bfIFyX1aRIzZW75tfGmQLAc4DolgbEEdq7lyd9FsUov1PjEZEI9kR2PNVUszegWimLgVWOaxdb7bZ7dWzr-0_LcHP2ebeE_zX7_U46VTvXDro5lQ1VJwy0vvIKY_esFQNtE6xUfPB0dCQO8QNeJ_h5eUJ8ZOXK56DmGNNIPDq3crfH7IzWeQOZkWTBnr1R0o3-8LrQJoPxbBcVw0a8h_AFELovtK5CCDYZaG_ynVNT2M3nLiZ3FfMWBMe6SqNG83H-eUyBCI2n3-IgMJhYidfoaGxAKw46Urxkia_8SewwKYIw3-Hmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مارکوس یورنته پس از قهرمانی با اسپانیا در جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105454" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If-u76tK8Sltp9KalDMto5Y-2ZN9444oazbR-KThkj2EzGR9EnpYLmhaJKSsir5SrdI2oF-aYlUP8q4F5wJz2mMRr4l2UC2rw_iToAAA1GL-QNrmSmgI5oOiVNrPBRXIhqG65NOdAY080zzgHFv249zFORRu77VbLTLa1FpSA1NoS96YFKnYFBPwgOtVAqZNgswdEh5xEJ0F1RevZMD3daofrRHONaoEOM2J57VV0yuglMNLbgWYrlnp89fbxKGiYABc4Nu5B0h9fYP2mwzSMlxpICBTxXoREW4SeJQ2x_aqLH58TFWyMIo1bIZ68E2sbqDNbmhlViyyt3TMl2aD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ گابریل مارتینلی وینگر برزیلی آرسنال با قراردادی 4 ساله به الهلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105453" target="_blank">📅 20:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCJwUjNA0oGeYmCOMIg9K84fnLMESNcnsiag8UMhFSIBF-IL6YiYrKFVxqMPSCON-akc7KeujSixsRQc1XkJxU2cg4nv7ULaGIeSiRtEvtcDxQy4J29napbqlyq5wE3euZ7ZZWUYl3rX7KEomeHcJJP8QnLZg5LNQb1t709ZWQicPFw9gW14N4TPsQ7m9JPjiuO47Dg90iDH8pGQmmGOPVZosDr2uImWCKP8_Lb2IeIfK3zNA40CE8uqDu6MDygtadq5aE9u0UKEOhmFX7fVjhU2Aa4T1_fW7fR0q0o87i5cylQJ6Av9QHlCjzjpDXNIABtAUQF8xokR-Kd_RRAsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✍️
کوین یامگا، ستاره سابق استقلال و نساجی با جدایی از تیم الفاسی مراکش به کونگ آن هو چی مین ویتنام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105452" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8qvLQLkrHU9qeAk0CE1RGeyoHyGzC8rfjesAjvSalW8wqYMCk5D8tQkCjBUTk922jRVJ5AVwxKEQ_s0ZXOWeUbeyDM6uaPMFKOsWtXRi7HrxNrJhAPQlDsMy8zW6GQPSyvQ0GTTE8t95qHq9vTabRnrlYJi3JznVcuR6fRkDX4jZL9qggzrR0FKRIiN4XC0SP8MkZy2_jxlXZB-jZrSaDz2ridP0xCFDmwniXqEvYEDNEDlA_SBX2ILopdevcVc4iTri9RwSM0f-d4fSp4SkucJxNB0dYOOMESpsB1s29a0cNONC8l6v7s6zRmUDzugT6CBVKXQTzyKfZs0BRlIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
گرانترین نقل‌وانتقالات تاریخ فوتبال
🇫🇷
نیمار از بارسا به پاریس—  222 میلیون یورو
🇫🇷
امباپه از موناکو به پاریس — 180 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو از چلسی به سیتی— 145 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک از نیوکاسل به لیورپول - 145 میلیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105451" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZAfxso1Hr74Zl3M8CsCBPyMSKfg2OfuABDBYztQUpcn-pmPUXIZWE24xer5I8djoaLzCgCsiShYgeUgGyJ-e-gcgzFr03eZuj8KMtJ5BEn5nNlAwZswsuB3xrS0XVFebKLC3MjDRPjpsq0Y8xPumMASVqr9H1IS62A4b0Fy-1cJJdSwuadR61vazXoLUcbv7hcZpUPpgA-5GS3lFtchv9caDtb1WbpSDdmQoyzmJ5aT-q1poz0J8C5CL0STZq0gaxlpnTGyjPYfKsomZ8wKs1WwMv-tL_Kwi9CKfDxPUAyWBatGFdFZXdgJeYhRqhR-6PBUJERWaqh5VWm6ZWk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی می‌تونست تو این صحنه گل برتری استقلال رو بزنه ولی یهو از نوسان قیمت دلار سردرد گرفت.
📱
«ℳ𝒪ℋ𝒢»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105450" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egHEsKxRZh6ek3hzTP3Wyr5JZRita-bWmrdIuCEGhxyASFmI7-KWkWbfhXO9WAvTigYYsxMP7rOLg4G-8_v5PtvMqWIEKRNmjFc5iG3rLKV-vVjL-0IuOsL9RFkbY3TqBNZsnGGxsTov-U4pjBAMX_zy_H62Xufsd47DlltFcisTy-DqlsopURP7GjFX9baUlKxsVwBGbKswLRq_smXRpw6U884c6PyKo_jerfVps-YkwrD1Q-cYPH9jgfmWs50M6Qi5j1xtwQUXhjCxlOT9hXiBtghblqOTO0MprGHH4NlEbARjV4mudaqpDFEJ_LRrL0VZS7ZPQQByWQJR5y4fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد خط‌حمله بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105449" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9XDmwWWvO-euKoA-pyVXsxrc9WWFD3cLmfLcxaSZzHzMU6h8uYVT8nRhctwpPiFbdFX_Bwolnc5gXZ56N5_ow3mM0Iog9Vi6HJixRsDXPyLJG5LPQwlkLplWhhk36r3vmKO4NHiiUpZZ7E524XsvJEH4snHG5vaC66e7pbKf316RKlaPIox6ug3zlBkhgXlKNQV9Gh7AQybkOED0NSKaRjejcfW4ELWuTjQhi3UESXAToS4esdTl48mE01RXJ_h7LeCNvWV0D_LXv8p6Mi6jGdOIE8sQ1BDnrpIcBhghQ_sSqHNbsE4tDhrJspy_dIDQup5zXN4kTB0QZ62Zy60VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
آسنسیو مدافع رئال‌مادرید از اتهام پخش کردن تصاویر لختی یک دختر ۱۹ ساله اسپانیا تبرئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105448" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r49RZuwrCKGGquZQLBV2RCwBWcDxjDnomGXP9FpnjPiYNKnmihYiAZcRXwNKIR4DXEcAF-wS6sIxXq3JiWsxnUApGRj4rlO_5180uqy2aPyJt_e7WJ6ClELvqE0Ob40fOoSv5fMi0DN1ZSEK_KDsj9DZcVucXSaPM26BCgzmWI2GfuqoEluPmzVizoUXiiNXiKI2aXQ_T_MAquW6nklq8NE0CaFPritl1DiasgtvQpPJ2PhjSyQRID8zM6dFhLngnnqSHDntpm9UDrPLgyL24BHq5tnmnaWVxcxuPQXsk9IWQ514RlblmBA7aZNIcNijQqgodn54TehIiYY19Vb_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
😳
ترکیب منتخب ماه آگوست بارسلونا چیز ببخشید لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105447" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=pPFdVlTzG9RlqG2V1XDVcdK9G9IFbj3vkL2_BbwCipUUwe8ODvjbxSfdBC_NLlBbEXdzUXt68RBevLKFi1jxbpMpVL_cz0S4-cBT7oOIiyXp9fIRiqzBv9HdsXVFc_xErzmbvWSTobZ16sASCZxaykfqMEXLW-ItwjIPsS2S0sQ3oYKhv1lx_FvMK0caegJ7L3V5JyDCg063xN6_-syUEIwhcTdA0rAhsfHwjWVT8-9S6Oe1Nge-x4JJifoS-zPTOI3qe9S3GJeX7EuZeJnR1gRPCljKF9Hbt6Qq8DsmV9Dup9yeEqhnqlpii9if0mDo1H6giFsf_2cNinUsylWNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=pPFdVlTzG9RlqG2V1XDVcdK9G9IFbj3vkL2_BbwCipUUwe8ODvjbxSfdBC_NLlBbEXdzUXt68RBevLKFi1jxbpMpVL_cz0S4-cBT7oOIiyXp9fIRiqzBv9HdsXVFc_xErzmbvWSTobZ16sASCZxaykfqMEXLW-ItwjIPsS2S0sQ3oYKhv1lx_FvMK0caegJ7L3V5JyDCg063xN6_-syUEIwhcTdA0rAhsfHwjWVT8-9S6Oe1Nge-x4JJifoS-zPTOI3qe9S3GJeX7EuZeJnR1gRPCljKF9Hbt6Qq8DsmV9Dup9yeEqhnqlpii9if0mDo1H6giFsf_2cNinUsylWNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آمریکا برای اینکه به پرسنل ناو هواپیمابر آبراهام لینکلن یه حالی بده، برای تعطیلات فرستادشون تایلند. از طرفی تایلند هم به پرسنل ناو آمریکا اعلام کرده که خدمات جنسی زیادی در پاتایا دریافت نکنند تا فساد اخلاقی در بین زنان این کشور گسترش پیدا نکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105446" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105445" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105445" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foorSyP-BboWcpSgkmi0r9djy0q6U_8fqvf0jid5zqUOZuypunmgVT5x9GfKgsqRdF3iu_bArq9Tv0ZdvazXO9MAcY8jNDdX-XqTVoHG2fCG0k0UU3GifNo7Z2ApnPWce0nh1jQ6l7Cy5ixtDxztSFFr3C1weKqYHhvOuWAss4AArU00rHQ8K2D8qt8TRJfCAVyblz11GZBUKaYe048H7RRQ5azpX1LyxVobwpSjcq7lc-E-AFcUJyGym_o121p8sE3h0TJt2vCPlx57Ki4gq6VfIOy4zECZqNhEGIvBnbo5Q3ESmVbhy6mSAUPhUPc7fan4QdaewOxN5xLkBEMogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105444" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4fM3vKrmphCxaXeSsdNO5hWWA3018nRKABgbNmeiSnGOEbnu6TTG9L6dUWRhqE6avCQSaN4gQaf4aimXnCDXmKc0ZyI3cHTvewNNWpovmzWbepIyLm3DfGx9m5Gjg7N70POzNQmkJh_M17fFiRrL8YksJmCVKOsaBX5ePLD3SuLQbF9BDn3cQF2HIhyqzgSAOmgeAhv4Yn-3ORHkeuSHhl28f7aSijkI2PL5bpkVpkNxvAHDyWhPVE6N4g1WaTUNdalemAYDEskRLKmsziHQWbG2EsKei576ogZIi8VQkoh9qCllERgE_Juf5bcQfAGYhiRyF-J03x4TMKGWKsrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2vpsah8LU1DTtro_unmqujr08E__oF_DvLm5-R6k2OeF-vPGwx1JbH18f14ybO4oGeWUatQagDjJwpujF3cus_0pB0gdGz42dgsVNbjzxy7X-kWUKq_RvBAF24gChdpC14ywkRLmTho5nyOWtbIU3HDENmwx-CDspGP-1fljE0rpsLjqb3jqyB1HD7d4DkI5IKhBTxKq7qsH9tF3R1W-hvDP17ftk24oxfWlLjcb9tJcsW98iLTkXKDvoh_AdFmqi72OtfK09OmT1maVTcqOIr-M5w5Kj0JPwwgDHU9RIA44ZuZy_jPVf7ovj4kMFBibnAU2NnlX96X26-CkTfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSYxGpCjoPgG6_MJb_He6nGC-dCjmRPw_PtrrDOw5ajQ3olOaSpN7tRPtx8JbVmz2kczLRxCxA38VKZKQGkv5uyNjEYHbTbHxACOCNTi_xNLkEksWae2Y473JnFsWpLEv3F0pvIeP-WMJGijNBSKW1uD9zTVzgpVxoFcB5i991y3eofUpHOeICNfJsMYH-cVEurn9tKKxIgeBRUD6ALntU-27a-eNC0NTPZPLAP6kIf9pcyx8mUFih9zNc5M5BQqfk7jXH3IF34PMjk60mlS6fSiYepxFt_TEb9CeAa46oEK_lmaoyZZf4KdIIq1KbOa3DDjjNIss9B5I-U48O3lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVF_qVl6IfNnrtpe1aY7AQZ_srhWmZCQOcQMbDuQdRmtoC6MIvxR-KivoX-Z9uWmz8d4_gf19f6vMFWZ5odDR2nZYGiJ6Hp5toRYuXjv2TD7y7FRuEZydvTGPdF8MbHIHXosd9mQ08kVcXiwafSp04mW0gofmyET6Ou5suIEdrJTCtsNIL5X-hApAJlUnr9yZhqDaM4h80LSd8UTl4gGdIHDyI4LjEUR5N9ZWO83lvgUoMY6CGs7g15VXEyjk0JrWFbDMOadtsZAXCIIg2PnJZ7q4_-xhqN1HqLtwDdf13gOlL_1XcuNC17s86bjeXs7hSWzhWRatjJYxz-FH0Mcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIWDyVY2l7tDoQ1M1YRVOnieHTTwN7KLnxmPS2ha4Z-oxGMZgQEg770CnG6g7hQF2v5MhLQ2Uuv3ZuesflT8LoBOJkFYMA7fAaIIecugeNU5XpzGIXovKPnv-kbMyNfF239NgaIUR7baeGYHh1NiUWwif8ASGXS1tIbTwdSXSZQKHtD3lZbHdhe0DWHtWRZRQTyfU6VR8gce8PdJG6A3AP8-q03t7VV54mzBJfRTAWbwRnLx82PqFKPx7y9g9rSQMdFDkmDqOt8nv8SGSOvg5CsUDmn_4cyz7y8KDm_Bj_TlG_tlUia3P9Djz7eVmQb1lTGZYgZCiDqvLOFSnre87Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
هوادار بانو استقلال در دربی نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105438" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تلفظ نام سرمربیان ۲۰ تیم پریمیرلیگ که ویدیو بامزه و جالبی هست
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105437" target="_blank">📅 17:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=c991qujrGde2A1vygcsYMPKn6wLSOaVL4-gz_RHQ0gsVE2lnpnzgsD6sdFoK_s9Uw5un41IqalF2_NqM_bWgEj8ciP-Xrrv56Kjew3QeJIawqJMWfQsDc26e-Kj_Y8gU2ztcb2EoYSVUEf2lYA07oNfP6C2Z8lhsZstIVeha3bFvnyXH0b4GKT--Y0SwfAGCitlt_rp-wp1OEIhVUR8vNPSW8qZLasoTjDQ4WjdovEwlX27LVLhhkEM4Q2MMGbLJayKbRWxa5eEV5Hsr9xbAsrd7ejX6-EU-NvC4BNVLSYSwzxKTabEuz6o3wUXcIs8_1rfQgXeVSDMIdzJArq0fcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=c991qujrGde2A1vygcsYMPKn6wLSOaVL4-gz_RHQ0gsVE2lnpnzgsD6sdFoK_s9Uw5un41IqalF2_NqM_bWgEj8ciP-Xrrv56Kjew3QeJIawqJMWfQsDc26e-Kj_Y8gU2ztcb2EoYSVUEf2lYA07oNfP6C2Z8lhsZstIVeha3bFvnyXH0b4GKT--Y0SwfAGCitlt_rp-wp1OEIhVUR8vNPSW8qZLasoTjDQ4WjdovEwlX27LVLhhkEM4Q2MMGbLJayKbRWxa5eEV5Hsr9xbAsrd7ejX6-EU-NvC4BNVLSYSwzxKTabEuz6o3wUXcIs8_1rfQgXeVSDMIdzJArq0fcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇹
سازوکار نقل‌وانتقالات در باشگاه کومو، از زبان میروان سوراسو، رئیس باشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105436" target="_blank">📅 16:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f719399999.mp4?token=oMYhf9kW1YUuulxRNt01gpcsyDi8dPhNwTYXP8fhFRGfulkmAPE4LD2cRVU_MLhmXWc52r5L_3d81yOuuplJekFutN6cH2ggn6N2iXAMRtTUs6miEjlu8gQY9AnyO92LEb1TgaFFOulZOXpm08kdHDODRlZ-b4z4d_kkt9gVctPsxzNXuddn-0qP88XzzXAOgY1TQpqVZ0m3AJtosech6pgVx7xgg26nitMeQBF1Hi_CHnckLaQuGyDJKs6RZzKjzVUoiBRQMD64KZHwiz4jh31l4m4PZ5xqy91YvOE7HrXXzu_-NvlpZWg47ZAVAHximJp0VhQOyMmz3FPz7d0xWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f719399999.mp4?token=oMYhf9kW1YUuulxRNt01gpcsyDi8dPhNwTYXP8fhFRGfulkmAPE4LD2cRVU_MLhmXWc52r5L_3d81yOuuplJekFutN6cH2ggn6N2iXAMRtTUs6miEjlu8gQY9AnyO92LEb1TgaFFOulZOXpm08kdHDODRlZ-b4z4d_kkt9gVctPsxzNXuddn-0qP88XzzXAOgY1TQpqVZ0m3AJtosech6pgVx7xgg26nitMeQBF1Hi_CHnckLaQuGyDJKs6RZzKjzVUoiBRQMD64KZHwiz4jh31l4m4PZ5xqy91YvOE7HrXXzu_-NvlpZWg47ZAVAHximJp0VhQOyMmz3FPz7d0xWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
امیرحسین صادقی خطاب به فشنگچی: کم‌کاری کردید باختید بعد می‌گویید استقلالی‌ها دوپینگ کرده بودند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105435" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=nF9pjTMVxNemvtlWSmgumEPKsS804viY09yaduYJnvV2s_B__DkSgH3DnMGL3KGsCutYNxoOtOjqggEwISgrqyh-Sxg2amVf4bp6GfCA38cx9Sbc_F5SAIY9IKDhjzC7OLukUA_aPWeXu5xyMg1XqVWU2W-1wQk5l026gS0RM6MbbxBWqKlhpd96KFZu7WDBkteQxzwt_kyHGVQtomY3FDXpcje08Ks0PhjSdJ2m8AcCOBpOYhYgvXXbSRcnq0zBe5nTEn6-p1z7M854WBRa4kNyQW243NG3w-nHZIN-qt6sQ-oKM_dG-2wQGiHPRZIFZwrjU8iiNXnRkOF7jUHdUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=nF9pjTMVxNemvtlWSmgumEPKsS804viY09yaduYJnvV2s_B__DkSgH3DnMGL3KGsCutYNxoOtOjqggEwISgrqyh-Sxg2amVf4bp6GfCA38cx9Sbc_F5SAIY9IKDhjzC7OLukUA_aPWeXu5xyMg1XqVWU2W-1wQk5l026gS0RM6MbbxBWqKlhpd96KFZu7WDBkteQxzwt_kyHGVQtomY3FDXpcje08Ks0PhjSdJ2m8AcCOBpOYhYgvXXbSRcnq0zBe5nTEn6-p1z7M854WBRa4kNyQW243NG3w-nHZIN-qt6sQ-oKM_dG-2wQGiHPRZIFZwrjU8iiNXnRkOF7jUHdUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
روایت وریا غفوری از گلی که آخرین برد استقلال در داربی‌ها را رقم زده: مسخره‌ام کردند، به خودم قول دادم گل بزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105434" target="_blank">📅 16:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=VrSeoMgzP2RTA0YHiz2M01ojhLYu9Tc6r1jKqBPqHh9EiInbFNQjRTBKrlipaRDu1SZ7X666KAp8-WP_FDGqnOOx1FPzNA2okRd-m1knGc8mg2gIp3U6bdwxMF4j5nsAvwCKgQci6IMzhynkMCZIBpLii5ETaxeJbsia-i5MTuoeGVOozwL_I-MLZQ-p39XFoxJHfvAYZOyYZl4GKbYm5kEj9Uq1B_Nra7wnkLyTTO0-fNvAOaxtoQc2sIv0Nr78MDdD80Eduak1eQXKjtshnTolEeKwNdHZOkkmhrmFWu1EVF_8GLoD0h5X8YaLUucGRfs_4a8tC5yjxH_EKjQntbWnfiiCPzeTrLdJE8IbiF32_4APf8DYAMYKRARHNvwAzqEzKa2Ig7qqaVVp3YEmGWmec9v2Jl8CUfhm-kK2AGP4Ro6HASmwngS7PRp4o79Q4QAHj01fjUeu1SRxCJ2nYdOgh0DatfPFKUa5-p5N72QCGCDE89Sf1blLl0gKM_SAxI9YdC9EOkCMmUjL92JdbeYnA80snpudeEsCiXU8biqh73USZx7dfHACRUWYIU5WHOFq05b6LXBaWrsylj-yIn9rQrFShniJTi-e_REz_SQIJul90k5Eyi_LmhkzwxEt3WyF253T5UlpDdJzHilaZnf_CCkHMhuGCOnZefMYnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=VrSeoMgzP2RTA0YHiz2M01ojhLYu9Tc6r1jKqBPqHh9EiInbFNQjRTBKrlipaRDu1SZ7X666KAp8-WP_FDGqnOOx1FPzNA2okRd-m1knGc8mg2gIp3U6bdwxMF4j5nsAvwCKgQci6IMzhynkMCZIBpLii5ETaxeJbsia-i5MTuoeGVOozwL_I-MLZQ-p39XFoxJHfvAYZOyYZl4GKbYm5kEj9Uq1B_Nra7wnkLyTTO0-fNvAOaxtoQc2sIv0Nr78MDdD80Eduak1eQXKjtshnTolEeKwNdHZOkkmhrmFWu1EVF_8GLoD0h5X8YaLUucGRfs_4a8tC5yjxH_EKjQntbWnfiiCPzeTrLdJE8IbiF32_4APf8DYAMYKRARHNvwAzqEzKa2Ig7qqaVVp3YEmGWmec9v2Jl8CUfhm-kK2AGP4Ro6HASmwngS7PRp4o79Q4QAHj01fjUeu1SRxCJ2nYdOgh0DatfPFKUa5-p5N72QCGCDE89Sf1blLl0gKM_SAxI9YdC9EOkCMmUjL92JdbeYnA80snpudeEsCiXU8biqh73USZx7dfHACRUWYIU5WHOFq05b6LXBaWrsylj-yIn9rQrFShniJTi-e_REz_SQIJul90k5Eyi_LmhkzwxEt3WyF253T5UlpDdJzHilaZnf_CCkHMhuGCOnZefMYnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥇
رضا قیطاسی پرچمدار ایران در بازی های جهانی عشایری به مدال طلای مس رستلینگ (چوب کشی) دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105433" target="_blank">📅 15:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=I97--gHBsBUuB1bVVGeYh8Uw0YeImBhxr_Dq4-gGcirDHu3Ro_7Wyr-o1spcwEjx5YGRTSpkcwjXFKWixyEV5_Ix7kZ_6OtM86QnU7KiS5DdjkZPMn0PH_jdCfSmNfUicYcxunDSBmXVkwRqLE-6SZpIlRm7cHi8iqmRMVN9uLhpBbMabRLgMfqCikzR1DH3iVvgrqJBfa8Eu9bYxcrFm-4MrSU2ThpVxJR3hei8Faj9BPKm01tE4jkfXWRyBKz2Kus6JA3p-khol3I92FjVxwab4wH8pB1VRECdoybIJsJQSbVIQQ32wYxi4qxwOMd-6Fim5oxUwB5vGtwcMFlGFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=I97--gHBsBUuB1bVVGeYh8Uw0YeImBhxr_Dq4-gGcirDHu3Ro_7Wyr-o1spcwEjx5YGRTSpkcwjXFKWixyEV5_Ix7kZ_6OtM86QnU7KiS5DdjkZPMn0PH_jdCfSmNfUicYcxunDSBmXVkwRqLE-6SZpIlRm7cHi8iqmRMVN9uLhpBbMabRLgMfqCikzR1DH3iVvgrqJBfa8Eu9bYxcrFm-4MrSU2ThpVxJR3hei8Faj9BPKm01tE4jkfXWRyBKz2Kus6JA3p-khol3I92FjVxwab4wH8pB1VRECdoybIJsJQSbVIQQ32wYxi4qxwOMd-6Fim5oxUwB5vGtwcMFlGFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
اسپویلِ بازی بارسا-اتلتیکو در این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105432" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvSsaspaQRwzXyFbKSqMn9Lrf6CmLkxXwstNzRRYcaB0WCyAKIchl3W0eBjCNwX5SKAucfeFsQYfXDwsD3BkMxvF1MtqOSjIXfGnOeYllWNsAtdTzMAy8g2Yy33bs9y2fziqhLhLgFiOHx22YKFu1qDRWwM65lMJhJGMQe413NbdBogeXJ7V1LErzjci1WJn-KiUyPN3ungFKZv_kYo1CbjwI9m4Q8M-SBgkX7TZ_1Aglps0jdRSCE-m9HNpcW3wyMTxFdCa32p6vjzlAI0kvaCZ6qYE3NSrlGNmbcmve9KUjNyQ9FB2KmViPs98JzSwxrJcnlTYC6uefElPR30Klw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YV6aqlVRqQ1z-bc4o22qkZ1eoDAWMNCehfoyuDDMuEmNe0a1vPIidPNOqw7nJXP70DT_TbUTEv1J6f7oQyE9iVO-61yRtLoTEYKF8aPm1a4B9vpkrpwzjLrzTm6HxVFQd9gRE8RHc8ZoGBo8N4Jj_W5UWnNJU9uk7Kg7vHrNF7rqCQ-uCfeck0exgwl0XT6BEP3e2Z-YdMGrLJ7JoH86EkpROU6iKsHfm3jvtWfUaZJPnVQlVCRPfuHsRFnLnDH4J1dZwxPCFIDJAcp09HMuePaJJ_q26e71QMY6XbURqY51EvQpw9T2nPP7R2DyODhpbn-nJ4rqth-XdKAu-lgPTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
عیش‌ونوش لامین‌یامال و‌ زیدش در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105430" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO6oPosicKPUxOigmHX6oRBKbm1sc9KgME8Q6UhigFMtOO_V09EjL-N_OjY4zmRhex5MwTMlXmDZJ-Qc-Fa5V7OD2TlDxgm84BhbT1LLOhMoCCGQOBi4mKew-4MJCkZNyqrhyLpdSFO4piRQoq03DCad6bhNF4zy3eOJCfHYa832PLaYEKPqmoWRzSicce0aCt5EzIB2P5N_v79nbW3-xmBRb6RqThIoa_lXOLaJZgTRBK4YV76hb739oDrGODX-sCsQBa9FFQJFA0GiYyQ5weKq8Atk2Hv0MfRy76apu7fOmGEvroHYGH9TP0mb2WO-Sr7jTlE2-9oBxhGQpubelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105429" target="_blank">📅 13:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105427">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBs6d70F2cNfJV6UsV1n9r20R11gGiSUlJxql6ol5VvW1UDyULtR_lY-uZEC83giFa0a4dAs39MYBXu0j-1JsLbK9m9rJ1PeLTzZlmLuIiHWOvII7jYvM0ZrSr6nzNWR8U2hqb_beaAgPbdfZXW_CBRyixCSvAHVU_ygZznVPXZzzaCVvbc34QgfI3Y6oIhhNymiK_kUa5XefxF-Rh8l3-peqqsqW92M7DsbUvaCrCNr36YGeKvPQ_-YS-hHScyxP3IdiVqKZ3R0pNzqy-rrJo4tDo3M_e6m1S6hPVhKCxLyln52KM4YSpjs8FbBJbzPckoYJti04tK8aMoTniFUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105427" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105426">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHzhKcZj64UEsrQqa76KX4rAFYU89zB0s1Sp5TUNNzsbZ29fay-a4hRSACaf8gO_g-1i3DBjZBKKLMmPd11qz_we2LBL6SmBdti6KpdW4Rhp3xAfMJnyf-NM-UjsF6hmDFVYEd1TuJVboufLCilELHJWdEfJIim_DMcH7ddHBUuNzRq4AG_HOL4uikS4_hLwNLpcB73AFdKaQTVwP9c0JBruPqqZTyw-IcvD4FnJPeVQWkBy9YNXlzElxOVTx0AHiPExisQ-tyNwCxku5PO2IO6VuFW4Ze3alwh5OaJzqPfMAjzP5qCm1mwLEZm3Rk_A47jQNaHFrgYviYrrkAxY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!  باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105426" target="_blank">📅 13:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=usiUcYPuvTaaAeXBg2CzXhcLH--Rrysd-B1YGHHikdGFr4A001ta7SqVcNQeFVc5GXgCkjJWjcdzmbomr88UdNyImV3SnQ_JhswdBGjwvUENZYp6bywosRnWRGqWiVeqvz_i6uoxd7VDhwLBuIBgtY4mhyjs7bBfahvih7j1oFVSO1AbNZ-_adNDga54sbrAu2EnDYTaVWLPbGRbi-Eh8nMQBc7M-xJwehDDavyOsS3nKbeQbGcn6OMOIZFJql61xitDGdTogRC7IvYZUlAFo0wDSpR9Dr3On2mdW6Arhu_qelHZkfYCUifizJUEZpjr3cQg3r9RDlZq-lejSi59yxnYJoYh0Ytndsbuqbt6yqU5_ZWhzaooOvBTZDoycRD8Do9qw1GPzqAedil10v0gFngSfB-5IwV035txJr9JAkctwnB9XdR1xFHmrTuthhReym497a1JAN3hVAUjdZD2JtYbGbxXKfNj97EqiJ25KISTAqCk1p-zFhg0z3nMsGFZGvhIXB9DPfI5MN27cqrgkw9pcxOWISTCRHcdHiSrXJbKvQ6zQoLAPkb1Byhzqcofd5V7PEBRtiY3mNPzA_c-al6bbDUfgByDtfF1SCQIOSqMiDqCOOj0XKMEm66YZ2HAVnB8ZNmZzF8Xhde8LA8WFiu3fW3tESWR0HbzWx1n3xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=usiUcYPuvTaaAeXBg2CzXhcLH--Rrysd-B1YGHHikdGFr4A001ta7SqVcNQeFVc5GXgCkjJWjcdzmbomr88UdNyImV3SnQ_JhswdBGjwvUENZYp6bywosRnWRGqWiVeqvz_i6uoxd7VDhwLBuIBgtY4mhyjs7bBfahvih7j1oFVSO1AbNZ-_adNDga54sbrAu2EnDYTaVWLPbGRbi-Eh8nMQBc7M-xJwehDDavyOsS3nKbeQbGcn6OMOIZFJql61xitDGdTogRC7IvYZUlAFo0wDSpR9Dr3On2mdW6Arhu_qelHZkfYCUifizJUEZpjr3cQg3r9RDlZq-lejSi59yxnYJoYh0Ytndsbuqbt6yqU5_ZWhzaooOvBTZDoycRD8Do9qw1GPzqAedil10v0gFngSfB-5IwV035txJr9JAkctwnB9XdR1xFHmrTuthhReym497a1JAN3hVAUjdZD2JtYbGbxXKfNj97EqiJ25KISTAqCk1p-zFhg0z3nMsGFZGvhIXB9DPfI5MN27cqrgkw9pcxOWISTCRHcdHiSrXJbKvQ6zQoLAPkb1Byhzqcofd5V7PEBRtiY3mNPzA_c-al6bbDUfgByDtfF1SCQIOSqMiDqCOOj0XKMEm66YZ2HAVnB8ZNmZzF8Xhde8LA8WFiu3fW3tESWR0HbzWx1n3xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
🇮🇷
تمامی موقعیت‌های خطرناک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105425" target="_blank">📅 13:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNU5hYcXB-ow636iE1DXbdM42dz7pCsmkHc4TiOmXKPRsr_B2wuPkWZN_nWXOfxScHs0MERKJBAgIW3611ZiUF2tTFL3KKIiL3bfl501fXkI591isFhw2BZbYjPlSpJ-yYRFBhGt4oxwE_bPQaE1I_b0UwUiBg7x1J5DeRbcOoXrmVEZGHdCdwR4B5Tg7XVS3N2oFTOeeK4u3Lip-FGT4jAc4g9F75ace9hdEpRD1w8wB5jjvosupAB4omKJHA06oUhyuOj0_WROCoKgRKRP_vTgjNKcPq8CLqf_GhFmL07PYi9cANFSf7gtdmOBzvNoPHWHuEfvnH5FazG3bvnQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105424" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105423">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105423" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105422">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkSRVir4A2f0VmWdRfQLwvHBEC29xPBZJMDq4ZmGZT4y7HJxg3bUqjZiN92bXy2GCPl3NiyHyKKuA7B2oETsDZeU6Xy-Wtxk9ArYq_AXkVzDoHBD_3LTWn70W8krSG_pl86W53FCFOMxyuUS9Oy_HtkhLr8yRUTD1Vv7rff-ikPRtzPn67jrjo5U1xKmWrdZUI08L5OrhGKON9JOd7xCPJ-_j6vxUCvJkLjFofQDG2KQmBHQeZfkysB1YRjhiR8bA2Ony0nEWw8TGLOxCHxQp_dEBsDcigIMzN70JN93opRuhci2dhvsmwXzKJAyzLb04ZD4U7292v_F1M0GU9G2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105422" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
افشاگری همسر رشید‌مظاهری از شرایط این گلر شریف سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105421" target="_blank">📅 12:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZE3hjDUnx6_dvZdVyaMLJm3X0eKodqmAMxEs5b2WuAD6wiJt2vCgzesJULWlGiuW4mQ3AF_hPPfOO8N0C8S2HHp--CvzsTNbAsN8t-FWzcSgDBKbN7mWiJjJ-ydQj37iCQVocQDa5hoUgMGJbE97NOFYdX_se3eQu70Ksn4UdBPUwIR3P3XGX1UBzu64OTdKrq0M59cAXLNqgq00rJ9mwpjjLYrQC9X67BUO7adgg5v_K5otc-NYXXIW8gzwQzUI54wxwaOHDNJUuB_T6LZ8MIprurQYP9bMKs62CCtoN7iUt80bopEiJkhJAWAeIqJQO0R1SkAqQx2-0RkWw2ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
✅
🇮🇷
پست اینستاگرامی مهدی تارتار سرمربی تیم فوتبال پرسپولیس پس از داربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105420" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSQm6bEzzlVu1CNEzBZ84pQqbaeG8ScyUGTj4XdCB0JPd7z-A_iGveDb2nKSxWThXGPu9IpxIU1LztfXvRHe9zAAqnZ4kdtMQ7Sj_ZgbvZts1v0FDnABAnnspR1bKRUjwSCXIcQfgE5gZHYj_z3Y4WM5sIBEblB1fBIlUlINN2ivRGltLF1LAR8JhzzSsegtrz78zjnwlCOH3qscp2rWv4FpI6JMf7SzBcWyFv-8FYErlmduGHQH0auGlisovviSvCAqiZ3lsMQZEUfTAtm-TRBXQHeWcOr3lSj-EbQPWWHdqpP2ldQWy0P3nkQXTMx2QXvHmTXA92eEkx83qFhwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
اعتراض تند مدیررسانه‌ای باشگاه استقلال به عدم اخراج حسین‌کنعانی‌زادگان در دو صحنه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105419" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105418" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYD-oQlVqaV8x4ugevwR3kWbimSgLTNESu5AOJGScrOZMeczgiWaL9WgNUlTd1kNnisRtyZ2t98k_bLHJtZgc-Y3Bw030yOwJ-SAr9OCzxQ2OJA1QV2SUUYZkrmgJwKK8wCxnYEctGLBT8sW34pS1Js9X0dM-I2cpt7CpcWR5MmhTYn4AEFBTdvV10Csv9yRpHj5ySL1VlU9NyddlOBujv9_lECEmvVhAMc-IZ3CpxuAU9iL06r7lmWQYDbUV9FXyPCP0sUpvVqRTtb0Wh6icvg-Hh-Ejzzamkb80GKUXroCj2ahyKasTFXiJFjBFF6TnqaFjYjDKoN_uqGO6pTVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
محمود خردبین اسطوره پرسپولیس و دخترانش درحال تماشای بازی دیروز دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105417" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105416" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=HsU3y0RZ982xLVwFmOheoo8J2cFGRKJRIX8qDTaSCcmgtF7nykxpbz1Bp4P4eEzMhA_-AbmXNWfd7fw0XfmF4c28gubzuVG_9NG-z37cW6N5N6LQ7OR9fF198dnkrE4_3SLjpSJmH7JlfVCO-IWYYu6CrkTjw8oARL-nfbacobWEOfhCqL1hAj_t7asp22P3ST4igviF906mniOUulBp3n9NE5JVnbWMo8_e_aj6ZdyZSahebHlMuPzlGDseyRU4ZaS-94DPds__0a2AfFknorL2Pt9o5tR8v0_pCdHzgCb8p_RfN8RBnv3BonyF7GdPtuLMBdzCLE9yO-GLM9Q2Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=HsU3y0RZ982xLVwFmOheoo8J2cFGRKJRIX8qDTaSCcmgtF7nykxpbz1Bp4P4eEzMhA_-AbmXNWfd7fw0XfmF4c28gubzuVG_9NG-z37cW6N5N6LQ7OR9fF198dnkrE4_3SLjpSJmH7JlfVCO-IWYYu6CrkTjw8oARL-nfbacobWEOfhCqL1hAj_t7asp22P3ST4igviF906mniOUulBp3n9NE5JVnbWMo8_e_aj6ZdyZSahebHlMuPzlGDseyRU4ZaS-94DPds__0a2AfFknorL2Pt9o5tR8v0_pCdHzgCb8p_RfN8RBnv3BonyF7GdPtuLMBdzCLE9yO-GLM9Q2Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هواداران اسنابروک حریف دیشب بایرن یه طرح قبل بازی زدن شبیه ترن‌هوایی که خیلی پشم ریزون و جالب بود. تیمشون هم در نهایت از جام‌حذفی کنار رفت
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105415" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=gC5rCDGEoHBENO0duaK0orZH_dRTBVWKodITyc0BTuxGcWdEUPQ5Jh9AAbUKhIhUXxdadMhbuovTb007KYDukS_3kLLGwUmpcb4XhEwZ04He1_zgDy50CcbJTuYrNfP9I33lKv-cMlW8ah2G6OvhqoaSU63l1tl7zodA6Tby65IgAHa4xtlBTdjC_uMK3xt4Q6u-YVMFxO5SftZnN6NpFaUDhvniSwNHcTyY0wNUFBBfASHBXyiHeyK76nayX05wbpjqpif_Xwip8se-5Mr_1ytN2Op-9fDDJLjIe1_yorjDzR3OUHT84k7SpQtAE9fCZ31beU6_GNle2VFrski5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=gC5rCDGEoHBENO0duaK0orZH_dRTBVWKodITyc0BTuxGcWdEUPQ5Jh9AAbUKhIhUXxdadMhbuovTb007KYDukS_3kLLGwUmpcb4XhEwZ04He1_zgDy50CcbJTuYrNfP9I33lKv-cMlW8ah2G6OvhqoaSU63l1tl7zodA6Tby65IgAHa4xtlBTdjC_uMK3xt4Q6u-YVMFxO5SftZnN6NpFaUDhvniSwNHcTyY0wNUFBBfASHBXyiHeyK76nayX05wbpjqpif_Xwip8se-5Mr_1ytN2Op-9fDDJLjIe1_yorjDzR3OUHT84k7SpQtAE9fCZ31beU6_GNle2VFrski5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید ایگور سرگیف از تارتار بابت  تعویض شدنش در بازی مقابل استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105414" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFRE4ZxsWk8o5n1WpW2JuZNyXYnya8aoiTbQmWuSpEj8ouTaTRMwDF_-469UykrTfRxzjeIlWIVTrwjnm7MtTkcv2-sTaoouS-kY94OWho3T5hemTo1K5cau1bwdBCq8Yu-J_93fw7HogEEgc2z21b_-n4i3azSG5G7ltEiM9_tiMpGB6jmcr4V8qtjH6jCLvjGHBCARSKV3aoyulYjt2ZKvRyydA22EVhi5jMxWtgVPlh8pG-gHNcpDEwRKk_jFEpQopvTu14_Pn3ASqdJ7J9Z2npuh4emTEFiLCDQz7knNQVkWgAoYpYIEtxvndeeT1mr3agqrHkRBizOAIUJLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
✅
قرارداد کارلوس کی‌روش با تیم‌ملی غنا پس از درخشش در جام‌جهانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105413" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aSYYhjNBqZgxS49uChfxqgfx5qoY6rWrouN0b3dkR6lJ5glByTvTE6HcvRh_10OkpU5o5QVjezG4lJKQO3lpYIHuGIRy3ca-Cpl9Y_lR91In-IvtuFHJwCAQQYox5S58_tsJXNHfAzvZSZDIo0TaznTvBX90wVn4ELre6k-_N2HDP-0idGofGnAlA_SgJ-BGnbeMIpBrJK9G6zGd7QQkE8b7BCwlJ0yjT-JDtHyMc4lp7f8t9Cj03ZCQyJhTIKlLLomXh4cLcwTEoibwyxWRFlDRlmHiEVXUi-B_F7Z7IGkUY_uV0IbrRnhFgwezaCMjMT1snVD77hwV1hN_vSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105412" target="_blank">📅 10:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/105411" target="_blank">📅 09:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🇮🇷
🇮🇷
توصیف‌‌جالب عادل فردوسی‌پور از دربی جذاب و تماشایی پس از سال‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105410" target="_blank">📅 09:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/105409" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=RDtxQ1r1LFZFqd6VYKivuGQa7N78-NjexS1hM9NrfOonH9Deg7fIaqRPU_n6806gVmenEr6O5dUjE0lSf6QJ0lUlyhrMLBylGbmgAJWYZkwn4yNJvlI-5_uJgOv4LUxwQsgiE9BjsA9lrzYjKslrpexghpyPUj9fJSE768VIPyghh3N8MuGRubNDX4KXeMFoisF1xwUWtPRi_NK_70SjAMWv-Lq167Nf7uOCy9DVJEhyKcZ0ActqtaP5M_LfHsaXsm3dwtAdPB8u5H4w9IRXxw0sZ1x4OJc7fIR-jjrbAMh0_OSnhDv50Zu6XaNmx0x4V0aFACttC28m2_qNzKbjGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=RDtxQ1r1LFZFqd6VYKivuGQa7N78-NjexS1hM9NrfOonH9Deg7fIaqRPU_n6806gVmenEr6O5dUjE0lSf6QJ0lUlyhrMLBylGbmgAJWYZkwn4yNJvlI-5_uJgOv4LUxwQsgiE9BjsA9lrzYjKslrpexghpyPUj9fJSE768VIPyghh3N8MuGRubNDX4KXeMFoisF1xwUWtPRi_NK_70SjAMWv-Lq167Nf7uOCy9DVJEhyKcZ0ActqtaP5M_LfHsaXsm3dwtAdPB8u5H4w9IRXxw0sZ1x4OJc7fIR-jjrbAMh0_OSnhDv50Zu6XaNmx0x4V0aFACttC28m2_qNzKbjGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvl2WsACVE7IdiYz_s56wjj6z_jmty4OsUg3XvcRp1Gt_FHZEyGMcs-h5kRJbngXs4sCELYptHeCmURZJIjvSV8bld6-u_HIpZselM4_vGESW80yB4Mrh-I2b4U2Rxm235uso6L4L7g27wQTsCu_tk3uFw_IL6wXd226hGBYJX1XPYL9gQX5n6YhJe_8X5_imG4LgSNfOQxqN0wEkfYhR6myBVr4mcUFBHzPSK48VYmT3NW16J0HDcdSL3OJZ3NKyXRwVDwgE_1H5n4xrMWvLVngB0z08RDbJBZVZbv3EXfBY3Z8pEF5OaLZpvaO3LuTmkpv9hVe30MDZpH7SrSgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=CuFjsjsF5kOqq-7FQFNWQx4xkUXcXGJfz5YlEwM5B55JXCERDy8n_4XA3lu79yqBQrzVKICSVYJ5J1wWBuufGsUMU0IP7CBcF2b2bHo8pmcUa6pHqXZdAmk_7SmOEq6TrQBmLNeFdnGJoNQ6kgdGIQaypEDGnO56ZbgeGAaPvSQC2NDgcGpP19WXD6L5PRbp7RdQJbDH-daQBvDAfAd7rigQNAbFqvU_Xtb8ymY9mM0NlzqA8ddaYL2CUIuWkO6I_fmbEWh_JNvn6daCE6144phubrUwm76SaUhLM4gI13pHt18lsxFmlJjWPb_tGCPbDL-brh2KzWyf6AaUwlMglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=CuFjsjsF5kOqq-7FQFNWQx4xkUXcXGJfz5YlEwM5B55JXCERDy8n_4XA3lu79yqBQrzVKICSVYJ5J1wWBuufGsUMU0IP7CBcF2b2bHo8pmcUa6pHqXZdAmk_7SmOEq6TrQBmLNeFdnGJoNQ6kgdGIQaypEDGnO56ZbgeGAaPvSQC2NDgcGpP19WXD6L5PRbp7RdQJbDH-daQBvDAfAd7rigQNAbFqvU_Xtb8ymY9mM0NlzqA8ddaYL2CUIuWkO6I_fmbEWh_JNvn6daCE6144phubrUwm76SaUhLM4gI13pHt18lsxFmlJjWPb_tGCPbDL-brh2KzWyf6AaUwlMglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=QSuCkiACNvB2L2Wf7jk2kGVfoM5GQ7mlVbfGJxF866ntDpfXNSK4Y1QStgK4_XEg36wV_WPrGlWL19oE4YrdCga50v0Yq0cPjFxSiu6W0ljQ652hAFvnx5nhAIPvOm0hdLnXMHhlXtWE6Qhv1caK65pY9lx9CnWOWHKLqokd1VnQzqzHxvlm7dIvhUgzjeCtQoPw3-GfQSXAzsCRMIN3JjQVHD2Y5eqm2tjUlQAocNZYxEN6VEU9SD5SpHIPNu3mmauhZGcfuFkF4RzOykJ2CP77Rsl4NVYtcSRvK9FPVd-5vGJy_hniahDAi6VLFeaZivjgs707UG0tq8YbGtIopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=QSuCkiACNvB2L2Wf7jk2kGVfoM5GQ7mlVbfGJxF866ntDpfXNSK4Y1QStgK4_XEg36wV_WPrGlWL19oE4YrdCga50v0Yq0cPjFxSiu6W0ljQ652hAFvnx5nhAIPvOm0hdLnXMHhlXtWE6Qhv1caK65pY9lx9CnWOWHKLqokd1VnQzqzHxvlm7dIvhUgzjeCtQoPw3-GfQSXAzsCRMIN3JjQVHD2Y5eqm2tjUlQAocNZYxEN6VEU9SD5SpHIPNu3mmauhZGcfuFkF4RzOykJ2CP77Rsl4NVYtcSRvK9FPVd-5vGJy_hniahDAi6VLFeaZivjgs707UG0tq8YbGtIopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=c8i41I8oUhHTt5CdO8IYI7BfLmWiinvb1f9HB9qFSJz57ednTb-_TlXcFqY-AppBJiMw3uwZlRDiOKCuhst0RSHxuzcEu1WThLvFSyNNDpOkfneBrQ8m3R0ulVbcPp3uIOe7XzmKLH1TuR3lkHpuElsAYnHSeDjuIZszE4JPPDTGLUBh4QvNjcqHILkHg1Su0KVLjFX40STFuESTioV0yMSuzIK9Ayvp6M1LyiH3RxXK8fUTbmXWgS0StGWC7VenCRUD9hGgdZm_XHzG7cD6s7f3tZNpKF7ZZ394nJWULBetqrDALwGWWrkAJmwQE8-5XWjOW03Ks_L1rHETIBxNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=c8i41I8oUhHTt5CdO8IYI7BfLmWiinvb1f9HB9qFSJz57ednTb-_TlXcFqY-AppBJiMw3uwZlRDiOKCuhst0RSHxuzcEu1WThLvFSyNNDpOkfneBrQ8m3R0ulVbcPp3uIOe7XzmKLH1TuR3lkHpuElsAYnHSeDjuIZszE4JPPDTGLUBh4QvNjcqHILkHg1Su0KVLjFX40STFuESTioV0yMSuzIK9Ayvp6M1LyiH3RxXK8fUTbmXWgS0StGWC7VenCRUD9hGgdZm_XHzG7cD6s7f3tZNpKF7ZZ394nJWULBetqrDALwGWWrkAJmwQE8-5XWjOW03Ks_L1rHETIBxNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1qXW94HTezN4qlggpqm6ipqVjm_OOHQciYpVAGilBwmvTBxIUjrwKsBsY9T9tNROVdiWDTUm7tiZg5FXQzmlRWx3tmEGm9Vg368CyaqKi88I0EXySup06LjyorY-TRCmb3aOIDGHiCGJbvDfSRaQ2kKCZBO-fGVDDZouG25kXVcTiJHAV8Ild8w4PiKOP0W66_fW5zyOV_kJwfjRFkSQWcqhYp8CijDrvmBhmQ2Z0lxPhyHf2uBf_l3Qg53DoflXI1mng0Rnz4R-ps4MEQQzpga7Pm04sDJKqF2z9ngkdFdNIX1rNtikgPAaCqiXT0CPF34KB_7y-C0BuY3zTrTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDN8ZtvhL_cfde3kjZm5An8yduDtK3jTF1ZEERiUTIs40jvc0DeHEUprq0u1qjFz22jSw3XRe9saEa-rs0cF-NM0_FiKoBr6V6ZiCwLVMR-Q9SePAlPD3rZM2ItkzQbBrwBxJ64ydxZ8IN1uXvC6cHxK99EwXKD9NToVMjvUOuOV1HXTK1QzNckQ5w9fgisd0cEcJlsiWcCQqYzCykvRSJhoIblsOy2AF1UzLU8Uqi_WQRKQghbn7_jImGo46AMcmVaJUPvMkE8YQTDJl4Y6wvkKfXAa6DuXrV_J5yFE9S-zPVxhiA-qPsAWryMKaKGi62gVuSDDHOu--PiuTrLWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=J69g_potxa74eZYFXx8NruFQySVIwYMZJjLvw72Z5ArFEpEOPMGDn1qbT8SvSb1mIChaRUUzbcI0J32NoWwW1ebnKhSMB-1h-p2Xi_rsjltPPRj7y1ycyC_vziBfa9QTQPSFuI9AKPNPsH-pKKcwUbvpciNYfCuBfiZtxAavs6pCoaTi1tnTzj148_i16mkcRkzwwkfMqEWEAwwbomPQ6cr7_1PMxroezFTuxcY2kh3ZqST9vRJyu7Bt3-uvKi7T1s8KzNf7XhPzbu3Z3anUHYc280SjZPu6X3IqVrddjKPfxiYjTh3RmvZg0bjU99rOUPq9XioRXGXm56lA2w8kfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=J69g_potxa74eZYFXx8NruFQySVIwYMZJjLvw72Z5ArFEpEOPMGDn1qbT8SvSb1mIChaRUUzbcI0J32NoWwW1ebnKhSMB-1h-p2Xi_rsjltPPRj7y1ycyC_vziBfa9QTQPSFuI9AKPNPsH-pKKcwUbvpciNYfCuBfiZtxAavs6pCoaTi1tnTzj148_i16mkcRkzwwkfMqEWEAwwbomPQ6cr7_1PMxroezFTuxcY2kh3ZqST9vRJyu7Bt3-uvKi7T1s8KzNf7XhPzbu3Z3anUHYc280SjZPu6X3IqVrddjKPfxiYjTh3RmvZg0bjU99rOUPq9XioRXGXm56lA2w8kfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bamKowMVMQn-gcIv8pG8zx4jUyXf3pqRWoDVC3GQ5waO20s1pBUTdcHvoo91evG23oo2I7Cv_shGWwmHhkpH96pYLHzNHM-sxOLCoK6Vv00UigbUegQYJdnlMEfoM4gJB8OEeWlNnopS84RIUs8xMdlX62nTVayrHetluk-r8n-Q21kG7GutzN2JbGSUH4A_w1-fixFl6mI9HV4extJarlgYTMRy_DmPGm6iZTXwJoqQE59iElnpgBq9p9MlXDT3PpD2iRQoQmry2mOABXV0D8qvlowimmGljZNJgmKea0vtE3wN6GXcg4Q5e7GsVAVoYUwiNp8hgxU7mXzqrjKUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=GvcmYupcn1SqIKAIn4UPrmsx5yjBe0aCchsg3rlSD9ozaHAVtjEaxJra2hBGkXZd2bQDSIcOKlRldHhIi8XDNYXJqxVXbmmpZE10_ZDU27vYSoq1BqVFvDSAIqVonepsMde8m6zf7E-2zOVnth99aJIPpVxzh7oMsEoGNzWacfx5Zr1m_4vxbNUxTwcGa-KgUz9Ob96cZSgJ7tnMnzWgIqmvUB2b17r7Ss2lJ23vPhywXmzk0NEC1uGuLEQ-wVSjCDcVPkaH1xqZsUnRVDcsdva738--gXzIsTQOJUn6KN-fWJKR39raneW1ujF4iVM41MfEsRVgixk1HKZZ2G7EtQvr6z0CECr-hupE8zfplR7r7m_siAAxwkP9BZ1xLBKTqAOoiZObsK4k_K_SgMivDUp-biVBhvr1Y7kvmyt1CYwc15MbtnRdP1s6zX4wlK4n1rO7Dm4e8dCLHnXplW3-p7HdtFPyCq1kXWu3h--91_mOEtQjsBwkuESAAIsJN9Pn_3p8gUKS74jZSerRrrFuQR7eNAxzM0gwrRouE_H9R85SsCvP_7Z3B9Fh09NwK4pmuxUs6nI8F7A7Vlgo7MHy70hq6aWK3Qlipq01FSOU9eg8iXyt4eyf1R0rjFSuLPHi0s0JAqGVS_QKfFH4UnxKjIZoCflstbsZNQBvVLo-fWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=GvcmYupcn1SqIKAIn4UPrmsx5yjBe0aCchsg3rlSD9ozaHAVtjEaxJra2hBGkXZd2bQDSIcOKlRldHhIi8XDNYXJqxVXbmmpZE10_ZDU27vYSoq1BqVFvDSAIqVonepsMde8m6zf7E-2zOVnth99aJIPpVxzh7oMsEoGNzWacfx5Zr1m_4vxbNUxTwcGa-KgUz9Ob96cZSgJ7tnMnzWgIqmvUB2b17r7Ss2lJ23vPhywXmzk0NEC1uGuLEQ-wVSjCDcVPkaH1xqZsUnRVDcsdva738--gXzIsTQOJUn6KN-fWJKR39raneW1ujF4iVM41MfEsRVgixk1HKZZ2G7EtQvr6z0CECr-hupE8zfplR7r7m_siAAxwkP9BZ1xLBKTqAOoiZObsK4k_K_SgMivDUp-biVBhvr1Y7kvmyt1CYwc15MbtnRdP1s6zX4wlK4n1rO7Dm4e8dCLHnXplW3-p7HdtFPyCq1kXWu3h--91_mOEtQjsBwkuESAAIsJN9Pn_3p8gUKS74jZSerRrrFuQR7eNAxzM0gwrRouE_H9R85SsCvP_7Z3B9Fh09NwK4pmuxUs6nI8F7A7Vlgo7MHy70hq6aWK3Qlipq01FSOU9eg8iXyt4eyf1R0rjFSuLPHi0s0JAqGVS_QKfFH4UnxKjIZoCflstbsZNQBvVLo-fWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKoOcj-AGbSmtVQB83hQuneIsISZOEQgtgS70-udxX03viy5BWtFHwgF-z7rL472bE-Iw2PTUDCTytFzgi5Cb0F3nLaZVYPZ3z-nxJRQ-O5lXkNWZYGtWEqkkIx-eDfXfsReAE_I2Qy5mRUu_RnMlviP2-Zz6iTHEuQgIksZO8hMK6Qwe_wEfAfvfobQqtYkH6mSoGF2oNaUCF54CkgHbHmM2X2ykziYZrQib-2CBu0E0ECfLLpT_pc8q4g61g6c73HyzmSbEEpsL8HpKG3PM1-oFHtH8qGEgtMxOYETa2yNjtaH_Yw6VewymPWqEyJ6bDFE0jpovoVjwILye35M0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
