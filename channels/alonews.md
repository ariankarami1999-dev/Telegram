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
<img src="https://cdn4.telesco.pe/file/O2aWxPgh7A7l5-Le1oZrswqIGfq0EJpX4L_19Un-TS8jEGgbrnB4db_N1hAkJKdc12JlO8ziGQNnhLvBF3tQwDD6fRFEENQgy9I5m3TLC-iNZ_5PbL8neuZ3FRoiIQ4VyHjMaEW1uWPF3OPYgiyonr-5AOFSYeuZNLEyHKKc4025N_fiZsu5wq_HWvexJ76vX7GCST9YzmnMpgvZ0ylkbaFU7f_B_pZrzSD5f4XiNwDM4nOsL6HnyxJzWPDJu1DF81sLLWmpjovfbJraWiQCCZNUHUAKtgwYSwOrQsDnNFZiDX8jaZwd5e-aC8V1zx-srMfs8AQdkR48GfT57TubXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 11:55:20</div>
<hr>

<div class="tg-post" id="msg-120546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGzgjkcY0M3m2IAGLC9ZdiD1A-bkRXqFgwQG3LxFfvk-2yIuf1ko9rZzinxy1jjxU-UZpS1muJTncI3n79618Jd02KIAJ-idEw8NjK9qjnS9AIK67GAVaVFiXPUPI7s4Tgju_adwoL4vNK35RSGbPqtTsyASmt_EUl7Mj7GfBFlZSpUJdxWUKsHtkvZ9e1NCg3OsyEL3sJrvEGZ2TYAB1k3rOSjsmKTNa7YmPVd25xJFiQ76RHNlAD8yzYT7ImQSP0jcpeMiUTMp-BjC1XLuvq2SiYtDvufsXL_C9JFsOJSYqFVq-f1VSwkj_F7hcAPCfNRHbBiqQgOJMf1U_IYIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5UWQqL9LdoTY06bDMP0LcWJqTNy1BUIbKjV3mIHCeWFr6iEDSYl30C9o5xNVwnENsqHqNnWBFDf6q8kpKXY2BjkAewh_kqRRc-rSzsEo5cdITIvdAiItRNbY_JKxL2S7wV4weXxgcUyzvEXasDAIUZp2NoXb_Q3IV2uO5EtPxAc6hM3acS2B6c3CwOBg8QdzZnmU8t7yVJSg6jRGUp7sITm2Lp_Ymp-21CspOSTAesDlpeSf3gnavTZCrlA8cRxVy8w_VZGw3XD9oGmTrCMIEiRtzrKvcUKmahTnL8572ttQQFgsQaKBJaRGucDrDto6EFdo3RZOf4N7BhKDfBu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3gPsxpeTX_ZGEHclvIq0Rb_kFT5pkLrgqQ60ErfGGoeQFjZy5GkzH6eM72YnnlJuvsMlLRSV_618SZ8LQlPEo4fZjTesRLdQyeC0YhdP-IPV7x5prWgPtUntGh0XfWNgz5sikVnyfdOM4YcNKwU7PcKXQdqHU60EVCWf8hudPZ2ELOGci6PxSyd2bFEXE6f4Bu0W9UtXQPQmkdpMPuKSxDx4HbamAsxzFV_knznhbYTrOyjk6-sUriw16jaodhqF5F3owM3Dbj_CJBYIqKVMFSKXjLYbLR-0EbbZPaLTGI9YOLLA7yIErGuMlQQNc9QMffIXUB5SXQPszwRcXE15g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از نصب مسلسل ۱۲.۷ میلیمتری گاتلینگ چهار اول نصب شده در دماغه برخی نسخه های بالگرد میل۲۴ با یک سامانه دید حرارتی در روسیه برای مقابله با پهپادها ..این سیستم بیش از ۲۰۰۰ گلوله بر دقیقه آتش می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/alonews/120546" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCQL5hcvtI20egbxYuNiALfrM4MV08fAiadQ2ptMGM8oJg-FwN8v5umSNzJ12tmL_YSM61krS9j9WZT9kGUfKtCWgk2G-FXYV3vWzxedU9AUjBQ0ieRkuLnyXK-vDRpUjkK1uWSkA1aymU2u2whjBCmanPx9m_ERLViLhm-rAc4MTuCZ0vS-HewWnUrJhw7Df3ax9K_vHl1BPEam5idfJzhM8ONuE8fjWsUS7X1GLU-hA4y3gqmM5kCl9JlTDd4d8L6flggBkCxVDZK8XEdNNiFA02Uu-_66vA9cpNWmhYuL7C6StWaWpVxSv6muA5XN-jDHvzqinroG6RPiBfv4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از چند ساعت گذشته بیش از دوازده فروند هواپیمای ترابری راهبردی C-17A گلوبمستر III نیروی هوایی آمریکا در حال ترک خاورمیانه و حرکت به سمت اروپا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/alonews/120545" target="_blank">📅 11:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فارس: محمدباقر قالیباف، نمایندۀ ویژۀ ایران در امور چین شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/alonews/120544" target="_blank">📅 11:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
معاون شرکت مخابرات ایران: دسترسی به اینترنت باید برای همه مردم فراهم باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/120543" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAfJWAFnfPhDHpPMd9eFU76oXElfaOBxV6jTJBQ8GzibK8nIlRZyUsvgAkTxdiHi7VcsQPPR-IAKMlJIsKKFtM7Bb6AmDSc4wGZh3y30L2c8hjDS8ybrliZhxJGumKCUXecbcwC62yuWJOmQnF6lmmCVPSQ4Om9p9FnKWi2GIlgAhJQX3yi9HD_7skJdtCwbHXm6-sC2yXBYokQl5RF0CV8ACKf9WFynLwheUGjiRqFDc2tI7qxqYi6yy4qCqqdtRUnVN0I9T1NwHsWv8FnhjvKcRjYOsHI5owMYViHlrmTOSU06fTrZKstRj0xWPg827oJqAiFZH5P2RpcWMw3ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری لو رفته از گلشیفته و مکرون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/alonews/120542" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy0UlrjiWbsY5tJzWiQ8UdnxsIPi3JQWFD9Pj3CCMdtdG2Y0WdSHt7GAlegYPl8_PUYSg_pQm68GlCzje86Anr2Hoq-WIRtw1LcWLIXcu5U52W-NFcor-3dnsI2pQSlx2Vo72Bl4P5Jzet6h-1BjbeNMQqWvA_jVwJqvEVdkGHzfIaKNwUwlLTxw7cCYRXp0X2xE12cNd1ShnO4Hgi5YcloI6ulA8IZxG9qwq3pAVz-ev-mF0DBgk0cVWouLvDJfnKaAQxxS0t8qpouTq0epW9n8LhP89KRcKY3sd4GefadCIirNmHD2hWyuJVa0HU2w_72frWY6uoPvZYDAXwyuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفر ترامپ به پکن نمادی از کاهش قدرت آمریکا بود، به طوری که چین تنها رئیس‌جمهور را سرگرم کرد بدون اینکه هیچ امتیاز واقعی ارائه دهد، طبق گزارش آتلانتیک.
🔴
فرانکلین فور می‌نویسد که با وجود پروتکل‌ها و مراسم پرزرق و برق، دیدار شی و ترامپ هیچ دستاورد سیاسی یا اقتصادی قابل توجهی برای واشنگتن نداشت.
🔴
مقاله بیان می‌کند: «وقتی آمریکا دستش را دراز می‌کند، دیگر هیچ‌کس برای گرفتن آن عجله نمی‌کند، و وقتی تهدید می‌کند، دیگر هیچ‌کس ترسی احساس نمی‌کند.»
🔴
شی نه تنها از ارائه طرح مشخصی برای پایان جنگ ایران خودداری کرد، بلکه از امضای توافقنامه بزرگ تجاری یا ارائه تضمین‌هایی درباره دسترسی آمریکا به مواد معدنی کمیاب نیز امتناع ورزید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/120541" target="_blank">📅 11:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قطر و عربستان وضعیت منطقه و آتش‌بس را بررسی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/120540" target="_blank">📅 11:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfU8JGszgvOgGADbtYdDJru0_pWttQRZnZN8yDdzSY3sAihlNWECH4f6eFiSWwccJbq6XtFzN2b5yF7HOs3j2rsjNu3STA-euosn1sCsm_WdqcvMKs5EwwTan-uS8WtbTYLFRGJmz5htHJI15hAprruEb8s9xm9BXcM3V3vr8GZvlWHZoX6iZtjDhJu1MgUqMtIyOuO9vGJZKWMveCEsgnUAslcvYR1xRdnnohYBDC-2Vyccft8ArKiXv9I9LS3HsP7d7PtdOgmHMFeif2elHyaOHRlRF_i1Az29N6B0gllwpIOuwFmJhjWszrn6NSulhIWlyelzl2g2T06RP2fBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/120539" target="_blank">📅 10:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خارگ همچنان ظرفیت ذخیره سازی دارد
🔴
تانکر ترکرز: در جزیره خارگ، ظرفیت مخازن ذخیره‌سازی نفت هنوز تکمیل نشده است. چرا که در این صورت نفتکش‌های مستقر در منطقه را تا آخرین ظرفیت پر می‌کردند که تا کنون چنین اتفاقی رخ نداده است.
🔴
علاوه بر این؛ ایران همچنان نفتکش‌های متعددی در اختیار دارد که می‌تواند نفت خود را با آن‌ها بارگیری کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/120538" target="_blank">📅 10:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بر اثر واژگونی اتوبوس در محور عسلویه به کنگان ۸ نفر از شهروندان جان باختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120537" target="_blank">📅 10:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120536" target="_blank">📅 10:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR1LVa2WJt_YbxzO97AzomXFh8_-oJBU1IMlTpquI1h5wsGqNiqEevUJRso0wbNmNXzbYslODgRoc-HNCbgDPPHZLIONMl6eghIfqew8IcA_BHPw45nzoA4jq-FGemrD5Fg90JFPX_IjzxzA5B08gZcWy2DgLEqt3cURYunRj5Bg8bbWXTMEigyGfqQxoNu1NOSQH16mA96AjfZMWqO0yYuIPTUQqwK7M_n5op0aR3PSh7VtKVjw0gDlNDxOD0_Ak9G8raS6ieorU7ej3T2SPRODEnNOc2ERzC83PdIduIvdwVd95ZhVLLScxXmKL6hLrQ0TMBR9dTj4NhKtECVaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت 6 ساعت پیش اتاق جنگ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120535" target="_blank">📅 10:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
تایمز: انگلیس برای جنگ آماده می‌شود
🔴
یک رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120534" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تایمز: انگلیس برای جنگ آماده می‌شود
🔴
یک رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120533" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2461585c.mp4?token=HJfnoISB6FcRLQmF-GMnDJp72ZBFRhrrU8A5q-annNv8pIpH98wQASjMz0iVQGoraL7ql59yh5EUCDNS8ipX-cUzE3ugdq9SSGxDqp-T1ZBNa6WmpBU69Cdcu70bgsuXHoMn7GN05PIeL042-Aqbak472V6mVOHnagF1bd2wYqZYnryAVqYOSJdjYBIkIeRckjx9gNyOJyztPTeEmKFIisZkGMTy2BDA0x8DeBHlCA-CYMuhHTQyJF8zJFpuAKdzByn63xdwahtirCRR-gyzJm-zp_KyZc97DAOGk2nujxBlvcmcrMJ8Jkkltl15ClYhmW4qvaJU4wh5uUTlNc_m5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2461585c.mp4?token=HJfnoISB6FcRLQmF-GMnDJp72ZBFRhrrU8A5q-annNv8pIpH98wQASjMz0iVQGoraL7ql59yh5EUCDNS8ipX-cUzE3ugdq9SSGxDqp-T1ZBNa6WmpBU69Cdcu70bgsuXHoMn7GN05PIeL042-Aqbak472V6mVOHnagF1bd2wYqZYnryAVqYOSJdjYBIkIeRckjx9gNyOJyztPTeEmKFIisZkGMTy2BDA0x8DeBHlCA-CYMuhHTQyJF8zJFpuAKdzByn63xdwahtirCRR-gyzJm-zp_KyZc97DAOGk2nujxBlvcmcrMJ8Jkkltl15ClYhmW4qvaJU4wh5uUTlNc_m5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت غیرمعمول امروز هواپیماهای باری برای سوخت رسانی به جنگنده‌ها در منطقه خاورمیانه
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120532" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ادغام کنکور سراسری و آزمون پذیرش دانشجو معلمان منتفی شد/ آزمون‌ها با شرایط سال قبل برگزار می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120531" target="_blank">📅 10:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: پاکسازی ۲۴ ژنرال آمریکایی در میانه جنگ با ایران
🔴
پیت هگست، وزیر جنگ ایالات متحده، در سه ماه گذشته بیش از ۲۴ ژنرال و دریاسالار را بدون ارائه دلایل روشن برکنار کرده است. این اقدام شامل روسای ستاد ارتش و نیروی دریایی و دیگر مقامات ارشد است و شائبه‌های سیاسی را تقویت می‌کند.
🔴
با ادامه بن‌بست مذاکرات با ایران، تصمیم‌گیری درباره عملیات نظامی یا محاصره دریایی پیچیده‌تر شده و پیام‌های واشنگتن به متحدان منطقه‌ای گیج‌کننده است. همزمان، وزارت جنگ درخواست افزایش بودجه‌ای نزدیک به ۵۰۰ میلیارد دلار کرده اما توضیح قانع‌کننده‌ای ارائه نکرده است.
🔴
کارشناسان هشدار می‌دهند ادامه این وضعیت احتمال دستیابی به توافق سیاسی و موفقیت نظامی آمریکا را در منطقه کاهش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120530" target="_blank">📅 09:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قتل هولناک نوزاد ۴۰ روزه در مشهد!
🔴
مادر نوزاد می گوید: از خوزستان به مشهد آمدیم و سوئیتی را در خیابان نوغان اجاره کردیم.
🔴
دو روز قبل همسرم که مواد مخدر صنعتی مصرف می‌کند دچار توهم و بدبینی شد.
🔴
او ناگهان تصور کرد نوزاد متعلق به فرد دیگری است.
🔴
ماهی‌تابه حاوی تخم‌مرغ را برداشت و با آن ضربات هولناکی به سر نوزاد زد.
🔴
سپس با کف دستش چند ضربه دیگر به سر او کوبید.
🔴
بعد هم نوزاد را به شدت به زمین کوبید و باعث مرگش شد.
🔴
پس از این ماجرا جسد کودک را داخل یخچال مسافرخانه گذاشت.
🔴
او مرا تهدید کرد چیزی به کسی نگویم تا اینکه دو روز بعد موضوع را به صاحب سوئیت اطلاع دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120529" target="_blank">📅 09:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
دولت ترامپ اجازه دارد معافیت تحریم‌ها بر نفت دریایی روسیه که در روز شنبه منقضی شود و مجوز موقت برای کشورهایی مانند هند برای ادامه خرید نفت خام روسیه را به پایان برساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120528" target="_blank">📅 09:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آب و فاضلاب عسلویه : با توجه به تعمیرات ضروری در خط انتقال آب کوثر، آب شهرستان عسلویه از ساعت ۶ صبح روز دوشنبه، ۲۸ اردیبهشت‌ماه به مدت ۴۸ ساعت قطع خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120527" target="_blank">📅 09:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سی‌ان‌ان: کوبایی‌ها خود را برای «تهاجم آمریکا» آماده می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120526" target="_blank">📅 09:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کوثری، نماینده مجلس: ترامپ در جنگ با ایران درمانده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120525" target="_blank">📅 09:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a1405883.mp4?token=kNZbBn7DNdEL4DmTag2qnyUEVuYrBlFMlguz0kULGqE5DqefPTQg4d75KB6aiCEUGDyk7T4Y9aXQdFUwYd4ezqsrF8IN4mAsYSihtOfvfNLSR-qNb_-Km2eoQo17bF3YaNod4BZUHiq31d0-b-KtpvwNjajkzDavPQJhy6lShRZFl5oyinTU4kijnhyw6K9I-7_k4YSfxD6p_GIO9yzrBb-xTul1UlaBeMyDwbnigEluQwYemOD7Q5UKqDZvcDfyYXFRTFWrONyY7fUy1aoVxefGI2L0BBk4LmIlW-t0aXQ7rOIzotMp3rkFazxSLk0gdaMLC9GPc5ghbJgrH-sKQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a1405883.mp4?token=kNZbBn7DNdEL4DmTag2qnyUEVuYrBlFMlguz0kULGqE5DqefPTQg4d75KB6aiCEUGDyk7T4Y9aXQdFUwYd4ezqsrF8IN4mAsYSihtOfvfNLSR-qNb_-Km2eoQo17bF3YaNod4BZUHiq31d0-b-KtpvwNjajkzDavPQJhy6lShRZFl5oyinTU4kijnhyw6K9I-7_k4YSfxD6p_GIO9yzrBb-xTul1UlaBeMyDwbnigEluQwYemOD7Q5UKqDZvcDfyYXFRTFWrONyY7fUy1aoVxefGI2L0BBk4LmIlW-t0aXQ7rOIzotMp3rkFazxSLk0gdaMLC9GPc5ghbJgrH-sKQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی به ساختمانی در زلنگراد، منطقه مسکو روسیه برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120523" target="_blank">📅 09:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZqDL3AcXFS9yFnLuvjzoKLHZpCcjIDefcBONoHbYKQ97XP-hYKCPUNbej-_1HFedyRIsCJwDjfddVspOlRhdejKMuBFGnlE1iDODORZ4xqPIQW3_xUMA8qy39mjDtcAp80rp0R2x7G5Xvr01_2WWEJnLDw3bm_W6ZFXemXRo6eP30dB5z5cC47hvG-A8odqx9el2XFVB5OqZC7m2nPAKoYUHN2uB8DrjX13GTeKYZA6Ru6u7F0eblw4ng93j8V05hFu9xpcaLzpUpBrKxS6DwzKKj3XTV1JnBTX0GZeSpoTllbkQSB02EnLzrlwLYv-w_Efdzvg25-Vyo4oMysTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات پهپادی اوکراینی فرودگاه بین‌المللی شرمتیه‌وو در منطقه مسکو روسیه را هدف قرار دادند.
🔴
شرمتیه‌وو شلوغ‌ترین فرودگاه روسیه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120522" target="_blank">📅 09:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بلومبرگ:یک نفتکش غول‌پیکر پس از توقف چند روزه در خلیج عمان به دلیل توقیف توسط نیروهای آمریکایی، سفر خود را از سر گرفت.
🔴
این نفتکش غول‌پیکر به ویتنام در حال حرکت است و دو میلیون بشکه نفت خام عراق را حمل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/120521" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9e336326.mp4?token=CmbpEE3axXMXOgkRxzaL2kl_2HrtFq_wbr_83G-2V5KUTpiQNEoaNqCT9HasRuustACkmfD9JBk6ssURc6B_vKCKX-4dK8J26U20c9Njv8K5sySIP2oBTWQ-xr0qUbZtkKz9fhrBGxstTu2r2B8cepjCiv1uJvsAG9ST7dALdGGIy8jCIsziU34BXgk0QEuKroFUg9jh__7Gl8g5A5GNwyXnckcQe-cfi8eAYbkfSS-SCg8WnsxiInUmsXxla2BAjABPZ4hprk6vJXqQDf36OhpG4Ap61Cx_hEqERsbOwAtbMxW8aGFe7LtOZbNmFDiw928DoEgQQgtgu9EbU2eGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9e336326.mp4?token=CmbpEE3axXMXOgkRxzaL2kl_2HrtFq_wbr_83G-2V5KUTpiQNEoaNqCT9HasRuustACkmfD9JBk6ssURc6B_vKCKX-4dK8J26U20c9Njv8K5sySIP2oBTWQ-xr0qUbZtkKz9fhrBGxstTu2r2B8cepjCiv1uJvsAG9ST7dALdGGIy8jCIsziU34BXgk0QEuKroFUg9jh__7Gl8g5A5GNwyXnckcQe-cfi8eAYbkfSS-SCg8WnsxiInUmsXxla2BAjABPZ4hprk6vJXqQDf36OhpG4Ap61Cx_hEqERsbOwAtbMxW8aGFe7LtOZbNmFDiw928DoEgQQgtgu9EbU2eGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون : کشتی‌هایی که پشت دروازه‌ «تنگه هرمز» ایستاده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120520" target="_blank">📅 09:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120518">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsVScsPg8gvNXXl9PAIeuB-llQaSAWsLkxf32bFs_1zOlC54zbvufuj18FeyDjZ1n3vT8FmGTfgsa2kQlWvXCEsqdA_5DFiuCNwrQWgRvvbqh3OBg-iw6DvB5EdAD6mJDlecjkd7mg3bpPV1nWgo5LcquMB0jAga_fr2hWmVprSzwvuaHZ6OOqOZC_u4Bw-6WaQGqtk9_oRHkXQD1oVNxFCPOwnIojM5Z9jtBGpCn24KYU-5BVgzilvo-Vx2uXSP55EG5sifgK2GXO8y3ZYGry8E4YeiQGpADYxTNfQ8ge0nk7t4YDAeSAKX3GF8-Fsk4nF7NDMVFY1zUI_pOHmJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62322570a3.mp4?token=R6g650cu_WLNeTDliRPjPEdN8XgkUicE4BaMu7uAd3RVQC6TAZ9hj7cqkczwAepNd-glL2zPhFrkzwsHDBOwzMGTqawEY3xBdaHVezPjcPUJgUwCBsBqzel9f2oNqxryy6sDqSj6HPkCckOD0zIaFUNvtaTKrK6TQ5gyJ-fMrEkGc5_PGsA-Nud860rPsFISpBUlYQc6zKbo15TqXk2cu8DI97RNgtXMk5nJHq2PjAhHDau5vsfrqn7GzDw0epV1tp8QDkP-WhhFT3gi_eQJjXXBjfG-dUPrfMg8aBAIwaMkjruMohAe6pc1Za1JzDrUUUME3y3_LB5Ou2_oaBxNiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62322570a3.mp4?token=R6g650cu_WLNeTDliRPjPEdN8XgkUicE4BaMu7uAd3RVQC6TAZ9hj7cqkczwAepNd-glL2zPhFrkzwsHDBOwzMGTqawEY3xBdaHVezPjcPUJgUwCBsBqzel9f2oNqxryy6sDqSj6HPkCckOD0zIaFUNvtaTKrK6TQ5gyJ-fMrEkGc5_PGsA-Nud860rPsFISpBUlYQc6zKbo15TqXk2cu8DI97RNgtXMk5nJHq2PjAhHDau5vsfrqn7GzDw0epV1tp8QDkP-WhhFT3gi_eQJjXXBjfG-dUPrfMg8aBAIwaMkjruMohAe6pc1Za1JzDrUUUME3y3_LB5Ou2_oaBxNiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی ایستگاه پمپاژ محصولات نفتی «سونیچنوگورسک» در منطقه مسکو روسیه را هدف قرار داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/120518" target="_blank">📅 09:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120517">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فایننشال تایمز: تنها چند کشتی روزانه از تنگه هرمز عبور می‌کنند.
🔴
پیش از جنگ، روزانه حدود ۱۳۵ عبور انجام می‌شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120517" target="_blank">📅 09:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مقامات ونزوئلایی اعلام کردند که «الکس ساب» متحد نزدیک نیکلاس مادورو رئیس جمهور سابق این کشور را به آمریکا منتقل کرده اند.
🔴
ساب، وزیر سابق صنایع ونزوئلا و از متحدان نزدیک نیکولاس مادورو برای دومین بار به آمریکا منتقل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120516" target="_blank">📅 08:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کیهان: احتمال بروز جنگ اسرائیل و امریکا علیه ایران در زمانی نه چندان دور وجود دارد؛ آن هم جنگ فرسایشی / دشمن شانسی در آن ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120515" target="_blank">📅 08:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120513">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLX2Lv8Y4Wl-BZvUplbkmtSfIDJveIxtRro_W47_hFSPhSo8q27bhuU2WWuo1TwuMptKC2e3-gGY353aZDC9nBNrVAmzP33O8QFoEi4egLeAqPOBO-VpCP_yZkkzQoXUFQHl1QRrg3IKBREOWpP4BMJFj-8vr9YD7g_OY-2IF_OKnoI2bydiA7Sx_Ob4O-TQACbvNEcw-d8Q7le5ZNTwNRUQ7BftRBIFbyHue-lHA_go8JlUn02ZPUTBLfq1yjQKMoWo5rKPwtbSOzhS_hYGWYZ81HIynLKndbQNrbpL29iJuQ9BAo-AK57gEchKul4OyOqQpvS6gAduWKuZdpm4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWo5j4vdepRsNvbm6jbQskU7WXMzVeF6hZHseS6NAMqBLJ0uTmA9izY7OfDDmJUhc_kqByZnr_uWpjcpnixpBE88Lc2SUTREBYc3xpEs4nanLwcjsRTd-g7tZzzUCBTPnWoTdRQ-l79W6SRzKbRnKxBaMFbss-XTjnCdaE_Hmp8-ZQRvw6dZEDPEJPkyuzcbEQoPFWaE0zoHiyrvrd7j223_ezfbqzgrUty_VZsRf9lFvnraN0xzHPbSy7YdTLwYKP1CWsJGA1sIa8y4s1Zp0GE8PstmnGgHIBTdiq1kku76RHksUxVVF64232q4DeYfnunQv75aafd_UNJrhnGyFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ به انتشار پست‌هایی درباره سفرش به چین ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120513" target="_blank">📅 08:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120510">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxGWJVKUcc3QgfC6FRF93xwa_3j0iTt4NY87f6JQz8VpyCijPgRcNl8nFfh49y0k3x8UZzJcbP2qyY8jVhxLMRRi9G_e3guYztM4v0r6nb-wZQQ55eKhi1dyesCvyIog7wfcAelF1eHg-J8aB25sa000kQ364nke4btmyVyGfIYErqLbFcd4O1K3Qkv65Gkzsv4urbSsZrajMT9ZecYpLE0uoA46DrHba14lpgJlR0dfhn6YqcjGyofg8oL0Qrcr-Lpqtw2IEqMu6y89gu8lvRfhrSkoIFVGxKKS-Ke8VazABpay8WEtcbxUtstKTv0Dt7rShntJ6fMOquJ9EiTpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0P9gVe9t_7nuY8Vr3q-SlVrEXX6FRqFSICGTndv_ZLWERCWhZDX_8OKU3IZ9jz1cas9zSgVbBhNY4ZMrbNX5kcXyQcG_IeSWuq70PlxCWI_vDAFbBrp5dQITu9-jVWXBDNYoCIevGSBT-N12nnqUFZapmrw6WOIM2kzVVTD0sTA7OI8vtPVaLlYXlDPEF4wUJ2Kqx1-ZBMqrXNeMx4T4shhD4vuyBAKnlYen8tWk5rbjb59cWYsylTeeFyn82MnHAHG80XqH0-FhNxSfTIWCao6mXvWyFic8RPx9hf65ZuEbhwz9o28oJY8kV0uzOTK36byW_DILuz8ipAVIEIO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9cRnG4dfu6fwuw3Kpv5a0kdAWjXdOq0j-IosPoh5HSw0B5UGgHBAgLiD6s1mVN_z9KN30LBpONLLGs2A8sttXvCjhgwoQF0R7trTAjQG5jX5OhxU5ld8hc3f5p_UscSlvJj3GbYljHNllCOiBxMD5tprMzmlTaf6ClfC0VLIZhBU7WfocuQMrzoth2CgPox6rX0f1AlnDyaH0_XNcq8jgkcspPDhA8z7fLhfbHKXovS8_nDezgF8EJ-PI0XGTxNqvaPvsntB8mVkg1dhlfVCIryd9QxyJHdzJ08_SEunTTZkrH3nC8V_0ZW-MfaQS3UFKZ5L8Z4h6KCPRJ2YM0DnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دونالد ترامپ در Truth Social:
🔴
«همان آدم قبلی؛ فقط حالا پرانرژی‌تر!»
🔴
«رئیس‌جمهور ترامپ جوان‌تر می‌شود»
🔴
«رئیس‌جمهور ترامپ برعکسِ سنش پیر می‌شود!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120510" target="_blank">📅 08:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120509">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7Z_XHhN6L3uUTo40PlhIPKmniSR8XTA54lP-ygDUNWpzoh0e-D15pSkrM8v9zCq_sWdwRAdbVrvng2SNPtZPg-S-0YwaoPCyeSf4aCEatwsrNhmNqFuGJAoWVKygCgHkvDQH_zmPMcXiANregJaRtEh0bhN_92vjT0KRqnvPXYh8Qqn1Ze51aRUG6ajKft5Lv5Q9CRAT76M5SS05kJWjMSWpYIuBT7JHwrak2h6KsT87K5JDso1cfBBVfPFXRW8Y198LALKwyIkaICDsy5mGAmGgodMSf8MRamAwoE42EALbbrt0cwaylHOvluFgKydcIIVSYjjmGVI1uCt_KTtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید یک پوستر به سبک جیمز باند از ترامپ منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120509" target="_blank">📅 08:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120508">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egQr4GivL8rhAcAyJ8Xs2TboE0ADK2fqQ_X46nBbVBjZBDZ-v9I9FlvqZqys4Jm95s8Lpytm6mkJTuRlmFq12UZ_BbhNL4F3F6HXozzuXQSuKZH09YiR2M9pbh5t0tG6titTRv_cZvOUHynPcaz5ChCRYYp-NJIK431CZYxirocYpV20AAQvGeuFxQJmCpKAFAFu9E6IjQjpx73LayahmK-gf2Hw9u69JfyzJrpZCknGS-wC9UzPF_MFMdgj3n8ZyRauKJtsVoGTmug20RXXtOVgjR6C-9FdYoHbTGgjopJyiWAis_kcALbI_Up2gsFbcvc0V20PpyWZqPvnG0ZK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/120508" target="_blank">📅 08:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120507">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z03Ce7EDenF4YsjLKBbTNSizqo6ErDSUQfspYyYfC3qmrPl1oOMkOkawrRwWwxnZ18FqYOMuel67R7hdvAi4l96da9FGhBrGkKIsSuFlZ_tef97yweA5YFMyYNPzLPvXRhe2v01EPWijWrGqu4k_BYs7spudK6kZPAjsiE7LZjg-gyjZucMM_Go5OukqpAxLWt-4rDZU7fLF90oZjK_CCfLvBpdeBJyjd__nkGxRJG8mXe8h6xi_tw9uIzzUUITyR7_CdmLVLhfzh_0RpdY8u2PXSdwwINjgGWrxa5muMIbyTRm79Fczi2uhJYUF2bJoJyvKt0yD-ZKtj3I0Dmfxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیلی‌میل: نخست‌وزیر بریتانیا به نزدیکان خود گفته که قصد دارد استعفا دهد و یک «برنامه زمانی منظم» برای ترک خیابان داونینگ ارائه کند
🔴
برخی از نزدیکان از او خواسته‌اند که هرگونه اعلامیه‌ای را تا پس از دریافت داده‌های نظرسنجی از انتخابات میان‌دوره‌ای به تعویق بیندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120507" target="_blank">📅 08:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120506">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: کانادا در حال تقویت روابط دفاعی قطب شمال با کشورهای نوردیک است، زیرا اعتماد به ایالات متحده در پی تهدیدات ترامپ برای تصرف گرینلند و الحاق کانادا کاهش یافته است.
🔴
اتاوا همکاری نظامی خود را با دانمارک، فنلاند، نروژ، سوئد و ایسلند گسترش می‌دهد و در عین حال به گرینلند در توسعه نیروی نگهبان محلی که بر اساس نگهبانان قطب شمال کانادا مدل‌سازی شده است، کمک می‌کند.
🔴
نخست‌وزیر مارک کارنی می‌گوید کانادا هنوز به شراکت NORAD با ایالات متحده ارزش می‌دهد اما خواهان اتحادهای قوی‌تر در میان «قدرت‌های میانه» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/120506" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120505">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5Ue2pki3hMwDEiWwq0xuK00HWvmmbuh-piLbBgQE_pbdxD0YnnPOR1RWfdPgnNO3pgx2TARD8khhv8vmPHCuByMMN-4GLZ5-zJ__tc7hLFasm65DMrD5xbp_Po06IJSTp1qfqpKDxslNAtDzRFQFAEe7PumDYNZ80atUgJH1GEB_w2xqfKfjtYq43ZxXkfl8oENpefbK43eSgrwKGYG0gCglCMqFjehWh2jGCOvDuAXcbq38BDek7eu-d_O-Vq3S6PGe54UHf9aXzHnFqvLWy3McK3UfZINx8MJ9Ysbx7QwQRWgUfcGrr5xYJazTNZZwEMzEzCvqkxB3qL3DRripQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: باید آماده نبرد آخر بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120505" target="_blank">📅 08:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120504">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
طی ۲۴ساعت گذشته تعداد زیادی ترابری آمریکا وارد منطقه شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/120504" target="_blank">📅 07:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120503">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbKHbPdN-qdFGyW7AvbvcQIM14G5txnpSkwvInUhL6PjgOVD9KS8J475ruK5nVG7X9-88khqkCXYAFN_qcu0rNZRCZX1v1W80QR3qsAJgxpQYPFSS9BCU3uTw9yiBsaIydtXGs2s_AYwpnQxzT2pPuZKgWcV43NyujmSMexpR0j8bTy2BBJx0_qAcnmCPMR3bqKYoNo9Dnfhho7Qxl4W0xz5wcdjMbutbgi7kQIedTRSC4UlmP3hYHywxYfaLhGyDjzgeT-XyHjQpxkt_YbyOAiV77t3ZwTHdwoh9lP9BeBkBzB3BlIM0dhNttuk0t1nqBaz-eUjOmzVMkj9_BYEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک تقوایی میلیتاریست معروف:
انفجار در کارخانه «تومر» در بیت شمش، اسرائیل، کنترل نشده بود. این حادثه ناشی از یک حادثه بود. انباری که پرکلرات سدیم مورد نیاز برای تولید موتورهای موشک‌های زمین به هوا در آن قرار داشت، به دلایل نامعلومی منفجر شد.
🔴
به گفته منابع نظامی اسرائیلی من، این انفجار به دلیل حمله پهپاد یا موشک کروز نیروهای دشمن رخ نداده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/120503" target="_blank">📅 07:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120502">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHb4jP5MQQ_U-WTJVX3qrf2AtB9NaHLDjKeEejIrkzVKa8_FXSrDGP7iOtRN7udpeC1CDYf2OotiZ425yKkLcFtW2cpqGb5RLciTndTdOK1nXNhWRakyNiy6I4iwiCd7JFQ31IwpPXfMvOltcVo8Ljh499TBVxt7-rRbZQDli3tgPcz95Ac8MoJHIvRUPwNa5v7HP-V9XEpWiY4nWBagHIMaCYCPhRPumiwWNQq-JXi0ovPgSaJwOFi8TbZd_W7p94oiAkkRact_5dAIsOdbrLlYMmXyOqFlk5YWVOM6PqqcWfA_d4odFn_ZLGEKj1mGPcQq2BMpdabDe-71jX6-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/120502" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlGweNkOJmVkxVNYZaNO_RsMWGiYG8asEb-5yPXlxbAvBFIIBaIborbaZ2N0iEMW9MDbcq0r1lFRgzaoMT76wr6fnG3HAXshijao7oXTGYXWrhGgLdK-BV5CSxWQxFYXeZWqTP4vfuJn747s5GGDwpICTh-tk5uLAxFXBEWE0fuJoNJx3dhHQReIYW19sY1A499PGyrBTu9iYTSurNTd7TkoYGO9cZEDPYDr3vYz1vjiicdcndauWAlXGayyHTOxfmcJSRwllkPEaoIoN2Y21kugnSjcKyT7H6rbBgJf-NXh_-KPhvcI-v8J8vKz5_K8cxovduqoJn8561xti030_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده روسیه :
کارشناسا میگن آمریکا و اسرائیل ممکنه به‌زودی دوباره به ایران حمله کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/120500" target="_blank">📅 01:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e011596213.mp4?token=mZ2QHSvm1HZxkBwlTjIb5fPvg-MRtDbDL4SzKpl2YJHuz-S2hmM1x8Wu7VvcXkZL9qqlith4Xe0erxEsylaivL7k8KRPI-vSIeNEG755q5FGu9eeD_Zpn4IGhzfmkUn0TC5YySwk59rYWjoP7EuAsoUWeR8xGoYmVpxgAKnp6w6ZuhzVXb58br-1MKWjt_AIP68mXoDptz9an2w76zthaQa5P4n2WXrSwk8srOAOQLyM3Ga0Ewr4sioEjlF4cJKvgHaeggl1xxksvZacEeBdFtJX5VIECUw5bJOp_H5wSuWx9atSoKSOpvzEElUF-6C3OFq9f3fC3Lu27oKWsI1NPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از حضور غرور انگیز بیرانوند در دایرکت یک مدل معروف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/120499" target="_blank">📅 01:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmBb-DIA_YiE-_xIuvdga8SeBlzYqtcz4qTE6w3rJiuabo8vRp6e2NsawdRhHrAau4pCnbreYmxstG8Jbd4-PCwdI4SHO90gYXRjLtjoO8roSCr5yxTETod52Ecg2Hsj-pqO44ZCTzxiuQgIbbM8LqVF6Mt2QAwwUjPHkwIa3ZIXWF7DQXpQ3pN793KMNlpNq8mg-cKIID8rXOvBnoEaUbQ5l6qMHwq-i-ev69vw1WOsnHE5wMYoIVcX5XqeubSVDUlsIx6rBNeo3nMmLmoLCTn55YlA41t2Gi7zT1oMWlgO4DDbRES5jtJkr8WLbOVJGsHInxRzPfmQIZIP4mCx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیرانوند : با صدای بلند و رسا کف آمریکا سرود جمهوری اسلامی ایران رو می‌خونم. مخالفا هم نمی‌تونن کاری بکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/120498" target="_blank">📅 01:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj0vDORE6vCYn7d8RLQ4ZkJcMS7qVfSSH372FY75Wvxgmoyj9jRg5lIRQESAyRMAgXunXRWUGQrnPO0YPjaFmEy0NEMjiCde1oYGSuU4TMyoaOerk3uyduNwFIaNsQEON5vg0cEagKkmQ2ofq9FZVk51BvT1sdD94h8LEN521eEUEGgg74FjBpcmduSA-RovkxDIKhPhKqWieiBPk6-OYioTcPqNsiwqNvk5O57fOBY9TeSq7MUG_UCsptX0ZROSOgtFonbAaLwLrHl5QJ4KyepxJdORJ3ASuaS1AdZ5wAr6CU8SJz3EGFLMHwlu7uLDHzXRkC61tC15bfUAj4vBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: تو آمریکا 9میلیون آمریکایی پرچم ایران رو دستشون گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/120497" target="_blank">📅 01:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شبکه GB News ادعا می‌کند که نخست‌وزیر کیر در حال آماده‌سازی جدول زمانی استعفا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/120496" target="_blank">📅 01:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان مناطق اطراف صورت گرفته است.
🔴
کاربران فضای‌مجازی گفته‌اند که سوال‌های بی‌پاسخ زیادی دربارۀ این حادثه وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/120495" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muPamYvHylvpxwzcsDCYF7ne_-VAfQ94A5Pak4RbHrtCP-dgf7_7WvHQathiKKmEiAWIjD1GPc86SDQoseqEPsb8K8lA63til7hXGM0SuQX2bh--0UK6xgl8PPJP-qUWhIMqij1vDysCgRmKDWw-fKLTV4dDR-m6DACRlyz3zKe9k7mhDdaakZrEJwTUEP7ZH3aUcwyM1DxySpEh42HzzhWTimNxuSjWfuWgr86yn7qg6n45Qj8MEjPO3CKpwW9rsA_6Q7Bo-pRcF_Opt9LviIXKY9vjORLs9t_dAfVgAydWHIIm-uZInebUL5SGfxkdyUi5Qw1CP4mBpGurvtEtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
🔴
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/120494" target="_blank">📅 00:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fHbdUxkOTZCbge2O7n4Te3n7HeNvuSX-EW7ZizvIAJ5txDN_1hJoOaGU4ZFOKoLoWsgf3Gt6k2TnnxfqsLnHIdoc6bFBwQ7LNTGsX6k8BeuOKdnYbnHWzY0CrE6PhMj3r95QHxuzOOKU_EsesE1txKFrwpj7M0iF64fsZa2_6m5V_vG2QYw0YQPxtWrD5uetXmrjLvPgyLVe7k7UsFF0cr7az4DmbJOue5BRwhAET_Kvr3Dd3-QFY3ryid_jptHhfwGmrj8DDDunvh-03CSAp8G8IM2WFOdwU9UrtCoBxOykz3fAUuKpSQ9hEoHcqQh-FZ7_In6PAf6MVNRl2g3New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KE6XUqcspKVQfkffdCV2INot2dzZgwnOUXdb2VdAbV_e4RMaor8LegDub2DI_Fc7Rordx26uDs-S3YyuIXAcjTFpR4AtMLoQAd9wwFKmC8Wwg2aKNtq8d1Gy6sQPwImK__Lq4XnvLk8fetIiRGFiY9zyDiT_QWaH01XPp_DvTptUWLdr_Q4XqO3UyGCbl2e6PpZVDHkCif8sT1nNkssGu_Jb6_qhrb2z02j-8aJH9xe1-5MPxveTYnEM61wCTlz0F0BzqcIIKU6bFkRL8Ta5FdDId-U7fx-vkpYg1oNl9rp6CPTWl6uzNNHwbvIAbgRLYnuQzda4UhhD_bMd2cTXRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی از جمله Channel 12 گزارش داده‌اند انفجار بزرگی که در منطقه بیت شِمش دیده و شنیده شد، مربوط به فعالیت شرکت دولتی دفاعی Tomer بوده است.
🔴
این شرکت سامانه‌های پیشران موشکی تولید می‌کند؛ از جمله موتور و سیستم‌های مربوط به موشک‌های رهگیر Arrow 2 و Arrow 3 که برای مقابله با موشک‌های بالستیک استفاده می‌شوند.
اما هنوز مشخص نیست چرا این انفجار ساعت ۱۱ شب شنبه انجام شده؛ مخصوصاً بعد از گزارش‌هایی که آخر هفته درباره آماده‌سازی برای حمله احتمالی به ایران منتشر شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/120492" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6fa999c5a.mp4?token=oDcbJAt71o8shpHhzlmt55g6Zrgdc6m13Gr8dLc9xEweCv59uQNK3sZQ-AzPYL9HWsdYfy7ZiF6umeuPaYR7OURUiC_pk6ZSGE8ZH0sxOkCWQ-IhJZb2ZZbrn0wrk_zQoXuoug6wRL_rxfcztOLSi5dzPggULF2SrCRJ0Xw3jg7I_PaGQe0pRr_Z4_Vn3juP10TIDDiquMMhwyOv0CDbhv2Y0Uu8mIlM-Ybf8cmuecXTiZNozY2RUNtpJ51riMRFiqRDtJYl9BEXC4pJ3RNjaOiMGuQnPXaGpedGmzXXZ1sdAVqExgIk_qKWVIQPAmn_fuX-WCjkdNaxPcgetAd7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کان نیوز: حادثه بیت شمس اسرائیل یک انفجار کنترل‌شده داخل یک کارخانه غیرنظامی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/120490" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: این ۱۴ بند شامل خروج نظامی آمریکا از مجاورت ایران، پایان محاصره دریایی، لغو محدودیتهای فروش نفت ظرف ۳۰ روز پس از هر توافق اولیه و یک ترتیبات حاکمیتی جدید برای تنگه هرمز است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/120489" target="_blank">📅 00:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج: در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/120488" target="_blank">📅 00:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رسانه بریتانیایی امواج:
در هفته منتهی به سفر ترامپ به چین، ایران یک چارچوب ۱۴ ماده‌ای برای پایان جنگ، به واشنگتن ارائه کرد.
🔴
یک منبع ارشد سیاسی در تهران که به شرط فاش نشدن نامش صحبت میکرد، به رسانه «امواج مدیا» توضیح داد که این سند شامل ۱۱ ماده‌ای است که در ابتدا توسط دولت آمریکا ارائه شده بود، به اضافه سه ماده‌ای که ایران به آن افزوده است.
🔴
این پیشنهاد که تا حدودی به دلیل تشدید محاصره دریایی آمریکا علیه ایران – و ظاهراً با ناراحتی ترامپ – به تأخیر افتاد، حاصل دستورات صریح به مذاکره کنندگان بود.
🔴
به گفته یک منبع مطلع، پاسخ واشنگتن که از طریق میانجیگران ارسال شده، کل این چارچوب را رد کرده است. گفته می‌شود که آمریکا بار دیگر بر مواضع از پیش تعیین شده خود در مورد پرونده هسته‌ای تأکید کرده و از پذیرش این پیش‌شرط‌ها به عنوان پیش‌نیاز هرگونه مذاکره خودداری نموده است.
🔴
با این حال، یک منبع سیاسی دیگر که از جزییات امور مطلع است، چنین توصیفی از وقایع را رد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/120487" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/120485" target="_blank">📅 00:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdtwhL7C28eWBMKyeIA8HvGsAa51UeFzGMzeQvFEMzDQp2cRhBzz0Cj1I2THNUZTZmPKDYJPqyHp7hjnw3S2xAYghKcVl-9mH4UsZ4pDsdTWQAOgkU0fL4T9uNC11ToDeDo9RUlHLfJXAWEXZW6WZ_vQKSit9a9hEMpyGFJ02EoWziBBX7qqPGlJissh0dL0Ga0VmmR-OVsgi8IVC_sMtYNsChZU3gPheIr3KCbQmlLAKuim5z5Lfw4iK7GCCM4ORHKGSbgGorkpw6jQX0_blds8WDuaK-H3Rig87llpYOyIzp-S6Hv7veX5aK6QTbx1n_tZRaFtv3TCmwI4xbCVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ عکسی از خودش و شی جین‌پینگ را در Truth Social منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/120484" target="_blank">📅 00:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87e8503cc8.mp4?token=uRi4EvM3WD5THqq6P4R_ka8vp4wYO7AZa5UbDWCeWKuhSnr6fbBFMs9qsXGfAwlVt3gha14tLCdGBUYhiwv20ukyOlkSc5iFJHhk_2y8vVAoO0mBM8AsHOlGZ70bGiM3Ku2g3QwwlhsEUUtUGnnq76EXjOnZTsq3ltvR9S28x0nYl11kkaLt5xvI6KA0Lznvua0HoP31fe8zjjT3U2N5nFXp0_jibZVZYvMV3aMR-7VNXP3HjU-Xyu7WGO7q3ujk88wpNTWDSUG4cl7DOKItoh2fw0-u628Fjdv_JNSThboFgLwTn3FBChUPS6RBMEaaf00P5XxB0JwL16m22UDRBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش‌ها از انفجار و نور بسیار شدید در بیت شِمِش در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/120483" target="_blank">📅 23:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfDCMoYh72YCU934UcBGgcRsmYJ430H_DTathnhzTFHCmW0h65HTVt7YfzS1Z5RxUMhMzHfJCShkkSL8zDbkBaKCrme4tLAuaEhTy9rXjsBUpntjCX9LCcpyikXVRfam3rGleKXObe8sRogyTnaXjeaufFLVQ0YcL_h6iZ0vK8FGYp7ThXXPOkG2MXOXrZabqqYEMadQ5PuecSD4FnqPbbPBX6XFwoEt7tBtRnpKTVLv3Se415-OtgxJQ8Dp79AdM6xFeFFAepeSLgHx5rItwLE3UAxdi-E7_grN-7SXkO4TcKqt7N5IYujsCUklUlAlPWSVJbXeTRaryYMPMHEqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
این آرامش قبل طوفان بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/120482" target="_blank">📅 23:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPuWCNQ0znGpfJIOBH3eZTh4rZOT7f_vsDvtmAxSPulFVXPppgqcTqI8nGyk-BkRDR_bIOasZjnnbWGEo3_Hm-sgdSAVdGRCgK_zi44fiI7F80At6p6jYz0ChjLlJgBW7kPacqKJUlH48Qp41UsNmIyPoDxMHQbUKS-eYLMiIJAvcViCjOVxjOdQ0_MDQ3xkaoghpGmIea0C94Thb7EK0vI1lOep1znHpUX2xxaF4PUK0lzSXLD2-xb6JtcBl4upLnDOUrQJj5-TKivQZ7YSC1u_YplreBIOGmkJjuMJl7Z_J51fH8HRBlxaMUNC0MAXlx6HcZCeN4DNNGz4XCOBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید پیامی تهدیدآمیز از ترامپ با عنوان «شوخی نداریم» همراه با تصویری از حضور او در اتاق جنگ منتشر کرد.
🔴
در پیام کاخ سفید آمده است: «اگر به آمریکایی‌ها آسیب بزنید، یا برای آسیب‌زدن به آمریکایی‌ها توطئه و طرح‌ریزی کنید، ما شما را خواهیم یافت.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/120481" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYKAXp-aM-NvadLiC0-2um3NId7NpgN0Qvr6bfN52dA4W6l4JeF-7aqjYJo9-AM3lZ1IDNKLy4a5qTBbjregK7lF-kOuLSjqiOfW7SUwH48sKAYok89i4q1LKD0S4jc2R9Ui1uD_EicrX_Nx8jmf3jbTB2TvU6mG6wrIeDEkMGNp58q72d8DcU8gsQQVJzVDIBloqh4SCFgEaxE0PXudjp7oikhiNtB3BcoIyUdAB4v_y8Jhg7_UKInvl1xQ4Dtl5zbkk21T8pF9MiJwEznJyCClzsCcwNWhCUVRsywuN9f9ZD1OaEqVa9lTDdWz_RMR-3xiuq5wFSnLRhG6Nx8Hyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1374، کل پاساژ علاءالدین: 500 میلیون
سال 1405، آیفون 17 پرومکس: 500 میلیون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120480" target="_blank">📅 23:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120479" target="_blank">📅 23:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
العربیه به نقل از پاکستان: حضور وزیر کشور پاکستان در ایران یک روز دیگر ادامه خواهد یافت تا در مورد چشم‌انداز ازسرگیری مذاکرات گفت‌وگو شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/120478" target="_blank">📅 23:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
العربیه به نقل از پاکستان: حضور وزیر کشور پاکستان در ایران یک روز دیگر ادامه خواهد یافت تا در مورد چشم‌انداز ازسرگیری مذاکرات گفت‌وگو شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120477" target="_blank">📅 23:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سی ان ان: ترامپ بدون پیشرفت در موضوع ایران از چین بازگشت و نسبت به مذاکرات متوقف شده بی‌صبرتر می‌شود،هم اکنون ترامپ در حال بررسی گزینه های نظامی بر علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120476" target="_blank">📅 23:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/120475" target="_blank">📅 23:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXOgL8hG9x5FZLA6DN77WAxL2C8hVE-tz_g9JGG0XveiYbXfc36G7cgTv8FVYGmFmw8J7KgHRCw9tzIZUK6IUjucg2yqsbvabny8yfZxbWeu0eT_XJUgfC9JVn_MfZaDuHDA3lJGE_B_NACILVgFvFRxSE0HLUJrHgUxlgBadnvyXSnXShRCH6q5hds-Qg4uQcxUhmOFHIE78t8eU7qTVS3w5V9TzQRZIAfeZc8UQ2E7cPLHIx0IMIf47NDmpgbASn3iVBOMka5IXx1X8MrO8tHXcm95PZrogEAbbifyrmMVgUuvJ4x6kpI4NFTxdI756Y1Dmdy_mnOw0ezCA356hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/120474" target="_blank">📅 23:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4581f1ff1a.mp4?token=e217og9J_i2Wgs3P0tWMcf76wdQGnGLZd8edQulX9AvmX_TH7KqOQT92YHyG8wfv_6OMJm9UO-9UM3dSY2VhjtW-aLlRUuNzc6-BatQdmZVOtYtHFZjCEwFMUPi7AFtjva9BUujTVgR6j0zXz9t6aUtygTjiidsx7oLNlYg7f-U0OBkaQv8X3rNG10xx91dq8SbCNC5VmTWMfX5GMOkWsT9c9iBRsWZMVFVWHGkXULlCSuQ8fpoDWHDvFYBfCMZ4tXxqWZWP60jcVh1uKE5ePXScmsFQRA-kAsK6oIp-qmiYJvm-8ZRKm4gFfnlj5NMpspB0m5LK2RFZCawM44e7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4581f1ff1a.mp4?token=e217og9J_i2Wgs3P0tWMcf76wdQGnGLZd8edQulX9AvmX_TH7KqOQT92YHyG8wfv_6OMJm9UO-9UM3dSY2VhjtW-aLlRUuNzc6-BatQdmZVOtYtHFZjCEwFMUPi7AFtjva9BUujTVgR6j0zXz9t6aUtygTjiidsx7oLNlYg7f-U0OBkaQv8X3rNG10xx91dq8SbCNC5VmTWMfX5GMOkWsT9c9iBRsWZMVFVWHGkXULlCSuQ8fpoDWHDvFYBfCMZ4tXxqWZWP60jcVh1uKE5ePXScmsFQRA-kAsK6oIp-qmiYJvm-8ZRKm4gFfnlj5NMpspB0m5LK2RFZCawM44e7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران در گذشته بارها تنگه هرمز را بسته است!
🔴
ترامپ : ایران سال‌هاست که با استفاده از تنگه هرمز، جهان را تحت فشار گذاشته است.
🔴
ایران از انسداد تنگه هرمز بارها و بارها بهره برداری کرده! (بارها تنگه را بسته است)
🔴
آنها در گذشته تنگه را بسته‌اند. از آن به عنوان یک سلاح استفاده کردند!
🔴
اما الان نمی‌توانند از آن به عنوان سلاح علیه من استفاده ‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120473" target="_blank">📅 23:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یه پهپاد حزب‌الله مستقیم به خودروی ارتش اسرائیل خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/120472" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/120471" target="_blank">📅 23:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
FLASH NET VPN
🔥
⚠️
شرایط جنگی؟ نت ملی؟ فیلترینگ سنگین؟
💪
ما هنوز پایدار و بدون قطعی کنار شماییم!
🚀
پینگ خفن
🌐
سرعت فوق‌العاده پایدار
😍
رضایت فراوان کاربران
🤖
ربات کاملاً خودکار
💸
نرخ‌ها پایین‌تر از همه جا
🇧🇬
تک لوکیشن بلغارستان
♾
بدون ضریب
🔗
دارای لینک ساب اختصاصی
━━━━━━━━━━━━━━━
📦
۵ گیگ ➜  650,000 تومان
✅
📦
۱۰ گیگ ➜  990,000 تومان
✅
📦
۵۰ گیگ ➜  4,500,000 تومان
✅
━━━━━━━━━━━━━━
🛒
خرید فوری از ربات
👇
@Flashnetofferbot
کانالشون:
@flashnnet
⚡️
FLASH NET | همیشه آنلاین، همیشه پایدار
⚡️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120470" target="_blank">📅 23:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb22a2603.mp4?token=XhQ_X4qZ9acyNrHt5pIxqdiDs0Q9bL2u2Bwoe3QZVNUIPFfsnlRjI023GDFyiX8H5M-PrCqNY1N0HTcsewbUBkwnxal_q-TlBfO5Usu4XBLBKL_6J5fQwGwj2oh7ta64N70HKQP1-hL9piHeNNyk5IfvnNnsHTODq6IYgji2_DjSA8Jd7ZkzXLhw1_zRtXWb65OBQe4ap_IA77Id6IoKQQPf5ZAjFKcBmERyXKlJKUqjBWFYCIOMX_Na-HTAJb2obhJjwJ9zUy2T3q665PMRkiPjHDrDLuFcKzsAaw1qtvkOVDvoCCwbKnFwC1nHkQn-fKWcgBjTaKJeZMpu7QKqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb22a2603.mp4?token=XhQ_X4qZ9acyNrHt5pIxqdiDs0Q9bL2u2Bwoe3QZVNUIPFfsnlRjI023GDFyiX8H5M-PrCqNY1N0HTcsewbUBkwnxal_q-TlBfO5Usu4XBLBKL_6J5fQwGwj2oh7ta64N70HKQP1-hL9piHeNNyk5IfvnNnsHTODq6IYgji2_DjSA8Jd7ZkzXLhw1_zRtXWb65OBQe4ap_IA77Id6IoKQQPf5ZAjFKcBmERyXKlJKUqjBWFYCIOMX_Na-HTAJb2obhJjwJ9zUy2T3q665PMRkiPjHDrDLuFcKzsAaw1qtvkOVDvoCCwbKnFwC1nHkQn-fKWcgBjTaKJeZMpu7QKqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسول جلیلی، عضو شورای عالی فضای مجازی،چهره نزدیک به جلیلی: اینستاگرام مثل اف۳۵، اف۲۲ و ای۱۰ آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120469" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIXiAzAMrzj6id_NwPa3EZ0k3L0wmCfZtJJs78p5f8lpTCKuU3mo3wNQmbUC0Qm-xjDDpjFziCnVrOybtMQ43agHck7HLPm1JArZ-sJcnICL-1S2vf92cEzxU6-XNZayGR_vlHYpy0SusdKFmil9RDIFYxR7dRC32JbGhN5821evZEKb4KD4oCqDBUBOWXo9j-302wzbbulJdav5Y9ahDbLOvGEOmFJhIM-tiivw1qPXcyU-5lO56rnGxgxZ--mw0nqDBGkZS6zx12Mn_QDx-88D2bDbPPaXUtHjws_q0B_3DKVPsBNlp5u84ZCGfaMFSMfdC4SCSaVWxNas6mIfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: جهان در آستانهٔ نظمی نوین قرار دارد.
🔴
چنان‌که رئیس‌جمهور شی گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
🔴
آینده از آنِ جنوب جهانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120468" target="_blank">📅 22:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9y1FxQ0tgw4_Ls6AhWxe3tFYyfmJHnKHLxR-B3YFftdL63p0I_iTxNlumcqYQfDb6aj9jmLg9N82FEbAy4RLgLVf6nikr-rVdVyfBoyVYNT0Q36twsOh4fG5Z8zQeMNdJ06ipjw9BQiWK37svlHj65zkiP2M_qNrSIm_BNV2hcg_3ZGP4sewUBztcflUIIjg0kYOTXVU52HvfPAfobH9II6XAgyxAJL2wvDxgFLnvQbdx1IckjQAHiysc4j9_w6tBdsu-1Zz9N9K5YvT6b-gRt_a3qAQm_ESuDoPm3c9qjJ2pd6WnooNUAZF_jxm_m-pv7M7rEV7NCu_g99PPiXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت بیمه ایرانی تنگه هرمز راه‌اندازی شد
🔴
سایت «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگه هرمز را شروع کرد.
🔴
بر این اساس، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج فارس، تنگه هرمز و آبراه‌های اطراف آن عبور می‌کنند، ارائه می‌شود و پرداخت‌ها با بیت‌کوین، تسویه خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120467" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120466">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کوثری، عضو‌ کمیسیون امنیت ملی مجلس: دشمن باید بداند، ما در خشکی و دریا امکاناتی داریم که هنوز به کار‌گرفته نشده و در صورت نیاز استفاده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120466" target="_blank">📅 22:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUa9SIAKgoneyP7x1Mgv0_GKnR3SWLH2CHc6Hp3rV_2yPIuIYLsDUeavch2Sbi2MeRNPfHMEXM1PE5knl0jk52F_pqZwISNQSGfC5Ohscjt90b7ca9j_EcwxsPwntp23fIQwBiwKoqGpkHpHPv6Kf5SyaQGRvjhnt7gbN_21QUIyCjUBJ5YBwF_73oTIt0K44hZ4G_LSPL447wMiQyVo5lpxuJa18l1vpCCOVF5uzACM6O6BtTGa6jSyU-xZrKUOqEupLMf1CKA4f1Vj3V1gXERMjDv2NzE86uhR_lxgaarVHVF8VxyiIDMwwJFjphXRVYgmhETPmtgxHVLhzZdDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورل، مقام ارشد سابق اتحادیه اروپا:
ناتوانی اتحادیه اروپا در دستیابی به مواضع مشترک در مورد مسائل ژئوپلیتیکی، جایگاه جهانی آن را تضعیف کرده است.
🔴
اتحادیه اروپا در شکل فعلی خود قادر به پاسخگویی به واقعیت‌های ژئوپلیتیکی پرشتاب امروزی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120465" target="_blank">📅 22:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120464">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از سخنگوی کاخ سفید: رئیس جمهور فقط توافقی را می‌پذیرد که از امنیت ملی ما محافظت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120464" target="_blank">📅 22:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120463">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رهبر حماس: ما هیچوقت تسلیم دشمن نمیشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/120463" target="_blank">📅 22:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سفارت پاکستان در ایران: گفت‌وگوهای سطح بالا بین تهران و اسلام‌آباد درباره «تلاش‌های میانجی‌گرانه» در جریان است.
🔴
وزیر کشور پاکستان به تهران در چارچوب تلاش‌ها برای «تسهیل گفت‌وگو» صورت می‌گیرد
🔴
وزیر کشور ایران از تلاش‌های ژنرال عاصم منیر برای «حل مناقشه موجود» تمجید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/120462" target="_blank">📅 22:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
فوری/گزارش‌ها از پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/120461" target="_blank">📅 22:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyc3HqnHKKqAfA2b_sXo217rMpawwlZ413N92K-OMy5ZGyPWPTsWkTVO6kn7o7MvLaCHr8K8tLYjNcnPBwmi5Skncz1-UHwjSEcVt34zGAlMsL2oiHClx-8jq4yeqkduQOtqSJ92axmVavOCeuniuQW_kExK_-ZjoFpNIbWfCHzFVl2q33l3jCgTOWDTdxo51bx-Kx7G3yBVcLqD6Gm20f7UnSELwcfqrP0aAl2soRAwwyA6Bxgl6fJs8eAUpQgdAz5Cjxa9PnoNZO8YrH2kkuFVyJcvTofrKpvloQ1w0s9u8EvGeQ1L1nG4sNqjPy6Jz8d3zt9iLVV66eoZQVl72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک افسر اسرائیلی از گردان جولان در جنوب لبنان پس از انفجار یک خودروی بمب‌گذاری شده کشته شد و به گفته ارتش اسرائیل و رسانه‌های اسرائیلی، تعداد کل کشته‌های ارتش اسرائیل در لبنان از آغاز جنگ به ۲۰ نفر رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/120460" target="_blank">📅 22:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران و آمریکا بر سر یک موضوع توافق دارند: فعلا درباره سرنوشت ذخایر اورانیوم گفتگو نشود
🔴
در حالی که بن‌بست دیپلماتیک بین تهران و واشنگتن ادامه دارد، یک نقطه اشتراک وجود دارد: هر دو طرف می‌گویند که در حال حاضر درباره سرنوشت ذخایر اورانیوم غنی‌شده ایران بحث نمی‌کنند.
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، روز جمعه دوباره در هواپیمای ایرفورس وان ادعا کرد که ایران گفته بود مواد شکافت‌پذیر را به واشنگتن تحویل خواهد داد و سپس از این کار سرباز زده است، ادعایی که تهران آن را رد کرده است. اما ترامپ ادعا کرد ایران معتقد است که به‌تنهایی نمی‌تواند این مواد را به صورت فیزیکی جابه‌جا کند، بنابراین این موضوع فعلاً از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120459" target="_blank">📅 21:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو : اگه آمریکا دوباره بخواد عملیات نظامی علیه ایران رو شروع کنه، اسرائیل آماده‌ست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/120458" target="_blank">📅 21:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=TIIA0OwCdLQx7cf1CKHf01OI4qgx0P251JunFpq4RG6stAKL6sxpxWst8reExzgavX7u_rztAk6TJLnPRsINiKMl55-eJcBZX2mSgfEA2h1qVukNX6vBCPRj8FXBTxT2yz1b4zqsp4fDpoKb9KNWo5uXJtO8HHw-hx0u3epboUTDpoiqmNVPPhy4FK1x6NTJh_dBcBXZ1z4pvEwpnHct4kU8t1W2fUoIIbOV-SU7BvED9MW0XOSe7vhIIQKcjzdGPdZxZ-hVsg5lwoo_MAgSsoDfI38uKSF0jhM5VCr-469xXLLc1cv_UzGXbjOVffSfg6bpJ_NpfJk39PBDy_P7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=TIIA0OwCdLQx7cf1CKHf01OI4qgx0P251JunFpq4RG6stAKL6sxpxWst8reExzgavX7u_rztAk6TJLnPRsINiKMl55-eJcBZX2mSgfEA2h1qVukNX6vBCPRj8FXBTxT2yz1b4zqsp4fDpoKb9KNWo5uXJtO8HHw-hx0u3epboUTDpoiqmNVPPhy4FK1x6NTJh_dBcBXZ1z4pvEwpnHct4kU8t1W2fUoIIbOV-SU7BvED9MW0XOSe7vhIIQKcjzdGPdZxZ-hVsg5lwoo_MAgSsoDfI38uKSF0jhM5VCr-469xXLLc1cv_UzGXbjOVffSfg6bpJ_NpfJk39PBDy_P7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ درباره ایران در Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120457" target="_blank">📅 21:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3O4ZbyzroxOo4kAZ2GkVhfHs2mSGSMDHsTt7dsGl19HOf4_Syaqb0yVWo_5007pm_l2gHy-1ZC4y-pWzy2dEysBUjTX6UQdG27aq0SyQkKC_PxDsUii87rANb4Hs7ptIyWTFZWnXGI4n0qNCc7CzFXXv6AcES-_iCG8zigN_asd8UtFYZ4yTzs0inY1L7ogoLl-1bjDO_JppoMNPWOkQL1b-O4NBuSjqo1Ry6jzWOpboH1TNAo9QzXvU6BI_eajfx21fk_ZKx4U9-hqdVDycAn2oDNMXnzYlh2zdF8IxQCiJSqMMzyAKsuSkU5sZIsyBS0t7X6-GeTNDrBZEJeGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از شهر بنت جبیل، قبل و بعد از حمله اسرائیل به این شهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120456" target="_blank">📅 21:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره: بیش از یک میلیون لبنانی توسط اسرائیل از خانه‌هایشان رانده شده‌اند
🔴
بیش از یک میلیون نفر در لبنان بر اثر حملات اسرائیل آواره شده‌اند، از جمله پناهندگان فلسطینی که دهه‌ها فقدان و آوارگی را تجربه می‌کنند.
🔴
بسیاری از خانواده‌ها همچنان بی‌خانمان هستند، زیرا محله‌های حومه جنوبی بیروت با ویرانی گسترده و ناامنی مداوم مواجه هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120455" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c07hbxi9_Nf612psYP-dDVmv3bZy8Lpn4b9HojdSx6PZBpYE96QO7iE7W-ozB3JORopmna02_o9guuRLKWqlc3Thy96O4p1cz7bTtHGJrsTsNXlhcYUdWBdq83DToEBQ9Da98muy1d_xlzGtQvyWmET4pkX2h9dfaGjSGrg-0O_KMUMFGMsYXK2PlVx1r5feMaOqu9Q0Nz1o1-hr15H_S4dOM6n7mEdwFojCKxIKTT6IDXswpOriUH8mIQ3rvcmh6lfA8Uz-MkJddx7_oAEizjoPMxueQG8WS59aitpO8wjSlVY7NbBQjoH_73n38aFHrC2qLSwVZ1QBJYLBZGUO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، بایدن رو مسخره کرده : چه تفاوت بزرگی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120454" target="_blank">📅 21:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcpD4kiQU55_MkUBfYw6vPkpXLi2iSwdA69DSt5OUm3h5zIP3oH7adp7ivw5Ht-Kk8F0Oo-DT55WQ7I474gQu0FRED16WY3THgCCtBr091jcMRjvrbUIhLn6W_agN1a_sQNbJ4p8L4LgGLV_nfo9QBwPfwFpL1z0_pipmEV_VYeZvLsgIiYc49eLwSRwKKneTD34PWB3A5yy8Eea_2Czhe1awrWrqUJXgenO1vpcwRtVmjCJ0Zyji8YCwFVC7XOBFPFslEqXXiG5tkvWp4-EJ3mpsmOgPQ0geliEKABE2CpZt-4eEC6126jOIJUq5ymFi6OnvYVCATOV8BGvGaYg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابک جهانبخش، خواننده: به تازگی از همسرم جدا شدم، من اونو از ۰ به ۱۰۰ رسوندم اما اون با ۲ تا بچه ولم کرد رفت. زنم فقط به چشم عابر بانک بهم نگاه میکرد و از من به عنوان پله موفقیت خودش استفاده کرد.
نظرتون؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/120453" target="_blank">📅 21:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : تو اسرائیل یه سری برآوردا هست که میگن احتمال داره جنگ با ایران به‌زودی دوباره شروع بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/120452" target="_blank">📅 21:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqce6qwBRY2TGMKHoepQhhNGNuyPQIssSlfMUx4vl4Q7mRZ2dm3dZdQ8u_qq-43k2NWtK3zC7CNmxobnfBxXXe4XpikoweVWk3DLuYdNYjvSwgASIGWpvdOv_ubriq-pn5OYsJi-yfqXIWn2W6rQ4LE0mDiFMNCITAT3gDhhyWy2IbLzTcPulj_90eJSG-jKVUHKt0-tLdXqPrW-JEgJog74S7shdXOXl6uPW5l4N2vUDKsF6ZYKzXJ2it8lIldsTtvq6vufd42GBtZT9oTOBs4qdEIXT00WQadcZSEIF0oUUitXuLrWYvv63S4BOGW73f0jh6Jl8ecFHl1D0VjYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray استارلینک
🗯
گیگی
150,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید پیام بدین :
@v2safeBot</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/120451" target="_blank">📅 21:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwKvL-bOzwffxdvn61_F0i5h-fhofcnUvAcawFC7ymyM9HpqcF956AFolzXnXkizsGCJi1vFcLoMOssgyMQAMsvy7b4pZUTegTjGM0wRlFFRH_sRMUJy6gXuRRK3TyCRh2DdCYNRIx6rqykLlr-QxLgyTwPpfP08zsniy8wvrOf6YNAb4Kc0HqV5WnrH_e0l5YBdA3bkzQChEOyrZU7YIbne0QCCU3G_8DwvUEBnL2e-CpbhENmxIljfGJNsqiMVNmcIRdoan3TyCNsVlvHXbUgvYGjYOUhIz23xrTDDV2adFC3pmeV8A5ndtMDgeLEJSe-IB2uTbWFmAauAZbaEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YowlcsejIwUWVLMxVlnFFdRKNvvgZbDmYo74PLMdSbZaHFt2oy1jAnoWkx2DmCW5gEtIb37N2UJQTGFxW5S7ySvOnlmaeBDefCpPNMJbyKXTPpczlVy4QUo7FpSrDxb0b-gfQyF_K2EFA1mBqWBlvhnn8A2EZzBtqJCcQNEJMDIWqP8ujcLLAAdlyKQHVeFgwHKp3tq5eMjGHTPExZfxLKVXuZRpnX90zx3pLpi61nNu7KuqFuNNMuzrhwS-fQQ3qOlRDe72Gvbb4Hxras_x-3SdETCnhO26ig8nOybCFZ_W-jjouLLBCsQdNJsrWTp3HxB7kyJGNWdqzYOY0qZtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZqRvJGcJc2ZWz4MlvLyOsKAHUkC7atCiKKLRiGUl76ln3ssNc2Chr4LS0pApWSxflOM32oekdFdbCM-_5FxX4sKl8iUshwVsqyPGUBMjr_2lH3pRpL96_-GOAjInP-wL_gdlga7r0HPnMFhIHlA0LnEmnz_7jWPVwZmHoCr-KvOOXqhTFT1ERDFxHwYa2puCN-pozEI13dzSUkPP7cmwyueRqd8s9OrSj5baj7BdI85wFu3Md53b3fUhE5Mg8qMRRlA4wfOU3Q1WBKrsPatAv9dJjBClbY1Hujx8Tw3F7Pmqac8wfZHYwq9bxzmaj9W3avJKR8cf1TRhlC8H0zCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUbzNYZ8-xO-zdGlVvQEi-HNf5lkXVv9HBi-vEF8JB54u6hLL8vUb4dNt0gpslxDdtP1apDrjL3aI0GPRYvDdsr6Q80rxQBc8Zc1Khb0Y8CAVj3tXNFJlNguMV1J3SIPHHlbX7JVOIr2V2tZmWhHtiUKzrpFEl7t2dviFMy6nCMTB7kbQmwcHnSGXu7l4eEg5eQPeuInrrn750LMAXce5rSuCqXUoEevHfVjVT_gl8guND35062DEiruw27T3tREeiZTWMGNGE31X0GW2etlyvGCMWigo-XP8DvAmkGBYLfKwaV2B9Dzs2Euz3VfrIycDTsrvycGZRNLg9XVAv4wZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به تازگی خودرویی را در غرب شهر غزه هدف قرار داد که منجر به کشته شدن حداقل ۳ فلسطینی و زخمی شدن چندین نفر دیگر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/120447" target="_blank">📅 20:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRE5uqT9QskIE9pDh_k1Vt92-oNfhc3hGbqlWwtQ7-twc-V67zliu_B_iFUfD7pCi12D7bzxnbAin3Xk6hdeq1d2ZfzP7T78Q0yFMGTtBAd0OS8qyFl2PUb9QSKzgyt5Zc5nDAW5PI3BRuC5yWBwTfDZMG-G_oAEyRJmXiaEMMeuMZaHdJTWhSUITVuu_o-KgCuUK4XSbUIz6ear_wq6ff27iMu9a3SpHl_1smpmOBSfLa_Ekb7zKWs2pX9JeV2I62Ep4G9_SFvj5wL1NdM14Yx5TWBYuWxQPUEJiFG2tIFwXHWNOM542gEcoMD4rOuFZ9YLdKWGdHudjSV4VWl5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت مرغ
🔴
اردیبهشت ۴۰۴ کیلویی ۸۵ هزار
🔴
اردیبهشت ۴۰۵ کیلویی ۳۸۰ هزار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120446" target="_blank">📅 20:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff57b4508.mp4?token=EZCuZRwczKwLKKA-RncHbThczJ7_MscyEPJZ-qerO6d6Pv3LiRvM7SU9Bm5xQh3Im1fjCTjAb1J1hD73Oj_Y2xk1UokVeukAeWVyfLN-MMX65pxvAQGaxx3mU6I3HXTGDcPAsjhCApoR-m3iOKhKBCnhdvRARFTFvpPWOyLSWiWaeZhzHMI9EHQeOxIaPfCHQ0tfVgC25dLCPWDJqCht4tl47mvmR2fD2pt7FkUeP0CzsSyyaYAmJ_qo0AylC7CCx_ILwf4bFMTZwgNbnaLYQHWbRA78_Dg27qKtxdWXznz5DLYhVhAUwVS_y5IhwoIkBR0U_0aZlfzJz1zAFmMlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff57b4508.mp4?token=EZCuZRwczKwLKKA-RncHbThczJ7_MscyEPJZ-qerO6d6Pv3LiRvM7SU9Bm5xQh3Im1fjCTjAb1J1hD73Oj_Y2xk1UokVeukAeWVyfLN-MMX65pxvAQGaxx3mU6I3HXTGDcPAsjhCApoR-m3iOKhKBCnhdvRARFTFvpPWOyLSWiWaeZhzHMI9EHQeOxIaPfCHQ0tfVgC25dLCPWDJqCht4tl47mvmR2fD2pt7FkUeP0CzsSyyaYAmJ_qo0AylC7CCx_ILwf4bFMTZwgNbnaLYQHWbRA78_Dg27qKtxdWXznz5DLYhVhAUwVS_y5IhwoIkBR0U_0aZlfzJz1zAFmMlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا به کشتیِ که داشت مواد جابجا میکرد با تیر هشدار داد و توقیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120445" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
زمین‌لرزه ای به بزرگی ۴.۵ ریشتر دقایقی پیش گلوگاه در استان مازندران را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120444" target="_blank">📅 20:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا در گفت‌وگوی تلفنی با شبکه فرانسوی «بی‌اف‌ام‌تی‌وی» آینده مذاکرات با ایران را نامشخص توصیف کرد.
🔴
او هشدار داد که در صورت شکست مذاکرات، ایران با پیامدهای سنگینی روبه‌رو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/120443" target="_blank">📅 20:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرنگار سی‌ان‌ان، کیتلان کالینز، می‌گوید: «ترامپ ظاهراً نمی‌خوابد.
🔴
«یک منبع یک بار به من گفت هیچوقت کسی دوست ندارد در یک سفر طولانی مثلاً به آسیا در هواپیمای رئیس جمهور باشد… ترامپ همیشه بیدار است و حرف می‌زند، و اگر کارکنانش خواب باشند، می‌فرستد بیدارشان کنند چون می‌خواهد با آنها صحبت کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/120442" target="_blank">📅 20:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020cf5e837.mp4?token=SMmQQfReX0P4VekASyWNoKJwuDCopor35MKoFUOXPs2wMp9z5lGMflXdzy9Mgt9sUIcFeYgrKCIhrPhN5YjonItFYIRtpcXmWpybGD9eiOvxH0kiXRTdPH9WY_KfDJSwXsoNk1uiPDTO6dcXzy8LJmtwZlZdGQlGBEnbZO4NAm-_8kWS9nzYmfuBi1Ox2m_fGM6gKTkzSn1iW3pGJxqQ9W_k2M1-DRO1iB5_HdHZwUKglrh2JM2_qeoyKNtQoICZTvtEZUCbT9-k0R1548jSrZHIWDuRgSdjtB02be8jqKt5ytYbege9tBQu8pQErl0l_BgzwvaQqcOJnHi5udyqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020cf5e837.mp4?token=SMmQQfReX0P4VekASyWNoKJwuDCopor35MKoFUOXPs2wMp9z5lGMflXdzy9Mgt9sUIcFeYgrKCIhrPhN5YjonItFYIRtpcXmWpybGD9eiOvxH0kiXRTdPH9WY_KfDJSwXsoNk1uiPDTO6dcXzy8LJmtwZlZdGQlGBEnbZO4NAm-_8kWS9nzYmfuBi1Ox2m_fGM6gKTkzSn1iW3pGJxqQ9W_k2M1-DRO1iB5_HdHZwUKglrh2JM2_qeoyKNtQoICZTvtEZUCbT9-k0R1548jSrZHIWDuRgSdjtB02be8jqKt5ytYbege9tBQu8pQErl0l_BgzwvaQqcOJnHi5udyqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرده است که در طول آخر هفته حملاتی به حدود ۱۰۰ هدف حزب‌الله در جنوب لبنان انجام داده است.
🔴
این اهداف شامل موقعیت‌های نظارتی، محل‌های ذخیره سلاح و سایر زیرساخت‌هایی بود که ادعا می‌شود توسط حزب‌الله استفاده می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/120441" target="_blank">📅 20:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120440">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e055879407.mp4?token=GNLjYmdoysjOWO77SaAf0fX0QINtbWq6Yl_kFgqzPBtMUezmfCLEJKegj4CfDDZWV5YJyYOhITkQWls0JvCWrDZKU2dvAhJjOvlm1KQol0fOGEJ8pT1xb9IuYbPR3MwS42DiBxUmx283x58qrq10T7AeqadrtA6vY-b3DGK5m3T-LnB00VpcU8aLA4Wq6-CDZ7ZSHnVzMMxrSL94OA9KUmkQjSpJKMh6O9wkZVsqFY9dHHmprBw2sPh4ALN2pazbFfCn6_IuJG4OIfnEqflZscQtCJqEcaTVGn1dwezWNmt8FzNT4D9PXw5WkpK-3AQCFlZT4y5qLSHQIM_Z4zMjwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e055879407.mp4?token=GNLjYmdoysjOWO77SaAf0fX0QINtbWq6Yl_kFgqzPBtMUezmfCLEJKegj4CfDDZWV5YJyYOhITkQWls0JvCWrDZKU2dvAhJjOvlm1KQol0fOGEJ8pT1xb9IuYbPR3MwS42DiBxUmx283x58qrq10T7AeqadrtA6vY-b3DGK5m3T-LnB00VpcU8aLA4Wq6-CDZ7ZSHnVzMMxrSL94OA9KUmkQjSpJKMh6O9wkZVsqFY9dHHmprBw2sPh4ALN2pazbFfCn6_IuJG4OIfnEqflZscQtCJqEcaTVGn1dwezWNmt8FzNT4D9PXw5WkpK-3AQCFlZT4y5qLSHQIM_Z4zMjwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز بمب افکن B-52 تو پایگاه هوایی فِرفورد تمرین‌‌های خودشو انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/120440" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
معاریو: ترامپ در آستانه چراغ سبز به اسرائیل برای ازسرگیری حملات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/120439" target="_blank">📅 20:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کاخ سفید : همه گزینه ها در مورد ایران تو اختیار ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/120438" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان، به نقل از منابع آگاه:
در دولت ترامپ نظرات متفاوتی در مورد چگونگی برخورد با ایران وجود دارد.
🔴
دولت ترامپ و مقامات پنتاگون بر حملات هدفمند اصرار دارند، در حالی که دیگران از دیپلماسی حمایت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120437" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042ae6010a.mp4?token=Z_q84IpNlAaAk4sjuhxmDxX1G5iZtEak5k_N1uzWPnAQi8GXBMKUlA81w8XtDvVUAAbOKYsYzvBXDH7dzeRTNh_dDzf75tGUzEAjrxrf6rJnU4Yy8p9I-in7koIyCNhAbzSoga6s9svDNZUtta-V_gaSJcV4wTWxi-d9bxsX07Qpa4zGVGLWEqL84_c7xvtkLsQKIyo429882I123WA1Sej7HnYOOVbf7ClxR7VGjni8m5FMDdKDGL5x9oJ_D6MUgXzWev0Ja3SBJ_09S2aaQob1sz7z0x9hE4wC2Rq-YziGTfqtYEq0BSHsoQduEA4Xt4JhRbSHq-q-S-QMf60QTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جنوب لبنان دقایقی قبل ، پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/120436" target="_blank">📅 19:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRY-MA60g_DNNgVhriLOhBP9PiXDremonAsrHlfOwxkEbJp6hSP92mI21CEaSOEQCJ8ZbQz3LZX3j9vjYQVSPp3AW01gX50ZohIJTy-ZUkzbuxY3laTxx4WX6SQYcis54OpzhhF4NbMxY5T9xdM9c617RzKwCwKh2hgu6v1uTEFJK7SHPc74Mj1GkJm1zk2snk-np_045IhXj3C6ANVOS272gdcwyoK6MoHnvFVnai07xJ6kmLwuVLJSMSSG-k-0SEzH2YklApnQ-Qezq88S9KR4G8IClPTDzEQgg-SfNqkX5hWN23v2C7T5eh1gNE0R7I3h2kssQX1Yt730dX0dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین، موضع چین در قبال قطعنامه ضدایرانی بحرین و آمریکا در ارتباط با تنگه هرمز را تایید کرد و گفت «روسیه هم همین دیدگاه را دارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/120435" target="_blank">📅 19:46 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
