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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-125096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار الجزیره: حملات هوایی اسرائیل به کوثریات الروز، صفاد البطیخ و عین قنا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/125096" target="_blank">📅 20:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اکونومیست: حکام خلیج فارس پس از جنگ می‌خواهند نشان دهند که در خانه همچنان قدرتمند هستند
🔴
آنها تدابیری شبیه حکومت نظامی را اعمال کرده‌اند؛ ده‌ها هزار نفر اخراج شده‌اند و بیش از هزار نفر بازداشت شده‌اند
🔴
امارات، که میزبان صدها هزار ایرانی است، بیمارستان‌ها، مدارس و باشگاه‌های ایرانی را تعطیل کرده
🔴
فشار بر شیعیان و ساکنان ایرانی، احساسات فرقه‌ای که پیش‌تر در حال کاهش بود را دوباره زنده کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/alonews/125095" target="_blank">📅 20:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrKAFgp7erCPNiEBqeOaA3AP8U5uwRamGeHeJQWRW3B45UF-pdf30PirWrxRNgLdjAfgOYu4WRYCFHY_TOrHNIQsYzyQ0v52RUBDD89PUl1UM0tTV6YanH_RS116kMgRRSZiUh1fX60rOlzLxHrAFi6hR8bKm5KPPXj7Kt6swCcOF0nVI-0iEbk38BU4Ei1AGpAk0snt0bg2cbXz7onayc5SFunRGs4f569MQRtuQSHLk4xTcGalZaX5RY1-YD7ZYPcFA0YS66SiLdiKr_eC9YqsrbTPMajewnq5qQxOChH6zTvDAvQ9lE73VHp2YSoCx85zTpy7CUnXNgxHR5PXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان بولتون، مشاور اسبق امنیت ملی دونالد ترامپ و یکی از منتقدان سرسخت او، با وزارت دادگستری آمریکا به توافق رسیده است که به یک فقره اتهام نگهداری غیرقانونی اطلاعات طبقه‌بندی‌شده اعتراف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125094" target="_blank">📅 19:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125093">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر خارجه روسیه : غرب تو تلاشه تا روسیه رو نابود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125093" target="_blank">📅 19:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125092">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فارس : آمریکا برای تبعه خود در کویت هشدار امنیتی صادر کرد
🔴
سفارت ایالات متحده در کویت از شهروندان خود خواست که احتیاط کرده و دستورالعمل‌های مقامات محلی را دنبال کنند.
🔴
علاوه بر این، سفارت ایالات متحده در کویت سیتی تمام خدمات کنسولی را به حالت تعلیق درآورده است.
🔴
واشنگتن همچنین از تبعه خود خواست که از اعتراضات و تظاهرات در این کشور دوری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/125092" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125091">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
واشنگتن: ارتباط با ایران از طریق میانجی‌ها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125091" target="_blank">📅 19:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125090">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد، زودتر از آنچه فکر می‌کنیم، سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125090" target="_blank">📅 19:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125089">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مدیرعامل مایکروسافت: دیتاسنترهای هوش مصنوعی جدید ما به‌اندازه یک رستوران آب مصرف می‌کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/125089" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihcEe-c_oYix9qDofAFuv4ghnO5muWpZEBu2olsZuYIBO4PTidti_NYUjX1ViwPI5VYTzFhYXXC4MlnZASx-Q2yHImyk1sMX8e7hg2S1IwHrg8pDFGUvQo8dnYEWFaXMuXmhtgh0nIbaBvxR1y3b8TuSnQHFIQXItcuKbsHDcjv2hvEF9jy-seIC87mN4PGQxjqpV8xmiWxKKeOZWTqowOphl1Cn7GfMw_mCscT1Ix0z4mcKTkPdNmaTpWqjO6r6AUOMMbVgdPBwoGMggr_AlRqZcjTXscTuoRUIVqpTBDn_Bh3o-E0wfpa603Lk7y2DriQOUt6c_QhgIWJExT66tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۵.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125088" target="_blank">📅 19:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنتکام:۶ تا کشتی رو از کار انداختیم، ۱۲۷ تا کشتی تجاری رو مسیرشون رو، عوض کردیم
🔴
۳۶ تا کشتی هم که کمک‌های انسانی داشتن رو اجازه دادیم رد بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/125087" target="_blank">📅 19:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/125086" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJ0VaugUsnCQO3VmRDaFm921NPM0DzemhrV1NZbENGoQ79DfMtXsI-Zf4SpKLFQSfrzvEaqJgZZb8thK8cegmLuL6yG8wbfClp1fXZo2mO9jSCevVzwZpd31c6b7FsICz2aW_o9GKPQPtFVdS5SvMtMWXd0M3-FeTu1SWLhbH7frZgYJ1IqyGH1DwxCf9ZtkeUQtl9kdgi44-1yRAn8VX_7KFD1sBxzmoigo8jbcGSM_4iz9ZRIjZLAkdg2lDGx3NcO_iAQ6k7YtyGaNiD3Xui-KxZPJzh_Mx7C8LdNO1V4UTmJlXwWMe_Jc_-XY5iilD-KL7BkIdIbSINe-8cjd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/125085" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=GpGq5QapRz3j9yGE_Pj9gmUJl0bJgWod7wSBBLz3B0miONO7LT-59b62hnHADDUczhIFmg-lKiw3VDMd4gkuI_FKLqtt51Rzu0Tnqv7BEqKRGp8mWK9Z--wUuRLQXsgbSv6rD-gi_ZHAWMG9TJEuwhcLM8eZacg9LIUmIJqx_TycDeB2XBIZ2u1hn3zF0XuDhNb8mABOTMQqXE8XRvZNwJ_PgIc5vXt1y1ZXX_RlmNcdSZVWIxlUSPw1TLCG4dhKZLXxUvvcUah344S8UQVohOF3rY6taeWeDhc5zoVmZXucIJKzLXyrhtPu2lx12YWuTY6V06ZqSLd6RUBaBHhdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bb3a1fb3.mp4?token=GpGq5QapRz3j9yGE_Pj9gmUJl0bJgWod7wSBBLz3B0miONO7LT-59b62hnHADDUczhIFmg-lKiw3VDMd4gkuI_FKLqtt51Rzu0Tnqv7BEqKRGp8mWK9Z--wUuRLQXsgbSv6rD-gi_ZHAWMG9TJEuwhcLM8eZacg9LIUmIJqx_TycDeB2XBIZ2u1hn3zF0XuDhNb8mABOTMQqXE8XRvZNwJ_PgIc5vXt1y1ZXX_RlmNcdSZVWIxlUSPw1TLCG4dhKZLXxUvvcUah344S8UQVohOF3rY6taeWeDhc5zoVmZXucIJKzLXyrhtPu2lx12YWuTY6V06ZqSLd6RUBaBHhdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ،محسن رضایی: برای ترامپ ویلچر ببرید!
🔴
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتواند آمریکا را اداره کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/125084" target="_blank">📅 19:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حزب‌الله به دولت لبنان اعلام کرده که توافق صلح لبنان و اسرائیل که با میانجی‌گری آمریکا انجام شده رو قبول نداره- AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/125083" target="_blank">📅 19:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلومبرگ، به نقل از منابع: بریتانیا و فرانسه برنامه‌هایی را برای یک مأموریت مین‌روبی چندملیتی در تنگه هرمز نهایی کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125082" target="_blank">📅 19:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش گروسی به شورای حکام: آژانس نه اطلاعاتی از ایران درباره وضعیت مواد هسته‌ای اعلام‌شده دریافت کرده و نه به هیچ‌یک از این تأسیسات و مکان‌ها برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی داشته
🔴
حملات نظامی به تأسیسات هسته‌ای ایران وضعیتی بی‌سابقه ایجاد کرده
🔴
انجام بی‌درنگ فعالیت‌های راستی‌آزمایی آژانس در ایران مطابق با توافقنامه پادمانی ان‌پی‌تی ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125081" target="_blank">📅 19:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=CM0w1HDvt2Nc-RPaY87nvTfwlBSeQIuZZR0wLtYGeTnFfo_TNf-xt9XKwVAUmy1zDg3xUVx_1qUp5twfCVUJYRQnPxoSbmJG7hdyBp6RFIFtIQwJBWMXDtqQD5ldW-UayRlfkpFtVrSRgeby5lmvho_UQqSZkWjht-wkduYWRKeOA2Qt_wc46TlZjO65T0u_kaOdO2ODfkjvu0UOXnvoWLGOA6rc-dnFqT49yH0ycjZMi4NuiQLYWqOqB5ah4aHBvnlmqZivC1tnoUoNNI8EZZZWzY_nWWiZUSESzJpvctIlScilBWOvC4ERUIIAKencxt7yR_MtPAbZfvfu8_M8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dff1427f.mp4?token=CM0w1HDvt2Nc-RPaY87nvTfwlBSeQIuZZR0wLtYGeTnFfo_TNf-xt9XKwVAUmy1zDg3xUVx_1qUp5twfCVUJYRQnPxoSbmJG7hdyBp6RFIFtIQwJBWMXDtqQD5ldW-UayRlfkpFtVrSRgeby5lmvho_UQqSZkWjht-wkduYWRKeOA2Qt_wc46TlZjO65T0u_kaOdO2ODfkjvu0UOXnvoWLGOA6rc-dnFqT49yH0ycjZMi4NuiQLYWqOqB5ah4aHBvnlmqZivC1tnoUoNNI8EZZZWzY_nWWiZUSESzJpvctIlScilBWOvC4ERUIIAKencxt7yR_MtPAbZfvfu8_M8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی که از لحظهٔ بمباران مقر سپاه پاسداران تو نسیم‌شهر تهران درجریان جنگ ۴۰ روزه منتشر شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/125080" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knq7nOUsa23ua57slfkZYEfqvC-BNbtzkwGPCnLlobdmMMxTT_TgtpXvUrEAbc82aV4yoA05bL4j3qvZufcn26tpS0MBRqCSmjYKUq2x2IOsQxNkDVlVvulF2S-qwXLYEI1weuy-MFE8CxBjwL256g7ZNC75miItB8ZdK2xSypUUi3V_EHmlumocbv7XDhCmofi73e_G5beEJo6SB4xaGB_YJgVsAlf5LptaidyK0z7WA0SuwR2LkBA7AWrFJ_3sESqmmMuKJ5jFeTJSDQ68POdo8WT6cLqISLWPsfqet5ElyHSAMydWHFyoiZ3w_wNxjtTsrbcqvRt4VjPgWKu2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/125079" target="_blank">📅 18:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار وال‌استریت ژورنال: یک منبع نزدیک به آژانس بین‌المللی انرژی اتمی می‌گوید هیچ فعالیت قابل مشاهده‌ای (از طریق تصاویر ماهواره‌ای، یعنی در سطح زمین) در سایت‌های هسته‌ای ایران که سال گذشته بمباران شدند، در ماه‌های اخیر مشاهده نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/125078" target="_blank">📅 18:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL4CWyZYjXpyenibXznmKoZMS2h02j9eQPXW0NzAgeeWOTQ3uL4rC3BH3E3jB2pN_csHe6kU8r7ki0mSIM7EGmG1uwZ8DRa55UaZnwf43w7UAtM7Py-T8AUAZYb2Ke4svHymvevf6X06VY65FssL6tbIrMQvXKChs8_Ztqm1SH3nkS4zVE8UhNBeu2sniOADztfnCnqFWVYHnUlyI7kdRYOUDiUn7GdPWxsREuwSOi4AQeeC3jfPj7PBT_ByrNVcswnZM2VQmzJLbU9oUtw0UbQtyt_lY1Us4w0GXikmueTJl_YWcxUV8Hg-qedr2f_A1Z_wu1PRXXdEMnTTVfJT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید از آقای قدیم سختگیر تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125077" target="_blank">📅 18:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvuu1x0jfNk3XjpVqXj8MsC9JIxJaKgiQGdou8Ym7_6jHUDS2nK7vjyb_szHy8tbrw6zAi92-3GxRx1ILEZlu0TTP9MttULghl-_tNJVxtBpM113swrzawXeMpe_4n_1u7uyDAZOnRLSrZxYxC2TtAYyvNS5T7jQshOWLaAM4pvEe5fParnLAARJksqXhZkoAR67awuozb9ZXWn_K_9BnArEyd_TSzr2NEyx1IXmRRRlY8sv_mNEV3mN1sJvJ4_9ZSZLgtLVkXijX7SufCSlyLGuPMZ5Y0womkKYGOz-h9gfwahNjq-QEeAkKCthZ5bcNhYG0XDPMRH-m96EWzu66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس صداوسیما: به نظرم جنگ تموم شده و دشمنان دیگه جرأت حمله ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125076" target="_blank">📅 18:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7OlSbAyWQ2PMfOyIzLyK2G36i8IeuioHBftA6Bce7NJJQ6wwNvhAvkEgrC0kuZREmFLGzntvcUcr787U5cyKGGRxd3u8nqPeORV_oMvR1aVX654KMFnTo8cIzCgegTIBefvBv0z_xBaUnJdJPDOSHBSya1N2w3rWdmPZKP7IcdC5lGkSNXZMwwljeKUVjcoA0V07xx1xu64Dv08FvHYQSe8vER3iooGI1JhB-uZgEOrg1M7Y11KB3AVSkQKvEgf4lASmc46b4FEONh_D5SVotHNKY6HcHjp7lO8PCv7AcpgUyqZVZb9JHkxrT-y-oK27uZ2JuLAMkmyvuK9gNNGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
🔴
برخی زمزمه ها از رفع فیلتر یوتیوب نیز درآینده نزدیک حکایت داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125075" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYtyuRv5FMCcRESmeQSmwsalu8zRd9KNQMTKrkihJPXDouZDUvjqGRV_GAOha8bM5xoRN_azXiwj0T1g3sc5VyhjX25-acz0YDxOdfQb4lL52GAKS_XeRUUUUXcEMb_oQVYH01L3JmxTQlUlcOEuWQ5f1XvMZePPpH7ph5S45yDsxcdejJbeZ4jp6dWItTbKHc2LP-wi9oNkkw1KAIlUC394rMgenGqy_qp7DWML91LFR5vwIlNMzw3HkUGwe_sxmGxlqs4tr13SRQdJx0JZ_sYkU7zy2bstC84yve5in1BrqU0DB47ES875MjbILwTS0oquY5br4q9s9hnsuMaLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125074" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه آمریکا: ارتباطات با ایران از طریق واسطه‌ها ادامه دارد و پیام‌هایی بین دو طرف رد و بدل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125073" target="_blank">📅 17:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
🔴
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125072" target="_blank">📅 17:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=v-dxUilDhSVhkYK6FMpXgspNg0gTjNIuynP0QFLhjxhl65QqEXn1C0B7m0fNob3YQjm2QXqLC9qqSr2EkF-2hGmcwKAMRCee266jQMl8pKYqlpbtyrGL-dYeV-DPvg0bhpiLWchCpVeK1zvnWif_DlGb3BlJNNHD0ap2ggOWgz2Qv19Y2kmB4Bd5fSiuenEEqOcSaYnhqJgDIpz0buRfLmu3ggWk3wld62MHMlUaoNonPxZL6ZjV2Ku_56QnSKrHBGlYcSTbXwrGgIFrDSCbtVCISDaLxZA_CapWLKPUgY2xCxbcu2GuzYTef-Y6XfcUkDIeinHUyKmNyRL6dzdHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=v-dxUilDhSVhkYK6FMpXgspNg0gTjNIuynP0QFLhjxhl65QqEXn1C0B7m0fNob3YQjm2QXqLC9qqSr2EkF-2hGmcwKAMRCee266jQMl8pKYqlpbtyrGL-dYeV-DPvg0bhpiLWchCpVeK1zvnWif_DlGb3BlJNNHD0ap2ggOWgz2Qv19Y2kmB4Bd5fSiuenEEqOcSaYnhqJgDIpz0buRfLmu3ggWk3wld62MHMlUaoNonPxZL6ZjV2Ku_56QnSKrHBGlYcSTbXwrGgIFrDSCbtVCISDaLxZA_CapWLKPUgY2xCxbcu2GuzYTef-Y6XfcUkDIeinHUyKmNyRL6dzdHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125071" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ab6bf7d8.mp4?token=C4mWyklxzuo_F8Xb-Biw2vzD9oeISHXLhPDILPfF2qt7wgLLrA5yzBEWuk8NdCr0NI35qIoFnsD_je8T_IW2GmYypTli5cJABHXd4llDF7Q1Sc5Q-QgnZRWriecIyG3X28sl3uTvIGgLX9qtkGKTE03SCueJxMxtmOxDwBFwdUHctCxyL9dp1mP602v_4MWd3M0sDBxf9UiWA3z2Tq84t9tTtFxSa2OkKtqDX9kDECGwxxtjiNI09QXrZIUMQkAteqvztNN_q7baE2swZe_66gp6bf9WlPGqyc2r1brVOD4DEcpL_ONDMcxY8ko9OB_e40IY7sPVSdT1dGoDWTAhdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ab6bf7d8.mp4?token=C4mWyklxzuo_F8Xb-Biw2vzD9oeISHXLhPDILPfF2qt7wgLLrA5yzBEWuk8NdCr0NI35qIoFnsD_je8T_IW2GmYypTli5cJABHXd4llDF7Q1Sc5Q-QgnZRWriecIyG3X28sl3uTvIGgLX9qtkGKTE03SCueJxMxtmOxDwBFwdUHctCxyL9dp1mP602v_4MWd3M0sDBxf9UiWA3z2Tq84t9tTtFxSa2OkKtqDX9kDECGwxxtjiNI09QXrZIUMQkAteqvztNN_q7baE2swZe_66gp6bf9WlPGqyc2r1brVOD4DEcpL_ONDMcxY8ko9OB_e40IY7sPVSdT1dGoDWTAhdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سه تا موشک حزب‌الله که به سمت شمال اسرائیل شلیک شده بود، رهگیری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/125070" target="_blank">📅 17:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.
توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره.
دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه میشن، می بینن دو تا دختر 7 و 15 ساله داخل دستشویی حبس شدن.
با اومدن پلیس و اورژانس معلوم میشه توی این مدت پدر و نامادری‌شون تا سر حد مرگ شکنجه‌شون میدادن!
یکیشون فکش ۳ ماه بود شکسته بود، اون یکی دست، پا و دنده‌اش، شکسته بود. رحمِ دختر بچه رو سوزونده بودن!
به بچه کوچیکه انقد غذا ندادن مثل چوب بستنی لاغر شده بود. انقد موهاشون رو کشیدن که مو روی سرشون نمونده!
کل بدنشون جای سوختگی بود. دکترا گفتن هر لحظه ممکنه بمیرن انقد عذاب کشیدن. پدر حرومزاده‌شون بهشون تجاوز کرده و برای اینکه معلوم نشه آبجوش ریخته روی واژن دختره!
این پدر و مادر امروز دستگیر شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125069" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">امروز عراق با اسپانیا بازی دوستانه داره و جمهوری اسلامی با مالی
😐
@AloSport</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125068" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی در تبنین، جنوب لبنان، پس از چندین حمله هوایی اسرائیلی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/125067" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/125066" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCTg3RSJjPrdo1rlRcUJm8j7W3t5m3ujdVyHdv-aPK1hVn33_NgQ2u317YP_B7XSYbato3an0ZD85JCrLTHFkPG_dTMVZnwHySJtAZGusneq0QsEhFaizuWHc9u-dSXQ5kzRRFTQ_ewHmKeYzvZgN-_mzn7pq6XMuG1MvR73SXQeIqgqVadl3IrBqPAIjfhXZWhZu6aOQ5m2YNU4sNYFjhjPuskiqqHUrORjlTPaFoHR6aqG3FcnGfNXE5hJfZi_9YO0p0G18_IlzyUZ_gkJfNN_YCigXyGNgo3IwcJMmggDsRCoarJWB0ilvk3qvuQ8SK30eCFNeBg2NQYq1LepSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/125065" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از توافق آتش‌بس لبنان و اسرائیل کاهش یافت
🔴
قیمت نفت پس از توافق آتش‌بس بین اسرائیل و لبنان کاهش یافت، زیرا امیدها برای توافقی گسترده‌تر برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران افزایش یافت که می‌تواند به بازگشایی تنگه هرمز منجر شود.
🔴
معاملات با احتیاط انجام شد و کاهش قیمت محدود بود. قیمت معاملات آتی برنت ۱.۱۴ دلار یا ۱.۲ درصد کاهش یافت و به ۹۶.۶۷ دلار در هر بشکه در ساعت ۱۰:۲۲ به وقت گرینویچ رسید، در حالی که نفت خام وست تگزاس اینترمدیت ۹۰ سنت یا ۰.۹ درصد کاهش یافت و به ۹۵.۱۲ دلار رسید.
🔴
دو قرارداد روز چهارشنبه حدود دو درصد افزایش یافته بودند، پس از آنکه خصومت‌های تازه در خاورمیانه، از جمله حملات ایران به کویت و حملات نظامیان آمریکایی در نزدیکی تنگه هرمز، روی داد.
🔴
جان ایوانز، تحلیلگر نفت پی‌وی‌ام، گفت: «ایران بر توقف تجاوز اسرائیل به لبنان، یعنی حزب‌الله، تأکید دارد و به نظر می‌رسد واقعاً پیشرفتی حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125064" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125063">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رسانه اسرائیلی i24news : یکی از پیشنهادات مصالحه «صندوق کمک‌های بشردوستانه» برای ایران به مبلغ میلیاردها دلار (من شنیدم ۶ میلیارد دلار) بود تا دارو، غذا و مسائل بشردوستانه خریداری شود - تا کنون ایران این پیشنهاد را رد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125063" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ۲۱ درصد افزایش می یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125062" target="_blank">📅 16:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPMp4oIgC66a9qLuSGJj53PLwJeS5I61i7ZfcESGPIvs_gVYya5Tly4eslSJf8c4j5CBqyQvUU3Tb4eSdZ_SNIo_NricPei0Q3TQLopMN7z_p0cxbprHNmpkmaEOvDMW7hUfL0iEPTqQDiC0MG1DPxgtXZszco-bc4NQz_pmN3LAhVwfdprREk8QHsunZZ73cqvwJoFb3P_KGgDws-EcqPgGmFQ1kqCIKLhC-XnN6El1ZQETmCQeQrznWCApSL4xlhGCzeWiI3G03KXjFfK5wUPebyUDynuQx9z04vR5qO-ihDNP0cmAYvqBAVBPnAQfPxtjsxKxdex-Gp7ANC10Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مراکش در حال ساخت بزرگترین استادیوم فوتبال جهان، با ظرفیت ۱۱۵,۰۰۰ نفره
🔴
نام این ورزشگاه «گرند استاد دو کازابلانکا» هستش، با هزینه ۵۰۰ میلیون دلار قراره ساخته بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/125061" target="_blank">📅 16:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بریتانیا و فرانسه برنامه‌های نهایی برای رهبری عملیات چندملیتی پاک‌سازی مین‌ها در تنگه هرمز را تکمیل کرده‌اند که ممکن است ظرف چند روز پس از توافق آمریکا و ایران برای بازگشایی این مسیر آبی آغاز شود، گزارش بلومبرگ.
🔴
ائتلافی متشکل از ۱۵ کشور نیرو و تجهیزات برای این ماموریت اختصاص داده‌اند، اگرچه استقرار تنها پس از بازگشت حمل‌ونقل تجاری عادی از طریق تنگه آغاز خواهد شد.
🔴
مقامات بریتانیایی و فرانسوی معتقدند که تلاش پاک‌سازی مین باید توسط ائتلاف مدیریت شود نه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125060" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125059" target="_blank">📅 16:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رهبر حزب‌الله، نعیم قاسم: مذاکرات با اسرائیل بی‌شرمانه است
🔴
تا زمانی که اسرائیل در لبنان حضور دارد مقاومت ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125058" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ادعای موساد به گفته کانال ۱۲ اسرائیل، سلاح‌ها و مهماتی را که از حماس و حزب‌الله گرفته بود، به کردها منتقل کرد تا بخشی از طرحی برای سرنگونی رژیم ایران باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/125057" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125056">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJfhLMk-1c3n_C2UyUixck1p0tbHUoPS1OIL8k5E0OcWuN7iEL1jKOkirZlxLfb2GZWt18gojV970xCmQbpAnboQx0uqXIJutV_gdTj-SRyRX9DDhsCs338683gYL0Mnz6Q1_isKw9ohn1hLVifFZyJRkkeYFYy6ttgs6TdHpQZfmeVibMItFxZo4q3FHnUlse5EqeSN36g7VJrTvQQhIjCKk5pH-IxvTzHXUroF_lmEo4LRxGDqTd51Py5PbhJcbRG9JC6B-2tHnD4fs0j4KWZb5HKJiajN_YyBIBR3sSfAjcDK3PsGB7eGu2NNmEn-cjV0N9Ic3iBNoEzyCofL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی دقیق کمک‌های مالی آمریکا در عملیات «خشم حماسی» توسط USAID
🔴
ون نگوین، بازرس کل موقت آژانس توسعه بین‌المللی آمریکا (USAID)، اعلام کرد که این نهاد برای تضمین «شفافیت و پاسخگویی دقیق»، هرگونه کمک مالی خارجی مرتبط با عملیات «خشم حماسی» را مورد بررسی قرار خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125056" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاتز: توافق کردیم؛ اما با آزادی عمل کامل برای حمله به بیروت
👈
وزیر جنگ اسرائیل جزئیات تازه‌ای از توافق با دولت لبنان فاش کرد: ماندن ارتش اشغالگر در منطقه امنیتی تا «خط زرد»، ایجاد منطقه غیرنظامی در جنوب لیتانی و آزادی عمل برای حمله به بیروت با چراغ سبز آمریکا.
🔴
ارتش اسرائیل به هدف‌گیری زیرساخت‌های متعلق به حزب‌الله در لبنان ادامه خواهد داد.
🔴
وضعیتی که در لبنان تحمیل کرده‌ایم ممکن است در آینده به توافق صلح با این کشور منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125055" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzBjo0ZVVuIvCtUlbNg0gqtx9v5KMY3Hly3BynlGlenJy6eniYOV05tJxngNGdDBdBXuAnkrJc2T7UkbvV80FQJON0s_dQAkQFcGRo9ft4BCH28AbH1gA-YCgFOt-dS1MKwoYBi4cVhLvMD2fLy-1MSULvlNHqfp9DIfN_9FYJ1TuREmb09wF49tkohqiMbp4ieElEHbpFhfUFOhMZjSQQwU501UfVPLjWoTZMtr6TgFOhWzIFeqEkWbSvsPXziKy6M_YuqY459aTCijFLrQAFmBs63Ir12qfgjfdJZ4r45Lm7txWrqOrAqs_Vu2kiOCH8hdeTZmGGTiagR6DBkVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: کشورهای حاشیه خلیج فارس در حال سرمایه‌گذاری در خطوط لوله، راه‌آهن و تأسیسات ذخیره‌سازی هستند تا جریان نفت را حتی در صورت بسته بودن تنگه هرمز حفظ کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125054" target="_blank">📅 15:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ: دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125053" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قراردادهای آتی نفت خام برنت و نفت آمریکا با امید به پیشرفت در توافق صلح آمریکا و ایران، بیش از ۳٪ کاهش یافته و ضررهای خود را افزایش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125052" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیروهای اوکراینی به یه شناور گشتی کلاس «Svetlyak» در کریمه حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125051" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
۲ عضو شورای شهر ایلام با دستور مقام قضایی بازداشت شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125050" target="_blank">📅 15:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No9ydGBaitVvaUIB3a3Ei75flpfSTM94Uze_ToGS0Lh-xjUw1ntGEiKGGXDqmounCTOT4ii5qGiBZ-yV4PYTMd0NRplyJgZBYxGaOJkxVM8GKXLrxMlazEW8yOQcPD_PaG50Pk9lWxVRhQ_x1XdlpQ0999TnQrXgbMkH_NmJ0SYk7gAGB8o0LLQdmsnZg42ksK0oSl9plbFYH3Cs_yIAP_vzybt0OfHreqL8QiaJKKHZ9jU5lqTRI1M08xrBd6InYvt9d5y6Z4Qxw3yO5x3teBXt9UEL3dJFu-VTBVCfbmmQjRCa0_syPe-DC-v4VHYX62tNPGj6D3ibp790Kny5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکسی از نشان‌های پلیس و اصلاحات با نماد جمجمه به سبک ترامپ منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125049" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در حال توضیح‌دادن این موضوع که طول استخر کاخ سفید (از پروژه‌های محبوب ترامپ) از ارتفاع آسمان‌خراش‌های معروف دنیا بیشتره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/125048" target="_blank">📅 15:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrMVZIKv7XbulS_JFltFz6YV8XKJ1ljp6RUoRrh0bxzXRmA6Vi4SriM0gsribSu913UavXo_HcBguxkIcKX8Qhzj02Yn-S84BRmfGq3RUbx2I5KjNb6aQDnLSGbUNULKe88rB0b3ghkzHd7uzkOu3wRJgPCjGs7E23wCJGUR8urw3pggAv48Zy0l_BoRvNMF0jjt-kMLxj5s0fGCpk5LAVDHrBhrrJJG3udVaBPMhUFOqR2jZCCqfr090lnkvxeIJ1dNzPLPByyXgZm1876_4GS3N8_gUZDQcoYJjeE9I_Xl0EG0VG7qOAu9hsNG03h4tJcNPWpg306OngKbM-1lNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار پارک ویژه آقایان توی قزوین راه اندازی شد!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125046" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به ساختمان‌هایی در تبنین و حاروف در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125045" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQvrHYQ0LEbL8zBJbUKVo80QHFVr0RNAnq8-5QW-ZMewqY9ZzGDfThf5wX9t-f0aQDTuFBNSjwg48poeATc_xwTv7gscWmoSy4-ffLjsVEHg2CKei1Jr2Pdv044Va4AzaDCBwpcDvZFfl7-ghCngyU_w2z2flv2JMpsQbENa1j6f-Q4vB-CrqiNc0HSb-4SPxlw4exBt8l3HSw7BXtFBzsQP-rjHQRC3kTf-PEzq8P1JX7jL0c0KBBZZJugaRjM3QfHzeAMu8r_5PufuUENxWeCAShZ8eyr39Sbwpe_KEe8E4MJDaOV05qweRnQCZpN5N1NT31iz7yj1L_rhrz9QdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش دکتر باز شد فقط با گیگی
8
فقط برای الو نیوزی ها با کد تخفیف
🔥
Alonews
همراه با لینک ساب
🔗
و مدت زمان 30 روزه
❌
بدون هیچ ضریبی
❌
⚠️
ظرفیت به شدت محدوده
⚠️
📥
جهت خرید سرویس کیلیک کنید
📥
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125044" target="_blank">📅 15:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فیفا در آستانه آغاز جام جهانی ۲۰۲۶، ورود بطری‌های آب چند بار مصرف را به‌تمامی ورزشگاه‌های این رقابت‌ها ممنوع کرد؛ این نهاد پیش‌تر اجازه ورود بطری‌های پلاستیکی شفاف و خالی را داده بود، اما با اصلاح آیین‌نامه ورزشگاه‌ها، این مجوز لغو شد.
🔴
دلیل این تصمیم مسائل امنیتی و جلوگیری از خطر آسیب‌دیدگی ناشی از پرتاب بطری‌ها و سایر اشیا به داخل زمین یا سکوها عنوان شده است. همچنین ورود اقلامی مانند قوطی، لیوان و شیشه نیز ممنوع خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125043" target="_blank">📅 15:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اسکای‌نیوز: حزب‌الله توافق آتش‌بس دولت لبنان و اسرائیل را رد کرد و نپذیرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125042" target="_blank">📅 14:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-2S7oYLpf3tG4IrbPINR_zHbZbQnMOnyhqQtp4AN7Y5zHGLtkewVnHH-l5jDRZ2tBE4kE4X5harYlBGePbsaZ1fnBtEWL7QS6Gx-pibF6Lff5Vqj_4hR8lHrqNo6nx4qx7PTSYmg7llPEHqo827-FbnA67iSn1QsP_3_s5gthwjgBNLEMxZXr7PAMsH_T5LrEyaQx0NyFWAo0OpmPCaYk99LpkoiYfzStlz61yVYIwxtRq-av4LIZTOZZ4hzcy1v-y1qdI6EMPj6jbdu21mhfLZvPd5bF4dJZWOFZ6RJYfhfnVdlNNDnDmKVj_7bG0vk-gEeLBtfGsdPQDEGfGaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ:
دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟
🔴
آنها می‌دانند مذاکرات در چه مرحله‌ای است. دموکرات‌ها با سندرم اختلال ترامپ سوخت‌رسانی می‌شوند. آنها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یکی دیگر از پیروزی‌های متعددم را کسب کنم.
🔴
چهار جمهوری‌خواه، داستانی کاملاً متفاوت است - آنها فقط نمایش‌گر هستند! آنها باید از خودشان شرمنده باشند. ماگا!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125041" target="_blank">📅 14:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X52UjX8Uj8yMvhz47YeoPkXgOWMnEXks2wKz4lzOVkxzh0PWvr4owJTZJT8xmxyOOZd4wu-XgUY66aou9rIxpxO6ce2HwqNaLQ2FgzSjqdw8GG8ZWNZJm8WbwLJrJ1_us7AFrhhVbOirVYffBSVqoNGFdZo0ASLATJeHnUnW-iSdCvSTur-KjKkGZ70R6mkPJarYPCWFk3M8rNqaS3h3YrMhcKAVAC7X5Jw66XHUOOKoEP0sYEKf-FgDCMCiyrhvFtQo97gV4a2K6itW1Qj7yRC7U2ZaR4i1VdRk2X5niLdsoE_ENWIE0SCoWfRZloTQr_T2uig0TW918s24KBMI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارین پالیسی: جایگاه متمایز آمریکا، چین، روسیه و بریتانیا در صحنه جهانی
🔴
نشریه فارین پالیسی در تحلیلی به قلم برندن سیمز استدلال می‌کند که اگرچه ایالات متحده و چین از نظر اقتصادی و نظامی بسیار جلوتر از روسیه و بریتانیا هستند، اما هر چهار کشور دارای ویژگی‌هایی هستند که آنها را از رده بعدی بازیگران اصلی در صحنه جهانی متمایز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125040" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7vkqkslq4sD6OMKFExsWOLQpY_RE1Zf4RmEcVjtm2_GQ-Qb96W9HwUw3pG3MKSAT4MvHOPgWCNUjYlTFZcDpbCt22p6D9l5r404zdnrl3rOT8430OWQvcGtusMtLZUAmhtgHp_jpN8UGQ9eeR2toTt3rrDAKvcqOtnOFHP0h5Mktwt3J6vehoay2rgT403W_z624ukCVLoM4IqYh58jrEPFDHDrRKyUgNltZIzlLb6rP4Nnfvn6kxXqqIpHaFuBby4K-xZLUcf5fKUB0MV593c-ZA52UEYTlePvaXfwuC3izg-PgEej0PIMtaj8ubthFdLPOpqk5Ofi9Xz5MFku1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش نشنال اینترست: استفاده ایران از موشک چینی برای سرنگونی جنگنده آمریکایی
🔴
نشریه نشنال اینترست گزارش داده است که به نظر می‌رسد چین سخت‌افزار نظامی در اختیار ایران قرار داده و ایران در جریان عملیات «خشم حماسی» از یک موشک چینی برای سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125039" target="_blank">📅 14:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
چت جی‌پی‌تی، دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125038" target="_blank">📅 14:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تسنیم: پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125037" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAXAqfSXSiV7_P0cM6USkak7U9FR0MKXAf6rzlWii5Mo9dfRoZ3SAiZ9Kd19KSYKeY758q79FJTMxwAjFQYgMH-Q6AX5DyMq63-7xtdqrn3Q-YCpe5YwguIQN7PyvoxKEUKT3rIUR6Ku9u-_LvdsqspoVlqNguZ81vYEusC5nUmyP9BZ-ITcQ9neygskY7rpU6X9nbpdQADuXPxqJdHxkUiaK7jTBVa6jH1368JbQAbiejcSU65oqgsp6_bT9qC2EOSp2ZwnWqp2ESl-gYyHv8nKnL5OJzo0YwFcvPGj0fo7_9XmM9qPK0vXoX_0mr8w7QEQdISk2Ungqp77gFwM0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125036" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نخست‌وزیر آلبانی، ادی راما، در برنامه CNN با ایسا سوارس درباره تنش‌های پروژه پیشنهادی جرد کوشنر برای یک مجتمع لوکس ۴ میلیارد دلاری در خط ساحلی محافظت‌شده آدریاتیک به شدت واکنش نشان داد و گفت «هنوز پروژه‌ای وجود ندارد»، و گزارش‌های منتشر شده را به عنوان اخبار جعلی رد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125035" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDoB1RaRJgjtqvOgulExO6smSdgcoecMjA4Wz7hDUI7Ub_S-WQbwxwSIeH9kSAdS6TMw-SDHOpALrpy_DqUvzuLQ4Bhse6rWksXoJIyjtKhxpOXwMRnr_9P_Hwp34GP78mCDa_0JJdHI3DL5vy0x-lexrGNh2czzm0QwFBvN-2wBmhm8Ybye4-CHoGvZMp9oPM2daqNiIkSGQd0CFnBsQpIiKt-k5rhag6kaVC0OyIofdhtOzrd04PRDm87e1C1S3jlEh1N3rjiGVryKE3XJR6g6uZSvSPSPweGeitAiSoQ2G2t67DFuYFq2QCJQLx_zhBFcP6bxyL7Kbj0jI_x3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125034" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
🔴
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
🔴
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125033" target="_blank">📅 14:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم جدیدی از حمله هوایی آمریکا و اسرائیل به پل B1 در کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125032" target="_blank">📅 13:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل : لبنان و اسرائیل بر سر لزوم توقف کشتار اسرائیلی‌ها توسط حزب‌الله و عقب‌نشینی از جنوب این کشور به توافق رسیده‌اند.
🔴
لبنان و اسرائیل توافق کرده‌اند که ایران هیچ نقشی در تعیین آینده هیچ یک از طرفین ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125031" target="_blank">📅 13:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آموزش و پرورش: اعلام برنامه امتحانات نهایی کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125030" target="_blank">📅 13:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : کابینه امنیتی اسرائیل امشب جلسه تشکیل میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125029" target="_blank">📅 13:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آکسیوس به نقل از دو مقام ارشد آمریکایی: در حالی که ترامپ می‌خواهد جنگ در لبنان را پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/125028" target="_blank">📅 13:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ادعای العربیه: مذاکرات پیرامون دستیابی به توافق برای آزادسازی بخشی از دارایی‌های مسدود شده ایران به مراحل پایانی خود نزدیک شده
🔴
رایزنی‌های فشرده درباره نحوه و سازوکار آزادشدن این دارایی‌ها همچنان ادامه دارد
🔴
اصلی‌ترین گره و مانع کنونی در مسیر مذاکرات، به سازوکار و چگونگی مدیریت و استفاده از این اموال آزاد شده بازمی‌گردد
🔴
پیشنهادی مبنی بر تشکیل یک «صندوق ویژه» جهت واریز و نگهداری دارایی‌های آزاد شده ایران تحت نظارت مشخص، روی میز مذاکره قرار گرفته و در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/125027" target="_blank">📅 13:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125024">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Egv1R5ADV5zfKHiBz_awxXIIDoHpdurHAzdRSQMziESvyS2FydFvNkf07jZ0fr7WPlMneLj12gBwymW15qNouFnD2inN5caTUL3i1xCZuoT4lK6CgvOMlEhOAMOnj_-5X2uZkpqKaRFwLzxRBpzQfEfHDcCid6OUywXqUw0b9dh-8S1mP0vIzm0EfMtUMAI2ZnxIlvCGYSZ7K5laSU3ipQG54S_VrNAeP4kR4ZhxN4f3MuvtR_IhqlbRAzt9hYkrI5FYaPyzMPcA_7UacBiEZuDofw7wo0xVnJHWZhiG8ieH07g3Sy3f9Ixbp9irX7wSpGUXEaX7aD0REkOo-JNtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpOq0MexkTLYGCfLwtp48mbbxE9WYXjTJTLXLmx2eNTtojGDG2ooPm-0gcTBcepAzL86hzUrj3w582m09-qWBJlJp-ORGhT0DIbRot91jBfypcFgMhMSZ8rw4ffalqeKHrR2jyjikjl9LxCT4tiQlMtT6ufswlMrii74z_FYY0R5ju8Ed-HvgAUUsF_HNU3jOMMg1eTOwtmGz--DfMMzPf3EIPFiA_7922RvVh6HD-iNIqvkTr1JYIcl39-6Vi9mHJcYVj9kqJBtFR8ie57ACsZZTSsw8Q_r9Iz0upxXaiULvl1Y7oxs7NUlI3Mqk3Slwe8mRAYrRw2URwPvmnWzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pU5MPV8GLjkX-S2OIEudpuKuZS71esisU0QnAvx8nvwvrSgTc-p6ve3bV9Y60QmJlm8r-GU2KnYrWQXgADs2FpxIeLGe7kJXnmYszwT3dqNe4LlUqMs2TY9Sar5RPLRQGw_aY6azZN1Beb104ghuR_D3C_ouZ9WV__fApfQpF2kX20iYwa9Oqic5i7wgWQoBPiH1jkldkxXxaGQamwoqg_KevFo3e-YEc6VhNpXTtJhpa8Ycdt6__z4ioqyRJk3C6UfbiccN8dXkZs26NqMurLIQ6CmTPTQblG75N_ZlcpkhZXY9cZ6UuVe1I5-2sdXG0Zt8J71W1_uGSP3eNhBRAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به تبنین و نبطیه الفوقا در جنوب لبنان انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125024" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=X4HnMyM2LQPGRYgNZP46btPiTMN0tSdg2UD-NP5MfA4TVRnX25E5d-JPFvB0ZgNuxtfWCzwJHziDoGWOwsJKQqhk5Qz58-zV4lWNNwjVk5_ASHH39rC6nWrnO0EfEEA6MED0AD_JOsMsR-D5ez6WuKuRFAg-i3hhkcZ2Mg-W6q0qQtPU00eJjMQC_5vkoNB-I9fqnBH5RzdnFedpU0cH6M3QCYErq7fZ8ob4EspgjaAh2XeS05X8Yi547ZqJtJIKXDYMxNiR1v2MT_dlI0Vz3r5IRJBEbgRW2QtXPdvggg8YiFrKtr5hNm15LbHLHqH0Tq6FS_VMKAPUv1EjEin1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=X4HnMyM2LQPGRYgNZP46btPiTMN0tSdg2UD-NP5MfA4TVRnX25E5d-JPFvB0ZgNuxtfWCzwJHziDoGWOwsJKQqhk5Qz58-zV4lWNNwjVk5_ASHH39rC6nWrnO0EfEEA6MED0AD_JOsMsR-D5ez6WuKuRFAg-i3hhkcZ2Mg-W6q0qQtPU00eJjMQC_5vkoNB-I9fqnBH5RzdnFedpU0cH6M3QCYErq7fZ8ob4EspgjaAh2XeS05X8Yi547ZqJtJIKXDYMxNiR1v2MT_dlI0Vz3r5IRJBEbgRW2QtXPdvggg8YiFrKtr5hNm15LbHLHqH0Tq6FS_VMKAPUv1EjEin1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها بین نیروهای دولت فدرال و واحدهای امنیتی وفادار به رئیس‌جمهور حسن شیخ محمود و نخست‌وزیر سابق حسن علی خیر در طول شب در موگادیشو، سومالی ادامه داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125020" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فارس: فعلا آقا رو دفن نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125019" target="_blank">📅 12:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: نتانیاهو دیروز یک جلسه امنیتی محدود برگزار کرد که در آن ارتش طرحی را برای یک عملیات نظامی گسترده در لبنان ارائه داد.
🔴
در حالی که کاتس و بن گویر از اجرای این عملیات حمایت کردند، نتانیاهو به دلیل فشارهای آمریکایی نسبت به آن محافظه‌کاری نشان داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125018" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125016">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=o-Rrp6JXAu5_n84kkRMQo4AYM_JLn-2ARLcUtKd3ycNRAiTWJxh4cDhDYrFHxefqmPjXn_cu1ykutfSB799Pr695FNGyKD8qyKBsuIugY3CEl5eBaxqSCmbiii2tfNt4XZQjVdPErmembQrUkG_OmkOlg2V6iMvEaSdgLPZ9H5rol0ISOiLnYiPgj610qgyegu-CoNpLKcU-O4AUUIrRgwNynOXAoInEmQP1gDZ4gaKaTOoudXXmoYf8s_rG6TM5nM5Wi8loF6tWNan3Uc4E2fcLQBuBAWq_v5VC0vhiYbSSZ8RzjKg_TChKTFG-_AFWnUgC1ORBdZtW3iKesxDptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=o-Rrp6JXAu5_n84kkRMQo4AYM_JLn-2ARLcUtKd3ycNRAiTWJxh4cDhDYrFHxefqmPjXn_cu1ykutfSB799Pr695FNGyKD8qyKBsuIugY3CEl5eBaxqSCmbiii2tfNt4XZQjVdPErmembQrUkG_OmkOlg2V6iMvEaSdgLPZ9H5rol0ISOiLnYiPgj610qgyegu-CoNpLKcU-O4AUUIrRgwNynOXAoInEmQP1gDZ4gaKaTOoudXXmoYf8s_rG6TM5nM5Wi8loF6tWNan3Uc4E2fcLQBuBAWq_v5VC0vhiYbSSZ8RzjKg_TChKTFG-_AFWnUgC1ORBdZtW3iKesxDptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان فتترمن: من همیشه به هر چیزی که اسرائیل نیاز داشته باشد، چه نظامی، مالی یا اطلاعاتی، رای خواهم داد.
🔴
می‌دانید، آنها یک معجزه هستند و نمونه‌ای از دموکراسی و ارزش‌هایی هستند که ما در کشورمان و در کل آن منطقه زندگی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125016" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125015">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی (IAEA):
آژانس بین‌المللی انرژی اتمی توسط نیروگاه هسته‌ای زاپوریژژیا (ZNPP) مطلع شده است که نیروگاه حرارتی زاپوریژژیا (ZTPP) که سوییچ‌یارد آن به تأمین برق ZNPP کمک می‌کند، امروز صبح تحت حمله سنگینی قرار گرفته است.
🔴
تیم آژانس در ZNPP دود کم‌نوری را از سمت ZTPP مشاهده کرده و صدای فعالیت‌های نظامی را شنیده است.
🔴
فعلاً خط برق هنوز متصل است. کارکنان ZTPP به دلیل حمله در حال پناه‌گیری هستند، طبق اطلاعات موجود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125015" target="_blank">📅 12:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAsesueU4yQsV96CsFoVsEUeOwzaDhxG8snNWZT72ZG-kyfGfSJa0wDK3wzotSlJGzzcj2HRBwZa_hGDfCm788GgDUjz7gLDBf26EbXAcm0pfSLjEt2jUlIJmm57G8Kj3RITkMGYbye5MGKdl-rZkYiHGmz6KszwIgqfW5R3uiRpKMqkcMhN90e1VSkdmHRMYKVyqsC7fr5QgJvTPNrg8Uk29KhqLUQf9C141aRVO74YsKgDNguCTBmXxdEk-vslda3es9k9j0eko2BRqn3Fa2qqjF9x-m9E-8sqMcxDFFSlHeIZrwxks1kFS4opNheQWlqtdduU0o8jVeJTbVy2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsy9F8GGTWzRKBe1Db67RmTsUiaClamQw8-eRav-88QVdSHkTK5MatRMsqVMjBMhpnX8xZ6UmRWmgPpX_LFSw8NI1NGljwV1AKLRhOWE3Ln0vPici8ouj7pQLT2YTcuivE8LrOSnB3SHcgK6hlqJcehPEeUb7bqucLNXcwL9dAaESwOfN0icRSAMUnFhEjiIt9_8RdQxR8i6Vc_LvnCgsTMphwEYlmjnVEdVlHv0jdSGFDRRdBWVnkEUqj1D0ruaU25CuQM38GaCf_OYpGY_piVO4hdz9F59hL9YbCcFNdvjw7l3aDO0D4gcwSPVpj8nvliuhWWfeZvC_BRHfcIxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMxv2vd2TamAL3x7mMsGEWGG-xNQMG9vtt_0-8pFG4DvatVfUXgtah5kPbQ_il-fpIGIFbhRGpnxG97E4leZVPQhf6nJ8vW4mw4NISisNLqqLEjzcjmq1WjzykSc4PjC2UhJgak3PJQscmkP5kH49Gx7c8zjOJgRMk52nMf0Nsu2R4hj53o13VV-mICHAFPoo-vCWx0UgWPjxGrdjQp_JFSuC0D5t4LE5IYw364m73KkoY5ouuuxbsYjo9xxr6f0W7HPerGhsbxgoXoc_KQRvhXwIA9IQ5Ks3khicB-77J-N6sp0Y3xLxL1LcqB4MJEReMUFlAZmo-FrYkAxgNMqaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی همچنان جنوب لبنان را بمباران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125012" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: پهپادی که حزب‌الله پرتاب کرده بود، لحظاتی پس از پیاده شدن «رافی میلولو» فرمانده فرماندهی شمالی ارتش از خودرویش، در آن خودرو منفجر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125011" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدار تخلیه خود را به همه ساکنان جنوب لبنان مجدداً اعلام کرده و از آنها خواسته‌اند که به شمال رودخانه زهرانی تخلیه کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125010" target="_blank">📅 12:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گویا اسپاتیفای رفع فیلتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125009" target="_blank">📅 12:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شبکه عبری کان: پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش اسرائیل اصابت زد
🔴
یک پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش در جنوب لبنان اصابت زده است بدون اینکه تلفاتی در پی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125008" target="_blank">📅 12:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
منبع مطلع به العربیه:  ترامپ به واسطه‌ها اعلام کرده که پیش از امضای توافق، با آزادسازی پول‌ها به ایران مخالف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125007" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/125006" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ATMfROmNiFzCgPJkFK6iyD6wgW2n1LiRib7NbpuEJqNrxfQqWaumWzEC9itrJQAViJw-P2tUIRml6V1JAhwH_J-fkfd4YNfb2VBTd7M7R9f-m1xnqFSiMFkbc-u1UObbRwv0gXWvvVaxOTuRu77AQCzV0YnV-t-MBfArB7N3gPRxmUVo4LgPOXLATuam58y0gaimTakl9BaIe-wkzmAeI3Sp4YcMkQ-EC7DYm2UtQvF-CEK0LLjxpT4f-ZpoMBcyxuw-mwb02Re-DjMdqKZstMq1enekgkIPw9PGQmyFf91srrKhF2agm9gEH-Ju72iRbcn6S2sHgyZC9NteiZIayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/125005" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shK7Px-L00VJvYg8EdpwOm1U-NrYYaA2_Gy7tpjFQevJVVhvaQiY6F-2zI8kFYaeiaQMYAb8SgaU6lk_x9FsFRwYehC0EgNriGpvFKpNCbH2148Eg0gpLY9olchyz1gvrhyv9pGw9rdjFyYmYf0DE_o0A5RLHuG2Tp21kzInoB4Ni375o-9xK9o1k7McqAqDhJA4Ee_deQKdIQvbmwa_kp_4itT6ZcpdnHorIOxlmwprSErX6AJdDMOyk5rnwnkmgmg1nGhF3qaz1mq9yYbQIFqXP3oLBiuSvjJ3aqE_5itrMwrq1t3wGEiaXV3ZLW5nSYzoiur7G11hfR-5WzOTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از ناوچه Boykiy نیروی دریایی روسیه پس از حمله پهپادی روز گذشته اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_gPXc9tlQcGfaLw3PDVIQqN3CCDaTGrTuntdqL-kE8whnaP7pMTIw9f6Trq_Xa9OVjzG3nkrzMaJhkiKlToQB9N6W38PQXjlsGlDKgfWrmEFfQHgKEAvMvn45l5kySIMLT7Jv97XTnhdTf1Ay_k-VbzR1XDuoK2jlzjkc1zhfRtuEIzT4nEul_Gj6ASFBm_J7a4WKqnb9NmddtBIYrXTfeZcJ6tk_Miv56yiRJeyJvXOOTOIIqjKSljcwsgk1uGMThoVFwbd-LMLQsohoyNjf4t9vTDDvfKlxVRZIhVwQR6Mfzdbhj1zEpalu8-CH2Hkg7IBPA6xzNDAOxTTgY6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: سرهنگ دوم آویخای ادرعی می‌گوید ارتش اسرائیل اولین هشدار تخلیه در جنوب لبنان را از زمان اعلام آتش‌بس توسط ترامپ صادر کرده و تأسیسات حزب‌الله را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125003" target="_blank">📅 12:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125002">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم آتش‌بس در لبنان را از «مشکل بزرگ‌تر ایران» جدا کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/125002" target="_blank">📅 11:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125001">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مجتبی خامنه ای :  نظام سلطه پایگاه نظامی به نام «اسرائیل» ایجاد کرد و ایران از موضع خود در قبال «اسرائیل» عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/125001" target="_blank">📅 11:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125000">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jck4OhJvEl5UEOb8z4iAGwEoBHnBwXlw6Ool_3rTiaUpSSoWN8AmfW-4eRTvxwYjzak2-rBWwW1ikImUqS2axdWv6ZdKCnuI8B0wKwDorZ8uWRKkIWq76sVjJcVLl99VYdODlG6UVqlNPfLisImXNQcHYrCQNkaNqQIvm_FQ46FByDCAgNaMiQ1qUgz0ep8eR2lS-q6yyg9Czs9EUMUWoBtgCuekYjyWOWzUzrqjgmE6IYArIjfZHsgvu2M4f3qqpzl97PDGU7BwpxAUuqvNtQO-XFOdrN6GR4oyb9c8_QXmhlv6hZj5j3PmKLwGNl8cTBrONQW8o7xFsGZO-MmE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۴ خرداد؛ سالگرد درگذشت روح‌الله خمینی، بنیان‌گذار جمهوری اسلامی هست
🔴
وی در اولین سخنرانی خود بعد انقلاب گفته بود که شما را به مقام انسانیت میرسانیم
نظرتون؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/125000" target="_blank">📅 11:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxmjlIxnB6w6o66nNGbhfAfxueqlgj_cB6yZd79gDDD9M3yz1lrbKuIsGHvVU7WPRdNkzPoqZE-9_1ZsGhT2dEWxmkHi16yxwK9GGzMJvSdtTj80wKpSOR_bSihVxrbg795Q8qQw96AKfON4AJ3OXUxBj9FzJzuxqEwH13YoTNiPA0f1e_C1BGwOvPOQwyvHtt0C_AxIVfah5PHKXkFokYPoN6WUJ8KUKY7Ceo-XDfFRjMFLWcbKtAc_HEXNQeu_vpeKpPiCrB_zeUrTjPv51aIQbHp-bI7SKIs3ALxwGoAxppLxwoXqtCEMhB2IXi92st1gAFE2kMdLAPj7CBl2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDjyPduS1rfRam2sZ3OeL0CWPw--L2pr2KXEv_yV5gD4OXsKVg3Dk17r9Sb1YiR3-Qe_tKgU-eyyALnqkPGg8JHV8DoGVfB046r-zjnsXZvfQ79Nc8tmn-34KnBmjNyyb9NNm8xxifTtLPp7sIw5UyJUjccHFhHzkzIKlOPhLU17hageqYEjtRodrrL9C_lXnJcDEOC6A-wPCEJ8UBf-RLDy_TWc3z2rxsKNHV2MdKtchUGDvjjHYd1rzAA_AT8CF-XUzr-3LPgn5jRbj50EdZINRpRxsCJSV00ExEmeMSbk9kV5kXm10nE1DDU9jJSroxL36BPzwt3IzUxKoiWfHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی در سراسر جنوب لبنان ادامه می‌دهند.
🔴
عکس‌ها از زواتر الشرقیه و المنصوریه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/124998" target="_blank">📅 11:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECzPEmx2PwB6b40bVXuCZ_Flvh8R00OPFTipelejDEiTut67Y0-Bbjokkh_Zo3DWJ-2AJ-qe17QCh7NZJEES3OdKKiDd-3-Ji4wctzsdVDc2X9uxXyxdtGl9ANvBR-TZIHgslNigIyBi7Zwvwnptr1_CsizJtkj-AcoKvTOzvbyOGRHUZiWvJJ8L9DlXff1XjXByehm5Xi6S0mWX_Vr3I81J6l3Qk--oAzb8HMtUSE6kyzoMMN_9Dd9QdXPCfcF__LIJUbxccTvSOpiHy1Y8y2BWB5zXmgP4tHS5-DScJ50JjAzkblzc01pIKxYnGpYdTreYns687hUT2tdTQTmUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت «ایران تک»، جمشید قمی ۶۳ ساله اهل نیوپورت بیچ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران بازداشت شده است.
🔴
نخستین تصاویر مربوط به بازداشت او در آمریکا منتشر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/124997" target="_blank">📅 11:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: روند مذاکرات میان ایران و آمریکا ادامه دارد.
🔴
هرگونه افشای اطلاعات درباره ایران به آمریکا در سفر اخیر وزیر خارجه پاکستان به واشنگتن صحت ندارد.
🔴
در جریان این گفت‌و‌گو هیچ اطلاعاتی به اشتراک گذاشته نشده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/124996" target="_blank">📅 11:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
در ادامه موج بازداشت‌ها در شهرداری و شورای شهر سقز، یکی از اعضای شورا و یک کارمند شهرداری به اتهام فساد مالی دستگیر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124995" target="_blank">📅 11:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EILPHi4pQwd7fRxs7ziInx9nLOBjVo7p5HYv9W0ybY4SRRwaEPEF6P3xLs-AKCkHc_jqReZlaNDMxaQ_H8aNAocnpFZGSm-66FeyQxFGvatiP3bZtUb0lUGkf8LKYn-yyYR-S0WwMgahVaNnvMrBxzI4npez-BqbPQBh9CULXPqPpCNnnHbjx-9-A4GbXBdcZFxpJJRIaypoo-tVzono_Tdn7yMMDv9q0VTOPLB8q6lhLma5w3D41h7umRPgmFvgLhTrq8PIoEzXfTDIWZTAD2Tz5EgeWm_ZdkMPuVoQotE5eQiWCYD2O8xmoQX2mhZ9pMBBdIB-m5BaBoXa11hK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به پزشکیان و قالیباف در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/124994" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کیم جونگ اون به رسانه‌های دولتی کره شمالی گفت که قصد دارد «نیروهای هسته‌ای کشورمان را با سرعتی تصاعدی تقویت کند» و اینکه آنها ظرفیت خود را برای تولید مواد هسته‌ای با درجه تسلیحاتی در پنج سال گذشته دو برابر کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/124993" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/124992" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=mIbtkaseYud48q3TWzh8GSEsxKpi9i-26aJYHdy66VEVnCchVkA061-KAS8dLWF_WIerQ3-UwrOP0P8NyEz_mjPp_KiH2V7-dS9OUKNIyLXYYLmaBxIqDhD0x3T7-2aNwQp1a6xGDBrKWeu2ppUiF16cbrbcsIqGn6GlFcZVr24ptUDdUUgiXcKgl2Wgcq3Swix3HopihpL2QSozgh_R3oZGLwDmqL8-MP_G1JZYcMddkHE-R3iChaxpcY3A2KkT1-FCYxEN6E3Yy6DR7m_L8omva9C6UC4cA3_64cl71DHg75Ur9mVag3kaEEVRrQFwKy4APU5Rf70c_assK8wP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=mIbtkaseYud48q3TWzh8GSEsxKpi9i-26aJYHdy66VEVnCchVkA061-KAS8dLWF_WIerQ3-UwrOP0P8NyEz_mjPp_KiH2V7-dS9OUKNIyLXYYLmaBxIqDhD0x3T7-2aNwQp1a6xGDBrKWeu2ppUiF16cbrbcsIqGn6GlFcZVr24ptUDdUUgiXcKgl2Wgcq3Swix3HopihpL2QSozgh_R3oZGLwDmqL8-MP_G1JZYcMddkHE-R3iChaxpcY3A2KkT1-FCYxEN6E3Yy6DR7m_L8omva9C6UC4cA3_64cl71DHg75Ur9mVag3kaEEVRrQFwKy4APU5Rf70c_assK8wP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از پرواز پهپاد پنهانکار RA-01 اسرائیل در آسمان تهران
🔴
پهپاد RA-01 یک پهپاد شناسایی-رزمی پنهانکار اسرائیلی است که برای ماموریت‌های اطلاعاتی، نظارتی و حمله استفاده می‌شود.
🔴
ویدیو مربوط به زمان جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124991" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید درگیری‌ها در جنوب لبنان ادامه دارد و به ساکنان لبنانی هشدار می‌دهد که به سمت جنوب حرکت نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124990" target="_blank">📅 11:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaFQd038_Gg6neRcC6LKfenIbrmDPaa8-au7fKAJYd0HtrbXoFfS_HL5B4vMKkmDRYiX8zsZ25HZZv5Rvg76tkXewzfwE9SVVaSDTbn2e_08duOjVd5UdAP17yF9VJN38moGh2z-TaYHJZCvIFvOQaJDu6ODHH_97Wy9eHjR9Dbt0EkaZXAQMzTs_MSvyYyov_REDT6xQvTuOLLywYdf9ExLXnDQypMeoDkk9b2M-lVcvz1n8Lf_rGVbd8Qbf-tGOPC3HRx7xCgj-_dL9lgsf25YCwfM0TAFQsehQac8vqZ-1T6CZN3n5nj_fG6EexQZaOJKUXqNMYgeJk2eTyqKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124989" target="_blank">📅 11:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQ5MqRDexEX297tCqi4_FDbNeeiEZD06CQdvIhwolWawZ3MpXoO7vRZ0-iFVBYLprRxfU_m4D3yX1kkLUnb1-GR6ILt9e1WlIYX_NEejAQ2qWe48ApR4hhSXfCLTOMjDIh_Fr9GsuSiU-OEJjmQVdxnqin7tV2XLQ4fBLr1SL7B1Il6enl4eP32QSvMj1jTmNfH6-OPk6APknuoPQLdg1KeT0A4UL9rJxyZqbxhA5jA-Q0IWBVQ8wdcvGydborC1V1zyZRzjuk27saDwJH6MpAxWPscVvzHH5qZww9N08otOJmufJ-9W916h3cbbZDNxWEzuXZih9mG00nD5ZfNxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124988" target="_blank">📅 11:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=vvM1YSi1NWE2Bmu3hs3BmlUZn5QD8wm4fatRX79mYVO_JqXFRyqOFy_W1M9XxJ52GaUUClVShLTexnuTetqXDMRXpB312JZrOEFRN0mlu1pIwc_UfbkU-rbN9a_Kijb20ikl2HF2DUnT9tS6kPJs8-f3rw2rcxqocElgsCBW1Umx7i033xnStJ8snrNT77g4zBhnA_j1s8Q9Gk1hsCUq77-RNqaQDsWrykpPTx8GvyIIgqTTFZRhVhoBD0a8ZGW4Tpq7DLkFxeDI7FKG2l2u5uP_Yn-3pSng2vo-gT3cK4MulvgCsmVJIsgfRx8vJYDZLeSkryHSxcgGoXEFm61bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=vvM1YSi1NWE2Bmu3hs3BmlUZn5QD8wm4fatRX79mYVO_JqXFRyqOFy_W1M9XxJ52GaUUClVShLTexnuTetqXDMRXpB312JZrOEFRN0mlu1pIwc_UfbkU-rbN9a_Kijb20ikl2HF2DUnT9tS6kPJs8-f3rw2rcxqocElgsCBW1Umx7i033xnStJ8snrNT77g4zBhnA_j1s8Q9Gk1hsCUq77-RNqaQDsWrykpPTx8GvyIIgqTTFZRhVhoBD0a8ZGW4Tpq7DLkFxeDI7FKG2l2u5uP_Yn-3pSng2vo-gT3cK4MulvgCsmVJIsgfRx8vJYDZLeSkryHSxcgGoXEFm61bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جدید از حمله آمریکا/اسرائیل به آزادراه بروجرد - خرم‌آباد در طول جنگ اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124987" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
