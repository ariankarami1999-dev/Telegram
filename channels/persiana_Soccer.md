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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 450K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqriLFHajIRHfwoOfqnmDuI2GdvzQKaqejMctENwh1daG0Cf5fPO7ZuhN71ROBoMBTEdj-VsRhbItxgkvVScsfy2c6WR6kx7AZVSXeJr0fJ6WOZtIMJ3mJfljjEpF-Do6s1FtozzCsujQzJd08nLV4bQpMJzzDBWOeGkyMUfKlcpyrx-TSsgktOFCEamO-EvRMqbjkXQvEsYPFCOghpZazilSpKMTkKXpaypxBsI-ZQst_O0Kq0GxQPgd9q6_AlnDgM0omO5PZAp4A3ybG88Igtis030AjYROmW9uLep_iFrRZHBS7Z8AoCU_XpZfvjVTQvQljSrfP90DX9Dv3ioeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCBs5rkN8CTmcWkJjMIu9_HZ3v-0PZT9EmD3sqv4RrWK6GS7eq0PLBfjSUxhLUcSC4txe3wdJyqhocYcfuH_ZsWxAelPG7MRpMNnTOaiN5h6KYARK6SV6DIPMQH5ZMk_fOfog6QzzC2ZIl7XgQER78MYsMxIqVAvDMcBvG8G7coK6XRS5pMvD6Bvf95pD7B-4go9U6TaYzpNlFXlmLRUu9DeLXiaXf1wdqmeGUuvI-vJErWZHBnj3dQzTIpadWuK_08bJCofInO5aR0tmpPbdAVy7xKVx8xZWsQ3mZacrWXrY3lgWj8PyzCVI6bNXrNMa6_iRRMP2Qo9LUdnvlaTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjuqlK7DetvZpKR1A5e1wIT9awh_M7pRtiFoVYkoTggjcUTJtA8nIV09-Sih5lkMs-PEbwn1xO2b4yBlSpuBj5B1l51L2DWmbiZvDX53USM4dtFFxhA8tZHzMIddEO8j-8l2ogFHAvTVEL6I0qONN0_PCCTgiQy8-P-VeA6eh_lfbczEuk_TcA4F-6r6yaYaG3nWyPYeaJKNCXK_4O6UatLbGCbgOwRHRQ28dn8rb9irg22CKkY2hUtAF0axLGiVs1EybncvGZANDqqj16z-NIGyxBYcd21lIvlh6m7RvSfbDlI4TLYjLymlv997EE23NOZ7NaqAepPKgbsp0KLpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTffYSjIdZMBgC9KzfB6wehFLLFK7VUues_HSd2qgMuL79TAZq93deMJRrdyi--bKdIBXiUTc0WymZNqci5OZ3OtiepN2BhLroRQoaUH5igCu2CW1PUmGss-yQkm4CsLvSAgfhzrbmr9AN51eyMUD2uJOYUbkYWx_r-U0GIfeEX_u-VlW_pyPIHsRxn74Mo4K0CwB23wbPcdU7NfPkZ1CbB19-0jwM7eSk0Q0RuMZUjbdtFQb6ZRIX0HDlC_f6WJpvngpt04OCl-8fLCER8bZvP_7urRtU0CUy-NqplDd2Ad97MdwhTSVQxQshkYdfnGi0iCzfgmB6PsP_vXG6v2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzygQH4GgW6QiNJlvi4-okX7wvc2aRKrhaGNX-7YNfw1pS8lhczTO180gof9SXPqlYfdcK-KTeDb8TyvLLd0gfRuiVoXYA3p8EhZIUZU8KcoP7NzTMYl6z9xdAZfaqV_0OIr8DXkVp89mGD2goe2mkELjVjpCzsUt-04NMUEq9nmsdZz35uS3ZD5rt-3gu7BNKIAcPtX3eycLUdJqOleYE1oQ9Uj0E7aCjgY4hd_jdZYISSm_o-ZBDjhW0Yhy_lM6NYCc-m9ToVR7HBMc4qx1fuV7xrAp3mYdfX5NojYcf4hxFejcfPNvex7vzWgZnubSegHO9dFF7RxfYgOf2wc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGEe8bTcw0OhECXnIxlNt58bo9oMob15GHL25Q32M6nm7Mzfei9bslCK2xMmqqobRhTmpx0crlD8TxwaJ5BbjdMtD-VWaHHJYUDxtDVZ7irAYFxSq2HoJYqzHtUluBgJ6Pr8T9QTkYFZ263WRlFZ8P1BENPjV_0liSydIr1PCKUCeHkIjphEy4dW9PNj-FsHM6Z4BJPIYRw-O-zCW0RmQ6GozO6BQ06E7-np6TYLvfCKhXSqrRn6X3KtJC1hNRl5Nhzk4Wzrs0ORzBJsbgWARIT4cnoLeoH89lAuQxL1plq6oRWPLeIXWUxVjnZu9NsLqcQws_pik9kWSeUlJC4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXNjP0uhQ3RdTsmXsGtSQCODh5GdU5imEZ7cSjNOpbV14TUxVyAeHYcCp5lGNOojSx3kJEHQAmgMhB6p_oJpOuv3JZ2zs89yGtXxCTCseHMKsDSVaXxQzfMGBfGyr2DGLJ4YujFuOmWg7YO-sTj9AGwVlWP8yCbf6NibrtT-zduABIkYWFBp6esay9NuECNzwdlLaQ361piemOE6u4GYo28Yi4wBkx-TOgLmsuNntnF7yYW_4zPq_KgCMYAhUapEdbKTYURfUoIrOjxr8wj_qfKPXBIPos9jx_U-l7ZZg5K-p6P5Bbf2Djb5tdZ00nGZvnDviOT-ycoTy5E-TatI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la5b1-qvOLXmh9NrtIx9Nq_pI52klFrZCAkHfSIDdXLz9EcCqTuad__Bg9Lcbo9YuxgnnFNeI7TtPFoBkp4oEVoh_p2Ij2vG1oFVmSMOKR0AEl12fR4Bb-9sssa6yGuAYtJJaRNkbQ9XFGPNygyjXz2__jGhQ7mTwqCv48X0m5ZlhMl2MbCzojMHgv-5nucSfV1sfA_ynmgZsEAWx0nOSKdNrybJ135RYlxzNk5YlMSovcvLEHsXC4Myb9i5GtSzj5ZIjJYfNQFSQ6XHJaqd9TU4GbeWIHFUUk2LsrmvN_s8DW4JaBQWyJGLru7jOMRw2-bU46_bCc12_F2fCpNdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bilUJU9g1OpMEuAhG9IezUwSfCRpSv2848xPxKUwf3IiSwoHtlVwAaNDBYROU4jwdu3Cw8rZTCNX7RMBy-PzfYmorF_iXWlAs4cgBsYSwu3GK0u0piTyFEbk1dkkEYPjRsHXy__BHYWuqBUj0179D5xn77-T9bE1mLeDhmWpi86T6It88YYawGIxt492WNhzA8mAzMPKrJ8lsk0TnpbEZrpplJZgcGlYKL4VdsUNmea5RQQtP1umBAaZUObCc1-cF_qc1-0P0udLXyivkTytrcSeE9jkr48Q1BdhVMId7Ey8Y1BQMKvwwS5jUKoqQFFaaaqSn-Fop250UaA-Rb_WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=A7CnRSTxiU_6UX1zC2xdLGdhN7uPnk8C98pTaZb13IRzgarP99UobXcxOBMIdGYscd7DS2xvvwb6lUWKKXGpa3K4SixZw1lQ22zAjkPffZg2KMNGObtf1vDgTgESaJX2KtPmCyDDm8GRAA72GmEPUKGplA8Jbc4SwkmO9muLzagfLjjOPJI-Mg7aPqUtiJ1l2otrM7cBc7dhZ1NNGhb_zKnMVg5TRWQZcU2V6X2fPc-0U6-dXW_99pPC-9aSc2gHdIU6EQ11eenWKUnmaUA-OCsI30L46r8-bkTH18Ejxbhx9rTT4TdLiiJm4jx5gsEsZ9Svn2ceZz_r81qM3_aORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=A7CnRSTxiU_6UX1zC2xdLGdhN7uPnk8C98pTaZb13IRzgarP99UobXcxOBMIdGYscd7DS2xvvwb6lUWKKXGpa3K4SixZw1lQ22zAjkPffZg2KMNGObtf1vDgTgESaJX2KtPmCyDDm8GRAA72GmEPUKGplA8Jbc4SwkmO9muLzagfLjjOPJI-Mg7aPqUtiJ1l2otrM7cBc7dhZ1NNGhb_zKnMVg5TRWQZcU2V6X2fPc-0U6-dXW_99pPC-9aSc2gHdIU6EQ11eenWKUnmaUA-OCsI30L46r8-bkTH18Ejxbhx9rTT4TdLiiJm4jx5gsEsZ9Svn2ceZz_r81qM3_aORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMv9_AdwwddkV5pEeTx_DqqZUeLlSsm_cuYplI2k3gLUJAgtPQfmFX7g289NH0n3xrLH-gsA48zdW4uU8Re4xCWb1egppWCP4ZxafVY1OCz7-NSh1GBE52esaDJRQnTwFHYzj6Rcd23nw0vBKxgbWQ8p_NO4F5cugrbrGZ-eHL07pI2RUvTxrj9LvMekBl7fgWv50MaYiN_B_grrRRHGbf58ImphtWcef4wskYrl0DiZNjd-oJKqlwoVFYhkfEONFyEitiCk-QFoJYsXc0clEANf1Zs9kFQRjghlBs3AAzTNfzdMwBPsiZEOGuqpllc89P4hKVE06XfhP2NhlChaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTtor1zocHM_RbKP9AWj-UtbaGiUtwvJfxl_TL2cxXxOmGsl38cNOU9hOfYXkskb1gg_sxAiNQXNoTtxlhmaxjOCIpxQFKBwTxnkxrl62Mj_zHL3NsENXTp0r-C4_CmqK4zDZLU5res0XRZ7smOvLWBlyV0jkZKT908kP-xg33YYfyC9e4jO_aAsPq4V2glDC2qE2TqqKjMt7ol14IjJ7uTsLRenaTGq-RFF_ln8ujF9dUvHevTxy7ofgQtQwxYqtD0-7AroJGLS3af86TTj4dMgAYNoonoeJ4lgdn2bY7XDNPYsuYNBcljj4qbo5dFuymVpUaDyKQHsPFGQbI10AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUE4l7_T8DFksd7TuW50rpy08Wf12obwnTgg0XX3vgwUpsAlFgYIFGXtdcgcFRW9iprq2UjQEUu4fOKhF7lJAo61FokStDE944cUc0KyJUBR-X-qwaChmCLD1tLjwLF6dOFfgN8d4ktvsjZylrEb4TKvd-DVo13OztxGkz5PairJyDU-xub-TT-wBsnt87kiBvOXjxY-uyo6tvooFRAQVjGNcqOpwZH6WgqsC5ZQ7jPP2kiiY3UXA21ZiJQyMRXJOlg_qiQvbiKFg4OTV512064vn-EBL3Njmvxa-yrYNi5VoHjdVCSl1Gx5gkglHmwLYfzrpA7waQsljfsaQ5ez8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh5H3yez0WNGrgpbCRpFPKYBtkbC_sPHiGjf9gdFZz5xJnj9PpaqY7sz608H3aS7ldxqLPLKMeO0ttnKzQ23Hu0fM7ulIgcamYIlB6gmDADHSfyqwsKepSBikG59QvgDsnJ8zy2TIaWt9xyWOFV8qGAPwOyG7pxG4FL6yBXVKWMgdzmCv2sMyhyiU8ykRCwWOu1pygqA9yDJR0Ksw2QkNU1e60DpM-RF0lKmuaoAYXZZmnIncSoTJvAP8H6IOG433izsEA4G2vkAoVLEINebxV4t6JJ5LK3CAk24kiy5peVHHGG2xxuuBuQ1VAwQ6Am5wzg6rYjtx-MLfsHgrijZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5PgRZmrATEznrWpun0FyQbGZ-iEZ3EN2dztDCNXG7FX0QGt6SXd5ySIbvf9egwfPAZ4FOMWbcqRN6FYbaTfR_sk3xbuorTbiHRwxiWqr0uD_YHgONIKJdLsSPEey-RXaC6E-1pShOzlLeVKxUVPewmKuHT3X7CaXZnsj7h2v1hXtn8kn1_mqFLFLXfuQU9vrYQAhieln-CHgat5SaQMyvsK2SK4A2InDUTBNpAXNzJydmipnjcxvjklw-g2Aci_UTO57hFUsmzP0CdKjQGqUWVxwSm6qrFiJcwc_SuutTxOwI61e8dyJe0nLsrFuNL5Ucml06gY-nj4T2uZarO3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olsbtqf4QTYK4Xy2q02mbWUca8rN2F754nYHqwnR4ogB8o1Uuv6ZBOhOK3pKlK6RwQSvUFWTNXvOBV6N5KVmdoFgDXSM7D3clbVV2hTdrelarg8jXhH9xv7S_4mhZ31A6FNml06OXlHb4sBGuTbP5x_QgWK6plU028XKQg2ykEYxr-j9EGXp3MlZW5LRAw7nAXgoFSE2XuFKeu9es-IZEvUmJ1lhRTlSJ4BT-mZWiEQdwtjxQRfdgk7zrzLPRemJ--jLoilaP-fjIgkGEkpT6AytzRrYEP5KiKCEHCwHfTpxDLZupg_WkY7udMLYrErptOtytPSJu0jO5ycvCFnW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLUwz7T5sdKaYIglJcasOA7eQxE4OWeD7POKdoLzuvG2L_eT867gLISV7ipgSXKxWjOOoKjGx1ij9nDyax2E4338r_5jWyNUbdq6TdjXJiVxgFfKUaAob3afONm9Yfyoj9h2VrRhyMEJp0jUM1UnEcawQhbsMGhTmYvzPEAzbbTIax-cdCg26x0K9sdrJVJ9ENT21x2FiIU4ApKAHpLDUMt7rrbShXMYSht1zRh0gTMDGEDyPeO5zPK_Qn8-1iCzs_JVfItbuNaq8YVdsNtniLyur8Tb54U-sGqjxJ9U0QuhX05ybWVabxIQEWh8-iM_EgQ4SnDAqaUyFhDdx40qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYbUQ_GvdhH_yRMXsVDPznNWd12XIGxl8bxuGvc3qf8Ak4tkWUzCugOEjMKgpkMqfBi2ocXJ2Iao1H653XHxDlNlmpMJM8H-9JgNhwhP_1O1kk1cIkiAA7Y_JO7q5dnkA7MN4EfTlUJu9NJel-7hr7t6fxvG3TyZR0H7ff5UUhYSEGd_IBCGeC9FVYNGtXxcTC-dWXDWwS4peJWPE_O3pdCQdUCxOB6mKsUgbETycLlhDg34IbYbVI9vIB22JwIGnNYlMy6Y04F3JVm_rkL7zQc7iFSMR2Khxe1CDYR5peGPa_ltTC0Gffr9qXxUjjwN2DuoTf0-FFQfvTMDlaRskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilg1B5694AOsv8sSxMvm6LY7HeXfNcp1k2Wa67jEx-na8rvTZIn-2SahcpkFV8ctnupzXtTSdHeFYxvilUGLcazWmKoWfSif9UC7c4NsTN_GJ-AqtiwT_SGKrViCsx5ZzD-YRY6Om_v3U40MmFH39ehY0dXpCBqfSR-eDSvHSX0TSP59HwxxDW98ZPAmb19vCO-lwdInMxaBes_dsGyRoVKxg8um4nbp08s2VxRA1YcqgFulwvxMWcYmSJxnlah5Ysy3nFdJvm6A_FqzosPadcxRRDSb_-fss8wp3DHQKnsoV0ZPOhGft7TpvGeS74Grcc1dZPdH07osCLV46AzB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS8MJkJgzIYw5YolAHcb5kefhhmVZOmgRHK9dNZ5hdzwFOcGflQauagnssqSx1Va0SjRb1wWdzd7ZUuu1htsRXx2Ko9NHrfuFS_lhw1rFew4pRMFYboNrJLjkxu6yVXfPQer6iu1UDE4DWfOcPRKPhiWvYKqPUWuegSOnOX-I5ykmQ2GPylqXG8KWtCopXX3G5ITwWQ08lpLIAjyaRy05UX1oXJiqlBMzu3YUUUhXOKA0fCX-0NRintU-Sv6ut4AG807-TyvF-ZbvSQXBOd6zdF9jqLoFOyG1JV2lHoVylGmv-kA8KHofDUATZo_VcqiVWGdj-PnFKdbvrtBMh0c2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSKNbaDvhEFOuhM9gZuZ7zng8s8k7QJACki0AplsHglZS_k3sSD6L2E7xFYxnvQb3RFTJ33nImOlLSBw38TyoQnCTmHM7xL0jELDf68X0ir8-yakr1QdVavu0VeRmvE9NLzZLKoDczpY_n4-1ppSGvegvGXcQ-13OlVFoBYMWj3xyml6QlNv3pMHUsor0n2iHHYaNQzkOzVxLDNtG64xm3GK6uy4X_lM1zUFvZm6A7jUlsai8kO-k0GR1fR4yKt5h9yio1INjeG22A6gp0tAl4V5liqd-2iZ6v14vlz1qV-4QivRmlw-WLD0hW3shQYn8dR3ok3ya-EqSOEjRu68cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIM1P3OOkMl00T0QiKRymx9BfpQAJKIk4IJL8-gGULtCxNefNN5EG-8nYRkdZIegYqoYoVbO-N5obII_MxKu2D9UjYqmdbb2xaKwhcSMBIHyMU5eI-rtNN1C8PjdGGiZ2LNpI33VWIF2J5p20I-WPwbRZOVs6q6EuAVUba8jdWY8wDGscxo09Aq171PUrSC3Upe96zhGpHhEZ5g16dyWO-47sZCeUxrtRY5bmEVdsOIyNa_MsHi_cRNOXy1CCpbubjcYOoraITQlzXmKagvHkWcHPbrUfEKK9n-CV_-bQy5gXBLkWLqHjuXgELMeoA9NoiQ9M4OLcwFRyExRwMAG9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIs9PQQE95zWrfIe4RrinkNLX89ZdYTEW79BITeYKFX6nz1pDDpsV-Xi4YjdG9sP9Ds4W9OY_yc_f5rcdAT8_ng5pYYJwE5S_Jc1nXuV7MhjlJnO7AU810FebHD4owEjWJe53YFnsm5VpOpYmU6p93KhaY_D3CBiaaUi1PZ8D4OUGPQL-WJuHf46CJkZg5kJgxRVv43F4ed1yPIhtAScqbdiji-ZK-qEF5A1K4zHBW8ZUuiZsVLu18zXYEl6JS2w2W38IN5jLVctsnS96xuS1mp9kgIU28iB_sbITUPsGtd8DcKSMVJn8WXJMviCSA1u_tk3VfW_AI7YSTmaNOo-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=XwF1yGhUoMiEXoWPN0alhJ8DMdvXQSoZVO4PVTD_3n4K6BRys7qUDyBzdKAvIQRJRVdVOncqsUw8j0H5RQD6d7KLscmq3ilfYdfZtrKKQDDqJJa7Pr4zohJd4H1GCyjMj-pbVptIlMFX5rB8FtFOM8CfsP3Em5TLWSQHn8YVcgdMGGnI1vi9o_321EAGUlz6ryr96R3dyI-28MOXRR5sFj3oJKV1BknuH5X-3tclunRcdN72c8tX4YF6NRNZ_J5IRSsfEZHAYv4kfjTnyreq08H64MhXT2xsRibbElerh1rGMQk9k-Gej8kM3JUKfkCIpBH8W0IHv6GiFobGIRC4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=XwF1yGhUoMiEXoWPN0alhJ8DMdvXQSoZVO4PVTD_3n4K6BRys7qUDyBzdKAvIQRJRVdVOncqsUw8j0H5RQD6d7KLscmq3ilfYdfZtrKKQDDqJJa7Pr4zohJd4H1GCyjMj-pbVptIlMFX5rB8FtFOM8CfsP3Em5TLWSQHn8YVcgdMGGnI1vi9o_321EAGUlz6ryr96R3dyI-28MOXRR5sFj3oJKV1BknuH5X-3tclunRcdN72c8tX4YF6NRNZ_J5IRSsfEZHAYv4kfjTnyreq08H64MhXT2xsRibbElerh1rGMQk9k-Gej8kM3JUKfkCIpBH8W0IHv6GiFobGIRC4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMPxev_mPqMWodIVT_4xgkUT-Nibvq7aPDTLl5YwQ1dKdXC7kBrjZ_u4N5o0twLypWaxI7howh5I-6VdrCHakqDVBaCd67XPkjd9eom58-R4twiLzRXRQqYqSOfYfvY4lu7NF7NYM07gxXlD4R_4PBGP9nAS-lh3RzLW7isoEiJKzx8VRffUSCR9dXvD2Bm-VvoUjc1pnQtWI5QzKXYR9ZWdOtljTMA6W3DgY7pnH4LaZeKUkzeL59_J-b0RGwNiz-o-mrgFa0DzJYq_STJKq7YqChtB_wxATPP_g7kPbHHSzQqFdg-GLrJKGBqWPnuB5bDy2Jn08S2aKIj8XUFivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL5DVswHqCNkrdF6PXhHQdO7pxalIyxIzUZSs_0eiu4voedysE_8n4pnzxPBkkOIYAuyW5sIQr23j-tUt6OaxHadVFFBX4nI09CKtn60xGtqLSX3-SYEFa0j95Av-WgKacEzPsx603R_YtjcEnTL0pgm8209sZteicC0CfSmGbcFjCV850kEVU-W0ta_i9AONZ0zxHbnDndqa34vDuhifHHICOtjAWsB0RvxKAfgbjqsxTnf8QrbfROFICqyJHubFbSiIsWKE_pdH-YrA-8AJmcoHFRVy7eLHR4Rb49wrqJzRauHjR9wQ2VHfz66h0nxGlVky6hXEk3ST009y5R3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-24x2mdOMOZuo-NZJKF5N0NwQZIVDKLkAP5zWwNl01c-iasdfo-Qe1U2XTUCrjBnyKk6BJBdZAv-dfENj8z_Y9qau-w8vi5NBqlefGT8bpguB8S5c4JDRDEjbuQg13CxSxyu-wespRSIRLtv16QynsXb7tOc9FKZdADpVi9NyomTsHoKYtcLpLYpIwnyRxrvXaaBKf-ZCjWYFhRDGVyvtmMyLLZHPcmUj1x_UcQfdh56IkmLzEbOOAsR_0-mG68_FNyg9YsV1nEG5UAzjtzfcdluV1vXGZHIkV9pNV--qrXw--ZIySdZ7IWWKtQAPGJFfuBByu0LU3njnHNJ64CIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUkBX7IL5_zofvk58dZbVvGuN-UJfXvnzKSyQtYj9V-fzW6PrAeW-7p0hSnPZnBpDw260hRmHc2mkQIUIUgqhxTkddJjihE-k2-gE1D_ex8MPb69A70RXhJCfGpb5H6ncFHnelrRolQKSDVHpBdy5kyM7G3QlgTTf5PsieeSAgG80TvrvKrvyg8oTPSG25BCqH4G97CWBH-9GP12nvqPp60-Ri3euAyLPLFIW_ip9Y_CqYTsGS1VNXQ43qBGtHrYDeSei4r3ryMbs2_IYs-HSZGwHUVMK2r7jbWRjkPFTbzGGey193y7BgHqelPdrxobqLKsogQBPtMYrGZyojU-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjpNRrEB5DmFwZUbWnjCxQ2aJzXtWBK2JhJ113iXcJ2D4nxgpBG_lKCmZanL5V6iUZtHJpII9xjPftPsnAmzj0x_Y39VcQHoqPg_AovyA-7wKeyKg9SKQQXB-TFEjq8QbKcRnYbFd8EtY-lQmm33iU7Ormh0OvZeWoKqVMtVbSrP7s9jesBIYz2hFhYzo9kntwedRYIvT9_XCsMS0SChmlwxgDGmOnkyHqrchHqhu8mXjEPa4SR2ea3XWG_CwOpQFHmr6xNJow99wbpPxPPHL4nJq6D0ayPPROHtE6oJgaaVvFnEBoI2_kngOZwvwfMiQJtV_GUuE1cK8NmdiKVujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ZbnaWVTskLm0Lim8ouDuZqxBAk04g9vzxWHfN1YI0N2fYON0_L2O-8SIroZMcuz-9DajPu4kvsLxvJgjjak2nGNl4gZ6-bSsbC5NqkJNnF7pdHVBxt7rSTcIjsKHPApVjdgytqE7AlIogcjQuy-A4n7_aer6ACNOqNsMy255GlDukUpuSihpvc7Gq_pN_rGTiNm0bEisC_mZSQsn1gVaukTbZCvm-36f4dlZ5dqtTBoKX6LsKTYlavkFKCJd_S9dOxdSuqoIGR7nT9Ud85nNl34gUVtvfYcYYYjcot2Dj5VKx9sR_KSG_2mWLuNPH9INkVIsU3jPz3VQkmGGtGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDqCNGni-9-u0xPzHJlUR4QTpIW2cvP9_QwGpj0c3m5w9ySpBZzKZrEPk6sQOZIfoc2hZeKqhGOliruemJOq7Qhk0A8jWTxXYwhji74VOODqCR_3G9-nKUIf63WMN9KMrHqRUtXhblBStIUs3Fsjf5B1DhBrHK5FQs7NkBTUZxPwJY0OsF49t0q1q1gZ4SDt1Eh9LgClrGdv2OqVtS6elAUPYHeav7QLdzj2bzlLdz24JWEjsIT9T-fCmnxbP1cYpiXQ5b96Cs0qVcKaktY2sWbB5DZieXOzFd7ZQ2qyCnfrTVn9YfGcMkGFm4AHzgjVpKKgM8KRih-ynjBIhHM7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8oyYgwhcW8r8jc05V6629rU21iw2GBhez1kcUv2oBZa_Naazy8RnR987me2_PcFT8GUd1YsCGtFMX1WVJjOcnOElfo3NCQSUszmPMw8gc5zO9MsGiwiOFb5WCkWATvZjBQKr3LDaXxcsvJPDPqSv5H6zKt04j2N37IvhPuvqPeU_7klhnHP3YCeFOof8anHuOhwcS9ifoOEC3HAo0t7uaXfZDH4FoGkA3EzdPI77UyCFZENedw8NAGKqDIL4ocX5pk5YSk1TzZj7WI-ct1XhXHhnMoSoWE5TblGhmsOfR3-xWXVdtyML532yMD0hC_tJw_XLduh6NNunpZH7XzY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldS23AfIboLCwCxKm_lXqxO9g6460TukndzIE3AOG_W8vAWA4OnPAFt3CkURNHBRPYP-nB2kpTWf0-RJW9Gf88OT7ITeyycUc8zs7V1UcFup-HYeWLwGIBHJzz11pWsUnxaaBRlk3Yib6cJSsb1EvlUIncxrUoWTYFgZpqKruPvJoltysA6hjlAzuFPIBbnomafOxvsI1PmNtYa4bS17pIgMokgh7WMUpnOQkJBqh1uOFdTlManwTJ3vT1Sda-MstnTzURpb-xGLHp4w6aos0PGA1MLKBRlaIkw2Jh18bX28qrILJE2PBDtB2eb-5zsjJAqaIhS0cDqiThUX--IjZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq1ez2_KTZyRWR8-9GMKowEju4bwoCnhX68jB-iGQZu1xDZHUkGg2nmptfPsAeD1MbobVWuG-PI4JY0clRKEiXzEyLYsxg1JAjNOdiv-x8RDgXEDCd7TBRFFQRc190LBQsPRFxMH0RTdXNrjS64Mscv7hBMGtZpJ74M0l4h_C0N2OC7rRsnBiCpsU6_rN4U9j8NOdnwVPPx4ZFLQuLRWJQdt4UE7c1MqKbrUA5SlP0wrss1L8EVsi6hhQ47i_EMR52gt8VQRJTnVs3L47aCX152waukPSZKngUFAbxTuff_LQAdfNhhfVrwLFre3qOxp9UAEejgDNhuXY6wyQQjKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glPGoC2Z5hP44MSoS5lwojzWo8oPwwF9MiMOEnUp4QGaubsEQUdtp_Svwut4bcSC2sDJyCYxl-DnaRUGdrEFxY3ZoUgVQwyOyJCV29iL6X9z2JHF9k7zFrR0zS4mSwq3MyS7f7dvklhhlQbHQXma4OziU8uYEEU0z7goBSm__YafItRtUmIFVcG1H-RwhnoAwzSO0xmE4LQERGansg_8YmNKieMWdIlrfoe4NbDRDHEekQjMYS3fVlNH65YalD7ZfDbOWuaunYkwsiL2K0yZ5SfR5IphMn2GSK3-SEPre9qHnuPej_uusYRVgYS_zjmrY4s4iRExtuM8738qcseqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب حداقل 15 میلیون داشته باشی
💵
اگه نمیدونی تواین‌روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 15 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
https://t.me/+HOIRMsG7xT4wMDM0</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25574" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=YkjTXCXzTeO8YkxLPttAr6SqC1HQPp2o2QLyi6vJQMi_-nVWMPyiZkyS8a9xHMyBO_s0J9PALMTcxbwqoKrUnVeg6d3xQtjyP6u9OmTeGro6730k9Y1aTwnu9Pr7eecU7lrwsptZSlqxQTBs30AXaO9yRu3UviFy9QmKAdT3eXLrbVJ6zrWaITYYygwadBVmFpH-G80PwtI_7ayTj_9sdSX0AKQ6qvnkeZ7iYVoCpuyB2ZLp8RobHD9pl0lUGkgLIGGwTfcM2e3CuRNR4ozWhfHc6sDMYFYlhIAW1lKs_J5TEyG6vKNlbnZXuEcdavFqzGakbDdk6UhKVWzcxjPn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=YkjTXCXzTeO8YkxLPttAr6SqC1HQPp2o2QLyi6vJQMi_-nVWMPyiZkyS8a9xHMyBO_s0J9PALMTcxbwqoKrUnVeg6d3xQtjyP6u9OmTeGro6730k9Y1aTwnu9Pr7eecU7lrwsptZSlqxQTBs30AXaO9yRu3UviFy9QmKAdT3eXLrbVJ6zrWaITYYygwadBVmFpH-G80PwtI_7ayTj_9sdSX0AKQ6qvnkeZ7iYVoCpuyB2ZLp8RobHD9pl0lUGkgLIGGwTfcM2e3CuRNR4ozWhfHc6sDMYFYlhIAW1lKs_J5TEyG6vKNlbnZXuEcdavFqzGakbDdk6UhKVWzcxjPn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVhsukaVcSQNsGATLwC33g7C3Kf0-KH2OlpJMTPq2iCAz6TOIVnrjfdkJraqt-bxvqpjz0Tf7Y_AKDFlkq1V1jZbiGZ2qbaBoNao527RZYf3LEGHK0mQL5gfHhjTv4Tvp40XCN7xtm_EdHuv5v4sBrqp0Nluy6wAKhLT_ck121HsA21ZxQg0f-qkF2YcJ6vCouqAvL8uJ9A5a6e1YAcq6yXxr8gSltQKneSSVtg5fcODISmyLva2gbgz7PobEIatB2Z4-UYEDVkaifu8CRZHEPawUZGyaYAFmmqussHVV7TEvCQmNRWzGHENw52a91eRgjlTbAlmV1tDlGKD9y9liQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjLyIjjz6veIro-rpc0qZw84jk9TvMbv5mNJLG5FprN7nnLzGIwyKhmKJiBTreMdkalsUM5yg2GxfmkRRT8QMEXvI9H78h8K8I0DQ_H7fpp1K8k3ZSFvImfn9emhUAEJYOoUaZe8qDptRV8bWfgrhv8YpF95yc_Z1aMgKTGiSvKUNEpL28_HfKpyVmvVs3PSCJKJNwsHXJtE2abwVh-UMzZ5vCmII33BH52kUZBbCqmFT2U7uhH7BE7zjLZz_DZMAh3JKXHTlmlnIqyShe2Cf_ZiE6Tuw5M6wnENMFM5Pz1-XQ6lkSf53WfI8T5aIe4phCxdyr4QeD-GLQeK9dj1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=OTPRsoNEi2bqA33gejfUlj3FBPTjja-WGxg1-UWl4IGEFq-axD93w2LBWGBP4fEVjfvdSaqk0I5pgnFtbsHxT61ZpUueNKA5UmhsAZ3SMF0jlK6LGxHFLBHoJkOyn6WS-iN3_b5VU6RBUDAxWWsROs2ksH-MRrADbC3aC60RVR2WpB0e1UMmBFqTcXbD6iPF0XHe9QYCUI2r3FweqjvT1pKRg5iJdyP4JSf6zYRt3Nh22mdtkIQv1AmWtYE6XjRM1DpTXENIQm1TSEke3DI8Ea6CXlV3O3hYIGvZrJ5t7tpC2j6PFch-zzYXBi7fI7iWIs26zgrwhgn5mIUyP6ogzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=OTPRsoNEi2bqA33gejfUlj3FBPTjja-WGxg1-UWl4IGEFq-axD93w2LBWGBP4fEVjfvdSaqk0I5pgnFtbsHxT61ZpUueNKA5UmhsAZ3SMF0jlK6LGxHFLBHoJkOyn6WS-iN3_b5VU6RBUDAxWWsROs2ksH-MRrADbC3aC60RVR2WpB0e1UMmBFqTcXbD6iPF0XHe9QYCUI2r3FweqjvT1pKRg5iJdyP4JSf6zYRt3Nh22mdtkIQv1AmWtYE6XjRM1DpTXENIQm1TSEke3DI8Ea6CXlV3O3hYIGvZrJ5t7tpC2j6PFch-zzYXBi7fI7iWIs26zgrwhgn5mIUyP6ogzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adziitXtE_ZmzODzi86Q4_t0o2BkkBKcwInvPVMqauct3F_1t12NbdQ-G4W31HZ0biM4nD6gUDEr01vMr9OdYCAc9k5ddzeWjbSGLcb_YxaGIGGlPcCttiLVxmZspETHwCrROeN5eZMr6CIiaBBeQslmXsQzmPVQ0REgzyQTgi5myaZZWqv9kr5qp19XpZgWC_3uILaRXuf6MHM5ePNvjWhHCQa34-RVDA_bwNin63hj68-mUqeRVF1loGdcCP8EGRvQBA4r91E1S6E-aVi-sY3hVDy_A6Xbdr0zlFxwDFvJe2drlimodwOQULf433jr2m9sFk56mwptvw6XOE_deg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keM91029C7dQ_OEUOozbRJCisNXP8tekdvjumrYWwL2ykO2ZNw6FQzgZ5AxM2Bl1ewmszeD93Bk6cJNXnfODDEZN25lUaYY41EUQm5CvLKK7pe9Y7_dJIxir8nl6mWp5a2r-QNa5oUmoaxdqYUrfnj-4cw-xXMrIE_TfWgEmISEO1wEHet5uyXy5oEbsJR278Vem_4Vrzsm6NqEuIhq-l26lvU1-q2FKwIFg90vlPcQffgsZt8kXbEmcnSzXWf_u8gbUbm6PpDDE-bFvSn6tbf33YnSHg5RTVBV_iWtlrB-VGgch0CeY6WnRwNFV0texanNVol-RnvVFNZRQBBrfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6lU8ebDbaoWhMUFoTPmt5ea4-2cNVGxuCefqDy6YHOmWUMJmy_JCQN48jZYbX15gd8qfrVzOa57rHYZUbKsR08FMI09wFsezfDvmjcqHEk1YLd7kSdfFGJ9JE66oC464ugx12QI1UEjPcMQI2NFUbB5azwWG_Ki3r8Pa6LcC_1NxdEO0sbUiPsWeWDsdBxzyhn0SlhBkTEz1AvCnlVn9ku4uvNesxPQ6lv4ueWv8fobC3m480xcWOV1HvoGmxJlpXjRkLJ2WNR9b2BCj2MwZ4QvycLAZLjPKmCgrTtDx4JICPsrIvT9LUYoD5wKU8_3XC1ljd-Im-MjWs526ls6iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps0M6XXvOycHYJqFqUM0Qno2EdnoilI3_XifFujNKLQO0K_FTzjEWDmrvX_mRJsHEYynn191840eFL8_CabxY3OeBj8xZw5B8qUodXp2EEN3Yt0agVuvLn60ZYZ52X7Ocs4TUAt8ixB2Bvbf9rWBcq0GlmK6CQdefWgDUYY8l-ZZMP4tLcBbun7kB_wlKwAkeTvZS5rRTT2c5_fMiUiHlvLGsa9zOnmtdaRRTOrtQH82JLju0aQwfZKyDRl2kf7vrT07glS0czD_zhLcEvw-BXOXGbfytE7Ah-tvb7K3aW0Q5yANl5MmKB_PS2rSSBQlD0oFoFfXNT3WXAFvhQ3B3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=fqQa_Buz0dpaTw8Y8Uq0zi8HtYCiSqa7r8o5W3GnZwJBkWAB4PJGQYeu0av4gIbWUSiVa_ryzxamhfG_bgBjY85-sZnmPSNFaJ-8SDfsJ0dAzPKH7t4mZlvKzJWX2BdhacBaRqjkstJdyiYv6jYV6072I513FeIbLTdQzKRQUhDUiThifgHJoaUFpfHJzacHcqRkNZ75MY415Ypzf8AIGgl9Em1KwBmuDQ6akDNdg4-64Cb2cgK1-_5xkb0j0QigniJLpmxj4bUq4SW8iQvCxMa-kyxOC1vuJFfxeSLTUD_qovwq34A8ddHxNeBxNdVZnf9ve9LASLlxondH_VSsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=fqQa_Buz0dpaTw8Y8Uq0zi8HtYCiSqa7r8o5W3GnZwJBkWAB4PJGQYeu0av4gIbWUSiVa_ryzxamhfG_bgBjY85-sZnmPSNFaJ-8SDfsJ0dAzPKH7t4mZlvKzJWX2BdhacBaRqjkstJdyiYv6jYV6072I513FeIbLTdQzKRQUhDUiThifgHJoaUFpfHJzacHcqRkNZ75MY415Ypzf8AIGgl9Em1KwBmuDQ6akDNdg4-64Cb2cgK1-_5xkb0j0QigniJLpmxj4bUq4SW8iQvCxMa-kyxOC1vuJFfxeSLTUD_qovwq34A8ddHxNeBxNdVZnf9ve9LASLlxondH_VSsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=cLmVhXfvDaoj0v0LI077kSCszSoMZDA-M3KSgfFi7GsCC1iXDcxZIG0zdbPRnMkQO_h2xneKxx3Ow6MO_bUA1NCa6O4RbLGz5sZObQSAu3z1THN7jwk1xqCY1iNP9rZbzhQ8QqcuZBqivDxEOwHH7cCcm5IEx-k1sSh1cO9AbizpT5yOUTsDCFjODqE6tCg9Ozwl2f5HTlGaQQ2GJ9XOzkaDqwqBc2avosxdw4vGgnd3-J4peolsnfl7Kqp2fyKWDkQTFm_OySsPI1Z1cWTn7PwCyZVBt2ttprG6Q1T-b7TA_cCjR5xE2pNGlSeB2tmggEacnenmtDA9d_QB6duE1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=cLmVhXfvDaoj0v0LI077kSCszSoMZDA-M3KSgfFi7GsCC1iXDcxZIG0zdbPRnMkQO_h2xneKxx3Ow6MO_bUA1NCa6O4RbLGz5sZObQSAu3z1THN7jwk1xqCY1iNP9rZbzhQ8QqcuZBqivDxEOwHH7cCcm5IEx-k1sSh1cO9AbizpT5yOUTsDCFjODqE6tCg9Ozwl2f5HTlGaQQ2GJ9XOzkaDqwqBc2avosxdw4vGgnd3-J4peolsnfl7Kqp2fyKWDkQTFm_OySsPI1Z1cWTn7PwCyZVBt2ttprG6Q1T-b7TA_cCjR5xE2pNGlSeB2tmggEacnenmtDA9d_QB6duE1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=jAqI8u6OqXGFBjn0kVetkhqjUE7aT-ua33DuhhlMqQHdqetyGTLQhE8g2pSB8KBHZYh6h8kWjSH_bGwMvZG_ARhfitYro-byXwkuMs5FBnfL32jr32JlXok0IxxDWFcMdy8ibzE7m0bQboKh5V2SsTkmN2YGPXy2x0iFKzmNbmX5e-N9ZERs3BIjKmugkOpSQeSVsz1Qes-ng789tmM-2zjKDzyMBewz_eJm0fLQbAuPFGJciDcRCQuCOMaSNYsZSp8daCPFnge8JhKJiy6PA0fgcpl07BMWfLfvX9H2Dwmqz1bx1_X-p30kM0ebDhI9YHqj86-CB9q8Le1rYlC3ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ff28adc2.mp4?token=jAqI8u6OqXGFBjn0kVetkhqjUE7aT-ua33DuhhlMqQHdqetyGTLQhE8g2pSB8KBHZYh6h8kWjSH_bGwMvZG_ARhfitYro-byXwkuMs5FBnfL32jr32JlXok0IxxDWFcMdy8ibzE7m0bQboKh5V2SsTkmN2YGPXy2x0iFKzmNbmX5e-N9ZERs3BIjKmugkOpSQeSVsz1Qes-ng789tmM-2zjKDzyMBewz_eJm0fLQbAuPFGJciDcRCQuCOMaSNYsZSp8daCPFnge8JhKJiy6PA0fgcpl07BMWfLfvX9H2Dwmqz1bx1_X-p30kM0ebDhI9YHqj86-CB9q8Le1rYlC3ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25563" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH6SjlaDtcUoBqKQFygJSw6GNjG5424nrmKT8jvb6a_A-Y9CfJi1rnB51SSxQwV6puHP7vt0K82aJxybLJ1WCMM8JsS82cDiv2jUt0Hg8OCRzMG7NAn8fqXvah3kTIIDtArdbxTNQS9hovN9G30Rca58j9oPSrcDTHioukF_uNPTkQGZGnRMJE-zmKPchy6c0Vx6aokKnXqBWWjrIDbS8T97k4yRsL1UkPrzCoVQIjiRXb4nhWqDuOFtnYB_OSJJIUw1CBx242l_18FHWGahPnDw07yWm-IzkJ9vGZDO4vS_XKp_LWvb_1zdY1xleUMu5ZWKkyJvrWywudN0gS8mDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25559" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9ZSRq26ECdXQEuVA_jDi1nfWSLG5OUxaDCxvSGGS6MNqYp7Mifzy5Fr4MRjDiBtWzC4H_XV6mcgzph6zEjfr2Q70qnll1xJu9BSxv8sHIFQ74LHMgzGQWbQEKlj8xCvXRZdPAIAtXzEVzVromOLgQhQsg8ag66IDvsoVsq22HI2tfS2wNaIcWH8qmWbI6oJjbnRlGTz-pOqdHLvN8jJ6bEMeOS_Ad3DU85FIpdZdfU9Ur2nnf1ye0rti6QvtailMT9htTEafYTelZ4Qh6aYIo-uQLEEKll9FBx1mz9dMomwlRPLeeCiignhCNOwKKBj7RkH62Mrmipsyat30yD2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کسری طاهری مهاجم جدید پرسپولیس: ظرف 24 ساعت‌اخیرکارهای‌رضایت‌نامه‌ام از باشگاه روبین کازان انجام شد و فردا باشگاه از من رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25557" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkA_7Gz71oAkm4eBx8fjVqPhtg6BDKyR5rL6JOS3wZuUiyFcZrgz3tSditFnIpgKxXTqQbaxdHmDBbpDRXI55EFYtmt8OnVRuUFMqw_7J8cKsaKTG4NH1J39CCh34kIWjpsa3pid2eI1kM1ZZ1nOgrUGkBX60nrrTjzdTlqWAjvFf6L94SKRiPEPZJ576z2bOivzv4Qg_3SYjpVjsuogku_BiC8ILIuXykgzZhrXJM3KFXh7A6uzLwqSQfQz9Ce4EFCWBDsdROpYDmGOmJVtMk5PSOUflQznPtaqhMuKxUtki0B_XFa7XQqrAdaKbOvJtMyzy2Eid_lZG72v80ZaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌عجیب‌ زیکو بازیکن تیم‌ملی‌مصر:
لیونل مسی، بزرگترین بازیکن تاریخ فوتبال است، اما بعد از کریستیانو رونالدو و راستش را بخواهید، حتی حس نکردم که لیونل مسی در زمین حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25556" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=DPH6ILccpU3B1co-3Xyrm9YZZUjFTIxAt1wFdmhEM9Jw5Dytaa4VJ-7BiYfaPXeuaqh0gC6zdD1gXCQtgKwxsNrPACH27U72qd0yF7rFU6svH1eIuZ4maQlAGcNvbNtcDgHW6YmqL2_xsZDL3HmUGYZeQ5KYxhhbZcXe-x2y3hUGIvuyvhNPV04ElGnzl7ogxp7lhogP55FICN9V3mCEFnrvwEFzHme5cdwJvnP7Rw6Q1bHD_rGxidRZZtpzc-wfwijoNe8PznZYgdiPIqqBuYJ0N49YJRc0HQ0KPc9zeStIKOyak02GqNs8Ncx_L2ZbLxeVusPDFZNFTYjM5p4Zmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a89f9e96.mp4?token=DPH6ILccpU3B1co-3Xyrm9YZZUjFTIxAt1wFdmhEM9Jw5Dytaa4VJ-7BiYfaPXeuaqh0gC6zdD1gXCQtgKwxsNrPACH27U72qd0yF7rFU6svH1eIuZ4maQlAGcNvbNtcDgHW6YmqL2_xsZDL3HmUGYZeQ5KYxhhbZcXe-x2y3hUGIvuyvhNPV04ElGnzl7ogxp7lhogP55FICN9V3mCEFnrvwEFzHme5cdwJvnP7Rw6Q1bHD_rGxidRZZtpzc-wfwijoNe8PznZYgdiPIqqBuYJ0N49YJRc0HQ0KPc9zeStIKOyak02GqNs8Ncx_L2ZbLxeVusPDFZNFTYjM5p4Zmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب فیروز کریمی کارشناس شبکه جم اسپورت درباره صحبت‌های طارمی در رحتکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25555" target="_blank">📅 23:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-ZWLFwzpWUfEw9ggRfIrCr6vbApm1vHohdRaW2psKGd6MjtuZ5i_6FSKZ4PN2jUTwJO-MTyz17kAqdV-ZCCy8BA1XeGcIUE_3WEkotpZcFWQpvybaomi26zSq4rYl7n99LmZQLzfdOM0gqdGFXis3RXgB7szerYdlG_qtCGTbtXEkGAb6t7p3rAM9UCvyzdI3ywAKSniyrTYKON9m7RxIGocLOUix1HYRkszAptMZo_84yz1ZQhSR5Q8v9UZfIisjZ6gMD_1ph737UhV7_R8WaPVhsK2j3UxDD7RVJCFd1LOM6KFy91bwM2weE-uwFJ4-xGDByczkxovGWKowwxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
رنکینگ‌شش‌تیمی‌که تیم‌ملی آرژانتین در این‌ دوره از رقابت‌های جام‌جهانی‌باهاشون بازی کرده؛ به هیچ‌عنوان‌نمیخوام‌ارزش تلاش و کاری که آرژانتینیا کردن رو پایین بیارم، اماازحق نگذریم آرژانتین اصلا مسیر سختی روطی‌نکرد و سخت‌ترین حریفش، تیم ۱۹ام رنکینگ فیفا بود!…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25554" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fShesMEQeLvc4hCL2h-KYBTfSpcPClE29BSZgnBnNAfhBL87dZi4C7umcUqVDmngQVEa6HUBe3aldno23oNjtyl1zYtljeeqxz1QAoQI6816WJYGo6O4HSQVLERvy4mtb8afe35qNWJ4CVaUoGj4UvpKP4Tujr_KJgBIG-YBz-x3iIQpsfWwQieXlZk_QZWUJMv7SRzkIKHYxU2pOuIJDm21wAPZioK3PuLaL3SEL1_k6px5bS35uzQlZwJm94RXgf7gTtgATvukLRLGQroozWvkJrS4iD24X8ZY4-7ZcTGdhLdmbcfGly69EaFDSaCmtiTtO66QaFwDlf_zjof8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEQgr6ijLqq4Yad2vpi26jZ2sZQdNgx-wC-GqhWeR53DWdtQgzko8dF16bjgFM8IJKOEI8HHn20C595aD0Bfz_yc8mFuLBCwYy3IPDZ6LlvY4hWAiUsjkRykvARiWnrmdnMUWQXnLgsoq18vNTK2vxZPumfvNQdJ09Fh8qfAlvjHE5EuFmEDf4xHP0B8nDuiFMUSMzFZ3CmusbH1LpT2RGT0J5y0DdD8OvAUYtbzlpX_tCJ2xLENnYWccVi9czq16Y-ObC2GICd4udwAxaMDamotax5CmRfGNJKb226YYb_BK5q4WFmaxaRPVEh-gJmTQAajrLWcXlG88horp_8Y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD3PEBONk_SoR5u2OJW-j4PAswDLxM2ObGwGcBZFBh9zwtJbLfq_A_u3Zqm-q0SwIuG2PW7WE-qCLLAXoXxr1Oxf6o8FYjBZaoE8MX0XN2YASnES304zueB9CNNM1YaPZNbqBOZ65tyVrXANTplfdU5xbETZKvxVAIy6q0yClLvqDlVYCaShjbaHTQ82jiB4wM-ZO90P0C5cih4-RnTUCYPm1s-i-wi2GNJfbCkVeXJU2rBzbYG79bMZHSt-am6sCVxea2FApWGzyWREhV2OuJov6ZvxKiwpUCrOarToF6eyk1GEnxVHl_KsbFPnzCZBXTs44NpuzZ0UHtylNyPcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZDFCHihPE3cMImlpzZ3OnQmoJZrPTgyMDXSEPhO-Fb9R4nRBr0YzQCGiYHLnI31a2tF8HIk4l5Rchc8WSmvhJT91Gl5GZ1AiSnqgxyS_3nMxBNotCwAKmjNG6R0PFlpC1OFqKZkUkNvUv_IkJaIJpK5BX_JJphMuSXgPy5JkGGaEL-X1GpyiOQTDZ8ufk66rEltGf8G0JEbMaa110UPCzwHWV2k0bHM30F-ORyjKu2PCbMj-ZyKgRXPy9VjqLZe0hitgGYjDvBhZ0boIjuCpaSUCvCWWT2hbi56VdJU3uLGD8-ONooStZww5UBpg3Sd6ium-YzuyVE3GoPSzB2e-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx9nyWGjNW8jtsxIxz3pCF2docCQB2ou6gXhdpYwV65KwfRgdRe6f14e9JCsjW7UvXj3I34-raEUuvb7yzXvHnF9eGXd4xiF9OLCCuQyY_xwj5idTrQeVTnQ7nhhYtlb2pipKJVKORDr5M4TQzQ8-N0sTkfNd2qn3piU3G5exLRNgkLuLECQqLt-dsgC0qsru9cCAgeD-OOhCPPh7OUkT2sWL_b29JP-ifCGcnzcUn3LXN3Pn6MZcD2wSnvQKsv-UUDulA0gi7IWQ23dlAqMLUDxZpkYFncOzL7mTpr_CHGt5efRnsvqA90S5kLQc7Nuy-SuJuRfqCSrTsKPeDf7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL6v4ZD2Z72fyhwdrxP55T-8f0UAnmszRTk-lD-5pzThWqEbPYOBsZIx1ES6-ENfldhwWsKYOK0qMmJtzCAa1eEGuboqMpqGfZ9yl0g4nRE7lScJjXCu11ygRbVZc_Xu5h-YhrhbKtWbYtWmH378hydKJF_PCys2Iht6TtBahWOoaLKTT9n-Mrp_qEBApEcadEIv_nIS0GryPyPppvglVT4baKivx5qxI7yBbQqF0ZMAE1Qz6XwR3xTkeApq5hKZUysaJvxcMF4C2aEcfn4XO5h31RiwHU4auzTqgax61lttSrQwPTaDAOa0E9BIUMUQgdw-g2-KQzLQRqMCArBQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRS1kl-dr2BDGI8lJ1aG3np368j111tb7X7Gt89gPr5ER-NKO9yY4a-04FZIQUsHM6QnfO0g_a4-0QJzG1T2lHRnL2-NgiZIL3NosD40DOGllk1WB5LMHLwhx0jr5oZLLUwm6TyuuZQpTXVqIv6L3wHCFcHImdGh-357IOndAX8oh-2OH-e-kx1gHLG2350kz99NcgEj2pFK7-XWh5kVYtYMT58yea0V6HYPxY88cy72_4R5re42IIlOGg9M0HaROrRTsfLpECMWyNpQruBSdH9EpSwnVpBiBsMWvjhTgPAITWciPKNliCrcWAs1U_ts8Sk7ws6Nsm6jZBHKb_f_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNKTDKz5qPHBNNXyltUBrbWF4QCVn_i5Z49PEDSzLsO5DTAB_4rRMWH9jC_1GYZgQ__wRWGFGS2KbND-2fpH-dGU7SGe3BE2VjPU4PWBc3h7Ij35bnw3V0Ug3Ev2wXQ6QIQ65z9QDvuceLWJZCN60WAqewkoSA5tgdCqQWynK7e1RpoyN_vgDhGiT2kPBDVWOe9p8I5lFtlbzNSkDYs6GXiJrpSi7njXt5yAsNFloKRIiXmI5NI3ACNtovo4KviZx0fx4eaoo6xwNb7bnMqe3AfrMYZaC9weR6M_AbiBjeiOAWhsI5VngPkbbO4vd2gM3Hbpy9jDS5Hyt5ptv1ZB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FgevWBpPKCQs7KXt_AeiIDYVxgz3PdhPeIM440RjfaHrkfrLLkFa1IpUGRhwh7XZzy3BzmcaQtpQVwdCuzaH4bYiQM1e_w58WF6KeCbMRowz8u0QK39_Le3UOTb_ybrnu6OKjqQWTfydwGpKlGYff9SxH3L9Z1uynaKb7jibq5n4Sz7PYCNg4KJqNK36I5VCdKPcCkC5tprOmjf1kAkZpXMWeimiNhCdRNTuIYNu30TsY6TkN93XaT86gS3I35HEbpxYp2EvyCPmGsJPPCIMuVniuqUNMGIsWMKoTlmjLLMfgFKCjimH7PqT2hgDvOyCfm1WeHT2Mu4Li0yu8OALbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FgevWBpPKCQs7KXt_AeiIDYVxgz3PdhPeIM440RjfaHrkfrLLkFa1IpUGRhwh7XZzy3BzmcaQtpQVwdCuzaH4bYiQM1e_w58WF6KeCbMRowz8u0QK39_Le3UOTb_ybrnu6OKjqQWTfydwGpKlGYff9SxH3L9Z1uynaKb7jibq5n4Sz7PYCNg4KJqNK36I5VCdKPcCkC5tprOmjf1kAkZpXMWeimiNhCdRNTuIYNu30TsY6TkN93XaT86gS3I35HEbpxYp2EvyCPmGsJPPCIMuVniuqUNMGIsWMKoTlmjLLMfgFKCjimH7PqT2hgDvOyCfm1WeHT2Mu4Li0yu8OALbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXeQBIo-xJpiFjocofJklLZCIfvExM0SZ6KAOccsRUl9WIo__muzF-udq5iewX9Lu8wMAIhpQxb76UHJWjI6mOjtZbnZy5xU4cL6NhRvcZZ3FH5_ZBWlx5lPv3F4J9CkNgpEpnpTzukPBZ_ZlyxKr7mhKLEtYoozi-SV2uHiBaUpx-gbmEZpocBSi-UOK2DI6aWzRtfL0bwwiSAlbnPXK4nLGTcd2jiGKPNqhJgkmzi0GmG2KgelbnNj2nKDfhyllpwK5dQK7IL-velC8IyeTXgrxCAq35HhvTo-nJ8Zm1dNe7jbNWtzsaoBPh7q3azZyjx246pMdc41_nFmrWZNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOFol5jMAtiGShh9FxrGSB8qIrpACbFCD07omuR0-4oqUh-ylY_u8kK6rOvXmTfrc-DykEVRl3YIDm476NMqHM5zntvDlRL6ApKgXQS_BxLHdXXmE3EDLQv6SL9WegAHPBwaMgrlJtODwkvt95ZSTS5SemvpsdTLi7f4Ze_yLrQFSsZx3UV4dGjaOHgdnGEHH0go1KKJ7Xs_PtlHcyPWTypiwdDiHkVjvm60nQFX37HKEcz7pAyFTC6V_ulPL75GhqqTFZ40eXzHn_u19CbVF3YeGxsTellkpr8c9LI0ALXTp8ZYcxWBWO6i5RRFwutPLAfHyyt2iRG4XalfR8-3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=YU6udlgoPTQQDFYJCnVG_0KNfuHUPCjOO-uva4kiu39IlvV3cj7u0LaGewNvcKOYYpOA02InmIih5VHoLi1bV-ksMxPqsryddlwtWZEAAwxllfjTSr1g_rlPelAv5BpXIUUpDsa_eW8gPtydGdckx85Wx8g8PUiWhtewnGVturilk5E47TzlyydB7g5eBExCkQ8mNWzODnlzo1-E9tdJksVBp3saJQLHFYK0rPx0KnaAm23deJFVPSOMx_IkuLWHS6Uc27FTgWIuJaSSnXGBrgnL2Ws6z4k3AtBS0VCMjwI9sbaSc1arj6qey1Gtv2PPX_YPAJmOudUEt_dg02-PIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=YU6udlgoPTQQDFYJCnVG_0KNfuHUPCjOO-uva4kiu39IlvV3cj7u0LaGewNvcKOYYpOA02InmIih5VHoLi1bV-ksMxPqsryddlwtWZEAAwxllfjTSr1g_rlPelAv5BpXIUUpDsa_eW8gPtydGdckx85Wx8g8PUiWhtewnGVturilk5E47TzlyydB7g5eBExCkQ8mNWzODnlzo1-E9tdJksVBp3saJQLHFYK0rPx0KnaAm23deJFVPSOMx_IkuLWHS6Uc27FTgWIuJaSSnXGBrgnL2Ws6z4k3AtBS0VCMjwI9sbaSc1arj6qey1Gtv2PPX_YPAJmOudUEt_dg02-PIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_xfxunfedA1K0d1wLqUXKhVwBTcZGbEapul9DfhyqQqf-H9PykeZRuJNA1ARNNtIWU-rsZ4YnHMWjbX_QhrbUhNDfonWPcLBW18ysi1hDBc7tLqSNUxvBPxoIXJEYhy8VvLDXz8GCNW0m5wDyWd2Oa0APPSTopckW4MoLNYgJtF7gsK7pmr8Ja6Srloas1rJRHyiFk8VhSiSBWT4i1F8_6UH6OYxfW7cA11WZGR9ewHOg8aXFClD6kOv4lMSHcaQIV1lZdwChbbgQddQF-R42sAvTxV3UTB66Na7RHqxHc8d5UCN7l_o-wyD_Yrf1R_37epvQF0PLKeZ1r5dNcm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPiXC0VKeZOEv96mgh_WZLc6SZmWL7pRlAjiyJDz5wk0rJcbT1AQ8jUf-5KAMLg5lIvA_OY8vllp3JgbeBtTmiP-HBJxOBQRSqJ-w3YHM1CnjrhR-W-jTEPbga58WVc08t9xKo3EVl1GeZksPw27fv043ax9zRIRkrKCokxxKLZOoF0ohU_zGlCepkDvHJLrYzcIpOcKAbg3eG9Lfgjil-2b8cRbNCZzbiuKKSmQ43G6hnj8T5QMKzcrKOZC_2hATqmcP5etjG5C7vFLSEdLLkxEEKPB7BXIoEZru77LdcooFVfn_mkNdOrNqVwicViMr7xYDlQnpe9onbLpJwdRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvlaJ3syiYHMlPpD2AZ6eovMZ2MCwcgnurbmXum-_NyiQvaYn3AiZdyDbUYgzsnpfVbQjl7XYlwKImoCJeLOxxu_n02VGXStTUA_3FqDtd9G8bYL6DJFqFVE7ielQ5VMHjP2awNlrxNe-5bUk4288qijFMjfQBHIn-4afhlUaR_yuugV5e21pDP55lkQc5FweO1Whv0Csl95UeGtZA8xVs2aETHbUNeMupq3VvddaMq702oA4nonTFrvmmSLzggNOU41S3DZhNVPdhczOHT68b8zI4Xtr0mkBDDR1szdcKCxPsWwM33JBsacYDYet3FykRHvw89Bg8pG5WsJ5tE18w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=OhGaS15HvkY24xXLBJcJZWwbwoFNFlQd0sHyYT-mRGa9CKlFrIJDKX3iMi7AAL4e8o3EWkp4Tzd-nTtSknR-ZBIdSjy55qo2ZBJ9o5eAaxCOonO60iama2PGQygXO2SgC9LR4rqIYJrMmSVFm34_fIO75mVw7hj_yIWUYYOhC3B2n_je7e0siJ6-URLDZL7r0i2euc4xgtwgnjbCg_3bBgubz0ARiYPULq4ugyPSN-yGD9eq5lOFGQcS-RI7IMtqRuaiqPE3cCEwVvnc8SnriQl__nxoV4SDH5ZrqzAxhgKhuMp3ckZJ-2-1vxNwc1C3ErOLoXRGxFbOyotRTgQQwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=OhGaS15HvkY24xXLBJcJZWwbwoFNFlQd0sHyYT-mRGa9CKlFrIJDKX3iMi7AAL4e8o3EWkp4Tzd-nTtSknR-ZBIdSjy55qo2ZBJ9o5eAaxCOonO60iama2PGQygXO2SgC9LR4rqIYJrMmSVFm34_fIO75mVw7hj_yIWUYYOhC3B2n_je7e0siJ6-URLDZL7r0i2euc4xgtwgnjbCg_3bBgubz0ARiYPULq4ugyPSN-yGD9eq5lOFGQcS-RI7IMtqRuaiqPE3cCEwVvnc8SnriQl__nxoV4SDH5ZrqzAxhgKhuMp3ckZJ-2-1vxNwc1C3ErOLoXRGxFbOyotRTgQQwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLXWQavXKVl7PE0SAOLgNJyOnXd0o6VJsel8ns6wE5rcxfp_6AtS6TYxFX7xETBIXZ47PxxCADGnxkxa-3I81vu3arL4pNQ4VLatDf0yxtjfG0dLrqxh29xoDU2Ptodn9MGWsLrHbzfu3bMFRurwqaEj07G9Eb_elyDX772F2YhJygDVlH8850EP1eh1pNRuNZnN7g5nSiyamAaea856nhXDRhJkoJCexPOGN76Qg_pbaqomiTyKGfdyMNH8BzdbZUHt2frLr3_UWqwNk8QAfA9UwClmuNNNcWSJcEQaORAA_j07b2lQ-J-CNrhPo7R3Z1apUDI1eb4TQn20J8-RQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orWxgUrX7jAiJJemAFhZ-9oW04Au5AOmhwqx5oKwLHJ4LDFI55leGIKH58AZ4GM1LSYL-bw3i8EmwLUFaAPFyVIoVTNbylY-RqXaowFnmp_VtA7zHLk_2wtsfOxg5v-KNGdeVCThG8PtBsxwnW9W6QIZpHo8g9FQZ5HRDMHfuHswvgzHHpPi6ZQPiwMq4cqVu5yHsJWg9cppxg6KJ7gu1gweFhbw2QeQPPSYwzazWOk5qCOIniEan8scZ-UJ5lqqr6HJdbpzCbJ7kYGAeFbcFJ0nqnl8Ckr5fesdSCL7kYBSXblT7dQdmQPTTt2LbqSw0fKpY7KSxBfgMzpDZO4rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sww-TjmPSy4xrZ8Y1NX3B7Qdf9qkZeNuGs5FDW7cNqw3K5YfxLVeOti9Ga85bMTsrlTHS7EeSjwO8sAUP6lELFFZrYv1lbQb5KEq4Um7jJM1nrQQKCcs21-NqQZVB2tXm3QIY7dvkw2fNqkY_3k7f7Usa1hCKDIgiiI-NlQDVBv9Sxyx38Ed6aJhvB9Ql972j3vdw6rmHEJ0CSMgfg24dFC4VAc1tYw9FHvY4EFO4v5yv5YTF-wfj-Z_y7Tfj3QrPx5d-3GCaXIxV0EXBKIf_aNiF6HgZ-jJbjHEpIakydZTVM370vQllDwpTT5Bslzrf0Ew2TOiKoQXnehSCCIeXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=BplWkzvtVUIbKKmca3UPHtMMWnqFYQP3wGBHU64ldwqIkdGzHsh_G6mELDZXjlm8rwPZ5BR46hNJOCZYR_ocYjIoRX4ynxtLaGP8Km2VKSmJpZbbAH4E-XAvP1v9n5U2p2TNg5Yj9dS1RBA9FHtbhVSMlXBAV8eSdrS8dc5F-kY_vNOr6ni65CWvrG2JUg-rdEXHj8ATG6Yri0h9-roPfV0rNUzzj-HgX0tIAIWPE08Is889pyhD7I3aVpU-e0b2JqX1jteGUmy-arf-4iOkdG7hM7Nbfl0ZjSpr8pY54hPuB6pcSVsvKmni9iw59inV5utqoBEGvlMxGrBh4JVTjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=BplWkzvtVUIbKKmca3UPHtMMWnqFYQP3wGBHU64ldwqIkdGzHsh_G6mELDZXjlm8rwPZ5BR46hNJOCZYR_ocYjIoRX4ynxtLaGP8Km2VKSmJpZbbAH4E-XAvP1v9n5U2p2TNg5Yj9dS1RBA9FHtbhVSMlXBAV8eSdrS8dc5F-kY_vNOr6ni65CWvrG2JUg-rdEXHj8ATG6Yri0h9-roPfV0rNUzzj-HgX0tIAIWPE08Is889pyhD7I3aVpU-e0b2JqX1jteGUmy-arf-4iOkdG7hM7Nbfl0ZjSpr8pY54hPuB6pcSVsvKmni9iw59inV5utqoBEGvlMxGrBh4JVTjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=mxNarR3-_3jNNF-lHKJYQ39wJXsdKvLsicVzjXg8_qOf_dNG4ejuve5T5wPOUc3GNrjK-dGkvv6Y-d7uWC5t5Mj6itB_5lQp0OlfCKJogS51gzwqjqTCnypUE4jQ3R6NeDuZgsuy3zfV95fGBZMfjluYAF-Sk7Pwq31VzRfMTcQT74VwQ4iZsnd8jsSGX60vV_iskIvIFob1EMSsBpNAzbABymrxJtTbi8h6bLFmqb5LH4QuJhFvbXXj06vc4tuajt8O5tjLWsu7F5jGi-6FtKK4mRSGRgc53S0c-7NgR_Vh7jnT_0yJDIjqxwnHoGsrN7ZFrQw1ohprr5C9mhYbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=mxNarR3-_3jNNF-lHKJYQ39wJXsdKvLsicVzjXg8_qOf_dNG4ejuve5T5wPOUc3GNrjK-dGkvv6Y-d7uWC5t5Mj6itB_5lQp0OlfCKJogS51gzwqjqTCnypUE4jQ3R6NeDuZgsuy3zfV95fGBZMfjluYAF-Sk7Pwq31VzRfMTcQT74VwQ4iZsnd8jsSGX60vV_iskIvIFob1EMSsBpNAzbABymrxJtTbi8h6bLFmqb5LH4QuJhFvbXXj06vc4tuajt8O5tjLWsu7F5jGi-6FtKK4mRSGRgc53S0c-7NgR_Vh7jnT_0yJDIjqxwnHoGsrN7ZFrQw1ohprr5C9mhYbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=TZknP5QFKjBTY93m3qsoVutVAVqO7x8xnmkaxaaE8ik7RmUdGmHIIc_s1sA5mfep7nvZ4iQ93JJNpYj_IskBIOMNHxEtgJK7v9k2ltpL2F-CJYulxOROk0X1WAhH5GMV1h8u4Pxb9mrJDZ3P7BWVDEML0LwdcO2drxsflmDfAps_MLRf4T8nFaPwweit50bnwCw9OyIqdRPFyMh1WmFmcDZlNBp8c4GlztVVVQxRyqOkKt3MEE-UQ4jdkoJyRCCn-d7y60ZQ5PfLmlvnHfeag0X2ReQK8o2CXr-gI9Ir1qm-tn_6dHGr2thgyzdZHmCh3aHEPhneyT8kpHVOC64GjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=TZknP5QFKjBTY93m3qsoVutVAVqO7x8xnmkaxaaE8ik7RmUdGmHIIc_s1sA5mfep7nvZ4iQ93JJNpYj_IskBIOMNHxEtgJK7v9k2ltpL2F-CJYulxOROk0X1WAhH5GMV1h8u4Pxb9mrJDZ3P7BWVDEML0LwdcO2drxsflmDfAps_MLRf4T8nFaPwweit50bnwCw9OyIqdRPFyMh1WmFmcDZlNBp8c4GlztVVVQxRyqOkKt3MEE-UQ4jdkoJyRCCn-d7y60ZQ5PfLmlvnHfeag0X2ReQK8o2CXr-gI9Ir1qm-tn_6dHGr2thgyzdZHmCh3aHEPhneyT8kpHVOC64GjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvRaWjCH4X7QO2761lgmQrWAKpwTJzjrCWVf1a0PLauH_DWfGeDQPucOQakXm8Ar48L3tJbsgqWILy6UNB8wNHj4mSRiUc3BcvHQfzBIvKLn_XBsIVuSgZWJV-R2Ol5IMg9uLpS1wBteSUQsIi4EqCFZNHtUe2ptHMxaq6vPU32RkDonwgMQ1yX1AfrC8jbjd0LDTZKjzkNsSqFvl-lwGBWYRBa8F_iJLPa2WR0zOMRc9y6sYOhP_Zh6r1sZuFnS00RqAYd5BzUvix9cSCy9_t9qmyiiGnr3o8XQ2LYI6WZ3M3qrAca7aZSJvMq9_FlqWgc_uApWfPfyqornQnFJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md2Bp51H0oSAad37X0Is-QT6e7hzbFTG6J15n9xofjOIZI0VBNeWO6EHEuBN5fiKPkuhdz3ltlY88MuY3gQbb2rpWa3WonoyEUSQBnllL-PLuPRDWaulN_tiLJCDkaYa7AboXXfrpLGKYzeLm-7rKz9FR7XNR73l0yz6yVoxYjxO2j9SUD0lt_uVNUSc7El8JbCtB5yiIAozxv_B-2a9LKLFes7Dtb61xOd4XGwVaJmHdzTMRKaFrXwGmEI4m8VdFkGVKplVEydsYbCo8lSHgYwUOgt6vH_sF4Qg6x1UMoKrrkMJ1PNNrsrbA7PlK3fU8KcfvlEw-TdcLSAlflmBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8ky1JJzkH0XFtVNfvWdrnTvjlO2FiIZ8NClWGg4K1nygKFQt7Ck-sAg7QTS2ABgJtWPfHoxhgncLgp-eJgsbXyeCZNxIYxXm1fUZSAghwryVF55G6iC7u8D_PGFygv5hYOgWHwOOHSF7Lv643NiICkztCHfQCXbQJOP7KHBT5eOYNiLHlTahKrngRFXMyRzjl7ykQF1iYJ_XjvNVqHXsXOa53Ji_oBuoTpfBwcntyVr6NJeZHRJG_M4eDzfifxVFlzwRcnKywzaBHYh1suJsb6l10FpZVhMN-3CCNS8Z41GLwgPqzMehqIfqPk7Yq2C92CueFmOs33dsFQK-sdp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3jE49PuMFasGVcL3AYoe-Pxujrwci9u0_daOIaNEFYpxdWJGuSQH7R1oWR2h5fZl3xBMO-sdENaB7S3E7gm-kMa9dpNpCouCep_5hNQmKafv2BVrsWD4Br48xKgg0Rm12JX-KsaWdm20ra7DcBxbpoGCMX6FP-SB4wuFB4kZ8vcml0Sz5pkO-Sm-pOQ--sXqpy3PGBw-Lo5IIawQM3Mw814j0gLCHMLAkOIg5sVaY6zZtGaOyEsemhkhWcyscpLKx9pWq0Zloal7d1g2k-PPJ_TukzhSXng_EK3v0MXO8-SmoFBaNWcjl1lcnpShleM-_XpoM1dsl3zrDyKWBzayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=lLoK-5X8N0GHnWISZeVz1MAh0GEl6C88tn94cKJ5lDqLz6Locgy9khQMKsvAdVXhpLvm4f0GvNWUqWMvK68NZk_ij54u5frkEHMLRcm_Iox-BNtSyMijfT_tCxcmJWz5F9dc6rTpS1Retslsg1mL9qvGYh45jNcYLf0yL8ko5FJyoC9tdXaRMb8GrRPX0skdqF7pMXAuV4merFFiFQZg6YLho1QrR-7rdzDV97zfoWcPKjxfy89W_EP_B9rslkgH1xCqi92LAwdzckJqHqeKImvSj7o1A9Qqj3QttEy4xDadY3ihpxVLNkx-VMHx9S3-6B2ECEooyaWbGIjqSMGAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=lLoK-5X8N0GHnWISZeVz1MAh0GEl6C88tn94cKJ5lDqLz6Locgy9khQMKsvAdVXhpLvm4f0GvNWUqWMvK68NZk_ij54u5frkEHMLRcm_Iox-BNtSyMijfT_tCxcmJWz5F9dc6rTpS1Retslsg1mL9qvGYh45jNcYLf0yL8ko5FJyoC9tdXaRMb8GrRPX0skdqF7pMXAuV4merFFiFQZg6YLho1QrR-7rdzDV97zfoWcPKjxfy89W_EP_B9rslkgH1xCqi92LAwdzckJqHqeKImvSj7o1A9Qqj3QttEy4xDadY3ihpxVLNkx-VMHx9S3-6B2ECEooyaWbGIjqSMGAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Nd-m_YCuXQuFvG5Kj3w3QF2ekLknELC_QhhF4ecpqV4UujT23dGARTIFPfp6V4ZIAPkMmVM__qBQt9oE4vKHi3y3waetyAvLM8x9FsF6mY5OtDPYxDam7gY2QMe8Hw1WIb4dGd9FqGKx5BMt8MR3vF5nQiLZSKytB9bNZOTIHgAHGi6i_dPRaLvNzdoOkfwJ1RqaFummJv_hzcx1zhbkqHnxlmNFRsl4XOza2-YnsfVVqRTgkdfexU9l3GVqfVHxCGCss9dsVFszW4LTzI-dOtlHSykU1ukmsVuDF8Aw5mZizIBHLq6Q0kESE_w1ZifoA5lSXJqiPXrMsRGGfqprAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Nd-m_YCuXQuFvG5Kj3w3QF2ekLknELC_QhhF4ecpqV4UujT23dGARTIFPfp6V4ZIAPkMmVM__qBQt9oE4vKHi3y3waetyAvLM8x9FsF6mY5OtDPYxDam7gY2QMe8Hw1WIb4dGd9FqGKx5BMt8MR3vF5nQiLZSKytB9bNZOTIHgAHGi6i_dPRaLvNzdoOkfwJ1RqaFummJv_hzcx1zhbkqHnxlmNFRsl4XOza2-YnsfVVqRTgkdfexU9l3GVqfVHxCGCss9dsVFszW4LTzI-dOtlHSykU1ukmsVuDF8Aw5mZizIBHLq6Q0kESE_w1ZifoA5lSXJqiPXrMsRGGfqprAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=vVycKhDPW8IoSOg-UtAtDp-CFozmt2UHzB0VzaZIh89PiGaNFK-pe3VYqyupY3ZZ1UDuzPpgWa20h0DaePjIpVkVue3p9ZGHh_55CBf1oedTavVYtPQOpjdWR9awC68qCENllAUWAV9QVZ4zU7_jWgrQKdJ0FajK-M2IpKR0ttacLIaSTKDiBlhp9YtZi-6M2lbWkbFXGMqjCOjIftYgQLMrwRL0Hb8uDn1Ni_HPCcMvplci9e1aMrT6929LoxyXWJPPMNQHFlXa9DMQzu7vMrnIwgpLzKo2nh0hGO1noQIPZaW0qU8QNAfDlguc3BPjBLmCk6iVyjTXZNIVQGBpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=vVycKhDPW8IoSOg-UtAtDp-CFozmt2UHzB0VzaZIh89PiGaNFK-pe3VYqyupY3ZZ1UDuzPpgWa20h0DaePjIpVkVue3p9ZGHh_55CBf1oedTavVYtPQOpjdWR9awC68qCENllAUWAV9QVZ4zU7_jWgrQKdJ0FajK-M2IpKR0ttacLIaSTKDiBlhp9YtZi-6M2lbWkbFXGMqjCOjIftYgQLMrwRL0Hb8uDn1Ni_HPCcMvplci9e1aMrT6929LoxyXWJPPMNQHFlXa9DMQzu7vMrnIwgpLzKo2nh0hGO1noQIPZaW0qU8QNAfDlguc3BPjBLmCk6iVyjTXZNIVQGBpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdC2s8hvjkiTi9HFx0GAClaN9Mp2wRJTq5F5W_rPYIyq2gZjGK1ke_iO5DRUgaHkwyodRVyEiNklocQ89eWZCsE7hdLmKezGQA5dQ4Z1rfTEWgXreoGNspJ6M1v9XX_20e3BLb1JGb_5gFuSBIneZRCRESOMNvX-7mSFv86AGoxIlrAtIE7FgFyeK3qQg7BEf1_RY48dv2DtxqQhgqoWCyWsHT-Wp54b0tOOKdXp_hsVokBLYHqCkLzVgFVmLz2ABG-TbfVpWKJhEPY1653SkNL321erl-IIvoK0rigLz2q9z4Ba3F5gfAtiYHrTOFZ77vQh-kkklUpiyQoo-xHUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxHgVXXNGqkzXk5SGLnFRKxamCxnEdT_GuRZtYy4pbSTygal7rzIAzV9p0vLdQjAbugje0CWufghcRokCYZGnv_um5stlFOXSu9m2N1xCYorMpyffKbgrrSPF6Z2Nnhp2BfhtNBJ5xlmSDE0Xf5OxL7Jr9PFO4TgFl3QaPAgcYKtCLmitB9XjMHZ1nOc1kx8NOX5hDyy79WG4RfnY0PUpzKygPTQNQqpoOfNsbIpdsYYtVZJ9IEbaKCWWVvKyqBZ278BjrjfmgH8LnWc9scdxLWfm8upLqNPmfqiGxwNKvD0a9JbgDIHUImajgMAkR-wYAaz48cljyWEzj88M-ED0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzgBKfu8teInPIOqcgyYg2iEfEYXi4T_K3VhBtYdk--jp5KmqdA097KmVhSK1-r17NUn34ZsAy16Fa5F33txzXzQ_MH_AsM9DcGB82UotOVXlUbWpEknf6_7q1EPRgoOuDF8BLHxjCpeQCAzn9nCbebET7ABHn8qv1Japh0Nt-FzJ4S6y3IRLV6VEexWzlhfG6o2LcJBhasNyVJUvBQiakPX0TfgG-PaWHfC34AWZiFlDd1v3PkDhTY3vOtFZwu8b7XbUgUtyQ5MwNjlDMWAymKzzcKI7V2tIlLAZgs3reEW5UHe3Ifr6kZMp51BoyK26-Qbqn2pl2ow8pJ90LqZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0LvVRBlisjUvCvPX0Yn76u3hW007P9gDFNg3mszeQndMaBDOkcAdEnQM5FWiFmMHYJ45w49AXuyEzg6rRRAnNZMXZc0mWhAuDVpLVWjPjT2lL53RCehSYuWoSsJLXCwUNG0WAT8fgmr6jOsehUCx5P7nTgS9iqQvOD-fsGCcFZs2VddWp3s2R5QPc2iXTxfaBZMSjp5r-B7ZLcgKGEOAfBhXlbjH6BShXMuiSU5AEI2cMq0MwUVRg9EiySoDIizAPUaazI-qn_EsG0b2jY59rg3oQ9chek9kqduYQS7DF_cV1MD8WSvVAHndu7FgQunTnB-j3_2OzPMiLtZ9wFzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkwGjpKGhf74l_FZ79mg4GrNoQq93HrPsW0P0Wrh7iRwWaJAL5_uef8dc-6MhoJkccbiSsfvmnd19LtEFBKCPvNR2l3Kd5k4TaAAmZZSjraT9f8QAVzIIg7la7M6xlc2vVEfu-Brw4_-GGB5qcxwSVctpL7bINgENcPVogP5YJQJYa2BYwAXusUU9RDnHz5ONqBo79rIKAm3qyIjbdMWEU3uFlu5LmCU5Ka-z2bJvJ3YUYicbNUao59gEceKRRroqFJpHFnl_o4bem7gvu9lWWO9FgTFg4MPxZnyLyjXiGEezkQTxTIxAjV_SA8N7P0xADUmrJ8POtmElpYFXxY5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=Z95Axqe1jHCdhZg1hmMJLRnovxD3tsZwZiB_3LCxJxzzyiiKFHXZR2I9zfNNIcqfbk4vZB8s88saFAXIviM0BDo9DRcP46Fi2CoLUjp6ObIKkFAOlME46Bmjc1AQuRGeMoTl3TRf8DctNPZKj52ZL6xdrTYVNo9brgkIkknTKAXI5p3tU9mjwFr_vi1zvjc7bFp6V1e2YmW5DAbHO70r8KHKXRBUmtc5vKrVnsmDbbgF2DZAmHQcbdiQzh3E5MWIX6aFT6vyQ0zZGYMRIjxrkImo9kB14Pdo4ZeVj94ZJjFjyDvuGE3lSYc-K5DdRY3YeoS7tP18HgIGAN1CDTE2BC8lARGJEVaBvudXIDxuG2XZ_-0e5awJrU4mvapmt-ptMHbfmOl8yqwEgYP-HCkkJ5p6hAEdfC9UL2cdAnLrR08kgsVsD9lMszzz56Yvd--z4g0qIbfUviYbOMRjGdhm-UDncTPZ6wbEYvXjOVYdHcnOCsGF0V65SY5AHMCnmpSpmDuZ_cEPLRGI6Pz_FWV7PVIrJGEZDsgplA3QhUo1GCDSA23XEdzXW_3k3JABIKvq98527nCNPOtm6EtJ2D2_f3ycTJof37AFsH-SiHqHz30tn436nKxwZZSLC7J5ip9t39IAmGnSpGCcG1wme5c6T1goZsNIo9oxISatTZRHYjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=Z95Axqe1jHCdhZg1hmMJLRnovxD3tsZwZiB_3LCxJxzzyiiKFHXZR2I9zfNNIcqfbk4vZB8s88saFAXIviM0BDo9DRcP46Fi2CoLUjp6ObIKkFAOlME46Bmjc1AQuRGeMoTl3TRf8DctNPZKj52ZL6xdrTYVNo9brgkIkknTKAXI5p3tU9mjwFr_vi1zvjc7bFp6V1e2YmW5DAbHO70r8KHKXRBUmtc5vKrVnsmDbbgF2DZAmHQcbdiQzh3E5MWIX6aFT6vyQ0zZGYMRIjxrkImo9kB14Pdo4ZeVj94ZJjFjyDvuGE3lSYc-K5DdRY3YeoS7tP18HgIGAN1CDTE2BC8lARGJEVaBvudXIDxuG2XZ_-0e5awJrU4mvapmt-ptMHbfmOl8yqwEgYP-HCkkJ5p6hAEdfC9UL2cdAnLrR08kgsVsD9lMszzz56Yvd--z4g0qIbfUviYbOMRjGdhm-UDncTPZ6wbEYvXjOVYdHcnOCsGF0V65SY5AHMCnmpSpmDuZ_cEPLRGI6Pz_FWV7PVIrJGEZDsgplA3QhUo1GCDSA23XEdzXW_3k3JABIKvq98527nCNPOtm6EtJ2D2_f3ycTJof37AFsH-SiHqHz30tn436nKxwZZSLC7J5ip9t39IAmGnSpGCcG1wme5c6T1goZsNIo9oxISatTZRHYjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJvb32QGc7twzW_IVLWHp_YEJfyb98tVlpa361AA3YiMuQ11RHlS3WUcccwNnKVMa5b_WYQTm07e9cRZ6YCPMxI5GSBOoR_ZRTaTp9pUS92GSSKxacZE8UkmamyY9WhgelmK9fE6oenCxCFtjlVMwNg1RhWGWS4qdI8CZjPwmZYaiagnX1OOyJO8Vmd8zngaa7Y0TnX-5QUCwOlg2PIufwkuNGdqNank02mUW4TfA2C0BEikjkzyPASwxm3B74hRo1jCsK_1prDl9952JW3T-5Syi1Ovn_Naha6gIo0S1yiCoGvxaFB0mq6pc7dicRmCg_i6i_Dw_s6ii8jjWXf36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-YSkvgw6rxtU5IgD5W_ZXF-LYwiLv_M7-IYlDFEmSfMKZ9qvZhhW-G_FbtaGg6NpCzQTZ7Y_3fpkhh0zJ5xC919_Sqaz1sc9Gg4OI_e1qWItJqlcKIiOz41XczLrDLyt6Rfv4NIB7fZF1xw5tvlq4WZcQrnwxdViNsNDHguNobt4mzdmUxEurBjMq5koGOVErxPI0QNSkVLfQBodB_VoLcrLI2H_h_H5ehs5Tdt8XVpOtV51HHOzvOKKE_CzeKNGH7Z3oJfMgnYIA4M8xRfUTzoUshtJtAQbVuSygdscWDfDEeOwFUCt4PZuC-WcWxVnBHTejjlGeH5o5ndtiQ-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA7DaD13fEEXk3YOC8x4bfDhGx3tgIsQDvYNCJVXQjgaZSAJ_ROsKnUEAOIcbxe5cLdwlwQG8JLeHILB5B-ZkMTdtlp0B_lt31OPxYijW3_p8gW4MzUDJyexpKTrD7AohyZJhA-T91ztzX9VY7oMa9-37aCpAyQY7MRupE2A5jv9A1BdRImnaftkHtvtP1WmgxjY3HhO2xFGADWoP4C1NXf95hSyzgtpENwI8Z4UgQfxRxLI0G62RzuNflSyICLDuBdrHyf3rE-s4n5e_JNEvahRtaBEghNoWWPtyCnKzMVmLmH2PJNIouy5kjZzRqeUdk9yXCPj9G_-NqEfmZv05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU2gPMbUHH-7tQDhVUvJCoa6HiZqO7DzL28LkX-NJ5Pgy0u4PUjxeJc94ZCC4vdkwEZhomFZIbZlIydD2SCgxfU4G48aTsPNJRjq5K3g7GfD5l0cDQ3fPPnGJd64PYyhtAaaYrjXJsX0QgZ0IHYcawhh_NSSiAeTYat3wAdCsu_nN-FLXtI-POWOhikOwZ2Pxb8zYxbhsZjVZEAh4uNZgTDuZD8hE9NMdC5jPGGptMIAom357X10YfsvcySR0qjTi7KCfWZTHxzaB1d_E9xW6J0ZNYqUctNK6qnYpY3GEhKFhyXCslwUFR-878ng0O1fHdBZgF6_eM0BckIKU8Qb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBal_QgK3UVodfbH5mPofukC_z5qiPF8G0ePWFw9ij5duShHg7auT5YunkA5_FjEndMEqFNa8F2O1HuenXruivcu8Faia-dgysLl_uCEub3GqlTYF_F2W_t_xsEgtZ_JIiAQmbKN84WWoO3TkrRS1mB67lhxWySa4J0-VJVY2R3zcKyM5LmE504zRfY2fxG36bf_k58viIydRkfcwQH8qkvDoOdmq4FS5R6Vs-BOa-DPa3_d4DeuUN5BZGXdAO5CeX_NmQzV8eaWMjzck4NUX2tyPIib7nLObDfEhFMNv7sqtlHTX2mGTRoi3zmZdQMNugcbgkQRrID2MVfpkQpkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDi2hAMmSRnKVdFkXUa0NSu65mmKZsn91mOgqZY9uY1VudYhNCg774UCSzB33o_QbseOUgzI-IEbS9rxULg7egdbN9Jl2j4A9dbJdyibpb3jDrXkrZAdF1TMs-5GMkOqcBjpxlVTM7PiE340gZy4pIwuk2pUn7I3ys_cmeCWQ7yQs85bDxJdkFv01vmv7S6JwKbCwkSvuOpFlyyORK8kx-zoXXCSkFWTPS1llh-HAcRMtaEsCI5URWQVhCvOsZEYXTY3lji_uVlL5OLnlzIsAjL3d-lvuqbA5gAgLSdpnNBS0EGETCcWgtmjU2SLxNuAdsKodgkCQA9hwHgdAyyr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=GqzDcAkdGOApeUjnjouAjqrENOAqEuJLeRci7eaPmMMPnd3koF9S_EfnM6qhs5Y2UKwUybWOO-02CvSyqxSQmsRwyLw8brkr683nz1jJoqglOkWnZV4lCd5A4Uc2HOc9HgU64hisL8vZAed9jGg6Y5V5BLRT--Q0n7M4EjQF0XNopYINMGxSe1nk8K5S23EmK97bwAWGS6HRqRLjD5Y3H-WBX3VksVmsSi5lSYOx7AnRhSg7-r4OfIZHRgSQGxc0rUeRazrpBEi6bxRle9nr22GbY6IRLeYhYxAOqPxaC3bHLSOck8B8NxcToX7Z51sKArkff579SjBdjeKDT1vPTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=GqzDcAkdGOApeUjnjouAjqrENOAqEuJLeRci7eaPmMMPnd3koF9S_EfnM6qhs5Y2UKwUybWOO-02CvSyqxSQmsRwyLw8brkr683nz1jJoqglOkWnZV4lCd5A4Uc2HOc9HgU64hisL8vZAed9jGg6Y5V5BLRT--Q0n7M4EjQF0XNopYINMGxSe1nk8K5S23EmK97bwAWGS6HRqRLjD5Y3H-WBX3VksVmsSi5lSYOx7AnRhSg7-r4OfIZHRgSQGxc0rUeRazrpBEi6bxRle9nr22GbY6IRLeYhYxAOqPxaC3bHLSOck8B8NxcToX7Z51sKArkff579SjBdjeKDT1vPTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biVCW0hpwV9Q_J8f5D40urlL8T6hk0Y1vRdUXuWTdddDJYZlI4YVKIHxMZTqI-lT-J986u6CQuJ_oaa86B-jCF6RVf3zuPLi3EASNFOxiNcRcXJ0zNOuU3XiBi88tQZw4D8ZAX_kQY_xOkxCmnx-odoTibRI2yXHlWwnydake6NguZPC1B8DBpI42PwG0pAx2vhddA1siSxb3K_z-L8fnQczj1_4ropbwfCVQnwp7mBkK36EkRVP_GGVVDLUEu1526nVtXlVWRkOVYNLKdXmMSiSk09S4w_kfWZQPSzUe4X9yAThNlA5ixEWUhBtMNrwsSB-i2RyTP2EIwccql8ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCf2p1eRCsiNOxoHWmwyzuJ3ZeG-YeumuojRBTJFYKRdJIQ3NTHg7ghVqjYEAwag7AJvGBSbZ0mvuvyjqfv52OfsGGH9Hl9BASzcPwom32uIXtfMnNWtzGaOSPUeiGp95BuObCZ36zby3kONpYm4u3KJShNUT1CaXrvPFfoxDjbTXDGtTNw7GuFMkqH8fgbI-g_rOKtmbG3VFp64BSJxm1pqHjITKeNql3qheZ3wLQqDbLIxFpnxvKntRXXhdpgiFj6ZIwIg1fQ7sAGlZX38EX4U8UhWz5GgB-pFoAfqZ_qt_ZlP6DpBK85f5MOQDdEyjJz9kIwpEeQN10Rhg-Prvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=Ayhy5_MaqoQgdedz6H-YpWInW9-wo9E9rLbZo1-dXRFfqoh9B9xQrQmUbEM_eoH1GTGQs2GziXuBLx3_T_ke9vou46PVQZHWpTY_LX-n9YUruBoRvLlB8EGS7kud8MoSfaYMzZeIq5noasmRHtXfxWPtraBiY3koU-EsDVLScIziWvuCyg9WMxTz6g19qObWcYkAcDHRrcyGPp3JbZMi7PlX1ww1BaMuNJHjS4qpRicCwAJiuEkrdDEq72y2EJdLIScTq1e3VZaajZPpjWYA246vyiYXTxp3JSs3z55cEDNi6DsWQbFLHKinbA3wFD2OWe5Ap3A6U50u2ao_PRjEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=Ayhy5_MaqoQgdedz6H-YpWInW9-wo9E9rLbZo1-dXRFfqoh9B9xQrQmUbEM_eoH1GTGQs2GziXuBLx3_T_ke9vou46PVQZHWpTY_LX-n9YUruBoRvLlB8EGS7kud8MoSfaYMzZeIq5noasmRHtXfxWPtraBiY3koU-EsDVLScIziWvuCyg9WMxTz6g19qObWcYkAcDHRrcyGPp3JbZMi7PlX1ww1BaMuNJHjS4qpRicCwAJiuEkrdDEq72y2EJdLIScTq1e3VZaajZPpjWYA246vyiYXTxp3JSs3z55cEDNi6DsWQbFLHKinbA3wFD2OWe5Ap3A6U50u2ao_PRjEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7ldbQl3DfUs1mykKbeyRN1xQII0xvfxxEit5W6uNBJAdhje4YyPuz72jSu9FTRV5Vs2lIR0WUIq2F9A2m_Tiu7x_9OxZxSVMSb3kSyvch9FM3lm_oUL5BjrUe0CnonQdEzlcrAHmIy-kPw7vrzXY0A1aRI0Bd61XOZAv5zSVtGgXEVo9C_IV2kntpigc2I89GH82xPzodDHaIEvV5hrbssWYJ4iSYbV_6eYOIpi78hu-J-Yb_cigcKQ3iuQx_5mNMJkjujA1nHg2BT2qwZt9__aC6JVVPMlRs6G1xN749E_H8LfrFpGT5O39RJCbef0UBrptytL5GSXnIkiLSpMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=lCVJD5v7X-H_QM7UmTrlSyHTdFP9lB7xoTCcyeDtJhZ6Q4mf38SDDnusNOFjJXN7DM4NtzYK2b-fDmpSeQrV9UZYRTIOO-q4vFPnkcTM_w7GE9UsH3pmxTdA6NCmAELV7ePzPiFa5mkhaqiLaL07o6OE774ZGAH_uczIQbC4izJ5zpolLZ-n8XfNz92Rmb44nmUre3RTfkW7AmzIP21pT9hC4Rv9dD7wKj1k3T-RWX4jZJcA_5fYa9UYJuxrrNZvEs0vQvjaNvlytpICzRMrmk33EQkbRQFAUWS9HBUyteu3G2FkaK2hIOdknLr-iMtG9tmnygAhf0qLZuk5cz-35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=lCVJD5v7X-H_QM7UmTrlSyHTdFP9lB7xoTCcyeDtJhZ6Q4mf38SDDnusNOFjJXN7DM4NtzYK2b-fDmpSeQrV9UZYRTIOO-q4vFPnkcTM_w7GE9UsH3pmxTdA6NCmAELV7ePzPiFa5mkhaqiLaL07o6OE774ZGAH_uczIQbC4izJ5zpolLZ-n8XfNz92Rmb44nmUre3RTfkW7AmzIP21pT9hC4Rv9dD7wKj1k3T-RWX4jZJcA_5fYa9UYJuxrrNZvEs0vQvjaNvlytpICzRMrmk33EQkbRQFAUWS9HBUyteu3G2FkaK2hIOdknLr-iMtG9tmnygAhf0qLZuk5cz-35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDTLXRkH4gl0QH6Ga2cNY-qeec6c2WMSdwcCsvav2cP3jSFzmNcjrrhOSxHA60aWn-YSyasXST6_UsECwMa6uq4NzOR_p-GgvP-elTt_xGq1_PMUshNXhQuta68mFoLeeDT4PV9sADO4k2crFSgYZBwkPZnmj8CmctoKTARjl1h-vbaQIFXAFlH9MaJSRsrsaUBavdbwyhktVnqpoB8xnFm5yRRNuxI_hOtXX345bTOmp6RJ9Gpc4MV9vExf9i-h2rHVkaXEIDIRT45UcgfxvjY5l3HpglFZ4LxcvDobzH95hbttNY1jTjVbMkKLx31H2-c7q0XUpNliGgDpKkICtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDKptye9_xwyU3Ou3ucQCH6LZVJK3uso2sCMNeN4TqjYOd2VJdzzycowDDluliRCjQ3mUA9vvveiqaiCDkXyZHyd5SD0UHIBoFh4nt2becQM_7QxbBKVLfASWP_8LJ_JyRo9tRURreu_-6gA4J7jaT9-A5-g6LuOUuWB6U_XpFvZTBHMDSlp5xJdkYGufuCodcCKES6EKOhnfc2NFB7PMYK35RsUnhsfauYZPGPqc2M89erURECObdgVFNd1H9xIEPQpkb3q4gmPzcPTRGIUWuVnxSg26UqY10PiP8QiIvNr6rV0UI9RXlUXJZQZr-q1WGl_LiymxsFQCY5Ij3g38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
