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
<img src="https://cdn4.telesco.pe/file/rQNdqqN80ZKSCt3IXlYdWn7zfGYBrB0hq3I-H4bHCHVKAUw1aF27P1T9qfGf-v3Yf_6xZ5VfXE2hcD8bYsMPklkOgiusBDA_APl3qLQTthPVYZLa9P_QDHaQrSYBJIWw-JxgfIPJGg0oEuwtwS9LoxdgTSV5143CNRg6s2VrgBbENl3RbL8RcESBkgUK2IX3Wrgvi-CeCZkS8gPywoQOjzZoOXyhEEZRcXfmoJagDs3f1zNOAu8K-g-VaYviL1-MEHvXQjsKQF_kuZgwZI_RJURb41jyb6ZUzmTFy4X57KpeVf94NKzqaSpfSDgTKVGsMFr5SkAYb0EnT9AyZpFH5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 115K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC9f64ZE2kVVcnAq6jDHym69fh-jwbfABGU4qa8pWNXPPM6fpNv0FFFnaMuFe6BD8duzzfzonr-1cf2-OT-XAOWoDWrvJNpfMMfk3jB9xEMenryA0FmVfQgNIBEjXIuhhXOLSStRHtaKqziQTQ3aK2Zflm50MYf2cLDddHTyN8ODatZG9wP4hDSAfZ659JwihWOI43KjRTyXyLJ9544OQmL7GlJoKVeUw39qrfSobZkDEb0SOrXqxUVgk5f6l-y7RuBVhyo9duFQRnSHPxlfFD8RhOyq_e7c_8KhbCPVgl2lMhM7efojtugV5x1AuLNKO9kkl1PMQtnzMPI8cwbvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZXjbPR2yRpG-tUDeLswb01tt6oiNDJnfD5hqZKUtpyngpY_ZC8gPqcsLt9YJkw9PEmvARW2DMm8IXKVYJrXTcmy8OQMA-xgKhVx9p9rsAHjCRJS6vmTIXEsJ5Ki3h7krpfBpMpInYl4ABwxylDSpTcoE37NHzsiqz-nc48-1LIW9y4GgNXeGHVNbtLkkG64HpwI9AaB0aCW0bATJoE-fKA4PeYO0TfWv5CU6swPiYBbmae0-FGj_R1yiRflsBhr5KkvTE6pXA-TF5cx16jbTRkUL5ONgJsWX382EAULgi2LbxE3l3iYCwWkNzsnk2u5VW5G8HFEaPtyDq2C87PyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=VOiYqNSrwZRgGqsgOgk1S1tLXsYVbnx_Yls_ZIbAg-moC-RDmIZ8goB7H19OPCkvvkpaVjaXa4YgJdVpZKNovm31fQXORjKZyMiwPvARHRrqojUSWosUpIvH9Kdmhbk76HRaSOLCXKdS2K--fFL8SlZk0zydL1vC6dYRaFNqx7wkKL-mSqQ9ARh_6djwF1Nc58a3fKMeo__stUcAg7DwttoY0PT_aH_LidrLh2s9DnMvHSp-mkfw9E5qHQcaZqW-tVI5jDuJbOSfxQDndJSeLl6FPBVnwQ6sPGFCwWHqTBckwi05QHW1gAmlEgkaxS-GyNQvrIQ2UrUPuRJBH_KOeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=VOiYqNSrwZRgGqsgOgk1S1tLXsYVbnx_Yls_ZIbAg-moC-RDmIZ8goB7H19OPCkvvkpaVjaXa4YgJdVpZKNovm31fQXORjKZyMiwPvARHRrqojUSWosUpIvH9Kdmhbk76HRaSOLCXKdS2K--fFL8SlZk0zydL1vC6dYRaFNqx7wkKL-mSqQ9ARh_6djwF1Nc58a3fKMeo__stUcAg7DwttoY0PT_aH_LidrLh2s9DnMvHSp-mkfw9E5qHQcaZqW-tVI5jDuJbOSfxQDndJSeLl6FPBVnwQ6sPGFCwWHqTBckwi05QHW1gAmlEgkaxS-GyNQvrIQ2UrUPuRJBH_KOeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=bbgdHjxRH-90bqHnneR7d4l7q9ERKR4iel0RlvJVstebCjgSoQ_xGZGvSQPRT9ggksZ7WNT0A9shjtpY_z5Mii359BzKIk8SyPbA3HaR57UJTGlDLLPg8VUSKSgiW4o4eAsf9sBiMrzleDA9DUUz7Gjr31WIN6D3KJEYRKShPNuo4xH_gxiFaohVb0XA1ZaGl6zReK1Kgi6s0atE8cDJoni30w6xjUOC4wSihhg8wYKxhfrM9Y9Y50mZyP-1jwdJqm21OevyL0agcFmHfp7BaYykbP0t1yu58r0VuKwnO7wtBETWlBmHaM0Mp1jpRkYP2FK5brhFoSvWAMAo8QsgpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=bbgdHjxRH-90bqHnneR7d4l7q9ERKR4iel0RlvJVstebCjgSoQ_xGZGvSQPRT9ggksZ7WNT0A9shjtpY_z5Mii359BzKIk8SyPbA3HaR57UJTGlDLLPg8VUSKSgiW4o4eAsf9sBiMrzleDA9DUUz7Gjr31WIN6D3KJEYRKShPNuo4xH_gxiFaohVb0XA1ZaGl6zReK1Kgi6s0atE8cDJoni30w6xjUOC4wSihhg8wYKxhfrM9Y9Y50mZyP-1jwdJqm21OevyL0agcFmHfp7BaYykbP0t1yu58r0VuKwnO7wtBETWlBmHaM0Mp1jpRkYP2FK5brhFoSvWAMAo8QsgpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-B3w8QP29Ay5uBkAw4iVAn-uw3Lf46DzibjbGqJ1RqjERD-S_eTVU6SibkIMAwUJekJGUhEkKkFvOxQA_EJXjOdxscKOTmkE-3dyykthywCEj2t5GHkWw95qZ-KSvNM08f3FmhcuE29T_YgYPDj6f1c6MHPbIvt7ssKsX9WaH1N6eeX7yXyHtg0QL7M9NoizvuZ-1Fdi82lR6sSRkdvHiHvrNrBiLj39Dlz2rnl1DmDMDoL1QEAuriY7Ma19sFujP7oFahBaRcyXgsgztTGToT-mojXJZlXsH4XTfDQzgD1fUndKiJJncpIEgEDL98GzWy9MUuFqfa0rOWZyeSKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=obWvcKxaYwrZTyTuwWA8DTt04nT2GcnBXaBeMKz4oVO0mQDZuuMepw-Bpad8eGc8SSNUVxMlNWacZDwEmWRNBWypQ9whu1GncAMX3ORzov7GJE2F5GpRv3IuotFVF6G65iXhLhcW7pIBgHOEi82rAtEaCN_BFxC2XMne4BesMTnepi-F_hGPlV3s4ZHOxPbTKMB_YPmO77HpMFJST_iUYskNPuRiXE843BRVThy-LgEfO_g-l8atUiQn28QSRDE156YakjrowiGT3EsvZY2FCzv6j0fr0xLKeBJV4SYv0rAIQgLwgiqYeRPKs02ASmM6jII2_P4TC011S5Vtwe7p-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=obWvcKxaYwrZTyTuwWA8DTt04nT2GcnBXaBeMKz4oVO0mQDZuuMepw-Bpad8eGc8SSNUVxMlNWacZDwEmWRNBWypQ9whu1GncAMX3ORzov7GJE2F5GpRv3IuotFVF6G65iXhLhcW7pIBgHOEi82rAtEaCN_BFxC2XMne4BesMTnepi-F_hGPlV3s4ZHOxPbTKMB_YPmO77HpMFJST_iUYskNPuRiXE843BRVThy-LgEfO_g-l8atUiQn28QSRDE156YakjrowiGT3EsvZY2FCzv6j0fr0xLKeBJV4SYv0rAIQgLwgiqYeRPKs02ASmM6jII2_P4TC011S5Vtwe7p-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIsMLGM-gBdem_YPV1cKKangWhsSTiD8VVvbXzXJlnZ8WnGrTBDV-kIao8NVyc4vaLVuhcinAPompNYbKSGUqn0gMJL8fZXfrg1DzuFZGa2rl_WoiJQ_Hd6QP6eKezCr6jhmViRxro_Jxt6snIquI9sEgveKak5-ebeI9mkryCDX1F-_OUnesnsHW9gcLirwpNQE4rQqpPGGyL9r9gKP6hMi3souwM0PtSJFlq2cRlyiTKE256pC2k5cz0iXXqaKPGYovuawrbwE49rrMlpe6sDOii9vsov-H5nKdrIR1LVkJDEseHJWu-8gVP2-m8wQWwxLb3zfpkBASgGMqDsbNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=NL_ONPnypzMDkz1Rxd2Np2io07y9u49UNjzdLeUvAJHLv3CRPK-fwIFpFrJmcxzg4JD2gowHP_yRysFG1-GMxVe5dIaO3obV4ttZ4sjtzSLWLLmCxCkYhUJ1KiGXpd_teFLR792NRXvnY9wo6k-9hkM9Rf5t44nAYt9iiSD_yUJaZJibE4LWFNRjVuFEFIVjZ0MRZV4UvNl4KWCshjJLzNUAagi0cC_TeH4Ei1z9c-6FGqoOVgxj5T2X4x7SW2U_liijVLTsHjek7eUzCAFyqDbbNrUjKauWHfl7SwNYtppG0M2zrJh-vE004pp9ON2v-Ch3HpQFxQ8FPBkTV5UrdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=NL_ONPnypzMDkz1Rxd2Np2io07y9u49UNjzdLeUvAJHLv3CRPK-fwIFpFrJmcxzg4JD2gowHP_yRysFG1-GMxVe5dIaO3obV4ttZ4sjtzSLWLLmCxCkYhUJ1KiGXpd_teFLR792NRXvnY9wo6k-9hkM9Rf5t44nAYt9iiSD_yUJaZJibE4LWFNRjVuFEFIVjZ0MRZV4UvNl4KWCshjJLzNUAagi0cC_TeH4Ei1z9c-6FGqoOVgxj5T2X4x7SW2U_liijVLTsHjek7eUzCAFyqDbbNrUjKauWHfl7SwNYtppG0M2zrJh-vE004pp9ON2v-Ch3HpQFxQ8FPBkTV5UrdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBxU8vswmAyxp5ITIZVc4fb2FWO4RMJJ4fVjewxWxXMpSzzF6l8idciaA_w8Zm-hHrIlfrUIq0jCZB-gzf7fFnX72_a7X40ITuNcM2Wjt64UHeSyGJpr73NjfjiD7SbjJpXvgyVfRiPsey43BPLu8THskDvxPKM26cz778GY8kdaTZm4lkq77DxSTXRzZRaZ3ONdWewDjvjMXYJ-z2NNplJze_13rd8ld9H1I1smR1daMfIBANgqisqb-K9TB8lBSCWRs97yGmfoMwQ7zgIypOcuZlklSKychq-JoJuVFICTAVFIqz_jq-hcPc4CDrQEFSnnNWv9yuuRroYWrzdlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری؛سپاه پاسداران:   تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70823" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛سپاه پاسداران:
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70822" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INFOo-MzkZduGKVcaRCyQPGdngScz9ccGFGjMHo3QXF402KY0RRHLr_v_WLeicSaelGmIqaC9RMdd6iHHRfgtJRny2JTcoQqs2jct8hAYytstaIM-IW56h8vTYePIogsQ3nOWobuYX1BaoP-VaMaIdtFjLzfns_Lba8sjkOXdjgJ7Ec6k0DknPXIatDPtFa2Fuk6DRSk0ERN0esi0UuDpttka9YxaBH4sIdHyTEfsKBZo93IRv7GwuzstA7Ab1h0tZCgKQrC-eBnvStPiQxtsEHb_G4CkpBCZ2_enM1qRTLNoEQu-xK7WVQAZbfeTOxVlvGSIiMJL-UUo3NP48Jpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d778b593.mp4?token=ZbiwHKZiCfzPbEBx6aI8AyPS3fFvtu2k7XI2rTb4Aoo1Lnq5n5-YTuBu9masdOUcq0J-5rDhXM83mXn-x6v8gUCcaF9ozMEvMtBaJUAg7ONYexi-ene3U0ibXTFadbticH--4Rj6TpOqPQrOMd1igltvIdg7F4xzOUpEolCpCYztGDDNIifm94emTk7hR5YhlYZ4x3it1Ad1M6FbwWzLwuNlQ-Mbmz3ZFU0qBx-_kFL9c-S_rWFnXv96CaUgipDcuXDN0OwohHuJUGyFaF_xMW0a8T0hN2pOdoL4dzouZHdRoxBoZZOeUX4Nfx8-qaDuFrLG3SHNuMDtwVP2hHhcNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d778b593.mp4?token=ZbiwHKZiCfzPbEBx6aI8AyPS3fFvtu2k7XI2rTb4Aoo1Lnq5n5-YTuBu9masdOUcq0J-5rDhXM83mXn-x6v8gUCcaF9ozMEvMtBaJUAg7ONYexi-ene3U0ibXTFadbticH--4Rj6TpOqPQrOMd1igltvIdg7F4xzOUpEolCpCYztGDDNIifm94emTk7hR5YhlYZ4x3it1Ad1M6FbwWzLwuNlQ-Mbmz3ZFU0qBx-_kFL9c-S_rWFnXv96CaUgipDcuXDN0OwohHuJUGyFaF_xMW0a8T0hN2pOdoL4dzouZHdRoxBoZZOeUX4Nfx8-qaDuFrLG3SHNuMDtwVP2hHhcNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه نمایشگاه عراقی اومده پژو پارس گذاشته برای فروش؛
و اما کامنت مردم همیشه در صحنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70820" target="_blank">📅 23:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
#فووری؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد  نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70819" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onzjeee3EXHNU7xWOy7WGvNUUoKjh8Wa6OWBm2ciAbea4C-D6u6rX1PSC782LiEnx1oGiwssgrZm9NGYRPLxEaOg2oeXgr9kKF4ce143xWzo8W0IQxXlDtCYka7qq6sZ5y9TeHWObK52QvUDASxhrH0fGeuYE8RMY8117X2WsRD9ceXOp8MRaMJA4V7NvPN5-1EMWfV1IrmdQ0aOrIFaugpUslldKSyTmbjpOrML6lqX-qIyyxBR7jsdgCNj6_qSbqkQNOKErlK8-6kc3PY6-CBbt56DxFpgWThS0BuwBPeLlRxDkTwxlThy2HwQZbK-FPEQyKAGXs_ygX-ACM2JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد
نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70818" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=v3CwoLvQwR88hNsGVvKBG4y8elZqpU7cFbKdsiX98oziAxKrID2FkSfJmUUTeQy3vF0Ovq6dmxlzoD7hO6lw2dWzTgycL2BuWj0GPAwMGnrbaAVDUWAzvDrw61cJonViesUCuRwAVGQz9n8EbBdaDgVE-hOxqNVY2Ks7gL7DA2PfCQ21_eZnDJ39wVSTXzF_gOqoebw9pb6UrT9kbcOnGWT7ILmm6exLX2uJC7oU1pWZ3NvoVTr0rbCDBvkEDM0QS2dR7P992770DwKvT53q3LeX0AJLAaTLHKVUtt3THl6qH0z5zD1cB-YX40P9BY-UpX7pymaZkOeqL7Hets7bEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=v3CwoLvQwR88hNsGVvKBG4y8elZqpU7cFbKdsiX98oziAxKrID2FkSfJmUUTeQy3vF0Ovq6dmxlzoD7hO6lw2dWzTgycL2BuWj0GPAwMGnrbaAVDUWAzvDrw61cJonViesUCuRwAVGQz9n8EbBdaDgVE-hOxqNVY2Ks7gL7DA2PfCQ21_eZnDJ39wVSTXzF_gOqoebw9pb6UrT9kbcOnGWT7ILmm6exLX2uJC7oU1pWZ3NvoVTr0rbCDBvkEDM0QS2dR7P992770DwKvT53q3LeX0AJLAaTLHKVUtt3THl6qH0z5zD1cB-YX40P9BY-UpX7pymaZkOeqL7Hets7bEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
محسن نامجو در کنسرت نیویورک، شانزده شهریور نود و دو
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70817" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=FJaNkutRmGQa6hnfvQS8Uw750NZEl5wn8zCGvIs2e7m1hpDyaZmaNcnY4c0EY3jnvD038EuRErgwQwS3FPvHC8PgbfFTTAGhLTmvx3K_jREY79PwBFZ5ycmDYMVWadF_fCjnppihTQzKyZfb23FO7BMxRy1er_PQ7B6K1mxGzEgNuYXuN1QZbXF8IrBePot49_V-JLusUjCoK9dw351Zrl0OUHNuAOGkOIv9AW0qZpUWj6NebI6tbaYls2oVzlkc-7N1BmpLhjs6VrR2Ls-LuCXPXTCYnh5AOlpn9buUn-ONZDSXp_A4_UewY5mHnFG1hgMOuXP96T0Z0VkJqjlB3rK7Blyy9Yw3VrYwUa25xdavFDi4-tVDPghzQsEiym1Gmid8nFKeSNu12MiYP14wr2ksM-5ZO7REWOlKzNu5SYRvrDq_Ql2JaZJkz_wYoBQRrhGyXWV1T5BFEul0nPsCLmCPHGnhye1Pn61lBUCWnUySaS4YOkYdraqsaRURv-Gs-55soaaWY3W9qTYqD1FHNoGUPWfX-QOx32B2Zor9pU6eGJ__YgY9pClKg6W8ktxy2CX1CO6I2y85fgtGyOcyeEQKC4yCm-mJYrc1AZNgVsrVxuggxlRelQfMnbKh5oIbEHhi8UAtA7sKrIuOl5CXuVTxIhzfLudS0S91pEwB8LY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=FJaNkutRmGQa6hnfvQS8Uw750NZEl5wn8zCGvIs2e7m1hpDyaZmaNcnY4c0EY3jnvD038EuRErgwQwS3FPvHC8PgbfFTTAGhLTmvx3K_jREY79PwBFZ5ycmDYMVWadF_fCjnppihTQzKyZfb23FO7BMxRy1er_PQ7B6K1mxGzEgNuYXuN1QZbXF8IrBePot49_V-JLusUjCoK9dw351Zrl0OUHNuAOGkOIv9AW0qZpUWj6NebI6tbaYls2oVzlkc-7N1BmpLhjs6VrR2Ls-LuCXPXTCYnh5AOlpn9buUn-ONZDSXp_A4_UewY5mHnFG1hgMOuXP96T0Z0VkJqjlB3rK7Blyy9Yw3VrYwUa25xdavFDi4-tVDPghzQsEiym1Gmid8nFKeSNu12MiYP14wr2ksM-5ZO7REWOlKzNu5SYRvrDq_Ql2JaZJkz_wYoBQRrhGyXWV1T5BFEul0nPsCLmCPHGnhye1Pn61lBUCWnUySaS4YOkYdraqsaRURv-Gs-55soaaWY3W9qTYqD1FHNoGUPWfX-QOx32B2Zor9pU6eGJ__YgY9pClKg6W8ktxy2CX1CO6I2y85fgtGyOcyeEQKC4yCm-mJYrc1AZNgVsrVxuggxlRelQfMnbKh5oIbEHhi8UAtA7sKrIuOl5CXuVTxIhzfLudS0S91pEwB8LY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70816" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70813">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u6iawc6rFqmz26vBLTQ1dYWoW1hsGmw1gnLdN5mnBMvh5_6QTi0YqT6xpgQycbxWAHK6nCaCxwePCDZfja-0KB51joyar76ooPJ9zSnsBmghdXEnQWXE5wVsIRlp6nUwaL0TTASKDJ6tuyvqioQ2anYHYiA2dV5Nc-cBLTKIhdw2orxRey_UnY4dLHTSbMWI3rBWfMkhlckaDFFMP8HkvFFJjL696SYiynlyWwGJVUsiOL2kfn2AM9L0ptaovi7sA8BryjcNfxG9zizqp0LRF0VQzCydzgLlRGZ_jQN7El4Tltol48m96AEqKCY-0KaNibk4wNTUc6pq60C34T7cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LWY6HGWqkRrdAG3hAE4cWuw1bG2j05J_w9pVaG_jAOGdUh0XYI6i5qFwSAx4Pr1bC2EAs1NH-IVK_Uf1_kA1yW21PYcXP6bmJBOqiAJSG7YRGbBkaLv6H6eyOI215JqF3YD-4MSX4C7HNmVMxoGeObyQ4Gn3VMq1vPWPfs3RDl1PUFT198bt_QJ2ykPWxKpZlj03GkNtLUYafdbo8IkuRQZdtlpKFaDNCDlL2HdUdt-yBILzbP6yn5bipdnCR5BRSBSS2YKh_yEGUyTN34DlFLeiT5k0-LeQpwDqu2iH_Nc6ULnEUBktcEAQ0LzhOVaM7WYYZVkg0E5Gbl8Y82PP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dF-Kr31O_K3q0zPsSTJASZ-U8s0zllnvCL5e48aRjzMlXIGe-la7611qEzSo7JnEp0vDyWqk9M_pcOO5nysLFj-OMVnZz9mkLbDw7A75SkF7M0Y5RcYFI8p0HJiYWmFq1n8lKVBCE0E6x4NVpRuDJf8lMXw1FuZ3v7XkRrp0qq2DN6nn12CWCfxxNzaUVhTDxRbLsAXCt24YfudQtsLePO1MvS7wd9aTjYvj05fvSXNfkqhJ4IZKC5oEYIa_XhylWsEK1FtLgSVZk1CmJTCfAMIWcqgdbG2_VvMdr0idWxjYcm1Pz-fdUoinfRy61n3LEH7buFHKhffKpEmKIm8XeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
از کیوت‌ترین عروسک ایران به اسم:
کون‌کش، رونمایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70813" target="_blank">📅 21:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70812">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=Cj1LcnOLlcBVbVxTwwNKiLiApKL2LSgDVtK3QWUawv51z2_8WAULzvWXBXUv5COb-Hpdh6UveWHM4mfUCR6HEOUwOtRFK5LJ6QzzvCgqbt8_Ys_WHYJQ2hspN5XeIwUmavEbf56NDSMCJEwR6EXLDxpolwyYGAts0YLCb0LZiiyQtbV7Tm-i_5OGxQdS71euMS61G3deruDo_BKhTEru-5xNvtWomUE2O3lUFAvXVET4x5bbLcVqExjg1943T1of2_HzoLl8HN8dYj31MzyAnL7BCABE4ZLZVtHDv2vah8VUvOIro4mOSp2qIzyBd6ur18LMdSfzJtJVidklMFZd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=Cj1LcnOLlcBVbVxTwwNKiLiApKL2LSgDVtK3QWUawv51z2_8WAULzvWXBXUv5COb-Hpdh6UveWHM4mfUCR6HEOUwOtRFK5LJ6QzzvCgqbt8_Ys_WHYJQ2hspN5XeIwUmavEbf56NDSMCJEwR6EXLDxpolwyYGAts0YLCb0LZiiyQtbV7Tm-i_5OGxQdS71euMS61G3deruDo_BKhTEru-5xNvtWomUE2O3lUFAvXVET4x5bbLcVqExjg1943T1of2_HzoLl8HN8dYj31MzyAnL7BCABE4ZLZVtHDv2vah8VUvOIro4mOSp2qIzyBd6ur18LMdSfzJtJVidklMFZd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر برا مراجعه کنندش تزریق لب انجام داده و از شدت ریدمان، خودشم نتونست جلوی خندشو بگیره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70812" target="_blank">📅 20:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70811">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo5caWynFcEunWpwvdvLX5YZIar5xFVZrqxFOy6qNJyiR8uVKZWRt36Lfy7EYgeaGDvVK9fe0ZmllC6gCXxCA1AqagiuxQN7FfApp1qu5O3G78gSgKvEcvGrdHXPxSa1t9lPCtd3ALzQuCHXyfAHkS8gLtauFiXzoYnx_GaaSB3R3WE6VqE_TsXxAgn4JUfHJ3GFY-OwGyRj_LfNvfwWUHPFkCFeHKXtDQd0Wnpy9OdTBpwv3JIhdKaz2n5G9KqRt0NAYChlqc80IInqO1LZ4LTnG7RmL8PyT5YLXPli_oRi4EK0nqcPUg0WNBuTE1g8uxvt4KsbUf5U58zW_HwVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
یک نفتکش هنگام عبور از تنگه هرمز در مسیری به سمت داخل (شمال)، در موقعیتی تقریباً ۱۲ مایل دریایی در شمال «خصب» عمان، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
این حادثه هیچ‌گونه تلفات جانی یا پیامدهای زیست‌محیطی در پی نداشته است.
موقعیت مکانی حمله نشان می‌دهد که این شناور هنگام استفاده از مسیر کشتیرانی تعیین‌شده توسط ایالات متحده در آب‌های عمان، هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70811" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtek9eIRkxBOxFQYop5IvI0Z_cxbEFfPPu0HzuUS4WkigxnplG70m9JCe-k-j98rExESOq6vnl22RSCZCq8QerxVD5ruZJCvtLQFFQSbmVOPoEcdjggf9EIiSpDQU7dsvuB-NI2R0FrcatOzxKdUmlT9YcqMAE2CAk0mkkU0P16kYGar1huJmyr13hDWTsIf0DidwZvcTf6bpWcnMHb01KBWEyXN3ACyK9BBxylcY0640u84Xk_-xr8XE_EyS2BSyt2lVQyJ0AvwUn3I-PaatHZ4IrkCjkaWw9JqiLYzGzhDGif3dtqqehdQxKeO6X6-jTm0SEuXx69oJvGBs_qgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ برای اینکه لج کانادایی‌ها رو دربیاره، اسم دریاچه کانادا(Lake Ontario) رو گذاشت «دریاچه آمریکا»؛
کانادایی‌ها هم کم نیاوردن و از لج ترامپ اسم دریاچه رو گذاشتن «دریاچه هرمز» و تاجایی که میتونستن این موضوع رو تو فضای مجازی وایرال کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70810" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=rU0W4gJAn9Qr9PTl9ZtZzEr5Y6hnnXNnXLi3BcNupF75oKIH_pfByjyij24aqoL4j8Ce5NNDpjhcbW1cohtih8jhMmebNjJTpC4qaoWOn-8ahWSMaIdTcL8SuGyUBgwC_Sz7rG5i3Y21EIqhbnByW6-IwO09Yy4yMl7uNx9J1hGqZlQLA0dVdIJC-v9eGUcjhpX8FcZKpfmhTQN7ShunuhLLpyn6qclpDbFPD6OE4t_0zwdw-6hoT_e24BrIN80hEleXviNiF1x8_7QmngK86t0H4LOTHH1_yWlwHY4K-T35qMdbD9ybcjZBRucdlMlN3v01jF6xkd5LLWNecTzPPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=rU0W4gJAn9Qr9PTl9ZtZzEr5Y6hnnXNnXLi3BcNupF75oKIH_pfByjyij24aqoL4j8Ce5NNDpjhcbW1cohtih8jhMmebNjJTpC4qaoWOn-8ahWSMaIdTcL8SuGyUBgwC_Sz7rG5i3Y21EIqhbnByW6-IwO09Yy4yMl7uNx9J1hGqZlQLA0dVdIJC-v9eGUcjhpX8FcZKpfmhTQN7ShunuhLLpyn6qclpDbFPD6OE4t_0zwdw-6hoT_e24BrIN80hEleXviNiF1x8_7QmngK86t0H4LOTHH1_yWlwHY4K-T35qMdbD9ybcjZBRucdlMlN3v01jF6xkd5LLWNecTzPPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حمله پزشکیان به صداوسیما:
مسعود پزشکیان، رئیس‌جمهور ایران، از سازمان صداوسیما به دلیل سانسور خود و سایر حامیان تفاهم‌نامه با آمریکا انتقاد کرد و این نهاد را به اتخاذ رویکردی افراطی متهم ساخت.
پزشکیان خطاب به جبلی رئیس صداوسیما: «این روزها دیگر اصلاً تلویزیون آن‌ها را تماشا نمی‌کنم. آن‌ها مایه وحدت نیستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70809" target="_blank">📅 18:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b978362a.mp4?token=LSHvmBUrNwBA-xPBYFzVzT_-Ws1If_F5BsmyI61i301rMJDju8-g9Wk92TNPk8XOaJA0sm8qM-FaGyEva-QWxdGF6HyUFzUCsrG21oPiQzLnEgWvRKZ05yuftJYSD1nTnXmwUMB1woWQXSUzp5gxplgYq0gWD0EdltwVFHqod-ozfyCFy4FmY9qLS7ryxNgpqTsL0RPfp58LKXm3OdmdTrn9zr7JCzQMFjc9-ab-4E8h_a1ARfA-OylmFKL0eWufwz6Eak3N5nsjmPTnf8442eLuSPiykro3HyPY37OOm09zzdz3hyvdR4aayOYh9kc3op1QizwyS543cRMvONbkMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b978362a.mp4?token=LSHvmBUrNwBA-xPBYFzVzT_-Ws1If_F5BsmyI61i301rMJDju8-g9Wk92TNPk8XOaJA0sm8qM-FaGyEva-QWxdGF6HyUFzUCsrG21oPiQzLnEgWvRKZ05yuftJYSD1nTnXmwUMB1woWQXSUzp5gxplgYq0gWD0EdltwVFHqod-ozfyCFy4FmY9qLS7ryxNgpqTsL0RPfp58LKXm3OdmdTrn9zr7JCzQMFjc9-ab-4E8h_a1ARfA-OylmFKL0eWufwz6Eak3N5nsjmPTnf8442eLuSPiykro3HyPY37OOm09zzdz3hyvdR4aayOYh9kc3op1QizwyS543cRMvONbkMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:  ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود. امروز همان پوشک ۸۶۵ هزار تومان است. باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70808" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjxuWYrJEiOsULvNHmuIUZ0SEQkwjViY4c4S7NM_J3KfiTfRocX2BwJwhZhqOReDVBU4pf4nW_lVhCuO2tzs5w1CVIRmihW2z3UPFAARIF30aeInvz8obzQdV88i_I8l1JIBPSciUNVXZBbWkD8qWnENr_qYBYcfafQDCV6N_eeaY3smEX9l7jMzeajbd0PgQTpvUxTL4pnN0Oyv8qM4eY12xR7k5UE2A-CdIwBeNysOLkvDpCdw63Uwu6aINkUsu6N1OgYQ_0uRCa612X_rp4uyAliQlPuIhoQrErbDXZzeOEQaxH_t5IfpTxf1X_GHJM_oGeedQm6T5W_OSm9QcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70807" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اوپراتور های حروم‌خور ایرانی مشخصه رو بسته های اینترنتی ضریب می‌ذارن، من صبح یه ۴ گیگ هفته‌ای گرفتم الان تموم شد، آخه چطور ممکنه فقط چن ساعت اینستا بودم
😐
از سال ۲۰۱۳ تو اینستا بودم قدیما با مودم یدونه ۳ گیگ می‌خریدیم تا یماه می‌رفت، شما دیگه مرز های وقاحت و خارکصگی رو جابجا کردین خدایی
#hjAly‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70806" target="_blank">📅 18:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70804">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePiFSvOKepf4IQcyTO_gg3V9WqKaGBhnMq2GaF_V_PrmQNOwM9WIcalEbiURsVwZxdAb08Rpum00coxPPAMbOt6RSouvpBP01n6JNbrA2Qfv5kima_yHCEBXrbjfjTG-mYEmvmrC47DvmkZnAdH4lFW62QKo02goowADGVR5gCwubte-p14Mj3j3vL3DSDBmdV2gehR0RyOV_x0zLLAfem3ZFEgbCZ-PAgklVTPpTCDefoRuTNu9C620kyFO5Nzf17dLc4cEBeLRJ3gCmmJLLgK9yitsm3IKpwqkSTO3GG7aN3JtDes3uZ0viKPiSlu4_Y8ay5rg6Hkk8OYL2fP1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8RQ_LpDTOk5-zGj9L5ZOi_xH4d8jyL-Ut0eloejeNC6iH3IOFffjARXvK5iuAm9wpUT_UZ6DntQRGg7eqYvIXPKlQQW35x4LZ5WmVlbfjxslNrktEMlWpcp8arhTGekODRFl5Nq2F1p86ViJtsHO-aYmsH98VkZs5oG_2Iah8CTpXsz6LCwPsCAj2w9lgUmmtNGa8gOu3pQ3b67rn9rrVG7R8NQ_PY7EfPtQ4kYvdLXWrLpe-1wRFZoLazMzWrvbvhONAkDzyBFN7OPhsR93R3GbPfUTcKzDoyUDOV-w40UuShchY5dj_fSRbVMDP2i7QhZuTdvY3IYCOdBX0kIoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصاویر جدید مادورو در زندان های آمریکا که گویا در اونجا از ایرانیا خوشحال تره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70804" target="_blank">📅 17:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70803">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=YJNGbJjGg0tIdBBbmjUL2i5t8Un7q8U91COyMjZCso22g76XUzVZsSTuHJNkwDNjd-miZi8mtBXb8m092qGgBeecHR7AXZD5M-_k_7W_1g9edwOERsofHxlR9a_KQKRHp2QfFcb39TqaGoNhAjxu0Zb2QpINQH4tOmWjadrRvJIlKbQFnWTNpZ1m3zx0qc8dXrLC8uZdhvv2955vXh8Q9_LpWsGlwW2gHAePHjeXG423AskRhnye7disG0xXuXUqVPpz9dhsU3wneGzTkoFGVLQcjx61RQkpu8TsSk3uc7bfZG4yybluby5FKwfbevBOaWNjGXszf60ECAzxAHhHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc84ead5.mp4?token=YJNGbJjGg0tIdBBbmjUL2i5t8Un7q8U91COyMjZCso22g76XUzVZsSTuHJNkwDNjd-miZi8mtBXb8m092qGgBeecHR7AXZD5M-_k_7W_1g9edwOERsofHxlR9a_KQKRHp2QfFcb39TqaGoNhAjxu0Zb2QpINQH4tOmWjadrRvJIlKbQFnWTNpZ1m3zx0qc8dXrLC8uZdhvv2955vXh8Q9_LpWsGlwW2gHAePHjeXG423AskRhnye7disG0xXuXUqVPpz9dhsU3wneGzTkoFGVLQcjx61RQkpu8TsSk3uc7bfZG4yybluby5FKwfbevBOaWNjGXszf60ECAzxAHhHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حرفای وایرال شده رحمان و رحیم پایتخت درباره ازدواج :
ازدواج نباید دوقلو باشن چون ممکنه این وسط اشتباه بگیریم اونارو
آقا کاره دیگه یهو دیدی در رفت دیگه نشد جمع بکنی
سارا و نیکا هم خب اون زمان تازه بچه بودن کلا نمیشد
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70803" target="_blank">📅 17:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70802">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Tmm1XQB6JUKK33MEUHL_jQY4FJmt6ipfNaUi9cFPTfdCjVQSwmtIrfn_WTlAHVOXgISgV6AEPAsvxNDbJKRLRMu2wGkir9TP8P6AFr_sxkOToB1YyEmYJpiEtRJjzrhZZ0PTN3K_gt1J9it6uzObuLsBx9I3EfwFYbeRaShHUUU-XrnKyJP319OBoPec6E-ZEEnTm8uyQWIyKNNtW2geUpsOlRtylbGq_36Uib27-mP0XOzM-LAW33c7nte2S2VKpkzCigmHgGnML9HzNpRJpiKqsken7oZ_-bn_-yadqpVDECeIvLap9B30VgeWpbsLTWdc6LPrMtk11tMRQHH9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5696dbdc.mp4?token=Tmm1XQB6JUKK33MEUHL_jQY4FJmt6ipfNaUi9cFPTfdCjVQSwmtIrfn_WTlAHVOXgISgV6AEPAsvxNDbJKRLRMu2wGkir9TP8P6AFr_sxkOToB1YyEmYJpiEtRJjzrhZZ0PTN3K_gt1J9it6uzObuLsBx9I3EfwFYbeRaShHUUU-XrnKyJP319OBoPec6E-ZEEnTm8uyQWIyKNNtW2geUpsOlRtylbGq_36Uib27-mP0XOzM-LAW33c7nte2S2VKpkzCigmHgGnML9HzNpRJpiKqsken7oZ_-bn_-yadqpVDECeIvLap9B30VgeWpbsLTWdc6LPrMtk11tMRQHH9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صادق الحسینی کارشناس اقتصاد :
کیفیت بنزین رو جوری پایین آوردن که تا ۳ ماه آینده تعداد زیادی از خودروها قراره تعمیرگاه صف بکشن و موتور تعمیر کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70802" target="_blank">📅 17:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70801">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=mJE1Q_VBkgSE8LmvLTpifMEZFw9-CGUC3wrC4mO_uDYtgN1KbttDahUyiz9hEa-mkCl-gIbNetM7JeYbTwoSg7Y5o4DIp9GKS4bqY7FynGQF6kHs48-wYuVGi2absq5Vt-vd2ChdQs9WHEUv47ztXgjSe9ZiQO7qPV_au_WnmBEyXI08qICTeo__CpChoeOI4NAdYS5rTpLYhbiQeoJjMlI9GBDxmeW3JUshAZT7UpPIBOgk7MHTdCujo0U7dCF58p8xwRzM7bFOGFmy7UhMrf0SWCySavmSrcFFlPmZDMnptBgAU806vED9z6_pOWJgC9r9W2jp7lPRMGb_NmDWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1befe3460.mp4?token=mJE1Q_VBkgSE8LmvLTpifMEZFw9-CGUC3wrC4mO_uDYtgN1KbttDahUyiz9hEa-mkCl-gIbNetM7JeYbTwoSg7Y5o4DIp9GKS4bqY7FynGQF6kHs48-wYuVGi2absq5Vt-vd2ChdQs9WHEUv47ztXgjSe9ZiQO7qPV_au_WnmBEyXI08qICTeo__CpChoeOI4NAdYS5rTpLYhbiQeoJjMlI9GBDxmeW3JUshAZT7UpPIBOgk7MHTdCujo0U7dCF58p8xwRzM7bFOGFmy7UhMrf0SWCySavmSrcFFlPmZDMnptBgAU806vED9z6_pOWJgC9r9W2jp7lPRMGb_NmDWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
پایین کشیدن تصویر مجتبی خامنه‌ای در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70801" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70800">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=n23kQk9q8b5_p-ggS6RgBhlxRmM6tAvh1VWa9YNPAzWW-vl_JIF7N0n2M-g85-LJFUIL-KE20BbsBwvJ3IG3CikHG1eC6vFiH4Bn6lob7c_1LXCKVZgwGVgBeD59my0D4j03aIDdofFeUG-gtbrBLj8oB-HRychP6UP0NcRr_NHIcAK3yotIFEUOf03kzqGDjraOXQe4IRW0-1BbU6bC01n8NOrAuJgzwFGc6GsNvfAa2esMLyNJsaTpBFDaY1CBZusv1c0NqlrRNgofWkcGMfGoAg98HMY_m6joAF3kNC7f7x3Bj2cLx-Nu1WwlOUgVo_8st52Oato3ZvdueE53aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c5ff11496.mp4?token=n23kQk9q8b5_p-ggS6RgBhlxRmM6tAvh1VWa9YNPAzWW-vl_JIF7N0n2M-g85-LJFUIL-KE20BbsBwvJ3IG3CikHG1eC6vFiH4Bn6lob7c_1LXCKVZgwGVgBeD59my0D4j03aIDdofFeUG-gtbrBLj8oB-HRychP6UP0NcRr_NHIcAK3yotIFEUOf03kzqGDjraOXQe4IRW0-1BbU6bC01n8NOrAuJgzwFGc6GsNvfAa2esMLyNJsaTpBFDaY1CBZusv1c0NqlrRNgofWkcGMfGoAg98HMY_m6joAF3kNC7f7x3Bj2cLx-Nu1WwlOUgVo_8st52Oato3ZvdueE53aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دوربین مخفی و تلاش این خانم برای اینکه جلوی خفتگیر رو بگیره خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70800" target="_blank">📅 16:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70799">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=jnac81io6PCdICXbo_as17vFmG7XEIETduUzNOW0pdErUbGVj5i7vh7LG8n9iWgzwkEwbBgmR9QOQV-WuG2JVv47zaXbRBrtXVglen8mykozSO8VVwwUuh8Gcv-SWyfXisKnyffoocw0OPvyXojBuSUIMWWMp0LzZeJf5KvsgZH0yjhqc7AsjaHyfqbVm7JdPR6GSzIvmKt8HwyX0DyuM4_SN4NQHiyVrtG67SEYliYkdUbSLANgvfNT3BGaYrxxm8oQYs9TQ0wzXpeJmdaUbgpMFoOEtYUOx4sbJVNBr-swNPIk-ArgsbVmnU0me8scs66E4twTU7g24CjtivHYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdd874dd6.mp4?token=jnac81io6PCdICXbo_as17vFmG7XEIETduUzNOW0pdErUbGVj5i7vh7LG8n9iWgzwkEwbBgmR9QOQV-WuG2JVv47zaXbRBrtXVglen8mykozSO8VVwwUuh8Gcv-SWyfXisKnyffoocw0OPvyXojBuSUIMWWMp0LzZeJf5KvsgZH0yjhqc7AsjaHyfqbVm7JdPR6GSzIvmKt8HwyX0DyuM4_SN4NQHiyVrtG67SEYliYkdUbSLANgvfNT3BGaYrxxm8oQYs9TQ0wzXpeJmdaUbgpMFoOEtYUOx4sbJVNBr-swNPIk-ArgsbVmnU0me8scs66E4twTU7g24CjtivHYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره کسایی که میگن تحریم هیچ اثری نداره:
نمی‌دونم چی به اینا باید بگم فقط همین رو میگم که عقلم خوب چیزیه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70799" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70798">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=vpz5D95RO-T5_FIskplM5NH3F6j7KtZOkOuja69WBwKxXgN3t5fCM1Oe0mbzDhECa9EJ86tnhsR1FkWldM3bOVEVvuUxDmDe8H9O3Cy3CEN7Tphrzdz8ZBWR3b1nWtnu7X_Xif-Q8eLDARM11hNz1ToraP_c5EzXJ3SZVhVjOxB0Ut_XaqvOyIy1dbf_jae3UvwPwuAM-7qwN_1RBasJ2lw1b_iUvMjqoL66mjEIfYe8efDuXg_LPael5umKXsLG8rahWRTglJ2wenyNn_TdgzgQH_bqMBArl5nPSztvYK6PnlDr-VoLpLM65RQShwTmDN0TQrkDBcvasA1CESD4T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036dee7c15.mp4?token=vpz5D95RO-T5_FIskplM5NH3F6j7KtZOkOuja69WBwKxXgN3t5fCM1Oe0mbzDhECa9EJ86tnhsR1FkWldM3bOVEVvuUxDmDe8H9O3Cy3CEN7Tphrzdz8ZBWR3b1nWtnu7X_Xif-Q8eLDARM11hNz1ToraP_c5EzXJ3SZVhVjOxB0Ut_XaqvOyIy1dbf_jae3UvwPwuAM-7qwN_1RBasJ2lw1b_iUvMjqoL66mjEIfYe8efDuXg_LPael5umKXsLG8rahWRTglJ2wenyNn_TdgzgQH_bqMBArl5nPSztvYK6PnlDr-VoLpLM65RQShwTmDN0TQrkDBcvasA1CESD4T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنلاین شاپ های اینستاگرام برای ویو دست به هرکاری میزنن
مثلا این ویدیو با ترفند شیک باسن باعث شد میلیونی ویو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70798" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70797">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=g0IbxOH6PqfyiZYeEl6SUrV38Pl_Mlef2NtvtFcK0u5iiD7BAR20CVdBzKIR5DQf1_6mEasQaIBGmlAlxXuIe4Yn2JnOYKJ0afJs0UMxa7INysft0PNpPHND4znPiTrNx9ZKIUQhJL_TuCeuKbN4bF3LB4UJvahJDFPTB_eL53sg8c2c0Em9yF8OWZEZpY3VeeVN6gZ7g5cHkkEGOrtfMPE4zkfW8xhu0q2hWimwy5I1BcSlD7e7lAUpdQiXYjZVFCaROkFhZ7iii3CS_80Qo-eyF6VsbUINCquC9jvj0WOQnhnQf-a03TlgAL3SXwxmqaam6vrATkzl_jxVqgfvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0459b57f2.mp4?token=g0IbxOH6PqfyiZYeEl6SUrV38Pl_Mlef2NtvtFcK0u5iiD7BAR20CVdBzKIR5DQf1_6mEasQaIBGmlAlxXuIe4Yn2JnOYKJ0afJs0UMxa7INysft0PNpPHND4znPiTrNx9ZKIUQhJL_TuCeuKbN4bF3LB4UJvahJDFPTB_eL53sg8c2c0Em9yF8OWZEZpY3VeeVN6gZ7g5cHkkEGOrtfMPE4zkfW8xhu0q2hWimwy5I1BcSlD7e7lAUpdQiXYjZVFCaROkFhZ7iii3CS_80Qo-eyF6VsbUINCquC9jvj0WOQnhnQf-a03TlgAL3SXwxmqaam6vrATkzl_jxVqgfvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
آیفون 17 پرو از ارتفاع ۳۰ کیلومتری سقوط کرد و سالم موند!
آیفون 17 پرو رو با قاب محافظ
RhinoShield AirX
از یه بالن، از ارتفاع
۳۰ هزار و ۶۰۷ متری
زمین ول کردن!
باورکردنی نیست، ولی گوشی بعد از این سقوط وحشتناک
کاملاً سالم موند
و حتی یه آسیب جدی هم ندید.
🔥
🏆
این اتفاق توسط
گینس
به‌عنوان «بلندترین سقوط تلفن همراه درون قاب محافظ روی عوارض طبیعی زمین» ثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70797" target="_blank">📅 14:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70796">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6McSo-8PtZpHJ-A1ZtLIxRgL33Wlb1_4StXbKEkUA7WichndMnjvErctHwZUMGooWtFzkD0pNzlU3ABY6-c5jSJ3aSOuDdp7hF0Y30FqMkow2TI6HOlmEOzmo3zQ36an7ZGKm4O1MByAxlYLYCKBuE48gBKI5ngcehKGGBA5IQBU6Di_haEbUseig4vVakYpsHuIaIV4hzCPA7hX304eD5uLbd45Bv0qHzaS6RsmZvepxWAvgqm0d9bU9vD7EAKrW1x5bzNrW6U0kiaAL1EOVUpu_BWX0TRZ40Mp6dcLjOciXeTbSkpPuS_gdZ-Za_SE6ysTF6Kj5cJ5YkGcgHDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تصویر ماهواره‌ای از بقایای شناورهای غرق‌شدۀ جمهوری اسلامی:
تصویر ماهواره‌ای تازه،بقایای ناوچه‌های جماران،نقدی و بایندر را نشان می‌دهد که در حملات اخیر آمریکا طی جنگ ۴۰روزه غرق شدند.
در این تصویر همچنین بقایای احتمالی یک شناور کلاس دلوار و دو شناور گشتی کلاس هندیجان دیده می‌شود.
محوطۀ پیرامونی نیز آثار گستردۀ تخریب ناشی از حملات را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70796" target="_blank">📅 13:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70795">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=A7GHV02jMegy2nxhlbriD94zkDEiJgeDLSAETz80YyOpmpMalDBb8c0D_2BwREAym8hYtvL4ZochaNB0l_kOhTufJZjKxrz9e6hl3zWbVVQf2L7Q8yi0AiPmae1LLRmhXzd9_OwN1khTKRcMaJRijnGWABX6sf7UDVT6tATn2-0PGdTYFhR37zfdnsbhTHkOI61snrpyfL8EW_rVl2mSoeb1HCT9K-hm70vxMiY_p6z86gh_wcAQHbg39ePc9ly4GifSHl6C8_OJD6j2pQf1QXd2J3niv8mtLzDuWbW8o1FLeLcfFbF_q8ODB94D1EDe9CBaC6GhSVDxG4j2N1kpIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45caa5a649.mp4?token=A7GHV02jMegy2nxhlbriD94zkDEiJgeDLSAETz80YyOpmpMalDBb8c0D_2BwREAym8hYtvL4ZochaNB0l_kOhTufJZjKxrz9e6hl3zWbVVQf2L7Q8yi0AiPmae1LLRmhXzd9_OwN1khTKRcMaJRijnGWABX6sf7UDVT6tATn2-0PGdTYFhR37zfdnsbhTHkOI61snrpyfL8EW_rVl2mSoeb1HCT9K-hm70vxMiY_p6z86gh_wcAQHbg39ePc9ly4GifSHl6C8_OJD6j2pQf1QXd2J3niv8mtLzDuWbW8o1FLeLcfFbF_q8ODB94D1EDe9CBaC6GhSVDxG4j2N1kpIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
تاکر کارلسن، تحلیلگر آمریکایی:
در نشست‌های پنتاگون درباره نحوه واکنش به ایران، گزینه استفاده از سلاح‌های هسته‌ای تاکتیکی بررسی شده است.
روسیه، آمریکا و اسرائیل در حال بازنگری در دکترین‌های هسته‌ای خود هستند و آمریکا نیز این موضوع را بررسی می‌کند.
سلاح‌های هسته‌ای تاکتیکی با وجود قدرت انفجاری کمتر، همچنان تسلیحات هسته‌ای محسوب می‌شوند و استفاده از آنها علیه اهدافی در ایران در پنتاگون مورد بحث قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70795" target="_blank">📅 12:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70794">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=XQsDE4OOWMFb1YfMPOIp1C-sWSLsl3vCXZs0nIZbwk4D4B1VzsCcWRU7Oa2r96JODzCE1UHvvSYP-jAKvz0cd94RNfuXowDASSVVdcZjbEgACDPbIFXHyiU0JQPOiK8v0zObOEklvB7XCzQM_nU-xZrN5DYOL_ftWSfHJdc6p4TWQKRqLoAMq0sVqc3zXNN_BLYOKsYfrUtt8V4oA6Lg2-nN_nRsJabCGOLFZJslpOx-duE2VNWpn3KsvRWb6QSkiNKMvvwdVGTRIf7eN_4WdhzcMejoqdrIWbAPSnBIpVG6XoShNVaZdf8IlLjohhx1_MBEN1Z84PmOFQ4TRJw18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d50eba94.mp4?token=XQsDE4OOWMFb1YfMPOIp1C-sWSLsl3vCXZs0nIZbwk4D4B1VzsCcWRU7Oa2r96JODzCE1UHvvSYP-jAKvz0cd94RNfuXowDASSVVdcZjbEgACDPbIFXHyiU0JQPOiK8v0zObOEklvB7XCzQM_nU-xZrN5DYOL_ftWSfHJdc6p4TWQKRqLoAMq0sVqc3zXNN_BLYOKsYfrUtt8V4oA6Lg2-nN_nRsJabCGOLFZJslpOx-duE2VNWpn3KsvRWb6QSkiNKMvvwdVGTRIf7eN_4WdhzcMejoqdrIWbAPSnBIpVG6XoShNVaZdf8IlLjohhx1_MBEN1Z84PmOFQ4TRJw18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70794" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70793">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70793" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70793" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70792">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIjb2v405HS-AzlUEX7M3Pxx83KHUYiXyGPcY1l2pKlXW8S4UhrJqb3z5VMhkjuIS5hkpj1EQXD6T2nSk-MuXPH4KAhcXQO6ouMZPEiU87-HeE8yHig0rTZoA2HjgvRFT1xI8uQLDuvXKv5KK3OZL6UMnXLR-s58hd88e-q3kmpl0Q6iq6BngN1-WlqVIoN_LDFNKpE9kicz9ewQGLJg8b17GFSCfN3gzfnl-cWrJfOzfexySERfhzJKEBxCVjDke-cze1ek7kDMONc_qJpwf6LzPeZdPZiIQSa_CzjC3Ujh8BSBylMztLKawK6axIGTI3ZkZyLy3qeKjhcukOE5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70792" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70791">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=mvMrSL7pAiYqfDzyxhfuAAG2obs7aqrU8C23zT31klY7QRTKtR8wF07wY0ytMiUJOq4hnfpgU63kraOzIK-MlJaUeRJ9RLAzlfWEak3pGQ47ep4phVpHAgP5bE_b9tXQykmD6xM7q6M5AuRRD8oBcULLMmBB6fxD25qDFiVsGxrIqoMnKHnK2vG8m2jrO-VIxi2P42Xc1RwpBqErCYlKhU8JL-aKaEa052QaNPqfvy9bRdMk45dvuBupG7DwZin7f7uqv64ykW1Lt26MtIn41BtPPkaaSCicDRk3MyCRo_7YnFQbADVHjkWHg_IpVl66TFZV30EU4DJ34AwLz-suGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b95ccb0b.mp4?token=mvMrSL7pAiYqfDzyxhfuAAG2obs7aqrU8C23zT31klY7QRTKtR8wF07wY0ytMiUJOq4hnfpgU63kraOzIK-MlJaUeRJ9RLAzlfWEak3pGQ47ep4phVpHAgP5bE_b9tXQykmD6xM7q6M5AuRRD8oBcULLMmBB6fxD25qDFiVsGxrIqoMnKHnK2vG8m2jrO-VIxi2P42Xc1RwpBqErCYlKhU8JL-aKaEa052QaNPqfvy9bRdMk45dvuBupG7DwZin7f7uqv64ykW1Lt26MtIn41BtPPkaaSCicDRk3MyCRo_7YnFQbADVHjkWHg_IpVl66TFZV30EU4DJ34AwLz-suGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که کلینیک بیماری زنان داره تعریف میکنه که یه خانم 56 ساله بهش مراجعه کرده و گفته که همسر 67ساله‌ام از وقتی بازنشست شده، روزی چندبار باهام رابطه داره؛
قسمت عجیب ماجرا اینجاست که جدیدا یه فانتزی‌ای پیدا کرده که میگه سرت رو بکن تو ماشین لباسشویی تا از پشت باهات رابطه داشته باشم!!
الانم این خانم سوزش شدید پیدا کرده و مجبور شده موضوع رو به پسرش بگه تا اون بره باباش رو از خر شیطون بیاره پایین...
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70791" target="_blank">📅 12:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=Bw_NARW9pNde85uxA-3Qb2V9Sbb5ps6VF3F-Qpwt5_lEIImhhU5XwxChL0uuwMPJtIo_7l-xVNRDw9Hm5dQhwKhTvSwHDtW87n_x0Vp4NqLXXyRT5zFlV7kDzigoWEdFLU1HB1_CJFkk8eOGTL6SntRL-o6wn6sETOsH3WkRGeosBnNRRpeBeZHu5-6htugHK1mcdgDqKQpK-30qH_KLkvkHgD1RPBtOdfUzcPZzI2TzRJUWd5I5yM4u8dRcGIgS4cPev_e3vLZDpTMOVkDLmF8KH2Hs7Zw6oVvHyck4oUdxGQi5klShQJMJCdBoYSw6vY4qgjSyi-om7MlNy6ct-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bb7d34aa2.mp4?token=Bw_NARW9pNde85uxA-3Qb2V9Sbb5ps6VF3F-Qpwt5_lEIImhhU5XwxChL0uuwMPJtIo_7l-xVNRDw9Hm5dQhwKhTvSwHDtW87n_x0Vp4NqLXXyRT5zFlV7kDzigoWEdFLU1HB1_CJFkk8eOGTL6SntRL-o6wn6sETOsH3WkRGeosBnNRRpeBeZHu5-6htugHK1mcdgDqKQpK-30qH_KLkvkHgD1RPBtOdfUzcPZzI2TzRJUWd5I5yM4u8dRcGIgS4cPev_e3vLZDpTMOVkDLmF8KH2Hs7Zw6oVvHyck4oUdxGQi5klShQJMJCdBoYSw6vY4qgjSyi-om7MlNy6ct-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش توی باشگاه انقلاب تهران مسابقات و ایونت تنیس برگزار شد که حسابی سر و صدا کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70787" target="_blank">📅 11:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=QJqWAdT1oAc5eWjTthRjjbU87fFgbYKBvuJhFxKrmnRYpmqS2B7JmSkLuy2N4YlJ6LLs8z4ZIIJCbmq96qbY1Zy3cXkGmiERTyVlyDhZN1_hRDXEIOGgYG0GCh0Na02h8q7jt3oWo-wb-nu1fkGlxnWDhMkmIrjPTMbOHCWvRVNz6hY3UKgqvnxqCQZvrthr0SVaEq4Wt3lZWPPiHnSTri4ORTiJvrZusPHvsVleRMt-KVAcK2ilNiDpT_sbzBs-8T42m7pUKsixbkkl0wbK4ur4heOmoK6RAqj5A0XZ2s9CNqk8A4GF-xQmw1TP0sst2DsdkZ-xZwGZm3NabRLJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f98f823a9.mp4?token=QJqWAdT1oAc5eWjTthRjjbU87fFgbYKBvuJhFxKrmnRYpmqS2B7JmSkLuy2N4YlJ6LLs8z4ZIIJCbmq96qbY1Zy3cXkGmiERTyVlyDhZN1_hRDXEIOGgYG0GCh0Na02h8q7jt3oWo-wb-nu1fkGlxnWDhMkmIrjPTMbOHCWvRVNz6hY3UKgqvnxqCQZvrthr0SVaEq4Wt3lZWPPiHnSTri4ORTiJvrZusPHvsVleRMt-KVAcK2ilNiDpT_sbzBs-8T42m7pUKsixbkkl0wbK4ur4heOmoK6RAqj5A0XZ2s9CNqk8A4GF-xQmw1TP0sst2DsdkZ-xZwGZm3NabRLJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇳🇵
🇨🇳
ویدیو اختصاصی جدیدی که توسط نیویورک تایمز به دست آمده و تأیید شده است، واضح‌ترین تصویر از ریزش کوه لانگتانگ لیرونگ در ۲۶ آگوست را که باعث سیل فاجعه‌بار نپال-تبت شد، ارائه می‌دهد.
کوهنوردان قبل از اینکه یخ، سنگ و آوار به دره فرو بروند و ابری از گرد و غبار عظیم را به هوا بلند کنند، صدای ترک بزرگی را شنیدند.
فیلم دیگری، آوارهایی را که بلافاصله پس از ریزش به سمت پایین تپه حرکت می‌کنند، به تصویر می‌کشد - آغاز فاجعه‌ای که جوامع پایین‌دست را ویران خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70782" target="_blank">📅 11:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFSicMk4ut-aQQ0tvCS7tFmy0yZHy1Qk5Npk2xrbqokZiZjYtYq8rksAm_mEHrO_kIIbEmxq_E-9Fbk0LdjROqgmEbMiXgSjj_KTwLW6_JMd8NYbkjNT2ieW2hqwbKuWS8l6HAJZot3E_o1KONwyCjgZeUehiI0pss60UygINHvOS7CuFf26L5Nrd5QVLcVUhNSo_VJ_StrF9RFsP-av0zo870L9Epw-HzCX4UXpYPH8xLVSzk9RL8lAP0-uy8nDAvQpogrVCOrtAiOM7qxYtHYZfH7Or5dhpEsULAqRX-OWgGh1apwddwKG5pe5RUs59nn420bjnuw_Z4TgD822EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCL2wMIX3NyTXHItXz4G5qYHDTw6UjATcDqSNQXGquC3O-lbZykaL3yJzKnJcohbPKNDvMU1bYdcEzNBgx4KIzlg36LwEa7bh480CPEFklwffYqG0f34TxHaX8HvHhg_BHCwIV4o8mbpfLDcG0Fz8EJOLRMxaHn1kHrHsA49I1dcgc6c1yuPU-6z5KAQ-rORd6TY7WUL-VHP8P8Gl12r0W3XGCFR8mEfrk-LMQf1iKsCuhtf-atIyWPxEV2tIqvkfhJB-fyiOY3THa4ecmMr96LokyQupuC8jQWhnPFdQHXAI2sXe8pq2XCFkwEvUHfojb4S2JUEvr1Yhf0PjirW9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
استوری یوسف، پسر مسعود پزشکیان:
مسائل رو ناموسی نکنید که هیچکس نتونه درباره‌اش حرف بزنه!
اگه تو غنی‌سازی منفعت داریم، دنبال کنیم و اگه نداریم، متوقفش کنیم.
اگه تو داشتن توان موشکی و پهپادی منافع داریم، دنبال کنیم و اگه نداریم، دست برداریم.
اگه بریم سمت هسته‌ای، دیگه فقط آمریکا و اسرائیل نمیان سراغ‌مون و اونوقت یه اجماع جهانی علیه ایران شکل می‌گیره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70780" target="_blank">📅 10:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=BOPFxTu4-b4VQbi_Il8Syz8bAEIvI8t1SWfQtyw6wnLvEnG-EakqK5IQVjBYrJVbGIJWb7PA4SvEdwCr_l6YP7ZXju4eeGIODJcrer3ARV5cmQC0UEkVpEq5zaHE9vRF3V3iFIw3bw6UtExGIOup3PIHXqNmJpGX-Xp40bdFnCRrFLHqQufALyhj0aKyZjStm4uwBGPAzK6rZJ8x47hJxqMDqPyJLZyF5SLjOlQbIQoFsw_zRIDeIZ7YaKsxqgpVoXH6IGXEAPlYGAn8-v3yM8uNrh78GpQ8w6xhUSp3wrbUI_JlCwu540g1skfkdu73xVmyj6GmY9RvrZubxKA0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ffa3e78b.mp4?token=BOPFxTu4-b4VQbi_Il8Syz8bAEIvI8t1SWfQtyw6wnLvEnG-EakqK5IQVjBYrJVbGIJWb7PA4SvEdwCr_l6YP7ZXju4eeGIODJcrer3ARV5cmQC0UEkVpEq5zaHE9vRF3V3iFIw3bw6UtExGIOup3PIHXqNmJpGX-Xp40bdFnCRrFLHqQufALyhj0aKyZjStm4uwBGPAzK6rZJ8x47hJxqMDqPyJLZyF5SLjOlQbIQoFsw_zRIDeIZ7YaKsxqgpVoXH6IGXEAPlYGAn8-v3yM8uNrh78GpQ8w6xhUSp3wrbUI_JlCwu540g1skfkdu73xVmyj6GmY9RvrZubxKA0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت بندر شهید رجایی بندرعباس، بزرگترین و مهمترین بندر تجاری کشور بعد از محاصره دریایی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70779" target="_blank">📅 10:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=vudi89ZgRKt-svhNLP0-N8BYnhuklFtE5p0ihBQfhosC33L-Adk-bp6W2TgVhHpsUBHJ1XqhP1zZuB10ZB1hSK5dVqMBxoxhdpE3zdHwWSYGfnXLtMTNbasQ_bQWO7Xj4bloXmj8d-5dhV24uSAHilufcpzZ3CF7U-pfL0Dj4fkUf8SLkl1zG_CiT6uQNSBn8BQsZwg0GzDqqsDuas6y427qr7sXPTmPAizFrm0ZAHXtKqdBJIGCgmUFbFS3BA27ONLO-Lm1FnEUPrOTWXJX5yUl3RfppTBjYp3_X0oYFlRhRMJ2xx69Bl8unZY2HUDmdFjiRsFHWw3y-wvj4-iaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6d1be5bb.mp4?token=vudi89ZgRKt-svhNLP0-N8BYnhuklFtE5p0ihBQfhosC33L-Adk-bp6W2TgVhHpsUBHJ1XqhP1zZuB10ZB1hSK5dVqMBxoxhdpE3zdHwWSYGfnXLtMTNbasQ_bQWO7Xj4bloXmj8d-5dhV24uSAHilufcpzZ3CF7U-pfL0Dj4fkUf8SLkl1zG_CiT6uQNSBn8BQsZwg0GzDqqsDuas6y427qr7sXPTmPAizFrm0ZAHXtKqdBJIGCgmUFbFS3BA27ONLO-Lm1FnEUPrOTWXJX5yUl3RfppTBjYp3_X0oYFlRhRMJ2xx69Bl8unZY2HUDmdFjiRsFHWw3y-wvj4-iaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان بعد از بیانیه مجتبی خامنه‌ای که گفت ضعف های کشور رو علنی نگید
داره پرقدرت به حرفش عمل میکنه و اومده گفته:
صداوسیما هی‌‌ میگه‌ آمریکا تورمش ۲ درصد رفته بالا؛ خب‌ بابا مال ما ۱۰۰ درصد رفته بالا.
همه چیز به تحریم و واردات ربط داره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70778" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=cY41_W3F1jpDdpRPXBwnQNhxrjKrloPjfl3qR6VKSu_7He7tgjiGZu7ZydMzNUonGu8f-4T9gz0ZtO21P9osvEwzvDPQOioAuvCOpK2ouDumi1qgP_8yUZ7jsKI75J4LbZfQ1qq1njijVALID0qDZzthIEz6xDy906DpwRn4gD4CGRkw1pRU0LLv4GCubBf5YdhiZ6lBSVBrZD427gIsG-lCfqq5gmbOcFb7bjNAgTv9Wnku98D_7SOhGD6SYLzMlnNqhhGvFOq5KTVlt7mpUi5Pcxwob5EQ1isv7_-KIzlLpOXYPosGDrEzi2R19nDyP__FtL8P-fVbOgZdG4CKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5638aa725e.mp4?token=cY41_W3F1jpDdpRPXBwnQNhxrjKrloPjfl3qR6VKSu_7He7tgjiGZu7ZydMzNUonGu8f-4T9gz0ZtO21P9osvEwzvDPQOioAuvCOpK2ouDumi1qgP_8yUZ7jsKI75J4LbZfQ1qq1njijVALID0qDZzthIEz6xDy906DpwRn4gD4CGRkw1pRU0LLv4GCubBf5YdhiZ6lBSVBrZD427gIsG-lCfqq5gmbOcFb7bjNAgTv9Wnku98D_7SOhGD6SYLzMlnNqhhGvFOq5KTVlt7mpUi5Pcxwob5EQ1isv7_-KIzlLpOXYPosGDrEzi2R19nDyP__FtL8P-fVbOgZdG4CKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات اولیه حمله پشم ریزون آمریکا و اسراییل به انبارهای نفت تهران در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70777" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0awB9-PPA3heVIysbhQWSyiU7sQyJiczt8k7s-M__nPm7rOzCKxafez0deGqmobF8TKVs4T1JJEjJM_WRyuE3xmovd3sMsl9THQ90musCcNNidSiTnPafrrqqAAp8Yj6Xj0r8fNgb2nMipXSPs8r94lc-e_rOWXSK_b0jY7HhZA-6mTrub8h20DYuK5Hd8B6FJ3eqsXtWoVZHrmf0Nes6qcBYq5L6s8nNRG-rdai96xaV_JO8oZBDQ11b14s9E62gws-Q4MI_qGpSKQVyF5S0d7SsKPKbWK9lqbuCKzLl5lbPeG0xNwxtx6UH1lcrxXzUkURhKkh1lOsNAM3oqfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70776" target="_blank">📅 01:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26b389410.mp4?token=noP8c-aBhbTqfQtwtqBEYCU3F44VLJSBb_IzISQhzmdKTxiNeY7GDAZkRBRCeJE2fvA2WslnPNRYJAtFErxCj1DYmRhchhtp7cWgAT_iL6hQAMz7snqZsuODmvAxVmC_5DjDvyf902RUp4zpfAKS1195QXZq9rPggO5h1gi42s_Z0QsuGwQDOe3__5gw30BGryukNfNMGvpPI5DzwckSQKiptM8bHbuRtmBhWNOG4sg9eUOz5YYS-kR1FIxqAlVDU8aV4CaaZSYmgxiLb33kBeshsFOirbDSnvCuyNAF972ycpxGqkZXqcnVIgx3xumaOAr7R79FdfDGzaPNEh2P1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26b389410.mp4?token=noP8c-aBhbTqfQtwtqBEYCU3F44VLJSBb_IzISQhzmdKTxiNeY7GDAZkRBRCeJE2fvA2WslnPNRYJAtFErxCj1DYmRhchhtp7cWgAT_iL6hQAMz7snqZsuODmvAxVmC_5DjDvyf902RUp4zpfAKS1195QXZq9rPggO5h1gi42s_Z0QsuGwQDOe3__5gw30BGryukNfNMGvpPI5DzwckSQKiptM8bHbuRtmBhWNOG4sg9eUOz5YYS-kR1FIxqAlVDU8aV4CaaZSYmgxiLb33kBeshsFOirbDSnvCuyNAF972ycpxGqkZXqcnVIgx3xumaOAr7R79FdfDGzaPNEh2P1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپِ هوش مصنوعی، تابلوی «دریاچه انتاریو» را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس با آهنگ «YMCA» شروع به رقصیدن می‌کند
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70775" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fknaJGg5Al8G0c7d9_ny4au0NoW6hA6JwEylDyd5rVRMfRTTeis--NZ4A0LLdZRrjMS8ypUaLQCxyuPaMO9TwmDTbRTFhCy20s2itOO_rdwUPL6x9tJkr8ajbyuEaOMh7HbCxHioSnZ61rAnc53tgM9OaAK2l8pflzJRsr7FNFF_ZNHZK7fS1AEnLaESSNIhYjz7-BxFC5_I5cp-X0uEE3hBeXKDrWtFZm9ZD_Vhliyw9viHL4fNFfxs1yle9CYS6O8S2DlNwsuMWgz3P5xcvnc4cLPW1i7m1W4pLnilMt02us6kge6RVA7h7DvXz6WQ6QqBb_q1_ZTbyvMWSMZI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
باراک راوید:
دو مقام اسرائیلی می‌گویند که تصمیم به بستن تنگه هرمز توسط فرمانده وقت نیروی دریایی سپاه پاسداران انقلاب اسلامی، سردار علیرضا تنگسیری، اتخاذ شد.
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه را می‌بندد و هشدار داد که به نفت‌کش‌هایی که قصد عبور از آن را داشته باشند، حمله خواهد کرد.
اما به گفته مقامات اسرائیلی و آمریکایی، تنگسیری در پشت پرده دستوری صادر کرد که تنش را به‌شدت تشدید کرد: استقرار مین‌های دریایی در «طرح تفکیک ترافیک» (TSS) که مسیر اصلی کشتیرانی بین‌المللی در این تنگه محسوب می‌شود.
تنگسیری سه هفته بعد در جریان یک حمله هوایی اسرائیل در بندرعباس کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70774" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=TerZNyO6RCCk86lQTtdDrF_WeyDBp9IkZVI3z7hheFJGqCsmarERuK3QbPMzubSkyXLQizSjOBZZkbB6VzxB8zAV48H5EMn3SXqklaehHdhjDnV3wTGmaqI-n3IMBjDMujg_1TLJoCHTvvrQXL4RXVwSV50-Nd3yNu9bU5MyaiWtLLHwNJ36j9BtaQkYkzxGVenn9mpjr-GavaWCzHrZEv1VUTBUTPK_7heTMgnpNoX-wH1rltubxZQjwrRM5xH3erHYEFbXGNzLm2USO-LrjiUzQKrhxbpdofa89ICIwoqYLqP0AszCqhhGUNj-N4CMVoZ5jPGmBJ7Bu6pz-WIeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=TerZNyO6RCCk86lQTtdDrF_WeyDBp9IkZVI3z7hheFJGqCsmarERuK3QbPMzubSkyXLQizSjOBZZkbB6VzxB8zAV48H5EMn3SXqklaehHdhjDnV3wTGmaqI-n3IMBjDMujg_1TLJoCHTvvrQXL4RXVwSV50-Nd3yNu9bU5MyaiWtLLHwNJ36j9BtaQkYkzxGVenn9mpjr-GavaWCzHrZEv1VUTBUTPK_7heTMgnpNoX-wH1rltubxZQjwrRM5xH3erHYEFbXGNzLm2USO-LrjiUzQKrhxbpdofa89ICIwoqYLqP0AszCqhhGUNj-N4CMVoZ5jPGmBJ7Bu6pz-WIeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارتی شوگر مامی ها توی ولنجک تهران
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70773" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqS2nWKX13ySG8Goc00GzAgeXrr7_JQZ6CsMQ5pMaKvsY4O5cFQ_UNUfoq-oBKNx4CucPPpGJiJgfcI0JBLfGXDPHw_j8PsaAGT8do-3A1jEg-RHEzKtacVIZzcqHVKSRXGdarong7wIprSQO7_zR6cSjjGPa6RNIp2qJ5vKjk0NSoPRXkyeKcaeCNXSu7Q7YdCaCn1eRbxNCf6Iz-CRDYgWHacYaE2scJIKMymaYdOWNusfySsm4W1X7CBQF0booJIS9ubU2zZHcyJQT_dD4AHbz5zmPC6TtqzN8mSI5GH8tna8BH71jF_CMqSSYwfCWDn9Q9nvhrdOM4FbmuYexyp_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d44837a.mp4?token=I-qIIDuX97UUPiKOMgbXuP3XXPCe2EohFSQAUa4Ys98Z0ZXuvPJfEDWWZyXBIm7MoXqfqpawKnFS5MdRy4TE5C4BbfWr7XnFSlblxHShwuuj7wKtqbKcvIj14hBuI9Nad0uPKcEK-V2VVzaPLsdbGkTnbJgaXLh1N5z0lj3GyCBvujXZXzmPZ3JRcH5Bzx35NSitsvZBTHCmEvUNUA_9VLBhU3avj93SvXnVSj-FAl8xDIRFqruDqdAnFN_wjfWHjALoo9NCE6lh_hsOyob3KZ0dD7Iu15kDAOGi6D9GWNVi3BDE9jSAk9-YXNp56ZIcySAzBtgjnqzS_Yy8-YwqS2nWKX13ySG8Goc00GzAgeXrr7_JQZ6CsMQ5pMaKvsY4O5cFQ_UNUfoq-oBKNx4CucPPpGJiJgfcI0JBLfGXDPHw_j8PsaAGT8do-3A1jEg-RHEzKtacVIZzcqHVKSRXGdarong7wIprSQO7_zR6cSjjGPa6RNIp2qJ5vKjk0NSoPRXkyeKcaeCNXSu7Q7YdCaCn1eRbxNCf6Iz-CRDYgWHacYaE2scJIKMymaYdOWNusfySsm4W1X7CBQF0booJIS9ubU2zZHcyJQT_dD4AHbz5zmPC6TtqzN8mSI5GH8tna8BH71jF_CMqSSYwfCWDn9Q9nvhrdOM4FbmuYexyp_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصویری که صداوسیما و رسانه های داخلی از آمریکا نشون میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70772" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=TFDEbcvXoTpBJ_Dnc02Cn0lYw-q_kYtTG83acDeTw-aCmf3WzSd_aHyAK7ybU6Q--yMB6VvpiJjrcQPOwGJ30glkQpR9YPT_zeI06aDAVaa3v5orY0aP0XUoGBVgKvufa5c67SUafFNkpA_HygbSFkZZHw0uk2vsLNclnOH-aujTBvkcPjWMKCHh2-eyxrVfsTjiftMVvQbxGDolp_P3Smp5AQT4MPNuJf3CLQx_kkkpZTYwfPkd8of1__YdMs2HtwkBrbzycwXDFyIp6r-WK_3gxgkcT_2oyeyUkt3xViiN9J1XignnSrTSZDt1jolLTD_pe0Rty5Sg-KYI9azswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=TFDEbcvXoTpBJ_Dnc02Cn0lYw-q_kYtTG83acDeTw-aCmf3WzSd_aHyAK7ybU6Q--yMB6VvpiJjrcQPOwGJ30glkQpR9YPT_zeI06aDAVaa3v5orY0aP0XUoGBVgKvufa5c67SUafFNkpA_HygbSFkZZHw0uk2vsLNclnOH-aujTBvkcPjWMKCHh2-eyxrVfsTjiftMVvQbxGDolp_P3Smp5AQT4MPNuJf3CLQx_kkkpZTYwfPkd8of1__YdMs2HtwkBrbzycwXDFyIp6r-WK_3gxgkcT_2oyeyUkt3xViiN9J1XignnSrTSZDt1jolLTD_pe0Rty5Sg-KYI9azswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
«میزان، رأی ملت است»؛ اما ظاهراً نه همیشه!
🎙
روح‌الله خمینی در سال ۱۳۵۸:
«میزان، رأی ملت است» و حتی اگر اکثریت مردم اشتباه کنند، باید به رأی آنان احترام گذاشت.
اما چندی بعد، در سال ۱۳۶۰:
«میزان، آرای ملت است»؛ «البته مسائل اگر مسائل اسلامی باشد، اگر در رای هم مخالف باشید، باید تو سرتان زد!»
🇮🇷
🎙
سال ها بعد علی خامنه‌ای در پاسخ به پیشنهاد رفراندوم در ایران گفت:
«این چه حرف بی‌خودی است؟ مگر همه مردم قدرت تحلیل مسائل سیاسی را دارند؟»
⁉️
اما همین رفراندوم را برای فلسطین و دیگر کشورها تجویز می‌کند تا خواست مردم مشخص شود!
پس چگونه است که مردم دیگر کشورها قدرت تحلیل مسائل سیاسی دارند، اما مردم ایران ندارند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70771" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=g4-KMRt7yUuiaxcQuOgb3ddnufCjkGX2OMrfSM7jvPwrNueMPUhs3GftyX7rXEnx9qXofLBEls19pKyWBg4l0gKm-ck_s4VOy8hjhT7lMB50kIw7oH2aJZ-A3CnngEqb5mPxTcOdCkpKV_Exr3WSe07wsTwS8ijBYJHp1MazQ6qHXUFFgwx9DFfTf9H4EQw542hWbllg0iFGZpI2GsuvKQTMe_3SE5w-z4py5a39Drggv24ObIOMjooNA_7O3COdh4XPqv51V_iWPNk-gm32cnteNBzLc4L2yEtkGhe8XAn61deXk2Mxw7A0oVwYtypQMxUQ9PRfjM80fqx0NSPCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=g4-KMRt7yUuiaxcQuOgb3ddnufCjkGX2OMrfSM7jvPwrNueMPUhs3GftyX7rXEnx9qXofLBEls19pKyWBg4l0gKm-ck_s4VOy8hjhT7lMB50kIw7oH2aJZ-A3CnngEqb5mPxTcOdCkpKV_Exr3WSe07wsTwS8ijBYJHp1MazQ6qHXUFFgwx9DFfTf9H4EQw542hWbllg0iFGZpI2GsuvKQTMe_3SE5w-z4py5a39Drggv24ObIOMjooNA_7O3COdh4XPqv51V_iWPNk-gm32cnteNBzLc4L2yEtkGhe8XAn61deXk2Mxw7A0oVwYtypQMxUQ9PRfjM80fqx0NSPCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر رفته دکتر و میگه وسواس شدید دارم و نمیتونم برم دستشویی چون چندشم میشه!
برای همین دستمال کاغذی برمیدارم، تو اتاقم لای دستمال کاغذی پی‌پی میکنم و بعد از یه هفته که جمع شد، میندازم سطل آشغال
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70770" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=b35xCa1wj6CLejO_Q0mNAz6DME9qfqMpCGxfuA07iwE3afJZkd2k26Yj-BTAL87Rln173tiP-R6EmF6He1Z7XUJy9tpbExTzAAA_VRRwmeBWZXVa2F0FOO9dEO5GBBwMoi-huXmcWJbqeDTHG26g2-3n_sLGYQwitIYzGT7Otof76M5e83rG57QkJcUovOuY0ZK2ti8C8YaiEiRGqO3MsO3IqfFaRhBEeFy1ptOHqScIdyrJIPQbf2M2C4LC4ViINsARYbspJj1DnZPNtofkgdmKjLYtR0wLCKMcXxUnuzDbm0q3ePoAznyRxtDZDQuNvhwGuQTcUfg16vhkqiIUUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=b35xCa1wj6CLejO_Q0mNAz6DME9qfqMpCGxfuA07iwE3afJZkd2k26Yj-BTAL87Rln173tiP-R6EmF6He1Z7XUJy9tpbExTzAAA_VRRwmeBWZXVa2F0FOO9dEO5GBBwMoi-huXmcWJbqeDTHG26g2-3n_sLGYQwitIYzGT7Otof76M5e83rG57QkJcUovOuY0ZK2ti8C8YaiEiRGqO3MsO3IqfFaRhBEeFy1ptOHqScIdyrJIPQbf2M2C4LC4ViINsARYbspJj1DnZPNtofkgdmKjLYtR0wLCKMcXxUnuzDbm0q3ePoAznyRxtDZDQuNvhwGuQTcUfg16vhkqiIUUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سخنرانی یه اخوند در خیابونای قم برای در و دیوار.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70769" target="_blank">📅 21:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=DGPg-zKAMco4tuEPzCjrUM4lmbz1gxiFByTuZVN6bzR2_CGksjVA4sHQQ6pfRXeWq8ccrmMLeyoe0NNO1U-jVJZopzlecoKpwHIKGSqeWZVTKVKmbQ0iQ4gKEl62NrGAEYgQlGBxQh4LmZhUR3YH9QObQugpz-0KGYFBmEdOEuVabaBKeysip61J3hkfiCt4e8rbwl2foiBFjjT6ujSo80MepYyWFO8r89LxxBMYh-B2Gi7GE55ZhmHeuWneW6qDpSweHjTsPEsCHQV8YcxxGdPkk8z2X_VM4waWKehzXVp3RiKZ9nvaQ70F7MYX3HF7io3koodypr-KN4s1LC8N1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=DGPg-zKAMco4tuEPzCjrUM4lmbz1gxiFByTuZVN6bzR2_CGksjVA4sHQQ6pfRXeWq8ccrmMLeyoe0NNO1U-jVJZopzlecoKpwHIKGSqeWZVTKVKmbQ0iQ4gKEl62NrGAEYgQlGBxQh4LmZhUR3YH9QObQugpz-0KGYFBmEdOEuVabaBKeysip61J3hkfiCt4e8rbwl2foiBFjjT6ujSo80MepYyWFO8r89LxxBMYh-B2Gi7GE55ZhmHeuWneW6qDpSweHjTsPEsCHQV8YcxxGdPkk8z2X_VM4waWKehzXVp3RiKZ9nvaQ70F7MYX3HF7io3koodypr-KN4s1LC8N1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صدا و سیما:
تو رو به خدا تورو به ۱۲۴ هزار پیغمبرتورو به همه اهل بیت باور کنیم که ما تو جنگ پیروز شدیم
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70768" target="_blank">📅 21:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWoFJ2GaK6mjpmaVUBlp_eR6ANKgWs9CuK08V0uvR3T1dtOJsnRRZKK7k4Wrktza1yAiOKq5PtUkcotZ2KQ5lbEzglqFFsxlcUzc9auAGg33jJ7texwwb9PHnrUO7uuNv5CMThShgprNQKB5DsIz128Q3qyf5y-_ySh42OfuPFMMIjb7ga_xi4P4zv_BVahKq918fgcY2CFZRGh5Lc67-HHbm7YV5aveMo8I5KDTa7dqBpn0q0uEILy15qk-XuBkvXJYKvBW8F2PDfe9-RVgFP9a6S-1QF1hTdrEiGzL0mzPUlRJjjQCSXP3hzsxSkvpQw3mCYOecYWvsJL2AiP3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
دیس قالیباف به بسنت:
دروغگو، دروغگو، شلوارش آتش گرفته.
برای ۱۳۰ دلار واقعی، به کارمندتان بگویید که آمار مودیز را که ۱۳۰+ میلیارد دلار هزینه جنگ را نشان می‌دهد، بکشد
از دیگری بپرسید که خیابان جین چقدر از ۱۳۰ میلیون دلار فروش استقراضی نفت را فقط در یک دور معاملات آتی برای شما سوزانده است.
دروغگو، دروغگو، بازده (اوراق خزانه‌داری آمریکا)آتش گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70767" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=cMyaRlF9szac2EdG5IAfviCTiELflNg5BZthlX500bkG7HPySJhTDxToOdlHVdqiA5eNY87yiHZM0zmC0L4aaf3FMAJBz6jkpBM__an9F-tHu4BlSLgm-TyGROaH1zPtywxAhDMjZ88v3r6vnIML93b8RBCQDWkf0C_WlqnmgFBCOO54JCpWQB-PoC_s51K-hghBv_xllqBg7ZRhz_oW81ZnnNTgTgaFcixju385qXWaIac2YLCC9BRdYTNpLXPF_WWj48n_2AROKL2XEIKaYryzCOXxQjJA5lM4OOT5-cVlPhlPUAnJFG5O1ZM7hZCmEOpk5gOkw4tpK3-K61Gvyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=cMyaRlF9szac2EdG5IAfviCTiELflNg5BZthlX500bkG7HPySJhTDxToOdlHVdqiA5eNY87yiHZM0zmC0L4aaf3FMAJBz6jkpBM__an9F-tHu4BlSLgm-TyGROaH1zPtywxAhDMjZ88v3r6vnIML93b8RBCQDWkf0C_WlqnmgFBCOO54JCpWQB-PoC_s51K-hghBv_xllqBg7ZRhz_oW81ZnnNTgTgaFcixju385qXWaIac2YLCC9BRdYTNpLXPF_WWj48n_2AROKL2XEIKaYryzCOXxQjJA5lM4OOT5-cVlPhlPUAnJFG5O1ZM7hZCmEOpk5gOkw4tpK3-K61Gvyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
دریاچه آمریکا توسط «اردک های دونالد» محافظت می‌شود
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70766" target="_blank">📅 19:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
صف ترسناک و طولانی ده کیلومتری یه پمپ بنزین توی سیستان و بلوچستان!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70765" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70764" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRObmotLLlZ8pi_KYyduZh4nl0xYtXxrSBfhOSvwi-ZEuAtBZ-q51n0NXkzmSQBFtY4UA6DfnLOcj0pi1p1mOJI5Wv-KGtFy4qop9JxrlG4lO2qV4l4JCW_QWHUFVc4ZXrKVzspKq78N9VRMeFiaruiTslkf5NEjBrW-zn140S4tDKZEmVn8jk-vkIJjxj6mj-uMve5RrgBdQVfDhBZpHs9wnKsPrxhkVrqNZcLHtMHNMzLBFIzIRcpBF6003umwKyKy8F-OqFqgPSppjXsxpKjjssy56whkPuPHdSLtnLL8m0cBm7ZuZrh7DkgB3Ygye4Ulqg-LuKBJrFZPZB_8ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70763" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qF3rKxU1MBY0vadPYCMr5DrrGLEq4ckWnnYh9go2L8rSjtFcE9P73Mhow-FLWf7OfcGh3U5weL9MIa4t7a4P-rYXeHSoCgBkH7ADiEK3tv6B60fI_imfBNB6CBRYppXLNqu75FyUFjH9YwNKbtuehDtVnwfij-IqZ98jS1YOhhrdtp0Vt29Ib6pe24t5iNbjq6hzq6y3rW2GHB86PNUherh7FqfQ1AuWDhYNvZ3Vj1SuLUqn4QY7xBuFVCD8TxxxAVTOuAEUrNzsap14h45S6-yWStRqZP4U81cdVMiI3TqbYzN4GaiO9wc1ucMLXb9UXI92ZXzFxXtKXN95H-f8IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qF3rKxU1MBY0vadPYCMr5DrrGLEq4ckWnnYh9go2L8rSjtFcE9P73Mhow-FLWf7OfcGh3U5weL9MIa4t7a4P-rYXeHSoCgBkH7ADiEK3tv6B60fI_imfBNB6CBRYppXLNqu75FyUFjH9YwNKbtuehDtVnwfij-IqZ98jS1YOhhrdtp0Vt29Ib6pe24t5iNbjq6hzq6y3rW2GHB86PNUherh7FqfQ1AuWDhYNvZ3Vj1SuLUqn4QY7xBuFVCD8TxxxAVTOuAEUrNzsap14h45S6-yWStRqZP4U81cdVMiI3TqbYzN4GaiO9wc1ucMLXb9UXI92ZXzFxXtKXN95H-f8IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنفرانس خبری علیرضا منصوریان در عراق که سوژه رسانه ها شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70762" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=c7Nc0-sTf-Z4BgVLUpMtiPAtkUiy4wgtdvZnsGndOCsR5mgq40LR_dRZ_0bU0YzCgIA1i2G4xKYr-KtEnd1T9_8qvwMJiM8lCzecsz7_SL22-EV7aHGYHfku3PEXAL1SL5mEOLZQimA04FPkYnNhfb68w7x5EEM97KTCCQaLCFdfQ9gnuLvVON3KYW58Ftbts86kndLG3uAv426CyoAoDRJ2Ji-GDNQqqIksebPRnNqkvFPITjophlX1bUoJ3a9XHHZtVvuGVDu3DZcS3ZCYoTYHLbjJR9gfQEjBc1-WKwf7SliSQ-bhkeFYNXDZOxvl_BHjDMAupXL6CXHEf13Gcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=c7Nc0-sTf-Z4BgVLUpMtiPAtkUiy4wgtdvZnsGndOCsR5mgq40LR_dRZ_0bU0YzCgIA1i2G4xKYr-KtEnd1T9_8qvwMJiM8lCzecsz7_SL22-EV7aHGYHfku3PEXAL1SL5mEOLZQimA04FPkYnNhfb68w7x5EEM97KTCCQaLCFdfQ9gnuLvVON3KYW58Ftbts86kndLG3uAv426CyoAoDRJ2Ji-GDNQqqIksebPRnNqkvFPITjophlX1bUoJ3a9XHHZtVvuGVDu3DZcS3ZCYoTYHLbjJR9gfQEjBc1-WKwf7SliSQ-bhkeFYNXDZOxvl_BHjDMAupXL6CXHEf13Gcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
رقص ایرانیان در شهر وان ترکیه؛
هزاران ایرانی برای خرید، دسترسی به مشروبات الکلی و تجربه تفریحات شبانه مختلط — که در کشور خودشان امکان‌پذیر نیست — به شهر وان در شرق ترکیه سفر می‌کنند؛ شهری که تنها یک‌ونیم ساعت با مرز فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70761" target="_blank">📅 18:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=bTvugyXVo2r_ejgHkxyEBzyI9Sx3dC8-NzShjfQzhiGBEpBdxpR_ARlhdYIxKclIPltnlwazUhNSwvLBQsAu9KCrlx1w8TjNuiZieZ5Y0M7EFjbcxcelyM08bIXNNaBc-_gzKNQQ_LQFuIKUHcfdwAP-IQWArh2dL5e5VJBnQv7heNhj_ve4c16-pBW4j-StxBcKWZ2G7O6ftgClQuo_OgX3oRFNglnpWKBCXWGWx21KRgEb6gCZgPfzlJLCheb5onys3sqk80zyG2P2SK5Zgw41IU2frPYYvyJcxUn9_lHC8yuhY7dvIHQ6R97tmUwlWtDBU_KuT8kcG5CxbwGmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=bTvugyXVo2r_ejgHkxyEBzyI9Sx3dC8-NzShjfQzhiGBEpBdxpR_ARlhdYIxKclIPltnlwazUhNSwvLBQsAu9KCrlx1w8TjNuiZieZ5Y0M7EFjbcxcelyM08bIXNNaBc-_gzKNQQ_LQFuIKUHcfdwAP-IQWArh2dL5e5VJBnQv7heNhj_ve4c16-pBW4j-StxBcKWZ2G7O6ftgClQuo_OgX3oRFNglnpWKBCXWGWx21KRgEb6gCZgPfzlJLCheb5onys3sqk80zyG2P2SK5Zgw41IU2frPYYvyJcxUn9_lHC8yuhY7dvIHQ6R97tmUwlWtDBU_KuT8kcG5CxbwGmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر داشت چالش ضبط می‌کرد که دو نفری باهم برن غذا بخورن، تا اینکه یه خانم دکتر خورد به تورش و آخرش این شکلی با دعوا تموم شد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70759" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=N2i341UrjEt5z1fIJQobxHC_V8D5Wx8HFVYolxNTgQahO1ur4yMYHfF0EVxozxnmlqFjkF-TsqWXpXglUCqYEoC2jhk4uX4z8VJpxy6_F3HQtwVsWsLaf83idtJTjljR6AKGb67klzdxGq1jxDIksCt4GzRLeYgArhZH_F-rntwRoxaZmhJ0UFQY3XUnSVdOsoMLzx7iy_M6FD1WNPde6ZaAkqUGusi7hZ4cgy5wAycq0DqMn6bYMjpqp7A39Be3LJbWPZwHZLbo_gaUb7YA_adXJ9oQlNzRfPLTXVpkUzMd1fvPsHsflToM1ikKlNYSVDQM-xDoBEVuIvFoZEUqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=N2i341UrjEt5z1fIJQobxHC_V8D5Wx8HFVYolxNTgQahO1ur4yMYHfF0EVxozxnmlqFjkF-TsqWXpXglUCqYEoC2jhk4uX4z8VJpxy6_F3HQtwVsWsLaf83idtJTjljR6AKGb67klzdxGq1jxDIksCt4GzRLeYgArhZH_F-rntwRoxaZmhJ0UFQY3XUnSVdOsoMLzx7iy_M6FD1WNPde6ZaAkqUGusi7hZ4cgy5wAycq0DqMn6bYMjpqp7A39Be3LJbWPZwHZLbo_gaUb7YA_adXJ9oQlNzRfPLTXVpkUzMd1fvPsHsflToM1ikKlNYSVDQM-xDoBEVuIvFoZEUqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:
ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود.
امروز همان پوشک ۸۶۵ هزار تومان است.
باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70758" target="_blank">📅 17:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=mGP-HE3WqXxHRE7K-cOvkB9rNf4bGRFyIrvLQyNNzc4_dmkjrRUm5TlMjvko3FeFtPeDRrYOAWz2P7QeYVhhibATQR8_w-x-ODXuq-QJMJFLeaqAEj5VI4ZYSYfJ3Nn9_zjVj8dltUk4_ADbX5p7qodsm3WJQc1rZ3G4c-e04y-q8qIZJe0urBRIHFR15gNlMP86R_UOCxXFtIqO1H9KrTHxG-vtnTmQH7AUgpAGadYcoZjkU8sbK7H_lBQ1tUO0mpnRs_nbOoBh1thsplrrVxsHUQEqa5GaEctbdvkpbGupAjetj5l5y_QoyIm4epr9BgFyMZhN8_rAbveOhmpAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=mGP-HE3WqXxHRE7K-cOvkB9rNf4bGRFyIrvLQyNNzc4_dmkjrRUm5TlMjvko3FeFtPeDRrYOAWz2P7QeYVhhibATQR8_w-x-ODXuq-QJMJFLeaqAEj5VI4ZYSYfJ3Nn9_zjVj8dltUk4_ADbX5p7qodsm3WJQc1rZ3G4c-e04y-q8qIZJe0urBRIHFR15gNlMP86R_UOCxXFtIqO1H9KrTHxG-vtnTmQH7AUgpAGadYcoZjkU8sbK7H_lBQ1tUO0mpnRs_nbOoBh1thsplrrVxsHUQEqa5GaEctbdvkpbGupAjetj5l5y_QoyIm4epr9BgFyMZhN8_rAbveOhmpAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💀
این ویدیو از سرعت تایپ مسی شدیدا داره تو رسانه ها وایرال میشه
حالا جدا از سرعت تایپش فکرشو بکن لیونل مسی با ثروت تخمینی 1.1 میلیارد دلاری گوشی ای که دستشه آیفون15 هستش
بعد یه‌سری جوونای ایرانی با هزارتا قسط و قرض و بدبختی میرن آیفون17 میخرن و تو چشم همدیگه میکنن
از یه طرف هم بعضی دخترا میان میگن پسری که آیفون17 نداره کنسله و ...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70757" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=hzSrBM4ph_AD3N89LvREd-nFnZl0FXWKIdWAcZaxqEXX15rThyY3GjiaxLFObjh4YnP97fBxT7OF0OTbqtau7dylM-QGg7rUXOZyVh8AA5UWNZq0MjG7TuMkaUg0jorCixk3vPgh2ftDVFtYhHW3LSIqoGesuPI48J7qWA93_tyVVSYphXy8Yj_caPPsrH54jrpB1SA531MzVKn78JQfRHgzXAQx1jipaXbajS4CI2KElutwSUpCf86e6FD7JLYXJAhVLanll1H2nVHl3i4_PHiiJ9URQDCCSeG978qU-zdZT2Mev4Owh9N7ALKhZl2A7hI5wiMY_eZ5KGxcQdxgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=hzSrBM4ph_AD3N89LvREd-nFnZl0FXWKIdWAcZaxqEXX15rThyY3GjiaxLFObjh4YnP97fBxT7OF0OTbqtau7dylM-QGg7rUXOZyVh8AA5UWNZq0MjG7TuMkaUg0jorCixk3vPgh2ftDVFtYhHW3LSIqoGesuPI48J7qWA93_tyVVSYphXy8Yj_caPPsrH54jrpB1SA531MzVKn78JQfRHgzXAQx1jipaXbajS4CI2KElutwSUpCf86e6FD7JLYXJAhVLanll1H2nVHl3i4_PHiiJ9URQDCCSeG978qU-zdZT2Mev4Owh9N7ALKhZl2A7hI5wiMY_eZ5KGxcQdxgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار در گفتگو با شاهنشاه آریامهر:
آمریکا و بریتانیا نیز، که احساس می‌کنند رژیم شما غیردموکراتیک است. شما چگونه به آن پاسخ می‌دهید؟
❤️
شاهنشاه آریامهر:
خب، من به آن پاسخ می‌دهم و می‌گویم که رژیم شما دموکراتیک‌تر از ما نیست، زیرا به نام دموکراسی، شما کارهایی را انجام می‌دهید که ما از آن‌ها وحشت داریم.
هیچ برابری بین مردم شما وجود ندارد.
تفاوت بیشتری در سطح زندگی و ثروت بین مردم شما نسبت به مردم ما وجود دارد.
🎙
خبرنگار:
آیا اینطور است؟
❤️
محمدرضا شاه:
فقط ببینید چند میلیاردر دارید و چند فقیر.
در اینجا، ثروت کشور، حداقل ما پنج قلم مواد غذایی را یارانه می‌دهیم
تمام آموزش رایگان است.
در سراسر دانشگاه، ما حتی به دانشجویان پول توجیبی می‌دهیم.
🎙
خبرنگار:
خب، اجازه دهید به شما بگویم که آقای کالاهان (نخست‌وزیر بریتانیا) مانند شما در یک دفتر کار نمی‌کند. شما چگونه به آن پاسخ می‌دهید؟
❤️
محمدرضا شاه:
آقای کالاهان نخست وزیر است.
من شاه شاهان کشوری هستم که دو هزار و پانصد سال سلطنت دارد، اما این کاخ را نمی‌توان با کاخ باکینگهام مقایسه کرد.
قیمت کاخ باکینگهام صد برابر بیشتر از قیمت این یکی است.
در گذشته، شما، بریتانیایی‌ها و دیگران که در اینجا نفوذ داشتید، می‌توانستید نخست وزیران را به دلخواه خود تغییر دهید و در امور داخلی ما دخالت کنید.
آیا برای آن زمان از دست رفته متاسف هستید؟ آیا همان چیز را می‌خواهید، دخالت در امور داخلی ما؟
ما به شما اجازه نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70756" target="_blank">📅 15:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cITKZnVm230xKHaMXXBgRJ43RnymHxrGewPt8pzJN38230evTOH_zdS4TXpLYVkXnL2Mc41QHUL8ZBiO5xj4Cuj4gHeuYWGdkByGd4l0bjfsSsw1z0D5udfSJVqYXDdmRNIOjsKGhNpybsvjsjNXWJKkhB0sPU3xEsOdwvgBLmDt1Nud0MJLFHpiSirXD8MTyTvIHwa19QuEdfkj36MtSYJh_DlLbOGVLflyUOnxK9rlR5fEyQW_A5t82dDnn5TLdbJXT6UU7Pn8CHZf5jD61z-brFgq7BoLvysKFpQ1G4vwwViwFeQDkjJvf1S1n0BI3z9COb3I29DCMvFGDDIeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
اطلاعات ما حاکی از تلاش‌های گسترده برای دستکاری بازارهای انرژی است.
عناصری در دولت آمریکا با بهره‌گیری از رسانه‌های ساده‌لوح، سعی دارند برای منافع شخصی بر قیمت‌ها تأثیر بگذارند و رئیس‌جمهور آمریکا را همچنان درگیر جنگی بازنده نگه دارند.
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه، بر طبل جنگ می‌کوبند.
این مصرف‌کنندگان آمریکایی هستند که پیامدهای واقعی این وضعیت را با تمام وجود حس می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70755" target="_blank">📅 15:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQStmV96gyVYcVKig-fPHGPkTeMf4eS_EQneWadze9VEYL2uYCpxsSU5p9SY3EvndQGwjcdT46fm1wvo0c8mTPELbZDCgp2-Hq2ZFAVRWRXDYPce_GykbIJNlny4rtcGyOzOwv3lHlfw-DMtlIxHwXoiv7RroLbeye3a7HLwwayXAyWovji8uYrf-vXsZgR8r9C2zaJ6irLvTRN5cx493tjxGiyKgIA4HNjCwhrFAhspYDZxtPihYHyHvRxYjdIrNd-rYKPUsbThT3E8lVwBZ671eSP2oFXH_7c9A-swJOkiWgdbIwlUz8YMnu4blWHDG6sUswEllFPfSs5pLu1MPDKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQStmV96gyVYcVKig-fPHGPkTeMf4eS_EQneWadze9VEYL2uYCpxsSU5p9SY3EvndQGwjcdT46fm1wvo0c8mTPELbZDCgp2-Hq2ZFAVRWRXDYPce_GykbIJNlny4rtcGyOzOwv3lHlfw-DMtlIxHwXoiv7RroLbeye3a7HLwwayXAyWovji8uYrf-vXsZgR8r9C2zaJ6irLvTRN5cx493tjxGiyKgIA4HNjCwhrFAhspYDZxtPihYHyHvRxYjdIrNd-rYKPUsbThT3E8lVwBZ671eSP2oFXH_7c9A-swJOkiWgdbIwlUz8YMnu4blWHDG6sUswEllFPfSs5pLu1MPDKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
مراد ویسی:
۱۵ هزار میلیارد برای شیر مدارس «نبود» — ۱۵۰ هزار میلیارد برای خانه‌سازی حزب‌الله لبنان «بود».
بودجه شیر مدارس بچه‌های ایرانی قطع شد. عددش ۱۵ هزار میلیارد تومان بود؛ گفتند نداریم.
در همان حال، ده برابر آن — ۱۵۰ هزار میلیارد تومان — برای ساختن خانه برای اعضای حزب‌الله لبنان پرداخت شد.
وقتی می‌گوییم اینها ایرانی نیستند، عرق ایرانی ندارند، بعضی‌ها معترض می‌شوند. اما ایرانی بودن به این نیست که در مشهد و تهران و کرمانشاه و اهواز و کرمان به دنیا آمده باشی.
وقتی پول شیر مدرسه را نمی‌دهی و ده برابرش را به بیرون از مرز می‌فرستی، معلوم است که منافع ایران برایت مهم نیست.
بازنشسته معوقه‌اش را نمی‌گیرد.
گندم‌کار طلبش را نمی‌گیرد.
پرستار اضافه‌کارش را نمی‌گیرد.
بچه مدرسه‌ای شیرش را نمی‌گیرد.
اما بودجه هزار حوزه علمیه سر جایش است.
اینها حکومت نکرده‌اند؛ منصب حکومت را اشغال کرده‌اند. اشغالگرند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70754" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=IxV2C9NGsTpCr2T_2d2RuWjOtOZ8Bb6U9tt6gKP2zGpPmBevEXJcNhjEOzPM-0Df-aVMBfz1augAyI-3Hjfm9oR1dGg4bv8SrCrm-Vl1vnskDEIuFnxpCK7SltOvTfJJoIq6JH_F8P6Gr0QG6HjQXXKA7bSugvMku0Xn77RAgKdP4W_xx0y9glfjMCIFb82KDsai9h12nq8U9RoYlh4wrNChhCNJq8XeMzWW181W5CEjSyeLGJMCK5I2kjDKx5E5lzE2ZGV7Lu8zwJSYvA4d1eWJYRr2ETGUpLFoICT2umM3rIl-NikNdM4ZYwkGqdinCGVz13kjRAzHNHuN6s7QPIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=IxV2C9NGsTpCr2T_2d2RuWjOtOZ8Bb6U9tt6gKP2zGpPmBevEXJcNhjEOzPM-0Df-aVMBfz1augAyI-3Hjfm9oR1dGg4bv8SrCrm-Vl1vnskDEIuFnxpCK7SltOvTfJJoIq6JH_F8P6Gr0QG6HjQXXKA7bSugvMku0Xn77RAgKdP4W_xx0y9glfjMCIFb82KDsai9h12nq8U9RoYlh4wrNChhCNJq8XeMzWW181W5CEjSyeLGJMCK5I2kjDKx5E5lzE2ZGV7Lu8zwJSYvA4d1eWJYRr2ETGUpLFoICT2umM3rIl-NikNdM4ZYwkGqdinCGVz13kjRAzHNHuN6s7QPIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyvNj6IdgpEnihjjix5K4XgHxJ5EC8ATQdU37ioC64oZRpdgP-69gWi1z_GqBSv8Qz6iYUUTaLU5j49chZwe_itSOKwlt9wpM5DbLxYufkqrzIBQHjudpypHnyypY91SR1SHk99gDTnD5oZw6ksbangCdckMvfZABVwx-GH59gvVEzalonv6P37ZpFXC2w0iAk6Yp5KgY3jJBc_6uW1WHAxJQNHgoe06ihPJ2Lsa5z8b5PjMvxRukVnwiFNRBWWmXymRmwxGpwrW23cSo0UjNlA5wwujjca0V02NJFqHmeZ7Cx1ZAMKELoC5wmTM8TiJCirPav5PpF9aQWig_RL15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=ofPHcb_B9jJ4FlLyY-2GWG_xdAgnGdybcemegoIhSJOcfrdfKvGESDdogyNgat6-NYjxjITWiT1ZCBJmpthrGOnH07QxdvPMtAV3cHGuzWjlvWHJgOE0em3jt-3fOLBANPNV7Xxk886MVgZGo8SPe4sLswJgEUchs-tbFmqJb1EYtRpZmFcKH5UpvVLM1OYZTL-C0TLBoKiU71zEIZx75c-NV6cjZr6Z0rcJ2ZZiAp4pBheRueeUIkSgsofO5hpdrzRf6jqBAwqzMMq_cGGjciJdhxj9oROHVu63T-MBwNVW3XblyVxvVpDPfEQ4Am5fjLaoz-hinJMdROh6NG-YPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=ofPHcb_B9jJ4FlLyY-2GWG_xdAgnGdybcemegoIhSJOcfrdfKvGESDdogyNgat6-NYjxjITWiT1ZCBJmpthrGOnH07QxdvPMtAV3cHGuzWjlvWHJgOE0em3jt-3fOLBANPNV7Xxk886MVgZGo8SPe4sLswJgEUchs-tbFmqJb1EYtRpZmFcKH5UpvVLM1OYZTL-C0TLBoKiU71zEIZx75c-NV6cjZr6Z0rcJ2ZZiAp4pBheRueeUIkSgsofO5hpdrzRf6jqBAwqzMMq_cGGjciJdhxj9oROHVu63T-MBwNVW3XblyVxvVpDPfEQ4Am5fjLaoz-hinJMdROh6NG-YPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVbj2_xG_LLf8qTo33diQRYbJbMvXoJpCM-F8b0Q9_3R7WvEm-Al8fam1jxycQW1XsYlwlbro9v2RPTCgDfO8ZS6iCYhEq57Iz-QJO0GHVL4RWEgvSxVDjqn39XM1qFfbigMxUbQdhWUwbu_QzJu15DG1pW5Y3VkdEvTn2uWrQkD1-12d_NrXrIKLLjLiNkvpuaxLcANnajQheRBu6ObD8qcXVdXh7yI0SxYX-lJjO7if5KUIWXpBQMLhBOwfXxUFUBuoZviUoT9XvNHSN63C1rFE4o1pKahI4V58zCLF3Av9mar6MItrIEC_FgN3HcPIlAvjIrRt0Z_klwZuJ0iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=J0j7yfJNzD1W_xgG7vkCYR9pFSRTN0Dqr0i-Y8sHbRZYbK9mUPvK_92jNnOSTG_Am_BErzBMOl2FGuY6Drg5fHF-qKyphKXKPQKJyI_E-nBJKIS2mdTFrAV4l2WkPMUm_nTwmweyMKZCUcOsgFCchZhM60ngkuTN14-byqykFpC0CJy3_SUQmBaEF_cpPV9CCBJT1TRDuuMURU_Ndw7wjHoeZMWhJnaZgskqbEpaEwmNUiNlRX-c3-BESt51kO4gKoiB-KqPkWQ9GxI5dgyj6X1OVpMz_Pz-ZSj-YymxOpI_PBsVbHyvc7MJGLIfwNKi_9MMzygiVfXOUCOgqaKBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=J0j7yfJNzD1W_xgG7vkCYR9pFSRTN0Dqr0i-Y8sHbRZYbK9mUPvK_92jNnOSTG_Am_BErzBMOl2FGuY6Drg5fHF-qKyphKXKPQKJyI_E-nBJKIS2mdTFrAV4l2WkPMUm_nTwmweyMKZCUcOsgFCchZhM60ngkuTN14-byqykFpC0CJy3_SUQmBaEF_cpPV9CCBJT1TRDuuMURU_Ndw7wjHoeZMWhJnaZgskqbEpaEwmNUiNlRX-c3-BESt51kO4gKoiB-KqPkWQ9GxI5dgyj6X1OVpMz_Pz-ZSj-YymxOpI_PBsVbHyvc7MJGLIfwNKi_9MMzygiVfXOUCOgqaKBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz4aT4fAm7eDXZeJpyNTEJ2E_tQ5FUaw4Yifp6p8SIyRtTJbM33_u6BoRBNyOifwQZ1SiqptO25Qcxh2erxa9jyjBp65vDh2rdseykTT7G0Ho127XV8Xk8hXpTD6xpTAQ10ekHGm-pRQf-5kj7Y5qR23wYgMnr6yODUXxfL_Eh7ndpwsRnzi7od-6Kk403z_C1-3jvp9nKRhH0lJs6Hn0M46LHcEHMhDqVy6G4HB9t5syIrcRA68JX3AWOT7bG1Jd_zCMj0cyT5IYsoh4_p5UM34xFV4KzGbVg37laSlxgguYzDSA8haOdnLFGBqSVtt09ZGiQbuqRIH2D8fXLouig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=D3dphf42DQ-KUgbnmQAs02u2ebevE9qM973C_XFpOEd_9n5gyLXq07zqLq_5C3U1rOqTP3S7Z9uICCZ-iBgzKwalcXvH9tyOCTtHyCTpHhrk1zYzGzZH0uFFhnRvri6Dyc198HUSYGhZDQziZgbGbpeLlsWVg530kYY7XZPJ2LjwcXgGWwdyAV9hDC63iq15RyQCCNPkfUPOX-XMCud2ErvOUnLNpaHl97CMUL27qZN0exHDI7ADtYxDKldjGdXrRGMwLUyGdQs_kyWHt3JsTCyqaaMOu1TNuO9AZTiq8UQCw8HgwELuJvJbBD1RX47yFcp5A5a6Sd2qn5KJN2vNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=D3dphf42DQ-KUgbnmQAs02u2ebevE9qM973C_XFpOEd_9n5gyLXq07zqLq_5C3U1rOqTP3S7Z9uICCZ-iBgzKwalcXvH9tyOCTtHyCTpHhrk1zYzGzZH0uFFhnRvri6Dyc198HUSYGhZDQziZgbGbpeLlsWVg530kYY7XZPJ2LjwcXgGWwdyAV9hDC63iq15RyQCCNPkfUPOX-XMCud2ErvOUnLNpaHl97CMUL27qZN0exHDI7ADtYxDKldjGdXrRGMwLUyGdQs_kyWHt3JsTCyqaaMOu1TNuO9AZTiq8UQCw8HgwELuJvJbBD1RX47yFcp5A5a6Sd2qn5KJN2vNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGpApN1h9wIoPzkOgLSAz0ekGxpaeFQ9Zke1R2Ib2L1JJl4bYi1UcC6bYf9AxwClwuiFkFltTt089_c2wSfq5degRF4JSS8-wuUum4lohUoHGrgugzuJOagLYccSQq1woT4E7T1SaK__w8ie1V8-ZGotLRSgo_pqRXTsod6AUoq8xqQFKZuVrlcwVpy3sixkwc5qTBMdnkaMx2_o-VkleldFxgzgTMmc8lu3ylikJhSkLREiejhC55sDpmkz8xBsOpe9OM4pDBt-BToSpjVRKq3W-mv8fIpHG7dX9rtNghvt4BpEOr0R60OeW375_sqlqpQK9v1mWQ7H_lBYiOMpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=L_nMadDu63Yx2qi-KUJIuRmBvBsEgYvnU3Rg4yIrOcnYZEM6WidVp5q1Vjo_MZfbFVfke-aqiKKcqFwkHbZhe2XjkrXAAsAy4sbnisc3pMI9efR0LQGQld5_f7xHjpJXafSTavmM4JyaHMfakakCYr8xmD2jry4OIv8rlAR6vDMsMPXIcSutnNp805qTqqK95xU4afB9eHx7wQQ5qA3ptoBfpq1YsC-zxcUUU7r-8E_rP4LPAQwFKpmH81tQUvu5_O4FnKVCm1kTFcEvd6etjPY3eFnwCn3zA3Cuy8BRPPw-Ev18FA9sB8K308HROC7eQpQnmRNSPRg4PK0GANDxXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=L_nMadDu63Yx2qi-KUJIuRmBvBsEgYvnU3Rg4yIrOcnYZEM6WidVp5q1Vjo_MZfbFVfke-aqiKKcqFwkHbZhe2XjkrXAAsAy4sbnisc3pMI9efR0LQGQld5_f7xHjpJXafSTavmM4JyaHMfakakCYr8xmD2jry4OIv8rlAR6vDMsMPXIcSutnNp805qTqqK95xU4afB9eHx7wQQ5qA3ptoBfpq1YsC-zxcUUU7r-8E_rP4LPAQwFKpmH81tQUvu5_O4FnKVCm1kTFcEvd6etjPY3eFnwCn3zA3Cuy8BRPPw-Ev18FA9sB8K308HROC7eQpQnmRNSPRg4PK0GANDxXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=Hf3ytWaAj-HkpF6K_o5EoUbi6-4P8Pvi2SW1jELenIGjILkISi9bmNOEHReAzw6-bTl0_ofI0bu647OgOKlsU2Vpr06DyxVFE6J5tn04QAb4eCvGiLuIVkX9J_pXSrUVHBGeXPPqNJvWxWVFnfkGmTTg91IzuoGvibncuKuWh-M7bth0a1rPQGWgYhgu88yGHb7gwtaLfFzcWY6R1O7b9mKNcJAwJQ5xBp8LwgeHfteCU7u7SKewNrIf_uV4ibfmqlbrfqcaH0AJGSW5jkd4W5JKStUmbHFFM3UMcpNaRrwBfaEG4_6z8Onwv2Rhv32olBYpU3jEeKOWX2Wicy2h8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=Hf3ytWaAj-HkpF6K_o5EoUbi6-4P8Pvi2SW1jELenIGjILkISi9bmNOEHReAzw6-bTl0_ofI0bu647OgOKlsU2Vpr06DyxVFE6J5tn04QAb4eCvGiLuIVkX9J_pXSrUVHBGeXPPqNJvWxWVFnfkGmTTg91IzuoGvibncuKuWh-M7bth0a1rPQGWgYhgu88yGHb7gwtaLfFzcWY6R1O7b9mKNcJAwJQ5xBp8LwgeHfteCU7u7SKewNrIf_uV4ibfmqlbrfqcaH0AJGSW5jkd4W5JKStUmbHFFM3UMcpNaRrwBfaEG4_6z8Onwv2Rhv32olBYpU3jEeKOWX2Wicy2h8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=r0TEkX6DDrDNXZ1O6IKeaseg2opyZ6XkPcw2hUsha-lyjFGklYnvEv4U86AkyDejgIcFQklBf87jH7iqpIdyA-UMoBSK6yambx45WpSPMyiEofZc8Y44vyZuMzzPO-9dk0PEvyV2UcOUVRy0xSrnuqzApH_Y2L7Ij4g33xV6QAwVdotxnFk-5tsNrf6aq7pr_Q-1qpFZoa7mMyJ-e4gKdNudRk6ZHTcGKB1G30uicHyMf1dRTt7-LtYL9RAOC6vXxfxuISATQgKofQKTfqWVJu9FSLN4wQMLFHzQ0LftoZiKsZYox7DBj5Rkh3XHULaa4NcAEMvushJRfm8KRVvJe6kAzXEffbxWVRQM8x4N1rUMr7L3M8spW3C9MaQ8_6au9zPXaOLz-MHT7UMSDtB1hbxQFRIIdjub5NNlYqYw6AdO1vMrZlG8u3aRlri11Bg_Juq2H5VaVoGPHWZS3P5_waWFQe271L789-Rt-79yuwYk5oB-ow4e_5NWx1HvhQlYiDvEfhqKtKa0qme2rNr9YO1nW2V7AXzZAxrgsaRCDZe_b7y7Fr2tTt3JwlKcwjtvhsdVj5jWtQpcsDnGKI7FfmYMZ6vX7YqZMbuLf1tIH20KOyVzee4frVG0PhRFfftxZkVGtH7N9iqB99jg2_gY1Zraekrft7rYQAr1CEPDpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=r0TEkX6DDrDNXZ1O6IKeaseg2opyZ6XkPcw2hUsha-lyjFGklYnvEv4U86AkyDejgIcFQklBf87jH7iqpIdyA-UMoBSK6yambx45WpSPMyiEofZc8Y44vyZuMzzPO-9dk0PEvyV2UcOUVRy0xSrnuqzApH_Y2L7Ij4g33xV6QAwVdotxnFk-5tsNrf6aq7pr_Q-1qpFZoa7mMyJ-e4gKdNudRk6ZHTcGKB1G30uicHyMf1dRTt7-LtYL9RAOC6vXxfxuISATQgKofQKTfqWVJu9FSLN4wQMLFHzQ0LftoZiKsZYox7DBj5Rkh3XHULaa4NcAEMvushJRfm8KRVvJe6kAzXEffbxWVRQM8x4N1rUMr7L3M8spW3C9MaQ8_6au9zPXaOLz-MHT7UMSDtB1hbxQFRIIdjub5NNlYqYw6AdO1vMrZlG8u3aRlri11Bg_Juq2H5VaVoGPHWZS3P5_waWFQe271L789-Rt-79yuwYk5oB-ow4e_5NWx1HvhQlYiDvEfhqKtKa0qme2rNr9YO1nW2V7AXzZAxrgsaRCDZe_b7y7Fr2tTt3JwlKcwjtvhsdVj5jWtQpcsDnGKI7FfmYMZ6vX7YqZMbuLf1tIH20KOyVzee4frVG0PhRFfftxZkVGtH7N9iqB99jg2_gY1Zraekrft7rYQAr1CEPDpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=OZYtT5aBI9W29uBG2ZhrV6UCYpQCV9cN0cPmfvtgASBGhThme-jyORyYn9hThzd5eM1SgJCUzZqiKE9nX4WqT7VtGY1EJvVecQpJ7wgWlUmxHJCXW-GxAUxgvnCnGujWEzVKpebLSmlgN6LT9yedx9427BEusgXsxlEN-xDjE_eV7CkrXtbvtpnIx5qw51w2ZXH2PuEtSeU2Im7-vhjdjX8T90JUxsY43ihFmh4VAQXah1Y0Uprx2I2JCknb6J6dvKEbat5ygan0upr5Q6p3ryGfYyuOyXzlfs2sZwbRVXm63r1eQD8ZQLAcqjfjwFZrSlEKwd_2Kq6HnZSEWELI7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=OZYtT5aBI9W29uBG2ZhrV6UCYpQCV9cN0cPmfvtgASBGhThme-jyORyYn9hThzd5eM1SgJCUzZqiKE9nX4WqT7VtGY1EJvVecQpJ7wgWlUmxHJCXW-GxAUxgvnCnGujWEzVKpebLSmlgN6LT9yedx9427BEusgXsxlEN-xDjE_eV7CkrXtbvtpnIx5qw51w2ZXH2PuEtSeU2Im7-vhjdjX8T90JUxsY43ihFmh4VAQXah1Y0Uprx2I2JCknb6J6dvKEbat5ygan0upr5Q6p3ryGfYyuOyXzlfs2sZwbRVXm63r1eQD8ZQLAcqjfjwFZrSlEKwd_2Kq6HnZSEWELI7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXoWhBKtovzGHFHJ5v5rBXx3XSD0yzmzTZC-j3TzcL6MHaEHj5RiiUyiNKnP5wkuEjewLEcMIxuhueN4uizjhn-HMMnCzrX0GqV13St2_tyc50T10a_1If0jDvG4w5XWefA0R8IaNSOW0XpNa1wSOFEs4twqaIRjndzz8qgV0HaPWdEHjoX8LETYrMpr84slWVgVII2UESWh5nKJr6wOcoQnUN2Jsa2kUazXezSpAndqWcYO0UqPSX10ov_HCVIgWTEs6GaHscRGZr3upUlvLyYm9_dbAwMVqr4uSLlcJvwAEA2_ekHMx0cvDYyv2T8f_lfGTiYWQXvqVLnYroVeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC1swOP9XVnhWFcv8C0rsjpSUNyFgCt6gqMIJjO3bHy_Mx_yZqLdHyMH_uOrOMkXlhiB2XLNlW61nOWaHccwk4tK44nsOqgpHArMkjJtPqYsXdnJ0qMy4Ja-yiJ2viE3Lr1HDV5SEWtJGiv3JFGdX0eE1hT-XFSZMvVkuquO2Dee_K-_rQhycwbNtyEpYVqMcklzJQ6e4V6BBmLb-n_GttZBbHZTePL1jRmLVBPmDsuk5wbx8VdRaMGxPjnELFuFvFUuiN21zQpOLTYqKsF-Ofwl10e-Oa3pqhgi9jVSj6tJh47xhZvIy8jArCyEQGp4YT6EY0bpbNJdRWKQeqwUyg.jpg" alt="photo" loading="lazy"/></div>
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
