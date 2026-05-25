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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 01:10:31</div>
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
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwm-AwGQxTCTKEmdK81H3GiB042JrRVvQJN4jmEDdWp99ARJjnBVbrsV7R8pS2Ab2f8K8rnxl8LWq54ocAH4BoKaP_FKPQa9RJsJ3Lv71v5AQPDzrFLUHB4nby18wL_RSU1GdK-GRmym2BbZWUOHegvWkKh5bMIMweHXPX0HN-HbG4_gs8lAHk0AsP0InGB1bjrURuUCqgTq-_6GpDClfPIAhFgx4dm4fgVFkh_K2H9UBngCxhot63aggnNMFjApkGsDQpLpUkWEPbV-aQUYoeDOx5qhQWJioaGsaIn1H8Zd0NjIJ98vGfgn4h0UBag_TpUsc71_6ozSKPsmXGJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCbckK6TTtgJfAiNB8cTAagOrCgOG1Dj6aZBc96z-aJHkW_oozS7UvC_YOxsUYxP334t4YXOd0F4YuoloQttLu2XUwqfAR-BzbmIg03REke9869hUFk3P1HgcksP9Bmieohsl-pTh06SBjwAwppTTW31TRJ9K3jAG01BMqgYUaptq7YWuDfoIJQrnGKE7R700rfam-Wmia3TifsNxJkf5NsgP1JG-hCdKedUSXPAmo-QNw5P8-enjoZttiHZTgXTKxDQGCh7anvfWrMgHekrClBWfbtNbW_xgjn-GhQlrZbXV7wVKB3drwjYwJioA300NOCBWMJCyClIB7-mhRrGnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB5d3e0VeC8iVIpx3EUhrYYctLLY9X9CwugDWy5fKbW-FAXu08r22uynb1mEybJBrhpQB5Vz22rGbvvVQ-S7papdESSF1bM8I7rg4LxTL02FazTmvt7UkwZsSRJNMcrnzi0gW5NT9JhYQJf4CS57Qk7pTmppbknlTCUmltnOnR7ETC0pYnuyhJZrjDein-wL045LNTUxeoGpH4ST0FdEHQFUFYViMFdRhDxq14wElKMHrgLnF8KoTBNtxb6yIcjMznuyv6vKmPjSueYDCnilJh-V7R9paromQUuK8fWtyXwGUeUzMP5DrHXZCvAozUXk46iSuu8OIhnCwA_xnsGjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzi5Ww8ZX0l6tCFvzJUBdnQNSOZXLkPfHH6f2Ni9QZ5a6v-1cQty2pF85t7a9xafVpDzBpKU0rRtgfUC5yBzfF5KQ8LOKIjZRlMiVKyCxK9CTruXyDEXoKUpCRIcjwrM6Eaa9jvT-t2oAr7XtiVBFPU208ZPQ5Wp9e1by4niGkRPDBt5Lt4LYVijgmFjhS-qEjoPdp3RBUlPPFKV2720WXVPRMxyFa0sSWjIa0TbSioQLWNLLlvV7RSs9HsksvzfiWk4o4NnfZI0-eQROD7G4dh87fZXKSQziZt2f8Vciz18-BTG6xnH9PSN3jQ1urFfEqWu-c4ysc4a1xm9kwcM8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyYTRaikyFEEuK1zKD-Bz5_2o3liAjGpMPc32CNYaQx2UErXra4CE3R0UgF8D3ILr6GipI6eKUl4ekjYwq5mgAnlgOOjlKYsDIqHt2Swi_9j4FbE3m0XFF247X-NR8H9-QEV9jE5R-SUx966D8clZ1WglZ-uC-mdIInCNcsZ_r0Cn9RpM-gHWit-GkBJTM7FfOz7AdBiDhD1-mVqT4F8Qi-kdAHmIhP5imKi0INt_BJbd1dB0unVhoh4beMr7atG9xdVuoICgqIeKQpI_IsHrCwLn0KAk9imJyghzLumJSQrmaQ6n5z6rJpFGse_fd-fRq5wjxnoU5J3UGO0WebOmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpfMgkEmNvSTydEZBoewJP7FoIHAXI2dkClXMqLsL5hGLCzu64I40ZEv6B3upQdBnyqJkFIb0_04r4Ig-Ds-UrgRWd3ywW0Il5sJABsYj0gTXZMGXWpgIhtmmzb8a0PIk8Jps_uYFpgCg3xXyZKwZ2YRPoCPjgdWvVH0sTNy2Wja5sC5ZHdHfdrEXI38gQ1kWcR6dSmNfxfeD-E3ZrW4j8EPFBUVT_fTM6tiptrndEU3_lQ-xeZ_VawN7cQ6vMoNakMohGzK0RpO-PSR_nfXZSB8QbaeO1uP3MsEo-xdPgN1jeIU3tpS0yPwo8wHXE3pdMm4QjiqmZ7QJ8eIBNfwPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=nHjaf4mnkVdDb473K6m-B9ADJD21yCk7dVZBi-UyKQYtVwPtv8WkR72bqiECBYsnu6Lud-YppGDhZAqeslNJzfyXCdKU2q5leri3sUNqoNkH2Fj5r4CYiUFC88LbkvQ8I8qWdqjmtbSRex_7m1seIl68_JTB9WhYwUdO6pGpOodUPSfWIsYSb9sBNYPJEZpQM0fWLzwszGxkT6BkxBQhGSFIwRSMsZxcoW9bgHs53sW190H7zOb-T7PkVGYjLRIhohd5YWmycdxbFnzZLIxWjjwRm_-_CnzXLkJB6UA-8GK-PP1rOndZKGHhcj0qcmnAGO-aaOsi0aiv6W6ukVPZOaOCMencdW_0zLD8cLNtdwYjXOEKs-GlnxTDK5MrnBfB4TUpuSEZ3yLD493AwR-YU_8Fm47p-BxLggr6jjlpSNDO2UwGSN2xXWcmGJp2-oo-64V1hD0pgEPrMYFc4lcsIgj-uSHl4Fe4YDTGFZAG0Emh9SgAoRqbufVJjQfTP0cf-p6u1HagclKpo5JGuN4O4QgNiJCAX3kYvwEtLtOBIgLvm-rCf2DbCQ4raxnc6AXkfkMspWR9EVpXRP-dkMXuaNMwnr4CVAmCw8dJivI7fjHo-yMCc5uVtXmjkaCRYHC4lPFQa6OKwLqQuaTVFC2WI3SCOi50mIlyMcipo04XQtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=nHjaf4mnkVdDb473K6m-B9ADJD21yCk7dVZBi-UyKQYtVwPtv8WkR72bqiECBYsnu6Lud-YppGDhZAqeslNJzfyXCdKU2q5leri3sUNqoNkH2Fj5r4CYiUFC88LbkvQ8I8qWdqjmtbSRex_7m1seIl68_JTB9WhYwUdO6pGpOodUPSfWIsYSb9sBNYPJEZpQM0fWLzwszGxkT6BkxBQhGSFIwRSMsZxcoW9bgHs53sW190H7zOb-T7PkVGYjLRIhohd5YWmycdxbFnzZLIxWjjwRm_-_CnzXLkJB6UA-8GK-PP1rOndZKGHhcj0qcmnAGO-aaOsi0aiv6W6ukVPZOaOCMencdW_0zLD8cLNtdwYjXOEKs-GlnxTDK5MrnBfB4TUpuSEZ3yLD493AwR-YU_8Fm47p-BxLggr6jjlpSNDO2UwGSN2xXWcmGJp2-oo-64V1hD0pgEPrMYFc4lcsIgj-uSHl4Fe4YDTGFZAG0Emh9SgAoRqbufVJjQfTP0cf-p6u1HagclKpo5JGuN4O4QgNiJCAX3kYvwEtLtOBIgLvm-rCf2DbCQ4raxnc6AXkfkMspWR9EVpXRP-dkMXuaNMwnr4CVAmCw8dJivI7fjHo-yMCc5uVtXmjkaCRYHC4lPFQa6OKwLqQuaTVFC2WI3SCOi50mIlyMcipo04XQtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=YpMSCz6F-sm0V7qBwStC2wMFEWMYilwp-KpXiHHQy0OIYZJYmrz-WzemlwUCHYawmlibRr0xHlB6VhGTVVtgajOr9xJdLvAdh6eNWquS5_H2EIwMUcsX2mNYZubX6sppv4-vm0fWsOwL5GdunU0k9CjOkHxon31CSkyiedmMiXFxt9oAq1S1VI50JuXyiQhknCCEfQvk3BeVQxtZRqtyiwcKp4x6L6mPNpDWV7qvvU33XAlx_XuDU7HGjG0MQ6ViO7ALa4FwUbSXMsMzchCo8Zs7CTjGRaDfpbHqZ33jF0JMh178hVP8kRACbj2-st0MnpNZ5X09_2GXoOaoZVIedGZ1FiMHk_z-MbFAsBF9iLIICK3bILkwKYFrrdJ_Wo22heZpT6KLfVAyjs2c6rTnQQgdoyZY1EZopGKO1eEwvuRf_c6BI0vAwr6u5-O1Y6DRPztZeQDZDEBahafBT35FnuWcztjKx0NWOQG-QdKfvz_3Uu1tVUkYAbY7ZPQWhSafUM0IyAJKXNmCLi2-v1kK_7zWzbbCEfw2xe7dU47KKliFIjaWD0V4kiSSbJ5etV3oTX_FUi2EqnfWVWcVxS1BmpCylQJCW7bGmXugfmEWXu3KfTH7ZI7IW7CwrP_BYInbIqaKiEGJTVYQILrjdioebD3QZeqlH5-ozAvrFvixr28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=YpMSCz6F-sm0V7qBwStC2wMFEWMYilwp-KpXiHHQy0OIYZJYmrz-WzemlwUCHYawmlibRr0xHlB6VhGTVVtgajOr9xJdLvAdh6eNWquS5_H2EIwMUcsX2mNYZubX6sppv4-vm0fWsOwL5GdunU0k9CjOkHxon31CSkyiedmMiXFxt9oAq1S1VI50JuXyiQhknCCEfQvk3BeVQxtZRqtyiwcKp4x6L6mPNpDWV7qvvU33XAlx_XuDU7HGjG0MQ6ViO7ALa4FwUbSXMsMzchCo8Zs7CTjGRaDfpbHqZ33jF0JMh178hVP8kRACbj2-st0MnpNZ5X09_2GXoOaoZVIedGZ1FiMHk_z-MbFAsBF9iLIICK3bILkwKYFrrdJ_Wo22heZpT6KLfVAyjs2c6rTnQQgdoyZY1EZopGKO1eEwvuRf_c6BI0vAwr6u5-O1Y6DRPztZeQDZDEBahafBT35FnuWcztjKx0NWOQG-QdKfvz_3Uu1tVUkYAbY7ZPQWhSafUM0IyAJKXNmCLi2-v1kK_7zWzbbCEfw2xe7dU47KKliFIjaWD0V4kiSSbJ5etV3oTX_FUi2EqnfWVWcVxS1BmpCylQJCW7bGmXugfmEWXu3KfTH7ZI7IW7CwrP_BYInbIqaKiEGJTVYQILrjdioebD3QZeqlH5-ozAvrFvixr28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqIZR7eewF_CinlBx8kIlC6myAiPtbB8XZvCyQfimf1M8QPn3vlDRqvlcw1-yU2TNLWS-HCw0g3chr3tUsmtcvG09QBA-RsgZb_xcR3gwlvvo4SYUjmZy3XpxLBxjAD1xaKKa-ng9XBp41aK4TMBKuAKVN7rJt9g82znp2_J9VSThOTPrcG3jVT0K6MfdCc5AmfdGtGbOrlDEz-pHljr89wNqX1gKyVxvqMX9mx_TSBGGcnn-fLTIRIHLc8t2W3QhqVcDyD4T0SGsFE1xl-MfQByuSsc-Sa6uBmnT7a5C0v0QxVqhmOQYQqj67r20v7mK9_3XJTfNVlS-Y497VLtMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=bwI8Z7a7Sxe4hNgdwZStPtaWkOne49FMaUSwdHh-q0v_q9XKbAT5GjTt_SLAck898quNuvfszbx1RIN7el3GKL2mVQzzWqPQtfJbmKKD4q3oKkNPcyWBtuuTpOqyg-SpH5zZyW9MJAZy7yDSXljd1oAgCE0lUaD-OiNqUenJOewVUD8XADgyPAJqkX6OOl2vqM3CazpiggvWyU7lGWeCMJmEcTfiAq0HOTdmTwxmqeSJK2nLRR1iOD4GXq2qmmQUpd1lYOJU3e5RvL2wILs8pOK7n7_MmNV4fgfkRWSudA0BjRrWOteu5KWDG7EntpQqVG_kTCDuZjnFtdZMvBnxLz0uYJYiXiJQF1bmctwoVrPnWhoyrZdPbDxzxHAem3FOhoBOldfBQGBbZg4YONTAqxaH-aFh3jzplS4hHHw6x67Uc64gEBcbrApLWgxOV2NDfLfdwIdwfKr0DE5ZpnsB-lxyULasIv5qgcmY0rM-DIpE0i7XY3JeMd9Y2UQJ0ednmGRVc2tydCdTwTSfVzXpiGhj88ibk7IRNftngmK0ETgn5xvufswWiZWOThhq1c_WRaeEU8UWe7_B8-2gzoR5Tpy-R44kMMHC05NRJ7tPSoPRMeolyZkhgg8PMQuvKj8Oo-sssndlrz2XwLAwUKPzjrOHIGUMXsdVrU7htiFos7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=bwI8Z7a7Sxe4hNgdwZStPtaWkOne49FMaUSwdHh-q0v_q9XKbAT5GjTt_SLAck898quNuvfszbx1RIN7el3GKL2mVQzzWqPQtfJbmKKD4q3oKkNPcyWBtuuTpOqyg-SpH5zZyW9MJAZy7yDSXljd1oAgCE0lUaD-OiNqUenJOewVUD8XADgyPAJqkX6OOl2vqM3CazpiggvWyU7lGWeCMJmEcTfiAq0HOTdmTwxmqeSJK2nLRR1iOD4GXq2qmmQUpd1lYOJU3e5RvL2wILs8pOK7n7_MmNV4fgfkRWSudA0BjRrWOteu5KWDG7EntpQqVG_kTCDuZjnFtdZMvBnxLz0uYJYiXiJQF1bmctwoVrPnWhoyrZdPbDxzxHAem3FOhoBOldfBQGBbZg4YONTAqxaH-aFh3jzplS4hHHw6x67Uc64gEBcbrApLWgxOV2NDfLfdwIdwfKr0DE5ZpnsB-lxyULasIv5qgcmY0rM-DIpE0i7XY3JeMd9Y2UQJ0ednmGRVc2tydCdTwTSfVzXpiGhj88ibk7IRNftngmK0ETgn5xvufswWiZWOThhq1c_WRaeEU8UWe7_B8-2gzoR5Tpy-R44kMMHC05NRJ7tPSoPRMeolyZkhgg8PMQuvKj8Oo-sssndlrz2XwLAwUKPzjrOHIGUMXsdVrU7htiFos7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5rNISM7P1dIVb74PuqFa-WVc99wjlOaHkANwZoc9NKY6tZyU1mQer_reSiic73JJccqPjURmDout1JBaFIUGFEzdco81a7EBEjMSpjoa4EXmtJIJviXf1z5jJslkrgrLpV033dh9y7iX4WGmOEZ8n8ynqMvuyhnOWsYgE4Ujx3z6BYDX9iA6mSPdxmo-OdK5JG0LRnE26R3vhllifeNzK4V8yu4e7FGA1E6WuE_ymHdUjQDrJT9BDIVJ2JzReA1SsTioCNUJaWNJnYmOlhEs91bzleOzFWzHljvac4m8p--IF3nXLI_-hbLScHyq4zstawG2LoVSQxz8MF69lKVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=RFw4FWpi_tCiWZ-hDzWwu8kPYx5MNiHMUWP--cBLm7QQap5Gc3XQxPpfu7wEiK3cOXJQIneomBqW_fRLXH1fE03dfLTbrI_-35WWJMHsQWhnHnwwdqwCkywEb5uDKfrmh46K0pTO22yLGdsJOP6_IB_JsH5t1dbrIvTPrKJ2zRqTmH6NAipbTAdcBJpal1Yohj6tDaAwS-oGQoAtLySBbGV14N95j8_sgApxwprxDgS9p1BfWp5ikKXIcWu3YFG-pZKe6FiwWc6pAoxPCGfEoz9xN3e7gD7KmBlym24km_fepPcOTgVTSWOV6RHclgrbagDEFhXXGx5wzK1eY0_C9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=RFw4FWpi_tCiWZ-hDzWwu8kPYx5MNiHMUWP--cBLm7QQap5Gc3XQxPpfu7wEiK3cOXJQIneomBqW_fRLXH1fE03dfLTbrI_-35WWJMHsQWhnHnwwdqwCkywEb5uDKfrmh46K0pTO22yLGdsJOP6_IB_JsH5t1dbrIvTPrKJ2zRqTmH6NAipbTAdcBJpal1Yohj6tDaAwS-oGQoAtLySBbGV14N95j8_sgApxwprxDgS9p1BfWp5ikKXIcWu3YFG-pZKe6FiwWc6pAoxPCGfEoz9xN3e7gD7KmBlym24km_fepPcOTgVTSWOV6RHclgrbagDEFhXXGx5wzK1eY0_C9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKmnEIOJI5WH_9zLAUQAFirWftxLHrxjz7VmVA8HK6K58zF8BiIy1dXNoxW4nTjZ17ahI3tt6kRwCmnS4PDREBRXgmRoqWkJ9XzGAn6chzDlZJ4AARsf843msMNLH5RZAWLt73VTXSDYk4Zy04Ck2dhm9a_j1Qx1ck8EI2jI75I-5KkoAV0t1Ad_LdPA1wTM8Z3E7x2CNvetz2o_VoX1tvjdSFXnzFYWFSf00Cb8qGOPyTi2gU1fUKoIiQCwVase4IcheDmOdX__Cr5snAOb8p8JHbZUQY9wYehBUqlkRvZcnpbtwGQJ7rfBGHtCPK0G1aSKKyvSme2N-lSU9bteHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGf0EdAaTgoJ8Qt04Zwl_qzxiJzLZrb9Ix0x1HbpGlvXvGrR0FgjpmEUEke8xrVSlusB25FWvgLk9E3srZkA88gjK7gBB4RlaFYus-90vJJXON6dsr-8eWpsuCu12whrzmtWiRGAEJAPvRl-pVpWOqVihduvBaeefTF8yaTm4PTVwkSzRDMPEgsGIc1Cz1wLdnNOdRhLpcdrWAOeRXhtxkU8EJXzEozk5nGpAyj-8cNZ7RgrRBsBXe4t4U8LRcghJtBD8TIe9ayvmejntFaAOYh64b8k5jdVDXlkfma1GEunoP73ZENEAx6bbg9B7IuVVDo229lMJydErA6rCky8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=ersjccntIf5wmoLAVIUQRhunXd__YtbIHk6rbimummpUMA_ezjQmsOL60ca9-xsfQZsMDJQHVe320biDYxKM7G4XUoeyigEXOwUUW3RP1b4cJh4UBYYzhSw69F2RuyEoLMolF34FlXC9eilqgqGDFyWYNhGW-oti1HIOjdquQVpGKctLv5eBXcEjMNtgah0Oz3Y4ecX483k0fMsPqDmmA-cY6EfrWJVC52X8Ze-v22pRgeX9agpPHKT7YlzXoHrFiM4EI-8KSHan1ZA4k9XstwdH89cJsQEA8-IDnmsIE4wcZMR_c6-Wnzgl0hRUPfZsWX9NfktTIKvsO6BxtvfZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=ersjccntIf5wmoLAVIUQRhunXd__YtbIHk6rbimummpUMA_ezjQmsOL60ca9-xsfQZsMDJQHVe320biDYxKM7G4XUoeyigEXOwUUW3RP1b4cJh4UBYYzhSw69F2RuyEoLMolF34FlXC9eilqgqGDFyWYNhGW-oti1HIOjdquQVpGKctLv5eBXcEjMNtgah0Oz3Y4ecX483k0fMsPqDmmA-cY6EfrWJVC52X8Ze-v22pRgeX9agpPHKT7YlzXoHrFiM4EI-8KSHan1ZA4k9XstwdH89cJsQEA8-IDnmsIE4wcZMR_c6-Wnzgl0hRUPfZsWX9NfktTIKvsO6BxtvfZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=qyxd6xAI1U7kw3VnMc7Sdh-NTbs_V6NnO1sFzCHgk_FZWHKoiHMppVwZVoguWy5jSp0ywSvQKSK_SYaNIlbq_YmMPRCDajwxQBj4o6fChTCZgQJuUbMMZyIbNrUBhdXmqvfu2pkim2YBNZCWeX7aU7eEyEKOxoO_4-AoMoaqbJYEowyuBmVChqCVyE8BWcDlkirO2bqxuYaq6ebe6nQZLmAWATZsgJ9jrRyCNqCr-xRAoMMAQyhoBWkYu0mPAUMBQXOIJQMbsoAWZFWsaD6zgFcuCSy8zwTN6ttddQ4booMVDbjxqsfbzPNuExsaNwkFJ0OtrtqhDvvtVJbg9byOfgQloPTm1pl-Y45WbIWpHCWBVHq809AKX5Bx9foGUgF4H97Kz4UqnF8VU54Z78k-VOVm7vhVxu2_GmfFtHLwUB43FSFkga3ghzQGc-KW0w2ceiUI6dqU1BiOkvS1DgfRk-n6IhGbwEAPU69YQjsP8LumuWHTwPIHl_7xE5vJI2d9rDzK6hmvSeHPzF6dPnkVI44oU-9hbaL8WlLYKeGmbxkLpqsclLNP_T56w0J-dIKhGlB41NiGq3y_TIAi0tXiWX1ENk73S8zur5XhSDY_ohRaLiNOFBotSOioINWmS_6fp7cwxxaJ4Fa5dDLkminA9aLaIxer-PEX9ISQZ1icb1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=qyxd6xAI1U7kw3VnMc7Sdh-NTbs_V6NnO1sFzCHgk_FZWHKoiHMppVwZVoguWy5jSp0ywSvQKSK_SYaNIlbq_YmMPRCDajwxQBj4o6fChTCZgQJuUbMMZyIbNrUBhdXmqvfu2pkim2YBNZCWeX7aU7eEyEKOxoO_4-AoMoaqbJYEowyuBmVChqCVyE8BWcDlkirO2bqxuYaq6ebe6nQZLmAWATZsgJ9jrRyCNqCr-xRAoMMAQyhoBWkYu0mPAUMBQXOIJQMbsoAWZFWsaD6zgFcuCSy8zwTN6ttddQ4booMVDbjxqsfbzPNuExsaNwkFJ0OtrtqhDvvtVJbg9byOfgQloPTm1pl-Y45WbIWpHCWBVHq809AKX5Bx9foGUgF4H97Kz4UqnF8VU54Z78k-VOVm7vhVxu2_GmfFtHLwUB43FSFkga3ghzQGc-KW0w2ceiUI6dqU1BiOkvS1DgfRk-n6IhGbwEAPU69YQjsP8LumuWHTwPIHl_7xE5vJI2d9rDzK6hmvSeHPzF6dPnkVI44oU-9hbaL8WlLYKeGmbxkLpqsclLNP_T56w0J-dIKhGlB41NiGq3y_TIAi0tXiWX1ENk73S8zur5XhSDY_ohRaLiNOFBotSOioINWmS_6fp7cwxxaJ4Fa5dDLkminA9aLaIxer-PEX9ISQZ1icb1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D11oV_jBkDx0mZoNxn4KNP12BpYRye5fctDGuZWV5bEz333MKgZaFkpeGKj-rJRiqtEufdOvJU3Tm78bDcq1cVUBZwujb-T6LMYCOawemDO6rxswX87N7j9rRe-4bU9W43JNITPLqTvXWnVZoA31CIJ5kMMQrKZfqVzgG7f8hYY0AzdtE2hb7fdiE7zUnPVLgSizEDqu10kAP4s_XGhwKUx-rmiF87qBR-lwPZzSVv0hNHlwe9Tg3hwi_wU5JoHflcl24OZQmfS39nZCiC8uxq7lHDCMrJOIuaGsPZ-jKFgyg0hU-YedYccCmiK1y8TfQMlq8Wp1oqvLj4z1bmVXtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6mc_ZKxY9-H1nAVAGvcYow-n0tB6MmEFT4cFF_HCNTqmckn_F6sx1djPHiEx9Izdas7MVu7ztrDsOMdVKiR_DQBAKnTPLL60KpY7stuuBBSxccQnnLuh2sb0_4zkOyXiA1WohnZK3zT1h4lxvey26KBK1MTcm4fI9rnFs_MTfd4-mIz4ewOSpLkiEON20x5W2S3ayxQdTv7Nv6UDP9MvhHZ009_eOMqWdm7bIe2kgQOnihuGPRWcDsdGYIIg4Y1YR08SIzNvyvQpy8IpaVgiMB-3t9neSk7W7hLRGcYLg-dREsHk4wnL7i-xF7aKqR8BNl0VnPllK3R1rTHeALUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFsp3kSvi8EyRAUkjoYQ_H4E37_SXBVpeQ5pYgJc63vX1pT6WBY0na_URHoLajECCUMa0hhP53q5sFMUkbKiUn825Cb_A1QPZ9aVGnqlVHuJtYS6uwTxa-VPemkpWnMA97-TK_GIGZlhqkaYZUE9V8eoCiK0AqBuKecIhtsUJKnQcLv2q_2GH3gm-OC0YwAhrTwxCg9055_Ndxt9EVpjpsDaHB9M3spmp-mxGhLSzepje_JvZ4fGSJpBXTMZYnEK6xp31v8d-p5CD2rT0mnMCcA8j8i6_y2Gp8iXG3orl9iLiowTTWyPuXokB_17958pKaBVHbqaSo75AzdXAl2NZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=b2Y5CCiJXE1wNPEIVu3Ol1rc47kXkePNAWGXqO3f0cPnnD9YXQnn8vRL2KqOm5E52ladcbwrHgnpi0Z27WSqzmD7bOxZ3AOQ4AOsYaQdUrQjHY8jEb61zRGr3xBCu_oStZVTXYuSB7TrycucaJ_PTp8gV83nyPyIqD-uRmLwA7K1IPjvUYWAbIfWLDxP0XaFGzRetv4mqPKczuQeHt0jZZ0FEYKsuUTY3azZJnxLGgSs9O1Vkm_qjxImXV7LgQ3-MIjSIIc2MWNR0zaQAwbe2YORU4ZgQ00kzIaAkyjYYGUNqNdRvBhSjjiIPsA80z6MxJ8Ib4BTtpBbbTkLUO8e1jUBpoCrFlf1RBmB2D7xT1MBCl39iSTTBUpBUvxM5v0Uz-UIheWnl_azHfkAWObaOcKcyG2OlXm5ZCfGJQ-UkWTA-pS_GX_aPTi1g0wnpIS83lSX-qXQYyoC4-g_bGysTTZjEpcL0JTzCaIEkagvqQPdyJXT6tIJUuWtO4ttE4Kmcw1yLibUymq1pXzmIVGrVrydJOmyyABaLf8PDhhXPE8TU-322VjdQb0eKQIsloBU0CFhWmDXcC-eK1LogF2y9qHS7SUpnE5_7dSnR36IjY2T1rvb42_KnQ-zDQG2vo1R142YS_LlYnuCjrf2jStspVNQvw0Cga7zNTbpGnb7QNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=b2Y5CCiJXE1wNPEIVu3Ol1rc47kXkePNAWGXqO3f0cPnnD9YXQnn8vRL2KqOm5E52ladcbwrHgnpi0Z27WSqzmD7bOxZ3AOQ4AOsYaQdUrQjHY8jEb61zRGr3xBCu_oStZVTXYuSB7TrycucaJ_PTp8gV83nyPyIqD-uRmLwA7K1IPjvUYWAbIfWLDxP0XaFGzRetv4mqPKczuQeHt0jZZ0FEYKsuUTY3azZJnxLGgSs9O1Vkm_qjxImXV7LgQ3-MIjSIIc2MWNR0zaQAwbe2YORU4ZgQ00kzIaAkyjYYGUNqNdRvBhSjjiIPsA80z6MxJ8Ib4BTtpBbbTkLUO8e1jUBpoCrFlf1RBmB2D7xT1MBCl39iSTTBUpBUvxM5v0Uz-UIheWnl_azHfkAWObaOcKcyG2OlXm5ZCfGJQ-UkWTA-pS_GX_aPTi1g0wnpIS83lSX-qXQYyoC4-g_bGysTTZjEpcL0JTzCaIEkagvqQPdyJXT6tIJUuWtO4ttE4Kmcw1yLibUymq1pXzmIVGrVrydJOmyyABaLf8PDhhXPE8TU-322VjdQb0eKQIsloBU0CFhWmDXcC-eK1LogF2y9qHS7SUpnE5_7dSnR36IjY2T1rvb42_KnQ-zDQG2vo1R142YS_LlYnuCjrf2jStspVNQvw0Cga7zNTbpGnb7QNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBpRuyc3qCHDXk1yHHj-w4Emjn_YLlm5J3K-OjjCjGA6gVWDDHC0nZkd3mE6wlSsXEoNdefA0ErcYCsKawjdeuixg3J0vVCMGpw-I4I9UC7T94KJKhf7LPtvwwQyYbvuN4LqzTZL8voFqfzLO8hBm-bq3AyJO_dDi01q0dVedIbbl0PPek9ftObFpTen_rZhTS6h95SdqJDKmADoG5TZ1w12tZJRffmzDOyFyOAcC0ihnYEvUWwJZfce-vuxEijjICoYD7Rt_-qJFUew1w2D5KNkJh5b9pEIH-dFAHfyX5CZFQBGOC8Ru2YkK4ReRbpbU2CIwLSWOgG6afLh1AG6LrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBpRuyc3qCHDXk1yHHj-w4Emjn_YLlm5J3K-OjjCjGA6gVWDDHC0nZkd3mE6wlSsXEoNdefA0ErcYCsKawjdeuixg3J0vVCMGpw-I4I9UC7T94KJKhf7LPtvwwQyYbvuN4LqzTZL8voFqfzLO8hBm-bq3AyJO_dDi01q0dVedIbbl0PPek9ftObFpTen_rZhTS6h95SdqJDKmADoG5TZ1w12tZJRffmzDOyFyOAcC0ihnYEvUWwJZfce-vuxEijjICoYD7Rt_-qJFUew1w2D5KNkJh5b9pEIH-dFAHfyX5CZFQBGOC8Ru2YkK4ReRbpbU2CIwLSWOgG6afLh1AG6LrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzMC5PTxQblIoUntrJfhD9NsG_oE9hP2J9G9pds4H5aMlPn8pWs4ixWOv_pzyDUjjK2fX-oV19hQKmvb3HDAiXIIlkMNZc8qOQ15CG9dAfUujRASaFvqfCSk86fxevXKUZW7bj5uybOsFeXYLPt0XY9U9xLCP8WW2shG8XIprETS4zoTcpXuO0Ujpj0fXRcuAkY5XyUOsnJWfayVfsWhDtCcJKMRezrNQ5BnwsG2iM5jftzbiiFmB5i56GKdPLjxxlCYCPXkXXWJElPpYc0qugoMV9f8_iY2l8H1zEVkSXSeGK6XyYeNHvnxrQhwpj5aRIlYULFKwzNtYCD2oEMZwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULl7WxciqIlXRbWtkl8UrA5RB6OxCSkaN_VJpFcOnOV25jGRK8LLNF-b2VirhgNA8Yqr7uGyFwItl8U8b5Y3TR-icM4lmfFMuY13GcX-0edlQndPdQIJ5NxZeXptOhpowaccHSkZo8ow0ISsGFeLH9oU7RFnJASlEuRisYjJqf4jjYiMilngzMFiJn-Hk76yOazofdEVQSDDPgnDagxn37bWoABTp6S6K42RO-ZmqnZ5WEPW8U-uQjT_YS9WUjrXe_EfgIJt1MOiNG21duopl1VckY78fAn7HoMYKTbY0V61uToQOBL04Ku9V0--2UNSaqy9TANXtLjix9V15I56Kw.jpg" alt="photo" loading="lazy"/></div>
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
