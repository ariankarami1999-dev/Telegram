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
<img src="https://cdn4.telesco.pe/file/bdiIB1ufgds_E3tQk2lgIldjwrghyjnbu8VHMsHfO90aRfeGHMD78K1QwVAQdHyE15gIgA06awTCG08tFtHFacIggDVfS_ywEF7P_2gnhLHn2wEauSHUSxG-xGOsiXSQFJaRFliJOQLv4eyETUiPIPP-MbE3KHDsGBo6s8MpRroxOHMPO5RYSr1ZLj_aonFHwdRY6SNR02MGD8tmiSbdvgKrZsNU45rwFXAlL8-P0jEJWibaATh5U1FffdIvzVGbWHHmdYHKfvpQUOQCgiAGBjRxSHjWkEMRyokzky0bBf1sYlGj4pSHw4e-PyZ65qt4eO7QO4J-4dmzspcv5s379A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-122478">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpcJ8S5-VxhrI4UG_pmFRIniDJaPc1b_S6Ybcr2xpiLjuKp4eMd3MOOFrAd68wRFSVQ91YFIxil6WGR8DZpxKwBKu9xpUk9OIiwKtxNB0iWVdRc_o2ptMFMBybdKnQ851LQ7k70ASFjtgV4LcDo75uemTyXnszjLb73ckSGgcThrAwcmVClbEJ_FSJ_w7x4up61ch_Y9Gz1K3N5cIxQWKVgGu-f7abT3IYcNADV8Mqe5meL7k6983dVFieZxbqJiqhlPI9xl_7xifl9f2lEM9Ih82sBdjVjOxEJIk2-u-RWfBvRvxbyKgea2w2KugccHOuRnM7d_F4FrQlqD5g145w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل از کشته شدن یک سرباز در لبنان خبر داد: گروهبان نهورای لایزر، ۱۹ ساله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/alonews/122478" target="_blank">📅 10:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122477">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3a3zPk0aTLbtcrYeZmJnhaJLv1rxoZbKzDTspsQ58us5ymkt1hIgKwuWi2ffu1kEuqJJRLbHO3a0N5fw1B6346T6NRZHAPSZCJfQYSwGuBUDPCOdskG6EiD0DLD0JFEGHtxWqUxC265u86y6_yaTPTCl8J5_TVM01yNQYcaGSPhSuKyoDuxyH95yZge3O5bJEnp5-dm7kTAd2a3kPtIwPUMATTHCB3fNEFU64K2bPaPReC8ANpwouSDspNxt8NWcuPEwJcsYcjOGbqdC6U6qdLXsoiZsnOE8REjlOR40FSCeEDLbn3hf0o7zBWKd2aq9i6qExptj-bQ2HUUVp0jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:آمریکا منتظر بنزین ۶ دلاری باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/alonews/122477" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122476">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
انتخابات هیئت رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شد، دقایقی پیش پایان یافت
🔴
این انتخابات بصورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت رئیسه مجلس شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر بود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/alonews/122476" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122475">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی: فرودگاه‌های فعال کشور به عدد ۲۰ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/alonews/122475" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZZ44_rnIsdjrQMNBTRL9xzzvPj93NA32bibcSD2HcmK2M_ilBMzoQurAau_3i10vtZhtdD1Rb-x6aGOrtyiZa6N14L44URDJnFsK3waqO08jhgR4Tm1HJkI0jG7_6sGatFfBUe5yxtL4rgntHt1WVMKY8sUkS68rkHG4mrqarUA6m_1-z1Vt7dJ5Q9cTTfzW9hF9m-MqJVe98S7i31HuO_KeQd3iTwj4Q8DwceH0CGHuwvv_knD_P8wGaKodDLUR55BYOpHJ7NsQKU3eDKfX0s8Ue6-zzD55TIlX8rALilhTVn-ASR6oH4EHdCI5iobybXaPYcx_ZdOXmBfR65Gqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6uZMHNoccHDiEl7FDNjE0xYfEj7rGMAy4A-3Crbm9GdbtYZ3w4RjKp4-KT65mDYF5nxDLb11u2j0g1ylw_3Mh9wS1ozz4N5w6u7QwJf_1zhAPDlj-gwNagwKtZmz4GE-PHvjcVnXIk1lW6s_wLnuwqBTWsvajoJuBq9ZteHWbS661Z_HDhogrnsi83F3TVQ3A6xVhqDQ5RTVimUZailWG_xg0kwY89awXQtep87888oZY7_5l7atocL3wjnPm6qyCLdORminWyuEQ9q4sPXFo-17qkPXfEu-Q9ck8txpZa-XBzIv2xU8xUEehf9lhW728jQYCI0CCZebdeVaA6ehA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قاضی صلواتی با رد حکم دیوان عالی در پرونده کشته شدن بسیجی آرمان علی‌وردی در سال ۱۴۰۱، گفت بخشش نیاز نیست و حکم اعدام ۴متهم را صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/alonews/122473" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت امور خارجه چین: جنگ ایران هرگز نباید اتفاق می‌افتاد و نیازی به ادامه آن نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/alonews/122472" target="_blank">📅 10:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گزینه‌های نظامی ترامپ برای شکستن بن‌بست با ایران پرخطر، محدود و در نهایت ممکن است به نفع تهران باشد، که طبق گزارش فایننشال تایمز، نقل شده توسط ایران نو، چهل روز بمباران را بدون عقب‌نشینی تحمل کرده و از آن زمان تنها موضع خود را سخت‌تر کرده است.
🔴
از حملات هوایی تا عملیات دریایی، راه آسانی برای مجبور کردن ایران به عقب‌نشینی وجود ندارد و حملات جدید خطر کشاندن واشنگتن به باتلاقی پرهزینه را به همراه دارد.
🔴
ایران از روش‌های جنگی آمریکایی‌ها آموخته، در حال بازسازی دفاع هوایی آسیب‌دیده خود است و ممکن است از چین و روسیه سلاح دریافت کرده باشد؛ می‌تواند با پهپادهای انتحاری به نیروهای آمریکایی در هر دور جدید درگیری حمله کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/alonews/122471" target="_blank">📅 10:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجارهای کنترل‌‎شده در محدوده شاهین‌شهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/alonews/122470" target="_blank">📅 09:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مرندی: نه به توافق با ترامپ امیدوار باشید، نه نگران عدم توافق باشید، به مذاکره‌کنندگان فرصت دهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122469" target="_blank">📅 09:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
انتخابات هیئت رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شد، دقایقی پیش پایان یافت
🔴
این انتخابات بصورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت رئیسه مجلس شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/122468" target="_blank">📅 09:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مارک لوین: ترامپ اعتقاد دارد که رژیم ایران را کاملا عوض کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/122467" target="_blank">📅 09:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عباس اکبری، یکی دیگر از معترضان بازداشت شده در دی ماه، امروز صبح اعدام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/122466" target="_blank">📅 09:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش اسرائیل: به ساکنان ۱۰ شهر در منطقه نبطیه، جنوب لبنان، هشدار تخلیه فوری داده شد
🔴
اخطار شامل شهرک های نبطیه الطحطه، لویزه، سجد، عین قنا، حروف، کفارمان و زبدین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/122465" target="_blank">📅 09:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ارتش اسرائیل: یک هدف هوایی که از لبنان به سمت عرب العرمشه در جلیله شلیک شده بود، شناسایی، ارتباط قطع و حادثه پایان یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/122464" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فایننشال تایمز: عصبانیت رئیس‌جمهور چین از «افزایش توان نظامی ژاپن» در حضور همتای آمریکایی‌اش
🔴
پاسخ ترامپ: ژاپن به دلیل تهدیدات کره شمالی، به دفاع قوی‌تری نیاز دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122463" target="_blank">📅 09:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUGtK5tMr829jruQqF4pUJWybSQWApfgeMeqcgpSIA2fcCRWmoCzPz4DRbfjM0OMDhXyX9smW2gKv0lf81BaRJq2Ky8rkjLvwmLQ_rJee7y3YpcTKzXy3M9d-yQRYpurFrli3d4cL_DmN01KDNAp050gvo5XMl-ML7KNcwOaYYkGnWT2BmZw1BQi_ooQKQVl1Y0DJoTKcSirv5Qx51cejQqta4B28d5Jp3fhMOl0ljFI8h_abuOwxBH3wF_-p6INoKuE7mAv2uB4SE8kXz-H9FEyhO2V4t0ZRpUPEA6veYguhoyNL4q9ZwAK0XAdJe2XbiZMuDgtnT68K7Raqi1MWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی
:
تماسِ نتانیاهو با ترامپ کافی بود تا سیاستِ جدید آمریکا به «بدون گرد و غبار (خروجِ ۴۰۰کیلوگرم‌ اورانیوم)، بدونِ دلار (مُنتفی‌شدنِ آزادسازی اموال بلوکه شده ایران)» _No Dust, No Dollars_ بازگردد!
🔴
آمریکا تصمیم گرفته دلاری از اموال بلوکه شده کشور را تا به «خواسته‌هایِ هسته ای آمریکا» تَن ندهیم، آزاد نکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122462" target="_blank">📅 09:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: رشد شاخص سهام در ژاپن در پی توافق احتمالی میان ایران و آمریکا، برای اولین بار از آستانه ۶۵ هزار واحد عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122461" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مدودف: اوکراین عامدانه به دنبال به راه انداختن حمله گسترده به اهدافی در کی‌یف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122460" target="_blank">📅 08:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4cgtxOuh_Bav05Q-o88uiN_zhH31r8DCNS6G8Bvjy6IZb7KgiH91ksHblpuAI-mhzQep4U6yz9YD3-cNcvnGMNYteFxOA0e8eIWp44W06JgdvLKT5m-Z_OIkHjY8EK_V3wIdH3XnBXCDedlwauUl1WcdZzz3Wwul1zLUGtLaR_VxB6nnAaq_aSZFFUxlO2p4k3KEpqm_H-B61zrxaN0WFgrQSvhfVwyUDDxAb8mLsB0wvQjccxCPYHxDmdfoSp0NDTtWfDI5zs4-2sUR6lEzTsT3ZGQKpqKAh-jjKFgumwrAwWVoG8YvAILCychSNSBV_ImRcNV7wd9mxMq5I7j1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: گزارش‌ها حاکی از آن است که عربستان سعودی از دونالد ترامپ درخواست کرده است هرگونه حمله جدید به ایران را تا پس از حج به تعویق بیندازد.
🔴
همچنان ترس وجود دارد که اگر درگیری دوباره آغاز شود، زائران در آنجا گیر خواهند افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122459" target="_blank">📅 08:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89b8e994e.mp4?token=BIrzxA_lr2sVYrAfe0JJUujCABUvRJ7MJPNvWYD4wHGVpecAhEyZH331-dFgoRpjLFGIYm9ZSjtN7CAaNW72eLSITKl1OaHT_gEIUdoFZuX_Iw8VsZWuMPkdUGqzoqElEWBLd_qYgIhJCsB4-skFjq-I5A9U9Ie2VMhQljkzNNOoDTq3Nh6zTirUJmA3N6CHcuXGzd9ER3OtNTHWpfJnVTC6lZ_vGg54F5X4BIkYl03hYcjFvImPwBQ7Ea0ANcaM3LvUsicIn-eVPQAvbHHcaRFVFII3VJxsHjgPcZT457LJT5MmbdMb507CxiDNN9wGf6NFpqJWRQ8Jh89AEpNyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89b8e994e.mp4?token=BIrzxA_lr2sVYrAfe0JJUujCABUvRJ7MJPNvWYD4wHGVpecAhEyZH331-dFgoRpjLFGIYm9ZSjtN7CAaNW72eLSITKl1OaHT_gEIUdoFZuX_Iw8VsZWuMPkdUGqzoqElEWBLd_qYgIhJCsB4-skFjq-I5A9U9Ie2VMhQljkzNNOoDTq3Nh6zTirUJmA3N6CHcuXGzd9ER3OtNTHWpfJnVTC6lZ_vGg54F5X4BIkYl03hYcjFvImPwBQ7Ea0ANcaM3LvUsicIn-eVPQAvbHHcaRFVFII3VJxsHjgPcZT457LJT5MmbdMb507CxiDNN9wGf6NFpqJWRQ8Jh89AEpNyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو
:
باید به یک توافق خوب برسیم در غیر این صورت مجبور می‌شویم به شکل دیگری با ایران برخورد کنیم/ ما ترجیح می‌دهیم که توافق خوبی داشته باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122458" target="_blank">📅 08:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز مدعی شد: دو کشتی حامل نفت و گاز طبیعی، تنگه هرمز را به مقصد پاکستان و چین از طریق مسیری که ایران به کشتی‌ها دستور داده بود، ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/122457" target="_blank">📅 08:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ادعای روبیو، وزیر خارجه آمریکا: امضای توافق با ایران روز دوشنبه همچنان امکان‌پذیر است
🔴
پیش از اینکه گزینه‌های جایگزین را بررسی کنیم، هر فرصتی را به دیپلماسی خواهیم داد.
🔴
احتمال قوی برای ورود به مذاکرات زمان‌دار درباره پرونده هسته‌ای ایران وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122456" target="_blank">📅 08:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmWkEOxYNPNu2rFtIpJKB-dlW_Plr1U4hgTrQeZyv6VdhMMo2a8_768K5AK29_iVF7Mi8dxPCmovWcqf04g8fsELPOYwqA0vSO_T7nwT-sUVrDR16IxlSoablUfh-yLo-JpbbPMnagMOwANyrAxIBLK_I75w_8gmnL9aZKL0TZNsIAQOZgDZqZmDSVrT9v3rVNijx_IWbEswyxYJ68jnhXa5bnx2yPwNnPt2QwrCJj1QWKvWcdg0EAAvxiKodI6HHWzOAkDpU4TvlETgQ4ZWzQNEai6y-mda4khClXNfpNKQe1EdzTLwznftFFviBZ1l95NNsIR7WNFBPswbWtyhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ رئیس کمیسیون امنیت ملی به تهدید اتمی ترامپ: قابلی نداشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122455" target="_blank">📅 08:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هم اکنون هر بشکه نفت برنت 99$
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/122454" target="_blank">📅 01:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1GkbcPuMcbci7mCbmZlntHoP8Sx_i2kOra49h9bpmOTxQPVTFopdMS0xDyAYJlghFSc4KRtsPmtQKBakMstP6953xbeJudb3Unn6fRszyPbLUJLHxUg-gz5i8D61aFcev27_27pkUCTyqF1zR0yDPRoZ8V6SYvw49LhOBdIolRi8Gk6acbA9DCkd-WWzn09A-_ymSSl8V1iwEvzY8_LaXVZUx1k68Nb-qcE2O1785YjTtvrEukuKHxALpg5FvERHR5HTYKCX0y_Z6k76ByYMVpODEMML7G9l-jWXssu8Mwv_rhX2ORd7hiRvb0inHp2MT6miSONsCzhqfgG900Rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: قیمت نفت در آغاز هفته جاری در بحبوحه امیدها به توافق بین آمریکا و ایران، 3 درصد کاهش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/122453" target="_blank">📅 01:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntT1-8vCe8HXCdZnZ26dfnVfrkav7PpoqJ6KCA_IvHB6d2C0mc47Ov38uKjNuMNFAT-108BrxQyk4FWfCw6WPrQLXdW1tKRyC196A3zJCZUigM8B3nMRVWTURmmaNYh8-RWMG_fVilVXXhQf9zmcS74_Y0iMzmqrdg5dfbDPBPDcLDa7mL893q2p987z4OdT38nH8Ur0RMUW-r4tmPx1nyAehGsxoD6JE-6Gh-xBnlMuaVrD0NbBF17qPtagrXpnKpQgr-ewc0uNH0zbs8PKIyEeHpq9he0sFSY2Xja4dhG_EicBcEsZtjDkxGfaF0lp1r6cnnOk_C1OTigGdWUQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکنون یک هواپیمای هواشناسی و کنترل هوایی (AWACS) بوئینگ E-3 سنتری نیروی هوایی ایالات متحده نیز بر فراز خلیج فارس در حال عملیات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/122452" target="_blank">📅 01:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122451" target="_blank">📅 01:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: آمریکا و ایران به توافق اولیه برای بازگشایی تنگه هرمز دست یافته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/122450" target="_blank">📅 01:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نشریه آمریکایی پانچ بول نیوز:
کاخ سفید از قانونگذاران جمهوری‌خواه خواسته بود که آخر هفته جاری در حمایت از توافق با ایران توییت کنند.
🔴
به گفته دستیار ارشد یک نماینده جمهوری‌خواه، برخی این کار را کردند، اما برخی دیگر «از این هراس دارند» که پس از پایان تعطیلات مجلس، مجبور شوند از این توافق دفاع کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/122449" target="_blank">📅 01:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/alonews/122448" target="_blank">📅 00:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی‌های کاملا دقیق و حرفه‌ای نوستراداموس زمانه؛ استاد خوش‌چشم تحلیلگر صدا و سیما.
🔴
فقط اینطوری کار می‌کنه که هر چی گفت، باید برعکسش کنی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/122447" target="_blank">📅 00:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyzpw32t_GGuPBZ_r88TjoSwv17wHAFwgKnTLplfvKf_AGJZchizzr-0iVuFvUOsmpk5yZviLujrZhHOM_q5cBUUXaRoLXvTP4O9mRXqp0oNaqRccMEmg98P9VGI6gnK3gL1cu1IVQzSqYinqmzrdnpyse-AZsXP06HsC3kx7Jg_T6l_T_5yVD35Zjb0GrphvYArUXryrCXAJmsybvwveSIZRetSQYBA-fnLAUPLZYWZrmWIOP9MUkbAGKvwrDSM8nzNUboITAg9sF2hUr9uY3dwQEVV2mBvKpzZgVYIFbD3HAxnCC1ItL5n3e1-xWTSt24DEBYhBRZ8ccrvKNt8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی : دست روی ماشه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/122446" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال۱۲عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/122445" target="_blank">📅 00:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع مطلع: تا این لحظه تفاهم نهایی حاصل نشده است و چالش در بعضی بندها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/122444" target="_blank">📅 00:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqDXq7nErn2CnoysBPYDFYCuaVaAHzJFyeuBa_L0iB46jVFWcxn8V591IEWWPKqSCT67JA8c8-ISuBkuD5esynrk0ge0BjiUbfsjapdoqw6XAtsDRadGTuqEfA_fTdW5tyoyzq19BgAwY2XIhSk_ZBsOEciwYWIHrvqCT8ROvvu0s0e55ro092Hl9nf7v0L5NZLs930pHSAnSgbw9nDRtfqHLeOFDvS423WzWIUH-msoUgp82DkJtGtmUnh-rOATivWv6akLYma3vq-yKvO9JFIUGmvkO2BslvAk9ModIwp5EAwHyY7Kf9DCIamqR_KF7ajvNy8OuORbUXXwYT1Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییتِ سخنگوی فارسی زبان ارتش اسرائیل
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/122443" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
همزمان با سفر رسمی نخست وزیر پاکستان به چین، دو کشور تفاهم نامه‌های همکاری به ارزش هفت میلیارد دلار امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/122442" target="_blank">📅 00:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر در تماسی با وزیر خارجه عربستان، درباره تلاشهای میانجیگرانه پاکستان گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/122441" target="_blank">📅 23:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/122440" target="_blank">📅 23:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/alonews/122439" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه «فاکس‌نیوز» گفت دونالد ترامپ، رئیس‌جمهوری آمریکا ممکن است به ایران هفت روز مهلت دهد تا به یک توافق «قابل‌قبول» برسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/122438" target="_blank">📅 23:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیویورک‌پست: احتمال رسیدن به توافق بین ایالات متحده و ایران به طور فزاینده‌ای کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/122437" target="_blank">📅 23:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به طور خصوصی اذعان می‌کند که اسرائیل در حال حاضر توانایی محدودی برای تأثیرگذاری بر رئیس‌جمهور ترامپ دارد و فشار آوردن به رئیس‌جمهور آمریکا دشوار شده است، طبق گزارش کانال ۱۳ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/122436" target="_blank">📅 23:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سردار نقدی: اسرائیل و آمریکا ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/122435" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
واکنش پسر ترامپ به منتقدان توافق با ایران:
🔴
ما باید افرادی که فقط با حمله زمینی به ایران خوشحال می‌شوند را نادیده بگیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/122434" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92bc8959c.mp4?token=uzyQzNeLQqRf1ptv3a4_xoKJkfnuxBgXv8sWEtpnCTLiOcDAfglo-aJo7WskEByfI86w06Pq9NzCPK_h0tDbRjQ9vKCe35MRJ3DdImmuNuAjQFDs3Jd62rXqyqum8nVQXWLl46qCPH6VFtL829f3ZDU_eFdwQ-K0wJsQjhewXMlPA4XFYl2NVtcqdVE1MOC3YlCKOZP6kUoMdiW39rT91y0so4WfDGLL438sQxlHkbQ7tC4HW5-jrei03L4Zle8k84uYTwMgIZAlVO720lt8OelNSqGS_A_v5LxCGw1u2WgytHSOEli2dMi-4NAbFfZyuqiVnkkslOdWYS2rF6G6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92bc8959c.mp4?token=uzyQzNeLQqRf1ptv3a4_xoKJkfnuxBgXv8sWEtpnCTLiOcDAfglo-aJo7WskEByfI86w06Pq9NzCPK_h0tDbRjQ9vKCe35MRJ3DdImmuNuAjQFDs3Jd62rXqyqum8nVQXWLl46qCPH6VFtL829f3ZDU_eFdwQ-K0wJsQjhewXMlPA4XFYl2NVtcqdVE1MOC3YlCKOZP6kUoMdiW39rT91y0so4WfDGLL438sQxlHkbQ7tC4HW5-jrei03L4Zle8k84uYTwMgIZAlVO720lt8OelNSqGS_A_v5LxCGw1u2WgytHSOEli2dMi-4NAbFfZyuqiVnkkslOdWYS2rF6G6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زنده یاد مانوک خدابخشیان:
خدمت دوستانی که پنیک کردن از مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/122433" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس با تاکید بر اینکه اداره تنگه هرمز به وضعیت قبل از جنگ باز نخواهد گشت، تصریح کرد که  این تنگه تحت مدیریت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122432" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوووووری /  پست جدید ترامپ!!!!!!!!!!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/122431" target="_blank">📅 23:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9UpdoqPgnLIAwJbmm2vThKpvgr6fI9TTW7X3PMO3X2fC4zPMUnBs7shcnzUMv0LRCQW7AnDOVExs9OgB1cHob5OByPGDgbP98nrQtxLPA_auOQpT1Uj7M3iGBGi3t9AKdL5TiNikQYXDihlHSGmSOQLGkGL4NBNKdODU1reSxwIRM2xIjNiKPOl9Pbc9u3XpEtzf_UWlUEiBZAllNi7iUwQtzzk9IqRT6SCmPkQtyslXbkHnEe7cF5WB78hDfA-9MWJKd7dQhXiOTlk2H4vlLs5PRf-unQfJBJgQPxljHEV_89plXxb6zvXf45k1zcJ7P0P_vabgOjtT1ZfQ-HoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری /  پست جدید ترامپ!!!!!!!!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/122429" target="_blank">📅 23:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/en_gyFWDg0a2r3u2lfaaJs-sOJfeiVizHc0zY8950C0H_AXuDceJkBO3jI8RVfb19QB1Ur6uau1tEpzeqWGpVvrxWYtLuuL6EqMh9FWIBj6xcvUNxVZwXRf_sApTAX-A9W_5V-d0nNwtegeLDoFj_L5bjAu5kqQQJC8eez3gWdsAvO4qggydDfDlfjtq3xLBKRx06DT3JNL8R8w9mgNSTydqyaqtVXq3aY6m7AED34PAmlSIMiTMUhTaAPn_BK2Ppqgu-DX18KdKsvyNLWvCrd2mXsY96r9I-hMKM9gFvwWX5AxTfJd1PSPp3YEZBCUh_1huJpyKUgSYgw6fbBYCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییتِ سخنگوی فارسی زبان ارتش اسرائیل و طعنه به ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/122428" target="_blank">📅 23:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=ekzgLgOjkxreIugv3N7EtAMryb9iUqSj5ICkKDe2qi9i4cmfbtAfjfY-UIiwT1T5AOqL6DxA19BcxotsZ2F1hPTIaEmC2BCUakHhF1oG5BUAG71AaSTv2MsoXn-qNzTh8cQ4YVzsO7Sjk9hQ9n9DNjFAKcPIjYUVW2PGFbn9Bnf6wGLzJck6jNnzOuAVLJtF_JqHTXtzExjALss3zu4rj9V4DRvFLoFyCcOAsH7O_kkhsmsTzWm29cZ99mbsfWSQU5_M7bANd8P1Z_swI13DUB-P_Rt2-bicWe_AT8bgaJ8hqs8xo1U1Xpn0EalnFq_erc4BX3ziNbyuidgvKAliFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=ekzgLgOjkxreIugv3N7EtAMryb9iUqSj5ICkKDe2qi9i4cmfbtAfjfY-UIiwT1T5AOqL6DxA19BcxotsZ2F1hPTIaEmC2BCUakHhF1oG5BUAG71AaSTv2MsoXn-qNzTh8cQ4YVzsO7Sjk9hQ9n9DNjFAKcPIjYUVW2PGFbn9Bnf6wGLzJck6jNnzOuAVLJtF_JqHTXtzExjALss3zu4rj9V4DRvFLoFyCcOAsH7O_kkhsmsTzWm29cZ99mbsfWSQU5_M7bANd8P1Z_swI13DUB-P_Rt2-bicWe_AT8bgaJ8hqs8xo1U1Xpn0EalnFq_erc4BX3ziNbyuidgvKAliFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این ویدیوی کوتاه که توسط حکومت جمهوری اسلامی و برای ایجاد رعب و وحشت تولید و منتشر شده است، بخشی از روایت ۳ دقیقه و ۴۶ ثانیه‌ای بازجو خبرنگار،«محمد نگینی‌پور» است.
🔴
این حجم از کانتینرهایی که گوینده ویدیو هم به زیاد بودن آن اذعان دارد حامل پیکر عزیزان کشته شده در اعتراضات اخیر و سندی واضح برای محاکمه عاملان و آمران این جنایت علیه بشریت است. صدا و سیما هر تولیدی که در رابطه با کشتار مردم دارد سندی روشن از قتل‌ عام شهروندان بی سلاح توسط حکومت است و باید ثبت و نگهداری و مستند شود.
🔴
تاریخ انتشار این ویدیو در صفحه شخصی شبکه اجتماعی این بازجو خبرنگار ۲۴ دی ۱۴۰۴ است ولی ویدیو روز ۲۰ دی ضبط شده است.
🔴
محمد نگینی‌پور، مستندساز است که پیشتر در رسانه‌های وابسته به سپاه پاسداران از جمله خبرگزاری های فارس، تسنیم و مهر و شبکه افق صداو سیمای حکومتی فعالیت داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122427" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1VbO7-cPQRLluTtSIt0CI7344GaIZjqRQpaCGI_4hwhpt-L91NMSMt9hv97Fb-rnjKRsoRRr_EU1JOM-1Ui3UDDNfgFRd4kzSs_eN317nNM-YVg8goc-sNgDZ3c9ViwOij9OPgEF7T9-SDrgsgvHpEO6TP46dOpYuhIzLTpZ4VZS61n0EopGkiV7I7CcgEQGXf3ruyFYjl2RcquTn_DUBvVq77NI_652Mla40eUOQzo-3i8Pq55rpTd7lI-w78IjZgO7eqFBkkAkE7wVkYYpVCxqpBLWlT1Beu_d3XpJyve-XXfxxI-WEXPfN5CB9e0p0H-tuFLjTI6owiqZFAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش دیوید ونس، پادکستر و تحلیلگر مشهور آمریکایی به خبر احتمال توافق ایران و آمریکا:
🔴
ایران ۱ - ۰ آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/122426" target="_blank">📅 23:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به شبکه فاکس نیوز گفت که هیچ توافقی «امروز یا فردا» امضا نخواهد شد و افزود که رئیس‌جمهور ترامپ تمایل دارد به فرآیند چند روز دیگر برای رسیدن به نتیجه نهایی بدهد.
🔴
این مقام گفت که رویکرد دولت توسط سیاست «بدون گرد و غبار، بدون دلار» هدایت می‌شود، به این معنی که ایران بدون برآوردن کامل تعهدات خود، از تخفیف تحریم‌ها یا منافع مالی بهره‌مند نخواهد شد.
🔴
تفاهماتی در مورد انبار اورانیوم غنی‌شده و بازگشایی تنگه هرمز حاصل شده است، در حالی که نگارش نهایی همچنان در حال مذاکره است.
🔴
آمریکا آماده است تا در صورت شکست مذاکرات یا تولید آنچه آن را «توافق بد» می‌داند، حملات نظامی را از سر گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122425" target="_blank">📅 23:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آی ۲۴ نیوز: مقامات آمریکایی می‌گویند ایران تا زمانی که انتقال ذخایر اورانیوم غنی‌شده خود را آغاز نکند، هیچ‌گونه تسهیلاتی در زمینه تحریم‌ها یا آزادسازی وجوه مسدود شده دریافت نخواهد کرد.
🔴
در عین حال، ایران بر این باور است که آزادسازی وجوه باید بخشی از هر توافق‌نامه چارچوبی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/122424" target="_blank">📅 23:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvY5wNEDYDPsXOrKJ0OBJrjwwMNC9HJDLtI_Xi5E1AAMurVC-NVlRXQUNLOpkvPqjgTL6XXVR75MAbm4q_L015JEgpaeWO9NKyVgr1EnbqUJFFNvRCEc1pkzSXuq929ij8PmTa4LwVVP71AsmsCEFSFcVn7OlOIzRuCDbGqlA-fTzHiwrtBqaFzYdH3Ly96i_TEW-Mi4FiWZ0St7cFoOEGpkm1TCN1AVRWg3Tbc6JoD-qjog4QaCfKffj7r3WSY7g9JavnS2FSPjt--MbbgeBifWdiQ3B3_110LodrCDadOpBCECV2jNl23qsoKeAJ9o56y92ztwUgq543mP6ME-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشتی HMS Lyme Bay در حال بارگیری مهمات، تدارکات و پهپادهای دریایی شکار مین در جبل‌الطارق مشاهده شد، در حالی که در مسیر حرکت به سمت منطقه تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/122423" target="_blank">📅 23:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFZWXtH_SAPp4FMHGzvn4onyMO6i7uSa0trwPPw93zkkncyzXm7N0AeH69_xfO18gbzIm2e7xmbI6ketuL_qfawbkmBqCMcZ0Bi3IG97euO1qlAv7cZyj2pIjQhhD7W0S14DWOVtGDk9YmR3ifNp_GEgCCMzQanqtjnHdT34JGMPF_Acn3c0kEMg_Ve4MhJ4dak92jYNGsFXXJO0OevzHCtaPbA9w1pEd6e1aYLKMyRcnn6G-NYI4tRQLJLfva73MA9NVNXfnfCKwWoHv2wtHRuL0PtxjhasE5BTXI_KYhoh32C1kqfIbixrV5tqNjNRWNyREcmpF8Ul_r83MEBPoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122422" target="_blank">📅 23:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر خارجه عمان: گفت‌و‌گو‌های خوبی با غریب‌آبادی داشتیم
🔴
همچنان به حمایت از تلاش‌ها برای کاهش تنش، پیشبرد همزیستی مسالمت‌آمیز منطقه‌ای، امنیت و آزادی کشتیرانی ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/122421" target="_blank">📅 22:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_PMKnKeDNGUnFOqFUoTObfF8bfWRIngzniYxJ8_iwO_8PW49T4amTkp8Bf1968VDvpc25rhjNQHmPfQEOxSNY0JzMxjVv1tyCIyvhrqeveaUSHc8_dv2rhGIi7TMWMEOy7dhEUzLVEBY1yGVJATdHgbEBvZHXFOyNoBvh5M1t5GtpuvI8XcjYz4ecKiZr6L-xFGVnjhaKoxhCjrGSZatI1g0WiCdsLhZcEEIuPX0j5X13D5gkYxzUKsaE7WaCI4Zuumv7pGQacoGbPDt7dxBpPFen9IBXLREl6n7NaekR9y810p-T6wLX8tkhlDObbRuYbNSyKo7dZlZdRV9k2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای بلومبرگ: با ادامه مذاکرات، ابرنفتکش حامل نفت خام عراق از خلیج فارس خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/122420" target="_blank">📅 22:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPQ-EncS6KVNBLdxEevGFiXBuVye1IGL0LRjhgnGYMZOdfK93BNHfAgRR3Q4SLnwPFafO7SqSHD_rHnkGjx3rAsn_ov6_lc_I-g8q0pCyjPgLPl5jJrrFOudQsAEdXv-HPEeDxkMl60WhZKpxh01mQp-D_Xpq3bPitTztkC4tIOGkSc1qu1ljb650xGss912kVl8PMkPGr_Y1cL1YkLfrIVcT1Kw32DE3QNd3tNhyT1TH1OOVLpaenHSoFjZRtkuD9eUMYeJmKzEJYTU6bqZZSsuvDVkvqZaKzzj5o2wyuOxZ84zwDXr2YfcVL9QvwBjW58btA8AWX4WLqn0dQb6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ جونیور در اکس نوشت:
این یک پیروزی بزرگ برای آمریکاست. ما باید افرادی که فقط با حمله زمینی به ایران خوشحال می‌شوند را نادیده بگیریم.
🔴
پدر من قول داده بود که جلوی دستیابی ایران به سلاح هسته‌ای را بگیرد و این دقیقاً همان چیزی است که او به آن دست می‌یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/122419" target="_blank">📅 22:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اکسیوس: ترامپ از چندین رهبر مسلمان و عرب خواست تا در صورت پایان یافتن جنگ ایران با یک توافق، به توافقنامه‌های ابراهیم با اسرائیل بپیوندند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122418" target="_blank">📅 22:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روبیو: ایالات متحده کاملاً از تلاش‌های دولت مشروع لبنان برای بازسازی، بهبود و ثبات حمایت می‌کند.
🔴
اقدامات اخیر حزب‌الله یک کمپین عمدی برای بی‌ثبات کردن لبنان و حفظ نفوذ خود به قیمت جان مردم لبنان است.
🔴
حزب‌الله در تلاش است لبنان را دوباره به هرج و مرج و ویرانی بکشاند.
🔴
ایالات متحده قاطعانه در کنار دولت لبنان می‌ایستد تا اقتدار خود را بازیابد و آینده‌ای بهتر برای مردمش بسازد.
🔴
دوران گروگان‌گیری کشورها توسط گروه‌های تروریستی به پایان خود نزدیک می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/122417" target="_blank">📅 22:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f10d05.mp4?token=p5uT9vtnaW1cvwJrmm2FCkiI9p_CieFXXfgFn0wAMJRusRUmOxbDgwlftJ8QVypdiS3KCL4lFX9gktrvQCCou9cfs-DgC2oFQTdsKnCs89ZRZoyBMFbudRjMh6kmjmElXQE5lP_qqkfVMZq10oiMI6pCjj85xhZlvbDVSGrAjIFDon90idNIMPo354tJZMgePWOYCwFwbllXY-M0r7U72yfjE8dXXZwYFi_T_zrGG-WbcVWcWr9bOr0fImVmHs2Hw2qNRcBonrOd_G3tablMv82zd85LvpZriACsnfYwh49B5J7hyLxUkv8FWih5UujxEGjs1LXro4u80wLDjLhpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f10d05.mp4?token=p5uT9vtnaW1cvwJrmm2FCkiI9p_CieFXXfgFn0wAMJRusRUmOxbDgwlftJ8QVypdiS3KCL4lFX9gktrvQCCou9cfs-DgC2oFQTdsKnCs89ZRZoyBMFbudRjMh6kmjmElXQE5lP_qqkfVMZq10oiMI6pCjj85xhZlvbDVSGrAjIFDon90idNIMPo354tJZMgePWOYCwFwbllXY-M0r7U72yfjE8dXXZwYFi_T_zrGG-WbcVWcWr9bOr0fImVmHs2Hw2qNRcBonrOd_G3tablMv82zd85LvpZriACsnfYwh49B5J7hyLxUkv8FWih5UujxEGjs1LXro4u80wLDjLhpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سوم خرداد، سالروزِ آزادی خرمشهر
🔴
نقطه ای که میتونست جنگ تموم بشه و جان یک میلیون انسان حفظ بشه ولی با طمع، هزاران نفر کشتند و آواره و شیمیایی کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/122416" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام ارشد دولت آمریکا به سی‌ان‌ان ادعا کرد که توافق بین آمریکا و ایران هنوز کامل نشده است، اگرچه گفته می‌شود مذاکرات تقریباً «۹۵ درصد پیشرفت» داشته و دو طرف هنوز بر سر بخش‌هایی از عبارت‌بندی و متن نهایی اختلاف دارند.
🔴
این مقام ارشد دولتی گفت هدف بلندمدت آمریکا همچنان جلوگیری از دستیابی ایران به سلاح هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122415" target="_blank">📅 22:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122414" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0235b6f6f6.mp4?token=EpEMgMvIhHX4N775FmaRL_8wsQqsTANEU8JkKPgh7R6I8ZLwa3E0rY0-b8JMF5nxoyW26bO0Dx7196p97tk3oiZbDfujQa3CRe1jRaAFfzZZVN5B2fg_tHOZwoJJyFEgUvq3C7ZAgW2z9Yv50_pJhxR_CcLi8DjCIoGyPZ1-76Cb_F5do8MOFvvLzz-rnPNudwtZ5mrZJascXoaG42QCdXOhnERd04XCjEogHmD1CAVGJzkecczfUm0Ac_sU4wftSZyKCxaPx5TST2wYTiigqZjG1OxZG94pD4rOJQu8h1Zhn1V9ltL0uAzpdncCGgzmXyxE_WElLOaHHYdoJW_0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون هماهنگ کننده‌ی فرمانده‌ی ارتش : نمیدونم توافق چی هست، سر چی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/122413" target="_blank">📅 22:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
منبع آمریکایی به الحدث درباره لبنان: توافق آمریکا و ایران شامل همان بندهای ۱۵ مه مربوط به آتش‌بس است.
🔴
پیش‌نویس توافق آمریکا و ایران شامل تعهد به پایان دادن به خصومت‌ها در لبنان است.
🔴
اسرائیل به واشنگتن اعلام کرده که هر توافقی با تهران باید آزادی عمل آن را در لبنان تضمین کند.
🔴
پیش‌نویس توافق بین واشنگتن و تهران شامل خلع سلاح «حزب‌الله» در لبنان نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122412" target="_blank">📅 22:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ادعای منبع آمریکایی به الحدث: مخالفت‌های درونی در حزب جمهوری‌خواه با برخی بندهای توافق با ایران، اعلام رسمی آمریکا را به تأخیر انداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122411" target="_blank">📅 22:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر امور خارجه ایالات متحده مارکو روبیو گفت که توافق احتمالی با ایران حمایت منطقه‌ای دریافت کرده است، اما هشدار داد که یک توافق هسته‌ای نمی‌تواند «در ۷۲ ساعت روی پشت یک دستمال کاغذی» به دست آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/122410" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: محاصره دریایی بنادر ایران امروز با سرعت بیشتری ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/122409" target="_blank">📅 21:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مانند معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری واضح و باز به سمت سلاح هسته‌ای داد. معامله ما دقیقاً برعکس است، اما هنوز کسی آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره هم نشده است.
🔴
پس به بازنده‌هایی که از چیزی که هیچ نمی‌دانند انتقاد می‌کنند، گوش ندهید. برخلاف کسانی که قبل از من بودند و باید این مشکل را سال‌ها پیش حل می‌کردند، من معامله‌های بد انجام نمی‌دهم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122408" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نیویورک تایمز: یک مقام آمریکایی می‌گوید ایالات متحده و ایران در اصول برای بازگشایی تنگه هرمز توافق کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/122407" target="_blank">📅 21:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c8f1a7b.mp4?token=av9QjLaizKB5XfojyOsqMvUnCGVFcqRUPbMHxdKlIvCK4sO71NM9tbUCmnpGQ5pfhGWEryaoeYLJC7KJtU21Mr2MegnGr33Or3LP1akO30mx-eYfYXkpUPDFRj4nc1oZP6roCAtE4G2FuTmfvtTN50UKPLqIsmaF8XvJOLa1Lvm9vSCrxUqkS8_xDW-QAcukvpu2ylcuBgI9HEB9OT_YEanxAjsceLsOMDGXosjgruYnKu0Y37zUmEtV44inxWUrpRXX-Wxp8UVnw6xzL6TfI3OZKR0E0Bg6mGPVYeYj9jcPM8s2GI8ilgdChgoQC_kFA9PJV60ua_06QDcDFxotbSWxLSdQ0oGgcWEKcAjMzkaxezX2BMvyWnwmKyM_-McVLqLZ22fNqkqufoDDLZD1WF0QsVqerZYv6A-2kL-HX8GfdVhJ3VXDP6Rm0psNWQ7KZ0vFAEUl_mq1opk8NwkW4fsY0nolQJ52_SD5W8NZam1fuBxZkqrHAHlTi3dLsccEdGLlNCzjxQPkO6YR1stSs8n_zw7e-dVoHNkTgZydgVKsDWtnaoqqaPh367Sd8lzEyk2yeitktOc3CXjqCjLxmMry9FOCEqXRxo7TXUyx2_igSKsM_LCj6ymvdyYVv3_PGOnY2JXZlemtJHfRL7qSTxIVx2z6YLgamDwESRKK1mM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:هند می‌تواند ۱۰۰٪ به من و کشورمان اعتماد کند.
🔴
اگر به کمک نیاز دارند، می‌دانند به کجا تماس بگیرند — همین‌جا تماس می‌گیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122406" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
العربی الجديد: تلفات انفجار انتحاری در قطار در ایالت بلوچستان بیش از ۶۰ کشته و بیش از ۱۰۰ زخمی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/122405" target="_blank">📅 21:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBC2WOg6Wh7qpHrhkpMPtowIHPUNrSCOwIfgmCH3aDzRcSEUB1t82VrRxEe-axyuXtN4bHLms3ZKuKLTj8fD1WD0x3PaLXB7NN8gPgXqMWYuV9ICiW__aSWBocizcVkfTnmFIhCw3e-BlPgU0FulTRgKDmmZ_JaZ3MonQeZSfmBbSrw2i0xHxv2Es99-G7BtNwN3XNRNl0u4dpg2q62LiHabRVTKP6nbUR_XVm2AC5JF51dr1405GHeaJbswDAHt9FveW6rgBOdB1Xt3PPOYgsjMNA0QjSp7h36oTiCjhGCamC7EH-O43L8rkWapAcCFiyBife86bs6DBUUZ7KV81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه وزارت خارجه ایران: در موضوع آزادسازی دارایی‌ها که مورد اختلاف است در حال حاضر راه‌حلی برای آن وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122404" target="_blank">📅 21:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ادعای یک مقام ارشد آمریکایی به آکسیوس: «ما در نقطه بسیار خوبی هستیم اما راه‌هایی وجود دارد که توافق می‌تواند تضعیف شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/122403" target="_blank">📅 21:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اولیانوف: برچیدن برنامه هسته‌ای ایران خلاف ان‌پی‌تی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122402" target="_blank">📅 21:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یه مقام ارشد دیگه هم به Axios گفته :
شرایط خوبه ولی هنوز راه‌هایی هست ممکنه توافق خراب بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/122401" target="_blank">📅 21:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عارف: حتی‌الامکان خاموشی نخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/122400" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiRQlFYbdEvdDEdVJKk8CM8VHLKmxPvKVi1DTF3EemyE5nPicaQLPrLTD6Rxkve34IlC7gybrurWWK456uqKbNkkMU3CEBRpNIOfqzx7vxHRlWVczlCzGfS5RckgeKW4qxGkM6DodyIn1hv-iiDFjfUliP7X0WY67jeTf0hDwNaarl7j4HNJL9xWgHufQ9i3Wimyf8aMxuQ4TvVWCMFETjHGAr-hYMkl2TeJX8LK-mKKTqH2rFdRJJwKloHpXbiW1u8ic621PZkkkRf3Dm_GhcaRYgyGqPu57nZAq139JqdxTiQIstKJp0038-N5OEuwdNVVY2ZaI4drhvBD0wCCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
120,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/122398" target="_blank">📅 21:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ادعای واشنگتن‌تایمز: آمریکا و ایران پیش‌نویس توافق صلح را ظرف ۲۴ ساعت آینده اعلام می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/122397" target="_blank">📅 20:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhc63T9wPyTES98iKGtaXLkhvQu1w6GPjHFwSKJ3I5sTLNXpDRfYdC28ppAQjl_zgxeEBo8JfGIFFu6o07KoJPSFfbgPLPw5t9ijEC5wOf6iuKu90SHpeNhLpW-UjZU-R6R9Xh_jQtFUlHbwC3PfjQ43KN5Is3I7aJCwETbWDwI6s3cU-G4uXKT9ZUUH6tqH5seH1Trui-cKa9MJq_Jw6sBvkOdZhOq6GRRMqffEbwD_8Vl1wtuc3VbKIA49Ln6zLlvWAD8HmgAH6cM79JKKf35-eHyzw7iNOMw0eoN0kzhmmezu6mwR8GcJmyiPBwev6iFYLXPWbS_ybHE50ZRJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۳.۵۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/122396" target="_blank">📅 20:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل هم اختلافات بین ایران و آمریکا رو تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122395" target="_blank">📅 20:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فاکس نیوز نقاط اختلاف در توافق ایران و آمریکا را اعلام کرد:
🔴
1. اسرائیل خواستار تضمین «آزادی عمل نظامی» علیه تهدیدها در لبنان است و ایران این را رد می‌کند.
🔴
2. تهران خواستار آزادسازی فوری دارایی‌های خود است و واشنگتن امتناع می‌کند و اصرار دارد که این موضوع به فرمول نهایی توافق مرتبط شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/122394" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پسر ترامپ: پدرم بهم قول داده نزاره ایران به سلاح هسته‌ای برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122393" target="_blank">📅 20:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHAm5M24S9wgKqu4yrczy9ILq5ezrmLZX8-3hyRBD0b4VPzYT_pMxHGWbzh-b9hMYxiWAh9_J74IZAq2r-aAFxpSYsFY8shxU_3C8dbYRVFzsDb-AjKc1A4NmFb-LeSAeag-JyF6V6gWUmNdQ73sC0Clwk3lB6Tgont1AiZJEqa0AM0VDnAEoZt-nTL2ZlpjA9NfFrDnFSt-1yDP_-ae7y4gvXfwHPlF3pgwbC3ys2u_bQZMnAOI5ZUk_JW3SOdAk3v0S2P5x9Q-wyOzTFclh1tt5x0rIBm4RemumkEuZVmN9_8LxKMKiU9rfLLGk-vqdTnMFuNEctHhMZnI8xjwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/122392" target="_blank">📅 20:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل شهرهای شرقیه، کوثریات الروز و زوتر الشرقیه در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/122391" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تسنیم: علیرغم برخی گفتگوهای امروز، کارشکنی‌ های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
🔴
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122390" target="_blank">📅 20:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / علی هاشم خبرنگار الجزیره: کمتر از ۲۴ ساعت پس از ظهور خوش‌بینی در مورد امکان توافق‌نامه ایران و آمریکا، حال‌وهوای منفی دوباره سر برآورده است.
🔴
منبعی آگاه ایرانی به من می‌گوید که نشانه‌هایی از عقب‌نشینی آمریکا در دو مسئله مرکزی وجود دارد: مکانیسم برای از یخ‌زدگی خارج کردن دارایی‌های ایرانی و دامنه آتش‌بس در لبنان.
🔴
بر اساس گفته‌های این منبع، توافق‌نامه شامل چارچوبی برای آتش‌بس در لبنان است، اما گزارش شده است که اسرائیل با این چیدمان راحت نیست و واشنگتن را تحت فشار قرار می‌دهد تا بندی را اضافه کند که به آن اجازه دهد تحت توجیه پاسخ به «هرگونه تهدید»، عملیات نظامی در لبنان انجام دهد.
🔴
ایران این فرمول‌بندی را رد کرده و بر یک آتش‌بس پایدار و ماندگار اصرار دارد.
🔴
تهران به تمام میانجی‌گران، از جمله پاکستان، اطلاع داده است که تا زمانی که تمام بندها به طور کامل توافق و تضمین نشوند، توافق‌نامه را امضا نخواهد کرد.
🔴
گزارش شده است که پاکستان پیشنهاد داده است با بخش‌های توافق‌شده پیش بروند و نقاط اختلاف را به تعویق بیندازند، اما ایران این رویکرد را رد کرده و اصرار دارد که بندهای مورد اختلاف بنیادین و غیرقابل مذاکره هستند.
🔴
تصویر کلی نشان می‌دهد که تهران فزاینده‌تر واشنگتن را در حال عقب‌نشینی از تفاهم‌های قبلی که از طریق میانجی‌گران حاصل شده بود، می‌بیند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122389" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل:
ما آماده‌ایم که فوراً به نبرد با ایران بازگردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122388" target="_blank">📅 20:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
طبق گزارش فاکس نیوز، ترامپ می‌خواهد توافق پیشنهادی توسط مذاکره‌کنندگان او، از جمله استیو ویتکوف و جرد کوشنر، اجرا شود؛ اگر این شرایط برآورده نشوند، هیچ توافقی صورت نخواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/122387" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تسنیم: کارشکنی آمریکا در برخی بندهای تفاهم تا این لحظه ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/alonews/122385" target="_blank">📅 19:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHjJU87iSQ8jbN5TDQM1C3YX1I0CEB7Z30boDV0d6THlOXn9eSPeEBLy-UaVOSAen8f51St9dSllHx5x0jm9Knoo3_KGwST3M-DCONXZv6GhfFmj1Wy7-xq2LrPra1Ewljw8l5GUdS-0mAZL5DqjJXhWkMvQxOey8vDIz7mtflv1GKEVDk8oVQ0-GFHPRqPn9hOulK3ImQi1-0CXtgoqcxgh_SflavqWkIoffT6MSpPeIirF7mTpGQ5dD-O2rcE2Smf6CF_q01UzHRestGvnYk5brz9MRdev0dmvDT4xTZMMMGFtuth_sGTpq1s2FBF1Vo0dw7ODroB5TfwRnL72Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGpgu79X6brJR8E1zlIBRZimp-sibkO1fBZrvPukNN3XbiqFXqKu4xPO9LjNXM1UTFq03h0HDbty2B6XtDPDRD3h79I-tEK4OEJDwJiaca0aT7WT_3NAIfgixqoAgPFQubq9Mvplf68HNiKV5Fzu8Zf22tG_II1nz6uMJJ4tJNDzAGEje3LqQGIBYOB-EokJ2Cv6e2gfv-Fl_UG9H2syraPuVRjNn3AroOcyqBJX3ZXGg_odjN8Er8PnN-LignxA5KQ_FO7Oi0I0l-IbVtvY6lDKdtuYjzo6M_KCoNdsUb6GS1aYCB9KZb_ine5aUPrl9smeYTWSXxBc_Dq7m6Tp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uy3IRo5ny16N-p3xGurLZysDppMOHUaNHSSs2t82oWVSTJsW2AGllD_jpFHIhR4NNW00UpH3lXlgsYUE-Wulk_acIDDb7eTq02h3JU1tqan08SRry2zZoMYuLEcmMQg5w9e0ZO2XDq_ydMcdod7RhkvydMlE1vjoB8Q1SfOS2vGPVX6VZ9h1Q35NAgHQTqbff8OaJuFvLxbbR-LLe5K0P1lZV9UPRh024qXRll3Gtz2fGkZ-W7qcWTWh8DwSxc6vIrkjmhTslPCv5BMKeHE1k2jOs2pLt9f3JxD378Dt78_OgQCwK8_UP7yMg-xRabDllHCp2SRnPc6LRU8dgFUbBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b49bac95.mp4?token=rZWeTafMnOTV7AL3SfliEZ1bmedy0trarRwoEbEUV2fIE2KhuJeELFan53SyFFNDv3-s40racCfEiPagEakSgLTM1CjQy0XxVx1R1m4viSJY-qyvefKlBlf7DiG-W4EXtQnqSEvkXqvhoNyCnYVo5MXs78a2K1FP2yS85-p3bp-3tmdLCJCyiCWAhumtgWMqcuAG-olHFmvsHRx3Zceeoydnr5PACaZx6gzO-kncCy0bSD_cw41tVGGoFOA2fyJ2_3iSGyrSZ0vc_zQOAsWMoqaEfoJK2gkivEp7rbhTzxwgfzn1qRyUdzdhGyqhYBMemrlseZgzdXAjDpIaVdUmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به زراریه، سومور (دره البقاع)، كفرسیر و سر الغربیّه در لبنان حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/122381" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: خلع سلاح را نمی پذیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122380" target="_blank">📅 19:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز: موضوعاتی نظیر ذخایر موشکی ایران و غنی‌سازی اورانیوم در مذاکرات آتی مورد بررسی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122379" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس گفت: برخی از جزئیات توافق با ایران هنوز نهایی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122378" target="_blank">📅 19:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مسائلی مانند ذخایر موشکی ایران و غنی سازی اورانیوم در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/122377" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
منابع به المیادین: ابتکار چین، تنگه هرمز را از نقطه تنش و اختلاف به نقطه‌ای برای توافق و حل‌وفصل به سود همه طرف‌ها تبدیل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122376" target="_blank">📅 19:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌بی‌اس گفته که به واشنگتن اعلام کرده‌اند حتی در صورت توافق با ایران، آزادی عملشان در جبهه‌هایی مثل لبنان باید حفظ شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/122375" target="_blank">📅 19:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXwZ-ztoNig0CQX7iGtlABxvMYP15XsAFmPz9lTkCWH8DE5AW_RwP5JOCkj09TKPcmV9Z5qTnzeQEMzWH92Haa4i3pE9OxwkqW2BEW34tfudILlQIyMBqt96-zBAo09mzBumoiaiuLsQIP-hbNGhKS5l6aICP-Zvd4fyudeN9TFlsO4LkawDyOzSQB2Ab30qcDZYoMTQPWDPS1q-Od_sc96P-hJhRzyTRfdTRra1Wdw9598o8RD3jM-lpYTnKTayJSnL_cIEDmD_pecGfRlPZVjxN5ijP_8yqSQa1CcUOkE7fuYmlOgstIL4US3eVwmkI1cHVpgZFFcukpOSmF0pYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvR8QY0Kja4N5wyM2iuY5xRXurzoT2Oo5GOhWNgW2h3SBP5zEAjkgsNpxf4O2cH2s9IvdJyNRioJRAnVke93tYelrJl1Y8Y8e8U29B2Jsw5fCX8ghcnBEMwg1emc9qI1iyxbR5fLXfI-srFYei0OQEmy0VyzgZ4V-aO_2pE5FPIH084QZ3BMJIKMUV5uBw7ZOBLnYo8A3n56DeyW2xtRjTtOv9JK2B11deXK-adDdWLfnlEKyCxTQIrM7N7B2N-2xpNcl6m9I50Z2ADOeZDNiZYYV6MBqxReaAcSTJWliinEwR5DUYIjhlo_6bcxM6Qz9F4OPGqtqJ_WVBzm-6V4xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسرائیل دقایقی قبل حملات سنگینی در جنوب لبنان انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122373" target="_blank">📅 19:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUELXwrRDgx4KGBMfPEPDWkVoZUN2hjso5k62AwnMzsXMijAVoitTyGd6NMWdx0OI6lovWj5kUT6xMy0H_emKscldkik0r58Zhthsz1WVJGxz79Z990RyUcn6KnlFdQU0dmXbIN-b4ynMeBzQXeqmkSqWxnJvQ0FQyD9_vr6LlnmdUkLEQaw9v5VoBdPeapGctJ5d0zpx8gVq2H37JxXFoF9oOBnhf9cwlbf9DK00nfMdjIA8zHIwZzY1vQVhATJe5TC2ygsDfNzKlqnZtqJue2Yo2ew_FnrpPW7FTJbY6etqEd2hoSOs_PLpQiHpFN_l9MncioSfvjON83SgXRJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSbjfy4kWqfAkLk-R78hYV_eMqShu0Wzez3iph_X8GsvqkHCu64GYm-LquBhJTVlVtoSgKMKwEcOl3fuHTTAk8bZRt3ytTXv9W1lUAE0n-_YwKt-x16hv0OJsC_9KNqMqIGthy8e-pYEJmYJ-GhJw2XTH9RMJUPdxR5_JgaADyLQNb0b0yLF8zGEIQwFjw07tSTEetfkOBliwXfrhY04472_4Pd9WiGa1Ga40W9J1ALpHf63ZU1ZwL9EiXkhPDCx527N9F8dptDvCkB_ZUe4XCKDpLjJOeY91txYUI_WflEGih-gch5LAq21lubWz41V_UnHz23TzYU9WxMzmEZgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUQSTO1TGw04YCeUJvA_sJR9RapeGEME-e9YqhW2XkNegTVCarySQ_DGwUzxJfQiUAYWjzR9Vicyba5OStBc6N3VFgCtGNT4ih41o7vI4CCtvPXONm-CL8uC5OK8-jOWQh_tnVurmWV-wBydfd6at8BwaC70E3KIdb5n89lT0tEVWMaTVRZ9nTLdQBqC2kBznuiDF_ZpszXEDLtcqWhC-CRcQ6aHrc-kyUFgjAu4dD3EdAErFJSdf_pwtHMDLmBoW4cePAUCHtzi2cKyyx8jTLsz3W1GUq0EiygFXZ-9GZjhWwTsHa-NGj_uiATvX63e0h8ewOhJrcZnwV1KXuYnww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122370" target="_blank">📅 19:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prEJB0b_ppvRYpkV-5U6PL-KAFn1C9HQHjHgf5qsKtR63v6CUBHJWU7uEEq8xhLWPXjNAzY5U-hOZFEQA08A7lFHZKcp4w1X6a3MEoKBoFYM9Ht2ZMmdkejrenC28RV2MD-2ASTBh9T-O7nG_o_vWBDg6lv0Bgwr-cpfrot-iU9wILK3E5ln2DF7-gjqwpuH84mLf1qs3NyuradXin6ae4R-MSULhhB8lCjbVlDr3wf5hTpSiuhLl8ZRsxYe8tWOuIYHP834tr8n1AKbYma8tYdb9V0wcXBmXtXiJy5tH96C0WIxQq_35RIM4THtabq_X2XELhDvvNtICqi2GRdihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: توافق ایالات متحده و ایران برای بازگشایی تنگه هرمز امیدوار کننده است، اما کشتیران‌ها همچنان محتاط هستند و بازسازی تأسیسات تولیدی و ذخایر زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122369" target="_blank">📅 19:10 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
