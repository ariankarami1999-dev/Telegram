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
<img src="https://cdn4.telesco.pe/file/OVmEd3_krpBPPz52Ay3BjEMPIvFNtYYtnEpNUqj6H57cVFgOOz0x4A8_tqojEk8LTGIHXG2izU4hwnWMol42fHmDR9dhpweat4v7SVjlMPTHApmIeCAjydF9WHhAILcdGIFEkeXWWve_RsGzKSBbk5bwWEfHsNRYKWZeWbRtQsrRQUgIEYTVrYiMPBgNbwJSLhfsgRE9GgyprpygdV1kDsR_b7cpGNMlHI83VsndwE98JyTnN9mT9zqwAx_DGg7CDJ_6hhBFLTU9wYRTe8Zv794p-wzY3-UbDK2POAK5SwnXaOKIo4szAubNb2j_eXUDE0dSkGktcuKq0Txd28iAmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-65715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/news_hut/65715" target="_blank">📅 23:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
باراک راوید خبرنگار آکسیوس:
ممکن است مذاکرات در چند ساعت آینده کاملا فروبپاشد
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/65714" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
آکسیوس:
عباس عراقچی، وزیر امور خارجه ایران، به میانجیگران و ایالات متحده گفته است که برای دریافت پاسخ به چهار یا پنج روز زمان نیاز دارد.
این ماجرا به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد که در طی آن، ترامپ به طور فزاینده‌ای از پوشش منفی و حتی تمسخرآمیز رسانه‌ها در مورد وعده‌های محقق نشده‌اش در مورد توافق، و همچنین انتقاد تندروها مبنی بر اینکه او در قبال ایران نرمش نشان می‌دهد، ناامید می‌شد.
بدتر از همه اینکه، ایرانی‌ها در ملاء عام و خصوصی می‌گفتند که انتظار دارند برخی از دارایی‌های مسدود شده‌شان از قبل آزاد شود، علیرغم اصرار ترامپ مبنی بر اینکه این امر تنها پس از انجام برخی تعهدات صورت خواهد گرفت.
این مقام آمریکایی گفت که ترامپ از این اظهارات ناامید شده و موضع او تغییر نکرده است، اما خاطرنشان کرد که ایرانی‌ها می‌توانند با شروع به برآورده کردن خواسته‌های هسته‌ای ترامپ، میلیاردها دلار از دارایی‌های مسدود شده خود را آزاد کنند
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65713" target="_blank">📅 22:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آکسیوس: جمهوری اسلامی امروز به هیئت میانجی‌قطری اعلام کرده که حاضر به برگزاری نشست سه ‌جانبه با قطر و آمریکا نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65712" target="_blank">📅 22:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
خبرنگار الجزیره: حمله هوایی اسرائیل به حومه شهرک زلایا در غرب دره بقاع در شرق لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65711" target="_blank">📅 22:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0I5g9W5hqWYNrObgybtzrbC3MY2Qk0uAofXtQiC7ygWIdUwp9tfVh8CbWi_aeYEdlEPOjb2xfWmesAZNdph8wz0_qlAImV6tmUzneqC2eoLUM8MKS3P9bUACjylehIFrBj1eMqaJ1Wpf9kSzspfH76E1jWiv9KRAYFQOAkHkNfr8mVjp1AsuMmm3DcK4RhGibApy4ksoncVompnMyBRM9Mg580sCWCtuaxhNLv7n3UHw06D2JzOGIQAcyKkr3cqcpqk4A6Cg0tr8DyGz0thamNx-y5mPRLME9zogS2HWyk0fxXJQll8RJ2_TjFbEZoZJa08RGRBP-f1mWPUzzhNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم عزیزی رئیس کمیسیون امنیت مجلس:
ما از جنگیدن با بازندگان نمی‌ترسیم.
تعداد تلفات آمریکایی‌ها بسیار بیشتر از آن چیزی است که ترامپ تأیید می‌کند و افزایش خواهد یافت.
این بار، جنگ محدود به منطقه نخواهد بود.
خواهیم دید چه اتفاقی می‌افتد!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65710" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_A8IwkdDYpJkZwakK7aAorFqOUcXhkIX2YGbH4KDA8Y_bVOFnqR6GkErkUmi8Vzdm7K5YXIu_XMoSIDt48HvyM3_GU05CYromp4eH-C19oXnQA6BNcTNIXMhBy4LyprBaOUjRm4BfyTc_pTgX5LGnROEToh8ExgMZNPL3qc5Srnb1EfGKhlm7cziq1p2aCv1k5iPTQe0vNJ3kgMuKLVk95ko00ORQ6g8_KzBiYJpR8umiUoTblqeWEdKmF15VtYnZiZeSc-epgLFv7KM3ZVZPDlw-URgl7A7cYrflG0qvqezhzll415dIjOWb6VZayAkTor3kI05z6q1TK6i9gx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
آقا بووووو میااد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65709" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
جواد خیابانی از اساطیر فراموش نشدنی صداوسیما میلی، اعلام بازنشستگی از این سازمان کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65708" target="_blank">📅 21:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjrEnBM5eab9U7ikKk8v-abiAqnYvV1Ynquh-GgvdFNUJ1GBAYewYH0C2omPRYc8KT_BUUjtfbOkyzz0sqY2k6p2Oo5X9lryc56Q8S2qAc-mKoS14ht7TEIMLf2OteDXjQhTxD_NIHSObfgKBrO19u6dZpMO1tYQAdBanVIRCef_Ne_j9mqErhHvt8jwktscvApIKJ0TLqRWK6AdDypZR5vKUGg4mL0u4e57oD957HNFZke0Jx8dlN21OAK9OLYbodRhNCHRJoC-mIqsolRJ338GqhXY0SC8tPreL23nbpxeQG4SsPwL-7XvePsbUjbqNzpTA7S0UuyK8nn0R0ApDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پست ترامپ:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است
!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65707" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه! #hjAly‌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65706" target="_blank">📅 21:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک فروند بمب افکن B-52 بر فراز آسمون عربستان داره کص‌چرخ می‌زنه!
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65705" target="_blank">📅 21:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
ایران ما، امروز بیش از هر زمان دیگری، به اتحاد نیروهای ملی خود نیاز دارد. با یا بدون حمایت خارجی، سرنوشت ایران در دستان خود ماست.
ما قوی‌تر از این رژیم فرسوده و ناتوان هستیم. ما مصمم‌تر و استوارتر از حامیان اجیر شده‌ایم که برای نمایش‌های تبلیغاتی به خیابان‌ها فرستاده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65704" target="_blank">📅 21:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65703">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
⭕️
رسانه‌های اسرائیل: ارتش این کشور درحال تدارک آغاز فاز دو عملیات مشترک غرش شیران با حضور مستقیم ایالات متحده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65703" target="_blank">📅 21:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65702">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OY2suJPlbEOqhVV9-vHDw2Xc5wYR-HQonb0myILZhLuclO1zQyLJFfMXHMYt291J9uhjQpfXpfzQz9gKQOw_wJVD79uwFV0m1ijhiaAc1bQbD-So23C1ozVZNlABgU6ChN1gjYcY1lBonnJ0uSXUq8aJRW60IP90ddeT20j3i8-7tdcsZCc-QdkvsOykWv7HeyMTq17dC5hpTBOxV7FzWaGzIn695wc8-M-LhG5nAEwz07NQYpfVSeb6Vtc-HEv1YjxZJIncESzDTj7zKXCvhtQwJpPSeAlL2_iMhDZEUQ2pYP-sTDBsga9C8Mj6qFfDvmfQ9--LEcFQ48ajcFOff-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
♨️
شبکه i24News :
انتظار می‌رود ایالات متحده در ساعات آینده حملاتی را علیه طیف گسترده‌ تری از اهداف ایرانی انجام دهد که دامنه آن از حملات شب گذشته فراتر خواهد رفت
هدف از این حملات ارسال پیامی به تهران برای ارائه پاسخ فوری در مورد توافق پیشنهادی روی میز است و به معنای بازگشت به یک جنگ تمام‌ عیار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65702" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65701">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c979a7db.mp4?token=ZKjEPfWTV8gplY9Gfv7Eh3oYkPAovAAi_gqKvo2ELLV0BmmGanEnd451m0yZb3viBK5zKb6JaSEilJPn5yecLmMb-TKTBvny-YEzsouI8aD1b6KRmhaYw72Ws_R-JaeDxDwHtoYQN1-lSLH2S_ghl2sL5W-JTAtAcbgK2wa_Sq3fPXSCXkvvXGLiU4larDX-OKsbB5TgS8vwfXIszsBC24cNkQh0csPw3Mw_CpxbTW-Gm_5k5E_DD2z4Q934T-Eia8ZNTvntn3Da8fAzYNdVNQ2eE2opeisFCjqI628hrVwSFnG9QvmI-4srsVAMKemMI3PySzXHaItEtmMlqdVAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام ویدیو ای از هدف قرار گرفتن یک نفتکش مرتبط با ایران منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65701" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65700">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گروه هکری حنظله وابسته به سپاه:
به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند.
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست.
ضربهٔ ساعت‌های آینده تلخ خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65700" target="_blank">📅 20:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65699">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
سخنگوی آتش‌نشانی تهران:
ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65699" target="_blank">📅 20:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pReXK04u7JrubxCGaohXEj5gnMSJqg74wyHpjM59FH8qJIiT_58szZs8vB_3qbXVbcMKHd950NY7Z5tW7o8x_k0MZXEkpOMamnctkzJ6K5nk_to3aFQEoQcqyMMmDN3P-JDoZ_3it_JqBAAZj9i81GiDb6PDVGGACNqT--oQKI9jzynVp1aPVDDj9CwKNwA6Jiemus5jCzH1Or0Wt3JSBWkKB3YIb3Twhp4gKxngu7rpjNItcl19SFcOA3HLDByw3b4w1Lh3BTmiLRgH4yI86ukmQjbCjTXXP6umDk44CiGELPJ-gr8w8ND28dopBJg3v0QqelepfOWmKLRotQKIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ساعت ۲۱امشب «
شاهزاده رضا پهلوی
» با مردم ایران سخن خواهد گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65698" target="_blank">📅 20:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
رسانه های آمریکایی:
حمله به ایران گسترده خواهد بود و بدتر از قبل
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65697" target="_blank">📅 20:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNZeUbPcCyaaBeByXjS2C5bSH74G5JrR8-QbLmTJs-HgNLQUuHWx9WNJoGyk_4nS4UFBHm99e8WJMa7KWK1IpujhK3t-DBRt28Pr11D2b8LgvD0RqLeuaT0uUZjB1ynmrxrto6EijTXUzlgZHI-TUfVH9bapfn9lR03RDaRoa0Zxvzper7SSbqaN4Bn0nFHe-e299r2YDsdO1pnziHmjAVU-bIOX_FahojuTb4ZcOKMpVaeADysdtiTiqoZDBjrkCdNT4b0YZAI4qivOvUpQqiUDGRgQPxlmvu3Ubiw-9fHf-WxX6YaXNSRpSFZCQhrAhoQKW04RX_n3Gb8PlbNzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در خیابان قیام تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65696" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است.
حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65695" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ آمریکا: عاقلانه نیست که جمهوری اسلامی بیش از این آمریکا را به چالش بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65694" target="_blank">📅 20:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=kSJHplVstW-Hal6H3m2xVWo2aKSzq1q6uZCREeQvV0KxYCEkHeglGSKFoqqmE_Ekhea-Yr4c_aRhOrD0EMkQIu6HSlOb8bEY47R_nLdqxmM4nICYgTKYgIpnOMnaIQEfxpmDe5zkPy_Yb-GjZivLp4lPRlm3beJ4Jihsr1GJUwoT2e-Y9FbiWtUDt7j7XOt4_y6gurEcRtmnfw3f5QUAipHVTpgZJtRyRRQrENCB4AGI1Irq1_Ifwmw8XoPgvwEhtqbVtTotDllXJed0QecWJNqn5IUnASPcpgHPIOYl1qFeM7ryOT0A4mCWjb-x9yzR14u55iHHwEDRJdGKqDweQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=kSJHplVstW-Hal6H3m2xVWo2aKSzq1q6uZCREeQvV0KxYCEkHeglGSKFoqqmE_Ekhea-Yr4c_aRhOrD0EMkQIu6HSlOb8bEY47R_nLdqxmM4nICYgTKYgIpnOMnaIQEfxpmDe5zkPy_Yb-GjZivLp4lPRlm3beJ4Jihsr1GJUwoT2e-Y9FbiWtUDt7j7XOt4_y6gurEcRtmnfw3f5QUAipHVTpgZJtRyRRQrENCB4AGI1Irq1_Ifwmw8XoPgvwEhtqbVtTotDllXJed0QecWJNqn5IUnASPcpgHPIOYl1qFeM7ryOT0A4mCWjb-x9yzR14u55iHHwEDRJdGKqDweQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ :
به درخواست پاکستان، به ایران فرصت دادم.
فیلد مارشال و نخست‌ وزیر پاکستان افراد فوق‌العاده‌ای هستند.
ما جلوی رفتن پاکستان و هند به سمت جنگ را گرفتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65692" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65691" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDPHOwNSwi8oSZAADCcb0ILHBRgwK0Kp30dA2mLMtv65AmN64nUkYpAA-4XlR7oIz6R78VtROIKfh66cg64Q89ocjr87oVGOMqj2zXCOkxbiXfjRvswryiFJ--Jv1evIsCxHWFdPZgWdKX1XY9sTIQMQlpeJ60Xp5Zs39ERWsHt2t6tYtJz0IG2T6-54Mi8vS06s4oZu7h22I9yNb6CNDzuqPMShERZdKxVqRK99GdS5AI_9S1GU8MbjZNkkUASX2Xy2kCZdz54IrkHhKEqVSpS1CLZpwzmQ8bV8Gu7UWL4R7M00tLVHMDF5WB_mlV0Igz0vLCQqjP3UQNsv6sMkIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65690" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65689" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: همه‌چی سر توافق نهایی شده و فقط مونده برگه رو امضا کنن، ولی هی وقت‌کشی می‌کنن و امروز و فردا می‌کنن. منم میگم باشه، چند روز دیگه هم بهشون فرصت می‌دیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65688" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65686">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اونا فکر کردن من رو هم مث رئیس جمهور های قبلی می‌تونن بازی بدن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65686" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65685">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19aca716f.mp4?token=Hfi1A9d5GWLsLA0EGop11GTgsYj24XOAS5YQLmuJjrDU7Wl5pTZ4fqImDScYAjuLJUI1S9t7VzWcK4_Z50o0nTFnBrmvEmYNea30uS6iBQRLeSkrCQZTUWaCiH85YE1OFkn9OEBei3e-e0OI08SoCg0y8v0844iKhpTIOCMeb-MOJfFeYKdIOUlhshycm2AJqyHtL8TSpINc7wJXSo0IssXUw-XRV9f7WABFvy_WuhCjxhAgHwS0AdllblUewtExdWyew_g005jxn7OjuN52XG_7yHEJy-HMH3VpZWyZrPGAl0KtFc_jdZX4ppogDIIJByxInnRB2qMuwjWD7Zuj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19aca716f.mp4?token=Hfi1A9d5GWLsLA0EGop11GTgsYj24XOAS5YQLmuJjrDU7Wl5pTZ4fqImDScYAjuLJUI1S9t7VzWcK4_Z50o0nTFnBrmvEmYNea30uS6iBQRLeSkrCQZTUWaCiH85YE1OFkn9OEBei3e-e0OI08SoCg0y8v0844iKhpTIOCMeb-MOJfFeYKdIOUlhshycm2AJqyHtL8TSpINc7wJXSo0IssXUw-XRV9f7WABFvy_WuhCjxhAgHwS0AdllblUewtExdWyew_g005jxn7OjuN52XG_7yHEJy-HMH3VpZWyZrPGAl0KtFc_jdZX4ppogDIIJByxInnRB2qMuwjWD7Zuj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: دیروز به ایران ضربه زدیم و امروز هم می‌زنیم؛ اونا فکر کردن من رو هم مث رئیس جمهور های قبلی می‌تونن بازی بدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65685" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65684">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa5IL5KeZ7pZgSePlbvs2oxaC6nAZ-ApfIMLom4iaE-rPtNcbsVYslsuE2eLHnjIzc1cZsK4WcCK480AKZNgjfk1pncpfEYQKNyT5bPhPF88z9WE-EQEdbf5BP_Ysib1vjb8x7aVGtCFaSK2caDLMh4Cv17VOCCa8O0wRHr06W70szUPDaieemxQA4jOVP4rl5jLYS3wy7IXYcFwG5sr3azvteC7gyCSkBQQ-hE3AF_w5DxRcYcaBxsk-SaJ5TTumZPxhXMedmsmbthw9sjCJNoniHJblxrvtN-BAe3PYkzaLq2lLClG7QTZjtMJS3irU8CqOXnmYerK7tBaaqaKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امارات متحده عربی روز چهارشنبه، حملات موشکی و پهپادی جمهوری اسلامی به بحرین، کویت و اردن را به‌شدت محکوم کرد.
وزارت خارجه امارات در بیانیه‌ای این حملات را «تروریستی» و «بی‌دلیل» خواند و اعلام کرد که هدف قرار دادن پادشاهی بحرین، دولت کویت و پادشاهی اردن هاشمی، نقض آشکار حاکمیت این سه کشور و تهدیدی علیه امنیت و ثبات آن‌هاست.
در این بیانیه همچنین آمده است که امارات همبستگی کامل خود را با بحرین، کویت و اردن اعلام می‌کند و از همه اقداماتی که این کشورها برای حفاظت از امنیت و ثبات خود انجام دهند، حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65684" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65683">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. بمباران را از سر خواهیم گرفت. ما حق انجام این کار را داریم. آنها هلیکوپتر ما را سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65683" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBWP8t89BwTJmgxbLgfu0naZsLcCTWzJORYAvZxQ7NG3rw0ISvccXZsWrsoJIM8Y0A1X6FBCYKW_NcnmzI2cPqYD-PwVYhy8nQqOqo_BI2YXQOrabX81mryDIYQ9FAYy8WvOLztvBfhkmBlNA4qEd-XArcwruS5fjH7eqEGCYGmEnO0hsKN3I2BVowTKQnHLBzHelv9A7DId8Zsr_GjWX0Zf3mPCFh9VtROEXCYtstdMros-wadX93_YF5rIeOjiNdgWOAbMh8Vc3DShe4N4xhYoLVEUrkQOeyU456mRc4BrdUixBtKhsUeg2pkGOHpx0sXKGSilKk5vSJrh4ql5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZewzgGt5P_CROBzSY1cpV0xVDmqMR6pwQhhCWU4paTEjU9M9vUMoTJFBWPcuJhUllxr8--s16F2YAP4M8naTHgEIq6MZV56jX5E8Lptmn_mUBxE6lfd2jujJu4iGWiNow3y3bZCCmpiTl9owMKVyfGTzyamFbW3x4U9f9oPYdmET6lrXL9pXGM7LZfOZWdRa8NSo2zyGsfglKqmyznkFFcAUPCmgPLDEjnAsMSZRusXCulC0Qhju4CaPcdFSyAsU0t-fnB2KPiijDPks1UqojdebO1dH5JDIG0GX4MaDUQ2Jkzb2cM-PSdZOFOHsN55u2Zh8zzBckX6pkNTIDteLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت (خراسان شمالی)، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65681" target="_blank">📅 19:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcAF4ORU6WZKnrd0wLlHVMrtzhNg6wmXTQOd0gjnXvhT6iw6cAzZnyf-8ZpqAC8tM698BYUiEfYNPf027_i-DsnLozQa3j0Qx6L96kQji3JdnRnXMxluo2LCN09k6rgLv3fPENUfM4foqjnyKQif2z-VvZVlqNlmcGa7rnRhUrbJkULso1oM1XlNzSgNg6mvp61p5OU0dnHMzBsdcBLguEuo2-VP1Ma7Hyrf1y9sxz_-UqsQ6cgcZXCvB3bWS8QOTzXBiKgxjyvWd2AkrkINiOCWBUkpwSL6iIQ9tzQOEtrZDZofNzS7RpsEP6p0YGon4LgoOqFIsBvW-1JBdV4bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حمله هوایی اسرائیلی در حومه شهر سحمر در منطقه البقاع غربی، شرق لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65680" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
نیروی هوایی ارتش اسرائیل ویدیو ای از عملیات ها در جنوب لبنان و ضربه زدن به زیرساخت ها وشبه‌نظامیان حزب‌الله منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65679" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
؛ تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
+یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65678" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT42jJhYlox83F4PY-FMLPWVX3J59o4akijI7LNID4KnUUKq9C4LS-lYca50g9IM4vxMW6-djJDOPKj3vMxzSaGgT2kquOryKLVxOUedaoJXCFV81mo3V_UjNBslmvWIIVT4ZNHiSwV6GBh293uMg_DGARKrPhu67OzuMZKFsllJhmfYaP0wrMHPA3-YWumv0mUHKUZgi7tQ0nkR0NZsbd0oZ8SzyD728ZumBZKcF_3CHAdS-m1plDb_YJNeTMs4KlTfTMzJi-bieJo_QrT39Xa7hy4AebdLM7Jxr1jHpZ1mY6QmsebxQ4O7m8ibiSYRGtjutS_l4QBcmJqfvfRkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انس جهانی طلا هم به ریدن خودش ادامه میده و امروز هم سه درصد ریزش داشته
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65677" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !
https://play.google.com/store/apps/details?id=com.barkovpn.app</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65676" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا در یک سخنرانی اضطراری با رسانه ها و مردم صحبت خواهد کرد.
جزئیات و محور های این سخنرانی هنوز اعلام نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65675" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC6ObM7Z8jbMWh8SF-GemDCve8OYD3rBohgBHdSZr6qhSEKpwXDi9y7K8AAyQ3ozDRfVv5g0gR_1fh_ZN0Mt-AHtlVg_Xa0o_SWP78YYo4i6tc8d5G-j75ecg6ApwUYfxeDj0lWsBY-_R5zfP_LTktpKs2fkfPmsf1E33C5eSW289_i625RaLewMJW0DxsTKgOi2XhgIm8_9cHbgqgO-h6_YOi0vdl4NoJet1aGpAT0VK3pXqo6HWSnaGtWHu-NlXf20u_JrHIBQnMzFclNjJF2ex6A8qc-3T-j3CtxuoUNbBRfRCyvOzvQmfbPupaM2s_Mm4WuVdkkYJucjgz4rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو:
به اقدامات قاطع خود علیه جمهوری اسلامی و نیابتی های آن در منطقه ادامه خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65674" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwlUIOCQdrE-LcXRuhJhqQ46lFG1rogpBsKrnYXybwHdCV7SRp524zmHyuguVnU98BXdhua4Wgm09MSjwgMPIZpJCgfM-yun0TCThTWCy6fFn6FzZVrnrVrgKhdIls-Ox3z15eDGozi8-MGl7RDz29zpI36LNOVeCnSwO2FMZ1rPI84CywXejKPpj5mQeriS5sro8SUXswOkFL-ahOGXIazUHmj0XkPTeuu8fGo64TN2Ek4Xy4Rb2BhkVtffTACH499Bn_p8VCJF1ZCGVVj5nlQbGm7Fe8m5BVatz61cNrhRdNh9kgTsrsMnQJ8CDKUnmhUXXDyjs1fOCKCBGy4hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب گذشته یک فروند بمب‌افکن B_52 نیروی هوایی ایالات متحده در پایگاه هوایی فیرفورد بریتانیا فرود آمد.
با احتساب این بمب‌افکن مجموعا سه فروند B_52 در ۲۴ ساعت گذشته در پایگاه‌های نیروی هوایی سلطنتی بریتانیا فرود آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65673" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EcZzrjvFoS_kJkaNLsBcMXwbtGgfv8e5lzOC1u5vUjhMznanUBKqkDC46SpPdquED1uVzgBsCytfVIx367Rx1_KBcr68mLsB7yNTk9ACV6b6mRIbwbJqH7wH07wpWxw1eICjbqImk-XZps2AXkt790tvc35HPmdo9c5EXKgyZar0HNTCe3muJTTvCdgI4FtApjmrx275eNgpKLaFUshSAqp00JjGEtoRkzCV1RcRUuGOCdjVXbqFL_JLQH7W7kecCYZdMyHHWwk1zGIyVQn1s3gU2jo2pNVEqdbfpPKkK-V-MrmahhcqYdI8TeUnaJOSz3cUKeMuMZOqX3Z3ZhxZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۶ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🎁
| کد تخفیف : 40
▫️
5 گیگ 30 هزار تومان
▫️
10 گیگ 60 هزار تومان
▫️
15 گیگ 90 هزار تومان
▫️
20 گیگ 120 هزار تومان
▫️
30 گیگ 180 هزار تومان
▫️
40 گیگ 240 هزار تومان
▫️
50 گیگ 300 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🗣
| ربات :
@OPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65672" target="_blank">📅 17:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=CA2sh3SpL8gmsYyjMAeh3DaN3klJVH4pCzLKB6HVfZM88pGA9bGGDpHwMpox3opWdly5l9rg6jinXQIbvFgI8n4s3xUYn4FJ4zeRFZYDGi6xKTTMxrzG_Af7dbPhSUK-1eZTSbKplZYSvYnFN0b4d-5sJffEoxQaTvlzLlaww8zTySYm-FOTJeNqfJUk7zqW8Qi5vOv3owdB1B-qtltZtcFiNoQMudDuE-e08aFKOkzQ_d1pCYOCYCpuyg9-Ul3ovMXcB0IM6Dl8wCdI48lQXWg_ilLcELHJnhZkqUExn8zfHGGPlKMeY5iS4Vas_l_ZYlDchJwWL1-8zJzFA6vk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=CA2sh3SpL8gmsYyjMAeh3DaN3klJVH4pCzLKB6HVfZM88pGA9bGGDpHwMpox3opWdly5l9rg6jinXQIbvFgI8n4s3xUYn4FJ4zeRFZYDGi6xKTTMxrzG_Af7dbPhSUK-1eZTSbKplZYSvYnFN0b4d-5sJffEoxQaTvlzLlaww8zTySYm-FOTJeNqfJUk7zqW8Qi5vOv3owdB1B-qtltZtcFiNoQMudDuE-e08aFKOkzQ_d1pCYOCYCpuyg9-Ul3ovMXcB0IM6Dl8wCdI48lQXWg_ilLcELHJnhZkqUExn8zfHGGPlKMeY5iS4Vas_l_ZYlDchJwWL1-8zJzFA6vk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🚬
تو مکزیکوسیتی شورش و اعتراض شده و در فاصله یک روز تا افتتاحیه جام جهانی، معلمای مکزیکی به خاطر دستمزد پایین ، حمله کردن به محل استادیوم افتتاحیه و ارتش وارد عمل شده تا جلوشونو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65671" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65670" target="_blank">📅 16:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=DLauXrSVi51y34DtpL-5gnzvJZ48WKWivD5grT19Hj_SZ50Cx2L7nYMfEuW82VMMPdwUAsEX3cv8f4d62buSxnPANGqPiMURhrqeMGPefIWkLya3_r5nt7d6cja45B9ozMQDDvlTGqVzaoEXKN8Be_fygHY9ug59791pyJ5e75eVe1mgm-DrQcENS_86_Zl8yWGq61vePNGD1G0gb9kxiF9gkCTK3mcZKRg13Q9zw909DmqbbeVCqEKu86z9p06sfrA9THY3507SON4itvYdUH5glx25aJKtomOWj3_bl7A0bCs5N24dfu-oT_cVI6tVHfh8MH1JabVobpwTCIQAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=DLauXrSVi51y34DtpL-5gnzvJZ48WKWivD5grT19Hj_SZ50Cx2L7nYMfEuW82VMMPdwUAsEX3cv8f4d62buSxnPANGqPiMURhrqeMGPefIWkLya3_r5nt7d6cja45B9ozMQDDvlTGqVzaoEXKN8Be_fygHY9ug59791pyJ5e75eVe1mgm-DrQcENS_86_Zl8yWGq61vePNGD1G0gb9kxiF9gkCTK3mcZKRg13Q9zw909DmqbbeVCqEKu86z9p06sfrA9THY3507SON4itvYdUH5glx25aJKtomOWj3_bl7A0bCs5N24dfu-oT_cVI6tVHfh8MH1JabVobpwTCIQAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جزئیات عملیات نجات دو خدمه هلیکوپتر ارتش آمریکا؛
جنیفر گریفین، مجری فاکس‌نیوز:
مقامات آمریکایی مطمئن نیستند که ایرانی‌ها قصد هدف قرار دادن بالگرد آمریکایی را داشته‌اند، اما گفته‌اند ایران در آن زمان چندین پهپاد بر فراز تنگه پرتاب کرده بود.
دو خلبان توسط یک «کورسیر» نجات یافتند؛ یک شناور سطحی خودران ۲۴ فوتی با برد ۱۰۰۰ مایل دریایی و ظرفیت حمل محموله ۱۰۰۰ پوندی که توسط شرکت «سرونیک تکنالوجیز» ساخته شده و در زمان وزارت دفاع لوید آستین، تحت مسئولیت دولت بایدن به کار گرفته شده است.
این اولین باری است که ارتش آمریکا یا هر ارتش دیگری از یک شناور دریایی هدایت شونده برای یافتن و نجات خلبانان سرگردان در دریا استفاده میکند.
«ناوتیپ ۵۹» اولین ناوگروه عملیاتی مجهز به هوش مصنوعی و پهپاد نیروی دریایی آمریکا است که توسط دریادار برد کوپر در سال ۲۰۲۱، زمانی که فرمانده ناوگان پنجم بود، تأسیس شد. خدمه سرنگون‌ شده پس از دو ساعت شناور بودن در آب، سوار بر این شناور خودران شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65669" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
صادق زیباکلام از اصلاح‌طلبان حکومتی بدلیل اظهارات اخیرش بار دیگر بازداشت شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65668" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ:
آنها فرصتی برای امضای توافق و زنده ماندن داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65667" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۳ اسرائیل :
احتمال واقعی و جدی وجود داره جنگ علیه ایران رو از سر بگیرم
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65666" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65665" target="_blank">📅 15:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBuCjvNETMPB4-dzliuVD2U6f5yks6zeXF6WTbNMcPrIUeGLsqIiHzJgPFhuvpQiF7tXDBD1nHehHqsvwvq5U0gVrziJHBkcNxjfSg2Y3MmbQwWnaYpHDboDlMiuKOftXHm1O_AtlD9vi-RIkSvDfzKuXQmX9UKbRo8Ih6MFg0T3vsyCO5CmyUUEQntCuuI2i6aC-kTNI7NXDKYDM7CykO-XbJN-CIkyX7Kt_VywT4yCk6gx_Yxp5YcCuRE1Z8rJnDQeU07xqNwn46z_1rqx3_SLCysQfWbOkA5uo6_C893qmISAyBLxeRvgZgfPL1atbNZgMRwIqYwQBurS5g_S1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید رو بیدار کنید این کاکولدزاده دوباره شاخ شد #hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65664" target="_blank">📅 15:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqB2_PIiQFPpKXcK_k3NMBhpBB-8HL1Gyjbv5A1oAUxYV2KWa_5Nq-n9-3LK8Dz5wIrg_afKVbBmk0u1si9iTl9gbYCp0rUTLukDD7S0sehKWua9GojhKMrx3fyceyFnuxG6BZSx4ywewTYrQ--tUsN1K2h7OWj5sZ17QSWLIANtlaas6cyQas5LaLm5C5KSWoUkKNnau3vXe81yhcAov_X6lrD9u0M7rnd4MTIvZpxUF8uNtnnNYaTurXRRu3mD0W7nYOETDr6wjbTlqLqVdta9A1aovsJ9iAIGkJJ22GILZZj-jQyhTeQu1X5vDuGejE9pvfrY54pzoqU0ZFI_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
رسانه‌های خبری جعلی از گزارش دادن درباره میزان اثربخشی ایالات متحده خودداری می‌کنند. محاصره دریایی موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است. هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران تجارت نمی‌کند، ارتش خود را تأمین مالی نمی‌کند و هیچ یک از صورتحساب‌هایش را پرداخت نمی‌کند، و به زودی به یک کشور شکست‌خورده تبدیل می‌شود! نفت زیادی خارج می‌شود. الحمدلله!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65663" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65662" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:
به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام.
ما کارمان با ایران را ادامه میدهیم و به جلو میرویم
.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65661" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ:  ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65660" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfRZ5ZBX-mBf1XgARIlXPBOWUdTIEJ9JQ7GwUAEpJohbayKehogZvipR7ZP0YcHQ3qE5q4H_FAvMGouXyteikEaHVVEsb1hjZxnyLluQfODyoa6jH4Ml9y5p5oycnqJhfyo19Vj2xPblsGWSvJjShhXB9nFXLOTNyXzZmZImqMLKPsHcwg_d2MXlVK0eaXlVObqAboblw2aAiyKz5nJ043Uo3kEM4irwzd0dYRZIm2sxFNTj7xafGUMeAy9PHytLbrVLLphblCnppfbEBt0t-SQ_tgn3R8OQQ3SpoiLBek1HAUPVK3sGxvm1g5VolG5fYVBzAWyhAkX1Cy0wtSqCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ:
ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65659" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=TcRY17u51hTLStqGP40SxF9tI3L486Ae1XJg91P-SZOPTF14IQUp2TsnuWQ4cIN-qZhc-8PUUVAZoh68nHmLOC0mD9oDAx2PYq-s4B8BGlqlBNtiyTG6qWR827m7H8PStH0mH81GK9mhNtr-87QlzGAYE2Bi7q8ArwNqJVl2ykAyXSWCrsbBMFiVPnBTk7JewPhOrzLSsD_oyY2tPlXTLSyssk1iQGCtwJT8yY-Yclem58149-9fPjTYc69b4-zKV_pLAgrFwgYMooI3M_w1boj-X3evg6PMmcCJpE275vdeljLHRUvD0tP_xvYzqUQ8kx5GZHiw3MKrK-B_BxQUtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=TcRY17u51hTLStqGP40SxF9tI3L486Ae1XJg91P-SZOPTF14IQUp2TsnuWQ4cIN-qZhc-8PUUVAZoh68nHmLOC0mD9oDAx2PYq-s4B8BGlqlBNtiyTG6qWR827m7H8PStH0mH81GK9mhNtr-87QlzGAYE2Bi7q8ArwNqJVl2ykAyXSWCrsbBMFiVPnBTk7JewPhOrzLSsD_oyY2tPlXTLSyssk1iQGCtwJT8yY-Yclem58149-9fPjTYc69b4-zKV_pLAgrFwgYMooI3M_w1boj-X3evg6PMmcCJpE275vdeljLHRUvD0tP_xvYzqUQ8kx5GZHiw3MKrK-B_BxQUtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگ جدید تتلو بنام "رفتم که رفتم" از تلفن زندان که آخرش می‌زنه زیر گریه....
⬇️
دانلود ورژن کامل و MP3 آهنگ
⬇️
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65658" target="_blank">📅 14:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b931b462.mp4?token=SQdgPj7D0UNp-54bnMQMq2vZEb4HetZVZrCiTJ4Pp8hJ6PVBr5PFkc3pfZ9Btk-Pet-Q9ROIKe6Nqdya9-oPzux_8NGIFSWQHjTu7q7NZhw-e42s6vidAdWGoitHvuQYx8FC5452qXTXK2C_I3WLIMcPadpUZWEj5VDF07VCUQ1HPmrIyJOX0bElt4wtDLMp43a9PqIm8ccF6VaGScOSL9eDPY_R3IULmnr3FcVsT549kV-FvkzwAWjM_8OgAy7XrEQONg5k3JdTbRETlGe3_XZfRtIF3ZFJ-IVmyDXZ2UlhRv3sMWOWBKUiqC41Hgjc4eCHtR8-KNxWg0c5nBYrvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b931b462.mp4?token=SQdgPj7D0UNp-54bnMQMq2vZEb4HetZVZrCiTJ4Pp8hJ6PVBr5PFkc3pfZ9Btk-Pet-Q9ROIKe6Nqdya9-oPzux_8NGIFSWQHjTu7q7NZhw-e42s6vidAdWGoitHvuQYx8FC5452qXTXK2C_I3WLIMcPadpUZWEj5VDF07VCUQ1HPmrIyJOX0bElt4wtDLMp43a9PqIm8ccF6VaGScOSL9eDPY_R3IULmnr3FcVsT549kV-FvkzwAWjM_8OgAy7XrEQONg5k3JdTbRETlGe3_XZfRtIF3ZFJ-IVmyDXZ2UlhRv3sMWOWBKUiqC41Hgjc4eCHtR8-KNxWg0c5nBYrvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که این خانم از خودش منتشر کرده و گفته؛
«دختری که مدنظر پسراست واسه ازدواج»
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65657" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=ZsYGhAR1Z0UgRBzPxbCcxhX0RzqevuI3ho323dWLgU83HeZf5XgLy_8REu12OXyhR05no-s9KZ2tNlcrFW05J_wGRTIlYidsVaN_2Xtt4K5j0eAsrDTlDDYGxDqodmcldjy8GKEs7nY6P1jwYQAwgweq1KSX2nE3Un1Wd4lWORVkqBTiRQRm_w3MWD9eVpteG16uSW2zotgoqnoe5gTpReqz2e2wCpZnDI0lB7QEGtq9SsQG7HHdTD9L8LMWaoq81Iu5ucGtfI3XEZMg0e87zjPDbwJIMOgtoDJpFeJafOIHzQMf9hNzSwomnLeqZUeZZcp7508dMnHDnXRcAsal5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=ZsYGhAR1Z0UgRBzPxbCcxhX0RzqevuI3ho323dWLgU83HeZf5XgLy_8REu12OXyhR05no-s9KZ2tNlcrFW05J_wGRTIlYidsVaN_2Xtt4K5j0eAsrDTlDDYGxDqodmcldjy8GKEs7nY6P1jwYQAwgweq1KSX2nE3Un1Wd4lWORVkqBTiRQRm_w3MWD9eVpteG16uSW2zotgoqnoe5gTpReqz2e2wCpZnDI0lB7QEGtq9SsQG7HHdTD9L8LMWaoq81Iu5ucGtfI3XEZMg0e87zjPDbwJIMOgtoDJpFeJafOIHzQMf9hNzSwomnLeqZUeZZcp7508dMnHDnXRcAsal5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران شهرک حومین‌الفوقا در شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65656" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQJqH1g6zobglnSrA1fns-rtVkT7AQFiKLWqI4Yg9QEHEH8JG73TG-_UpCU8kmE6_aiLrimXzNldAn_pfIIhkx75RKurbyVFEuWShvcmVpXs8gFWmwcVtteZqsaGg5F2_P9p1ldTXpHhdS39J9zTtEPyqQcAlGGukGSYn3FpAGB2J3eiALbaKBF55KUw5AGAr1s8kGrU0QBVTtJKiSxzmCepA-iCDjBiQ4N2kGwC73-v-BEdwcJEeCaicArFEfdG7YabVW97vJvp-IyVfuMiWp5rFMU6g0Tfo6mpQpEISTMjOYWoexeSm-hvOZpn47De6wMhXt-hfHjIPwq3Ft2OMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65654" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65653" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5KIEVeP3aWs5S-RGpAIu-mlpq07aQL4HDAHHmu63n_NBH9J8F_U1BkXagKtM2V0fvZ4kVpbvIG07u3RC2u3YnRX3-eAPrgE8u6VMHrj10E3LpdKQcmgzCdFlvQFEP3qX4SJHiX9UsWS099yDiA5t0fygaMHPqs5iygmq_wCjudqy524opwg0TU98RGQBm5T859J97w4T3rp2Z_9HREDuwjwSiaJUvNVBs-Qb81TyxouJ4lYUUEwh8zQ8h0pISRQY8Iu_5Z-mv86Vfv_aPz13T8QhAd6eAP86eTpDiBViCesTvmQv6cnigcMHYTIHPGRlIL5SMUFRW-5wPypgsPa4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65652" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXmpoX7TeW0cUTDLSA35rABosPDOIJEOF69PBcW1QpGwCAn3JwA60WG565KgeZjedfaZBZnxuFPMQbAUpL2DF3h6xR1Hkf8I0vW-2ZUSh5Sl0N2bNK0F7PrLRyvFh3k09COgRYN5ApVKVtQWoEK3dnBR2vDt4RWytkaSBHMAgtsGLd5w3QeD5HOkerjPnqGLhM-7G_jvS8h5gbhdsOs3WkxiHRClYT2Z-YmaH8UqUxVDi9CkrUwKVius-vEBLLk46kZspFxE2dHbbU3F_ko8CLRHffg42sbEsuNzZCjyusVY2a9nuHy7iLIMRN76ZDVipdAWgcffMryKBh8TptyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاتو پاک کن عزیزم
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65651" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65650">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم  این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65650" target="_blank">📅 13:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=dt-1422bSbbkGGFlHLvgbmL4kqMJuc9L3oJiZdKVVp7ZF_dAnXCBBuGete-iX4HB8OPcEjFaIJBTMHKUpSulRXTkImPbr5DLxz_Z8XtTJxt1jfbBsGOYZvmwOu6uPjjoOpmF8tsM-g8VwSo6KfE5hDjxlcabu9NdMso6wLHaySBBYOT7FDX3LaN4HMaAJnHHWW57ErP1fY2PnAYaICWtVPLF_rE9HXVyOFxfTMCENxD1BOwRxMZapbzy3bQKFfUre7KDBqnl5-9faa4u6SwzbR7jVSlAGke70ylodJny2lz6K-2mLt0L-vERL-_Za9yfLr0seMsiIZKQ-vwEKUC0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=dt-1422bSbbkGGFlHLvgbmL4kqMJuc9L3oJiZdKVVp7ZF_dAnXCBBuGete-iX4HB8OPcEjFaIJBTMHKUpSulRXTkImPbr5DLxz_Z8XtTJxt1jfbBsGOYZvmwOu6uPjjoOpmF8tsM-g8VwSo6KfE5hDjxlcabu9NdMso6wLHaySBBYOT7FDX3LaN4HMaAJnHHWW57ErP1fY2PnAYaICWtVPLF_rE9HXVyOFxfTMCENxD1BOwRxMZapbzy3bQKFfUre7KDBqnl5-9faa4u6SwzbR7jVSlAGke70ylodJny2lz6K-2mLt0L-vERL-_Za9yfLr0seMsiIZKQ-vwEKUC0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده:
اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65649" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65645">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feI6OiuEGs2NMqcISA-PEzPwDfnod2obg6Z6pIv7K2YikQmsEsUyRYkgw7lsjJbejwqsV0wZfpkjPLeHDiy9DfGOXUs6TF08IZFdK9uLDZ5iEczybJTbd913LvlnupYWGUWYYw-Odo9z1Q2g5_kaktomaN8dwaoZoDafYLXFafCt1ysFWH3qM_U3l3FwY8C1AYYCW-NlnmT-KCVYPSfloMBfoFsrPaoVv-bkqEdtSuhoSmbL1JtKnG81lJOAe9JELCzXAdtnAeeJ0JmSZ2kGd7BE8T4BS1BkzQy6zCfexrT90treVUdf_NtzGCtzxVX8Gn1jB3hwtwJRHVTKYaSJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLAT9ywXx7t2tKl3W47q20feA5gOwiKO8N6HX1XIRWWFyIy0ak1O5fLDh8dT0AcatayduwCfn4Wi7tuftYsCxSbgbll6g0VKZKcjRY7ohjrtaph3oIkxTMfxI_G43wIBKA4VpHNS9UtpELEfCH58jRxbEQli4MlrSqn45ypYZSmf2meU-p2vAuQPjQ5pXN98jK6mzYRLlqMPk7XqrySc7k3VzqxMgTKikK5QsuApDW9NpVHVl5pyCMnki4cPpfFkte1DwXzdX8dehp8s4q1h29svF1I2IA6Xx09FjDdDt5tUaF6PI6eZpGvC3P6HhCc8egGV_7pLwumFaSH2P4gNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EM07TDUtpXguRNIhLt6FF1AOB1fmvD6OK_1hKP7jTQ-WEkRqR5muqYqan0snvI0jr6LyUiJTt3fNtLyIRoTq6Is_2AvQINdYihUO8TosQQ_FVmr5etEBn84LZ3r4cM7stmY7M77XOJ1TkrMNH3bvga-2Iy-HAFlx3vnRvuU6EuWrF8m9ch2cLkJu1XO0sW8Vr73aM8O94vbSHVcXd_kflL1iit70mQs7gX6VeEx2-6Dpov9dMBuoeZAeSoMIxTjmm0qM15oE7OeWnRbB5OP_ym2SH3_QG4zI7ngvUU5RXQ24v-xVky_kwxizgnsLeWKOXT63ZOoAF-wdK0GsGU1vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqAvS1ZmQ-5ISQClJlvDgeqdN3253TRJnQzesyOi7wqD_n0ZsEHjo819AZyfrRTGcPgCHi9Kq6zyl2Gt-0SkktXhg9ZGIjd0P_Li3Mflq2tEXBzvGKI511vtb2V5M1O_d9hFlP2nUSwG0SKiEC0NVp-YOkLSseTpah4xP5g8OeIsETQAy5sR-3qdGj_sL56gSSpUAZO9Z-iYVAHy2vM8dABhM8sYbnV8YfMMrUaxKOreWaKOEHLAPgwwdFGnNszHrxdUaZKrkJNaZqDzYLVMcadYfAoClI03w8Scs7yrmewFQ8EUwiOH9UFK1TfPm231ZTT6NK_ad5S0E-rRZ9b36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حمله به منطقه طیر دبا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65645" target="_blank">📅 12:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=JHWgm7o6mSqw6FWMyibyJ8rOBGZbNaju9w9pa-QhKO89Tp91DZF0PGhuTJ58e3f9HRrNtKXsqeRjwMXGNqUfPIVpkJFJgMnh1xjiCw7TLptXW_S9RBjdKzfEMhyM_kpn4Pbknyf1TnKXt8F6EZwajsl7fqm3tiR_c6w1YAqLqpQoPaWxB7_Yedy9sgMFQQDTNtF9NYrYAYbJZNsjKMxW-IjlU66PWoyHkDLemmDYBKW3dWN1jAbWKdW1xrVd956f4qPgjAjgo9B3nlhCU3762GXA2Ag0hvMY_wjTJy5lVSHLSNfQqIoxjLR_VjLzgPr7tuIWIKyrlED7NLHdD29ISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=JHWgm7o6mSqw6FWMyibyJ8rOBGZbNaju9w9pa-QhKO89Tp91DZF0PGhuTJ58e3f9HRrNtKXsqeRjwMXGNqUfPIVpkJFJgMnh1xjiCw7TLptXW_S9RBjdKzfEMhyM_kpn4Pbknyf1TnKXt8F6EZwajsl7fqm3tiR_c6w1YAqLqpQoPaWxB7_Yedy9sgMFQQDTNtF9NYrYAYbJZNsjKMxW-IjlU66PWoyHkDLemmDYBKW3dWN1jAbWKdW1xrVd956f4qPgjAjgo9B3nlhCU3762GXA2Ag0hvMY_wjTJy5lVSHLSNfQqIoxjLR_VjLzgPr7tuIWIKyrlED7NLHdD29ISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
با توجه به اتفاقاتی که دیشب افتاد باید وضعیت مذاکرات رو دوباره بررسی کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65644" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=Qnh8rc79pg71ypPMlQxMpLRNa-IIc8BnsEZ-3uDeX4j87ImsGAKnRTUfuu5jJLHxRqgzmo2-ZEAGz-jFhsFr2FbIkKJFy2h-BtrokXSF1Eyb5R4MUVNwgQmyYJ6qOeRymbWiWTMWelnnvwDxM0Q3Uj9MVfiTVg9iiJ89EWjmr49cIItuarf5HH0PIuwpPxQij1rgLhXdZ_xMtkvRK8M4eby35JQH8qebGv_gfpTFx55guwukaxlIsM_sDVKdSKQ0NZdKirMhumLGj4jXw3A2J5aGCzZzvnxesksZvxWd3a5DEXnYM5k-vshzxJU3ho96C2QuhJVR8hPZRcEpsxQSDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=Qnh8rc79pg71ypPMlQxMpLRNa-IIc8BnsEZ-3uDeX4j87ImsGAKnRTUfuu5jJLHxRqgzmo2-ZEAGz-jFhsFr2FbIkKJFy2h-BtrokXSF1Eyb5R4MUVNwgQmyYJ6qOeRymbWiWTMWelnnvwDxM0Q3Uj9MVfiTVg9iiJ89EWjmr49cIItuarf5HH0PIuwpPxQij1rgLhXdZ_xMtkvRK8M4eby35JQH8qebGv_gfpTFx55guwukaxlIsM_sDVKdSKQ0NZdKirMhumLGj4jXw3A2J5aGCzZzvnxesksZvxWd3a5DEXnYM5k-vshzxJU3ho96C2QuhJVR8hPZRcEpsxQSDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای از صبح امروز که حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65643" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1yJvo4EnvRl_PYkMRQuzkgJXEZx-oJgLWkI_0mMbRI0iEhJk_RtT5anfGCR82oJmXs_BA63kTVEFMBpWSNJb5yvexBOIhImV_l9XunN2DkbvFV4euGExcy2Ej7drRInc_KAqQv7ADI_p0h5tcP43HKOgnkfRw8otUpu5ZnngKG4OoNwNOZZWhmbf416M6IcH5pvAGZ2pCOlxNH72ccSCiI_R3uQ8L31A7TC-EjDRAx46FhWdxJvhPTh3eAaGDtjcWkSj_YSQK_M5S54B58pu2E07nT-TSc5C4i72q8vd3gw172ndOTjEy2x0EtSkoUJXasrFW3Mpue8U8bGZfzwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfZ-JUUiuyDnV7Y1ctTFEJXcUxnuIFiJZa-sWWMvaf5P--FbeogJU6xi0Lvjcj5T6ZQqIANkseg9UpJa3QNi_wo-MWVNPAnbfZ3zgStsdXNPP61IKEsM33CYTSJ9SoRtMtpIe4LCmblgSoi24ejrGijONAV0BC5cWUsvmMzAwBmaH1Nk6zu31RA-q_SFA9uM0_oVH9eP_HAENR0YXkKhlHVMjkBNxaC_yz5JzxYPzjzdTwbvo8lyI9Ek_kwamLNQHF5PYPuc7_P2g6wxzegkMXWX0m_TWQXHiwnCdr_7k3cjdNbeUXe5LFEKJbiNDFN5svA1eSiG3rKpteOFbOa7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmhn9msICfKNruteAYMhqde_U4s1mIIXlwjNeZNTmRNwT_ENULofKwnOiQlYDtvjRmOC2Xwgdf2uoRuNa8BpZaKrvWeWZ07XNItxVlVIS_evjmhtcija6dZn9uUsHPguDc2tr1oYSfBZgS-1yTV4xX_2-byURr8I_n5BDQsmOdeIdtGH7jgWHmTXUA6-0PjkvtoJxAkkLDJfUz3ZG4okvplxV7-ZU7iLMZkjNGUHMFCzbycHuWdxjnhWJYQ4vLjJx1q5Uv-mmnw4r3Gkde0IH56X-T39hWXC4dNK-Ef_HVtt5CPz9w_ZQZO5oBtdqmHGFKgo02qxVByWONJZqikcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdYav3cRi6dwXWOaPLT2F01pT6yi85ALmHj7aDxSLdBjNCCSlAtwEN4ndvnB_iB1c5madZ7YlJv3nHyDjUXVV_S_pXlYzgQyTHaxcu0Stjp6SUlKwoJ46PF1RRyG_hmEMICfJg9nhW8wLCeHwgow9_iDWE51d9Elzwp79cMMAOaxxaXunQJ7Mp6t-2hfWbRNaX6kEIRykUqrqjr-pNavF00Dd_ktCkTH8jseTch6g_VRvioe7luV5cRj0XDJDBX3rkoTBUXdpXr0LaFxux2ARceBLbJFXFNc1a9FYQaiu3cCKEBa8LUneWSXpYzrNwBEOXFR86Xv9-CEjECIE8QpSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حملات صبح امروزاسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65639" target="_blank">📅 10:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دعوای ۴ دختر تو بابل
😐
@sammfoott</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65638" target="_blank">📅 10:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwLt8P3NHGqbXWFMxJ6oU6Y3ttuy1gB8TsDYxePlf0KbOVtLHrqCEkIEJ_il1FSBdz5yfd__-w4T_4sD2Xv81L_0FLjdhSm0bqIO3lMVniGOUPlSVWHi7GnV_1HHFZGH-fCcOL_CWrexbBQ49n1gYljG_nFyOmc1LjqCO_AXW--kkF-q-f6rhniAmDRCaHxRmxCKf_ue1QZXWsNPm-MSRAHx2YB6lktqmIyDlVdclTHvPpHE_fSXZUaKhhdx2-Ej0E4-yEsrL1f4uMxZTlBXu1cl2sGfHmrRzNQcF9sVmVpRq9eooiGMQzdHt9MhyJ4e8zmd9DivEQ-nl8B_PcVHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری که فاکس نیوز از آرایش سنگین ناوگان دریایی آمریکا در منطقه برای «اجرای محاصره دریایی»منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65637" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😁
برا رفتن به باشگاه بهونه نیارید. از بی‌بی یاد بگیرید با چنتا کشور میجنگه ولی ورزشش ترک نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65636" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHRCvjs_uqasb8CuBisd6mSmS5W1fGTcuk0qRatM1n_52MxTY95eHmq_1xRb76jrsSIet8mg2g4etf1Ubpmo7j8XEa-QbFB_chCJvPJmSJ6ZL1RR7eVTSsm8ZGFzT8QTPkElFrPChIg5iVC7uoJZZ8Mel5RUhwv5t1BXw3c3rSurMcioiw7A9K5CwXcIhZ_1_9qcaL-s_whotSNl9rS_wssleJshgXv5WZKiSutg41jBASR2v8DGuxn5RDIelgRKnt6_nM0nAMvOv3tHrL9hchpi7mivJzRMnF_o_8cUeIvIqBvFmsQt3QIhh49vdeir9lQRLMobyQY22P9362fV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر دانشگاه صنعتی شریف‌بدلیل آویزان کردن موش روی تنه درخت‌ در ایام اعتراضات، با حکم شورای انضباطی این دانشگاه به اخراج و محرومیت چهار ساله از تحصیل در تمامی دانشگاه‌های کشور محکوم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65635" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbWa0-_A03WGRMQIN_DoNft8axeaOMjMHMOl3izK-a2SNggUkjDP25Cgox04zqL3JICpi8ISFSQOIMlC8A6HbT4lXm0sEejErAyHsZMFwb2cO8Z3zWEAb0R6rBLR1xKGJ0Ask9zr90AE3s2Z3nTZNhUJgqAArP65ayOpNEfO35i6hCAydZajcYQxIHLwf1TUbiEB60hoV7aI7BxCPDsSTSGp2xw0T0vM3DlQI6uLvwzcvYKdD1IUD54bwhGBxevdk5ulXTG3c4si8I0DCWAyUUgHIfek87HNG-9j2tKD-2ctfMDMiID5aEMKQ1PMnWp-OOjPtPaBx4miLbnzdvlkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویر منتشر شده از شهر قشم
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65634" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=LLkdJiWJrZl_OTPdnV8QmXGMOqhHjFqHRZs0sDLZwuXunml7oAy3dtwHHh_u2wy1GEyxKsLAZtLwcoDn3nWl60-WXcSi4mbIGXXaj67XcGxFNivba983UgZmFqXmmPzmnIslOOThJACo0kE0iGpBnf4rT1h9ZbI1rACOPt1e8ExzBe53WtoUJOOPbJ3CdDf4P8OV_4fHk0TF38HmyXr7qtsb9dqP70vuqH6BZyLmlGuezDYDiQ3QUceFtVatl2LEkeEvL_bc7lknksOSqkE-KbKe7oRRgS7bk2pZABKYnqVQmHYduZyygYJqwcm8ZpjWWuOLXpDrAcqnb8SyP39tbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=LLkdJiWJrZl_OTPdnV8QmXGMOqhHjFqHRZs0sDLZwuXunml7oAy3dtwHHh_u2wy1GEyxKsLAZtLwcoDn3nWl60-WXcSi4mbIGXXaj67XcGxFNivba983UgZmFqXmmPzmnIslOOThJACo0kE0iGpBnf4rT1h9ZbI1rACOPt1e8ExzBe53WtoUJOOPbJ3CdDf4P8OV_4fHk0TF38HmyXr7qtsb9dqP70vuqH6BZyLmlGuezDYDiQ3QUceFtVatl2LEkeEvL_bc7lknksOSqkE-KbKe7oRRgS7bk2pZABKYnqVQmHYduZyygYJqwcm8ZpjWWuOLXpDrAcqnb8SyP39tbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک‌های پدافندی سپاه از جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65633" target="_blank">📅 03:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام ارشد آمریکایی به کانال 12 اسرائیل گفته؛ هم‌اکنون موج دوم حملات آمریکا به ایران همین الان در حال انجامه
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65632" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKW7NVulST5WBMslJyhT53_WHgM4jVnGuodzEFkX_6EqduP0sWQs77im369eyqyRfwWYJvwLBlRCQdJlQQOjWVi0lH8oc950vnxiHij2khqFlCS8QRlaWiKyQtShGBMLd7Mng20wGhxieWMzM33ZHUI43PVMEErT1W2Lqa4WA-L8bhYatDAWKkyq7ye4elca-Xl4ATrxDk9gj5WnAKM1vLzXYaR0sWeun2Qnhv2b6lFxuX8orgUk3XjiMoXDK9Fy5jdaFY8pWWYqCHjMJv--wJ6ghOZYIUC58RYKRxWrWye_bCt3kdCwMsir9ffoNPkdNZMdPPqUVjYGfbF941LFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🗳
کانال رضایت ها :
@AtlasSmartTrust
🌐
وب سایت رسمی ایران :
AtlasArbitrage.ir
🔥
ربات رسمی  :
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65631" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65630" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mH3CZoAVF3JQOOB-2aRFQAE1LLw-Use8x0TI4Llxt5-ymnjMdt709rgTGdj51fxMLOEictCwXoypgaUdfO1kdwg1vhiHLMFMMbYa8wxFdahlJJUOVCbDwATbbo8oId1TiaCAQN-UPtQrYvLxMl26UqimMs-t3APD15E5tJJWFyskrd95NJ-Pwyh89nOCatqM6rJFfR56IK2Z0xCwJ432L3l6UHZ1tagKHvCoMWj-1lpflIYctR3FQmoeseAmWU5K7nVfxaoZeMBtoeBFQ-KQ-s6WY3udu_oGVS28xVdLnyUi2DHCB2_uKZFAgZh3qH0dekm9v_h_9XkuEoWgDK67Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65629" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارش ها از حملات ترکیه به شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65628" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65627" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=U03dsTXegnW3TX_FEjpRrQfIv4Zq_H9zvOGtXuXjrDUTfeA39bqSfoLtCDsuteVUuqAk6TMwZFnf38qwM8jx0R3mpz7g3QrxGc47UIOLKEBscoXu3GA4u5tzImhuhf8BOdx2UIiebRB_cswxPFQo-hrjEFNUm3q9sRXWE4gaPkf5sHRZQ0GW1MPa_ywREXTZQ91MrLiHFGQnA0hH6yl5B_H7IFOtMJEbeWRxPjWts584MKTBkOPBkEt_I2YN9vyhlwuffAJxcYXy2zUiEpLoAa9_ZTR-4Wv85R7ZfArUxsOhOL2ToG5TmIrgVqr8wqqpBfWF5EMYehdARsEHQXHomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=U03dsTXegnW3TX_FEjpRrQfIv4Zq_H9zvOGtXuXjrDUTfeA39bqSfoLtCDsuteVUuqAk6TMwZFnf38qwM8jx0R3mpz7g3QrxGc47UIOLKEBscoXu3GA4u5tzImhuhf8BOdx2UIiebRB_cswxPFQo-hrjEFNUm3q9sRXWE4gaPkf5sHRZQ0GW1MPa_ywREXTZQ91MrLiHFGQnA0hH6yl5B_H7IFOtMJEbeWRxPjWts584MKTBkOPBkEt_I2YN9vyhlwuffAJxcYXy2zUiEpLoAa9_ZTR-4Wv85R7ZfArUxsOhOL2ToG5TmIrgVqr8wqqpBfWF5EMYehdARsEHQXHomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پهپادهای سپاه در آسمون عراق
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65626" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEhNMpUUmLu0s-CT6PLHcTBhf64q-slvQ5lpB1pdK3el3qz5acn0KLALcbhuF8UVxE_jORh8BNLY-utNaOb21nqIyscXE7yeN8tDDSnGOjL3h4QRe_6OJdAj8nNdHfw82dbfQ-U2t6WjUNLZt4ITT3SwiqyY4ULuN-ZusiA1T0v01EHXYTu5wvUCh6OEaxriHZOQrNF-ywy0cUB2eZEYZy-Hv-C0yFsCIqIjzhbLs02vNFwlBrG32OWYwSc_7ApeN30oJNstlHno_zUcVg79nzZKgomq6AJpqjuwYhk6oWvnl3yCGhnVUcTmqEkCl07pChcAd4xtn4ll6P9i0U7O3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار تخلیه سپاه برای بیکینی باتم
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65625" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn4xSoqgWGMWfpqZUW1Y17KkQAME4eQAK1C3iiXRZuFF6833PnbyCVJ0CfGgumSUTpswxRMVqdwLuAD-eWaosVsKKzs6e0Fsh7WPVWqgvdM4308MSrtCFFgV7AESKAv92Qeur_pDZdgHOTLDJ4BRcdi565Y_iMA8qoaWsnKbC97o34rXtRS4UFSa8xK4G9lwUWz0nIVdJvuihN45ts_kGEZgwzbW4S4J0y0CBL1Djbt1LqHtUTULv9s2ahcp34kwtMvZ1qz-y3_tYnKF_-P75kvi46jSlvzwEiTl-lJueI_M_jZ_Zui5Nfvlk5UAyS-QUS7ir1z5nrDboVVNg5imKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
علی قلهکی: برآوردم این است که سنگین‌ترین پاسخِ ایران پس از آتش بسِ اخیر به آمریکا داده خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65624" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFOEzGiPs8lV-VFQc4cf5nH2zDkbSnNvpotHYwuiHD6mD8mUfy9LB01VfKC7AzgUP6TzmrwhyJpgZFU4phci-JoAvj4RBfpDkFzlaz7RTxmgwgbMMqLRFceth5wMC51gzPbB3PqaxzKjr0pnjsLGWe1_M_D7Bj6v6W2Yb7E9h686NoAx4Tz9aLc9hjaKCkZtDKvxQCzUmKTp8hwwvA0Gow9IEr1jwF1mgkttDmX7zMGLu6XDEn38w9J_6z0ayEvwDik5e6vuyDF5JoPG_mC7mX89DN8X6kDhsDYJsCCpmrj_uUUBxnnifCubYhq5gQRWCCT2qo59DP7GmfzTVnXbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شید برید سر درستون کنکور به تعویق نمی‌افته
✍️
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65623" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65622" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
کویت و بحرین هم حریم هواییشون رو بستن
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65621" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
حملات پاکستان به افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65620" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFpdshp_tZWVtAA5r_Au0oXqB19mwi36nrmBagW-UayvqxBGRJWV8ROuuPB1byaF28pLw1K7NrA7Lo1Fhnuk-TBU1Zj7uMVmw0Y4f45fTaXlkj1h2DDllY2XTxx22YsV68VOMivzomDYN8moZn1twkzq0x5jJAb7SvrI1twbW3Hf5yjcE57z6MBC_LlLE5qFroFOwoysAH7vmuY3ZchXUi_vRrOwaJhFrQB4NXQI-2dkPzhHJSAEKb7WB_zZt6AP_33ObSVOPiwFJCGj_qU93kGGrFXnVFugqchSSPHk0QnUH_AZ38_CY-1Itkqdswgh8RNpypnJYq9GWf451kLOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65619" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی قطر بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65617" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇱
گزارش‌ها از حملات اسرائیل به لبنان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65616" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
سنتکام:
حملات نظامی علیه ایران با دستور مستقیم ترامپ انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65615" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود! #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65614" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛روابط عمومی سپاه پاسداران:
ارتش متجاوز آمریکا به ۵ نقطه نظامی در خاک ایران حمله کرده است و باید هزینه سنگینی بابت این گستاخی خود پرداخت کند
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65613" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ناو آبراهام نه تنها نرفت قعر دریا بلکه با موشکاش قعر مارو داره میدره
🙁
🙁
🙁
#E</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65612" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیمای جمهوری اسلامی گزارش می‌دهد که در چند دقیقه گذشته یک مکان در جزیره قشم هدف شش حمله هوایی قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65611" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از هدف قرار گرفتن پایگاه دریایی ولایت در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65610" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ترامپ :
فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65609" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارشات رسیده از حملات به مراکز دفاعی میناب
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65608" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65607" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
آمریکا گفته حملات با موشک های کروز و تاماهاوک انجام شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65606" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa1oW49eJZvIMjuSwyq85c7l4MtLbNB316MSU-Dk1sgAxT2FTuwPjaTGHi-KH5VfnDnm0yRP0WQl5Vix0MN-fNzV471mCtgLvOcqTcieLxH4JLKhXAyxYt_l2UdMXp7x0fU7g0-SlQqoxXx3t2vgaXRxL9tMZ9jC_Nk0WR76GHOB6gjVQR_xh7JkSiJK86MIDWqex45U5xSXBjds7ryzRzBE-k2p20HjN_Fe0P7fO_5M8GdHhmviSsM8u_IO0wLGplRjxI4SR1ECtFWc_33jfaELDICFuw1FiP5l01sVhadBHT58Ad7INOMBVedKf5LZKNjQ4tSV3uoyEUBUS_aDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65605" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
