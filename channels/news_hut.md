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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 08:41:34</div>
<hr>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Mil3TL9-pE2GufdC0RrUDNnIz1FNQdS4Ior7s0TmCBv3I9byN2KOerT42Mc-lFIEcL2P_I534wcZAZLOW0a1yfaiSspQFddnTSM7bDqwNEcO_vBMkrJhrjWmqYIWd3A6BE6_JtyDr9KHJ4U_ueKwT9FtONjOnNBGHJqRaKscJLkUNYPIImxz1tCAVXCH7Cf2100kTGsPrNUzFe0ssOU3rW-eYgg0erHe7bpM5EYFPOMb9Ho4gjlJKdXUlgQX_aIVcGjSBjgqEPPJHZnPkvSzdgjLJv_gJzoj6LlxJmnb5_HCddGw3N9BVwZlFUWo14k70XpE7pHqJMQUbo-vEM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvNcPqPsfZwMLBhutM-_wIoaQeZrCkrtE6Q7hxJe8g4RuFT4brbtvP7nh6SDGQG_wyVl9kALPxVRfZx-5z70uJ1JebNQTlvjEOjmNyw1nhcnkox7rfinDyWS9FDtlFZLoqBAQB1Pnfkq2H9kQ94_lMSQ6vxIZ9Zb9nmIvhgLqW7KwCSugt4cCZ1gI_VAEzB_IVTEBUOZFnRsGhfxz8KdKDjfLYq2f8aMlrrgcLe834gJnHe-lB7QNaQCTga3iEe7QfP2nQdqCyjWPMd7vAfQTeJmUxQlfgHfSkTIEYrAbKqqAMhbZbgKfauO_oCZu2mf6gX_GeW4IQhi4TdVFn6kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=kgdwK-b9u7MYCtAuKJxGRU3-w6mothBJxjjUvtmivKQT5r3U_PI2digWjHR7NgIc4fQMaBFBjHQ3ciwbGVfn9Fktw5kIXy1svZupOHg3q6_6gR1Vfe1zAANagDIcog1OEanm0xK3mSNFqeY4R1s4FtYc0RRlu37SGdl6UapJgP3HbwaSlVrhwRYHZqQ8T7DwQGevVG7Iad84nQy2EBF9zA8Vm45dbHPH72QhhqydHiedySN9PLennRY1p7J2sPvcX_1kpSUM668VYfohEV6DN3Xe9o7IWgdFhFhfv9-1UPX9NdR4wXwHH_-Wf6Q9b5HBq8vAN3Htlkbg7nQe1ooziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=kgdwK-b9u7MYCtAuKJxGRU3-w6mothBJxjjUvtmivKQT5r3U_PI2digWjHR7NgIc4fQMaBFBjHQ3ciwbGVfn9Fktw5kIXy1svZupOHg3q6_6gR1Vfe1zAANagDIcog1OEanm0xK3mSNFqeY4R1s4FtYc0RRlu37SGdl6UapJgP3HbwaSlVrhwRYHZqQ8T7DwQGevVG7Iad84nQy2EBF9zA8Vm45dbHPH72QhhqydHiedySN9PLennRY1p7J2sPvcX_1kpSUM668VYfohEV6DN3Xe9o7IWgdFhFhfv9-1UPX9NdR4wXwHH_-Wf6Q9b5HBq8vAN3Htlkbg7nQe1ooziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=SzTpZf_vxBL4-k2-AArKIWQ1ER-a90S9CoW6SxQ_DPKhAn-bDTZeWrtstb06wHMH_FCSsl2WpyatG7kUq7cDf81CnfYa-8BkO1jq2pV-4h3CIDj7YQvo3cWrehP4eXhSAcaTxYLrtcleKyBIOGDwJ-R9nfcqrZOnHNJnAxxlOS8_yioqL_p_WuyNKw3QI92Timqmkr9Xd5B07tXVNiQLuBIk_ILiMDf4hOxdZVZMJOBSCgZkzawpnwUEC--CvX9ZOwPoQjEMd80z6WPpwKc85oQTtkZB8tyfaHs8xPSg3dRA27F_3SgDj_B-SD9zz6zb-GhIUCydSf6PLP3rTus19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=SzTpZf_vxBL4-k2-AArKIWQ1ER-a90S9CoW6SxQ_DPKhAn-bDTZeWrtstb06wHMH_FCSsl2WpyatG7kUq7cDf81CnfYa-8BkO1jq2pV-4h3CIDj7YQvo3cWrehP4eXhSAcaTxYLrtcleKyBIOGDwJ-R9nfcqrZOnHNJnAxxlOS8_yioqL_p_WuyNKw3QI92Timqmkr9Xd5B07tXVNiQLuBIk_ILiMDf4hOxdZVZMJOBSCgZkzawpnwUEC--CvX9ZOwPoQjEMd80z6WPpwKc85oQTtkZB8tyfaHs8xPSg3dRA27F_3SgDj_B-SD9zz6zb-GhIUCydSf6PLP3rTus19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Bgs2QVO_9BXYUwHnjUBH8EhiUwJITvpMn5fF-F1REnKhGWB-eVm-6Ynm5zkJMNC5Qz0mrJGv61MudlcRnZxN6auxYBAFu932ito4Zp2NZrxZiapKL9vN9WdWg867Uo5jXcXqQAIiYAcN3Nb-AC_ioKUUxSnK2MruQTTUjZLoCEHVbbv3jXZPK8AXe2nouMbZP6Wu5hCczABP3dSfZmE5FqyvncPEOWPQ4kz9qUrO4mg70DQc_kqLs49fOBMdMLfD72bmi3gseBYnDTN3FKZb3gyxBEyxkDKnrmlqah8ZvAGVTbqThkSZVPInS2z1_tq63wmy90mrAJGddvYlDYe4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Bgs2QVO_9BXYUwHnjUBH8EhiUwJITvpMn5fF-F1REnKhGWB-eVm-6Ynm5zkJMNC5Qz0mrJGv61MudlcRnZxN6auxYBAFu932ito4Zp2NZrxZiapKL9vN9WdWg867Uo5jXcXqQAIiYAcN3Nb-AC_ioKUUxSnK2MruQTTUjZLoCEHVbbv3jXZPK8AXe2nouMbZP6Wu5hCczABP3dSfZmE5FqyvncPEOWPQ4kz9qUrO4mg70DQc_kqLs49fOBMdMLfD72bmi3gseBYnDTN3FKZb3gyxBEyxkDKnrmlqah8ZvAGVTbqThkSZVPInS2z1_tq63wmy90mrAJGddvYlDYe4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W86soodYcI72m1LWG-loExGtGUpM32ganjkTHOj7IvQ7v0HcWWCoHSGtUg1eZLfcgPrZ19V9Zoy3MdSve5z3D2_NNwXdOsflFNvulUPH5bqLWqENW9yNqYYM5VxPWZQeutwr8aA0_amYpBDzUma_i7ziv1jnrt4GoxJG2Jsz8UlVeqB3Gh6tP1Sa7bL61c7On4ihVHq0NRK_lDm9hEB3ayPSQ1lqJcjF-cbyDCpBhC6uzn75r9js21D2red8dWsOXnuW1bMdr8SRcS3EGzNubSzcHN6zr91mLGLY1t1QH4lv_NMf1Md9D1um_p6Zl2A0Ep-Bqpkk-mBLuAcr3KV8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=EwOh9FQtrq54l3A873k2JCwqvs5dQ1Kqpy8Wdsez2TVmvRAHUz-kJLbfQEbXTHbP2AIh01PKvGOdWClkgRioQ6qJxI9vVSh7ffgnu-NfZaBz1gd5NoVqg3BDUR4nbNTSi5vtTBKLvmDVH6s70jLPkHlWHq26F3Y6dnTrifeQMdcyb-aub3ST1aoba2A_KkzumoS7zaroM0ZOVGl5nJ8SbmhhwnwClKyhiF7bOewLwAAzPsX7HuSXw3YZWMWecSp2eNNypGLFbgMuNJF334Tq2l1zWJcN__T64LLmvznlw6t_2l6y8hBw7ZHPrihiG728F2sRwvjtk8S9Gtsjx1nGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=EwOh9FQtrq54l3A873k2JCwqvs5dQ1Kqpy8Wdsez2TVmvRAHUz-kJLbfQEbXTHbP2AIh01PKvGOdWClkgRioQ6qJxI9vVSh7ffgnu-NfZaBz1gd5NoVqg3BDUR4nbNTSi5vtTBKLvmDVH6s70jLPkHlWHq26F3Y6dnTrifeQMdcyb-aub3ST1aoba2A_KkzumoS7zaroM0ZOVGl5nJ8SbmhhwnwClKyhiF7bOewLwAAzPsX7HuSXw3YZWMWecSp2eNNypGLFbgMuNJF334Tq2l1zWJcN__T64LLmvznlw6t_2l6y8hBw7ZHPrihiG728F2sRwvjtk8S9Gtsjx1nGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=IifGDZZlnV_ny1Ifn7gINfIJWbskzSavxmjsPNVjUkHz2a8X2xS3k3RFssgRwfJJn61pOFf2SCVM2ahsF7xM0eDRLdk1UPtRuA7t4qbwhDH8RzFetHyyii_6ZPFpYsHiSYcz2UNJ2G7k96xClqOqxOiBxa4l9smgetUgp9k8z_C_cHBwb7WA7Y9G6pL6j3Huf-O0ywi__C_fsmXrg9kwsOy3syw5kX2bPJ29wFEBuBLuVA6ok7FhAIzhMNOFSzzvAGV7No5OHPhvGEbckspoZh-u8_2akTfDZIMf3jmaaeloAPi4brYQ84O-aJj26x6Di7AxxcNTjZadbNOY-STMnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=IifGDZZlnV_ny1Ifn7gINfIJWbskzSavxmjsPNVjUkHz2a8X2xS3k3RFssgRwfJJn61pOFf2SCVM2ahsF7xM0eDRLdk1UPtRuA7t4qbwhDH8RzFetHyyii_6ZPFpYsHiSYcz2UNJ2G7k96xClqOqxOiBxa4l9smgetUgp9k8z_C_cHBwb7WA7Y9G6pL6j3Huf-O0ywi__C_fsmXrg9kwsOy3syw5kX2bPJ29wFEBuBLuVA6ok7FhAIzhMNOFSzzvAGV7No5OHPhvGEbckspoZh-u8_2akTfDZIMf3jmaaeloAPi4brYQ84O-aJj26x6Di7AxxcNTjZadbNOY-STMnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=WnCFj7zytoakbnpLeZWN0LsF6yEOs1ZbWErMmQKi1I7bW54L8FC63TGDEyZBrKgtER98LwAYZ4O9V1Y2RUQNTlysCgUNtuSzEBivD_Xgjd4aLLYQvIvWnCJLeTFnhF3BTg78OlbsExXVx8oXqRC6WUxBkcBdef9WpintXdGe_gi4mQFMJqAx1WIJ0gofufgRXaSJ_IWj213_qbdrAy6uzEWqeG7my7W3oP_97HAeVSm2xYq6kcandi_92iJQ57B8SZoZE-VNzQxAFhdLmQJ5Sj2Rq7kWHvg7OO3-B3p7NpJQLEfrHN_58wyTEC45gwZ502fWxYkXaQLVoUSdX--zrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=WnCFj7zytoakbnpLeZWN0LsF6yEOs1ZbWErMmQKi1I7bW54L8FC63TGDEyZBrKgtER98LwAYZ4O9V1Y2RUQNTlysCgUNtuSzEBivD_Xgjd4aLLYQvIvWnCJLeTFnhF3BTg78OlbsExXVx8oXqRC6WUxBkcBdef9WpintXdGe_gi4mQFMJqAx1WIJ0gofufgRXaSJ_IWj213_qbdrAy6uzEWqeG7my7W3oP_97HAeVSm2xYq6kcandi_92iJQ57B8SZoZE-VNzQxAFhdLmQJ5Sj2Rq7kWHvg7OO3-B3p7NpJQLEfrHN_58wyTEC45gwZ502fWxYkXaQLVoUSdX--zrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=WHMlDWlU-h_qTrLiskHIBa69PwTz-hvSkas7JBgUtGNWhDMk3xxLBWhhNAA4WMOw8PWcF9F0ezjg8m-oC7obkTsAdnrQisJk5T3Eg5U0HIRA0sBzuU0CAP4igYzlJ_zf3SKGygQJQt9vNUh2tHHmCZlhccajU55VFKLBwV1AjP8rwng14Zzpqo0tCClEt8RD-28S7B4I2A2NIQLpZTpYd2AvihMlSXHXGS4WVVdbKt9LNluf9Z4yMV8KyhbrTb5iE71CMyHKD9EidGSjKfZN9Hjogr7UFT0U9TWksAmbxQamr4e3JwGvsiUkLCL6wjTq9kNnMJ9HytzeBt2CMHCJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=WHMlDWlU-h_qTrLiskHIBa69PwTz-hvSkas7JBgUtGNWhDMk3xxLBWhhNAA4WMOw8PWcF9F0ezjg8m-oC7obkTsAdnrQisJk5T3Eg5U0HIRA0sBzuU0CAP4igYzlJ_zf3SKGygQJQt9vNUh2tHHmCZlhccajU55VFKLBwV1AjP8rwng14Zzpqo0tCClEt8RD-28S7B4I2A2NIQLpZTpYd2AvihMlSXHXGS4WVVdbKt9LNluf9Z4yMV8KyhbrTb5iE71CMyHKD9EidGSjKfZN9Hjogr7UFT0U9TWksAmbxQamr4e3JwGvsiUkLCL6wjTq9kNnMJ9HytzeBt2CMHCJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVfxZn7nMI13gY2NnOMQOELkusOnEWHjjyCIBkvaBnpfblVh-wIrIe5sSS72l-8ek90ilZpORgMmaIXXwsP3hM3O7TgEQcWTQB4kCIM6PNwgjvQwQ-wieVer-GHo85ZJJT7R7IRrgcsdVWvKMM-vb-H44J5aufKOdypri9z8ba7bB1L-pGKlrAcASORTuaYU7sYafLsdACXbFAzyVDdQZpB0Eq6aCAUoyYq0Hf_piCGZ6k0dCwNQbsnwB2jvmTJHqUsZ3wMM05_UQAt7AgXGNvRzQsfgRhTNprWqN6UGsX5y42PFDcC5KkLTGF_wwupnUnxagBjom5fPvremLmDp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uov9ySljvgi5h6e3mIHHq6Osi6dcrAc5jQUdk2_1oaVMBiMK1gf9Ju5iwXQaOTqudgvB6Bs1_5XhXWx8R9l__Tj0xYRgzbi0aA3GVKLxnD4YH1JD34g8iotTyidoJ3-FINFC6RbGUIK6hUCNywgKi06HTZEATXuJ8e06jxv-vlGSqFW56ZvtbEzX4NvwV_mo9H1N_mo3Fg9jPMs-Mr25RhZTmDUFMfybVeKFu9zWMAMpi8dc8BEYvvxo8IPwsWLwaDv1NoHHKFDAciELegnUrTl92qqrQElILbspmNRCmIrRGD5FY1vkviO2RYpozenTjsdLCqdoko5IvfPHXatM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=W2F2zevA0ifErSNgsoraWY8AfjZwBA2i2oRDlmQ7ABVz6Q_4hlkGaqjtWKn33dIxG3qkuHCg7LGUNEcEGyLDs5pJpjZCCiKigMKPbQGww63vxsw5AgsTx8gLAtlj_ABHYZNbu-9u0fW2j_lMpcRDTeia-MS1odF5RRmEhuxinYZrZoEoLbHexBfVUS0wvY5U8XR9zYDDa51io0kB659gslPkPApIdwL5zHp_EWKZRJMjPm4GSFEbQhvq6of1s1_NBUR0Q9jepF_MaE0hPGtSKgu5Llum470uVdwxip81wnoRg08dgTdmER1Y6cZQdR5iMbVSL7KHzdtNDtg3xRc0o4bPZxH6IRW0pR7ytNU93kkrQcm94jM-gL2ERvf5mKXRrD9zlyFbUiZRPWhxBnHbP83tN7bUQaUicb8zzM1SZWFvJZBx014fyDhHKWg9HugKE3YcEKNxtEHHYvCTEnMAV6odom9dV8EjdU7RroUj9X8899-aruN7E7seHF4XtK0fCkNlrQ23aoTbxXj4iZpMzoiYifSqHui3xSePf_I5CBZO0KGWy1m1x4MUlGdiyiXMmLWMTT-gpAHXtrfizYT1Pb2ji8OtK8-GzU_UeDGLenVlaK8BDtYfDR8tPYXjiKax8vhF5lo2zJbhEvBMJlhRZeJsVDMUuPrYqI0Poflk75s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=W2F2zevA0ifErSNgsoraWY8AfjZwBA2i2oRDlmQ7ABVz6Q_4hlkGaqjtWKn33dIxG3qkuHCg7LGUNEcEGyLDs5pJpjZCCiKigMKPbQGww63vxsw5AgsTx8gLAtlj_ABHYZNbu-9u0fW2j_lMpcRDTeia-MS1odF5RRmEhuxinYZrZoEoLbHexBfVUS0wvY5U8XR9zYDDa51io0kB659gslPkPApIdwL5zHp_EWKZRJMjPm4GSFEbQhvq6of1s1_NBUR0Q9jepF_MaE0hPGtSKgu5Llum470uVdwxip81wnoRg08dgTdmER1Y6cZQdR5iMbVSL7KHzdtNDtg3xRc0o4bPZxH6IRW0pR7ytNU93kkrQcm94jM-gL2ERvf5mKXRrD9zlyFbUiZRPWhxBnHbP83tN7bUQaUicb8zzM1SZWFvJZBx014fyDhHKWg9HugKE3YcEKNxtEHHYvCTEnMAV6odom9dV8EjdU7RroUj9X8899-aruN7E7seHF4XtK0fCkNlrQ23aoTbxXj4iZpMzoiYifSqHui3xSePf_I5CBZO0KGWy1m1x4MUlGdiyiXMmLWMTT-gpAHXtrfizYT1Pb2ji8OtK8-GzU_UeDGLenVlaK8BDtYfDR8tPYXjiKax8vhF5lo2zJbhEvBMJlhRZeJsVDMUuPrYqI0Poflk75s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=FWT2y6JaGhl0LOfh3Nx8WDkkSpzwqR0-9YCNKKg7pemfFdruM3deyMaDdxVerif8C2X2udtuYzjH-P_LLmWBTIg5DW2AERs7Stl8pbzXzi5VH0a7Sw1jxEy4JHiGJig03NmGbOJ-D1wsI5TzPAdGbgeScVjb8D_2128ep-Npqn8KGw1Yy7S3zov6vQVX5UeoJFZn3c2ljA6Vj3MBfVovR9d9Du44VSrQbRCjndmY60jc5APkQ0f4r6HldIH0iqy-MB8LbVDJRj6civVT7745k3ue1KkSmqwItr3qY1g9M091u-6onb3kje-rPkdOK_waNCiZBJH_LrSMMrFTWIR4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=FWT2y6JaGhl0LOfh3Nx8WDkkSpzwqR0-9YCNKKg7pemfFdruM3deyMaDdxVerif8C2X2udtuYzjH-P_LLmWBTIg5DW2AERs7Stl8pbzXzi5VH0a7Sw1jxEy4JHiGJig03NmGbOJ-D1wsI5TzPAdGbgeScVjb8D_2128ep-Npqn8KGw1Yy7S3zov6vQVX5UeoJFZn3c2ljA6Vj3MBfVovR9d9Du44VSrQbRCjndmY60jc5APkQ0f4r6HldIH0iqy-MB8LbVDJRj6civVT7745k3ue1KkSmqwItr3qY1g9M091u-6onb3kje-rPkdOK_waNCiZBJH_LrSMMrFTWIR4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=VGM-WOxwQajEhER7RE_lyGMgRUT89jkdbB0FI4n0CJp9-UpnTua0KOR43ufkLjkcifSE0Nur1DnLi0tBqad4vzW-WzpvD1uitoLUwdewEDmpT02qNwmN-QkPLPDtQAAmLGRvycYwnIrk3pyGETXT8vhHItPGZGIuRXlUhP0mIbB6Ncsx6KWqK7cm0jumWhMhwnBRNzpvsOeMocNKDI0NnDTwlltwSXwvcyoLm3DkiybTQDgs0b3uW4_Y41l-O94PANPLjkrno1CYPn2E7LnaatgeXT9DILY6PIxLxWr2rNU7q-9eXmn_n1Iqv5i-EXNr4qzQLILNZNKo3tkaIZLkQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=VGM-WOxwQajEhER7RE_lyGMgRUT89jkdbB0FI4n0CJp9-UpnTua0KOR43ufkLjkcifSE0Nur1DnLi0tBqad4vzW-WzpvD1uitoLUwdewEDmpT02qNwmN-QkPLPDtQAAmLGRvycYwnIrk3pyGETXT8vhHItPGZGIuRXlUhP0mIbB6Ncsx6KWqK7cm0jumWhMhwnBRNzpvsOeMocNKDI0NnDTwlltwSXwvcyoLm3DkiybTQDgs0b3uW4_Y41l-O94PANPLjkrno1CYPn2E7LnaatgeXT9DILY6PIxLxWr2rNU7q-9eXmn_n1Iqv5i-EXNr4qzQLILNZNKo3tkaIZLkQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTohZW8wjm2EtGsK0flKrBe-WwZgSuqttwSNHzjK8iFqTcxtnOYJYct-Z7ZmaSCI11Q7JcQXIE8b1Q6EBJyRknqDAvfAPIOgh9EBfTZ5F83FkDitKDVPCk7wO7qblziZT4i51j9oyfT30BCMOUvb83ogob9D4RvAiRpfFJ2CVE-1zY1uniuNJW9UuWiC-tKJbosNwkXCH9B2MEaHc5MlGxHqu8AcXNdFpcF4EPnBDm6oKqI-kVq-CoemDrRSRqbnAwyU98mkj7rruhjeCYuji-XKi8FTYgvCLrJNePnJI4-BWEeUxyV4mQVSAeBT-HI-KftOirAUUHcLdfY-p-8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5ZWO2RNFB2F6BddBUPzQl0a5M163VoWdm4vHm8N45bFdp10Iwnyx2GWUWnrmF0D6TPW81UOo1bW1ANGX8sN1_9O9EMP1sq-vdum-EyAE8pp1KCVSsn97eAx0zJ5L3-RVGQdGMLMXSPc1F4kmIjgO6kjb4JaY-iFRzPHeQ4TF3Vs3aNgLEBVWZYN2tcjgmrGLu1BnoGnWQsx4oClcLAH9Rxi209tzhpKLQVLGbF_NCXvhcDy2l2ZyXK7GifauQoIn8DNxsXrgrqSnMCmISxb1JLjJfEmwJIf6DxekjMl6cbPmcZJnBQtMXczTNuknEDH0VzOkGUCFHP7AamqoduUpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GfWmwIWlA543rrDwSpla0HqH9wW657srLu6YzGY2mD_e_9HWDQrF0ntd-s5k8b0Ddt6f9ydz-f7W8heOHr-h9xNIx9mPcSJSyMetNi0tO1LIxGxQ_XbnkgG5WoRIqWaFfia6p96iBrEe1aR_mZJlqsyxT3QHZ64_gcIRIgRNTZI-OgbmHXSyQww8ZouJXTeVMbECV0zWs9L7dpI1vVOZS3YHham6tm3jlxMTpc6FP4FQCPOCQ9wHqns2oOya_McK3mbWLifVZN1EeeanBYEUcVd4jN9dJAufHTR40ISvCvAYLLNEDITmo7z7IBxoa5vrLvU5OKgGbYp8p-4h9CEnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=sdrbdi4O-hQVGYTIkyUb8celqqQxZRGlQmRh_tRv7UjnfF4redUnd85t5FiIshn3oPrpODqGYfnVqlhMzugAm92hRlM-q2QNkhD-tMc6e377OVNp4cES_ixrCXI7sNOeHLVuMERYCkIjvDJEJIH5975DNMn_HUqG4gLmXEnUwnj4Xa9YadaAUuBqLUEDtnhSPowSFeC4_Q6zIq46IQvvroIEQjTKeZdH1uNpabrqSoI8zh6eY94XH-FOyaQ2ZzORO_7MiwBNVxVHEaHvFD4XEt3i9BQ2sI-aX3AGESHnwiVkU_aBkq86TfKajucWmZ0xjdM5mGnokGsGuHAOtbbizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=sdrbdi4O-hQVGYTIkyUb8celqqQxZRGlQmRh_tRv7UjnfF4redUnd85t5FiIshn3oPrpODqGYfnVqlhMzugAm92hRlM-q2QNkhD-tMc6e377OVNp4cES_ixrCXI7sNOeHLVuMERYCkIjvDJEJIH5975DNMn_HUqG4gLmXEnUwnj4Xa9YadaAUuBqLUEDtnhSPowSFeC4_Q6zIq46IQvvroIEQjTKeZdH1uNpabrqSoI8zh6eY94XH-FOyaQ2ZzORO_7MiwBNVxVHEaHvFD4XEt3i9BQ2sI-aX3AGESHnwiVkU_aBkq86TfKajucWmZ0xjdM5mGnokGsGuHAOtbbizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=SnAyvIU8f4bkD6F6sCFUmb0CzsFsXMJixpBhaWn0EBMUh-eJQHZGomD_xv8Q7zlxdKXCCeYy69cGjo-2Q4k2huAyXWk1eQSzVB3DBoPXs1KIZVAGvY37tfUxPY5Y59k0en2SifDMOQHdo17ihW6MVprdeEeUxujj7y98X0tLgBFt4zvTSR9RzikEdgxs60b88eDXcNOjhSQ9GpXjoNOPOBNOHX70c1DQg_7r9MjfOEpBXOAehZ-q6fMVTJBhN5pzfuVWDUdYlA6DwDaJ15CLeuZgPj8BtQSNHODshnX7TGGW1ScHjCL07K2jsbPKC1a0QbfMRLBuPuewsGiHU6H26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=SnAyvIU8f4bkD6F6sCFUmb0CzsFsXMJixpBhaWn0EBMUh-eJQHZGomD_xv8Q7zlxdKXCCeYy69cGjo-2Q4k2huAyXWk1eQSzVB3DBoPXs1KIZVAGvY37tfUxPY5Y59k0en2SifDMOQHdo17ihW6MVprdeEeUxujj7y98X0tLgBFt4zvTSR9RzikEdgxs60b88eDXcNOjhSQ9GpXjoNOPOBNOHX70c1DQg_7r9MjfOEpBXOAehZ-q6fMVTJBhN5pzfuVWDUdYlA6DwDaJ15CLeuZgPj8BtQSNHODshnX7TGGW1ScHjCL07K2jsbPKC1a0QbfMRLBuPuewsGiHU6H26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-HjtLY7V4HBfwtLXQU_M-_A7_-SaJC2cvT8GHspGyrriPLs4HZ45RJljB0F9q7QilgIOL1h1ueqixFJWVNTT3210TrC5CO31wAmCOKrxXEKirJIoQ_9YeOGw6cdApxGEcRS9uJX-IcIvUJ-SFirxuT1l1QWiLYgJS7DvywTz8t0ztBCAeRncLjMAdHxcaJt8RT5uPR8YcK7DZGve3w7_FnDlpi3lsoD9IG1rwcBAL85-P4uNEk6WuaUgwePM3Jj9SppRVvsipPA7nRNb_Im-yDSPhhy80VdVvnjh425bt16k5XNVfcoVlMqhbrvWss2wNtu1Cib_OArFThmffby-DC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-HjtLY7V4HBfwtLXQU_M-_A7_-SaJC2cvT8GHspGyrriPLs4HZ45RJljB0F9q7QilgIOL1h1ueqixFJWVNTT3210TrC5CO31wAmCOKrxXEKirJIoQ_9YeOGw6cdApxGEcRS9uJX-IcIvUJ-SFirxuT1l1QWiLYgJS7DvywTz8t0ztBCAeRncLjMAdHxcaJt8RT5uPR8YcK7DZGve3w7_FnDlpi3lsoD9IG1rwcBAL85-P4uNEk6WuaUgwePM3Jj9SppRVvsipPA7nRNb_Im-yDSPhhy80VdVvnjh425bt16k5XNVfcoVlMqhbrvWss2wNtu1Cib_OArFThmffby-DC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=uJ55DEBpyNH8EvyX7f5_K3CO8jOQJ57oPxyVC8NdMnWFb87cSSxZLdeey54wzEn3B1hguLu8xKFihdszARytgg6jO7pRPCkcUc36GnvFYsS--bAP8FvNF2-SmDuQenZpZE8H0JkYe1OmZeykACyGlJBS_FdHsRbNQsQzb8vEQT_zk9ptmBuC3WkLo1LDNlfzAVxi7Lu_ZSJVVC5WQ8AGerSJY8ZMEwrj8Bljk9z6HGvTj6VHhlcxV-yuzsx_9b1TWYxeHsho44ElI89ATWlmBCO7sa_H7erR4n2sBZQXeeu-FdTGi3wScxmaVzVQ7A03zXvm1tT0fFAmz1x9w4vU2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=uJ55DEBpyNH8EvyX7f5_K3CO8jOQJ57oPxyVC8NdMnWFb87cSSxZLdeey54wzEn3B1hguLu8xKFihdszARytgg6jO7pRPCkcUc36GnvFYsS--bAP8FvNF2-SmDuQenZpZE8H0JkYe1OmZeykACyGlJBS_FdHsRbNQsQzb8vEQT_zk9ptmBuC3WkLo1LDNlfzAVxi7Lu_ZSJVVC5WQ8AGerSJY8ZMEwrj8Bljk9z6HGvTj6VHhlcxV-yuzsx_9b1TWYxeHsho44ElI89ATWlmBCO7sa_H7erR4n2sBZQXeeu-FdTGi3wScxmaVzVQ7A03zXvm1tT0fFAmz1x9w4vU2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=t5XwUOQBgAB_qHiRKQB6vf6R_mPQ14hJ9eLvMqmXsNGUmLPpF7_Y25YLzmY2S-E3xxCp2YMS9SyEwUDo4_1ZdBzI7ufX6AlxeyNBVSt-4Vr5Ih5DvPtOs3THGt42CdcYgw_ETZxaDXLE1FEO9rgNiTAQwGnqZxCsqGRcF3pGwQial8NfAUd1N2ywnZGz5nFrLQfXyX1ALV-iFXMPNOHmiB8M_6vqZLqN4yqsUDay0NufRCvtkvnB79N_yBBwH1e-r1Kym4ADOq7xo_FBZptPAU4dRhQr30JZsk5ItX9HdeT89Lrf35KLn5iOYjXUudXtKlu4wyyaYKR4cFkWBlx2VDfcna0xRi3cLsueaW1eb9phhZ5Rul7OzcSqmGp0YMu7sn7iXzw3jgt0sY1AHN_UGr5XQlRsTZ0Fjn_uV_jzzgaIHrG40N-sWQKhJ9ivg5lTrz_Iig9Pm3IvN_pmhocD77qx6LZjzlBBiAk4Sujy5Ks33KtEGEQPj2FRzcc5ZmZIK6jbSe8GjGj25FCzUqgYVSjy1yYOVHUmTLGBmmC5Uh4lmtKNjvq5SONmh69CLRYFuEe3SOhBUYGihlWUE08WnfBBAjVS9t2KLxDzX-lenHefPCNVw2BMdplTFMZ1SBMGdtAToH6sDmYT7vvbh2cLX2Trl82oSypvWM4Ds9MMv8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=t5XwUOQBgAB_qHiRKQB6vf6R_mPQ14hJ9eLvMqmXsNGUmLPpF7_Y25YLzmY2S-E3xxCp2YMS9SyEwUDo4_1ZdBzI7ufX6AlxeyNBVSt-4Vr5Ih5DvPtOs3THGt42CdcYgw_ETZxaDXLE1FEO9rgNiTAQwGnqZxCsqGRcF3pGwQial8NfAUd1N2ywnZGz5nFrLQfXyX1ALV-iFXMPNOHmiB8M_6vqZLqN4yqsUDay0NufRCvtkvnB79N_yBBwH1e-r1Kym4ADOq7xo_FBZptPAU4dRhQr30JZsk5ItX9HdeT89Lrf35KLn5iOYjXUudXtKlu4wyyaYKR4cFkWBlx2VDfcna0xRi3cLsueaW1eb9phhZ5Rul7OzcSqmGp0YMu7sn7iXzw3jgt0sY1AHN_UGr5XQlRsTZ0Fjn_uV_jzzgaIHrG40N-sWQKhJ9ivg5lTrz_Iig9Pm3IvN_pmhocD77qx6LZjzlBBiAk4Sujy5Ks33KtEGEQPj2FRzcc5ZmZIK6jbSe8GjGj25FCzUqgYVSjy1yYOVHUmTLGBmmC5Uh4lmtKNjvq5SONmh69CLRYFuEe3SOhBUYGihlWUE08WnfBBAjVS9t2KLxDzX-lenHefPCNVw2BMdplTFMZ1SBMGdtAToH6sDmYT7vvbh2cLX2Trl82oSypvWM4Ds9MMv8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXcaO_bZ62-ZOWK0KAVev3X9JQ9eFPcEZeO7z-Rri483ncPQmvEbI2P4-94Mq2-vCGcFt0ThTx8V_JCmA2WDsx11E7kpR7kLqbPhimT1HjLdsq1m-bdxwZ98-z6ueLfbzTGpQOgP9w6cmZ_FS9sOSi3_Ioafw1NDTms6dSp75jMhhdw-kRNzgN4_Dq1a3hUNVJiuO1hpRqgkzXXCHVTFrx0917FclhwbBLI-01kEsFEYhuDvWoF2-h3OMjnIO9AdlgpiH3-uV-h5u8da7I82becVrfHIWsWNVMMR-tBwyGDGmYbdN0RdIEcGDWKsAAW8IcUehtThn_n01zTH6EkU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYLHYkFvxPwvFcD8uukNDCePP3iGzexfNEDkLi28T4Qeri9dp_r1UG-PaoLPOVaRe5JSav-guru39BFitxqVQ7_XZx0dLay1dduBWdIF0OsNufv9ZAF74OSfdSHelbGXjqq4xdfI5NaXsO5O-ASUg05Q9vs8JzFglNOATfpCbaThxaU3i1R1v8WSOQYvSewxEzthyQoHBqeQxwvCp8qsMMhnDx5pQEUZi1cam9HjH52r16JicLbmkYtI_bq-kdX3of0XBoK23rCBuX-8iZvky-fZzZ3G4rvvsGqA4GcBQK5CyGTn2H2JonC-si876M16GW1AFJ1OpJuh7uASvyOmneg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYLHYkFvxPwvFcD8uukNDCePP3iGzexfNEDkLi28T4Qeri9dp_r1UG-PaoLPOVaRe5JSav-guru39BFitxqVQ7_XZx0dLay1dduBWdIF0OsNufv9ZAF74OSfdSHelbGXjqq4xdfI5NaXsO5O-ASUg05Q9vs8JzFglNOATfpCbaThxaU3i1R1v8WSOQYvSewxEzthyQoHBqeQxwvCp8qsMMhnDx5pQEUZi1cam9HjH52r16JicLbmkYtI_bq-kdX3of0XBoK23rCBuX-8iZvky-fZzZ3G4rvvsGqA4GcBQK5CyGTn2H2JonC-si876M16GW1AFJ1OpJuh7uASvyOmneg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSzTTKzNRfE6qTtl_WfFYaXnD2GvIh2YKb5kCgSj2v0nzC8aLFOF8ATuUu8_Wxhek7d1sw61bxrg-268u64SwyIB2umtcF0h40FnEEHoL_He-ZVPPrpQi5Q89gEP4fF-4utmbLI-objo3wkf07ENwl5lLGa3dAIG_Q7D7PuxZPfnJHCxajsQuuWigxgHWijFXJQqkZ9S_1yNl5xqAQvr0SGeTfkVRak29uv6-KtPPCKUH9VSTuEbc7AuGiTxJ-XUJmxN06jmcvRZ2SgdyJvFr59PS63sRhtRgxpMr5A4G6hRGY9cuDZF1N9Na4EGfK5o_M9PZu2Qo1yUyrNYXcgcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/X0eeXS-w0MjEhxeoH2ZqTXahnWeiNqa-RQRGlljZirFGc4hkkaNXCZHvZiQClMLhl2MjwaMdx9iQgWaW9OikYMByTwZvC7GP0wUVeeCBpSnPmopR9Rez9rs9M2HYst9rhRKYz3cdvt6xhq896WxqSopAVLxRyeeM3KO4VHQZXANYA0FENinZego1oWRa7XweOgbQa9HyYfdsRMU59F9rIPKimAMNdx9s-LJmhmsKGtEvhY0OSpcrnWYl6pKf6YyNAYyXcZlbF4AiD3YGdOKb-yqDKMsRFlhvYdT8rObZ4EY5NrGgjYhNo5pkYPZzj5fBL5-_b4lymgonzVLKuY1ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/gi16A7KTyD0zlSuACMJfO-So02L9OXi22SpprLK5SW6XPnJOEfaq8UKnVuyE7zoYxuSjJkTxOi2PnRLPD59TIttL03NTucHS3mAijXx76hJLa2nYGCwl6apRsT-b3RXqv17GpqhHH9heGNHMyQRGhH9NeNRaXFvyO5ha3OpsMRYMOSfYKwDk8Xe6-3h6bYFSsA5ax3_eSGTM7PAXCJOgH7KDvmC2QdzbpSieMPJVT86HunKo5aj6mtVaH_AHBWGXrRWm6ppP96dyvQqg_Xu9-d7ra4bGLXCRIZ4mcn6jqIZhSqsPHDvy6i4nc-br6TiKQj1U2yr6P2juy2c1sfzBpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=qyk4mHH6XNlVenjsShdlE_pFOR6x5W-Cb5K7uaafsfXSpXFdd1skIX1UChyhK5rj0QflTnU28Ta8Axcb28lNLPEdbhKS3cFHsm9NDoXTm6cnzPbO69Jik_wqkN33tJiPsUCYOMvsI-TmIo4mKcETif6pT_bL77dxV9IvEUsmX4PZh2vIxanby5-yVDB4GSv0IjiQwBExpJeCFZrZ1Z8xm6ZSMEHporLYavCSZyzu8QzNE0QvcnCVCw0dIAEWIPEjHV_VA-oEQFL45rUVPFcZgamyQ7d95azt4iPE5C3ldxZUsaSUWKclw4_ilSSkoc56ekTohhgXbFAhVDYc22jZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=qyk4mHH6XNlVenjsShdlE_pFOR6x5W-Cb5K7uaafsfXSpXFdd1skIX1UChyhK5rj0QflTnU28Ta8Axcb28lNLPEdbhKS3cFHsm9NDoXTm6cnzPbO69Jik_wqkN33tJiPsUCYOMvsI-TmIo4mKcETif6pT_bL77dxV9IvEUsmX4PZh2vIxanby5-yVDB4GSv0IjiQwBExpJeCFZrZ1Z8xm6ZSMEHporLYavCSZyzu8QzNE0QvcnCVCw0dIAEWIPEjHV_VA-oEQFL45rUVPFcZgamyQ7d95azt4iPE5C3ldxZUsaSUWKclw4_ilSSkoc56ekTohhgXbFAhVDYc22jZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iogRZfjWmYDZUGto1xriwA322blkFLAgv5QrmkAds27vkVtLtwfdzg0C7juoSqzamsmiBrTK9hFrhpiuQTX4jrWGlYH766PwjBQpFZgButHuzquiuYTCHcMsCU3u57d8-ZwB2HxnmSBqGC0G6wm--xuPW89IOc2BDVwRk5c5w9Mvfz7VtUrD2BNVKcFRN3PCg5a7_Quj7-gI6tZvGsVa72i9kGc1Q3VuBAu-Xct-r7Z8wy7zpsxFuv7WCCl3cTRTL5eanld4RnAy86SH55od99qpe48FvmLJZpHCPY968CNvrpUzX05nCzweFrbw8c48JKtwch4E0RAz6G5N6GsYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=E4edzPCdIy14hpUtymQM6mKE3jfui9UOcXJ9XN6_Wt1T4dtj3gZjQVyrW4nzWQYgo-8LAkerzVw-C_ZPOr7CL8xGO4XarxDVG2qaen9kQcnh6Qc6rrakqFPGUgtoaL6uJItL06pbS8W3y6prhvX2DJg_l-yUO8CSzh3hAqbRmxleb6nhwM5IVyJjChbbU1KizGFCgGfN8ey_TVj6hRipnqs2jwStFH5_NwxbK6CxTFFLIVyfjuNBFiypWIx2fCOKF8KKK-oWCeXF3_03m14n2tPPm5Be5xhis55c-v-Q3ECwIyzd4OgO7TXBihQDX9ZR38Pif9h-jxBxj9ZqlkTYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=E4edzPCdIy14hpUtymQM6mKE3jfui9UOcXJ9XN6_Wt1T4dtj3gZjQVyrW4nzWQYgo-8LAkerzVw-C_ZPOr7CL8xGO4XarxDVG2qaen9kQcnh6Qc6rrakqFPGUgtoaL6uJItL06pbS8W3y6prhvX2DJg_l-yUO8CSzh3hAqbRmxleb6nhwM5IVyJjChbbU1KizGFCgGfN8ey_TVj6hRipnqs2jwStFH5_NwxbK6CxTFFLIVyfjuNBFiypWIx2fCOKF8KKK-oWCeXF3_03m14n2tPPm5Be5xhis55c-v-Q3ECwIyzd4OgO7TXBihQDX9ZR38Pif9h-jxBxj9ZqlkTYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKb6GgaJ3Vm4kTs1ZAerjiDoj6Am1I-H7JIg7BdlKlP1CVB9GI_8j0FfdEaK3yTP8JLdQW1uNzE7Vw3uX8vK3PgQIADMPk1qR2hM2epw9xklrDvnVSs9ZArFgScjB0hP96SGWQ5F6Vf2NLgloQdD7eZQC7AE3kxQUw4DB7GPU7ZkvhD8qlka-bvaYa_J2K8pDthLPRR5BOzWpgbGO6VAjw35s3y-Lbelv4dLwUXMC_q8DqU4Rmlqm8X1m5P_V3CWeofns8rXUlHa_LJO9ILn7WrmMwIu5uSsWzWYrD19ZM5I0QO3mTbblCDXDhiUnLzbwDnZSvO_WmGcYeq5W1udRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFFMxQ0My9aF91jQnC8hIFmOZQx5EkbAOsv53b3ugm3dj18KLoAVVMKIBQB5wz1EVLDCQndQCL4C1EG4CKvNU7XY46Mv83StYtet0_UcTjRk8DB6TN24b-SYNcEnJe_LBhWFeII0e1QGtenD-WRQQax-aIaMIk3vJdoJm23yyesLLRQa_00IJ4ipsDNhDmeGRSeHAHDHvYC4ihbOd5zTSXXkiEev2b_ASOR-0BFoeQLl8CMgD9eU317zjy_ji_hhU4Nx3eRKcfzVvifqCw8lzLV4F5wnLFMbeVGt9EtZasP_mkeY3P0mPqepL4Z4bhICL1ZPQE67MFXMxl_kE4c-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=bXYs0fNl7-RKSqzZulKEPV8HKiRacn8yk6ehgzxwy6vot1apoGTPWBRsJ3W8t3Pm9xa2h4o3lQYv8nyqV-gEWQP-9XydPyuk3DIkK8zQPyXdSac8V_exqZbH4JBb1H4yperrYHcnHkQk-_PSyEYAQcFOw6M7uSk0rMub6FQLFKoqYhDN21LuZ5tscjcTFWLO7GiJzVhP8-7A4Ii-BoPWos9OfZfXIBHqp-5wefEVvK4EpO2WO-709BvTbeDHC0rV5PXeSnBWqRq8FXGn8sjsHi8mYoC2U0Vx-0xGRdsH3yfCP0otOjjTb80WTws-OpP4TC8CyoGu7N6l_d2kIGXCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=bXYs0fNl7-RKSqzZulKEPV8HKiRacn8yk6ehgzxwy6vot1apoGTPWBRsJ3W8t3Pm9xa2h4o3lQYv8nyqV-gEWQP-9XydPyuk3DIkK8zQPyXdSac8V_exqZbH4JBb1H4yperrYHcnHkQk-_PSyEYAQcFOw6M7uSk0rMub6FQLFKoqYhDN21LuZ5tscjcTFWLO7GiJzVhP8-7A4Ii-BoPWos9OfZfXIBHqp-5wefEVvK4EpO2WO-709BvTbeDHC0rV5PXeSnBWqRq8FXGn8sjsHi8mYoC2U0Vx-0xGRdsH3yfCP0otOjjTb80WTws-OpP4TC8CyoGu7N6l_d2kIGXCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqz-wUfMJNj_krlW1lha7e7ypljwSJiyPx0QHn-rov0nJRo1lbHoonmsqqwQWgMkhzAChUGsH-x1DWi2q7HVCtqV2v7N4EYGNpSpHnFCE7ezpZq5jqgJ14QvOWafpjwwdsRUuC8Vlkq5N5zaVi6_oSEVD6IIALbx_MTnti42UU-aDBxpIoVFpt3ZMWDVloQoK4-YOYpFKY86n7UFCDiaPzN7Apby16fCkKPm7bOGchyXdRaN9na9Pd-1yVwm9zqr9EP3NoJ9-T6emlhAmDkGN15pQfRcnctcQMZQx03pqViw9HHEC5iUwbkTPI8thLGWfZ63zqaZW9w0zmjpCU0kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=VgSlx54rb4UykJRFbu9DYRY4G5L36IHvCo3IgoW3iqPrbmJRnISkmbAyD7BMLz9NE8hXPb5yC5ddLmdhF6QFDYypcxbcawSDI9GV0wjB5VCIMkg7Eg3kRF81Urw3d0k6wczQapmKJgIS4Ems8FnFQaM40YculGE8MBl_B7kEGbrywMRLHmQdLDgrBGzjjCWifEyy8TG99GCNpHox7z3qoiaO-W6MZ1qBQlIirc0qg2Xx1kq40XHaf0cDmukgR6sHbYzN0zyDaiQYpufh8ALPMcqTCDzpm0fRlUOuvD508oYnXbxdzjrK-LBCNtEoQzcRM3DX2R-yMxW5bB_snMrTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=VgSlx54rb4UykJRFbu9DYRY4G5L36IHvCo3IgoW3iqPrbmJRnISkmbAyD7BMLz9NE8hXPb5yC5ddLmdhF6QFDYypcxbcawSDI9GV0wjB5VCIMkg7Eg3kRF81Urw3d0k6wczQapmKJgIS4Ems8FnFQaM40YculGE8MBl_B7kEGbrywMRLHmQdLDgrBGzjjCWifEyy8TG99GCNpHox7z3qoiaO-W6MZ1qBQlIirc0qg2Xx1kq40XHaf0cDmukgR6sHbYzN0zyDaiQYpufh8ALPMcqTCDzpm0fRlUOuvD508oYnXbxdzjrK-LBCNtEoQzcRM3DX2R-yMxW5bB_snMrTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=A8PdrtatV4YyNg7qf7s3p14VXLkVDpRcOxasmtU6Omte_gDs6OZqsxAabRoW7hjBIzgnmxz6LVyarwesujcGtOgkhkmikgIPsTvekbvWr9AU6QKqyof-D2_piXvTPYDV-_xmd4Is4TIOjSdwTfRADdCKS1Fltudn4hTm_ieoffdiUe8sD_IDKvETwjIJJpfT6eyA3_XzEu1zOfQudXTYMmctTPv-U0AMLIvMDYglPtXL6xqEOHYEKXWTjGRn8ZC7Rbu9Ua-iFqHPC3xRJqp2YxtM6ccgiUk9xKK01myWgQkZmVtXIaeuz37NN3868xdjhnbBi972E6cc0mnL9l103w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=A8PdrtatV4YyNg7qf7s3p14VXLkVDpRcOxasmtU6Omte_gDs6OZqsxAabRoW7hjBIzgnmxz6LVyarwesujcGtOgkhkmikgIPsTvekbvWr9AU6QKqyof-D2_piXvTPYDV-_xmd4Is4TIOjSdwTfRADdCKS1Fltudn4hTm_ieoffdiUe8sD_IDKvETwjIJJpfT6eyA3_XzEu1zOfQudXTYMmctTPv-U0AMLIvMDYglPtXL6xqEOHYEKXWTjGRn8ZC7Rbu9Ua-iFqHPC3xRJqp2YxtM6ccgiUk9xKK01myWgQkZmVtXIaeuz37NN3868xdjhnbBi972E6cc0mnL9l103w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=OOHFg6TrwEAJ7i-gZJ9ripI5SATBcVJU8kXsktwf2yawu0hTElQvsJaTQNVEvQrlGReWVtBa5wWV-px7T8aUlBtTPYHsgJCMAOxzgBDaVe9nQMhxWrkWw7Voo2cKKbeJmxUL9c549cs5mrBlSryd-am4TOS5UR0wv05h5b-ClDX4SgL5nsEeZYr66BQ0ikIe3UhJKMK1AotLOoos0p0ewDn0JDfE2UpIr00uRQ_l-u7D_1bU9XyP_yZXLihhw3TW11qCSVej9mEUrbavleH5jMNPqfH4IEgObMRV6CGlO3sVOwA4Tyywg_8_DIno0NHRF_h6xL8aKDL6LrLhEuigqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=OOHFg6TrwEAJ7i-gZJ9ripI5SATBcVJU8kXsktwf2yawu0hTElQvsJaTQNVEvQrlGReWVtBa5wWV-px7T8aUlBtTPYHsgJCMAOxzgBDaVe9nQMhxWrkWw7Voo2cKKbeJmxUL9c549cs5mrBlSryd-am4TOS5UR0wv05h5b-ClDX4SgL5nsEeZYr66BQ0ikIe3UhJKMK1AotLOoos0p0ewDn0JDfE2UpIr00uRQ_l-u7D_1bU9XyP_yZXLihhw3TW11qCSVej9mEUrbavleH5jMNPqfH4IEgObMRV6CGlO3sVOwA4Tyywg_8_DIno0NHRF_h6xL8aKDL6LrLhEuigqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pruAr7b3IWzq6-jS1Uw7NOqnZC7BmZeYIIB6j_SxpP90uYgEDIft7Gruf_pohQ_Bx_ve2G_FdOcB3Rb2b71fekxC3RIRYSGeY5hXVuoyzCr_wYFOGDq_gRMPOzR1gLVHxorWcDBxBP2ZRprLMjgGdKF0ylrFzrj5-9xsjuNqDYO-8RKGFoNw0_JnqsMawHNNDzWq1mpR0_72VXm9jrSiLIM7TfPNwEfzldRnZhGXfo_Nomg6UH3Tg8TB5oMZwxFeeDBWLvNfLRsvgL32S26LfVdifSXATNjwCs_H1-MoJtwwainsfuWPLqUMxua3rn3Azv6HT4MkhiEGbSvBJqy3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNo5skr4wBWHxWmrSXt8JhuB7nSZASL-nf7t_ZMcTH42lGMY2Q8JRVRh2iJrAYMwfFMCinNkTvLBChwV3KryzjtudEkafDASF-q3MReA1_70pZkHd86hFqC-2L7z0MxszBmusI4dgCNoZqkVMaEstkmHa87qDLjgRuIbcW4H_J7DLwIDXQ6aOay09pCrVPWxi1qKKJX_ZIIJQoCzdpDmRtSve2RhoLJFuK8s5ZwwL8brpPE53iLR87Mpa_L2jkbUJvF5mi2fM8r8gQaJR4PmK-95gUbyi8np5zEC5Z5AqNysX62BBWeG2wOjdUCuStLheimNFu3aaVNV3CFmuShiqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFOZjbv0-WGbi5vybRPTnhRYjKv_JsT_idJVi0DXChPIKFwntRwSa6F43l7dYq42TvMxVifTzDKjFe81v1n_voU-s7q69b1fSwj8PS_6y1dJtg9-NIPS89KBwss6-8umUMs6Rj3d-6_D5m6xdi5Q50C9JspbRs0PxXnMykgQM3eVUgrA8APFZSJEd3gMTWu3Fp90qQ_p_mIE2r8CNFfEq4bkEH813Xh1_TbKxwMxHgzBeNJG-i4Asm6Cv7-R7Jvd6W_qy-1JchnKWhYIfVtPp_EEq75UrYEY985Mo0pc3i0JVuitXdEATiSj6ePlG_zJtj0QtqcSHKk5q4SwpsX95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=G7ud0LNfvo6vioAjXF8RkXlRDrYa1IN9BeBC5hq39TfrfMn7b9OLsA8VzoR1yn51cKs1oPDD8e4rf7c8DdNqWuOQEEy_aMrhbXLbCkIAOmCAwek3mvf5fT7snq6JQPzu9R4W07sr2g_1d0EwFV66Xb4dLd6MfqNRAtLDFapKpp302wgB8TXEj1g2R2s5KnVS1yk5XOk0hKxfGL1e_aX-nZ7KqeD7y7WqhL3-p-LPBj2Y7iXO4zPX2t6B_ATJw_1R-ggXq6DnWkub9pcmFH2Yr-0y2Jr2W9NXA0Y-lV2KYmnqCIyRaRyS0OCmdb_avQMuqQYMynLrblQpub4_OsjJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=G7ud0LNfvo6vioAjXF8RkXlRDrYa1IN9BeBC5hq39TfrfMn7b9OLsA8VzoR1yn51cKs1oPDD8e4rf7c8DdNqWuOQEEy_aMrhbXLbCkIAOmCAwek3mvf5fT7snq6JQPzu9R4W07sr2g_1d0EwFV66Xb4dLd6MfqNRAtLDFapKpp302wgB8TXEj1g2R2s5KnVS1yk5XOk0hKxfGL1e_aX-nZ7KqeD7y7WqhL3-p-LPBj2Y7iXO4zPX2t6B_ATJw_1R-ggXq6DnWkub9pcmFH2Yr-0y2Jr2W9NXA0Y-lV2KYmnqCIyRaRyS0OCmdb_avQMuqQYMynLrblQpub4_OsjJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=VYhULsR0yCWo4N1QLksM0os4_kdhdMDgVUMPF37OTfFOlRk83VAAoCe8UeCiQ3EaoIUYZj8JLur0t2_fMmH1b49-XAS2ixjJOTsOifp4DYldF98s3drMXKLKug7waDqlubVEzcoGDIUSoEC9x4G9icGvZay-gJr_GLvqCyrbbt3HTdpssDbFlCFSnDlp2WZVzKIpoRv9F3w2thJHmuQB5QeqBi7np9DX-c-6UHzkN3iGtNzjxDiNt8cFeAyH0j58Qz1ve0SxXdij0KLSQtpUqtLdbs1GTf-01BJJRhwj2RiPKCuP_qZEWYdI4ooWXxb_xDiSUsEoKILMgQbJdKZoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=VYhULsR0yCWo4N1QLksM0os4_kdhdMDgVUMPF37OTfFOlRk83VAAoCe8UeCiQ3EaoIUYZj8JLur0t2_fMmH1b49-XAS2ixjJOTsOifp4DYldF98s3drMXKLKug7waDqlubVEzcoGDIUSoEC9x4G9icGvZay-gJr_GLvqCyrbbt3HTdpssDbFlCFSnDlp2WZVzKIpoRv9F3w2thJHmuQB5QeqBi7np9DX-c-6UHzkN3iGtNzjxDiNt8cFeAyH0j58Qz1ve0SxXdij0KLSQtpUqtLdbs1GTf-01BJJRhwj2RiPKCuP_qZEWYdI4ooWXxb_xDiSUsEoKILMgQbJdKZoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=Sla_HoIBz4zuFkmRUSFPd4vglFc9Riq1cTSKP2362IGscmofKoL85CshHXrC83eBiEclHuOS3SXNtyU_hVZPFkBEikAi2pb0hjQUK7lNjFcMuFCIOIK9shi1lw0s16Z28KAdn5uN1F0Qc58igcugnLrC1pcRA0h1K14Et4i6p8wZJJ9EjU-bqhJcqsok5WdnLLj4MAQnif2e3xDpMFMWBqBGrpzLZfYkcB3Bk2isarjeHujoWf3TwBDRlxZVmRp5N2drkur3D2Op6DkRQHQbu5HMn5QKgKt0GYBjtXjxMCWPsJyK9kMDrjk62DcFuOQJXCIzEQ6J4lFD6ZHyTEJZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=Sla_HoIBz4zuFkmRUSFPd4vglFc9Riq1cTSKP2362IGscmofKoL85CshHXrC83eBiEclHuOS3SXNtyU_hVZPFkBEikAi2pb0hjQUK7lNjFcMuFCIOIK9shi1lw0s16Z28KAdn5uN1F0Qc58igcugnLrC1pcRA0h1K14Et4i6p8wZJJ9EjU-bqhJcqsok5WdnLLj4MAQnif2e3xDpMFMWBqBGrpzLZfYkcB3Bk2isarjeHujoWf3TwBDRlxZVmRp5N2drkur3D2Op6DkRQHQbu5HMn5QKgKt0GYBjtXjxMCWPsJyK9kMDrjk62DcFuOQJXCIzEQ6J4lFD6ZHyTEJZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q04-QQJmdIR_MIzXg5_s9VOHG7VhAk3gxsA2JTwyIGQIfoyDz7UaXdCklcV-ofy_fKgTZZnSkq5HeVUQAilS4KvyJgrO8W3f1bNcNidWFTS5V97hBrbYIrfFZOiO1OCBEsy2rpy07KUJcp63sX5-H1882v-1GW5DjoLyxhOIkWLXkW-fcQWdCo2OA85jvZgPVuPyDx5yuqd14mVotesfrixOdmC2HmuKcHSPvQxNp1DnnjGmvBlQaxmd-0doN60R6TwkmYvVaf4qMkYQqCWFsoY_A_OKiDRdcc1aG8XWa9YqBl200FE0u_r-0NKxyYRAvS3h37Ch4L_4B9g5aQg2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQSXkazvlLqDiAjb4vk5YG7kldMScfHT4aEebnZbDqC2zRpjo6uQ5t4wFG1EzpTr3NCCcORz15L_hx-sjyxQOMrgDdg0iWQQQwh5GjxZ8WFnGhWBbOvVU53btYngL75MfQPnAyGHIWm7uDMr4baQLBlwMX6EXEeicDlJbw948Rui9DIok6IWu9sK_BIDBPZAXPfF0SEyTgTawSI6lFWW95ugSIt1neJNh565mlOt8X0IVe1kK7oBvqsIe6AEirC9-fcxkG0GfWEKQy68qTwqokVF_Sdah7GzKmBRJ7HCixxwDm418YSvYN4kYJtMMWTBsEptC_XGG9VozMbFKVcwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7xySdGDj643q2bGlQzF_8hj2tYV08CYKuKk8wehCXHkmOv0m1xSvCZwFv0zD9ZrHNS1HIf5iBsmAxflJio7HDL6L0aQ2NsKLvSekJVqMeat77gdougW789OMOQiGNaDQ954evBD-xgrd7n1_AOQvZXodADXj_ZfyfMG--3VRcmSSW8vQKpZXgIGZTkS-7nrFpFu16R2jRR9LhFgdrKuMoND1dTJGzmND5SwVwuAzI6k8OrNfA5XW58-_RirtLNhom0xKYO_K2jC7nA0rB3VESQieXCEI_D-_JPIQTWPnqhGLsmhjsUFT9JJX2cxsnWIKG__ZZTJqHp2bf3FoN81uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS-AwER1iQwwt2mPpErVrQpujhZzhG-Rgq-gvvk4wzcahDUYeWxHOtNfPsgWc9eXYCxLNYtK6yGrxcMHeoRArkbsW7r6VfqNs2GsEi1J7O9hpJkpKxtmPmVWawdo-PlrjRqKwEpJ5P5xONywGHOxWhAkBLNFKndRSPCGmTjAIU8fG9-oAts_BhkASlL10suMiwR-_OooUDdouQCNXI88i8RMtW6H8J94snELGyknOm32tI0iKLDYCkQCuE5DyLKTLwgGAOPwqq8yXdTB2_nuOSExbrNz5Hc3Xhleiwbo98216GuabVzId6dI7YmPs5PMKmDTN1zc5htWcKdXq2MbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RnZmPBOUFVTWNxtT7mQpd7mhGlZCvBdy7JO3xMlt0BobjmGyQtctW4jR5UsCsLSEWDzrd6l9sDPgey-2S8TuljTkAW2lo0rq8gSNkkRIM7JPq0RqSqsMXdT7cN8WQJgxfP4qDTr5wfXJKwnpaP39mCzk_PffdAvocR2lyKYCXBbgZsSr_jCWfAvk4onLfx2zVCQS1OL561MguQyhpxFSv2-bpTq5cfP7oAiCQeaPzeJxgHG5zYC0Ryb_zDG3TsCyHorMEHGlPEAyy6azhl-e7USOR5TL8iLldN1hpvPBEqr6XMZef3KWPx-FciukbjwCnZEX_c6lp2-__XVb4hS2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxZq0UQ_YLckf34w8n5gxHgW8HT51NjOoYkLM6dbQ3KoZCl8BS5jFsCUQ8CFXx64UJ8taxRaZyTImGTBVMOo765OjnpjVyWEcYUFpT1nqRAPR0j6bHgyYWW5-84rxLnwdBBrv1n_P-17Odyml5eJ7PyDr2O8LWOYLVgHEd4SEKMnNa2NuYzJY8guPrq--DP8Tw2hOJNtj6KQjEaaWaahhacskIvImHq5PRjvROENqIqoSeQAIZcWb5VYeWAjphq3gzjm6kEa5ihmsJ1SKh302qakV7N0J34358UJ_yXge3IP1ZS6h3CiPCeqSkJDTCeTfkQ9z_kGcpvnaG4yq1Bbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZnZXJkA45md75HhB1Y47hyWhWka1-tvVJuhn4pjKR7rGlb405IDqoBBSUfZfJfboAoB78bF7_qloBO3Ft4T95e_JENo03IbaBNDn3cNUaRcHyofa_7UYOjOhfgblDT4-nP1avARGNGyGIDEez2pzEu8bcaAJMYnMlJTJqvPi1v5ejGzKwPoWGzRcakTsz61MqGjoUwZlO8GKrN5sHWuMRQXE3uO_69bLyQ7EcXCrtLp2f5vE5azO4LmJNgIOYta4lbBVAjb-F1R9LJbzh9SR68CUi_cVprOq44SusPu9rb6jRoPRLwlqe0uJRIsp14vHYWHx8nzsWLyJzQ0niRf9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dHPyNhLD9aJThQ2IsLqxI42YNMsu5kfCnmVGnUPKa1Em6v10ig8icTovmT7LHtV7gwjf_VUj-5Er28FhL-6ayd5ct9bbzdcwg8vYoBhrYawHnbNg_sIEQiela7gFazQ4m2Mzz7YlENlIws7Ee8uI6KA2BNBRHuh_QLOHKklnRsUVdgh0GDOuv7mjlpPpjdEp3pFpO4My2VgvvruO9EkmeYGd-vpKMdq3xDHJ5SpIQTqJKrbUbTermO6l8K6mg4ZDE-yXZtahOqnarP5heEFL2oVhGHRFeOHIFCHe_VJl5lYRvecbFO3w7W5D5qYtcKpHIXSRBldmSIXkjB_6klepQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=et6GnOumT7dcEoJXlKAZUNfjRdCFkTbBt4ko7_q5SkD1ctUBZ5alqryKUh--fQXD2ZSbdtlUsn6YJg2D-0ah6213uiSvKj4zgB6zbkhf7mlVOMbTSXjsUmDnHuQ6KQndFk9QM6bGbvpg8EzKinsFIKWflYGCge6VvIRQlg6cl3aDrhSsmz6DZqETGGQQEAMsGhSMtshfN-OOYDo8_WnosrU7-i9PKXyFAeLE1F5dkfCBX1FctSWJeC0J4k4AIMoTj3eqxg4FcGDCDZjUIROfVG_E4ZNsIcxvM3KSjQsN0XEk28ReVzWzaU9MuUwXaUEMgfAQviyfC8Zlo3H-FAOmFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=et6GnOumT7dcEoJXlKAZUNfjRdCFkTbBt4ko7_q5SkD1ctUBZ5alqryKUh--fQXD2ZSbdtlUsn6YJg2D-0ah6213uiSvKj4zgB6zbkhf7mlVOMbTSXjsUmDnHuQ6KQndFk9QM6bGbvpg8EzKinsFIKWflYGCge6VvIRQlg6cl3aDrhSsmz6DZqETGGQQEAMsGhSMtshfN-OOYDo8_WnosrU7-i9PKXyFAeLE1F5dkfCBX1FctSWJeC0J4k4AIMoTj3eqxg4FcGDCDZjUIROfVG_E4ZNsIcxvM3KSjQsN0XEk28ReVzWzaU9MuUwXaUEMgfAQviyfC8Zlo3H-FAOmFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0oWZVlMey3DkFtqMEzKdhaf5zKWKRrONsrbj7rHIZQfGmwdfJtwA6ucz6LRKpEhF6_VGnEPq3upWrd0iqj1MX4USGqaBNJQty_zaFk_dW4odr2oS91jLS-KfBzmCycDtcmfAzg6x-16mgZ2RBktlV31oE73kLJojZuD-sDtaJqMwokGPebXhp0_VOkwv59ABxlenNtewErs_ULEhCS98lhasFbYvgnoPM7-UUUTjm_x9hSI9reLQe74n2mR3Me0vcAvyYiV1s5MRokOAJFrP3DKg8JMBMi-gdOXKIHlOnVZOyNymm1boPx8F87Y3nTuJVFosoz6QZ5Uqx0JszGfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=G1E8lrWb95Da8h6IYDYXWmzmc4Au4upHE138JkNwL4rHeihHtYYtoxZqrvPpZpDc6vcJ26yEXhLCYpFDkAs-EugEc78jhac1QLpumABSf4J7Ar66Bye-xR-5fo52eU3Fd-soZOVwLGdorMBA6aJqqI_BXJsJlBJr94bsKBO6yhZ1xsX2XA7O6umVIHA3jtMPVRgTU3YhmFEf28UPfi-YxpSCMfcHLYFe7549cX52rbPVldXzo2uwD2jfiksrGG09IWP4VxT-kbw_GAONys3-NZtWxhudW_4lItrq0v0E5xSw_r5H-XIinw8-jTd3J6FyAhdRQLsvhak5XvRMnFLQvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=G1E8lrWb95Da8h6IYDYXWmzmc4Au4upHE138JkNwL4rHeihHtYYtoxZqrvPpZpDc6vcJ26yEXhLCYpFDkAs-EugEc78jhac1QLpumABSf4J7Ar66Bye-xR-5fo52eU3Fd-soZOVwLGdorMBA6aJqqI_BXJsJlBJr94bsKBO6yhZ1xsX2XA7O6umVIHA3jtMPVRgTU3YhmFEf28UPfi-YxpSCMfcHLYFe7549cX52rbPVldXzo2uwD2jfiksrGG09IWP4VxT-kbw_GAONys3-NZtWxhudW_4lItrq0v0E5xSw_r5H-XIinw8-jTd3J6FyAhdRQLsvhak5XvRMnFLQvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=QFBuzu8Ba6pQZQhWDKU4nam43TiojNpveVvoFD_FAP3uKKHBEI7NZN3G_ux9Nldz0g3CKkzIKprzBX1ck44hZkz7dflTiQFG2ibxvzeP4uYgoejJzqJstWU_ib4rM23rmmTmOJNdZhm2TlW4AtRM35Y6djv9MGqfrK7K0ulXBbacv5QRE475XaIC_YkFpbzuKA_5j6jHnW7CAohdbZ_4xh-xE3fZ_M5_eRazC_KgrDe__sljQoDSw-lTnqtzBe1zmLATo2qVsXJ0tvozeyNuD9YNha0HTiJfWqz62RIivWX4te9R741Nq_r7XL7PjS5W1mmUbLbOFmODm6yarMveOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=QFBuzu8Ba6pQZQhWDKU4nam43TiojNpveVvoFD_FAP3uKKHBEI7NZN3G_ux9Nldz0g3CKkzIKprzBX1ck44hZkz7dflTiQFG2ibxvzeP4uYgoejJzqJstWU_ib4rM23rmmTmOJNdZhm2TlW4AtRM35Y6djv9MGqfrK7K0ulXBbacv5QRE475XaIC_YkFpbzuKA_5j6jHnW7CAohdbZ_4xh-xE3fZ_M5_eRazC_KgrDe__sljQoDSw-lTnqtzBe1zmLATo2qVsXJ0tvozeyNuD9YNha0HTiJfWqz62RIivWX4te9R741Nq_r7XL7PjS5W1mmUbLbOFmODm6yarMveOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJTS8qfl4wD16Roo_W00jlxVh2R9XOXj5bVt84icHJ9Lk6-TQtep3nl9gL2lNcLgxPVGTO1RZpu7V1K0xgRzuhf1jPIuOV_euJ0dh0-Hj7_F-SXqSDBQ5fNcCRVHqNsLJzHR0gMWtznALLniYI8gkYpYsM5wj5XVFEyY--nDBgmWlGVeU6-UaWG8AAi3MRtZ8PGIvEZmWPWVKz2dSzPmsBleBARh5rNAS7CC7M1DYZ26VpTNycPA3Mw1uwHZHoxybvBOMiAXFu7CE2yuZ3UtDtRzvTQzRlo1-PidmeDJdibS4nz1ItMDst8dDiac2-p9_54rt1tmdyL13k336EWA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
