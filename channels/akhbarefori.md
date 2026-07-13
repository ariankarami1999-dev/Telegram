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
<img src="https://cdn4.telesco.pe/file/edHwB3Tg161wjMCQG7ePdnsXc2Z6NyfSrKNlpYg-SzjP0Cgot7dwF4Yij4Tv6P-9fLaXrVgRhVLvqTOWS2V2oOv0uVHRPMF-jT2c_o2zPhhYg3gfAANjNfTdwiIOdBTCSr5QWfK3TAyYUIRkhSgg9aCCnVrXhIIuvBc8BM_0lYxxW1BXs1RUucr7bJCJve7aqktPaveTkNY3lFBWTiQE_U08iZ0R5UzF_MbOpKPLNLmL1uolgpNECjbEKB5wznPDf5sXJoVh-qdWWLYNJTeuMHqzKlxevTdUXYHGBo7Z4bS6BX7_kLjFmtsrJ2OOUXdURgNyVuC1uQlNVyJAGrf4wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-670597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4534901185.mp4?token=u8gSJCs64CZG5WHb0hE5DQOyEQOz5XOaxnE2W4Hfq31UMnTq-4wDZXRNnYxDFID_123E4jiqCKets7v5WRDNlZY3s6hrGK5YJAZAFqNYoxv_oT5VSpYL8BX_eiEI1anyyH4W1sFyeGCQSbtggROw5P4_xiS2zTtqjIsCZDooKNeSTxOxO4Khyi1m9YRqFk6L7tjv6sfTBlkwOVSySH7FlAjC0F99UY-tT7ab7WUPn-KwqAdyRvkxUjzCJCZ1DDyh92jn4WJ0kpzpdXBkVEWluzzAByhxCeSiIbw7nVtIum5ZmjxCJ2YBdw0Bq9hfHA9wlqaKZ7Vj6Xrd1QyYt7llig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4534901185.mp4?token=u8gSJCs64CZG5WHb0hE5DQOyEQOz5XOaxnE2W4Hfq31UMnTq-4wDZXRNnYxDFID_123E4jiqCKets7v5WRDNlZY3s6hrGK5YJAZAFqNYoxv_oT5VSpYL8BX_eiEI1anyyH4W1sFyeGCQSbtggROw5P4_xiS2zTtqjIsCZDooKNeSTxOxO4Khyi1m9YRqFk6L7tjv6sfTBlkwOVSySH7FlAjC0F99UY-tT7ab7WUPn-KwqAdyRvkxUjzCJCZ1DDyh92jn4WJ0kpzpdXBkVEWluzzAByhxCeSiIbw7nVtIum5ZmjxCJ2YBdw0Bq9hfHA9wlqaKZ7Vj6Xrd1QyYt7llig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی به ضخامت و اندازه کارت بانکی که برای کارهای روزمره استفاده میشه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/670597" target="_blank">📅 20:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670596">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بازداشت یک فرد مسلح در نزدیکی ساختمان کنگره آمریکا
🔹
پلیس کنگره آمریکا از بازداشت فردی خبر داد که با یک سلاح گرم در بیرون ساختمان کنگره حضور داشت.
🔹
نیروهای امنیتی به کارکنان کنگره و سایر پرسنل دستور دادند تا اطلاع ثانوی از تردد در این منطقه خودداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/670596" target="_blank">📅 20:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670595">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
روسیه در سیریک نیروگاه می‌سازد
🔹
در این دیدار پروژۀ اتصال شبکۀ برق ایران و روسیه مورد بررسی قرار گرفت تا  درصورت فراهم‌بودن شرایط، امکان انتقال ظرفیت محدودی از برق جنوب روسیه در فصل تابستان، فراهم شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/670595" target="_blank">📅 20:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670594">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مقام یمنی: زیرساخت‌های عربستان را هدف قرار خواهیم داد
🔹
محمد البخيتی عضو دفتر سیاسی جنبش انصارالله یمن شامگاه امروز دوشنبه تأکید کرد که این کشور قطعا پاسخ تجاوز عربستان سعودی به فرودگاه صنعا را خواهد داد.
🔹
البخیتی با اشاره به اینکه این پاسخ «بسیار قدرتمند و درآور» خواهد بود، خبر داد که نیروهای مسلح یمن، زیرساخت‌های عربستان را هدف قرار خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/670594" target="_blank">📅 20:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670593">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxMnmufH3ZeyIJE4BMfEcb4SJ05I4lBB5QclPZGtHFd5oWXhtQ-mm0b8h_kkyHRRhQbN8Qsho--F9hm3wmdqFY6QVfW9EutDbHb1O_Krr3NE8MXzbzQNoZK3Indr_SgtTUnveAZ1QQzgPu8fKUS0zh_kgcXBb1QBSMSaPFFmNr-H1QCW3_YzzM1qgLbVlVniKfTQ4XKole9BgshjepJu1__AIUH9q9UXkL3bEsezuHnzL7gqPhnGt2iOUQS0ebazRvEwb9_r3jL9np7nbuIf650Ti5U3YgFofhsR_VHJehONYARAhu7KzhkfZqErfIa8Iz1-KvZiWP7R857J-tF0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ها خبر نمی‌کنه... فقط وقتی می‌رسه که دیر شده
💎
اجرت از ۳٪
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
🏦
خرید طلا با هر بودجه از طریق بانک طلا
🔄
تعویض طلای سالم با عیار ۷۵۰
✨
بدون مالیات ارزش افزوده
📲
کانال ما
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/670593" target="_blank">📅 20:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670592">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
اکسیوس: یک منبع ارشد در خلیج فارس گفت که آمریکا موضوع احتمال دریافت عوارض برای تأمین امنیت تنگه هرمز را به متحدان خود در منطقه مطرح نکرده بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/670592" target="_blank">📅 19:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh05-3H42ZST4tYzOLm9-6CFCGvqgk-3Hvb2ylN7BCZQZuwweQAqV7L3bDtVOYf1do_CFR3CvekcxF7zcjzfXZ8fRtQb_ZW1Gf37VNv3VPoTrVrx4JrUe4VLVocmAJEO_qc_Tmhf9HREhpuL_LKJbZdaovTZYY-SHJGwtd6LExoWRzxZZ2vjh7f4pFvXI1qERRTNZmi_i_zu8DkBfNvECq3Vuzw95BopHI9-7iAWsiby1IkZKdKhltP1lPRUC2gu7w8kS8aODwy45Pi9KQ8tfFiWPH2aNjfFak1uct6d462KPKOxjmACJ-HPkTF8BPIIY7GNkvNDQoU3v_Uvt8zpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر آیت الله سید مصطفی خامنه‌ای فرزند امام شهید سید علی خامنه‌ای در حال زیارت مزار حضرت ابالفضل العباس(ع) در جریان تشییع رهبر شهید انقلاب اسلامی در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/670591" target="_blank">📅 19:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
مصادره ۳۵۸ کیلوگرم طلای غیرقانونی در اقلیم کردستان عراق
مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق:
🔹
بازداشت متهمان پرونده‌های فساد و تحویل آن‌ها به دولت مرکزی بغداد انجام شد.
🔹
دولت اقلیم کردستان همکاری خود را با دولت مرکزی برای مبارزه با فساد، جلوگیری از هدررفت منابع عمومی و تقویت حاکمیت قانون ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/670590" target="_blank">📅 19:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inBHJ-VV3k8FguImCDJwlzaYu7c8bikgZPgRUOPiAq_3X3VUel60VwtaOJyK7isFeScHK3CtIFEwWeAGpU_mGJOPxL9WFlfJGYEBC0ooB3TNKRSWvU1RHnY1pL8F2C5qXojKj3cMrspCPo2e2NEuCT1uyZahXHxvvQQPNgIRyEPB6br9P5hGtNKlbBiMpZHOcSLc7fxEGuJI9B75H6NcbkHH23NVYg5QKgedC8Hi_fosrX3c3zRjJjmv7i-VmkHbl8S_juRDLhNvVTenFfm0oS78KjCbcCMJ7FuH7F6LMmNjNjxvjQQrMXOIlFAZNvqZWIMi54IeoJDGq6maYgTt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتقاد ۶۸ درصد مردم ایران به سرمایه‌گذاری در بازار طلا
🔹
نتایج مرکز افکارسنجی ملت نشان می‌دهد اعتماد سرمایه‌گذاران همچنان به بازار طلا بالاست.
🔹
۶۸.۴ درصد مردم، سکه، طلا و صندوق‌های طلا را سودآورترین بازار در یک سال گذشته می‌دانند و بیشترین بازدهی را برای سه ماه و یک سال آینده نیز در همین بازار پیش‌بینی می‌کنند.
🔹
در مقابل، ۱۳.۶ درصد پیش‌بینی می‌کنند بازار ارز و زمین و مسکن در یک سال آینده بازدهی بیشتری داشته باشند. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670589" target="_blank">📅 19:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزارت راه و شهرسازی؛ زخمی سرفراز روزهای مقاومت
🔹
در بررسی پدیدارشناسانه و واکاوی هندسه‌ درگیری در نبردهای اخیر، اعم از جنگ تحمیلی دوازده‌ روزه و معرکه‌ رمضان، تقابل جبهه‌ جانیان استکبار با نظام جمهوری اسلامی ایران از ساحت نظامی و میدانی صرف فراتر رفته و لایه‌ های بنیادین حیات ملی را هدف قرار داده است. اگر با دقت نظر به راهبرد خصم زبون اعم از توحش عریان رژیم صهیونیستی و جنایات ایالات متحده بنگریم، در می‌ یابیم که آنها با درک ناتوانی در مصاف اراده‌ ها، عقلانیت شیطانی خویش را بر ضربه به زیرساختهای حیاتی و شریانهای حرکتی و ادراکی کشور متمرکز ساخته اند.
🔹
در اندیشه‌ راهبردی، مقوله‌ راه و زیرساخت حمل و نقل، صرفا مجموعه‌ ای از سازه‌ های عمرانی یا ابزارهای ترابری و سامانه های نرم افزاری مرتبط نیست؛ بلکه دالّ مرکزی انتظام ملی و شبکه‌ عصبی یک تمدن است. تهاجم ددمنشانه به بنادر، فرودگاه‌ ها، خطوط و ایستگاه‌ های راه‌ آهن، پلهای مواصلاتی، ناوگان حمل‌ و نقل هوایی، جاده‌ ای و دریایی و از سوی دیگر، ضربه به مجاری پایش، ادراک و داده‌ پردازی کشور نظیر ایستگاه‌ های هواشناسی و رادارها، نشان از یک طراحی پیچیده برای انقطاع پیوندهای حیاتی این بنیان مرصوص دارد. دشمن در خیال خام خود بر آن است تا با قطع این شریانها، تاب‌ آوری سیستماتیک کشور را دچار فروپاشی کند.
🔹
اما در همین نقطه‌ تلاقی بحران است که مفهوم زمخت زیرساخت حیاتی، از یک اصطلاح تکنوکراتیک و مهندسی، به یک مقوله‌ وجودی و جهادی استحاله می‌ یابد. وزارت راه و شهرسازی در این آوردگاه نفس‌ گیر، در قامت یک قرارگاه عملیاتی خط‌شکن ظاهر شده است. کارکنان، مدیران، مهندسان و متخصصان این مجموعه، با تلفیقی از تخصص فنی و تعهد ایمانی، نشان دادند که ماشین‌ آلات، سازه‌ ها، تجهیزات و فرآیندها زمانی که با جوهره‌ مقاومت درآمیزند، شکست‌ ناپذیر خواهند بود.
🔹
تقدیم چندین شهید والامقام در این مسیر،
گواهی صادق
بر این مدعا است که صیانت از کیان اسلامی، محدود به سنگرهای مرزی نیست؛ بلکه هر رادار، هر لوکوموتیو، هر عرشه‌ کشتی، هر پل استراتژیک، هر خط ریلی و ... خود یک سنگر مقاومت است. خون پاک این عزیزان، به مثابه ملاتی معنوی، استحکام این زیرساختها را در عالم معنا تضمین کرد و نشان داد که توسعه و امنیت، دو روی سکه‌ استقامت ملی هستند.
🔹
امروز، وزارت راه و شهرسازی را باید زخمی سرفراز این نبرد همه‌ جانبه دانست.
جراحاتی که بر پیکره‌ راه‌ ها، بنادر، تاسیسات و ناوگان ما وارد آمد، نشانه‌ هایی از ضعف نیست؛ بلکه مدالهای افتخار و اسناد زنده‌ پایداری ملتی است که در برابر طوفان کینه‌ ها خم به ابرو نیاورد.
🔹
این پیکره‌ زخمی، با تکیه بر ظرفیت های درونی و عقلانیت انقلابی، نه تنها به‌ سرعت بازسازی و احیا می شود، بلکه با صلابتی افزون‌ تر، مسیر پیشرفت ایران اسلامی را ذیل عنایات امام عصر ارواحنا فداه و نایبش امام سید مجتبی حسینی خامنه ای حفظه الله هموارتر از پیش خواهد ساخت؛ که به مصداق سنت الهی، هر بنایی که بر پایه‌ تقوا و ایثار بنا شود، از گزند تندباد حوادث مصون خواهد ماند.
راهبرد| افشین فیروزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670588" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4JL7GSAAF8b1hn_jL3qAA1a1BA6qWXTsEBY3IpqOZ8M-hiCupD_3qIYmbOWiQH16RipuMtzxLZANJ0aLcMzmv9UtLOHxxkipnweY93c0pAhVsH4FiW1Sb1IRhC2KYnz4d8fD5dgbVOtekb2pBch-dKR82Yr18V8YMBCh_nAF_9gxWqw_vPYcLaU1yFWyT097-yC_Ehbguuth3CM8lfruQPrcwybV53fwitthda13GN2HWkpjE1yiRn0Y6fww_cCYf8OlIVMrAqbg9P6iJ10INm5gf3qru-qAJoxip4_2LlspvPJTVkNUZv62_L8ULdjS3QjzuxF8e8oE3ou3BTXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمانه بر سر جنگ است
🔹
نقض آشکار آتش‌بس و پایبند نبودن آمریکا به تعهدات و جنگ‌افروزی‌های اخیر ایالات متحده نشان می‌دهد که مسیر تنش همچنان ادامه دارد و چشم‌انداز صلح بیش از گذشته با ابهام روبه‌رو شده است. بی‌تردید، صلح عادلانه بهترین راه‌حل برای همه طرف‌هاست، اما صلحی که بر پایه فشار، تهدید و حمله نظامی شکل بگیرد، پایدار نخواهد بود. در شرایطی که تعرض به خاک ایران و فشارهای راهبردی ادامه دارد، دفاع از امنیت، حاکمیت و تمامیت ارضی کشور به یک ضرورت تبدیل می‌شود. در این میان، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران است. گذرگاهی که نقش تعیین‌کننده‌ای در قدرت بازدارندگی و توان چانه‌زنی کشور دارد. حفظ جایگاه راهبردی هرمز، تنها حفاظت از یک آبراه نیست، بلکه صیانت از اقتدار، امنیت و منافع ملی ایران در معادلات منطقه‌ای و بین‌المللی است که باید برای آن جنگید.
🔹
هشتصدوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/670587" target="_blank">📅 19:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670586">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
محکومیت کارمند آمریکایی به اتهام صادرات قطعات الکترونیکی به ایران
آسوشیتدپرس:
🔹
یک کارمند سابق شرکت «آنالوگ دیوایسز» به اتهام دور زدن تحریم‌ها و صادرات غیرقانونی قطعات به ایران مجرم شناخته شد.
🔹
وی که دسامبر ۲۰۲۴ بازداشت شده بود، به همکاری با یک شرکت ایرانی متهم است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/670586" target="_blank">📅 19:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670585">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
نوین، نماینده مجلس: بدعهدی‌های ترامپ، ضرورت خونخواهی را بیش از پیش آشکار کرده است
علیرضا نوین، نماینده مجلس:
🔹
مقام معظم رهبری در پیام‌های خود بر خونخواهی و عدم سازش تأکید کرده و فرمودند که میدان‌داری تا زمان قصاص ادامه خواهد داشت.
🔹
بدعهدی‌های ترامپ در سه سال اخیر و شهادت رهبر انقلاب ضرورت خونخواهی را بیش از پیش آشکار کرده و قرآن نیز پیشوایان کفر و پیمان‌شکنان را به جنگ دعوت می‌کند و این وظیفه‌ای شرعی و قانونی است؛ راهکار اساسی پاسخ نظامی قاطع و سیلی سخت به آمریکا است که وصیت امام شهیدمان بود.
🔹
وحدت ملی و جلوگیری از نفوذ دشمن از اولویت‌های اصلی است و مسئولین باید با الگو گیری از روحیه جهادی شهدا عملاً نشان دهند که خونخواهی را جدی گرفته‌اند و با هرگونه اقدام علیه دشمن تکلیف جنگ را روشن کنند.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/670585" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670584">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsrVMlOmH0UnRlweli5wymIBO-yl7xjVr83cFKlZQOv28kectT7L3c-gYQ8GjwJm2ygOIerJb-RNRBHt5CNZXOFuREvvNbaU7mFe7tUG_JfN6gZ0JjTuIcFgTtGlLlCuzz12tvvb0I06zqxUdNjtcmkFGl9CtjXN285Df9A8C0Ez17D7iby3pMs7TK3ZTeBuHhJcuuITG-mWIxNR_SVac25aH8FBTks7aTzbHncw-Kn0SCL0WpRere3J0_GR-6aagkslhXmpUuCOkqYG650VsSYHdQAFcLY0-92KCqKTfNlJ86wolC5PQoc_KiatLXjLkP207FpMNA_ZEKxvybp5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنک‌ترین اماکن ایران برای فرار از گرمای تابستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/670584" target="_blank">📅 19:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670583">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادارات هرمزگان در روز سه‌شنبه و چهارشنبه تعطیل شد
🔹
معاون توسعه مدیریت و منابع استانداری هرمزگان از تعطیلی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
🔹
امتحانات نهایی دانش آموزان و دانشجویان طبق برنامه از پیش تعیین شده برگزار خواهد شد و تعطیلی شامل آن‌ها نمی‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/670583" target="_blank">📅 19:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/670582" target="_blank">📅 19:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWCqTqqjCIc0h2hasd8FICkkZ3x3-yYNbbVrl3eqs_EUA7pUc3Cv1JNd-6jcBKaAAvn2QZOfeoDp5GHSC-6qk9SmmgR_O7ZpoSqDSD97sZsTOHLvbjnymLKc7f1fVSpFbi-VmwK3K8wsY2SCiBMpINlsgcKaR-H-PvuGmght-WO5MlwNxrBPIP-mhA2AwKcQm5CjhYLgaHWo-obzXl1ct6YjYYrRA_qK9XPBfdwR4svsdFDQlvsUQCwxrLFKwDnfrBvSj-2rSorJzkmAdTEFx6bKdixKfO_WGxLiBTXe6-my_e_xNjCGkJ_L3jElGleE_4YXes89S0_j-Vab5Oy-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین بیشتر از کل جهان پنل خورشیدی اضافه کرد!
🔹
در سال ۲۰۲۵، چین ۳۳۶ تراوات ساعت به تولید انرژی خورشیدی جدید خود اضافه کرد که از مجموع تولید برق سایر نقاط جهان بیشتر بوده است.
🔹
این کشور ۵۳% از کل افزایش ظرفیت‌های خورشیدی جهان را به خود اختصاص داده است.
🔹
برای درک بهتر این مقیاس، باید بدانید که افزایش ظرفیت پنل‌های خورشیدی چین در یک سال، بیشتر از کل برق مصرفی بریتانیا (۳۲۲ تراوات ساعت) بوده است.
🔹
انرژی خورشیدی در سال ۲۰۲۵، ۷۵ درصد از افزایش تقاضای جهانی برق را تأمین کرد.
@amarfact</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/670581" target="_blank">📅 19:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670580">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اخلاقی‌امیری: استیضاح وزیر نیرو، با امضای نمایندگان همچنان در نوبت طرح در صحن باقی مانده است
حسن‌علی اخلاقی امیری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در ایام جنگ، مشکل کمی در مدیریت برق داشتیم، اما در دو سه هفته اخیر با گرمای هوا قطعی برق بدون اطلاع قبلی در برخی شهرها رخ داده که جای نگرانی دارد.
🔹
دولت سال گذشته با صرف بودجه حدود ۲۰ میلیارد دلاری پنل‌های خورشیدی وارد کرد تا امسال مشکل قطعی برق نداشته باشیم و انتظار می‌رفت قطعی‌ها با برنامه‌ریزی و اطلاع‌رسانی مناسب باشد که این اتفاق نیفتاد.
🔹
استیضاح وزیر نیرو مربوط به سال گذشته است و با امضای نمایندگان همچنان در نوبت طرح در صحن علنی باقی مانده و با شروع جلسات مجلس احتمال استیضاح این وزیر وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/670580" target="_blank">📅 19:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670579">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-text">🎞
|
#تماشا_کنید
❇️
بانک توسعه صادرات ایران، در سی‌وپنجمین سال فعالیت خود،با تمام توان و قدرت در مسیر حمایت مالی از تولیدملی ، توسعه تجارت خارجی و شکوفایی اقتصاد ایران است.
💢
۱۹ تیرماه سالگرد تأسیس بانک توسعه صادرات ایران گرامی‌باد
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/670579" target="_blank">📅 19:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670578">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Fj8P2c_FqURNuhaxG8qpku00ogTJsx7FpOH5YSruNqmADkiRveXZgYmwyLxgQirOovBba4X-rRCu2ECde4pY2R-VH9mqx11GOGhoXDudr7BKuRwAA2KCMsLcZkY2WuaOX6shYJk7seXVN-cNR3Jz1iQWBsaCuBH_fEPws-kinDvnxIHM6HDGyRfglal_zsPazARIAy79__fiFY6qbkDSOxTBmPjShp9KqflgQVKs8EGJo0dHpw5f3Mx6T8ij71Oz5_l0CaW6r4m4sNgPy0spxTAs9Wy94E0HLXDpSMN9ee4ktgAMq4u7ekaM8Pdwfcz36WLuDgskSF_2NuL-6qHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/670578" target="_blank">📅 19:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670577">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYfJenGfBpj5sG4OXuvWUy-xSUDc-JGcJpkrzYYqI_Aq4u3O9i8IrrNJSffkeJmfKNJTMF75JUkP7ycDWKHrGqt8hIySlyK1FTwc0hmSzZVdj8x8-HwMdn3IXRhL6_lUHEXZpaDZ3ZqbtsWchvap2Y1cvn0FGOyPFf6w_ArQdoL5pfWrORSm8-KpVZ0XvhgEdmcvOeWjtAIf6IS40kNtvdlHNBBwuN8cgtt5eHj1oQ0C42aGGkVQ9lDUQxFtkxw8apuuojdMgtHtTamAZvUoPPu2mLCSb0ysAZlcML_cgXcU5lYLTEj_k1cQL0Lk3GAmMLJiRtIPh_0oIUD3m7RhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک‌زرد: آمریکا حامی تنگه هرمز خواهد بود، اما ۲۰ درصد از تمامی محموله‌های ترانزیتی را دریافت می‌کند/ خبرفوری  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/670577" target="_blank">📅 18:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670576">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHLsToBrbgoxCK_bMp1zioKK7Y4_-ZNt0kKlsDx4U_h6_tU1kG6il0uwh8HRQ4P0_hAvQR5Mrvf-N6IhiiScLcaA1OIus8unmik3m4ddBCTEjGNAjLLq4Pl8tv3vCxffGWXwCDlXyN_E-3KwrUU1_DxmhEsBZX6jfsS6hYAphLRWjNcZj4u9AVwtfz866xQNOWYV7Ack0IuFj_obwCB8e0NQkktFlNpuinusB_fm_BES8iIyj0DTIyWR_aSiIhk6MyRRaQSMN8Pt6DBIWUDVtcC-uCU7X6n6glEx00sJlKtv4QIUxWIFgSL9jCJkuCYbf_NhQTZDrT4fxCVVL3Z-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل دولت ترامپ با دیوان بین‌المللی کیفری؛ تلاش برای تضعیف یا انحلال دادگاه
🔹
دولت ترامپ اعلام کرده است که در پی تضعیف یا انحلال دیوان بین‌المللی کیفری است.
🔹
مارکو روبیو با دفاع از این رویکرد، استدلال می‌کند که این دادگاه با تهدید حاکمیت ایالات متحده، زمینه را برای پیگرد قانونی مقامات آمریکایی فراهم می‌آورد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/670576" target="_blank">📅 18:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670575">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
افزایش تولید نفت ایران در گزارش جدید اوپک
🔹
گزارش ماهانه اوپک نشان می‌دهد تولید نفت ایران در ماه گذشته میلادی به ۲.۴۴۱ میلیون بشکه در روز افزایش یافته است. در همین بازه زمانی، قیمت نفت سنگین ایران با ۲۴.۶۲ دلار کاهش نسبت به ماه قبل، به ۹۰.۷۷ دلار در هر بشکه رسید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/670575" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670574">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
طرح جدید ترامپ؛ ۱۵ دلار بر هر بشکه نفت در تنگه هرمز   خاویر بلاس، ستون‌نویس بلومبرگ:
🔹
ترامپ از بازگرداندن محاصره دریایی علیه ایران خبر داده است؛ طبق این گزارش، واشنگتن قصد دارد برای تضمین باز ماندن تنگه هرمز، عوارضی ۲۰ درصدی از تمام محموله‌های عبوری دریافت…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/670574" target="_blank">📅 18:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670573">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شهادت ۳ رزمنده در حملهٔ هوایی به آبادان
🔹
در پی حملهٔ هوایی دشمن به شهرستان آبادان در روز دوشنبه ۲۲ تیرماه، شهیدان ایرج سردارپور، اصغر سردارپور، علی تاجبخش برای دفاع از کیان نظام مقدس جمهوری اسلامی ایران به فیض عظمای شهادت نائل آمدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/670573" target="_blank">📅 18:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670572">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اظهارات متوهمانه ترامپ در مصاحبه با فاکس نیوز: احتمال ۹۰ درصدی وجود دارد که رهبر جدید ایران دیگر در قید حیات نباشد/ صابرین‌نیوز
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/670572" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670571">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dclBZN0wNMiYr21F6AynRHzTjAEvSfhFweNRbpHg_gEF09-tuODWsouQYVX8I5vwIomzPAVq7k6gzMS2I6rjoRtBce6JGA14o08P_KJJfNLXqxtKq8-C_T2S5rrJw0d8645bsZfbg_Es8u3H98Kl1kMYwKU0aCPvZ9FX2mWPkN299y1jBeYgyfEZ1l6YoBfNMyDtkEfdFjQqAuUoLdFt08CyHivfNQE5AoQfuRQXTonO8bUwWstNxE3vdxTNUf06Jwp7xMuFUeg0poQ5RLFWSde2N1Z3ibSJPLmsUz4VqQns0LseBSaEVZvT7kd8TSmyD1iLOa6WBAtyeoE5mlx3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهاءالدین خرمشاهی، مرد نام‌آشنا ترجمه‌های قرآن را بیشتر بشناسید!
🔹
بهاءالدین خرمشاهی فقط یک نویسنده نیست؛ او از برجسته‌ترین حافظ‌پژوهان و قرآن‌پژوهان معاصر ایران است. پزشکی را رها کرد تا تمام عمرش را وقف ادبیات فارسی کند. حاصل این انتخاب، ده‌ها کتاب، ترجمه‌ای…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/670571" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670570">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr4Bs3x49S91zn160QVNY8S8o-kZZGShfFTavAnnuIfKzxQ18FZI2B0uMGmupLh0JHFjHZ9PlQtmzNs6pxLOyvZlBGGrci515i5kC_GF089FLlcdnk30qAZMZvKtacmg9ZTA8BFQnLXREjO6INIqWtw6zcChh6Uqn9HciP5e7Pv1ZRp3cFJ8XZtRmCQnVhpYHUtOXByHOdWaW0wAH-Lq98Hzd2AdAeLX8pAVSVtfxDpKAIA7lpSlmoHzvVnx0IiKaTUl9fFSm0Tqz5HBQHVZH8hQEDzQiX3GS-4mGCXmnYeS6UBkjB6acrxSNzb7LlPuUKuaNCyWSPU-M4caU6RYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات مخفی اسرائیل برای جذب محمود احمدی‌نژاد | طرحی که شکست خورد!
🔹
بر اساس گزارشی از نیویورک‌تایمز، اسرائیل طی سال‌های اخیر تلاش محرمانه‌ای را برای نزدیک شدن به محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، آغاز کرده بود؛ تلاشی که هدف نهایی آن، تبدیل او به یک مهره اطلاعاتی و در نهایت استفاده از او در سناریوی تغییر حکومت در تهران عنوان شده است.
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230082</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/670570" target="_blank">📅 18:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670569">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای خوک‌زرد: آمریکا حامی تنگه هرمز خواهد بود، اما ۲۰ درصد از تمامی محموله‌های ترانزیتی را دریافت می‌کند/ خبرفوری  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/670569" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670568">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHjxs9OPKuxY1pRNXHXbqF0CdzqSr8xCJApWJwTUDx7nCVLdqSkWnY2aeY8EOb8oqjMzbsF_PnRzrYNWl2m2KVq4LQl39vgpCoNDbGzgMBaxFOaiHmuGyeY-kkrpZi-wmiG3c_jgYA-K70YZWUblpWoerUryT-oAwtFPfInIkCk_ml6Wq5SfMRiTucjySLr6umK7_I6OmSOCWHSTeNs6N_8R8V8vta0sGiK7q14lDb6dk-XdtWlN1MZOn5cNCIWs2bHDeCaewyAPNdLXIQJ8SM0QqENIaMhUsUsE_QsNiioyE2FOCc5gsqKP1Yif_hxJZszX7E22CZ1IiTpNQwwwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر ۱۰ متقاضی وام ازدواج، ۴ نفر هنوز وام نگرفته‌اند
🔹
از میان بیش از یک میلیون متقاضی وام ازدواج، به ۶۲۲ هزار نفر بیش از ۲۰۹ هزار میلیارد تومان تسهیلات پرداخت شده است.
🔹
با وجود این پرداخت‌ها، همچنان بیش از ۴۱ درصد متقاضیان واجد شرایط در صف دریافت وام ازدواج قرار دارند.
@amarfact</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/670568" target="_blank">📅 18:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای
سازمان تروریستی
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/670567" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
دفتر سیاسی انصارالله: پاسخ به حمله به فرودگاه صنعاء، قدرتمند و تکان‌دهنده خواهد بود  علی القحوم:
🔹
پاسخ ما به هدف قرار گرفتن فرودگاه صنعاء، قدرتمند و تکان‌دهنده خواهد بود.
🔹
معادله شکستن محاصره فرودگاه صنعاء ادامه خواهد داشت و این روند بدون توجه به هر آنچه…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/670566" target="_blank">📅 18:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
یک نماینده مجلس: تعیین جایزه برای مرگ ترامپ، ضرورت امنیتی است
مجتبی یوسفی، نماینده مجلس:
🔹
حضور میلیونی مردم در مراسم تشییع رهبر شهید پیام روشنی برای دشمنان داشت و مطالبه خونخواهی و قصاص یک خواست ملی است و اگر هزینه شهادت رهبر و هزاران هموطن برای دشمن کم هزینه باشد این جنایات تکرار خواهد شد.
🔹
تعیین جایزه برای مرگ ترامپ و پیگیری جدی قصاص یک ضرورت امنیتی و اقتدارآفرین است تا دشمنان بدانند که تجاوز به ایران بدون هزینه نخواهد بود.
🔹
در کنار خونخواهی، مسئولان باید به معیشت مردم نیز توجه ویژه داشته باشند که کنترل قیمت‌ها، حمایت از معیشت کارگران و بازنشستگان و پرداخت مطالبات کشاورزان از اولویت‌های فوری است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/670565" target="_blank">📅 18:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/670564" target="_blank">📅 18:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAsvJufaoYAYAdI6kok8ZdRh9FZnj1YJhJ7aYkrfM0etEk9016fV6bSoLbCxgIg2aeg4WpoLDWRbIiLYSR_ogfHO9ifbZtIunC-I5GEaZ7Us0KrnSkHAC5z3DiJkuTQc8nH96cNqT5EU6hf7ZK1oXCPde0li0IhcpHnzCOzyoy9PeGphpZozuvY9pnP2iAlchT9r0rLzudCsKk4Y4GhApEoFFpf691eFdBZgGsrgcilZeQ7JlP1oOMZVK0ll_mbLV4XILF07MoNH4Hok16DP-eUgBp183Yo1IhEBqHCW_faq8E0p7_g6XzXgHOQjax9ekHj1LQsx_4diZKfXVAAJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/670563" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/670562" target="_blank">📅 17:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0UOunocfZyXUwhXjmvkTXmYnS1JzVtNeVWbh6hiDNUH3FoB5h38-ZLw93P2OPhA0HnWaIowhVDY9XEqQ0DMDUNzIwiv-iTXVJCmr1kGcL2D7guoW26TBo9WojCjs-egaQLHm6lFJQRgJFwTSLyP-UB0IkBeAAUuGF_CBJBprLr8UVXKfFvAKdK2cCcDp-mG8ZuFBBi5BtSnWN291yiO6JfIagzX0KWtdIbxCzHW0r0sArdngvcVmzkdrwyBX6cnNJuGkzxdMNCsJnyQfvSAcIoYSPsrjDiq1kwwYR1pxisOuA_ldneH_cDCRIy1G36Qa5HY4Q_pVvcAWXgB06duPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/670561" target="_blank">📅 17:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: احمدی‌نژاد در حصر خانگی است
نیویورک‌تایمز:
🔹
احمدی‌نژاد تا دوشنبه گذشته که حضور کوتاهی در مراسم تشییع آیت‌الله علی خامنه‌ای، داشت، دیگر در ملاء عام دیده نشد؛ وضعیت فعلی او همچنان نامشخص است.
🔹
اما چهار مقام ارشد ایرانی گفتند که احمدی‌نژاد در بازداشت شاخه اطلاعاتی سپاه بود و اکنون که ایران از بسیاری از تعاملات او با اسرائیل مطلع شده، در حصر خانگی به سر می‌برد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/670560" target="_blank">📅 17:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv5MyhfMpxpx8SSXlTShfmOrCPApkYYaiSNuEh9yAoYYLTgNlb6JDUss15H5Wfp0-dfZ_QYAQ9DY8LpQo1BF9L142FQu9pddIX9we5jtKddd-byIXj4t-9GNTa4ubjIdbX9CAxYD2BmGaoDfUAAsdgMCTWvB-yhnWrpqoHqi-gx3iSqviwg-zkg2UgbnUOUnluG3CXSHBVAYpkDTVemLxWm_IblXsOStPZKKpbDjj82rn0XUGlSj8OltbBVe38u1F1bnWP3U3uTOUCHo5tr8bHvkPP-68_-Qo4fdMySvB4YoWKaS5OvBXp09AvLye3zPdYkz0gYDQDsbSohQkJ5lqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داستان عجیب سناتوری که همیشه علیه ایران بود
🔹
در این ویدئو واقعیت‌هایی کمتر گفته شده از لیندسی گراهام خواهید شنید که همیشه علیه ایران بود. @Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/670559" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صدور کیفرخواست برای عباس عبدی و مدیران روزنامه اعتماد
🔹
متعاقب انتشار یادداشتی از سوی عباس عبدی در روزنامه اعتماد، دادستانی تهران به دلیل جنبه عمومی جرم علیه نویسنده و روزنامه اعلام جرم کرد و پرونده برای انجام تحقیقات به بازپرسی ارسال شد./فارس
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/670556" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">خرید ارز اربعین؛ ساده‌تر از همیشه!
💫
امسال با آپ و بانک شهر، تهیه ارز اربعین از همیشه آسون‌تره.
📱
بدون مراجعه حضوری برای ثبت درخواست، با اپلیکیشن آپ می‌تونی ارز اربعین رو برای خودت، افراد تحت تکفل یا دیگران ثبت کنی و تا سقف ۲۰۰ هزار دینار ارز بگیری!
✔️
کافیه وارد سرویس «ارز اربعین» بشی، اطلاعات لازم رو وارد کنی و بعد از انتخاب تاریخ و شعبه مورد نظر، ارزت رو از یکی از ۱۱۰ شعبه منتخب بانک شهر دریافت کنی.
💢
یادت باشه قبل از هر کاری باید توی سامانه سماح ثبت‌نام کنی! از اونجایی که فرآیند نهایی شدن ثبت‌نام در سماح حدودا ۲۴ ساعت طول می‌کشه و پروسه تهیه ارز هم زمان می‌خواد، حواست باشه خرید ارز رو به روزهای آخر موکول نکنی که فرصت رو از دست ندی!
⏳
#آپ
#ارز_اربعین
#اربعین۱۴۰۵
#بانک_شهر
#اربعین</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/670555" target="_blank">📅 17:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/670554" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670553">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ترین‌های جام جهانی تا اینجا؛ از آقای گل‌ها و گران‌ترین تیم‌ها تا مدعیان اصلی قهرمانی در یک نگاه
▪️
قسمت سیزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/670553" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پاسخ در راه است...
🔹
تصویر معنادار یمنی‌ها در واکنش به حملات امروز عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670552" target="_blank">📅 17:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0lblehvomsRpVpDsLFUqjG3JW7815BbEcXbB9hOU1UZ-fiSo_YWVO2NZRQnNK3JsAOzTVgh1OoCKN1ouoW6vkluWcv3BNHAiIvPGZn9PhHYIW1hmgOwJv91cmwxMsQbUr0pJdHXRL0fmwwZTPO3h0rY7sHIK2pzWsLrmN_SMUSJ5NXCZnzAHZydaYTiXYVdZyIAkbdt0GqSJvtUepVoBUogk6GBJoTg-cN7cKrYSMjK5xP7wFgnSKAcaM4S6AFn_X0-O4yb3Dr31MFAv4SUpKu-WD4W9PEKLCdyBNtYS0XOHN5PLANUL5PknKPDHqQVPRGoAXyCe27XWlUxBSP66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: حاکمیت و مدیریت بر تنگهٔ هرمز را با قوت و قدرت اعمال می کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/670550" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu6_iDsesRXK0HuXOmY6cz4wJX1VRDreYVtVOUbCrM8d40eqsy38_VQ8gCRCwkKtkfFRfXrHn09VY9tEe52TqYomls5X7ZLchw8AjXYWnUyRFOCKIkZ2OxCmlFtxH6pd9beX4moebqNY5yiI5P4YR7jUOklJKCbRFp3zOQ5y0mrNlSMjTLDv9pRHLQusqmRzA4XU9nUGfEGk0x_jMsn-E2RNlfn4J9ssENfhaZHBzOFhEseh6c0BHsya2PqqjlQxco3zDzvZDN2h1Fvhjkl9iIrq9tBZgHwI-SfnyFtLrRMcr8FKhQRMQulspOYP4hJJML4M3ro39RqBIFjri_7EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/670549" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2WMZ0__USCt6BqDJBl-HyuQG_CCybo9HxWLQx3yHSs0RVs_NFFU6C-jOf25tBcOLNYtif-v1_P-SwXSEwycCVUykakklN0kR3nx6fMh3wDVO8IaDc81x5SnSJg3WkybvnpGf-R0ZM_9eiDLvSc0JQk89hVGP9HSKCMKuB7oX1ZtLKCx3Ss79i89s8K_Qm4yqPPW3AS9aHBFVFjLWAOswz0GY0vovj8O3-ZicS-kgiiJVqflm8RrYDm21xoHtE_n6-IK9rTeHeVQxTqvzUxjFd4RrCqNNJkQACVmtlOl3JhoMmUF0nsrFrMEJSHmlkcpH05pttQHvs3GT4tlLQgeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با یک آزمون، استخدامت رو تضمین کن!
🎓
کارفرما دنبال مهارتِ روی کاغذ است، نه فقط ادعا. آکادمی آریاداناک این فاصله رو پر کرده؛ بدونِ نیاز به دوره‌های طولانی!
✨
آزمون تخصصی + مدرک معتبر + رزومه درخشان
فقط با چند کلیک، اعتبار حرفه‌ای خودت رو بساز و از رقبا پیشی بگیر.
🎁
کد تخفیف ۲۵٪: aria25
🔗
ورود به آزمون‌ها:
https://ariadanak.com/ariaacademy/
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670548" target="_blank">📅 17:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ماجرای سگ زرد دروغگو و بمب‌ اتم ایران!
🔹
ترامپ امروز: ایران تنها چند دقیقه با ساخت بمب اتم فاصله داشت!
🔹
ترامپ چهار ماه پیش: ایران تنها دو هفته با ساخت سلاح هسته‌ای فاصله داشت‌.
🔹
ترامپ پارسال: ایران تنها دو ماه با ساخت بمب اتم فاصله داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/670545" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
♦️
سخنگوی قرارگاه خاتم‌الانبیا: به سران کشورهای منطقه هشدار داده می‌شود هرگونه همکاری یا پشتیبانی لجستیکی از ارتش آمریکا، به‌منزله جنگ علیه حاکمیت و امنیت ملی ایران
تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670543" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
سخنگوی قرارگاه خاتم‌الانبیا:
🔹
ایران با هرگونه ایجاد اختلال یا ناامنی در عبور و مرور کشتی‌های تجاری و نفت‌کش از سوی ارتش آمریکا، خارج از مسیرهای تعیین‌شده ایران و بدون مجوز نیروهای مسلح، با قاطعیت برخورد خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/670541" target="_blank">📅 16:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک نجس: نرخ تورم در ایران ۳۵۰ درصد است. شش ماه پیش، این نرخ ۵ درصد بود
.
🔹
من سلیمانی را کشتم، اوژنرال باهوشی بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/670540" target="_blank">📅 16:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/670539" target="_blank">📅 16:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/670538" target="_blank">📅 16:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: خیلی محکم به ایران ضربه خواهیم زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670533" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIhZXBT35inJXX3qVHCv2rNZvRReZUt-SzxQfCRN4U8TguQhOlJkiiEfueVQIkLlLg1CkXXsTyYLV9vIgY6trRnVa4np3dhArrt4y42-JpDIyosKvCr0IIaeeXXIbDc_EBDbgXlrxrwF69SgutBewcTSX7vfS74TPh4M_pv-XC7Mf4gJVc7w6RFaGJmx5zfpxuT250uleg5IR68sK29o1m0W_HbsAFOD2VEbArZU-VlNPV7DBT758FTedTUIv95FpCD99hdUALpNsbzHO-9uvunqLyUCv4r5dIOGUAaXQXTN8m1WTETIr_g7HowooUFx21trglVZAkpiLaXbdG5_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/670531" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/670530" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/670529" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amDgqQPnbtuSce5_LbzYk-Rl-SPu8R6KNSG0djAXiRTJx2Qlcx-kcPoKM98-gwCJ2M73D9ECW3ayd8KR4PPMGwbNDBa-bJMGn9bIgnibFpaV-7rYrNcyzeo6Nxjy5Iq6-I1IZa45UCQLGPj42i8O98WZlMnqcCKM7qVGOU9HfygZqmzITeXWcKsqF2ZnKvm4AtEAUAhPkh1PrFYujeVVcw1TZBBsksd3ysBJH9pbuE9pCPGAUequ7UDg1eY1QDN5s_lJr3KTr16yQE1FwhmXtecyf8wCSgxehhZl5WcD0oYym0u80gSONsG71AZHJe59Xd7whGS7YmCa8Av8zplgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: ساعاتی قبل، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی با رهگیری و شلیک موفق سامانه موشکی زمین به هوای دلیرمردان نیروی هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/670528" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💠
ماجرای جنگ ۲
💠
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670527" target="_blank">📅 15:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I63SxN7RRgJ0Rn7tnkr3Iye9fzkSNu0vNEx_eXP6eKBhj9RZDzvWbtgbKoatUA7zNfOFOtAplebUOmp_w1U01bJAYD3G94SUeb1qMlFg0aUiayIyPX6SSb3YeS4gLxOGQL94chxqrrz1UakdJqEUZfqvJLvU2jL2tNJETi0_MQ-Eq43S4FiJ8AcgfI_bLUL_JXo_skMkYCI5vQHowkHPY_G5I9YUkW15eNfJYpU9HCROU_t4bhLnjqzXRGIxE-KgUy3MfvjP8HoZbpEpNSjFnBfaDz0XkLWhV2qZxCI6U_61FV_hpsiRt3JtQQSpDCiQFeGg1X54tZUTIePg8B-KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp7Lty5xh67yv3ARIcwTo8mUaJFKlCr8TQdf4rVlCM7w3XEHJlmUb2rOnBrWOoDzukMLVPJ1LkxHlf-UihotNQ87rORxbhGmfHoiRldv41Pc2jLDKgrHCdtUeG3BDxqgVGF_JLar5q8LxUgckkA4bdREpolDmW66fZJM_c7uSffqYlNtxFCtCHMDK1-xv9eHYL-iOBv89YW0omhIT1pUK3sAZTgRRQgNMfXXZGYSSfy9VXNGD76WpN79N-I6j8zP2dIeXsfBCRDDG1SXlkJizq_4ljKfEgkJgdznOGRvMqXJwGbHvs_cbHjQYev_uuyB4DXZADGGgcMF_3VmCUOydQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله: هواپیما با موفقیت فرود آمد و محاصره شکسته شد
🔹
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/670524" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای شما هم همیشه سوال بوده که این صحنه‌های آخرالزمانی در فیلم‌ها چه‌طور ساخته می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/670523" target="_blank">📅 15:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اقدام خصمانه انگلیس علیه سپاه پاسداران
🔹
دولت انگلیس در اقدامی ضد ایرانی و در همراهی با سیاست‌های خصمانه آمریکا، نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی خود از گروه‌های «تروریستی» قرار داد.
🔹
طبق این تصمیم عضویت، شرکت در جلسات سپاه پاسداران انقلاب اسلامی یا نمایش عمومی نمادهای آن اکنون در انگلیس جرم محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/670522" target="_blank">📅 15:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j48lCREzcsrXJ7H055fh4DTYh8Vrv-2IBp0IXxnMr-mC2BbzLY84CziVhTnFBje2M2cTuZhn4jv68tV4BIclhk08gUrcePL2mAY3kQpjIoB5RZ_b8EZ7lqhX-n8rwefjDswUwfNjk6lR9nq_dbaVG5-VRid9xtBxUD055J6lTuDwqGb8ageUqfR1gysuUDrwxuGYiP6Iim8xw60nPPGsQat4MStQP2nuW1rVXAM6GxC4JD5lYoLFjGm7zitapJF08yuUGkBhFD9VdR5IyYDYo3G2An1qK16KHAevc0qgguL5fohfSnKIr2xTzFJu7G6thgAqbNvbO2N_eF0j4k987Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه پاکستانی: روسیه هواپیمای روز قیامت را به ایران اعزام می‌کند
روزنامه دیلی‌اوصاف مدعی شد:
🔹
در بحبوحه افزایش تنش‌ها بین ایران و آمریکا، روسیه ظاهراً گام نظامی بزرگی برداشته است.
🔹
روسیه جدیدترین هواپیمای مرکز فرماندهی روز قیامت خود، Tu-214PU را به تهران فرستاده است که در شرایط جنگی هواپیمای بسیار مهمی محسوب می‌شود.
🔹
این هواپیما همچنین یک مرکز فرماندهی پروازی نامیده می‌شود؛ زیرا به رهبران ارشد و فرماندهان نظامی کمک می‌کند تا از یک مکان امن با یکدیگر تماس برقرار کنند و در مواقع اضطراری یا درگیری‌های نظامی بزرگ، عملیات را رصد کنند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/670520" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در امارات
🔹
منابع خبری از شنیده شدن صدای انفجار در امارات خبر دادند. وزارت دفاع امارات با صدور بیانیه‌ای فوری اعلام کرد که در یکی از انبارهای نظامی زاید آتش‌سوزی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670519" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/670518" target="_blank">📅 15:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سمفونی «مظلومِ مقتدر»؛ روایت رنج و فداکاری
🔹
هر پیروزی، حاصل صبر و فداکاری مردمانی است که برای حقیقت، از عزیزترین داشته‌های خود گذشته‌اند.
🔹
موومان چهارم «سوئیت سمفونی مظلومِ مقتدر» با عنوان «خون دل»، عمیق‌ترین لایه‌های احساسی این روایت را با آواز بازگو می‌کند؛ روایتی از رنج، استقامت، ایثار و هزینه‌هایی که برای حفظ عزت و سربلندی این سرزمین پرداخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/670517" target="_blank">📅 14:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSjdYNQ1n2NuVLiAYHvPbZs6zJ_iddIR_1Mo3XSQamf6GirHCcpX8iVbuHEcPbjBP0F0IIM7Ds9qPa0PXyw7ZW_HXyzZIpaa9NN62_Q4W76KbDHUD0BReW7qnVvXSEANNEU5M2H4CRR6aDauis-fsHH6Na_AcfxxRamGf2eeLobX539wUJOr2XINvoRUqlYIAfSsq-7d0gfiTDlcD2aO8A3W9-26-zGKhFJ9XtHVQPoSHUKiFfEXvec-zYVxWw-N-3xLdTa7fAdYKR7XbK9coztU2_lCliT8x6eedrMtJvOpXIdeo109VHYyh_kHMpNZIvg2ybtlCjffKFEtfylhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میچ مک کانل (Mitch McConnell) سناتور جمهوری‌خواه تندرو و ضدایرانی هم که یکماه است ایست قلبی کرده و در بیمارستان بستری شده و هیچ اطلاع دقیقی در مورد وضعیت او در دسترس نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670516" target="_blank">📅 14:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم حملات گستردهٔ اوکراین به نفتکش‌های روسیه در دریای آزوف
فرمانده نیروهای پهپادی اوکراین:
🔹
دیشب ۱۵ شناور روسی از جمله ۷ نفتکش را در دریای آزوف هدف قرار دادیم که تعداد شناورهای منهدم‌شدهٔ روس در ۸ روز گذشته را به ۱۰۵ رساند.
🔹
طبق گزارش‌ها اوکراین در هفته‌های گذشته دست‌کم ۴۰ نفتکش روسی را در دریای آزوف هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/670515" target="_blank">📅 14:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFEmPzkCB9GDuv76NbRp04cVKcXnj-3YATwIdSpSKklGUZjCWWhuYQyX8t8rPqFm7CtlYwPnzo9IUfZCjSXtoeIDONeh5qKEor5Khlno3O3UpsTEfEdz1UYsOK6DW2bZ7b5lBwV7L0jCfhSEF7xkOouiWaB0EzTRF9QKp1MhDAZjDkdnj266MFjmtGLS6dSuZDW92R-Bz2TD29N7Gb6TthU9BbAdKvHSmbR-qHqNLvuFNcItxHil1wSUlpRAr9NvwGiglE1O3j5pi9PZJgC89nR6FkL5pWbd2ol_M3JBYpvcgBgCL9ALrN4GGVs0l6Isa7XmSh1HH2ZfnNqA7ubX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/670514" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/670513" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670512" target="_blank">📅 14:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3OXq-7iRgYicHRq61yhNV12Lz67G8IwWxJhU2lIegwOZZWrOkUv4AjbXNKJb73vubwyqnFkZ9z5b0GSc792n934j8B-olBw2ACbk-eFcq7Egpzcc90EWydOpI1tWyZWPNmXiCDXdd8k2r93PihMJTbj5HFvELTqJrHz9_ij_CP9Gm0m1PEoxJep1pp1noRxm1sF_M7SdYOWY-CUFzgkv4-9P-J1Ox6iQ8nanUAA4uKFTK46ZK2v3dDVrnqHazEEEtaKv4pcRrH3-EXaTqY8JOJ6oT_q2CEYEQH3-ckY9hqV-Vo5kDITLuZn-UbXWlA2y8I6W58NLsiyP9fx8GuiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین بازدهی بازارهای مالی در سال‌ جاری
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670511" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670509">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ایتالیا: نمی‌فهمیم چرا نخست‌وزیر ما از ایران تهدید شده!
خبرگزاری آنسا ایتالیا:
🔹
تاجانی، وزیر امور خارجه ایتالیا، پس از آنکه چهره نخست وزیر در فهرست سیاه یک روزنامه ایرانی قرار گرفت، گفت: تهدیدهای ایران علیه نخست وزیر جورجیا ملونی غیرقابل قبول است و ایتالیا علیه تهران نمی‌جنگد و نخواهد جنگید.
🔹
این تهدید «غیرقابل قبول» است.
ایتالیا علیه ایران نمی‌جنگد، به همین دلیل است که ما دلیل این حمله علیه ایتالیا را نمی‌فهمیم.
«این یک حمله باورنکردنی است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/670509" target="_blank">📅 14:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
استانداری خوزستان: در پی تهاجم هوایی آمریکا به نقاطی در ابادان تاکنون دو شهید و سه مجروح گزارش شده است
/مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/670508" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به آبادان
«حیاتی» معاون امنیتی و انتظامی استانداری خوزستان:
🔹
ساعت ۱۳ و ۴۵ دقیقه امروز دوشنبه ۲۲ تیرماه شهرستان آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
تاکنون مجروحیت یک نفر در اثر این حمله گزارش شده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/670505" target="_blank">📅 14:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k08tjoHbcl3h_-Kpz9Y7K3A2YLHmtUx04kovuf0Mar5MJ-MaZJYICArJNfok5uMIilc1zKNLMfD0Hm5HClFy6D--WEiXYVZPBE40_K9pDMvHZMDs55kF7pD7IJagLa2UXBNYm40OK2pUzO8l2o7AEzHcCW3BCrFTJ-4a5shHCG4R8Hu9no7RBl_Iny0M2OIqC50raGWEgjsc6m09X9RF7QBfOtVz-8ww0Jnzeb6EBfxwP0N7Kq5PclgrJduepbviQ2mhJ7UyNDtqY2SHi9PKla8Tv2qfNpRj1_vWKIxb9uMqJkkSGs_ABELCxybEVLcgvJIo0boI-JO4yjJgdql3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما او را به خاکِ ایران سِپردیم؛ ولی یادمان باشد که او
خاکِ ایران
را به ما سپرد.</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/670504" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهان‌بخش پس از بازگشت از جام‌جهانی، نانوا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/670503" target="_blank">📅 14:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش آسون و خلاقانه سرخ کردن سیب‌زمینی، مهمونات رو شگفت‌زده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/670499" target="_blank">📅 13:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670498">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRbvwugMO_u5RYEEGAyWDGMVfYF8IKFd9cwDl0Unxp-fObMFGhgk9mB97w10bqGWC3WEtyikyrez2iiJaGlw1TVHGT50dzvEg_atF78wjEclefmIpjOhShqjJJHhI82EE4VHvY6ttiHHMx8FBMySU4cmJw2c8gIP-PucGYbKmmOU_Q7d1ult3ifQjFm-jav1zzAvNxj1y-jvel6wylVavCNf_Ti-DQ3DeCQ7A3mav888ecXi10YyOnV9eW5MTaA7ysS3ZzIhXnTf5AmrKd65Y0rUFDMws9Q5qeAGCWTyDjAbAFT4I4kmdic7rCBXNpV9nAkGIMUEyW7JXgYJIc61uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران فاتحه دبی و دوحه را خواند!
🔹
تازه‌ترین گزارش شاخص جهانی زیست‌پذیری اکونومیست از افت قابل‌توجه جایگاه شهرهای خاورمیانه، به‌ویژه حاشیه خلیج فارس پس از جنگ با ایران خبر می‌دهد.
🔹
در رتبه‌بندی ۱۷۳ شهر جهان بر اساس شاخص‌هایی چون امنیت، سلامت، آموزش، فرهنگ و زیرساخت، دوحه با سقوط ۷ پله‌ای به رتبه ۱۰۸ رسید.
دبی و ابوظبی نیز هر کدام چهار پله تنزل کردند و به‌ترتیب در جایگاه‌های ۷۹ و ۷۶ قرار گرفتند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/670498" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670497">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ارز اربعین از بازار آزاد گران‌تر است!
🔹
با کاهش قیمت دینار در بازار آزاد به ۱۱۰ هزار تومان، نرخ ارز اربعین به نزدیکی ۱۲۹ هزار تومان رسیده است./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670497" target="_blank">📅 13:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnpTKCH_ayeabqMroPJoQGjPhT-dbtITXPe-toPNfR-QjoZzRROAPHHDIKFruduHIeG0l6ErGMBF8ItKS7U9h-N6vTyATnTmzQeWApIyAAZ4DfcaxkMfA5BWRmKQ06TFB-nKGaHTpKIABBB3zMQW5ecw4ODMOIthyJW6VUEulxtThLKA-J4stxrm331U04-HnqVW3Wyyc7epNp4AIA9VEVsr77HFkGCEirs4IkcPT3-ddl7kF5RhXqEc2yolBhjFelxDKQ9ixI7J8m0M2T3PLVJ-ae9otz6dNv_bVvVtKYGZbxzmScdDGQK9_6G9AqLUdzO2MEaj-VmN4J9pK4-iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۲ تیر ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
قیمت دلار امروز در واکنش به درگیری‌های نظامی ایران و آمریکا در تنگه هرمز و انسداد مجدد آن توسط ایران، آرایش صعودی گرفت و در آستانه ورود به کریدور ۱۸۰ هزار تومانی قرار گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670495" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
چین خواستار عبور آزاد و ایمن از تنگه هرمز شد
آناتولی:
🔹
چین در بحبوحه حملات نظامی مجدد بین ایالات متحده و ایران، درخواست خود برای عبور «آزاد» و «ایمن» از تنگه هرمز را تکرار کرد.
🔹
لین جیان، سخنگوی وزارت امور خارجه چین گفت: «تنگه هرمز تنگه‌ای برای دریانوردی بین‌المللی است. از سرگیری عبور آزاد و ایمن در این تنگه در اسرع وقت به نفع همه طرف‌ها است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/670494" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
خیلی ساده و بدون هزینه از این دمپایی روفرشی‌های ترند بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670493" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دارو ۵۴ درصد گران شد
🔹
با اعمال موج جدید افزایش قیمت دارو از نیمه فروردین، میانگین نرخ داروهای تولید داخل ۵۴ درصد رشد کرد.
🔹
در این میان، اسپری‌های دارویی با جهش ۱۶۳ درصدی و ویال‌های تزریقی با افزایش ۱۲۷ درصدی، بیشترین رشد قیمت را ثبت کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670491" target="_blank">📅 13:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مصاحبه اختصاصی خبرگزاری وایس آمریکا با فرزند شهید تنگسیری و دلایل بستن تنگه هرمز و حمله به کشتی ها در تنگه هرمز از زبان ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/670485" target="_blank">📅 12:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مسیر پیاده‌روی اربعین از بصره تا کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/670481" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670479">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
جزئیات از حمله ارتش تروریستی آمریکا به تاسیسات آبی خوزستان
🔹
مدیرعامل سازمان آب و برق خوزستان از حمله بامداد دوشنبه ۲۲ تیرماه به ایستگاه پمپاژ زهکش RMD در محور ماهشهر–هندیجان خبر داد. در این حمله، «شاکر محیسنی» به شهادت رسید و یکی دیگر از کارکنان مجروح شد.
🔹
این ایستگاه نقش حیاتی در مدیریت زه‌آب اراضی کشاورزی منطقه دارد./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670479" target="_blank">📅 12:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جورج گالاوی، سیاستمدار مطرح انگلیسی: لیندسی گراهام مسئول ریخته شدن خون میلیون‌ها نفر است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670477" target="_blank">📅 12:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKYy73x7kQO4xuD9Ogt0UzK1BjltTQWxxrxWUzn1kb4UHyGI0h4oApvOWnq-0jCTHmxHPtbt52PxnBwsQ0LjUeS-zwe1I2oDDiG4RF5sqkt0cwuxnfF5JamjiUYzaoZQ2Z60DyOuZpZR1IOLM69uscERdFYbbQst4D9HOWcbRUB1vcGKD27My0VrJXTR6mCgmHHX7IpcLvvQUFrxcbRDjQgheQ1NTG07c0_owocOcELeUCNBz-9k368hjRLnV03h3gnmtN4lRQapHrNzRctUo3gAA-47o9hZYamtQcHSlFENYGIArVmWHJ3sMDM_yf0yfVbPD-tDFvsym2nN16_eaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سم نیل، ستارهٔ پارک ژوراسیک، درگذشت
🔹
سم نیل، بازیگر سرشناس نیوزیلندی که با نقش‌آفرینی در فیلم‌های ماندگاری چون «پارک ژوراسیک»، «پیانو» و ده‌ها اثر سینمایی و تلویزیونی به یکی از چهره‌های محبوب هالیوود تبدیل شد، در ۷۸ سالگی درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/670476" target="_blank">📅 12:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670475">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حمله دشمن به منطقه‌ای در محدوده شهرستان نایین‌
معاون امنیتی انتظامی استاندار اصفهان:
🔹
در دقایق اولیه بامداد امروز دوشنبه ۲۲ تیر، حمله دشمن آمریکایی به منطقه‌ای در محدوده شهرستان نایین، یک شهید و هفت مجروح در پی داشت.
🔹
مجروحان به‌صورت سرپایی مداوا و اوضاع تحت کنترل است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670475" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QghoFsjUwxpfJApow3DikuaJpAh08sE4IaW_1MAWMxpZaHBslytJrXZ-j8sqY2QlvOjSfHaswrN_BSl4rKexesnekcKTf4GAKSSkwK3ryuGxkJCjGR6dSM6E-o7YcDZ4GiHki_s9XFpaDPywQ5pv5gG2MJTuPh984O-EVxhC1_AWK16a-Vovb1WUSTFiSGqCXPw_uf02h0w6PZIPUvo-7a6JceNj_8BVKcqh6WyPjDgaIDnt1GRxTlVQfZ-eVbmqhpwRxjS6Ll4so-Q9BIlWZqImpnR1HvI2AoGrHewEVGacRe_AomcOIPsnCreBH14SG1ZwyuQRE1tZ0gvinrEJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران کدام نقاط کلیدی آمریکا را زیر ضرب برد؟
🔹
در پی نقض بندهای تفاهم‌نامه، ایران مجموعه‌ای از اهرم‌های اقتصادی و نظامی خود -از انسداد تنگه هرمز تا هدف قرار دادن مواضع زیرساختی، لجستیکی و کنترل دریایی آمریکا در منطقه - را فعال کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/670473" target="_blank">📅 12:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670472">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بقایی: سفر لاوروف به تهران در حال برنامه‌ریزی است
.
🔹
توزیع کارت آزمون ارشد آغاز شد.
🔹
علی‌اف: روابط میان آذربایجان و روسیه عادی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/670472" target="_blank">📅 11:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670471">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در فرایند دیپلماسی دست‌بسته نیستیم و استفاده‌هایمان را از این زمان کرده‌ایم و خواهیم کرد
🔹
می‌دانستیم که آمریکا پیمان‌شکن است و با علم به این موضوع و با چشمان باز از ابزار دیپلماسی استفاده کردیم.
🔹
مردم ایران تجربه تلخی از پیمان شکنی آمریکا دارند و برای ما دیپلماسی یک ابزار است و مردم ایران حامی تصمیم گیرانشان هستند؛ شیوه و کیفیت مذاکرات دیدگاه طبیعتا متفاوت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/670471" target="_blank">📅 11:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670470">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف‌های بی پرده یک روحانی: بسیاری در لباس روحانیت زندگی یک نسلی را نابود کردند و وجهه دین را نیز خراب کردند
/ تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670470" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب بقایی به اظهارات وزیر امور خارجه فرانسه درباره ایران
🔹
وزیر امور خارجه فرانسه دوست دارند هر از چندگاهی صبحتش در نشست سخنگویی انجام شود.
🔹
فرانسوی ها باید یاد بگیرند درباره مسائلی که به آنها مربوط نمی شود انتظار نقش آفرینی نداشته باشند.
🔹
اروپایی‌ها نباید رویکرد مهدکودکی خودشان را به دیگران تسری بدهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/670467" target="_blank">📅 11:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امورخارجه به ادعای ترامپ درباره درخواست ایران برای مذاکرات؛ طرف آمریکایی صادق نیست و یک بازی روانی است
بقایی:
🔹
ایران با میانجی‌ها در تماس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/670466" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نیوزویک: ایران ترور ترامپ را برون‌سپاری می‌کند!
ادعای نیوزویک:
🔹
تلاش‌های ایران برای ترور در خاک ایالات متحده معمولاً شامل برون‌سپاری واسطه‌ها می‌شود.
🔹
تهران به جای استفاده از عوامل آموزش‌دیده خود برای حمله، از منابع خارجی استفاده می‌کند و واسطه‌هایی را برای استخدام شبکه‌های جنایی محلی یا افراد مسلح اجیر شده می‌فرستد که امکان انکار را فراهم می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/670465" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670461">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◼️
بدرقه یار
◾️
پیام‌های صوتی مخاطبان خبرفوری در پویش «بدرقه یار»، آخرین جمله به رهبر شهید؛ بازتابی از ارادت، دلتنگی و وفاداری مردمی است که حرف دل خود را با رهبر شهید در میان گذاشته‌اند.
◾️
این صداها، بخشی از بدرقه ماندگار ملتی است که در سوگ، همدل و در وفاداری، هم‌پیمان مانده‌اند.
◾️
کانال رسمی سوگواره «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/670461" target="_blank">📅 11:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ منفی سخنگوی وزارت امورخارجه به ادعای گروسی مبنی اجازه ایران به آژانس برای دسترسی به تاسیسات هسته‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/670460" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران دولت فعلی افغانستان را به رسمیت شناخته است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670457" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
