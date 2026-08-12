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
<img src="https://cdn1.telesco.pe/file/qtKXk2vi8rK84YFnC6zJW6KyYmpRFFbpJ9RCpDMm4sjKUbYrVKs9Az92JoO5-p_D6D4FfBN_x7fNaPYNJ_-l53GdDywTfj1yExR-eamhNjYkgSri97VZXbEE8mjXyWJy7X3H5ExuJ6_Yw2YQ9iw_qA07qK6hw0r1rb9dOAhlYxJ0H7SxzHYn-Jq627rLyfZpE0uCav4yb5wia2FKqnShuXsPAgTRyLPAkQmF9b7oYS2rk2MOF97sgCRHXliXLNH3zmZJzN6JEKKXBSbx-FF0-3BJdOUciyP6uWRUQbShTXN5uE7lJ0wz0JYflXpCMixu3AlGpkAvXifsjrGE3rP3BA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 07:03:24</div>
<hr>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gBXSIMzYhHkr1gB_i_k1Zuubt_4jriXwFPvHtNGwjaywAH4viCr80SWd48KjzX6zUb3bxn5HMDKyzj4GLlGHMJiOLbWS_fRReEf-kAFGwaC8A35wSaMKqSENVLKpEV4F8NLF5-yrmWmfIrwOcellkJaKjBO017R2-O5l9Ro6cB02DXNthHPihX2D8xzQpK6Wh4XfYll6NAuk_SECD_HXloVHlB6RKTJg8qd08BqWimmqQqyu5uBmT9pJSwM78A7SOEU2ro0cmQv2hUDKkUnNmPOhYrjmj0bt3as1Y-zMCORMD6S5MCa27zifjwLRxovkHoFv7dmQDcqSCj81TpTtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-p4XHGAoPo-jhjEuBCGdywnyi-Dk53iFGtZMav7lNc2-XjjYxd2VaAVD9tDh4Qab95IFWCcv_AgILAqWZqQuALF2wukXDb6tbxl-Wsh6IulFInWdlTjsDjTVj3YXF0Nb5_02ca0XAYzWvmoaiLBqc7A6pLwjskIjRUtZTcVea0NztaXVXXYYeHVVki3anHFzS2Ictk4vYiySiYV1oJ9-WGz3vDcOPywz2xE_I2iUsK0SGHLwQgc3MGMjV8gaVlKW9u_yoHaWnUfA-FfJmXL0ZbKGsjGEyMREHLb2qhGD3zWtXIM_J3efDUaOGBW6HXVkBoylSriQFYhdib4lhsz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_VUsCmX1GJqfJbQzXHGPgHO3Saxa3XBus7Z8lnRwJsnSWRgwKOOSDdjcij_5lRfpcS0yILsA6giaTykH5DCaOMXYHF7XfLNPxfbKw-4GNIlV_dpi5IwhUhyOH4hOSsOBL-kUA3nWqBFJGC9OTWZTHjslX3qb6IxrjKq-2zTKjV23nWYM_kH5PYvmsqt_My0WeHGIwabHn17VoSQiwf0RW0Xi2pOhuH5e50F8zche-g_Gue8Uz2wmZTKFotFSj5IjmLd39Zt1QaVsl9vJQPg6C0Eq1yY_ahduVQcPC-ucKFG-EyUuf23gIVgTWoRXb1wj-ZmdWZQ7XAfS9jwCb0irA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBE4smuCu2KQzHi2FpzPDlLp0_LU4iWd3oF1DWfsjXVNLe_OJSnosWF_O-5EQdn3B6-rhK8fTvkoLvwmvvyLsOs6heJI5VH00VtEKU79Joqtw-kRQrF0J20Cp9p2AouykAmi-N8dPo_qVw3x_q8HnCYLvO1uYSnybCIJBwPCY62nfdeVJ2UQeuWw4Ea6XJUxBinyjjQDZSzJjC6Byt4Nj5OfstT_n1QH973kwBhwDV0wgCFoBHwZ-hJj7xx4wUly-SxEzhEih2my0FzSPkN7u0bua-Lhxul3nc7Z5lkO7V2Sm-tzTUf41ybRskSXMjgT0sb_gUlY38l7PnWY9tltfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lLcaL_1oJsU56Y2FDmzim5AIaghrgkRr2tgqGmHXcWeW_mj0R0ewlqaVyqbVMKwY-xjm0FLIwO8X8SwE6fJoQg9vy-zo6eytG6qGGW2XAiWLDX7UZLWpEax6Ctl5jY_OHkmdfdS62ByQTT2-n__Hzi0kx7Ehsw3NCMOzdaCHGzOYfShjU-eQrf7OKEqfrtGfGlEmShoVcr1UYojBIAmR-g44G3rs_Ix_I3cl00eoYqDaGrrxkIVFLulsATPY-JbD0tgJwt6VeiUvjqOtdS6pQ6uBf9NwLO_ncd9sc8viZFY8xAKo-4Bk5zrrYA_h_z3BM7F1pUZxTs8uPX4ylinJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=B5o_D0EVom6brXn-4NfIhQLCXNkxSrFyhlwANH0c7V1LJ3NARoT11QD5u1M2Q-xyygniCFbWJH9PPRrsZ0iF3dQ1-xJk3RN91KHNni7ieW81UcPwWIMEuZ2jjjO8Z6YRK7WuEDgYwH8I0J1yJQDLS-rGnmVkqcB9DpYX2HwgtmWJYKU1uox_WUxEql7PjSgdU7tLkpRYcLDsx7XVU5sEhABr79LhQOkh7ViMl1YOsFLk1zRHEich883bZ9O-2hTWSIWNZ5ogn2dQTvHCv2qz8H_6roG0BzYc2pLTiK1tPyb0It8UMnOE1IwvpI5KRrgh1pb2GihkE2_DUXYAcNc58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=B5o_D0EVom6brXn-4NfIhQLCXNkxSrFyhlwANH0c7V1LJ3NARoT11QD5u1M2Q-xyygniCFbWJH9PPRrsZ0iF3dQ1-xJk3RN91KHNni7ieW81UcPwWIMEuZ2jjjO8Z6YRK7WuEDgYwH8I0J1yJQDLS-rGnmVkqcB9DpYX2HwgtmWJYKU1uox_WUxEql7PjSgdU7tLkpRYcLDsx7XVU5sEhABr79LhQOkh7ViMl1YOsFLk1zRHEich883bZ9O-2hTWSIWNZ5ogn2dQTvHCv2qz8H_6roG0BzYc2pLTiK1tPyb0It8UMnOE1IwvpI5KRrgh1pb2GihkE2_DUXYAcNc58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1kW70LDJovjH6rCqGInb2MFCOJYRu6-YPYH3BRsmpJOQN2219QSXYPqqS4JfmeaWqsrQSz8uD7BVtQniUYa5Ws6i5swLo4L_MS9-4TYJd4Rob2AGrl-nkfFFccwf64WUGPoeyo8xkgxC1Z2YTVD_sO_D8MQEwcefBlSILUZU-cNE5BhPBNDShuU2k9UH8ZqtZECr4sctms7Pq558MmbTbjT1vckFRsc-_4vrYdfTdyaYndLYBoPuZYs38GSgcZ23GFWeXLWRg_sN0dp9fSxDZjLnlUVxQKiBQePaj4JNpcLxALfNOVtDbK1hK6Ui2XKYMZH_3IiJjBd3gJj7FOMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9n_9Vgdze6ylnaLAerNJM4jCCnZHhASafXrfPywoVdcDsjMPWMaUCIV0pjluRMI7N9HZDmC0mLZot8W_u-0t4jRe2jBPm4P_v84t2KWaKrIeOTIEDRJ5SjqF2SnXbbRbezgV_PHcP6Djc1HTyrpv_rNBcHjoAejVcaibOBTUvYpWWtd573CByhKch9f715gUo9r5rKgsZuuJq7R4QL3HTDwgtrbuS81QMxLNzv1w2q3IP9GYpIXVTnd9cggA9vBHd0m9lJt_euvOqBbnLau6wUJHWonPEvp5_dEiwrdNUjkuFWSH4cMXg83pGnINOX2Pk035vzhsHOUdZFmUr8mmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exTrpSLmXdNV903COulIdVpZk7EUxcy_LGS5lsMQwGvTgc8ghkS3P_HRxCbee0M5zxBHimqussgameVjKfEQHNsOfZ7RY6AV7G9EvUezEzOOBbnJjLvO4XBd1ZLngrdV9wTglbDBHtFrTdXkka_oEykqjYijg5k1zeW81OJm8IqkRgs8B9wU7J_J0uKFmagoIkzSxw9JKhJ01XqbXfHD-Gl4Zr9F54fxwCylrmOx1TqZOScyAfuoWwvVveuoVCMP_DzOSW0j8zJ4c6Zrob_CkpM7fdN-kSE15oivJYolTyWhqWCKCOT9Dnh5NVuSTzIZYAK7GU4DMgah26fFVYU4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DWS05qPbxZoDKtdqPDG-8nmHuX1ZCHhEK-Xgm4_4k92e6bAX-kPtUZvixz9R7Zm-DG_YQpyABByHF_nBlYFuB8aCgC0TbF_ykgWBF1ZPEmVXGkVf8S_Xfjb_4sMCe-E9eY8MjFuK5NizGieBNdwS_sedjEZ9mge-TGR_FCXW2vXN7P3GTqbeLFn-9g1R-8FjYgbrTnXS-hEYJM70m4OsRSDnWOjnrodV65wKfpKb0enPizXsltlEuuoFbzzfZ2pYJm2GrxEr32OSs5gko8BnnfpIP-skLrccdB0WTIVfHZfKsIeoosFHhnWd1rGix78O8O37XR6DobOjMKpI33qP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CXdX18h7x1vyb3qAfOvQB1xtlilYeQVtsgXlpOsFBl8sZhReGRYezFHoA-90FpZxlorz6-0brHnJGwBEmjsOSPwp8VMY-w00fL_7WXLVtiYBenH7UXmD_I7Z92WKheahBH-BBvggHYZ6ul0YJGvFJDYC7xjraU3ZKS8bNjfmx9pEqo-Vnm4cQCjX6Phv4d3NPz2vNmpQiNDQXM2JeVnBCiuBbQzKNyYw0gxD3h4JsB2OUazLaDcfkHT-KBDowpOoDQ4gDWII_Nh1xd_4ndpGUJwIpFg287pKGP_V4BlFRoUet9xnOZlylCWQhCqyaADpQgDXsu5DYCPIQ9_U-t4x5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jfnem1ZDhKUeQARGdUFqhPKTzXyDDHfhCP6e06POhdn0OLHp6QVpqq94JXrfSmitwrrVZXX8hSfJGW-dK7ePWotLJtZUt2vOaY-GnKm06l68tzawiwqErrWKt4epSQw6qWx06thQ2-p2DFbiwEt5CtSzbSrE68sZrAF5Wi3AMbNwJ8rIksNpfC7xU1Pn-ZHKJo4FdMzgnmDAwb7ovz05RoYKRv6hYLHkhFNBn6nFFceelhKHI6_7QXbh7T60_y5ryf8fuVIhKpJku-zWGYQJ02CkqwP_5u86bs1KRiovdNHID7g1hcdK3ihUSqM7PH4vVNgVJ3-9TQZ_5oHTV6sbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=nbR9_E9UtGEUbFLQcui-49ZJ1_Nws60wh5kS7_hSEXEIPdq_QKeXgujdxDLlvq_9BMMAcNv6J1JKYwCcUqgKhJP48UPfip9bJroxE1uxXKi9lEEgon1YdQcv0SJ4C1fTUSwT7xzvaMnQRGpTzvMzIUNnbtSucIwAAL2QxHVUM7Q6obCL6xHOw8BafCQG95NJdW_EETW1E8VDPUuxHff3g_dVzHlYBJBJvAzCEm-T_xp64nKayo0BKwn0ZdKpXVvIONQardG18F8b4WenMFX-doSTUYo2zniQczxc-_UHSqKibI4Ksyny5wN7Xlal0LBngu3BDi37w50aZE6he4hT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=nbR9_E9UtGEUbFLQcui-49ZJ1_Nws60wh5kS7_hSEXEIPdq_QKeXgujdxDLlvq_9BMMAcNv6J1JKYwCcUqgKhJP48UPfip9bJroxE1uxXKi9lEEgon1YdQcv0SJ4C1fTUSwT7xzvaMnQRGpTzvMzIUNnbtSucIwAAL2QxHVUM7Q6obCL6xHOw8BafCQG95NJdW_EETW1E8VDPUuxHff3g_dVzHlYBJBJvAzCEm-T_xp64nKayo0BKwn0ZdKpXVvIONQardG18F8b4WenMFX-doSTUYo2zniQczxc-_UHSqKibI4Ksyny5wN7Xlal0LBngu3BDi37w50aZE6he4hT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=jpLCS4W8UljQG64UDfLb1cyZsvq_OBKq1y4K9Qn_5-g2DiZ5eFC9z0MnHLT2NkJlLIzc-ZCvPDeBVAUg4IETAnoPW5yooviSmzDk9Ler82Ok-4aF2hAwUGmpiM2I9T9G0gCuCOglAEXRxytdCv_daCMIAp6M19NgSsQk-GopyGquRFPHOqeA1gVbdOMu5eKy2Jzhxn0q9H9n_gk7i7pDOozoZe1rotEyfc5Fr-aHr-Z4mr_0rpHKfXKijyU1vE49-rLBCk2gilIqZGLyO_qtQI2vnmIhyN5Sc_70b8Q28p54cSqRMntmaRQ89SvN1BQK0nS07yDtXCYdEfdcjL94GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=jpLCS4W8UljQG64UDfLb1cyZsvq_OBKq1y4K9Qn_5-g2DiZ5eFC9z0MnHLT2NkJlLIzc-ZCvPDeBVAUg4IETAnoPW5yooviSmzDk9Ler82Ok-4aF2hAwUGmpiM2I9T9G0gCuCOglAEXRxytdCv_daCMIAp6M19NgSsQk-GopyGquRFPHOqeA1gVbdOMu5eKy2Jzhxn0q9H9n_gk7i7pDOozoZe1rotEyfc5Fr-aHr-Z4mr_0rpHKfXKijyU1vE49-rLBCk2gilIqZGLyO_qtQI2vnmIhyN5Sc_70b8Q28p54cSqRMntmaRQ89SvN1BQK0nS07yDtXCYdEfdcjL94GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBePeCznqBGfVXVhXRQCupqmFO9rf0a_pfcFTxJjx4SD8zLiKiWcD0de9fdEMqaMXpmFWF73qem-F0AANpeWhkI9P7oz5LmJbGChFlEsb1PG2HcSQjFAuJ8yB3J6k17Vs7mqjDPZYVBGkzSJLCn6jEu1v0TG7WOX2yIHLvIZOA-CuZ-Z_90tdltPNO4YS4vpY9-vT8Ftr3BfeReMq8eaPyMx3BZSBxPjxHHRsfkN48XsL6yKPG1GFohjKAXSdM_1jSAsuDX_izSoCbZgspkqsyOBYBuR-5ailCtWuCxQE596djTTRHM8Dm6c0AnVki3MSrs-ETP3OQci4CiA1oPmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U6GAJGNNvk_ncgDIa9OjgNfn-u-pRTCjqGILZlMAn05BPslhKuXGB4pX5qXflmz8VEoGnTcigNVvdy7oEUZn9YYL6_TsPF2K05q6bDZvLm_RPBCnBAgHwM1L_nuJDpJ89a5bkE8HlpbV27ZMSJgBtay6We4kIc1kIGxGtQRFWydHe4gO8FAld84Ar1v3028GRuut8UTWvLtod_QvtwyBBKIZwyAZZkxBFCFG_DUWwFKVU3011UCUW1tjfczNbMlwz5vmSM3M14_URl3g9GpLkjx-rJ0FhUO4tg0azSZe1ihW1BjF4-HhX0TLn_5ELSaY82YwZSeJ6HysnkpvCypmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ht6vMFS2Q2uiiwGPfVA_KcaxaGiXuZOOGbWAJL6sjQSFQmJFp5_pMBRAQFprudpo0qSk-GRxj4yqPks5V8VD-d9G1joVn8hJG1N2241LJhDev_AEJxL18a5hFrnJWTmHgb8wWfJH98wWdNoxtcyDkTYXMy4L_KQUtqd2oGRG9xqL_-glDiOIvzdVwioHoFdmDV5xjYlhf-HHcAaPexqbKSD53pHJP1ePXLrkYq3P9b_wCH9WK1DGlF4qqx8ipn7OaKHBQHUX7QnpeIgm0zZ1JMLyoJeGz6LNE2Vy-Lti3RbBKISjocF3wvxs0807U-ZyOv-av4xO79kB1LGroOBI7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuOvcvQt5mqcJ31NZdBEMThZW2KGPr69UaVT_DzASyLUuJk-2QxeuPV4Y_E-UG9bW0oywqmkv97cxmHe54P-LY_WfSk6LqPg-DxpdFYlzC4MGnb6Ypi7XwbVB8bfmOIaL_N308MOWPJ6d9PLYo_A_9GEysiMVnQ_gqOE7UfJPeTEBS4ToS5Q98eGt2lUzKUaOox1n7RXUVe5HZCcnXXQ9m9RdcaQfsEWHkKnfNHDh33U9FZZcU2LngMql8QFdp_TXzQbBMAPuLiuSpRyNlZC_zvpkP8yWdkL2yqLfs8Lo5cRUr12HPgohiuscB-eaR1CVfZ0UFCSOrPBoWo_1k8f_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A9Om9G_qWplxOBMiTyI_8Nv-01UUA6TYe9m7vckaIp5ZDfrHLMxGMNHjFIvO7vcaHvt683jbhVobiY4bTHZdGdDbopD21Tt5vgGKN8G7ghsKIYJOW8sJXX1VT4VsokZTFWC55y24rxiztUhnUU_AuI6rlySIGKi2xM5V9nzjbrlyWKNBJFqLpbAFldPIGFvtQkxtAi9iPEAsVoCH4tL8FdgkXBnOzuhKLiv88aAVcpzAMAoNwfdCk81Rk30srSuI8QDv3CayUn_zbcsYzaeBdgcUl4glnQXZUKnGFIg4pdKzfoXYkum8LGHDTPJ_bWAEwvDJGIcPWSOHjAMsdGBTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gBy5GY00zKSqkdubhe3NnfNiDthWtpB_3-hvaqXSvP0EKDeEL1B2zYmoVQuVe_ee0_hPbWvYkYXAVPiDMdXPp389_EPu_06Xvy1OctRUXbtU1gmgY84USLEe8T-9dn4d2fKorMW4wtuqayvxhKSF7gbIBa_6Q9980HXHURsri_10s_DaMnGsmP7KcWJpGABSw52YKIeQROZ6t3zVFN3my_HNy1yEQ8ES6egK_LPu5Qh6gnLdhreiozcjChyGxfFoGCAdi71xUFlunlwxdxIWI5Gp95q8ryFtk3B4xwZayLcesQDH5WeoWwxB0Py8h1ulRNrW6CU2kjxyjftafI7-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PF8D_CW8sIJJibC2mllAXxeEhUAvOaCXCRESrgNS99D_9czMzp8IEUKAr_-69kfbUMaJEaOvM7pS4Z-WFeG6h44aSulHnSOTDSmT3fjYCpK6ZAm3b6IxxQbtvCZ-7ikgvXjR9JCESSfLjQ-cJ86MLLoLsXqR7sbcIzXDhN87J2UDYEqwKOMjC3kIxnBJZYf3u3xvJivcyd5tKykLA64Iotk-HcoXDxksgCpL2usPo0opKj_cdKI4Ooz2lP80h-ifVK4EONcnWO7JhQkBbdWC6IMBZS2ygClsrPTRFgTDsQsC15nWjhQQbJlRerg6IPCkBRnrEMYIGkqPCnERBwy0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dC3dkwLgUifg1KP_OU1slJTjts20BZy2hs4bvfms0y5L83nkRQA1qaCc7qPMAHYij8DdCshj6Wv4VDn2v0Difl6e9Jzs2SbqpHaYvnppuUddpIfEeznCQ_33e37sbe4RHH3qF9NFy14H-4FBYJUB9N6iLPrmh3_2P8naiPepnffqdwVT0PnlWtIuWgYMDaPjp9q8suRcyOnm81rne-n3W8fowjPtW5sKUjgSdUOcUiWy6Nw-g3_kcn9xchz5NBQUz6OQPT1NpjpSu0q7qdMdZhpJp_C4kajTSVyY4rCI3XhBQ0zLjDMiysnpAhCEdul6XZAHrmZF8lgTT47pnIT_EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtNeATHxWHkJ2dimJpmbsQUwUPC7ts9Siqx87H-kVj1ZJkxU--mS60_e_ClsOwDwZgCp_olI-KL2VgCK7mXBht-KJC0v6BxAJqlB5_Eo_WifOvlC9OQin1VZGcg80qkjXVDIlnKnmh1cqzdIhe8Qi1USf4bamE0R0eGpmy0fJdtCeMyfutmV3ieP6nkKXlrAcI2EgO6GNIYmc29R2xfi_DjZtYVvkx0GhGAUd-ed4AxglSJ0M4FLIxnJBwc8UNVTf0Al2NYrt-fNVSivtcZsSRiQ3GCnZb4Us_qrQYRwWhoHRiSt5mW6cMjai_nvdTuPRbQq1kt-ScEUhTg7An8mBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCK8qgPiXwKFqnsoiDsZYpZPAB1HGvKWZABxj9MTplE04HmBS9Y9M1kkKZ7hKLIc2UF84Hrz5RdLGDBSk0CxuNmJ1lpZoNmD9D9SsCOIyZbFsH8pmuOXuGWxm6rdfp9R1pj7xybSpfFVXTsIuL9ChqELDvzopKwpmIJsIEe6iRGmbDagPYtscRV331TUTCDeIY5wzbN7Z1UvsZW31CJR3YoSWTOGYbbhxLthFalQyz-eoVOF99v7fR2_kiPAAe8QobVk74OxQwM0B4JM8RlnPHxxJnsXR2drRey45cawysoVdg67XztM5TRQrrfuyKuZupDDKH_62fewuFtFwoPWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L5Bd79zSidRiipL8iZ48YKyT-rnb7_uVxM5w6yGE0v1iVQCdmKnpqN87XazoalUNP0DK128D0-C1tMnJqCHb6Yj_dg6fSeSBT3r9YmJnm8GDLRoKwC95eD_4SzOIbagHXeUCkKjQhbiBt8f6OOkqNXZZReuOllcuHT308GqHiaHxpjoo-jp1ng_OHDGABxjg-ukmYvaW1JGt_9aan5LrlOdOy1rzIhp6_9qazkbrrE1ma3-VRiG6l0E8FykeVQFmYoqe4Z0y_mJ5HGi_AifXxSrfcZHwUIqAatO8n3QMR2p2WV0bTQk8mOQE9uXnINcIikCcIaEPVGxwce4gKG6KNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5n0elsg5gMJODjhnI9ja5IHF-HhYXPbVxLmYsBbdXXMpH95-msuwRMyxY6DdBBubSkXmvDNdhENlOm79lPP_NbVdDZnUmSPZLGDfPVLdfFh-DllFEnXKufomBpnwO2VmR2lh3E8uOZoNtBzjWNLDd69Ld8zLvawtU4MLL0CR3LFvh_NTjZu8WbMdolZ2Twm_uJ0FPoRTygo12Kq2pW_d7xJeIWaSQk-4hq7kjz0Z9-h825rEeBeZczR_T3curyM_X4hCginWu9C5rgYh8HFXQk_BtN1jU6LNBeuGdfmzYK9pK558PGK4HVBtz1yGr1Y1PU27lJGVmtOfZ2CrDwdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6NXYr-NhVzqPqiIyuJ3v6QxIDhMFC36o1ibrWayI1aqsErcWnRwnDqp8Z5wiY7IEGl5AMnthw0pCq4jp9mlME8Oj5U6Ef3QyxX2R8GMGMuTiUX6c7t12gA7CXFMJgZaqzO6_vFqeiFUEMp_uAU3e78V5lpNg2I8tkvpc86KNUBgl33XNp3lZUX_XAvL1r2MzdEMI87I02qrtJniUtuKEWu4vhNAlTiTZt7tdEBC1w00568hfLjHSulo5FC3o7R9l1f2QFXsBSXb9C560D2W3UdrEk1-BPGUp3jS0ytSLjGd--SqPxMW4pRa-SPy2IpdYgdceFf8ldanUAND9tlcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dj1AuKrr4QdxsPwY8JDDPQyWwgi4wYuKvBwOR8XmZeWO4HzYxnk6PjUlAAF-nTUHQCGplaWIRPdZhEv-NIFa_gdl01l1pPEiQKc5kfQHCF6NQWx4qlEVfKRbDjQ4-20hZo5GrQfNqemnClWAiEeEjyNl__SjaBNIlK9scB5kN5VyoPDQDOeAgri2aryT6dMDRlhY5t7WEQa2gBEQSH_O_HH2zwBWHq7ZA9SYVPETwl3bekaI5yFog6PuaZscZSpPOCLNW_EQyMvaXn2630k0w-cdb0D-y9fUYmlYCRdXLTZDScNDf00C9nt-rAQMvOuNlLgl_v_2yFqxRidBWX74Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XPk2DFfsNGju5gti2B9c3yqzcaiLdTenJWrEVGxVRSQVJhKJCWRl8ZF5IsbX_u1ir6EeBU_qPEpTX1oMm9hLko5ieEkyCF8zgQxkl-A8usBSn9asHZvB3Hfx9JkqedxyAfNx0fr8PXuzcxkeVJDKyLJ1mJkKW0CxoIS2cST_bOI98-Yq7N8gYqQv_o7IdCWt6TdkOqI2j-FumEIlbK3dMSvB6iK9iE1RWu7zVA_JSp6XOwswBdWRDNlC0VUYYGWtig8S3yO1omdf7_3vl-VUqKdgLA-XH-mGRoj4a-BIKZjdS9qmEsUjCpjGqWT8fkI_iZKKKGXYlLCMAPb75Hwlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kZxKB89JZQ_rA-SpY1RrIkP7mtOKQ4UwnLkwFU1tOHwJfU_lvb0jp9fuWs-wCS70yEKviUCCmqMmHOz8_n4WmYGwWwtv04vQXHQqmXnz9h1ez3Dk3-vour3wo0zGxGPsbwEbKkLununtaNO1K0XaRTnOp5SG7Pa56dgdOGoPmGssu0qRBbLx0d7VcgQ86svACpoBioi61kZzoUzXtn7F1xEKLzslXtRYw-r1BPhF3bc2BniuJboc8OsLysD5_ifmal_EHfME44Nx7cBKWA0EpdRG9f5UDV6uP8Z_uJ3mKj9j0X3FctUZrIqG3B9Fx7VMzKdngcpAeSHpwtgqmvDC3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TTUmoLxYCJnRELhq9guoCaklzEhRcfiW4cEGcKqSPd1K_6nxmy84K2OO9ifA-Y1arXD2cyFPRjP8LExKO7RoN3TQXIk8A2x2HI9vUsUKBK0AKUBXCMi-HOVkY5UZFSi-kBkm0c38-8gwmnAx9Ui-qJZGrb80hIOAeLX4irwVDCbioOPY-OfkdW4w8w-O5TBodplsDiGxWvTtVSEW3pz3OPjOpiMjph0Wsya_qHvuuJiZ5x0JBmKmRka0mjuWd6CvNc8CSmf1-wdDS0rp-IJ-twgJii-3RgO783kgpBw2RwCgUwzG_2j6-VHkz53bUAe1SCfCN66jc3f85CfsDFvL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MBHeTcC1yi2khULa6-mdPMs2znvtSGlcHPn-JEesP7fxfRJvtCCc1VKndFDd7PiQUym3pQ_GmQHsreN1pv9tuzLe40HPs1-LFQib-tRShynlFPvN1NuGawBHVHzoRqnT6WsbMdP7HQbQp08YnRK6aGW_SUSmd6LWGD9kObAZzyOLI30ZNxWRvvGHsD3MnUd2vj1pSmw56lS63BzCh-t3zlKqsHCt_hhRCTixLwNEtS58fY5lXeuDmaP8pvjVI3XaAO1MVLmKWu8fAP_KHhluF1zu3wjMG-xwbpwPdms9xTDxgPFK1hnDWkidKDHPz0gsuC0M0TuhlxwVRogvWOUuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CM11zxdaNM1cVFZLa0woHp2qKC23RQtx8_jHywukpucgVGqD_M1Zg-FvO-18qaJYm7v1XS5qwFj96wx5mNR3xTjfk-EBjgrp_oeW5y4skyX9T8XdB0FlI01OrJp-Wg_mleoO5mT2th08VsZsYRX_2Wh4nTV7FqpGA8lc--Y38kKsNi1iEzxx0BSWpj0ZTS8UFW1kz7wPfHVRWvcrjC_llDWm8O1uRS_rRdaPw0aRmaJDGVbMXgC7c2JKFEFdKqk8wQM3oznLB9yDkNXacHeREqtZIAC48UMYmVge9apUVPcEEfTNwIMpPg5fQi0WtXD_PNjwyR-raHbmJXXHHJy25Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhbLGYDeJGOJ2DKk1a2OT_lJV8fgR7hLgacVXQb2fIBFZwtKLigNnOtOJjJL0S0Nx9DoGjIyFebdRzcP0U97uwA6dldUdiKQKxdVm98bTjJSc2gUTGjJkqu0FdnnGAffgCyX3Fq7zXFRSlXtZoMU84ZvVeHZSBIsALeE-iixK-dc7jmJFim2J36MdztNBN7JWCnbMaxCiIfVqZ7I7LkMhVh10Us2SYPbvl2hwf8-PyzkwoxyrLHkw0qvwurycpyoTGuBTJKk_UAtpjpYo-QESKUKIs6mb99iv_AleHK27KhWKSTPA84fXOKx4pUT0VZ6o9VeiFFUSCgJm-RHhE59ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvyY5LE9mQI3FRD1Xg3q3Crx0-3SUg4nKfCRaQoDtgWvg7ha8aLYmyrDbmjsDig2ppYHD3asAQZFNYpu_7JLsPB9jO1buEgemsWv4HHVgEmsljwQzIv-E6WJgHimPXpMZ5Zaq7_C025sRH9wip2-3dY8TvO7JRhDdfpNkjbSy44uijicpCOcVXk_9kE03cbd5Uax2U79I358e0bPoSK0LyhyAM9qeep8p05OL6gUOmwWJWwtl3-fpPFkA6JXtAX0Dyeuvt4Juy3rXzbeAZORG-3x4KvxQ_54g9bR0EmjdpaKTPmQ27l4z7GvLvylFCW95IjC77VxoNYZhHhX3xOa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S731bmVf0SI56M1MlrdqHGonB55AKObxlcsPHxqCPTDOXop4vaYW7x05l2DFTStR0-SWk8crGfwL1vX6AIlTdvaI33wewa8qIIi6rzH1KuCMOVJIDs3reE4d4kWDG_HDFeBsKHgb2GnMwApka8TU-hS5xmNaZTU8V0xsFJ5Vqa5fkgr3RwDUrNFwXv7yxG2UlRLb1bZ_VRtGvMwa0goXMauAIOUruzMiawhXk38dYjTBSL0yK0hdRjrmykOZd0v-zBk_b9lDPPoREkI0Wx4Ui5q7rDGyvp-UFVT-gYcfofJ7l56qSKKkRI9FalzUZwng1Ngz5s98gmto_z-nb7K5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=OnCsuN8I3kUsiLPCbeomwPt9wY-AbCzomdt9_VRjCcpUlcLCi78_GCGAgHdZayNAsNT8jnS3SDj1GBQSie5RUlygCEqOk0qINkIwEcEnSv6roPus55cgbbUElHVdT7Ow5m9W4SpppY-MMGalmhhBslMiTp50Z8OvEyKOcCm3Xm323A7QyhDFyqBHUCfgX1r51dkoheh3Eb-2kbG2TO9re4iFa06ms1p31vOyjDxvjQmv-c6wqpzuVpeJeUrFzwXqi0DliuNuzGtMXI1ae7Ztorui3-tGi_rLjgPZh4FsFhS2XM8Cuexgd6zCoI7QX9Blp7zCzTG1lTAr0pKjiteX-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=OnCsuN8I3kUsiLPCbeomwPt9wY-AbCzomdt9_VRjCcpUlcLCi78_GCGAgHdZayNAsNT8jnS3SDj1GBQSie5RUlygCEqOk0qINkIwEcEnSv6roPus55cgbbUElHVdT7Ow5m9W4SpppY-MMGalmhhBslMiTp50Z8OvEyKOcCm3Xm323A7QyhDFyqBHUCfgX1r51dkoheh3Eb-2kbG2TO9re4iFa06ms1p31vOyjDxvjQmv-c6wqpzuVpeJeUrFzwXqi0DliuNuzGtMXI1ae7Ztorui3-tGi_rLjgPZh4FsFhS2XM8Cuexgd6zCoI7QX9Blp7zCzTG1lTAr0pKjiteX-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yq9ubJO0ZXiGqXd9rE5mvFkGqSYNd7btiFbIDaO-CwQDQNFY1zT3RBR_qVR6YwKqxpJ2RLuO0tCrsH1iFNF3suOvUNgoAW3r9aqofwSIuQgOUeRhEBnuwu9B78SmQC7tdY-M_rVjKYOmrPXCz-I_cf3HtXZnaBxdEDMOJOPhnP7VE7Vj-Kz_abmyMlgIzc4JauTEwbnk-eib7zDPG8lHSZRhhpjaThJ7k_fHH6tcKPsLE-R9Cc7oFhlX4tk8v1KpUoyj0J4SFjKIutDQKQJXP2Ad0TegZRf3Lq6BWzkejFGkom4Ic4l4eJi4WUgskFRpKWoffcoyHJ4V5XHagw8DEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWZnlSaz1rNZkawr4Mtq6b8HJykUe7LsiE7j9YhnXuo2NPllwZh2A9lOAnKKt-NvcTrNYy_J96iR0cJMq3yR05TG9IFe6Xdyjt1_aRDa3AbA4rwJXMTbFE3Y2UhtMRxiB6TdZDAlGCKfhhTFok5kA8iK0610G2IfNyoq__HR03-fc-6xjmqtHa1nPfZz1WOjKAE5VONS6llZQElgEhx8w3mSgOT46t01ltCxpGg6WszWssc9SyPlZbWUeyN7KJfLNyiGMDNO0OQMUzsQeUGNIyLOF8vEf4UHK7zW_4vfh37r2Y065EMgEQAVbWvCN29MyQSERBhrZgScFmO6lIut8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkA-5XMgTzOZonyvrHFICxTLsrNuQ6QKTpM2QX4MQZgTtPn0Kbgn0_BHR32zLQJB_yXFKWU0YcpujQUSiLrWYIItEaWuE_AgT9QCKH1oksJMc88cE5bBFXm82JnPMW_6-RiJyQ62C5hKdZ84QdwFvfSuB7DWnPQWjAU9xdPR1Lfg-Jc32dCaoU9Uk2JIJKYS9s41qyLQ6BBH3PNQz0ErKy9MZ-XUNb8_7FHGsFWjx4dQkAk1DIyb9nMN53e96-yK3uF4L_0DI-iJpFX17KXePOLzp-x5A4Boyq-3giDcqGASR_QdUIga3bXpo4gQRIUySJakLe4SnCVo56UC1qclMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kaRbfDQyBFZTg47fbWFM-cZSR_3B944-EsFzlV65JTQPI4rKK01i_iQ8mi3YdjMBOnqNmEAK_sf1TzXcABPu5lUKAZVqY2cE_FmLxBjFYaHbO2YJleuemwKEmHVliHf4BzxbQLhVdU8fb7WpEKNsleiUc5coMeOITJxLW5TguiNX1pfUstzUBxlF5KNNz30bbhtxg0MYOWaB1Zvo8pOy19fM0AaIizMVo31BcSKOizcIkup_Enh6kTGay_vfOr250qCKG3oda_N8zd_MYVVpahtqiXPR_EGPUA942LoAHp8E8CESDzmKidsVg9_C1Vy9nnCAmdlyDVFVi29gpQnaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NRiRYAu_YYYK50En4HKycvsqr43BnRhDlS-vjA_4ThCRyGd5dJW35TJ2EmTEanQd_Joiii6f5EreaDuL89q3wdc1DBnF70WDXH17RAHLmdkDifWvoiwEoFuQbUI1dhz-ftCowgCaBZDbs3IwAyudNBylEbNgO_7UGWl3KCRLCTzsChaiox52XfBhHs_8MWfBBbdpHVsMIR7X4_M1myqavVd2OjalUlarYssogoBFkAdEsvr4xTNMTMKC6lIB9PYVUZPpIrsoxIMD6VvpuvjxKPFWTX8LF7mWokcoBB9JZRdQSOaersHLvf2hmjjjIupoJnML9oe1tP5004oapWiC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oDsVesS5ThNA3lo1o1bhZ3vYe0UmeFJ6YoDinSVUzm-mGTVSR2NXBaJVHREc0Ftq3l4bBvYAZlV0ZimSfIYk9Cud_ZY-6ptElmP7_UFFLAD-iW5mabab7zPKQIbJXzqVzT0BIvUGvmxch1ypTR-vfnv75kwciBrrD6xoP1JjzcmFQ6Ode4zTS5NcNHARqG8KwjAqfPXRF7vEn8hT8w-5Pd9Z06lYG-almWIeN4xcWWYvDuS1ULRk4dFt7qAIWb3jJvOLeh9pt6zCc7JtOwqjFj_hbEaGpuX_IdyTL5z2huyYGdSfTBwSGfdjGhbeNdgup58E4UdtMeTD2wvVAn4okg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nCWF9xgIQHg0Ehcw8JBc4k08W2TtWCUChJqf_O87GogWuY44TF_E5akXhFYYYtQ8Qu74vokwfZtzJw30CXqgn-XHM19pS6yEHg7uu2_wxy6DqfxuJ7bBHfsgZ1Jm6O8bHPH7r968auMXNI94erV1SP3xcAzbHVqwA14KJot0bv3mSJeLcgpflG5A1xO1_eg7SmSaBnWn3VleYdFjYHKybhcQyEdBytfPWlS2NaqhISgdGwq5507pZnQXoa_3xu5Yh73vknsTuoyzVI18b0RCcNTHGZH0dda1idSdQGuyR5Rf59kblF_f_2AFhHT9f7AWUnMRE2lD4AWZDq80_-g2Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bt4JpILIIKcQMFBJ_-A6_FeuNCWNqL128WUp2mgz4pBeQBwUaobIIaUmF-HcCDJHF55scYs9Gzb1lh0-fii8JSDSmzkkEhjeRA0O7YpafNJ6sVTLnWAb5kVpXE1Kue9VZUH9fsBHBXN-rXHXsy46ZSHDZQigHtz8JnHzaV_iBS7cddp9QW4Y-M9lpZJFES9jurvK4Ogf9pDXQDUSFNV073LKr0dK8x7RyrFmCaQbeAUeZjlSp1csh0Iqzw7zSnkz2ugVEmB1Ng8FoX8SYLy6m660U_Ruvi-nA8Jdd7g5VCfQtpaNl7L7VVJSLbLtCONX3LjtYEIPUFJQqHjujzGnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lYmiB6U3bAmdlI5ViVfZt2HXPLD31cLcVZbkkTqAwNUuvME_oVJwzHchLTvShXvA4mhmFTXQq_yhoPyCFmaJKPhyZax7cBdkgmM9PDlHu2rkaqlT23saEnQZ3NjaBd34ZWPR2sPjOAZdmW7TAl1C_4A1uOjjbcsgiILcuX5DWwigrFkQUfXrQ5bVzRN3xJuOIP_58d5HQ4jyLa-QEawz9PPATXc9LHVzW_H9q-OYPeMWhGSqBvERk28xNVtz3fpeRnZDkBrg7gQo11cKGb8IN8DRzYnk6laqIfZCSS-8giSnMtuaYgpm87CB1oVF4GNgaTYXxRmuCGR3qZXL9PkDbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4xBgdyNvnqSal7e4RHCQQ8NBNhy6NgyWn0EeV6j9iGaLjixmBu1V5ocdrYb8ILwdTkX4NZfPhHro6ekUfYa2r5bvruPmI_eq9Gnin1gJCCBHJPn5TCCWXXrITnSh4BmLvoPRQ3XO7dxRap-LHVMspZKAPhuZC7ItYGLZhzwC-Zceah3ATQ5y9603m3ARJt_kcAcWzNGA6J9tvnGlqClcCN4gtI9JCaKKyjXbEraRiRkZtTB75MJADbU4vv985ZaD2fC_o1qQOIxeGSjDaGjL5fs0gQE-L5z5CgNKJ4zItK1oOC_uBPox4eeYbSYglUFFL9NYKNqkB6esoVNWA8U6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7i065ujtX3Z1uwM-iceG4dixc64LLL-Da-E3tlzbB61RwEAA6FnGcnfLbLOG_t8sSjZg5flHNz5ky0y9gRTUQIj2tkNwaehNRuxPa4CwpqcVYTh7nB6UjCAe8vWshkB1oE6MbPbfxyWD54T1y7gbj46sapxIxlvzkw0f1hYVmwGvgBe_mn2Pzf_3aLkI_jIGhqb1upErHe-1mmSTzDCucgfHXZll6_ABMe0a6jxjCgt7So90Wdwc-yNb1pFXe4Wt-fagLby19eX7-SX9TJMJqXJcQHbpZ1ccP8_x3YVadf0m8UlRjWeUK2Au7Xb__-VDRdRWKyLsHaBe2an3a0NEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGlm4Ij2aC2EOWoTOHWWH67DWg84ocxzm5WBNRjx2p9NOIsx-yJEsiGu7N8_U9_TCylh8BK6eQQnTxfC4-vo8SLcnhp-PcG40fc335ozRT_yKiSeC4u7MQQJWAbBEYG2CI2xQyFtAB6a_FjfomaxKMWVryByzXOa2lIliMsERz_q9Joo5Ofq4uSz6bYlVdlLfVF-Sk1YrHsKJv8HG4s1zCuGXwcpsvajRCimipsGqyoe90Mye0Egv8tFfvwEz0FUdD3gZd4KGomzl_-0ejYIpe_eaOBTPqKC2Xdda-A6lWFGcyZgOCaYy0F7f6Y-ULMMP0_gd5JEevwvv9PT8Tg6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uo5bFck2dqspamGy1IPop0baeaJR_zjomnHquPmNhBZjXBfvX8WWMUZS1VT0YWa2RGh6LmLoiF1isfrm02-i9TS0kSqf3jCjcTNYq2JmYknZkchWtc6j_eTMz20H6KnbA0XA9_m7ZtR3-EqCMFNL5yG-kUoHuUdm8X4TAGVd_gzZ1cEuWNp0AfP7yrXjtLptqLDUUY3kcJ0a3gQ1NJCrWhJEXwn2PZeSP-lkw7jQhXPHb5XjabgpdSnXF7eschV2QeFR5WFXz36YOkP1imACf7TgaJTESColK2q_S9YpKREliv8BET867FAj_3tJH5pRmb8p6gSFd_PmcJpDtJTp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdah92c4an9ueBbZqoKz_eFEusX_usE61maTqf8a8FjI8U7zOWSYTGmanUvJ6GrBkUysDTn0ryWFM54BlQrIT_dYWZ50j_UMgfacHozVNsdpE0h1jISvSN8UaxLbTdqgiS8rvhvzSlf-Zn6Da8mwWa4hsmkCusdAsgATB1HpPNa8Kpwe6Q0NVqB0y-BMl1u_jcwHyTsvN8NlXasuu0CunVaoaUGRvoElxUrflsda_q9_gLN2_sJzWuTkqwkKg1l97LBCJ0Kc4v7VZ6QO4z5B951u0rN3rqYH63JwuX8dEiqrm4VJukhb1fDO0mpqmVc22QXYTN05zJHCg86RPGCwhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rzVHvu4svoP6g9CcIvuFk9HD-kz-LYxUuMxGHFsZ8UIJxD879YDMK9FLZjDHluEHYOqcdSDJLENeJuAD8i_XSb9XHNz5jpPHXozDsMzprZ05iCQKa_dZQ4QJV7Vu6tAxs8lS3tY3n1jz7WM1EBsbmsklZhaeo4KIHRXLhRXkSYbJvjssq2Jib5etBPeUeX1anO-vJaIVhEHZspTTH6JzmeMT4bvIbcrKC5ETzjhz_GRhpnrLxt20em1eHjNkOmVWR7nmSlsW69UzHUGJ9mJ2kybiPlrC2XjkNza5FCK3vw9xg4SytYgbxWH3Jwk36NIx0RE3szOqpFYI-H2NMIY4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
