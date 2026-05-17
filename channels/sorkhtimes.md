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
<img src="https://cdn4.telesco.pe/file/XjTzlKTIm8fmowK4EN8YY9NsMila3UbIvmwxJ-p3Su8ctj5h9wVyjxJh-SxDopMjjpnhZsDHj7AzCwa7wkkVDvRgcAlBPjso1CgVrsFzDAQzudWslzCR7j4y2XxEqzaalBWGdRhXqQJYVicjEDXlJw1XObHG19G8pGSSCi_g_ieVWbmO6nUHh4XFowXBngQcgIySidL5_UQ59FEjAQ4HAaxj-pbTd52tSASWvfiv28Z8X4HKxaZ1HX_j6OleT3bdddpr_3ZktjXh7brNiEMXSYwcpP575Kx4ASgERC5x1HOwVkLfHNsAtfb5NW68FgNHQemflHIGfU2Ri3x9weJ9Pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 13:36:02</div>
<hr>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5-_yvH88R4gj-VvQ-iXwEjTQ2-heCx7l-lApypz3m6PxWBORZizJqPc3mkd2Ewc_SlSZvhfib3dNSS3ljSiCp4qLcWTianbmcqYQF9EbaypM3qANfWDMWm2ZabtQ86ec5NApUSqBHINLJX4MAJoSsFkdVV5UxPurZsufj0JkKbTmxpGFic9zWxLwlSu01JNpoljx3Qbb9k7xx26gyBBLBpct9ax0_uiCWF9cJq0TPvWu9mSEL5Zd3eY9XgEESCB6uhPMs_0ijC6Qs26vysifJY9iL9JPjKrraBlpORV8djBArKn7ekPzPbcjw8oFVm5n-Sstgg8uDUkMcWvZdXtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
داداشتون رفته از استقلال شکایت کرده
😂
🔹
گویا براش پیش قرارداد فرساده بودن که جذبش کنن ولی پشیمون شدن اینم رفته شکایت کرده که پولمو میخوام
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 106 · <a href="https://t.me/SorkhTimes/131771" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sr5-cdC4hR9JlZMlf86BWZq78pRHrN7cTXpvnfNz4jpH25YHN_HG_oHCxk6op3DzGNkK4BB1_Ka6qZ5ZQ-zXys6euudENCfJay7_i6oMYQ1Qn8UMDRec3Bh6TBDasquJS3d3ZZPPxk7EXPLKCdzyhs9aKQId5-603evuF8G0s0gokvTeCsjO_MhTOw70ZcSHAvlY_PE-Y1blsYfiCRkEv-aYY8F75b1aSDbbl37tA_M90uJzV1hvPtO9NNar3YtOyck2dkfOaD5ar3R_K2HzFXz1iR0euwVzQY_bTdR_77dmw6Pz6bwIclmkXJUgUQoHQP45brVTR2t7UDyxqOtQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پپ گواردیولا اعلام کرد ؛ فصل آینده هم در منچسترسیتی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 441 · <a href="https://t.me/SorkhTimes/131770" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLpkLnODSgP2zxEs-DDm3ZumbIQLvXEe4GxygXpAks5QnexMK1macPOTYk88WpZFYs27Jfre6jXZcDvJH7VGS5SsoBmbBkJocwjAW8vhauKqUS2qoDQWbkLu7AQrHMKjmmkdYeL_zgVT8CKkvT_-QOx3azJf6ySgBp0w45AydHrhqTMvke4GzEZOYwKFyJ2L7ZMG9M0e4epFekYktPQCnobJxH5FiK_cNdDcT-DwDZSVe9PTPG0c-UJM43L9BUc64R1Ka--_ngZk9mCvqOI2rhTJeBsckWE61rx2hVz61Ev9SpQ1fULzqT0RrpKwq6ymoAdEsY1mspfluUg8ZqgTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولیانوف: کارشناسان غربی معتقدند که آمریکا و اسرائیل می‌توانند حملات نظامی علیه
#ایران
را در روزهای آینده، اگر نگوییم ساعات آینده، از سر بگیرند.
💢
اگر این درست باشد، به این معنی است که آمریکا و اسرائیل از اشتباهات استراتژیک گذشته خود درس عبرت نمی‌گیرند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 488 · <a href="https://t.me/SorkhTimes/131769" target="_blank">📅 11:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 491 · <a href="https://t.me/SorkhTimes/131768" target="_blank">📅 11:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXqkDdjb1BPzi83VszFx_abaeUHZR87GdO3UWLq5Qm8x76_WMJ1Zkh9ww-wujxWRSOX7MWtfROs6ipVFN3eAHUa6q_a1FuQLkAd92JoU6TCzp3LbVmFd0Qv9_MLY5WtBDEiJ59Yju8Pou448ryCdSrplwFx3HU66-UOrEtr37k6wdJTMXM22laMJY5SEe8I5hx2x7v7XY8qo-0hqpXiXUe6pOaY8fufQ1Hwvb2MXBdc_mywxWA8KSXjnFQIhDYwXRXhHbkHJu2KN3oKdGU895U7OpaKDZEGpB8PJPk6L99AbM6HUJBuIP3KoBvPML4kRduxG8F9eq1FFH_-jvm-kHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
علیرضا بیرانوند:
▪️
سرود جمهوری‌اسلامی رو داخل جام‌جهانی با تمام وجودم میخونم و مخالفای داخل ورزشگاه هم هیچکاری نمیتونن بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/SorkhTimes/131766" target="_blank">📅 09:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👁️
غول مرحله آخر…
👁️
🛜
سرور نامحدود 2 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 6.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/SorkhTimes/131765" target="_blank">📅 09:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🟢
محمد شهباز شریف، نخست‌وزیر پاکستان، به روزنامه تایمز بریتانیا گفت: نسبت به برگزاری دور دوم مذاکرات مستقیم بین واشنگتن و تهران که منجر به صلح پایدار شود، خوش‌بین هستم.
🔺
پاکستان مورد اعتماد همه طرف‌ها از جمله ایران، دولت آمریکا و همچنین کشورهای خلیج فارس است.
🔺
تلاش‌های میانجی‌گرانه ما علیرغم تبادل تهدیدها بین دو طرف، ادامه دارد.
🔺
صلح به آسانی به دست نمی‌آید، بلکه نیازمند صبر، خرد و توانایی حرکت دادن امور در سخت‌ترین چالش‌هاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/SorkhTimes/131764" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNlZxAJCKc_yXoI3zMZ-eRsiEdQPFOnwI0804DYu6buoF1JAuoJGAXyRUrzzP9-gREIxYHw2c1NR-U1tR6lTJAR-rbSfU5gY_c65EWNZXfHgzV-505WVRaI1s2ZMR28Ku2bCggSG3zQrPClOhIFyok-WsWTnqP-H7OOxaZjiD-wvct_rN8DSTg2OWJHThv787aej5_kHi0PQ2kof3_tRAAu1N2L91VxBEwHG8m8hpkC7I2xFiwaheEpdHB6vmPBDeDd6_cgVhEkxU6ZxW9OqVZjZ1nXuh24FtH4GiAPb1nG9kFiiATxUVQ-XfC6SQGD9yk9PsmH3RwoCbBQpni39ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/131763" target="_blank">📅 01:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/SorkhTimes/131762" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/SorkhTimes/131761" target="_blank">📅 00:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131760" target="_blank">📅 00:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131756" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
ده دقیقه تا قهرمانی تیم ژاپنی و از دست دادن جام با النصر و رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/SorkhTimes/131753" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/SorkhTimes/131749" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/131748" target="_blank">📅 22:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/SorkhTimes/131747" target="_blank">📅 22:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT9mkVRIuKDHKoCcvmi9wSst5cDHtuM9WlIhpSfQbG3kqX3czL43gNV6aeeAz0WPCcu2xNfh4TwcBpxONxh5N3PQefmAJx6j7qlRQLx2ZjO33IPYQJ_JAd66BIAiKtFUD7NCW0KyezCADYV6_v8In3ESokTLe96dVTofWI4pIeQJdR0X0uqagtJ2Y__T7w3z-DOMaybV4_A7EEeTA5ad33-QaYiRds_Xw1B6b9N8HBYXHWkKo5LATQghMEkTPF7iCZdISZ5b-XtfBFc6116HWpMP_11BSupFzhit71nX-1YhHt5abcMt2_9Bpnka0dJBPpY_SFXqb8IbHs8MSVafJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#رسمی
تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/SorkhTimes/131746" target="_blank">📅 22:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
رضا شاهرودی: میخوام بازیگر بشم
😑
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/SorkhTimes/131745" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/SorkhTimes/131744" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/SorkhTimes/131743" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
فرهیختگان: امیرحسین محمودی با درخشش در اردوی تیم ملی در آستانه حضور در لیست نهایی تیم ملی در جام جهانی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/SorkhTimes/131742" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰
گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/SorkhTimes/131741" target="_blank">📅 22:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر از سایرین گرفته تا بتواند به برخی از مشکلات خود در کشورش رسیدگی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/131740" target="_blank">📅 22:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
قدیم‌ها آب کله پاچه رایگان بود تا اگر کسی هوس کله پاچه کرد و پول نداشت بتونه بخوره.یا سوپ توی رستوران ها رایگان بود تا فقیری اگر پول نداشت حداقل گشنه نمونه.قدیمها نسیه یه امر روتین بود و جایی تابلو نسیه ممنوع نمیدیدی.
برکت وقتی از زندگی هامون رفت که دیگه به همدیگه رحم نکردیم.
‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/SorkhTimes/131739" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
ترامپ: اگه حکومت ایران به توافق نرسه، دوران بسیار بدی در انتظارشان خواهد بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/SorkhTimes/131735" target="_blank">📅 21:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZ_Y7GIXW8Q-TLlI7DRd-sQ5-yGg21eNQwLRX96Kfk7Kn1Wp7aT8bvSGFsR5POBD_bcNLlbnRblGyNjUsAhfEAq2TisY8TZdnJqb7sQ5Jzllg61FsYneWClBzsVzo7s_walClK-M3aHnl0LWFxCwPUgFI89Kf0qwPT7dz_xcT5U_Pb82xiOUuc-asSjFojPhdFcTld-T9iBxIBv4n60y1m14zbZbG-Q7OeNpgf6SQEqN-mjV6VWf-v3xWR-_GJ1I_KnEetReOPKdSwGi5FvXiNYS3jhG69LBxVhUu94iq6akOaFrfoOSfzw4ohxtPkF8HxKVsDb-LAW3QUB2akbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Nassr -
🔵
Gambaosaka
🔵
فینال لیگ‌قهرمانان آسیا
⏰
شنبه ساعت ۲۱:۱۵
🏟
استادیوم
الاول پارک
⚽️
النصر حالا با رهبری رونالدو؛ در دو بازی باقی مانده از فصل مقابل اوزاکا و داماک، فرصت دبل در قهرمانی را دارد تا سی‌آرسون، اولین قهرمانی‌های‌ خودش در تیم عربی را تجربه کند.  تیم خسوس، آمار کاملاً بهتری دارد. النصر در ۱۰ بازی، ۳۳ گل به‌ثمر رسانده و سرجمع ۳ گل خورده. این آمار برای اوزاکا در ۱۲ بازی (با احتساب پلی‌آف)، ۲۵ گل زده و هفت گل هم خورده. تیم ژاپنی با فرم ضعیف‌تری به‌میدان می‌آید. اوزاکا در پنج بازی اخیرش، متحمل سه شکست شده و این آمار برای النصر، در پنج بازی اخیرش، یک شکست و یک تساوی بوده.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/SorkhTimes/131732" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فرهیختگان: سپاهان مشکل مالی داره و به بازیکناش گفته سقف قرارداد ۳۰ میلیارده و پرسپولیس میخواد از این فرصت استفاده کنه و حزباوی، لیموچی و یوسفی رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/SorkhTimes/131731" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
وزیر کشور پاکستان یهویی و فوری وارد تهران شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/SorkhTimes/131729" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
باشگاه سپاهان به مشکل مالی خورده و احتمال داره از آسیا کناره‌گیری کنه که در این صورت پرسپولیس شانس اول برای معرفی به لیگ قهرمانان آسیا هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131728" target="_blank">📅 17:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRo20f1q36JYqGHfNtBllCLrTLBhPpegdhvlq4CB8q2dSa6JN4Fjzrshui70NtvElWViMp8tbspSiKeSkDOc_R42z_AWtufwN9duzA7F06U7hO5VFCvNEQnTeKqj4SBNwVEscJgRd22NMbtTluK7KO8lBFEwkjxF_MV8I9RgPFND-5rkekhJmqQUWEYra2OJsKii9RlCoNUA9-5ipH7ntq4B7r8hHc8nzfbK53Y5GJV0_rdZRe-dafqr0IT7Pa_SaNSYbQf-PM6_nXRqkBpTMWixneSFMbq_xmTczl01_yBQbT8OakMynQRITwykByzwLlvLKoZMa_BxUsI8W54CUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب میتونه یه شب رویایی برای النصر و کریس باشه. اگه الهلال نتونه امشب بازیشو ببره، النصر قهرمان لیگ میشه درحالی ک خودش داره تو فینال اسیا بازی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131727" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131726" target="_blank">📅 15:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sURyqTCaW3Nv1rS9B5NUoYssG8TB03nq_XWtbS9tvJ5Z0wHKDoO8qxXl39PXXm9wmYs_e_pBWJdTw5Ff__NWHUA_pHpML59gIRFkWStTIQBcxTauzZcjKyTtqOKZhM9m9JRzMV8HH48ar7QVo8rSmFK0sA_BkcIdJ57AiRyTRM4l2ohqcSIOccu7_DFpT5rn5Bc485TpjZio9oxgzSrqfSLEH4L_WqZlJje9TRfhJVG5m7NMMmcQ0daNOeHjXGIUU7NndhqGaP9r33aysHGADi3cZ1bNpCIA_zKCzmYgh4cYKDGrU5B1XhY3hH5dEFrDpfdQuS1gQbNbHKS64_mwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مراقب پیامک‌های کلاهبرداری «اینترنت پرو» باشید.
🚫
🔴
اخیراً پیامک‌هایی با ادعای «آزادسازی ثبت‌نام اینترنت پرو و هدیه بین‌المللی» ارسال می‌شود که با کلیک روی لینک، گوشی را آلوده به بدافزار می‌کند.
📱
💣
✅
راهکار: لینک را باز نکنید، چیزی دانلود نکنید و این هشدار را به اطرافیان منتقل کنید تا کسی قربانی نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131725" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/SorkhTimes/131724" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFVRJWq6PZyQyUoUMnuK8rpeJ3HB-f9nAPAPkgmfkZpf_150hNmsb1I-YoytyAp7UtLsia97e5acMyIgwp0jdroxjxvU25V6Izj86m2sgj-rlXQizuHX0EbxpLuwng8rDCjXNpoZEMTgImgLa4yiReQlknQ-Lgo9GW16kQZbeUNvzwmcmNT8T2awX9tX8kCyh_XJiylFU0ron8XhuxYTkA6psG3Thyoonyn4rQ67oah2ITwOPnmr_a_Jn8zF0880E3pdST0753mklUpFT5FxGA78PkmUKVGZIjzHXfFnIp307NyLGvAbVGFA6LXckLQQtNgMZgwkI8VcAvwWaK7u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/SorkhTimes/131723" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
پرسپولیس حداقل ۸ بازیکن تو  جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131720" target="_blank">📅 11:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/131719" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد  پ.ن پس اگه مجدد جنگی باشه میفته بعد از جام جهانی ..  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/131718" target="_blank">📅 11:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIwdtwIpL3lQrWqSUG8v8hs63ua2g_9YDrdGlWIQoaMQqHlA8Q8O4wPGAqRLgho_tUgC_B4s99VVYFAgROXX3IskVCtE8BhYMdowxzGD1mk77HVIctiIBXNBGoMEsaebpaJYIYlaqEaDGdQLAfEHyMOlFLAAcQEFAOSmqbYioV99tbMoMlsbUKKmb1XfRdlosBufVxpgUuFOiyCF1-M6pKe19GhgS_Trf9idXvvqfpht3JIQc6U_ZDFWVd2CozCgBCYQT1mUq_MEQXFeVBqtAl_27QFXBjYrX054ElucMM1VgJ2Y4yIZZQMpDHVTiT8mD4pHZxREO6y2yU7WUPEbRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس
؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SorkhTimes/131717" target="_blank">📅 11:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH39-nToO1q-GOqn3q9iNh21QPT3NYLVyvioAK_EbPIeFJexZ3-qaSnSWYbHp4GOiSfF5uNqS8yRTkk_vTAvjC57ncF8brzzbcdhu0bz43wVxQaDLr0v9kL6niiLs4QkMo9lwlyyJ8AyabRC2jJcXlqxurKd0JoFI7B8i8tXqfLtOqmkOHMXJkdTYEfCML1Q3laiRVihff3ICEdDG0S7W7WRIBeOZob7kKINiaDL3UdPID9uNN54x6Kkm3cFc78znI466N4ce-RlT2HBbBZ2iFAXVRJPzFSV0psIyhjJgttQ_s3_F6iZDwqNZG21dfK67_Gv1IbtsTJeh1uBa2dhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز امیدواری کرده که باشگاه بتواند غرامتی را از اوریه دریافت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/SorkhTimes/131716" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbxW255EaBHw7Iedy4ISEDU2mRwzMkqAxf_hNC7EOsEoXvIJ3uOpg4UNYzjunB-eHQVtkgJR-Gfzbn8PCn8GptcoO--FTf-Kp5W-S2PcyqjH29NaWqNyMQEZgE03GNYM4f83f21pjEiT-WtUjR0p8lDDArUtc8SAwIBmziCIw_2gkjoQiRWrg6hgqIJLOZIlkOOmePN6Ar7PYC_JIuaZvCNjCaf-oXh_2svw-8Nw7Vnj6jtLtWDftF682KJZY28ojliWVewyGujgnuVQSVi37bOgsCcSg0_XSk36AO0MlXQK764wok2vfLXCExsmfu2RBI9g58xIMKmiEmDbH7Lejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه بازی‌های مهم فردا فوتبال
⚽️
فردا دیدارهای جذاب و هیجان‌انگیزی در فوتبال اروپا برگزار می‌شود که در مهمترین بازی‌ها، سیتیزن‌ها در فینال جام‌حذفی باید با آبی‌های لندن تقابل کنند. بایرن در زمین خود از کلن میزبانی ‌می‌کند و دورتموند هم میهمان وردربرمن می‌باشد. همچنین در دیداری حساس و در فینال لیگ‌قهرمانان آسیا سطح دو، رونالدو و یارانش باید به مصاف نماینده ژاپن گامبااوزاکا بروند.
⚽️
بازی‌های فردا رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید.
📌
وینکوبت
انتخابی حرفه‌ای‌ برای شما، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131715" target="_blank">📅 01:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=JODUuW7vr8cNB_kwws5uyQ5sR-aOGkQpPYLWtsDbKGprzixjIAGyaW-eR5kdgDvFcsvRsEd8iQtVZpaIU7Hdm3Zrvp2G19jsFRim4zkYZUIw207RLLOtEEBi3KqSFFsTBWOCg6tnZhMabAnKlQzRs45V6xicZuxXdmej-mxZM1DwCjF35FGQyCdeirFBSJE5eE3FNEM7lecP5YCNDpOfs-8WnQcstZvgNNPLBLpeAfGiRRmZRfIdFH0UnR60bXlDxOVP-uBvbidL4vzzzVR09Hj4Bwc_RY0Mmb1kKCZlSaYRp2LuWN2CxFTNluIl7CPB1rvThNGIZ5qojSL3Cr3fAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=JODUuW7vr8cNB_kwws5uyQ5sR-aOGkQpPYLWtsDbKGprzixjIAGyaW-eR5kdgDvFcsvRsEd8iQtVZpaIU7Hdm3Zrvp2G19jsFRim4zkYZUIw207RLLOtEEBi3KqSFFsTBWOCg6tnZhMabAnKlQzRs45V6xicZuxXdmej-mxZM1DwCjF35FGQyCdeirFBSJE5eE3FNEM7lecP5YCNDpOfs-8WnQcstZvgNNPLBLpeAfGiRRmZRfIdFH0UnR60bXlDxOVP-uBvbidL4vzzzVR09Hj4Bwc_RY0Mmb1kKCZlSaYRp2LuWN2CxFTNluIl7CPB1rvThNGIZ5qojSL3Cr3fAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: از اوریه غرامت می‌گیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/SorkhTimes/131714" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juj-qOUcrANg_RJHwMQ9vnGRHuEPoytfW8YmyZpaJtDpDdr3aLaj8UUGKrjU7OnUogAZD7qeGyA0zZH-sp6hKGEb8TUSPdwsd2oLSiKYDBjDmp89zJbHzdG9716XTfmIJMzmUvDvB_HfjHe59uMkSI7XoxabeMmizbUJPkpx13me-zs1NrFDe5UHcc_OkgF9bdfr39zmTT-MqZyy_gMireoEZH7d7gQvRjJE7vBP-FcgrKuQ4Z3sJt1Z_CvEfhKb-mAkTra4SX60pKaU1PLku-5JENKAL6NMRoizH-Kr9cfMu2MgJTTY1ZRmWgt2MC99zGbCdYZNEBarx8TuUDKYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
محمدمهدی محبی، وینگر تیم اتحاد کلباء امارات تا پایان فصل به تیم فوتبال سپاهان پیوست.  پ.ن اینم پرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/SorkhTimes/131713" target="_blank">📅 00:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=po8NlyJEQ9NKy-bwVYyQR1YxUeLf8xWbb1bxbSOWqO1ALlSV6H-O5s4yb3L0_j_nIBh5VxbFv_MwYIMVeF_QwHWegOLRlpjFrjv53d1M8Z-ji_5LwB6iRnBsV5Q75deIrcEkog-YtZbeYntUu8CQm8XjdjXlRO3ms94SWlz68XPvesPuthvrBbB5ZW5T5WjvXGcFRRK_kOrWM-Ouu8UaNREu3r9pIA4Utf3JhC3rcLe6lUirmxtRx8r5nfZATalrkFX827ZtADY_SavIOMcy72ynFaE7w073GI29qGpSbDABAHFAM6M8WVdjNl1GBmYWiheeoipf4ISArpC5UV1U8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=po8NlyJEQ9NKy-bwVYyQR1YxUeLf8xWbb1bxbSOWqO1ALlSV6H-O5s4yb3L0_j_nIBh5VxbFv_MwYIMVeF_QwHWegOLRlpjFrjv53d1M8Z-ji_5LwB6iRnBsV5Q75deIrcEkog-YtZbeYntUu8CQm8XjdjXlRO3ms94SWlz68XPvesPuthvrBbB5ZW5T5WjvXGcFRRK_kOrWM-Ouu8UaNREu3r9pIA4Utf3JhC3rcLe6lUirmxtRx8r5nfZATalrkFX827ZtADY_SavIOMcy72ynFaE7w073GI29qGpSbDABAHFAM6M8WVdjNl1GBmYWiheeoipf4ISArpC5UV1U8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی: سروش رفیعی به تمرینات پرسپولیس برمی‌گردد. صحبت‌های پیمان حدادی در مورد آخرین وضعیت سروش رفیعی در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/SorkhTimes/131712" target="_blank">📅 23:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/SorkhTimes/131711" target="_blank">📅 23:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=OYDzePbbzHMZIldb2B4BJqicxG_B4NNIa3LvNy2P2RCQfjrmsOwyNH9qlHC3Cot4rAgveeXoUFatoJ342mR90wEnYB87RO2NIsMidH9z1tkYOWxqvhtdClHP1jmB1FkwlEL8P-Oue2y2esJDatgjXqDBR0PT0_Ixr2Y0mPYwr8CUJMopW4PaXT-VLUJhT8m3kzg5HxuYbaa6ulOjd89S5CvBLGe3pEEzDPaLJcQ9JBFwcVk6BR4MVNoFC_3MrfAkduNmreaLghjApi3k2YBRKauHnHBMHW4ccY4fyrqRbPVqL2ACZzL5omgjhwy9mloenQ-Gsm1H8P9lD7iaHRfmgQpBKoKsekPm7bqP4OmlmiV_8j1Co3YZ2GPXssDLqOlqivT29mOn1SSiuTuflUMWDq002ls5huF2Vzzz_MS7EnQxfK4KkVjEPdi6eXWrrv2baRoToBQYujfvOsagdcjW3hm08agk3610kEdvJm-eDPxlBl6l9nTHH-hRsUFXVLPC5Fzq9io9rLBQzD9qXcHWaQV5E3DLmB7HjBSEYsSUkskPLLP55USt47bagQg_yJ83LgQWcEY84eNOFmtnSmM3WfeBXqld7FBPFA5EyMcyI2v4yw826tBv7Ayep1sQD1IxIcG1hGv02wWDT1OmBnFsB2eOPsm3Pks4O_ddxiHBFTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=OYDzePbbzHMZIldb2B4BJqicxG_B4NNIa3LvNy2P2RCQfjrmsOwyNH9qlHC3Cot4rAgveeXoUFatoJ342mR90wEnYB87RO2NIsMidH9z1tkYOWxqvhtdClHP1jmB1FkwlEL8P-Oue2y2esJDatgjXqDBR0PT0_Ixr2Y0mPYwr8CUJMopW4PaXT-VLUJhT8m3kzg5HxuYbaa6ulOjd89S5CvBLGe3pEEzDPaLJcQ9JBFwcVk6BR4MVNoFC_3MrfAkduNmreaLghjApi3k2YBRKauHnHBMHW4ccY4fyrqRbPVqL2ACZzL5omgjhwy9mloenQ-Gsm1H8P9lD7iaHRfmgQpBKoKsekPm7bqP4OmlmiV_8j1Co3YZ2GPXssDLqOlqivT29mOn1SSiuTuflUMWDq002ls5huF2Vzzz_MS7EnQxfK4KkVjEPdi6eXWrrv2baRoToBQYujfvOsagdcjW3hm08agk3610kEdvJm-eDPxlBl6l9nTHH-hRsUFXVLPC5Fzq9io9rLBQzD9qXcHWaQV5E3DLmB7HjBSEYsSUkskPLLP55USt47bagQg_yJ83LgQWcEY84eNOFmtnSmM3WfeBXqld7FBPFA5EyMcyI2v4yw826tBv7Ayep1sQD1IxIcG1hGv02wWDT1OmBnFsB2eOPsm3Pks4O_ddxiHBFTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131710" target="_blank">📅 23:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/131709" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود
؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SorkhTimes/131706" target="_blank">📅 22:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
حدادی: محسن خلیلی تا پایان فصل سرپرست تیم بزرگسالان پرسپولیس و جانشین افشین پیروانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/131705" target="_blank">📅 22:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/SorkhTimes/131704" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=ZZWMbPjpnJunNsf2ZjW8uqbe1BTVRUvBmxHrOUcnMGjv0ozMjFSPx5_TMoQjfyFIXK7CW8_dRBVwsmBsFP67Sm_ZNC8BELEq9pAPfPIQ8yFjQq6omgAkVT7eMU8ou5D34rKipPP8DYZEbVlxN7So8VUX-Y0G6kY6qZ0C_bNDPD7VGzck4a_op4UZZLd_yTceQs41xJOqzUuadrBHDBN3-bFrod_5i_WJA6v8V4CnmwH3MtJ57_nanqxBrgdNHzMfUXOsEdbZvYsYYI7Lb_0BbWXx-aKwQeCnFd3Ji-e0QXl86BifboUQKy45yMaaemRg6Rfk4lpDFmxybkmL5YGihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=ZZWMbPjpnJunNsf2ZjW8uqbe1BTVRUvBmxHrOUcnMGjv0ozMjFSPx5_TMoQjfyFIXK7CW8_dRBVwsmBsFP67Sm_ZNC8BELEq9pAPfPIQ8yFjQq6omgAkVT7eMU8ou5D34rKipPP8DYZEbVlxN7So8VUX-Y0G6kY6qZ0C_bNDPD7VGzck4a_op4UZZLd_yTceQs41xJOqzUuadrBHDBN3-bFrod_5i_WJA6v8V4CnmwH3MtJ57_nanqxBrgdNHzMfUXOsEdbZvYsYYI7Lb_0BbWXx-aKwQeCnFd3Ji-e0QXl86BifboUQKy45yMaaemRg6Rfk4lpDFmxybkmL5YGihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131703" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
پیمان حدادی : پرسپولیس پرهوادار ترین تیم ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/131702" target="_blank">📅 22:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/131701" target="_blank">📅 21:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
ترامپ:  ممکن است مجبور شویم یک کار تکمیلی کوچک در ایران انجام دهیم، چون یک آتش بس یک ماهه داشتیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/131700" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DajisRROZH1WN8uzFZH7MCOREWcanQqrxX_u40id5MwegdTrhcXxTs5k93ok8KgcUsNx1TcvPpEyuh_1sIm2KXYNN_UWoZmP6C88utW9oFpvRosa8xm1pVD9mfIFVGgbHM87qRcVCGtyfIz9s6QdFjczVXn7-EyCSN0609o6pJN3TsmKXrq9g42xls7_1F6qgxIYUv0-2Ao_7CdDGHfPS8aBbhaTYtKvo2gTVbKggjMvQh_qNhxrLbu0bLBDLvVqbLCEAzW9dV276aWODm-A2gbhbqfNhgytfZNR_RhZL4Q0-juISiVxEOLfrz2X_pgODvdhhFTd8gmS0J7lJvJ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جدید و عجیب دونالد ترامپ
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/SorkhTimes/131699" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/SorkhTimes/131697" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
آشوبی: استانداردها را به فوتبال روز دنیا نزدیک می‌کنیم/ مسلمان نیاز به فضایی تازه داشت
🔺
تفکرات و ایده‌های بسیار مثبت و قوی در باشگاه، به ویژه در بخش آکادمی وجود دارد که به نوعی برای اتخاذ این تصمیم مشوق بنده بود که در ادامه مسیر بتوانم در این حوزه کمک‌کننده باشم.
🔺
مربیان آکادمی سال‌ها در این رده کار کرده‌اند و شناخت خوبی دارند.
🔺
برای از دست ندادن استعدادها، تیم ب تشکیل می‌دهیم.
🔺
انتظارات هواداران از چهره‌های شناخته‌شده به حق است.
🔺
محسن مسلمان نیاز به بستر تازه‌ای داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/SorkhTimes/131694" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SorkhTimes/131693" target="_blank">📅 19:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 841 · <a href="https://t.me/SorkhTimes/131692" target="_blank">📅 18:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/SorkhTimes/131690" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/SorkhTimes/131689" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
مشاور وزیر ارتباطات: اینترنت بین‌الملل حتماً به حالت عادی برمی‌گردد، خیال مردم راحت باشد.
🔺
روزانه پیگیر بازگشایی هستیم و بخشی از خدمات بین‌الملل هم‌اکنون برگشته است. امیدواریم در ماه‌های آینده با تصمیم نهادهای امنیتی، دسترسی کامل برقرار شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/SorkhTimes/131686" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
پرسپولیس به دنبال تغییر سرپرست نیست؛خلیلی روی نیمکت می‌نشیند
❌
پس از کنارگذاشتن پیروانی به دلیل سفر به آمریکا در میانۀ جنگ، در روزهای اخیر نام چند پیشکسوت برای پست سرپرستی پرسپولیس مطرح شد اما پیگیری‌ها نشان می‌دهد که باشگاه برنامه‌ای برای تغییر موضع خود ندارد و درصورتی‌که مسابقات ادامه پیدا کند محسن خلیلی روی نیمکت می‌نشیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/SorkhTimes/131685" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
هلدینگ خلیج فارس به مدیران استقلال گفته پول نداریم و فصل بعد خبری از خرید خارجی و بمب و اینا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/SorkhTimes/131684" target="_blank">📅 17:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
پرسپولیس
حداقل ۸ بازیکن تو
جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/SorkhTimes/131679" target="_blank">📅 16:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thFvDNYSJBhi4e_QHnGBuBwFCk-HmcyUtMVebeIILNQDSMs_HYxmkqCZ549S1bw2IsSMg6wWeX6HaKaZQ7EZF9AOaDwa8qCnkHe6Yuku8ut9J3bKrWeBLzQchZNxXJaOPI65C_nQenLUvlnxm2V1d5j_KwT7nYcoXCiG8ip_TABZtZEvCKQK1HJ7NEQI-F41bHnkHnncTi2GymuiHNmb3rJKUtUrnkDXhR9_itA1MK39TxvnxWn1MhEvTMyXzn08ddEC0kXQ-NyyMg1R21IsO-1YPMhSms9EeRBahgE5unU_5mNLVRbdHwYjfetUifwgNcVTmkBLHMHrLF50q12htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 787 · <a href="https://t.me/SorkhTimes/131678" target="_blank">📅 16:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2kHcc3vuNoK8ELuywHURWErRIlePXL09nINoGdOgF-VxoozEzCjsmZVurWOhsWLxU_jSk9GgItqt4te9Hz85vp_JOKEkWuMzneXy_CC2OH2vusrb1W3L6HEbi4Yi3GWAGH2bxT9XLn0TcVg5ChPME0OzXrwLWmIxDHxIvcSLW4AzV7O_BGQNz9_XYXGL1PuIqXoeye0nWxZ1dSFgjkJgsFG_qhH4O_JK9tnU3GzGA0GNE6Qv1hvXoh39cxNNY2eWGEZhxM2_JbUsn92fCK7yhdzHEDXRyecQLovnmcCJrc9euX4Sp3zo1GUiUp92gSAWkA5A4kr7ddIbzUPkbL4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاربران محترم برای دسترسی به سایت وینکوبت فقط کافیه از طریق ربات وینکوبت وارد بشید.
🤖
-
@Wincobet_bot
🤖
-
@Wincobet_bot
📌
بدون نیاز به جستجو، بدون لینک‌های پراکنده، همه چیز از طریق خود ربات انجام میشه.
📌
ویژگی‌های ربات وینکوبت:
👇
▪
︎ورود سریع و مستقیم به سایت
▪
︎دسترسی راحت از داخل تلگرام
▪
︎بدون مراحل پیچیده یا ورود جداگانه
📌
اگر دنبال یک راه ساده و سریع برای ورود به
وینکوبت
هستید، این ربات ساده‌ترین مسیر دسترسی شماست:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/SorkhTimes/131677" target="_blank">📅 16:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=mNEe8U_dDI5I214YzQ33dUPTNV2OPOi5ZaYUaTc0xPzyoZEYSY8dG93Gca6syJflJtNV2uPxEAuSu-r74c31Bzu2XudaE_bvZSEMxONq-x0w75ByI6uIIY3gOPTVXa5COBMSkSR5euEdvNALij8ZIMnVWf7hiaA0pF3kgcvUWsSzwP662T-YeA_ZpHMLJ2xvWM1i47KMnA1e3XqSjASdTKYEtH1cHPXdYUBkn9e8-d3Pc4DhU8cDOWps-KjWQ593FUFL948IeGy0dOsszBO8N-NLgKc3CEwS4ujvUwKMXAf9EXHetqcWtWhAThK7ZYg6qhBSBuVfPJWc6l9myOHuKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=mNEe8U_dDI5I214YzQ33dUPTNV2OPOi5ZaYUaTc0xPzyoZEYSY8dG93Gca6syJflJtNV2uPxEAuSu-r74c31Bzu2XudaE_bvZSEMxONq-x0w75ByI6uIIY3gOPTVXa5COBMSkSR5euEdvNALij8ZIMnVWf7hiaA0pF3kgcvUWsSzwP662T-YeA_ZpHMLJ2xvWM1i47KMnA1e3XqSjASdTKYEtH1cHPXdYUBkn9e8-d3Pc4DhU8cDOWps-KjWQ593FUFL948IeGy0dOsszBO8N-NLgKc3CEwS4ujvUwKMXAf9EXHetqcWtWhAThK7ZYg6qhBSBuVfPJWc6l9myOHuKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
افشاگری بهزاد داداش زاده مسئول برگزاری مسابقات هیات فوتبال استان تهران از زد و بند خلیلی در آکادمی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SorkhTimes/131676" target="_blank">📅 14:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131675" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس‌جمهور آمریکا: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/SorkhTimes/131674" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ: اخرین چیزی که بهش نیاز داریم الان جنگه، ایران میتونه اورانیوم خودش رو به امریکا یا حتی چین تحویل بده و دیگه جنگی در کار نباشه!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/131673" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس جمهور آمریکا: من دیگر خیلی بیشتر از این صبر نخواهم کرد؛ آنها باید توافق را امضا کنند!!
❌
رئیس جمهور چین به من اطمینان داد که با داشتن سلاح هسته‌ای توسط ایران مخالف است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/SorkhTimes/131672" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/SorkhTimes/131669" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔴
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131668" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
رسانه های مملکت : ترابی و اسماعیلی‌فر دوس دارن دوباره برگردن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131666" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131665" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
دیشب تو لیگ سوئیس تیم اف سی تاون که موفق شده چند هفته قبل از پایان لیگ این کشور قهرمان بشه به تیم یانگ بویز 8 بر 3 باخته و دو تا اخراجی هم داشته!
❌
همین بازی باعث شده تا فیفا به دلیل شرط‌بندی ورود کنه و ممکنه لیگ این کشور کلا تعلیق بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/SorkhTimes/131664" target="_blank">📅 12:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
پرونده های باز باشگاه استقلال در فیفا
⏺
منتظر محمد: ۲۸۸ میلیارد تومان
⏺
پیتسو موسیمانه: ۶۵۶ هزار دلار
⏺
کوین یامگا: ۸۱۵ هزار یورو
⏺
ایجنت یامگا: ۲۸۰ هزار یورو
⏺
آلمدین زیلیکیچ: ۸۱۵ هزار یورو
⏺
وردان کیوسفسکی: ۴۸۵ هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131663" target="_blank">📅 12:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
فوری/ آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
❌
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
❌
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به…</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/131662" target="_blank">📅 12:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131661" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
احتمال انصراف سپاهان از آسیا / پرسپولیس جدی‌ترین مدعی جایگزینی
🔴
مدیران باشگاه سپاهان به‌دلیل فشارهای مالی و هزینه‌های سنگین حضور در رقابت‌های آسیایی، در حال بررسی احتمال انصراف از لیگ قهرمانان آسیا هستند؛ اتفاقی که در صورت نهایی شدن، یکی از بزرگ‌ترین شوک‌های…</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131659" target="_blank">📅 10:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
خبرهای اولیه از توافقات میان چین و آمریکا میاد شامل مواردی :
🔺
خرید بیشتر سویا از آمریکا
🔺
خرید نفت بیشتر از آمریکا
🔺
خرید بیشتر گاز مایع ( LNG )
🔺
خرید 200 جت بوئینگ
🔺
ترغیب ایران به اعطای هرچیزی که ترامپ نیاز دارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/SorkhTimes/131658" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SorkhTimes/131657" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
مهدی طارمی دو سال پیش تصمیم گرفت از پورتو جدا بشه و به اینتر قهرمان ایتالیا پیوست و همراه این نتونست هیچ جامی بدست بیاره و در نهایت آخر فصل از این تیم جدا شد و به المپیاکوس قهرمان یونان پیوست و همراه این تیم هم نتونست امسال قهرمان بشه و فصل رو بدون جام تموم…</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/SorkhTimes/131656" target="_blank">📅 10:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4ao1zVTj8mxbA-3zmUqqjFC1Z2ffvZW4uqEKSMZjapaYsAJKlhe8XhqCXGJlz9N5gtm23tM1T0A33OJP3DxxcBRvzrulQleU_Mv_fBr_xZ3NX8GewFl3wBBqat4bIVAqSAb3qVbEbmFMzP6a2dz0cfsVNaXCpcZ14zjmQ4t01jFQ4VQ6AW-oJZ_qvEJ_h_lTadslbhgpeUq5La0rpCXDdBawXIBQFGAcz9n5hUlu-d_YINq53UZ1u-aQ0E4XtbGqT0JVdA07Ci_OQedzoBOsgeSsk36d0_XT054noTUiq0YyjDqzcP8QEBw-ZCRz3UCkeGTWhJmwauXDnP7YazE7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131655" target="_blank">📅 01:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
#خبرگزاری‌مهر : برسی آمار ها نشان میدهد استقلال، پرسپولیس و تراکتور شانس بیشتری برای حضور در آسیا خواهند داشت
🔴
این در حالی است که سپاهان در دیدارهای مستقیم مقابل رقبای سنتی خود نتایج ضعیفی کسب کرده و شانس کمتری برای کسب سهمیه خواهد داشت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131654" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
با اعلام مهدی تاج، باشگاه استقلال مجوز حرفه ای گرفت تا حضور این تیم در فصل آینده رقابت های آسیایی به نوعی قطعی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131652" target="_blank">📅 23:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚡️
⚡️
قلعه نویی ستاره پرسپولیس را خط می‌زند!؟
❌
در تیم ملی به هدایت امیر قلعه‌نویی، رقابت در خط حمله خیلی شدید شده. حضور سردار آزمون و مهدی طارمی تقریباً قطعی است و بازیکنانی مثل شهریار مغانلو و امیرحسین حسین‌زاده هم شانس بالایی دارند.  به همین دلیل احتمال دارد…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131651" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
فووووووووووووری
🔴
به دلیل پیش رو بودن جام ملت‌های آسیا در دی ماه و برنامه آماده سازی تیم ملی برگزاری ادامه لیگ برتر پس از جام جهانی منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131650" target="_blank">📅 23:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131649" target="_blank">📅 23:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131647" target="_blank">📅 22:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔺
بخشش جریمه خداداد عزیزی توسط کمیته استیناف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131646" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131644" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131643" target="_blank">📅 20:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131642" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده
.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131641" target="_blank">📅 19:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ6Bb-5QGUF-CZGtJP-zpFi5HAMcAQaeXjc1tnWCiHPR-zmU6A1oDDQc-tsmdfk0Cy_g8KyNMiuc5uDu9HN_zKqJV3qI6OhFcDM_VZ3OYT1Zp76y2dzFwJtaXbIeK8-xlRyCovOMELWkPoxM4ywlTDi4_GpubbSQU_UQd6vLv5z5bUx47GthbMqUvWKWUOe2pXhHJfeqrPpKoIc96kHRoNiHqzP1UVKjKkw_kGoaNqbQin8WDgsgjWhdcWJ3FKJGJFkCXt1eN141LbofXb9g3i6TBb5pjNvtyokSCGaqCrfB5DQ2xaiUbGjvHUXh06K2CmmgrJNqUzMuKDDnwZiPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روزنامه اعتماد آنلاین:
🔺
اینترنت بین الملل خرداد ماه وصل میشه
🔺
هفته آینده به ریاست عارف معاون پزشکیان قراره زمینه‌های لازم برای رفع قطعی اینترنتی فراهم بشه تا حداکثر تا وسطای خردادماه اینترنت وصل بشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/131640" target="_blank">📅 19:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBeVlL36-dVof8Sh4HJtVaz0VG3uA3TXHhJX_bOiq9s4R2nIrcbslllY02ovsYtlstYWRycgJHtWc_Py5n9Ne5g9CsGRUOvdAC7tHX75svj70OoulDmfJxIXOg8LYzrEieeg7A6UmwWYCR7xvrXJKr4gJT8AeQjxIDfnd-wEFmAM_k2OGXHKb-vhybdM4rbC3QI_EdEh-sWQsWSlWHsqAXTICAuhT5--2-8U2s_DwRMaBl6dTv-lraKmDObCHBRXnZ2eqC28qjl0yKQ8b8SJchxZeWQDmvnCfnJjRb9C_Ac3x8qbuicBKTiSSOcJ0mgINDF9LwxyWHg032IUPwlJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دنیس اکرت، بازیکن دورگه ایرانی که برادرزاده آناهیتا درگاهی، بازیگر سینما است، نام خانوادگی خود را در سامانه فیفا به دنیس درگاهی تغییر داد و مشکل او برای حضور در تیم ملی ایران حل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131639" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛜
دو
عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131638" target="_blank">📅 15:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
خبرهای اولیه از توافقات میان چین و آمریکا میاد شامل مواردی :
🔺
خرید بیشتر سویا از آمریکا
🔺
خرید نفت بیشتر از آمریکا
🔺
خرید بیشتر گاز مایع ( LNG )
🔺
خرید 200 جت بوئینگ
🔺
ترغیب ایران به اعطای هرچیزی که ترامپ نیاز دارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131637" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔵
تاجرنیا خبر داد: هزینه‌های استقلال در فصل آینده به خصوص در جذب بازیکن به شدت کاهش پیدا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131635" target="_blank">📅 14:14 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
