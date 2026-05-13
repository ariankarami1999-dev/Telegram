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
<img src="https://cdn4.telesco.pe/file/Bv7gP7nZvNVUGBF8tmi-E1IxSO3qas54juQxOWZOnSP8-SiaVyI52ZfAfcSi0hKKxhbgnDzOKNb4fdv41qmcj_QPVht46KermKP9y42I7vR37Vd50jTFYA2qafbqgqIKOIoV6xgE9HUVziWOpkoFnJCaDvADeuG8sSbsYKglIRWlcoupKMEfvVFgyVzdgC1VZeuQzS_jYBNTW_zzdeKY-zf2kz1xwpkjFj_KUL-JrTPwf4rCREgUyiEKxybnLVGlztSmg3qW3qZ9JsCOh9Gi2fNrJhNzpNG0vJGbzyT9ug1_RSKb2qGiB_M590_2kVn-vBSzlQokPHEXfSwjbd-JxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 259K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-11133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب جلسه امنیتی ویژه در مورد ایران برگزار خواهد کر‌د
@withyashar</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/withyashar/11133" target="_blank">📅 12:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11132">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbiQo6rjbSexTHLanMHlkCi2etLfvfmNcYjFqMepf0lgz4G3UCnvU61ySHv1wUxbaQ2Kk0OzmF8rOx0VwXOibhPHCNO_-ABPCbLTBeBwy1cUTmK9q-2utL4OD7fWqVfXTvS-IG4Trh7BGkUH0QvgRAVGaB765rkD1eM6N696pFv8RLt292yezHS8UF93VmLMw36bx6mTPJQHDdgwozjfmfxnVmpBCpO3KZAqDuHPbrAcVRC_CFMfa4hbi45zSMT4qk9RHBVnjD6RCAmgO536M9capV5hsYcdrkkGFi_nVyCMI1FUdfvZ_fiIcnMIgkqOLObUBOQ1IbWFVZteIY2Kxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/withyashar/11132" target="_blank">📅 12:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فدراسیون فوتبال: امشب مراسم بدرقه تیم ملی فوتبال به جام جهانی، در میان تجمع حامیان حکومت در میدان انقلاب تهران برگزار می‌شود و قرار است در این مراسم از پیراهن تیم نیز رونمایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/11131" target="_blank">📅 12:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11130">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عبور ابرنفتکش چینی از تنگه هرمز همزمان با سفر ترامپ به این کشور
داده‌های مارین ترافیک نشان می‌دهد که کشتی
یوان هوآ هو
صبح چهارشنبه در حال حرکت به سمت شرق از طریق تنگه دیده شده است.
برخی بر این باور هستند که عبور این کشتی نوعی اقدام مبتنی بر حسن نیت از سوی ترامپ برای جلب نظر شی جین پینگ است.
@withyashar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/11130" target="_blank">📅 12:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11129">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک مقام ارشد سابق موساد: ایران ممکن است ظرف چند ماه از نظر اقتصادی سقوط کند اگر محاصره ادامه یابد
@withyashar</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/withyashar/11129" target="_blank">📅 12:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11128">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/11128" target="_blank">📅 12:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروژه هارپ یه پروژه برای تغییر در آب و هوا بود طوفان میتونست درست کنه ولی زلزله نظر اکثر کارشناسان بر این بوده که امکانشرو نداشته و فقط تغیید در لایه های جو بوده به هر حال دهه نود ساخته شد و ۲۰۱۴ امریکا گفت پروژه کنسل شده ، ولی تئوری توطئه زیاد هست درباره این پروژه
@withyashar</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/withyashar/11127" target="_blank">📅 12:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">سلام مرسی از همه زحمت هات
زلزله میتونه پروژه هارپ باشه؟</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/withyashar/11126" target="_blank">📅 12:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درود یاشار جان، خسته نباشی. مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی. داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟! قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/withyashar/11125" target="_blank">📅 12:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11124">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadegh</strong></div>
<div class="tg-text">درود یاشار جان، خسته نباشی.
مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی.
داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟!
قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل ۴۰۱ بود فک کنم.
بنظرت میتونه چیزی بجز گسل و دلایل طبیعی باشه؟</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/11124" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlS5Yj9zjnBT--WF8p4yUwgW0gkRaEIJ3E-gFhbeICypbY-yjDtxSSyGEAIvxa5iFVqcdR4ASXts5EfJBgXTJcW9RUt7uSNgAR-7yk6-8yQuwcHbtp7qk3rapDhOnTcID8wSP5I1vS82YNAPNAXeocGtCfJJ2jYi4WgSR3HQ_mSFc5mOK4vHeKAf1-fbhv8nEQym919WYzm1ZAga0d0zuyN1HlEj1vwACpIBOVDfRBwPcERzA2o51Mfe32CEYdCdr57tb9k6hAYY8krkOio05eM2j_FJiyuxuCb-93m_uNP1WX1QKBQBsp6xu3_fc_mQOu79_zk0HuZ-EZGxcV5HTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهندس ارتباطات حزب‌الله که متخصص فیبرنوری بوده و پشت توسعه پهپادهای انفجاری این سازمان بود،   توسط ارتش اسرائیل به هلاکت رسید.
@withyashar</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/withyashar/11123" target="_blank">📅 12:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند
@withyashar</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/withyashar/11122" target="_blank">📅 11:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش مرکز ژئوفیزیک از شدت ۹ زمین‌لرزه بالای ۲.۵ ریشتر در پردیس از روز گذشته تاکنون
ساعت ۲۰:۴۱ — بزرگی ۳.۴ ریشتر
ساعت ۲۳:۴۶ — بزرگی ۴.۶ ریشتر
ساعت ۲۳:۵۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۶ — بزرگی ۴ ریشتر
ساعت ۰۰:۳۲ — بزرگی ۳.۴ ریشتر
ساعت ۰۰:۵۴ — بزرگی ۲.۶ ریشتر
ساعت ۰۳:۲۹ — بزرگی ۳.۱ ریشتر
ساعت ۰۵:۵۷ — بزرگی ۳.۳ ریشتر
@withyashar</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/withyashar/11121" target="_blank">📅 11:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">غضنفری:شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند
@withyashar</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/withyashar/11120" target="_blank">📅 11:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62701b581.mp4?token=isLMB9sxZVznQHj52Mq71SpDYWzgtYv3KltmhqOgzQAwwnlv2n_2Gq8pi0oM3duu_cqQODiZthwpr9N925pzzfz8fuiyolDKe3oKaTwvp4Xf3UzJ-HXmzbV7TSd1c5HDdwnpHXniD-N41M0LT3IOi4aD5A-doYBWnMA3dFD_66z9qebBknAcUA7pChS_5fRk_b-RSgMreDDOzq9kR7uITiRYZklq89ML7HUQvM8fVqTiPhXQkc5_4k9GbEmp_Z5Gv10HN3AML4pl4MaANftY7WLWHQROlzWiIVjdh0mJirlRp8go6uZUY7-DqKvhbz53i7R1z-pEz47aTKU26RmS3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62701b581.mp4?token=isLMB9sxZVznQHj52Mq71SpDYWzgtYv3KltmhqOgzQAwwnlv2n_2Gq8pi0oM3duu_cqQODiZthwpr9N925pzzfz8fuiyolDKe3oKaTwvp4Xf3UzJ-HXmzbV7TSd1c5HDdwnpHXniD-N41M0LT3IOi4aD5A-doYBWnMA3dFD_66z9qebBknAcUA7pChS_5fRk_b-RSgMreDDOzq9kR7uITiRYZklq89ML7HUQvM8fVqTiPhXQkc5_4k9GbEmp_Z5Gv10HN3AML4pl4MaANftY7WLWHQROlzWiIVjdh0mJirlRp8go6uZUY7-DqKvhbz53i7R1z-pEz47aTKU26RmS3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور 53 جنگنده F-16 آمریکایی در پایگاه شاهزاده سلطان عربستان  هواپیما جاسوسی آواکس هم که دیشب نشون دادم از این پایگاه نظامی بلند شده بود
@withyashar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/11119" target="_blank">📅 11:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/11118" target="_blank">📅 11:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPSd6ysrg05bPQ6kc_I9mDPVx3rSCh8zhptgXTV25SiAf8_O7wTDlqvdU8AwijEsQToHEv7P3UCe_Eo9E4hucmQzjjmNfGBIoa094BN10FU3SOw4BMS2EETvJVrGq4swwD5XM9BwFBu1P9hNvX7fka8lpXJ9h0iHRt-uxI_uUyaZoapiaj1_p8nchZLQHas17p9JB0lGONARyr_i65fmd1duwq6w7VxObXFFhGBcrn9sybkPF85wFW_FOoGyHxCFHZsEdpJM1P779U0ANrDOE0PJHxEwTZ1an_EEt5IT2-TZFxk9us9CZZ4IwYe_G0wCoV9rlyxi4Y1vFN3mrLOE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس وایرال شده مارک روبیو در هواپیمای ایرفورس وان که همون ست گرمکن مادارو را پوشیده. نکته ای که کسی به آن توجه نکرده کفشهایش است که مارک آدیداس هست.
@withyashar</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/withyashar/11116" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11114">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpACFgndmeGEpC6OCKdy0muwGveJ8OHwvjlV3Qkh3eieLRzFPNmey9iLoB0EAJK7t2sWlhlm2pA8Amq1w3t_khzP1ylxkzrr-MyOlBb_zFEKcDQpdIJuqh4WYa4lgK0tyXieWUrsGoCUQe5g_5uE0nb3nohf0bx7uHVRGJHsll-7lYL_7oykr6EH2CXbUXsoR9BfRu7SlqwcgqPVkUd75UD6Utua1A1rUpav1psJjvs4fAFETwQVFz9CZLlk-CrG_JA05Lsh7lws9J1vliF3DFNxT2keWpZkpcN9Ci7iy8H1yKJf7Sm5QnEBeEzBM0ugIp2nhRyqb0fHg9bDBgz5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/11114" target="_blank">📅 10:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBJEqu47qk50WSTtOx4q67O6Rzy9gN_GvaijCx0sx3cDyZtDAnPJpl97UOlWzjr5DqtETjkEGg8FxeGoeZu3OztoGhUEJ2kkXpWl8zVLq2v2Rt-QTIq-sxi0kOLJMNvahRkKgIEroqHzJashYsmeBenbwe7DqxpLaiEkQZXEgUPvNYEKpZaR-ltWs2pjVE7wEO180T68pfbwh3FKqMvncw45wRI70D1obLQfmJza45s9PibzA3A2738XiTJlmsYwDEWOvUlJRcRXWoS9j3IhglwRntOnd0a96JMUGAO9km1hv71K6EuiT9Dns_CEjIzzt3TNZ72oS1EASuaXV_WwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهد که یک هواپیمای باری جمهوری اسلامی مدل C-130 در پایگاه‌ هوایی نور خان پاکستان پناه گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/withyashar/11112" target="_blank">📅 10:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الجزیره: منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/11111" target="_blank">📅 09:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کیهان: اگر مذاکره کنیم جنگ می‌شود؛ مذاکره نکنیم جنگ نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11110" target="_blank">📅 09:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ویزای ۵ ستاره عراق برای جام جهانی رد شد!
آمریکا در تازه‌ترین اقدام خود در آستانه جام‌جهانی ۲۰۲۶ ویزای ۵ بازیکن کلیدی تیم ملی عراق از جمله علی الحمادی (ستاره لوتون تاون)، مهند علی و حیدر عبدالکریم را رد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/11109" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ در تروث : شبکه سی‌ان‌بی‌سی به‌اشتباه گزارش داد که جنسن هوانگِ بزرگ از شرکت انویدیا به گردهمایی شگفت‌انگیز بزرگ‌ترین زنان و مردان دنیای تجارت که با افتخار راهی چین هستند دعوت نشده است. در حقیقت، جنسن همین حالا در هواپیمای ریاست‌جمهوری آمریکا حضور دارد و مگر اینکه من از او بخواهم آنجا را ترک کند که بسیار بعید است گزارش سی‌ان‌بی‌سی اشتباه است یا همان‌طور که در سیاست می‌گویند: اخبار جعلی!
مایه افتخار است که جنسن، ایلان ماسک ، تیم کوک، لری فینک، استیون شوارتزمن، کلی اورتبرگ از بوئینگ، برایان سایکس از کارگیل، جین فریزر از سیتی، لری کالپ از جی‌ای ایرواسپیس، دیوید سولومون از گلدمن ساکس، سانجای مهروترا از مایکرون، کریستیانو آمون از کوالکام و بسیاری دیگر، در این سفر به کشور بزرگ چین همراه هستند؛ جایی که من از رئیس‌جمهور شی، رهبری با جایگاهی برجسته و استثنایی، خواهم خواست که چین را «بازتر» کند تا این افراد درخشان بتوانند توانایی‌های خارق‌العاده خود را به کار بگیرند و به جمهوری خلق چین کمک کنند به سطحی حتی بالاتر برسد!
در واقع، قول می‌دهم وقتی تا چند ساعت دیگر کنار هم باشیم، این نخستین درخواست من خواهد بود. هرگز ایده‌ای ندیده یا نشنیده‌ام که برای کشورهای فوق‌العاده ما از این سودمندتر باشد!
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11108" target="_blank">📅 07:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhEODDLs8pq8xXmgzKopEhjGfdoYPnUIteemBzpC5VPanUzZos7zC8X_HAfzgC9hUivmo90a2IGCEFekD9ToxmFZCO68-QkVgfPRnLDqrUnS2LLa10NTSzc4iY0nKj-3F1y7ZzWCldQaiddGDjL6wnAVVoaL-f_UMsT2iIqXB5bGtAseZOh2L5fNE1guaam_OGasIDypwCJdiNlc2sGAwgqi-XHJ9yEtIs7MhLZ68gzhs2LPpU1hjvoyEFpxDxsmAZxzEmkb9-6U4NQ1oy3KYV2QvDl_JKuY_eJeprGnUSm5odGQK9l0kotu5eZ8AqwwocD51iTMZN1aGi9ykq3tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پستی گزاشته که ونزوئلا رو به عنوان ایالت ۵١ ام آمریکا نشون میده
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/11107" target="_blank">📅 07:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/11106" target="_blank">📅 01:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجان فدای میهن</strong></div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11105" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11104">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه  بزرگی: ۴.۶ ریشتر  محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس  تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07  عمق زمین‌لرزه: 10 کیلومتر   @withyashar همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11104" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=tPfj6YJocm-mabANp2K-tYQ3UCbwIuqrV7FXst1g8FgJAlJSG7ASjJu1b0rkvIqfvmguLKo0OXPnovwQ4QRszgLBKSYvpccFnJDjiF-2a856qs9TDL9YU7zxr6OvM8z5jdb5OhyyulcqZbg7HP3ir-6iQtGy6gF20_07GWF_SCCrvpkwqbsR4AwiFH6fDPxBojRKMIK4CVkESMi6tl9CAUAUl-88qbahiWnMtJqvM4SwLJgWfwg9xUkMcByN-cQ7zo40_IXP3IFYf86FRGelYlpoODlnKGcqQS_LoXoWpo-0GslV-HY_08j71YN1Gh9rf0jlIaC1WkIDLGExnZkQjCcXfh_Od2ZxN0mzgpzMoQQ4ChQVeRE_HxwXXjHdQ5ZxNJ51tIK5MN980y-iqOHK0zUYhQn1Lgh8fGZbjl1gZJBsdB7jmej97IQyfjv4upEMKCqavjuJD8mk5CfLX3Yjz_lDN0xkVCMMy6MCgYHZhoevp7xx9kRzHFCyAgQNk2Dq-DiGJzXQC-lLoF07MDXfE1P3mn0TzPV1060WeZEuGkLmdN30aTWqKxdoG3MZmMCPCarCf_PchGy3lPZjZecU3a_xPq9vf5XRywoDDR1cdTy_hjJGrtxkw3_Xg6mSWJFvK6uhAE0SUTbriSK2Xm0kYfG8qcypMNAuSfnbdTWhZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=tPfj6YJocm-mabANp2K-tYQ3UCbwIuqrV7FXst1g8FgJAlJSG7ASjJu1b0rkvIqfvmguLKo0OXPnovwQ4QRszgLBKSYvpccFnJDjiF-2a856qs9TDL9YU7zxr6OvM8z5jdb5OhyyulcqZbg7HP3ir-6iQtGy6gF20_07GWF_SCCrvpkwqbsR4AwiFH6fDPxBojRKMIK4CVkESMi6tl9CAUAUl-88qbahiWnMtJqvM4SwLJgWfwg9xUkMcByN-cQ7zo40_IXP3IFYf86FRGelYlpoODlnKGcqQS_LoXoWpo-0GslV-HY_08j71YN1Gh9rf0jlIaC1WkIDLGExnZkQjCcXfh_Od2ZxN0mzgpzMoQQ4ChQVeRE_HxwXXjHdQ5ZxNJ51tIK5MN980y-iqOHK0zUYhQn1Lgh8fGZbjl1gZJBsdB7jmej97IQyfjv4upEMKCqavjuJD8mk5CfLX3Yjz_lDN0xkVCMMy6MCgYHZhoevp7xx9kRzHFCyAgQNk2Dq-DiGJzXQC-lLoF07MDXfE1P3mn0TzPV1060WeZEuGkLmdN30aTWqKxdoG3MZmMCPCarCf_PchGy3lPZjZecU3a_xPq9vf5XRywoDDR1cdTy_hjJGrtxkw3_Xg6mSWJFvK6uhAE0SUTbriSK2Xm0kYfG8qcypMNAuSfnbdTWhZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بلرزونش ، هواپیمای جاسوسی آواکس و زلزله… حجم کم
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11103" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: دو تانکر حامل ال‌ان‌جی قطر، به دنبال توافق دوجانبه جداگانه بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11102" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11101">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه
بزرگی: ۴.۶ ریشتر
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
عمق زمین‌لرزه: 10 کیلومتر
@withyashar
همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵ کیلومتر در تهران تاکنون ۱۱ حادثه به این سازمان امدادی گزارش شده است.
سخنگوی اورژانس تهران نوشته تاکنون ۷ مصدوم که ۵ نفر آنها سرپایی درمان شده‌اند، در ماموریت‌های امدادگران ثبت شده‌اند اما ممکن است آمار مصدومان بیشتر شود.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/11101" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11100">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/11100" target="_blank">📅 00:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nciKUkw_vs3zyyeU8x3WojP_TSy9IZfiY7BVSRvyXpHw-FTjs327qgb5L0rFg2irVY3yidmZX7H3MjfwtRaoL2X7ryyTndEgno4xLvlPDuUAqjQOnOveR2yz-uUKC4EB-fzDwpREunCFofM5r8ErvFRUgwDR1OxUmBC_WECGOv2422UCPfsdiVGya4rC1QsZ6h0zx5VKqCg0qxDSh_Mq0FeNuTP14C32RIDkkTVHrkeUhLE3MTq20NaPr84H4Qwl2d32iJr3QynGhbYIfLsG-LytCr7v5fInUNgQhKEcwS5jBqX7-0K8_j5HBhWqjxk-1So5RsH0rDCltGSrK8fhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
وقتی رسانه‌های دروغ‌پراکن می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً نوعی خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آنها دارند به دشمن کمک و همراهی می‌کنند!
تنها کاری که این حرف‌ها می‌کند این است که به ایران امید واهی می‌دهد، در حالی که هیچ امیدی نباید وجود داشته باشد. اینها ترسوهای آمریکایی هستند که علیه کشور خودشان طرفداری می‌کنند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت — اکنون تک‌تک آن‌ها در کف دریا قرار دارند. آنها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان نابود شده، تمام فناوری‌شان از بین رفته، «رهبرانشان» دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلال کنند!
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11099" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11098">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خارجه آمریکا: با چین توافق کرده‌ایم اجازه اعمال عوارض بر عبور کشتی‌ها از تنگه هرمز داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/11098" target="_blank">📅 23:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11097">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اتاق جنگ با یاشار : جابجای‌های غول آسا دو شماره یک «AirForce1» هواپیمای ویژه ریاست جمهوری و «B1 »بمب افکن اسطورهی آمریکا و خبر ویژه از داخل ایران
https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==
کارای اداریش رو انجام بدید تا بعدش بریم برای سوال جوای</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11097" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BABKmF4Hhfp7HU_ppN4uXrm2Oy0gnB89vramXcMFDjdqQ5nCpsCmQgpcw4lIO4xY7uNik3Rw_fu4p2hA0ZQuXNQZSl3WklR-alCNYbQP1cZd8-YcdpTHLywqrSwqzam5jMJ9cv5Uqdv-QDFW9epDIdG2LFQM7RjKtZHU1eMULZF2ZPbp-2nXWCBjmsX7_cTD3cBwHltLtu9cLoVJdtfiHf3LnfrDS00qDwo_Es_JnskSH5kLX6uMnHD4-yXwUtFHJYOfTT25VUNkDUIJy4oHmD8Id2GtQzLQiOsYMbPdmTK7h-iwwTfmFiahqKfL8FvfjIO4wKMeGZZZHaQgdC5uGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11096" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11095" target="_blank">📅 22:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11094">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=ceVg8hnzuZw_NTvqzYc4hxGztFeF7BocZS6CR1rpEj83gRT5YqhTOsWxK46uMijAs11i3Qucn3etrcmIJxcU6UYCn-Qr5sGKWWI3Yc16G3v99BLyy-u__vKxYhwpOka2p61lvJUzyp_7fxVCRMOtko1QctU1ZERAKCpT-Xi4DmxCR9HbOrBgMGudQStvI8EJFmFhD2Czk9h9KRaIA-b5lMBZepOqrslN_JTVNOnqFoBGkXdUI7nvJZ0YedgaDssxfyC1mhD3_YpcfSS95oQZqhy4p4h3Z-DFm8aKq9nfWyHX14qP_JIvKnpqD-gtUjGYs7fWQFqY4U5_hHT2gj5Spw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=ceVg8hnzuZw_NTvqzYc4hxGztFeF7BocZS6CR1rpEj83gRT5YqhTOsWxK46uMijAs11i3Qucn3etrcmIJxcU6UYCn-Qr5sGKWWI3Yc16G3v99BLyy-u__vKxYhwpOka2p61lvJUzyp_7fxVCRMOtko1QctU1ZERAKCpT-Xi4DmxCR9HbOrBgMGudQStvI8EJFmFhD2Czk9h9KRaIA-b5lMBZepOqrslN_JTVNOnqFoBGkXdUI7nvJZ0YedgaDssxfyC1mhD3_YpcfSS95oQZqhy4p4h3Z-DFm8aKq9nfWyHX14qP_JIvKnpqD-gtUjGYs7fWQFqY4U5_hHT2gj5Spw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سوار ایرفرس وان شد و رفت به سمت چین
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11094" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوباره ترامپ یک خبرنگار دیگرو هم فیتیله پیچ میکنه اعصاب نداره امشب این بازیکن
خبرنگار: تورم الان تو بالاترین سطح خودش توی ۳ سال گذشته هست. آیا سیاست‌های شما کار نمی‌کنن؟
ترامپ: سیاست‌های من به طرز شگفت‌انگیزی کار می‌کنن! اگه به قبل از جنگ برگردین، تورم ۱.۷٪ بود. اگه می‌خوای این دیوانه‌ها سلاح هسته‌ای داشته باشن، پس تو آدم احمقی هستی و من تو رو خیلی خوب می‌شناسم!
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11093" target="_blank">📅 22:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11092">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ یک خبرنگار رو به توپ بست
ترامپ: ما یک سالن رقص داریم که هزینه ساختش کمتر از بودجه هست. اینجا ساخته می‌شه. من اندازه‌اش رو دو برابر میکنم چون مشخصه که بهش نیاز داریم.
خبرنگار: هزینه‌ش دو برابر شده
ترامپ: من اندازه‌اش رو دو برابر کردم، آدم احمق! تو آدم باهوشی نیستی
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11092" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11091">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/11091" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoni Ami</strong></div>
<div class="tg-text">Yashar jan, Chera enghadr faaliat kam shode top Paget? Aghaaaa enghad zahmat mikeshe Like konid</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11090" target="_blank">📅 21:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ به سیم آخر زد و برای با ‌چهار هزارم گفت :
من به وضعیت مالی آمریکایی‌ها فکر نمی‌کنم.کلا به هیچ‌کس فکر نمی‌کنم!
فقط به یک چیز فکر می‌کنم: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. همین
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11089" target="_blank">📅 21:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار: فکر می‌کنید شی جین‌پینگ باید اصلاً در موضوع ایران دخالت کند؟ یا می‌تواند به نوعی کمک کند؟
ترامپ: فکر نمی‌کنم ما نیازی به هیچ کمکی درباره ایران داشته باشیم. ما این موضوع را یک‌طور یا به‌هرحال حل خواهیم کرد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری. تمام ماشین جنگی آن‌ها از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11088" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: درباره جنگ ایران گفت‌وگوی طولانی با شی خواهم داشت
ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11087" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">همراه با ترامپ قرار است یک تیم اقتصادی بزرگ از روسای برخی از شرکت‌های بزرگ آمریکا و جهان به چین سفر کنند تا روابط تجاری میان واشنگتن و پکن را تقویت ببخشند،این تجارت‌های کلان اگر موافقت شود برای هردو کشور سودمند‌ است.پیت هگست نیز امروز گفت ترامپ می‌خواهد از…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11086" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZv-viN5kXNOEPPiDEsKs4nKerkuSzRTxqMMqsRo3eNoQL_EYHN-HnlumoD03St8bpP-13UAIDwLxWcQpcGp5Yf1w7SQA527BHayn7OftpMM2uBS9svOSI9kpMemCs9DkI2yzWu-4vtY8Hxc9Mjvm_4QY22EaSuZv6-WRhIzD4oBIY0mpuYG0mfFq0f5nEffopacWARGTQgEUswciZmD-pejxlybHLO7LXN5OE6A2hCQwKRilLxZmiAaLoDseOgXQjE05iFOuN1t6hikpv9OQUx8UnRssDqjbEJ1-MJpHkCXLhNVEqYUmkuyZNd5EEloqSqdmf8aCRGjtVVJuOcIlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه با ترامپ قرار است یک تیم اقتصادی بزرگ از روسای برخی از شرکت‌های بزرگ آمریکا و جهان به چین سفر کنند تا روابط تجاری میان واشنگتن و پکن را تقویت ببخشند،این تجارت‌های کلان اگر موافقت شود برای هردو کشور سودمند‌ است.پیت هگست نیز امروز گفت ترامپ می‌خواهد از نفوذ چین در برخی از نقاط جهان(ایران)
برای اهداف مشترک استفاده کند.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11085" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چهار نیرو سپاه تروریستی توسط کویت دستگیر شدند.
سرهنگ امیرحسین عبدمحمد زارعی (سرهنگ نیروی دریایی)
سرهنگ عبدالصمد یدالله کنواتی (سرهنگ نیروی دریایی)
سرگرد احمد جمشید غلامرضا ذوالفقاری (کاپیتان نیروی دریایی)
ستوان محمدحسین سهراب فروغی راد (ستوان یکم نیروی دریایی)
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11084" target="_blank">📅 20:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست امنیتی سالانه پولیتیکو:
سیاست مماشات با رژیم جمهوری اسلامی که راهبرد بسیاری از دولت‌ها بود، شکست خورده.
با یک جانور زخمی روبه‌رو هستیم، این فرصتیه که نباید از دست بره
بلکه باید کار رو یک‌بار برای همیشه تموم کرد؛ موضوعی که نه‌تنها میلیون‌ها ایرانی، بلکه خیلی از کشورهای منطقه هم انتظارشو دارن
مردم به‌اندازه کافی هوشمند هستن که تفاوت بین حمله به یک ملت و حمله به یک رژیم رو تشخیص بدن و اون کارزار، حمله‌ای علیه ملت ایران نبود، بلکه علیه رژیم بود.
ما فقط زمانی می‌تونیم مردم رو به بازگشت به خیابان‌ها فرا بخونیم که اونا از سطحی از برابری در توان مقابله برخوردار باشن.
نه زمانی که رژیم بتونه اوباش و نیروهای سرکوبگرشو برای کشتن مردم در خیابان‌ها اعزام کنن.
اما برای رسیدن به اون نقطه، باید پیام روشنی وجود داشته باشه. باید راهبردی شفاف برای پایان دادن به این رژیم وجود داشته باشه.
فراخوانی روشن برای قیام مردم، و همچنین پیامی برای نیروهای نظامی و امنیتی از حکومت جدا بشن و به مردم بپیوندن
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11083" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11082">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئیس جلسه: آقای وزیر، اجازه بدهید به سؤال سناتور کونز پاسخ دهید. سؤال ساده‌ای است: چطور قرار است تنگه را باز کنیم؟ در جلسات محرمانه، افرادی از تیم شما به ما گفته‌اند که راه‌حل نظامی برای بازگشایی تنگه وجود ندارد و در نهایت این یک تصمیم سیاسی از سوی ایران خواهد بود. شما هم ظاهراً همین را می‌گویید؛ اینکه فشار اقتصادی، تهران را مجبور به باز کردن تنگه می‌کند.
پس آیا تأیید می‌کنید که راه‌حل نهایی دیپلماتیک و اقتصادی است، نه نظامی؟»
وزیر جنگ : من می‌گویم قطعاً ابزارهای نظامی برای باز کردن تنگه وجود دارد؛ چه از طریق اهداف زمینی، چه توان دریایی ما و چه محاصرهٔ دریایی.»
رئیس جلسه:
اگر این درست است، چرا تا حالا انجامش نداده‌اید؟»
وزیر جنگ:چون راه‌حل بلندمدت و ترجیحی این است که توافقی حاصل شود که ایران تنگه را باز کند و دست از دزدی دریایی بردارد. این فقط کشتی‌های آمریکا نیستند که متوقف شده‌اند؛ کشتی‌های سراسر جهان درگیرند و این فشار بیشتری بر دیگر کشورها وارد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/11082" target="_blank">📅 20:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سناتور : من هیچ‌وقت از رئیس‌جمهور نشنیدم که بگوید هدفش تغییر رژیم در ایران است یا می‌خواهد همهٔ مواد شکافت‌پذیر آن‌ها را تصاحب کند. چیزی که من شنیدم این بود که هدف ما فلج کردن توان آن‌ها برای باج‌گیری از جهان است.حالا شاید دوستان دموکرات من بخواهند بگویند ما شکست خورده‌ایم. ولی من نمی‌فهمم چطور شکست خورده‌ایم. آیا تنگه بسته شده؟ بله. اما اگر این محاصره ادامه پیدا کند و هیچ‌چیز وارد یا خارج نشود، در نهایت مجبور می‌شوند چاه‌های نفتشان را تعطیل کنند. نیمی از میادین نفتی‌شان وابسته به فشار طبیعی است؛ اگر خاموش شوند، دوباره راه‌اندازی‌شان بسیار سخت خواهد بود. چیزی را اشتباه متوجه شده‌ام؟»
وزیر جنگ:
نه، به همین دلیل است که رئیس‌جمهور می‌گوید همهٔ کارت‌ها دست ماست. و ما بهترین معامله‌گر دنیا را داریم که می‌تواند بهترین توافق را برای آمریکا رقم بزند. و اگر لازم باشد دوباره وارد عمل نظامی شویم، وزارت جنگ هم آماده است
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/11081" target="_blank">📅 20:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سناتور کونز:
حالا دربارهٔ ایران امروز صحبت کنیم. آیا موافقید که ایران چه در بخش دولتی و چه خصوصی الان عملاً با تف و چسب نواری سرِ پا نگه داشته شده؟
وزیر جنگ پیت هگست:
اصطلاح “تف و چسب نواری” اصطلاح دکترین نظامی نیست، سناتور، ولی در کل با این توصیف موافقم
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/11080" target="_blank">📅 20:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سناتور کونز : دستگاه اطلاعاتی ما مدتی پیش کشف کرد که رژیم ایران یک طرح جدید برای برنامهٔ تسلیحات هسته‌ای‌اش یک نقشهٔ بازی تازه طراحی کرده بود.
طرحشان این بود که تولید موشک‌های بالستیک، موشک‌های کروز و پهپادها را به‌شدت افزایش دهند و یک انبار عظیم از موشک و پهپاد بسازند. بعد از آن به آمریکا، اسرائیل و بقیهٔ دنیا بگویند: اگر دوباره مثل ژوئن(جنگ ۱۲ روزه) ما را بمباران کنید، برنامهٔ تسلیحات هسته‌ای را از سر می‌گیریم و خاورمیانه را نابود خواهیم کرد؛ و ضمناً موشک‌های ما حالا می‌توانند به برلین، لندن و پاریس برسند.
آیا برداشت من درست است که یکی از دلایل اصلی حملهٔ ما به ایران همین بود؟»
وزیر جنگ پیت هگست :
«فکر می‌کنم این موضوع را خیلی خوب بیان کردید، سناتور. آن‌ها تلاش می‌کردند با تکیه بر زرادخانهٔ متعارف خود، جهان را برای رسیدن به سلاح هسته‌ای باج‌گیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11079" target="_blank">📅 20:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سازمان اطلاعات سپاه اعلام کرد که پنج شبکه قاچاق سلاح مرتبط با اسرائیل را خنثی کرده است.
۲۰ فرد مرتبط با آنچه آن را شبکه‌های سازمان‌یافته «بی‌امنی» مرتبط با «گروه‌های تروریستی و قاچاقچیان سلاح» توصیف کرد، شناسایی و دستگیر شدند؛ این اقدام پس از اقدامات اطلاعاتی و عملیاتی نظارت بر محموله‌های غیرمجاز سلاح انجام شد.
بیش از ۵۰ سلاح گرم، ۷۰ کیلوگرم مواد منفجره، حدود ۲۰۰۰ فشنگ و مهمات اضافی در جریان این عملیات توقیف شدند
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11078" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هدف جنگ از زبان روبیو: بازگشت به زمان قبل از جنگ
مارکو روبیو گفت: «ترجیح ما این است که تنگه هرمز باز باشد، به همان شکلی که قرار است باز باشد و به همان شکلی برگردد که قبلاً بود.»
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11077" target="_blank">📅 19:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد. @withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11076" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وعده سر خرمن پزشکیان درباره اینترنت :
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11075" target="_blank">📅 18:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">️عراقچی: هر کسی که فکر می‌کند ایران به دونالد ترامپ توافقی می‌دهد که می‌تواند به آن ببالد، در خیال‌پردازی زندگی می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/11074" target="_blank">📅 18:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو
: پاکستان از ربات‌هایی استفاده می‌کند که خود را آمریکایی جا می‌زنند تا شبکه‌های اجتماعی را علیه اسرائیل دستکاری کنند
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11073" target="_blank">📅 18:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به گزارش ایرنا، ایران و عمان اوایل امروز یک نشست فنی و حقوقی با محوریت تنگه هرمز و عبور ایمن کشتی‌ها در مسقط برگزار کردند.
از سوی طرف ایرانی توسط عباس باقرپور، مدیرکل امور حقوق بین‌الملل وزارت امور خارجه، به همراه نمایندگانی از چندین سازمان دولتی هدایت شد.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11072" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا
نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11071" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با شما : به کارمندان دادگستری گفتن فردا نیایین تعطیله ،احتمال شروع جنگ رو دادن
یاشار : تایید میکنید ؟ اگه خبری دارید بفرستید
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11070" target="_blank">📅 17:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عبور نفتکش قطری از تنگه هرمز
در حالی که روز گذشته اعلام شده بود نفتکش قطری MIHZEM  توسط ایران از تنگه هرمز برگردانده شده است. این نفتکش دقایقی پیش موقعیت خود را در دریای عمان ثبت کرده و از مسیر تعیین شده ایران از تنگه هرمز عبور کرده است.
دقایقی پیش بلومبرگ هم خبر عبور دومین نفتکش قطری که حامل گاز طبیعی قطر است از مسیر  تعیین شده ایران را تأیید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11069" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: من رابطه خیلی خوبی با بی‌بی نتانیاهو دارم. ما واقعاً مثل دو شریک واقعی کنار هم بودیم؛ اگه ما دوتا نبودیم، اسرائیلی هم وجود نداشت؛ مخصوصاً بدون من قطعاً چنین چیزی ممکن نبود.
@withyashar</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/11068" target="_blank">📅 17:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
چین قوی است، اما ما از چین قوی‌تر هستیم. ما از هر کشور دیگری از نظر نظامی قوی‌تر هستیم.
شما این را در ونزوئلا دیدید. این کار برای اکثر کشورهای دیگر سخت بود. ما آن را در یک روز انجام دادیم، و حالا به آن نگاه کنید.
به ایران نگاه کنید... آنها همه چیز بزرگی داشتند، و حالا همه چیزشان رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11067" target="_blank">📅 17:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFqgHrmOZmqrx_tTzsh6fOer53eYfERP2a-vf78KPfhIFjJOfFUG9zcoOPGxsOdAQP798Mf4D08M4xNOjX7yAfnfWfSxmyqzEfSXBTQPI8jHOK5QfC7oDwKsUBvetPvfXlQSwT8-DB3xKhFtGR63jy1dvCU6FIGQncgIbHH-F8VVsq8BQXE5e9CWWYUsMYQ5k0wlsvURBgb_B1M0wG35Oaf40Yb0VbeUZoJjqQrWsfE9bspmRz8hIcQQMAI-8MLfelys25yvNNIv5Q7vSpeEbxcdD80MLlLaUE6nal8ZBIE1SJiEOc4o98vJCyq60FxFgoUaFMpMYM5Ee_eEP_sIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدعباس عراقچی وزیر امور خارجه برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
😅
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11066" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: آمریکا در تماس مستقیم با مقامات ایرانی است و عجله ای برای رسیدن به توافق نداریم
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/11065" target="_blank">📅 17:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزیر جنگ آمریکا: ما مهمات و قابلیت‌های کافی برای تضمین دستیابی به آنچه می‌خواهیم در ایران به دست آوریم، داریم.
وزارت جنگ در آمادگی کامل است و در صورت لزوم آماده اقدام علیه ایران است
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11064" target="_blank">📅 17:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11063">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ : انتظار داریم اقتصاد ایران تحت فشار ناشی از محاصره بنادرش فرو بپاشد.
مناقشه با ایران بدون نیاز به عجله کردن، حل و فصل خواهد شد و ایران با انزوایی مواجه است که آن را از منابع درآمدش محروم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11063" target="_blank">📅 16:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11062">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ در مصاحبه‌ای با برنامه‌‌ای از شبکه‌ی WABC در پاسخ به این سوال که آیا معتقد است می‌توان از غنی‌سازی اورانیوم و توسعه‌ی بمب توسط ایران جلوگیری کرد، گفت:
«صد در صد آنها متوقف خواهند شد.»
ترامپ همچنین مدعی شد که در طول مذاکرات مستقیماً با مقامات ایرانی در ارتباط بوده است.
ترامپ گفت: «من با آنها تعامل دارم. و آنها گفتند که ما قرار است گرد و غبار را به دست آوریم. من آن را گرد و غبار هسته‌ای می‌نامم زیرا نام مناسب‌تری است و ما قرار است آن را به دست آوریم.»
ترامپ همچنین مدعی شد که ایالات متحده نیازی به حرکت سریع به سمت توافق ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11062" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر جنگ آمریکا پیت هگسث درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11061" target="_blank">📅 16:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سنتکام
:
ناو هواپیمابر آبراهام لینکلن به عملیات خود در دریای عرب ادامه می‌دهد و تحریم‌ها علیه ایران را اجرا می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/11060" target="_blank">📅 16:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شکایت ایران از آمریکا به دیوان داوری لاهه
این دادخواست بر اساس مفاد بیانیه‌های۱۹۸۱ الجزایر و به دلیل نقض تعهدات بین‌المللی آمریکا در جنگ ۱۲ روزه علیه ایران، اسفندماه سال ۱۴۰۴ در دیوان داوری دعاوی ایران و ایالات متحده ثبت شده است.
جمهوری اسلامی ایران در دادخواست خود که تحت عنوان پرونده الف-34 در دیوان داوری به ثبت رسیده است، با استناد به بند اول بیانیه الجزایر، ضمن تبیین و تشریح مصادیق نقض تعهد آمریکا در جریان جنگ تحمیلی ۱۲ روزه و همچنین اعمال تحریم‌های اقتصادی و تهدید توسل به زور، از دیوان درخواست نموده است ایالات متحده آمریکا را به نقض بند اول بیانیه محکوم نماید و آن دولت را ملزم نماید فوراً به مداخلات مستقیم و غیر مستقیم خود در امور داخلی ایران پایان دهد؛ و ضمن ارائه تضمین عدم تکرار اعمال متخلفانه مزبور، خسارات وارده به ایران را نیز به طور کامل جبران نماید.
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11059" target="_blank">📅 16:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ در تروث :هیچ جمهوری‌خواهی تاکنون درباره کوبا با من صحبت نکرده است، کشوری شکست‌خورده که فقط در یک جهت حرکت می‌کند به سمت پایین
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/11058" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YppqFn-IemNT0fyoGuEcSYqJ6ld6PzcevEfmpQnTY1_eFsjkFnMr_LsMWodr5osmDmtqBwOgAL30J17gGIV6e_lplm68505iUZxKTqvGLYVhzwbBYyQJvRHvGAGZJq9aYPZqrzpM65jRiwa_2mlbmu8923B6By_FA4H3gZRMXwiFdd5iRtsEz-ydN_7xDbNTQUlEr8um8jpimo1WQ3WyZYWMQLwQTtwaOw9RzF9iHS13NdmujDISxEHKwqnBwqPLLrttro21AyxrhIl9P66SzJ7UY4VvPo3UsoT6OrLM3Xtq2-Z65RT_qIjp1dGcKS8olJLoL_ZM-Bac5qV7lnhkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ قایق‌های تندرو
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11057" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11056">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3PSnU3D0jhvNdc4VwB8sW4YeocBgYJ5Iuhyu8gK7xGLu2D6b3p-tOm7JosU0BVbEzMLKIDXi9zBypeYO5gUXLRcNVUTaWZNOU9uWTeKuNjzWTcFh05-WwMpLFprC9a5UdBmI0ZV5YEdmk8juaMzoqpWoR2zwusJCTDurX2Xg5-PyUCCkLsrVqH4IXk6LdaGVTC9H1bSIzr9O8dNaERr4zAY89BaGqEyynPfORKYnYFzb4KWMW9RN-WLmgBsbDmYHAmUJDRp1PPEoWRN4ndFANpsz2mHjiSn3C-HF_ujuItFUTNh6--R3aOyLB6cgPDrihRTMUngNZVZCXKLqKRECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : دموکرات ها عاشق فاضلابن
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11056" target="_blank">📅 15:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11055">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ در تروث  لیزرها: بوم بوم… رفت هوا!!! @withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11055" target="_blank">📅 15:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11054">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در پست جدید تروث، ترامپ طول جنگ‌های بزرگ آمریکا را مقایسه کرده:  * جنگ افغانستان: ۵۴۳ هفته * جنگ عراق: ۴۵۷ هفته * جنگ ویتنام: ۴۳۹ هفته * جنگ جهانی دوم: ۱۹۶ هفته *  گشت و گذار در ایران
😂
: ۶ هفته @withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11054" target="_blank">📅 15:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پست جدید ترامپ در تروث : ۱۵۹ کشتی ایرانی  در زمان باید و اوباما روی آب در زمان ترامپ کف دریا @withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11053" target="_blank">📅 15:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فاکس‌نیوز: در صورت شکست مذاکرات و تشدید بحران، برخی مقام‌های ارشد جمهوری اسلامی ممکنه به روسیه فرار کنن و مقام‌های رده‌پایین‌تر به کشورهایی مثل عراق یا افغانستان پناه ببرن.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11052" target="_blank">📅 14:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932a7cc108.mp4?token=mht4ZCCskhrkGP55AlTCRodb0ovmHmujRJa11TzKxyjaISPsu5S0xi1WdBBPlU4gUn_nRw3Z8BaEnROxPkUJLhw5R9x3L9rYuG5z_Y4Wr7bSnHQtKwJ2972g4hOD153inmB_yeWjRR7JrXBADXmSLfQkUH2jrLYz-GNis5bTvYdjg9trRs_q2TmD6UOZupEzXtxPcMpwD6Ap9PKzkidSTKoELQdwjsZYFTdt6FR6Z-kRqwDyRWDQh9tZBOGbUoj0Tti9OYKywJ-zeXCu2ZW7n6-ir0XfYrksVNqgVI3CE4MwinTbDnjdnX34933P63cAp5HtrvGsqcUOZpXsHX-fQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932a7cc108.mp4?token=mht4ZCCskhrkGP55AlTCRodb0ovmHmujRJa11TzKxyjaISPsu5S0xi1WdBBPlU4gUn_nRw3Z8BaEnROxPkUJLhw5R9x3L9rYuG5z_Y4Wr7bSnHQtKwJ2972g4hOD153inmB_yeWjRR7JrXBADXmSLfQkUH2jrLYz-GNis5bTvYdjg9trRs_q2TmD6UOZupEzXtxPcMpwD6Ap9PKzkidSTKoELQdwjsZYFTdt6FR6Z-kRqwDyRWDQh9tZBOGbUoj0Tti9OYKywJ-zeXCu2ZW7n6-ir0XfYrksVNqgVI3CE4MwinTbDnjdnX34933P63cAp5HtrvGsqcUOZpXsHX-fQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتکش ایرانی که در نزدیکی جاسک، در جنوب ایران، توسط نیروی دریایی ایالات متحده مورد اصابت قرار گرفت، پس از گذشت دو روز هنوز در حال سوختن است.
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11051" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسانه اسرائیلی «والا نیوز» :
دستگاه امنیتی اسرائیل باور داره «مجتبی خامنه‌ای» الان اصلی ترین مانع پیشرفت مذاکرات بین ایران و آمریکا‌ست.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11050" target="_blank">📅 13:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسرائیل هیوم: هزاران اسرائیلی از شامگاه ۲۲ اردیبهشت پیامک‌های تهدیدآمیز به زبان عبری دریافت کردند که در آنها از سوی هکرهای منتسب به تهران خواسته شده با جمهوری اسلامی همکاری کنند
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11049" target="_blank">📅 13:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3ff38bd1.mp4?token=q7Eqjo9hectUprwTcJEclTK1xzFUpysQcxdsVToLkrFEewxDicquaIzChXji82wsMzvejv8KAg8fTIsXlrsmYMwjPY6Pf-_bcnx_zTKPpdTxDPWiUoIaO-QWZyfO2MK1Jj3BoNzCA4E1JWXHXt67DStpLEVj-pYC6k_kYs7Qu5FEEfmenVFxGK7N88A1rB850x6MCStc4iy8xIqcxkD3El-51N1oWm1YIXHZdIqwjulXyBHpBPi_sXLs9Ye5kEKRYlu8F_LE2ZhubI6HAH61RwGzrv--3krvi_9oIs7YINQAxSgAKDHYzNok5IChni-3e97-XAne1jMpL0KxHTa4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3ff38bd1.mp4?token=q7Eqjo9hectUprwTcJEclTK1xzFUpysQcxdsVToLkrFEewxDicquaIzChXji82wsMzvejv8KAg8fTIsXlrsmYMwjPY6Pf-_bcnx_zTKPpdTxDPWiUoIaO-QWZyfO2MK1Jj3BoNzCA4E1JWXHXt67DStpLEVj-pYC6k_kYs7Qu5FEEfmenVFxGK7N88A1rB850x6MCStc4iy8xIqcxkD3El-51N1oWm1YIXHZdIqwjulXyBHpBPi_sXLs9Ye5kEKRYlu8F_LE2ZhubI6HAH61RwGzrv--3krvi_9oIs7YINQAxSgAKDHYzNok5IChni-3e97-XAne1jMpL0KxHTa4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست های دیروز رو ببینید و ویس های تحلیل ‌دیشب رو حتما از اینجا به پایین گوش کنید</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11048" target="_blank">📅 13:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کرملین: ولادیمیر پوتین، رئیس جمهور روسیه آماده دیدار با ولودیمیر زلنسکی، همتای اوکراینی خود در مسکو یا هر جای دیگر است.
به پایان جنگ با اوکراین نزدیک می‌شویم.
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11047" target="_blank">📅 13:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">میاتا فانبوله، وزیر دولت بریتانیا استعفا داد و در نامه‌اش آشکارا از کیر استارمر نیز خواست که از سمت خود کناره‌گیری کند
این نخستین استعفای رسمی از داخل دولت استارمر در بحبوحه بحران سیاسی اخیر محسوب می‌شود. گزارش‌ها می‌گویند ده‌ها نماینده حزب کارگر نیز اکنون خواهان استعفای استارمر شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11046" target="_blank">📅 13:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ :  من نه قراره خسته بشم نه قراره کوتاه بیام جلو ایران ، تا پیروزی کامل ادامه میدم !
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11045" target="_blank">📅 12:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e519f8398.mp4?token=BK-E3s3eoxJuT1UKW1NLECyV-xuv9zrDbf288tW0pObJ8-ocJYh8zAJHHyfOIX_8R8Q0i89wQHTHZUhPXUbWBaOm6QHIwxGUOBPvJ0VzfBYohvhhKvUmaGiWhKTRCBsBwseJZVvLdATb9iosw0S6scL_Z7QW59bzwc8MtFLX3kuPf4ZMvCyDamYqh094EDt5Pf3nutROLtJBvcsu3380tj1i31VgQw5Kb6om1Uwz6QlVRyKD4IZxcdq2JD74_A_dimAnjwJuWEO7Vny8wf4EUjGY6TvpvM2o2-KEn57fsHPVdBtpKqJ3bHymPXIo9XuK-_k71OgOVVucaUTla0TIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e519f8398.mp4?token=BK-E3s3eoxJuT1UKW1NLECyV-xuv9zrDbf288tW0pObJ8-ocJYh8zAJHHyfOIX_8R8Q0i89wQHTHZUhPXUbWBaOm6QHIwxGUOBPvJ0VzfBYohvhhKvUmaGiWhKTRCBsBwseJZVvLdATb9iosw0S6scL_Z7QW59bzwc8MtFLX3kuPf4ZMvCyDamYqh094EDt5Pf3nutROLtJBvcsu3380tj1i31VgQw5Kb6om1Uwz6QlVRyKD4IZxcdq2JD74_A_dimAnjwJuWEO7Vny8wf4EUjGY6TvpvM2o2-KEn57fsHPVdBtpKqJ3bHymPXIo9XuK-_k71OgOVVucaUTla0TIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بار نخود از جمهوری اوگاندا رسید
😂
مونافقو
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11044" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">درود بر یاشار عزیز.  اقا یه مقدار بخواب و استراحت کن.  اخرین پیامت یه ربع سه شب بود. اولین پیامتم ۶:۴۰. جات خالی دیروژ از ساعت ۱۶:۳۰ تا ۵ صبح امروز خوابیدم در هرحال خسته نباشی. انرژی میگیریم ازت باور کن</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11043" target="_blank">📅 12:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">درود بر یاشار عزیز.
اقا یه مقدار بخواب و استراحت کن.  اخرین پیامت یه ربع سه شب بود. اولین پیامتم ۶:۴۰. جات خالی دیروژ از ساعت ۱۶:۳۰ تا ۵ صبح امروز خوابیدم
در هرحال خسته نباشی. انرژی میگیریم ازت باور کن</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11042" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الجزیره : جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11041" target="_blank">📅 11:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شاهزاده رضا پهلوی: جمهوری‌اسلامی امروز از همیشه ضعیف‌تره و مردم ایران آماده‌ن تا سرنگونش کنن، اتخاذ سیاستی درست در این لحظه میتونه قرن آینده رو تغییر بده
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11040" target="_blank">📅 11:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eeaa36938.mp4?token=VsuFGP3VmnnCVmSi-85GjzCsROp-gFQDCVG15qcM4yc196Ido23IQtRS28-KCdPu5U1LbEXKghmq-rxmUMp6xBiobU2xtlUfl6n0Vy9_ZX-o5rd_U85MLBq-_ngUuYDlUVw7hEdOD4MoMFtQmE8L2Vxtf9uyHQpI2fHVZqYAKRegPEixNGSMAV7qsHwIzO-iWeTxWu4K6wq4wB5rJV4Pj_YgPYys5-Tl85e16bBeobXmC43N5xz1Z52JJ4xgIWIBJddtsCEbxVmzDRA6XCvmj-CgpQA5vZBrRUE0tTawBikvCYBDvU6C4BptIiuBTecBDF4i9s6LsFXJ257jT_S4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eeaa36938.mp4?token=VsuFGP3VmnnCVmSi-85GjzCsROp-gFQDCVG15qcM4yc196Ido23IQtRS28-KCdPu5U1LbEXKghmq-rxmUMp6xBiobU2xtlUfl6n0Vy9_ZX-o5rd_U85MLBq-_ngUuYDlUVw7hEdOD4MoMFtQmE8L2Vxtf9uyHQpI2fHVZqYAKRegPEixNGSMAV7qsHwIzO-iWeTxWu4K6wq4wB5rJV4Pj_YgPYys5-Tl85e16bBeobXmC43N5xz1Z52JJ4xgIWIBJddtsCEbxVmzDRA6XCvmj-CgpQA5vZBrRUE0tTawBikvCYBDvU6C4BptIiuBTecBDF4i9s6LsFXJ257jT_S4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتظر تایید خنثی سازی هستیم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11039" target="_blank">📅 09:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منتظر تایید خنثی سازی هستیم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11038" target="_blank">📅 09:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11037">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🤭
😂
😂
لعنت به اخوند</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11037" target="_blank">📅 09:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11036">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با شما : بوشهر دو بار زدن دود سیاه کانفینگم حجم نداره
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11036" target="_blank">📅 09:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11035">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPillar</strong></div>
<div class="tg-text">بوشهر رو زدن پایگاه</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11035" target="_blank">📅 09:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11034">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش صدای انفجار در بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11034" target="_blank">📅 09:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbuaTD-X2lBAv3TrlsZZpTCHUGvZl2PmKOw387ByVXkAPmKcQy2dvIaPutMXdvW7rxgC30PekmvVgPNvVz2UpVXAoS3N8mmE1g5HyElOdYB5qFYA-wC9jVigbbA19UMvHqcUdT5SpS76yXzz7E3jlV-zmim_w0o9FQimJQGgVyzpkbYrXs4xEmg2tG4RDZWb3YSFH9eAf52DMynTgEximytj4GknMKnfXMzJVwIoyys4IUicS4p-mmkJNF0i1WWAp8d1gWYTcfQwOlCuA-rtNIRF0WoHK94TFo5ifE0l7txbZRKCzRQlzl6SAvfHgZNsGuJjR3VtbGlzT-DnL3cQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی امروز در اجلاس امنیتی POLITICO واشنگتن سخنرانی می‌کنه
، در کنار مقامات ارشد پنتاگون، وزیر سابق امنیت داخلی آمریکا، سناتورهای کمیته نیروهای مسلح، روسای کمیته اطلاعات مجلس و مقامات دفاعی آلمان و مدیران لاکهید مارتین.
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11033" target="_blank">📅 09:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Raper Ghadimi Remix (IG @yashar)</div>
  <div class="tg-doc-extra">Reza Pishro & Eminem (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11032" target="_blank">📅 08:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11031" target="_blank">📅 08:28 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
