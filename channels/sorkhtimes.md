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
<img src="https://cdn4.telesco.pe/file/HVHNnZVEfZwhBXFC_ykW-C95tQbmsa7EBoa4bG9tuNn_APwdDG2dmZLZ2wjt9la-4AKAUg_6jvi9VfyrNGLzb_4gja7JFUIo2sAdYQp5-_9o1jDq3Dp3lkgyRr_HMk8dAlzJFR2ee-ShVm1Y8eVY1oJXr94mJ457tMV_a4El1A8bbmXGGzjEYkmoihil4orZUjrYwifrMTUr49LpDK5ErMFzMdvrXRndeZqtEmzu1Rp3gKAY-KVZJ9o_GYwJqzaNbBdKaSZUwACAHgDCyUnc0OxM5fWW1zaLt_G2_q6cQvVIsyil0g92tCwra3bB2BOs6DrDUV7Hyl0O1_q6D9_fcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 23:28:45</div>
<hr>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di3M-rkwcCymljxKqDJ8_VEo49hhFcvMZT5MaHm8kWzwjxbsFSg5FQpCKMKeGDHqAqiihpu9wZ105O7vHa8rnkQdoFCAwxC1ATNgoPkVuk0Jwwi1RckI0LXnOrpP7F-yorl4W0n5YDU73nv91BLGx-cp8bor2FMmiBgW-UD83XvNcim0UvyfYec5zNqYv3Vwbu43SP3iJ9slrNxH7ioEdBywpwiFN0rVY8SJLSF57PRECLBJTLIWZTfSfbc0SiIz_P5ibSWTJyaUpc_EK9LfoXvxrOaibnlGB0Mnlza0ZJTblN-mfz-Gq2lugxjZ5UkbwUIlB4qBzDgTjU0naCPyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arOS11sMzI5UXZDF4HFeeQTNipeCCqgL-v6kY_2pXC3agiYPkRrIRD5Dft1hTfUUBwrQnpU3Mn5ZM2s3iIp6IAZMcVNdlQX4BSFXaRBgpxM-qI-HVJktz9L9Ovn-cy6QyFdwpJMvI1tmpaZ3S2Tu_404SaTtP87VFsGRxk0CgSuY9vBFzlKOrBtj1RRAiUWpqF1nj2ecVZnJw7uNqYlbqJYAK6z2ki9xDKLfSSCqHe_tnIIufUvGoBcq9LnnfjvWBms20r7C4lSwX05mSUwQmfaBM05U0RFkQgY7KNSXTtzO8zSumukNzcW98c4o0N2oS8d4Oc68T3oQ-xlQDnXs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSMWlKrPiKfByCwRepfACy2GcaqJXx52KeVNHaRYWZzhWQR7lcU5WodPW_nSV6SL02eLYOEpKjZw6oTYk7caKhlRsgSqsLFgG3CP2YZirep5NAeZCrQ1LAKE5savFp6NbjWjVefqJSa_NCBeUBjZyvnfyDEDbsXQ9-o6c1yEG_wDRSxeeei3PtOLnI5K4U3cBjZsYLPTRnwv7cCj24QRD7qUXi1nQ-7bGrXW0oRkqilfKQ9sm0uyI0lm_WeFoj7m5SBWizIjG4RzMkYqkF2FmzTcqH29I-P3hjjUyab6P8Q6RjEZDHZg443cwVb5PmroRgioppFGtx11jEDAli5aAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm3AvlVjZ9AOiGEaLk1sUeJZ7AEG9oUmbTMcSA6YC04RWmTDm9MtlfJ6MkkEg1HUNebLcjPcCBaZYcIvhwC7QjmdWf1kQ91A670pZOYb6oxk1hSyWmJfEn3_QwPj2j5R5DDlPVSJFOh2--jLsMy92Yxvy_VXNihXeS_I1S4-_ITZWrnnIpuH0ATpnSln2SauhWbnSk7utUWWlB4-6jvcUMM7-QzeM-TNpIZt9gkoLWGJ0t6A4FK1ijXoIqFh6jz_3WfV6OlFsTNlf7UlNkA6ndCLHbnwzLSNbR1KVNHWWXsGAxjQZpeWDtDtYPdVtb13S0c9itXzc9bhbWAMPSoN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrEOnHtRVYiw52GrJ2EA4_3OfmoYSH6Kw0Oj8O2HBWWTgrEHE2tBaWblBpGEJVdbzJ8m41emcFz04IfsprMbtUs1j-Nk-fcxyCBxRncCiIXbqbwmi6WCBTZ3dz-97QgFNvroUs1NcEPMHpwMbGD8d6cmIu7ab-6ls7YqCLDRUj8W__O-SYtPiiXBIXHnoMNi9Zwz0mevKefD_ZKV0H_usluGr_ksOkQCmv3E6uCAag8uE1CINqMVbIYIDe31XCARaH5VnYLzSAwxcDWXkqYjIOCt9RN9iUMe8Ig7zqHCb121l58U7ksg-Y_tGwp0BMSQmm-keNlyFQ44aXZ7tEI1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ItbsYza2L6JHmpWO64WuiMc-XAzRzGaQmTLjC3ZWgv026WYvOGIshAwUwaD6yvOMHJeOzWfl0dXifFF7MwQvNGY9jUY6Mfca8jLeYCUiqQYISzgQ9YkvdvocQWTU3QSi_ZPoY7DRIh8_bgTZ_V7DYHp5wRl3hMpnT8YAKVOpCsWKCl9qx2YM2di2_8ldPrnQn8WMsaX-velFgyXSUyQ9EpikOTXhtV9mnRaW6sqRlY8TRBGlCHjhCHMMPEBT5mdM2sH9hONY0tnzCU38y5s0Tgn7WarsMxCj5YgTJueGhdSebQSsTsS8TlZrFADFQ1TckmEF-LbZgjfmZEeGwVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlELnFD67FxjnEdC2UrZ1oxipA6vT7WVKW0rvhtP-mgPDCDqdocT6VOSMSTb3dH8RtUmzbYGgfp50-4tAKzK-C1vY5E6ULmmln3RCbeYXHr6VH7WSRLbIbJ4tYj772d7avznRGp81jLUZfrVDEFPxHq2Dg_PgW2tgY3fjREt5LvhQXOHR0kpP1pOi5StMCqIiZK30PQHMnlaPiHa6OY5G8cbUUtvWHTZqHQkWoEeVKkcsLvMgLTGW7Gu53gaq6XgjLltZUJz-Le_HBvlojpKFUFW5I0b2kffklO7s-S3UVeMn9hMgrBA165nFhtLpDbm_h7ErMAA1zH7raUVdA7nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC2g893onQ39syxOhE7-t9b04_q-PLtccbZdMZeva0s_9QGhpcijNYRNPNXulZAfzWXcT3a5S4ipBHew0Y-vMKi0K4m01nHyMizPs6WtbLvQodUQI7FSO9-DmLiuGJx3bfViXFM7ioWiMH3HE7M526H2TFF9vQ2yOA4NGAqnlLXRRurzWjNiqlqLe213A_NYVT5SG1B8XF9xwTrDuQR-5g24UJ8wC8JvOc-UH81ZNrzX46Eq2uHWfZXAqQUCgu5ZS0-3Yv4XEAoHEnayO5v5ZnXbbAbCPQizkp-zTMM0nNZeeLAURdDbYia8E9sOZijEouK-PvhKf1fohCUr7ivz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLInYUXqLIDcMmVy5XHbfWXx0anAk54nQlck6dqxZ8hWb5YIXH-jl45fVK75a-PABnLjSQ7tY-biUn-jcq7suSMUpjRXWbQpvAlJS35iSE51cy1tRFdfmE7nnww7dHaSxzjZJSxB6BJRzC2CtxDrv8PJmlzbHzarsI3c0ZLflmEH-zV6gC8Y_oNgY8Ky9xzKQrnD68Hs8Hg2fa_9TMD87I-vdoAK9wwBSi2HdcO0OBgC_oWhZH1ZrylUNUBAVlO5AIuR1v0LlyWBePbreBL8jrmHJr93jNZ1WG77Ul-wEWJM8pMg_KUp_QWFhvY7DNq88b8gbiiqH1cpWJfHJjp0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9PwJ3ZqR41PFX4kWw0upOFNM8LjgYOFSoFoBahCsbSvWicm0esHd3Go7M6OpKHYdBUAmMj-wch5Bk6DSWkG2Y92-uUl4ZGPkwF_TV3aiDhfXyZohhmrG8NtRcJBYW8SJQ08snd7apYXUkNd4E0USt4jz4z1m8uzAKJ8MZnQTopdbAroTSjsKmgIMCQZRMuDxpniKdkHDJQlTweKGRIFP0u1VcKcRHQijA4XGMiIPyTIvhSuHciMgDGRUCV3dY5TAwvt9m28aj_tunqdzdASnf7ILmlnzN1df9ogy-OaUJi2RoIW_yR_Q69uIwq0SaR_DwwFWPRWgpGCXzPAbEtlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=HrdRYNy9p0jp8nHNEeZsd0AzntHmzw4RXvOj4MarbdShq5CIB-26Nn-8xN_7lOHYb9hHtTqCRnHug96-j8zYUo6XJwJQ7NSn7PVVz3pV4jSPoXGucjT97dVy1IPjyV2FHn0RxcG2QDAiht0YlJirRDi3TDgf8khdQLd-rAkaLC4bJwdFIh-jiDof6GmLWsB_-rnGq7lxqgrKQpfat4EwbC9kYSJX7Ev8F96IF_gavpRv4Jj6T9WuRJ4GTYvsoiAO_5b7DlhRiOCmxUwAEWKYhcHpJap1KlzAEoylBDvyjA8rkgQJdRyUUZo2yh_wIipqkhb9Fcsmj4L3ft3K_m9ZQhRgAqpvre9lRExkDg_JrK80XbrtoHruHFR6YhPx2L__7MLHXd27un5_W0USAp6XIilSuf5-41SDYnxmkXoyeV9x6PAw0m5S21Q1Q86NwYGvbxWOipIVVoBJi03wAKxbnziOY8s9SlwYVuHfw0vfyLPqsbCPniTF7HRmxiXXWQZZnh6m68YBPPHVqsEZNSijjBHLle-eJt_ZHYALPtaNAWh8b9FtA3mBntgh0Pneqbd6Nf5kINIHmuG1a-fkaw12P9DbsuMhWWYIuYTnwMi3UpurIu0dYg83SSNDONjFuYs97Z5gBHqQ7hn2mvvhQle8PJ9Zq93ppaIIf6KS3Yzq42k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo5R-94qlvy-51HFMSF2n56xLSjHH1lhC15pZ7hzB_c8xA6YUkM3maxqQ1O_y9uwQfcwJnfpNT3uqE2qcqw2JmmNaKt61pTLyho-1Kzgry4DokoaXycIv6V722NNDsm73bgfiDncqRreEny7ALrT1sfiSMk5Ks6MujLesPshjwWb_PFnAGXOXSRagfW5qPq7OpCui-s-RbAR5Te_ukNurSPFldIG1l6x0N8Pdw_y695GVGP4zkI2xKFtIQVHnumWBedhIewHHYokMolxafmWtmwL5898DVcq-qK_2wuDr2Ak9IdxsHifCMU1AtrLTOzOZtUFd_Jb9Ey6lN8beTzqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8MWgJJAF41yjJihtYWQCx25nYHhDcsRSHOJGaa2Au3DsW5woSX6QWf8Z5r5sfUTx2-0edPYozlPkeu9vyXIYH8V_X_wWLMTAS9jDQNo-BxmbqmzZf9SyWNoOOCyOa9yTINMWXBO1GEfwsVRtgz8lCyBqlwkFzvbRDCHMj4mhMBpwI60QmIQaOrcqUvBtmVAYD3GI4OAI_cewcJV26B0QX_w1BWVPppui3tBank9XauZknNtGnsNSPZZCdSaQw0lw2Ng0LhKTXLji69pUlYDWX6i3uNUW2twK6ZGT1Odw86DCzK3kmmc81Jyakis6ZieR7gRQoKLb76lceZURYI-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZXB0tZG9VzT_rxuGqqXWP5-_ZKrob_3o8YfHFsw6_L12clVJ3e-0JvhwIuI1JskkPvcBLLBs1nm3zpzqafsyqvJ2rDF64xQjKAaIXIfeS73V8rec9Tb_ZifnY6Cjw7pZ41fAp2jil9uCwPK_jvf96ETd9qRidA2nvrtgHDKldx3wp3CKMne3BqKOU_Di932YqzJMOKOyM7jtXiqB2Pc7ET4Dt8aSLWPHj4sYItpjeyfTnQnTD96aNeTJE1sQmRAZXd4vmgLb3vhBL9H4oTfE3HrsF2aCPBFpd9E96mMptONCwVZpVmRux1-kU-WJsEaaSLm3VJlPci2JuiyOBAiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOdjvvr1JgydIttT3np62Tt6rZJjcndawWK5q05LmwkfLdQbtskCjCJCbBnQsSKqq5xbqb2NhK8purpVJGpJeuaTkpTtamN0-W-zMEN1tOUqcEYgjwOqkcpcYoJq6dUqm_tnYBswZS1BEPUDPdzQq3YM8QEMqXVcULX-sxUnts8fk6suNdmOx0jHgZln9f7ZbZ2dXa_Rj5pPcZ65XNSW-_Wjh7Ar7N7aIwJfe2WPo2N0uCKx3JuAsN4rVsTZIofS9tH9vLBNrl0aUehT-_XDbLqHeGFz7L40KwavtMqMZ3mex87rWuGtP27GEibti91V9Gha1LSpDnh0FAQizANmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=X_SzSgDg4j-NSlQPg4IO-nW9QxfED9PACTIybn14vyQJh4IvrG9R9bcWLokHx5wzIfOSHyB8Irqyt5wO-ovw37y5JrsOZeICftVwApAAAc0A7jzhVeHDCRBmz5kfzNBCX9KFTV2MtrkLUgj1v5buxVLBtfh4OhgtKzQPW6qk3R31xEdE5-sXnKNUq3DLbaLxr-liJvcXHkN3T0LifN4zhtF4W6jcFK_b_5uyLaM-G9k6XLkYF6ySKLNqT_YDN75OE8GbZuXL_mqVSMTaqJ8z3ZJ_SHT-MC6t48mOCsycHeSZt_AxjAA4B3jGcL4MxkfWoCG3FVQDsY2Ltn6f8bRV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=X_SzSgDg4j-NSlQPg4IO-nW9QxfED9PACTIybn14vyQJh4IvrG9R9bcWLokHx5wzIfOSHyB8Irqyt5wO-ovw37y5JrsOZeICftVwApAAAc0A7jzhVeHDCRBmz5kfzNBCX9KFTV2MtrkLUgj1v5buxVLBtfh4OhgtKzQPW6qk3R31xEdE5-sXnKNUq3DLbaLxr-liJvcXHkN3T0LifN4zhtF4W6jcFK_b_5uyLaM-G9k6XLkYF6ySKLNqT_YDN75OE8GbZuXL_mqVSMTaqJ8z3ZJ_SHT-MC6t48mOCsycHeSZt_AxjAA4B3jGcL4MxkfWoCG3FVQDsY2Ltn6f8bRV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=u3habf0GzFrU1JQOUlbF9vFZJnb0zK4jpoo_VoDQth70i5IxFWgIFQJVMfIJIP5NI68HfICllW8e72CvJPejso2kLxYbnI97Z6RIsNawgNvYQT78B09YxBAEvRFq8lwVW_lLw4170mhhuB1LUtQzIoZm3rYRXNHNCOw6WPE1gOO0rU9Ix147ZPDj7Ll_dVSDEbUk6Dk1k4aMf3Oy4uCtjddNodymIMfghGQ6XJNBCJ6Q8qjLBlodYvZ6VRzL4S7lRnpcbSvA3Vg8MLyd_J6kd-kxUklCqfQ5NJHMxF6TSN0J4A6_FkH-eCf59gHrzPhmNyjpxArS1g5zC2IK0VsBNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=u3habf0GzFrU1JQOUlbF9vFZJnb0zK4jpoo_VoDQth70i5IxFWgIFQJVMfIJIP5NI68HfICllW8e72CvJPejso2kLxYbnI97Z6RIsNawgNvYQT78B09YxBAEvRFq8lwVW_lLw4170mhhuB1LUtQzIoZm3rYRXNHNCOw6WPE1gOO0rU9Ix147ZPDj7Ll_dVSDEbUk6Dk1k4aMf3Oy4uCtjddNodymIMfghGQ6XJNBCJ6Q8qjLBlodYvZ6VRzL4S7lRnpcbSvA3Vg8MLyd_J6kd-kxUklCqfQ5NJHMxF6TSN0J4A6_FkH-eCf59gHrzPhmNyjpxArS1g5zC2IK0VsBNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-J0fsRdf_z16R1WPY6hSHZNYrcWpQKmopTZZWaJnMqN9JKUrMqhT7_RLkF5lBnhZ1bf2KubMWAJY6IPBkpMMVYPee2FQ0rhVUbWKiLoYtOJOdYNm7OqHxO1c0chwULcm9RWEuQMlZSGr9HYRBDP3hr4UX2s_n9fnRZJ0pATcMiKW_XEPSg2F_MbRdpGYWCeBWq0TBOGvbj8G1jspfDT5Apyey26023jehbNsnxH7ZYMQedwVGVR5AmWtgXXafATUlwXkMNlcGdoyr__IC0VOsWcF7uriwy_8R6DM1vlBg60-0SSnnoWS5tn46TPB7N0PT0Ciq1P_sX_2JTOYR0eUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=seVqfKseMw5jrZjdVWZ7vT3C9iZh0voFJitphh3O9igRldd9Icuf-5-HlgnrnneuAYMFtv3Sf1wJdB3WiSbxuVVtuHGO0RVshU9xD8RPmYBn_2A1Rn6VS7HWS6o_CrR-SbQlp6F94GMaZAdTGoByKV-tlqtyyqkI7UWcMjC1nPPJYgGHnHrxJjT9AOsBTcNf5najpAZGgP2LT0vEqryxe3hDOrlKs-xFmK82Ja_WYcO9gRziUKGpcz4WB4HqCLeobt8eog6PbJrkn_ouul0W7VgmnCnUTz_oxqz6jX3SYAAySGdPxeUR8KY9-tQApbCRnqA8kwmcMqUz6Wjv6n3caQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=seVqfKseMw5jrZjdVWZ7vT3C9iZh0voFJitphh3O9igRldd9Icuf-5-HlgnrnneuAYMFtv3Sf1wJdB3WiSbxuVVtuHGO0RVshU9xD8RPmYBn_2A1Rn6VS7HWS6o_CrR-SbQlp6F94GMaZAdTGoByKV-tlqtyyqkI7UWcMjC1nPPJYgGHnHrxJjT9AOsBTcNf5najpAZGgP2LT0vEqryxe3hDOrlKs-xFmK82Ja_WYcO9gRziUKGpcz4WB4HqCLeobt8eog6PbJrkn_ouul0W7VgmnCnUTz_oxqz6jX3SYAAySGdPxeUR8KY9-tQApbCRnqA8kwmcMqUz6Wjv6n3caQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=LiW1QT0RqcckbLbV9qlPJAWloQcq2BiTvpUr1078SzGO02kTtIP9UCBK7Mv6so_qf--2pZclBOmeE4LNqK6cSdkzZi9a8k4oxhNqIoh4f0eL8v8OSZfXYgyDSneKCerpfp8JiyHP9riH7mnZOHwNS7irNQ2ReE-iEHWvaHsznkPJ1gnOLBb7SyiS8ScsTS9rx8FvhOmGKkYFd_HtMn5Vbrp9TQcS_PgcH48ulW3U9-JK4nbjy2CT1wArCKVixj7tvdUB_oYwEGPs7R4K7aINlVY7AwZpngoMM8Ku9I_cQlsWlLdhZqYg17qmUH-FnUaVGr2tJngL-ib8IyGJ-pHqxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=LiW1QT0RqcckbLbV9qlPJAWloQcq2BiTvpUr1078SzGO02kTtIP9UCBK7Mv6so_qf--2pZclBOmeE4LNqK6cSdkzZi9a8k4oxhNqIoh4f0eL8v8OSZfXYgyDSneKCerpfp8JiyHP9riH7mnZOHwNS7irNQ2ReE-iEHWvaHsznkPJ1gnOLBb7SyiS8ScsTS9rx8FvhOmGKkYFd_HtMn5Vbrp9TQcS_PgcH48ulW3U9-JK4nbjy2CT1wArCKVixj7tvdUB_oYwEGPs7R4K7aINlVY7AwZpngoMM8Ku9I_cQlsWlLdhZqYg17qmUH-FnUaVGr2tJngL-ib8IyGJ-pHqxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prk09GsgQgmJICmZGVBTtsMEThVWUbxcaY13j1AROkVNacInrSKx2k2R0PJyqq9TxG8G4t2sJbotWzoejovbluj7er9akwqAwTTsIlTwh-IbYpRJ-H0DAmTngc_8XoHkvfp1ODbvZJ89MKNbwZXgTciTucRW2BtkHnNSE74MjBuCKc0AjvHYTJRoZQJDZdjXFQkHK9qg-nHkJ9QrcfqFNBlli5pS3S44g_Z14oINreIaH5amQNItD3eIdxCBA3tU7WuMIA-sD1ZVBQAKUlF6lkoXb_OJnXnnkhHqLse99tszOOGn_F9vvhjKFMNVBZf8DAa-Bj5VaDAC0RqABAo2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/139437" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139436" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
ما به اینا نمیبازیم ...نه ساله نباختیم به اینا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139435" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139434" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139433" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
امروز هر کاری خواستن با مجید عیدی کردن از بس که اون سمت اتوبان بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139432" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139431" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139430" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
گل مساوی و خوردیم متاسفانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139429" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❤️
❤️
❤️
ما به اینا نمیبازیم ...گل اول و محبی زد روی پاس بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139428" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🔴
بریم برای نیمه دوم ..الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139427" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
امیدوارم نیمه دوم شانس با ما یار باشه و کارو تمام کنیم ..شاید ارونوف تعویض طلایی ما باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139426" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
نیمه اول دو تیم خوب بازی کردن و بازی زیبایی و دیدیم از سمت هر دو تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139425" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
نیمه اول دربی بدون گل تموم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139424" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
بدون شک بهترین بازیکن نیمه اول .تیکدری و زارع بودن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139423" target="_blank">📅 20:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس خوشگل کیسه رو کرده تو قوطی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139422" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
❌
❌
پرسپولیس بهتر و سرتر و سرحال تر داره بازی می‌کنه و سوار بازی هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139421" target="_blank">📅 20:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❤️
❤️
بریم برای بازی ..الهی به امید ...خدایا امشب و پرسپولیسی باش ..حس خوب و انرژی مثبت و بفرستید برای بچه ها ..انشالله برنده بازی ماییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139420" target="_blank">📅 19:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139419" target="_blank">📅 19:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAxfmuT4Jjpuu7dhs4Ve_-SW343giBtwbgHzFSpszTVquFYk0MCKAmSwkUiOpAGy33dgZ9ajW1GAEdJxTCQSKgEX7IGnHLkDH3ktk1-lBhyBV_Vr4cAg3vqxg6B7b3YaHyfREueapxTHZz4xeNjgwFida2co4mRH6IvhkEYtgc0ch44FojhsmcCTevL9zrbeuqlj2FfRElgOViXXKbH0QbuSFfDgbhUMPWRjIQnJc2sSpgpn-FhgmszHpaihAdiiccmw_2AhrZ4h7TtN_sI3ogqVzdTiQmtj17rNLF57u34R_uDDKr9tmY6KTEk58JJhom8Tc4G_4c_8ed9X94kOXDJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105ef18474.mp4?token=KpEMeN8HQ0LLByOhZbC3RMMknbR6PLMnwj5aGMMK-OuNj9pC2tQ2PM5RGzLt-vU4iC7M__Xo-S7-fcUXllBly_yRZ6zYCJUJzSfE4OwGNp8O7dn-t60KIu0ul42kSgShgqrlSJ6o9PrQ3vp_JkKnpQr3l60-RFrC6qfNDST3U4ITwGklvJ40Jthm_l2S8OcwI4EE7V5PX_11VKMBoXE_Gl0KFM_T1yRDX1pHdSjvGh1XOy1R9Ogc1ddmIvh90sUw0WChPkOjGFs_L9IfmE_2OUSMrDxMup7nZmOEpsmPRwGKeBXDIOsw-Ig0_QCaqcY5bYRgmvW4GbYW4ySpDDSEAxfmuT4Jjpuu7dhs4Ve_-SW343giBtwbgHzFSpszTVquFYk0MCKAmSwkUiOpAGy33dgZ9ajW1GAEdJxTCQSKgEX7IGnHLkDH3ktk1-lBhyBV_Vr4cAg3vqxg6B7b3YaHyfREueapxTHZz4xeNjgwFida2co4mRH6IvhkEYtgc0ch44FojhsmcCTevL9zrbeuqlj2FfRElgOViXXKbH0QbuSFfDgbhUMPWRjIQnJc2sSpgpn-FhgmszHpaihAdiiccmw_2AhrZ4h7TtN_sI3ogqVzdTiQmtj17rNLF57u34R_uDDKr9tmY6KTEk58JJhom8Tc4G_4c_8ed9X94kOXDJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
همه چیز آماده دربی پایتخت؛
✔️
✔️
هم اکنون ورزشگاه نقش جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139418" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139417" target="_blank">📅 19:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244018c05.mp4?token=iBzmag7loEVObeJ0jZIjQvZ0YQtNNIFYHlMtUiyluKzPzv58gE-G6z4w1NtetAvGuP45_VQToAI1p8lC-6xVjQqPhc_8aOIa9vIqkUqs_UgXisAQu_5QAxpZnvOziRNT2jmENYe0XQA3JVrsiPEv5XeL6R8TvLnAUy0lH5i6QQxXbWAxJ8aV3btRcK2pOWpqzA-ju1q5rSRhIMyxTH6LLLPOg-G1f62qGbVGuCK6MaYBvL5F3yJKBbED_UkV7izILSlZuai3z7gdJKIZ00xSt4Iqw5MpHyKpsB49pnFWIDD3ybIzEcjllj13DsRupo9UezQI6J0BzVCFH2cdr1beWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244018c05.mp4?token=iBzmag7loEVObeJ0jZIjQvZ0YQtNNIFYHlMtUiyluKzPzv58gE-G6z4w1NtetAvGuP45_VQToAI1p8lC-6xVjQqPhc_8aOIa9vIqkUqs_UgXisAQu_5QAxpZnvOziRNT2jmENYe0XQA3JVrsiPEv5XeL6R8TvLnAUy0lH5i6QQxXbWAxJ8aV3btRcK2pOWpqzA-ju1q5rSRhIMyxTH6LLLPOg-G1f62qGbVGuCK6MaYBvL5F3yJKBbED_UkV7izILSlZuai3z7gdJKIZ00xSt4Iqw5MpHyKpsB49pnFWIDD3ybIzEcjllj13DsRupo9UezQI6J0BzVCFH2cdr1beWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازدید بازیکنان پرسپولیس از ورزشگاه در میان تشویق هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139416" target="_blank">📅 18:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139415" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139414" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139413" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔵
دربی تهران در نقش‌جهان اصفهان!
پرسپولیس
🔴
و
🔵
استقلال؛ در دیداری حساس و هیجانی از دقایقی دیگر در لیگ خلیج‌فارس ایران به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی این دیدار حساس همین حالا وارد سایت معتبر اسپورت‌نود بشید و با بالاترین ضرایب پیش‌بینی کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/139412" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139411" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44157a322f.mp4?token=U42IYm0YIwA5M3CbeUVFE0Za-nvVUoEagjPyTNTY9hhYsItLIGBga2QGKHH9vVm2IWuQvRNcLxHSVS1xvnw8s-OuskRRDTi1IwxODYeLc-6ZAQmWigrxlOth5F7f6Ulf8qC04pS-Wxgm0Vqo-DU3pFLNYHCiTvJhGyuchyPAhjjH2vEufCwL3sHmfqPTAmPGj8kMlspBqQnl8oxg_gPhDo8fxM1dUXZeZr1OXmQ_bijdi0HYwMPdxEBDhlPKT6hBbl6v9RRcUBgKKWb6kAkfuL6XhXwFi8hg5SGDV53j-hYARJGviYlg5mOnGuoCbdbdmsHEz9th_eh4kJhN3LTCITQkSUjLhKteNHdriTjknU2cnDMk2jrNuUPAnG01GYktGB7rbN-ePvFRL876FBWLanH0GTbTsq7SPOpZ2WDa6YSoypp3QtVLWX8GveYBBKDSbB1yz-JglJo8Zqzfw5TnoH-TLcyqmQ6ZILkh1K_pZ6BoclmITJV9cjXypOJXzZdKpN3naz5YBSorgMhVja_3wYArol6hezALoNILEQY3FA7tyfXFnnZQy1zU1uGomU8j13cstl-5d4P3SbA9Zy9OaxuJ5HZPfUT6qXaGiM0_-5w3yDPfkvOiOgWZw4qEl65Q8FH5lTHSUaauQaTwMtFV8NQdAyUqjOsUai6YMuy4nnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44157a322f.mp4?token=U42IYm0YIwA5M3CbeUVFE0Za-nvVUoEagjPyTNTY9hhYsItLIGBga2QGKHH9vVm2IWuQvRNcLxHSVS1xvnw8s-OuskRRDTi1IwxODYeLc-6ZAQmWigrxlOth5F7f6Ulf8qC04pS-Wxgm0Vqo-DU3pFLNYHCiTvJhGyuchyPAhjjH2vEufCwL3sHmfqPTAmPGj8kMlspBqQnl8oxg_gPhDo8fxM1dUXZeZr1OXmQ_bijdi0HYwMPdxEBDhlPKT6hBbl6v9RRcUBgKKWb6kAkfuL6XhXwFi8hg5SGDV53j-hYARJGviYlg5mOnGuoCbdbdmsHEz9th_eh4kJhN3LTCITQkSUjLhKteNHdriTjknU2cnDMk2jrNuUPAnG01GYktGB7rbN-ePvFRL876FBWLanH0GTbTsq7SPOpZ2WDa6YSoypp3QtVLWX8GveYBBKDSbB1yz-JglJo8Zqzfw5TnoH-TLcyqmQ6ZILkh1K_pZ6BoclmITJV9cjXypOJXzZdKpN3naz5YBSorgMhVja_3wYArol6hezALoNILEQY3FA7tyfXFnnZQy1zU1uGomU8j13cstl-5d4P3SbA9Zy9OaxuJ5HZPfUT6qXaGiM0_-5w3yDPfkvOiOgWZw4qEl65Q8FH5lTHSUaauQaTwMtFV8NQdAyUqjOsUai6YMuy4nnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
مصاحبه با مادر و دختر پرسپولیسی
✅
پرسپولیس امرور برنده دربی خواهد بود؛ شک نکنید.۲-٠ استقلال را می‌بریم؛ علیپور و بیفوما گلزنی خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139410" target="_blank">📅 17:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=ea1wpyctVt6PtNFEPwUTnt1jdRRT8uH_P4AFwAJT8TFx-fdfQZCU4esTX6iy72XmcUEd02V8GWB-JzxG8XO1cdBObEh0X2N35_rWidCcYPzxS9LrTqFKXWFrj_CVinQ-XoU9kHl2jXtyd99YVGy97rDwEoC-K7crC5BPcsHxiN01DeZW0oShoDx_W2h4Vh1lCJ_uVSNWw6n2zYMghiBDvtskw0gP3W5GI1psEbuqzUSjJmYurtUKAjYJyJgzE5hEfGPbuLQR8E_qfbAlAcj8ry6nWGtGHKoMr3zOlhOyJqYOQFK0BvxzPCerGX7db8cFZqEE2hPI8WQFcVCQ02SdtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5be238bd7.mp4?token=ea1wpyctVt6PtNFEPwUTnt1jdRRT8uH_P4AFwAJT8TFx-fdfQZCU4esTX6iy72XmcUEd02V8GWB-JzxG8XO1cdBObEh0X2N35_rWidCcYPzxS9LrTqFKXWFrj_CVinQ-XoU9kHl2jXtyd99YVGy97rDwEoC-K7crC5BPcsHxiN01DeZW0oShoDx_W2h4Vh1lCJ_uVSNWw6n2zYMghiBDvtskw0gP3W5GI1psEbuqzUSjJmYurtUKAjYJyJgzE5hEfGPbuLQR8E_qfbAlAcj8ry6nWGtGHKoMr3zOlhOyJqYOQFK0BvxzPCerGX7db8cFZqEE2hPI8WQFcVCQ02SdtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
ترافیک سنگین در مسیر ورودی به سمت ورزشگاه نقش جهان اصفهان در آستانه  شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139409" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=TB8QPfAJ9Lbj4jrkYOcae0WswDD4QxP-tusM_00LRsZJPfBPZWv76v8ekxS6LCVTFoaMfE7vE_XpdWKb-iwT78GiPf2XU4Mo3mDICNq05zS16S78AYOgxjmnLx60AbLd8TiDV236XvHJhvs-Y3ztCRmJo4Po_aeWNYPTs1Hed5ijNc-5XfKsUUXNtIROi7zuphxZ1o-MKNgsu9wdPYODEK5-QMcCpKZGcv0FWrrvkUHvZcoPlmrxWs4uHm_89SI-4WUK3krJbTOl1vcmtve1jj8vF151y8cpaQZOCVnypvdC6yfVfHlaSKZLTdxRctZXBMhdj5bjD2A9pGCcOyoyEIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4db0aec.mp4?token=TB8QPfAJ9Lbj4jrkYOcae0WswDD4QxP-tusM_00LRsZJPfBPZWv76v8ekxS6LCVTFoaMfE7vE_XpdWKb-iwT78GiPf2XU4Mo3mDICNq05zS16S78AYOgxjmnLx60AbLd8TiDV236XvHJhvs-Y3ztCRmJo4Po_aeWNYPTs1Hed5ijNc-5XfKsUUXNtIROi7zuphxZ1o-MKNgsu9wdPYODEK5-QMcCpKZGcv0FWrrvkUHvZcoPlmrxWs4uHm_89SI-4WUK3krJbTOl1vcmtve1jj8vF151y8cpaQZOCVnypvdC6yfVfHlaSKZLTdxRctZXBMhdj5bjD2A9pGCcOyoyEIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
هواداران استقلال و پرسپولیس در مسیر ورود به ورزشگاه نقش‌جهان اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139408" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282676305a.mp4?token=iTtiuteFHv-HmXnGplqMgt1hVZ94mn9HI8JBV5qj2Tq1zd_EtUObRlFhzOBujG4ou0lr03LwXdg0NMWbFcJtCjg_XwsTJvz2-ogRE3GoYcSmpXq_yYLtMX-mEupPkJf56NyhjPcP_vymIM1nqArgABCyjLbF3lEj-CwTiN-NJgczRavAobTvA38ecdGJn-3NtxNf5JvGhdCXJbHJCcaWJw5VpHC_K1TKYWS-CkIWnfphgSl8UXq_Xna3eVWXPW-DoPhHysWh1lgxrFsuJYfMUzAFFqi7MtxhBJi4JfzGCCHOul6LjsCyf1SoXLl3dRy-LMLtQMfSZKOK56VbfAaWQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282676305a.mp4?token=iTtiuteFHv-HmXnGplqMgt1hVZ94mn9HI8JBV5qj2Tq1zd_EtUObRlFhzOBujG4ou0lr03LwXdg0NMWbFcJtCjg_XwsTJvz2-ogRE3GoYcSmpXq_yYLtMX-mEupPkJf56NyhjPcP_vymIM1nqArgABCyjLbF3lEj-CwTiN-NJgczRavAobTvA38ecdGJn-3NtxNf5JvGhdCXJbHJCcaWJw5VpHC_K1TKYWS-CkIWnfphgSl8UXq_Xna3eVWXPW-DoPhHysWh1lgxrFsuJYfMUzAFFqi7MtxhBJi4JfzGCCHOul6LjsCyf1SoXLl3dRy-LMLtQMfSZKOK56VbfAaWQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حضور دو جیمی جامپ پرسپولیسی و انجام خوشحالی رونالدویی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139407" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=qdAS-GxXYUWQNk2G2mP03dyd1UN6a4kA2-26RL5NuPMh2vWbk60NgZlD7zowrbvDqex0JQsqON_o2T0RjQEya0f6IIAUQei5-QuNQZHbIzBIpa4a54e_thIbzUfBRZ0TKXUptMdWmHQZQntXzFY5y3adL5kjWPPiHqh-Ju5ZQpdbDLgWY94gYjc88N2qiC5ocoC2a8QKXjpdMXkSEapW-AMTncWWO2eCamLckROnNnojpdI1Eg2sa1pmirXQzwuW_EBRUnRpfik3DdL1EEb3vdY_IFdNLAudqm1YNRsQDp91JXIru3UvbPOohqB1rF2cWP81I7zcipJjZslqKFOGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7410fd3106.mp4?token=qdAS-GxXYUWQNk2G2mP03dyd1UN6a4kA2-26RL5NuPMh2vWbk60NgZlD7zowrbvDqex0JQsqON_o2T0RjQEya0f6IIAUQei5-QuNQZHbIzBIpa4a54e_thIbzUfBRZ0TKXUptMdWmHQZQntXzFY5y3adL5kjWPPiHqh-Ju5ZQpdbDLgWY94gYjc88N2qiC5ocoC2a8QKXjpdMXkSEapW-AMTncWWO2eCamLckROnNnojpdI1Eg2sa1pmirXQzwuW_EBRUnRpfik3DdL1EEb3vdY_IFdNLAudqm1YNRsQDp91JXIru3UvbPOohqB1rF2cWP81I7zcipJjZslqKFOGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
اندازه گیری چمن ورزشگاه نقش جهان توسط نوشه ور  مدیر برگزاری مسابقه دربی 107
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139406" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=NU-CzNBuy5VDrWPwh492c87Lwa-a1xARheoT3nhKGTH8qwYWD7q1znMoyVfAOEn3Ypica5Nk1lXt1ns-5zXhkX9av8c6npXP3hfbhmFMDEXCLdWz13w1P8U8vC0A2-Kr7_xBgp-5ORr5XPE2hZMEST54RSjZ_C1dcoWrKkubPBavw7GJok95xk2OUFZ-VIr_1iBNYlmD4LVI7cBel936zq2bUQHgAAdoTJEdFFp-nvAUyrIsxBd4rpOAiKHea3HQVdxh0qgRLv8JmAuBbM_opLcBsXhrX-zcVC5u15zrO-w-4OgpMsxygIK4xj7-DNMFD1G7lP5yNUxeky0fI1diRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=NU-CzNBuy5VDrWPwh492c87Lwa-a1xARheoT3nhKGTH8qwYWD7q1znMoyVfAOEn3Ypica5Nk1lXt1ns-5zXhkX9av8c6npXP3hfbhmFMDEXCLdWz13w1P8U8vC0A2-Kr7_xBgp-5ORr5XPE2hZMEST54RSjZ_C1dcoWrKkubPBavw7GJok95xk2OUFZ-VIr_1iBNYlmD4LVI7cBel936zq2bUQHgAAdoTJEdFFp-nvAUyrIsxBd4rpOAiKHea3HQVdxh0qgRLv8JmAuBbM_opLcBsXhrX-zcVC5u15zrO-w-4OgpMsxygIK4xj7-DNMFD1G7lP5yNUxeky0fI1diRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
