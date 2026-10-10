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
<img src="https://cdn4.telesco.pe/file/YHQZN0z1707El812QT5YjPaelTgvKnaV7QdqERTlfoZ22OW5IGIvK4TyHKWzy0OA-6jCJ9SGjiGTCFCc_9HT0qbYEj7ep7jInbB39dCQAQPLe9xYmxC9E8Mu56BG-WYa-DYgq-Jvt7t1pOYaHoVdp8xwEh9Y6lFSLCjIT5JYpHVXexTSYic-YXxV1VOCa3xQfHfmUXAsRZA_gA7SPx9GVVQjpJ7DWE4e7dnoZw3lVBq4KSiFgi5kZYNNpSOo5XWc1dpXqOj44DPDNLIsZ64QD-dtmaCpeoC0EwBSUv0zHZgO67hxf9RUw2EEEUP0YLN4cQNolsDC9gu--aNb1NjAHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-697287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXuQapPAx684hFTQi6fZ6y-avFT4QAZvQdY2oggK7z8tOi1pLDNGspnik8vtf6bX-9_yDAWq13tRNJwOf_YEZHX4T_RDNbemj9Ght5rQb7V1z-f6P8BoILEuPvV8JsbzbmdFH-xeFrjPDnGEyTI9LPgcKgBe3_Py9I0Uz-UPx1uyIHTBkDQvAP9op99RVEm75-RgSRwTjzQU7c2M-tFFVOQMBcy9N-BYcxqBpifgNNCrsbjgklyc_NOeFoCJ5OvFtqUU3_vzRM8nmZLGn4v6btXMQe08I_--ep-NmAR0nGGt2QWdXy2auqLYyrPTh-nncG-n0jsJYeyJ5TkZz-gMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/697287" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grNgkiPGR3NU-61Q5aXJK0G71rFSHRvkmHMy2n6SzXZKbnXI0jrqvLhRkExDvCo2wocJb-QxmxO2l0An-Cbu_4wCm73jHVLYG7kGARtY5AfmJmE8NKus6OihR02rKdUE2DppMD7LBAkJklWt9sk50coObTE9oG21xcQrOg1Vz6GfPKAlviQbsvpFdf35TYbTWIHbDNsXR0-UYXJyWF105g1D6BC7Aav1iycyp24Y9ICbkoRZhJN6ooVZbuRhdiTNPhwayYwGiPmVfhviR25ja27mQblWh6WzOy0u6J5AplhxZr_FIQ7QHxfMc9fFGDeclgspDb4Rzf1N6TIHbHgsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/697286" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b7e6e16e.mp4?token=d7Y4m5HBUKmx1MYUx6QSuCuDQxWLiksFqKYSaY6ZS6LGoWfpvhYtj60eM8ea3G1IsPaoMmSpisFY3Oa3bwS42xDuZIplzKgF2lP0tlb-G9Vnp_vleVnbd8CcW4IWuDeUHUYUu0L5GTMxfvnrz-xw8f3Tqqg3TscH47X0lKbwv_0i3Xvz3WyLB1Nza2_tQTybsjEJbR6OjTEZQOETTC4tcDfWWY8MPWOfblVZvqVajJF8tyYDAU3JAYlhn9dRtdn_Nt_jGHFv07A-IBOSySaj1OlCgDJlCfauOToLPLXOlEsGDZLoAH3zxhdNVeJu0Nt1dPYbmMHfvw7WeBTrVn_cUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b7e6e16e.mp4?token=d7Y4m5HBUKmx1MYUx6QSuCuDQxWLiksFqKYSaY6ZS6LGoWfpvhYtj60eM8ea3G1IsPaoMmSpisFY3Oa3bwS42xDuZIplzKgF2lP0tlb-G9Vnp_vleVnbd8CcW4IWuDeUHUYUu0L5GTMxfvnrz-xw8f3Tqqg3TscH47X0lKbwv_0i3Xvz3WyLB1Nza2_tQTybsjEJbR6OjTEZQOETTC4tcDfWWY8MPWOfblVZvqVajJF8tyYDAU3JAYlhn9dRtdn_Nt_jGHFv07A-IBOSySaj1OlCgDJlCfauOToLPLXOlEsGDZLoAH3zxhdNVeJu0Nt1dPYbmMHfvw7WeBTrVn_cUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند کاربردی رب‌پزی بدون کثیف‌کاری!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/697285" target="_blank">📅 20:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من همین الان از حمله به فرودگاه ریاض مطلع شدم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/697284" target="_blank">📅 20:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349692f31d.mp4?token=ulsTVNaZXUbr98roUfbtH1out3TskY4sWl0SFZaZmov8wu_e-mkWeSlVwnO1iiDOlg2HSWnrxVP5gBdmb_6RnAuMS9vOltz2AA-kqGEhumD8ULW89xxYCJz_aYd6NkHmYzqb6XRgRl57fuG9BgHKMUr0Ki9e8hacOI5bAx6BrtT5oKUYLYajBC6-XcHYUjejocv6cZlMJ5yrSB8RNM3i-OY5l0LOS2PEE1GYLKsDFbn4eBlrzURgFBM5MbH6p4jwhL2QYCT8UWyFyOvUxLkju7EM5yWXAO8e_QDnWiGmxkLB_PMrZ3EvhwwqW2WcSxlVEnG7_kHUpb-TG25VO-uVvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349692f31d.mp4?token=ulsTVNaZXUbr98roUfbtH1out3TskY4sWl0SFZaZmov8wu_e-mkWeSlVwnO1iiDOlg2HSWnrxVP5gBdmb_6RnAuMS9vOltz2AA-kqGEhumD8ULW89xxYCJz_aYd6NkHmYzqb6XRgRl57fuG9BgHKMUr0Ki9e8hacOI5bAx6BrtT5oKUYLYajBC6-XcHYUjejocv6cZlMJ5yrSB8RNM3i-OY5l0LOS2PEE1GYLKsDFbn4eBlrzURgFBM5MbH6p4jwhL2QYCT8UWyFyOvUxLkju7EM5yWXAO8e_QDnWiGmxkLB_PMrZ3EvhwwqW2WcSxlVEnG7_kHUpb-TG25VO-uVvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از زخمی شدن ۴۵ نفر در حمله موشکی انصار الله یمن به فرودگاه بین‌المللی ملک خالد در ریاض پایتخت عربستان سعودی خبر دادند/ جماران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/697283" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133220ceea.mp4?token=qWQYAzA2fx4YgvIYiulSE6sjqr03CWTdYwWu__7PijF7mo1d-L9EnaBEZMYtV0mq35EutcM8swK0FanHwrpAOHDPZSFo_KFAnxTcmq6iosVKgHRbUuXKzM4mFPd-8JiaVMrCfSvTA8pBhjXRc_DEZRiiCXPNasPAHxTCqUf9M57l6b443KIDBhHc9W5yLQHqm06sNLznoH0rCGGQXwH7vJCys5RCVlUHPLzLp2uZ4ttoFtG5QaicrxoUGdncSB1EUMrEQwazD-W726pp1jLqrl4xZJvNC3Ht-lRfMp8mnzQ-MNXheo3ZCHk6FURCJDGnZyLG_RnsPYqJTFQVIprD5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133220ceea.mp4?token=qWQYAzA2fx4YgvIYiulSE6sjqr03CWTdYwWu__7PijF7mo1d-L9EnaBEZMYtV0mq35EutcM8swK0FanHwrpAOHDPZSFo_KFAnxTcmq6iosVKgHRbUuXKzM4mFPd-8JiaVMrCfSvTA8pBhjXRc_DEZRiiCXPNasPAHxTCqUf9M57l6b443KIDBhHc9W5yLQHqm06sNLznoH0rCGGQXwH7vJCys5RCVlUHPLzLp2uZ4ttoFtG5QaicrxoUGdncSB1EUMrEQwazD-W726pp1jLqrl4xZJvNC3Ht-lRfMp8mnzQ-MNXheo3ZCHk6FURCJDGnZyLG_RnsPYqJTFQVIprD5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره اوکراین: فکر می‌کنم وقت آن رسیده است که اوکراین رئیس‌جمهور جدیدی داشته باشد!
🔹
زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/697282" target="_blank">📅 20:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5100424818.mp4?token=VS5zZugJ6Fa7ltl2GoHF6v7sElrSTxQkXVs4iFv8CSN8vDrS3P06dtBoa2ouosK9UCLrUEm7imckBcg_kgYyia3BtUbcqmz1RslI1HjjgerfuQhm5p0PGlECnNGzet9qJvB3sGcln8UCBiyRnyZoLeZBFF8U-jUOhN2m41ZckEpzQ4TfTie3ujGccJk8kkjQT93gKTszvRp0EX8wEqux9iepIJNTYOwAzhAUPQbXeshupQz1W8_EXdf95F_rcBWEYu4BlbbMZPwXN8u3qSM_DD59vq7u8691Vy0ye4KPn-jSZSJLHhan7Eqz0H1akWTUuCjJlQp-JbcQ9J59LkHpcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5100424818.mp4?token=VS5zZugJ6Fa7ltl2GoHF6v7sElrSTxQkXVs4iFv8CSN8vDrS3P06dtBoa2ouosK9UCLrUEm7imckBcg_kgYyia3BtUbcqmz1RslI1HjjgerfuQhm5p0PGlECnNGzet9qJvB3sGcln8UCBiyRnyZoLeZBFF8U-jUOhN2m41ZckEpzQ4TfTie3ujGccJk8kkjQT93gKTszvRp0EX8wEqux9iepIJNTYOwAzhAUPQbXeshupQz1W8_EXdf95F_rcBWEYu4BlbbMZPwXN8u3qSM_DD59vq7u8691Vy0ye4KPn-jSZSJLHhan7Eqz0H1akWTUuCjJlQp-JbcQ9J59LkHpcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه: سوپرنفتکش متخلف در تنگه هرمز با مین برخورد و در آتش می‌سوزد
🔹
عاقبت هر نفتکش متخلفی که قوانین تنگه هرمز را نادیده بگیرد، همین است.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/697281" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ترامپ حکم اعدام یک نظامی آمریکایی را از طریق تیرباران امضا کرد
🔹
نضال حسن در ۵ نوامبر ۲۰۰۹ در پایگاه فورت هود تگزاس به سمت نظامیان آمریکایی تیراندازی کرد و ۱۳ نظامی را کشت و ۳۲ نفر را زخمی کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/697280" target="_blank">📅 20:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f9a72d14.mp4?token=nP0pkMdTjV8VSH3_mD-oSyrZhemVmz4sr2pvTwtwGK-7d2YEx89eDCwiLU7_S84imYSuXKy_-tq7ByERC6nBihia8Vnul5Rc_T5wTiLoXexKbh45bTSwyepFPVrGbE8bvt9SbCGz7gLZGNcGpX9AjOyhc4XHwugnTqsRG0Osnk_ydiYcNolS4wHMg46-cHRCWwIZ1v5J9rj2w4PGXg4TiuDmMso5wL7lAGryP7s3DRxXFLYBukj0rIHIemhCOXNDk3cMDIxSsvLUZU6xNThFfu6_Nw3lMitlrJ9cU1BEjbseO6LyX2-kFHbC81IfJftM9151Zc6KKHulTCWmhSV1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f9a72d14.mp4?token=nP0pkMdTjV8VSH3_mD-oSyrZhemVmz4sr2pvTwtwGK-7d2YEx89eDCwiLU7_S84imYSuXKy_-tq7ByERC6nBihia8Vnul5Rc_T5wTiLoXexKbh45bTSwyepFPVrGbE8bvt9SbCGz7gLZGNcGpX9AjOyhc4XHwugnTqsRG0Osnk_ydiYcNolS4wHMg46-cHRCWwIZ1v5J9rj2w4PGXg4TiuDmMso5wL7lAGryP7s3DRxXFLYBukj0rIHIemhCOXNDk3cMDIxSsvLUZU6xNThFfu6_Nw3lMitlrJ9cU1BEjbseO6LyX2-kFHbC81IfJftM9151Zc6KKHulTCWmhSV1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش صحیح نجات نوزاد از خفگی را یاد بگیریم
🔹
در لحظاتی که نوزاد به دلیل پریدن جسم خارجی در گلو دچار انسداد راه هوایی شده و کبود می‌شود، هر حرکت اشتباهی می‌تواند فاجعه‌بار باشد. هرگز دست خود را کورکورانه وارد دهان نوزاد نکنید!/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/697279" target="_blank">📅 20:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای
ترامپ جنایتکار: من همین الان از حمله به فرودگاه ریاض مطلع شدم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/697278" target="_blank">📅 20:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0708ab3095.mp4?token=qB1rwn2Ht0_TQ4S0toiJezoyfs1sibLyfSiu4YC0x2vr_cp1ZcA2df0gp5WU3v--7fNTwGHRESLKedbd25s79wW75ykn7VMmR51SpuUvAA2d_xJLEna-ZVzdw8aXRABTqqLxuSEL_qw61h3esKIy9h2UpkPg-x_qFWdLM5dIlRwoZKXJV8Ta1ND3ujKlKj4aqJEjhoqvOnSXgiyvI53cKfZj8Bbk3Gpl6L7OwTUHvb1sJzG9SChph5ZR5PatyWXce35h28iBT__YknFJShQ32DNok9SG3X9S3KutQfHkh3xUyoNsuRsbB1dyKsFpIrjII-U6OXhp9DtQvuYIRZqgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0708ab3095.mp4?token=qB1rwn2Ht0_TQ4S0toiJezoyfs1sibLyfSiu4YC0x2vr_cp1ZcA2df0gp5WU3v--7fNTwGHRESLKedbd25s79wW75ykn7VMmR51SpuUvAA2d_xJLEna-ZVzdw8aXRABTqqLxuSEL_qw61h3esKIy9h2UpkPg-x_qFWdLM5dIlRwoZKXJV8Ta1ND3ujKlKj4aqJEjhoqvOnSXgiyvI53cKfZj8Bbk3Gpl6L7OwTUHvb1sJzG9SChph5ZR5PatyWXce35h28iBT__YknFJShQ32DNok9SG3X9S3KutQfHkh3xUyoNsuRsbB1dyKsFpIrjII-U6OXhp9DtQvuYIRZqgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکسیوس: تصمیم ترامپ برای لغو تحریم‌ها علیه صادرات گازوئیل روسیه، اوکراین و دولت‌های اروپایی را شوکه کرده و باعث ایجاد یک بحران جدید بین ایالات متحده و متحدان غربی شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/697277" target="_blank">📅 20:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f25bd7935.mp4?token=dvLNkHh3rvxWZoOARnG6zr4O4IUNJ6t_NowXNssEMZkzfKd9UsScl3E9SWaWUuBQ-H2r3n1B6sCMK_f9cMCXug20ikWGNEJWOkQ89pH_ZKtRn_MHt61M489USlLf-4lKDc3Us9q--TzphN20gjJkEW1ylIb1Wh82pWZKrl3zvjPKdPxDGrb-KbQMgNT1_0WbcmJJBZRfs8q1I7P76-TEHv94ccjKG1SgV0JD5FJXfViOZXVxiBZR8W_nADHpE-iR5E57MvYmGUmy2E153CsTR5LsEmPNZUlqJBDZ5zIkWv0TNPdqOSKhSm61UWrmth-CHh6aXLdlUBf3ugvnlSfRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f25bd7935.mp4?token=dvLNkHh3rvxWZoOARnG6zr4O4IUNJ6t_NowXNssEMZkzfKd9UsScl3E9SWaWUuBQ-H2r3n1B6sCMK_f9cMCXug20ikWGNEJWOkQ89pH_ZKtRn_MHt61M489USlLf-4lKDc3Us9q--TzphN20gjJkEW1ylIb1Wh82pWZKrl3zvjPKdPxDGrb-KbQMgNT1_0WbcmJJBZRfs8q1I7P76-TEHv94ccjKG1SgV0JD5FJXfViOZXVxiBZR8W_nADHpE-iR5E57MvYmGUmy2E153CsTR5LsEmPNZUlqJBDZ5zIkWv0TNPdqOSKhSm61UWrmth-CHh6aXLdlUBf3ugvnlSfRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات سعودی به طور فزاینده‌ای نگران هستند که ادامه حملات یمن می‌تواند به اقتصاد آسیب برساند، گردشگری و سفرهای تجاری را مختل کند و ذخایر محدود سیستم‌های دفاعی موشکی را تحت فشار قرار دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/697276" target="_blank">📅 20:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUs1tgBmXkZO4wAlVlaSweEmBwFsXF4otnriIySMj_pdFsaCpAqs6XbeWkcjqPnigYroKijP0G1cnz6j_BsXH7c0lNUlNU1HaxnZPpxVEZ3G0pQtd4EZIb6YM8GJYZLftJo1qebQ-ByzPBathJsNNo4QcALr3UE4cmoUdjvCMboVN4UpEK0cvyLzFguGnQsVII6RCjA62YIPvqbPPE_STsfcW_3q5OXAi7bpE_-vXIlVNR45Md51VOfFV_PpjJ0h0OmtXczpju_cQNZ6s1i-Lm1ix7zwkuhLggfYeo0w5efK6S5U2fUMminUsDbXadd2JPMkU9CnMgfKS3q7wn65rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریدور عمانی هرمز تخلیه شد
🔹
تصاویر ماهواره‌ای از تخلیه کامل بخش عمانی تنگه هرمز خبر می‌دهد؛ ایران در دو هفته اخیر، بیش از ۲۰ نفتکش متخلف را هدف قرار داده یا با هشدار از عبور منصرف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/697275" target="_blank">📅 20:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPHFh6Qhuy9tDcTniphNDsncaPJzw9gJUkwqnAjyWSPXLgK90tVRQDbz7HJSnA9mfPK2bRfrhpP-gg4EYun-FqiO_QMjTKWfRZW8hNEubPsgMfi4QPKZLdWuJ10ULxB097FIWLDuFBNCYqANtzhU0lFi-IXW6IhCdUdvqKjM4J22rsZIrSFK7kDJJRbgpEZuhK_XR3rvqYG19cXkIbWC7WPUMrQpr8TVje-RKrQG6Vmg6sfH87FK5UxxU3MQ8BLFqjzG_5U9jqE3pJDh2Sc9hrDn5V_Qrnnw7qoh6sLluOdpkI-CwHmrMVktXy_2DNLz-tFqcSyXEEmv2M34T7avXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و اسرائیل چه زمانی به ایران حمله می‌کنند؟/ حرف نتانیاهو به کرسی می‌نشیند یا ترامپ؟
🔹
آنچه این دور از گمانه‌زنی‌ها را از دفعات قبل متمایز می‌کند، وجود یک شکاف آشکار در زمان‌بندی مورد نظر بنیامین نتانیاهو و دونالد ترامپ است: به نظر می‌رسد نخست‌وزیر اسرائیل خواهان حمله پیش از انتخابات کنست باشد، در حالی که رئیس‌جمهور آمریکا ترجیح می‌دهد عملیات نظامی پس از انتخابات میان‌دوره‌ای انجام شود.
گزارشی تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251392</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697274" target="_blank">📅 20:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df2c609dd.mp4?token=lmm6iIYnr-BJFTyTGQvhkMtrb7XnXjc0pM572XO2CD_b3940eLZ0OPiLqZMbFibGGWwZRpo4nhBu_PrUcwXiB6cKlxqeU9HPWxD5CzhTb0yw_-lpjbkDBiRbtkA4toZBkqHgXeXqDXqiR-Gtc1erlfgbOWW0wTJ7qFWJ01hvMnX3MebNyS8yDtDJ2MD1H_Y4eOzk-mLRTxfDAiGA9e4vPhTPzWIZaUM3z3JRQ280wCGFMvmj7DCSamVAhHy2_jIs9FTfwIdVpiznTPotGZRcLHEFDEt7hnUtom6p5PG7pe97ouzN_vmSTobAcw3fhaAFZJzezyzbedKdcdovTirpHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df2c609dd.mp4?token=lmm6iIYnr-BJFTyTGQvhkMtrb7XnXjc0pM572XO2CD_b3940eLZ0OPiLqZMbFibGGWwZRpo4nhBu_PrUcwXiB6cKlxqeU9HPWxD5CzhTb0yw_-lpjbkDBiRbtkA4toZBkqHgXeXqDXqiR-Gtc1erlfgbOWW0wTJ7qFWJ01hvMnX3MebNyS8yDtDJ2MD1H_Y4eOzk-mLRTxfDAiGA9e4vPhTPzWIZaUM3z3JRQ280wCGFMvmj7DCSamVAhHy2_jIs9FTfwIdVpiznTPotGZRcLHEFDEt7hnUtom6p5PG7pe97ouzN_vmSTobAcw3fhaAFZJzezyzbedKdcdovTirpHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فتوسنتز طبیعت زیر آب!
🌱
🫧
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697273" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ترامپ جنایتکار صحبت‌های تکراری خود را تکرار کرد
🔹
خبرنگار: چرا اقدام نظامی علیه ایران را به بعد از انتخابات میان‌دوره‌ای موکول می‌کنید؟ چرا همین حالا اقدام نمی‌کنید؟
🔹
ترامپ: ممکن است اقدام کنیم. خواهیم دید. ایران به‌شدت در حال شکست خوردن است. ارتشش شکست خورده، نه نیروی دریایی دارد و نه نیروی هوایی. تورم این کشور ۳۰۰ درصد است و ایران در وضعیت بسیار بدی قرار دارد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697272" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">24-2 Ane Manaee (1404-02-13)Mashhad Moghadas</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/697271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وچهارم؛ بخش دوم
🔹
افشای پدیده نفاق در لباس دین، روایت چهره منافقانه یک منبری مشهور! [00:00]
🔹
آزمون ایمان در میدان بلا و جلوه‌گری باطن انسان‌ در لحظات سرنوشت‌ساز  [09:50]
🔹
تبیین اَشکال دوگانه نفاق، از تضاد در ظاهر و باطن تا کتمان مکنونات باطن!  [14:05 ]
🔹
واکنش رهبر انقلاب به نامه تاریخی امام خمینی در سال ۶۷، مصداق خلوص و پا نهادن بر هوای نفس  [18:55 [
🔹
خطرات دل بیمار و داستان‌هایی تکان‌دهنده از عاقبت برخی بزرگانِ مبتلا به بیماردلی و تلخ‌زبانی. [24:28]
🔹
ضرورت فدایی شدن علما و مراجع برای اسلام و خرج شدن برای دین در روزهای سخت.  [38:04]
🔹
"تسویل" و "املا" دو ابزار شیطان برای فریب انسان‌ و عقب گرد از هدایت و بازگشت به هوی و حیوانیت [42:20]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/697271" target="_blank">📅 20:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d005002ee.mp4?token=Y9zqQyUBSmd9tPY43rbsLm1WqA8ZIxJR5znVkImAE3PUe64lglOw-kom2kL5uutQEls8SwXan_XBu4Fcc6r6-Oof3CoXuWJwV0gkAagSbP0cpXVYDfncqailOKbj1vWL-THvh6-LXWDD7PFqADRlFpyvmwuBoJdAB_N5-39XsgJzlb2qc2p-VfmQWWfk_uHosNwHinZ4jYwlxI0njtHARLsdOPRk-k9YWjAC3LnzywvDRTx-Wx3njE1LImQus97fXPHHObEJnYvm0gAAZ3YCq1qTGYz3gYNWZw4OunQj_c0szze8no7qoajOc3BHoq4zflNUaFgKQadwAIkjf19mPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d005002ee.mp4?token=Y9zqQyUBSmd9tPY43rbsLm1WqA8ZIxJR5znVkImAE3PUe64lglOw-kom2kL5uutQEls8SwXan_XBu4Fcc6r6-Oof3CoXuWJwV0gkAagSbP0cpXVYDfncqailOKbj1vWL-THvh6-LXWDD7PFqADRlFpyvmwuBoJdAB_N5-39XsgJzlb2qc2p-VfmQWWfk_uHosNwHinZ4jYwlxI0njtHARLsdOPRk-k9YWjAC3LnzywvDRTx-Wx3njE1LImQus97fXPHHObEJnYvm0gAAZ3YCq1qTGYz3gYNWZw4OunQj_c0szze8no7qoajOc3BHoq4zflNUaFgKQadwAIkjf19mPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کودکی که با زدن دکمه سرقت، مه‌ساز و آژیر طلافروشی را فعال کرد، در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697270" target="_blank">📅 20:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787d451d8a.mp4?token=JPjiR9qkZ2a-Wd_SZB8ErcLQS1NoXtiOIwTQFXVf-SeayiVpkfFMlmhWruDR_buS6kh0PCa_pnvvjKsBx34Anj0OnWfUi8Td3aTJ544RHsFJriHW2jr3n9WsrTpX5kH9wWVcdLjNCFswGzM79NciXGtoxU-6BDCCAkpNXaMIHc1jQkKg16eHCIKMuEaDnY_KWu6ByvJ-E8cCiQyhGIL96LB2mbTzhj0NDKgrPZic2ml3I1lRuH1MgoWqZ2TrKimnnhhysObsAMHKgP-l5_7Bri7vtx66woPt-B_4xuLbE8s836_dswrpYVRMbEDuhMPwSyuz2fwoym54hge8-Zqf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787d451d8a.mp4?token=JPjiR9qkZ2a-Wd_SZB8ErcLQS1NoXtiOIwTQFXVf-SeayiVpkfFMlmhWruDR_buS6kh0PCa_pnvvjKsBx34Anj0OnWfUi8Td3aTJ544RHsFJriHW2jr3n9WsrTpX5kH9wWVcdLjNCFswGzM79NciXGtoxU-6BDCCAkpNXaMIHc1jQkKg16eHCIKMuEaDnY_KWu6ByvJ-E8cCiQyhGIL96LB2mbTzhj0NDKgrPZic2ml3I1lRuH1MgoWqZ2TrKimnnhhysObsAMHKgP-l5_7Bri7vtx66woPt-B_4xuLbE8s836_dswrpYVRMbEDuhMPwSyuz2fwoym54hge8-Zqf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از زخمی شدن ۴۵ نفر در حمله موشکی انصار الله یمن به فرودگاه بین‌المللی ملک خالد در ریاض پایتخت عربستان سعودی خبر دادند/ جماران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/697269" target="_blank">📅 19:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دادستان عمومی و انقلاب شهرستان ری: یک مهدکودک در شهرری به اتهام ترویج عرفان حلقه پلمب شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/697268" target="_blank">📅 19:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlyMc2n0hRpHc6dyJ9RENdXBKLIlWgAdJMRuQiUbcSi16sWXZQRUY8XQxT4BoxtL1SuV28gELETH1oiHb767KKMGnJjgNMTjERbBE-c-0dRiTaQUmk94Izch5Pb0ffoCq7iHpWpUL1SQG1FinN9VChcNcYjvC9UcFE-pS9sfMyO6gdo1rgfPrw8t9TMT76fjmjdFG7E1Nu0wUNK_BeSUQg10BGrlxU7_rtpxBOlY9zr-w6IhYUGNxtjrRhjl5UzJ9O7yLDnwydmRmZr6pFqoto8Bcy8_DiJjxk98v3Z0dvPQz6SA4R3R8f0YSGfKYIVS_4yw8NzUsExwAL09Z2ebQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9SeD8eMylPvrRXUA7x4TWRKS6BngMnKvGhCrgKWNrOrptiL-kH9s7FYqTq7fZ64Rks_YjffKGkFz72UcsNxiuxZGzZwhp9-ZpwnF4yPyXq8P6--VqvAHOuQ32w8YE1nScvwsevDmZoIhaEQSJKC1RLkwOHoAWVNI0CfnB0VWpuPkHpRUaMaa9sBKxeWjlWr0StRgz7edD3qCHujCTAXSjq03zaWNW3Dhd09TJBH6Qct_pP7njyvRXdmrut8LRdz-k0etYKGgHK5erwqrxRw8xg_nltrTvKYnUuHmy0cazhxdLEs41whgkkLkLV_Rcm--8yND2Eba1wyYGFR6TOrQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرامپت
تبدیل نقاشی کودک به دنیایی زنده
🔹
پرامپت زیر به همراه تصویری از نقاشی کودکتان را در Gemini آپلود کنید:
Transform the child’s original drawing into a charming, magical scene. Preserve the artwork exactly as it is, including its original shapes, colors, lines, details, and imperfections. Do not alter or redesign the subject. Only add a beautiful, softly lit environment that complements the drawing’s childlike style, making it feel alive while keeping its original charm.
✨
#هوش_فوری
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697266" target="_blank">📅 19:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: پنج نفر در بخش مراقبت‌های ویژه به دلیل بمباران فرودگاه ریاض بستری شده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697265" target="_blank">📅 19:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318768b4ca.mp4?token=BD5rM29l4eb8tBFZK2SHf6fJ02xzX11OyprBNsMEKexHnsDOtVPH25UvnQ8EQWIB4b6sq5f2sTvjB4I_mbdlaiw8WNs1WnLMdmX3mb-IGAOV0P66MPNhEwYR0xrFbo541neofISz1rNzgutc8dCHdljnIPG5Nrp1RbTI3lrHpDw1RAGY_roSNkZw6RBRMaBdkR1aB-1oWtWhDb5T1TqvPG0oWQWenTvZrNoBdQsZSxT6fhPj-CjQmAtoqWnNZSXSAU4UQqR3NQH2B8Jmd4jF2ttcx9ZOHGYToyTGw0mcG_o86QFFE0XsAM8WkYmxZxYcE1yopoyXohNLbWTZvooyZ1EXcq3KT7E05LPWiCJ6LdfbNOhKHW2PWIQIny1TYg3Q3NFn5A2LlMk0VRJsoRT1nfswjTtoXbkxHi1XEteGqanfFeXygAjCTspEDpP9q_QW787oXlsLB2i_AUZx_46CwIcvQlVI7jgQze8Gjp-2izi6JfKRzMH4ndjff_NBSQYxk6u3CDvdEs0d1OFhdk6f75eUKk276erkSHU-Y1V73KLUIaoqm1yri9U1eut2_iqMql2u1BvNBFi4nJHPv6D74HkX6DAr8OTIwYnz3WBlFGMFd7Zg7zO1skDKDQiXfbLtkDQ0a-UDZ_3pQQI-EnBpZjCM_ER7WoD7x_Jra45iy1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318768b4ca.mp4?token=BD5rM29l4eb8tBFZK2SHf6fJ02xzX11OyprBNsMEKexHnsDOtVPH25UvnQ8EQWIB4b6sq5f2sTvjB4I_mbdlaiw8WNs1WnLMdmX3mb-IGAOV0P66MPNhEwYR0xrFbo541neofISz1rNzgutc8dCHdljnIPG5Nrp1RbTI3lrHpDw1RAGY_roSNkZw6RBRMaBdkR1aB-1oWtWhDb5T1TqvPG0oWQWenTvZrNoBdQsZSxT6fhPj-CjQmAtoqWnNZSXSAU4UQqR3NQH2B8Jmd4jF2ttcx9ZOHGYToyTGw0mcG_o86QFFE0XsAM8WkYmxZxYcE1yopoyXohNLbWTZvooyZ1EXcq3KT7E05LPWiCJ6LdfbNOhKHW2PWIQIny1TYg3Q3NFn5A2LlMk0VRJsoRT1nfswjTtoXbkxHi1XEteGqanfFeXygAjCTspEDpP9q_QW787oXlsLB2i_AUZx_46CwIcvQlVI7jgQze8Gjp-2izi6JfKRzMH4ndjff_NBSQYxk6u3CDvdEs0d1OFhdk6f75eUKk276erkSHU-Y1V73KLUIaoqm1yri9U1eut2_iqMql2u1BvNBFi4nJHPv6D74HkX6DAr8OTIwYnz3WBlFGMFd7Zg7zO1skDKDQiXfbLtkDQ0a-UDZ_3pQQI-EnBpZjCM_ER7WoD7x_Jra45iy1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وام گرفتن برای خرید طلا، خوبه یا نه؟
🔹
این تصمیم می‌تونه یکی از بهترین تصمیم‌های مالی‌ات باشه یا می‌تونه تبدیل بشه به یک بدهی سنگین! چرا؟
🔹
جزئیات را در این ویدیو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697264" target="_blank">📅 19:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697263">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a36ec5560.mp4?token=ACKGQwDUXXKjVLoc86h0ldf4NWIZylACSIA-GrTEUVIn7fX4mizA22Q9M0s9zMPWLkNTbnXffdrlKivmfI_dXPN7s8U66y2Zbx_Py5yxHEnm4gp1S4wobBVTzV-67l-ENUugX-fyMlaKNa-cYnOABwE8wjNqRwt95w8-sMyExy-dcN86SiQqw_19t0SUCDCTOrAoLlcaX4QSwJhVxOjHnl6VzbvX0Oppa3YTxItfOs7ejNCVwK32Z62n26rlBH2jbZwO5ueFjO9QF86WPKT-XkO8RPwrntthS7l5wCGIc9cLe_2WcvivGTLssRej1AkEzMfalf5xvRaMVEWrfbWPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a36ec5560.mp4?token=ACKGQwDUXXKjVLoc86h0ldf4NWIZylACSIA-GrTEUVIn7fX4mizA22Q9M0s9zMPWLkNTbnXffdrlKivmfI_dXPN7s8U66y2Zbx_Py5yxHEnm4gp1S4wobBVTzV-67l-ENUugX-fyMlaKNa-cYnOABwE8wjNqRwt95w8-sMyExy-dcN86SiQqw_19t0SUCDCTOrAoLlcaX4QSwJhVxOjHnl6VzbvX0Oppa3YTxItfOs7ejNCVwK32Z62n26rlBH2jbZwO5ueFjO9QF86WPKT-XkO8RPwrntthS7l5wCGIc9cLe_2WcvivGTLssRej1AkEzMfalf5xvRaMVEWrfbWPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به ایستگاه پمپاژ نفت در روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697263" target="_blank">📅 19:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697262">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ5Kh5C8wYGkfR3Y6BpyWxp7clknvLEoMcCBgESGz49cs4iJJ8f2pRXuUrr8GeC_nB80ZfwUn7Gp38OmVSpU3eKLXvxhRDRUtESYOvZ5PYnVNur_J1NW-gkG2PxrGX7uDyoicwkpU2c51H_aelot_OoohU7q5zym9U4x8m-W1cpZArBFsL5P0WS9f1ydfBh7xJcHQp4s3NYJZWmzQqLcowAk-t_igHSnmd_T9A5LL9BXmlyGMx85pkXNDMzmiBVhlbWg_2GLppGFXSKv_nYanFcx2SeAyyXSlwZIZMz2-ak8zcb68Bo-Mo32BMnKI9xzNduxeF207IletZYVsMTecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر فوتبال ایران پس از پایان هفته هشتم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/697262" target="_blank">📅 19:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697261">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: در صورت تکرار جنگ، احتمال قطع اینترنت وجود دارد؛ نقش رئیس‌جمهور در تصمیم‌گیری می‌تواند پررنگ‌تر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/697261" target="_blank">📅 19:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f4ab0908.mp4?token=JzxU4KS7ZJe3neAMbyWh5zH3aMrOFL-Vi4AjRFVQOgXzCpFgv2wLaLHW4_dfGWQZISDc8ZZoKsS-51sDElkOoByJCXX6sR-WqMQVKLo4TFyHm4j_sqdt-P2Snasnj5J4pX-04IadYNO_FdAG1BBPGSPBiJOt9JDP4bDAigPIbkpcb_xCxhuvewEVG6r_aKLMFt7wJyX5wAaYEerbkLHYzYQTAQ9AvBRJ7ld0UH4mj9WjqgD8ip-5BZJktES0qbRj-Zd-YKIWMUZbQTYbEGDgA7Fw7pu69IwD72Q_sEaSZnVdFS5VVAb3-VrsryXU9DEa25NdZZ60UvoBsi9XwYsk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f4ab0908.mp4?token=JzxU4KS7ZJe3neAMbyWh5zH3aMrOFL-Vi4AjRFVQOgXzCpFgv2wLaLHW4_dfGWQZISDc8ZZoKsS-51sDElkOoByJCXX6sR-WqMQVKLo4TFyHm4j_sqdt-P2Snasnj5J4pX-04IadYNO_FdAG1BBPGSPBiJOt9JDP4bDAigPIbkpcb_xCxhuvewEVG6r_aKLMFt7wJyX5wAaYEerbkLHYzYQTAQ9AvBRJ7ld0UH4mj9WjqgD8ip-5BZJktES0qbRj-Zd-YKIWMUZbQTYbEGDgA7Fw7pu69IwD72Q_sEaSZnVdFS5VVAb3-VrsryXU9DEa25NdZZ60UvoBsi9XwYsk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چراغ‌های مخفی‌شونده؛ یکی از طراحی‌های خاص و خاطره‌انگیز خودروهای قدیمی
🚘
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/697260" target="_blank">📅 19:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20e545737.mp4?token=ggg3OYfp__zsea6X7ANa_xJL_PwDVu86FI4Ut3tAxJ3ldxYOfQ3PBQVQogHbGos5xkKqMjzflv4DhMhn63IzzVssd1H0ORUKbnYeEvzsGe-HkjB0WN80KuWawpPV5ORIhpNam0671c35L2iMcBjxjf1_mp7lALvxOREF6Y95E1WB_t_L7tp581XkAxC8-oxJcp1Myf9BfogE3M56SslTSIQvTbqUt07lfpItUqa16a6TkT8QPqr_tmOnMhGJRrANSE6uTa3GtuO12AWtZ5P66Uih4wjDHwTxsuAp7SzyfSnAMXXJXzgub7_2dkvd5CXuDo23UCtTuYPQzKBhOxMS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20e545737.mp4?token=ggg3OYfp__zsea6X7ANa_xJL_PwDVu86FI4Ut3tAxJ3ldxYOfQ3PBQVQogHbGos5xkKqMjzflv4DhMhn63IzzVssd1H0ORUKbnYeEvzsGe-HkjB0WN80KuWawpPV5ORIhpNam0671c35L2iMcBjxjf1_mp7lALvxOREF6Y95E1WB_t_L7tp581XkAxC8-oxJcp1Myf9BfogE3M56SslTSIQvTbqUt07lfpItUqa16a6TkT8QPqr_tmOnMhGJRrANSE6uTa3GtuO12AWtZ5P66Uih4wjDHwTxsuAp7SzyfSnAMXXJXzgub7_2dkvd5CXuDo23UCtTuYPQzKBhOxMS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جدید ظریف که با واکنش کاربران روبه رو شده است:
وقتی موجودیت کشور در خطر است، شما به دنبال بقا می‌روید. چرا عهدنامه‌های گلستان و ترکمانچای امضا شدند؟ چون دشمن تا پشت قزوین آمده بود و درصدد تصرف تهران بود و موجودیت کشور در خطر قرار داشت. در چنین شرایطی، توافقی صورت می‌گیرد تا بقا حفظ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/697259" target="_blank">📅 19:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697258">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33076f3269.mp4?token=tbh8H_JchzNg67nysULc1QJMYB3NJypSbDOU6NyOI_hfW-Wa_x2KNqf7-TzTzj7pssltMFbwSFgqidfvgnLI-F3PxuCoMVjSTmU6MD4peO7kru2n0nZy7cn20rMWvJDN8zH4VWaXV7_W0EG0k-Sv8_1A1VPL1UQu_qJ5K6htJJuuNkn7x_guIQdcqp-ZrwSxiL9fl1A1NKnYVkJ-v3jjbM241rYGCL711kBvk9Rzukhos_Nj6TXOJCVCrX5okEhHeaM3_FOw3T04e0Gt72avP0ccV9PEFsgaEnKhIXf4JKHJFVT6fg5imVKXsAPv2CUNEGruLv79k7Jh3xJjPFQo_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33076f3269.mp4?token=tbh8H_JchzNg67nysULc1QJMYB3NJypSbDOU6NyOI_hfW-Wa_x2KNqf7-TzTzj7pssltMFbwSFgqidfvgnLI-F3PxuCoMVjSTmU6MD4peO7kru2n0nZy7cn20rMWvJDN8zH4VWaXV7_W0EG0k-Sv8_1A1VPL1UQu_qJ5K6htJJuuNkn7x_guIQdcqp-ZrwSxiL9fl1A1NKnYVkJ-v3jjbM241rYGCL711kBvk9Rzukhos_Nj6TXOJCVCrX5okEhHeaM3_FOw3T04e0Gt72avP0ccV9PEFsgaEnKhIXf4JKHJFVT6fg5imVKXsAPv2CUNEGruLv79k7Jh3xJjPFQo_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نماینده مجلس درباره تبدیل کنوانسیون دریای خزر به «ترکمانچای دوم»/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/697258" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697257">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a6d63389.mp4?token=Qr8svuAOeHcf4wtk_MTuwVgEKtD1hQ7SH6WHsqKsD4jXBKdjtWQthkjQwRZvNczJh6QC9CU34Ldgg_D2tzEijUCTeJ-YZkDrV0Xd1okocF-LddC16ynifr9Un94KJD04_atyTaqBbrfKzeFQhWFecim3mdHQzcV1-nSyveuabOtqeVcXrRaL-mcF2U703_eEgUhtUlrJiwu4L52XelzAiRtTHGGBrCQxc9ZR8mtJS9GfaQFUt9MoBi74Q2asBH5oPVoTcZ7Xr_QwjZO-S0jTFf6OxQjwPBdMiZcgBbZXGfARES3BcUkX8BUhL0c3ddwxmlD1zes_2lVSYttrefOoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a6d63389.mp4?token=Qr8svuAOeHcf4wtk_MTuwVgEKtD1hQ7SH6WHsqKsD4jXBKdjtWQthkjQwRZvNczJh6QC9CU34Ldgg_D2tzEijUCTeJ-YZkDrV0Xd1okocF-LddC16ynifr9Un94KJD04_atyTaqBbrfKzeFQhWFecim3mdHQzcV1-nSyveuabOtqeVcXrRaL-mcF2U703_eEgUhtUlrJiwu4L52XelzAiRtTHGGBrCQxc9ZR8mtJS9GfaQFUt9MoBi74Q2asBH5oPVoTcZ7Xr_QwjZO-S0jTFf6OxQjwPBdMiZcgBbZXGfARES3BcUkX8BUhL0c3ddwxmlD1zes_2lVSYttrefOoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بایرن مونیخ سریع‌ترین گل تاریخ بوندسلیگا را خورد؛ در ثانیه ۷ بازی و در دیدار با اگزبورگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/697257" target="_blank">📅 18:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697256">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgqLi9RtIPf-sQMncXxBpum9QgBai2QJhOiWAuLON_G5kAflRusHuuIKp2v3VoNp5ODsj7bhjPzwTyeR-z1b3PmWp_0qnLadesRP441rgPR8IXVHVSzokp-PjaefHc0FEseK1NkVpik1HtGqhGJEtdWzhoNVVz8DUvVJPF8uDieC5wlHW2iXrp_nwCaaHwOgTSffY7aAJhSC3zcCde-goZOD0s2spb-Enap1BprCWPfQFlh9n_GYG2bt3YHSu95urTG6qb5ZeknDl2tj741gqHugFGKQHQt9K_thvL0nS2YNa5Sm29ol9hEJnRzNtLX-d4SGuVNswRxNJLtpuaND5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلم منتشرشده از محوطه خون‌آلود فرودگاه ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/697256" target="_blank">📅 18:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
فیلم منتشرشده از محوطه خون‌آلود فرودگاه ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/697254" target="_blank">📅 18:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meKV0jnYKkyh_lrrI6I56ajSjDdoHm19EG0IvD62RWiGuiw0Wl5CZzOQOF0qbyJ2GzbsJdy8lFSDjkg24imLdYy5tufTVdxYGbdynhr2ghgYUZee6U6k5j_mEGOesu3GD_qdbeYUq5HL16cy3Dr4w863ln7m00ODETZbcINDI1ZSt876iOjhibD_pTBGdBAeDQ_OZk43r2RHwjwNlaiJ0-jEcvEShiHHDxviR3nbHvnhHBhBD9ADvV0qdHts95CwT7pHbmjCmABZ7HnPLVCaW6HqlfUdzOLyE7joAevdJ0YI07gI_LGjykNiIGiRp-FO0I7uqW6xnnPiKszMB3z7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴۵ درصد صادرات کشور در اختیار ۸۶ شرکت
🔸
تنها ۸۶ شرکت شامل ۱۳ شرکت بازرگانی و ۷۳ شرکت تولیدی، حدود ۴۵٪ صادرات کشور را در اختیار دارند.
🔸
تمرکز بر همین ۸۶ صادرکننده بزرگ و رفع موانع فعالیت آن‌ها می‌تواند بخش قابل‌توجهی از صادرات کشور را افزایش دهد.
@amarfact</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/697253" target="_blank">📅 18:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYZISNgOHlPFMVRo4AkZiDrzVKpHFFBQjsx7KstfiMH58eZO59EKoa1zY-VCo0FFf92Vr9JIOIvXEsRRqLwwBrdexjh0DOVC6-0Cd0N_o7wk7Jlt4rIReSUFjiCQ4stcLs0xGMDYgqLol55NNSd4s5gMiBEVzXwXYxC1HHsY_19AWcLq3sM7V4sK9mN4TdRhTeiiXi8yRxIm6jmiTjGUCG6tWIZQw8CT3ZEELHAlFDGDK6BZ3o3L87Hv_dMsxvI7r5XiyvUDdNcoazc2W6G2H5geoleSqogXK8H6DOC5T8Z8Mk7juI8-y3QsoEMer5O_YX6HtDwIAYFpNHzYqzQ7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری محسن‌ تنابنده علیه روبیو: آفتابه ایرانی ۱۰ برابر کشورت قدمت دارد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/697252" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJCWK4LdCDJHd2WnOmBO95PvKrunMv2Sk3Ft9TV4CH2B2ByyvoXIGF_pIjq7GQb4b8AvnQn3qYnvQbxa5wpeO2uLKLEjRi8co0FOm4lpWdZIUvm03PQboUZqaf4zzSqkqA59mZdB0BRAHsTQSbchj4Ha7cJi2nbQtfPVDc_dpYnMbIVzf-K-2ACRwNGTXvhWdjQL3Fe6yI4GzXrNGNAE3_WDOqBOc7w6AYl4oXImt7PD_HPgTWjLLEl9THa8JcKjpX8iIzaxNCHx8UDcF-HwH2fp0rC5_10o6hu12bepDueugTfxaW6UBrFik-FSF9uWYDQbXNY7FcL30VMYhKLCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسیر روستای گرزلنگر، ایلام
⛰️
🌳
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697250" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895582443e.mp4?token=Lk_5yFfE9DJXPgPOG498iuc9IuHZZDEIfuJLLCFnFLd_PsE-_A1Dogt5Abtd9cSO_BVjgyIHY9mf0LADl5LnFs1aoPZrGzv0JX3N3q5h5rFCMdxKsV5nDhis0-I_xX-WAGh57go8dETFgxTwDRkiKtCMwdi0WvQX7VUHvSVzg8EstNmdXlfafdk_Fw_KPhQX75YGlxVu2SKDTd875xhLVQc9R3M-q2DGRgAElYzynmr_qSB8wY9_kYQEpeONytWNm8RxtSIV1dUfTgRes5aSVuFQNPr89lTnsejzByb5W_Ww2Nnt3JYEYKTOSRnhWWptz5rfKtJjqJQ4rF_3hV-WWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895582443e.mp4?token=Lk_5yFfE9DJXPgPOG498iuc9IuHZZDEIfuJLLCFnFLd_PsE-_A1Dogt5Abtd9cSO_BVjgyIHY9mf0LADl5LnFs1aoPZrGzv0JX3N3q5h5rFCMdxKsV5nDhis0-I_xX-WAGh57go8dETFgxTwDRkiKtCMwdi0WvQX7VUHvSVzg8EstNmdXlfafdk_Fw_KPhQX75YGlxVu2SKDTd875xhLVQc9R3M-q2DGRgAElYzynmr_qSB8wY9_kYQEpeONytWNm8RxtSIV1dUfTgRes5aSVuFQNPr89lTnsejzByb5W_Ww2Nnt3JYEYKTOSRnhWWptz5rfKtJjqJQ4rF_3hV-WWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: تردد شدید آمبولانس‌ها در نزدیکی فرودگاه ریاض. یک شاهد عینی می‌گوید: «همه جا خون است.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/697249" target="_blank">📅 18:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952e11e567.mp4?token=SNHi9cHrADuSfRMOqgFqjIStLueKRhCFaCQIx3drwjSZ9lw_IR8cxo5WwpmwitEip03YVwUtdWQLdhGHc_X2KD62CST1MKfScfIGl1gR4oJsZUxJVq1i77-OsswXi-ni5sTu5WP9RxOCZDZ_6RdUfq-rzoyMsREteP33Xn_bl3uKN-z_4VzwVWm4jSpyaeIvp3LocNhYSLImZcMGykoyZWaP_M9z6P2-gnUmpzj-9sooFjEB82yuMuoEL0BAfMnMgETQPq14jT2DJ8mt-rkEy8QyIQ8QC3Fqcpd8iDZ7W6JAqnVJFs6mHRayNX7YB0-gglf_PsEpdlRc-tOehXkq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952e11e567.mp4?token=SNHi9cHrADuSfRMOqgFqjIStLueKRhCFaCQIx3drwjSZ9lw_IR8cxo5WwpmwitEip03YVwUtdWQLdhGHc_X2KD62CST1MKfScfIGl1gR4oJsZUxJVq1i77-OsswXi-ni5sTu5WP9RxOCZDZ_6RdUfq-rzoyMsREteP33Xn_bl3uKN-z_4VzwVWm4jSpyaeIvp3LocNhYSLImZcMGykoyZWaP_M9z6P2-gnUmpzj-9sooFjEB82yuMuoEL0BAfMnMgETQPq14jT2DJ8mt-rkEy8QyIQ8QC3Fqcpd8iDZ7W6JAqnVJFs6mHRayNX7YB0-gglf_PsEpdlRc-tOehXkq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت شدید سیل به منازل، خودروها و احشام روستاییان شهرستان گرمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/697248" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7155a17b87.mp4?token=DXJA1nM2NmXprZSSqGZ6SO_2lugDhET1nBS26PVylt-mmztJ5D5i2G9dXngvQTdBHyRPdwzHyyTM4PLqCY4FEPMJPDgZCffsyT6UxmbtldVXGEr267cBCy6zfABIviQkfbZbwrs1mlbnwSVvMKDnImx9VfBVYDED3AYk16xX9R-Ek43gob3v_x90XgvfNlCdBAso-OduXMYOnrMy2W9ajR0sP_5duXup2vRE4i3bcN1ECdSbrvwMET9RxOlweqLm7hEEcC1sxYjLcKAo8dCiANSDcEsw9FT95D8Xs1nog_k6DRD5wft1MsvVFohSf5XDjbvydlpwGAwbmG5ZSETMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7155a17b87.mp4?token=DXJA1nM2NmXprZSSqGZ6SO_2lugDhET1nBS26PVylt-mmztJ5D5i2G9dXngvQTdBHyRPdwzHyyTM4PLqCY4FEPMJPDgZCffsyT6UxmbtldVXGEr267cBCy6zfABIviQkfbZbwrs1mlbnwSVvMKDnImx9VfBVYDED3AYk16xX9R-Ek43gob3v_x90XgvfNlCdBAso-OduXMYOnrMy2W9ajR0sP_5duXup2vRE4i3bcN1ECdSbrvwMET9RxOlweqLm7hEEcC1sxYjLcKAo8dCiANSDcEsw9FT95D8Xs1nog_k6DRD5wft1MsvVFohSf5XDjbvydlpwGAwbmG5ZSETMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتسب به سوختن یک تانکر نفتی در تنگه هرمز و پرواز یک بالگرد آمریکایی در نزدیکی آن، که گفته می‌شود توسط ماهیگیران ایرانی ثبت شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/697247" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03c0d7418.mp4?token=efSuJDh1Y0HM_fxgV-25HoeGgVn11Fbqvjbt-ZAnPyzMWdFt3Q_wFMRssXe-k98TPXb_ytxyeDtY_C44qMmceG0nwM8BxPJ32DPDckSxS3wqAFAAgYgMDtMIKlOUe_mpuvoDGydFD_5_-O_8QwsTm1ZFR0ODHD15zzlFhumnRAKz9-2aTZqDkeoXho-aE0DVsz1vO-j0qbQ6IKMll-BlFF-WR9PRAWG-FGxkPtwvlbR827lU3JzkwM6fAG4l96E8yR5vWgHpEWXThD9yJgPKNA3Xc85sQixh3xe1MI-f3EEhNG-ZNwd2vorEyHzR03P1L1Vqq1doR546fSeNt52KVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03c0d7418.mp4?token=efSuJDh1Y0HM_fxgV-25HoeGgVn11Fbqvjbt-ZAnPyzMWdFt3Q_wFMRssXe-k98TPXb_ytxyeDtY_C44qMmceG0nwM8BxPJ32DPDckSxS3wqAFAAgYgMDtMIKlOUe_mpuvoDGydFD_5_-O_8QwsTm1ZFR0ODHD15zzlFhumnRAKz9-2aTZqDkeoXho-aE0DVsz1vO-j0qbQ6IKMll-BlFF-WR9PRAWG-FGxkPtwvlbR827lU3JzkwM6fAG4l96E8yR5vWgHpEWXThD9yJgPKNA3Xc85sQixh3xe1MI-f3EEhNG-ZNwd2vorEyHzR03P1L1Vqq1doR546fSeNt52KVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی گلوله به جلیقه ضدگلوله برخورد می‌کند، داخل آن چه اتفاقی می‌افتد؟
🧵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697245" target="_blank">📅 18:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRgRKFG4C9r1fkPO2kkKB1iE9HKKvv96yE6WKaM2aQpF4RHhnNZHEDZhuAxjpf76MELpGOMxHDWhLo2MehjllFgWEzEaH9v7uFvFzRI7AzXWjINPFRNcrnsj0ctitHenBuHilAvtUaZZlyw6gDI46IOFYT8RVpNP5D93rdt1FYpjdXn_H1fQEHfBHZN3dc45ksAPHwsddq0vF07JXalBlvQl80TER7L23-e3sAsKY_Xw8yoJlyxhL-yFH_gJfN3NxRztPvnenDE1hXw49O_YSqAlZFpH12wjN_fewIdHyYXahNFakrK6sG92WDWfaZoMa0UmEe00Bc4rxAse345R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ازکارافتادن کامل فرودگاه ریاض/ ۲۲۱ پرواز لغو شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/697244" target="_blank">📅 17:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqWs7N8VsSx0K7qs8O89abhZL6QCmMejpkNlyvY1siSoTzd9DP8b-L7914bBX3R_m_gzB-7aedDs8xbKXWqIcXyJfGPQGzwuizR9Fik8hwXw9HC5AtkHhXlQZk2SY3Gk00exP0Jt_4XKv56jWubAtMDnUY_3mQMP11cPrqCYbfrjosaVuL5s6IKWlLMigEvQnzeaOnK2Qtw1AgNEnrmKP0SCsms-DdProXPONY0XBo4N4VaP2Kl1mQWLdbdyfjZKF1L3h-E7UyDvqMPBCDbMbHHr2yyh5gb3OoUCPG3QjbynjVkPN1cyh3k5x4BITODBpJ9TCczju3zrdsiJB_YY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNz6OFO0b4IErx2UtxTOOMmCAbWF_qPODkltFhaUfYHuyK0V72h_wiN8Typ2IpJPSHhNcKQrGNjUhjuWjmLr_3HCETT2o5vqeloV8xRujhUA6N_ruOpi_7ZTvSAwbBKEqeKCjM-Lvv1I1yjXDT6RzgYgyHH1jhlQekC1cz-tze_E2Ipqj2oK-CsKpP9otBqYhnY2v4bDx_8HMVc4glM3yuKGKgABRqbBDihs2QicYD1aCrJpps41GgTKsJDgNiWTo_nB_CN7jYtaUSZ1l-HfbxKEFN019O6nZTX9pWxANSKw8giRvcwvmyZJkUqHwzVWjr2FO96dQcOZYAqmEIFiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikDcKT_FXwKOan72G7O96pVKfkj9t6oYfi_IsM0WTlNqeTfkzkVTvTuGz53VcppWTkGoTVJrXfd0HJ3XR_FzGn4NRqoCoLvrcmSSGrFnPeHkk9kwvGIqv26ox1v-k41y9kr4g2f29ypl_WqQKlvmuItyxWmMwf-hWb6xe01YIjB-bDZcUNGQdY1vicwZ_Hfslx0pKpVjUga3_Mo7I5blpRQM7k4rR3qfok3dxUrxpYKuoSPNyeGCtold4l4f34r6oi3oEULuAeszWlK-Ly-Hm0t88lP3p97JRQKXmN3K4R-U-vnzhp5UlJhtq6C6EPxZ4K51RYDRz9crb5eo5jp4hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسم تمامی وسایل ضروری سفر رو به انگلیسی یاد بگیر! #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697241" target="_blank">📅 17:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c8ec8d20.mp4?token=nNASKaSFfnQlErrzOc9x3I_YatkDC89B6S1x6XaU1zC58cbqTtKglUjpRNcZsR_3Y3FVnPaaAt01e1AqYXmYzfC9fURFVhTWS8k1KjyeQEsmLwaVUelsMJEjJCOwjemHDc6cvNcLfGMIF8FyElyotyk8szmfkQW0wAdZ6D8ds86kuAzfzerd20H_Fb-Yx0VKVDNcfDjm0Zr2m_kGwwdReZWFZumPPg9ciykLiIiHnAceNrhvi6rW3Y0cviaOQtJNqsI0zsjwJ0_Il80JiWLvx09BEprmehuTHUAR90nM4kc_yKy6Zn8nSJS3KG7ILNq-MFywRRgISBw444xWc_Z_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c8ec8d20.mp4?token=nNASKaSFfnQlErrzOc9x3I_YatkDC89B6S1x6XaU1zC58cbqTtKglUjpRNcZsR_3Y3FVnPaaAt01e1AqYXmYzfC9fURFVhTWS8k1KjyeQEsmLwaVUelsMJEjJCOwjemHDc6cvNcLfGMIF8FyElyotyk8szmfkQW0wAdZ6D8ds86kuAzfzerd20H_Fb-Yx0VKVDNcfDjm0Zr2m_kGwwdReZWFZumPPg9ciykLiIiHnAceNrhvi6rW3Y0cviaOQtJNqsI0zsjwJ0_Il80JiWLvx09BEprmehuTHUAR90nM4kc_yKy6Zn8nSJS3KG7ILNq-MFywRRgISBw444xWc_Z_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند می‌گیری نوبت دکتر بگیری؟
🔹
پشت‌پرده کسب‌وکاری که از صف انتظار بیماران، ماهانه ۴۰ میلیون تومان پول درمیاره!
🔹
ماجرای نوبت‌فروشی دکتر رو در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/697240" target="_blank">📅 17:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b76f8139.mp4?token=HY7yGI7ae_QAqR54iVk3qFRhiu3P9vUMoNvkiGBeiRGmQzB4uzC2wRk1p3mWzHRLdbAFz2xa08Ac3-NxVlF87iXXEq9jA68RUPWj7X4Q9B3VYZgJX7tWBIiT3Wm9f8KDxoRH9l2MGtCeyaZ2-EV9a6j6V00EcmkBtdMi-R5mPI_GcDIhYoUZEcyJ5_45Xa64tYXjRbJ7c82bo3WVwFT1hFIB_nfAYwe5LtKkTr0qSJUJC_-JVZmj42qdfjMntKLnQhS0OvFhf4RZ25hM0Lm8heYdoOhQ0fGlz1MZb2fxPByG5OsGIbtDalExNigH9LuP9dMk7umIScH7J19HcFaGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b76f8139.mp4?token=HY7yGI7ae_QAqR54iVk3qFRhiu3P9vUMoNvkiGBeiRGmQzB4uzC2wRk1p3mWzHRLdbAFz2xa08Ac3-NxVlF87iXXEq9jA68RUPWj7X4Q9B3VYZgJX7tWBIiT3Wm9f8KDxoRH9l2MGtCeyaZ2-EV9a6j6V00EcmkBtdMi-R5mPI_GcDIhYoUZEcyJ5_45Xa64tYXjRbJ7c82bo3WVwFT1hFIB_nfAYwe5LtKkTr0qSJUJC_-JVZmj42qdfjMntKLnQhS0OvFhf4RZ25hM0Lm8heYdoOhQ0fGlz1MZb2fxPByG5OsGIbtDalExNigH9LuP9dMk7umIScH7J19HcFaGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: تردد شدید آمبولانس‌ها در نزدیکی فرودگاه ریاض. یک شاهد عینی می‌گوید: «همه جا خون است.»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697239" target="_blank">📅 17:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بانک مرکزی: بانک‌ها دیگر اجازۀ فروش طلا ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/697238" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن چند انفجار در ریاض خبر دادند/ در پی دستور صنعاء برای فرود هواپیماها نیز فرودگاه ریاض تعطیل شد و چندین پرواز تغییر مسیر دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/697237" target="_blank">📅 17:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ff2aa89b.mp4?token=GOWLLdcghhUt127WnH0Ds_OxmRjPD66YDaKJuNdbQoueVCrz7Kx2s3CuZmDgU7c0BbjJ703pS-jToNkgxkzRcGLMYaQx1U42ijphIQOqhdFqNACCHaeLXm-B6gSC2l_r9FjxSxTaqs4I085S5703gAXF1Ga8PsxwUupCvBitA8g518CmiAglrr9WmbKxmIS6714k3I-rW9mbZ3OGqgA8_VdKvjjK1jNcjUuzMO6hz_CKvj1GXH7J5t4mJsgj3iPUO_bY1hizf7pQdZWop2l2pHASTG4yOaqclYcG415xyTo1OgvLRkexcTtMYhBql9R0LlreksnQeyWSMN5mEL3qqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ff2aa89b.mp4?token=GOWLLdcghhUt127WnH0Ds_OxmRjPD66YDaKJuNdbQoueVCrz7Kx2s3CuZmDgU7c0BbjJ703pS-jToNkgxkzRcGLMYaQx1U42ijphIQOqhdFqNACCHaeLXm-B6gSC2l_r9FjxSxTaqs4I085S5703gAXF1Ga8PsxwUupCvBitA8g518CmiAglrr9WmbKxmIS6714k3I-rW9mbZ3OGqgA8_VdKvjjK1jNcjUuzMO6hz_CKvj1GXH7J5t4mJsgj3iPUO_bY1hizf7pQdZWop2l2pHASTG4yOaqclYcG415xyTo1OgvLRkexcTtMYhBql9R0LlreksnQeyWSMN5mEL3qqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی از ماشین‌ها دقیقا صداهایی مانند صدای حیوانات دارند!
🏎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/697236" target="_blank">📅 17:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن چند انفجار در ریاض خبر دادند/ در پی دستور صنعاء برای فرود هواپیماها نیز فرودگاه ریاض تعطیل شد و چندین پرواز تغییر مسیر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/697235" target="_blank">📅 17:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای الحدث: نیروهای انصارالله مین‌ها را با تراکم بسیار بالا در منطقه باب‌المندب کار گذاشته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697234" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828c66f5ee.mp4?token=km6GV_Sd5nHdP0bc7a4To7UAb40Keqy1wX6PHqB5AYjTAaAvxMrVnpAyZc7JViA3L7iycugCvISwUlOWExMJ3fN2Np9KzugUVNq7vAKe41qQ0R1KRhjOQGzo-LAd7G4RAIesf7HZjy-D8238fYYp0y6WBWC8KcWM9M3X37gGIFCeLsx1YsnenHCrTNlwi7QG7k6JyH09fSA4T5enxLcZvCiuVfYr3WRsWOu94k0dsHSoulNAHjHAW-HpWg6weM6TamYUGbwudIVJDOF3blPkffqK4EKHhF_ZwG69BqL8rCdXptkI7fWB1dahFhjBJBoTJce_8JTnxq_vhI4HUHC2xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828c66f5ee.mp4?token=km6GV_Sd5nHdP0bc7a4To7UAb40Keqy1wX6PHqB5AYjTAaAvxMrVnpAyZc7JViA3L7iycugCvISwUlOWExMJ3fN2Np9KzugUVNq7vAKe41qQ0R1KRhjOQGzo-LAd7G4RAIesf7HZjy-D8238fYYp0y6WBWC8KcWM9M3X37gGIFCeLsx1YsnenHCrTNlwi7QG7k6JyH09fSA4T5enxLcZvCiuVfYr3WRsWOu94k0dsHSoulNAHjHAW-HpWg6weM6TamYUGbwudIVJDOF3blPkffqK4EKHhF_ZwG69BqL8rCdXptkI7fWB1dahFhjBJBoTJce_8JTnxq_vhI4HUHC2xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطای دیدهایی که مغزت رو به چالش می‌کشن!
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/697233" target="_blank">📅 16:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxBL06YNbyFFB8c-FKpEXCjBpD9XphDuc4K6F_v9bfFtZKfjxlezWtSnyV8v7JKvkdRPjaKM17aw5sjSR9nHP1QuvruNLOR4YN9lLu4H3hqNV_c2L5PLMz8b0EjL_N-xWfl6g37swHXcluHaknUn1S0CsP2nsdLEoqWknaPAVHsnzIA6DK0j40imdb2eJx8a6r_r_MtMr6Se0CWXUvUFlNb3fWfOsW7rEL8SU7Wtm2OtsCwuP6ZgyPGO-P1qW1SA3NMHvE9ev-D4M0rmN49ATGZDa7VgaB5h8s3MTcxfxt5WVaMZOL18EWXTIyoTXBlDhfgAlTrG1aRCLdWDTGSpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری محسن‌ تنابنده علیه روبیو: آفتابه ایرانی ۱۰ برابر کشورت قدمت دارد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697232" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۱</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697231" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی
🔹
جلسۀ اول
سخنران: آقای پناهیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/697231" target="_blank">📅 16:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پزشکیان: اینطور نیست که اگر امثال من را شهید کردند کسی در ایران نمی‌تواند مثل من باشد/ همه می‌توانند مثل من باشند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/697230" target="_blank">📅 16:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d10f0225f.mp4?token=KfQX2yYMkn12lXb9hL2rhZIRxDGM966RJLRcxsf_P62PV_Dq68--iQIRey5u4W9fdj-pWth7iS1ryB3DgDtBhjINcpxq0SpzkF8vAgu3bLGZnpc6yJi3eR_oFLLaMRsr4uH7ydPqJRz845UTSpXPUCTNeCg8uZFKcXEzDqp1llgN15FEXLk5wpznrg5hbDj0zTP0-e7HNMv84nBhHS44Yk0Q15ymGEbZLDKhGQ1lIPg1zJYDntZZewbVXQHNzifKBhaYru-CsJgXzaxuwD13X-XzejmcrSJ8aNicMI11-JOCt5jDhScziMEpQFUkcYmNme4iE1_wtUiUiw7aWlNIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d10f0225f.mp4?token=KfQX2yYMkn12lXb9hL2rhZIRxDGM966RJLRcxsf_P62PV_Dq68--iQIRey5u4W9fdj-pWth7iS1ryB3DgDtBhjINcpxq0SpzkF8vAgu3bLGZnpc6yJi3eR_oFLLaMRsr4uH7ydPqJRz845UTSpXPUCTNeCg8uZFKcXEzDqp1llgN15FEXLk5wpznrg5hbDj0zTP0-e7HNMv84nBhHS44Yk0Q15ymGEbZLDKhGQ1lIPg1zJYDntZZewbVXQHNzifKBhaYru-CsJgXzaxuwD13X-XzejmcrSJ8aNicMI11-JOCt5jDhScziMEpQFUkcYmNme4iE1_wtUiUiw7aWlNIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با سرمایه یک ماشین و راه انداختن این کسب‌و‌کار تا ماهی ۳۰ میلیارد تومن پول دربیار! #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/697229" target="_blank">📅 16:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b032a3244.mp4?token=J__VarEMCPVxWgX2iU5VNDhUc5pL3ykXbxonM6C_NCmWXi2rkak8ErQH0qWRFV9Bg5ZBEuB_VAM4SIC0A5R5am5rOGTEwGrBGdPCzHFXdMMNHxRrn2nfJB1gMGSGPpfDZ_ibYv-QzkClBDwVoCTJPtUmHjHvSd80uHCPJsfCmjf7BfXzbCp45iM3x8iRa32PitSc9DK9z2LZ6so7N8s_Kpf-5nUYH4q1B7s4G-ooK-ojhiiIFeUotuS96NywQrHeECFBNNCLCBBE7TvAetO_hz2NqJjoWLLt2GJuSxCXMgnlKPinpYUfYpOcpxeugSuPyNoS8hKf0OGdXEPwvoZO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b032a3244.mp4?token=J__VarEMCPVxWgX2iU5VNDhUc5pL3ykXbxonM6C_NCmWXi2rkak8ErQH0qWRFV9Bg5ZBEuB_VAM4SIC0A5R5am5rOGTEwGrBGdPCzHFXdMMNHxRrn2nfJB1gMGSGPpfDZ_ibYv-QzkClBDwVoCTJPtUmHjHvSd80uHCPJsfCmjf7BfXzbCp45iM3x8iRa32PitSc9DK9z2LZ6so7N8s_Kpf-5nUYH4q1B7s4G-ooK-ojhiiIFeUotuS96NywQrHeECFBNNCLCBBE7TvAetO_hz2NqJjoWLLt2GJuSxCXMgnlKPinpYUfYpOcpxeugSuPyNoS8hKf0OGdXEPwvoZO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان «ایسایاس» در آمریکا، بیش از ۷۰ درصد تولید نفت در خلیج مکزیک را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697228" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان: مگر کالا گم می‌شود، مگر کالا می‌تواند در این دنیایی که ما در آن زندگی می‌کنیم احتکار شود، از ناآگاهی ما است که این اتفاق می‌افتد، همه این‌ها قابل مدیریت است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697227" target="_blank">📅 16:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9825915b6.mp4?token=KAC76vnfgHWayE1KCNIqcn2ZEWFPtPRzyT_xqYwi1dVbsB1SshuNZpLaIcQZz01wdi34B31KAM47WIZSqr7flm1g43AdgfIa6RGC9i8TYB874yL0njusou-Vx0OCQYeon9VRcf_BmB5dvjKDQ53tznOfS7tBQu3OE3H7_FVSMyxXxycWBWeuO05Ygi3Eael_bZDrK4ygGg34TTzwj6-CAgcJNzcOhhF0ekSEE6R4l6Id9FXAbJK5FlswU_YlsPbCk5gNRtfArObA6AXTr0i6_VCiL1sTEUmn0DzMsX3lrSHkS9U9DTirvDf2s6DASL9yiTKor2qgGBB6aAMSvy20cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9825915b6.mp4?token=KAC76vnfgHWayE1KCNIqcn2ZEWFPtPRzyT_xqYwi1dVbsB1SshuNZpLaIcQZz01wdi34B31KAM47WIZSqr7flm1g43AdgfIa6RGC9i8TYB874yL0njusou-Vx0OCQYeon9VRcf_BmB5dvjKDQ53tznOfS7tBQu3OE3H7_FVSMyxXxycWBWeuO05Ygi3Eael_bZDrK4ygGg34TTzwj6-CAgcJNzcOhhF0ekSEE6R4l6Id9FXAbJK5FlswU_YlsPbCk5gNRtfArObA6AXTr0i6_VCiL1sTEUmn0DzMsX3lrSHkS9U9DTirvDf2s6DASL9yiTKor2qgGBB6aAMSvy20cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به فرانسه خوش‌آمدید!
🔹
جایی که ایستگاه «شاتو روژ» در پاریس، شبیه صحنه‌های فیلم «راتاتویی ۲» شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/697226" target="_blank">📅 16:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1949049c9.mp4?token=X3HkWKpBxCeFRjbtQat4v9cbY9Mte8KHzPgI6wWmpdT7kRZKf03oNBzwznscMscULyJ7p5AgMmUQWsXP4fpAc5t3GNpavB-ZNd4H3vBg7LOqfaHkvpTfrpiZ6_lL11RdwMIpEreR4Ns-rn8a5aOGGeAZa7aTILlwENG-eRX69eQcc4rq9XS8mhe8xBq6vgja1LLiNZy3AE2GTB3YZ2lSp--PcV-9aPO0MW1iEKJf9XEhdgNBOtjb9XXD04sgNS7AKmIRxVeWRwVgIhyQE2pr-wXz96x0XFNvNtDDR8FwoMGtULtu3t71dUiqtuOf72eVbPce1YeDeoCjeYIGdYJ3I4Ljd4JOVpkl0ZJsM9DsU7eUSYrzMGI5Kxwlmyq5r8gDP3lDma2VJ2c7LydOphB82wsn10f7WW4Eoa0O9aQ4u90z1ZC0FAJfCvrNixZcFTcOaMbxcGPygSjqzx0cmPrTrAuJCuvbWlbeb-d1p-3iXbW9yY_Kw8czkhdYUwmcUj3pOgSogamAVyJlmT4f3kpBFg2RpLh24c8s-BaZ9xbkSfVPFoJvan5kHF4-SJjOoCdlNaaGBygP0PX1pgkbt0X_eHNaWsFBWGTf4ScxyFMlYf0ue9jqffCG2GzAAP_kIg0Ovg9J0eTKXpEPvYNsccRrid_yI0OatpqVr8UkvfexQXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1949049c9.mp4?token=X3HkWKpBxCeFRjbtQat4v9cbY9Mte8KHzPgI6wWmpdT7kRZKf03oNBzwznscMscULyJ7p5AgMmUQWsXP4fpAc5t3GNpavB-ZNd4H3vBg7LOqfaHkvpTfrpiZ6_lL11RdwMIpEreR4Ns-rn8a5aOGGeAZa7aTILlwENG-eRX69eQcc4rq9XS8mhe8xBq6vgja1LLiNZy3AE2GTB3YZ2lSp--PcV-9aPO0MW1iEKJf9XEhdgNBOtjb9XXD04sgNS7AKmIRxVeWRwVgIhyQE2pr-wXz96x0XFNvNtDDR8FwoMGtULtu3t71dUiqtuOf72eVbPce1YeDeoCjeYIGdYJ3I4Ljd4JOVpkl0ZJsM9DsU7eUSYrzMGI5Kxwlmyq5r8gDP3lDma2VJ2c7LydOphB82wsn10f7WW4Eoa0O9aQ4u90z1ZC0FAJfCvrNixZcFTcOaMbxcGPygSjqzx0cmPrTrAuJCuvbWlbeb-d1p-3iXbW9yY_Kw8czkhdYUwmcUj3pOgSogamAVyJlmT4f3kpBFg2RpLh24c8s-BaZ9xbkSfVPFoJvan5kHF4-SJjOoCdlNaaGBygP0PX1pgkbt0X_eHNaWsFBWGTf4ScxyFMlYf0ue9jqffCG2GzAAP_kIg0Ovg9J0eTKXpEPvYNsccRrid_yI0OatpqVr8UkvfexQXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی: ۵ بار تا حالا فقط سگ ما را گشته‌است/ دو تا سگ دنبال مهدی شیری و بچه‌هایمان افتادند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697225" target="_blank">📅 16:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA_KwjOJCn84X4GTtTM0-c-FTpoVCgKHsY5yIU94XNSH-4xWFdHsyzBssqg3q_LG9hMayoLPB7bcgo-BktnAmkt0zGuhuwoCYscTIe1n41P-r2pmEIxF2QnnfQlL0gUxsAigsyJrKsfi4-uXhNUN__QqNG7MYnBeM6KmmyT5rxCHyh5t_A40EjGv1LmhiuXm_WBWayrRC0eGAAPQBs2-Lm98dR3g936RhMst11V_r4G0z0S6kEgaSp6wcpHC-Tmx9kfOoIA1f0bHIbNccIoDgU1tLRratghcXwJwTKnt4zvovi5xM7HGrukJtbdPEzvPraHd3g-U-_SxCo3xQTonDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
شهرزاد مشیری به ترکیب هیات مدیره بانک کشاورزی پیوست/ قدردانی از خدمات ناصر سیف الهی در آیین تکریم و معارفه
🔻
طی حکمی از سوی سیدعلی مدنی زاده وزیر امور اقتصادی و دارایی و رئیس مجمع عمومی بانک‌ها، شهرزاد مشیری به عنوان عضو هیأت مدیره بانک کشاورزی منصوب شد.
🔻
وهب متقی‌نیا مدیرعامل بانک کشاورزی، در آیین معارفه شهرزاد مشیری و تکریم ناصر سیف الهی، با اشاره به سابقه طولانی حضور مشیری در این بانک، تجارب ارزشمند و عملکرد درخشان در زمان تصدی مشاغل مختلف مدیریتی به ویژه معاونت بین الملل بانک، ابراز امیدواری کرد؛ حضور وی در جمع اعضای هیات مدیره، منشا خدمات ارزنده، تحولات سازنده و تحقق اهداف بانک باشد و مسیر رشد و دستیابی به موفقیت های بیشتر را تسریع کند.
🔻
مشیری پیش‌تر به عنوان معاون وزیر جهاد کشاورزی خدمت کرده و سوابقی چون معاونت و ریاست اداره کل خارجه بانک کشاورزی، معاونت بین الملل و عضویت هیات عامل این بانک را نیز در کارنامه خدمتی خود دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697224" target="_blank">📅 16:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A58bQLBq8lQOe4wg9MKnFnh0zlzY0mwlfWVbzBn2oxIKEARqOCdtbVnO0tzWWSUoLpzNlBVVkEbiWRwh2ElF9Voy6nuvW5R2-zKwh8MnlP8QuYktoimhpQIoAKGcMdVhP8_yGtUWExxTk0odx4RJYS0VGvUz4g-m2EJa6DCHQ6jzoglM3SLXPb8QqQhWllE9JCTX8WTq-4NZnl7fmswfMYZYVHvsSi69vgK98zaKmFWI6-SCDqL6PZd4KJFlakWA5m_OGXAaCz0YX9SMtd6IqJB3qCTottmVSLRx3cQOncp3VbQ1qygDvi8GdiNd7gh3dejg1MTc9tecD6oC2u8tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز شنبه ۱۸هر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697223" target="_blank">📅 16:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
پزشکیان: مگر کالا گم می‌شود، مگر کالا می‌تواند در این دنیایی که ما در آن زندگی می‌کنیم احتکار شود، از ناآگاهی ما است که این اتفاق می‌افتد، همه این‌ها قابل مدیریت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697222" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOChQ2VIyFNJaqA7a3tlyDKSdDMcP1Tibx7wf4D7geOY93vZwLBm7WkR0R_QoBkA7C0yw7CVrCUATSEI18Il6jTLg91AesCUt5UAFI3bv60MjIWn7W4hbLKHxT0BKmhfTnN5Gi-re80q6p8EwBWJnlmHkejT-ecEXcBuMM-WxDpQ88y2Z5ngGyKHGFeF2Sm3DZXehT84X213DArPVCsqKwNCNxawGj91uIhM17HLwIkj5YdO8XfpxS2khFQ4OUuEDuTzpkrkzh4_VHcEjMbD6qeAVn95AqaYNdje51zB0MUiYVJRU9iBnutBunLIoHy2s0ez7WEbivvh4ajAK7SBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697221" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231f67b31e.mp4?token=V-K_2vVl8LS8N1v7N0ThkvByO1y92Wl_HP5mrqX721ax66T4P6yM7hRoip1UIsZmfiEOmDw9rW1vByKoqm922Ir0rscSuZ2cgv8va9bKIwRj7L-Ibr3JU-jUANr-ZVbf_dgQp-bArwy9dacFHeatW8Hh5AVX8kzIr4r2wo-UcJA40lo3dQZJ5EoDKLvClLsIt6vfp4dLmI-FFTNcDPF9VIK_vn5erU8FDWHi5zWFOwkpdmtbxXt1yh5tlv0HEYsTnLkKuiYpeQ5NoKecj8exLsuI4ZyFHYZ3alSmVy4lS-BFrXch00wJm5cAl8QO7D49YMD2rtMgiTCD3mBMCc6gow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231f67b31e.mp4?token=V-K_2vVl8LS8N1v7N0ThkvByO1y92Wl_HP5mrqX721ax66T4P6yM7hRoip1UIsZmfiEOmDw9rW1vByKoqm922Ir0rscSuZ2cgv8va9bKIwRj7L-Ibr3JU-jUANr-ZVbf_dgQp-bArwy9dacFHeatW8Hh5AVX8kzIr4r2wo-UcJA40lo3dQZJ5EoDKLvClLsIt6vfp4dLmI-FFTNcDPF9VIK_vn5erU8FDWHi5zWFOwkpdmtbxXt1yh5tlv0HEYsTnLkKuiYpeQ5NoKecj8exLsuI4ZyFHYZ3alSmVy4lS-BFrXch00wJm5cAl8QO7D49YMD2rtMgiTCD3mBMCc6gow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون
بارش شدید باران زنجان
⛈️
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697220" target="_blank">📅 16:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
پنتاگون برای جبران کاهش ذخایر موشک‌های رهگیر در جنگ علیه ایران، قراردادی ۶.۳ میلیارد دلاری با شرکت ریتیون امضا کرد
🔹
بر اساس این قرارداد، ریتیون طی پنج سال موشک‌های رهگیر SM-3 Block IB را به‌صورت مستمر به وزارت دفاع آمریکا تحویل می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697219" target="_blank">📅 16:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZsFH4gIMYL3UxmYU62nSkJz33D3Kmr_dbzmC6--NcURpLyMFfs5kw_fFaf7Px8hsDnNBJatWC_8v0K748d4WDKC_ZVxQ86MuDBLBBTkppWwK6xfxmCf7oMooFmrdLMjF2hRowPzMzGhWY5Gvdc2btq2tDYQX4D4m7VcfsQ28HAaRjz-X3G3C7LZKHlt3DXhP7iNuK14s8FN84Osi0KWgRcwIEl4AZgiP48wPinef19fJww70GkjWlXzCiSoriMqwdCGV54u18c9QIxCD2bxatgPS1hTMvttRS0GGOxnuDo2C4oSQKcFQsHTK1bqmLylhNEhRAXywl-Ww1uf-wM0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mID3a5Fk5FvQVU3ldi7SXnpcO3qck5mlw-ajUsOv3VZ4t7hbxP52iw5tdxowUyz_nAOEoY7ZhWfcrbGem2EH4yCy7Aor5FM9Zmg47515cYR8bWEyiLY4x5NkkaY8cnCRXs9seAXr4GxVE0QwebTpnhg9aBzayhR_8AWaJDtafet4ThbiWvuA7FpV_rIzohN5K7WqFCGrzK7Z1OrN8cohQNVAu1z0Jrp9rxFe6nfsSR98KbLF-WgbSNOpEwL1SW93BanbYZ-IqeQdxl05HRqEXI1I7kCXIW7ty-x3BdfxVeUxIz_8NFL1v2W7vrJnzfhCM-arffktonqZL7JEFhoTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUx8_O4J9hjgw0Bj8T9LqkenKN0nFrqQmARlr9iLYuC4RPtj44VxsPQRLVSZN0D3uPAe7BzqF4A5eaHpPUZtF4N0f3mfSAEJvKzGr1p41X3E7LpBDic-sqaCRoF0owjX2wvNBiyH5Z14zxN1BwjfLUXx3JCOXTRhOEaolAL1u19zPeC08GJWZYcpDPB5uVNqXCuu7d_tt8mP-chxXuJvRRrY6SwB9yAwPvjFq_F18Ieliw81VjvbyD7SRYaOdAogLER8jPLjYChkHRVAw9XTpR_md6WhzTzw2CU64L5gxqI8RZyvqdHPJd_p_vtWIMXXWch47a3v25-4C5rkoI2ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFmLY9W2o5d81Ewvm6kobi_XKCDw2a6-IOLjV7P-zTEfYHarX4BKA44nOXt0GpOXE-DTjckdoXPHwQCGSDCnlVH7I7pWVuZ2a4ZsSQxhYcIm-8-obYDOi3AlNVXbAV0IwGazZrhCIPcMWVGg11S6sh7V2GCAObM0rf71nU3CeW_Y_aYDcuEjQ_-TCqwBfN6MlTPmP78R8P15jOghUg6wqRWRjOl40EWedl0TOdoxU0yKY4eTrM3QSulkKfVX8OO9C4Q6ekvF2sFaH3xKuQ60BcwaApuo7K5Fyo0pq1SEmaJh0K0pLOBwtiOVZun86-z_oLxMF1jVZHHELfwt3MuUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHrFRbn8MWEyXEyNV_kipNN1hYHHeh2n0ERmvA0CdD7sBhmJ9qVblj6ABmeuPoMraiatygfLxqS2qJBvfK3FgMzv-BmCm0ruHn5ovzVRqOz8YzvPcwoo7STtoOOi8eotSMr4dA2mtfYfa7Spkjol1Up0926fpCxpUIDYloiA_hoZ9EXERQoMFIHJ1Pr2JU_tix9HwtauynEz5bG9leyCE3d9wU4fjKQSFxNSqfXejx-B64u-4aEks1tBNfRObRbfRmECEnibalGAP8t5Y8QioyBXUDwg0K1OG_s3Gy0YpPEookrBRtnUWpOliRrdrnfUEGgsASUgeE3ZsiPG_k4_pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برای هر بیماری، چه تغذیه‌ای مناسب‌تره؟
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/697214" target="_blank">📅 16:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
لطفعلی بخشی، کارشناس اقتصادی: تصمیمات جزیره‌ای، سیاست‌های ارزی بانک مرکزی را تضعیف می‌کند / سیاست ارزی زمانی نتیجه می‌دهد که هماهنگی میان دستگاه‌ها وجود داشته باشد
🔹
تصمیمات مربوط به تخصیص ارز نمی‌تواند صرفا بر اساس مسائل یک وزارتخانه گرفته شود و باید با سیاست‌های کلی دولت و شرایط اقتصادی کشور هماهنگ باشد.
🔹
وقتی برای تامین نیازهای ضروری کشور محدودیت ارزی وجود دارد، اختصاص ارز به کالاهای لوکس و گران‌قیمت نیازمند توجیه است.
🔹
سیاست ارزی زمانی می‌تواند نتیجه بدهد که میان دستگاه‌های مختلف هماهنگی وجود داشته باشد.
🔹
اگر وزارتخانه‌ای تصمیمی بگیرد که با سیاست‌های ارزی کشور در تضاد باشد، این موضوع نمی‌تواند صرفا در سطح همان وزارتخانه باقی بماند.
🔹
نیاز ارزی کشور فقط به یک بخش محدود نمی‌شود و اگر منابع موجود به یک مصرف جدید اختصاص پیدا کند، نیاز سایر بخش‌ها همچنان باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697213" target="_blank">📅 16:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اعزام زائران عمره که قرار بود از نیمه مهر آغاز شود، به‌دلیل نهایی‌نشدن جداول پروازی و تخصیص‌نیافتن ارز زیارتی به تأخیر افتاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697212" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL2a4sf8Ss4j8FBFqNYX1pyAYjRaHZzYygHCV_rcpIhPSEoySdDS9x5If8gNjxMqdofo2ZutQgrQ6wxTceOj5DruuZVl94Drcw3IG16uUKDpFQ8EgbaltiNQrStDaNJPyuhJk1mdEK0V36C0ogWqYtQXHnpo9wEcAotJefy3BrUNTxIjSASga_c0sDUxUqG7CtX0TbFLfAF9JYH7mpl83ok7dqclcHg8XtvuqcTMONVADR82j1e4nqj7X6yd17ZLStePc7q7ssRkjO7f34n3UxUWnSGYK-1lE3CAtvH5sIiNfNqDKyZyqytz1be9Is3tkscyug52ddrPg7HKjd2QWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم اکنون؛ رنگین کمان در آسمان اراک
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/697211" target="_blank">📅 15:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
واکنش ولی نصر، مشاور سابق اوباما به توافق واشنگتن درباره گازوئیل روسیه:  آمریکا تصمیم گرفته برای ادامه جنگ با ایران، هدف مشترک خود و اروپا در قبال اوکراین را قربانی کند
🔹
این استدلال که ایران دشمن تمدنی غرب است، نمی‌تواند شکاف عمیق میان ایالات متحده و اروپا را بپوشاند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/697209" target="_blank">📅 15:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503f0a9d2e.mp4?token=pw6sh9gm7TW4buyfJAeaz8ZiA5tRYflQS6pU_xQW4NPH-hlrmgNOkqmxOh5KaC5XeWu05Oqlp0OZ5mFEGC8IIhYhczAbeWKRIQqZczmS2mA7osfqyGMSQj7QiP7GUBmxNYSZlJMxp5RZOPpK83kGB7kzPCG2FZ_2R_eZFVSmNEhN4PYxgAWT0EwcrPjFX7aCPY3cY_iTY4d_YjGjbA5TiZgBWXsrPX24o4bquuVdktGttzbXvLfwZ3cQrthHeOOhGWhs6k24pEN0LZq5MN90qehlsANSlheVRRSUBOsSvRW3o4ovEifGwwnPIrRDXh4g1SVh3oNR66vh9EQkBfNZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی وقت‌ها رگ‌های دستمون برجسته می‌شن؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697208" target="_blank">📅 15:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngWZ-jp0TdXNpsiR01uPp2fTqJ7ONUxZXgMV-4izXUa0PqAhCt0Uj435P8rqKtBD2Hp-6zcHSXlPMnrmbk5yXF2QsvFD5xOPOowuWhKvl7Tn3vr6f6hDNfjc_Xe4QF2zFD3u-UJeXMRv_oQIy7Jd6P70HBMr4eHBIZcJl7UVxAmES5vt-OF1o8yk40khOmhMpwUJtmA6jfdTzvlYjZoIhiJqld_iv6v7QaV3dWFiqPs9A47E8hACzhIlXcyGR439vm2tTK3E_d3qXtG_DOQ3Xf1cjMmkby-o9ScqKuwus9urnZZnPTBSIPsLBbdeCl2eYYS83v0dhTs3PkgcbJ1LSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ سفارت ایران در بوسنی به اظهارات روبیو: آفتابه ایرانی ده برابر کشور تو عمر دارد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/697207" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رئیس سازمان هدفمندسازی یارانه‌ها: یارانه نقدی تا پایان سال بدون تأخیر پرداخت خواهد‌ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/697206" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ظریف: آمریکا من را به‌دلیل حمایت از رهبر شهید انقلاب و نیروی قدس تحریم کرده است؛ سخنرانی اخیر بازتاب‌یافته نیز مربوط به دو سال پیش است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/697205" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmxckMRNZM7EcEccjo-Ey2qB9b26yFx085EMVGufHQsIq3RVRYfBnQp8rPGRhUICmLHtyxg4XsqjZO9hec10FGELSgEjhhorc4D0CSRQlHDxivVttZmdFwtDGuPW2Uh0mi4wJ1aLvZFyOKzzyAb-FZIaVb9w9SFqcrL90M0ml0vc1IkaQBzDTGAL7ZHI1p3IQlacLup-7O2L9Sey7k8KYrXlmCqcfobTvIPSQO6I8LuS_qQMkt4jMxFIo3oSsojoRY3JESmWzdxqGfUWBZT8O6P0MtvwsRehFh_jyRaHswgJgachUCitCtGjQnmhjSyJXVfvTO20KPKHIGLj-xztRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی طاعون مسکو را به شورش کشاند | از شایعات امروز درباره طاعون در روسیه تا همه‌گیری مرگبار عصر کاترین کبیر
🔹
این روزها انتشار خبرهایی درباره احتمال ابتلا به طاعون در روسیه و گمانه‌زنی‌ها درباره منشأ یک بیماری مرموز، بار دیگر نام این بیماری باستانی را به صدر اخبار بازگردانده است.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251315</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/697204" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgHVrT2k_l3kaJKXYc2zs_Mzr3wD2khDIoE-wv7v73ZEMAk5FnrB1-3vApgQyfiYHrByjp3n5uMD5ql8Gfo5n-qFs7co0FP8Ldo5lfpgEeAdMMLzl-Mu9j5tt52Dbz42hp2VW87NcsuZaIIq5ju0xGE8RTBT7ojHHZj-qz7XzsLUpI5iec_WrYeANqmsw9ljBjR450qeAp5a41JkajdHqnG4quPhcuAmPkYN-cwl-2RzkIeE8bl7XSv-zf9iLOfn9PkI1rbew-uCoECknCzT9PGxIF6eefOkLMJf0Wm7SXe8mqaK5VWo7ncfVJCt41iSPh8kdJ8XJf0uJqbi_WKNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
می‌دونستین یه ابر کومولونیمبوس میتونه ۱ میلیون کیلو وزن داشته باشه، یعنی بیشتر از وزن هزار تا پراید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697203" target="_blank">📅 15:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvdEajSAXHqSRoc1Am3znDT6iiOHGunaJCddr-NviywCb2LRQHLgC7zwgbxl_jqAPJPNnlz3IdYuS_LwKUSENMofOF6_E9B9jLfCBtVLtE5Wwl2DdOODoNShX1ViBCozrgvBZxCuNOFUmha2-gAt6O1xgRFUpDGB5dSBmwmv29rOY6tjWnAy8pPyVtv0Wt1kMbPCnq8ggwqD9lPQwHIQhn2HR7ttJ-K0NWTNkuo59ReRAnbquJsnjfCd9ET0OUS0D9m514SowoZyPQMm7y-IZZ0ncH6WvJzjGd6IzPkGvTj8V5dOAogYnYEe47CS80VBq4gw5SJxI4xSaz5jPXS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جباری برون، داوطلب برنامه مستربیست که در یک چالش بزرگ یک هواپیمای شخصی به قیمت ۲.۴ میلیون دلار برنده شده بود
🔹
سه هفته بعد از این اتفاق در فرودگاه بین‌المللی کشور پاراگوئه به همراه ۲۶۲ کیلوگرم مواد مخدر دستگیر شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/697202" target="_blank">📅 15:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697201">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97db5a1cf.mp4?token=KxFnTEwnbHdCwYPkJdHwIzi-TpxmYz_D9aV6cAjcN13UI5jOUhovC6XSCC0AeWF-hnaT3Nc71o2i0CS0UycjqC1bognBzMmjGemGBRg2nziWfZawX6lZtxhVx33dPhAnnRLuBMlf_mXl3-NriitQ0cnFAIyv36fGeCsd9ErYhCtfAkU_JVpEzk8sIEv5-G49FV4ia8-ZUSw7dKVRI8Auaxj3Tyw_o5-kvX380sdr_SyMJERhB_IAOo5ULzYzyVP8heVE2GbfXPiEWCdEJXlN2zoxBUtgxDDXVRyZHDE2AvXftrsKENKpj-F__mRf8SOVDv4D12J1e9kThzHHcoNk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97db5a1cf.mp4?token=KxFnTEwnbHdCwYPkJdHwIzi-TpxmYz_D9aV6cAjcN13UI5jOUhovC6XSCC0AeWF-hnaT3Nc71o2i0CS0UycjqC1bognBzMmjGemGBRg2nziWfZawX6lZtxhVx33dPhAnnRLuBMlf_mXl3-NriitQ0cnFAIyv36fGeCsd9ErYhCtfAkU_JVpEzk8sIEv5-G49FV4ia8-ZUSw7dKVRI8Auaxj3Tyw_o5-kvX380sdr_SyMJERhB_IAOo5ULzYzyVP8heVE2GbfXPiEWCdEJXlN2zoxBUtgxDDXVRyZHDE2AvXftrsKENKpj-F__mRf8SOVDv4D12J1e9kThzHHcoNk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژست نشستن این گوسفند سوژه فضای مجازی شد؛ انگار اومده یه دورهمی خودمونی!
😄
🐑
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/697201" target="_blank">📅 15:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVBbYyuA10P8shFuioy2gEzxZkBSq-r3g2XHTa0Xl__yujO4CepjnNn7zWn7ZFGZpeZUKZ5wQ4r4ImzBbVp-2w6VvYUwg-ro2OEmhAMO8xKjXDNAlWPXvMXod_gOGlSMU6XnjlDly69xR9T3KS2LRoDaeAV3Ktt-raHI_uakvAo0mNvFH-0WsiBpSZ07feH_gKewQ2MbruiaIwN4spZrc03mosGlUlYw7u1FydaY9_P1uy7cKaOFqJ0UgMtkyGyh6o8p_26zLfeojVJ4E3nIKw90OWFTspr86BR5SaMcDs24gL8I6LubtRlF0XPGhCxKgA5GPf6yeyBaYMWoUQz62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: سناتورهای آمریکایی خواهان خروج از مهلکه‌ شکست‌های فاجعه بار هستند
وزیر امور خارجه:
🔹
نتانیاهو یک جنایتکار جنگیِ تحت تعقیب است که دستش به خون اعراب، آمریکایی‌ها و ایرانیان آلوده است. او برای فرار از عدالت، هیچ ارزشی برای مردم خود قائل نیست.
🔹
او همچون قماربازی ورشکسته، ناامیدانه تلاش می کند با قربانی کردن هر چه بیشتر جان و مال آمریکایی‌ها خود را نجات دهد. حتی سناتورهای آمریکایی نیز خواهان پیدا کردن راهی برای خروج هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/697200" target="_blank">📅 15:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ظریف: آمریکا من را به‌دلیل حمایت از رهبر شهید انقلاب و نیروی قدس تحریم کرده است؛ سخنرانی اخیر بازتاب‌یافته نیز مربوط به دو سال پیش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/697198" target="_blank">📅 15:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OByJpXm51bzSTz7rEhnK06LrYbV5cs7onC5vlwHoyh9FNBR0HqYe4ZSwu7IkZwdmy9lig-uty7FD3-PJktRJGAeqzv2ZUlpgxiJevJcz79_6psHvIeH3Gd73uPQe8Ni6l1wk5rbayuiqhzUzC7afFhl26oStJJoGinni5d2iN_H-cCyYbaPHtgEOFVqgLiawFLTYSu4RrxftrG9lUf3hAgmJJCiIM7jDybUsF-4_aSU50qoAfXxxtiS_Ov0oNhj9c4betAMcP87HGcA3Gt3-gmYXqu6-l38QwRSO0tuuPQlYm_qmwlN0cK-13wFmDo5wHMgUm1vsSdOOQKsHMWyxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنهایی نتانیاهو در سازمان ملل برروی دیوارنگاره میدان انقلاب تهران
🔸
جدیدترین طرح دیوارنگاره میدان انقلاب تهران به مناسبت سالگرد عملیات طوفان‌الاقصی  با شعار " روز به روز منزوی‌تر" با موضوع پیامدهای جهانی و انزوای رژیم صهیونیستی اکران شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/697197" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d702b7e656.mp4?token=VS43bHUwnyzhks2H8rzdGH2KKZiVZHkdKXqY_XndobyAhnPrd8VH9_eGSv-gxDPufvfivn_EWsDuIg1S47ggBXZVJ5e-swI7SDPkk6-nMiF0TKtwlz6cRES6P0xHdT5RvuafofBiv6bzRLpbNprD4UUfTC6RjNba_B7aX_5uniiZuCK-FGqCflmwBNfjqJumV1JI-N6IszLZ9hIGPAGjAa-bt5Ffi92KPje0XsNXy4jxIzfCwe-sHfH5McAHN23oz3I85hHWN1wrxlp0Qrkky275MCHVA1IAt_Tdsn0l33UI2NZme2LGQ6trFDEsOTzpH160zsTgSAn9sFrrFiCUhzbzMvqeaGCVGsNSTQevrmd2krf80RCoEpUIl-GxjL5ORaOAMjGsOpJ9V-90BIp62nL5XpiBvb6aWajgjSs9vUjr-xbPuUl8ZPzR7dvIhPmNTkEMs91JEUxlkKrxwj91ufp1-bj9c0Ja8EwbeOC-sByZFqiwQXxXom1soMXb5fujcwD6QmrFw-2kKx45U69TrdPlfR2oRPgDKyBgu0g1TVkWOR2Weyqxbq4Nzik6wwfcMjbr9DtEdP8xG6MFd3d4nvb5rrqlSu9DnftIgOkc06MtZVT-OwUqc1qcCBNymTpWm-zLc5LwC2Ioeum5wPO99SC35WolkuEwQ-XogbDT3Nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d702b7e656.mp4?token=VS43bHUwnyzhks2H8rzdGH2KKZiVZHkdKXqY_XndobyAhnPrd8VH9_eGSv-gxDPufvfivn_EWsDuIg1S47ggBXZVJ5e-swI7SDPkk6-nMiF0TKtwlz6cRES6P0xHdT5RvuafofBiv6bzRLpbNprD4UUfTC6RjNba_B7aX_5uniiZuCK-FGqCflmwBNfjqJumV1JI-N6IszLZ9hIGPAGjAa-bt5Ffi92KPje0XsNXy4jxIzfCwe-sHfH5McAHN23oz3I85hHWN1wrxlp0Qrkky275MCHVA1IAt_Tdsn0l33UI2NZme2LGQ6trFDEsOTzpH160zsTgSAn9sFrrFiCUhzbzMvqeaGCVGsNSTQevrmd2krf80RCoEpUIl-GxjL5ORaOAMjGsOpJ9V-90BIp62nL5XpiBvb6aWajgjSs9vUjr-xbPuUl8ZPzR7dvIhPmNTkEMs91JEUxlkKrxwj91ufp1-bj9c0Ja8EwbeOC-sByZFqiwQXxXom1soMXb5fujcwD6QmrFw-2kKx45U69TrdPlfR2oRPgDKyBgu0g1TVkWOR2Weyqxbq4Nzik6wwfcMjbr9DtEdP8xG6MFd3d4nvb5rrqlSu9DnftIgOkc06MtZVT-OwUqc1qcCBNymTpWm-zLc5LwC2Ioeum5wPO99SC35WolkuEwQ-XogbDT3Nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍂
💦
جشنواره پاییزی سرزمین موج‌های آبی مشهد آغاز شد!
🔥
هیجان بی‌نظیر، تخفیف‌های باورنکردنی !
🎢
بیش از ۶۱ سرسره جذاب و هیجان‌انگیز
💦
دو مجموعه مجزا ویژه آقایان و بانوان
🎒
تخفیف ویژه گروه‌های دانش‌آموزی
🏢
امکان عقد قرارداد با سازمان‌ها، شرکت‌ها و ارگان‌های دولتی و خصوصی
🔥
فرصت استفاده از تخفیف‌های ویژه رو از دست ندید!
📍
آدرس مجموعه‌ها:
👩
مجموعه بانوان: مشهد، اندیشه ۷۹
👨
مجموعه آقایان: مشهد، بین اندیشه  ۸۳
🎟
خرید بلیت و اطلاعات بیشتر:
🌐
wwl.ir
📞
05136008
جشنواره های تخفیفی ما رو در کانال زیر دنبال کنید:
https://t.me/wwlpark_ir
🌊
سرزمین موجهای آبی مشهد ؛ پاییز پر از هیجان!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/697196" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رئیس بنیاد مسکن انقلاب اسلامی: سقف وام مسکن روستایی به یک میلیارد و ۱۰۰ میلیون تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/697195" target="_blank">📅 14:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eubod0mqRlLBHyXADlrqgMU-u0m7nnWIssYpR4yMS0rFUjh6u4hRf0GGNikwZBtmvOBFh_PR_OjYXNxYqOMRnpcF-lmxSdNMk0NSmeW5lIg0sc2qbgfCRdFE8fJkVS9wHacahNGX9aT26jfwblNsBAzE7ImBLgi7wUtB6rmkSDAZZKf2NI7QmHtml3TxVgF0I_a-PlAyFfFB7YijfrjugSkhMKoIfLC4Qs09r5E9iIwLNTnzYIG37-GYgfnR-IaeQrRI-PbcK7Oio-QNflwl309t8P0dLDPiY3OxyuU1jLaP-N6JOgRr2J5hgK6K5v5lEAUYkcpRtqc71E9tqWO-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGn6o19u_2KeVtEz0D_7JtK1TYO2G7W8NJQ-opOqZ-eVgvuUx95ZUCR6BW04WH783TpOnW9o--VDZOFpzvQ8nqAIZ5SIHA1V2-FnsIPIpzJshsp-0G_h4BnOEnVxVyxvzSPffJa_GznqaCzFoSBmeKUl6ohYTjuR5MZa5XczPF6rMBadZY91HKODwwGqRZqeM-55MMgaxT1pZQ6rCB_GJNLdGBfGjxGmyA66z2aEZobK2gg_M-YaOEqTuPYTQ9YUeWkjLrdPrSRWVBQ2h3S-M8jU1CN59oW5uWXf0j3W6w7glO_TLKBFIz0HEdx845IsiDKD_Gw7OgfeNRs9D6mY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M64QsW2DcwS5FpGcWAupO_7rU2D0tEQ3MwElxo7RABquSrFr_eplFX7IRx1aJNaY450Q-e1DqxZssD_y0azHx5_S0gP1WI7YS8WDas8UZE2f50pOmV2-WClfXolg1CDo72XO3KKAHn3YmrQlLLx0xdNF4htM4aaUJmFkdHWeZBP1TZlGhh39RR5DZtQYBroZTGAkTbhdQzX3vB2QagQTqD6uFqUUXEYnT7QtaTnzPlAWL1_wXNSm4QrpvpYQ3zZfDY4oWyZGAJS-fCiJ-dCCf-50ro-kwRf1C5lPsQC3Xps0n99hKYKubmwQMuosghW_jgvTWkq7d6ifi2Qr4stIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JouwhaPya6_wy3Qj3DO2tpOE1uOFfRIoQWvmvjLwwR9eRfu4HDOjh4YEhMxy4ITp2ni48fS3JYYLH6rd6QWp5f1iyBHCSMT6tk3zI94VEnPok6NvKK4A69tR9Mdnkpl5DGaMj6JkVpCVpQEeKTTBmYFeK5-4bb8-VpBtxfoZc3gVsuoajd2Yzz9DqAfMdlKIYQwnKY3_12LGvgMYEPkMKA42wownJk_3SYuHjjDHMHSUfZujv3AlqnCYk53AjGiFhXlS589_5y9cSXwPE-XxBVp2YF6vaKipQzIqW5QGbA1Een-PAwE6140rxm8M7GEh3v4XmKSRjCiLgXUYL1Myfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRIc1ARuyH4DgLXnlTbKvRTYrUgOtF0f1LyXl8bW0BXMO_RotXOi7_8qlwsFfUmG-be-jPmcD2rP5U16DWG2GzLW5DnyKsFFqjcE9Lnv6XizgDO3UBassm7u5_IS2wAmZIik3RBfmhJ3tsr0f8RFYXDAaXd6Z1-_n5SyrDHqgCgwTaSddmKdg2iuSfHB-3PFdQLW_XvUJJ2fuGxAro8RRYkZkSNevsu77jh-lMank4BZ2cxllNyPJmkIKYp5dMvqzDwR3BG2TwzzLsBwHmlDQw0jfWQQH8jI5dgNMCqe_62H7TrSvtq7UbJ7LUWDjwX38eiRoQZ6DlvdaSRf1ETVzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طبیعت گاهی آن‌قدر هنرمندانه تقلید می‌کنه که چشم‌هات باورش نمی‌شه!
🦜
🦋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/697190" target="_blank">📅 14:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOFDxPnyULI9K2rOqrRH8fWrOPE2s8M2AhaJgQGUJAVgEnmxwMe-FEqREjcT7moQG-1RqWVbniPMP0Ud1fGuQ87z5fPEZfjwWhqyZjOWwc1ZZvgAmHKzeozWsVjLAZnV0t1echlMApNh19fZoN5ZnX89XDfsMaUW5909l6CmzaXWxkvaFnOc0J0yZXTgv2JMqnvBlfqe6MbxmXF4B-L_O4jq6YhC3oKsNTRL9CsdaEHVTBbIWXzCRSsU9lNTMY0puO5ZCye40M_mQ0pwhWwUUSwustagOvd79PmZjTMEi4odXg-imwA83yL_obWCATQX1kyM6X_Y81J8RqzFNT0wcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالملک رهبر یمن: از آغاز تاریخ عربستان سعودی تا امروز، شمشیر نقش‌بسته بر پرچم این کشور هیچ‌گاه جز علیه مسلمانان به کار گرفته نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697187" target="_blank">📅 14:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697185">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20ea3297f.mp4?token=tglDIMKqUILbPhRh__HvqRx07jcZoDLUdrtTwZeXMsvBqBGV-FjXdhrwsc4WS4hnHiRaOJcfKmunSDhvjk9lwnwZ1Yga73qz5bmnJWftVPVNz3LWE3M6dVofCav7pvhMyX6I1bm-FUOY6OQnNf9PnX7ckwbCLE76o9xZynvm_MEqXovsa4tOqFatIpH6Mlv1n8Q-nU8N0zLRkzLo-eElIN8Kwlach1tTbfolrNuH3aWVl2zBriiac5mOTKT8q4IFmpeEieAIJVFNMr24OT-kkm2Bbj604nxInWU7Pw844Cg2ywq3Kmd2fXvMbpx0WslTkZFUi96OyUOZlJx9hjRL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20ea3297f.mp4?token=tglDIMKqUILbPhRh__HvqRx07jcZoDLUdrtTwZeXMsvBqBGV-FjXdhrwsc4WS4hnHiRaOJcfKmunSDhvjk9lwnwZ1Yga73qz5bmnJWftVPVNz3LWE3M6dVofCav7pvhMyX6I1bm-FUOY6OQnNf9PnX7ckwbCLE76o9xZynvm_MEqXovsa4tOqFatIpH6Mlv1n8Q-nU8N0zLRkzLo-eElIN8Kwlach1tTbfolrNuH3aWVl2zBriiac5mOTKT8q4IFmpeEieAIJVFNMr24OT-kkm2Bbj604nxInWU7Pw844Cg2ywq3Kmd2fXvMbpx0WslTkZFUi96OyUOZlJx9hjRL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای همچنین نشان می‌دهند که از مجتمع گاز الحوية در میدان الغوار عربستان سعودی نیز دود بلند می‌شود، این بدان معناست که اکنون با موارد زیر روبه‌رو هستیم
:
🔹
آتش‌سوزی در مجتمع گاز شدقم (احتمال استهداف)
🔹
آتش‌سوزی در مجتمع گاز الحوية ( اصابت قطعی نیست)
🔹
آتش‌سوزی در حقل الشيبة (اصابت قطعی نیست)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697185" target="_blank">📅 14:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697183">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
آموزش و پرورش مجازی شدن مدارس از ۱۵ آبان را تکذیب کرد  مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در #گفتگو با خبرفوری:
🔹
درحال‌حاضر هیچ بحثی درباره تعطیلی یا مجازی‌شدن مدارس از تاریخ مشخصی مانند ۱۵ آبان مطرح نیست و برنامه‌های آموزش و پرورش بر آموزش…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697183" target="_blank">📅 13:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697182">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a6ca658.mp4?token=MxVSNIxzSO5uCp3KqXr6I1i9Fkjx2MAktcdxekK1hHLm9laC4QlhRd60ae5Mz9kLddW8aS_zHM2SJN6BklNq4UfJdk7Umh8wnfxPHLilCCLsdoRRVlHlAmfwn2z2GIXEgh_di6lkxetUV75oFCh6E2OhLd9wSM9mR05PrnQR3Nk8-RefhTZk_N4rkIgTejG9E-xNUifKYy71Jk7X5RS-3DR_7Fok0GcZrOTQDfxuxAqq0-wGI25gWgR7C63f3IVtEQQUFydf2c3dH7z3O44--fjEBADaWHNgDuJkl8_RcO75x5YbGJIOOiF2FVh7uthzwfuKBXdjYkgUbBB1jhr7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a6ca658.mp4?token=MxVSNIxzSO5uCp3KqXr6I1i9Fkjx2MAktcdxekK1hHLm9laC4QlhRd60ae5Mz9kLddW8aS_zHM2SJN6BklNq4UfJdk7Umh8wnfxPHLilCCLsdoRRVlHlAmfwn2z2GIXEgh_di6lkxetUV75oFCh6E2OhLd9wSM9mR05PrnQR3Nk8-RefhTZk_N4rkIgTejG9E-xNUifKYy71Jk7X5RS-3DR_7Fok0GcZrOTQDfxuxAqq0-wGI25gWgR7C63f3IVtEQQUFydf2c3dH7z3O44--fjEBADaWHNgDuJkl8_RcO75x5YbGJIOOiF2FVh7uthzwfuKBXdjYkgUbBB1jhr7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌ها و پهپادهای یمنی به قلب ثروت نفتی عربستان رسید
🔹
منابع عربی از حملات ارتش یمن به منطقه الشرقیه که ثروت نفتی عربستان را در خود جای داده و دهها چاه و پالایشگاه نفت و گاز در آن قرار دارد، خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697182" target="_blank">📅 13:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697181">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt9HNMcHAIR79SpKkHBijbfuMDPPnugHspqKmmv9RJ_UmRkj22qL9IQaEmQMWhdy1cYjMMEHE3t2oTGa_HAnJPzG_RjTPYbOUBcG8aS0S1NLDdaGOMQ79_Y3JDrDhzjslzNPriIStN1Jwd0iVv_ScojlQBCuTeACLcdYfXj_Y0lFFXM3cxZLMKFfK8778CPPqwVkc4i7U_6jDO_qd8XhYvApFoNSyFw7v0JtCsx-P8eN43S6mbcqN20dyEDaO_7Hc2H2boY-4No7FMLvzsHD9gj4Plxa5BcTilbCtfr0-PU4CMaC6dRkKumyD8q2zj-cjkzbRdRhDFY-h3lTgHH6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، کیتی زکریا را به‌ عنوان جانشین کارولین لیویت در سمت سخنگوی کاخ سفید انتخاب کرد
🔹
نکته جالب درباره این خانم اینکه پدر پدربزرگش ایرانی بوده و به ایتالیا مهاجرت کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/697181" target="_blank">📅 13:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697180">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سردار رویانیان: بی‌حجابی اگر از حد بگذرد فساد ایجاد می‌کند اما نمیشه دخترها رو به زور باحجاب کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/697180" target="_blank">📅 13:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697179">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31974bb27d.mp4?token=cJnj6XgOqcClSnz55TA2AHAHAYXFiiKuQiK-z_17jzjE2GiB8St5MHK4SXw0bDrhSgXrAmexgEmrwBVg4GTEH-sZ7EP4j0tVwGPpQP4hrdjWjfJDs1ksBDO_tzH2rzjS6AhyRWp_1b9bwBh1gVIN5Eq664gpxCypdEWtI_lgtVPauVpAHIwH6bA7pEceXJuUPdF7xqNxCEZV1TgQVorUcRj6k-8VfwjmMxReVjSPrc25D3DlXX38YXeCk1qYCKXMne2lX_TXyq68qBEz1V_grGPw7itTYf1QYLcxLSBuAKhvA-pHdUnFo4yrLQugsomkclCgplcAqAfOVY1DzthPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31974bb27d.mp4?token=cJnj6XgOqcClSnz55TA2AHAHAYXFiiKuQiK-z_17jzjE2GiB8St5MHK4SXw0bDrhSgXrAmexgEmrwBVg4GTEH-sZ7EP4j0tVwGPpQP4hrdjWjfJDs1ksBDO_tzH2rzjS6AhyRWp_1b9bwBh1gVIN5Eq664gpxCypdEWtI_lgtVPauVpAHIwH6bA7pEceXJuUPdF7xqNxCEZV1TgQVorUcRj6k-8VfwjmMxReVjSPrc25D3DlXX38YXeCk1qYCKXMne2lX_TXyq68qBEz1V_grGPw7itTYf1QYLcxLSBuAKhvA-pHdUnFo4yrLQugsomkclCgplcAqAfOVY1DzthPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاییز شیرگاه، مازندران
🍂
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/697179" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697178">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWcxJrml_Y61Atuj5vPcl1W0yBjr0IpazWq8XmlGCweyPlNlpoBIgXCMsxIR1Inj6Ej7RP4UfQfiCwQpOvzAvIsCPMmCVeZMHHKEW_CQXrqEWHBXCiMWGXTRSRMUCjpo6zFtW67hqYd-TxdIH8dTsnKLlbAY_rcRsoKKLP1k5CR9_iID9OM94sdexNETqkzUT78apOdcB3oZ7yHbdzkCnbSpCaWhdZBKhFbdsbvRkX7CsNlWkUpabRmYDFN3_yTT76klLHugF4FdjhwR6n54m0fCA-ysm2AKqtRgcfHffrmMnSdMF8PrqknNdQcDB1P7JeDvhtukNLdMkQWDBQaraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
«اگر کارخانه دارید، قبل از اینکه برای سایت، محتوا یا تبلیغات هزینه کنید، اول باید مشخص شود مسئله واقعی کجاست.»
🔹
با یک جلسه‌ی کوتاه ما می‌توانیم بررسی کنیم :
حضور دیجیتال فعلی
مسیر جذب لید
ابزارهای فروش
سایت و محتوا
اولویت واقعی برای رشد»
رزرو جلسه شناخت و مشاوره دیجیتال
https://digitalcast.agency/consultation-landing/</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/697178" target="_blank">📅 13:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697177">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw74LjBZKMA7xjOmyY4iS3yM6jewcjIhBwHkdlVX2odwHkV5A5jpVaHBorxcQYHKS36URgzk07Mm61rxAPhGpkL5WMIGzmN0L3tlhoa6txBWFaQg9psS9lDVJb-BlDd-ehjsX6_QbCWuLlgmDY01AN35vx-x3X7BvoURmpJN_O6_nneMmQgzGPSq0faO65RvJUZN7QAbH8EGetRpmedEs4BtiNWqgdAhBttlfjMWXxKxI41mZiPWhU38K5qauIgkFEoIJymhk3O2mi7Ab6dUxPProPWjwbi4wDThL4YbQ1rAZwvfmvu7dOFdgJFXhEd5BHV1MSJadzmZoGcS4igzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر پربازدید از اعتراضات دانش آموزی در فرانسه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/697177" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697176">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=rmZVALsfBZ1panFdXNI2o6gL8hD1foPavLBlbriym99IBuTnEpx1Rtoo33ic4n5DWUUh6rN2cp0LdmTmH1UX5HTMlcgOCdlKLpgWo7MWSs8AE3fSvk67hxOzCqQiOBvgV999c_tkZPaP0ghvI3IOhUttdOS8PQTXfCHPyHKb0BpTBF2zK_cnGRIrt34Ni2y5bZ5ac4_yh6SYcSMu0e9yXYEUmAecKnWPewbRHZZtAbrjfMrmii0dgEziZVhPmqpYdMaEikLev9akoCsJBTzW5o9Il5-yjm6hP8-4BVxMSqb67dQu8KWheFv3lAJIisOvf2D_f7b7kkrUQ1qnH-wdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89eb24a75c.mp4?token=rmZVALsfBZ1panFdXNI2o6gL8hD1foPavLBlbriym99IBuTnEpx1Rtoo33ic4n5DWUUh6rN2cp0LdmTmH1UX5HTMlcgOCdlKLpgWo7MWSs8AE3fSvk67hxOzCqQiOBvgV999c_tkZPaP0ghvI3IOhUttdOS8PQTXfCHPyHKb0BpTBF2zK_cnGRIrt34Ni2y5bZ5ac4_yh6SYcSMu0e9yXYEUmAecKnWPewbRHZZtAbrjfMrmii0dgEziZVhPmqpYdMaEikLev9akoCsJBTzW5o9Il5-yjm6hP8-4BVxMSqb67dQu8KWheFv3lAJIisOvf2D_f7b7kkrUQ1qnH-wdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهان باز کردن جاده‌ها در پی زلزله ۷.۷ ریشتری جنوب پاناما
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/697176" target="_blank">📅 13:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697175">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCfcYQIOBAJSc8CBl1dP-2Y8VhTIGn8bKaVMOf3GMsg45K6YuiRixG1adBL6z9Ch4PtH6bOXMx53jWqUwZ-3UJZlXW2avPfsq3Q6uisFm_GXkjESJHhQP9OcpcAMQcyq7wBKRTx-F1fXHYTDFEZMbD8bppSGwcmfbQL4rIP-Yrr7E7XVY1SJxzIVU-I1mM7fDsfot3So7fND9o3VuhOE_5j8qO1vSXzTapTgqJX8WadDtH22fDimcUPM-kYRnEhWHk-TvhsJcjyYHQOBljcWCpyFuSeasTViM6MmS1azBXNMq16WOKU1tW3spSGd6AbnVk2B4iT79Ln8yUnFAiXLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذاهایی که فاسد نمیشن رو بشناسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/697175" target="_blank">📅 13:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697174">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95c8d48f9.mp4?token=qVpVELAr1siUOQemMvT_Xa34oKdTFANl6eJhQOznYkUGv-So1_RGWecqlQWqhj9nXATrlx4OymQtPcdONvkpM8jXlJ6i7BAf3JFhGDh9xJ6hMK51DqwTjGqH_GmcaHaZmwOQ4rTeyWMcGmUtpQncoMbLL2TYQ6GR2Jx_JgAg67TEHnn9yXNSUVPCd-cei_Cc1no0Ycqsk0cGMo_XQ3znufeiYqHd2LS4VR5lRXSYQx3U3YgG02PFaHpX1OGY3_dIVq0Ok45pyVrL5TP0_hMjehmZFR41KErgXFXGLJaeaAr8n8M0rQLaFRr0rKiOBfWx-WkZ_lwTgVEheRJC8h5aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95c8d48f9.mp4?token=qVpVELAr1siUOQemMvT_Xa34oKdTFANl6eJhQOznYkUGv-So1_RGWecqlQWqhj9nXATrlx4OymQtPcdONvkpM8jXlJ6i7BAf3JFhGDh9xJ6hMK51DqwTjGqH_GmcaHaZmwOQ4rTeyWMcGmUtpQncoMbLL2TYQ6GR2Jx_JgAg67TEHnn9yXNSUVPCd-cei_Cc1no0Ycqsk0cGMo_XQ3znufeiYqHd2LS4VR5lRXSYQx3U3YgG02PFaHpX1OGY3_dIVq0Ok45pyVrL5TP0_hMjehmZFR41KErgXFXGLJaeaAr8n8M0rQLaFRr0rKiOBfWx-WkZ_lwTgVEheRJC8h5aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیلاب در بخش‌هایی از شهر انگوت از توابع شهرستان گرمی استان اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/697174" target="_blank">📅 13:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697173">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ‌های یک میلیون تومانی آغاز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی از افزایش ۵۰ درصدی کالابرگ حدود ۱۱ میلیون نفر از هموطنان خبر داد و گفت: در مرحله اول امروز حساب کالابرگ افراد تحت پوشش کمیته امداد و سازمان بهزیستی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/697173" target="_blank">📅 13:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9d065a2a.mp4?token=sG1GBc3m7TybY8iSvUFjIVhzTPJgqX2fWUvl0SJG-RSGHp95mRcU8DOJdXHjH507mFq_lTPMyRgdmZXri3dWdpSrTXZIXHYG3yY6i1Q7jMcVRBPeBFNn9JsWsGbmbIOlGcuhHyrX_aZAYCZCmraoR4H3P8mh3RQbBC-UOJkqO6Xtb33p-9jZTKLwjw2lASaPN3VKqm472XV_1jXG7JQwgVr3HxO-Q4Q2p_ksNt2EK-v0jtNqF6qgVqncMHQjAcOye7oWuIIXutivC5dEPkA6ocZvdEOQmP77L_Blot6VeDPg3Qh8tT6KvzFKqlP-pgabDIJHzBvZ-wbBvaBDUeFvlKQpCPzf8GcuhcV3xdBnfrS46GHwOHKw0g9IyO6GySqPHI-U821m-m7PvD3HXxxqO6UZfgrOp107ITZA1CyzWJGlX3snbM1L0HhLOoikeBIvIiR5p6vHR3cVmkE9FOHtzKg4a2kWVkwNPEr2-si6cbpl-egFMk80SjZkrs8F8JlZXrcwL3kiWc9kKRwGwkdYnt2K67GfTeK2rPsKbE5-K4TMmZo0sIKbkNPtWwsn_CBfNEhUSdISVa_LVpiTqznsrWzlPa7ZasvoGhyuur0HG47y4St6CGHh-nN916a5ima6yIMEAMMj8ohkzMSkuOB9JIId0MSTZQDHoPrZ37eY0VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9d065a2a.mp4?token=sG1GBc3m7TybY8iSvUFjIVhzTPJgqX2fWUvl0SJG-RSGHp95mRcU8DOJdXHjH507mFq_lTPMyRgdmZXri3dWdpSrTXZIXHYG3yY6i1Q7jMcVRBPeBFNn9JsWsGbmbIOlGcuhHyrX_aZAYCZCmraoR4H3P8mh3RQbBC-UOJkqO6Xtb33p-9jZTKLwjw2lASaPN3VKqm472XV_1jXG7JQwgVr3HxO-Q4Q2p_ksNt2EK-v0jtNqF6qgVqncMHQjAcOye7oWuIIXutivC5dEPkA6ocZvdEOQmP77L_Blot6VeDPg3Qh8tT6KvzFKqlP-pgabDIJHzBvZ-wbBvaBDUeFvlKQpCPzf8GcuhcV3xdBnfrS46GHwOHKw0g9IyO6GySqPHI-U821m-m7PvD3HXxxqO6UZfgrOp107ITZA1CyzWJGlX3snbM1L0HhLOoikeBIvIiR5p6vHR3cVmkE9FOHtzKg4a2kWVkwNPEr2-si6cbpl-egFMk80SjZkrs8F8JlZXrcwL3kiWc9kKRwGwkdYnt2K67GfTeK2rPsKbE5-K4TMmZo0sIKbkNPtWwsn_CBfNEhUSdISVa_LVpiTqznsrWzlPa7ZasvoGhyuur0HG47y4St6CGHh-nN916a5ima6yIMEAMMj8ohkzMSkuOB9JIId0MSTZQDHoPrZ37eY0VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/697172" target="_blank">📅 13:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6560e7755c.mp4?token=tbV0Xz20ucWQRldOCsPJ6JHiuAbU5ag9ym7Z5Q4V8fKsQy7C2sGpA603WF0gizSAVQEIhV2AhIZFeCzy2Y13EpzpJPGl8B8eok-XfBHCBmhynxn6Z9oc76KAQOT4mfF4fmDEhi96MEQZ9GpwJEVcrXrJ4XAt3-jLmS8MdhkDSY4eDnCF7EGJAXzuYtbfrNef_EF3zjeus0jqb5X7orKbJA2181MvRaCdS9UoFbdnEwQpOh8QoR9xKhu5Ew0MD-UVFlzUl0oaiGx4WsWaCSnceNLhVKUPWTXLczpXaKKuzpVdYZNGGB8mgaYEKfuk1tEHWZNpAjnL4U7t6w3ui-erjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6560e7755c.mp4?token=tbV0Xz20ucWQRldOCsPJ6JHiuAbU5ag9ym7Z5Q4V8fKsQy7C2sGpA603WF0gizSAVQEIhV2AhIZFeCzy2Y13EpzpJPGl8B8eok-XfBHCBmhynxn6Z9oc76KAQOT4mfF4fmDEhi96MEQZ9GpwJEVcrXrJ4XAt3-jLmS8MdhkDSY4eDnCF7EGJAXzuYtbfrNef_EF3zjeus0jqb5X7orKbJA2181MvRaCdS9UoFbdnEwQpOh8QoR9xKhu5Ew0MD-UVFlzUl0oaiGx4WsWaCSnceNLhVKUPWTXLczpXaKKuzpVdYZNGGB8mgaYEKfuk1tEHWZNpAjnL4U7t6w3ui-erjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تک درخت دریا؛ وقتی نخل خرما در داخل آب زنده می ماند!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/697171" target="_blank">📅 12:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
افزایش اعتبار کالابرگ‌های یک میلیون تومانی آغاز شد
🔹
معاون رفاه و امور اقتصادی وزارت تعاون، کار و رفاه اجتماعی از افزایش ۵۰ درصدی کالابرگ حدود ۱۱ میلیون نفر از هموطنان خبر داد و گفت: در مرحله اول امروز حساب کالابرگ افراد تحت پوشش کمیته امداد و سازمان بهزیستی ۵۰۰ هزار تومان شارژ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/697170" target="_blank">📅 12:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پوتین به ترامپ: گزینه‌های دیپلماتیک در پرونده ایران هنوز به پایان نرسیده و دستیابی به توافق، امری ممکن و ضروری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/697169" target="_blank">📅 12:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTHw5v0axqOAZ-PFqGx9lLVP9aosbeWvvKTSY0JPijBse19OLtGPe8jUGFSt0YF02pwtYnM-kaFLE02wWDNip1yMZhL2AoBM1Xlk7RIXqlIZ6KOOtcMgaO8NIRzpniw7mZ27pWjoAhxcm7p4N3MtTLu8HcWjFiPuaoG9yj_bVUXkikaTIZTnQ6FEtsWi8rxcJJkc_THl09QEgmrnVfvGtCsDDxJY7AEJYFFoJWy_DwWXNSB00wdQjhw_ZFOv1IPb61qOfUGAn-q_WjlCl73y9EHUuhUx-p0cYG7p85r4fAE2yPffIlofLxSg7Hb0yZe-I1t_mwXzgnkOl_4Qy8Q0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
برج ساعت حرم امام رضا (ع)
یادمانی از طنینِ خدمت،
آوایی که قرن‌هاست زائران را فرا می‌خواند.
روایتی‌ست از لحظاتِ حضور در صحن و سرایی که پناهِ دل‌هاست.
✨
مشخصات محصول:
▫️
ابعاد: ۳۱ × ۹.۵ × ۹.۵ سانتی‌متر
▫️
متریال: پلی‌استر
▫️
وزن: ۱۱۵۰ گرم
▫️
طراحی خاص و باجزئیات
▫️
مناسب دکور منزل، محل کار و فضای فرهنگی
💰
قیمت:
۵٬۹۳۰ هزارتومان
⏳
موجودی محدود؛
برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697168" target="_blank">📅 12:46 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
