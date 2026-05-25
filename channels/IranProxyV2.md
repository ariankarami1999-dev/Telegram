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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 137 · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 352 · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 524 · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwm-AwGQxTCTKEmdK81H3GiB042JrRVvQJN4jmEDdWp99ARJjnBVbrsV7R8pS2Ab2f8K8rnxl8LWq54ocAH4BoKaP_FKPQa9RJsJ3Lv71v5AQPDzrFLUHB4nby18wL_RSU1GdK-GRmym2BbZWUOHegvWkKh5bMIMweHXPX0HN-HbG4_gs8lAHk0AsP0InGB1bjrURuUCqgTq-_6GpDClfPIAhFgx4dm4fgVFkh_K2H9UBngCxhot63aggnNMFjApkGsDQpLpUkWEPbV-aQUYoeDOx5qhQWJioaGsaIn1H8Zd0NjIJ98vGfgn4h0UBag_TpUsc71_6ozSKPsmXGJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwyNoiPP4cLzs3KcNKvdP8_CrqvbKaY7ziJPgWSdjSW4Zl0H6OeNJKtQFJe5QcK0lYWWTT2kYz9Fes9uRvuVrAUK2GnvebgVdCyKBwA0EEw0KESy2VhK3Bo8rfxw0fGUJHRs9wCebVaR3pajYi6koXQNbWiGj1Wy-4g5LKLJlNEOpaKnT2qQk18IEAWE2CAEpbvEohcWc64YeEWrifgSLwISEZrBygf1_iN0Zqi-geAjpAIQKycpnlOFuuOozkvpcsNaVwJnKX8I1p6ZKWQwXzfW6NskyUtt8_Abtl8LHN_xoy6gWJ3cjvupdytZ8Z1TdU3h1MFbbF0JjqlZvdTpLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdgrWwkJr0yAoIuUQRYNB24Kaxn6T0QbwkGvesyb73MrbhCMSbcEE8jVfeTLM5zLVQjDD0-TTkL4rS7v1Tpcv89JmZ4L_A-sK0Mv0EZURG4YRH0lH5CMCN5cKcHEJX96nZk3M-NNyq-Ly5R06LJTqb-j1CCjW5rlYYrDP56AMR_bzNF9fRBYtnbE1JqeJlg8_auNDmoCCt4O0f5_jLpxrx3_yUAjxjGsbFA26fiCk6RteoVmopOdfDvEh4SN1BcGgcaWrxr6oHhdC7PqDAt4s3uJGjHLcKXTty1q_VzPgfTS5sALFAo1DzVoLkg2__yfS3rii_Oc5-7DcEo7f1IhlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJKB3ufZ9UV-eiwJAbUw5pbG_qd8cqE_6i4WkeaXckNi1jCYZvTrFc9TlSfcvXl9MYFM6LAv4vdNQ2WEEGqwMa970B7pujCvtYXnpbWziUsdbF9McppnisOYAGVvI4KO2_6IN41OuHCCWHAN6D6UYA_Uhw9w11hS1kyOnpGV0QK3Es5rAqN6vAyjtIxg9_G6dxIgZ6UfPNv9LBaKos_dbIEz48hcWXfosg1TUVkanbEWFHLekNSJPcR4_SdkNV4Ip9rSrglG-fD40ECAfrfwUAgjspn6sS0f33dfEawmg2lAFncf-AZrebmUK9Mr8kg0MCsePXbv6MvBxqoRaFtNew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ9LGKcoHZBNU5SyQDc1jwl42rLsMnPLp8n4SkCk50MzUIjK_QAjXueS-ZtvPJdlSD1g8MESwbAbvlGBHpnYx0ZgU9DN_xrZA7zgXuU4deufutdkRvgW8i4QMttC4nXMljTRV9HhU21lHByaSPYYi-E02C0VWn4hRn_Dq4gFc0aNehgM9UsU0bXd-eA42C175-G4y0WfE9mk_VrQwuuyxptC5Nqe-CY0HNvHBUlBHcRV7F4In1rXBbPGl6Y-vH3T1ycdV-CDdVwScuW3wFX7K_nouTQVHXeKFrbTnmwPltYzW8Kw2i1iF0L6anx5GQe3KfMidyFsltYBS9WU7BiCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKxP_X9SvyvUAJMdYNRzGm3PdM2Kj4lN9WgQ3UuCxfUjnpoFUuoNAbXt7GxKTz9AflLmhYNl07hWkq9cDKsvVNSp5kiKslEd47esUM5gGCWWX67TUyT-gfiP6bS9CL9P2ECkZqJVapSQciTVoAqeun5IYzBUGew1Wv-1yyYEC_KZIXMPPEDpADthuOfkG7KTyr_lfFzsqMyGc7UY2NWyUEdc46A5JIcACnlfGVd3965Xc6ojtOQdFBEo_E9uthFW-jWTRGYytQUCzoMPw_MqSMOsR3Udq_jjnq3nvE6EariQ7YXaU-3tVA_7MmmlxmGx2dRSV0zRWXnWIRPoCeYzeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCQXGBF7NKSE6Ra3mTvytZi-kkXR66Bb9XdrkmEMVrlyoQu1KaEYvUNYRIYJF7THG5h_ESTBsZ_MnJLScGINr_dwXgFGv6oTRu0-NubHyQs4dEH2I42vgELWWxg1KLrAaJ-YUDv8hBQGJ0c_yQtH_LCr91QMcdEhyd1GyaehwW8UCjLcsDOu3YTCZkYYladqkjXsG1ewQhKIZf4e00DFr3FrAc58-9S8WyiylytUBSmgqhjVAStoYwP_feXmGwsDuqo7WN2aOERQi0ZEeAh44q3I7-PuWbGIHChXn1Lc9jtORG9X1kw5_kDfgP7_odz142UNb64MoKyV7W-TmuyLXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5FBwmzDab2bZeVKxU0CVea2ewNLGuVEUFhQ5NfqMo-npEYTqREPgVdLPiXAOLp386nbGM0ToSqJaDR0ejcguj0TyLg5aw-b1Nnpf1nS4-74KuAeYQtVbnQCXQXp1MX0Fj4mlf3f93yKO8GPFRsD1xC6UiVJDwKwkWmGy0hRaMY6wn2KGAGdNqzDbsqbJoJwo9smQ45nKYpA7inogrI5KQIZlcgiJAdci9j6upFsVuDcm-P0MacO7m6Od5g1FYmyuBKa3KinMelUYCTWqBm6w8T6nGEpLOVMRutjU0Fz2erZ_Gv-j3KsGTONRGwZxOEQSlBryYb-yAcBhHnYAhMmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=rGTuFzd4FDnMUw3LoHgdyzATDESa2e59IUm_E7IjdyTxT4vzJWrdsdXlcGwiX4o5HxpN1K5CPaVXuj0piSCsuiqHNO08_cm3onVlaSSyfcYoYCB9rr6PnjACqpcXZzEG5-b5-oMSe5u61E6WjwwUNP0xsF31qr6VgmH9ZjbmZQokQLOH2mgWlqrCzcV_vZBdO4sm_H_w6GUQmSnOb62RrhgCRcjDvsoiT7QTil1BRK4pdluKJr4-x374-upUno4ShKTH2k4pedzFRIGgcjtfYCqu5Fdj0PbAbGPQipEpAqTbLw5ZU1XZgNfkpAgS5qy-_mNaMM1hTUjd3e92V6V8w1dNjJZgQhGuOKxBTkFRZ1TmfBhkDx7fP9t1_JSjlQapBS1g_1R2a-jH6ff-SztDA05LA9a9f_tT3F7b9BztCkm6TtFeEd8fLoYs9lBNgQhq353vbdoNuIO_hd0ltWFt_dzuyGzoNEJ4CpmGfLLmK2IU6cXo_as471LzwLQdMHPP3NGGy30Dmt78KRLojR8AMce2OFT9-T-b-UylOV7AXks99WA2No-aJKIkTKRhFwuPKYVxRxXsbDH7qm_AirirpxfbSIacwq6y3d_7sXSOfZ_mJocettoR2StSe-SuCEPlFP67kbwN71KRO-ff9ta_tKmXMmH6342ait9Ik_YQRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=rGTuFzd4FDnMUw3LoHgdyzATDESa2e59IUm_E7IjdyTxT4vzJWrdsdXlcGwiX4o5HxpN1K5CPaVXuj0piSCsuiqHNO08_cm3onVlaSSyfcYoYCB9rr6PnjACqpcXZzEG5-b5-oMSe5u61E6WjwwUNP0xsF31qr6VgmH9ZjbmZQokQLOH2mgWlqrCzcV_vZBdO4sm_H_w6GUQmSnOb62RrhgCRcjDvsoiT7QTil1BRK4pdluKJr4-x374-upUno4ShKTH2k4pedzFRIGgcjtfYCqu5Fdj0PbAbGPQipEpAqTbLw5ZU1XZgNfkpAgS5qy-_mNaMM1hTUjd3e92V6V8w1dNjJZgQhGuOKxBTkFRZ1TmfBhkDx7fP9t1_JSjlQapBS1g_1R2a-jH6ff-SztDA05LA9a9f_tT3F7b9BztCkm6TtFeEd8fLoYs9lBNgQhq353vbdoNuIO_hd0ltWFt_dzuyGzoNEJ4CpmGfLLmK2IU6cXo_as471LzwLQdMHPP3NGGy30Dmt78KRLojR8AMce2OFT9-T-b-UylOV7AXks99WA2No-aJKIkTKRhFwuPKYVxRxXsbDH7qm_AirirpxfbSIacwq6y3d_7sXSOfZ_mJocettoR2StSe-SuCEPlFP67kbwN71KRO-ff9ta_tKmXMmH6342ait9Ik_YQRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_5ymzG7DHnW94uRq1HAs64mHxr0YT9y7m_Nz_2Ly89H3f8SIrEyOrNxPT6dCrvkYigESE99pG4ybzL5DHgpKyWe7n8w9-_ROd-9KNB21K034aZCzbc5vzPz3jM72EhlYZmc37_7lISsUYMuhcZS3JQX5i8JGROhIjLQTM0LLdpnA5Vpw9RFnqaz6mTY4hufahdJ-_zmluQoGeqmlRA3qZSwanoEd1M0V5JBl3v_QUbURgfZnQsDz0yfLjPsZbDX4Szk3IXVav-56bz2rp6BC7oXHXQgkSeTvvlk2ZyMUoz5CZtTPlovsVOhaRwTlSt0-Rbr8UAs_s-_D8NoJrO-TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLggdzQ-xM7PIpEahASwTwyQalzzKCbMMqPAXmgQPpHpC_SlCVnFVV7GnPPLt_Xt6ZpnVr1zL5q542Ty9BW87JTcMkoo3TV71-PGs7htcBgnQMOD6L8hAm4bFvanKFRH5RfpJ4hy8iKltUiEv9-c3SMGlAZRt-Ust2g9CmjOzm6hMBPt3oNbyA9K6mtaqOBNZ0n1U49nmf2q1LFL4LUZRhZF8bkWYcLfctzPq3nBIMS4ZN74RLaJYZHCq0KBwgsktVFum0tvk-FSIPMmB9JjeKoZFrIEO-F3diYapzoSvHpRCSOrK_yMBG8coPRPFc_VUvzDbDah-xbWZFJE1W8QNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiqME5qRNuqwpAqKb4sMUteqdJfJIlU35-8NgdPIFVzshk8LQ_qIsamnM7uGMbQTvXG41Ls-PEAdmIq2lqwJKE1S9K6Jcv_TcISHgS1Mea1SGpPOVdmHNsHmykdlF4l0erZ3IKnMcnXyczraKR_2lIQY1_UMibDkdStZtv5texyO1SOvWeqF3N04Q3t4HtT7ok52vE7CAvfWhP391cX-cYwHM9NhvppgFebDEvCuyXUAjYQ3AQMxXCho8aoCtFQ81U9MiATet6IOZoPlAwRWODDSBcdSn5DSHv-ROs_sGaJR3jJUVAnci9sdSE_YhP_f3voTJ3P37ctD2GMo_gIrYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=v7tp7gMTfh-tOkttQikOUpCdh_SmsiKQG7ZC__f0npU6pQh-iaO_NoIfKkLUO65WkiNH8NpUBvMe8mXcKxMnjGRchjbZfWaDTmo5qLXWyiLfQiIFcaDSN6tCX7lv_4ctP3HA7-YCxHJW28QYEIw3KhEMZ8vDv4HTUM-XPACS8ZKVSSNYzp9OfAOC7k5bu93U55U9m09gDYP1G6gDZvP0TMK20MIuPshSSZM5weydWurly12R1OHd88z8NF3wZRvndtzbyAIaJrdRhOWLLJtLXViPDF2Iuye8Aj0SwuRA8epCR-WTzCACwAxArWVnjd1qjk4aY2vqeMqFd8Cqm7vltWxvfY5d4vCaAc8WMsmGeQf6uzLeZpViyR2NZ0YDLyGC4xjn83SEg5m8--ZgKlLhKCU6b-b4KobNNZQfPXNZYNi88zxdOLKyYDsvzAb-qavNIHksLBkhR91FRsmT3_lpn8p0VuL0852-U_ZSQRWtet9MW8pqntctUs_ZM2NtOxwGW9FBiZKEqOlTIMmFdApj3gQaLiJ-2IgSolfp23fE0cJIUq8Nf4iBhbd6Rbc0DY3Oc8YfxE2wFsCiIeMFBcYPWRoZPe7fW67ldqkaNRvrSmD1nuHMvZk_VDX7XOPQR9iA7s7HuPf2RxWNUDnKKyyFah5eSoVROXBGbTlua9wybLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=v7tp7gMTfh-tOkttQikOUpCdh_SmsiKQG7ZC__f0npU6pQh-iaO_NoIfKkLUO65WkiNH8NpUBvMe8mXcKxMnjGRchjbZfWaDTmo5qLXWyiLfQiIFcaDSN6tCX7lv_4ctP3HA7-YCxHJW28QYEIw3KhEMZ8vDv4HTUM-XPACS8ZKVSSNYzp9OfAOC7k5bu93U55U9m09gDYP1G6gDZvP0TMK20MIuPshSSZM5weydWurly12R1OHd88z8NF3wZRvndtzbyAIaJrdRhOWLLJtLXViPDF2Iuye8Aj0SwuRA8epCR-WTzCACwAxArWVnjd1qjk4aY2vqeMqFd8Cqm7vltWxvfY5d4vCaAc8WMsmGeQf6uzLeZpViyR2NZ0YDLyGC4xjn83SEg5m8--ZgKlLhKCU6b-b4KobNNZQfPXNZYNi88zxdOLKyYDsvzAb-qavNIHksLBkhR91FRsmT3_lpn8p0VuL0852-U_ZSQRWtet9MW8pqntctUs_ZM2NtOxwGW9FBiZKEqOlTIMmFdApj3gQaLiJ-2IgSolfp23fE0cJIUq8Nf4iBhbd6Rbc0DY3Oc8YfxE2wFsCiIeMFBcYPWRoZPe7fW67ldqkaNRvrSmD1nuHMvZk_VDX7XOPQR9iA7s7HuPf2RxWNUDnKKyyFah5eSoVROXBGbTlua9wybLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=ORWCfb2sUg0dqZAVX3ckz4qlVIlZ4wetiizWn38U0QgxqfHVCHogtG8XuMETvJgOp_BLOADy_OwWe3uEhoqeqQUm5W6JND0ikbbe3Rsq_wl2AouqIiOdxDtuBA1McRob3Tu5H2pSex97CJSfYCGhDk-ppJeyRY3cQOKlwFHMYhH-Dcq0mX-82P4jAspmMNvBW_8q5P1cjNGWRsgwae3i6Eidxg2byUNjBbeAB46dOypPBOWT7dhE6abDe1zjIlhwvBkk9wpHj7TkpzDBMCvw5ywHbcfDntladE0OQfe7ELynQb8EPZkqSgWmqAchrpCljOkAh5nE4kuv574tGywjLzvxTW6MLtqQzyUom903HEb9dM_PlRfbqa2z-xSMgcDsVUfqdzMMPNbC8sQW8DBzug7Ck2Hpaa9NU2zvfT8OTnqC7N5Tx3N0-L9Tghgqrs_V3TLO5EZB223wukAFLUJR78epSN3eA28yCB4i8KRLxGqUjHSGua6YTQgBxM-vuFk4ESs5oSUfoowXi0NMytdn11p-dHk-WgP7P3_0rBsN0ThWCrD6_oLMHha4RuN4zmG1HIexVDiXmskUhgizEWCcaZkmP4QaI03SQllj6dnodz1s8L9tjRMJDj9f4FdjI3xnQ8CDOhQmBx60KgBttuETKWGcjPBYrRR4NZ66RoRXfGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=ORWCfb2sUg0dqZAVX3ckz4qlVIlZ4wetiizWn38U0QgxqfHVCHogtG8XuMETvJgOp_BLOADy_OwWe3uEhoqeqQUm5W6JND0ikbbe3Rsq_wl2AouqIiOdxDtuBA1McRob3Tu5H2pSex97CJSfYCGhDk-ppJeyRY3cQOKlwFHMYhH-Dcq0mX-82P4jAspmMNvBW_8q5P1cjNGWRsgwae3i6Eidxg2byUNjBbeAB46dOypPBOWT7dhE6abDe1zjIlhwvBkk9wpHj7TkpzDBMCvw5ywHbcfDntladE0OQfe7ELynQb8EPZkqSgWmqAchrpCljOkAh5nE4kuv574tGywjLzvxTW6MLtqQzyUom903HEb9dM_PlRfbqa2z-xSMgcDsVUfqdzMMPNbC8sQW8DBzug7Ck2Hpaa9NU2zvfT8OTnqC7N5Tx3N0-L9Tghgqrs_V3TLO5EZB223wukAFLUJR78epSN3eA28yCB4i8KRLxGqUjHSGua6YTQgBxM-vuFk4ESs5oSUfoowXi0NMytdn11p-dHk-WgP7P3_0rBsN0ThWCrD6_oLMHha4RuN4zmG1HIexVDiXmskUhgizEWCcaZkmP4QaI03SQllj6dnodz1s8L9tjRMJDj9f4FdjI3xnQ8CDOhQmBx60KgBttuETKWGcjPBYrRR4NZ66RoRXfGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV6U0sYDwHEqO4IXrnPU7eVLmWUD1aIt2Xufmq8Lm1JXSHH6vEInprIQbER7uO-VAv2-nVe3G25i8CjLbI7LzpM5MOOb1dm47Pon8xRTYTC26-A4I0F4TVtG3HCZoclxK2lqL--dzAmHTpv1maUVCKh7sFjRnhVuuJ5UzhW4X7cgpZtSpB2pM2Ffh4jVpnoq_88I8pJlWqBAMzBU6gfjEpTo1mNj7ShdVN7bBhmPdA0Jvy7rjAva5FLL5fddUoDN_rvO511Z4LI_TEeef8Y2XmeP6YPgk2M6LWJPwdjbXdsUpDuGtgilT-9M9-B1UrIhhLYAyNrc6abwvZ8M01B1fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=nHiwnyCY0rdSPm_ANqdKH8_fo5nuKCMqAQmpAhU2axvaUzIiWbVt3XFE32GU_P2KEsTk7pP_FJRRk_Uz_tb39nL0RiaA6thHkKBgkZTUN1FoElJubP0IkpBgdihrysWZ_ZWqBEUL_TLCAP5r_dR5L8nR63wix06ZETpVCOQJIvXQ5nuoW_FEZNSebatRP1CNVoZzLqyfqm5PEsJlMrv9hG9xRFdJ8WvuiuPm5uQW8bRUBG4aYtIzek5-_tDoIYiTVVbAvGpX4u8NKTo_adnzHPrO7kx9iBBd0qyQ-QTvcF6E1Y-0jp6a7H2qaHByFBspdrT6ERXAttpTX76giLef8jvMHJbVW0DOnJSa9hL4L-n52kejMIusgrwjEV0_vA0YiCtTHpWQ_5X1es2Sw_Y6w1undss7wzkO5OXJ-ntfHgUuPDLBeqC2yJe8v8HHq_fZmWEHWAJmZU-vsbE6-DP5aL3kTyUcGrrp9lGOo8PJUBmNLnnGIC3GiXGfJj7vXcivNMui4F2i_jlH5iOZiVcn2LXiqD_fVXsSgA_clYH7PO16uPkAlvXvEl4rzJzryrRQpVzbrslL0CU2WpNZBf_fcaMIyPxq8PIo_x_Yk1uaNF48roUpURbC_N8Vn7asxLkfIMAVPScXTz3oAMACCWEkg18-Jh9GJW14qBl5nghXsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=nHiwnyCY0rdSPm_ANqdKH8_fo5nuKCMqAQmpAhU2axvaUzIiWbVt3XFE32GU_P2KEsTk7pP_FJRRk_Uz_tb39nL0RiaA6thHkKBgkZTUN1FoElJubP0IkpBgdihrysWZ_ZWqBEUL_TLCAP5r_dR5L8nR63wix06ZETpVCOQJIvXQ5nuoW_FEZNSebatRP1CNVoZzLqyfqm5PEsJlMrv9hG9xRFdJ8WvuiuPm5uQW8bRUBG4aYtIzek5-_tDoIYiTVVbAvGpX4u8NKTo_adnzHPrO7kx9iBBd0qyQ-QTvcF6E1Y-0jp6a7H2qaHByFBspdrT6ERXAttpTX76giLef8jvMHJbVW0DOnJSa9hL4L-n52kejMIusgrwjEV0_vA0YiCtTHpWQ_5X1es2Sw_Y6w1undss7wzkO5OXJ-ntfHgUuPDLBeqC2yJe8v8HHq_fZmWEHWAJmZU-vsbE6-DP5aL3kTyUcGrrp9lGOo8PJUBmNLnnGIC3GiXGfJj7vXcivNMui4F2i_jlH5iOZiVcn2LXiqD_fVXsSgA_clYH7PO16uPkAlvXvEl4rzJzryrRQpVzbrslL0CU2WpNZBf_fcaMIyPxq8PIo_x_Yk1uaNF48roUpURbC_N8Vn7asxLkfIMAVPScXTz3oAMACCWEkg18-Jh9GJW14qBl5nghXsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cirnEH8mCMmEwU8HridDirWhAV3JySElSEOjaJ3DCx3yS9GPPiQ0hseIVXistX75qIAPTLXS2IoNbpBK4WnsZITCToQFKV-7yXRzjvNqYR7V1ZCK_0VsU7Jzu0g6UJiLBEykc5Zwy_7wu5uhkl-BT6kgN-7ckBy0ExhuqtfCnSqTNIXVaaM83k7U0-0RNGK0a8v4u8IRMlMHzlTwZciQjMnlFgQBKnvT95N6bkZyuLXfJrPkkbyuBspziRPbHpvmIfhle8cscUoEOFRXv-xyActJJBLjfVJdaxXPkPWRHyRWE0KmuTV1xIb2BUGKmzJD0EikJmS6oALUvN9W1esepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irlTgp42HP7qSM7hsFUx5u8cgxXjmAsNjF9uxJakctZXLGHQ5bpqn5ZBbGYFY3iDiqNfjADiN95leefxvUJ0a25TYR3R35F6ydD3HSnBAdySEFEMqP4GAaTvnwViQuAOAn8N9n9gR6IobmMupLA-4__l4RkQwU8Ls9fPpI3mdP0l-0oJQ3fDpRdZx-DnseLburCmuVIDAm1x-gcA8hLPNcYYfIsB3YMjjoVni2jHAgDNbN2vmb0fr3gG6DeSid-aNA3A7nkDr6UpvxQW6wWONSz16rZGayrtKqj0PShY5gqxLWxeWLljgUd14qM6KT2sntG_q3v8YJUSp1hONCbZdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=BFAP8PFTfAX_rN6V4NOw8zqLGG70g3Lm4bq390XtNc2Q6ZuMtNg-oA9kZLcoRVmufypF56xvHSQgpNka10JnH2Jsof2-hjDzYccKu2vl5JmPI5Y8LxdRpwHIVPv7rALK8SDMwrJK731vygVbLxKVdKT_7xZQmGBkA1SRssJ-hoWgNh_1Ctp2biteQZ8_kG2NJh5eso2JhcVjPNHHv-AevGECcixBeCkSj000AVf-Pt2HT3ZXg6MsPgEQ-jTaJIEMGfeeNy_BkGmiwS9Zkf1RxuXulVe7v7xISsuLCJDEhBjHxEQMraZ0bfXc9dUhvSRa7ylhhy-475n1gqelo3eufQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=BFAP8PFTfAX_rN6V4NOw8zqLGG70g3Lm4bq390XtNc2Q6ZuMtNg-oA9kZLcoRVmufypF56xvHSQgpNka10JnH2Jsof2-hjDzYccKu2vl5JmPI5Y8LxdRpwHIVPv7rALK8SDMwrJK731vygVbLxKVdKT_7xZQmGBkA1SRssJ-hoWgNh_1Ctp2biteQZ8_kG2NJh5eso2JhcVjPNHHv-AevGECcixBeCkSj000AVf-Pt2HT3ZXg6MsPgEQ-jTaJIEMGfeeNy_BkGmiwS9Zkf1RxuXulVe7v7xISsuLCJDEhBjHxEQMraZ0bfXc9dUhvSRa7ylhhy-475n1gqelo3eufQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ConB69xZhCNm24bQcanWf5Tq-eMbw80X9oNsYXwfXnYgSyH_xByi754BbX8t_yq0TqMwpmJCotdMOauZH1JkI3DlTcm8oq2rPa-vFR91AIqQ6V1oHPzbQ0cY4JZPuKwpNs25AuCNqCfVtFIoSbbanrbHPIj_-otNfyKZUFQWL24EBLNXVv3t4_DBlFFH0dGjhwEmK0S81rcYOew65Hlhb7PyUOAAVSDhhQrGKtNXRqIVZToOV4jBODq8NCJpu8Vpiu5V3bthaGU2zq3O05rYptPLf9AQZpmDFkYK3urUaZ2jodWkr8jI7iP0eUg-Qv-S3N_2kr_g_xMV60My7DZMRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMonKVagyTbEO-Qz191hWEw1AlN82eacSTrs3hio7Bym5BnVLPjxKrMXOKaEWN-r6Rf2jbv-c38fVp1GtrMotN_Hbsy09VggCLHISUAs96R-e2OR9_zApJZ26BL7rpYfQ838b6o1OmFifqXcrCiQWvmja6OWbIvtY8F7fL-5y1aDmXq-f70EDxtLz-lQQqYV-rUHWc4vDNGbE3opBUPRwB24WBj1s31vLZP90K2FwXkaNMpNK7RhAu4geU2VHNxkii7-7fV9PwH_vOkZ396Hqv2dWDwZabIYuE8ZbSyz3KS-HM5eZmrboDkyvqpF73b-2cvv2M9T0iGK6iUVr0Asrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=GAKLwppgssxASASGZbQvOwEvd8FudL-JRuajZh3yfb-NNtimiPQnX6rZo-Y8jaz99TvAFu3asRcgwN0l6bDIXw7wPomj2rOpxDZyjDECZxHubBTfUo9R8QWv4zvLfbqsl7fZ_H8ATuQgVftP04Zw_kCq96P3GHp4m1fqr4ZVx2-aLLLsJ5L0-tjNbuabjoPeUipXrEdSP-1tr_AjzB50_I4Zxa5EIlFNvK-Go2xBzsQRgcK2fzaaaTDZmasCe5Q1uAYTLMM4OiD-Lv-6TkDbNhUTe0mc1v0rAYC274BRFYCk7JWycHJx5JXpTa8NtAwUC306DsnWwZ3pmdAlQMbkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=GAKLwppgssxASASGZbQvOwEvd8FudL-JRuajZh3yfb-NNtimiPQnX6rZo-Y8jaz99TvAFu3asRcgwN0l6bDIXw7wPomj2rOpxDZyjDECZxHubBTfUo9R8QWv4zvLfbqsl7fZ_H8ATuQgVftP04Zw_kCq96P3GHp4m1fqr4ZVx2-aLLLsJ5L0-tjNbuabjoPeUipXrEdSP-1tr_AjzB50_I4Zxa5EIlFNvK-Go2xBzsQRgcK2fzaaaTDZmasCe5Q1uAYTLMM4OiD-Lv-6TkDbNhUTe0mc1v0rAYC274BRFYCk7JWycHJx5JXpTa8NtAwUC306DsnWwZ3pmdAlQMbkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=bzQGlninqqjCHKRG-RNL1LRA-YCA8YOZrfO-dlD_Jdr-iMUanej4390hXv-LnKj3YaiLyCO8tEulAjyqOXQOqMVQENBv0GYFBOKCu4ETeQ7pvMMpavjPh8hGiuTMeRLq1LgDfARI2bMXcO0uzTzy9zR6oBjFZCRVCchfB7BYax-i7ZRMVMx-6BajEAaachT2mSApJiGyNmeQzGL1Mo1jKOXB9KV4oyLPsOxLiMw_6jwH6h_Mg0lrCn52JzYg2NHkkpYU5cAMSen1cnQBj8As7OHXO21cWtmvWujp1ardvdnn_BVV-a7eMhsUfhI2cY4UTsyieNlk5CwqyAWLmAkUzaBJFpNOmcKV4mQSJFTq8H6iC0stNftR9iSUWGmOhamY3aImU2aEZHGsTS2w_CtLYi-GCFWgfm_oQ5-LN_05x22K9fxAn2bYo_dr1vAH7ktl_WgRCQzj-_R5UmYGgJknHf_pqPuDctKfacqlzvAd41ob7yTCF3WFBFi5om9t-z6Ri8wIBVKGrNISV65gdNk5HvTiUtE2L96sffoGnJmGt7o8Ch-UIL4qYJDXf8_ZEaocWx2lWHRBWBXbmTu7DDNt02yl9pg5EUX0E4_8et8zKOL-CFhQ_r349DG3eEbVXPpik3LODopMhAFKWQzSSpsKo68oMX4jF4hEzHcnru8snGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=bzQGlninqqjCHKRG-RNL1LRA-YCA8YOZrfO-dlD_Jdr-iMUanej4390hXv-LnKj3YaiLyCO8tEulAjyqOXQOqMVQENBv0GYFBOKCu4ETeQ7pvMMpavjPh8hGiuTMeRLq1LgDfARI2bMXcO0uzTzy9zR6oBjFZCRVCchfB7BYax-i7ZRMVMx-6BajEAaachT2mSApJiGyNmeQzGL1Mo1jKOXB9KV4oyLPsOxLiMw_6jwH6h_Mg0lrCn52JzYg2NHkkpYU5cAMSen1cnQBj8As7OHXO21cWtmvWujp1ardvdnn_BVV-a7eMhsUfhI2cY4UTsyieNlk5CwqyAWLmAkUzaBJFpNOmcKV4mQSJFTq8H6iC0stNftR9iSUWGmOhamY3aImU2aEZHGsTS2w_CtLYi-GCFWgfm_oQ5-LN_05x22K9fxAn2bYo_dr1vAH7ktl_WgRCQzj-_R5UmYGgJknHf_pqPuDctKfacqlzvAd41ob7yTCF3WFBFi5om9t-z6Ri8wIBVKGrNISV65gdNk5HvTiUtE2L96sffoGnJmGt7o8Ch-UIL4qYJDXf8_ZEaocWx2lWHRBWBXbmTu7DDNt02yl9pg5EUX0E4_8et8zKOL-CFhQ_r349DG3eEbVXPpik3LODopMhAFKWQzSSpsKo68oMX4jF4hEzHcnru8snGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vdluu7RRhDWH5fJDn0RMI5jbVE0dB5J7mc1-j2AMWqsfr6LhsqR3BM1jeBfzDFDGXcKsXXhYNSF__QKM_bA68-WNXYexlF7zrDA9fbhvPBWQor6T1ZPgpJT2aFeqwaavzAwK6AmGC8BjlCm14FMk79qYnjk6QYCQsfgVVpQBwsYaHh5lYzaIVpAXgYwxKVGSgayRFzZGNT1--9yqzy3Lx-DrEHEEKqDquaDaAqb3JDe4mj3IEGJd6hcT_b_Gwq652PV-iMjUbGoOasxw2V0cZsJ1Yzo_bZWf3IJD1p9hn_Cuu1dY_7QumFxNQDti8pz0hLHzt4CcFVzUhwFy2BSR7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkMuyPc8U9hPzehKkJbjHXso1BF52_CJR1iFDHD1A1pfOD1FD0juQmvP5TBqkfGY6kh89EUEZTJb8ngzu6PAWaYReG5_-g15hCORHcRf8vqXcY9VUrt7HEkqLFF36xSUVPpGosZ3NriwqzxdINZMVIVz55p-K9jEWnjUpO0VBe4mxiHUBmC20BsQ_cBW828s5OLHf32fz4mwUOMjXbCglxQEweWS_UaRqN6K_HFV6jygaJDo0uR__CPkDHmaUYpZUgRGH7dB29rEoU6NQ0BKML1QXtuX7K_FvL--mKUzpVPJoPYCWvVBUaSrwGvGehqA8GcGvJzPlyk1YGcUwhBXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJkf7h1wil4ZMDLtdmQ9CLw2FCANZHLfeGDYKElGoiW-iyOBoPBjQ0A0q_qzlFRklVubwaTSnAia0qy5KNn5el1r0Ktj2cgK-V1hymNVsYYqtUF6_wU9mGXq7wOfipcYyW6eYHm4YHsDu2j1zHYHilWdkYzPXdhmuy7nc6CyxEIvnBtikfIc2EBLJhxd0RUVrp6awPfGgFJ7eKCOMhsbgmbEap7U8kNnVwmfk7lyktGZXnrVhZGtdJNTN8DTZt6JTilFFIsLDrIe7kfVZpdZgEl_uHElRpvJjPPsd_vQUpwwa027GWN7Vkrz6XzLMUIgzjovFefCJr-fZZzYHt7qBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=i_zG2mBC0D-WH0qHIwObp_aGAuQDWPW_knFxnu1ATllOX_NuzXy8_GkEuN8CH3Jc5NUUIiPt27z-6SWM0Yz_eFzTmjMFbpIq3UxKcHn22sdok56PHH88tbC0v3_H5sGX1VqmUcdaFieczmO3sgOL5LMj42hGC8wA3sAHDo7JpPn49pY26Bk3hFPxOYZzpoUEgJHis2_T21dagPDKOd80wzbov65IZ2uV_Eyof6Rj7LCCG18P7Sowc12tNz44Bvb_Av1_oG6TsoJiegqauIo2bcP5hPfQWyTaB9Vrbcu9k4yxQafJK-yrzBaJ-GNuiJHbI1dXQtKwjMRWUuCCqaevr5uhi6dY3PyfsqBvwiVCU-M-bv47SIgDtSWUWDttJqQlGl-QJgaTy-B5aiGt-YNni9GBzEDI4ZOD53X7lPsYa7Cm3Hq-J6nXlBPaZoi9shuGbIaaKLaHa6VAmE_k75woE68bVOgcWQrbEPr60gQsNC0XLU0HMKPtukFU_bl8yI8Z_6fkCwo017z_0UQLbY4lZpbuxzwYDdGgXmqUqJSmsYtbRn5E-4ovdf7-WElOlpOlXFjfP39TZooY1tP5D5ly3da1NxvlyrErJJbSaRvDNuYRdCX0EPtiiRjejWGNaEmH8jeH4GgjhtxnVQnaZMjX8ma_9BvtVfFv0n6oUNKQ_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=i_zG2mBC0D-WH0qHIwObp_aGAuQDWPW_knFxnu1ATllOX_NuzXy8_GkEuN8CH3Jc5NUUIiPt27z-6SWM0Yz_eFzTmjMFbpIq3UxKcHn22sdok56PHH88tbC0v3_H5sGX1VqmUcdaFieczmO3sgOL5LMj42hGC8wA3sAHDo7JpPn49pY26Bk3hFPxOYZzpoUEgJHis2_T21dagPDKOd80wzbov65IZ2uV_Eyof6Rj7LCCG18P7Sowc12tNz44Bvb_Av1_oG6TsoJiegqauIo2bcP5hPfQWyTaB9Vrbcu9k4yxQafJK-yrzBaJ-GNuiJHbI1dXQtKwjMRWUuCCqaevr5uhi6dY3PyfsqBvwiVCU-M-bv47SIgDtSWUWDttJqQlGl-QJgaTy-B5aiGt-YNni9GBzEDI4ZOD53X7lPsYa7Cm3Hq-J6nXlBPaZoi9shuGbIaaKLaHa6VAmE_k75woE68bVOgcWQrbEPr60gQsNC0XLU0HMKPtukFU_bl8yI8Z_6fkCwo017z_0UQLbY4lZpbuxzwYDdGgXmqUqJSmsYtbRn5E-4ovdf7-WElOlpOlXFjfP39TZooY1tP5D5ly3da1NxvlyrErJJbSaRvDNuYRdCX0EPtiiRjejWGNaEmH8jeH4GgjhtxnVQnaZMjX8ma_9BvtVfFv0n6oUNKQ_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgDJnSOeudtEXSY5R_ZtBsTerxnHObW1ymfZvyk5NiFpRd7GAUDY6s-U1fYsSFsT3jEYxfZ0B4U_onWUH01Tvrq2eiok3CqbvwcbtXiVXU0k17vIkfUkxqYgX3l0-zT3rlF_CjJVQCmeVXgxPpvkKjIdvcnFzlxgBOh5QJ0YLP-ciX4hRk40AO4cAKkdUcVSWlBFT8B0MhiOAIb4wxOq8j4ruV_JtEMtaw2crH3MGkJOoL3j8Ha612zP9o3VrAAEq0-dBu-8u5cWgnczeXmSgKXH2t-ZcNMiw6T9wwxxnwKIp2SfxmqGgCukeL-epfBvP0QHJIXvxi3FJKruNXWbN6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBgDJnSOeudtEXSY5R_ZtBsTerxnHObW1ymfZvyk5NiFpRd7GAUDY6s-U1fYsSFsT3jEYxfZ0B4U_onWUH01Tvrq2eiok3CqbvwcbtXiVXU0k17vIkfUkxqYgX3l0-zT3rlF_CjJVQCmeVXgxPpvkKjIdvcnFzlxgBOh5QJ0YLP-ciX4hRk40AO4cAKkdUcVSWlBFT8B0MhiOAIb4wxOq8j4ruV_JtEMtaw2crH3MGkJOoL3j8Ha612zP9o3VrAAEq0-dBu-8u5cWgnczeXmSgKXH2t-ZcNMiw6T9wwxxnwKIp2SfxmqGgCukeL-epfBvP0QHJIXvxi3FJKruNXWbN6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V5VUDlGjZKBwbDMgF19t1OQpr-af-5W3QuOuog2-jr1F6-R_sj6fPBBsnryXqrhMtd3PeQiW2pIi4geuWlDEawo1GAWdLzDWNz4VC2A-cLPj8DA2fOPLCCwK2OfKjTMCE7YG1OpzbV290OkvhiTpzbw-sa_kiPzMbPW2aUoRs6IACCSWdKxEjFZpXn-4qD2M9zJmnxihM2GtDGl3jXXVrWupYqgQFMI1Jf9jt0CHgZX3epVEsQuxx3PV-ZJk3G9vHIeM3seCtCOuZ4CS0R4AJkhUrPHTB5DkiqhcMI5GImF9yHAX0zLi0qhbaZDtGOmTGONdKUnd4HnUgSN1fdR_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6xiSenwzD9ts7UxO_3x4hmklkqjkqJw4kOnnY7kpLWg8ZOoIZXd-iwAYZWzZlrVAVEN2XyFMyQl0BVE2gpL522YK8VewDs0CnBnJHdTsojRkZir_EZw_0R2jbQxlEiARVgFB6e34B5nXJG9ipVnYvfCfqmviDXA_nRWtbOiFFEhvdjh76eYJk8mRRTxJsy81EGSSLRbqX0rhSHSZEnZWGlBz4vO7UpHCCR1qsv8ua-vhpEWc7dRJww4NZA3mJmYrndICBSzMK6m57f_mbdX8jI27N3jYiqg2Wa72WtjjkLsfSUk4DFSAmCE9QX5jCPYd3b3PGgrx9lM-3YvYbI0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
