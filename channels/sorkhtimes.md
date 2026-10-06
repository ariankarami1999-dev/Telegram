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
<img src="https://cdn4.telesco.pe/file/pXIRET1Ivb6DCLzsszBIujvTv6o9-D4vddbP2JDpiRggSqefwnpLncG6U5LH713NDS025lHdMxdzAKFvoGZrIVh6m892xYA1fb8sEKwMC3qo2QV-PAKrKDconEZKcQ1zpQs7UVkqHGnebJXojWQV-v5MlyG9Ka0nQUsUHK_8-TNuetFi35hq-oXYi2LTpl5WbJ8VLRzJPXIt_C9Fmdlh85BMrGqltzd5AwHyWnhRFjvjFX8v8ZRyO8oHey5EFdIRJ922FVbFQGh2Ol4N--6o-m7nvSQ6mCQqd4Qq5H4wq9KSglOBIoxWYJxX_pjXc8JOUQPz7OmKVNoVJHaNEFXIgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-141021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✖️
✖️
✖️
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/141021" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/141020" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/141019" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjVgcrFKN6nNiSjz4FrV4y6sXdsv3Z85POppH2uL4XwaTc_R6lLO4hN_NOkIAmrtxSRC1pN1YzQiU9Qb1nycxTqpL4K8Dn0GWz48G8PFGW1MRuaN1fvZ-h4eQxWrEl6-PkTR04dQaHIvF5TYWQt_FUX5zE-Jn4rq0qehrEdwchTEMkHLCfLBKkyCSoeIi6PJoYmBamP8BqlS1oXkLgv2q38IPPmnVlrlWSzD1qdpkvT5fCVY7nab9pQOXjBm3qSEi3gPzZaADU8HvIMJkHgIdsHfi5erHq57lqIw60FTFEfqxtIpSJCUpJagdl-u9Nw2l7w4AvqmExe-_IYs_PQI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد آتشین بالکان؛ کروات‌ها مقابل ماتادورها!
🔥
⚡️
[
کرواسی
🇭🇷
🆚
🇪🇸
اسپانیا
]
⚽️
کرواسی با بازی فیزیکی و انتقال‌های سریع، می‌تواند میانه میدان اسپانیا را به چالش بکشد. اسپانیا با مالکیت بالا و گردش توپ سریع، شانس بیشتری برای کنترل ریتم و ساخت موقعیت دارد.
سناریوی محتمل: بازی نزدیک و تاکتیکی؛ برتری اسپانیا در مالکیت، اما کرواسی خطرناک در ضدحملات.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/141018" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa3ESIEDp4HPLoRqr8tusrVXBWXK1pHEcg_AxtAJmzXwN4-6vOF00xWHt-Uyy9ZxZ8kXIF2p1_ooQOZT13bzi-f2C4v4b4IYr42PtthSbxvqqlI9oFLndOUdBqt9k379T8w6367nvikxY27JWcZJnIZUa-FlcJdfQliSCCG4V3zVk9rtTuvkatJ8zxLYbcrAl-11S0yfvc7dykOZ-yJKbJNW9GhRcCNm4Rxl0DrhGCTZstR6Y5V_fJE3E3BFG_MgNNoY_Gx_a8IU_LEmAL_yRFcoRbINfvovwyCofCoQeMHQKG9wLNacDDWQGlvhj8NJ33JiBjaOF60uTj-xYHNfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
ورزش‌سه: برخلاف خبرها پرسپولیس هنوز در مورد اورونوف تصمیم نهایی نگرفته
دستمزد بالا و مصدومیت‌های اورونوف تمدیدش رو سخت کرده. البته احتمال تمدید و فروش او با قیمت بالاتر در آینده هم وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/141017" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/141016" target="_blank">📅 13:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbT4L10PQJNz3ToWjurBZthsTupJGty9Nmy9427HFgKfVxqn-j5Z2GL_t_jjrIxblyUBXaME0D8sPn38YS_JZw5bBGeHSfD5jDKj20KcvwgnLLNipCsPhumN9Q_czHz2v56UcZ5liH3-Gzjkr4ruM4Q2FUhcoeSWVS2nU4gUHRkBviW6AHJEoOaqdZCkuGcMYjROy5a8ZzTwflPdC5eXWyX9QOuoN0YSHIrxuYpeXRfDSqsO71cc-2hFHbUK_18wvQFkYSm2hnGkTloE4-EgTzhj1qT74dqALVON40MuBmBszORjMohVy0tQkW53bELYbFO74SZ8b3BDNOqhExHMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
به احتمال زیاد امیر تتلو به 20 سال حبس محکوم خواهد شد./آنا   پ.ن اینم نابود شد
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/141015" target="_blank">📅 13:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_eM1OdKVGrQpUz52n5e1yChZ_Ur4NUUjCjkSkht_rAX5Axhq2L6xLFyvokwXctVqn9xe0c6G8hbQsSGUidTB1Jxf8G8tHe93qFBgkuXfNJMSZdOSXbUUKbyS_QQUs5wyRO8hSwc_-VtftIJiwhsYe_oWFYElAu8vZiFGXliHv3W0YnSJwIJ1P1nqR72h2wVlLjIht2_hQxbk8P3naA--D0bWwUgo6fOZMg3nyH8GW5YFKaM4v2GO6DniezfwhPG9P45xkzTYsiug12Ye3mKcTllYZ-5q8TxICTfW56kYoKRe7w6UVdZgiiJyGHVHo3yx-Rzy_8QMEA3Qj93_WE_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/141014" target="_blank">📅 13:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
پزشک پرسپولیس: دانیال ایری در آخرین بازی تیم امید دچار کشیدگی بالای عضله کشاله ران شده و به محض برگشت به تمرینات پرسپولیس برنامه درمانی و فیزیوتراپی‌ش آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/141013" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
ترکیب پرسپولیس برای بازی با صنعت نفت دستخوش سه تغییر نسبت به آخرین بازی این تیم خواهد شد
🗣
حضور حسین ابرقویی بجای کنعانی‌زادگان
🗣
حضور تیوی بیفوما بجای اوستن اورونوف
🗣
حضور پوریا شهرآبادی بجای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/141012" target="_blank">📅 10:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTJwO7mwAtorqXAEwfaKWYupGDIlLDRsQPMkMdhnhinY47dwj3fWT7tmhK-P90zLzYFlMeOgpFxHD3Q-yP30FSsr--ulkzd7sHFbaGMD5c_WoGQ2IgeGyL5spE49H1oGfmvCwmEkdCMfus4Bkaa85kO_HvxHCxs4eX5ANBCQP8xL5IJdWhCUaaspeEMpoeExNylrkJ-s-wYgE7ZeAAM1D63NyyfRgsGSRJwf1CCPS4i44jSFrhTXFFKM0edIVZvmsi7LZPM02SzbI0-Ww-ZcD79sQajSQUjImgNsMN6jIXTTyS_3ca9kLoqgBsP9yPCKzXavW74SvpeSNrigEdzpew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😄
بیرانوند به یعنی میگه یهنی
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/141011" target="_blank">📅 10:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
#فوووری از ورزش سه
✖️
✖️
محمد حسین صادقی یکی از بازیکنان اصلی پرسپولیس مقابل صنعت نفت آبادان خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/141010" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
مهدی ترابی نمی‌خواهد در تراکتور بماند و تصمیم دارد که هرطور شده به تهران برگردد و فوتبالش را در  پایتخت ادامه دهد
❌
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/141009" target="_blank">📅 10:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/141008" target="_blank">📅 09:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
فووووووری
✅
باشگاه پرسپولیس نامه فسخ قرارداد یاسر آسانی با استقلال رو امروز به کنفدراسیون فوتبال آسیا فرستاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141007" target="_blank">📅 09:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141005">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvI2jU3kOkJ67SkJyugtBcv4vceZBJxs1MwbnicIXkbY9taycp6nZe88wpYALV6UPbBNVeMY-R3EjInDaTi9h2Gm-jyhaJcFzdLXHmN95CrSAKHCVHWETRBX32aH3E_pEgEcobgKi4lenuHDOlxcBV0SOwy9LZRqK6l5V0-EUi38oC8EZq94fqiftO05pRTm4Azndu91LzbuydJHQzS8UEPl_-3N9CL1ELNSdIz8tPLzzJK1q8nRrfKzyz4UpSa4vP-bdpKa-14oAUbJTNVFFMdQK5YqDJ1EJN08OC8sPCyusLsU47pJca17vhrRJxuByoSYq9rUco-AJ0iHCZQ7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
سه‌شیرها در کمین؛ چک‌ها آماده‌ی شکستن نظم انگلیس!
🔥
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇨🇿
جمهوری‌چک
]
⚽️
انگلیس با مالکیت و حجم حملات بالاتر، احتمالاً بازی را از همان دقایق ابتدایی در اختیار می‌گیرد. جمهوری‌چک روی دفاع فشرده و ضدحملات سریع حساب می‌کند؛ اما مقابل فشار مداوم انگلیس، حفظ کلین‌شیت دشوار است.
سناریوی محتمل: برتری انگلیس در موقعیت‌سازی و گلزنی، با احتمال بالاتر برد انگلیس و مجموع گل‌های ۲ تا ۳.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141005" target="_blank">📅 01:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141004">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWyoAnnSRxvn8nydPw-pxvT2Bzi0ScXZtdnf-irxo4t7vM3SwiAHnHlFsdOVDKjX7_63MzZEdUE1mF4SN-K9mehNZzKjw307rJSaWAXWZJOntXYi0wqG3dK2D7WAxNiDOLIZrYwhfGbryzybeBLByVQfVSZm5_qVFfOrecd2ix6Q6shnN7bw4dUuE7EkLW-pet6PHmb56gJEAj2iGzxJWTlHCo6CGTjoJBeFzv1fRRiI-92GIsPTPB3ad9SYyCzcyQXhrAEFtXY3oUkd5RtN80I2SyJmFI7NiirC2g_zXWm5vP0LuEdAxj90BT6pFNm-L7FQJYZsTix-pwgU-AXHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سعید شیرینی، سرپرست سابق پرسپولیس، از مطالبات حدود ۷۳ میلیارد تومانی خود از این باشگاه گذشت.
🚨
بر اساس اعلام پرسپولیس، این موضوع مربوط به دو پرونده حقوقی بوده که یکی از آنها بیش از ۴۱ میلیارد تومان و دیگری ۸ میلیارد تومان مطالبه به‌همراه خسارت تأخیر تأدیه داشته است. با اعلام رضایت شیرینی، مجموعاً حدود ۷۳ میلیارد تومان از خروج منابع مالی باشگاه جلوگیری و پرونده‌ها برای مختومه شدن ارسال شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/141004" target="_blank">📅 01:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141003">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
مهدی ترابی در اندیشه‌ی بازگشت به پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141003" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141002">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141002" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
عادل فردوسی پور: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبود بهش گفته خودتو بزن به مصدومیت تا تعویضت کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141001" target="_blank">📅 22:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141000" target="_blank">📅 22:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
✅
فووووووووری از فرهیختگان
❌
❌
پرونده آسانی از دست فدراسیون خارج شد حالا دیگه فقط ای اف سی درباره این پرونده تصمیم میگیره و کسی نمیتونه کاری کنه    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140999" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔴
علوی: هیچ جامی قرار نیست به استقلال داده بشه و بحث قهرمانی این تیم در سال گذشته منتفی شده
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140998" target="_blank">📅 21:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D84YggrhSgR9JhFpqWPrUujNtTo_TK23Pj9_z4qzIaQZvYOmycwmdSbyOrzPSdzJqULywLFTDi23OO_S6SeVWSUNTGwGfEZnp3pqcgS1Fw7As8HojDwLNOcPiLem7-F8naWh77Nv-XMFB-g5ZmVyC3wEttL3X2vjFDdeVk4f9HbqzgxET3b65ZS3zaxNQ2dxecp0nGOcp1WvbDCLnfJwxMgCu-4BLTSpZmx5pXS1Rp5492Q8yDIES1tBrHdUNgtfzryJZXu6iZsKfQ7__AJPdyI9Ho0Z_d_UVAWUvk-STLYWHJQZ_wd-ys5TuK4atycohYGnRdZSNUniAa38o6ODGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
گزارش تصویری از تمرین امروز پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140997" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💚
عادل فردوسی‌پور: دیگه حوصله شوخی‌کردن با قیمت دلار روهم نداریم، روزگار سخت و تلخی که سپری می‌کنیم، شروع فصل لیگ برتر، با دلار 187 هزار تومانی، بازگشتش از فیفادی، با دلار 270 هزار تومانی!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140996" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140995" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✖️
✖️
✖️
فرصت طلایی
✖️
✖️
پرسپولیس در هفته‌های پیش‌رو برنامه بهتری نسبت به رقباش داره؛ استقلال و تراکتور درگیر آسیا هستن و سرخ‌ها هم بازی‌های عقب‌افتاده‌شون رو دارن.
✖️
✖️
با توجه به لغو جام حذفی، هفته‌های ۹ و ۱۰ می‌تونه فرصت خوبی برای تارتار و شاگرداش باشه تا…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140994" target="_blank">📅 21:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140993" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1mKrZsW2JlxSp7JRkzFP43sc-FFPoNLTQxSmEgAH_XCvwV1vaxaKgO6RmjqnX3gBoBXLU_egign1Kyer4k05c4lcfk60u9iEgyWbOVjuT4Tgp60c3SuWer8X4n6177YdYL-04B2W16WHl4pDlVekGNqm5MoerXp-uLB2QtF8QgtCh6dNN5fTy2x8gVD6tQCc6Sw75nnssyxcPtxXR17iKN8uuWUK6LJhJZXAfElRzDUFZgLMn0Wbmddv1z80eUzKcsyJcMa0lK4O69NgtEWoZjBuljujL_WqavR3VX2BEcQocp5qt6fFlRYhyIg5xe9DtBy2z0vpbV_RfUmzDRZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140992" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
مزایده اموال پرسپولیس با یک خریدار خاص
🚨
در پی شکایت یکی از طلبکاران باشگاه پرسپولیس، دادگاه شعبه ۴۱ عمومی حقوقی تهران حکم به توقیف و سپس مزایده اموال این باشگاه داد که این مزایده در نهایت برگزار شد و بخشی از اموال پرسپولیس به فروش رسید
🚨
🚨
در این مزایده،…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140991" target="_blank">📅 19:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmN_5mXObZryhu529bywKs6UcZR0y_cJg4nLdfhv5s6PZUQuc8YoxesZv2QnFWmN17kZeq8gnJvZtC1pEpojuGh_J4G2PHNaCOm7QYIpGHb9WFWlwWoZDzyxBGThNA-SaekT7ND8XyPHJ-E4Qq4LopMJXLHpFlHCtlWBm0J6kvdQYPjRpgx4hpwvanzPA_r8wb65UwUlY2eLrwlZxcNtmU7-wpdYQqDR7lWRxOK6saRnFHxbHvRHGKCqD-SirVDq58nMHpa2hMmdO08HBJhjungXxPvI9czXuzaVr91lFAnzglnwYvZ5Wb6lK0rUuoMwhbBE2kqXUvxil9vSmA6BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇧🇪
بلژیک
]
⚽️
فرانسه از نظر کیفیت موقعیت‌سازی و عمق ترکیب دست بالاتر را دارد، درحالی‌که بلژیک بیشتر روی ضدحمله و انتقال سریع حساب می‌کند. با توجه به قدرت هجومی دو تیم، سناریوی گل‌زنی هر دو طرف محتمل است؛ اما فرانسه شانس بیشتری برای کنترل نتیجه در نیمه دوم دارد.
سناریوی محتمل: برد فرانسه با اختلاف یک گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140989" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140988" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140987" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTfqvQdzcUaGSu59WVwSn0rafaRbcVz0J-p1s8uhjuXlV1PKA7TqhPRUooMo6W3HvCIGaUigyqZ1LDQ9lwE1ITBRxbuqfhLnE74IWXM3x64x35eJmNxzFW3L9Mf56Sq77ZlcFiW90uM8bRMigTK0Z2s_BKt4wuNUT0t-pxh0rSETIvorYM0TaD78E44Yc8w9XR7QMjmtVuwEJxVncr7LYMOgSyVpANTKoCD0v-Yc8SC_x6p8S1sddaVJWmVHa3msEEO93w61be3GbIkjm_NE4kyAacsdnEdcOsKkYDhcyxw2ezzidx9sSHv200TutU2V-xFcAX4mSM56O7hNC4861A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ساختمان شهدای میناب باشگاه پرسپولیس مزین به تصاویر شهدای مدرسه میناب شد
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، این اقدام، ادای احترام خانواده بزرگ پرسپولیس به مقام شامخ شهدا و خانواده‌های معزز آنان و گامی در جهت پاسداشت فرهنگ ایثار، فداکاری و شهادت به شمار می‌رود.
🔴
باشگاه پرسپولیس ضمن گرامیداشت یاد و خاطره تمامی شهدای مدرسه میناب، بر ضرورت صیانت از نام و یاد شهدا و ترویج فرهنگ ایثار و فداکاری در جامعه تأکید دارد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140986" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrhtFMTjJJS1tJBRlsc96Rdqm51pc11Uq1Gm2WhrduekDzN1twszS9ourYigdp1uQAhe9Qiot-XKMyr2r-TyLBWCvipvcaATAV6GncQ3a8gxjEk4TQTxWiiEmsVnPPk2jSSFodJHH5sQIBdgXdwUZMW7m54jo-EWNaYisgSEucTf0mkTiJ-gWL2elx5imqBeJfACHt228dH9Fk--jgVh9hZbPb2-xkR3LXpdyhPyG62ACPEoVJkR-_-Xmo28ffDA30FxU-lE6UUFU0EbT34-RcmBNItLgPCU91-NjAx8ihhY98gJZaaflEakCUl-o2DdLqYB1IlxZA-YQAjtwWpKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140985" target="_blank">📅 16:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140984" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140983" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140982" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140981">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140981" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140980">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140980" target="_blank">📅 14:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140979">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140979" target="_blank">📅 14:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140978">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140978" target="_blank">📅 14:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140977">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
والیبال به میرزایی رسید!
🔴
با حکم احد میرزایی؛ رضا صفایی سرمربی تیم والیبال پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140977" target="_blank">📅 14:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140976">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
سعید دقیقی در لیست نقل و انتقالاتی خود برای نیم فصل خواهان جذب سه‌ بازیکن از پرسپولیس شده است
🔴
حسین ابرقویی نژاد
🔴
یاسین سلمانی
🔴
محمد حسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140976" target="_blank">📅 14:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140975">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIbpDPS0jeqFMDCewi7L05dCMgDcv21OwNMPk6siKTM5T2WcyTbMsfXgNN54YLGUgiyHeNBwxoMG_G8c2t_E2LE3wvRr1EoIJpjmgZHBXpYoRcz-vxbI2DZquu49VRCShVUO9itgWKh2_06LXgTznvtJ5VKWZET-v33Xs-2eViAv1h-FeRWerbZFLl2eL655luVJzJYA-ksP4DncgTkEb6Keqe61P20JmzqXazIojLTXoMidaxHgrGWzXXFDPjw2G6B97JOMrRcKE2-n8F1LZTpAd8LDoxowwfHUeOHGyEhHvGshzxjNz-MOgvkchdmcK2xkrJjv9w1fT0GUYeFe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Italy -
❤️
Turkiye
⏰
Tonight 22:15
🏟
Stadio Renato Dall'Ara
⚽️
ایتالیا در ۳ بازی اخیر ۴ گل به ترکیه زده و در ۶ بازی خانگی اخیرش ۴ برد با کلین‌شیت داشته؛ ترکیه هم در ۳ بازی لیگ ملت‌ها فقط ۱ گل زده است. باتوجه به برتری ۴-۱ بازی رفت و برتری تاریخی ایتالیا (بدون شکست در ۱۵ تقابل)، کفه آماری همچنان کاملاً به سمت آتزوری است. احتمال می‌رود ایتالیا کنترل بازی و مالکیت بیشتر، ترکیه خطرناک در انتقال‌ها باشند و باتوجه به‌فرم دوتیم برد ایتالیا با اختلاف کم محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140975" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140974">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140974" target="_blank">📅 12:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140973">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOopSsr0-5Eua3Q4dIHuDaMS2YlUwyNZ1zi72g1t4E3wLH1JI7hqg4n6_ORXOrl5GFXPkgxr3jBXQkhXIlNLuXwy5FXf2JKBmXYxQ4BUSphq2TlD5NuisPWgSJKoAKF6FylCEiZXjKwKRvkQ2gj19h6qouJNj9WyZWKUUSdYMqC6jsdXVmSAaNZJGY5jWivC_Nfm0xgnpND7T3gOj-pCezGp9eYvgHjX9GxBftJ-1Kl0t19q0XmLWvix-BMOjonwimy4KRrRXHcBfvdEK0XNH9_iUt0FWoKAHKh5kCbciKnZqd0qPzYV3C711SHIrTHiW6pabFbYXgyNmjnyGFioAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار قصد داره از پویا اسمی مدافع ۱۷ ساله‌ی پرسپولیس در بازی‌های بعدی استفاده کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140973" target="_blank">📅 10:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140972">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1PkKCxIUgt6998gH78Duea3ze2NJmrEvdiS0Nw3DuSZTq0-zEPyWz-c72cKS1BbaGqbhVxxHSiIEY5KpmIso8bKPtLN53TfF_G4iqRH7KuAqjRj8pffVGy8YvaUgLi97H2bmnaPXi126u63hNks9LnE-xIjN2HAYQmq5MsSWjMWfFcud8rdKirckrLtE_oBEgzEHGJ4y28-cSrSBxHyIhdRGGwjbArzcmsyxOLvDaHiZ9eVMYKvpyBS6Gf26U1_VvYsfadob4qQREfkccXBhGeskz_oQu-ju_vhkUXynlv94pRy-6LWOGlc_JRN5v7NVe5tv7xOe9ZQ7b-XPdHwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووری
‼️
🤩
با اعلام خبرگزاری برنا
بازیکنی که مدنظر پرسپولیس بود
شرزود آسانوف ازبک بود که بین
دوراهی تراکتورسازی و استقلال قرار گرفته !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140972" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140971">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
عادل فردوسی‌پور: نیوزیلند جزو سه تیم ضعیف جام جهانی است. اما برای نتیجه نگرفتن احتمالی، برخی بهانه‌ تراشی می‌کنند. برو بجنگ بعد درباره ویزا حرف بزن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140971" target="_blank">📅 10:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140970">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
✅
#فووووووووری از تسنیم
🔻
جلسه کمیته استیناف برای شکایت پرسپولیس از آسانی امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140970" target="_blank">📅 10:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140969" target="_blank">📅 10:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140968" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuNJ8qCYQkCSBEQvCM293c_7Q9IajycURGtVbk0rCbRVDyfX5BJ6istHZRUm-1Yyz12LLMKLXDr5FS5A2lmv8o_Et8_l-pbLhGcly_KC7g7T15wZKXS9xnmzMBGeyEls0UQ9LowXTl6_bYGojvoGyzzZHZMZFA1d0kdNcWqSOeC-wTK2p8iOjGaC-HNU7_8xHONZVcPIjPcZX0laPf0Htnp0Ve5gvFNF17cSC32K6fuGCRxnswR9qFgu55oYO8b7Boc2F7CbnzsAdcUzxdEP8jtytl63DcnlJXLvAGC9oQrn7hKAp6rwJOw_cOmyjHlaA3mz3NdcyWwJ75Bdjonl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شایعاتی از نهایی شدن انتقال فرهان جعفری به پرسپولیس به گوش می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140967" target="_blank">📅 10:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140966" target="_blank">📅 10:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
مهدی ترابی در بیمارستان‌ آتیه تهران تحت عمل جراحی رباط صلیبی قرار گرفت و زانویش را به تیغ جراحان سپرد و شش ماه از میادین دور است.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140965" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140964">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140964" target="_blank">📅 08:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140963">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOwhHI3gWxB_sYWmv9d38NVBRdZ6br_AGRHmK9rI6NBcRqzSIUYre87NCTcKzbrBSkjL6KxEh-PoxByrno5Kg1j170AujjbwPVUokrZScDyZLSbXh_nSEwZDEBoPw5LcLoy5NHhwS7xjfec2a-K83-THsJ7VTOBzo82C1n8yAzCS-nPD8-4l99JwG0mD78QZ7GJ9wWuebO5Zzr6zIy61YwuUT4nNKGOG1Pjc1eXpMLZk-Oow_8v6j9vxDZXWbeqH9lySLRQ0-XRzEjUZsaXNBtGUFF0b0b5hWMO0ukls7PmEJIMSunjPx3nAygqgzwoXR3_pn3c7nETRdr5OJphBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140963" target="_blank">📅 08:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140962">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc_Jd5CeKGfMP-13-sE3CgtsI5zmVcBbyvLivOV6ya9XyehEqFfa4oyy0056N-g2Arrxh3TrQ9DdlMr2V7zanrEyxOoKzIYCs-L_wT5KgdgrgFc3qeqf0TootraJ51b1VJDXValQvoEigwxuP9OX6SMbTd8KQ1yBvr0-bqsElop64WnbIU7XatAACW4p3qZXU0mUms9D2XntOAj7TZP7L-iUOyf7_ATym2icWeHqZvNCVrBemNjJgvgTxWAeOSWNY8wNR_EOUIRjbOGMtCUo6r7HckKO5y2ZK2e1baalBKJJ7yoGbAiPSt8GOirpzW_NU8naXgaIa-Gao_ipXhBrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
France
🆚
❤️
Belgium
⏰
Monday 22:15
🏟
Stade de France
🇪🇺
فرانسه از نظر کیفیت هجومی و میانگین موقعیت‌های خلق‌شده برتری محسوسی دارد و احتمالاً حجم بیشتری از حملات را در اختیار خواهد داشت. بلژیک در انتقال‌های سریع خطرناک است، اما مقابل فشار و مالکیت بالای فرانسه احتمالاً فرصت‌های کمتری برای تهدید دروازه پیدا می‌کند.
✅
برآورد آماری: برد فرانسه ۵۸٪ | مساوی ۲۴٪ | برد بلژیک ۱۸٪ | بالای ۲.۵ گل ۵۷٪
همچنین در غیاب دی‌بروینه و تیلمانس احتمال می‌رود خروس‌ها پیروز میدان باشند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140962" target="_blank">📅 01:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
💢
مدیران پرسپولیس به تاج اعلام کردن اگه استقلال قهرمان لیگ اعلام بشه از لیگ برتر انصراف میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140961" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140960" target="_blank">📅 00:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140959" target="_blank">📅 23:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ZwFjWfUh3PGNWkdlhDvZxRjzLC-SJyEHj504uleApvqcY-xl3me_hKp_bAAxvfYTf5V0f8p1qcLzkTWidJ6LgkwnQT3RCFkBGEfj5_Koj-jjDvZOQ0Rjc2Uqoq2IuRpahw7sNwKO7Dxr47bXzaek0L05VwXspzNN4bjj-fCYN5HP6X4FNAzad7VBIVZWNJSBaCKwkPTYN-eVJe6PT60Z2q-IomYWXPYjoLU9Fokp14WhJja-KyZOKu-IIyqKmG0HDQi0v9lwJWAio8N0SNXU6MYKOtpFPhpa7NLBsyXiCuZK-HTA3mQRvr8YOvo9K6wUOmkPFomAtL0RUNMGuiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚪️
برترین بازیکنان لیگ برتر تا این لحظه از نظر متریکا
1⃣
⚽️
🔻
علی علیپور 7.7
2⃣
⚽️
🔻
سعادت حردانی 7.49
3⃣
⚽️
🔻
اسماعیل قلی‌زاده 7.49
4⃣
⚽️
🔻
تیبور هلیوبویچ 7.48
5⃣
⚽️
🔻
یاسر آسانی 7.46
6⃣
⚽️
🔻
محمدمهدی محبی 7.45
7⃣
⚽️
🔻
عباس کبیریزی 7.44
8⃣
⚽️
🔻
امیرحسین حسین‌زاده 7.39
9⃣
⚽️
🔻
مجید عیدی 7.37
0⃣
1⃣
⚽️
🔻
امیرمحمد رزاق‌نیا 7.37
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140958" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140957" target="_blank">📅 22:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140956" target="_blank">📅 22:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
قرارگاه خاتم‌الانبیا: براساس اطلاعاتی که دریافت کردیم، آمریکا قصد دارد دوباره به ایران حمله کند. اگر حمله کند، پاسخ دردناکی می‌دهیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140955" target="_blank">📅 22:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140954" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140953" target="_blank">📅 22:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
حدادی : قرارداد همایی فر ۱/۶۰۰ دو سال دیگه هم قرارداد داره فردا قرارداد هرکسو زیاد کنیم باید بریم صدتا نهاد جواب بدیم ، اضافه هم نکنیم بازیکن انگیزه ش از بین میره و راحت می‌تونه فسخ کنه
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140952" target="_blank">📅 22:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎙
🤩
پیمان حدادی: به درستی قهرمان لیگ سال پیش اعلام نشد؛  امسال ۲ همت درآمد خواهیم داشت. خیلی از باشگاه‌ها پول نداشتند. پارسال ۵۶۰ میلیارد درآمد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140951" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👀
❓
چرا خداداد عزیزی منتفی شد؟
🤩
پیمان حدادی: سیاست پرسپولیس و تراکتور فرق دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140950" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🤩
🎙
با اعلام حدادی ساخت ورزشگاه به خاطر نبود ثبات اقتصادی و امنیتی فعلا قابل ساخت نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140949" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎙
🤩
حدادی: یا فوتبال یا یه کار دیگه! بازیکنای پرسپولیس باید حواسشون به فوتبال باشه. شکاری ۹۰ میلیارد از پولش گذشت و آقاسی با استقلال ۶۰٪ بیشتر گرفت. جام حذفی رو هم با تیم‌های حاضر برگزار کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140948" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140947" target="_blank">📅 21:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🤩
حدادی : حتی من لیست تابستونی فصل آینده رو هم دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140946" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤩
حدادی: با همه مدیران باشگاها رفیقم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140944" target="_blank">📅 21:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤩
حدادی: برای آسانی مدارکی داریم که هیچ باشگاهی نداره؛ فدراسیون هم باید استعلام فیفا رو منتشر کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140943" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▫️
🤩
حدادی: قرارداد علی علیپور با پرسپولیس تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140942" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
حدادی : هرکس نمیتونه توی  جام حذفی شرکت کنه انصراف بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140941" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤩
حدادی : اون ۱۰۰ هزار دلار که بخاطر آقاسی دادیم بخاطر پیش پرداخت یک بازیکن بود که می‌خواستیم حسن نیت خودمون رو نشون بدیم و با اخذ رسید اون پولو دادیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140940" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at1ptPcfx2K_qzaHKgm9ftFkGiaxP1PXEp9MT4kXhF4oGLRDxyCGk_PCqxGH7NcH3RSIWzXJ52vkXiOW6mVntDyz9zCCu_EWKZl6BJaCKn9tt58k5ulE_5pyADD47exws6AIbdS5ES5yrPwyDO8RIvthKHv3KZU5ys_l_ZVCzDYCMVx50iS44Zyarv92pTZKoUqUpAC4ubO1mYdni2ZFXt9sAq6qVzpuyIIAC2e5if-R2v-ITXWuUo4KkNZdcNO0CbkZssvM1wu2Wbo2uaEWZFGC78clhd1Z717KdlucvaIionusSyi0KGXYOGkrknwXKXg6N78saKzF22ErPSh2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
Portugal -
❤️
Norway
⏰
Tonight 22:15
🏟
Estádio Do Dragão
🇪🇺
پرتغال در ۳ بازی این گروه ۷ گل زده و با ۹ امتیاز صدرنشینه؛ نروژ ۵ گل زده و ۶ گل هم دریافت کرده، ضمن اینکه پرتغال بازی رفت را ۲-۱ برده است. از نظر xG، نروژ با وجود کیفیت هجومی هالند خطرناکه؛ اما مدل‌های آماری همچنان پرتغال را شانس اول می‌دانند: برد پرتغال ۵۵.۹٪، مساوی ۲۰.۷٪، برد نروژ ۲۳.۵٪. می‌باشد. احتمال بازی گل‌دار و نزدیک زیاد هست و همچنین احتمال ‌می‌رود هردوتیم به گل برسند.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140939" target="_blank">📅 20:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
فووووووووری از حدادی : قرارداد امیر حسین محمودی 3 میلیارد و 200 میلیونه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140938" target="_blank">📅 20:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
حدادی : نمیتونم قرارداد محمودی رو اضافه کنم چون باید به سازمان بازرسی جواب بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140937" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/140936" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
فوووووری
🔄
🔄
حدادی: تا آخر همین ماه یه جلسه مهم برای بیرانوند تو فیفا به صورت ویدیو کنفرانس انجام میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140935" target="_blank">📅 20:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فووووووووری از حدادی : تصمیم گرفته بودیم اورونوف و تمدید کنیم و بعد جام جهانی بفروشیم ولی نشد
🙁
🙁
🙁
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140934" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140933" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140932" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
قرار داد 27 بازیکنان ایرانی تیم 1همت هستش.
🔘
اسکوچیچ برای پرسپولیس بالای یک همت هزینه داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140931" target="_blank">📅 20:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
حدادی : اجاره شهرقدس هر بازی ۱/۲۰۰
🫪
🫪
🫪
✅
بازی های میزبان ۴ میلیارد هزینه میکنیم مهمان ۵ میلیارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140930" target="_blank">📅 20:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140929" target="_blank">📅 20:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=ejtdBAmv5pDQhYQW4-XNx7feKpXqM4eNrl0ZcfxJCMVbGwoMj4-M_jwXmurMBj8CIu9mKChxTEEmOW1dXzW4vCNDwz-qbsqAWnnALXJKkZjbUpzxG0nYMliuYetiJlJp8DHn8Xew6l_En1HRFxm5xIwGwMLqK69xbCzxOaUqCFvbcUCcNyhM6_XiOirkAEoFWj7Ut-BuwojmKErQFye9Nw_cjcuW6QdogiUkLcYJiTmksCPvR2_TU4tEKkNSEQRRG-2kKah6jeWq-P94UOtQoUfBiMU5yEhM_Xq3BtRCgH8qp5Wlt9V_DLNkFeLw89hJIYzQW-TyvI6PXLQMjOmR_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=ejtdBAmv5pDQhYQW4-XNx7feKpXqM4eNrl0ZcfxJCMVbGwoMj4-M_jwXmurMBj8CIu9mKChxTEEmOW1dXzW4vCNDwz-qbsqAWnnALXJKkZjbUpzxG0nYMliuYetiJlJp8DHn8Xew6l_En1HRFxm5xIwGwMLqK69xbCzxOaUqCFvbcUCcNyhM6_XiOirkAEoFWj7Ut-BuwojmKErQFye9Nw_cjcuW6QdogiUkLcYJiTmksCPvR2_TU4tEKkNSEQRRG-2kKah6jeWq-P94UOtQoUfBiMU5yEhM_Xq3BtRCgH8qp5Wlt9V_DLNkFeLw89hJIYzQW-TyvI6PXLQMjOmR_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🎙
⚽
حدادی، مدیرعامل باشگاه پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
⚪️
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت، ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140928" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: ما شفاف هستیم و هیچ مشکلی نداریم نگرانی بابت لو رفتن قرارداد های پرسپولیس هم ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140927" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
⭕️
باشگاه پرسپولیس با خرید امتیاز باشگاه پادیاب خلخال صاحب تیم «ب» شد.
🆕
🆕
🆕
عصر امروز با حضور مدیرعامل و مالک باشگاه پادیاب خلخال در باشگاه پرسپولیس، امتیاز این تیم که امسال در لیگ دسته دوم حضور داشته به باشگاه پرسپولیس واگذار شد.
🔜
🔜
راه‌اندازی تیم «ب» یکی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140926" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140925" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140924" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
امشب پیمان حدادی مدیرعامل پرسپولیس ساعت ۲۰:۰۰ در لایو ورزش سه حاضر خواهد شد و به سوالات هواداران پاسخ خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140923" target="_blank">📅 19:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
اوستون اورونوف در ادامه‌ی رقابت‌ها نقش موثرتری در ترکیب پرسپولیس خواهد داشت/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140922" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
⭕️
۶ بازی آینده پرسپولیس در لیگ برتر فرصت مناسبیه برای اوج گرفتن و صدرنشینی در لیگ برتر
✅
✅
✅
ما ۳ بازی خانگی مقابل صنعت نفت ، فولاد و فجرسپاسی داریم و سه بازی خارج از خونه مقابل خیبر و مس شهربابک و نساجی و با توجه به آمادگی و اسکواد خوبی که داریم باید به…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140921" target="_blank">📅 18:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
پیمان حدادی: خدا را شاکریم که سومین برد متوالی تیم بانوان را شاهد بودیم. سه پیروزی ارزشمند که باعث شد در صدر جدول قرار بگیریم و در هر سه مسابقه نیز کلین‌شیت داشته باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140920" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✖️
تارتار به دنبال امتحان کردن امیرحسین محمودی در پست شماره ۱۰ است.
❌
با مصدومیت علیپور، احتمال داره محمودی از وینگر به پشت مهاجم منتقل بشه تا خلاقیت بیشتری به خط حمله پرسپولیس بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140919" target="_blank">📅 18:22 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
