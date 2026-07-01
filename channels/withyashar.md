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
<img src="https://cdn4.telesco.pe/file/Sh_oQ_zrKPH5aEEo_UHIkHmH4ohkX1KR4MgYFCYvn9QlX2PzCYPFnD-d4MYSKlo7ZtpWkjqFnbK54kWzJIGARLUdef5dkc1zBOhNl-1dEi9SWtogSSxxpDYbUrnn_C6Y8qwMG1d8Auofk5yJawccRL29wVE0zGv9qyC3_6hfWBgaMkoH-TGadSadhCVWHiuwJhAKuAvFMVkxs5xqfkF2lM9AyiK7QN1fnOKY3mGG0LKITp9gKq5FOG4btqrwhRpDC0VE9keN-QkilQ351WFaKDAtQ2F1Ern5snhIU0Tz6Apv9bacXS3OP73D_kK9wt_GhAKpqTR0z4Xwl0QBu69vvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 03:19:44</div>
<hr>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/16298" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHkGh8B4GJSsjoKKp_N0ul_uSIr4QGA7Snu3MTQgebJAkyIuDbsE6kW3XATWCqZvJ3C3V-pticX56sfkdxcGX1Snz2u0uFWfZ2RjrYkCG1WrJe82ItbcbWx3YqpgQ7aCJrqBmvKbPqwuveK74YdTHBBjK3P-3W7Phvf4NBqX6c9UtwmdFbWF11ybLOPytDJMKxiWHJHZrHfahCx-6j8gjL_B_mnp6l7PNbduw-7H-vQm8uttn_WFI9JOf0tvJNeDbFAftxRP1h7rf9VI9Abqmhb0mg4W53tEasAy1t1To4BSTTZ2MMYVXDJ5Z_YLtat4tvvxY90g0MjoWp9dZZqXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق نظرسنجی شورای جهانی طلا از ۶۹ بانک مرکزی، رکورد ۹۰٪ از بانک‌های مرکزی عملکرد طلا در زمان‌های بحران را به عنوان عامل کلیدی در تصمیم خود برای نگهداری طلا ذکر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/16297" target="_blank">📅 00:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/16296" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/16295" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/16294" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/16293" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/16292" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK5dnKO3u-4kQoJhlt3OMx40t7DSbNfCA5LxkCvd8vFepqKlzVrVVRWOTpoDQB6YTv_OX-OFdGt1UiUaG_RSYumw7WNXUAaVbOsYlyhALKSipSadgLlcvsSW0w_HB__A3xqTHah0ikn4laIT2BKK7QbkM3bkOtXgrsUSVAUWzCfaN_IunHtl6e-VvP6qhFCJZh6vFm3bdiAlKbTSWIDzjDIEROH31Zkn2lKQ7sEv2Ez4ph19epkh0uvEJbc4KHvqu33zTNxKkfEIcrCahqfe6pMNQ3UG_SuExlFmQnqsVRVJ9lDjsgTdHUktuvJgURKNRiS6DGmPaCuAXtOWU5swOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8VtvNrKhstWxkp8e4QynIAW3gr9Dy6zlgq27dH8KL5OtTuq7AFe0p0L7O_VIJWIRrdODJmtnvtVRgsyP4PjBuJQz0unxI40ezQCznagI-_dOUPOlYpy3E3chniLc4eisX-t0q7GBkxHsStD_yhNPfrdoW2SuQ6fpzjfL197R8Lpa0iVd-Mzxje10fTcJpVntyd3dgwlbcr7JGp262J2NCbcFjHV1ES595CQRHdnxklvZBvFP7o9GotD-ORBcM9YBV217Q4cvZ5MJUjd_Du6AeQ8cvAL20DP4vmhPyiUcgCdSnHAKBqvTECaFt4V0c8pv0zhWkfrc72kfCHqiIsP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOrvBE_9BlVjiZtWiaHXQkLvhQLg1e3N8X8m7nLtlkTn4gaQ59OOI37aLso2OWRBLZ7FD1n8rRaUbIBUz4YD4tTvuXIY3oIRqZJG7DDQNc_R1cJb4pL8qSr6fASEBNrweBLMM_O-KvWfAzd02wscJ_F72EmrXMt7RwsAu4ikjP32LG7CCRqOhQ-nQ15IDjIrzSYOWkYz20LRoqz_wOM_D407W0xOBWZA1JNjHG4Gsm9NrTdnX0nbtgCQN9HKXyaWMZ4FXx3ZS6JMnl3OXkNb8-4FdsHI94HmXambstBjE4vhkJFe8L1JA6I0YVR8KpwFY5WhyX7qVb0e3NGhmC8ggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=LrBvxTqAkL6gMDa_BZIOVpooSGhdfPNxywlIFNgSMkJM6akD_Db4IfD7zaxUDzHfHtfZVaowvAoVcDplPV5KxjrwR1cM0a0vt-QMPY7ANyVOoR6pgUXSKooqfp6C0ByoCvwfoUOBw96cPnJWzuHwLrA78YX8-M0K4U2cAHt0ORynMBgNr5ZabaeDvESmFerLiAoeiLgbjfJcdeeUlkZ04WZ7Wi2DS2TFe0s_FlBM0l2edhXvDnk6dyz78eBXQNYLubJWohSXc3nKXURw2gNOQuSYLiYHOO-9AXvthMXtumCW4BPpOF8vqkgR_nr4BYRh3z49cB28n5aKdZHh5nL7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=LrBvxTqAkL6gMDa_BZIOVpooSGhdfPNxywlIFNgSMkJM6akD_Db4IfD7zaxUDzHfHtfZVaowvAoVcDplPV5KxjrwR1cM0a0vt-QMPY7ANyVOoR6pgUXSKooqfp6C0ByoCvwfoUOBw96cPnJWzuHwLrA78YX8-M0K4U2cAHt0ORynMBgNr5ZabaeDvESmFerLiAoeiLgbjfJcdeeUlkZ04WZ7Wi2DS2TFe0s_FlBM0l2edhXvDnk6dyz78eBXQNYLubJWohSXc3nKXURw2gNOQuSYLiYHOO-9AXvthMXtumCW4BPpOF8vqkgR_nr4BYRh3z49cB28n5aKdZHh5nL7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/untiPDhkPz02LTDniS_l06qPZe-mudXRRT2wusS48C3ELyfyiLaF01_K_pZvkNVOeXtI6CT-psYWfilJFR2l6vPoPNjaxSEI6tOujOGH-hfG_wCx0Z06k3U2DzUtgnuuvJJAzK65CidSIB2r64vikd6EsN7qO0qsi-DGf_BKWegwBKrhqBMNLExcYsCdmPMOYne7BwKO2uXcqgM9iHfC7WAGPMIC1vbcgnGtmkijC53kblkHM-tGj1SDnKYHIiB5EXBh4_HbJ0fQrf0uCuH9BD0erfQxg88kTyFzuraiQ_eSBOnpzGgxbR7ZYzFSyyJakDuKvIFHJYHp_GygiwaK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M-QQsEkXfGNBBM8-P6t1ogKbU2nU0-D5HsNDQ6WURD9bQTcW0R57H7yNTdWZz6ctiuK-k0ObyXafZF6AuHF2zt13Vr1rIoYzdeADg6Fypr8k34QdNvH2KYyyG-XFX2aWLSxlYPH7VAWW6D_ebp2Ta6pgu-ePJg7Tuu8G5Q4OzpqzvvgvZvLqMAmtJTEOzRVSczi3YmZblzyumNkmc0DX5nJU-LZlhthm9cHhqb99ij7YTg9rUGwx5YmddnwkbuLK8oyxPjpnyN6UFnMcKU3y1J_pNAswxY7SJNAtCZL-h2SrbsTTUNcOz4s8VrlWJZ9anOrGtO82bG2fINM_Z0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr76KORnnL18JKTeGHziyjGkimCmzANHwCwDGXc2rffFPyOEXz-mJe4EnSExkO_Jiq0jteqtYXNZIuUH9drOIOE7AZ_WV499ZEaHQZLreTnmJdfSpkoUqwZxMDrBrJ8BiUNl7FKVS2GlZDLZgYsMudObid8l2e-wCIaMLRIPhzK4rPUu43t2T-5dJTHNGezINhGQEhJJAQFqTvQCBMNi-LpK95LbH8ERNcWBhuw0s9myW7ShEj06vJA3j1monxsXaRD4-S6RwMsGAv93md-6soOLg5Pp6iKnl_1FHnqooGHnlRbxRaxiusvLWXOqAcRL5zrXITdOXh2kxe9UQ6ceWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkqxtZRrSy9--sKJr8DMW-p1IjgYgRlTw6I49APJEk_-YyWPAoPFb45INX_i0cKWx7KVnzRjn-4OHPfY8YP1GqzeBb5f-T6O6yfpynxtLyHP7VXUBiG2YfHg2VTkfX9b0JGwUoSKA7rmGV8xbP8bCIlAm1fJQr1m0aPv6pKVvYebpPMXcTqXkF66WA43v9iMDdw4zA_1Ti7utnfnZ9CN_4L1q9p5FRJmCzz6BMVQ4Iipnei6ZfBSSPI541SCBuOJHup-8GLz1x-NIbMBaGbkUf-9wRYw6cs6iuLMU80Z9g5PIGDQ9p1LyFrhHX808ovQGTKVPogzucdNtugETOnyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIPnEhYv6wPYzlyleIXGlbFfGVgRiBuNU1R43W1l_R0MYgEQB-2LltZalrOJ5FrPfYbL-GrjPzNPIwRlbSqrrKfOSpTiHfQUys9HvRuKy90JgZZdsBhd_-Qfg9KpwZyWIMu1iQeQY_lwi_rZ94JW4VIcTmQwYhHPiwQ6JfxeIr1MHq48bJ9nDVP46ROVFKYThKZLGCd5tera60Q3Iiic-1RMyYM1X3cda_Eirb4WILL_4NzuVrSh_wuykJs9muAhRhqVd6vRGpUpyLhAzRn5S6dCcNWSzcsl94miTItgszAlFINdcreoLuJ-g6hE9SeAPecsD5Xlg7sPtIIbD2HjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt6-NZbSY7OXiI296BHtQEcL5pO4MNfU-f9azP93XnlzDo6w0GkLHdlMyoHImRV5bAsDc9SSqeoL8wZvuHn-ulsYaHe6y6oXUnw5si5Vm1Z3G6CwVcgVVc5laU7GWONE9FNTYlRgWwWO-ms_Ofz4rpifSlLjRbwtbEBi5F18Z9Vr1zxbtsN0SUemvLrQiKSxlw7Ym3JmJJ9KpubIb23J7hsFE2hGX2WA4PaiFKIV7zEWzflbogZ9CR7mwyy8OlMq9c1NPnwrj3_0qKVaAdGDDzth84DgZ3yR3qVlJGhmJplgL1K9DJK9Z77CcOZ3332jbNfED2NrVilhqjY9JciH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=cl-dr4CUO5u9CYPECytMq43NXGtWfCdU_3eZCLqCf0oaQmDo1zDMyKqnjoSrjWNtMFrz_ljgajQMSYxrpY16efTZ4VbySBCqAfALlc-nFSROlVu9Ovx4JhO_CFu7GmaX5msmLVcwr5_jvUvh3kmtaPM1Gbm9i9l_ImP8rk5_SK4UYFnOPz2h5O1t1ciiCLBkd2y5T1ysaMcC0x7-4LKSnbZ6ov5FGV03KqZzQGuBhA8hgW1tssIDB5POMVdTAU8vbTUeFFI78lpz-WiYNb973o6lcKyVinsvFFonIubZLEwtaEDWKgUbv7mqNwMB_YQTLK0UgEdnx_omcYCTe41wFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=cl-dr4CUO5u9CYPECytMq43NXGtWfCdU_3eZCLqCf0oaQmDo1zDMyKqnjoSrjWNtMFrz_ljgajQMSYxrpY16efTZ4VbySBCqAfALlc-nFSROlVu9Ovx4JhO_CFu7GmaX5msmLVcwr5_jvUvh3kmtaPM1Gbm9i9l_ImP8rk5_SK4UYFnOPz2h5O1t1ciiCLBkd2y5T1ysaMcC0x7-4LKSnbZ6ov5FGV03KqZzQGuBhA8hgW1tssIDB5POMVdTAU8vbTUeFFI78lpz-WiYNb973o6lcKyVinsvFFonIubZLEwtaEDWKgUbv7mqNwMB_YQTLK0UgEdnx_omcYCTe41wFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLg6OH3LRvVbahHRA6QdU61lDFyuvrg2Y7lFBCTep1RlNLeX8097MzkEKNvwdgSnfyIMJcUaM24n5piahJ0dnH6fOLdnUmfQyx68thpUCcya_S5h4U7cicsO9AZz96HAsx8h7k7g1TbOARs5Sm8r43dz-R9J0wsMNYu0vBEBXK8XkUNGaoIZiV9ix4f4RIUt2AHZOQaUF11Bpknzm-78vBW26WaLsLnC45fBwcQXjAJ5FgJ_JA_mf5DYDs0MB_aXo1HB7_PgnaXpEhjxEOnnYRI9Bi0Y4C40RDo0jZjeGFreFNZUCwun-wULTC8klsMAguJoREWEQkG4rQi_db2liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdZnXoJdXVMtAens2CdaGzInJr9zZ5oEELwiOcf452u5PqMV6nmrpJ8MUpC7wyskvuXjBqgy63tTscXqSW9Jhomv8YmUijf-FzRnlNeI91YV3r0A9d4I4pTWjSML1JSt5Ic06u_eG79uptC6UkUJKk4Xx0AOUR8Avsh4E4NlOzmMeLQ6xsQao_v9KvMYjDEGZPvWsyVEoAbiKSrbnQuL8tnRPWrEWChHkx_-GVZQGJenrDo802ikDj_qpRLyCSEWcj1PmZ005XdqxGG8qLc56md5-L9JIXRpUrFRV6jeGDcJcoXLVcjbzQhBV2fiiYy0h0XYWW0XDe2FLmKitghJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j63s3-NiWXyZL3CpOoI7FOrvj8cJkknQA7IU94VP5jh2-lNpdy2fe0juYOF2S29oZlW6UFungC6e_uURQ1b6lPr98_og0BH7dxM_M5mhSrNI_a79RCR6GLS9zLui6_9EtWDcobM_mxOZwoV0wrbFbIn9JkRNGSZ9e3ZlzI22RQI1sSuFnDnr_5hTNnMxk0IE-F5eImA-rwm3t1qA4CyOpu2rhWxv9QnOgJ-McnHuWKRfOattiBwgI3I9okiA-Oj7DLsfDQqPN2oSACY8UbEcwkiIcnORcNN18rTWtfY8ME3u6bNlDvBYSHoW_C-epygJF0p-6YYgvawfCkJRkBbbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=LtfTHLSmsOfH9cEg2v9-eEpImXMg3H1m_bInEGwpv35KJ4MWZwGFunRvQ_ZwGSe0au-E3Mch6FTTeX_yvlvNQBAGSEbpccwSL6ONWWcx2pT3mAx75mNzIOvDZUPDVajeLXrDQaiTqe1C6GbB4whm03NNJ9cc8gA_Trhv1SigKryVs31K0rH0pfB-Fy4yKjiFMsCJmuH117YMHWhh8t1Kn1KFopcbwjcK8g7w69wfyA3Hzr1e4EzkTv2p80dGHGSbeBECC1IXQadItAH5FwXoVQLb0GLaIaYj_DHt4P9aCnc5pgzHbeRMl877ZmcmtkMff03FlKZRsC859ZCZXeil5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=LtfTHLSmsOfH9cEg2v9-eEpImXMg3H1m_bInEGwpv35KJ4MWZwGFunRvQ_ZwGSe0au-E3Mch6FTTeX_yvlvNQBAGSEbpccwSL6ONWWcx2pT3mAx75mNzIOvDZUPDVajeLXrDQaiTqe1C6GbB4whm03NNJ9cc8gA_Trhv1SigKryVs31K0rH0pfB-Fy4yKjiFMsCJmuH117YMHWhh8t1Kn1KFopcbwjcK8g7w69wfyA3Hzr1e4EzkTv2p80dGHGSbeBECC1IXQadItAH5FwXoVQLb0GLaIaYj_DHt4P9aCnc5pgzHbeRMl877ZmcmtkMff03FlKZRsC859ZCZXeil5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQgTJ6imqTVX9e6kdxjqNa4grkA2D3fmty0skr2uj62j7imTTmIXva7YohhxpfyjdxexAiVR4SlYGfwBVD9-_XOpckkKFhZDO6d9er2Z39OmFSlXIMRFiOetn9eKQ6-hANlQkp1Q-5rZ2mkBF0TCu6fq5UdnFjiMA1XhyfMh1JU2dxmctCReMUUKeYCHfIepCwornQRX_m5hqlYtr63j0d0E8-nrUaLvO8ynFnv94WSM0BUyaPjB-gUk5Ws3ge1Vrhk7rkuA3Ki4fruT-cVWLYOHjMN2B5b5KsBfeYNlPuTl_Zxb5I24X6WnRDZnhgObxqivV8UL555ZzBJ-nO53_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK8pE6GP5N0HP75Lr5HWvS25jf_3XeajGubGujQxWS6t4bfwncqzkJXpoSnkY_-Fj61Cfe5D6jlfOhO0LblurxasrDjo7-Lt0hunvy_JKzj0my8V4NAV6p7XjhCsm0NOgjiEedBKg8gT-zCFosuwUeVhv6n6liVnJ92zv3zD6DXJha1MbWt8qHr1XVBXnjohr4K1iKabWaWM-wjoLimYKL6KP1xizDJgsQemf9F0FOfp-SZIurViZ7BtZyafVCjBFIk0dXDTi6bgdFzhf0kV_WPwnVALDSIboxVUfUWf9NSSaEmXLQpZOgezueS7qp4thlMj7O6XsOvaS7oEEVmyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8MZyLmeaR_LGp0cG1Moqg0OsTIBsY-wv3uXbT53thkqpHbzdpAtxqpV1pqHhi9Us6WDI_UR28DabHTltm5SplzfynrmFr_YHA36hKJEv0T8REtOoCuThLa9oBl2gd8ATk-4rw68p7I-JTmbZLscM8rnwvzPlyS8W2rG1okzxQPSpLo1FV-bzOGFxNkXxWo2mkTJ0dPL3-kWNNq9hRng6KUAGSBjY9leAFjCtcly_PElmMOjU8h8PLk5U5ZWKLvwj2Y5-1x80R0lBxcyyKh2q3w1teqYaNU0t4cZYA6XT48522MH3_jFS00zNRcmm9luWv_8ZVX9wD8Vrz88DLFkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=mbrDzD1K-DVE66fnYyvPISHRI4bMOINF2G7X3augboDZ7G9PeB5zFsTMuS49SoVK5mwZk-pX_My5KWOFvnQmTu_9lIDluzHdtuYwjT4JHaCV5od-YubG55NZuR3oe7yfrc-dtv5fekvzo_ElDn7QEAM636gczKOZo6cu_tAS5Wz0vURK6QjaLlQleR0bggjaPFObEjh9nKOTIUosPTgUtQT2rkbAvoReRY8SPQ5JDeCK0e2l3ck3GzuarKWGtLCZGitHH7jC17hxr20MXzWZ9drUS2Z9Uew_h-IgIQlThGPKYi4q56jXgRHl_Xs-u3TXGu8brdtPfMaJoJdJv3YZCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=mbrDzD1K-DVE66fnYyvPISHRI4bMOINF2G7X3augboDZ7G9PeB5zFsTMuS49SoVK5mwZk-pX_My5KWOFvnQmTu_9lIDluzHdtuYwjT4JHaCV5od-YubG55NZuR3oe7yfrc-dtv5fekvzo_ElDn7QEAM636gczKOZo6cu_tAS5Wz0vURK6QjaLlQleR0bggjaPFObEjh9nKOTIUosPTgUtQT2rkbAvoReRY8SPQ5JDeCK0e2l3ck3GzuarKWGtLCZGitHH7jC17hxr20MXzWZ9drUS2Z9Uew_h-IgIQlThGPKYi4q56jXgRHl_Xs-u3TXGu8brdtPfMaJoJdJv3YZCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsYx_cJt_c_RsJ7KHsSOsWFWtrhFULBUq0Nd9wWUiFTVgnFka7aU4GlbOG24lA9aUUdxZOzoPjl-jPJxIce0dnQSF8fZwDgT2X_JuVN4dqI1WZsnIGFwZOXZ7zXn1gI9pUhZQIzrUpjNUfqowJROBH9ZhZl0-EmbjYlzpxC0WZ8VRdEOeS9EYT3XrlbsGX7CKCIcqnWYVkaE65MEYJ0F6BBjW7gtnzhycjqgBxVkcJr8grxdkrNSgy00P9NlurhCxfCCp6luJYk-R-pnoEyaU46Gqt1UJC2BZYSvY7M5yCSZ8D-wFXMSjcxwRRCXa1p4FH5hOKocybgk_48LjCeG2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=IQD-s3ixkw1CJ4ixUl5nqhfZ2aaG6jN-oDrqq7O5uA6koqPZKn7KrFLFNC_6VPoC86QC6KtqyDr6cjbo0oYFMgEaSAnmO1GYN2nq4RzyljC2lmSA62qkjZ90kqCBDOl4T-jX9T9bzsGWhsfz6r2Lsmn55sNsGKPHPGEuTAvr4xcEPB6bRvT7A8WcRJcDwvgHsdslys5j5o4SlumJz1Zy7npVrWfr8TwORKY6BWq6bBAPaOP_E5_vFXZ8jI0Jg5uk4rc-C1QAieqDoDZwuPLfmCmxR_3cG53ArhrElqcyMdZcm_6ea9BmNLMDYzmjLpZjFhd4V3udEWqU6PdOTc1qAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=IQD-s3ixkw1CJ4ixUl5nqhfZ2aaG6jN-oDrqq7O5uA6koqPZKn7KrFLFNC_6VPoC86QC6KtqyDr6cjbo0oYFMgEaSAnmO1GYN2nq4RzyljC2lmSA62qkjZ90kqCBDOl4T-jX9T9bzsGWhsfz6r2Lsmn55sNsGKPHPGEuTAvr4xcEPB6bRvT7A8WcRJcDwvgHsdslys5j5o4SlumJz1Zy7npVrWfr8TwORKY6BWq6bBAPaOP_E5_vFXZ8jI0Jg5uk4rc-C1QAieqDoDZwuPLfmCmxR_3cG53ArhrElqcyMdZcm_6ea9BmNLMDYzmjLpZjFhd4V3udEWqU6PdOTc1qAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlmU7UTaEeyjpqEFRZmQyv7Lqk7X8VUJ5h4c2USdFzR6RxTlxYV-26eSxhdxwgCSgyWaQuiWBi_0NTMxfkIy9QR2GpsikOIimpBkdlggvxd3LUAeYN6un3_5EfWi6B-ojqn6oMquLcbxwdN_Th8aSMd_xfcEEK-RV5a_tdVdo6H-TvS-1q-4A5qRQRSKi0paS-bc7TChSPUJ05_gacjExUAuQWLapwaGskZzPlrH5J73UmuD-mLNEEXPb6RFy9UIuIczRkKz3CNCsj_8SCv76ts4RrVXR1EUHKEEa8xBkM_mEWCP3r4fLV4MngPK62z51Xq8-4Q0sHcJgoBhS2lqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWQjIkTNauFHN0TnVUtE4dwZlw95Dl7du3l3docU4TqJ4WSEkJx3mWKVw2TmcV1zQGNBSma2eTIKQjAYCmFWHR92O1fA0kfqioM61aFO3aRjeNz2pbK-vK2w1Ib3ZMYBHdPgkGOEX4uT5cJCuXxeNND9ntD1VpN1bR81KofdvldMScqyJus8eWn6BP85EBg3HHwOHsOOX1FqKJiFJAFtq6WX4bFi4vmG3nqJ-8fJuvXYolkzjawSiRdcbV0j9qu1wdZ37ruCpYBkX9b-uEgDi1fOLufCpPZLBc40LAgD630sQUzRGeGkBFqtgttge4VpsoN23srtoK_mdJBwCqY36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1wOWzsxYjnSYeg4GM1uHHsy1J-yuUxVEajtYinDlZymQZTkxPhdhXEi-fgWjosoNN8zIAJLdLccaiOvE1t260bMpbVMDYjPlCxgeq8u5BfAlri9FHucz2hqH0l-cCuycdW0x_7GDr-aA1cuGJUU7sLFl3Ykp7GWlAvFjZ4YYJ6EUVESHOr-0y2BS_hhQ2uxrRRWfarIgxYKK80xVbzcA3IhwZzCt4bEpn3TOLo3hMxx-3bHxDkvufOs6na_gkkXaspWUk2-r-wnOz7raH63lHTSQwqaU38CYEROytA5awmXoEk7nTuq9_pUSidqbsSw8ILeiQMNh0EDlFa5aBdCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTh8rJChR1tpbZXD_JBHYRfrT8Txh9WxjIND0NhTw2BYYioGdPrxj_9VmWr7LbgDCSfcX6ze8hZNms9PO3-YeyeZuC4ya4HWAw6ZVQg6K7qV7kOFZEObKJTlTrffo7HtKTib5aBUSFEv_6WHTG7BwDVXBB_kHftfK7wv806-foXuY8NGvSO2FhdhLO35Y0K6Z8g9CsU3rb5RXsPeOgk5yxIi7nU0bfeA71azhE4MVffpskm6QBobXGSLBiklIL8m73oxqsdiQXJsOltJkaASIZRx96HITn-uTeROxTpZOEHL7uxD6U9dL4DXUI2SX8-cA_pB0B_pvu1EuqA1EKOqWWnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTh8rJChR1tpbZXD_JBHYRfrT8Txh9WxjIND0NhTw2BYYioGdPrxj_9VmWr7LbgDCSfcX6ze8hZNms9PO3-YeyeZuC4ya4HWAw6ZVQg6K7qV7kOFZEObKJTlTrffo7HtKTib5aBUSFEv_6WHTG7BwDVXBB_kHftfK7wv806-foXuY8NGvSO2FhdhLO35Y0K6Z8g9CsU3rb5RXsPeOgk5yxIi7nU0bfeA71azhE4MVffpskm6QBobXGSLBiklIL8m73oxqsdiQXJsOltJkaASIZRx96HITn-uTeROxTpZOEHL7uxD6U9dL4DXUI2SX8-cA_pB0B_pvu1EuqA1EKOqWWnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
