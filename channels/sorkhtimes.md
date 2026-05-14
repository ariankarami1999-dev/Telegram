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
<img src="https://cdn4.telesco.pe/file/GAuxKi_JId5zHGYTp4CWLmUMj82O__iNgVW9IXX6vJfksc1uwEKPhdIczW5SYNZhlka18zBATBflrMhlXxiYfOWwerm07oVn5n-y28kdktSArKuOO60Kivb7p9yvPHTfsnhWwrL0Rq3otN26mMIw1yXVyXluz8J_c9i_qOocQ02IDc4Tzjd3YKixd2wc-UJKl24OhD1zsnsdP6ky9aRFWJtmP_iF14Th4yBfLBSmZs3pqb7ObtZkunInzy0Hhz21BRZ2SOhQeX3DlfBZpaXO-xv72q9GNZx8ibBaCd8siy6bpoQze_Is_gGGjBkZmrZtJdghiBJPxhoYaaYqZz4EIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdYLmgumIu5t62xHh7OUcWoLd3NQUFDMsx_7ZCt0IpWEQB1A2aOFROUs6NJOHhAXjf7iOx80cKZF2ed0DvCfnHVYFlGOHJrUD4HJfcWLqljJksi64Jx7tidOrZms2MQ_H7P8c3RTfFJ8M3hU37Ueg4srLjaDos32NwdN_HzkAZ2oc-4ylbhY3rLoaBpDrKyMwgROE_-Y1nxceXUdQt8TZIS-6XR3T44BDOoKaqX3Y2bvi_1uSF1yL7WZ_-hhsivV9dsKsIoQPrt43KlZ7DBiN8RcvofNLC_Mz4yEGjY3iK5z5hNbSRgcSTxMTSygDo3Y20SWaPM42O2OKHEXnxYl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی که لیگ تعطیل شده است، او سعی کرده تماس‌هایی را با مسئولان باشگاه سابقش داشته باشد.
🔴
حتی با خبر شدیم که بیرو با محسن خلیلی رسما مذاکره کرده و آمادگی خود را برای بازگشت به جمع سرخپوشان مطرح کرده است.
❗️
پیمان حدادی هم در جریان این موضوع قرار گرفته و حتی به دنبال این است تا اگر پیام نیازمند قرارداد سنگشنش را پایین نیاورد، به موضوع بازگشت بیرو به طور جدی فکر کند.
✅
جالب اینکه بیرو به حدادی پیغام داده که حاضر است با نصف قرارداد فعلی پیام که ۸۰ میلیارد تومان است، دوباره سرخپوش شود در مورد این موضوع در آینده خبر‌های بیشتری خواهید شنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 197 · <a href="https://t.me/SorkhTimes/131627" target="_blank">📅 12:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 297 · <a href="https://t.me/SorkhTimes/131626" target="_blank">📅 11:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMNBgeaY7EFKdLBkK4T01PcXs8nMrvvKlgxitOSYYape5aVducl590ehXjLQSlU1xMk1Ls7IMY2o-O7-QLYKxrNLwUWF3A-6Cu1O6RLr6C1naoYD-L0Nwd3qud60jUOSAy9sKz5Vu3Bag4VVFxw_9vLEi2M3zdEgQTtPuACZnaX-uL6gRqDXj8DI6MXWGd5PeWNXg55viEzGkgonVqt3OmLUGoli_1rZD-mNAyfHsnzb7mJCLS92Qfep_f_fMCNiVtfloThUeTII6OgmI3xWg62MnhDA3WDMGLU0fJLf05oSZ4PZ48OXqbghjAx3ZZ1h0XPO6kXwHdvqo0ZkbEzetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
معین
: قرار نیست واسه تیم ملی آهنگ بخونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 295 · <a href="https://t.me/SorkhTimes/131625" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imnd06OGd9hjAReiUTSE_SblGValyMjHtcEeYKnHFq6-I8IMMWR6jsl_G9PvSI4Va_QjT-DqpLkIQG3iTvuF_LriflUoYg4BH2CJJ-O6v-u6qLLaHzagZPqivGJqc-R24TIh7Vkxfg-KGMo_7QA34bHbTbg4C969sWrj3WdPjfK28nvjRtmKVWOkkBgVYHB6TFrmcBJ0OOUG6UHZfBBsEX2YyrrpZa_xwRJWNaaTg9gVjW9IfVcJBrjY_Boz60Nei41vkNL2Zgjcxb6b_24sGN29bO53CxLlL4xMvFtWOMqDbCY2OLI95BD4wBPIbNs041I_8spB0_hfDqOr-wNL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اینکه مدیران پرسپولیس بتوانند از لحاظ مبلغ قرارداد میلاد محمدی را راضی نگه دارند وی به مدت دو فصل دیگر با پرسپولیس تمدید خواهد کرد و درغیر اینصورت به لیگ ترکیه یا لیگ یونان سفر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/SorkhTimes/131624" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD8D1haQ2OFY1aM6lw4sInqPGv0nWTEQQp-k5JyNMqdT7bmi8WfnP0b3whze7Ljrf2_CFW9HMORwhOuHfsRAAZKmOS9MYt4fCnFX9QF8-IQqtN54ueo6siSfL-PxmcK0UnROUiiVuYIKjaaw3uXTNrB4usSTI2VKMjLnok52Frph2LFOi-T-1QK4Qo2miOPOvoLbOwEKl72_R4uEN96jBCNRS4FHsl65ENyluvlB0ddbQXhRJnmTSaQvW37cpdUAOY3Emmijs1LHE_oDLDoca10t326xijFkejtYHppshQAHjJu6PhvrrAM-jtfsKIDQePrXeUmN84p_iCq8qTa7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تسنیم: قرارداد باکیچ به طور خودکار تمدید میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 303 · <a href="https://t.me/SorkhTimes/131623" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx9-v-rv58_CEAARuj4zWQUagAz0sWkobXbZfiZF9C3J3WxiW3JpN5IRtqzuNXlokCl1VysoAVaiXwfVLjtp4Ug5JRiyUHXq4D4k0MW8i5Bn-6B_kcuxGzsDcqYeIc4NZYGgeRzhBC85h88Zx2hnSDQKklO9obE6aTgXaui1ASMTtEK8hdgmA0p-iJB9zAX0GeHkQ5_hk8dcbFbCxRjjZC-_Ogo6PCV9OhVOTngRKEzpLqUK92YIlctxXqHcOUaJxOjuQOYot-fyba5IJdjUU6uz65yfvifS5_UcrhZd6o-MOFqRNrwL1tY_vPchAXzv9cqyE2AbTCNBApdd7APS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 561 · <a href="https://t.me/SorkhTimes/131622" target="_blank">📅 02:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🛜
یک عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/SorkhTimes/131621" target="_blank">📅 01:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🛜
یک عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/SorkhTimes/131620" target="_blank">📅 01:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm0jfb6bUjk3v463OuoojNQsd7NJwV9mUBYsXIlCK9vBqUOqAdRmmLJBCkSgM0lMan7lZJFBrLYhyb3oJjQXhxIPTMJtfLHHj9n61qrBu5CawQIEnwrrudW-LZ8ihKY0DpxvfrVXuRSDYNuFYrZl7tI306y538d1Q4quadf0nqH-UwEIAaQj_2UX4RKjTrdEDyMUs7kVdTt8KIMWtNYS8HdqAbXowQaeO3uEgXrQkwcrePnLpSQtZ9ja7hKrvxaYWeHxeYchEgt_fTnELUno71hAUGfbVemu-hZ30ZQ6mf8p9lPjOS6S_OcUQ935GBKa_mXsDbxJujI2RMtw3bPvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مهدی تاج: شنیده ایم معین برای تیم ملی تو جام جهانی قراره موزیک بخونه، ما دخالتی در این موزیک نداشتیم ولی ازش حمایت می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/SorkhTimes/131618" target="_blank">📅 23:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5_v-fwnCYfGTy49tdpXpMoeangG4rlCuXFS3MlQo_SEpbLdpMoFuvoZqrQQueZ4F1kUQWKexhKNvrWBgymBUraDWtKT7oxTLjRwrj4yyJzxaYXQgaFU8FFFi6pBIat1EpUq-rouhin6STHoX-nFpehDpkM4bJWToK1orW26LJvdCl22VAcOd9TY4tll24eymUn3jXxUly9TS__FHnHG5Jro7W4naeCCzu5oFSXS45nYlhIfPNS5qz9vvQpGdTiZ8ecmOLnDaofJlVd166lMI7uteKEQJBWMF0Hq9LS3diUZv3QMP6MuPJo3jGMnMqlz1aqJ3zg9Z9b49RD_zghzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
از کیت جدید تیم ملی جام جهانی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/SorkhTimes/131617" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/SorkhTimes/131616" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwLlDnnjQ2LhSpBCOiyR60Z4v7xj41mvzQsnz-h0ccAX6RaIHe_1hBO7ewCaS_rPPNeqgGRIbU7yAfJY5dqBl__D2XaO317bWtMjRnwtCdteZITVcRHNNUv3oN81z-4_KRaqzxB66k68QzHyZ-nKWjtys_zPVlB3DP6CqZi21o_7rmGqeYk_dO2fqfK1COSvUHeZ4jM_JsdCn2hYw9uEXOJ3dK-cvm_0lgdvZOpqr2QDN6r7pIKSjyQzUT3YmBF2hWyXZbQNuzXDvx9hKYZ0vxCeab859hOXE-p51G-sSp3hixIUTHNh2ecSmpKGNJmhN2Csxs8EG4YVZs5webfOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/131615" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7EX0hLmqVKbrRKDf1x8O07HZ8sE1Jx4m9QO0GMdgqs8hpEhzG3AagAZBYhKMZt-CbCRSEDav5vh5hgRq2CdwJkwrwjc9pZP75fvxXDRyVfR54M7fHlJq5yagDteVpnbsspG7kvt3vJwS2Tpn2o3Z9Db9nou7euoDb_ONIA7y1-_EluXu8cc-jDT2qSeRf7-T1nKLWbQMH8_m2-xLTF5k30OSgCB3Ci_D-GEBq4ATq7esVnOpeeKkj-ailCfuJFJRuExbIfEXCWT9AQ-cCJUjKNulW6HmQcBKYH1VLh5RkYErDT5jt_PFjMQ0fljn5CNGHkmJ8sy7_2BAW1bFtif-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنای تیم میلی کنار پزشکیان عکس یادگاری گرفتن و راهی جام جهانی شدن!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/SorkhTimes/131613" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
معاون اداری و پشتیبانی وزارت ورزش و جوانان اعلام کرد که برای حضور قدرتمندانه تیم ملی در جام جهانی ۲۰۲۶، مبلغ ۴۰۰ میلیارد تومان بودجه در نظر گرفته شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 707 · <a href="https://t.me/SorkhTimes/131612" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
توافق پرسپولیس با مهاجم تیم ملی فوتبال ایران/امضا قرارداد قبل از اعزام
🔻
پیمان حدادی مدیرعامل باشگاه پرسپولیس پس از تعلیق برگزاری ادامه رقابت های فصل جاری لیگ برتر با اوسمار ویه را سرمربی برزیلی سرخپوشان پایتخت برای فصل آینده به توافق های لازم برای تمدید و جذب بازیکن در پست های مهم رسید.
🔻
حدادی در نخستین گام برای حفظ یکی از مهم ترین عناضر خط حمله این تیم پای میز مذاکره با علی علیپور نشست تا مهاجم تیم ملی ایران را که از مبلغ قرارداد فصل جاری خود با سرخپوشان ناراضی بود به تمدید آن برای دو فصل دیگر متقاعد کند. نشست هایی که بالاخره نتیجه داد تا علیپور راضی به عقد قرارداد فصل آینده نیز شود.
🔻
مدیرعامل باشگاه پرسپولیس تصمیم دارد تمدید قرارداد این بازیکن را قبل از اعزام تیم ملی فوتبال به اردوی ترکیه که هفته آینده خواهد بود، انجام دهد تا اینگونه نقل و انتقالات تابستانی سرخ ها را آغاز کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/SorkhTimes/131609" target="_blank">📅 19:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/SorkhTimes/131607" target="_blank">📅 19:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 703 · <a href="https://t.me/SorkhTimes/131606" target="_blank">📅 19:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbXUgQD-Z8EUXPc5caJMg1jYhIYwgt44fkkNzp7se4vk9ac58CJAi0RYfjpGRZOCqr9p6eG8bv46fLzjobnmrbDvLdJntzhIRBKyJeK9oP1cj09FgPt7Va3isxd-xU7EK6ElpGH51XsolrP4z7I2c-5lWEhz4mtEuGuDsMRJ9PjXiotTWjWB64VRNSs__FgcI97wg_XxNcJ3WPjASk1jYyg-BXHrtfalcZjoPBeZuTG5drBQ4fpRHnyuwNA7CV4ENxO8299YPVvTSLwwi3MoAqidJ8kIfZG031_nfkvPhJgHihPzV7fDNCmxy80kQNwrWApymakavDCPJQYbPm2ECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت علی بازگشا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 745 · <a href="https://t.me/SorkhTimes/131605" target="_blank">📅 17:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♨️
🚨
نیویورک تایمز:
قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید 60 روزه حمله به ایران شروع کند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SorkhTimes/131603" target="_blank">📅 16:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131600">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ0Pl5nw6Qale1ADqo35nkHqwaU7GBEwYX3m0rGvYl0mW3xt8nmdxRoMO_r9Ewtz57TXzcMknBDufwZ8zYNBfFWzhiMXtkMaJkLktN_G3xsEd1eDb8vS2OlFz7dJLveR0ltMS7AVz0WnZL626o_SRDLI5YEDeA7kBV2YOO5eUZ_ldmvzzUusjI8qivW36Sgni-2yu4NeCaIVErjdFSm6xY1Ue7i9_zL6hKkATGyhpCYWZbf-XQFk0Ju0q7O7aEEf_X66Pf7NsoaXBkvWROWctkDGxZKS2jqv0XAs8JHR4pI6tooh_MWnUzezjEAW7vztwt6NnfGj72L1lgnsbXrBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
قرارداد علی قلی‌زاده تا سال ۲۰۲۷ با لخ پوزنان تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/SorkhTimes/131600" target="_blank">📅 15:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwJr0hax98Vk7QZyw5D9Mo7A1ROlhPW5e5oXhrOtq9oP71q5rxyecoHLs9aNYKGgssBJqAZgsM5PiOaljHyufbiCS3X9gUq1WvJfKbrCIKijOHl7eyJnUxeAwEUcwgKnnJEVqUqbK5GSMXG4jxjrEoVRrFoHOGbamX6Yz3Nts7ov5rgQungiwpr6jNN93vr73ve3ba21PJul0oGmwTq8Kj08Vlt6yAbtG2whMj-Zyj3rrWdrRi3Wg6DD5C1Cysp5YGdRJczOHfwPT5gpxP0mh7vlv0FQiipudqojKyqebKBYsn4RIZOrORw4fm_7koTg6-72LTmsgpGnVxa1h8dksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست
مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/SorkhTimes/131599" target="_blank">📅 15:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfW5EPoyEA3j72k6TtVEy9CJzbE3_WFvYAHRKyVMCLEsrm-AFlmqa-a9WJx_BtAqd3ozAtPEy-jNcGDGARkLAy6RdRShKRECr5dp_h5PD81yQKhgMzKYY3hHe2LAQJKg4vKqirQyIPeyeAUGu1cCveEZgvefgGh-7L1QeKDmW5UVPL9qJOi5L7SKUzQlaxaJ9Wlin9f6AESTHHqS7Emc5jx6TxYxueM_9bfu1cjmCTxyn0v1aYxy3-LDM9nTGqCyi3xoX9ZsQr8r2oaWq74gixagkBSf4MxndgTXOMluWefSEBQFfNUvUNCcsTJZrqF9oJ3nYDlOe8Y8iQ5pBYq2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها و ورود به کانال وینکوبت همین الان جوین شو:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/SorkhTimes/131598" target="_blank">📅 15:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
کامران غضنفری، نماینده مجلس: شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/SorkhTimes/131596" target="_blank">📅 13:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
ترامپ رسما اومد گفت انقدر صبر میکنیم تا ایران تحت فشار مجبور به توافق بشه.
❗️
یعنی ممکنه تا شهریور تو همین وضعیت بموییم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/131595" target="_blank">📅 12:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/131594" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔴
شنیده‌میشود محسن‌مسلمان فوق ستاره سال‌ های نچندان دورباشگاه پرسپولیس بزودی به کادرفنی این تیم برای فصل بعد رقابت‌ها اضافه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131593" target="_blank">📅 11:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHM13vUBscPmMqRcDBYZNw6vaQVST5uleaRp_ew25S7sgLIU29Rr01f4_hjjo9VRG35MbjPcHjRtv1dGBQwJmsTZ2_IJVsyL1N8iobLoGVCX9JgBTOYqpu2neW7fpLS4OPKeQaTUd8OlPn_yypfVTl-UHXyPZcAv_00NV8OvTVuW_UVYAcSXoRLR38ghz1VUi_TSVroP7q58lCzj3-OWPcBH6q22YHA1IVzYKN5UqjMpYA41nu3WeaXKKl1mgj65H0wwGkxaJwHbLOyzYP6IQU4kGT9Bqbo3sOib8zLX42bNyPyFeu_Wcgb0YAdHmKZ1Tcco8nUUCqKToFKib7cyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پپ گواردیولا:
من بی طرف نیستم من طرفدار فلسطین هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/SorkhTimes/131592" target="_blank">📅 11:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
🔴
مارکو باکیچ تابستان گذشته با قراردادی «۱+۱» به پرسپولیس پیوست که طبق بند الحاقی قرارداد، فعال شدن سال دوم منوط به حضور او در ۶۰ درصد مسابقات رسمی فصل اول بود. با وجود مصدومیت این بازیکن در اواسط فصل، طبق ماده ۵ آیین‌نامه نقل‌وانتقالات فیفا، مدت زمان مصدومیت از مجموع مسابقات قابل محاسبه کسر می‌شود؛ به همین دلیل باکیچ از نظر حقوقی به حدنصاب ۶۰ درصد رسیده و قرارداد فصل دوم او به‌صورت خودکار فعال شده است.
🟥
در نتیجه، قرارداد دوساله این هافبک مونته‌نگرویی قطعی و لازم‌الاجرا محسوب می‌شود و ادامه همکاری او نیازی به تمدید یا توافق جدید ندارد. همچنین اگر پرسپولیس قصد کنار گذاشتن این بازیکن را داشته باشد، احتمال محکومیت باشگاه در دادگاه CAS بسیار بالاست و باشگاه باید کل مبلغ قرارداد را پرداخت کند. از سوی دیگر، تاکنون هیچ نوتیس فسخی از سوی باکیچ به باشگاه ارسال نشده و تمام بحث‌های مربوط به «مشروط بودن» قرارداد، با مفاد توافق و استانداردهای فیفا همخوانی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/SorkhTimes/131590" target="_blank">📅 09:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FthPax5d4ymQ8YsyX_Fl_HUzelloNKHWNKvDgdUzvw1YOklg2HICb9bgMFBiKrr40LyMosqQdOUnx-SYJ_rl7fe0H-_Np18XG4F7NRsGLgctu2oX92cKcrFcQ2QkxwPIqU0sWEsvjNRgduXfBMcKBIsYp35ygPvt9yxwLsWd7avSgXEY5_wuP79MLIhxrcpTLoeeaKVAE0nyna1Ns2zBmzeZSp7oP4C5pNco9b4cAAeIHvLYFmo2q1wuw9DS5ENYucCgFORNdedGDISH9RO67Ft64Z9t1dkpdbRRYLLtiTRCIh-OUVpDGDjmIVdk3cFRIDAF0cnm-7oPQqL7XYV06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131589" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
همین زلزله رو کم داشتیم وسط این همه تورم،جنگ‌ و بدبختی، فیلترینگ و قطعی اینترنت!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/SorkhTimes/131588" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران   بزرگی و شدت: ۴.۶   محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس   زمان وقوع: ۲۳:۴۶ عمق زمین‌لرزه: ۱۰ کیلومتر ۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/131587" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GmQd6HxE2jO5U_UFfnugLljS0I13sL_h-R3i7YTkTR3oy4Cf_tqjEc3Oj2qETGOOygy87qr9vlhvCDTNgsbhTJtVIu47sYwmhmQ7yTMeAwPY5EJHQjlijJZYkqpLlxz6xUMdFGdS5B8QFJuKnLz0AU_wFDdOx7lXX4v0aVcsG8tOttsaPxk_v3yzKN-IPmuksadaz_OB0OJR7bsdIZRRg-98GQ9TZejL3HI4FlmI6Rd5umNV229pDW10OJS-mg40CrEvu4TsdNwyGuzeJnB6CiO5jznRP16utnMvAm5_InRUJiyO1872rFzXd2sNXlmdg09oPH03xe8mZSCqkmelrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران
بزرگی و شدت: ۴.۶
محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس
زمان وقوع: ۲۳:۴۶
عمق زمین‌لرزه: ۱۰ کیلومتر
۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/SorkhTimes/131586" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل:
🔴
انتظار می‌ره که ترامپ بعد از بازگشتش از چین در پایان هفته، تصمیمات نهایی و جدیش رو درباره ایران بگیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/SorkhTimes/131585" target="_blank">📅 22:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/SorkhTimes/131584" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی: ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن…</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131583" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=Z55fnrwthORrxP7khWGcnk803O7hWHdOygTowXL-xvxEWVGOJE-1DEwsfwNlNA9nRPGRXLg32bTMjk-w_9GYHvtE1rwKiJqfv96EHWWx5g-vJzMnFWcVl2w1FwSnrzdoDYBV_ekFMsyDM2u_wFVv8-mxNSmPuFV27IdYEx_OF7Yh5HmpuoJZ8hlke8td2paB5c_KixrI-U65iNsii4dFn3_6wY6Cbq3J5lysDRKJnZgocuStv8CRoVKoeJu5PzE7o8aJxvTrfBrKl4Gamm4iQKO6DDb2WQ2jOWIIg3pkmU_V1L0iXrfio_DMGaC9UNAQ9QqTHXe5nLJQESAMesVTlXau9MSn3FY1tkaqxxXfiWKGIF9iefCgC3HqLbizz6IrZnmo82uLb17YAimIH90GPu1I1476ZOA6rMw2zkUJ8Jwx4QJN0TVjcMGn70FbB8sTa-hWnM2O8qzGzReLefsj8DqSyJitleHqnKbxwKwXKZxGijUy9YMqozc8lEUSgSzKC6kBP3PAIrwW2l54KlPKTImGTwt2rjrY7HwjBH8oAYS8-90M7f4hr3tXhp22d3f6b8dQ6GPMedPhtOkPD1nGJVuQO_0bQ-B8Rz2I2zhkR8TmfGbcTGpbIsLW-Du3AVlktJfCmI3bmEsezfncKqJcFBSsBDp4TsScxcD-156WmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=Z55fnrwthORrxP7khWGcnk803O7hWHdOygTowXL-xvxEWVGOJE-1DEwsfwNlNA9nRPGRXLg32bTMjk-w_9GYHvtE1rwKiJqfv96EHWWx5g-vJzMnFWcVl2w1FwSnrzdoDYBV_ekFMsyDM2u_wFVv8-mxNSmPuFV27IdYEx_OF7Yh5HmpuoJZ8hlke8td2paB5c_KixrI-U65iNsii4dFn3_6wY6Cbq3J5lysDRKJnZgocuStv8CRoVKoeJu5PzE7o8aJxvTrfBrKl4Gamm4iQKO6DDb2WQ2jOWIIg3pkmU_V1L0iXrfio_DMGaC9UNAQ9QqTHXe5nLJQESAMesVTlXau9MSn3FY1tkaqxxXfiWKGIF9iefCgC3HqLbizz6IrZnmo82uLb17YAimIH90GPu1I1476ZOA6rMw2zkUJ8Jwx4QJN0TVjcMGn70FbB8sTa-hWnM2O8qzGzReLefsj8DqSyJitleHqnKbxwKwXKZxGijUy9YMqozc8lEUSgSzKC6kBP3PAIrwW2l54KlPKTImGTwt2rjrY7HwjBH8oAYS8-90M7f4hr3tXhp22d3f6b8dQ6GPMedPhtOkPD1nGJVuQO_0bQ-B8Rz2I2zhkR8TmfGbcTGpbIsLW-Du3AVlktJfCmI3bmEsezfncKqJcFBSsBDp4TsScxcD-156WmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صالح حردانی میگه ملی‌پوش‌ها از سربازی معاف بشن تا با روحیه بهتر فوتبال بازی کنند!!!!
◀️
شما چه گلی به سر کشور و مردم زدید که درخواست معافیت دارین؟ کدوم قهرمانی رو آوردین که اینقدر وقیحانه درخواست معافیت دارین؟ چرا یکبار درخواست شما، رویکرد مردم نیست؟ چرا همه چی رو فقط برای خودتون می‌خواهید؟
❌
جز اینه که هیچ جای دنیا چنین پولی رو به شما نمیدن؟ هیچ جای دنیا به چنین ثروتی نمی‌رسیدید جز ایران!!! باز درخواست معافیت سربازی دارین؟
🔴
چه تفاوتی با یک جوان کارگر ۲۵ ساله داری که اون باید بره سربازی و تو نباید بری؟
⚠️
تازه سربازی شما که مثل بقیه مردم نیست، میرید تیم ملوان یا فجر و بازهم فوتبالتون رو بازی می‌کنید. خبری از پادگان نیست. چرا همیشه طلبکارین و سیرمونی هم ندارین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131582" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/SorkhTimes/131581" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/SorkhTimes/131580" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=J7eEUuZCw6dzZ_JpXp-8ynpdJa4U23hXRQJSC39U_rmTtDh-9OXNLhmkkUYk8r5KMDtJ_FRuoFe-t9usQdeoNStLc5IZTBWmEIpZZHnGBQO6rcumeJFnLMG-W1ME90gfdDNXneziOU09SzBj2hSFboSYVcY-r3VWhzASvImAVB3QPjemC6ejMN7wzh-U7h0Nnji5jpUit3b8shLH9zlIR35u4BcncjL6kegVlOUc5jBFRso4CWZY1W1siJKP71WpJT_aDsxZFb7jJIxKdrhXn6VFktrAd2hdTwwUBjeFzcmSZWH12zKK6QVa0A2LmMsQCH2GvsQOpk2kNCY-bKqSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=J7eEUuZCw6dzZ_JpXp-8ynpdJa4U23hXRQJSC39U_rmTtDh-9OXNLhmkkUYk8r5KMDtJ_FRuoFe-t9usQdeoNStLc5IZTBWmEIpZZHnGBQO6rcumeJFnLMG-W1ME90gfdDNXneziOU09SzBj2hSFboSYVcY-r3VWhzASvImAVB3QPjemC6ejMN7wzh-U7h0Nnji5jpUit3b8shLH9zlIR35u4BcncjL6kegVlOUc5jBFRso4CWZY1W1siJKP71WpJT_aDsxZFb7jJIxKdrhXn6VFktrAd2hdTwwUBjeFzcmSZWH12zKK6QVa0A2LmMsQCH2GvsQOpk2kNCY-bKqSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/SorkhTimes/131579" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔻
فیفا یه قانون تصویب کرده که بازیکنای خارجی که ۳ سال سابقه حضور تو لیگ یه کشور رو داشته باشن، میتونن واسه تیم ملی اون کشور بازی کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/SorkhTimes/131578" target="_blank">📅 20:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3vIHYjWbZc27KdDKR4xN4oGOI93DTKBupdePfLtsv20yNkw-xEiw7a_lvHpQ4ge7Y9cciDLbKsoWP-tbv5XWjMOgVJEm4eCJfLiqgQJM5uvhP-Uhtuo70hbvzQj76K9oLhYiERo4sK6VUOOD_IkFC_A7XDYHGtghHLk7gM9pec1ffpbcX_yzxTmYb_8_-y1slnC-2Kphq3j72oKqeM2qnTPryNceG-lFdnq5S7mMX1NTW4ihJyVek7z3-EAjYtYfy9NtG3k0_7JcHGQaYY1dqRkb2vBdDOAJEJv5t_P0Fe7S0KRmAxwf149q_lF5McB-pWX-EqevAy0vzHGSj5HLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
پزشکیان توییت زده قول داده اینترنتو وصل کنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/SorkhTimes/131577" target="_blank">📅 20:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
باشگاه پرسپولیس کارهای تشکیل تیم دوم خود را انجام داده و «پرسپولیس ب» در لیگ دسته دوم فعالیت می‌کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/SorkhTimes/131575" target="_blank">📅 18:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚪️
تاج: تیم‌های راه‌یافته به لیگ نخبگان و لیگ قهرمانان را انتخاب خواهیم کرد
🔺
شاید بتوانیم مهلت معرفی تیم‌ها را یک ماه عقب بیندازیم.
🔺
۱۴ تیم مخالف برگزاری ادامهٔ لیگ‌اند؛ موافقان پرسپولیس و گل‌گهر هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/SorkhTimes/131574" target="_blank">📅 17:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6YetX6O_r8RakLWOcoPztD-SckXcceWkkB0_Aed8c0Mqu45H_GPNL_yXFnpqpSJNOBQx8NZD11yyViyZlvDNh2nnnqaMpNhyVB-IczjdexjKqScmavesD1oLkzroTtpw2kL2iUgXXnnjRGuM11iKV87-SMMVQbcKcTI6oFMLY90D9XH-X2acRLaIGA2JYod0IIrwW-lQuNxQ4jDAuSAFig_VvNVKJFd8yZrozIt17o47qw2iFeAz8PlTzzOBTFWcbSCnJNelpDIwLTeSzcl78ufjBoNSzSas1jP5X_1aAYQzf-fGgAbB7jGdL4eH9nCGgyHjsYNOUjqgWhLCx2oMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اختلاف میلاد محمدی با مدیران باشگاه پرسپولیس تنها 3 میلیارد تومن است و مدیران باشگاه پرسپولیس قصد دارند با پرداخت این مبلغ قرارداد محمدی را تمدید کنند
/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/SorkhTimes/131573" target="_blank">📅 17:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/131572" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/131571" target="_blank">📅 17:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDlzHd59UMo6RRjzoZu_WpZxTmu9zzcNzdYy_LyHpOVDwmZ2YcpcUK07Xa8M9-EECWbiELYWEhGBOB7gpN00lxcpAzsyay4zQfe510tvzDitK0piDmi_wUxNEYeTywcKV8rGyMXtEWLriOaMsYq_5h-Nug9dzMROcGy-8yjLS1ZDfNQP4y-8gaDx4GDwKR5dBFgDSpC4U2-04Oc_oq8FQHS-jpaWCiwrgocn3NDpUvK2AMpb0PRGb8F_FureoyyFV9PtL4eoH8zkr8CO3EwSjCgoiuqJ2VYZEd4A0aHl_czHx3T0AQnAZwnH5Z26BEeiIEZKZ313A8VN1gAUNDd6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شباهت عجیب لوکاس برالدو و محمد خدابنده لو ستاره های خط هافبک پرسپولیس و پاریسن ژرمن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/SorkhTimes/131570" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 726 · <a href="https://t.me/SorkhTimes/131569" target="_blank">📅 17:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/131568" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚪️
ترکیب دو تیم تیم‌ملی برای بازی درون تیمی
◽️
تیم سفید: علیرضا بیرانوند، دانیال ایری، حسین کنعانی، علی نعمتی‌، رامین رضاییان، روزبه چشمی، امید نورافکن، هادی حبیبی‌نژاد، مهدی محبی، آریا یوسفی و علی علی‌پور
🔻
تیم قرمز: محمد خلیفه،‌ شجاع‌ خلیل‌زاده، عارف آقاسی، صالح حردانی، احسان حاج صفی، عارف حاجی عیدی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، امیرحسین محمودی و کسری طاهری
⏰
ساعت ۱۸:۰۰
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/SorkhTimes/131565" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131564">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی:
ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن کسب و کار ها با اینترنت پرو چیکار میخوان بکنن رونق کسب و کار اینترنتی به مردمه.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/SorkhTimes/131564" target="_blank">📅 16:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131563">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شهبازی مجری شبکه 2 : اگه اینترنت،تلگرام بدون فیلتر و مستر کارت میخواید و این چیزا براتون مهمه،برید همون سوریه،عراق و افغانستان
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/SorkhTimes/131563" target="_blank">📅 16:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131562">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
پزشکیان: نمیذاریم بعضیا از وضعیت جنگی کشور سواستفاده کنن و برای مردم مشکلات اقتصادی و معیشتی به وجود بیارن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/SorkhTimes/131562" target="_blank">📅 16:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131561">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
وزیر جنگ آمریکا: اگر لازم باشد، ما برنامه‌ای برای تشدید اوضاع در ایران داریم!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131561" target="_blank">📅 16:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQJFm70TvNI5Kbl0YC3Ho04v2ToLCeegQGJX4CSNLipd5rGMtTvQ9_Q79BrWtc5PAy4ULUyMq5LLpL4aFENkoaPJYTuBBXPMXVviosRr6UOyclEY9vkR33r7f_46_lk-WRQeHv7eUjZlZoq4ifl0CxmElDq1SwQ5P57z95gIighyA4asEyMF3g85ArOeKiAV6iFUs-1yp5pAde2H6aHPod74aIGXh2_6fNDgHW1NUlPAFIKsYXAivOszfFsPDCGgC2ZtrqYTO8Hi2YyMWwEOG-Si-fJH1fHyiipFdNkRId0yjCFgrKYmVYbC9ITfbCDvq3VOUjCCCB0fyQH5YqW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131559" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NscXFCnTh6_NmyQBO0tIYDeNeAKNnRrOFCI0-C4jSGM_HZwD6_1T-ZlvOYK8DjwC_q7s1siT59FIIBi5TiCsGZKaAQeiYyZdIXwDwPj33vnlbShR2B3Kgm1RtKoYU_UseFBjMUPH1Cy9MRl6eJWYA3GFLAAg-_aqCesYd7C1vE3On6PWHvxzVStgTe7YZFA3N1Up_g_EEXNjOdLkbgZMFU2JLmKEU2nDgE7FrqfMlVV95B031xbcsuuGfP44u5-qfX4jTK3Wwi6LQQrYqmygo5VioJmIdVdiMxmS0leZq4DzaE-q55c65-WwybY60QgvdsFgQyu5fr1k5E5jLmMkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان،…</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/SorkhTimes/131557" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان، یکی از باشگاه‌های مطرح کشور، به دلیل مشکلات مالی و عدم توانایی در تأمین شرایط لازم برای دریافت مجوز حرفه‌ای، در معرض خطر قرار دارد.
🔺
بعد از آسیب جدی به کارخانه فولاد مبارکه، سپاهان با مشکلات مالی جدی رو به رو است و هنوز نتوانسته مطالبات این فصل بازیکنانش را تسویه کند و احتمالا هم با توجه به میزان خسارات وارده، حداقل تا پایان سال بعد، قادر به تسویه طلب مربیان و بازیکنان داخلی و خارجی اش نخواهد بود که همین موضوع قطعا بر روند مجوز حرفه این تیم تاثیر منفی خواهد داشت.
🔺
از سوی دیگر شرایط اقتصادی صنایع مادر باعث شده وزارت صمت نیز محدودیت‌هایی برای هزینه‌کرد باشگاه‌های صنعتی در نظر بگیرد؛ موضوعی که می‌تواند برای سپاهان، گل‌گهر و چادرملو دردسرساز شود.
🔺
نکته قابل توجه دیگر هم این است که با توجه به وضعیت منطقه و کارشکنی مسبوق به سابقه از سوی کشور های حاشیه خلیج فارس
،
قطعا بازی ها به سمتی خواهد رفت که رنگ بوی ورزشی نخواهد داشت و این بازی ها یک میدان است برای دفاع از نام و اعتبار ایران و حفظ ابروی ایران بسیار مهم است.
🔺
در این شرایط، انتخاب نمایندگان مناسب برای حفظ اعتبار فوتبال ملی اهمیت ویژه‌ای دارد، تصمیمات فدراسیون، در روزهای آینده می‌تواند سرنوشت فوتبال ایران را رقم بزند و بر روند آینده باشگاه‌ها تأثیرگذار باشد/ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/131556" target="_blank">📅 00:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری ؛ ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131555" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🎙
میثاقی: امیرحسین محمودی با 5 بازی لیگ برتری جوری درخشیده که الان داره میره جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/SorkhTimes/131553" target="_blank">📅 00:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131552" target="_blank">📅 23:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
میثاقی: کارهای اعزام تیم ملی به آمریکا برای حضور در جام جهانی در حال انجام شدن است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/SorkhTimes/131551" target="_blank">📅 23:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🛜
معاون رئیس‌جمهور: نظر دولت بازگشت اینترنت به وضعیت عادی است
🔹
حتی در شرایط جنگی هم بستن اینترنت راهکار درستی نیست، چرا که دیدیم وقتی اینترنت کامل بسته بود هم ترورها ادامه داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/SorkhTimes/131549" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
ترامپ:آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/131548" target="_blank">📅 18:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
ترامپ:
آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/SorkhTimes/131547" target="_blank">📅 18:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHG0UzkKBisTA8hl1zHSpnj_IkgdJTOAvGUK2_dJBowbX4qXs16UtqgxuMfTLq4ReuD3C0BBzlLeMHe8QgxgC7lUnXJj2rx6z0ctblFZkFeS-LvcdmF4rZDO3Z4qlshkJ-ZHGsabk0ZyGMnY35NhiXfOf9F6lZRHUQZgTngIYWLUITE30tiDOPnhmIZczpMbcs1HNaxPJwsKv1cU_p7NS5MMiu-rzCXrNa-cct1wlvVwytpWWxU7DG65UcNt9DZWkb7xJM_D3pT4zw5OiiOnsZSwO_R6WeUApmhcmTmSt6kvlLDHvLh3sR8OT2gKrtubnAQAprewiDX_w3WnIKAeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/131544" target="_blank">📅 17:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/SorkhTimes/131543" target="_blank">📅 16:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/SorkhTimes/131542" target="_blank">📅 16:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 739 · <a href="https://t.me/SorkhTimes/131541" target="_blank">📅 16:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 767 · <a href="https://t.me/SorkhTimes/131540" target="_blank">📅 16:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
هیچ فردی به کادرفنی اضافه نمی شود/ محمدی و رفیعی بازیکنان ما هستند
🎙
لیست مازاد در پرسپولیس شایعه است چون ما هنوز ۸ بازی دیگر داریم. میلاد محمدی و سروش رفیعی بازیکنان ما هستند و چون در تمرین غایب بودند جریمه شدند
🎙
با شروع تمرین در خدمت آنها هستیم. سروش رفیعی یکی از کاپیتان های ماست و حتما مسئولیت پذیری او باعث می شود در تمرین شرکت کند
🎙
از یک ماه قبل از شروع مسابقات تمرین را شروع می کنیم. در حال حاضر هیچ فردی به کادرفنی اضافه نمی شود. برای مجوز حرفه ای شرایط خوبی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/SorkhTimes/131539" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🟡
نتیجه‌ای تصادفی یا سناریویی از پیش طراحی‌شده؟
▪️
سپاهان در دیدارهای اخیر خود نتایج عجیبی را ثبت کرده است: تساوی برابر گل‌گهر (دو بار)، شکست مقابل تراکتور و پرسپولیس، و بردهای حداقلی برابر چادرملو و دیگر تیم‌ها. این آمار بیش از آنکه تابع منطق فنی باشد، روایتی متفاوت از لیگ برتر را به تصویر می‌کشد.
▪️
در پشت پرده، پرسپولیس سیاستی شفاف اما بحث‌برانگیز را دنبال می‌کند،تثبیت سهمیه آسیایی خود، به شکل ممکن فوتبالی. برخی فعالان فوتبالی بر این باورند که هدف اصلی از برگزاری لیگ چیزی جز این نیست و نتایج اخیر تیم‌های مدعی در برابر سپاهان، نشانه‌هایی از یک طراحی نانوشته را به هواداران نشان می‌دهد.
▪️
اکنون باید پرسید: تکلیف معرفی نمایندگان آسیا چه خواهد شد؟ اگر قرار باشد تیمی با لابی و سیاست‌گذاری راهی قاره شود، احترام به ماهیت رقابت‌پذیری فوتبال کجا خواهد رفت؟ فوتبال ایران سزاوار شفافیت است، نه سناریوهایی که اعتبار مسابقات را زیر سوال می‌برند.
🔺
سپاهان ۱ استقلال ۲
🔺
سپاهان ۱ تراکتور ۲
🔺
تراکتور ۱ سپاهان ۰
🔺
گل گهر ۱ سپاهان ۱
🔺
سپاهان ۱ گل گهر ۱
🔺
سپاهان ۱ چادرملو ۰
🔺
سپاهان ۰ پرسپولیس ۱
🔺
پرسپولیس ۲ سپاهان ۱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SorkhTimes/131538" target="_blank">📅 16:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
بزیک، مدیرآکادمی باشگاه پرسپولیس و سوال در مورد همکاری با مهدی مهدوی کیا: من با مهدوی کیا مثل برادر هستیم و شروع کار ما در کیا با هم بودیم/ او اکنون با تیم بزرگسالان در امارات کار می کند/ لازم باشد حتما با مهدی مهدوی کیا کار می کنم و از تجربیات او استفاده می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/SorkhTimes/131536" target="_blank">📅 15:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🟡
حذف سپاهان و سفر پرسپولیس به آسیا
🔺
فرمول جدیدی که از سوی مسئولان چند باشگاه ارایه شده، احتمال حذف سپاهان از بین نمایندگان فصل آینده فوتبال ایران را تقویت کرده و استقلال، پرسپولیس و تراکتور را راهی لیگ‌های آسیایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/SorkhTimes/131535" target="_blank">📅 15:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131534">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس
همیشه خواهان جذب
علی قلی زاده
بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/SorkhTimes/131534" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/131533" target="_blank">📅 15:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
باشگاه برای توسعه آکادمی برنامه بلند مدت دارد. از شاهرودی بابت زحماتی که کشیده تشکر می کنیم. امیدواریم ریل گذاری که در آکادمی شکل گرفته ادامه دهیم
🎙
امیدواریم بازیکنی مثل امیرحسین محمودی را پرورش دهیم. سرپرستی در پرسپولیس؟ فعلا تا پایان فصل در خدمت هستم. برای پایان فصل و فصل جدید حتما در مورد سرپرستی تصمیم گیری می شود
🎙
جلسات ما با اوسمار هر چند روز انجام می شود. چهار روز قبل تماس تصویری با اوسمار داشتیم که در مورد شرایط جدید با او حرف زدیم. در مورد مصدومیت براجعه با هم حرف زدیم. اوسمار منتظر تصمیم سازمان لیگ است
🎙
او گفته در صورت شروع لیگ از اواخر تیر تمرینات از هفته اول خرداد شروع شود. جلساتی خوبی با سازمان لیگ داشتیم تا ببینیم بازی ها چه زمانی آغاز می شود. حضورم در معاونت ورزشی و سرپرستی وظیفه ای است که مدیریت به عهده من گذاشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/SorkhTimes/131530" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم. وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است
🎙
یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد. مذاکرات خوبی برای پرسپولیس داشتیم اما شرایط کشور باعث شد تا نتوانیم لیست اولیه خود را جذب کنیم. فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم
🎙
دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم. بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم
🎙
وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است. یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد
🎙
فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم. دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم
🎙
بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. ما همیشه گفتیم عدالت باید در بحث قهرمان این فصل رعایت شود. ما به سازمان لیگ گفتیم از کجا میدانید پرسپولیس تا آخر فصل در رده ششم باقی می ماند؟
🎙
اگر گفتم عدالت را می خواهیم باید جدول نیم فصل اول لحاظ شود که همه تیم ها با هم بازی کردند. امیدواریم تصمیمی گرفته شود که به نفع تیم هایی باشد که شانس حضور در آسیا را دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/SorkhTimes/131529" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🟢
هنوز برای ورود به سایت دنبال لینک می‌گردی؟!
✅
دیگه وقتشه ساده‌تر وارد شی و با ربات وینکوبت، فقط با یه کلیک مستقیم وارد سایت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون دردسر و اتلاف وقت
⚡️
بدون لینک‌های پراکنده
⚡️
ورود سریع از داخل تلگرام
⚡️
همه چیز داخل ربات برات آماده‌ست؛ سریع، راحت و بدون پیچیدگی.
🔗
اگر میخوای بدون معطلی وارد سایت بشی، از اینجا شروع کن:
👇
🤖
@Wincobet_bot
🟢
تحلیل بازی‌ها و آپدیت‌های مهم رو از دست نده:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/SorkhTimes/131527" target="_blank">📅 04:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
صدا و سیما: ایران آخرین پیشنهاد آمریکا را رد کرده است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/SorkhTimes/131525" target="_blank">📅 01:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N10iJVbxh1ajoVQlc-c9yJ2m0nw9tDOjJSMy3RoaCd6jJZCA6hnAr4tiSFx6MCDPUlCHMHVyFuLzA0Dv3oobMRgeZXJgv6PwpOowJKSnjHWhyWcsjtnZnSTj76imhK3okSgxGixNVCmBs2m8bpuFjjzrAy3nPlhpzDEECFT7837iZqnwrViDFBR_uXhfLzbiRRoJtD_1J7W38hk--KT3EZynhxpLQu8dTu4FLTOKGvWqi7Aiy3NA2y3rlY1eD1T1F77yRsMCqGwTbUuwub4fGEpWlsZJhwztTnz7BxzmxTY8J4QV4ybJAEKeA7o4B_ZBpX9puWTz-OMnAr3ldE1rXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی نجفی مشاور محسن رضایی: بعید است مذاکرات به نتیجه‌ای برسد، چرا که شکاف‌ها بسیار بزرگ است. ایران علی‌رغم آمادگی جنگی، راهبرد «نه جنگ» «نه تسلیم» را دنبال خواهد کرد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/SorkhTimes/131524" target="_blank">📅 01:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Z6TX7Lnc_1JimZHDHGq8FlSDxSrZtGK-Mz53-G2D8w7emZtxEgrg-nG_BIhnhioAR2It_LG_7w6Vv7iba7FdJjGIAU2BNTgpIb8BDhyMwXINcnR-B8F8J-czlaa8EPML3aW5uMOkHHY-XQbFoQtOv4qBs6IXG5Xdf6RtDeTfx-l5z9shNZZgrn8ildg-0tcC_sucwvzYkT2V2ae66Y2nCknEQrn-SU1JRBJ7k2bEfdQST6WilKj_jTIM41DTmu5NYmNN90sjAr2q1YmcLSFrW8I7ZxGU3jEVCbzAoWcn_j7BLLw7OhXBbqkPkhGtWshaPPqeqA4lgdrQxIh8QVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ درباره ایران، اوباما و بایدن که بوی تهدید میده؛
ایران 47 ساله داره با آمریکا و کل دنیا بازی می‌کنه؛ هی امروز و فردا می‌کنه، وقت می‌کُشه و معطل نگه می‌داره.
تا این که بالاخره شانس بهشون رو کرد و اوباما رئیس‌جمهور شد. اون نه‌تنها با ایران خوب بود، بلکه عملاً طرف ایران رو گرفت، اسرائیل و بقیه متحدای آمریکا رو کنار زد و یه جون تازه و خیلی قدرتمند به ایران داد.
صدها میلیارد دلار پول و حتی ۱.۷ میلیارد دلار پول نقد رو با هواپیما فرستادن تهران و دو دستی تقدیمشون کردن.
اون‌قدر پول بود که انگار بانک‌های واشنگتن، ویرجینیا و مریلند رو خالی کرده بودن. وقتی پول‌ها رسید، مقام‌های ایرانی خودشون مونده بودن باهاش چیکار کنن!
تا حالا اون‌همه پول یه‌جا ندیده بودن و دیگه هم نخواهند دید. پول‌ها رو با چمدون و کیف از هواپیما پایین آوردن و ایرانی‌ها از خوش‌شانسیشون شوکه شده بودن.
ایران بالاخره بزرگ‌ترین آدم ساده‌لوح رو پیدا کرده بود؛ یه رئیس‌جمهور ضعیف و احمق به اسم اوباما. اون واسه آمریکا فاجعه بود، البته نه به بدی «جو خواب‌آلود» بایدن!
ایران 47 سال آمریکا رو سر دَوونده
اما دیگه قرار نیست بخندن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/SorkhTimes/131523" target="_blank">📅 01:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoMbiFce6dss7Z_wjtnYeMGyVNUViPIHQ72WmjLAilYJIHkueycDneuD7gTUTjxykYw3HsXkW2yNNEv-1jEmxZfkkr5hJ_bMGzhIXv8TMSEnRPGKJZndF_IyAdKL7DKryjJjPvcAkL-naH9cuX-d9fMb12If9fc51hn-vFhrnxaWnvlBVLXIiYVukVhtkZAnlqy5CJ7U7tXmjii_n-nVY7Eu-WxSDA6qAQwNp3ufN38crUQCqW9lXUu55SXEdcYL2dPNxsBIptlQNj7QHKeKD5fnU-kA1QLaMRnFV_fgpxZy6uiS-72KxQ5ntW99qCAhnSlqO_IT59jOQ2CzQ1vAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: از پاسخ ایران راضی نیستم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/SorkhTimes/131522" target="_blank">📅 01:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
منابع دیپلماتیک به المیادین:
پاسخ ایران شامل درخواست برای پایان دادن به محاصره و آزادی صادرات نفت است.
پاسخ ایران که از طریق میانجی پاکستانی ارسال شده، حاوی بندی مربوط به آتش‌بس در لبنان است.
گنجاندن پرونده آتش‌بس در لبنان در پاسخ ایران، جزو خطوط قرمز تهران در مذاکرات محسوب می‌شود.
تهران برخی از تفاهم‌های مطرح‌شده را به تضمین‌هایی مرتبط با پایان دادن به تشدید تنش در لبنان گره می‌زند.
هر توافقی با واشنگتن باید شامل پایان فوری جنگ بلافاصله پس از اعلام آن باشد.
ایران بر لغو تحریم‌های آمریکا و آزادسازی دارایی‌های بلوکه‌شده ایران تأکید می‌کند.
تهران خواستار لغو محدودیت‌های «اوفک» (OFAC) مربوط به فروش نفت ایران است.
پاسخ ایران بر مدیریت ایرانی تنگه هرمز در چارچوب تفاهم‌های مطرح‌شده تصریح دارد.
توافق پیشنهادی شامل مذاکرات ۳۰ روزه پس از توقف جنگ برای بحث درباره جزئیات است.
ایران گام‌های متقابلی را برای آزمایش جدیت واشنگتن در اجرای تعهدات پیشنهاد کرده است.
مذاکرات بین تهران و واشنگتن در حال حاضر به صورت کتبی و از طریق میانجی پاکستانی ادامه خواهد یافت.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SorkhTimes/131521" target="_blank">📅 01:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
اطلاعیه رسمی ارتش:
ساعتی پیش یک فروند پهپاد شناسایی دشمن متجاوز، توسط سامانه‌های شبکه یکپارچه پدافند، تحت فرماندهی قرارگاه مشترک پدافند هوایی کشور در منطقه جنوب غرب منهدم شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/SorkhTimes/131520" target="_blank">📅 01:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/SorkhTimes/131519" target="_blank">📅 01:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
بهزاد داداش زاده: علت عدم نتیجه گیری پرسپولیس افشین پیروانی بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/SorkhTimes/131515" target="_blank">📅 20:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اوسمار هنوز قولی برای برگشت نداده!
✅
🔗
شرایط بازگشت خارجی‌های پرسپولیس فراهم شد
🔺
فرهیختگان
: تیم پرسپولیس در نظر دارد دور جدید تمرینات خود را از اول خردادماه آغاز کند و در همین راستا به تعهدات مالی‌اش در مورد بازیکنان و مربیان خارجی خود عمل کرد.
🔺
این باشگاه اواخر هفته گذشته طلب خارجی‌های خود را از طریق صرافی انتقال داده و گویا هنوز این رقم‌ها به دست برخی از آنها نرسیده است. هرچند با توجه به شرایط سخت حاکم بر منطقه و تحریم‌ها، احتمالا تا دو سه روز آینده آنها به پول خود می‌رسند.
🔺
البته اوسمار و دستیارانش هنوز برای بازگشت به موقع در تمرینات سرخپوشان هیچ قولی نداده‌اند بلکه با بررسی شرایط قرار است تصمیم گیری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/131514" target="_blank">📅 20:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏳
لیگ برتر برمی‌گردد؛ حتی وسط آوارِ بحران
✅
مهدی تاج بالاخره حرف آخر را زد:
لیگ بیست‌وپنجم قرار نیست نیمه‌کاره بماند.
🔗
در هفته‌هایی که خیلی‌ها پیشنهاد تعطیلی کامل فصل را داده بودند، فدراسیون تصمیم دیگری گرفت؛
نه خبری از لغو لیگ است،
نه قرار است فصل بدون قهرمان تمام شود.
🏭
کارخانه‌ها زیر فشار
🔺
تاج می‌گوید تیم‌های صنعتی دیگر مثل قبل توان هزینه ندارند.
از فولاد و پتروشیمی تا آلومینیوم؛
همه درگیر تبعات جنگ و مشکلات اقتصادی شده‌اند.
کنایه تلخ او هم جالب بود:
«در دنیا تیم‌ها کارخانه‌داری می‌کنند، اینجا کارخانه‌ها تیمداری.»
📅
تقویمی که به‌هم ریخت
🔺
تعویق لیگ فقط چند بازی را جابه‌جا نکرده؛کل فصل بعد را وارد بحران کرده است.
نقل‌وانتقالات،شروع لیگ جدید،
و حتی برنامه جام ملت‌ها،
همه حالا به تصمیم تیرماه گره خورده‌اند.
🔥
سناریوی ۱۸ تیمی رد شد
بخشی از فوتبال ایران می‌خواست این فصل بسته شود؛
بدون قهرمان،
بدون سقوط،
و با لیگ ۱۸ تیمی در سال آینده.
📌
اما تاج صریح گفت:
«امکانش نیست.»
🌍
چشم‌ها به جام جهانی
🔺
فدراسیون فعلاً همه‌چیز را به تیم ملی وصل کرده.
برنامه این است:اول جام جهانی،بعد ادامه لیگ.
یعنی شاید بازیکنان مستقیم از آمریکا وارد مسابقات باشگاهی شوند.
🎭
فوتبال ایران؛ بین جنگ، فرسودگی و اجبار
🔺
واقعیت این است که لیگ دیگر فقط یک مسابقه فوتبالی نیست.
بازی‌ها حالا وسط بحران اقتصادی، تقویم فشرده و فرسایش عمومی برگزار می‌شوند.
اما ظاهراً تصمیم نهایی گرفته شده:
لیگ باید تمام شود؛ به هر قیمتی/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131512" target="_blank">📅 17:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📌
خبرگزاری ایرنا:
تهران پاسخ خود رو به متن پیشنهاد آمریکایی از طریق پاکستان ارسال کرد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/SorkhTimes/131511" target="_blank">📅 16:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAWe45KlAruigt7fOzha8EVBW0-VZ52VLZeRwvpghYNIi-geNLrFjhoncbZgZ3kpv8JedG64MtNfZNcNrmZhz_Z1gq5iAyoXCoh7J6Xf6Qbz4xjRtOqcLLszmlE25Vf7l3bawJFIjHWIJSTTYU3JcQUrk7KNOFK7AB7_fzXI5-kmacKfTAZXQ_9Ol86UHTNDciapAKKUgG3syRtA9M07CtQpCOfrM5YbVxdiAABzVcXKaNeQz5zPHzJ_u6eo_QllET_gAzaQvaq4D8DWoXp7UuiPN973wh6uXetAvD5JEMKWW8F_j4SnkP4zjryV73E1086zTGXMezCraQjZvD1FyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایگور سرگیف در گفتگو با رسانه‌های ازبکستانی اعلام کرد که به قراردادش با پرسپولیس پایند خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131507" target="_blank">📅 15:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVu38Uy324GspHMExOvnrdZVz82hdImcajwmDj8-8tOH8Gmk28sdhQm9er0uuBc545xphiLIHGNIAz08YbM2sLwbPdAvc595OloDPiercdjcHMUocTPYhEwgQwqPd7InJPSkUuJVLsiaaJn1pWJaU-_XNPmfM355KOs93Z3s6LdazAGBdLT31WeperRs-rrQSYxza0y9gnrWrZBOV7Aj7uXHaiemDrqUvAoexedB8M1CBtl7Z5Vq2Z8klkeialFWOKt6RKzhREpMC5XhjjudJzUxb4oS36hCzWZgIWIZMrcevcTy6uqVcwsl7AIRxAF3YC-GjarnYygujyBDKngKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
برنامه بازی‌های ایران در مرحلهٔ گروهی:
▪️
۱۹ دی: ایران - چین
▪️
۲۳ دی: ایران - قرقیزستان
▪️
۲۸ دی: ایران - سوریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/SorkhTimes/131506" target="_blank">📅 15:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/SorkhTimes/131505" target="_blank">📅 15:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فوری/ رویترز: مجتبی خامنه‌ای به نیروهای مسلح ایران دستور ازسرگیری عملیات های نظامی را داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/SorkhTimes/131504" target="_blank">📅 14:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/131503" target="_blank">📅 14:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzDEgc3Zy0EGzd2aW8s82ZQsSzefpQFaLbeWEwCtI0wEL4mSQgZJjjC55b1v7zlkQNXaMm9dvE6_YFZbhVO7NKjbei1vZo32Ju-Mb64hE7_wDark1_kuRPT2-Z42NHc8TQPXwrf2HJhr_OuGkIxDnTF_fDm2eNvv6KLrDLGjRjI3HEkXVABGl5M8zkiBIK6zwN0LzCIbipWi8m3EPFGQIvHD_Lf7lVO88mshvZYtbJBuLnVsBG7LybTbisuQl3vI_N4Kt3yEefZEPdU2f1FvE9HjmPY4QBDXosAE9Pj94UJOBBvNkl4HdI24McB_nRfppMEsrGSR95ja_hH8bWz2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
افشای رقم رضایتنامه ۳ بازیکن برای پیوستن به پرسپولیس/رقم پیش پرداخت به ۲ ملی‌پوش مشخص شد
🔺
باشگاه پرسپولیس در بخش پیش پرداخت‌ها، از پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه هوادار برای جذب محمدحسین صادقی، پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه خیبر برای جذب حسین ابرقویی‌نژاد و هزینه ۲۲ میلیاردی برای به‌ خدمت گرفتن امین کاظمیان خبر داده است.
🔺
همچنین پرسپولیسی‌ها در این بخش، از پرداخت پیش پرداخت قرارداد ۱۷ و ۱۲ میلیاردی برای پیام نیازمند و میلاد محمدی خبر داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/SorkhTimes/131502" target="_blank">📅 14:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚪️
مهدی تاج: 10 روز است که از کانادا برگشته‌ایم ولی هنوز چمدان‌هایمان را نفرستاده‌اند، نمی دانم سرنوشت چمدان‌های ما چه شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131501" target="_blank">📅 10:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131500" target="_blank">📅 02:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎙
⚪️
قلعه‌نویی: نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر
▪️
امیر قلعه‌نویی پس از قرعه‌کشی جام ملت‌های ۲۰۲۷ گفت:
▪️
پیش‌بینی فوتبال سخت است و نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر.
▪️
دوره قبلی هم شانس و لیاقت قهرمانی داشتیم اما بدشانسی شامل حال ما شد.
▪️
فوتبال در آسیا پیشرفت کرده و تیم‌ها به هم نزدیک شده‌اند.
▪️
امیدوارم در جام جهانی و سپس در جام ملت‌ها نماینده خوبی برای مردم ایران باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SorkhTimes/131496" target="_blank">📅 00:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
‼️
🇮🇷
نیروی دریایی سپاه در بیانیه رسمی خود اعلام کرد: از این پس هر حمله به نفتکش های ایرانی با حمله به مقرهای نظامی امریکا پاسخ داده خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/SorkhTimes/131494" target="_blank">📅 00:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131493">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb2d5L2N7jNMzP1UyxnQVYCNS0B_v40Ij5XSoh72A1rgSRWKfo8-xTEY67NHpV2YPMqhrD4cJe3EUjOdq9cVeosJCnO7i29GIak_riOSmFR_MP7CHeAr2t2s8w1g_q5IrMVjDK5eBBUp_Mkf2LQMEdInT6_dP2OzvE2ieypHC--GrSTe5jslpWYCnIk7ItRwg9Lr4bU2gakJwN6M5zXQCvrrL_4C_ejk9-RFpvbLL5zuzBwfjFFD3py6sG1LEE_ECAp7BgYtd4qVhQBhYyGEcMBNimFzkHtMBHAwMslsEzULbmLxUPtMpw_z7fm2XHFxHGkpwBYDyNE8GjAE1-Wn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توضیح علی بازگشا مدیر روابط عمومی باشگاه پرسپولیس در مورد وضعیت خوب مالی باشگاه پرسپولیس و پرداختی‌های باشگاه در مدت اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131493" target="_blank">📅 23:59 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
