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
<img src="https://cdn4.telesco.pe/file/NWuI8alquG1GlEggxE9JtVJiaqHI2Um2NxcJB__MF-1hqTeUBGu6ZC7BhXbRrgQ62wu0TtmtlcfGhjIQ8eKDFSGblccPbD5wopsCdAhPUgyeDFvyNdVtHn2xrHml9so6kaVDYRkz7aq97K6rB9s3juE9iZJAeiUyo8fM4hjquJt_WIq3ZXqDjoC0pPkpkRe9PyBaQtnj9uS9BgpWpUZC0kZYsSHEmfvsSkBtTfN1RA6d5mk_OYQext-hRiJnGjcAmy4x2JZM2g_0E9z9TO2FlKbQQ52xVIr0ebBDvLe0X-Wc2w3Vdluxv6N3HAFWDdhS7vR3F7I3QhzG3NoV7SASuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar5av3iZL4rS4bIFLUff4kpBFYaKNvSw51NHrSu94rie36NS-MRX5OWjWl5v54XvZhP4-OnmkCthzV7Q4Rzxnm2iAJDc-Rya30SuPZvTm7QoOEltIty4Vwm1qELI1jwIYGFgHLuz2BFuffcPIIEADxWA3b4dQDRGGu6qf1hODJ6Eku5e55kItx1bLkHH9YqxzwK4G0ZqKXxfDL5JyKokaM7jy4DRR_T25HyFWk4nvMg7dfuL-kCDKbWK54an2c8wT5DMXpYzB42rPAHP6x3CrwGdLu7dUfa7lc5p6-bLmErxB1PUY7OCsbKbFZvqQ0TnTzqroMW42fqbW2ryIRfiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کاروان ایران با 19 طلا، 18 نقره و 15 برنز و کسب مقام‌ششم مسابقات آسیایی ناگویا رو تموم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/140880" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/140879" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/140878" target="_blank">📅 16:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeWcuQ2jRh2O4Cf_3tm8BlAipQ033ggO_gkGVbo1p5uiBK9IZOs2p5HR9A72toQHl7VLSEMrg3qe_UBfhFTDUz-FL9S1xAxmJt2dLoI6L0yBTx8n0tfIQbmIR7JZzd-nsQZjHRx1GwNakuf_oZ55P9_FApOiZTjkVGOUXCnbpus4SQgw6M6N4Zt0uUhMcKBfDMQfg3eB5Nq2nNlZ_hmUZChBSMqTBeZUCEr_Wzhu8j_H9EHSXhMuvIrBcepUS2Y-QUx0xkv0OuqIk4iqeIgmKvc-mmT2tjKQa-r1meSOj7br7HQpdQNz0tBzDiHzpKFyW5P3_c0wZJAQHcMk6qGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
SPAIN -
❤️
CZECHIA
⏰
Tonight 22:15
🏟
Municipal Carlos Tartiere
🇪🇺
اسپانیا با ۹ برد متوالی و پیروزی ۴-۱ مقابل کرواسی وارد این دیدار شده؛ یامال هم با دبل اخیرش همچنان مهم‌ترین تهدید خط حمله است. چک بعد از شکست ۲-۰ برابر انگلیس و اخراج پاول شولتس، از نظر نتیجه و اعتمادبه‌نفس شرایط متفاوتی دارد و مقابل مالکیت و پرس اسپانیا احتمالاً عقب‌تر بازی می‌کند. احتمال می‌رود اسپانیا کنترل و فشار تدریجی روی دفاع چک بگذارد؛ اگر گل اول زود برسد، بازی می‌تواند به سمت برد با اختلاف و کلین‌شیت اسپانیا برود.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/140877" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A0PLmGVmPt3eEBRgvw5hiF5MRf7tF_amwK1o-hDSLP4Pwe5Pcl1bz5vZDti7K_3uAspF-aOxXj064K4Y5OrhnTPzQv02V6O3iPkaGiOYjfiDkPHZb5V1jJnMTYnjXntxfs5hhr2ddaHou2edTTs2St_36ReaVbIlE0DVcQsVu_5D3TkYkd9EwfAl0PBn7Q3hc1nYps9CU5pI1hjukbtY8MTRHzQqbYnXHv0UUKlduttsq2bZTkWliHsk6bKA_MWrO3RDK3cBmS6tOs91zgNMfZkyQgUij4OjEbS8GquIWYClRMf0bp9gDWwtdpxuDrjuMGhhLt55kD6FItqo6tc4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
تیم ملی والیبال ایران با غلبه بر تیم ملی ژاپن مدال طلای بازی‌های آسیایی ناگویا رو به دست آورد
ایران ۳ - ۱ ژاپن
🇮🇷
۲۸ | ۱۹ | ۲۵| ۲۶
🇯🇵
۲۶ | ۲۵| ۲۱| ۲۴
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140876" target="_blank">📅 15:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
خلاصه بازی پرسپولیس و گل گهر سیرجان
✅
پ.ن چه کاشته ای زد یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SorkhTimes/140875" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
والیبالیست‌های ایران به فینال ناگویا رسیدند
🏐
تیم ملی والیبال ایران در نیمه‌نهایی بازی‌های آسیایی ناگویا با نتیجه 3-0 پاکستان را شکست داد و فینالیست شد.
🇮🇷
25 | 25 | 25
🇵🇰
13 | 15 | 11  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/140874" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/140873" target="_blank">📅 14:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
عالیشاه امروز اصلا نزدیک نیمکت‌ تیم نشده! و هیچ سلام و احوال پرسی با هیچکدام از بازیکنان و کادرفنی پرسپولیس نداشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/140872" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/140871" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/140870" target="_blank">📅 13:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scFce4oAiFMtZ9xHaoWSA1BUF_OuQv63A2FaqROBVWadhohw3WtVJ12jr3nLvkte0kZVnqtQ6hjNDqXd6zMq-OOYLRKWsrjHOXrQB93aBRSP9dxEK8nGF-gYRlUJM632B_BAYSx2SCSW2vhKmceORZu05rA_FrXxoOECSYrXvtV6nRTNtc-CVFPq_Oxstgb3lJxUL8UfUJ6-ekOTEfZOybjTTbTHAX-eorzW80Ql-57hPPfDNbR2jRchkh4obyiTorpdXlHJq50C9IduQTAV8kpXXlnJh37Ukd77qo4QwdrALS4zt-_GkG4EoVLEUFCdESJgxqtHNcMubWOF910tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
زمان بازگشت قلی‌زاده به میادین
◽️
بر اساس پیش‌بینی کادر پزشکی باشگاه لخ پوزنان، قلی‌زاده می‌تواند پیش از پایان سال ۲۰۲۶ و در اواسط آذرماه دوباره به میادین برگردد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/140869" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKCE4RNYe81PTmC_7PxDUDwx2q4QgSxw5RrYX8d1W9_i-1SriXnXgU2LXykOaee5ARybu_9c3ENVkoIw3-aKvDpomFbaK6FvpIHxfy6_mkrThM5lSFpPc5YZiWD9qMt3JkDPZE3ICgGqofpYijq9M2Fxpgc9hz91jnvbmQcTg2Xck4ZpJz2wmEyPF1AGBnuSpx3VxG-U_S5rn1MFss5XQW_WMHbxbtkN0syuiYZh0_4nfMdSzNX7Dt4OP-QbrCEhbaY1VTYW0nECc8sOXMuJCGw_NSi8yUdGADrjdC__c34kls8LHMmFmmZLqzMgomm7pdhTX6hpgz8K3y6mC_vIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از ورزش سه
🚨
زوج خط حمله پرسپولیس مقابل صنعت نفت آبادان رو ایگور سرگیف و پوریا شهر آبادی تشکیل خواهند داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/140868" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚪️
⚪️
محمدحسین صادقی امروز علاوه بر گلی که زد، عملکرد درخشانی در ترکیب پرسپولیس داشت و ممکن است در بازی‌های بعدی لیگ به او بازی بیشتری برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140867" target="_blank">📅 09:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140866" target="_blank">📅 09:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
✅
گرا: از پرسپولیس نمی‌روم؛ از زندگی در تهران راضی‌ام
‼️
✅
✅
گرا در در گفت‌وگو با «Nemzeti Sport» درباره مصدومیتش گفت پس از مشکل کف پا و انجام MRI و تصویربرداری، شرایطش بهتر شده است. او درباره شایعه جدایی از پرسپولیس هم تأکید کرد یک سال دیگر قرارداد دارد و…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140865" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-KliyALPnMNcmoOZZ7iECwhnpAtEmAtlspXRWvY-5plyQnZZbCIrSl3TjgGTn6kwkwAhhasQmBuK7AeOMrqAP8gMpntIUBtb4d4HSff_7vaCPwlQ7HtTC1t6rfIt6PCRpcejbxa2ysP74nqolvRaCO3XmfFuoLrhJwVwx0i76_IA_zyhRejDylIkQxUrE8tYhOO5y10G2NbrUvaR98cVDqf08qudHZ_EHjt2RBNe3qeZO7m7J0n4YKw1L4FfSUKf1VhsQu3IHcMjyx1C9Z23ODl3Axsfxk5BAWHE3XhRX8GY7cvuzscgH-mpqhX92LPMWQQZcC_xh3-P4QAMx8J8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140864" target="_blank">📅 09:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPXs8ZY6DYVEcaBN3p3oFaY9g3hI2rW8OU7Sy4I60Vo_MwlDE1swDAn_zOfo4LVz1SiDBXq1PwwLFy65GZ3MujnsEVlwAojYTh-9A_7Rh5mF33dS5PoqMuHIoaT_zhXjy1HXxRCpn5hur26PCKYfmyoffA4ORM45ut4iNxU1W7MATFmcbUU6fUTx5Jw_tXLL8PGkz9921g7dw5pofBu5zPk5Q8CAg4ywsXtfaffhptCrFQ0m3A5amGBcbmxG7-sFrqmnvQ7abRTnc3xm9ius0uCSbUzvck1bJe5LO2m-bclebMKbhiMAYa7scA9L4RgA_ZsdG71vWhqpRNH44JtnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
CROATIA -
❤️
ENGLAND
⏰
Saturday 19:30
🏟
Stadion HNK Rijeka
🇪🇺
کرواسی برای کنترل بازی روی مالکیت و گردش توپ در میانه زمین حساب می‌کند، اما انگلیس با سرعت بالای انتقال و کیفیت نفرات هجومی می‌تواند در ضدحملات خطرناک باشد. تجربه و کنترل کرواسی در کنار قدرت هجومی انگلیس، این مسابقه را به یک نبرد نزدیک تبدیل می‌کند؛ احتمال موقعیت‌سازی برای هر دو تیم بالاست و گلزنی دو طرف سناریوی جذابی به نظر می‌رسد.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140863" target="_blank">📅 01:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140862" target="_blank">📅 01:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
غندی پور، مهاجم ایرانی شباب الاهلی امارات، به دلیل مخالفت باشگاهش نتوانست به اردوی تیم فوتبال امید در ژاپن ملحق شود. طبق قانون با آغاز پنجره فیفادی از ۳۱ شهریور باشگاه‌ها موظف هستند بازیکنان خود را در اختیار تیم‌های ملی قرار دهند
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140861" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
پیشنهاد پاختاکور به مهاجم پرسپولیس؛ سرخ‌پوشان اجازه جدایی ندادند
✖️
✖️
بر اساس گزارش چمپیونات ازبکستان، باشگاه پاختاکور در نقل‌وانتقالات تابستانی مذاکراتی را برای جذب دوباره سرگیف انجام داده بود اما باشگاه پرسپولیس با جدایی این مهاجم مخالفت کرده است. …</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140860" target="_blank">📅 00:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
در نیمه نخست و در دقیقه ۳۹، شوت زمینی محکم محمد عمری را دروازه‌بان حریف دفع کرد که توپ برگشتی را محمدمهدی محبی به گل تبدیل کرد.
🔴
در نیمه دوم و در دقیقه ۶۶، حمله ترکیبی سرخپوشان با پاس شهرآبادی به محمدحسین صادقی رسید که او بعد از جا گذاشتن یک مدافع با…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140859" target="_blank">📅 00:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✖️
✖️
بی اعتنایی عالیشاه به تارتار و حدادی
🔴
بر خلاف سیامک نعمتی که قبل بازی تدارکاتی امروز پرسپولیس و گل گهر، به سمت مدیریت و کادر فنی پرسپولیس رفت، امید عالیشاه ترجیح داد، برای احوال پرسی جلو نرود.
🔴
از اینکه باشگاه او را در لیست خروج قرار داد همچنان ناراحت…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140858" target="_blank">📅 00:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
ورزش سه: امید عالیشاه به باشگاه اجازه نداد امروز مراسم بدرقه و تجلیل ازش برگزار کنن و تندیس باشگاه رو هم قبول نکرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140857" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140856" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140855" target="_blank">📅 23:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140854" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✖️
✖️
شماره ۷ رونالدو واگذار شد
🔹
پرتغالی ها خیلی زود جایگزین کریستیانو رونالدو را انتخاب کردند و رافائل لیائو شماره ۷ را برتن خواهد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140853" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140852" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140851" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
پایان بازی / 3 برد از 3 بازی بدون گل خورده
❌
پرسپولیس 1 _ 0 وارش نوشهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140850" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140849">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
خبرگزاری فارس:
🗣
شادمهر عقیلی مهر میاد ایران کنسرت میزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140849" target="_blank">📅 21:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140848" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=Gia4HDZNeH0O4ALVCthDssAH0quJ34CLluH0yHyjqSix73MTFO4t54CP_JwQ8jJhFNw3GLZseYogQZaszfNHiTpfoPOU3YUgCfaWGlCVcJPnpgBrx3kSztDZWs-9CCCB7Zc66JEtNTtEo97H4BnJleV_dlfpP_cXyIV7LTNTJKixemHcCfekJTbxhgqi5F2tamVlefveEP9dLAiLKB_v0mon1j_1lV-U7Nc0fQA6woqEvhTxgebd3J5L9-uM5Hg3jfx3ebM_YQDosmPektcMGcMi5H2RRg8S5f0_MwvLU8LkUZyymdxKstnNsl209GpYfbXZpH5GbXbUFHUbrCjNmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=Gia4HDZNeH0O4ALVCthDssAH0quJ34CLluH0yHyjqSix73MTFO4t54CP_JwQ8jJhFNw3GLZseYogQZaszfNHiTpfoPOU3YUgCfaWGlCVcJPnpgBrx3kSztDZWs-9CCCB7Zc66JEtNTtEo97H4BnJleV_dlfpP_cXyIV7LTNTJKixemHcCfekJTbxhgqi5F2tamVlefveEP9dLAiLKB_v0mon1j_1lV-U7Nc0fQA6woqEvhTxgebd3J5L9-uM5Hg3jfx3ebM_YQDosmPektcMGcMi5H2RRg8S5f0_MwvLU8LkUZyymdxKstnNsl209GpYfbXZpH5GbXbUFHUbrCjNmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140847" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
حاج صفی: بهانه نمی آورم اما چمن بازی با ازبکستان و روسیه خیلی بد بود. از مردم بابت پاس اشتباهی که مقابل ازبکستان دادم عذرخواهی می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140846" target="_blank">📅 21:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140845" target="_blank">📅 21:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140844" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9nKLj6OsPyZ8HZKZ4svXWiw_EN7cYKYTfWnGEhSM5puMbdGA2unB0L9IfC25Ua9NH4xejGL4nfhoEHefFCwRKQYfwB-moVXpSqnG68NC21F4oJcYHwfbxFSAi8Gm_CDJIvg59dySOwpSkUM6eA08kKTy_8VP88TCH_sZiFstNhouQ821r0SCy0ffca9BG52hdWl4OvzoQXX9t7thqc1VlaPUTpKrf_nRuWLh3rYc0ylIQAHdC6oyPOvvkZNJGpX6Osq6yPlEXfeI1HpSP7najtsQqF4VzEm6F3GOb5fdtQlSOJE7FEBvbCY3Tk-s8WDON0NIBmH8erHhPMgMwvXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
FRANCE -
❤️
ITALY
⏰
Tonight 22:15
🏟
Stade de France
🇪🇺
فرانسه با دو برد ۱-۰ مقابل ترکیه و بلژیک، از نظر ساختار دفاعی و کنترل بازی شروع خوبی داشته؛ ایتالیا هم بعد از شکست برابر بلژیک با برد ۴-۱ مقابل ترکیه واکنش نشان داده است. غیبت امباپه از قدرت هجومی فرانسه کم می‌کند، اما حضور دمبله، دوئه و اولیسه همچنان تنوع زیادی در حمله ایجاد می‌کند.
با توجه به فرم اخیر دو تیم و میزبانی فرانسه، احتمال برد خروس‌ها با اختلاف نزدیک و گل پایین خیلی محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140843" target="_blank">📅 20:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0YGGe5y03sz8tgpHoLV_-7RNWx9N09Gv_VmnpfokOgv9Vae_6JtpyzJndcmnHFW2wM8Uj-MCJF9EBhBjFVUuSSQUVUhnLcAHxeHx0BpBavCJ12o5OUq3qdHlIv0TTOLRmjpcsvLwrwBMEZdaW6ouAHAsem5Xkvv94jf2a1Z-WHf3lrB0PIrFUab2N95hjSdLxYFf9f09Mvq6Ta-0JuUnZt6u9rSFyNirbUyBLqKi10kWztf-TZtZQEjHbsMyONbxgpawGkGsdyyOmEIYbTOQ7kFhcpMUAx412jDlnmrEKP49BuRwaGEv4vdrw8rDoNr-yp8XOV9SyYnKSCuvnX-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140842" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIxySuNAg4blF-SbpiThqTAnG3lbLPabJUVtHW97Z2wjzAmUupzeF9E67rfGMOAvvdZpGF-0ocbN6ZANREwKzXgJDwVjvja0cd63wRryyq4Sv1sAWpi8DFzgW1IaXIaFVN4O0MAmw6NGNBIi092fzLY0im5Ex2SJT7n-Tu7RLMXRbr3OWntaDi1pSXZhYyTPUaketv3EL11IWpG0nR5uZ-hfXFeVx1LmRNafZc80B5p0PVI2sjbC85uMJwhbcYTb1zrekPCgcAae6FPIDUlqdCbkctIOQDwbz74KJFYQg3AA7NUZiPHhAJ9UIGYGUi3g3fdlW-_q7Ivb-nVN6Yx3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
کاپیتان پرسپولیس در دیدار دوستانه امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140841" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول  پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140840" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140839" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.  #دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140838" target="_blank">📅 18:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3MoOj7N-KKd1WZ3p4HE4e6RLtquAWv3fkaOvSs8UzEX0xFyV_drD_CmtKEthyy0ZXu2TSDc9dBDwGbHcjHo5rQglynNtmhJCwPkkU1Yd3uFQVj0Mw4BMSj8a6ldtCsSeOctIBvPQ5-Zy8K2hOG-zsmcRvpzrseefyKCtnAUEbT47RcTUCHEzOXbukScBq7HiL_0xgqeS-DXq-100TeGMa1e_Y8MpbhwWNlOJMwBFlDas_5XKCRUVZIJ92aO3YFC4rWBadMvbS2UlxLVFGXxVWVImP24cOvTbISMgRRrcSv6pe-cdqVLNMmoAGgeCvxzzLQeryA-zvNhbF_xEhZDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.
#دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140837" target="_blank">📅 18:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3yrmOVhHVuzeDEVQoypWIaUKv-BMvgYTJvRwfrJ3OzOMfnLjsQTIAIbDxjBKlru97W_23XxxUcIfb0GhvO5RSLRX4jRGGYAMbC47vP53arpqUhpHuvRE4TtkDihLt4tPwRG-DctL4Pvm0fy3D1eEJ6olnl8XpaHMtaxZuWd0yr9_MQCiBqjbGgl4oLsvpfB-ylAENRMC9fmnX_LTn1GQ0LmeRjEO6E5UeeMKbq_7rfQ2EamHHXtxyZRwBtF886gkcD4eHI4RwvubzOvONOMLr1GMC7sqflFo5B4NLJM8fK9RWrp22CHJ_6AgLwJqY-nTweLxoinG5_LA-PYXaBjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😀
سخنگوی فدراسیون: قلعه‌نویی از باختن بدش میاد به خاطر همین بعد باخت جلو ازبکستان اعتصاب غذایی کرد و چیزی نخورد
🗿
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140836" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f945d97990.mp4?token=OAmiYX8AepYVjq2TnQ80RvXMDGWfp_PP9w4Yel2wh1X_iuJYvsxcZy9Z8kr35UF0c_J4esSlG1YhJerzXTzUEflmDJKrLS1Jjb3TbJp6gvaGdhE9PUmJIW2ecixCucIh_ZnLpBmls2IWv3vgqZqpuY0Bw1FgnRIdnIbRZtv66Ifjm0yhm4UOjisLwWz9sbT4pONSJinNo8N261D9gqDaoSw4-C86ZUwgFGX_WhrisPX4PPtRJlhc4rrBzToKF16Ii5znvWA1UxHsnQ_HRpc0Z3N2436SvYvzuKLfXEVlQPtHfIqpt3u6DFpSAth5I7V4XizSiibk7wahKlfnDjXuvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f945d97990.mp4?token=OAmiYX8AepYVjq2TnQ80RvXMDGWfp_PP9w4Yel2wh1X_iuJYvsxcZy9Z8kr35UF0c_J4esSlG1YhJerzXTzUEflmDJKrLS1Jjb3TbJp6gvaGdhE9PUmJIW2ecixCucIh_ZnLpBmls2IWv3vgqZqpuY0Bw1FgnRIdnIbRZtv66Ifjm0yhm4UOjisLwWz9sbT4pONSJinNo8N261D9gqDaoSw4-C86ZUwgFGX_WhrisPX4PPtRJlhc4rrBzToKF16Ii5znvWA1UxHsnQ_HRpc0Z3N2436SvYvzuKLfXEVlQPtHfIqpt3u6DFpSAth5I7V4XizSiibk7wahKlfnDjXuvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول
پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140835" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bocnJonQnoKASbhwJdD6rCPg2HSnOGQGgL4v1YXT47Wqs_5puZS_sjfWlX9PsZCkU1zP3seUOHiXk5BZei7jc0Ykc6hu_jAPWmcnYoiL8I0qvMAIc-C88VRQi-zMdEvX18PIJhkR-lthgFlGMCLtpGRKPOtkugT3XMKA8UaE1DLcWKmOV_RCdLq6lLuMPKBK0xjjepOjv8LkKFht1rNlSHt-Dqxem5EZ2BdXbehmqCvWc0rosjDL9iPs2L1lcR4ZHHqsC-P7xb29RcS6UDlOMXur4sE3RZ9rrV8d7Ea8PcT3UJi9DqBhCBMmRULQ8uFMpUp2jPLLpW9r1oq4LDVx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پایان نیمه نخست دیدار تدارکاتی
✅
پرسپولیس یک ـ گل‌گهر صفر
✅
گل: محمدمهدی محبی (۳۹)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140834" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=IKjVtmixq8zEQnTcmfrA9M6VERtg8lOWINmZoqp-AfwerYRRUpBMF_RX4svy2YrBwhZ-dShV9iq96Z9AzlcDs3mBpYjx4XL-UEELmqAH-IiJZhWj8BVII4QU9gKefFRlM6PvUIKTe29Xk7ZMp08szXBdFmqD5R6J7zSvAupXTHsGgIs5sEHxQQCC-y9J5cSxy2GoBII3lJ8GSY6IglejMJhjgemQkbev8c27LKwO47aa0hRUuLuIMvnOj--lerImf4VJUjJgnrGfxb1mToIcVcSmnRlqhV0X0XlGMQ4wMwO7WPfIjqJFo21MZ00PZkLF3AfIPMgPFEpkQdx8lDqxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=IKjVtmixq8zEQnTcmfrA9M6VERtg8lOWINmZoqp-AfwerYRRUpBMF_RX4svy2YrBwhZ-dShV9iq96Z9AzlcDs3mBpYjx4XL-UEELmqAH-IiJZhWj8BVII4QU9gKefFRlM6PvUIKTe29Xk7ZMp08szXBdFmqD5R6J7zSvAupXTHsGgIs5sEHxQQCC-y9J5cSxy2GoBII3lJ8GSY6IglejMJhjgemQkbev8c27LKwO47aa0hRUuLuIMvnOj--lerImf4VJUjJgnrGfxb1mToIcVcSmnRlqhV0X0XlGMQ4wMwO7WPfIjqJFo21MZ00PZkLF3AfIPMgPFEpkQdx8lDqxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حاشیه‌های پیش از آغاز دیدار تدارکاتی پرسپولیس ـ گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140833" target="_blank">📅 16:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=BkljCrUAJi4VsZriewxfEA5qRq1uW9CVCFf0B4eWsnPCW_wnea2jzhyyfFQj2s8JHSWLGWVc1q7oK-ufLk9ZGboKj3Wb91_go3oV-WTpZrjXuVOdBoCkaad4FN_TxRQ3v7VNmR0B0TBdM2e6tJ0ru0rUpdt-GQ_UGckGJxB4LLfomypJqhhgEu-x2S8cd3sEKH2md6MqPVYupb6gLryBwZUKqK8BqesMc2w84jl2UaKkCyYK7CTVNHxzmqDjS5LeyZX8Bi_5DLzBPX33inql9gtgsxJS9EgTmVoyW7IYC06s6XY0HY4YDefwzOhSJRvlcmgKAkaHXknuZ9B7YsNzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=BkljCrUAJi4VsZriewxfEA5qRq1uW9CVCFf0B4eWsnPCW_wnea2jzhyyfFQj2s8JHSWLGWVc1q7oK-ufLk9ZGboKj3Wb91_go3oV-WTpZrjXuVOdBoCkaad4FN_TxRQ3v7VNmR0B0TBdM2e6tJ0ru0rUpdt-GQ_UGckGJxB4LLfomypJqhhgEu-x2S8cd3sEKH2md6MqPVYupb6gLryBwZUKqK8BqesMc2w84jl2UaKkCyYK7CTVNHxzmqDjS5LeyZX8Bi_5DLzBPX33inql9gtgsxJS9EgTmVoyW7IYC06s6XY0HY4YDefwzOhSJRvlcmgKAkaHXknuZ9B7YsNzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140832" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuttFkQSibQopPc5aBoGNluejaNHfmsQWfHzcr98VT8I9f79bwiQRvRKWre5gJoq9zqNT1LHs32EOnb6ck24rjSyn35doHzL5Ows3iuHvlLt-ogofl07ewAH_KF8Mte-w54j6eNrXcApYKvZJD1zUOL8i8Myx43cHv8TqJdxYQqALMJ1dvvr_GVIi-37KspC_mXJQa9cJXpTf4tbMfodel_DBCt4MywWus2Un9Rer69GhSTW-dLXY49ghP8QMPvqNf7GD6Mh-hweu2XmbFNHzjYw-tkjCgx_EGloBvSbxmS3Elf-U1ufqkAbF22aLypDzo45JFUCty6PxnhEL0oMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است
.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140831" target="_blank">📅 15:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140830" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOSlxMPeQv1Yx-xMjPuCYTciCA7EegYmlOJPLWwNVLrHjj9vNR5G20Mx2e_hBVsjkjrBj6SkfB8cEdAva-p2AtMZtlvN9r-5vGThOIpIWR-U-6K9JUiWb2YqQFW6z-xsL-4SmwinydHvqA-8OADVeYp2Jxk0aW-w1R_SbZY4B_SZ1uClQwSpM4BMWMeWrsxbdqdZdYkI3AiA2bIfR1-4mmZ1o4xOD4d1fQkqnuTRQONMJBje77I1_ZJ2DF2FB0rPfzaA7vDUnd8bbdkO5i_buhYJLaPw063BYzwCCwRN2IESRCBOWCXp0ypmWg2QOW1zMdzvg0WyIoHP432YdbMnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول مدالی لحظه‌ای بازی‌های آسیایی ناگویا
✅
ایران با 15 طلا، 17 نقره و 13 برنز تا این لحظه در رده ششم ایستاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140829" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAol3qGcmk3LeKGiYn5yZZ52Y95KctgR_3L65Y7tBrWvWaHuYLaIWPnuTm6oVI_zV5XXzjb6udi2VLY6qRN8ra6faCisHVGQazGbH0Zr3-5BQzd2hzv5ejURTeRWtmHemy4NTdfvYV4iR7c2dLCfuz_GqfUTCFMLc9hvkX_grqSL98geQEZdM-Ppo5VdcGGJXIYFx2ftgTqyYYrsOwBVusakiz4aVTWglMAa1ETb8jPk3J13bpdJ_TuoeRLTAWDphjfp4zenDGTLK8e-F4vVvbfIOKROY0itvPzLr8gzwWchzUK7mL0Vl-BdnGZVA4NxZ5zB3uNzA0vLibzE2i-qM9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAol3qGcmk3LeKGiYn5yZZ52Y95KctgR_3L65Y7tBrWvWaHuYLaIWPnuTm6oVI_zV5XXzjb6udi2VLY6qRN8ra6faCisHVGQazGbH0Zr3-5BQzd2hzv5ejURTeRWtmHemy4NTdfvYV4iR7c2dLCfuz_GqfUTCFMLc9hvkX_grqSL98geQEZdM-Ppo5VdcGGJXIYFx2ftgTqyYYrsOwBVusakiz4aVTWglMAa1ETb8jPk3J13bpdJ_TuoeRLTAWDphjfp4zenDGTLK8e-F4vVvbfIOKROY0itvPzLr8gzwWchzUK7mL0Vl-BdnGZVA4NxZ5zB3uNzA0vLibzE2i-qM9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
✔️
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140828" target="_blank">📅 14:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2Zq7NzGagt-Bw1V_nTuiR8w-q7Sxdc8FlbWhJlCvoYtjsfEnOY8cCAwIK7ecSiOiMxZ3XKq3WAYWCTTWKo26IdGDulDaNJyB7RPlH_Bb3e4lVCR1XVbwmJLOEYP5MfLJpu-LZ5235OGMjBrHDLar63XT6DwSsHCiRPobl_4zg171c7m97663Ohz0a96YHFVOJB_PguN2q8NTOVS5HPUlFXXVxrg-dSxo5EYgIJmXRfUOCvoB-5z3jV8PLoH9qFsqyX0HyLX1cqyuV34V9T9bxabvrspOBBzeWkpeSAFxEnqns541UDwXNbgFCKtpV15kqOAvyQZ7INUIir1gJ1zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
چهره خندان و شاداب جلالی در تمرین روز گذشته
❤️
✅
ابوالفضل جلالی مشکلی برای همراهی سرخپوشان در دیدار با صنعت نفت ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140827" target="_blank">📅 14:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY9Rg4QOmncCPvNV2rAEEnNmOpWwGi4iaTsQAgZCuYo7tRakm2bP9Uc9G6PMx0SjqWd7Htwr-f27ixZ9kn2NcgqPpUHqjC0funUcre_erpdpASv12E1BqjY363ws6C4U9E9YsNmkoE9M3gyFO3BVul5ai5H_bQRu6yiK2E_xTMbUGFK5u8mjrvRKE1rHNfz7wLHaKtvum_xWXGbMsevJnpyk0ssnwXwgHRNq7CphLIVqVYdG7jDkvchy6JznfHZWx9ugAaSLh8_H_iElop_sQxFlwSrynhbANjFfi0k1ii1mBj2HfQKIwwNEDj6mZZHqfGJguXnczkH6ED9yl3A9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد خروس‌ها و آتزوری؛ جایی برای عقب‌نشینی نیست!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇮🇹
ایتالیا
]
⚽️
فرانسه با وجود غیبت امباپه، از نظر عمق ترکیب و کیفیت هجومی دست بالاتری دارد؛ مخصوصاً با بازیکنانی مثل اولیسه و دوئه. ایتالیا بعد از برد پرگل مقابل ترکیه روحیه خوبی دارد و می‌تواند با بازی فشرده کار را برای فرانسه سخت کند. با توجه به فرم دو تیم، انتظار یک بازی نسبتاً نزدیک با موقعیت‌های محدود و احتمال گل در نیمه دوم منطقی است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140826" target="_blank">📅 14:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140825" target="_blank">📅 12:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
تیم والیبال ایران جلوی تیم دهه چندم اندونزی زانو زده و بازی به ست پنجم کشیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140824" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140823" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: منافع ملی؟
✔️
شکایت از آسانی را تا آخر پیگیری می‌کنیم!
✅
یکی‌از مدیران پرسپولیس مدعی شد هیچ توجهی به درخواست علی تاجرنیا ندارند و شکایت از یاسر آسانی را تا زمان رسیدن به نتیجه پیگیری خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140822" target="_blank">📅 11:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1aNWWJ2JHNz0k7VbGeNpG1ZYho64cEaA3upstIEHhvJR_2vouMnuMOSxyYRda8AJkrPPWh85exifpGpTImUKyjBaz_yoQRB5oiffCKP_fSEo_hVRICsFaFmxFz8hgKp0Zjshlrh1eCvD0LdKEGu5G2KE0oMoMKf5mBWz_WTlHAde21UPHuQ7ADapgx5-IIeHFzrxyMM7SFyA-V9DCB37Njc4U_7BA4YmtwF1e4M8j0yPGhWehfCUcarsdPy0Uj7PBLS8qGrtaGw71zlVnDvvvS6l1n-AfX97pD1-QiAgGMI2446TpdU1czQg2-UDVi_98KmJVFA18sKY_jjFYffmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
⚽️
👀
‼️
فکت عجیب ؛ مهدی طارمی در شش بازی اخیر خود در تیم ملی، نه گلی زده و نه پاس گلی ارسال کرده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140821" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140820" target="_blank">📅 09:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140819" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0J3G8TizyCvtxhA5h9irGGgNNd8_ULaqPYMslcDKIRVMVzSkN3DDU8UN931gbUTv4SZ9k65Drv6hVJDud_xlurIPRvDZ3S5LfGS2oyUrPMSG1VtoQ_NPHI9_BpxjXSb_FNTELgubBP5mUdvX94NysHqgh_9pupFYbI9G7ZsGr50TKynnq0VwWzTqk5IAv2twqX5EzE1vL4wDpjvBOwyAEUElhV4_1UR241AHwwZFNlXfpo6uSyvOdCdh9Hi-vlVuCU-uOabPqduyIwE9SZBfeadqIp-VCOeqHH13Viv-VHuE5Cw5CoC3uALgboIFwmzIJ2OGNsVKFoO0La5JI526g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امروز تیم بانوان با زنان نوشهر بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140818" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140817" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_i3h0G92IoPW5qufaX3q4elRtWM4fpXhIaR3OD9aIcBndir-gAFIM7DMmCY1dL-pMyNtjiCbwPID8lI4uGKAeyp94ULd8WZhLUEoLpJiaCKSIeLNswywNln_URt6Okj5RuN1v2iKY-7A-IlcSGHpTyOevyDN3lmUVtYqGiogHa6ZOzppCKy-pZr3dEQYSJrI0WxLsQfRB_vwWwZlu1joiq6EZ5Jk-LuVYOdDN8Dzr_-CrS1n2HHPQioGQZvKV3QjKZzgCCgmCMDO-uJ4F1NniKAPu1vFCokCV6uKdBM1TE5l3miLOH4VqbVB1pLu1cqQF7evQ5S98xRwo-vvz3FhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک شب پر از بازی‌های سنگین و دوئل‌های نزدیک؛ جایی که چند دیدار می‌تونن تا آخرین دقایق غیرقابل پیش‌بینی بمونن.
🔥
⚽️
از تقابل‌های پرریسک فرانسه با ایتالیا و بلژیک با ترکیه تا بازی‌های متعادل بوسنی با سوئد و مجارستان با گرجستان؛ کنداکتور فرداشب ترکیبی از مدعی‌های واضح و نبردهای کاملاً قابل پیش‌بینی‌ نبودن است. در سمت دیگر، اوکراین و لهستان روی کاغذ دست بالاتری دارند، اما فاصله‌ها آن‌قدر نیست که بازی را از قبل تمام‌شده بدانیم. ۶ بازی، یک ساعت مشترک؛ از اولین سوت تا آخرین دقیقه، شب فوتبال ادامه دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140816" target="_blank">📅 01:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/led2FuZW8ZqVzdqVT_oCMj9ByZrkMwLi7t5RLXu7vgXnm9CG3HfW5zCVLrrftTSW-pNJSIOAPi1wVHQgVJZDx9fiir5P3kGeZoyo1_EIqNwxAGX1PX_j1MqO1xkjNTsjw_53-62H8L0EKoNAW66ALu018qxCojVkU6DCZrM2WByE7KW6XTujPxuolQjVJT6R6osNb7p_CMsR7fZ81J0HA4hDJBKlHEgrdPuWM6FgfAAZjboKa3phweSTqWUuXr79DL_dpoNVr4XohQhNrRyhA_JO--inqM_Ls-wamXo6R7kr5vfPe3LjA9FBcxzIGjDfBU5YDoRyhZg5ThXX9jyZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گفته میشه که پویا اسمی ۱۶ساله یکی از استعداد های جدید و درخشان پرسپولیس هستش و تارتار میخواد بهش بازی بده و مثل زارع تو گل‌گهر بهش بها بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140815" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWcGFAZnGHOlZgJXtsS-sMIM_yPSKE4aCzOSTPFTdC9O2UfL5KpQig2KSk3CFyzPJZmV7pEwm1I4jthu730i6zSPVow46gb8pv0i51cgPn8DhYWjJDPCEHHkUevFHNHfp_l5T9GYRuRY_-9XlOI252tiK2PK66SCyvQ9SFYNVtfVlyAsJuJdwGZ7yPMKlLiladLB07MGmak9dayP8New4MF-NgcSObtUkiTbulo3lwtHeAMMh1K0i7qFd-ftGvgFKDl1K8lRifrEgDe87bZyyDdUy2e_o7aGB_9QajaSxgqiadySNAJ3h3zrm4oMqU8ePYbkUqdv4zBRjHLLyMDfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس فردا به مصاف گل‌گهر می‌رود
🗣
تیم فوتبال پرسپولیس در آخرین دیدار تدارکاتی خود پیش از آغاز دوباره رقابت‌های لیگ، فردا (جمعه) پشت درهای بسته به مصاف گل‌گهر سیرجان خواهد رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140814" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140813" target="_blank">📅 00:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZleZPGj1oyIHwPwG2MI-9PZAjuPtDJjSBr37xttQ8M_mLXZWGatuV-x3DdrfBYMNGJRKvGNYuno5FntUX71W2F-l88B6bdv7kb-9iTGd5Laz1ny3WRQI_nPmAo56tPBFke740OecmPl9-RCZpKL_hbz7gFDigu2l6fro1kuKGuO8pe-W5324grNQR4TGiuYNV2GLPqumncTMH01w8W1UTYDLp4d3owOZ0kHCIeKmHF8U0hzG15OBxYo2qtH3K0VygURvJLP34GRHPFrg44BSN2FrEFCyRwH8ka8lKRhem8BNoZU5UyM5OCGLJRcpbxtEx3wDp6yKdpbMjRCMg-E0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت ملی پوشان پرسپولیس به تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140812" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140811" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
جنجال قرارداد گرا در رسانه‌های مجارستانی
🔺
رسانه‌های مجارستانی با اشاره به غیبت گرا در ۶ بازی اول پرسپولیس، دلیلش رو مصدومیت پاشنه عنوان کردن و درباره قرارداد و دستمزدش هم نوشتن. همچنین مدعی شدن پرسپولیس دنبال پایان همکاری با این بازیکنه و اختلافی هم بر…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140810" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
هاشم نژاد به تمرینات تراکتور برگشت و برای بازی مقابل استقلال اماده هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140803" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIVXPtle1yGw1K3BsQNV5Jf0KfhJcNEN89oFWJBBYaH6Suksiy-JdfqPPjzmvEFTrHnXKJPiSEOlQZj7XJ-YEZdjFuQ7gNvXwAvaGxdsQ0B78OzJ-v3W-GD7m57yKcBPj2XfTQLndbEQhzr9xsfIIxlrwvoxcVBCS6RYzAjrMPeCg_CY5qp811XUbWXn1EFxya2obGdGkA_qqSWYTtKV7_MMoyHyZSyQh23QLu3to_7elJ9TpiuNjaNT_q2hmU4YgXeX-NWvcYA-g-MdoX0vEXJIEOhSB58XNMHnLe6WLX1fcUUErsG8G02lN8vdpMKsT37wXCQRPQAfEVS09K2kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد شمال و جنوب اروپا در یک جدال سنگین امشب در پارکن!
🔥
⚡️
[
دانمارک
🇩🇰
🆚
🇵🇹
پرتغال
]
⚽️
دانمارک بعد از برد ۲-۰ مقابل ولز با اعتمادبه‌نفس بیشتری وارد بازی می‌شود و در پارکن هم معمولاً تیم سختی برای حریف است؛ پرتغال اما با ۶ امتیاز صدرنشین گروه است و دو برد متوالی داشته. نکته مهم امشب غیبت کریس رونالدو است؛ او اردوی پرتغال را ترک کرده و برونو فرناندز هم با مشکل جسمانی روبه‌روست. در مقابل، دانمارک روی هویلوند، دامسگارد حساب می‌کند.
سناریوی محتمل: بازی نزدیک و پرموقعیت، با شانس گلزنی دو طرف.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140802" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140801" target="_blank">📅 18:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhi8CIf-0VS_47YXMwcS3uFFqJbn_T23wRvzTyAUwpRDdQxirSFbonyu3PUUe39x_Ckx-sSAIgG7h_PmM-BeLbaWYHOQBFXzqU7SZWe1k9wS2COE5OeiFuGBzvCBdozcPb1BFeW_NLVfNhxWl1Fc9aoAhvqoPnC2I6mBa8s__TRx47ale633GiwAGY_btnBfUiKy10GLfcHBv0neDKB7Qs4-h81LEj2BZjE3aDwMu0ukQzYFP3UJqL89MHNgit7O3lFNrHO_O4DRKv6k9r7dN8mFz9iunUlgAYQNsyex4pn1kOArFms2I8dq74rVJreOPVPE59rOLlAlvJMJUO-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور دویدن را آغاز کرده و احتمال حضورش مقابل صنعت نفت وجود داره/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140800" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQph4kFHAzyxfRM_CuB3srNbo6p27wrjT0IhLy1L2LAoVY9RQ2TXWGoq2upsWYOd3UseMwH68ZzMFQFLfne99d-CIHVyLWTTxnWBElO7kBg1cp73Wxsb3ywDufRRgMoQsYQxCzsfQVR3GTKLw6IJsBxsmXoA38thsckvX90nWrHbhQYExtQjUI2_gP5eqE8QHR7X_yJt28ytnoD_gthozjIZ0EyRYAQcl3Wm7YuMhgE3gZ4eJz9NLFUsSKa-FzM571GRi621zTW3pjf7ZdMXuD_EOiyiLDK3XdWp0K_LLXl2h08FLPmpFrHrNmx-9kyQoehdjukAf1gwlI0YhzwRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گویا بازی دوستانه سلحشوران تیم ملی برابر گینه بیسائو به دلیل محدودیت‌های پروازی لغو شده است. به این ترتیب سوژه خنده سوم این فیفادی از دست رفت!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140799" target="_blank">📅 18:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140798" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXca4JSdygRJ5Pt4LnkUDO7u_wh1aDilO48dHSgFzuVCYYYXBYEz8dMv7hMxkFX8Dfc1bT8t2Wr2cxHCOT8m4MegYvD1lY00MjVmIGqer8_YLJjDUHnNnKL7kNHWz_getpwWPFZ4elYSyabWo0VwriBJzvinjkl-Ax7BFcffKZ2BanJ6Rjx2DLmaZffTvw9SFAN2Xy3dgzka6QLniyhe4-OsGlRlu0sK5YOd5eKjXRVvrrOpDohRP7ku4CIcIzQ06IyaTixjP3cl0B_dD6-GxOXHIMfZUx-BU5hfW2Nyqa_VojkYlaME3W_P_uj6uUN2ryFiqL1fvO1_Phj6rCrP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
ایجنت دنیس اکرت در تلاشه که این بازیکن رو فرو کنه به یکی از تیم‌های ایرانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140797" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrugKwf9s4To-3TanadSDl5G1B968gRJc2NAShnVsk5tKAx5eq8kKuCQpKjiSCSJ4WJJQnxwHENusprLlbi5-uT66QWcB4CbLox_7ZoS9HQilzBoIyiww3m9OCd6qsz7XnEU1dl4664HBf8Q0FHCPFxUgQvlqwZXDbAKrBet6uOPwBC7u2_UoXJlq_tKWhPZMzJBvp5PhRprMoHSWQCvaKvvoJ4qdXsVrEQKH7bAAS-2JZBJ0sqR8zivyBWs07XuMcoAOoJr8GK6i-DMVVkfL5euJy4O7Unp2pUIBmnJqyDdG9Ngz2I91pRFIiXuTofUa3qhDn1gXR5lu7nHb6WD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdIz9jqXzNafv9IsRrevywHCGlGZG9h5oJE3ep_FgzxwiHEAYbNHRGRBzAP5fbRcwdudFNPbnYhrmWyjJ6GuYcvvRRAQSO5d5N_MdihCOHBHyW1GEP6CPE6j1TIHeR27V9AcRVrthfaHSMAWnKOocPaKXUcHRSA4atTCQTz9NAjroEUE8dDOMpRv6eHdqKm-YwXWRldtmwkZX6WrfdE1BuCazRAOuxWjnej5QXdDu2zilVVa6MRKD3l6WeDL-UnmatQlYfhUltHYzIMYIUNxY6JhuvIsx7my7cOuAfzKfVA3lrYDtteIYt49EyNJDnJZ-gnVV2AJxM8cGF0Tc5a12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzlH1EQOXmAbHHJveTs_mVYFUuiCwgdQut9LTrHJqfxQWYTIiTeWaHdpH-rlYrg3ssX4hmfLml-2qAgTtvw5HQuHeLj2Qhek-uADguv4am_v_pSFEdyHTCafZ33y_VU4nhlTNauMTknGkgnUvQrEdDu77lknk92XDnEDN-w3yIJFz080Jlm-TeqTA53bXK44hixLCafKE31TT_q0BOiSu-tdvEf4HxIqOur5zWk8zdzBWYXH4tcbxT2p8onJTlddL44CsFPVHxXSelJaKOn9WU4v1JUrGsAZDOJ30mrUNBhpYpSLY6GA462WiY3CTfPeiqLeCA8GJsD-m4PS_dNq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyoiHz6R7kinH7VkRI--OheMIms_Kps0_tyjJtN2ea6RYk7lQuS1Cg1ol9L_wk5ylHSkMyruPp444OoGQu9Wcx3PTlTPl4haMdI-nd1Vbgob2RgI4khI3JLyZsI7lvgWFrPgxDkJXizjR-n9teciQR7fhNXXWKfx2ktMh54U2mfljYUM70rd2vIEluNrr__rvkMja9cg4aGCsMZkibjUU9QwlJIIydx2U90kyUnGhg7E8jtl4yeBlpcyuyR87Vd6QsDkbU40c9EFWmxkffNQOpqyGCMYzj17toyamWoA96Ep-vVDxDDCKX7uxDYyd3cYpSRmBaad8buFDDVKe7an5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
