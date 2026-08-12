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
<img src="https://cdn1.telesco.pe/file/JSgLurnfwWgMTDsQgym1T6rFQ51Xq2d9h5TQ0vzrR9fWfjWFH6AHI_kiTVm6fg6Mp1MEx5VCmhnBR3xVl1YYAWyJOa4V3Vutyf37yHdwEA9a359ZUyrH4FjOPIkWKSgWImQtjQ7DBpIg_0RJtWT8Ysj7SSs_Qoey_S7yFbChCrzQ2vBl_gXWjVfmXDaL29glj5x8EkphNUtKFvpS5d1_zAcyQB01WjEjMwIHeAGsvGO69QrBvCza2pKpnlKCXXJcojMJK0pnyl9-Xm4AI1GmvKufMJfLISFCybU5YEMmUY4DFHlT0sK3XtrJQqmm-8oVwuvhLw19BKJaPyWiapqiZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 21:44:00</div>
<hr>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dW7s6DZDE2CoKJBEa_whCLdZ1NtTyikgz1Nrq9IhQoUdJDd4D_EsuA_6APbfpRjMbuXg5a68Ow4gaEyMyvrHKKHXC18DkZMC9yxnQXRyMr8-DqBSIkQ51111F3pZM6GK-bprjPcajbcDnnofjhpZ5Wn48T-HwmoMtUeBGMheX7w52gTF-1NbKy839FcghSwKOIRzp26IRhjnyG6JNzqkiOuXf-rUnw0zNW5htR8XJ4EMd2Fuw_zuvt9gM3XypbGpmCNLQR2NSiquiyz2YyWXioRW__H5WSQNe-HqMZ6TTaWzcCksS58UlksCtjC61dSc4mc8PYyUp9R7rHW_VAqcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gBXSIMzYhHkr1gB_i_k1Zuubt_4jriXwFPvHtNGwjaywAH4viCr80SWd48KjzX6zUb3bxn5HMDKyzj4GLlGHMJiOLbWS_fRReEf-kAFGwaC8A35wSaMKqSENVLKpEV4F8NLF5-yrmWmfIrwOcellkJaKjBO017R2-O5l9Ro6cB02DXNthHPihX2D8xzQpK6Wh4XfYll6NAuk_SECD_HXloVHlB6RKTJg8qd08BqWimmqQqyu5uBmT9pJSwM78A7SOEU2ro0cmQv2hUDKkUnNmPOhYrjmj0bt3as1Y-zMCORMD6S5MCa27zifjwLRxovkHoFv7dmQDcqSCj81TpTtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_K9LTp1dcTeoIpQ-1aJ8e5VIgMLTL7qJbXl_iVfoDtfiz4md1LV_fX661PwC_X9Rtzfod4iuvx2ZNJeoA9F_Paft5NIQgstEk-WnpS_yOC0WKbR3d64CIVok4wj6YvI9OQwIRFcNzbTif7KW6tPg-ZguUYb6kIG9Tb6tKb83vx45jtGWdA1GPrmkfJH5SOm6KI-6OUwPqj8ciMt4mdjoMnZQq6gOvzhkjqixgfR6NWk05YlScviW_P65rpgQlgz6Q69L9UX0xy4gJ4ebc-ZGRRNFK-ilCPjFjNvw774GgR0N9KYBvNth7PRI6YVdUZPtRbQrG9CRQqjN6kOnGWegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_VUsCmX1GJqfJbQzXHGPgHO3Saxa3XBus7Z8lnRwJsnSWRgwKOOSDdjcij_5lRfpcS0yILsA6giaTykH5DCaOMXYHF7XfLNPxfbKw-4GNIlV_dpi5IwhUhyOH4hOSsOBL-kUA3nWqBFJGC9OTWZTHjslX3qb6IxrjKq-2zTKjV23nWYM_kH5PYvmsqt_My0WeHGIwabHn17VoSQiwf0RW0Xi2pOhuH5e50F8zche-g_Gue8Uz2wmZTKFotFSj5IjmLd39Zt1QaVsl9vJQPg6C0Eq1yY_ahduVQcPC-ucKFG-EyUuf23gIVgTWoRXb1wj-ZmdWZQ7XAfS9jwCb0irA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgeCL_JZfY0_DSdV_55EItr5HVt7Kjm6BfQiOEgDdFXHprs-hGoPxfR5A6CRQpkhm2KrY_zvaPWbFtZgCvr5UM_mPE2QXczoJkGzlF_FraW1h3trWILhDOUd9uY5Jt_6-bkXPVAfKOZJliP08pkpP8uNnoc0s-yTr1CwApgNI7RjV1XyGo3m9qzi-QbZ0EnDzB2utC3eOmWxf1SiiCtZdosN8Yl3CsqBLcByn5KiZehB1EjuBzJ7b3m1vkvza2Pn66nVE_ybtAburbfRIZgJlLAZhPoC8QdGiqk8ZsMrdxKiz1WYJkgQoj4pNShmbkOBBTIqU_3xPoI6vWoUUOt29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KDGds_8snrca065PwGzTlEFhQi0iYauFFTQg8IZRT35RH_IEkZ264IqIg8xFEWRbK9nXSGadboPCiEHGse2Rw3nj2VYnCzeLdxhm6hrMNxXevChNb1NDF-qWy_r98ufbmhXk3-rPkBp6GzsaKD-dlGD6pL40ckm29TehN8S09QfYUtHloSBrJwecm8o8v7bJWNZcmSToUCdEZd1jhyxUsFfyYZFfVPPtC4PqzwRtN5_9R5uPbie8yYO-iYUTlm9GaFFa5icvK9WYGTikEuIi6Mcf1I0UMXBc3XceI7_QdqRVhKWxJXCGd267F8L6aP7Vf-3S8oYXMbwBOkulqB2IEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=Z_skDNsPJ8L9eOn3eAMiR-bAsy7kBFfDUznoREMvxo_0KGC28ua8h3kskHdFQ5HIT_HBN3dBT6lK_AKsVBC72z_YqCgW9doN8v7J3N6MH_YzJivbo8SgDdDdaexPoTW4idLPPotW6x72vvNwSm5TNpAY8brif-ySTV4eOFvXGmdPguwbhobs5pl3GeTTG2Het0OGlkvAIhzIKqE7vbvUX4ejJfYAO7CY-_EA3Qxk7ITi2egD2h6hGF-t5819HdSuXCfIKuQ2vC8KPexZzILXbqGrl0b5rNtVSv_mwsCxLWXBpaZe1gUH5hfPyYNhEKCFHppwH-Tg8NtZgBht-rf7tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=Z_skDNsPJ8L9eOn3eAMiR-bAsy7kBFfDUznoREMvxo_0KGC28ua8h3kskHdFQ5HIT_HBN3dBT6lK_AKsVBC72z_YqCgW9doN8v7J3N6MH_YzJivbo8SgDdDdaexPoTW4idLPPotW6x72vvNwSm5TNpAY8brif-ySTV4eOFvXGmdPguwbhobs5pl3GeTTG2Het0OGlkvAIhzIKqE7vbvUX4ejJfYAO7CY-_EA3Qxk7ITi2egD2h6hGF-t5819HdSuXCfIKuQ2vC8KPexZzILXbqGrl0b5rNtVSv_mwsCxLWXBpaZe1gUH5hfPyYNhEKCFHppwH-Tg8NtZgBht-rf7tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CkAilRQmwVyGHtFKhlY9oboLlK8E-7Z1kMzABkJQdHKP7bAr2eFsd59MtNn344iS8AxPKtM50BI8s5tSRJmaOHZPFk7UuQMq4-IYV3zjdhiXFpRPBJcBX_npk9OqLHCu_h04th1GfCvkGpS4tMaITXQwBtZLe230FLmv7YeXKFcPwzFivqa9C677Pse3eFfPmtG_1fIaRB5QK4_RUz3dPgDBXf-dL0HjX9QKVdA4m_ksX4WG3K4e-Fa5HZQbTj7S9eTDiHc1TLMsG5CrJsYTJf5DArX2K1EX-Iow1qBhVQtmI_NgdbMWqRfArex0ibz1-SKVR2PHWRf1PqMK9kxFpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JshJ7Y56RMOYae_WncDkFoD7zy9ULpd9PEgpTBD2NdIG1tbQKOO2vBaRpiLcybLM9jzFozCKzdYTmMZlL6LA3dsUrf6rBR1QG1KS8BQn8rYl2BLiPcS3qqk2i0434DM0GfIBTFq5nLmeLPcGYSOzzuJgLi3L8Iaux3cVoQhitEq66WEi0RZusffAu0-Dhu6PKEGRkbjPb_G2OZXnbL_WXL-QKobn3hl7aGM24WfdNGh7xShOr1QQxdK4GulZ5xpzBXeWB7uwXTyTHCOpCgaW7DmLh7LX3g14ZrHMoB2oMEFiTz5aEoDGn4a5kFp6wU9ZJ_uyE7jHDiBDbMeNPUJF0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F4azYahHRouxrXlqtpM5p3OIWJUUDyTPORS4v0WYgYwOQcH7g3f6O19zs5fCsWU2OesZDHyHzDKdDbjpYGOPyK4kaBse0AXO0wX6ZqqSvpDF9VpBCU56wlXRcYXRGbTzi3aMW7tmde53ofVfapGVcewQs-BYsDQbPfbF0n_PETR-1TxxwfaI89Jfw1UAAGJ3znjiDjHjjFEvqYljFkFfQ7-OH2QSx8A2J9Xn42Bb4aBncGyaqJpf0B-ALeApf4-9g1lZ3seHeQAZECFnSCyUHjHaBhVGNoNWnODJPK2f8PVL8NpDacFEgfSQGkfG-Gpf82NqebIURSsjKy-6PwhXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PjiYnRwSVJigaYEUARXSisS23Y4K_As9A1r-QrNBGHWtSd0PNxEonrhCNipLW98qKCI0S93JtBhqcOSoBJREIqE3k-210UFuVqkXPz6IRBwmNwwr25VW-tHa7MmIUhZKzVYEYkpBabVHkxDp_DlFrJRKTcHatfHw3KN3Zu95hGUIsepoMtJl7Z9NHGvi1oE6A6BqqBa6w7pRypSdkuuIWLMa-gf8RsfJCbkt4TaOcaQ_ocspG112XbBuOb9FgdSv2M8KNH7nU-YJ4BF8MnPWOjObb95hoUjAS5uRwtNDT7a0qjbwABR-sd0AXp1w2wJsXbVE4Ew5XfIctepNAtN6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=IHN9kvBoe07o3pJszAcrU9DKOMyy2JVhDXPJ7J-rAfWNxI6IEpwxl-4ejqlkuDbRF3FwfzQD-QPcMQTMa_wM811-hrJrWXuu5zelx5V_ZUfFolxGKaZ6X57ChDUbcugwjg4CoknRNVC2l0urje1D87CV_SNk2dPJSoKVF_kMgcjOcrLHh5A2MzAa4G3wNESKRrsok34OS4TIsFc8oJjXGfy2B6xWcRwOCUTRgq812hM_kOl3ZJpuGru_ueeYuoatJNW0GF2JAT90IOr_mXwGwacKYyrJiZOWe4HbwCQxHMmqC04h62NevW8LbFG3w4zeR10GO5NzwkZihx_UQfSwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=IHN9kvBoe07o3pJszAcrU9DKOMyy2JVhDXPJ7J-rAfWNxI6IEpwxl-4ejqlkuDbRF3FwfzQD-QPcMQTMa_wM811-hrJrWXuu5zelx5V_ZUfFolxGKaZ6X57ChDUbcugwjg4CoknRNVC2l0urje1D87CV_SNk2dPJSoKVF_kMgcjOcrLHh5A2MzAa4G3wNESKRrsok34OS4TIsFc8oJjXGfy2B6xWcRwOCUTRgq812hM_kOl3ZJpuGru_ueeYuoatJNW0GF2JAT90IOr_mXwGwacKYyrJiZOWe4HbwCQxHMmqC04h62NevW8LbFG3w4zeR10GO5NzwkZihx_UQfSwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyCVvgQI3qWh4CNJzrir1umnZAphJQiXo_w9k9Be1zAyj3TOlsbXZbwPjsVYOHWvsvH_lEbaHVHMsZo9Y72Y_-xfXEPTddOO7KVzcAiDswJ6DwO9Tsi0RIRX6gB3gI3rUWH7oDdk1w5T3efIg0xgfD03U1EhMhE7S57KeKGuZs9hcQBzlPEn4_lK8h3n0j3lBq-Q2E_-kv10vpXWR4HGMqi8GTyVHZyjSFhFlrFR4MMPF3sFsopVtB4RHY_sp5MdhpDb4JzT6BnwoVqJ4YVRzsaC_VPISVZLYuvj6ddmmgV7vUTZjH_W2zBEl7SyXGJtNu8yeq3LZfNoBZWoa5INgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZBs19Cru6IkeEckZH-W_jO7CBqosOV40tmxotuvcVrsTiHTdO86JYitBh2OHFyYeNyoDM2daUGDLrjGHkBfXgRzlELGzYSeOfgq6ryabRjaVVnoiJV93elHFUOB0ty0eOl5jIsTN4P6nD0powNhiwZYthxfR05hGucSRyCL-4-ghMJ9Uq-ANIPw_Sow3EoMDh64RtcicoewdKrzySAxBXbggSBOHtsvc0v1B6ZUDpUsQzUe30hSmLF2KxHCT2lEhvFzRYLYLb_BHEZyAnA0lEo3q8OxeAo0sZjqxFBMoK41z9VHN6UjY3wgVV53M5GX-g7uF1p5brJxxTvgwQ9pi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UIW5GqX31Z9I2hZmKDVdU051NlAh4BdrwtPJKvkpR0GKrgpBqdeq5ixBltH7NN2lPwydZCsmqOhQCdvJIn7QXzQXzynIYbUXfJvW9YqkSTrVneSOLhv7j6ODaD9_3vQNMZrSWiRlmZFas3y9lV4pEznWbzIhhz1xjtrA-qPlep4n1tcFcFa-G5v5DbyKuGjBn4_fQvrzUpJCD3E75oE2xi28P-c4JqjhzFXGbiyDkfBIaRjlj5dc3ipXkbe05zAwc1Q-6wisFkbJduGIPihxhvM2upL-A8aCcoyeKrBlKvGdjFYMz4LsdN1l7WBJwwUIfPAaTCneytK9rvUGTkLgdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NglsnSJ9vI2K6wd3bqFh21DuZhTr9mInUSZ6A-hztWMfOrB9KWL4hiEhsokz9NAXhGLx7Xs4yilES8nXS43Hvms0Te1F14hH60paZSbN8utUTQmt03WQ7_wJohJ-xvQnVC7muWjAffjiI7deEG-udCe85Tga0d5KlhMCh4y0bP3D_3LEEO6HNGojuHpcN9um2ZE7as9RTJHSrFeKyQMRWqWQLKALRkrXlgw1tFrhAJihTJzmwxavcv40FO1DL0ntoWHirPkqwJ2aOiP0xPk6LxOHlLk7YjhRVRRj5nbEn8KomXCtjzVSdpjlrLN7tXudKL0bbYGHQW6oTWzTRI_cng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9q4g5g8y5y1ITdBmcAa2LrvKovwUjs2W_MVhLuS-bE0Xa58wrgUOUrFB5-VLz_HdxyFAAYaM_VpgVvTXHvf80OHaLcFK17dDtbSSn6lrRG1RV5LgOMQMNDNTM00cxtuxedYtGJY5iRjKBtgGQD_vzhDWMxn1TLgJEePPX7ajJE33DSUr4VLwb9jNsZFyYWhOHFw4nXFOSL6xjGEfsdRHZ69xemyfF1QuaPY76Za_gNOtMQOTXc06c6L5IT9Z4D1iNVfuGNTl9oykU5DLXjitNY4HyUSr_t44zDSWdrxW1olSsXPEqUHqdFWXpaen1C93lRCa4731szmtyz1_J_WTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cVq6UZDCdy6g2DoaaJ_r-_UEL7b7BQqysA3_hVGMX1M_pD1wGK1xx7aIZaoEW3IBTB27AmIBhEGm2dLfWSkd0XGuizSExoyCnEboRzvQUlgvPLJbIJxWRMSJjazdI_OWU9D0zcOrMlwWVuuHBp0lgcNEF9uVSCfKAFwLsZkJXMmcKRvjPsevKZgkbDQ87fMOyPz-e2NQ15EHTX-1rCbt57IMmI2PngBv0K47wGmJAY_L5l-VHa9e0ioxeWqGiSU-30cvAXf_bZm61nSc6nSnOdAG5ys6Jzsqe3VTDL7zxxWTnp0bRLfEqEF0AL9conMZkHrjNuuj8ZzP2mJcu19dnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LG6yo_FpLzQQRpG2TlM1E_16qtomp21OtLla7bkaabT0tq2S2Tz42z14eLTHHadUEyRdCP4epy8_Egr1Ktj1rZfdonEikd856eSquLHMEU4xjYyyUL4GO1xTodzQgHiD5gTZRoznSZK-qnjptNKnLWSL-Pv-F1vbspHbx615vU0zSI4k_ezSjaqHzPfwvK6aVx4R54ov7B0lmM5zieCKjyYWznLrEX1iycWZ_gelQk7Ze4h3CqXynA6Vp05Z9BR6CNVutJduNEMsv1_wj2-h4BkwTU7G7c9uicUmg4plXECHIqOZegkS0PxJV7vwXVCyxP77cMvvt_ASgdt6OMr3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/apE1_GNy9E3oifhESaP2dP4R7pFNsbaE4dQAOTujOccpEg3P28Cti66Gl8rs9JcW6daFSvLLD72jLl-UH3NuY968oI74kuChNfuNlygx1kN5eVd0Ux7hSelgfd5Dr0azLL166yK7kmz8cCMUk7kZgsGudoNfBMGgiGUAjCpXTUsd3MjLA7LBU7ycK56U1G_mWOxwp6ddRbBaLIHk87Iy7zSmCG9ZveCivNNKq8MernoYd6BT4PiWAF5c5j3JAudeBkeylKUa5cnzlW2az_Q2UtZdeIt9Zf3g_tUaJ3gx7t3KJJAZKaM0QUSrSsYSBDnUdSEngryVTa_9lU_HGYje7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtNeATHxWHkJ2dimJpmbsQUwUPC7ts9Siqx87H-kVj1ZJkxU--mS60_e_ClsOwDwZgCp_olI-KL2VgCK7mXBht-KJC0v6BxAJqlB5_Eo_WifOvlC9OQin1VZGcg80qkjXVDIlnKnmh1cqzdIhe8Qi1USf4bamE0R0eGpmy0fJdtCeMyfutmV3ieP6nkKXlrAcI2EgO6GNIYmc29R2xfi_DjZtYVvkx0GhGAUd-ed4AxglSJ0M4FLIxnJBwc8UNVTf0Al2NYrt-fNVSivtcZsSRiQ3GCnZb4Us_qrQYRwWhoHRiSt5mW6cMjai_nvdTuPRbQq1kt-ScEUhTg7An8mBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCK8qgPiXwKFqnsoiDsZYpZPAB1HGvKWZABxj9MTplE04HmBS9Y9M1kkKZ7hKLIc2UF84Hrz5RdLGDBSk0CxuNmJ1lpZoNmD9D9SsCOIyZbFsH8pmuOXuGWxm6rdfp9R1pj7xybSpfFVXTsIuL9ChqELDvzopKwpmIJsIEe6iRGmbDagPYtscRV331TUTCDeIY5wzbN7Z1UvsZW31CJR3YoSWTOGYbbhxLthFalQyz-eoVOF99v7fR2_kiPAAe8QobVk74OxQwM0B4JM8RlnPHxxJnsXR2drRey45cawysoVdg67XztM5TRQrrfuyKuZupDDKH_62fewuFtFwoPWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L5Bd79zSidRiipL8iZ48YKyT-rnb7_uVxM5w6yGE0v1iVQCdmKnpqN87XazoalUNP0DK128D0-C1tMnJqCHb6Yj_dg6fSeSBT3r9YmJnm8GDLRoKwC95eD_4SzOIbagHXeUCkKjQhbiBt8f6OOkqNXZZReuOllcuHT308GqHiaHxpjoo-jp1ng_OHDGABxjg-ukmYvaW1JGt_9aan5LrlOdOy1rzIhp6_9qazkbrrE1ma3-VRiG6l0E8FykeVQFmYoqe4Z0y_mJ5HGi_AifXxSrfcZHwUIqAatO8n3QMR2p2WV0bTQk8mOQE9uXnINcIikCcIaEPVGxwce4gKG6KNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5n0elsg5gMJODjhnI9ja5IHF-HhYXPbVxLmYsBbdXXMpH95-msuwRMyxY6DdBBubSkXmvDNdhENlOm79lPP_NbVdDZnUmSPZLGDfPVLdfFh-DllFEnXKufomBpnwO2VmR2lh3E8uOZoNtBzjWNLDd69Ld8zLvawtU4MLL0CR3LFvh_NTjZu8WbMdolZ2Twm_uJ0FPoRTygo12Kq2pW_d7xJeIWaSQk-4hq7kjz0Z9-h825rEeBeZczR_T3curyM_X4hCginWu9C5rgYh8HFXQk_BtN1jU6LNBeuGdfmzYK9pK558PGK4HVBtz1yGr1Y1PU27lJGVmtOfZ2CrDwdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O41BtUxYTNV9LZqIMeRbSQY8wdmxPrRS3pZIyVUQuFcwMganZs1Ipr2JdKuTwJ1eQfHWqU-eZRBA5KNBaOcY2KXJF7ZY6pQ6WEjWoCkBw9o0D3WlqCL-voHZrzV9dx6pslWjVtzZEH6qP6HXS-92STH3td2mliW0HtSGYwfXq40zj6fUTuqPKNLskgT0DGmPWIAs1z10NXuumJ-Ew0NUEL_ZLTNelIJfrivHSljOdzMHamBqhB1lHGvno4uZVZFcCdrqQI6UFE73WqFYuPONLuyK-xuYZK0XU6ITXe2--_ODPvMzvn0skIvtiXW-0CNiYG0I5Jm6llPcFuWMXDWioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J0SVoUFrkbyCBJFkrGmFADLDav1KThTftM65YZxFI2y6QwftbuRYpV2cHFNQpH630Uc9BkaDe4waxyJnL4vEWYaoF43BcSn6qg0XAwXZ9X8I-7nwbq_jbpW_QN4x0b7XQ9UnyNXiauhZrygvHnnXA7jbIS8YQrC3XEclDhOYKWquUQh9KNcyTPLJbq_CndBxGJ3U4OYO-izAPDhVelzDtpgp2LsnHiX0rToLFEUqYKOFbfT3_rBKlZP65Iy9kvuw3i99igE7Um8B1jzIGfJnv4GG4b1On7OR9dgQ3JXIwGJiXhdRiRUmQMDIooYkObqcx_iSMPfN7Yg4qjSR3BANeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N2JYoRK_bEUafRC6q_enxiFr0PCmQ6LEB1UszNemw_-L-e-hvspffHyq3QQvFxpfP350TQdaybebXjqufiBBm6qGbhSyOgYZledgMlqaXtC37Au5gvAaSOu-oWz_4NYikWA3Th97eVEqu-vx_aNcg7y0c3isABcD-Xn7QSd59OGDT1KavN9GXx9RemNTv2lYQ3Qu8pfRi7tPUcADLq3G96paHU5ym1kEvOiTjmRh66pT0iBZBuPiw8BHXpML2Mq1REtmLLTSeQb3Fk00I-KVKIY5JXvjrQ7Dy8lqcI2GuYxxuEqKS_fTmy3LAPDFKbDhBdXKNui1V3AtfjkKtIsgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ziv1aWDK6hFI9ReheHHBCSYD6rJ3NCdIsp-6h9W78Bk7IIb4IEl4kwkjbseMz4WklmF4OV6Rw07ULBcSC-GrQUpMPe-2GxPtRgcxflRiat6B15b5ySOukvLOSJCfBc5CcPmaMlEOiKMRCQfsFaaIyaWmPLVzRwoVw9pV1GKcb4cPeT0208c0aMFz5QliKxI94uJ3GA1VQ7kaA8rgDCafan6JmmQx10c_3NcY3pQTUUm-AoK-oiBuZCPMRvH_Q6w5iwPk1h4fMdtAbeF32chG8Kvz_tSNzKc9EDuDf-NA1Zgoo7yLiZpWVOYpMRARnpNSDD8Gx84GAJyY6stLaDIlCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uM-V8Ahd8TGa135kMDMOgnJjwHO2nkQ-lzUL4G-CnSPzRpM_QWTTujnZ4zOguy1m0ylEUaxV1mljtLlqC7RMg5DQ1ItvRTOtz6DNtL-D6b0MGwF_SfQdDFFStgjnB-5w4nHvVjVeaJudZkC-D3qNJ6r5qO_41uwczNXneExRW2WgIAZIzhH4T8K24UOQSdG8BgBHErEKXrUuY2K5hEEEgIlqxFG5mnxAEP2OVCNtaDWhudvshd6Bmlcxlcm3kY9L2L9Hz9MXpDlYVmuLNYumgMLL4gDMOYfXdhAUbSXOu-clzYbjVXtL9PrlB8ssr1ASTo7XQ9A8g788nBcV5OaUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mgNHN7SAZTj-WlgmFtSZ71JEdCiHARrF1-_vps1NlbC4aYCrKWk9HO0z63MaEI8T2hmq-23XGdJJ648tytXBhFDjjjTuRcnxFjqX_Duy0JzoPib_XMgurTlqn-xAABxhL_DpihKEbnW8gZ2nSgfIu9GWd7YJTE84w3FrE4nS5WBP-_V9Jp8wMS5LHCR7a2ey6OGd8GZccNVRl5DYJxcu9QoIXiMcTmg3MM2dY_2uN5BwC-jYXSQld7H8c0HHZEib4-zgaqV2EyWYE8dvcmRZuJVhrOhQoRkY62aZ6fNK7cOXhGvt_EX_K13L-LjejJ2fP1Ba-6G76fVcQzWgS4jMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/soaLi3L8-9nQYT0f7WJFGRTm7z15-BSYkUp_hkSyuNISNz5S4oYQUsvoOrT6jbedoP2Gfe9-dapHZ264SHqmZLfWl_bA8eqcKCVX5A9aEp4nwtj-oV7g_t80DutnX9QDGU1xNfDOky3XYHFvPhAtGsAKUhTpTCQ0UKhDpVSU_47MPc-eRw6kN4O8_KQ60JeX1StCjF5NibkeUQlZ6n2iD87T9t5eDSjZnpkJmygaYKtgI-2jIZJ1CxfHeztPMOiTfMkcRUyBxRxF-SOSUJ7h8gQTEIFXjdcJu5ntexxg0_Y4DI6wXoW_3s-CqoJMlDcHEyezYbIbxuepw9Z-xxSBlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl02nwoonZUTWrWaOfOlsWayKHMeqs7SGnjMw6UtXM8L5Zr1ZNdXxZNpCjqNUrAlf01V9Ib0ae1TgSDsOIkb37wLMhIfrCMoSlsTJIsQi7-ybPOhtCpgBZLLEwuv7tIP7U4cLs0gNJwYDRur4k2PqCDaWpdtzw-odFupPGcb28bAQRXiHtcLjYCHJvP17HsFxTt5TL0hv16c6zNYU98XsugE_VYnMMJ76cNvkXCUw3i6nmv7wwl8M8ARq_K7F7MDSo01IL-a61sOwwRkbVUE8TPuB2xVnmm_MuxPotlVswcz-IvHBlxUQbn_p1KiTPHNkC7fEmOxHyMWLz5fYmb-cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juOgR5dzBSSSkdVVLlrRedcTB3R6wlP6yQ-LbEj_CocEiZslAKu8vzaA5mv3SFY6cw-pfZr9s4KZYItrr26zuzKocUnk86bz-d0g8vzCTFuNxmalg1Qu5ibm-7KpY0MW-wd6aMEC5WLT-sQ4ZPGQ1CAEfZXfpA-lp_feNdjBphlh2NkAELWjAArhcfOMltW9eT-BLzDH5y7pWFeC7Nup0hhlVbgvPcjzicWc4nQY_WDgfmtTOkTmxZSdt8kgZu-efhK9AGxRd3aaNBbXIjAjq8jRDVSGEkBZpcb_EUSPJ1mbVOESunohfwOQo_F8rzxW70k27xqTweKoxbQtX1DzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbfzzxiTlZWi1BUvUqtVL89Xc8FjS_l5DpEhU4Sf33QznXZwtJsqg_lRGwEvNnQcYP4vg-cICqDM9bQITp2XT4nYpApRRcTiM29IeND3ZAMK8A3X6uXv-fRdg1tGIettjfXW5oV8YU53BwCdSaWRukk5Da5U5KWAiXzdIyozEdT-Mv_7erb2ob2H9-gLWV8mLLYy6x-GzJbzvjyS67s5hUDRC7-F9tAp5Pp9_vAgvGwkKgsTZkpAMjvBDdxjm509i9Sf6vQZkrISeHGeAsFzN0-lG8bFKdSIEqdt535umHLVDbCym0SxELi9JhxY-JbktGBKYffxAdWG7OIjMnQA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yq9ubJO0ZXiGqXd9rE5mvFkGqSYNd7btiFbIDaO-CwQDQNFY1zT3RBR_qVR6YwKqxpJ2RLuO0tCrsH1iFNF3suOvUNgoAW3r9aqofwSIuQgOUeRhEBnuwu9B78SmQC7tdY-M_rVjKYOmrPXCz-I_cf3HtXZnaBxdEDMOJOPhnP7VE7Vj-Kz_abmyMlgIzc4JauTEwbnk-eib7zDPG8lHSZRhhpjaThJ7k_fHH6tcKPsLE-R9Cc7oFhlX4tk8v1KpUoyj0J4SFjKIutDQKQJXP2Ad0TegZRf3Lq6BWzkejFGkom4Ic4l4eJi4WUgskFRpKWoffcoyHJ4V5XHagw8DEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYLsJzgzwTBfHNJw7KbHsJkp8CJlfjwutt2lBcAClBNgluVoWE391EnOYx3D8l2_lZtMN8whJZ-fCVzZNsa503-zAM4jsPkuQbpBAwlC46p2wNOkeJL1C0Yho85Q163HihWEFYey1V7AkA5HBBXpaCRJteAYmcxndRH4m2M8gxU9AC3GYnkhh67iYOyH0qsYyRY9iOSaLG7hcasfiOZ64-cG6acCMuySqxM7yux27xChFJtJSAi1q-mUlwZwUtIHItynCP0T0iJKODh8IuTwcSuL90JHUVn7Zp_8ZKqgyXp-Wv5ew-iyZYrqi8YdlsuWLQQiIjCXCH1wOf69HAKm2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B0nZwro2RcW2shjy4RSPL17OSkOwa4tAjGYyIa5Nt3JL6IHReMdhAI55dxdPZVKcD9hX_ZW69_b8_mj168VDeIZHdLlOTg3cEZnVlZsUy9jtjH-4nHOXsMpeVBfzlnWOZx0NCfwumuKLcHDZEi0cOFV-y-XK7y7vqvlgRYorrfbg3hDnjLpfXp8NuttQ2MqCPStMm-xmjfd8Qbu_EY4oDQaBj5L7YGPAAG4G0Q0DdHmUj-XfbW4ZgsBg_Bt0GcmboHX46EhIR1vw4VK-t7cU_yacQouuV5wE9hUQqUIBlh8iNmXZXVweH9XcSCbjLhauqBmG49yNkhhfSZ1UWdMpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3jdmIZGF-HuDKR3WObXlhvsG33iO5WA3o541uCX4TMSM4XSuD1wv9eNHXGirpde3XiKU0erEjDlM6zUEonjTDL9TXIxFyrL-0Bj6fgSI9-A7TwmmooSd3Ejpc-lXZTr0_jxWuev4-zLpvRk9z9QQdyhDDJGdlgT4FjZq2hxe9bXfuXxZ--SL_IcHzBvcPlkwUnA99gCfe33-rtMiYhsteLCZ8IjxCXTwKQVpDhT_iX6JnlfGQABQ0H38el5Z6Sf9oiKXpiKnEPfb5pttjJ4MUbqfSXlmDJguSWLGCrygpgEVYJTYlB3h3hOpv9IqLukWNeLS-fZtOKUjE9lbCEoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bt4JpILIIKcQMFBJ_-A6_FeuNCWNqL128WUp2mgz4pBeQBwUaobIIaUmF-HcCDJHF55scYs9Gzb1lh0-fii8JSDSmzkkEhjeRA0O7YpafNJ6sVTLnWAb5kVpXE1Kue9VZUH9fsBHBXN-rXHXsy46ZSHDZQigHtz8JnHzaV_iBS7cddp9QW4Y-M9lpZJFES9jurvK4Ogf9pDXQDUSFNV073LKr0dK8x7RyrFmCaQbeAUeZjlSp1csh0Iqzw7zSnkz2ugVEmB1Ng8FoX8SYLy6m660U_Ruvi-nA8Jdd7g5VCfQtpaNl7L7VVJSLbLtCONX3LjtYEIPUFJQqHjujzGnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lYmiB6U3bAmdlI5ViVfZt2HXPLD31cLcVZbkkTqAwNUuvME_oVJwzHchLTvShXvA4mhmFTXQq_yhoPyCFmaJKPhyZax7cBdkgmM9PDlHu2rkaqlT23saEnQZ3NjaBd34ZWPR2sPjOAZdmW7TAl1C_4A1uOjjbcsgiILcuX5DWwigrFkQUfXrQ5bVzRN3xJuOIP_58d5HQ4jyLa-QEawz9PPATXc9LHVzW_H9q-OYPeMWhGSqBvERk28xNVtz3fpeRnZDkBrg7gQo11cKGb8IN8DRzYnk6laqIfZCSS-8giSnMtuaYgpm87CB1oVF4GNgaTYXxRmuCGR3qZXL9PkDbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4BBGQg_lPdfZUMoQHb6wWfvIjxP7MyhMv9XMkZbTgVRlRVeljg5cfKv08EYWCT_laCFP3UD_t6kuJTYGKRxNe30ATsDr7Eozs2t4h4INjs47KvQd9nDhSn4la300UbTHMdsNS_J69y9SyDoKHKlZkjza2jUI-M9BGDrsv223i0fDujswkzbmr1VAt-CCQLPoSmu7AL4W1kl7Jk09fKc10ZSBWhNvoaFdvhdYKZLYQff6Z-PzKF7M-dp6vP3QTfsDSJ_Xx2rDQ-S7fspedcJsJLXALcPsM_0W92SVb-J4Ad09l4DPT5lyQ96YcpMOptifR9oN0xok35ZyDQBFdalMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmMn4_ITgeh3n-VUblAADbCdRXmwR83XKuME3pRyUmGoVFnf-WwqDoKuDpNW6Yp9K0Qe-k1LB7PQzlg9CJDCn0bbUdrBTXds6IJAx52DXpm8F74gf0RxvOdd4UCmaOyufg_sxguWnmlry-mp659TfftvKoV6zMgdM8v443Jg7un1ndv5ps53IXxmzf4rc7-kKExGTPFznuLne2XK6mT27qM9VxH_eH9eIaedHyZxVKXInzwplBp4V5yxqctlQlTo7RirMHp-ShsHN3i1RrJeNm06iZ-_CXhK4vTDbwXsYwMUM8m3-FpwIA0ime-x4U4px6WJEt2z1NkiYwXlO4QbQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMRw5CkUiPB_OvboXYoKysI6MSj0ReVXI0EjnxLQpJetUoNbKtPyzUqeSq0K_t7mXxvV11tZJCKc1zHKXWEJu6b2sHRqALWNcu-CuRteaN4ZdzULeS3trnxe0pkHU9o97wed65mQxZEdjS4RZAXDrD7J0c6hAJ5r-kmT8DdT_bV9jZ_N1DLxiiH0r24Wzts6VygSGgue9WauI5ar2s9NXU0OSLNkhvFWeiYTWhyFVaPOcVsCTUGn8C8N1ZgXqH49tMwYDxpLQX5rSWDs2tkV3_Dy7qlYqljouWwZvXLHu_2zJUNSqcwCbWAn1aAyQcF6QrE3nIb3CGOVZnx4YLUeDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
