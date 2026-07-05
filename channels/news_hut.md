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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 205K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWfMuvNit0HsvO3Pxtlz12OvOMhduVo_V-I0vSVKlcTTMKxcjE04ifcggWR8TPpbnHnUCb2o3vtoPMQAuO90ppvBd-N78OKINmhGriabBW6YWkrJ3MSaY5qyVV4eMBohz_aj5lupTZd4CeNyvkOPKVyqC1f09R19eUIwEq1Rg1mm0ZHxBTKeu536PtvKgsI9fxt1N_GDvt6Hm7iOzt97rl0hDfrgiLrHOjK95KZ29GzP-vQNzgJgvaWih2WYAOSlrcIQyxD2t2SPykyJhFQp5mlXxLtyMQAY7MLDMIb1FfsZjj5wE7jCwemf05xlpfKjR0AHU6YbU0Z_3FEXDoitmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm-J8mdXqDkBr_GYo_c2Dx4iJTRUUb5_JNg3BRFsh5-XoE5FFhzQ78pZ5OFEwayM-fx0qbqo0VSWFp0hQpEFhkrbx-KfjAeHdNjLAvqqt6_U-5qXAEh5FvYOSLJlh9NyncoUscHZZvN-5wBx_-8oW3LDWAspJMQQjc8I9xXgKdbh68vJa36n-k_RMVg99DBYyn9Q_QBDK4gA5Vq4XBqJ5T6A8LK989zJtdl8ZxkCtqIveLdquG--URu5HD3BpesH6_SM4P6x3XkfdH1WEyb0nKSDgj4IcpodW9RYWK93lLuj-t2iHa6BZpQhAWkweoq5LD7C5tvZqRXP-TFCo_Rnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imlaBmP8K5B94CcNALz1qLnopgVMnNhhP7CefwNXd94_raM1gkJcnzf6LgvOF748VqwOlXi5y8Jw763_f6lYIdzviBzrZvm5554MuY7HgC87d_x9hi-BMyq_k7SMaqrPdZ-dTLs_mAEnl1sqdc50tn2OBfvsfJCtEwRW_nlKrugNpLlaWjpoLpOZZvqpE8VFx77zgXx5FN2IJSJRJw_RfwyCgJ170w-gF8mTYLA3FF02GWvwNunJuTQ9-nB9IgrnUw5jg4QnmMJJA8mepfg-SAZD2dcKIXcQPFfrMULSdAsSMZYhf7yMoVl1xpSdKwKyFkM0cANdEIyQbPinoVq24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrSdbI3MRsl2wWIugJq0dRVlAXQW8fAYiacjo_jnWO6_FucEzIjs8MkV8551FR_d4Hd3OkESIoQbbKKLjn419RDZ9SuICgqOqKG4MGorkjaSR8Dsruh4cyQVO_PBhj7wO8QSvCQ92QwD3PqMl8ZjF5je40z5XzbIYunAWrfEQTmGDGO2wGfa5dS9tfOHQLeTlRMtpumS64yMM0QiVUs9w4dGmspgFHBIdIHkQFYLN31uoVSU_FszKWqe6ROh6hYTaaPN3AFrm5U37Eult-N5zNfhOkYnwE1lGSZyWhez4Pw5ziLQC0e9wphdPCOmCSn95D9o3onSODCAp4TpLrtYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgj0lbBM6XPEAKI75v5spsMaQIKN7JrXbzbrrSuDavPKpWCaaVZ_z8Z6l1KP_u0cpwZz6ETcTxBPIzMF3lcOi_7_IrhSrx7yH7VAJFVdSHVGvmfHsLoOs8tB8d3kpHUk1_W6SBUn5a_w2ScfN-QK4dKqMvr3N6KDsFqTLlTcVsxeQ3ewCx5hyVehKeyn4OHmGjhkUxYgT2_0cPu1_j0Y5txLLRk3pwzKiOG5j7N3WNptbhziuxIu0R70s4TivpuzCs3hKOsOOr5HGYp-YjPDWDC67vsLPvjtqzYoV2MXTnPmodBiBjEpAeuuMDLvcGb7nMtu1esq_y8kwiqvkZn7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3wpwJ5qVzehFZpCrX61LV87mMqTgWMiN6NFVDshzyEfedzYp__FxZsKIvCUIceTn8mquCih7uqOq5qKP1vCYoGEu5EkR4w8SHKDc-PbPF5TPy-UeZ-vWHAs1fxOGLuusegCaP2sxdxmpCdZZoUuqHCW8hbbXppv0zQQxQ44weoGkZHRETjSJDq13MUb5UdmsVusra_JwGO4NDp5bORBbi8AIn6U2FbDmPTvNmSVAsWU3o7gXIEpzBs_ohEkHYGUavrehI4qOTZyRnm0_COYI6KAXlrpBQvvh8bL9pqVTs_QS_o5CUPPbt3sH_bcVImKBfImlpP2l1nmUWrtqkV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaB0osKUzDmp6z3ij2h6F5IuJc_2UnA_E4GzGrpS17rA478rtwXPUFHwDSAXWxaliA5OoE0KWo3ob2b4wtndC1O8w6KgBVcOVb9FQI7V1LCAu6WD0bX1J_6h5v4YOyVLHc254w9_r3XQJOOIirdcW81ZkELLtNd-KG4UbbhY0Fqnbu78oov8ZcDTUckpx1yZn-i6CTWBVEtnqh3DVS5bZwGrx94r-3G7ln9ok4Vl0t6H0z9CQmjs_yHNBGoLSsUnfXOx37FraI4V1LYG4aGlWwgu3eLPyOS4s1FeP5roMc4okXDGfrnsLe2BWB2WJFL0Ilfjq1MaEyd1cYYmS7GB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJKKjAZPMdnfKhz2__gcVjCP81-6WOnDym_9JiH9qUqPy7ySkRgJ450GDHxHEJvbR2d2fTf1iBZ_IlJsoXsaG8LAtYF66Rm66iXWXDQe1735iR7Js37SUmKSKK5IeGufHbt_yIsVjG4hXKqNi0jLU23vYB008YBsWupyX5erA6NPCSZiDhac-1HYgDTIIkJXEkUWDHlNdCctDeYRNY0c_iiHt3-dQbBz9F41_HioXYuinFCwJCFeoSotuEIulVeU50CAyz2ogpbME2HNsXc23L4jQbDmfWmhYldLoOhiNydhPRZ29gw1BbtWU36hEh_YWfQCjW90YHGK6gTarL9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDfdGlSNMHmQDgPBEqpVQv-xAdkK9YR2mI6PfTwTAyJYLXu4_jHl4q7rUGmBToRT_Qsizvn-OwFloz0Ywp_RCT2651rEhJZhfaV2xFYE5njbfyeEuzXU1sRwvhHcbkmUhxCCbRmtjy-X_266iqY7T0h7rfusFGASq0_cQXAMVHJp_Wjj8Q6usDXRRBi1yhkJgSe-2HYx4_pXCyivfOuI2naDDWvOa4shwpW5zluBH_PnHDQyEPxFHdINppQ0CdqBJZZ0to0UAag7NfkfDUhA1VU8LHYGBXPc5M212K6yr7BiGvucsjKXk2L4HML9Nis0gxH7dIqyDpnrqRGKa4HjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFqfwYEnYJns9kB63zx0WRm_-ZkGOwHi2VVRSAT4fiJhYK1tD-Dagb6iLc2aNA6kPQa9ONPgH5GEtWUBZOcGDhF6H5zHA81WigGEWLB4ACAFmBz0_mjHTZnFzH_Z9fF6m9Zp_gi3o2tsJlNRJQ6PHSF1yDxHYHkN1pTXCq32vATOJdN-bEFWdhd5SMqH5U2soSXNtxUxf4xEwOPoANk3tofV8_sAZjdMyv8ix8V4Sng5KPTNovA8vniWGq3pSjqDSazUw5-WfVZAMOHBKkg2hi6FZ0jEIE9ObxKBzJ4XUOQlPurdxPeOZEuOisd-dosiaWSk3aOmEixA2TirozNEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBmHBZEDtk6vawUGHKOj5OK_4y26ViC98_XWZFOCOdZ9oRU-FJaxrXByNzazfuW2DePuPgKYqzqsoEsTmcvXqVj5Gy95VLBvqZ4cAg83VqpqEK7jh1ti9OebcgwGzh8HrPFyR3KaOHb_xtJF6cEGdCiiMWUQK8RLE1oN8q3eyPhirzl-B54OXQJ_ZtB3m28BWucv_XFRQdtdvuv7MVTmyeLtnXvrbuj1c6FTiEusRmqwN73aLZveVTFUCqW-2CpbP95zrGnGkWvrvJwxs49KLbjWeXfjE-G9hY53FwYdkZxzTjFwpICvQed0tQTWtSyEGfVRI09OtBzEi9tGimbw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=rVL-7N6zoFXWPyYl1oQjwx3nFS2FBlLlXq6v1MtXc5XQm4dhcMxrzpW0NINBi9QOBhxkK6ykFuy2fIxaie9F6uwUeXOHNfOqbvowYPn5QuL8CoJqdJyDx7LdmUOD9ewc4TmHagJUJn8F9BYuHxOvJTJVzPjKfE57eslOUgQqfG1zcNarHsVviL_2TDREdRwue4TJKHdsIf8HXMVH3DRB_DBofCGDyHiWfZwwjvjWSuXVC-wAUAMqe44YyPzAWTsUFOhBzSJ82VJMY0xggI0R2m1dXxo0zf_4r76Ainz5JOOSxEfE3SWQV09RXjAiA9LyWTiqN7NVKWJiV-26wJfHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=rVL-7N6zoFXWPyYl1oQjwx3nFS2FBlLlXq6v1MtXc5XQm4dhcMxrzpW0NINBi9QOBhxkK6ykFuy2fIxaie9F6uwUeXOHNfOqbvowYPn5QuL8CoJqdJyDx7LdmUOD9ewc4TmHagJUJn8F9BYuHxOvJTJVzPjKfE57eslOUgQqfG1zcNarHsVviL_2TDREdRwue4TJKHdsIf8HXMVH3DRB_DBofCGDyHiWfZwwjvjWSuXVC-wAUAMqe44YyPzAWTsUFOhBzSJ82VJMY0xggI0R2m1dXxo0zf_4r76Ainz5JOOSxEfE3SWQV09RXjAiA9LyWTiqN7NVKWJiV-26wJfHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hl8Z-5FdHJB_hkxGrK7UffjhJVT0sXI4y5m68KycCspYSIGvaj4AJkPaM_a3xRnNdRbfLy_hv9uHrNZqq1NQ7h61on3-4hpKpa8ga6FBl8Hf2SaswGa0jzRME8TDlYmgOcXSvvvWrqkLveR9jWzUaSou1-IOlU0YRCOgRjz-LdjAXwfwhI7E_LFsvwAIK783yCuqWqLOvoeai_M_er_OPpaMaZ13RkhF_8qpe0uzu4OCbMtImabRRSTg9U_FUoBFozwQZ2NegHv0MrrWOZTxlclmS--lFywPBQ3Lee85UIF8_MrNCmfYES7rLYiKcRStlHfy6oUpgqdlX-JONrJOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=N58GYgCAaSE4Vgb1zkPfwCoQ-05pMihXQOc5_MYN_u8LzhJeRhXJbVXCkLYAhCHc7NuKK0QUjeuHyWRSeEz6WeUTYwcpr9EyOLiSUrrXMSd8uPhAumRWIGPUdyLT3dKi7nu95-SlU3r3SvG7Ap0UhKxMfibFTCLeU_rQXbkLKUdVxqfMzWDbvodv_FcD7pq3GeUdbkzUikcJWQ5joL5_lHE7_5macRaa-RPWTWqpSmTG8ktASu3cZJaPUxpG1QsDz-gQieyDjrJo8t82HWspuy4lXTrcWyzAGUDBswpDrZHb_aNmGjk0pBH0hhTuhvKimrf6Q1qMXGm-KNLCgXGpOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=N58GYgCAaSE4Vgb1zkPfwCoQ-05pMihXQOc5_MYN_u8LzhJeRhXJbVXCkLYAhCHc7NuKK0QUjeuHyWRSeEz6WeUTYwcpr9EyOLiSUrrXMSd8uPhAumRWIGPUdyLT3dKi7nu95-SlU3r3SvG7Ap0UhKxMfibFTCLeU_rQXbkLKUdVxqfMzWDbvodv_FcD7pq3GeUdbkzUikcJWQ5joL5_lHE7_5macRaa-RPWTWqpSmTG8ktASu3cZJaPUxpG1QsDz-gQieyDjrJo8t82HWspuy4lXTrcWyzAGUDBswpDrZHb_aNmGjk0pBH0hhTuhvKimrf6Q1qMXGm-KNLCgXGpOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4aopl4KWXxkN19FFlRCgRMKg2fWoX9VL-Lwc0fHv-M7c5O4qPqmth7kRP2mQNl5nBRhsJ8IHcSJTFlEZ1hvOMc2bzO-8AwAsvwfKRmW1SFEH72iWS8dvu4-R_CA5aeorvHDdDIto-ZYWuE-EES0yXB0N9ztDetdSHvBSC95ZT6c7XCfP-HZA7sScbpJ-MYiIg2tpVxFaCe7QxI9_W4prbUFNfqPnTp-iw6_mxOXLZBxqU12ga_3LDDD-ud61o82OOUcTdDTjDDX9nzGA4s55xz48Tk6-Z623LU3Xg2m1r8o31EAo37f2y7n5eB5OodK5ng92LN5JO_0b8eElr89Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=TCt2HlngNV04t1vpfI7r_EENOe0FtteVTOlGDysMW7so7OCASokKwP5B0wRLbA6mCc8mPiqYk_iAIe0stwzR41IpZwa-2a2i_DIMBWDWJ5EzGMslhRUqMDsAtReRGfiAv7Bq7MjP5FNUDAuC_bU--t4BjaILlNacRqQ1UI4dUidBNss-2QMOIJKLDrJeRDro5VKaXXF4AWFvmhppIxFuxESFQ8FYOXIrZmYuHDLo1z0dGihRxGW5l7xkd917Cxj2SRZLFdu7mp406M5JLFlSQBHhq9Euv0-R25u92m-pPWHp3OhDxejxeZ7wHvRzgLsTiFT6eYnRlagtX3l2BgOSJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=TCt2HlngNV04t1vpfI7r_EENOe0FtteVTOlGDysMW7so7OCASokKwP5B0wRLbA6mCc8mPiqYk_iAIe0stwzR41IpZwa-2a2i_DIMBWDWJ5EzGMslhRUqMDsAtReRGfiAv7Bq7MjP5FNUDAuC_bU--t4BjaILlNacRqQ1UI4dUidBNss-2QMOIJKLDrJeRDro5VKaXXF4AWFvmhppIxFuxESFQ8FYOXIrZmYuHDLo1z0dGihRxGW5l7xkd917Cxj2SRZLFdu7mp406M5JLFlSQBHhq9Euv0-R25u92m-pPWHp3OhDxejxeZ7wHvRzgLsTiFT6eYnRlagtX3l2BgOSJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=tMmKaVuCc6AD4SGB96Yc8pGnwUcJAJcEbMc81SZxQdjBbSCI5oWUOTjKHsnGQ2exz5Aakn1MbuCcbfnfjAlqE80JEwOGzAePe6Bf6p7PG1fG2mk-9cKQT07CE3nB1_uFE4NpKt0A_YwTIJQXyJcN_lW3YneXJhFvNF3KX4dexgeMQV6OJsYj2gOTFBzPdQ-esHn-HOg51IaFPqQx5rMx28BvdNjKP7AHBOzjs9BBEiKHPbHoUPqZyBG5bLDuQySRdiwZCAUh0Gha_crGRZlYY9rTXs7goL_hI-zRpkxD2eZMwD1msLmCeNIJ8xCMI1RynYsnYXjVw2uQ-eg90JQ2Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=tMmKaVuCc6AD4SGB96Yc8pGnwUcJAJcEbMc81SZxQdjBbSCI5oWUOTjKHsnGQ2exz5Aakn1MbuCcbfnfjAlqE80JEwOGzAePe6Bf6p7PG1fG2mk-9cKQT07CE3nB1_uFE4NpKt0A_YwTIJQXyJcN_lW3YneXJhFvNF3KX4dexgeMQV6OJsYj2gOTFBzPdQ-esHn-HOg51IaFPqQx5rMx28BvdNjKP7AHBOzjs9BBEiKHPbHoUPqZyBG5bLDuQySRdiwZCAUh0Gha_crGRZlYY9rTXs7goL_hI-zRpkxD2eZMwD1msLmCeNIJ8xCMI1RynYsnYXjVw2uQ-eg90JQ2Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu1AGH8kumxlmagHxaa3KTysElEM-iLU0cdLqQNYfDrKG5B8BRlMQtAFx_Y3XExJJdCytqO4mmk72ih2wHPssexSs_a0ri6v2XRapn3Svz1krFkByav_Bkw-lmKTd1ek4KjvcYipzBEgO4Iar-5K6V79XHG7DOTg-Sr1EgZ3wNQp-0Prrs3MoQF-x89DZxthH_iMu2Lt2mRpWRuif6sR0Mu5GHn6h9wtDYRQJTqEGAAFyERsIfdcuKWAGzss4VydiUrLeicbUQcVvR44dLr8pErjcBVayBGVWn5eRqYpXvot29slvJAKDHwtyl_kkTamU6ymGTfbmrjyfzrB-aSWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cio279um1PWETkOQ8NGx95GMYiL2ZIKqM3NVXcZhpMpQdMICJMtw-RbQA4ykMQB0yAQ5bGxWgQjkFh5HX1yaM0ro7oBqk1IShbQMhBBZ1lfHa1GGSSLwJLs6TZkXSgpXnI7K5v5fSRtdBF8z1oGWDgBA_sVB94NVyyWQMhKFE0bhnDGmqMhyEOmvAyZ7YpaNX741qU2wRaeljL6W0vYxlOGx1ZyGOccIJXHu5PtKV1VnQitFY5IWCGh6QYiXN632_wffbJjjKp-IOeJtmZKoRg-B86uQDUXqEH7cjyR5uliKmMjxGfqSnP8LZB1sSHal8OGpPNRWfdli4wz24Av6ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_lvKy82BAdMju-KHBxUioQsnUU9Ec3CJFEQZ_NV8ED5GdoZ-FZB_oNIjWRqi_SuW2fVWgsdRb9yf3taNa_erHg5-69sQ0j5Dq5uNM7IQjg7O8IOExzYsbzE2LwurKyXV3T9x_K0xKL3qqH1Nv1-09W-F2oSG5JeFKbUQ9KawiH_DW8jfvJw3M_UsNtFAlGZHtYcoSHkOUphJk_pWqiDH3UpBm2o52cJN10Cw7xQbYET4mo_TRf9CZm8hBi38sEUm79UedrbCNFpuc8pzWH3oGqH9A7FafznbRSzXrkGc-mNisY9QXGAFAmG0aq95fk1yiqkXtwI0m9zpcT4YofGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=U2ysXP04DJIwJYm1cIyc06Dh6O6x2PTRCTnu7XZ3mLv0mk_xiXTIGm2hbwsqU9dG7BhIjVAUIH1_szEds9B57n4N51rxojkPUy5B5nFroeEzLNQvk9gxQKqT4y7GqUn49FrSsT4rmhwg0YYSFQFpGBhFttuy8Y2Jc-OS-MpScMNVZOizvZNorYG5G4SQZI5oodJECH2E_Jtc42TogyYvNHbwXpxNcQGowY3tn--m3jDW1IsWei0foZMXhEaspTNaQvLlEqotOgYvtEHuEhrYmYs9QW-DljwjrQHHPQVJ1gs28neXV3fpQhiv70xHJptVH38KMdLf8q-L590f6Cpjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=U2ysXP04DJIwJYm1cIyc06Dh6O6x2PTRCTnu7XZ3mLv0mk_xiXTIGm2hbwsqU9dG7BhIjVAUIH1_szEds9B57n4N51rxojkPUy5B5nFroeEzLNQvk9gxQKqT4y7GqUn49FrSsT4rmhwg0YYSFQFpGBhFttuy8Y2Jc-OS-MpScMNVZOizvZNorYG5G4SQZI5oodJECH2E_Jtc42TogyYvNHbwXpxNcQGowY3tn--m3jDW1IsWei0foZMXhEaspTNaQvLlEqotOgYvtEHuEhrYmYs9QW-DljwjrQHHPQVJ1gs28neXV3fpQhiv70xHJptVH38KMdLf8q-L590f6Cpjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=WUAkKCcM_jFaC_vNrAxeNvGzjBzYaQ6ZLqVI0MunyFOB3o0ZGXxspz8jx5Ef2zbiUPTBhRLaxO48FVuhqo9gPs_DBk80FrTkFQsjU5lj5D288OSRHuZq7-sRxgdf-V3MXNZqPs3bEUbTNwQjVnhBxVQHU7u2m_rOaOzBoy6uvKSoQp-eVA5xsDbFxa9451dhD5ihNQk8msENJUFDe_fdr91XDobvmFUGKW-CU03or3hSSutOM5o83S3bMED1HhOqaCwPLw-8sCCBfDc-KvXbQspJZIhsfOyUxXNlbaW2N6Zsu7bKNWr815yTIPFS0F2AJAdrivS61ln8tBT62FRGWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=WUAkKCcM_jFaC_vNrAxeNvGzjBzYaQ6ZLqVI0MunyFOB3o0ZGXxspz8jx5Ef2zbiUPTBhRLaxO48FVuhqo9gPs_DBk80FrTkFQsjU5lj5D288OSRHuZq7-sRxgdf-V3MXNZqPs3bEUbTNwQjVnhBxVQHU7u2m_rOaOzBoy6uvKSoQp-eVA5xsDbFxa9451dhD5ihNQk8msENJUFDe_fdr91XDobvmFUGKW-CU03or3hSSutOM5o83S3bMED1HhOqaCwPLw-8sCCBfDc-KvXbQspJZIhsfOyUxXNlbaW2N6Zsu7bKNWr815yTIPFS0F2AJAdrivS61ln8tBT62FRGWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpGrTvJ0mupGjYoRMRvHuYggEHMlCwTCdKoDj-8pFFF2vu6SL1knBGFc4gmLd98SEdM2mpKdc2H6gu6F3tsbt1C9W6H7i7x0hOk-HK-P8ddgXHfd1IhPHuk6Nhwes2gM85JND58WSRtghv_joHPHubB2frNpRSUAkbMy6N2tb5LAeqXXfdh-H8jvKi_3NQMeY5FbhTv9jZU2K4p-3xRPKJ2y7QMqL3Vrw4EESBX8TsLfZZFD5_IdrecS-W26Qt8Omxdmc4Q4nVYO0PQiqtzoxJkpdNBJ5B6KhqZe_fxQdVsVYcqBIyvWlqouhdfelrFOzpf3dMjLUbO9hgeKAnwV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es-qDDLQbQD4gjchCcz-KOMIupkPr0dzfmijOOPxtwgPAH3VPj0EDQ4los36XpGZ06qL4zIhKaEWwC6h7Dx6Diw0ZPqt5TSn5JoMYgZe842V8Tg-3UtSRllaqb7_KjagEuKOkdt28xGQhbHSOd8-wA0WaFzWVTofJnnnOY4DaFMwcjzwDD1Xb7C3Y6clOiih35dIwyBRV8anBcDT4ucw2oSnfodMeyDzPRD7_kqrsu_FLlCcfsJkh-d12Smxrbv2pVieQ6yUzlUpr0Wch6WdoeVHbSHq0ZlkT3d6Oa1m2gtxnWEY_0vZ1kSY7j3xGiD9EOVGHJpuYccBcQ5dEE527w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ4pxwUkR_IwcqxemyEsDaM9N2GSDNeFoDIyVKurVjVM_p-u9ueNysfLkP0ORmwG3MsZCYQlhVOxNPRWOwM1mB9p5Z6GUSy4N46E5gFe4CE_QltBcm6RVc4KRtYnyYRrqoUjp4CaWto8VYKJwJImnsRU-1CoWvRu7JH7Hjs3rgLgV75ce9OxtwKnwOwLJXV9laCTkyv0qTLBzn0V_g5TnYtkvxUYcLqhWbGoPbbvcoUsOExFNQY5qp4n3mGNu_A9Cg2b2pfjK30mGfx6RcWCQETZmq1B3k8YaRsvh6yCoQPueRTnsCiaCwqNTjh_MzeWvFjzL--To-dEm8D36-bjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=qKYZY7PKcmMCWrdfLiGgNdXEorVWIZ4LWeNVTLUHcghZKE8SsEqVXkoQyj3OV5TSsmkxndOK2dT_9uYMzpU3-65IY2Tpm1L7NZlRHMLsgcJYjak3wFhXzTTJucxFX0x30SvADuPEedZdstd9LbxjzwWTe_eiSfBkyFgAmakFgwnPv0Na6ehQ0iVczKU5QDu2i_jp0m50sByQr5leyJwEs9UcoVuws1nuFBHqv1ughaXE3Ky9XOJTVCo4zSrRohX8jV729FPWDRFY5d-ZnLia17947uNdTn0aFSjm4pt5tLQ1Wphm9MZyylQCulwP9X1nWXiagtx2V-E3s9kfuwEJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=qKYZY7PKcmMCWrdfLiGgNdXEorVWIZ4LWeNVTLUHcghZKE8SsEqVXkoQyj3OV5TSsmkxndOK2dT_9uYMzpU3-65IY2Tpm1L7NZlRHMLsgcJYjak3wFhXzTTJucxFX0x30SvADuPEedZdstd9LbxjzwWTe_eiSfBkyFgAmakFgwnPv0Na6ehQ0iVczKU5QDu2i_jp0m50sByQr5leyJwEs9UcoVuws1nuFBHqv1ughaXE3Ky9XOJTVCo4zSrRohX8jV729FPWDRFY5d-ZnLia17947uNdTn0aFSjm4pt5tLQ1Wphm9MZyylQCulwP9X1nWXiagtx2V-E3s9kfuwEJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=HB3tdyFv06wS6779E_EBB9abd74UoUcwkPNXz6a1-J9DINVT3BWwolxN3SZxdtQrF_n3Lfg8galVO4gVIm1JZpezoH-jsDNSz9KqvhUUJQFabx0AOerMF-UxIK69J1lw_gXWMVUiA1qZ21JP_dVhDef_WQfOudLbG0Cn2J6A1pyxqwvYxQEDyI_DqnVyN6uL_Yea_pkorcCdqLJpHonfCfe3jLp1aJ-XN4npQLGprGBHqpb-Ge39w7lZeqhd-dM8DXvO_tVd0lRefFrrr9y-7YcNhtfEfpZxSm9t7Kmq69zjCQAYgZkdI2KKcM6NYzWqfoOsyyXNl57P2whyb9DKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=HB3tdyFv06wS6779E_EBB9abd74UoUcwkPNXz6a1-J9DINVT3BWwolxN3SZxdtQrF_n3Lfg8galVO4gVIm1JZpezoH-jsDNSz9KqvhUUJQFabx0AOerMF-UxIK69J1lw_gXWMVUiA1qZ21JP_dVhDef_WQfOudLbG0Cn2J6A1pyxqwvYxQEDyI_DqnVyN6uL_Yea_pkorcCdqLJpHonfCfe3jLp1aJ-XN4npQLGprGBHqpb-Ge39w7lZeqhd-dM8DXvO_tVd0lRefFrrr9y-7YcNhtfEfpZxSm9t7Kmq69zjCQAYgZkdI2KKcM6NYzWqfoOsyyXNl57P2whyb9DKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=urS5U_BSWDxipGI54ztFkt-aA5sDNodSdtwcWHnC6WIN7NpnjeR15bUYJVBaMGRmC_DYu8vXPWhi4UuV1ZkoFuqigzYR9TLMEw1b2p6POaHDfi7H8LnUGLJyqL_8FFvboIfpvhr4wFX9BiA8scuM0kPlCqdXfNnQPUWVnD-JLhspxHYG8rQnb_m8KdW3tpezzddKaewoJQ-cKO4b4NjPSxP_6OfLVHVQKhGokoa5EnNineEY__PSNAR8QRIs8EjztBf4Sjsl9NeQTbg_qyyhN163puo5Egv5p1-6nuXGgnaVC1Nb0nwxUH2FZNTUo-4nR3Hl7QJXN2IiaP9e-IUdQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=urS5U_BSWDxipGI54ztFkt-aA5sDNodSdtwcWHnC6WIN7NpnjeR15bUYJVBaMGRmC_DYu8vXPWhi4UuV1ZkoFuqigzYR9TLMEw1b2p6POaHDfi7H8LnUGLJyqL_8FFvboIfpvhr4wFX9BiA8scuM0kPlCqdXfNnQPUWVnD-JLhspxHYG8rQnb_m8KdW3tpezzddKaewoJQ-cKO4b4NjPSxP_6OfLVHVQKhGokoa5EnNineEY__PSNAR8QRIs8EjztBf4Sjsl9NeQTbg_qyyhN163puo5Egv5p1-6nuXGgnaVC1Nb0nwxUH2FZNTUo-4nR3Hl7QJXN2IiaP9e-IUdQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5p3IHWluU2dCBeSE-K085kGfRiKUb-csCXvLLPMi9l7ekjA937xKhm5zVHvHJPQ8-2_mOG5NlDATZ5ju3zFnHaPV35x0KARlK6E0BxPYFb96Mbiu-PwmRgi6lXjRTIRASEeb-V9j1M8kIVYvSdtYDIRI1hHvitMkJEpjUX0DaU35T8HvVgbwU7ngtfTkeq-1jGvyVt5APDQ07HFDpSgXNuWV7vqZuZeOXHsTLdGxL0Sf8kFwneam4RbMXq372ycK8yFxj-fEqVvHpHJJmrZWuV64AntzhZxpv7M1NxJWbtzNVAmRFWC0zgkRDuBp6GMbH3dKV2iSK4cKK9YE2mwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=GSWpTRoXxms-jRaHl6QN_hKsMaFaInF3-uLSTZfVnnoRSCdfpnEdxEVwG7KRx0puwi5BOHobW9Qb6wbt08Qz69-qLddgnG6aXmw40ZSsaJbIvo8KXLyj2kzkCAl4N-htljAGp5Zv1AnLh7gSESpeTtx1Czw4aA03Jaluhi73hcVQjGDYTAoBn1PbxRYx6KkwVlvnbbNJ_mFeHhiXUwPOH2OSbZiDZvt5Ysphjw-7vITuXz7-1pbwgZqU9xqNSAjuWoF_5ZHR1KIfiLToDdUMEqTFOJZtRyP8m-DfvgYauLuPITEWnlvEbV-AYSxyiY84jInovIO71Hto0sLbyqjkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=GSWpTRoXxms-jRaHl6QN_hKsMaFaInF3-uLSTZfVnnoRSCdfpnEdxEVwG7KRx0puwi5BOHobW9Qb6wbt08Qz69-qLddgnG6aXmw40ZSsaJbIvo8KXLyj2kzkCAl4N-htljAGp5Zv1AnLh7gSESpeTtx1Czw4aA03Jaluhi73hcVQjGDYTAoBn1PbxRYx6KkwVlvnbbNJ_mFeHhiXUwPOH2OSbZiDZvt5Ysphjw-7vITuXz7-1pbwgZqU9xqNSAjuWoF_5ZHR1KIfiLToDdUMEqTFOJZtRyP8m-DfvgYauLuPITEWnlvEbV-AYSxyiY84jInovIO71Hto0sLbyqjkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=Ndrc2lJ6exJ5zC244_7B0LXNrGFrv1_A2HTs4j4x76Vbedcyqn-Bf-iIfPPA4QDF-pbUbguB_b5X-NAjdasOSCrOyhd2HOX-7lcPQ0bxwm1FvDufRARzqrQDuw2bOST7Ygq4EEL0d7NxmHOZpspxC-5KKC9IKL0_c-q5BCMvCy9P9EPlzdg0ejuyAOFQFCBEaixmUKPo95w5RpTHCdBmbZyMaj_kL5q0WswYk_HobTFuT-jahnBbsCuva8LEcTYuCr2WOfzdPNr2rzUhG_UsjFU4V7J_rZJC1dM6tyy_TJ6majInnH1p6vRVCESxzOqDEmlJvxT5gM5kRAOvFrvZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=Ndrc2lJ6exJ5zC244_7B0LXNrGFrv1_A2HTs4j4x76Vbedcyqn-Bf-iIfPPA4QDF-pbUbguB_b5X-NAjdasOSCrOyhd2HOX-7lcPQ0bxwm1FvDufRARzqrQDuw2bOST7Ygq4EEL0d7NxmHOZpspxC-5KKC9IKL0_c-q5BCMvCy9P9EPlzdg0ejuyAOFQFCBEaixmUKPo95w5RpTHCdBmbZyMaj_kL5q0WswYk_HobTFuT-jahnBbsCuva8LEcTYuCr2WOfzdPNr2rzUhG_UsjFU4V7J_rZJC1dM6tyy_TJ6majInnH1p6vRVCESxzOqDEmlJvxT5gM5kRAOvFrvZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=fxBptojD7mYDKjCqyeX_Fd7r9oinIJ4Nd9DKjVdag_vlMbmdoR4GtNiqpSmQlR0ltlpowuewj10nln_ZV8iW6eOLYkz6qkllLFEODgkkJ6VT63Ep_019imOknuQ7l__vNDDrjyQkmj8QITzozhYGdAqTBPJiXU14_nukggjyREHYwIlXnGZloJ-GBLh9hx-47LSzIG8fkuFNqSp5Xhyh_A92Fxu3YFgUQwa_AHbRyGSvBcfJDbDGYSPNgWcM1ztae_AGVRkwptBR9vqB7lCIQ-WABPs7uoLTuqdC9D1tqiZ0yc6d3uRQGXIUyfcF6imPFT7od1166r944Bf0GYtRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=fxBptojD7mYDKjCqyeX_Fd7r9oinIJ4Nd9DKjVdag_vlMbmdoR4GtNiqpSmQlR0ltlpowuewj10nln_ZV8iW6eOLYkz6qkllLFEODgkkJ6VT63Ep_019imOknuQ7l__vNDDrjyQkmj8QITzozhYGdAqTBPJiXU14_nukggjyREHYwIlXnGZloJ-GBLh9hx-47LSzIG8fkuFNqSp5Xhyh_A92Fxu3YFgUQwa_AHbRyGSvBcfJDbDGYSPNgWcM1ztae_AGVRkwptBR9vqB7lCIQ-WABPs7uoLTuqdC9D1tqiZ0yc6d3uRQGXIUyfcF6imPFT7od1166r944Bf0GYtRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeATo0BSCPFtHnsjLgRAeKntHqprAr0cyoxA2UOZT-61_vSkObMPuMn_jzVS8B6M5efZ1B0kkaSmlmpd8B8Sz27a1x7axrJIXNvKPke36WBg0rA3NA8_yzM2R6IaJBuXvTyvKlMX-3LcfMii0_uEJRRCjw-sHmNeXHqNFzX2P8hO3zAjYCDky4O79gMLE-tHCE1wklhZHbsxlvomgFcuOtg-65wBt1s4A_7U27U2SbU9uzg5xHgdnTGFvfMU_06-RYwk1OD3H3fOx8xA8Pl-5kiux9dJIkPhz_TtEZ9hYw_NGyCe4K51ZJSgq_um9LvoB_hVsyqFh-XN0eil3eGvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgFhnVnoxia1awLKAWDn0sTl5Orbh-wEhwhYLc-kNh4pamMQ8VmuHO591rjOLP2lpR9c1Ns55v7l3bN6LnQWg1smYofZgBol9oPfLD6GgrChqLUxfOq9FyAjL1IyQQZyPHl7727VWQNsfe8vR4geUyPQRiZ4VAwtwEwT2_zF6Nf-plAWLo4D_xPHgf6OcD2Q9BWoSUhbwEkn5nTlARutHU00DgjKIaLY3fAHiAAyrVp8L0njmTf_Lta7Nju27L-Kv1stFl8vL0m2TBJaS3ye18R0XpbNLiuIJVake4vQXkPa4ZIkfhpTQQCvFfEkcBZ0BTucE_Esvpjr3Nzk436VJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkjPu2CcET_jqA31baDFbfzF_iaImeixS0X1MsMGtkUT8rzG0W1Cr3wQQAVWVM7xyCEbOnVT2HfTPz8aTiKa0kTE8umjRHaW9IqKCXsyW3Y09-bV8nd7O58XyC1vfvnejaX-lQh-9ZnShXB4gz--lfI3_x7dFrw5XtU3SJxPR1aoFquXHAZk-Jov0yMOALiT09CYSrHLhmlQultOgO5LijbsW5A5FlQ_m4fJGGEI6iRhuPtWcIzIYLjgXaQWVvYRN6BdhOuIJPrCg7vK5GjiUzJo94c-VcnVIRi0bnhMWV8PT_-7REg1TtPOMnnH0KJWWtNqo7ArU3usljj_xUlriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzT7SB_ALeGVXJ0mw8Sj8gdX2ZJ8bLsClXV2HU8hV1WTF4sDQBIo_TgdSYO1Kk-m_9XyFNNvBUBp8L7NxGvABnnYOCQ7HICmEleX2mn3ybuRlZoXpuHuxOURNBg-4LdUBgse_R4pTg_lPjFk95ML8SiQBqdNUUngYeMKAYMp6Hu6XBIwkdaR0s6KCmyGqV-HtDNbuNxktrXKzKk8FuUQ3lIgM3r9JYzEn5RdZgbZLtNeOyYsR3T5m7A75XsUiXLht1K8DW9XZbGnve1zfAbAXqdGGAVM8c5nSbVf-6IsalWcV9PvDYbQGUA3ic-dVCBIaaDGy2m6Q9pJjVp4mYyyMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=Ss8IbrFNQ3Rn3Cj6EPoregcNElai30Nah4wIc2E4-FVrS5cYJiYSgSj9lek4oo0aPaN0ISEV6pu9glFtCL4y3Ye8Z30NCT8AP-roQSkfRgOHKyN859W7TnSnqsYlvAGP4Py4iIDNdZZ5ikW93iyPzygL9OWRd7g5T0uDLEeb7AWnE85YTS0ldXfpdnks8aHD0FOZkDUQxOX09u-Tr_JJSKO98NBluT6mgArZISgjRBv1E4g43Q6IAsFoLW8-MT41O8TOUox_SPOmKKwb5AeMJkgLACs7ByhMsQHTKfL6a__PE5FG1M2Qkwguul_Vvpfwe3EUC5EpyvChrIdPNJEl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=Ss8IbrFNQ3Rn3Cj6EPoregcNElai30Nah4wIc2E4-FVrS5cYJiYSgSj9lek4oo0aPaN0ISEV6pu9glFtCL4y3Ye8Z30NCT8AP-roQSkfRgOHKyN859W7TnSnqsYlvAGP4Py4iIDNdZZ5ikW93iyPzygL9OWRd7g5T0uDLEeb7AWnE85YTS0ldXfpdnks8aHD0FOZkDUQxOX09u-Tr_JJSKO98NBluT6mgArZISgjRBv1E4g43Q6IAsFoLW8-MT41O8TOUox_SPOmKKwb5AeMJkgLACs7ByhMsQHTKfL6a__PE5FG1M2Qkwguul_Vvpfwe3EUC5EpyvChrIdPNJEl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8WWHuBeYwvI6tFYVyzWMdQaYWqTyPcUi7jarcHOraXnsNctatF9_HXVgqEk2B1LH-g81edI6yzZeTNfdRAuYx_IKFHik-D-KI44pioaXfVfAOJjVd8E0Cyfv7vXaOPMC78oEjA0wyOdiETv9s4tuhNdv5LaRreMHBMzEAwOPdcMuZId0FrFMtVQDDNxW2feFHP7gKPNrkBJxasXidFLYbW0NM61hXlV4aoInGUr0iPZTeUV0MGFLEq3LhIGNBE0PZSK_tX62Q0QEughYkPECG2HUeZRJL4Np9YKNQG6pmP0SfBMiKM_uYRtEK0rniad9mTUQeVCmOsTtECneT9ong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laKh1L2pYpI6VMUzqAwaHGyiq_bM6b0OjWznYUHcF6NP4fbkStnhMRNVFupFK_Dj_cNLXgvlGE9mvmW-Jc113zsznVkmQhdbUyjHbK3oTCHcVWWWvBnyhxe-gCnd6gc7O6knZhACLudEP7V2ayj1HYw6Cg9l2JvbVxnd_W3Icb_HaGGuEgqPn7W4cH73fKfQbc6Q76x5Os7QMTxNOybnZ16ocspizEJprIJAS3jTdF5_vZ1emL4p32VV0xsUPrk3J49z1QnRY4IQTp49QDCWDa4bgThZySWyYIwl_hWSFC8Zx-hl0P2GbL-8ScYmneZQv4mEXnhrQ9BAvm_C_YTvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF2kifqcn-kgHyu6HL8xuWQDNF4C_gJDhDB6s1Fmdtw-Kf5zvv-b7NXvjrdYT32iAAyjGWJClU_MGtkgU975TKVxjeiV6x9IQ-7y7tIqtEdLscarzZcqkQZVFq_S49hNroYL1qIzmvUh10eA0XfME18AVeabq19yTsGfefUZGQeZ8Pg-bCYn2Vv3jHirdB2DsboiYrcCfWjEnoCg90bAL-3EvOylEu6X1vre8nxRbSQHdlMzBn8-JIoqNzzgCySZzjD-_4sR0AcD8YtUdB-W3kS6eonOuUJEhqAof1WglynyS8gFBAVcKld98-D0L_i_yytRfPD7KWYw-ClqY9prtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=gf2pE7H8UW0oG-9e178xPLo2iXH-PNu3tVhTfErlTcvt4VmGzVBuhh88n0oXilp6nzjPNhvClvWiEonGTzQPN9fJ_cAleTvLZ5ajB1H5UalvQGTnfn4MZc7Rq1qKiUt7EFLidlOIpADW3XS2Bo8Fb1GDJQApewn5SM6Zt0jV5Sl8iY8skvDA_c23FDaq1K75We1lmGoowInW2B0fPzV8oofkETHeO5ZVG6Rd2fIUOpUUZjRJQ15qV7H8T84MYJoBwK8RUK3VY8zQFw4CQFfrD5_fsIYphIVpCE-T6X2EgkPOv9BdZ-LtLfszQxCx4AeNL0TlQLF94C6TJedc8d5P9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=gf2pE7H8UW0oG-9e178xPLo2iXH-PNu3tVhTfErlTcvt4VmGzVBuhh88n0oXilp6nzjPNhvClvWiEonGTzQPN9fJ_cAleTvLZ5ajB1H5UalvQGTnfn4MZc7Rq1qKiUt7EFLidlOIpADW3XS2Bo8Fb1GDJQApewn5SM6Zt0jV5Sl8iY8skvDA_c23FDaq1K75We1lmGoowInW2B0fPzV8oofkETHeO5ZVG6Rd2fIUOpUUZjRJQ15qV7H8T84MYJoBwK8RUK3VY8zQFw4CQFfrD5_fsIYphIVpCE-T6X2EgkPOv9BdZ-LtLfszQxCx4AeNL0TlQLF94C6TJedc8d5P9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXmr8WQoAqDq2FAO5qjbPm0Zr3veHwxL1asgQ64Usw1OdK9UsNdiQfTd8FvM8Tgdp4ZXa5KspdzOzvGwDUb2uIhZcQi827rSy9_YJHPC5xoxnY7KvQMbX2BC7cxolsOR-hI-s1rgmt93d3ngycuCr2HCilaDPe6BEv-rvOBRDFLgqxI97BpcRDYTqt-YLp5dbsQ-JVgecXwDazRqwbtDU8oQSeiZKlaq3DMMu-aXGmlxGyHAeUu9gn9hkPhjJmUXLVhIW-Ts7vzP4PS6ME1kdMlix-6uk_IWZagQ1C-286_eRYSEHFtCqYh0W7lM4hgIK6C1wXvIXS6_jTID5lIYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=ROfGeJg2Jka5JA-Y8_q3HKd2eNr44xE2LydJe_0oqVI6q7vOuW5yOZLNEvqWJxMm48hM5NpSLzmYKyrHbJOE2qwBhN_QOoJxCAx22PNWKd66jO20qbmMB_XjSvb9hOLBR9829i-O3qFW90EnqBk8hJbDFOHtWriJeNTeSdptzsekIcG5LGOvIXwKUrico34q8Dnz5_N8Yw-ErcyFE7qEzHyIlH7EkCrpoJScsKYpFKHorbS8P271_azcaOdUl5W4QhZ-PzAiXftfY2UA6DDT742N7YFHLRA6OyVDeq3wRu2eE64vpxjTCsB_P0WbbybByuKS2UMhURB67TwUU7seDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=ROfGeJg2Jka5JA-Y8_q3HKd2eNr44xE2LydJe_0oqVI6q7vOuW5yOZLNEvqWJxMm48hM5NpSLzmYKyrHbJOE2qwBhN_QOoJxCAx22PNWKd66jO20qbmMB_XjSvb9hOLBR9829i-O3qFW90EnqBk8hJbDFOHtWriJeNTeSdptzsekIcG5LGOvIXwKUrico34q8Dnz5_N8Yw-ErcyFE7qEzHyIlH7EkCrpoJScsKYpFKHorbS8P271_azcaOdUl5W4QhZ-PzAiXftfY2UA6DDT742N7YFHLRA6OyVDeq3wRu2eE64vpxjTCsB_P0WbbybByuKS2UMhURB67TwUU7seDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=Iy-HfqHmfZWvPw_WRCNl2arOsucvWwgoGqr97zTYmNa8iPYwXLZSCk2GiA21uY5lfLWqV7Jk5NTR3-uk7Uoq-WfsR6OuILrau476ofzyAoL_SrfX-_6EVmwNr8DPt9XrW0xZozQ5uJOX8RH1Z77By2eJz_3v0kvJodZAlucJsGnIEn1G2ectbEshMw5x4KK9aYnmIHZYRmPQlEhlxjs51LFS4a1AdAi3dr0PHTtjJNg_IqR7vVj6Ro2MdrMklc18G_px-1psY600vRJo6AC58H-uRWS8mqZX4qp_OeKh1N1NDeQtxMlWdDgcNdvqVlGgTngsmZ3PNn4rPp_mmSbsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=Iy-HfqHmfZWvPw_WRCNl2arOsucvWwgoGqr97zTYmNa8iPYwXLZSCk2GiA21uY5lfLWqV7Jk5NTR3-uk7Uoq-WfsR6OuILrau476ofzyAoL_SrfX-_6EVmwNr8DPt9XrW0xZozQ5uJOX8RH1Z77By2eJz_3v0kvJodZAlucJsGnIEn1G2ectbEshMw5x4KK9aYnmIHZYRmPQlEhlxjs51LFS4a1AdAi3dr0PHTtjJNg_IqR7vVj6Ro2MdrMklc18G_px-1psY600vRJo6AC58H-uRWS8mqZX4qp_OeKh1N1NDeQtxMlWdDgcNdvqVlGgTngsmZ3PNn4rPp_mmSbsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=NQv1u5xdUjFJZ5sYBMycsZ3yVEe623-fGctaSuQJFDxz6oT0lwWNRCpgdZCIuIrwdFu2x2GaszZip984kzc4qDgKUPVsGgRji9I_PFtir633PWw1ir8DfVdmaOyQRLpokmHXnONvANvAjaRxo5wkH9U-s9OQezkjxhlJlD0HqXDruJXPwcw9fYL2jKp4XzemtxGP4g4Al3vvHcLnRS4f8Na4FLledmCMd4TkAc1dYNeHVkTK6ngLojDH1Af4_836Cnz89A2pgWaeHn75ZOu3HF2d3MjsNCIPFmXRUOlkL5ReDMG33jI1EA-4Ytwy2Jv8g1asT0Tpzv1wVrVXeVbpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=NQv1u5xdUjFJZ5sYBMycsZ3yVEe623-fGctaSuQJFDxz6oT0lwWNRCpgdZCIuIrwdFu2x2GaszZip984kzc4qDgKUPVsGgRji9I_PFtir633PWw1ir8DfVdmaOyQRLpokmHXnONvANvAjaRxo5wkH9U-s9OQezkjxhlJlD0HqXDruJXPwcw9fYL2jKp4XzemtxGP4g4Al3vvHcLnRS4f8Na4FLledmCMd4TkAc1dYNeHVkTK6ngLojDH1Af4_836Cnz89A2pgWaeHn75ZOu3HF2d3MjsNCIPFmXRUOlkL5ReDMG33jI1EA-4Ytwy2Jv8g1asT0Tpzv1wVrVXeVbpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=opa1hUFwxQQZSeWK-NWW89d6SjhcHz9hB5OTBs_zl6P45FASw0iizuFKxhRvWk9ZJEIvwJeOFPElwOchmEoG-2TaqE7GG0bQwpcA3mzikXe1wXNABSA8nXEz26oib5QjCI-Pz30f5rY1NZe3GCVgLM26fXyHlh6hr0P5eQsmIT41yVVhe3DLI5uLIsO1uvl90q4Rub8P5zTqBboaVBwKBXnKLwQbBhgunymJXC_c9jjORV7kUBZDavtam_oDHi72tD8IjaGSMr9ODQwK5WEP_jSb095wnoDXMzWo-e4nOvZ8kT6JUWM9H8XjFivL3L-mFbH2T6DZXCesqzFdgmmq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=opa1hUFwxQQZSeWK-NWW89d6SjhcHz9hB5OTBs_zl6P45FASw0iizuFKxhRvWk9ZJEIvwJeOFPElwOchmEoG-2TaqE7GG0bQwpcA3mzikXe1wXNABSA8nXEz26oib5QjCI-Pz30f5rY1NZe3GCVgLM26fXyHlh6hr0P5eQsmIT41yVVhe3DLI5uLIsO1uvl90q4Rub8P5zTqBboaVBwKBXnKLwQbBhgunymJXC_c9jjORV7kUBZDavtam_oDHi72tD8IjaGSMr9ODQwK5WEP_jSb095wnoDXMzWo-e4nOvZ8kT6JUWM9H8XjFivL3L-mFbH2T6DZXCesqzFdgmmq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sAm8UW5XcsySuG1oXFMD-zTPGXm0JzZrQKHEsf5b5WP_gw6C0jo-6Lp-tdvpTa6gCDUYqkFTYRlpzheohGAuVZEU1hTSyp5lcnuGI2g2IixT4Dn91NtL-WM7N4vWAnF7PDUANjCASaBj1CXnbTNjsdkxlY7kNnpHsQcFoxL65x_raHY5QMSyS58lHtjLnPw0MeozNbT3Ud6vn9i0iByeohwrsz_0fs20jVoBTJAhFSFGMZu-SWiAvVrTOOhorxBm1pnsCOxCnv20steMUlPNu-Fvc15Nys_69w1fQgTe4zazgQr3Z2XDf6_-mLJiVru-qHwOKHBD5xaj34FgpIeqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sAm8UW5XcsySuG1oXFMD-zTPGXm0JzZrQKHEsf5b5WP_gw6C0jo-6Lp-tdvpTa6gCDUYqkFTYRlpzheohGAuVZEU1hTSyp5lcnuGI2g2IixT4Dn91NtL-WM7N4vWAnF7PDUANjCASaBj1CXnbTNjsdkxlY7kNnpHsQcFoxL65x_raHY5QMSyS58lHtjLnPw0MeozNbT3Ud6vn9i0iByeohwrsz_0fs20jVoBTJAhFSFGMZu-SWiAvVrTOOhorxBm1pnsCOxCnv20steMUlPNu-Fvc15Nys_69w1fQgTe4zazgQr3Z2XDf6_-mLJiVru-qHwOKHBD5xaj34FgpIeqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=drU1sj4-3T875vr3h0CoycgrYTyNCu2I3K5B7D4Bfn6xJdTGEJJ22hWAuxNxu4Qod6xLrNI-c9i3S_0XtcHDIzi-SIjWesCEyTohH72qWN5gtHvAeTStYIQ-rmJuGGnLhO5JC00ajZBPn5o2DcP9M0OhxKLtvi65N34qLr7eAJv2_gW4HdWWjVhO-ynbGeWh8E9lji7YSqd5gVsnm68IP6dCfJ43BWCOz6NJFItNXsFL18FtORJAOauyVRbCl5Up-N8-w79DN_vG8FtPho1Pajvislm8llUW8g2TOhaEpxZ0gBt3CIrYtHzqeOIeTSdGNBv6KanxU-2mO9GdLTM_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=drU1sj4-3T875vr3h0CoycgrYTyNCu2I3K5B7D4Bfn6xJdTGEJJ22hWAuxNxu4Qod6xLrNI-c9i3S_0XtcHDIzi-SIjWesCEyTohH72qWN5gtHvAeTStYIQ-rmJuGGnLhO5JC00ajZBPn5o2DcP9M0OhxKLtvi65N34qLr7eAJv2_gW4HdWWjVhO-ynbGeWh8E9lji7YSqd5gVsnm68IP6dCfJ43BWCOz6NJFItNXsFL18FtORJAOauyVRbCl5Up-N8-w79DN_vG8FtPho1Pajvislm8llUW8g2TOhaEpxZ0gBt3CIrYtHzqeOIeTSdGNBv6KanxU-2mO9GdLTM_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=okYQ_G3y_FAqK96rs-kOk7PIHqRQ3TYcI8kQ1ACf6sqTMTdLKM6cdgIY1liJGvpKGjrY1uSlyqVd2KdFRIe8mUQ5_KOcLaI7q5x69DGCcw4ZLJ9_W-Pf8YXa1LtcF-RuLpIBKT2P6yJVhPtRo6hxZh-CzN9TukMH6g4qqvGc0vaD7Tq_jx0d9HucT8RrZ39ySic8oqdAPxqapdMXZQMpW8dsLzkKWBj88S9fNOyJYU8bhggzDPmtyNuTIfqcm9wQwS7nJH4_Nlo5R0exKhSp4js5gsVHpmvMGjmPs90cR8tBsnuE8zBlq3cYyrdyGJyNcqF2sqUUKu6bVLj8wzXdsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=okYQ_G3y_FAqK96rs-kOk7PIHqRQ3TYcI8kQ1ACf6sqTMTdLKM6cdgIY1liJGvpKGjrY1uSlyqVd2KdFRIe8mUQ5_KOcLaI7q5x69DGCcw4ZLJ9_W-Pf8YXa1LtcF-RuLpIBKT2P6yJVhPtRo6hxZh-CzN9TukMH6g4qqvGc0vaD7Tq_jx0d9HucT8RrZ39ySic8oqdAPxqapdMXZQMpW8dsLzkKWBj88S9fNOyJYU8bhggzDPmtyNuTIfqcm9wQwS7nJH4_Nlo5R0exKhSp4js5gsVHpmvMGjmPs90cR8tBsnuE8zBlq3cYyrdyGJyNcqF2sqUUKu6bVLj8wzXdsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ryKzMg7zb1uJWTgTTODl8NpPaMU5jXn8U1NY_bKGbPWrsVmGp4eEjfeEZISdls6GcRoPVeOf8o0HtUJH9JZ2ZfhI2wpcfi_OGeJp0vhJoK23fQ6qTlAjjRpjO5KHRR-Y9KZXWmSsqvWn6OVsZbUgi-PitQnatfcDq3zJ69dVB-HxjbxPxnGQakYac0KauW30Otp1ijMAKONiBivl9dgcJODFMyaEuSa5Uprfkib9ADENO_EKXDm5uVxg_i-L8k2ZNO-IthUslclryG_DhpClztNfdo8Q4QhtlLStA113RgI5RJciCKcXjln80tlnyEGzFHJJoTTNfTEWw1HU-aTFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IyutoQHzZKRXVzk8wNE6T3audOEEm6dDYzZYgr8TpXUqciaiH41_Yi6uo5-9G7XnCFgxKkb5KD6oCuAHslhapdjIcgy9ga5wDp9vOx5an2KxMohzPZEnONvIpKWa6_3OmT8HBTVBPjO8Lyj3riW4DHVZV7B_-K6g5yqcJMxNI4le9dEZVdBpELfUqUDYlO7Dzja02EHOGEQ-l98HqyXO-6HSz4P3mix8r9LXtBZE3F9JI_4zn9wwourzWK-uVs7DYJcOC--70Sx7yxzQLt-hYx4i9xxYyNy_7uPGY-HAHesjJr4uy65nXkMVCU8CPMMi6Urmne3x7Slkl5gQPBUKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=CckrfSgqEr9MfljklHEUR2_QZexUWMOgLbUZDPrmrMNMqjVqeWjpIxhGCWPFhQMZrwS6eAJHUq37oxhD0lYa7zhWQcFJVRoqYaiJPIYveTfs8S2AAoMOpJjWgCBhpJw2SU3hSMJwGucxWSZ_2-iZZT-JL_PbCrfuNanph8sD9H0YMfWwYAdZF1MkXlnfWaKrXQ_PnssqyQ8OSpp0-U4vPW-F2SYdd_254c3G5Ue8F4w4-q2mWKo7EKSqRWeoN5g7e3i5u0248-tDNaUEh_VJPgFb--two8KswfUqaCedZKkCtSjrPBsd98YlHG1LmILNchSAUy6Xz0eg7aDDdAsY4W7rT8KlaV0_fIGkoF_MA_qvmF95UtAl6C7e8bAvBBI0WLs5DGqB4g6tkBZdvRTTK9LGhRu3ZU6NjikB17kuehxlEgxS5G_GfCCu7ClhPmPx7FzP53Q9FmFvfBEb9NNIMBY3WOo0glZRyQHiCkO-Dead8jLSWHgqng8UKMUUHUfGLrB-UD5JdZAchBiS4u-Iva0Qk-piH4beyxcKh_yj_hpg_5nZXDpVEgNiRdes2F-l_q-nwNlO-xTBTh81ejE8RqLVoAxQv4rrX5lwV31xHLQeXzfkzc8NddUw57RGtiFGKnP3cl3e_arQaosmPaWfTxQ0CczLAEL72wxPcNMQN8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=CckrfSgqEr9MfljklHEUR2_QZexUWMOgLbUZDPrmrMNMqjVqeWjpIxhGCWPFhQMZrwS6eAJHUq37oxhD0lYa7zhWQcFJVRoqYaiJPIYveTfs8S2AAoMOpJjWgCBhpJw2SU3hSMJwGucxWSZ_2-iZZT-JL_PbCrfuNanph8sD9H0YMfWwYAdZF1MkXlnfWaKrXQ_PnssqyQ8OSpp0-U4vPW-F2SYdd_254c3G5Ue8F4w4-q2mWKo7EKSqRWeoN5g7e3i5u0248-tDNaUEh_VJPgFb--two8KswfUqaCedZKkCtSjrPBsd98YlHG1LmILNchSAUy6Xz0eg7aDDdAsY4W7rT8KlaV0_fIGkoF_MA_qvmF95UtAl6C7e8bAvBBI0WLs5DGqB4g6tkBZdvRTTK9LGhRu3ZU6NjikB17kuehxlEgxS5G_GfCCu7ClhPmPx7FzP53Q9FmFvfBEb9NNIMBY3WOo0glZRyQHiCkO-Dead8jLSWHgqng8UKMUUHUfGLrB-UD5JdZAchBiS4u-Iva0Qk-piH4beyxcKh_yj_hpg_5nZXDpVEgNiRdes2F-l_q-nwNlO-xTBTh81ejE8RqLVoAxQv4rrX5lwV31xHLQeXzfkzc8NddUw57RGtiFGKnP3cl3e_arQaosmPaWfTxQ0CczLAEL72wxPcNMQN8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=f5YJvA9ll5F-lFfPfbRkfAlktvC7DH9GGCRLCPo-DoQq8gRPTC8Jna6eSKDxz5osCWc6jC3vhGweGfqhCa5CByl6fjefREukBD-sq-xJWUFUYqVx2ezGnDN9NWfNS1qLgDioPW7XlBct3KnCRWMNTdBP44Osc89JgkKAqFmXV_bDghi3hb1K-hqfC2qZQUtMZzDPKtaJY3M02xNUBxb8F2ZG9ZWVehFt5QWZ3rwI8Rw7lNQrHS06OdkKb8giUHYQWmIU6wQ_VlsBRfY-DGbbn56kq3Du6L12Y7N1GvYXgVlUrGkAFAJbah3skHTrAIiqKWMUeEzuCNlheRtZLbZh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=f5YJvA9ll5F-lFfPfbRkfAlktvC7DH9GGCRLCPo-DoQq8gRPTC8Jna6eSKDxz5osCWc6jC3vhGweGfqhCa5CByl6fjefREukBD-sq-xJWUFUYqVx2ezGnDN9NWfNS1qLgDioPW7XlBct3KnCRWMNTdBP44Osc89JgkKAqFmXV_bDghi3hb1K-hqfC2qZQUtMZzDPKtaJY3M02xNUBxb8F2ZG9ZWVehFt5QWZ3rwI8Rw7lNQrHS06OdkKb8giUHYQWmIU6wQ_VlsBRfY-DGbbn56kq3Du6L12Y7N1GvYXgVlUrGkAFAJbah3skHTrAIiqKWMUeEzuCNlheRtZLbZh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=qFk7WhEfbpz2ZB2AMGAEYifh7-cza1lTz2vL9jSv9OCHdOB4I2s4CqadhQnNNEOoayDeB0Euw3LAgTI0nEq9do4Z6wy4KOr0J0fqQBjhKOESYGmgIBWL1kQQCNKMRUh0xb_6x86sCwr0vSlC9hXwxQ3A34XhiYA_x0OlAuYGckcjxD1SWL8IMkOTUGz02IJ2XUvYL0Mb70130Aah2F_N2jIzhAumM6nbAOX-cQsxv6VYM0EIS1Jt9koLtYdNLALYEmQj9_Zt1xIE6sOvMAST7qfwfQ0tWA2JtOOUoblNWjkeGsuHw_u56NV3AJJS0_JK2-UlrPdRg-A_dzdiTlPrZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=qFk7WhEfbpz2ZB2AMGAEYifh7-cza1lTz2vL9jSv9OCHdOB4I2s4CqadhQnNNEOoayDeB0Euw3LAgTI0nEq9do4Z6wy4KOr0J0fqQBjhKOESYGmgIBWL1kQQCNKMRUh0xb_6x86sCwr0vSlC9hXwxQ3A34XhiYA_x0OlAuYGckcjxD1SWL8IMkOTUGz02IJ2XUvYL0Mb70130Aah2F_N2jIzhAumM6nbAOX-cQsxv6VYM0EIS1Jt9koLtYdNLALYEmQj9_Zt1xIE6sOvMAST7qfwfQ0tWA2JtOOUoblNWjkeGsuHw_u56NV3AJJS0_JK2-UlrPdRg-A_dzdiTlPrZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=ZkCf7lnYUpwaIDYJWJUpSZnvxfUfohdC58rt17rNkZ8lcUr_VAXBEaYX2EdrCtRGEiq2uGBoOG97kSAk6hFlPcERzDvwDiTzc5r6gvOMfRKlMsee5-HkE8B-bmLhtn-7BcFEpgyptYH3eK7dLWT4xd5IQlCmomKEHkecxBP93laL2zkmLYwkVD-34lLZskCaXL1R0LWXx3JAwsbORw0nJKnEmAnJyQAFgSd4gXUzPRt44jUjQHEc7F-bcDNjCpp138PnyqToHB7UyUcturwaEqDV41JfJZVu37bWHaX-rdCYnGOxnAvCVKgiUxDZn8r2bqM0m2GQhzrqg7TPI-AqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=ZkCf7lnYUpwaIDYJWJUpSZnvxfUfohdC58rt17rNkZ8lcUr_VAXBEaYX2EdrCtRGEiq2uGBoOG97kSAk6hFlPcERzDvwDiTzc5r6gvOMfRKlMsee5-HkE8B-bmLhtn-7BcFEpgyptYH3eK7dLWT4xd5IQlCmomKEHkecxBP93laL2zkmLYwkVD-34lLZskCaXL1R0LWXx3JAwsbORw0nJKnEmAnJyQAFgSd4gXUzPRt44jUjQHEc7F-bcDNjCpp138PnyqToHB7UyUcturwaEqDV41JfJZVu37bWHaX-rdCYnGOxnAvCVKgiUxDZn8r2bqM0m2GQhzrqg7TPI-AqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=bkxj-UwlBzCBQe33VvymmKBmuKfkwIuo_docv5sLXyxG1n6DwWszSIYYvfjBDHg7sQ1lm20kXsLct68swUUBQq5lCSP2QQAzWhSZxqf2jnnR17wjgQBCn2cNfBnMU2XaKROCWV_hoN8I8XK6-Qvv7-MtFUXe_-yrTkcBlZM-r9Zdyk3I_Z6iL84azr15leTNIN8OWNcVfClhAQh-aPyFTlkGjuYoCGzOs47KKsNvygXYwIjQWjBSx2blJ9lmmk63D_JBstiDOFM4I91E40nT1tfwHgQGenHP6YU8-XyRVGFKxAbPBfIVarHuKJr7_nIBt1X9gf77SlJYsxgCsH5fog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=bkxj-UwlBzCBQe33VvymmKBmuKfkwIuo_docv5sLXyxG1n6DwWszSIYYvfjBDHg7sQ1lm20kXsLct68swUUBQq5lCSP2QQAzWhSZxqf2jnnR17wjgQBCn2cNfBnMU2XaKROCWV_hoN8I8XK6-Qvv7-MtFUXe_-yrTkcBlZM-r9Zdyk3I_Z6iL84azr15leTNIN8OWNcVfClhAQh-aPyFTlkGjuYoCGzOs47KKsNvygXYwIjQWjBSx2blJ9lmmk63D_JBstiDOFM4I91E40nT1tfwHgQGenHP6YU8-XyRVGFKxAbPBfIVarHuKJr7_nIBt1X9gf77SlJYsxgCsH5fog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxe9iluu3gTbNKDXsmRV7zDgvtH_qmc1F0dNyUdh_kikFTeyAzrKvi_rz3OlDEkCDewwZwAbH8MUerpDlLI42twhbLV8Ep37S6YPcIaODNPnPF4YLxxrGXdfNLWL0CwfJQsKlwa6MQEL5QEvkKQM-Qm6SN2Asjqf5TeRE7CXQY6f64CQ1UKcfcd0Tx2RKvjNinsrxH0wjv0YqIUlxFH2e_g7joDs-gnnCYL0iom7-EYg0oS9ZvfOshCijxyBq_qy8cXryMgijplvxk29lvMs9KiBIWrHwFbsA1Q7lFQUl-qbbVUKWSC03OnXfCOSxPy-IPOFm3DS_6J2yb_CWL187w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIdVkowozvZ95PYlbhny4vHTRGdny1xcToJpoVMKn-CDosXXXBjtMlkx43U9tH_Koe8g6FgXxSht5tl3Y8O-Woo7AvQbk3Sj9lirXkzvce52HfbRmCztVDP2IBw7YEfF43nbbwdgqCDJ-vTm1T2qEHolVwB2hrUAYn8IK4heF9ZjDEd0qpGQ-HfeObt44ER3nTWR-lKfq4aOVmbLKL1M33sy1XxnkQvcn3aeSE5_IDfa7xyKCy_TLswUA8pgekAWp_EEFZGrWRUhP0eRy9dzJ7058FIktR4CDftXFpwR6cgXnjsMdF538yhm5BndUZSt8qCHy3wuuVvVNzri2pFvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLnFBaovuX-rZwd4jREK_wnSqD8da-pXXkq-YyL-gWP8TyJucRr-m9fTcYVJ0SgLu_vM5WVEuBfo4fkDOuRMCen7dQbIMqADIWXxeTtzxA-9Dr9wCUSyZa5SsjnVCKEuXBiEqSsdAkWsnqut2wwjHq9Q4fS0HAD10lc4p297JXMwm0Hsb-8hTGZn13B3sgxJ6EQy_9N0wlr0bEc0A0Cq2dTU1IViClWxVC_vn74wYENZEoptiqrCT0V-nR_iTFd4RthsczTXO1vOrVY1MuJydtB_sawITTlTGLeGs5WnH96qZX_ydCTcX7eKxegIW27V7KeXGkm1wJ-NmbfYsuxJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUgXEACGeZLPRHFye5K-17CQHjL5B96azGhVsnwq6MF9P0t8pgV21qUhMwnZbxi7Stdn_-Za6tKGieRjJqNQIHGxbimZhV5luP-q5UGg0X79QIHNnHV2y17S9u7T5WR5bzKzSezbVBWKRE5BkHnAKavomlhNj8Da90_-m9co2BcuOP7TtMJGtWJXjJgycJkAhobU0Qu-6UTgE6IIu-xeOB3X4RcA7jwb77xYb8Zcr7JNr7C3ilU1BT4lXJ6NixmXQHh2pNgiVE6hunZaoi43nSQFriE65BQTjy41ZnFXaPlikNHkXV4W3cwa6eykuSREb6cyieCqwUNGFtYff9AkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdUfc0tV-6Ezkaih8hnvt3gHOG7nVckiTaE-Qe8DcZHwkax7CvrtQ--oBTpSJzeVz6g-XlW1hWR-hX8LVdQ40rOyeHe7PogCh-VgKh3NSziHLGRQtAg_PcpWW4DFnh3Bo3dyDJY3ZNCUqSP-ULqwthtoqZhHn-GCuV59DjiKlVufB9FPfiKnyzIQnhlNcN6C3WdRS1zhwbVKGAO6VF1HK0wTDcHTk2y_04KGnO-QGBQ3feZVZZH_E-4o8g9Q_3losT-nFyxFlfOaczFcnk-1t5sBhIiZwy-Tptexm7TPJhnn3U3ZNWL4dP6WhoFFeAJj4Zo9G2j04zD4KXegHYK8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxYJVBUTx4UCIM8xI8FRZ8lQvCaadbjG_1IpPInweUUVnQvAZBp_-CSU4rhsAUbboYldn6Tjy2BeuOutW5n9Wz8-SsQrFQn_hDNeX2Yc9TsijiqRwenxkeadgTjoK6-OG69prl_wQ_7WHFo1xOJ9i0AVGt6HgsjOmSGpLWuSqEfZ_qGQsceS0WtvdLSEHY6oFlGqum5C2ZdbF_IMaPkuHN7lmWBD3q8uUHSfCmhMexVkyJDYKA6nnPKB-27yiR53v76Nbb07ryDJGVH0h2RgsD4_GdUhzoORKLYBPItv2WvWfQsoGDpUcWPdLI4kH9uicL4gUAbfPvWs66u2ZZrUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=gARmeomhacRehvJBiUN-McIfIxEMvWAdsrekiSgTnGLV8lHrktIDkGu8euZgbt9kKBX0p1S08jFzssLFsIu8iA8dGQv27rkvsbz5hglh7tcmdIKkMh2vzTeBnvXMP113fvUc-SHde484jmLMhUir2uUuXVZ73bRPyN-tnrhAWg4E5b9RkFHcNnDgKjP5SCFUeHNd3338dc7d2Psi0_NZQrOI2Fifb9_yA3zxTmCI15kl4kBGDhUkVleurDihBhwl7b7wIjUcDv_F3stKBPjahfSvk8_mQMXQMB_PLKkVGlBV0nAf2o36bmGqLPlBBYs5sLxCfkDWPJk5ROGSh0JIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=gARmeomhacRehvJBiUN-McIfIxEMvWAdsrekiSgTnGLV8lHrktIDkGu8euZgbt9kKBX0p1S08jFzssLFsIu8iA8dGQv27rkvsbz5hglh7tcmdIKkMh2vzTeBnvXMP113fvUc-SHde484jmLMhUir2uUuXVZ73bRPyN-tnrhAWg4E5b9RkFHcNnDgKjP5SCFUeHNd3338dc7d2Psi0_NZQrOI2Fifb9_yA3zxTmCI15kl4kBGDhUkVleurDihBhwl7b7wIjUcDv_F3stKBPjahfSvk8_mQMXQMB_PLKkVGlBV0nAf2o36bmGqLPlBBYs5sLxCfkDWPJk5ROGSh0JIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XuFGRcgyssYPj3dsjS_cg8WCYWXoflXIe5FMxG5BdqbNyiDHGaDljoiGfmgUN2PVWZUt9u0nsXjIADedcBzpGqSRkg3gyStDlgj3CwAE80CxSxrOinb15piVGwrWpwtFnBzbIeb4fwCqhmdC1_br7f6fUekz5GSjqpe-9LLrhCdmoDKUaW96abkOyH8tNPoH8LXc5eNn_nWTyrOUAIiQxAzYWKYCEgEJZYJdZ-CIxAicQTwdQwUYYdhGOGxkPedaQxZbSg5QZlboxGPLR_6_fxWBxu9-mSevJ53JsORm_BjANUdN9SKl9mdX-xKLnrqGscaT7ppSX-ozoaeHEVxl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=Zlu55v1XlPv5c7B2bqp5VOPQigxpjubqge6Oz7GhOaBqt1aPc8niX10ClCwQ1Z_U2va8z2tWSqnkl70YiN51Unx2ECeg6v51u5qy4SoWUBRbxdj4DttwmShb_Oy-fdz-CLuTqyHwSm1ZXlGF5Fy8IBrCNlp2tyS68A7YGc3v1e5GAl5mE8DPPjcJNSRWyI--U_CTzikTUfwJ28omIV62awHmmZ0KYXnvYNdNeoVEnkTyu3h2z340oQ5mF6vRIOYLGlekiQOpFupKv19wAAreRw73owZWtkJT7ihO_UmfTFPk9xrckI_peyzdxNNq4Qs_RKxHD8vyMo-IRVE0lU1Mpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=Zlu55v1XlPv5c7B2bqp5VOPQigxpjubqge6Oz7GhOaBqt1aPc8niX10ClCwQ1Z_U2va8z2tWSqnkl70YiN51Unx2ECeg6v51u5qy4SoWUBRbxdj4DttwmShb_Oy-fdz-CLuTqyHwSm1ZXlGF5Fy8IBrCNlp2tyS68A7YGc3v1e5GAl5mE8DPPjcJNSRWyI--U_CTzikTUfwJ28omIV62awHmmZ0KYXnvYNdNeoVEnkTyu3h2z340oQ5mF6vRIOYLGlekiQOpFupKv19wAAreRw73owZWtkJT7ihO_UmfTFPk9xrckI_peyzdxNNq4Qs_RKxHD8vyMo-IRVE0lU1Mpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=ncWu0F-pIo0OnR2COfdmLF4C87PncZi9N5JLG2rH66Ox2IX-64xd85BeErHbrzJL2QBrWmF0eZnOd3FiLPq-blNz1AHmavy8owTfGN2qbPeFiX8XgaXa3tb1Ri2LoERUi-craLDugQf98ccqZ1-pYWxbMEqESgKcWOF1dHg-qtvuK0wqwWvQR1aXWKaTFAvuzZ7CNB9DzAC8aCvlB1frDj-pcZy15u3t7emkucVxb59bIIfa18T5ReBnhoev6VSHTV069s8_OGKZx1lWFCvUu9Eujfs0vDqEFg0KsGcE1yhYe9f7sTtEg1YpU_kIjAAx7xVSJ-ZpG50kMLNCLjy8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=ncWu0F-pIo0OnR2COfdmLF4C87PncZi9N5JLG2rH66Ox2IX-64xd85BeErHbrzJL2QBrWmF0eZnOd3FiLPq-blNz1AHmavy8owTfGN2qbPeFiX8XgaXa3tb1Ri2LoERUi-craLDugQf98ccqZ1-pYWxbMEqESgKcWOF1dHg-qtvuK0wqwWvQR1aXWKaTFAvuzZ7CNB9DzAC8aCvlB1frDj-pcZy15u3t7emkucVxb59bIIfa18T5ReBnhoev6VSHTV069s8_OGKZx1lWFCvUu9Eujfs0vDqEFg0KsGcE1yhYe9f7sTtEg1YpU_kIjAAx7xVSJ-ZpG50kMLNCLjy8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=gWX83Mqwi9K65ikJkMjWiD2biF3Phwwpt4aBMe0SAX1sgQ5SKG_vBTSMCLubXaYWFa-uNwgeOtWEVW0RfyxDju2YTroBRB1cujIbN4GSO2JdmzYbkYomj5V98lLytkQ8gBgj4PFN5ZDT3jYxz5cvsPiQ9WeVMFgSeQfaaqXdd1n_zTYk12lRluHJ0dWjVOROiHiDGcbs3qUUrhAuf_S-Pledc7yFE5hlttmNuJbtBLeyd4N4p9_pjG74NRN3YZM5MgIKeuIxDVlQYz1GZd7d6rRUHysI2HmP01uVQTYcOBqiGy8f9Xzuj1W1zb9_AUK9S5fAPlIEXv8JDUmvpZYv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=gWX83Mqwi9K65ikJkMjWiD2biF3Phwwpt4aBMe0SAX1sgQ5SKG_vBTSMCLubXaYWFa-uNwgeOtWEVW0RfyxDju2YTroBRB1cujIbN4GSO2JdmzYbkYomj5V98lLytkQ8gBgj4PFN5ZDT3jYxz5cvsPiQ9WeVMFgSeQfaaqXdd1n_zTYk12lRluHJ0dWjVOROiHiDGcbs3qUUrhAuf_S-Pledc7yFE5hlttmNuJbtBLeyd4N4p9_pjG74NRN3YZM5MgIKeuIxDVlQYz1GZd7d6rRUHysI2HmP01uVQTYcOBqiGy8f9Xzuj1W1zb9_AUK9S5fAPlIEXv8JDUmvpZYv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cunWD6yAdykURv_W2wX6tMXDY28MkZn5g4EQRKvv5XqNqh43bhokrNnrpl3QGwQyaZLWMXP_dtWKtLGYHbWzgDgfqVQKSRcNsZZgPAfotClRBtsP6sux29N4guobzTscYwNlinsv0Rvu3iwZXWN-sCyLNZCvvtraE1AD_dO945YlvfG6l4LopSyf-xlbo4TZIDWgCfSNS3SLZgjoDM-FpUH6sfbzqQ8i6UBEsUKxEdjcr8PZ-7DCG-n5o-F6qYYITwj_MfP_i2J-MtI5ijBiy4EZe2CFXh0a-nRB-LrCAyplc4pSsxGniiPMMmkGdhMaQWHF7O_1S9EqXhTfkd-i2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=HJ1JlBpDmw7o91JCddrSKgvLW7BI61TERth2zWZzUtKQVfhSGPdJZ5TvST8Rc-NQZwO509In6FcjMwKC3aVRNe-9Q0OBvnFawN3B9VSS7LXsmm47A_SdoOChfvvYPb5deKUuMxt9ohl2DVw_6in4rw-221VWIbLJWV2PVrEpPplo9DGu4cloqWihCQBqIQkslb8VBdAeZV0qA3n8_7EmuPAssjPJCNzTo1MVK8M9ha9XCR0tz0idR6NAcURxYZG8fwMFBKL-0mYb7fGgnGcqD0ziugn1XJCYqbrK8y9bDQ6TvQJFqMlmxwus-xfQysAFbSycnSBlMOLc1V4edcJdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=HJ1JlBpDmw7o91JCddrSKgvLW7BI61TERth2zWZzUtKQVfhSGPdJZ5TvST8Rc-NQZwO509In6FcjMwKC3aVRNe-9Q0OBvnFawN3B9VSS7LXsmm47A_SdoOChfvvYPb5deKUuMxt9ohl2DVw_6in4rw-221VWIbLJWV2PVrEpPplo9DGu4cloqWihCQBqIQkslb8VBdAeZV0qA3n8_7EmuPAssjPJCNzTo1MVK8M9ha9XCR0tz0idR6NAcURxYZG8fwMFBKL-0mYb7fGgnGcqD0ziugn1XJCYqbrK8y9bDQ6TvQJFqMlmxwus-xfQysAFbSycnSBlMOLc1V4edcJdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=k_c0ECJ7BiWjyt8S7Bpa_JSVsUT6ZZsoFgMlYNaeehvEiEUCQ9FcJewmoJN1cjnZ0eFPPmxtxbia6ZD068sM2UNPJn1HA_vLV_hvADoqgG7DJg7gO-0NTP_YdrsCMkqVE0mp7o1HFNVh83N4zVNGh7ogQi8litSdqUhyYEsL8IRCqrw7wlQPtjntXm825YYeOzi-8sx8ffnMaZ3axByEyKL-HftT3c-Drw96nq35_XKIvncvJD6Y2DsEhIFN68wqzcz5J_BbIAry7a2KBQpXy5Js4GzIxU_rg9g1jqUpQlwWnRaW_msV_37ySanmExSHYxfSHVXOKGeARtCR2PuHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=k_c0ECJ7BiWjyt8S7Bpa_JSVsUT6ZZsoFgMlYNaeehvEiEUCQ9FcJewmoJN1cjnZ0eFPPmxtxbia6ZD068sM2UNPJn1HA_vLV_hvADoqgG7DJg7gO-0NTP_YdrsCMkqVE0mp7o1HFNVh83N4zVNGh7ogQi8litSdqUhyYEsL8IRCqrw7wlQPtjntXm825YYeOzi-8sx8ffnMaZ3axByEyKL-HftT3c-Drw96nq35_XKIvncvJD6Y2DsEhIFN68wqzcz5J_BbIAry7a2KBQpXy5Js4GzIxU_rg9g1jqUpQlwWnRaW_msV_37ySanmExSHYxfSHVXOKGeARtCR2PuHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=fa8RLtAe2PjHQd658xbqCLnCKdpnfzUSMYaO_SU4oKmjkwnWP3RipLhkjlza4dMLFsYHfOr4u7TJVQmOpb1VoqedMvLf_hjp_n5tXY3uccz0jm8j05N9ZgrEhWeCVGpIetEEoQn_SLVR3bHUBE42UskgOm7-TvRn-nnffkQBOQf6sLtmRhEwoE1bLy-bC7K3VS0WqAu-ZvpQz3AkHyG4MuV-qLL4wYYKTk6o7_JvBLrTS565y78f-wgc0sLqO3yk8LWhh3uL7teZREFG-60N1_KMeDhH7qghwS50LkTseyTVgprrDkWzZ9IBjGuhql1RLg8Ya5JxuRomI-pgjsNz0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=fa8RLtAe2PjHQd658xbqCLnCKdpnfzUSMYaO_SU4oKmjkwnWP3RipLhkjlza4dMLFsYHfOr4u7TJVQmOpb1VoqedMvLf_hjp_n5tXY3uccz0jm8j05N9ZgrEhWeCVGpIetEEoQn_SLVR3bHUBE42UskgOm7-TvRn-nnffkQBOQf6sLtmRhEwoE1bLy-bC7K3VS0WqAu-ZvpQz3AkHyG4MuV-qLL4wYYKTk6o7_JvBLrTS565y78f-wgc0sLqO3yk8LWhh3uL7teZREFG-60N1_KMeDhH7qghwS50LkTseyTVgprrDkWzZ9IBjGuhql1RLg8Ya5JxuRomI-pgjsNz0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_AWKluSHS0UNn2nPk4PQ1lKn0Q81V-kmOgwo26u4FBbkLEMk_9wAk5UdBhZuY0JgbfVNvPen8xKIN6uqDb7-GJiVAfrPRiZqC9P4s-9CEJru-HfDM14YV7jSmeH12Tuy78XJ4RU52tHPC38-VbEvgjUE46uQuCNWXFfOA_klq_55VoGfz_MINF_kT6-K9pJeucU9K19rykg6ou8KiGG-0ZLWjQE9hjFOM5AWVn5X3lwU57wWYsWERnQWaumja8tu1Lw-zIhwGZtu9T_h5X8qPQ-60IFKy9V9RQsa3oh3-TlB-9lA9qQ7rS_mqCSg0MFDNBL_4w5XIquzZhgk3x5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxZk1qqmXlTmcq9Vgx549pUGvl9ALyIJTqYjQ6_8M474QKxQ7PCBPOdzBLE4pcIZbsNyfs47NA16ZeuLDNv19zP1r5IxRTPnlhmp1tkwjECPWIumo7L1pFkfAfXhTbt8RMcH0HJHzq3qyVyaSrHmqn4fEXS3tFmPF_vmRJqK3Qjw1YdtG4fE9oKYqlTLMJjHPNxFwuslwWhCFpDZKRnDuYAu68WcnbtTXQ6a2XSqiREoDhsaXmk-C9Srvo30jvruCd_uSBS2C89PAF4QifeHGzoTKoNjsU__4lBbroBq9ZncnrQoNUt-PBuGP7K5C-nm_kklpKHjcY9Ya5kBBWRb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=jG39XPEQrCg87Qc6rq5W1VGE1QFcgtIX2Vi8hIATWvRhNhh2Is7sj8T5V9bkl2QxfejU6fO5X8u9PjuuWW5Z5YAMiGs4868THvdPz7e--BNAmbDsJHKx4eDVvlVay7BVLvXi1lWA4EvY-gov5WbwdGkYmqclha8AqAIdlaJDBEjcf8kNNCSwHJUrN5NEyFJLDKa8etv6lDtJphxeTDv9hmtGIY7w9oSHCl85isAL4BzcVMfrXlPsOWB5SUeGdf3IYugEpEM7qUDmxtJ4_XSE1VUXNKNs14_VlUHb8uLjQ45yTgtAaD_Ge-rVL9x3uZ-4qizdwZHLbUX0r4fyrMqPdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=jG39XPEQrCg87Qc6rq5W1VGE1QFcgtIX2Vi8hIATWvRhNhh2Is7sj8T5V9bkl2QxfejU6fO5X8u9PjuuWW5Z5YAMiGs4868THvdPz7e--BNAmbDsJHKx4eDVvlVay7BVLvXi1lWA4EvY-gov5WbwdGkYmqclha8AqAIdlaJDBEjcf8kNNCSwHJUrN5NEyFJLDKa8etv6lDtJphxeTDv9hmtGIY7w9oSHCl85isAL4BzcVMfrXlPsOWB5SUeGdf3IYugEpEM7qUDmxtJ4_XSE1VUXNKNs14_VlUHb8uLjQ45yTgtAaD_Ge-rVL9x3uZ-4qizdwZHLbUX0r4fyrMqPdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q9QevyZszCLS8vbecGJrvI-HMM0W4Mla2F1mYNEyAo-2w_q3L6q4ROBsa2X4DW-Pgvt68wqDLiuY_HK6EWlo6TosxFxdH0AsioPAWOF9A1gG03akcByXfy2r2uLchpkkgtAT2wkx8_z1ko4BXYhShHLFLSOnSOWq_czx392FBKA2xPykn6sjTwkC6yief21u_spG4O7Xlzq2yu8YUlkJtCPtCSqu7_OOXoSfsr_SWnoQIP3V2VcR4jaq_zSaZio_egcrOL_euH4Dmd3UEM0rHrwCgeKkQSBljG57WlXVlkXIOYwXC7f0A0tR_W2nCW73IxuEuXw-EkE1Yd9U3ImvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UmOos4PsZmX0Dh1HLSJ3B4azD4qpGQRUnMoMIYWURW_ruluegt4XwVxTuX2lcMbec2s4bEP8UCDTnIZWCaoJy2vZjMRs517N8u1NJpPds9uMqZ0rpajzQA30Q0DzYJ-P5DxpSqCDOyO39FAs2BMCLVqtR84OEXPxLc4d8FonB7e9QI08DRmjCyBTkZDgrq8i0yeXp_DCoZ4V2PwLINPDgWvC9E0wp5-pVD6cdTZaxt_YxkilpIC7jMurKiKmDkBj9Y6jMCBYdlxMVKOR9l6su9-W9jvkIPytocmypmW2eF0bhStr29m8K7YQgGY5Jh2LJRhhd3LELLN1wGMLDJv3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UmOos4PsZmX0Dh1HLSJ3B4azD4qpGQRUnMoMIYWURW_ruluegt4XwVxTuX2lcMbec2s4bEP8UCDTnIZWCaoJy2vZjMRs517N8u1NJpPds9uMqZ0rpajzQA30Q0DzYJ-P5DxpSqCDOyO39FAs2BMCLVqtR84OEXPxLc4d8FonB7e9QI08DRmjCyBTkZDgrq8i0yeXp_DCoZ4V2PwLINPDgWvC9E0wp5-pVD6cdTZaxt_YxkilpIC7jMurKiKmDkBj9Y6jMCBYdlxMVKOR9l6su9-W9jvkIPytocmypmW2eF0bhStr29m8K7YQgGY5Jh2LJRhhd3LELLN1wGMLDJv3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbReD9pcGPrHah9H5fQf11k_Rb_-Qea2zA2ULGGTQyeezhB2iGEaZNWepvvLYUsEOcnN9QOV0qBaWPA0yPLw4atB-togjuyJbJXuUSQxU2zBWqohGUqxEpOa0Q-PQZB4Hi58tyKjo0w-Kgl-qGOPAr7F4O_DEhEWPl3Iz0baqL54Nj0YB_cIeja0CgDBHq_Kni3GGmcVcfuURLj8aE9gVlcAIr9d__Vndxt6KKra_JeCmoi9YJYOfapXjNO0paNuTZS_LfkTu4uA5ZvD1eV9qllS5IVtx74IlBpi9djyrNifGUO2nvJ4cMRXCSBYPiGeYgT4Ag_uTXPSAE2wecRapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=J9UeLcEcU6p84wJpbSbpgh0wFMr5iR4Bz0YpIBtLWOfv_LfrA7nh0Vy5IKF7LUanzmeJChaLqlfHZrH6bCVDq1ov2GpQvhG2VzQuv4QezL-edrEyDS9hXkbjKkqABorsCe6FFlhDTMOPsfpC12geeCyvbCS_-8Uje8JQV_1S-YuxxzE6_Ut09KZ-dxVv1zByuTgTaXQLKBTlpvqwOJZ3P_UOz_4CzfeZIYQNZfx9P6tZdQSN5Glj7BlaO8JPYu7X1mwJtI8fiSanO_ttR2GJ01Vsss-RUsbM0Dlvw54cfyyasAIf5GuWq4JjMJPG415jRwAhneWJvJ5JNcizjQC76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=J9UeLcEcU6p84wJpbSbpgh0wFMr5iR4Bz0YpIBtLWOfv_LfrA7nh0Vy5IKF7LUanzmeJChaLqlfHZrH6bCVDq1ov2GpQvhG2VzQuv4QezL-edrEyDS9hXkbjKkqABorsCe6FFlhDTMOPsfpC12geeCyvbCS_-8Uje8JQV_1S-YuxxzE6_Ut09KZ-dxVv1zByuTgTaXQLKBTlpvqwOJZ3P_UOz_4CzfeZIYQNZfx9P6tZdQSN5Glj7BlaO8JPYu7X1mwJtI8fiSanO_ttR2GJ01Vsss-RUsbM0Dlvw54cfyyasAIf5GuWq4JjMJPG415jRwAhneWJvJ5JNcizjQC76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
