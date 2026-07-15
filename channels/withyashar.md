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
<img src="https://cdn4.telesco.pe/file/XEPx3HeecqAQ_V7GpJs6yHCUO5awMV3VnjdAmJPAP8r-7xFT1PY8uZpXj-PRXM6luH5xsWcJjbx5VbnVyorpEuxOfIvVhqO0kMn-36PLab4aD51J10PVdUECAvneSpsKNCZM7FeRwx3rW7Btg0R5lIZCqXR2vmPnwS0Vo0zjI6HG6Nq0Gn3QkSFCOQv6d6fxXoXw_hN-tgqM3Col7eldz8Bsr0hkT2WOU8jdCqh8I2R3axJvirZRsRLvVnslLAZ9_sZSwLTX2sfZSdG4WzPiwxdsJnCP5JdBGOg8rFpo-as7YIepG66xiEp6S0EPpOhiIRpxqyb7QVZMr_Q8KGjYvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 392K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قالیباف : انتقام عمام را میگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/18246" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف:
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
، در غیر این‌صورت
اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/18245" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت خارجه آمریکا:
از تمام شهروندان خود می‌خواهیم فوراً ایران، عراق، لبنان و یمن را ترک کنند
@WarRoom</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/withyashar/18244" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/18243" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری آکسیوس گزارش داد: به گفته یک مسئول کاخ سفید، سفر نتانیاهو به دیدار رئیس‌جمهور ترامپ در هفته آینده در برنامه کاری او قرار ندارد و باید منتظر باشیم و ببینیم چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/18242" target="_blank">📅 20:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/18241" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEXN_qFiPlmiKdS3bSUgvgQJmOOthtKpEvWTL3niSDU9EmsPasm5w7XttTIgHp9qtok6Gb-CMx_shWAXGTOySUXfKXtPQEA55bwwSa_vppOoFSNnHfnlQSe6tZMGFwzqSu0_2ll1ULIB_xMGshe0Se23ECPtQAl2e8xKbwKF4mMlC3WBPyaigIYnrmvprS8IkPgSco1NjQzk9qnBzJUEiz58QuCBy4b7WDwnFDHL5_RuVtVllOxG0NzpRdmrJqDWSmoO8ukiYFcZkHQE1wYEAboNAxOqZqcvEfUvz5TgX1-teFs9v7K_2fvfRwedvSasLTQIhqk4cmepVKDEdcrtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۷ تن از سربازان ارتش ایران که در جریان حمله نظامی آمریکا به منطقه بمپور در جنوب شرقی ایران شهید شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/18240" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند. @WarRoom</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/18239" target="_blank">📅 19:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حمله ۳پا به کویت : انفجارهایی اردوگاه پیونگ متعلق به ارتش آمریکا در کویت را لرزاند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/18238" target="_blank">📅 19:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRZhkGYWisppIFRJrgUlM7cCIATrNGA8t1Nd-grHjQFEwueTVnsLgu56oYq81RNtWhrJmjqyT6MGus_AEBbjdwjWY18K5wmPhn5XDs_2Yxl_bXxWOxDRXVhOhur3Ri-KYQ5ly4_4jbZnpOJOA_ZQ5ZX-4ANXKBYE7N6Iw_eDV2D-oyRfHgHoA28jAeUDv3UmYG4ID166AopVG89H34Flj8gXWj80OhxI48oyQdSGEla-b_QIkRnCFwHMhTulum5lizU-inZmMUqp6kDHk8qdspKmhzDW9ozhwiHDh2wD_M3tU_5BrgII4lHAEoRcPh1Ike5x85q8ajzlJQ7FswgIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یابی سنتکام :
ادعا:
رسانه‌های حکومتی ایران مدعی شده‌اند که نیروهای ایالات متحده در ۱۴ ژوئیه یک سیلوی ذخیره گندم غیرنظامی در هویزه را هدف قرار داده‌اند. این ادعا
نادرست
است.
واقعیت:
در ۱۴ ژوئیه، نیروهای ایالات متحده مواضع نظامی ایران را در
بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک
هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را کاهش دهند. در مقابل، ایران غیرنظامیانی را که در حال عبور از تنگه هرمز و همچنین در کشورهای همسایه حوزه خلیج فارس بودند، هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/18237" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیل با بمباران هوایی، جنوب لبنان را مورد حمله قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/18236" target="_blank">📅 19:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارت بهداشت ایران: از آغاز حملات آمریکا به جنوب کشور، ۳۵ نفر کشته و ۳۰۰ نفر مجروح شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/18235" target="_blank">📅 19:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ به فاکس نیوز: خوب خواهد بود اگر اسرائیل در لبنان حضور نظامی خود را کاهش دهد تا بر مسئله مهم‌تر یعنی ایران تمرکز کند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/18234" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18233" target="_blank">📅 19:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اوفک، چهار فرد و سه نهاد را به فهرست افراد و نهادهای تحریم‌شده اضافه کرده است. بهروز نمازی، شهروند ایرانی، به دلیل ارتباط با سپاه پاسداران , دونیا اتایب، شهروند ایتالیا، ماریا سلینا و وادیم دروژبین، دو شهروند روسیه، نیز به این فهرست افزوده شدند.
از جمله نهادهای تحریم‌شده، شرکت ایرانی نیکا جت، شرکت روسی آوراتک و شرکت ونگارد تاکتیکال ساپلای مستقر در نیجریه هستند. وزارت خزانه‌داری آمریکا اعلام کرد این نهادها با بهروز نمازی ارتباط دارند و مشمول تحریم‌های ثانویه شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18232" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18231" target="_blank">📅 18:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش از اختلال شدید اینترنت
🚨
😔
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18230" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دور مذاکرات بین اسرائیل و لبنان در رم، ایتالیا، به پایان رسید. مقام اسرائیلی گفت که مذاکرات خوب بود و قبل از شروع مراحل اولیه مناطق آزمایشی، به مقدمات و توافقات بیشتری نیاز است. او ادعا می‌کند که این امر در روزهای آینده محقق خواهد شد. در همین حال، یک منبع…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18229" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امیرحسین ثابتی
: نقشه قطعی دشمن ترور رهبر جدید ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18228" target="_blank">📅 18:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59153729d1.mp4?token=EOHGYl2DRPwTQfluKuyntKoAW3u_4k4Gs0LKPU1IEC2Y2UeKN7CbKv5YOOWT8o6kaCdRIImcNglXmNGd9aXBhcwrTkk6xLiyfalKpWHjmS7Ex82sD5W0zHgI428QynfHZBt6u_uDoYPI_PMuowlH2hkgj7Ozy0XhKHPtIRdIiqTVT0KBVep5s85MdcLI_qKl8zMseZ6hYqRW2DUYkl42kmW0DXJ30cUO25aMZP66c0pXD8vWDAIPpa9lee8ej6pR8ckS2JjF8QdfJMexhng-8Ai6peXZVcmiQhE0Im_qMH4PXQYn4Z8mwCiesrsa6kok98qK1y_IliH6bVr_oaYI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جولانی وارد عمل خواهد شد و کار حزب‌الله را یکسره خواهد کرد
او این کار را به شیوه متفاوتی انجام خواهد داد. فکر می‌کنم جولانی دقیق‌تر از اسرائیل عمل خواهد کرد. او ساختمان‌ها را تخریب نخواهد کرد.
جولانی خودش مایل به انجام این کار است و من دارم به چراغ‌ سبز نشان‌دادن به او فکر می‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18227" target="_blank">📅 18:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تا ساعتی دیگر ممباقر قالیباف درباره جنگ و تحولات کشور یک بیانیه مهم می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18226" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجار جزیره هنگام
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18225" target="_blank">📅 18:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!   فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18224" target="_blank">📅 18:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f54be6fd8.mp4?token=mTaR9xkWAHMkS2FIN3ScxElojKsXQDetFTFHtO10G48zeTTrHJtPGXSO6NiJ6BsKyL2JkF7USZDCDTOgzKelWKudJThS3JME4SmVN3w0sLN2quOiYpYICrUPnRvTIVv2zu6zJcWMzlr1oGA_h_Jy7vTVU_IWRmKiXT0VddzsdWwtVCQS7JA6NyAzGFPboveA1SCJJX2sGEmZWKRItk88lK9z34Z7JJrNUST6MawhIjlcG64ENnfLpK6nBwxCBvsSzv27wiTuAvUcr_bwbwtUyOQ9-t_oELVwbSA6lc8VqIqDPBrGlPw0RUU04vWqDpjVQFCBcMaOy3CIvSoVGV0uRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه با استناد به این ویدیو : محمدامین دهاقانی رو  به جرم آتیش زدن فرمانداری و تخریب اموال عمومی و فیلمبرداری برای رسانه های موساد؛ صبح امروز اعدام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18223" target="_blank">📅 18:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c80c5db7.mp4?token=jYEUVbN7KFPkl49rgV75FYo6B59z_dhrXCapk2JvlF5XRysJMKg3EiJFm7OWtYimb1a6haXIb5dXFwYcz-Mo8FOD2Rww242_9FEcrh0rrwWs3jKVqBNbHeALh_79oq0U0GOsgkiKd296IfBa2rlahLmBqPI0oSwBhHQnP-DuhSmdMsmgbeMk_xCcRCMca2sq7aSGaWbt7ykbeAbsVyWUQM1J3M4ktEHfVksiTf1FUxPigT2fZBeDp7wsjsl_yyD7fkPi-p6p2kocMKvaAa_NcU-_qNEaSnanu7eVrRJ6mIpsAxEgtTPS2rROex7SZKXhOpyDtWbzKRsJ3c8-oeY_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c80c5db7.mp4?token=jYEUVbN7KFPkl49rgV75FYo6B59z_dhrXCapk2JvlF5XRysJMKg3EiJFm7OWtYimb1a6haXIb5dXFwYcz-Mo8FOD2Rww242_9FEcrh0rrwWs3jKVqBNbHeALh_79oq0U0GOsgkiKd296IfBa2rlahLmBqPI0oSwBhHQnP-DuhSmdMsmgbeMk_xCcRCMca2sq7aSGaWbt7ykbeAbsVyWUQM1J3M4ktEHfVksiTf1FUxPigT2fZBeDp7wsjsl_yyD7fkPi-p6p2kocMKvaAa_NcU-_qNEaSnanu7eVrRJ6mIpsAxEgtTPS2rROex7SZKXhOpyDtWbzKRsJ3c8-oeY_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: وقتی عملیات خشم حماسی رو آغاز کردیم، فکر می‌کردم تغییر رژیم در ایران ممکن باشه.
اما هرگز تصور نمی‌کردم حکومت ایران حاضر باشه برای حفظ قدرت، 52 هزار نفر یا حتی یک نفر رو قربانی کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18222" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!   فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18221" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78e56925.mp4?token=Z5n321mm4Bhjz7KudfvchmDjyA_pl2HL2TAGukJTHjtK8jOjFBUY1kjD7rp61p0uhCBAZx9zuf50ZgiI3xJ05vRFL0t8iSbnPSTukkR-vyt_yUGXACcg50Q3ZDosMMN7UloVRvO1K7lmi48eDD4Qac0mk0T4snUmwl00qKrjTsuWciz-WIrN06Lrrx8SENoCL3cgXOi5mtv0eziJwD3dloCAJZj_Cy-q6QbyYNvIGrHdkrBjkfS5MHkrhEX6YcxoqdqNW6ff2mjol25-5eULdxRKMxSQBggDSaXFgJSag6AguWSg5cWBp4pFVH5AoVYhDf4auwZP-ExSFGqADiwv9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78e56925.mp4?token=Z5n321mm4Bhjz7KudfvchmDjyA_pl2HL2TAGukJTHjtK8jOjFBUY1kjD7rp61p0uhCBAZx9zuf50ZgiI3xJ05vRFL0t8iSbnPSTukkR-vyt_yUGXACcg50Q3ZDosMMN7UloVRvO1K7lmi48eDD4Qac0mk0T4snUmwl00qKrjTsuWciz-WIrN06Lrrx8SENoCL3cgXOi5mtv0eziJwD3dloCAJZj_Cy-q6QbyYNvIGrHdkrBjkfS5MHkrhEX6YcxoqdqNW6ff2mjol25-5eULdxRKMxSQBggDSaXFgJSag6AguWSg5cWBp4pFVH5AoVYhDf4auwZP-ExSFGqADiwv9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ممکن است تصاویر مدرسه میناب با هوش مصنوعی تولید شده باشد!
فکر نمی‌کنم هیچ‌کس هیچ‌وقت بتواند بفهمد آنجا چه اتفاقی افتاده. همچنین ممکن است آن تصاویری که در اختیار دارید، با هوش مصنوعی ساخته شده باشند. به نظرم هیچ گزارش قطعی‌ای درباره این موضوع نمی‌ شود داد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18220" target="_blank">📅 17:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : صحبتهای ترامپ که الان پخش میکنند قدیمیه</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18219" target="_blank">📅 17:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زلزله گرگان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18218" target="_blank">📅 17:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه مکرمه در جنگ علیه ایران استفاده کند ، بدین ترتیب این شهر مقدس به سپر حفاظتی برای نیروهای آمریکایی تبدیل شده است @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18217" target="_blank">📅 17:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صداوسیما: دلیل حملات آمریکا، پنهان کردن شکست و ناتوانی خود بوده که با پاسخ قاطع و قوی‌تر نیروهای مسلح مواجه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18216" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایلان ماسک می‌گوید
ایکس (X) پس از تکمیل بررسی امنیتی، کل کد منبع خود را متن‌باز خواهد کرد
و از
بررسی‌کنندگان مستقل دعوت خواهد کرد تا تأیید کنند سیستم فعال و در حال اجرا، با کدی که منتشر شده مطابقت دارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18215" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش صدای انفجار اهواز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18214" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام : از زمان آغاز مجدد محاصره دریایی بنادر ایران در ۱۷ ساعت پیش، نیروهای آمریکایی مسیر دو کشتی تجاری را که سعی در عبور از این محاصره داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل این مقررات اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18213" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زمین‌لرزه‌ به بزرگی 3.2 ریشتر خرمشهر رو لرزوند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18212" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دور مذاکرات بین اسرائیل و لبنان در رم، ایتالیا، به پایان رسید. مقام اسرائیلی گفت که مذاکرات خوب بود و قبل از شروع مراحل اولیه مناطق آزمایشی، به مقدمات و توافقات بیشتری نیاز است. او ادعا می‌کند که این امر در روزهای آینده محقق خواهد شد. در همین حال، یک منبع لبنانی به تلویزیون قطری "الجزیره" گفت که "این جلسه با توافق بر سر دو منطقه آزمایشی، یکی اشغال شده توسط اسرائیل و دیگری در مجاورت مواضع آن، به پایان رسید. جلسه بعدی هیئت‌های نظامی لبنان و اسرائیل را گرد هم خواهد آورد. تاریخ و مکان هنوز مشخص نشده است."
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18211" target="_blank">📅 16:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به علت پیام و سوالات شما لازم به ذکر است بررسی ها نشان میدهد هنوز هیچ رسانه یا شخص معتبری برکناری «علی جوادمردی» از بخش فارسی صدای آمریکای را تأیید نکرده. همچنین پیج اینستاگرام این شبکه همچنان او را فالو دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18210" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3meE42_-2DeRVu1YB92tuopgc8lhFNfsKaKcUEjF6TQCAYFPvQjdUUl_vvBfn-dzqHbnanoB7SNlERRq2hq281dRgFYuulAjydrZSDt29a5WXqYb14p3Krzr5yG7to__HLjuchEDWf-jrppvdY-gALSrTexffnSrkLbpvOQTI01vT6rAOaKqx_GEY2qyhLcsML7ADx9hWnqKRYKm-jA_hD_bKO6OmXvlrQciu83U_7e_hkbMUNXAZcHrVOwZ2PIaDrGl4cPpBhtYMHBupr5z6kKIPwBGKTmNjswTea45SfmyOGfZCoOApkD6tMhK66RsbyEPYfSXgLrqNXPScmiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سند در حال انتشار از وزارت امور خارجه عراق، که محتوای آن، طبق دستور وزارت خزانه‌داری آمریکا، حزب الله لبنان را به عنوان یک سازمان تروریستی طبقه‌بندی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18209" target="_blank">📅 16:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رمضان رحیمی عضو کمیسیون آموزش: کنکور سراسری در صورت ادامه‌دار شدن تنش‌ها، به تعویق خواهد افتاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18208" target="_blank">📅 16:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAUlKQrFZVl20zyYbLyxZ1E9UJT-SbXNCIUpuW4ZLiPR3Br2M9ZJzAgvv_exE0BnHtgXYREad4TfYsZ61deVGfGnWJtjzS8SzLjqj91hJ34rRI4v7LdIW0ad66XbB7rnRE9bQ95RbZxTwnIrTfdRYLVV--ajSRSgBueJeCLNHGLq03iM4afgiNxuUVJLeEzOxYCaKRIw0rkm4SboyEQTXYx0d-LM2W8ZCaknyN_50HPy5mIkA3KzCUQwsksZf0_72OAHRSslYd5KWj9HYkMnnDAZ0B35oS7d2DH4vuPY3awP7NDSLagfM_sDvCeZtU4pfpV6pp7ZCn6LJrIpCIP4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود احمدی نژاد در سفارت قطر برای عرض تسلیت
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18207" target="_blank">📅 16:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnjTuVvJ8PIbV4bk6qgs85xQzRJ_SXQJdnrxXq6Y9Y0VB801oWsIgWHCABDIn-sKeSYleT8v0vXDGHtHOKwI3njZPhzz6oJ_rkx9k7HewhSjVMD6c3F6bULWHDGYMkChJKS8imJ62RUG7xz4FTxBNjwHUgUW_0tuR4jr4KDIrZsHQ3O5wbMQmzmP3cVAhP7p8oHpK3ajPecaMLbBVnUBXprw0OQLqs4hwqu7IcKexqNy_G4xVv25YbX0eRfeFadm1Y_2iMBppLLT3Kmp4dGovdlOyHjpT_2QxBFyO3UhqoxTT-5Yj4NNBvKVR5xQLvvY812IXgS-lJY0m5ZtMm9shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز معاونت آماد و پشتیبانی مرزبانی بوشهر و زدن
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18206" target="_blank">📅 16:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فاکس نیوز: ایالات متحده صبح امروز به جزیره تنب بزرگ در خارج از تنگه هرمز حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18205" target="_blank">📅 16:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بر اساس گزارش رسانه i24NEWS، انتظار می‌رود دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه در واشنگتن دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18204" target="_blank">📅 15:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f16969a88.mp4?token=Dj-0rLIt4omNdovl5UOZdUyhRgj9BREWbvQZq_7-88VpBQwuAM9vWT_tIYWihsQ4Idrz2enoV7XZ94z32aO0xliqSvGvcZOMB2QCuuGFRTRtCT-MBgcAmYhvCOJfD82CtByqX3pXnbBdykvX9_1GHu7bLgagZvuYcCwOFdSdWeS6MdEUIk6JzHGJz6w9QoM4D27feJkQPgqpMwAyH7Ond_VVbR2WkDALFsGBuMtYhE4x3TkzjmNLAI2_PuJUAk_qewftRwVrDTxPmNZdimrwhAlwJgGhE2efz78oWXZrOXc_0Z2gdpQDdviZLQlHi1e51MRxgoWPVPBGNkF1XMQELQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f16969a88.mp4?token=Dj-0rLIt4omNdovl5UOZdUyhRgj9BREWbvQZq_7-88VpBQwuAM9vWT_tIYWihsQ4Idrz2enoV7XZ94z32aO0xliqSvGvcZOMB2QCuuGFRTRtCT-MBgcAmYhvCOJfD82CtByqX3pXnbBdykvX9_1GHu7bLgagZvuYcCwOFdSdWeS6MdEUIk6JzHGJz6w9QoM4D27feJkQPgqpMwAyH7Ond_VVbR2WkDALFsGBuMtYhE4x3TkzjmNLAI2_PuJUAk_qewftRwVrDTxPmNZdimrwhAlwJgGhE2efz78oWXZrOXc_0Z2gdpQDdviZLQlHi1e51MRxgoWPVPBGNkF1XMQELQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : سنتکام در طول موج ۹۰ دقیقه‌ای، مهمات دقیقی را علیه سیستم‌های دفاعی ساحلی و انبارها و محل‌های پرتاب موشک‌های کروز در جزیره تنب بزرگ شلیک کرد. این حملات، توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش کاهش داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18203" target="_blank">📅 15:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام: دور جدید حملات خود علیه ایران که از صبح چهارشنبه آغاز شد را تکمیل کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18202" target="_blank">📅 15:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایسنا: سفر همزمان پزشکیان و عراقچی به قطر
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18201" target="_blank">📅 15:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه مکرمه در جنگ علیه ایران استفاده کند ، بدین ترتیب این شهر مقدس به سپر حفاظتی برای نیروهای آمریکایی تبدیل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18200" target="_blank">📅 15:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتاق جنگ با یاشار  خبرنگار i24news:  به احتمال زیاد، این شخص که به عمان میرود وزیر امور خارجه ایران، عراقچی، است. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18199" target="_blank">📅 15:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe4f78461.mp4?token=GmzEt_of0NTcDm7y2DGX4qkbK8U5mRtR-6fgNeJSSvQWoGnx3PKck4Y8glvm3eTunLA2EapOZScAW_Pq-98uajLQuXaXQcPsDTw8lk8e0ebHkxCyK_IKGrggeHdEUQfroke6j9kiWVvpb31p54YNA-8QA96c284jXPUbOqLaDUjo9ZDYCKnvoD4pHCpv2j6h77FQPJb8nNG8XHzqnec7aJ-0Kips837kMJKbAH52fPa5vy2wconBacO-2xmQtrfBmUTAa-QLrWL5aoW-8GpWZma2iRKB3AoI3Duj5-OBMveVXACN2F_c9Q3fGmi7W_4qpDdwN0uSPynFDSDgrGEs7Ge95OM61Cd66Qfpctkyt3wxWcaNUDQH7JrFDIYEl19PptKWTqSlacqpPqTvk90d2nZLKN4g-mFkrqwnCMohUrGR8fmF4ckHqUqWAkMm757A5IUtSHXz1AOhq9IIMy2xBDQG73kld5gGEXnD-VwFilyqPuJu2MUleXOptq851mx4NuVD4LwQ-N3iVXC0dwQtFCYpYC02NXwciZqeY7ZzQ7HK2GFW06jLN0WIlvHVVLJLmZDppMcMG6caZyQ_pGifqqe6p2iAwthULXqmCQ21CL0RQ3YCFlKXl0bSx9teqjZXjcvC1wHj4fl4-xrsbntF6Tt0f87vyl46q24Ht4EsCqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe4f78461.mp4?token=GmzEt_of0NTcDm7y2DGX4qkbK8U5mRtR-6fgNeJSSvQWoGnx3PKck4Y8glvm3eTunLA2EapOZScAW_Pq-98uajLQuXaXQcPsDTw8lk8e0ebHkxCyK_IKGrggeHdEUQfroke6j9kiWVvpb31p54YNA-8QA96c284jXPUbOqLaDUjo9ZDYCKnvoD4pHCpv2j6h77FQPJb8nNG8XHzqnec7aJ-0Kips837kMJKbAH52fPa5vy2wconBacO-2xmQtrfBmUTAa-QLrWL5aoW-8GpWZma2iRKB3AoI3Duj5-OBMveVXACN2F_c9Q3fGmi7W_4qpDdwN0uSPynFDSDgrGEs7Ge95OM61Cd66Qfpctkyt3wxWcaNUDQH7JrFDIYEl19PptKWTqSlacqpPqTvk90d2nZLKN4g-mFkrqwnCMohUrGR8fmF4ckHqUqWAkMm757A5IUtSHXz1AOhq9IIMy2xBDQG73kld5gGEXnD-VwFilyqPuJu2MUleXOptq851mx4NuVD4LwQ-N3iVXC0dwQtFCYpYC02NXwciZqeY7ZzQ7HK2GFW06jLN0WIlvHVVLJLmZDppMcMG6caZyQ_pGifqqe6p2iAwthULXqmCQ21CL0RQ3YCFlKXl0bSx9teqjZXjcvC1wHj4fl4-xrsbntF6Tt0f87vyl46q24Ht4EsCqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار
خبرنگار i24news:
به احتمال زیاد، این شخص که به عمان میرود وزیر امور خارجه ایران، عراقچی، است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18198" target="_blank">📅 15:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانال ۱۴ اسرائیل: منابع آمریکایی از تشدید جدی تنش‌ها در منازعه با ایران خبر می‌دهند.
دونالد ترامپ، جلسه فوق‌العاده‌ای با حضور مقامات ارشد برگزار کرد. محور این گفتگوها، عملیات گسترده‌ای بود که هدف آن، پایگاه‌هایی در تهران و سایر شهرهای بزرگ ایران است.عملیات‌های نظامی قبلی، به طور خاص، بنادر جنوبی ایران را هدف قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18197" target="_blank">📅 15:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18196" target="_blank">📅 14:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjv-aYztWIyF9MFLz625_wMSe4GauR80ePlYZIOUbrsJNx07Z3VRvdWmt1Gg8i1PJj6OQYk1LXuTD5AAt1z4JC48NLUNSttNSnKMvIt4RZJvtwIBvO3MnqNkg_T-OxFw0FpGYcnaosIxovm7hM8vOOqEbwBYyhV3wF6X7nm735VYrdV9_dNYDXA_9imkI4sWTkWF0Yjm1iEn9HsAAdpNHLbpwTldY_gUKlWoPn0qh718HE3djL7uQuwyneeJ9ZpUCGXbpw_6Hu259FMB9yc6RbpvCpvAdsaVD6IZPNAuDzpEPtBKax0IN9BMlepnoVrDKCUOYB2O_vD6WyVGFrv7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب ایران دوباره باید تصویر بالا بشه و تا آخرین لحظه میجنگم براش هر حرفی‌هم که بخورم
🫱🏼‍🫲🏽
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18195" target="_blank">📅 14:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18194" target="_blank">📅 14:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U77xgDbuWVFsCviUEIxcBkjM36FxAfajzawcglz6MsDDxFDKCHSu8Mt9e_SXyQgqB_O_WNV74LABHXkej-RCO8kaMM0H96bAHiUoJcKSPniXOvFLEEA06VGUTlh8GyugG_edb4r8ZC3_tjH2S7dWZms1v_6bN6wl0qEtLxFW77T3Kh6Wb3KclGi7SyKtmnRrBxJZFyvxNQ0viA1I8O0vdX8GcAqqhtOvdDZLAS13PK96TVHghlo5wD-rOTozbDFtrK9ObWFgn1p7yy--T_gMsNducGPWjDW6x_AbwAI_Cs2tT_7oA9yd1MyAUA0iH82_tiKCsPyZ_tII3qo0W3AZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی قبل، دارلین گراهام، خواهر لیندسی گراهام به عنوان سناتور کارولینای جنوبی ادای سوگند کرد.
@WarRoom
اتاق جنگ با یاشار : دست خدا عیان شد , لیندسی گراهام جوان شد.</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18193" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایگاه هوای بندر عباس ۷ انفجارررررر
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18192" target="_blank">📅 14:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار مجدد شیراز ، سیمانش حرف نداره شرکت چیه حالا اسمش بخریم ازش
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18191" target="_blank">📅 14:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48130660b.mp4?token=Osa72NoxBjvLwrrhUuVSdKkUeAU-F6eRFiERwCVrf9abSAJ8VNHRYIOFleKxpD7igVN8b0b1dtRpxYGTg9El1MFEiqpd-ogad49AHKiSwRyEu7ddELo6iI71pQVX25OTlYnmAg0UTjAUyihVrCCgYr197VW1vcWWtc8ZsAEjQLfnPD3OnDAoP-TSD0dklOjzuNVo4is5-VD4aigpKb-oFr9CjkOdlNuwoT7jWLPyPEa_NToZ__oQ8dEmeBRs4K7gveRFtgX6UMo7n6KP_kwk1VNSm8Yp-jAYy-4Wq0PuNbJH4J378zRFFH8NpcrA8Ecy4yd7_Z2bb-Wdt5UsbTjB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48130660b.mp4?token=Osa72NoxBjvLwrrhUuVSdKkUeAU-F6eRFiERwCVrf9abSAJ8VNHRYIOFleKxpD7igVN8b0b1dtRpxYGTg9El1MFEiqpd-ogad49AHKiSwRyEu7ddELo6iI71pQVX25OTlYnmAg0UTjAUyihVrCCgYr197VW1vcWWtc8ZsAEjQLfnPD3OnDAoP-TSD0dklOjzuNVo4is5-VD4aigpKb-oFr9CjkOdlNuwoT7jWLPyPEa_NToZ__oQ8dEmeBRs4K7gveRFtgX6UMo7n6KP_kwk1VNSm8Yp-jAYy-4Wq0PuNbJH4J378zRFFH8NpcrA8Ecy4yd7_Z2bb-Wdt5UsbTjB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
😾</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18190" target="_blank">📅 14:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIKERDg1Q9BExuM8_ICV0G-UeQj74Qkvxasjgq4Cbca9fS8Mvf9AtJpX_0hzXkfru-lTXpQ6OKfAOiJ6ydJm3do1dRbK79dSVROjPOBq7jhrfeKYdNlrv7BaAp8dwUyyahyXAtUtmuxViSpLBX3bjuTfcem-HM09Xr_UwU8d-TlDPTiSdS4kUq_-BQ3_R4uwEka5Fuo-in3xj4TFtiZb0_NRcP7QjFByZBI5Y1PbQMzCXJ40UolKMF7t7ErDEzlR3WW9zuYKf941KOvHpKlC1WzA6HCJDW75Eq3JqehuXJIiAzo_w7UZB07RyEKK7e5PBI2MR87Pxn6xPYF0ZwIM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا از ضرب سکه طلایی جدید یک دلاری با تصویر ترامپ خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18189" target="_blank">📅 14:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18188" target="_blank">📅 14:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تعویق ۲ امتحان نهایی پایۀ دوازدهم در ۴ استان
صداوسیما: وزارت آموزش‌وپرورش اعلام کرد امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان در روزهای پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر برگزار نخواهد شد.
زمان جدید برگزاری این آزمون‌ها در این ۴ استان متعاقباً اطلاع‌رسانی خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18187" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هاآرتص: ایران کنترل تنگه هرمز را در دست دارد
روزنامه عبری هاآرتص: ترامپ گفته بود که تنگه هرمز را باز خواهد کرد اما مشخص شد این ایران است که بر بازی مسلط است.
ترامپ مدام با انتشار پیام‌هایی ادعا می‌کند که در حال تغییر دادن قواعد بازی در تنگه هرمز است اما در میدان این ایران است که شروط خود را تحمیل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18186" target="_blank">📅 14:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدای توافق شیراز
🫱🏼‍🫲🏽
🤣</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18185" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18184" target="_blank">📅 14:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18183" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار دوباره شیراززززز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18182" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18181">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام): «نیروهای فرماندهی مرکزی ایالات متحده از ساعت ۶ صبح به وقت شرق آمریکا (ET)
(۱:۳۰ بعدازظهر) به وقت تهران
موجی از حملات علیه ایران را آغاز کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18181" target="_blank">📅 13:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خود آمریکا گردن گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18180" target="_blank">📅 13:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKNM0u990ptyYapeCx5lB2geEl9C_L-GhHz32ixPyt4zHaqKhF4sz98F4ZqmZiE2YOJ1xYi2GAcN-1C1XDekSarGf9AdRjNQRIjIKdhEBUszdD3N6vsYtNSJdhRpIPuSIT0cxAKxMWsUdtndVuxKDar-S2T332-ChlhUV46OmuALWe7FgwS_mnG9TtxINr8vhYxE0intVM8qgqch_wTQlx1wiSnXE9rWPAS3Bl2n9CbszkorrZfp7o0G1U3pN7Ulag1r0dxcPmRiwdx666bm1zGvvvJa6GGFLss1tLFWAVSg19-QcTF9JZnmqpXLvBT0S7cGZ6TjR6IUoCvOpjC2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی‌نیست دارم سیمان جابجا میکنم
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18179" target="_blank">📅 13:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18178">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجار شیراز چرا و چگونه
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18178" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE6utGOH2kdLGGGWjhU_moOCOtrt8fiV8Qg_pbPy47lyYvDAlESrz8ageJ06T8M-kBX0MKMEKuP43jynNcLFd6cc0h7AoJuJ-GtxPlb9gvjv0I52iB1byELaSzFtEk-jvnRAmuQ1qUQwNsz-4e_MN5CDPFq92OVmljsnGPkMPOAw4TX2ajUB4HlB4iNRJbESDuKxL1jQkXKLRFcBW2y-zVWQaO7SrdWCz-iXushamqHmIybwSWLfOF7sfGovgKcmLbwSHbKh_k7YfXkQdcBZR2-L9Yl_LASUf4QxumkCaqlOA6qBv0l_ChYYEpP0dOStz4-dVbJ2gjsV3rr4FRDiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای اولیه که ما نمیتوانیم تأیید یا رد کنیم، اینه که هدف حمله شیراز در دقایقی پیش یک پایگاه موشکی در کوه بوده.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18177" target="_blank">📅 13:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18176" target="_blank">📅 13:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مقام ارشد امریکایی به سی‌ان‌ان:
ایران از توافق‌نامه تفاهم با ایالات متحده خارج شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18175" target="_blank">📅 13:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18174" target="_blank">📅 13:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18173" target="_blank">📅 13:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش انفجار چابهار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18172" target="_blank">📅 13:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fd8c081a9.mp4?token=nlZVCgKJM6p6riYXVX43sONfoBT9u6iyqGZtrpQXZiy2wSmS-l99sPjz0loxWE-FJnBhWaKaRNjTPV4oOE7mXVmX5aHdVNKU4y-Li8GWJWvdbzzZiXE6tI6HNXsr6wTb4v7jGVhyzsjbsCsW1EKb8OTQnYe4VDU5xpB06A56NwB7l3FbGO4O3hdt2EJSHWOte0ZUmTlzOy-mDcMN0wvsTgq9W2qKQ9Z7lFC8C93pKwrkbaBjHx_eLuy4GEaphcBJofg3qjpFg7DiXR4cqqaPim19aZ3VlIN__kCJuyRXZYJ6okuAivdl5IenXfMYtR4BtdF79g3KqKtxksHyovU3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fd8c081a9.mp4?token=nlZVCgKJM6p6riYXVX43sONfoBT9u6iyqGZtrpQXZiy2wSmS-l99sPjz0loxWE-FJnBhWaKaRNjTPV4oOE7mXVmX5aHdVNKU4y-Li8GWJWvdbzzZiXE6tI6HNXsr6wTb4v7jGVhyzsjbsCsW1EKb8OTQnYe4VDU5xpB06A56NwB7l3FbGO4O3hdt2EJSHWOte0ZUmTlzOy-mDcMN0wvsTgq9W2qKQ9Z7lFC8C93pKwrkbaBjHx_eLuy4GEaphcBJofg3qjpFg7DiXR4cqqaPim19aZ3VlIN__kCJuyRXZYJ6okuAivdl5IenXfMYtR4BtdF79g3KqKtxksHyovU3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار شیراز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18171" target="_blank">📅 13:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔸
آیت الله اعرافی مدیر حوزه‌های علمیه : تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18170" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ستون دود ناشی از انفجار در فاصله بسیار نزدیک از تخت جمشید. @WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18168" target="_blank">📅 13:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a2100800.mp4?token=kPfFU4TQE6RGodpjAw8J2zsOd8NjYdJaI_50ndKn2ezRk9pCmSW0Gvw3jKBEVzgFCU2k0pdZ_Wkeay69cHBYWE1dE2-BmVpgzKnyYq9SnTN_17J5PreN-O-DL2rxBuHbEe_IfqS2jEQrnVolXH72jY8_qWA6WR0-2smELpcz2uczUziLRS3Q6zJgeAVuyKBxFSmXXUkBKN6KMxPjhgffAwzL7KRiO8OOv7bojEg9BaqtuWNFU4X2Iy79Y4WlrjOY63k6htCkPAMktxwQwiXPW-5D8evCBAGuxNqeiMHy9BG589zOwfVQ5jGnDTmH-hjs2lyJX2I7HpHtcz66iC_sWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a2100800.mp4?token=kPfFU4TQE6RGodpjAw8J2zsOd8NjYdJaI_50ndKn2ezRk9pCmSW0Gvw3jKBEVzgFCU2k0pdZ_Wkeay69cHBYWE1dE2-BmVpgzKnyYq9SnTN_17J5PreN-O-DL2rxBuHbEe_IfqS2jEQrnVolXH72jY8_qWA6WR0-2smELpcz2uczUziLRS3Q6zJgeAVuyKBxFSmXXUkBKN6KMxPjhgffAwzL7KRiO8OOv7bojEg9BaqtuWNFU4X2Iy79Y4WlrjOY63k6htCkPAMktxwQwiXPW-5D8evCBAGuxNqeiMHy9BG589zOwfVQ5jGnDTmH-hjs2lyJX2I7HpHtcz66iC_sWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود ناشی از انفجار در فاصله بسیار نزدیک از تخت جمشید.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18167" target="_blank">📅 13:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش انفجار در‌ اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18166" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وای‌نت: نتانیاهو شنبه شب به واشینگتن سفر و روز سه‌شنبه در مراسم خاکسپاری لیندزی گراهام، شرکت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18165" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۳ انفجار اصفهان سمت حکیم نظامی (ممکنه مهمات هم باشه )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18164" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚠️
دوستان لطفا از ارسال پیغام صدای جنگنده دیگه خود داری‌کنید چون بسیار ‌زیاده و دایرکت رو هنگ میکنه همچنین تمام پیغام های ارسالی رو فقط در یک مسیج ارسال کنید ، تا من بهتر بتونم خدمت رسانی‌کنم ، ممنون</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18163" target="_blank">📅 11:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در حملات آمریکایی در شهر بندری چابهار در جنوب شرقی ایران. طبق گزارش‌ها، دو اسکله دریایی و برج کنترل ترافیک دریایی در بندر، به همراه زیرساخت‌های دیگر مرتبط با فعالیت‌های دریایی، مورد حمله قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18162" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18161" target="_blank">📅 11:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرمانده سنتکام: ایران در یک هفته گذشته به هفت کشتی تجاری حمله کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18160" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه‌های اسرائیلی: نتانیاهو شنبه به واشنگتن می‌رسد تا در مراسم خاکسپاری سناتور لیندسی گراهام شرکت کند.
وب‌سایت "یدیعوت آحارونوت": زمان دقیق ملاقات نتانیاهو و ترامپ هنوز مشخص نشده است، اما انتظار می‌رود که آن‌ها اوایل هفته آینده با یکدیگر دیدار کنند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18159" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بلومبرگ درباره دبیرکل سازمان دریایی بین‌المللی: تنگه هرمز همچنان برای کشتی‌های تجاری بسیار خطرناک است.
بلومبرگ گزارش داد: ۶۰۰۰ دریانورد همچنان در تنگه هرمز گرفتار شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18158" target="_blank">📅 11:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیویورک‌تایمز : وزارت خزانه‌داری ایالات متحده اعلام کرد تلاش‌های خود را برای مختل کردن شبکه غیرقانونی کشتی‌رانی و دور زدن تحریم‌ها که تحت مدیریت محمدحسین شمخانی فعالیت می‌کند، تشدید کرده است. محمدحسین شمخانی، فرزند علی شمخانی، مشاور کشته‌شده رهبر پیشین جمهوری اسلامی، است.
همچنین ریچارد برمن، قاضی پرونده، رضا ظراب تاجر ایرانی‌تبار را به مدت زمانی که پیش‌تر در بازداشت گذرانده بود محکوم کرد و هیچ حبس تازه‌ای برای او در نظر نگرفت. ضراب از سال ۲۰۱۸ از بازداشت خارج شده بود، اما زیر نظر مقام‌های فدرال با نامی‌ جدید به عنوان شاهد زندگی می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18157" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4668458d0.mp4?token=HfHU0lOBFYPSaAgqCHWkBAEU2o8NF56-biCWnoGKBhCOObraZZUXCrn5BNSujeJxEqw3rVBtatOErwdJqyi6Ev2bQ7njJY5hUJ_jzZ9M_TeWI-cvjmPhd7wJc9ZkjmJNyr1LoweqOChDE6PArjfuJhCBxw779LIWZRbWGhqENvTbed21mnoJdZ1NR5DC3GTXUJ3mAuqmXt4aNn3a3q2lI75m6le_E2l_NezoiwVJ-DlgpvoU_uluk6N1F8zKdakLuWMiQdZJHU2iyMlJogbeIRUZ_KjTQxC2ElLY7eXUCVa6-F_epchmBMhucF8-dzl6d7MJDteeRmoNXGcEzQGiFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4668458d0.mp4?token=HfHU0lOBFYPSaAgqCHWkBAEU2o8NF56-biCWnoGKBhCOObraZZUXCrn5BNSujeJxEqw3rVBtatOErwdJqyi6Ev2bQ7njJY5hUJ_jzZ9M_TeWI-cvjmPhd7wJc9ZkjmJNyr1LoweqOChDE6PArjfuJhCBxw779LIWZRbWGhqENvTbed21mnoJdZ1NR5DC3GTXUJ3mAuqmXt4aNn3a3q2lI75m6le_E2l_NezoiwVJ-DlgpvoU_uluk6N1F8zKdakLuWMiQdZJHU2iyMlJogbeIRUZ_KjTQxC2ElLY7eXUCVa6-F_epchmBMhucF8-dzl6d7MJDteeRmoNXGcEzQGiFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمای نزدیک از برخورد شاهد ۱۳۶ ایران به سوله امریکایی ها در کویت
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18156" target="_blank">📅 11:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کپلر: ۹ فروند از ۱۱ کشتی‌ای که روز سه‌شنبه از تنگه هرمز عبور کردند، از مسیر ایران حرکت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18155" target="_blank">📅 10:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش اسرائیل: دادگاه نظامی، یک سرباز اسرائیلی را به دلیل ارتباط با یک جاسوس ایرانی، به ۵ سال حبس محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18154" target="_blank">📅 10:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ارتش ایران: در حملات آمریکایی به یک پایگاه نظامی در شهر بمپور، واقع در استان سیستان و بلوچستان، صبح امروز، ۷ تن از نیروهای ما کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18153" target="_blank">📅 10:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Tether = 186000 T
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18152" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یاشار جان سلام آسایشگاه سربازان ایرانشهر، به خاطر اینکه دوست صمیمیم سربازش بوده ازش پرسیدم الان، میگه که لانچر رو دقیقا کنار آسایشگاه جانمابیش کردن، با شلیک لانچر گویا نقطه یابی شده و بعدم خود لانچر رو زدن لانچره میترکه که انفجارش آسایشگاهو زده اینا توی آدمای…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18150" target="_blank">📅 10:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA R</strong></div>
<div class="tg-text">یاشار جان سلام
آسایشگاه سربازان ایرانشهر، به خاطر اینکه دوست صمیمیم سربازش بوده ازش پرسیدم الان، میگه که لانچر رو دقیقا کنار آسایشگاه جانمابیش کردن، با شلیک لانچر گویا نقطه یابی شده و بعدم خود لانچر رو زدن
لانچره میترکه که انفجارش آسایشگاهو زده
اینا توی آدمای بیگناه عادت دارن مهمات و لانچر جاساز کنن تا بعدش بگن وای وای مردم بیگناه یا سرباز وظیفه آسیب دیده
😞
😞
😞
😞</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18149" target="_blank">📅 10:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e10469190.mp4?token=mNism79pSVAHD-9N8AFRfjV8LexmKXDiHdm521Y7el72pixWBeJKcvnXCwFtTFOwxPO-j0xQjqv4KrcSQ9VWG9Ya8thUqR0ONv9kGR6l0SpoKUFd8bp1FG7Xex1lTwheAEe36rjGGcck_RVusHRuXvJmazsAdJVQC7zXF-QD06LAsbdZoJTiFPHpNkCGmHBrkVLeMqo20r_na_LurLp3ILYtpYX6RF22J961AmF01F39QefaGN0TpKA794lh1n1fPCWh-MO5QSu4CFd8Bamz8SSrSezHZAI0LFpyU_dOlkH0Ns4W7SOLAEbkoUc6prXQkd0Yb5Uic5X6T7Cnury4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e10469190.mp4?token=mNism79pSVAHD-9N8AFRfjV8LexmKXDiHdm521Y7el72pixWBeJKcvnXCwFtTFOwxPO-j0xQjqv4KrcSQ9VWG9Ya8thUqR0ONv9kGR6l0SpoKUFd8bp1FG7Xex1lTwheAEe36rjGGcck_RVusHRuXvJmazsAdJVQC7zXF-QD06LAsbdZoJTiFPHpNkCGmHBrkVLeMqo20r_na_LurLp3ILYtpYX6RF22J961AmF01F39QefaGN0TpKA794lh1n1fPCWh-MO5QSu4CFd8Bamz8SSrSezHZAI0LFpyU_dOlkH0Ns4W7SOLAEbkoUc6prXQkd0Yb5Uic5X6T7Cnury4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دیگری از حمله هوایی آمریکا به اسکله شهید کلانتری چابهار و پایگاه امام علی سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18147" target="_blank">📅 10:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱.۱۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18146" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4cb2010d.mp4?token=K06GyZyTkjMZpj_egzRJVOqzSQoKVgtYWjGW1i71IKsn-mNo_YEkEF4ED-OFTtt2PrYTt5daDF-rJF8Dkc1qdQuSgjjSsDyEk9ABRIqSVjvCdRxDPW3PT1Hu4F30LakLOY-wwzyeQQKavF0x8Uw0IiGFAH9CXZDgqyt9L__-pW_RIyfGJF03fcasRpaNbdQ6Z7YRTo-mql2qIXfenjYihaMMCxJZJXCYdSY8ESY0HORqyz3BgwmTQda058r_hXkQwR-3IPGtGTZVq8jcbkRxaaKuZgEyTdq5Hzk2LYqhFHnXjIOx7dp-sIrjOTcc7uzhkKr9pGn0fIAGKg_kCeFRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4cb2010d.mp4?token=K06GyZyTkjMZpj_egzRJVOqzSQoKVgtYWjGW1i71IKsn-mNo_YEkEF4ED-OFTtt2PrYTt5daDF-rJF8Dkc1qdQuSgjjSsDyEk9ABRIqSVjvCdRxDPW3PT1Hu4F30LakLOY-wwzyeQQKavF0x8Uw0IiGFAH9CXZDgqyt9L__-pW_RIyfGJF03fcasRpaNbdQ6Z7YRTo-mql2qIXfenjYihaMMCxJZJXCYdSY8ESY0HORqyz3BgwmTQda058r_hXkQwR-3IPGtGTZVq8jcbkRxaaKuZgEyTdq5Hzk2LYqhFHnXjIOx7dp-sIrjOTcc7uzhkKr9pGn0fIAGKg_kCeFRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا (۵:۳۰ صبح ۱۵ ژوئیه به وقت تهران) دور دیگری از حملات علیه ایران را تکمیل کرد و ده‌ها هدف نظامی در نزدیکی تنگه هرمز و مناطق ساحلی ایران را هدف قرار داد. جنگنده‌ها، پهپادها و ناوهای آمریکایی در جریان این موج هفت‌ساعته با استفاده از مهمات دقیق، سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری و خدمه غیرنظامی بیش از پیش تضعیف شود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18145" target="_blank">📅 10:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGlcABE-AUSxbPraW5iCVgZ7KQ_SNxkW5IRsHMX-rOX-5XFK5dSzi_0Elw2QeJXbcXjdTckgvENjc4wPmIIhlQRbuDQjLG8f9n3zqJBDVLG7PXrpDELXSpWmHlowmFRTaiW6pe1E80Q2clVqyqMYgt_GU2F9cUGmWtnYgv0JvIhyfbsInh0YT9rPSOOYrL_2rlwvmS26BTQCKX09e2YG1JKvhpjg5oFshews7e7pYA7NmULf5GzMOQZaP40pIXZukvL_2A-Nvkr0a1DSqNUnxulOEsEzu0-VIEn_RhtGvBiQtSt4jN102mM1U6rI5PI7PjFNytlh-6Rv8cnFOcz1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پیش چابهار کنار برج مراقبت رو دوبار زد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18144" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
