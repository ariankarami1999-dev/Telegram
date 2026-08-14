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
<img src="https://cdn4.telesco.pe/file/krTHVLfSwILa3A6ofqvxnbSmOUnlCApvw0E6_4NZE0nfSdNJwJ3MG9iRJhOXgYCGcwT9QMINZNpXe2q30qH9RZk10Qcehla29eejpochP9umZkX6MUk6gkUZVN_CbaUbWrJINHiUv0gh59ZLqm3E1fp2pZrbgV4BkczhGzNSVLBSVv7FRKP2SD5YhdqWHJCTKTIYTzZNe_c_Oem3c8wmKI-eTrTw59riaPa2uLGbBawbv8FUW_AX_G4kWy75otidv4XeDIZQVLdNQhxg-QFi0r4A3SHs9kO79Ex1gZJ1HeLTaORK0z8SP9gjz-I1P4WCFLQete5WEfsWv5-trPKsiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 637K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 01:43:19</div>
<hr>

<div class="tg-post" id="msg-27759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پریچارد کولون بوکسورسابق‌توسال 2015 آسیب‌ بسیار شدیدی به مغزش وارد شد و پس از گذشت یک دهه‌سختی‌دیروز درسن 33 سالگی درگذشت پریچارد در تمام این سال‌ها توسط مادر و پدرش نگهداری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/27759" target="_blank">📅 01:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op3NNYK1fmzkyDnyaKOKoL3167H0bBki0_uj9SC5-3P6_b7hpI6iVFzl1ieDHUnFhE4Zr61LgtxQaeknIs08ipBBB3Wwdj4qwfR2hKAYFgVf-JInwSnZhfjHIexBcmU7vtOTBfZypKZ0sym2A_iADdGMY_z3QUtWKmnDYOqzIePLtTh05CSuSZ70xgmKAxNYVfYHOfw_ZUg-JdU7EvtpVq9ocWPd_iRpHKqRvPufVL26sT_NMl92kS60zncafQ2gojtvka8p0CX4sW6YE94bJuUIPgUZM-A8XcYfiB2t7rJDvvAqxFMsxn-JzR2fykmr-cEOf0ipb2OJT6tlqylqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/27758" target="_blank">📅 01:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27756">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl-su2kF-lvuzP3244zvdTXx4GA66qG8s_FDSrbFloBn08Kg4ZDO-ci1iCwUzIxK9_kyiWqS7DSHuGxAH1Ms83_RHxK2xelCyCK49J2ksAP-pukWTJDqcS4raxLV0asnp-1g5bUq303NYYVU9HrrXbFOtYEqZlKhfep2EYxo2yKWnnxvGrvNHffRu16mWmmY76B4qWiC5tAULgWOP8E7jmTy82Xm9SXl2z3ELoath3tJLMpFr6EHKD3RKwlJbCalJOVduyky2vp-rgNKZukhd5ObX6okMpOIHpAZ5JSrVnSDgb8ZjDw_d3MPoG5xV5sP9fJRZMMGBhugSRc3g1dCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/27756" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvyReSWjKoDgwtGhxPZuB52ZGjw_upWT93FbYsOP8tVvjammlcPuSq4SRnKX2obPyuMVGibfuNFSSfFrH_Q2nztPJOZjWJNfAAihMQ45Qfcp9qA8P-qjaLWgZQjg01Rw1t3tHxeBYxAfRVTy2Vj7Fa0FNc32XeDekkBOIAywR60Vhy7uCyL84pZ4HKP9XN39O9wheSQgKG7jSjR8JwZeyuCSTjFE5q7mkhUxHL0mWcOJo_kQIV_WIxsuMK5W5bk4mCVp3UqEQff4q54yXmhK9NQJPQZBs-TgIIbh9rWfvB4LKPzh-ByoclHuglXBIYOH88G-BEhsp7D9rWA-SacZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برد پرگل آبی‌ها با دبل سحرخیزان تا برتری تراکتور و سپاهان در گام اول
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/27755" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K48-X_Kb7XwKI_LTZpOMaSb2QNVeUNRurYT6q4MfhTH2jayF3h6b7mZTQX23xlkblgkSpcRyjofD__X0x9viWzZc-OI4C_WVo-H0yfwHQLglgNbzwaESind5-Ye8XIAZ6l8iPLjk8T8G-aaS541HvSHo9K3D0fEU__gSeyZbHeuookv7_Z1vrRg7k-jnlYYaKTUhAmhWXVyA2T1ok5Swuu10j6ikFOLkdWFP131k14Dv_gaUSbUZrvcGWy1J4bSGtZKfoEmiyeFXCw8e4rLfTU3MsT6ndr-4MGd7TZQPzbMzmmFTawa51FGP7Gnkt_zi4XhuisaOMFqmXDyHtb12eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شروع لیگ برتر ایران با بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
شمس آذر
🟡
✖️
🔴
پرسپولیس
⏰
فردا ساعت 19:30
🚨
ورزشگاه سردار آزادگان
🎲
با شارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران در صورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa23
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/27754" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuiOT7FBZ4EZ5-ncpovnASrctCvJIgMVZWDjwx_LIT6xXQgiI1qqbM-nIs0mUIKiiZywZi-MISg0Q1IYQRuT3X92DpWQqFN2BL0EdMolY8wi0kxpRr5btbk8Z5LZQX8YCRHU8Tj7Cy1qLwe1Ue7I5v7oIEPj6AwgS2isxQvQHOxEkfonW0I-haruUWN5LEdfPMCS4Ha3NE0K7Ng7qRNnB85NYRsOi0OVl7aW-8XmNAmda5dA5tUJWTFIQJPv7zehw4_OxPvGUezust3TmoMulX86sPo8yTaAl4N6t8kTyws8t2PRswtDPEvh-LtXAbhCFxf7Z_7Y3rbqiRYc6SQoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/27753" target="_blank">📅 00:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-xvyVi3SbLYN53iO7zERgLCDZ2ZJC99Ds8zi25LgIAMTc_4ha0HtFSy4dYVhDekxc01Ht139K6Oz1NIuU6kUZYGT0ARjJtajCpor-iU8S9dtKHEhJ2jexNrWsJOiKG35bFi0xTxAaAqwEgBpKKH48I8SdW_fCDfbYHF8JlU5jDhSjMQEWkzK6Yrkye3hs98qvtljlSPKNtdr8WZKt-P7I20bHDz41unWwg2Lk47yB3E_iSzhNMq2qAgtuVPZN4K6JsNmA82htPHTvozMWugp75xkdmRfOCXIcqRa1NsjlAx3R-KDO06YySsOAtnAFeKeoiR-5IVpPvghrv4UyvHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/27752" target="_blank">📅 00:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLA2J1V6BrzHMFm8htXoeCZ5IIyB00QSH_CYP9vzNaspkIkglw1XUWaQavuPAY5TRACnl1CBkZu1twBYnyqoNCF8brHI9B4piosAOC-xTxSR0gCLrpaWId9oXUqWB_PIabQhaUq73tTrLrdyUhbzhptEYDm9n2TfOBamGM-T7w4f70pkFujRYEroJKZdYrqXgNCElOXOp6qgx8c4U0Sb4ytUoJ5DR2bSUJl6UOAVZfZEVQqoYP6Y0rj4c4hBYbQU1bBfMjhm_3PEO8iy_fWUC5kHbKvniYcsvf6H1dituT_KKCNctjZxjkxTTPAuj8MnOnC5aQxBjZ4KuObjrYjSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ رحمتی سرمربی گل گهر امیر جعفری مدافع چپ خود را از لیست این تیم دربازی‌امشب بانساجی خط زد و اعلام کرده این بازیکن میتونه قراردادش رو با پرسپولیس ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/27751" target="_blank">📅 00:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27750">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRMsM_BZaARA7eMktjae2yZvxEVG0zovG9MAxnQVWW5ez6rqjeh9rhxtvH2fjchQ_xdUkexZbZht0gvDAw6OXfRpW4EXPNw_1_eONVL98u3jjNNQyp3TtKOTU2tuNkSJdKFM-D4DEZxhcmuLTE0n7wjkLrSHLFKnaihp-7viAQLmxUGUcQRffSkdxhRPRkWA6V7J7-Cy1v-VcmBu5ntt0iSg9_QK4VByfj6ZAfATwholike6vYbE0eYf2LfJqqZ6X8BCu56cpumh7UhxxG9DBx_YOpjMlpCnADKGpFzCaEbvTKedmQEt0rsXJhv2WYAcM6Cx2jN5_ZAv0NhxX0VkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تصاویری از رونمایی باشگاه پرسپولیس از کیت جدید خود در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/27750" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27749">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsxTuIS7L7nsuWFNMOcMlA-yqEkRBLyuIG9fVVEd_HZhC6MIFlBHEPW4M1TKo53X8Fjb7e-LmXStm6apI4QH46HsRkfpdvT9OBaGgOBQ8kXomE_2OFSxxlwU_NvOpsErIwyVKBEggFNjmGCxzQ98m84qizJ_YYDMgUIqDV8gcTGGb_B_3FqwSI3eqth2oij-u6EeDoMfZnlK-cJxsol_4q-c1u6XQ9ltvUUKSN4i79e_4_W29jBRtzJ84HsiR1DevK3e9yEF2zPrTKoQ7TUAFMr3hg4m63Tj3JBTooshiPRPf4sj4TZRYv36n0Y7LWhJkfE4O04OVF0xRY5b_id7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ به احتمال زیاد بخاطر بسته شدن پرونده داکنز نازون و جلوگیری‌از خطر تهدید شکایت به‌ فیفا مدیریت باشگاه استقلال هفته آینده با نازون توافق خواهد کرد و او به جمع آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27749" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:
اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/27748" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWyvciNKwdXd6ZLeHUiktHHlYZSrXl8n7bJTKRKcWCCRhFQQ79sQ8RYaaJINdhFl__GflVjEUvsuscNTUdTNsGFy8fXavizU5_tvWRLUcbNoooUqgIuh1uk7jhukZjd1Dm5foj6f6NZQVU1qiImpNmiPAXc5mpuwDKaBtLR-C1fup3TNUcoGNF7_HTnuN-oaiSNXHUMbUVpsffEc-Ni3HYD1F1ADtxRcZbMa0kGjDeME4yXG9QdHhkXdH05OgTVjkqaKuh_8VsTfVQjPwhUJ7E7ztMeOwbWGsTQEmKvjVJeTHePzbZNXAt2qOrJfc1GfVXWJBT9ceE41xBZfGYJOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHASf1AyKSECVI4JiHr9IldFy9fb9iRAKYcoCOyjwtC8CwhZieitnM44yeNbizEHh5R0CH0oihOdKT81GrWibnDmD1OROty7sc21rSaMIch3EsGP9CsHXLKaC2JOwSzJXUGzk0gTW_YB06ZAMUDgEofVMUCTDnZK3XfuouEFh1ixtSlnoBi4OjbdbuHiLPEtbWxvQP28oTzB_5tZkzs07zxee8xxSoKQoPu0hu9-QuE5bcyVGG0EUaTOhEbw13HWjLPpfAMZkdi5rV-G9yb7miQaTHJm8PLUamPYqjJV94q8JOwey8HvAX1vLAYZHRU8wedYVohUSVYMw0MwNF491g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/27745" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foc8G1KxWxP9C6z8W9CXYzQsxwJ1JQcYO0Idhi25YfnN9PsxW7nFKElYhNQoD7bXP7srUwmmgw-BGbo-bi17ozxP_0esVqvZf6LawdG4M0Tp0IuXJ82Jc1arZhwDm7wefjtkGz5upQukcjlHR69nW_mW3uehxwTsQyCsmvjWb-RElBWs8_9HYibLhThIQR6tQ2z-K9EnbFNHRET4KhNfJZDpbMX41k4CTnY5lamON-C4Q9LQ3i18-GW-2GX4e6HQGSJixb-GTAetB06KPaD8GrCKlubJyRiC9uY4i-8DMNJkwTAmLd5-Ma0HoI7iVl0qLezKwAQv91C8KJb5xpQXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده: وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/27744" target="_blank">📅 23:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhqt1Jx92yzmaKr6TSUMtLvFj_BuUDbw-OJXS5-Wil1XBaIZ6r4EEW8ygur54ZTczfP6H0kBmgogiecgFM9RUSdJF0XPwMOGM7r7d0hIUQW1oGv_nYb1EAg37tQJ0-DfNeNtjIWcLDvAFevFG5vscUWF4yMUW_1lmaImml3navax0vygscB4vwzc_TpI7MyJlAdHsuzm-05s2As1aXtAGJlEV2J2h1Aj39LAICBmVDz1MX6HyGSVHLiOfjvDiQ92wrumVh-tBSvm8Z04_FoRjlR8D7Smo1GZfRK3bvfxEE7zmIdQIE8VPm1fOHxnJ0zkRExfey5N96mOEzq2mP4UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/27743" target="_blank">📅 22:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27742">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsoLlcVlOvFmwW_OjE4nPOl_vjc7ORxvZSk5Mj2zerYb33fhhBZYS9Da5Gs4gbbT9dizRzZr56GcMreLLIZ9nXxL_rBlSh5kYni4WwUasGGO6Y0Xutu2Q-PUSeu64YMwdHEHh9bRy7qgroaoq8YyFGj3cZzoew8QHewvP5SOfnX5zCa0DCkvMoUX5MteYH0-h0GFxXAucQEMbE86jj8Pt_UeaQop5iVN3yEcCLrKI_W9HChSKRFilP_dJoUhCbq-lt-Djnq3yYxD6eJDiUZpVjfpZzRc2UnpX5LAiIdQs6nz27NMJJa2J34XPsJsDV7GJRxx0MnTnh2x0jRXYWvPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27742" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LslJ7I51H6UhdRX8lJgFh-c0Q9AxYHCOQS0pC7hW5qqPkRP3EgdLiTng2PbhpKzfj1vOIeeB5KCZt-4TtIzUX384jA-lq6GNC4sdnZzR-AoF0JnaBJMhmqyAayXNbB9UnJDD8ZclY1jC0gTus2p-QgWaLSgSxItv3WOaKZecA3x0ZqZeaURezCH2URQap8S6N18rfl47xQfTRPBe2ldD6s8LZRKKH7VnO15sNsTI_Huqkzo3C-f2042v6joAEX1SG4pgZkhmy1agmQQDVc0XnhJ8UEbuIaLVmmoCDzfZq4QO_xpqMofS1D6Nuz0zjujrzr18XZg3NgLM82LFhmI7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ey2MU57BgYVEGTwUq0shWbUeyWCxrQlsfqJqd0lykAHwwnW5Tf-iu6II-PDAAEItj9sFhF1MP6aAn9h1qLAkIxtorSFExYdXt5Sa8BArhDu4sLow4tU2V-BcGsTrmhc3HrfvJb1cXoNaJOm0Rq3hdF2LC0mheXVgZoKNRacy_WVHHJwpn_4Ksqb3Hm3SuurskPQuxl9uTr_3kv2dJtisng8bkFfWoSjJQHbtWDzCnlESqj3j-APrSzuNxsdf3S31cbyhdIoTvhnX7g_FUCdciRgDq7Uwd3KB1dSUs79XB_t1vOXTx1XMLfjQga_4d_kOww42ZfM8zaICD-O6e9rV1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/27740" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxEOEzv9YiAnaHfbs_dIVKsPK2zf4CHGbMQKcvmNg74oybQ0jRjLHGbnh3o8lvpsWUPMkLC-99U8NYA5z_bbQyvhtc-UqeFegWnT-9Tx0-dvJVfNIyIe0i8GjiqTLPBApekwhFothp59vA3sYMY9hC9b19R_csFXmIDkqDrlggWA9YW9ozm-QtLu0Ds-tMZh6g48-QOXQzffxDqAO3ctQmVE34Yb3xM3juOJwwvwyjBJKKxeTaYWvq7gfpjCfFeIjCdcBNJhp5YZsVjh6I-NRbvtz-Moqm6Mfyo7Tuduk1WRvyGSnufmFQUt1ONMBfyDMj9U0EqbmR-XOIV4BqJ2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICnBi2_CIUi7uTSgzyHHEMumWR6J47pkHN21PtU-uf-3hPmot_FsgWAgD83_WNZVf1Pi7l6kGJk0HaWANHTKztVrbK-bah7KpkFEMlDRB1XQm78ioKoqj8ARt7YtS5BUOP8fpXgeVdFy77Dca7ZQi3zwL9nlYhDbs5KMyDWjPpZkfpEaO_0PhG9SfoV8auJ1dx-lGN3QcO78vHw4D7aIe-TXRcNLTks_p4-Owu_FJUhSx37OyAkDT4QZ-CxIMA7-sGOFOJBei9u2sZO0Z_pIN6IxYR9DFGOfSH4q02qNCcf2rCFrdV-RX2uehGJ5Ev_SrcMrw8Uvu6NPq-PaGBQBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ سوغات سه امتیازی و ارزش مند شاگردان محرم نوید کیا در یزد در گام نخست.
🔵
چادرملو اردکان
0️⃣
-
2️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27738" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27737" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27736" target="_blank">📅 22:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب سپاهان برای دیدار امشب با چادرملو؛ ساعت 20:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27735" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-usX5anndCcTf-m5mcCuaGIoDfWrD6XiP2RaVufV1SXwn9op-injDkC3flTAu76ftcxu7h1OV_UCIAt9Rgxy7Fep0cK7F9ehPKQpS8k-K4lSkERrtmuw3vsciLDLUj01TV7D0dri3ZsmNd0oer96X-hbUryIxCPn1wwMb_x4NWDoHD0DRvVI6x4oIlV9WGWBoGe3TR1Zir9HFXrMmvNksuPAzUBM9Qy5BHdpyO-0c_aIDEfj64EhC0oLHRnK2T-tKZCPV8UXLvAj-MlHd5-_eR3nqxP0EywHcFjDK7DoYVNSQNyCbqUURX0A2div0q9dCAxPjnPNSLMdvByiTDhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چیرو ایموبیله مهاجم سابق ایتالیایی‌ها و باشگاه بشیکتاش که‌تابستون‌سال‌گذشته قبل از جنگ دوازده روزه چند تا از ایجنت‌ های مطرح فوتبال ایران تلاش کردند او رو به لیگ برتر بیارند در سن 37 سالگی از دنیای فوتبال و مستطیل سبز خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27734" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9ewBlkAGQGdXhJavFK-tThNTGx081jj_1EolGgQPjauHhw4JzEG7ny7ydzzXBBRBqqlOtYVcv0YSSKDUWfyDhlKkBM9ZKEYTag4t0huUAl0i1_O6BSWDlW7pxIf0xss9BM-1b3pTaNZRSv_2YTEvGBVLYs0SLrfU0VW8nYG7S-5wd4w9OSHFPsQ4Zd-RS5gmJ7yFsOsWoKKWCijpXr6M8ndf2yysPjwONp14DI0nyyW4MGPK9j4eVeLx-jPx5ARG19qZtSCy8nJlEf8hirrAvJtLkgRmBKXjW0VcXPfs0Q3PH5hNv7sB6hedMSgW9Lb5cT6nuDxwgQrvXHdoeue_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های رسانه پرشیانا؛ سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27733" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDhEr_47bFregnQiNqwjjQ2RaxWU5qyg1J6KQwmAiwf722xKVRUF2LdL83BSfqNoTg8DU_vsEDvjLck2siaVnXqKHKs37mJnVJSdVwOrnHhNIzuTYsCS4XgkXRIb8RP4ZU2HeSx48M_XPn-onyA89fiP89GIv37dbjYYg8kHy1ZB_4xzEa4q8GvHt927mrOapiOcfryZQb8DgRn6mY-5seGhZiv2rDT4bw4i4dEwNlBdPMznkZ-Na8tFjYgxC-xgKBkS9laOyr2xURxtwI5rLU5UxjJNBKbSeTbZSisvhl-OKeW8nVuGasQOPjsL1q8rgoPeo4jAqVJWBJZmnICDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27732" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27731">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs2khp6gGp5QmqDbABQ7Fc_DlhpMBIXs9wwgQDHttQLeURFlA0ZlA9BS5cA3W1EMzu12eo67b-suDkiM7MvIi6optLde4eEQeMrHiV_7OBjoqOUqFFUwIzWLPLuf0tBbIPLqrdz4ixeGAAWIY3CJZCtEoWO78ezJRyKLJd2AIt8LhGeMNvrQ_QkvC30if2OP-AytXzpkeh7R4J7S4z75g9Hb0Y7ePVysy2XjPvhgybWkJSlA5DoI89BSfc7SEx2uIi0kr6eizVBlAdKM1awlt4BohnWGQ4DPwLRQMtjHRn-xG-uGtMbkcuk4ahVR88V2hrOAlRr-niGgvwHCEROQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27731" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27730">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تازه‌واردهاگلباران‌شدند؛ گل سوم استقلال به مس شهربابک توسط محمدحسین اسلامی دقیقه 88
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27730" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27729">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27729" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27728">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27728" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27727">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27727" target="_blank">📅 20:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27726">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWpLb5DNLoncxxuJcCLh8u0YBzO081O7-R7y1gHPoYk-870JBc4WMFJMKC8Nuun0lu72zmnlK4l2JjXPk_5m9zVvdZFtFPgVgcWRl7Tfx_Vcc7voM1BW2n8QmzJ3n8ObO-jJ65hktYXILT3iROOcA70giwQaOxiigLcKAEs5Aw2T6I2AtHSRIGf_DlCA9bYoqRQoOcsGjNUmYPNL6QWtRJOA5m_7dNslrzZ_dhGL2bg8vn1QeJOQ5AzTebk0DyK01qVy2bhQLLPgmVwul8oH85MEvm5ABSCi9K7w1koYtxXr5VTLZ1Y8naQMgAAQdO-bkHzX-4iMfwQb3AzP5rff4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27726" target="_blank">📅 20:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27725">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27725" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شماتیک ترکیب استقلال برای دیدار امشب مقابل مس شهر بانک در هفته اول رقابت‌های لیگ برتر.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27724" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEE-qxsOgKWOcJzfxYNoXbaTGTwMYwlXvBcnWKBXOAMlM4NegN9rTGrFthoLEPOE3qkNqcy2WTjxChCvnGo48h0x2BiPhYddpHdYE9O633cvHUdqWmcnTp6Z5SYzuGQqjROOwQoo5FP0ib34-s-Lh85eCbYrXXmt73Fp7--EuDYKFyPx-rsFcpBtj0v3XNG_3-9mcthPMdD1MLEBI6Bsmz4CmXmBeZHrxepvQfQxfq2nGpiHjVjxBwzPdRzIusuinFFtSvqhowlTa9XyfG-Z3Wnm-QiCcwKhk6yWJtFhFKM3dhWhDs5z79VzTnI2I_-d4rvP6qlWhK8qmAieqRopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ستاره‌بلندقامت‌پرشورها؛گل دوم تراکتور به پیکان توسط شهریار مغانلو در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27723" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27722">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TupqVRfSCGQ_ecvtE31yyPS1qxu1bR_x3JWkFEhqHwjXFuItjer4CkrY_IBNvfXFqVki-3bLdp9Xg3qmIdBSHwOljh_HWzTbdJPD-8iASX8Ck8lZoL5PCP5JfMb9nlQXTiEy_QS9Yb0gHDy7OsZlDG8mxqLvNkv3wlusl9FZduXMpuaS67d-UZW0tkCvdETn7xJah4u9iuhncMjtwvm7_moqHPDuWeELpt4mGoOh3axZ_0n09LK4FGWMHq5iCbKd7l4ySzRBASL4B--oOe8kJhfHuTjkZcKGNN9Z6Ra_45PRq2sp2E7id4d9oyUX46ANzFu-Vg5cuavRs58X__w66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27722" target="_blank">📅 19:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QoJaeP0qO8oe52OlP59D91nUwPpPpA555bWeKzEGiAXV1gDfjp5-7UglMpsTE2lJTV3Em35CWVqhkv-sRszA57cMrEjxWKxHUPrpZRLfNw_8yF--4BrZbZfn_oZeD5DZhux8SlTtkX64sK0_ETdMRojV10TUOVN6HdDsyKnp8qqJqV7VvT4UrJYpy1XEKl6M9IKYOvz5jf5_rGqtaz4Tzq_v4QQxaKEkul51TBgPEfEYlRpaflcqDRVKbOEXXKh8tozGViKhsk9arvnO-lnTCOMJJKtAscLU25njfGxQJ4QzE1mhn5S3jZ9J9J3gNJCIkV5swb0A4TJQkPuBoboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
همسر رضا جعفری مهاجم جدید سپاهان که آماده دیدار امشب طلایی پوشان مقابل چادرملو هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27721" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIYQX-KgAO2QNKHn1zKJ2-Z8uYpNcdDn3KGWXTNuh8l6UAHokTTQLz-UQxkrtO6eUexJcrXYRy7ItC9VoyuHDcIWhd5NPZCaVcO0iE9ghmlgCDViHNpbvw_UYzquZcXqKG1iJruqyzy388EdAGnk-e1LiMhcxR94mTPQnHZKGE6aD7L5pQhFQPHIROgK-mpQmMSvx2KLy4RTUcLaVF0vFh6DMcDjJykbpbmsvy-BPnMYWJSf2BSN5Az-_PVO6jOhiaEO_6GsrMQIfg8--br27o_Tc-FrgOkRj3awnhmmsVQOR7wXFAtEmz591EXYDjKCS53s5WnFngtC-f-if_fuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو قبل‌ازامضای عقدنامه؛ با جورجینا تفاهم‌نامه‌ای را امضا و حد مالکیت همسرش را مشخص کرد که چه چیزهایی به او تعلق میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27720" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUUoZTyzj9yvMHpI5NxXVpN6wf9eavJfpxA55eilkwyII1P3QyU93dO07Au8usEXaVTJEQ4QvNPDoGXXyI-piJyLj04DdsHMGWEwVuUkFNhbA0utO-Yjxh97KcYfTnu3VP85mwlIFeRpzIkgg0lqNKhRARH9hVf88OCqNgWeRVf5B79yD-t_W3Mhjp8h31PrC-ccTePR4vcM1dAcZXelG5_v5cnxVNY2JCZtDMgWNqR-PjtYOmMC0nScNp4c_rBO0dOpwFrCzi4vUTaduPB4o_8SkNjrTlZ-oHSZjCNkxqaF6wJsmGp4t_f1-OgV3NDhUUeK0nXGJDnHMyyjrLkhSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب +15 میلیون بشی
💵
اگه‌نمیدونی‌تو این روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 10 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
sg23
https://t.me/+q-sIylsuFEtlNGI0</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27719" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osQPpvrGDY0pSuRECRqlQJSqWsyw9KLMBRN9OEIYd2UALzdbVUeC5OKl0_8I62gPJ3PQwl4SAjEs-rBHX_83eeLFyrPT1yQP2Ro7gyYv44NBNnFW3nyg9qMpMdfMsrc8bbPzZxWEbVCyZdCxtBQLMRDthMSAHO1-uQ8fhCtHopo2Qtvd5VOtjuJl23Qgj9sIniwp1-YD8A7QYjSEfo0Zth05r6YwuYzbLSsKACb1tpInbKX7E72_hLU-BgUG1_Gsh1MdbMozkr3tDyNidn60Z8QiCLDQDkdA3eaDz7r5-uZhEEl1YZwqdpfKramUWvGHw17oLGu1totWu0s5HgzaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27717" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریار نیومده‌گلزنی کرد؛ گل اول تراکتور به پیکان روی چرخش دیدنی شهریار مغانلو در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27716" target="_blank">📅 19:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تراکتور برای دیدار امروز مقابل پیکان؛ ساعت 18:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27715" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILRZ32amTt_rPPrXspH8Sv6RQub176K-tdCHq-z7Z2wpmJgfwxUam-yf5p-A8Z8-fLggh80s1dB9T9WJwDrO6r7xBJkevWAjwC8F1H7qR6HXzUtkn-wxX2lla34dM_q5ejRzzMmsBOn0IQcdso-6ahWcb8pDMvIqBAfqxfHn8fn724or0OVgtnQsXK3W7mC85Fz9uyXfUk5L973DMsLWKmpz5ygL7Spd2b3z2Y0GOzw0tQO0ycYDvkRA1_h3ra7H4ufjUIlim2SnRy73RIeYU6orYXY-SlrgIa81bkhVXqLt_BYkYZJ2952-xsQ49S6v9793o_msMTfC-7DcGVS_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب دو تیم استقلال
🆚
مس شهر بابک؛ ساعت 19:30 از شبکه سه سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27714" target="_blank">📅 18:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWk9OEjjpbvieowWLwXezTpgzMZEqTpChYABHkIqEwzJwuNBpfsrnlsRNEM-wXoRVxBhftaXkuwnp_SSHZx17BRhRQcUc02ely9-DAEUpz-W-1aFkKZPW--hAu_96A2YY8I_B-PV3GNoOedevy_uBjC7ACOiRUv4Vt602ejx0I3g431pILZXRjNh-7_1WK3b6wvxwMoTLY_J3pRypRfseOgYloQA7EQLPNbERstU5JBQ1_thzWqVzF6k8_tDdm_a3dgLcN-w_QiJRBmLye_4MNGpQRtoQQtxZJNjTyRqcR20Mnt3XMJv_ot3-l2b2wBzm1CsAD7WT6UBryawUOcbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل تیم تازه لیگ برتری شده مس شهر بابک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27713" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/27712" target="_blank">📅 18:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR0sje3m65gMjkS_GHSWGuLWhBxM-9gItSJFAPFSun1DKKT1ZuPkW0oNyztBgkSn52Qa7r1rkBKRwhcyPammqIpRjiXgZot4b301t_hH1YqTIEAs2A13-QsDKGIEQ7bsG9msvBBjQWavMMHnpO9U-H31ZRWoNG07OW3SVnsNeQShkOKfeHIaEOCLclL3Xnot0IOPX81_EbSgU4Gw02_LXhugI_-VJuQiPFOca8LFf67mbyIAMgeNxnfseBZZ7__O6pc2aov7q9TEmvkuaP6-YM3XRDIZdQKG2h8rIRqGinrwqyyo9J9hdc54WWZiFnrHSsUZ1YPJZtMlGKy_EBKnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27711" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDGRwbLvii5RbhhN_f0SAp8hQs7IxSSf-0_s5_aobkM8FGPIikbCJ0_UV21ck0ILiyENxluzbsx4kveCG6XEDm4Qka4uGA01BlVFVMgN_0HloXjYJbp41goGE2xj6YUx3-N2A8YZpdE7sF_ddTGHosl1-ZyYWTqYCYCW1uVP99oJcgh6FyqkvBmZMHPmMoyJc8MiXpuc_iknqdSb1jBRXixVSJL1Rgj2lkj5Z4F5Kcndaij5IOTUKmWqneFvG5wDRngyOsz4mqJP2pSltE8rI2P0UAdP2BiohPdYUEJNIOOdNo546tCcCDmsiAaFgQ88DhGlgIACJH_zRD7FU00EsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27710" target="_blank">📅 17:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iza0cJWDzS8xk2_R_Zm01QK8AwcOLNX2NTtn30JR3hqSQ8YNWDlg_sYSESOExQ1ytREkQnSw4hL8_RSSj9HlsTdYz89D44Ch825Wmng7xWF0Mji-Hq7khhm5Y7329-44KHOZK7FE5XSv4uKWxDtoK0HeleFmRn3M2ZgPGbwWe3tfxadwWl6N2ZMFM-ZiHTZ668izm5tG5gDwS_g3n3n4PWWpqq_ISYYIfcoFRApLwM9UP8pmsiIAO-4MKqvYQ3U4FLgTYOYsbvk7-Q1lVAYLgpI1rBQBDBrJG02qMJ93wWoMBRhHUSsOQbLAge1nDSoU0AVCGjXQiap_8GN1rx1Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27709" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27708" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYAeEoAZ1oy9GeptIt1VIC1u1kCYTgb4rYn5DNXwqrn5nA4qShcke5HZCrUBKTwC4bOCQF1Rcc9RunB7ld5Ybxs4CQAAAAqCGa17RY_3R-3qHcCE0hJS2WFwITD-4QgTZFhXUAXlobqo_wuSKulfRm1Jtw7uhy_SWTJWnbQlJN4LxupUrHGRXgZ_unwqaevt2ZWl_8D9PSzPQrVVy5QB3pvbA-pMT15A61cvXpTFSTzGZ8w5rveg5bKZG-3hxbCDRRt6UstZ7tgiDf6kjsEprzzGcIDSKGUkXLDP6cfK0w-rq3qxTbymmguVtG5pPnmN0OPMyiC6ciOSUU0CvBphEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3g1pvgLjCLi8T0gJhaun1StvGY-IfGBkdQVfkOWFTWOJLv5gYs3YJ3S7azBWqmtoQmMv0bEaWCM81RdvVnWatnYNohvJuutxAx2j4ERroRWtORJmAPN3zYfKNQJRUhF1Z2ouANxFC2WnSRUK46Iq94BLYU8kw_nwiaJKyJqnTK9O4NNCsAhjZq6wiMWB9nyyJSLa2WvMCeB2wsBNFo2TUHVuXfnTJICEHVzZgvhvGTgtK2MB5FxfJML03Ox2oLJhWVnk67eWS_uS5j0a3AodPtXwgPVzziKsro_gQTJgmx_k39r866ZXbFvhxglBmlzqFoWJ2NYEqK5rkfQZlwzUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27706" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erDxQ5mpLUfynsK6AxUJoqRD7jjYi2lGx41do4DrUJZRWmz7AT0b_ntubWLvmv759rCniLerYfBvRpsgwazZKqzaqNZ_YFzIYA_Rf9mF_cJIYFpZgTNJMAxodMXsNmwqGdwRESzE0OIa8ezdbLt-gaxvZ7bVp8bCGhfAeYHSkUTL8QdEdgJrIYbTuIYmH5VGyx6ucHEwpkPzTb2itLzU1NkxC2UOflnvUkEm3oTTocCJmKFas8Xbe4rRxiXSk62pzUQDwuJYbWVzHanlRL_AWwIIOvKY4fsznDpTKMFWxgvZI77B2ge38-Z3Gy3FFQIakyu9vSu8kxVhNRj9SXfrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27705" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdmkrCd2yNRNIrexa0rB9zfRo4RlllfnOZHNUTlSz8FsJ9XKWNMexPoVuEPl9on7gYaosnKH3MuO3hxmnYH5dHbI9mQSuYJ-VNu2lqm_nO4beqDOp4A9HlVYU-WNctl4fm7rQ6aBNx46WXPHpGaXYbsoazcd6iutv8e1mP_jxG_-A1rCNlXmJskEjXPVWqPMHSdPBw8fGAGKex7qNefRBEBWUFt40AnPSSicSw4nl5wYOAgDOZSbhotsBOBCq3mubEaH7PsvsZQ9U-SwIA5yEXIv4G-Qu-R7MaOcv58YTqrnWyopXdePW_MBgynUtY2MSRzEkCx042UZx7XlxMHkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
چادرملو
🆚
سپاهان
🇮🇷
🗓
جمعه ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27704" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuzgNFPAeHxasJX4bG4mTpSnVJoNUtD-Lljb_DZeG-GBVnfxXphIhvvq48C8W6OwdDfJoJLI92oM15veCjDSonVZ8XkV3YA9qTdaWKTB-S9TabMAaJG4vtyE09-P2CKqq2XFUMRHG0D4Medz1G7IvScJV-tufEm--K8kguJk2z2CDY8Eddr5ryaZam3-DUsQOl130CPGURY-9uIX3mV7a2HWWFkOr-otIbWyWUsp6QkAAm26154RdnFybE6vfybjQkjCtKf1m7UwULGi2uxuzyJwt4BqnVYW5KBkChLHkzhXlXQTLI1IvJGJWiz-xh0N7Mp_ltiYfwQfewTQJyovtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkITcL7a0BS8mBzM812y0o-nKVBJrvTd-miv1ZXTaAFbct5natS4iy61zQHql9iQnp46OJXxlu0Qi7zCiKQbNI6m2IK9OIfW2A-r01dwp8kNrCzQHR4-p_D2VcHEXRNNmvJxmLDdfg_BTck7siUYMo08DZlP6k-yZ4oyHN6mNe4Bs5EFhx1Sl3tLnqRSYYGQgSHE6J2E04WUXyOBIpLsQBLzjOnBaQIVi8ED4P-qOh1HfS-rYVDyrFX8zd1ahh97owaViqB3kiGYJLX9zB2cyvUzGHsQz4gmpEALNTDEz9MTt8ppVoDKsv7NTTbJ8bXy2PnYlAULC6lVpPoUgyK6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
ویدیویی از مراسم ازدواج نادیا خمز دختر پاکو خمز؛ خودش‌خونسرده ولی پسره چه استرسی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27702" target="_blank">📅 16:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umk9hbz_xeg8GZ134cjLecpdFSFbINSwk-M9rg8CmCM1cPvM419vz0TAOGsjbJomSjrby9GhCyOUaVyWR2_TxAAZ1wn3xMxoQKJ16U63gnbiUULrnyjmCshOBuDsQx6hFZdOiFk2HUil1uvDG8H4izsrMc3EJS_IfChvb-ZSKcSWXt6fibF6-Mzcyl_3NtbWKglT7B9klR37Mh6GpWrZm_32HHFxCoD7lj2MpiYBJLOwoXchhR2m2_Sua5mYv76ARd84a7LM6KxHOggRiZ1xrjB6U1kMzFs9SAeMU8XOTCSnxQvRX8cvcGTr2r3eUrHPR5LlF42AeyoKHB--nhl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27701" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
🇪🇸
🇩🇪
#تقویم؛سال2020 درچنین شبی؛ این نتیجه رخ داد و بایرن مونیخِ هانسی فلیک بانتیجه هشت بر دو بارسلونا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27700" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1SdeK8MgBmjVHpWEgNqWwxXKUgCV02LlVf9B8B5BYOqtT-5EFhwOxXKAVGnhiaHcJ8PxxloeQkCgKeoQduRR_9Aqib9y234_ir254kwteeq73tDIV4FRNNx_m_hTDygv48Q8QlITN3WhYgRYLWPvHk3KXd7gWnL4n-G5tKt5HkCo10OOA9aLMN2ZHgemQZrgkRN3Mg3cvig1BYZ53sk0cb3s28tqAGPeX6dgPChJ9oeHrEuZ_zihRf9CS6p0GwnEqZMu84U60Os6xts0hCQRgvIrhoV4tG3mpgUiULauIiUuXedkfCkyhlAaBvtsHBPUdJHu4ieEz3GCVPSQHTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27699" target="_blank">📅 15:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27696">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWrBvLyXetIR8ex8ADHX7jfylzPMchPrjc5CERIE0O1DvR8ppzIzZYKIbOMwYB00W5igkphd1oQA5yXhfdnXlIfaW7o855fLdbuQArFKFNnanrQu5TRUUMgf9WtRnzT0tNbzABXS_q6jeo8iZ2twq6trrAhqWGPfOw7Cocet0AV7blKgxP8Ta_W88m0eTNFsmMiU5wiW3mLTDtCLeM1skQlr3MsFIuZ3R954kc30Vt8pSRRukWGiSK8yQwUTaU2uYy_HuCWMvHlRkaD_D8FARtSvojKPaXqJsGPsWqx9qPCxl27Fdttap8EhEgM5n-CQ5xcN9a2vY1jr7FwoRfGEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ به مناسبت شروع فصل جدید لیگ؛ تمامی قهرمانان رقابت‌های لیگ‌برتر از ابتدا تا کنون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27696" target="_blank">📅 15:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27695">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlBsbyE3AIOd7lnlGsxvRXv0kVVLjdeFwfcZhJbZlUV16mKoIVORqBTQBU30kL6RIjYmZ1BVzstShm9m96qUitsuBQXh4SthqA8MJOakznR8WT_vB8Y1-q70KEBg8-DkmXg98pkeo9ko4wEEaKhs2vAk5fCkrv2sV9cWwI8yBW1T3TNchtdhbX_NytUgazf8rzANWB0ulbIe6rF0AKzLdZgMVFdsG-ZyeP0zIMW4bLiRDzHqWYyhKbNnX2IFgJigV-Zk-7Oh1uYboT-13mUzjiZlBGq4uCiqmWT6UTs_CFvYLQRRZgdtnJzyp86M9h_C5xte1oHZOkwPuPGuQSCoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ موندو گفته:
چیندو اوزور؛ بازیکن نیجریه‌ای که در بازی دوستانه از هوش رفت و پس از معاینه، پزشکان‌مرگ اون روتایید کردن و حتی باشگاه‌ بیانیه‌ای برای‌مرگش منتشر کرد، در سردخانه به‌هوش اومد و به بخش مراقبت‌های ویژه منتقل شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27695" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27694">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOGeDyYL3hP3aotdBGitSDgR7L6A_vLUGCJbyBk7yXGG5fX-S2vZk_UPrWZvLJPiS5tG22LZszOnQtTHGsrWNJnrwzBvXx5UIcYeoe3D0SS5OYc-G5LNWBAkmpTIirmDNvuEwGIPbF5AAeLOOxL1U5l0UgElOY7PLrw7WJS4O5aDPd1XzAC5pMwxRk8V2W-1drsG-LlWZ7Fm6qSvrPloDgZfbnu6kyBtYZy9PnSpi685fusXj7d-5D6c0i9tsTabqV_k2p8J8del9pYWl4XTY1DUted-4inEKamuZNGbl5p4zaEWZ5ThwkzC2nYL1A8JkW_U6_x6H8hWFYNTpbOCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه‌پرسپولیس امروز ظهر به نماینده مهدی طارمی اعلام کرده درصورتیکه این بازیکن‌ تمایل به‌ حضور در لیگ برتر داشته باشد باشگاه پرسپولیس حاضر است بالا ترین رقم قرار داد رو به طارمی پیشنهاد بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27694" target="_blank">📅 13:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27693">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27693" target="_blank">📅 13:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27692">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27692" target="_blank">📅 12:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWtqaMkv32S0hIWgRIabNtRvjtTbe4D9dcDzqHEhqC2UZdJgTp7d3dNePoshcBEBmB_cjqlJuGp-yk6YZjwkpASKvFt3ZhbeJ6WNaqFULHBORlJrso9fhMjhfAoLMO4_FfbvCGhJ0OAWz-inFsIYbWX5KzFKxQq9emEiJM0x1vDUxn-hXqlKBiQyP5aZBTryzUkGQJaYT3tqFUr3kDL35UW3amDHVV6CApMsZiKHnU3iVRvKf9a_Ls5l_iesdoixtu2r0G-sy-UGH8Mm8yzOnkpwUc0m8jMMF-KwhAryByUzKvwc2goKebFL46Y1bwjKHP8Cb98dWALkQia_g8fD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27691" target="_blank">📅 12:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBJQw0JtpLSGOCm6uySRGfeATiIwfUf-XC3ci6bJ8dWwXGBtj0QmBnSvF7-f7V6Sts-f2MTBJv9izNsCn6QjmoZiOQnATBeTLpvecYHNmrWkbucHHRFHOVeCaK00_zucZdfHKlE8hvT9QPEz-ziNZph0_H8eJDbaeyULKoC1e61-hbPgvvUoaYO0gV0Yk5xbhxsjyiTSA2Bfjno1wDqPf2zaFOmKs8SMoSv9GOAWbG_GtrLmMK3rgC2MMVUi9tfeKzCQFkdN2M3h-02OPh9FVFE4ud9efdQZN9MQqqD6wgvDjyLjKjj5fjVgACTfeRxkXJvJ61d25SZHvxB4dj-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27690" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLqPnXPFxvRfHQFsIZCF8O_mSmy_XECTeBAb70Ggo-LwFA9ScI0TMIAkRy7a77oyOgZnzE39Kf_yG9sFk-s6Amud03r3PrV-OOFM53ohkWnMxZBsQm8TlKpE0UrO-NxZKzbnIMbWD9lN1ErBVhOAHa4TEvXY2-GJoNDGxUfj2m--P9MtNBbSgV5JlT_LC0pAMYeiubhBhVpLNGPZtDMma5vdEhHubXFMl7msWV1MGHOJk05lU1SRFuc5tc7CUfmwubuX9KvCLinTkWoWpcvf0CM6SivqJYguD7dTfbyg4t7NVyxgRUhjTM7g39Fm5vonfvp4eR5OixHzex8A2B-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
تلگرام‌ِ‌عزیز۱۳ ساله‌شد؛
تعداد‌کاربران‌ایرانی چقدر است؟
۱۳ سال پیش در چنین روزی
«تلگرام»، شبکه اجتماعی‌محبوب‌ایرانیان‌متولد شد.  تلگرام بیش از ۴۹ میلیون کاربرایرانی دارد. ایرانی‌ها بیش از دو میلیون و هشتصد هزار کانال دارند که در طول سال بیش از ۹۰۰ میلیون پست منتشر می‌کنند. این تعداد پست در مجموع بیش از ۱۷۰ میلیارد نمایش به خود اختصاص میدهدکه‌نشانگر کاربردهای گسترده تلگرام در ایرانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27689" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmeGIdA3UQXiiSFbhYyWGjM3ptILlzkQnysJevny2pltODNMwFhnDHeRXYbmmSvqTqoFWEw3XQ6udU6AcsxznIw3y6sAfbZ-dHUQvEZOrUnjm-OKkjnPpdgcg8qUaUJfje6OHpPevgrrfScEx4OzaeC87wapP6G_IRsm_R-wxZ2uxiyLpQBA2xnGcyLAwaEJPFjWsvWEgHh2TJhFMAQtrcMKoF4ha8Pu3xFoaWfNS76yUwhC6b6hUiG21f0IXFI7ACPw6LVmdMEmceoFrb5C41k02f_Dtr4SZqIGrScNbH-Q9UugGE01jnandF3KfC44cj5m-z1KY_cloD5uIyLBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شروع لیگ برتر ایران با بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
استقلال
⚽️
✖️
⚽️
مس شهربابک
⏰
فردا ساعت 19:30
🚨
ورزشگاه شهر قدس
🎲
باشارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران درصورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری‌بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr23
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27688" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPVe17HymHhnEd8u-eylOve1Qj2smAQjw72qsmquIEaDPOWXNF8EH-O346i3EoSa89v3wESRNcLQkZNmFSvdVldEZCuOd88n1NDTE8H4gI7pWZM9h5UXYvQ3zxwMzV4Gc-rY-zQi8G4jxC5tDF03N_lEoOXBPpcMvzT7sU_uxK-V089Sm2JCmKZrYuhh0In9OV7vHvAs8aynvmBn-ZI8tf1iBMVv_2oIDg0IIC1Ua5uC98_9IHtuR2olPf6DqRCNX-Dr-jil1QmhWYN0qazCpKckFZpdZOBqVnxvumXEFwMEyYgbdZJb9_FKkpQYnpex757i1PWbqxB1QreAf05Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
صحبت های مهم فتاحی رئیس سازمان فوتبال باشگاه استقلال درباره پنجره و آسانی: پنجره استقلال روزچهار شهریور باز می شود و استقلال میتواند سه‌سهمیه فیفا خریداری کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27687" target="_blank">📅 12:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD3xZ9GhzCfdSe4BRbD019VPkOpzIOk0Tb4FkXAKTZyK3ItxDu97xfb_6lgrNemEEPanmcBaWGHS_Z98T5TWG0ScIGat5BOXHEp2OT9kVlw6atAKhlLB3pqucqM_khQEC3lEmN9NCV0mtrXUZs3EBcIN1gup7E7JUIYyoXWJYmQahAk0uIy9UxKlHD6Ytvt70pZo3VYWge8L9poEupPibqCJ1_du2s_8ZOCYciMR_M3rmR1Pto7BMXX6GCjG26dVwN8m-Zv1Ed0GJUe3jzkz9JMcX_BXImj2EfUH4jFZ5C4lPSDbUOQ_dcTovE2d_iFMFK5R0A7hlWT6JqJb4jY_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در عکس‌هایی که باشگاه پرسپولیس منتشر کرده علی شیخ الاسلامی آنالیزورسابق‌استقلال دیده میشه که به نظر میرسه به کادرفنی پرسپولیس اضافه شده. البته‌عجیبه‌که‌باشگاه پرسپولیس در مورد اضافه شدن او به کادرفنی اطلاع رسانی نکرده و مشخص نیست شیخ‌الاسلامی بعنوان آنالیزور…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27686" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27684" target="_blank">📅 11:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ابوطالب‌حسینی درباره صحبت های عجیب‌گزارشگرافغانی حین گزارش بازی دوتیم ملی فوتسال امیدهای ایران
🆚
افغانستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27683" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویویویی‌جالب‌وتامل‌برانگیز درباره داشتن "ادب"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27682" target="_blank">📅 09:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27681" target="_blank">📅 09:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGS5nNYX9F8efzqb4utio77IB9bAPXp0ztwaDDBSljfIZoLUWg2tY_x1FZgxsUVkvt-rjhno2G2WZDCVf-GjIUlmUZNRsku1ALHveVmrS6QfnUn55OO5j35IsgP3WJRIErJo0Q752Jcz8dX6_-pW2Y1nSAaaXJuknAGjDHLXgZngCqNq6-rpH3mFonIRZ2O0hP_t97rOCrT7-eHku3xPr-sHIeNUxbW6TkScgqvaEqhGI9jzwncCTIiR-uMVztO1pqXTRp-sHupqX3Y5kKa9me5FjpIVVFG59eDenYkKpxMcsNqBlRekWzp8zTPn-Pc4UXdtFEBHV3hRX7Uwmiwn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
سیدمحمدکریمی، محمد عسکری و آریا شفیع دوست سه ستاره سپاهان دیدارهفته سوم با استقلال رو به دلیل مصدومیت از دست دادند. این سه بازیکن فصل گذشته رقابت‌ها رباط صلیبی پاره کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27680" target="_blank">📅 09:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=nAnMvxB4z0YzUmp6oFUwpv2gakPiBdHY3Ai2LpjcDSxqFs3_8z6gmt7XAdSkPnA7vUMx3hxzDLsWcguymxq1mdWYpAs-GTKqKUCtMBbDlpJ184tjq_cGwNHZg8S1mRpxNOWe85eJUOAYLBpej5bRaaXl67U1Jock5ebKgZqlq12DH1FbrcHJ5Q4noX8erpU-1tOz9AF7erw2rNCZGvWMOnRB5KdLLATdbyZSvv9tt6bHIJlMBRHTvy5qj2oollKaLmQlJDHA214wqJnhInvxEKtlbIJucEQ5fkrCjjTNZD2WiDHVNdiPwun7mhKKH6jdYoOr_AtA-hm_oNpCoPDYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=nAnMvxB4z0YzUmp6oFUwpv2gakPiBdHY3Ai2LpjcDSxqFs3_8z6gmt7XAdSkPnA7vUMx3hxzDLsWcguymxq1mdWYpAs-GTKqKUCtMBbDlpJ184tjq_cGwNHZg8S1mRpxNOWe85eJUOAYLBpej5bRaaXl67U1Jock5ebKgZqlq12DH1FbrcHJ5Q4noX8erpU-1tOz9AF7erw2rNCZGvWMOnRB5KdLLATdbyZSvv9tt6bHIJlMBRHTvy5qj2oollKaLmQlJDHA214wqJnhInvxEKtlbIJucEQ5fkrCjjTNZD2WiDHVNdiPwun7mhKKH6jdYoOr_AtA-hm_oNpCoPDYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌‌تند رضارشیدپور مجری‌سابق صداوسیما به‌‌طرح عجیب بنزین ۸۷ هزار تومنی:
هروقت درآمد روجهانی کردید بنزینم به نرخ جهانی حساب کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/27679" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm9WHDlWIxjNtb2LdHWN9k_uvE_L7BkAWhPv5EOwiIqmK61GBJRbUDi7Jp_HEvqniiggTyI8rP0EegwF_154rj24xXYja0nSV93DTm0-WGh23pmzFIvfFd8n72HwczkdFOEsPliSP47ZTlS_IC5goTk3GQ0sZGZtLM4s4vXwaBstGahXLqn5pLfuv0rUUUCnRTQ3b5NYP4337XICB_tBIyWj1qQfB4wrqbD7dWbABNGPLIu08nfKdWVEKZtwGCrK08UQIPU1GGm9QbYwRC0njfSjA7kklsJLFsBnNqJYKk6oE_LCFEY-1khGrSmUcHnL9l56ugGgSJmRunIUXDprJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27678" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsHVuXxfkcEHtDIl70kTSmC4DFro_64efCGZk-Yz89llgAyMVCgAmesxxCVqRkfFwv7n-Nz5rYdMfbDadWTwfgB_8FYhM-70d1wbTC_hNeMy-9PiDr5dQ1rjmjjm4ILv5yYLHbwuqwwi6r5u3e6O6ujIcKkOkaEK8NNCRDxebPWJrBH5sa_Zv55za_SaB3eifosw2Bw3ZN1pBmeQMQyPlTV6jdTRiRy6Z0nWcQSEOdLOUpHfyS4xsmwo5Uj-vkVOpCRJ5sef-0mhxhHid6AlgOgeFqeQK_xd_guCOX8yCBX4xWc-yOwIPmDqhjxYvFuvt2Lt30uHr4grVMDz8ffU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
حذف‌زودهنگام اینترمیامی ازلیگ‌کاپ درحضور یک‌نیمه‌ای  اسطوره لیونل مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27677" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7bEU3DO1hp0CRgllps8Nrs75UKhPJIRfTcsnD4pxCo0bXRFr1D_0GuFAMmAWG3PkYQP1KEhXYBdnfuTSJzzpxtDL-7uJjXX6HfOZjeRI5g538hdu6J-f6bC3Y5ffi67z_ZJuR6rXmVnMuikkwXxSVvkOxVpzoaFTqa5ApaibVocA7Np1U3TAp4UhBIOTdLVosha4ulMwvxDoE5X1812AqS0QuLgYSljACGSE9BmgyQfF2aEmvvotyfuXE5J3nfeYnWq5C1r-m3-_OqbQEKpR7ubl-H7G2_05CSlTRsNFjrh-NpDIDj-yGOVe5QuqBMAbzGA24cx9oaQz-yluvwBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تمامی قهرمانان لیگ برتر خلیج فارس در فرمت جدید؛ هنوز تکلیف فصل گذشته مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/27676" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSmxEyeVyLByVggyDcgw0ETk-31DorXOktfF3q0gGBbXeotFsRa483nsr-q6w-A09aAp1D2115MVkJShX2fSr5MG8b0z3eNhjgPdenBAtThlMBMGg9ThHoc3B5PhotcJkNN-xg4zfJ5WLZQKVrBkDHPomYPMojmf4le5nXhU2U8s-Imdkak1d9JOeoUkj_8KGWx1Yq6qxiMf6VV7kyoT_UGzfjfMf61rzel0YyFRyXy8PCm5-XGtirbtrYnkE50Bbmr61AAoywkkTk3UT8DyAmgAEXl-o0fkIBJaMX_f3sNDt7sZVsVxhhDOZKSNGuvRWx5QTADCrTu4u-N9rmQyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgFN2yVrYoYdfdPVaCepqWSx2TaKh50ywOAHDn3H1O35pEpGyHqngM3R5vP8zIAmRKuveBAuhnJ4SOUkcrNeZrnLgOZMezkt4fvqb48pkiwP6V08ZvF5Gg5QcCPnj0iurOxS6nnhObgjzbKq-mksJN0G9oiVp1Unn6MEUe2Li2xDAaiS04wo6FiQVE6vcNJbh_3AjJV_uc9Otop_DBausvgANJhXef4L6JD5R3udsmS-SVMwAnPaMO5zG7KOLsqJoJbMbO0NMFX14wvCFKSmDU-ssWWwXjiOoAwYuILmXu5klswpfUfLBycwsN3xAnlHiTizSFeqdr6nocK0kzNd5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم؛ سال 2024 در چنین روزی؛ رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/27673" target="_blank">📅 01:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsy1FgvcOuKWia-Q8OZAgL3st48EC3cdbWmLETByj9CdG2mRzXp6BwM26tIApeDfwBnesqzVQ_DWwrbDhUdtC5X3ClOX2QtyAJ7Wi0irXdGMmC-lspYLxQcRsu_HOmq61IZ_jGSei8h3B4F5R29i8MS9XwPh3UK84J_GFNOGyrJQy9DwbhJSd4VKkoJOo1-7_Jvut8AD8A7sNaAjv61gluUIeJkzlsKvtBTAwJMJem3gLzJ_CGqaamiNUCTYq9rvktWGvFSOnKN-QHhVXNLivEJgPt9z49TAxbwrfbeSYoPnHI7XZibQuLhN3YxIoKsIog3xPtUu2J6ZhF0hwHWyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=mv2DGDCddzitxey04TuHrOP0q-uTD7T6iEg1C8iteUBonVe4Fi1Q8UTPpiKy0uJrWKCvDK5zFMlehh61wKTgNjaCf_G15Adq-8LvralWwICqZTPzVenfX6AYgKIKfD0ydjHU3FLATNw518Fw9RhaqGapLDDieav2glSlV4snLSrkAx0dbuMiFAWwrnIuPtekc41ZHTalgGi65BZcVEyRUyU6LSvuXYyggwYieyUdhcj2-oFjTiPKON6jy7UAZ0_4sQLq3HjDcgnI0fBNvWS0BohXHwNDIhNtJGAZWgaDajPHOkxzYz5-K4nY0kzUceD0tAM9BdpVQ45itI2MHhI9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=mv2DGDCddzitxey04TuHrOP0q-uTD7T6iEg1C8iteUBonVe4Fi1Q8UTPpiKy0uJrWKCvDK5zFMlehh61wKTgNjaCf_G15Adq-8LvralWwICqZTPzVenfX6AYgKIKfD0ydjHU3FLATNw518Fw9RhaqGapLDDieav2glSlV4snLSrkAx0dbuMiFAWwrnIuPtekc41ZHTalgGi65BZcVEyRUyU6LSvuXYyggwYieyUdhcj2-oFjTiPKON6jy7UAZ0_4sQLq3HjDcgnI0fBNvWS0BohXHwNDIhNtJGAZWgaDajPHOkxzYz5-K4nY0kzUceD0tAM9BdpVQ45itI2MHhI9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2024 در چنین روزی؛
رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27671" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW_oiZTSaTq5tnCaFiB6oSa4eMwyvR8VS5SSgQkZs2hY8Ab_qTsVnezo9O_5tF4fWMhCWQ4Z80Pwe6jUEcaYoRh-ghggAWnecVTAmIWnjX839zqBz5o2BVfj0A2LFQOn__TD-tLc_Hg20ClUMz6ZE791mBd5cKCQteJX4M_z9IZI3GCm3NZmDisB-0x-sx1vy4uhrmkJddTf2u5SDerzZZ-Ms6-R_rS4SzS4nlH-3bpZAjU116qsxtbKfa15HMYYlXONBtiDH6lSmztxzHx4IIn0-4bA7woMatG4oB2acrfGyG9duud7zoVX5yJ5BwL3SPS2me_GfaTXPFgKK8GHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛باشگاه ریوآوه پرتغال یکی‌از دوپیشنهاد اروپایی محمد محبی ستاره 27 ساله سابق‌باشگاه‌استقلال است اما رقم پیشنهادی این باشگاه 400 هزار دلار کمتر از رقم پیشنهادی تیم استقلال به این ستاره ملی پوش است. ایجنت محمد جواد حسین نژاد و محمد…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/27670" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=hSj83hcBgPIFYpw_psV1pTc-29J-G1BQ5uXptCmNPLUMuZFg5SsB7xUWL6x9C6jGD5WL6Qx5awillGNO7eESA_GJfY-s3Gc0KHkKAb9ZPH99I0xDaoflUfiMaNqhY_xnY9mrtfdNhFz4m_3ieyaIIjU9UMAoY0e0t1jjj6BpJtzWF02H37A5V6RUGARXYg4_SH0-tYGNeoUFGySJxbwkaAPyDXGIM2s-lbxmX6Q-TAPUBRXald17E7eHQbE9oN1aPo-Qgvrl86E-kRsDRvRymEXExBIQFyF8d7jhiGqBwyFekXVlDdgkeEXwuqWn83DJDscgK0qL_0iQzOMqM0lXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=hSj83hcBgPIFYpw_psV1pTc-29J-G1BQ5uXptCmNPLUMuZFg5SsB7xUWL6x9C6jGD5WL6Qx5awillGNO7eESA_GJfY-s3Gc0KHkKAb9ZPH99I0xDaoflUfiMaNqhY_xnY9mrtfdNhFz4m_3ieyaIIjU9UMAoY0e0t1jjj6BpJtzWF02H37A5V6RUGARXYg4_SH0-tYGNeoUFGySJxbwkaAPyDXGIM2s-lbxmX6Q-TAPUBRXald17E7eHQbE9oN1aPo-Qgvrl86E-kRsDRvRymEXExBIQFyF8d7jhiGqBwyFekXVlDdgkeEXwuqWn83DJDscgK0qL_0iQzOMqM0lXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استایل‌ومدل‌موی‌جدید رونالدو بعد از ازدواج رسمی‌اس باجورجینا دوس دختر 10 ساله‌اش؛ ویدیو ریپلای شده هم ببینید خیلی سم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/27669" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNPwV78WX93fg8IV3EaFynKWRPV8ErJi693pD6n8fIuywJeA7rk2bafaecUrSeGF1sD8sKth81HcIxgkx0Z1mdtyc1dAP017fO3t9-Tb3iJQazLdMf7GEooqclnF4ctjKy2wG2hd0M62IY46mZD-WKEYjkayGspUyJVuQz7fM8PSIuCuczIHqL0wOPxPil2n9i_kuTReZxfFhEfDXi5x97wLbBYwPU8t4eu_pACw6QLUAZMANfcpRe4JUqj4q1gm_mvEoBZgDE8WbRfLJBd8f5F6ok8gpBk4D6eTg9nGKd3nSxuoC0OhKw4ANwdkZVns5-RBazZG_ejhHiamJjINVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/persiana_Soccer/27668" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOyhwdxnSfqdvNU74d-cg_ycs5KC8zb0gzC9DHEVbDvfn6R5aBG_sT7zNWn8hIRQCpACAqvtFMqI7hzzsof5r28I8aLZOSe_R-imLGN9DT-a5gBGvNugdDZWXfFOOU0VQHTs_XlIfjZLTt_NqcDU7V3PcC5jQfhVN-EE4HFBblnTybalOJANov_aBl0fPS5HEoPl3tmFxeb2s2eGLgU6TbOeWVKdmZq6x8IoRyImFixVcw6mNelBzL420_6t4kUzl0lJMzYVWW7hzsDCEu0hPcm2ZTVnPiVZsDdd_N7P1HRnLRNTT4iolxySWZ-L3ib2ni9hH5lOetI16csxcgJoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/persiana_Soccer/27667" target="_blank">📅 23:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید خود برای فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/27666" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqDkReZHMwb26yN_cMceE2n3U6LXD2OVBqMk2Y6qktTdlFUNPeMFB_RbxUN8FJfFnIpJxRKvGJU_6MnrnKhk-CBz4TvNcTYMbQZqBtr_-dgKT6-zKqIgdqcBtI7uLZ-dpZmqb_u4HCuH20ZmIlAQC5M3b7je-v70npAVLTM6SzrWPxabqjSrK7aPBp8m6lhJFuKf37ni0u1e68JMBhTuvEmbkNkVwCHvO5ynhdQ4drc2ftTVBSfQW29XwSKR3d9xbvqhqbbul59wUWiyrMRd59pdoWJxvvB_jCJYt5vp2aIY3bUX1kzrz7Ff0MDalA-fAf1qZpF4JEVY_Chrk1DuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27665" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na1UU_y2int_sSH-ccjZ63_bM5gfuvO7ykRyXWv4YIUGnqUt5KEi--59UzhVi1K-2D34cbL-9ATZJuS3xM7YGsPeD4mHOeATUPBZRA-3eXAlrGJw6l8lqV38gsJjU0_y7YL3Il3pcGl2glZYEk_y--8x5h7DSIBVUSPVAcozU6XmYShempXWXJ-sEh8MNkrX_TqxFHzxVxCNRWKJX6ItVtqIfkLBiE1a_AquFTfk930aETgiFNakY4MH2a9Q_wMsJjaI9V2ClGfvxLyCYCUbPJAtmi-ty38bz47ghIWkPl6Dnm_Tid6d7sodeVl5vhx_4gie1eMqv5oURTV6ToE9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27664" target="_blank">📅 22:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFxQDuPL9Me2lepuu9Esx060xWcZ7wTX5ztOdBWY9QhTl1qd5YJcFrjxN0MQFFRpnA0hVlNVVIGf1tUJt6SSlg7IWIdQEVi_0YJ8SR8Cu3gvVoTU075KA2UeWw6n2xsRT4_nErbYwLybNUEbgGBnDJhJm7O_-F_huNwT6B5QRdVYBVDCGB4na8f9J49QqVu95PowLXo1s3yiUAWQaOVJzKxer0za9YdjLPhad2YFh51zQnAjTuknR6PpxYwnTAX8fScasTrfbjbXkn9-S-UAZ3BWsKL9s-ZbykIq2RAUneT1kt86AlFL3VAxKKuVWcS9PBJgls_hVHliAV8atbNa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27663" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVVhf09FP9cJ8arJsqWqz3lNks0v52XjcBxgBA2CSA5ASbQFJGYIazxhRuQIsuPXf_bh1aFrklgcjj1N-Eh_NRrQqjxwTLTd_hlC1KObIrrf1032XZQle9h1p01OBrTps14wXZbQSbcfe_6N4iWZEMRaakYPWhLKR4qvC_3HXfDxmDOP4v9u7ywt_xJgm1OepoivJzW95qLDpvH8c1oz69EiYUXamXDaNqEoPMg8yXTZeVE7N_o7xvAu-8CSg8HgVHn7HExDObSFAkkDrgVOodUmTk_n3itAn8ZkISL-4vedxVwDNcIH93L5p2vCy0U_8VSPyb3C6qEVpQuoSj0ETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌برمهران‌احمدی؛ روزبه‌چشمی و جلال الدین ماشاریپوف دوهافبک باتجربه تیم استقلال به احتمال زیاد دیدار با مس شهر بابک رو دست خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27662" target="_blank">📅 21:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baUSNXkPvCkauZV7YCvT3yHrAGo5QsnUtavyDno3wUzskpchlviug0EDc6SdQNKco2tqYaiPVCah63k2fI548vG_TNuLkQLXbDmITNu9dNjslXYsP-10QQHOMayxsEUMc1Mv-zrt-WCjmQik9IJqgQNu3PJb6JzxQ-XdZNCA2w4RgcOdE2MWY4p6Et-MeWFy_BkSD31NVq2pZZjbYtZZDZr3wRj4c9qXDIyAYg3slom3Ya1atoTT5uTTGvaZ1HDTA1xqoYTy4DESZiKVSILRvel1661bmGx_1_kwdiIuqU8Lf9d1M6kE10pasw7jXsVdcOp5p4_kE6K1bQQcHiL1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
#تکمیلی؛ فران تورس مهاجم 26 بارسلونا با عقد قراردادی چهار ساله به پاری سن ژرمن پیوست. هزینه این انتقال برای پاریسی‌ها 55 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27661" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gerqncyB60bwbR_8vL1LI3W_oKIub-R4aCSlCp3oQHNRAf8qNPcmbEXd9pvPz8MLgkLUnfshT7uX_oOvsQl4mtEbRThE1aRV2OPuc5i7AdIKnQc6BYl9mGBUeyBdWfucVowiXthB5iF8uWRL5WmhLbEAUbO2mYtCASVKBVi80NmyFNkuhbdef8xwel8CN6i6Pvho3Rx0Y53IJfL4cVu5eM4UgIz7k-Ckmp1MOdU_eY1AoNT0dXBH3t1pF472FX-EziIamF7wAggkEn3CM-RoYqiz6fhbCGNjXYMXzJtz8EyLKawpB8Atjf4F8NsIup6_ZklN0JLTkVcnRt9p2EG7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درانتقالی‌برگ‌ریزون کریس رونالدو به شمس آذر پیوست و برای ماه عسل جورجینا رو برده قزوین.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27660" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN3oJLk7l0E_MaxUu1OprtlOFxMGnZo3veLEzmV2eucNiaoJBDZsHetPzYsyJPbZuLzrMb2b_5rIKhgURCyyYTnBFbmojapT0nX89KprsBRkkEwRYKrPfAmZJY-hzWqyzU5r7x8m7yoFA4oBShwhzxhImw65x2d4gVmri-aPpUd-ZEaxueQ4wxdrG4MChBvmjwi4xZGa8ot1ykdjF6rW-tNcVxf4tRj7J1Ogjl6DcCxDWD2pzlrYPzxnhA4zM2teBs99hAbmJGPBKYlNV_KRHoFojvMl2A-jXYNQaWNyxHFWRbbM7r36oNo60WiW8cBv2SdNEMK3fAgxF9Cq_2KXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی رسمی باشگاه استقلال تهران از کیت اول آبی پوشان پایتخت درفصل‌جدید رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/27659" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=FqEgZeP77eH7rdzQuN2a61xdET3Fzjl2wvYx4vB2IeeqOircQW0N7wqTzk0DLt2UvuaOWVkKyLaUvNGmOOnwgH_ZioluGjUmi5fdH00Y5q1rfE5cVBKihkhOgo7gkRcBLF7oMT8zCTOizSioW1LQ4FtSo3QwrAsG1qBh5iXG3BCVNNKeVeB4CfS1K9W_E7vobobIHyqtqN1BtYuvT-BQfWy-IRuo-Wgjmo7WY2UFTwp5XR7UcKUQpQ-lonwYzLvnOJdJyhmEGc-GfXuBnGkdjK51ecmWIXLS4_p8We-VIXKKbcfcdoBZ1chbsNTa_pPes2BAmaf7OGS45lR3hNistw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=FqEgZeP77eH7rdzQuN2a61xdET3Fzjl2wvYx4vB2IeeqOircQW0N7wqTzk0DLt2UvuaOWVkKyLaUvNGmOOnwgH_ZioluGjUmi5fdH00Y5q1rfE5cVBKihkhOgo7gkRcBLF7oMT8zCTOizSioW1LQ4FtSo3QwrAsG1qBh5iXG3BCVNNKeVeB4CfS1K9W_E7vobobIHyqtqN1BtYuvT-BQfWy-IRuo-Wgjmo7WY2UFTwp5XR7UcKUQpQ-lonwYzLvnOJdJyhmEGc-GfXuBnGkdjK51ecmWIXLS4_p8We-VIXKKbcfcdoBZ1chbsNTa_pPes2BAmaf7OGS45lR3hNistw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
کل‌کل‌جالب‌مهیار حسن و مریم ماهور برسر بازی پلی‌‌استیشن؛دختریکهPES و FIFA بازه‌اگه‌زن زندگی نیست پس چیه؟! تو یه بازی هفت تا زده مهیار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27658" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=u30dxROjVVOdszJNY_PuqW2z6d04vjtxcHfnX-aOXhS9rJEweBftsFIjQSg0ade3EEmO2DYcczq78jtlI5yb-hTkREvPxmFe5zKg7-j_5dVDQKNYucJS6LRbPzCuZvOKVYLO9BXo1YExF7aOz2eG6X3p9IEHvXXh2cAmN0VRAqPoJ8KlL4Nku9g8sG8yatDGYfWAwLzsXsK_aVhPTcvTPcFZFi6_tcW62E4cHeU6kN5d57f9GLlOrubzIXnP0bRW3Pui6uG1oZSphz1hx81VFLt6YQEmJWOJv5Xz5PkC4qNdIPymVrmaBBZrIDFWdlvZwJLYKb1mlR-w4SZpsEHSY2Jj8Rv0vh34pEp-NtmZokYdg-bQFK-TATlqkQdszffJwWSc4QH4eNVYob2n3pUAbLsY_4j8-xkRCeioMLqD5hdLNICNi1Uaxg9cl2VlSVRSYJgG3tKOH-UAfH3e0YOpvSMfyUPn0Sm2vFP7X-IehdmvSgY2Uz-5mdtM1HpJj0Wuh-GQLcJxAhGR4fWuK0HgJvmWYNYqUrfrpVQ0Bi2f89dKs9aEtX0gMzXtVNA_UCu_7LLajaYauXaFBWI8YHBQXuuYMYMhd290mco3D1ZlhovlQfjPyqnOJJbW4AuFoquPqkHwz6BKuaV0OyIu9criD-nUcpHO7o1Rj7YEIw4ooyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=u30dxROjVVOdszJNY_PuqW2z6d04vjtxcHfnX-aOXhS9rJEweBftsFIjQSg0ade3EEmO2DYcczq78jtlI5yb-hTkREvPxmFe5zKg7-j_5dVDQKNYucJS6LRbPzCuZvOKVYLO9BXo1YExF7aOz2eG6X3p9IEHvXXh2cAmN0VRAqPoJ8KlL4Nku9g8sG8yatDGYfWAwLzsXsK_aVhPTcvTPcFZFi6_tcW62E4cHeU6kN5d57f9GLlOrubzIXnP0bRW3Pui6uG1oZSphz1hx81VFLt6YQEmJWOJv5Xz5PkC4qNdIPymVrmaBBZrIDFWdlvZwJLYKb1mlR-w4SZpsEHSY2Jj8Rv0vh34pEp-NtmZokYdg-bQFK-TATlqkQdszffJwWSc4QH4eNVYob2n3pUAbLsY_4j8-xkRCeioMLqD5hdLNICNi1Uaxg9cl2VlSVRSYJgG3tKOH-UAfH3e0YOpvSMfyUPn0Sm2vFP7X-IehdmvSgY2Uz-5mdtM1HpJj0Wuh-GQLcJxAhGR4fWuK0HgJvmWYNYqUrfrpVQ0Bi2f89dKs9aEtX0gMzXtVNA_UCu_7LLajaYauXaFBWI8YHBQXuuYMYMhd290mco3D1ZlhovlQfjPyqnOJJbW4AuFoquPqkHwz6BKuaV0OyIu9criD-nUcpHO7o1Rj7YEIw4ooyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27657" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldTZ4zN5XXLR_tB5e2cFrHa1XiJsAvx8nAAJ0W1WViLcRTofWmRY6ykNdNrOeEcaGNExL97e8rMT_MPJf5kCp1wMFujb_p9btmG_rSg8d9kQE3BByA9ULCWmLUcIgW7nLCouSaOgRzrBx2rNoS6OByWhIsPWQ1YmPnf1aeDE3izssc4wJNg1LlujZcUzrYutz60cBV6Erbbb-h-WlyGXt6g-cg4JBXPbVGxf8u51dtN3el4porkCbAXcgONVrcHgIxjZ0Cm5Geha2tHir2B0MqpZ-NsACnON8e29yw7GBE_sZ2CP9IpvtPfQm8w3HuUg5PIIbHuim862rWgeag-6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طبق‌اخبار دریافتی رسانه پرشیانا: محمد محبی از دوباشگاه اروپایی آفر رسمی دریافت کرده و اعلام کرده ظرف 72 ساعت‌آینده‌تکلیف باشگاه جدیدش رو مشخص خواهد کرد. حالا اگر با هیچ کدوم از این دو باشگاه‌به‌توافق نرسد احتمال‌اینکه با استقلال قرارداد امضا کند و قرضی راهی…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27656" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plhsLFAfvMDp9ksoxXsHl3hiFym-uI4q0-AkBd6lyvTO02yACtcUDzaA83XZI3jJUc3RlTJ2H_DTqEyMuzSQTlacKfDLdzmt_xB3QGnZ3Rxt3QaaIw0N_Y6IspySO4iYSpUXZr-Nds1Ye9IVGMAV4-nGt0mMdbrtRn4Rbg_nCMRoWuFGSoT65nKjF7gdcWLFot_CxREDe2xbdVCtxD_esoBIKakUTX1JmvklP9WO8aFjOsv2gAVSM0sxyOEfSr5XOFkkp5zLKLpwaXN6BQgBUSyWG8SBn9qNNsOSrdh2vIXlEJ6_SHBmPF0n-N5_K1nKoJLLxjj874egXx_ScnHmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27655" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPxB1IlmOLn3dKAJYUVskOc7IlZpa8BlELr3iYs4r2nYYX-zFOO7UpQDM3-XM6mzTFwxkmRCTwZhyCZBLtU1TFU3l7CLyBtZx6ccfDqXLURuA3chX26PSL9u7e95cqctppjzW01zbhf6stEI_Q2CQ0W9vRzCelkm_5rBKDXi8yS-gE5a1v-E96TP_TGy3TGkwA24nNKIDXfYXmRrjRqL-GS1ELOQmNo1Pi42aSxh_hR3iSJ0J_b_og6tHcoGvOLU952FweE24YQFri-IO7kMEVSwYKcthI_r6rjlOY_5vJTYunIBsDq967bffycShwW3njaHG9t8Kw73pRWlA28Frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27654" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYmYYvqmy-n5WLsd5jXUPjJCNc_RU9_2dRebHSbzOM72IpXDCW3_fDzcjnhXgkazedopZJpOnkoRAaIQY8wF3Q21bg3y5qz978uHTS2bpUnFOGDXfIZbfz6Dtk8ABQsmNRZcEVGtjp_3KHoT-hXydh8osqToJ1TBLWLpt_94t-PA9_TYdSAtSXWcnZpQ0cJd5ZeCbwGsjUfd9PoiPcZIJCHIcHJP80enTo4wC8B1jTVK7XdzhovX9rIEvZnwvONwb3lrutD82DXqT_d8_0XD7kRgZA1L2lR7PFNcBfAvzL-t-1KdXgD_izuMDzL_6iWixWcG7K8ux1Q39z9gGuzgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سزار لوئیز مرلو:منچسترسیتی‌پیشنهادی 120 میلیون یورویی به چلسی برای جذب انزو فرناندز ارائه کرده! انزو مارسکا اصرار زیادی داره که این بازیکن رو به هر قیمتی به خدمت بگیره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27652" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nunxVFepI1rJeysM41JoCNxcpZH1YdyrDadHEcsZLU2GqYFjV-JDlXubqIgP_soF8iis1W8AS6kopJu5NbuR-StT_fjYVjHtqa_Z7EGTcLgvPr6w5Q35iBjkn9HLUOfTf1LIev8AIPvpo_0IKAPdADrjOL2GewraouUGWl3DEqglkk4RSaavXUVdOgo-hdSbNLMWCXLh2G3TP1doATP1G1d1p6upN_fjAY1X46HlqsWKZ8cDrcAT9dDAW6nlNtm7or9N5pI09CezHP6-N-JGQsozlwx8Zu9jomhDCzSPGaWMOf2YgwJgYhxYcK5d-jwT8jNetUcfm0dSe5fg5WcJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27651" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-W2jKYolsJ1yE_QoQBqaehZ_4aTh2UHTKT511_h95OOXQ5rf1jM4PZmTs3HWXW_K-nU2rMr1gS-rMAr1gNUq6s_3ft-LHhRElXCFG9-SMjlFiG_TQ18Xvr9FSlR5MjFbD0hjVkuGXvO3oUnQlRPVKW821qeNAJLGPBzbGBMaEivlZmO8-WLN3GntphfFkziz3v-nPQw2axXmQNjhORqzscM_Tbeb-vxtHSH41JxJgSeqRdHDrUpjJJFXTxOXszWcA0ebHX4haKYyEX2tK3qDTOB6NhYSbnyQsHCk9nrS9FPyc_pT2-ru8o7dr7haIXL6f_44Gd0w8TgOzVtou6LtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرکت یوسف جامه به‌عنوان اسپانسر فصل جدید باشگاه پرسپولیس انتخاب شد. طبق توافقات انجام شده قرار شده این شرکت در سه مرحله 550 میلیاردتومان‌به‌حساب باشگاه‌پرسپولیس واریز کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27650" target="_blank">📅 17:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy7xvcaAqtqgEa33Bp2gcc4CMW8ZGvc6gCTslxtEPfRx8kjsn7i9B5jeHVpQfF8e6hsVLvvOIErm1Dd5yIwFfeiz4vXni7AYZioBRdP-zshwmPdfpFnDHr3zn3tdfrDYpMKQBb2uCqcdE3xMaE2pmjiTteF4lalFugfjgnmSw311KxXZs4W6q4fzBg_ybHxAtGjc8S5knBnF3f2wJeMr8WNOhgmdfDZz7BEHao8uurk39tOlvjWcMZrxPF8-P0pkQHVK7TTQKl3Y8F5cAFJl8hyiOii8hEDMdVRicSMHcA-x-BXjs5psDluV9Tm9SQBzUUSIT9dzormMjbX_-heqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
دوست دختر هکتور فورت ستاره 19 ساله  باشگاه بارسلونا در ورزشگاه سانتیاگو برنابئو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27649" target="_blank">📅 17:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIvA8axNGsL2low-J3PWPbkLJt_xU3F5W8IjlAPpkNOs2eCXi175R6VOQRmfXzJVtpTp7yIKUhMfUJeMLr3LTP6BQ-QNBXBuxcLrcHClshycBz7Y8tKBsioMizHKQIexoXAAzrEc49ClHPF2fmJhZyymL79w2t5uSZ0U6q9rVQyvYGb99o_2uVBYG7syiACXhAVE9NFct5Z8KiVtjBEAmFogJFW9QMCLzSVU9-3M7l2bS-2FFtjtmUxIjWH3edXvcZV9tdpZ4h-Qx8FO1AiX6ZKM0BItRByPGvJWccV0e2rvt72rbWwgjF69jFNFRDrfRM2W8cRFUobAYxMrCqTuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27648" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kED5ne8HS5FN9LOUySBCY2i7APzmlOmKZ3M07tpfk_FuFxTX_8ccd7cOz6k_0VTPO-_5W5Z9g6B97zhQbJCemniVPMLO05c8lZhs0fD8ATXIgnarZwYdpHhadDtYGc-RYO39IiROjQX3cAZiIC99ojQt-70F_asj9TGQxCo6aoziWCJ1kNhaXyYuoCZeSLWYmR06N_vFwR7JOC99OsgZm7Wmhu9lfYtYXMT3h5NAp0MpVrAOscKEKrIvah0XCrpExpJ0s2PHFmBIcOAfj2fdUXOZZnXI14sHbI3NzyJG3AOlHNhXav0EneLmdYFEY9pTqBipRQbg_9DCmIkcbxUu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27647" target="_blank">📅 16:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27646">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwGVFlqc3mzQgqZb-nswkl6z2vX8S7Jc1WoppfVsGc0opHHBQkRfN9ONhK4kwlTb5TNcw4jzMg06HkB7b0JN-kZjq0r6Zz9Kge8hGHeyxC_Rs6qgoz0ZHvi0APrJ4lVVXAKaaobUzDF25yaYlYhvg2lY81qV-HNoPCnQcw5z_5UY16a7cTDxBzpU7eNfhdxo96QZ0IQkFykcAa06rz5N_FoM51nXOw4Ais_CbJaICSVq5NJmCiXLhzBerULZ5qBqCVuGnXmFf0fRZggrqa4vGL6y2KLD5GfyyjA9JWraAJIVdkHCF-IIsNhQf6ZHPXUaXlZ4mCXqsyuNL9SySQLrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27646" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27645">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX_YwE3yrrlqhcOD91USlV_sMG7QMDnnTtDihoF2sCSyblJXu-ImiIRVvkIXFm5H3uVW_AWUgB6YvDGfMTyaTHrwsV5stymR864NCIgcw3dCzadgMorkYDSa4_xAvwaX2LcEyEbmQcINCNj8vydheDf6-Pv0Kn1VBAdvvt-mw4JS5gMhBvZcz6kayPZX1DhS2xEyTyx3-sz-e9Y27YIZroKihBML5u02TtoJiucxEt74ZBIGjNPGBo7FKmRJaacil8ypkbNyITGHzlL4lySAe0XkMFS-oh_IHH6Amh17SpO2UGdVA2khocnZgptf5pUoVgdrGloyGcPD1IRwebITvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27645" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
