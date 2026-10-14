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
<img src="https://cdn1.telesco.pe/file/asJjJsZZpPcPxVsMpjHsjaTE7Z3kt16oEd61HzCzSMdY0qLbdh2dM0K7YPp4WVOk_yBR2cPNWS-IGFUTJRy92mmCIPb6qKtnc7sMgJ_RqzwFz8xS-Ylq0SsjBf4k9HBJ35UN9B18V47F6Tp_Cxwc-E4cg9QEEVZ1VSPBJTpDkDGIQUkBPdKDpLBOAXwbBrjqnD-8t3SpMPiee1xSFYkQe3lQeSUhmcg1MphLYnBwAInfnmGuFlvAaq8kmQ202x1FIbCxFwhOuX-XpLO8jTZ8IiRaDQbwVM6CkM5YG_ylmmEtfptCcjfYPYoZkkBBZCjj-aaBfEDb8Zt3Hk9JdEZKjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvdmqcnVIsM_qm9URWpEu2zn85YKj_taTo5n7w6aZ7_w-dqoJN5lPb_jkLiDWmblPdoM2HV4JvZs42dfZYtHdcYpV1vMxGO_mMKAJ7UdUIrzO9InRU7ovWs8HuPM4sqmuf1TWkKSWQ7j5wekGQ8fP9WxJIiuFbABtHf531iOe8kTUW-klXva6Dpt9lIFg2ryM_w1IPlfORvyPZJSd8igHC5V_TASwkIEavF3oB-8iDxVzyyN236c9GD_WSYpRv0vlW6Xvr24L9ceT4wToFqEvhNJz6SgbnwfR5UiA0ykdyL3Zs5joXfoZ8LeSrUECoQgD9nKxBc_bYEydv7ElNLLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای 4 آرگون اومده و به زودی تستش می‌کنم
بچه‌ها جواب‌های خوبی ازش گرفتن
🎨</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/5582" target="_blank">📅 22:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">- با این روش یه VM آمازون بسازید با لوکیشن آمریکا(200 دلار کردیت رایگان):
https://t.me/MatinSenPaii/5130
یا با این روش یه VM گوگل بسازید با لوکیشن آمریکا(300 دلار کردیت رایگان اما 10 دلار اولیه باید بدید):
https://t.me/MatinSenPaii/5149</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/5581" target="_blank">📅 18:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جمنای و سرویس‌های گوگل رو هم راحت میاره</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5580" target="_blank">📅 16:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برای ایران هم گویا نامحدوده حجمش و رایگان</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5579" target="_blank">📅 13:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P09JIJPfX4yyLy3uh5YpwpWnYRPPM7zxvum91M881f81GcAecyex8Q14A9eMwP_CoGlSiE0Tw9-sGhVjupRW4GDubynEhwjPxAbjuMMw3uLJ6Y7U2cLxi90OCOIhSZ7FXPX6vmme4o9GJyha5HtAyesMjtw3rbJxKbmwk9OtV6p3NvFQnXa96AuM83qB225hoLNGwwqmuAQbJXc8CEa9VLcBvHODX8FaE7qjfgk1V5qKMGPRi6p-wetffASKLjG0ONKVQL_r4YshfcmKcZ9_xqNfL_5JWkhCij1dsdv4IWI9avm9PU-rmOsY5FIU6EsRdHv3W59XFMs_zZZrt1xKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FK2KPj_yZ4AVQjl8UPntpDjJWUCcpeJBvVcJjvhTgZnJl1Lnkrxy8U-rP9Kl3xzD81Fs8JdkKQVwsQQ9WGDBmWNZnbz8FaVSxpwdmLyKfboszm_FVYamA3L9L5CO_E-jKIrud5lqwRJ_vWYuSvTwRVmgVSW3HNBzat23MCpSvPHigW-YCFRVPgBdXqDdidBdtAzou-8LdwlIIskM8TZFgkH2DEKE9UGvJuEKp0HVIyPLAR6NNRbiC7GwgM-4VwrbontueBCO2EvW8MlNtjh7SWzp9ug3qq2MynIqHfV28uNLsn7bu4w7FxLbATTbz697Cf84Yic5n8C3lWMrXoDcbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب ورژن آخر فیلترشکن Lantern(نسخه Pre-Release بتا از گیتهاب) رو نصب کردم و با همراه اول و ایرانسل و شاتل کاملا اوکی بوده. بار اول پنج ثانیه، دفعات بعدی فقط یه ثانیه طول میکشه که وصل بشه و توی شرایط الانِ اینترنت، عملکردش رو عالی کردن. یه تست بکنید ببینید برای شما چطوره:
https://github.com/getlantern/lantern</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5577" target="_blank">📅 13:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Qa_b8ALAAAuBV5F49tmxw2S-L-cWBumbf0fUOraCB3C45cLqiyg__z6nuUWt9CMZgO8Y54ZW_bujWjfuKN-yhDiKoek88AwLpiQUnnJ076VdWwtKk5HKBLnaLaFXYG-o8ISXJ0yhfqRcqh3MKWXsAmqBgCXbEIGEYS8Mi3WpTEWXqgPaUUxjuDAwQM-VeI2ZmeLrMJlktSrDWGx3FZICYYAWwtS64HY-FFtH2O6ZzlXBvFqVfAaa-JrAuAtRwAedZzJ_Du2KVPBInp3PQPg_kaeX3hz1bA77_3zNs4qYFSJXHznRS6hO16wD4lZ5Fk47SyJ2pEOu4S7K_Jyn6Jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
آموزش ساخت یک تیم از ربات های هوش مصنوعی  Hermes Bots
✨
با فیچر جدید Hermes به اسم Bot، شما میتونید ربات های هوش مصنوعی با اخلاق و رفتار های مشخص بسازید. بعد از اون‌میتونید اونها رو توی یک تیم قرار بدید تا باهم شروع به همکاری باهم بکنن.
👀
درست همونطوری که یک شرکت و یا تیم واقعی کار میکنه.
توی این ویدیو یک تیم کوچیک تولید محتوی درست میکنیم و نحوه استفاده و نصب Bot هارو یک نگاهی میندازیم.
⏯️
تماشا در یوتیوب
پدی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5576" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی و فکر میکنم با ویدئوی بعدی یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5575" target="_blank">📅 20:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا Mpay رفته زیر maintenance. حسابای منم قطعه فعلا که گفتن اوکی میشه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5574" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tAXHTkhI5v0TjgmKgdWD5HJYE7_G7yGJpWc0BEOSSal2nkF32oWzu1y6k8snHPgp5IT8anwHEsV3yTGku2kPyyVYVzg2QF4iOoSHnrtBN_2FVgtFND0qvpJypZxnE-0TsvXZWeJr3qNgLsPeoMUVFSBZLk9OU0CcIcgF_X1wc7CGkAxLbFlsrWBahg18ElmlQRE6RgzUKTnHTkPgaJlyBxX0F5ttJxUjc3WSWCwzKOt2NgVAO3ORjP-H37FhF0iIf0-lQ6bgLdECMQpt0VKz5JH3iIXC-mJmO2iJc3dSLkbmx3tp-dzf6jPgJ9s_p9pkewsT82ukvz41WD28wO-G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Wonder بی سر و صدا معرفی شد:
• $4 input
• $20 output
• $0.20 cached
قوی‌تر از Fable 5.1 و GPT 6 Astra، و هم قیمت Opus 5.5 اما اندکی ضعیف‌تر
(نیومدن Sonnet 5.5 توی بنچمارکشون یعنی احساس خطر کردن
😂
)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5573" target="_blank">📅 11:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flUdsrIq95vQL4JS3utrSb_f6druVMymXtE9gvl9xuT90dTkouvgstgE79MJ7iKHzTL3Y5Y_pIcSqOTgl4C80Bn-5WkJeEcBjCU84BCAYTAyG34krp7WRto1ijFwzlk5j4iivcDX67-89QzfsJ0AsvsjjxKKpHs88dFXOee93miJM3ivuSgvxmhnpR2_6HH0JV1ZZf25gX7NI0_ZwU59TfgvLjnhmHg9ABVz4yoMsJbC8jx7T1YCivx0PTXs9xNmEmswBPjH_d4hP2E1ZnWgKiq0HxSNZSAUqDeIE7_-7Z6uc3uqFFuWHWFcAATbhg5xQxazpaabzh_jcX97aGFNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ؛ مدل تصمیم‌گیر که ۱۰۰هزار توکن رو زیر یه ثانیه می‌بلعه!
استارتاپ Subquadratic مدل SubQ Snap رو منتشر کرد: کانتکست ۳۸۴هزار توکنی مولتی‌مودال (۱۲ برابر رقیبش Jev)، پردازش ۱۰۰هزار توکن و برگردوندن تصمیم زیر یک ثانیه، با قیمت ۵ سنت به ازای هر میلیون توکن ورودی و خروجی رایگان.
توی بنچمارک Decision Index امتیاز ۶۱٫۷ گرفته مقابل ۵۷٫۹ جِو که طبیعیه. ۱۰هزار کاربر اول ۱۰۰ میلیون توکن رایگان می‌گیرن:
subq.ai
در واقع پنج دلار میده. مثل اوایل jev
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5572" target="_blank">📅 08:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی  اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی): هرمس ایجنت رو در نظر بگیرید. اما: سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5571" target="_blank">📅 07:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MhfDt37jVHFnheTvXiVE6w1Ybf5M91xbSCuHft4xvEqqyrwYgao9h4SkKcVp4Frs4fIF1_OphiimWmTAVGJw2EDQ7sHvmpvUHte8hS8Ycz_oOvNlJtkHmcS2Q9v81mYa6f1cjLAPYswL4VQ_3_HFWfpIH0Uizz7KYJ6ebRXEuY9LeCiYwo0SVobUZY5uuEabH0VIp5ihndKoRqGRftnR6mJdIJ0RwE1KEX53xcd37fxrur6J4B6hX_yG3sN5bs35d16UeplKVRv7QgG0wca4sOYpnyciB1oNn_zMwoVfWoLCuzgmDZ_Z_2uuehwk41VhMoTaGfQMJK4PBI14w_arog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی
اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی):
هرمس ایجنت رو در نظر بگیرید. اما:
سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت داره روش اجرا میشه؛ با راحتیِ وصل کردن هر پلتفرمی بهش که فکرشو بکنید.
صرفا... با سطح کنترل کمتر توی مسائلی مثل محیط اجرا یا خود API. که شاید نیاز معدود افرادی باشه توی این کانال
حدودا یک هفته‌ست که دارم با این ایجنت کار می‌کنم و واقعا عالیه!
مدل پشتش Muse Spark 1.3 هست.
ایمیل‌هام رو جواب میده، واسه‌ام برنامه‌ریزی می‌کنه، چیزایی که می‌خوام رو توی Google Sheets ام وارد میکنه، جزوه‌های دانشگاه و Rustام رو خلاصه برداری میکنه و قسط‌هام رو یادآوری می‌کنه(
😂
).
یهویی مثل هرمس "سکوت" نمیکنه که وقتی بهش گفتم خب چی شد و چرا یادآوری نکردی بهم، بگه "اوه شرمنده داداش! اون لحظه api key یا سرورم قطع بود(دفعات زیادی این اتفاق افتاده توی چیزای مختلف اما هنوز، هرمس عالیه. برای کارهای مختلف. خوب بودن Muse دلیل نمیشه هرمس بد باشه)"
شما نمی‌تونید روی Muse، پنل VPN و DNS و... نصب کنید. لااقل من که نتونستم و اصلا آیپی عمومی نداره و فقط دسترسی HTTPS میده. 9Router و... هم نتونستم طبیعتا. هرچند به نظر یه کم Tricky میاد و باید باهاش کار کرد هنوز شاید قانع شد
😂
در مورد 8 گیگ رم و 2 هسته CPU هم بگم که این منابع اشتراکیه و متا هم سر گنج قارون ننشسته.
سرعتش هم یه وقتایی میاد پایین اما خوبیش اینه که شما با هیچ اروری سر و کله نمی‌زنید! و یه دوری بزنید و برگردید همه چیز اوکی شده.
و میتونه براتون تصویر و ویدئو هم درست کنه(ویدئوی فریم به فریم کوتاه و..)
که متن فارسی هم داخلش خوب میفته.
آموزش راه‌اندازی:
*نکته: اگر که هر چیزی شنیدید(ریجن ایمیل و تایم ساختن اکانت و آیپی تمیز و...) اشتباهه. میوز فقط و فقط به آیپی حساسه. و تنها آیپی‌ای که باهاش تونستم وارد شم، آیپی آمریکای گوگل بود(که صد درصد یعنی با آمازون هم میشه)
1- با این روش یه VM آمازون بسازید با لوکیشن آمریکا(200 دلار کردیت رایگان):
https://t.me/MatinSenPaii/5130
یا با این روش یه VM گوگل بسازید با لوکیشن آمریکا(300 دلار کردیت رایگان اما 10 دلار اولیه باید بدید):
https://t.me/MatinSenPaii/5149
که گوگل خوبیش اینه که سرور Always free میده و منم از همون استفاده میکنم. یعنی مهلت اعتبارش هم تموم بشه، اوکیه.
2- پنل سنایی یا پاسارگارد و هر پنل دیگه‌ای رو روش نصب کنید(توی آمازون نیازه پورت‌ها رو Allow کنید از توی پنل مدیریت سرور روی سایت(به Grok بگید راهنمایی میکنه))
3- یه کانفیگ Vless معمولی Raw بسازید(مهم نیست که مستقیم کار نکنه. گوگل که اصلا امکان نداره مستقیم کار کنه)
4- اپلیکیشن PattN و PattNG رو نصب کنید(یا هر کلاینت V2ray که از قابلیت Chain proxy پشتیبانی کنه)
5- یه کانفیگ که واستون کار می‌کنه رو اد کنید، کانفیگی که از سرورهای گوگل یا آمازون ساختید رو هم اد کنید، و بعدش این دوتا رو با همدیگه Proxy Chain کنید. و VPN رو متصل کنید و پینگ بگیرید.
6- بعدش وارد اپلیکیشن Muse روی گوشی موبایلتون بشید و با یه ایمیل که تا به حال روی سرویس‌های متا ثبتش نکردید، وارد بشید و ثبت نام کنید. به همین راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5570" target="_blank">📅 18:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e5nnDVvu-ajQjd8a_zkkcZV8iHK56qEmBresS7Z2HRz3-J2msjOk6G74YmCUN3rarohw4aHJZ0zs3NtSCajDvyo2C7SnMLbDEMYrGyYA_93MfhmrPRoXyrdNb5Obnqa1q67pffDj-BHa54GugGpNtp0pOISIdeP8Jqv-hHiujqlk6dE89C45Iy360rN_iMMCb9GYKfDABYOrlbMKTSJ85ttLvjvQ7nn9IAWua_JEABsJdgJuJZ1m5v36PVwEy-AhRAM64brGfyOtaOsBKEDeDUMjGv3x8I3Tlq2f3i8MuxbkfZEoUtRJjHfW1a-k4Sd-OxAUAhOsCVH-r3ITPgoOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول نوشتن آموزش ورود به Muse هستم
فوق‌العادست این ایجنت. عملا برای کارهای روزمره، کمتر از هرمس استفاده می‌کنم به جز کرون‌جاب هایی که از قبل داشتم چون Muse همه چیز رو Unified و سرراست داره، و توکنی که میده توی چت برای مدل هم خیلی خیلی زیاده و کامل تمام تصمیمات و کارهام رو یادشه. به زودی از مزایاش بیشتر میگم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5569" target="_blank">📅 15:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeFXZWPMC60-32CM3FNCngp2tSxp3uXdnzRKHcgs5s9e2zoAAmG-42mcwnwN7yRVvqGBQa6r3oKScw1pKUPqSgD8Ur4zbNhWx7qlZIuDIFEljaX59uZ18UnLD6IpUVXwrXW_qAsdG3koVMFibVYcqNcBb7viCvr-vTrqxlSyN0BeWtvWnbh_AXlofDDh_1bt3g5w94gvJbs657bCZXhbrK7AjtuHx6TsBpmjzDLKurOvyyJWaIZ1qeHC_d8WTPkvwW6SoB4V2zJmktYnRWxqdCf6BwZqhS8kcR5Gp1TQgR1WfW9dGFeMH54P5o8Q27dSHjp0O-ccfDY7w5ljte37fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوری؛ جایگزین اوپن‌سورس Canva
پروژه Doory
https://doory.art/
به تازگی روی گیت‌هاب منتشر شده و خودش رو جایگزین اوپن‌سورس Canva معرفی می‌کنه؛ یه ادیتور طراحی تحت وب که می‌تونید خودتون ران کنید و یا توسعه‌ش بدید
🔗
لینک ریپو
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5568" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPWQpduSmxs23RXuhgS7T5RqKckfasJDMsM8SSeHNlLsoveJ3z9HXolJHx-FcjPS2RzITDNJgmrR-yHK7ETlVqKZ9PtlGE2xiTFFvssKzckufe75YmxVj5xHxRz844Xo2U67sX8OyHP3VfMfa2ekSmMt1oUP_wTKXykynRwXmei8ZB_oqKTGRviGjVR2isUFftSfd96noPlTm3wRdkJIArK1qNQAS6tfgHSsKctHsxY0N1F0-hMgqLiszsDznzZpBnKbknWA2JWDvFWfc2XiRsBqASTsxtU2CpR05gG4RGx-RsQSsavWri4n9vcBLclNj-_gkHqOCHwIvBoj_xgg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل زبانی‌ای که خودش کانتکستش رو مدیریت می‌کنه
محقق‌های متا، MIT و دانشگاه واشنگتن روشی به اسم CLM معرفی کردن؛ به‌جای خلاصه‌سازی و فشرده‌سازی دستی، خود مدل تصمیم می‌گیره کانتکستش رو چطور ویرایش، نگه داره یا دور بریزه. می‌گن هم عملکرد بهتر شده هم هزینه محاسباتی کمتر
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5567" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5566" target="_blank">📅 10:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط
مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5565" target="_blank">📅 10:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5064aac929.mp4?token=dJoJv3d4CatTXvX9YntRBr2dF_ED_V5nrBEI74z52p8qAprZIzqPA2oDmwKMaw11EWkAnpiOi6dUGszbvTklCEItNeb79KSNUMNkP4rFCjkY3G8rpJpcK85hPjvMuAMZzl71i_WAgKUDzMi4Cb97Cfu1xjnU0P1wrg0fD3wX2Ep0sHjhjhZIDsHUQsTAoOVJUlVx3cSjcZHjrFRNfNYnECX7uXOx0QqA8Rq1r7j4AXqce4wUdVAVf7d8zRoMh40x--mR9UmV-W77zhNwFal5QH3vTYXK2HBxwzva10T9PcnPDKUljEFomOT23YwOV0sPrTe6EuQGVa1H1JqNQYijlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5064aac929.mp4?token=dJoJv3d4CatTXvX9YntRBr2dF_ED_V5nrBEI74z52p8qAprZIzqPA2oDmwKMaw11EWkAnpiOi6dUGszbvTklCEItNeb79KSNUMNkP4rFCjkY3G8rpJpcK85hPjvMuAMZzl71i_WAgKUDzMi4Cb97Cfu1xjnU0P1wrg0fD3wX2Ep0sHjhjhZIDsHUQsTAoOVJUlVx3cSjcZHjrFRNfNYnECX7uXOx0QqA8Rq1r7j4AXqce4wUdVAVf7d8zRoMh40x--mR9UmV-W77zhNwFal5QH3vTYXK2HBxwzva10T9PcnPDKUljEFomOT23YwOV0sPrTe6EuQGVa1H1JqNQYijlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل جدید Claude قراره خفن باشه(اگر لیک‌ها و شایعات درست باشن).
مخصوصا توی ساخت ویدئو با js خالص.
اکانت توییتر chetaslua شایعه کرده که روی Claude code به مدل جدید Claude Next که فعلا در دست تست هست، دسترسی پیدا کرده و هی داره باهاش چیزمیز میسازه(مدل Image/Video generation نیست)
و میگن احتمال زیاد، Fable 5.5 باشه
(R.I.P Gemini 4 Argon. we all forgot about you brother. hope google come back with Gemini 5 Xenon next time
😂
)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5564" target="_blank">📅 07:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnvlRP51fKoub5NdKBFGQaP5-UdQav7SfDR4NJDNu7jeA2cd9JYAoTdEdK-BwTXWwHWcWLkabqchZb2Lpd4zZzW19qYY1ajPxQkP5MnvLOFxRxD3JGT2H1KagTDWyr65-5jXcIIq34QdzBop-irdQ_KLDVsB7qNrLuHrvncBrI-f7rRA2utg8QWufoyslFfl5zYIBh5QM6UFyCYsheQxsRyeKGY3emdDoVJrvSsWHThN6E_BDz0OZtnp_fYpnq-aKOMO4GI2lv-KuMLMbGLfmeW4P87xzBM032rqI3wjfiTG982GNVJz5ikx4QSWzlFSs0Cy8ZjGHAxf-7UkVE1eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله ClickFix با طعم Claude؛ تبلیغات گوگل آلوده شد
هکرها دارن از ریدایرکت‌های واقعی نتایج جست‌وجوی بینگ به‌عنوان لینک کلیک توی تبلیغات گوگل سوءاستفاده می‌کنن تا کاربرها رو به نصب‌کننده‌های جعلی Claude بکشونن که حمله ClickFix تحویل می‌ده. ترفندش اینه که لینک تبلیغ ظاهرا معتبره ولی به صفحه مخرب می‌رسه و با انجام دادن پروسه‌هاش، دستگاهتون آلوده می‌شه. کلاد رو فقط از سایت رسمیش دانلود کنید.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5563" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مدل‌های زبانی بایتی؛ بدون نیاز به توکنایزر
یه مقاله‌ی تازه ادعا می‌کنه ترنسفورمرهای معمولی می‌تونن مستقیم روی بایت خام کار کنن و با بزرگ‌تر شدن پارامترها حتی از مدل‌های ساب‌وُردی بهتر بشن. باور رایج این بود که دنباله‌های بایتی چون ۴ برابر طولانی‌ترن(در مقابل بیت)، ناکارآمدن؛ نویسنده‌ها‌ی مقاله می‌گن این طول اضافه با مقیاس جبران می‌شه و انتزاع‌های زبانی خودشون درون مدل شکل می‌گیرن(که به نظرم اینجا باتل‌نک قضیه‌ست و باید به شدت بره زیر تست). به نظرم مقاله‌ی جالبیه. وقت کردید بخونیدش
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5562" target="_blank">📅 21:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lqQE13bsVxqX-jlQ5RKd5FDHtIAre2l-j22N6U1ClOuEPOQQG9r5z_VegKpQTUsKXjm4Nj2ktUE7Vcc9mabCJodGcvGA5vngs2zTA3kSG_SDRjsG8ZYoukhwlhev9_JKdLVZGqPNeoCVljle2qZdjwgHUEPi1XvP7XunNvCLdHhK1IczxIb2Mi0MtPKLkfjw0FUOA75upJIdxBoxbOieJoyCQgTNvKmGi9984Ja5jvJ-kwk3UWO0aFDX8KGlY1UIKBaTZ4y8nr_SwqKqQIVHwMhzaYhMd5wFPVgpTUjqRVvSeXl0nI0N-Uw0FS4kZ43fCGSmc7xqqTUzUeDN-r4EIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل اوپن‌ویت پرپلکسی از Jev جلو زد
یه ارزیابی مستقل روی ۶۶۹ کیس پزشکی می‌گه مدل pplx-decider-v1.1-27b پرپلکسی تعداد ۶۴۳ جواب درست گرفته در برابر ۶۲۸ تای Jev، با ۴۲٪ هزینه کمتر برای هر تصمیم(که فوق‌العادست. موندم مدل مایکروسافت چند میگیره
😂
). قیمتش ۰.۰۲ دلار به‌ازای هر میلیون توکن ورودیه، و خروجی رایگانه، کانتکست ۲۵۰ هزارتایی داره و روی OpenRouter در دسترسه همین الان. صدر جدول Decision Index هاگینگ فیس هم مال خودش شده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5561" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uX4ymoovevy3bebVDnHJCT64n2EaJTceBld-Ltl2xk5uBX3oS4xC8I9C4Ym3-dNJXhi_96PF462d_T9CcPvbV7bUype7FrLtb65VX4O_wNEUIX5ajgNL2qkBqPkB-5xB5vMloi0CLUZKZrDjP6op74-fc_l67NIh_P7Rq3yXseXi14wBxiuF5CJmS8AHUEwGtbKhf8PD1xzUwjlffMjKPKH5SIKHa--Euz69Qyf1BodA3s3cfmxQOWDOSqGFmNhtdR34R32rSUf5yKtru2qUykcTvThu3wQZ9Sp7v69NFw2l5ex8iq59QGV0ywrg-BKoSBtIQXFW32uWLv5s8ZJmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت Decision-1؛ مدلی که فقط تصمیم می‌گیره(نسخه تنظیم بازار Jev)
مایکروسافت یه مدل تصمیم‌گیری (decision-scoring) معرفی کرده برای کارهایی مثل روتینگ، دسته‌بندی، اولویت‌بندی و کنترل ورک‌فلو؛ یعنی به‌جای تولید متن، مستقیم خروجی ساخت‌یافته می‌ده که نرم‌افزار بتونه باهاش کار کنه. ادعاشون: بالاترین دقت بین ۳۶ بنچمارک با نزدیک ۱۵۰ هزار سؤال، و سرعت ۴.۵ برابر نزدیک‌ترین رقیب و ۳۵ برابر GPT-6 Sol(چرا باید با Sol مقایسه‌اش کنن؟
👍
). توی Foundry اومده و به‌زودی روی OpenRouter هم میاد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5560" target="_blank">📅 20:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کارزاری ایرانی با ChatGPT مقاله‌ای جعلی در رسانه‌های واقعی آمریکا به جا گذاشت
گزارش واشنگتن‌پست می‌گه یه کارزار منتسب به ایران با کمک ChatGPT مقاله‌های تولیدشده با AI رو تو رسانه‌های واقعی آمریکا جا کرده. و این نشون میده عملیات نفوذ رسانه‌ای با AI چقدر ارزون و تر تمیز شده.
اینجا هم به دلایل مشخص نمی‌تونم بازش کنم جزئیات قضیه رو
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5559" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb_Cu0_e0V91OSrInep6DePwSTI2No1YHEhrSbu0dgyS9UT1rwG-P_mPUFvzNSJ4_ouH8lJ7Lf-B4OQh3tjDEQSpxwSTefzpC2AZICc_B-FS1EhMRfNkHxtrN_-gF8ufb2y-vMW8xTxYxRKF2I0qGl2mrz-qfIUcHmstGWio4TW537ILo4X7zhKlUi2bgY3rCsDh2dvQRL_32gM0dYUCMjUyVbtKJAZ5L92mhRgrprvo3qJC_M6J6t8wgKeJhLwxd5phyWhA_EcbqEnbH6Cr-lZDy8X-Hri_lZVUrGJbU2gdbnTOa00MFvipLFMRv_4wgIUiY79uS9ZVqvCPoOqC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌ای که یه زمانی فورک Redis بود و الان انگار وارد رقابت جد شده: ValKey
پروژه‌ی Valkey که دو سال پیش به‌عنوان فورک Redis شروع شد حالا ۱۲ تا Maintainer اصلی و ۹ عضو کمیته از شرکت‌های مختلف داره؛ تروپوت بهتر، کلاستر قوی‌تر و برنامه برای رپلیکیشن Synchronous و ذخیره‌سازی چندسطحی. تمرکز روی امنیت و اتومیشن هم جدیه و داره از کاربرد «صرفا کش» ردیسی، فاصله می‌گیره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5558" target="_blank">📅 18:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOO6s1NaVPC2NmcgUJEGX57FezmGEWSUGQdKLUv87HJmLHuZYdB4V2bKf4XZWzeRzzB4pnfL9vfCSPYFl1-5mP1pQucGHkQKNPtRpb_IIhCxjI0_h4GVJ9gMnSDe56lMS6qvZfP5sMrZ0tcMlhPtwN2xsU725KEObpvsvmcVuC-_ne8qD--VSvz-Kb-F9lonpfMBm8Ysohd_n99xbTba-iixZVugG9bbioGsvO9YuTMleFa_OIyd8d7JJumP9_Ma_Z26GEcotVUteOtq677cJjDcAyZl-ytgW9NlO0uiHV2kiLTysgltSHa2t-V721PGSsy7szuiodlV4nFz_ERg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من و ایده‌های استارتاپی خفنم که قرار بود باهاشون پول در بیارم توی ایران:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5557" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تیکه گمشده‌ی ارور هندلینگ توی Rust
یه رایت‌آپ خوب که می‌گه درد Rust انتخاب بین تایپ دقیق پر از بایلرپولیت مبهمه؛ راه‌حلش کتابخونه eros با «مجموعه خطا» هست: به‌جای تعریف enum تازه، می‌نویسیم (io::Error, ParseIntError) و کامپایلر چک می‌کنه خطای اضافه propagate نشه. با widen هم ترکیب می‌شن و کانتکست می‌گیرن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5556" target="_blank">📅 15:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ec0VBaA2XY0qRkNc3px5Rx6G8zOtNH4upzuBeV8_L5rb87hFGqeVpGTV4XmrjDOtIGgFJOJEIZETCV3nk-AnwqUdu79Tfo60CySJDavRR-eAXhefkNT0GHwm66LatUwISQ0CMw1_3h8Rd2Mqe-TDp4arkUBtcLUtOhRFKkN5FB0krV1iviVsH7KMFIUGsN6kRxouJchObXM2v1DPDZPVwEMpieb4Cd_gP7zDvB8g01jxRNixIIXOAfPGBif7Qohae-Lx5yzrfLCva6hJOhGqb9eCPYebcRT6ydBlk2JdCLvV0a46wDOIyG21SLq_VeJnxCJS_7LBLwj3Z5yqLkmsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدلی که وجود نداشت، پس خودت با ML Intern بسازش
یاوراج شارما تعریف می‌کنه دنبال نسخه کوچیک بازنویسی شده‌ی Qwen-Image 2.1 بوده (نسخه رسمی ۹ میلیارد پارامتری که ۲۰ گیگ رم می‌خواد) و با ایجنت ML Intern یه نسخه ۰.۸ میلیاردی ساخته که روی CPU اجرا می‌شه؛ خروجی معتبر ۹۹.۷٪ و کل هزینه محاسبات ۱۶ دلار. تو چند روز شش مدل دیگه هم همین‌جوری ساخته و هر هفت پرامپت رو تو گیت‌هاب گذاشته.
به نظرم جالبه ببینیم برای GLM 5.3 Flash چیکارا میشه کرد
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5555" target="_blank">📅 13:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/der89swyz5vjmnWNqF5_Z5WjEbSVtY-1hLpeVjpHk4sy1o4GP1D7KZtFft52L_hk2kKUzYizoU4UYB2ThzStmm06Mi-NRWNF7kzqilAHCa5ZPM3a6E7QmyAyUR1uDo_O4DnrW-q0BgvkZX5Wq8KgVdhBmyIXeMbaOZCgeO0RsPRKXprPs04wtHYXjZYVs1QHWVoADVYoHmWhJS6bbuo-XnMn7sdIczMGANBpt8nsAU3_w9D8zRuILvPN7xUW6OvyHloT3OIAI-UsiCQofxdz0RdfWrHwEC8_oTOTt2pC38s2gqKs0mTRIcf9GukfkCwoqP5VKBWLAqA9QGSbwoIDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده‌های زیستی آماده برای AI
ابتکار Virtual Biology شبکه‌ی Biohub گسترش پیدا کرده؛ تعهد جهانی ۱.۸ میلیارد دلاری برای تولید داده‌ی زیستی باز و آماده AI تا بشه مدل‌های پیش‌بینی‌کننده زیست‌شناسی ساخت. اگر کسی از شما بچه‌ها توی حوزه‌ی پزشکی یا بیوتکنولوژی کار می‌کنه، دیتاست‌های Open این پروژه ارزش دنبال کردن داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5554" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حمله به بانک‌های کره جنوبی با کمک Claude
یه هکر ۲۶ ساله‌ی چینی مظنون به سرقت داده‌های بانکی کره جنوبیه و شواهد نشون می‌ده از Claude برای پیدا کردن کانال‌های تلگرامی فروش اطلاعات سرقت‌شده استفاده کرده. یه نمونه‌ی تازه از سوءاستفاده از ایجنت‌های AI برای جرایم سایبری که زنگ خطر رو برای دولت‌ها به صدا درمیاره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5553" target="_blank">📅 10:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مدل تصمیم‌گیر خودتون رو بسازید
یه آموزش عملی و تعاملی توضیح می‌ده مدل‌های تصمیم (System One مثل Jev) چطور به‌جای تولید توکن‌به‌توکن، با یه پاس و ماسک کردن وکب فقط از بین گزینه‌های ثابت مثل A تا E انتخاب می‌کنن و احتمال کالیبره‌شده برمی‌گردونن. نویسنده با Qwen3-1.7B و transformers نشون می‌ده چطور همین رفتار رو خودتون شبیه‌سازی کنید. به نظرم خیلی بامزست و ارزش مطالعه داره این مقاله:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5552" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DcN4Z6nG9YBRG1KgxaRa24L-QgnKcfoB7YG1twsl_RYW-XLy4ROWUCkNpZRap8z4Pcw_ylWuUCTQ4JETaOEHYN6CeNqzWdpjZoa7xMcIvw3kdTcyjp-wXgl6XDA7IoY5o5j2faxaMt1X39O7UxYjWWSTHn2eSB-h2mc95MKDZsCw5hpyV1GUSw96GYPLzxRZA7ZPxI6ZLA5AtKkTNS-BRhxWosoWn2iG5nB_tR9lVQUecaqQLrFONZjwD3yhXz20vKLTLDnH1NvzoNK-2p0-GdD4dO5ewDKMxctPNTqfF30yXTGgep2khmY6VY4A-UOZWrUpJAOzztGQ5kyzROTnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفیس اوپن‌سورس با Rust؛ کدنویسی با Claude
استارتاپ ArtCraft نسخه‌های مشابه Word و Excel و PowerPoint رو به لاین‌آپ اوپن‌سورسش اضافه کرده؛ یه جور بازنویسی آفیس مایکروسافت با Rust که بخش زیادی از کدنویسیش رو Claude انجام داده. هنوز برای پروداکشن آماده نیست(که نکته‌ی مهمیه و توی اون اپ‌های جایگزین فوتوشاپ هم دیدیم که به نظرم به زودی آماده‌ی پروداکشن میشن).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5551" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طی امروز سعی میکنم اخبار سه روز اخیر رو پوشش بدم واستون</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5550" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلام
من از غیبت برگشتم
👍</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5549" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W7e9ex6-Gp9volCwgfjcgVti4PNKWSydJT6i5mNtZ66JONRLYvFw4kpfyFBcZcoDQt0Nb-6v-FxdKwbBelsSuU4cPQmbF9bbnHbI-oSS8DpdyGy707FQbpc4bji5YLfI8btCB_HzzMbbUHdTbUELVza8CyrmJXx-b6Jb5dDZPDqOVJMmSbYcHLgQSxQwUXypLlJHU8Cf-d254VupM9aWwm5aySa_x1nZgyDaBPfg5u4aSzHwY1i0l31UOagnx038FQXLesoupBZKX51ja_iBHXmmn8m-L3wy6EOqIzHOM-dSoOSfCMgY9ZLRm9LxHG2Ayknciojw21QDx1AbHiISmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADeoC_czPNDwh-Q9zoXBdCYfldoqci3V7dC63a2SpZj4MrFMhP4ebxiLcIYTbrLC9ezsiPxvSX6VVZNiCQb-WGQwuw2bwnSbdOkg0kguYxqC3ccQ6hT3bLZqqhjcIgPtsJZ0TU4f4XdczJl8MTpBYD7c6iTEVtLE1Gpuk0xlDvfAzCq1nhmJlm9MTu6aaRZBJaRUJYmaiRNFuSqQATFwXaTFoobeUij-gSnM9NujGdr2RWhHnJcx7EmOMqaCiF2-wtSu0M3gdlTFQ8DtCZwAKIj0vmZ_JHDAcGIY7BrbUB1vyrwUfmKZftDpPxBV82B7Zmwzp2kPDzLHrvcRRY2xWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAXDKwDd2N58w89SuELmyfYyaw_0YU4VGtEN2BTOx4S2KGmQ58wp2icFIty8kUgWejJASeE-7vPdZ7bb_Z3QPM0re1wNoYpnpNTPR3j8VP6nu71e4P5UIGkUyuxoPonWrVOxG4x0pJRBZPhQxdVCA6YMqFJCYfHO5omKu1XGMwI9QWmcG1FQf3eAjknD94-4_9b88p1zvEB93r12nAQ0GaqGMr7EGvY_Yu3EtyKNhWHNtkzQYQuzxV51A0rmNcxYLd_dv7pc1cQXHQvjx5oq7dl7t0rTsNmAbotfspZH58tv7TUvrKwLQMhfjE0BqqbwMo1z3kdIqZX1U6SckX0uJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=NvH-ekUPRSDA9RrZJ01lQyyJfgpn-4t7vm767mgZ88BF-J2ZxCpy27arhTAwIp_P0peqe0SYvlE6UDyNHReeYgXbp9X-xPa5hZFCTEVD_cEGVN3lxMyJudUxRThoOCIm84E8_EUggx-SZuFNjEKHbA1fNtDIkONanPLZGHEbcxTQb5hn9NUZrmG6hs2uT9m7Ujw8hMW2ublbqKIWYBx9WUEmQlsbUAr7V7x1g35y44zHd4MG7gi8VYrzKIxYOtKYkaQg9lTGEz3_e2eyjSIuWZwE8FZbpq7m1cuJJzsjHG0eIwiJUAQG1rCVO7tgUD-nm0gqV91igl9CqeFP-NU_zD8OeQ2hUFxDTERbMBgsUbIHjSBfQwJNJbtKk3nAU-zNUUDVnw79kLOWhv6M6UAmfIsHu7VVeYQidgWrgp2oNA28ctHuLBiMdqplM5AKbHyZNkm3NXKnySnmJLvXuvZePhxGs7X3gnS-DD_QOBkB8804DfZYuvq6syTXGQevQYpGGhB7zg8M9q3yI6jfhNcyv162Wrw6e3vBwVLgtkry9W_6rwRmCPXNHaHuKC9P1Zl6ZVtGmJ7NBffn6804tn8biRq8F9Utc_M17ILEPwCv2fJ3r8gYCD7gmnz8NPJd9elcS1hLI3tXilR01B3kd2PP1EszWpf_Cs-wdzq4TGSBtNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=NvH-ekUPRSDA9RrZJ01lQyyJfgpn-4t7vm767mgZ88BF-J2ZxCpy27arhTAwIp_P0peqe0SYvlE6UDyNHReeYgXbp9X-xPa5hZFCTEVD_cEGVN3lxMyJudUxRThoOCIm84E8_EUggx-SZuFNjEKHbA1fNtDIkONanPLZGHEbcxTQb5hn9NUZrmG6hs2uT9m7Ujw8hMW2ublbqKIWYBx9WUEmQlsbUAr7V7x1g35y44zHd4MG7gi8VYrzKIxYOtKYkaQg9lTGEz3_e2eyjSIuWZwE8FZbpq7m1cuJJzsjHG0eIwiJUAQG1rCVO7tgUD-nm0gqV91igl9CqeFP-NU_zD8OeQ2hUFxDTERbMBgsUbIHjSBfQwJNJbtKk3nAU-zNUUDVnw79kLOWhv6M6UAmfIsHu7VVeYQidgWrgp2oNA28ctHuLBiMdqplM5AKbHyZNkm3NXKnySnmJLvXuvZePhxGs7X3gnS-DD_QOBkB8804DfZYuvq6syTXGQevQYpGGhB7zg8M9q3yI6jfhNcyv162Wrw6e3vBwVLgtkry9W_6rwRmCPXNHaHuKC9P1Zl6ZVtGmJ7NBffn6804tn8biRq8F9Utc_M17ILEPwCv2fJ3r8gYCD7gmnz8NPJd9elcS1hLI3tXilR01B3kd2PP1EszWpf_Cs-wdzq4TGSBtNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xmo6EWmEfUdlpG5Oe2EZGCLHuCt5B1idkymukFMaEkWBzrM9Uhc1_mqeYXbAlNe9xaNLF6ss72iCgC99SLAQBjp4gTNTSjpn8IB1Lk9ed5JV4QkBTIxWO3CyRkYQ367ZwMVuARPPo7g4qaxPoITifV1dEVuUfiDgCs3LaboQytUVuIW7YNTmOoBmhokZLTHkvst3NBog76_01MSBEJHu5ZKrNQx9GjQdJWLC7HwJnOPTsrpYmgvqdjOhImLb7NmEHVMORYpQbmEVb11CmFbQwkddX-o8pTSmAfFcFbByEgAeadRv1lnnX1wQc2L8Irz0b4ci_yEqVogKcDPAja6Pcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBjJfSsbwQPIXKGDbILiORmKUaUXYt4Mdz-9DF5eB_QZ5W-xzregfZR3E4LAhTvG4eRTltdhjH4r2rTs_y3YpQYCipyZ9c7n6qKdiySNdwY_XIEXgGkswHqcmg_9if0jkGKhEkYFDvemUR-tiXdoOekx1HIVgFgfAfJH7sV4OlrX3W1x2rBxREttbPXkHFvs1OPzdAnttikk4vXHc8npAYygTu7Yj6zzZKjgPH0QjiMEUAlL-MYM67EbbukgL688Ybt36s8hcZRBAx_DkjB7bCPiVWob6NOHgo28JnvwZkVugQtC_11VpbD_6S3xihf9Uj_J01cLLUSq_fC8pBv7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzKlNOfYKVBOR2hkEvN7TdTChQJKrxSXm3M9CN8K4VG6XS0RO0W1jP_57_cP-dqIFXuW3Dko3wo1z9D5HoQzb9AzwWZClQ71OplQ_3QY1N3XKn7AeyGMDG3Ds42R-Tn_W5AqpBAB_qQqVSXnztKCKM77_K2gvFm7CNXKxX7ykCCgQXqu-M_92lFkVaStJ-lxcP9s06MR3YXJeMaZ_MPZiIcnnwU67IbIk9n_ybLFvXDXtm7SE64O3SMZ9L6FbIFUfZ0pkVkyeIMkLlAY6Xzhlot8QCBPpyYUNTen6dW-l4LNgsZxfiBYmEczVp4ErJDRWzDT07b5f0hvjBF2XRJT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfS_FmO-5WldmX23nERWfwJDKSj4NylaeQQ_XGzWnpWXjwWAXxffD_Q-zuLQZWgVcYkbJSTSGkCZ-F0D96xG8zowEx7N42aX-sfdJEC_5b3w_ShPykKBQp74C2r0Rroxhf_kksTa3rsb72vwSTX3cyx3XigJm2qCavlYh1vvcT44cy9OJyIbCx_rfhbT1F1S_JVvga5xfkvhY-_KQ_znfUQ2tClMUYsOx1LvwiJUefmHPk9w23fKtAOnzCdUSKzYEWhfrPZ8NSvO3QuiDu8vlr15lplskfLM0aw7ReidZ1SPLE9b0-1oGcbRXL0RReV-JTxIDFoTjVrOjXpPrBhW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oElhxtrIdccbz1I8xgGGxaeHDJA5830Oo0FyV67vpLUmrXmTPN1AVZRRVNGhdHrR4hSu0wSF4KCnmILESmLwM-a7OcNbSZrq4EhA7c9BZFLa_5Vi3vSK45gQ9wVxhPLj4y242BkvTZhvUDKCnn-Z6XMf85Ypj3DncG23ZQOiF3RGQzdQ1kMKzhvJwctecpT-qAM6l2xU3B1ISn8xo7JPQybisyyap-QZ6mRnRkW7zZI_VBTFTnv8CwGsHorvsRStqpXk5knkk-dO1uU2jhke4TcZ2Wzknc3RKWOgZ-PTq0p8oitBzquK7cnJDcGOhO6CsUkcg6ZsrtX1EFjiSpeMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaVFeOsJdG843V462REB2dJnQuvkzV0a1udls3sLWvNNt3WsGRK481LGP256mxe1g8X_aPcDIb5QqaXxC0uKTLzWMEw3IRuUsbsWcw4fJ7Xe2hrPcEsDQOj2_YJuv3W0D9AprPC0ZrSHNtv7HHD6vHzuHmUF2GQfU-xag20Yc3zohCGBLcwEo_K18qgeLLdBeM-iOYxfmbMqTTHjTj-s30ipXEKCZPIhVO7XQf98c6ZY2tbhkGTI0XzhIUTlcUNcyJ5I4gHB3-bjHfC6hemcPX7hc3vPeTBVgJE5VMX-J_wBJivedJNGOyJSGTjpKNpsJwe7qJTcMuwDz56RLi0n1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nMMDwG4tY7wnAH_oiPcAva7oh1aUfryENn70E_2rGeXgcwCFjdWtJPbuX423JZlrUcMz6RTBEMvu06NVnvZAi-cIVZKvGXSVIjEFu9s_NoRvJLtbPkfoExvR3eJdCLAbXHGsPZCPQhJxKNTlCo8B744irYXbuhPSJHPpK97ZwAgxJQxCBohhGZb-JNc0fMyynF-011tKMRX2MqJeWg1YJ6KXlEghkF-rFpO7JoanfFJyIa8OR_JH6eWmfCWOau829nKWMVT8wdj_PX-XSTJuNh47O8O1zL74vLgquUI3sKUVT_w1kySLGaxV2lS7Lox7wG_7wviuahIMyKzFpsRxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ajs17MYOA3G5TZcRfvcbT2zsM2mEW4e3mi7ArFFm-TSo4KdDkdm0QTgy91y9-T6QWWL5tnvHNNxjESxkJ2pMA-40D9Q4zxXnGwoXlDr9t0r5fneOQFjhNpFcwCg6XlUfdjEnRd6icdNAZa9078yWMkQAre8zGUsvK5LX6F2Nv-AdC_73lJVxuSxdsiVPasm9REuBbSAZ4KDeMH4bujG1AbSZauZ_-WKMwdN-nyPfmc30tKwC3QdWzz49LRg2LfyLU3fphX4Oe7jv259P8fGilzg4Gb1bLDzVvrQmB_O-piTQIK_Xa4TMWZu2bsr8ofbKDFi0llDm16u5SF64xw55Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xp8etlwdrz-DJRHxGzlh4bi9RGnurJJK3jBnpnYnSDChLu7J9vQNvGsjBfqoQuv2Y8ArVlMFhsKaLqQi0AChSGBaOx7uPjjCup4OdGo1xIvwmG2kNwkx3tNEUaibYLfNuFcr4eMf2htRM4ZxF3XBunpgNGrMp1AxQXdUeNmXWy0MMfAlWNcUamgXHkC2SaWWbqbBGYR-0hOWJ6zLM3xJ6Fasd6JYlPG0powJCUriWBoKbHQnCP8OiNpgsoIABedbXbKtdqzS8WpkT9ZXSl7Arfz8nhdcQFFsH87oGoKJWHJouaduyXzAV5Qd8WlGaGg0CoQvZ_GHFr-ua0tga7yCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrMCDPKRqhtWLMA6xoigntiK-KQKQ_DdSbAZZe2xBElemAf5tq0hd4fGeTOs-wvtU5BtuwCyD8gXyRW3q8ZYugeGOC1RexjJOmDkh89Oo3_KSqTEgR_GuxXzZzeAMa8YchjcS9he63HvICwr7erMwEhgQ8Af9Y4D0jtzbM65JFvFf4gcU5JePBkY-AzfS0rIvFz3hUkXlYrt5R2Z-vSpIDE4810kAJrVn9oPwxek1LHhl5EXI8Z4EUem0pZFpMlbPcy9mZQ-lo1rD8QcH-lLBFAYXhcdctVqOERsDYp3lxg4eeyx7dfdoFKuM7BmoGAxLRrhcPPWXtcZ0aNWxWtIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pS4AfDXSsOpCbZhqJEl2t9bYj8ZN27ZM2i95lUJZ0OOqrORmP0lpVrSzyHpsLqFnBVlmo43sfPJpIptefNQ_lp6SPsR1a2vLMRgtqDbBJ0JCPebkYLTu78-2bKGjG3H8lAeDTNzgO5ezf83GOOGuT-wNpPO1dVG0Q5MhKbo4WF5hvTAvJTm4swmHq57x_rEXTXfn-5LgEqQmVbbB2YcR7V4nAOJGXToMUhvMmxHpApeWXsX7CiPnOzaozDz_IdZQYQQZe93eUHFfIxjned1MXU_srFKuvVJahK7g38YPwHu9UoPoHmB2stLVlF4WRGkXvnmu7NUh2i_aBl3ha0JExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FDyxJ6at4HXXnDylqebkcckD_72Q30CNf8Kj0LTO4vtcOiGxNkT14yus8uecE7hcjBrSxhJmURusWUyDUxdVFFb3Wo-Gz7lSjC7aGGOQNYK-yxFdg_8XMPp90gpwQ6J4_HW-JL5_R8D6TFf85w_IuicTv2J7oztUgq8SinHPYi_VMxA8gK3o32vMdcjQpf4yuaGwFVfrV5YeW6zl5WfYK9wJxQsZOrvDpWM0P17EeKz_zwPzc45UC1aR3r7IU1pOmJEUSJYqehh28P-3h1W8QJYu9tkIVbRLHZ29CYdFLAlq7WRa1a_k9GDQqw9QTaWJv9S2MGKJlKBDjPrBOF-zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kAkh8R8lCC1XZSb2emGsNcjp2YNC0mumKa5w9nbQH18GpYRfBY15TYGvLNZNnQbD9HvhctFhD9TG72di0dvUkOrCYW6gykVMgAzbRB40lAM-75I3h7vfyI2u6hKdRLS8Iyk8J9R9Fy8RHsxKj2A6qnKa7uVomovfb80idsG5Fbd9znseqLOR8yLnZAOOiXG5uppbz-Q7meUBDu4jojouBMOwgXtFBNjlBTQoxqNlbgpCUcBJqNgyIGJhH2S6Fp6JRSK7U17Xd2MwT6EXpK3UrArZK0X07LPh2FTPod7AG6WnZmyiTB0dndr-e-SYpfQLbS1UBFDTt10Ls55gH0w7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDFi5cQFvfyi_lbv1ltEfRn_ZRz9c4ezZb2WyDiVq5gW_CHDtV-gzQtmOpAiKz4B5wF7WpVVGT2HFE4Q4rwTlA69uqEttKhdkIuFqfwumTQcQa1LyGQ2B8XoRHXD36RSjgD1YnlQ9HgepCHCkb-VfOh-SsHfC4xw0nbZay_CFamS1VCks4sTm46-RP4zbDUkk8wNvjt7DxjossdxuMyPUOfuwNbYsDZOHHtPUvlVfCcWyBvT9i5jsRd85Huus4BhnCxUav00vawKcAlpC0i5O9WNhnMAHA9eMOMkMhAdXtUDZYfM1RgwgseqYDgQIuylsgrnkyG4Csnr6WITF8oshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EOJDetY1cGtcAb0RkkV0TkRXCJktZy--Gor9Tg102HVD0_nepbrXFDR5y6hdNTUDEhHiOVStVZ9w2rKqoTmyE25YhtlRDSgu3YzxZ_3r0m00x-58PZZnybtK3KUMN3BdXbpdX-xfqOQCRKm65D-p8MnHzCe8Kmij_WOwSvpshZOgDY33vDRl2b1PztzASW-5WW2o-TeA-n9Zgamj9FF5OWi6DX9XlXqaT7HRF2MORTiGroFFxySqDFacJHg37Zxcvd7QHyiUIXZmWAeysLts913JT9JTdWVY-pDCo9C2z7_cWtunusHqK78wO2ZE-OpLt8mJ7-9WIQn--AaPe-r47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/djMFqWpaQvXp0TMXWaX0Us2JGA_gz_Y-Wb3J47ihhMl-KqROOH_TFn_R2gOvLa3dYiLZb4vabfy590gCv0LFSCc5KXSav8hwlqFnjS4pjbXSzVGJ8Cvdl4V312G23uP8yfwfR-xI7sXNpT7vr_o09T8GEkM4IuO9_vhcfSc4G4_vWaQlZIjeYke_keCuRyzALKxZdvY52qSaOrU0KvL7FBFhcfFao87_B3xOE1Ij5Xjj5zHgn6pGfDQzf5IcqPv-rbL_xS-DqGqULWTQx9Sy-6spqAEl8NW9KnVvKQq3kYtI7QDD3vpZL4X6QjvJQQXUcSGCJfh8J9c6lHNNNMnaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdPpb5-OCj3lOGC3Wm06_cynK6UcWAca4HAyqYkptnsSLZ7P9kNt17PCEw0aaZ1eCJ8esCjIen_r0avB17lCf_2WQof3VF0RIJBSYJqbKNeOo0iJUVlciZkzLPsHdCZEupV8r2qN40L4YDkplWjoTUEYDUwJGu8zIhCucomzg4VrRU8XmcBNiUlzZeGJFEzrzQ1TKIy-VD7Ykab5NmkfWcrFWPGcNWIp7ndkbJBcpKlXLlKpDTReBo6b3rE6ef2jvcybw4f6_PUjrMpedUGcOhzUh4kfDgGZckXpbO1J_CvVB4aJ40nNt8afccwGphODfVDuokkb_E5YfEFx_eh49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOO434BbOfhC0qGWfI177D5rq-k4hQjJn8GMdJjN14rmIOSmQokVGRA9ihIdZNAsA9g-dWWqz8VOuXCisFJQuhQcgXPJeYCP6gg5JaT1IPCkb76e8-Jqx1ucvMTjN2Rz5PwMYJrh-Qwnsbsy33kp_21vAjE27PIrTROvaWQ5F_DVGoK2Cd4LZ9J6A5qmRDuLnI3NYoWaRNFsqghhEL8J1xefO0VilWo-dSyiygBW6zv5B7E50QOGQauyGjF4Z5lE2ntvu0Bpl-bvTUkZVy_OK3VDtQEj3AE8zIqJosld4W-60H__hE2HEEsonCx2Y4EDrlsO_aO5QPuZ0W1K4t-CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=utdox7IbHt2IZDiebWrrxyojgZafQrK7QO2yzV_gmXlzQJRYLYtaufLy9b0MMaGPYAO5mnVv1CPVMfIu2WdprnG6rL8R0r-hfO3uHN8N3knamnY4R8YT00xJJBSuZgHa_I5RNfaZUqJUgm_UaCoyG4I3uOmb_7NnLiFyNLBDv8r-B4954S8VL9qr9wVaCa1N1QHtUlMFWTk1LQeCIymLvwdz97fodmgkKreto70lGWfYlsHqDqCF-XHr7nHraERyLz-uZiyJqi_TfrHuTK6rM1fnktGO4m91S1bNyURIQthLO8nsw6ACkwyzg6Q5yCaeK14wHQqGrD91ha3ZwLHaMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=utdox7IbHt2IZDiebWrrxyojgZafQrK7QO2yzV_gmXlzQJRYLYtaufLy9b0MMaGPYAO5mnVv1CPVMfIu2WdprnG6rL8R0r-hfO3uHN8N3knamnY4R8YT00xJJBSuZgHa_I5RNfaZUqJUgm_UaCoyG4I3uOmb_7NnLiFyNLBDv8r-B4954S8VL9qr9wVaCa1N1QHtUlMFWTk1LQeCIymLvwdz97fodmgkKreto70lGWfYlsHqDqCF-XHr7nHraERyLz-uZiyJqi_TfrHuTK6rM1fnktGO4m91S1bNyURIQthLO8nsw6ACkwyzg6Q5yCaeK14wHQqGrD91ha3ZwLHaMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrvZ35Yth5INlcjEhmAZA0_gMtbGlihtvahAH1xRh2xsNES_IzppaHh4QFcdNXW_oFigMGNPS11_DFyub-4lN7yAaiURpHkIQC9Vu9TGYRNuv14Tp1f9fbuLFZ3WE4LATh6ZKZNEUEVNz3gV9qVf7hOc8hsTi2wtoHNQzOlgSausXRlau7eOfYtR2kF1oPrHJ4pIPnzsRfRbhyd7utwMhD9CUtABaImHTRlT4J0VgVad4EFEYfx-VJVE7FYia_ofIN8qoqtlRaJBtPu19a48vAVeFZVgUCPup2gO-bo-GbLzU2_fHklMpQYLlr1wjDCpcMVIGmoPktrV2xqE3muDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0lJ-4UqBHATnHqqUKiv9AC_bicxqlwPH4WAmmdkKV4ClOD8TfvElgjTOSg_W3fcT0Bl0vjK-KGv-_79SliuDLNquvaDIo-RszjyB1fdFuQ1chUPZ3zKvQ4jwqUohQjsG013xOBvRffT11tWvZ4968HhoU_cNofcr8TxNbTtqGo_WNYJJJxg6k59u6-9CZjpK9H_kkOojphrrGizs6l-fV2TJ-SSFqKirqHFnASBG5tVXUjilRHDgv2YaKgXDw-AokDv3bxnxvqhGaDq9HgcRfAVohhVxnqVO7OGkm6wsBdo2c5BHaTpF4dQlCXXidp14DNkgX_wRHdNNE6zKBGdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FXa1ytpsi9DJh-uS2kSMtzEzgqPBRGTWpGKLwxSasmb8f_iRPhLRNNVPTfxsu4Vh3BJ6ttQRBEuW3iHQHkWWWms6TkrYxoMvrSBd97pNWKpA89io4xsE3ubFrs7K4t4ItkIZlYGLjhcjUUbjb4ivueIcaQ6Y73WnPwh0EnCxmP6eT7h4BBiMfksdZiVZjUDsFLG_R4Wme53NO4f_w4jjhezhytZcE5oGZGc16RywuA7Ew47qZaQWWCj1EAVmnTAuapEsxyTAUldNDn4Mq1EgYZa0bsOzGz88hwst7qpJnKaByt8e-ij-aUTJ5ZV4F5aHZ1c8BxthVbMXJa8N6ThSuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CftJ7DAfuRi0vWAv7WkOto5sSup5zjUBdUPqYmDJwwAhIB_nOrOkLzXARhiSU13Dc6i5vrPTgx2ICXRJZbV4zg8mN8a-GdAqOG1v--3q9ZTNXn_LZ0ApZsL-5r6BzM9Y_CjPadLJZeQXz6bgHjF6J6UqnOgIeYL7OSrPXZ0bigWbdC2tAkXNb_E51Ro_kY1hJXCqYb_FfhHQv1mFgAu56QcodXPYfdPFBBJc1yQDyKiMboSwr9_2M4kYgcuBYWcShq3HgHQaPnwa8xISwzzgUlnDSrcs91HwS8vGl8lSYGq0wrRk-y4BI24qsGwjgdbjfjLOef1Hzd2Tpn-VJ2gPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jESW4S5qIkHWP-pG9o047ppbgAMrLywizWHqZuhE2agb2bzYvOdT3ozi-NuFKf50O8ltMmXGRwE0QVobZTZtaAolC0kNIbLmc47_hszAMu9SEihBgOjEh4xWAR8rXCUoKnCI7jNjTAROZZzgLmiK-rJEtQEOL58OsshCRVUOFgyE5iTRO1dsqOqdHuAg8h11qvwsP87HdH0SJR5gigzaoRe72hkyLkFh0PESuZ6CByzKt2v8gjyp5XArx5QLHcF2fS-MDbNvu7PnE3aVgW4N32KzZXp7gtyDzpA2lI6HfpssX0Dqdg52ZYqD_24udW8yfjQb79NIM-IOlQgz8i2wrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G0gKag1P5MFBs_GG8EZ_z8mjw-1RJ-Qc9Ds3vDgoL_8Q6adZs68fZ8zsumebM6ayYN8sXdW5v-TXXsRDsy81usFneai5QvmFDDO7VLcZayywTk-hT_enq6IWYSWbENiWWvoszz3iC1k-EzDqP8IfP9OZ2hF0iycVox3qkisJ2WAqbptn3fDt0KBwTkoYHvUXiWjify7E4UxsEX5YmQPwxPa439VYAmOjCHRhrLRIwAzad6UIxov1zfCMaWf7VDeJkpTuZiGmpCAjgy5gmidKbwhGTCOrzP3LRe8t3kxKI1Kkp8hIePQZkXckOSRNTxjIWC2O16QRWGAO-t5e5fQQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAKuxYbm_1IJ-sLWu50Rs1HjXPHjiA1D0Z_7gTRkDomIwJmImnP-IEc0Oig8UAAhIeALtExsXebYjmXzbGoSN5ghhLlSDTaSwmshRbO6Plj2HYqkFRKP1Nd-J7JaFEC5O-sZLPShrLcUx-UkHaew_m4zzv1GJPp63nWmiPqgS4XjiWkAxD1xpoWIvAU6MZsh_f2Qfect5oB-rOYKwssUWxtRidxicYbiv4dc7dBkhSsWA9x5xgyNxfe2mKdB634ezCzWDRgDCbjK2zwXq6b9BEszaM1wnw3t4sjuXMHgTK1IbZX-Id0mXmHUcPqAQDx7N23zYDZOIW6n-kQTrMyuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlvntGvKcsSbLY3aO8dh-Oj3WYJzT48uxSA6I3D_Bv93vgSLTuVRgujiYJYj63mQ96T4zlwq7b4mytBUG_sGIQBXY8jiIxlGrUl0VgFe7hg9qgIcosGNF5bj5WNb9TOXWs8C-K7Qit_VuEiDXMOXWmArB8dzXiDyVvfkLAFJLwLaX4HcXXEd25IUuvVgsYgsbW-hK9QOwZlIVUjYQxr2-2VZQsSqN_78AeXF6N1_GvWKUIYhpCnyMj1hwUqvCRfX6mIWIjtNCc0iW0uiOqAUexTWtqXRC5lhtS_vtR_Fl0Ua_4y4BxzsEAd4vePhUaovY74DQ1P0LaeXnfXxQ_7R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fVBbDUfbxfjBBK6K1V-Efs41mqNN-bcthln6QfBSBTzUoGXl95_EDAi8jS4VikeczunPElqxiftqOPShX7MPcXSEyI4cNZw1sMdWYCNwxCJZzq2-J1vTJUBqkdbiFLQ48oBI5tvMz80XDiqu_fP5VyvcLbTLUrd_5GLe9nFqV2VYQXaXB8pDfik8MJZvG8rb9LLKQW_C193csldZsk0zDb_rp0J3GgEvzUhr7Nb7pcalpaFir2O_0x5v_7R8UwYLbbKRg9hgM3HBa2Eq8fXwI5STi7EeO-dwhVxvbcPqMMNd0r_oyUI3XfWzDO84TlT7cf-Wz7mgWP6AkGSo4Qz6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D2gGK_ZM8QHMFXcXm0QCk2GJG3YqMj1FrHPXMwBnJKPcM-Fq5i7ykpZnVz7f15qDKdKwH9uFvmmO9h2tq1j2-DPfyCpqW5WJoiEMm7dOS6bq9FndN2Ha0Yqmulr7-BnUEQd1qzpr3BPHGYITjKIHp1jaNjis8dzSmCEii0lB0zE-uFkiojFcFACEvy9Y_NtNI9fPmgaQq8dmgfKT4TfpAskMaBdmDEuohSvBLkvZKtRbuXm-IGxRMVv4XHzZvVlBpfA2JSa20o0dXuH8qQxnAf5dXKWnf25YZnOxvM547i4Lwca0raTeoIeMtrllGtKnNSlcngujjw_LCZn0vR6gsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
