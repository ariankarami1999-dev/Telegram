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
<img src="https://cdn4.telesco.pe/file/JxUApXNeeRg8RmR05A0xdd413RzMzWIvjQUqjwUk6RHHxqMQ5vop5KmTCR4bKbJwkKeJfMoqE0k9w5J42OtVV9UiNe5FaHN0J3_Wlmkm3YhMffyyD0p-6mRyjnWBygf9S_Rfhx26QsbSQbhI7q8AjxA2JG_xTJOhvygzd08k5nMbxJ9gm3Vf8wTEXGlo8wtnl68_f07G0Ona7ND5x5DX8j2RWxCcj4ubY-FVRv7SIge40kEPd5I0sza8d1b9k6mb1Ze_wmmV5jm8sJG1KXWckGUsGzyiye91cY7z6mCtWgooZ-HR9DtzkDE5X-85aJQlqFwGDfkNc6-xl5uuMd8I4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند. @WarRoom</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/24222" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وال‌استریت‌ژورنال : ترامپ قصد ندارد محاصره دریایی بنادر ایران را لغو کند؛ واشنگتن امیدوار است فشار اقتصادی، تهران را به پذیرش شروط آمریکا(تسلیم) وادار کند.
@WarRoom</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/withyashar/24221" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کوین‌دسک ,
رشد برخی آلت‌کوین‌ها
: در گزارش بازار روز جمعه، کوانتوم (QNT) حدود
۳۸
درصد، اوندو (ONDO) حدود
۲۸
درصد و چین‌لینک (LINK) حدود
۱۱
درصد رشد روزانه ثبت کرده بودند. این ارقام قیمت لحظه‌ای امروز نیستند
@WarRoom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/24220" target="_blank">📅 11:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روزنامه گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
@WarRoom</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/withyashar/24219" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏سیدمحمد مرندی، مشاور پیشین تیم مذاکرات هسته‌ای رژیم جمهوری اسلامی، مدعی شد مذاکرات غیرمستقیم با دولت ترامپ بدون پیشرفت بوده و منطقه به سوی تشدید تنش می‌رود. او همچنین کشورهای حاشیه خلیج فارس را به همراهی با آمریکا در جنگ علیه ایران متهم کرد و اقدامات ترامپ و اسکات بسنت را «توطئه علیه مردم ایران» خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/24218" target="_blank">📅 11:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز ، عربستان، ترکیه و پاکستان هماهنگی امنیتی را افزایش دادند: مقام‌های دفاعی سه کشور در ریاض درباره وضعیت امنیتی منطقه، تبادل اطلاعات، هماهنگی نظامی و یکپارچه‌سازی نیروها گفت‌وگو کردند. این نشست در چارچوب توافق دفاعی مشترک مکه برگزار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/24217" target="_blank">📅 11:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">«یک مقام ارشد اطلاعاتی اسرائیل، در توصیف میزان ویرانی رفح در سال ۲۰۲۶، گفته است: تقریباً هیچ ساختمانی در رفح باقی نمانده، مگر ساختمان‌هایی که تصمیم گرفته شده بود حفظ شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/24216" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=TNX4lFiRVRYol0UXRgWMNY-dXCN9gnihGBo6MOaAhs3-Z14VEqMDI7JmipkMfvnTUPEKIDHHoyzDyTjZ_zmRFaD3oBaen17WLLeV_eNqJmAJy47WYYf2Mm8CH2fdnQ1mTaozstSeXjXMmixvcaaod-W1pstOfUAPjmZ8PnUitTcwR56Fx8skJW8KwO-0So91Uza6yCA_JqMq7tXDT_zN0OSinmVIalKWnpBXPUlsNCoV3LgRBPNm4bOe_jTXRTvzsIm3hOTfsgiu7SXL4RTXHpaD-Do_eMTvg6RmLPaG6SzXd92RE_atEGH58Xl6OUoQ-GRicDf4VjDIsEOkI_f-YKh-jBJ57SXyeggveXmL9BxziF8U-cTgDj95dHJgV73Zq9Q2KQThPWZEM-pmEan6pIqy-nNYP0tsiGyl1quaEeOs6LdwE83p81MejFJs8OJn4bhypV2e7cIUok89TdOJe5bdFXv3JC4_e7eAEItHcvF4K1B9h_4hxoxTmbCZNqHwMM71LUjYuYKR7yaHOcSDuz41_6XY4VOFVYb2hr87grIQjkttjtY8yO9L1ZApV8dxCi-DJVkqTNNCvMeySIC14bzj-yn2mVr_MhEArlaPr-SnYw7V0yiG4RuYnbN3zgmVv-d2iJZkHIj7hYieZA6kXHa1XekKxLhASaYlY-uneBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a2522c0a.mp4?token=TNX4lFiRVRYol0UXRgWMNY-dXCN9gnihGBo6MOaAhs3-Z14VEqMDI7JmipkMfvnTUPEKIDHHoyzDyTjZ_zmRFaD3oBaen17WLLeV_eNqJmAJy47WYYf2Mm8CH2fdnQ1mTaozstSeXjXMmixvcaaod-W1pstOfUAPjmZ8PnUitTcwR56Fx8skJW8KwO-0So91Uza6yCA_JqMq7tXDT_zN0OSinmVIalKWnpBXPUlsNCoV3LgRBPNm4bOe_jTXRTvzsIm3hOTfsgiu7SXL4RTXHpaD-Do_eMTvg6RmLPaG6SzXd92RE_atEGH58Xl6OUoQ-GRicDf4VjDIsEOkI_f-YKh-jBJ57SXyeggveXmL9BxziF8U-cTgDj95dHJgV73Zq9Q2KQThPWZEM-pmEan6pIqy-nNYP0tsiGyl1quaEeOs6LdwE83p81MejFJs8OJn4bhypV2e7cIUok89TdOJe5bdFXv3JC4_e7eAEItHcvF4K1B9h_4hxoxTmbCZNqHwMM71LUjYuYKR7yaHOcSDuz41_6XY4VOFVYb2hr87grIQjkttjtY8yO9L1ZApV8dxCi-DJVkqTNNCvMeySIC14bzj-yn2mVr_MhEArlaPr-SnYw7V0yiG4RuYnbN3zgmVv-d2iJZkHIj7hYieZA6kXHa1XekKxLhASaYlY-uneBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در شبکه CBS: اسرائیل هر کسی رو که دلش بخواد با تواناییی که داره ترور می‌کنه، با پشتیبانی آمریکا. رهبر ما مگه تروریست بود که کشتنش. خیلی راحت میان ترور می‌کنن و بعد به دنیا می‌گویند ما با تروریست‌ها می‌جنگیم.
@WarRoom</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/withyashar/24215" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c51e273e7.mp4?token=PGkvvdfmSuKd6TKAeV5ilY0XcVhjhDqdQiqpiYGtQYxT0oi-_0FfqvMd1f0tUKazjE6FM-lMqXqc5FFrUwiRCdU1XRS7Ik0tmpUlU6vh3YiI4XcXOWQLhbKcX4uz0Fibm-DECqKi23I7mHmFdN22w1FguTXxoFn9b-A6Cr1fGdEgL9zu7dPFAihLulcnKni4C8538LCBlSrwmJySIeiZahppIwaDBDOEOaR5OljrLwHnZCcF2a7GchG6mpUjqYOcJ1NK6zO9THKSAM7G9Vje5XIJZwmdUgQzLgI-HY6kkxnqdcIalCQ8rNXIfYxC9yEvkJAKW6RDIzVe0eqycbtBpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضجه های حقیرانه پزشکیان در شبکه سی‌بی‌اس: آنها دنبال این هستند جامون رو پیدا کنند و هر وقت دلشون خواست بکشنمون ما گفتگو می‌کردیم که آنها ترورها را آغاز کرده‌اند. هیچ ضمانتی وجود ندارد که دوباره آمریکا و اسرائیل دست از ترورها بردارند.
@WarRoom</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/withyashar/24214" target="_blank">📅 11:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873be0f119.mp4?token=JX_Jn9knalLfO9VCdSv33pbWcknpKTtr7w7D4hxScEbHPn5f9vRSyhtunWqW9vD9woChA6l5E_14nYMIhnsNKtPNGqB8_rz1tGhcx2Kro7ZCMcms8K6QNWjDX1V4nEnN0EnqGrF3lk_aSlI_kAHt3-Ppq4nYt1WeNS0Hu7828X9KZqeOdKt2o9vtNrD2pVUFU2KwhMOG9xkGYPJVQlyZ--HeuceUR6ANh09FlvssdXALqx5qCv04mnuxM3gNCmiYZaKQDfEUNCS_02jduZgZC89pvdHgLBx4vAyvwxbonReSpZJePuM5xfa2YBaLpvX57QsHSq3iiEg6aiyHtWFTKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873be0f119.mp4?token=JX_Jn9knalLfO9VCdSv33pbWcknpKTtr7w7D4hxScEbHPn5f9vRSyhtunWqW9vD9woChA6l5E_14nYMIhnsNKtPNGqB8_rz1tGhcx2Kro7ZCMcms8K6QNWjDX1V4nEnN0EnqGrF3lk_aSlI_kAHt3-Ppq4nYt1WeNS0Hu7828X9KZqeOdKt2o9vtNrD2pVUFU2KwhMOG9xkGYPJVQlyZ--HeuceUR6ANh09FlvssdXALqx5qCv04mnuxM3gNCmiYZaKQDfEUNCS_02jduZgZC89pvdHgLBx4vAyvwxbonReSpZJePuM5xfa2YBaLpvX57QsHSq3iiEg6aiyHtWFTKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس: «اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران هم به آن پایبند خواهند بود؟»
مسعود پزشکیان: «طبیعتا هر تعهدی که بپذیریم، پایبند خواهیم بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/withyashar/24213" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0590db4d.mp4?token=JiLLUm-FNFBzWH5LWXktDCu7TP5KGCNVGco4xjRQy65aNu4Ppyo5eVlpF1L6EcRhqWhyXGfsJwmLoTbW4uTxE25k3WxFXmSCBm-Hi2W96azRsWg7hSJCm5jMHXCBZgnc8aU3AbEuQsyT9YJGcHqfy0K6lbBO8_fPO664nBB5M9g5dN8njccZzIAdBhZFF_lFXwCrwHXLXcG5ROnSiuo0f94PJcsmg7GwDi-Bv8Z9rBM37wzrbenhnBScixToYgxnvXVH9G6NKEfn72F8iDu0i71kMSZ4JjTDFV2wW5oWu05RdA4N5iPiUfidEC0po8ZOmz2zmAgsTQprcwPlT-JTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/withyashar/24212" target="_blank">📅 10:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d94d064.mp4?token=tFpHTfPX3WBJLC7jTE_fNGcJYIuT22i7PTRma6hyqvm08Wg5bFWbXcfuNb43HkPNA0oJFFzj9RzfP-_9pqJItBaxVgXagIGxELhAymx2rJWmNHfh3OHrycc3YQpTYV4wXkknT62HZVY9-Beo59LLViF1inA7OXEKsWgw9SJoU7LxdO3c4MGnbvbYxm3gv_JgL7X87DJZdCFZJdO4_AAH62vCkEcz08hXv9AtZQXMP8rwlgNgxZ_FdpdJBWjQ5QCs827w7GUhHm14POZeezTq9NOZuwReo8THm9mOXpy4Nz3WZMglvBGC_Yihjq-P4tTiQ4MmAASBo_T2VxHZSwwhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید امیدبخش ترامپ در تروث شامل صحنه‌ای از منهدم کردن لانچر رژیم جمهوری اسلامی
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/24211" target="_blank">📅 05:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود ۲۰۰ جنگنده در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود ۵۰۰ هدف را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از ۱۰۰۰ هدف را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا…</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/24208" target="_blank">📅 05:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری ABC : در شروع عملیات، اسرائیل اعلام کرد حدود
۲۰۰ جنگنده
در بزرگ‌ترین مأموریت پروازی تاریخ نیروی هوایی اسرائیل شرکت کردند و حدود
۵۰۰ هدف
را زدند.  آمریکا در نخستین ۲۴ ساعت بیش از
۱۰۰۰ هدف
را در عملیات چندمحوره مورد حمله قرار داد. طبق آمار بعدی، تا ۲۳ مارس بیش از
۱۰ هزار پرواز رزمی
و بیش از
۱۰ هزار هدف
در عملیات ثبت شده بود. گزارش سپتامبر Air & Space Forces Magazine می‌گوید Epic Fury در مجموع به
بیش از ۱۳ هزار هدف
حمله کرد و حدود
۱۰ هزار سورتی رزمی
در ۳۸ روز اوج عملیات انجام شد. همان منبع آن را
بزرگ‌ترین کارزار هوایی آمریکا در یک نسل
توصیف می‌کند. خود CENTCOM در ابتدای عملیات آن را
بزرگ‌ترین تمرکز منطقه‌ای قدرت آتش آمریکا در یک نسل
نامید.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24207" target="_blank">📅 04:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۱۵ روز قبل از شروع جنگ ۴۰ روزه ۰۲/۱۳/۲۰۲۶</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/24206" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9961f001.mp4?token=k1LsUyZQht_VcaZXlAYBDXt5o0M8mX9LuWbXzmxaom2mTTyKXs28VeRpPhvQeHYC0ifHFSgDWamKE39MMnylipmjd3kFbxO8h1RgCq56f1azHe3OAQKm2uQZLnI27wJowAodcjmn-JR58vRxSSF-t2iQPdD3_ILkFKKBZCMMacywq7uPWH2YmB-zA_Ja_OSkTOuxHzXU94Jk6qrYNciwktgVJrBFBzMvfte7bFYRPNXTSsN3byWPnmWhD_QOzq6IFuzNIgfAvbyBRzE3DlKFIDUvEdUncqpIUksBnXeRLKqAMgy1C2Qyes_hFhNonUrbPMicCzBAqrTE7g7NinGK_wQE8xRy42nUH0yW7MxHecbF-HeHnYqa_vHdotBXHSSSYZlo5uwKS2L_9_pf4q4ZpNoRE-EDKZD4rkeYsYAxeFEEy6AYrihVLO4O6CHEDgDWpVuvi7qd7cN3T0BTmI6ee5VB_qkHUN6sEzzL4T2e6cpV5Goyu2aVJ7M4K6VN5-A_4KRMVMfOTkflusos_ZcDj2OYbQ-75ggZpcffVFkepZnxbGy5ZW5oo1OOhWDx8kNdGszGET5yEqZbPZ3S3lyPQ7XQbI-Gw8-XtigWAmWKwvyBxZAj6oMlv6F1DAyC029QCPhhMC1M7qPN0otbHa6p2Di7-GCD0XyBo3YUteZgEgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/24205" target="_blank">📅 04:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/24203" target="_blank">📅 04:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/24202" target="_blank">📅 04:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24201">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383cae6fd9.mp4?token=pJedq7bFgNZ8plMdtFMi2_gn5jPuzZCymw0ZrC5LEJAVG3IIQtERudS9nuLqf5bDMbtpDEebNaBndGNJmXAna-ogBYs6OIUX0SnHzZ2lXHzzKNLy8Yp4ViTaenxLWN9BdIVAy5yhkCSMPY9T_sLKkKp0g14XD2ROjM1-JPHFN1jR_Deww2XPZM9_NbI3vwuvbeBk6zZBZmM0ik-2L3DJuddG4ub6mOfXEqdWVR8HNIfzvEmJLRlom8AxaIEHoiMHgosmh6oYsHpk0eFpNB38DzalnbVNeo-G5JJKVGsni9FkoYbXRv-2uiSH8CuV-M6kunLtKsKr41owuAkcaiPhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏هم اکنون مایک والتز ⁦سفیر آمریکا در سازمان ملل : رژیم تروریست جمهوری اسلامی باید از بین برود
@WarRoom</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/24201" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/24200" target="_blank">📅 04:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واشنگتن‌پست: پنتاگون ۳۷ نظامی مجروح دیگر را به آمار جنگ ایران اضافه کرد؛ مجموع به ۸۶۱ نفر رسید.
پنتاگون این هفته بدون توضیح عمومی، ۲۹ ملوان نیروی دریایی و ۸ تفنگدار دریایی را به آمار مجروحان اضافه کرده است. زمان و نحوه مجروح‌شدن این افراد اعلام نشده و یک مقام نیروی دریایی گفته ملوانان به خدمت بازگشته‌اند. مقام‌های دفاعی پیش‌تر گفته بودند ثبت آمار تلفات ممکن است با تأخیر انجام شود، از جمله در موارد ضربه مغزی و آسیب‌های مغزی که علائم آن‌ها دیرتر بروز می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/24199" target="_blank">📅 04:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/24198" target="_blank">📅 04:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/24197" target="_blank">📅 04:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/24196" target="_blank">📅 04:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdZL7kHrt2ZjIsD73vvNHwMbvQF5x1IzxezkY3olgMVqM_jqu6CkW9f2QaUIYaKTVZELYX1pVpuup8Zk7_9QR8wOyNTclcdSsYeyLw6QM_rhHXaJ8Xn7Wmvb4RwOFWNxSuNg-PfyYHpTRRACzi9W62ivg6eDMpbUEGCxs9IK8pcJ3EQ0qOtf-rQ6sjjlQDlTor-XQEZn-TbCUq2IIytPso-gNfBKEsxyvPtSJDLAjxumOvs8oC3LqhPOAC0rNHFurlzGNKb59kvmNrQijEK30X99wBQlQ5M-mLD_jh_wyjsQ6GdwPEQReWy-zZvLpPKaeqf9zLh9NGHy_l2xaOybVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ پیشنهاد آتش‌بس ایران را رد کرده و از احتمال تشدید بمباران‌ها پس از انتخابات میان‌دوره‌ای آمریکا خبر داد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/24195" target="_blank">📅 04:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/24194" target="_blank">📅 03:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/24193" target="_blank">📅 03:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/24192" target="_blank">📅 03:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/24191" target="_blank">📅 03:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=c94lCXH2ik4Rrqfgj2wUdSq7kho7y4riLtGzhnSgK7lBhwdxnUK9nKx43q6uPglmRblGS8DBkbY4EnLxtR9SYabWL48suQkHMPw751CgKjM3l78TcsO4YydjGHLd2ly_chBMYpJpYZIClAjYyAssrtmGFzLQfsG8B_Y-wtOasFdxXwk3_L-mZYzx3a10eJtXBvHysQ5PEyBd1cXS02Q0ag3fExB3UGgf9uflrfWItdk-QxMqxYmvk_ZbBhVCIGLHlOvK9I7NewfZy2fj5rLk2Gu_B9WD_zNpYqy0je6h40BEsZqhuzEz-b5_7qIlZmXeqWBe1uptrN63RGwnLC95tjxVQ207oky_LygbrJdPf9l_3xooBFvdObPMRmvcYdFw3Z9YMgCSwK86qTzAi1aRxQBMNMyEemkf0medcFXwcGPExH66Fl0dTrnP91BBeZ_m1OvuLXeyrzIcm-UVAif3DQ3Fd4Z5fTf-GZ0xsjSMs7BT4oG2dnFKGx5B_EN_0qwdCFOSCfHBGwJbY_T3c3Bh8qwh9t9yLqgKabeO9E37ZEyL21tv-KqGpwHt2PJxCg8PUv1kgmLRzWY1N7RBguoZFq7msJcVmISvUFfSVMS7wpWKQNm8NuMwhRaiKG3nLNqTIUrR6Zm6CjaZKo9ycIdyoe755kHBIJUdpasFQEbX6Ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d80d824a.mp4?token=c94lCXH2ik4Rrqfgj2wUdSq7kho7y4riLtGzhnSgK7lBhwdxnUK9nKx43q6uPglmRblGS8DBkbY4EnLxtR9SYabWL48suQkHMPw751CgKjM3l78TcsO4YydjGHLd2ly_chBMYpJpYZIClAjYyAssrtmGFzLQfsG8B_Y-wtOasFdxXwk3_L-mZYzx3a10eJtXBvHysQ5PEyBd1cXS02Q0ag3fExB3UGgf9uflrfWItdk-QxMqxYmvk_ZbBhVCIGLHlOvK9I7NewfZy2fj5rLk2Gu_B9WD_zNpYqy0je6h40BEsZqhuzEz-b5_7qIlZmXeqWBe1uptrN63RGwnLC95tjxVQ207oky_LygbrJdPf9l_3xooBFvdObPMRmvcYdFw3Z9YMgCSwK86qTzAi1aRxQBMNMyEemkf0medcFXwcGPExH66Fl0dTrnP91BBeZ_m1OvuLXeyrzIcm-UVAif3DQ3Fd4Z5fTf-GZ0xsjSMs7BT4oG2dnFKGx5B_EN_0qwdCFOSCfHBGwJbY_T3c3Bh8qwh9t9yLqgKabeO9E37ZEyL21tv-KqGpwHt2PJxCg8PUv1kgmLRzWY1N7RBguoZFq7msJcVmISvUFfSVMS7wpWKQNm8NuMwhRaiKG3nLNqTIUrR6Zm6CjaZKo9ycIdyoe755kHBIJUdpasFQEbX6Ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از مهمانان ضیافت شام دفتر نمایندگی مفت خورهای جمهوری اسلامی در نیویورک تحت عنوان «دیدار با ایرانیان فرهیخته و مقیم ایالات متحده آمریکا»
@WarRoom</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/24190" target="_blank">📅 03:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24189">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX4cik0V7_m7hcPjBnd0zFdIVtcCOIp5b02ns4UhcAnk1l7AoBc2Af7cgZzzfxXBGa8aZHKxKKIsfWm7Qd2THDWt8T0EdPE2Ox15hE03VpL-VuR_1jSx4vRzvQVMipM2PFvbbXT6ExOa0tBAf5yUFvuCvwfd5Rbjv3ny-g3VKO-Wo9A0t22yzkeTX2EeR5GlyBPVWJwOj9FBaxvUEAdqWPKadsXQNVYSnLoi7O4UQR107JSjBkqhXiwsXx2l6wb4MJbFxnNxoYK_Nc46Vrcr7J070tUlBw9Rs8d80Q3beOVfzVfeWTCBqWW1ePNoh5RNvQhfRrQFbo4vUcD9cRjrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ریخت و وارد کانال ۹۷$ شد
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/24189" target="_blank">📅 03:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/24188" target="_blank">📅 03:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/24187" target="_blank">📅 03:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/24186" target="_blank">📅 03:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش صدای انفجار شدید از‌ تنگه ، پیغام های زیاد از بندر و قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/24185" target="_blank">📅 02:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش انفجار شدید / شاید شایذ پرتاب از مرکز شهر تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24184" target="_blank">📅 02:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من قدم ۱۹۱ هست
😂
عکس‌ ها رو هم عزیزان دلم درست میکنند
😼</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/24183" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🩵</strong></div>
<div class="tg-text">با قد ۱۶۰سانت واسمون کماندو شدی</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/24182" target="_blank">📅 02:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کمیسیون بورس و اوراق بهادار آمریکا (SEC) توضیحات جدیدی درباره قوانین کریپتو منتشر کرد!
طبق این توضیحات، بازخرید توکن توسط یک پروژه لزوماً باعث نمی‌شود آن توکن اوراق بهادار محسوب شود. همچنین توکن‌هایی که کاربران در ازای استیک کردن دارایی‌هایشان دریافت می‌کنند نیز در برخی شرایط اوراق بهادار محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24181" target="_blank">📅 01:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عراقچی هم اکنون : سیا توبه توبه سیا نرمه نرمه
البته CIA
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/24180" target="_blank">📅 01:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlGzbtiQjURRJ0QlLpjU8mxGKDU57y_43F2FZnrKbgA1loY_cY2QP7c_WsFb0posAr3XQUrjbGPX8BXxkIX8HiRcSynbwlnMVl3cYUlfmEQkW1VCee7g-CrGVDppwRKMK9vFQsE2m6Gs6iAIPK-gAIdIFm1B6lVYbXBUssZ4oo_hBw1gbGCS1-pPy9qRjOLcG-zpRo9U_i0ncLbWMrcHSHEdOJEJFU3t4J0hY6Y4szkFuWHljAPgV4o8szMyiKZWzR_Qu60ZX9NCzlDU961UWvDFp1B-rGhIbUakl6pNx2lfHKdUJv9K-l0qQjE1euB5bIDQR2NV8WBHnSJvi2OE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوخترسان جدید الان از قطر بلند شدن در‌ مجموع ۵ سوخترسان همگی ‌از قطر و ۱ پی ۸ از بحرین از که از ۸ ساعت پیش در حال انجام ماموریت بر فراز خلیج فارس و تنگه هرمز هستند
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/24179" target="_blank">📅 01:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خانعلی‌زاده : دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24178" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromادمین</strong></div>
<div class="tg-text">یاشار. داداش من الان رسیدم پیام هات رو دارم یکی یکی نگاه میکنم من و خانومم خیلی وقته اینتر آشغال رو نگاه نمی‌کنیم کلا پاک کردیم خیلی روحیه مون خوب شده من که فقط کانال تو رو دنبال میکنم ،دهنت سرویس چقدر تو کانالت خندیدم،بزار اعتراف کنم اولین کانالی هستی هم اطلاع رسانی هم تربیت هم فرهنگ سازی هم مبارزه طلبی و هم خنده و روحیه خوب داری به مردم یاد میدی در کل عشقی داداش</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24177" target="_blank">📅 01:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L50LwyyecxVZ8rMVp654LTLWH9jtsLjwM5w6iCetHVG3lxFzlc3kz9zRMKjyfGy4cfzhtLhcCK1dsczNHAFee79bxIPHrcYhK0uK9YQ0t3GO2OXD5ux3cft_zPsqqCxSQOIikXmdyqNe0VD-QxgNO8VpZa2Ybhl2U4pVFkpc2YMnGYPaXbR4n20iAHonebo2PIEuoluDomT-ukXpRJ8JZQXfEzrBjVV6JoKXrPzjrepO9WSiX2qvTGxaI0fEjaWPfs7C18gTMq61XUwXMvz8u6t9HCg3yz9uruFvE-5Q6oEiXEl4H6aZi7hhL3XajH9rQLBhJNPNssNN_DiilkQ-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : ایران آزاد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/24176" target="_blank">📅 01:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عراقچی: ما از طریق قطر، این پیام را به آمریکا را منتقل کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/24175" target="_blank">📅 00:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امشب دیرتر‌ میرم بالا منبر</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24174" target="_blank">📅 00:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدای ریکشنا نمیادااا اهااااا بیا وسطط</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24173" target="_blank">📅 00:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پرتاب ۴ موشک از سیریک با صدای کشته شده های حکومتی‌که راننده مست زد پرتشون کرد اونور بلوار
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24172" target="_blank">📅 00:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24171" target="_blank">📅 00:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل گفت اسرائیل هم خواهان تغییر حکومت در ایران است و هم به تحقق آن امید دارد. او افزود این موضوع هدف رسمی عملیات نظامی اسرائیل نیست، اما به گفته او، تحقق چنین تغییری به سود مردم ایران و کل منطقه خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24170" target="_blank">📅 00:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی در نشست خبری نیویورک:
اگر شرایط فراهم بشه و فضا از فشار و تهدید دور باشه، تنگه هرمز ظرف ۷ روز باز می‌شه و امنیت کشتیرانی هم تضمین خواهد شد.
این مهلت ۷ روزه از زمانی شروع می‌شه که آمریکا طرح پیشنهادی جمهوری اسلامی رو بپذیره؛ الان توپ در زمین آمریکاست.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24169" target="_blank">📅 00:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام: رزمایش «شیر آماده ۲۰۲۶» در آمریکا به پایان رسید.
این رزمایش دو هفته‌ای روز ۲۴ سپتامبر در پایگاه فورت کارسون ایالت کلرادو به پایان رسید و بیش از
۲۰۰ نیروی نظامی آمریکایی و اردنی
در آن شرکت داشتند. این نخستین‌بار بود که رزمایش «شیر آماده» در خاک آمریکا برگزار می‌شد و آموزش‌ها بر
عملیات ستاد فرماندهی مشترک، دفاع سایبری، واکنش به بلایای طبیعی و افزایش هماهنگی عملیاتی
میان نیروهای دو کشور متمرکز بود. این رزمایش دوازدهمین دوره «شیر آماده» و بخشی از همکاری دفاعی بیش از
۲۲ ساله آمریکا و اردن
محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24168" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلامتی همگی
😂</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24167" target="_blank">📅 23:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مستند «پیجینگ حزب‌الله» درباره پشت‌پرده عملیات انفجار پیجرها و بی‌سیم‌های حزب‌الله در سپتامبر ۲۰۲۴ ساخته شده است. در این مستند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیوید بارنیا، رئیس پیشین موساد، دیوید پترائوس، رئیس پیشین سازمان سیا
و چند مقام و چهره اطلاعاتی اسرائیلی و آمریکایی حضور دارند. این مستند به کارگردانی جاستین فولک ساخته شده و قرار است
۳۰ اکتبر ۲۰۲۶، برابر با ۸ آبان ۱۴۰۵
در آمریکا اکران شود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24166" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwO2fK2GVGhEIA0FF3N34ror7VzS8jtR8IiNURySvkJpMdgb98f9qHgLYDUImRLQRAWTGFzP6VGPykIbiwu_tz_YLpBKKviWJ9o9YGqFwKkzftziSH-FcbEfkUNC19tG_c_DQshdlSL6sNVJ2U6FyXNVK2RPDAeBC8e6Ne68ir27heOV-LUacsVSIJrFqTSguDnjax1hY6Av12SfJKDzN0CpuOM-eJdx2UHu2ujI6aYpBN05S2eQA3k5odSfgp4jDzIF9E-zhQ-7L1LB7tHAV8MyeD53GI0WLJ0r3No6GYnTSJ3W3VlgS8XfzKoi1JgbaPZ1Bu4JSCLRoGYoL0V5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت برنان
(مجری و خبرنگار سیاسی شبکه CBS آمریکا)
: رئیس‌جمهور ایران، مسعود پزشکیان، در گفت‌وگویی با ما درباره وضعیت
دیپلماسی با آمریکا برای بازگشایی تنگه هرمز، برنامه هسته‌ای، رهبر جمهوری اسلامی و جنگ
صحبت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24165" target="_blank">📅 22:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Byxc676y3L1HksjqOlIUQWAs0s8T5N1QfuULxxtJ8MhzZbVpqEKX25j5E6a_ZfSq89odpZ-VstsohACCpPlg7olm3Yj53xWZQAbnks6i98GiPuIkhG65zQTlc5Fvx5pSv_Civnvf9HrYLJ7n_oGcX1PpwCeQFJcRlE4EnImuMHdGlhWQPT6pkG7bpq-y58oEYKUr-UoUmM_DvpEz5BpfCTfZQix9IL-RHAO0PInQtfDrcjtTmpN_3uOItYmB7W9Pg1do65cQX4hUz4VAydswGDW7TWQpts29cuwT1RapCoSmJQOJ814_mVuZlcFy2mcyapnR-nauT5PGLULkXDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: هنگام آغاز سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل، چند هیئت دیپلماتیک در اعتراض سالن را ترک کردند. بر اساس تصاویر و گزارش‌های منتشرشده، صندلی‌های هیئت‌های عربستان سعودی، ایران، سودان، تونس، ازبکستان، سریلانکا، بنگلادش، الجزایر، مالزی، مونته‌نگرو،…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24164" target="_blank">📅 21:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7ZPmB0eTCntASGEoJy4xx5ZNArMqCJX-_0jrBNSU29TT6Y7lukP9jbBxaA6Ub16XASwDsIoOfRxqV5fOoa7iqS5VrS0dppPavcqRXxABDzbYoeA4chrnbqJfWSyy0uI3Z4KX2VIwdKxeFiCz1ZKvGgcNNeSzeTi3PlqpAqJWoi1ZESIxOfh5UYIZazp098lQW56Ev51ge2I2cK2ujSMsFh6dRqVl94wjJqqVC8youKic2qARFU-2ADTstfsFlyBqSfnFlDPqy12y7dsYuPpC-HFad57JlLMztCKrtZTKV3_EpE6YvJGjCNN31Myc2gtK9BbYdwraey25_QNG42KVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای سوخت‌رسان بریتانیا وارد جنگ علیه یمن شده‌اند؛ به‌طوری‌که برای نخستین بار از زمان آغاز جنگ عربستان و یمن، یکی از این هواپیماها بر فراز خاک عربستان سعودی و در نزدیکی مرز یمن دیده شده است.
این هواپیمای سوخت‌رسان بریتانیا از نوع Voyager KC.2 با شماره ZZ333، صبح امروز از پایگاه آکروتیری در قبرس برخاسته
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24163" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مشاور ارشد محسن رضایی : تاکنون
هیچ پیشرفتی
در مذاکرات میان ایران و آمریکا حاصل نشده است،آمریکا با شرایط ایران برای بازگشایی تنگه هرمز
مخالفت
کرده است،در صورتی که دولت ترامپ محاصره دریایی علیه ایران را لغو نکند و تحریم های نفتی علیه ایران را کاهش ندهد،پنجره نیمه باز دیپلماسی به زودی بسته خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24162" target="_blank">📅 21:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در تروث : رئیس‌جمهور شی و خانم پنگ به‌تازگی واشنگتن را به مقصد چین ترک کردند. این دیدار، نشستی سرشار از دوستی، اقتدار و موفقیت برای هر دو کشور چین و ایالات متحده بود. ما بار دیگر در ماه نوامبر در چین و سپس در ماه دسامبر در اجلاس گروه ۲۰ (G20) در میامیِ فلوریدا با یکدیگر دیدار خواهیم کرد. دستاوردهای بسیاری حاصل شده و خواهد شد. مشتاقانه منتظر دیدار بعدی‌مان هستم!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24161" target="_blank">📅 20:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کنسولگری ایران در نجف : فرودگاه بین‌المللی نجف، حرم امام اول شیعیان و پایتخت آخرین امام آنها، به روی بزرگترین کشور شیعه جهان بسته است؟!
@WarRoom
😂</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24160" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مسئول آمریکایی به شبکه الجزیره: واشنگتن در موقعیت قوی قرار دارد و کنترل تنگه هرمز را در دست دارد، بنابراین عجله‌ای برای رسیدن به توافقی با ایران نداریم.
حدود 40 میلیون بشکه نفت در 48 ساعت گذشته از تنگه هرمز عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24159" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYpYsDeChSiUzn3EraOnFbDFwoTYZrCvnSdGWXsb0guw5IJ-h7VX8bMZiktL2Y-LGfA5Mluic3zyX-5aRhQykXZgIs7lhNQW16PCaaVEy9YvHr-xmqu29Y3LpY77PMRazJiLKqQ4br27OS5E86y9mEDUqQR8k92pndHg4_cLF94TxXmVOcusABMF0-DPBbjvhZ3CeUM7Jb_VdThcBl5uRH7lTzLZ1D-ojmSiknLigdy7CsL4hLcm2bz1KfxsaIuoEfpetqONngfg1tZ_j9xRnSvDKkt_LZGOBliT9RcpfgSQNdFQngJep5MVOUcsnL5zgTigREcfHfnqym39yOXGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
تفنگداران دریایی آمریکا از یگان اعزامی تفنگداران دریایی یازدهم در حالی که روی ناو آبی‌خاکی
یواس‌اس باکسر (LHD-4)
در آب‌های منطقه‌ای در حال حرکت هستند، آموزش می‌بینند و به اجرای محاصره آمریکا علیه ایران ادامه می‌دهند.
تا ۲۵ سپتامبر، نیروهای سنتکام ۱۲۲ کشتی تجاری را برای اطمینان از رعایت کامل محاصره تغییر مسیر داده‌اند.
یعنی نسبت به رقم
۱۱۵ کشتی در ۲۳ سپتامبر، طی دو روز ۷ کشتی دیگر
تغییر مسیر داده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24158" target="_blank">📅 20:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک‌پست: اشیای نورانی مشاهده‌شده در آسمان تهران ممکن است مربوط به سلاح‌های لیزری آمریکا باشند.
این رسانه با اشاره به سامانه
هلیوس (HELIOS)
، گزارش داده آمریکا از سلاح‌های لیزری برای مقابله با پهپادها و موشک‌های کروز استفاده کرده است. هلیوس یک سامانه لیزر پرانرژی نصب‌شده روی ناوهای جنگی آمریکاست که می‌تواند با متمرکز کردن پرتو، حسگرها یا خود پهپاد را از کار بیندازد. با این حال، ارتباط مستقیم اشیای نورانی دیده‌شده در تهران با هلیوس
به‌طور رسمی تأیید نشده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24157" target="_blank">📅 20:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرتاب سه موشک از کوهدشت لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24156" target="_blank">📅 20:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز گفت: ایران در مورد برنامه هسته‌ای خود هیچ‌گونه امتیازی نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24155" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس»: ایران تصاویری از ماهواره‌های چینی را برای اهداف نظامی بکار برده است. واشینگتن به تهران ابلاغ کرد که ایران کنترلی بر تنگه هرمز ندارد و بنابراین حق ندارد درباره این آبراه شرط‌‌هایی بگذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24154" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=ub9UkUbMKWOrLP6G1WHUsASEPTjWdQaQyJlaViLlB_5p9kO0j0yz1FCT5rWsifCUiuOeq-7wIHbnhnkmQ5McwuAKjL6-4D_jdwvRro5B2INYriTyGFm26yxJuIFtAeJlZWNAYmcTnCBWaInWnK_e1JQgS77O6idlMCL01Gu-dZ5jooxolVbRXsAW2EgSo74CJIKHQxPdvrVkxzjzrG5ae2CwJGKGvdKo9Lbl90CV7JpqNHJ9ruAKz4QHOm0Xs1k1uY962QhrI_LAO19woJGGVHWFprCaNX3WIzADw6d2nP6JEz2n1VKsoOW9M_CA3Z3JQ051xJRK90VjxPHY1u-Asw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f03282bab.mp4?token=ub9UkUbMKWOrLP6G1WHUsASEPTjWdQaQyJlaViLlB_5p9kO0j0yz1FCT5rWsifCUiuOeq-7wIHbnhnkmQ5McwuAKjL6-4D_jdwvRro5B2INYriTyGFm26yxJuIFtAeJlZWNAYmcTnCBWaInWnK_e1JQgS77O6idlMCL01Gu-dZ5jooxolVbRXsAW2EgSo74CJIKHQxPdvrVkxzjzrG5ae2CwJGKGvdKo9Lbl90CV7JpqNHJ9ruAKz4QHOm0Xs1k1uY962QhrI_LAO19woJGGVHWFprCaNX3WIzADw6d2nP6JEz2n1VKsoOW9M_CA3Z3JQ051xJRK90VjxPHY1u-Asw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
در مور
د جنگ با تهران با شی جین‌پینگ بحث کردید؟
ترامپ: بله.
فکر می
‌کنم قرار است درباره ایران عالی عمل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24153" target="_blank">📅 20:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیوزمکس, ایران پیشنهاد معامله هرمز را ارائه داد: تهران می‌گوید اگر ایالات متحده تحریم‌های نفتی را لغو کند، دارایی‌های مسدود شده ایران را آزاد کند و با پایان دادن به جنگ در همه جبهه‌ها، از جمله لبنان، موافقت کند، می‌تواند ظرف چند روز تنگه هرمز را بازگشایی کرده و مذاکرات هسته‌ای را آغاز کند.
پزشکیان: آخرین پیشنهاد ما برای بازگشایی هرمز منتظر چراغ سبز ترامپ است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24152" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=qCxs3X3oizDzRh3jb-w2KIj4SZl9-TuOk8tvZQ9Lct-d7m8B1LEAbsgJVcl3wK8wzMy92dcTzYL-S6-VyIsw9Edjg6In2LpFDHMocQiZAapYuqRxtWLnEnUFcT9BeWrVRlJeXvkBz-HIibNhlKN238fB3tqJmEKSoNfrGrfxCdnx2emR6iATXpDukvgSjTawAZpJoN5SqpY3vXAohzefR093je3pVTkQQLEILKDxIxgxPgO56KgVRCns7t5NvmnuYF5k9Bfkw_YnnX2SHtF0E6wgzSrZatgns1JlBnj87BhjJfdYkT8s-HSqVubobZLYTdx-8a9RAOp0jSF5H1FmvEfikEKveEETFIfq68hFxBuuWB7x1wCngwwpq8B1Pm7O73-FI-gHWMEL6z2RebQLAmCBEW2Gt5ndq_9r9LIzZu70ZcRQ4j-LVSUyOpeA8QEcm4nBGgqsSpUOo6W6lPGPxuN6-4a7r2oloRkXO6z_CwwSZFiwT3d7pfjqKe_46N87C3vZdQg8hRuhJEGwRJolW9jSWyfuCniSkOD0K8FnsGXh1XXn8YKCo8zT-IF1gzVn3c4idRXKisFb3q-oegy9E7erSPz5PiMAzkkx5ezIGG7oIAiw9gPhuiIlS2sDfyOOYJd8Dajf6OGdEvrSItA2dE_hNnoIrhklR9BXGvKS7Q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1621b33d91.mp4?token=qCxs3X3oizDzRh3jb-w2KIj4SZl9-TuOk8tvZQ9Lct-d7m8B1LEAbsgJVcl3wK8wzMy92dcTzYL-S6-VyIsw9Edjg6In2LpFDHMocQiZAapYuqRxtWLnEnUFcT9BeWrVRlJeXvkBz-HIibNhlKN238fB3tqJmEKSoNfrGrfxCdnx2emR6iATXpDukvgSjTawAZpJoN5SqpY3vXAohzefR093je3pVTkQQLEILKDxIxgxPgO56KgVRCns7t5NvmnuYF5k9Bfkw_YnnX2SHtF0E6wgzSrZatgns1JlBnj87BhjJfdYkT8s-HSqVubobZLYTdx-8a9RAOp0jSF5H1FmvEfikEKveEETFIfq68hFxBuuWB7x1wCngwwpq8B1Pm7O73-FI-gHWMEL6z2RebQLAmCBEW2Gt5ndq_9r9LIzZu70ZcRQ4j-LVSUyOpeA8QEcm4nBGgqsSpUOo6W6lPGPxuN6-4a7r2oloRkXO6z_CwwSZFiwT3d7pfjqKe_46N87C3vZdQg8hRuhJEGwRJolW9jSWyfuCniSkOD0K8FnsGXh1XXn8YKCo8zT-IF1gzVn3c4idRXKisFb3q-oegy9E7erSPz5PiMAzkkx5ezIGG7oIAiw9gPhuiIlS2sDfyOOYJd8Dajf6OGdEvrSItA2dE_hNnoIrhklR9BXGvKS7Q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون می‌گوید پس از آنکه تلاش کرد ترامپ را متقاعد کند وارد جنگ با ایران نشود، رئیس‌جمهور ترامپ به او گفت:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس اهمیتی ندارد.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24151" target="_blank">📅 19:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3QMx_HPuMcZETs5QVk4eeb2vjwdCu4Fl-WLz67exWBQRNr-zAKrFtGWKUFZUHSs2h8s0hJSa3gtpYcbwkApe9WW3IlE6QKTGVu5_cjYmNe3qfXzfsUyiX9YIfNXTUv7XsM2plS1CVNDOFQ5z9aDJWcBTQKdfhTE4_qGbz9bln0BnUqZcrtmLQdelJP_qYbsMH8u1xzthTr1-fssXur8Qsf8qnITIhJT1WxEKzXJ9-18Zg5Vfmpa3YFVmgVoUvWEP-j_8YgXaH6BaJo3uFVa23DLJm2usMEZMWCFlKNDqkf79Lpml13-L7ndQa-BJLIewCGwbhDZrhZyiVwzETewbU44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf75471ddf.mp4?token=PGNweNsU3fgCfSH6f8i-zSZ2OHnS7WoUYpi8HY1SE73dTp7LCQCiAAdtd-m4HzhCb45RJ6uK3CWGY1i4UOV_j4FGIQMWCKRYsKf3rbqOrUco3nun50XXDVGryXpUWWTlCHnNcDiObHykb0xMxORrG24envdH2meXwsQZuMthQLOL7dnWUjlpIJLoJZXSLK6_yTceWM1_eE0nAuWNZLnjaEHFSi_bQwi3GucFMlh_nNNJYudHYqaS4jw48eBPX5Hh4nkMk2eAmhcIlCuQbfz1aGRUZRNl5P49Fb8gd9a1AfZ1KLcM77fvOhMEOJQhYMnc1oijJFgbcZt4k9vkue4x3QMx_HPuMcZETs5QVk4eeb2vjwdCu4Fl-WLz67exWBQRNr-zAKrFtGWKUFZUHSs2h8s0hJSa3gtpYcbwkApe9WW3IlE6QKTGVu5_cjYmNe3qfXzfsUyiX9YIfNXTUv7XsM2plS1CVNDOFQ5z9aDJWcBTQKdfhTE4_qGbz9bln0BnUqZcrtmLQdelJP_qYbsMH8u1xzthTr1-fssXur8Qsf8qnITIhJT1WxEKzXJ9-18Zg5Vfmpa3YFVmgVoUvWEP-j_8YgXaH6BaJo3uFVa23DLJm2usMEZMWCFlKNDqkf79Lpml13-L7ndQa-BJLIewCGwbhDZrhZyiVwzETewbU44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پدر جاویدنام ⁧
#عرفان_عبدی_پور
⁩ به اراجیف دیروز پزشکیان در فاکس‌نیوز
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24150" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیوید پردو سفیر آمریکا در چین:
ترامپ دیروز به شی جین‌پینگ صراحتاً گفت هرگونه کمک چین به ایران، چه اطلاعات باشد و چه قطعات یا تجهیزات نظامی، کاملاً غیرقابل‌قبول است,
ترامپ مواضع و منافع آمریکا درباره ایران را برای چین کاملاً روشن کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24149" target="_blank">📅 19:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627df24333.mp4?token=fl3qHtSNNq4-MTT_to2pDntiYjcdSOFotFnyKclV0jqDHeoP8yctBvO5ulbygjeLu1125mCpYiP0V31E7VyuKMxdXkkvnMOejIzgiY2ZOyP74fcjNwLf1EYlWB95Pnt3zfZKkvtU63pobtZHRtRwbEy1vlFBWFv-oB8u12k3p1xR5Q_b5eeWcA5MSbXKIN0J0WVT2B2jd3VWYW9obogXGvGZ-ulKcNK-2FAxpXnPVS7cSp3CFZ1345S0wvcYGdJOh4eug0Dw__8hUgeZ3QSiGEmt5k7TBcWJO2iKg401mPrCwo4-sbUsbbjnNg2LhEk_gcL23I0ucIuln0JjsMNh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627df24333.mp4?token=fl3qHtSNNq4-MTT_to2pDntiYjcdSOFotFnyKclV0jqDHeoP8yctBvO5ulbygjeLu1125mCpYiP0V31E7VyuKMxdXkkvnMOejIzgiY2ZOyP74fcjNwLf1EYlWB95Pnt3zfZKkvtU63pobtZHRtRwbEy1vlFBWFv-oB8u12k3p1xR5Q_b5eeWcA5MSbXKIN0J0WVT2B2jd3VWYW9obogXGvGZ-ulKcNK-2FAxpXnPVS7cSp3CFZ1345S0wvcYGdJOh4eug0Dw__8hUgeZ3QSiGEmt5k7TBcWJO2iKg401mPrCwo4-sbUsbbjnNg2LhEk_gcL23I0ucIuln0JjsMNh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش تحرکات ترابری آمریکا در ارتباط با خاورمیانه،د
ر۲۴و۲۵
سپتامبر(دیروز و امروز)
، فعالیت هواپیماهای ترابری و پشتیبانی آمریکا از جمله
C-17، C-5M، C-130 و KC-135
در ارتباط با منطقه خاورمیانه مورد توجه قرار گرفته است… یه خبرایی داره میشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24148" target="_blank">📅 18:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در
۲۲ و ۲۳ سپتامبر
، هواپیماهای
C-130H3 هرکولس
از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24147" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کارشناس نظامی صداوسیما:
در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24146" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=D7GIhJETIv3a8GLvWzYPZHbbiwFihhnvuXky1bl-G7sIDggEb7B9dtzUz9KOM1jXHm9rqzhNLXYpkj2GC9PhsV1PFjfSuBr0wLY3-za8fqBc5GQMn-E8r4_oDyBLJfsbejKPV76zYoiCRMFK0ak_V2DFXtnsRmxOzdhYxRKIPR9YXtx6Srzreq7A-LJY55rYp58qdulrDyU10K78R_ju6IktRCS2mQVsCeye3RxTmTgOqEfS3J9y-ABRpl1wkbT0BoXVrXxTroEfiQOQBz3FJhgWnYLfyebv-JEBmlANFmNG4TPNPvZmeKvRNARuoqfrx_rlbWU9D57pHDaC0ZXb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc3da78.mp4?token=D7GIhJETIv3a8GLvWzYPZHbbiwFihhnvuXky1bl-G7sIDggEb7B9dtzUz9KOM1jXHm9rqzhNLXYpkj2GC9PhsV1PFjfSuBr0wLY3-za8fqBc5GQMn-E8r4_oDyBLJfsbejKPV76zYoiCRMFK0ak_V2DFXtnsRmxOzdhYxRKIPR9YXtx6Srzreq7A-LJY55rYp58qdulrDyU10K78R_ju6IktRCS2mQVsCeye3RxTmTgOqEfS3J9y-ABRpl1wkbT0BoXVrXxTroEfiQOQBz3FJhgWnYLfyebv-JEBmlANFmNG4TPNPvZmeKvRNARuoqfrx_rlbWU9D57pHDaC0ZXb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای مهیب و ستون دود هم اکنون بهبهان
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24145" target="_blank">📅 18:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm4sVb6uY2cC5cjsENYFqSuZsBUtHsWHCnLtoVR3rgkMDFZxDsfHEJCSh2P4zPO5v3gnyQ3joxNEoJ9KC5NvT7N78tJty-iClBeEucP4Pot5s43XNrG9hBMZEUzXiTzChcxnPAIfQn6qP8MK5LuAuJ5SW3ejvBQ6PDyPw7IO0TtooMaos5LXFV9rDbNiTj5Iz-vCfSOtj6u1_joiLTj4r77joPaXz7OzyISuPoaZzlzp0UEMOR80i6A0LTuTZPUY1eNUUp7KP41ZXQ4zUkbzy55tw-Yyg5Hv1svBsfoPBWQ-tuW_yNJ0hxvHtGS0FGSCUNX-IVJOlnfhOXXaaW1eOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین نام رسمی جنگنده پنهانکار J-35A را اعلام کرد:
رسانه دولتی چین، CCTV، برای نخستین‌بار این جنگنده نسل پنجم را با نام
یون‌لونگ (Yunlong؛ اژدهای ابری)
معرفی کرد. در همین برنامه نام جنگنده‌های اصلی نیروی هوایی چین نیز اعلام شد:
J-10 — منگ‌لونگ (Menglong؛ اژدهای نیرومند)، J-11 — یینگ‌لونگ (Yinglong؛ اژدهای بالدار)، J-16 — چیان‌لونگ (Qianlong؛ اژدهای پنهان)، J-20 — وی‌لونگ (Weilong؛ اژدهای باابهت)، J-35A — یون‌لونگ (Yunlong؛ اژدهای ابری).
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24144" target="_blank">📅 18:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سفیر آمریکا در چین: طرف چینی در مذاکرات پنجشنبه تأیید کرد که از ایران حمایت نمی‌کند.
دیوید پردو گفت ترامپ به شی جین‌پینگ تأکید کرده که هرگونه کمک مستقیم یا غیرمستقیم به ایران، از جمله ارائه اطلاعات، قطعات یا تجهیزات نظامی،
کاملاً غیرقابل قبول است.
به گفته او، دو طرف همچنین توافق دارند که
ایران نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24143" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945aef0662.mp4?token=IdGw86zpDsApvOAHH2WcPw9_CM9H9bOWulggrWlhobEDHyTfI72nIWaQG6Xf_Gutj2RltaP9lvH9U_Oyy8R6r4n0icm-RDfK8Ye1Ou_gQVoAcNuq5RHRzMn2pP_RsfQHi1QD5LkM9IWYWvZj-GHVzZTJddURcp7tyUWBapUoRSLBkVZ7yqtifZcBqRny-Wf5ly-iV-DPGQw-FTrgXNREBaY6zR17rIh1aLW-s4_Y0FATyFwvlRa_5FXWP9mgWfI0EGfXLtCocedV9ZZ0QKHHWZn2V4-LktYwvUaDuoNDMy13Jzh7VAlzqb6SrwvVGceySbFlkVlbtbjmq4I7G5ZE5wwIE29JfCVsV-0RdW81i9Iip3Nu-iGIjIDk6tD4xLVKowmnJlgjE4TnclYOHl93cUvfpD2unX-WQomsuwRKGYJqlcWCPMWr_yogN7UM72ZQ4LOHT9TTf6KpG0b4Pl8th18AIhiozvgVdw9vIM3HqFQJmGUOprkz26dKvJzM9rfESsNHAF4AN-YbXGRfm_74654zlibi4NNgYyyl1OW37WcT-PZ2PzqTNMcbDrmaa9BB7kn25BhUOCoLKblEX4wIwoMLa1QZ23TQMk3915nrR-xPqGfprfQo4MxAFdfnoDDTpBUFvyhRmCJiKtWy-E28jChwvjwNjPLQVXM0ndWgzls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945aef0662.mp4?token=IdGw86zpDsApvOAHH2WcPw9_CM9H9bOWulggrWlhobEDHyTfI72nIWaQG6Xf_Gutj2RltaP9lvH9U_Oyy8R6r4n0icm-RDfK8Ye1Ou_gQVoAcNuq5RHRzMn2pP_RsfQHi1QD5LkM9IWYWvZj-GHVzZTJddURcp7tyUWBapUoRSLBkVZ7yqtifZcBqRny-Wf5ly-iV-DPGQw-FTrgXNREBaY6zR17rIh1aLW-s4_Y0FATyFwvlRa_5FXWP9mgWfI0EGfXLtCocedV9ZZ0QKHHWZn2V4-LktYwvUaDuoNDMy13Jzh7VAlzqb6SrwvVGceySbFlkVlbtbjmq4I7G5ZE5wwIE29JfCVsV-0RdW81i9Iip3Nu-iGIjIDk6tD4xLVKowmnJlgjE4TnclYOHl93cUvfpD2unX-WQomsuwRKGYJqlcWCPMWr_yogN7UM72ZQ4LOHT9TTf6KpG0b4Pl8th18AIhiozvgVdw9vIM3HqFQJmGUOprkz26dKvJzM9rfESsNHAF4AN-YbXGRfm_74654zlibi4NNgYyyl1OW37WcT-PZ2PzqTNMcbDrmaa9BB7kn25BhUOCoLKblEX4wIwoMLa1QZ23TQMk3915nrR-xPqGfprfQo4MxAFdfnoDDTpBUFvyhRmCJiKtWy-E28jChwvjwNjPLQVXM0ndWgzls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیروز در مجمع عمومی سازمان ملل، بنیامین نتانیاهو از اردوغان گفت و از هزاران غیرنظامی کُرد که کشته شده‌اند. جمله روشن بود، به انگلیسی، بی‌هیچ ابهامی: Kurdish civilians.
در همان لحظه، روی آنتن زندهٔ ایران اینترنشنال، این جمله سانسور شد به «غیرنظامیان ترکیه».هر دو را در این ویدیو کنار هم گذاشته‌ام. ببینید، و خودتان قضاوت کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24142" target="_blank">📅 17:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فایننشال تایمز: حوثی‌های یمن به اتحادیه اروپا اطمینان داده‌اند که کشتی‌های اروپایی را در دریای سرخ هدف قرار نخواهند داد.
حوثی‌ها گفته‌اند عملیات آنها در حال حاضر
متوجه عربستان سعودی و منافع مرتبط با این کشور
است و قصد ندارند کشتیرانی بین‌المللی یا کشتی‌های اروپایی را مختل کنند. همزمان، پس از مذاکرات با آمریکا با میانجی‌گری عمان، حوثی‌ها به واشنگتن نیز اطمینان داده‌اند که
کشتی‌های آمریکایی را هدف قرار نخواهند داد
؛ در مقابل، آمریکا نیز از تشدید حملات علیه حوثی‌ها خودداری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24141" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVH3fD6Tkzf0Q9Ra9jLySA3M2oiAc3sQhqb7neCxZCnmIIXauMTafhrNx0ajNoAnCZHu9syGTFerd2EFmHJwlAQeCmFMVo1oywkeDrhyLVo8_LWhG-IbtdABdcnq1OtSKfVGPK46Dfv1CaxfF9wUttRFXnPJGC-95sj6JmrSi4WQx7uS9Aiq334VsX1D2YcLH0eZeW5nyCe23kjINlzBin2e7bHhpYuMh2H7Kz1aJVW9hoOFZPH8zvaj1hAy5-M1CmojVvxa0dfjiAfshO2RKv5E5CpOg6fi3FEZxlCHme6_cvu87xV-dsEnZG6wOWwJ6uIbrnIF3vPA185JASKtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علنی شدن خونشوران بین‌المللی و لابیگران رژیم، دیدار پزشکیان با دستنشانده‌های رژیم در حاشیه نشست سازمان ملل. رابرت مالی، تریتا پارسی، فرناز فصیحی، نگار مرتضوی.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24140" target="_blank">📅 16:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صفحه رسمی‌وزارت امور خارجه اسرائیل به فارسی:
یه خبر خوب.حکومت شرور جمهوری اسلامی سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24139" target="_blank">📅 16:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دادستانی کل نیویورک از پولی‌مارکت به اتهام فعالیت غیرقانونی قمار شکایت کرد.
مقام‌های نیویورک می‌گویند این پلتفرم بدون مجوز، بازارهای پیش‌بینی ایجاد کرده که از نظر قوانین ایالتی نوعی شرط‌بندی محسوب می‌شود. نیویورک از دادگاه خواسته فعالیت بدون مجوز متوقف شود،
سودهای حاصل از این فعالیت‌ها بازگردانده و جریمه‌ای معادل سه برابر سودها پرداخت شود.
پولی‌مارکت در مقابل می‌گوید بازارهای پیش‌بینی تحت نظارت فدرال قرار دارند و ایالت نیویورک صلاحیت برخورد با آن را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24138" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در‌ حدود ۱۰ دقیقه تنگه ۳ بار صدای ناله اپراتورهای لانچر که کتلت شده اومد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24137" target="_blank">📅 14:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع: تصاویر ماهواره‌ای و اطلاعاتی که از سوی گروه‌های چینی ارائه شده است، به ایران کمک کرده تا کشتی‌ها را در تنگه هرمز تهدید کند و حملات دقیقی را به پایگاه‌های نظامی آمریکا در خاورمیانه انجام دهد. این بخشی از بهبود چشمگیر توانایی‌های هدف‌گیری ایران در چند ماه گذشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24136" target="_blank">📅 14:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیروهای دولتی یمن: در یک حمله سریع ما به قله کوه نمان و منطقه دار الکافر تسلط یافتیم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24135" target="_blank">📅 14:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">3 رسانه‌ به کاخ سفید بازمی‌گردند
پس از آن‌که دونالد ترامپ دسترسی خبرنگاران سی‌ان‌ان، MS Now و پولیتیکو به کاخ سفید را لغو کرده بود، یک قاضی فدرال دستور داد این محدودیت برای
14 روز متوقف
و مجوزهای خبرنگاران فوراً بازگردانده شود.ترامپ پیش‌تر مدعی شده بود پوشش این رسانه‌ها «دروغ» و تهدیدی برای امنیت ملی است، اما قاضی گفت شواهد کافی برای اثبات این ادعا ارائه نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24134" target="_blank">📅 14:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز: فرودگاه‌های اربیل و سلیمانیه در عراق نیز از روز جمعه، پذیرش پروازهای هوایی از ایران را متوقف خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24133" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۴ ریشتر در عمق ۸ کیلومتری، سفیددشت اصفهان را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24132" target="_blank">📅 13:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=oACCPzlJj0L-8Gliq7n7NlmBxR7CgCVtiztlLfLo8-8XWm9TJyWobfrIRhZglf1PPKr2ZfoVSMj3VEo5LooYWUxuABbfaU_-b3QgCdfI-yCHBMYyyI0VPLPPmSRUXgAGSyJMkTt4vjTEXBZ_OpoaYhjJK8z9KM6KZR0VDRiVJIMQoFFO8HLAW_YhX8qEqaqrctMxt5MUc0jBU0aSz2ioqYOnRvfVLMCOTZ2eO2DU4aegf47l9NjULejWxd4zJ0C2iHHFq7eGQUqdlrfIgoZuKvUSrBSBvGytPcu_rAW-XqOJRXe9DR9sC4xQbbO2_Rq2rQiWCqUqtEfrIhn5W3XZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7fd7acc.mp4?token=oACCPzlJj0L-8Gliq7n7NlmBxR7CgCVtiztlLfLo8-8XWm9TJyWobfrIRhZglf1PPKr2ZfoVSMj3VEo5LooYWUxuABbfaU_-b3QgCdfI-yCHBMYyyI0VPLPPmSRUXgAGSyJMkTt4vjTEXBZ_OpoaYhjJK8z9KM6KZR0VDRiVJIMQoFFO8HLAW_YhX8qEqaqrctMxt5MUc0jBU0aSz2ioqYOnRvfVLMCOTZ2eO2DU4aegf47l9NjULejWxd4zJ0C2iHHFq7eGQUqdlrfIgoZuKvUSrBSBvGytPcu_rAW-XqOJRXe9DR9sC4xQbbO2_Rq2rQiWCqUqtEfrIhn5W3XZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیپلمات اسرائیلی نام تمام کشورهایی که جلسه را ترک کردند یاداشت کرد تا بعد به خدمتشان برسند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24131" target="_blank">📅 13:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زلنسکی، رئیس‌جمهور اوکراین:
«طرف آمریکایی پیشنهاد برگزاری
نشست سه‌جانبه در امارات متحده عربی
را مطرح کرده است.
ما منتظر پیشنهاد آمریکا درباره
تاریخ برگزاری این نشست
هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24130" target="_blank">📅 12:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=fTzi1c0i94k30J4Xy-i8JZ4Lw8kZZPo2OQ-cqjP0iUv2Ip1ix8nGiHcgQ8AHKgMdFEv5OJ7ACnXJZ2fjxb65aWZNzgypgYV1duVjy_FHrZh1BwNBz8s_xb8N5-em8KAaez3Xzc3TjnlsnLSkbVigMnfFGdpFwaE-ftlquXS1rvl6zsioQb7DpnpmlwYqXsx7v64oTTQ4Z5eXHqZmSUlZQeulEDcH9tzAuRKfpk8POH7fE_KE4eMLuVF_B2U7qz6nLxqHz0GOpcapcnj8APJj5xPBuhQ0fhuW2qPARjl14aIekfarlpgqXH-UkRXQ-P3B0eX434cA5Da9A2Cdz1ZLjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01aa2ba27b.mp4?token=fTzi1c0i94k30J4Xy-i8JZ4Lw8kZZPo2OQ-cqjP0iUv2Ip1ix8nGiHcgQ8AHKgMdFEv5OJ7ACnXJZ2fjxb65aWZNzgypgYV1duVjy_FHrZh1BwNBz8s_xb8N5-em8KAaez3Xzc3TjnlsnLSkbVigMnfFGdpFwaE-ftlquXS1rvl6zsioQb7DpnpmlwYqXsx7v64oTTQ4Z5eXHqZmSUlZQeulEDcH9tzAuRKfpk8POH7fE_KE4eMLuVF_B2U7qz6nLxqHz0GOpcapcnj8APJj5xPBuhQ0fhuW2qPARjl14aIekfarlpgqXH-UkRXQ-P3B0eX434cA5Da9A2Cdz1ZLjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  چونفدا ها رالی موتوری برگزار‌کردن هم اکنون میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24129" target="_blank">📅 12:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to0Lltfcs42wiiyVQ8n5OO2rOEkpKOug5vs3-oS5pDOPegDSWwRzdO16aQnZF_LaAe2RjYQe-EQCeo1ThDZOhnf0IaanqTWN1WpS15LQHAUEqqNq_ky1rDCPgcXJ5YqGqanpHHA7D2rAKtRktcD3T2JVCvuQrFjgDeCpOjpYcokcPoNoilJI4Ld_JojKmoLcgTqfw_F1b1--mLmICR-6EfSh7rsummFCMx1LMc0yJ9AUoUT9X5gRwSQr365ON3t9wgVbveymUhIo6zh1ibLCFDIFVWxFhNBbkW5wX3B_totDJteC0dPcaCC7ZbbRPP1XzbcT6npdfVK5Dt6RAoQLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید غضبان (دیپلمات اسرائیلی و مشاور در وزارت امور خارجه اسرائیل):
«اسرائیل او را از میان برداشت، اما قاب عکسش مجبور شد تمام آن سخنرانی را تحمل کند؛ به‌ویژه آن بخشی که نتانیاهو با شور و حرارت از فروپاشی جمهوری اسلامی حرف می‌زد»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24128" target="_blank">📅 12:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وال‌استریت ژورنال:
میانجی‌ها
در تلاش‌اند
دور جدید مذاکرات میان آمریکا و ایران را
اوایل هفته آینده در عمان
برگزار کنند؛ مذاکراتی که محور آن بازگشایی تنگه هرمز و تلاش برای پایان جنگ است. این مذاکرات هنوز قطعی اعلام نشده و در مرحله رایزنی قرار دارد.
@WarRoom
حقیقت یاب اتاق جنگ : این اصل خیر است ، مذاکرات هنوز نهایی‌نشده و خبر رسانه های زد فیک نیوز است</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24127" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دریادار رابرت هاروارد، معاون پیشین فرمانده سنتکام:
«من ذهنیت مردم زیبای ایران را می‌شناسم. آنها به آزادی و زندگی باور دارند. ایران نخستین کشوری بود که منشور حقوق بشر داشت. من
متعهد
به کمک به همه شما هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24126" target="_blank">📅 11:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP5h5f2e7SZi8EjOXqF7p2IzgkIB-c5AZhvYYsMwgH4PbyQIpo5ov4Qs5NI6R__R5yvjFu_zZut92Cp4hWTKegnilp9-J7-64Y9BMqoJ0rLSIKSi7ZLJvpVelYHumwqBD79_LRbdpHIyQ_YjggDHg3NofJBU-NechO3AHxYFO6q_sVEnnZpzkhCV6JGi-CIz4pkWUQ-89-gwcgVzbhj29PMO6R5LoRszmSebBpuKnb7PsebFnwi-jkN3L1Z_RODjrAF9gqUF_Gsozq6oWgQUODwgYAJOcFVa1hDEcL2UJdofeR7onMUJHrrH1VvQ3zMNIz7ddK_TRTo_tLh9A6zhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پی۸ پوسایدون ، ام ۴۰۰ (نمونه مشاهبه هرکولس از ایرباس) و ۴ سوخترسان هم اکنون در حال انجام مأموریت در منطقه خلیج فارس و تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24125" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏ نتانیاهو در پاسخ به خبرنگاری که پرسید پیامش برای مردم ایران چیست،گفت :
«ما با شما هستیم. ناامید نشوید.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24124" target="_blank">📅 11:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ان‌بی‌سی نیوز:
عباس عراقچی، وزیر امور خارجه ایران، در نیویورک به خبرنگاران گفت تهران از طریق میانجی‌ها طرحی را به مقام‌های آمریکایی ارائه کرده که در صورت پذیرش شروط ایران،
پس از هفت روز به بازگشایی تنگه هرمز و ازسرگیری مذاکرات
منجر خواهد شد. به گفته عراقچی، یکی از شروط طرح، پذیرش مسیر عبور دریایی مورد توافق ایران و عمان در تنگه هرمز است. ان‌بی‌سی نیوز گزارش داد کاخ سفید تا زمان انتشار این گزارش به درخواست اظهارنظر درباره این طرح پاسخ نداده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24123" target="_blank">📅 11:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جروزالم پست:
نیروهای دولت یمن حمله حوثی‌ها به یک مسیر مهم تدارکاتی میان عدن و تعز را دفع کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24122" target="_blank">📅 11:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کوین‌دسک
:
حدود
۱۸ میلیارد دلار قرارداد آپشن بیت‌کوین و اتر
امروز منقضی می‌شود؛ حجم بالای سررسید می‌تواند در کوتاه‌مدت نوسانات بازار و جریان‌های هجینگ را افزایش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24121" target="_blank">📅 10:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز:
تعداد عبور کشتی‌ها از تنگه هرمز در روز پنجشنبه به ۹ فروند کاهش یافته، در حالی که روز قبل ۱۴ فروند و میانگین ۱۰ روزه حدود ۱۸ فروند بوده است؛ البته کشتی‌هایی اصلی که انتقال را انجام میدهند و ترانسپوندر خود را خاموش کرده‌اند در این آمار نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24120" target="_blank">📅 10:56 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
