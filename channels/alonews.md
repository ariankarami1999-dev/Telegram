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
<img src="https://cdn4.telesco.pe/file/pKtdacKK7PZ0slH5lMiqmIbeyVn4NOa1XOpUKqbiM6N-NTfiTvt4JXTGsZ2_W5bo6Px9OWeQTZA3ytsMV5DBcaSEUxc0tq5ALx1FA9_hhVdzY66kzcL-5-23Hp_yM8Jt-dQLouXJgm5xT_HyOX477GARsFncTCk-MDnHJHwJhxTJ4rJJmIHF8fvc4LUDiVx2rn8DxlAzlHnkA7aH5cptnXbXDjyOMVdSd_MxdvzIzSJN7BjE8KD8RIFjlWGQl5Rvrb8u4xBUo3cPIwedPDwfqG0eidYAlZ2fa_hFjczCw3g4viTobkL43lR2Y2LHt3ZaexFo7MTn8HOxTdxtzgGkOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 979K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 18:41:38</div>
<hr>

<div class="tg-post" id="msg-143737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار دیلی تایم پاکستان: ساعاتی پس از بازگشت از ایران، محسن نقوی، وزیر کشور پاکستان و یکی از اعضای مهم تیم میانجی‌گری پاکستان میان آمریکا و ایران، با کاردار آمریکا در پاکستان دیدار کرد و در این دیدار، وضعیت منطقه مورد بحث و بررسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/143737" target="_blank">📅 18:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
طوفان تورم تو راهه
‼️
خبر مهمی که منتشر شد
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/143736" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143735">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJbf2a-IwlzkREVVbRpr9bLRiwGWwCdIPaG827rk2TU7LboFV97HD4BVSOMA6Dn0DM01DGfzLoMIm6qc7dJq_iRt-bqf0ys0LYLsMgWiqUm00FoiF7assXlYiUtsbL5VF8qGDRvRV1u4-kHmMqvzaqzZ06sZtVQLdxTn35aWI_ZC0FjA755gDjGJbbWbplpKcLerCZU0oWWVVpd0eMmjLqnt0Pu2UPU5ZeiItHT_2JItV9XiJeilQLTNpt7KDNyqCNEV5P0Z3T3RoPrXFEMIcvpZyU6BQ5P52S5MUAzWOrKYWWkqk6HEA9zvUN-stOoTzkcchY9zdZpTLCSmthll0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ در تروث سوشال با انتشار تصویری از دریاچه اُنتاریو (مشترک بین دو کشور) واقع در مرز کانادا و ایالات متحده رو آن را دریاچه آمریکا نامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/143735" target="_blank">📅 18:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh5jx3BJDwBRoPrTR10xMCToUA55ASHpz4A_4201FNhP4epy7Ij8E6mYVXHXJNL5O680G0E1Z-aRRWDDNEGpw-c4IbLHJHp-sID1hgwhKFYyKjhnqH9Xe_Fo2hgFeRFIPfLv-oeA4v6XAkq0UitSy26SGCvQt4J-fRKVVydUVdKTX23Cg8u3Evl-U8tsl-nDDfzOezZMCfssyAiMvCHhF_iyGjHmoKie653zdkItaM1AZCZ4MMdLgAZzo3AcBQi9lirIYMj6sv-20NH20aG4RCGp91nQpGM6GdvO_h1yxtM2Ds-TnqcnAbmFTeOEUzfTXcDzOmYsEDKCuPCnd-JIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: در طول ۱۰ سال گذشته، ایالات متحده به طور متوسط سالانه ۶۰ میلیارد دلار به خاطر کانادا ضرر دیده است.
🔴
دیگر نه!
🔴
پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/143734" target="_blank">📅 18:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8n2546VxAW1fzt_IMxbDPNovvZh1tig_lVjb9_5QPFa0Exeio_3jZigENj_KyKvsYSdXi15mYH8Y-QCUxOm0lbMSGq2L3vC0hOmC5KXzyRaIA117QSE37i00Unbyr2eX8s-dJQBG8TzeUlu34mi7R-svV2BiEWgJaHlZCBtDevE_SAUevJa10UBsLq8ccXMuOnq5STMTDMtf2IUROyijGOOBuHQ7D1CLPxjh1vvWkaoI_O7-6X7xkNdPesoH7hCgy2udi3GVL3x0G0x3WpDEOEcWemG8ZOflJCDE74GsxgUYr8SYDVMxxnNC8C1U5yaNceSqNicwoospWF31mbO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ چند ساعت پیش: جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
🔴
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/143733" target="_blank">📅 18:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عارف: ما برنامه اقتصاد جنگی را ترسیم کرده ایم، اما برای جلوگیری از تنش در اذهان جامعه رسما آن را اعلام نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/143732" target="_blank">📅 18:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFwUuLToZfus20Nq7CAKw0VG1aeV4qox18rev_FVQHf1YZd7V-IsM4z5qEuOIkEinnRObNk5R65vGMDIAh-QvN_Wqv8ALqPW552Ue_YWmj26npsmSuIepOuMvDB4rKLp12DOxIlaD7He-K8rV1F2qVNgcvqMOsCRQKLGkNiGVmW_WUyKehrFxyMgiNQ95sXOu1OEUxxQ42HQPoZZXcK_CGUYf-p7ddzDse6jRAJ08h-1vo1K-6lGuHG9c2yXiQEKrKEqvWBhoTzqd96k0j_iRlMnCj466hW5f9JXRQv5EMQ41vRSHvA9liLZ8zzLDjbo8Vc-BdgVwj7Zn3iRufzC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: به تازگی توسط نیروی دریایی ایالات متحده به من اطلاع داده شده است که همه مین ها از داخل آب های بین المللی تنگه هرمز برداشته و/یا منفجر شده اند.
🔴
به ایران اطلاع داده شده است که هر کشتی یا قایق مین جدید فورا و به طور سیستماتیک منهدم خواهد شد.
🔴
از طریق نیروی فضایی، ما در حال تماشای هر اینچ مربع از تنگه هستیم، همانطور که با کوه پیککس و سه سایت هسته‌ای دیگر که قبلاً ویران شده‌اند، مشاهده می‌کنیم.
🔴
یک خط مشی تحمل صفر در مورد قرار دادن مین با قدرت و اثر کامل وجود دارد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143731" target="_blank">📅 18:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/ترامپ: نیروی دریایی آمریکا به من اطلاع داد که تمام مین‌های کار گذاشته شده در آب‌های بین‌المللی تنگه هرمز خنثی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143730" target="_blank">📅 18:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
دلار و طلا ریخت
‼️
بیا اینجا ببین کی باید بفروشی و بخری
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/143729" target="_blank">📅 18:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرنگار دیلی تایم پاکستان: ساعاتی پس از بازگشت از ایران، محسن نقوی، وزیر کشور پاکستان و یکی از اعضای مهم تیم میانجی‌گری پاکستان میان آمریکا و ایران، با کاردار آمریکا در پاکستان دیدار کرد و در این دیدار، وضعیت منطقه مورد بحث و بررسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/143728" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
از سهمیه ۱۵۰۰تومنی بنزین‌ها، ۲۰لیتر کم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/143727" target="_blank">📅 18:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا در سفری ناگهانی و غیر منتظره وارد مسکو شد، طبق گزارش های تایید نشده این سفر مرتبط با جنگ اقتصادی علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/143726" target="_blank">📅 17:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: امضای تفاهم‌نامه نه از روی وادادگی، بلکه از روی منطق و آگاهی بود/ عده‌ای کنار گود نشسته‌اند و مطالب نادرستی را مطرح می‌کنند
🔴
رئیس جمهور: امضای تفاهم‌نامه از روی ترس و وادادگی نبود، بلکه بر اساس منطق و آگاهی شکل گرفت.
🔴
دشمنان متوجه شده‌اند که از راه نظامی نمی‌توانند ملت ایران را تسیلم کنند یا شکست دهند، از همین رو بر روی ایجاد مسائل اجتماعی و نارضایتی‌های اقتصادی هدف‌گذاری کردند
🔴
با مشارکت تمام آحاد جامعه، منطقه و کشورمان را آباد خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/143725" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGUwoB3a7hpFaSOt3AiQztByNGc9RNDx8FDlGwyfukMJfcSamwErTjSfU3biFIp3vPp7pj0YpE-8nbbmq9fkuyHDg0JMGsws73PC1SnPJx9sa1lDMTbDjHE7KEXvjfiG25DHILPxlq5L6UPWmHX3nwekFWNx5RoAiwQFr5oIDRCK5J5si9L19gX53YVmNCWoz3_twRhJfSA01b2MWOFQ1xwSTxrmtMUhmbDPGLyruOhLSjtL5gdyGmxWIMUNHBijzhKlXN3NXhCyVwR6CtABgu25K8VEpayUXbu6mXjg-YyYFVVsdZhrbfaCuhHRSWxRpW5I-1EgolAUD_EjxqHNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرانسه و
عربستان سعودی
به توافق رسیدند تا یک پارک سرگرمی با تم مانگا به ارزش ۶ میلیارد یورو در نزدیکی پاریس، الهام‌گرفته از مجموعه انیمه و مانگای ژاپنی "دراگون بال زد"، توسعه دهند
🔴
این ایده پس از آن شکل گرفت که امانوئل مکرون، رئیس‌جمهور فرانسه، و محمد بن سلمان، ولیعهد عربستان سعودی، در جریان بازدید ماکرون از عربستان سعودی در سال ۲۰۲۵، علاقه مشترک خود را به "
دراگون بال زد
" کشف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/143724" target="_blank">📅 17:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143723" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b43ed20b.mp4?token=Zt5g4yf05G7JzFDSDyYbTA3NOdZWJnQ6_1L-1nGbCIJyhoKzpX3jYCVB6EmGW_fdiq-1OPPa2ZZT_wM7waonIK5HY8x8dMGHozFppb4G9sW6NNMkFn2jri9uThzF6qv8-2d9tg9ZMmKKHRvXh3zGR3w_xp3bgB_C9J4M5M0ex-5FhjCFMfpSBh5Vua2jY_9IvGv7o5MA0Y7TqO0Nc1qmV5XmV9K5TLEsMzUbmVEHGcgTgrMRM4DfqVJMPx3T0i_93xA-A944Agu098eL1QEsN2BWSLk9-QAtOrJsIZO6DAx8PncQGTE5lTqVBfxhjnt-TEle-W-h3_WLWNyDgVR7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b43ed20b.mp4?token=Zt5g4yf05G7JzFDSDyYbTA3NOdZWJnQ6_1L-1nGbCIJyhoKzpX3jYCVB6EmGW_fdiq-1OPPa2ZZT_wM7waonIK5HY8x8dMGHozFppb4G9sW6NNMkFn2jri9uThzF6qv8-2d9tg9ZMmKKHRvXh3zGR3w_xp3bgB_C9J4M5M0ex-5FhjCFMfpSBh5Vua2jY_9IvGv7o5MA0Y7TqO0Nc1qmV5XmV9K5TLEsMzUbmVEHGcgTgrMRM4DfqVJMPx3T0i_93xA-A944Agu098eL1QEsN2BWSLk9-QAtOrJsIZO6DAx8PncQGTE5lTqVBfxhjnt-TEle-W-h3_WLWNyDgVR7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به افتتاح پروژه نیروگاه خورشیدی: یه کف محمدی صلوات
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143722" target="_blank">📅 17:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عقل عرزشی:
+باید با همه بجنگیم
_خب محاصره شدیم و گرونی اومده
+تقصیر پزشکیانه
_خب دلار تقصیر کیه؟
+معلومه!همتی
_دولت بره توافق کنه؟
+غلط کرده! رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/143721" target="_blank">📅 17:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECIuhqrNKYOgQVoVtZsRsH8Dk4GoMSSrUO7PmL1sNRnHK0004T3Tv7nvWcMx2TCk4zble6z1j99eN0cEa5o7IYq3kWwvbXzZynIDU_ojhdWHsVYrRVQVG6nCKIrbv0HmqTp2ja4pNT7jOkNZ3qXOjypY_1ExEwHbhwXy1VBFBWS-y736jKKCQTG7QKY1uG8wGvhsO-EkxGlDzGuLEj72oJfM3QDQyLHbE8EalpYxhvClGOyuMxW93vkci7agHTWx158qwUEtja8Dj2b09VOvOJ9enuxMJIGRbuhzUs_POGJ0ZlJQvvdeSVxDM9KkcxlreWKFkH0jvEm_9kPkEXtjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کره‌جنوبی حاضر نشد در خلع سلاح هسته‌ای ایران به ما بپیوندد
🔴
با توجه به رابطه بسیار خوبی که با کیم جونگ‌اون، رهبر کره شمالی دارم، از این واقعیت که ایالات متحده مدت‌ها پیش با مشارکت در رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده بود، راضی نبودم.
🔴
این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش زیادی از هزینه‌های آن‌ها را طبق معمول ایالات متحده آمریکا پرداخت می‌کند، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری می‌فرستند که تا زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده، تهدیدی ایجاد نکرده و محترمانه رفتار کرده است.
🔴
بنابراین، با توجه به اینکه برای لغو رزمایش‌ها خیلی دیر شده بود، به پیت هگست، وزیر جنگ، دستور دادم رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد.
🔴
در موضوعی که شاید چندان مرتبط نباشد، اخیراً از رئیس‌جمهور کره جنوبی پرسیدم آیا مایل است در خلع سلاح هسته‌ای جمهوری اسلامی ایران به ما بپیوندد؟ آن‌ها گفتند: «نه، ممنون!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143720" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyjNALdk-wwwaQ_TpDvQtwQZbSNGtf_5_YYwZL5FyjO0p8PS0UJWsDQ0M8Y6mWQBzX5_xoL7HFTOREiXseYasAQ_RIsur9Q4455UOYiUdoSFBATMnqOOdckAuM132FPkIh6E7FIKMhR1PlF4AiEfwPcLguLTyikvGnwtSrWu8XYlioBzui4_K-Ze-W0ANOqnoYdQ6xWpIhLq6EXSI7a_RgFcLNw3h__TAKM51PPakVMP1fv84DG3jn8QFNosiJ8dAR6v9KwZqyzLSvvRt1I_VPH0La0LcNiLrzxgSpe4hHVMrsLxNxPSGjznC9clAvcvSDPj5VnHtet7m2bzmyxQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: با نون زحمت کشی به اینجا رسیدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143719" target="_blank">📅 17:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ویدئوی جنجالی صداوسیما؛ نقشه ترور بارون ترامپ!
🔴
صداوسیما در اقدامی بی‌سابقه، اطلاعات محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143718" target="_blank">📅 16:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKYAre6tG5WbJOn1zxNv0z4vMH3xiBeX-Y5nmYaHVn_fvt75Y-GpG90hKt5IlLnReMDhrKctGmQe8Qx_pmkGAdw7fvtk7bIPwv0SXbVhr_bBuDdLt_cLwP4YLSv9J5hZM6mF3b1cajinLqe0xpinXZ3qehZSZBbvg6JXttRjTQxiwyt1lhsHHjrA4-P0-u1-L-qc1XDBLkPLs4unZWxqEq5pKwVxEakZ-CvsD613C7wDG06G9NWP6SPLAKpDavszaCsJHPe-RZELEbamuFcKdzBkuqTtw6HUAQz9WbZJkQ9T-D4Vm9Nwej0C4RuznhJqJWAK8lm74zbqOTHGehKo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/143717" target="_blank">📅 16:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxv6uyHeg0LOr_XihUJdlFXDXsDdt4PpvWAVRYI3sywJYUjM7ra_lKBPgxpGgPOUAhCSWgoSx1FDHt1wIWSIvEMBQ8xD9tOiZOfHEMjHER4ZA1gcAuATLs_ezriEw2IOeP5gf-NO-z68UyT6sbcrxBFF7g8hScLnGao3C_xXDitNle5RGaaUOBzlBXQ8TAG2WK1VbybqAbVUY-ml1aAyVaVRMWxYmEz2cgYxzGwKMFU1g7VjiZX3lU5GcROHUHN5n2JGZPN5t_qjgr2m4-GKWhAHGbIMYsU664F8wm98QlueizDFcQwOLDSJW4PylexPtpM5dDxITWFzcG0d7H-l9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اردستانی، نماینده مجلس:
درسته مردم از فساد و دزدی ها و بدختی دارن پاره میشن ولی با این حال بازم پشت نظام و ما هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143716" target="_blank">📅 16:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRlC8VQ3e8YXQD6nCniI0NT1w-Nvov7w2aNAQRnKuQ-6qlMbfRWP0FY7ZJuuqIeuUuv2pCmmeeuoeIiQdhoibmZWXKnapsHTaRvSh2iIoYLiMYexPsM5SiL5WPST7_NOq_VA31DfI2WGP9wzdPU6WPJBKnm0IiHvhiVQeP4qEoSeX72COt2eHcLEZqBFIRaIRH-JyVY81Qwu7U0xck8nYvSMwcpG56Mv15EQEo-aYeKAwZvdi9aBOopGOfTVz1RmF648suj6VnuoSsdnAeXXMn9d7SQIUhG5lqykdNOq7rMyw85nsHRogVc_jayLv5LF8dBiNSGrEJSt2On4iFiVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متأسفانه یه دختر ۱۶ ساله در کردستان، به علت فقر و گرونی، خودکشی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143715" target="_blank">📅 16:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_lYaBndHvHTCvIBeggdiy-LBw7Cf0on9zC-a_YF1zH2qjW3cebwtAsR5L2WUnqfpbKjYpCBYAP7UlapqgqO_SGiigkJ4sKMCgNzB32DrT06bAYaVLo7e2DfWJ0rwuGMHp6cIbTiEXcmNLN4GqKu56iac_CllDr9YE1lVqfexEelZK9-tIR6KKfqToxkgX3CM73MBPC31E93x6k0X8Fa_k7c0OlIULJd7KVt5DEbXYLRJZM6OczWNxd072zdmmYOFCv06hza33HozRogmCk6Zm5_cwqlNu8R84RhD427S6HWHI0t27yEvc9HhNMGDztN04c4-zeuLN3QDe18PgUgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیفون 17 پرومکس 2 ترابایت:
1,000,000,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143714" target="_blank">📅 16:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
طبق گزارش‌ها برخی سنگ‌ قبرها در بهشت زهرای تهران توسط سارقین دزدیده شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143713" target="_blank">📅 16:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر صمت اعلام کرد بیش از ۶۰ درصد ظرفیت پتروشیمی‌هایی که در جنگ اخیر آسیب دیده بودند، دوباره وارد چرخه تولید شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/143712" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGOt1tqFIcrudAmONfos2msz5fIGLOpzD1O9ATFmYfc0Ty-rj8KpeRmyjaef5hoOkQut0ZIpUhSP-vpGovnYiXi9KAKAUzH4sVT5xayO5N0PCk2Y72qpTXWdy-fwLjzEHqocJhBeWF2-IXDCoVITXSSndV_L_SvbJqvCCqWrSJ1ovfsZoOnKByIqL-EovuBnWruPtS-UsupZoXKgvmtrpqzC0ifFiYA-nAbfvcsitmPTFzBwu0k_Rdb8xsH-vA2dEPJcXIBz4VUdy3Ui8ObWW4bEAgH11F9T7jG6d33Tt8wSDTao5BeRur1-mZMp84b-Irh-ufCnjfVupH1n-lxJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس و دیسبک طرفداران پهلوی و جمهوری اسلامی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/143711" target="_blank">📅 15:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdaoJoa5qkwTdifyOmTU2GALONjA5ZffQGyCjIDJcB4su9aFC31ENQcNG0rQeIleU9oP4hYALBqIjnOLWI3btDB46z8ghPZRurc5Uik7OM845KMvnT7vmyr7O2_7ok1SeJ9yZthmrHVT5h_iDIKtGO9HfMZ_P1rOqXkxzFhYWiSWjB6RGdUs6SaM3cDsk_Cj-GoX-LbBqmZ244sY-H_MPETSZpbHXhwS-H6yC6v3meu8Nqa8qNX1SQPOBIbUoFUmu7XslSff-7GU16NnEw6a31QjKcJGeEE05fNHL2Wsf8wzzvTQY26qkRY6XEC-7oh1PKRSqEK2ipLmKX-355fbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ۸۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143710" target="_blank">📅 15:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
برخی کارشناسان اقتصادی معتقدن که؛
به دلیل‌ کمبود کالا در کشور ممکنه دولت قیمت ها رو خیلی بالا ببره تا دیگه همه نتونن فلان کالا رو تهیه کنن و اینطوری دیگه کمبودشم تو کشور حس نشه.
🔴
کالا وجود داشته باشه ولی به خاطر قیمتش نشه تهیه‌ش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143709" target="_blank">📅 15:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
خبر مهم درباره ابر تورم
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143708" target="_blank">📅 15:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjOv1kcRkrohL9LcPA9I4eokcbcIV2dv2Zl9r2zLxGVYoZVWj0MrOuGFuB-GCNMW801ep4Wkj1M_zR5qa2w6xqJ5_HsqzpcJNW_oYqtfB3mz2xccq2-fsRfrQJjJiOv_rT9orpSPI6Wr7XRM9nT6yNRTIgFvX9_Mx3BIVNh4Zm7gSHHmOnW6JnCQMdmHZjEFoHNLkZV7YqCrBp6xU0Qut9UVH4NR_iZhjz4jya4AYhj21R4P_cSXlbuMO3_djZgYzWVPJrvELwExA7492khvkAwSAv4i3mmsHo4NarR4Tf-G_m05EaXyCatqJAoufQXxG98tchKDQqZScvzwPQwa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بوسعیدی هم یک پیام از آمریکا به ایران آورده و الان داره با عراقچی حرف میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143707" target="_blank">📅 15:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143706">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uijEFOx_G43gisFAOTGfKO2c9Mm2pA0ssIsRePEmm8mbpJwdLuTkmcw-AsOonPMsWxSsonHEJ4GOsWdslKxrLk6W_YXuY_A8t58pMq2w648KLasKVZ9vjT15Lyr1_gatGkSOqePlf7HHbZUn5DdcnkOCwCduaNjvOSaCNOpVMho_Yb-VTRFNv3NMAiLofmskGd5jlO2IndemYgO8nYtRxpAS1b2njtW3-edUAo1Bxq7UegArMeeIUH6DTTUAt3eVcJza3QktUafodK8kG5scOR8kfXJG_ZCDOGr0G-XdM2Jv0i6N85vH_GFkMGwE72NtC8n8aJlm82VL5fajITCQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس
شلتر
:
باید سواحل آمریکا رو اشغال کنیم و همزمان واشنگتن رو موشک باران کنیم
🔴
باید با همکاری کارتل‌ها، تجهیرات نظامی رو به مرز آمریکا و مکزیک ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143706" target="_blank">📅 15:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-GL7xRC2efZYiUz5udcGQtOBTiHeH_Ryhr_0NySH1HGOZZrGnCJOh7DcTdOBHw0XyDi0GqPpFiDy1N4l8mLwi-MDdOmkgeUe2mb6-hlha10TJfhDEhul-V9QFU8dXZPkQkPwLL8nT3s9a5CLJuoCJF_aV1Lcea90ip9hyu4t1wHCrK-YSKwKMmHDx7YDTUNzPHKJvPLDMEZ1Q49rm-A81rclGflzCZ4eXJ0l2mLkISJ9gSd-mjt6UrzP3PU4QkvO3guSUbPk9h0XW5FYrx8UpSz0AuS-Z9BfFk8WxhKzJReLtFaaIwY7E99TGcdxjnhjNQ7C_hNRfbuRzojIfVe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی ایران در حال سقوط حتی حقوق بخش بزرگی از نیروهای نظامی خودش رو هم نمیده، ولی همزمان داره معترضان رو میکشه
حتی آدم‌هایی رو که اصلاً در حال اعتراض نیستن، اونم در سطحی که قبلاً دیده نشده
🔴
چیزی که الان در ایرانه، یه بحران انسانی در ابعاد بسیار بزرگه و باید همین الان متوقف بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/143704" target="_blank">📅 15:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0AlOzCVuWoPXBphtio1Yl4lDMM0x4Tgq4qXilyi3GsKGmUgpHc_vYHZAk-q0olu2l71KhaaZ_eAUZATFq65AWmkTh1gXqsxGMjPeesbck61YJWcRo8hGnCyAO2eTHbYO-zFm9RtGQ2HOBmGQtwLaDi7XY_qGiFZQCrHN21Lb2Pm7m2pGT58jKeBw6z-lVMkQQ3U_NNacouiplIjSvLVx2sH5TEGVxbtp0jejo1_1cHQqwyBl9v5QhyCfgVTKEH-jGXXU8OfJWuqMAIEXSMGphIFa4lsUz8pYzRQxiOokdYC62SHyPf00Sym5ituJkAmEX-F41j0wh7w-zcUF5dTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: هر فشاری که معیشت و امنيت مردم را هدف بگیرد، بخشی از جنگ است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/143701" target="_blank">📅 14:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قطر: ایران با بستن هرمز آزادی دریانوردی را نقض کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143700" target="_blank">📅 14:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e42e42d81.mp4?token=uh-VFDGEGzEsqP_lkYkUr3dI-PiJgM_9EzjrzDZ2iG4b-_NWkNqJ67e3OzpVcTtNH6Lzh3wl_RrRESvSh1CBwz7Yrao4InShTYTe1lLXSM0x0UWSgmYbC0sW1Sk8-pQEjDj3Zt7nfmJ1_UtPihXbZHBOpFLDJ-8_oWD5R5mpi-45WBZBDN3oRkwxgpCJH56LNogMaslHurQCggJpro-nj2h4UEMyfhMXQRwIzD_FjpQlgDOQZuEk04Q-xi_uFSnkInCeqh6sieQ5hlf4Ub5GC9YwQwsB3S18jvr_pyQ2pb7-UJ8kd-Bsb4HaUl7Uhuq_aJbsi6WxuGQq-KMPCkMlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e42e42d81.mp4?token=uh-VFDGEGzEsqP_lkYkUr3dI-PiJgM_9EzjrzDZ2iG4b-_NWkNqJ67e3OzpVcTtNH6Lzh3wl_RrRESvSh1CBwz7Yrao4InShTYTe1lLXSM0x0UWSgmYbC0sW1Sk8-pQEjDj3Zt7nfmJ1_UtPihXbZHBOpFLDJ-8_oWD5R5mpi-45WBZBDN3oRkwxgpCJH56LNogMaslHurQCggJpro-nj2h4UEMyfhMXQRwIzD_FjpQlgDOQZuEk04Q-xi_uFSnkInCeqh6sieQ5hlf4Ub5GC9YwQwsB3S18jvr_pyQ2pb7-UJ8kd-Bsb4HaUl7Uhuq_aJbsi6WxuGQq-KMPCkMlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پزشک با گریه: مردم وقتی مراجعه میکنن میگن توروخدا دارو کم بنویس پول نداریم، بعضیا پول ویزیت هم‌ حتی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/143699" target="_blank">📅 14:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=mud3opm0QQdcQl6zwv6SKUfpZJgEHoOx3eKzm1Kl55oJP3WRURfmP5yEDoks1wdT4XBUVkKHRcVDzQF_6FItI1zXAN44Xuhijd0CYTsAtvE0Ld5fEjdRDBvX5-iKMTnIjF2X48mO5foUlgYPgU8IXXLd8L7b1_HGOqXuc2lNk8j-pfE0KYcqvtMJuFzlCGLHoEjm5aGYKAF4yYsVspN-j0Le4Qj2q3dTFTlPaFUHa5eB9dfmowj-Wqg_eeUPh_Ta9Ao85CXEj54LECaIbri7olkFyBEjNz4tpSYScThzo8cg_rYzwc-pm8vXaCAe9tSBjGcKb3IGIk-BFzS-Nv6p3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=mud3opm0QQdcQl6zwv6SKUfpZJgEHoOx3eKzm1Kl55oJP3WRURfmP5yEDoks1wdT4XBUVkKHRcVDzQF_6FItI1zXAN44Xuhijd0CYTsAtvE0Ld5fEjdRDBvX5-iKMTnIjF2X48mO5foUlgYPgU8IXXLd8L7b1_HGOqXuc2lNk8j-pfE0KYcqvtMJuFzlCGLHoEjm5aGYKAF4yYsVspN-j0Le4Qj2q3dTFTlPaFUHa5eB9dfmowj-Wqg_eeUPh_Ta9Ao85CXEj54LECaIbri7olkFyBEjNz4tpSYScThzo8cg_rYzwc-pm8vXaCAe9tSBjGcKb3IGIk-BFzS-Nv6p3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند مریض: اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
#پفیوز
#لاشی
#دیوث
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143698" target="_blank">📅 14:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=VqeHRgMbfm4mMHlcTGJUJnVurWsnJUWFCKgkEZZvwcAoY9WmezTXpaxOB59GUSrZCJP3m7A-qEIJLytEEsopj0IJp87wWsPA4HHJ9alA8zW8L6SAfuGAQ1CsZnhdXJc2Qt4nn_9Wj8f8GdJZ0OZ7MjyfKTNZgOc1oR4v93uIKWVVopIFm43vyLtGs9eRGUoY7hW6Owv_ha5RkQcRwNrVh-Yb8-e-ajufe2hxR69iVU4MJXhJFsTb51ZLZqxFgMNkRTPzsRJfAvFOi_9VC8p1nqsif_M590orI77sgupJBk5FsJ3D6MCgL4S9hL5ZkNX3C6GK62h9EMKcsLgn_nda2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=VqeHRgMbfm4mMHlcTGJUJnVurWsnJUWFCKgkEZZvwcAoY9WmezTXpaxOB59GUSrZCJP3m7A-qEIJLytEEsopj0IJp87wWsPA4HHJ9alA8zW8L6SAfuGAQ1CsZnhdXJc2Qt4nn_9Wj8f8GdJZ0OZ7MjyfKTNZgOc1oR4v93uIKWVVopIFm43vyLtGs9eRGUoY7hW6Owv_ha5RkQcRwNrVh-Yb8-e-ajufe2hxR69iVU4MJXhJFsTb51ZLZqxFgMNkRTPzsRJfAvFOi_9VC8p1nqsif_M590orI77sgupJBk5FsJ3D6MCgL4S9hL5ZkNX3C6GK62h9EMKcsLgn_nda2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجموعه‌ای از انفجارهای اسرائیلی شهر "المنصوری" در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/143697" target="_blank">📅 14:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فرهنگستان زبان و ادبیات پارسی  اعلام کرد: معادل فارسی واژه بیگانه «لانچر»،«پرتابگر» می باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143696" target="_blank">📅 14:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
الحدث: عاصم منیر به مقامات ایران اطمینان داد که پاکستان در تلاش جدید، به دنبال پایان دائمی جنگ است
🔴
محسن رضایی به عاصم منیر گفته که تهران پس از رایزنی‌های داخلی به زودی پاسخ خود را ارائه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143695" target="_blank">📅 14:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1525fa44a.mp4?token=JpuZTClsT0uLaJ0vwXxhf2Zieyzw7QtgjuVgDE65oMDOIiaLZ1viPMsH3luDXah78yXhEVOR-BO_QCGvlTKCqwv4Kd6Gday12ENEHytbVcp5iyXZiHHL-sz2JXriiCnpxY52otR7xuy9kQKo3csaJdnbeOpZyau3276ZnLaJ8i9LOeW8ezkF5j-aqsVXGsL2ckUY9vipCg-z96Hw7Llgdv-i0rNlVBsPBDv-OSJrLvS0D6imiTDiAJMaQvJTOo04JJqGmX-EwfLfyYgmkt9l7ePe8MA4nHkADo7LbYfk7HufTuHep9ybGZuQilPrywDvN4cEge6o6Mu3pgx0NlEjRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1525fa44a.mp4?token=JpuZTClsT0uLaJ0vwXxhf2Zieyzw7QtgjuVgDE65oMDOIiaLZ1viPMsH3luDXah78yXhEVOR-BO_QCGvlTKCqwv4Kd6Gday12ENEHytbVcp5iyXZiHHL-sz2JXriiCnpxY52otR7xuy9kQKo3csaJdnbeOpZyau3276ZnLaJ8i9LOeW8ezkF5j-aqsVXGsL2ckUY9vipCg-z96Hw7Llgdv-i0rNlVBsPBDv-OSJrLvS0D6imiTDiAJMaQvJTOo04JJqGmX-EwfLfyYgmkt9l7ePe8MA4nHkADo7LbYfk7HufTuHep9ybGZuQilPrywDvN4cEge6o6Mu3pgx0NlEjRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیده‌نشده از اصابت موشک‌های سنگرشکن به ساختمان شیشه‌ای در ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143694" target="_blank">📅 13:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تحریم‌های جدید آمریکا علیه ایران؛ فرماندهان ارشد نظامی تحریم شدند!
🔴
این تحریم‌ها پنج حوزه دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی را دربر می‌گیرد و به گفته آمریکا، شبکه‌های مرتبط با تأمین فناوری‌های موشکی و هسته‌ای، عملیات سایبری و انتقال درآمدهای نفتی ایران را هدف گرفته است.
🔴
در بخش نظامی، امیر حاتمی، فرمانده کل ارتش، رضا طلایی‌نیک، سخنگوی وزارت دفاع و محمدباقر ذوالقدر تحریم شدند. همچنین تحریم‌های قبلی علیه چند فرمانده ارشد نظامی با مبانی جدید مرتبط با فعالیت‌های تسلیحاتی گسترش یافت.
🔴
آمریکا همچنین شبکه‌ای متشکل از افراد و شرکت‌هایی در ایران، چین، هنگ‌کنگ و مالزی را که به ادعای واشنگتن در تأمین تجهیزات حساس برای مجموعه‌های دفاعی ایران نقش داشته‌اند، تحریم کرد.
🔴
در حوزه سایبری نیز چند فرد مرتبط با وزارت اطلاعات ایران به اتهام حملات سایبری، سرقت اطلاعات و دارایی‌های دیجیتال هدف تحریم قرار گرفتند.
🔴
بخش دیگری از تحریم‌ها شبکه کشتیرانی و «ناوگان سایه» مرتبط با انتقال نفت ایران را هدف گرفته و چند شرکت، فرد و نفتکش به فهرست تحریم‌ها اضافه شده‌اند.
🔴
واشنگتن همچنین پنج معافیت تحریمی مربوط به برخی فعالیت‌های آموزشی، دانشگاهی، ورزشی و حواله‌های شخصی را تعلیق کرده و دو مجوز محدود برای پایان دادن به معاملات قبلی صادر کرده است.
🔴
در مجموع، اقدام جدید آمریکا علاوه بر تحریم افراد و شرکت‌های مشخص، با قرار دادن پنج حوزه اقتصادی در معرض تحریم، ریسک همکاری شرکت‌ها و طرف‌های خارجی با این بخش‌ها را افزایش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/143693" target="_blank">📅 13:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0fgTCpPv2Kmd2IgpA0-XX97ayTMHMIkIqgXE1igZ4CEU6RIADx3KU2PrE-CY7JAyqzhHnZ-6vfKCHDRIzJY8dVs5wanCiVsLBnZbXGhaEGsNSbaRMqC31DIvRie7uLaasd7X9YDWMtO7Ggdx-Z7fqQy50fxLO5cibdWoybW1sWwqd4EjciU0LoZsiKvLArJmL_sn4OY1hXagscLaAqQVV0UmDlFRRqt-fCy5-7ZKfpCNluOxXaMI3sTC_LgMh2qIXoHvWqLH8KVgM4B7rR-eJlG49VD6rx4Y-kiQRhtM8blB03LO56lkqdumyGi8uwV4ku9s1wVr6SjpPFZuSdXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر صمت: ۸۲ درصد مردم از عملکرد دولت پزشکیان راضی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/143692" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اختصاصی/بازگشت طرفین به تفاهم طی روزهای آتی اعلام میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/143691" target="_blank">📅 13:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyUfIPU-IKTSTd3uPsExrZf2xKJxXRYCnNS9Asr4LRbsa9Rr9RbZAy5KxvnkNxc-wuem9A2nJigxdpPeEx5mPbcFmpfjcsIFRR-L6QGAYn_ToNVnznEeUZS-XJr42xtZ-nYtNyvPgabAYqqOo41TjfNZNkirOTNNC7IFxOjAZTniAsR1jC2QZ5YNizB_ryUpUjYGcJJ5reJw9RCk4Zqpojnt0Ac_0HIjyCpeaJnIFrNOeUqfpkZZYoecgJmd5pdXLLYDwqGd-B87_1Lgmqv0fUAxoVJ2RhRMCdtEqd7Z_MafzKUD2vCm2RhSX1oQAsUxeVPx1pS5XV8hAwT96RNvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیبایی کوچه‌های رو به خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143690" target="_blank">📅 13:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رئیس سازمان زمین‌شناسی: زنگ خطر فرونشست در تهران به صدا درآمده و این پدیده در شهریار، جنوب ورامین و بخش‌های جنوبی تهران در حال گسترشه؛ فرونشست از حاشیه شهر به داخل محدوده پیشروی کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143689" target="_blank">📅 13:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgdDwbmqzpIBqsCyfNYRvjM7jZu5qM42zl1krWRmie2JiSq_ZKMPLKhDrFeiraz5CuPFwu7bemRpAQHU7Ww_xAa2dyjcxJML0ZrBBf-DqP-Mxna9yxfqoLw2yEjPgvUt9O--6Y-fyR7hWmSXd28EIPPVpaeTVxinbgeucJiI_Ujmk6lXplg1qasdmDP50G9cVUptAl_YMs8CSNExMMN4yHMNQwKkaQsRjAEccp-dIDOlzdyymhtHGdA1JU21ltX7s5Iqdtr6KMakxlvmVnpyJX69IBPyJUgSRKm0IHhu5ybhBxUbGBVaDNLouXXEUqjdYjhXyam46NGB7T5lTIbYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: دولت ترامپ قصد دارد دیپلمات‌ها را به سفارتخانه‌هایشان در کشورهای خاورمیانه بازگرداند، که نشان می‌دهد واشنگتن پیش‌بینی یک درگیری گسترده جدید با ایران را نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143688" target="_blank">📅 13:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ماده ۲ طرح مقابله با نفوذ بیگانگان امروز در مجلس تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143687" target="_blank">📅 13:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز، از نیروهای مستقر در سوریه بازدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143686" target="_blank">📅 13:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرنگار الجزیره به نقل از مقام ارشد ایرانی: مذاکرات با عاصم منیر سازنده بود و در جریان آن، ایده‌های مفیدی تبادل شد؛ با این حال، هیچ پیامی از سوی ایران و آمریکا به یکدیگر منتقل نشد
🔴
هدف این سفر، احیای نقش پاکستان به عنوان میانجی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143685" target="_blank">📅 13:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143684" target="_blank">📅 13:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: در طول ۶ ماه درگیری در تنگه هرمز، ۶۸ حادثه دریایی به ثبت رسیده
🔴
این حوادث دست‌کم به کشته شدن ۲۰ دریانورد یا کارگر بندر منجر شده
🔴
کشتی‌های با پرچم لیبریا، بیشترین خسارت را متحمل شدند؛ ۴ حادثه هم برای کشتی‌های با پرچم ایران ثبت شده
🔴
حدود ۵۰ درصد از مجموع کشتی‌های آسیب دیده را نفتکش‌ها تشکیل می‌دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143683" target="_blank">📅 13:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phB_EW3FCZQE8rs9sRTjANywf7k3fbnvL8u-oz-l00Cw8kO4R6zF0lMMreIA7H1gbaOLlKhQQcbd95P27B1VKNH0SutU2qlsdDEkeDFxLmha6n534filUkQR2waTzyishwLaoyqCXun3yj6OSluykkJdOfO-xlKAphyl6UN8eQ1yJeqKzkoY4fnafUuKemsyR1P50lj8TEQ9aeObNxZq6CU8iErB_ebQ78FqHYfuarBKn5IsEe7W-QkyOMliofxJFWMEyLXHgMxg4aGrGv2Bir9VCItoaRygF4LsY2gZeW35vV_pcMdjc0G9cg8DBcfi560-ckRxlf5x1aVX3kDKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: محسن رضایی به دنبال تحقق شروط تفاهم‌نامه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143682" target="_blank">📅 12:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=Vzj2hWZvV-nOQjcu8X0RPshd-U2nmLzWT4xAtSyFDwtvJ3cYF775lrUj_2ArIPIWsmV4OWA-g315JHa-CdZdibM97B9Z2DH370CXbXe7qdSnxdLJx65_2xVt9BPuaIMIrdr_Jr5E01a1NzCdt_yj03fyAYeJSQIPqfZCbHLIIY3XE8bMtSQke3tsy4TX-d2VwNtpW5PkxnWyAIcu2LQJvgHeJ6J6elwM8HQfCPNyKHIa95M8lveQHnGpa4mgilKI94wC-z2BSzgjyT66xVe6tHnetUEOwlbrbopERGt2781egDjOIQvoVXfTwvrIaOqDtrCgZccec70oOXlxVdFcyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=Vzj2hWZvV-nOQjcu8X0RPshd-U2nmLzWT4xAtSyFDwtvJ3cYF775lrUj_2ArIPIWsmV4OWA-g315JHa-CdZdibM97B9Z2DH370CXbXe7qdSnxdLJx65_2xVt9BPuaIMIrdr_Jr5E01a1NzCdt_yj03fyAYeJSQIPqfZCbHLIIY3XE8bMtSQke3tsy4TX-d2VwNtpW5PkxnWyAIcu2LQJvgHeJ6J6elwM8HQfCPNyKHIa95M8lveQHnGpa4mgilKI94wC-z2BSzgjyT66xVe6tHnetUEOwlbrbopERGt2781egDjOIQvoVXfTwvrIaOqDtrCgZccec70oOXlxVdFcyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به پالایشگاه نفت آفپیسکی در منطقه کراسنودار روسیه حمله کردند.
🔴
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143679" target="_blank">📅 12:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
چین: در همکاری ما با ایران نباید مداخله یا مانع تراشی صورت بگیرد، زیرا در چارچوب قوانین بین‌المللی انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/143678" target="_blank">📅 12:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سازمان اداری و استخدامی کشور: ساعات کاری دستگاه‌های اجرایی تا ۱۵ شهریورماه از ساعت ۷ تا ۱۳ خواهد بود و کارکنان باید ۲ ساعت باقی‌مانده از زمان کاری روزانه خود را به‌صورت دورکاری جبران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143677" target="_blank">📅 12:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de76922b9d.mp4?token=kAz7es_-I5ar3p6Iv7VA7Ne2dQ3mnIU2bbkiOA8kWO0uC7YfOFbwTyHk0wIK13by1ZEMX7QVCNnEPM_7g61eWXcdFDOBPdgoxfLgqpPvZGZCK4u8OsJy6-csc9KbFojVNjHMUJ4RllCqBCb-tkMCdlmwbRgNIxa1faMlCKwg-c4ROgHwcQolRTOdM-kRp8T-HmKvrjf1EpaxeSrOVUXBS92Hb7MJV9lbv9iAwhVbPlWycBR9oXOFWvSIQ0_Oa10aLj-8tPTAyX8iIi7zsEFuLfl2xMToaSEIEWceLHV7buIdAIupnNCdrzvf9fUsaaYaGP5arREIUjYVy2_IK1VqKmp6zQZurl7GUavb05wjPsNcV0fpOV6j0aevzGWsMO9gs08bjCDp5qN_xHL3W7FuJfCnvHFN6PknBIJZxTuUFRO7sFGrymTanGA7pLLUNAOvGvcZ8Icd-eeNcxd1sHq9p26WKYtBir5N4YKOumrKls5ETEztPxHgur_Mckbap0bCwmn1DAB8l7CrJrJnbwYw2V5zO6pPtpJxKw3bsid8lzdbOMeSNAQEdfifY7GLu_23makFiQfFnIt8mK-QZ5FgrAGTFReGA4uTu0W5TRP6AhkYLkRFwo47Auj3UW8ib-QHmEuy6-SMtjuI4P4Fj68ClUhKgJlzVlK_Cow2W-M56vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de76922b9d.mp4?token=kAz7es_-I5ar3p6Iv7VA7Ne2dQ3mnIU2bbkiOA8kWO0uC7YfOFbwTyHk0wIK13by1ZEMX7QVCNnEPM_7g61eWXcdFDOBPdgoxfLgqpPvZGZCK4u8OsJy6-csc9KbFojVNjHMUJ4RllCqBCb-tkMCdlmwbRgNIxa1faMlCKwg-c4ROgHwcQolRTOdM-kRp8T-HmKvrjf1EpaxeSrOVUXBS92Hb7MJV9lbv9iAwhVbPlWycBR9oXOFWvSIQ0_Oa10aLj-8tPTAyX8iIi7zsEFuLfl2xMToaSEIEWceLHV7buIdAIupnNCdrzvf9fUsaaYaGP5arREIUjYVy2_IK1VqKmp6zQZurl7GUavb05wjPsNcV0fpOV6j0aevzGWsMO9gs08bjCDp5qN_xHL3W7FuJfCnvHFN6PknBIJZxTuUFRO7sFGrymTanGA7pLLUNAOvGvcZ8Icd-eeNcxd1sHq9p26WKYtBir5N4YKOumrKls5ETEztPxHgur_Mckbap0bCwmn1DAB8l7CrJrJnbwYw2V5zO6pPtpJxKw3bsid8lzdbOMeSNAQEdfifY7GLu_23makFiQfFnIt8mK-QZ5FgrAGTFReGA4uTu0W5TRP6AhkYLkRFwo47Auj3UW8ib-QHmEuy6-SMtjuI4P4Fj68ClUhKgJlzVlK_Cow2W-M56vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلینتون: وقتی می‌شنوم ترامپ و اطرافیانش درباره سوسیالیسم و کمونیسم حرف می‌زنند، واقعاً برایم خنده‌دار است.
🔴
رفتاری که او دارد، در واقع سوسیالیسم برای ثروتمندان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143676" target="_blank">📅 12:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143675">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DphX9rrPsoyZha4wYYensqR6MniD1ED2fRThieRpZWXgdSEXha_UT4a4d_hIyIQgOA54Gnwh6kZtHIDyajnosyJk5-KlZe8ORB8KKTSYNpAAE-OI56r7Gz-xkS3rCkNW3rIOsFcNGmF-vNDqfCfPv-nDfNw_3yV5Iwbpz90m-2NDVOSDsuil8lYr6H10KGaOqczhGXuJqlja6K_CpTbxf_bfmiQyBrWWa7MhWRMYJmlThfsr7kOtKBZL08ygx6-JDVruxpcwz-6Q4qqyePZyNzNL42j2wRS3Qzm7OAB-VuoRp35GHk1lUa6IvYoeGQXKMdL1MFXzT2DA3J80Q82TjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، شهر خیام در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143675" target="_blank">📅 12:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drXhYpt8rBM2MZYWxvTduJ8-PbmfmFP4RhfC-nFWkAyw3A3QGjDVrWXZQokaa1hZArc1kjcMHTpYAYpUoYBudJqXQgxiiqaRUnhmBwTh4pk2P80OP3AmDRm2XjCDaMMdUDEBjCF4ngGat75fnSdH0JTpk714Ew1hiOIiEMEuOpan_BoOQ_ClcoVKyLX18tdGqkh0TJFtpTHgrcMlouzrI3616BCmU1d4c5eYOOrWO2nYif3RFLoKcUyZJkEkAxUXx0m4-QrM3DbpRsuqKEGKojKx0OgrWC49wemeeV4oPfVigSGELf4-EHClmFmO8g9_GiOhA9M1z-rIezG5qRYkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توله هندی شبکه خبر: لازم باشه باید با همه بجنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143674" target="_blank">📅 12:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
برخی کاربران گزارش دادن یه سری پمپ بنزینا میگن بنزین نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143673" target="_blank">📅 12:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50c75dac6.mp4?token=vmzbhgruwuGQ6F3uTjtCbiy8KwO-5YT9FDUaP_kJhcB8MKB67jF8onmKUYxKNjokYIZlt2U8Aqq-jLoPHLksmOHs0MJ5El56HSZ1x7oGtrQB2rz0pLPKi5ejYkR8H4FnM7aQDeC2hU2o4vKUF0Cn9TqBDEQO0zKWBzC1o1iOsG4XSgzFzxt17VsqfQMjvkILBTnlfYkHXotBJCPyyVoontpuztj4-9W3G2zsLrcPpYvVBl0skmIyM4ZWSVKxKzPe_sLds2c0QZeRBGmuZrr0gUzYn1BHQ_iIh5Irm0u6ysu68SoXLErXJPBc0EbrYkZkP86uWgyn1_7fiG56jBn-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50c75dac6.mp4?token=vmzbhgruwuGQ6F3uTjtCbiy8KwO-5YT9FDUaP_kJhcB8MKB67jF8onmKUYxKNjokYIZlt2U8Aqq-jLoPHLksmOHs0MJ5El56HSZ1x7oGtrQB2rz0pLPKi5ejYkR8H4FnM7aQDeC2hU2o4vKUF0Cn9TqBDEQO0zKWBzC1o1iOsG4XSgzFzxt17VsqfQMjvkILBTnlfYkHXotBJCPyyVoontpuztj4-9W3G2zsLrcPpYvVBl0skmIyM4ZWSVKxKzPe_sLds2c0QZeRBGmuZrr0gUzYn1BHQ_iIh5Irm0u6ysu68SoXLErXJPBc0EbrYkZkP86uWgyn1_7fiG56jBn-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی غیرقابل وصف یک پیرمرد از دلار ۲۰۰هزار تومانی و نابودی زندگی جوانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143672" target="_blank">📅 12:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک منبع مطلع به العربیه: آمریکا پیشنهاد کرده که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143671" target="_blank">📅 12:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
علی الاصول دلار همینجور میره بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143670" target="_blank">📅 12:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naef3BTG6JtHrwu7ya_Kun-5Degg1IpjxSi0xdI6avnjs_9gd-WEBZRt8a0wK3nmxcpEDBpK2Ulp9dQtCO70UJ7h4EtdjsqOxD0DrkQ__0L-BjTVxSnjfpasOLaGYms--9Mcxj3ogW4QBVviIWX7Ul6pZnxgU22G2dMKChsoSH_f0NINT-5-T6gzLZNFcM5FH9Y2oO42_HTcThWxLtYWwvSUGGk7KALVpaLJEM9f7omTMYRayYCmsVYH41ANDCBlGPwTt1Um6Cd5i-THWb-wccUanjmIKKlx1U8XD7f6gwfGj1CH7kJwdWaKSLi7efdjbBUcFFBqgMunL05R_UI02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: سفر فیلد مارشال عاصم منیر فرمانده ارتش کشور دوست پاکستان به ایران بسیار ثمربخش و واجد دستاوردهای دیپلماتیک بسیار ارزشمندی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143669" target="_blank">📅 11:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143668">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کپلر: شمار عبور کشتی‌ها از تنگه هرمز طی هفته گذشته ۲.۵ درصد افزایش یافت و به ۱۲۱ مورد رسید
🔴
۴۶.۳ درصد از کشتی‌ها از مسیر تعیین‌ شده از سوی ایران استفاده کردند
🔴
تعداد کشتی‌های تحریم‌ شده که از تنگه عبور کردند، از ۹ مورد به ۱۶ مورد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/143668" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMRDTYdgv0RSepEBZ68Vi6KGXLB2OEbjeNWVie4-tgSLjgOHV6sRDGDg_ReQCcIULlBy5VcgCjIGX09hjrD3Uex1UIRjNurdsASknTy8ciQHnsn-VW0aK586D78JJBN_FA22VkGpWMDWpS7InslB6ScJj-D2ZW4EmxJ38-rVFbywWwQhP1arqgKZeeub7Trt9N-mCN30BMd7yxZLNJKDg1Q-5FipjEL8JZ_PK40GZzN6MxcgSZINcm8RrOv4MNjaqqV8GY5BsuBUjt3jRx1CJGRnp6NwtGi8n33CVtV2kl2AOd3vyOHeAgkm7h7Mzh32AcBxR1NuMi5XjZ_cYdY89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKI0J696wAHt_C5nk9oyKC0sihbx4yFdJ5hd4RI5AP-hVF8TlKbl8o5NRtNzH_bWruIJXpGWJR7Ur7xezyDwZJGHvGo136y82ft1sz_qNqocxJ_CyQnC7BDwqhin1eYiOByFqIHbP6x4OijX6YHgraNHcdawGQO6pDAqsnQVBs5JGWGMFkITimKJ1ZfN8My1JBZmClkn0CxxGDb6GDpikSyXoz_1N-_uuE09ZCe6Kvu8Bkej70Cc7FChzPal1GgWZC-8uKy2Kah1TIBFl0lomCL_mJKpuARY7DhnT8j55-yNpbH5BdsWdJVoSvVpxhSI-629vbFI0iLfyv0Uofxd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtUYh4vUDoaPQkFNdIQWHtAF_wZIo1pyOp0OGYo0qQdv5iihsNaxmDPbvEZlN9vnFk5yHh6LV7SzXo4b6MGU8lFVRBBMJIRoNLDCCLMMcOQWCEH4dkTNvWq-amrSF92RcXc4KTXRY8cr1FjwUnRLZ1kkWIJkVfgkIE4jptuj2aZnxWuEV8rSfscVHF2_hH6Ihvp7iYoSn9VT_apv2Nfv0Ji5WJR13lOqqHkjec6Knb_xKNWqj1Po6Ql9z6nY9h_tP9dmZJw9WpcbDnLznXxGYBf5q9Jcjja3BwMJzgheW7YasL_Vv7Xk5OS4WtOfcqjViyGORBvQBXN6VUWxCZix4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
امارات متحده عربی تلاش‌های خود را برای تشدید جنگ داخلی در سودان افزایش داده است، زیرا سطح حمایت نظامی امارات از شبه‌نظامیان نیروهای پشتیبانی سریع در سودان به طور چشمگیری افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143665" target="_blank">📅 11:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دلار 205000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143664" target="_blank">📅 11:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=VZjLUVTpaIXiBJ5YQPWUXEWx7u3wg9BKzmQrCbcxCCL6A5iQxIQJ5L-9d9qb-a-MJlXdsf0t6uz8XQ5V3Wupla_AT3BsyY3ydbhRN_HiRXjd3bVGzp1Cm1GOlqhrmGc8qveBU3500VUDbnoEfRK-Wv4XDY19A_odsSqVPdHBRK8w64dyPQXOvDPPJaKPyfqcMfdj02-hcat5Ed9__4VHEFS0QBiJBryNk_0zxOpPfs5mKFczsLGB90_VpkpyBt7EvUjrj9FQJBUI3CgWwJoyJDzc8qGlZcbHCbGLvnmXw4ZpnAuVCteyHQamM0TRF6hEb_VFlifbZ_9wy9_bYQ5G3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=VZjLUVTpaIXiBJ5YQPWUXEWx7u3wg9BKzmQrCbcxCCL6A5iQxIQJ5L-9d9qb-a-MJlXdsf0t6uz8XQ5V3Wupla_AT3BsyY3ydbhRN_HiRXjd3bVGzp1Cm1GOlqhrmGc8qveBU3500VUDbnoEfRK-Wv4XDY19A_odsSqVPdHBRK8w64dyPQXOvDPPJaKPyfqcMfdj02-hcat5Ed9__4VHEFS0QBiJBryNk_0zxOpPfs5mKFczsLGB90_VpkpyBt7EvUjrj9FQJBUI3CgWwJoyJDzc8qGlZcbHCbGLvnmXw4ZpnAuVCteyHQamM0TRF6hEb_VFlifbZ_9wy9_bYQ5G3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 205000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143663" target="_blank">📅 11:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مجری صداوسیما:
مردم میگن میدونیم گرونیا بخاطر آمریکاست، برای همین مسئولان نگران نباشن و تا آخر پشت نظام و کشوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143662" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فائق زیدان، رئیس شورای عالی قضایی عراق وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143661" target="_blank">📅 11:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرگزاری رویترز با استناد به داده‌های اولیه مربوط به تردد کشتی‌ها گزارش داد که روز دوشنبه تنها یک کشتی باری از تنگه هرمز عبور کرده است؛ کمترین میزان از ۷ مه تاکنون.
🔴
رویترز به نقل از داده‌های شرکت ردیابی کشتی‌ها، کپلر، گزارش داد که روز دوشنبه یک فروند نفتکش بسیار بزرگ گاز از سمت دریای عمان وارد تنگه شد؛ این در حالی است که روز یکشنبه ۶ کشتی از انواع مختلف از تنگه عبور کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143660" target="_blank">📅 11:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قیمت آتی نفت خام برنت ۲۷ سنت یا ۰.۳ درصد افزایش یافت و به ۹۲ دلار و ۴۴ سنت در هر بشکه رسید، در حالی که نفت خام وست تگزاس اینترمدیت آمریکا ۳۷ سنت یا ۰.۴ درصد افزایش یافت و به ۸۵ دلار و ۳۸ سنت در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143659" target="_blank">📅 11:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت امور خارجه چین: ما بار دیگر مخالفت خود را با تحریم‌های آمریکا علیه ایران اعلام می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143658" target="_blank">📅 11:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روانبخش ، نماینده قم: حضور اثرگذار چین و روسیه استراتژی تحریم آمریکا رو شکست میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/143657" target="_blank">📅 11:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: بیت‌کوین امروز با عبور از سطح ۸۰ هزار دلار، به بالاترین قیمت خود در بیش از سه ماه گذشته رسید
🔴
این افزایش در پی اقدامات وزیر خزانه‌داری آمریکا برای آرام کردن بازار اوراق قرضه رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143656" target="_blank">📅 11:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143655">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دلار هم اکنون 205,200 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143655" target="_blank">📅 10:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143654">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
آمریکا مبادلات ورزشی و دانشگاهی با ایران را تعلیق کرد
‏
🔴
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) با انتشار سندی اعلام کرد که واشنگتن فعالیت‌های ورزشی و تبادلات دانشگاهی با ایران را به‌طور نامحدود متوقف کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143654" target="_blank">📅 10:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143653">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خیابان «پندار» تهران به نام اکبر عبدی تغییر یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143653" target="_blank">📅 10:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143652">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: برای اول مهر آمادگی ۱۰۰ درصدی داریم و کلاس‌ها به صورت حضوری برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143652" target="_blank">📅 10:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143651">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پزشکیان: ممکنه فردا یا پس‌ فردا تصمیمی در ارتباط با بنزین گرفته شود
🔴
تصمیم مشخص و برنامه ای در دولت در این خصوص نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143651" target="_blank">📅 10:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143650">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhSHG71uyHE5xzXzF8dYLfpHZlJ2qkXBR1uXjDCzRjZr_D17wJZW60A_JXLc-Mn6gdRi6EKbHjiWOHROcnAFDfMpVrfqpa9GCJWTHVPuJygWdQNo7-zkbvSZHAZRzzeK4RW--R9n1IugUo3iQFnYq1d4T990bVejIMA3lo1-0MxQDnbGzoevIQpwl2cxCgmu2okiGr1KeRftRzkksCk3EJyGn5tB1eREb83dbc8ieuEQj5IoWM3jYEWYMVrW7i8QyuXW9s16YauQID79_qri-xhl9Op7PV-84UzFGBRuCnY5DDvchhzMy8J3bCMvMu0oLcUjV0Lw_f5VRwdnKT8jLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای ارتش اسرائیل، شهر زبکین در جنوب لبنان را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143650" target="_blank">📅 10:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143649">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNcW4Yo_VfHifazXX-O9kIyM6d38Cn7ulHrhSV3ay0Gd-2HvFTrnRelyewF-HbvRQsikD8BWBEuSq6RJKbE3qh-OeFhTE6gFgWMAA4RdmKHwM0Zj4BTDNJoq9uZjtSoqErB799iqED5-k6zGNo0fCLLBz7xJ1ohTAd3EzA3OmtLUCg1r1cBLsIGixFoYJ_EUirdeuGNfS9bLheowJ4zLL_fp_dB7J8_bd153c_HiGjzQoPadtJHFLbgZp6TKN3KPrpXju-YP99hsDa1wBRMAhQMxDfwRoGHwuF_8nMqjbght9zGD3upr3rFQNjoPawo2QWsM9_csFVDztO5GeR5QDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابناک از تعطیلی برخی پمپ بنزین‌ها در تهران خبر داد
🔴
از شرق تا جنوب تهران گزارشات از بسته بودن یا اختلال پمپ بنزین‌ها حکایت دارد.
🔴
یکی از مخاطبان می‌گوید روز گذشته با موتورسیکلت به دست‌کم ۹ جایگاه سوخت مراجعه کرده، اما همگی تعطیل بوده‌اند و نتوانسته بنزین بزند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143649" target="_blank">📅 10:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143648">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
خیابان «پندار» تهران به نام اکبر عبدی تغییر یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143648" target="_blank">📅 10:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143647">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKlXk8fsXT9jMkaWc6TaCMR4_cNNJYte22GrxcnEdixWBE6n3Vk3mm1YJt-F8cdpXimhu380NDdgOYfs6PMXw81d_8OtKedUrpfNME7h1t0IeZ8hWND_gmth_JCxPT-7sHG_YYLLNRUJR8LAOIOyqxS6wXRjCrikTfEfrcepioyGC05T1sAuWzd0lmLolu5wPs0GOwSDpEzu0a6K4PIv-E4Qh-wUexHTzqHYYoUFpUFVe7cn7fk8gkDfedvbHDO4dBjkLrUXVNhMUuWjP8n3T_O5-gorbbmkBD9VsEB3aN98Fx2oJyZdt6YvNlybxnho7c1vamMJxw7LHJ-k-IkBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتایون ریاحی، بازیگر پیشین سینما و تلویزیون با انتشار تصویری در صفحهٔ اینستاگرامش، از ارسال پروندهٔ خود به بازپرسی دادسرای فرهنگ و رسانه
خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143647" target="_blank">📅 10:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143646">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: ترامپ تاسیسات هسته‌ای و نظامی ایران را نابود کرد و حالا برای نابودی اقتصاد ایران آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143646" target="_blank">📅 09:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143645">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
معاریو: در ارتش اسرائیل، در بحبوحه ارزیابی‌ها مبنی بر اینکه تهران ممکن است منطقه را وارد درگیری‌های شدید کند، مقدمات برای احتمال تشدید نظامی علیه ایران در کوتاه‌مدت در حال انجام است.
🔴
در نهادهای دفاعی اسرائیل، تأثیر تحریم‌های اقتصادی و توانایی ایران برای دور زدن این تحریم‌ها را زیر نظر دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143645" target="_blank">📅 09:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143644">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رویترز: بر اساس نظرسنجی‌ها، تنها ۳۱ درصد از آمریکایی‌ها از اقدام نظامی علیه ایران حمایت می‌کنند
🔴
این مسئله به پایین ماندن محبوبیت ترامپ در ناز‌ل‌ترین سطح ثبت شده، کمک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143644" target="_blank">📅 09:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143643">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8379764469.mp4?token=gJXAtKsbVi5GIXzFXAG0A1b0UCno2ob8nDP6hsSdixfOtZ54GLAC4a5n_2sssHirvjRDC2P2QBmrtP9xnc-4pY3JEKK1cVfbSlBM3j5NIr7kejHMiIbVjxH3fyNdtdzQiUjwJeqLJNUnXJYbOg9Q-dHtDVklF8uilX5X-Z9CwpqELowPwnlWqrBfqnNxiFw34gSSnqNxeO2Ss9325toRiFxHgJagbvC1jgikG9OQFqdZfyT4LWy0s2brqbGVgpuRayA287EF3n3vRQhRwGdTWdhGsZv11AIjdM59pKOJEN40_AhT4las1KFfc5D0fNYJVZI88TAqX7rsH4W52-aQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8379764469.mp4?token=gJXAtKsbVi5GIXzFXAG0A1b0UCno2ob8nDP6hsSdixfOtZ54GLAC4a5n_2sssHirvjRDC2P2QBmrtP9xnc-4pY3JEKK1cVfbSlBM3j5NIr7kejHMiIbVjxH3fyNdtdzQiUjwJeqLJNUnXJYbOg9Q-dHtDVklF8uilX5X-Z9CwpqELowPwnlWqrBfqnNxiFw34gSSnqNxeO2Ss9325toRiFxHgJagbvC1jgikG9OQFqdZfyT4LWy0s2brqbGVgpuRayA287EF3n3vRQhRwGdTWdhGsZv11AIjdM59pKOJEN40_AhT4las1KFfc5D0fNYJVZI88TAqX7rsH4W52-aQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار در شهر زوتار الشرقیه، در جنوب لبنان، به دلیل عملیات تخریب انجام شده توسط اسرائیل، رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143643" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143642">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وال استریت ژورنال، به نقل از مقامات:
ونس قبل از جنگ به ترامپ توضیح داد که باید با ایران محتاطانه برخورد کند و اینکه ممکن است این کشور برنامه هسته‌ای خود را از طریق مذاکره، نه جنگ، کنار بگذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143642" target="_blank">📅 09:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143641">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر کشور پاکستان: در حال رایزنی با ایران برای فعال‌سازی مجدد تفاهم اسلام‌آباد هستیم
🔴
در گفتگو با مقامات ایران پیشرفت قابل توجهی حاصل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143641" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143640">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آسوشیتدپرس گزارش داده دولت ترامپ در حال بررسی طرحی است که بر اساس آن، ویزای تجاری و گردشگری B1 و B2 تا ۲۰۰ هزار تبعه خارجی که برای پناهندگی در آمریکا درخواست داده‌اند یا پرونده فعال دارند، لغو شود.
🔴
این طرح ویزاهای صادرشده بین سال‌های ۲۰۱۶ تا ۲۰۲۶ را دربر می‌گیرد و قرار است با هماهنگی وزارت امنیت داخلی اجرا شود.
🔴
لغو ویزا به‌معنای اخراج فوری نیست، اما وضعیت اقامتی این افراد را پیچیده‌تر می‌کند. طرح هنوز نهایی نشده و احتمال مواجهه با چالش‌های حقوقی وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143640" target="_blank">📅 09:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143639">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDgfW_85686EJUc1FKMRB_cAmva4FaLh8ttSBdvJrG5QWipIbxy4D_RC3cfjUge5XQzNZ3IqRWP0GPVVSNpv6JrD3azRJPbWrtceMD4ve4vnB-glQeEg4GuorhAAgKMDQVEuyopoI0a8lrH0xv8BYDkdi7X3PLbse-No9MGtcoY1t1o-9c-6suFkxym0jgD-FE_GX3EuZIxjrsqxQmXCA_w-OwpLpndYYkBY7-g1h25p2I6G3Qy2ltoCV2g04TxwXjRXMP3UygoaccOT7hnvR04VSR_Fn8wT9ViGRgw4HSGUrMQpKCNC36ZK-JdB8udnE84MbC2TFbg3ap5zHB9Nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش یک جنگنده آمریکایی از نوع F-35، کد اضطراری 7700 را فعال کرده و در حال مانور برای فرود اضطراری در پایگاه هوایی موفق‌السلطی در اردن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143639" target="_blank">📅 09:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXf7ia1zEScz6y9PONK1chtHiP8IjUqLoV_M_PQ0xkdHEoPGDgvCY4TC_1jeSl16SR_DOe36-U_RtXLiZTdK7_U3iE7cvOU4YoTTM1HiSX-cuJpDyht4wEEiO8hLozQVVrWlFQ2ZSJth97f1kcG7OFN3tKaS0ZktRTqw4C75QMOKMk0Pg0eCdSB-7AdTmvTwaEocgULMXYytvWkdZAXaXX1zCoYkJewq7S1Q291a8OF79A6r8djgOWNKT7z5k28wwgInyVSIT0XuIjaMbdMmQMRDiGe41UDWWJYjTKPRLNRrB5TDxJzXX7Q8xlC7L3n6Nxo07956E73tfhCX-_z9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیلی و حرکت نیروهای نظامی در شهر مرکابا در جنوب لبنان مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143638" target="_blank">📅 09:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هواپیماهای بدون سرنشین اوکراینی  پالایشگاه نفت شهر «آفیپسکی» در فاصله حدود ۳۰۰ کیلومتری خاک روسیه را هدف قرار دادند.
‏
🔴
این پالایشگاه در حملات قبلی اوکراین نیز هدف قرار گرفته بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143637" target="_blank">📅 09:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRXK0kqsWqT8noJTtUrLK-KKKM_6no91AA18YJoPq8bRakRdVwTAprTU3j7nRiuQZYycp37MDG0LmoOm5Y456pwaaI1I1GV_THPdAqDBq3orsKS2f8uupzhb5-OjCJLqYaWjRfuM8H_OgjL9vOO-f5XziADw5qWEGFO3YkJBwdzj9IVTtCU1mZJnN4sciwnvzy1cGdt1-LMeg8xvH4_YtH2xA01afs8O20msD9b6XqrgfTl_U9pQ8mCRNeJdNaqI9AMQeGuZqS6ox1kKB0zsV_FZMVQgbQqHEK28PiTSGWqJZsutv_JQhmtSYes06xA7gIGcnYrt33_sfmiKOQzO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
هدف قرار گرفتن یک نفتکش در تنگه هرمز
🔴
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقه «الشیشه» در شمال عمان، مورد اصابت یک پرتابه قرار گرفته و موتورخانه آن از کار افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/143636" target="_blank">📅 08:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ4wXQ1LVotD8aokWX1j59BpUFKTVRrH4bTuQdK8g27DoSM14F-2_07py-af-ObSr9zu6DgBUObEUUp90NWEusN0TacxExPSxVDgirhZRV2Qxawp9wpGuebaVE3pTKQ-d1DX_6DvrsMwebv_FPMRZW5XueklTympWA5xQgpJHvcInyFPTwbQI1WUjG8fBXIFg6Oce8oN0z1XH5uj93AaU3rbPHdIgP8IDg43eeqTQQKm4btGWmDA9UEmHBk0mku5l89ueRKOWui9Gpf2JdviA_I2Xg_0sG-TAgeUtmn7DZ3s4GkZGufY4fRpJl_bMt8DyTF6oGq-fgeXePFRowVd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
خبرنگار الجزیره: میانجی پاکستانی، تهران را با پیامی از حسن نیت با هدف حل اختلاف ایران و آمریکا، حداقل روی کاغذ، ترک کرد.
‏
🔴
پیام‌هایی که او با خود داشت، تحت الشعاع اوضاع سیاسی ایران، به ویژه با رهبری جدید شورای امنیت ملی، قرار گرفته است.
‏
🔴
این سفر با اعمال تحریم‌های آمریکا همزمان شد و اوضاع را پیچیده‌تر کرد. اوضاع همچنان در نقطه صفر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/143635" target="_blank">📅 08:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بیانیه مشترک عربستان و فرانسه:
پاریس و ریاض از ایران خواستند همکاری کامل خود با آژانس بین‌المللی انرژی اتمی را از سر گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143634" target="_blank">📅 08:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143633">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ارتش پاکستان: عاصم منیر با مقام‌های عالی‌رتبه ایرانی درباره جلوگیری از تشدید تنش‌ها، رایزنی‌های بسیار سازنده‌ای داشته
🔴
سفر یک‌ روزه وی به تهران، در چارچوب تلاش‌های دیپلماتیک جهت پایان دادن به بن‌بست در مذاکرات تهران و واشنگتن صورت گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/143633" target="_blank">📅 08:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb3b80fa7.mp4?token=qTNDVTPa__Ht4wFSA1pcxZbqwiK7WQXmy3td_uZAzGntWeUuM1W3u68PBgwHk6ejGYoMCZdqWNISxRgEeXe7vI7YgDGmipdJx0YDaW1d_TZX82Z3qHEjhrMcBdGVtQ7cAt2In9g7PQYTSQJ6hmjW5L5BkAjGMdae7nWgXbUidC8viGvLHWWsE09NTmgDgxDZFJmbOlm6ZWkBNzMhWTlnq_B6wK67s4kvJ4ZhVZCv70FHTXC3tvthVV2lOTLVsALNBAH6ELztsS5R79prOJuonqwEVOgIVhn7Q6QPIYW6GFN23KbpupAvuwM2OPrm9jJNd_0PLRn0G9-F_tc9sK24aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb3b80fa7.mp4?token=qTNDVTPa__Ht4wFSA1pcxZbqwiK7WQXmy3td_uZAzGntWeUuM1W3u68PBgwHk6ejGYoMCZdqWNISxRgEeXe7vI7YgDGmipdJx0YDaW1d_TZX82Z3qHEjhrMcBdGVtQ7cAt2In9g7PQYTSQJ6hmjW5L5BkAjGMdae7nWgXbUidC8viGvLHWWsE09NTmgDgxDZFJmbOlm6ZWkBNzMhWTlnq_B6wK67s4kvJ4ZhVZCv70FHTXC3tvthVV2lOTLVsALNBAH6ELztsS5R79prOJuonqwEVOgIVhn7Q6QPIYW6GFN23KbpupAvuwM2OPrm9jJNd_0PLRn0G9-F_tc9sK24aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تعدادی عراقی با شورتک و سر صدای بلند و قهقهه و چشم چرانی داخل رستورانی در گیلان باعث ناراحتی خانواده های ایرانی داخل رستوران شدند که مسئول رستوران رفت تذکر بده با صدای بلندتر داد زدند میریم از رستوران شکایت می‌کنیم ما مهمان جبهه مقاومت هستیم
در نتیجه بیرون از رستوران تعدادی گیلانی شیرررررررر مرد ریختن سر عراقی‌ها و تا برینن کتکشون زدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/143632" target="_blank">📅 07:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143629">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZcpuLYHR9v78muWrwYHhIMOj6gOOsd4lj4lVbY87nmollv8g3AzJRJdN61t3Treu-ZbjjyjrcdskSfomEVCaf04F509eJb8h7j3sJMXWAva-2Aw4nNr1XJZjvjAyh7NvOUYGMHI4M8Wle5bjZRhc6FXD3teI_Qw6f_wNwc7SVqCu35gH3HLZnTKZTxkfZzX-UDy15kYkuntLqQC7PvJwE5l0tolSBGuEnXrqqHdIhWfbtdz-q3pSat-EsyLMFQ6r3u0fjaxwrTFniR129Dxm1fIz8ipOMJz0osvET-earLD9_Rc-21auW3ZS5mzFhjdNJZIqRPfl9PMsDqa4B-efpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLtKP-p-WytNyM5BHskD3h6NyjJW0jtK-JKtvPJb0LBKOqcRj6J18LwAI_AY3wTqRbZjldyoco8-REuzCJ9kypBHdTUsva-MHnNZXpDqD6fb0SJdzlMB_YqlbEH25pFuKzcX3QraRsEkEhYQIJTfs1mgMUPbc0Pd9itimMdXSwkdbIJRT7IH8Q2O6SuKGnNBzTR9g5k5UICg2wcBLqtQks7Yyo9mQjG1EmfxwsQ1SNsoDMOe24PZbOoZxGIQ-XPy3JPHk9DVf5s96x1EVUoJjQANA0ED8a9tvP4ggaC6w0MYBdjm_KldzpsCJ_WjJ7DucrN3gCQZ-zOAzmfwBK38LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5jEYjV_fIAYUN-DIq3oOiyLJUMYVUlffTz1VEVb5fdl9_V-K5SAETqxwMTeyo6SunRIj_u2HZI5N7_pdzZbwE6KPVsoNnAcWw64WChsz7vRUdtjzO8ohLJm0lp0lD1WHnvvcsfhEeDoAmjJiO9dyfkqlyey8oJW-_d5SWnvQfreNwukuaxyU_ochlQ-y-aTgZicqga23lIwWVB1u_sdvNbOzQba48TP5VBWoPLiLDP2qoz8EW-OXiGS0KJMemm75a34g_0GHjodjLuCAop04SPFxJ5ZKiritOJJiZx7Hb-IeE-cNoXo6PHpTWgDWhniYCYnm2ObYoXtN7RWfAVEsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ عکسای خودش با کیم جونگ اون رو پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/143629" target="_blank">📅 07:04 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
