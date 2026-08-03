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
<img src="https://cdn4.telesco.pe/file/dY4l4vfx1LLu86P3nolCTfId0RMjPQY1OecpXgfFa8f5Sld6U8_COjqmUDbFvYDMFRP4_qZZUKSY6GnW2WQKeim2Moutqvb31FmqyJx53pmZ2I1wm1AcR9oZbZ5F7Rnqdy4g_tv2nREA3R2i1pY2wzKSnID-U4LRA48Ee2BTNPi4uDRQXBz-zGVupQ7si20tHoVwrpwjnVFvQo6Cbu_yTcMO5q7uGNOxo7W4NNFMtYgh3Jt-6eqcNRIUuc3Fd72F037XHMUduokEQwIQPJvHbJ0iJUxmV0WnectyNnmxIUuiVcZX4CDIHriLsk7tEW_F66lEZpujVttJDeoFpdECKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 04:34:08</div>
<hr>

<div class="tg-post" id="msg-20393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/withyashar/20393" target="_blank">📅 04:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6507572.mp4?token=b7ucFD6H77wnY545sfh4cTNQpLZf1ZTbyiGGFzi_A6AeEBGKC-HgbdW89HjipY4FBt6jSEXe3CPH91yEzfkYCrFvFTwNdx9Re0QsNcgXa6ZSNhppXxd3kjKoY_97WdNvshdHtWEAzUTSyw-A7nkRGWZ-Q-pUqax7R0tTEkv6d7hH5oLyjZzEqtNXkzBzgFpeE25nvY4noDLggrrI7Hu0e3Uw5gcCiz32wKL_b1e_QbrW4Eat88a-z7vyJfAOzJNqAUHmUrbcM1pTjR0J3b4LrpSt94m97QPfHHtGClgCpafXp20WzQF0FbywilgaeK913S1GNa0H3XeEyWF2TtAw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6507572.mp4?token=b7ucFD6H77wnY545sfh4cTNQpLZf1ZTbyiGGFzi_A6AeEBGKC-HgbdW89HjipY4FBt6jSEXe3CPH91yEzfkYCrFvFTwNdx9Re0QsNcgXa6ZSNhppXxd3kjKoY_97WdNvshdHtWEAzUTSyw-A7nkRGWZ-Q-pUqax7R0tTEkv6d7hH5oLyjZzEqtNXkzBzgFpeE25nvY4noDLggrrI7Hu0e3Uw5gcCiz32wKL_b1e_QbrW4Eat88a-z7vyJfAOzJNqAUHmUrbcM1pTjR0J3b4LrpSt94m97QPfHHtGClgCpafXp20WzQF0FbywilgaeK913S1GNa0H3XeEyWF2TtAw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو مارک لوین به ترامپ برای حمله به ایران پیشنهاد میده:
۱. تداوم توقیف دارایی‌های متعلق به ایران
۲. ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
۳. هدف‌گیری مستمر فرماندهان نظامی
۴. حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
۵. هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
۶. حمله به بانک‌ها و مراکز مالی
۷. دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/withyashar/20392" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عمویم پیت هگست
:
وزارت دفاع آمریکا آماده اجرای عملیات بود و همچنان نیز آماده است؛ در سطحی از آمادگی که از زمان جنگ جهانی دوم تاکنون نظیر آن را ندیده‌ایم. ما کاملاً آماده‌ایم و هر زمان لازم باشد، عملیات را آغاز خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/withyashar/20391" target="_blank">📅 03:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز: زمین لرزه‌ای به بزرگی ۵.۴ ریشتر قاهره پایتخت مصر را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/withyashar/20390" target="_blank">📅 03:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/20389" target="_blank">📅 03:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAf0iVIjB2z2vrMwqIt4lxx6Sip4jNsflrUeBIXbbly0rz1sWi0LRQ2KaqP_ag2W9mtXJw6VKuAKthZmHiw0IKhul2CEvBXtEhJJew7lJHLstpbz90tbOiaq3eL7hWxt-538GUA1hMGhyULOLWGkQ6MqGbypMNDRI4sN9wKG5gIZNwBZf3xrCZ5aMwFNOjpNocPzbWfnLY_98K1BcPrl1GP9o0S39p4V53TGk9JOxD15F2t51_vSmxMfmbXNATIJdt8LFe3p9NJJAPyyU92IJ1g_m9BkYNQCGtPEo5I5DsOCk7wcZauDFujQj7vFhxOROXDPSxmHfG-1-35RH7Sv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۸۴$
@WarRoom</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/withyashar/20388" target="_blank">📅 02:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ دم توالت: در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه. امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره @WarRoom</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/20387" target="_blank">📅 02:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فعالیت‌های نظامی قابل توجهی از سوی آمریکا در عربستان سعودی و خلیج فارس مشاهده می‌شود، به طوری که یک پهپاد شیلد ای آی V-BAT در حال پرواز بر فراز تنگه هرمز و یک هواپیمای E-3G Sentry بر فراز عربستان سعودی است. @WarRoom</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/20386" target="_blank">📅 02:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJMmOkshpzVuYT9Q6H6oAVdfT9YHeFfhZlHXzJTcnNANIvh_qXSG4J2iXDzVIP-va_C-gPlcHhC1-OAnkzo5-Lsk59Uth-Ted7xINxY6EpnP7O3nafRS3JHkOL2OdIB44mcXKii5cBB4mC41oGSluA_DOYV9zgrI2RLBbnYsJ1m5yxa8Kiwas2UKbQyZ-9jxzmMle5PtvqeVCJRGrEFl0qIPh3IfzznHPoEZNjxJeFqA5skSBOnHXbZ7e9Rw-rXRbjJNZZYbkUHm3q7cEb_GWSWrrxMWESQ3SwFlyoXv3KPA7RLUfgq_IbUVabp_DfWH_wPt0U4gJfzHeqxcePATEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/20385" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پس از آنکه ترامپ تنش‌ها با ایران را کاهش داد و احتمال توافق پدیدار شد، قیمت نفت بیش از ۶ درصد کاهش یافت همکنون به
۸۶$ رسید
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/20384" target="_blank">📅 02:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=qosZwCNAXtfqQdEIQk99YZ8sXLorvDWEHls5vZd9QQBkBfTdunrXFeeI5IjQ0YKTYjuKi-14Yhm17VEpe3rZ24hR5h0gvCA9qZyeqGD3T2xaQzxnKATN3s9DJMylzDjAMy_ww-UMcwl4Mdko0a4xTwTJ0lBVKCzDCWwHb05M_fjhHXG-1hD4eT-9WzFv98P7brJV_O6ja58Eo0mBDiTCMAct42cL8QbifudymclsD5qfFqAxZADkmqHPsnIBKYBFndWqwRJNgP9bs84PTq7G52V1QmwUUu86ljA9GZYOWfRpHLdy1qd-H_6PP_mcyy0ksElBlt37Nzbaz4gF4puUTTiYP-a1CyXqT6zKYyyOp2fNqAEKIYbuqL1xRkDplb8i_H34fxi71UYxOGv-J8TfSTIMK0UEwIyxncu9sqa3BaYsW11fiX0W7BkAIHAcHRFcvFTtTDPhgtPJxqKpmmAh2gVOwVnluF26NtWQBx7HLtkbm4EWqN5RJUldPU9Sa1w4Q1SHlKLgOfmEkIjh338c51u1Zw9xotTWrjOzDNV7TgO1tCNozeevDD0xAegzRJflAXlhLxPzw1jVQ6C7-ITLEO_nwg-G3tZq3lwK6goXri8jO3r3ohCQnub71EVPL6gu1ZoftRonYzZ9NfC4zTCSlUt3U6AWzVNbSz1IgItggoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=qosZwCNAXtfqQdEIQk99YZ8sXLorvDWEHls5vZd9QQBkBfTdunrXFeeI5IjQ0YKTYjuKi-14Yhm17VEpe3rZ24hR5h0gvCA9qZyeqGD3T2xaQzxnKATN3s9DJMylzDjAMy_ww-UMcwl4Mdko0a4xTwTJ0lBVKCzDCWwHb05M_fjhHXG-1hD4eT-9WzFv98P7brJV_O6ja58Eo0mBDiTCMAct42cL8QbifudymclsD5qfFqAxZADkmqHPsnIBKYBFndWqwRJNgP9bs84PTq7G52V1QmwUUu86ljA9GZYOWfRpHLdy1qd-H_6PP_mcyy0ksElBlt37Nzbaz4gF4puUTTiYP-a1CyXqT6zKYyyOp2fNqAEKIYbuqL1xRkDplb8i_H34fxi71UYxOGv-J8TfSTIMK0UEwIyxncu9sqa3BaYsW11fiX0W7BkAIHAcHRFcvFTtTDPhgtPJxqKpmmAh2gVOwVnluF26NtWQBx7HLtkbm4EWqN5RJUldPU9Sa1w4Q1SHlKLgOfmEkIjh338c51u1Zw9xotTWrjOzDNV7TgO1tCNozeevDD0xAegzRJflAXlhLxPzw1jVQ6C7-ITLEO_nwg-G3tZq3lwK6goXri8jO3r3ohCQnub71EVPL6gu1ZoftRonYzZ9NfC4zTCSlUt3U6AWzVNbSz1IgItggoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من واقعاً دوست دارم این مسیر نتیجه بدهد؛ چون جان افراد زیادی را نجات می‌دهد و از ویرانی و نابودی گسترده جلوگیری می‌کند. صادقانه بگویم، اگر آن اتفاق می‌افتاد، سال‌های بسیار طولانی طول می‌کشید تا بتوانند خسارت‌ها را جبران کنند؛ اگر اصلاً امکان بازسازی وجود داشته باشد. حتی فکر نمی‌کنم بتوانند دوباره آن را بسازند.
@WarRoom</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/20383" target="_blank">📅 02:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای انفجار جدید همین الان در تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/20382" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtsODPuFibJ9jaTxBg1uPJiLxrGBiE4iTFYZgt9bcOgBbnSFaYpTkp-p6ajdIqHLbb0pGZtDIOOykxLvIdI4kGdbAqEs_y-1II8p3oHuFJUp2k5CImGIadqMrtsxi9aJTBqelCzHr2ooHsuD-MCaDl-T_MqKOBnFtjUrBSrpO7hRH8Nh-NuGfuUHEQsOrq-2k4nXzaC-sg1QTWl1tf1HdcRFL-Q8BrCgLfxyUEkIffdoALw5bhlmz2imabMbzQGDaRuorr3Bc6YBt0NsDKYbMUyggYNctGaT3xyS3hF87d9M8A8K7qo6dif9qF6qY2VZJmtvejQ3F5FvNjtPIrMaoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/20381" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/20380" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست. آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/20379" target="_blank">📅 01:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار : شما نمی‌دانید این حملات به کجا منتهی می‌شود. منظورم این است که آیا همسایگان ایران با سیل جمعیتی که به کشورهایشان سرازیر می‌شوند، مواجه خواهند شد؟
ترامپ : یک فاجعه. اتفاقات بد زیادی ممکن است رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/20378" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ در مورد ایران دم توالت:
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/20377" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: ببینیم که آیا می‌توانیم به توافقی برای خلع سلاح هسته‌ای ایران برسیم یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/20376" target="_blank">📅 01:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ دم توالت:
در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه.
امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/20375" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایگان آنها هم همین را گفتند. ما فقط فعلا می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/20374" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که نشان می‌دهد شما در حال عقب‌نشینی نیروهای آمریکایی از کویت و بحرین هستید.
ترامپ: تمایلی به اظهار نظر در این مورد ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/20373" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار: آیا ایران برای رسیدن به توافق، ضرب‌الاجلی تعیین کرده است؟
ترامپ: خواهیم دید. من قصد ندارم به کسی آسیب برسانم.
@WarRoom</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/20372" target="_blank">📅 01:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ درباره ایران دم توالت هواپیما:
گروهی از افراد هستند که امیدوارند من این کار را انجام دهم - به عبارت دیگر، بمباران کنم - و گروه دیگری از افراد هستند که نمی‌خواهند من این کار را انجام دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/20371" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/20369" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU-6N0RbzXnFUgZqPmSniqv5Ua8WinrA6MDSWHk-RDqWd0_BJbMxTYcqFngYpynmynfcEiyGsmZZKhQos1BIcRV8TA3JgPlBoqtgwUfv83Gr11zsFz1XeGzFSZBNIYLIQwQpW_rzgFT-hgsr2DUvLSBxZ461TkaV53peSBoENOrcVIvJqxfCJlihTEdOoTQgYdzLJEZgNhuM7yqNKTE_aGWFdSGZW9p_6dai2hIMZASgTFMZnFw4jhSoOASR_IHXqEzxpMy8207TLeqYaf9tFbdEXzMFhFj5qkixd4bzEe8mYor2bl2J06Ykuju2g0SZv8hE4aa2V6z8_3WzMCq1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس
https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==
کارای اداری و اد استوری رو انجام بدید
کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/20368" target="_blank">📅 00:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تنگه صدا میاد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20367" target="_blank">📅 23:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استوری ۱۸ بهمن ۱۴۰۴ اتاق جنگ با یاشار
۲۱ روز قبل از جنگ ۴۰ روزه !!!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20366" target="_blank">📅 23:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۲ عبری : مقامات اسرائیلی تخمین می‌زنند که ترامپ دوباره موضع خود در قبال ایران را تغییر می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20365" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع اسرائیلی به i24NEWS گفتند: «حمله نظامی آمریکا به ایران هنوز روی میز است و لغو نشده»
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20364" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مقام آمریکایی به تایمز اسرائیل: قرار بود اسرائیل بخشی از حمله به ایران باشد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20363" target="_blank">📅 22:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تیپ ۳۲۸ مریوان : ساعت ۳ بامداد امروز، گروه کورد پژاک با دو فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای ارتش در مرز حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20362" target="_blank">📅 22:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال ۱۴ : انفجاری در اردوگاه تایجی نیروهای آمریکایی-ناتو در نزدیکی بغداد رخ داده است. این انفجار احتمالاً ناشی از افزایش سریع دمای تابستان و انفجار مهمات ذخیره شده بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20361" target="_blank">📅 21:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال ۱۲ عبری از قول منابعی در دستگاه امنیتی درباره لغو حمله آمریکا به ایران: "ما برای چند ساعت در یک وضعیت واقعی از عدم قطعیت قرار داشتیم. رئیس‌جمهور ترامپ ما را در ابهام نگه داشت. حس ما این بود که ما را نادیده گرفته‌اند."
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20360" target="_blank">📅 21:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کان، شبکه خبری عبری:
مقامات اسرائیلی از نارضایتی خود ابراز کردند، چرا که دونالد ترامپ، رئیس‌جمهور آمریکا، برای بار دوم در یک هفته، یک عملیات نظامی برنامه‌ریزی‌شده علیه ایران را لغو کرد. آن‌ها اشاره کردند که این عقب‌نشینی‌های ناگهانی، برنامه‌ریزی‌های نظامی را تضعیف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20359" target="_blank">📅 21:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geMUymXulDoYBSsWmn5VEmHXBXvWeSHwVrtTS1gRG3Z46xbLkvDVS4eUcte2g_kLrcRMvyNA8CFpVkEg8sOzGgimkVAc582bA2ffNfZ_xzlKEmZpuV6N3Tem2a0dOSXaOPOm_Oeuj-psIYidlJK0c8Xk8KQWXoedzjX7pXy_TyhjAUNWTOEeR3RLP088PHqstzov8Fa3JOPMe-fYJsj_-uLBE6Cg3n0w-syZ8MijtuOyLZrL1bLABK9sl9GVMLalu73nyFfN0LGpP-duR3rqg55nFs9BkPFCmqP4IqnQgAT3TpwCj3WD8BLIwp3IVwU-7CVHIQ1v4G_YNl-cTkE8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره Sentinel-2 نشان میدهد ناو هواپیمابر آمریکای لینکلن یا بوش به 200 کیلومتری چابهار رسیده و این فاصله همچنان در حال کم شدن است....
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20358" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKBwcaaDKkNg-t17bNIYBIoCQF_ZAUi3A6eC0JS4u7tyKu27H_WjXZvZ7O3AHKnRnvae5EFBj9gs89lbXY68IqfEvIIixeAILRzdKMgoVZJZ-3u7NetvZIOMMoteTszYQBswT7ZIlodSeYqlt3As8eT40AKB56vObqoVAVSRdR_o3FOfXwXdP91JdGn1T9fZXGs90D-bkhfUDCbccZpjv09BFai3NDcem_nWm9x6IKe_zNaDGeCdn57ZXz_xJ6UdJwxMuuD19mAF37Be3XAZE_IXyGc0qd4qM3kFhzCEIOgGd6zUGzvlllbkd8sJSu7k3N1w87aAfBifenMEJ-X7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در تنگه هرمز مورد اصابت موشک قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20357" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20356" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qb_JU3j2Y-wtfkhf_V06vw1e1UdE3OSOC6iERXy5prTtu64m8YhE_9xp45nzkaEGbbeKI1JrmSZKFZqAEpnJkpzEaBuMKjLjZmUNOLPnED5uQYUoy9e-1s_2txyL5lnoNSLWy8u6N6X_Z-3lHGSOhvMCfdLhuLGL-iYa4CYFZxg8nEbJU2NLZyCsD5h_QIAWAPsJYK663G1ib3eYrsO_0TPIMUgWaJvfKrUj3s-rsu-eDw-2kDyNWUjUygWvT5-uDRGL-4gKd5I0YuqPF5AFJulRTBdBGfAxOv2pVX9wEcejXz6yXwt-3RAa5BT78EiiRBF406UaamlacTrnN3Dygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA7wmaZcxGBmcgVzbULE1bNuZ3s1q0tTWTKHe5tLt0UfS9EU3qjnXhDFy3OakAFgQXddUEGS0qxuz9l3DUQd3hqYcQHG5ok5xOtpU_yBfNrVOg-pI3Mg-kg5Pu-htDi4pw5gaHW23vQyvQTajnWt4sSxir3Xq1Wd7Tn-XJXEvLgxv9miL3zxro1hPz8MYZ_CdVAmYcctBk6BVRJpARoYxL1TRJQhoF7F30J1ZJlJwtW7cAkQBJTdD1X0hEHrLBziRde9dqDTkRvBY0kp55_0T-I5YjqSmBXVIUDLnoiES_fZjk5nVVzb1MF0JeC8sq48Mx_-kasOgyojRNAmWJXjdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جابجایی راکت انداز گراد در حوالی اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20354" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: ترامپ اگر فورا پیشرفتی در مذاکرات و توافق نبینه، میتونه هر لحظه عملیات علیه ایران رو آغاز کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20353" target="_blank">📅 19:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20352" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92517c853f.mp4?token=WQpWgJFUwNeuwPKKQNH22c8RTlXee3ksL845F6vS9OE-FAb6OLTdc-HpTH4L0rKSlwTNnSTuZOcrpuJ0tfNn4mBoAtm1BiMzfZljk8JLLznrWoBv0tJ-5meG5Srr0jUIvfc3Pdr6kWvvoUI6qJHo5gUzEhDsum5E3oOKKTxgocDO-mk3d2AmzQpTI3UKjPEjeYiYRxHQARbOlIiSt3tGREJofts1mQ4A5xkdNxpgZUthpKC4HC9NaS19tumkMexvWTbmBm9Yfh6QL35FxTbwXvF_ZhiFX2Zi7yQaweLGhacKi6_eX7b822PRiVHp2Xs8QpjeETOK4qMjkQNtX1NcxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92517c853f.mp4?token=WQpWgJFUwNeuwPKKQNH22c8RTlXee3ksL845F6vS9OE-FAb6OLTdc-HpTH4L0rKSlwTNnSTuZOcrpuJ0tfNn4mBoAtm1BiMzfZljk8JLLznrWoBv0tJ-5meG5Srr0jUIvfc3Pdr6kWvvoUI6qJHo5gUzEhDsum5E3oOKKTxgocDO-mk3d2AmzQpTI3UKjPEjeYiYRxHQARbOlIiSt3tGREJofts1mQ4A5xkdNxpgZUthpKC4HC9NaS19tumkMexvWTbmBm9Yfh6QL35FxTbwXvF_ZhiFX2Zi7yQaweLGhacKi6_eX7b822PRiVHp2Xs8QpjeETOK4qMjkQNtX1NcxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35C متعلق به نیروی دریایی ایالات متحده، از ناو هواپیمابر آبراهام لینکلن (CVN 72) در حالی که این ناو هواپیمابر از دریای عرب عبور می‌کند و از محاصره ایالات متحده علیه ایران پشتیبانی می‌کند، به پرواز درآمد. تا تاریخ ۲ آگوست، سنتکام ۳۵ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20351" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏وال استریت جورنال: یک مقام ارشد خلیج فارس گفت که برخی از کشورهایمان بر ترامپ فشار وارد می‌کنند تا اقدامات بیشتری علیه ایران انجام دهد. این مقام افزود که ایران تا زمانی که ایالات متحده اقدامات تهاجمی انجام ندهد، مانند کنترل تنگه هرمز و بررسی عملیات زمینی، کوتاه نخواهد آمد.‏
کشورهای خلیج فارس از فقدان یک استراتژی مشخص از سوی ایالات متحده ابراز نارضایتی کرده‌اند. به همین دلیل، متحدان خلیجی خواستار موشک‌های پدافندی بیشتر و تضمین‌هایی از سوی ایالات متحده برای محافظت از کشورهای خلیج فارس در صورت ادامه درگیری‌ها شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20350" target="_blank">📅 18:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۲ : مقامات اسرائیل خودشونم از پست تروث سوشال پرزیدنت ترامپ متوجه لغو عملیات شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20349" target="_blank">📅 18:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه
Axios
در تحلیلی می‌نویسد ترامپ نگران از دست رفتن احتمالی اکثریت جمهوری‌خواهان در انتخابات میان‌دوره‌ای نیست، زیرا معتقد است نفوذش بر حزب جمهوری‌خواه حفظ خواهد شد. این گزارش پیش‌بینی می‌کند ترامپ در دو سال پایانی ریاست‌جمهوری نقش تعیین‌کننده‌ای در انتخابات ۲۰۲۸، هدایت حزب و استفاده از اختیارات ریاست‌جمهوری، از جمله عفو نزدیکانش، خواهد داشت و احتمال تقابل جدی با کنگره بر سر اختیارات نظارتی نیز افزایش می‌یابد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20348" target="_blank">📅 18:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فقط خدا رو ببین
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20346" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شستشوی مغزی Brainwash چگونه انجام میشود بدون آنکه متوجه باشید
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20345" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">میدل ایست نیوز: دقایقی پیش اسرائیل با استفاده از پهپاد چند حمله به بلندی‌های‌ علی الطاهر در جنوب لبنان انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20344" target="_blank">📅 17:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیویورک پست : انقلاب در ایران ممکن است «هر لحظه» رخ دهد؛ رهبران اعتراضات در تلاش برای مسلح شدن هستند!
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20343" target="_blank">📅 16:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صدای انفجار در‌ پارچین کنترل شده است و اعلام شده بود
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20342" target="_blank">📅 15:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">هی میت ، داداش یاشار گلم چطوری من نگاهی به چنل های ۶۰۰-۷۰۰کی حتی ندارم رفتم بالای ده تا چنل میلیونی رو هم چک کردم، نه به اندازه شما ویو دارن نه مطلب و تحلیل مفید ، همشون فیکن!!! فقط یک خواهش دارم به عنوان برادرت در غربت… حرف آدمهای آشغال رو گوش نکن، همینطور برو جلو و همه رو به یک چشم نبین ما تا آخر با شما هستیم یادت نره تبلیغات منفی بهترین تبلیغاته برای شماست چون میان و حقیقت رو میبینند</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20341" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تتر : ۱۹۵،۶۰۰ رکورد جدید تاریخی @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20340" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آژیر خطر  حمله موشکی پهپادی در اردن به صدا در آمد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20339" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فقط همین کامنت را لایک کنید و با نگهداشتن روی آن، اد تو استوری و کارهای اداری دیگر را انجام دهید.
https://www.instagram.com/p/DbiPnCyMgQw/?carousel_share_child_media_id=3954792076531598384_1638317016&comment_id=18015084023866564
ترجمه کامنتم برای بیبی نتانیاهو :
آقای نخست‌وزیر، بی‌بی عزیزِ جانم،
این رژیم فراتر از اصلاح‌پذیری است؛ شما این را بهتر از هر کسی می‌دانید. هرگونه معامله با آن، فقط خون کسانی را که کشته شدند می‌شوید و آینده نسل جوان ایران را قربانی می‌کند. یک عملیات سریع، قدرتمند، غافلگیرکننده و از هر جهت می‌توانست به این موضوع پایان دهد. اگر اقدام قاطع در ۴۰ روز اول انجام می‌شد، رژیم می‌توانست ظرف دو هفته سقوط کند؛ آنها در حال فرار بودند. لطفاً رهبری این کار را خودتان بر عهده بگیرید. شما این واقعیت را بهتر از هر کسی می‌دانید.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20338" target="_blank">📅 14:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رژیم ایران ایلان ماسک را به فهرست اهداف خود اضافه کرده و ادعا می‌کند اطلاعاتی به دست آورده که ثابت می‌کند سیستم‌های پیشرفته ردیابی ماهواره‌ای و شبکه‌های ارتباطی رمزگذاری شده ماسک مستقیماً توسط نیروهای اسرائیلی برای یافتن و از بین بردن آیت‌الله علی خامنه‌ای، رهبر سابق ایران، در جریان حملات هوایی دقیق اوایل امسال مورد استفاده قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20337" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال 12: تا زمان خلع سلاح حماس، اسرائیل حملات خود به غزه را متوقف نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20336" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه،با تکذیب خبر بازگشایی تنگه به نقل از منبع آگاه، در واکنش به گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه، با طرح بازگشایی تنگه هرمز، نوشت: «هیچ توافقی درباره بازگشایی تنگه هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.»
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20335" target="_blank">📅 13:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسانه های رژیم : سرلشگر غلامرضا رضاییان رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و کشته شد
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20334" target="_blank">📅 12:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تتر ۱۸۹،۰۰۰ تومان و همینجور داره میاد  پایین
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20333" target="_blank">📅 11:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میدل ایست آی:ترامپ از اسرائیل خواسته به حملات علیه ایران بپیونده و یه لایه دیگه از فرماندهان و رهبران ایران رو هدف قرار بده
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20331" target="_blank">📅 11:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20330" target="_blank">📅 11:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20329" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سرپرست وزارت دفاع ایران: اظهارات آمریکایی‌ها بخشی از یک جنگ روانی است و ما به هر تهدیدی به عنوان یک تهدید واقعی نگاه می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20328" target="_blank">📅 11:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبر ها رو نگاه نکنید ! حمله ناگهانی خواهد بود !  خواهید دید</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20327" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">همشهری: از مجتبی خامنه ای هیچ صدایی منتشر نمیشه؛ چون آمریکا و اسرائیل از روی صدا هم همه چی رو میفهمن و جاشو پیدا میکنن حتی اگر فیلتر استفاده کند، آنها با معکوس کردن آن، از صدا الگوی تنفس و استرس او را متوجه میشوند. فقط ۲ یا ۳ نفر با مجتبی خامنه ای ارتباط دارن. اون احتمالا توی کوه های قم یا تهران مخفی شده.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20326" target="_blank">📅 11:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود. @WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20325" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد. بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی…</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20324" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد.
بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی خارج می‌شوند. با این حال، عمان درخواست کرده است که تأییدیه رسمی دریافت کند مبنی بر اینکه سپاه پاسداران انقلاب اسلامی ایران از این توافق حمایت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20323" target="_blank">📅 10:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00731102ad.mp4?token=Md7l5VeW3QYTsWMOppp3-ilwMNdNh1pWw_3fIb7uIQusi6Cpy5kq4mybpLZ9H9r9Ks6Eu3yFwHBRcaLzyt3cUtqhmUayLCM5MbV8KRu5qWtb52PA2WDfkcID_PSc8Jdec4VEggatf4Onkg-vFuWU6ev4EXXiqj6bKiw3k4nZUajNj0bduY_BDlOZZLEDM89qFCUEx-0_r7TNn4eQc66tpucZAlDDYl_lgf4U0ghifx4m1m5VKffuHWCs0F2Qrl_E-ZHIY-dpzzhLW5r8Pe9Ss6guVGqldHMEfvnfTTNQfYpkIz_zIOcom1WemS2z1Eb_8-OmHspvZt6C54tQnRDiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00731102ad.mp4?token=Md7l5VeW3QYTsWMOppp3-ilwMNdNh1pWw_3fIb7uIQusi6Cpy5kq4mybpLZ9H9r9Ks6Eu3yFwHBRcaLzyt3cUtqhmUayLCM5MbV8KRu5qWtb52PA2WDfkcID_PSc8Jdec4VEggatf4Onkg-vFuWU6ev4EXXiqj6bKiw3k4nZUajNj0bduY_BDlOZZLEDM89qFCUEx-0_r7TNn4eQc66tpucZAlDDYl_lgf4U0ghifx4m1m5VKffuHWCs0F2Qrl_E-ZHIY-dpzzhLW5r8Pe9Ss6guVGqldHMEfvnfTTNQfYpkIz_zIOcom1WemS2z1Eb_8-OmHspvZt6C54tQnRDiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو وزیر امور خارجه : حکومت ایران باید تغییر کند؛ ممکن است سرنگونی رخ ندهد، اما خود حکومت باید تغییر کند؛ آنها می‌خواهند انقلاب را صادر کنند؛ این موضوع حتماً باید تغییر کند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20322" target="_blank">📅 10:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری NBC به نقل از مقام‌های آمریکایی گزارش داده که روسیه اطلاعات شنود الکترونیکی و (SIGINT) داده‌های هدف‌یابی شامل محل استقرار، مسیر حرکت و الگوی فعالیت ناوها، هواپیماها و سامانه‌های پدافندی آمریکا در خاورمیانه را در اختیار ایران قرار می‌دهد، این همکاری توان سپاه پاسداران برای رصد نیروهای آمریکایی را افزایش داده و دقت موشک‌های بالستیک و پهپادهای انتحاری ایران را بهبود می‌بخشد، مقام‌های آمریکایی این اقدام را بخشی از گسترش روابط نظامی تهران و مسکو می‌دانند که در آن روسیه در ازای دریافت پهپادها و فناوری تولید آنها از ایران، اطلاعات اطلاعاتی، پشتیبانی فضایی و تجربه مقابله با جنگ الکترونیک غرب را به ایران منتقل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20321" target="_blank">📅 10:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روزنامه وابسته به رژیم ایران ، نیویورک تایمز گزارش داد که هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20320" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2oX44AxWBmHo7HQ9xVc1t_aCRnkXfcz9asrCteUsWM4DWnf1_dXdF756Z69lTj-2jWDO9CtIEm5jckD43m9wk9tMrZ6C6B_RbkrBDl92Bo_Zry5H0rOE3zgypRqy_efyURMqUB6PnJ2RAg6ONsDEcuG6qBuigSyXmpfidD5-iQK0F8QiSf9qEakw6RNtN4CZDqpEaAVb-qSJHmB6xbsj5vPRgSQEZjcRwdSwT1oSmbuJbiJ1fMZOLn0MPRMepg7BgYcLlmSlKENSa2IsZXJQ5by-AvVGOo9LsRssXrFYeb7FoZG4mC4Mo0N1lOd0D7pFF8w7V0FTRGqLGpZi8SBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏در جریان مرحله نخست عملیات مرمت دبیرستان تاریخی انوشیروان دادگر تهران، کارشناسان میراث فرهنگی موفق به کشف و نمایان‌سازی یک کتیبه سنگی ارزشمند متعلق به سال ۱۳۲۶ خورشیدی در ایوان جنوبی این بنای تاریخی شدند.
‏این کتیبه اطلاعات ارزشمندی درباره تاریخ ساخت و افتتاح این دبیرستان، یکی از شاخص‌ترین بناهای آموزشی دوره طلایی ایران‌ساز رضا شاه پهلوی ، در خود جای داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20319" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایلان ماسک در حال نشان دادن کارخانه تسلا به بنیامین نتانیاهو، نخست وزیر اسرائیل و همسرش
@WarRoom
هم اکنون نتانیاهو به اسرائیل بازگشته است</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20318" target="_blank">📅 09:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اکسیوس : پیشینه لغو حمله ها ، که همچنین نشان می‌دهد چه کسی (عربستان) این روزها واقعاً بر ترامپ تأثیر می‌گذارد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20317" target="_blank">📅 09:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20316" target="_blank">📅 09:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVYcQM9raKhm18h_zui-YRgobEmEJWQ4FZMgKadzlMCwrWjSZhCYFJZOdteZB151ZsSyU4ZJ35sfHw7SndWMXcrsq1dGKl7GeZ_e424-urPlQuKUs9_CvNZBbMlkmOFX7JSfvG_h4fciJHjQm_WEkUq2CQEbOfZF4rwW9e6pVYBzQXTlsCr8B7YeUvp6EZNWkiR-geEjODS8cW8yDy1PyPeX2hSt6mXMNAG8ah6OyvoJA3uNlZBv-rbonNbGz8cAnGhiG3RlKVKVS13eHYk_81J3e7v5CgknkDMCHOIZSUZQ1fsSooyaBRFBHF7nASEaoQxvhKoaHiTyr36OggstcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث: آمریکا مسلح و مجهز آماده حمله به جمهوری اسلامی ایرانه، با سطح وحشتناک نظامی، قدرت و زوری که از جنگ جهانی دوم به این طرف ندیدیم.
با این حال، ایران و چند تا کشور دیگه خاورمیانه ازمون خواستن حمله رو عقب بندازیم چون چارچوب یه توافق رو قبول کردن، این توافق شامل باز شدن فوری، کامل و تمام‌ و کمال تنگه هرمز میشه و تموم شدن تهدید هسته‌ای ایران.
بر اساس این درخواست، من موافقت کردم برای نفع آینده کل دنیا و همچنین بقای یه ایران موفق و آباد، حمله رو لغو کنم، به شرطی که بتونیم سریع یه معامله ببندیم. کشور اسرائیل هم تو این تعهد با من همراهه. همه دست به کار بشید و این توافق رو نهایی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20315" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فاکس نیوز:رژیم جمهوری اسلامی در واپسین نفس‌های بقا؛ در حالی که آمریکا قلب توان موشکی آن را نشانه گرفته است، سایه فروپاشی بر تهران سنگین‌تر می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20314" target="_blank">📅 09:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو : هر کسی که ما را دوست نداشته باشد، آمریکا را هم دوست ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20313" target="_blank">📅 05:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFbl2j-UlCwXyeeCPHtkMqhtRt9gIwBVSBoUCTYJkS550yOZxBJ2ZudmhHEifMurEOXPihHggzc66fRw77LmY9S-bYt1Jov8WT2dmJFqwuCxYUxdnfS83-4exC-1v1qWJmPBlKadh1jaoemuMBYNPiqMwIbXA5Hs_uiWiiLVHQ9pz-PGluRUPZoutjBbhifIWpXtcyFjSOb49FWl0P8cOijTtsJP-481mywO0RVtXmvBvUE7DoVjC0PpKNPSgMf9Gkd8qJ6xDgilJ0LFuVslfGJkfqJ2Ih_1ug9hyXTJNrHPB9MXR2kVOLN9M2lk0url7-jFaOnsxdeBxvwO6aG-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20312" target="_blank">📅 04:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۴ :
ایران مظنون اصلی حملات سایبری به تأسیسات آب آمریکا؛ رسانه‌ها از احتمال «پرل هاربر مجازی» خبر می‌دهند
حملات سایبری هماهنگ به تأسیسات آب‌رسانی در هفت ایالت آمریکا، نگرانی‌های جدی امنیت ملی را برانگیخته است. در این گزارش ادعا شده اگر نقش ایران به‌طور قطعی ثابت شود، این حملات فراتر از یک حمله سایبری معمولی بوده و مستلزم پاسخ قاطع آمریکا خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20311" target="_blank">📅 04:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">@WarRoom
😂
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20310" target="_blank">📅 03:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آکسیوس: سایر قدرت‌های منطقه‌ای، از جمله پاکستان، ترکیه، امارات متحده عربی و قطر نیز بر ایالات متحده و ایران فشار وارد می‌کنند تا تنش‌ها را کاهش دهند.
واسطه‌های قطری، جلسات جداگانه‌ای با عباس عراقچی، وزیر امور خارجه ایران، استیو ویتکوف، نماینده ویژه آمریکا، و مقامات عمان برگزار کردند تا به توافقی برای بازگشایی تنگه هرمز دست یابند.
این مذاکرات پیشرفت‌هایی داشتند، اگرچه هنوز مشخص نیست که آیا این پیشرفت‌ها برای حل بحران کافی خواهد بود یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20309" target="_blank">📅 03:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20308" target="_blank">📅 03:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen</strong></div>
<div class="tg-text">آره یاشار تو کیش همه میگن هیچ باری دیگه از اون سمت نمیاد قراره کلا دریا تخلیه شه</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20307" target="_blank">📅 03:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مقامات آمریکایی به Axios: ولیعهد سعودی، شاهزاده محمد بن سلمان، روز شنبه با رئیس‌جمهور ترامپ صحبت کرد و نگرانی خود را در مورد برنامه‌هایش برای انجام حملات نظامی گسترده جدید علیه ایران ابراز کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20306" target="_blank">📅 03:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=QqEQM-1nqgTKPObD-6OJ6eHOJBhQuracOpd3PZs6JSnnxLZNJ5aemQuN8Va0Y73yKZ_r30lgeiNF5DX5I_OboE7us458ZyFcXLPVAlpKwhoS5sAXXSzuC4nw0xyw1B4XoVs8eTrcu4v2bmK5bNjrHYUEgb95oDu2few5tI8blXEciCRj_Ac4jS1bPvzxfip7d_bszJdDCoip-Ylhy8Sm2jHOyCZzb2dC75hnatQpMxl7gqdI9oFnlxj6SX_EM1hgxF3GmcOHEdIPe7feZvLSq1xjywQ0bCyVqqQ0382lgKCzygKAaONRLWsBbPW_5gon8Mj_f0DuTSe6xxqJ3j0mCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=QqEQM-1nqgTKPObD-6OJ6eHOJBhQuracOpd3PZs6JSnnxLZNJ5aemQuN8Va0Y73yKZ_r30lgeiNF5DX5I_OboE7us458ZyFcXLPVAlpKwhoS5sAXXSzuC4nw0xyw1B4XoVs8eTrcu4v2bmK5bNjrHYUEgb95oDu2few5tI8blXEciCRj_Ac4jS1bPvzxfip7d_bszJdDCoip-Ylhy8Sm2jHOyCZzb2dC75hnatQpMxl7gqdI9oFnlxj6SX_EM1hgxF3GmcOHEdIPe7feZvLSq1xjywQ0bCyVqqQ0382lgKCzygKAaONRLWsBbPW_5gon8Mj_f0DuTSe6xxqJ3j0mCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20305" target="_blank">📅 03:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قوانین دریایی امروز کشورهای خلیج فارس</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20304" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20303" target="_blank">📅 03:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گویا لایو از سخنرانی قدیمی‌ بوده</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20302" target="_blank">📅 02:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق @WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20294" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی گوشی رو گرفته زنگ زده پاکستان ، ترکیه ، عربستان و … نسبت حملات آمریکا هشدار داده
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20293" target="_blank">📅 01:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">همکنون هواپیماهای جنگنده اسرائیل حمله‌ای را بر مناطق شمال غربی شهر غزه انجام دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20292" target="_blank">📅 01:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز : شاهزاده رضا پهلوی : «این وظیفه یک دولت خارجی نیست که تصمیم بگیرد چه کسی یا چه چیزی باید جایگزین حکومت ایران باشد. این به مردم ایران بستگی دارد.»
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20291" target="_blank">📅 01:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مارک لوین : رژیم ایران بیش از آمریکا یا اسرائیل از قیام مردم خودش می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/withyashar/20290" target="_blank">📅 01:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/withyashar/20289" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیمارستان‌های اسرائیلی وارد حالت بحران و آماده‌باش شده‌اند و پرسنل پزشکی در حالت آماده‌باش قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/withyashar/20288" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">المیادین:اطلاعاتی وجود داره که تایید میکنه گروه های کُرد دارن توی خاک عراق خودشونو آماده میکنن تا از غرب کشور به ایران حمله کنن
@WarRoom</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/withyashar/20287" target="_blank">📅 01:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کان نیوز: نیروی هوایی اسرائیل در آماده باش 100 درصدی جهت حمله به ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/withyashar/20286" target="_blank">📅 01:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۳ اسرائیل : ترامپ تصمیم به حمله گرفته و این حملات انجام می‌شه مگر اینکه ایران لحظه آخر همه‌رو سورپرایز کنه و بیاد پای میز‌مذاکره
@WarRoom</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/withyashar/20285" target="_blank">📅 00:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حساب رسمی X اسرائیل:
ما از امپراتوری‌ها جان سالم به در برده‌ایم. می‌توانیم از بخش نظرات شبکه های مجازی هم جان سالم به در ببریم.
@WarRoom</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/withyashar/20284" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۴ : اسرائیل آلارم خطر نظامی را افزایش داد
مقامات ارزیابی می‌کنند که حمله گسترده ایالات متحده به ایران قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/withyashar/20283" target="_blank">📅 22:27 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
