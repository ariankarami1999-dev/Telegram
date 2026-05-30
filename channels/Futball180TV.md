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
<img src="https://cdn4.telesco.pe/file/sji9SiE5wsGTNeelQ8Q9JKA8Gc6TOrFE67U7HIX51fofm727SMgGXIV3lcWkDdxdIikfDytfHPeW7cZKWzzPrbcXUfnvSImc5J5Dz9ucey-flJygwz1IMVmznAGp5FomtgXUX7c4lfHqatvzAVwSamE0w8VlSrtPCUMZQbosOg2bb8fRWM1AhbQ9tCoJpCvWVJsuQUGTGU3Wj0O8q-0Ps7K9XtqYOohqqt-ll7VjD5cx48v1Fu-OB2C87njGKjagSdB1E5fVO7f-Tc0qnlspm61-VgxkqV9kUu3qhuLnu1j868j0BAQ6wu-HtwMuYpgTrfdim0KJlQX8ZDBTayd33A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 127K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 13:51:29</div>
<hr>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emVepJW_-MOMj9nLIMT0M4lCkhcp4YgYEdbDlbdVQrb-XinC0UZDy3-4On4nUCEDdKVilX9qDgoZnvwWACw6xX9GuFJAOQ_mBUxb0OaFSWlZcDjDyCXobWqWTTUSG0glCRoT1DMRpjdTIj9Ujb8ukRUNUkYz_dFFmygc3RiEJ0789wq-HQt0O50MmGs7CZM4A5f7P5k2di7oEj2YWr3T4oJBpGC3egAbPJpN0H2FT2-QFlj_sWg34zo1PPOw4JeD6eI9NEsZbyBw3Z4H4nZkiJRysLVRUcyXZNmQ8yJNA2ofHy8Ca3sS5hTA8RCa6FV_F1VJcjAs5EINPWyOfKaw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇪🇸
آخرین شایعات نقل‌وانتقالات بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/90459" target="_blank">📅 13:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🔵
با حکم دادگاه تجدیدنظر، شکایت شرکت امین‌سیمای کیش از باشگاه استقلال برای دریافت غرامت ۳۸۰ میلیارد تومانی مردود و آبی‌ها تبرئه شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/90458" target="_blank">📅 13:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180
؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار دقیق و کاملی ارائه خواهیم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/90457" target="_blank">📅 13:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUJ350gLc9KtttlunSphgIKhqPM9uGz9fa3RTL2qm5prncOUfh2pfU7Wjm2WlStNq57plL3l_FNlBREXsHemA-8zl9AUalwLUKBkpFvPNfNCtEEyVXmBXnehCF8c_k8gzAA-65ZH2reKpaVV-1bCsAJ_T5fGi1DuZiPrSrMQIV9PmyvHk9uMyB75P4KvJ0KhBHYUzx8--XRx1kTWJh7yLZtH2QlQPNJu6XT4hKxi7sEPF4X7gGdzhD4rlVmP8Is52GHzNnZl7jOfRRlLG5H9L4UzAhSdwx-5G5__tirraMDhwbKGc1hJAc0J-BBTtjMNuNHBDlob7C2IMnRR61_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید چلسی خواستار جذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن را غیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/90456" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh2tiXxgvLjPmWKYQmRCFC5oH63Lv4BQryCMl_SeG4jpP6cJuatFNn3cZd11HUXEkXPFiXnRbBNXuaNgRwa29x86Y6V8fiFoLj9rZV1R0AxenDJC9dGvFmj-pd_ZqRC_7YabKJ0AJRnBE6UM5RugfU4ZlDUNQNxpIpKhsaL_WChCN_Knhr3FpkRzk8KXhYXjV29Tg4BChyMG43q4L9hNWcZlLxrDIHs2H7s1IcDcvncYBqGtwzs4JJP4572XkDeyvv050HH5X6mHW7M9EI9Z4wkOlTYXXbaZfR7Or0FFVhCeFYcDszr44mn0BwAUE3l3AonmuwX8u2U4e_SEZ8y2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|به گزارش منابع اسپانیا، باشگاه بارسلونا در صورت جدایی ژولزکونده به سراغ جذب کوکوریا مدافع تیم‌فوتبال چلسی خواهد رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/90455" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFx28MFBJrypr0UpaxCJBjvYySjwCFxdkWG8HR5-38iob2IjbKynK1WvM70MQOww1m84sLxJJRmm8zi5ipPS8taWrzQ5W2Ykp_pSo2an9CioeyEbigKdHea3zdDIq5eTsMl-OIu_5GumlZFu_rEXjNFemjUk1qhEoaa-AMVlA5aW8zy7eKJiA04mAWitNAnLxIDouUb7UaaVvy26-kPVy2673PYJTl8G7pfKplgDSIts_bBhqEpJHDpGq3cf040nKDg_4mUxlUanMf64h9SDnxLyE8C7wBKmMBvV1sQ2PFDh3VRVBC0yfU8x5eNCrfzXGIUtUYi92w0f_DWfSfZEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد آردا گولر و لامین‌یامال در بازی‌های‌ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/90454" target="_blank">📅 13:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5LYGenwZZ32P98JdTzIp03MBr-AbIQwhMDra5Zo2aa85TjnPo9qoJhgae25ZCVhbCSzhtBNnCsHZ6rmUzWltt1fcC7ZGfAQpCM2hkmsCidzfcdvTE5UtXGeL0Rh4Tk5esORiiH3TLP2r41-AQTPP_yUh5EHliypamVSasuI-t7qXdfFW0dVPW-4aY6diWr49hpwESR4bGQVD-02Jf3-b1Fj-WJIxnD9QK7-5WZz8HjRW7TcnJm3-BasZA7UIBjF5kLmwa60TmjIxyu9XcfcvFVrj51XjUIqaoY3JAaMjzz8ybx6SKIIQkEtkF63T86eMpTh2vKG0ll0qqL7_h_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ ژوزه مورینیو به سران رئال‌مادرید درخواست کرده که یک‌بازیکن بزرگ در خط دفاعی را جذب کنند. از کوناته فرانسوی تا گابریل ستاره برزیلی آرسنال، گزینه‌های اصلی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90453" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lHMbVBt9JU2_f7yxkbwtEPzjQUVO-PtQkWbEGeLOTGxKVvpnSU_cQFGDXIgxfEy4SRzgumUQNzuX1o7ZudwB-1vv6TP2r_8GAdWnbJpFG4pKs7fobz5neLljhjIKdjRsUnQ9GEpdpQf2ouKNe41fUm7VRCXa8bWKVX_0b7papor2zFy6nCwNXAeG_kGfnE1-exo12s6PdAMpnfLVDO12IzylhHDZZq7BY0OvgHRyz0ktu7bvyj7SJdE-EAv3FDeM65y-GuLHvpiWXoVGlq4hrUSSgHECf5nte_q_5jgbJRBcWIe3JhBHQHP94Q_Z99mskBSMGqgpA9ycNvGOAppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد گوردون و رشفورد در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90452" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/90451" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Doh9Kjbujc_kkb4ftpKEUrc5xGEA4GViFDRKN26ZjID23HwZe67BNLYdjqTR9WUejEuAU3ZdXYow_EACwXWAFh2tcoZ74oVp1TRQGheKUL6AO_DzzHz8ALQrkC9C47JW2fj6bfGE-2tUfWApbEitER_AVR63Hk6oy7jjHBq71YPRObwaX9R6NVXQBjFFzjyjzh_Q16I-7vJzWFMIIs__PURf67svIIhb3rk-5x0JVdFaP4j2BbP6EMqtl8w68n4XZoNG8U2czkRPcZNXT47YxXvF46ZjzYl9VtXP0xKedClUagk_e0ej7ljo6F2MXI8RCBvLvCsQjJN-m-qxqBJrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90450" target="_blank">📅 12:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584cdcb707.mp4?token=iOBy4yW-bUtoeXlmI-Bt_913Q6p5ATZij-X-0puqORXwb9Dg0FA0XjjajYHBJiiBg4UTeVGdEzzChyQkzZ8s4fIYUPupz8biJ1-M3oGHSTL7aF4_M4y1IjOfYLBQcsSrDxOnMpnlptXQKKhyDMWZogEURR3y5G4Yp6N7CuwHHcSKtvyMCkABP2eN5B1cVlSuDCpnN-VXZRc_D35B52vgDNWECiNa3r7cxdbFJD64p408TT6G43XKCxsU8YR7YwCCfPQnISwC97M_M5ZX54OguWLHN_hm6F8OQoaYpbJzQ-agmvAoXSvIFV8PK18ytVuiFkWsWh1wisO_5t5rNidrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇪🇸
وقتی سال ۲۰۱۱ از خولیان آلوارز درباره رویاهاش پرسیدن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90449" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628ff40327.mp4?token=bco7VhDzPVl_pkuOEvrUXVTFn8akiLwKPhO3p8B7e5mBjO2HhacMTSbwpWtwG22ryWn99cNfNVsNhNl-R3YGhChu5fHf3AXZpmCnJnK74pjYBHBqG2hbYZ7Xbx8t2sellyzREqUGOYOpLohcbqfV-QFCO7kNFU3KvWC1h1i9hrBGeD0U3P0Wk9o8Nb5-t-baQR7Y3h4ypQvzGBgVcrKuiMQ0b12OTksT7JzYfsEdQsjjNlfDUULmtfag4-eO1t1nk5iYJkv1poFhynqvYqyTnM1aPsa8eKI6a1HecCCIig16mZPbsbKS08StNH2GqfzliMLZhUVwEIT0h3BZXL9iug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628ff40327.mp4?token=bco7VhDzPVl_pkuOEvrUXVTFn8akiLwKPhO3p8B7e5mBjO2HhacMTSbwpWtwG22ryWn99cNfNVsNhNl-R3YGhChu5fHf3AXZpmCnJnK74pjYBHBqG2hbYZ7Xbx8t2sellyzREqUGOYOpLohcbqfV-QFCO7kNFU3KvWC1h1i9hrBGeD0U3P0Wk9o8Nb5-t-baQR7Y3h4ypQvzGBgVcrKuiMQ0b12OTksT7JzYfsEdQsjjNlfDUULmtfag4-eO1t1nk5iYJkv1poFhynqvYqyTnM1aPsa8eKI6a1HecCCIig16mZPbsbKS08StNH2GqfzliMLZhUVwEIT0h3BZXL9iug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مجسمه‌ لیونل مسی، با ارتفاع ۲۱ متر که در کلکته هند برپا شده، قرار است پایین آورده شود. این تصمیم پس از آن گرفته شد که مهندسان اعلام کردند این مجسمه در برابر وزش باد تکان می‌خورد و «به‌طور خطرناکی ناپایدار است.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/90448" target="_blank">📅 11:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=WFyWC_zdsaJjFxW5BMbniDoV88mPZBEhT-2_dnbuV4tOcJ8gfQNfSE7bDI3-eW_9IN7jXfS5-ExANJ82l9tZLk_o3OEVqaiSpI7JFBQa5sopzziDfdHOWh4NG9-ZntcJzYvvS7ik6JDg4CwUzIIgxmyGWx7T2AxeudK0FtMPgqfZSAAcShj0zDKizJ1kUTBZn0T4UeKnPOZgptngcQpISerSjj7HHb2fh76ldlTw2aLVUGBWYYq9TEuDlplip13_3cNcKZeQu_bdm6E-sr0UWoPT8FyjEQf9j7K2UBLGhZdypKLMcA7RzZ2gORde32Z_neexbZzMHX_kmzp4qdn91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=WFyWC_zdsaJjFxW5BMbniDoV88mPZBEhT-2_dnbuV4tOcJ8gfQNfSE7bDI3-eW_9IN7jXfS5-ExANJ82l9tZLk_o3OEVqaiSpI7JFBQa5sopzziDfdHOWh4NG9-ZntcJzYvvS7ik6JDg4CwUzIIgxmyGWx7T2AxeudK0FtMPgqfZSAAcShj0zDKizJ1kUTBZn0T4UeKnPOZgptngcQpISerSjj7HHb2fh76ldlTw2aLVUGBWYYq9TEuDlplip13_3cNcKZeQu_bdm6E-sr0UWoPT8FyjEQf9j7K2UBLGhZdypKLMcA7RzZ2gORde32Z_neexbZzMHX_kmzp4qdn91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpMdd9kHIvLdOgTFT426wLpfDU59QbWIaLfL4vm97KIaiDbEhPdwjYtepxwHHUvj7YM2AjO_poyCgMzBTpJonZbPU_yxhqI7R-Xl1WBJFsMR0JKtpGn0fmmIehSFJSfZPwktUmKIxl67QTP-wYYddP3kiIeinci6cY_9LlMFTGSmnEtf8oHx88uJ5CTL5psy7hMKOUi5ztyS4bZvS2SMAQ6jPhQOmzznGHPJvleFKcKQcY_wbJpF7fH1bq2_HHcEWVFBuPf54wL2cOfk2VBiXIePw1zYhQCINJsHFacr6vafvth24bPCK1rTt-379FeS4UByCwPBsdq9bCm-8UANkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNiBtSWpn_9Bj3qZgHbofU6aoHAaDDu0z-L7vwode9laOpz3vWHlwrnNuVjExOaIYWm4ozAkwAwyUKMRFTpFQqdvNJzaNPnD8shVLGa873WTGfxJeD8CoS_8aJzaxQ0tPbz4nmmbcL6TPzphcI_NiwBKzY8hWR404n_7GSYXoPZDMhNUNYemx_MibRS5xysz6Lw4NebjUx1IbazpaA4ZojuHlsJl8KJGf5b5ehMpbLfWie9qh-yduVFT-o_xTqi476IC8U7E8qRj0ilxFFQ_dqHaMSv3CpxeVqg9Y-PJFlgeFiqhSbzqoIb6TJHJ_BXZsSmAmxfOg081htpllpwZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=JeHbocjA6-mKjBIBr4LtDN4C2qIinqytZIXgALp5y1UvVP_vj68_0L3vcl72xci0BWzH_yK_P0B5X0tJNsyGLFCS_zvCdMVA_hvFCBj7Qj8y-5IR8X3NFWSjddUeBOHDKZioKO2CDeP_0yfTjlJ0XZCvg5nMyipnKQTBAm5HaMstY2v80U8wlJ4rBN6J8zAmQ33o1NeO6ABWA935JDV-LJye1ClueQ6wlYQhVS9368UhTQJgRYz48VA3Ykc2kt2CBr2gBau6LAPujLcH7laJ4xswNPOgwGSE8zuYuVFh5RmS3oBixiJXQNKGbIuirbRT9RyQMwIYJhOSXCUdZIbhoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=JeHbocjA6-mKjBIBr4LtDN4C2qIinqytZIXgALp5y1UvVP_vj68_0L3vcl72xci0BWzH_yK_P0B5X0tJNsyGLFCS_zvCdMVA_hvFCBj7Qj8y-5IR8X3NFWSjddUeBOHDKZioKO2CDeP_0yfTjlJ0XZCvg5nMyipnKQTBAm5HaMstY2v80U8wlJ4rBN6J8zAmQ33o1NeO6ABWA935JDV-LJye1ClueQ6wlYQhVS9368UhTQJgRYz48VA3Ykc2kt2CBr2gBau6LAPujLcH7laJ4xswNPOgwGSE8zuYuVFh5RmS3oBixiJXQNKGbIuirbRT9RyQMwIYJhOSXCUdZIbhoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLrqzCZABlAsEgHurk38trN8c36IyOTxpDAYbcr8VsShFTg-jT_FY9BN-Mmec0dtRcqX3roS7O24GolesTd1vMMD556UK35o12SUqLmj_qxTOtDwwyCw_xma72sNud53XKp3dOtFebSzF-ObrmZLr9iPwmM5eTiAWIzTMzNkaJZtdRfyVxTKARfWzJ7A0s8AWSBNTxyAZN7YQjMXZ1WXRtQhwPCCZrGeL4_mneYA6JraVrDP1Zi1oQmUyEpkRKW4K7KFDIudkiFjxmfY1_m-wTRf8en6KshLFNq2aPVTgPfxm5VHs2D5miJHFi7u4msVmK_S42aMFKYDG2cTklxegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=ooMOXIPqf_rkz0d4Vv2Z-QO2zNcxQwSGYAJkotK8vtWpYpUgpdo4g6O34mKLBeHpVMmQrXCfK---HXImKoXur2-EIHv6UrmE4zgswsIXexN3BXWLZaBhiERCfHccoDMc5U6-ZMAzmzlRoT6IdSM0SxclJYP0L8dNCuyxHexRQuYNoeLLTcpfUY4Y8IRUfC4lIR2wATIeGvWhqbNp4mSEjbsmmwrNP7siOJoGfx4w3eJTmfVzjU2RDVB74sgcxUVZShLJGRP5eg6KkPTMsz9al-H-YXMx3rZ54LjT0L1X4gjr9A03_vYS1OrsF6-fF3utpBYSi3MrHiuBXOHKRtJLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=ooMOXIPqf_rkz0d4Vv2Z-QO2zNcxQwSGYAJkotK8vtWpYpUgpdo4g6O34mKLBeHpVMmQrXCfK---HXImKoXur2-EIHv6UrmE4zgswsIXexN3BXWLZaBhiERCfHccoDMc5U6-ZMAzmzlRoT6IdSM0SxclJYP0L8dNCuyxHexRQuYNoeLLTcpfUY4Y8IRUfC4lIR2wATIeGvWhqbNp4mSEjbsmmwrNP7siOJoGfx4w3eJTmfVzjU2RDVB74sgcxUVZShLJGRP5eg6KkPTMsz9al-H-YXMx3rZ54LjT0L1X4gjr9A03_vYS1OrsF6-fF3utpBYSi3MrHiuBXOHKRtJLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyc8L0KG086jiRpuEDtLbFy6J9Yncg4JJaj_F-e5Ptc-QTusT-O3SCOca_d3BWZQiyYQpSWqtp9zGlgObED-9oKDYItImV5PWGUHYE5aZ4iv_CM3zWeu0vOrTT8dXktA_Cz3sjXkGI-U1JevPeKc1MFXgoYtLhXQ5fcBxDjhJh532ZrsZtpBYMCN6n2lN4DSVVlnL_gFldOBRlB6rsn0Wm85-8_Vckq31ArY7vqREGhOU85YZ6Yic_hcYh0t0ec1iFGg98FQIUbOF2vUcajByrTfanoDv-Eu9gVWE4stfshth0Pwmj-eZTkXOr0iKejRyW5Sqj0xqKFRiH4zsGDTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfCVpDuTvO6KhzivpKyJZpvfUvaPnLLJLbaB6ruZLNXcG3t4y7MAP3qEgTcUWp2L-JwZjHx11KDiA7Nv04LD5cCi7gqt8vevzp4_28P7RIblA6PwQI0CmrQHhY-afvtMdvfpuNm0QUW1vHdqVdq59HeD3WexGqkbcXCBt23Z-KgXOi4CH1REpNyz-0iNlvYoSI8Mv1drSBTImlAGkapBa4XINNAh_7S4MORXekppwTdu7NpMVYBvHDTR5CzghgeIiy2LlmCobdz1op65Bk9hvqKZXAcokOPU1RjlcFCaRee7YRig9NmbPS-0PVEjWDr6jKtVq_andbsVv6hlCJUCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZGdwz5PnM1mscdMsEAwK516bfk9X6BD0MCRKQXvEEZkT-5jMRPg1eX3sfA8XDHgzNg8xcx4ScOJkYGlVMawLlUeRG_dfUMiCc2sCbVk1Zs1IDQ25ow9doGHmq0kNFMgcwXOuGno2JxFYXZzk5oNHuAcj6cHPhWkV7ZvdRmiHsZP7m5Jga7d61m0D1rmcl9nm4Tfe0X4eiyIyGE-AHpvb20Er3JXeiZHsazOxqk89vnQ6ybjwUlUDGIGO99Gsxgxe1oLh_3qNPWS5hfdhSbaq3bPrT0BSO3HxbeBDEkBpY0868xGDao66ooUDkTlbBIDTkC1L0dg4ZhkrUgRvxPsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_iSDQaNz0h0DAqU4Tj_rtxMcrOZMXmzL_0Wsz2_CGhF0pkkdctQEeBIGAKykVprcLvWXZHlO6bRoWFnVu3yq0X-YX557n8BUz_XWuQXdOmC7SCjYZCYlsbQr5MKANMLc-isNVTcAKFi2PD1XrkZdgsHLhn-nILje3uZHKuYa8Jbk7kkubVxcmhUQrBYnOqfy2hsd1MjbY7dQuf3aYbNPIUBDeJAxgG_WI590OV3EVDOS7MDAn0dC3yKiYuWdz-SP70dFAyhVgwxKSORJ5gpb_Ik-MmmSqYVzywHoCFkdvUGdSzRwNI-KCcSrZdUTmA8NaDJHDK-V0guyczCUiXUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltZDc578FFEZf2ApRAdm1GOzIVJgrrtrV9VzF9Ixc1Bg88LxUK_2hweUVkVHomk2byjamg6Yg4qqtgjOPvnu2ga9UgmG-hbxbBeDUl5_aDPU5_OtDemtpR7U0crSWjIH8AhGYOd7k7WXeNAPkOqgHxGAs2DYWEgKnXLRHn1NW15-K2miUbADfSt9rthGs5zVHgraa3MJEC6PRYaDTmVyjTGpMzJB9lNYRfsevGbdqpIkyIgW8zHuOqHnrip9gLRqQ6jK39lIKRYqGSWrv7hHE5F414iblzA-YDujrL7RPIp45klPqZqOaYvuewQkZSzz3UybfeqeDUxrgD0e7BMWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ0v2i_izd1AazGWeYsjgyqevLO55GYS2FqDR3hbJYN2ti35bRPXxJXRcZ5TXuomFpJWY3vXjNXtTfKfOcODlsxaXoZMJHbenX1xXPaoshBR6tcN2uBnYBSd2MelJYcTlQ3qvpUwUDNRteh5aOJ_MCKyxhWMblYj3FKs6aGz9BKtkBZarEjrkD_nw6KIknY5GE9siX0ykY5Yy_h0QY0fUEjG8OceeqY67P2e9N-dB4efwbpOFQ-iDFx7mZQaVHkpkEXDhc6uWJAM--7WsLv3oWCN-bH79tWgcze1_U3ccbHgQyYYl2hMc9V1JSMXzWk7IRci72meMyKj20G2XbvfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvwq_I_DoCkKethVsn2ofHsLuIVAN3j63h31gXGvofs9jf_gQHCix7lfzhU9VcxAXxQeG1Rs29uqf4mm_qnGaFTvNWjPXbQgWAf4fQrWHg7Ak4YFQgQi-8ZRUjCkQLUXH6sKBxTcd8lcAL8gR2IZyBvkfRzZTXcStsFMXxASxCelTHjRl4_wL2EPDJNEyYQGiSfCQ7uNDVoDnUeYoO7fD1loTed6glYljVvEqoOWiTxCQeHK6IBCBmh5Na8Y91n2cyI_7MQuF3Dqhbh99WLRp6uner1wgCyYSj2PKXN1vJnn697Dbkfkahoxm3AaKfjYxAOCvvJmOObnx6E0bsfWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnkizbXhuwzsUYjuQ6UISKXyQd16krr1ok2u4ys9-CI1jjugFYekNqK8vNCVX-iHlO737J5wbfegWZ4cbp79JGsPOKuyM2azwwbpXQRmtia7cXOPa7vU53I2-s1fMviyYlO8dEKGUQ0HmKLwLMXtoMk8RcI0dyk8Oz1m5X75nel_5AICbMZCwOxL0_1OkcEiXakpSKfyMAHQfW86uWNxy8YX_FtPU6cRgekzln-Gw41O-L3VJIXamaXoIWKY3ZHVqi6g5RpqgMbYLzVtVwaUIwvhgS58qW4ln1UYkLCgzeK4Jb7I7qtS9LuNx9C58HF227tOOPhXGfWcTTrFurAZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYKiqf2QXeXwfkWB8VrCZ4uNu0v_PxwS-BLpd4hg3FwKLLrlqhCyhqyvkrl31W_GDRFfI5S00vhBo75AXXk9ZVmlCsr3CNyVR37WiS3jCBp1SB2rqTasEAOapDT-gvPFQa9v_Q9WCA7ltDS5RrEwrMysS-7rhknzn7mjGUFQwLp_qXt1fjJY1QDyMwpQAe_P4x1OqLNvCff7LtooJATEMHdBqu4hr6PB8mvEsdVyUJ1TatGNUy4uYSah5nNSCzPsFMKQhMw3EagQ1Xun_EJyiKpDuqtMDLUkDQKVbQgMT3kXtkqhNe44Fo_muh0eBCvCYmm9NMez0Wsx_fiO8-v3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrUPSpUX6niMz85UzvycxAjY-si5d_eWhrZKJnhhxbvBP73y_SsHyH99CSK_fng1QxfbcMDHGNjnfhoxdXlomL2mHLS4rzvbGa1Rw8NCphc8xpecIa0TVA5SnSMVgRyuhe0LYCRbNCNDqi4Y5uQvLjCUyC2fJ1hWUY45Zn8xTE3bheUUycuhD-86iOEXMhumOvl_tUqUV42lEv8YKDvBdP1d8Lx2kafzy9fO4bEX2eSRp8v8zJHY6YyoGhVZnhU7uNPUffGATdW7kEnlbrfYoMPzgte4aniBJVsGPZ3i4e331Ka0bo_BeO94_Ba1ir3e6fUxMid8jxMmHFI5mlv6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWeTIpSZH9vU-QuXKvB_SwtbE1TiDUCUbgrQOYFNtMOaWQwGddEmnnxQUDU3MBA_-WYLPHDXysg682_CmWeu2gfFrCUPKR0r0AAHcsbIS-4ahSXGNqRbxwpxeq0C4qgz24lYIbL_MLsQsx6eCezi-T2T6FJmpP5sr7tjAuwgOlUCMyXedEG64TaH-7rozEyzPdnwrEy6ZqwOt4NQ-nSW4Z2sBmCw8BZKmaP554fYoQWInzMu0GLYZCImPIEmnhaCMHB_0umw8TT0DOKBbgaxosTWRCUDKQPP3QBXzE15_K8JjfjiNAvsiFSnW52536V2OFnkFZ__viCDq44Sj_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoPTU0nditKWTVjm6FkiSnMuPBVV9CLxfGYWV0ouUzyxjWocOp4GnomHXz2xXqFroJqM1dEhxZ7LRYWLROKoBK52H3wyE1N98BlBHtCWIzARgG9H5sIgdP1SwnIlERICsuvFN0dSO0fQZN7wYikoWRy_gM6nW72zmw7sO1kxEfkh4uhXsH8Vvgv6-P68zhMtu7fU69kriBBoSBaUruOrCqY0WVnCOI5FRL0Uy8SEMGYfAMOhmTdA-klvHejV64zO5mjPFuyxbD0vWprqf6Au8wj__YfSQB3mSsXJ4mXNta-5cTxJnVUUaKVTSNUCGZUBSoePbG84Ly8Yfq22bO1lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl_oljQWGX71WWhk_W2riclgEvakVJGcOZm082teTxPYnhNyeA19SZ124o34NhdUCj1bWqIDxmaC-epj0NJmfkrm3FeCk9igheeYZhOyptHGA7Ks9XLBMb7S_nYLWJX9OsN70v53k4TXcmnRia9yd_6ZBrY3ym99JtMZnU7Tb7do9eteOJyrAKMYjPalKu4z9eHDCDTrkRNVdSVntzfpfCMZzSDacIdJqmZYNt6xUvUevuOvO5Eu946ni3RSqO_YYqzncI-73ZRlkaBi22MdRdw2sKZlz-s6D0UDHYmwdewjRsmaJdWBqp1zVega8nMavMfz2F858znb-tDgJWSq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb_lVxWJl_o4JygknDnrVdD7w9LohIBpckXlrCyzKmEFdMFSeJTqbsspgytCpBK_ue7CflNTVAPprU1ut098qG22-Gczsj-NRNKE8Zich67VhhSDQryHVMzFgB1XZi6fMRasNxdcDpNdNrOiQO_L3DLsnOSk7-hNKLUIvoKGvYBjAgHI9j-Rw4asS4-WTGrC03nuJyzolnxcCiiYKipoaX_gtXVEpe89Pnqb3p8IsbwOFCTMgKXYPONcIJ31nOyyJFxOPZeLhNDhl_yEb0HH6X2ml_jlLe6xOthrtQVTF9NCmo99W819Nk-gX1w0BuoNkVYrK7fEi3wA2B1UqBfd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krEkBobuxPipiwBmC7mcgPZNqyGNGeCdXv_To7Wub4KRToBoHCeWieA5fJNiXFXPWPkHJxMDzuiFZGtWJ6oipUhRsDXg3PBKJHt6BRPtJ92ksDdXkGsxi13MyEUu0oCvN0gn7TOTHjMyuFvosdNL0NqXcon92b69S_sAnaKeyx9_IX0XzdWLWgC7DRbps7aVRTVll2Hw1BkTeCMGGNoiKgkAPuf2LIqdGMoIvFdTb1g-HHcXpoN3iyyEy1QpwLxBq0vnpFa4HtjKopiNzEsO_2RubmGXbZQL49_zl0jxln4P3EYND5mpP2Df9FNKOTdXVv0dtYzJFNQIOs0QJ3CGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDsLOC0yhzu5vP25kCen9Ws75unOemLi3IaN6bzxilu1DQOf-cnDDBZtBxMRxdUYAI-glB9w02lVn-tDspq2YXOlNlyHOuUau67OdD7rzgL2tnnC21N6ol73TLLiJUc89XCMVEy2Fz6VTLwT9fmGXT4TwyhKMYzSqRZa3gWMxROxBXT9M3ejDTMi2c8c_aTMod1zr7_nRBD_mav_DNc28P5v8NgaML5WtdUF3Yt10C3IR6E-zVFPOYvydtxuJ3ZKOzHNSGUVhK4qqG2FcF4TQy524mhtLMOdzEvP5S_72b_E3-nQBG0Tsg27se7AUlPKw1Otbgh6OG4VCvpTNvh3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgM1e_A8qpw-kZYOJ68Qk7s0Zfkwi_8mVah51T9HxxZ0MNnobUdT_aO24_0lP691RWA1esPZ7rKCl3F8lRJaYG_jTdsNbTD2R2ii78_1FpAREROPb6ZhXn7tLCWa5iP4psYrL9WII58_04BM5cr4sAqZS-LKFqnattghyKUXJcdy7QV4QZl1N-oFoTW29VifXlzRA_4R5j3XiSN6VF48w5DsYzUuZtBwfTue-J5KycbkDsuCHEaYc7n8TxiOcKsOQ7QmxL5vLvms2Q4GPswclej6c_6q6NDKJ6N4eCUC0ZyFg6uZW-JsLT08dWWE0658LATtU0TFhMBs-9X5il6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9vvmeIcOf1mD5N-tki_KtXfZSKaUZ4rkUwb-4TFhoZygjeB0EJmeGBZFnJCcFeVOIku0NNKF3dleIQzhNm7KdgaKpivYhB3hAo3JwAR7NmayJfR53Rnr4zrRbJa6Oupe87L_khpcV_ZbolUYBdwVXb359OqXzsjZ5O_s0hpEfP-2KQClDkC0M_ncVHo1fCw9QBeFKkH50eJFdkhL-oVy1jGzIeq6-uOKEnqyDEPYqyIejMUCM_ND6N72y5sluVpiMmjIZopz2cGzA0PgSwGyJ_gq6mTzJ5peD7FFlQcAmcirabvZs66jOMdv8i0uNvDjFaY6AvfrlWBhup6j3Hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usmMtdsnhEA8K7dh29mDRywEUFTmaR8_uvWGSmbyXiL8Cx9-gcida-J-E8SPrRjdjrbMNtlZvcp7nWW8-j9voBFvHk8Jx2uVgfGgmYBenXk8Ye528K4IKGQGTHHd857ZOjYwZeDfZqoisOfFa6qbKJc8ood2gPMoMMXYrhvumQiyrzGhPefs8ag8zix86KclapSdZnNvfnm9M0xYoiwLFQK8mSiyhPlH4J3ZDucRlfdK6cigtbIbNWVmWYbdIFt0-Bv3h_B7ehl8nZ3NcXNfGyfuEgIyuCnjJ1S2UzBEUArzEmmIswdj9BcXBwABb1kUSvAYNIJVceITL5Wylh0pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfxgu2NIP9ytYfcFk1lkX-ZpL_o7amC6RHx6pJNNgfiN6Pi8JE_QwFSiYX9P51dxEzMKB0686oXF56uFN2inE9XHYo9r-VVqwre55YihE9QMsZzZ2KIB6OWFPgDnwo5iFQL3mSm3Vhkd_8SJvjG2RtO0Vwt-dOx4xAEX993GttEOJzCq3o5p5u80Ucsc8ezOn2lJcXuvkE24zjpXz4risk-nShI7krYxjqEjX8o4HBFAc2bqya6E4sjai2LARaKPdudV9VGND0j8k7gVYXix96xMQ9mR9jBn_nyVqe094Xfr93ogIBnJRr3SJ-EmhZEuNEoj7rTTBVKR33E4TajBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAfNhvIz2uv3jNOvHyqBzPuSWU90rtJIYIjWTwMM8JLgM70P7qLBdwSOfBPsMvx0JrlaHd4uTL2nM05QJbpsJ8R75cqNgPfKVbRAc4-6JN8l68HexapRYdVOFLqEdZ4qku2qjYkTtsIVKLBAYPUkhHuOXeRSdKuI7iYLrqWFQmkDSW1v3-wyZ8fsWNi7Z7QaJ-vvUvlIfmNpEEMFBXSIVrexVClSOfVM_w2D6HErceJgxL-LCtNO32yAqfvCxxc7TMr2Se76t-YG3ldYacmWZWiqpQQepT_0FQpNYCV6HIRq3QTppNU66J6x_9hplxjsAS65sf1DyS_fCB5UifzGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBbXqgwvtueeo3sCofWVfx0fMrg1YimEDr5_KveaOyzMgW5lBejRYanP0xq5nYeV1TGDiCGzY9wkdAxCA2Jyf648K5OgD5_hIO8qaKF8Rpc-NyQI4Q0I6mUdc6h8w9ELoJRkY817Pc04GPfAbLep7NV9Peo9kJW42MH1Bx4E84g3rP1MdHMCNrtFAjaMD171KyAlDbk6oH-RG2_I5AcB7OMbBAdt6N0ZS0HMu9IAW_rMPttl2-a70cURlOMAQof4o6wa9RS2RcUdfUsDqXnaE34oAiQbXrs776ghOC9wAs29mBovA99vweZ_uwwE2zrqaMOA215PQFPxDT6xRs7M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pD1qAbfKqQ29nb8-BTNN9JvrzO9l9eW0a5seUzADvhKPPixl2mKCzuc7sDJfXphOuJpH4jgH0BB0d-wrqXsH9WKdpWJwVIvigmVo-VisdbhscZNckQHRKpLwGkZ-2QziNUlQAEx3pUjxP_5oA7ubodXCAG22mgLDjupRqz3KVs9OEWN8Kb4OG1v_SBgW41p3s80J69VvASgwuCX8VbEDzMGq7g6oaWhVGKif8Xr_03RnUl1OJe4Vevevm1-QzGyxAdv9NpB_eCBNwG51zwmfCwVoeeutZ_YN70l_CDBWUIySvtErWT-og4Kl7s5ZitfIqYzgGnP7L-W_tghipVdlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9fO9PGk36qWKZ0tzrbkvoYtqIA48KtCIfzvJpNJxAvfScwpsbGqf-5SeIGIDoSYDdfe1i4MK2Phyilpupp_G-r-Wn2VXMr3o5NmPNzjCvFHvo3dAZ9kDyMudixiAA6eb0GuTEpzezII6OGs2ZLajTcQKuC66IIHpY9xTciWK3N031jsyrqKAIJaQiWiom7WIPNnG0Fs-3I8N76Plg7tj66LvFQURusjrP5rXEQBCwkQDP0VpqE0wC3NJ6N7Uy2F6M7TEz6HpyDJLwyFRQsvEHXzcnNpy7vo_ZZgmKVSWuMfvymiFuNQzGgIAntZnK3KI2IdiYuT_rfFi93hlkVN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyuOnaDLAFvvUU-YrKXyLhS4ElmukDcBB4J3Rxi6Enceh99YMVpjhhdiU5z0H4ttYffIzfwqLd4MJ2ELXoR7WQmhHt-3UIdo6fqkpQ02vp_BblpVuX_OQ2XItUsAjS85x8s5UnuvpRe62DgtA14i06QJoSHYBo1UIFYzBXcMW8Fnq7MaDifDaeO7dQpG1V9d0_AsInOUuy342KEv1541UHmOiC6BYl0bILimHzJcq0-IEW9rKE1QqUl960Fo5DdGzvVUEhXzg56Sr-D-qeXP0ZySkrHg3bjznls-pnG5FrAu7ODuR20Py5URKQUtuB0bRSIPd6AKUNizu8JOTJ4OGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9MFjTaW7vg3qb_1T0TcsYYQzAvP1lrjCc9r3TtJyYZYqqhSPkgWugUPkQv2QxPz7WXDqcNCtcpHpeHx_MPcao_0__7ESgEvNLykKT1sfi_6Dy0oWkOcxYsver_4ZtPGx1jTYIBLZe9gfPz8kZNEr0LEbsgMVwY2OU4dnjfaZD4gLBX6wid69WRxierWyNBskiGSFT3tCCSVApwcNwXA5pr6yFtkIPXVY8ly66NYmtCpgykrOdRao6ctCMMFQ92Nyrwk-0tcwy6BzDa1TCGdo_GON8grmvScLC9dSK-v4bz0glEQrVG_iK63S4S7w-Ya1Orr9UDmnOOXGQv_LjJfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFtsVX-Zo5bBuSQj2bOh8lHyfzC_ZibbBVmXtL476EzwIpOAjVMxBWuvFFs2Mhqxs0qlpvudNEe4ZwdoIuWfKJ5rupDqgZe2bCiKmFFE2hAz5tTVqBuyNfjxRCQ6omzcOT81zOdD-zHJVmTehGHe_03Gss5pFLPfE3q1R3LzmuMyrwfdkI-TpKi3soglqMMIyIfpctTXNz7KOYIT_ChfsbnNdStOCXZCIjq-qTHy8Fu0NXMS4b09guRVC7iTTg0vP-Zhvc7yArJz0aFYUf4So15g_BaK_4xZKq7jIqma8vi7RbrbkF7SUitiCGB9rP0lY4PquHgkMNNi01hrdsUKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyfxUEjktQ89mjzw0oRhwOIyXZeUtaG3WPVp4kkHOnH5w-Vzx46ldm2L_NKRPgde3TnQURl_szDPZXks6Bfvz-X18xpKPllDyuO-m4wc8qdmDlkBHnuZAR47llRXJfNpSehZZM7j8sQF4xm4NCGtitWnIV94ZtIGMyeuU76ukR5w96mrHBGmkD7z0AsemFnOV34O2NvHcNrhdrc4UTzRPAChRjtbfOT8boDgSYOcZ7Gk5bxujyOM8rthRhWOxemFaklo7zgYC8vNmipE8782vGjKfhRiAvm_SVqqcYZ9TKp8WU9tUx3nLOnc2tITbdn5vYV-KlLxApxcJuR4eAn3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgZgdlJSOWASD0uU5Vt0QHXvRT4UNGEh9eKBxwiTdajJnVSSqJ1-iz6ihPmpcJ4BfHOo6hNteWtgjHErZZVUbEGAsrXEV8CUoF6QUdmtgBS-hbDZ0k9tAYGtAYtFcU0ltXFD_zXXPsoDCCriFVklAmQDY7PLk8AthbsEB-828NA3hM1TjQvEi2Gfzph32JwaUgTqcpCmPWp7wIq1-H_wxXoaartr7ipt0ZgB58VEBI9Dki-7JEtjHMvwQrQc2Wk8DiLgYARdh4BG7aCMSAjrGoJ5mFXzac_oqMkaCqbt3rfYqIhyE27RNPc8JqY21it47m4JTVEpJxuGnzQfCF70fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=knYMk1p4WqUzxFKoOfmTFoagLXo74wOJAntnxN_7IkahSZWU9WemgqZ_AWmWkTPK6z76hkaW6kcCyOb1tSChlkKG0b6IXDPg_usd1gIOXePEtoJXt6dg2jMGM3mkBMO60a72bpNDpsqereu7WIBGLciv0-6TOA9PKtNAt9rhqgx6MBIETBYKbtUCRb4njTf5alXBwQEts7mVFLRtxWZ4zyj1JM3_7ZtUtfur0XoN5YGrAU1uTsNBRAdgTHrZJAHY3eV1SZBJGqLpncPgLqA9zRUsgx93fToglw4Qip-s3NhFCkJqt1QUS3jml0-Ryv-1YUQlpEOHvEDieaadnR5adA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=knYMk1p4WqUzxFKoOfmTFoagLXo74wOJAntnxN_7IkahSZWU9WemgqZ_AWmWkTPK6z76hkaW6kcCyOb1tSChlkKG0b6IXDPg_usd1gIOXePEtoJXt6dg2jMGM3mkBMO60a72bpNDpsqereu7WIBGLciv0-6TOA9PKtNAt9rhqgx6MBIETBYKbtUCRb4njTf5alXBwQEts7mVFLRtxWZ4zyj1JM3_7ZtUtfur0XoN5YGrAU1uTsNBRAdgTHrZJAHY3eV1SZBJGqLpncPgLqA9zRUsgx93fToglw4Qip-s3NhFCkJqt1QUS3jml0-Ryv-1YUQlpEOHvEDieaadnR5adA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns1ofNMSs1eHI1OJxozxiBabUPLGHMBynoeH-fH4kzn2kOb-Y-cv30oa5SfUh1hVOHt7eunHM1zpvIlFl81neV0AG-WWKDjVP19tQYMtLMMClLd034pTtukLeP2EEHJFyWULlhO5ubdvTj9yYlB5ptCWWvmmtzC8rvfRN7xVbRZSpXlYJL7rXFHGNPor0iz_7k7B38XZoz4vfQI8j9SmPHmpq1b-xHh4ueGhspo9vVwWP1t2OqPuqenF1icCJHskT9NYuncsPT5zxr-axkoypqJHVzuU4L0dz5PoaXNB4PWG-vvVtOPAtfAj3ijwYJIo5BPNwZRNABKtdhgIN5Wq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvFk7v2oDZYhNOHlDIYYvZVI6qIPrW9itT_jCAq0c87MMWmVynH8mHcwy5mZzy15ER43Df3mCgiIkFqUakBtVvdz43itiwwc7gKNgAwqHcMCsVCz19sLHSqBUHJi_398DdObyMZC2sUeVV6eY6E7MuQkxMid4aU7ooKtl-DYieJLp3gLe72OY577PJEkOqqKUTKDB6ATiX3SADZQKzbjjtM2jPukWMcfsXM8srWEd788IqKxetBX_T6yb_4W4btGbL_N74kT1Z7rL1hP63tjFdhGGXhI3vOWXioo8wO48mGWpBAa5tktDglQrgR9VuhqnVXphBBRv_BMwTglTwt8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPZopaXx3EBLdHI4TCI7CpDUak0aDzLdPleE5mM-tCCqFfvyuoCrorRaap9HeARaTFjmhM3itWYcZp-yqeqJPdCDI8mluyGT-pmInIcaqjJyGRLuYFTFkax1GgwlPH9jAKguvxsMzzuibAWe7wNQK-nQeJ2wHruCCylTyUw9NxPG-0gXEj2cyhYiDQ5N-38GwHsWBvokynsWCaQQB9OJu7ijWLV3gFmvRWsRxDbIDj_8-kvxO8-oQMQzUSNJ4Yy8Qwi3bZhuAJmVgSv4jnZfA115y1wHP5ak_gYmK6sGlDKOSAv3PSCOb-jIuTMUlRPMibfSORBdlykFOM7q-6n0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ3vvANQqFhrQzW2-f_qx9-kUuwuRQlThQk41qk6eLMmbsrToY7KkpM7WUvOF3abb52tE3sLghcxMPbh2g-Zhz1OlGFEs5NuYflUrIkFMjFGJwxpa-N1M9AvPlbFoa-Y8MiiP5NgCkvqyjBbjkzHYSyNer50CRML7U5x2zUsd3p91vTv6p-BWDg9LcWNcC-bH-NROwYn3_G6AA94fhzFdQb_uKs7Ye4ZUEoQNzuNWfRdTXwi42WyZN6aieax-YVfJcsXlWuRfc1D4M3MswfHcnzvltat9IVXjbG10wRbhV4bAHdmHbpGND8c5Gs-doxI09q6oe_vg6zmvat9nqxqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=EnicKC5LsIqRmEA2F_Vadxsagd7hZNvtlubLC0ansU457dQE_bJTOYR9NEqCTD0Dip6lZY_9o-SzZaw_z8kKouTh9A65c9A5EG-NKMybMBVcDCTy2pP3BByxl50xvisAl2MyuWyciVEvNZZMo0kP62qTG_hfneAR8rPKQJzHA-OfSMkiQm82-AOGYj5BWAHbmEUkGkfY0WQOKKj9wqdAS_dHZ2AGVkb8WQFEUUIE0zJzc-Mzv2MoRsJ_urzyDfZ1eWvd-oqkm3NPJoZvQX5XlYLcAPyckkQpDv3RQOrZdzjOHh1OKkukvpMsFsimefqKxOFnVCGjSXEUQkVHUkvfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=EnicKC5LsIqRmEA2F_Vadxsagd7hZNvtlubLC0ansU457dQE_bJTOYR9NEqCTD0Dip6lZY_9o-SzZaw_z8kKouTh9A65c9A5EG-NKMybMBVcDCTy2pP3BByxl50xvisAl2MyuWyciVEvNZZMo0kP62qTG_hfneAR8rPKQJzHA-OfSMkiQm82-AOGYj5BWAHbmEUkGkfY0WQOKKj9wqdAS_dHZ2AGVkb8WQFEUUIE0zJzc-Mzv2MoRsJ_urzyDfZ1eWvd-oqkm3NPJoZvQX5XlYLcAPyckkQpDv3RQOrZdzjOHh1OKkukvpMsFsimefqKxOFnVCGjSXEUQkVHUkvfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWJ6_dN-76Rbe4Viwu4LCuDMKERuqASWW1Y6vZz3_RJ0RJvVYVXboB7CQ2ruJAWt45PFGxtC1cwMl4fAXxeI2vkyXzM2zC38lpZmHqcUIUUta94qEJ-qNaPQWvhyk4VuGzMzVoi99cV1dvZv6ApNA6WUgBvFXYYk7OTWROD_tGBKBk6o6DrEP-kcXdr7fAWW38m42vn5yIBws-Rs41hpgBIxaViyASPCMhR_XYtSv1gAiwaQ1hyQ4__MqN9nBDPDKTtgWKPx8Z1838l5-Rbkxnpy_TxJhaUL6bt3dH2J8gdZf9ikSnfc-5ALzjzH5oc-MDJlFqYSzw2mEI-iGfTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JgLK_wiRH_EpJ3KvH2RDDVrw8H5ciys8q2Ty-f9EYm0almRKkWtLn3G-rDu3FXP0Kv1NX7ZKbk3rqUwNtwxxVOGIzobZDYhD2JTNvtfkP37hqbIWTqlk51W5fH1FpTQ5zby38h8O2RMwJY0eH2iVoz9bx0Q4kVTNMUybKUOemfdctU0kzQhil4akaihwMCgm1HC0BLuBBtsRyiB1B455Zd2PwI6PO3p_fvLCMWGZF2tbKuN5zwS14nRBLXC7giSfKmQuAKKtc_r35lBH5GLRkdYAs47fAeRBltHAxj8DMT3Q1BIxb305Hu51DdbqdrBwS2VIT6y_by_712bP7SVw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJMgrbmyIPvc-77aMrxVQ0b_6g9uK3ABLddsYfxBETctKcl_55I5gJGOgpa0Q0nE5K7aM-i4CyNE1qPdlOVPRVsj1lSva-6NaKJsgQ61MLkx25smH-IU7ui8aFT4CToykgd6lb1YXSxN0ySi2LtfdqyrCNE-catio_ep7QRnD_s-QESyNkCRAWPW3P4rViYgllnSfeQ9orVmA78GJnEm7jk4pcxBE4c-1XgzcIBTHxDK49c_3g-LBHPoY1QvEW-urHpvc6IIC_PLfLcofm-gXLj_elK3N-QJskq0WaSCCTLncpmgjWjuGkkBC4EfIQ6VZuNIOATPvAw1znh8BCdLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9txfCmvYJfpMcGO9213HiEIaSED0yIriDhIWK4pxbBhx4vadGF_Xtow6RqLXBdX4rHTm3tT267OequOMiklVI3045LHc1HqszkGp8NCG0utCwwrYD9Uwgp2_7c6dBATib3uPW2_5xGl8e7FqoHEKANj63ZG-X9os-qK7WPVLtToAr7qU5phjXVqFhZbMUyFFVSsYRnS-l0msLIh3fwSDjauuEBwnQmvC7tnD8LXOiUIz5SgoKkjfXjOkrlpLzcPVekE2GrHk49U4UNiLTZJS8T_17Vb5oWh3W45SFs-jd8WyO6mOOj9z5Hc-k7c5AgTYLsuaBoJRkjmEJ44oc3rfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=HHcmyP5VO3BnjcXIuy4MraO2cQdqmo7GHfRydVQGuXY5KIAXaLldpESUVN3yQPNrhZT7noPa7_mpu3dU1_-o9D122_In2HLIAsLT_xV5n65ASThX9p7v5wXD1J-lF5Qly5ABov_8BGn9UCmTsPriglfQfOuqfyMJVLuchwpsey_WU0YKx9bUFiHd8D7SpniEHbLtTsMW1nsprXG6YSH39FWVUo9M2oOJxkqYibTuP6_E0hIr7vZvaF9ZCfyMVmr4-FNJINfCJn-AFmT92QFBzczwd2Ww3Y6EgTye0CvjycUdvIE1fDM5bn--bqzIhCSGLcktP6D-GNZTy1y6PSLZ775_MaSgb-tiR2mYwSU7c3ZK2SUQmf64qX3lsN1QZMBxXSRDIGmHiHVH0D7RhES8sQCFPbF4J4dy_CMfz41PJJ2rOuSipwDdmhNV5tJpVWVGixvdTBA5N0RCrb49Os-UosXlsqLqL-fZPaGOR__MjolN_5siqqZvdW0Prmhhb5Eq_cL0tyos41XuWMqAXWJQIf4t8c9wptCTLEkjz-eXwg_VRXrBB9lH4onHx_do117Ze1P0H7PBnCaik2jbL2gYt836jAeF7DCqVBvhRuDsVk-vwCy77j73IfIiVyKLh-UezH2RSHOCG2Q0yRv43pf_IvlCG4MEGX-A2m-AgV0urQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=HHcmyP5VO3BnjcXIuy4MraO2cQdqmo7GHfRydVQGuXY5KIAXaLldpESUVN3yQPNrhZT7noPa7_mpu3dU1_-o9D122_In2HLIAsLT_xV5n65ASThX9p7v5wXD1J-lF5Qly5ABov_8BGn9UCmTsPriglfQfOuqfyMJVLuchwpsey_WU0YKx9bUFiHd8D7SpniEHbLtTsMW1nsprXG6YSH39FWVUo9M2oOJxkqYibTuP6_E0hIr7vZvaF9ZCfyMVmr4-FNJINfCJn-AFmT92QFBzczwd2Ww3Y6EgTye0CvjycUdvIE1fDM5bn--bqzIhCSGLcktP6D-GNZTy1y6PSLZ775_MaSgb-tiR2mYwSU7c3ZK2SUQmf64qX3lsN1QZMBxXSRDIGmHiHVH0D7RhES8sQCFPbF4J4dy_CMfz41PJJ2rOuSipwDdmhNV5tJpVWVGixvdTBA5N0RCrb49Os-UosXlsqLqL-fZPaGOR__MjolN_5siqqZvdW0Prmhhb5Eq_cL0tyos41XuWMqAXWJQIf4t8c9wptCTLEkjz-eXwg_VRXrBB9lH4onHx_do117Ze1P0H7PBnCaik2jbL2gYt836jAeF7DCqVBvhRuDsVk-vwCy77j73IfIiVyKLh-UezH2RSHOCG2Q0yRv43pf_IvlCG4MEGX-A2m-AgV0urQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=Y-Zv_Ukja6a51-kt6tfCU49jCXkRhrw6aaNoPLLx6S7-gh1rTh65JWL1OcLmB2Ofnik5xfBG4wn7mqxIpyZiHuWk-UG-olthV0Sj0Wcrt980AXJlKQdb1ypO8SrP8LuQvF9iOgvVvP8aNR5F_oEjTgQo3sg6rPN5hOFP9ldnT0pjK9lxcTWf-vXZBppZakb4Cu4Am8Wf5mJcPmq6kTXGLxB34gS9k4DqcCYRh4pvvDiApp5JvgKMZt3cPDJe-TupdmGxOg-Mgqn3Dnp6ZgUDX0jQm7v3IUqbvAjx8WXbfD9x7S2WtusMGFMDwpr86R14gJLoIsri01NfA0DF5Kw3ezi8VyVhjBtfGavcX7-L6crjEtwkWNxCmVAz6FfXJzkz_mICHSbW3SV9VyKkwk9PUnKr_sk9CqD9TnMTsW-o8yibhuZZ3cKeVnveqrScy1CI_8Gv-HczAJ6PFjOJ5GPa7qViXXkP12FoHODNW6Vvo2q7JrtOBJRiD2putgpyCmbo8ysImZqfaP-n58aO8n5K74-H-467zaKHgOYSvNAIWySjeaITGDuWUqWvNKgM5j2Zjr7mAdQCg0X865TN9qo1o-0f8LfV_ylwm7VDMc73TY3vNGSknxMaXrk9KiEWOTgvY04osElVEeQWlntNgBJZJHKnRl0TZUonKpD5OBq4Db0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=Y-Zv_Ukja6a51-kt6tfCU49jCXkRhrw6aaNoPLLx6S7-gh1rTh65JWL1OcLmB2Ofnik5xfBG4wn7mqxIpyZiHuWk-UG-olthV0Sj0Wcrt980AXJlKQdb1ypO8SrP8LuQvF9iOgvVvP8aNR5F_oEjTgQo3sg6rPN5hOFP9ldnT0pjK9lxcTWf-vXZBppZakb4Cu4Am8Wf5mJcPmq6kTXGLxB34gS9k4DqcCYRh4pvvDiApp5JvgKMZt3cPDJe-TupdmGxOg-Mgqn3Dnp6ZgUDX0jQm7v3IUqbvAjx8WXbfD9x7S2WtusMGFMDwpr86R14gJLoIsri01NfA0DF5Kw3ezi8VyVhjBtfGavcX7-L6crjEtwkWNxCmVAz6FfXJzkz_mICHSbW3SV9VyKkwk9PUnKr_sk9CqD9TnMTsW-o8yibhuZZ3cKeVnveqrScy1CI_8Gv-HczAJ6PFjOJ5GPa7qViXXkP12FoHODNW6Vvo2q7JrtOBJRiD2putgpyCmbo8ysImZqfaP-n58aO8n5K74-H-467zaKHgOYSvNAIWySjeaITGDuWUqWvNKgM5j2Zjr7mAdQCg0X865TN9qo1o-0f8LfV_ylwm7VDMc73TY3vNGSknxMaXrk9KiEWOTgvY04osElVEeQWlntNgBJZJHKnRl0TZUonKpD5OBq4Db0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdAOXmZ4MSiE2afIGIrhEOWZoU5Ri4tIINU97L5Qg_9ovIRFZLRR3FrrxQ9C1rUAv9PW3xCjuI5SOyV3W1IwxjN6Y7b_FvDhdt7iUv2sGugwxcX_fgtfiPOy6qf9jOHE__9TwYLU0sOPHYr5V-QhvUk6BtYbCshgjhutPD50AhBnf0bt1WAWfCygqiHFtI7vZAiGBPQ0WIXLO57qPf4Ool_UH4DGhS7vzIJvlpcntnNHaZIv1usAnZcGOUCikaPMLt4Essb5iPxTkFjtuHCSwAY2gZfmxFfm5n9BRkBTPv2KZchU-Mnp5vfWBtg3wg0DQYNhOwYddjWysDwo5sKOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoEF_IqJrhbYrKVOe042CPNU6kffCnyXpIcSeop_wXEj0ql0DxS2Ii3XIA_svPWpIqnkeImsnNFfV0_ZB4jCTLiANYr_o4rzCQFlxlznNN5AR5YX-4mSvDSC4WeuXKipx8Efc5pK43bOh0fc4P0WiyMQ2dPPqFRihqsb-viOQUy92EZ5whUs3mMOM2AK-XriQUTrYxfpVvi4R_7RNDBTOvB3lJWC5wUzV1rPJ7vGkgYT9eCjMIi3_73M1GAUCc-B-KJIIzOacJUxi8rggZ4DQJK1nM2FVAG2CCnCWvW8ZgJ9HGhXAKN0WnLJqGCIbSDwClHF6myxYZEEgWN6PBklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ترکیب رویایی رئال‌مادرید که البته بیش از حد رویایی هست و احتمالا محقق نمیشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90375" target="_blank">📅 09:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏆
کار گرافیکی فوق‌العاده زیبا از قهرمانان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90374" target="_blank">📅 09:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac09312735.mp4?token=VcnavcFN-lYGK2De_05ns_vMilZ0pRkPavxu8CQBKwpNhE1Hbpy3eR5KFfKL8TyRsKegVDNlNlreNY_8U6ERyF3W80LifcuXNm4nAxb6CWjQShAK_S58Vw2tCeACFs95DcpAZLtXSCQdQlwfY21_DtC-NnFcWKy_7AtikZGtfQyBDkagAWv1IFFPwFNGUAtPJypxryTlaOG3TQN-ZblYW8r3v7NZDDSkYpGB2I_8_clMZmfb1zzeTIR8ReQ1xL2JhzDfj-nWha3-OPu9pHcxQlyMgMBAghPYXIoxk7xYjMlbqqgTFTM84p4rvY9Fmb9pBoGk_fsvNd93LnRHp7W1vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac09312735.mp4?token=VcnavcFN-lYGK2De_05ns_vMilZ0pRkPavxu8CQBKwpNhE1Hbpy3eR5KFfKL8TyRsKegVDNlNlreNY_8U6ERyF3W80LifcuXNm4nAxb6CWjQShAK_S58Vw2tCeACFs95DcpAZLtXSCQdQlwfY21_DtC-NnFcWKy_7AtikZGtfQyBDkagAWv1IFFPwFNGUAtPJypxryTlaOG3TQN-ZblYW8r3v7NZDDSkYpGB2I_8_clMZmfb1zzeTIR8ReQ1xL2JhzDfj-nWha3-OPu9pHcxQlyMgMBAghPYXIoxk7xYjMlbqqgTFTM84p4rvY9Fmb9pBoGk_fsvNd93LnRHp7W1vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سانسور نام علی دایی در سریال صداوسیما
صدا می‌گوید «مهدی طارمی» لب‌خوانی می‌گوید: «علی‌ دایی»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90373" target="_blank">📅 08:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxu1FoxOOv0f5eJmD0pm1mrEYxVMNdIqX_laYy0W4M4nTyUSIEeSZvh6hiSnKkLsa1LTx3K0R0AViMI7fGd4EiGDYkhbOBQtkwRjyv01zk7E0R_L88v3G-QNc8AqpIV9pCecn2fZiH5pifo5yXn4pDzNekEpIJA9aWhGK9lgou-3LxpYGiHts3jFRe8q2zTBoD9AdAEgb-9L-SqNTrVqdPkna9Q_768I5mDlvu6Zf51iWX61TRZMiaaEsFYSwuh7UVoNHjJNgKryYHyXXubRlRv58wczX3ZskmIElCecPNCKHClbbFqpPFopk1HkWxikIePDvX-5lLnVkzlbxoBU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
لیست آرژانتین برای جام جهانی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90372" target="_blank">📅 08:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ-eIEOXiCWqAkjBPGT5txQNzfv6JYVdsH8CGnw2omPa3F6B-r8rk7WdBehzNzcUYP6Lh0Wu4ctiaq9gZAh5sNAm8fdk4drKOBFPCYjWoGKgDuXM-QgFA9JCPrG4jzU5v4pm3LOpknq8U6Kqg_Rwg8jkPDYfJwk7vbkpR0CiTBGTPpCv7pdCJs9uTv5yV9KDM81LdTKrKCXR2p6tThzOSBPJzUjNmokr6BneHMoYb568-3_a0DPWQ8tn-h_XixpulUEWj73tgd4Kpz7tQefOyYTHw9gIxEgfHMz4PiA6FUwn1KbUb-iqqYOMeI8bSU8NTmHQ4K_AZ6QOOWX49RD1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=DmHAwMnLpv8IFuI4eYWw-qfDGHotyjjNHPxw71-R7Wog0IROl5oyg_O0Z8KuRWVZb-xsjojWMkM1WJrnReHvpGDuA1himitt4e6RCgbm2KRtnpEfpPbHnzT3gKw8kovIAwfxCh4_gwFoM3e5UHiYDqIL-ns0un_GqMl9aZGdyoR0ktvBr3aWmAWo8aZJuMjn-ve91UIlByfIlMythBzNyDbaHudIrkgbBUIEBacfjKFSecsZkJtEUxUCiZP-WAa-5pEZdeW-DlDU7UzV8EOx8gwnraKK-kL-PwqDvn_Ug6wEBv6JshigEJC9mEuUn-jHFSROkbxHSr6h02Zfsi9pKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=DmHAwMnLpv8IFuI4eYWw-qfDGHotyjjNHPxw71-R7Wog0IROl5oyg_O0Z8KuRWVZb-xsjojWMkM1WJrnReHvpGDuA1himitt4e6RCgbm2KRtnpEfpPbHnzT3gKw8kovIAwfxCh4_gwFoM3e5UHiYDqIL-ns0un_GqMl9aZGdyoR0ktvBr3aWmAWo8aZJuMjn-ve91UIlByfIlMythBzNyDbaHudIrkgbBUIEBacfjKFSecsZkJtEUxUCiZP-WAa-5pEZdeW-DlDU7UzV8EOx8gwnraKK-kL-PwqDvn_Ug6wEBv6JshigEJC9mEuUn-jHFSROkbxHSr6h02Zfsi9pKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=JmvCrE4mn--p9YsO8AozERm5-8nBSCuMDhcqcKyzftOytvJWj1C2_oftemk4F7ePef95MxP5eeTMH70QRyVvgrpdmqfxxbHztDnvYr8YVo7bBb9M-0vw-4ix1W7UrXejqIK9Rd2_uvcozugiLrer8Huu1PZ6Ik4ukKJsvkg8UzuXUHwzwQQau63xj5TbVHlHZE0XmPgQF7AEcq-S6Xt315kI8_IG9PjL_qmntcmOD5un90LZ5NeHKskC-kpnz019ZPTeJO7XCqgpmNUje3_XvMst3zkszOZb32Wsew9HzQzODWv3YzxacfmK6EgYONaMBxdXX4KvYWSRoN15Gi0r0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=JmvCrE4mn--p9YsO8AozERm5-8nBSCuMDhcqcKyzftOytvJWj1C2_oftemk4F7ePef95MxP5eeTMH70QRyVvgrpdmqfxxbHztDnvYr8YVo7bBb9M-0vw-4ix1W7UrXejqIK9Rd2_uvcozugiLrer8Huu1PZ6Ik4ukKJsvkg8UzuXUHwzwQQau63xj5TbVHlHZE0XmPgQF7AEcq-S6Xt315kI8_IG9PjL_qmntcmOD5un90LZ5NeHKskC-kpnz019ZPTeJO7XCqgpmNUje3_XvMst3zkszOZb32Wsew9HzQzODWv3YzxacfmK6EgYONaMBxdXX4KvYWSRoN15Gi0r0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1KhZhl6T9TY6_HGXaie7BMGKVReAQUSIlSiFr03uY_k5iVoJPdwWk-Sd904dxgzXh8MNzr-lVwPCPHUaFOWo5GZpyxk4JwEoBmQTLNKCP88CHGfoPqNO0ORl9M8SxJQf6w7kw2pgUuMCF5sFHvisNEaldpPAR4xCFk6B_AflOJhljPEBC6Ois5YKA8pcXJTSnfuXKzhKf6cAi3GSWV2QrxEuvczVeQma7vtTtlGTl4ZDu10fb6MB-Zc1ge3iyewCeWKP3SxGtDXAhaMFrdwAnfvPfI-Hd6cnjlyafC-iSWiqcJdBaxLbjaqNl0vR2SDtVxXbBuDxy20mtjHRswVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iylQggjQ1bGyYjJ5TnfesWCU4MPyaYz0G5ZHvge8vRwLSgW4FRetZm0P49KxR8oxMB9l-76OHgckPAKXcwPsJmEdxkOkqAzAq78bxTVq1CLuyxh6bONgMUdv6GoOc1mpzWBvOwOdnkRJTZ6h4HgwhfqveCH3bdiRRQm0JsyMuv2B5Gdj3HBdOAmxn_Kcanobr5rLhKIP5ZMi8YXaCm9NUoynYcUwbr7gIbu8irCJqBsJmiaqnKdynQzpdkqOFyvLlA-Sx7QEbsZnGOeg2xzHe1IlNT3gwOtOldxw3_uD1cab0_mRKba_qjIgWK3Zd8p8YdOunEO3DwTcHtqa8C-YFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozp_8iYtohvno6Ctk0u8CLaG2gQFGcvYrYOxcmMJdtn9QMtyUkdTi9Y8xud7kKphBml41voKkSDw6J81qENJ9ueR0gnWZkEfKvk4UNdRhjRolEU4v47znvg0pBAtKGfuOhS-g3ISt1TY0pXKZeNM-46pMiHafoi-PoyddyB97glI_QdWjH05k6snGAAODEVofN3b8tM4jpS_a-B_grhPcPkcO3CfDUnjvNYNB1GRJcGombw9Mx5wWrvYsrNVFKMsyfSpWpHzFOUPnBSIQrQ3DkKxS9JGlnqmjwJ-MoPH23c12iQA_ACgHU-AQMkbCXF1NAFGbTLSItxlbW34c-Au5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeskKFRdVUw48aShdio9tH4eUSivhpaJjDdm85UXfiuYLKnzoQNe41IpoEY72oRp9cchorPu5U7lo7an7Efwjlomrm_E2Jr8JXx3MGJbCqUU9MgcebrsZTqa9bsgoReX_8ZtIMQ94FUxKlyem6-icNXU9V4_fNm-9ttgfQs5ZaxTs-zSWsmbzPa5aW4TZ5CEx299BICh39wzsdmZ-zbcQaROt_oWXA3qLq3V59LnW0RG8JNuyH-oBloOBOEvbPMMeXuukZDRo13X67V5JvERBuB2FcHZyjg37-wikUWEwHUN58Wp95SElHDA2HGidDcDA8nvEDsEAca_92molQDu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qciZb21VeJ9LitxMqweINlQ71LH8fDri5KJlR2-0NGxPOAYYcJ3W-mauE1zvABvxFz0E5MecHM4-0srCkWIgk7T8W3v3Fk8B7n0zhtFMLnpkKBT4IUJJ1aV6WyYRJlrKQIqPk1nMvavuMIB-0UTNp0gXprdzkYPw2NGFscl9AhZeBr5vKC3xC3MYuhAID8ug9ePBMCHprc2CVP7Xod3t49j8kpn_vzfyFArFJTjE7-vJO-FaSMTHXHC_N2syUQIHiYhfJj_b9btO8LpZiTPimQP3FzTvCW-N9je2a1uJIC0DtbXmulnFPm__aqAYqyjeNzwC9f0p8mwgZjhXT8atCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgyw72Gv-COZrnOUQ-S-EKvMi6PLgLfOCcHAUe9JmlRa8oJaEmsOu27fkUKTgSCdK4SROv_ZPME3mbv8cFVoyLNGmnkD4yjvSXcbh1iNHg8ymOeT5nqzdXnrZMNT-HQsPVDjpP6LfkJDCT2hk3HRrgQ4gYD4Ms5X4VIk0Fv6NSRiV5lNJKtiKUa5yQTw638zzdIfTFbsDyphNMjBxrpfm6BcZoIZABVyyO1cuOcltK0uXPRpQlmtaJei2QyD20QvILNx0g18k772Y7YB_iDM5CffUlwiHw6lUYPLiAf8YPrV4IDQHOEXH6Iq8daxqzd0n9gQfyET3Yxnpj-Bi8Xhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf3EMp_dDsntE7lQqORZBEwDiwAtgwEtrK5GKgafUJu3UKyylpxh4BD954_tZWF6JdKPyIOZg2BTNxlzaUKNY-PSUxqhK_4TLP9NjUQoNqOcI8Dwsa21Hpd0lp1yqTZeiitTt0gww_HY-c7DPiianL8dBd-wxM8K_fYuOuWhJTWvuO_hqXIpGBGyWc6JpoYlkpVK4zrwB8HAGSqKmxEhP4IZ7xitJDBJnnEDPpZPEQ_rX41lg41JO05-Hct43Kk6tKOuoBSrlemxaE8u037nOloK3mRUVpjrav2N1RtRkhzhq3MWdMPAha73cqvEPnMgTK5JiAn306khRLfTNswN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
