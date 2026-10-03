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
<img src="https://cdn4.telesco.pe/file/BSao45F0BMJ29sK_hD1E8f8kicSAKpqlvgrT6-VASBGzoZsx59tyrT31D3vnYUFXvdyT75NaDLWlWUXT2DVL0QQyzUHDNe_wQRk1UHU_zfUUjni4Vtquffw3oPNAxCLEmgfi24FwE2EyPZvLDwplJyg0_K3LuOY7qKK-BXD4495Ct_LbCvmQjK8BwOZF9ctt3dk9B4uYpefHj3UX00TW6OVHwmindZuECD7-CQiv7jSR-Asd8RZIjdYFM5JE3hLxNo0S8zrEjBMEStGJoNLx8D4PztxMoop9beFTFXHPky994EM1TcP12Ms5RGpNp0MmbiNZaVqVRwSxV1X1GqSITQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSimbaServer | سیمبا سرور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpu6_4XbVhnkjqxUwzV8Ru85gp02UC2CeXiJ1GWsoyxPcS3J0xVCRfE6ju_dPaVJRrtYEzkNFKhPP0aE7ylp1589VFGuP_tEwRq8Kll0aKXsKUGY2F5H57W3WQ9D0XNV89Eu_8NS6sR_0_pCxE1EXX-r4WumSRwYEXBLtB-rzViS74MygZn81rojMwd-dRrMFPxElxSDd1rM-PqHXJlfe96yyCvEk-1FLTf-Xifb3xrVCRUB41O2xex0kkdQA13rPcQbhRkGQ3DMKF4c_F1cwzobl0O42PX4duPTHzhb1LMwwlfAMWSj-CpXH48IW940Y1YiIi-2dEqQuTCAsgv2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
سرور مجازی ایران | سیمبا سرور
🖥
شروع قیمت سرورها از
۶۰۰ هزار تومان
🎁
۲۰٪ تخفیف روی سرورهای مجازی
با کد
SIMBA20
📦
هر ترابایت ترافیک:
۶۹۰ هزار تومان
⬆️
آپلود رایگان
♾
ترافیک بدون تاریخ انقضا
🌐
IPv6 روی تمام سرورها
✅
بدون مالیات
🛒
سفارش:
SimbaServer.ir
💬
پشتیبانی:
SimbaServerAdmin@</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/iaghapour/3087" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLFEo1dAPYFRMEVkNUCqdeytjxy-Lk-jfKbNd-xMvR6jDMWcl3TIOfi6fYljxJBc89II5fyg-6YOHwZMYp5BPWQXzpbv9XCvDf-sE2O4D01WxBWhvlLovmFslT8tkwCM9unxgbu5BkurBYSi4gCRrlFh9Mt3694OHnEORK9qGXGzqfIwLSasCSd-s0EhG0E7yZDsFz1ykRmhE65ps9DX6yY0SXcuXfx1Gb2-0Xs5tS2DryywM23yWlPnhKDHrn8L2FVtvVAxChEtT7RRIK_Hmq3Z_RD7urbxlVy1LaOszOvvoolj6HMdolC1GZ5KH480jo5p_F5dFb4A1uRL5Q8HXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تانل بین سرور ایران و خارج با پنل پیشرفته GRE
🔹
تو این ویدیو یک پنل گرافیکی و فوق‌العاده حرفه‌ای رو معرفی می‌کنیم که تمام مراحل پیچیده تانلینگ رو براتون ساده کرده. با استفاده از این اسکریپت می‌تونید به راحتی تانل GRE رو با قابلیت‌های عالی مثل پورت فورواردینگ پیشرفته، لود بالانسینگ و اتصال سریع با کد جفت‌‌سازی راه‌اندازی کنید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#gre
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/iaghapour/3086" target="_blank">📅 17:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA1ZrDEJUUx46w7wNgM1h-gaUdjwpP0q0E_ojhXCw56vO_cDidKb8pHwLGJdUdluDaZlCargK729V4vkwBy905wIvOKjwdvuyhvkeuEXVPdAtHPgeqJXuKbT4YffJLtOtdRGMneHKY1eHaIr1E454ssWs5Ct_VTab7V3-ZgEtKGZI59TyWUDFEGnmQcC9sFWfAsBc_cgGB8_gLZUu6TM918ZEChNno2ivaiOts0ya7VbyvvQTc_zurya7X4Vok3aKRkK0WpQ5Cgw9S2TxyP3Uov1jnwlC056w6t8jULjaUVwoVueEB0Mh_9IIHuIdBmXiXsf9PZjF_O4gOpSwqYFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی افزونه Xray for Chrome؛ مدیریت هوشمند پروکسی‌ها مستقیماً در مرورگر!
این ابزار از دو بخش «افزونه کروم» و «برنامه همراه روی سیستم» تشکیل شده، به شما این امکان را می‌دهد که کانکشن‌های Xray خود را به سادگی و فقط برای مرورگر کروم مدیریت کنید.
🔹
پروکسی اختصاصی کروم:
ترافیک فقط و فقط از مرورگر کروم عبور می‌کند و تنظیمات پروکسی کل سیستم‌عامل (ویندوز یا مک) دست‌نخورده باقی می‌ماند.
⚡️
سازگاری با VLESS, VMess, Shadowsocks و Trojan.
🔗
امکان افزودن دستی لینک‌ها (یک یا چند لینک) و همچنین پشتیبانی کامل از لینک‌های اشتراک (Subscription) با قابلیت به‌‌روزرسانی خودکار.
⏱️
تست واقعی Latency سرورها از طریق HTTPS بدون اینکه نیاز باشد به آن‌ها متصل شوید یا اتصال فعلی‌تان قطع شود.
🛡
جلوگیری از نشت اطلاعات (IP Leak) با مسدود کردن اتصالات WebRTC غیرپروکسی‌شده.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
📌
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/iaghapour/3085" target="_blank">📅 16:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e754doBNYgmGy9QXhAwsb--pZ6RlL8CV1gMwkLN2CjYClTNoWMgvbFDHjzTRM_zUhHIW03KrN7p3EiL0hTZHfFmSkCYC9i0kTOpcLxp0bSb0mSczGS98MQ5Jf90Z0U1FcY0q5wlLWwVVFZOzYDd_4Z7c3Br5JljkeO2tm3VDbpvT9ZYYCkjRWZA3ThN1mn1AD_3HP1rU-0F3Cul-4LbYzdH9M_H2ThCIhwLQyhqf29kuKhmgCjXxG3_R1jpxuh_D_rRozLhc4V7F5FnBZMbBSmt81ucjML6MR7WqJDClIPmw3mtwj6wIeohzC2P6DozY33xnV_DzK62_hSd-sKaNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ پنل W-UI به نسخه ۲.۶.۰ منتشر شد!
این به‌‌روزرسانی با تمرکز بر سیستم نمایندگی (Reseller)، مدیریت دسته‌ای کاربران و ارتقای امنیت منتشر شده است:
🔹
سیستم پیشرفته نمایندگی (Reseller):
امکان تعریف لاگین اختصاصی برای هر نماینده با محدودیت ترافیک، زمان و سقف تعداد کاربر؛ با قابلیت زمان‌بندی میلادی/شمسی، دسته‌بندی در گروه‌های مجزا و اعمال تغییرات گروهی.
🔹
عملیات گروهی روی کاربران:
افزایش یا کسر حجم و زمان کاربران به‌صورت دسته‌جمعی (با پیش‌نمایش قبل از اعمال)، بازنشانی گروهی کلیدها و لینک ساب، و امکان حضور یک کاربر در چند گروه مختلف.
🔹
بکاپ خودکار به تلگرام:
زمان‌بندی ارسال خودکار فایل پشتیبان به بات تلگرام (روزانه، هفتگی یا کران‌جاب) با جزئیات کامل سرور و حجم.
🔹
ارتقای امنیت و پایداری:
بازیابی خودکار قوانین فایروال در صورت ریست، محافظت Rate-limit روی تغییر رمز و 2FA، رفع کامل تداخل با داکر و دیتابیس، آپدیت مستقیم درون‌پنل با یک کلیک و فونت فارسی وزیرمتن.
🔗
لینک دانلود و گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/iaghapour/3084" target="_blank">📅 15:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/iaghapour/3083" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTmcewjKq-kBdR-4L-ndM4m0XNgjdn-doH14bihMDmTxmOn_pUMf0Akr0cGyd81jOa-gxYkmBZyD-VLGoFhzCnjfk_UixNWc_9rk1G8oy2kXeX01yZEUif7lixp9bMnMrSPy5mXz56bjpXwpRoZ1XoofzXm8emZ_bYcWMKkDD7G1AMkvaF7SSv7EaUGsSjw8w9Fft8kp330ISXDXkhO4YkJgaJCjT53e97Dq7BMu5A8McLkmGWn8Faio8gGpe9-kjss644Z8e-jla54u_Py5mjBsaNEoGzm9HZPyAyBWBQ-Bqfxgmaz2WE6-nSwO88U6Wub6MOLZ8Preb0mT_6JMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV0jBEiA8SFweEZDALKyOrHERSvrF4M8k6A6X96XZl1SIlS27Wp03D6YT2AQLi-wJwI2quomp7J0haqOR65vMnkbPPvL7HwGEA2x4PFYHc6_o9_dYtVSVZ9JRUtOWqwYVtJxAh9ajh9cqC1IlgEiul9tphA5HOgLsimbG6gjAP6NqdUAHEmCqE030XIVaQGpjmYUIAcKUq02mXWwAvFSiNqVXaJq-6hyRvKWdvh8-JzivlsJKz9gUz47MwdiubJxX5L1dnK6z2jrC0Sjw3s9vzx5rPEoyfv9YfYD4J0H6jg8Ge365R675ie1fBPMZkmlfix0Rk_GZ6u8kVcVD56iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Row-Template؛ قالب‌های شیک، امن برای صفحات سابسکریپشن
اگر از پنل‌های
3X-UI
،
PasarGuard
یا
Rebecca
استفاده می‌کنید، با پروژه
Row-Template
می‌توانید صفحه سابسکریپشن پیش‌فرض پنل را به یک لندینگ مدرن و کاملاً اختصاصی تبدیل کنید.
🔹
۱۷ قالب متنوع در قالب تک‌فایل:
هر قالب یک فایل HTML مستقل و بدون نیاز به منابع خارجی است (اسکریپت‌ها، فونت‌ها و کد QR درون خود صفحه پردازش می‌شوند).
🔸
امنیت و حریم خصوصی بالا:
بدون ارسال هیچ‌گونه ریکوئست به سرورهای شخص ثالث؛ تولید QR کد و اطلاعات مستقیماً روی مرورگر کاربر انجام می‌شود.
🔹
کاملاً وایت‌لیبل (White-Label):
امکان قرار دادن لوگو، نام برند و لینک پشتیبانی اختصاصی شما بدون نامی از تمپلیت.
🔹
امکانات کاربردی برای مشترکین:
نمایش مصرف ترافیک و تاریخ انقضا، دکمه اتصال با یک لمس به کلاینت‌ها (v2rayNG، Happ، Streisand، Clash Verge، v2rayN و...)، تفکیک سرورها بر اساس پرچم کشور و پشتیبانی از ۵ زبان از جمله فارسی (RTL).
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/iaghapour/3080" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEiNCYq_yJIzhZV9uCcDZXpQ7AGY_GKvXJFdrNrloZgaclOrV18KhTd0NxLPusydgJP7VxDbElTahe6r6Dnb9OY04LzxfoDlel3ptJh6PlwYYNZ_h7xFd8IZ4bV5yVXok1WRD5Dgq6PytxTiNu3DPNHI6j1hGoFsnYg5l7mrID7UetRwsv3hd3Oz-N_-NoyUfp4wjU3Qj49b2aGsSTqplfkLxwufmbOLeBoe_PTk7emK8PWAJDHzOiK3TRKESIqWz1ipcMOYySwMGMqnDAvAtTW8UZEy3u8_WMwyjHAc0wWCqtnOBp5Ve0WYVh__pGI3vRTma1XhKZQ_dBANEiK6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aESy4Qt4Ve40hmbWTgdya2EuRU96ISSK2xNfCrBsxy5qeqcLFs_NVJG-5MrCv8vu8Z8tzqVRNd7Dsv2o9jZW0nOH7sPhEpU70eQ1aEKJKjaeDlF6khIXZQrozz5hKvFK7FVOYJZWRRtYBTDHDilDK3zj5nu5mOjTbMlhLvDcCR4E0zTKjfo9QDvpFsc_LecJHYK1q2gbNOMX0I-yLXhxoVzgJ7Ruh0DSBR-LLDAVyUoaymtVVizUQGI3js72dDr3CV-MSSPmY9e6Q1Q34A7qbfaWI-3zofdNI1EjDK72z6znsv9V_cfakibkAjcCwXkqQI-mtZF53zrP-jgBnNkSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه ۱۳ هیدیفای منیجر (Hiddify Manager v13) منتشر شد!
بزرگ‌ترین آپدیت هیدیفای با پنل مدیریت متمرکز و کنترل کامل روی جزئیات کانفیگ‌ها در دسترس قرار گرفت:
🔹
مدیریت Multi-Node پایدار:
فعالیت خودکار و مستقل نودها حتی در زمان قطع ارتباط با پنل اصلی و سینک پس از اتصال مجدد.
🔸
تفکیک آپلود و دانلود (Split XHTTP):
امکان تنظیم مسیرهای مجزا (مثلاً آپلود از تانل ایران و دانلود از Reality یا Cloudflare).
🔹
موتور جدید با هسته Xray و sing-box:
پشتیبانی از ۲۱۸ حالت پیش‌فرض و پروتکل‌های جدید مثل AnyTLS، Snell و SOCKS.
🔸
تونل‌های DNS یکپارچه:
ادغام پروتکل‌های MasterDnsVPN، Slipstream و VayDNS.
🔹
بهینه‌سازی عمیق:
۵۰٪ کاهش مصرف رم، شتاب‌دهی TLS، روتینگ بر اساس دامنه و تجمیع کل داده‌ها در مسیر
/opt/hiddify-manager/data
.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/iaghapour/3077" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk-mzZDxk2_BkHyd1vTROEy5FziZaAfJSprHu_VphlpN0p9ZXqXSXOoV_sdOyFsRbr4S9TjBBPhVRk7HsD-Xfj-xg-tQfwjmKtZEP9HZsMoXfYo0WupMaK9Uo16BxN7RVNi8dOhuwtKR0baVztX09ZKaArpXu-8YwLA2U5hpYXl-tGwX3IFKCo-K9-rtgLSGAY0OEOFBCaffzSZ7Ilq0FtLM2c9f3QyG9QnErAOuiXVeFdxcM1dB18nIrLQOzcvZS3fou7-NwtZTOP6cxcXV7Jqwmt5EZ5vVAtuy2Delj1JnVrnIGmQiu-_Scy35y0gkY3pvb-UVhbjgA3OyNXolfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOoC1mJx5qO9Fe4yhN-fcZz52BE4OUmB5dG8NDPXqYInz3bibjhY-dspKCZRbU2hf9S0fHqqVgaT7TEmWKOa-djCAA0vsTGEfUlzEDjzoRXdcdAcj4jJcpNP88UOvlz5-Zygw9jIymLM2YEnL4WbvsZH8Z9q2YEsWmjTOuGHN42jTzjq4LnAdegrq3z-VR_ZChxZb1vrlpl0WAyYAiQq82TR-JLlBVJQ-8MtnUM8GMoiFs3hzp4-C5nnbW82dpwNVOZowgHONckrUcFMhZCTP4d2pm13WEJzDN3uARVjj6YTG_DZfLoS2UIdlqtipeGxRxf6P8b5NLSuY9UjNM1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beOfdKouCLPrutFlN3m5aaPTZT0pE6UeU3HRIXl5OjuB7vn7rJOlatTAuQQWXk7r2CEzg_b2PTZiKoTfnUICbodFHL7VhkVlMspQ5DmYbG47PRbY_zAp2fRbEdZyMORAAiaVBU5-7YviBUpHB6MG6pWYOHGTc9ipaKrCH0tNiJqfB5z52QasIQbEoIeYyuq95gIOrGqIhMB1jvwn_UYb6TGVPk-F8oFc3i9gN8AD-TFNaPxhCq9egSB-Sc3j-sXiCCepg_UjdxZ8KoXruFw2VVUxfMBSnuBGzYTQ-jOX2TWFRF17f4yBuMSrha8LFhtgsuR7sZ34qV4EQGgni4y_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qjqrv7Gsu8XJBJn4evfgoVBri9-Eij8Ja5O9uQE1oHB5ja6WJoEWmKHngn6VkzMkeLYwN0glbeVuT17vsIaxsLF62JPDvv2dfdjU2OaGFjvxD_1uCks_BrQYn9szQ7Df08AgXMoIQOSHTEyu5152Jp_Dr5A1RUleaLv2WOXm4b3iEXIQ7cWZEwCOAL57a9d88WRECUxyx6Q2r5SUUjrIEjsSmdFfFIfoO4vDgiik_-zVvzAyAX8AFudBBopPSlNfZ4bCJLHwnQ3E-kY6VVHM9Ss5ih1A_CF8Ol81ySEIlW2bM2NSKntcDL9_Y003J_3YWDJxkaCG3Znpld0qqhH40g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEe1wfYf9824BmAOMPU-GFk1XioD83mV-ZQ1Bo-_KZmdWimR-68F8_GpgiEvyAQpGboDE7h3qlUeW6DSg3oq70sCYppX_uWRyLDpT2h1obAl1_F_SU6hUBcdljKdMp6qfmbPo269SaYk2H7Lc8tIgduqbVGVaDMQjku5Kq2-NvMkn-B0pQj0S794-uvy3NuhavqOJt7JWY648UqXp2qu-GaP5j_V5swJ2esKeeyxcCi-bQI2nOMXkuel9Cx9yLylv36WHWZQivhQUGGf6PCbVg3A7cGehvkl-UrmbowU6MuSCc2x1ZomL6bSKECssDPkaVDj0ZorZIgim9kTko5pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون کامپیوتر فیلترشکن بساز! (مدیریت سرور با گوشی - اندروید و آیفون)
🔹
خیلی از شما درخواست کرده بودید که آموزش کار با سرور مجازی رو برای کسانی که کامپیوتر یا لپ‌تاپ ندارن بسازم. تو این ویدیو قراره یاد بگیریم چطوری فقط با استفاده از گوشی موبایل (چه اندروید و چه آیفون) به سرورمون متصل بشیم و صفر تا صد کارها رو انجام بدیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#گوشی
#سرور
#اندروید
#آیفون
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3067" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=MCJ4kGyQOPa0xIUnkBCpupeiRV8aTH9LrBTL1nas3f6EQrr5_VIklcQyx-c-0Kp9wHiUpFBP8qb8PzaYO9O8oSLXd5rDbdxVj__feDy4rZs6K0xz-Vx_K7RDjT-RA-bGMfhzRiuYV3WvkfJQM4onhNmL4D6y2Pdozo0Rum4urBkRmXhNxVjKVWoJS-RpFwUngfCarFso5usdxg4XGFrgPKggbEIOatvamPOTQp2GvEUnmNMoDM_wEdaQrqI2twOquSle61OWu0VquiUl6H_45X_mugMgNT3IvdcwGh5Nx3WRjBvTTQmnHt1DuN2SPdAx8yZCUH4Ucu9I0kmSOnYf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=MCJ4kGyQOPa0xIUnkBCpupeiRV8aTH9LrBTL1nas3f6EQrr5_VIklcQyx-c-0Kp9wHiUpFBP8qb8PzaYO9O8oSLXd5rDbdxVj__feDy4rZs6K0xz-Vx_K7RDjT-RA-bGMfhzRiuYV3WvkfJQM4onhNmL4D6y2Pdozo0Rum4urBkRmXhNxVjKVWoJS-RpFwUngfCarFso5usdxg4XGFrgPKggbEIOatvamPOTQp2GvEUnmNMoDM_wEdaQrqI2twOquSle61OWu0VquiUl6H_45X_mugMgNT3IvdcwGh5Nx3WRjBvTTQmnHt1DuN2SPdAx8yZCUH4Ucu9I0kmSOnYf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRpEj163UBVA5L5YjZh_Wik2bSqG_b-nmvgD0MIl537z6QcACb_GJEFBaxRPQHsiRn5vAgYRyv1sy88NP6Y6tfHKtFsN16ARiJZD2-q79NDwdJN8ctfNmtNWQaZuLwTb0thAyNZtvTasXK6X2f3yj2e47a0G1-uXg3cuK4VDSIkaIAwdTgYEnheYPgC22rkJe_CAeNq4gnTb8Z5Zg1EqTFSgEUnPVTPO2D8x49eSZBqUZAHLb-z72_l-3f_XjVzTbvk-hPRjX9NEG-KN6GNvWXz-sdfNECfi8J-5Bk3_gohg_9kigWPfPB3NAdINei6R-dVUgJ2-ZAGahk2u03kCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی VMTun؛ تانل کامل ترافیک ویندوز از طریق v2rayN و Xray
یک ابزار کم‌حجم برای ویندوز که پروکسی لوکال v2rayN/Xray را درست مانند WireGuard یا OpenVPN به تانل واقعی در سطح کل سیستم تبدیل می‌کند تا تمام نرم‌افزارها (حتی اپ‌های استور مایکروسافت و UWP) بدون نشت از آن رد شوند.
🔹
تانلینگ سراسری با Wintun و sing-box:
هدایت خودکار تمام ترافیک ویندوز از طریق مسیر پیش‌فرض و فیلترهای WFP به پورت ۱۰۸۰۸ v2rayN بدون نیاز به تنظیم پروکسی در برنامه‌ها.
🔸
جلوگیری از نشت اطلاعات:
بررسی و رفع نشت DNS، بستن نشت روت‌های IPv6، و مقایسه تایم‌زون و ریجن سیستم با سرور خروجی.
🔹
قابلیت Pro Connect:
فعال‌سازی هم‌زمان کیل‌سوئیچ فایروال ویندوز، بستن موقت IPv6 کارت‌های شبکه و بلاک کردن QUIC جهت رفع اختلال.
🔹
پایداری و بازگردانی خودکار:
برگشت امن تمامی تنظیمات شبکه پس از دیسکانکت یا کراش احتمالی (همراه با اسکریپت
Repair-Network.cmd
).
🔗
گیت‌هاب پروژه
🔻
این پروژه متن‌باز است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده سورس‌کدها را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3065" target="_blank">📅 15:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgWrsLyNh9AOH_bS-0MkPzVfCp794PcOVb4mYQSURV1cStkZojgFJsapMZgTCDLVxOkEcrXDrPa3u030USJmdcYd5HoflDcrDZjC_X1SQqAIbGhN_4WVvfN-vWH6iQL7QNSEqsZAoLkkiqI0hyzUTE71NYMsGnNieMK5b34olu_Etuaf6aedZQTA3rptplDK6KLM3rtolqDtLFyMt-6xkXcrfo5OipgKXJLByFzDCuSN_xsXUPL2Wf6bzeJmTkhPy2EXmlQmvCYtssIWE_J_Hr4coIuz-Fdm7JRrGo5L1C8fxrGM_5VQYrjfv5hLkRIHnrJ6rzDqJo4moRjWgr19Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMjTOQGlJe4aiK22F4a6VW96XHFeAqT3iYHXnHaTZyfqVddGBjRUbyEef9QFwbxaaatGODWdL2fu2274EHmQg9rju73Nc4kXfjQMBUERucgFHLhTQLgryYNhiY5x_YuP9IZE24G6tAgtuqHsFvurAiAEitJlEGZpxeJ29IUu41S9vQTTLywC53SQxsfLmiZrjNnXkAdef_yF_oeAhOe0QCRqUDcZoBj7PHMZb3blJ6_k8x5jPsWSu7WB1LB5vyE-20_oT1MRTTgEQI0h67jjiCNbxW7cm_CL891yKkNAmyYRmSYrKQFyzc0xuH5cAfmSEg59RrnN19D9PQSdRmYjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت نقشه راه جامع دسترسی به اینترنت آزاد
🔹
خیلی از دوستان جدیدی که به جمع ما اضافه میشن، همیشه می‌پرسن:
"از کجا باید شروع کنم؟"
و پیدا کردن آموزش مناسب بین ده‌ها ویدیوی یوتیوب کار سختیه.
ما حدود ۲ سال پیش یک صفحه اختصاصی برای حل این مشکل ساختیم، اما امروز این صفحه
یک آپدیت اساسی
دریافت کرد! هم ظاهر سایت کاملاً مدرن و مخصوص موبایل طراحی شده و هم تمام لینک‌ها و آموزش‌های جدید بهش اضافه شدن.
🎯
ویژگی‌های این صفحه:
🔸
دسته‌بندی ۶ گانه:
(از نقطه شروع تا ترفندها و تانل‌ها)
🔹
سطح‌بندی شده:
(مبتدی، متوسط، پیشرفته)
🔸
توضیحات کوتاه:
(توضیح اینکه هر آموزش به چه دردی می‌خوره)
💡
کاربران جدید:
این صفحه بهترین نقطه شروع شماست؛ از بخش اول شروع کنید و قدم به قدم پیش برید.
💡
کاربران قدیمی:
حتماً یه سر به صفحه بزنید، آموزش‌های تخصصی و ابزارهای جدیدی اضافه شده که احتمالاً ندیدید!
🔗
لینک صفحه راهنمای قدم به قدم
🔗
سورس کدهای صفحه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3062" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3060">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpP6Ykytcfo-PTijYw9yWOgkqv4DW70z2rZSITIMvt_PYdanEUblBwMKY3Ex8btSj9VX_4oAUd5n-bljsMtL2BbInH3D3wNBILrDlz2-cNz4pWTGkBlrNLTrIRE7T5guaQJbz7Kqzap3r1DUBYuO3GfwlHbsFOEbwE0zZ-pLRfwKK9VUvp7OQAcv4Ce9lBIrYL1orkO5TOvEkht5M6WTqEbOzf4-fPmj67K9ebmKMoh3xwkCedJK2yFkU-1XvZCfuoEXCc-3LOoQK2lSni2PiFWeXRebdjmbfPgemrRFp73o9PpAjnKIljd2cSy37OQkIBLp4FYS6oBPb40bBzEmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
بروزرسانی مهم: لیست جامع آموزش‌ها و ابزارها آپدیت شد!
اگر اخیراً به کانال اضافه شدید یا احساس می‌کنید حجم مطالب بالاست و سردرگم شدید، این پیام مخصوص شماست.
لیست راهنمای کانال با اضافه شدن آموزش‌های جدید و متدهای کاربردی به‌روز شد. این فهرست یک مسیر دسته‌بندی‌شده از تمام ابزارها، ترفندها و آموزش‌های تخصصی است.
🧭
پیشنهاد ویژه به افراد مبتدی و اعضای تازه‌وارد:
حتماً با
«بخش اول»
آغاز کنید تا قبل از هر اقدام فنی، مفاهیم پایه و نقشه راه را یاد بگیرید.
📌
لیست کامل در بالای کانال پین شده است؛
پیشنهاد می‌کنیم آن را ذخیره کنید تا در مواقع اختلال اینترنت همیشه در دسترستان باشد.
🔗
برای مشاهده لیست اینجا کلیک کنید
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3060" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZktWxmD_DhBqfiUM71gWMYdXXSHfVJUU2TuGvUbi_AukinN7WdfM4nT9N0H5o8SiGJE3EVSf8Ff7Elj9e-Ayb-ADWB-UQwvL8wmMTAC7f4NzLEDG23-pAHu1HfxDYT_EHesv-kp4OUo724yN4EqaDPh7CtyykTrLFoEC8XXas8-27WmzsFiUiUW-Hpt6FSDoIgHFjMTVH1gZsoqsFsnmYrLhOJjzn8wi0E3-rCXth3HWOmtpkiVg0vjZyLbFMlfWz8gLK0HWCHzZkNJGyGK1Sa41XVzjUpdFl1qZg8YRtphGs94ue6ffbXSwmE1qxpvvpBZITAxOlNQaFUhKz9Ip6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
رفقا یه نکته خیلی مهم درباره کامنت‌های یوتیوب، مخصوصاً وقتایی که قرعه‌کشی یا چالشی داریم:
🔹
خیلی وقتا پیش میاد که شما کامنت می‌ذارید، ولی یوتیوب اصلاً اون رو توی بخش عمومی نشون نمیده و مستقیم می‌فرستدش تو قسمت «بررسی دستی» (Held for review). حالا علتش چیه؟
۱.
کامنت گذاشتن در ثانیه‌های اول:
تا ویدیو پلی میشه سریع کامنت نذارید. یوتیوب به این حرکت شک می‌کنه و فکر می‌کنه ربات هستید. بذارید حداقل دو سه دقیقه از ویدیو بگذره و بعد نظرتون رو بنویسید.
۲.
کامنت‌های بی‌محتوا و تک‌کلمه‌ای:
متن‌هایی که شبیه اسپم هستن سریع فیلتر میشن. مثلاً طرف فقط نوشته «کامنت» یا یه ایموجی خالی و چند تا حرف بی‌معنی فرستاده. سعی کنید یه جمله معنادار یا نظرتون درباره ویدیو رو بنویسید.
راستش منم سیستمم طوری نیست که مدام بخش تایید دستی رو چک کنم و خیلی وقتا یادم میره؛ همین باعث میشه پیام‌هاتون یا خیلی دیر تایید بشه یا اصلاً به قرعه‌کشی نرسه. پس حتماً این دو تا مورد رو رعایت کنید. دم همه‌تون گرم!
👌🏻</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/3058" target="_blank">📅 20:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXNyVxnkQ-EbeYo5yGwSPQFx1q3cofhFJa2UuryZomwlkXyEN2HGDJicVR27RVCf7cLKohM6qydTXpKaOOYTn6L164lB-iQVfaJ9cZs7sSeS71tljoe1IxLaZlwf6hzJQx9dgx2hhtyl6v7Glj0c9P3lSASGaxmnGB3VGdLqV4t8jbxen2JVBL6js-fP3EA-fJEMk7h13FezANU5v-5HQfcPmXgMAscdBDayHIqPXta50f7OD4d2dYxCm4yLcQdszyfbPeyvwdunt4sksHbC7wfi-JUt813pK82365hjk5UBE6Najpo_cuh0cFfGsyevrRU0WUxkV5uPPLPgpN9mDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keya0UbKvmgCUNOxvnCUmVGjEM5WZMAGBKB3LDk892a2F_sVcjLKDZGaYPQls1OQatgac8yJFNDPvflF9QO1kjVfe6pvuVNuQthjJVrFp6Uv2fc3UJwY9cMtl7fU00n7BRB9vf4XV8PDxRr9yRL0NdbHEfZ6drDPcwgY3G7Hyox7kUoftk9qLa20Jh_mXLrvubfO1bBr1ZeoCDm5nMB3ArVZkjR5qDI86rzmId0WoDjvabBlnoo-hpP0x3loDO4WSRIcwZYrJA47kHO9MXI0GBxuyhO03XAGKLNp8FfaRettxYDsKVYaqbqFJusNPY0QeFKgkWSCcjwDpo_GNIjpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ufr1nEfoVRj-4wK4OlTjAv47P7afn6DE6aUl2D6Ga80xCGxEFG7XV-vGOGnDJSq-x-6KtHJtalWjQiLfXDd-qaHhXbBCGw0C8vNGoNAgYz4NScz2nfUZ8B_q59GpHjfhfQN3TO2nBFEZwJZWxeaaovq5l8441XN6XJcP2QLamhcUK4XkUDve0jueIFQSRBZvlwSlPxjFly4NIY72fzJB_8JdofQb6J01kmq7ko7p2-XINwEJxXp4okfSSKL16ek-hWhzwZTndk7pS2Pvot4JvbHXLz4X5DR6Y_UPalljvecAQYvZgp51wiA0Uuwol3egep6NCKVk8NRciAF5HTdB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی جعبه‌ابزار کاربردی مدیران سرور و دواپس
یک ابزار تحت وب و رایگان که تمام کانفیگ‌های کاربردی لینوکس را به‌صورت بهینه و استاندارد تولید می‌کند:
🔹
ستاپ اولیه سرور:
تولید اسکریپت شل برای امن‌سازی SSH، فعال‌سازی BBRv1/v3، فایروال، Fail2ban و نصب داکر.
🔸
تیونینگ TCP/IP و کرنل:
تنظیم بهینه
sysctl.conf
متناسب با رم و پهنای باند سرور، کاهش پکت‌لاس و بافربلوت.
🔹
کانفیگ Nginx:
ساخت پروکسی معکوس با TLS 1.3، پروتکل HTTP/3، سوکت و هدرهای امنیتی.
🔹
فایروال و روتینگ:
ساب‌نت ماشین، پورت فورواردینگ (NAT)، رفع تداخل داکر و خروجی مستقیم برای iptables و nftables.
🌐
آدرس وب‌سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3052" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZBWjJ5NuxPg7pjGsOmlDJ7zytzfphNdrD8Cj087NUpXVjuays6BskY1H5TiaFXwF6Q-8tXavMroHmIcPxMxXV54PN-yu9s26ZPnOKDAJyKNRAGmeATRSrk6zL0f6Xezlt0N3mUv7jd96r5NMCPLfbGZiq_tUCrzVAFb1hWhtrA-gQsWdXZSUIGvJ8LmlcV-FbXCAEE7WXJGR8qiR7dn40ZfMG4Mnzxn9e-eSPKrjG8JFZuE5OJYuS-KPO8k_vCngpP7kWkskmx1Z_G4FKRbuLfavY6J288HRAb9RwT4R27DOewBkXXM6SduS_g9cIm8-xZbeP2N_BPqsGdc31kS3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2vUVK1U_OSa8bxbHbsQz_kVljMC82zrPpIPCLF9gghq984e7vLBRk2x4-AHq3maa0-45xnwl5h-102IKDVL6MqeJF0vWQWtcA_UGZvq2QAPvOwIfTdwj7EaNf4yyBftYb6Koo0TmaEXWUMsrx3-BEHY-jwWJ86aMuglT6EPZRXNhUrJNI99z6YbesOZa8VjJZ6nxnyJCv7Hvz5Y_33RqDvg2nTr3ExQZz8FwYZ8wxcdQs7KmF-sHipvxMML3YRpR5a80WbMYqYIilZ77joaYDGqG1zlHx8GGK_dHKsKCms4Upttu9dj0zr6YTo8LXKynO9LwV9nKZDjMTc6I4is4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB43cPvOqHCrwMECJEEqGknAzb3cg2iLOeo_fl80yNsKzCvZwlXWa5fyjsaZ4zv2Q0LwxPS_f4K-LcHq53B0_ILDfE045cEVyl172yCwMRIMOzM8FVKbDKXynMY9rm5qDBdCp-4naeFoajcPcKSolKzU_--InA-AcS8N2sCKbU9RAAWwdvXYHbGz2hHWvbDyqNySPmr-bLqKwLIbT5o9hpgpzP1ZZerkAN8EIDM3O782nvm91LWbJwNnklc45yjgcdTcwR09UbUnG4EZPpRIdD_NoR1o-fohRVWGO-MaW5RpoFCYAuE-iUYJ_-CJDCoZU56UB2oSb7tCwBnQpXPCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=k6Q-IZ9ZXNhf8hKWE1OvPLvYta5XIjMrmRhJgjuHa1Ctre8GsHjT7W9kB6P6FgaRST4__gGjlum44IOMrhp3MaraqE4DyCRm_8Zu2b_cLwlU7kC5SYmGsH1BreFGWKzUqvJRD9_UMfHlgbJC5UlqZpXHMdyNt7mIxQwuhU8Qrmc-OGdMydMwMQzYArUswmDPKi-rM21-4DzoiNppCUB0xPLBZmotexhVDtvYPT_jazVL0IZM8xMkktR-En1YWMKd0tlATVWeZHS_ZwtmxZBlltJu2FruHcaIqEgVutg2gn4QM9gpJF_QojRH__6b_jhEKjMEh9A0RSvNTL_UuG6GMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=k6Q-IZ9ZXNhf8hKWE1OvPLvYta5XIjMrmRhJgjuHa1Ctre8GsHjT7W9kB6P6FgaRST4__gGjlum44IOMrhp3MaraqE4DyCRm_8Zu2b_cLwlU7kC5SYmGsH1BreFGWKzUqvJRD9_UMfHlgbJC5UlqZpXHMdyNt7mIxQwuhU8Qrmc-OGdMydMwMQzYArUswmDPKi-rM21-4DzoiNppCUB0xPLBZmotexhVDtvYPT_jazVL0IZM8xMkktR-En1YWMKd0tlATVWeZHS_ZwtmxZBlltJu2FruHcaIqEgVutg2gn4QM9gpJF_QojRH__6b_jhEKjMEh9A0RSvNTL_UuG6GMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK6s4j7_Qn3p4DVtEzYHsnpZLHgvgslnpeOBiUhuoE8rAX3H9n-g9O1qFnfM29z9OWmcjgzA0VgUsSK2bgTtFAupCFkApxFVazT2yqPd0i9GIkEnVeGX20aYxXHprwNA36n9gpbLnLCdeyfSTherOQGuH1Vm9ugs_De497JVK12_cZsf1h15IaekY1DMdGL9Io3Ud5ylerlgrbpJTeB9t9y6AlqyUmOlLkqBcQIQJlMOJIa2NhUrdq_JoixWltr7gwyNQWRf78nk-pRTeWljkovZJi2D1b5aGAYHot1tQwiqwIiI_l9WeXQdZkVQKI3yDoh67k81pVEWraNB_EMQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlTJtzEBHrklC-yZ_bh_qE5XMEgpontzLW_3PkV40_zy3fjC4V2QXaFAOA6ti2amY8FMnGuVtBYwLqHeZqljVrIrf7tuSA_pEvGDN0Pm_pUgOMPFqKxuTqn9eJuGwHDAnreC8axgLwUwzD_YXKI_NVodfcrS6LPEz7e3JDsfGwyo4p9NhFHysZzNNPuzlsxa7S-kyUnxpFyWUBO8axzPU3Pi3Mu6h-73bYyWXBlWF8PDd_4KtPYNTJuuOl14VWqJGYusUK4tjS4k5ny-YXEmoXcMiK_vys_RER-7R-bYkYC2TuMd5SBLutxHBSxXNHGVr1gZofhjCPMoTo3gRrjZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d98rhJ9qxU6g7ZO7M9d_VTAmE72GHHMBqO4v2PTMZNGGQsUWcRMIxsquIFNJ6P-F4BJdb1kBLx90k1SsRd6voWtcmTldax5cYLXPHw88-nrkfG6JgGcRiOyojM8znKybfyliWPyvBaFibbVFzm-xgk79ANs1CtwvgjykFRHl5Vj4xRIAeOd6wOmsCl3yFypOKSElHojhrEKN6UpmpYjr_NUJrJIQq8P7ucclA7o_NyegPmrkaSaetAhSt3HtYeS_JH2eQb5il-xkAUVrypUGsv5hcUzcTreQR2Kz-OUKKsafbriYVBzeqTsCbOZPaXeIEfgf_h9CmnTbrN1UnATHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRo9sqCzNiAN9IsS45SnQYaNPFgEbcipWonbDwHRP-Suv1DTH-6sm7lyr4PrCtTv-PFKWVH8g4Ccshz1o5vfKjOGMb4DPSaLETxE4DXfiJy8MaQ0kmcgMjNyUu12yPHprA9izrr6JCG5b2zlBSwEV098qGSwUKr4XLUMzXyDgBjuDSBT6fyLhgGYZpKAmX4t8ZczIPozRuHXseXNhPaipf14vWGyPSfY1ppfkTGwOmyulg3G2FTlh0vYFcKbxO4ldeDuB1UoUCrp_R4Tbss3QVS8S8_EYJgNBL6FB3O2zMFXqU9SLMDDmRwRfO4cI1Nl8AZQSuqIijrwq0FXXQTO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB9KHl6KdrYRCfjdu0GoORah8r_Gk3wUMq5W45OeBEY9Z8z5wYwosewnb5Kk_aTBiuQWYByyth6Okdim7wOYRvmoXAVUMnQQ9XRggJa6EIeGn_PQepMJDCYXVF4DEMlicbeRbRpr_m6wh-WXy7_AhiZedQn-vs55KlgPCYyM-qKpUcPifQ2ffFdUwILNj3tZvYX097m2YpbEP-iDnr8Sc19BqCa6E7MXStq0Xf8BTBnayJx0hmDZvFuLaXQt3ep3OokM8xK66zlZ3JRzChu2MrlIPU5OgeBv_pUwTNq-5chd7hxGiQEZ3wGkt97Uajw1R_9nB1bNN-2_Ea0fXUei5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyHUdDWlYhi50uPBdxwosB13bc8qoUkugYWdqM87zvd4mGv6Z6_cAILY6yFqW_vR43UdnoFEyQ8EGrk24KAr7VZL1xhU5FiCdICbaHro7SODw5RaJzfJa-VUQ3xQFsdN9tiUlhtYGaTHICIWNGduDydatQqhYQclxCGlxmrxKzZVkNVGi21nkYXSpTButOun6gfQhrD2acfWUYGor7AcoRrZF5bbv8vJFZJpQbB1Xo0bl1H1PQ9_lHFy2VIZf6l1iMqBxwEnRbhZCxL8wLJgrrGsX57oGobdfBImiHoX3nBPhIe5TIz8tQKIKZcbTYlN-I3Iv-wA61RDG06Q38m9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJMywQhfY9JweRbu0UNlwkbHJmJw9uWHOtXr1uip3KGndUmtfwWOFuZI3UkQ91f3rKceKSlo8TlfddBexwQhOvfTfAPPrjsCMY6K74b0x1Rtc3Ju82_BQDb7IPg-OMNgzVkpPCEn2y_aSQ8EsULbXsriwpB8vbO6mIfOmU7d6BSFDy49YBKRyxP7rM49gLwiWob6H0fzx3nWituHWBQt5F3n90XtSG346r30RvZ_cdN5oqgwb_-UVbG0sCYSfmoLr7GtpjJ05CzxJQs8Fj89m1AWhCRNhAlDIzwnjdOTLRrNHIZ-zTN6nwKioTqsebP8DDpscG3L0uPcJCI0AqTuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuTBmAWpoqHvSCg0lMO6FKf3O8xcxOwAGnvW9MfHv_0Es2jBw47o3xcKEmMHLOZ9anis9RAsNdlxItfC66UCCj4WM-b-UrbI2-7aj47elfY7vGFgFqPLRp-hPVmegAdqHN83aWY7y8vsn33lmRA5wQvcjyM4RQQrcQew5UbG895nVuS3IIFljb2_GWRV8Z_aT0UYd78bX3aqgEq-PO-GIRbMUd1hxz2UCc3TXl55WMeXkqwAIUwHAP6SHBpkkiVhcqYzWOMOU7Z5gZBALn2iBcPqbVQuqFXUo2UA0Zn90DQTx09AO289oa9dZKAziVHpQmqoG-bEKJFo2Gg7TsFluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwL6yxgCZJWVkGrw8bT1frTSTxdhqs9RrWEceuQmmDTwTwYW5Dy-QRxWgkSz33SAkEXQsFVcIiXs7A2rErnbcTHycqPUK9NPp107NR6ig2EZMVDgIdMUBY6LZa9eb60IFWQljxnWP1w2_wKE3szzAIzzJmLKuGUvVF5QHq2UgOAe4fPjYHTwA15TwxPh3aR2OMoNGWIUGD8O6dAwJly0m-kejCBX6m4MuNJBOtS6VEBY9hSJfMqcCuU2-Y4WtKsMzLcwaH1KICXw6ITi_-nrQ21FoeebjsImCfTWnCeWNMdgz_rKxgqim8FS8gRT3q9ElY-JIuLjgRctFJGZ602hJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmFeN470UnwtGdw-DQgbEXzKLkhHmO7ZU_kofIpXJiW9yNvztHWwiowxvKlMyDGpZt2JS5oHJ1qtIFzF0k8d2_sL5WayyUMr1HXe-cz71HbdS1yI37z3m3PkVR9hzafHtdbqH7N0I9Bqoubda1begthw1akz2HNqa0sBoq4GsQzmXMeHfNPHDqb-8iKOwdIF4JXdPkztrpCNzLNKHKnpQqG3kNgrympoFhilqLJXncEIAAjS9Ft7yLg-nZiRyiTzer8mSCY2P92axwFIXzG7N1zJ0i69-NoTJC-8Ai0BSpQVqgkF4zWvCiRBA05pKqJ67hpLVE5azvrRk7Eg1vI9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=tlK5t-iQg89PuVq4aG-Zoc7ejF2i1v_g8QliKi83SrGdN-TSiR7ryhIvLz7Q4oKyTOZbx_BdgzNPr9x_CuXp_dbM-Br1cPhgs6vmH_gYVCJFQd6faisROfQCgPIpiXfiy2AV2_Jt4tvBVs_zV2cFkcHluHnH7XW4caC5x17qssXQphuUdkgkuRSBUT68mPHC1Oi86Lof8ImqASyjIycqi4R98XlCiqHmzh9bAvM75ysg-CAq2zEOeKLJCtKs_jHjOpL_O1jPDG7mTL1S1MoQJ3POuGx7ZJlvWeo6uYf2GtWk2LKK-_17p5gu7yrwas21YTEDtbUbdX5GHgbFTKUtBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=tlK5t-iQg89PuVq4aG-Zoc7ejF2i1v_g8QliKi83SrGdN-TSiR7ryhIvLz7Q4oKyTOZbx_BdgzNPr9x_CuXp_dbM-Br1cPhgs6vmH_gYVCJFQd6faisROfQCgPIpiXfiy2AV2_Jt4tvBVs_zV2cFkcHluHnH7XW4caC5x17qssXQphuUdkgkuRSBUT68mPHC1Oi86Lof8ImqASyjIycqi4R98XlCiqHmzh9bAvM75ysg-CAq2zEOeKLJCtKs_jHjOpL_O1jPDG7mTL1S1MoQJ3POuGx7ZJlvWeo6uYf2GtWk2LKK-_17p5gu7yrwas21YTEDtbUbdX5GHgbFTKUtBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrGQBg_Hs3gf9PiSRsybeuoyWi7zRmgoIusUqRV8rc5alea4T61wwuxhfQLh6Ryctcz2el2KHcM1n49uNB7lR_nTg7HIIkVE_5EXu3MepNGl6nDQwWRNKJyAUEA3EMhWlPm2LdpZASsF_-kuYWJHpLgdYEtgZNi1thJo7ziUoig1CJxu9GCGaAkU5brNTra5u5sIgfwF-gns7jW50dob8pkE3Z-S_SG8brKVv1nmZOcaqgkyYqBMTP4RCuUAhIBRFU5i6_oDAA4IU0vtarE6AXhFar_mY2hEhlQXBjbxpNhlxspnStZTktjC1ExwQI8OKreCjSnO57v15NeVJwDeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZJrusNuTTCbFKf52hkYxfDuGWvqaA1TgA6f0glUdV9AsOwIYdOFkM0Jzu0SgWtSt7LKSfAZZFzCZ_MsmEzQywOV8AgPUgUepLEMKzt1E55Bv5gTDa-6KEBoXBEpOBRv3l3Ec1z1tm78EUykxGwI8Lc8TWu8iRtTfhel5Z4wkUeQt3fC-cqL3vi_QzxU2TD3wCNwMm8zTvE1_1RieMqE5lO_u5RMzY9SETjRhxOPiNu2gMQJGUxqBD9PvQsjp2SpxVuYhkZ9YQnpRrb5SBT5hD8359mqLVG7vJACq8KhLB-su8GwHd4yJNK8zjhNV1VqdzmxCYS4dTHux6x5r9E0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STQUPvqU7Tl-ZNy80LEdtUuKR14TcJP6DoHpFGoFrH79sIIR0l0tq6fGdkEobPjQevX-DOGpimEjh7AiALVbboH0OVUL8-ZAF2I6xkieB0Eq4TheHNrUBT2vyiSEPI8xh-AxdDmNEztRCNhlCySs8mMQSSUCL7VQlGUo4LIK9ktL6g-gkG1t95NnreM1JhLyxh6IEoiRkhrfdS5JpbpCmXITAtNw70BpnoCGuNBxM3-epVPlNtHc0EKITC9wWoxfeYiVl-AY9AMYEA1_t5mLwCZyb8pvBCp1COdZSkAnD2dLnQ4mgo1LjwXINErF5uw3QgqUWl61NvcU9rxGZfNi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV-itAXNlCiWvushzk5x-53xL5XWJJ8IsSi9CX6tL-mY-D54VhMAEak2rRo_5nOLmERZBQXWb85-ALLCzOJJAJUtH49hVR_gYMqjoVvBfGrrEV_bF1cd1gAG3KyVfiFe90_spL9h7STNoDQfmyWhoXcPpKBJA1qL5ETuApDa814IECPJdRkCEUGBhrjePXc0JfGuNIHTQRjcGRtFwEWFrXPV5NHjvez3m00TTIfC0PgIz0wFWrHWiKinoRogD_RU2iQNLL__o_fKl5tnCriyddbqdTG4wVkYS0TCpdwc196n3U12Bhkkfi71MzWECzMwlvGl0cSZ2t8-i2dLngr7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhCI9KcPi4eldqHcrsCvOZJvNjA5aBxPKV6KUQZmecdnofSWGMkWbwAYk5RQs2uJK62EiJ3C2bGOMR8L10CNYgmkmuggpVOgTlpX2ns3nuFo92kZSqnjyAkPYBo8mbxlPpMnp57DVnKFhwJyLMbXXrCnu6exNlRCTaUZPXXJfvsDmzN_EX87j8TwTQgUFtftvLmwgsHqiVrieishtOSljh-ALruzB9--jq03TWcxmFDJl_1FyzfjbRSvULtzNQN0s8zJRMI-UeLhlOXGUNdBeIUa-jGMvd0vibSK4CdH4JUtpl6I8NUGMFK15ONkZ5ULh7a7f6dBJJkVLjJawDrj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqBQpCOL0YCvFk09ylh4IoTCAoadtKDyFEORQSBnIzXZdNI59D19AutpmdZ63_aqtjPhMjrnlHWSx_JkiLItoaG8IraGG-HhCA6MXw_qyfMxSClymr9VkxB7EBLDnpw7UDGitR842vXpDLhLnDG_1gODtmXefCBWGhZUwg8Z-_9NTuYXLs4rbJtKEqvkUznPz3pEC8jcrzI63Uk0Q2U3641AXorV4hPzZG0tuicvA3KHqZnPpxi5XSI0k-GWBYdHXJkxmTeQhVO2tLmzGfO6NE4YEL8P91V7xZFg_uWNW932tSFGwfbSJmQpt6UhT0pkXXMoWdgVW-yWMKL6mppsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=KbsBV799aUvWRXJbJm2x1VAeDIuo8BO6hJcwCeFnpITFWgPwaPBKZafupJ_bQh81jpDvV4aZLFmRAvrXC8NOLIrn7JZOMhtWROnL_DipYxvWkLohbwtbM9xbAbKwkNDcnkzVEgKzAIsVcDewgGFPCrvBEL71bPtq81GMpI69VKuiGiOo56j7_Ki3dOt8_Gl4UZtqlF5hGV-Z9hB1zhaLVjN9JUi11PncCtoOrwpkmNFNsG2Q1OrEO9eYp5uK12gqq1JEX7WXM09LBi0iqDYjnFDq96hZwR0NQ7YnOgcTLK0Rcu4PpVSPuuxUc19FUzTOcCRxNuZkeQmn2GUvh6fcjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=KbsBV799aUvWRXJbJm2x1VAeDIuo8BO6hJcwCeFnpITFWgPwaPBKZafupJ_bQh81jpDvV4aZLFmRAvrXC8NOLIrn7JZOMhtWROnL_DipYxvWkLohbwtbM9xbAbKwkNDcnkzVEgKzAIsVcDewgGFPCrvBEL71bPtq81GMpI69VKuiGiOo56j7_Ki3dOt8_Gl4UZtqlF5hGV-Z9hB1zhaLVjN9JUi11PncCtoOrwpkmNFNsG2Q1OrEO9eYp5uK12gqq1JEX7WXM09LBi0iqDYjnFDq96hZwR0NQ7YnOgcTLK0Rcu4PpVSPuuxUc19FUzTOcCRxNuZkeQmn2GUvh6fcjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbGxvVzmWrQk6peoZ2mVOYS4K9LVOb5TpzTF4G2IFwczpmRlNdB9Vd4f68Nj4Vw4n7I52rJ_lPBOplbvcf0McSdK8Rw3_QYS-187H4P4P18KOH135uOp_tyHRl23B-B_A8lxDp_cujgGwhsTG3GvK4FGKsofP5bhFVIrffW8Dq6SXvnSu6HJyPcfbs9NPfGDr8ZvERYXzXQsDWNWO0wUJYjhC_U-aVEOfAVnLMgekUAxQxtq1HkA62Dq4eB4Y8lSvXRnGkHuPHZM6bzojIUPoKr692TYvZ3e2wfXs3zMSPVPgBYL82ug4N-UF_qoNfzmGqlpOGpjddelualX3JnHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsQkFzCEwDrrAiAFAj6rbHfguPXrAaOLchmQM2lIP6XNPYb8cDL8rqs-o26J_aqeqE_e1sv4OOIVDesk1HhZw4KNMqfG999cPFL_Hdyy8r4XxiITsKRUfHlwKpBq8P6rSOw-FLFdG7CuswOvglWpGPclRd1sn9Pq_vW_yz9zLhadhLbwEUc9B-_KR6ccVDtDlDU4FxHCcQ22MPx2n2ZHAk0lTNFrWh1EhC2H1vAaLaKvFqZxnat0J5_vCX_swkTTOCtHC7-roEhxd8wIwy2-GVpPf9sYKqJjKM2g1D7dJ-XbDBl0MWaC7_HOAJ6SKFRBO15suF79ueGyJCd4hiuIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaynnHWAsC1qcGPSsZsMgsPoBD7Y8cpA5ioErWBOwFGOFof--JXUq5AOREVcpeZlFiyiGd408he0jEAoLVhcO-jitI6lVENwweNUUSgocAL5ThRsbgd8XfMVPNZCtd8a29IxpJYv_Ba92gwspuB4AF62WIXypVM1FMub-U1EAEQwWjyNmjxyl7H19eMeJ2ssDAFUUXhTte77zDAjG2-Px_uGD_Byf_ZvtWxJcjDE6IifuDdt0zqrzjfzcWtkLCdDSOgcCale_slgg9VDg-eeSFl-oS5E9WcXB4mStlCrrhPTeyMPWpd7Uo98thd34p-X1_22AdMSSfgCa8YZNFrXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb1dvAhI2cTrhb6UudMxX8R5QXFFGknx247WD9vDk7LC_HYRDNgco-ypcdKIvCr4ZGZQlIRuNovF6J8-_jw51BSINefyccxJVQeU4e2s8sauWzLJoLE_aFGVIAmJKIb0GO5Y11AW2V6OLM9ZQC7TV9d-IawspImsfVL-4JPvtVjbwm4o9LRSlmvNQH0xzsPj0o8G8BNJBRyEJ4SWqcFYohCGpAcEna6KFAj8W5jsVUjczEwWOyvNSoYCa0Nn4eNoYOvM6b8V7t-0yfB3oTxtVs2xYOwyBQalQk5ySoWWQ0nUh62av91SlYPco9ZO79hKGnz-SxSDcAUeAT6G8FKUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1FKdEhq3GjhiYMjBIouCEkxvhhcP43utZEq_U4IP10MBgcP0_NhvIgS929_XRH95fElBLNmODO7n0JYIqIMdxwFMVeUNtLZosWpQpBUrVKCkwca_tbLLZYYO_BRG119VHx8lLmx7GC80oahg9oU_Q4FeQJFIgGp8vF6dWH_O7UuCQFRT3iss4Ydp5x4SobH5IhBwd2Vw40thYq1uPwB2e2EUu4lyuJGmaa6CD5hZFZSV7bqExJkinEZfIphFR9mLkIz6mON9xAL5mLakA1EKFwCMGd4CkUkneeGmYVi4yOoq09vQbGokh5n5pDfnmDUJ2fsDSq7hoW3r1EJEL_OCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFOpHJnWoEtm1Qi9mFTV30ox9_pe15uTM7la-hOgHn-mAKxcpIhicuGzzle7ylzEH6YBnTtu9o_hinpbyNWsJxPn0nKn3uvy0dhSOlghyFuR7STFXiGyNMH0D3j1ckgkOlsmy-rSUMo61RmWCQ6PYXrFKs7NWvG8wXMX_3STMVKdwGUw1AZtF9Y9B112rFzksLZ6GQ9NaKB7lrT5n-fyqIRpzFRP--JBaKi5yKww-KD7gvJ7ffcZHDAK3zIiZw2jUDyGJ7jSUN-kYZ7uAmt0-jI-fZEpkVcrJOw_JUL4VZxuQjQUq7VGRksXyikxqVt6alMOeGERuzJgmCSzUvt96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz1hOlN7De4HWsjT5clGfnQ2qIVk5XNY3VxVm94_9aA2GU19qlijkqKofknOUKE9FxqfKNw_ikN1gNFsvxo3k6vwJsszDQ6NxtMGnQuOUDX4kgdj-gySaLw-lcD7v7l-gccmuOs0BT2qceMPwgDT-Qvzky6vFq1v4e9IbOgvbpU4xXE0bA4gYsvK-Ui4Dh0s-flkkk3OO6vvXtTPplOe4KKyJ1lnmbQTna8NSQAnTbwc_7ew4UWO2LN9Giwro-8m9qcZUAulED_Qqjqkqc1lUScChPTvGgAlURHR7BsQozf6hMKxWY8NtoxVkm1XoR6u9GDkhZOvzt8qUqYsZt0pDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mbC8p6itGWqkCNcInQC2w0bMB7MiVRXdK0xxY6L2BMBWUJrZws-Dyapeoi-Q67jAtdJh0rMPrFwNllimLMqni23GdHqT7RUheMY02qzmxA-4KgeYHmj-TnSue-n7KWKflFm73qA9ClWq2pj9gewhdvK3jdqFF-D2seVmmJihuM5sKvj3npCFsM70u-SwxwoxPcxl8rUJifoGYh6RxqXPZchYjYZXH3pKTb1DlBpmRjulVT6QSM5zWAD8cuGgzbvVvKQfs6fbC5kdVxaOS0vib8w78KbMbrXxSgY6hWPbQS4hxbjmuohCEKDqgnOFPBy65ls_u767tRJZAM7AlXcuNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mbC8p6itGWqkCNcInQC2w0bMB7MiVRXdK0xxY6L2BMBWUJrZws-Dyapeoi-Q67jAtdJh0rMPrFwNllimLMqni23GdHqT7RUheMY02qzmxA-4KgeYHmj-TnSue-n7KWKflFm73qA9ClWq2pj9gewhdvK3jdqFF-D2seVmmJihuM5sKvj3npCFsM70u-SwxwoxPcxl8rUJifoGYh6RxqXPZchYjYZXH3pKTb1DlBpmRjulVT6QSM5zWAD8cuGgzbvVvKQfs6fbC5kdVxaOS0vib8w78KbMbrXxSgY6hWPbQS4hxbjmuohCEKDqgnOFPBy65ls_u767tRJZAM7AlXcuNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQWGlFPHjtnf57ovm-k49u5JtHneLdN2l5iCO4sKlLN-LSoYv3WOgXa_u7LTcvjdqX1X6BFQEwAH_tmICau86lT9YTab8NVPJFw6wYauZsEbsZaQG7A5h9ij9YYZE7E6dFcwe-avMyDzypLsoHIWxlAFM2IXZnUvssGdfo98G4LMCbV-RTRlI8PARcBpw0y4btN34l7e_BxG7-YDhtIvQlgrrqLxdlpuI3k_EU9-I_uUGToeWUIh-0etd80agFYUwjdoo-3EA6Hz66mtaYCcRFs3HdJ1XP181avQxz5y-Rry6MbqbzvVrqclJkRBUggjNgQA3_cRNNje-n9FieETDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=Ei0JaGKdaPz-aDRLCed9kGs4pKxzAPyDeoM66bmesmWQg8MlEZUaeszkUoCIofZldTtEyaalP46rT0uoeMVBT9BKdih6LQzdkBXySdGvntqlNErfsOajoz041M4t0NLC1QT1uCyy1HdjA1rCAZesOwG3H0GWOnFX4zm0YS0--xC6C_4YkY-nO_V_QYLCTaljpMLeWBeqjk4u-R7DcuFRdKqgBGTMg92UDAKQb99qQpR9eoFshAyOC5ACoy4ExW3gxCs06uovxo4NiDiVF52gdPWf_IInx2Q-EjzkuasCP2AmVZOuUhWRh4ln3GQtAJpd8TFKKgTpCdcozuXC5MIPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=Ei0JaGKdaPz-aDRLCed9kGs4pKxzAPyDeoM66bmesmWQg8MlEZUaeszkUoCIofZldTtEyaalP46rT0uoeMVBT9BKdih6LQzdkBXySdGvntqlNErfsOajoz041M4t0NLC1QT1uCyy1HdjA1rCAZesOwG3H0GWOnFX4zm0YS0--xC6C_4YkY-nO_V_QYLCTaljpMLeWBeqjk4u-R7DcuFRdKqgBGTMg92UDAKQb99qQpR9eoFshAyOC5ACoy4ExW3gxCs06uovxo4NiDiVF52gdPWf_IInx2Q-EjzkuasCP2AmVZOuUhWRh4ln3GQtAJpd8TFKKgTpCdcozuXC5MIPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY4sZAYou0P7JrExW1Por_iEsIcWdyTLMuRAqLn1q9KM746p4PfxwB3Jsyo8zq_UW6gPA8r_IaWHrZg4e-aN5s5YZswQ2TogU8Qh8_1AD8faSkC75UpqW6vO4vkeCTa1McmQ4cr7kDJxfnAWvewDOdGZSA5NqIWdK880mOcL0MPTv0dmQJgX19PqtXHE4w-FkC-evVT98VL4mwgNyguJs1-rnCYFqMcdle4KlNtZcwmNqS9QIN2SsIZU-Ut0ALJBw1rClJiKmTd2TAo0PdheujmNsyPQB2bp67mMvhdl5uNXQrr-Wttn2n7V60KoDaR5BDZOf8umJob7SEs7nyyG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYzsr0wo1V2dVYTKo5JFDlUeKVpGeb5qHmztY8CozJTB9xTrpqjVaRjqGq0aLfpPENmI-EilZpIX1elJYdUl9Z4-52NlUSntbdj_gBX8LlW7OlkbkQ-LEURWfHOb1FnxoU8_q_Zu4GRcTh2DYQAesRUJHhAjrr1ik-EB_bZiKOGxEiftMY8Fklh8VzHfNnttsaGAQndf4cDnBWDx9kslL92-m2X0VJE5arFNecOuwxM6WCWK-2u63aQmpCX0vn959LWImkDy9oIfnYOtSNwsEa7DIOvauDEN2QVCWrYef1h93G0Mn4rxC6GzAH6PJ1KrkHn-gW24mLYF9LFIwgKOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQd6ChIF9LEBxRaTCX98oLEf8lk4-9kbzlO6bVO9ijt4AqbIXxL31niUj9tVDK_gYi9kBGHP9BrNhLRQcCvZ9MZvRqoHM-73MXtXkOb4zxcRDSnVO6ThSGo-XykTswYAt91KstOMVbbSSofAMCMG_ezG0F6EspJn78eLwVpRUGRF0mJZC4B_BsAUCkVhZS3DsId-oq2KSpIthG9JSpUzsw_C919u-xvOxFi1IEbiocSlIKRQaoxq6qzt6pFjhPois7W-ATj9sJq9HK0QmtfSOwQfA5Ki1Kz86ZRLD_ZaR_Je-N-OV-N5nyXFGH2uTEZURKjptNw_lE38jU72j-sglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_NOFS_vb8DkV3LP9cGuiLMhmUM9ehWHMSO2jSSZgxArIc8mFxnPQWang40l_MDlCaHSMBh0PZn7OXxoNAy6GVG3xlSrAMosSip5474ALsyMSenOnK1EItOy9SUSmuB_pI6UDPnBb77Uq-fP63UMRwgmXCnTjwLK7KhWNUtL5kVKTjy9knopCBGHrpR1cLixZOsSHgeVhQQNXOnhH_RaWCoZLSa0zw0hubzk3Md-mnWbmykGHlCIhseTdrsc-6J5ZA1k7iz6aOiXyZh0uEOlBsh6m9_Z9IErKaLHYzRGaeJhd519ilWbMUyVPY4eetR06bIZpehRMJ3kVF2jl1KxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUW5YRiiMpCFTIv2Z-qpGUBelMDL7Z3tDTk0sCxCHNxFriW6YKve9Er_GIFrZdkvzxjcnjdmKbVWuEE0_aoFYAujF0Uc6BqeKMpRHvr6G5U3LtkLnFARUZvjJqwUlTDO7vSD9EgFftNZ0bYSkH7NR7Vi9tVmYtMjpCil7DcpR7bFFsrhJxzTI-QFT62y1IWk4N35hs4Vig98GDy53VxauPEHQYZLNB3bI-pXk9gq3G-5OhFJOOBRpzqMDrTsUwlAkRxfmRNwYPqsA7mK3YHekMAPKrHJr_FVT9yqBZtYC5CucIi1g7deOLXEiUPSEJ9FFkOhVzNV2dNBx1WBaI-qRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdUEgrxz5VGOOxgkDB3sDEiULhpMq2eZL5Hl8bvlCi5iOX8voFOTlvv_KqXKAEOxH0FEO2VfZd4JiOFm-bcFYIQWLPkpTIfotcdC6m21qc0dIKPIm6kAIBdD9RE8nC5nu91Mx0NUkBPMZGomjsOc3lKe2ckXpMAtTVj0Q6jbu2aQ_WwpoCwhpJVIyGjK2poJPhr43wE9Hd4Fs1l4SbolN7B22SNQl2eBH1DC_haTYKxCtZKejtRJGxR5IKNNMCAwv2jtY7TVTonFkX5VvuLpXvzEHQJdYNyZyFnx3YYAiUOdfclfkUJxoEC8L5MIYZX1t72mYZchq8jFxU5z-0twCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhWkQBC4FzO3beXXBMXKW2y1vpAx_4UfNtScew-t48BmZoC8o9Cxbm0pLnksvGrJ0_Y4gp8_d7AWWc4s4JS1tP6GYzZ9GV-Uj0XCRIxsZa1gDVsDzhoeESUhJGLoqAdaX10cT-0xS0S-cRNZVhjk-duDFuuy2_w4qI1-d8YrbnLjvnICPqQ3dhEcv0NtJSlK4jhIjb-izThV794wuQFTU2RzNKAtVWctnq21Tuh141mS3mc2_hq08Ylh2qYQEEYUy0kVVRU1bV5Zjiyse8R468KIAxZn-GH5Y8H4CFs_omAfrfO5tXlPy2R39Iw8Q40AGiYaI8lrJOhiYBpGWa0a-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APg8TUNhc6qSrF76Fas10UipmDIPxfaEtYUiiAjt_qBPqL2-PXBk2VnH2Ws5QHXz6W3F87zwZu2cB0TlD91sQt5a4myt3Zz2003vbuJk4wwZvhxIaL5_mHvqyn1y6bI7j4K29wF1b5p1iPSLwkZAJdCbK5Fu4pNefnMxbuFPEWCzl-qFLJdFUYuDNZxuvaNflmzZfanG5XKQ4UWte5tBlgf8F1KFbglVXcVean0cAUIAzMrdZS81dGSjjFLFYtCg1A9AATeBaCoQEbVVWONJhjvJu3tikH0g4wMueUjirEi21I1Z7in0Zn_eBBoPj8DgCzvbBaDutYUtHZ23Azfo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=eBqHW5TMrsSdsFkVRpUnWI4t-PxVPwblA6WGYqC6B4aNktGMRh_g9jF7TxRcWxX7rcT4QbIDd5Ysm5L4QS-jfQb7iQzwHApDXTsoB3TlvH-QhZoYN5I493xRw2vg7sEkrllqSfbK7nz9W6jtAgyfuRkqYrI34KUKtHT-U3kQG2A2SAU0FzKx5NG-8TpQiXND0G6J_0BcGhDodfLz_9_7uH5o9qWK7QSk1d-NOH6S1rv82uvvSq6k1I7UqFlFml68NZX-MmUkd5hwpl93yJp4mAfYrxX38rK8HuB5ZCRGTzTmCBKGl448xMQdmWtQFqRGuT17SUa-brE9iVYAcC0Fbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=eBqHW5TMrsSdsFkVRpUnWI4t-PxVPwblA6WGYqC6B4aNktGMRh_g9jF7TxRcWxX7rcT4QbIDd5Ysm5L4QS-jfQb7iQzwHApDXTsoB3TlvH-QhZoYN5I493xRw2vg7sEkrllqSfbK7nz9W6jtAgyfuRkqYrI34KUKtHT-U3kQG2A2SAU0FzKx5NG-8TpQiXND0G6J_0BcGhDodfLz_9_7uH5o9qWK7QSk1d-NOH6S1rv82uvvSq6k1I7UqFlFml68NZX-MmUkd5hwpl93yJp4mAfYrxX38rK8HuB5ZCRGTzTmCBKGl448xMQdmWtQFqRGuT17SUa-brE9iVYAcC0Fbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF_ItVFt9nPaqn71976siWDtigPHtPozvzI3zo-fkerH1mq7vE2WYMYHnfK4Hb1yILfftuJdzWT60Thp4nk7-ZPGXvrxgqBgQFfyu7MdWPGd7ZOVUCzFpeTU5h7ZLzOXnL242Q5m3XU1q1AXXUtkJfegycvl18_-5GkfjYnxCWMn-ij8xOpvJntXbnTDf2301ahcmhzJ0Wl2w_JBcO7Q5HN361vFvJeq1I1e_YQ6eGpE3XCyWmH7UkCrMZozizf-mR7VPBSAa0ahvCT6yBCTIfmPDGCbfIZdF4lFtLzjZDKFq2xWHNRi4TXMCKM2ZCU2WVWhvhztH2-gE3JwrEYu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h4469y-z1SJTPo6Ecu1oFS50jsOIQiEjDvXoqVvSasM8O5MBBykIsEOeBDvpY6gyhE1I1qB4TU2QU2aTelWB6mDDWEY50Unrt_gv_94s6KQlI9TtwUu92Cx3XkleuG_1j6CeAw1NLF0Ev_ft6frBfU1JmOZZvUlfN-Qxd_nL65Ufennr2vRa6b3rOu0we9GgImTnYy1bpq55BjRV8mjmWHRtZbR_v_6Wrn6wbS_JXtjsmeu_fdoW7cEle77JjParviWFchXY5AHC609QHKwuA1ArNAs5T28Oh4iFThBDpfL6iPGMNSRh6wSt7N2ZNdOYySm5KsgtvRKCjYuu8Qdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2gF1wlyFAZ0hsSG5PeNzu0-uEq87zIJqfQe8sg-SH5YNWr5u-3KjoCQ2s11tw3kcPfXx87tFt2MhGeI579DTUTs6lu3NgCqPXavGvkcrLJo7sJPiblhSOzQ20W-FmAhb7-ENClX5BHKAEocmWH-kz_gBqa89yUgqbDMuyHvI0IGgSsUsVT5eeJtGMCgQ37QfyYqp4MEac0BebtL4uZ45uY_smpcODadY-h9uQ5nPHPy5hvzEzy4JvILG_R9bTTB9wYNNN4vceiZVdOFh1rQqIZy9LQMcL8dvZ9lxkdjwviiOEZ2zJFnOqHDdbfgV1boqCAedj3lnL1Ac3TvRq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px5mIw2kyuJVlKE6-BWKP5TrEpUJSkgd1fEy0aa2Xg8a4aIK1qdICjWuSZuld5PiXcpfh2hfvRDx-Do9RY5z0xHjiye5L2hbgZ-3OISuFjk18qg1OAf36gkjWYqtxfUJjczNEFR6ZAZRrTctV73isArxVqje7C2uancSUabuFaXsRM5VtnnFbcZb3_0I0vSvXgQUllszoxJU5lNTOg3pLN30w4lBl303HKoy_8maKPHNGtyOkbFpF7MVVogJhf6IAcij2c8CdrH8VCjNT7P4nrgUKMfaU2RXEoe_sRSgat81-IuEQdRg-dcoKfGaNRfQbvNfdbA4PaJ4DB4BLi7d5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=GmYVP-mQ0NbPVR42kKAAzNqdRCZhcN7qSUJHvmgDa1Tr68IynvE-n01s9Xstpxfm1nAjkZRstGmPE1ruJRNyAEL2qQnuf03OoJ9uTlDDbKJBcwIPYK4wv3TEb855Qe6wC4WYfnkWrrnzoNGZLWJPDbDb93_QOpvAcfKlXsv3dkeGt3Xh-atv6S1p71cIQMz84qX47-8HN6-Y7plSADUjGWNL3Kix3kFLyjwRFrKpytEZL__4h8ucks6wTkqPW8WY68ZGxDuoUiaQKsRu-LqEnUPM1AFgfP3JiD2e8V6csSLMqXu7JokKUFDhQPbbAqvu8A3IobI1VWzOC6WxSqiL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=GmYVP-mQ0NbPVR42kKAAzNqdRCZhcN7qSUJHvmgDa1Tr68IynvE-n01s9Xstpxfm1nAjkZRstGmPE1ruJRNyAEL2qQnuf03OoJ9uTlDDbKJBcwIPYK4wv3TEb855Qe6wC4WYfnkWrrnzoNGZLWJPDbDb93_QOpvAcfKlXsv3dkeGt3Xh-atv6S1p71cIQMz84qX47-8HN6-Y7plSADUjGWNL3Kix3kFLyjwRFrKpytEZL__4h8ucks6wTkqPW8WY68ZGxDuoUiaQKsRu-LqEnUPM1AFgfP3JiD2e8V6csSLMqXu7JokKUFDhQPbbAqvu8A3IobI1VWzOC6WxSqiL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNHU85EezcaMQGr74rNq_ZS5WIyqYvbEWhdsLU44I5K9ZHEvhf-tRsVsx2CJCAmhNmak082WoZ0_A3_BRk9nHLLIlNS260rQMhFcZpcDbcGAa5yMqKTGUGUx43_CxwKG0Cswkdh8dZQXPBRQwjl3o_0B8faG84gkyp7DcEBQbB-PPBrcSsh8xuSN1RvhL-m8ewhP8QwDy6lu1IsHTL-z0_EYZwugYt7L5BBqCRrrnUmg-si8132pYf9PTAixCPSf89QJEf0TQcBgfMebZlF5QONOvNv_HS3lOYBC3HajZVLofec_UdDn2Pn_1JpjgU82KpXG2Y38wgtoQliZihkx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq_KXpYKLmzt7llpGYCcd46XVUrqqOpMNTo8Xvaniyac7BibYtUDdkyGRJ3TD9kc1DlU_OIItQKDnriMOFFn7aeY-bdBluzswAS-L5SgdkmUvo9988uFS1fKMDvDx4ZL_2o6_EzlEVtdLy_ggnmFPPaVT6FHK9Nxa-uVSSCuX-ATsIgDevbFngRiqrjKcYEDiEuSbwyNI5J_D46HvuVE4sQzLzfT4m9CwC98PxVpqIVIiD6cP7jUa3Soi0ol_b5x_I4f3li03VVO_m-4zrm4_JIu4otEZr4aMlZFBGyplCuUTki81K9klysRvjnscF9b4SpgUo93x-VKsTO7vDEkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUBHSQz9KRxhq7_J_qIoaHUkjFXV4bMAMSs0nJCBvdbQ8WRSp30vTF0MGq_VnP15oVK08tRussVi-Q4OuUxUTNNxTnClDJAUBN4IuLZPWEXoE7B8OdT6gzkqXHy4yYW4Wqr23HgCM7-V5m-9ZaaYSkXhXyoCPJd_icTA5plHLWMrQfTR162iD9DXqCw2i03_BAfmW-R6NYj8Rltdt8fU0kH7Sfjw5dnZzwA88VVkfQY4-nrHeE4_6d_f58Fu5Zq2Ctsyp_D4Iku80U5EYVFj4gNkMfdkYTOMDReEosCWgb1DyW8nCQU7uVqWIlmZloidTKZIuSPLtFPkUuLKAzD12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neLmSz4I8ds4dqvFbqlPSPQxIjU_kuptPqVDpr2jqOJFVQLpfIpYqjyqOAxQHFlJh-3GgVyf4ZhKP5sXYCogApfhhMggqt_c7HVSXjdSkdVXl8JWuYfHoD0b3_z4nUwLnXrNMWIp4mqtKCPimr5bzRpIuHTxCRJ8rEE_2JYkpQGEDwiuFpx938Forn3B11gGvNkPzmZ40-WvfuleGhjhOxQVCaU28Lf4eEYT6PI1gY6BV9z4qBsa5HQakA9KNlghIOH5r1w6Wtml4mJh81DQAD9svMVZHHMrFbMcWdZ1XdnNaNGSTMc-QfDirMOy4TcruWHhq8awa3y0u_Z2L6Finw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyeEvsJbLWQAsitAlHIajODMjXhT6ReMY1VXhcEqQX7WYp92ykPVKQABc55LgIPA4WEAsNd-h_JY-KJQfWp0_VYvsOyAX29k-8EEGYl3HDlgaCdKuqfPHHmnXIHVVITh07mDcLDNo9DEylqp8kSpspWtmadWXRVanSyI1yiOk1Guz7OkCTM4BxAsK0K45BHUHyAdRqsunXr90OJIMFMq_bTi34Xv-Vl4qXvPiCJEVAq45g5BKBjal5JqjeHckcG-OsIsSZlY_kweyD1xlFgZtiBFc1wOPCEleYh0R536hR7YSCu6YWw3Pd6TVXr9xYjbKtCuN_e4652S7dw4qJ9TVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKCvVyIfuH64MUccj9utuBRq6XCLLTqX337YFE5i4uSq_eVhkCBGIYDvYujWKGYHGACTP61md4EwQAeg4ijSZyDKpRmuaye7noku32QQmTLxJzEYoYwXcNb0fDILjHyPyYxlRq3boZoGDVDkM8tZ39jnJmVy_KmCjJPnAr-A281yiMgSvXJAU05Jnd_tTK4SRe6LAoeR8kxLRSJQtQPI-_xzIp_4nhuuBURVh3C8tKf_K-r4m-t-YdRdW6fqK36PfaDAEKzURQ1l19kxnekRjMv-HA37D4r3oLe5lI4ZlS3tenC9YNzz0aiseYZ0HsZnn2HR5g34UB1sfTZa2Px-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=AEbrylFqHdp6LFae--B_k96Q8JtUCGm1TbZQF-Pzdw_RIvRSAHelBnyaSUHGKxCFARZfBPXso9qvD03RUbtynzwa7i-2CQCabHxOlqM-jv76PJ0WDGGRadhzcp_CaMxZu_xfDKsORJmT5VWyTZQuGMDI-TUPe9L9ErAqwiO76R68YobKILM4YfiDWNreMPqF6Oge6Dq1qr9OZHrR2wSf65j_YCvIBan-EWqcevbSYfLs6wffKun6fYlUzfMgOcPVU121ydoP7oCqROZUXhbU-B0V_Jo1hJ6EIuYgtvsg-u2k-fDfeJta9j398pfKosXAAgVOfEqwBOkIEcCOvgLbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=AEbrylFqHdp6LFae--B_k96Q8JtUCGm1TbZQF-Pzdw_RIvRSAHelBnyaSUHGKxCFARZfBPXso9qvD03RUbtynzwa7i-2CQCabHxOlqM-jv76PJ0WDGGRadhzcp_CaMxZu_xfDKsORJmT5VWyTZQuGMDI-TUPe9L9ErAqwiO76R68YobKILM4YfiDWNreMPqF6Oge6Dq1qr9OZHrR2wSf65j_YCvIBan-EWqcevbSYfLs6wffKun6fYlUzfMgOcPVU121ydoP7oCqROZUXhbU-B0V_Jo1hJ6EIuYgtvsg-u2k-fDfeJta9j398pfKosXAAgVOfEqwBOkIEcCOvgLbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAKNkPh5F3c-YvJ3Gemr6RNq-iTSGrovaBRwUk9rInccIy_rVrnjOqW3J_joBWFdUy1J9R5v-r7FwXd4eJI3veC-YdpySHyC8WgpPQzj61JVc3LdvqAoTAzlatOIW1sra78TVCRgWGVTZ25K05SPVHizMD4N88zzxMzmipjc8o3IUZ900K7alg5Xm0s7Cxz65lSu_7SdcQH2oJsLT60m8dcqdJhHALKkRkMfqdETT_IlRSirLiFBIlCeHkdvaxVLRL7KFO8Yfq2s5XDpush0MHY64OBQLIJeZENqTtGOvCClHyx3aoIENRG4tT3uot5hMCZTOwgZRw2wl6ObHYwdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih_SMLqI_WfHukDnmoHoYuKpp1ED9t1BHZiKnLk5Ev-EpbrqV9iYqRHngt3Lvv4mbn8K_dTUfMhQqArQ7MuwriS0CO0E0jvDdzEaykuLvNplvEnAylGrfiDMKVxpe2qi7VpL6nKE7h7Y_medB8_Al6OuYEqVp-Z8HTYg0zxDMgjXrN02kxbl-JKPl5E0INu-aqP7AE8avDXBMD_h3icpJdEXa5NhQ7SjMTmgyALP_FzmaWyMar_NVhzgj4DR-oOzn6o5yx-r8kNFJMz_r7pO5_hshm_ii80W_hIz2x3MnVHslb7Q7b5B4XOtpaZvayUpZA-nus2L4Emn-vwm3xriaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzOCJi6hIPcxppH6ezJD3_5HiKwbGBSPtEUWiJ6AF9e8XXFF59AyuyBaGxSu2Xq_dwEf-XLCneHZo2idsovv3YewTb0SAWomzn6aDlYNEiT-ppoFrPkYTqo1VerQb0eSqqLRFVDMNK1H-kKSjaTKyJGFigm4tRYW2PINxZZ5kHcFFobgFmvYt4LBGihT65lDVHAANdbieMmUlBLcmxnxjHIjN8AxreejLn31Io3iVJsfE2B9vuwaRk9f8kmrq3V9ihi8KVlNbKozzamIYA_zAemxBn8y-cFBYA0wyukvWY3O7ruqTlSN4MHchZBBZtQBiPl-D76JVYDIhI0Yp9hEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IG-qpbWnEmVZC7ARKMH0aSTMFKLc10mm8bphn8enfNvKbQxwymvNuSVMOdfC8XF4UsZvXeU34t7NoyjcN5nHLINV4kQH6oMfmD0Vt28F-4AnuQiPo99RXND1lNfzZEL7k_o817EqQPa3cDYCCMEW4Pthiuykd5w0nrSaUMagD3SL0thTHPrOiKW8gGB0Hvp8SnuPaK6c1aDkApvRu04_ilWb5an3Y1w8mKg2Wvbvc0aM_m_c0qcX-B4w4pQiiR22PF7Y8VSFBu8MIMvsa8oJkSn7wRrx3JqZOKnDwCc7-G2UpPbLsy3DDcKF-4WuR3mVjCzfV3mjvTrI7RKIJoFPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USSIoUd92yfiF1iSrzYjk5SDQqGZPHjyQlIQ4LUJeR6TdjMLGnV4JcrTOeXaEky8S9xB3OixfPGEd6z75tGO4XIQNzvJE6m4anszokJs6s6OHfCN__0s5TxHOcjMK2SuDAnHxUU3Ouej8KmPGr6EWXUbanmMnotU3UvxBHtPYjlHF3jXWqly4iN6s-9JqMzdTXv84p1ZsZulaoUc6_D7TSMrswb6beE7PnFlf6l5niEPtE-i6n4o6t-SO0u-W5gSSEDW7-XClAygKizQIXS9cEX0ouMIZQJk8K2fh8BcmaUxboUkHrHFMN9piyiLkZ6zmAjFoNv2-8E2AdcOYxOtvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX7JImB-1q5XmxHV9M56Xm-yuqAd79OCD7X-j5n15ljzOP8l-B9orfDkUBhiLNoETOq8WGNYkb9OgQGAIOy3STuxlr87W8-uGG_OeAZPR5JtxlYhS6mE32l37wjn_DpnwX55XSTbd1GVZeUWTGJ4fbTmQVvxXVdKXsT0Lnbt8uHeRQohXIl3UEMKQx28Fr-hp6CbJ7nNpFw6ruFzeRhKj1MJG0XkZn_V8OLUAZeNrKr-E9bBh_2Gs4NoxsESb41GN2DzCuAninapYJi-NBKq4PsOCPU97Y2l1jWaJQLpv_Ur1N0MYTg-UtBe6wjWYpVCUkgmp88ZB1wxspe_mofFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJv05Oew_4JulNXBsvZLGuybW-Dm1zHIcgDakmrS9ITyp5ddwo-b0xzxtOhOFAyWSwXd-yPo4jX6jEDmH7OWsu03g6oUhdzpYYEE-4XKgVFcmuI3dOXwYygD4HURQ2MrqzegGa7JLPTk31ZxMvHBjf9GvbM2-zPvz2W7lWJ3qwgreURknLU2TaVWKkp_pbaRREiQXytZdI3A6Sy3sF1mTPf7Z2e9XioRLJZTtd3RsRa2AgwPUMJOWdestyMU5mMPteg5efMk76kL44SHfvzaBJMYOdAlAm5ExOcaOUKLVjkdCs1IuFAslqP6myDzsS8pQkX8abhBtIY0h3f7Wy50qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHHMErd4qqyjJ8RMYpOTQri7erRCPdZm8sdnU52dufEiCIh67lK2JHwQ3mBYndiEDRpoptAeahoy408ffYAZnZlMOOXIBjoQo9QeykMTsztaGZKMxZ4AVMDD5lX9KqjdfZ1JWqBfFqMdbZ9kUntnkzn_KTpziteQBVnpZvYtNbxQgR7O4p7MVui0ddAFbGUHYXxqSUMq3RriXH0VMdmoZ9dev2uT3frNbFM3ODPfVea_yvsgLpLnT8Gv8neZ9OEilvkH6PRL2rZIV8ipzWQfDGqeobkUfEDyWuQmpJpElxj0JjLj_sgyexbRPfkJLjSXKwa4UYOowCOnDX_4GDK3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdBS70-k9xhXSSS7PokF-lybJQoMCiVUOAytKm6VCcMnMCVc8jpaNa_r5C_mE115aJF5xHS3k7KnQHBiD1-KbSbQqMb6ARDaxm6KIq8HP7NpO4uKs7sZ4oPPdg3xrYyjPu775lMqxu_t0ALbWHPqrkZLR44qnkysANH44Zr8480Kz2zPmC4YiJUrflqd1qgoacsQCzEeLE4fcbk3KsqP5RBDKaF1h9ycg9ftmrZ6sP7-suWim32BtjUzbcy6FzQ04cuX2LMyTXZobIP5NqCAFgkRdWtuw1tvFFmSgXZaE9_NUnnBuM7ukHKkeQAhBSY-mnjengf8issVNoRAwuCktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شناسایی شبکه گسترده افزونه‌های جعلی فایرفاکس برای سرقت رمزارزها
محققان امنیتی شرکت
Socket
شبکه‌ای سازمان‌یافته شامل ده‌ها افزونه مخرب را در مرورگر فایرفاکس شناسایی کرده‌اند که با هدف سرقت کلیدهای خصوصی و عبارت‌های بازیابی (Seed Phrase) کاربران وب ۳ طراحی شده‌اند.
⚙️
روش کار و جزئیات این حمله:
🔹
جعل هویت کیف‌پول‌های معروف:
این افزونه‌ها نام و رابط کاربری ولت‌های معتبری مانند
OKX
،
Rabby Wallet
و
TronLink
را شبیه‌سازی کرده و بلافاصله پس از ورود اطلاعات توسط کاربر، کلید خصوصی را به سرورهای مهاجم ارسال می‌کنند.
🔹
تغییر ماهیت بعد از جلب اعتماد:
تعدادی از این افزونه‌ها ابتدا ماه‌ها در قالب ابزارهای نمایش نتایج زنده فوتبال و بسکتبال، تم تاریک، پسورد منیجر یا وی‌پی‌ان فعالیت می‌کردند و پس از جذب نصب بالا و امتیاز مثبت، با یک آپدیت مخرب به بدافزار سرقت دارایی تبدیل شدند.
🔹
ابعاد کمپین:
کارشناسان موفق به ردگیری ۷۷ شناسه مرتبط شده‌اند که مخرب بودن حداقل ۴۰ مورد آن‌ها به‌طور قطعی تأیید شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
