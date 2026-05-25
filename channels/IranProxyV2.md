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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwm-AwGQxTCTKEmdK81H3GiB042JrRVvQJN4jmEDdWp99ARJjnBVbrsV7R8pS2Ab2f8K8rnxl8LWq54ocAH4BoKaP_FKPQa9RJsJ3Lv71v5AQPDzrFLUHB4nby18wL_RSU1GdK-GRmym2BbZWUOHegvWkKh5bMIMweHXPX0HN-HbG4_gs8lAHk0AsP0InGB1bjrURuUCqgTq-_6GpDClfPIAhFgx4dm4fgVFkh_K2H9UBngCxhot63aggnNMFjApkGsDQpLpUkWEPbV-aQUYoeDOx5qhQWJioaGsaIn1H8Zd0NjIJ98vGfgn4h0UBag_TpUsc71_6ozSKPsmXGJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5P40kYaoToTNGQUlQqzMlSL5dQWrcZaH9g-RfVc_pCgONXPvB0tOWCjk1vrYbzp5EZwVM0U8ub9K3BSLJfy4ZUzwhJTbp93QwrntyZpRRHeEcD6l4QLjOrLUWoc6yjk_Znp57NRAvrVhV6bfzx5PosTVT3EZkQpztmkKGyOa6TloYe1T5no15ydCIeRL2yHysNYeJg_vJtedevFbqexfZpzh6K_zhHemD066azLfPhGVtp4a5zglhCYo8efCivzHoVZy9NcB5F4gobSSVSEcu8twGJmmosNztG4r1c-NoJnsCunXaiB2UC4594Jy6ERsA5rQ9PO89em50qN0_AloA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMHOXSRZ_joYW7vScqZxL3txklFcEdH6GzlswJvsBmD2shvF4BoXtk_xeStE2NhnHZqueZ9GmeTEvf-nm7p8Y9lkUpAKo5KwrqA3SaOXQVOH9JqyjZesuD1wSvJ_T-199vMt14cr7Xqxwg0Dcnkp3HZcgH6aIxAG723c8e5_G7XuylK6NZF-JIYIKnjndJGA8QNMhmNXachWewQhQA8Db3B6FZ_Bp_Q6gu5u_uMkV41ZKXBuJOJutVHiyKxlQpOm5X-whaoTDnstcC9C4MmlKmTHzUd-XfKWOof_BYcLt4oVgto-U8KdLNBogMo8uddgKkIDy6EfmPWDIaD6xGerog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke2t23CalTBz9SvobsS2yUT-DfjG3cwkVNUgMPQzVClDSLGEoMxlLJ0PAAwe1a1GryQLHsJ7yUFie3otbbMcyVrXzbNs90r4Cl9TlqyUzQ82nehbD8O0lxOyHsgbq5otcvNUZabF6wJbNjOwa9jdRQauCj5cg2yNdxiBPqlWw4Z3yehJWejVJcnTnrA4A0Q7sHGDrJjzDX4iExtx4DjNDmr3SvzGrfBClgJSgxZ94WtvHOkClMVNCA-pJen1pjUNncjrt7BfDNElWaqmBL-gUw8-4IMyiq4mIPUGRzQnxeH0Mf7_YEMh3RZfbO48anOLO-FmpiiNFv3J6QnD7_mK8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT1-C8UU_Zjx9HOE7C7zd6BJGRwyETt5P1OKH3uwDyiUah1KiN0mOCHnq5sbOYj7ab_BKm6k_976KGLbXo1n0vq2umktXC99Y5Q6QN-HtLZe8cP0ehZmUh1BWwtDTLDpzKGtUBmkeBqNJ0JS8p-fTUWjpxp2MLkQE9N9gwzAw3zBKa74XGXY-ut4vu36hBq_sKH-R_p2l4lucnB0G6_WppWkQpiHYKIUMCxDYjEtmwhy8tYcsCbz97TjoexGJkFEdVpnxcaeBUwzk9JMzjeDcyjTw2DtwTlbxMdcxUMv_TiCmkorB6a6vse8nRWMyTxQXx8gY3ZmiPpc9Ba0yWVpCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMX1tZ1pCiiaBOcp4To1N9gpJL1v2uDEMHi5pVLKzAYCPRgVckXDr68U6C3niJ0IX1ZgNQdCN8yArvmDoqV_ti1xzSyLP9oyam5mJr1azeTFskfeH1iBPI4NykppLb8VyrfBWH2sfz9CUmL1hVUOYTEmrbBShExjFM5LxfV8TGW2MV6d3KZHN7FYV0F50-CGoOXbyPsg3VZ_vJqDm_UTxn8t8-BdnQvR_NFeTm_NzM61NrfLHrbQy_C0DNSChYpYq_Aw8Qbu2KDyQZ396LxZcwH4xQ2B4Grfej36JTDP_9aVnF2aORFCcyDqi_wvT34H3bp-PC7k06_zLUXcFgOxTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ7HNNrnuT8I3bRQ23KAdQtAFV2B6JYceX8mdOh_Cf_De-volA8VKzgCHJQtb6lbgwD-JBmJlOUoM3f-ZYHNwjaXZLs9vdnEgbOSk7maPiIQzM-jqa6bWEvYFJE0cpGImnlh7hAglTedyb4bxvufPlZIpXnVAOz9kzZ8wWs9Cx714Gj3t4GsQyFup-gw7jfFV7mt6TVr1cXL9RF3KBLkYBNWKrWqiBBfDq16SQcH4AOcQ6DWEh7AoJ3mLGcYN5LFmrrba88wMjybz1fU1BiNougRZwBBWEQpu7iokCp3Qm9aSi4u6bceWkj4SGEhv_Uf94gaqonJNDYFlu9kb6OP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=YMfo74r5BogYNdxlIj1AlPsSMzBIXQNPSLdZas4KL7fj2v4FPboz9lVPXuBsio4y5nNYsu7VN1_zG1-7nM2wERcEo5-LlzkAlx2i4JL9yrS4SwrNEQNMfXQNisCRciza-xLbH6T8Bw1U7KInRBk33lf43Omn_eXOOhe_YKgLFu2BPa9yVwt9UF0Dh-CanI04sFu7DGj7bBkAFUtf8aL40MJeGVy2yonoy8tHLbxbWI1nv4HWL_hoI1XvZNpfwTarUKVSPfhUIAkh4npxzX_J-vsxb-AeFll6YevB6cb0feeCjuPj-pKvuP_R2qn_Oy6CV6QVEpooAeu46FMIPQapgZ8yIuyRkMQFe3QdIeoChHkA69a3u8wv6S-nKBXLSaE9A3eNXsZMzWIAwBlODmKLnGR1Apy35wEErHwsQnGpYjUK7s9BlU08B7x9OjsE42841WvzMvMkb6L-kuI7JKvn2HWfkZqhIoJYtWLK9Y5B55gNa8JIyMn1VwyfwWnYXXRYnXdHXEQyWo-aFRe176_jE7hqBo5du2oPSsUARwjI4u7QEcbEnHwv1L_1Ivw139eMPMRloYQDexX1m8usWEqp8ClgqTvWAWOlJxqaBwFuLBWDFv-LOoLumtEh2jVvwerdX8eZDFhRNG0tqCCh87VGXI5ZUyVQovlQCpTUMyQZu8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=YMfo74r5BogYNdxlIj1AlPsSMzBIXQNPSLdZas4KL7fj2v4FPboz9lVPXuBsio4y5nNYsu7VN1_zG1-7nM2wERcEo5-LlzkAlx2i4JL9yrS4SwrNEQNMfXQNisCRciza-xLbH6T8Bw1U7KInRBk33lf43Omn_eXOOhe_YKgLFu2BPa9yVwt9UF0Dh-CanI04sFu7DGj7bBkAFUtf8aL40MJeGVy2yonoy8tHLbxbWI1nv4HWL_hoI1XvZNpfwTarUKVSPfhUIAkh4npxzX_J-vsxb-AeFll6YevB6cb0feeCjuPj-pKvuP_R2qn_Oy6CV6QVEpooAeu46FMIPQapgZ8yIuyRkMQFe3QdIeoChHkA69a3u8wv6S-nKBXLSaE9A3eNXsZMzWIAwBlODmKLnGR1Apy35wEErHwsQnGpYjUK7s9BlU08B7x9OjsE42841WvzMvMkb6L-kuI7JKvn2HWfkZqhIoJYtWLK9Y5B55gNa8JIyMn1VwyfwWnYXXRYnXdHXEQyWo-aFRe176_jE7hqBo5du2oPSsUARwjI4u7QEcbEnHwv1L_1Ivw139eMPMRloYQDexX1m8usWEqp8ClgqTvWAWOlJxqaBwFuLBWDFv-LOoLumtEh2jVvwerdX8eZDFhRNG0tqCCh87VGXI5ZUyVQovlQCpTUMyQZu8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI8HlxaEbjmZbSjbbQOWm9Pu5FGm2ICGjOJSAYheKUhOm8ABb7ZS9KwMofjTk6NGwmN3wPirbJ5DlvoYlUTdJ4Yet9ZqJwFFualknkqwWC2HPzN-fDdJNtK9Q9QCWRLwKBt7oxejWkUO_Yroh-m2ORsSMiuQjnggWfE-5GY2LqHUPU5uLQIlhxsynyw9Y0TAuIHRFqbcp0vT77xJvqzhx4Fly47IqVhpdlH_z-BfCsCIvyrEhpllBfcvKJgC3cB0vjbMsxKMzYwZ38btf2nl91tsTdHTDtOqjdxgXLVA705HAzM7lP_hHOe2Zo3JbNqFYoHBAoo55pxNgxLAqCVHHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYImexwTjAG5JWp12gYr0a8SKDP5PonKLyTFp6n4Vxksilsm8pYrDEvnzmRry5xa4OPi_HxxSUmTUmh2CVendZXegeBjB5fDv3MWybakPKQJ_38JdaF7mesdny0KB_SCm7eHU3m8MaUR5mFa4e9wDh2t9_vVil4Xu798Qtxansblz6_6o38sYbEex6l30_mPsvmLTeb8EkGwqD53EhN7ufggiIUO-9Ct_NXZ3haAGMYFRt4zIvnk3mb8i1gl5Gx2IMEQ1-SMBQ7BSoALabI-HkP9ExOgx8H2l1U-rqSsFD2No99IaijHMFukkGvhWM1KD8NonVCu5zbR59fdl4z5Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0zn-6csJ4PzrwvwLxb4cMcCr1QJuRCDJB5hUXRrFGIuL8qTZqJg3Gi-Q1rxyT2psNeXbDszjlUfR3HciNCyzM_EhKTXzCFdiD33ltGxKv5lCjkdrYx_VU33wBdDV7owMm4cbcoxsIXeuTGRXACqRW1lbN4yQ94VGy1b80L6ZQD0GD7-Nqty42NGWjISoaS03H6iw5MNV-cdYI2t8WaLjnSyxlvNEvtb2qSsW49BRXKXM_o1QNBXqmULTi4pNg-eAWjSeZTHQ-3wh5fUWYBQvj6eE4gm19S2fbMNigA5QnzbwfVB4JKenrYdPMBhk5L-HjfEinzPHE8WpRQigNKQew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=VrEumreFMtzAOiT9Sn6tMDNi4diM_MTMh8QKh9UCU3-IFmdYBl3-SjT9XCJADc9IrExkawJrK4rZQFye1m39VRbVSbX1B6sdiLrxoYGMiUmnBV08XGhYI3fY2jU1F9KHlnA9foCi4Tc0dIYFhlj_e-mVAsQ7nJPkz-_XD7PK_2YXDuqfhVJGqjVOEO3vRLM9JWmqD-SiA2ekFP4HYqblZeYhSqaCmLw9Njb2sKiep0sxJTGyl6-paIie0exCvcyMNsTwfzjVESAfJfAv1NOE1BzVyou2v0kP2HFy7kCmTNUAtZN1uFc5_0vkPm_uXmfDw6lZ6Lw5eYrpXUhHPwXu9WGjVIjrG5hpyGwChRBd54CVYfRg_3hIwxzZMA9QBEmPeML-yoYlYX3uSR2IYmQegWe1bhBHaGJo4XwMByKCNJp4uA-aDvEI1EggYaQNVXBNjVlS9CAB7zyo7DWdrrYNMaVYJ0-l115DPqn5iZBptLjqnqFnpiQ_kg90iov3D9w6uWuTN69Hg8JvCCky5OU18kIBJ7n3iub_OmwcPEvChsTpu3D5rLLVkNVhIGfO_dvCg5SrWGrEGMoLIj9GJpdtp84I4lH8qOSPI0mgUf3XApJhfSzgmlFkJU60PbBPtYuxM-XVxvGGiYhhqnQowfnbHBWT533QG1UTTALszixYI00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=VrEumreFMtzAOiT9Sn6tMDNi4diM_MTMh8QKh9UCU3-IFmdYBl3-SjT9XCJADc9IrExkawJrK4rZQFye1m39VRbVSbX1B6sdiLrxoYGMiUmnBV08XGhYI3fY2jU1F9KHlnA9foCi4Tc0dIYFhlj_e-mVAsQ7nJPkz-_XD7PK_2YXDuqfhVJGqjVOEO3vRLM9JWmqD-SiA2ekFP4HYqblZeYhSqaCmLw9Njb2sKiep0sxJTGyl6-paIie0exCvcyMNsTwfzjVESAfJfAv1NOE1BzVyou2v0kP2HFy7kCmTNUAtZN1uFc5_0vkPm_uXmfDw6lZ6Lw5eYrpXUhHPwXu9WGjVIjrG5hpyGwChRBd54CVYfRg_3hIwxzZMA9QBEmPeML-yoYlYX3uSR2IYmQegWe1bhBHaGJo4XwMByKCNJp4uA-aDvEI1EggYaQNVXBNjVlS9CAB7zyo7DWdrrYNMaVYJ0-l115DPqn5iZBptLjqnqFnpiQ_kg90iov3D9w6uWuTN69Hg8JvCCky5OU18kIBJ7n3iub_OmwcPEvChsTpu3D5rLLVkNVhIGfO_dvCg5SrWGrEGMoLIj9GJpdtp84I4lH8qOSPI0mgUf3XApJhfSzgmlFkJU60PbBPtYuxM-XVxvGGiYhhqnQowfnbHBWT533QG1UTTALszixYI00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=M7B1-yojgw6KLzjisjnU0bePs4VBJ0ZH-jyhADiqlEQWctx6eqOFBhnavsn_Nht2tAR9WP-HVYte15txcMeXQlPdz4aarYC_k5JCA8uvL9p8wfsGD5zukY55ec1N1Kk27fNfXDYRIJug2D92xQo3W10NuSjJtXZEcdkpDJh0RSDMy5EGJUKm40drkXXyql9GbzRgwAmgpHIX8Uui9EMdJZRW6VlNPW-sRMPTHTGkM6DFONLXFBaOnoi27oUtP72RBEO7b3YuHS-w05zjrmqvuqB-ptfYkmTdT9iXMAJ-8SSzMZ9ASe5iuGlppwxihuJ8hlMB_qANigS3dNoQLVuSq54fZFcIhSlUB_pY4E0kOQdDGGIz_l9miF9OmIGbBSEzfE8ctDsjyG5AnUCIKxQEAx2pXnbWTK8lJnCYCO5dlRUOZZgyIgpfDm8IWSS4EvkOWcSm68xCpIBgq8Q5A_Eqr5LLSCJNPmxSg0X_k9Q_gNeRJNX6JmJuAH64zYC5rxxkSbb4QZtcglzaJTASrSe1hE3X76dGZQBIhCP97RwoscTaXTAiejhpTOMvAtU1v2i8pXEqRZw5xlBWfvCAljzQNZCjsB3UMpHa5MuBTkJoMn5frUditgoQ9R0M_9bs4m555jCXaFY5RwVQB56HtP0nO24VrwHD5x2HVxtEqqHHMO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=M7B1-yojgw6KLzjisjnU0bePs4VBJ0ZH-jyhADiqlEQWctx6eqOFBhnavsn_Nht2tAR9WP-HVYte15txcMeXQlPdz4aarYC_k5JCA8uvL9p8wfsGD5zukY55ec1N1Kk27fNfXDYRIJug2D92xQo3W10NuSjJtXZEcdkpDJh0RSDMy5EGJUKm40drkXXyql9GbzRgwAmgpHIX8Uui9EMdJZRW6VlNPW-sRMPTHTGkM6DFONLXFBaOnoi27oUtP72RBEO7b3YuHS-w05zjrmqvuqB-ptfYkmTdT9iXMAJ-8SSzMZ9ASe5iuGlppwxihuJ8hlMB_qANigS3dNoQLVuSq54fZFcIhSlUB_pY4E0kOQdDGGIz_l9miF9OmIGbBSEzfE8ctDsjyG5AnUCIKxQEAx2pXnbWTK8lJnCYCO5dlRUOZZgyIgpfDm8IWSS4EvkOWcSm68xCpIBgq8Q5A_Eqr5LLSCJNPmxSg0X_k9Q_gNeRJNX6JmJuAH64zYC5rxxkSbb4QZtcglzaJTASrSe1hE3X76dGZQBIhCP97RwoscTaXTAiejhpTOMvAtU1v2i8pXEqRZw5xlBWfvCAljzQNZCjsB3UMpHa5MuBTkJoMn5frUditgoQ9R0M_9bs4m555jCXaFY5RwVQB56HtP0nO24VrwHD5x2HVxtEqqHHMO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJgrTgI5raQ8F7KirZqTbPvfAuk7DyuGiOsWUDtelATlhZMYgBBGySx0G5-6xY0rR-T9XT7TObsJFc5Xk1ClWTu8-6WbiQo9iKWss14T2lmx8fm_LnN_53CBEwfWCMx08A_p5B3ub9pFo5l-xGw8sEg0AkWM-_-0ZxpgLoB9Q9F8eh5nBs449osi9j162ZB6koT6Kc1M-apwGqAb4SPjLzxzlWVLFaQAqijN58FTw0DehGSWyCh80gUTpaqz3AO-6-zEw96AafUBSiAVmXZ5mD2Auoc0QMnH30T3_F-Ie1EITlbUCmM1JyvROIBKA0XOZkf710M2uKo37ekkK7QCxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=rY537r8ST9bzCCYuMVtSGbL2vRSFrpNcn_CWKwP6MVUCjrBeMyZLvOtHTld3GtCOP6ssRiaano1yjxNcesP1_pnP6jk584eOIQ5zjHNXgNsCceUIoqh7TiXUyDUJKTcR8IENU9Pg3GGgYqeq00eiIsrJ_C1JUQSNNOXvLuvdKFpjhCPgelPAgE4whQykXlTk6yQeiXehMdaBMqOANqMx9T60Zkr7N__wx8X3toWoPY1fc4zLbCZiO5UL5lkSQ1yCM2q8Is-1VV1vW5flmEvkGkZgO8fJFTYfttPqZCFCo1qgUg8MQ6LYFCHtqQUKSXmpHI_Idx5qaFbHjET43ELO3RgQwKstnhYq2aaHBMEFb5AuGE22ZbqVXCExhrVRyUfHt72803OQUn8YaYHcB5skjkIdmRiofDDUiebe1QcvqvhrraS4et6TqnRXEXpfBSbnf-IqCmiuM1FSelXmsT6EdqFkB_3mqnkREBe3aSSFCoJTQoV2zcS65GjTeBEXTHRZpgz8yaVwk_MPeUAn0-a9jQZ64NXrQxUDtMBH2B3uuiWTDMPw91ph8eDW1MRzX9c9paIrohfr8dEYZfl-o0zebyHYw4FacgbY9laEO-uXtLeHpdZMEZO0CzrLApS4m8Z0KOQcf_ffBlmKqpXRgjaOH5VtZA5wTTtsxrtQ9xp5uvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=rY537r8ST9bzCCYuMVtSGbL2vRSFrpNcn_CWKwP6MVUCjrBeMyZLvOtHTld3GtCOP6ssRiaano1yjxNcesP1_pnP6jk584eOIQ5zjHNXgNsCceUIoqh7TiXUyDUJKTcR8IENU9Pg3GGgYqeq00eiIsrJ_C1JUQSNNOXvLuvdKFpjhCPgelPAgE4whQykXlTk6yQeiXehMdaBMqOANqMx9T60Zkr7N__wx8X3toWoPY1fc4zLbCZiO5UL5lkSQ1yCM2q8Is-1VV1vW5flmEvkGkZgO8fJFTYfttPqZCFCo1qgUg8MQ6LYFCHtqQUKSXmpHI_Idx5qaFbHjET43ELO3RgQwKstnhYq2aaHBMEFb5AuGE22ZbqVXCExhrVRyUfHt72803OQUn8YaYHcB5skjkIdmRiofDDUiebe1QcvqvhrraS4et6TqnRXEXpfBSbnf-IqCmiuM1FSelXmsT6EdqFkB_3mqnkREBe3aSSFCoJTQoV2zcS65GjTeBEXTHRZpgz8yaVwk_MPeUAn0-a9jQZ64NXrQxUDtMBH2B3uuiWTDMPw91ph8eDW1MRzX9c9paIrohfr8dEYZfl-o0zebyHYw4FacgbY9laEO-uXtLeHpdZMEZO0CzrLApS4m8Z0KOQcf_ffBlmKqpXRgjaOH5VtZA5wTTtsxrtQ9xp5uvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9PfyzzX4BcN194Wn8A_k7BNqOrAx3cM1mrRQatUDJX9aowp7XQaklmtXbUmc4u_A4F-LTndtAYsoQ3GP31XsMCbm-_oB6LtJ2sNhjrGLki-_x1mydUcxqrFags7rATANkYScw8mOqnmQdZhc0qPyZMNu_Z6az1X-eTNJyouF1W8BHjizqxbS-hgnPWi298lwy4ytDvFaT8Ku0ascgnVSe2D8-SEIdUIRe1N9rXc2GU5AI43qVqkcOPy0ICoSGp_cJ-VVXbW08t23G8dCkFnbZ0OW_3MGUeMgIgbilu9E3ZhS_gX9Vxh108pMwkjeOXOfZk6rrHOX9HEmbqxWl-tzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQBMi5sYXHinYmyt0l-uqFJHMxlGlp-FlzqvJyHfE0Nlqc2Pn_5BMqzrbM6x_KNQuWnNvgUMZ0htP49XJPs9vZYUjNAvXOlhyEstmJEy1X_VnhpB9P4B955NRgh5tunIvfcMkObwnGjGDTmsSxstwaMLhV58toGwVbNRNHhqCuEzn0HE9d2SIcUsrsUJ_JSbvaftjzWjwQmf2l7xT_AKsUCg9BOIy5Ebtn5_LxRA_1v-A9J-ATGJ2tCYGO0xUzyL6uIFqaOzeOMe9aSHARlHZTKGMzoMPBOCDXFFGNpDWxbNLsGXWywf8gbRIjtjaXNP48o4lzoWe8JXtc0RjJz76g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=qvOxD39YWC8-eBQYSDxfmWUIdwIeGEQZ5mxA4E3qWhT-CXJcL3x-cturb402jRf4OCtg8n67wKfIagaxNiDEML6CyyBIYViBZ_wUqRdyoG5pGWafdLuDf94c2yw-idVqYVZj3oZ-VVL-KXCtfKQLjLTl44guo2eqPvBo3srNEDKqQlvDW1DAUsVnVZ2zMj3yYp4U-45znwOnwDQXcQInLYN7Cv_YEf6kEj2SY7e2MUdKmGug9KCfcNniRJLnOBgy5EPQzQG6PVC_umUyIIUF79z1H-h30c3v8zreZvkZOLVbZmRh7XtQzXwbsovDROKe_IqBpTRvyjZo4eQs_SameQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=qvOxD39YWC8-eBQYSDxfmWUIdwIeGEQZ5mxA4E3qWhT-CXJcL3x-cturb402jRf4OCtg8n67wKfIagaxNiDEML6CyyBIYViBZ_wUqRdyoG5pGWafdLuDf94c2yw-idVqYVZj3oZ-VVL-KXCtfKQLjLTl44guo2eqPvBo3srNEDKqQlvDW1DAUsVnVZ2zMj3yYp4U-45znwOnwDQXcQInLYN7Cv_YEf6kEj2SY7e2MUdKmGug9KCfcNniRJLnOBgy5EPQzQG6PVC_umUyIIUF79z1H-h30c3v8zreZvkZOLVbZmRh7XtQzXwbsovDROKe_IqBpTRvyjZo4eQs_SameQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLRfjYB5jktBfOovSuOte54osTMzA6zci-h5WtmE0h8exNsHvx3fnIAtxQo7SCs1zjiBQtCREIieX2BYsgBc9fS_5lIq2EuQ91x4de3j1wYUN5Sw-KtkP44VtDO08Mh42dd2MSO8oBKahsdY-BGcszTgHUnztgv0BblJYathAMef09Unup1cdkTl93o3CiSEY0VkrY7XxnVZRZl2hck4cVDUL2h82dBc8e703Ix30R1seme9dy5xdnun2Cvu8WfeUtUbnE3CUKSCjfhyTagofwKzjecPdt4y4yT5LgWqbD7Vb9OJA24uAirSCfK9V2kpPnzeNNuZR3-hIZsmfIRScQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEqSU4vptPIjCPa9or2j76cFta4DgWkClqZUgn0nMsGmwcFWanuUF1_jpKfmZyIZSf_u3UwieJeYEI6ofj6czWyeUMVpb0AdAMEw-KQUAPLz9pJpJDDJgDnsubxgWflwnecj8Tscj2qwq6F9JDTqVuldf4yqX_r2F3u7FAzk5i1z1no6e0GEgbiWQ3p0u1Bxodg0qglAcVYlzM3ptevHWSKp6YrlN12u1BhMa3GSbZfB_UaNdhISaP5d9uvXNgKAk6ja6y4femaoHm8tvsjzuC91DoEHvmG8-kSeGWq-TOPJJRDUtkWGrDLthAk0fFmxIC_JimBfFheVxU91-GZORg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=FHPJVBEbDey3m3lWP_HGTPlm5o7sii2WhYAhMALJ0-Zw1Ok182StOzfJl3D9CdYQ_qFinNUS7MftBomDefEIwRBtrzHv_IkSpvd822pdHeylptaGEDzgF9PvHGikrACjvTqcHM86iudUv6QUI1qexpP4-vdtA9PfTWEVoR9eiwmfR1WkO2ng2KaVYQ_7WlwMZDzTR5byh1YDTZWzXo7v0Bb1XSXK_Hn1-CTpr15b11fuojmvpr7k-1j83nbrLMqciXtQvvvD3jtoc9YUJ5pHuhey-PIT8osvqcTtxpZRRcZS22y3TZ2nkE7w47mCLTxnbgaI0chu8OXd6swvqRX8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=FHPJVBEbDey3m3lWP_HGTPlm5o7sii2WhYAhMALJ0-Zw1Ok182StOzfJl3D9CdYQ_qFinNUS7MftBomDefEIwRBtrzHv_IkSpvd822pdHeylptaGEDzgF9PvHGikrACjvTqcHM86iudUv6QUI1qexpP4-vdtA9PfTWEVoR9eiwmfR1WkO2ng2KaVYQ_7WlwMZDzTR5byh1YDTZWzXo7v0Bb1XSXK_Hn1-CTpr15b11fuojmvpr7k-1j83nbrLMqciXtQvvvD3jtoc9YUJ5pHuhey-PIT8osvqcTtxpZRRcZS22y3TZ2nkE7w47mCLTxnbgaI0chu8OXd6swvqRX8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=nkFFcPIt6qRei1KxSC7VahDExqhdsRuiFZG4HhY3ErVIrxDaxIuIT4QIiKr4iUsgrB61Ipsv5XGVedC-jzZaocp6IEakcN-itHU4HdlKGd-KytuCPUO7RQX5dKQHxYjp6U7u1r55xj_5WfT8PgOVyyXk0beRb6dJjHgtu8-0UaEfTywtXLVuNuLmVgk_S35_cgFVjrStf1YrfFNFq7qUWMcWmoW-tLPgUFE2hKkB8eJ5y0bAOrMJArLHluglR6EpzhigzQDtSQL_-9_l7D_mUpGNqZQV2lyzBm_rW3yN4AWH31gSKt12WLY-Aykex7E4gYe-4NaDYgNI4I6mMT3jYLNK06mV5QEGN0F-yn7xWgABlr0LNsrfVlHV5rxP_Etl1gCTnCek3TjTpfsPuccyOJIfkKSmKIpyMbkVxVYWoVk0gB-H-661VN5mFoS7GPuikrm4T1rAuRWCFZCBubeSflyq3tKRUAz-fDB0aw7XAxw-MXRjb7N09BACt7UNfmKaET5JvE2L6oeHz5kX5m_yG1kuGEeWhB75DwgIaWpqi9JErb4ENxeKMumpVXjdjFbH3RhwMnVtMHddreg1PDN-xoqWJyvMY1WqFOjLhDIpDNnfgYvdFOsZch1qEshswxjsWRZ3Ai0FyoX4PMxgnePGED_xMnBPAuTGrCcErGe_854" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=nkFFcPIt6qRei1KxSC7VahDExqhdsRuiFZG4HhY3ErVIrxDaxIuIT4QIiKr4iUsgrB61Ipsv5XGVedC-jzZaocp6IEakcN-itHU4HdlKGd-KytuCPUO7RQX5dKQHxYjp6U7u1r55xj_5WfT8PgOVyyXk0beRb6dJjHgtu8-0UaEfTywtXLVuNuLmVgk_S35_cgFVjrStf1YrfFNFq7qUWMcWmoW-tLPgUFE2hKkB8eJ5y0bAOrMJArLHluglR6EpzhigzQDtSQL_-9_l7D_mUpGNqZQV2lyzBm_rW3yN4AWH31gSKt12WLY-Aykex7E4gYe-4NaDYgNI4I6mMT3jYLNK06mV5QEGN0F-yn7xWgABlr0LNsrfVlHV5rxP_Etl1gCTnCek3TjTpfsPuccyOJIfkKSmKIpyMbkVxVYWoVk0gB-H-661VN5mFoS7GPuikrm4T1rAuRWCFZCBubeSflyq3tKRUAz-fDB0aw7XAxw-MXRjb7N09BACt7UNfmKaET5JvE2L6oeHz5kX5m_yG1kuGEeWhB75DwgIaWpqi9JErb4ENxeKMumpVXjdjFbH3RhwMnVtMHddreg1PDN-xoqWJyvMY1WqFOjLhDIpDNnfgYvdFOsZch1qEshswxjsWRZ3Ai0FyoX4PMxgnePGED_xMnBPAuTGrCcErGe_854" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVzlgAcjCo4Ajm2Mjvw-x8VCpqlDwynhXKNwsln_U2re-z9V9Idfb0XE9i_MATfFaoarBUbfsCgibYShzZsn5LOtAfOx4VCwpvbQXLUkG9cmA7AZ2DKxdxMXqdXQZ5BC36JTTC4vWSKqIp1ha7tcHbjVb82IdMWrl--iNtq9UeKD1oQfcI_3NJQlIn3j29E1n8F1v50kx5Frib7TQ8gf7Yo1UgdSMW7tbQc7RPBXqcj7LuKyP6qtwuRiOll8cu4u0VdT6rTVZ3tkNUXORyKcXw9kci7L6QayiePP_Gk330jHaY7mzsEFPqTtHfKwsiom-6KJh5zr_YdlLqFMgvGFAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liSgD0Z0jfEwPy4xctsixQWiy2cxHuLGFF-QjWsLTW3-1XrdeLGiXtJ0zx9PCKrmXiw2mQfKI-clFWZNWJ3nfTDe_gOuPvbiQCQH3lky5893-0aQeC_w6eAFHDnPO7UF78nWWYcq-MhW7mv-lwIA2kRFsSB1AdLCkjAkpkg0LkzPNMo7mvct5DSpbBH_EGn9-O4C0_j-neDVgU2N0XzLlH8PVF14IyqmD53fcoDnAq6Ynoq-k8DeCCqQk9mcWVdbkZX_DGwsomajbdcn7hhBqjZn47jY2tmSQ0KyQbhhgJyP0G59E8FEAhBJgnU9X2COa-ykv43nuwVKqZjAUYSabw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdZGprKIZkgulpWUqd7XDSnWj2MyW5_T-Xpcy48jNHSQB89PFMxxN8sf915vmrLvTZogS26BE_qRIFtjvWmPGdCGoT9jm7ppHq9b2u7vsNKpvhVdaitl7KMtyjh0VK8esHwRAlBUUjYFx83IgNGdehp3a4lNRxGs7zSE6N1y48YDhvzgvERqlZbPBFk5w-naKFHm1Iut9RFLYTalQGT_RMGiQ7-ohJF0yyjvFlzjDXzEt_z39QBlAQZ7H67Xsj5Y67-sm27r0MtcsfMxOdT5z0UEd4H0xpvlBoxV62zuXBbG0zS4qNfWgJb2F3RHE79Fzl9uzLv6SSDrzcGGZNe80g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=CbVx3ptTUtt5lywITXaqDOBfHFXSK7gSJkh7QmvZYCuJjBovEB_rC7_C2QkCZKSoSWEl3vK9LDBBU1OBe5l-ELKvKtoWumkfwUpwp-ZKFE1P_7sfwjcIEmQEtfs-2VYbCaluLN43aeTy1ZOooKogOcnBPoIR2LI2LCrYy0apGofPUmFUsTf57WfZZFMe3pk2uobYoetRfAU4UHZQk3sgRIsjBxBmZTrzU9DVrq-ZIF5UPbPcC_oegqnXM71ErZE_s45SMGMx4vujBrxdj3B4KilTM-ScTKy7EI9yDnKKpHmEzXqCpLOUZkJ0PY7qyphsq0uP_0RiPcE9tqpCpPxbKhXRayF-q771MoJ0obgE45mWgmuBrogt0567n7XDVQt4IBRnT95oxak2vLDn6nA46TMmtq9vnKcG-EGskDoLhMAkSuk1s3F7cENRVtjxtoR-sHJ8n_p0beVAyEqzmz3VcZ_RAUhIWYwLs8vdvKhYTExKVU7l64WXC0S8W_LB9XDeMJ7VUXLckpHinJLHRFDRkkPoVWT1nzNA7n6PVSaV48UFq2LxCB0tuYnO74aOwpB8XfL8cMEd4ZdCBuS-e9KebtzwwViz8zjDgYh8FlaKd5tyDYqn_6ZFFUb9yYbizfCWgNgLiFiO38_npopXngvIxUK3F5jcc8L5VeeAy7L3zXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=CbVx3ptTUtt5lywITXaqDOBfHFXSK7gSJkh7QmvZYCuJjBovEB_rC7_C2QkCZKSoSWEl3vK9LDBBU1OBe5l-ELKvKtoWumkfwUpwp-ZKFE1P_7sfwjcIEmQEtfs-2VYbCaluLN43aeTy1ZOooKogOcnBPoIR2LI2LCrYy0apGofPUmFUsTf57WfZZFMe3pk2uobYoetRfAU4UHZQk3sgRIsjBxBmZTrzU9DVrq-ZIF5UPbPcC_oegqnXM71ErZE_s45SMGMx4vujBrxdj3B4KilTM-ScTKy7EI9yDnKKpHmEzXqCpLOUZkJ0PY7qyphsq0uP_0RiPcE9tqpCpPxbKhXRayF-q771MoJ0obgE45mWgmuBrogt0567n7XDVQt4IBRnT95oxak2vLDn6nA46TMmtq9vnKcG-EGskDoLhMAkSuk1s3F7cENRVtjxtoR-sHJ8n_p0beVAyEqzmz3VcZ_RAUhIWYwLs8vdvKhYTExKVU7l64WXC0S8W_LB9XDeMJ7VUXLckpHinJLHRFDRkkPoVWT1nzNA7n6PVSaV48UFq2LxCB0tuYnO74aOwpB8XfL8cMEd4ZdCBuS-e9KebtzwwViz8zjDgYh8FlaKd5tyDYqn_6ZFFUb9yYbizfCWgNgLiFiO38_npopXngvIxUK3F5jcc8L5VeeAy7L3zXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqAY2_V5XTkcUYKYmj2Ye_sSwckTzQ6I-X-HQOsJCSntTF-yCm-eshQOds9ob6RQD7M1FAGZLjaKDJM1lMl-YpxkymwHDEYcy5Ya8tstQ-PYtOuUB6GCZmNyhXdUpGTOniX0ieCAD47bgZJo0na2mvyY3OUSuI8zJKLc8-azosjRDt4Ep7vw1-oSu6mRZv_PGmr-LRnbfokTVKmySdNGaz77ct9QLYAicJF449aWmykHg1lWQRv375AfB2bTOTu86ZSqglPd_jacI46teaAnrIV3n_muhEcyWU44uwc6puiJ1PW0q60V_87o5oKkZRX0NM2R-0TGps_jFeD7qeA7MC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBqAY2_V5XTkcUYKYmj2Ye_sSwckTzQ6I-X-HQOsJCSntTF-yCm-eshQOds9ob6RQD7M1FAGZLjaKDJM1lMl-YpxkymwHDEYcy5Ya8tstQ-PYtOuUB6GCZmNyhXdUpGTOniX0ieCAD47bgZJo0na2mvyY3OUSuI8zJKLc8-azosjRDt4Ep7vw1-oSu6mRZv_PGmr-LRnbfokTVKmySdNGaz77ct9QLYAicJF449aWmykHg1lWQRv375AfB2bTOTu86ZSqglPd_jacI46teaAnrIV3n_muhEcyWU44uwc6puiJ1PW0q60V_87o5oKkZRX0NM2R-0TGps_jFeD7qeA7MC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYQIY-isp0q9V_Mt890FJ1REeWDadrh-wl5ZmVVFCrJdjMWKZnQfcCWGuO5Iq92RggBTmWav8oziSpFC4KAMHsem8dzo1DkC70t7WzuDfGJuQYxQSFvm0ahhUAB-00O8VKk7LvTQeXZljWdPtQPbt6C6azInrJbZPFWTKxcUPYcnCVYtB7roXcigNyH5A3bF_kA3_uC4Ffnj0c6p3Pc4gObFmIIOk3P4iRzvthxsNzVNDBPt3zQBUcxsxnaKDTzjGIR_ywAqSzoJwt1C4ZMTvZgiS9kC9fhZvBkUZxyO3oReg_gtPOPsbKmGKsZjG0_pyQJYz_n6D_q0rJf4wjxJoQ.jpg" alt="photo" loading="lazy"/></div>
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
