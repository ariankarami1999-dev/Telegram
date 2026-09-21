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
<img src="https://cdn4.telesco.pe/file/vonXj5Wlf2woTFtRWWPSCeQGB5Xwb-C2qrAHcZxBDrCnPUTPvtddUdgI75wVUdlrh8Kku3walDapTWgQEvQI0zopIkEqzkSciygf_FUAvQEZcKJ4cKBYh4xbg79XqW5Fa6RAhqhQokaKH5Keg-Q9qImlIitUPofB69S2I-UgIF7UinDSY0YoDV4ZRXKmNPPOw3TSmEnz-H-QVtR066XyPUSrNLYiwDx_2dEzNEgsXo33c9fwh6E1obWg4mQ4gAH8jiDHqsIrBjpErV_5Vx2LBmPRloPFuuTe2b_T3UHJlUM9ocx2ReV-sTW2dCNQuSSpRO58ywOPXm0jKtXnCNoJYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.6K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 09:11:44</div>
<hr>

<div class="tg-post" id="msg-3037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSimbaServer | سیمبا سرور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxWuCdHPus121vRz9AecNnu1iu1v7zKxv_bXdscifz_igyOmpHmoBXzdC_1YUjsdc6T7kzwMFKnTZTjhRM-n0Jlw_3j9ASDX2108mOVRF7AGH8hTRoeg9jMM29qogJEidegkZsMH_lV20w5auhBIs7gmrmeT3UBkzcF2DIdbALYfsNAu0kXbbeNNzIaP4rm4p7jhhPTiptyFtO0y6AVracm2PwmQzkwSArwltSGTMi2zuY5MW40HbFh7wV-ZaNe0pz_mxxkmoDbaG9rJ7uGr5rj5TbgpfuUd6KXQKD6tahbgGLsgcVlTxVgiF3XZ_ZhdqAF3yI--WI93CfIB6g41Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
فروش ویژه سرور مجازی ایران | سیمبا سرور
🎁
با کد تخفیف SIMBA20
📱
شروع قیمت سرورها از
۶۰۰ هزار تومان
📦
هر ترابایت ترافیک فقط
۶۹۰ هزار تومان
☑
آپلود کاملاً رایگان
♾
ترافیک بدون تاریخ انقضا
؛ هر وقت نیاز داشتی مصرف کن!
🚀
برای مشاهده پلن‌ها و سفارش:
🌐
SimbaServer.ir
💬
مشاوره و خرید:
@SimbaServerAdmin</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/iaghapour/3037" target="_blank">📅 22:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax7-RjGFV_WAAQPzqytjKRjDFPoVj_fiw7-aCyjiHa_qbpI4N-j5oMGlcK4kaG-IwmIblrGCUDLClIH7MKtlTyDI2dySp83IoVhW8sFu931_ExqKXs4QKGhveizwkzUXMZZ_KYOfu03E8rsj8JI9oGEeFHeJMN4WVEKLOOeY6qgZSL6BvvcSiRvsfaQnfNKLfUiOsu_QruwGuvHsFE5Rnc6DxIQs1ajqBPklT0EqQ0eSTtYsk5AgZzyuNrRId_zSNIAI05AAp6XAHHFc8Utt6-ha8jd0uN0JbohuCdNLCTR43kRH3cjRHUumCDoW2BvoevESSUHrlTP686zfYdS8JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXa-J2lbbIO1EzGZUFykCBjbAoM7GZgsrw2B4W99QlhWvCvIfCEmhbTrgYxacji9VGQH_h3PO5AWAO0uctDfd3i2A6NjIFOfUJKvkeDrNKFZkN7cU95NMx_gBXkslyHydc7mAJIDcVOzV4PQcsU2rzSBiff44GH3XOJUTV23TL26knnbon53U9PYqH1zx_BxtHf7XBXcOLzCmKyWIH0EnJLybsTTOAgaNyuGwapKJnqHbxXKYGlrtsGOEt61d23Qy_8NF-I0OywSnIjymx81JMVh9vcAq_2hzDf442iDadoRx1MmglhyL1Pm6WBc_4RsbYVW_wZs3uXFKfTKV3Lviw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTixo Cloud</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vol7A5eM0W23BwKxT1UTUtvElvnxtrevs6JnJ6ObZqDQVcpwUjgaRtjdLriDFcSmesN1JO8wzKxZuQYqs85fjXuVlMHnENDgcfPS-wLzuEB9cy8G8E83TOO-bS9CWQwAj_Nsm-3RqHsZ4upUroBgDv0WOvhy4eXI5VeJNHxJyvAls9u_r0Hs__sg14HQDanra1RHQBz8wSI0wv-aTvAAqcKKTRDS-ZLwc8Pi63QO6b0k7W-2TA8AWQgjtFTS8ILEtzVazli8_XtKFBjbDQxX04f8qEF2UYQHcQLd2lUzWKUCWdgMXvsbHAUzZ4UnizwA_xLJehMEkajSDQzMeE68Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
برای ترافیک بالا، زیرساخت معمولی کافی نیست.
🛜
سرور مجازی ایران با شبکه پرسرعت و
پورت اختصاصی 10Gbps
🌐
مشخصات شبکه
• پورت اختصاصی
10Gbps
• دیتاسنتر
مبین‌وان با Uplink آسیاتک
•
آی‌پی نیم‌بها
• مسیریابی بهینه و شبکه پایدار
• ترافیک با
آپلود رایگان
🪙
تعرفه‌ها
• پلن‌های سرور مجازی از
۶۰۰,۰۰۰ تومان / ماه
• هر ترابایت ترافیک:
۸۵۰,۰۰۰ تومان
— آپلود رایگان
• هر آی‌پی:
۲۵۰,۰۰۰ تومان
•
تخفیف اختصاصی برای مصارف بالا
💎
تمامی قیمت‌ها
نهایی
هستند و مالیات بر ارزش افزوده به مبلغ سرویس اضافه نمی‌شود.
📦
مشاهده پلن‌ها و قیمت‌ها
🛠
وب‌سایت تیکسوکلود در حال بروزرسانی و تکمیل است؛ در حال حاضر
ثبت سفارش، خرید، تمدید، شارژ ترافیک و پشتیبانی
از طریق تلگرام انجام می‌شود.
⚙️
راه‌اندازی و کانفیگ اولیه تانل، یک‌بار رایگان
💬
پشتیبانی ۲۴/۷
☁️
تیکسوکلود | شبکه‌ای قدرتمندتر، تجربه‌ای سریع‌تر
👤
@TixoCloudSupport
✅
@TixoCloud
🌐
TixoCloud.com</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/iaghapour/3033" target="_blank">📅 21:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvP_p3K6OrJTSGMFgDFVehmvK-QshaiZk29RneDk12XzI3PB-0Rhp8Bvap7WwrQJT9Nelq85Niy4e540digWP7upKHh-9DhkmstVfVL2Su1HhP-xHNL8ZLCyUS3aXyU4wFpmXpoLBqoTADEaVdtN9NthF6UL8vw7V9ZxDQego4ltba-4H2qjtYUisNMXwaxFlBjIonc86eb6LMcIwx9EFRjqdRXtkEo2Ge1M6o94LBw9RVLPxuzdJUXjTpL90mHq6iI6plJiijToGxF-jcRew0bx4ShBhnMNZR2VzLp2YxYh6UHgPigY42RNeqAUJl2fUGlRGBOaJvRb20Fb4Ke4hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpguyuO5fDyWM66DMjY1CXiOT2GCj7E_ZpZ3jYoRsLJpkofVGufA63BwA9_tYfY8obUVK0bcntQT_-Kh_Ct6x599ivblLFGavEs_Tt96I56Rr7AZ-aLSVI3vBqrXyOLBcmacRxre9oCYjKQIyluPJOTeWJSqMx0xvIBd53_aULsi-UDAKq9O7F-zujt5KuR-RLvGkSuG5FwbpgPlK9P1k-sjXXQ9LrgIgJUX9_82DzBgCq9V6lAMOxhgX_8OBvGwfGXLt3gnmuRDiME8VBVjbEA-arkTl3pLcm4wDsyHC99Cy9FfsjjCbGylGiAZzIUxQpii0Ro8lSZBJBcJL3iyfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSSZnkMsaLWf4tXm5VOz1AWAmgchHH1gm94km1k7TK9Se6Qf-aOYJ-D86mWf9Wdf_TgKtl9J7SAq5uvhkzXPPUK-8wLc53jiXSEqwB3LBtnJZNmb0eT9LEQLp4lUVUUmirsRkQNWhVEiSSg3W0X-uQWJTjg6Ei-GFcS-YszFsH3ppQAItoEWdiLJ6wh2AkWKxHvuIDOHMob9eFtO4dzGUNbxoR1pkOhFi5QYC4sr47f_XopY6Q0q6OjmIztWZrcaGdUdwTglGueCcbNRZNWStZsIgTSyC9kW5_rAWCGMnt-6imSwNSQfXpKzinRIKPHXvHIjB_GFfKGmQAvd2HwDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎭
دم خروس پاول دورف از زیر لباس ایتا بیرون زد!
سال‌ها با بودجه‌های چند ده میلیاردی گفتن: «ما با اتکا به دانش بومی و نخبگان داخلی، پلتفرمی کاملاً ملی، مستقل و امن ساختیم!»
حالا توی جدیدترین آپدیت نسخه وب مسنجر ایتا، دولوپر خسته یادش رفته حتی کامنت‌ها و استرینگ‌های سورس تلگرام رو کامل Find and Replace کنه؛ کاربر زده سابقه جستجو رو پاک کنه، پاپ‌آپ اومده بالا با فونت درشت و انگلیسی:
«Telegram: Are you sure you want to clear your search history?»
قشنگ مشخصه برنامه‌نویسه کدهای Telegram Web رو کلون کرده، کنترل+F زده هرچی Telegram بوده رو کرده Eitaa، بعد سر این یدونه دیالوگ اینترنتش قطع شده یا چاییش سرد شده یادش رفته Replace All بزنه!
خلاصه که زحمت نکشید فیلترشکن بزنید برید تلگرام؛ خود تلگرام با سورس رایگان و دست‌نخورده در ایتا منتظر شماست، فقط سرورش توی ایرانه!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/iaghapour/3030" target="_blank">📅 16:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=CPUq7CEOdRDCfq-FyWXxW3GNMuJjQfxK7QjaQOBwiy4rbQIwVw1agfOAIR87UdlpbhGgjBGxczmk-hX3Qav7cp3QMhO9iE3LffKHKQbu90zFobZuO05eGnHxtNLzRchxlaEkbEVQYHodCtm_OX7iuZojG3pmoxMPD0l6iElWqFfxbVCStZCYCSZyvixj82568cS8QrN-y6dWy_tKn3pTbt1EZNl1AIBZS8jIO-UcFYIryCw7W9uEJLXzY_mYbJ-rpAbxjGX7Kd6h0D5kwtqPz9EDIFuVa87gGp6Cil8IHhQf784f7NLiLOl5JpzBN1s1ZygH3TZmZvI-BoRROYsUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=CPUq7CEOdRDCfq-FyWXxW3GNMuJjQfxK7QjaQOBwiy4rbQIwVw1agfOAIR87UdlpbhGgjBGxczmk-hX3Qav7cp3QMhO9iE3LffKHKQbu90zFobZuO05eGnHxtNLzRchxlaEkbEVQYHodCtm_OX7iuZojG3pmoxMPD0l6iElWqFfxbVCStZCYCSZyvixj82568cS8QrN-y6dWy_tKn3pTbt1EZNl1AIBZS8jIO-UcFYIryCw7W9uEJLXzY_mYbJ-rpAbxjGX7Kd6h0D5kwtqPz9EDIFuVa87gGp6Cil8IHhQf784f7NLiLOl5JpzBN1s1ZygH3TZmZvI-BoRROYsUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3026">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrT4_zwyG40pJqJBdm4x12o08roal_OTHfuaW5LOXyvvf4z4vtq_JM5llU5_-OOBfoGVHi1ctYYoBFtGu35z2QJw8ZPrb0mO75oHmrhHYEbdEPAJ6y2u_WgPOzKIOhrYhn69SNXLT2nnVIKlQuloXKsZbtnSu1wLbdliUvyMDBpjRGI14qgTB9KOkwCyS4FiyMVmoKp-TjxSF0BWEQk500Rl2s_7xgNUCqRas1Bjol_3k3L7teSNFgtFI2zW0uqC2WpFk-rfef-hMejGD4Ft5kKdm7AwZCEbTtCmqXPF_p4hal46uGYsoEV8nQT_MtaK81bv8ojI_PLH54Sg7411w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
هشدار پادشاه بریتانیا به غول‌های هوش مصنوعی: تضمین دهید سرنوشت بشر از کنترل خارج نمی‌شود
چارلز سوم در یک رویداد سلطنتی در اسکاتلند، با چهره‌های ارشد هوش مصنوعی پشت درهای بسته دیدار می‌کند تا از آن‌ها تضمین بگیرد که پیشرفت پرشتاب این فناوری آینده و بقای بشریت را تهدید نخواهد کرد.
⚙️
نکات کلیدی این نشست و حواشی آن:
🔹
حاضران کلیدی نشست:
دمیس هاسابیس (هم‌بنیان‌گذار گوگل دیپ‌مایند)، نمایندگان ارشد OpenAI، انویدیا و آنتروپیک، به‌همراه کاناتیشکا نارایان، وزیر هوش مصنوعی بریتانیا.
🔸
شکاف عمیق میان رهبران فناوری:
درحالی‌که داریو آمودی (آنتروپیک)، سم آلتمن (OpenAI) و دمیس هاسابیس خواستار ترمز در توسعه و مدیریت ریسک‌های مرگ‌بار این فناوری هستند، جنسن هوانگ (مدیرعامل انویدیا) با هرگونه توقف، کندسازی یا قانون‌گذاری مازاد مخالفت کرده است.
🔹
نگرانی از پژوهشگران فراری:
هم‌زمان با این نشست، استعفای دو تن از محققان برجسته دیپ‌مایند و آنتروپیک با ادعای «مرگ‌بار بودن پتانسیل‌های کنترل‌نشده AI»، موجی از هشدارها را در محافل علمی و رسانه‌ای ایجاد کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/iaghapour/3026" target="_blank">📅 16:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHgwHNSaiQVaTZntye0JGZD2NesntSmqMHiRp-ubLnJrZG1eUvkUdQl6fwI06eJx_UOhYtPMmdXqaza7ZXVjtN6h1LwBjjd2ORvtvyKA4kQt1UA4Mf1YOWE-jrqHNFKo9CSiN7h6l-QnOs0Z_uWHRL4iOTl7VnyuNN_Hqj2y-Uk56sdPgp4fl57SqWPvEXs94V3el-NUgZat3jwdKIARAG6wRPBfwYvLMTTjpeXM9HqrfD_dXgug8RrW9q135lDcJfOAxYocXoSBvc0pj-zrwcgkSWRDe1_vBthnwkHNAIe5pN00rGFia8JQLVtyTNxB157ys7ACJGugr-9cRagC_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spEvkW7i44fpyTFAvwo2umAx3XmR-RWTE4dkwQePqd8nFUhe1zC0avs4Jwnc4jozmXM1_Lmm_d673JXd-iQWxrDHO-sP67TdBsfVMXA1DW_T1quAT94hJuF44vh46Mkfcov-HUUkmc_rQVRjt0Y8FkQwFGOMgyc0rn1zppk4fuW8uKCSgklj8ZuqZjVNeIwAQJ_i-24wA93_-zvuHFdkAwhUz5yrIcMxe9SgN3trchhSmKrJJcSP-Nq1FIiXQCjSTM_Em574ywZ_kORkbwEdyWkxNiEhMWlMDfNgIuLBuJwOXB4kwQIwROWIF3t2kfDYkUgQLqUOsaq6zHseSrCjPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKm4b1jZjUCL8uCVM-_Eu-EI5woCC9IU0CWXLzYDodhK0ws-LdDdo2z4jR2407IPGhTU1OB76NKHRkqhgz_ivltD46DuhDb6kEqMUVKFqJ-ywwxY_qCeOyU1ZGfMX_4EwzsImW2XsWfyBv5Q1eZuM_IVwXNKUJJSjFCjMGZbdF0-Yt0ylerR7rkhXKcCxq9igVrxfVE5Y-HUZgKzZsmZRyj6oc6OlC3vqRMYUdO9Il301pTJHkwS9Syv2cBUQCqBw8CGElNHqkNdvMCz5VhTrUKv9vAbPYCghHvut3jr4KcqbDbQ1cBkbanwQ4gqBnfqUkiQ_Ek1gJKVtdotdwcCUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmazpOFpKKjKib-hRASdRaqmJXU8qCVGPWkucwFYYL8tGpAPCM48Ha3hUOTLdUUh-_-jsEbTSjFb7evUK6r6wIJ7btiZmcb83CAFH5FI99qY3V4IlhADsPl5i2H82oY_S9ouk08-yd9xjZWNBl47hf_9Cy5sZ9GM5CocO-ulsF7_Tkoh3BnHeA1lNRupReZPHuVtfuYcNRr6io4PyCOy1FjZGUt3Dh2bXNilNRNlVGUpnpb0PQmG9h3Tod7ScW3I1ePnzYE3FohPDmbqwdxFhF4RJQWm0WbTuLb1v6JBZ1v-XsFzCMs5zUfo11_ofc18QC9QtR1D5qoUtHutcv6HNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqQhFYs2SXSuBtQEiLOFdZS9EGEATyOGwNUCzezSGprLA4hvULddVNB1sH57U7mHLk0vLUgfo8VycH0PtCoigzQzcgiIVqPgsccG6Gp-cDzpD3-GqPnhvgkmZIr_ibMSRi1b0dVah3GIcHk6i_a_7I-YU0WvyTNxqhEhhsbm-qT-XFKXMfEuWbBTD8Y2MDcF2II7vSqczPUjsot_tYS5Op-gcXVl2JzhC3VP8krivCD9bDynEua67E-Mqrfnjj5gvPmrj1bqTmLKK1n73j91b8t-a9krO7BQrKjQ4TGToLcvlykPiSarFkPBVuFiK8-QGZwHahAjYmajbWMdjUZU0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7YohBn9cPc94a2NySbh9pi0qZ6LNrIpafPXCZkeGkXcRx2f32mGNTu4PgMr4R7baqbmOuq0UY0RjLqJHH6NJXI8xZ-amAq4-vwnMWzZMubaBVFzWyva5LwShzSbmqX0MB7-elewg3k_g74U8v25IRt7ftKmvU0DLaY2N-sCzBReArHn235PvTPMT6Dq_hO5MexvgjLVhh7u-fvKgOqwXmVO7HhWD3w9YexCCfFt4gTg8VqoahXmXqx4e1adp0RrjsmBVEIBBpYukJBIyOI0FF4pLTNJnrN9tmOA2Wl9RJqoxeHucfCO1ZoeahwoGWFuRhBtTR87eIlDFrFvp77DXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=vNJm10q2KohaW50NjIn_dCraaggqnITMPgMUA8ivsbVrAtEC8zXAs0aSSbMSL5aPuUgAm65dY2uqr0MLQV0rtUCZeZbqgNhnpc10F-JTlFoSVxIycFXO0e0TRLHQQz6nVzq7RUvWpHx5nkUrmUgK_hymPh71kJFP2Ou2U5PeV1yJDWHDhbt8Q3REulN4uo9DW9qEUZtCatJWpeBS20YVF8RVxVzNqFBPCiN_T7kEhg1VCJ0Woo47MVA_nPl2157MBCQJs-V24LXwBLkNuyt2ysCjzkSu4K374wV26HBCNBFxBvM5iM1A6VDvZP9cqCndzMBk0TeBBr9plqH3BY-2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=vNJm10q2KohaW50NjIn_dCraaggqnITMPgMUA8ivsbVrAtEC8zXAs0aSSbMSL5aPuUgAm65dY2uqr0MLQV0rtUCZeZbqgNhnpc10F-JTlFoSVxIycFXO0e0TRLHQQz6nVzq7RUvWpHx5nkUrmUgK_hymPh71kJFP2Ou2U5PeV1yJDWHDhbt8Q3REulN4uo9DW9qEUZtCatJWpeBS20YVF8RVxVzNqFBPCiN_T7kEhg1VCJ0Woo47MVA_nPl2157MBCQJs-V24LXwBLkNuyt2ysCjzkSu4K374wV26HBCNBFxBvM5iM1A6VDvZP9cqCndzMBk0TeBBr9plqH3BY-2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_CUx4g9-GLOZGdT8sHtBM0KJ50CbuBRzx8FY23RPl7mVxaqYukI3o3mcFnjvw4ZoYltcyCRE0GY8jk1I0d-VK4gIXduH6tVbkU9Zx3iSzKcaASmECqlTGQTE_oiRPqGZPMfDQZ7k2OmEFk04lPAe7HCklRmig9NCNdGxwuyYhB6LnTxvhHq7pJc22vo-vgR9jDlsJnFxK-UyFHP1GFE2j4AAeDAzhn-cBbbHb4FosBFfEZW9cFlrhJHiBaxV_0_Mj77rtISAIN4qXZd5Ygu9tfswy6tEiROmlZY9Jy2fUhsme0II0YYO8WoRbJh-G9TJayPQk-a-luYNbzHH4L87A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmWDgYNRuS_Qs5M9gPFZTo5JkbxXOfYN_Iy1EF2TPsf63t-YgacVFnFrkzqBs8aOvBKi9utrsn7ruDPjYdzJ1ngUFP4ZXCDmIapPp3ISuUJdz1LQKgc4aPvtz14eWI-PEUnag6xsO8rdcHU9OnaVRg4UBGz-uRR20yI_AnWUJnDAMvFq4XbWw8qQtUlxf-letVgR6qJYjDuGueMKhEZIo6SbEfxT-eKsrt4R2bWsEa0VZUU42Pc_hdRdQXgKbzbUx3OCHXJWkRBQZwrdaCq7eiNs1nnLG5Xg2tXP3FoUhxGt5C1MHPfKGwsjYFMxTkax4i-h9IAKjIONJeg-xF7P1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmZlLfjgyIuFY7-45WEDmQDRFYeHaLwjjVbbCqHG5MA3FXUafXHS-TzRLSzglzFNwV3W3sasKLdGuC0W9nEhoe_hx4YLvZHK65nnKG_B26FDkkoaOgfoIqbBp3wiP6D4cHmA1yfpSi3BYQ2wkuHjuLYSXRKYHKcU9lk4fZyEzs_3kr6fVut5QVLPTVroDdpyOT2aHNvP2WwLDYxyv8PQulWMomGu49Bv9FtXwV727F7U0cLHGlhyMnYQte3MpStPJL6xjFF55Sw7SZAiuxdn1_4svRcK96fC7qGP1vTHbHf2jnFyxP66BnCrGn4jcHbC3qOYiB8hBK2a-HegaWrnzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHozjFQTIbvh9C1GZR5erUO3XlZMI5qJlQ6wE-6-Ri6Kfuo11DeQX3KerIeoi4Nnpro_COFLHRpCjL4ldP4uYuvu9fL46yB7UpeN27m15hFJUEnwVe5bT9CRSM3C1M5j7-SLXopEIFoLDvvN8M5EehKDiF49tVCyB7VtsarpnYfdZuw9CLV5EBfKMJeNfoalgqqa2rI5rlxmBPs3f5svvzDldQYEw_qsWFPXuGXcuQCVfILHjIHJUNOU8KsVIth5uE9G7byIWF_0htNjeV6XkBclA7CFfUXJVkrvWoQZVMcXv41st7ekHd-GNnk0v7AO5Pzvz7qC9McfPDju9ttb0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD7oNkwOBznMVjdS75gRCPWWaoRvkZb3uYFvOe2tCYTZngCUXY87dpntLLvcIuau75PoA-L4M1eNAC9DiHZryAmsEL6o16ocQNmPwmb7WNIqfkqyRxmI19Bbw9xg3pqgupwRdt6vivH0jry_xxuiLnnqItcOVNfdVUDl5W5FxL-lRk3X71-dzKpjM01XFg7ItG8Y3lKHIivLwgkwoUYrLdJFaHjIQMEFcu7pC15yW_SNKtU8QkGbWxRxkJa8fOwV8ONPHNlFKEqQZvfv3IBEO2QdeiomhDFJTO9ord030hSzdNxyld9baucnwamb-M7tyUROtdXl0gMf9tT85LnrKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONrvf2XbGynM9Vft9fKmnWpSuLlj73CdO-xqbKArhyeDdSuADRxPAJHwmLXxda883ZZnJ-ERdy8ChnrtdM7tegHstiHoRZBmf4LNNvUtdwcZqYt7bjISkk4p038xnRpZWvyGJh_fJ1uZsITpGQbLEdqGYcpZS0kWk2Pg7seOFooJxRseKGoXVnOqNW0j12pbk-mjADaJRm4ftZIrpbpIcnFY-fxqKeWzRgioyincKkHt4tFxtqsWiVTL_IDeluACkxGHgEslRxaaPHoECsp-vZIUOtKLJY5HLhyk775t4Gz3yxXAcZyUq2zbXlFpM3Ru6KvPaq14jtLll5XCvTesIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دستور وزیر ارتباطات برای بررسی و رفع محدودیت‌های پروتکل IPv6
ستار هاشمی، وزیر ارتباطات، در جلسه شورای راهبری شبکه ملی اطلاعات خواستار تعیین تکلیف سریع و رفع محدودیت‌های اعمال‌شده روی پروتکل
IPv6
شد.
🔹
نبود توجیه قانونی برای محدودیت IPv6:
وزیر ارتباطات تأکید کرد اگر مصوبه قانونی برای محدودیت پروتکل IPv6 وجود ندارد، اعمال محدودیت فنی روی آن هیچ دلیلی ندارد و موضوع باید فوراً رفع شود.
🔸
همگام‌سازی شبکه با استانداردهای جهانی:
هاشمی اعلام کرد شبکه ملی نباید در تقابل با فناوری‌های روز دنیا باشد و مهاجرت به استانداردهای بین‌المللی مثل IPv6 از الزامات توسعه زیرساخت است.
🔹
پایان نگاه دستوری به فناوری:
وی با اشاره به شکست پروژه‌های دستوری مثل جستجوگرهای بومی، تأکید کرد فناوری با دستور پیش نمی‌رود و سامانه‌ها باید توجیه اقتصادی و رقابتی داشته باشند.
پ.ن: سال‌هاست به بهانه اختلال در سیستم‌های فیلترینگ و رصد ترافیک، پیاده‌سازی کامل IPv6 رو توی کشور معطل نگه داشتن و شبکه رو از استانداردهای جهانی عقب انداختن!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3003" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdW4K0FBlSicmPO5vuROOeWaN6lLY57-Fccc_1ehJrXR3eQiF5dFZC_4Sk0jzBbbFnXzcsDw-SEF1g402HKH9AnDvrgS7KBitfb6nfIGmQ3TZCTuEx3X7_8SMx7j1qjbkzHcbBAAsGNXZaHFAtNq8QEyjj3wOmWGIjDOCU8lzRsGgZ7_OKTyLpSOPzBF2sTUBca2n1aPzRnv3LkHOmrZBRm5Dj9n-wud9J-9_hO6jli1Xn29p-tjs8a6xuxx-gCM7xHjUOycRbNuUc-MCINnv8ui6YpkQxS54iNe0kxg1cGFvBIBG6oShHtR1aA94uIGF5HduBYJvCL-TWp4hPpWxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHUe6KC_dLeeXsxcFzlHNcOgzGDaPsuFthKB1wtSQbDTM3LfWgeURkxSIFuXKbd377ikbpcMp5OX6nZakYWGNYExPVvEFevLjjil4urj19gserLoFuI7OupWzen6n_M3trbM6Lcd-VAocwUkGFtIBz33AvC7cS5dSOYDYpSsgbFPDlvdsIH6xxr5l-Dmt7eAh1hUpg6TRCVSBkLIDqdd9KfVSLl04-OmSnUxpGr8kXtkGC8b88sumSoCcdvjjAE2QyWsaqDehpVUrnuJVg-f_KLEl24GeXQY7oszWQNdgw9aTSZ6J9LyS36taUTArhAGBSAYjYtvxMLCcy4hfVhK9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=T2PUTIXeIuHmaJRgyUcZIxiYSNpP81DiWn2FJmouHpP2XK0LibXHyhfxeKUYvincaq8Dug33VnFEFE44qWscQeoWLJ9JrEeDs9wz0uR_2cp3BWkOwo1ts-xnT6ltTChXKz-ZQAGzwzQ6IHetMcx9oWxB9lviAjWkSKRkov5lH89NCEjf3m20fBSu53lRQfjD6Wa5hIXAeZemEP9xTUHSJ170k7ZAH5lStMMTSgGtNocQ_fCXtBSyhz4PqrP7gbWWZjk5Gv3rV0kLimkI8653yJg2zDVhIzArCFlQZS5pI9uguZE-x7WxYO1CskkppAAM92fMBx1eTonokrYkTyislw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=T2PUTIXeIuHmaJRgyUcZIxiYSNpP81DiWn2FJmouHpP2XK0LibXHyhfxeKUYvincaq8Dug33VnFEFE44qWscQeoWLJ9JrEeDs9wz0uR_2cp3BWkOwo1ts-xnT6ltTChXKz-ZQAGzwzQ6IHetMcx9oWxB9lviAjWkSKRkov5lH89NCEjf3m20fBSu53lRQfjD6Wa5hIXAeZemEP9xTUHSJ170k7ZAH5lStMMTSgGtNocQ_fCXtBSyhz4PqrP7gbWWZjk5Gv3rV0kLimkI8653yJg2zDVhIzArCFlQZS5pI9uguZE-x7WxYO1CskkppAAM92fMBx1eTonokrYkTyislw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umjlz1B__ldGPFRIi83HOjV4tNchaPmaJ1hW41gs6zM5Su_c_GBMP4zlldmhNajfUDyyMhvXs-hPpiSdCtUuHdGiGqpHrljwseqM5D-_HMJlvfz3woavk5bHQyGgKCQE4ntDVXA5jKpdCGTmiWlVSQfmxGFIPi0Pg3g8ccg1NPPNwEqmiocAgdV4o8D_FZQvru4v3ySwd2uANgg1N02DsBBgU-wc0j2hjoWdv4HmUzO6_8vm01SBW8ScGiWbgT-5cPDbhVDDwZAxeNXc9vcHc3oMf9FB4Krfgu1PtB3_qCYw_YB1UCg3pIVUjVnoC8h8uiK1aavBhx1DPSge4wucjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=BRe8HrcoWLJ0QxxRq7gum8fkE0x2IXLb3vf0ArcJhlmZMCCdbmy5IuJpM_0bFOHhtnWlqk9nnQfuVOpUuIWHAVztomMfEXnL4HkfEK5ZwQbcsDRt1qRiYo_daY_DbMuquN_NisxesBq_JAoihM6RbwExGD8fP0MonEnCcgbWl-BXCRyGpMVjKRn8EMpckH3T6vKfXPImGE2xT-wd272_UAYkydrfn8_vmrpJQB82XY0n_56s_Wewx0iX-JrIHxTd6jR7engK8PByEKWx-MgktTUhUh1IWv-PPMwiQhh8kVMp5P47agw3ZsFTAo9_LNi2sCnrfQqoTlTjCQ_y294drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=BRe8HrcoWLJ0QxxRq7gum8fkE0x2IXLb3vf0ArcJhlmZMCCdbmy5IuJpM_0bFOHhtnWlqk9nnQfuVOpUuIWHAVztomMfEXnL4HkfEK5ZwQbcsDRt1qRiYo_daY_DbMuquN_NisxesBq_JAoihM6RbwExGD8fP0MonEnCcgbWl-BXCRyGpMVjKRn8EMpckH3T6vKfXPImGE2xT-wd272_UAYkydrfn8_vmrpJQB82XY0n_56s_Wewx0iX-JrIHxTd6jR7engK8PByEKWx-MgktTUhUh1IWv-PPMwiQhh8kVMp5P47agw3ZsFTAo9_LNi2sCnrfQqoTlTjCQ_y294drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgTaGKk8oRcudXwDyeSibK2ReVM0KdUgB_K3XBboBoc2F4LZlEOhc-Oy2KlaVXf6n2crBAqT1cHrcTGmkVQKg5DHKAWnY0Pv42jzzfSRKKntrqhCKoBt7Ud800yUnxFtoODXvnmdN11fmb-CeJpFxn-ptalf7WyCq6nx5bgFp57mdwWAl_It4sbPGnwEskK-gIKotz3tn2lvPH9Ek-ujO1FS_wtsW9_rXCflqAR5oPIyTbyJCbW2Ks5o7-PTYtRjTh8Qh7hpPGntXD7K9vfb6cmJua44kLmkDi6gdUd1qT2XjCKK_Qw2hmG_dGBp3eKrVHtju3_AJpatOHD-k5xlcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYQ4U8IRUwNuBoEVaFjpBhzlHRyMnEqbAFNWcKKKp9p8zZXWe0Ek7tLrYibTD0RMzZzwJuR9cqSxWsvHeeNqpV8A08Euib9svDL2yeIQaXdhEL56JkZSUTeoxIWvPAwVhpnwzLtWLh77RBwEQ1iPlGQxj9VG3om1AFL_EDNBeSp-b7UAXkxKAZRXuj5B_CvZsthzJD8kwWqn6IGXJTO30sey2tD1H3bR18yGmbxrG1UYah6OVH7EttpC6mxRyw2sLlY5VxOYqI3a3h6OKWrSVE7Yx78QBOt004PqZXxegVfzY6H6Unn70wVZlmj1nCvWaujD6Uf0nCPhP8zvNFOU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ab8yWs0yN9Wo0BFMUHRzuAXYjC7b9WamRQ_y8Pl-4o9VBUsvACS7ydwMNlGPMY4dZpZ9wcpk-Cyos4NPpAgZrirNL_vSf0wM_Dcby7uyFIZGZtKrLgDRmDx-5ZFKjm252Gm380w7KCm-vLP_P-ILiN9kv_pCXB4v0ab5GfFm0O_TJOVqJG96moSmWW7PwVirFTo2wGO0TnezvoYVAvjhA2dOGpLSzI2npdGfJv5gL3f0L9dRIikFjqkn2vyhKLRT0ByEH4rbBxYbSoyzLEOtxDg_UFE6atA2aZ2qh3fDNyrSS_iJ9uRIkzfIihEcZDpMLgiL79V-hyLHOBsBNzlGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hj78U5zFPfnDwJAlILm7JuTQYHI8bqU4OEvVsr_8sGQl2yepdSwWdNVRF_IUfrOgitkKvDx-bnRuTm8m5caYQhXE0vUq2C9bjJeHDAAnAoy1N3HQ7o_1RoQ3a0Q6iedm6lDR-8TtS1M2sEVe3drLgY4NaywyWheoWxVYSLWGpDBwMa3gRkW0s5UdP2NEu7MBojkCvwOEFsAOL75pPy6Nb2WtxX5RTYfgjB2t7KMDKj7Y5b0KY2VZRVNPLpYkZMKdMpJhhjJYm8M2jzWtFL8LNobLMbidK0ynLULEgwAva1zgvdsO-xTtymsn_6srIUquqxPeKA39gkWdzm7EiAFWpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
رکوردشکنی تاریخی قیمت آیفون در ایران؟!
اپل رسماً قیمت گوشی تاشوی جدید خود یعنی
iPhone Duo
را در نسخه پایه (۲۵۶ گیگابایت)
۱٬۹۹۹ دلار
و در بالاترین کانفیگ تا
۲٬۹۹۹ دلار
اعلام کرد؛ رقمی که با ورود به بازار ایران احتمالاً به برچسب نجومی
یک میلیارد تومان
خواهد رسید!
⚙️
چرا پیش‌بینی قیمت ۱ میلیارد تومانی برای آیفون دوئو دور از ذهن نیست؟
🔹
مقایسه با قیمت آیفون ۱۷ پرو مکس:
نسخه پایه ۲۵۶ گیگابایتی آیفون ۱۷ پرو مکس با قیمت دلاری ۱٬۱۹۹ دلار، در بازار ایران به صورت رجیسترشده در محدوده
۴۴۰ تا ۴۵۰ میلیون تومان
معامله می‌شود. بنابراین پایه دلاری ۲ هزار دلاری Duo با احتساب هزینه‌های رجیستری، سود واردکننده و حباب هیجانی روزهای نخست، به سادگی مرز ۱ میلیارد تومان را رد می‌کند.
🔹
چالش بزرگ eSIM در ایران:
اپل در آیفون دوئو درگاه سیم‌کارت فیزیکی را به‌طور کامل حذف کرده و فقط از
eSIM
پشتیبانی می‌کند؛ با توجه به عدم فراگیری و محدودیت‌های گسترده فعال‌سازی eSIM در اپراتورهای داخلی، استفاده از این دستگاه در ایران با دردسرهای فنی جدی همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2991" target="_blank">📅 17:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVQWLcRXBCYQ5mnuLTbclb5JG9Lo3_Np0o8J4-3qmD_UyzxrMVcJD5MgqDISLe2iEKlkeiZpnn31E8DzmlyTYk7uTIsfPM0r4TfxK9vsghTU1K3iIZeuOtt2HFzsyjIGY4HBUgXVbr-AAqsGWzSinqLnVFJS6TtpDhMz_OTf7Z2yMcS2mzBLsJm5AR_gQ11YGy_yOJKqmuXbPrb4BuOobN625FvZ6trUQFO66YNpOL7kZNKa2X2znl0TKsBwFHzML-dLjU_d41NdEO5FhzhMRBT6uXG-3rfR3sUXT_iqnOWdmw5D6A1sn_H5aTid_MsQzxYezbExUwZRL0xe8fjpCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpCS9BXhVVoJvIzpxw6SIy0DeeFm2rTkYHp700p6mPJQpO698O-V412IEWhS3O6eBV88WPG9anxE3La1zJApFYejFnLZ9Qo8L1_umsBeN6ipJTpKYXVMQPjBDUZDa_bkASCXM46f_34fU6xnrWD6du1td78UXwUilNQpNdX1Aa2W0DRzT46m5Yto1AJPQqTJQm8koyP704QE1ZZE6SdtgnnL2DcxNKeqOzm7ouN2Nk8LpRqy_mnamydB0IhUhGxDQjaiSh19IrRBN9KoAVbBSJ741qwjPxNvwy0bKbPPAUJ5ZOnOSjutRXbo_jdgMnL_chBKRsDYLF0FxvTix-yBVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-yzyu6VM-mxit4xAk_FWJwpudvjTRPysw2Hona8jh8RPjnqD814yI3GAzH4r_CfVHr6EN3I5-YhZScMyWW2GGJI41umAnb47ICV71pOiPu8wfZyIV6p6RTTq9otMY1WiyYByOnvNnEfvMdl5Kdqb8SAO_TeLS0b8xsF2iKDcrLOGPXR3QGktD5R0CNwjcovQfAnSvqt4LLnQnyl3KqDbBtucmSQUIJxvx-zJs6JPRk5W-sG3_0YP_Zyx9jOZNL30WdFcb_KaM2CGeIG72cStFTWKkWOp9JdAALKj2seSexVieVsR07kkdSm6cTbDEBgGLYJ1NcpD9JmiZfOaFA6Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV7n2c07U_VK4WIfh8eFtqpDQZVhxEUYLi_t04woKB--gWJknZfmpvMD8X3w7_5efYRo6J8akONtGe3lxOg0I1CL5qQMmrfCk2IqinzC4HOOfXnDbC2KSAuPjkzFk3hmfzK-6NMOSwJdwflHx4v38SK_rt9fbD5GOFpkAzA7y-U2nuoRjvwZxdUokID2Kpx5ZVYU69NcGqjgzZlSq-clCcW5LMWu2Tzn6KNmw88u6I2H6TlzEO9JNiP_5UIcKlULQcmNVQGtIXxLIC-fDzv5uXF7DmwsDvWCfcofoXB0LFXfHOHxqCSiycKLOFPTde9MLQx7EryMCso8WESxn4lMew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
دفاع وزیر ارتباطات از گرانی اینترنت: کمتر از بقیه کالاها گرون کردیم!
ستار هاشمی، وزیر ارتباطات، در صحن علنی مجلس در پاسخ به سوال نمایندگان درباره گرانی شدید بسته‌های اینترنتی، از افزایش تعرفه‌ها دفاع کرد و آن را با سایر کالاها مقایسه کرد؛ پاسخی که در نهایت نمایندگان را قانع نکرد و منجر به کارت زرد مجلس شد.
⚙️
محورهای صحبت وزیر و استدلال‌های گرانی:
🔹
مقایسه با تورم سایر کالاها:
وزیر ارتباطات مدعی شد طی ۵ سال گذشته، با وجود جهش ۲۰۰ تا ۵۰۰ درصدی قیمت اکثر کالاها و خدمات، رشد تعرفه‌های ارتباطی کمتر از ۸۰ درصد بوده و در نتیجه گرانی روزافزون اینترنت مطابق واقعیت نیست!
🔹
عوامل توجیهی افزایش قیمت:
افزایش هزینه‌های ارزی، مصرف برق و انرژی، هزینه‌های نیروی انسانی و نگهداری زیرساخت‌ها به عنوان دلایل اصلی افزایش تعرفه‌ها عنوان شد.
🔹
کارت زرد مجلس:
پاسخ‌های وزیر درباره گرانی بسته‌ها و عدم توسعه فیبر نوری نتوانست نمایندگان را قانع کند و به او کارت زرد دادند.//شبکه‌چی
پ.ن: می‌گن «چون بقیه چیزا ۵۰۰ درصد گرون شده، اینترنت رو ۸۰ درصد گرون کردیم.
جالبه که هیچ‌وقت کیفیت خدمات رو مقایسه نمی‌کنن، ولی برای افزایش قیمت سریع دست به دامن مقایسه با تخم‌مرغ و گوشت می‌شن. کاربر الان نه‌تنها بابت همین اینترنت محدود و کند پول گرون‌تری می‌ده، بلکه مجبوره‌ ماهانه به اندازه همون بسته (شاید هم بیشتر) پول فیلترشکن و سرور بده تا فقط بتونه به اینترنت آزاد دسترسی داشته باشه؛ این هزینه‌های تحمیلی رو چرا توی آمارهای ۸۰ درصدی حساب نمی‌کنید؟!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2981" target="_blank">📅 17:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Q4UHzoumm9zBl4whLdYXbivTlXY1LT95AswzmTwkbhB2HBjLVCdlNgvSSx5vr4wMbEj7npF-U4osPd9Oc2XSG7XhAetmVi9vQFFVTDnD9dlIvTMs0-fLepExswb2a_EKklfn6t4rzhy72VvYF4QkEL-Vfzj07gfZ9GRSehfzlSnTMoUgOzERT1iweJODhthpeG73MmILUoRFwGd0CqEp3qmSc5KbLSUitrnGV_yJXXoxPuANQadh6L2xQc5tHfF06Zg8lK6RlXyaCJV80xG4yQ3uW-hne-wT5yTsNE9Qu9Pi6MyWilJbbM2qnib8RRVyOm4EwTye4i1ROusCFYvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZi4W4G3MLQ1t2pttQd2E_ww_5-ac0BoIou9LeEwoxlFHsQS9qt1lQbwcmYrweGYXgNRiBTCZWpofxkJ7VRPG96PkOHvfIZfeC6xmvqcHg6RU-NMQ8Xo_CK32_zQGLkuOeQl0n6U07v_oPozw0PVCX1gKYUUJnJeVsqwE-7B1XHbpDFbmZ1z20Pl7wHWYcmYtfzv2A0YQtKPUVuYqTbBVRlisgOcvU54ko9_AxYsD3zLtyzmWXJWMjcl2nQPGb0zEaJ7oF4W_apYhictrN7CUv6WrPYtFwnXqa6oLMSC843gDds-vVkhu5FGwR7nfFy0cMqtJtDpU9iBLEETOjIXUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhJj8mNGF-ll_a-4qwVJVXPkRoAVMPQjcwD9nvGxopKQTeiLZQA96vpxmGqklpN7WEpvaUvIfv-3x7bhhAHoxJY4eOAY1NRZJdOdohej0cZLlwf3N2Y1vSRgXbkgDAOXsNHjK7e8kTY6XUZ3wg25e9_i77bJk-4PndgePNaxheuOpi3-MdL0ewXt-1WTZU1JBDGbuswygEy8-umeBu9_1E98B73C3XVAqZ8wIwrRahYuu5C8TBIHGJdwTW2Mwm__zuAn149n8apRrQc7jypaEBMaYd39iTwJvf5IeBxcjh4S3k89ls4Kyl07JSpXZjXEHfO14dGigs-Vbp4zOaft2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بحران لغو گواهی‌های SSL در شبکه بانکی ایران
🔸
تحریم مراجع بین‌المللی صدور گواهی امنیتی مانند Let’s Encrypt و Certum علیه زیرساخت‌های ایرانی، سیستم بانکی کشور را وارد یک بحران امنیتی تازه کرده.
🔹
تغییر آدرس به جای حل ریشه‌ای:
برخی بانک‌ها (مانند بانک ملی و بانک ملت) برای دور زدن باطل شدن گواهی SSL، اقدام به تغییر دامنه‌های اصلی خود کرده‌اند؛ حتی در مواردی بدون ریدایرکت خودکار یا اطلاع‌رسانی دقیق، که مستقیماً کاربر را در معرض صفحات جعلی و لینک‌های فیشینگ در گوگل و شبکه‌های اجتماعی قرار می‌دهد.
🔹
عادی‌سازی خطای مرورگر:
مواجهه مداوم کاربران با خطای قرمز «اتصال امن نیست» در سامانه‌های رسمی بانکی، حساسیت عمومی نسبت به هشدارهای امنیتی را از بین می‌برد؛ کاربری که یاد بگیرد این خطا را نادیده بگیرد، طعمه ساده‌ای برای حملات فیشینگ و صفحات جعلی درگاه‌های پرداخت خواهد بود./دیجیاتو
پ.ن: اگه فردا روز دیدید یه «SSL ملی» راه انداختن اصلاً تعجب نکنید! چند وقت دیگه میان به بهانه تحریم و امنیت، همه کسب‌وکارها رو مجبور می‌کنن برای گرفتن درگاه پرداخت و ای‌نماد از همین سرتیفیکیت داخلی استفاده کنن.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2977" target="_blank">📅 17:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmqiBbWZqu0QUieffw29Q8Bx-ZL4yh35YS-r-0-tE12q2z7MuGSgmQHQnkFJYnUl_9166XTdhxJ5ciSVXaIJg8sCZLPxbH1-PxqP-92RoEPnyjtmwjnGzJiZQn9HyBmHuvuv_zLVGbXRc_7Kl1l_35nNpj-qaOnMQNL0lojXiDpL8gcd4_3c65SkFMnxc9O3PiGOxXZg8PC49B2zFDUe6MlazW9JBHps5vYxrZMUsppZqnGtCaNTbhMJoMDcGkJlEMU9TphOCKJqOb9PdI6EeypftO-qgW15Uwm1RotQNMNwLzJ7swFMgF0rlqMv-04FeWNYSBqi5nXzIqUjfXu0NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=nbiBuwuk9wvxt-lxBUyye4ZKJvFTzQexhrdf-Vik0bf_D3Vg726ti6fnK-fA6RjFXptEwGiUGp5oeP3Lte9jzCP3RctY-shiab815SjUSdgX7_WPWLdH354bFVOxZxyDDe4akChUyXrK4wv7QN1lMVtMfH181OrWU4Sz9sHf6Kmq8JjChRUICiXOx04qw1vbRS9ghXm7lGG6wwO56UhrOCUlYTASZQBHewX7nb6EiPGk-wPuFSa0B9PE2vBGpPdDEwLzCtOV1Wj8O447GaPlSPPy0yUjDRG29XgHsZRpM-iwnc7eRLRpUKhYfWvOThqDuyNfh3xLnpDKXyTyvNqXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=nbiBuwuk9wvxt-lxBUyye4ZKJvFTzQexhrdf-Vik0bf_D3Vg726ti6fnK-fA6RjFXptEwGiUGp5oeP3Lte9jzCP3RctY-shiab815SjUSdgX7_WPWLdH354bFVOxZxyDDe4akChUyXrK4wv7QN1lMVtMfH181OrWU4Sz9sHf6Kmq8JjChRUICiXOx04qw1vbRS9ghXm7lGG6wwO56UhrOCUlYTASZQBHewX7nb6EiPGk-wPuFSa0B9PE2vBGpPdDEwLzCtOV1Wj8O447GaPlSPPy0yUjDRG29XgHsZRpM-iwnc7eRLRpUKhYfWvOThqDuyNfh3xLnpDKXyTyvNqXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8QfxiLS3pB98LFP_9yUINcXslUCaL8IBnWIvLwhcRtzy2KbTp5ept2TdbPddc52t2OWzF_loCGToQFJO-DoBpPXDewhWE8291rZd8jsH_OiEJKwjh86Kq77U9jE8lNEPjYywbcE77dcWA5wyymy1kvZAWY5X7EQJ32HmdTg1R1EJOrxd8jAlE8hfds0u9MPocV0wamlXg73DZ7tWES3CVAhT4QEhDH40IH222-CUYs_Dp3iowAsDwUBdC4JkU0SihWNPA9Hgwpc2XuW3n8B4GMZ6qb6hm-lfHRPtMh52NLsUJ66Tq3ArtFSiY7SRFjVTWciu6htpkvGW2zOLSIC6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpGwRg5Lp7VEe-0y-WplWHkWXL5_fFYxn_vNO3p-1I_mSDawBIYPtvPOWpdqaaq0HoHe8J6Seiy0gZw1jm0P3RVInWJpJ2EbAr5zxqcV1HOvc1KtvK1WMHL9V6JxXF96lWFwpyAzKEJP2k8BUsSimFCVyONv33gKR9Xb6DUMO3z4wjWsk97UYWHpyby7lZZ_gggFBNri_PR4SRrK8BkXt70Hfm6cD909nWsowXqB7A1OoqQE3X_yedN3RMQmi9xBPtqmsb7jMOyOI3nbgCl4lPOnM0LAOHu5vP8FESJ4-9qhd5qJPQ_ad08e6uEFFAthSwknTKwu3C86bfYLoEDjfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqa0CxThppVtBPeoLyybl-syfgLDiHZF_Rz-h1h3JX5SXEmyJZT8eY2NNpJzl1dM3iGmtwUd1y4cr3nRz7Iz7Ahxi43kCeBG1tXft7SusSOlHUdjHJ6826syJ2wYKSPjGRa2IN0N1hzFwIUSpdD8Puxf7_DhKI2Gy6xWOjWObZOyIZc8wYAOqdUU0LGITxeEzu50WD58rJpU9GsvVhgkSO8brIWGU4j-BXW0u4ncmN2STYkqwZdq03f5rQJg51QVfi6hZ1-ITJEmHN2PGAuD4c_C-n9m3sguWXAJmdkfnPqo99AXsv_R_TJTQIoHvqjBOD39b2cEyilpPbzN5rxfbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA5qs6U-kLQ5ydefEGAh5hK9SQs5kbY9_HE5kqgWBg31dbPhenf4dz_4q7Jn509JBd-5n16qPSSgzqsFEKh4jHcICVhtx1NC3akFJzHxajdDTgwzNzdzavzrTrADumllJTuDB0vD7eOFOzsmgx8osM-WW8UlfxoxSh_q54N8Ex0lW1tJWzxKDQBu_X_NMUIApoMHxvUA0YzmXBii-U1dpbQXrPN4gSJlVdkxqNO9QljiPoSciaYuYptVcU6UciEQFPy7k5-kV83OFrN1GCmmejMXcssOomf3GPY4MnWaFCap7VZ64-IxXOA85lZCDbQ3bHzps_qaY53pOefI4LZe6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=JiZn1Fxlxz85CnmBzEmo_aZVUsu6QE4RIOnectzB9M7sXJSC7JKTeR1jKTvdgmXfVoInPsDLDGUD-TQ3aK4ft21PALf3VwjJsQ9D7-LT8v2vsoalBn2fEYZ51eLz-sm7OzwBkisFuRb5C5xe8ELekLRbaYFOtWh2GrEheh23ZbEVCgfH9MWcKYntSO7J-1qLQIFd9_6gD2gNkWiMqitLR_wCRah-JKB6d1FAqaUk2r_qfRbXzDhLu0vS-jLjj7k-hfLCst2-WN8elTIDZ4xRJ2yvRqqz7PnCkp_Tzq7_ejtbdYBKexSsLNQJUhM5KbNpY78Lr8oJnuv9WrBv3dRfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=JiZn1Fxlxz85CnmBzEmo_aZVUsu6QE4RIOnectzB9M7sXJSC7JKTeR1jKTvdgmXfVoInPsDLDGUD-TQ3aK4ft21PALf3VwjJsQ9D7-LT8v2vsoalBn2fEYZ51eLz-sm7OzwBkisFuRb5C5xe8ELekLRbaYFOtWh2GrEheh23ZbEVCgfH9MWcKYntSO7J-1qLQIFd9_6gD2gNkWiMqitLR_wCRah-JKB6d1FAqaUk2r_qfRbXzDhLu0vS-jLjj7k-hfLCst2-WN8elTIDZ4xRJ2yvRqqz7PnCkp_Tzq7_ejtbdYBKexSsLNQJUhM5KbNpY78Lr8oJnuv9WrBv3dRfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2qWQfMTvVOEKAhLjCSFplMHfKwKYNLKOpedvVJVCfUqkHoEdzSHKCz3R1wkpjgR4-sw1w2e3q-kPkCVLquZIATe_N3dMHfLYh-AyOrcdumfeqmoP7I6viILqNHQjT29sHvHiGD1-jLYWdgEzLQNuxTHXhVgIAgLDurTTnCZCkO4rlVP6rF1XFjhxVKRYVrNmnxaIc55YyZlhL2uSQaUvQGDUdaTpgmgnWSodbxgqxnn6JV8mX1lQfo2AyCdvZEKCeswVr6okR68XwgfTkea82EzRNRYaFV7DtlNsTKh_O6hjrH1IRhjl50m_2e1bTlazQ6ZuEuI4miNttai2FBBng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU6if7Gn62kLLQgi0GJzXWwI0dri3xfgzxweLplHozYT8rhUOqTe0q3ZB12SqUQvw6UcUqM620LLhKdF_I67eCJg3JfBgQwNGir90xPfUPmUTlt7e2RaMOtfbpTuf57xVfDgsvKFPLrnEUi2SdCkBLhYhxRyglyjoc-NfPpYOfaDCONDnGOMkO_H0wPR9vJ-TCAnAT5NC8HYGm1_EsgmxwdBiz4IapXALVCdWnRo4nVXUUthjFahoGy4zTLoAkrB-yoJFfUPWJ8bkkenn8xgKYP9PD0xkPmvEAqvygjDjdTuixU6xWSnh2GwFHPmtYYDJY2XsVNogE11U2xu1OV3kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pP0pT0IGORaBNOhoYogE4XdgAJiJ2hQXvSE2nAlSQGZHloVMNZ10t1q0WmU4uZNLQ0XAVOW4AgpOqyp-80QrtWgda6bEjynlpCTzhyUKUdxEWu3FHVoUpxeqoy3IYHJss2UUc5Yr2ex2TyfMjF9tVF2DK1ReDYYj1jOIzkI9BFcFEnr4t5xMQIvSZgoYlf7cEG4K7c3Y04djHaDwHr7CWLhHH2dZLdM51wKNBVnGp1Zfakih5azndFpeLSPdFBBDdNtbweTtddR75O2S_xoEuSjeQSh_6BWbUk13M5CmecS_fyv3_OYdqsHq1HyKhiKa_OUPFmz5CuoaE9Lrs7KydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توصیه بابک زنجانی در الکامپ: گیر کلاهبرداری نیفتید
— بابک ولمون کن!
— بابک خجالت بکش!
— بابک حیا کن!
— بابک شعور داشته باش!
بابک زنجانی در قالب هلدینگ «دات‌وان» (با ۲۷ شرکت زیرمجموعه) در نمایشگاه الکامپ حضور یافت و از چند پروژه رونمایی کرد:
🔹
توکن و بلاکچین «دوتو»:
وعده پرداخت کوین به رانندگان تاکسی اینترنتی (بدون تاییدیه بانک مرکزی و بدون لیست شدن در صرافی‌ها).
🔹
سیم‌کارت و شبکه اجتماعی:
معرفی اپراتور مجازی «دات‌وان سل» بر بستر eSIM، پیامک انبوه و پلتفرم «مای دات».
🔹
پلتفرم معاملات طلا:
ادعای عرضه طلای ۲۴ عیار بدون حباب با ۱۹ لایه امنیتی.
⚠️
ابهام در مجوزها:
بانک مرکزی پیش‌تر اعلام کرده بود فعالیت‌های وی در بازار طلا و ارز فاقد هرگونه مجوز قانونی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2960" target="_blank">📅 20:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZePYcPtchdkkTpM57xVNUiydjqgsSNO3A2SKyEs8ImO8bC39Ju39Zzpip0RWx4V6wRKJpuk8xoq4B-ooU3UZz9oJHyu9kx66Zda_x18_4Ay615uVhM-rIy-L7af2YFO9hmgfvggsr_t9pLxAD8_S89_-KjZcgFIXESSdlMyWsRjLEpxc25vfTKDrWzkPs41JHWfjHf00cIR9DvFJYXAnxZjoSCHUeCrmhziTMXWliGx0wAOVgBOhVWHiZl1x86Ha8IGtTTG0sIk8iJTzn4nrdPa_lIROJPyvyOFvmwV9sKtNmWajjCSoPCu_q0yhOYhtd4y2h_9r5yS2KYpPbc_0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
قیمت آیفون ۱۸ پرو و ۱۸ پرو مکس لو رفت؛ افزایش ۱۰ تا ۲۰ درصدی به‌دلیل بحران حافظه
✍🏻
احتمالا با این وضعیت دلار و سودی که  دولت بابت ریجستری گوشی میگیره که در اصل یکی باید برای دولت بخری یکی برای خودت فکر کنم بالای نیم میلیارد پول این گوشی باشه تو کشور.
😐
بر اساس تازه‌ترین گزارش مؤسسه پژوهشی
ترندفورس (TrendForce)
در آستانه رویداد جدید اپل، پرچمداران سری پرو نسل جدید احتمالاً با افزایش قیمت ۱۰ تا ۲۰ درصدی نسبت به نسل قبل روانه بازار خواهند شد.
⚙️
پیش‌بینی قیمت‌ها و مدل‌ها:
🔹
آیفون ۱۸ پرو:
بازه قیمتی
۱٬۲۴۹ تا ۱٬۲۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۰۹۹ دلاری آیفون ۱۷ پرو).
🔸
آیفون ۱۸ پرو مکس:
بازه قیمتی
۱٬۳۴۹ تا ۱٬۳۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۱۹۹ دلاری آیفون ۱۷ پرو مکس).
🔹
آیفون تاشو (آیفون اولترا):
ورود به بازار با قیمت پایه
۲٬۰۹۹ تا ۲٬۲۹۹ دلار
و احتمال عبور قیمت قوی‌ترین کانفیگ از مرز
۳٬۰۰۰ دلار
.
🔍
علت اصلی گرانی؛ بحران و تقاضای هوش مصنوعی:
🔹
هزینه تامین تراشه‌های حافظه ۲۵۶ گیگابایتی به دلیل توسعه سنگین زیرساخت‌های AI در سطح جهان نسبت به سال قبل نزدیک به
۴۰۰ درصد جهش
داشته است.
🔹
هزینه تمام‌شده قطعات (BOM) برای یک نسخه پرو ۲۵۶ گیگابایتی حدود
۳۸ درصد افزایش
یافته که زنجیره تأمین اپل را تحت فشار گذاشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2958" target="_blank">📅 18:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRutQfPmtHWddq0ioJ_xX6D7FJRDz5vEQqWzaI7lYllwM6YHsMgPInRWaOQWxGybqf8dkN5PhVD4TxDSl-XuyizHtFGnp_FaWNjmic_PTzAOzgGshxinOjI63fHpFKj6mHZx9B0vVxVIyCgZgP4xsQQfYK-DJFY5QzuzDg0QRemiB8Z-Pdk2MQ_1IW5lrifxLzLvIUQWCdpskOMlEtd7xWq5YrzkUEpbYA7Nsr7nyVWqtHr5hDPUJkObHz5OlKSChkvugvhg9rvkULjUCJJVPis0mOVbQ8NqihCVuZPwtbya4f8YjOhpDUYnDkA5pv9IQg_dfC5hWTcBIYKPjs8wRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT1vuijIzoF7Dm28ea-8V0BmGdkb_YbRnQObmYcg6HK2ZvSUrdbJHZR7I1DRiu_9SkSQNSzZynqm41FaLtUw8DAq1DHOxVTOjF7XLbmd3wVbSSd_hdCG_DyMIqvjKQCIS--FLt3BXrNGcZuGaobT9homMIy0yLMDqS2UU1REctfjCmit3dOMniCAtyder4jZ74OdFcKRxxjAoRFP79sznehYfbEbZpyzYg3YjLS1XFVpZs-qb7KeLeOMow4Jbqu-bgHDgIwq52UcU6u26xbxjYBvkHYF8jUk0ELsRMI5aQr0paf699aAkiSQR3IFLiNVKgWq5OroYC4Q2bWo31TGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7gdpnpaydzkNlFnNLn_QeCVX1hwTvdDAUOHGWt1Lg1DQvO8g5ErgKjX7jNWmcG_NidssBhlqRYBITEp8UNZWfmAshVK_SCygod06DQnQzXmjkwb5DOw6TFAode2xXjcYgsuQox723v76FrXR2WAC3IwpYh6TgZ6fkOGBeuJWPOZ80eyexrXaQVhRvu-MtWFwzku9IRcDC9JQBxZsNAFkqCL6EWAyAttfjel0OJtP-mXbFbhw9OUkFOAMIfepOoGoCybjPk4XkJ7HaPNReju22XSCjKfT4OG2x_9USFh_YHQY3JoStGH-FHeYE9tHg-y4-bP_fLNb6xXgV71BhkPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنتر ها است.
در این طرح شماره موبایل + شماره ملی + آی پی به هم وصل می‌شوند و بدون ثبت آی پی در سامانه شاهکار دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©️
Saeed Souzangar</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/iaghapour/2951" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnqnjSWKjtEIZGxC8yY78ciSSqy4qkek1sN_NjlLHCiPzbdGgpVqqjVmZhR-oyz3IApJ8EduURdlFT5PS23idr0w8VXKrCue-RHzh-13mrakZkVU1DYIdvEwTSO7yyh-9oVYby7Liel30MIxpqxUhc17gVQe0M2cpK7dp6ccffliNGpW_UrVDIjn7VPg_TWCSftTc_W_pDkjp9wBfMLfzp7ViW1Z1FL20XKPhg02SOpLFMr4EbKyDIB4IxtGxve0Uhw6I35aefcBgd0tBv1AWyzK7VYS9SCb2iySJaq2sb0AQPM0T1-jPpWarks8jpoc8Jpbx_u3KkbYv4Yw6E_wGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معاون وزیر ارتباطات: گران‌فروشی اینترنت احراز نشده است / فیلترشکن‌ها منشأ اصلی حملات سایبری هستند
محمد حاتمی‌زاده، معاون حقوقی و امور مجلس وزیر ارتباطات، در جمع خبرنگاران پیرامون ادعای تغییر حجم و قیمت بسته‌های اینترنتی توسط اپراتورها و چالش‌های امنیتی شبکه توضیحاتی ارائه داد.
🔹
عدم احراز گران‌فروشی اپراتورها:
علیرغم دریافت گزارش‌های مردمی و بررسی اسناد توسط سازمان تنظیم مقررات (رگولاتوری)، تا این لحظه وقوع تخلف یا گران‌فروشی بسته‌های اینترنت اثبات نشده است و نظارت‌ها همچنان ادامه دارد.
🔹
فیلترشکن‌ها؛ حفره امنیتی و اقتصادی:
استفاده گسترده از فیلترشکن‌ها به ساختار شبکه مخابراتی ضربه زده، باعث نارضایتی کاربران شده و ریسک‌های امنیتی بزرگی را به کشور تحمیل کرده است.
🔹
منشأ داخلی حملات سایبری:
به گفته وی، بیشتر حملات سایبری ثبت‌شده در کشور از طریق بستر همین فیلترشکن‌ها و از داخل خاک کشور هدایت و انجام می‌شوند.
🔹
محدوده اختیارات وزارت ارتباطات:
تمرکز این وزارتخانه صرفاً بر اقدامات و مدیریت فنی است و ساماندهی کامل این فضا نیازمند همکاری نهادهای امنیتی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2949" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn35JwmFWQ_Stx7JqZEdHDlsnTmYk6VEIxwYRAefyMwF2HzGFjcWOZpC0-dGr5ZmbBbBACUzqUtdSh2x5J6e2d3LSpWp8_Bl9TFDFnZA4vXG4wil-KHuJI8YZRyHfPJU_yrgIBlUbRUMjTn8b9jtKuVF_USCIxoy5AC_RvrOmzIgy7-iSfDTSCjSYkXQomNiKW83YObDuh8jcUDWETGlz25AxdamFDftl6uwHQAeKq25tKVHoZ3xKnzfM-X1QD-2u9u2AAnN0_MespNe8SEhPayovM-NFCQa2hwmjPRPGGxqd52R8oO0aWiGlG1aekUOsd2j6_Ac5RMEHuIhS2Cv4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
موضع دفتر رئیس‌جمهور درباره فیلترینگ: دوره محدودیت و اینترنت طبقاتی گذشته است
سید عباس موسوی، سرپرست معاونت سیاسی دفتر رئیس‌جمهور، در گفت‌وگویی مواضع دولت پیرامون رفع فیلترینگ، اینترنت طبقاتی و فناوری‌های نوین ارتباطی را تشریح کرد.
🔹
پایان دوره فیلترینگ با پیشرفت فناوری:
با گسترش فناوری‌هایی نظیر اتصال مستقیم گوشی‌های همراه به اینترنت ماهواره‌ای، سیاست‌های اعمال محدودیت و فیلترینگ دیگر کارایی فنی ندارند و دوره آن گذشته است.
🔹
رد کامل اینترنت طبقاتی و تجارت فیلترشکن:
تداوم محدودیت‌ها در زمان صلح، ایجاد دسترسی‌های طبقاتی به اینترنت و شکل‌گیری بازار فروش فیلترشکن به‌هیچ‌وجه قابل قبول نیست.
🔹
تفکیک شرایط جنگی از زمان صلح:
اعمال محدودیت‌های مقطعی ارتباطی صرفاً در شرایط اضطراری، بحران‌های امنیتی و جنگی برای مقابله با تهدیدات سایبری توجیه‌پذیر است، نه در شرایط عادی.
🔹
رویکرد پیگیری رفع فیلترینگ:
پیگیری موضوع رفع محدودیت‌ها در جلسات تصمیم‌گیری بدون ایجاد تنش و بر پایه اقناع و وفاق انجام می‌شود./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2947" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=kSD-JhtwU2CGXSD8ExEwTUztXK5oIDFRtlm8IJkv0-RxFLRtn8hDc-hDVb4bkbvLWEQbbzurWKUIX5037fWlsweA07ChITrdIqcDUUcf4lbPh3UT1P9OzezRDoZvwVx4sGu8vZGO9XOcW-oMwNlqijYd18qpoejI2w3ggic1WjoYN1aJ1fzZtMSmQ-BHH-3RYnmK9Vy_RZGEr2K2BYYQcCSBnIJoFn1NpS1gfXwQru-oBm8CyozBG07Ehn_-o2aQNOWwgPJlplDps0_PMVMDc3T8T2I4yu9hJH8COhbsifRMX-xITH6jahzBkq-7ApcLfDVfVEJcBTTIRvx4HwBDRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=kSD-JhtwU2CGXSD8ExEwTUztXK5oIDFRtlm8IJkv0-RxFLRtn8hDc-hDVb4bkbvLWEQbbzurWKUIX5037fWlsweA07ChITrdIqcDUUcf4lbPh3UT1P9OzezRDoZvwVx4sGu8vZGO9XOcW-oMwNlqijYd18qpoejI2w3ggic1WjoYN1aJ1fzZtMSmQ-BHH-3RYnmK9Vy_RZGEr2K2BYYQcCSBnIJoFn1NpS1gfXwQru-oBm8CyozBG07Ehn_-o2aQNOWwgPJlplDps0_PMVMDc3T8T2I4yu9hJH8COhbsifRMX-xITH6jahzBkq-7ApcLfDVfVEJcBTTIRvx4HwBDRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Beo5qJRwOktvKN25aRyN_UEGMJiw_PuNR_i6dwuXxxXqvFWxUc0lK-m_hFTTr3_vF8wnUAwP-_vzXowBkAfYRg06xFOVkijXzvKY6h23WedEuaywrHikeWOHcNAci_gXWZeAy-OEx5sdAFyzn-f83OeV4pMb7J-jRs7lytlE23yvhQa6Rn_hJDi2fE8i83BC5ufsshGs2D3rzsSWUQ_IRngpTpShPBR5gzaj7QeU7L4cQtJPOqxs2lvCf3wYLAdYf0zs-0C6o2YrPaZLf9Yz5ggoMZIrh9DaOJDlCUoYxKRqu6a60aPPgt52LRjeZhXcMJ6q06OPezZu_ISlmeUNtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmvLP1P8J0nMt_RyDeJKafAgM-zevsMmfE2kBDznDC_JVs-hd1GNtBxVK-mgxQkHOKZQMR-8IU6w_fd-tgA-D7CFAUnZPbK_RXtRsIE-BROUMUZBPNm-_qxa7Kq7XCAEQOz5ffIoUebLyAgB-KXJIR5LQ80T7Fxw91sT-taDUu4Uw-yTc2tRUR_YBadkvoexXxNch3Fpa2unqQTj-ywYgx5_NeZYxQQ6lkh8CrmuDq9VLDQH7TyMWDFd0O6hb1vr3E-oNmZRFQU1Fl_4-HNOcVd549AOJJMTUbA1Dqn2tRlZ8VUpty6BUqWBRKJAQeaZK0FSYkinLDNeXJQIchDV_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXjVda8wyYHPt8qem2mcs6_DxFF7Hrkh92CA6IwZnOv7NFeBnZ3SCgHCn45FbVgiM_oZhBo7MOsCwfAfHNcjwVKxl10gg8DRtIGXTo-ktHbFpO_UZ3q7gUNCOYBBqMxhXht2lNNCthjevFnzx-T3mG1fHREiGi9rukX-TFEWzFR3SX6Ip5BayseGMLZfPEvpdNmDnfMB9TVhs_MD0St5pOCLF-69Io_WIDQjVMZZy-2JS4V7on_RcS8oLbPczoKB0DR3Luu3JqXdG50dYvLhB-ByQNpZGG23kYjkaDIVRfODNwDFDnLtwgnDVVKNE_6dxG1NaXjkFZF_yukGDQ5fzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC5CtRc_FH8AAiw0AZUQAx15xS3eNBO4bPGneHBNipxWd_tpnx5BMckJbWBfTnH0ip4a2J1OrhlpQXp5OCfC8I5adY_AqfX9YV5xH6fPyVPHf9-Mf9FOeV2ZNxLYFvdUSViFSkXzUQy5zwnOS_U4Jbmp60najfMPZJTVevRZ2zJ2PPIAVpU7VH9x8PU0b_fJmAOVgOrtc_pAhao__0XSeFfUD50tkmDmoCzhzhjFlwhCHa6jWgVcG1wnRaLgr8fTKs2muLYJt2W5WnD8CPNPXE-nFeJuCGceP7jeGGapBfvknWJk3zY-sBQucFchkbJEpOzbtmrV7vNfagxOg1JgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDA9q3g7U7HX-Rd4fZ8LJIkXe852lhvHhH-_Iofoi2RrdDYq0zVe5sOXp5hOicK8XXSpEYVZqS7HX3seS8cvOdtEQkedOIG970uGvcDKksN_AuFiX9znicsfhFr8M_buP4EnwFj8snykEdfDWBcfjb6ez-9I0Kd3ZZxmgz2qgRwAEvcouA1v9snWUbXe6ArE_Efe9B6oQlnA6N9BAtTqX_AAvqLgLE7a_YwFnsXAl3-7vUaxsXCu3im0TnS0HR5HFcrkYun-6bZECpItXKL_Fi9hM6YXeE8oHxQbPudFXw_4FrNjWp0dlSo2qGiZ6YOYJ5bnYRS6VRAnuK2XSF53PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz3FCfJaYqj_t2F4TdedCeuNGKhj0N0XEXgkjz3HwQ-5aZHfAFJULadKTtkF40RZ9KoWrm1olLFjTrX518QHQj-M3G8NUHkiiKEAuvB1Ma19SdUxBTrMzuMom8dLHP5mg6dtv6vi3zuUkZtxI3NiXNKpqZijSzaS8vW3roXQB59QI0qz9izUXej8eioroNODyoaKAAjSLfEqyxGsbJrWQzMHxCKVZPMWdvDk0s2SaWr_LSz7FdAx8OvgnDh8jvEQ_d-y_7yQQQ3Cx7hwpjr0pS1xffvnzJ0MmqcOI8IZp-1wU_IMDGTj3QqsoD2qzotz2NZJo2y3dPIyI6DvG-EOSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbmHg6kOZLV5BnO2np9muLyfIYvqqEAw5G7zvrzHf70LMGOHSoP5iS-WG72tLZ0UjckdQF1v_H97G6_98fcT9FOWEBP3BNfYjo6rQS5BejPm_52xWsPSoDKjMqnQLH-2MCIBLRnMup4M_-hsz46QBgTyiF8lR55Unr5y_52wDDjsWz2449WpnFfe1XCQDR3CfDUePphPops7c4h-WlfSkBVQ3mELVeMFnw0MuWBFd88mD01-qlFg8cQCxjv8dIaefJ9jXmsyl61xdg_p5QlhUCjqpqcSq0xy4JYB71erz2rCEG6RNuxwduUXjAYZExpQDkjYsxiuR1LZNN5JU6lWNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJMeR8NIbv9gmn8gzncdqivEoL8SbfCANY5hOMOxnwVNht1pQi15dbO0iQ4iLlsq6dN5jFZcgnGHkc2IRJ0HOHq-eZ_jJevljB1XudRKeTovTrnhvtGDWj-4nK5emK5nh5QKCkXLdhomTPDxPae1uyz2Hq180oNfPcdhLVBfuAip6qtlxyTgY5WHWZcY7-n4SIxdvH2FCRa0m_lLf9HOeoB0RwO8znqKICstK3HlVzzRR_MeppkNUXIYdoeIl-ZtNuVP-JeFZFVoBgFJCFltiCzKD94gm4SUGKqPlmQ_xo1FOrdTo1RAuYS-ChoJCZCG1w_dliujsr12jSkfVlAgbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdMKclxyy5xSPG1cOOUGfQRXv6zcHDn9Tk5GDwhTKNzJuYdzzV4MQhq2odE9PWKGnA2te9m7-5ik_Vtj48O-_NO2w6VQn7-MVJ9FCs5fqrePGEilrlKc56_UpCFVtiu1T0uyTNM7OSSbn5F0lrJqKLAgypT3JERxn4GkZL0dXaiC2kZcPhHD6_qxIE802u7erPRn33RVbWVZTJmPR5Psm0KGZqJkT_XdZASrpuZ9WSRY0ix0-h3dbdy36F9sUtH-U2TWY_G5mWRYAzDgZIZHNjTZIafg_LFMsjAzoRH0KF9D8skbm9TUKviVDNgX5nmNhSQrLLe_o4t7OAhEIjzomw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAIAhtZa_3OdJT0vwc8GcURyWtABzIGVUeSco1D3of6vdvBDGCJxrk33LwLNAZ8HuPl2FzL0Te6k4eELPueGkd7O4t48ekG4ZpPalLwWe2bK4Q_PTrB1nLqilQwUkE8oEkIxdam2_KggDxNFlhhdO0YuMxhAhOHxjGiJg_z9gRrt1ajXyKooOmBD0EFLRsa75xbVwbhzexWG9wvZ8WJgCJRqPBQdiu4h3VGubQFYNM_pSkdVJ4225gK04tcw8FeFUvlKIBTuSVO4EdAa1_7Io5imMJcwbcBPSjOpYRx4w6_otU0m_4YLBRp-imgzYAqDuk-V7KptUsziG7jwdPzYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
لطفاً برای هر ایده ساده، اسکریپت جدید نزنید!
✍🏻
دم همه‌ی دوستانی که توی این یک سال اخیر با کمک AI اسکریپت‌های کاربردی نوشتن و به بقیه کمک کردن گرم. ولی یکی دو تا نکته هست که باید بهش دقت کنیم:
۱.
فورک‌های بی‌مورد:
لازم نیست هر فیچری که حس می‌کنید یه پروژه کم داره رو سریع فورک کنید، بهش اضافه کنید و با یه اسم جدید بدید بیرون! با این کار فقط کامیونیتی تیکه تیکه میشه و کلی ریپوی نیمه‌کاره و بدون پشتیبانی روی گیت‌هاب رها میشه. اگه واقعاً ایده‌تون کاربردی و درسته، بهتره همون رو به صورت Pull Request برای نویسنده‌ی اصلی بفرستید تا روی سورس اصلی مرج بشه.
۲.
تمرکز روی نیاز واقعی، نه هر ایده‌ای:
لازم نیست هر چیزی که به ذهن می‌رسه رو با عجله کد بزنیم و فکر کنیم حتماً به درد همه می‌خوره! مثلاً واقعاً نیازی نیست برای یه دستور ساده‌ی Iptables بیایم اسکریپت نصب آسان بنویسیم.
۳.
مسئولیت نگهداری و امنیت:
ساختن اسکریپت با هوش مصنوعی شاید با چندتا پرامپت ۵ دقیقه زمان ببره، ولی پشتیبانی، رفع باگ‌ها و حفظ امنیتش کار راحتی نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
طرح جدید «نظام‌بخشی فضای مجازی»؛ از جریمه ۱۰ درصدی درآمد تا لغو مجوز پلتفرم‌ها
پیش‌نویس سند «طرح نظام‌بخشی فضای مجازی» با هدف تفکیک وظایف تنظیم‌گری، تعیین مجازات برای پلتفرم‌ها و تعریف حقوق کاربران نهایی شده است.
🔹
تفکیک وظایف تنظیم‌گری میان نهادها:
مدیریت اینترنت، کلاود و دیتاسنترها به وزارت ارتباطات؛ پرداخت‌ها به بانک مرکزی؛ ضد انحصار به شورای رقابت؛ صوت و تصویر فراگیر به ساترا؛ و اخلاق و ایمنی الگوریتم‌ها به سازمان ملی هوش مصنوعی سپرده می‌شود.
🔹
ضمانت اجراها و مجازات‌های سنگین:
شامل اخطار، انتشار عمومی تخلف، محرومیت ۱ تا ۳ ساله از تسهیلات،
جریمه نقدی ۱ تا ۱۰ درصد از درآمد سالانه
، تعلیق و در نهایت لغو کامل مجوز فعالیت.
🔹
مهم‌ترین مصادیق تخلف پلتفرم‌ها:
نقض حقوق کاربران، رفتارهای ضد رقابتی، عدم احراز هویت معتبر کاربران پیش از ارائه خدمات، خودداری از ارائه اطلاعات به تنظیم‌گر و عدم رعایت مصوبات قانونی.
🔹
به‌رسمیت شناختن حقوق کاربران:
تاکید بر «حق دسترسی به شبکه»، ممنوعیت قطع یا دستکاری ترافیک بر اساس اصل «بی‌طرفی شبکه (Net Neutrality)» و رعایت رده‌بندی سنی و حقوق کودکان.
🔹
سامانه حکمرانی مشارکتی:
الزام به انتشار پیش‌نویس مصوبات ۲ هفته پیش از تصویب جهت نظرخواهی عمومی از مردم و کارشناسان در یک سامانه هوشمند./
مقاله کامل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4p2z_LMA29k4XOBx8qsbEy17wi2QkPCtrT8DUJbMlLDFenbkiqLsd7_6QcMigmK1NONyF6G2Cf2sBOslfAJZJadmsdjVk5MR5U2oD-TAgATrFRENF1DM4BFKILqEOdtMD_ciluxguSoioM_cjkC1n0jEgkW2ibS1rWh4EmNLs6EUdjJ1hkaY_WxSfyTphBOVVQO9eNxAJvslTDDEv9xmRU4bsIwpepshL9MQ0GMygtmYy45DWXYtAXhTQU9w_WADj8FK4yb1JTb6Op3InuiKZwVfJ5OPvlCfjOIXmKmKr04YC13Ou6PFq4sfWV6u_VkZ2qTpu3ylHzCHw4SloqgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی تانل سبک و بهینه Netlink Tunnel
پروژه
Netlink Tunnel
یک ابزار تانلینگ سبک، بهینه و کاربردی است که امکان مدیریت کامل و سریع تمام اتصالات را از طریق خط فرمان (CLI) فراهم می‌کند.
🔹
تشخیص قطعی و پایداری بالاتر:
واکنش سریع‌تر سیستم در شناسایی قطع ارتباط و اعمال Reconnect خودکار.
🔹
مانیتورینگ و آمار ترافیک Live:
نمایش لحظه‌ای حجم دانلود، آپلود و مجموع ترافیک مصرفی.
🔹
گزینه Optimize:
ابزار اختصاصی بهینه‌سازی پارامترها و تنظیمات شبکه.
🔹
پشتیبانی از پروتکل‌های متنوع شامل TCP، TCP Mux، حالت‌های مخفی‌ساز TCP Stealth و TCP PCK
🔹
پشتیبانی از اتصالات وب‌سوکت WS / WS Mux و WSS / WSS Mux
🔹
انتقال پایدار روی بستر UDP + FEC (تصحیح خطای رو به جلو)
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc23T_xPckAlgB-Bk3pW87_LR3GPRZ-z07kiDl4zg_bcCWJTDKSxi5OVB2Q7gziMqAk3pvU-5Ob1y2sB6fjXmeAZj5AoY51AGRf_61Bw-ZV5gWEEW_cW89S-HJUv03BLEVGFUFn_cXisGZWPTMRc55Hzy6opaawU-bIgFx6sJDl8njhGqc63HHitEG5D1pu1XcvW6SmO8mLdgZFE9AHPNpGDHlhoJ9acT3Z9E6UfVZoaIa9X3SyzO4masGHXbK3OM_J5Bg_dEfkTZXM-2vg6voJ2b1KZTvKYUvDwAYrCO8ITJOdc2vZR6UT2QDnuwHeFkN90v7duAKzdbSbUGL7Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
معرفی DayLock؛ گاوصندوق دیجیتال و ‌امن
پروژه متن‌باز DayLock یک سرویس اشتراک‌گذاری پیام و فایل بر پایه معماری «دانش صفر» (Zero-Knowledge) است؛ یعنی سرور هیچ دسترسی یا کلیدی برای خواندن اطلاعات شما ندارد!
🔹
رمزنگاری سمت کاربر:
تمام داده‌ها مستقیماً در مرورگر شما رمزنگاری می‌شوند و سرور فقط کدهای نامفهوم را ذخیره می‌کند.
🔹
پنهان‌نگاری پیشرفته:
مخفی کردن امن فایل‌ها و متن‌های حساس داخل تصاویر (PNG) یا فایل‌های صوتی.
🔹
رمز فریب‌دهنده (Decoy):
امکان ایجاد یک گاوصندوق جعلی برای مواقعی که تحت فشار مجبور به باز کردن فایل‌هایتان می‌شوید.
🔹
قفل‌های هوشمند:
محدود کردن دسترسی بر اساس کشور (Geo-Lock)، شبکه اینترنت (ASN) یا تنظیم زمان مشخص برای باز شدن پیام (Time-Lock).
🔹
تخریب خودکار:
قابلیت حذف برای همیشه پس از اولین بازدید (Burn-on-Read) یا پاک‌سازی خودکار در صورت عدم فعالیت (سوئیچ مرد مرده).
🔗
لینک بررسی و نصب در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVgNO_oLfrQ_xBVwbLufnH7peMx-uXgOe_UnJNSqeZDaf5ubyN4Mxgnv3C9ERTg-0M7mrHw2wfhMd3tWbOHsG6NKnJoh52vUdYeUp2g5mULwI5TjtBhlm4hHfFv9YQ73tizGXIJtfA4qmCRd4J8EFs1AZkBnGpZWgQwT855WOP943Viw3XRzDkyZJ_ucRj-BGkqgXgUQnrBi2bemQb6CYC-PPhDeNZh7qtMIwNUqn8PwprijpPFZLP93AGr_MFt9J_DrmJNPtkFuoi5xS40-sN64ZdMRlMGqlVELO723vzVCBzdVo1yVHeqGEbU_-5UfjoLzuY6j27zMOUER4lBeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPIjwPDjZikd-JSpZE23GAjLLujJbpkt_2HWyMirepkC4Q5B2ndw_WEpRRz_BhBXbgLWXqnnLL1-ITXBSrDcBZAxmfuPCq7gsu4mtTIWA7SA4_5_XT0XYwTSJmeLWlRlUN-daHcJq5BgRb2jtXd3Goyd2t7qyBoD8ah8hY8hof5oGabGaCINPkapvikMzCuxr92woOyjAioJD6TRb1v5eDBiuXvAgVQYY4NgFczStj2f82a_P4ur7TcEGgINBpwE2slVA2mF8R_oSzdZobjBkbV174zl8wuTKJSydi2rPVkpTENfFTCxhmDgSD5lqGQeuFeIQqVAwtTtq40YqRqdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آپدیت بزرگ ۱۳ سالگی تلگرام منتشر شد؛ از فایل‌های درون‌متنی تا پیام‌های خوشامدگویی اختصاصی
تلگرام هم‌زمان با سیزدهمین سالگرد فعالیت خود، آپدیت جدیدی را همراه با قابلیت‌های کاربردی برای کاربران، مدیران کانال‌ها و توسعه‌دهندگان بات‌ها معرفی کرد.
🔹
پیام‌های خوشامدگویی:
مدیران گروه‌ها و کانال‌ها اکنون می‌توانند بسته‌های خوشامدگویی شامل متن، عکس، ویدیو و جداول بسازند که تنها برای کاربر تازه‌وارد نمایش داده می‌شود.
🔹
دکمه‌های تعاملی درون پیام‌ها:
با به‌روزرسانی
Bot API 10.3
، توسعه‌دهندگان می‌توانند دکمه‌های کنترلی تعاملی را مستقیماً داخل پیام‌ها قرار دهند و امکان اجرای بازی‌ها (مانند شطرنج)، آزمون‌ها، نظرسنجی‌ها و سفارش کالا را به‌صورت زنده فراهم کنند.
🔹
قراردادن فایل داخل متن:
ویرایشگر پیشرفته متن اکنون امکان گنجاندن فایل‌ها و آهنگ‌ها را درون بخش‌های مختلف نوشته فراهم کرده است (با نوشتن بیش از سه خط متن فعال می‌شود).
🔹
افزودن امضا و پیام به هدایا (Gifts):
هنگام خرید هدایای کمیاب (Collectible) با استفاده از Telegram Stars، می‌توان امضا و متن شخصی دلخواه را به هدیه پیوست کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🛑
یه اشتباه خیلی رایج و خطرناک: «هر اسکریپتی که اوپن‌سورسه امنه!»
سلام دوستان عزیز
✋
همون‌طور که می‌دونید، هدف اصلی این کانال معرفی اسکریپت‌ها و ابزارهای اوپن‌سورس برای دور زدن فیلترینگه. اما یه سوءتفاهم خیلی بزرگ و خطرناک بین کاربرا وجود داره که وظیفه خودم دونستم حتماً در موردش باهاتون صحبت کنم.
خیلیا فکر می‌کنن چون یه برنامه «اوپن‌سورس» هست، پس قطعاً هیچ بدافزاری توش نیست و ۱۰۰٪ امنه. اما واقعیت اصلاً این نیست!
متن‌باز بودن فقط معنیش اینه که کدهای اون برنامه برای همه قابل دیدنه.
این ویژگی به خودیِ خود امنیت رو تضمین نمی‌کنه؛
بلکه امنیت زمانی وجود داره که متخصص‌ها، اون کدها رو خط‌به‌خط بررسی کنن. اگر کسی کدها رو نخونه، یه بدافزار خیلی راحت می‌تونه جلوی چشم همه تو همون کدهای اوپن‌سورس قایم بشه.
من خودم همیشه قبل از اینکه اسکریپتی رو معرفی کنم، تمام تلاشم رو می‌کنم تا در حد توانم و با کمک هوش مصنوعی، کدها رو بررسی کنم تا مورد مخربی توشون نباشه. اما یه مشکل بزرگ وجود داره:
👈🏻
اسکریپت‌ها مدام آپدیت میشن!
🔹
یه اسکریپت ممکنه بعد از اینکه تو کانال معرفی شد، تو همون چند هفته اول ده‌ها آپدیت جدید بده. بررسی تک‌تک این آپدیت‌ها برای منِ نوعی واقعاً غیرممکنه. این یعنی ممکنه اسکریپتی که ماه پیش کاملاً امن بوده، تو آپدیت امروزش حاوی کدهای مخرب باشه (حالا یا عمدی توسط خود سازنده یا به خاطر هک شدن اکانتش و...).
💡
خب راه‌حل چیه؟ چطور امن بمونیم؟
۱.
هیجانی آپدیت نکنید:
هیچ‌وقت به محض اینکه سازنده یه آپدیت جدید داد، سریع نرید اسکریپتتون رو آپدیت کنید! حداقل چند روزی صبر کنید. اگر تو آپدیت جدید بدافزاری باشه، معمولاً بقیه برنامه‌نویس‌ها زود متوجه میشن و گزارش میدن.
۲.
استفاده از نسخه‌های تست‌شده:
سعی کنید از همون نسخه‌ای (Release) استفاده کنید که روز اول تو کانال معرفی کردم و داره کار می‌کنه. تا وقتی اسکریپت فعلی‌تون بدون مشکل وصل میشه، لزومی به آپدیت کردن مداوم نیست.
۳.
به اعتبار پروژه دقت کنید:
پروژه‌هایی که تو گیت‌هاب ستاره (Star) بالایی دارن و افراد زیادی اون‌ها رو فورک (Fork) کردن، معمولاً بیشتر زیر ذره‌بین متخصص‌ها هستن و امنیتشون از اسکریپت‌های ناشناس بیشتره.
۴.
گزارش موارد مشکوک:
اگر خودتون برنامه‌نویسی بلدین و کدهای آپدیت‌های جدید رو نگاه می‌کنید، اگر مورد مشکوکی تو آپدیتی دیدید، ممنون میشم به ربات ما پیام بدید.
در نهایت فراموش نکنید همیشه حواستون جمع باشه و به هیچ ابزاری، حتی اوپن‌سورس، چشم‌بسته اعتماد نکنید.
🛡
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkwgbqFFWLDG3VeJor9XPfIO6jblNl_mjJOKOdVoPOmVwZfUIaZ5Uum9OkzN0FU6k6JZ-GovaabylzZ0OrLlcGa2I5y7kwbW57LVPQ6k0IB0kQEaQj1H9ZaUFva2WQtKGJeVpSFzvmguGkFPRnXKzMtGRBHeW1U75OAP3955xLTX_IU5erOEmy2YPHuTd6pd0TUva2FoGGS2f-C3V4qIra8K0an5qBpaPqN_N4DTTfDjdb9lGoY0LcAazodNiUgpk96xFJ33SrIvNxLjGt5OOYFVdeaEWMkIoAhkxYuGB7EFcTva-BbPozweZNOaZ8bwVYd7Lv9JYxE7nVx6TYQDjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoGr9FVOEggi0y1VWobORUjGd52OZqvfURS_3LCQNLMcBaa6nfCR2FObvAhaVOvGVOHQ6zKT09Qbldz_IoUN71xpsXkExvrhXzY99krjcLi5TgcozaeplDAkj9P2XyxaV0A8dEd3am245RsXOBZPf5RN2KIqjT_Bqb4udKwKTW9o9LE_Qq4MywkwdqgIW3y9EqzW-awWlI_2torvsKHCeOEEa1bLqZXBBq-U-LX-fNfWUDo9hG7irOhOX3BxMiE6tXCDFuf3UqLaRTyyufXNnr7_pExVN7oMSrnKhgQh6PUAtEPGddh051oRovtfdY8eE5Yl4JMFJejBkT2uRqQxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وضعیت اینترنت این هفته
🔹
بر اساس داده‌های Cloudflare Radar، ترافیک بین‌الملل ایران همچنان حدود ۵۹٪ سطح عادی پیش از قطعی است. برخی مناطق مثل مازندران، کرمان و آذربایجان‌غربی افت محسوس‌تری داشته‌اند.
🔸
اگر این هفته با کندی یا قطعی مواجه بودید، تنها شما نیستید.
منبع: توییتر سایفون
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlBxjkxaIKLqCWZojT88zYJyl4c-O7OlvCkpiT-K7FIB1zzdR39qqOW8pswzeEl8iYXtoN0fKHdWpp8TOYYt61KAEaAavyvJ4QZK9BPM-QEdiUPKPo5Ll79MpgeH_FQhLrlCKxMX9NO-201O3aWJ1sdkZ0fDqxg6eP1AQlFBhEJsSgC7dOOAoOS6bP6Aj2dCX68Yf2Icsqp4TuBOZFyjBHH7JJJu44PcVJP_SPpv26FxaGFFyjsYFrHguyJ_fH7MYhkqDhxzmI_PCtEK_uSVcgGo6Rzv3I77--XmDPjtFYlXgLwBRvWmsAAjYo1uK_1F_htEd25B0co-IdMHeD8L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت پنل و شروع فروش در ۱۰ ثانیه! (معرفی ربات پنل‌ساز)
🔹
تو این ویدیو یک ربات پنل‌ساز رو بهتون معرفی می‌کنم که بدون نیاز به هیچ تخصصی، فقط با زدن ۲ تا دکمه می‌تونید پنل اختصاصی خودتون رو تحویل بگیرید و بلافاصله کارتون رو شروع کنید.
🔸
این ویدیو یه پیشنهاد عالیه برای دوستانی که پیام می‌دادن به خاطر شرایط خاص یا مشکلات جسمی دنبال یه راه درآمدزایی هستن.(می‌تونید ربات رو ۲ روز تست کنید و بعد از تحقیق و صحبت با پشتیبانی، کار خودتون رو استارت بزنید).
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/2920" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=oVd28sTfgh5lyViHQXJ9n7jjDoi4m2Z5HpMtuiawQRX6ktpLz7O7NJHUlzGsWGNZ_ZgDNJlAaWkZjSMyVHEPWfpBFDpXEflpgPhCoVAOfhkjo6szL4ZcBd3sW8NoeSz6EFuWVD2tQm0DcF35C2wtQjJwN3EBtRj2Md30OXX8qUZsfVmzbQ7LH3Wx3x3HOLoapaK__rvpNNiQqfTtlEtvaBdcLeJUasnNF6PBMkgL2Svg4cRve3bZYWc4u7JCr0rhrrMpdmP5ELe8hoEgybyTORD68vbi2EOI9Z_COM1N3coOOPuic7BrLKtUgvA3od_NT-2iFqUlcV2s1I_qLNd2kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=oVd28sTfgh5lyViHQXJ9n7jjDoi4m2Z5HpMtuiawQRX6ktpLz7O7NJHUlzGsWGNZ_ZgDNJlAaWkZjSMyVHEPWfpBFDpXEflpgPhCoVAOfhkjo6szL4ZcBd3sW8NoeSz6EFuWVD2tQm0DcF35C2wtQjJwN3EBtRj2Md30OXX8qUZsfVmzbQ7LH3Wx3x3HOLoapaK__rvpNNiQqfTtlEtvaBdcLeJUasnNF6PBMkgL2Svg4cRve3bZYWc4u7JCr0rhrrMpdmP5ELe8hoEgybyTORD68vbi2EOI9Z_COM1N3coOOPuic7BrLKtUgvA3od_NT-2iFqUlcV2s1I_qLNd2kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
علی‌بابا از مدل قدرتمند تولید ویدیوی هوش مصنوعی Wan 3.0 رونمایی کرد
شرکت علی‌بابا (Alibaba Cloud) رسماً از مدل پیشرفته و ارتقایافته
Wan 3.0
برای تولید ویدیوهای باکیفیت ۳۰ ثانیه‌ای رونمایی کرد. این مدل با هدف رقابت جدی در بازار جهانی تولید محتوای ویدیویی هوش مصنوعی عرضه شده است.
🔹
پشتیبانی از ورودی‌های متنوع:
امکان ساخت ویدیو از روی متن، اسناد، صفحات اکسل (اسپردشیت)، اسلایدها و صفحات وب.
🔹
پذیرش چندگانه فایل‌های مرجع:
قابلیت دریافت همزمان تا
۱۰ تصویر مرجع
،
۵ ویدیوی مرجع
و
۵ فایل صوتی مرجع
برای هدایت دقیق خروجی.
🔹
حالت تفکر:
پردازش هوشمند و تحلیل دقیق‌تر برای دستورات و پرامپت‌های پیچیده و چندمنظوره.
🔹
حفظ یکپارچگی کاراکترها:
توانایی حفظ ویژگی‌های بصری شخصیت‌ها در طول صحنه‌ها و سناریوهای مختلف با خروجی‌های بسیار واقع‌گرایانه و پرجزئیات.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2919" target="_blank">📅 16:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2918">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Gm9pk_uAz5q8jnSNWDIT5Emzn_3BMN-0yDW5p6KnZS3Lf_z9wIf7tQMGy6-3FmZj2MceLNY-Io1vX7B1iR0dX20qf6Es_9Vbc9G0Lz8kehSvv1EoMDbvTiTydCOBa5Jzws6Do48qFFPowAFIUtkFXPxrI-vRQq1XhlikBdGpGpWkn0K1iupK3BJrxSZUr51rn6buwzjlUItEzQX8YpUD5lML7OMS81DyBvX8_G0zIuBcHSDkvzYOAgo6tWe2885Y61ejg-_OVEl7HbbfczEMF81IFt8zOvZyoFg50LyE6H_bMQo3TOzYJL-aEO2j6Oeq5onEH9Srj8VgLX-YoDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروژه استقرار PasarGuard Node روی بستر ابری Railway
پروژه
railway-pg-node
یک Wrapper مستقل برای بیلد و دیپلوی مستقیم نود پاسارگاد (
PasarGuard Node
) روی کلود Railway بدون نیاز به خرید سرور اختصاصی است.
⚙️
معماری و نکات کلیدی راه‌اندازی:
🔹
مدیریت پورت و لیسنر:
کانتینر یک لیسنر از نوع TLS اجرا می‌کند؛ متغیر پورت (
PORT
که معمولاً ۸۰۸۰ است) از سمت Railway تزریق شده و اسکریپت
start.sh
آن را به عنوان
SERVICE_PORT
ست می‌کند.
🔻
اتصال به پنل اصلی با TCP Proxy:
از آنجا که پنل مدیریت خارج از شبکه Railway قرار دارد، باید از
TCP Proxy
استفاده کنید:
🔹
پورت داخلی:
همان پورت داخل متغیر
PORT
یا لاگ سرویس (مثلاً ۸۰۸۰).
🔹
پورت عمومی:
پورت تخصیص‌یافته توسط Railway به همراه دامنه/Hostname عمومی.
⚠️
نکته مهم آدرس داخلی:
دامنه
railway-pg-node.railway.internal
تنها در شبکه داخلی Railway معتبر بوده و برای اتصال خارجی باید از آدرس TCP Proxy استفاده شود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2918" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2916">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVwD2tV7kKyyLN_JBnmUgxdX9GR5Kxb_QOlDHzSg1i2S4DC5YGE8a6DF2Bi9dOz8Icq7SgZOLI92RVxORo5gTO1W1YcNCSQiD2PxywWJOWE4E9Kv4qAl2fNiRGvNCaBeroAf49HB0-Xqp6F0h1h2l1a3pahS9STds3-96KGJBk6E7RwCefnc4pDyj7Dh3slwRQrpXVzeqtp_oajNxHKDhJaNbGKDSplCWaG3dJ9bHUyPQWdcNd2TR1lFamwjrYujdr3nGA15lqefh7aXhePasSniWz6_Ls9SomeoVClUxZuBb7FlDw0iQ2RNS-RkHzk-8k_13pNgPNIH3vsrJDge6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی tproxy-server؛ نسل جدید پروکسی‌های وب برای تلگرام
این پروژه سمت سرور یک طرح اثبات مفهوم (PoC) از سوی تیم تلگرام دسکتاپ است که روشی کاملاً نوین برای عبور از فیلترینگ ترافیک MTProxy از طریق مرورگر داخلی (
WebView
) ارائه می‌دهد.
🔹
پنهان‌سازی در قالب ترافیک وب (HTTPS/WebSocket):
اپلیکیشن تلگرام فریم‌ها و رمزنگاری استاندارد MTProxy را حفظ می‌کند، اما تمام اتصالات TCP را از داخل یک لایه انتقال مبتنی بر WebView و در بستر امن HTTPS یا WebSocket عبور می‌دهد.
🔹
چندین اتصال در یک مسیر:
این سیستم چندین ارتباط لاجیکال را مالتی‌پلکس کرده و در سمت سرور، رله این جریان‌ها را مجدداً تفکیک نموده و به سرویس رسمی MTProxy متصل می‌کند.
🔹
استتار به عنوان یک سایت عادی:
دامنه سرور مانند یک وب‌سایت کاملاً معمولی و عادی HTTPS عمل می‌کند؛ تنها با داشتن Secret اختصاصی، صفحه پل ارتباطی پروکسی فعال شده و سایر درخواست‌های عمومی فقط وب‌سایت اصلی را می‌بینند.
🔸
سازگاری کراس‌پلتفرم:
این ساختار محدود به سیستم‌عامل خاصی نیست و هر کلاینت دارای WebView می‌تواند از آن استفاده کند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/iaghapour/2916" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2915">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8YVILW_6J7BHuuqG-7LwkL-GfMlMXrXSw1amLYAc6pfrr09ragpYEWqURFLKAB3_HdXEVoTAygqZxG6_U8dpRMay7RDV6GzNuzJORynBNfe9rSRJJCmlxeiUb72DJMdV5DKIppm1Y6XVAQ6Ulz5Axc-ykMrL013MM2LSMUyobGaZgvNOKe8otjzc3SWvvy66M8tlYJ0yT4Y_7jGtUp7zYGvwQGD8jKOWdh9DekamdZdH6qOlOO8AZ9MlYdS8KnakTu4eAwMtuC0YQ8KsoVMzRRVC6t8GmchW8BvP5l1ph6TINdDJcNfyTh2bWcd-Ayh91h01s6_egT-EvmSpfQUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حدود ۴۰ درصد از آهنگ‌های جدید ماه ژوئیه با هوش مصنوعی ساخته شده‌اند
بر اساس گزارش تحلیلی پلتفرم
SubmitHub
و با بررسی بیش از ۱ میلیون قطعه موسیقی، نزدیک به
۳۸.۵ درصد
از کل آثار منتشرشده در ژوئیه ۲۰۲۶ با مداخله هوش مصنوعی تولید شده‌اند.
⚙️
آمار و نکات کلیدی این گزارش:
🔹
سهم آثار هوش مصنوعی:
۲۳.۲ درصد آثار کاملاً با AI ساخته شده‌اند و ۱۵.۳ درصد شامل قطعات تولیدشده با AI بوده که سپس توسط انسان‌ها ویرایش شده‌اند.
🔹
عدم توانایی تشخیص مخاطبان:
تحقیقات نشان می‌دهد ۹۷ درصد شنوندگان متوجه تفاوت میان موسیقی انسانی و تولیدشده توسط AI نمی‌شوند.
🔹
هجوم اسپم صوتی (AI Slop):
پلتفرم Deezer اعلام کرده بود بیش از نیمی از آپلودهای روزانه جدید آن به موسیقی‌های هوش مصنوعی اختصاص یافته است.
🔸
واکنش و مقابله پلتفرم‌های استریم:
🔹
پلتفرم
Bandcamp
انتشار هرگونه موسیقی هوش مصنوعی را کاملاً ممنوع و مشمول حذف اعلام کرده است.
🔹
پلتفرم
Spotify
از سپتامبر نشان اختصاصی «AI Persona» را به پروفایل‌ها اضافه می‌کند تا شنوندگان آثار ساخته‌شده با هوش مصنوعی را به‌راحتی تشخیص دهند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2915" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkSpUleVTZB757XoQQDF0MBoAIEYwXLjLYX4TVjr9ZK2BqPR9ziTFTT2yrkfnujzRDiFnDYRwlrG1rNXwLtgqgybSWsOu539l5L9HDpEdRBTSyih_1_fUVDTOZm-O_Z_fxI1uXp7-evh6azwvns1858VEHJ6D6cUwwMHjZIb0LAT0OF9f82AlDQQqjy6rzx9phkc7zeqx_8mNtre49gEwV_TOHBKfrXwRzw85-uw3c9dC3dG1zozFiDRFD_g8-yQuUj2RxLLmpIDDFTmcMConsIhPOcgWkZZ35hSbzNdsOiXmfsaAlvT_ZJoS9cRIddyGaGfc4SBFlk0ybVrzAarUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دسترسی رایگان و آزمایشی به مدل‌های هوش مصنوعی Qwen در سرورهای Hetzner
هتزنر امکان استفاده رایگان و آزمایشی از دو مدل هوش مصنوعی
Qwen3.6-35B-A3B-FP8
و
Qwen3.8-27B
را برای کاربران خود فراهم کرده است که می‌توانید آن را به نرم‌افزارهایی مثل 9Router متصل کنید.
⚙️
مراحل فعال‌سازی و اتصال:
🔹
۱. دریافت توکن:
با اکانت خود وارد سایت شده و به آدرس زیر بروید تا یک توکن بسازید:
🔗
آدرس سایت هتزنر
🔹
۲. اضافه کردن به 9Router:
وارد برنامه شوید و یک پروایدر جدید از نوع
OpenAI Compatible
اضافه کنید.
🔹
۳. ثبت کلید:
روی گزینه
Add API Key
بزنید و توکن دریافتی از هتزنر را وارد کنید.
🔹
۴. ایمپورت مدل‌ها:
روی دکمه
Import from
کلیک کنید تا مدل‌ها به لیست شما اضافه شوند.
⚠️
وضعیت فعلی:
در حال حاضر مدل
Qwen3.6-35B-A3B-FP8
فعال و قابل استفاده است، اما مدل
Qwen3.8-27B
با خطا مواجه می‌شود.
©️
aleskxyz
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2912" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💡
راهنمای ساخت اینباند در پنل 3X-UI روی سرویس ابری Railway
نکات تگمیلی درباره
ویدیو بالا
☝🏻
با این ساختار می‌توانید بدون نیاز به خرید سرور (VPS)، پنل
3X-UI
را روی کلود
Railway
اجرا کنید.
🌐
مکانیزم عملکرد پورت‌ها:
پورت‌های ۸۰۰۱ تا ۸۰۵۰ (وب):
ترافیک از طریق Nginx روی پورت ۴۴۳ مدیریت می‌شود (مناسب برای WebSocket و HTTP Upgrade).
پورت ۸۰۸۰ (مستقیم):
از طریق
Railway TCP Proxy
مستقیماً هدایت می‌شود (مناسب برای Reality و gRPC).
🛠
روش اول: ساخت اینباند WebSocket / HTTP Upgrade (پورت ۸۰۰۱ تا ۸۰۵۰)
۱. در پنل وارد بخش
Inbounds
شده و روی
Add Inbound
کلیک کنید:
Remark:
نام دلخواه (مثلاً
WS-Inbound-1
)
Protocol:
انتخاب پروتکل (
VLESS
یا
VMess
یا
Trojan
)
Port:
یک پورت بین
8001
تا
8050
(مثلاً
8001
)
Network (Transport):
انتخاب حالت
ws
(WebSocket) یا
HTTPUpgrade
Path:
متناسب با شماره پورت (مثلاً برای پورت ۸۰۰۱:
/in1
، برای ۸۰۰۲:
/in2
و...)
Security:
تنظیم روی حالت
none
روی
Save
کلیک کنید.
۲.
تنظیم بخش Host (ضروری):
روی گزینه
Add Host
کنار همان اینباند کلیک کنید.
Address / Host:
دامنه اختصاصی پنل در Railway (مانند
your-app.up.railway.app
)
Port:
عدد
443
Security / TLS:
فعال‌سازی گزینه
TLS (Enabled)
⚡️
روش دوم: ساخت اینباند Reality یا gRPC (پورت ۸۰۸۰)
۱.
ایجاد پروکسی در Railway:
در داشبورد Railway به مسیر
Settings
⬅️
Networking
بروید، روی
Add TCP Proxy
کلیک کنید و پورت کانتینر را روی
8080
بگذارید. دامنه و پورت اختصاص‌یافته را کپی کنید (مانند
domain.proxy.rlwy.net:12345
).
۲.
ساخت اینباند در پنل 3X-UI:
روی
Add Inbound
کلیک کرده و
Port
را حتماً روی
8080
تنظیم کنید:
حالت Trojan gRPC Reality:
Protocol: Trojan
|
Network: gRPC (حالت Multi)
|
Security: Reality
حالت VLESS TCP Reality:
Protocol: VLESS
|
Network: tcp
|
Security: Reality
|
SNI: یک دامنه معتبر (مانند yahoo.com)
روی
Save
کلیک کنید.
۳.
تنظیم بخش Host در پنل:
روی
Add Host
کلیک کنید.
Address:
دامنه TCP Proxy دریافتی از Railway (مانند
domain.proxy.rlwy.net
)
Port:
پورت دریافتی از Railway (مانند
12345
)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2911" target="_blank">📅 20:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhPlS53-WxmTd-tIrDRWMm8T5EQH4LbT93NT3eHjKRIa9KToK8rmAzcPmHmSpRTVo4VMAGPxUSfXvx49TG3pF-e1jX5tJU4U07A-jFEs1QhtRD2x01JuwoDtbBRoOyCCTHw9V_iScLfcH5SrNXlSSnTumUEVZ9swVaJC4tHKTo1tHcuYWT2vobZJltKrdqnvvYgHaw6IUhyLoflESROBzk2IWRCDJPNF0ps2uEtm4grkADW--dBdzFG0w9BpBmpAe6Og_9zxcLAJzTlPiKjzVRiKZIUMXSJAk2b0SQT2L6nFxu1tGqKQtgOKKnk3tEPRcLUHZ9ZqmH9WZVhicNyPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بزرگ‌ترین آپدیت تاریخ CPU-Z منتشر شد؛ نسخه V3 با ۱۰۰ تست سلامت و سیستم اعتبارسنجی جدید
نرم‌افزار نام‌آشنای
CPU-Z
بزرگ‌ترین به‌روزرسانی تاریخ خود را از سال ۲۰۰۱ تا امروز تجربه کرد. نسخه جدید (V3) با بازطراحی کامل بخش اعتبارسنجی (Validation) و افزودن ابزارهای مانیتورینگ سلامت منتشر شده است.
⚙️
امکانات و تغییرات کلیدی نسخه V3:
🔹
اعتبارسنجی استاندارد:
بررسی سلامت کامل سیستم در کمتر از ۱۰ ثانیه با ارزیابی بیش از ۱۰۰ شاخص مختلف (درایورها، دمای CPU، برنامه‌های اضافی و...).
🔹
اعتبارسنجی پیشرفته:
تست استرس و خطایابی سنگین و دقیق روی CPU، رم و کارت گرافیک به همراه بنچمارک جامع سیستم و سنسورهای مانیتورینگ پیشرفته برگرفته از HWMonitor برای بررسی دما، سرعت فن‌ها و فرکانس.
🔹
حالت اختصاصی اورکلاک (XOC):
محاسبه فرکانس مؤثر پردازنده‌های مدرن و مدیریت صحیح اورکلاک رم جهت جلوگیری از رد شدن تصادفی تاییدیه‌ها و ثبت دقیق‌ترین رکوردهای فرکانسی.
📥
دسترسی:
فایل نصب نسخه جدید از وب‌سایت رسمی
cpuid.com
قابل دریافت است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2910" target="_blank">📅 18:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=nTBCnEoSSzcjSD8psU9Lq4eVOWAUD9XFSB2VBmEoOqjb_L7I3ixawOafdqCgostYU6Vtg3PwoLzZEUB09ouGXEFnO0TGmOlzAZpwBEHRwxYp9duETHE9ASokuUFDxWaIzzkKZIBdvkEpfhujYZ8wWRXFPhn_Z7cqcNokvRkcUfQxczQCvtVATlxgAhaUPve6xogwS5teQPyeYqhxfAPIPHsU7Sd1MPvdpsxVyDiM2puOK6uWRrb1Q737xPNWvUhESfa5rH4Dcqrd7_8cTWFBLKJVgFC3fQnrKx08q5Omeq8sfNDmXjxlBq3TuoXLRgMTJaA31RsR_ueHFYpXKSUl2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=nTBCnEoSSzcjSD8psU9Lq4eVOWAUD9XFSB2VBmEoOqjb_L7I3ixawOafdqCgostYU6Vtg3PwoLzZEUB09ouGXEFnO0TGmOlzAZpwBEHRwxYp9duETHE9ASokuUFDxWaIzzkKZIBdvkEpfhujYZ8wWRXFPhn_Z7cqcNokvRkcUfQxczQCvtVATlxgAhaUPve6xogwS5teQPyeYqhxfAPIPHsU7Sd1MPvdpsxVyDiM2puOK6uWRrb1Q737xPNWvUhESfa5rH4Dcqrd7_8cTWFBLKJVgFC3fQnrKx08q5Omeq8sfNDmXjxlBq3TuoXLRgMTJaA31RsR_ueHFYpXKSUl2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره پنجم و ششم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
نیما عزیز با آیدی nimashokri5515، مبارکتون باشه!
✨
👤
حامد عزیز با آیدی hamedsalamati2286، مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسرهای عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2908" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5ZfS95iJAZndAmhZ7Nbe2s7NDGL5CBJfENAcrxY3--0dUZOtcVRmiCcc-kUlmE61CP7JLvdHSMC1hoQlITUWNkUgAvq1D-fYoLbf5KLD78oNcUL3oBM6u_cwJnjIskcmWzf1a9d1f8CSK6DkeX8TKC687OwPQATmC_n99ZY2zRJiitqmHNCO17KxCYfz_UNYF4nzv34wjNd-xmiPMXWG2_2_JZDW4S1AptmSBnj-TlyLYOOdIrFoszTLc7Wx4VVjDHUgqfv74TdzGIks_ukzpMFzZbmCDWmnsfVLqJVaTo3222em4jF-0iBfptfi0JVFbzROIEWxyEu6IgVocuVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
تداوم ناپایداری‌ها؛ دیتاسنترها گرفتار فیلترینگ سخت‌گیرانه و سامانه «شاهکار»
بررسی‌ها و تایید مدیرعامل شرکت ارتباطات زیرساخت نشان می‌دهد وضعیت اینترنت در دیتاسنترها هنوز به روال عادی قبل از دی‌ماه ۱۴۰۴ بازنگشته است.
⚙️
چالش‌های کلیدی مراکز داده:
🚫
فیلترینگ شدیدتر:
دیتاسنترها با محدودیت‌هایی به‌مراتب سخت‌گیرانه‌تر و اختلالات فنی مرموزتری نسبت به اینترنت خانگی دست‌وپنج نرم می‌کنند.
🔻
بحران سامانه «شاهکار»:
بزرگ‌ترین مشکل فعلی، الزام به احراز هویت دستی کاربران در سامانه «شاهکار» پیش از اتصال است که این فرآیند را از ۲۴ ساعت تا
یک هفته
طولانی کرده است.
🌀
سردرگمی کسب‌وکارها:
تیم‌های فنی هنوز درگیر ترمیم زیرساخت‌های آسیب‌دیده از قطعی‌های طولانی هستند. فقدان تضمین برای عدم قطعی مجدد، شرکت‌ها را میان بازگشت به معماری استاندارد یا حفظ آمادگی برای بحران بعدی معلق نگه داشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2907" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgPy1h_iS5zuzanZuUdLiI_T16xuVjTsmmYOwHbbKzCm16-y6T6ug3IJpIjfq45Id0zz8VPvIAXXbJMRfIf9xJEdYQ0ttGgxASUM0VLL5OHg-VAGYaXgVqtmAMv7XkBTIUE77UKAGcDlIvXIfcdi3Dqgb92jO5JHTkmXwCBJfBt_1reX9rVxJwTqVBd73V0m-Wh9-BiORMJM0DhpIN21kxhf_1eFyYzYgqjGZ845y7FPXA99PPNYMW9SogkGMgXe25b9tFVcupABRitH04kgKVbN7Gh_TKgu01zxXfg72dICOAif2MgHAszwXf8X0SPZ2NbzsTN3cDJa-PdjaW2xJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Tor Node Manager؛ اسکریپت ساخت و مدیریت خروجی‌های تور تفکیک‌شده بر اساس کشور
این پروژه یک ابزار تعاملی است که به شما امکان می‌دهد روی سرور خود نودهای مجزا و اختصاصی Tor را بر پایه کشورهای مختلف (مثل ترکیه، آلمان، هلند، فرانسه و...) به‌صورت پروکسی‌های لوکال SOCKS5 بسازید. این پورت‌های لوکال به‌راحتی می‌توانند به‌عنوان Outbound در پنل‌های
3X-UI
،
Xray
یا سایر برنامه‌ها استفاده شوند.
🌍
تفکیک نودها بر اساس کشور:
ساخت نمونه‌های مجزا از Tor با لوکیشن دلخواه و پورت SOCKS5 اختصاصی روی
127.0.0.1
.
🔄
سرویس‌های مستقل Systemd:
اجرای هر کشور به‌عنوان یک سرویس مجزا در سیستم‌عامل به همراه فایل کانفیگ، دایرکتوری داده و لاگ اختصاصی.
🔍
تأیید خودکار موقعیت جغرافیایی (Geo-Check):
بررسی زنده و چندمرحله‌ای اتصال و کشور خروجی Tor، همراه با سیستم تلاش و ری‌استارت مجدد خودکار تا زمان تایید قطعی لوکیشن انتخابی.
📋
کانفیگ آماده Xray Outbound:
تولید و نمایش خودکار قطعه‌کد آماده‌ی JSON برای اضافه کردن مستقیم به بخش Outbounds در Xray یا 3X-UI.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2906" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2904">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtyENdWw5hC7KYy1s9wqoeyYBXij_HXiftKhRzwtEtNB9bNWVp00Vqh3c8WvwJ8n8aAppfd5gJUNGgOGlXoDdy0xYXS6gV-GeUmU6xjNTQJeco9ouANOl6ir4mlLM6je5R8ZtLz330ZvuPil-JqRpzsRSA9vIpQjYr412X-pamPTnZPpZVI0DdmgsJ3FEkOZ7PYm9FA9ZEOnIzWO10gKdkDN5hjXI4OqWTa9B0fpNYlRF6TrvxDoHiceyTEY_z7vvci8QztdN_nSbiapOQRbtT2IP382shwKHxlu4JUKXfgpqcjtfEw1-Lxa1m1hMeXutmfp6fa0cbxj2uHjzbVssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن شخصی بدون سرور و دامنه (کاملاً رایگان!)
🔹
اگه می‌خواید یک کانفیگ کاملاً شخصی برای خودتون داشته باشید، ساخت فیلترشکن شخصی بدون سرور و دامنه همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور بدون سرور یا دامنه، پنل X-UI رو راه‌اندازی کنید و برای خودتون کانفیگ شخصی بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.(قرعه کشی این ویدیو با ویدیو قبلی باهم انجام میشه)
#آموزش
#فیلترشکن
#رایگان
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/iaghapour/2904" target="_blank">📅 17:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUPUpitP2ocKQBNPRMPl1sAThDKhIhBIk_zUrUwmAh1RFPFEGNWNoW7JRd56Lasm6yqwO6hzMBzeeMomdQ6PaayMCwWCj4KLhdiqzd97h-fzAY_vuGWHI-vAmTQbakeeQmYvG5l83LaKj1msJ8v5h4_lZAjTXIrYpcrndoS9z7SC_u09MeSitKqRqB7scfXc6tGgcO0Z6O7DmP3VJBZglEQINX98xv-xqMnVUjEQ8558VurlUWhmyjrsqASPVyQ2Eg_FyQH9oRxJwa5Op7FtBm4cHTgoEXIUqYq0va4C0NtyrgmY6QzlmEtQHm78GVhdJsqG8umb-_ofKPsJepMapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استعلام سیم‌کارت‌های فعال به نام شما با کد ملی
بی‌خبری از سیم‌کارت‌هایی که به نام شما ثبت شده‌اند می‌تواند باعث سوءاستفاده‌های حقوقی، امنیتی و جعل هویت شود. طبق قانون، هر فرد حداکثر می‌تواند
۱۰ سیم‌کارت فعال
در مجموع تمامی اپراتورها داشته باشد.
⚙️
روش‌های استعلام:
📩
۱. استعلام سریع از طریق پیامک:
— کد ملی ۱۰ رقمی خود را به سرشماره
۳۰۰۰۱۵۰
ارسال کنید.
— پیامکی از
CRA.ir
حاوی تعداد سیم‌کارت‌های فعال شما در هر اپراتور ارسال می‌شود.
🌐
۲. استعلام کامل از سامانه «دولت من:
— وارد سامانه
my.gov.ir
(یا اپلیکیشن دولت من) شوید.
— پس از ورود، از بخش
دسته‌بندی سازمان
⬅️
سازمان تنظیم مقررات و ارتباطات رادیویی
را انتخاب کنید.
— با انتخاب گزینه
«تعداد خطوط مشترکین تلفن ثابت و سیار»
، تمام شماره‌های فعال همراه اول، ایرانسل، رایتل، اپراتورهای مجازی و سیم‌کارت‌های TD-LTE را مشاهده کنید.
⚠️
اقدام فوری در صورت مشاهده سیم‌کارت ناشناس:
اگر خط ناشناسی به نام شما ثبت شده است، بلافاصله از طریق اپلیکیشن یا نمایندگی‌های اپراتور مربوطه نسبت به
سلب مالکیت یا سوزاندن سیم‌کارت
اقدام کنید./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2903" target="_blank">📅 16:01 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
