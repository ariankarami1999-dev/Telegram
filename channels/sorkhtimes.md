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
<img src="https://cdn4.telesco.pe/file/SUxGcNw3Cusm7jNVQv1gIVaGYz2DFX355FudxtJT8om7qlQa7PEr_9U_pbuVBKHQJKgRnzZVRCAyVLSvBtZLAhMGe6YWouRsof8VaKa0crA57_GNaZ5he8JIsDOs5U6DSY50_wvNL12Bqy0hKHIP_ALjevqGxF-Oga07AS8cdTFkV2YnXxBErzwSGwFPEDbGaYr_ALMfLhu3U__ZNyMtwz7S4NHgbltZTRzoW-RHG4D3XfXp-RhprH9BySwjqIObxVc-th2t7sQqnCKMWgqTf1besP0OQXgJRAY4r5GkdXgPjOZPR5sEAkw3S-e2h0mndwx_8fc-xSEcSTXR_MCUYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
علیرضا
محمد:مذاکره تارتار با پرسپولیس را در رسانه‌ها شنیدم / به خدا نمی‌دانم به او پیشنهاد دادند یا نه
💢
من در آن مصاحبه ویدیویی هم گفتم که در رسانه‌ها این مطلب را شنیدم و منظورم این بود خیلی از رسانه‌ها گفته بودند که مهدی تارتار مدنظر پرسپولیس است. خدا شاهد است صادقانه به هواداران عزیز پرسپولیس می‌گویم من اطلاع ندارم که باشگاه پرسپولیس با مهدی تارتار مذاکره کرده یا پیشنهادی به او داده است یا ممکن است بدهد.
💢
من فقط نظرم را گفتم و هنوز هم می‌گویم اگر قرار است آقای اوسمار نیاید مهدی تارتار می‌تواند مربی خوبی برای پرسپولیس باشد. ولی اینکه با او صحبتی شده یا نشده به خدا من اطلاعی ندارم. امیدوارم پرسپولیس موفق باشد و وضعیت کادرفنی زودتر مشخص شود و نتایج خوبی بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/SorkhTimes/132801" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132800">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300 30 گیگ 350 35 گیگ 400 55 گیگ 500T 100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود  جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 429 · <a href="https://t.me/SorkhTimes/132800" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132799">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plDQM9C5pBQnnkSWyr3embziZFaqIXFGw0py_Omh4DrYnjm6F6MznRilP7g4M6VocGzZaj9Virw_lG_1U4LAR9U-8I9uLho_-y12UuT--gS9K2eMAtw6B9DNA0Dn_jnYnrOLi0qMhOP2TwFT4DmcksKH97WyLxTkYfVuay-lDqo6yuopCvETYRsb6pjyEeBm-SorO_oUqrjEOWhe9wFyelIT99zLwbHw7dLU17bJsvaBWmqqtEF-37WWTSX6SFmyc_VO8WEZKv4WWFoOXS3CgPBhy3PQEhqdDChAu_b3s2QDuBTbZL2FRgqRW3CAsGjsVzhBhHoK-n5NwKabtX9mKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس نیمه‌نهایی رولان‌گاروس بین
منشیک
و
زورف
رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 660 · <a href="https://t.me/SorkhTimes/132799" target="_blank">📅 17:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJX2jafniNiMRehF71SlVl2lK_UnT8nZqysSUtljwtxhJVluvVreuJhuXtRmpwCX737yivcIGzuv1Z6ewQ8Z-nEDAwxzFOA4UZ_U4I8nAXRMwxsZTNNjg62auEUflN9TgvAQPBRGNjzrYTUPl-NgW-nsVgAwyHPbJO4nzHmTdFjZlhFIg8k2lXR2j6RW7C-8XyaG_cUFCz8jMSJrvTHT-_gCOAP_Lty8stoAZiUQJHPIzK_FJrotza5-2CAaVUYJhY_Ioo10xwhItCxQiE0CDhLn49zmPV-OF51bVFIrlpQCrPLR3HWXiBYkG6Lfw1BtgKpKqOQRxKX2qszAnd6xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عکس تیمی بازیکنای نروژ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/132798" target="_blank">📅 16:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/132797" target="_blank">📅 16:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCOjgQtldEg4iA4u4GCzP1qpUn64XTJS-TLEGLRzPx1DYQ-sZSMLbzcSU7OHF6RVb9GCfuOXOBmbDXRzkpgYXd0I4oeG2v-7qA9GN7XiehS6NSTWrkpg0N_z0muUO0bo7W6dmmcBLszZ7qJAqL5pkD1Q1j6R9AxVtpYKE_5yYTPnSsn7IqoOl4nWox186MX61mtMOQoqFn8I-hsw4EF_LVLDYH9RLchnttWJO169XFIKSkDLvtnBGsuaRAydsDIWGQVp4MF2V-hMR4K_o6vFoXNG7gm1zKN96INs9YXLVZd1Nntdj2QbVVg8tez8-OF5P4tmwtwNbAXCdb9yrzW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔼
صعود یک پله‌ای در رنکینگ فیفا
؛
🇮🇷
ایران دوباره در جمع ۲۰ تیم برتر جهان
🔴
در فاصله ۶ روز تا شروع جام جهانی، رنکینگ جدید فیفا اعلام شد که براساس آن تیم ملی که در آنتالیا گامبیا و مالی را شکست داد، با یک پله صعود دوباره در رتبه ۲۰ جهان قرار گیرد.
📊
در این رنکینگ، آرژانتین تیم اول است و سوئیس و دانمارک تیم‌های قبل و بعد از ایران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/132796" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
🇵🇰
العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/132795" target="_blank">📅 16:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCSR8fq6NtUQWkAFDlfs6WfmYPloB53aLFvcPM0kfA3ePmtuZHzvlpEz0U5ycwg4rtObJQSzVsEfgUDLgX_5IrxkWAnS47VwZwUfozInxTmkcmumQBqv9XQno9Q4_s6F0hvO7JKIO7oD7d5lbR1XNkKPmdKwvQZlHU4LPWQgLZGBtdHav_VsFyxd7k75vkWvWwHmPXBAMCh67FJSk21c2ZUxIb0CLv6KssydVEpQ1oQshMJ5KsAGgS9h00WOPctu4UNTn3G06u0S6b1F5f3D-2nz1Rk8gYO3Q4Bo9aAvkgNnOc8jdqinM2aDlpuPBctgMBHzZpNF5GlrkMn5So8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132794" target="_blank">📅 15:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txP1-AwyUvMmcNcREm28OuAhGBGWLu07XNo7UAHGFH-xilcPjNF5T6wHmQKnAOA1soPc0Ei86Gcki-DDFzx4PG1xsMD3PTJkPYMhVw5pONRdju607h-jb6uTsfYo5utauFlD1vLWI-w5aqb76Ve3tgj4whZVkWsl8RWZTaYnD0FF0Qod2C-Bvl7LAmb0QdLCzTKfcpSrJNA0dqQCOfzjsG4Py4cNJfOmVdatJ_V4arxDEiFOPT8w60j6xCO589LkW2q48SVhJkKYSmi3kKOaC4bfRTF_RSjcoI19XZnL1eaOVhjuUHMdle6ZMjJy2O9bn2NcD_NwkaZXlHPJeXaYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سروش رفیعی به طور رسمی از پرسپولیس جدا شد. سایت ترانسفرمارکت هم این بازیکن رو بدون باشگاه اعلام کرده.
🔴
رفیعی در فصل اخیر طی ۲۳ مسابقه به عنوان هافبک بازیساز، آمار صفر پاس گل رو ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/132793" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVl6oO3cPc6tDecdl7DJ_174wxRNWRHv5RnDzlnE8U2pTVMv-QSIM02_XVZwEhPcJBLjNUO8Jg0GzvviUxncRIwsSRlk2XaZyK-seDzE6NNpDSgmxsjo7AmNtMXG0txbpdMTJYgRvE6I_f0glve5MXFpmIhBdTpmuubtbcP4CZLXxU-jn3OXz_F2yN_sWKvfgsOhn3OHQBO9piv5asLPXZmqOW0AjO0aUVlIMRa-WT7oQVUiSLhFEGu4YmzsBdOF8HiHkFYAgy0r_VdbouCEUsi5mnywGtkSRtG7OUVfxqYKtg0Rk4e1zy9Yq4vWNFI9Vz1NbN_IrqAsBg1vZpUxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/132792" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
🎙
مهدی تاج:
⏺
فقط با فیفا در ارتباطیم و هیچ تماسی با ایالات متحده نداریم. کشور میزبان حق اختلال در تیم را ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/132791" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/132790" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
با اعلام ایجنت سروش رفیعی، این بازیکن پس از سه سال از پر‌سپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132789" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132788" target="_blank">📅 13:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
اول یا اخر هرکسی بیاد و بخاد بره؛امثال سروش و هرکسی که حاشیه سازه و از نظر فنی به تیم کمک نمیکنه باید بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132784" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132783" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132782" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132781" target="_blank">📅 09:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSKtoxa11Abv9Y8vVC3tV3OBMr4MTGtfMj67NdWDCya7hDJ_RQ6TxerbKvs0Eaa2FvcPASgfqFRrISFd38ttipZBbY-hD2LGGrkcUnMK506WpcyqJD_YoXf9-eAtT5U-u2I5SV5dBe-zVo4qa6f1ndSu95ld1kctSg_3zI8_YZjbP4VG84-E-kSdekbxnIrUaI6r_carY1kP2v8Yuo1taenVZg17bfoqbeAugNPUIJU8DWogfJHK0SsRWx_PXMozAHuUB0Khl5GWchdV3bS1pXgFo_oYnR749AMnD0xAxGv4_xoF8342C4v_IRqrfitB54WL6GYdyUsVIBMKaOFsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132780" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
امروز عراق با اسپانیا بازی می‌کنه و جمهوری اسلامی با مالی!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132779" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132778" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=pWU5NAigBJi-rRRXJPmdMGf2ZWIdaCSVPqEl62Z_4b-bZrKvmB1-Ro3QzB9eFvYL6mXAUaHfJshs71xVrFRTemQf0RFoaDV9kpVmrN45RmlGu4aznEivAwPv__Ixrw9gRLNwKZZt49DF8gQrk3Vh6rI1FcNm4BkPPAf48rCzjKd-gNzaf10STZK_L1SYZh4URCoR53maFm-2FgAqL3fu7QF9RGjceaSW9I3-CYAxhjiqCPWNVKAqQH-aLE2j9MGerWeJQnqEJ5zI9ugDOsE1wSia4x9fOlNb26znF0rX3PUNaVX2fSmp2jDeyL_F0jkoH6u8Z6tIW7CVH9PS2n7lEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=pWU5NAigBJi-rRRXJPmdMGf2ZWIdaCSVPqEl62Z_4b-bZrKvmB1-Ro3QzB9eFvYL6mXAUaHfJshs71xVrFRTemQf0RFoaDV9kpVmrN45RmlGu4aznEivAwPv__Ixrw9gRLNwKZZt49DF8gQrk3Vh6rI1FcNm4BkPPAf48rCzjKd-gNzaf10STZK_L1SYZh4URCoR53maFm-2FgAqL3fu7QF9RGjceaSW9I3-CYAxhjiqCPWNVKAqQH-aLE2j9MGerWeJQnqEJ5zI9ugDOsE1wSia4x9fOlNb26znF0rX3PUNaVX2fSmp2jDeyL_F0jkoH6u8Z6tIW7CVH9PS2n7lEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ: مجتبی خامنه‌ای کاملا تو کارش حرفه‌ایه. البته یه سریا در موردش بد میگن که دروغه، مثل من که یه سریا به دروغ در موردم بد میگن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132777" target="_blank">📅 00:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132774" target="_blank">📅 23:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132773">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV0QlX1XZdhkXaXFQn3Ol43ZQvDxCn0DxeMYQSmFZ4f6Wd36Sf5g6v1ojrHvzUsKLDcV-3J7ne2lCbKdQC0P2jamXiPa-45ZdxRHhF2ad2ZhOqPYHbftBu2eUXDVa5xqlHH6_sJSjd2WZkQGohwRUJk-4ISovltTawoc6jKoRIgfEnGkXgxLgpOT-hFubgu6kWisp5YNP4NxpgCas8KNmRLQgx7oabK9cfB40HYYpDxBQGlwmq-70aebXlgg8l8gV6uRuGOfApu3nUTApPVBPhuAPSn1kSk4bDalmN5JQd3WVfNp3MtwjdVIs-aJPYPgvws3aKvpj-WVXDuy7hPJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران با دو برد مسافر جام جهانی شد | سعید عزت‌اللهی دقیقه ١٢ و رامین رضاییان دقیقه ۵۵ گل های ایران را به ثمر رساندند
ایران ۲
مالی ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132773" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/132772" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132770">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drBghXpXkcRflmKJeK3m6HLH1baZfPce8M3k_9uJwohdAjklSqelIsMM1YdEhn3Hl_MnXiRgV4LACM0mUxu7Oe39GmpVDZDjkAZ7vX1RLzyyCqSM7C8gFxsV1g8xvV_-2GrBEXseGgm07A99LrtvtkOB-VH0aZzd1kp48yCn6FRdHg5_7CNQ8reyyzjUVOwCH2L-wanBmumYsuNOZYglsVgJ2LoXLOqzS9gfB83RJVezM_TOeEfNrjpan82xFEc32RLP_hQ36qSxBhLSS4icidcxmWeihcFXaxxsw_SFvK52Uvzygi_PWhAnymHL52GM8-_EnYUB6QoqVcKwPaGvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گفته میشود که قرارداد امید عالیشاه با پرسپولیس به زودی تمدید می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/132770" target="_blank">📅 21:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuDbHEEnc_LnnwyXSCCT_KhsXyNTdzUr8pRdHnCQn3v3HLIXR_pt1GJq0X6Rpbk5i2K3o0upD387Av9xSCLv9dJ-3Fm_PNqoHoKr5025zc2ALDXcPmaV_WePQiLeoD9vDpW4UQGZTz1OoepJndnqKsPl3DmBqhTmfVwJI8lWqSyA-j02JqFs6Qr6oHv7YVzEEfRfdeoZmSTbQCb2tLRr5RviEE9bHyokKYNvB8CfzF7frDtgveSWoNWpyotxOQVyQ31F_swn-cA8rzzF6t8SeAlh-Z3Ip2I7cizJRF0r2yPHK-EE70JBIkaocbk_o7NU_uHrPOYAlQW3DqDCWVsm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:
🔴
استقلال درحال مذاکره با اسکوچیچ سرمربی سابق تراکتور است و جزو گزینه‌های خارجی این باشگاه است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132769" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔽
تیم ملی امشب از ساعت ۲۰:۳۰ به مصاف «مالی» می‌رود. این بازی پشت درهای بسته برگزار می‌شود تا بلژیک و مصر نتوانند به اسرار تاکتیکی قلعه‌نویی پی ببرند
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132768" target="_blank">📅 21:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
فوری کمیته انضباطی آندرس بازیکن چادرملو را غیرمجاز اعلام کرد و نتیجه بازی این تیم با گل‌گهر، 3 بر 0 به سود گل‌گهر سیرجان اعلام شد.
🔺
گل‌گهر با رای انضباطی، به رده چهارم لیگ برتر رسید و اختلاف امتیاز آن‌ها با پرسپولیس به 5 امتیاز افزایش یافت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132767" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAj7-4xyrqFWJL640Ff1Hu_7rR_M6bPKe50OHbgw0iWcPReknfVIjfi5gnY1jk7ugtVio-yAeVOYAHFQDj-zkem-473WhVLaJ47OSXtkJLhoHq0gncIU5E_RIbSHHyKxDm_ZdqNCVlUy-bhXr4Lh91hyn5VTxxH8csko5ndXP-Q6hUhO-C9VGJVV333BKcTsXR_R_DDBE3vHy70wmzAPMtw9qGvaeTpuTguucgCt2LBtiCsDWM_FgVKdU3EOyhu1YjymfZIq9XAlYuKZ5PSudPiQWJbT4PCss6ycMb9e9HayhnCBJgoHw4atgTLNvXaXq8NyovBAs9JvrzidwJlaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132766" target="_blank">📅 21:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Nd7GVP77pNHIjYLg2Aopttq1fJgsQuizklH3cl2if0vPN7gOHtpLunVro8xYXkvrgOyNPJI3UihO51hQD9OluIso6bGLW0v4icSibKUmGiXmsDOGBnz3WwcmCjhcu3Ax1LtTzZmv0KBI7ezkXgRTw0qdu4oG_QdYRvRCGqR5DexN_gL_SPig9989ictS37Sl8TtRFz7VZWsv5UMKffUBOPZx1hNSj6P5tlq9NuzszISEcak8Hb3-RcJaxzgxVRjDDPMjw8AXoLoc9ZHYIMQSsyco3u18osfyRq68HsvOV7A48cadHmxTt7ZMjwp4DWcWGXWlVQLSPv0di9L9Nh3vdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=Nd7GVP77pNHIjYLg2Aopttq1fJgsQuizklH3cl2if0vPN7gOHtpLunVro8xYXkvrgOyNPJI3UihO51hQD9OluIso6bGLW0v4icSibKUmGiXmsDOGBnz3WwcmCjhcu3Ax1LtTzZmv0KBI7ezkXgRTw0qdu4oG_QdYRvRCGqR5DexN_gL_SPig9989ictS37Sl8TtRFz7VZWsv5UMKffUBOPZx1hNSj6P5tlq9NuzszISEcak8Hb3-RcJaxzgxVRjDDPMjw8AXoLoc9ZHYIMQSsyco3u18osfyRq68HsvOV7A48cadHmxTt7ZMjwp4DWcWGXWlVQLSPv0di9L9Nh3vdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132765" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3zT_9vbzBq9oy_DeqmhoTxHcoGpdvZVjsj4DYiG7P531IDQR7bEIfgIS1vnUMvWWZZNxx3rgZrumbpdd4ETqqwZ8eMn4jjMMMIE-JTt4xTfnSg2ZAzhOo6lQPV_1xDbmK5ubr3CSu7dD1VjJCJx8FogE7uYbq1SoiQT0HbZkXv4bOaSr6yt-M82euS7mnDfO3bP-dPosgOEznnxuxmoxrUSsMReAYhvaQzm-DaceGHXH-7TT6jRrv_KqcCped28wAFmsK1rsTwk01WztLc_JqVzYRq0Gyppr8hql-Tb4MnX6jbFxjb_njq8_FdhRhKrzt5M--9AjGpqelW0wPQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#رسمی
| با اعلام رسمی باشگاه بنفیکا، رئال مادرید بند فسخ ۱۵ میلیون یورویی ژوزه مورینیو را فعال کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132763" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
فوری کمیته انضباطی آندرس بازیکن چادرملو را غیرمجاز اعلام کرد و نتیجه بازی این تیم با گل‌گهر، 3 بر 0 به سود گل‌گهر سیرجان اعلام شد.
🔺
گل‌گهر با رای انضباطی، به رده چهارم لیگ برتر رسید و اختلاف امتیاز آن‌ها با پرسپولیس به 5 امتیاز افزایش یافت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132762" target="_blank">📅 19:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
باشگاه گل‌گهر از چادرملو بابت استفاده از آندرس، بازیکن پارگوئه ای شکایت کرده و خواهان 3 بر 0 شدن مسابقه این تیم برابر چادرملو شده است؛ در صورتی که چادرملو در این پرونده محکوم شود، جایگاه چهارمی خود را از دست داده و به رده ششم جدول سقوط خواهد کرد و پرسپولیس…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132761" target="_blank">📅 19:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
یاسین سلمانی در پرسپولیس میماند؟ آخرین گمانه‌زنی ها از ماندن ستاره خاموش پرسپولیس
◽️
یاسین سلمانی که پس‌از پارگی رباط صلیبی خود بازگشت موفقی در دو فصل اخیر سرخپوشان نداشت، بنظر میرسد یکبار دیگر شانس به او روی کرده و اوسمار ویرا قصد دارد این بازیکن را به…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132760" target="_blank">📅 19:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
⚠️
طبق تست های انجام شده روی اینترنت مخابرات و ثابت ایرانسل وضعیت اتصال به دیتاسنترهای خارجی و اتصال به VPN کاملا پایدار شده است !  اینترنت به حالت قبل از ۱۸-۱۹دی برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132758" target="_blank">📅 17:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59133ac2f8.mp4?token=qPgFdBdcG4IHVHNeIhrfb0ruRJ76TM7jYhEDfwQSnuYbBlBi72C87egSWOFXVMXMBn6Bio5JohhfKID_iEl7YJ0H8UWTIuLMvGe8g63PTRZ96zxT6pTEcvxfGuCbp-V6FaFemrqBALTZ3GkcxwNxkjNtDozu17h5A704a7998-y8HiDLk7UDYX8WiQoh9yqR-T5uWtCYSDCAmOojetcEdlJ4Z3mCniehuRDKV6mN6FKgx23bB-2UPsdxQTCkH1hm1IPYGD7Ckgpc0iNmv5VwkI9AuXe8AS5S8GfjwQbTKBg52S8OgbiLy8U3VURKSADYdPFDPxb_OR7M0g3WJUDZPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59133ac2f8.mp4?token=qPgFdBdcG4IHVHNeIhrfb0ruRJ76TM7jYhEDfwQSnuYbBlBi72C87egSWOFXVMXMBn6Bio5JohhfKID_iEl7YJ0H8UWTIuLMvGe8g63PTRZ96zxT6pTEcvxfGuCbp-V6FaFemrqBALTZ3GkcxwNxkjNtDozu17h5A704a7998-y8HiDLk7UDYX8WiQoh9yqR-T5uWtCYSDCAmOojetcEdlJ4Z3mCniehuRDKV6mN6FKgx23bB-2UPsdxQTCkH1hm1IPYGD7Ckgpc0iNmv5VwkI9AuXe8AS5S8GfjwQbTKBg52S8OgbiLy8U3VURKSADYdPFDPxb_OR7M0g3WJUDZPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🎙
صحبتهای عیسی ترائوره مدیر تیم ملی مالی و بازیکن سابق تیم فوتبال پرسپولیس:
🇮🇷
ایران در قلب من است
⚪️
کشور شما به من همه چیز داد و خانه دوم من است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132757" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
خبرورزشی: اوسمار تاکید داره درصورت شرایط عادی بمونه برمیگرده و نمیخواد جدا بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132756" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
♦️
تاج: مانع اصلی ویزای آمریکاست که نمی‌دانیم در چه مرحله‌ای است/ سعی می‌کنیم با پرواز به لس‌آنجلس برویم
🔹️
رئیس فدراسیون فوتبال: پذیرفته شد که بدون انگشت‌نگاری ویزای مکزیک را برای تیم صادر کنند. دو نفر مانده که آنها هم در کنار تیم هستند و تا ساعات آینده این…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132755" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
بزارید تکلیف سرمربی برای فصل بعد مشخص بشه بعد درباره لیست ورود و خروج صحبت کنید،باتشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132753" target="_blank">📅 16:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
بزارید تکلیف سرمربی برای فصل بعد مشخص بشه بعد درباره لیست ورود و خروج صحبت کنید،باتشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132752" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس تاکنون هیچ لیست خروجی به باشگاه اعلام نشده و حدس گمان ها در رابطه با مازاد شدن برخی چهره ها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132751" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔽
اینترنت بین الملل وصل است اما مردم دسترسی به پیام رسان های خارجی ندارند
🔴
قطعی حدودا سه ماهه کاربرا و به پایان رسیدن اشتراک های فیلترشکن آنها باعث شده، تا با وجود وصل شدن اینترنت، حدود 80٪ مردم در اتصال به تلگرام و سایر پیامرسان های خارجی دچار مشکل شوند.…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132748" target="_blank">📅 14:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFHyuLxdA4f9Lah_ciwNBpV6cl6Nmh07L6JTElqm2R_npVbsnrhTZpRI1DtLEcdVM64mBkyFcQ5NlhzP2ItPyIzuAszBnLgZuYajl-GTE6yLDrgfJmNr3NFgcvtrKeTp3mNP73BsceVpEX5MtOcpgD4wFKxano0cSbh0C64xBM8ibBmmpCt1nxNod-CeNxCTgDMdBTuVow1dCdTB-dU3TBmtKC_n97uNyr6LU0792jsHdI4Rlv6oWzNcgn94GRQpp6mnOcsOZxLIhjqaEMSNBw6DxpYL_rnsUidQ704brHOJCYQHWHFOvIqQ4MPTvLxQ5E0R4iTVJDHsrQQkkrcvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طارمی در گفتگو با الجزیره: آمریکا باید به این اصل که ورزش از سیاست جداست عمل کند
🔴
اتفاقاتی که در حمله آمریکا برای ایران افتاده خیلی بد بود و ما فقط می‌توانیم با بازی کردن دل مردم را شاد کنیم.
🔴
ما ایرانی‌ها آدم‌های صلح طلبی هستیم و دنیا درمورد ما اشتباه…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132747" target="_blank">📅 14:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
فوری رسما امریکا پایان جنگ رو اعلام کرد
🔴
روبیو، وزیر خارجه آمریکا:   ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132746" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
علی دایی هیچ صفحه ای در توییتر ندارد و این توییت هم که وایرال شده ربطی به ایشان ندارد.این را با اطمینان می گوییم/قرمزانلاین.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132745" target="_blank">📅 14:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔽
تیم ملی امشب از ساعت ۲۰:۳۰ به مصاف «مالی» می‌رود. این بازی پشت درهای بسته برگزار می‌شود تا بلژیک و مصر نتوانند به اسرار تاکتیکی قلعه‌نویی پی ببرند
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132744" target="_blank">📅 14:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132743" target="_blank">📅 14:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس تاکنون هیچ لیست خروجی به باشگاه اعلام نشده و حدس گمان ها در رابطه با مازاد شدن برخی چهره ها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132742" target="_blank">📅 13:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT6Z4ksun_fowNCrDJ3FEdR2wgx5Q58qe3ieN7uQhus49ivcXRwnGok_6hg6VKZ2Jn6-1l9ZWvPpYG2GZ4cwo5NrNUAHMOW_N5pxe0q5ak7FZqHIHtrbYr8MtC8oNCN0pvoBSuprLNGCk3U5vgtm11rPNBsdR-n4A_76q1s3H1noUskYy7MrPZABObLrXKwj6V_Bj0rXDZOWxqZ5jIk8Mwy5ZMto8cEk-BSrOj88RfFUYztmsuNsZwZ2_tElvNIz3EIj-kBgxBedhAvrX0ustDyuaiFtNZRNmlOXeCWny36X7UGFwaxiOt_JxCee7r9-1x-W3pdXPVUoHH5juuZKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
-
مزیت روش ورود از طریق ربات:
👇
• حذف جستجوی دستی
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132741" target="_blank">📅 13:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCnGlsSD7434SF8m-iTFnMfcanRdaY9h8etcWvO5DVdePNBdY4MWsO7_bEc-FP7vJ6kH6FX4p37wTJ8TrSapLQ7F6QzURwRMzfsaVakM8AnmG363Bj_J0PGNuAR5fjz1l2kkwIdsZ0WnyxkLfbh4_ua6t1CbnjvI_V6SlSp-z82iGFqtfKkvL_lpIW4fb8TyISghDGg1Msa4temBK4x6SxC5sYFFjLsStKExWKUNp0Pt1CDOa5OkOh8WCBo4NJPSba4ghySRN5k4dZhjmzprdWwSNfDDZ1_g_gWd9mj9lWqsY-x8AyCE13wSRwNtNdSV0ShEtdX3u-Do_GaB0cM7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پست جدید بازگشا مدیر
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132739" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
👋
خداحافظی مهرشاد اسدی از هواداران پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132736" target="_blank">📅 12:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⏺
⏺
⏺
یحیی گل محمدی: با حضور گرشاسبی آرامش قلبی پیدا کردم
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132735" target="_blank">📅 12:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132734" target="_blank">📅 11:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy8LizR4b6RJ7LXfE3wgVKiW2PNwzdZmsZN7GuM7_0ltr6t_0VWpeFYlT8IkMfpizgCiAKddr-MP8N3qy1HGGQdU4LhGDoxumuR_gTMUx7WTL_EnEflTl3kwAab1EosI3oglNBJ1RkMD_XXp6ENnbsWA8nhx7KiHp_1cv8rqELu-FRAmvzWK3F1g2HnhzpfEzmPWTZ0Z0WJVH4Ru9lZPbS_ub0PdoCeCwq4eSpnUM5fB_ZYg3YfUH1qoRgHcU-Z2aPl45Ytre8QT6CsZUMPc6T14f-ZJ8VLXmC7OHJROGPIUmcf0JXMzx0psY3_ur9mifJJt0X5TX17xJDQdp1i9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ریکلمه دیشب تو یه حرکت پشم ریزون پیراهن 9 رئال مادرید با اسم هالند رو به هوادارا نشون داد و اعلام کرد رای بیاره قرارداد هالند رسمی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132733" target="_blank">📅 11:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAJvVjb7lmJITih4fl_6u9iyMIlatzFrS3FmZbBeigp_ElU7wxcgz37nyJGbKES9mN_0U3CwbXgIJyLcEVmoKgOM0VGCxqVHhYU0H4PkRNUHU7d9s-Nutm30TCAadD4PCUCT3JS2LJWk4PEzoAaq4bklvYXhUoZWrRkvc65dU9Y8v1dvLPKw6K6a19JJChznzvQbVAAWMOA_5x9ZnGIwjDjUDub3T6646a5Tqg0wVLCbq9RWIScWliA35d8Ml_1ygySsb4JhaAjoz8Bpz9k-TyQqfSUwmpNSPMuPDHfTXXbhFev12RiFFCIopdYjJ0YpNvSIAhj_tI1fmPHPj5GsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ریکلمه دیشب تو یه حرکت پشم ریزون پیراهن 9 رئال مادرید با اسم هالند رو به هوادارا نشون داد و اعلام کرد رای بیاره قرارداد هالند رسمی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132732" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0583b73b4c.mp4?token=vb5Q7pFSKv0XIFy-45-A1GsnvAA9HaPbLRkMjA8Wp4JNpQV92fS7yF49VX6hAElqOkz_hXtRLU-Uso1MnhdBf7CksWHmy0aRjnZt6sNOH6ZlCll2-0lGxfSgF7lAwl94MthlBtvPE9wsmVxWqaZTGh7zkWkIIDIM2xXEc6oNLecaEDw_0r5PqiCAm3yg4i0OWVmlpr8rHRqck0VcY1ePKpJ8KBf9-o17NRYmxIIMpYAMupnOkzymkn3pgKNHSXfAUD1cOAMuW0hQAeHubyXtU67FRREZK9mG8KDlsvW2oGrIBNfC3pklDsjQeR23gh6fzYoazWLf4qJmpthODZx13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0583b73b4c.mp4?token=vb5Q7pFSKv0XIFy-45-A1GsnvAA9HaPbLRkMjA8Wp4JNpQV92fS7yF49VX6hAElqOkz_hXtRLU-Uso1MnhdBf7CksWHmy0aRjnZt6sNOH6ZlCll2-0lGxfSgF7lAwl94MthlBtvPE9wsmVxWqaZTGh7zkWkIIDIM2xXEc6oNLecaEDw_0r5PqiCAm3yg4i0OWVmlpr8rHRqck0VcY1ePKpJ8KBf9-o17NRYmxIIMpYAMupnOkzymkn3pgKNHSXfAUD1cOAMuW0hQAeHubyXtU67FRREZK9mG8KDlsvW2oGrIBNfC3pklDsjQeR23gh6fzYoazWLf4qJmpthODZx13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
⚪️
فلورنتینو پرز رسما از ژوزه مورینیو به عنوان سرمربی آینده رئال رونمایی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132731" target="_blank">📅 11:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
ترامپ همین الان
🔴
خود مذاکرات خوب پیش میره اما ممکنه انجام نشه اما اگر بخواد توافقات انجام بشه باید تا آخر هفته انجام بشه ؛ ما نیروهامون همه آماده هستند و بیشتر هم شدن و راحت میتونیم چند هفته دوباره وارد بیشیم و کلا کار رو تموم کنیم اما توافقات انجام بشه…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132730" target="_blank">📅 10:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpcdOJLuUwEYV6W7QnsA5TIoId0zOGJYUJMvywEFMpZ7-xRL2TpyLe9pDVOagGubZ8Q5_wfr00Llk1uc7MjLhxBa6LS3zI7Sd6WppCZhCjqabHmId2UlOYDX8tHnUcJAf1-yFocjTImKEc135dfODB_o9T-2rMSYb5l7YiVLcdjpraiXD6ciaLXd0DW7wLIb1tzkzQ2lT9cgfcg7-NEiyeetYG_JKIPtWHGKnl7WQ9BPe-X93c45VVPW1fOLmXhq_NqAESjlohC3xriw8RXZaOkWT9R6lwkFBdZphmHqxeD9vPTyS50Zv1G6mlo4UDwU0tS-uKYirMUC_zeyqsyjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دلارزاده با ارزش‌ ۱۰۰ هزار دلاری، جزء کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132729" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb6uFVgFamY-oI-MzrFrNDAiiZOIPkGL9_oOzYM6DCfje3790-n7IZmaX-0EMwvvk08evgw3M9V3Vgka6ss2BKe6bIrFyGxDLgb7t7Zk1tIoRBwcLFQuP3ezVhriwPgzDbaLW181siKsF8_qCGeODc6_XhcxsK1B6Nq7Jjxm6x4qsDESN4sqkT-LuZGJGm_Xcc2cBszeKVV0iI0G_Cuj4vtglCpUAkM_CA-usDpZq8c68HKw1EyOXlmNgiNvrl85JO-hM_2lttkQez_EUtG84si8r74ReB7QWeOtkSRuYqMlmLa1dNfAOq3r8dNacy5XBrjvnTMWnRDc3GrVAPqlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132728" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
◻️
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
◻️
ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132727" target="_blank">📅 10:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf9zSgwc3ygow20P6aMMeUZFSfLr_lb6it-gz6UYBkhv85KN6nKMe89tUVUGaFmtZLbkTqlVi4C5CyI150YWC8ExwO0Jc_repRf0kFcsLO0CX6G22oQgVUSvDo0Tcua_jDulni0NFjo72C6J-bX8Zyu3zY2Yhh1axu4P7vAG6ZqLLg2WiY2XUNOofu_Y1yzxlSX0ad3KMg-QYlg1bVD9k4V82OPuBrbcjhat9RQ5GzD2oz_4iMaKEy9FnXEMbnn6dO9ak_0yqh98tDVfdKI0_b7G8GvdbS99ZzPFVnCeNyMtfouCB-1nck0CmS_IrhokrLKwarZ72dbJlscsG_nAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
◻️
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
◻️
ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132726" target="_blank">📅 10:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132724">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=mk0iQiIDK8TxbDNXVWwmQ1a-ICyP-C8EOT1b_jW3xkO2kxv_zN-4INISgkEpBpw_jl8goxQQBSSggSsvDfzl6ODnFPQumK_bUVvJeZujmMRObzi9pVLlrMlmf8N8SkBD2wIgt9kc_-EAQaMPB9fe9ogoD6HKE4Y-AlfhuiHOYMOzdIGb2NXFnbJJ0rsxVbEs_o9NXfucGDafmDi5KvgizetrOrj0zVMYUOIzL3J7LnUN6vZ-UdsPyx07WaqxLg6ktGAH2XqFCX5dKa4JuNlPNHlf8Vt4AIsAeXSVa3ypLtGD5lF40aZ7Cdu2wgN1bPsq4BpahK4frRI94z3rJsgf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=mk0iQiIDK8TxbDNXVWwmQ1a-ICyP-C8EOT1b_jW3xkO2kxv_zN-4INISgkEpBpw_jl8goxQQBSSggSsvDfzl6ODnFPQumK_bUVvJeZujmMRObzi9pVLlrMlmf8N8SkBD2wIgt9kc_-EAQaMPB9fe9ogoD6HKE4Y-AlfhuiHOYMOzdIGb2NXFnbJJ0rsxVbEs_o9NXfucGDafmDi5KvgizetrOrj0zVMYUOIzL3J7LnUN6vZ-UdsPyx07WaqxLg6ktGAH2XqFCX5dKa4JuNlPNHlf8Vt4AIsAeXSVa3ypLtGD5lF40aZ7Cdu2wgN1bPsq4BpahK4frRI94z3rJsgf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه رایگان وینکوبت رو از دست نده!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132724" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132723">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132723" target="_blank">📅 01:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132722">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🚨
ترامپ:
🟢
نیازی به حمله زمینی به ایران نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132722" target="_blank">📅 00:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132721">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
پاداش ویژه مدیرعامل باشگاه پرسپولیس به امیرحسین محمودی
🔴
دکتر پیمان حدادی به دلیل درخشش امیرحسین محمودی در اردوی پیش از جام جهانی تیم ملی و راهیابی او به عنوان جوان‌ترین بازیکن، یک پاداش ویژه برای وی در نظر گرفته است. این پاداش پس از بازگشت محمودی از اردو…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132721" target="_blank">📅 00:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132720">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op5aHkFMiIWNh807h80vRa6_t-rynZkpPVF5fZjLBBvBAszllSntLXzNrtMcCSky4ehEiEZww-bSvP1bNfgMuX2dWVZW1FtUBpNd9HmlGIndI3NFq6ph6Gs9p6yQF_l5tzzeyYphjU3mi7wWcvzAqizMqoyxQWHZvxseDyWdZ9W50SFn9tqQ_73eiyZCrYFQ9bvxuvXIBhre6NPDLSHoyhoJ4fQo4tfDI8HTiV9wyEBLvM8rHCLc9HAVhUeyQIs8aRc27AiwqVCRhJqqF54yFe9tX-tgig-6iRWGI0bR7ikeN8IIG-u-AhBIXh09DZWyv-oTqLsGUXTvUi6YkF6VKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قدوسی: باشگاه درحال مذاکره با اوسمار تا وضعیتش برای فصل آینده مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132720" target="_blank">📅 00:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
طهماسبی، سرپرست هوادار: پرسپولیس مایل به خرید امتیاز هوادار است اما ما تمایلی نداریم
⚪️
خرید امتیاز هوادار توسط پرسپولیس؟ این موضوع به قبل از جنگ برمی‌گردد. پیش از آن، باشگاه پرسپولیس صحبت‌هایی انجام داده بود و جلساتی هم برگزار شد. آن‌ها تمایل زیادی داشتند…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132719" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132718" target="_blank">📅 23:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132717" target="_blank">📅 22:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132716">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری؛ سروش رفیعی از پرسپولیس جدا شد /فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132716" target="_blank">📅 22:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132715" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0FWzdbjPplWTecEk6jN8FaMKZkPdnoKDudgvYHj7F_NBKjwXu-e-jTzUSzXI2SiGFrisV7lPhFcdFoHw7Bmkq8ZOcH_tEFnU0U2Dn-aEL4-ipXeVsoovF0_M1vEI-guQJlhkB6WPHAsTuH0twFR84yEK6p69pTotFMXtk70rUtlA2EF1IlByZclStiaYafBQw7X1ulD7mjjEVAWw28H1YMiRtChIhpQJIW2owrDviCWRCWxm4RmjWd0FbK1NjxGGq316heOnFWW4siZwc14SJqRzP0KPcvdCRni3H7nHP-ruA9WbOjtx2qjptsyOrB7VFaKshJ2KcIWokDNgO0E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آوا اسپرت کوردستان: یحیی گل‌محمدی اکنون در دهوک است و فصل آینده سرمربی تیم دهوک خواهد شد، قرارداد امروز امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132714" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
فرهیختگان: باشگاه قصد داره اول با گرا و بیفوما برای فسخ توافق کنه و بعدش اسمشون رو در لیست مازاد اعلام کنه تا مثل اوریه بگا نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132713" target="_blank">📅 22:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/132711" target="_blank">📅 20:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای (رهبر شهید )   ۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی  ۲۳ خرداد/ تشییع در تهران  ۲۴ خرداد/ تشییع در قم  ۲۵ خرداد/ تشییع در عراق  ۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد  پ.ن تخمین جمعیت حدود 25 تا…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132710" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
رسما پایان جنگ اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132709" target="_blank">📅 20:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚩
مارکو روبیو، وزیر خارجه آمریکا:
🟢
جنگ در ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132708" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
واکنش اسمار به  شایعه  اخبار جدایی او
📍
دلم برای انرژی آزادی تنگ شده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132707" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
حسینی؛ سردبیر خط انرژی:  متاسفانه تابستان بسیار گرمی در پیش داریم و زمستون سرد ! توی جنگ اخیر به شدت بخش انرژی ما اسیب دیده و الان اگر چیزی حس نمیکنید بخاطر این هست که فصل گرما شروع نشده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132706" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
واکنش اسمار به  شایعه  اخبار جدایی او
📍
دلم برای انرژی آزادی تنگ شده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132705" target="_blank">📅 20:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای
(رهبر شهید )
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
۲۳ خرداد/ تشییع در تهران
۲۴ خرداد/ تشییع در قم
۲۵ خرداد/ تشییع در عراق
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
پ.ن تخمین جمعیت حدود 25 تا 30 میلیونی زده شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132704" target="_blank">📅 20:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
🔴
آسیایی شدن پرسپولیس در گرو تصمیم cas
◻️
باشگاه پرسپولیس در تلاش است با استفاده از مسیرهای قانونی، شانس حضورش در رقابت‌های آسیایی را افزایش دهد. تعیین‌تکلیف شکایت این باشگاه از ملوان در دادگاه CAS زمان‌بر است، مگر اینکه درخواست رسیدگی فوری پرسپولیس پذیرفته…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132703" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
با توجه به اینکه قرارداد سروش رفیعی تا پایان فصل به اتمام می‌رسد و باشگاه هم علاقه‌ای به ادامه همکاری با این بازیکن ندارد، احتمال تمدید قرارداد او حالا از بین رفته و با پایان نیمه‌کاره لیگ بیست‌وپنجم، به‌طور قطعی دیگر جایی در لیست پرسپولیسی‌ها در فصل آینده…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132702" target="_blank">📅 19:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132701" target="_blank">📅 19:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
نتانیاهو: ترامپ معتقده که میتونه مشکل غنی‌سازی رو با مذاکرات حل کنه؛ من فکر میکنم باید بهش فرصت داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132699" target="_blank">📅 18:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
یک بـازی بیشتر گـل‌گـهر و ابـهام در تصمیم‌گـیری سهمیه آسیـا
🔴
در حالی که پرسپولیس ، گل‌گهر و چادرملو مدعی کسب سهمیه آسیایی هستند ، فدراسیون فوتبال برای تعیین نماینده سوم ایران کارگروهی ویژه تشکیل داده است. نکته قابل توجه اینجاست که علیرضا اسفندیارپور، مدیرعامل…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132698" target="_blank">📅 18:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
شجاع خلیل‌زاده، با ۳۷ سال سن، پیرترین بازیکن تاریخ ایران در کل ادوار جام جهانی فوتبال خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132697" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.  این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132696" target="_blank">📅 18:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🚨
ترامپ:
🟢
نیازی به حمله زمینی به ایران نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132695" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
گل گهر، چادرملو و پرسپولیس به ترتیب به علت حضور در رتبه های چهارم، پنجم و ششم در صورت کسی مجوز حرفه‌ای جایگزین سپاهان در لیگ قهرمانان آسیا سطح دو خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132694" target="_blank">📅 18:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
ترامپ   به نظر میرسد که ما با آیت‌ الله رابطه خوبی داریم دوست دارم او را ملاقات کنم. احتمالاً در مقطعی او را ملاقات خواهم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132693" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9aKW7FTgLXoWtFRm4SWHbT3RIZd3JsJvULcUMwPisRrA88pKNaPWHK745EaEFH7HvQKrJqj4FEDTAsuVTU90eu1sc80Gr-iUji78rAfnkpRYdUe1eJQq8lyNmGwTIvTS9cYCMYYqlUwIsvA6L_sBFKgIsL8X1Ao3Yna_yWQX_vPgx9KKa3wDio1yowrSnF--U5Sa4lpR4N-R5mGNTyPgWJ6mjtGE8L9cdI1pKlRNKqmD2u4tvWk9F9hr0p1ltSjvr4NcJTeFq44tOunMu3zkhWjwE39960YtfrEQIGVLA3N48uvwwu8mThBbxWmkgevzmc_C4JMpysCx8tJEpv_OEk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9aKW7FTgLXoWtFRm4SWHbT3RIZd3JsJvULcUMwPisRrA88pKNaPWHK745EaEFH7HvQKrJqj4FEDTAsuVTU90eu1sc80Gr-iUji78rAfnkpRYdUe1eJQq8lyNmGwTIvTS9cYCMYYqlUwIsvA6L_sBFKgIsL8X1Ao3Yna_yWQX_vPgx9KKa3wDio1yowrSnF--U5Sa4lpR4N-R5mGNTyPgWJ6mjtGE8L9cdI1pKlRNKqmD2u4tvWk9F9hr0p1ltSjvr4NcJTeFq44tOunMu3zkhWjwE39960YtfrEQIGVLA3N48uvwwu8mThBbxWmkgevzmc_C4JMpysCx8tJEpv_OEk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویزای اعضای تیم ملی برای حضور در جام جهانی صادر شد
⚪️
سفیر ایران در ترکیه: ویزای اعضای تیم ملی برای حضور در مکزیک، امروز صادر و تحویل بازیکنان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132692" target="_blank">📅 15:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🖍
دو باشگاه پرسپولیس و هوادار تهران برای واگذاری امتیاز این باشگاه لیگ یکی به باشگاه پرسپولیس به توافق رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132691" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132690" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0PbVkOsepiqGlfaWiTbiqixIBZbNOGOPizRve__H01krP1h7vXV5mU4Q8Un4Vuv3YOhGBNbHZZkk9jhVVX57BGgJ4D7wrlZHsufNTdehMg8cWo_c9UbnzdlamVLmpuBT4tQrRrGILFgRdlr3RRJaotvJAlzC6Dp5VPixKeZFDLkLd0gn5aCCX4cfWahQnYIKOGNO_C2LF36OkYYao9AVYckiqMmQURHEm__c-sINE8bjY181-cA5bvP_BZV9MDgj42NnpwrxhheaYUOWZTa0_MfsYfUm_pLIxebXRadYD0XmeLaKCwUPBzd_B9IRYszNCVPEVtUfk_l5dpKiNZCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
رقابت جذاب و حساس برای رسیدن به نیمه‌نهایی رولان‌گاروس، دیدارهای هیجان‌انگیز امروز تنیس رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132689" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVtVTWAQdstZsodah2t0L3D38GZXeuWWgFkcP0i0SVVUpVHIGfOPLYBKuj83GAZsD1nasjpYfUJ0xlME_LWpTenqYHgaGBELCjIn2bQZ4o2l3RMLJ955jpTWJNieA7KIEY98luFduU4_foYHFwr7wKp284BahDNbWpT-fU5pPaSCsyM3IbroC0RCy6QFYZQBys1sJCOeSwKcukx753YQIhSNYgFNtdXSROQEO3O0He3B_cUJxTERmK0mHZc672pwVCElR2NXydZsLXkBvMO-nwSqC28yE3hosNIs9h3Eloexit57z803z5kqDnB80jkEWfs_Nlf6to4p6LQdWu6tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
روز کارگر که ترامپ گفت ممکن است محاصره دریایی ایران را لغو کند 4 مهرماه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132688" target="_blank">📅 14:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
ترامپ   به نظر میرسد که ما با آیت‌ الله رابطه خوبی داریم دوست دارم او را ملاقات کنم. احتمالاً در مقطعی او را ملاقات خواهم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132687" target="_blank">📅 14:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🚨
ادعای ترامپ:
🟢
شاید با مجتبی خامنه‌ای دیدار کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132686" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ برای هزارمین بار گفت؛
🟢
ایران موافقت کرده سلاح هسته‌ای نداشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132685" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
