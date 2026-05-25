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
<img src="https://cdn4.telesco.pe/file/uvLzG3WB9-fqz5zxOiT9TltuL94qUE4cv09Ts6aVCarW3gmxM_ah21s4c652ZHJYbgaHz91L3NmlFuDnNRmT-wXjzmVoZrjlfpPDlsdYjc4Jkwj1ukkGYFTDN3eypZDkKwJXwpJeKILVDajmVJIETlzFpnlYCNpEOCl5QUnYmPJaw8BwKmSbhxhMQAkHcKoSDcfkHNMnPwtJLaCYRn56uRbVwaP1uhZ4BXP7aFTAO9k_x1Z5-VnMgydCFkquEwmc1y3VBz4xvtxy1MT68ilsJQ97mSYkrcq-32L-EeIxjwUZ4k-mbxCj7Nqf46UKau1uqqEVIReuzz-6ctezJYFTfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.5K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On6U572b3yMuNkG6dIu489vTLmhHkW7uq2kR_7unhR2FGdWxHHcx6QDkAl5TBaSDU6_0IH9gKB3n_4F7pjTheaQwN22Qbs-oaXcTcbUc8qbP5fkJIOqJa-PUYCJhJdGWtXIBxUun6C8IlTkfu3lXmdW2GO4ATMqz2j7vHUV6_DpylXyQpclysPFy7I-03onHNlwv2UYg-vlqkpcSVViuF0BmZ1p7XjzlfP5sWGVJDEqjwWl2ejVfhLSVMR7mI7FNeI_miPGbv1EuJyIdgwySWUPnTUCORt9_MMKBHdh8isnlorQHwgeb77dAZZjdwTp-56WyUzXbpY6U6xOTCaZkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJqHCrPemJPklhZbDeB6mH0e8wP0RvOSxjCmi00q4Sfqb-Dp6d7i37mevQL3U-huBK_hxkIpDzYOPHav6ERw6MBnvztoG6c5aUN3lVXphAb9PP-2-7jw6-YdugGCPNwD4qiXkZV2x_Tke0RS23G5J5HlCr5x7WTG4YI-P3I8W4mNRjDPrdwahKXjnN10memcz5gtFkcJIdnWfTltMHSe2AqTfAE-v__wYyRfiuQH5wnnsatD_VEnMu_JilCRz3-yGXBwEmJI_CEtZK5wA-rbQKYoNNEKQp2J-MlrqNZVvOebNMM3S2pKicbj5BMsRJeksGzATzWgKCiBrBQGlknEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwm-AwGQxTCTKEmdK81H3GiB042JrRVvQJN4jmEDdWp99ARJjnBVbrsV7R8pS2Ab2f8K8rnxl8LWq54ocAH4BoKaP_FKPQa9RJsJ3Lv71v5AQPDzrFLUHB4nby18wL_RSU1GdK-GRmym2BbZWUOHegvWkKh5bMIMweHXPX0HN-HbG4_gs8lAHk0AsP0InGB1bjrURuUCqgTq-_6GpDClfPIAhFgx4dm4fgVFkh_K2H9UBngCxhot63aggnNMFjApkGsDQpLpUkWEPbV-aQUYoeDOx5qhQWJioaGsaIn1H8Zd0NjIJ98vGfgn4h0UBag_TpUsc71_6ozSKPsmXGJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teAoLK6kRmg43FvnSkSILSUOarcPtzXEUr3wb7u7bxkGlaZ9lGv4qkoxieRedlkTlvBhgkgalyU33ChYaXDOLN7CIovMQFbzPIQae1eCttKUjXlYRhYvha7s4yo4zrmjYdeCpgObeGBPFn1Qi-E6a6tI5ebg17InBTAdntapjpIOSB7gOhrYN2pjt9tGw7KCNLq89yuizfIvrL_K2ZCsfetqjWtlQ5ZuVSCOWqn50q5Obo0ZsjHSBaZ2gvxArdt8LcmBpzHyCwOQKY1w1EeQYzpXjQLx529oAMImdpoW6UiZrFBMgxByFQxZArolJTFpXkTZ6OBGie8X0ynAm1Kimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7cvsltmPQ2BgrDkLGwvhUdzkpake-KWe3tej31rPcEKdedxIh7zc81_3xe2Oxk_RxxymN03yV92SXz9c5tTeV5ysGhTruYDujMFcdMohz2AekkB2fNIw0P-WRwBqU-d2fFbz8XUtZewG5uZLSrIlB-LYGcmlCptV-JeLUYBbhkloCIhGQGomTItYgYG70i_fH925NXBglwGn-nx_MwaeXTn-sfP930fQn5A_8CAkJAR1MV4JuFsMrATgPVQgIo6YXryQyMww7tvj17q8xJvYBe56pKzSM3T61bw_j2iCtNcKM9jwGjzWioYOdnxhlnMACmtRhbbbeTOBA91ZuvCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb5PnIyJ3om1W4Ecs2a4PYLvLQUO5-H0der4KmkMGh3bdN2dILv2Ol2Af7XScbl8AGfB-ftHETj6vI6PDGGSOBGgpgLIrsbGIhP4IBHrruXFsUj-Be9FnA0HKKLxMtr7SyU7ZGPKz49jH6Kwt0IL0OMfGZ2DH40dPlVmwT-GnaHCXSar7a7gyrWg4MHjMpNbDvI4_ZwIGEAFLKOyBxQGNRV94ze1in-T5ZwRze0eq-UF2A0IVLssYLMmxeIWt0fDTnWdhCBd6fZ_U8YngFNAOXJT_OQNkHT97IpFzws1szXMI5Ri3bfRBJPLkyJdNQVhl6yZDyaChiP06w5LkqzG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn1tAhcTDQXtgpTcUkW5Pz8loW_RTxAVzkyulkeQbgPUYAux3mkCeSeZGih9eRhLKBv1HcooscI-bGUwCx5zzPNgGyuYb8qu05TUXBKCHyJ8ZtV0nFYdxugtgqEsSQGfDwmv1Rjr5vAqAXKjFLuVXr9k91GeoML9-JCVcsgMu4S-7Jfuc6ggHR1PIbGnNdfj4Ytm7Rhb0MimLLSHT75ml7hJIDEXhzPFZkuevkDdF6AEJayrIYYOd2DTWiYZ5snWizd6znncxYVsYB6e8SQKB-ymrCn0znqdWfDxG2i2tf8Vvw18OJI3lBHfdt1xnmnYhSlcNHccDR0MDFrK5Q6apw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXqVk34M5MNB6fRDX-0JqMdOyQnJNZrLgeSBjsA1kjdQhWsHQIF_HBx2xR8v1Wz2SWwHLBbJvmDeYdDx81HzI9O4M6D4a7R7ZwOm1M_OaaYRigkGfOKLk1ua-qpETMmp-KDXyV6scUzFsysKj6X4lZbLz8Hx848BGklzJhMGlyd0ScE4PX5Hd8KF5HfWJB7lIZX3MP-yradP6LMfhlxdjtq5UtLTk5GOhZur00AqknECY45ZLsFLsTMtb2cvxMH_8n5Jp-NvyLE5Aa883ODqlJu3CkteNWbMJd5G6z62O0IFbyErGwkwB1KWdWm-WPRB9UTWnbpC_6QnfCH5S7-Cjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_wyY08poHzq3EwBq4JoklskNks-uElK6-nUPvF8-UamFVTqGSe1qtE0gaoEu1pGpEdgipu3Lqcy-uhhybOCQ4fC4dADgb1T4i1BZiPVv-tr4PIsBtVP1ujZeNEB-KRGCqQJHNr7e7do9t0CqcvUO8NlW5Cvy4I5KXRgGt6oEYzOnw94CMlvL6-T4va184jO9UvPaFVmoa871729qhlKc-1hgoEs32R-B2wM0tHcya1kU35Ov6KA4-WFTtBn1OTld53VYxJxkjauvDazMZM9h-jjw8_exngHAhR02Ne_bIPPo7jGuwzej0pk0ccHFm5cJbxR580djgGgEYnB1WcEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYhdDMhRiET4dVja3UGnK_Vg1xDU5Am034umUbqa3f1N7ykypgx0A8_VYcrv6NWpHSH-EOZ9lZN6uFSKxeFMb2uOO6mn_x-k-oQBQh1NCQdJP7FdBQ3vWV1B-7lzCn_xFKGrw6UnI8aYMb2huOb7GSyH9soo7AdIhXVZ81KvYPAekGVcR46xNN50z1Fs_6TTnsj3jA6pgDaheGHh_8JeA996OQWLY0K20mKaSx-_vmpBSAZ77gt5Ms53ima94L3VpX1kfnM5FfKm1HViTeJ3XgjDjyAxbkyB86obE7T0IogELO2YXaeR6Os433lFoyVj0PSCgeFRGrhmz06HQmvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ3zLDsO1_QAHrOtKQiqBTzudmX-Y4T6buTPXtx58deHNQcaFFlfv-2uM2YBVe443usyZ4bKJ1_hUdsrOgFkgh6kzgtWBg0ELHAqicF7iDGPpxMxc8AQij8TtqsKNvuCzSaAmOgiBI1LiOrmLUFGIh3sbQyEYZEXdykKnKPbvmxJNasoPA9r8VuT9HXM8oVK_3S3peu4WutKn_OBn887IgDeov0tOB7U4amQZ8WmIJ37rMktgHynNyipBe9AK3SySOxsN7jd3R4R__FfUtH218aEaoTY1SpA-i7h2-Msf1Bx-O64GPQWTgXIOMul8lSB1JB4jtDMbaWaf1bQOIa2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwpaUPUXBxOZ73ssCk53-HsvdGWQqviQNG42SPV5ADZ-czFq56_5dwzXTOJhrGNenzqAX0VOlXu-PnqdlvEkKSA5O7Ptj3ZzGg0VJ6SMAYoiFvNhKN-uW1JOYeUBtfaDCJpWth2J2BGuCSUWixw7XFyqUjkmEp14mgmqYCsnBulBi33dux01SlkU2srFRO91x5fkf-ECAHc85BeyBfsiuUcN8NkoWYw6woMqaPKeIP1OlatUt-njE3DwM2gFjDfp_H0XFLUohYqvQkXICttCyzVVvgMt3aZFLi769uw103-cQQ2rtm-yly368595o7f87MEJISDvXIV0jhfMoCN7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syeRXOYpBHjB9hllVTeXJAT7zuLcVuADXFwrNR1dYZNJvDrzwyx7CLJp4myj709v1GBgHBYAgrauiKvtkc3d5D3QVg4i3sajO1oqLgLBvJf9iPVlaKqcKbOfNm8-tAtwmEnF4QV9rDgvQHYCbdvsK5myrumPm919TKYAxkZzTpW09qvXVtQAi56NGlturnuw-p1gSKl8OHs1nd0m6eOjU0NzI3X_dmJYyEZG4c92VCGf2LGBP5V_9QiO-gjnehEPOFzwajsnXYFn7Pgcdo-GRFvnsBmOykQaLvnxO6c0jEnT62Rwxrbvzfc1KaVfWLkS5ozM4W43pmEewg9dh7_qmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=F4dp4AG632CbfXbfDSq9hl70yqbLwg2f9zmxhB5wBQ8030eihLSL6YAoWljJvZp3LcHDXuFdox2Zzsq3gEy2oYbhjTd7a71PZfrL7FMBNif-0IJI44BP7OEHBhq8G4tP05nK7nhsO4tp4cr5ABpq43c-pnFDdEPUKGf24RcXnhaQ9YQv-9VP-Lq6ECwNj7aeJ6-tvkCABiPGxjbJZT-I8RVycyh40rgS4fGrAWAB6KuUoIbkHntmrqPv4-OPIeZNf0Juys86tP8aLGX1RK3blTSoaNDX8fc-6gHyTHbSNlPNJ7SE55FXwCE2FX6SfiLxLncfgG3zt1Z-7uW9lkH1PLLZ7gyKwobldim_4poYtNgb40FB8o8Db2Tj7KsHMskMxKd5G39vvnF9Z95x2WjXQ7QfsJPqpn7QmeqA0_G-gfB88iWctDJt1x0jn6hdEFsLyAEeFMdENryFI8qMa9b4skXkSthOc0z8tg_T8WSAKsLf_fdEMpAq8vf8nKvNG7rXIkOJ5V5IQxzCjOO-seqMQQUYsVNg3BKlzplmaJ4iKaFQ1JXSrooiVOfI-L4ca4QmRt4vPA1TRoq66kEw1U3vXEEEV0BNwSJHJ-8LUqfE3lsTXdGz0Tfjtg81n2BgqFCqxT2ExRO4tyOu53mlpnytGcoWLWCIDQLyhk5aC7LS844" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=F4dp4AG632CbfXbfDSq9hl70yqbLwg2f9zmxhB5wBQ8030eihLSL6YAoWljJvZp3LcHDXuFdox2Zzsq3gEy2oYbhjTd7a71PZfrL7FMBNif-0IJI44BP7OEHBhq8G4tP05nK7nhsO4tp4cr5ABpq43c-pnFDdEPUKGf24RcXnhaQ9YQv-9VP-Lq6ECwNj7aeJ6-tvkCABiPGxjbJZT-I8RVycyh40rgS4fGrAWAB6KuUoIbkHntmrqPv4-OPIeZNf0Juys86tP8aLGX1RK3blTSoaNDX8fc-6gHyTHbSNlPNJ7SE55FXwCE2FX6SfiLxLncfgG3zt1Z-7uW9lkH1PLLZ7gyKwobldim_4poYtNgb40FB8o8Db2Tj7KsHMskMxKd5G39vvnF9Z95x2WjXQ7QfsJPqpn7QmeqA0_G-gfB88iWctDJt1x0jn6hdEFsLyAEeFMdENryFI8qMa9b4skXkSthOc0z8tg_T8WSAKsLf_fdEMpAq8vf8nKvNG7rXIkOJ5V5IQxzCjOO-seqMQQUYsVNg3BKlzplmaJ4iKaFQ1JXSrooiVOfI-L4ca4QmRt4vPA1TRoq66kEw1U3vXEEEV0BNwSJHJ-8LUqfE3lsTXdGz0Tfjtg81n2BgqFCqxT2ExRO4tyOu53mlpnytGcoWLWCIDQLyhk5aC7LS844" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYGdKj7a8cuAU0m6HPlmJmUfNYb6u0zH5vG8Q-SkErQHGnHNN9cECCXzPQftHc-WXvEwa0U0-Qt3LWvMlTV3U_qNJs08VQMog6YfggOCd8ydfy1PMs18ZL_OzPSYQyAi3KatG8JgNL5kjbHu7eSos_BNZovBhZJ4nNpD5ZBMoesItHod7GL1VNXxX4HIIdbxfgNYtthcpavRpoMaX4NcTqaqGCwAJU07ziE2bO5m5YzoQUM1uJ80S29BIpQ0V6eYO_bNL-GVAcGHErtw79GV2hEC8mC9A2VyNePq-w66mt1lNtmraq74eLUW88DAu-m_0zLpb6zU19WfnXRXmLYc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhiG-3ONxOiQzXVJj2_E6uv_X5-JRrp_KvWm912jZxyKjU8AcmXlwF2GQwH-1H3nw2fLzM1qLZyy-KvZz-rT_IP9A2lQrFpyPH-2S9zpZyHLj9viZgEQtUn3-jcMck4bQDTRo5x54tHdY54lnmvzJZaAJoDfwgPowlqq_gBVvENzIz-6ncejewS0wRiH2eLgT4jUpkVfVCsYoM8Y3yExubmygqSHkiGRK9L44jsl5W1g4zuZ-MLSgXG6v9xK3IZ7D3ytgOshBrV35uME1h-fM5rR7uFzq2PxIKnd3gTHCwCM3LghmglYxrWLqYi4oILZS_YcrPExT-iJrbUxhId4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt5UZ2PkbMku-F-0eSdLzxr87zsr8SBuvKIVToP0eAlcggbHb_xqyTQA3OYckCCX7e1LT0uNAw09vN0s2JJULjpXCe_m3Y2xSfG6xHH90oMDuO-Dq66ap12TXJzOHdC6k3vsRuoYThmU4OFjHvcvBGsK1e1dz3Lt0_jEN_th_gsz-qvcut8H4dtKnWBOnDjpCBBK-760arVMoRMSAnMsIOlA5QHUHWICa1OoVe9jueTDYFqODoCDFjs9GDFac1d9j5bAB52Xi6NbJP3Uwz9a_3UeOdJUCd4SMJ5d3Kl2dwPfW7fssWaIY4lg5BADqaYvQa_SX-ZlWIK7NzsiZ33hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=N9aSAGCrKtEg1sUCQlLv8qBa9OTpy4Q1VLnz-Z4KHyqibxXKIqLz33bkqJDzh0cyz9U-snyYg0dzE-QHHYqcEstgfRAHELRZHKdxe5laEqoLoNV4hZPTAr8kLp0P24U5plyDbHOOUOdysF81IpAeprbJRYRe3hDrO8Fh7I0w9xlPDOAlb-wQh9rPkfYpiMI-8cvVwSqOnIYc1j2RWTy4ZxTpEo1NET2K7fCbIN4CMofrlMYkpFyxrxmh-XXQyjTFmGEEN_xB4U3ZPnKP0VuUlfKFEKWtkCeu_eK2sLDNDGJO6VdfGL8WuqXmKs-WzwpaUG0FwFkUbQf1MUqq4Ez0kGEwzLUU9x1CPxnpBEFjIZfZ1sdzdl985e5z8HDAs_ilNCiRfyY6bS5P8DfCD3HGiQkl2bhqDFFtwGKaopTJEx5V-ogE85W0h_bcP2D6fp1ATXGdFctpd_mZymHLXGw8OB1-89JqcnYToL8Na1aixtErA2wjGnlEr-NiR10qf_hiwyrS0PrQkTykn5pMZwTyeJ6Y1BNu8811aP9Z8lrs_oBS6CeWgxFFY-1q-_Qhdw5feHMbBJzEfVo15kMoKxJFEVZqkgu0tz3FIB4LQ-qZLkJ7iI0dLJWa-_Semhq25IgsYQxSAGW4h5A8Yjiv6OeCCDFS_VWW1yJCMLJwOec1-68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=N9aSAGCrKtEg1sUCQlLv8qBa9OTpy4Q1VLnz-Z4KHyqibxXKIqLz33bkqJDzh0cyz9U-snyYg0dzE-QHHYqcEstgfRAHELRZHKdxe5laEqoLoNV4hZPTAr8kLp0P24U5plyDbHOOUOdysF81IpAeprbJRYRe3hDrO8Fh7I0w9xlPDOAlb-wQh9rPkfYpiMI-8cvVwSqOnIYc1j2RWTy4ZxTpEo1NET2K7fCbIN4CMofrlMYkpFyxrxmh-XXQyjTFmGEEN_xB4U3ZPnKP0VuUlfKFEKWtkCeu_eK2sLDNDGJO6VdfGL8WuqXmKs-WzwpaUG0FwFkUbQf1MUqq4Ez0kGEwzLUU9x1CPxnpBEFjIZfZ1sdzdl985e5z8HDAs_ilNCiRfyY6bS5P8DfCD3HGiQkl2bhqDFFtwGKaopTJEx5V-ogE85W0h_bcP2D6fp1ATXGdFctpd_mZymHLXGw8OB1-89JqcnYToL8Na1aixtErA2wjGnlEr-NiR10qf_hiwyrS0PrQkTykn5pMZwTyeJ6Y1BNu8811aP9Z8lrs_oBS6CeWgxFFY-1q-_Qhdw5feHMbBJzEfVo15kMoKxJFEVZqkgu0tz3FIB4LQ-qZLkJ7iI0dLJWa-_Semhq25IgsYQxSAGW4h5A8Yjiv6OeCCDFS_VWW1yJCMLJwOec1-68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=kbSr23Nngeea5mS_eMG17T5w58ZH6JMUAb8vSKBw4PCnpbzYelATv8GFSFBlcJ2zUAqrytpJAzXX_tAEmt9gyWxfy8a6Vp29cEkYadXClKiDiPS6q4C6AfyqUpu7WxMjW-pUuX7EgO0U8gt7PYJGXASVDTGMYj4dZJMdt3x2XDWDRS5W8fJF1PY-13yZSDrL8FFOp0YBDdoU6D0d2sMcrzCM00GOnUfcaemrADaWkBMR0BOgeB1-4VsjahGcObp8MuPE6X9DYe4AVzCgY_Un6oiiVKoaTfUBNcU0QJpCc2EaqcNJttfuiptAh8BfdQ8uG9CJE0ztZwMCYUEgRPKBwW4QzfETzdF6OjUys_Dr457sjct5aKLCpLRPkvTpDCsVx8-CHGW-bIfFlq0pDIWzAz4NeayPsTKhGUauXXLuPRqGJ_ZVH8Ly5K_ixJIjhyrACYhR8h7kvVb1WBsfyooCB1YPSWdwwpPdoOywauAyomyB6aqdYZOHkirnwKeMdQvObLmCBjP-dXijGe79PliFgW-naJFRNdGXIDPoV5tbLKLUyMaxc0Wf1B6eNCbcYa5XpMIfJ0xE8IoFm5H89KFwZdwMBlXZ0G4wQT-gq8ebzIhDdOXxyasjNombpe_SDqv8lSG9oQAzBLzDeCgxs2ZVMYlGbm7d_WgILU43zUp--x0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=kbSr23Nngeea5mS_eMG17T5w58ZH6JMUAb8vSKBw4PCnpbzYelATv8GFSFBlcJ2zUAqrytpJAzXX_tAEmt9gyWxfy8a6Vp29cEkYadXClKiDiPS6q4C6AfyqUpu7WxMjW-pUuX7EgO0U8gt7PYJGXASVDTGMYj4dZJMdt3x2XDWDRS5W8fJF1PY-13yZSDrL8FFOp0YBDdoU6D0d2sMcrzCM00GOnUfcaemrADaWkBMR0BOgeB1-4VsjahGcObp8MuPE6X9DYe4AVzCgY_Un6oiiVKoaTfUBNcU0QJpCc2EaqcNJttfuiptAh8BfdQ8uG9CJE0ztZwMCYUEgRPKBwW4QzfETzdF6OjUys_Dr457sjct5aKLCpLRPkvTpDCsVx8-CHGW-bIfFlq0pDIWzAz4NeayPsTKhGUauXXLuPRqGJ_ZVH8Ly5K_ixJIjhyrACYhR8h7kvVb1WBsfyooCB1YPSWdwwpPdoOywauAyomyB6aqdYZOHkirnwKeMdQvObLmCBjP-dXijGe79PliFgW-naJFRNdGXIDPoV5tbLKLUyMaxc0Wf1B6eNCbcYa5XpMIfJ0xE8IoFm5H89KFwZdwMBlXZ0G4wQT-gq8ebzIhDdOXxyasjNombpe_SDqv8lSG9oQAzBLzDeCgxs2ZVMYlGbm7d_WgILU43zUp--x0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z170Hej9KspFdar4WDYh96L4If_SQBXqC-iSea3YlKtJGbaKv4yVs1DsOh1cUpUGWrkrrPfQJrqPmeYGFJ4_ACndskCpxm4TGHd0L2z0Hvajw8mLzO3h5428d7sBE1lduuN_GdLsnzu29RYs9t7NLChJvFa1kzFN-mAQ4MqlQXnb2Kk0-6-vyYgLECx1DQSuGhwbvCAg-w1VMZWR3wozxQ5nK6mW4m0h2WOHGSSnD6nAinvk0vTBO3Bx2k9Rw5mOGXhhwpVmxpOWnZRjfk8QMAGR51FBe8enn_9NfxYUfXUGwLndbRNLS4i_gX9owtk1tGQhsXnsyTufoB2sHVjNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=fH6vqJt9DruJ3F0pcZj02v2Su33eiENsh7CXJnVfrc3oxlBJnGyShqnNWqb7bZIL-bcF1DeoUDtSurZszC9dE8FUWYkALC_AgDJZhJnBXJltGBaNN7j-iP4Z1Mf-qpQ8Mu6i07gtmyNp9_zDbR-mcVe7LJRUtKcViFWsMyDOOBqc7CGzVgIIpqXvnrsiMKYlfdJxXM3JDjwTTQjPWKEc8CrffiFzAxaUriWeoIlik5CyF70LFRVbodPYBpXntArxZ88LW-hCWCZMQSjjSJB4p1I36sBXaiYC3DMmPlj972GTVz5WvPEtv6piLX9PapTwo0r51cONRyHR_kOwGuyVOkgEE66njlB7OMMwv04WBRDJwjRlc3g0ydcZ0XYYzMX4yRlyqz1NACyY9guuGg62GoScybAaLq2GAACgR9HlqP3G_bvkzblmyTLBF_6lKNzr5OFPkL5FO841db9moTU8LbKIrMKTqBQ7VtIU9WWMzjaVV_EmAUFB7SiwkSMNgCO2qXZRrLyCH6A9xShJaHMD_c-We5K-TPDJ8UH76O364M0JiPYsZO_3X2ZXpHRAQMrNNzxrHX_Vd7GP0HwdP6m4ofH-kyoEINKNOmAHimsjuM2jdxxG1_jeYAQFdmFDNEs9J9sxweYDvFuaJgbnupdY2JYGN8L1Gh7KmiZJkk7-TOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=fH6vqJt9DruJ3F0pcZj02v2Su33eiENsh7CXJnVfrc3oxlBJnGyShqnNWqb7bZIL-bcF1DeoUDtSurZszC9dE8FUWYkALC_AgDJZhJnBXJltGBaNN7j-iP4Z1Mf-qpQ8Mu6i07gtmyNp9_zDbR-mcVe7LJRUtKcViFWsMyDOOBqc7CGzVgIIpqXvnrsiMKYlfdJxXM3JDjwTTQjPWKEc8CrffiFzAxaUriWeoIlik5CyF70LFRVbodPYBpXntArxZ88LW-hCWCZMQSjjSJB4p1I36sBXaiYC3DMmPlj972GTVz5WvPEtv6piLX9PapTwo0r51cONRyHR_kOwGuyVOkgEE66njlB7OMMwv04WBRDJwjRlc3g0ydcZ0XYYzMX4yRlyqz1NACyY9guuGg62GoScybAaLq2GAACgR9HlqP3G_bvkzblmyTLBF_6lKNzr5OFPkL5FO841db9moTU8LbKIrMKTqBQ7VtIU9WWMzjaVV_EmAUFB7SiwkSMNgCO2qXZRrLyCH6A9xShJaHMD_c-We5K-TPDJ8UH76O364M0JiPYsZO_3X2ZXpHRAQMrNNzxrHX_Vd7GP0HwdP6m4ofH-kyoEINKNOmAHimsjuM2jdxxG1_jeYAQFdmFDNEs9J9sxweYDvFuaJgbnupdY2JYGN8L1Gh7KmiZJkk7-TOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzrK3xZaAGzS4-WwyCPF1ifwtAN1dOAZiTyzyt2w2DMkOWJAeSGvvwXOpMRad_VeL0eGWrTTfgbVPz6HN4zPNnCQbXXwdaw7a_f5Gfe3eICLwMQiP4SwIPf4qeKU9wC-RDiwTtFK6cTYba_YlgxzZ-SuHcbDlzinnlRhZgKHwxrBB8jVyjOQlQzxOLUDvTUsqEHzYLPl4h-2ffq8SBvGXnufnT482bvRy7gaorDODvmP7wFB5J-7bhVHIK4CI5ajajhtw2uMc9oorGrb-jaZwOrywAuIZbah_bHBV6ZUpxWJJm2tIFouJ_5qA8q3qL2cBTGZil-f-Z91k4jhB_1vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHnWU-lMta8-geJWlWYlRpan-YBDFB2oQQvxwUy1_l53LyKEa5fL2aZ_wFe9I4KhDDeQohEYyI_jDfnjhFJkFTRGHmJVc1VKq1R1n_EuizP-79b4F7HmbobaM4hx6OKzZAujFlSmorGhqFcohAejMAQWjqr9t9hJbYSWKeNunYoPpcJzkUg0HBRPI-5SKTioQnaiigefy8lHA7rQZ7oUuj7vu9MJNVz7rhr6QRYEsIP0zE6esCIaZPDOYHCOVE6JMTE2q2Hdq6DiR11IbkYBjF4-NBJ8NhdsvqKHBYoj1swwPWjdCfICkJ_9MHOt0JNbeLmSjGA0dokIN--ZEmFFXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=LNV-mHYlL2JnZLqKbMYs_jM1F717lM2OpSTBR6GQLjP_B8KWe-ibgWTfYPJDzCxApXthjMSrXlKohgzci8Jv1Ll8lHK3PnwqYrpQwMrq8Iyb0HjLwmn9xlt30oj5O6PZ0NfSklPwouvNZcMHyWhj24c3UTkDH8LYbBVbL_9FduMF1qKJFsWuyuz_2_9RadCi2d22K5KaesrF_gSSwLcvYqlBaasWnStH5Nyxp0TQl06rqMQfDVoREDGXW6nCysLd-7ONLq4whRKA5vjkfH-JpLPM7AuFr4HPZG9G6DKGB7FaujxWWzGPxhHZABxifhqKCS37zGUdU9tX0do_0f8B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=LNV-mHYlL2JnZLqKbMYs_jM1F717lM2OpSTBR6GQLjP_B8KWe-ibgWTfYPJDzCxApXthjMSrXlKohgzci8Jv1Ll8lHK3PnwqYrpQwMrq8Iyb0HjLwmn9xlt30oj5O6PZ0NfSklPwouvNZcMHyWhj24c3UTkDH8LYbBVbL_9FduMF1qKJFsWuyuz_2_9RadCi2d22K5KaesrF_gSSwLcvYqlBaasWnStH5Nyxp0TQl06rqMQfDVoREDGXW6nCysLd-7ONLq4whRKA5vjkfH-JpLPM7AuFr4HPZG9G6DKGB7FaujxWWzGPxhHZABxifhqKCS37zGUdU9tX0do_0f8B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq5Rp41z9XhhHwemSu7L-SyHM8ZZrJEiU5ejIDTIk8OWsTr7BKO_LD8bdVnCPorcev9zutPv30fQnoLQ8QT0T5Ucxx4DCpRj_6P8libbgzHFFAsPcWGPQpm7C08JvZFa67TxpTOQ0_mCj93x5PAbHbZ4pc2v9Hyh5fxvwdV3Rj9VIW7mwR-ko6OiFmJaySK26w0O1eYFGKTlsnfv7BlbmXGcYkTxXtUbvAVN4ncmbuPAYlscYd_BYb_8ZxjG1KR2Rf5eSXQz64MxBE5hLwM-4FCwFnk5NUKBU-8x0AHRjYYYZvlY7I8AUs_26kau9RGUQoA2Os5y6O1kpymNPGresg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdHPCzK25k4k9l8QGEStgorJLD57tMO5R47C4lofxPImXeeKoMLl-_51gAeIvnflT4U-cB94dvL4HOY7XZHNVnwSEPvRzilbvTUxAw2_WFiFaVdZE3Ia_TUiGkNHjotEkH1leZoRDRcPgJhNNoxSMLcwmx5p-XSHl7I448fsqBTrAUnaVeK38mz5c2l73KR2iN-iP_4HzmaOKnxgolQ8v7D026l07Jc9boUX0C4WsPpcMm5NG0uw86X99u5Bgijr_SXRFOfNk5mXVqcHA2_TBppuXVdaYRlGQ3UcU2_xvv5_q3_B7yBftTKuwG5E_hcO4qSWef5lxBNOS0MuFyQHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHLJtOGCXizQPSSsZRjLNIKuI7MM2ncw8HwlwpyWcDVtgKMw7s7U_YQq01P1u1cHK-UIYRn4gfF00x1S53ytkpA0LAM2eChbbV5CsTs0_DebGXBYwO498H-unnRB_ty1CBUd6mrkVSjGsdWBR_f8Z3waeTSAgZcjzSH0bgbC_0Ir4CmdI4g7iKuPfJrSoA-oKMReMsOdK6dzfvZDZyWvGxUzyCjU5iUm-ZZWSUWNxW_x78LGHXZ7uI_Y8_-2FadAlGmMgM2GK82tanKTBmjPCLb4IZJV8HvEJxpfLGO2xBtwlOPe4NXxvl2soOZMi5xkIK9191SiuWmLmXmRiVA3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Ebp0HXYdi7i4ctItPcG5UcHwAhxBT8O-yWPIndZ0KMoqzuRfcavC0asu7MG9EOAoWbLfFI2jRNI215MktYsXHTI40aiAU0tOPrGDRIApR80FNqij-mz3WDuoaMH4KYMLiAFhFeUDUSMjVynTqlSJuTTeARLi4yfH56x4Yjcbgs0StHoK2UffoPyo0OpRrlBaqpUCdxvtAWKrpEtL7xlRQpSW8EGh7WEv81jWweuBeS63IXIMYd_9MLD5qK5CHGgqzT4rR9mP4Wbi3B3wgfxdhwkMj7Cghum-Tu9-uZQ-otFoVywShgD8aR11bWnCANUSU5PPVhCruiBOdfkBtllfDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Ebp0HXYdi7i4ctItPcG5UcHwAhxBT8O-yWPIndZ0KMoqzuRfcavC0asu7MG9EOAoWbLfFI2jRNI215MktYsXHTI40aiAU0tOPrGDRIApR80FNqij-mz3WDuoaMH4KYMLiAFhFeUDUSMjVynTqlSJuTTeARLi4yfH56x4Yjcbgs0StHoK2UffoPyo0OpRrlBaqpUCdxvtAWKrpEtL7xlRQpSW8EGh7WEv81jWweuBeS63IXIMYd_9MLD5qK5CHGgqzT4rR9mP4Wbi3B3wgfxdhwkMj7Cghum-Tu9-uZQ-otFoVywShgD8aR11bWnCANUSU5PPVhCruiBOdfkBtllfDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=gkXRyL5ZlQOwNKX_La6JzomkwfdsxPpY3-_vBySXKJupV6zE0I65Lq-gf_AM7ZwccnBK02M3g9vW0YR66BUaVgmBvVkogYIx4pFwp200ya9e8zyTyXWqN2yOOPWzoCp60WzPEES5vkJhptOLOKuRlcSqEOR3S3c-UaXpn2uLWKEu9F67jx3Rs7fHPpgCW_955SS4u3tgB9rC0CC4AMTjBMeAWVRN6dBtTRo5gT3cfVU6_BLHkkvB_gSMUsGF6WQ_SqNCMe9iXpeS6uUZZVj0ztyB1ZN85_jzPhwmlGcZGD8scG7K5Ii3IgmnVOhusqsOXDHPJlyBEF6CQ5b6OSDlK10xvny1ifabn_TZxckFHitjHB6DdolRODrTDT9cKHTqFZMQ09Kmc9gT9gKAFlVpXpLn70zvXYX346n6ovVwBHeJuQJXNp3R81RQbK4XbUy_WAXlLMCBLemhHrW84k7kFE_jklaRxgLl9sgy9TlHV6uCb-AY7D7sHLiOuxDGCxNzE_w1EsrFvza5OvrfmgzUBVF8vqAcyJ5hH4h9poPKSp6Fo74XBAoAL9NSrTZ5dZYjnOLj4Wqq7NpY-gMjPhFIyi6TeCUFVO2v-BQn7OaqLxNtq0qQV6yHY4svCTHGocQPOTOKo4cDSA-aeANZPHhrx7oU4YT8RaZyDshLRJrXY28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=gkXRyL5ZlQOwNKX_La6JzomkwfdsxPpY3-_vBySXKJupV6zE0I65Lq-gf_AM7ZwccnBK02M3g9vW0YR66BUaVgmBvVkogYIx4pFwp200ya9e8zyTyXWqN2yOOPWzoCp60WzPEES5vkJhptOLOKuRlcSqEOR3S3c-UaXpn2uLWKEu9F67jx3Rs7fHPpgCW_955SS4u3tgB9rC0CC4AMTjBMeAWVRN6dBtTRo5gT3cfVU6_BLHkkvB_gSMUsGF6WQ_SqNCMe9iXpeS6uUZZVj0ztyB1ZN85_jzPhwmlGcZGD8scG7K5Ii3IgmnVOhusqsOXDHPJlyBEF6CQ5b6OSDlK10xvny1ifabn_TZxckFHitjHB6DdolRODrTDT9cKHTqFZMQ09Kmc9gT9gKAFlVpXpLn70zvXYX346n6ovVwBHeJuQJXNp3R81RQbK4XbUy_WAXlLMCBLemhHrW84k7kFE_jklaRxgLl9sgy9TlHV6uCb-AY7D7sHLiOuxDGCxNzE_w1EsrFvza5OvrfmgzUBVF8vqAcyJ5hH4h9poPKSp6Fo74XBAoAL9NSrTZ5dZYjnOLj4Wqq7NpY-gMjPhFIyi6TeCUFVO2v-BQn7OaqLxNtq0qQV6yHY4svCTHGocQPOTOKo4cDSA-aeANZPHhrx7oU4YT8RaZyDshLRJrXY28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DapJyX8SJcyoPWHk5gUdBeP9i1LaMG9pEaDAwE-Dd1cW5RscQT89W_S0Kac8zjb5A86MhTp1mdS4IyIBxk46YiAaqi_OJdYJvxYCH_IkPTrnPO4TUr9hursTv4bsTSRBwurRYiVrrBIi7Xb9IbETp5YmhSoGC_6Fak_QqdhXUXsh2ch8XreKLZvAxza5gOp342OUQndS_EafDrsjryQSPfBaO2RfsArK6UGMVDJs5WNmyN97aoFq859YGjsXJO_7p4kzsFBGZkFiFrD_z6qi-uT9cUwkgzXzPVmiHYstlyOBGPZHWpwCq2xGkCl3bYScEotS7sAuuPTob0N-_-1Ycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atQDFV3Hg3USEjXew2eupEPQ6vRHSTt0iTL74q-lmBbE6y5hLT2ekB0qqaJxdARUUtjYYD3zQ1lCdjv2jGN7UarHL7Wr4BTd7YJvEVnGb7MWyrp3eXYef3OW_EfYfBX9qglU__vukOzwRZjntcJ_2WsEPFi3SobrgscfPcovbsz7uB2l3qYK69UAsbqRuiXzTdPlSr-VqEd7Ycjm9JJY7C3koOv1zHp0NJG5rDfLqofJDi5sC1Er0mmniHPpUt8rzCDB_dtn-fy_Ic2QUPeLrVvURUI8pwdNTnvMUcWHOp3MiFMo_NmWjns2Fxjj3gkVijuc9WBwDdXW-tmDGRjLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gLjY8p8wQ-y0xKanD3rFAdg4SVBKJRI1ZMofrnBm7yU7gpOkUIQJCWnyOssftcZZe7nCcu4NcfkUY_0vi8IbIVcdv_bl_s8PfgaSGDnHb8CE1ETRhYbe9-Am5VGVxhIbmd7Z3TiL_kcAoI8Mf8kiBV_koOIj6TLa9uq616FSdMjZeG34q6HU_eGqHX9JjFGAzecJ13h3RIkmb3TY0UttcqPwzk0aHbcSik9iuyNQ6xly6IHlmxTusjgVE7NGqmW2Hh1kiQW3qKKQu9CsUtkeE0Cn1nJTKqdwDbOf-WVl-NRLJ_H-Ce44KiB-Gdf7cOcxQ9zbgVuCMx1KRcHJCMYb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=L4dzodwv2hRQf2GgPw6ysM1qtuHhic5lbAML_p_FzrjK7-IrmfanZrbroAi_zpzc91ZkQh2QCd6HJHJc8PVjFyCqDzPKRFbnTjcuZk2McybOOeFzwTLWHfkTcRoxipbImw4hnrt7yYysXBCDXeuwsM0ywoDM5Q5GepPQjSfONB2hzbt4fCg0q2gGlXP_H0rfe-b_z8RVxLpis0_2F6Jw1L4PHSldkKDSED-1IVTr5rUifijxQxqaOpR_tntpH6GEHmPRcshSDhSm0aChT1AZfjIf-AfWyCn1oQuSMGEKInNmWEQxoS6CXJlBumo53Q4FBXRKS4puYfFLZFM7FEuuaw52i-qLsGSoke67R1aCRYmGd_9oj-vNmbj8dwO2hwTNQh5O69AizzXqln2RLSdgnx4MErrZbG0z2owIDQxVWBRg-ZJUGx7sjMdF407tsbnWu-cPE8U9gmrTyyMjJIREcrFPDxIeZvKGJ_zie1i621nKo0OtA8SrXAiklH8YCNPo3Cm58lcRXSO8UgONeweel9t86GRehpnsTzm_9A-5DMu9JZWDA_heZucUOqVuwy2adnLsQzmYvglIg5Mb0iJnPEXSHO1BT-sGRgUY2ynWjQwfD2Ux8YE_dEko5fHn9QaJI5QrLNPJD4P459g7AuLPOCX9VGNkpw2etbs9axuCTsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=L4dzodwv2hRQf2GgPw6ysM1qtuHhic5lbAML_p_FzrjK7-IrmfanZrbroAi_zpzc91ZkQh2QCd6HJHJc8PVjFyCqDzPKRFbnTjcuZk2McybOOeFzwTLWHfkTcRoxipbImw4hnrt7yYysXBCDXeuwsM0ywoDM5Q5GepPQjSfONB2hzbt4fCg0q2gGlXP_H0rfe-b_z8RVxLpis0_2F6Jw1L4PHSldkKDSED-1IVTr5rUifijxQxqaOpR_tntpH6GEHmPRcshSDhSm0aChT1AZfjIf-AfWyCn1oQuSMGEKInNmWEQxoS6CXJlBumo53Q4FBXRKS4puYfFLZFM7FEuuaw52i-qLsGSoke67R1aCRYmGd_9oj-vNmbj8dwO2hwTNQh5O69AizzXqln2RLSdgnx4MErrZbG0z2owIDQxVWBRg-ZJUGx7sjMdF407tsbnWu-cPE8U9gmrTyyMjJIREcrFPDxIeZvKGJ_zie1i621nKo0OtA8SrXAiklH8YCNPo3Cm58lcRXSO8UgONeweel9t86GRehpnsTzm_9A-5DMu9JZWDA_heZucUOqVuwy2adnLsQzmYvglIg5Mb0iJnPEXSHO1BT-sGRgUY2ynWjQwfD2Ux8YE_dEko5fHn9QaJI5QrLNPJD4P459g7AuLPOCX9VGNkpw2etbs9axuCTsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBk_CJGMqZJC_NHagImNuejBh3MUtv17w1iXfmfwAyN_9J0JzHVxqbJ_VY6FzA26B1F4JCTg6wCtX3XHPLskiApQbS5qzcNY0wBH8YE03JbpkOrQOLA6kwwzOh1uw_hXZi6NZpAJaSieh_itfyH2NP00s0hEUI9V05SQOb5Xf9MWPZP5h-4Rekg5Sk7gTrQJZFeWn11XkF3-eRuOC4gJVSs83Jv3k-OW1FSoCseiQcSFJ9Qu0idPbftzFNwpAyXdLEFosb3WH1OB-y6wG0Uz_WwiKyRs7t3FYarrwFlWAHuMQWa531VRG_mJDakbMwuY2faMYkxy3UU2z_vRAeWxtpxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBk_CJGMqZJC_NHagImNuejBh3MUtv17w1iXfmfwAyN_9J0JzHVxqbJ_VY6FzA26B1F4JCTg6wCtX3XHPLskiApQbS5qzcNY0wBH8YE03JbpkOrQOLA6kwwzOh1uw_hXZi6NZpAJaSieh_itfyH2NP00s0hEUI9V05SQOb5Xf9MWPZP5h-4Rekg5Sk7gTrQJZFeWn11XkF3-eRuOC4gJVSs83Jv3k-OW1FSoCseiQcSFJ9Qu0idPbftzFNwpAyXdLEFosb3WH1OB-y6wG0Uz_WwiKyRs7t3FYarrwFlWAHuMQWa531VRG_mJDakbMwuY2faMYkxy3UU2z_vRAeWxtpxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K07fpcftdEkzcqRssr64fNujJIcD0rLSgXw4d--7w_HpMzMftjMpI5am0pc8HDLImcNOoDbTa9T4Eo_xhZK5KfBI8yW7fZq4N7BTULDJ1zHr0mB4_2ALcg4Sv11i8RXMREPN81592wLOW9cAdpvz3GoS3W8ZU_7F-PpHSX-ZiCqkY9G46dnNWgqMp5MNpRz-npVqFQDCeCgLa_CbH6IZJXgYymPDyF9MYpTuEMFw8JHUi9jNDjfUQmP5kNR3KOFG9Fnagq7D1kHiHayEbhVfp8wYLvVoplTFVXGHE9tFRtO1SqB3B8YL5KzkW3DNDTfzANSsT2ukFIt51UW37Ad6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIiNQRJ8vmoyi-q4j505R-ZvH6-BNEF3rLEsomqdt5lKWrQA3llfICwyZaQVkOVtohr9BIMoE2HbGn5QswJxGvwhkBaMOCQCiSKYSj-j449Kwt_l7TcXbQn4fkqW1M5Q83yf_lqQjZgXkM-yWzjettQgGjKD1Ys1OZLxC6zK991HzNm-xR3LVFpBx3IhKFVUpaedfZ7-Ad9jJtZEj9E5jCHnNULFcadw4lLAbtly9BpqyH_3Eqq6Loqd8-dNEwb29bngA9ou1wBNngF1QobJP1_xUKSZMm_rFZ6bUZbUIUifS4FZhE40zd6wcPur9Wwmg4PejjRJcMIcjAX9G_O2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
