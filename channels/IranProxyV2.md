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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 20:30:38</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwm-AwGQxTCTKEmdK81H3GiB042JrRVvQJN4jmEDdWp99ARJjnBVbrsV7R8pS2Ab2f8K8rnxl8LWq54ocAH4BoKaP_FKPQa9RJsJ3Lv71v5AQPDzrFLUHB4nby18wL_RSU1GdK-GRmym2BbZWUOHegvWkKh5bMIMweHXPX0HN-HbG4_gs8lAHk0AsP0InGB1bjrURuUCqgTq-_6GpDClfPIAhFgx4dm4fgVFkh_K2H9UBngCxhot63aggnNMFjApkGsDQpLpUkWEPbV-aQUYoeDOx5qhQWJioaGsaIn1H8Zd0NjIJ98vGfgn4h0UBag_TpUsc71_6ozSKPsmXGJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQvPMwL0u_dM0W4VJgDkeiHgCXAGbwwmZfC7iVa-55D_eUpE9OCxBHamX5APZwqAbdIyWAq1HYOr0W60FkgVWhyypBzj-mF9PXoUB64EBbxXzxb4tgnnKTou176xkmAmmSRCOoGNWhnGPLoIPEHuh2M3tZ2XjcWyGD4On448SqEXDVdrxwLmijGNc9n0l0urUb3cH4sZVF0epDmhl2YpHRu67Ms4NrarL66V0RWq00P5RE9-4r2MzGW03dBK15ufSqYxyiJ44G9ucthpMtRsT74sdsEjy5yX2PKpmr0nJVTr-p1UXrvWZ8Uujp8ugV2PslCGkHiwoN5_oApR4hdpAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4b33omq43t0T9Mc3npPBzTPdCz4tn2XG2IMNR_NPeMiQEwUKterwHaSFb7glFZhimW8j9WK4o3CpiipdAywtbg2aJEAjQnn0yMEoBKrlfguvunmXGajEdkyF0PlfeuU1AN4AZDQwMKC8-HwcWS2winvO_RPwHmVNyxdtuVHTRGr8-lO_oCLBebY3I75WxhQiF68e9dLNFO0AQSUysqHuzX1Zmn-oDuPpv1k_I74YH6As-nrf--7XUHaiVmt9yhm7wUNyewET3j3kTvD6XsL5xGdeSnm3befvqPdFjB3KAx0NBHOiqvbMTQYxBSVXIdZtILVf6QZV_pGPcyR-637iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aenG1GFYPtsf1bTu3kgnpig4zJxVkP3DrXV8pxptmm2Bb4ti5twBvXDyWjH2t1dH11zi1pmlRPiimCSEiO416alih_A06jKmgbs1lszbpc7RzwBlxq2SJi7uQ0F3mfSeJOycRr79sPSpzJlPOWtHeKogqnE0APb-o6aQKqF5KetiSnAvocUYGxjJFOF9m5YxY8Ze2hD3yMBND4zlL7W4cDFba-QhgY6B71FUec8w3Pn_F6f0hKWrXPMa0SyWkn8Q60SPj8BjJ8wRnb9QI07M56UlaxwAYIgxost_7_yi-Cp2zvb4u6v3SO1x9c9LUczF_lYYP2MU8rBeF_GpndOlOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBJwVBoNZhLd9_Cj6SANjXlhdBjyiRL8XTgSPJ9i7Uhm4GwT3WJl5Pe2mEjU25VU5YMQaLH8BdwAmBCrLIpZRl8zb42qMUFm1U2v3b2KMxxuEeuWTrhwCVKV-mR3NmQcKDmqlTgBjno_txfcGoBqsXDLVGaIrzqJcPUA4pHVpwT89Q_2wvjed68twls7u8-OFb-3NXBVkMQhiOQuM2vL1PAXTnu5DBFdTkNrf2PkWC77SmGMuJTA1GnthSL_rdSkGVWxhXnIuzOJfp_REjqDxQl_iUpLhHmGf9hf1N7gjL-8xV7fWdPziQDzsZdB9MrhHH48zLEWA4BZpW2uSG4uiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW8QP-037bEpESw3mQGofOBBw-2zT_8X7YQjnbvAGQId9euePJeQDfJWOE9DsQ2Tuk9-wgyruwGN16U7Dsi9oag08Vux_inQ8PtA-FvV9xvHBH5BMwGlAcC5TgNquc_eRftljbf8va9c_j5o4hqVypWb5jCQsucgVDc_lCDuILdGUk4KI2j4NBqWxsoeovg1AdzrbV5hTsex0X2gvY-rRj0osw19bCajNn4p8jXdzgI7tOIsuKTtgOG47PWvoemJ-TeMYXqguocp1RKvR4n14rZwvvqRAyBwb6piN8MW2-zjJgQsOuZIYby-yTpmhr5YzCoezFQe29NVSV-eDjTkgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urjOCF57BvSQdzn6wDae_oeXcfj98f_3Hy_zv6hmF6Kl0KeAPQXTZQ7rYb8BQWIIpLzL1ZvcAKbpsjZ7o29ICLspqMFz-WDFBqoIE_7MOLrKuAAx6J4wlYto7vvv7DvaLf1REEGrbe7BJjcpEq-LPoh691LxGdpvpf7H0oKkkirK9edi3odgXbaMLvAqTdgXb2GUBKT-shhG61IgOnxKyBV9mYeiy0sd7yfgJRfpIMXEZl2VGx-URE9ITD0bl--wbKWspth3gmihQ-tRWn8AwJCSYrb4fhuLRBpNYBWgaRpPe6OIm8rujfcTr662Jht7f5tByMaj0-IDdns6NmV3dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB5d3e0VeC8iVIpx3EUhrYYctLLY9X9CwugDWy5fKbW-FAXu08r22uynb1mEybJBrhpQB5Vz22rGbvvVQ-S7papdESSF1bM8I7rg4LxTL02FazTmvt7UkwZsSRJNMcrnzi0gW5NT9JhYQJf4CS57Qk7pTmppbknlTCUmltnOnR7ETC0pYnuyhJZrjDein-wL045LNTUxeoGpH4ST0FdEHQFUFYViMFdRhDxq14wElKMHrgLnF8KoTBNtxb6yIcjMznuyv6vKmPjSueYDCnilJh-V7R9paromQUuK8fWtyXwGUeUzMP5DrHXZCvAozUXk46iSuu8OIhnCwA_xnsGjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=QsP0WOZt_vPStX8H8nEQsjTB84QKy5Le2O1J-lToJL43cR237jtlr6ymA83HkgLdiKXd3Lywhtt-diav1aT2HCLE5JFPRdOCG_uaiNUyXK3vH9coOIAN0Ei-6jmeM67yKL4IkUlzki_c8wdcpuEBOp_P2PVuASCwmBlEOOF5W2zd7nAf5Frwdy32Pvd3FwgHHLPoZpeYCp8E96qjog4Qw3s9judXCTZhhAmMnGhMOoPQqKwyX-YF5X71yQ-fMOwkBfXARhZ2oPVL3MERI5-3Ry831Fb8ApUjlJ8i7nwS7-x4JOOw54ETLr3yE_Ly1ZKGfjpV1g3u13n49LpG2Yqnb6rPxJTGdTen6QL7Bvl7XZLhkStfbcaAZY9U2GtNbCswDeMXWgBDNoYKKn8s9MLMkbG-FwwQPeUoSDyeJcL93FMWzUDbfkoO6whU0Ame42LghKSXhelswRsTwoqPeeuGnHsGwKaruSKB9YdG-iL1MlFKNEI33Wq_tffJ8sVsR7h6J7XB0RpvPYJVEzqOpW_kBMk6pMY2VB0rvzYEOC-oJ0_cBbVRDzO-u4kLqeVV0B5DpKJ1Y3t3w08k19tUc6yOHnUOYSFr1FHIxJvARd-G3LvDWcCcaze8qLZLGJpgyZFIhTKu7yjEmj8JIF5xcoYw9B2e2hKeUrxBFB5tz_xyPRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=QsP0WOZt_vPStX8H8nEQsjTB84QKy5Le2O1J-lToJL43cR237jtlr6ymA83HkgLdiKXd3Lywhtt-diav1aT2HCLE5JFPRdOCG_uaiNUyXK3vH9coOIAN0Ei-6jmeM67yKL4IkUlzki_c8wdcpuEBOp_P2PVuASCwmBlEOOF5W2zd7nAf5Frwdy32Pvd3FwgHHLPoZpeYCp8E96qjog4Qw3s9judXCTZhhAmMnGhMOoPQqKwyX-YF5X71yQ-fMOwkBfXARhZ2oPVL3MERI5-3Ry831Fb8ApUjlJ8i7nwS7-x4JOOw54ETLr3yE_Ly1ZKGfjpV1g3u13n49LpG2Yqnb6rPxJTGdTen6QL7Bvl7XZLhkStfbcaAZY9U2GtNbCswDeMXWgBDNoYKKn8s9MLMkbG-FwwQPeUoSDyeJcL93FMWzUDbfkoO6whU0Ame42LghKSXhelswRsTwoqPeeuGnHsGwKaruSKB9YdG-iL1MlFKNEI33Wq_tffJ8sVsR7h6J7XB0RpvPYJVEzqOpW_kBMk6pMY2VB0rvzYEOC-oJ0_cBbVRDzO-u4kLqeVV0B5DpKJ1Y3t3w08k19tUc6yOHnUOYSFr1FHIxJvARd-G3LvDWcCcaze8qLZLGJpgyZFIhTKu7yjEmj8JIF5xcoYw9B2e2hKeUrxBFB5tz_xyPRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTs6Jqma3FawhLEYvMZKQbWPEJ79xmBjfzwWoQdivksNYoGNgy4MzuPA6cTqjUaG7CAXbyOIPQpkY_CIbQmm4TQ4khXRR3eGGe0aPFwq6-qBkNjwCct6gli8Qj-Qsj9AKBCdI9_P5vrWPetXtsMtaAL4P_UhJRpyQEzdrkKrL9CBZI3ZbQXpwt0SVWMwuRUewYhekS6eY-ae_y8TW8U7C8l5UrejXNVy3FkVTEDWnY4N9ZCKaR0Zu1Pmykfji_Onw4CCsRyLLOr6UzGrq6oivPinZ-mQzwu-ukmMep5Wh_7ZV3tTaObYi7ad1E3p4PfJP9UcRFFlbmAR3yeRxGcmZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6aPTIMcvFSmZmy6pWxqeCA7a7sxIrhJH97vXqh2KxqHo83grD7DX-D9kqo8UguP_Ip6K1Lp0DiBt1cpvQjpHs02TKRimlK7bUav0p4KjMlKKGqG3VLg-xe9ComjbsBRLnRflkKSPg6IxmZqWJ_nxnHaCTxmiAFPXGKhDK_glXgADXS17Aic_NuKgvl5whHA2bCXGtPyk_Pplomrcbh29CUCHn_6iJG9R8fs5S1M4WjcZL86yOEZzpjo26f5q5v1Or-QTZq_M90i9tF5jnIcQ-N3v5q914auH4Eaxof8XV0okWm9X3eK3ZPMrZVJKS8FvKoEbRGPfKD33PObaof5aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjOlnyyPG1bKsk_OEau_2rYZ3MHEMIb0ebt1xLpHMIbmyBpkafxz4wLM3XnN-VNZCrU2y0xkn-knW_IPDTGm-AXisWecV5P1a2NglyAGNdp6YZZpW8bTxfNBDjSirQXrvKY9fBvorCo1ZuAWcRB3B57gb_mDD3XJsChGJzV_0Ki3BFNJ2DOKOUV32HQ0FX143eZGYTUf1W_D59FY-lGgMNR7SURpa3S_FF6oC4oP0PIJwnTT8-NeSr5GINs-CZeAS8T2J3G30UkG4sL4yFvP8ens0JZqyE9tzF7RmBqKxQgHFRj8k6_4pxt8187RboQJgqTRyE53Endo9Pz6yU9_DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=GAQYKa1imua6HqjdsrUlR_v7Vl5XnEbqm8_AIjX1w17dt4QxB7GoENyzqtK19VhTysK1-u60iQQFw1mWLzCnE0lE7XTb9zKYOGZVosM8CBdqdMnfG-bntmdg1OwryoH9LQEkCaewKM9BZxuJxL9GAlZke9a5DvhMUPLVq2b2yWuwccwJDWq3T47nuOXAd7MNdifZ5LqyTzqP9KeZphytixFjlfXRuswuBrSPMZXHbPSFBORhR9lShcItjMtbcTgvdAKllbgK-ObL3lUWO_BqjVZnfYisz1NPTALaSeZff19WXY7C0PCDaQgyaGc1iF8wyfBVHohm-4QD_mWSSOFUMktm2rbu0Wp380KRziUwwsvWWE3qyniaCQiFGfRcPyG8VO5gQdHYS63fFtsQwx3RyQfHwWlIIuDya4ZlVmRTYriuawi1zmV1S5DM6MlFx3Zl7XEWZkU1Nj47cnd9B8PkY3oNl39mn-DF2WgvLyLIk0LDDSw5kHxRC5Xwk3qp_JcDcOibFGGSJWNqfpvmtzE_eOyJ-guo4tjm4d1Jd88U9TP_PF7O_8tv9cZGsJedxO7TK5M9GC1Q82BtxjVzI32Lzqc6-MtTV3i5A3bz6caOJqX-He_WdYz8NkCkbmYB_t56MGdSlarJ7Dm3NtVW3AullgjreXXLzb1qe-OmsVRkrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=GAQYKa1imua6HqjdsrUlR_v7Vl5XnEbqm8_AIjX1w17dt4QxB7GoENyzqtK19VhTysK1-u60iQQFw1mWLzCnE0lE7XTb9zKYOGZVosM8CBdqdMnfG-bntmdg1OwryoH9LQEkCaewKM9BZxuJxL9GAlZke9a5DvhMUPLVq2b2yWuwccwJDWq3T47nuOXAd7MNdifZ5LqyTzqP9KeZphytixFjlfXRuswuBrSPMZXHbPSFBORhR9lShcItjMtbcTgvdAKllbgK-ObL3lUWO_BqjVZnfYisz1NPTALaSeZff19WXY7C0PCDaQgyaGc1iF8wyfBVHohm-4QD_mWSSOFUMktm2rbu0Wp380KRziUwwsvWWE3qyniaCQiFGfRcPyG8VO5gQdHYS63fFtsQwx3RyQfHwWlIIuDya4ZlVmRTYriuawi1zmV1S5DM6MlFx3Zl7XEWZkU1Nj47cnd9B8PkY3oNl39mn-DF2WgvLyLIk0LDDSw5kHxRC5Xwk3qp_JcDcOibFGGSJWNqfpvmtzE_eOyJ-guo4tjm4d1Jd88U9TP_PF7O_8tv9cZGsJedxO7TK5M9GC1Q82BtxjVzI32Lzqc6-MtTV3i5A3bz6caOJqX-He_WdYz8NkCkbmYB_t56MGdSlarJ7Dm3NtVW3AullgjreXXLzb1qe-OmsVRkrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=mXJv4JdMkc6PMi7QdGqMfz06JsaVcRifDtJr6TTU1hoIuGZJuTS9ewVvm_n2h1Z_yICBVel_wv3vJKJCCSgF68Av1DA4ERnNIw9hzVRvoJE0rW3SvRuy2Oq4grJurgWiYpTeEzuSeYPEe-DrxyWBFLpOQbSVbP6jEMAegPevra5ZZfv4q-PVLik-wFs518BCedzaE9EwobMoIwA3Np2kHBNQzVBw-kV_4jTVbBedbkY-8E-EqDVvSMcjBZE9eDZsK-pqEGoGKEunvNj7HFnAkh4xrNR045Os1heaZxFO5AqUNArqGs0kT5m-E5A5YzzdEjQEtXWqchGnyT7rje26II799ypz0eEhmsUyL8wgfj3X5MZ1RPEIlBmIyQmng4U7o05622uLqV48M8rbDB4PqjoL4STTmV6CbDbFL4snelsO6K3BWvvvq_Zuf-hdf85-PqKnu5Al8DeO-3YuwsaiR01StUOGl468MuUlatoRHknZr1l_c3ikXurSSobcZ9oBH2yERiEeoON8xXJGkhU1WcJR4PLQKh3dnzgOVO-Lk6zJyITL3kMzMYYmXDuhnS7BLGom_kS6q0E5598cAkVCBeRfV8K5yEFlAoqzanQ95jz5DDdvSLJIP40NcSNGCC9cmnMpXUi4Hq18FHFG-7wAMGTmh0GAP2tNFee6MUARkSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=mXJv4JdMkc6PMi7QdGqMfz06JsaVcRifDtJr6TTU1hoIuGZJuTS9ewVvm_n2h1Z_yICBVel_wv3vJKJCCSgF68Av1DA4ERnNIw9hzVRvoJE0rW3SvRuy2Oq4grJurgWiYpTeEzuSeYPEe-DrxyWBFLpOQbSVbP6jEMAegPevra5ZZfv4q-PVLik-wFs518BCedzaE9EwobMoIwA3Np2kHBNQzVBw-kV_4jTVbBedbkY-8E-EqDVvSMcjBZE9eDZsK-pqEGoGKEunvNj7HFnAkh4xrNR045Os1heaZxFO5AqUNArqGs0kT5m-E5A5YzzdEjQEtXWqchGnyT7rje26II799ypz0eEhmsUyL8wgfj3X5MZ1RPEIlBmIyQmng4U7o05622uLqV48M8rbDB4PqjoL4STTmV6CbDbFL4snelsO6K3BWvvvq_Zuf-hdf85-PqKnu5Al8DeO-3YuwsaiR01StUOGl468MuUlatoRHknZr1l_c3ikXurSSobcZ9oBH2yERiEeoON8xXJGkhU1WcJR4PLQKh3dnzgOVO-Lk6zJyITL3kMzMYYmXDuhnS7BLGom_kS6q0E5598cAkVCBeRfV8K5yEFlAoqzanQ95jz5DDdvSLJIP40NcSNGCC9cmnMpXUi4Hq18FHFG-7wAMGTmh0GAP2tNFee6MUARkSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVzUAIzv1Aibd639Z5fgJwOVbjtvZ9MJA7hYvvMRb4D9I2wKLIuGUH_8EWkzXZ5iFeVmAhB2Vpq1XYb5KgZHfZtKNzKff_jzIoVlUf9pIMjI3YPlqCGWS6S8tu4KWV_URAbkvtGAaIwcgCFXyEvsCDWZQHYGrr4KPq6U_aS6mnYhwjrJ9eiCdIzla6h8kVjE9jcuGt4DbZzTA6tzzth4rvXNs40_88VZXc4cpDsqWKne6uh9QcAVIw7kdmsC8dx1K7-EDMwi_33D8FpSwcfc_sujPEv6ifVdnx6Uzv13mz1F68og4NzVCStETdvdXfWqhTAuAGZgeuQ5kRgZtcrJ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=S7Y9zRuSFJcsMelMvERyw__IdmvNn8uPBtqH3Lne8sISiSHYYTIPR5YcPl3h2BQVguJr3NYq_LcilrzKJgMecvdgnrWHnKliU8gieAY_dXsEEvSV85_CGtXS1N0V7OdnU1Y5gxEAM7TAqs7Ysdaqct1ul95uj7EFBRbmkzSG1-_2xUN6IzlqlD5Em3jgZkqsvq8I-egi_wmSzPct9enlOj3ak0rEWmWy6pYz1Ks5nKNhXu9rcgTZK-wVo66U5Frrp80UqYGeoEIzd0uFEq8rsOzaoHfpUYItTzAt3wczLNu2ACd_HF7VvcgM9hKjbSeLiB4eKty61ep-m8rJzxHXaqp2xj2lnyg-02qeJ6yci8zQsOT1RS_MBeXOYFgJMS3bpOyFzqVeSFO5Jy_b4jiF1jmNvNi1LyC73qqQkd73-saiwQhTyLuwWH90x3FJr4g6o_ffRg73RySi3M95Ik55OrTBC8KO6xnUMULt_291_sMa1OKkohL8n7CX5AdCZGDpiA5G9p9omQIiKr07lBqcd_MKmsG3J1Hg7bbQTU7Zr1V5IGsgrpdAfq1Q5ZCBo5yuGd2Nd9QUDksGWF079MJdStqfTMpDO5W7KjxDXd3nwcoCuL7ydCYMSrnbVlvfoagmAMz9Hsy6xQ5w9xm2yIlUkyOimj315eTTDIyK2MjU7W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=S7Y9zRuSFJcsMelMvERyw__IdmvNn8uPBtqH3Lne8sISiSHYYTIPR5YcPl3h2BQVguJr3NYq_LcilrzKJgMecvdgnrWHnKliU8gieAY_dXsEEvSV85_CGtXS1N0V7OdnU1Y5gxEAM7TAqs7Ysdaqct1ul95uj7EFBRbmkzSG1-_2xUN6IzlqlD5Em3jgZkqsvq8I-egi_wmSzPct9enlOj3ak0rEWmWy6pYz1Ks5nKNhXu9rcgTZK-wVo66U5Frrp80UqYGeoEIzd0uFEq8rsOzaoHfpUYItTzAt3wczLNu2ACd_HF7VvcgM9hKjbSeLiB4eKty61ep-m8rJzxHXaqp2xj2lnyg-02qeJ6yci8zQsOT1RS_MBeXOYFgJMS3bpOyFzqVeSFO5Jy_b4jiF1jmNvNi1LyC73qqQkd73-saiwQhTyLuwWH90x3FJr4g6o_ffRg73RySi3M95Ik55OrTBC8KO6xnUMULt_291_sMa1OKkohL8n7CX5AdCZGDpiA5G9p9omQIiKr07lBqcd_MKmsG3J1Hg7bbQTU7Zr1V5IGsgrpdAfq1Q5ZCBo5yuGd2Nd9QUDksGWF079MJdStqfTMpDO5W7KjxDXd3nwcoCuL7ydCYMSrnbVlvfoagmAMz9Hsy6xQ5w9xm2yIlUkyOimj315eTTDIyK2MjU7W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqqMDE8yTvR_w6cQ70VumYaUBPdpJCrGAoKIMy4l-NmQc1Qz7GFxJxsA2t6XZJFVAteXoNMoxh90RwGdDkyjs_SRL8iGSZmMn5nahaUEqi7Mn7He15Jqg3WsFz5uZgfJ7Ybn1GZi91VNbWo0JNAQn7fln2oCt9DG3jzI7HETtWxKdgmjhQWC7RA2t56dWW_bjZuHXclIRAZKUJxt8LCpMK0FUrgcddUploVZyg_OqzSMzUPYAJgDibpcHRL-1iDcjqqT_dBRMNyywQRSpS3HiLpQawe8Ush57OqRumt0Ou8gw2dOczPbNWA05VEtAAkQSefJ7MVJ9LSCR-_fgl1zNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6vk981IEp8fjLc_NQJTr_msazOfwmI3zywyTiLuwXZ-RUt7-OtWSXiLRvuil5pad7OE6JWIITzH7FoHlpu-ScZhqdXaV88hkLRPCQRtxy5p36lU6SNWzg5h88DnvBOgxH2GXzO3SvazB8mzMmeuXC32jiYNvEh5s09-OqXdItrrBCwtVZoFjACM57MOYlLtrv5v1OtnVmH9q4AV-PSCVuvH__gSlVvaYW-eNREwzdK-9Alhn7NG8b9lTnZOmwKpiIPoAK_mQoiie-XPfb2r43muXLnJLNLLqY7Qbi5VxlNnofKbDoLp_59xcUuOzMVmL4Bo-KhN30y_9R5rtIX8kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=KT-raloBp3K8bbsWb_w9Pq9wpW-f0J0ZyIzLw0XlA8dDjDAlHZ0bA4YF3LtNvHvQ6ELcQtzGraOPWpTWDRVwTIp6585GwBw6H-mj0zoAL3wWR3piaRSXzRI0IYCFxl-uK8QYOm0WWzdeCNBWf57TgWEaFvtO5e4CZvoiNUJE3wrLDtKoXXK1aDRtd_jGaGzXn8vu2SY85fmINlrLnafPYAz-jwCLgRj55oCGEnndKeBWi3GvZSOabO0JjhYHzw9qqStwOXrLvWuNzsr5vFcm5770CC937WSPd3dHBg0ZLhhFDwwvKAmmBMoGk_JZtFuFz1gS9E_3SwZ8EqkF8AfHCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=KT-raloBp3K8bbsWb_w9Pq9wpW-f0J0ZyIzLw0XlA8dDjDAlHZ0bA4YF3LtNvHvQ6ELcQtzGraOPWpTWDRVwTIp6585GwBw6H-mj0zoAL3wWR3piaRSXzRI0IYCFxl-uK8QYOm0WWzdeCNBWf57TgWEaFvtO5e4CZvoiNUJE3wrLDtKoXXK1aDRtd_jGaGzXn8vu2SY85fmINlrLnafPYAz-jwCLgRj55oCGEnndKeBWi3GvZSOabO0JjhYHzw9qqStwOXrLvWuNzsr5vFcm5770CC937WSPd3dHBg0ZLhhFDwwvKAmmBMoGk_JZtFuFz1gS9E_3SwZ8EqkF8AfHCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGVs6O7CSl4GLZmp0nh31QK8CY84N-BBfYOqnKlqMCMe_yfaGRhIHjnLy9nrCceBmCE3WXUkCTLeFiIWKKk7dvxHCdjA98pTVLGQbKZVKhgElb01117MT1-tltn-DYdo7tk9OiaR-l5lXNaPYAPFW6_peXRQvCgQRlNXltGJzRgSXcf2Nt0MWeF175sRWgHBcgaHzYZksc_NFrDISAgyLYcs_8jNfst6nvAvA64Buk0PDsHtPuWNyObkdRX9nVoCD469T3wjufctrSq-x809G38qJCtwXrlP-vTNw4zEn2Md7PZKw8bimAhwjKP4Zj8hUN35vXkH4upqEO_jaE5pjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwBuxv9Jr28i3bIS5JL_2MOnWVK7WDW7CvznuYq494iEFz8xzIxRCJfGXgTPUW8RtqS_AG2lKJZN7KIypTifQBu-lN4tXo836UCrDzgduQzI2WrpOjwQWyKlI3L5Vkxdq7BO9a6EjcBAxIsBsMJL4w-Q_wc8Zx7Xv40WNZGcq6H_7oTKAnqSAOnOF00iD3teHucGX7HaMhD2u5T1TpWBNMy9v-8yvxDCENs686Nn3NUz93LIo3IY73U4w5ZwZ6G9KJM-347u0Mx-wSF23_OOSzyeO2Tf72ggf6y-Ac7bzeYh6oZ1cSKuP9q9SetaMrHnlZThKq-MZ8ECUliB1fAFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1ys5ufQQQsfKs8CoYF468u3G1a7ToU13I1B_VF-6CO9qJ3qHF5WbneE3-7S4ngxVtEvyx1y9B3qKJwKXwkubq-PFtgI_YXpGxgqyScs9XuEXQcu2AUE1ZyZ3tniBk9S2-1g7TGvjohw1xvoUKmAeZhh-HbY5BOCZi4tn5Iz9aeN_z62Ci7N9W_Qp3GmSEKbSTNHtDLtWf72ExiYzHUZc8klBxwiHAzPbBIYpO24LH7Xrz1x9jrOF3Q4WaHPfztt-XgytC3t-Or7ycOgUsD78euqbEkpLDzmy25nAB1ljTKW2ACQM5nP-RIu9oVx8woiHA2UVsIs6sUfkac9y1psuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=r7CpmgS_PmoHAwcjmsKi0GzCyFz7s0U-Tvc3eJyH0o10WytKf2BVbqQ0romrIyEoOVCOOZ2LJIxhv7RZ7LfGAZFQypt63uKa0o53tKIeXHAVE9BSZ_WrAnS2HngPv7Vh_L1INXjnlUO80tYakphuuBblM1xOd1-CEibhmVFcUj_Fj5ERFyr_uQN4WyZntiVK032_4cYOTNH2zioqYZzu8E1RD_734LZf7jSc61NlLjJs6ZAyIBg3cp51uEiLvvFn6PVRiBjfBd5Fjr5yQhXfAebdVneW3hgZiAfDZ_fStOEgomhnnGeCfMD8oruzDYlGHo3qsQfgyzeqHHeGskJnFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=r7CpmgS_PmoHAwcjmsKi0GzCyFz7s0U-Tvc3eJyH0o10WytKf2BVbqQ0romrIyEoOVCOOZ2LJIxhv7RZ7LfGAZFQypt63uKa0o53tKIeXHAVE9BSZ_WrAnS2HngPv7Vh_L1INXjnlUO80tYakphuuBblM1xOd1-CEibhmVFcUj_Fj5ERFyr_uQN4WyZntiVK032_4cYOTNH2zioqYZzu8E1RD_734LZf7jSc61NlLjJs6ZAyIBg3cp51uEiLvvFn6PVRiBjfBd5Fjr5yQhXfAebdVneW3hgZiAfDZ_fStOEgomhnnGeCfMD8oruzDYlGHo3qsQfgyzeqHHeGskJnFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=kA0TXagh_k8z8L99nbqzYHFtN5Cszt4jlFDtyEGxUPmhKdx3KrY1KIvElUUjEKgy7PVNM2BOtolyMVNzSVQC8SnzctwjEuFizKA0KlDlbfPaZYSOoHliBLH7PlzVDLuv1uFvrNjc1c6PiVuNVA6I7zwGsdTHgcLBSZ1nYDUUT_CH9eT6F_4MwQtObeTZ8dadasBI__qonzNHqUL_rsUJ1qio7aCx2x2ejK2i3RsPVrhm3dzivWqgU-pkOVFZWYi1kCf-DvLprnjLdwVJaED8cOzVwBaE9TcBxTrlcnKPVaQUrlAtpJfuqOvUUsitp2FS3CZK78Nb3Ewhum5AjJiPwCXJiOMLGOM4bQTmlQbkBTPehD43FQO8n8D3m4MqmF2nCgjnIyUhYAX38MLC_GJw8xnlX4TbZ3Ok175fk-Vq0ow5UQ2B-GFpHQLrbcrly4mS8nta6X-tDu421qva1ZjmWB81HYB4ZktqEu9-Csu8FfkW8x1-EWVQApLjdFghY4LOQapcchiQNsX-2tjB8XlWPwKqHzxDTtYVY70hTIA_NXDqEEVJ3zOkLBcNsl2kTvrk4arR0cwA5qvQ9R_CEeVG9XX2ofT_FrQJjQP1PWNGRhGtJrsMCASQMGP9kv4PyUZDBVMWA772Gp92qGay1owNErcbA5VPKCuhJNQAE1BH8Ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=kA0TXagh_k8z8L99nbqzYHFtN5Cszt4jlFDtyEGxUPmhKdx3KrY1KIvElUUjEKgy7PVNM2BOtolyMVNzSVQC8SnzctwjEuFizKA0KlDlbfPaZYSOoHliBLH7PlzVDLuv1uFvrNjc1c6PiVuNVA6I7zwGsdTHgcLBSZ1nYDUUT_CH9eT6F_4MwQtObeTZ8dadasBI__qonzNHqUL_rsUJ1qio7aCx2x2ejK2i3RsPVrhm3dzivWqgU-pkOVFZWYi1kCf-DvLprnjLdwVJaED8cOzVwBaE9TcBxTrlcnKPVaQUrlAtpJfuqOvUUsitp2FS3CZK78Nb3Ewhum5AjJiPwCXJiOMLGOM4bQTmlQbkBTPehD43FQO8n8D3m4MqmF2nCgjnIyUhYAX38MLC_GJw8xnlX4TbZ3Ok175fk-Vq0ow5UQ2B-GFpHQLrbcrly4mS8nta6X-tDu421qva1ZjmWB81HYB4ZktqEu9-Csu8FfkW8x1-EWVQApLjdFghY4LOQapcchiQNsX-2tjB8XlWPwKqHzxDTtYVY70hTIA_NXDqEEVJ3zOkLBcNsl2kTvrk4arR0cwA5qvQ9R_CEeVG9XX2ofT_FrQJjQP1PWNGRhGtJrsMCASQMGP9kv4PyUZDBVMWA772Gp92qGay1owNErcbA5VPKCuhJNQAE1BH8Ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaeayQPmLubHhJBTZrlvA3kAWkz2ExIwHPHqxy2n9N0Ne88gS9bXy_RiHuVTfgEQn7-hlHBbBchdP0qbTrV54BtIL7UDUt2UmCycdgratOKrpDS4OkDazGe2C18lRyR90qLZCvDu9epbJBYNRh1VbEunxqmbZqt0Jy1PMo7LxEjV-sIa1OmA1kilDs_52_dJTJEb_FG9Qn5_VQdlWKQhlB287_I2m0i-z6BqX3aD-srkSoZGESEFcFM4ZRy1EQJo19kWAU_3vjcZzeYfewrj_PwUEJxDOY1uNQOluU6Gc2ZWAH5QqSCr1Pu1GGh32W9W8wrI6qHNuk8qL31ZXH0D3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBjKEdtYzr22kldmAMoLXuRGF1GE5pcpRg_l7U-4qMx1f-dZSoLQnLPIJtXWJxX9iI7CPmlwrPhXeBjNRwSIq2kmoLA-_xYUMLAaRpVYriy4mcKU7aIx8JpsymJCRlKs8ZfqXbAK_hjOFp8mpA0HeW9CedpmFNomAg3Mk72DfJm5oCxq5laG4KGW74FKTl6qZxgIuWqQcNBqHt1z4SoffhL5VqywRiLsBt9dlvamunAJQ8tV1h0Sn6vmxxa0SVNx0KNbfN5RcfzAfmGYUsPrgx35ObZbZsqQFUdqDyYzggq0gscQAw_QXoix8atNsFD_qJk-SuGRHOKYrmjCPA6NLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m-r3xI4isu1O-QFc6Q2S5m9I-TrrAl023TP5SJmp81zQE6y02z8_WaLmWQrBMMw4L9FXOxwa44Q0NHy77oS9UC8MB8-MJ451PyUXaONQ30TxBY3HjMD1IQFzSu_R8QkP-_mioEK7ZaRB3jW_UuvvYykGoLq9ACAcdqke0CMWrCp_COWW81JmW9KL4KXLRm8GI0pchrBDnbuCnqbFMaujtIu-edfpt6ug0Q98T2pvYQfBv6MxMn7SaB-crgtd4C7FK2Uy3MJzB5UeTiMPaAz_NMTVh5illmLfdoutq6FYg193sG3pPwn-axyR3jB8zL9CuZkBaKtwMFqTcEkW3rPzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=YpidJZrIHutQiPtSgGtfymZreAnfsKm-XEufhx-cfe7qsUCghpd33z2-2jgTYyqFhaUysUfJAUpOrijmz68-B8iEOHGF2NltAn142oyOE4idZUHUi-Aj8kIx-VMkRSlJH6eM1lHJPIYZLKDqFMSNTeecP7Cipta2q2zrH_i4JHhks9b0ukNKC91WLX2lk0_4NwF4b2_cSIqXV20RJzSo8NQ_AQ-8ZwFkCGFFDFxAZau0SMtRlEnlDyoO13LgtR78Ge_3LIioIl_VeGDDkLaDXvkq7VjW_tdxhNJt23XKEVneWjoPIbQnLlroZo_bvkwqau2B6zuSBqurd7tzi180Z5KoBjDxax0RQp5Dtl2QI6WPByNMKJ_jMdI7X5n1YQwpo7miEM0wKqj8tIQxs1nMa91-IY-JMpELQbs45IL8CNAVhO39NWxvt0hlS8ij5T4wwxNJI-6dLXqdRwKy8fCYwvCrRSRclxDwkEM3Tw-_H7_OauRRY-gwr6aE4umY2-VqqPtBsMqwOFVDSvjVSCTM3Lwrio2GNmXqLu1P5guzTPLDG5J5nKb1JuPSl85jW5dmHKieZo0bcmIyX5nVl03SFFKlVI4JVizZRpJ0FtPUwAnnGgQROuboJ-M0Jeer1fh5UM425FRraf0gDQ3Vy7UfHYrjll5g8RsKpm2mA3eSL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=YpidJZrIHutQiPtSgGtfymZreAnfsKm-XEufhx-cfe7qsUCghpd33z2-2jgTYyqFhaUysUfJAUpOrijmz68-B8iEOHGF2NltAn142oyOE4idZUHUi-Aj8kIx-VMkRSlJH6eM1lHJPIYZLKDqFMSNTeecP7Cipta2q2zrH_i4JHhks9b0ukNKC91WLX2lk0_4NwF4b2_cSIqXV20RJzSo8NQ_AQ-8ZwFkCGFFDFxAZau0SMtRlEnlDyoO13LgtR78Ge_3LIioIl_VeGDDkLaDXvkq7VjW_tdxhNJt23XKEVneWjoPIbQnLlroZo_bvkwqau2B6zuSBqurd7tzi180Z5KoBjDxax0RQp5Dtl2QI6WPByNMKJ_jMdI7X5n1YQwpo7miEM0wKqj8tIQxs1nMa91-IY-JMpELQbs45IL8CNAVhO39NWxvt0hlS8ij5T4wwxNJI-6dLXqdRwKy8fCYwvCrRSRclxDwkEM3Tw-_H7_OauRRY-gwr6aE4umY2-VqqPtBsMqwOFVDSvjVSCTM3Lwrio2GNmXqLu1P5guzTPLDG5J5nKb1JuPSl85jW5dmHKieZo0bcmIyX5nVl03SFFKlVI4JVizZRpJ0FtPUwAnnGgQROuboJ-M0Jeer1fh5UM425FRraf0gDQ3Vy7UfHYrjll5g8RsKpm2mA3eSL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBppwBTLWfmj3J5rHjt_Ox_rHWSXd68IdQmz4GFsIWpe8nFdSJrRdU-AhV0M2QFmUFuAbgyAJb1jXV5E2ljg6nJmhe-1T4pxgT3cST1SGxQ38aaktYsAtRJetXuJo-0HlnWTjIqukEUDnSZWt5ZuA5njaqT1A-y8mlfPxIad8KiOxPwCR_TrOxNe2nxt07p3Dx_Re5ZCHTPeLlhwJXZhi9p3Uaz8rMBIw_oHz9CHOSXQF8TgXfG8vIIYENLMvzHQc2KLcRXXT9fAt1HvnPag2XTd92wFH6zn2XLWw7ikqmousvfaKIq3RpblgiSMH-EcejeqHRc9ctJXFDR5FZ5x5Rg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBppwBTLWfmj3J5rHjt_Ox_rHWSXd68IdQmz4GFsIWpe8nFdSJrRdU-AhV0M2QFmUFuAbgyAJb1jXV5E2ljg6nJmhe-1T4pxgT3cST1SGxQ38aaktYsAtRJetXuJo-0HlnWTjIqukEUDnSZWt5ZuA5njaqT1A-y8mlfPxIad8KiOxPwCR_TrOxNe2nxt07p3Dx_Re5ZCHTPeLlhwJXZhi9p3Uaz8rMBIw_oHz9CHOSXQF8TgXfG8vIIYENLMvzHQc2KLcRXXT9fAt1HvnPag2XTd92wFH6zn2XLWw7ikqmousvfaKIq3RpblgiSMH-EcejeqHRc9ctJXFDR5FZ5x5Rg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-LMaV1NO24ypr-sLV07L_LLE4YJ2UATqnbnM6ibnkwBXPPWf1BylnToNlDb1Uu1AnP8YsJGJa_sn-cycoDGdXR30UDYTbqYmILt8OKPqWqzph2qYHw8ZfNeLA5TvbNc6ueZdUPEqQ1DmrvLXCputdU5KU1Vp8BWNaLbc_fI1vRJ7g9KH59Wcgy1LECHW9C56hn5LEKP7JwYSwCcOsYLI5d1JL172xeq4Br06C8FnLAVFTffd-zpmPkxuUCVcHIvkd_UKkWkRZ5VNqiX466bHahlWpr88KGqW5DtB7RoMqC3CD7DF2vnRT-C-w2HZfd9yJHTgyOkDL0-c1UbugbaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcGjrNwbqAvBoMCxzYHVYOfdlEX30bJrcVh5llGn7q_FjDdGR5l0iKkdCCAUYP2N_cK2u93ni5dzwZBSFY9ZxZYFcmV197O_JE3oZ_Jbr8ComU1jygwqZRLMDH9pdzy3YYp4NjuqsLQYmuyyvy4w-WrixtY4-gdDOBRkWITzfa3ieTDXygyJnJRpwoalac4Dh0TNLtuTBCP8Z4DuhRNAd14PLmrU_Mmt_VzVgASBfDNvmT75kFmM8IQQH8I7WuVFh5nuseW0gGxacz8koFMonP9YPyoJGQedZi0ZrXrOrKtNnGVjsLaVUR7kVXOAHCRLh5ZoXqnPwcwtS2Jrrdfk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
