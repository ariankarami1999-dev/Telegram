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
<img src="https://cdn4.telesco.pe/file/urFNX22FrJggyHxBjMD_j3Q5_l4L9NJN-jTYlsscJc-qppcgHVp1kf3V9evIbNGSonmr3J-lHWW7WWWJPuv4vu6zJqLDu7n1lIKqf-vbsYcUeeCrW0ij3gZOsWV_g2fyFuWfQrOtSHC7haPFQxeAc7-XfP2425_R3UDDia49UkIU45rnOZVgE3YO4mH8hsk8lhssIfPHktJY0CPN_AMNdoK9PeyJK1sAZyKaNtQMIDSugDIP8Fra94gsXNZZt3UYqo1_EW_8IQWbq5jKyaG0g0sn4CKZeRO6gWOeWtNZDUdc4QCVPIj_v0afBfT8_jM35yDv8dFJTZH3eUzfnS_ETA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 906K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 14:58:45</div>
<hr>

<div class="tg-post" id="msg-123921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul_qzBvg8eKVPtr7cQvGozrJHoCeBi7F3t9dCrDtWlaAN1Vzr86_ZN7-EbU9HP3gL6_CmgBN9mpUX2w4dSUtdhqEdtCYzA5QYKTWCAUQA4KIDHkmlNRytCaiE29f4n1aphqsW4IOBPm07EyqfrrYkRCTGseFgPzktx4nwII30JHjoZBYduMGjQfUfMrjL0c2Jo4rcDGPBe7nrEWJx35PBpdtRNvsefnJrGNzH5uWhAYqezu1NuLWW3QzxxQcLSqa1d847UkFEj6EBxovznXsxCbJOUfYJboPFtupyCLzGn0eJt1dOXB_ywiE7s4BPPTtQMsCg3_8U7UPw83QmC_rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/alonews/123921" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
منابع عبری: عملیات در جنوب لبنان بیش از یک سال پیش برنامه‌ریزی شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/123920" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تسنیم: تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
🔴
تا این لحظه هیچ تفاهمی نهایی نشده و احتمال منتفی شدن هرگونه تفاهم نیز قاعدتاً وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/123919" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: باز کردن تنگه هرمز یک اولویت اصلی است زیرا ما قصد نداریم همچنان بهای جنگی را بپردازیم که جنگ ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123918" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jozFS1NSKJ92iO7LEVuBrGHHPMXWWLuxHSi_A3cQOC9qQyUhefOfark6Nkp993xnetLaQL7Yr3-nJA3loLyuGYAQaMIcLAZfqYTaqfe-oV4dvsopA1XwodY0Apl1FjKhdA-2OH69z6Vcx79XYJhQf2SPKsnHSpYG4KdopJJP4hau2bbmIoIkYVGHIpCKItEQAarS7kKg8E1X3CQ1Up0-ZZT7pVGfXNePFj5J7nGPEEI-m0tyjQwgbgG8JY6ppgFy3cLv1_Kw_Ydtbq9EWxSVe8b2O78RC-M8af54U465R50k-3UtCL2Ix9apcxEBEK_1M6erfe275WEBqb94LHRNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرباز ارتش دفاعی اسرائیل، گروهبان مایکل تایویکین، ۲۱ ساله، از واحد شناسایی تیپ گیواتی، در حمله پهپاد انفجاری حزب‌الله در جنوب لبنان کشته شد و چهار نفر دیگر به طور سطحی زخمی شدند.
🔴
تایویکین، فرزند تنها، در سال ۲۰۲۰ همراه با مادرش از اوکراین به اسرائیل مهاجرت کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123917" target="_blank">📅 14:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m13QyZOMgzD732b7PlS1uH192KPUaD_NOP98fCTxXBUN5Zfm283oUQHbIZhe_dSYaFi_wy71IrEqkyAPDwgEV6yX-Vklpzdyo3imdzTjNwwUFzMNye5PLkkDjjkRaMMsHVW62R5WYygGN_atAwwpDXuTropQ24KkiT1f2Cq-QTshJuaYNkt74wpaZSmh4t1o0Q90sDoIcIc2-B3gxTPrkCEWJkz0wxuuLSvkwzs55hTikakOQJ0GFO6kzLzDCAhnpgALy-31uxVdn6Sc5g9TcqK1RoPZr7kTH75-CL8vnmFAAgWV7VXUPzLcRNj0NxVTPlqnTfNsovi37eLG3r_cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرتی: حمله اوکراین به تأسیسات جانبی نیروگاه زاپوروژیه و افزایش ریسک ایمنی
🔴
شبکه آرتی (RT) از حمله جدید اوکراین به محوطه نیروگاه اتمی زاپوروژیه خبر داد که در آن، گاراژ و خودروهای خدماتی این مجموعه هدف قرار گرفتند.
🔴
این حمله تلفات جانی نداشت اما به انهدام ۸ خودرو (۶ اتوبوس و ۲ ون) منجر شد و به گفته این رسانه، خطرات برای عملکرد ایمن و باثبات بزرگترین نیروگاه هسته‌ای اروپا را افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123916" target="_blank">📅 14:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123915" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123914">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123914" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123913">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است. ساکنان مناطق مرکزی و جنوبی جزیره، وقوع این صوت ناگهانی را تأیید کرده‌اند.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123913" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123912">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نتانیاهو: به ارتش اسرائیل دستور داده‌ام دامنه عملیات نظامی در لبنان را گسترش دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/123912" target="_blank">📅 14:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123911">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس مدعی شد: یک مقام ارشد در دولت ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123911" target="_blank">📅 14:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123910">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: حزب‌الله حدود ۱۰ موشک به سمت کریات شمونه، مطله و چندین شهرک در جلیل علیا پرتاب کرد.
🔴
آژیرهای هشدار در طول یک ساعت گذشته به طور مداوم در جلیل علیا به صدا درآمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123910" target="_blank">📅 14:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حزب‌الله: مناطق زیربنایی ارتش اسرائیل را در منطقه کریوت در شمال شهر حیفا را با موشک بمباران کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123909" target="_blank">📅 14:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
قالیباف: سربازان دیپلماسی هیچ اعتمادی به وعده‌های دشمن ندارند؛ ملاک برای ما دستاورد‌های عینی است
🔴
تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی را تأیید نخواهیم کرد؛ تضمین این راهبرد جان ما است که کف دست گرفته‌ایم
🔴
خود و همکارانم را به پرهیز از اختلافات پوچ سیاسی توصیه می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123908" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123907">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل: به صدا درآمدن آژیرهای هشدار در کریات شمونه و حومه آن در جلیل علیا به دنبال پرتاب موشک از لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123907" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123906">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP-SY2NNK9c4ojjeUS3FUejB2JUqiG-1RFfgwcuC5N6dWMfqlB12xcq9zZiRisil0gtKqT-nhfnNeQgHLy6XvcmuLV65gBg0H8ni5wAR7W-vAai5p2xtHF-lKDTjH2E4MuN97ZrwkPbCwVf6wlMDTzo_hL2oZgM5Lxeul_ueGXU9ZOibBbcGUY58PvAjmuGAdPMlKxdC2tHwq1KdRR9jA5gYMKMYDUDYxrWuIUTaeEt5JE9Gxhl8i1CbP255CztDmG6GI6IbAxnKRGacBLVrq9xPYp0YRouDOzsS4kPWwlgqYJ33d0NmRaSAjY8dSzFX6bRUmEPSWibZb95nAaWuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و سکه امروز‌ ۱۰ خردادماه ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123906" target="_blank">📅 14:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123905">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-AfNkUX7NuAmG3w4O746DiPhkcOHTm3BkDGgHAbarGgJFCQbvBaLW5sDno1rO4G5ZRgs6RVBUClkuCM9RBZYefgSUMulluARqLvg8Ll2mxmtmsuIPX7Uw1-TM7-Q3EytAfYm_qFK5IOxYI9aSKyPdKBn09BjsKqD0pPQMNnSgc6LY6aI9CcMPNerubO4gIj6PETPIob0-apZW5djKPV0GgkZL1ijYlU3suKof40bU-_eYS91NXcMYjuIDgeEWmGfWkPrFJVYFkYHpp4PSa6hlSQO798riItG5NTzFE2KbNLsHiq604oRprEokChgXIWk1vKhSKUH-CiebeUqMR4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آشوب و درگیری شبانه در پاریس پس از قهرمانی پاری ‌سن‌ژرمن؛ پلیس ۴۰۰ نفر را بازداشت کرد
🔴
پلیس فرانسه بیش از ۴۰۰ نفر را که در درگیری‌های خشونت‌آمیز پاریس و دیگر شهرهای فرانسه دست داشتند، بازداشت کرد؛ ناآرامی‌هایی که شامگاه شنبه پس از قهرمانی تیم پاری سن‌ژرمن در لیگ قهرمانان اروپا آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123905" target="_blank">📅 14:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123904">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c0898080.mp4?token=NcqQgVlM6u1lUDK0eC93UNPfmJo4B_CRXbjZVXwIXxOBFOQfr6s9EXIC6lppMA4A36maZNAt8kpdISs5M1Wx4ab2oshk2g6PcL6GhEY9EBsnSWl-KBGjqFFePF3GkrxEPe8whTPw4pM18t7WU_MewyYxaF3PO8BYJGBfDgPZZk_KoADsfD1RiLgpAFq3X7-C1RCR7rdStFdXNuxuRZZeAGr0MjlWtPRkhaUEW82mvKKbeYGi4mwxgrSsSDUkOhJBaWj7rifsEA7ikzR7pTO6i-bQOsPQ9oTrrKm0amwZbWWuqMPPnpkmPrzm_4yBfoidkSC6N9y6Z41HP7SfF_bJzJHpQfFmuB4XxbIgQfKVfg1HAGm8hxxfTDnjC44WONeZqL7MyfBPt2orUP8wAKL_2qqZDGHuYQ6ipfMaTzja8XfskThnM-qdpsBfsvpltrd8jMqADUOVEpcgObw4PmR-a0lQTV-aI7IvEPfZGJOek2lJzgX9rhk9aQCKN-PS1jrkWknV4Zh2hZa0wl5OHYZBe7I06VKwstDODz4qCTOQ7Ncin09gKZm0RgF3Zq4np9mWUNMJBhap-QNhuLb6irrvYAWx3W3h231hQ-OaCXH3sCZa5cSEOJhVPHLzyEUGSQmE-s1HuUAcpTuojHgVttMSdKXNAV0jLplRfQszMJnRVWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بحث چالشی مجری صداوسیما و سخنگوی دولت درباره تشکیل ستاد فضای مجازی و موضوع اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/123904" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAiPeIteED0f0_tWeOXYViSz2v60t5TG5kUNOBXLFWYdd42janceK2H4behEr8kNpzZKCr0y1FAe74E88QLemiE9lOjJnT6Cs5DWpCz20kD3OtdxpzRVKnIAnEApxV6JtZpGK66KbMwJGcVlcUbK6_US-U8tgakn-SWz7tyOdBftaVLQk8uRtTbytg4sXzq_5H0mmf-5GITtPugpMZwTC2S5vDc8l4dS5AO8eMUctDAK-uxFeDjgRaAMEnaz4KB1X6gNVlKiG4nUh8G1HsbGQJboR-AMPVcfcZaKyRTwaf8So_YtgL2S1h4qUckABfdAqTxeHHwyzKNj2F4iRyfI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cm-Vd3STKpKY-hU78IBbF96_BbHhaFmL9BgDDtMtVMtLDcGueP-cMJuoZ-AKkFKTEHmS4zLq54VGqEoECahFFa6qsSgVzryzxgv6Kqvmmu7_nJPyynK6l4-5mscOMLtMOhSbjbQPBdjQCyXpBnnFcPGwaerPi02cw-enGNfICtT2LAEgdAwWt3MvLYsfMqiU5Y9gQf9L_IMM1otKN-2FJiDNVXfAaazNLKyEIpBEe-INoDMbid0pL_5d9tno8BnjL5MQ9mUwncefkykTKH4cwu2h38WgoGEYm68s6mVuGOfQbYAc5wSfauxb2oDLyb8sa3xXz3MzK-_n9ncQauFKIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
تأیید هویت یک دانشجوی کشته‌شده دی‌ماه؛ جاویدنام شهاب خورشید، دانشجوی معماری
🔴
«شهاب خورشید» ۲۲ ساله و دانشجوی رشته معماری، شامگاه ۱۹ دی‌ماه حوالی ساعت ۲۲ در جریان اعتراضات میدان کاج سعادت‌آباد تهران هدف شلیک گلوله نیروهای امنیتی قرار گرفت و در همان محل جان باخت.
🔴
طبق گزارش ها گلوله از ناحیه پشت کتف به او اصابت کرده و همچنین دو گلوله جنگی قلب و ریه‌های او را هدف قرار داده است. بنا بر اطلاعات دریافتی، پیکر شهاب روز بعد در کهریزک به خانواده تحویل داده شد.
🔴
بر اساس روایت‌های منتشرشده، شهاب پیش از پیوستن به تجمعات گفته بود: «یا همه‌چیز عوض می‌شه یا من می‌میرم». او ساکن فاز یک شهرک غرب تهران و اصالتاً اهل اهواز معرفی شده و بنا بر گفته نزدیکان، از بدو تولد با دیابت درگیر بوده و انسولین مصرف می‌کرده است.
🔴
همچنین گزارش‌ها حاکی است پس از کشته‌شدن او، فشارها و محدودیت‌هایی بر خانواده اعمال شده و خانواده اجازه نیافته‌اند برای او مزار جداگانه‌ای در نظر بگیرند. بنا بر همین گزارش‌ها، پیکر شهاب در بهشت زهرا، قطعه ۲۱۱، ردیف ۲۳، شماره ۱۱ به خاک سپرده شده و گفته می‌شود در قبر خانوادگی سه‌طبقه دفن شده است.
🤔
عرزشی های حرام زاده این تروریست بود که بهش شلیک کردین؟ داعش ما ایرانی ها شمایین
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123902" target="_blank">📅 14:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نشریه آر‌تی: لوکاشنکو تهدیدات زلنسکی را «حرف‌های بیهوده» خواند؛ توصیف ارتش اوکراین به «گوشت دم توپ»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123901" target="_blank">📅 13:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/redJyeRHNMVK2fTirfTLWmfkG7W2_4CF5kqwV8zNbOf2RtsHv-f_V79dGwRkfNBB6OPu3ZRhjLFAM0fV6rS7ocDP1dDLYgZNIlJH6jVhkcca9GJKKS0Dychx1KmFDHBnXtEmp4TZ5uk3XWIsnde8JhNJXk-vPQxPd-LiYfGeCMnfnadMPPQSxbv_jpjLkVTtHXoVnblBsUUGoY9nUEoAVYfvREoZAyS7GVDPLcHLcWemV_5vPj9QwSqlZ_EmJnRTo-YaIj2PVv4rieG1RfBw0J1o9TWK48fKmxa7xnOy00vi4MzV8iOj0H-x04gmam402gKw8k2JOZiycKHEtlEQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بررسی ۱۸۳۵ اکانت بازنشرکننده توییت‌های قالیباف نشان می‌دهد بزرگ‌ترین گروه این اکانت‌ها در ایالات متحده امریکا قرار دارند؛ پدیده‌ای بسیار قابل‌تأمل، به‌ویژه در شرایطی که برخی جریان‌های سیاسی در غرب تلاش می‌کنند از او چهره‌ای «میانه‌رو» و قابل‌قبول برای مذاکره ارائه دهند.
🔴
نکته مهم دیگر این است که پست‌های قالیباف که تا پیش از ژانویه معمولاً کمتر از ۵۰۰ لایک دریافت می‌کردند، همزمان با قطع اینترنت ایران در ماه‌های مارس تا می، ناگهان با ده‌ها هزار لایک و بازنشر حمایت شدند؛ آماری که با میزان دسترسی و ارتباط کاربران داخل ایران همخوانی ندارد و مجدد احتمال وجود شبکه‌ای سازمان‌یافته برای تقویت مصنوعی این محتوا را مطرح می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123900" target="_blank">📅 13:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123899" target="_blank">📅 13:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ویدیویی از برافرایشته شدن پرچم ارتش اسرائیل در قلعه تاریخی و استراتژیک بوفور، لبنان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/123898" target="_blank">📅 13:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db1c2c33c.mp4?token=Qp1y7ekZueiWIyJesOywgvLxnFUF0dGpDDO-OBSxFZWn18S7vOzupqCBLd1uDEW_gwzn1epfmq8z9seOOeM2bzwKwCAVsUIw91UKJ76A1_VfB0S947kjCxq5KcmNQJVOSlVB6UZvkFhZA6LzqWUl-rdTBmtNZ392hrhvWO6yUaKn3unR0WyCYNnaRNpK-oyJjl1jmAbslpo61Fj7-evNXk-wAPjVDMM_1aRgUY4LU6Jeue5rf1s1UWR7fr2dJZTgiJD1oxG_fC7gHvWQm0zZGhgIBUTEc312MxRn6jNtQMM06vTggehztFPUdoRRjHKLs440bDL-YsYfQ4I-MoTiUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف : دشمن بعد از شکست نظامی، با فشار اقتصادی و جنگ رسانه‌ای دنبال ایجاد تفرقه و وادار کردن ایران به تسلیم شدنه
🔴
اما مردم با اتحاد و ایستادگی نقشه‌هاش رو خنثی کردن
🔴
رمز پیروزی حفظ همین وحدت و انسجامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123897" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF-5GSfwyspdOnvYM9Edpqvjd4sstNv-jEqV5SfXvLUSuOPZcBCBuc1-5S_4JgTa-7W8hI_8g--GU6aAKbhBSnCXYWnhcNO6tsELTM9Qa1RhsuPQFSohSGtk3bcRygltdqhGVgnS-frcY0OUZ_1z6qf8gnbkolWRb-Ij0Nf-aLrX6Swb0qMakEdp6usB4aVph6yyWPrk12cuQNuPpjGn5vn1n6jcKwz7lpwdunra2w_SM2bxv-GPCKejeT9XiEPdoWUxXGqhxACJL-sTi5XREMvUCvLAy6Iu0I-mRjFbyEIJzrbVYv72JurXPpRmvwq4AlbNnTMTtQ_eoDVafC6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۸۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۲۳۶ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123896" target="_blank">📅 13:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7328c91388.mp4?token=cE7o_LKWKVyP1SSEpbsN4d_Cmsfx6p8xabZrx6DG9l8VZO0vhYO3y7iV9bBMgm4xltjxDBaGtZTFQ4kjdeXSSadf19MrKOtjuKRdDfSEXCa47PU3yuwsmUpjoke0NNO04d67gpSouMHsHuJE7CiJOJh3r9eKx6c_IG0rIpQVL1kmoyNT6o0I7WChRrPXbXJd3-aV7npD2zrCv7m1OJAWWUJnLj_GIV6rvxptmz2GpEi2I5uV6ZlYkRnPMw6vft1S9zV2LTXvSxTDvMQjHoIee41H-Fdm152sMrA5UW9pSimM8265kzvhaIt3BRtAMtP9vfKUggJbK-1gkjFjbSdzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوِ وایرال شده از ذوق کردن یه پسر بچه، بعد از وصل شدنِ اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123895" target="_blank">📅 13:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قالیباف: چک سفید امضا به کسی نمی‌دهیم
🔴
رئیس‌مجلس: ما فراموش نمی کنیم که در شرایط کنونی کشور، دولت در میانه‌ میدان مدیریت مسائل و مشکلات ایستاده و نیاز به کمک همه از جمله مجلس دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123894" target="_blank">📅 13:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/123893" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123892">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQlQMrMP2aQuAIO69A7EnsBDQVG8BGNqzVGdZgCyUCffB6XMKmmgbD7Z-oP0PhE7-I0b0ruDnw5LKwA_nfoJJ4VLjilEWxE6z-LzDR37azpkdWEpc0EyncNchyWJ1GaIGKUq7hdmeQwwCc-AnPSPnYd0HY-JarQ2VfyRfDv7Do0bZyRfA2S04MVcDUaQ7nh5GaWgYA-heEjecnAcinDdX1WQOQOnDxr8QOTS9WA7H6gBMsOjgvNpJKFRCeUVbF942r29P4hAPMqaxKsQsQjDNdrIDjlv-rvz5TnI9MDiaOTVqGbi1IbfzZ8lurjip4fk8cN_iAJVMhm3yLNy0VyHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/123892" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnqDdOa5DBKP42BL5TIu2mEczowbPMsCL3XLn1Aup53OUJSovEmWOUPqDCBJZ4q--Lgi1yt257w5K35EdklfCBEduhuMXlfzWlB76V6ac9exzRYIUGVKnY-kRDOIOqd2MDwWfj-q4s8F33sc97ZDfUJ7wPA73vlBL4cA0vTi2ONv0z5ub26aXNF3OuElzIVl7jZy-X8gY-kkM6DGyev_911CEzROawBV5SfTOZAAsqVHCK4w3MGzEPSxykdbCP23SAUZP7tnknb8rZqSq-Be6_KgQH7eQAsYvKTRtqPVK5tMvEqQEuJOy-otygF4dKw_BS9FCP36th8sCaAi8ILoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امسال ۷۷درصد بیشتر از پارسال بارندگی داشتیم و سدهای کشور ۲۹درصد بیشتر از پارسال آب دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123891" target="_blank">📅 13:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الجزیره: [جنگ آمریکا و اسراییل علیه ایران]، فضایی را ایجاد کرده است که در آن هر دو طرف احساس پیروزی می‌کنند و بنابراین تمایل دارند در مذاکرات احتمالی برای امتیازات بیشتر تلاش کنند و این امر تلاش‌ها برای کاهش تنش را پیچیده می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123890" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره: از آغاز جنگ، فقدان شفافیت داخلی در آمریکا در مورد اهداف مورد نظر، منجر به عدم قطعیت جهانی شده و به متحدان و دشمنان کمک کرده است تا جایگاه و رهبری آمریکا در نظام بین‌الملل را زیر سوال ببرند.
🔴
تمایل ایالات متحده برای آغاز درگیری با ایران، ارزش درک شده سلاح‌های هسته‌ای را به عنوان یک عامل بازدارنده در برابر متجاوزان تقویت کرد.
🔴
این جنگ انگیزه معکوسی ایجاد کرده است که کشورها را به سمت دستیابی به برنامه‌های خود و توسعه سلاح‌های هسته‌ای خود به عنوان عامل بازدارنده نهایی سوق می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123889" target="_blank">📅 12:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: کوتاهی ایالات متحده در مشورت با متحدان و شرکای سنتی خود یا جلب نظر کشورهای خلیج فارس که مستقیماً تحت تأثیر تصمیم به جنگ قرار می‌گیرند، پیامدهای بلندمدتی برای کیفیت و ماهیت برخی از قوی‌ترین روابط و اتحادهای آمریکا از زمان جنگ جهانی دوم خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123888" target="_blank">📅 12:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
هاآرتص: غنی‌سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست
🔴
یک رسانه اسراییلی نوشت غنی سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست و بازگشایی تنگه هرمز و ارائه غرامت به تهران موضوع اصلی آنها هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123886" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123885">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5afb45638.mp4?token=a_YnIjnHzEJHXYtBGCWjYz-AIPgMC6KSm8GPItkf4k1KSJ812b-XPml4k4SojCCpH6Y2DWL1uPrkZCRrYB5oN40mJVqMBGKyRXlvyxX1fwY4pSDMGmtQhLbD_a_Ujd7Quc9KaxIRVDH4AneNZGbcKahtadw8fwP7MFmZWcRuQa655-jhJOkQKRB4z5e-naNb7oX3d6mmVAbHuWvjBUCjcHaXLcYyalYapSOnlc9wnyY_rfudJvOsf13tl1zXCBLJ99Cv72G5450buSGCvIk_Q4oWe8uDcRBTlAsQR_SEoEGY7YshhHt-w0eb2KLL-dGHFdyHa240JK5WtF0QSo20Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123885" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123884">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b253c1d60.mp4?token=lkfGXnGAVB-hL9ZTWgsoVYDast_j9BiW-qriir_FRuMtgS5jKi3ElGXMdQF3CKOpbuj-iCMj3YwptJOmVe2xy4z37ig9LPQNz0WdufsbRSnt3pCut88lNI728wG-zxiLUcyzawewkphH3kMERIMBimlQEgErlPZYKXwi04YHL3NGoOD-lLi31d6G0rP0gnVoUfbR8OoV0WqJ3ty4mP_7th8rTBbEKPRfoIe1fkDzeh9-z6VgqOl1ELl8SGz_ES184QvDrPDo3VwHbC2FSYGBmct66yTkXfgX4VY40CWuHF9Y_GWMhBkAYac0afdjz1AjdTXT5z6p-EkYCbt1UZt7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما اصلاً نباید درگیر ایران می‌شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123884" target="_blank">📅 12:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: مترو و بی‌آرتی تا زمان تعیین‌تکلیف توسط شورای شهر، رایگان می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123883" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123882">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OIq6ZQYhdAl0PHxIJxegt_C52MYHd0VZgxo0vP71rl2Jo_8_1YyoPyHAXTrK1Si-icVfMaH6kqJO4D6fIT1G2Hr_0ef5crFVkp5FMgExnHBp1kt3m9_Iai_hwTXUj3Aeka_t_p2e64FZ5Wl8e3LuhcWt5XS7h9mlRA3hzZ0BQqo0nzCvN_D_Wjyp7X4nvTbLurj8jA2La9MO_abaCbshO-XKcg7C7xy-iY-IXWtpQR_IjIehxgFLoi4F9DviG112hhO2GRY0-WHSQfpA_2un7njVtv7ac96fqajwXkvwa_Wy199uoIwNfY7RjzsXq6AZ6Ki_ggDJQdi7J02t-2KSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=OIq6ZQYhdAl0PHxIJxegt_C52MYHd0VZgxo0vP71rl2Jo_8_1YyoPyHAXTrK1Si-icVfMaH6kqJO4D6fIT1G2Hr_0ef5crFVkp5FMgExnHBp1kt3m9_Iai_hwTXUj3Aeka_t_p2e64FZ5Wl8e3LuhcWt5XS7h9mlRA3hzZ0BQqo0nzCvN_D_Wjyp7X4nvTbLurj8jA2La9MO_abaCbshO-XKcg7C7xy-iY-IXWtpQR_IjIehxgFLoi4F9DviG112hhO2GRY0-WHSQfpA_2un7njVtv7ac96fqajwXkvwa_Wy199uoIwNfY7RjzsXq6AZ6Ki_ggDJQdi7J02t-2KSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
🔴
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
🔴
ولی اونا میگن شکست خوردید... این واقعاً چیز بدیه برای کشور ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123882" target="_blank">📅 12:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123881">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B23Z5sSVcIYO5rnOcXKpCmnzKo1t7H560EWXotBvWGqvNmcLxYg5AbDQA2kfMDoCA6Eh6CI2fH3rrduSRBBUJco6BCKsfGPOvkmYlhF2dV5LMbwMP7-ZzRjo9kCw1_llGV1sh2sw4TQd99s1xKYcMvxEUYQudh0yfOrfp1Uss7T9FsDrD1P8jLXTvEb8c7qP_gBqGzTPk1z79GIytq5yOZhyJrloxFh8yquGpUZVZ5nATRj9cN2WpiRZLbKMcqPG-oxgG4IiRbBU6B-qZNb0kqE5a84smP0bhiH12j65dNB0KmoaQCIPXElsxOFxAOzjoGS41b4K1ojt9slNF37rwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل بار دیگر هشدار تخلیه کامل جنوب لبنان تا رودخانه الزهرانی را صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123881" target="_blank">📅 12:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123880">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: برخی اخبار حاکی از موافقت آمریکا با شرایط ایران است
🔴
ابراهیم رضایی: همه موارد به تصمیم آمریکایی‌ها بستگی دارد. جمهوری اسلامی ایران چارچوب و خطوط قرمزی دارد که به هیچ‌وجه از آن کوتاه نمی‌آید. این آمریکا است که باید تصمیم بگیرد، تسلیم دیپلمات‌های ما خواهد شد یا تسلیم موشک‌های ما.
🔴
مواضع آمریکایی‌ها متناقض است. برخی اخبار حاکی از موافقت با شرایط ایران است و گاهی هم گفته می‌شود که آمریکایی‌ها مواضع خود را تغییر دادند. برآورد دقیقی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/123880" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123879">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی حکومت سرپرست افغانستان: توافق فنی‌ـ‌نظامی اخیر طالبان با مسکو برای حفظ امنیت و تقویت توان دفاعی امضا شده و کابل برای همکاری دفاعی مشابه با سایر کشورها نیز آمادگی گفت‌وگو دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123879" target="_blank">📅 12:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123878">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی گزارش می‌دهند که آمریکا به اسرائیل اجازه داده است تا فراتر از جنوب لبنان عملیات و حمله انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123878" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123877">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937516b130.mp4?token=bukCYJCfVLiM4f5VpbxuU8MEVBh2uM_goIQH8OqFz-gUunC6LJVtJs5rODJkN0iG0bQ8D3hzi7SFfPJrSWmByYrIXAJ1A9QvSM5GoqdUSWyaJUSvU8vbXqouhiAzyBONZ2pjvRchgmQ41QbbxA1Xbw5uHMMnPgykWrfDJbX4OE9molf207chzTyy20tHBFOaQGrfHQfG9ePykP5Gj8w9vMNnf991FicGOk8FXXuUt68BcnoTsr-6WDQUhDAumoPos9u5I4YGyjT1B1RjbutZuMEAt7SAxbLFii_lVPBfrTIHtqn69R0PBxn0lEuexm2qbM9c9te_Z7qdA-3cvyIIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937516b130.mp4?token=bukCYJCfVLiM4f5VpbxuU8MEVBh2uM_goIQH8OqFz-gUunC6LJVtJs5rODJkN0iG0bQ8D3hzi7SFfPJrSWmByYrIXAJ1A9QvSM5GoqdUSWyaJUSvU8vbXqouhiAzyBONZ2pjvRchgmQ41QbbxA1Xbw5uHMMnPgykWrfDJbX4OE9molf207chzTyy20tHBFOaQGrfHQfG9ePykP5Gj8w9vMNnf991FicGOk8FXXuUt68BcnoTsr-6WDQUhDAumoPos9u5I4YGyjT1B1RjbutZuMEAt7SAxbLFii_lVPBfrTIHtqn69R0PBxn0lEuexm2qbM9c9te_Z7qdA-3cvyIIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از برافرایشته شدن پرچم ارتش اسرائیل در قلعه تاریخی و استراتژیک بوفور، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123877" target="_blank">📅 12:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123876">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS6B2EkH7wU0FjUrbjI_kEQs__91O9VIrSydI498uVaZ8JMJDiGgtwJQaruBV1DYVisR8PfsVPH6FR_EWFnkbiXvetODUleDam821Ruo2zKwhg6lA_wYTnNKmwOtl5IXEpM1gsCI89Rf1k_HQd8dSDGFo299CXaZuqsA8nI96nhXwFUYyU2InJZNcfJ-IYYfTCGdSih38-GBrMIqp7quvETUN-4_d4LSuvsMcW2BgLb-9emajYZNAE7-ou2mOCtAFmPWHzuSSy0-Pywd6ncXny-rYOSAbZiq4LWmdSo_-ijX7NIwYekQJGWqL1l-uvuHPj7wJSA7MEYHUbaDf-yeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتحادیه اروپا در حالی که جنگ در خاورمیانه وارد چهارمین ماه خود می‌شود، در حال بررسیِ تعلیقِ موقتِ سقف قیمتِ نفت روسیه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123876" target="_blank">📅 12:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123875">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEIfXd_oMWtXyqcTWh-2IspdJ4q20-EFNa8tdS6Ab8ARtL-MRr7-Rd6DYa4mrSKifpm1vOnUbjMwiuje57k-LpVfXZzbasrCdtowUIId2GKDjb9mN86AKgzIa-xGfkRLTQfqYr7d5maXgqDvATYWBSXf0peqz1qdBobyWH9yurGmdqUYX-3Ot1GfbnyDJ4e9gl7V2j5KDEOPXpNgjEMhHhTeSSDAbG7vNzFY2yHOjkDopT9KX18rEsOKQO_Qd5VeesGkhODbiLMK0oHD-RWPKFsi8bD7zZ3qd4vYuOe1NVSreJpqOCc_9S4ILmaNrXkhKW7P9un6bkDBueFD0506dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمای نزدیک‌تری از بخش دم هواپیمای سوخت‌رسان KC-135 با شماره 63-8028 متعلق به نیروی هوایی ایالات متحده که هنگام حضور روی زمین در عربستان سعودی بر اثر ترکش‌های پهپاد/موشک بالستیک ایرانی دچار آسیب شده ولی کماکان در حال خدمت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/123875" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123874">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_9wQZlbZK37GcZMDJGA_EBnVGFPPCuTp3ZlXVn8mTpWod2DLusg4gzSJrzVglJisG6pdM269PRtEWiRbpvJKc1H-G10Th1svLL_KxpXd0LRIWmMXjABSKr9aZ2hcCAXDeq4i2ZBhwi50KiUX_6vk6jqhQiE7CUDuMxKQ7gTX4kid60iDBa9Qdbf_OxJl6tMPO76zgjaZ4mWaU5JHojwzRIcv9ZFR2qPXJ2L9yRm4oG5PKCTKOcQK3Cl5lNDaVdbkmrqaXv7Du-Enoe4J4Q7XMSeRsunNpFkR58GYa_RvS9GprXTuQ2B7W-eJAYps2VyfiKHu70sUjrDA-jhMXJJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123874" target="_blank">📅 11:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123873">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سپاه: طی شبانه روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123873" target="_blank">📅 11:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK14o2m2o__W5GSOLcn0O8aISBicMlznH5he61oag4UuK-oRJIvBWRAcO7FG0oMX9CZvUwczEo5_GZ9lHsOqL-5xOHVCNqOJNckcHyPrqOiAgGD3jsQYw6B6_PoYpN9_tIcUZ_NtaWrh_c3fH-DRyVXR2ndeCCF40sQtpJGWBRqIqF6Qt_tMz3I4LW79D3ESV6YjFV8FnEyZ89-3XOoJg9lWceREZnu2DQ8wdLR9IM_QIotSTpL_WhW6iVXrHW8JwzBY8CZ5nXNPCWdbQnOUmTftBk8Ic_5CpbVwuA4TPgEm628MnhprZNBWs5xCjys42eiZFep7zpZPW8dZiOXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد خودروهای پلاک مناطق آزاد در سراسر کشور مجاز شد
🔴
بر اساس ابلاغیه رئیس پلیس راهور، محدودیت تردد خودروهای پلاک مناطق آزاد در سطح کشور تا اطلاع ثانوی برداشته شد.
🔴
مطابق این ابلاغیه، خودروهای دارای پلاک مناطق آزاد کیش، قشم، اروند، چابهار و ماکو می‌توانند تا اطلاع ثانوی در تمامی جاده‌ها و محورهای کشور تردد کنند.
🔴
طبق اعلام پلیس راهور، این مجوز تا زمان عادی شدن شرایط و صدور اطلاعیه‌های بعدی معتبر خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123872" target="_blank">📅 11:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123871">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
منابع آمریکایی به خبرگزاری فرانسه:
ترامپ به دنبال توافق صلحی با ایران است که «خطوط قرمز او را برآورده کند»
🔴
منابع آمریکایی که نام‌شان فاش نشده به خبرگزاری فرانسه گفتند که توافق صلح منتظر امضای دونالد ترامپ است، اما او پس از جلسه اتاق وضعیت کاخ سفید در روز جمعه هیچ تصمیمی نگرفت.
🔴
یک مقام کاخ سفید که نامش فاش نشده است، گفت: رئیس جمهور فقط توافقی را امضا خواهد کرد که برای آمریکا خوب باشد و خطوط قرمز او را برآورده کند. ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
ترامپ گفت اولویت‌های او برای هرگونه توافقی شامل موافقت ایران با عدم توسعه سلاح‌های هسته‌ای و بازگشایی تنگه هرمز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123871" target="_blank">📅 11:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بی‌بی‌سی: صدها نفر پس از جشن‌های دیوانه‌وار لیگ قهرمانان در فرانسه دستگیر شدند
🔴
درگیری بین هواداران فوتبال و پلیس در سراسر فرانسه منجر به بیش از ۴۰۰ دستگیری پس از پیروزی پاری سن ژرمن (PSG) در فینال لیگ قهرمانان مقابل آرسنال شده است.
🔴
هزاران افسر برای مهار ناآرامی‌هایی که خدمات اتوبوس، قطار و راه‌آهن را در پایتخت پاریس مختل کرده بود، مستقر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123870" target="_blank">📅 11:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی گزارش می‌دهند که آمریکا به اسرائیل اجازه داده است تا فراتر از جنوب لبنان عملیات و حمله انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123869" target="_blank">📅 11:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
میدل ایست نیوز: سرمایه‌گذاری میلیارد دلاری چین در عمان
🔴
دولت عمان با جذب یک پروژه استراتژیک یک میلیارد دلاری برای تولید مواد مورد استفاده در باتری‌های لیتیوم، گام بلندی برای ورود به زنجیره جهانی تأمین انرژی‌های پاک برداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123868" target="_blank">📅 11:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5411c3d8c3.mp4?token=uHtttZZVnXnb-Ii-E3k2ps9AaqyfVc7qwGy0BipoEo5faaLVAIcM-Cp7o3sjumZmIxO6jMgZEeSzDEkLO8slMAzEG-LYksgH3wGN1G0H6AASh9jwclCb_7SM_2b9cRqVqMFEhC3Nxcv4mROV-Grb3C52RauILPOWiq0I5Zwm4iw1jcEeqNTlMCb7GyoWAVHYxRnFe0Js8DFz6JahocuB1P_B8tl3nNe7kWs6ENS8ZeVXYe-NuTggrv-3dgP1CtXiEAx7wlfx9BC2_A17sgJ1VJs9F7sSgUQMTf31RCDyL_lOEW8KhMvP8pJ4SBwrg_sgg9sGK4abPl5Wt4AICcn3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5411c3d8c3.mp4?token=uHtttZZVnXnb-Ii-E3k2ps9AaqyfVc7qwGy0BipoEo5faaLVAIcM-Cp7o3sjumZmIxO6jMgZEeSzDEkLO8slMAzEG-LYksgH3wGN1G0H6AASh9jwclCb_7SM_2b9cRqVqMFEhC3Nxcv4mROV-Grb3C52RauILPOWiq0I5Zwm4iw1jcEeqNTlMCb7GyoWAVHYxRnFe0Js8DFz6JahocuB1P_B8tl3nNe7kWs6ENS8ZeVXYe-NuTggrv-3dgP1CtXiEAx7wlfx9BC2_A17sgJ1VJs9F7sSgUQMTf31RCDyL_lOEW8KhMvP8pJ4SBwrg_sgg9sGK4abPl5Wt4AICcn3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از کافه‌ مروج شیطان‌پرستی در خیابان ولیعصر تهران که توسط پلیس پلمب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123867" target="_blank">📅 11:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فرمانده انتظامی خراسان شمالی: ۲۱۵ تن برنج احتکارشده، ۴۸ تن آهن‌آلات و میلگرد و یک‌ونیم تن آرد در استان کشف و ۴ نفر در این رابطه دستگیر شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123866" target="_blank">📅 11:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الجزیره: روابط روسیه و ایران آنطور که به نظر می‌رسد نیست / هدف مسکو تضمین عدم انزوا، فرسایش یا شکست استراتژیک ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123865" target="_blank">📅 10:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سنتکام: «پس از آنکه خدمه کشتی از تبعیت از دستورات خودداری کردند، یک هواپیمای آمریکایی با شلیک یک موشک AGM-114 Hellfire به اتاق موتور کشتی، آن را از کار انداخت. این کشتی دیگر به سمت ایران در حرکت نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/123864" target="_blank">📅 10:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پزشکیان: همچنان در برخی عرصه‌ها با فاصله‌هایی نسبت به کشور‌های پیش‌رو و حتی برخی همسایگان مواجه هستیم
🔴
فشار‌ها و چالش‌هایی که امروز جامعه با آن مواجه است، ساده و تک بعدی نیستند و راهکار‌های آن‌ها نیز ساده نیست
🔴
مدیریت نباید به حلقه‌ای محدود از مدیران و تصمیم‌گیران منحصر شود
🔴
نباید در جایگاه تماشاگر و خارج از گود باقی ماند؛ حل مشکلات کشور با نظاره‌گری امکان‌پذیر نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/123863" target="_blank">📅 10:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc46929eda.mp4?token=ZFH9Skelm9YAWZ2z044vsJImrIZYzJpFYg1He6XZTCQdIbW9RzXZQcSrEt8kBk3t3DZzIbF6A8R4-QLEzG-MsstgGFKBMWho3_Pcw3NJGSaPsWTWrWXrj58oGcWgrXdux2vrLUI9K1fh__7NIzj1yPA_Fiyf_kESrEkFnxpUshoY8ZhiFhub5hemTirBEzj8NmlocITJPMbfxckD_uBWFC_oyG8And9TuNVfFrjIIsmEr9ijhUPr6gvgB3HKKJVQF21FCFxMSCzWL6V3bYk9oC0nulzrG8GV-WrOCRwi837xIUxqQ_QUBLPxUFK339cSZB8wg3yj_purAntsWR6fpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc46929eda.mp4?token=ZFH9Skelm9YAWZ2z044vsJImrIZYzJpFYg1He6XZTCQdIbW9RzXZQcSrEt8kBk3t3DZzIbF6A8R4-QLEzG-MsstgGFKBMWho3_Pcw3NJGSaPsWTWrWXrj58oGcWgrXdux2vrLUI9K1fh__7NIzj1yPA_Fiyf_kESrEkFnxpUshoY8ZhiFhub5hemTirBEzj8NmlocITJPMbfxckD_uBWFC_oyG8And9TuNVfFrjIIsmEr9ijhUPr6gvgB3HKKJVQF21FCFxMSCzWL6V3bYk9oC0nulzrG8GV-WrOCRwi837xIUxqQ_QUBLPxUFK339cSZB8wg3yj_purAntsWR6fpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر به ایران حمله نکرده بودیم، از سلاح هسته‌ای استفاده می‌کرد و دیگر نه اسرائیل و نه خاورمیانه وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/123862" target="_blank">📅 10:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ew8t2FPVQAksFJ7KwrfQs8y7kIExhaWta1CZC91TLXzM8WnBLDMVP0eHkx8ybjxpJKWy6dWDinhrFyWi1XCfbmORrtr8u_I6h-tl8L6L3cOPM5LekC7wJSJ-T2qmDl9xMNisnupUX4MBNBuUjpRB7-2ZGW8Qacq0TKU0MEvyWwiD8QI4ma4uNx9ieDIK7LS945Pf3QriAKndd62pc_Nn37XeO50fhx_BTzNC60lN25G-qL74jWy7mwEyg6MDdEyeaRQWlg59ufvHK1chQxqwm-qTaZg0YISLBA5ngStxEe5ujltwKsmjeNcZFAchgn3AEoW0luMyR0Jjc5HobrfqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ew8t2FPVQAksFJ7KwrfQs8y7kIExhaWta1CZC91TLXzM8WnBLDMVP0eHkx8ybjxpJKWy6dWDinhrFyWi1XCfbmORrtr8u_I6h-tl8L6L3cOPM5LekC7wJSJ-T2qmDl9xMNisnupUX4MBNBuUjpRB7-2ZGW8Qacq0TKU0MEvyWwiD8QI4ma4uNx9ieDIK7LS945Pf3QriAKndd62pc_Nn37XeO50fhx_BTzNC60lN25G-qL74jWy7mwEyg6MDdEyeaRQWlg59ufvHK1chQxqwm-qTaZg0YISLBA5ngStxEe5ujltwKsmjeNcZFAchgn3AEoW0luMyR0Jjc5HobrfqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ : اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123861" target="_blank">📅 10:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7614fe349.mp4?token=Sw5157SHYs9MkA1yq4TbXj0pnV2LCm18Hs29PsPgP_CxWEzG1A_zwbdLvSfQm8MMUtoV1_vQHI0sgp9C09gSnax1if2MjEioupHBBD6GpmprbejkKY1WhLK2DZsd1LE7_PC1M834ZE2qqjoEmPI_azqTQZEqRotgfKu9T144yUnxb1cVI1Of3OZ21715tQffqrdXoFc1oGon8_Nc_J9YKtOSSDlaEYtxhljUj41Wq7mLycpPyneIDEvc-PCRTUNKxjTlJjaG4D4FkHu8u7DrKHkiba5Gv4ehzGFrwU7ss7QRRc704UpVY43IIYXss3ixk03PBEXxjTrSkKbp-rRGFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7614fe349.mp4?token=Sw5157SHYs9MkA1yq4TbXj0pnV2LCm18Hs29PsPgP_CxWEzG1A_zwbdLvSfQm8MMUtoV1_vQHI0sgp9C09gSnax1if2MjEioupHBBD6GpmprbejkKY1WhLK2DZsd1LE7_PC1M834ZE2qqjoEmPI_azqTQZEqRotgfKu9T144yUnxb1cVI1Of3OZ21715tQffqrdXoFc1oGon8_Nc_J9YKtOSSDlaEYtxhljUj41Wq7mLycpPyneIDEvc-PCRTUNKxjTlJjaG4D4FkHu8u7DrKHkiba5Gv4ehzGFrwU7ss7QRRc704UpVY43IIYXss3ixk03PBEXxjTrSkKbp-rRGFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: ببینید، دو چیز میخواهیم:
🔴
1ـ تنگه باید فوراً باز و آزاد باشد، بدون عوارض.
🔴
2ـ اینکه آنها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔴
همین است؛ خیلی ساده است. سپس ما از آنجا خارج خواهیم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/123860" target="_blank">📅 10:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQS6Fc3AA2PUC-wdBcKgv-36jXiLw-h-KZBBTyYTtKW8kGrIoZk0rDZd-tqerW3bSWOjodBRemdFY0EC4cp837MWkstMGSZxqN4kMEgpHATMrHhEIUkUw8RIrzwlIUEAp7ESHnVGyrf5VIjnhX2V7BwRjWqou483zcZ0P7Jb4ifWJPhLccNHzv1aS-DhchQJUnpUjGAkDCWjsrSOfp-8dp3SzG6mN6sm8j95EgJvbr2b2_q7uV3_3tvEFB5377oy_bvr-HJt7H2SB4SOfJ9vWzSrdiixDY9yPnbXP-1LZEhYkDxRKR_PAnG1b7MZNg8Oiwpq4HIf-E0AsZbqnAxh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تلاش است جنگ ایران را تقریباً تمام شده و کاملاً موفق نشان دهد، اما روایت او با واقعیت همخوانی ندارد و پس از سال‌ها تحمیل نسخه خود از وقایع، اکنون با بحرانی مواجه است که با داستانش در تضاد است، طبق گزارش نیویورک تایمز.
🔴
در بهترین حالت، تغییر رهبری رخ داده است، اما ارائه آن به عنوان یک تغییر مثبت توسط طرفداران جنگ نادرست است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/123859" target="_blank">📅 10:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آکسیوس به نقل از منابع: درخواست های اخیر ترامپ جرقه دور جدیدی از رفت و آمد بین واشنگتن و تهران را زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/123858" target="_blank">📅 09:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:  آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/123857" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یکی از مقامات کاخ سفید، به آکسیوس:
آماده ایم یک هفته یا بیشتر منتظر بمانیم تا اطمینان حاصل کنیم که رئیس جمهور به خواسته های خود از ایران می رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/123856" target="_blank">📅 09:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAGLiiYeyuZVmVSU_bOdIDlrRsxlzgybhmudsVi_5Xak_hUHMFy2MUcv5CaKUqnJ5FoL8nUbSrquVId9TzayjUNbCpnnT8PjMLarXA4Ry0sm5FXzp4ctErv6Rvh-sicdM-6zdUNhKkiTlgo41T1C7kN_fcpT_vKimiRpD6VybK82i8Jehv0OUejvAWAHxViTD_s5_UctIPaXFqGR1BhOUQXDuytYcEkI5Tfpc5a1kFJdIv_pOE-O5bk69Fqmjnm2o1wPO7yuS_85RLyx9zojwpRBgd7bvYJJQBx4oDGojcOtqfvO7SbhjyhXSmc-pjkWVIGbzbBbt4FTkedFEIal4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس برای دومین روز متوالی سبزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/123855" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs4JsOhn1cbgDX8TgwYne0hzuqntgNt3r-PnQVg-cCGpZcUX61EsmCOZQQSwZFeM4laloE66LKkRuowauhiQ9Oh146kBmltOC-ZunodQX01fNI60x5dUDzwXwXkfitgfm9f8iVavo79CnvVIsutAr4k4YxNTxvcZ095QaMMs9eCfWqiVkki-5UV07pRmDmXV6uqUJ9oQUGKcZAZZdbQUpF3GX03N7fVTxEsFv7UwwVi06UhOyfuJZ6SjGdjfjbaQ5RbYfK7QoeDGN0jaFwIZeIpzmOuEslcKpn09_VnjtQSqnyw8kHROz8iDd5d6BO8I2Z6T1s_vn0bJN5O6pBi9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social:  «دارید گیج می‌شوید»
🔴
دونالد ترامپ در پیامی کوتاه در شبکه اجتماعی Truth Social نوشت:
«You’re getting discombobulated»
که میتوان آن را به «دارید گیج و سردرگم میشوید» ترجمه کرد.
🔴
ترامپ توضیح بیشتری درباره مخاطب یا منظور این پیام ارائه نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123854" target="_blank">📅 09:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: دستور پزشکیان برای بازگرداندن اینترنت بین‌الملل کاملاً مطابق با قانون اساسی است / فروش اینترنت پرو هیچ توجیه قابل قبولی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/123853" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔴
پایۀ اول ابتدایی: اول خرداد تا ۱۰ تیر
🔴
پایۀ هفتم: اول تیر تا ۷ تیر
🔴
پیش‌ثبت‌نام مدارس شاهد:
🔴
پایۀ هفتم: اول تیر تا ۲۰ تیر
🔴
پایۀ دهم: ۲۵ تیر تا ۱۵ مرداد
🔴
ثبت‌نام پایۀ دهم (عادی): اولویت الف ۲۷ تیر تا ۱۰ مرداد، اولویت ب ۱۱ مرداد تا ۳۱ شهریور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/123852" target="_blank">📅 09:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUJF8gBH9aAWASY8Rr3U8iEq-UPeVBryhrMSQJZxYIHm4zwMeZ2-fg8gkOhy_cZM9pOjCchLam4YfE0bEOYWg9Xc29sWQ0gtrxnM5zX55p_7ITg0mEfXILmAS5TMuEw_A06Oy_t8YyINmusIftFAOpk4EY_O3mnoJvJ4e0SuK33bsKYB_69W3w6RSUCHG8Ic3iRoBJC7aqD-YZrHTubMpmKi03lO_-73OadO3RGd-4C3GdiQDkJfjAaEjizMn3VVGZA4VeCiF79k48ARS7xOGPQaW2jmh4qQLUO6XoPdNCVtwBl3JqbXKuQ2O5864wuALtEvW3lDdlNiuE53vbhXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه‌های هواشناسی تا پایان هفته برای شمال‌غرب، شمال، و شمال شرق کشور ادامه بارش‌های بهاری را پیش‌بینی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/123851" target="_blank">📅 09:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اسرائیل هیوم: ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/123850" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
روابط عمومی سپاه: : رهگیری و انهدام یک فروند پهپاد MQ1
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/123849" target="_blank">📅 09:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز: ما به یک توافق بسیار خوب با ایران نزدیک شده‌ایم. اگر این توافق برای ما عادلانه نباشد، دوباره به وزارت جنگ متوسل خواهیم شد.
🔴
گزینه دیپلماتیک را ترجیح می‌دهم، زیرا امضای توافق به معنای بازگشایی فوری تنگه هرمز به روی کشتیرانی است.
🔴
تنها تضمین اصلی و اساسی که بر آن پافشاری می‌کنم، جلوگیری از در اختیار داشتن سلاح هسته‌ای توسط ایران است.
🔴
ایرانی‌ها در عمل قبول کرده‌اند که سلاح هسته‌ای تولید یا خریداری نکنند.
🔴
ایرانی‌ها مذاکره‌کنندگان بسیار باتجربه‌ای هستند و این موضوع زمان می‌برد، اما من عجله ندارم.
🔴
تنگه هرمز باید فوراً و بدون عوارض عبور باز شود و باید به طور قطعی از در اختیار گرفتن هرگونه سلاح هسته‌ای توسط تهران جلوگیری شود.
🔴
نیروهای ما به محض بازگشایی تنگه هرمز و پایان یافتن رسیدگی به پرونده هسته‌ای، از منطقه خارج خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/123848" target="_blank">📅 08:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ شرایط چارچوب پیشنهادی برای پایان دادن به جنگ با ایران را سخت‌تر کرده و پیشنهاد اصلاح‌شده را برای بررسی به تهران بازگردانده است.
🔴
مقامات گفتند که شرایط به‌روزشده تا حدی ناشی از نگرانی‌های ترامپ درباره بندهای مربوط به آزادسازی دارایی‌های ایران بوده است.
🔴
ترامپ همچنین از طولانی شدن زمان پاسخ ایران به پیشنهادات آمریکا ناامید شده است.
🔴
چارچوب سخت‌تر اصلاح‌شده ممکن است به منظور فشار آوردن به ایران برای پذیرش سریع توافق باشد.
🔴
در حال حاضر مشخص نیست چه تغییرات دقیقی در متن توافق ایجاد شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123847" target="_blank">📅 08:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
العربی الجدید: همکاری نظامی بین مسکو و کابل؛ روسیه از طالبان در زمینه سیستم‌های دفاع هوایی و سلاح‌ها پشتیبانی می‌کند
🔴
در جریان درگیری اخیر، ضعف اصلی طالبان، فقدان ابزار لازم برای بازدارندگی نیروی هوایی پاکستان بود که مسکو برای پر کردن این خلأ حیاتی وارد عمل شد
🔴
پاکستان انتظار نداشت مسکو اقدامی انجام دهد که مغایر با منافع اسلام‌آباد تلقی شود، اما این اتفاق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/123846" target="_blank">📅 08:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ادعای اکسیوس: ترامپ چند اصلاحیه جدید به توافق به دست آمده اضافه کرد
🔴
ترامپ در جلسه روز جمعه، خواستار چندین اصلاحیه در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن دست یافته بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/123845" target="_blank">📅 08:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XG423WQsbs-vHMX6wCwMTVL3pn811Lb57-umHVrpXOJevqi0x7XpbsUuxStgBafgNNceNxdaIjPrKFMNQd-ZChhaWF0lYgSt9PQhvJGBqZELvFvJ2ZLhRYLW2i7_sCl87AmZQqETpjAxoJgDx5vlioQWkepQ1fHCYl32lmz282nQEr8DiaErdtJRg5iCsUh4Qn8uk5j2OWEcMVojtUzGSzWyHt5ckCh-l9Cbow1iYWJ3_ZHmdoOWMn-6yPbaSp5zyrnS-hF-CcVPmSsptuZPVjzoKqAFTBp2mW6tJkk8XY8mr5DWOVUiAFVwwdLWXTsJyST1gDdPUICGeent7uwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
مطمئنم آمریکا بازم به ما حمله میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/123844" target="_blank">📅 07:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f990f36121.mp4?token=Hzpa0ZE9MDR_ZqU-A6qNunwI1_yUx9i5LXfXYfZaydSSSn6wY-VCXLo2aLMCvokRioiJJ3NVbaoq2gbwPHZXKS4drVbc0caTGUFSY5oCTlHBZLt37ZVqryLOeDfkbiNbEiHzHuqkzxABAr6_rMgFiLv_4UJ43Tri4cD5MXcFkPELPFR7QHfmospfifiGesn4bymKlMu66t9X1nCmXPnVXg7H1sQVorPLDqpTp_s79oh_njL9vUKN787oUzVx5X1Z7PXeJVTcC5lDDIQ0j0Fll6jataskgdQYHOng04fySClKI_LAExiBHve8ijToKkmZuIeyfvNj7qdOK7IuI_TEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f990f36121.mp4?token=Hzpa0ZE9MDR_ZqU-A6qNunwI1_yUx9i5LXfXYfZaydSSSn6wY-VCXLo2aLMCvokRioiJJ3NVbaoq2gbwPHZXKS4drVbc0caTGUFSY5oCTlHBZLt37ZVqryLOeDfkbiNbEiHzHuqkzxABAr6_rMgFiLv_4UJ43Tri4cD5MXcFkPELPFR7QHfmospfifiGesn4bymKlMu66t9X1nCmXPnVXg7H1sQVorPLDqpTp_s79oh_njL9vUKN787oUzVx5X1Z7PXeJVTcC5lDDIQ0j0Fll6jataskgdQYHOng04fySClKI_LAExiBHve8ijToKkmZuIeyfvNj7qdOK7IuI_TEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوریا زراعتی مجری اینترنشنال: اپوزیسیون ما رویا فروشی میکنه و وعده هاش دروغ بود
🔴
ما به کسی مثل جولانی نیاز داریم نه رهبران فعلی اپوزیسیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123843" target="_blank">📅 07:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ifk8ZdESzLu2A1IDJWn8GgxHD7jRaW4dKbzYj2085FWxgHLlsv0Y8aug05VFzMgCKdfAhfoQ1JPztsUZFym1FXu-ChdOBo2jblEF-_FviFB8N_OhcqKiOnArM5xBzEi-v4vq74c1Pn8dEdlkd27Rmt4veEldm24TjgDyZ-dp0rZ4iVMIDIcAFI9d9jPqt1WlN8wvMlaOxT21xBmJy_-JUWMgKVprgzyZfJec-1eXFGtoD4hhgM17dyCLv6o-tYJ1o7np9GZ8rkFYu78rVHe7umwAEfOTrA47dphsuQ1mThrgKot-uGZWK4rgBEY4o1hoU_bUMc3mcNI95cLD22OcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 9T!
🚀
❌
آفر فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
💎
کیفیتی که بعد از استفاده متوجه تفاوتش میشی!
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/123842" target="_blank">📅 01:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS5o2S54tZH8WovvN66N5ykGbIJGfaORAU9V9h8iTQqrBzyf2_hT77U8d-AdohRQ788MA0YjKGLcYcROcZGIEq5U2gafyBYyXNJgAr86VHLcVGcJPX9yFkTAfgRIGKPWm5WLs75svLEsPT1Pj7592pXWQ8NGj7Ogq4wpZ3dBcycm6-4wIBcuo-csC5ifpiyL5pYbA_a6Egoe1ARrjBQdZYVwPFgl3hEr-ZpBDl72GlRmdWmp6oqg-7CRaHjNwz0ml0N-r12C2aIjZNF33P8cqlI6Bc2YFuuFTXUoVWCWj_mHYluirLhbZdHAdU-E_Fe-BEBCupzMSK6DgIcmCEUQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/123841" target="_blank">📅 01:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lepcHbcUjQV2HqYzVp6244I2eeY7gQDGwydn0W-UcyuVW31wvis1i_khbgaPyu9Lt5FCcisrpjb_cDwc3XBUe7JOKfMk4MMtHkF9tJqObOPINWU8tlIEgfQKGpjAQIObyIMQi3-nwu_SZfqWz3IJCqjzZWrsTzRc3IxDtcvi8yv2KDFl4WmZucEbhRVr3d-G7hgh7lWIMF6VvzKR9tWcnc9NQwAFBnY1uiti28C8W0p-WU-PRUNOuXA3n8Vy7JjVkRT5JKtV-mCI_sXJQDsD1LuZ-wEr-bL3z-QYYTU_FVpiAZpqV3Z3KcDZ8fc3ea4a8SIovyacoqxdDgVtYNjXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTGwytZPK3qFsGyqEbITT2978zaYg-rXQ5irKUBtIBIHr_wEismpQhEIl2LVUPSYu8SCibxy7uW3frcrgjJptuZkYFpdi1ANKOtS9A5BVXG-_DURmQOtejb2Ocx9mHbZDlbSSL68cG7EkM_OCfXjnofNOSvEz0_w9lu1kwacSbdzwuaADDvvAGBDPugpzSYevz2jjvZPTsEQY75Z-9_1o8zP_SgfU5Wi-hqksbNj1AQAcVD_adsSqlrhpL0mCE4uaOAVPh0j5CVbZ2crpgVTHhIi94ID_5MP8sWGD0GL5bImQR_4nvpYycv7jPbLemdBGpt05vg8PgKm1pfcMuDOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uf6yKb1W-diEGNqFZp2r53t8qwAWfuf-i4eXXAn26YVNxIhNw7jV8hn5Hz9FOsIpJaLv0hx6_JnvSM0RRQCYuGS1eGpQeOCdioQJZvzMgvvHR68yAj0jRXilD1SiDlWQneTNsCj7QGd1vl8PzduvFXvBeI4bKAhYbIv6abOMsFOXNtYkimIrcg_lcxU6bYSAOEWiGa7e7-tZZ5n0kHhdeM3pePndUPBC3b7OG5sWLFXVG9D4FD9onN_8vDs29V7yKVomg2Y7MB3DOtENSoSy5SLOFDFCTwcNRfhblK_4KNIj8BZnB9w7mvTHSMiUsv_I9GX1S5kS5pXmqJd37imdcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ss3kZ5KDH1D5zC_GbF5J2J5PoRa60qLfZtaqGj6GXyl0Mw6U5WgxSbdPIf30lWFv5-8gYoGLVm5zL_ijjGIEDso8wKNTqKxElZ34-geQyrbpd05OsvJ7OKpnDRtFw3ZF3K10LXo98B-HQOc1OKtkrxRSErYClhfsCXvcf2KvIFRAGZM7MrH2HNqFKud4GPBxBz5iiSZFmDdzoct_CL7vN1Pf0s7ImBmK6M_EsD3k_99Lz_-5woqesHt0BFrdux31IWWLINScGY0rHHZUTKc6_xy_2yfEykbIZxPyJdJCMbvJ4WYEZ0cecn0HA1y4VYeTT-a1zNf9h9edLTrgP2OgOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ بازهم رگباری پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/123837" target="_blank">📅 01:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1def876b8.mp4?token=FDMjpzKNunQFYZPhjKEYLeLVMkrgC7hMpl25diCseMj0jF8mKmoI6ZOEqUSuQVg4uSlUb7E4k95_oMUAw18cMrUrTwrhMhc2SvH29W9ekTwWYdWbk29GwtOEb5HEdUdlSAwlTvEbF1rDX0j30nLnZMR0wOFZA48zkEWOr4P_wsnGdiaEgVQ08hfkjjuc2_ISpyW-luyAqQeSSaljXSavsB5qe8Xklx5qGtPeo7feJVjKAFzh7S9iTIpkUH9p1IzMsTwdflkvht7DvYaRWMyuM-kmMsFvpcusm2TLMLkxHKzEykU2zLDDiWjeC5VY4hnyUzL7Oq6bhLmO9MsydMeYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1def876b8.mp4?token=FDMjpzKNunQFYZPhjKEYLeLVMkrgC7hMpl25diCseMj0jF8mKmoI6ZOEqUSuQVg4uSlUb7E4k95_oMUAw18cMrUrTwrhMhc2SvH29W9ekTwWYdWbk29GwtOEb5HEdUdlSAwlTvEbF1rDX0j30nLnZMR0wOFZA48zkEWOr4P_wsnGdiaEgVQ08hfkjjuc2_ISpyW-luyAqQeSSaljXSavsB5qe8Xklx5qGtPeo7feJVjKAFzh7S9iTIpkUH9p1IzMsTwdflkvht7DvYaRWMyuM-kmMsFvpcusm2TLMLkxHKzEykU2zLDDiWjeC5VY4hnyUzL7Oq6bhLmO9MsydMeYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغ چادر پلنگی در ایتا و روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/123836" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAkh1HZlOo_MLw39XWlIBdyrJUSWnYB7QVjgBPLgWGTttsWf3Xw-_D4wFF-d761_AwlMfaVXNjWpd834cHmQEEmsFd2gxLjSgDKCdN9-WSutvC0DpbJ4EyaFU5L7BheNLyohzsyaxRH6ErCDBUcHul5wjL_9E_jR4d3NnP3hJ905weOP5t_6GR1b_wTfCtga_E_AiUAwYp6KQqZo9NJND7BUR2W0euBW50ATCgMB4nUFCHczBFiSWxqiQo1RnsSGjIgsvdHU6FPPlxwjanflMSZnqJXAS7pBxgjq3Q0GAolga4P2IeDdG_q0VJglpyGC-skAyxFDpI5b7usuhOUung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابش فرابنفش
🔴
این هفته شاخص فرابنفش بالا است، تا جای ممکن در ساعات میانی روز(ساعات۹-۱۵، با توجه به داده‌ها) کمتر در برابر تابش مستقیم خورشید قرار بگیرید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/123835" target="_blank">📅 01:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1s1JaMNF6xsmarGKKDfCR1EwIIWV99_ywlo_EgaFeWW0Wo1RO5S6iwyDNbgFBho6_jJWtOuG8AXqsVvXJAeGpagTELppGVglx5Wz2JPFiKwaAe__Kt0NUjNJ81EGkpErQV4WCjaZn6JTDkbK2lZjpJArt91uwTiLPJ20bFnjQi2y29hGEcRdnParSEZ8nlJJ3kIxJj0J1SE-Vvy_HKyr9G8A0iyrY1MKwsVQt945uCX_X2k4F5MdnK6wToAkN9OPIuG3uAquywRvv3ZWWwQdto9WLfgAAwRXOTAUORH7V7ejlYRas1r3LpLvJ5Zp0rZioZKSMq7mDKm4mGo6KKjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله: یه تانک اسرائیلی رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/123834" target="_blank">📅 01:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Tf76oSPYuon8Lrje9JDmnDRtI6rIXb25HXWKOr2OdJe-SKwkl7_5ZNf5eaHbnuN5yotv8apj31ZmxaQ2U_xi2fgQ3-EKhJEAwTMAEOkw_DYYlU73xPAwDI1K-aSm649Hf9WmJcogJIorrnXiwVGZIDPZPF_JdBHzM3LFZOBFrgjHPKPi-sfHW1j9LltE4mTx0675cUpEtOdtW0kxLen8KQp27sltB5hVy4-wdkIoTsnEZKjr14EPY6Lwvqr_jbOIiCQ-s-KOEOcTgWxPtGNvfrHoYdX0RXOxvV0sALliwkzEf2y8YIJSyXYBdUAEkVlx_jdAkdUyklw0_1AHzLD8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/123833" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیروی هوایی ایالات متحده آمریکا برنامه دارد در قالب بودجه سال مالی ۲۰۲۷، تعداد ۱۵ فروند هواپیمای سوخت‌رسان KC-۴۶A Pegasus را به ارزش ۳.۵۲ میلیارد دلار خریداری کند
🔴
با تحویل این ۱۵ فروند تعداد کل سوخت رسان‌های پگاسوس تحویلی به نیروی هوایی آمریکا به ۱۲۰ فروند می‌رسد و برنامه نهایی تحویل +۱۷۹ فروند است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/123832" target="_blank">📅 00:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqwnvD8A9T1qnNKWqH4wEdIMK6CuWDsk23NUKvrTg9tSV0_0RH1DDz5mB-yDR8po0iB-uQc-l3Pu5bIiF6DRjL05ZpuLQO8-ada70tQwPVfs-jG9jE55MCYC-g-GO5zsjivcQ5vOiTmRHjO4nfgiKOHxpL39s4vaZD-ZwYqiWNrxZiUrKJJwMM4LKDOYMO88UeGo5hwnpDh9Gb4U_sQukRimmhI_9jgMWFzeUj_esu2dPOzzZCppTef1G6q9r45zaHaz_b0MrWi7q0kUIP-CwlTMG3Y_H6NQKAkDqJ9vy28siUYrnDVxP3YM4i8yJvkvy0jYW4VDmh0uwJw_4ZpTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
- یکی باید به پاپ بگه شهردار شیکاگو به درد نمی‌خوره، و ایران هم نباید بمب هسته‌ای داشته باشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/123831" target="_blank">📅 00:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f8f1e279.mp4?token=RYezsZKYeY5isiGz30V3oY-N-sCGjcBWesHeKFeW7KRZe1FF2raTIHEnmjkcJuiCHN3IKILBDwrcNwAj1Y7FW8D-pPN8JvUULxvet2ny7ousVWIvertgOtqzCJ48N6Rjy48T4FtK3mi1IrERkpSyQTkQ3i8xSv_nLwxWZzpJHRv6f2eo6DzWM06ltqXD7nNmV7qAH6jk4uG4HcWNtuHNVZALHNcbY4kzqd876mGUIPdpG4dNHmJ8REmWGbKXg3gdQrspazMos7r_mi38DvV3fFxcAFgkiQKYLrjyNYLwykyb5zZDR1x9pMnPrXOnxHpXEc5uEm0aowUvi3vGSrECZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه مجری تلویزیون به تاخیر ۹ روزه در انتشار آمار تورم توسط مرکز آمار: اعداد را اعلام کنید یا نکنید مردم تورم را لمس می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/123830" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgWw7HvlskBioyIOEY1wuEMujs-hopR9moUmWBcPM0VVlfrUjNCwdw0ko59Td-KCHFYRFUhyEmAYrlTguvj4uBBYKYTz5jqchz1Ntk5096bQ9lvt05AAT0H87Op8UFhpvpC5zNAkU2qVmxVAPzhj1jJbeej1wPQ7J5qY-Eyk7cOG8Dkeo4813vaBOh3dQomN2MJLzt8Z_PQ07C-ULERQ8hm_HQKUE2MLFZdvJq6Tsia6IWv27P6050FTukEXaktSVQ9A3rNueKwqJG0-Wye7yd114E-3-Zh2uCIjpAsJ5KeQeBTblMx6IF-s9OGUq8OWJKjDo1TYLCLqQuByKQ1-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBbkszbfDJPySq1zxsYZk6doO807kSFsRQHfSfN2SVqNW8qZhxp5bjPIXagyWOV2xv9xCSlQ61pwHHNdU1l9eVmXy8gAf1SLV2wcsL-fn77wgkMjWfdktioT6qKlk9DGKxZfLrCz806x4OBIm9p2ELL1s5WP20y_LuvGpcdIJX54vHZP8V8pF2fR9hj5zXiUW0F6ehnSPCHEaiaG5yKjp0tigqQdWA3-ZyaNPwR1S5QXHiDvDqvIhg6J5YydEXTCki5gP9edKiznPfTUv3YBAfy90O2JDv_h8kcCRWZV7_OnRmyKO7yVM8H6LAtCDOPT5-54by9QJEBb4dSQ_VTuNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل بر کفرجوز و شوکین در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/123828" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مدارس شمال اسرائیل فردا تعطیل اند و بنظر می‌رسد اسرائیل خودش را برای موج جدید و مرگبارتری از درگیری با حزب‌الله آماده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/123827" target="_blank">📅 00:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
به حداقل ۵ جهت به سمت فضای هوایی اوکراین، پهپادهای روسی Geran-2 پرتاب شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/123826" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj4mIpnX8OGb1LnKD0B0OZodY_GKL-CGVhXfiHZLRYwA2-3UWMebbe5bxOg2ThN1c_cRtGfI-_VZ9jeOi5vkRowF415V4ho6Z8b5u2xHef6mndXYKxX5TO23RWk7CCfGxkadMelazSnpRhR9NgVHKnUqb2O1zD6BK_LKfnxuKQgvfVDk7BxY2EFexMbUXzlZVb8sciI0FtgEIBT11leEN46GdjrWTVRvEV6u8d_hgnu48OmOaklU56k0_x52keao5i5OlBcvbFTKqmYzZFYO79mr00CxP_Oji3ajYtRWkHDg9gQcAiDyK1YuafSW4OLxSUxR_vwHE_A1YKxBQCA0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری جدید و پربازدید از دونالد ترامپ درحال عزیمت به زمین گلف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/123825" target="_blank">📅 23:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کابینه جنگ اسرائیل در ساعت ۲۲:۳۰ (به وقت محلی) تشکیل جلسه خواهد داد. در حال حاضر ارزیابی وضعیت در دفتر نخست‌وزیر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/123824" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
معاون سیاسی سپاه: ایران بر تنگه هرمز مسلط شده و پس از ۵۰۰ سال، به موقعیتی دست یافته که حق مسلم مردم ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/123823" target="_blank">📅 23:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: میدان و دیپلماسی دوشادوش هم آماده برای هر وضعیتی
🔴
سخنگوی ارتش: امروز دیپلماسی و میدان نزدیک‌تر و هماهنگ‌تر از هر زمانی در مسیر تحقق منافع و عزت ملی کشور می‌کوشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/123822" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI6QdrB8QuDB0MtApR_BEHLkQDq8z2B3QzTGiNAm4ETMol54CG0tR_jzZB4IxFImJSqK-E_LvZJl3g3Mm9AA0wV601cdP7mZJF8vxwHamdDBal6NFViEV4Hxcp8jH7GhTn_3W1vP0hcnQlb4OOrTAU16-oGxPRUQe4gHM79qxleLPSOjkmjDPeQaTsyV5PDMASTQKNmrkVfh1eKNjq6YHZ2-YNFGUtWZMwvpnN0qOkIVm7DR7gN-CeR-_amymTE57Z8prIXxdHGK2Ci2W3mK9mxSADhoQRvufxkZQh2v_z53lcBKw7AKCzq2bQpxivODm4JSIrLxlHY2tKIXf_eQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=PSgU-nbxbUuJCnhjDKHvt7hlaXoFD6L5QHWpgKF3Hc-v7WENyzoWTmJshTk5NWQZOD0R-REtJ8JUp5gY4N9gSQgs7mx-fMnBygcOR0zWfj0dLbKxqa4UdLRbYad7HxbhCxZHBkcAQt1AOUc43o-8zyBDhyKPrkC3zz-1t-IAWN0Kf5to711MjRoH0ndK9BD8tmiOS1L0q_Yybm2a_TxrMXVr7DbO5ExjHWW3H9g3OUGxC2MiB8jPV0dzTOQWfJmKSISoYHGGAckBTntfvAo1GrsKbuqcif8acpXV-jzSHYVpIc6u9yaTQmeDkGnAqggKODgyV0ChIgj2qHTBocLp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7752c409d.mp4?token=PSgU-nbxbUuJCnhjDKHvt7hlaXoFD6L5QHWpgKF3Hc-v7WENyzoWTmJshTk5NWQZOD0R-REtJ8JUp5gY4N9gSQgs7mx-fMnBygcOR0zWfj0dLbKxqa4UdLRbYad7HxbhCxZHBkcAQt1AOUc43o-8zyBDhyKPrkC3zz-1t-IAWN0Kf5to711MjRoH0ndK9BD8tmiOS1L0q_Yybm2a_TxrMXVr7DbO5ExjHWW3H9g3OUGxC2MiB8jPV0dzTOQWfJmKSISoYHGGAckBTntfvAo1GrsKbuqcif8acpXV-jzSHYVpIc6u9yaTQmeDkGnAqggKODgyV0ChIgj2qHTBocLp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یه مین دریایی ایرانی نزدیک سواحل عمان تو تنگه هرمز پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/123820" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
پیشرفت‌هایی در مذاکرات وجود دارد و ما این را انکار نمی‌کنیم، اما باید مراقب باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/123819" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktvMgtqnKhagdb8ZP6YfNzugM92aJIJs9vUfUAbFQiNodkqnefZHZ2DlgqbjA2EvKdNVscQyZcdPqkqqMpv4MS4VwVXhsva0EUF-4nLa0bAx-Lrk9OAD9oi9-ObPAkx0Dc4ap1Bmo4VLVA9hmSm-n_Prddu8veZLUMh_F41PqC4qS4rRKn6ncKR16PT0gKD7q2Yni37EsyT1qac1CzHH8e3XYpwXdxI-aqIFnNv4rbDR1sq1FR3dU9KgGXN4LIHVCQvjYaLCiD7PDeZFyogH3hSZmoZxANniWbeVebTWtvpMnWxnSoDmQvo9QlCDDFxlf-5QKkQ0Ieir3ZkxoFqB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
موزه ریاست جمهوری اوباما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/123818" target="_blank">📅 23:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a49146ae6.mp4?token=h_6RUURP4nuh1xgGqAo3aKCmWe_TzT73mlVCUvf21aPO6z-W3849kxykGhU3zK6WgT3V77djuVRW1SxODlwnan3Pbz9iInqidyjbruF9ch512m0t7d9t6ptL5Yk_q-_iYJGsoTb7VT8jxL-jIBgxOuVS4f8DiLZc8kUI5CibJnqL59epW8BrOOvklqGai_6CCTJbV3mMEhwntrMoBCwpQmIZYIZQ9F4n0GdiQny06GspkLr7e4bcobT7Hi5XhzxuGM5dFJslsAeX-K8tRpKzNmmiSa_4-Fw8-ih3j7TnZAg8vfFdaL8SEumC9xg46uLbUJZUEudV8NxbGpmoc3qJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام حديثه اكبرزاده ، 18 دی در فرديس كرج با شليک مستقیم گلوله به سينه‌اش آسمانی شد.
🤔
عرزشی حرام زاده این دختر ایرانی تروریست بود؟ ظلم پایدار نیست به وقتش سر عزیزان شما هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/123817" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=JRr1G305xSHpa7B1FLJykP0xkoFPuJscTddLnUlKn895MBjhFWQJb12EBrwtWBM3pVnJXXlsCylQS-PrVI6KDxR3NLqbV2g2PLP_oEzshPtQNXVE9C3Vj77JdJfVWtBEPvHAfjyGfrFpOsCA3YfriCXky9_8i7xwlggVsa1o_wvf1Xw0ap7iCfhw-8ylGBiokHDqRYIMqIhjncY_l7H_g-Uaj90sHn_rqhIXHgh_ZrR8xkKj1S4bbbaAlRnkSkc1_hBPocI8WyvIvrodPfqzWHxueynRggctyTPoNm0YoXp1-MhGdtdgCdZ-IpUs2tpqSN1T8lSYj9bLbKTf7T3phA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1e62f376.mp4?token=JRr1G305xSHpa7B1FLJykP0xkoFPuJscTddLnUlKn895MBjhFWQJb12EBrwtWBM3pVnJXXlsCylQS-PrVI6KDxR3NLqbV2g2PLP_oEzshPtQNXVE9C3Vj77JdJfVWtBEPvHAfjyGfrFpOsCA3YfriCXky9_8i7xwlggVsa1o_wvf1Xw0ap7iCfhw-8ylGBiokHDqRYIMqIhjncY_l7H_g-Uaj90sHn_rqhIXHgh_ZrR8xkKj1S4bbbaAlRnkSkc1_hBPocI8WyvIvrodPfqzWHxueynRggctyTPoNm0YoXp1-MhGdtdgCdZ-IpUs2tpqSN1T8lSYj9bLbKTf7T3phA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت ملی اسرائیل:
«باید بیروت را صاف کنیم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/123816" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: محاصره دریایی یا با زور یا با مذاکره پایان خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/123815" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
