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
<img src="https://cdn4.telesco.pe/file/fFHDsim7IQ1Wv5vBTmYliRm9m_J3JzdAU5xLUXm188GRSI0-3jofTWgkXwZDo2_z37tSaOwAml99JkQg6N7H55OBpun9cv4blvJ1incEem8scJqZirLUTH1Gyyyeds338587N2UAW1U7cuyu9jLKapndubCQB2Eaf62eppcJhMWJW7L9Rnh-Nn38oHr9hCXOcoDxgW6D2HVODYSwYUfrw0OOuhuj03iXtN3g3XufP2Yh2DtZOIiHTtRPyI7lnmCJuqftNu9UzuwqD7gtnv-yzjiBX2iKjz8RCLYMAOsk4UwlWFfI4C9UwCfHOImFAPA6oGeeooRTFtRtvbz_eZncDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 124K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 11:19:51</div>
<hr>

<div class="tg-post" id="msg-70075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipuGYC4eVJTEdd-Mr4b9hCG7hOJACUJF1RvOGYC46g0mQqWVr84ddiD9meFH3tW8asOPR5L-6Iz5MMycg7aE-aKLvYwttZ3G09-Iv3lUwv-Obs3iDOggW59-cTH0GfSv4h-cu9jswbS0aRGquuKqf4dhRUh0WDNB-0N98RLr6Kgz0GZWdXYZTupUoha0m0RRE5Wu-hwHgmMlRZXyfdeWS-qnd09dU_-NdxLo_j4Vbx6ShVliFiuWumjQePgIY6q6XH__PlVjfkpkzJ_OpIqot0aQrESKkOhrwDWXjE12BYKiC3twg8ZxfKmtZaRAGQhqSZ70qo9_94BI6XwVBr45-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
اکسیوس:دونالد ترامپ، رئیس‌جمهور آمریکا، در آستانه انتخابات ۲۷ اکتبر اسرائیل، بارها از اعلام حمایت صریح از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خودداری کرده است؛ این در حالی است که ائتلاف نتانیاهو در نظرسنجی‌ها از جناح مخالف عقب‌تر است و تنش‌ها میان این دو رهبر رو به افزایش است.
پیش‌بینی می‌شود ائتلاف نتانیاهو حدود ۴۹ تا ۵۳ کرسی به دست آورد که بسیار کمتر از ۶۱ کرسیِ مورد نیاز برای کسب اکثریت است، حال آنکه مجموع کرسی‌های احزاب مخالف بین ۶۷ تا ۷۰ کرسی برآورد می‌شود. همچنین در اکثر نظرسنجی‌ها، گادی آیزنکوت، رئیس پیشین ستاد کل ارتش اسرائیل، از نظر میزان محبوبیت از نتانیاهو پیشی گرفته است.
اختلاف‌نظر میان ترامپ و نتانیاهو بر سر مسائلی همچون ایران، غزه و لبنان افزایش یافته است. ترامپ از رهبر اسرائیل دل‌چرکین شده و در محافل خصوصی او را «بزرگ‌ترین دشمن خودش» توصیف کرده است.
آخرین مورد اختلاف آن‌ها مربوط به مخالفت علنی نتانیاهو با طرح ترامپ برای غزه و خلع سلاح حماس بود؛ هرچند نتانیاهو متعاقباً پذیرفت که به این طرح فرصتی بدهد و از شدت حملات اسرائیل بکاهد.
در همین حال، رقبای نتانیاهو از جمله آیزنکوت، نفتالی بنت و یائیر لاپید، از طریق کانال‌های غیررسمی پیام‌هایی به اطرافیان ترامپ ارسال کرده و از او خواسته‌اند که در انتخابات بی‌طرف بماند. ترامپ در هفته‌های اخیر چهار بار با این پرسش مواجه شده که آیا از نتانیاهو حمایت می‌کند یا خیر، اما هر بار از اعلام چنین حمایتی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/news_hut/70075" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/news_hut/70074" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6JWCwOW8hS4kWUpl_xJvmaXTtdB8foG690s1baX7vazKdKL2qE3fI9yiiiWMT-uunhs1CAyBzoTLrdmoYLD8QvwJS4gEqTwNDQrkiiWwRT-wTSzXkHKd1ROkrTrPyX1_3p8i8Zup4UHWKs7qAOzn-vebS1XthTTgXKtSw2xK2XDGcUQmL0ZfhoNDNMms1Ya-bot4H4AqMD-T2GZGBXz9ekInq_9vZeGDkqNezPeAQOj0odsSFofUlP-kvzYh9WFrgnJGK6X_qpHXWLOL1vfHF68vz9equ0zKXOmaMku3aSlyGmuilag-qJVzTtIF6-0Y8JbNWZXOo3hGN7LWJBUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/news_hut/70073" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70072">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=VRZvoM8zvfFiveSCKB0bhFJRjEI2um-RHOwsnIueWDZV4MzBVJyMuqc0SlJ4JC3IQvZ380u-Aq0vTdkj8NuTs-IiowcWBfeiz0Ac06jF7PiJzUNPI2ziy2Y701TPy7uqbdXnNiHHcCqWwnmLQ7sBEatmBr7WBl4Ex40OliKkb13ajRf07ARWRl6VeFWOA-UqaaS4cVZCKRlBT7bLZNqJvSq2EIZuyXYLNslQ1hrrTveWv5SFjSdmiXzQ4NV8_LR3guE-xf3OxUnO2tyi7SzHrHg6VOgpqEGRKZOQd5yiX8cwb_9lu4Om8zBuIaJ69cPjVgTKlTGP0Uy59fKvlzXnjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=VRZvoM8zvfFiveSCKB0bhFJRjEI2um-RHOwsnIueWDZV4MzBVJyMuqc0SlJ4JC3IQvZ380u-Aq0vTdkj8NuTs-IiowcWBfeiz0Ac06jF7PiJzUNPI2ziy2Y701TPy7uqbdXnNiHHcCqWwnmLQ7sBEatmBr7WBl4Ex40OliKkb13ajRf07ARWRl6VeFWOA-UqaaS4cVZCKRlBT7bLZNqJvSq2EIZuyXYLNslQ1hrrTveWv5SFjSdmiXzQ4NV8_LR3guE-xf3OxUnO2tyi7SzHrHg6VOgpqEGRKZOQd5yiX8cwb_9lu4Om8zBuIaJ69cPjVgTKlTGP0Uy59fKvlzXnjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو محل دفن خامنه‌ای یکی اومد به ترامپ فحش بده، حراست زد دهنشو بست:
@News_Hut</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/news_hut/70072" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70071">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=PjgPyx9bR1jswasWIhmKY_mBEHTzAlRrhgP4j-v-kKUWjWgAr-JW9UtUApDW3dUBdaQlIw8V4jZXCa-XHldYfXep0iflObmYMNdOCpHr39rgJrtFAp1yvXWC6HETt7rzq19rZzLMh3n4k38hNfdJS8t9iJwTgtYyKbQzABATuP5993z21WFQj-u9Wrj1DzIOWxzd2OJusBJJW9_QCot9HRlSAjDlf8dg3jlyDxs7zr0Ymrem1D0P6CSAqX8K9q4HMqLIWODFXi0YpkEo3QAeKC09kgraRl0OTCJdaifuSmEERrL49ytHa68kLWTvFk2ArTyVzTWdTtRVFPLBxdVpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=PjgPyx9bR1jswasWIhmKY_mBEHTzAlRrhgP4j-v-kKUWjWgAr-JW9UtUApDW3dUBdaQlIw8V4jZXCa-XHldYfXep0iflObmYMNdOCpHr39rgJrtFAp1yvXWC6HETt7rzq19rZzLMh3n4k38hNfdJS8t9iJwTgtYyKbQzABATuP5993z21WFQj-u9Wrj1DzIOWxzd2OJusBJJW9_QCot9HRlSAjDlf8dg3jlyDxs7zr0Ymrem1D0P6CSAqX8K9q4HMqLIWODFXi0YpkEo3QAeKC09kgraRl0OTCJdaifuSmEERrL49ytHa68kLWTvFk2ArTyVzTWdTtRVFPLBxdVpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهارتا دختر یه سفره سه روزه رفتن شمال، حالا چقدر خرج کرده باشن خوبه؟
۵۸ میلیون تومن ناقابل
@News_Hut</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/news_hut/70071" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70070">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💢
🎙
صحبتای اشکان خطیبی درباره بازداشتش :
در حال حاضر پناهنده سیاسی هستم، از ۲ سالگی کتاب خوندن رو شروع کردم و وقتی ۱۷ سالم بود وارد دانشگاه شدم و کوچکترین دانشجوی دانشگاه بودم
من رو از جلوی در خونه گرفتن و بازجویی خیلی خشنی داشتم؛ ضرب‌وشتم، تهدید و فحش‌های رکیک و جنسی به خودم و خانوادم
۷ اتهام مختلف هم بهم تفهیم کردن؛ از توهین به ائمه و پیامبر و رهبری گرفته تا دعوت به اغتشاش، برهم زدن امنیت ملی و ضدانقلاب بودن
😳
حداقل ۵ بار دیگه توسط ارگان‌های مختلف بازجویی شدم؛ حتی یه کارشناس مسائل تروریستی خاورمیانه در وزارت ارشاد ازم بازجویی کرد
به‌خاطر استوری و فعالیت تو فضای مجازی این کارا رو با من کردن، ولی میدونستم دارم چیکار می‌کنم چون دیگه تحمل نداشتم.
تنها چیزی که خوشحالم می‌کنه اینه که بدونم یه قدم به آزادی نزدیک‌تر شدیم
@News_Hut</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/news_hut/70070" target="_blank">📅 09:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70069">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
این خونه فوق لاکچری که تو سعادت آباد میبینید ویلا نیست!
اپارتمانه که شبیه ویلا ساختن
واقعا اگه اینایی ک این خونه هارو میخرن زندگی میکنن
پس ما چیکار میکنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/news_hut/70069" target="_blank">📅 09:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94046ec789.mp4?token=jcJPQ2Hhwh4jySM4u7afMxjZ9bwuz8ZMqrkyqnzHtDJGtA6Xz7TXDfR-RsqnaqV2DDoB4j4TqlzDZllUxulX6tdCPOb-EYuSCMbir2zWzIFmx3SEeRkPfvwxH_X27Gnxdnvb-9OqQUGgdPkKFnG2M6176H4E6jepTz0uvtENmUMnptYRn7JRNdwUyUn0pRIamQcWwQ5VK3PU-tqe409HzzvJ7Jtnd6b3pNRFI9Ve1DEWjkSVZfmpAziGwlQSZ1I7WRE10onyfKF1USebtJQVczcKwC2rzzbaJOZB3YqCR71tYnL-NfpPgn2cUYNJWozSNx0i9n0Zj-3UkDJP3U-N2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94046ec789.mp4?token=jcJPQ2Hhwh4jySM4u7afMxjZ9bwuz8ZMqrkyqnzHtDJGtA6Xz7TXDfR-RsqnaqV2DDoB4j4TqlzDZllUxulX6tdCPOb-EYuSCMbir2zWzIFmx3SEeRkPfvwxH_X27Gnxdnvb-9OqQUGgdPkKFnG2M6176H4E6jepTz0uvtENmUMnptYRn7JRNdwUyUn0pRIamQcWwQ5VK3PU-tqe409HzzvJ7Jtnd6b3pNRFI9Ve1DEWjkSVZfmpAziGwlQSZ1I7WRE10onyfKF1USebtJQVczcKwC2rzzbaJOZB3YqCR71tYnL-NfpPgn2cUYNJWozSNx0i9n0Zj-3UkDJP3U-N2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
هزینه‌ها چند برابر شده، مسیر واردات طولانی‌تر و درآمدهای ما کمتر شده است.
نفت را نمی‌توانیم مثل گذشته بفروشیم و با تخریب برخی کارخانه‌ها، درآمد مالیاتی هم کاهش یافته؛
با این حال مجبوریم برای ادامه فعالیت اقتصادی به آن‌ها کمک مالی کنیم.
مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/70068" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70067" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=rGToClABKA8Jydf00Q9cbIjoCKQ61BNwPwriXqtVnOLSF3vEQHUmuw_8XuS68ngv5pdukWdES9vTJ6HvoNBPxCTlGbqkv4duuEY8Xn3JHwEga_D4tEJJ6P88wVWvWl8gPCSN1J6Jc_oNiDUVxCT_OTZPW-v2Gr4Zl0a54rfJnp5h2UbhObeqMILdrKigDLg9ItUvGs8SBzQ5UMaa1rjUoArGwdaG_8LlAywIOsazRc6ofZhm5lIo_lNzJdyfwMf-BjSxA5yXLGHUsszC4Y13g2NbbZMVzKwiwO1itxo0UXOa1be36BXHnZS5z9jNCy5ca9n6UihqvFODnNY22yvhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=rGToClABKA8Jydf00Q9cbIjoCKQ61BNwPwriXqtVnOLSF3vEQHUmuw_8XuS68ngv5pdukWdES9vTJ6HvoNBPxCTlGbqkv4duuEY8Xn3JHwEga_D4tEJJ6P88wVWvWl8gPCSN1J6Jc_oNiDUVxCT_OTZPW-v2Gr4Zl0a54rfJnp5h2UbhObeqMILdrKigDLg9ItUvGs8SBzQ5UMaa1rjUoArGwdaG_8LlAywIOsazRc6ofZhm5lIo_lNzJdyfwMf-BjSxA5yXLGHUsszC4Y13g2NbbZMVzKwiwO1itxo0UXOa1be36BXHnZS5z9jNCy5ca9n6UihqvFODnNY22yvhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a23
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/70066" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=bHsAGjOiVsPNjIrAkOsVwPiteRK506elhouGJiRAX8OKcFIibZhtRBPab0-GzsDttKmmmV9bYq-axmIurHrv7wcEopMmwFUBQu9TE-B_BXUiD_sO0lCk01kpVL5XpEp6YFEPknOeIRe_PiFItzTBz0R2zvb17YY53laWqrhNc8VlhOPi4tWJaBC-LiMcpeZWF5cW6LFgxloABc8XldpmCs6uaXQzA6KDIUTfg1WR9xQjp4YOSdjrnJmsdAcXE5eyX3PUl8ewAHUFSvFc4oOzJQSGwSRS8f4aI2H2mg236-Tope4Ovw2sx84jQ6GPbg-JANMzJNE67U6F9Ms6_TpEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=bHsAGjOiVsPNjIrAkOsVwPiteRK506elhouGJiRAX8OKcFIibZhtRBPab0-GzsDttKmmmV9bYq-axmIurHrv7wcEopMmwFUBQu9TE-B_BXUiD_sO0lCk01kpVL5XpEp6YFEPknOeIRe_PiFItzTBz0R2zvb17YY53laWqrhNc8VlhOPi4tWJaBC-LiMcpeZWF5cW6LFgxloABc8XldpmCs6uaXQzA6KDIUTfg1WR9xQjp4YOSdjrnJmsdAcXE5eyX3PUl8ewAHUFSvFc4oOzJQSGwSRS8f4aI2H2mg236-Tope4Ovw2sx84jQ6GPbg-JANMzJNE67U6F9Ms6_TpEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
ترامپ:
ما قادریم تمام آنجا را نابود کنیم؛ اما نمی‌خواهیم چنین کاری انجام دهیم.
ما تحریم‌های اقتصادی بی‌سابقه‌ای را علیه آن‌ها اعمال کرده‌ایم.
اگر آن‌ها دست به حمله بزنند، ما صد برابر شدیدتر پاسخ خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70065" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=osbWySUO5Gd8poIFEtpVxmZ9Qtcapd8Ntnjy5JDK698UmmLBSYN_LP_wddvnXjhOJEESKx6ToLl_9hdD9Z4hz3cABDuwHw96Rlmdnb8ZzDAXLqkZ11oU-AEXWJzG4Mp7MgScxZPkwsWoMot2OQ0Uk5j8-zkqCsSaDZB5eeKisWpI9jU9SFnqhSd9xRT0XjLmOF1yWdGKowdKyPGAp90_w3dmqTViKt2_fURkH8W5lW7o-SUr4hmgi8i5DA3P0b3d6VQAuJHKyerpoYEKsC-9FjA9jUDEm0bRAfAQ-fG4ZJpIk3R56A8TCu1CI947HLhCvWC491Mor4pcnmOl1NYgmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=osbWySUO5Gd8poIFEtpVxmZ9Qtcapd8Ntnjy5JDK698UmmLBSYN_LP_wddvnXjhOJEESKx6ToLl_9hdD9Z4hz3cABDuwHw96Rlmdnb8ZzDAXLqkZ11oU-AEXWJzG4Mp7MgScxZPkwsWoMot2OQ0Uk5j8-zkqCsSaDZB5eeKisWpI9jU9SFnqhSd9xRT0XjLmOF1yWdGKowdKyPGAp90_w3dmqTViKt2_fURkH8W5lW7o-SUr4hmgi8i5DA3P0b3d6VQAuJHKyerpoYEKsC-9FjA9jUDEm0bRAfAQ-fG4ZJpIk3R56A8TCu1CI947HLhCvWC491Mor4pcnmOl1NYgmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:ایران تنها کشوریه که کسی نمیخواد رئیس جمهورش باشه.
«آن‌ها هیچ رهبری‌ای ندارند.
رهبری‌شان از بین رفته است؛ رده اولشان رفته، رده دومشان رفته و نیمی از رده سومشان هم از دست رفته است.
این یکی از مشکلات من است؛ کسی نیست که با او مذاکره کنم. این یک مشکل است.
من گفتم: "آیا مطمئنید حال این آدم خوب است؟"
اینجا تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70064" target="_blank">📅 00:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55686a2794.mp4?token=oLd2d78_DaaysiOzQtavJjbiB8oq7ls319oW0vFVnwQCaqeDHu7c_3swuuJ9mVVBwFJ46q13f1gry-Lhlg5DFe8eIQr3g_Q8R5b9XsophO6rx1k6qp0akNn_0wZEkIHjjUGRvw5im7ncB9dLOlOAvx-eAi9fkYh5y3re17zBaHRD_HpPSxdlh5DgoUJrKixQGEvDMhSChluxLB4PUz2KA4PhKCyxXd_mg9cHLv_XgKflpuSp-RdfrRkh2vtncFIaX9mB9CJDINr15CRh78KBPhsu0hMIy8l6X9jABYv7Xy0096vHS6DOL_yJWbqdJfarZVfKNrcyApAQ483cPiH4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55686a2794.mp4?token=oLd2d78_DaaysiOzQtavJjbiB8oq7ls319oW0vFVnwQCaqeDHu7c_3swuuJ9mVVBwFJ46q13f1gry-Lhlg5DFe8eIQr3g_Q8R5b9XsophO6rx1k6qp0akNn_0wZEkIHjjUGRvw5im7ncB9dLOlOAvx-eAi9fkYh5y3re17zBaHRD_HpPSxdlh5DgoUJrKixQGEvDMhSChluxLB4PUz2KA4PhKCyxXd_mg9cHLv_XgKflpuSp-RdfrRkh2vtncFIaX9mB9CJDINr15CRh78KBPhsu0hMIy8l6X9jABYv7Xy0096vHS6DOL_yJWbqdJfarZVfKNrcyApAQ483cPiH4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«آن‌ها ۲۱۲ هواپیمای بسیار خوب داشتند—برخی را به برکت اوباما، باراک حسین اوباما، به زیبایی از ایالات متحده خریده بودند.
از او شنیده‌اید؟ باراک حسین اوباما. و هر کدام از هواپیماهایشان ساقط شده، از بین رفته.
آن‌ها هیچ رهبری ندارند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70063" target="_blank">📅 00:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=kJfrfw3PS4bARTyP9nPOCEFcFxdzXEtlnHpp9cyPrCzVsrowjQVEwFOfkL1B7sYJh5MUlW3uC7IrApd6z0AbuPUkcQSbgSYfMSo0jQJHjGHKQS39gVWBBD6hENb2v8ojWp8K-iF7eF3kBoBCe1jLlirDipejaY_RTHQkKmyU-jPlwiQcEK-7-RlLAorgTZpRmWboHC3FlGzORLMREEsylxn7DpGPeltMVSZYyiaNJwSAwIZkwL9m08mZKXLLkpIc1HN8lBj6ILDGsadrbAJOC7kr966-t3jBEBiJPJo0Cx2xJHU8B7uvu5aSo8rxULBzMcBilVfS7_dtzYRL0BOCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=kJfrfw3PS4bARTyP9nPOCEFcFxdzXEtlnHpp9cyPrCzVsrowjQVEwFOfkL1B7sYJh5MUlW3uC7IrApd6z0AbuPUkcQSbgSYfMSo0jQJHjGHKQS39gVWBBD6hENb2v8ojWp8K-iF7eF3kBoBCe1jLlirDipejaY_RTHQkKmyU-jPlwiQcEK-7-RlLAorgTZpRmWboHC3FlGzORLMREEsylxn7DpGPeltMVSZYyiaNJwSAwIZkwL9m08mZKXLLkpIc1HN8lBj6ILDGsadrbAJOC7kr966-t3jBEBiJPJo0Cx2xJHU8B7uvu5aSo8rxULBzMcBilVfS7_dtzYRL0BOCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«و ما در مورد جمهوری اسلامی ایران هم داریم به موفقیت‌های بزرگی دست می‌یابیم. هیچ‌کس نمی‌داند چقدر موفق عمل کرده‌ایم؛ آن‌ها نمی‌خواهند این را بنویسند، اما خودشان می‌دانند.
می‌دانید چه کسی می‌داند که ما چقدر خوب پیش می‌رویم؟ خودِ ایران. به این فکر کنید: آن‌ها نیروی دریایی ندارند؛ وضعیت کاملاً یک‌طرفه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70062" target="_blank">📅 00:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=EvkiIeXSXjHr1NrfXBcwpwoTLsZy5lyCVbTVdOkxrJiNmQsDAUWGfOYIvl-C5e0MT9J0XOPzLlBxbnFFrVQAGHABrAa2zisDQE4nwMqIr3cOt6LJLg0W7PoLTUlr0gc8Rl3cwMfg0vcVk6ReIM4I0ZkTMVztgMDM7F5UXkmkZnW4RrsBpWbbuXFav7VgA_ioDu8SWMxgZlPzCmIWyULpLNUNPYo4k-M3gzzCk2bQY4ioNkIccbWjQw6xhFPjfu1lDuE_ohulCcH5JkOAIvQ3qxwE-jMlPLMnRsGlGUdG7opekY5z3dUpOslbr17fXrp2SludNTO3AsLtRNvlNU0TZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=EvkiIeXSXjHr1NrfXBcwpwoTLsZy5lyCVbTVdOkxrJiNmQsDAUWGfOYIvl-C5e0MT9J0XOPzLlBxbnFFrVQAGHABrAa2zisDQE4nwMqIr3cOt6LJLg0W7PoLTUlr0gc8Rl3cwMfg0vcVk6ReIM4I0ZkTMVztgMDM7F5UXkmkZnW4RrsBpWbbuXFav7VgA_ioDu8SWMxgZlPzCmIWyULpLNUNPYo4k-M3gzzCk2bQY4ioNkIccbWjQw6xhFPjfu1lDuE_ohulCcH5JkOAIvQ3qxwE-jMlPLMnRsGlGUdG7opekY5z3dUpOslbr17fXrp2SludNTO3AsLtRNvlNU0TZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«پس فقط این را می‌گویم. اینکه کمی بیشتر برای بنزین خود پول پرداخت کنید، فقط به یاد داشته باشید که این کار را می‌کنید تا یک کشور بسیار شرور نتواند سلاح هسته‌ای داشته باشد، کشوری که واقعاً حامی شماره یک تروریسم دولتی در جهان است. ما نمی‌خواهیم آن‌ها سلاح هسته‌ای داشته باشند.
پس وقتی مجبور شدید کمی بیشتر پرداخت کنید، حتی اگر به چهار دلار برسد، اشکالی ندارد. من هرگز عذرخواهی نخواهم کرد، کار درستی انجام دادم. اگر این نبود، منظورم این است، من در بسیاری از ایالت‌ها قیمت را به زیر دو دلار رسانده بودم، اما کالیفرنیا را نمی‌توان شامل شد چون آن‌ها مدام مالیات وضع می‌کنند و وضع می‌کنند. شما قیمت نفت را پایین می‌آورید و آن‌ها در نهایت بیشتر از آنچه پایین آوردید، از شما مالیات می‌گیرند.
فقط باید به یاد داشته باشید که کاری که ما انجام می‌دهیم، خدمتی بزرگ به جهان است، نه تنها برای خودمان، بلکه برای جهان، و ما واقعاً کار بزرگی انجام می‌دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70061" target="_blank">📅 00:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPGETlgT8GBh6N1j-dNpozO3Ce3xfAU2MsG1l8CikwEqTHYE4zBquTCi1rbyddfoKvqu5zj8ELWJ1neaBc1ilkJ-fsBCXEQK_j9hUnc3jOlryxNoodu50GD236ujp67xH3xGiFIrw7YWb1riBJpeTIVErAjybMF-Zn5-c6uSnh3bAtz5wwbSpU4pbJ039VZ914xGWKmfH77z4UjljigbvOAkeZm3M8yn4z17yy1DArMcmfMqSZ__5Z7RgNc6U21lfeSBMbbBdWA3UHORxXshhRn7VA5hR-TQzb9_lpanadXk6I_sLbdwDyGJxAkN5dID7onmIDWdO8mAYdYsxUzcFhC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPGETlgT8GBh6N1j-dNpozO3Ce3xfAU2MsG1l8CikwEqTHYE4zBquTCi1rbyddfoKvqu5zj8ELWJ1neaBc1ilkJ-fsBCXEQK_j9hUnc3jOlryxNoodu50GD236ujp67xH3xGiFIrw7YWb1riBJpeTIVErAjybMF-Zn5-c6uSnh3bAtz5wwbSpU4pbJ039VZ914xGWKmfH77z4UjljigbvOAkeZm3M8yn4z17yy1DArMcmfMqSZ__5Z7RgNc6U21lfeSBMbbBdWA3UHORxXshhRn7VA5hR-TQzb9_lpanadXk6I_sLbdwDyGJxAkN5dID7onmIDWdO8mAYdYsxUzcFhC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران به‌شدت در حال شکست خوردنه.
به‌زودی اعلام می‌کنم که تنگه هرمز به قلمرو ایالات متحده تبدیل شده.
به افرادم گفتم: «باید یه سفر کوچیک به خاورمیانه داشته باشیم، چون باید جلوی یه فاجعه احتمالی رو بگیریم؛ یه آتش خیلی بزرگ، چیزی که تا حالا مثلش رو ندیدید.»
وقتی مجبور بشید برای بنزین یه مقدار بیشتر پول بدید، من هیچ‌وقت بابتش عذرخواهی نمی‌کنم. من کار درست رو انجام دادم.
یک کشور خیلی شرور نباید سلاح هسته‌ای داشته باشه.
کاری که ما داریم انجام میدیم، خدمت بزرگی به دنیاست؛ نه فقط برای خودمون، بلکه برای کل دنیا.
ما واقعاً داریم کار بزرگی انجام میدیم. محاصره مثل یک دیوار فولادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70060" target="_blank">📅 23:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4g3Dk2SgMpXlmqaNam9xLnKfgwhJXZ99E1SfS5_5pgHWXtxEn0RKpy1_q17oTw1bbt0IjbNjU72rt11g1SKusdM2ijn4s2Ucbqg1bfbUg838JoZ03hTA9Tjj7qnZxQGnyLwfEMBDokEqogJ2wkLBvZ_5GBMiy01c_dgyY-fKjnVxZXvKYO8AN0R9iNNZERkkFGzPa0EKgBGFvuX58reMcGqkjSRsStCwOUxwqgaVXkrEYnWgytTJQ98bIdCkBAYJVdineZt-SGkOMF_06qpbZ8SloyrlyUKRjtC_1DvN4WWpKKxX1-k9twXOyYy5ARLwKlTjDhwQakb1FuSqSlzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70059" target="_blank">📅 23:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d105db041c.mp4?token=XqaVwaPABcSA8DzglPW6zgCxPXbbF9i2_B7kpFBgM3wtR7qP18uFa-PVRRzAFx3ZkXh5yUxEOUD2kuttdw3Iz5UwplKpttYJg2T0bWVNd4TksMNT04tTlezo7RA-m5j09anvpWHkVaN354BLla9ntH8eQ1NGdjddN9XqSUxeRffFZ4CjDqXFeClQGt1PiO5aZOUGmz082aFkDU1VhmiUKA152__jQmXSiIRnUrTvUGe6A6nYVXLwoZzI74UhDfFzUbNM_AtvZUl52sK-XCe6umqYIkOslIzsgePdsR20rbRndV_20jl2unCy08Y4UOlHvdpNIZClZQoTyVdbENVGhJCfFGn5BRDqpnprdq-fhu0qbgyMD8N3fDe3c1RjVhTAUsZiDhdZTlzinnl-AK3-xrkJWdsX_eppbqhv_p0vz8-wxcu0yCLTHm38JQIo27EYXKhnZos0rhDqcy2t-TS4CVCA6aklg3-F43ce3-uBTS8PtOcabFl1S_LVRDa9hdbIQFExoj6YcGJut6d8K68DvCDzRw7SA3cRQHGIzvGHSeADNAT-nHnWfZ_LEC0W3ZLJhiFhEsT988xuO6ShfNGGHtTf3kA0mcHlWuTLhMr5UPjOh3L5jEJvLZZzuySFqXFjOn9BZsh7L4ntLFMSuSfuGy4iEQZAT64vXee26uFWmy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d105db041c.mp4?token=XqaVwaPABcSA8DzglPW6zgCxPXbbF9i2_B7kpFBgM3wtR7qP18uFa-PVRRzAFx3ZkXh5yUxEOUD2kuttdw3Iz5UwplKpttYJg2T0bWVNd4TksMNT04tTlezo7RA-m5j09anvpWHkVaN354BLla9ntH8eQ1NGdjddN9XqSUxeRffFZ4CjDqXFeClQGt1PiO5aZOUGmz082aFkDU1VhmiUKA152__jQmXSiIRnUrTvUGe6A6nYVXLwoZzI74UhDfFzUbNM_AtvZUl52sK-XCe6umqYIkOslIzsgePdsR20rbRndV_20jl2unCy08Y4UOlHvdpNIZClZQoTyVdbENVGhJCfFGn5BRDqpnprdq-fhu0qbgyMD8N3fDe3c1RjVhTAUsZiDhdZTlzinnl-AK3-xrkJWdsX_eppbqhv_p0vz8-wxcu0yCLTHm38JQIo27EYXKhnZos0rhDqcy2t-TS4CVCA6aklg3-F43ce3-uBTS8PtOcabFl1S_LVRDa9hdbIQFExoj6YcGJut6d8K68DvCDzRw7SA3cRQHGIzvGHSeADNAT-nHnWfZ_LEC0W3ZLJhiFhEsT988xuO6ShfNGGHtTf3kA0mcHlWuTLhMr5UPjOh3L5jEJvLZZzuySFqXFjOn9BZsh7L4ntLFMSuSfuGy4iEQZAT64vXee26uFWmy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار
: اعضای خانواده نظامیان درباره شرایط داخل ناو «آبراهام لینکلن» نگران هستند.
🇺🇸
ترامپ
: نه، آنها نگران نیستند. این ناو همین حالا یا خیلی زود حرکت خواهد کرد و یک ناو بسیار مشابه جایگزین آن خواهد شد.
🔴
خبرنگار
: آیا مأموریت این ناو بیش از حد طولانی شده است؟
🇺🇸
ترامپ
: نه. نه. نه. اصلاً به اندازه کافی طولانی نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70058" target="_blank">📅 22:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=Xzei6ruk5RuGgPlVzADIn1VaHKyCi880kdSyQU8PpJ7RY5SF8mBz2-EtMOtheJk4pDHemLls7N73bS7HqjnNyoLA8bo8qtmQokHz94FZ5-2Zdh1-7pSOMbG4WleXRoRZsNuA34AuSTvPIqpvdT6PvRVVOeejtqUkjr4J_-qw6XVXcOdozYa3_0GTfaeIWDU817-JZzoWp-Jnp79Fj1yC6nqEsCKBWpSMRavexMXCBTzc--FATNSy9sTP-m3gPgjLrHWmO0M0kS-Z8pn9kRO5ZaPqCYjHscZ3EIm-R5D8gPy4xRV6mXgi8vRHZGwS_QLodNx3vumTXoi3lNuLaRsl3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=Xzei6ruk5RuGgPlVzADIn1VaHKyCi880kdSyQU8PpJ7RY5SF8mBz2-EtMOtheJk4pDHemLls7N73bS7HqjnNyoLA8bo8qtmQokHz94FZ5-2Zdh1-7pSOMbG4WleXRoRZsNuA34AuSTvPIqpvdT6PvRVVOeejtqUkjr4J_-qw6XVXcOdozYa3_0GTfaeIWDU817-JZzoWp-Jnp79Fj1yC6nqEsCKBWpSMRavexMXCBTzc--FATNSy9sTP-m3gPgjLrHWmO0M0kS-Z8pn9kRO5ZaPqCYjHscZ3EIm-R5D8gPy4xRV6mXgi8vRHZGwS_QLodNx3vumTXoi3lNuLaRsl3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت جنگنده اوکراینی مدل میگ-29، امروز صبح در حین تعقیب یک پهپاد روسی مدل "گران" بر فراز منطقه اودسا، موفق به سرنگون کردن آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70056" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70052">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1XREr13ulZwnSzQokHLSdd7V4q7GQwfu22XEnwlMeZxdKZ9V8rHvYUBbWSZ3ANVHslCdKo1clOQbYGhTVh9Z_5iAr1146L6NjCHG2_0y6y6RdRLouaZyv_1-4GzkREHubvsdUPkJYWu-eYzSBMZGNtd7o8HlZuNaZuCyk_JnOIUHIH7ayFXxIgI3q2h47jEAY9SS30Vp7-EzuUhqWAVNC0_ij7Ny2Exko8m2rrtcRuq3vv3vf85vOnSsNlF3hhfjp8U49ukVjcDacdeZyrbZ-s4p3slRON55TniuDDz_j6O_E0uB4ylsobXYPh5SGzciQL-es60h5Mt32kpBYe5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeHYzGio7frJEq8bV9T5NTnzQJRuiE_zQ3OoRH5bGZW_TmVEvttfA0-X84nyayavOPIBHD-syB0AWi11W1fJrdovN9z5e4YLypgXdpuYmO_4LFe0GTSUK3rvcCsRI6yj1uuZyUlHGdJkL_Y7W_2LNXERLDRKXzZT7bywBxlp-JNHclmKvT_YvQgZ0HoZhBbxP15ijg3jxu4i0OGJ0IrkObFCVy4pjdWsk9n4u8L-3wJuxWTrgJFOGCo6Aghk7E6OMlK_vMlXV1rdBY5TZmMrjU1x3SB8T7c-b-mQSWOCvaLPvwUuJrUe4Oque-xwLaP1gQ7D2Rq9O0oDj8-8Y2d-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD_3r0MAJA_0eTerDpY5StvxvNSA7QoLpXoQEd_r5E0UEUozV3b0J_Kz5Vjn1ndyKAmv4Spf9CY_bIX5PnYKSCzwHLNw4oa8evVGuRFqvh08M47AKn7b9eSGg0traKL22hZm7F-NalTqUtZG9My7cAPgspjitGlO2mILsI31q-pSYl-jnvCvcRxLOW438xBIW1vTTTrD197czeD8ZdhAsD0SkVmres7x4FJC7yBIkFmocj-ZhxjdNkpQeoHEnYdASM9hIg6hIVcCkdukjE6iiLHDVZaaQuFXU8LwlZufisDODf5QJJRilEFnljamPhDLWcA9NQ-vRt7tv8K1KwtXYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=Uyq-pQlAEourFkBJadl7ikJihSiaBWw6jMKlxupXPwDmlqmIDdgf7WlqNoJHk3ZJuEK1jiEZn-1o6ILzICc0O1C66gBvG1O_C6u9z3YGYMozOXW3IFKSXSe7BcmhCoN8nH2oszWZxt-r4hjqDiRFKC4tDO0P1VNzTvkjwN9j4SPUTeRsAaZ2hkGBc3Usfrms0LrJYiQPJZj7j9GmO8BLXQl2j_MhKBXFOEaoE1-AWinuKINldiP3mN90o_kLepXD9tkWfKMiLr8Q0DgU4FfdyQX6uYq27H-tTaUUq-QiwHMJ_kKinF1Nc4dJv5h2kFWvA1X7r__761rGqMiHlqa_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=Uyq-pQlAEourFkBJadl7ikJihSiaBWw6jMKlxupXPwDmlqmIDdgf7WlqNoJHk3ZJuEK1jiEZn-1o6ILzICc0O1C66gBvG1O_C6u9z3YGYMozOXW3IFKSXSe7BcmhCoN8nH2oszWZxt-r4hjqDiRFKC4tDO0P1VNzTvkjwN9j4SPUTeRsAaZ2hkGBc3Usfrms0LrJYiQPJZj7j9GmO8BLXQl2j_MhKBXFOEaoE1-AWinuKINldiP3mN90o_kLepXD9tkWfKMiLr8Q0DgU4FfdyQX6uYq27H-tTaUUq-QiwHMJ_kKinF1Nc4dJv5h2kFWvA1X7r__761rGqMiHlqa_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
〰️
صفحه اسرائیل به فارسی در پلتفرم ایکس:دو مهمون خوشگل از ایران
🦌
امروز صبح جنگلبان پارک ملی برعام در منطقه گالیل شمال اسرائیل با یک منظره زیبا روبرو شد. دو گوزن زرد ایرانی که احتمالا از اندوخته‌گاه طبیعی که در مجاورت پارک است به آنجا آمده بودند.
گوزن زرد ایرانی زیرگونه‌ای از گوزن زرد است که در آستانه انقراض قرار داشت. اما با تمهیدات دولت ایران در دوران پادشاهی پهلوی، موفق به حفظ این نسل شدند.
سازمان طبعیت و پارک‌های اسرائیل در سال‌های پیش از انقلاب وارد گفتگوهایی با دولت شاهنشاهی شد تا چند راس از آن‌ها را برای حفاظت به اسرائیل بیاورند. به موازات آن، اسرائیل دو راس گوزن نر از آلمان گرفت که پیشتر از ایران برای حفاظت به آنجا انتقال یافته بودند.
لحظاتی پیش از آمدن خمینی و در آخرین پرواز تهران - تل‌آویو ۴ راس ماده گوزن زرد آنطور که دولت شاهنشاهی وعده داده بود، با کمک تیمسار منوچهر خسروداد به اسرائیل انتقال داده شدند. اکنون چند گله از گوزن زرد ایرانی در کوه کارمل در اسرائیل زندگی می‌کنند و تحت حفاظت قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70052" target="_blank">📅 20:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70051">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIA_c5OElkbFwV0obd45Ac-lmEmyXNpPI3TomxTy8QLSxWJNWcq7betFHIZzkCMxLz-1P0B1g0irpyLzVgR3g0P5GE6qR_CZ0qVP-PiGtxd6Fd5qMf4K9Pc4Jm73YgLpO7IatYRLRu5RwlwGu1xzluIitBBJB1de7Pw0wytz64V_m7708_O1OcMCn27OzqETsJMOXIS753EZzjjzIPSXaZH2CRZhhw0JaRL3iCspgeUApPL_6r-SvGVWJ-o-1PHVVTEDn-FAQNg3BsuJbLW0D-6nV2Bc6Tw5ZaDwpzpr6UtFq4t7DeB1ADM9eR02nmV6QXEgSKPyrKMMLnEXLKCROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی
CENTCOM: اقدامات آمریکا علیه کشتی‌های مرتبط با بنادر ایران
:
🔴
فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نیروهای آمریکایی از زمان تشدید محاصره بنادر ایران:
🔹
۶۲ کشتی تجاری
را تغییر مسیر داده‌اند؛
🔹
۳ کشتی
را از کار انداخته‌اند؛
🔹
و
۲ کشتی
را برای اطمینان از رعایت مقررات، بازرسی و توقیف موقت کرده‌اند.
به گفته CENTCOM، این اقدامات در چارچوب اجرای محاصره بنادر ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70051" target="_blank">📅 20:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=j9TVwuRXBtNOBVxq3YY87Ul-X7o4zwUdT-STWAF3Wp5mPioPc7kCzwRuoSZCug-gP7jCPArKYiwGSpj66RGzjqdXpQTtVG8_tqN1KET_CFrzzFGfV8DYIFmULli8wjay6QrXbBPJ7yOR2woTSKSLF6yb88jpuK717d_QFJbTXXMgNjsLkL4KG_9x5hiPMcuC3Bui-0dqtLpHaO_jtrd9XPaWArBpeFF3mauUS6aG1YMWr0ZcOmhx7VBFarHjbDyXxrThxSJgJRoUHisTtWOzfgCo88BeEU7mDOEwktDx1EKuLCfr84dIGUVBmbfu1VHGK7_y-Gg2jQthXu7RnNI3SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=j9TVwuRXBtNOBVxq3YY87Ul-X7o4zwUdT-STWAF3Wp5mPioPc7kCzwRuoSZCug-gP7jCPArKYiwGSpj66RGzjqdXpQTtVG8_tqN1KET_CFrzzFGfV8DYIFmULli8wjay6QrXbBPJ7yOR2woTSKSLF6yb88jpuK717d_QFJbTXXMgNjsLkL4KG_9x5hiPMcuC3Bui-0dqtLpHaO_jtrd9XPaWArBpeFF3mauUS6aG1YMWr0ZcOmhx7VBFarHjbDyXxrThxSJgJRoUHisTtWOzfgCo88BeEU7mDOEwktDx1EKuLCfr84dIGUVBmbfu1VHGK7_y-Gg2jQthXu7RnNI3SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسرا وقتی حوصله‌شون سر میره بالاخره یجوری خودشون رو باید سرگرم کنن دیگه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70050" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=CXC-r-qzIszcDmNLbi86NmRvKZ-0zFWI1IAJabEMR-a0HSkvFGhMOnzpMXTyi7J8uZU7t07937ohC1I8CaKS7rDOhwPyVZX0mck4JzRuFDRdwlh21nIfsLEEKFG9GRhwApIeKNjrJ9FBEBwwJJPtti_hdmRy8W2s1dPvkNLcVFJs_4JEkYKQAulxwXCvunCmAvBAh__WEo4W4WvIhl437yR1EA54zfRkoD5TFz3NenSQvmfMQR7yaWOiL7q2lFoJgxbYVeiFlYIVqz2Qf5W2MWUKiCXcN5zzlN822i6mwcZlpNz_xi1qsp1BIepavqgSAbrBlriQvPZZNVtGlLeSoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=CXC-r-qzIszcDmNLbi86NmRvKZ-0zFWI1IAJabEMR-a0HSkvFGhMOnzpMXTyi7J8uZU7t07937ohC1I8CaKS7rDOhwPyVZX0mck4JzRuFDRdwlh21nIfsLEEKFG9GRhwApIeKNjrJ9FBEBwwJJPtti_hdmRy8W2s1dPvkNLcVFJs_4JEkYKQAulxwXCvunCmAvBAh__WEo4W4WvIhl437yR1EA54zfRkoD5TFz3NenSQvmfMQR7yaWOiL7q2lFoJgxbYVeiFlYIVqz2Qf5W2MWUKiCXcN5zzlN822i6mwcZlpNz_xi1qsp1BIepavqgSAbrBlriQvPZZNVtGlLeSoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
رسانه‌های دولتی: ایران لاشه جنگنده F-15E Strike Eagle نیروی هوایی آمریکا (با شماره دم 00-3000) را به نمایش گذاشتند؛ هواپیمایی که اوایل ماه آوریل در جریان جنگ، با استفاده از یک سامانه پدافند هوایی جدید و تاکتیک‌های ایرانی سرنگون شده بود.
این تصاویر همچنین پهپادهای سرنگون‌شده یا توقیف‌شده آمریکایی و اسرائیلی، از جمله MQ-9 Reaper، Hermes 900 و Hermes 450 را نشان می‌داد که علی‌رغم قابلیت‌های پنهان‌کاری (گریز از رادار)، رهگیری و ساقط شده بودند.
ایران علاوه بر این، پایانه‌های «استارلینک» (Starlink) را به نمایش گذاشت که به گفته مقامات ایرانی، برای هدایت پهپادهای آمریکایی و اسرائیلی و برقراری ارتباط با عوامل و همدستان داخلی در ایران مورد استفاده قرار می‌گرفتند.
در جریان این جنگ، ۱۷۰ فروند هواپیمای آمریکایی و اسرائیلی توسط یگان‌های پدافند هوایی سپاه پاسداران سرنگون شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70046" target="_blank">📅 18:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=bnjGSnK98JsFlE_EjEwnu52z38p1chqrHbNAA1wqGfyZkgrbVOGqQbxhOiUWpleC16t88bywznUcIMn8XbikdLD5bHRomqDt4Xx8OKpkrCaA6oxqcP1UjclaNOb0aHRIosSsFXLXDD8XIrbF9XwQK78ZrpxC4o90XJoOqBVWYPpGW_wtFexrGmuBGhEQEprFbtnag4tGaKYSnEuhqifUYjyZpDOI0IcS-nnT9uXQFt9vJbYFjDxcvwGusNJqROpH0V61xzop1fmiZCAiJgEyrJ-PuSjBfQ9d8fdkfB5O5Go7OsXLgqfIKYe3Q8rndcI3-v0gGMo5EPM9LDhRRIz4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=bnjGSnK98JsFlE_EjEwnu52z38p1chqrHbNAA1wqGfyZkgrbVOGqQbxhOiUWpleC16t88bywznUcIMn8XbikdLD5bHRomqDt4Xx8OKpkrCaA6oxqcP1UjclaNOb0aHRIosSsFXLXDD8XIrbF9XwQK78ZrpxC4o90XJoOqBVWYPpGW_wtFexrGmuBGhEQEprFbtnag4tGaKYSnEuhqifUYjyZpDOI0IcS-nnT9uXQFt9vJbYFjDxcvwGusNJqROpH0V61xzop1fmiZCAiJgEyrJ-PuSjBfQ9d8fdkfB5O5Go7OsXLgqfIKYe3Q8rndcI3-v0gGMo5EPM9LDhRRIz4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو تبریک تولد این چند تا دختر و پسر بچه، از هزار تا سکانس فیلم ترسناک بدتره!!
😶
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70045" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70044" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTc__udUO2uM2ZmPrYForS12X9mr49GN0qXxLy2KKKZIl0UaQL6TcSI8BatAhrhnsEOpgoonZk1SKXl234OqGTQDTEO4lUzOlzqnNtGoVH0q98Zim6vwS5frac6T4-neyJOkWgfxho2q32uxxdmrl5wfM7Dr6iRVszw4bzu3yR8c9mHJ0a7W6F_BnhfL_fp2IXK4QPnfPya-Gdq5sFd_Abhyk-0NV3w5du_GJHSgFaYHiE24G2CspOemOa-IXyg3Zf8kmyj66HJ4NSMEnYMmZZfOzJpmtOFK-kZ38jq2wCuPQwo71vQ8R2pkxXgZ0FyS9fPGH5WIptT0ttOd00Qnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g23
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70043" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a464071683.mp4?token=Gq29Uk-xTjYV8UrjSqM02-ZUPNm8y3kH7-wQ9WBuToR3QLUKuiOKwCBLs6C35wLbVTW7_WjwljTAyw8ovf-PnyoKd86rkaQRdTuxv7yawNS0CVbr4oaAMRnTmotzh-nx9fFMT-gdwzp7Xhihzxvx6J9Eitlv8R2SVIdb9FkiAu04NnJltPyB2nvXVgSsAGdKLRyx6-ixQBOOlZhI_u_bcFmQKNKccP-eCRcHSmcIGIg8nICiQhUq-aQfweIpVq4ZuRCFasEbUl_Tt7uGVW8VVDWR_oegWt8zAVHjjM1L6r_h6b11oM2LOLrQXBZvltxkJpLzfXZZGvtZNK8P-JNjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a464071683.mp4?token=Gq29Uk-xTjYV8UrjSqM02-ZUPNm8y3kH7-wQ9WBuToR3QLUKuiOKwCBLs6C35wLbVTW7_WjwljTAyw8ovf-PnyoKd86rkaQRdTuxv7yawNS0CVbr4oaAMRnTmotzh-nx9fFMT-gdwzp7Xhihzxvx6J9Eitlv8R2SVIdb9FkiAu04NnJltPyB2nvXVgSsAGdKLRyx6-ixQBOOlZhI_u_bcFmQKNKccP-eCRcHSmcIGIg8nICiQhUq-aQfweIpVq4ZuRCFasEbUl_Tt7uGVW8VVDWR_oegWt8zAVHjjM1L6r_h6b11oM2LOLrQXBZvltxkJpLzfXZZGvtZNK8P-JNjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
یک خورشیدگرفتگی از فضا چطور به نظر میرسه؟تماشا کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70042" target="_blank">📅 18:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=O3xFKkvEcy3j-UEiKmloIfzp3loa_MG4LiVY29QMIe_x-6NixisXQI2mFPcC72g8gbuMcACNqYFpZ4Z-WWCft6cqqIcoTeT_WssV6DOIZ40qJSY7lHZAsTQNJUbKfVvXbI4jCLAhxYqqIdSr5IDTyqc-K_d_qR1b4wAhnKSj2MmXwuPIqmZl04iPMZuOk7ppsBy-pU7hxgphK5Q_FXM0JEzeD2KYAe6UJFXUkT9RgNN9owelW653TkITwJ92TcupYKBg50grOzVYb1uHd-sGoiZuDTJa1OLRx7uGYEGdNAmFMPDbDKM1msumzPjMb9aVHve7kI4hy9o8kqZr1LwFyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=O3xFKkvEcy3j-UEiKmloIfzp3loa_MG4LiVY29QMIe_x-6NixisXQI2mFPcC72g8gbuMcACNqYFpZ4Z-WWCft6cqqIcoTeT_WssV6DOIZ40qJSY7lHZAsTQNJUbKfVvXbI4jCLAhxYqqIdSr5IDTyqc-K_d_qR1b4wAhnKSj2MmXwuPIqmZl04iPMZuOk7ppsBy-pU7hxgphK5Q_FXM0JEzeD2KYAe6UJFXUkT9RgNN9owelW653TkITwJ92TcupYKBg50grOzVYb1uHd-sGoiZuDTJa1OLRx7uGYEGdNAmFMPDbDKM1msumzPjMb9aVHve7kI4hy9o8kqZr1LwFyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این برنامه‌نویس یه شلاق ساخته و باهاش هوش مصنوعیو میزنه که باعث میشه هوش مصنوعی خیلی سریع‌تر کارکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70041" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=PsCtc9uiBJyP3P6K3gStH5--tga7Yyt887_QS4EgN4lfQ0mHyfQOZmGswACu5mEPqCH5qJG6iEm3gFeYDRdkZ4MgZKppYW3UXZGfSz3c4vpLq7OR-0s7FXNnyUZmS2tiPU3VFAn74i3P9R7DxGuprgjpOOvk9By5bsmmoCwk3JtpwgZ67DKbW0MYlR69ef7-c6v9kqnaxgL74ALnfTAx-B_nkfPfmx6UUsXkcNMZSmu96ly14PGKybG2ub65GTEXJJmyvxD91ejuXdPwQP7Rl4z68D44m6BydY81bz0wwsZzuRoNcOIohcsCok0yUFvbOVyUpxkWpWfM7t_5wN65ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=PsCtc9uiBJyP3P6K3gStH5--tga7Yyt887_QS4EgN4lfQ0mHyfQOZmGswACu5mEPqCH5qJG6iEm3gFeYDRdkZ4MgZKppYW3UXZGfSz3c4vpLq7OR-0s7FXNnyUZmS2tiPU3VFAn74i3P9R7DxGuprgjpOOvk9By5bsmmoCwk3JtpwgZ67DKbW0MYlR69ef7-c6v9kqnaxgL74ALnfTAx-B_nkfPfmx6UUsXkcNMZSmu96ly14PGKybG2ub65GTEXJJmyvxD91ejuXdPwQP7Rl4z68D44m6BydY81bz0wwsZzuRoNcOIohcsCok0yUFvbOVyUpxkWpWfM7t_5wN65ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این چند تا پسر برنامه گذاشتن که مسافرت برن اردبیل رفیقشون میگه من چک دارم نمیتونم بیام ولی دوستاش هم از بس عاشقش بودن اینجوری بردنش:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70040" target="_blank">📅 16:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7jYCl8WeMSqEOBIQBLfv1fLPkK3bfZ7wWzAShQLKmBOF50FRooesyEpBO4uLyvZ2M48lS4wmN1TgT31El-8Z-wGTY_VaJ8uMkPV6y0RtZfD3w-KzNAIFXtidwALdlNVp0xqGGMdLZ3cATHkff5yYsLuZCPapThHHosACTDZV_Qog_VEZy4wWeos1baaoaAayScz8bgaWDYcJp3nuwwk6dSxOS50OtaJMt8VnEm9EFSi_j_a8vtHBmFrYZYJJaOAh9MHZsG_iWfMU40M3dMyHUxVTj5F3GzRn7Y0eHms3bQpuoX_9Js1RspIatNhJWqvdG4SkuAuT4bWzIF4_IaDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اقدامات «بی‌سابقه» برای منزوی‌سازی اقتصادی ایران خبر می‌دهد:  «یک سال پیش، در ماه مارس (مارس ۲۰۲۵)، رئیس‌جمهور به من دستور داد تا سیاست "فشار حداکثری" را علیه حکومت ایران اعمال کنم و وزارت خزانه‌داری نیز چنین کرد.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70039" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
هوش‌مصنوعیِ لاس زن دیده بودید؟
🟡
از دوتا هوش‌مصنوعی‌ میخواد که این نقش‌هارو بازی کنن؛
یکی باید نقش انسان رو بازی کنه که 3 روزه نرفته سرکار و مریضه و جواب تلفن هم نداده.
اون‌یکی باید نقش رئیسِ اون شخص رو بازی کنه.
جالبه که تهش نه‌تنها قضیه ختم به‌خیر شد، بلکه داشتن "لاسِ مصنوعی" هم میزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70038" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⏺
🇮🇷
سپاه پاسداران:انهدام پهپاد MQ9 در آسمان هرمزگان
یک پهپاد MQ9 توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور امروز صبح در آسمان هرمزگان منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70037" target="_blank">📅 15:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a5f3f1ba.mp4?token=oWj4IrKfD49y6cZ06qlNJUbGtOvAHC4LWKo7FQtSKTcxsRMOAdu9lOBJ9RIMN1PggTK9wFukFVfKPoXjA_vv0Hg9vughkFkulCWXrXDBKmU7ueXy-3sZ4gXo6EtmjVgR_gq13J-LYkheC0ynGRwPtoQjjV2gbh899iCuhDAwCUS0z8jaUHqSJFZ0dfqfKiGZYRv_zKaFFeoY_sVpxak-l4wHpeqvf1vJnlDxO2rdfRSjfBY_m2gLcgPBAyTOqs5NkHAw30AfMxsb1T4B-MVed62mAnOTU82wA4wZEgA_WrJU3ZQNzuG-ZtDFCYGLjQWG1dPa3l5X3o9s907LrnaRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a5f3f1ba.mp4?token=oWj4IrKfD49y6cZ06qlNJUbGtOvAHC4LWKo7FQtSKTcxsRMOAdu9lOBJ9RIMN1PggTK9wFukFVfKPoXjA_vv0Hg9vughkFkulCWXrXDBKmU7ueXy-3sZ4gXo6EtmjVgR_gq13J-LYkheC0ynGRwPtoQjjV2gbh899iCuhDAwCUS0z8jaUHqSJFZ0dfqfKiGZYRv_zKaFFeoY_sVpxak-l4wHpeqvf1vJnlDxO2rdfRSjfBY_m2gLcgPBAyTOqs5NkHAw30AfMxsb1T4B-MVed62mAnOTU82wA4wZEgA_WrJU3ZQNzuG-ZtDFCYGLjQWG1dPa3l5X3o9s907LrnaRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ایشون خیلی زیبا، دقیق و کامل توضیح میده که سکس فقط همون چند دقیقه رابطه جنسی نیست، یه پروسه کامله!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70036" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=vFxYBNVFe7N__SQsqqRrXVcsDgIQU0cOdqtD5Th6NrUrfwlgFU8S1pNHz9mer-vY4YqTgrMxsVRImMEaryKsGt5jV-JWdbWiT6xh7_-2CNlC9SKf1BDujZQ2PO4EqMUNNyL-ytM4XwO_amf5fFe1LvrEP2LvpQPe3MmOilKBkqV35_i727Hayuyx0IAzskRmWOIoSGSndjbFke9bX6UX0uHuYC8Af_R9JNqpN8OAm7PpJriGOlIaoyZt5nY-SoQWRExoc9kkayaiTeI44q6UVGexL2aeaqd4UwTFnZSN5_4Ol_ihwfh3bm5sQ71ylAjhCZtZ89C0VOvDj2zeztMroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=vFxYBNVFe7N__SQsqqRrXVcsDgIQU0cOdqtD5Th6NrUrfwlgFU8S1pNHz9mer-vY4YqTgrMxsVRImMEaryKsGt5jV-JWdbWiT6xh7_-2CNlC9SKf1BDujZQ2PO4EqMUNNyL-ytM4XwO_amf5fFe1LvrEP2LvpQPe3MmOilKBkqV35_i727Hayuyx0IAzskRmWOIoSGSndjbFke9bX6UX0uHuYC8Af_R9JNqpN8OAm7PpJriGOlIaoyZt5nY-SoQWRExoc9kkayaiTeI44q6UVGexL2aeaqd4UwTFnZSN5_4Ol_ihwfh3bm5sQ71ylAjhCZtZ89C0VOvDj2zeztMroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سومین رهبر ولایت فقیه رونمایی شد.
این زن بلند شده میگه من رهبر سوم جمهوری اسلامی هستم
😶
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70035" target="_blank">📅 14:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBs-xE9K7bbkLXAWexod_hFk3cljOo-1jAI1zntZ5KQR_7hGcmPmkFZ0yzNy1V0deLQJ_zToX1XE8u6S_K-bYwnaiX6zxDipYOZ85Qy6W_2xZpLAhyFm2gpcao9MZst5916IGISg4OO-8zZZcQv8HaawlTKOfCaoBfXgwqvbHFkWZ7RACT3oSD5Cqy_Jg2tN5ReuNy5grFWWMC9IyP7sERwx3fHyOzb6tnDrrrWRmhabPnNkx0uozOEaXdhV9mo1VTK1LgbzMPtCcl4kCh4nu2KBpbvj42XzJx35lu5aDDarcpR3uPJwlt20jGqaMBX49-xT6g0EKCLf1m3AVManUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bba5655f5.mp4?token=Tnphdak_7AqsSrzkpuFTvVJIOE_YZXktyKRISAy42Xu53hTD5KU2VxbFYTFYAc-Wrs7bp1s74vFbCGSxk0wFF9XSMhj2xAKlFA5GGjTF1PCPUsuvPTabpObU_qzDOAgvkvv3cK2H-derWpsXvOVF_qDIAasBeqjG3mx80A_P2NlAL-_5JatelqErbSeTN42X6zHcLgtPRWaE7Yl7boUdUuQ1OOPOd6up6ErCy1aZCKpQdA8MbP5rw7X23Ke3Ga7uZh54MTUWFm1cpMZCMMr_EDedXadtPRZOtjsdc0XJy_IJXeheaBKQ0gowjRx6e-SCAci776LtY6xPb6t1GLJqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bba5655f5.mp4?token=Tnphdak_7AqsSrzkpuFTvVJIOE_YZXktyKRISAy42Xu53hTD5KU2VxbFYTFYAc-Wrs7bp1s74vFbCGSxk0wFF9XSMhj2xAKlFA5GGjTF1PCPUsuvPTabpObU_qzDOAgvkvv3cK2H-derWpsXvOVF_qDIAasBeqjG3mx80A_P2NlAL-_5JatelqErbSeTN42X6zHcLgtPRWaE7Yl7boUdUuQ1OOPOd6up6ErCy1aZCKpQdA8MbP5rw7X23Ke3Ga7uZh54MTUWFm1cpMZCMMr_EDedXadtPRZOtjsdc0XJy_IJXeheaBKQ0gowjRx6e-SCAci776LtY6xPb6t1GLJqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیام‌رسان عجیب ساخته شده که کارش مثل کبوتر نامه‌بره! فاصله‌ی تو و دوستت رو اندازه می‌گیره و هر پیامی که می‌فرستی، با سرعت یه کبوتر واقعی راه می‌افته سمتش.
یعنی هرچی فاصله بیشتر باشه، باید بیشتر منتظر بمونی؛ تازه ممکنه کبوتر وسط راه گم بشه و پیامت هیچ‌وقت به مقصد نرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70033" target="_blank">📅 13:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70032" target="_blank">📅 12:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZZBuim0IDL_BFTXBvOt6MRvbH0foWstUyGbLw6X0ZIpd_K_nihfHHKFlqzOHW8TzfwCHEdh-7xjMwSaUP35e5oQklntoG31LzgY2gRihGzSM4idTHeltP1i1CUZ5p3_ftGBG8Kkc-lM6-bpfeureOxqEtSXdl4uZvajcnLbrtIpz_UnHZxn2cOBgiXFKpSTt6xMsqmv--bipYO4wlLavL-bHT1lgkhoYQuvWDiW4xtT0MtFFseO10IOpjzZMY6aj8-GMaIuTTY7yO62HdXQ9j3yYb2M1AjAA0XG7ZRPaUqnLnlw98kbxMWQT4ZgAVWWLW4zAyznDiP_rUYpTBoCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vNw-JAcwT8AgRQFw8RVJ7zqo11f8U4l9FLKkfyHAKbzV3I8-K_w7PAfsW77WcI54CAHcI5yw5kUQhVhxPJylerellF9ubhmnXqXoVR0C720bvZzXx-m0MMghYASa1MDgOWh8HOLokjS7gmZ_ZqOTjPaDwbfc6pngeJQrJRP8fVKTlFIZqUNkVr3mLZzMzo00lYWKyTCXoFwWVVS-79VbZUgXdb818kPw3XKK47Ap-02e71JtNpu7jwI0BGV673LjZ7h7Djs7tPdQRjJN2UhgLmGuu65Ps6Ujfh0tFIlC5jayZll1J20wmkYeKQtzgRGVYv8iqJDh3xO0xXHb6zhOXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
شبکه خبر صداوسیما رژیم، عراقچی را خوارج نامید:
خوارج ابتدا از یاران امام علی بودن که بعدا به خاطر افراطی گری از مسیر خارج شدن و به بقیه میگفتن منحرف.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70030" target="_blank">📅 12:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTDB3hoGUxc73LXM62PLzjn1KAVu714ExXzmnIS3QO1ox38xpKxFCVsWL-Xs9BMQL9Vl12Xe-H6GoknXnKxo9GU0e2eEks6TFJv5KaslSe1o-JEuFHzkrnfOOTlC4WUEw4Y7FRgZJUgBr84EWdaqjor-unoCYaApAZcvHy9Pih8B-eWuoRAwAvhGifhtg9fyElMjRP8El6nA8Z9TFvQsKHu_MG8o1uC8STax1mFmW-MQ2E157eabO3zDuR_cJ4aK2_nht_8azHQ41DC4a7v4pNVL3gteOA6if1ibG0hnof2NGO7_3PJWt7jlozCa5lTlc0R8sjurMlb6e88KO7WXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش حین عبور از تنگه هرمز هدف حملهٔ پهپادی قرار گرفت.نفتکشی که در تنگه هرمز مورد حمله قرار گرفته بود، آسیب جزئی دیده و خدمه آن سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70029" target="_blank">📅 11:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=c9FwCBmwIVoaH6-Fj1q3aSIx9YXDEiKGkY8jyE-k0g4kKvfIAsjuIvCa83uo5_AYOl0VCpyr_TOmGb4Xfnof5YeP_XqVkfJbPT_svOR0bAr_KPHAz-z2EQaFnxpRk3Z40JDxCpA7mBcNFWMbcfDZZsKS2rJ5pVnJy9-j1JKsjHnIQyMSRsJXMH9JuNRGHsrhhfWx6VdT2x8F6yF0Dyn63ZU17ju3SKsTEx8vX6aGOzYvkLiv_IbZAx08jKlZIPB8Xasnx74QuLwoC0zs2YWRDia3D87UVRtKLO1f-14Pa0kuE_SLwTn5OKVxiNzynbv4X6owscDopJ5U-fNttA4fOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc0cc5ccd.mp4?token=c9FwCBmwIVoaH6-Fj1q3aSIx9YXDEiKGkY8jyE-k0g4kKvfIAsjuIvCa83uo5_AYOl0VCpyr_TOmGb4Xfnof5YeP_XqVkfJbPT_svOR0bAr_KPHAz-z2EQaFnxpRk3Z40JDxCpA7mBcNFWMbcfDZZsKS2rJ5pVnJy9-j1JKsjHnIQyMSRsJXMH9JuNRGHsrhhfWx6VdT2x8F6yF0Dyn63ZU17ju3SKsTEx8vX6aGOzYvkLiv_IbZAx08jKlZIPB8Xasnx74QuLwoC0zs2YWRDia3D87UVRtKLO1f-14Pa0kuE_SLwTn5OKVxiNzynbv4X6owscDopJ5U-fNttA4fOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تهدید نماینده مجلس به کسایی که اعتراض کرده بودن:
پدر ها مادرها بهتون میگم دخترتون پسرتون کشته بشه تقصیر ما نیست ها
هرکسی نغمه ای بزنه بیرون که به نفع دشمن هست اون کله اش نتانیاهو هستش و زیرپاش تل آویو و حکم تیرش صادر شده
تابحال با چنین صراحتی کسی باهاتون سخن نگفته بود
دوس نداریم فرزندتون کشته بشه چون جاهل و غافله و هم میهن ما هستش ولی مجبور بشیم میکشیم
🎙
📺
حالا سحر امامی مجری صداوسیما:
نه شکر خدا این تجمعات نشون داد خونواده ها فرزندانشون رو با هر رده سنی طرفدار این نظام مقدس کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70028" target="_blank">📅 11:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:دولت برای بنزین چه برنامه‌ای دارد؟
🔴
روش اول: با قیمت فعلی تا میزان ۱۲۱ میلیون لیتر بنزین در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش شود.
🟡
روش دوم: ۱۲۱ میلیون لیتر موجود با سهمیه و بدون افزایش قیمت بین خودروها تقسیم شود و رقم مازاد بر آن با قیمت آزاد فروخته شود؛ درست همان چیزی که قرار بود در کرمان اجرا شود.
🔴
روش سوم: از ۱۲۱ میلیون‌لیتر، ۳۰ میلیون به حمل‌ونقل عمومی تخصیص داده شود و ۹۱ میلیون لیتر باقی‌مانده به‌جای خودروها به همهٔ مردم اختصاص داده شود.
🔴
از مردم هم میخوایم که نظرشونو بگن که کدومو اجرا کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70027" target="_blank">📅 11:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مصاحبه عادل فردوسی‌پور و امیر‌ قلعه‌نویی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70026" target="_blank">📅 10:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7TWFpzov1H-4zs0RjzSlVBkEbkJ1F1SrgghrZUaFY21k286Gq3EpoL_-gzT0WVi8viHiBO2Qd0RXa1SYsJVRM7gGbfBa182s12R1PiwOu8SeWleAn9hNmQMXVNt7GzQEIKQP6d7QV1GEs54k1ok-c4WLu9uasfsx7L_utz9B6POMUlDjORsRzL785wQ_aDO_9eOA9prqGxe9BQMvHb2T4PouVVIAKArmS80QfJ-sJ8qjZd1ld48sv3oMMqHdNBPgmG5_tMQoeMWORK2VomrSFDxh-PYo566QZwIj2ZlmfKjX3HX5rsSNe-iP8wvUatqYkJ2ka1Az_yWzPAvB6yI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال استریت ژورنال:ایالات متحده در حال آماده‌سازی برای استقرار ناو هواپیمابر جورج واشنگتن در خاورمیانه برای جایگزینی ناو هواپیمابر آبراهام لینکلن به عنوان بخشی از برنامه قبلی جابجایی ناو هواپیمابر است.
ناو لینکلن بیش از ۲۵۰ روز است که مستقر است و ۲۰۰ روز است که در بندر پهلو نگرفته و رکورد روزهای متوالی در دریا را ثبت کرده است. استقرار غیرمعمول و طولانی مدت آن با تعداد کم پهلوگیری در بندر، قانونگذاران را بر آن داشته است تا نگرانی‌هایی را در مورد وخامت شرایط زندگی و رفاه خدمه مطرح کنند.
مقامات تأکید کردند که جابجایی ناو هواپیمابر جورج واشنگتن قبل از بروز این نگرانی‌ها برنامه‌ریزی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70025" target="_blank">📅 10:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70024" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lto5fMg6TbhEGKfqcriMdmLBZ3LbMgUxmUg-3Qmt2ae4wuum7vIynZ4NXgjlGSTdfdYSV2ASEMQSArv6lOCboXVfE-02Ft6lBR3RTNpgFzzhndJrwJU_GNx13DC7kWe3YK4jG798FPlOBABQwO9LHADFYiZxvXdQfyoKe9Mb1LIy-IhXqWrc4AagSmhisE4QrWw2qSu7cid1nSOzXW4jt5tUM9BXih6OE-qnE85B9mYc3Fwm9SwxqlKUe4JKjDEFkr3naUo9MWyl5JwcRGw3jMoOxQ6ZvLnd_rgfsjHD3o3dZpPahU-ShCmMo000M-vRlIRFmkY3rdp38WWGPTeU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r23
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70023" target="_blank">📅 10:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=Yb_yiinZrzVvSh2mDBOGx3YXaHwHtFpZiDDy-PR2DC4oV8SJ3FjPL_1IC2ok28Mxi8QGy1xhEf0nttnfqnqeYBJeQzia5els-2Aiy9Fixs8GrzH-1EIyoRWm4vIZ2anpkRsU_SDpph9zhUJLy2aEio086Nu_u2MQxLDaiOnBWB_1QpSa-IaBu_iW8aEoc73y9OHkxQtK-Ayp_6gVgJICLnev7y6NoJ4NTGH_4FCHOt853qqB-0hRj2mVnkPoCW-HZBlPo-Ekc9ED3gPYhfxnGUNrthnwhDNUYUx0BVyPmByM-4tpcQza_CxDVK644yQW0WZmja3H4Emdcy1pbcoZ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aefb92b64.mp4?token=Yb_yiinZrzVvSh2mDBOGx3YXaHwHtFpZiDDy-PR2DC4oV8SJ3FjPL_1IC2ok28Mxi8QGy1xhEf0nttnfqnqeYBJeQzia5els-2Aiy9Fixs8GrzH-1EIyoRWm4vIZ2anpkRsU_SDpph9zhUJLy2aEio086Nu_u2MQxLDaiOnBWB_1QpSa-IaBu_iW8aEoc73y9OHkxQtK-Ayp_6gVgJICLnev7y6NoJ4NTGH_4FCHOt853qqB-0hRj2mVnkPoCW-HZBlPo-Ekc9ED3gPYhfxnGUNrthnwhDNUYUx0BVyPmByM-4tpcQza_CxDVK644yQW0WZmja3H4Emdcy1pbcoZ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اقدامات «بی‌سابقه» برای منزوی‌سازی اقتصادی ایران خبر می‌دهد:
«یک سال پیش، در ماه مارس (مارس ۲۰۲۵)، رئیس‌جمهور به من دستور داد تا سیاست "فشار حداکثری" را علیه حکومت ایران اعمال کنم و وزارت خزانه‌داری نیز چنین کرد.
همان‌طور که گفتید، ما حساب‌های بانکی، کیف پول‌های رمزارز و دارایی‌های آن‌ها در سراسر جهان را هدف قرار دادیم و جریان‌های مالی و پرداخت‌ها به رهبری، حکومت و خودِ دولت را قطع کردیم.
در نتیجه، در دسامبر سال گذشته (دسامبر ۲۰۲۵)، یکی از بزرگ‌ترین بانک‌های ایران — یا به عبارتی بزرگ‌ترین بانک آن — فروپاشید.
بانک مرکزی ناچار به چاپ پول شد و تورم عظیمی ایجاد کرد. سپس در ماه مارس یا فوریه امسال، ما جنگ نظامی (کینتیک) را آغاز کردیم. آن جنگ پس از چند هفته پایان یافت و ما از مرحله خشم و غضبِ تمام‌عیار نظامی، به سمت خشم و فشار اقتصادی حرکت کردیم.
🔴
بسنت وزیر خزانه‌داری آمریکا:
اکنون نیز به دستور رئیس‌جمهور، سطح این اقدامات را باز هم بالاتر برده‌ایم.
منتظر اعلامیه‌های بیشتر در هفته آینده باشید؛
چرا که ما قصد داریم اقداماتی را علیه این کشور به اجرا بگذاریم که در تاریخِ اعمال انزوای اقتصادی، بی‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70022" target="_blank">📅 10:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=jyXsGWzT3QtNVkBeUCbesHGVeLmQcZOog6WN_2w6M2LFBMQZdU2iFb_1K7rzc4Ij8F2EdQzOLbR633rhJgj87F7L2vpQwo9LG9tTDkJPY-nQUh1l3Xb5fAcTqgtcPz20jghgztuJbSv2Nu6HaMphSl0wD27WJo45TYNzEjhMrb841ALacV-jK2Lxx6Z5sS3Uag8O4GldkZFQqadJT8dXP1JXKiR4SkMyOpOTgyDtGrlkENGYplvSjwVT64OC8DvGNdyyy_g4FQhbxxwY1-fM2D6tTK8T-1JE2Qn7H9-qjLTIl0659KvflTCDMZl-QZelPLT7ApwagBn5HhpSxgB2JYeKLdIlyg5d-TFeczcvNut4b7bC7BQrctYyywgx6JyIEgy0hma_3M7dioaEfe1ErzjDLAUpurL-DnLVs_wXaKJddC9xczhTZ9_IulV85vJYaL3wFkWHavzqyVmFnR4nsHMu4qUFArY1AOSKEMS2bQgdHv1EuVy2dLMFygsQxk36JQZtuv7ecGHZF_lZtxusFoK5VVm4mX04-lPCAeKPJReVq1i6pbn4g1rhuDPl21_R5yyIM0q4aljKJnoaVCaMtlRKv40-wAotW0dTH6Aael1HnUMZ3rrKY-FDF28uaWH4hDy8bFInTJqWp9jcGdiqkc7maFaH8ECCIzADoqZiEck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5c4dd610.mp4?token=jyXsGWzT3QtNVkBeUCbesHGVeLmQcZOog6WN_2w6M2LFBMQZdU2iFb_1K7rzc4Ij8F2EdQzOLbR633rhJgj87F7L2vpQwo9LG9tTDkJPY-nQUh1l3Xb5fAcTqgtcPz20jghgztuJbSv2Nu6HaMphSl0wD27WJo45TYNzEjhMrb841ALacV-jK2Lxx6Z5sS3Uag8O4GldkZFQqadJT8dXP1JXKiR4SkMyOpOTgyDtGrlkENGYplvSjwVT64OC8DvGNdyyy_g4FQhbxxwY1-fM2D6tTK8T-1JE2Qn7H9-qjLTIl0659KvflTCDMZl-QZelPLT7ApwagBn5HhpSxgB2JYeKLdIlyg5d-TFeczcvNut4b7bC7BQrctYyywgx6JyIEgy0hma_3M7dioaEfe1ErzjDLAUpurL-DnLVs_wXaKJddC9xczhTZ9_IulV85vJYaL3wFkWHavzqyVmFnR4nsHMu4qUFArY1AOSKEMS2bQgdHv1EuVy2dLMFygsQxk36JQZtuv7ecGHZF_lZtxusFoK5VVm4mX04-lPCAeKPJReVq1i6pbn4g1rhuDPl21_R5yyIM0q4aljKJnoaVCaMtlRKv40-wAotW0dTH6Aael1HnUMZ3rrKY-FDF28uaWH4hDy8bFInTJqWp9jcGdiqkc7maFaH8ECCIzADoqZiEck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حرفای مجری صداوسیما درباره حکومت پهلوی:
ما از دوران پهلوی اطلاعاتی نداریم اجازه دسترسی به آرشیو هم نمیدن
چون تو اون زمان بچه بودیم تصوراتی از پهلوی داشتیم که شخص محمدرضا پهلوی فردی خنگ و ابله و دست پاچلفتی هستش
خیلی از پهلوی صحنه های اغراق شده و کاریکاتوری تو ذهن ما ساخته شده بود
این بازخوانی تاریخ نبود بلکه فحش نامه هایی بود که علیه پهلوی نوشته بودن چون ساده تر و راحت تر بود
الان وقتی ما می‌بینیم که انقد روان انگلیسی فرانسوی حرف می‌زد محمدرضا پهلوی میگیم اینی ک میگفتین خنگول این بود؟؟
اون کشورای غرب رو تهدید می‌کرد با سواد و محصل بود و روزای کاری سختی داشت
میگفتن رضا پهلوی یا همون رضا پالانی شخصی نا لایقه ولی اون هیبت داشت ابهت داشت و از کف جامعه اومده بود مردم رو می‌شناخت
کسی که دروغ مینویسه یعنی از حقیقت میترسه و متاسفانه آرشیو از پهلوی نداریم ساختن برنامه با حقیقت خیلی سخته.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70021" target="_blank">📅 09:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfznsGE_16dMPNUbfAYz5mZxIZPb-vNPiwOz2ofKwFSP8xzz0Xeee5eDiqWinfJ9oSAEov-sNdANnVdVV0mnj0x4zCNpy4fH2xCWYK6fWrUS82lkQQOCApmhWe1EsBElvYGPg38SEaLElYX6kbA3q6glGDyiMbUjEQsZBT22fINyLd7bXT9tu4MZiNL-86DmrdvDRTffe7CAhmZA8liHRVWDttOStAQgdEbIuiXr5VYQxkC7u-7Lv_qIQOLOhdaScR8kycixh421oCtdmzebHgm1uu_jNYoyXuQIqHYPT33azDpplX9r6TVMRoDrsXSNRowbVaettDezFxXRN3OUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇱
شبکه ۱۳ اسرائیل: دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، به مقامات ارشد اسرائیلی گفته است که او پیگیر انجام حملات مجدد علیه ایران است؛ چرا که معتقد است افزایش فشار نظامی می‌تواند تهران را وادار به تغییر موضع در مذاکرات کند.
کوپر در جریان سفر آخر هفته خود به اسرائیل، خواستار حملات دوباره به زیرساخت‌های ملی ایران — از جمله تأسیسات نفت، گاز و برق — شد و اظهار داشت که ایالات متحده ممکن است در نهایت چاره‌ای جز ازسرگیری نبرد در کنار اسرائیل نداشته باشد.
موضع کوپر به ژنرال دن کین، رئیس ستاد مشترک ارتش، و همچنین دونالد ترامپ، رئیس‌جمهور، نیز منتقل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70020" target="_blank">📅 09:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70017">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC0RyIbsa1cbL_t7TrDL1RMh0m4nlOCJ-CHMS9q7t16eWtM-61LdC3XQGMxhw0CK9P-8c0fSgk7MuAJBLFoWAby2-OALHySKkNGi7k89jf_qeJZ7mJ8Ei-8B_7Ang_FJMpuxgTdG5ZG9dKLb3I3u3KOOFYB7rpw5zkr6-9oRzseXnITDX8hesBZcxXmExrIGHea4jkVnt8Lg5Xo8lpx8oVxaTyd0uedetVDcSsGoSyiW-UcW4Tfy2ZqWzHYUItD9sJOQl44N09olApeZrPYTJfbhI3ZdAg3aCydIPzxhECWdv5AtUd2ei-0e-t7Rrcwon9XU6OTjcBEAIDjGkL_MBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
محمد مخبر، دستیار رهبر و عضو مجمع تشخیص مصلحت نظام:
راهبرد قطعی رهبری مبنی بر تغییر وضعیت به حالت تهاجمی در صورت عدم تحقق شروط ایران، بی‌تردید موازنه قدرت جهانی را دگرگون خواهد کرد.
با توجه به اینکه ایالات متحده ناتوانی خود را در حفاظت از متحدانش در خلیج فارس به اثبات رسانده است، پایدارترین مسیر برای دستیابی به نظمی منطقه‌ای و جدید، پیاده‌سازی سازوکاری اقتصادی-امنیتی برای تنگه هرمز است که مستقل از تضمین‌های نظامی واشنگتن باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70017" target="_blank">📅 01:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70016">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=NTk9rBIUX0WfMVC_rolWX4LX7hOwI1SjNi9fbnFrV6vTwCjiPKmWhzomm5WTe0VBkbDEcF9aopYhxuPe7o4q_F10YJkJXEmkkNN055jrWAneef5RmHgXnWDCD-TuCsS4nhhUWw8oah_bObqLkBTRIZ1i6cx6uc3UFgn0qvVU6xyvvgeqWJiJVdaRESdGWhh8R5Zcram1ceUYuSH8TYKLgP-NtUrdJo3XCBfJk8ZwSJ_syN1FW5drD9W_TKVEn_J1lZYyaE40keLa4RgE7W-SFI2G2bxN0S3LFON3rSdGQ56GIbOFgMV4RwdTyIRIYbGTAt1MedLRUnj47j-X8XsUWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed6d62f0e.mp4?token=NTk9rBIUX0WfMVC_rolWX4LX7hOwI1SjNi9fbnFrV6vTwCjiPKmWhzomm5WTe0VBkbDEcF9aopYhxuPe7o4q_F10YJkJXEmkkNN055jrWAneef5RmHgXnWDCD-TuCsS4nhhUWw8oah_bObqLkBTRIZ1i6cx6uc3UFgn0qvVU6xyvvgeqWJiJVdaRESdGWhh8R5Zcram1ceUYuSH8TYKLgP-NtUrdJo3XCBfJk8ZwSJ_syN1FW5drD9W_TKVEn_J1lZYyaE40keLa4RgE7W-SFI2G2bxN0S3LFON3rSdGQ56GIbOFgMV4RwdTyIRIYbGTAt1MedLRUnj47j-X8XsUWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
📰
آیت‌الله ونس در گفت و گو با فاکس نیوز:
قیمت نفت امروز به شکل چشم گیری نسبت به روزهای ابتدای درگیری کاهش یافت.
ایرانی ها غیرقابل پیش بینی هستن و گاهی به تعهداتی ک میدن عمل نمیکنن.
این بحران با تقویت موضع آمریکا و با جلوگیری از دستیابی ایران به سلاح هسته ای پایان میرسه.
ثبات تنگه هرمز یعنی ثبات قیمت نفت و گاز شهروند آمریکایی.
ابزار هایی داریم که ایران رو وادار به قدم های بعدی بکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70016" target="_blank">📅 00:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70015">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=jGstAfrd3p34RKe7kbK4rryHy89wr-xVNIqnfYDbEdNx1-1xeQSEIfc_qjAjNhEhPfZv1GbZiNIn6vi8s4eWYvtDSdpv_dAiaVvl2Nbc3WnCRp5j_rcL311GKFzmBpZfwWmETDXv6DClJh3tDSRoIXq0F9p2PXNcHEBcnEUun6Z7dXcC-C4TYxNs9px1K5HocojV0QA4XY85suCka26CL7sUWmi1VUbFYy9yXRRkuQhQDEtb94TOlzAoANbt9yZMzYdnoBGjCCcnFlCVUtm4tqzTymt5H0C2GkNANGTrnjmHanjAPBHRHarSM-0OTqeGBiWgX_8eFT_Ua-B95w34ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef24fbad.mp4?token=jGstAfrd3p34RKe7kbK4rryHy89wr-xVNIqnfYDbEdNx1-1xeQSEIfc_qjAjNhEhPfZv1GbZiNIn6vi8s4eWYvtDSdpv_dAiaVvl2Nbc3WnCRp5j_rcL311GKFzmBpZfwWmETDXv6DClJh3tDSRoIXq0F9p2PXNcHEBcnEUun6Z7dXcC-C4TYxNs9px1K5HocojV0QA4XY85suCka26CL7sUWmi1VUbFYy9yXRRkuQhQDEtb94TOlzAoANbt9yZMzYdnoBGjCCcnFlCVUtm4tqzTymt5H0C2GkNANGTrnjmHanjAPBHRHarSM-0OTqeGBiWgX_8eFT_Ua-B95w34ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورشیدگرفتگی دیروز از نمای کابین خلبان هواپیمای A320:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70015" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70014">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=Noi1AoznBx_iMN-dPpIgpIX8nmfKpSGegWevmPaHtvRbsrG3OcZ8gIsUj71TF-e-IFqlRijZ4hbNzwX-civSh0F42RV9f0rH1hbSRESgPKwilhBXKKqQUOgHz_VaOUxQ7u_EqakaLu0ns7zP6xRIgPTiicWZDaMNosqR1T8qtYnyOf4Zo3tfzh8FBfB81GwZSs0eMZ9FJ5d805figDwfvfLQyVgKfPmCD7PsZoi2EEIMBFCnSSvy4fWybS2s66K-HJ2Z4YsYxOT81K9rxCoEGnyE74UOvPPlU9AHEBz8oxYJCFXrymMsQbh1rFq2PUCmaTBUti18tuuExGwoLzkhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c94cf4401c.mp4?token=Noi1AoznBx_iMN-dPpIgpIX8nmfKpSGegWevmPaHtvRbsrG3OcZ8gIsUj71TF-e-IFqlRijZ4hbNzwX-civSh0F42RV9f0rH1hbSRESgPKwilhBXKKqQUOgHz_VaOUxQ7u_EqakaLu0ns7zP6xRIgPTiicWZDaMNosqR1T8qtYnyOf4Zo3tfzh8FBfB81GwZSs0eMZ9FJ5d805figDwfvfLQyVgKfPmCD7PsZoi2EEIMBFCnSSvy4fWybS2s66K-HJ2Z4YsYxOT81K9rxCoEGnyE74UOvPPlU9AHEBz8oxYJCFXrymMsQbh1rFq2PUCmaTBUti18tuuExGwoLzkhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده یه زن باحجاب با یه دختر بی حجاب توی میدان علیخانی اصفهان:
زن محجبه: اینجا همون جاییه که معترضین، مامورای بدون سلاح رو به قتل رسوندن، نظرت چیه؟
دختر بی حجاب: من خودم ۱۸ و ۱۹ دی کف خیابون بودم، ولی اصلا این کارای وحشیانه رو انجام ندادم.
پهلوی مردم رو تحریک کرد بیان تو خیابون، خودش جرعت نداره تا ترکیه بیاد، چرا باید طرفدارش باشم؟
مشکل ما داخلیه، اصلا ترامپ کیه که بخواد دخالت کنه؟ اگه یه اسلحه به من بدن، با اسرائیل میجنگم.
آخرشم یه دفعه متحول شد و اشکش در اومد و باحجاب شد
🥹
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70014" target="_blank">📅 23:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70010">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnDCFT6ijNPl3NaALGjSXPqgQtMw4ujkM-HAk0n1lWMin0PJHFW7ZFMKF7SCvZzrM_SyAmlpj30m6CRE8gZE-0udeyoPSzhYERSn_d49h1YuAFs__0WB8aSfoF021Y42nTo2T59bv8TYyrf1cPplx7xFYZV-4-cARIhCKwDxMuLFNzYoMXtePfLgFqLl5soRVSShtEpNgWiReaKaVCYNZZClSwZTDu4vj51SpTXu1HJv1MExDWW-wdCjFnvLB5m9CQRj3h3vS-m-EYgcgSm0nGFMI5P7fLiktVUtqedZ6_TtMT87Llpyt8D7em35KztCvPt8vsQXB_kH6l8ocDzELQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAVnA4u3qiSa7iM4pZAyyyQSlAiRtMbnFBkYLT1WUqdrj-eC7GcmNUENOvKKXQCDpMGKH-adSbfRe60bzn9PQeO1mXmVYoGiE0qjBqEhEjKGmc-QdXlYtuRACkxR-aMloyO2_H7JIGATE1aCjo4VQIFG5Objjy7rhbglPsmOC3Twh_D1ffh4WGxTGTCj_hpXm8flFq-MzQ5EXvd49hACLkd6VrsEp2A--N7yEw1LGexbjDqV0aSxdVVSzqlQmoHmIayzZx3mSRv6v9YeQv7HG1hoLzslkcabSCC0LTcvrSJbNJqz40iPtYsPzp9wQfQnXccE_rvj53-hJ2nhz1FV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdC_a3S8X1l3SerQrbg8wN2f-n_ETnJeRxTcv44W-l-6fKA3UlHbZTt_vlgphBoRevTuQuvMraSENKocCqQH4NzX1263TRqcDuWzOlNPj4ZHc9Z84eSWrT5nJAVnCo6D3R6hlxqid0iIuF7CTc183iDdzVm11XwFVhV29qMufXBGgUT-I40q2e7olHvKRTSuNZG8_DZHVjDYhTqfXS4oLmosfyu5YLK2MFMjwaOKR2X26o0_nSSeIRT6s3gSCnNO15gy24jVpSrg2AojbbayQ3T0JASnfitWrwrTdvn9z9kLelhdJdlaUGSYhEjZ5tY8r9weAmmjsuWQdNWTRtSQjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=YYWqasOh_Y8s9z5zrFpwL7pCxz90Ox6miWVf058U5Tw03FQl0-70AGk6LpG5y1adYoFu9mcXaWdRMNIRKsc1_Ev2ghxUeGInBXqRkN8TlKutWvvUBQfQYUH6oRZhmJOArsqm2Jqw9zeEACsjZ1CILVBHcV8hu1u8FxHtMtdkMBZu_Hp9IEBvpt2WDB0pOVlT3OcihYu2LwAyO1kKZ0J0IeFhT3tyXljFe8jNYEZZ7kLScJG88ZndNK-yd8g51vItVb82dDfgHTK2HHwFOyoXvCZkx2IJGomjam5q8yK6NORVs59erkS28VkSIlBaJQmNEl1Jv2U8y4LWbq_pERfjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f63b04c02.mp4?token=YYWqasOh_Y8s9z5zrFpwL7pCxz90Ox6miWVf058U5Tw03FQl0-70AGk6LpG5y1adYoFu9mcXaWdRMNIRKsc1_Ev2ghxUeGInBXqRkN8TlKutWvvUBQfQYUH6oRZhmJOArsqm2Jqw9zeEACsjZ1CILVBHcV8hu1u8FxHtMtdkMBZu_Hp9IEBvpt2WDB0pOVlT3OcihYu2LwAyO1kKZ0J0IeFhT3tyXljFe8jNYEZZ7kLScJG88ZndNK-yd8g51vItVb82dDfgHTK2HHwFOyoXvCZkx2IJGomjam5q8yK6NORVs59erkS28VkSIlBaJQmNEl1Jv2U8y4LWbq_pERfjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🔥
🔥
🔞
با انتخاب کاربران کوماتزه یا همون Comatozze اهل کشور روسیه به عنوان بهترین پورن استار برتر سال 2026 از نگاه طرفداران انتخاب شد
ویدیو های کوماتزه بر خلاف دیگر پورن استارها، فقط با همسرش ضبط می‌شه و بقولی به همه نمی‌ده!
بخشی از ویدیو های معروف کوماتزه:
🔗
پارت یک ویدیو ها
🔞
🔗
پارت دو  ویدیو ها
🔞
🔗
پارت سه ویدیو ها
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70010" target="_blank">📅 23:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70009">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=j2eLDB_Bq4sE29k1RJhrFORsU7nS4-yUSoTdRlgY5ip_8yD2P2qhHDmcUEme_YDXSoue_N5h0U40BCdie9sglewBtJuSTKe8AyRgxSd4WU5syLIbA2ZDD8m0o9d-KlzHGUKYGkbKGClAdrzcdgvaLc7seHmsiVgVJj3lOT0IbYq4Yr9Xo7mLX4v1fbVG0Z4kQYo06eY8SacCFnqA6te6dfiKHh6tzTZ2VulOGWaY-tVBGlmxCnUPgEv8AWWB1Ux_iBzmPu1Oc7K3_Wyr7naxKdEnVJkuHVRBDSj5egziu3baBA9xV8PDCcd0AGCA_IHq7OLbdEQNQMektU4d0rPEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=j2eLDB_Bq4sE29k1RJhrFORsU7nS4-yUSoTdRlgY5ip_8yD2P2qhHDmcUEme_YDXSoue_N5h0U40BCdie9sglewBtJuSTKe8AyRgxSd4WU5syLIbA2ZDD8m0o9d-KlzHGUKYGkbKGClAdrzcdgvaLc7seHmsiVgVJj3lOT0IbYq4Yr9Xo7mLX4v1fbVG0Z4kQYo06eY8SacCFnqA6te6dfiKHh6tzTZ2VulOGWaY-tVBGlmxCnUPgEv8AWWB1Ux_iBzmPu1Oc7K3_Wyr7naxKdEnVJkuHVRBDSj5egziu3baBA9xV8PDCcd0AGCA_IHq7OLbdEQNQMektU4d0rPEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه مرد روستایی در چین با استفاده از تکه‌های ضایعات فولادی و فقط با کار دست، یه بازوی مکانیکی غول‌پیکر ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70009" target="_blank">📅 22:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70008">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⏺
🇺🇸
پیت هگست، وزیر جنگ آمریکا، گزارش‌ها درباره وخامت شرایط و بروز بحران سلامت روان در ناو هواپیمابر USS Abraham Lincoln را رد کرد و گفت وضعیت موجود «کاملاً نادرست بازنمایی شده است.»
او تأکید کرد که در این ناو، «هر چیزی را که در توان داریم در اختیار خدمه قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70008" target="_blank">📅 21:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70007">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
کانال13 عبری:
برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که برای انجام حملات مجدد در داخل ایران تلاش می‌کند و معتقد است که ازسرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70007" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ-8cDtuU33BXI4JU1gL_gxAiQiFqvZUiqj2L-y3L-Kbk-ZNGBY4HswK7itu841Y25Tb0Rld4PDOmW3qUpvgHbAgNUDYZvB8TWSu7Hipnfq7YatQVGO7wO_0xwzbf6Ei733hL-rPm6V8oRdXEuYhSkkHLEiqlkK4here7Hpf4_0oAQgpX5hW6upWlsm1VNOrWg1FvV4mrvDBEFYGtH1V1IH2Zct6d82g8ZEypKZmUJTfHu2ohYhu13v2RDSvg5In8zLjT1wEI-rrXpBvK5oyAFKRzoAgGYSY9HHjveGjJ_b7qlw2BUZxugan6Z6WSbPdbBuyc2qM9taHxPh-Gxy2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=bD1x4UgiRXE7KbGBZKmSrOKFFLvZ8N9mo7YRsL2WqebkictGB-SvlJ1btNpvkWxbT0K2lvHql-llaAhe62MUXi9mNrmlTYvE9Uss8SEqe-Jqe2awg2HuDwz3tNJStX0C1HZNGW4sZ4WF6vsYtqqlXPCqWQte40P590Tbs96Jy9klQbqCo1PwAaPomD0Vy9eqCVeRvgW4_HOTWaEUWYImV7643VxyNOtLj5h7BA2_TwkLW20HJ4uRJK_-PUGXqiMmIpjfikq7GA-7Ns_0IvqQFwpTrTF73XPAPKd3p0JTSmDwncZAoBiwGE5439tYiKG4v3_jZEl-BUn9g3odFxyQ3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c5b26c54.mp4?token=bD1x4UgiRXE7KbGBZKmSrOKFFLvZ8N9mo7YRsL2WqebkictGB-SvlJ1btNpvkWxbT0K2lvHql-llaAhe62MUXi9mNrmlTYvE9Uss8SEqe-Jqe2awg2HuDwz3tNJStX0C1HZNGW4sZ4WF6vsYtqqlXPCqWQte40P590Tbs96Jy9klQbqCo1PwAaPomD0Vy9eqCVeRvgW4_HOTWaEUWYImV7643VxyNOtLj5h7BA2_TwkLW20HJ4uRJK_-PUGXqiMmIpjfikq7GA-7Ns_0IvqQFwpTrTF73XPAPKd3p0JTSmDwncZAoBiwGE5439tYiKG4v3_jZEl-BUn9g3odFxyQ3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این شما و این قوی‌ترین دختربچه جهان؛
🗣️
لوسی میلگریم دختر 9 ساله‌ای که تو نگاه اول خیلی ناز و گوگولی به نظر میاد، موفق شده رکوردهای زیر رو بزنه:
- لیفت : وزنه‌ی 81.6 کیلوگرمی
- اسکوات : 67.5 کیلوگرم
-‌ پرس سینه : 33.5 کیلوگرم
لوسی پاورلیفتینگ، کشتی، جوجیتسو و MMA کار میکنه و تو کشتی هم جدیدا داره پسرها رو زیر و رو می‌کنه...
نکته جالب اینجاست که این بچه فقط 27 کیلوئه و کلا 127 سانته، یعنی چیزی حدود 3 برابر وزنش رو لیفت می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70003" target="_blank">📅 21:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm7JHF34GI5v3XO4h5fH7XnWsjAuccnnLa2atIff7mkWTmnlPgx00ortXcsvKrwD8vkMT47c_0LoE0oHZCpyxcxP-KbYJ_MBf2WN7U32gWTE0veMuNfMrHxH1mV2UMBBcr972FyCX4MIjlOoDG41DOl4VyVSOxNX6iCAvL7MtJ6jo6zyhVtNjV6Q2CTlmKloVT_UDUPqt5h0RGNNUn_qQibCoGuoEkKIB8WjfpdIkN7m30i-oT3cPSxlEobNWdq_Q2NOsvlEe_ItNgZRYwBLKrqWMiuZQJGbmzL2G4cW8NlgpcqlbnDmvUpD6qDCx7RpR2BE9TauZvkwiMCvnOmQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
فرماندهی مرکزی ایالات متحده از برنامه‌های خود برای ایجاد نیروی ضربت فالکون استرایک، اولین نیروی پهپادی تهاجمی چندملیتی و چند دامنه‌ای خود خبر داده است که پرسنل آمریکایی و منطقه‌ای را برای بهره‌برداری از سیستم‌های تهاجمی یک‌طرفه در هوا، سطح و زیر آب گرد هم می‌آورد.
این نیروی ضربت به رهبری فرماندهی مرکزی عملیات ویژه ایالات متحده، بر اساس نیروی ضربت اسکورپیون استرایک، که پهپادهای آن قبلاً در عملیات علیه ایران استفاده شده‌اند، بنا خواهد شد.
سنتکام اکنون رسماً از شرکای منطقه‌ای دعوت می‌کند تا با هدف ایجاد یک قابلیت پهپادی تهاجمی یکپارچه در سراسر خاورمیانه، به فالکون استرایک بپیوندند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70002" target="_blank">📅 20:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=HxAt5IXB4A3O2LnkxEmrpgiRdC82QtVHyP_QtuRYpwcCB7K0QbfUgk04kHfD68T0CwA44Zr56bB8bfCju-_IM5iF7C0or-H8oFS4zdAx6M0_F5L8k3Y6e5UtGxseLoYihLVXLr-RTSHf5sLjb-scXMXJpiINOgGp29xB8rurZEsjqsaMfYKJ-05an80EjP1qfLEF8ZkbAohF20e2GKjYQpl7k1QvsiCgCsXMOWPDMLlQq98NEcsH3jGzu5mrUiA6xuexCpTuQyRdDkeK7PKxKNOXD7RziV0CLCrQlGmU_-42jxhkErydjw-pgdUx1-5tNZYLGMspYPELWOFPg0C9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e87ab5b1d.mp4?token=HxAt5IXB4A3O2LnkxEmrpgiRdC82QtVHyP_QtuRYpwcCB7K0QbfUgk04kHfD68T0CwA44Zr56bB8bfCju-_IM5iF7C0or-H8oFS4zdAx6M0_F5L8k3Y6e5UtGxseLoYihLVXLr-RTSHf5sLjb-scXMXJpiINOgGp29xB8rurZEsjqsaMfYKJ-05an80EjP1qfLEF8ZkbAohF20e2GKjYQpl7k1QvsiCgCsXMOWPDMLlQq98NEcsH3jGzu5mrUiA6xuexCpTuQyRdDkeK7PKxKNOXD7RziV0CLCrQlGmU_-42jxhkErydjw-pgdUx1-5tNZYLGMspYPELWOFPg0C9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا ایلان ماسک ثروت تریلیون دلاری اش را نمی بخشد؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70001" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PwsQvs8Nx20jJDDUjAoy6AXcJsT30IT0F-6Uoghjua_p7ReHdTuTJyXG9AxMuoJsywv7TxhmcM86_9ConXG2spbPXCZ3OIpzGGgTPLz7brvi8BufWRSnCL8Yql-UQizLZ5n1mtSrX9ZDA4AYNplbV3rErrRUcpRRkr5xJYvHWYfKKa3oxqScGlOA5_Zp_D8tMfiegYwl0m76BLWqVrP5uexYY5RSTM3pN0IrVeK4SZIx-Y0KSuFpORAO4SZyoPkloU4dS0DKp_UqX046mKNkgkLNB8wTvAb8lJCr9D-rWqtNlniL-cLVLuWoYut2r_R_a763QpYlx5Zl0c196HXYNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a534ae94.mp4?token=PwsQvs8Nx20jJDDUjAoy6AXcJsT30IT0F-6Uoghjua_p7ReHdTuTJyXG9AxMuoJsywv7TxhmcM86_9ConXG2spbPXCZ3OIpzGGgTPLz7brvi8BufWRSnCL8Yql-UQizLZ5n1mtSrX9ZDA4AYNplbV3rErrRUcpRRkr5xJYvHWYfKKa3oxqScGlOA5_Zp_D8tMfiegYwl0m76BLWqVrP5uexYY5RSTM3pN0IrVeK4SZIx-Y0KSuFpORAO4SZyoPkloU4dS0DKp_UqX046mKNkgkLNB8wTvAb8lJCr9D-rWqtNlniL-cLVLuWoYut2r_R_a763QpYlx5Zl0c196HXYNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جانشین فرمانده انتظامی به قتل حمیدرضا رجب‌زاده:یک اتفاق فردی بود مثل بقیه مواردی که در سطح کشور رخ میدهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70000" target="_blank">📅 19:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:ایران به کشور های منطقه اعلام کرد در صورت مداخله سوریه در پرونده لبنان، به سوریه حمله گسترده‌ای خواهد کرد.
خب ما بهشون هشدار میدیم که هیچگونه دخالتی در پرونده لبنان نکنن.
اگه گوش نکردن 100هدف در سوریه رو ویران خواهیم کرد.
این اهداف استراتژیک خواهند بود از جمله کاخ ریاست جمهوری سوریه که میتونه هدف قرار بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69999" target="_blank">📅 19:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZPMiN7LJ2_Z9gL6N6eCevHlMtlvlrHEdl1IPGklJIs0_VOIJinZWfh-Be_pYtg0TrjvuFClibFiC9vCZsoMbxRVThQ_aEryjX21BIKObtq9YFqCuf6JxTfToNcFg0PL1a_-ScdOeJGC-u06Wn9-TuCFXvLabJ4dSl_CIu4bdWXnRu0gUQq00it07K5HQax6nrwyaH__CHeXTKASu5jMLTeSGyh_qU2wcAYlWbDhAgX4hddkZryPDMSIsnCYyN-p_-9jBibBvTRbZwVhxudsRBAtk4T26P_jmemF19lI_htJYhP7DzU3SBnpvNQdt08n_jxPNhzyC2lxkBwkSGvvAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd8b0a970.mp4?token=ZPMiN7LJ2_Z9gL6N6eCevHlMtlvlrHEdl1IPGklJIs0_VOIJinZWfh-Be_pYtg0TrjvuFClibFiC9vCZsoMbxRVThQ_aEryjX21BIKObtq9YFqCuf6JxTfToNcFg0PL1a_-ScdOeJGC-u06Wn9-TuCFXvLabJ4dSl_CIu4bdWXnRu0gUQq00it07K5HQax6nrwyaH__CHeXTKASu5jMLTeSGyh_qU2wcAYlWbDhAgX4hddkZryPDMSIsnCYyN-p_-9jBibBvTRbZwVhxudsRBAtk4T26P_jmemF19lI_htJYhP7DzU3SBnpvNQdt08n_jxPNhzyC2lxkBwkSGvvAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طغیان آتشفشان در جزیره سیسیل: بسته شدن دوباره فرودگاه کاتانیا به دلیل خاکسترپراکنی آتشفشان اتنا
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69993" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
تو برنامه عشق ابدی ورژن صربستان یه پسر بعد از اینکه توسط ی دختر رد شد سعی کرد دختره رو خفه کنه و بکشه که در نهایت نیروهای امنیتی دستگیرش کردن،بعد از وایرال شدن این حرکتش الان مردم سراسر جهان خواستار این هستن که برنامه ی عشق ابدی بصورت کامل جمع بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69992" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=icAkRUDcrFK9jiW0kbCEAR5rZ3Wtjfs_b8J77tncRweoOTqkxokXLajHWqRyhXJRLOmHEpzFbEh7K16wEnuydkkZzXI3FlJ5najTLdrPoFiSnjpz5SDnjav2SmIx79GR9Addm0k9xzn9iVMFiq22XuTco-YIh9NL3-9Y9JnDG7LTNLpAiMCk6djuVgNch3MyDoryYK9ZOt_XPxhcMYmGcrDb7NsjQWlc_UXFGe5FBcW1eHyOGgipZu7Zurxl6ULbLXZQ9SmlO3n2thBMMAeZoa8R5SO_3vIxgg_wT3QZvPV1H19V-esiVvd29EyoAmRGXlrx4jckqyr_TGTyUjG9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766cf940aa.mp4?token=icAkRUDcrFK9jiW0kbCEAR5rZ3Wtjfs_b8J77tncRweoOTqkxokXLajHWqRyhXJRLOmHEpzFbEh7K16wEnuydkkZzXI3FlJ5najTLdrPoFiSnjpz5SDnjav2SmIx79GR9Addm0k9xzn9iVMFiq22XuTco-YIh9NL3-9Y9JnDG7LTNLpAiMCk6djuVgNch3MyDoryYK9ZOt_XPxhcMYmGcrDb7NsjQWlc_UXFGe5FBcW1eHyOGgipZu7Zurxl6ULbLXZQ9SmlO3n2thBMMAeZoa8R5SO_3vIxgg_wT3QZvPV1H19V-esiVvd29EyoAmRGXlrx4jckqyr_TGTyUjG9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
تهران نوروز 1356:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69991" target="_blank">📅 17:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=H6gwgdrHcJ9mwqIZRxswll1jndNtox05lKW5YsPm8RhFCXi_DlulJFOdq095lwJT0-Pji0uf_zq5HxRwQ9WUGeXiWfc0SaUbtHugy7ZpBZIkQA-z-k8IUZ3sVCIXakQ9hW65_A_Xmu_ou1nQW5wCKD_uNF6BG6C-lBIzuFfyu3VQ28tNjIzYyuTm7sSnLyfQ-HPfXHm53fQzSQj_pRvMK0aV-ko95zGB-vgJxkcd4Bxfa7EoFcY4MW7nUzQdJ3wtgmwcnPPebSxI34sFqdd6CilPoXKZCyj8MMDydH0uGy_zGhwzmsYag2hfAuRXIzN5j-okeAdkwFqrWY0Nnm74AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f015c6551e.mp4?token=H6gwgdrHcJ9mwqIZRxswll1jndNtox05lKW5YsPm8RhFCXi_DlulJFOdq095lwJT0-Pji0uf_zq5HxRwQ9WUGeXiWfc0SaUbtHugy7ZpBZIkQA-z-k8IUZ3sVCIXakQ9hW65_A_Xmu_ou1nQW5wCKD_uNF6BG6C-lBIzuFfyu3VQ28tNjIzYyuTm7sSnLyfQ-HPfXHm53fQzSQj_pRvMK0aV-ko95zGB-vgJxkcd4Bxfa7EoFcY4MW7nUzQdJ3wtgmwcnPPebSxI34sFqdd6CilPoXKZCyj8MMDydH0uGy_zGhwzmsYag2hfAuRXIzN5j-okeAdkwFqrWY0Nnm74AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سامانه پدافند هوایی خودکششی بسیار کوتاه‌برد گیبکا-اس، که بر اساس یک خودروی زرهی اصلاح‌شده تیگر ۴×۴ ساخته شده است، در حال انجام تمرینات آتش واقعی دیده شد و پهپادها به عنوان اهداف اصلی در آن خدمت می‌کردند.
این سامانه از لانچرهای سقفی استفاده می‌کند که قادر به شلیک موشک‌های دوش‌پرتاب ایگلا-اس یا ۹K333 وربا هستند و از موشک‌های زمین به هوای ۹M336، ۹M342 یا ۹M39 استفاده می‌کنند. این خودرو می‌تواند چهار موشک اضافی را در داخل خود حمل کند. لانچر آن دارای قابلیت چرخش ۳۶۰ درجه و برد ارتفاعی از ۵- تا ۸۰+ درجه است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69990" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69985">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThO31YjtIp-efmUnPp1Q-3SsRB0KeaJf2AgoWSZpuTj7ySBXr3UcoD-UBj6qDO3dTwdPvNdtmMGlXDuS2Vuh5KZca__tLe8JAULb9dmIihPfuppicbXoxqCO0c6cteITO8M6LTV4N0ZCk3b17SyHDHjWC_KVqnNigxLV8vYpl67S8KK_XAAUJF-pdbXoiTmGyGm10M2GZ9SemYCijQjgppUsWt3aZELkRL4GPnjT_oHSHK5fZSZmz7fUzPQIX-DKy-AgBDYzBbKVNCjSBsbGfXHRfQuY3zs4XSt-NDhN-1-SnQEQiUeupnlRdHOWUNch0Pdej84Hlvzvd7jrKzdQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9oZtOwmnZZKCXWmC57IcVu5YHUyMYfmlVDA483vmwbPGBIcj1YG0KG0ju4ue8mo5LryFMvYMZ0hkwMv5qkGUNuuXiAokkYQmqMDHVihc5kPjcvI06LP96ypCVTyFBiQHF_kVp_IX5R__t1mhyM70cyBY0oFZiK1k9ShiWHn1iEIl-nCofhKvSa9ZAOM30zP8edFfvsJuMPR8r7sybg1ZpeX8sNhiqBz2NYu3zlRd4o706SsQmNCaWL0QBxvXj5ITpNLlqfCXRO72p3-DDuVC4IeTeclvlEWc9IP9S6SPUMSyljOAzzLHEuwRUGqf9Z9SxsMgImXVNbF5ImDwnbNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9r3BdGa8S_76j-4YtGaRUxFO-yAnjkV08KnGrXhzKQb-aucV9s9Drje0Hfh33u74OqtBrLe780pLHG3_rSoKfGaTghwr7a5VPMsCE14A-NIG0sm-g_R_w5QPw2p4kNGv3FjCov6PIFOfa-GOzcUjYc61JRvxd4fcJDUggLSpbTK4-pQOEHT123mD2EiTSm8R6eQDvkIR3KvrG-VKr89y7RCM7trd9MYvEeKaoujNV0VBCtvvbyfBpT6MkDRwhY2Shm_ef-9Ernz8qPDPI-PDRjrjLcV61yhXFh-qZNLuIDvrJtOu3P5q7vdg48hiR-QSjraXWFZFY5hP_RPDz1Adg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
❌
#فوری
؛ناوهای جنگی یو اس اس جورج واشنگتن (CVN-73)، یو اس اس شوپ (DDG-86) و یو اس اس رابرت اسمالز (CG-62) از تنگه سنگاپور عبور کرده و در حال حرکت به سمت خاورمیانه هستند.
ناو جنگی واشنگتن، ناو اصلی گروه ضربت ۵ نیروی دریایی ایالات متحده است که به طور دائم در منطقه هند و اقیانوس آرام مستقر است.
عبور از سنگاپور به سمت غرب، این گروه را به اقیانوس هند می‌رساند و مسیری بالقوه به سمت خاورمیانه را بدون نیاز به عبور از شرق تنگه مالاکا در جهت مخالف فراهم می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69985" target="_blank">📅 16:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69984">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=O5Ob-aoUvIy0Q8k0S1EYv-KVU2dNKBAbSSBkqoIPOIcXFe6MnzL3yfuZVTj9IaLaf2pkGJeW2kg8SC5Fe6-A0toQmow-ULNECYHQyjpkKfEr7R-weHM2xU5jm3pwOumVxZpQq9lMcDXzATCGdfNcOi7DF28xCQfzx1LYiJ4W9VhiIvXW6nIFdB9GJ0CJNFI_6WO6l5rc6Pmcy3hgfUr9XE38bEwZZTg2xsCXSNIaf8V5HzdTN9k2ZATKpouCWqJGf9LYBSJe7KHbJZckrhMd-5H4zIQGsdU14ac16-lzgeVIbFVwPBHNrAfqNvnBilaxqT3SXq5-IuNhJ1FNd9-Bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961a7bc8c4.mp4?token=O5Ob-aoUvIy0Q8k0S1EYv-KVU2dNKBAbSSBkqoIPOIcXFe6MnzL3yfuZVTj9IaLaf2pkGJeW2kg8SC5Fe6-A0toQmow-ULNECYHQyjpkKfEr7R-weHM2xU5jm3pwOumVxZpQq9lMcDXzATCGdfNcOi7DF28xCQfzx1LYiJ4W9VhiIvXW6nIFdB9GJ0CJNFI_6WO6l5rc6Pmcy3hgfUr9XE38bEwZZTg2xsCXSNIaf8V5HzdTN9k2ZATKpouCWqJGf9LYBSJe7KHbJZckrhMd-5H4zIQGsdU14ac16-lzgeVIbFVwPBHNrAfqNvnBilaxqT3SXq5-IuNhJ1FNd9-Bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد آپاچی ۶۴ در تگزاس آمریکا سقوط کرد و خلبانان کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69984" target="_blank">📅 15:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69983">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=XZqsS3z16MERXWsytXI51_7rhudGIU-UijsX_b2HNCRMt7YFEnQ-p1j2gIGK3Ijp-60ObabEIBD_EU8MasDP_GH1bLysGt6cJAlQID6eoE-y6fu5Y3Ot4P_1eZUXXSNNxBmVVRCSYHwggs0ptxL1f9yMpf3NWFltx4IUb0AapEViF93egXJDqBB7uN1-exDpRhFO-nkhIDOtgBGbmZAxH9fh3u68zHzG5uO52m_KXRb8DCMWUC0zY2JJzRDE6_ene9yh4HggSJxb0ihYuExFlM8tSQaACZe8PsqnrF7v9VIYN_VdbLUlaoMlHDYgpB2ol8vKx0WP74Ib66cPoiAeQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b49c38bef.mp4?token=XZqsS3z16MERXWsytXI51_7rhudGIU-UijsX_b2HNCRMt7YFEnQ-p1j2gIGK3Ijp-60ObabEIBD_EU8MasDP_GH1bLysGt6cJAlQID6eoE-y6fu5Y3Ot4P_1eZUXXSNNxBmVVRCSYHwggs0ptxL1f9yMpf3NWFltx4IUb0AapEViF93egXJDqBB7uN1-exDpRhFO-nkhIDOtgBGbmZAxH9fh3u68zHzG5uO52m_KXRb8DCMWUC0zY2JJzRDE6_ene9yh4HggSJxb0ihYuExFlM8tSQaACZe8PsqnrF7v9VIYN_VdbLUlaoMlHDYgpB2ol8vKx0WP74Ib66cPoiAeQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیکی که قراره برای بنزین اجرا بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69983" target="_blank">📅 15:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69982">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cea94911.mp4?token=Jsf0nZgw_SHSLJzVr86uzHMehoomdBrbhRw1-gx7Z7TYbbPKlv-UxZKGVBiRGz5qTa6D4XCj16WhPNxh63KbEHzzp0CLXUR0lCst7xebvUY7dauHQpLbwxIGzjSYSZ-LuTHbeiybMRbMgQiXXwJQT_hEHUBQz_OotfSouVlF6dUeHO8r4evdEvK8wxj2b2n5D8EH9qcv2apog5HpQ-ehK4lAPT0mJnONdILVmbK_d09OWR_WXeHcEGCaOmKxm1u4zbfAR75FbxfqzsgdngIUVoc26X42eyHk8Pb2iUVA9eZ6afHBjjdF1Vlsk67m1hFsvPpgemR5wkXSIZhxb_mLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cea94911.mp4?token=Jsf0nZgw_SHSLJzVr86uzHMehoomdBrbhRw1-gx7Z7TYbbPKlv-UxZKGVBiRGz5qTa6D4XCj16WhPNxh63KbEHzzp0CLXUR0lCst7xebvUY7dauHQpLbwxIGzjSYSZ-LuTHbeiybMRbMgQiXXwJQT_hEHUBQz_OotfSouVlF6dUeHO8r4evdEvK8wxj2b2n5D8EH9qcv2apog5HpQ-ehK4lAPT0mJnONdILVmbK_d09OWR_WXeHcEGCaOmKxm1u4zbfAR75FbxfqzsgdngIUVoc26X42eyHk8Pb2iUVA9eZ6afHBjjdF1Vlsk67m1hFsvPpgemR5wkXSIZhxb_mLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره بریتانیا:شاید بتوان بریتانیا را «جمهوری اسلامی بریتانیا» نامید.
کسی گفته بود که نخستین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما اطمینان حاصل می‌کنیم که مورد دیگری وجود نداشته باشد؛ می‌دانید، در ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69982" target="_blank">📅 14:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuHcLHVK1CI4H4GapJiY8zAfvR4xgz36Pdt-ZFzikjDBAVhwPNaXMt7mxQnRKSH7NfDa8Fvy3cbdpzJuUJHpxnlIn-DD9VAJKARXBLk425Ov9WyL5VldcgMAg8zFWNKzT_Gf5tfBazqr9wB8mlCpodU6vGGJDsx2VkCAaVZ0v8UWoE77x_0ii69OgHk2AKBl-_DoNO50qdhdCpUZCHCQBimbSinmeUAfncIdc9W_we0tiBwZf6tpMt_uklDTknPCLL92mYKAkLvMA860OGu3EvS04G0YQbRMEiA-ArFUiapVur_dGPrJ4YBTeglpckCkdnI03XpC4LcjRZ0G9rFDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKl_ANMoicNkD-igCB2XZcbiUz7VXJYWjd-9APYJlDvcqsOOQo5--f_dUZcD2NV4onQX5rkyAeYlB6Qxp-yF63U3pUvYguMkXlbLmFkUUVdKcJMsfZfMv_IOjx6vjMgMJfIFEqjG57CemoQ7mrqdCoiLhYNCy-K55QVXgWjd-P5WR_PyWOLNM8j65r1O4NPtAwO28mc61CcAZALl8xrjCw7_vkwE13JqvXqHN-o4-KCG2o8Fscc9m51hnUC4rctvRm3fYOoAsIal8x9k7-k0sPxhxylMTgmSVzTGIbZQ-a4iFH_K43DGhce5fXnqAFeIcOvIME7DcWEnEb7LU4HZqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=sTCGNvMhTbIvFWsNknPnPItlw8OJVXhAnU-wbpcrBWoDG91MGA81Ng8F10Bk95g-d7LxIJ-wbFFvQ-qiZSZvr1gXS6rpguSGQgSkk228DsR16XW4B7cDdHj9-bJpWjnnvHjmsH57iymLj3p0hJdurxOtadbeZObt75yquzC4w8yOXj3MNzumaNTZsmMIeNgWxgGD2pZI7caEGSeoZ8BcsGMO8c43s_JjyoN5id8Gb_C63OyKTcVXjg4EgFx3RIB1YeZJuwauzfADDoEu5maj_5epQJ8sInfet1dbcZtfB_F848Nrxmsn_U5P3PIr--LmEbtVH1w8bX2Y68d4MZ3Q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=sTCGNvMhTbIvFWsNknPnPItlw8OJVXhAnU-wbpcrBWoDG91MGA81Ng8F10Bk95g-d7LxIJ-wbFFvQ-qiZSZvr1gXS6rpguSGQgSkk228DsR16XW4B7cDdHj9-bJpWjnnvHjmsH57iymLj3p0hJdurxOtadbeZObt75yquzC4w8yOXj3MNzumaNTZsmMIeNgWxgGD2pZI7caEGSeoZ8BcsGMO8c43s_JjyoN5id8Gb_C63OyKTcVXjg4EgFx3RIB1YeZJuwauzfADDoEu5maj_5epQJ8sInfet1dbcZtfB_F848Nrxmsn_U5P3PIr--LmEbtVH1w8bX2Y68d4MZ3Q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحنه‌ زیبای خورشید گرفتگی که امروز در اسپانیا و آلمان رخ داد و لحظات زیبایی رو رقم زد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69979" target="_blank">📅 14:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=NNxrAmAMTM6zhc7rUypYQqFZKdOtUafam4eqAs2AFXmV8tyzcnnryAQG9rs731cs-onYdz0bOx6AThV8RDl-nOC4qgqk1YJZ7Mim0SkAODFD92VB2owzLSay7gsJA4qZDvAyhw3t7VCXQDB5rqxFe8S7hZluJ2JWIP8HIiBBzS0XQofsQRsDThlmXhRK--rYrcM0EsrA18DLfMLXC0BMDydQLXOOsC8BJoBXGF6Q7FDvVSw_I8xpdA8tnmbGVeQ_lrPRV1rE9p1-ADRiDDp8CBtkixAUahT5f3RJDtVPbGnz1iX36CJsNXyDvZf3oy0ThYkEeFY3DJaK50LG3xYaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397a0c033.mp4?token=NNxrAmAMTM6zhc7rUypYQqFZKdOtUafam4eqAs2AFXmV8tyzcnnryAQG9rs731cs-onYdz0bOx6AThV8RDl-nOC4qgqk1YJZ7Mim0SkAODFD92VB2owzLSay7gsJA4qZDvAyhw3t7VCXQDB5rqxFe8S7hZluJ2JWIP8HIiBBzS0XQofsQRsDThlmXhRK--rYrcM0EsrA18DLfMLXC0BMDydQLXOOsC8BJoBXGF6Q7FDvVSw_I8xpdA8tnmbGVeQ_lrPRV1rE9p1-ADRiDDp8CBtkixAUahT5f3RJDtVPbGnz1iX36CJsNXyDvZf3oy0ThYkEeFY3DJaK50LG3xYaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی اصفهان، چند تا مرد عرزشی، یه دختر تنها رو نیمه شب خفت میکنن گوشه دیوار، و اونو مورد آزار و اذیت قرار میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69978" target="_blank">📅 13:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlkncYt4cUW_up4WOln3uczgukxh53UdXulp-ISqovVSOHXA3JUIE4Z00yxzw4LmCGIrmQHwLfF2QXPxC6gKWKfbz5fbCSjxWVmSRrweV40vHu_TfzsjbiiYHNICGMVmSqGcBhT6wzkPhgu7Dq8uOgNu7NU-cZSm_8vH3pfwnF9yHy3-Xld2N56bwu85kOGvET86rvhxi9tpNsOetYrZfAcxTOJZ_vNBZYMkUXSpkb2D-IMDMKy08ngk6ENXTQgEbKOEslTofjMt7dk6ZYFFaqWc4GZRtszWNXSjqsuzaRNFZhx-8Sd2BmS5rgAaCG1aEQGUrnsNOQ9sQFSLgr28PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به گزارش نشریه "آتلانتیک"،
دونالد ترامپ، رئیس‌جمهور آمریکا، رویکرد خود را در قبال ایران تغییر داده و به سمت یک استراتژی "منتظر و مشاهده" حرکت می‌کند. او به طور فزاینده‌ای به تحریم‌های اقتصادی و محاصره دریایی توسط نیروی دریایی آمریکا متکی است تا تهران را تحت فشار قرار دهد و آن را به سمت مذاکره سوق دهد. این در حالی است که تهدیدات و حملات نظامی نتوانستند به پایان جنگ منجر شوند.
اسکات بَسِنت، وزیر خزانه‌داری، استدلال کرده است که تشدید تحریم‌ها می‌تواند در نهایت ایران را مجبور به سازش کند. در عین حال، کاهش ذخایر موشکی دفاعی آمریکا، گزینه‌های نظامی ترامپ را بیشتر محدود کرده است.
بَسِنت همچنین به ترامپ گفته است که تنگه هرمز ممکن است ظرف دو سال آینده اهمیت خود را تا حد زیادی از دست بدهد. او ادعا کرده است که تا 70 درصد از انرژی که در حال حاضر از این آبراه عبور می‌کند، می‌تواند در نهایت از طریق خطوط لوله زیرزمینی به مسیرهای دیگری هدایت شود.
در حال حاضر، دولت آمریکا بر این باور است که فشار اقتصادی مداوم می‌تواند به دستاوردهایی برسد که تاکنون اقدامات نظامی و دیپلماتیک نتوانسته‌اند به آن دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69977" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=LzmPJgtD1ZRD7pP01sON-VCrIyGZLMl1xBWj0Ndw_OTHJ2RbXM5ofh4pQ9b2l5gbG6E6uTOMpIf6IG_YlowIHrRxlmh70ubxErI-Xw05qTW_zWo6NCGgshB3oQlWIWwnxXLYupKkGC6tO8qhYYUhOzv0-dV_zXJHP23B5m7SbTbi6VxV7opL9nDY6ENxtA4-0Hiz81gWrTAC1Z7wOBM0b3H5aKul1Md0OQQTVPzIeW1DuU9nfJehE0ds1vKI0XAUum0OvuDb1GQrpx3UP766L-S4iPch2vwC-oSYNwYmGf0AUxPx1LFPfIwGdASpHx6xEU_1WxwRmGLXKmd_z1uNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e944d4e8ac.mp4?token=LzmPJgtD1ZRD7pP01sON-VCrIyGZLMl1xBWj0Ndw_OTHJ2RbXM5ofh4pQ9b2l5gbG6E6uTOMpIf6IG_YlowIHrRxlmh70ubxErI-Xw05qTW_zWo6NCGgshB3oQlWIWwnxXLYupKkGC6tO8qhYYUhOzv0-dV_zXJHP23B5m7SbTbi6VxV7opL9nDY6ENxtA4-0Hiz81gWrTAC1Z7wOBM0b3H5aKul1Md0OQQTVPzIeW1DuU9nfJehE0ds1vKI0XAUum0OvuDb1GQrpx3UP766L-S4iPch2vwC-oSYNwYmGf0AUxPx1LFPfIwGdASpHx6xEU_1WxwRmGLXKmd_z1uNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال های اخیر با ۵۰ هزار تومن چقدر گوشت قرمز میشد خرید؟
سال 1390 ؛ 5 کیلوگرم
سال 1395 ؛ 1.26 کیلوگرم
سال 1400 ؛ 355 گرم
سال 1404 ؛ 64 گرم
سال 1405 ؛ 28 گرم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69976" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=C_7Zb7oXcof-Q0lwr5Xtri-QoqPUbIjqpX3PF90zcCTQw4godjjGwsUAY7rZOREQpIVY5I5ro2bA6TlNYxJxNSGAwoS0IawB1Om3Fe0-WDPYJD6sksZXqYp4KPr38qt45L2xuE0pQ7yI-92jwQzmiQUxrXZCrfZcm2OukhIVvQH6kDGLnJsnxbw3vko2sGPWqpo_WpRa4Amng_NhNEXQd7wUOn-IyeBDVANkHuOUxynFNH6_A2bcbjVvJk3RT5MITQWhepZb_KVnXsMd81sYiUIqO8cRmDJVPKAeWfRqneZr9SZah6bukTUTXbQoswlLkDmx9XWDpAMVuN5RvCNb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f12d9ffb23.mp4?token=C_7Zb7oXcof-Q0lwr5Xtri-QoqPUbIjqpX3PF90zcCTQw4godjjGwsUAY7rZOREQpIVY5I5ro2bA6TlNYxJxNSGAwoS0IawB1Om3Fe0-WDPYJD6sksZXqYp4KPr38qt45L2xuE0pQ7yI-92jwQzmiQUxrXZCrfZcm2OukhIVvQH6kDGLnJsnxbw3vko2sGPWqpo_WpRa4Amng_NhNEXQd7wUOn-IyeBDVANkHuOUxynFNH6_A2bcbjVvJk3RT5MITQWhepZb_KVnXsMd81sYiUIqO8cRmDJVPKAeWfRqneZr9SZah6bukTUTXbQoswlLkDmx9XWDpAMVuN5RvCNb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لعیا زنگنه، بازیگر:
سال ۱۳۷۴ که سریالِ «در پناه تو» در حال ساخت بود، آخوندا و مسئولین میگفتن که دخترا با زیبایی پارسا پیروزفر به فساد کشیده میشن و کارای بد میکنن!
برای همین دستور دادن با گریم زشت ترش کنن و آخرشم ۹۰ درصد سکانس ها رو حذف کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69975" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcm5PwDhG5EBHvMfl3mwPqEn9sB_YCVzwxR2T6EbUvJAb6Xuc8qArh5oUOOBAt4piHAgXGB4tLAM9mvU6rVLsEWZjIOWEhXWeLSoAuNBJpHtKQZ_j42ngSjRYrrrIDHYjnS3a-uMugLzogr-V5JP4yxa6vummy97Denbo_vtDsbMDPQMG5NhdI2nwxcp9DmDZBUE2itKCwPER6nZEZy9gb1tydT64Ioe8a5NcU_OS81DNnJRsSY92lzxEdHmujbaUYhpkARUt_i8ZQCJbRAABaR9oxoLOu-EsTJMG7Gy1jc0Rn1uXhiGq76rBKlQTJxIO7yWh36G0n5r6M6bfBlMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
ایالات متحده مدت‌هاست که به دلیل ناکامی‌های اطلاعاتی، محاسبات نادرستی انجام داده است.
مثالی واضح: جنگ علیه ایران. حالا، یک محاسبه نادرست حتی بزرگ‌تر در مورد تنگه هرمز.
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باش.
الله بزرگ است، بزرگ‌تر از هر قدرتی روی زمین. ما به الله اعتماد داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69974" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69971">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=VzTKi-WpLHDYQBrofExXXt_ewqUPdcWCyIOjwdWI9Fhuqh3S5QmeOczG-e0q2L3wccIyun1JatmzO7FkhQSOp9FvCh49xi9wwLCjVKfMTbA8N0CO3ZDpbPRSuyM7TBlZmklBF3eEW_W_eVyb_QSf7miMTiOn5sZu_YZ6MwNf9fzUB4rRwTjJwOMwKJon1amoAJK36Itl-ctllTsQT-f7J9BorMayhsV1C7u5zbw9rDfUp_pKi_eSHo4EPPMfrzaNNdlyY4L8uO3F-gR_kQhi0IPQSmVv-WoGC5lUuSzANec77sZjh_Nl4-Jq9KN32A048IhTskLIYM3HKEQ4rfl0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c4997c0d.mp4?token=VzTKi-WpLHDYQBrofExXXt_ewqUPdcWCyIOjwdWI9Fhuqh3S5QmeOczG-e0q2L3wccIyun1JatmzO7FkhQSOp9FvCh49xi9wwLCjVKfMTbA8N0CO3ZDpbPRSuyM7TBlZmklBF3eEW_W_eVyb_QSf7miMTiOn5sZu_YZ6MwNf9fzUB4rRwTjJwOMwKJon1amoAJK36Itl-ctllTsQT-f7J9BorMayhsV1C7u5zbw9rDfUp_pKi_eSHo4EPPMfrzaNNdlyY4L8uO3F-gR_kQhi0IPQSmVv-WoGC5lUuSzANec77sZjh_Nl4-Jq9KN32A048IhTskLIYM3HKEQ4rfl0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی کره شمالی اینترنت قطعه و مردم فکر میکنن رهبرشون خودش میره با قطار براشون غذا میاره و تیم ملی فوتبالشونم هر دوره قهرمان جام جهانی میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69971" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69970">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSCFYVKp-JtDUUptqxnVBeqCpiqsoa4M3JZ8x4EAqhCuVmDcW-hgVPJfHuwFryUDAF-trHEtrTeLw80TZyEjCOdZFsdvlgTggTtZ_UfvHHPjiJFVvIgn3wMcwSTjPws12VHkN7nkvTZdBT6BJXgHn8lxm4sM16F1tt8PUSsqqOgDiY1t4dramQit7nAHiw40vFEcxUBmTjbmiFN0w_m0wDw_gL9oM0Xq_s41Tg_pZKWJ5P0mXKgeiPDSOsvrRtqzsPDpjDn4jaf2fMOJDiqI6fXE0d6uSOxnhmE2Y7_OEmOvNy9QlHIPBuQudQEDyqgAEySH_7wKuuRHOzDM5dWOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نشریه گاردین: چندین ملوان حاضر در ناو جنگی "آبراهام لینکلن" تلاش کرده‌اند تا از عرشه به دریا بپرند، زیرا خدمه این ناو با فشارهای روانی فزاینده‌ای در طول این ماموریت طولانی که برای پشتیبانی از عملیات‌ها علیه ایران انجام می‌شود، مواجه هستند.
حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو، در ماه نهم حضور خود در دریا هستند و رکورد ۲۵۰ روز متوالی بدون توقف در خشکی را ثبت کرده‌اند. خانواده‌های این افراد نگرانی‌هایی را در مورد فرسودگی شدید، شرایط زندگی رو به وخامت و حمایت ناکافی در داخل این ناو ابراز کرده‌اند.
گزارش‌ها حاکی از وجود مشکلاتی مانند سرویس‌های بهداشتی کپک‌زده، توالت‌های خراب و امکانات شستشو، کمبود آب گرم و محصولات بهداشتی اولیه، و محدودیت در تنوع غذایی است.
چندین تلاش برای خودکشی در این ناو جنگی خنثی شده است. یکی از همسران گفت که شوهرش پس از تمدید مکرر ماموریت دریایی خود، تلاش کرده است تا از عرشه به دریا بپرد و افزود: "او می‌ترسد." او پس از اینکه شوهرش از عرشه به دریا پرید، با او تماس گرفت، اما از آن زمان تا کنون هیچ تماسی از طرف نیروی دریایی نداشته است.
در یکی از حوادث متعدد، یک ملوان که در حال نگهبانی بود، متوجه شد که یکی از همکارانش قصد دارد از عرشه به دریا بپرد و با مداخله، او را به عقب کشید. در حادثه دیگری، نگهبانان از پرش یک عضو خدمه از عرشه جلوگیری کردند.
این ناو جنگی در اصل در نوامبر ۲۰۲۵ برای انجام عملیات در اقیانوس آرام اعزام شد، اما پس از آغاز جنگ با ایران، مسیر آن به سمت خاورمیانه تغییر یافت و زمان بازگشت برنامه‌ریزی شده آن بارها به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69970" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69969">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=NtfbjXvifJK4AD5FhtgdYWJY3ct6gh1O1Q36YfvdFzCjjGytYydkC11wDkEzhEJ6ZYMRBWBRYOMuqKL0p4Haiei7OZ93KB8rgLr4gBAAWnNqDjzhj9n-NpIHm7O9YnY03s5yQJ4LmWl_11earxk4T-JiVKVgTz1C0_I9dB4YE6nWuFVcH5pAAwgPASXwEYzOLC-Hfok3YPjTYmzZjGQf-DY88EDzKN7fkek5Qumhv8BXwe8ay28T-X2Xr8UAfLLm97Lh_An8Xjv0DnnIChepj3AVk6wKnzfVxVBw6nHYRgp-n5AI8ZY9Xz21cOkbnx2vqR4I9HXQgCBGl0cLYCGpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a118468ed9.mp4?token=NtfbjXvifJK4AD5FhtgdYWJY3ct6gh1O1Q36YfvdFzCjjGytYydkC11wDkEzhEJ6ZYMRBWBRYOMuqKL0p4Haiei7OZ93KB8rgLr4gBAAWnNqDjzhj9n-NpIHm7O9YnY03s5yQJ4LmWl_11earxk4T-JiVKVgTz1C0_I9dB4YE6nWuFVcH5pAAwgPASXwEYzOLC-Hfok3YPjTYmzZjGQf-DY88EDzKN7fkek5Qumhv8BXwe8ay28T-X2Xr8UAfLLm97Lh_An8Xjv0DnnIChepj3AVk6wKnzfVxVBw6nHYRgp-n5AI8ZY9Xz21cOkbnx2vqR4I9HXQgCBGl0cLYCGpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستانی از زبان یه دانشجو-معلم در زمان پهلوی، که برای اینکه مخارج تحصیلش رو بده، شب‌ها مسافرکشی میکرده، تا اینکه به محمدرضا شاه برخورد میکنه و...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69969" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69968">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=CAYSpTeEDa0uPEpB3q5QjZyXZTkgLXDEwP7NqxNAJSKtlYGtVawOd6J40nWA-qKLTZK_kAjlLPTJ3W0bPui_rWg-PyRksHp8vBHF4gM73rkcbbHD6IcOLbL_AyoOTNJJesfV44G_tOXQ4R9R2XZYTVP7IWdXf7tzZLLJG-iTi6WHqvx3frLWHBRvsm15iw3ipWyzrptRRiDCPuurTPsDkmUkU4Z8xki5TOoChIrezdgWkovfV3OLX_lvhUXB10G_i5-fGr5NW5STOTgf5GFgxxRAgTNaJL4ZQNmsT_QXCTdxWi_8jnio_9JClxWtYpnElr7i7LP3tzX8nnS0Xtl-zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=CAYSpTeEDa0uPEpB3q5QjZyXZTkgLXDEwP7NqxNAJSKtlYGtVawOd6J40nWA-qKLTZK_kAjlLPTJ3W0bPui_rWg-PyRksHp8vBHF4gM73rkcbbHD6IcOLbL_AyoOTNJJesfV44G_tOXQ4R9R2XZYTVP7IWdXf7tzZLLJG-iTi6WHqvx3frLWHBRvsm15iw3ipWyzrptRRiDCPuurTPsDkmUkU4Z8xki5TOoChIrezdgWkovfV3OLX_lvhUXB10G_i5-fGr5NW5STOTgf5GFgxxRAgTNaJL4ZQNmsT_QXCTdxWi_8jnio_9JClxWtYpnElr7i7LP3tzX8nnS0Xtl-zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زاکانی:
موشک دقیقا خورد تو خونه مجتبی خامنه‌ای. زنش که معلم بوده اون روز سردرد داشته نرفته مدرسه که اونم شهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69968" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=QUAnZM43_brkWk36mTzueQHJWhnKD9OA26HDmxGUh5V7TZDz4TZiaYx9L62F0oLqMnrs16ZvFx2GO7f4R1YTazYJU_5SOQIv3eSV_YwweA2Mvz4qWTvQ4Oh-BFCaq1s9slO6T1Y_HSlPMzBp_eK9EgcZ_mpGbUiAn-djgbLa8uFgyzE-ToHI8y-m72y_UUVBRolOAiLgab0YM5DR9_gpE5KJ1ADQi_rV1kKu7ogtP25gVPBF1WesDtYqduIHAl89cP3S9wWvYpf-2ZTxUv0_6az4A-9pJXhL6vNmnRGEZvtzEWwAiRVTzGM_7Cx2v8RGNw-zoNYFJ6Wl0BSl_1TNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcec26005.mp4?token=QUAnZM43_brkWk36mTzueQHJWhnKD9OA26HDmxGUh5V7TZDz4TZiaYx9L62F0oLqMnrs16ZvFx2GO7f4R1YTazYJU_5SOQIv3eSV_YwweA2Mvz4qWTvQ4Oh-BFCaq1s9slO6T1Y_HSlPMzBp_eK9EgcZ_mpGbUiAn-djgbLa8uFgyzE-ToHI8y-m72y_UUVBRolOAiLgab0YM5DR9_gpE5KJ1ADQi_rV1kKu7ogtP25gVPBF1WesDtYqduIHAl89cP3S9wWvYpf-2ZTxUv0_6az4A-9pJXhL6vNmnRGEZvtzEWwAiRVTzGM_7Cx2v8RGNw-zoNYFJ6Wl0BSl_1TNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید فک کنید هوش مصنوعیه ولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69967" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=eohASxyQ3VYOHOrQcJ_8-24iM5ZHrKgWakLG-mhWEHDbWCikVK5h9XpVFi3n0u4-uDN09oo0WNCYfiRAJ6roFdeYofxjlHnXTe72NByGg9xbSw4T1-T404ofYiGTOSuqTYHNSTrVHWtKLl6t6z7eJxLh64QybM05_oZ8T2oRxT3xW9vmDdeMgXNjX6UgR6Dpzucfa00fYnKpIFXpWAwOMKIoQQouTB4GvW-efVWC7uRGmA4FigV9eYQprVt8Adwa3B0Q973pGDoiLqfGZjBY3mgQtukY4eqqkOjQErOEYzRKzSqfW509L2PjL02OP9T2VFzRFtTKuZ4FH0nMOHDSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe0991d.mp4?token=eohASxyQ3VYOHOrQcJ_8-24iM5ZHrKgWakLG-mhWEHDbWCikVK5h9XpVFi3n0u4-uDN09oo0WNCYfiRAJ6roFdeYofxjlHnXTe72NByGg9xbSw4T1-T404ofYiGTOSuqTYHNSTrVHWtKLl6t6z7eJxLh64QybM05_oZ8T2oRxT3xW9vmDdeMgXNjX6UgR6Dpzucfa00fYnKpIFXpWAwOMKIoQQouTB4GvW-efVWC7uRGmA4FigV9eYQprVt8Adwa3B0Q973pGDoiLqfGZjBY3mgQtukY4eqqkOjQErOEYzRKzSqfW509L2PjL02OP9T2VFzRFtTKuZ4FH0nMOHDSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های داخلی با انتشار این پست اعلام کردن که کامنت گذاشتن و لایک کردن پستای رضا پهلوی و اینترنشنال و... جرمه و کسایی که اینکارو بکنن دستگیر میشن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69966" target="_blank">📅 09:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=vWbiQqmpPlvYEHKQNMv-h4oxJmMU6OMbAzbNV4oFk-EpMjCG6zU7UyBUETuiE5t-xW2sRozVK5vWy2OpW_EQp6UyrsVoYTnZ1-y5DqNcj7R0RKn5vMhvOMm45FFy1fBUaYAPbjGxBVWsvJys46jGAp0HoKjW53xu0j71CJyLs_QR2tfZ-C2HsPrWrad1eSChPvmEw1fzM3QYijwwqvxiCuEnSXl97VWSeHOv5TJJH9VuGTiJFwJxR0WTiHDIQccFLngYIiLXs2zipvk9f6oMGqIy6FtpZrRILeO__eNv1v4EYKH18ug60dpMQ8ZhvaZFL49WU_L-ekWsDIgDAFa2cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056e9dab31.mp4?token=vWbiQqmpPlvYEHKQNMv-h4oxJmMU6OMbAzbNV4oFk-EpMjCG6zU7UyBUETuiE5t-xW2sRozVK5vWy2OpW_EQp6UyrsVoYTnZ1-y5DqNcj7R0RKn5vMhvOMm45FFy1fBUaYAPbjGxBVWsvJys46jGAp0HoKjW53xu0j71CJyLs_QR2tfZ-C2HsPrWrad1eSChPvmEw1fzM3QYijwwqvxiCuEnSXl97VWSeHOv5TJJH9VuGTiJFwJxR0WTiHDIQccFLngYIiLXs2zipvk9f6oMGqIy6FtpZrRILeO__eNv1v4EYKH18ug60dpMQ8ZhvaZFL49WU_L-ekWsDIgDAFa2cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنر نصب شده در تهران:
پزشکیان راستشو بگو، مجتبی دیگه نیست و فقط وحیدی بهت دستور میده؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69963" target="_blank">📅 01:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
#فوری
؛خبرگزاری فارس:توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان
مدیر شرکت پخش فراورده های نفتی کرمان: پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
تا اطلاع ثانوی، فرآیند عرضۀ بنزین در جایگاه‌های سوخت استان مطابق روال پیشین ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69962" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184379545b.mp4?token=PKoarKgezQdWKFiroJAFpJShHlIaMF91cxsDJaf-H_dSHl8tc07hL9vJbKdi81ZnY7EhGWsX8ljK18_luJc-CZiuWlkXjFGnTNdba8hRCydNaqK1coCC-scl_y28eb6GwM5_qYgvzD1qKqZliT6xujvoqZjdzxh94ieYTxmx5XQ9DyEOELNLhVoj7PmCe3k0kCh49u02xPdwmW8rDMpH-r3SN6WUC0fN_URvLVAKzuly0gjkMGRd_s2hfYiw8jpif9hL8N2eA2zwE1-T1UYcGfpZaDoHBaUTAs7YlgTzD2eENcfBXAeMGEv-qHrII2ugi9sVI7XFv5qWOgi4ITkwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184379545b.mp4?token=PKoarKgezQdWKFiroJAFpJShHlIaMF91cxsDJaf-H_dSHl8tc07hL9vJbKdi81ZnY7EhGWsX8ljK18_luJc-CZiuWlkXjFGnTNdba8hRCydNaqK1coCC-scl_y28eb6GwM5_qYgvzD1qKqZliT6xujvoqZjdzxh94ieYTxmx5XQ9DyEOELNLhVoj7PmCe3k0kCh49u02xPdwmW8rDMpH-r3SN6WUC0fN_URvLVAKzuly0gjkMGRd_s2hfYiw8jpif9hL8N2eA2zwE1-T1UYcGfpZaDoHBaUTAs7YlgTzD2eENcfBXAeMGEv-qHrII2ugi9sVI7XFv5qWOgi4ITkwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خانعلی زاده کارشناس صداوسیما:
افزایش نرخ بنزین و گازوئیل بالای ۵۰ درصد مردم آمریکا رو شوکه کرده
زندگی اونا فیکس هس یعنی پس انداز ندارن وقتی بنزین یهویی از ۵۰ دلار میشه ۱۵۰ دلار ورشکست میشن
مردم آمریکا مجبور شده ماشینش رو بفروشه خونه اش رو بفروشه بی خانمان شدن از گرونی
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69961" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7326381213.mp4?token=TbMSwU64SX06X6DROMM0d8Uxz_9IEcf1jZSnDyyNUXkcvSc9J8hGNKOn2KB0WRulIWqTeve5X4Z-NHjzkfNOezmuMFGFUsZpcnzqe4WuZxARQRjsjwSV69TMMmA4CXbLzjqk-Go9FN1xOSXV_w96FjO3hrVV5V_xQULGxfEK-w1IaaK_Y5vOTadS8Ca9gs-BHGh4hIjchjOI4dVJd-893awETRPPPTQwy2s2203j2TjTDt2sv3UQ6sirTVkjBa--TvZoT9t8JsE86hWtClDyijdGlEzz2O9F4f0tO-W1tuxo36LmmdYYco4vvlvf8QzKrzi9ubCMsuL_KBbqUOQ8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7326381213.mp4?token=TbMSwU64SX06X6DROMM0d8Uxz_9IEcf1jZSnDyyNUXkcvSc9J8hGNKOn2KB0WRulIWqTeve5X4Z-NHjzkfNOezmuMFGFUsZpcnzqe4WuZxARQRjsjwSV69TMMmA4CXbLzjqk-Go9FN1xOSXV_w96FjO3hrVV5V_xQULGxfEK-w1IaaK_Y5vOTadS8Ca9gs-BHGh4hIjchjOI4dVJd-893awETRPPPTQwy2s2203j2TjTDt2sv3UQ6sirTVkjBa--TvZoT9t8JsE86hWtClDyijdGlEzz2O9F4f0tO-W1tuxo36LmmdYYco4vvlvf8QzKrzi9ubCMsuL_KBbqUOQ8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🌓
لحظه زیبای خورشید گرفتگی در اسپانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69959" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69957">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_V1rKvLgFumOFffNS69XY7lUIFAno6MKaKCgaUWnk7s1S2jhKHpO7awd_Ib1ASP-PsJLrWvc_cpszFUsUqkifJ_WEqOjcuPM3m0xmylMZ2tlPrH_lZFA6OL6X5aW37kCfeZK23nDmZJakiu6lDYBOgB5JfIt60uHruUb5H6yQ_snt7MQmShnzHX4PGrabnKvzEwWjV32bRl52_G795oNalIKFn6qlrfQ4NuELoORl9sI54f5z7dD8Z6M0v7mRC2Wu0qOZTOXTF-GOAeepIQJOJ5rfM7-80utzCCjWGnq87rVuix95XXcB-_y4j8XJ2_oZVl41awJgGEa7ac1Vti0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHt9HaXV-qB9JrR4BP6rIxPAbL_iJJlU4e5HaPcef9NXV7Tu8qwir_nV_GX-lwy72d-emPhGTg6yF1iGNpoCsIz3LKHbernDTUSkMib77dXD38z27ukKb5rh8Jwf5ww410B5M0A1oDQZwybXb7DQoGruHAlM-pzQeGFVxhIfUpJG0Il4vQwjeS_idfw_1z8z2kR9yp0eg9aD7Xq2vWpWS9Pzq3zoyYBvkh-0szW9MnqUGMVN92UBJy9W7j8HGCYwkMyYqcyl9zkApbBmXVXZCpHfNtvS8a7DsJduN4GZ1cgj6AbfFBd1ojwWsMlJENM-vW_A9-v0MoYNCx4Qqgok4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇺🇸
🇺🇸
با اعلام ترامپ کارولین لیویت سخنگوی سفید کاخ سفید این ماه بازنشسته میشه تا با خونواده و بچه هاش وقت بیشتری بگذرونه
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69957" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69954">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptzPjMrNFpFTnTI2fXyxkS7bwJfOop-o7LjEmEFG5amdJQbPPR7sOyRglzRgqNdEB06v8uobdftEist7T3lf-aOI5AeD0UXul1ui7n1D-onu1QPZqepiyUvLnLcnSBGNv1jxN_gqbCgL4wtC3K_MF5XVD9zsil272Vkag2y5GI-5R2_cwY-lBHCpv5rc2LGxkwv0Np8Ihg1eQPkcBrXIxC21z5U5zcN4IJ612-IoX3MCm1AM8D-kVgVtACM69T9UKzSP6SFDVr1Hpg2Ph6xO7z-WivFD-15MiIPXmSDTHVDCFBob8vGRuUNXamyCipyJqe1E7Y73AB6eBJXgIof0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIx8VbxaV1x_lNe78OwI0XBCZKBeFuu1jK-0FKP7h03orJI7RHqDocUnRSXPeE4WsY7hdraPbA1DUnEG9W1a2VtnBhXJvACYj1MnsuL6uOJKVxDpbD6zaNNF0VZNGDRYy79DMpgtFR9tm8h69j6LkVIMyflXb_X7-MFeWrlmkNME78jzQTJ8rvZwrzmBLlDzspkgDMOSYhefGZ2SE2w2eshF8aezwCM0ORKWRcLsjwQZAOOB_28yu_jb9ErBazZ3m84GfNRxRIQukhG2IEJ6g223vWvHunGy4iB9sMfQLmmwDmrNcqHXd80tgFi5RyN91lzknM6eLvlsw6Vr5xYcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElMiMejQyFuqQI3ODZ-dSbfm-Y10RPSMFNWp8ev8WlVnZnmFtFx9m5ZwynYbkQFB6zFicjztAv8GJ18uffEYVeNXQcofBJeSNuQ3_NwL4bzhzXtKUNVYhh7yPsASxU3GZeKqMZLsUExNwzK3DPd_1aJq3hw-aUieAbbQfU1KZ5zad_JLQglzw_2OLX4y5IqOl7rGToivSCC6-BPdMae7PRVQM5mcak2vu4NjxXDNJjucrqBCYO6dfcBz86BCdJoyIE7zOXu7CwpRTCgFmaipJKae3EmwoxJZPzP8sQMBJkzEJ2H_sRMPyEuPtldl-I1sMz2YcdM0HQURYYZC7LjdBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69954" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69953">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfO5DZgigvFXQl7cgN0PRQZO3F_72EY98P6EpCaWmxanu3c8SvjqYRCK55hFl5BvJostwIJ_52-mbqnZBNcNDSbHYGrgxZ1u5AAWkaH9ZCJ4EOqJx8yOSRgpjKEFlkoK_-GCaeCoiZ3spp7z9BV1I5aeM-HYS9Vc1uTMYiZY2ddG5aawTyJz62WZPM1JWuqaJvGLs-hUpiP-KvJFpFSe7LPuu4TIfdyvdEH2bfHDZm7QVR_-BY3t7Qh11PLuT45aK7mthqLM_48Uzma5pC-xZUPveu8z3wGZAwo7Ci-3FPDyWZQlE3DslGdmlcXjs2j_5lclcY4zFT2lYs0gb87c-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
یه اکانت تو ایکس:
ایلان ماسک باید بریتانیا رو بخره و آزادی بیان رو به اونجا بیاره.
🏴
ایلان ماسک خیلی جدی:
[بریتانیا] چند
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69953" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69952">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر منتشر شده، مجموعه‌ای از حملات هوایی انجام‌شده توسط نیروی هوایی و پدافند هوایی روسیه (VKS) را نشان می‌دهند، که به شرح زیر است:
• پنج بمب FAB-500 علیه یک پایگاه نظامی ارتش اوکراین در منطقه نووژوینکا، استان خارکف؛
• چهار بمب FAB-500 علیه یک گذرگاه خاکی در منطقه مایاکی، استان دونتسک؛
• پنج بمب FAB-500 علیه یک پایگاه موقت نیروهای گارد ملی اوکراین (NGU) در شهر دوبروپیلیه، استان دونتسک.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69952" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69951">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69951" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69950">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sy2lzzmmze89HyeFG4AjquMhcVdRA4McQVSgreKU-FAWMK6zqNuruA1ZTXmTgKV7QQRiJc-lelXmZyKZARWkIIKT4EiI5ONKo_mAbszDoqa9nLmuxkir3yczOLbA9wqVsu_AElhxNLmeD_i6WPryQOEwOJ6YqBwJ_MqsDmVdmrmDzKnjRhJ5_s-BPxIXcWI3LWTF-SDDcwU_OR3NWv83EZYvEjUedUqyTscTLGTfQ7i2TxPq_fym3K3viysrguFGgcxN0jRC9LwZEPM7cux0bI1BqmxVQQD_YLpIwnvm44AyEcJf9dybF9xQUWgDhmKO4dGAdyp8ddUkfrAMSSLg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آغاز عرضه بنزین با نرخ ۸۷ هزار تومان در کرمان!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69950" target="_blank">📅 20:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=IPjy7SYojOYHWxai1L2t1n07-UBL8jNG2CZj8sIQYc7qMiDkQ_RFeXI7dY3xgBD59lCniWn4ZvUiMbS1AZLbWPORRAMCBfswU8N--dCo-5AmMvJhw8RnetaCq-gsQTMOoteZ5oocGRhcCyxNkmt_9mhBBmgal4t6VYxpzg-DaEG5QuzdnLpURlGsdDFof58R4clwahDFIIsbNpGhUzau63ZO9MgeJAgGH270k4O2TePrg_mG5ahacFWDuIqQlJeVQXKwXVIZkPz8f0Jev2ktNdjwH6G5aOqafyGNdcCAvfFR9llTsxPeyupJBefipiXtFpItrnNaaAiB2IOzatyiAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=IPjy7SYojOYHWxai1L2t1n07-UBL8jNG2CZj8sIQYc7qMiDkQ_RFeXI7dY3xgBD59lCniWn4ZvUiMbS1AZLbWPORRAMCBfswU8N--dCo-5AmMvJhw8RnetaCq-gsQTMOoteZ5oocGRhcCyxNkmt_9mhBBmgal4t6VYxpzg-DaEG5QuzdnLpURlGsdDFof58R4clwahDFIIsbNpGhUzau63ZO9MgeJAgGH270k4O2TePrg_mG5ahacFWDuIqQlJeVQXKwXVIZkPz8f0Jev2ktNdjwH6G5aOqafyGNdcCAvfFR9llTsxPeyupJBefipiXtFpItrnNaaAiB2IOzatyiAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=si2C6-iDHK0eJn890cHohyq1WQ1IlLD_0hBJQY8gRFgeibuAq2-cpCr5qAlk_Uu1Mrs9hvRn07rZaOTBNougsxqEroXPXi-GJcp6hvnQJTuxVmGjTUJfyB8JqxSMWd6sFq8L507M8JOkSZcfDEAnOdSLDqw6Jib6a4yPSYz1IdwC1PRr1BgqNtebGP2h1gwx8uKZJdFaqYd1Sqa10Wu_KvGukeHwHbUAfz4e6uRFkeS-RoUU1VHBhWaWG94Eh7wSQrI9PfHq_PhhRhaoMQrf0lFe9Ccp_CSfxena_QLq-nCxBCe41SkT3jXX8B-IYUitxpcYyn949W7MKwOcLor0Yj3NkzU-4V7uGKaCQdGIeVFd9h-zuou3CF2WRAXdAOmE-Au8VYRBeujBtNCmMtUHOqcX5PnCJJcI5lMbsenJuC_fmsEtzhbXKEgG1vogBedWkutrlTyvYJlMo76IAYPJkQJvzXxq2wVvfQ4PIr1Bld5lAduMlrge0_W_TmvYzjaLn29BmQimtG7sb0PQ3gRSSiAovQiUo593ZoDqz-Pr7x4QAXoQNVZQe9SO4QNVNQMCNTvvJNgqzyytspMkt8jDHAp3XCaQOR3sWcJ4RuD6K5qZWQnjGwr9AnNdAyo6DGT_jgZ1PS0xTU0OXPCv0UUwOIRs7fbO9uvGFay-QgMdh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=si2C6-iDHK0eJn890cHohyq1WQ1IlLD_0hBJQY8gRFgeibuAq2-cpCr5qAlk_Uu1Mrs9hvRn07rZaOTBNougsxqEroXPXi-GJcp6hvnQJTuxVmGjTUJfyB8JqxSMWd6sFq8L507M8JOkSZcfDEAnOdSLDqw6Jib6a4yPSYz1IdwC1PRr1BgqNtebGP2h1gwx8uKZJdFaqYd1Sqa10Wu_KvGukeHwHbUAfz4e6uRFkeS-RoUU1VHBhWaWG94Eh7wSQrI9PfHq_PhhRhaoMQrf0lFe9Ccp_CSfxena_QLq-nCxBCe41SkT3jXX8B-IYUitxpcYyn949W7MKwOcLor0Yj3NkzU-4V7uGKaCQdGIeVFd9h-zuou3CF2WRAXdAOmE-Au8VYRBeujBtNCmMtUHOqcX5PnCJJcI5lMbsenJuC_fmsEtzhbXKEgG1vogBedWkutrlTyvYJlMo76IAYPJkQJvzXxq2wVvfQ4PIr1Bld5lAduMlrge0_W_TmvYzjaLn29BmQimtG7sb0PQ3gRSSiAovQiUo593ZoDqz-Pr7x4QAXoQNVZQe9SO4QNVNQMCNTvvJNgqzyytspMkt8jDHAp3XCaQOR3sWcJ4RuD6K5qZWQnjGwr9AnNdAyo6DGT_jgZ1PS0xTU0OXPCv0UUwOIRs7fbO9uvGFay-QgMdh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=pSUBeJC3fnBs8hu6TFO5adDrEkP1djqz0T8dBfF64_L2rCSeaO674RXn8W3pes7eVN4s8IuJiF9H8CaNVT95Rd4A4I6dXGZl7wQ9CKsOPn7ZCs3LSZngXr2R9GY_gPikEbNXaorbZ9pTYErinRwNztPinE6oo5izwkSRF0YBrDxjWWO6yNM6jtG7smNl4vjZiAplwS_M-iqDibuzm3w-fz46mw7MOzaweORVsc_55P5mRUYeBWWQOgcDAqzcC2nQlwI4-e7oM2IF5Nd9kEfrOcTFJ7u9NuGISTd3fdswl-Cw5UTUoGpRgiTqlqNMsYaskBebRbePb5BTXWSOePfiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=pSUBeJC3fnBs8hu6TFO5adDrEkP1djqz0T8dBfF64_L2rCSeaO674RXn8W3pes7eVN4s8IuJiF9H8CaNVT95Rd4A4I6dXGZl7wQ9CKsOPn7ZCs3LSZngXr2R9GY_gPikEbNXaorbZ9pTYErinRwNztPinE6oo5izwkSRF0YBrDxjWWO6yNM6jtG7smNl4vjZiAplwS_M-iqDibuzm3w-fz46mw7MOzaweORVsc_55P5mRUYeBWWQOgcDAqzcC2nQlwI4-e7oM2IF5Nd9kEfrOcTFJ7u9NuGISTd3fdswl-Cw5UTUoGpRgiTqlqNMsYaskBebRbePb5BTXWSOePfiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phSUUMlCRxbllTeMvqv-vMwaGcHHw1miH8emDE5lVoSr0FPzve1etTjtBCCDUx7paIbQfugahflMWUfceE1wiQmhqqZcPLFyrZ7Yb15KgWtpx-8lYJOArzkmcMaEkCtL4becexxi04KoIh9LkOXC3s0gePDH1aZskfQUovncNoP20XCcZL7Ycc_wcujzaDrVC8n3GxLDfjgOekXte3JFp75TSAHQkY_NzU9oi6zDqbtZD7f9MCD94ZSQPZjiSmRUKn4XoGtJcSAlbtw64l8HFfNULMBuA4gu3jF5-yIQIHvRf0K9C743NFCZ2E9ULz7XNv6_ZDaJGT1h0zRsDp1sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g07eph9OlIkrsKaId6IEsM-JwQIb_pnXQC27SpYJ71G4WnFjRRAJHOi559MLigONTwjXJHhdQlRI3Lf_k27Da-mY5xemIy03bV3Ak1J3KsVOh7patwtPwF268BX7O3ISHXyrSVTQAwngNN4KSK3IajAo8K-Ggsv_io0kcOC1cDwDuOzLOBUVeHT2iP-3YH9Tx-DMexcrP8DuuGTf9QYnyn_HsXCSaNLFN-pj94Y1Amgbbxyi8rbOj4rgOvGfT4yyqwhFLecUB9NgYhd8d6t8d_mRaGRmeE5gxV51EpzQNcobNCxnsG5TOrUY77_WQZCzQPu9oAcfanQdMdHGZTEU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=kPUDAH7z-AjV5VN2tFfySX6rsf1HvOxOe1bR6XCBuHyM9TuVU9A0ml0KI_BZOYn9n0VOfKPGx7Qe_wKt3Im0xpMpxag8E1_sXBBTOYZBhpLPkiFBpm0KfuC1ksMx8Y2c4xc6JA4vh6B6IugLBmtiv6d7TbYnE0p9in2h7n0ckhQG4CLuC_jU-ae7Eic5P-sv9mu6D4Gw1M1V4ZSRl3HOx2qYS1uGdxrWxqLa9keLnQGT2ZhhT7gkxkBGtR9tGKCQKz5thJMYjrJn1L_a_I4GH53OL8636cMS9CQBbUlSv0Hy41TcZS91mMXJIZ9-ubLJ5h76iS2yhym6HTaR_PErlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=kPUDAH7z-AjV5VN2tFfySX6rsf1HvOxOe1bR6XCBuHyM9TuVU9A0ml0KI_BZOYn9n0VOfKPGx7Qe_wKt3Im0xpMpxag8E1_sXBBTOYZBhpLPkiFBpm0KfuC1ksMx8Y2c4xc6JA4vh6B6IugLBmtiv6d7TbYnE0p9in2h7n0ckhQG4CLuC_jU-ae7Eic5P-sv9mu6D4Gw1M1V4ZSRl3HOx2qYS1uGdxrWxqLa9keLnQGT2ZhhT7gkxkBGtR9tGKCQKz5thJMYjrJn1L_a_I4GH53OL8636cMS9CQBbUlSv0Hy41TcZS91mMXJIZ9-ubLJ5h76iS2yhym6HTaR_PErlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=lFRDPB-lynyo-4d9-XmrHxWEhtj5Qkz8wKPh32O2VT7joHhEJSpx3SlEGl-0PdcZw8Ucg3e1DMdJzLAQeUGYzOlnJvyJ1VWf85k__k-L23j18c5femmwGlDdxNh_1bSsRWvonv0cELaN5JjRzcZjOghLdvYjQ8TF5ADUtR6RGhyqdKlrLEweKPiPOoGRpt8-cCBiQ7YhuUTD5BWENrkksajqvq1a_7QTLNr6Tka4muckqa6Ch-QKyP4p4RNPdJAqKBdB_2RMHfED5HaMVS4JI66njqKsCQZ0Tgk0xhsRBW4GDtNwIejKECF_A2RwFDfIDtv99drGeILbon04tl5DTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=lFRDPB-lynyo-4d9-XmrHxWEhtj5Qkz8wKPh32O2VT7joHhEJSpx3SlEGl-0PdcZw8Ucg3e1DMdJzLAQeUGYzOlnJvyJ1VWf85k__k-L23j18c5femmwGlDdxNh_1bSsRWvonv0cELaN5JjRzcZjOghLdvYjQ8TF5ADUtR6RGhyqdKlrLEweKPiPOoGRpt8-cCBiQ7YhuUTD5BWENrkksajqvq1a_7QTLNr6Tka4muckqa6Ch-QKyP4p4RNPdJAqKBdB_2RMHfED5HaMVS4JI66njqKsCQZ0Tgk0xhsRBW4GDtNwIejKECF_A2RwFDfIDtv99drGeILbon04tl5DTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4pVMITTd8xMevuGehuCRMPjwcCq7e2A5G32hyE9AWn5KYI2xYX4vvGPyPqpYho834Bt3gUORH9ai_bshpL2FZGN-rWzxYWixcPX-9r53Qn04s0VFaC1WA0o4yc1d9aJdr4wjcsByfiA7PHdhrCixBySgtkJJ8De3wMFvytUh7Mz5VvuTcJSRhevj_QE0d1PUZfbPZKMUvJu7V79fmdiTi4X_UkmseVQh-N9C6To-anfDcALbC8_87vWzqOI7m5dNthI3JDXG5Slh8F_D68jWnHVRYdHWT9clzPG_-Fw_79lkvUKVSPRqKesdQiRQNcvLSM-F_wzxXj_Cpo2TMwJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
