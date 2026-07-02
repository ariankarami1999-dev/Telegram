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
<img src="https://cdn4.telesco.pe/file/itHaiWTdT-1XahCcpvQx1PKObiRfl8PodXuHeXFzckzdv9l4L01SFYJayHqweelnjKMYb6lPbNC5rz3ZRiyOMEYXJlLBOsuVp4y7m_7u2tPtM5EBFjRD_5UdE-fxqaeIwqgVJsh1_jUfg5N48pUBPtLgp2j-XLqbF8eHncQX5Zgi72qqCld-7A7f2iWO7HGWS23J9NUMe7DvT9_ZbenGlDCXPHgV_MJUPKpmcHoEdcsTLQx5z1QEsAPdGdfKWLkMRS2buIy6PJo8UJw23Nm-ZpEoMQCWagyhidA4i9yFimjlUdulkSXKjngt-7wq_svcp37Jsdtn8TN_qawL8pDDmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/16298" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHkGh8B4GJSsjoKKp_N0ul_uSIr4QGA7Snu3MTQgebJAkyIuDbsE6kW3XATWCqZvJ3C3V-pticX56sfkdxcGX1Snz2u0uFWfZ2RjrYkCG1WrJe82ItbcbWx3YqpgQ7aCJrqBmvKbPqwuveK74YdTHBBjK3P-3W7Phvf4NBqX6c9UtwmdFbWF11ybLOPytDJMKxiWHJHZrHfahCx-6j8gjL_B_mnp6l7PNbduw-7H-vQm8uttn_WFI9JOf0tvJNeDbFAftxRP1h7rf9VI9Abqmhb0mg4W53tEasAy1t1To4BSTTZ2MMYVXDJ5Z_YLtat4tvvxY90g0MjoWp9dZZqXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق نظرسنجی شورای جهانی طلا از ۶۹ بانک مرکزی، رکورد ۹۰٪ از بانک‌های مرکزی عملکرد طلا در زمان‌های بحران را به عنوان عامل کلیدی در تصمیم خود برای نگهداری طلا ذکر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/16297" target="_blank">📅 00:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=s8unCgRbBIc_04DHpNOq0ICHY1J-8o1ymOvbKF5zHnJS0clMrLqvnBegC60FoSJBiop56w97ADtm86RfXqu7ffSKm8Wp_oy9rXmE0Jl3b7c395hl-a-Pw2Vmw3-_3UfZTuQDLYJtYGqg7Y-LjBGpgB5j2OkhckzrDyCjfwM9GnPLsi6-HwuK_JrZG-Bk2OHBMaZQhEdTOe_22ThjpTMMOYqxrjiDGxko0vEPKvwl7sLBwaF-fW4QgZTITsuIUDlCBIocMSq2RptFldAyZblfHIgZbmf03c7Is8bw4M8FON1CtdHSwwhQmkpr4QDhDs88ZX8ozo_Q1wjWAXEmC6D_UjmHkC7szMhkECoKUUWC9zxkjUm8v-WZ2yvMZMXV8qZHAXAUqiXO5eOmqzSVW9SEg5Bx3lpGEYJ1ogoA_JUYZ5uUMg0Od4nF_n97mXq9A6Drhhs5qCqGhha7AWyuTQLi3wHOPPFpd-OnQgLdtH_haxTOUYtS6G0nPWHBPQCb8ORphP8-eZy6Rmq38_RHm2DFQwTtoRCXuSGr2HXVliax-eBRFqQNYS0yljh2Dz8uLWG_i7aVY7aorwZKFbRIppmNYLpe03MjnvqadkiiAOOmyAxyocwSdQK84R_8GZPb1YR0SqKLGeeOniyxGVyWmZ8iCld4K7Px4vrurFn1PUuT4cE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=s8unCgRbBIc_04DHpNOq0ICHY1J-8o1ymOvbKF5zHnJS0clMrLqvnBegC60FoSJBiop56w97ADtm86RfXqu7ffSKm8Wp_oy9rXmE0Jl3b7c395hl-a-Pw2Vmw3-_3UfZTuQDLYJtYGqg7Y-LjBGpgB5j2OkhckzrDyCjfwM9GnPLsi6-HwuK_JrZG-Bk2OHBMaZQhEdTOe_22ThjpTMMOYqxrjiDGxko0vEPKvwl7sLBwaF-fW4QgZTITsuIUDlCBIocMSq2RptFldAyZblfHIgZbmf03c7Is8bw4M8FON1CtdHSwwhQmkpr4QDhDs88ZX8ozo_Q1wjWAXEmC6D_UjmHkC7szMhkECoKUUWC9zxkjUm8v-WZ2yvMZMXV8qZHAXAUqiXO5eOmqzSVW9SEg5Bx3lpGEYJ1ogoA_JUYZ5uUMg0Od4nF_n97mXq9A6Drhhs5qCqGhha7AWyuTQLi3wHOPPFpd-OnQgLdtH_haxTOUYtS6G0nPWHBPQCb8ORphP8-eZy6Rmq38_RHm2DFQwTtoRCXuSGr2HXVliax-eBRFqQNYS0yljh2Dz8uLWG_i7aVY7aorwZKFbRIppmNYLpe03MjnvqadkiiAOOmyAxyocwSdQK84R_8GZPb1YR0SqKLGeeOniyxGVyWmZ8iCld4K7Px4vrurFn1PUuT4cE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه آی24: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/16296" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=JXebRMVEuDFi9fJ9y-ypsMQfb9kr_eXfjPaKH8FFCsbz6dUe6ML1ZHon9AjfxyB3rCSiHR7wiUIFntwlqK8HK9Y79MyXOS_vHpkuV7ILgaYCQbDqAecLFoQdpq6vWQ6Pt1_u8OHqg1Ays3C1WoMNFG4c9Ym0eGFRiIlj4cSCNDedNQ2GnjdYjUvZJl4apOo-2jglgYlLETuLUicBFcd5iD-P8btCDcum-Xm-jqVq31TBgBsae9E_f2c4t0cjB5BciMFxyUIOHH4Eu1cWZ6ila1ceN8kql8lfQlf353QFeZbqcT-CQjFFJYikz_9jZovAEw4mS-l_mY53kP9RjOKOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=JXebRMVEuDFi9fJ9y-ypsMQfb9kr_eXfjPaKH8FFCsbz6dUe6ML1ZHon9AjfxyB3rCSiHR7wiUIFntwlqK8HK9Y79MyXOS_vHpkuV7ILgaYCQbDqAecLFoQdpq6vWQ6Pt1_u8OHqg1Ays3C1WoMNFG4c9Ym0eGFRiIlj4cSCNDedNQ2GnjdYjUvZJl4apOo-2jglgYlLETuLUicBFcd5iD-P8btCDcum-Xm-jqVq31TBgBsae9E_f2c4t0cjB5BciMFxyUIOHH4Eu1cWZ6ila1ceN8kql8lfQlf353QFeZbqcT-CQjFFJYikz_9jZovAEw4mS-l_mY53kP9RjOKOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16295" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16294" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=ndutm7rdYJqBHQeTGkuImU9wkJWen8rWL-TiNO5Cnz5089mED99AbKrcDs4rATa8yv-Cjpra74UT4GZQPNJJt_dz5pi75oOVaMFL5IJrYGz2lL4wtCDBpEzBZqOh0jfb3G1R3iNs8L5qg8xJCbXOCOV2uyqygWmOpDFzORuwvRka440_VLbSLSfF-Rha9Gn0_R9QJLeZ9InFSapkOyUGt16ym_yFvB6hdZgk-TSMlUB0GNHVB-PBXWP6_J-KzebkNRKqjZmTPthudkbMv8O46gbpQNeX6OUPlhaDyTeF7q5WZhipCvBmJDsy4mfbHLX_SVSdBs2BBZaV5mC8mxpusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=ndutm7rdYJqBHQeTGkuImU9wkJWen8rWL-TiNO5Cnz5089mED99AbKrcDs4rATa8yv-Cjpra74UT4GZQPNJJt_dz5pi75oOVaMFL5IJrYGz2lL4wtCDBpEzBZqOh0jfb3G1R3iNs8L5qg8xJCbXOCOV2uyqygWmOpDFzORuwvRka440_VLbSLSfF-Rha9Gn0_R9QJLeZ9InFSapkOyUGt16ym_yFvB6hdZgk-TSMlUB0GNHVB-PBXWP6_J-KzebkNRKqjZmTPthudkbMv8O46gbpQNeX6OUPlhaDyTeF7q5WZhipCvBmJDsy4mfbHLX_SVSdBs2BBZaV5mC8mxpusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر ژئوپلیتیک چینی: امضای تفاهم توسط ترامپ، فقط برای عبور از گرمای تابستان منطقه است!
۶۰ هزار سرباز آمریکایی آماده حمله زمینی به ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16293" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16292" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK5dnKO3u-4kQoJhlt3OMx40t7DSbNfCA5LxkCvd8vFepqKlzVrVVRWOTpoDQB6YTv_OX-OFdGt1UiUaG_RSYumw7WNXUAaVbOsYlyhALKSipSadgLlcvsSW0w_HB__A3xqTHah0ikn4laIT2BKK7QbkM3bkOtXgrsUSVAUWzCfaN_IunHtl6e-VvP6qhFCJZh6vFm3bdiAlKbTSWIDzjDIEROH31Zkn2lKQ7sEv2Ez4ph19epkh0uvEJbc4KHvqu33zTNxKkfEIcrCahqfe6pMNQ3UG_SuExlFmQnqsVRVJ9lDjsgTdHUktuvJgURKNRiS6DGmPaCuAXtOWU5swOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16288">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A1jr8XALskPXIP_avJnB9xTXYazJ4fy8kaeNKMz8fglRxI-C6O8NYnWwv9uWAz0cu3nKnBS8EOaLqb6FCtQGJ34-EoOOgDy05abGwJ6SSD6K2XWZ7hsA9XuX-fL5KK0AYMYozmpQfeM571bA2oO0YfQ_Y4m1Jzztaaa-UOBCnoiCi4VHd0Fc86T-Bpr7aW0wIIFoC0cKddJxYeGXzLqqZFwvHtw2F2xZPKQUs3Ep6EzJGUimb1cpJINgKVP6uu68hyBZPvcwrJThuc0FFQRmioT6HmdVHns9fIw0S5MQQYt8E7yL-U7Q0_nufeTctsbtdMCw6GRvGDqFH12BO2D6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=A1jr8XALskPXIP_avJnB9xTXYazJ4fy8kaeNKMz8fglRxI-C6O8NYnWwv9uWAz0cu3nKnBS8EOaLqb6FCtQGJ34-EoOOgDy05abGwJ6SSD6K2XWZ7hsA9XuX-fL5KK0AYMYozmpQfeM571bA2oO0YfQ_Y4m1Jzztaaa-UOBCnoiCi4VHd0Fc86T-Bpr7aW0wIIFoC0cKddJxYeGXzLqqZFwvHtw2F2xZPKQUs3Ep6EzJGUimb1cpJINgKVP6uu68hyBZPvcwrJThuc0FFQRmioT6HmdVHns9fIw0S5MQQYt8E7yL-U7Q0_nufeTctsbtdMCw6GRvGDqFH12BO2D6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان پرزیدنت ترامپ توسط سوارکاران خشن (Rough Riders) تا کتابخانه ریاست‌جمهوری تئودور روزولت همراهی شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=JwzTY9f0f1Lq8DDoFvADTBaUQkgecX8YHM-1d00s3Qe3r1wweqrLaf6rw7uDfJXQYX5KPPgai1PmUIzMs__WuedplAGx2YA6z-dJGqzi9oN87NcuNiAMeAWGnn33EFpRy6bT-chp-WUcPUkofU-BQg5ATG18TjCvhz8C5rl7UQrYudPxcdAV3-g_8pGzhwV56aIUHbLWqRqkkeDcOpcS0PYV6XRnS4YXlVYdaj99FiZjwmCCNddJCtVt10R_8jjzlbeRGLtPNh0aG4SsmmRSM2zkRutpNbLjUqKt5B_Mdy8sPXoYT_edCwtFAXv25G0LJpNt17c9mObegLMN4O0t0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=JwzTY9f0f1Lq8DDoFvADTBaUQkgecX8YHM-1d00s3Qe3r1wweqrLaf6rw7uDfJXQYX5KPPgai1PmUIzMs__WuedplAGx2YA6z-dJGqzi9oN87NcuNiAMeAWGnn33EFpRy6bT-chp-WUcPUkofU-BQg5ATG18TjCvhz8C5rl7UQrYudPxcdAV3-g_8pGzhwV56aIUHbLWqRqkkeDcOpcS0PYV6XRnS4YXlVYdaj99FiZjwmCCNddJCtVt10R_8jjzlbeRGLtPNh0aG4SsmmRSM2zkRutpNbLjUqKt5B_Mdy8sPXoYT_edCwtFAXv25G0LJpNt17c9mObegLMN4O0t0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروز کریمی روی آنتن زنده صداوسیما: قلعه نویی 5 سانت و 10 سانت رو تحمل کرد ولی 30 سانت رو میخواد کجاش بذاره؟!
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8VtvNrKhstWxkp8e4QynIAW3gr9Dy6zlgq27dH8KL5OtTuq7AFe0p0L7O_VIJWIRrdODJmtnvtVRgsyP4PjBuJQz0unxI40ezQCznagI-_dOUPOlYpy3E3chniLc4eisX-t0q7GBkxHsStD_yhNPfrdoW2SuQ6fpzjfL197R8Lpa0iVd-Mzxje10fTcJpVntyd3dgwlbcr7JGp262J2NCbcFjHV1ES595CQRHdnxklvZBvFP7o9GotD-ORBcM9YBV217Q4cvZ5MJUjd_Du6AeQ8cvAL20DP4vmhPyiUcgCdSnHAKBqvTECaFt4V0c8pv0zhWkfrc72kfCHqiIsP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuM9QkdqVrUYQtwWBGfZCw8pnICOumxmmY5EkZtObm4tZepQK4XdEkZQufM1hAFq6SOXC8G0DCtZhCIXoGRlGBnEsaXHT3Pald2PdubYOQpxSROIFh5808u8Ea8WNxdagSDs7Y8P09kaNL5lBbQlOqjZKwLTBW7YVrEBY_iCxvRtOm2NpL0S6t2K0Uhtj60H_eM3u7Zgr3NS8ij8ER4RnAfhwK88MMApyTI9Mo3k_cI6pyYgqGLlsi0zyoU0JxY4G398iWk1lw87Ba4QiHxtUoxLLZaxPKYjdzVVcymT6ep_XAurZYtBYbmr2tnMdyXd9KawOoryGoi3AHvihCIb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=lGuFHG3ND-tGgCF7iQrO8S4w3oKwBxoCfMEp7r6fTPZa51O-sB1IyWgeRXgnZUzwUmdl1-lzBxYrHgmtGVIx81apWfDazXoIylA1NC-rz1PU4AxPd93wEoGMWIlo9bCRFkRVm79hyT236OsXGJUwoPBf5tJ0wDTuZO2wrvHSMM5XsScTuPkXuaJMJ5Wy50SH_cgqCa9hiXgK2fbKhnLBrvseWj3mNxMFSy9BH41mypE3wgrKL8mDwbqTB8qrA3l8DWkBEq6uu9_eV2pTQGwTMQvN80cr1tbwW7uaGc8AHxC4RE3vl1vS9x7U-ad84WUNEasbnQ-PZmr5J9UHzKSb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=lGuFHG3ND-tGgCF7iQrO8S4w3oKwBxoCfMEp7r6fTPZa51O-sB1IyWgeRXgnZUzwUmdl1-lzBxYrHgmtGVIx81apWfDazXoIylA1NC-rz1PU4AxPd93wEoGMWIlo9bCRFkRVm79hyT236OsXGJUwoPBf5tJ0wDTuZO2wrvHSMM5XsScTuPkXuaJMJ5Wy50SH_cgqCa9hiXgK2fbKhnLBrvseWj3mNxMFSy9BH41mypE3wgrKL8mDwbqTB8qrA3l8DWkBEq6uu9_eV2pTQGwTMQvN80cr1tbwW7uaGc8AHxC4RE3vl1vS9x7U-ad84WUNEasbnQ-PZmr5J9UHzKSb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش آمریکا:
امروز ، ساعت ۳:۳۰ بامداد به وقت شرق آمریکا، خدمه یک بالگرد MH-60S Sea Hawk متعلق به ناو هواپیمابر USS George H.W. Bush در دریای عرب فرود اضطراری انجام دادند.
هیچ نشانه‌ای وجود ندارد که این حادثه ناشی از اقدام خصمانه بوده باشد.
سه نفر از چهار خدمه نجات یافته‌اند و در وضعیت پایدار روی عرشه ناو USS George H.W. Bush قرار دارند.
یگان‌های نیروی دریایی آمریکا در منطقه همچنان در حال جست‌وجو برای یافتن عضو مفقود باقی‌مانده هستند و علت حادثه در حال بررسی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7L_zloAEONLXt1aRI51FSXJnUL-UsQ4ZBxjmi4jm2vg9WW6ALaeH9qVFXKsl1XDGz3J83W3Ib0nmOU25_UQvwGkSsVu5iNNZMw3RZHvQ9JtV3rRQAS1l0PgW5OezYjkFdwJD1BguuS8V3E9bQ5NRJViwlYpD1pKHl7CUoc2yreV923Yw8Pp1lqzO4jAUrUMzMhFrIF67wiv3xn1p-rskjrgAvemQdgr7Xviwg4rFHZnabK2DOwMaRbQIFbV0JqVLAIW6aSqQEAUimpxuWn4r4ctpaP8GtBfuYLXN1VuM_nxUrk2sw0ymn-FU4nlbbpWuyhGNKzKis6ci_gQXrzHlBmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7L_zloAEONLXt1aRI51FSXJnUL-UsQ4ZBxjmi4jm2vg9WW6ALaeH9qVFXKsl1XDGz3J83W3Ib0nmOU25_UQvwGkSsVu5iNNZMw3RZHvQ9JtV3rRQAS1l0PgW5OezYjkFdwJD1BguuS8V3E9bQ5NRJViwlYpD1pKHl7CUoc2yreV923Yw8Pp1lqzO4jAUrUMzMhFrIF67wiv3xn1p-rskjrgAvemQdgr7Xviwg4rFHZnabK2DOwMaRbQIFbV0JqVLAIW6aSqQEAUimpxuWn4r4ctpaP8GtBfuYLXN1VuM_nxUrk2sw0ymn-FU4nlbbpWuyhGNKzKis6ci_gQXrzHlBmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=DjRTyHnA3tWtGsEwXIz0t48WXwL6hAJzDrPsaytoqtKms1ohnQ8cKeYvyXKaQzkDFkYI8oCKKNEGXa_9lmzeuhX4GW30MenAM-RRzDiQro0FbFcPmGYzQOVT6kcedBk9tjCRdMRDX-BJGhDY4-vWFesG0AtDCsu0celmkYD5LPFbsm6WtQbfT8GWMjXGNvOA-qDs-2AVoGy-Tg51JOK7P8Iuivs3uR9P6zrpFDOlR13QbMvxabB34R-IEq17iUOxJldQNB6JS2E7P2mQBcbCNiz-6G1TUFetd7ECu-A-XkUGbubY3WcGiiEiS1NRN14ANKZqpDOuF0M31VB3D3xK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=DjRTyHnA3tWtGsEwXIz0t48WXwL6hAJzDrPsaytoqtKms1ohnQ8cKeYvyXKaQzkDFkYI8oCKKNEGXa_9lmzeuhX4GW30MenAM-RRzDiQro0FbFcPmGYzQOVT6kcedBk9tjCRdMRDX-BJGhDY4-vWFesG0AtDCsu0celmkYD5LPFbsm6WtQbfT8GWMjXGNvOA-qDs-2AVoGy-Tg51JOK7P8Iuivs3uR9P6zrpFDOlR13QbMvxabB34R-IEq17iUOxJldQNB6JS2E7P2mQBcbCNiz-6G1TUFetd7ECu-A-XkUGbubY3WcGiiEiS1NRN14ANKZqpDOuF0M31VB3D3xK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXw7-TmJDQwzzyd4K5V7oq43vpaOdQA1REQmHYo_pEhrphwT_DPItBl6OxAXLPGCN8Um9OGb2qlToToNX5T5wdlUBb5mQKMFtFr3_c9reYXHyz2OKROceJCXukHlKEiImi72jl6MHuLcNogIkplLTOznvxGlv_r-012vkDbz4gB9hn2R9IfoGNdl3A8KSfnbZwi0pvNDiB2Y9om_HGnwnjCetWzRzkYKfVZvgAu7bOTOwadNa6_g1khHM7fAe_cDyZalohP7r70NQLemWFpershtBpI33lSvP5zlEHWsDIJWQjC-XJn5pT5TfGbtsXwt4CI1AWg1IyYUKrOD5nZqNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gExyb846HrdCxTf2BvlGJje8QvP30p45arLVSYYgaoCiXR7yE2y1j-N9fBYf-FDpVaxT2xk7zyQ8PcJyKSAGpuT6CKCzT5koHEN3ZK0_WuqzGLN8XjU7NK28m6QXK2zE9gJmrjPgb-qrwO0zo3XV2E35WV-qUFRW-bmqlZ3y84zCVAnInYNMs6iQLaNJ8bXmeWq4PiZCXZgksq4xKgvxoEW0-n_KALyvDqDB1KsKkrn4sNIZAh-8OnK2hdxiLzZiKyx-qPfj9uKf1KDyLJXRgQqxPYD-ZA00VF7A139wqRZNIeGjCxvpGVPvBIflyjR8JAPGR4qc5x8oIKaiHTzkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE3k5q81q5W5SWu8ZTsCuVLkNG0Iuxf4r0mvJy-jz6bJ6iZ6DclzC91_Za1Alqyfc1OKmLe4M2D1y8Y4TlHLTQthCBPA85IjaqWEbHKbsHJNJq8W2nLGd058JaOzqt3vRjwbIXeS4SuSWDovmUchlXW84oHqOjnN9Tmu6h3GaQBmSn46lPjEU2Lfz1k2yxZMGaenq_4utzp5y_deVie1RKYzoG4mBBmXlja0JFuyz31YsMZRrODBDS4eb8_ddPtcifUgbErxC0daojkPli_b-pvF1RdkMq_Qdr58lb3bMaJR09Cc97zOZ_cV-ePDI77CEd37H6dOwqI0WfJ1Q5OGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=Pij-Mi9GMhozuNgL23oUtXewXZrrwM7BfBR6w2l_8B8SJA4oHUz1XnR4V9r608-5NisY9MFoWjxcxC-SqIQ9p7B4usLxi4LyJKT_alZ0Nlhfp6OW5h5oI7KtWatdgIb7mFFL9GHDA-6erbnaFoin0l0btvbSZgRMA7OXDynFMPR4g_PrrrcZchcrWBPh8UCVjw8Q7hDIfyKG1SpOPWHfzOLuA5y2lJ4lznNvyhgyxZj5HmwuhVIi9nOmb5ZbA3Guy3JCUEt758ikMnetUTVH1sUgN9YR8lS2PlS_gkSOqgXt4JAGjudgWg1UFwa20G2u3lfeDHdCluPSqlfDF8bXghFXat7w0PYq5_LGBjU9ytrL1YUAN3vwW3DLrNQTy4GpNF1U2V-KxAxyW9tHmwFKIixkKWcF-PZ4p0ieLNC9otXMjY5Tmgsjr-T4RDr8AVeDOtqdrJZULhqF44673UIeaMXZyl-vvr6Km_3ozqbeV4Iy6JgYOyozS-lYNshqKdJlyvgNfDM1MpuDLrNwbJE4Ibn1gAfmNSyXkCShMOg-eOf3ABUQL4UIDviZobnc5KFUk-OY2ScAkP_wMEnoE7kObueKaBGwgZtn29OVpg_W-cZofzF9mJeKD0i1LQF-ny3b5NPyn0TTYKUAX6UV7iP8TjSh_gQcD2-S69lawsN3JBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=Pij-Mi9GMhozuNgL23oUtXewXZrrwM7BfBR6w2l_8B8SJA4oHUz1XnR4V9r608-5NisY9MFoWjxcxC-SqIQ9p7B4usLxi4LyJKT_alZ0Nlhfp6OW5h5oI7KtWatdgIb7mFFL9GHDA-6erbnaFoin0l0btvbSZgRMA7OXDynFMPR4g_PrrrcZchcrWBPh8UCVjw8Q7hDIfyKG1SpOPWHfzOLuA5y2lJ4lznNvyhgyxZj5HmwuhVIi9nOmb5ZbA3Guy3JCUEt758ikMnetUTVH1sUgN9YR8lS2PlS_gkSOqgXt4JAGjudgWg1UFwa20G2u3lfeDHdCluPSqlfDF8bXghFXat7w0PYq5_LGBjU9ytrL1YUAN3vwW3DLrNQTy4GpNF1U2V-KxAxyW9tHmwFKIixkKWcF-PZ4p0ieLNC9otXMjY5Tmgsjr-T4RDr8AVeDOtqdrJZULhqF44673UIeaMXZyl-vvr6Km_3ozqbeV4Iy6JgYOyozS-lYNshqKdJlyvgNfDM1MpuDLrNwbJE4Ibn1gAfmNSyXkCShMOg-eOf3ABUQL4UIDviZobnc5KFUk-OY2ScAkP_wMEnoE7kObueKaBGwgZtn29OVpg_W-cZofzF9mJeKD0i1LQF-ny3b5NPyn0TTYKUAX6UV7iP8TjSh_gQcD2-S69lawsN3JBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_ta2uWGDoEIpwvGjivb2bPuTdH3YqBdgF0cD-zR_YFGX1i8eRKIYPU-ZuR_8qADzjCUMlohJIXuDZxt6iUiXp321mjYDXcTS2BpdmtszrZFbPh6hLZKuk47N0WdHrXNaYWWkZ6lprG2Yfazbwe5iwk4EYy8-_5kBWj28siqh1xiw6JLdgtL54moZl4kblFLtIiVGoVoNJgosUD5I5Sbb7C9GXkMtBrv5h-Nu63Z3JlutzpFkI9rG6etP5KtnSeKhBkznAdJ0QOEMJRGaLUUo1VmMJPaMMWZTu0VnYf7L4-3BsGw1v6cj6I-Reo-OhXFIwd9vQaMvBtHHS5UegZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efpxdj2TIebo7vecw-DYW1ben2uXdtOn9YGpMAbGvELW5g1CU2237XAdFowo0-IZakefyAasn8K3GyK647qYqDVQ9umjA0LsPSFQ7-8ZSflHSUr-JaKTK4c6ElX8sB_u9irBPFtAljL1ZwtPZjMuu4KK0eYTFSL7Hv0NhzM_-5I9O5PR5KrZHBh3LT3JEbBp343OCXeXd75Zb07Qk5113l3wX5dTkJTQ7G03CQcp59adH0-ShGZ3jOqWDwuAtDWSq0Eg3nGWHt889V6vOWUi0IhRuxXHIQkMvn_Fc1fJCHD-sg4WZLRTTURJ58tRA4fk6ePIqZltOLmNl4r0D8fMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ppqxmfo_58Tw_kxymx-M5h6e8shK6eL89DIbLep3rJtIO9wCH02zEkUzp64BvkN2-pnmwADL7PXC2zR5XBZ_o6s7B0bw2ptfz9jyjZBR22aRTq9eP0ZFCr5VTY31bU9KttRNjvsTjhEHMAkfq_r4-fto4xY5CQKvnEnNBDL7WDfZvwgAJItNPH2ox09VprNU_mmM3rrlUcTJN5SJLodMhsVFlrZ6tRmZfDcWHTkh1iEyZIctXFliWCEHxpI1xAT8xFALRczEDaozkWyJGLO_hVEHlBHr4MVCIbMp2GXZj7Nze2aIAvdKuyqJL1vYaRAi87kZcQVT3z7wvYUPso_7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=mZCJhtFA-JOnv_MxSXD8Kz4o31aMwuNVeZiUSMnEwW4NO_AbGVQGuN_R23lfxqxhViI_x6oBsHVEvUab6Uh3PkBUHa0G8v4odKNN5mIiDiqhU47_OLLAAal_SYwPYFCxqS9w2e8VUbSPZdz3m759bdIAWEsTY4u8JSpbULyK7WZOYJF7Oc6cx_Q-lFQBt5U6cbI5sOeO_3-vtUl9n1Cb2uAFU47bzz6oaFJc72VXh1IOdM70rsTk3ViVBSVeMp8JyzL9Lh4AZ6rzbj25eMR3R4uoe6yOPL4a49NTGXHbqeqBvry94yLN5p3AiofbqJmUXlDojS8OisBuCPYUFl-adw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=mZCJhtFA-JOnv_MxSXD8Kz4o31aMwuNVeZiUSMnEwW4NO_AbGVQGuN_R23lfxqxhViI_x6oBsHVEvUab6Uh3PkBUHa0G8v4odKNN5mIiDiqhU47_OLLAAal_SYwPYFCxqS9w2e8VUbSPZdz3m759bdIAWEsTY4u8JSpbULyK7WZOYJF7Oc6cx_Q-lFQBt5U6cbI5sOeO_3-vtUl9n1Cb2uAFU47bzz6oaFJc72VXh1IOdM70rsTk3ViVBSVeMp8JyzL9Lh4AZ6rzbj25eMR3R4uoe6yOPL4a49NTGXHbqeqBvry94yLN5p3AiofbqJmUXlDojS8OisBuCPYUFl-adw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As4RN1FIUOdmMLDeSGJscQ2m8dUShLWEcdgz4FSY-OlEM5P8g4h9WmHBiJ78IYq6c5bos0j2GlrlWc7g6qdjCwSjE3_ylsMhaf2kEF04AsFG0TcKQ4zA8xhzTVpLzZK2KnjvoEezK3wn8F1z2CG5ImQjYFM4wMlAqvbdj28nmun2XjEe_XmwsZ0BtjiS2n1WAnp3wlH2y2mmsUm4Clza1jKyi4N6O22q0rFZ7_4Qb1ZzC-X987erhgW6smNo5_tmYFJcgkZ-wwwL5Z7RJaiysFmzK_Kjl16krN3Kn6-5VMYkc6dSJVgIwO9WDCANy2V01dDc1w-wa_1GY5Ld1ckI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcUUh24XU7Qb9iHs24mdp8V_3NA-N37AQSkZTzdaPTHCgkrjtiLqDePjXKoElABf-d3GXfk0vnkG7bpqQil98XJDRdqPsKIQkCvk6DEcT8uCqdc54Zp0XMDThVVVwlR7MZvt9pYwzaLgepGhNoje4c0mC7V0bRXEHAE-Yo5eDrVx22oDBiPWvvXOmNJRhpn0oqRyDRMNZeAEaNXX2esQ7B2bIg1Tj2qI42xQUe0EIdjkIMf6jQJr-4JGAABlBcn0SG5OS6JYI-ZzEaoDMHbra6Dug_4KpleNC6suaOqmxQKq3SuvWCGExiHogw_xVwAtrF9zwG9Hl8dcCNvFUci_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-0LbyqFKNRclCia7Kpb3HzBe780GyDq7W0f2oiTnWxRSDyKghQYAWeoWrIXYPbfVNGohh6f2S91tQNpQD7XmMRX8HLcbLYIWZ6SL2Ljx_3OtFZMz_eAPhO0GJ9z1WscO0cYMyXVau2xG8AmpRdvda7v79TIL64otsaVcEvwrKOl4E1RIxaUGHTMoJ7BSKxt-GinnzfB30qrEBFm3SU-bW-cTQwJYlt3epRafkQKO2B_WqZGQd2XsHlJOvGek42agZ22PAqi4DjyfdhszczAVVVzYja9rhuTnb-5m1tXc2VM3cxDA6MiB76OAJj8jYVinb1soVUpOoPUPdH3sRkxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=pdMoCQ0hIbgfEtb6rGK06MRj7NDIGX7-VzKL9BgfHf0X0JnbbpvawWSC16ASdJ6g10Zn7xF2RaS1JOvmJEsOoIy00dTg44WqBDxTwZMgKmmQ0pgswqrCz2dy3-O5I79BBRH8QPCevO0k9sVnAvWvOEk08sXOQGnwHKQa_nio5aHqhyzoXOp9GS3I02k5zD-lxpxLCsz84Wx-lo_OscoS8_obG3OYcAcJaO4sldZMB84wchbgQPCw5n-MdTF4rCxjSDDMGHvrqf-1FoUumtMSKcugsK7WKCCABwoCjwS27jeAKf5-JRCw8q8dG3yTjWV_SKJDb-ObQipY7-ItlBXE4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=pdMoCQ0hIbgfEtb6rGK06MRj7NDIGX7-VzKL9BgfHf0X0JnbbpvawWSC16ASdJ6g10Zn7xF2RaS1JOvmJEsOoIy00dTg44WqBDxTwZMgKmmQ0pgswqrCz2dy3-O5I79BBRH8QPCevO0k9sVnAvWvOEk08sXOQGnwHKQa_nio5aHqhyzoXOp9GS3I02k5zD-lxpxLCsz84Wx-lo_OscoS8_obG3OYcAcJaO4sldZMB84wchbgQPCw5n-MdTF4rCxjSDDMGHvrqf-1FoUumtMSKcugsK7WKCCABwoCjwS27jeAKf5-JRCw8q8dG3yTjWV_SKJDb-ObQipY7-ItlBXE4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8w66r6NyD4j8EXTG_rlcGEn6R3K3LgiRcHZkivm3ISKpP6ZuQqaibKX1R6yY0QFioLtjG_tJ5wXn0uE1eTMX9A4VdcQCXtbv7fufJp-ZOQzd4ESTLEs2x4XCPdLfpjKQ9DDdPt0pYGxYkF3E5jCbZBH8RG3QIkkbEYWk3GrFpaG4zWqPIc--gsqCDxUslKSoh5bGwq2GpYL4xgwhzsUCUIg3mQHBaoYhUmBImdhOopscEnTn1gsEdL9RMoHF-EgsfVlYIEgaY6NRxJdI7XpP1N7AtW9C8QXaV50iiE7A4j_WlFhl281wOmk84-j2wyazvuMCXgd3yvnp7WW3jWQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE-nkLH0I6Trld0SF5PZ4xpuq9KMW6e2fJMDBmOaZIn2w363bAd2vutocJZM4MnukvUEW8cLyyBAC2Cz015yU8WQmndM1MMkY3yC_89Qv9BhwP545_hpdm2rDY0pPJHart1ldH2YR6UNbhKjGq6DOwx14okZkbUY-guPdEeFKX8YkxBjzfpjOXd_f6IW4yI5WpYFChNUUKx6Jlv--eXzBGEsPrNA-alvqx_zwssEV3GSdiRE6DHcd9K9rFqcCJTt6NYJEfs5v6U4fq2HKHfp2E6QNbsarl64E3NcMiKs87493ODe6yvNMaloBigDU0UnEuK_p4XCMIKr9YVb4lLoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn0AtDEESx03_afMihtlq__uNbgAusK-slfCX4cfRaCS5xo8l0qI8AVDA46W2S0Oyqz3dSsthkW-0NwGz-QsvQ8M8tgE3uzI-2VPfN741uig6hiMFABV6-qsqRxY2ffS4ztVDI8NKKlXv-KmfutYS3icXFErM2NL40-EmDruSuCqULS4NHAC75NLzB3ZBCPec-lmzEPSS-9Cpamt0zvqsgsD5t7o3ORvKD07Xrz-aOLoQfv1veCoiy19y2ccaRFy5It-mdD--7HCAtDBQuzAanuXenjjmBny49_5dJJ76A89cOesxOXwbG9M_GKz3MGUiLil2SksL40Wxt7GbR_r5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=SP0k84V5c9UNfaG1dQjvCMvLBPjod22cbcrKTtBNqGjqIUrnKaj6YMzkve20SJ96MMBY717mnqlbEKuiuqnS9ooWK4LgduEPmK9fQzbOosybaNrigGnl1aWnczvZTPQI_jSt9-cCpp20D0LXAvXm2Rx_9VVoJYyevjH92k7wLJ-vzLM4kDYlMHTsEfIFwMFstnIw7PbchsBkLiTN48yzxNetX2u1HZWLo6L3gF0ndgeVSInsD9V05emyJVw1l4WWME9cCodp1iZE2NFDW6jqJYaeHL3zTJFbGHMg4H0igZlCeZ1RgV_FtuvbZP9Xa5jyOLEE-jCGLKKc25QgXGaXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=SP0k84V5c9UNfaG1dQjvCMvLBPjod22cbcrKTtBNqGjqIUrnKaj6YMzkve20SJ96MMBY717mnqlbEKuiuqnS9ooWK4LgduEPmK9fQzbOosybaNrigGnl1aWnczvZTPQI_jSt9-cCpp20D0LXAvXm2Rx_9VVoJYyevjH92k7wLJ-vzLM4kDYlMHTsEfIFwMFstnIw7PbchsBkLiTN48yzxNetX2u1HZWLo6L3gF0ndgeVSInsD9V05emyJVw1l4WWME9cCodp1iZE2NFDW6jqJYaeHL3zTJFbGHMg4H0igZlCeZ1RgV_FtuvbZP9Xa5jyOLEE-jCGLKKc25QgXGaXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVP26RbEoEiKOvftheRSSJh98FIHs-spzlOqagqq9kDpG2G2Ea9gyrk8I5OWv3gnErqaqExfT0mKgxv9TVeW66GHpsGISvqrQ6Yi_O3sz-20TJgCkmG_ghgEpS9qn1V8o1ND6KKzbmanylrp2urELeEDcLzb5ez17oEsQz92Omn9SSlzjw4XYTL4gEtDn4TvWbIWO_e27UtPJzmshju_KhZhqTsogawk0Xu1kdTAgyXPwYK5G20nHsHGlj53TsjH31_3_XWCcR2ZV4Ck6t_aFzOhieCbTE-OowracfeOg7pYXHcZbVBdMybB3AtzmuWsMRNafOkKRBa7G0HmEOjaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=u8c0Odf1xDgsglHqPJj6PJ1i5rmomL8m6y8N3D4MWUXKkvGC6R2LF-YxloftLePekDty3ptpX22o8A8RJu6MK7Gixlh84auTbAAgcJm86QbtHRF9FmVOJRPqUhE4n6CyHKsotXJpdlTo05M23Fa5v1o-edf-ShMY-1p6vBLtEk0J8d0ocG1P63tem3DpRe1lmXW7HVV3p_evWHdeZt7q95ISZM_seLQJSgaukoq5ivq5wIH109FkfUTjFdsgIF1RBwPwZzn1hcNHY3i4O8Iuz-dSL_3cfS94537VXHATbCg0Z3JAeUNRmfbHjl3D4I8Sx0DBYhfZP_i-N6BGH1rb3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=u8c0Odf1xDgsglHqPJj6PJ1i5rmomL8m6y8N3D4MWUXKkvGC6R2LF-YxloftLePekDty3ptpX22o8A8RJu6MK7Gixlh84auTbAAgcJm86QbtHRF9FmVOJRPqUhE4n6CyHKsotXJpdlTo05M23Fa5v1o-edf-ShMY-1p6vBLtEk0J8d0ocG1P63tem3DpRe1lmXW7HVV3p_evWHdeZt7q95ISZM_seLQJSgaukoq5ivq5wIH109FkfUTjFdsgIF1RBwPwZzn1hcNHY3i4O8Iuz-dSL_3cfS94537VXHATbCg0Z3JAeUNRmfbHjl3D4I8Sx0DBYhfZP_i-N6BGH1rb3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0ekXJ20CbtHIPh0htrTOIXM2mKIvdf0weHLazdcDioQaiCT32LYCzjpRckEB3GFfFsUMxARQZxKo8w8tFR9kTleXTvF1qi5Bs-hRMvG8XnTo2K3sDWc90-Cx0x26TEfLH62q2KG3K4I_1AudOpTtKVUSkZ3-Ozv4XJGoxg7sh4VEJr4gdm0Dgk_-ro9Yhih1DGAdhz-fYnzD8UYNoCL4S975xDlaQwEaR9QgYFx3PEI3HYhPFuM6bkDL_xzhw4HiUQ2PHrLu-bPE32hPGF0b5Ggexx2CPtH9D7SSUdhmi5QBzUg9xZTkN3vmMLPhA1hKTcdr6QG_nuJkCBSIK84Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqjfmBhEOdfvPt_HCF3JtIuVB7Z-n3cbBYBldRKOR-pcskllFBxuBfjuozmNDuIPQS2Kg3LQBjy2y9MREtYkDUR0wPyNHPmZ39xVB5i0kQBpcCgsxelswspJdTxeXb7ToEDaoEyz_UDM_x4GGFxWei0T9jy8zLHKQwDlF1OlxXHB2Eibb2aRwF0SmBCv4O1KMZJXGhVh5dZYRLLIKGuFnI8ypSomySyhQpVJALXQPCorChCIC4pRkTXirFWFTm086qglDzpR_o9TtAE9GR3k--N6DcZ0yl0D6TltAjDsIHk51YHfPJIpmckM48bMFZJqpOicpZhYhm40b5asQmUIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eshU-7D4vcVo_sqkgO1cqcDpEctfZATzvDTR41ooPtNcA8qb2nfLOn7LweaAg8GYwd04cZG7rMDA_ww5_cmpdu2RPmKBQL8xhwuOlQdsEKyGSeZGYxDW1dviTP0Xew2U2WSQ56Vczfj_ChgReFd4dB0O42kGeUC4TGeGGw7VLbFXIy2YTGfDSFsER58CXOh7FFxxqcHLEFz1-NM01wv-U6A1TghWCl7iIhwdObIHNtJCrbe-5_MXaO1Hl_GXFPVdBuGzxJhxZ_kwn6j4a6GaZHwIeuL4OdaywWTWGAMa4ot4p0Rd8zBmA73-n91qZ4arNQaI0VaBuHvkRQ-nsMfVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyToUjqsqHD0lkUEG-Wb2pZ7PVRLLVZTYw4-mpqGU05sX7Pgk73FTjOy16UMOS5JCF-Ec2s50SDT31AjXyynB0qKv5ATHPuq5N3oEx2V0pD_VQfQZvK6NYKNXqXFDBYtCvtB061qoVBeJAycNYxKTRoZTkaVYC4SH_MbD55MJD7MJC37Mq_D8ivssqKdlFaSc6aGDaptDuD5tKLRKTCdLAlR7_4Pfe_echbkyNTXXtRZZPVojxaPo1LrBVW19Aq0htuZ7aW1tlj-YwNWQbK9qQ7ra2tGOMiNywEMSUxGbMfkO7DU3crbGBWqmb9qMomNxLuM7sjdb2-ogD5OOurG41UN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyToUjqsqHD0lkUEG-Wb2pZ7PVRLLVZTYw4-mpqGU05sX7Pgk73FTjOy16UMOS5JCF-Ec2s50SDT31AjXyynB0qKv5ATHPuq5N3oEx2V0pD_VQfQZvK6NYKNXqXFDBYtCvtB061qoVBeJAycNYxKTRoZTkaVYC4SH_MbD55MJD7MJC37Mq_D8ivssqKdlFaSc6aGDaptDuD5tKLRKTCdLAlR7_4Pfe_echbkyNTXXtRZZPVojxaPo1LrBVW19Aq0htuZ7aW1tlj-YwNWQbK9qQ7ra2tGOMiNywEMSUxGbMfkO7DU3crbGBWqmb9qMomNxLuM7sjdb2-ogD5OOurG41UN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
