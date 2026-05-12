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
<img src="https://cdn4.telesco.pe/file/lowYcSn0XK7aIQbaTOU1ed5wfYafMkO27kNDECxkMbv6mh8EZ5ryeZX-3U7fH5gC6JuobQ1Ntxbo2hHKcyMLQfa2nHd6TD8KmqzGZ3ZHxYditFOu57loIvQ8pcTPNUJsqwgn7MbbcZiXoxHbHSGuNK3mN4RcBOL2IaTaCk2oYlSB2lH4IfNYmwzNBRfUISgEzI1ZBugwf1XeUqpsRwdkIk6sAb3-vFOXQ5fOzeEBpZC8OrK_G5lFImwXeQcK4CDy5naXQiXnOnsfgarGoDiWsyIuKX1bAyQ8JupI8BKQlHSP-FbRGfr8VNXorcfN_T9t_7mQdWxa-03kCyC8oRSLkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 962K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 02:09:20</div>
<hr>

<div class="tg-post" id="msg-119631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7swM9MbjVjsF3Izn3zMHq7Y6xG8EDoU8Br_8mR5PXpp_YNiPgw-KvuIA26xoAz6pfInQZEfWNUdNykqiJOpr80-0f4czBAZcJIhEYLAqWWg6WKX3o8RSeyW_kycaxgW6-AwyvJwdfIAXo9L5FXDtb6XH-fnvWoWA3TYijFSRbTDFAVH3j3T2R3310Cno304tl-Sh0s_gLrnOR2ZYP6w1vBpTiVTT6c38bIR7S7kVDzRH8Q2aI_b7tnTaNzyWHb-ZFj2H4rLP_1JM1RZafcmB_AF6zlF4bYrSsOKj7AxKJ84TnGop1QzprKtikaxUx7OP1bh0mx1Y9N-zPrR0eXR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران امشب رو ویبره بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/alonews/119631" target="_blank">📅 01:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b1310b3d.mp4?token=CWmfZaTaDYwwbfLDT-1sq6iW3U5RDBKmSG89YRMeiwilgawEHCM9MQWiPnnuIy_3PnWCPkWkt7uSipLeKg1EM5ICiT7HHr3BpmFiY_FEEl41YAyJBkU8YAZmsHJsXCrRvI4Vp7kuyY35pPKx69s5a-EhC9l7BduaomBPFJTKEPrjl9t0-PA1PHP7hGskiQ0M4ORRx8-qnqGGxkwseVljQ1qfEPMqHF_V5m9Vs2qtWNZ-6lJdwhE1WSdPl_H8KwcSTBKxMkAQx4E4hLX87wIFxZ3afgdMsUBREiVpE7NlqGHUizNv1VvJmP_h9pBlJIqRt7Jcf3N5IRBLF9WlsTijwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b1310b3d.mp4?token=CWmfZaTaDYwwbfLDT-1sq6iW3U5RDBKmSG89YRMeiwilgawEHCM9MQWiPnnuIy_3PnWCPkWkt7uSipLeKg1EM5ICiT7HHr3BpmFiY_FEEl41YAyJBkU8YAZmsHJsXCrRvI4Vp7kuyY35pPKx69s5a-EhC9l7BduaomBPFJTKEPrjl9t0-PA1PHP7hGskiQ0M4ORRx8-qnqGGxkwseVljQ1qfEPMqHF_V5m9Vs2qtWNZ-6lJdwhE1WSdPl_H8KwcSTBKxMkAQx4E4hLX87wIFxZ3afgdMsUBREiVpE7NlqGHUizNv1VvJmP_h9pBlJIqRt7Jcf3N5IRBLF9WlsTijwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور مردم در حاشیه شهر بومهن پس از وقوع زلزله امشب
🔴
برخی مردم در خیابان خوابیده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/alonews/119630" target="_blank">📅 01:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnMcqjkJI2OARX7M9k3ZRVbBYd7Dpe9csZTpVxDPWeeqWPyWPHrmkzBYG2rfxr3Ibzs7u1RHP9uK-VHhkMkeT-hHhaWkQ_Pn71mnFSrtoCu1_63DY9LPBFzVJGE0xj3a7qFn7XeyNVq5Vx57QJCmzncH32ALPJBJbJWqcMiiJNtvjLbgLf4bzPPn_6P6cdVk0M2CE5D9gpnGdBTFzaBtDNOiY60zzT32PDkwBNOw1ecoxVs6Mlk-8vBTwc1k7q-MP30QPOQZAV5QCMNr8Bomb2_yUemvb6IgtpLuetVNyN_C8m7uPSpDl-DBBWLjIesTg-eq3XB3fuHnQRJext-SUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: منابع میگن عربستان مخفیانه حملاتی علیه ایران شروع کرده و تنش‌های منطقه‌ای هم شدیدتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/119629" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp9VZf79tk6LdWtjCZleW00P8OBS_0IdzqHdwlxEoVq9qR83gP-elwikWHsegiFa3vK_mESFFnW9UmwbfMNRcBJCTVWWuIHCynz12Rt4psh6np-u02TErEqjoiCtCcCmYJZHF6pc3MeVvcNTaHzBn6DyQJ60TpM-SoRVtm1467tQZy_XS_51D6VCwhjdrXWMSPkS9_5zGKCqpBic63XS88Nf-BIziHY1yGZX9nMcNoL7WuMqIxDWHDCN5oSfaYZbqKUly-c9y3M0CxplSqH8G80v0RNKGKaFo15wTwMqISsYd6pUriGbhLpyx54FQjY0VQXWnh1fsZd5nd23zioCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به سی‌ان‌ان گفت: اگر توافقی حاصل نشود خوشحال خواهیم شد اگر محاصره ادامه یابد خوشحال خواهیم شد و اگر چند حمله دیگر هم به ایران شود، خوشحال خواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/119628" target="_blank">📅 00:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
طبق معمول پمپ بنزینای تهران شلوغ شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119627" target="_blank">📅 00:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش مقدماتی زمین‌لرزه مجدد در تهران
🔴
بزرگی: ۴ ریشتر
محل وقوع: حوالی پرديس
زمان: ۲۶ دقیقه بامداد
عمق زمین‌لرزه: ۸ کیلومتر
🔴
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔴
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119626" target="_blank">📅 00:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
چندین پس لرزه خفیف در تهران ثبت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119625" target="_blank">📅 00:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عوضش اورانیوم ۶۰درصد داریم میتونیم بزاریم تو شیشه نگاش کنیم و روز به روز بدبختر بشیم
😍
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119624" target="_blank">📅 00:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/زلزله مجدد در پردیس تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119623" target="_blank">📅 00:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مردم تهران باید امشب رو هوشیار باشن و زیر وسایل خطرساز مثل لوسترها و پنجره‌ها نخوابن، احتمال لرزش‌های شدیدتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/119622" target="_blank">📅 00:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پس لرزه‌ها تو تهران شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119621" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/زلزله مجدد در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/119620" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKfdt7b3wWGcKDRz8OVrwlfUReyXxAU3kwSPrS9UtfxRdXG1pz5HHrZSRNh92QhmV78a841xfTF4Zu3ix8l02UYQwh34npSHZ5t4k9yRn_VQWIiB37pS9S-HaoulERHPRDonCuaBCzzH2ydMzet4hdYvdvCQ2VKw9S6HK2b8QO4xt-CFBh--GXb3bQTgbXPMvof6Dxzv0Meac9FWbpyD9GK8AkRwBBaOgmJ79DWrSTSyfhD8vQXesp-ojcLqIFYYxFywrdS3szVpKBobERVRUOCsNISXUe96RRTKwetsfyhhk6PCNcbHYfM6Ab19V2bog4XwKCRhEX_PwTsHapuMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم بعدا میفهمن با قطع اینترنت چه خدمتی به ایران کردیم
🔴
دشمن برنامه‌ها داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119619" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119618">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
⭕️
⭕️
حجم 1 تا 100 گیگ  بدون ضریب با لینک ساب بدون قطعی سرعت بالا  و ضمانت بازگشت وجه   قیمت هر گیگ 235
💸
برای خرید به ادمین چنل پیام بدید  خرید آسان و راحت با کارت ب کارت  ثبت سفارش از طریق ربات:   و اگر تمایل به همکاری دارید کافیه به ساپورت چنل مراجعه کنید…
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119618" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی اورژانس تهران: در پی زمین لرزه در تهران تا این لحظه مصدومی گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/119617" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhJvAOaji6kJ3-3bPbdv5B7i3z4N62pIeVU0fT4B5D-YEkbLOnfApeBTTeLOZ20eUclmILOpV3_rUOCtU6jo_Y10FRxnEYvOwSJJQ4R6G0uMsH6ZNVWwybvnuAdikYGqJkcNUu1uGDseP7M5mRz1HHQwHbX7GoLHjKTSxD4vud2n5P-3if5xvjaJ1QG9fDINzKTwWOF_P9hpTqPeTpa7VbcfDfmEIdxfKAgCIQQHSfFn8iNv2LhVaocv0KeZ8Rt5f0LAI8M0cZxKuWZNIFIAcXInF-V6-i01lrxZXHkKBQwERqeJ4SRamPBYlObSVKClSMjvbkEHJ7U_ykXZ-oWDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در زمان زلزله چه باید کرد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/119616" target="_blank">📅 00:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS5Oo3ludhesBm9dG1r5XwBW74n46f1KBsL9U_20Cdx4z69NE68prG_FE5kwkzhGIGaAXhfxNVeS0beu1ZzKZbRVNxqhLDcGM-ucYrt4Q-uFG4YH5dKm617h9wN8J5oZLmw3pPyqyxDvotIXH_zkn-0Hdl1vePb2MjXocN0wXS8Fw51up2i8yPccLuQLISAPILWFQeSkB0VIAN27NoKvB5aTsvyHb5As2CAhdW5QPZcUqU7l-dtUzJERgtuLc1MjN-wp62WkmT8EHZqv17ge4wndQvm-y4fbdj7_uDS36Un0fh3cUFNTRWLMQxhV2bPGTRaNzVPGag1jJo433esgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانون زلزله لحظات قبل تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/119614" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119613">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مردم تهران امشب هوشیار بخوابن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/119613" target="_blank">📅 00:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8qmvaGZPa6U5vBtgz07m9x40G_zVhr9Ro2Iznq6MzsN4ZFw6TC1FiVwyJVPY1qr2J4NAFSsP6L4xVbP2DNGGp4m93GtiOmuJhJJn11XcT50hMujugZFx5AM0G_H0WbHN66lF3ZYRlvgZr-VXSfyVogx9AEBJE2jvhfCX5KbqcOAMJeQypNwKAByxPzIoh7xibhuQ3TjLIhIyhHf1BV2NDG9jj32Wcy-WBWAKii3P2ivybhpttpinvyKafDPxcc8od-NUAATNfftCCSUqhrEb4Byesdnxl6rPGrzFPdNUS3vPdGHHOXgOSyVZJQ15pIdTe0-eE8KYFXB-SS20hj6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: وقتی اخبار جعلی می‌گویند که دشمن ایرانی در مقابل ما از نظر نظامی خوب عمل می‌کند، این عملاً خیانت است چون چنین بیانی کاملاً نادرست و حتی مضحک است. آنها به دشمن کمک و یاری می‌رسانند! این فقط به ایران امید کاذب می‌دهد در حالی که نباید هیچ امیدی وجود داشته باشد.
🔴
این‌ها ترسوهای آمریکایی هستند که علیه کشور ما ریشه دوانده‌اند. ایران ۱۵۹ کشتی در نیروی دریایی خود داشت — هر کشتی اکنون در کف دریا استراحت می‌کند. آنها نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌ها از دست رفته، «رهبران» آنها دیگر با ما نیستند و کشور یک فاجعه اقتصادی است.
🔴
فقط بازندگان، ناسپاسان و احمق‌ها قادر به ارائه استدلال علیه آمریکا هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/119612" target="_blank">📅 00:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش مقدماتی زمین‌لرزه
🔴
بزرگی: ۴.۶ ریشتر
🔴
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
🔴
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
🔴
عمق زمین‌لرزه: 10 کیلومتر
🔴
نزدیک‌ترین شهرها:
🔴
8 کیلومتری پرديس (تهران)
🔴
10 کیلومتری بومهن (تهران)
🔴
11 کیلومتری رودهن (تهران)
🔴
نزدیکترین مراکز استان:
🔴
41 کیلومتری تهران
🔴
77 کیلومتری كرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/119611" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تمام پایگاه ها و هلال اهمر در تهران به حالت آماده باش در اومدن، تهرانیا امشب حتما مراقب باشین و از زیر لوستر و دم پنجره فاصله بگیرین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/119610" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شرق تهران باز لرزید
🔴
اهالی مناطقی در شمال و جنوب شرق تهران از لرزش مجدد این منطقه خبر داده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/119609" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/مرکز لرزه‌نگاری:
لحظاتی پیش زلزلهٔ ۴.۶ ریشتری مرز استان‌های تهران و مازندران را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/119608" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بعضیا میگن تو شرق تهران تست بمب اتم در زیر زمین بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/119607" target="_blank">📅 23:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ایرنا:
در تهران هم نزدیک به ۱۰ ثانیه لرزش زمین به طول انجامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119606" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
امروز پردیس چندبار لرزیده و نکته ترسناک اینه روی گسل بزرگ تهرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/119605" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
این وسط فقط زلزله کم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119604" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef9a6ce7f.mp4?token=v6WX1TO1lwJvICDB3KgpaQWuSR8N4ZHhpi2P0DYQwqf0Z5g5AYky3Kg9oGL6qj5HNazPFLVQaiZY8FWr9VWmMi7AAziuHUTnY5cZjyeJ-TXtbGMJC3tTvMGGoxc02QLkoMsKX_Qwgh1GdvUu2-SYH8McEUt7EyKnsykNbmgT66IdeQju482EBDsjGjWD73tRqTGlMCWx5fJU1yzuIiJIGos3AfpXtqKlM7j8oLmKtM84UoNOG56xKiedwIF06nMjKzwgWEXhbPhabaand75PGTeaFVif0jz8wPYS17jc4galowjA-PvTVqrSCyHZ6yoHQ5ciT-59d7F5IvNFav8ZmSO-ZGBPGKWGJp0r8C7cH3aJWM5X0Os_k9S-slKcze3Qw_O4R568CpYDZLjk3Ky9h6SVcVTAgxHLzux2J7C3OYI_-y0bvkwDwdYQlDC43pMiL-tTruY1ginpthiafX4zOsYBJo6Ds2-68Tv10ofrZ3j0kLVwXSFOMW4EMMxXU_KSYVSxpWm_qTOZhB3Yi8nwmIMfS8GDM9ChbwAUpVW1VOaU54N2D6imsmzPHmu-MgN8H9y18HMsXHi8tVQy5jwPcnQ--uxmc0axuCGPZTDnx1caY2WV4Hd4fbbUFXc3IhvEhlqR-MlFGf9ul0-ZEoOjIgLRDuhi4JaHjTRZBphfk1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef9a6ce7f.mp4?token=v6WX1TO1lwJvICDB3KgpaQWuSR8N4ZHhpi2P0DYQwqf0Z5g5AYky3Kg9oGL6qj5HNazPFLVQaiZY8FWr9VWmMi7AAziuHUTnY5cZjyeJ-TXtbGMJC3tTvMGGoxc02QLkoMsKX_Qwgh1GdvUu2-SYH8McEUt7EyKnsykNbmgT66IdeQju482EBDsjGjWD73tRqTGlMCWx5fJU1yzuIiJIGos3AfpXtqKlM7j8oLmKtM84UoNOG56xKiedwIF06nMjKzwgWEXhbPhabaand75PGTeaFVif0jz8wPYS17jc4galowjA-PvTVqrSCyHZ6yoHQ5ciT-59d7F5IvNFav8ZmSO-ZGBPGKWGJp0r8C7cH3aJWM5X0Os_k9S-slKcze3Qw_O4R568CpYDZLjk3Ky9h6SVcVTAgxHLzux2J7C3OYI_-y0bvkwDwdYQlDC43pMiL-tTruY1ginpthiafX4zOsYBJo6Ds2-68Tv10ofrZ3j0kLVwXSFOMW4EMMxXU_KSYVSxpWm_qTOZhB3Yi8nwmIMfS8GDM9ChbwAUpVW1VOaU54N2D6imsmzPHmu-MgN8H9y18HMsXHi8tVQy5jwPcnQ--uxmc0axuCGPZTDnx1caY2WV4Hd4fbbUFXc3IhvEhlqR-MlFGf9ul0-ZEoOjIgLRDuhi4JaHjTRZBphfk1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
شیعه وارداتی از اوگاندا تو خیابونای تهران دارن داد میزنن:
🔴
«مرگ بر منافق» [یعنی معترضای ایرانی]
🤔
یه عده خارجی از یه قاره دیگه اومدن تو کشور ما، بعد دارن برای مرگ خودِ ایرانی‌ها شعار میدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119603" target="_blank">📅 23:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فعلا بزرگی زلزله تهران مشخص نیست و لرزه پردیس برای چندساعت قبل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/119602" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119601">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری/زلزله در تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/119601" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119600">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل نگران است ترامپ ممکنه قبل از حل کامل مسائل اصلی جنگ، با ایران به یه توافق سریع برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119600" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/زلزله در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/119598" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhy7bhBKIK12feiBVh5_8Z5bua6MuCLe2-o0nTRLuXpWeyxkNG3dL1MB_bnRhAMEIfDdKl7ASV32aXd1Q7zN0gwBMq4kunKNMASBU9hezT_l7lwhCr-agMnUpa20FgbcvK1nFIOdrX7VF59UAYTrNoeVvoS3iupSw9aB0KR6tNZqtflCWXz0QJMKvmV2a4lAPIw_EYyvdVvu7z_nMWNW6ZoDTSXh-XuEQUhP2uKkXHHe_SpBIW-4TeCTnDIXsd52CDmFUD_i-ksSNts7J6pq4TZ0fTdbTkoWcFCr7-vDIw23lgElGTSIPAnR7-98707hPfrTjwTY4zlgghKYW4pNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی، مجری محبوب صداوسیما: هرکی ناراحته جمع کنه از ایران بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/119597" target="_blank">📅 23:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/119596" target="_blank">📅 23:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qMb86eVlW0DI_p5k9PlZZanRSKrkLCofcTQjQG-mzLOg8S3DR7i8WP7CVByRaj7CK3ay9fiGbMJZvrX5VjzqD_Ifneho_j7rjvvbGy3z1kqGASTq34ZaMn-9m1RgFufxzc9n9SgPhkrcq2qtcrXBpEwHW7lHoovREN9Omlb9GcWoLEBM0s5__gnstqTD2fkNYxVju_nxSpe_IN_Z1BGndxjImrk71YlNfUDfkCFsKqnWfHCCcuA81swbCBBcqBAkfX0Mie56FYHX_dVMHIiUJJZQ-UbkLvoWKJWEqlSdhqGTu0W8YyBBj7X0_-s8dt_X-FpBCJMdbNGLYUqjN1JDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران عالیه؛ فک کن اول باید نیم میلیارد بدیم تا موبایل بخریم، بعد باید یه مبلغ عجیب غریب بدیم که اجازه بدن موبایل آنتن داشته باشه، بعد باید پول بدیم بریم بسته بخریم، بعد واسه بستمون باید بریم پول بدیم کانفیگ بخریم که بتونیم از اینترنتش استفاده کنیم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/119595" target="_blank">📅 23:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c91d54e64e.mp4?token=rHRrw_UjiZ6rriLslix2r17Tt4NhKEBEyoq0L6sxICbXn1SXI-BVAwp7I4a1NhyqBw66B5veZPmorlx0pBTzXYdhZ_0q8GO51V7oEpTps5jI8GUpWEJVHtkhNkzTenHaaQxDmLjxunQuSv0DZxdLGbANxvu6mJ-umF6M1tMg5gpq0QSTaYeJuDyCI4Et77y07neYqYBFMohmsVjxsnNWQVtx8KGsTg5Ozg32_IWZjBIUNXzgA1mJwgloGHr6F_9TSI-l4j-KyIVyXOJQiPonP-C4oGFGJFVVRPHID4f5GEgz43CLOpKGFQAIAVTxtyU4yP9yKDrEbd7eJOwxl-qDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c91d54e64e.mp4?token=rHRrw_UjiZ6rriLslix2r17Tt4NhKEBEyoq0L6sxICbXn1SXI-BVAwp7I4a1NhyqBw66B5veZPmorlx0pBTzXYdhZ_0q8GO51V7oEpTps5jI8GUpWEJVHtkhNkzTenHaaQxDmLjxunQuSv0DZxdLGbANxvu6mJ-umF6M1tMg5gpq0QSTaYeJuDyCI4Et77y07neYqYBFMohmsVjxsnNWQVtx8KGsTg5Ozg32_IWZjBIUNXzgA1mJwgloGHr6F_9TSI-l4j-KyIVyXOJQiPonP-C4oGFGJFVVRPHID4f5GEgz43CLOpKGFQAIAVTxtyU4yP9yKDrEbd7eJOwxl-qDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل : نتانیاهو در تلاشه که انتخابات اسرائیل رو به تعویق بندازه تا قضیه ایران تموم بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119594" target="_blank">📅 23:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دیدار معاون وزیر خارجه نروژ با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119593" target="_blank">📅 23:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
صداوسیما:
الوعده وفا؛ داریم اینترنت اونایی که کسب‌وکار دارن یا تو فضای مجازی فعالیت می‌کنن رو وصل می‌کنیم(بهشون سیم‌کارت پرو میدن) که برن عشق کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119592" target="_blank">📅 23:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An9RPmD2CeQRV0mjz8Kpk95Y2qcu8ZEZpNuBgNEK_jLjnJSlSBAS24eEJNqK3gfozvXau-6inh4fyprEMPwxgqJrVaEwwGQ5iQmtvFjaeg_q5Hmh23jF5TGo_0ltM5w0zzD_MwV9ykGsz4mE_srVh58hKGcORwci51oXYxGpCQABrBpivTDpjTf2Qp9SFlaFg64Bsu6c7GRPuiUDFSdNHZyP4e_02AieWJ0eoFSQ7In-H_HmsmcYfQjVPnjtdlNlvwNeI7eFbSagOTnZjokARof-jdz7ljlRJrMQj56ZvB1g1w2QiTTg5qvvXLgROD_B01ZgX49HBaVqsf4_259xNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست میلیاردرهایی که با ترامپ به چین میرن
🔴
رئیس شرکت بلک راک
🔴
رئیس شرکت گلدمن
🔴
رئیس شرکت مسترکارت
🔴
رئیس شرکت سیسکو
🔴
رئیس شرکت متا
🔴
رئیس شرکت ویزا
🔴
رئیس شرکت اپل
🔴
رئیس شرکت تسلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119591" target="_blank">📅 23:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c8339b93.mp4?token=tLd1lw4TyZ1tKYG4IisI9gAkG2x2vXsC62WAofu9L14fdqBQtRbEiGiZcJY_as0p0PuB5HEmUKRugFJOZWUAI3c5snPZrcor2km_uTPlBeEtvff-Gn0WolJBsQ2jfev0KHg-yKu_eEWUcM5ECHL5DXP2hwziguse0K5zJhSF9dNy9vIwZSQTG1H65AYQ340T9e1JeM8UckjZUjr6szkkYy5wOAc7940BJRa5ITcb7alnzoo32LH5KEpKANOr0FmVS3mrjLHJTtKG6UT697AN25dWQpEnIief5OXcxN1kTWk2_wwQo9C161hS7B541gQrnvbQ2ysCVZeyqkvReBVscmJhwWsMXPgYIUp94A4usOBjGltiTL6QXqy-hXdCiCsAOiV4Finy8cyzDYzANkzmjLjMB2D6-ng9TK5U3TgXU8msrfnUQLoHSwvX-mYMD5FHyZSXOIATCamnWjVXIsBQrXBUETSG2PwfEFpSc4AX3ndz4RXNI7GgBs2gCFE-dwttcYvaTYVq2aNf1spzAN_o9VepBSk_SxDcdNgxBw13uiI-604nbHYBAyC5kOxDmfs1mao6m5H6saeCFFCmRvsA3exqWiDQla3j0ONLQmIQOZUvk_Xa01R_1gd_lF9kWnJhdLa67RoU5iynh-3M7n1GXrQ-zDPWYosCnXB4RReCqG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c8339b93.mp4?token=tLd1lw4TyZ1tKYG4IisI9gAkG2x2vXsC62WAofu9L14fdqBQtRbEiGiZcJY_as0p0PuB5HEmUKRugFJOZWUAI3c5snPZrcor2km_uTPlBeEtvff-Gn0WolJBsQ2jfev0KHg-yKu_eEWUcM5ECHL5DXP2hwziguse0K5zJhSF9dNy9vIwZSQTG1H65AYQ340T9e1JeM8UckjZUjr6szkkYy5wOAc7940BJRa5ITcb7alnzoo32LH5KEpKANOr0FmVS3mrjLHJTtKG6UT697AN25dWQpEnIief5OXcxN1kTWk2_wwQo9C161hS7B541gQrnvbQ2ysCVZeyqkvReBVscmJhwWsMXPgYIUp94A4usOBjGltiTL6QXqy-hXdCiCsAOiV4Finy8cyzDYzANkzmjLjMB2D6-ng9TK5U3TgXU8msrfnUQLoHSwvX-mYMD5FHyZSXOIATCamnWjVXIsBQrXBUETSG2PwfEFpSc4AX3ndz4RXNI7GgBs2gCFE-dwttcYvaTYVq2aNf1spzAN_o9VepBSk_SxDcdNgxBw13uiI-604nbHYBAyC5kOxDmfs1mao6m5H6saeCFFCmRvsA3exqWiDQla3j0ONLQmIQOZUvk_Xa01R_1gd_lF9kWnJhdLa67RoU5iynh-3M7n1GXrQ-zDPWYosCnXB4RReCqG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
هشدار یک شهروند معمولی ایتالیایی به ایرانیان:
🔴
اشتباه ما ایتالیایی‌ها در سال ۱۹۴۶ را تکرار نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/119590" target="_blank">📅 23:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSt9u3-LuFxsTfaFW4RmNV1yRfMmTXtIR6s49EyaiGn3u6poyWl1sl-UZt5VMLjtARxwml5fFjuNd7EOemCV4hzy9oaSHK5kymKpEPsM1kKSqkFNu73Bjew7F1jzMs4uEgbAHpbEeJLV3z21eP7_nZ08REW8Cb0zpBIvLePf5vAh_TwJnQV3q5jXHbcRMCP11YJH2NEqiZfIDmJ2Hf_b8UXsybb9TZ6I_uPAkK-fDdXBlijF5lHOWUnb_hBSXLx8a8du9tyBkN76DAS2IFL4BytRWR4alFMou-5KWCYCW549FgjwmZeKBDhyMiVwDnmxU63of6N9rp088oNJtOvFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: همراه اول به 4 میلیون نفر پیامک اینترنت پرو ارسال کرده اما تنها 450 هزار نفر آن را فعال کرده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/119589" target="_blank">📅 23:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/119588" target="_blank">📅 23:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر اقتصاد: به صورت ناشناس در تجمعات شرکت می‌کردم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119587" target="_blank">📅 23:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119586">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFXdtwenkzPjDTMf-8tMmdp6lrq-c6h5rWnKXDZ3cTpoQO0JZgkSRpWi70rIb7p6U_1j3iTz-BZokWsK1sR1IOrI4jN5h3CyTcuavOP6R8Zz290FXXJBT-gg3T2tfvpUg-gi2gVbYZp6XsVRfc0u_zxsHOzk4JNXUp7ZoZOsLsu4kz42nhsSgmXybyXCJRNDbnsNCDTw28fLKvEuysDLLe34-cySwkzTMYS-2bdxXyrQw3N4ho4N5Iu4kec9ocKHkN86i3EtX0DDlwCqP9nYYP9tVy-jr7oVDcKb7sEMz12nnHbrjEyjwmc5OS_2-zYnNw2t5SAzdL8769cU6BWrBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا دبیر: ۱۰ میلیون ایرانی خارج از کشور داریم که بیشترشان آدم حسابی‌‌اند/ ۵۰ هزار نفری که پلشت هستند و می‌رقصند، در خارج ول هستند
@AloSport</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119586" target="_blank">📅 23:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119585">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مارکو روبیو از جی‌دی ونس پیشی گرفت؛ پیشتازی در نظرسنجی ۲۰۲۸
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/119585" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119584">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فارس به نقل از منابع: ایران به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119584" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119583">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رویترز : مقامات ایرانی و غربی گفتند که عربستان سعودی، ایران را از این حملات مطلع کرده و سپس تماس‌های دیپلماتیک فشرده‌ای در کنار تهدیدهای عربستان مبنی بر تلافی بیشتر صورت گرفته است که منجر به تفاهم بین دو کشور در مورد کاهش تنش‌ها شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119583" target="_blank">📅 23:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119582">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9fca472b2.mp4?token=i9t9ecYsGcR8pl3vFb2MsizlYUfn8JFKE6wYQDG0KCvT0VAbGquDSX9yaAZFpkx3NsjfnB0kCHYtAVdhlUeM0hi2rXtx66LbpmlmMWVzi10TxwE3lbdp2ha3lSpiFwVOik1ltoXEkutpVbEuR6xErFwYIKCCSDv755RKSUlpJeGzCXRAvxw5FCHtVia9OKr3ufEQDNhuTYKAWv6vprJriTAGlH7zdssQ8VPO4iTNRQKjaZBUU_XCixn9UqowzPgbzEuWAoAy4g1Mq1Hpy2GFUUgI7a2YP7I13vvrvE20lY1y_s8rmp5r2vEiH_DRm0Clxizid9fro_pCpfjmI7gKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9fca472b2.mp4?token=i9t9ecYsGcR8pl3vFb2MsizlYUfn8JFKE6wYQDG0KCvT0VAbGquDSX9yaAZFpkx3NsjfnB0kCHYtAVdhlUeM0hi2rXtx66LbpmlmMWVzi10TxwE3lbdp2ha3lSpiFwVOik1ltoXEkutpVbEuR6xErFwYIKCCSDv755RKSUlpJeGzCXRAvxw5FCHtVia9OKr3ufEQDNhuTYKAWv6vprJriTAGlH7zdssQ8VPO4iTNRQKjaZBUU_XCixn9UqowzPgbzEuWAoAy4g1Mq1Hpy2GFUUgI7a2YP7I13vvrvE20lY1y_s8rmp5r2vEiH_DRm0Clxizid9fro_pCpfjmI7gKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ویدئوی دردناکی از مشهد، 18 دی. فلکه پارک
💔
جنازه .... جنازه .... جنازه .... اینجا هم جنازه .... همه جا جنازه ست.
🔴
این جوانان توسط حکومت تروریست جمهوری اسلامی و عوامل بسیجی و سپاهی با تیر مستقیم کشته شدن، نه توسط اسرائیل و آمریکا.
🤔
انتقام ما رو توی تاریخ مینویسند، شک نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/119582" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119581">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ادعای حسن ایوب خان، خبرنگار ARY News پاکستان: طبق اطلاعات من، لجستیک اداری و امنیتی هیئت معاون اول رئیس‌جمهور آمریکا، جی. دی. ونس، هنوز در پاکستان حضور دارد که نشانه آشکاری است از اینکه امیدها برای برگزاری دور دوم مذاکرات ایران و آمریکا در پاکستان همچنان زنده است.
🔴
با این حال، هنوز هیچ پیام رسمی از سوی هیچ یک از طرفین درباره ورود آنها به پاکستان برای گفت‌وگوها صادر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119581" target="_blank">📅 23:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119580">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر اقتصاد: افزایش‌ قیمت‌ها مقطعی و به دلیل آسیب دیدن بخشی از زنجیره تولید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/119580" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119579">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت دفاع کویت از دستگیری چهار نفری خبر داد که تلاش کردند با یک قایق ماهیگیری اجاره‌ای وارد کویت شوند.
🔴
وزارت کشور بعداً اعلام کرد مظنونان اعتراف کردند که به دستور سپاه پاسداران انقلاب اسلامی برای نفوذ به جزیره بوبیان و انجام عملیات خرابکارانه هدایت شده‌اند.…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/119579" target="_blank">📅 22:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119578">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر اقتصاد: برآورد خسارات منازل مسکونی آسیب‌دیده در جنگ درحال انجام است و برای تعمیر و بازسازی و لوازم خانه، منابعی توسط سازمان برنامه‌وبودجه در نظر گرفته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119578" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119577">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
طبق گزارش NBC News : ارتش ایالات متحده در نظر دارد در صورت فروپاشی آتش‌بس و تصمیم ترامپ برای از سرگیری عملیات‌های عمده رزمی، نام درگیری خود با ایران را به عملیات چکش سنگین تغییر دهد و این جایگزین نام قبلی عملیات خشم حماسی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119577" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119576">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57db4a6aa.mp4?token=XGaulrhar7koRsVif-PCFZ1e-JXV1dQjLs5Sy9WDLskIygVscxkNTDuK-t-Ez8NDJ8u7ROnHC_6jCPwyGNB8CyeGikHYxvXH4FYl7IhrflkmO42cBPYd5Pzyf0WlW275pZ6szr1GoujTyOlJnoss_KMQNJJ_iY_RVKBHJOmhZIL1VhwcI2Wpf10owWgtthd5Z_7mQ1mP1K2sLNGYPasgNS3Gx5-AYqbcP3dg0jaxB2HY1SmT8C9y2IBg0jDU8RpTx1XEjdUQDvpE3PmChiTAcVFaPw_EhKHSag39XQodJB8pMsrPthHeHjxD5aN8_oi5tMaCyD1Ts8qZ4SXFtgw9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57db4a6aa.mp4?token=XGaulrhar7koRsVif-PCFZ1e-JXV1dQjLs5Sy9WDLskIygVscxkNTDuK-t-Ez8NDJ8u7ROnHC_6jCPwyGNB8CyeGikHYxvXH4FYl7IhrflkmO42cBPYd5Pzyf0WlW275pZ6szr1GoujTyOlJnoss_KMQNJJ_iY_RVKBHJOmhZIL1VhwcI2Wpf10owWgtthd5Z_7mQ1mP1K2sLNGYPasgNS3Gx5-AYqbcP3dg0jaxB2HY1SmT8C9y2IBg0jDU8RpTx1XEjdUQDvpE3PmChiTAcVFaPw_EhKHSag39XQodJB8pMsrPthHeHjxD5aN8_oi5tMaCyD1Ts8qZ4SXFtgw9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۲۲ اردیبهشت، زادروز مریم میرزاخانی، به عنوان روز جهانی زنان در ریاضیات شناخته می‌شود؛ ریاضیدان ایرانی‌ای که نامش برای همیشه در تاریخ علم ماندگار شد.
🔴
میرزاخانی در سال ۱۳۷۳ مدال طلای المپیاد ریاضی ایران و در سال ۱۹۹۴مدال طلای المپیاد جهانی ریاضی در هنگ‌کنگ را کسب کرد. یک سال بعد، در ۱۹۹۵، دوباره طلای جهانی گرفت و با کسب نمره کامل، نامش را در تاریخ المپیادها ثبت کرد.
🔴
او پس از تحصیل در دانشگاه صنعتی شریف، برای ادامه تحصیل به آمریکا رفت و دکترای خود را از دانشگاه هاروارد گرفت. مریم بعدها استاد دانشگاه استنفورد شد و در سال ۲۰۱۴ به عنوان نخستین زن تاریخ، مدال فیلدز، معتبرترین جایزه دنیای ریاضیات، را دریافت کرد.
🔴
داستان او فقط درباره ریاضی نیست؛ درباره کنجکاوی، پشتکار و شکستن مرزهایی‌ست که غیرممکن به نظر می‌رسیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119576" target="_blank">📅 22:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119575">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUSQ8GtwiZsEPQYTX28sKkB5lrXrvfSMaYgWEymGbBb0GDCo98a18YgburSCufsqaRjHzl-WKVkioYUmHSZTTYXTUJwBAAjsvsRRFAgMEolSRvC9WuS-MbmzG34Gc1fRNF6MwRxSD-c3g7QItZPy18XwYvrUd0eRXH8LHK2OlssWwOOflpcFGpa0ult3nJDH4dqD9J7vn6BmXFSx3l8YJO5vh6GyqcxKYXhs_MUvLafMgKzxxxzQikMGGdT4QthrqqgCKLd05j99aDa7xKe0yD08QgCpw_E4tqCE27G7kP2JFgCwV1-q6B14_yxx_PGTHe-ap53vCSD5-UY4xc27UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر بودجه کنگره تخمین می‌زند که سیستم دفاع موشکی ملی «گلدن دوم» حدود ۱.۲ تریلیون دلار طی ۲۰ سال برای توسعه، استقرار و عملیات هزینه خواهد داشت.
🔴
بیش از ۱ تریلیون دلار از هزینه پیش‌بینی شده صرفاً از خرید و توسعه خواهد بود، در حالی که لایه رهگیر مبتنی بر فضا تقریباً ۷۰٪ از هزینه‌های خرید و ۶۰٪ از کل هزینه‌ها را تشکیل می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/119575" target="_blank">📅 22:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119574">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd76a55e0.mp4?token=TDEKqQ7g7KdyLX3xHhx3IhK42rfeHz3owIauspt0SlEaWvcF306z-mtQb4Puw88NH8AwLksW_TM48oIw8ByZQOtOMoCjjMeEcizwXkjhuruSA0946H5oo5aPqawV7LUSiILO6Lo04uUB1Jsz0O-kAgTpezh3bclvcemVQNyVgEe3ChiX5ncv9nL6Sd0lHJhJlFKq1BDIYHdG6IMk3-HSxtMXazOJrpMct0XblkZglccT8ttVmqQlSlxc-nneWYbWqnEj7BLfeDlPLdVl8VL9fwK2ERjFduz5KSLbKAXQAdvg53VD4SGOkAOimAIBdU92uPQ-WLGCUE2cnPjYheJnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd76a55e0.mp4?token=TDEKqQ7g7KdyLX3xHhx3IhK42rfeHz3owIauspt0SlEaWvcF306z-mtQb4Puw88NH8AwLksW_TM48oIw8ByZQOtOMoCjjMeEcizwXkjhuruSA0946H5oo5aPqawV7LUSiILO6Lo04uUB1Jsz0O-kAgTpezh3bclvcemVQNyVgEe3ChiX5ncv9nL6Sd0lHJhJlFKq1BDIYHdG6IMk3-HSxtMXazOJrpMct0XblkZglccT8ttVmqQlSlxc-nneWYbWqnEj7BLfeDlPLdVl8VL9fwK2ERjFduz5KSLbKAXQAdvg53VD4SGOkAOimAIBdU92uPQ-WLGCUE2cnPjYheJnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیش در روزهای آتش بس
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/119574" target="_blank">📅 22:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119573">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
⭕️
حجم 1 تا 100 گیگ
بدون ضریب با لینک ساب بدون قطعی سرعت بالا  و ضمانت بازگشت وجه
قیمت هر گیگ 235
💸
برای خرید به ادمین چنل پیام بدید
خرید آسان و راحت با کارت ب کارت
ثبت سفارش از طریق ربات:
و اگر تمایل به همکاری دارید کافیه به ساپورت چنل مراجعه کنید
🙏
❤️
@CHERNOBILNETBOT
❤️
@CHERNOBILNETT</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/119573" target="_blank">📅 22:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119572">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
عراقچی: برای آرام کردن ترامپ امتیاز نخواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/119572" target="_blank">📅 22:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119571">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPIyumYedhQjzuypVZA3QEBNKQbbJeEVyoU4vAHvcJ9rTpFHNK0tg5swlpdvWhRs6_hFNsFNXRJbFnPMtU8qHg-8T5ccyzWgywEpJq61KVZcXEH-FA2mwIvxtSmrDt9oucrwAoqtZz8qAsEzKUlWZKI403FiTpA-QXV3XcljBISj4nWUP3gw-zrI5Qy0TOdpKGjvqfFlFdy3O7LKTG4yrqFEOc2EDIVtjybJe9qpPTH1uljo_5oUj3ZNzmj7OH3cf6-0VWAz08yRR4rTuO0IdAoaiDLlGiuVbH_AKb-XZCirPPH36X8usuazP5--tt9xgztGlyuztaeHPcBbw_22IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۸.۱ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119571" target="_blank">📅 22:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119570">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز: یکی از مقامات وزارت نفت عراق گفت که ایران از عراق خواسته است برای هر تانکر، مدارکی ارائه کند تا ترانزیت از طریق مسیرهای دریایی تعیین‌شده تحت نظارت نیروهای دریایی خود تسهیل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119570" target="_blank">📅 22:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119569">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: دو تانکر حامل ال‌ان‌جی قطر، به دنبال توافق دوجانبه جداگانه بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/119569" target="_blank">📅 22:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119568">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رویترز: ایران از مسدود کردن تنگه هرمز به کنترل دسترسی به آن تغییر موضع داده است. هرمز دیگر یک مسیر ترانزیتی خنثی نیست، بلکه یک کریدور تحت کنترل است
🔴
در قراردادی میان بغداد و تهران که قبلاً گزارش نشده بود، عراق عبور امن برای دو ابرتانکر نفت‌کش را که روز یکشنبه از تنگه عبور کردند، تضمین کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119568" target="_blank">📅 22:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119567">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دختر اکبر عبدی: پدرم دچار سکته قلبی شده است/ وضعیت ترخیص مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/119567" target="_blank">📅 22:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119566">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رویترز به نقل از منابع آگاه: عراق و پاکستان با ایران توافقاتی برای اجازه ارسال نفت و گاز مایع از خلیج فارس منعقد کرده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119566" target="_blank">📅 22:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119565">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ امریکا رو به مقصد چین ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119565" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119564">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: عربستان سعودی در جریان جنگ، یک سری حملات تلافی‌جویانه بدون اطلاع‌رسانی علیه ایران انجام داده است،ارزیابی می‌شود که این حملات در اواخر مارس انجام شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119564" target="_blank">📅 22:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119563">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dceb5719b.mp4?token=N8YnIg_mfwDrxmnSh-u_9sjO_OeNGCGYB0qUvJe-FKfOHBrxkQjTz81l46LMyg3UZG-JoaLB2n7d29UP1zWx3UfZl3ybfRvueIRczqrp6Z4R7ynHrtIE_90Vi2vl1lcZHQd-mi3c5U-Ojv1ugsCAc5m5puN7WcPa8SxZAXb4yn9JiLOV55Akv_rCggg6OtDNZZKotMFdMex9YQ5L_7r99ZmW6DA_kDqeyqvPInd67DWK9_AnbIB8TImxak2SnietoohxxFcdKgaubSjGIbTb6HgNv0tjLIYAeZ0g7zfzMO4VTg_XpQDV-28ypxGkGhxvjQRSZIw4cN0ahDaW10RfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dceb5719b.mp4?token=N8YnIg_mfwDrxmnSh-u_9sjO_OeNGCGYB0qUvJe-FKfOHBrxkQjTz81l46LMyg3UZG-JoaLB2n7d29UP1zWx3UfZl3ybfRvueIRczqrp6Z4R7ynHrtIE_90Vi2vl1lcZHQd-mi3c5U-Ojv1ugsCAc5m5puN7WcPa8SxZAXb4yn9JiLOV55Akv_rCggg6OtDNZZKotMFdMex9YQ5L_7r99ZmW6DA_kDqeyqvPInd67DWK9_AnbIB8TImxak2SnietoohxxFcdKgaubSjGIbTb6HgNv0tjLIYAeZ0g7zfzMO4VTg_XpQDV-28ypxGkGhxvjQRSZIw4cN0ahDaW10RfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما داریم یک سالن بزرگ می‌سازیم که هزینه‌اش از بودجه تعیین‌شده کمتر شده. همین‌جا ساخته می‌شود. من اندازه‌اش را دو برابر کردم چون مشخصاً به آن نیاز داریم.
🔴
خبرنگار: ولی هزینه‌اش هم دو برابر شده.
🔴
ترامپ جواب داد: چون من اندازه‌اش را دو برابر کردم، آدم احمق. تو آدم باهوشی نیستی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/119563" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119562">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: عربستان سعودی در جریان جنگ، یک سری حملات تلافی‌جویانه بدون اطلاع‌رسانی علیه ایران انجام داده است،ارزیابی می‌شود که این حملات در اواخر مارس انجام شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119562" target="_blank">📅 22:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119561">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فارس با تایید پیش شرط های ایران؛ به نقل از یک منبع آگاه گزارش داد:  ایران به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/119561" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119560">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: شما دوران طلایی آمریکا را زمانی خواهید دید که این جنگ به پایان برسد، و شما اکنون آن را می‌بینید
🔴
من به وضعیت مالی آمریکایی‌ها فکر نمی‌کنم. به هیچ‌کس فکر نمی‌کنم.
🔴
فقط به یک چیز فکر می‌کنم: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. همین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119560" target="_blank">📅 21:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119559">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرنگار به ترامپ : آیا بین شما و پوتین درک متقابلی وجود دارد که روسیه باید کل دونباس را به دست آورد؟
🔴
ترامپ: خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119559" target="_blank">📅 21:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119558">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
زمین لرزه ۳.۴ ریشتری پردیس تهران را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119558" target="_blank">📅 21:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119557">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ درباره نفت : قراره یه فوران نفتی داشته باشید، چیزی که تا حالا ندیدید
🔴
من فکر می‌کردم خیلی بیشتر بالا بره،ما انتظار داشتیم قیمت نفت خیلی بالاتر بره
🔴
هر کاری لازم باشه انجام می‌دم، من هشت تا جنگ رو تموم کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119557" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119556">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: ما و چین، دو ابرقدرت جهان هستی
🔴
ترامپ درباره ایران: ما یا یه توافق می‌کنیم، یا اونا نابود می‌شن - به هر حال ما برنده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119556" target="_blank">📅 21:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/119555" target="_blank">📅 21:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/alonews/119553" target="_blank">📅 21:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
هم اکنون طوفان شدید در تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/119552" target="_blank">📅 21:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93485c07a.mp4?token=luh9RVvO4MKY4EH9vmR1ULCShSZFUmSGaupk5LfXWYc4ufMok2b6iDaO8xQPg2NF61tkQyvXd093w1G18tcfp1keR7CKH75VITgrKG-le-oH6hAjlSWIs5rlFUWFLRYkUd1Xgz4_nbYHoXzElgy3joY9EHuSPPJxIb0Q-1xqEvxz-jZ2-nBk2r1Qs5LiWG9pUHQ3lLzgKSRz3D2T5hkCNz48rMHUa_HXq_ijEd0hQC8DObujbdvrUCxWWsKWA_OV2oq1AcApG7Sk1-U8s93OMu59_Wdj6owFzpk1t3msBDHiMVcIhFJs9aYAoFRV7ylqeXrk_7O10hYTrR-QZUC19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93485c07a.mp4?token=luh9RVvO4MKY4EH9vmR1ULCShSZFUmSGaupk5LfXWYc4ufMok2b6iDaO8xQPg2NF61tkQyvXd093w1G18tcfp1keR7CKH75VITgrKG-le-oH6hAjlSWIs5rlFUWFLRYkUd1Xgz4_nbYHoXzElgy3joY9EHuSPPJxIb0Q-1xqEvxz-jZ2-nBk2r1Qs5LiWG9pUHQ3lLzgKSRz3D2T5hkCNz48rMHUa_HXq_ijEd0hQC8DObujbdvrUCxWWsKWA_OV2oq1AcApG7Sk1-U8s93OMu59_Wdj6owFzpk1t3msBDHiMVcIhFJs9aYAoFRV7ylqeXrk_7O10hYTrR-QZUC19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : از پاکستان به‌عنوان میانجی تو ماجرای ایران حمایت می‌کنم و معتقدم میشه به یه توافق خوب رسید
🔴
این قضیه هم برای مردم آمریکا خوبه، هم برای ایرانی‌ها، پاکستانی‌ آدمای خوبی‌ان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119550" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119549" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119548">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: فکر نمی‌کنم در مورد ایران به کمک نیاز داشته باشیم و به هر طریقی چه مسالمت‌آمیز و چه به شکلی دیگر پیروز خواهیم شد
🔴
یا ایران کار درست را انجام می دهد یا کار را تمام می کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/119548" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119547">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: با ایران یک توافق خوب منعقد خواهیم کرد
🔴
ارتش ایران را حذف کردیم
🔴
ماشین جنگی ایران از بین رفته است
🔴
گفتگوی طولانی با رئیس جمهور چین درباره جنگ ایران خواهم داشت
🔴
کسی که می‌خواهد به دیوانه‌های ایران اجازه دهد به سلاح هسته‌ای دست پیدا کنند، احمق است
🔴
نمی‌توان اجازه داد ایران به سلاح هسته‌ای دست یابد و این را می‌داند و ما بازی نمی‌کنیم
🔴
فکر نمی‌کنم در مورد ایران به کمک رئیس‌جمهور چین نیاز داشته باشیم
🔴
خواهیم دید در مورد ایران چه اتفاقی می افتد و فقط به دنبال انعقاد یک توافق خوب هستیم
🔴
ناتو من را ناامید کرده است و نیازی به کمک آن نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119547" target="_blank">📅 21:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119546">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ در پاسخ به این سؤال که آیا آمریکا برای حل مسئله ایران به کمک چین نیاز دارد:
🔴
«نه، فکر نمی‌کنم به هیچ کمکی برای مسئله ایران نیاز داشته باشیم. به هر طریقی که شده، پیروز خواهیم شد. چه مسالمت‌آمیز باشد، چه غیر از آن!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119546" target="_blank">📅 21:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119545">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967e54149f.mp4?token=a91BMjGBQaYqMg2Gwv-QMy6loBGf9qVzqx6ORuiDMUdvJE6036OuBbomEclWxNTRHUvWQHoKrxVPSJ0hUtCFlzCV9yp4X-dPHo-S4T9_vSqWn5btZxewy9BsPZHUxq8xhXFKT2LFiwoBz3746YHmAJK5nT3I9Wm0Xpf2TR4F5epgMMfyCKXP_cBq79RZ4f9YcOnUfTNZ5kCKyFL2tMSyIVKYslXI49ps02A6WrUnLuQBoqzYwjrbZs7dA5UgbcTEWDE27pEgwf0yqd6Na7aD0KY9vpPaE9yiqvTGjdILZDUerdwKc9uq0ldvCJ7EFmab4LY14RfBAHj6f9hBlTJ7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967e54149f.mp4?token=a91BMjGBQaYqMg2Gwv-QMy6loBGf9qVzqx6ORuiDMUdvJE6036OuBbomEclWxNTRHUvWQHoKrxVPSJ0hUtCFlzCV9yp4X-dPHo-S4T9_vSqWn5btZxewy9BsPZHUxq8xhXFKT2LFiwoBz3746YHmAJK5nT3I9Wm0Xpf2TR4F5epgMMfyCKXP_cBq79RZ4f9YcOnUfTNZ5kCKyFL2tMSyIVKYslXI49ps02A6WrUnLuQBoqzYwjrbZs7dA5UgbcTEWDE27pEgwf0yqd6Na7aD0KY9vpPaE9yiqvTGjdILZDUerdwKc9uq0ldvCJ7EFmab4LY14RfBAHj6f9hBlTJ7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، از کاخ سفید خارج شد تا به چین سفر کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/119545" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119544">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پاپ لئو چهاردهم: مسیحیان و مسلمانان، بی‌تفاوتی را به همبستگی تبدیل کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119544" target="_blank">📅 21:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سفیر ایران در چین: آمریکا نمی‌تواند مواضع چین درباره ایران را تغییر دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/119543" target="_blank">📅 21:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a082533c19.mp4?token=PwAOWOAvX-FcHkEg6Bj02h6WlDg7HSIUhg60CsZkv7uwzcBg74r0dZHqLt2x9zQlRIcYvgcSGxbtov-AFcn_qzOWPN2sBwSSXPX12p9VE39rxzU3OtMfTIT0zJdOYhD_eKzj7J--IrNkqD8uJ_sdkM3zghhfjedKbyvti19N27WO0DplC65fWeZ-1NJXnwhxJ6PeD2HaeqbHz3NUrtIoeUZ0xIlhmjYWPK99B-OrAZjvebt5YYuPBniv8y6_g1BuhwpIOvUfr7A8x0hwc9C_EPYBxOifoX1GrJkIjrp9B3cvYASWjWlQAlKdmJUqj_4rxQrmGkSXYwai1ktAqCYRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a082533c19.mp4?token=PwAOWOAvX-FcHkEg6Bj02h6WlDg7HSIUhg60CsZkv7uwzcBg74r0dZHqLt2x9zQlRIcYvgcSGxbtov-AFcn_qzOWPN2sBwSSXPX12p9VE39rxzU3OtMfTIT0zJdOYhD_eKzj7J--IrNkqD8uJ_sdkM3zghhfjedKbyvti19N27WO0DplC65fWeZ-1NJXnwhxJ6PeD2HaeqbHz3NUrtIoeUZ0xIlhmjYWPK99B-OrAZjvebt5YYuPBniv8y6_g1BuhwpIOvUfr7A8x0hwc9C_EPYBxOifoX1GrJkIjrp9B3cvYASWjWlQAlKdmJUqj_4rxQrmGkSXYwai1ktAqCYRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم کارشناس ارشد صداوسیما:
این دفعه جنگ بشه اصلا مهم نیست ساختمون اینتل تو اسرائیل چند طبقه زیر زمینه، کل دیتاسنترهای اینتل میخوره، پروژه مشترک گوگل و آمازونم که میخوره، بقیشم هرچی هست میخوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119542" target="_blank">📅 21:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت دفاع عراق: هیچ‌گونه فعالیت یا تأسیسات نظامی ناشناس در صحرای نجف وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119541" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v96liZJ1P7GqiUH6smVa23HRxzsa_20aH_tm9mjP8fGkT5qbtCECxxJaljQe7_gs_YN737F1xvcG0NUqYClJcjKoUNMvjK4HVTEwOW3441Uf5oY27_JpJ4KPZDioOLruuclo9FKn2wApGSwd9Z6QiAlZu5sj7YMb93dgG8a5r2Tv4bpZ5hyBa-Ez_JN6clAFIwh2fEwgTR6JfYi9TPbDWwmWYiTouWkj832Kvkv_cLWbSebB0RnElrsItdj3CPMF03fnOAMmgUPMmsKW1Ktf_PeH6WkwQR1lZo0-EO79Jw0C3z4e4Bd-m4QJf4nQhS6r0-d9UahPemG3W3FVu7Xe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد یک فروند نفتکش ایرانی در ۱۰ می در جزیره خارک در حال بارگیری نفت ایران بوده است که نشان از تداوم بارگیری نفت خام در جزیره خارک دارد.این نفتکش بدون مشکل بارگیری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/119540" target="_blank">📅 20:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کاظم غریب‌آبادی، معاون وزیر خارجه، در شبکه ایکس نوشت: صلح واقعی با ادبیات تحقیر، تهدید و امتیازگیری اجباری ساخته نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/119539" target="_blank">📅 20:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119538">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a55fa18e5.mp4?token=pV4AJr6GHJ2Usx4hizbVgHJSv1ruobt38es50-8qu3mf0K4tT4ccEROL7Jem-04RH69Gp_Tk3CevUFdHGY_qDnZ_4eeq8uoWaUi4b2xeOk0BUOJHgJLF_GQiQ1oLUPyLnlAMR3iXDi1XWIFXRl7rxKU_--XOaO4TDuHRXUudDK18lJWjd3-t7xKhc79JRRnmF-B6Z4z1PJAV7lwUXYOWUExIn92gn_F34--uA-m3_u-jkXBchKUbGRAeMswScHtLOlt58bB46dnfF2HSfsKh6mQUl-vXOPDODnuWlFthPNjGVJLyAa8tSV7RQMCqnx4GNxA1m4hoqNHVHgNIdor12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a55fa18e5.mp4?token=pV4AJr6GHJ2Usx4hizbVgHJSv1ruobt38es50-8qu3mf0K4tT4ccEROL7Jem-04RH69Gp_Tk3CevUFdHGY_qDnZ_4eeq8uoWaUi4b2xeOk0BUOJHgJLF_GQiQ1oLUPyLnlAMR3iXDi1XWIFXRl7rxKU_--XOaO4TDuHRXUudDK18lJWjd3-t7xKhc79JRRnmF-B6Z4z1PJAV7lwUXYOWUExIn92gn_F34--uA-m3_u-jkXBchKUbGRAeMswScHtLOlt58bB46dnfF2HSfsKh6mQUl-vXOPDODnuWlFthPNjGVJLyAa8tSV7RQMCqnx4GNxA1m4hoqNHVHgNIdor12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع روسیه فیلمی منتشر کرده است که آزمایش موفقیت‌آمیز سامانه موشکی جدید هسته‌ای‌پرتاب روسیه به نام «سرمات» را نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119538" target="_blank">📅 20:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119537">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بلومبرگ: نیروگاه اصلی گاز طبیعی که سوخت مورد نیاز امارات متحده عربی را تأمین می‌کند، سال آینده به ظرفیت کامل بازخواهد گشت که این موضوع نشان‌دهنده زمان طولانی بازیابی برای برخی از حیاتی‌ترین زیرساخت‌های منطقه در پی جنگ اخیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/119537" target="_blank">📅 20:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119536">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بیانیه دولت بریتانیا: ما پهپادها، جت‌های جنگنده و یک ناو جنگی را به ماموریت چندملیتی برای تأمین امنیت تنگه هرمز اعزام خواهیم کرد
🔴
کمک ما شامل تجهیزات مین‌یاب خودکار، جت‌های جنگنده تایفون و یک کشتی جنگی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/119536" target="_blank">📅 20:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119535">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سی‌ان‌ان : کشتی روسی حامل راکتورهای هسته‌ای زیردریایی به کره شمالی تو شرایط مرموزی غرق شده !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/119535" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119534">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: رهبر ایران ۵ شرط را برای آمریکا پیش از ورود به مذاکره در مورد بحث هسته ای تعیین کرده است:
🔴
پایان دادن به جنگ در همه جبهه‌ها
🔴
رفع همه تحریم‌ها
🔴
آزادسازی دارایی‌های مسدود شده
🔴
جبران خسارات و زیان‌های جنگ
🔴
به رسمیت شناختن حق حاکمیت ایران بر تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/119534" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119533">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بلومبرگ: امارات دو بار با هماهنگی اسرائیل به ایران حمله کرده؛ یک‌بار به یک تأسیسات پتروشیمی در عسلویه و بار دیگر به پالایشگاهی در جزیره لاوان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/119533" target="_blank">📅 20:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119532">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtrX_O11nwMi6lPBsVgzEuAqtjCF87S4QceOxFGvjGh7ROk8MGTiVbpp43EKWnUNnOBkvIc8Zxd-OuNN-UTNwXdVrzkfbpCHYGTftHnl7kTzOa85aAtH6AgdCAQWakb8EmBFCwyPf3x3MdSZD01xvCoFBviaJ7tv0LsiPodb13vejvaMzmP2YFvao1rQxKF458mYNo9LgC_j0Il8LEcXePDq1fegLsVPrxEeq4Es_qEobo9Fny28yhNbDPj72OY2UjDcrqUfLI2hH4RYs4LwiOHwDBprVBqYpio4HNK6Dcsj39XSwz60NhJXFT5CUblz76iwZKosgtuWjCyiQL91hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش WSJ، گوگل در حال مذاکره با اسپیس‌ایکس برای توافق پرتاب موشک است که به برنامه‌های گوگل برای توسعه مراکز داده مداری در فضا مرتبط است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/119532" target="_blank">📅 20:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119531">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e268bcda1.mp4?token=KhWvskJ8Bh-Bd9CsIJYqsDG-ycVwdhlSpjq2Uee9iPA2n9qEkdchaJxufB15FSDtKkDG39MZRbVZLZoW9qxVwUeYCfkiaQeeaf5l-d6_1x3enHr77SAqmu7MWX87abZUvYpjNOBxwCAoeH9kQdFgP36dP7UzUCx_wzsXI_6k0jAf01pG-oru1uxRJsbW7E7hQF2LIm_MK33U_DZCRT-dYwHLR7sjjWGc8y3xSC4lHIIG5bcgu57msGW_zkwgT3hGPC4OOiXaiObWw2OS-RBA7wRxWkAwugcLIhtUXFJfntAER-DweJQsI0-4w8P-njwOh6Wu9ynwljc94l2q21jh-iG8QDvf9bTzH3SoL-AWDexge2t_nGuNcRJfhVwZwfvqbBDu_Azk6M7UW5sJ3LHKajDA4YoVYbLHzxFSAqgfJW56Z4bF0GfJcYX7JdXLn-qZzDX3X9CV799R9nwAdicLkt2sce9ZxbX4E6fNmU0B6OzmicUJTPp0SMzmd-gQsBSA9aq0GaiErXnDuctNqXBzY477E8kcCVgzbZ8f7iozJqdr8WvUQnhD4kXoFk8fU0hBIEYhe1qhU-Kz7mskm9QwRAAzBziHatCv5a3kqz32_NTPRCnWeFhNTaTHfiTo5m-NREhWZtyNdmT5gmGkONEWz3Rizhf7a_XTsQyQwa6Alz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e268bcda1.mp4?token=KhWvskJ8Bh-Bd9CsIJYqsDG-ycVwdhlSpjq2Uee9iPA2n9qEkdchaJxufB15FSDtKkDG39MZRbVZLZoW9qxVwUeYCfkiaQeeaf5l-d6_1x3enHr77SAqmu7MWX87abZUvYpjNOBxwCAoeH9kQdFgP36dP7UzUCx_wzsXI_6k0jAf01pG-oru1uxRJsbW7E7hQF2LIm_MK33U_DZCRT-dYwHLR7sjjWGc8y3xSC4lHIIG5bcgu57msGW_zkwgT3hGPC4OOiXaiObWw2OS-RBA7wRxWkAwugcLIhtUXFJfntAER-DweJQsI0-4w8P-njwOh6Wu9ynwljc94l2q21jh-iG8QDvf9bTzH3SoL-AWDexge2t_nGuNcRJfhVwZwfvqbBDu_Azk6M7UW5sJ3LHKajDA4YoVYbLHzxFSAqgfJW56Z4bF0GfJcYX7JdXLn-qZzDX3X9CV799R9nwAdicLkt2sce9ZxbX4E6fNmU0B6OzmicUJTPp0SMzmd-gQsBSA9aq0GaiErXnDuctNqXBzY477E8kcCVgzbZ8f7iozJqdr8WvUQnhD4kXoFk8fU0hBIEYhe1qhU-Kz7mskm9QwRAAzBziHatCv5a3kqz32_NTPRCnWeFhNTaTHfiTo5m-NREhWZtyNdmT5gmGkONEWz3Rizhf7a_XTsQyQwa6Alz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام: اگر میانجی (پاکستان) اجازه می‌دهد هواپیماهای شناسایی در پایگاه‌های هوایی پاکستان پارک شوند، فکر می‌کنید این با نقش میانجی منصفانه سازگار است؟
🔴
وزیر جنگ هگستث: من نمی‌خواهم وسط این مذاکرات قرار بگیرم.
🔴
سناتور گراهام: خب، من می‌خواهم وسط این مذاکرات قرار بگیرم. من به پاکستان به اندازه‌ای که بتوانم آنها را پرتاب کنم اعتماد ندارم.
🔴
اگر واقعاً هواپیماهای ایرانی در پایگاه‌های پاکستانی برای محافظت از دارایی‌های نظامی ایران پارک شده‌اند، این به من می‌گوید که شاید باید به دنبال شخص دیگری برای میانجیگری باشیم. جای تعجب نیست که این لعنتی به جایی نمی‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/119531" target="_blank">📅 20:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f3fcd3b9.mp4?token=Hh4W3mDuEiS5imBR4m_C2loKKpDjNvjkRlmGtm8htw-qiKapWzqW_vuu80v2M5-r_XL9PP96SzEnqNm3pgunMBSBFv7MG06aHHPRLjyB3lmbCoQe27KLPtnTXTgSrefjFt8Cs82fPz2f4SF5qlbg2W8_YmF-bDzyLbB3948ZaZS9hHrSA70KzaBkcZYxaFswvT3WZM_rk0c35V5S2gQEVMUv4ebHgdTTiCqJKlhh-bX-K2H3AdKUrsj37ifSiHFBgKeKpFM8-OgYHjdcMJrSyb4f1WTdKUI8Uau9DqOqvi4QXeScDTXPcV5OhC5TERbJ-NJ-A4JEW54eBr6Xv_5yYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f3fcd3b9.mp4?token=Hh4W3mDuEiS5imBR4m_C2loKKpDjNvjkRlmGtm8htw-qiKapWzqW_vuu80v2M5-r_XL9PP96SzEnqNm3pgunMBSBFv7MG06aHHPRLjyB3lmbCoQe27KLPtnTXTgSrefjFt8Cs82fPz2f4SF5qlbg2W8_YmF-bDzyLbB3948ZaZS9hHrSA70KzaBkcZYxaFswvT3WZM_rk0c35V5S2gQEVMUv4ebHgdTTiCqJKlhh-bX-K2H3AdKUrsj37ifSiHFBgKeKpFM8-OgYHjdcMJrSyb4f1WTdKUI8Uau9DqOqvi4QXeScDTXPcV5OhC5TERbJ-NJ-A4JEW54eBr6Xv_5yYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازان روسی در حال استفاده از پهپاد رهگیر «یولکا» (Yolka) علیه پهپادهای اوکراینی هستند که براحتی با لانچر بسیار کوچک دستی به سرعت پرتاب میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/119529" target="_blank">📅 20:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت انرژی آمریکا ادعا کرد تصور می‌کند که تنگه هرمز تا اواخر ماه مه میلادی (۱۹ روز دیگر) بسته خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/119528" target="_blank">📅 20:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / سی‌ان‌ان: ترامپ جدی‌تر از گذشته به از سرگیری جنگ فکر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/119527" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
