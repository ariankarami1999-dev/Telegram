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
<img src="https://cdn4.telesco.pe/file/PoTRiaYtNAYva8iG6vrNBT9ZG6y0o533YDXQ6LZXV6Dg3V2B64eOFqL5IoiyDGKh6MwKJItW_23UIP0txMRuLntZaZfhp2SO-pZmdPlXwpMM4MpfwHUOf-1b9rEA7BYMdUaXES7efRcbH5VbZECi4jj8FNi_5jewXeZmFIP0VP7m_4du4K_kiyT7F1d5O-hSDuGikcvRJA1Tiqpf3u4J7gh9dOEawZQ-6wGp66x19ztHqjIJuocLEWqUpLS_D_DuKobMCb6iaBFjiRa3XmUdo-j-aotVoS0IEIql-XtRXgTsJIa4H77b5etyZByd8bvWF582g3HQPb85Q1LGpV-VHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 912K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-147469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تا انتخابات میان دوره‌ای آمریکا ۵۰ روز باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/alonews/147469" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT73UCN7_rxkLJSNErKdIVZvW7lfzpBExkhJQw8pltpriqy5-10-vSTboA9Dz9ZindQahhe78HbjARkZ653QLSiXWi6WNXp1XPMkxkVpg4hi0pFEDv2g42qbhjAGJ6CGrXYpDN2c1ZzvoMqydPACB0S0SzHzfmllkkdU6x-PESNmwcUfvh9iKVES6s7Z0_nsdRJ-NU6ZgKRyrwxSU_FNJ-hgyUxk4zxxSVRcbXiF4vPOVkZpnPovenMPslwTag89-VLWg3Ak3Xby7qlzglItqnYW6bDDLnql9YW49cjlwVO2fjGSLbg3zW1f_taBiLQhP66JQPJ51PLQMVxip0o6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: اصلاح طلب‌ها یهودی هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/alonews/147468" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
👈
فرود اضطراری بوئینگ ۷۳۷ سپهران در مشهد
‏
🔴
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
‏
🔴
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
‏
🔴
در پی این حادثه ، باند ۳۱ چپ فرودگاه مشهد موقتاً بسته شده و احتمال تأخیر یا تغییر در برنامه برخی پروازهای ورودی و خروجی وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/147467" target="_blank">📅 23:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/147466" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش فعالیت پدافند هوایی عربستان سعودی درپی حملات یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147465" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پزشکیان: آمریکا راه غذا و دارو رو بسته. آخه آمریکا هم انسانه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147464" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان: با عربستان جنگی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147463" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پزشکیان: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/147462" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM3JQzUJ5fS2cffSxkuxjdfHCjgGmlIaPLuWNaQop1Jg0gv4XDkrklXtnPUx2kJ7IOlDEF4sc8_obXG08HT1_FFU2cbv7_LHqQ0XluVmY8cg75Sn2AUWV229wRcM5olfUe9UqIZi2aWlc6It_6v28cbtxy4qJ__Py8vyzOj2Yhqytfvxta95Pxx3pPBKVOAnbeT2MXRTFfVQU3rT_pdWPOYmqACWyru441gDzPrcwsAirBlzX0xzDbqn7DtS3Wn_x-R93Y7IJWYbHSXQV227xsZm0CbaVOIHSXth_CvsKDqwKhuv5Wxt6zsvfuxR8-Q3WPWpTItuHe2BT0uKagk2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار جهت حرصی کردن بعضیا
#افتخار
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/147461" target="_blank">📅 22:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj682yRoWqjoeORma2ANEnk7hdf2fKihxToFJ3OziRadtyf6E3V18_Nsh48X3TGtDVktFICrZpj3GM4zZ1PWrDDTTF4N5416TdDvmZLOLfjI84D06ZRacVf4K22Pvi3Ob5cKvnsrtpwiHhIG7Mvd_Hzl8qTicdS-aoGl8bvwKSZbSNyHcnLD5ZG4IaXE6wcG9zS8xNsPSfGdeky318xTFs7NWyL8eXSEemW38FX19FXB_0OWikSkrtPMpu4CUw2m8_omohzqx8P3VIQxIh3aBEJ3mTG0FqvPdzu4pyO83czIi1aD7iykVRh3A2lupBzF7TDP0XDZnks-DYjSzgAUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله های آتش گرفتار شده است پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/147460" target="_blank">📅 22:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: مشکلی با امارات و هیچکدام از کشورهای منطقه نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/147459" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx0nHfTUPYCVzEKEesmEuYmkOLJcYxDCGF-LjVOsxsmNieJ31spTlratrukztlXdMDfhQ_2T4K4eX0BxQ3GI3-9DCdyENIAgHEBLanWM2HUT-uauTbh1Ar_4gV80lVU-j35bz40HZUaeFv1igLOJ-dKmDlppWHFjSNTV32VMr4SfOzB_L6vF1GHqoeta-ZTFVs7y3suetuKyNDoUsznsxQ70a4GsxgLbxlOTx422a9OAwfoqI0SUNlJsW23JSMOnBs7X6cMkEFyiiD50VojgB7D67w1iyQ6I8RAIE6uib7wSIZuaPRlrWEJWlb6qj0Pst9drBMrweR1X0B9zWCYyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماره ناشناس تلگرام ۹۰۰ میلیون تومن
🔴
شماره ناشناس تلگرام تو ایران حسابی گرون شده. الان هر کدوم حدود ۹۰۰ میلیون تومن. سال ۲۰۲۲ میشد با ۲۰۰ هزار تومن خریدشون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147458" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147457">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147457" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147456">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
به گزارش نشریه فایننشال تایمز: اعلامیه دونالد ترامپ، رئیس‌جمهور آمریکا، مبنی بر برقراری آتش‌بس در حوزه انرژی بین اوکراین و روسیه، مقامات کی‌یف را غافلگیر کرد، زیرا مسکو هیچ تضمین معتبری ارائه نکرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147456" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147455">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: هدف قرار دادن بانک VTB روسیه در نتیجه دست داشتن این بانک در دور زدن تحریم‌های اعمال‌شده علیه ایران صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/147455" target="_blank">📅 22:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147454">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بلومبرگ: نخست‌وزیر بریتانیا، در حال بررسی درخواست‌های عربستان برای حمایت نظامی در برابر حوثی‌ها است
🔴
این درخواست‌ها شامل کمک برای دفاع از زیرساخت‌های نفتی و جلوگیری از پیشروی حوثی‌ها به سمت تنگه باب‌المندب است
🔴
فعلا برنهام با اعزام مشاوران نظامی بریتانیا به عربستان موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147454" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147453">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=GbzCVwNE9BBioNUICP5pQXccWUumspMpeHWfGBG9bn48RaoK0TZUhytbRvS2I6nk2vq0ZNZNTsvoJm1cR8p4ZXdqcV8QhLlDT6rOGk9KQHUB-0cZI7fHoU4SviFSgv1-Q5X7GIZ9iumEo4KRfACNXlbyZ9qJX2p8dxxxU85oMkngyQv8fhn7fssZEckrnJ_a4mZBFgjilrlZ7BqUSU0YTh0GiKHtNucUl5IB2jXtsfZ94J9kozWqVAZb0EJ5wcf2H7l7ttKx4MsR01R94cgAxqCQ9_TO0vA_71aRDCZdgWs4Bbh-O2p88HtWZR63OxvWTzAinND4kVhEpLsjYxmvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=GbzCVwNE9BBioNUICP5pQXccWUumspMpeHWfGBG9bn48RaoK0TZUhytbRvS2I6nk2vq0ZNZNTsvoJm1cR8p4ZXdqcV8QhLlDT6rOGk9KQHUB-0cZI7fHoU4SviFSgv1-Q5X7GIZ9iumEo4KRfACNXlbyZ9qJX2p8dxxxU85oMkngyQv8fhn7fssZEckrnJ_a4mZBFgjilrlZ7BqUSU0YTh0GiKHtNucUl5IB2jXtsfZ94J9kozWqVAZb0EJ5wcf2H7l7ttKx4MsR01R94cgAxqCQ9_TO0vA_71aRDCZdgWs4Bbh-O2p88HtWZR63OxvWTzAinND4kVhEpLsjYxmvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، کارشناس فوق‌ارشد صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی حیرانند سیستمش چیست
🔴
موشکی که بدون نیاز به ماهواره، ناو در حال حرکت را پیدا می‌کند و دنبالش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147453" target="_blank">📅 21:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147452">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نیکزاد، معاون مجلس : آمریکایی‌ها برای خلبان نیومده بودن،اومده بودن اورانیوم ببرن که شکست خوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147452" target="_blank">📅 21:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147451">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/ گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/147451" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/ گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/147450" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOMrgsovJ0naA8MOu9V98aXKwptd5Sy43J_VxXZdwWq8vTGN3CHH2pwtkDhN0Z7eMHLY54BLQAzsxMhEIGrTtu0LvS7VNxOgXnC61p9SF5Hi2Dq4dlzzAupn78tc5ZeHyWMvmaNmFe1wGz6aznBKirwINaeldWW6QjMSClrc6GzKpbcKYGRVBZjZYB3B91gcJGdXysL42HlQL2tOn0xfhnpTSXV-CtsI52QjWVyS1gp8pkrcwJxNSzjJnLf2oXrpK-0vr8V7eB6QC9VNLCuXzwd_nUn7v8D4-ZDVIA8OXc08BzpmBAJAtswebCyLquBoDc72fttVA08ZkNLtdUnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: در مورد هوش مصنوعی، در تاریخ کسب‌وکار، کیست که رهبران یک صنعت را دید که برای مقررات‌گذاری فراخوان دهند که اگر به شدت اجرا شود، آن‌ها را به فراموشی و ورشکستگی خواهد کشاند؟
🔴
هوش مصنوعی که دنیا را تسخیر می‌کند، بشریت را ویران می‌کند و همه چیزهای بد دیگر، یک دروغ است؛ تفاوتی با «روسیه، روسیه، روسیه»، «اوکراین، اوکراین، اوکراین»، دروغ استیضاح شماره ۱، دروغ استیضاح شماره ۲ و همه دروغ‌ها و کلاهبرداری‌های دیگر ندارد که آمریکا مجبور بود از طریق بازی‌های کثیف و رفتار غیرقانونی ویرانگرها و منحرف‌ها تحمل کند.
🔴
رئیس‌جمهور شی از چین تازه اعلام کرد که چین هیچ کاری برای جلوگیری از هوش مصنوعی یا آینده آن انجام نخواهد داد.
🔴
گوگل اخیراً اعلام کرده است که می‌خواهد یک کارخانه عظیم در فنلاند بسازد، فقط به این دلیل که دریافت مجوز در ایالات متحده را بسیار دشوار می‌یابد.
🔴
من از این موضوع خوشحال نیستم و می‌خواهم آن‌ها فکر خود را تغییر دهند. هوش مصنوعی و مراکز داده، بزرگ‌ترین موتور توسعه اقتصادی در تاریخ خواهند بود — بزرگ‌تر از نفت، طلا، الماس یا حتی اینترنت. این روند توسط نیروهای ویرانگر که به شیوه‌ای درخشان اداره می‌شوند، در طول دوره ریاست جمهوری دونالد جی. ترامپ متوقف نخواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147449" target="_blank">📅 21:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147448">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یمن: حملات امروز سعودی‌ها را بی‌پاسخ نمی‌گذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147448" target="_blank">📅 21:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147447" target="_blank">📅 21:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147446">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
امام جمعه سنی مسجد محمد رسول الله زاهدان به ضرب گلوله کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/147446" target="_blank">📅 21:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8571b00e3.mp4?token=BBSLpled0H_dQX6ixmv7z4SKoAXrmDcr9l-HIie9qU-F6Yu6OFOoHrrUhf3hqs2l_UINfFWL5XsGuSQUDhVbXiFl0rhX88sa4E9sY02kAikuyZe0dW3aTtaH6aGaPeN9cFG7cARSbreI7z0hm6rF15P-CTWra88dea6P_7wTct7zgTbONPBUnGQFQivsEuNhcK4QaWl8Q5CcGdcdICQOZ6sBAvtywHK6w95caWQTzlw15BZW4me16jSO0SOaynNzHcIsuJwL2nbLKgiCbFE6RAEUOmswthCYoXscs5-WSrYmtielBKCY3jyZernA7E79IiRwBjbC7og87Yh-mEHlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8571b00e3.mp4?token=BBSLpled0H_dQX6ixmv7z4SKoAXrmDcr9l-HIie9qU-F6Yu6OFOoHrrUhf3hqs2l_UINfFWL5XsGuSQUDhVbXiFl0rhX88sa4E9sY02kAikuyZe0dW3aTtaH6aGaPeN9cFG7cARSbreI7z0hm6rF15P-CTWra88dea6P_7wTct7zgTbONPBUnGQFQivsEuNhcK4QaWl8Q5CcGdcdICQOZ6sBAvtywHK6w95caWQTzlw15BZW4me16jSO0SOaynNzHcIsuJwL2nbLKgiCbFE6RAEUOmswthCYoXscs5-WSrYmtielBKCY3jyZernA7E79IiRwBjbC7og87Yh-mEHlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور، جی.دی. ونس:
اگر شما اطمینان ندارید که دولت فدرال از پول شما محافظت خواهد کرد، چرا اصلاً مالیات پرداخت می‌کنید؟
🔴
ما تلاش می‌کنیم تا دوباره اعتماد مردم آمریکا را به دولتشان جلب کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147445" target="_blank">📅 21:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سی‌بی‌اس: در پی تعویق مذاکرات ایران و عمان درباره تنگه هرمز، قیمت نفت به بالاترین سطح خود در چهار ماه اخیر نزدیک می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147444" target="_blank">📅 20:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sigVSY6nwCPdf0PalxmyMVsgOTLdTl-LufW0cIBeWdEHWCROy44Fvi_7cavxrTHsOIXP4sh8ZG7LIWLm2I7IuuRZvUPylXnF047OreZKeNpdOI_VaNmaCPtj8HdGt5X2zTZqg6ZMnFgvRC-0zlCoT1JuFNJIagKCxfBRyED5pR778f0FM7f36RDns4MRKhMZbfL3ll_YCPaFbIHHOKbVNFRMd39-7J2kI8AqQdpeetrOw3bDa0ZqvGQ-7UtZ2Ke4dXvxSbCCdzj3piRL_h8NsfctKhW309S6rTq3b9J8wZhRwwdwZO1TW84lPaEpie567aI2uAAzMK4KZe02WPC5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیامکی که داره برای جانفدا ها ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147443" target="_blank">📅 20:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/percFomUt960uQLuKavRNess5jw-r8r-YcWgKswfQomeXPvcsYJ5CFmKI2aRb-qxHnVIJ4AQjltWGz-N6mhaTSXi5d_o1sPPkQPrQ3gxPewZvabplfO6Ws6EQ6zPCI_00tlqhrxSaRCpxktgI1gK9O2921Spwn1D-NZxQjx3JvnFac3GoL37nHLCC96NHa9Ue_3oITbO5Jgl8H7EM6-R_dKN2Ob5jc3VQ6KA6cUc14H4rhCF2dEyJfcL_qSElPtsX5iRHmFFV0ix5XU1hS5PqtLMN9bGv-YZODm9dOdYtjsAM5OdSlSYZyOBn440ZWIZkVU6xAJpndoHy3UksUbdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر استراتژیک نفت ایالات متحده به ۲۸۵ میلیون بشکه کاهش یافته است، که کمترین میزان از نوامبر سال ۱۹۸۲ و تقریباً ۴۰ درصد از ظرفیت کل آن است.
🔴
این ذخایر در طول چهار سال گذشته، دو بار به میزان قابل توجهی کاهش یافته‌اند: حدود ۱۸۰ میلیون بشکه نفت در دوران ریاست‌جمهوری بایدن، پس از حمله روسیه به اوکراین، آزاد شد، در حالی که ۱۷۲ میلیون بشکه دیگر در دوران ریاست‌جمهوری ترامپ، پس از ایجاد اختلال در جریان نفت از طریق تنگه هرمز به دلیل جنگ با ایران، مجوز برداشت گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147442" target="_blank">📅 20:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147441">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLedfrLm7OTxaXIbWmV_cu9PbvpuD1zqDAq_TaWj1rTLPoV38obpm1dGSd3rlrJlRtNuWiwOvSC7fvNvLfJK0Vocpax0U6cQ2eKAj8xnO_NeKqveEP1j4NdE9C7Wgqyx_dDXdrP0SSarGUTTHQ35Y67mNE8FT2yYJsr70D2IgfKShZkCHy1FEjG4DCUfIdYGGON31795uE3YwIV7sJXNIiy0awrvzkHxbFjW_JEcf68TgqXvRrzhYJkGIzj4jLvatZj-zDzctEk7TA8F9RymMX3FlOskLSgGfr3mgRFxUneDb3YsaIDdp_m0KNgl66A2kDCWEaJm0QXPLZS8-WFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی الزیدی، نخست‌وزیر عراق، گفت که عراق به «پایگاه پرتاب حملات» علیه همسایگانش تبدیل نخواهد شد و می‌تواند به «کاهش تنش‌ها و گشودن راه‌های گفت‌وگو» کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147441" target="_blank">📅 20:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147440">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منبع پاکستانی: آمریکا به‌دنبال توافق مرحله‌ای با ایران است
🔴
یک منبع پاکستانی آگاه از روند رایزنی‌های دیپلماتیک برای پایان جنگ آمریکا و ایران، از احتمال حرکت واشنگتن به سمت توافقی «مرحله‌ای» با تهران خبر داد.
🔴
این منبع در گفت‌وگو با «ارم‌نیوز» گفت اظهارات اخیر دونالد ترامپ درباره احتمال پایان جنگ پیش یا پس از انتخابات میان‌دوره‌ای آمریکا، لزوما به معنای نزدیک بودن یک توافق جامع با ایران نیست، بلکه نشان‌دهنده محاسبات سیاسی و نظامی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/147440" target="_blank">📅 20:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147439" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147438">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTK1A0FDP8NGK6OJuVywV4ehO2Xy-9NF5u3YR3rsnVg6hxoA0mXD-ZOQtDPNZIWOpfNfVxALyArJgx_iC2Kz7L_SaitN5wEB44jNGd-AYFD3uNpC5SUfm6T-vsxZXGbFiErIGD9MacjebGC1KiC3JRTmb3tR0XzJIoYgi-xOrAwofiWb7nEwSEAPmlZG8mZ2qW3ssgZ3adDUebUn0T7lRpkmliaAMKAiArlWryAeepy1WRSAcVgvTott2voH3hPgAM5L7upX-WUV9t6W2npPbszrJViArJ7-zttmogTQdyOvdAv4fNUX4_dtKlWN578FoQ5B_yEB3CBPitcUr8mSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی در تلاش است تا حجم صادرات نفت خود را از طریق تنگه هرمز افزایش دهد. این اقدام پس از آن صورت می‌گیرد که حملات پهپادی باعث توقف فعالیت خط لوله مهم شرق-غرب این کشور شد. این خط لوله، مسیر اصلی صادرات نفت خام این کشور در طول جنگ با ایران بود، به گزارش بلومبرگ.
🔴
این کشور پیش از این، در ۱۰ روز اول ماه سپتامبر، حجم صادرات خود از طریق تنگه هرمز را نسبت به ماه آگوست افزایش داده بود و اکنون به دنبال افزایش بیشتر این حجم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147438" target="_blank">📅 20:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeC5UlauWAXGhsr6w8mOrI7aOCbtxoGjrgAenN14YaoLryOF6i6cBHZgo80wnA-OGp321xjkuYTPg6j4090vC1Btqni1z8HPRfbUsYqEuQ3JTfxdn0fvT7lBQJcUw7yscbBIdatBs2sVHgKcgpq39hctYQ0vzFxLJ45HVLQlHJmOW1FYatprhEQRa08fXN2jRO3Y1jKFxhffFyFL44v9jJ29iyuTbVqlR7y34-QpTor5X7mheMWqGAPowXHzRRFqnCR_czhXJyA3V5QEpGX6a9jPBKycRQy5GthpAoWaBL7et2Fbdso_t2KQKDFlAen_1rzheCEs7Ol7FMF-Fcpo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : امیدوارم همه متوجه شوند که افزایش قیمت‌ها در سراسر آمریکا ناشی از جو بایدن و دولت او بود، نه از "ترامپ".
🔴
حتی قیمت نفت در دوران بایدن بالاتر از قیمت فعلی بود، و ما مانع از دستیابی ایران به سلاح هسته‌ای شدیم!
🔴
با استثنای موقت نفت، قیمت‌ها به شدت در حال کاهش هستند، و به محض پایان درگیری نظامی با ایران، قیمت نفت نیز به شدت کاهش خواهد یافت، و این اتفاق به زودی رخ خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147437" target="_blank">📅 20:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVCB1s2S7-ySBoSsfK4dR6f19b7CWNAW05_z1kHXH4rvlYgsqdHG7TvKAXbmPfyais6PNk4ext4R-FGqfb8zU05I75NFoLxyfXPcU4BHPFKiVEDtEKtf057ULcWzjiZwpq6ayBvPgcfh3upHG3pEIXlAPWsHSbQX7Z9X_KXM2jXY2r22BkmCjbQfnH7IrKaU0fGgcfeqponipl2uk3aOAz2q-WutT5mxeaPtup61dJzibMMHEA9KP924lXVCCwEgqWXNGQY1gGPX2qN8SQhpnpIxzZ29Mf19sD1QowWd829OIkpZdRwFWTg7z1s8lvxaVtnysyXVARlkliJyRjAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کشورهای جهان باید هزینه اقدامات آمریکا در تنگه هرمز را بازپرداخت کنند
🔴
دونالد ترامپ گفت: «نفت از تنگه هرمز در حال عبور است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و در نهایت هزینه‌های ایالات متحده آمریکا را پس از پایان این درگیری بازپرداخت کنند.»
🔴
او افزود: «ما این کار را بسیار بیشتر برای دیگران انجام می‌دهیم تا برای خودمان؛ کاری که نسل‌هاست انجام داده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147436" target="_blank">📅 20:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: بیشتر از هر زمان در تاریخ سلاح تولید می‌کنیم و این سلاح‌ها به طور روزانه به نیروهای ما در خاورمیانه تحویل داده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147435" target="_blank">📅 20:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKzVE5vTpuVpFqlCe_xVemc2pmDIP8FCrFAZZBlkSM4kgV2mBzHjpk2-g1E_g4yhmPmI2DbycAhCs5imPYOvrp_h2xfmZhZRW_57bj8pHKXE3seDT1PpilLAugTwvKWe_zpXGMDaWbheIIqf6ncGa5djyOvFOSHdZ50m5GoOY7394zLqxB5Lb6rAgd4BDqsaxu2IUPY5Nqjz78GHj4MYXIxfD_gpcf2Aa3bx69GdCShmRruq86AGY1V2l2PIkKDKrC7EelYRvzpQO1bSmogCiXvyQsHQEqaraSNjXCMZdDxyPjLXAXzhHPAKQkGpklzSfeS7Wv-2qfm4vuSc5H3zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من به تازگی گزارشی دریافت کرده‌ام که نشان می‌دهد ایالات متحده در حال تولید سلاح‌های فوق‌العاده و پیشرفته‌تری است تا هر زمان دیگری در طول تاریخ خود.
🔴
این سلاح‌ها به طور روزانه به نیروهای ما در خاورمیانه و سایر مناطق تحویل داده می‌شوند. کارخانه‌های شرکت‌های دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند، در حالی که به طور متوسط، 4 تا 5 کارخانه کاملاً جدید و بزرگ در حال ساخت هستند.
🔴
تمرکز اصلی این تولید، سامانه‌های پاتریوت، سیستم‌های THAAD، موشک‌های تاماهاوک و سایر سامانه‌های موشکی استاندارد است، که ما از قبل تعداد زیادی از آن‌ها را در انبار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147434" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رویترز: داده‌های اولیه رهگیری حرکت کشتی‌ها نشان می‌دهد شمار کشتی‌های باری عبوری از تنگه هرمز در تعطیلات آخر هفته به رقمی تک‌رقمی در روز کاهش یافته است؛ رقمی که به‌مراتب کمتر از میانگین ۱۴ کشتی در روز طی ۱۰ روز گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147433" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو: ماموریتی پیش رو داریم و آن را به زودی انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147432" target="_blank">📅 19:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
دلار میریزه یا بالا میره
⁉️
🔴
تحلیل ترسناک هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147431" target="_blank">📅 19:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
عراق توافق‌نامه‌ای با فرانسه برای خرید سامانه‌های پدافند هوایی امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147430" target="_blank">📅 19:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCYAxBMuJldv8mGCJHnMpOn7FdE1RnhY3Fqh-zYJnjTfpuTgDJFA6D3EJs4cVOMj16wFdzw1CMck7yeVOu85HRdQm9k9ZTezptWdQQ3wBxzhmwwZvh0O2XPXuY6nX0h4ZJVAPEaM1kd43EG4ydnIyLMgKx5-lSk315ow9qDpE72U1ErWHKaxa_K1_-YJS75BU0Pyuf2-nnKleKd3aGnlIbe44XNd1GJMZyBxOVjPcjinzaR9SufDqVJ5BP7co3B07gI2oR9MWn6ceZPKX0p6RR78bxKZ4_K0mFzcmA6uuqBUQmYxWoBYhtAY6ErcEkeVhHEBIe1o5uOnMOzE6jUYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش می‌دهد که پالایشگاه‌های آسیایی خود را برای کاهش عرضه و افزایش قیمت نفت خام با گوگرد بالا آماده می‌کنند، چرا که منتظر شفاف‌سازی از سوی عربستان سعودی هستند. این اقدام پس از توقف خط لوله شرق-غرب، در پی حملات روز جمعه، انجام می‌شود.
🔴
قیمت نفت روز دوشنبه حدود 3 درصد افزایش یافت، در حالی که شرکت سعودی آرامکو هنوز اطلاعات به‌روز شده‌ای در مورد تخصیص‌ها و برنامه‌های حمل و نقل به مشتریان ارائه نکرده است.
🔴
برخی از پالایشگاه‌ها از احتمال تاخیر در بارگیری نفت از بندر یانبو در دریای سرخ مطلع شده‌اند، اگرچه تاریخ‌های جدیدی اعلام نشده است. سایرین نیز انتظار تأخیر را دارند، زیرا خریداران برای به دست آوردن مقادیر محدود نفت خام با گوگرد بالا از عراق، امارات متحده عربی و سایر مناطق رقابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147428" target="_blank">📅 19:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3tT7NzTPRycadHhOE3cPm3BUQQySumegp2V--zo_0VwNbSos_uBH5fHuxO6p-lvHeHNlub_Ueb332okuxilLC8AeudDgQ-h4q6CENIhPDwQUMOQroS5sVQd2RP5q-fD4JRXbdeNTPRhq1Ke-mjoAZudlis7_a_sYD97rUCBwN6vCNtkbNJJEu8pM9e50WefBITv-sfIeNvn6dNy3aSRIKpzAWlVkyhYmcqYLmqd5fOXjsdJ_-2f3rJhUZKdGLR1BLh8T6-Uir-T7zGYp9x4RIgnB1hf8euNyg1cit9026Qfxe6mwgqwbHBL6_Kf8uA58YKYdkhQCadQ6OskSXzXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس مسکو در پی بیانیه ترامپ صعودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147427" target="_blank">📅 19:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a9fa4d5d.mp4?token=e0HF_boYLtz9bR4cFpG4asmsAhkbPofx8yUxeEeJl9qBXTIOBFv4C5x0qKGLdxq0kBU8CxcXNwWCbIqRFsRB8fRIw9wAEM6K07Xrz8Con2RT4OzTYUQ4FliwxnyLjPPyicr-MfGi4QdBtqf12VoFu_MghOPmuPaIjklYcQjKqxGF0762NwJaO2IXU1vfGcJ7-oIqmi88UhudHW7tIWig274li1dxGqLGFj-ZxMbhHu6uiOkOuFqsDtRwVwOMuH4B7dVpi3zcuorQCScDzFwMANLpS55TKH5FJrFsEFzq6iNBYWILF1F3FWeZztQ7D5ukn01GvF3I74m0j0PJZ9SB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a9fa4d5d.mp4?token=e0HF_boYLtz9bR4cFpG4asmsAhkbPofx8yUxeEeJl9qBXTIOBFv4C5x0qKGLdxq0kBU8CxcXNwWCbIqRFsRB8fRIw9wAEM6K07Xrz8Con2RT4OzTYUQ4FliwxnyLjPPyicr-MfGi4QdBtqf12VoFu_MghOPmuPaIjklYcQjKqxGF0762NwJaO2IXU1vfGcJ7-oIqmi88UhudHW7tIWig274li1dxGqLGFj-ZxMbhHu6uiOkOuFqsDtRwVwOMuH4B7dVpi3zcuorQCScDzFwMANLpS55TKH5FJrFsEFzq6iNBYWILF1F3FWeZztQ7D5ukn01GvF3I74m0j0PJZ9SB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرسش: آیا آرزوی تصدی پست نخست‌وزیر اسرائیل را دارید؟
🔴
بن‌گویر: من معتقدم، بله - به امید خدا که به آنجا برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147426" target="_blank">📅 19:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بحرین: عبور از تنگه هرمز باید رایگان باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147425" target="_blank">📅 19:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
حمله هوایی عربستان سعودی به المخا یمن
🔴
منابع خبری از حمله هوایی تجاوزکارانه سعودی به شهرستان المخا در یمن گزارش می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147424" target="_blank">📅 19:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رهبران اسکاتلند، ولز و ایرلند شمالی در کاردیف دیدار کرده و بیانیه‌ای مشترک را با هدف دستیابی به استقلال از پادشاهی متحد بریتانیا امضا کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147423" target="_blank">📅 19:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نتانیاهو: ما در حال مبارزه با تحریکات یهودی‌ستیزی جهانی هستیم، اما وقتی این تحریکات از درون خود ما سرچشمه می‌گیرد، غیرقابل‌تحمل است.
🔴
اکنون، دو کارگردان اسرائیلی، ارتش اسرائیل را به عنوان جنایتکاران جنگی معرفی می‌کنند و جوایزی را در جشنواره فیلم ونیز به دست می‌آورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147422" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYRhjtUlHfnbtaBlMNrI-Ln1KIpQw3PoQdl4r_ERQ_0DS6vUFbjsEIqCELKh6UmaYqX2WweCgfM6a6yp0fmpeWhQGeRItoWsKnMOyp0tqfu3Cs8kDQEQjArm6XUg3WCDLU8XKZpoaijHPdSjBIX0NmA4kBB9AKahOkPIJOOTMgxZZKa7nT_ZxjOzaPX7CstRI1shmFq96znhPrI8ekOfOxMvCKN1e6MdqIFmKz6hAgadFWxreD0NXJ8IkoZnD7MZCoeWIIwt2mKsEDoIbO2kRmTITx6nHlou-3Sc-RVi77XK1eoaej8VFGU8M8OJzOAEHPjRBqCcwhSpRGk2lU37GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
«دولتِ در حال شکستِ [رژیم] ایران می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
🔴
من تعیین خواهم کرد که آیا ایالات متحده آمریکا تصمیم می‌گیرد وارد مذاکره/تعامل شود یا نه — مفهومی که ما نسبت به آن گشوده هستیم.
از توجه شما به این موضوع سپاسگزارم!»
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147421" target="_blank">📅 19:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAosuwPAqdCo-CiJoz9Ok6D-Qk0ozWSje7DmYfIozQhsh2XsSouXRAXukoIu8ZECGZ8MwHlOcaeNhkE7hQKad_Tlo91RO8cfp_inkA4kX2RffYdtWYkBdbjIR4aikGYro_yIiH2wY5M3AdYvtW_3STnqTureygKCR5_h3lhlwDkE30v81Y3F9PUF1gDfXDbFh92gouIlFpIa678Jtff2LeiaJE3r0QXpAsiCboEi6zlLwMqtY6sk_e-u-3efsXpZ6B1ao89ABXsxplz27I-nE2yuuMXXAaE7XMhP0eI7z96izujzau8kDDFE9FvebRqkqrk5a5aL1nUatd3QHXfT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه داری آمریکا:
وزارت خزانه‌داری، عملیات "منزوی اقتصادی" را آغاز کرده است تا تمام منابع مالی را از رژیم ایران و کسانی که از آن حمایت می‌کنند، قطع کند.
🔴
به همین دلیل، من بار دیگر از افرادی که اطلاعاتی در مورد کسانی دارند که به فعالیت‌های تروریستی ایران کمک می‌کنند، خواستار افشاگری شدم.
🔴
به هر کسی در سراسر جهان که اطلاعاتی در مورد این منابع مالی دارد: این فرصت شماست. اگر اطلاعاتی دارید که برای وزارت خزانه‌داری مفید باشد، ممکن است واجد شرایط دریافت جایزه باشید، مهم نیست کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند.
🔴
اگر چیزی مشاهده می‌کنید، آن را گزارش دهید.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147420" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4IjMRLlw8xKzh0o1-lIQaS-H6BuotPYEliX-grmhEWRu4eRG2ZpEEjoL1yNjNRLa07sdzkGZ9vga33JbrmY3uneHa8w4UvWC1DJadDNDArvrkGEOtA6tdxyXkEiq03Ww2BUTXFjOK1P83C3hWTVtUtj-5GJThYprGgWD4le5OAKvRcfrOiVa-UfE8wvyeTo4KEAXk58e5cMS07kjbBjYOtq83KgSvqp3m767xXIoouISadEj1a5O5TWR4YJc6ChM1qq_IR46AIHL_wWyiUjwcXHMcS-XKetxsivT9rg4K5DRff3TeWMUvlLBzxo_tePcQmJqwf1uHtEmIaqx07_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سریال خاطره انگیز قصه‌های مجید به دلیل اسم بی بی دیگر پخش نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147419" target="_blank">📅 18:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP-iVHIgQrYvd3b0FgEDVMBwMpK8JfZqv6Foj_5ZV5qfJSlKvLOIlUupg0rY4VPCr72czXfs_Khqp22ps_g_LxXZvJhUNWZo-XVNl2oxbD79sshfO82N8Ol0V9SNC-d3T7n-K7apUqMONpqft3JsBNs90v904q_YkJElu6m9qzZWfYQAEsv0HWU-K1QkuF-0iajDpRnjM5_m6psTxu7MlyPC1OJMSzj7khiK8xyDzNnKMUyDq7XyDuEUlflXMPmt4ij6CAqoU36bf62IxEWscgj9SdT4u_Ug_Zesm9DbkZSeH6LH63UujONx7PQlxwz4Tv-mYYy6pO_B5ACBKfS71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند
🔴
افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147418" target="_blank">📅 18:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
طبق گزارش ها عربستان سعودی برای اولین بار چندین موشک بالستیک ساخت چین را به سمت مواضع حوثی ها در یمن شلیک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147417" target="_blank">📅 18:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=af_nEjvcIS4jPXO2VDr13SEYOpWKBnACidF5rIB8pDNrvAt1i56y6l4A8Z5bvzf6Mn-Bcgf_aB2adm67tuMsNIUJOS5_YUQMcQtB6Ck8fYdXqCFVi4yk_p3hzaelG3ZxwbcJxNGCmBgBfVLMNYnNB1tomWkf6LO50raN-npG6DWgQREJjoTj3yR8P4nbNouJT38yDPXLVUOs4-3JMPpGU07ukDesJjZYpHH1RgKR-Heme-46nmQimWeDqzfRe9vwRwKjhOCQFSRHyBSuyiDRdAWnTtilE2kTMUru7ESArDrXGKnfFskJEGo0C7_42Rz1439AExMjURY1pAdCl3ubaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=af_nEjvcIS4jPXO2VDr13SEYOpWKBnACidF5rIB8pDNrvAt1i56y6l4A8Z5bvzf6Mn-Bcgf_aB2adm67tuMsNIUJOS5_YUQMcQtB6Ck8fYdXqCFVi4yk_p3hzaelG3ZxwbcJxNGCmBgBfVLMNYnNB1tomWkf6LO50raN-npG6DWgQREJjoTj3yR8P4nbNouJT38yDPXLVUOs4-3JMPpGU07ukDesJjZYpHH1RgKR-Heme-46nmQimWeDqzfRe9vwRwKjhOCQFSRHyBSuyiDRdAWnTtilE2kTMUru7ESArDrXGKnfFskJEGo0C7_42Rz1439AExMjURY1pAdCl3ubaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو خیابون شریعتی تهران، یه خانوم با یه پیرمرد سر رانندگی بحثشون میشه و زنگ میزنه به شوهرش که بیاد.
🔴
شوهره هم به این صورت میاد و با زانو حمله می‌کنه به پیرمرده و درجا میکشتش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147416" target="_blank">📅 18:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تلخ
‼️
تله‌کابین نمک‌آبرود نفری یک میلیون و صد
خانواده‌های ایرانی اغلب با دیدن قیمت
منصرف میشدن و میرفتن
تا چشم کار می‌کرد توریست عراقی بود
توی صف
ایرانی‌ها توی پارکینگ با کاردیاک
عراقی‌ها سلفی می‌گرفتن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147415" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرید، برادر زن سابق مجتبی خامنه‌ای : یه روز با مجتبی تو یه جمع فامیلی نشسته بودیم، یدفعه موبایل یکی زنگ خورد ، بهش گفتم این چه موسیقی هس گذاشتی ، بعدش دیدیم آقا مجتبی وارد بحث شد و گفت این موسیقی رو نمیشناسی؟ این موسیقی فیلمه کریستوفر نولان هس ، اونجا بود که همه پشماشون ریخت از حجم اطلاعات و سواد آقا مجتبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147414" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=CGmiaY71rqMdD2ci3_NK_29nDwb92R1R8GyR8AjWssHB9J--Cc0ThI_IaYDIQYuVY_vQUe9SIcwYbGs0thMvaK8cDTsHfyhgqesmxQoFaQYEtTvsz4S7S3vps76GHuJdiReQTB4Aiu7GAYFILWQkVI3sXFc_yYA9NJqczzcpnMzGbrRZd-ilU0CYNkOXDYYnheeyFo2mx9vXosDpNv-CQp4u14EXETN2TwGs_YMvsQURj3dVoDO3rwdOBBYj0Ql2Q-IE0RsdqdGOQQNRCZ1m2bG_wVGA9cLlY4TMQ0JVc2ktb66OwyOlmJjn3cOdfuO4bVKxdvZ4xFqv9aLIxUnhYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=CGmiaY71rqMdD2ci3_NK_29nDwb92R1R8GyR8AjWssHB9J--Cc0ThI_IaYDIQYuVY_vQUe9SIcwYbGs0thMvaK8cDTsHfyhgqesmxQoFaQYEtTvsz4S7S3vps76GHuJdiReQTB4Aiu7GAYFILWQkVI3sXFc_yYA9NJqczzcpnMzGbrRZd-ilU0CYNkOXDYYnheeyFo2mx9vXosDpNv-CQp4u14EXETN2TwGs_YMvsQURj3dVoDO3rwdOBBYj0Ql2Q-IE0RsdqdGOQQNRCZ1m2bG_wVGA9cLlY4TMQ0JVc2ktb66OwyOlmJjn3cOdfuO4bVKxdvZ4xFqv9aLIxUnhYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بیمار سرطانی: شب‌ها که پرچم تکون میدید اصلا حواستون هست که ما دارو نداریم و داریم میمیریم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147413" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=QfECycaKqdmzddHm7TxutJmIOpPsiwSLBKAh1BM3xuFzTfC7ZPXU79oZw6LtNpWO4dAyWMFVI_M7jMVWmEduUq-vvQqgSs08cAfdTI_4t5WrcAYS_7TwVACqgdce8z4cIEvuJCoZ-XVfjtLWDFWpkU-hkjao8Slp0bqqAPVD2HJT7rx4ghK_CM37K08OvnSsGRCNUwv-g4xyEyvF5gQGDuGI8oPWNn4cJCy2Gzz5vMdD65ZP07TvEW-nLhMz_5oBUk3DQzCxARO9wgDZlpGTpJEFDSWb6ACJO7BSHA7mOEoMKLA1k2Scwny3zax8t-Lm37u-ZJ-Tw_yEBqblbe_lbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=QfECycaKqdmzddHm7TxutJmIOpPsiwSLBKAh1BM3xuFzTfC7ZPXU79oZw6LtNpWO4dAyWMFVI_M7jMVWmEduUq-vvQqgSs08cAfdTI_4t5WrcAYS_7TwVACqgdce8z4cIEvuJCoZ-XVfjtLWDFWpkU-hkjao8Slp0bqqAPVD2HJT7rx4ghK_CM37K08OvnSsGRCNUwv-g4xyEyvF5gQGDuGI8oPWNn4cJCy2Gzz5vMdD65ZP07TvEW-nLhMz_5oBUk3DQzCxARO9wgDZlpGTpJEFDSWb6ACJO7BSHA7mOEoMKLA1k2Scwny3zax8t-Lm37u-ZJ-Tw_yEBqblbe_lbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
باجناق برای سرقت طلاهای خواهرزنش، دو سارق اجیر کرد!
🔴
در تهران، مردی که از وجود طلاهای خواهرزنش خبر داشت، برای سرقت از خانه او دو سارق اجیر کرد.
🔴
سارقان پس از ورود به خانه، دست‌وپای فرزندان خواهرزن را بستند و طلاها را برداشتند؛ اما در همان لحظه، صاحبخانه به خانه رسید و سارقان گرفتار شدند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147412" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
زکریایی، کارشناس حکومتی: حکومت امیرالمومنین هم فاسد بود پس انقدر به ما گیر ندید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147411" target="_blank">📅 17:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در تنگه هرمز بر اثر شلیک موشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147410" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=rM5-2ECpuXyskuZ4inFg3FvKanzkBxuKK0YeRQ5LdFxEeeG67pLvrzXMcxbFkxDEddd615IxXVGaquZT1W3zKawi70magdBaPhds9pmpexyu01uzepgb9HO7SxlZJW02FyUgTLrdiL8HHQiRsifB5cvy0ZfIPdOgrQNUYsDMy16PjVvWQCKdXrwpV0Z6R52U8rR7luAIGu5smfETnlnDm_tFhLDAMjQNji8wW7cIUoaMRxnjOaosCrknDGFIWvkOM-C5vv7nEW-__qnwFsi44gPW_0gIkWAmnEP9bIHMpaZuP7m9R52L8k4EBejsCs4RQ8CDa03anoAauoLqssmHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=rM5-2ECpuXyskuZ4inFg3FvKanzkBxuKK0YeRQ5LdFxEeeG67pLvrzXMcxbFkxDEddd615IxXVGaquZT1W3zKawi70magdBaPhds9pmpexyu01uzepgb9HO7SxlZJW02FyUgTLrdiL8HHQiRsifB5cvy0ZfIPdOgrQNUYsDMy16PjVvWQCKdXrwpV0Z6R52U8rR7luAIGu5smfETnlnDm_tFhLDAMjQNji8wW7cIUoaMRxnjOaosCrknDGFIWvkOM-C5vv7nEW-__qnwFsi44gPW_0gIkWAmnEP9bIHMpaZuP7m9R52L8k4EBejsCs4RQ8CDa03anoAauoLqssmHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار کرمی:
نیروهای دلتا فورس پس از هلی‌برن در اصفهان از ما ترسیدن و فرار کردن
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147409" target="_blank">📅 17:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای مکرر و گسترده هواپیماهای جنگی سعودی بر فراز شهر طائف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147408" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147407" target="_blank">📅 17:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: لاریجانی زندس
😂
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147406" target="_blank">📅 17:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckWfRYSLHmPmDtLa4JYI-Su06MU5HoHTMJoQIEHHcHLpmWJ_lLnVdjCogP4dps1gD4_leSyh9Ufb1PD8iQc5-CcKmnLyFYhM7SRDTwJQjgQitizAL0nP8eHbz0oH-HVgEzip9bkk9kdpCzYWVeyFupkm6EYOrhwzyMQOjsKgXQAOBG2Cyf8UZYkTUcrtXHeaDN_wmyXeGewZKmsSJCv5Y3Mx7Vr-N3cBI-r_bV0W2P6yyxo2fGphi0431ldY9tkCCMaTse0xgMIVM881FB-xg6BHwSr8wtf6HE-MKesGSsQgW_8QDvGUde85Cz7zHj7-VmoYQbunwHVdi-YGcKgZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
روایت آمریکا جعلی است و هیچ خلبانی نجات پیدا نکرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147405" target="_blank">📅 17:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولین طبق معمول دروغ گفتند
‼️
🔴
نیکزاد، معاون مجلس،مدتی قبل: آمریکایی‌ها برای خلبان نیومده بودن،اومده بودن اورانیوم ببرن که بازم شکستشون دادیم
🔴
اما دیشب ایالات متحده فیلم نجات خلبان رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147404" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / لحظاتی پیش دفتر نتانیاهو اعلام کرد:
نتانیاهو هفته آینده به آمریکا سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147403" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=omY-BYuiNv0-vWGLKiqe-TFba6wlSA0cKjbU4WXUktWfmw6Pl7Qhh3RB_HZqCxCkwj3Qfi7_X70o01uBGeHTbqxwkeaqYKV1ugk8dppZ4aR70aziq2n9yQHPHogM1iqWtXhRx09k9nJgWosQ05nwj8fuQuBwc6ew3_bmpwFp1zqAljYfKTRQWIfitJ9EYwhzjIyPZqEMssgPyEGbw24TqHDnfb1UtCrPpTXQ8S3-NLG8Ln3LfMWVsn0AUuOiqSH2OFmiwOR5mSzXOgz1GBhoDbrzS6pP6gliNmwbvgHj-KUqocBXzg07YN7qJYcUhCuVtNDf3iscK3BIzeN7qcz-7X44NdW4tSMDWmr60Q6dWutJcBCXM7BrzxmNQ0vY-iaoH6Y41QIACvbpz8-v9aNjOWcY2v9h2-HLZVxDjtUW2zHmH7PQYZt64Bu4nhX4FrGd5P3mkXjkmGZpg58ZlG93SMLt6lcndLJk1DnY98ZY4YcvKIgWqIdPJ0HE56BQC0yR2y8DI2Oxd0FIJz9HyH-wBTgnFfDhyCdd_vfmPiHUhIZakkym-TmUL9ps4ZG8GsizmFJTLK1HNvhmY14KM_Bp7DRAVVjmBNIPD3mA70GRMyq_cbU24W0aCBgZYWXNIgeEeaXMaSqcDUU2pQclQGdSx5qk97sQXXuESs4kM3I0wTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=omY-BYuiNv0-vWGLKiqe-TFba6wlSA0cKjbU4WXUktWfmw6Pl7Qhh3RB_HZqCxCkwj3Qfi7_X70o01uBGeHTbqxwkeaqYKV1ugk8dppZ4aR70aziq2n9yQHPHogM1iqWtXhRx09k9nJgWosQ05nwj8fuQuBwc6ew3_bmpwFp1zqAljYfKTRQWIfitJ9EYwhzjIyPZqEMssgPyEGbw24TqHDnfb1UtCrPpTXQ8S3-NLG8Ln3LfMWVsn0AUuOiqSH2OFmiwOR5mSzXOgz1GBhoDbrzS6pP6gliNmwbvgHj-KUqocBXzg07YN7qJYcUhCuVtNDf3iscK3BIzeN7qcz-7X44NdW4tSMDWmr60Q6dWutJcBCXM7BrzxmNQ0vY-iaoH6Y41QIACvbpz8-v9aNjOWcY2v9h2-HLZVxDjtUW2zHmH7PQYZt64Bu4nhX4FrGd5P3mkXjkmGZpg58ZlG93SMLt6lcndLJk1DnY98ZY4YcvKIgWqIdPJ0HE56BQC0yR2y8DI2Oxd0FIJz9HyH-wBTgnFfDhyCdd_vfmPiHUhIZakkym-TmUL9ps4ZG8GsizmFJTLK1HNvhmY14KM_Bp7DRAVVjmBNIPD3mA70GRMyq_cbU24W0aCBgZYWXNIgeEeaXMaSqcDUU2pQclQGdSx5qk97sQXXuESs4kM3I0wTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: هیچ برنامه‌ای برای غنی‌سازی اورانیوم در عربستان سعودی وجود ندارد.
🔴
او گفت توافق همکاری میان آمریکا و عربستان بر ایجاد صنعت تجاری انرژی هسته‌ای در عربستان متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147402" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=Nu-65V2Re7Z2RLUfFp1lb9FETUMqp6xmsc4tH4_DiI_SKoyynrbQvQzdxyfaeEPm-ItwBk1tqGJzh5mOWPszQhe3buibef19RzZNexG6gY6XcQcxpjfdlnHBW9RSQ3WaUeDh1PtnmfORuyD7GxIyIbLMutWzv4wr5LbgyIEdoknwLkCWBg_PYUwmI9soL6KOwYySpe_n0r9L2UQxylN-yjIkkk4ExwZVaapKhBxdAqUcs12e5orRDytVj7QsMKp9LBNngtlffhHxORIecth85cBS1IrWCGxoGltFqs3jfPi1d1JRxSt6S8Y-D5WGehgk7X5m8nb09ewWTHKfyRk7piSezQEg1PRQtETigvY2e0lhw8ouTgYzfYsjUgG5x5QVPvVBkXJWcZ9orCORQHRKL97dO1nPbIaVClt2iKo0wbC3uCJQTpoAv0YT9LVU1NjDm7uPWK6BUXwMHvfncyLuAgsfKR0AhzyTXUrKV7hQb4AQj4PZXT6d3eLXk8fn32nqCUZuOYIzrwIxno86RD19c1zI4T82yWZe9DJaN2f6nXenAXLVRgEgh4Q5drBfEPjuYlTnO0ZkDXFFp1TQ1Q4pUXDif-ovyOTe8YhXSn5RL6cZSRPcaMEKUHFrtTUezt7lkvdytGrmNVsIQwhiIw2boJlJfebohGhHHRjUat1x554" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=Nu-65V2Re7Z2RLUfFp1lb9FETUMqp6xmsc4tH4_DiI_SKoyynrbQvQzdxyfaeEPm-ItwBk1tqGJzh5mOWPszQhe3buibef19RzZNexG6gY6XcQcxpjfdlnHBW9RSQ3WaUeDh1PtnmfORuyD7GxIyIbLMutWzv4wr5LbgyIEdoknwLkCWBg_PYUwmI9soL6KOwYySpe_n0r9L2UQxylN-yjIkkk4ExwZVaapKhBxdAqUcs12e5orRDytVj7QsMKp9LBNngtlffhHxORIecth85cBS1IrWCGxoGltFqs3jfPi1d1JRxSt6S8Y-D5WGehgk7X5m8nb09ewWTHKfyRk7piSezQEg1PRQtETigvY2e0lhw8ouTgYzfYsjUgG5x5QVPvVBkXJWcZ9orCORQHRKL97dO1nPbIaVClt2iKo0wbC3uCJQTpoAv0YT9LVU1NjDm7uPWK6BUXwMHvfncyLuAgsfKR0AhzyTXUrKV7hQb4AQj4PZXT6d3eLXk8fn32nqCUZuOYIzrwIxno86RD19c1zI4T82yWZe9DJaN2f6nXenAXLVRgEgh4Q5drBfEPjuYlTnO0ZkDXFFp1TQ1Q4pUXDif-ovyOTe8YhXSn5RL6cZSRPcaMEKUHFrtTUezt7lkvdytGrmNVsIQwhiIw2boJlJfebohGhHHRjUat1x554" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: ایران می‌گوید آمریکا در جلوگیری از حضور محمد اسلامی، رئیس سازمان انرژی اتمی ایران، در کنفرانس عمومی نقش داشته است.
🔴
کریس رایت، وزیر انرژی آمریکا: او یک فرد تحت تحریم است و ما نمی‌خواهیم افراد تحریم‌شده از تحریم‌ها فرار کنند. او درخواست معافیت از تحریم‌ها را مطرح کرد، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147401" target="_blank">📅 16:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=LcXhtDAnbUrgYvJYkkJ37vGjx9_30wywbbrkg2XzUvtqEc9ME4yk1pI4pvbpINntRnSy0QRx0ghaceN7xiXDYHZrkWAEVX37VwC-DJCc8N6QMlT16zZCr96S-CN3iVSvDTrubUn-PEsJMIpZRsfG7O_aBH-0jhid5WD9mEFQsHiaz3-w2b2sQBjN6R7U0QC-NxDtFOeRXPtxPFsTSzx08jEVcOMzcNq0pC0l9ETjcDee6VH_pc60FWEntPNLpJL37ATIzihq_e7SnfKVhbedqp96qy5qbqMnUX4dSvlHDjz6Rizvn-7u6z19oktPAzscs-H2qbg9UlJdZU2jPYDl_pKsze1PmK_XZ74WjQ7yIrS3JOeFiKQsae54BcEuX7Br0aaUwIKpV9h6G2o6hSwzysZD6mUXTW3UC89UcuPXTqtojwOeVUu3u_aFmsHn_oqT-DJJUSLxaJcl1KHZubiN4ZRH989B6j5mWxijymq7jvicUJNGruL7JBr1mpDJrHrGECjAjU9NjsNVbCJCKRek54XRQCYdJCSwbHQiqPfmdCIRv10byeDQihVSMjQg6IuFw_SLV8yK4VNCRZHByM6Lh0kvOilomIpD546Er4g6-4VHFng35A5cQCya5sNkC6jHnmitPHnpAd3bEeClBUGkQ1vKhcy9K3NFrWe91LVWK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=LcXhtDAnbUrgYvJYkkJ37vGjx9_30wywbbrkg2XzUvtqEc9ME4yk1pI4pvbpINntRnSy0QRx0ghaceN7xiXDYHZrkWAEVX37VwC-DJCc8N6QMlT16zZCr96S-CN3iVSvDTrubUn-PEsJMIpZRsfG7O_aBH-0jhid5WD9mEFQsHiaz3-w2b2sQBjN6R7U0QC-NxDtFOeRXPtxPFsTSzx08jEVcOMzcNq0pC0l9ETjcDee6VH_pc60FWEntPNLpJL37ATIzihq_e7SnfKVhbedqp96qy5qbqMnUX4dSvlHDjz6Rizvn-7u6z19oktPAzscs-H2qbg9UlJdZU2jPYDl_pKsze1PmK_XZ74WjQ7yIrS3JOeFiKQsae54BcEuX7Br0aaUwIKpV9h6G2o6hSwzysZD6mUXTW3UC89UcuPXTqtojwOeVUu3u_aFmsHn_oqT-DJJUSLxaJcl1KHZubiN4ZRH989B6j5mWxijymq7jvicUJNGruL7JBr1mpDJrHrGECjAjU9NjsNVbCJCKRek54XRQCYdJCSwbHQiqPfmdCIRv10byeDQihVSMjQg6IuFw_SLV8yK4VNCRZHByM6Lh0kvOilomIpD546Er4g6-4VHFng35A5cQCya5sNkC6jHnmitPHnpAd3bEeClBUGkQ1vKhcy9K3NFrWe91LVWK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوالات عجیب خوش چشم در آنتن زنده بعد از ممنوع التصویری: بلبل دارین اینجا؟ مگه باغه؟ صدای بلبل میاد!
🔴
چرا روکش صندلی نو رو نکندین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147400" target="_blank">📅 16:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGcQdmrufNNMXnJ7QmYNm6j2OfEmPe84XmThTKyQJj7-LMCmBlKrydDV7UZJZb2lImW0gbIo8WrOzsHlCr1aqS9EMGhqpaJyu7JKp2MNDBdbfRddFCAREKFcRKMUDJHylyU6qYGJmNNb4dDYOM39NFLT4Pe7ulBp3fuzqTkEoPyrpIWSbq2GRMPpbNq7slew3Pad7_MRz5nzEjEfnfZXwxChhnWngnDxpN6tWlSSKeKZCiT2O81obDROjFsKDLTuImvJaRKj63sAIPWqbRi3ai_SazoCxMWzplcr4Y872O3Y1c5GSKdUkLBRqt044l9YFthAQ7kP3M3IwWYUx3NZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو تهران (ونک) یه غذاخوری افتتاح شده به اسم کتلت بی بی که فقط تخصصش  کتلت درست کردنه
🔴
حالا قراره به دلایل نامعلوم پلمپ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147399" target="_blank">📅 16:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=p8xNSGcoT9mqRbUxIygK3NUfQ1kGxQoVnbqxiwfVxVhvDt97DwhOHVoLE_Cfv4bT7482TNq666ho7Zwmx6j7vj6wuVjcCcuR0cwaMBDY_Rz-ngNNBeKIbKw6CLJa4rTUcbr6G2befG63QfHKj7cumBIyrBmzv28FSTLZB5Q1I4Dqs0ydiQ2vwyU8g_gaVTb4n8Ygr71wdShiNOTU_eFhrj8XIgiTfvu-9xGkz6eGhUtHzav1rG8hoQ58-MPL6Ab6pVMwtt9_lyBGvyc3osVF-_WWY3STZfe84T8y0OBbJpecil_W3UDy5jcUAyynYK8nGufn4BDfy59kP4fPPNsU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=p8xNSGcoT9mqRbUxIygK3NUfQ1kGxQoVnbqxiwfVxVhvDt97DwhOHVoLE_Cfv4bT7482TNq666ho7Zwmx6j7vj6wuVjcCcuR0cwaMBDY_Rz-ngNNBeKIbKw6CLJa4rTUcbr6G2befG63QfHKj7cumBIyrBmzv28FSTLZB5Q1I4Dqs0ydiQ2vwyU8g_gaVTb4n8Ygr71wdShiNOTU_eFhrj8XIgiTfvu-9xGkz6eGhUtHzav1rG8hoQ58-MPL6Ab6pVMwtt9_lyBGvyc3osVF-_WWY3STZfe84T8y0OBbJpecil_W3UDy5jcUAyynYK8nGufn4BDfy59kP4fPPNsU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگردهای آپاچی عربستان سعودی مواضع و تجمع نیروهای حوثی‌ها را در نزدیکی باب‌المندب هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147398" target="_blank">📅 16:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ماهواره چینی که در فضا به ایران داده ارسال میکرد، به دلایل نامعلوم(آمریکا) منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147397" target="_blank">📅 16:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=f1ZuVA4H-KHrN_LHL20eLxCJrFgIa-p65VYXN4j30e3ebhIocwWpUkb_io0MBXBSihGicNNZ2xKkVbzzO4uNYTE_m4DjqlbjQHWZh8uCck0w7XRpEYykgI7W3ej_xiPzrmSWvDOOcp-UZV0mtF1NSnIpHqGbUAFk9o-cnRxkgGe0uTNjOW5Gfxt0b7yDzUsr1zyjB7YrVbjN1TWW6J7oiOEVMbf4hgTWSo0btKlhfC6MC3nwXCGjT4-bkVF9Ynw1itCjsNI_I3OMJNztyXN-xSNWvLkHpD_HYYlo81hcorIiZMqrrjfxPqz0icIjQKLrYx2saZGgWkR2s5ySewG6Eg4xIK6cWZjJxsAClA1KGmoSeP1x-b2reWadXasNQtXrwDHddear7IIFhLS1Wu31gq0VweXjF6RPStLM7XkUJk-amcNm49Mh3IpIw6uNBxfGm3_DFEaM6s3PP9D3anaPxwcr1HQk16myPp9zXXqp2mbg3EDAUpKZaSqBa17xOMA3P9mjJz8FcstwY1K8RuOIfHQPqnZK_c37ogaZy0ZPIcpD0UkDJTMIv0TfB6UAOCMbSdb541a9ZsCNcZx0_07-BEGFujVSOdmRF3UkoF6eJUd5CtUpw02RqgVbJPjqx8AIr9wrG6Wyy5yKqTIJbV5-8QwJ_tp-OXxbo6s1bYlF_AU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=f1ZuVA4H-KHrN_LHL20eLxCJrFgIa-p65VYXN4j30e3ebhIocwWpUkb_io0MBXBSihGicNNZ2xKkVbzzO4uNYTE_m4DjqlbjQHWZh8uCck0w7XRpEYykgI7W3ej_xiPzrmSWvDOOcp-UZV0mtF1NSnIpHqGbUAFk9o-cnRxkgGe0uTNjOW5Gfxt0b7yDzUsr1zyjB7YrVbjN1TWW6J7oiOEVMbf4hgTWSo0btKlhfC6MC3nwXCGjT4-bkVF9Ynw1itCjsNI_I3OMJNztyXN-xSNWvLkHpD_HYYlo81hcorIiZMqrrjfxPqz0icIjQKLrYx2saZGgWkR2s5ySewG6Eg4xIK6cWZjJxsAClA1KGmoSeP1x-b2reWadXasNQtXrwDHddear7IIFhLS1Wu31gq0VweXjF6RPStLM7XkUJk-amcNm49Mh3IpIw6uNBxfGm3_DFEaM6s3PP9D3anaPxwcr1HQk16myPp9zXXqp2mbg3EDAUpKZaSqBa17xOMA3P9mjJz8FcstwY1K8RuOIfHQPqnZK_c37ogaZy0ZPIcpD0UkDJTMIv0TfB6UAOCMbSdb541a9ZsCNcZx0_07-BEGFujVSOdmRF3UkoF6eJUd5CtUpw02RqgVbJPjqx8AIr9wrG6Wyy5yKqTIJbV5-8QwJ_tp-OXxbo6s1bYlF_AU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران اعلام کرده که ایالات متحده در جلوگیری از حضور آقای اسلامی، رئیس سازمان انرژی اتمی، در کنفرانس عمومی دخالت داشته است.
🔴
دبیر ویراایت: ایشان فردی هستند که تحت تحریم قرار دارند، و ما نمی‌خواهیم افرادی که تحت تحریم هستند، از این تحریم‌ها فرار کنند. ایشان درخواست معافیت از تحریم‌ها را ارائه دادند، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147396" target="_blank">📅 16:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=u7LGT1m6tqHbJEffyhs_o3yd4xz9I0SbejxQ_rQ0yrg8tlUFAPc7EeV4lnOUtTuAm-uoaoBb5GCdxZiDA-Vims1asUULX5rjC6svU0QckXDFYV2Hb_1ydvQvnzqU2Kf33-LfaJX3VV7xcQCD1_4JwyH6CrQtZsM6aQjRdNM37IkumTN1ddknj-mEkE5fjYDCt2c-mqcMnll6BFLBJdctmZj1VzsaqUs5hMv-KqMtGYIax7Pare17_C1fmuuNpJz6NmJkDHZmh8m5Fvd2aUzQUFZcftzmUcmAEXd70oPYIF9aQVDGSY_z21Jj5G-p9mmYwIs6c6LhX-10YR5bNhfvlDdXW32b9E0Q-AFhnrshtkZ2M5CfKFJm79L15tnAHUBoUGG7y_oI89jxWXn1NRZex9_hk2m-qeY82Wn1EwZo7mwNXAHbYvYQYt-KKlQgm0WZ7oNe8C8th6OARqCriVmcPI2S37rrLBsqKN3TBTGMg513BnUSEjAkvSrV30NeE2CMslXltdNNdV_tKSxp6BaekHNa3Ui_hLtEd0P3XPVTpVq-xWs_3uIHFTNwwl2xh0wLvTK0nfVYTuN50HkcQ835IOa_Xl4Myoh0Z--XH46XYgzsBcRT0wbTGITTkeq38giUJ7l1XwPVYcF5vPKbgJytJ8jew2V3Xml9dHFfm8UB3CU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=u7LGT1m6tqHbJEffyhs_o3yd4xz9I0SbejxQ_rQ0yrg8tlUFAPc7EeV4lnOUtTuAm-uoaoBb5GCdxZiDA-Vims1asUULX5rjC6svU0QckXDFYV2Hb_1ydvQvnzqU2Kf33-LfaJX3VV7xcQCD1_4JwyH6CrQtZsM6aQjRdNM37IkumTN1ddknj-mEkE5fjYDCt2c-mqcMnll6BFLBJdctmZj1VzsaqUs5hMv-KqMtGYIax7Pare17_C1fmuuNpJz6NmJkDHZmh8m5Fvd2aUzQUFZcftzmUcmAEXd70oPYIF9aQVDGSY_z21Jj5G-p9mmYwIs6c6LhX-10YR5bNhfvlDdXW32b9E0Q-AFhnrshtkZ2M5CfKFJm79L15tnAHUBoUGG7y_oI89jxWXn1NRZex9_hk2m-qeY82Wn1EwZo7mwNXAHbYvYQYt-KKlQgm0WZ7oNe8C8th6OARqCriVmcPI2S37rrLBsqKN3TBTGMg513BnUSEjAkvSrV30NeE2CMslXltdNNdV_tKSxp6BaekHNa3Ui_hLtEd0P3XPVTpVq-xWs_3uIHFTNwwl2xh0wLvTK0nfVYTuN50HkcQ835IOa_Xl4Myoh0Z--XH46XYgzsBcRT0wbTGITTkeq38giUJ7l1XwPVYcF5vPKbgJytJ8jew2V3Xml9dHFfm8UB3CU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی ایالات متحده، درباره ایران:
امروز، میزان متوسط نفت و فرآورده‌های نفتی که از طریق تنگه هرمز به دریا منتقل می‌شوند، تا 10 میلیون بشکه در روز است.
🔴
شما خواهید دید که این رقم در هفته‌های آینده افزایش خواهد یافت. و اگر جریان نفت از خطوط لوله فرعی را هم به آن اضافه کنیم، میزان انتقال انرژی از این منطقه به 13، 14 یا 15 میلیون بشکه در روز می‌رسد.
🔴
بنابراین، بخش قابل توجهی از میزان انتقال نفت قبل از درگیری، که هنوز به طور کامل به حالت قبل بازنگشته است، همچنان با پیشرفت بسیار خوبی ادامه دارد و ما به این روند ادامه خواهیم داد.
🔴
حالا نوبت ایران است که صلح را به این منطقه بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147395" target="_blank">📅 16:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=hAkCCsJsexVUd01wqtsY9_0WNM0ZG-KVBUfPQ7QGtzciJxOLt486gQow4-UPawO1MYJUX4bNfipSKVOszclYuG5BIBFTWk_0BXkHIzkWmgDpQDrzYsFz0allc-EKOP_11iqph32j7-uMpLsUDFWN7JE5NSOIT_ZjfqeCF4qtl_Aj0bWjiTwhYZJgDM203BGwfpZ1SqnLPSGJaacp_hvb2nzHK2qc7CzmE2gggJ9frEB-2uZh5fZhpqJqkXXinPdXwoFh2ttvhVdPEh_o9nsxWlHJgC8K4g56mDvTqVvfHghySleNXYHBj2O-URPsV34wpyFi454razcmGwtPYAZppp02qKtslfXcjvzc5IzBzztE73BrNthvr6NNGM4CIFmCtf7hhJ-cTSq07-GfVbPQ8WMgYOm-o68jqR9Qph8nm1kLXkcPROvjfVTUnl57aStp9rayMIG6n1QKCQ9VK4457rbyqrNudCexwf1Zo_4DQ-HlSbJiF5yc6lgVmI9rDyoSZ-UAVXoo19k6MTIL_HrxhmI0oVNPH2DhlgNyCvj_lWdDc6TEnwu8xQ-WdCpw-_hmjgZ81UWObHfdwnC7dm58A7M_JqbpskaCk-l3Sd-9XDj9SCShaHTYXR0AInA2exO7xYLj5KLi1jhxlEwrHRjozrvZ4K05JzXcLyXDGuSeVGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=hAkCCsJsexVUd01wqtsY9_0WNM0ZG-KVBUfPQ7QGtzciJxOLt486gQow4-UPawO1MYJUX4bNfipSKVOszclYuG5BIBFTWk_0BXkHIzkWmgDpQDrzYsFz0allc-EKOP_11iqph32j7-uMpLsUDFWN7JE5NSOIT_ZjfqeCF4qtl_Aj0bWjiTwhYZJgDM203BGwfpZ1SqnLPSGJaacp_hvb2nzHK2qc7CzmE2gggJ9frEB-2uZh5fZhpqJqkXXinPdXwoFh2ttvhVdPEh_o9nsxWlHJgC8K4g56mDvTqVvfHghySleNXYHBj2O-URPsV34wpyFi454razcmGwtPYAZppp02qKtslfXcjvzc5IzBzztE73BrNthvr6NNGM4CIFmCtf7hhJ-cTSq07-GfVbPQ8WMgYOm-o68jqR9Qph8nm1kLXkcPROvjfVTUnl57aStp9rayMIG6n1QKCQ9VK4457rbyqrNudCexwf1Zo_4DQ-HlSbJiF5yc6lgVmI9rDyoSZ-UAVXoo19k6MTIL_HrxhmI0oVNPH2DhlgNyCvj_lWdDc6TEnwu8xQ-WdCpw-_hmjgZ81UWObHfdwnC7dm58A7M_JqbpskaCk-l3Sd-9XDj9SCShaHTYXR0AInA2exO7xYLj5KLi1jhxlEwrHRjozrvZ4K05JzXcLyXDGuSeVGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستوفر رایت، وزیر انرژی ایالات متحده، درباره ایران: ایران یک انتخاب دارد. آن‌ها یک انتخاب دارند.
🔴
آن‌ها می‌توانند به جامعه بین‌المللی بازگردند و صلح، فرصت و شانس رونق را برای ۹۰ میلیون شهروند خود به ارمغان آورند، رشد اقتصادی و رونق را به منطقه بیاورند.
🔴
یا اینکه می‌توانند به تلاش‌های فریبکارانه، پنهان و شوم خود برای توسعه سلاح‌های هسته‌ای ادامه دهند، که در نهایت موفق نخواهند بود
🔴
آن‌ها در طول دهه‌ها، با این اقدامات، آشوب اقتصادی، مرگ و ویرانی بزرگی را به منطقه وارد کرده‌اند
🔴
اکنون زمان آن است که ایران انتخابی داشته باشد. آن‌ها کارت‌های زیادی در دست ندارند، و ایالات متحده پیشرفت‌های چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147394" target="_blank">📅 16:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: با تصمیم دولت، وزارت آموزش و پرورش مرجع تصمیم گیری درباره تعطیلی مدارس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147393" target="_blank">📅 16:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) چندین خانه را در منطقه طیری در مسیر حداثا در جنوب لبنان به آتش کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147392" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر انرژی عمان : احتمالا بزودی تنگه هرمز باز خواهد شد و وضعیت فعلی کوتاه‌مدت خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147391" target="_blank">📅 15:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwippc9w4D9kRlHX02R_KHvlmat_hdYVCZI3X7E1sVwM1EmQfjwDEpreXzmtkobjc9wjArAxE-rLdbhKKrUEyC7KW41xZXi5QfITQEePk_Wbg6AKO_ILLp9aRDdYHZRUeLcue6qPlkqeZ7OGH3GFSPrlRPA_IdgXVz099exnAWJlQ4CgkOuy23L8jWwXawSIUQlrJXRFEIUpK9Y_8OcZZvDLDuXErCdbnJ6cpsIVfq9vciG3bAzVUtyszOT6YNGo_SVzIVgwiV0IBXS1PtH66E1HLIoizeaX3HqDVAE0NG6-2-L-x68AvL69YK6BnjTZ-HvdR762MyR88sKAnpnYm-ex4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwippc9w4D9kRlHX02R_KHvlmat_hdYVCZI3X7E1sVwM1EmQfjwDEpreXzmtkobjc9wjArAxE-rLdbhKKrUEyC7KW41xZXi5QfITQEePk_Wbg6AKO_ILLp9aRDdYHZRUeLcue6qPlkqeZ7OGH3GFSPrlRPA_IdgXVz099exnAWJlQ4CgkOuy23L8jWwXawSIUQlrJXRFEIUpK9Y_8OcZZvDLDuXErCdbnJ6cpsIVfq9vciG3bAzVUtyszOT6YNGo_SVzIVgwiV0IBXS1PtH66E1HLIoizeaX3HqDVAE0NG6-2-L-x68AvL69YK6BnjTZ-HvdR762MyR88sKAnpnYm-ex4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا: ما قصد نداریم که عضو اتحادیه اروپا شویم.
🔴
آنچه ما به دنبال آن هستیم—و بحث‌هایی را در این زمینه آغاز خواهیم کرد—یک ائتلاف منحصربه‌فرد با اتحادیه اروپا است، ائتلافی بین کانادا و اتحادیه اروپا
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147390" target="_blank">📅 15:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZEQsfCqzs9uB46S3B-OJ26fPcI67KsYEPRiy-H97G9ijHDNBEnOQ9iexW_7fRMBQma6o7KDCYQgg0GIlmozDtcPIEnQUc3__hXXzI2zE3ihW9z229rxInCyUQxy4W3-sLwoK2fFAH0KegZDO3lhpprdkyZQFF8AGLh5NvXfIIJyxYfFRDMJnXc8nUT0FqDMnlqypxfvepHBjSRVgov4pdNgy_W1rZqkGf9J1ehZQdOIs1IGztq6-oYV_p4oPPWKGMMLnjRiioWIa27DESVLLB0IR4vYgKj68YWlojniaVxpB9gxcyCKEx8bfB-SbDWAQsN6Dl7YcJfc2_VrPMcAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو انفجار در منطقه مجدل زون در جنوب لبنان، متعلق به اسرائیل، مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147389" target="_blank">📅 15:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyCgdqQz2ewulQmOhqJ1W7V5d5OOIICOx0wotfd6CIlqqZJQs_HgLOLKIUne0wTurF2Y5oWmHRI66QhRTth7BkqPysEvJ5omVUtVUe4-5YvJJA7EnVDXne_-3HtvoUvZRU_rnw9nUT2t-LEvZ4CWGPzO0DxAmAPhhwDf-GehWUR5tuCG-Z1LCpgsLl7hx5UmSSuGlilTy49D-qpy5krpiKVceirhAb55iK_QDA9Dym_-SX765trA1_0Eb2IADxVa6u07s9Mw6BJMjhv0zr1dQIHk--CBJhmqFEwfjz9UqEinv7SqLbQgSuPYYwz_JxurPz13Eg9zlP8FnkH2DupQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، منطقه کفر تبنیت در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147388" target="_blank">📅 15:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۸.۶۵ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147387" target="_blank">📅 15:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دلار در تهران مجدداً از 235 هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147386" target="_blank">📅 15:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: نفتکش‌ها شبانه از تنگه هرمز عبور می‌کنند و توسط نیروی دریایی آمریکا اسکورت می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147385" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Aw7QZC2jBv7f-yMxieRXU9VGT23d15rYDs5fuPxd2yBjgWJWpWOABzvVFYbzAsih_uAMU9ggYh7GY5Ps0Xfl7RubS0sixet57A6kUXVxTCqp9g7qM7V7p_RYRn5WDnvsdjKWzr74bkvmHoXeA8Y-vF0_per9z5ZfD0Jy3VMOMwY55ViB-MWg49Uy3zjMVC3amj2ukrbDa9emCK8g-7WsrfeeZvGLGYYHCD1bpEIbTkHq4qU8MBsHGpKZgk4p_c0iXeX0H3SgrPAH3zETP6I6UEi3KwvOGXiSfp_zl12r71pznr7DsNGECPBaZY134G0zaSf7s_zUbvozV0AcH8lrqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Aw7QZC2jBv7f-yMxieRXU9VGT23d15rYDs5fuPxd2yBjgWJWpWOABzvVFYbzAsih_uAMU9ggYh7GY5Ps0Xfl7RubS0sixet57A6kUXVxTCqp9g7qM7V7p_RYRn5WDnvsdjKWzr74bkvmHoXeA8Y-vF0_per9z5ZfD0Jy3VMOMwY55ViB-MWg49Uy3zjMVC3amj2ukrbDa9emCK8g-7WsrfeeZvGLGYYHCD1bpEIbTkHq4qU8MBsHGpKZgk4p_c0iXeX0H3SgrPAH3zETP6I6UEi3KwvOGXiSfp_zl12r71pznr7DsNGECPBaZY134G0zaSf7s_zUbvozV0AcH8lrqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: از پنجشنبه سامانهٔ بارشی جدید وارد کشور خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147384" target="_blank">📅 15:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3T2OEQrLgkSl8TZWWuPCmN8_H1cOMa7GWFqE4cxcr8qzqFZovPOqJIQQ0bQMRBMlOq6h1tIOjQu_PlWYFnq-Ak9GCE7C90GMs9tjQoazzyKFraGhYaRST6b_O802VaPYklScUIQMWKrEcLJJNjLKl8P-IcSK1K3IXnu_3QrE4PVElCkapNPPzk0hQChUb7Y8KRV8UbeE30azNdCi6d1MzKE2bfAoSJFH-ZIP1XR3mG9TW8952kPcZOtqesweiY-FDxR_oJw20s9IsJupc0BmJcVBdwF9SFL8hh1uK0sScQuJOXV5-rS5MKE1j6GVO-ZjZfcemUg5dqgVUC8vFwfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع دیپلماتیک غربی به شبکه خبری "ال-شرقیه" اعلام کردند که عراق هشدارهایی را دریافت کرده است مبنی بر اینکه ممکن است به عنوان یک کشور حامی تروریسم شناخته شود، به دلیل حملات و تهدیدهای مکرری که از خاک این کشور علیه کشورهای همسایه صورت می‌گیرد.
🔴
این هشدارها پس از حملات پهپادی به خط لوله نفت شرقی-غربی عربستان سعودی صورت گرفت که ردیابی آن‌ها به استان میسان عراق انجامید
🔴
به بغداد هشدار داده شد که باید افرادی را که مسئول حملاتی هستند که از خاک عراق انجام می‌شوند، شناسایی و محاکمه کند، در غیر این صورت ممکن است این کشور به عنوان حامی تروریسم شناخته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147383" target="_blank">📅 15:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e279215317.mp4?token=blcgIwOgYdMgpDIVLuxMSFhKUBctel0oHmwZII7MfHbdbhC8t8rOMfj3NyxUmANFFBmSDGdbdN5sSN4LzbC-_LzRvIjRd6ZA9nnrHEeY5qTzRZr4CSqd-9Jh71HWeIH6dxAmATz5OEOE3qFAYsKoVTAH7DrpL1bC1f6X2AvGLh3oebMyxx8Dvwd_CSvdyLuCijraSeddDQNke2FuwdZ0BNI8_Wkt0cie1qUZxAnD6k0cBKd578sNEqD-LCxtmPPuRvgG4hpffbeI1wx06aciR4_mcZCBnEi9BaazTSa77pIOdcnEQAqZwCWRRIafFhKmS9msae5xuMvdsfpbgjCTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e279215317.mp4?token=blcgIwOgYdMgpDIVLuxMSFhKUBctel0oHmwZII7MfHbdbhC8t8rOMfj3NyxUmANFFBmSDGdbdN5sSN4LzbC-_LzRvIjRd6ZA9nnrHEeY5qTzRZr4CSqd-9Jh71HWeIH6dxAmATz5OEOE3qFAYsKoVTAH7DrpL1bC1f6X2AvGLh3oebMyxx8Dvwd_CSvdyLuCijraSeddDQNke2FuwdZ0BNI8_Wkt0cie1qUZxAnD6k0cBKd578sNEqD-LCxtmPPuRvgG4hpffbeI1wx06aciR4_mcZCBnEi9BaazTSa77pIOdcnEQAqZwCWRRIafFhKmS9msae5xuMvdsfpbgjCTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما : بازگشایی مرز تجاری شلمچه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147382" target="_blank">📅 15:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رسانه کوبیسی لتر: وضعیت وخیم انرژی در خاورمیانه؛ تولید نزدیک به ۳۰ میلیون بشکه نفت در روز یا متوقف شده یا در معرض خطر اختلال قرار دارد
🔴
این یکی از شدیدترین موقعیت‌های اختلال در عرضه انرژی در تاریخ معاصر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147381" target="_blank">📅 15:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoK2rkvYT9XKZA-VRr9MFC389jCMUykBNm5d-uqs0ztyf7KUL6-2B6LpzUHm4yzmj6UxU4y3u0yu-8ZSSBhilpDoK7IGs9wcjda-Fjs5ro4Gk29-Lbvo5b-PXmx6d9JihH8YQbuZGCGvI9k5ZwwL4FkziWGxM3IxSoTX53s_YMGpMNUugQnOaEWxCkx5_ESZ2q-zxg6JrQVjDxZEQVRcS3xcjaXW0OLwsPj9HwWo9o2qoDBD7t_9iwEihuAazjTrO_YWi5lbrpS_MH5nGpejqB2uuAlRANKmcb3W4Tfpb-echlgkxLAuaa8ot9HyZa5Eeo9jvMRKK0FSDYdTBhxFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c1fe0954.mp4?token=CZI4IJ0a5Gnm1sjNRQ71VjWmUVzu7WpVK2daSbw8O3zfydjJxWu3d5O7QVmZ3_6ejmitz5rgG6GruweHxBMeHYdDlHe0B7rhEupAhkC5hGkBLsmx2zp_nDhgJIWU3j6_l38dcl-6oVoQHWwp7KyZ9k8UNOcJuJu_MP9dqZ8zKpqcpI16L1DZ8jVydpBTrIg4fRGRfcgH98sszGSexJscvDqUw47kKVU672EZaHfrkwm89VWUwoOHGCH0SSgLy3x1YbsVRH0XxHqhRIUSPaw-ayriSCH2CIHw4DbNgVxUhXlfXH4Js7R_eQdE1z67Qlx-AL7-FQSonrakTVDyw32r1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c1fe0954.mp4?token=CZI4IJ0a5Gnm1sjNRQ71VjWmUVzu7WpVK2daSbw8O3zfydjJxWu3d5O7QVmZ3_6ejmitz5rgG6GruweHxBMeHYdDlHe0B7rhEupAhkC5hGkBLsmx2zp_nDhgJIWU3j6_l38dcl-6oVoQHWwp7KyZ9k8UNOcJuJu_MP9dqZ8zKpqcpI16L1DZ8jVydpBTrIg4fRGRfcgH98sszGSexJscvDqUw47kKVU672EZaHfrkwm89VWUwoOHGCH0SSgLy3x1YbsVRH0XxHqhRIUSPaw-ayriSCH2CIHw4DbNgVxUhXlfXH4Js7R_eQdE1z67Qlx-AL7-FQSonrakTVDyw32r1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شب گذشته، در جریان درگیری بین حوثی‌ها (انصارالله) و شورای انتقالی جنوب یمن (PLC) که از سوی عربستان سعودی پشتیبانی می‌شود، یک موشک بالستیک DF-15 ساخت چین علیه استان مأرب در یمن مورد استفاده قرار گرفت
🔴
موشک DF-15 یک موشک کوتاه‌برد است که قادر به رسیدن به مسافتی معادل 800 کیلومتر است
🔴
حوثی‌ها نحوه کار با این موشک‌ها را نمی‌دانند؛ در حالی که عربستان سعودی از طیف گسترده‌ای از سلاح‌ها و تجهیزات ساخت چین استفاده می‌کند، بنابراین احتمال استفاده از این موشک توسط آن‌ها وجود دارد، اما این موضوع هنوز به طور قطعی تایید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147378" target="_blank">📅 14:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87af46103b.mp4?token=W5PAJ-uAGsSPKP7jkWL9_qONNkXZ8BG9xJj7QuEpMIL0PHXOwUQBEOdgqoTKkOXmivT6-BPocoqk7dckgke6mZAX4dnHyY0PId52cK_r12In5znD90hFfHsD7JApBIMNsO_zPeyYJvORhMXW3Y4ivVUTtOhkCB4i_sq8WiIfO7sZmzQgrXAo0s5ipN-xliVK8yWpc7oc8IH5XIGBOJw9I0BFM24me_6NhMCeIM0Kp-QjfMAdZKUmqj6kt5AlVXS3EvtdzxwpoikP8cyDIcyR9XaWQH_SgjufaypvmPBmsOTvsEnRy0-8J3DpgJG1SIyOGDMI7WX9nQMCf1APb_pQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87af46103b.mp4?token=W5PAJ-uAGsSPKP7jkWL9_qONNkXZ8BG9xJj7QuEpMIL0PHXOwUQBEOdgqoTKkOXmivT6-BPocoqk7dckgke6mZAX4dnHyY0PId52cK_r12In5znD90hFfHsD7JApBIMNsO_zPeyYJvORhMXW3Y4ivVUTtOhkCB4i_sq8WiIfO7sZmzQgrXAo0s5ipN-xliVK8yWpc7oc8IH5XIGBOJw9I0BFM24me_6NhMCeIM0Kp-QjfMAdZKUmqj6kt5AlVXS3EvtdzxwpoikP8cyDIcyR9XaWQH_SgjufaypvmPBmsOTvsEnRy0-8J3DpgJG1SIyOGDMI7WX9nQMCf1APb_pQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه هند در جریان سخنرانی پزشکیان در اجلاس بریکس مشغول خوردن آجیل و لیسیدن انگشتانش بود و مدام از ظرف آجیل برمی‌داشت تا اینکه سرانجام کارکنان تشریفات، ظرف آجیل را از مقابل او برداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147377" target="_blank">📅 14:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147376" target="_blank">📅 14:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
گزارش برخی رسانه‌ها حاکی از وقوع انفجار در العقبه اردن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147375" target="_blank">📅 14:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7003bc8130.mp4?token=vzqu2q1Kb_zmd6ucSUhu7I8ExFEaVHMf77uQxu90tIYZL6zDM-55-cmZmUDZngyNf9ZMfKvIXMJFbUlNM_aXMgPNmFPkl98vXfs-8nZIXR6gwxQ2b-HRzt8HRMmDscFO4lMyCGZpzkAoe1XXs1xgDWDqwQachvd7DoqxctTjhOhiqq3v4IiFnYUJhAhTyxAbAfLRFfjRKUwYmpQdvn6Vgy2IM1Ud0diNmdlESYjUGmqraFnSCJXDZQ9LoAeHqwcvQWjqRSzGeHRzb3b2NbcMEmGWyGJmL3P7uTWj9olBO2891tdpEytdCf9a-LlyDEbX0tmfRlO_iVRMSJanEp5rEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7003bc8130.mp4?token=vzqu2q1Kb_zmd6ucSUhu7I8ExFEaVHMf77uQxu90tIYZL6zDM-55-cmZmUDZngyNf9ZMfKvIXMJFbUlNM_aXMgPNmFPkl98vXfs-8nZIXR6gwxQ2b-HRzt8HRMmDscFO4lMyCGZpzkAoe1XXs1xgDWDqwQachvd7DoqxctTjhOhiqq3v4IiFnYUJhAhTyxAbAfLRFfjRKUwYmpQdvn6Vgy2IM1Ud0diNmdlESYjUGmqraFnSCJXDZQ9LoAeHqwcvQWjqRSzGeHRzb3b2NbcMEmGWyGJmL3P7uTWj9olBO2891tdpEytdCf9a-LlyDEbX0tmfRlO_iVRMSJanEp5rEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل (IDF) تعدادی از شهروندان سوری را در مناطق روستایی قونهیترا دستگیر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147374" target="_blank">📅 14:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZ70KulzN-b11WJ5rvtpHsWqJyGjGDKqOFMZTtDHXd3We8EgYkazKznJXsxLVDNuj20F9KEIQTUX9ZJbJRTYD95_G3X2yzsiSG908ziQZYwspioqqjoN9VX0Dp8BOFan1lDNWhBxxIY7p_ZQAR3QYD9eayWcaGDTLRZuv9CsNRk-PWJGDKUozl80ORWPzmXLUirUrKA1Ica8h84fe9Y6VjqTChxsqEkggr0auBcH5V0eCXFAWi2k9XKovpIjMJpcWsuGgl7gL_p4_iGtqCBMFNe9D2DujOiqvdBy2pHsQfWDUYmDXqxkf69cZYK1SBdhT_44oK-DJLMGhTdcGdtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سدهای مشهد به گل نشست
🔴
دبیر و عضو اصلی شورای راهبردی روابط عمومی بخش آب کشور گفت: هم‌اکنون فقط ۲ درصد از حجم ذخیره سدهای مشهد آب دارد و در حقیقت چهار سد این کلانشهر به گل نشسته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147373" target="_blank">📅 14:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6KCNQK6hR5ZIGMTiy81jj-iVB3f2lmgN7rb8CV1m1vmSxw6dbStg1u52rRU2Je5yOzlKR__CugmkSSk3rGayWCBgDqtlrZ3NdhgwLnNtxagWlHIhCTjwwRSH97t3gZ0aCuufobi2b7g-f6N9TdtmoubXyBLTecvzUm6rZShRaHn9IKYAHrjghgPyDbEPHVkjczSspJkHwzShyATlPt3ronVvmcrdUc-xQhdNUIa_j9UbvxDEplDr-mrhFkKmnTPdOsM9p_bfQHQZqfIbG_GPhwAieDVr1qKMnzqkOdjYKx-yBT0xCEP7gpY4PqyGGfHpacpCPXiH_hcBzyCSgtLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147372" target="_blank">📅 14:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=F161FzWAxfumayaz1Gu7M9329UqR3K043Eb-8hnDgmy8aFxR24ZofhcnAkexy9yvRyThk8CJMzMaY35kPmSl-UEuelAm3kYnilaP_gMbGz7cy87RndjzW-vTXSVgzkOwekvxkWO3cCmR81xTHiv8tF75YdqGuwEcaLtuBvEbuEG_PDrCoewB7SVv0TmFTWJerQpfyCNA0KMOB_WX_JvwRISyhjJvbfreRHZS9QFxSn69fpUQHgJfPWNdYU_JE6lrFzWT1J4-pDBnyxrioIaQy3g3ML51BH_DRQeLCIhBhFZVw4yud-aPyJmkKiaXK6OEGDMu0Yn5K_rNUpMz1yUxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76d3eade.mp4?token=F161FzWAxfumayaz1Gu7M9329UqR3K043Eb-8hnDgmy8aFxR24ZofhcnAkexy9yvRyThk8CJMzMaY35kPmSl-UEuelAm3kYnilaP_gMbGz7cy87RndjzW-vTXSVgzkOwekvxkWO3cCmR81xTHiv8tF75YdqGuwEcaLtuBvEbuEG_PDrCoewB7SVv0TmFTWJerQpfyCNA0KMOB_WX_JvwRISyhjJvbfreRHZS9QFxSn69fpUQHgJfPWNdYU_JE6lrFzWT1J4-pDBnyxrioIaQy3g3ML51BH_DRQeLCIhBhFZVw4yud-aPyJmkKiaXK6OEGDMu0Yn5K_rNUpMz1yUxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله افراد لباس شخصی و آتش به اختیار به یک رستوران در رشت به نام « سحرخیزان » و تخریب رستوران به بهانه حجاب⁩⁩
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147371" target="_blank">📅 13:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
معاون هماهنگی توزیع شرکت توانیر: در صورت رفع ناترازی برق؛ از ابتدای هفته آینده قطعی برق نخواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147370" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5255c77892.mp4?token=g6ol7UjtvV3gwUJO-i_b5vt05mN6WU7cMhARALXhgcbB6jSqHKBuT-5Qb3KbF-4F8DxtAZIB77rER-UVD8yN5kN3252_h7OLGHPGjQOhWLLZym4PaG7E0Dtb-gS3AHXup1_AukYNqAOVwIhnhS7U9Zbd_gW944X7LM3t3dFAy7VlxR_e7O866tpKUNrxJNC_L0gScZZaqW0AoAh3tpR_ZwyqqEY52tDjzb5ShSTI1NuGGezg8lp8KhCVFCS9ez14E83M7sQDXNR8KEwwKQYkNa8hQyp24hTn5sm9fzDy0xZCTJIONTp_Kf1tPtMSwdPDyr5n_ISMmfu5JWRi8-wL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5255c77892.mp4?token=g6ol7UjtvV3gwUJO-i_b5vt05mN6WU7cMhARALXhgcbB6jSqHKBuT-5Qb3KbF-4F8DxtAZIB77rER-UVD8yN5kN3252_h7OLGHPGjQOhWLLZym4PaG7E0Dtb-gS3AHXup1_AukYNqAOVwIhnhS7U9Zbd_gW944X7LM3t3dFAy7VlxR_e7O866tpKUNrxJNC_L0gScZZaqW0AoAh3tpR_ZwyqqEY52tDjzb5ShSTI1NuGGezg8lp8KhCVFCS9ez14E83M7sQDXNR8KEwwKQYkNa8hQyp24hTn5sm9fzDy0xZCTJIONTp_Kf1tPtMSwdPDyr5n_ISMmfu5JWRi8-wL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا ممانعت از حضور محمد اسلامی در وین را گردن گرفت
🔴
نماینده ایالات متحده: نمی‌توانستیم اجازه دهیم یک مقام تحت تحریم سازمان ملل در کنفرانس آژانس شرکت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147369" target="_blank">📅 13:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940396b8a1.mp4?token=e6oV5PBNLZ4QIsTX2K2TQq6mN08_id_5c3GoaXVB9UcIyXFabq1BiF3RPudBPKLmskywY7hNTPsjAUxrfFBjUJnQtWMeRRmHNCHrubpM32e1f0IjaDAKSvcOUsK5TsrL16a5k7IxdmvNMSrPnke5t-FOBy68qOj_Dq_RhqJp0mEc7UGfOaLHORd4eK_nIgzp9d7e66ogokNpcrkU6tzhs1ZQ9rImil9wErZEvvBk_a5SLDJosHL5ysvVGLI-86HIVhq4edhKpjr6-NCIkfzrrFLMVE6hvJOgkTjnMCqc2V422TVnkpWgPWBoURw6DBQTO6q2A8dRiMptbwpm8HFkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940396b8a1.mp4?token=e6oV5PBNLZ4QIsTX2K2TQq6mN08_id_5c3GoaXVB9UcIyXFabq1BiF3RPudBPKLmskywY7hNTPsjAUxrfFBjUJnQtWMeRRmHNCHrubpM32e1f0IjaDAKSvcOUsK5TsrL16a5k7IxdmvNMSrPnke5t-FOBy68qOj_Dq_RhqJp0mEc7UGfOaLHORd4eK_nIgzp9d7e66ogokNpcrkU6tzhs1ZQ9rImil9wErZEvvBk_a5SLDJosHL5ysvVGLI-86HIVhq4edhKpjr6-NCIkfzrrFLMVE6hvJOgkTjnMCqc2V422TVnkpWgPWBoURw6DBQTO6q2A8dRiMptbwpm8HFkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف‌های ناشی از کمبود بنزین در روسیه به شهر سنت پترزبورگ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147368" target="_blank">📅 13:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ممنوعیت واردات لوازم خانگی در آستانه لغو قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147367" target="_blank">📅 13:19 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
