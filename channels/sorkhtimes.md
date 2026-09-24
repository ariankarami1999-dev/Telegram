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
<img src="https://cdn4.telesco.pe/file/BSbUCJ-I4IH_FGxyf8xjygcIG9bHva7T25Mz7kn3BW4zcJsxfKMdhzkW6ku1yLxVZjdLRmeTGW9lF3xChlqkOSA_owz6R7LRpUP_DboYvxR15Zda8O86NOhhdqh2l5p4FNEfpXzNkHgAkXK3eBtW_5eYDyhF-gs1H_7N60-Oq2jXTuy2QJKGk9IAOlLaWhIKUPnIgx_B21ZKgOQrNlGlKlCLPGTdjakHsaOFCtSAU12xexwxTNo7aIdJBbPw3fWYQReUCOGhumfBc_ApzRcdy6m2Pjgavmi_3gRcWMACdXFEsTxN7Skknbjes7TDOUsTateq2-IFxVKFFfvDoLZ-Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPkbiFpPwHSn59vJ3XP05XPQrJ8ZjvVcFdiSATG0hLe0YWyBVlEenmE9NGgQ6ckeuTupVJEjE_9Jp5qIV694xFSxYrlAULAMcsMfXksHCLy_dlghicZdXjfKmtPA5W0gHDEwPJtzHvhhtCg_Cox-ryLaTb2MZBLixX9mLg_sMp8nlsrk2uMHOpEPXif8r_IKhIJMLJz37WoCeJ89isNVFyyZR3Rv4PjcsAA0KB5eaIFezugDtEoAgwun_fpciPaY8AzzYEDuTwYw_f4QEsE_WnTW-t2lbaNlSaGFuLMyNiDkngdWM-y4vCjNsRdkPavalz1cL78nkqUdbDsrkOW88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-lqRg7rxXS8HWPY2E9SHTf9Odhgn5kOt5EpuQkz2NPkRI01MNxl6EmrKkVU3p1MzbUoF7HUIKgTeHZjjMBJJgYELeJkmJAx3GU9192Z65rfleEU6IJcH14-FTmleXeGwINuLeHx2mKvDyqonIalvQL3_h3qQTR0ezaVO-r7X3dUefb7Hj3DoDRjkJ-Xww6hV0yUiOdX5xNjCvX9GnKFCh4KpPSmGJSANiI2GMcxNfR4U5_hSz-t-5DOdQzTNa7Km609J8EEPuchbPoLgNHpJz16z9BPzZlc6NZaHFKJlVdsENppq5w8U69S4O1ub5OPDZrt9s0RIDzZg6CUOCXfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از ریفوی ژاپن تا لیسبون؛ شبِ دوئل‌های حساس
ملی
🔥
⚽️
فوتبال امروز با دیدار ژاپن و اروگوئه شروع می‌شود و در ادامه، ایران وارد یکی از متعادل‌ترین بازی‌های روز مقابل ازبکستان خواهد شد.
هلند با آلمان و صربستان با یونان از دوئل‌هایی هستند که فاصله تیم‌ها در ضرایب هم کاملاً نزدیک است. در سوی دیگر، نروژ مقابل دانمارک و پرتغال مقابل ولز؛ جایی که پرتغال با ضریب ۱.۲۰ واضح‌ترین برتری این جدول را دارد. یک روز پر از بازی‌های نزدیک، ضریب‌های متنوع و چند تقابل که نتیجه‌شان می‌تواند جذاب باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9mLsRdvFEYjcX4_CBAM78q5Su1ybRem_CrHdfODmtGitIEE3KGXEJetKCVIFL92GLBII9KIMMeAsbX7GxvNtRk95WFL57eJczGlvqHFSbJcVYb_xx_1tA8tsz1cJXdbzcss7y9LCjs1qBI548gRSSvvq0GmbDnYl4xmHkUWK5yvaQxsmvpTLC0pzYtVWVEJuvmbSfGajTAL_uMFEc0XcyOfhzNYROWoPHcXwoyrTU4bEJyIXRF6xlH3gu2FNzqqctbrRlt7XV2CqnQtAjlU2FClpACiymgmta8GHfZSHaYMtMnBk9aYLrarmfGXj4MPtF8-nZJt0Y2fbbPqVmnVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
| طرفداری:
🔴
⏳
🔄
تارتار اصرار به جذب رزاق‌پور دارد و ولکن این بازیکن نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/140473" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/140472" target="_blank">📅 10:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140471" target="_blank">📅 09:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmVvRtxgJJGvhZpbN2l1HU_BFqTNWh0wAH0prS_9G8hlBvDqTDFeB2aDutWjcayT2bK5Y67RP9FtWuDdGlho2N469e7l2Aq9tvrhzONmkvnbe5M6MxvP0aH98cFfUNaUH5AoOvUIZHgtyZhbWFFfQQg573sL_-x-1QT7buZJTxhRrquKJcQahJXnCQC7zh187wD08TwO1jGsd4iVNn5MVk3zvNzpDghcD4S7k30VIm6_YJXdQECGZNWb3kXauwwUYXnLdBMq6093Yd3MrzXotugwPvFXtYWIUUSrhw5ZJWAxZuU4gTd_tuJmDTJieopDZwBduM9EyxOzySjqDmX_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140470" target="_blank">📅 09:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH96QHZdg95SJr6GKm7Axes17zbctqI_0N15_6aybinxV-2XiXuMyxr_FDfC7yijapjwA12lGSUWJs9bB_R2xu1qr6WI4RqN2jmiwO5oh7bQh90ya7UMsgwaOEuoFG4x9Kog-u2PQkNCayoYYNi_F7sI3CClY9fjBcDqxXHmZ7S43IAw6t3wlrdk0RNzoYS4RLpIsD2Ile5TlhGsET3orS3c5cjatKmoFTHSGYgsb8qb8T03lOSbU_is_6hDRYbqeGgR_kT1wH6r6EvQINfoyM8iDd8l0bS_I7HoI1_jLZqTRYO5InqpLKmL7_ylMDfnUX91o-kXvQMrhbSfP5ETPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ایران و ازبکستان؛ محک جدی در یک روز دوستانه!
[
ایران
🇮🇷
🆚
🇺🇿
ازبکستان
]
⚽️
ایران و ازبکستان فردا در یک دیدار  دوستانه به مصاف هم می‌روند؛ دیداری که بیشتر از نتیجه، برای محک ترکیب و هماهنگی بازیکنان اهمیت دارد. ایران معمولاً در بازی‌های مستقیم و انتقال سریع خطرناک‌تر است، در حالی که ازبکستان با مالکیت و بازی ترکیبی می‌تواند فشار ایجاد کند. با توجه به ماهیت دوستانه، احتمال چرخش ترکیب و افت‌وخیز ریتم بازی بالاست و آمار نیمه دوم می‌تواند متفاوت باشد.
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140469" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🤩
فرهیختگان:
بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/140468" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUcibl79fXOchyBAUwCj9rSJ74nAhKXbjv5Melj_PHXmr7c3DThvwuc1E5vylEgktBYwWuK3rpz_yWs91SpVLuOF2Gug6D7UBupv5gZPV1XI_tjhFUliKrjlTzwTsK9rDOx5pdQsri9JfpVARgTjADOI_6C3Ro_F2-MloKll8ZJlds6RNT4LSl_L_CweDtbk-ox8QLHUz_tKTXW3ez3UiufzIXnYOYZfmEFhrmgOwA3oRfaWeo7ra3B6Nj4dII7ISzo97fFegfThBBOqyZDzKJbt8eD1jqZkwz7TRwPO6idiqNN2_ADBa1nmSesNmbNYStSzMnXjdjzpYmj-ZEFAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❤️
پرسپولیس در نامه‌ای خواستار برگزاری حضوری جلسات پرونده آسانی و ضبط کامل فرآیند رسیدگی شد
‌
📌
باشگاه پرسپولیس در دو مکاتبه رسمی خطاب به رئیس فدراسیون فوتبال و رئیس کمیته استیناف، خواستار برگزاری حضوری جلسات رسیدگی به پرونده شکایت این باشگاه از یاسر آسانی، حضور رسمی نماینده باشگاه و ضبط صوت و تصویر کامل جلسات شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140467" target="_blank">📅 01:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤩
👤
🔴
فوتبالی: تارتار بعد از دعوت نشدن کنعانی نگران وضعیت روحی اوست و قصد دارد جلسه‌ای با کاپیتان تیمش در این باره برگزار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140466" target="_blank">📅 01:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140465" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIS6xbIdrVZCiEj1yI8KV-raycpxa1_eN19BIKaLh0fkvWuRPAin80d-DaTT4xqnm3FTY2auadv7ljRrRCyH5cYmWWtbX59YAVK3GbWMx072CnL74q_E6TpEmVJ5gpQOZxlMWBAqzNj0-6LR7mqLwA9SnTjfYkjKDnWFjRCg9vCpsaqn_HlXA20m7pBIBy2KYdOel1h_-wpQEGSpPWz3prRWwM-ikUKJY-0hpq0pXGUHQDksTXjr2sDO9OHc6lDU1vQod6veUjXPnNOhGBgB9NPNiAeUHmjMzpQvm8YbpGfO3S8FcDPBNLXiGjINA70gQZCVjZrgNxGaXjZdXOvPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🇮🇷
سه درخواست رسمی پرسپولیس در پرونده یاسر آسانی
🚫
باشگاه پرسپولیس پس از ثبت لایحه تجدیدنظرخواهی در پرونده یاسر آسانی، طی نامه‌ای رسمی خطاب به مهدی تاج و ارکان قضایی فدراسیون فوتبال، سه درخواست را مطرح کرد.
🚫
این درخواست‌ها شامل برگزاری جلسه استماع با حضور نمایندگان و وکلای باشگاه، ضبط کامل ویدئویی جلسه رسیدگی و فراهم کردن امکان پخش آنلاین آن با هدف افزایش شفافیت و اطلاع‌رسانی عمومی است.
🚫
باشگاه پرسپولیس ابراز امیدواری کرده است این درخواست‌ها با توجه به اهمیت پرونده، مورد توجه مسئولان فدراسیون و ارکان قضایی قرار گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140464" target="_blank">📅 23:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eE2RcREKKcwCW1SEEXcXv4DD3cLgbxs9DkA8ptxUQxIgWtQg9Azqb8t2ApZbvyGQfFbJpSCtrtv_Larno07jzau0KZtxwCGepm5ELR6zea-s1gJLr-YSSlkb985emf_IaqFLFdLKDKjqzypHUs7awrdt5b3abU6OFNjQCBcPMxtE2RgJanhyjz5BYmO4C8Xq0db9xvfF4e7YmJpsOTYY1hAkCMHQqO0DwfXtcWeKHQGLTOGeo9pmUeCjUhtuRzkXRCKxn06cKI92Kdo6E0_b_Ag6cxaOYNWmejgfBeQKwdJa022SnHRWL1sb64cKYxEInP60CTPBKykZ5kAg4SpP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سعید آقایی: در پرسپولیس کم بازی کردم اما بیشترین لطف را از هواداران این تیم دیدم آنها را از صمیم قلب دوست دارم
❌
بعد از مصدومیتم در نساجی کلا فراموش شدم تنها دلخوشی‌ام در یک سال اخیر فقط هواداران پرسپولیس بودند که جویای حالم میشدن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140463" target="_blank">📅 22:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
در پرونده‌ی آسانی، پرسپولیس در استیناف پیروز میشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140461" target="_blank">📅 22:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjE9PhjsUkVOa5h9RqBHp9oMi6vUMyGktfSejW61aniDcI1RTpKUEd6Su8kbx8P6kOHy_gg70k3_uvG6il8f6MsDn53IWL6lLYhwxQErIr282BZrYk9TCaJ2qHZScSUda5NpGV6EZbF5AktcgeHr-nzd_mOKV6M14y_KDtJHZMUXw6HpDgZhhIGEs3l9YL8Kj7C3qebUoi62KYtv_Vuq2VvtaSSZDxvtZqjIw1DyXHZ5jUVPUkfD36F0HWHxte87XEXqlJ5xxReTzb0o2lsXrTxaGQ1MlZ_Q9XQZV5VSHCb2yqtOtQ8Di_LrL0kQpHiLV-BWcdoa4mlaqfRP-sN39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
حسین عبدی: مقصر اصلی شکست من هستم، اما بچه ها با توان فردی خودشان فاصله داشتند از مردم ایران عذرخواهی می‌کنم
✔️
✔️
باید به کره شمالی تبریک گفت؛ آنها خیلی خوب بازی کردند. باعث تأسف است که در این گروه سخت نتوانستیم پیروز شویم و به مرحله بعد صعود کنیم.ما…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140460" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140459" target="_blank">📅 22:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140458" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140457" target="_blank">📅 21:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcmI_rx8LSdU1acLTogkpZX_BX-Ljs_sLFLFw6S7_RZAdJKfvKN_ArX_yMIuwNx29iNpUxbht57TI7WGjFDVP0mJYvicXx974eHQEiT-LEX-64DfA0wX3pAscEbE7uGNFnfCxAy7rGGz8B3kKEdgL_3hd2CTJU7xliOPirBmktsSZqfN6L8OJPAlS4BuutnNNLr2zwmk8HVr6oXMO8tqdByG6RY0ZApp8lc5_OmdHkqoqUKjivr5Sq-30tQjc5pxR3zJrb-IZT3t69fPCgrl9g3ZKbhCWDUzKxKbT83vZBYu_D50WKid3qDj2lTqbs2z3yTnLXs5uE6XCVAJjn7c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایتالیا مقابل فنلاند در یورو والی؛ جایی برای غافلگیری نیست!
🏐
ایتالیا در این مرحله با ۶ برد متوالی وارد یک‌چهارم نهایی شده و در مرحله قبل دانمارک را ۳-۰ شکست داده؛ فنلاند هم بعد از یک بازی سنگین ۳-۲ مقابل یونان صعود کرده است.
ایتالیا با سرویس، دفاع روی تور و تنوع حمله دست بالاتر را دارد و روند ۶ برد پیاپی هم نشان‌دهنده ثبات بالای تیم است. فنلاند در بازی با یونان توانست در لحظات حساس برگردد، اما فشار حملات ایتالیا آزمون سخت‌تری برای دریافت اول این تیم خواهد بود. با توجه به اختلاف کیفیت و فرم دو تیم، ایتالیا شانس بیشتری برای کنترل مسابقه و برد ۳-۰ یا ۳-۱ دارد.
🏐
اوج هیجان همراه با اسپورت‌نود، پنجشنبه ساعت ۲۲:۳۵ دوتیم ایتالیا
🇮🇹
-
🇫🇮
فنلاند به مصاف یکدیگر می‌روند.
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
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140456" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
#تسنیم؛ بیرانوندیه پرونده تو کمیسیون پزشکی ایجاد کرده و گفته من چون خالکوبی زدم مشکل اعصاب و روان دارم و باید معاف شم
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140455" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnGIQRrXFVMU6siT0ylY9HlNAjh8tOh52XuZPyJMpVnk22dPlYjpi5_nIdGVZBVBqSnOn1jtAiMOjA6y3Qby_qOXZyYjbxdSZluIafIP-PCB-cjjsBUj386U6-w41fnPaJdcK8QPAZVp_Xf39L1KavUtPBUyofRDDCIOJNiNaht69CUQO3832kxZDVKsMeZbVcLfLIcvqdA9imDNDYRGlNJKoNQNF3YsZebHZzFr_KQrtMnSsNde48atpEMNTyvGAEWaTH_m7EPPOT4FCT2zOqCkJdfbj5v6YRc3MylOCIzpzO8Sy7Gz5m_BEkeXxxJiZiWFREnPN8n5uZwFQ5bjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
⚪️
رنگ پیراهن دو تیم ایران و ازبکستان برای دیدار دوستانه مشخص شد و ایران قرمز میپوشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140454" target="_blank">📅 18:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140453" target="_blank">📅 18:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUTLaZSWKyi-mpUyPtr1wjqoTUWHDe-N2W_XHqGt85yTAbsaIcCH6Atw-9hyAbfthRInYMBTrNdUPe_CnwNA9P9Msbtp97O1vD0wcX-k2Pq4f144_bzfe4S4HomWURW6ibhiXyrVo7hZBB3isOVduDWQH5xEuL-Cx7RVlvDOww84CO8RM1JC9UVnxiyB1Y7KHsuDC42V0-bEqR1ffNIXyTdeyjpYxZAM1kpRtFe9NQ5bEc20lGdYZcruqrlzVH-uZgb4K0F-Wb4NxM8kj_Fm7LoisCx7Z5Kin6XvoI4eJLQfxQoKvGg3hwu3zV_eLzp1UlaYppQ7Pp_sw832rASMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ارزش تیم امید ایران: 13 میلیون دلار
🇰🇵
ارزش تیم امید کره شمالی: 2
میلیون دلار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140452" target="_blank">📅 15:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgklBf0oSUYCFqmVS8w2h6FH7zhMw6Kf7_q_Q6Ma594yOURuqM57XzSCcCK9oVWhhXFnNK0DEvvquRaFcL9vRIqNAoYCYjbQTMfrIIfrFhg8ZWcEQVJJkFZUgA7RF5eVKabwtEbb8cMRxVPVJj_0A_7l7PEOdOEEFaD_FoCXMFP4cwJYb9-Xbf8aHYPHU6BmN2mTHitvTEWPeZLC-sOb4TF9jvWoSn86CAFdyjY4jCqwZKcA3zvS6pGIgjF-AxKhxbTxTJOGnTRDzeN6otLDTUPRNQOuE3-1pJkDz1x5v8cuq6DJyA2FI73HCeN3aLoTnhLbWQXVKiGG7nF8CoQApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140451" target="_blank">📅 15:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XINn7KrKML6dpbmwvlifIJlQs_dhQada6BmEqh_ydneOCOnzw0U88Wt1mp396XBwI4PHqTQPtcX3sSY15UgyfxCvfgAvKpI5SZ3a_hVrpS6Lf5fqnXhz3grUSJCmZdtyHE2gWBBZF8zSVnGaY2DbcZwlrx8jzyfyHnYEMS_CsBTlA9AlVFzTmAO-l8f2APLhA4UwC-aW5IoxUNm-iOtnNUSNAAwQFPFhUWr4EtzJTzsPFlJGfrXX1YuGbBxlKqBgD_rp7lyNiBEZHk0B3Pbr_I7F-HM-AqTWg3hSHw2LXlcPy9qAadOTgXi7I8cNTt-3n6nuwERp032bE9BRBMVlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا به اوج رسیده!
🇧🇪
Belgium -
🇸🇮
Slovenia
⏰
Tonight 17:30
🏐
بلژیک با فرم هجومی خوب و درخشش فره رگرز وارد بازی می‌شود؛ مقابل چک هم ۳ - ۱ پیروز شدند و ۱۵ امتیاز از دفاع روی تور گرفتند. اسلوونی اما بعد از برد قاطع ۳ - ۰ مقابل صربستان، اعتمادبه‌نفس بالایی دارد و موجیچ، پایِنک و کوزامرنیک می‌توانند فشار زیادی روی دفاع بلژیک ایجاد کنند. نبود تینه اورنات به‌دلیل مصدومیت، یک تغییر مهم برای اسلوونی است؛ بنابراین دریافت و عملکرد موجیچ اهمیت بیشتری پیدا می‌کند. بازی از آن مسابقه‌هایی است که احتمال کشیده‌شدن به ۴ یا ۵ ست در آن بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140450" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140449" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد حسین کنعانی به علت مصدومیت دو دیدار بعدی پرسپولیس برابر صنعت نفت و خیبر را از دست خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140448" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140447" target="_blank">📅 12:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=L-vkQuMYaI36wnpRaUFILxIVa0sgqf40fs_W7HzzNryACyTPVFI9vuajfeAIrm31PSp8CNbhlkNYomOHGyFYsB60Yf208Wt_iuQVCQrMFXDu06Aqu24HZW9NkGKbeHLTuo0FImSi_0-mq5zg7GG3M1uTOlpxRCw_DEkugEJtkvN8OsZaxloMsZOq0xvv3yA340dwYRc4pLBYrAyo7bavEx9qOaci81kRv0pUwIsF9fV-6r8vt9oD-DTVDHHTBNGd5hHpI7YNBFCrzJO4Az8k13WB9Tpvs-rt6VbSqJUJPqRutci5PsoUKwO0_fHSEq9AHy5QDmdONb8nDsBrbORBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c126edce8.mp4?token=L-vkQuMYaI36wnpRaUFILxIVa0sgqf40fs_W7HzzNryACyTPVFI9vuajfeAIrm31PSp8CNbhlkNYomOHGyFYsB60Yf208Wt_iuQVCQrMFXDu06Aqu24HZW9NkGKbeHLTuo0FImSi_0-mq5zg7GG3M1uTOlpxRCw_DEkugEJtkvN8OsZaxloMsZOq0xvv3yA340dwYRc4pLBYrAyo7bavEx9qOaci81kRv0pUwIsF9fV-6r8vt9oD-DTVDHHTBNGd5hHpI7YNBFCrzJO4Az8k13WB9Tpvs-rt6VbSqJUJPqRutci5PsoUKwO0_fHSEq9AHy5QDmdONb8nDsBrbORBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بهت و تعجب ملی‌پوشان امید بعد از حذف از بازی‌های آسیایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140446" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHVeMx0i8xgZTT9uU2l96E_HQW5vnqEn8Urze9sDUlJX_CkrI4BvJ1qA3iGMY-H5iDAYGDW8f_TI9Ick9ghuWr650lOX6lyyIBQ6q7dFYScdmdcwdGyDvCPCkHUH_FqMfLD0LWoXXvxLgsKsH5atO6vxfkkj9NVU8x0JCTPVY5bNTkSAmOl0DtIoQ2Hs3FreVHSGwLTnoQi4vQ-bDHOZTFnZO99-eSeCha6JMOoCKeNKdbn5Vyi1AeyJPJjV-hf0CUCKdV-vZ8n1lii2IiLa3hS2vqlmr5uemeiWqjVmnXbkZMEnHky5DdfTvifqw_3G14I1FtBMEmkAetKsdCT9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تیم ملی امید‌ با این کادر با دانش به کره شمالی باخت و حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140445" target="_blank">📅 11:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140444" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140443" target="_blank">📅 10:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=Xg2piODuPf5840ljO24IVfapoY7BGNPoMITKenWDAl7Wi9hSt_va6NOaC0zQJRTEoX48D6L1uFiegzCqpf54o-bMcTOxi70Mc4yF29VBtnNkrEjnyyd_rjGlsy1X8kc5uebwqdyU2cPb1dlyXHEgAt0WBf4g58epzZiGhmqHMU0ih23LzjmbCXC8PS3whfAjAtqmXWpLUdYn3NhGmgRbkeW2lGqe7IVeX4Sar5Kbu_CmqlSvYKgBFrHE3hdHjav0_-ksLoPs5ZrSCvkTQKbNUq-V4FLgAHmTcq7squ8LZriIz52w3EHn5ppfT1ELVnMlp5zulrYMaHM0btpVCOgQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29d58e82a.mp4?token=Xg2piODuPf5840ljO24IVfapoY7BGNPoMITKenWDAl7Wi9hSt_va6NOaC0zQJRTEoX48D6L1uFiegzCqpf54o-bMcTOxi70Mc4yF29VBtnNkrEjnyyd_rjGlsy1X8kc5uebwqdyU2cPb1dlyXHEgAt0WBf4g58epzZiGhmqHMU0ih23LzjmbCXC8PS3whfAjAtqmXWpLUdYn3NhGmgRbkeW2lGqe7IVeX4Sar5Kbu_CmqlSvYKgBFrHE3hdHjav0_-ksLoPs5ZrSCvkTQKbNUq-V4FLgAHmTcq7squ8LZriIz52w3EHn5ppfT1ELVnMlp5zulrYMaHM0btpVCOgQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چهارم و ببین ...از وسط زمین طرف تک به تک شد ...این چه تیم امیدیه ..آقای عبدی چه گوهی خوردی با این همه جووون با استعداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140442" target="_blank">📅 10:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
آقای حسین عبدی ..بهترین تیم امید و ریدی توش و تیم و حذف کردی و از کره شمالی چهار گل خوردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140441" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140440" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
چند روز پیش یکی از نزدیکان میلاد محمدی به ما گفت؛ این بازیکن بخاطر شرایط خانوادگی قصد بازگشت به ایران رو نداره///طاهرخانی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140439" target="_blank">📅 08:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo7VFVQjRGgh-Qpi8JCCt3xdt2Pbde4fjdr1EHz4O_tX2YM5f2ndtouQTyOD6n67lcQ5rTw3dYCJ2EOOX-onLWL8RXGgSD5NQTg3dqZOeFOKzzwkiehk5jh0cGiwV7pPN8rVUkWa-IXSsaBQRS2aRpp5oao-iKw-LBPD-xisWcuz6JAzSNp7NslUNLTWEEZKe1eaiaRyFahbjMCACz82L0Sp69MmZd85Efif-bUnux_gY5V4YjNi9NnD6h9dCm_MpKEPi4w9IInVCHdlvk9KltB9SHD2aLTFIEopETdSXn4KOFbjEiCuTXFl7vWN47Nf_d2UI9aUXSvTHIvqpE-Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🤩
خبرورزشی:
🔴
🔵
🇮🇷
پرسپولیس و استقلال در نیم‌فصل برای جذب محمد قربانی اقدام خواهند کرد
.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140438" target="_blank">📅 08:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
✔️
علی علیپور به دلیل مصدومیت زانو حدود سه هفته باید مراحل فیزیوتراپی و آماده‌سازی را پشت سر بگذارد و در لیست تیم ملی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140437" target="_blank">📅 08:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140436" target="_blank">📅 08:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
صبح اولین روز پاییزتون بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140435" target="_blank">📅 08:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1k2sr0LGWmiqzl76YXikCWtwmbMLLwnIf4O6maJCV5zgTJasKzOVKlj1gfgsvwStXfQskxvxED2TyaiurKvRQOYjxfdRi8d30oDE96FeRHifuLw1XCzN865CH5WreYj2R3K5Dje0o5idqfiUm7hYAIdG91JhDrF-F6RM216LLrlGMWF4seffK0OI_UIAE-tLYCArUQc6FIYe3PNI7IdwQKL3BLTeR8mlTnB1nLRMyi1BF_jikg3vc3rbInfbrRkWDpc9ytcOT0nAPe8hqDW3S-hri2ArkbHQyg_MmZHHkbe_3GtbrJNiofye8Z1Cwq77fGPWc1kdOtwfMagzQ388A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
IRAN -
🇰🇵
North Korea
⏰
Today 09:00
🏟
Wave Kariya Stadium
⚽️
تیم امید ایران در برابر تیم امید کره‌شمالی در بازی‌های آسیایی؛ جایی که جزئیات می‌تونه سرنوشت بازی رو عوض کنه. ایران با تکیه بر مالکیت و بازی ترکیبی، دنبال کنترل ریتم و ساخت موقعیت خواهد بود. کره‌شمالی هم با انتقال‌های سریع و بازی مستقیم می‌تونه دردسرساز بشه؛ انتظار بازی نزدیک و کم‌ اشتباه میره.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140434" target="_blank">📅 06:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
فوووری / میگن کنعانی مصدوم بوده و رفت شمال و از زانوش تو تعطیلات زیادی کار کشیده و پاشو بگا داده و چند هفته ای نیست ///فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140433" target="_blank">📅 00:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140432" target="_blank">📅 00:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=ulnoJZ63xedIX8H2dfWnShS_t2siUnxeoEErdNBSU6Fwoaoq-E-LaqgS5SWbpd1PmR5UojnfH3j9yquoW3kx93iCcXJ1ZwhTPoE-yEGhhXKDqdJajqEhLvTKTIpbJzg6-nRazopuV2wecyivnxAuqUEet7fo4eU6Drhpn0QjIjxTbj7Bu8ehi8qtJZyh-SnLCMKsYec22Fc5Mr_8liYRb0XEu8S9JVmN2oY1OTE97H5Nos87_ty6vmxGvZd7ZVA6bz0u29jzMlZrQWzMwe2bzGfNCxu_BGCep9ElgwkF_y4759KEW34SH8vzxMnLNCtDHHDZWa5cbhju1KZ89Dw3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd12c24d1.mp4?token=ulnoJZ63xedIX8H2dfWnShS_t2siUnxeoEErdNBSU6Fwoaoq-E-LaqgS5SWbpd1PmR5UojnfH3j9yquoW3kx93iCcXJ1ZwhTPoE-yEGhhXKDqdJajqEhLvTKTIpbJzg6-nRazopuV2wecyivnxAuqUEet7fo4eU6Drhpn0QjIjxTbj7Bu8ehi8qtJZyh-SnLCMKsYec22Fc5Mr_8liYRb0XEu8S9JVmN2oY1OTE97H5Nos87_ty6vmxGvZd7ZVA6bz0u29jzMlZrQWzMwe2bzGfNCxu_BGCep9ElgwkF_y4759KEW34SH8vzxMnLNCtDHHDZWa5cbhju1KZ89Dw3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زهرا خواجوی: گذشته ام را نمی توانم انکار کنم ولی امروز پرسپولیسی هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/140431" target="_blank">📅 00:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140430" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
امیدواری پرسپولیس به محکومیت آسانی
❌
❌
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند.
❌
❌
پیگیری‌ها نشان می‌دهد مسئولان پرسپولیس موضوع این پرونده…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140429" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140428" target="_blank">📅 23:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
بیفوما:
🔻
از لقب میگ‌میگ خوشم می‌آید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140427" target="_blank">📅 22:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
تیوی بیفوما: مدیرعامل در اردوی ترکیه از من پرسید چه چیزی باعث اذیت شدنت می‌شود؟/ تارتار به من گفت به تو اعتقاد دارم و شرایط نسبت به سال گذشته، تغییر خواهد کرد. هدفم قهرمانی با پرسپولیس است و نشان دادیم می‌توانیم قهرمان شویم. شرایط امسال خیلی بهتر است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140426" target="_blank">📅 22:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
تیوی بیفوما : بهترین دوست من در پرسپولیس حسین کنعانی است / شاید انگلیسی خیلی خوب حرف نزنه ولی خیلی خوب با هم ارتباط میگیریم / یکی از دلایلی که کاپیتان شده به نظرم اینه که خیلی خوب با خارجی ها ارتباط میگیره و شرایطو براشون راحت تر میگیره و این خیلی برای…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140425" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140424" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
تیوی بیفوما: در خونه بودم که به من گفتن که تیمی بزرگ از آسیا تورو میخواد که تو لیگ نخبگانه و با النصر میخواد بازی کنه و به عشق کریستیانو رونالدو به ایران اومدم تا مقابلش بازی کنم اما یهویی دیدم استقلالی که من رفتم توش استقلال خوزستانه نه تهران
😂
😂
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140423" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
ترامپ: فکر می‌کنم درست بعد از انتخابات میان‌دوره‌ای با ایران به توافق خواهیم رسید
🔄
🔄
آنها منتظرند ببینند من در انتخابات میان‌دوره‌ای چگونه عمل می‌کنم. چیزی که آنها متوجه نمی‌شوند این است که من نامزد انتخابات نیستم. من قبلاً این کار را انجام داده‌ام و با…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140422" target="_blank">📅 21:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
تیوی بیفوما : از چیزی که کادرفنی از من می‌خواهد، خوشحالم/ وقتی همه چیز با کادرفنی خوب است، من هم بهترین خودم را به نمایش می‌گذارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140421" target="_blank">📅 21:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
تیوی بیفوما : سال قبل با انگیزه فراوانی به پرسپولیس آمدم/ پیش‌فصل آسانی در ترکیه نداشتیم/ شرایطی تجربه کردم که امیدوارم هیچکسی آن را تجربه نکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140420" target="_blank">📅 21:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
✔️
✔️
❌
امشب ساعت ۲۱:۰۰ در تلویزیون پرسپولیس؛ تیوی بیفوما و زهرا خواجوی دروازه‌بان تیم بانوان پرسپولیس مهمان برنامه هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140419" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140418" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
سربازی فرهان جعفری در نیم‌فصل به پایان می‌رسه و راهی پرسپولیس میشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140417" target="_blank">📅 21:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3M4dvOk2i1fZtHtZvORoAYimrs4L1Y9huKzEvedaBAIITKkvQVGdYEBKnJSw9fSBIBOjhc7qaoDrajm_-qb2L2CFKh2izYE4foos1vcnjSR0QCZvwJIxXT3v4vybx19tRlEG5fdMgdKKr26KubExbeO9q2H_u0LvMC2DtfMiPQYoeit-T0wv9q-fKBJgshL6Lr6qP93cFBaubsX-u3nhbAPykcZMoSOMuMUw7hP8PTwoOg2XPU73rkRml7TcJ5tlvEmsNegwEBL7PAGO_SZiJ-4nGTqnHaMhf9yk5GJRoakqzunKr6foGH6S1Js3j_s5J8Uq7wRwOSH9So8UVLAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140416" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140415" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ایرنا: حسین کنعانی عکس جدیدی از مصدومیتش رو نشون داده و واقعاً مصدومه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140414" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFpx5D8nOLTA3FlHZXmaNVRh6J6MYRB4-CZEnCP6pm3xtAZD8FZbXE1f_Dst3MAEcYG2_882HUACQa-qwOj8apblJwqjzlMoVjKnNUWk9Us_OcnDPtyrr4sUqOCE02etrd9MrZhjXzq3AU-c6o20z5XRRFBHJ2r2TfE7jvPVz-bp_P2LcrWNhzYqjkFOMMywccXVTMIC4L4cwZcFyfUDeeUIPHQyhmYWQVKxn6beSKR16o_oOEw4HtMcI08pVKVlDKI7x7LbDp4ZHjZkofprswArLfCHipZPUXM_sH7R2aY570EcyH7_UM8zkW2Jey7Ckq3PmqWP2lcIY-jB8Pf0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا
🇵🇱
Poland -
🇩🇪
Germany
⏰
Tonight 19:30
🏐
لهستان با نمایش مقتدرانه مقابل لتونی و برتری ۳–۰ وارد یک‌چهارم شد؛ آلمان اما بعد از کامبک سنگین مقابل بلغارستان و برد ۳–۲ از نظر فشار و فرسودگی شرایط متفاوتی دارد. لهستان در سرویس، دفاع روی تور و کیفیت حمله دست بالاتر را دارد و اگر دریافت آلمان تحت فشار قرار بگیرد، کنترل ست‌ها سریع از دستشان خارج می‌شود. آلمان با روحیه‌ی کامبک اخیر خطرناک است و اگر سرویس‌هایش مؤثر باشد می‌تواند حداقل یک ست را از لهستان بگیرد. با این حال، بازی از نظر تاکتیکی بیشتر به سمت برتری لهستان و تعداد ست‌های بالا می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140413" target="_blank">📅 20:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند؛ آنها یک اشتباه بزرگ کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140412" target="_blank">📅 19:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140410">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
#فوری | ترامپ در سازمان ملل:
🔻
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
‼️
🔻
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140410" target="_blank">📅 18:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140409">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
سی‌ان‌ان: دونالد ترامپ به مشاوران خود گفته است که اگر شرایط مناسب باشد مایل است با مقامات ایرانی که در مجمع عمومی سازمان ملل متحد در نیویورک حضور دارند، دیدار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140409" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140408">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
🚨
⚽
محمد قربانی: بنظرم در الوحده ماندنی هستم باشگاه رضایتنامه مرا صادر نمی کنه
🆕
👀
چند بازیکن جدید قراره اضافه بشه اما من در لیست فروش نیستم چون الوحده هافبک ندارد  ‌
📎
اینجاست که مشخص میشه چه کسی دنبال فالور گرفتنه و چه کسی…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140408" target="_blank">📅 17:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140407" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84777f345.mp4?token=HQVDs0wAqUlovmsI2In0Z_c_ltX2nMzPWFe00Go8hktR3tqA8vRyIJ_q0HwDWd3lvt7qylUXSL8NuZmyVxGLZYWmKx8Dxs97nLTylMwrEAkcKzUWZ6r5XuCPGOPpgH5-3QXFAxpA1OTKbnNYaR10g6J_0Cbm2v2AVh3D2xnbLBF8rU1wzHRRd-q36otNQmMBqunjnaiOB2Kck8bb_6mWxRFYvFjqwDbmWJciPGTQautfXGrn0BGLV4hTnTccIuR_veAU_ac3D0wBXqXrUwShw7AZgv0BLw59iDtulkHt7OObDJiU_zYJ9WSW-EuB4Pawc7cSqAt2atg3mNiSmVMCH4SBqtl3I4Qr7B5PJABVlY0i4qIB-GUVxYn8C11Vy3Vf9tIjyj8M7j2ug6hglI9-pVa-hQiMI0wHuFE4Yak6JPxYkErFYan11zBWip63stDIesDmiMG1pQlk4ag70qbkOSBdQMnY9rEQhTNnASUBfDKoe7FecRfANCjqg_p2yLS8KsGfMW7vyOzMktkJuiNZUVGxjdEnQ-QsAerIhJVoMFHFshFpXj1DA8lhtHnJxyGzimsHgrlT8mo2p2bdl9FhzC5A1LlXMygnYuiQwbwo2iIreCmLXNmsjW-ufWZDoj41suYb9Ip_7uFYMSNDBtjSCqLS4N7uTNwlWHvsdRbV6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84777f345.mp4?token=HQVDs0wAqUlovmsI2In0Z_c_ltX2nMzPWFe00Go8hktR3tqA8vRyIJ_q0HwDWd3lvt7qylUXSL8NuZmyVxGLZYWmKx8Dxs97nLTylMwrEAkcKzUWZ6r5XuCPGOPpgH5-3QXFAxpA1OTKbnNYaR10g6J_0Cbm2v2AVh3D2xnbLBF8rU1wzHRRd-q36otNQmMBqunjnaiOB2Kck8bb_6mWxRFYvFjqwDbmWJciPGTQautfXGrn0BGLV4hTnTccIuR_veAU_ac3D0wBXqXrUwShw7AZgv0BLw59iDtulkHt7OObDJiU_zYJ9WSW-EuB4Pawc7cSqAt2atg3mNiSmVMCH4SBqtl3I4Qr7B5PJABVlY0i4qIB-GUVxYn8C11Vy3Vf9tIjyj8M7j2ug6hglI9-pVa-hQiMI0wHuFE4Yak6JPxYkErFYan11zBWip63stDIesDmiMG1pQlk4ag70qbkOSBdQMnY9rEQhTNnASUBfDKoe7FecRfANCjqg_p2yLS8KsGfMW7vyOzMktkJuiNZUVGxjdEnQ-QsAerIhJVoMFHFshFpXj1DA8lhtHnJxyGzimsHgrlT8mo2p2bdl9FhzC5A1LlXMygnYuiQwbwo2iIreCmLXNmsjW-ufWZDoj41suYb9Ip_7uFYMSNDBtjSCqLS4N7uTNwlWHvsdRbV6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
7 سال از گل مهدی عبدی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140406" target="_blank">📅 17:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140405" target="_blank">📅 16:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
ادعای عضو کارگروه حقوقی تیم وکلا امید عالیشاه: خداداد عزیزی با شکایت امید عالیشاه می‌تواند راهی زندان می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140404" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140403" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140402" target="_blank">📅 16:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140401" target="_blank">📅 16:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140400" target="_blank">📅 16:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140399" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140398">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLsD1QaK876TrDG-bibR6F9y6IRUh6_INjytkzfE4U0WzoG3umnvTcQiYqDDx8W7Sq0tWWllnl5_-yS5xDzJou780ZApmD2tR0WKNmKJXMEGvYi161qkOjIqmBdiltYAGaJlu08xa6n0Iiny1szchjT0hRWi51s8wcatDDDVH8xTG4KtbIKwVOJngX6Gdz0YSjGjCVucN6WOFqn3Y_kLVocQjgFUgX4m6EtKq4_bFZ2f3aB8xbCijg2J_NRKie2v3GcNQLRWUSeO7V3L_dErAqIDUCneTWuQZ7H-3NzSlYeyMgOKpC8SFr_2sYF9pIOdFl3kU7k4nf53clDb20qwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140398" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎙
🔥
تیکه
سنگین‌ ابوطالب به خداداد عزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140397" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140396">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=Mhy4vkRRXJ0e-ZBsZ-2qnLxzOYrJQDI5d2vE45dcsEN8PsxpVLQPi7Fea_YUNOrXPtc2BZ3yoyMxzFfC3dfB1oNDvZHzZ6DXlL0ikxwTX3e9wD8Ni4FNyK3XRVzlGGOjZmFM2oQeBcfAydJjZAm_KUt0zqNwvTvUR_WOKiKZbqzXr-zQWGX5-BDWvcFVjSVnlCutSNqZCqXO0KAaLEj5SgBVaMYRtpLkvMWQhlhSxhxbvJ0C0ILWXE3K-7tD-mK6Lwddyhj0l1zpaYarVr_MKqb6HFM4n1ECRzxRBOF9teff3qNJlHnqiXObEepIQMiJ25cGGeRZB0h5cGIfjY6Mjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=Mhy4vkRRXJ0e-ZBsZ-2qnLxzOYrJQDI5d2vE45dcsEN8PsxpVLQPi7Fea_YUNOrXPtc2BZ3yoyMxzFfC3dfB1oNDvZHzZ6DXlL0ikxwTX3e9wD8Ni4FNyK3XRVzlGGOjZmFM2oQeBcfAydJjZAm_KUt0zqNwvTvUR_WOKiKZbqzXr-zQWGX5-BDWvcFVjSVnlCutSNqZCqXO0KAaLEj5SgBVaMYRtpLkvMWQhlhSxhxbvJ0C0ILWXE3K-7tD-mK6Lwddyhj0l1zpaYarVr_MKqb6HFM4n1ECRzxRBOF9teff3qNJlHnqiXObEepIQMiJ25cGGeRZB0h5cGIfjY6Mjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
❌
جواد خیابانی: فصل گذشته باید از تاریخچه حذف شود و هیچکس نباید قهرمان اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140396" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140395">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKkwgOIJds-pP7_564Eg8iYBtHriSpAOSkCJp6rTI7sOl-pDEnxl5W_BNh9pN-t9shEIm49dkUycBdFD99y9__AhnUorcPQktW_O-PNddN4AffP7D-FBkg2UGDeOTusodFDRqH4cqAXWzfXwqi3BM1j0gI9pd8RBtz2sazTapLpwSK6aul-sNhVD9Ob6OBOIVbJ2tTWtPQhJs9g2tiilir6LLXQtxYDv3ECPom0Uo34HEUu-8uFvQvYJajKK74CQ8sr32Ryh29SIu_TDj_1nFe7MfcpOdKntZiahil8C-HmL3blI8N3dOj0yLsA-JzzUtmsjTQPBFbgpB6bmTkaH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140395" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140394">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZwyVid674NQuJKbJz39m0YYpx-wuQ6RZ4gtIA0_fAJA9uH8GJfgWaKHcMDZd_36R8msTLzNeJWY9f8BWLsoO7irYTlLzBi_kwl0SSN3K3D_IxGfSjLc7vAfeyf8UJ-jVAHczY_qMB_GqGqeF9X6_Zdf4lF8JDrJ-vFs4QNJ6Zs9hfSciCqEwtGIcfRQIvNLM5RPDnylobUq-37Sl7kqdKb1bFzAsXk92pPOuNZNu1U-a8TZe_nQ5h_OY4SURG12Cs3tnQlLsWRr3aTcOeEq_SAFni45uXIGVTiz9fcjnd_oXUZvBrHC2QecepBHg1AMC9K6Y0rBEayjv7t6MiGfXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه نوشته
:
🔄
دلیل عدم دعوت الهیار صیادمتش به تیم ملی این خالکوبی و حمایتش از اعتراضات ۱۸ و ۱۹ دی بوده !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140394" target="_blank">📅 15:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140393">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140393" target="_blank">📅 15:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140392">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت!
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140392" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140391">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6lSnn_olett7ou3HKunUTYJAgVmEdZFZMEi7rO63LoK9AljQi-1P73dPogx4xjTMNeLbAfo3r5mjEVm9R9yPTWTHpLSiY1i5s-d4vwlLC_DydiGkrSDypbWMraAE4u41Twshgz9rRAIMi-ewR1MX8rcP3S2H55mGTmDZ2Bn8K0pyzFHu2wjRRyz-yeUim1XRGVBrwL-QFnxjGTluhhYfhSeWGQ5tQRAUpxmkmIqT0VcQEK3xlefmq2Hcv7t_mhwWqnb492Og9KA5KeSQmkLURgwH0NTPG8CCOy3BGIh1-fv9fxSXQfwyULpZIeuwC4S2kuwmUZICW1-ZYSZlpipGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آلمان و لهستان امشب در یک‌چهارم نهایی یورووالی ۲۰۲۶ به مصاف هم می‌روند.
🏐
لهستان با قدرت سرویس و تنوع حمله، دست بالاتر را در این نبرد دارد. آلمان اما تیمی جنگنده است و در امتیازات حساس به‌راحتی از جریان بازی خارج نمی‌شود. اگر دریافت آلمان زیر فشار سرویس‌های لهستان دوام بیاورد، ست‌ها می‌توانند نزدیک پیش بروند. در مجموع، کفه ترازو به سمت لهستان است.
🏐
اوج هیجان همراه با اسپورت‌نود، سه‌شنبه ساعت ۱۹:۳۰ دوتیم لهستان
🇵🇱
-
🇩🇪
آلمان به مصاف یکدیگر می‌روند.
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
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140391" target="_blank">📅 13:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfaUOtKjsyNfcgbxTVkHvJlJO07Sjuo0iEj90BdFJFdqCTlIF5ezxTsL-D8uK_-inKL-qAd4Z2o4kF6Z8jFc-RGhIXM55g4LlgZeIGxg3MNDXSGjZuGiTOh1oUa2msV7m4gTfb9LwjrhwIoWUQhRxQ8aETxhxXYtJlyhTo1qoLteW0rRn2llLHbH29m1AmkQgbQ8KkzH8hwRl8q0AL1UUWFj2iy6XGFs2OfmU5gpa7EoWcJcy7Q_Wey7jD88D6pt5Ln9Yw7e2tmjmtHu15sE5-Itv1OgypcXuCy0h75Dj_EatPSFTPKQvrI-zfUO8TBt7GAs56cgNBIRK4krOqCP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140390" target="_blank">📅 12:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140389" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140388" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140387">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsl5QIRblSTnpYuv6LWj2Arp7p-fMfkAAYHjaebDm7mbbIu8Q8sH4Tcs2vMFv4ZxFiPLkLDO75JgE_6Z4GnYx8BHkEFpGq-Q88UR1kejB-v49JIuse2Fe6UkXH5YJ8PKVe-9UTawrv0hoNvx74whHzr__je6XbCoZx3eqItbhS8Yie5pfL547mRHg2Ajk6lv9TXbdBsNiojWvp1wVCSwgt2Np329Tbw_k-UuJkGCAZQiUBud811SpmOuc7tBOD8S8wHlU2Hy9Nan-UfSrPAnJ3JxZiz_dmIt2bs4PAnm4UtUBoV5td0jjECjgUVnltXPMFQ_Qqm6Rqr4lShgzyC3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
پرسپولیس در تمرینات هیچ مدافع میانی تخصصی دراختیار ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140387" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140386">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140386" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140385">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140385" target="_blank">📅 11:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140384">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140384" target="_blank">📅 11:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚡️
⚡️
با درخواست اوسمار ویه را ، امیر قزوینه گلر تیم جوانان پرسپولیس به تیم بزرگسالان پرسپولیس‌ پیوست و قرار است به عنوان گلر سوم در کنار رفیعی و نیازمند به فعالیت خود ادامه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140383" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140382">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚽️
صبح آخرین روز تابستان شما بخیر ‌.امیدوارم شش ماه اول سال و با دلی شاد و تنی سالم سپری کرده باشید ....پر برکت بوده باشه براتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140382" target="_blank">📅 09:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjNCX4UgDPQkeHICspTDXzcO3awiGs0k9-M1VhQNqPJgnExsQHk1TrzFzaM3WLhfXkw5a_AhzDQhNU0ENY6lhgIx58K_WKhgBx3EZVuKziScZP810MVnny97N68YhiVxT87QD5ccReeYZwvAnMiz8iNBbYuvYz2YFR5EsbkbelwP2YNwIMP87Ai3MfF-eJ7h0xpokqhBjVTY7FWMqJy5LBZnQb3Ic9hNfDBZt-OJiS1_gxDNhHZx7uoul8m5XZv9x9dm1CpoMc4_Rko82iaSLB2A2YEl66bSwaNbYpcKL5vGf7CyWvGfdgDXkK4YikZJn7xfWB5gR07TDyo5e7Xkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140381" target="_blank">📅 01:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140380" target="_blank">📅 00:20 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
