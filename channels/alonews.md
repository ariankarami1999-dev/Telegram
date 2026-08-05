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
<img src="https://cdn4.telesco.pe/file/kF-7X85kdkktmzHvQFspvR44Z0S0k0TotNH7CzwYqCxATVyV4Kwb6fOpXRsUBP_XW7CAtAGbhAiwSPsO3nGoI3_UsT1qPd7bVfY3YI8zaIX1oZWW-_jli1gWptMDMANW7mDWIkT6mxDuKM4PHX3hVXIQMhhNenrG5WBl0bH05-IuF85aHfHpjY2_0imotGtiafLzPoGFHNImvuPK78DkNyD799dTdZkw0Hx4_oSe0ZHdOtRmnQeViFPol6omDlZYwqsUkNslR1Wv7uOOkh46EgREbLEuorSvS0SiPxBdGqugvg9g8A-x09ZfgcmcJS_QKEP9MW7RBdYUMU5S7pap5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 984K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: ظرفیت مسیر نفتی جایگزین تنگه هرمز را به ۲.۵ میلیون بشکه در روز می‌رسانیم
🔴
وزیر انرژی ترکیه با اشاره به بحران عبور و مرور کشتی‌ها از تنگهٔ هرمز گفت تحولات ماه‌های اخیر نشان داده است که جهان به مسیرهای جایگزین برای انتقال نفت نیاز دارد و آنکارا در حال مذاکره با عراق برای توسعه مسیرهای جدید صادرات انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/140058" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOfF_8OgyMpwbv7yWUmKS3GIV4Dl2hF7SZOZJ-LMWqsGmpvT4FWWkm4Ej9Uz29DKjlQZ9xNzf1XtdicpoIPTApDUgQx_SYVTWemdpxFNk6XyW6K5iKtb9Z4Oj1cqSVTeETQmgyAuxAlfQgR0NG3PCTyKcwuVhOVZC2xm0yrEhWTTHMSwHJFUTRR_gd8e-esS36wqFX4Lit27I4cwnbCOKvDcSWkwkwpDRHRntKCA9-ZzgjBQ3oJkJL6aHrG9CbWlnWg9m_WtXJkECGQaoSartHjEL4PbhFeBStlWiObTs_jwpfFWLzplQJLTNc07c4Qt6ATMN5aXyXH2fOifGUTbow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز UKMTO می‌گوید ناخدای یک نفتکش از شنیدن صدای انفجار مهیبی در نزدیکی کشتی خود خبر داده است.
🔴
این حادثه در ۹۵ مایل دریایی جنوب شرقی عدن، یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/140057" target="_blank">📅 19:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نماینده مجلس: طرح موضوع بازکردن تنگه هرمز در مقابل لغو تحریم با واقعیت مطابقت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/140056" target="_blank">📅 19:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فووووووری / منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/140055" target="_blank">📅 19:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فووووووری / منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/140054" target="_blank">📅 19:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f4c0e158.mp4?token=dVoeY5atjqFeXu4Y1xKXcMKp0DNcW1hadBBD-8_X1jd_A88j-zqzo79Wm5Ymg4ZGtrhvdEH3IT4-bYToeis-qzUfvK_4CmI5d30m9EHhchrslOMnoKMQtoBR62HRcRZOX9uXHgA0alI1YX0Jz9mHQGYQSHCrRVYaXrbpOGeMITMnyU9o70wjOonaDAZ4gN5YSYg3FrVER1eC-BTOf27fXO5rK8RZ1uIL4n3I3mBBYI9saV6fdaIiK-ecnynID2pcUjhSTDUDlnWlFj5TaMEalUx2duWyBc_FJ_mOo6ZFK7yO_MJDXJ_qkAfHmPB4T0vFneLgwVvU6IcZaX6f-iuRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f4c0e158.mp4?token=dVoeY5atjqFeXu4Y1xKXcMKp0DNcW1hadBBD-8_X1jd_A88j-zqzo79Wm5Ymg4ZGtrhvdEH3IT4-bYToeis-qzUfvK_4CmI5d30m9EHhchrslOMnoKMQtoBR62HRcRZOX9uXHgA0alI1YX0Jz9mHQGYQSHCrRVYaXrbpOGeMITMnyU9o70wjOonaDAZ4gN5YSYg3FrVER1eC-BTOf27fXO5rK8RZ1uIL4n3I3mBBYI9saV6fdaIiK-ecnynID2pcUjhSTDUDlnWlFj5TaMEalUx2duWyBc_FJ_mOo6ZFK7yO_MJDXJ_qkAfHmPB4T0vFneLgwVvU6IcZaX6f-iuRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل اعلام کرد که یک آزمایش از پیش برنامه‌ریزی شده از سامانه دفاع موشکی برد بلند «فلش» با موفقیت انجام شد. مسیر پرواز موشک از مناطق مرکزی اسرائیل به سمت دریا قابل مشاهده بود.
🔴
وزارت دفاع گفت که جزئیات بیشتری درباره این آزمایش که به صورت مشترک با ارتش اسرائیل و صنایع هوافضای اسرائیل انجام شد، در زمان دیگری منتشر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/140053" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قیمت جدید بنزین سوپر در بورس انرژی ۸۴,۶۰۰ تومان تعیین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/140052" target="_blank">📅 19:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
المیادین به نقل از منبع امنیتی-سیاسی ایرانی:  مذاکرات ایران و عمان درباره ترتیبات مشترک برای مدیریت تنگه هرمز به مراحل مهمی رسیده است.
🔴
ایران تأکید دارد که یکی از ترتیبات ضروری، ثبت هرگونه ورود یا خروج از طریق تنگه هرمز در یک سامانه ویژه است.
🔴
ایران معتقد است این اقدام امکان اعمال نظارت کامل بر تردد دریایی را فراهم می‌کند و به جلوگیری از وقوع حوادث در تنگه هرمز کمک می‌کند.
🔴
عمان همچنان در حال انجام رایزنی‌ها و مذاکرات درباره این پیشنهاد است؛ پیشنهادی که ایران بر اجرای آن اصرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/140051" target="_blank">📅 19:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974ee64391.mp4?token=QQuL7FnUm7WH0eCj-ZmFTpV5J53HhJU_UscFT0Y2neqPrpzh8jJkSPS-Dsoj6t2Zphs-FJh97b9IxY0aEG7QWvjAS-tg8uAhI-xwHry3__-kmhE7hQ0194glybWN2VHA5K-RDsE6nOuAHcT_H6EN77lIPKg0aT56i_KbrQ-0d_uE8f5ovTvx9WmTZWvOA4ABXfzUi_EfphYAx2RY-aVP2npFoCiQ12rVTH7HZTygV9oAW0Y_4ayucCAtXnqq3gX0watQeiE-vDCgU1TgEjkYCeV4i8Jy5r-ZzlYmkcW-uX0RbvOEQXvLGrXY0RmTGdRjH3p4i3DswTBD98TuYhf8Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974ee64391.mp4?token=QQuL7FnUm7WH0eCj-ZmFTpV5J53HhJU_UscFT0Y2neqPrpzh8jJkSPS-Dsoj6t2Zphs-FJh97b9IxY0aEG7QWvjAS-tg8uAhI-xwHry3__-kmhE7hQ0194glybWN2VHA5K-RDsE6nOuAHcT_H6EN77lIPKg0aT56i_KbrQ-0d_uE8f5ovTvx9WmTZWvOA4ABXfzUi_EfphYAx2RY-aVP2npFoCiQ12rVTH7HZTygV9oAW0Y_4ayucCAtXnqq3gX0watQeiE-vDCgU1TgEjkYCeV4i8Jy5r-ZzlYmkcW-uX0RbvOEQXvLGrXY0RmTGdRjH3p4i3DswTBD98TuYhf8Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان فترمن: کشور ما مسئولیت بسیار ویژه‌ای برای حمایت و پشتیبانی از اسرائیل دارد.
🔴
ما دموکرات‌ها هستیم. ما ارزش‌های پیشرو داریم. اسرائیل کشوری است که در آن منطقه ارزش‌های مشابهی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/140050" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ecff42e55.mp4?token=BGbBmsT4pq55T2vDawT5dvNK7jW9LYGRP3v82kTndNaoPui5g1PkqPJj5g07C5xw-mztF3XJNtzpmB3EmLnif0Q2HJU2FxqhIh4_oOvhgOWJqCo5Oz5s7YgeiGfEOHcR3Negyo_t22IHHZ3ZtvhIHMY9NTg6QjufGXTGWJC2NfqyKOI9BoNPoRYDmh_u6MAdd3Ksmc8CGGiYV8lz64j1v66j5AVJ7xZBIwL_7pNWBcvLGJYq5HQFW1JcpizILaB0Xorl1Mu7Qzgo-owuY5ABVOA_1gLQVAkPiyX7sOLkxmjMk3BLPZyJbC_6vePJjljEKtCS0Z4emzJx9EDbIcuyvTcd6uIaCfU51KBmTqU3Dju_xAt7Aa7joMArc3xeiFEPu8RZqtgSoq0JtctOEXoB8-DZMKIeYetubCYaFmloqLgmspBsYn_xDP3LZ9d3uSa31YICHngRxCRT6EqiMD66DVA3RBr9ECJs0P5rfSsiKcJv9mJJEGRlUTChEecvHDIkCtly_PwfWLRMzzJ4kXwuM_dqLoyydoSHbgVhXMC6VdlPqtKR0md8_KGZcc1ZrGZzq5s29kuIILhAk_kbt9PhV8hSWDeG-ogRjdWexLLIQdQTyc82-EP_TZG3agExmM1T7nHzrrcMrorAOKkUAxQJqNMMeuyNBAogixYzxUYOgGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ecff42e55.mp4?token=BGbBmsT4pq55T2vDawT5dvNK7jW9LYGRP3v82kTndNaoPui5g1PkqPJj5g07C5xw-mztF3XJNtzpmB3EmLnif0Q2HJU2FxqhIh4_oOvhgOWJqCo5Oz5s7YgeiGfEOHcR3Negyo_t22IHHZ3ZtvhIHMY9NTg6QjufGXTGWJC2NfqyKOI9BoNPoRYDmh_u6MAdd3Ksmc8CGGiYV8lz64j1v66j5AVJ7xZBIwL_7pNWBcvLGJYq5HQFW1JcpizILaB0Xorl1Mu7Qzgo-owuY5ABVOA_1gLQVAkPiyX7sOLkxmjMk3BLPZyJbC_6vePJjljEKtCS0Z4emzJx9EDbIcuyvTcd6uIaCfU51KBmTqU3Dju_xAt7Aa7joMArc3xeiFEPu8RZqtgSoq0JtctOEXoB8-DZMKIeYetubCYaFmloqLgmspBsYn_xDP3LZ9d3uSa31YICHngRxCRT6EqiMD66DVA3RBr9ECJs0P5rfSsiKcJv9mJJEGRlUTChEecvHDIkCtly_PwfWLRMzzJ4kXwuM_dqLoyydoSHbgVhXMC6VdlPqtKR0md8_KGZcc1ZrGZzq5s29kuIILhAk_kbt9PhV8hSWDeG-ogRjdWexLLIQdQTyc82-EP_TZG3agExmM1T7nHzrrcMrorAOKkUAxQJqNMMeuyNBAogixYzxUYOgGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین زلنسکی
:
اوکراین لانچرهای موشک بالستیک روسیه را نابود خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/140049" target="_blank">📅 18:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3589745b.mp4?token=CnMWZ7RNbn7PwRPrIJT9FuvWLwcIdco_4Xb9hTHeHArsDSez6dMPL1_e0l8PMCwT2rqHbpBTXu63IIPFRlohFXH2kC-lKI82lco20fpuj-lOyXwOAnsDmcWbi2-w4pzgbeRCZPJzOSOgdSI84usnmWzsgFOhZV-f2Gl4MIhhOdSiFFYemiaM0fDJJMqkjPBVHfCFmbTjutNyB1Yf6pBLkzDv-OerAjdoHmWn7P8hhdNmAw_5wu3LM0jisi37XySyPtelKqCIpxQgLRJDKzrZAxCEWRSFBDjoWtVoEEPBxf_2Qy-j-idh191ShUWzK_o61MTtWi4gKm58osAkOXzljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3589745b.mp4?token=CnMWZ7RNbn7PwRPrIJT9FuvWLwcIdco_4Xb9hTHeHArsDSez6dMPL1_e0l8PMCwT2rqHbpBTXu63IIPFRlohFXH2kC-lKI82lco20fpuj-lOyXwOAnsDmcWbi2-w4pzgbeRCZPJzOSOgdSI84usnmWzsgFOhZV-f2Gl4MIhhOdSiFFYemiaM0fDJJMqkjPBVHfCFmbTjutNyB1Yf6pBLkzDv-OerAjdoHmWn7P8hhdNmAw_5wu3LM0jisi37XySyPtelKqCIpxQgLRJDKzrZAxCEWRSFBDjoWtVoEEPBxf_2Qy-j-idh191ShUWzK_o61MTtWi4gKm58osAkOXzljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو با وزیر امور خارجه بریتانیا اد میلند دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/140048" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شهباز شریف: پاکستان به تلاش‌های خود برای صلح در منطقه ادامه می دهد
🔴
رایزنی‌های مثمر ثمری با دکتر پزشکیان درباره برقراری صلح پایدار در منطقه داشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/140047" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
🔴
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
🔴
سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/140046" target="_blank">📅 18:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/لحظاتی پیش نتانیاهو یک جلسه مهم را به صورت اضطراری به دلیل رویدادی در خاورمیانه ترک کرد و اعلام کرد:
🔴
نیازهای موجود و بسیار مهم در شرایط سیاسی، مرا مجبور می‌کند که قبل از پایان این مراسم مهم، آن را ترک کنم،
🔴
ما در حال حاضر شاهد تحولات نظامی و سیاسی مهمی در منطقه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140045" target="_blank">📅 18:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مدیر سابق موساد، دیوید بارنیا به شرکت فناوری دفاعی آمریکایی اونداس می‌پیوندد
🔴
دیوید بارنیا، رئیس سابق موساد، پس از ترک اخیر آژانس اطلاعاتی اسرائیل، به عنوان رئیس جهانی و رئیس هیئت مدیره به شرکت فناوری دفاعی آمریکایی اونداس دیفنس پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140044" target="_blank">📅 18:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نتانیاهو: ترامپ بزرگترین دوست ماست، اما موجودیت اسرائیل قابل مذاکره نیست. چه با توافق، چه بدون توافق، هر کاری لازم باشد برای تأمین آینده‌مان انجام می‌دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140043" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
الجزیره: تنها یک یا دو موضوع باقی مانده برای دستیابی به توافق با عمان باقی مانده است و می توان آنها را حل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/140042" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL4AWsgeqMD3SFe_okQFNlNV9vexylHHU34WA6fENX-pzaWjS4XJWwXk8co55DOnlySAMeAYD5eTIMvhSlnCE3RHBsG3TXcZI1gT3WsYQvTHT9323unwR1Cw0AzyyKnHtmBuAfrgPBze-UKBPEA6sqBJa8Mm516d2cPkYkefJYfS_yuOb0wBYgEAJhWIt35xpnZdSqITTWktIpMzZrxDYicZ0-2zyYbCUOSe17_vMRbxcH-pXG2crMZHw7425jvmkpUjG1hkqTCLbmXCOcAWzstIRcSkddpbcI9W6NScAXmiVSkc_ugLa-sLqaVA-WMbnwVoYbezKea0MntjapO-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات رفع تحریم ها در وب سایت خزانه داری آمریکا
🔴
تگ IRGC چند شرکت هواپیمایی و هواپیما حذف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140041" target="_blank">📅 18:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل: بر خلاف آنچه که خبرگزاری رویترز گزارش داده است، این اقدام یک کاهش تحریم‌ها علیه ایران به طور خاص نیست، بلکه یک کاهش تحریم‌ها علیه عراق است .! که با شرکت های مرتبط با سپاه بتوانند کار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140040" target="_blank">📅 18:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7MDX11i-BpFKlzj26RJpB9orqPgm9Cr6BZR5yF5YIwt9A3FQKKiTIog9jp5t-9uVz8XHXob3UIJWVQubG2Hb_ArAla5Bk8AFAvlg5Ml-yN7_ksjdHSehXLwNNZ2Ta35MZPJbV-IUtDhLwV84BKBR1I0faFhiAgArX8j8hXkfNRzn5FqVazTo3ehMY7EEOJ3wsLuvQyF5EkkvnapIHR_06eJVCc5t0i0bCeMAuKDT8G_psoJDeSho9uSgS_ygdqn9zZHmHYrut-08_Y4pw6kprErPdz2hcYrW5TWzDmylt4wdA0pkBbHd53NdWdPGp2z9coa5ouWwBUxdT888Z5M2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وای نت: قبل از شروع جنگ 40 روزه ایران و آمریکا، یه طرح روی میز بوده که بر اساسش قرار بوده حدود 15 هزار نیروی کرد با حمایت هوایی اسرائیل از مرزهای غربی وارد ایران بشن؛
شهرها رو یکی‌یکی بگیرن و همزمان افراد بیشتری بهشون ملحق بشن تا تعدادشون به 150 تا 200 هزار نفر برسه و به سمت تهران حرکت کنن.
اما این طرح به خاطر مخالفت نهادهای اطلاعاتی اسرائیل و پایین بودن شانس موفقیتش، هیچ‌وقت اجرا نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/140039" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رویترز:
بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140038" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوووووووووری/اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/140037" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس:
مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140036" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق مربوط به تنگه هرمز شامل دریافت عوارض از کشتی‌ها برای عبور نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140035" target="_blank">📅 17:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق مربوط به تنگه هرمز شامل دریافت عوارض از کشتی‌ها برای عبور نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140034" target="_blank">📅 17:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رویترز: توافق بین ایران و عمان در مورد تنگه هرمز هنوز نهایی نشده است و عباس عراقچی، وزیر امور خارجه ایران، در حال حاضر در تعطیلات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140033" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فرمانده‌‌سپاه:
وقتی آمریکا و اسرائیل خلع سلاح هسته‌ای شدن ماهم میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140032" target="_blank">📅 17:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جائه‌میونگ، رئیس‌جمهور کره‌جنوبی با اشاره به نقش فارغ‌التحصیلان آکادمی ارتش در تمامی کودتاهای تاریخ این کشور، خواستار ادغام سریع دانشکده‌های نظامی ارتش، برای جلوگیری از تکرار کودتاهای احتمالی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140031" target="_blank">📅 17:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هواشناسی استان تهران: از عصر پنجشنبه وزش باد نسبتاً شدید به‌ویژه در ارتفاعات و مناطق جنوبی و غربی استان، همراه با خیزش گردوخاک پیش‌بینی می‌شود.
🔴
همچنین دمای هوای تهران در روزهای پنجشنبه و جمعه بین ۳ تا ۴ درجه کاهش می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140030" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز: علی‌رغم اظهارات رئیس‌جمهور ترمپ، به نظر نمی‌رسد توافق‌نامه‌ای در مورد تنگه هرمز هر زود امضا شود، زیرا چندین مسئله بزرگ همچنان حل نشده باقی مانده است.
🔴
مذاکرات در حال پیشرفت هستند، اما هنوز «زود» است که بگوییم توافقی با عمان حاصل شده است، یک مقام ارشد ایرانی و دو منبع منطقه‌ای گفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140028" target="_blank">📅 16:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ارتش اسرائیل در پاسخ به «نقض آشکار آتش‌بس» توسط حزب‌الله، حملات هدفمند در جنوب لبنان را آغاز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140027" target="_blank">📅 16:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIbpN40vHGegrWiiqpOUPmWxL-P4L7OiJJ7WXE_J7VvM9O7K1ZpnI0VUtmzhzoRvhB7dD2GLLBfpXCLPbsfh0dd9vixnJiKwcDnZZiF2YU82Im6MLr3X81ydMCXesamHwBx-6Hm5ee8Rjqu7nW89zW4HC9xfGY_6Wg1wYfZ-FxouvnLUGg0o_-c18q3Iu0RQO9-DV4hek0m0iNsmt5j5VGRFq4ngyoU5HpkUpfj8pF2kRlihN79opHEHig7rBLNITljFO2gQdh4AvEEMr4-6UbBZ-yZ6yD7w5io5a2T3YmfEIE2uO1LjsoWakSy9f3eTLu7AcNTJR3-trqzw7Yx6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : کره جنوبی پروژه راه‌آهنی که برای مدت طولانی در نزدیکی منطقه غیرنظامی متوقف شده بود را احیا خواهد کرد که در نهایت می‌تواند با شبکه راه‌آهن شرقی کره شمالی مجدداً به هم متصل شود.
🔴
این اقدام بخشی از تلاش گسترده‌تر سئول برای بهبود روابط بین دو کره است، علیرغم بن‌بست دیپلماتیک در جریان و تخریب کره شمالی از پیوندهای راه‌آهن و جاده‌ای فرامرزی در سال ۲۰۲۴
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140026" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام از کشورهای حاشیه خلیج فارس: احتمال رسیدن آمریکا و ایران به توافق موقت در روز جمعه ۵۰/۵۰ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140025" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر خارجه سعودی در شهر امان با همتای عراقی خود دیدار کرد. بر اساس اعلام وزارت خارجه سعودی، در این دیدار روابط میان دو کشور مورد بررسی قرار گرفت.
🔴
همچنین وزرای خارجه دو کشور درباره تضمین تبدیل نشدن خاک عراق به ابزاری برای تجاوز به همسایگانش گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140024" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGAZ1DEatMOJsZGO6HTh7ToG1uRI3mueyuD8XFuxSIU1nARcdb2UvzjXkbF7KIiFDcc0hofkrZrETw1qiFJPI1wy0tygOsdgsrnp9CF0xyr_K3N6obHyd-cEEZdmGQcr4tB7XS0IleuaDXRrlPxuUeYBv3ybaxns7NnhrbMT6Dwj5f4_4YmuQFg3Zhf6eJYFEjLc4AyMO4r60PnJ7H24WT4dgjogu-5w81SoNZJyogcMmtMAWYnjZ37cJRIzh1pDPoaeCC1Fpsc4qkd7uWUISl57AA_W2inMZ_lrVMiSA2dqqDK-uORUs2HmfkdbVUm9Ec2LF13-Z9liiQWWgp8qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرگ یک فوتبالیست تایلندی پس از برخورد صاعقه در حین مسابقه
🔴
پلیس تایلند: «سوفوان آوای» ۲۴ ساله روز گذشته (سه‌شنبه) پس از اصابت صاعقه به زمین ورزشگاه «سانتی‌فاپ» واقع در جنوب تایلند، دچار جراحات وخیمی شد.
🔴
به رغم تلاش‌های تیم‌ فوریت‌های پزشکی، بر اثر شدت جراحات وارده جان باخت
🔴
۱۲ بازیکن دیگر نیز دچار مصدومیت و به بیمارستان منتقل شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140023" target="_blank">📅 16:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حماس: بر پایبندی خود به توافقات صورت گرفته با میانجی‌گران در خصوص نقشه راه غزه تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140022" target="_blank">📅 16:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_WxhH8-HiBB2jr38etQitHptImKoUL0XGxH_cRx4R_H8vFe4e-1R5Icas7kntYiONLTpHgWpSgbKRpeqb9Im7MlAyTmF9arnq4ryIeNqrI3W7rxo5ELe4EdzQiunriuxKB8rVBqiTv_Q4ncpBHaCPHRCfmrTylU6NDqKmucResN5qL3TOTWLt_K3mqJAhjiEgoKGefb8x3Pl4vI5uOIwYR6jhUB_BaYiihKFkOHeWjvy5lrYdTEHGMW6ZKruzuX-uOKSM8mhdn1JiW_ORdtkdtlDEob17JimMb794-L6Afdm5-F7P4UvTqTgfnIS56QsBKGcwgq-r46hWSzbpDk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار از زمان توافق چارچوبی، ارتش اسرائیل هشدار فوری به ساکنان شهر المنصوره برای تخلیه و عقب‌نشینی ۱۰۰۰ متری از شهر صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140021" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز نوشت:  داده‌های یک شرکت ردیابی دریایی حاکی از آن است که تردد کشتی‌ها در تنگه هرمز تغییر چندانی نداشته و همچنان بسیار محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140020" target="_blank">📅 16:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkjx4UY4fKgmnwZIOi4hKBLACUn8li3MBsI7evS4I7EEgk0qhang5iTzMQ5W_YokksKnrJAetiB4lWwF8WJ1PJIavEFu_Gh4xNYmWXvZe4FQ3_Nv4V90wWm6PRJegkM7mncuuPBKp2Gj96XT-AA65kkwK5AIjPk8uLP4WVFt7lTHxfINDX7jEnSnsx5twAD4lUexUJetJVHjjbKjSnPvpH0BMH5dIRG3YHrCjYiGrprhLk4d3Wfjxxg7GAmQcGwGQb-hhfG1ueRQRaZlY0zrPHeSZN3CunAfIdI5PvrFmEIZkheXf2Xj8BQaN-4AjujczdY1ZjgIsAjFDnFwt9CIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا در ساعات اخیر بیش از ۱۵۰ دلار افزایش یافت و به ۴۲۰۰ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140019" target="_blank">📅 16:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri_fi8TZWD6kzWySzLAv_Q_mn_Qx6IGNHI11Lf2KNMkXbcnqAhL7HzHZl8PoCNHVaTLqDmRLcmH-vBDg_YVOyuowhMyX8CC4PV_TDqtg8Hl4-r6kBu3NHfsBJOHV_KF0jDUSSLhTJb-kLsj8-F7okjqj0ebgpPalKXnZucOpWPMYPfj5Jd3zpSZF4Tk06iEnzUunrTeerxjigwd3sy2J6hBHaDNK6u8pHlO_YeXemVCckA5EJUrvWjb8YBJHRYj_pki0SGeP2N-iGtGBU77Ubw7UJroFU3yhc6NcWajO4TO0Vt6ugg_I20vRJ1vHyxuf3Lb0KjjmM_VYenb1YseWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل سی-40 کلیپر، که مخصوص انتقال مقامات ارشد نظامی است، در حال حاضر وارد آسمان عربستان سعودی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140018" target="_blank">📅 15:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد
🔴
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140017" target="_blank">📅 15:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد.
🔴
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140016" target="_blank">📅 15:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBa4UbGa2HZXNn8_boM9RDRRJSeGbbZxemxz8ywY8EpQCvK6EO6WpHsF8ac9AwwAd5dxeNVqEsyIptF-_5n9I5xEMPgfWY-x9KDHQnVNnA5ccyfWS_mHqVMkAPSxUbmf1fnNRzX3TDGfmMVgDIotYguwKvyxgsKyXwx5Ka1OazKzsmR8fM38y1F-F8ivqFTjOkhBXdRA1pnrESdJCIVCGeY3mUAA4Zu4PtgHg4n3srj24CQVgIx94Prpoygf0vruYvj9RyfvxNEioHdqaUZz8T51i_uACZkidEQ6Z05PIefsZyVQFbf141NX_xMTQJJosAsl8dkVRicGWzlHD4Qsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پشت پرده حذف تلگرام از «اپ‌استور»
🔴
پاول دورف در کانال تلگرامش نوشت:
یک مهاجم با استفاده از ترفندهای فنی توانسته بود محتوای غیرقانونی تولیدشده با هوش مصنوعی را در یک پیام قدیمی ویرایش کند تا از دید اعضای گروه و گزارش‌های مردمی پنهان بماند.
🔴
این اقدام با هدف باج‌گیری از مدیران گروه‌های بزرگ انجام شد تا در صورت پرداخت‌نکردن پول، گزارش تخلف آن‌ها مستقیم به اپل ارسال شود.
🔴
باج‌گیران، راهی برای سوءاستفاده از واکنش‌های شتاب‌زده‌ی اپل پیدا کرده‌اند. اپل پیش از تماس با ما، تلگرام را از اپ‌ استور حذف کرد.
🔴
این رویکرد یک ریسک ساختاری برای تمام برنامه‌های میزبان محتوای کاربر ایجاد می‌کند؛ زیرا اگر اپلیکیشنی با بیش از یک میلیارد کاربر بدون هشدار قبلی حذف شود، این اتفاق برای هر برنامه‌ی دیگری نیز رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140015" target="_blank">📅 15:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S89yHzulntef7ynMCxkVKkGfYed5g0MpqoUvhBADRjhOvKkQiZTel38zobU10xFCOBkG0LNRtymAdfwq-LCQUB0XTsAGZbkkCoepiYAKPn-Gqnczpjqd0Xb13n_2ON6QiDIFytvLHWeokY0nN7flB5F0_4iwXHLzAfR8JgeJC2PabyGE58Y8z7hfnMigGNNRapxCVhytHFKSJrBHfbYflneTUv8d1bgZNmKrlMOr0MnewhxIFOJOOaTJgdXh_Q29yjGtdqQVtmwbKt5q6FnkkMNf3o8219Qxd6N0kjaLHE88oP3OuF_wjzo9GRFyCUyChTAOrAxU1aVChle8nk6vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون_این کشتی مورد حمله یک شناور بدون سرنشین قرار گرفت که منجر به آتش‌سوزی در داخل آن شد. مقامات محلی خدمه کشتی را نجات دادند و آن‌ها در سلامت هستند. گزارش شده است که کشتی غرق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140014" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140013" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=eeN3B4Ca9FmyryLSroN3zhjkOZ2Mp24JiXFHyJnxn8ymhruR5DaVC7FR3eD4jhxUH5WIku4Ulog7GXN5YdQ3MXV9We8KJkPjGWA8VlF99ga2_f-refkCIBWfu701rdHzvYVIHbkBSJLXE2m1HJZdssw5LopsozVtD3u-U4Jy_0uRkRrn-Eh_Gd3xAyqO8HSRw5Yp-lNuRGT0FhhfnqYW6D6EZDagfI1LM5n4LlUFhPUoYzFw-apTnixrRVa1W0o0L1KYdufyhMR1iL_xvdIB8ew4qozEZJep5OZv-XagTatTOH4h1GyTGDFFkQ4kdfTnQ45oNQSnCCbCW_Q5CYbVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=eeN3B4Ca9FmyryLSroN3zhjkOZ2Mp24JiXFHyJnxn8ymhruR5DaVC7FR3eD4jhxUH5WIku4Ulog7GXN5YdQ3MXV9We8KJkPjGWA8VlF99ga2_f-refkCIBWfu701rdHzvYVIHbkBSJLXE2m1HJZdssw5LopsozVtD3u-U4Jy_0uRkRrn-Eh_Gd3xAyqO8HSRw5Yp-lNuRGT0FhhfnqYW6D6EZDagfI1LM5n4LlUFhPUoYzFw-apTnixrRVa1W0o0L1KYdufyhMR1iL_xvdIB8ew4qozEZJep5OZv-XagTatTOH4h1GyTGDFFkQ4kdfTnQ45oNQSnCCbCW_Q5CYbVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور روسیه، پوتین
:
روسیه یک یگان نظامی جدید برای جنگ پهپادی تشکیل داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140012" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140011" target="_blank">📅 15:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded1face75.mp4?token=C2zW1F940e8YSqcFjvVXAFcy4ugDxLDklOscB8Tr1P9qD_WWviQhVbK4_Rf8fyNB_l5iLmc_7AV2zdiY3W4RMLLhYlVkreULI_cuSuFsWyF6Bi297Cc_SHO3bI6hBBxwrn0htfk46t3xrYWKgvJ6W736jOhbudz3RGP40qhwOJxY3xUkqSWjI5y7kGOTDYwDTWYYudxFo1x3IyWX1hButNa98unObIAtNy7dK8T4p7bxt5cfRFhGAfpFZCn7skWMWv3nwyi8UZxPSM4vyb00iyNgus0iH6-ENTDoHUzo5ZmGdZUxqXLFE_-F9E_6QyOb7f0lgg1gXVKJFKocZ2b1Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded1face75.mp4?token=C2zW1F940e8YSqcFjvVXAFcy4ugDxLDklOscB8Tr1P9qD_WWviQhVbK4_Rf8fyNB_l5iLmc_7AV2zdiY3W4RMLLhYlVkreULI_cuSuFsWyF6Bi297Cc_SHO3bI6hBBxwrn0htfk46t3xrYWKgvJ6W736jOhbudz3RGP40qhwOJxY3xUkqSWjI5y7kGOTDYwDTWYYudxFo1x3IyWX1hButNa98unObIAtNy7dK8T4p7bxt5cfRFhGAfpFZCn7skWMWv3nwyi8UZxPSM4vyb00iyNgus0iH6-ENTDoHUzo5ZmGdZUxqXLFE_-F9E_6QyOb7f0lgg1gXVKJFKocZ2b1Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت هواپیمای هندی به زمین
سقوط این پرواز چندین مصدوم بر جای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140010" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
معاون برق و انرژی وزارت نیرو: هیچ جهش قیمتی در قبوض برق انجام نشده و هر کی قبضش جهش داشته، بخاطر این هست که زیاد برق مصرف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140009" target="_blank">📅 15:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک منبع بلندپایه پاکستانی در گفتگو با ریانووستی: انتظار می‌رود عباس عراقچی وزیر امور خارجه ایران هفتم اوت (روز جمعه) به پاکستان سفر کند.
🔴
وی قرار است با عاصم منیر، فرمانده ارتش پاکستان، شهباز شریف، نخست‌وزیر و اسحاق دار، معاون وزیر امور خارجه دیدار داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140008" target="_blank">📅 15:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=KRBt4la-G18KJiZI0ZbuDYmKxtVfs7iIxCnjPdGWUL5Nmzvjoz5hw_E3AwTdmNsiHB-ggWGVe3gx-27t4OUGtH-l_MGZWkMp5A1EdmgqkioZIEJn9f5V3_INQe-Tc7DK7NolmFkZ1ZmWYgBH_a68QgGY23l6XzhyO3SuiijOcXYwS2hWPNks120H6lsuwzt-mWPFKCamPE71PTAmI_kOWyk9kYUm11tOHaiSjDCdllwCp-1-3o0sk2ypT8-omfkWhLCTPCLMcGykc0763GH-erhBrHFD3urAO1HFN04UxoW9sa0CAQgYV6B9dGcpo9eLo8t6AH2dxu6Q1hf3EI2nnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=KRBt4la-G18KJiZI0ZbuDYmKxtVfs7iIxCnjPdGWUL5Nmzvjoz5hw_E3AwTdmNsiHB-ggWGVe3gx-27t4OUGtH-l_MGZWkMp5A1EdmgqkioZIEJn9f5V3_INQe-Tc7DK7NolmFkZ1ZmWYgBH_a68QgGY23l6XzhyO3SuiijOcXYwS2hWPNks120H6lsuwzt-mWPFKCamPE71PTAmI_kOWyk9kYUm11tOHaiSjDCdllwCp-1-3o0sk2ypT8-omfkWhLCTPCLMcGykc0763GH-erhBrHFD3urAO1HFN04UxoW9sa0CAQgYV6B9dGcpo9eLo8t6AH2dxu6Q1hf3EI2nnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس بعد از فرار از مواضعش، گیر افتاد و کتک خورد
🔴
لباس زنونه تنش کرده بود و داخل یک گودال قایم شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140007" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
🔴
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140006" target="_blank">📅 15:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پرواز جنگنده های اسرائیل بر فراز استان درعا در جنوب سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140005" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حسین پاک، خبرنگار صداوسیما: خلع سلاح مقاومت در کار نیست و نخواهد بود هیچ سلاحی از غزه خارج یا تحویل داده نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140004" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAVC5MBmpPBoyBb5rIACfJ9MDVi6zQuhT8yXm90xaPLmWpsWznCQ-mpXEH4smqwrQiEUol3m0Aau74Mc0Nqymd9FTLdq8ATYLBmr0QGbJh_oJKuMW6OyrErKfO6jH6j_-IxIJx5XZtarxrrh3JsZqYcc6F3rFRx089c6QUUsb_ZAdrzYo_VDfyhn3bhRqK0q3KcZ7W1MKdWdgdKvwZoE2LZmw1j5kVVRuh2UkpWc0dfejnn5v3cXxVEa1nTjM3D8bEzxDS_aYHzQWHA0HLF-taXcxIT9aaKFQDbbh3snN4gCosHBet4tG28O7nj47zz66crau7NXH9QDAnhJHft69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اطلاعیه وزارت آموزش و پرورش درباره برگزاری امتحانات نهایی معوق در ۴ استان جنوبی کشور
🔴
ستاد عالی آزمون‌های وزارت آموزش و پرورش:به غایبین موجه امتحانات در دو درس تخصصی پایه دوازدهم هر رشته تحصیلی در مرحله کشوری اجازه داده می شود در امتحاناتی که مطابق برنامه ابلاغی به چهار استان جنوبی کشور در روزهای شنبه ۱۷ و سه‌شنبه ۲۰ مردادماه ۱۴۰۵ برگزار می‌شود، شرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140003" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
سرویس ترجمه Chat GPT بعد از مدت ها بصورت رسمی فعال شد و زبان فارسی هم ساپورت میکنه
🔗
https://chatgpt.com/translate
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140002" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=FCjDdBGYSAk0tRbPrz-nJ97N6AjubbuznrgQbcrik7ZRIORWtTJUS-fLSH7460d8R3_15bWTtboFmjEaLWYUorOGcFOzhdnjO90E-Zn1LKqZgi7dSnuwg3B9KNg64ieuqNlOhodlISe3Sj31OBU74V9fYJNa6pM4Q3yjpen703ksqKMwL9wpDyoFGnyevYltntILBktHQ4me_VNZUtdSeGBqnRma9JHR9_gTn4AmcNTuP2fJKVXEWkbJE4vjXLALzdkbj5dRcKgEx4OUeg0d2NCUUtLjMt6U8Ig5mIWjnyoqPzcg5E-xXAxwZ7KKk_DoSPKwJzRpohhBE2hMZlVXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=FCjDdBGYSAk0tRbPrz-nJ97N6AjubbuznrgQbcrik7ZRIORWtTJUS-fLSH7460d8R3_15bWTtboFmjEaLWYUorOGcFOzhdnjO90E-Zn1LKqZgi7dSnuwg3B9KNg64ieuqNlOhodlISe3Sj31OBU74V9fYJNa6pM4Q3yjpen703ksqKMwL9wpDyoFGnyevYltntILBktHQ4me_VNZUtdSeGBqnRma9JHR9_gTn4AmcNTuP2fJKVXEWkbJE4vjXLALzdkbj5dRcKgEx4OUeg0d2NCUUtLjMt6U8Ig5mIWjnyoqPzcg5E-xXAxwZ7KKk_DoSPKwJzRpohhBE2hMZlVXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های اسرائیلی، دو سرباز اسرائیلی در اثر انفجاری که در یک ساختمان مین‌گذاری‌شده در منطقه مجدل زون، در جنوب لبنان، رخ داد، کشته و هفت نفر دیگر زخمی شدند.
🔴
آسیب‌دیدگان به بیمارستان رامبام در حیفا منتقل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140001" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری/ انفجار در لاذقیه سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140000" target="_blank">📅 14:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی صنعت برق: افزایش سه تا چهار برابری برخی قبض‌های برق، ناشی از تغییر خودسرانه و ناگهانی تعرفه‌ها نیست
🔴
عبور از الگوی مصرف، موجب افزایش پلکانی هزینه برق می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/139999" target="_blank">📅 14:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اتحادیه اروپا ۱.۴ میلیارد یورو از سود دارایی‌های مسدودشده بانک مرکزی روسیه را برای حمایت نظامی و افزایش پایداری اوکراین اختصاص داد.
🔴
این دارایی‌ها پس از آغاز جنگ و در چارچوب تحریم‌های غرب منجمد شده بودند. اورسولا فون‌درلاین تأکید کرده است که استفاده از عواید این منابع، بخشی از تلاش اروپا برای وادارکردن مسکو به پرداخت هزینه ویرانی‌های جنگ است.
🔴
اروپا فعلاً اصل دارایی‌ها را نگه داشته و سود آن را خرج جنگ علیه روسیه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139998" target="_blank">📅 14:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ان‌بی‌سی: آمریکا با تغییر راهبردهای دکترین هسته‌ای خود، شیوه استفاده از بمب‌های اتمی تاکتیکی را در جهت مقابله احتمالی با چین و روسیه تسهیل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139997" target="_blank">📅 14:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دکتر صدیق،روانپزشک : کسایی که تو گوشیشون بازی ندارن به احتمال زیاد دچار اختلالات روانی هستن و مشکلات روحی دارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139996" target="_blank">📅 14:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک "زارنیتسا" در منطقه زاپروژیا و شهرک "ریژوکا" در منطقه سومی توسط نیروهای مسلح روسیه آزاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139995" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6f01196a.mp4?token=KtyFq1SyvEJNvxvzh58eD0KQW-BUf7LgaqkJfON1xiUbngFpzRY3HRLqr9oAK9hvTLMPaEzJvBDzbCmB1azKOpePSHNIYE1n91tfUfXyIkgisHI9aZF2pMEyGHiYhU5Gif821Qgu9vr5aP-t75KLBwFrAB-JsZIfzu3nPIOJo2U0tUuGA7ArraMR-wq_4IewuSfuCjauW0EJvBWjfk-TdlhAH1pyT_3LCfj2sCdcoRWZFg9Id8McyCDMvXR5v3VqO7MRKeaeE-3FoKgDj-K6JwuuIgosMW9SvnHOHQadFxh0ncsExkmWLKAL-5IOo0ib0KrOdQGURHUSwSgN7aSwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6f01196a.mp4?token=KtyFq1SyvEJNvxvzh58eD0KQW-BUf7LgaqkJfON1xiUbngFpzRY3HRLqr9oAK9hvTLMPaEzJvBDzbCmB1azKOpePSHNIYE1n91tfUfXyIkgisHI9aZF2pMEyGHiYhU5Gif821Qgu9vr5aP-t75KLBwFrAB-JsZIfzu3nPIOJo2U0tUuGA7ArraMR-wq_4IewuSfuCjauW0EJvBWjfk-TdlhAH1pyT_3LCfj2sCdcoRWZFg9Id8McyCDMvXR5v3VqO7MRKeaeE-3FoKgDj-K6JwuuIgosMW9SvnHOHQadFxh0ncsExkmWLKAL-5IOo0ib0KrOdQGURHUSwSgN7aSwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی از زخمی‌شدن چند نظامی اسرائیلی در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان اسرائیلی با بالگرد به بیمارستان‌ها انتقال یافتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139994" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5cPEn6aM-mtjPCduTUepG7MSV5P2XBfECXqjxphv8iKwKI0E8xfQwFc4MOVoMAFcTUuPn2sd-JVsIhX2A1Bbr-_vhZvnQw80Cjn6xJtg1lRjOi6BGbyUt3zh1lvK6g_CnfyGd-aQqHa0GGqMQx1Ys3jZ6Z1le_JgAwxCFYr1GbDbEysRCeJXiWrP-LhGrHf5IgvR6eO9mlETMQ0a_0FjulQagT7Z7kS9B5ya60WO_C_kE-TY6aCe3iZEKR0XzilWALgTDs7VfDtQddTc1Id9dWSEForXm9jv4FhV60dAqcEabBSS04akFNTY0mrV1sxD7JN3YtuJn45pHmfMF5CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر حسن، نامزد مورد حمایت ترامپ، در انتخابات مقدماتی جمهوری‌خواهان میشیگان برای حوزه انتخابیه هشتم کنگره، در مقابل توماس جی. اسمیت شکست خورد. اسمیت با وجود تعلیق مبارزات انتخاباتی خود از چند هفته قبل، پیروز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139993" target="_blank">📅 14:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccaj2g1JJiTAbQ0L6CQmyVWaFEUULX3TzYNEddjyQhYQdbVDG1aBSue8KDk5wx4wmdB5g2vMgF7QkTNSnJaW_-i_ZmArSkYTBAqS320P_pLh53AWu_P8XDcCsKvk-FuKHr9TW6gBCB2k-S-uS2zN0Y72OIX6T9EryMD1SEAIln7A1Ts9Z9rJPjRVUuKQLU_QsB4_Jw4uUlPo0MPKa0ybzjtrjv5Xb_6U7_HuhIFFUuQO8-Edws-IhXyTev7P_kFizcj63eT3ugrCEMfSYfCBOpgzadsXiJ_vLoBH1700_6lwns_i-SDUqA9SNTiqThNfI_ntBUqdrL5eCZDQS2yLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r50vVWRkkQe5sUtbsciSS1VTvzNs-vPJnZLnszrIIcvoGctxMTOgwR3iLOxIrR1SWnsHwkEaohHS09BM4lFN2clIa32egTVYcB5GYsI2ANsFx9to847MqFieZXO7GsMPUrCYvFX3pHtNvK-RMN-5DeCpr1sMy6srzkPo3XshsYw_XmZJUBccBnYPVU5a5681fXwdfA9tU3NKyj5HhqMHIsbkgSk2dSYngtW5d-PmCMrp-44auMGMlUFUVmCv_ujROuCsQNYdvjsVPEp2DUMfmoBTxo8i5mm3iIUZw6xh8k6eC8AENnknoe1HkjMv1hbg4K0LT-9jSxV0lZ6-DhL4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2B1EQT9NWqKAA5Wlya8qiISvI-FDuFrcnwxM8e9T5Viq3oC4t8PCE0lK331z-MCc511cxQ0XGm0TLYifQN4KGFalNtRFL4GwFPKJWS2IIRSq23rcql4mMLA9FyE5YkOGLzs94WkQNfmFvSv6D7kF805Nkyud1IGuYxO1rMyOfU-nL5J-xQH1ZGnnxJiHq00gX0CyYBZZXb8A6g7KpxGd6VDOAHEzYgLyWwgQzBM2IXVejEmxGRussR7XEpHFt7iF25nzJ6jLTfFE3lBpISqz46lndEt2sr7USf7IiJMMH4ReaFdGmJVdzhkLQ8MQ73ymkuvqoEUXmu8vejBc1Rd_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96951795cb.mp4?token=bCnhMMJ5rpG6FoY6Q8GQuW8y6WnXka1SzqFDacpU62hJC2FZUgjRh-8qdJmcwIQeH5uHdeG4giT-nZuGqOh2fzHwokmEqjMLW9z3-GBUsZmxUGZi8F22lt0qHLnKMZylY_aiDKWVHPjOKxHl7OQahNmfDkjKPlsD4S8-ElZ7bnWgLpIwn3Ij8U2FCM1CQLpvcD2Q4XsZSrYryp0i217tLqljUPuOu52K0XRCMqNXH6HpatkWnW13KJmaXwSpkryyFjYxrCy2d1tW5IBrv1avM3cFzSksUP0Xs7haiPODEfByozUw9kxZ6O8weZC-7ult8d6FTO164WoPNrXlJV2tag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96951795cb.mp4?token=bCnhMMJ5rpG6FoY6Q8GQuW8y6WnXka1SzqFDacpU62hJC2FZUgjRh-8qdJmcwIQeH5uHdeG4giT-nZuGqOh2fzHwokmEqjMLW9z3-GBUsZmxUGZi8F22lt0qHLnKMZylY_aiDKWVHPjOKxHl7OQahNmfDkjKPlsD4S8-ElZ7bnWgLpIwn3Ij8U2FCM1CQLpvcD2Q4XsZSrYryp0i217tLqljUPuOu52K0XRCMqNXH6HpatkWnW13KJmaXwSpkryyFjYxrCy2d1tW5IBrv1avM3cFzSksUP0Xs7haiPODEfByozUw9kxZ6O8weZC-7ult8d6FTO164WoPNrXlJV2tag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر‌ی از حمله‌های ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139989" target="_blank">📅 13:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139988" target="_blank">📅 13:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsd6tscHoQADzQrBbKUbPBJrm-anWX0iu2aAz_1s5vv-w_VyJ2i0JyaDAAxMe4DFgQAatzBzxkhElZKr7mYzWi8H2QID1-o84Gr2k1_ymr_NaLr7woeRIl39HB4EeHTWVfo6XdxGYafvrd_p3IChdE8pW_6S7UEiVvAg6XCrLlN4CJa9xEted6suQiqMD8xLUi_QXgx14yyXCkwJRvtdiG0sV-PFgtscNZqPcMDrIhLLUP6J0Zb4krM6gtHa7zekxJoNtENRmD1W1JplV17Fqhjf92hjOTsnAFfZyfi6rCrp6Pp3sQRdoqfq97UHCIgOoyaqy_Qf6WGCJK2-V7YGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمدرضا خاتمی به عنوان فرمانده مرزبانی استان کردستان معرفی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139987" target="_blank">📅 13:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139986" target="_blank">📅 13:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دور جدید مذاکرات لبنان و اسرائیل در رم عصر سه‌شنبه با تمرکز بر پرونده مرزها، سازوکار راستی‌آزمایی اجرای ترتیبات امنیتی، خروج نیروهای اسرائیلی و موضوع خلع سلاح حزب‌الله پایان یافت و قرار است گفت‌وگوها روز پنج‌شنبه از سر گرفته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139985" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k51l_VOhaFnVFojbR4nMZ3Mg3oo2n-gBz5pcO857PeoB5_9CmP-7gVMpXYF8bWKSBs2LlOg712eAF0KwvNLKGqIVRoro8Uxq0hQbZUn5N6WYcb8PkGoLNWoiWokS_O_zxnKZbgr7WoWZizijoe68raaLaoZlTD4rk6VpH1VlDc66_spKNbDcr2n6QaHWBqH89DjoApmhIU3Fo-DX0O8ZlWL1-UobEMf1k4sXprumK_9IPWcSpaZH-HUai9WaTcAOV_2nf3aYax_s0CIzxIRQPxfrMQCK0RKOSzcR7on8gQaqCrZ8i4OUeQfco6o97VcvT5EfPaqjJRm22X8vWCYVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کمیسیون امنیت ملی خطاب به آمریکا: به زودی از منطقه اخراج می‌شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139984" target="_blank">📅 13:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgXhtGUFXCPraJi7zmVn1gcZgBggQZ6ZrrYRIpqsBl04B1_8xWqVN59iKtPoFBST7yrpIS7DyBpdRBytS2-xnn7LXBPfXFe0fsVfOLaH5Q-sSycg5AhLBB7OaUNdDUFCGdzLmrEGHCE1aFQRDdQ-imGpbFLeHdLBJWZ0LTzK2uIHTzdUkN4seEXnIifjuu9egl0PQeJ9QdBfyEQAXFw64gp-uS6K6sVXlK4hYDTIyTeTszr_Usy9inDFqi9zgInGCxHVqSfYGFTo5weDq9GL9yj6-9B-n9WwoSxfbjTziUMcAKGyN-Edk0rTiTTTnyUcZipw8XYoKiarkJcZ1flS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش NBC News: مسئول سیاست‌گذاری وزارت دفاع آمریکا (پنتاگون) در حال تدوین راهبرد جدید هسته‌ای آمریکا است.
🔴
در این راهبرد، استفاده احتمالی از سلاح‌های هسته‌ای تاکتیکی (برد کوتاه‌تر) در صورت وقوع یک جنگ منطقه‌ای با چین یا روسیه پررنگ‌تر خواهد شد.
🔴
این سند محرمانه است و گزینه‌های هسته‌ای در اختیار رئیس‌جمهور آمریکا را برای شرایط بحرانی مشخص می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139983" target="_blank">📅 13:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYUcubtr5l4Ib4JO5HyHUmYo3wTvh3WoBw28a1mT4gdqocokhQwQ01iDuTxuDUw-1hnpOKcuC4ToQX8K4EkV5i5pRh9eOFFT_OAETv1QndPElnuBi8b2j4L7Cxk73Z5wCi1t1Aid6VyOWaoo87vo6ZmQUfOLbF66t5cE0Ld0byyek4sMGUwiUgM7diScV3RqpGdyS5DCQkiRlHNlLQNwTzkIdPuRikIqIjRaeVI-6yrdiQlgqEAquxgk9vNDj8KyKPgwsABSSSfWwOrESi5JQ5GI6_9FWEe4OqJpJHQzGeq6_GcB2YnsGKvLXrpwdsbRBvb19vTxyHmo_lMmKknMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139982" target="_blank">📅 12:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKmHZRtJJ8doKaIFpPVBjEP1F-1cDUpdvbMW5L0onVWpTsNcy9fxNWJlw6PVtJ-fvoYUlEyTTc1UwJ4pdpDHJO3y59vmG__CI5PRdOKo3XvqXynGaWeN6hwyRp9ORRTb35maT-fvcADa-6QcQvbn7I85qRJR1Iwd3gm258c2N0IRRJiKjaOOtdOA4SNVplDG0fwBYuLCqziyzTsBjMgc36BRcRzXgCP_LbEYqjvyfcyRDJ4HuBJNccbf7qMdBnNFSYyyaNbcpSYi9EDw_tqzlx3BH_OrK3pc2SldjxcWz9aT1JLVmkH8BpXc4QsVkdveHXEy-XfuWxrArb09jjDQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139981" target="_blank">📅 12:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0e8f6822.mp4?token=rCMxOAky_h4PmUjsG09VW_d8mpv4AOtMyOuj2cBXglnqht5gTF6VslhJxDBk1kvOrOG-3TwhSzteOyO3DixeaPTOlKLERCnENl7T2UvDNIiiJ7OZ8PP3c0zeFbVEyQj8Q6KNdhQe21olDDHvswtztL8n1G9v4zwiLJ2IvxVNXeftJfXmdtsIvqucCJxKB2g8bddnD5gPe1bXWW8AVD9lnskSuoFO32JBL9v2X8utDj04PxWHy43xJxO6lCiVnyjq8ap_Dr_ReI1Fx99-GocOgZ4QCp3gPIJjtEHc2fbCMyMiB-ymHS2yBVirVwGMgqKVcEbb0iuK8tIkdjlkj0mq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0e8f6822.mp4?token=rCMxOAky_h4PmUjsG09VW_d8mpv4AOtMyOuj2cBXglnqht5gTF6VslhJxDBk1kvOrOG-3TwhSzteOyO3DixeaPTOlKLERCnENl7T2UvDNIiiJ7OZ8PP3c0zeFbVEyQj8Q6KNdhQe21olDDHvswtztL8n1G9v4zwiLJ2IvxVNXeftJfXmdtsIvqucCJxKB2g8bddnD5gPe1bXWW8AVD9lnskSuoFO32JBL9v2X8utDj04PxWHy43xJxO6lCiVnyjq8ap_Dr_ReI1Fx99-GocOgZ4QCp3gPIJjtEHc2fbCMyMiB-ymHS2yBVirVwGMgqKVcEbb0iuK8tIkdjlkj0mq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای بدون سرنشین "گرن-4" متعلق به روسیه، دو کشتی باری را در دریای سیاه غربی مورد اصابت قرار دادند.
🔴
وزارت دفاع روسیه مدعی است که این کشتی‌ها تجهیزاتی را برای ارتش اوکراین حمل می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139980" target="_blank">📅 12:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39178e72d.mp4?token=fdzKs7tROkujjojG0g9xKtLrMf-pRKYVNfQhPcVsiXzgVt6HG4M4r5joQas-TJRO0iisGapg8uyPXtqZDQBKtummuU3Gev4YqVLQ50JWjta-OmKhOSZ2pBLMjlCPhPK3hdin8c7S98EVKm5bACD_Wa3rmGSxF7B9NPOSfSmF_jehc4NBwkkxioWdLHvgVeGgmwTFyv-lw9nLA1c2zhfeGodNfmPqUoKAZ6TONHYo1Z-e5af7UzeEtKA0pLA_LHHMLhbG93dswgRvNBvuZgrtcuub0FAqlwHE1U_diUVHfOMVizoSmqDT1yHiElM5xUjoBh9cecAo0p-eFyrM8FbaNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39178e72d.mp4?token=fdzKs7tROkujjojG0g9xKtLrMf-pRKYVNfQhPcVsiXzgVt6HG4M4r5joQas-TJRO0iisGapg8uyPXtqZDQBKtummuU3Gev4YqVLQ50JWjta-OmKhOSZ2pBLMjlCPhPK3hdin8c7S98EVKm5bACD_Wa3rmGSxF7B9NPOSfSmF_jehc4NBwkkxioWdLHvgVeGgmwTFyv-lw9nLA1c2zhfeGodNfmPqUoKAZ6TONHYo1Z-e5af7UzeEtKA0pLA_LHHMLhbG93dswgRvNBvuZgrtcuub0FAqlwHE1U_diUVHfOMVizoSmqDT1yHiElM5xUjoBh9cecAo0p-eFyrM8FbaNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر تکمیلی از موشک‌های بالستیک اسکندر-ام روسیه که مجهز به مهمات خوشه‌ای هستند و شب گذشته به شهر کی‌یف، اوکراین، اصابت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139978" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139977" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روزنامه اسرائیلی جروزالم‌پست:حماس در حال انتقال واحدهای خود به ترکیه است
🔴
حماس در حال انتقال واحدهای سازمانی، فعالیت‌های مخفی و عملیات امنیت سایبری خود به ترکیه است، در حالی که قطر همچنان میزبان رهبری و فعالیت‌های عمومی این سازمان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139976" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8BmZgfgK0BRjnMtaHiQkAVEtqjLaEX-DcfJC0tBfQ9dVS0Vk2UeedVv_2QaQY9kthj-l8LM_2jFTNOwiJUkCkWnCUpz3eq95fbM4D2K9IknTMxJrBZueN5VT8xyuimnECyjevcdkTYs0dJFyK9Jp_mh-SVSrqXJEr-aVl0vwlpScjBa21P7UnVsz4KStNPQG5ka8XRnjp8JHRxE3cv6-iMayD0pkAYw7UvYO4HG_NM-qeqI9cRicf-8eyn36HOajGuBD4LnIkANRJCnuIC9d6eNwyRxlty2_FSML7DlLeqDjD5TVSGMQA0pwYkpYrsB4QIfVMqZz9Y_sK9Y2T8cFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیلد آلمان : یک پهپاد در محوطهٔ پارکینگ هواپیماهای فرودگاه Leipzig/Halle  در آلمان پیدا شده است که به آن یک جسم حجیم با یک مواد منفجره متصل بوده و بازرسان آن را به عنوان یک وسیلهٔ انفجاری احتمالی طبقه‌بندی کرده‌اند.
🔴
گزارش شده که این پهپاد درست در کنار یک هواپیمای باری اوکراینی از نوع آنتونوف قرار داشته است.
🔴
پلیس فدرال تیم‌های خنثی‌سازی بمب و یک ربات را به محل اعزام کرده و انفجار کنترل‌شده‌ای را برنامه‌ریزی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139975" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
میدونستین اسلام آباد غرب، قبلا اسمش شاه آباد غرب بوده.
🤔
هر جا رو شاه آباد کرد اینا زدن به نام اسلام
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139974" target="_blank">📅 12:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFSRVXqEb63o92cZFI850j0r7eW1AA87QJ4cuA_KO20CX62TFy06c9gW9YA5fbIVE_oo13OgOIRHvBbE9QEwEZWHMEBsCD_yDjAoQljYD-jxMa0Ex23OJmwbonSoFuCCSsweHxx6ThVdyasBbDR25E6EKiA9j-yIQfspN-S_RrG3h7VWreHUKFpDVP5Ji8jZpy7NIMH8ri-Ia6ShSBbsihoSjBjhSOd4mlEi9Uwlt-j1LbpthpO11XhArsPuFnG_T-ZiZB23sG8pwU9sOlj-I61i2I3qTKwj3xGv24yVJu2RHNpqDwKMEQuaKlHMW3pgDhNeHrGlhI7z572EOLKXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به عنوان بخشی از افزایش حضور نظامی آمریکا در خاورمیانه، هواپیماهای سوخت‌رسانی بیشتری از آمریکا وارد فرودگاه بن گوریون شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139973" target="_blank">📅 12:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز: ترامپ در جنگ با ایران در یک تحقیر استراتژیک گرفتار شده و نمی تواند بدون پرداخت هزینه سیاسی در داخل، از این جنگ خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139972" target="_blank">📅 12:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac8efc6d7.mp4?token=VZD3W4RMqHkl9gDwjI9cOcfyjJP1tR3lO3fIO2pZKqWO9uSmIdmhunafk1wqXxjUOqM0t3z_UkytCRPyfRi7SXwuuH3BhyUWQiL2AYN9-6myVRBkAIK_EZJ5E7O59myTSKFDZXao3C0MTZuyQKKKLmQZaftwi3azAH6qQGxbYbFlF4q5nMmm4L5dIKaA8c9-u-1JkscUU-mZNm1ydjZKU80quYOQs2gZ9VTV0ZBuYbD_NmkjxbiLn9SUOUX6g3cJTddjKImCDDa7QgxyvyrwFCS-DxlvRw0cIS89j4o23u6jQ_0dJ0IQC7PQ0HNgFKeUNfhGfkuTYJy1fZYVzUv9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac8efc6d7.mp4?token=VZD3W4RMqHkl9gDwjI9cOcfyjJP1tR3lO3fIO2pZKqWO9uSmIdmhunafk1wqXxjUOqM0t3z_UkytCRPyfRi7SXwuuH3BhyUWQiL2AYN9-6myVRBkAIK_EZJ5E7O59myTSKFDZXao3C0MTZuyQKKKLmQZaftwi3azAH6qQGxbYbFlF4q5nMmm4L5dIKaA8c9-u-1JkscUU-mZNm1ydjZKU80quYOQs2gZ9VTV0ZBuYbD_NmkjxbiLn9SUOUX6g3cJTddjKImCDDa7QgxyvyrwFCS-DxlvRw0cIS89j4o23u6jQ_0dJ0IQC7PQ0HNgFKeUNfhGfkuTYJy1fZYVzUv9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: با حمله سنگین موشکی مواجه شدیم
🔴
ساعاتی پس از انفجارهای مهیب در پایتخت اوکراین، ولودیمیر زلنسکی با انتشار یک فیلم خبر داد که کی‌یف هدف حمله مرگبار موشکی و پهپادی روسیه قرار گرفت.
🔴
رئیس‌جمهور اوکراین گفت: «تاکنون، گزارش شده است که ۴۴ نفر در حمله گسترده روسیه به کی‌یف و منطقه کی‌یف زخمی و ۱۷ نفر دیگر، به طرز غم‌انگیزی کشته شدند. به خانواده‌ها و عزیزان آنها تسلیت می‌گویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139971" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ درباره اقتصاد آمریکا گفت:
آن‌ها می‌گویند محبوبیت من در موضوع اقتصاد ۴۲ درصد است. من نباید ۴۲ درصد باشم. ما شاید بهترین اقتصاد در تاریخ جهان را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139970" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سازمان زمین‌شناسی آمریکا (USGS) ساعاتی پیش از وقوع زمین‌لرزه‌ای به بزرگی ۶.۳ ریشتر در سواحل جنوب فیلیپین خبر داد.
🔴
تاکنون گزارشی از تلفات جانی یا خسارات گسترده منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139969" target="_blank">📅 12:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c27e3dc6.mp4?token=G-PjFJCo7VRG9B9shFlP8Lxt7TJAb0okm6ZYbhxbxj_tos5xo6eoSoeFfyxdmLNTXVrFhTo_0b4Z8Ipca3L9-SO4RJ22lEHWzjhH4upr-cZcOWWnAHsulBAZWO_PwNRDbgEuNvHH3jXPyQgmG2KaA5v4jHaycmrAPBVFU0OrT6AhW-XjzxSPkJECCoDiXgMHBSmL8rNd0LVGXHAb_V8kHtAmPlLOzyc8PQ0opVIVdx4qrNbGiEJvMPKOCC8FDZeWG9j5rFmivSOCxI-XQPxVM9RNe70MlPJIo44vqoNb2UvsFEmgEBj3otUyr4fXU_RkYRyVCCaRv1AxGLq8VdcNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c27e3dc6.mp4?token=G-PjFJCo7VRG9B9shFlP8Lxt7TJAb0okm6ZYbhxbxj_tos5xo6eoSoeFfyxdmLNTXVrFhTo_0b4Z8Ipca3L9-SO4RJ22lEHWzjhH4upr-cZcOWWnAHsulBAZWO_PwNRDbgEuNvHH3jXPyQgmG2KaA5v4jHaycmrAPBVFU0OrT6AhW-XjzxSPkJECCoDiXgMHBSmL8rNd0LVGXHAb_V8kHtAmPlLOzyc8PQ0opVIVdx4qrNbGiEJvMPKOCC8FDZeWG9j5rFmivSOCxI-XQPxVM9RNe70MlPJIo44vqoNb2UvsFEmgEBj3otUyr4fXU_RkYRyVCCaRv1AxGLq8VdcNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : حرکت‌هایی در حال انجامه, ممکنه فردا یا پس‌فردا، یعنی چهارشنبه یا پنجشنبه، اتفاقی بیفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139968" target="_blank">📅 12:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e4a309b6.mp4?token=Jo3OHEwGPC8lDk97ex6WYerupYkq14jdKDMYKaRyq5xDWXdBoUn3gCcOvHyFdEjze4IFPwjuOV7F7l2XoSWpsNmF6D2WMEPlI_bFiUv6pYbT21plTgmfVPeiqWicNDsze8GenFizqXkPb9JCuXfX5xOyueKYAapMDhnGGkfAJWsUcJORXKE-GYcm4_R1ei_8oRublSTNnlP9VMN7M47KlWd568pg4S6t7tJ1qETCuaqMxdKR0MM27LM1VvSDVOBNCT9uMIhL5FKUR2VMndnejD4QxAbzIZMU8OFZBTKXDHeDloP8leBuyCSCbnjtfLD8d-0L1huXkVABm45VwhX1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e4a309b6.mp4?token=Jo3OHEwGPC8lDk97ex6WYerupYkq14jdKDMYKaRyq5xDWXdBoUn3gCcOvHyFdEjze4IFPwjuOV7F7l2XoSWpsNmF6D2WMEPlI_bFiUv6pYbT21plTgmfVPeiqWicNDsze8GenFizqXkPb9JCuXfX5xOyueKYAapMDhnGGkfAJWsUcJORXKE-GYcm4_R1ei_8oRublSTNnlP9VMN7M47KlWd568pg4S6t7tJ1qETCuaqMxdKR0MM27LM1VvSDVOBNCT9uMIhL5FKUR2VMndnejD4QxAbzIZMU8OFZBTKXDHeDloP8leBuyCSCbnjtfLD8d-0L1huXkVABm45VwhX1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : اوضاع چطوره؟
🔴
ترامپ : داریم خیلی خوب پیش می‌ریم، مشخص می‌شه. تا ۴۸ ساعت دیگه می‌فهمیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139967" target="_blank">📅 12:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZccqIa_-MKI-VwPNXKGZT6jUSM5i6C1sPkXhkAlnZUtlJx2uM5qdL__GEnDVW9itC_-1bk_Hz0d270r-ibmp6P0Q6lh-moZLn4W8MsjFWCOESgT_YoFMdX20ibjPut1TD5KXoO42ADngEi_uQaoW5fj8z0vm49WOg8HsjWYBIW2Zhigm0fZaF6HkC2ErEl-zuF3-n1CjGJg_pjUhbq_P3eTF_BtzdEdusZTnob14eTJIVopEbbSGojdB2ru13XG7hTcjf1Lbh6XW7Jm2PcZgVoI_pBBI4gUkdWiLJnFCitEMzPcUxYvG-vx9qU2bnsJcr-rkH-ogIOA1Gu958-Xr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای شناسایی و نظارتی E-3G ایالات متحده اوایل امروز به پرواز درآمد که احتمالاً مربوط به فعالیت‌هایی در تنگه هرمز یا یمن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139966" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
صدا سیما : توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد/در صورت ادامه تخلفات آمریکا، تنگه هرمز حتی با توافق بین ایران و عمان باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139965" target="_blank">📅 11:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سازمان امور مالیاتی کشور: بلاگرها و فعالان فضای مجازی نیز در صورت عبور درآمدشان از سقف‌های تعیین‌شده، باید مالیات پرداخت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139964" target="_blank">📅 11:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
حساب‌ شرکت ملی نفت ایران بسته شد
🔴
کسب اطلاع فارس نشان می‌هد بانک دولتی صنعت‌ومعدن حساب‌های شرکت ملی نفت را به‌خاطر بدهی بست.
🔴
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود.
🔴
اقدام این بانک در شرایطی انجام می‌شود که طبق قانون بودجه بدهی‌های شرکت ملی نفت تا پایان سال ۱۴۰۵ امهال شده و این شرکت تا آخر اسفند برای بازپرداخت بدهی‌ها مهلت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139963" target="_blank">📅 11:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NufnnCmRZfGDAa8IKRn4Av52azc6SWM0dFEdzmkcP59om3pLal0tZtzilGQV_49WwfM0P0NcjN6A2jPUW1-8eJPEy8QWjGUAIHa-AKB-_NNbv84UhO3EDAHou0FAJn9vbsFNVWCQ8Fc8Onp4mwms7LLB-aXg-dadamCpYerNi9ercNE5HUF4oTL2golE1RiHFiLoZLhTdKTtX03tovAaXE4jyUiNyjIcgUInOlONjjASSGbGfqAZXOQTAl_yDTKsFuWwZy1DzmLwp-Gstylg-YwsWvyys7--AnV85XyqgSMZNRbEU48evw-LfZ0HlXEDkt67ctGzT4oTeFswYyAv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین بار دیگر به پالایشگاه باشنف روسیه در شهر اوفا ، یکی از سه پالایشگاه واقع در این شهر ، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139962" target="_blank">📅 11:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-EiAWQttU1p6qk6WO27Knigotu6Fj8Sg-X9uMBzZrI0pDP9M4iK4iKtWVbsCbW9yoVa1tZhp4g9uGAaBxf-sTxluPua0Fx9bKGtoSNK19PaxAYu_2Kjj20LuzryKsSIurn3RMj_yYZtH-XntVtgkAWLt1aLLsHWRxSUObsjbZDVLxfbR7RQx7oVo97XsNoTwhXr161O50dp7DVe3fnr6zD85BVFF1JCj7GnnvF7TR6BSYNGU3D5tg11u_K--XXTIwaGgRttYCnGDM6zSbFVG0hERaFb7qK0IoVE2fW3fN9PYGL9bKvQhFYc5V--HhdApwZMVhndK-41WaXhlNx8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : اطلاعات نظامی اوکراین میگه، کره شمالی شروع به استقرار یه واحد موشکی تو غرب روسیه کرده
🔴
قراره تا ۱۲۰ موشک بالستیک و ۶ پرتابگر برای استفاده علیه اوکراین تحویل داده بشه
🔴
اگه این خبر تأیید بشه، نشون‌دهنده گسترش همکاری نظامی روسیه و کره شمالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139961" target="_blank">📅 11:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW3dFi5uWV6DDKZYmcjhuHBh0POtaaLwAF545xMfoG8S0XsY2AtQ6TM-cX6sDquKXnphrP9h0oounwX2xkcHwbKrjYLrRCK1Iet6uiOg-Kxj10E2FUDMFe6hdZM70I3TPJStHa9YWLpLOcOrScufVBq3L4soAp6kwVYG8aMk4R8h5DjblotWPgCEdYzX3xXvw3dapCBIgJ3OW2YwscIyQsZVg1JCgt2Ew0LGUccSv4oSZgfsU3Xxo4MS3mCe5eexuVbrABgjaLsvPgxmIHSjv3WqvumGiyrwUM16mcMH1yoMhhVFsudeY91LnzUzIrjC4ZNmheCFNTVTPYNwz3X8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر رهبر کره شمالی، پس از آزمایش موشکی ژاپن هشدار داد پیونگ یانگ «گزینه‌های نظامی بیشتری» در پیش خواهد گرفت و گفت: باید کاری کنیم که پشیمان شود.
🔴
او ارتش ژاپن را به تبدیل شدن به یک قدرت نظامی تهاجمی متهم کرد و آمریکا را پشت این اقدامات دانست.
🔴
خبرگزاری کره شمالی نیز اعلام کرد اقدامات آمریکا، ژاپن و کره جنوبی از نقطه بحرانی عبور کرده است. تحلیلگران می‌گویند پیونگ یانگ به دنبال توجیه توسعه تسلیحات خود با نمایش ژاپن به عنوان تهدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139960" target="_blank">📅 11:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رویترز : آمریکا همچنان داره با اوکراین مذاکره می‌کنه
🔴
تا اجازه تولید موشک‌های رهگیر پاتریوت یا قطعاتش رو بگیره
🔴
یکی از طرح‌ها اینه که قطعات تو اوکراین ساخته و مونتاژ نهایی تو آلمان انجام بشه
🔴
اما تحویل اولین موشک‌ها حداقل یک سال زمان می‌بره
🔴
و اوکراین تا اون موقع همچنان به کمک‌های تسلیحاتی متحدانش وابسته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139959" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز ممکن است امروز یا فردا، باز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139958" target="_blank">📅 11:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT62Tcg4yxTKz6lz7IRQh1X29NNxG2CDW-IAKeODGjov2Ry4vMO28tVPIqAGZDg8BiwztigMyiSjIAo9xoT1dTSUWzW78AsXsPH9_F4Tc3DFdmAAbrkNzJ_-qfPVN8CsWKqvacfkfBTFyLa7tDzB17SqzttFL8scJWtlI8249x8sXBnbYqc4Qs9EoujuWuWnb7LitJ4gnKPoQw77NQxodOtWjjM4vh4Q7sdi3_6DxYVgvitnN0GGiKYOPPr8_javtxLQI01F6-4-2eQzEliX1KCrFn4YLqEzMIthdaPZP9PxULcbeyS4L0XxirBZx-fqEDWpCuQAMzwvsN2dCFZdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
در تروث سوشال
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139957" target="_blank">📅 11:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d9b3137.mp4?token=H5GwzVaKDjsxciF5tOL4fBYPHGNYaAAa_rcVWVkrv5TETprxSUAekwtEWuO-7IeLhCwiUvR_7JVp2_COWwcuToho8MHgUWp6XELkxRBguR2q3en5Ht06qVDsezxTPEJVIt7BDx2Xqa7B8ZblYdl2yjJTa9cRIuNmeWKlyDS9QfDODvA1g29weYUpauoWhoSeAvvzBJDVln_ATynf0Da1KLtJZ9eMe9SF4NKs_zeasAxawGjmrFyX1mYV-Swd0q4rT9JZrAlVYlZty2xszfwOrKdBpLQv57_WohRnLhyV1B6FFNOPyOaxjAqSjaNB6o0t2WeJTyqUsVy-0k8dYkCUuBmQdfD55I_hyMQmVB_TPtmxw0SURwMD1Wf3dwYT3oJEyhk7ef_4Vgme3L2mCZi55cs-NvZuC7B1McwcwgdB8A57GQHPZSLqOLY7U_G_yuLqqanWnDTJ2zLQra9kpUZVE6TnxFhJDUwjpIfZcwekVooiLn97fxWgqTRzp0KFAzVEM98_8iJ0kXIsbqVBqxXu-ZqemTz25tzbQRlJoS4vyNReJupTPld8UNqk9QkQmRUQ9eM37SZj9NihYhkiO9mBQjji7GeDdE8idZeB6kXwq_wuEApuxDnfedhp-iDTTcsD8ty-VggJZ1RG6ve66Csf8Z77lMFX04k7Cwv4duTAX7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d9b3137.mp4?token=H5GwzVaKDjsxciF5tOL4fBYPHGNYaAAa_rcVWVkrv5TETprxSUAekwtEWuO-7IeLhCwiUvR_7JVp2_COWwcuToho8MHgUWp6XELkxRBguR2q3en5Ht06qVDsezxTPEJVIt7BDx2Xqa7B8ZblYdl2yjJTa9cRIuNmeWKlyDS9QfDODvA1g29weYUpauoWhoSeAvvzBJDVln_ATynf0Da1KLtJZ9eMe9SF4NKs_zeasAxawGjmrFyX1mYV-Swd0q4rT9JZrAlVYlZty2xszfwOrKdBpLQv57_WohRnLhyV1B6FFNOPyOaxjAqSjaNB6o0t2WeJTyqUsVy-0k8dYkCUuBmQdfD55I_hyMQmVB_TPtmxw0SURwMD1Wf3dwYT3oJEyhk7ef_4Vgme3L2mCZi55cs-NvZuC7B1McwcwgdB8A57GQHPZSLqOLY7U_G_yuLqqanWnDTJ2zLQra9kpUZVE6TnxFhJDUwjpIfZcwekVooiLn97fxWgqTRzp0KFAzVEM98_8iJ0kXIsbqVBqxXu-ZqemTz25tzbQRlJoS4vyNReJupTPld8UNqk9QkQmRUQ9eM37SZj9NihYhkiO9mBQjji7GeDdE8idZeB6kXwq_wuEApuxDnfedhp-iDTTcsD8ty-VggJZ1RG6ve66Csf8Z77lMFX04k7Cwv4duTAX7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بگومگوی مجری صداوسیما با ناصر هادیان بر سر مدیریت تنگه هرمز
🔴
مجری صداوسیما: ولو همه دنیا علیه ایران بسیج شود! چیزی نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139956" target="_blank">📅 11:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آتش‌سوزی در جزیره آشوراده با حضور نیروهای امدادی و عملیات هوایی بالگرد هلال‌احمر گلستان مهار شد.
🔴
در این عملیات، بالگرد هلال‌احمر طی چهار مرحله پرواز عملیاتی و ۱۰ مرحله آبگیری، ۴۰ هزار لیتر آب را بر کانون‌های آتش تخلیه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139955" target="_blank">📅 11:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH8qMNc5dL44_EYo8nN27y89YXKR5iAejSyoxOe3wK3goB2xJfF88qSoBamdAe7UkZLYBENXCLvI1pi2jfkHnmTpeoBC6nh-WX8IaWmCcYT7bMnC1dIR4fOVhuXW7fHLtdPJ9WsWAnAPYgqVg7MIbMmo0aEGwmLOBQKSxt7bap2Dd4GbrJcfl0AuXb6Xso76qxFtY5dMSW2XdxfaZFJuVQqJFJan6h93yupmMATong1ou6kTB5GCmrJzW5RnVuAH-nwv7gloJLRWAwek4xeGkK8UpZKk1j9HewcCyQnX338QwGYea9CeJW4GS-nJpsdrCW_2PY6F76AZGKG11fNclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رسانه‌های پاکستانی، نخست‌وزیر این کشور شهباز شریف برای انجام گفت‌وگوهای سطح‌بالا با مقام‌های ارشد سعودی، این هفته در سفری دو روزه، راهی عربستان می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139954" target="_blank">📅 10:57 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
