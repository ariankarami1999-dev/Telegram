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
<img src="https://cdn4.telesco.pe/file/XEPx3HeecqAQ_V7GpJs6yHCUO5awMV3VnjdAmJPAP8r-7xFT1PY8uZpXj-PRXM6luH5xsWcJjbx5VbnVyorpEuxOfIvVhqO0kMn-36PLab4aD51J10PVdUECAvneSpsKNCZM7FeRwx3rW7Btg0R5lIZCqXR2vmPnwS0Vo0zjI6HG6Nq0Gn3QkSFCOQv6d6fxXoXw_hN-tgqM3Col7eldz8Bsr0hkT2WOU8jdCqh8I2R3axJvirZRsRLvVnslLAZ9_sZSwLTX2sfZSdG4WzPiwxdsJnCP5JdBGOg8rFpo-as7YIepG66xiEp6S0EPpOhiIRpxqyb7QVZMr_Q8KGjYvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 390K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار در‌ اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/withyashar/18166" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وای‌نت: نتانیاهو شنبه شب به واشینگتن سفر و روز سه‌شنبه در مراسم خاکسپاری لیندزی گراهام، شرکت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/18165" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۳ انفجار اصفهان سمت حکیم نظامی (ممکنه مهمات هم باشه )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/withyashar/18164" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
دوستان لطفا از ارسال پیغام صدای جنگنده دیگه خود داری‌کنید چون بسیار ‌زیاده و دایرکت رو هنگ میکنه همچنین تمام پیغام های ارسالی رو فقط در یک مسیج ارسال کنید ، تا من بهتر بتونم خدمت رسانی‌کنم ، ممنون</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/18163" target="_blank">📅 11:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در حملات آمریکایی در شهر بندری چابهار در جنوب شرقی ایران. طبق گزارش‌ها، دو اسکله دریایی و برج کنترل ترافیک دریایی در بندر، به همراه زیرساخت‌های دیگر مرتبط با فعالیت‌های دریایی، مورد حمله قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/18162" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/18161" target="_blank">📅 11:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فرمانده سنتکام: ایران در یک هفته گذشته به هفت کشتی تجاری حمله کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/18160" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رسانه‌های اسرائیلی: نتانیاهو شنبه به واشنگتن می‌رسد تا در مراسم خاکسپاری سناتور لیندسی گراهام شرکت کند.
وب‌سایت "یدیعوت آحارونوت": زمان دقیق ملاقات نتانیاهو و ترامپ هنوز مشخص نشده است، اما انتظار می‌رود که آن‌ها اوایل هفته آینده با یکدیگر دیدار کنند
@WarRoom</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/18159" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بلومبرگ درباره دبیرکل سازمان دریایی بین‌المللی: تنگه هرمز همچنان برای کشتی‌های تجاری بسیار خطرناک است.
بلومبرگ گزارش داد: ۶۰۰۰ دریانورد همچنان در تنگه هرمز گرفتار شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/18158" target="_blank">📅 11:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیویورک‌تایمز : وزارت خزانه‌داری ایالات متحده اعلام کرد تلاش‌های خود را برای مختل کردن شبکه غیرقانونی کشتی‌رانی و دور زدن تحریم‌ها که تحت مدیریت محمدحسین شمخانی فعالیت می‌کند، تشدید کرده است. محمدحسین شمخانی، فرزند علی شمخانی، مشاور کشته‌شده رهبر پیشین جمهوری اسلامی، است.
همچنین ریچارد برمن، قاضی پرونده، رضا ظراب تاجر ایرانی‌تبار را به مدت زمانی که پیش‌تر در بازداشت گذرانده بود محکوم کرد و هیچ حبس تازه‌ای برای او در نظر نگرفت. ضراب از سال ۲۰۱۸ از بازداشت خارج شده بود، اما زیر نظر مقام‌های فدرال با نامی‌ جدید به عنوان شاهد زندگی می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/18157" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4668458d0.mp4?token=HfHU0lOBFYPSaAgqCHWkBAEU2o8NF56-biCWnoGKBhCOObraZZUXCrn5BNSujeJxEqw3rVBtatOErwdJqyi6Ev2bQ7njJY5hUJ_jzZ9M_TeWI-cvjmPhd7wJc9ZkjmJNyr1LoweqOChDE6PArjfuJhCBxw779LIWZRbWGhqENvTbed21mnoJdZ1NR5DC3GTXUJ3mAuqmXt4aNn3a3q2lI75m6le_E2l_NezoiwVJ-DlgpvoU_uluk6N1F8zKdakLuWMiQdZJHU2iyMlJogbeIRUZ_KjTQxC2ElLY7eXUCVa6-F_epchmBMhucF8-dzl6d7MJDteeRmoNXGcEzQGiFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4668458d0.mp4?token=HfHU0lOBFYPSaAgqCHWkBAEU2o8NF56-biCWnoGKBhCOObraZZUXCrn5BNSujeJxEqw3rVBtatOErwdJqyi6Ev2bQ7njJY5hUJ_jzZ9M_TeWI-cvjmPhd7wJc9ZkjmJNyr1LoweqOChDE6PArjfuJhCBxw779LIWZRbWGhqENvTbed21mnoJdZ1NR5DC3GTXUJ3mAuqmXt4aNn3a3q2lI75m6le_E2l_NezoiwVJ-DlgpvoU_uluk6N1F8zKdakLuWMiQdZJHU2iyMlJogbeIRUZ_KjTQxC2ElLY7eXUCVa6-F_epchmBMhucF8-dzl6d7MJDteeRmoNXGcEzQGiFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمای نزدیک از برخورد شاهد ۱۳۶ ایران به سوله امریکایی ها در کویت
@WarRoom</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/18156" target="_blank">📅 11:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کپلر: ۹ فروند از ۱۱ کشتی‌ای که روز سه‌شنبه از تنگه هرمز عبور کردند، از مسیر ایران حرکت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/18155" target="_blank">📅 10:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل: دادگاه نظامی، یک سرباز اسرائیلی را به دلیل ارتباط با یک جاسوس ایرانی، به ۵ سال حبس محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/18154" target="_blank">📅 10:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارتش ایران: در حملات آمریکایی به یک پایگاه نظامی در شهر بمپور، واقع در استان سیستان و بلوچستان، صبح امروز، ۷ تن از نیروهای ما کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/18153" target="_blank">📅 10:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Tether = 186000 T
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/18152" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یاشار جان سلام آسایشگاه سربازان ایرانشهر، به خاطر اینکه دوست صمیمیم سربازش بوده ازش پرسیدم الان، میگه که لانچر رو دقیقا کنار آسایشگاه جانمابیش کردن، با شلیک لانچر گویا نقطه یابی شده و بعدم خود لانچر رو زدن لانچره میترکه که انفجارش آسایشگاهو زده اینا توی آدمای…</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/18150" target="_blank">📅 10:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA R</strong></div>
<div class="tg-text">یاشار جان سلام
آسایشگاه سربازان ایرانشهر، به خاطر اینکه دوست صمیمیم سربازش بوده ازش پرسیدم الان، میگه که لانچر رو دقیقا کنار آسایشگاه جانمابیش کردن، با شلیک لانچر گویا نقطه یابی شده و بعدم خود لانچر رو زدن
لانچره میترکه که انفجارش آسایشگاهو زده
اینا توی آدمای بیگناه عادت دارن مهمات و لانچر جاساز کنن تا بعدش بگن وای وای مردم بیگناه یا سرباز وظیفه آسیب دیده
😞
😞
😞
😞</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18149" target="_blank">📅 10:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e10469190.mp4?token=mNism79pSVAHD-9N8AFRfjV8LexmKXDiHdm521Y7el72pixWBeJKcvnXCwFtTFOwxPO-j0xQjqv4KrcSQ9VWG9Ya8thUqR0ONv9kGR6l0SpoKUFd8bp1FG7Xex1lTwheAEe36rjGGcck_RVusHRuXvJmazsAdJVQC7zXF-QD06LAsbdZoJTiFPHpNkCGmHBrkVLeMqo20r_na_LurLp3ILYtpYX6RF22J961AmF01F39QefaGN0TpKA794lh1n1fPCWh-MO5QSu4CFd8Bamz8SSrSezHZAI0LFpyU_dOlkH0Ns4W7SOLAEbkoUc6prXQkd0Yb5Uic5X6T7Cnury4Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e10469190.mp4?token=mNism79pSVAHD-9N8AFRfjV8LexmKXDiHdm521Y7el72pixWBeJKcvnXCwFtTFOwxPO-j0xQjqv4KrcSQ9VWG9Ya8thUqR0ONv9kGR6l0SpoKUFd8bp1FG7Xex1lTwheAEe36rjGGcck_RVusHRuXvJmazsAdJVQC7zXF-QD06LAsbdZoJTiFPHpNkCGmHBrkVLeMqo20r_na_LurLp3ILYtpYX6RF22J961AmF01F39QefaGN0TpKA794lh1n1fPCWh-MO5QSu4CFd8Bamz8SSrSezHZAI0LFpyU_dOlkH0Ns4W7SOLAEbkoUc6prXQkd0Yb5Uic5X6T7Cnury4Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دیگری از حمله هوایی آمریکا به اسکله شهید کلانتری چابهار و پایگاه امام علی سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/18147" target="_blank">📅 10:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱.۱۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/18146" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4cb2010d.mp4?token=K06GyZyTkjMZpj_egzRJVOqzSQoKVgtYWjGW1i71IKsn-mNo_YEkEF4ED-OFTtt2PrYTt5daDF-rJF8Dkc1qdQuSgjjSsDyEk9ABRIqSVjvCdRxDPW3PT1Hu4F30LakLOY-wwzyeQQKavF0x8Uw0IiGFAH9CXZDgqyt9L__-pW_RIyfGJF03fcasRpaNbdQ6Z7YRTo-mql2qIXfenjYihaMMCxJZJXCYdSY8ESY0HORqyz3BgwmTQda058r_hXkQwR-3IPGtGTZVq8jcbkRxaaKuZgEyTdq5Hzk2LYqhFHnXjIOx7dp-sIrjOTcc7uzhkKr9pGn0fIAGKg_kCeFRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4cb2010d.mp4?token=K06GyZyTkjMZpj_egzRJVOqzSQoKVgtYWjGW1i71IKsn-mNo_YEkEF4ED-OFTtt2PrYTt5daDF-rJF8Dkc1qdQuSgjjSsDyEk9ABRIqSVjvCdRxDPW3PT1Hu4F30LakLOY-wwzyeQQKavF0x8Uw0IiGFAH9CXZDgqyt9L__-pW_RIyfGJF03fcasRpaNbdQ6Z7YRTo-mql2qIXfenjYihaMMCxJZJXCYdSY8ESY0HORqyz3BgwmTQda058r_hXkQwR-3IPGtGTZVq8jcbkRxaaKuZgEyTdq5Hzk2LYqhFHnXjIOx7dp-sIrjOTcc7uzhkKr9pGn0fIAGKg_kCeFRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا (۵:۳۰ صبح ۱۵ ژوئیه به وقت تهران) دور دیگری از حملات علیه ایران را تکمیل کرد و ده‌ها هدف نظامی در نزدیکی تنگه هرمز و مناطق ساحلی ایران را هدف قرار داد. جنگنده‌ها، پهپادها و ناوهای آمریکایی در جریان این موج هفت‌ساعته با استفاده از مهمات دقیق، سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری و خدمه غیرنظامی بیش از پیش تضعیف شود.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/18145" target="_blank">📅 10:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGlcABE-AUSxbPraW5iCVgZ7KQ_SNxkW5IRsHMX-rOX-5XFK5dSzi_0Elw2QeJXbcXjdTckgvENjc4wPmIIhlQRbuDQjLG8f9n3zqJBDVLG7PXrpDELXSpWmHlowmFRTaiW6pe1E80Q2clVqyqMYgt_GU2F9cUGmWtnYgv0JvIhyfbsInh0YT9rPSOOYrL_2rlwvmS26BTQCKX09e2YG1JKvhpjg5oFshews7e7pYA7NmULf5GzMOQZaP40pIXZukvL_2A-Nvkr0a1DSqNUnxulOEsEzu0-VIEn_RhtGvBiQtSt4jN102mM1U6rI5PI7PjFNytlh-6Rv8cnFOcz1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پیش چابهار کنار برج مراقبت رو دوبار زد
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18144" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c138d5ff92.mp4?token=j5b_AdeHiPfpkh4ScN-4U7UWXZiSoxiBh-Uesda8YCAglSB84qlwnoK4Xg5uEJDugz2cs6e4voFEqO1EnUDE0CwQRh83nsnUWPopYqRPNYPQiIxU_1PUQBRM72goGYtsesiyAe2vRTPRFpcEg10gsS-bgYXr55tcVQF7jnmqqUe7D5ct1AMAq2G_uJdh3gygCeo6QYGD6RQ8AYjzZcdVNzZUQv0aIxnWUBrwt7EcKKmFrHLdxawofD1VSFNgLdBK7rkLAtij7dfbXJ_YR8f-z-YNcE8wf9qYIjL9fGOHpzEynIkA2zxBYQse5cD1pXHFJqjD1s-kUMVKifk-b019_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c138d5ff92.mp4?token=j5b_AdeHiPfpkh4ScN-4U7UWXZiSoxiBh-Uesda8YCAglSB84qlwnoK4Xg5uEJDugz2cs6e4voFEqO1EnUDE0CwQRh83nsnUWPopYqRPNYPQiIxU_1PUQBRM72goGYtsesiyAe2vRTPRFpcEg10gsS-bgYXr55tcVQF7jnmqqUe7D5ct1AMAq2G_uJdh3gygCeo6QYGD6RQ8AYjzZcdVNzZUQv0aIxnWUBrwt7EcKKmFrHLdxawofD1VSFNgLdBK7rkLAtij7dfbXJ_YR8f-z-YNcE8wf9qYIjL9fGOHpzEynIkA2zxBYQse5cD1pXHFJqjD1s-kUMVKifk-b019_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام موشک آمریکا با استفاده از توپ ضد هوایی در اسلام آباد غرب، کرمانشاه
@WarRoom
یاشار : خیلی از‌ گزارش های انفجار مردمی صدای توپ ضد هوایی است</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/18143" target="_blank">📅 09:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آکسیوس : ترامپ و تیم امنیت ملی آمریکا درباره حملات گسترده‌تر به رژیم ایران رایزنی کردن
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/18142" target="_blank">📅 09:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⚠️
دوستان لطفا از ارسال پیغام صدای جنگنده دیگه خود داری‌کنید چون بسیار ‌زیاده و دایرکت رو هنگ میکنه همچنین تمام پیغام های ارسالی رو فقط در یک مسیج ارسال کنید ، تا من بهتر بتونم خدمت رسانی‌کنم ، ممنون</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/18141" target="_blank">📅 09:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3402aca62e.mp4?token=eiaRSR0ida9KU7cIp92RaJpdFfQbhViXqUt9YRl_THVcd_1Zuicm3qkDhTs36xVsiVzdpmfb82_7zs7NlBpvjOVmpPkHBmjwkqnOcu067yjIjaQXowfvUxZ30enUjClLam9p6d_DLM9uy4pmcR-XJRHYQagiCKIZNkGlaOUasYqhyMD6TDvsr5uKM03fHoJEM_5s5RAA2QHlCqBJZQnAPrIYrIZch6qH313UxAVPBokp3iebbWpUprudghUWMMVZtOELB846HigJKv3PI4nCekC9jLtVyLPmQ660bl1zC-n7_Wg138nYGH8QKTTwSLhpVfb0jfjkT_Vq5JPUQ8RG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3402aca62e.mp4?token=eiaRSR0ida9KU7cIp92RaJpdFfQbhViXqUt9YRl_THVcd_1Zuicm3qkDhTs36xVsiVzdpmfb82_7zs7NlBpvjOVmpPkHBmjwkqnOcu067yjIjaQXowfvUxZ30enUjClLam9p6d_DLM9uy4pmcR-XJRHYQagiCKIZNkGlaOUasYqhyMD6TDvsr5uKM03fHoJEM_5s5RAA2QHlCqBJZQnAPrIYrIZch6qH313UxAVPBokp3iebbWpUprudghUWMMVZtOELB846HigJKv3PI4nCekC9jLtVyLPmQ660bl1zC-n7_Wg138nYGH8QKTTwSLhpVfb0jfjkT_Vq5JPUQ8RG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز صبح چابهار
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18140" target="_blank">📅 09:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8wjhTPpgDKTJBWrVvLMi-zB-oKqQ1a1rsmNv0WItlYqsH6Ce4P9O9GDF9STDxHFq6eDnxL9OhEHxuknWLNIJiIWTzYN7gCFymmFwkiKUTtz8jjDEYYv0g6rVI-agMBw2US0NokSZT38JuJ1uIZ8wGKrARzYVgJ5samTpuR-t8P8Z7CbdjiI5QMP8F2l9HjoB1uIatX9QrFGFvyuvAJTM6l3GjxoFtYDZVvDIn3K1RKDi4ZL87wlZD24vlDaJncL2ODIYL2Bl2eyjF_xB8oIziS58oxMhP8n_kJ3yuYI8e7RlgGJewL6F_pnrf2CN8nTytxL0nv1Sy1rA2x8HYwELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان کشته و امار مجروحین هم بالاست
عکس از بیمارستان ایرانشهر و صف کشیدن مردم برای اهدای خون
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18139" target="_blank">📅 09:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: ما دوربینی در نیروی فضایی داریم که می‌تواند نشان‌های اسم ایرانیان روی سینه‌شان، احتمالاً محمد، را از فضا بخوانند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18138" target="_blank">📅 02:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ
: آنها هنوز مقداری قدرت دارند، اما خیلی زیاد نیست. و میزان تضعیف سلاح‌هایشان فوق‌العاده بوده است. هیچ‌کس فکر نمی‌کرد که این کار را بتوان اینقدر سریع انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18137" target="_blank">📅 02:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f817c2d295.mp4?token=t2RYQAjy9qLwVtLBPofF22DT4hgaf4y1NQhKTHbcyKAi-CS4luSRLx10dTbizyax7r820ODYXXlryQPNu5383fTzEgunvG55Oz7lJtZVkZjb8TttDz5oXgWeXnMoY9LHrDHG6yWQN7AvNVilcYW6i6p0UFVyLj-zgioSweliiMVwx1eS0bwGMZwmpyJDWVf6-nyuxg0RHNOOqkYB1F7XlE6_QAni6U-T1WMN2QpIDQ9yMFyWNoDqn1f87n-e-LmjW2UiGs2zviyjYIZUa5Ox_6eVhyRasN-8YaLDOZmxA_e1z5E1kLXfZH6sMGlm5P-c7troX35N5ohh1mon8w4KvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f817c2d295.mp4?token=t2RYQAjy9qLwVtLBPofF22DT4hgaf4y1NQhKTHbcyKAi-CS4luSRLx10dTbizyax7r820ODYXXlryQPNu5383fTzEgunvG55Oz7lJtZVkZjb8TttDz5oXgWeXnMoY9LHrDHG6yWQN7AvNVilcYW6i6p0UFVyLj-zgioSweliiMVwx1eS0bwGMZwmpyJDWVf6-nyuxg0RHNOOqkYB1F7XlE6_QAni6U-T1WMN2QpIDQ9yMFyWNoDqn1f87n-e-LmjW2UiGs2zviyjYIZUa5Ox_6eVhyRasN-8YaLDOZmxA_e1z5E1kLXfZH6sMGlm5P-c7troX35N5ohh1mon8w4KvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18136" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرتاب موشک از‌ حومه تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18135" target="_blank">📅 02:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c274513f5f.mp4?token=ObZwI-6Wvv3nO5naZvMVyfIf8OEgyJilY04HDohZ1xszKAcahX0anF66puKZRKELW9kjYHIS7KuDJODaRfFo8snwkjWT2K3Cyh-6F0eWLqk3YlKSNeFleKVApIVkpxp7K_m30zlDXZRNoXD70yxXlDQY7CSr9lbwpXnOAsXAMDoBYD70uQc6ZyTQYpv2Jk5du82QjmDR-46tt8IlBWRHpxZ0FLN1mPO2w1mAOAUizy24DSpzn2heirtvwib_-RDVU6bJsRNouhUD1Bp7crVXQNIB78I2mlOrVVF6SVYTv95_1wlrgb5twkNragK5FmcOg6QNreh1vZOSJVR8-zAo-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c274513f5f.mp4?token=ObZwI-6Wvv3nO5naZvMVyfIf8OEgyJilY04HDohZ1xszKAcahX0anF66puKZRKELW9kjYHIS7KuDJODaRfFo8snwkjWT2K3Cyh-6F0eWLqk3YlKSNeFleKVApIVkpxp7K_m30zlDXZRNoXD70yxXlDQY7CSr9lbwpXnOAsXAMDoBYD70uQc6ZyTQYpv2Jk5du82QjmDR-46tt8IlBWRHpxZ0FLN1mPO2w1mAOAUizy24DSpzn2heirtvwib_-RDVU6bJsRNouhUD1Bp7crVXQNIB78I2mlOrVVF6SVYTv95_1wlrgb5twkNragK5FmcOg6QNreh1vZOSJVR8-zAo-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران
:
‌اگر به تنگه هرمز نگاه کنید، پیدا کردن جایی که آنها چیزی دارند برای ما سخت است. باید جلویش را بگیریم.
ما باید آن را باز نگه داریم. من قصد داشتم هزینه ای دریافت کنم، اما در عوض آنها ترجیح می دهند پول زیادی را در ایالات متحده خرج کنند، که صراحتاً بهتر است، زیرا من ایده هزینه را دوست ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18134" target="_blank">📅 02:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ
: مذاکره؟ نمیدونم شاید بخوام شایدم نه؛ ولی اینبار رحمی نمیکنم همه چیزشون رو بمباران میکنم
نمایندگان من همین یه ساعت پیش با ایرانی ها گفت گو داشتن
بهتره تسلیم بشن، چون چیزی براشون باقی نمیمونه
آنها دیوانه هستند ولی ما دیوانه‌تر و قویتر هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18133" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هم اکنون حمله موشکی به کویت
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18132" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مجری فاکس: همچنان قصد دارید جزیره خارک رو تصرف کنید؟
ترامپ: نمیتونم اینو به شما بگم، چون اگر بگم، کار احمقانه‌ای خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18131" target="_blank">📅 01:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار در‌ بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18130" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجری فاکس
:
آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18129" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Bitcoin 65000$
Tether 184.000 T
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18128" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به گفته فردی آگاه حملات آمریکایی امشب به پایگاه‌های ایرانی در منطقه شهر اهواز متمرکز شده است که این منطقه عمیق‌تر در داخل ایران قرار دارد، برخلاف سواحل تنگه هرمز که بیشتر اهداف مورد حمله آمریکا در روزهای اخیر در آنجا قرار داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18127" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجری فاکس: آیا جنگ با ایران از سر گرفته شده است؟
ترامپ: خب، فکر می‌کنم شما می‌توانید آن را به هر شکلی که می‌خواهید تعریف کنید، اما قطعاً ما آن‌ها را به شدت شکست می‌دهیم. باید آن‌ها را شکست داد.
مجری فاکس: آیا می‌توان به اهداف خود فقط از طریق یک عملیات هوایی دست یافت، یا اینکه این امر مستلزم یک عملیات زمینی است؟
ترامپ: من فکر می‌کنم که اهداف در حال حاضر محقق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18126" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به فاکس نیوز: اگر ایرانی‌ها برای مذاکره جدی به
وین
نروند، هفته آینده به نیروگاه‌ها و پل‌ها حمله خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18125" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به فاکس نیوز: امشب، فردا و پس فردا، ایران را با قدرت مورد هدف قرار خواهیم داد و در مرحله نهایی، تاسیسات انرژی و پل‌ها را هدف قرار خواهیم داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18124" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ : حملات به ایران تا زمانی که من بگم ادامه داره.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18123" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پیت هگثت: اگر نیاز باشد حملات به تهران نیز می‌رسد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18122" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش از حمله موشکی سپاه به تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18121" target="_blank">📅 01:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارتش جمهوری اسلامی :
در مرحله هفتم عملیات «صاعقه» با پهپادهای انهدامی پایگاه الازرق اردن را هدف قرار داده و محل استقرار جنگنده‌های F/A-18، ساختمان اسکان و یک سوله تجهیزات ارتش آمریکا را مورد هدف قرار دادیم.
در این بیانیه همچنین آمده است که از زمان آغاز درگیری‌های اخیر، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه‌ها و مراکز نظامی آمریکا در منطقه انجام شده و این عملیات تا «رسیدن به پیروزی نهایی» ادامه خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18118" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کرج ؟؟!؟؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18117" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18116" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کرج ؟؟!؟؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18115" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار در جزیره هنگام
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18114" target="_blank">📅 00:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91267f7421.mp4?token=i5eaGoSJEk5nI9thQ8A3ilVor-7wPYRAVvrdkD6stb-keosOzqDx8HoaDY1VLbdzjzEFc1Ox08JuKIPDjOekmuq5zBMbCCaCwHM5ve6ZZsI0WYXBgbkZaznHewEUsh_meNE32D-LJxlxAtWeoFSKwH2oFAqTxGrek5KTqxkCeRfYMv6ruGtmaRwr_NaRcBOvtpAxFZ8G2RtRPF9tqcG5WyaAwOcf8Qe5xtjkPL9VXeD79u213CYk-86KXC1mZxyv6JiUH8E56DYSTlTQxylx9lyVyuio5KuZxcjxffmtgqmfQfzCbLAwjL1h4tRYoYXzmF2Wn5JOy8c9P-S4DPTG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91267f7421.mp4?token=i5eaGoSJEk5nI9thQ8A3ilVor-7wPYRAVvrdkD6stb-keosOzqDx8HoaDY1VLbdzjzEFc1Ox08JuKIPDjOekmuq5zBMbCCaCwHM5ve6ZZsI0WYXBgbkZaznHewEUsh_meNE32D-LJxlxAtWeoFSKwH2oFAqTxGrek5KTqxkCeRfYMv6ruGtmaRwr_NaRcBOvtpAxFZ8G2RtRPF9tqcG5WyaAwOcf8Qe5xtjkPL9VXeD79u213CYk-86KXC1mZxyv6JiUH8E56DYSTlTQxylx9lyVyuio5KuZxcjxffmtgqmfQfzCbLAwjL1h4tRYoYXzmF2Wn5JOy8c9P-S4DPTG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار پیاپی ،دریابانی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18113" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مهر:بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18112" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امشب ری اکشن ام پایینه جریان چیه
🤒</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18111" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مهر : جزیره قشم مورد اصابت پرتابه دشمن قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18110" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما: دقایقی قبل، صدای چند انفجار در شهرستان بمپور در جنوب سیستان و بلوچستان شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18109" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسپانیا هیولای جام جهانی را کشت صعود به فینال جام جهانی پس از 16 سال
فرانسه
0️⃣
-
2️⃣
اسپانیا
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18108" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرماندار سیریک، مهلت ۱۲ روزه برای تخلیه کامل لنج‌های تجاری را ابلاغ کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18107" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شیراز صدای زیاد جنگنده رو مخ همه رفته و ترس ایجاد کرده
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18106" target="_blank">📅 00:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار :امشب آمریکایی ها فک کنم قهوشون تموم شده بود پادگان ، بی حالن…
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18105" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار قشممممم</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18104" target="_blank">📅 00:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دو انفجارررر بندعباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18103" target="_blank">📅 00:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3QK4jqkYfIRqDEQc4pcXkzT6mJO0rfbf5y8Mbv-fbkSUH7kUULKI27NDKuPp-Zgpp9uRfnu62ifySld91_wPlD3ayefFEeLqHyRtzzwZEJVpayJLlLV5n4NTyy49YCGBd552Xc12S_oxQTcgBujMk2-fMoftC3XODXqQVzAuVZu9odpwuM9hgoxwR_fdknwOhhQwzMeu3uwPzg7UDJu00E9nR2Eq4xekCoK96iXNrMehO9KihjzWJbSjNPMuBcyDLAaIBMSrM8c21bxWqwtuctHKputfSeTTQaowBEaGurN4yWx2uTY4EhBViULOoQcEljyX5ZPSzZDZW6HoFZIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه داری:
رژیم ایران با فریب زنده می ماند و شبکه شمخانی یکی از سودآورترین موتورهای آن است.
وزارت خزانه داری زیرساخت های مالی را که به رژیم اجازه می دهد تهدیدات خود را به امنیت ملی ایالات متحده و حمل و نقل جهانی ادامه دهد ، تعطیل می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18102" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات امشب در شب سوم تا کنون به این شهرها انجام شده است
💥
بهبهان
💥
بوشهر
💥
سیریک
💥
بندرعباس
💥
اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18101" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمد مرندی: ترامپ برای هفته‌ها مخفیانه در حال برنامه‌ریزی حملات هوایی گسترده و تهاجم زمینی با حمایت دولت‌های عربی بود
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18100" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzC8TEbrDuU2Nv3EvhKg1HeQGLicRZiUE9hzHNw-6rjQ1KkHu7ku_IYlwhEJeMXo3uXG4eKIhC7ktocsozjo8SCwrmLfXVxXCON4N1S2ESJkWDhcFWCZQuulVWU-PNDuhuoLDqkykMg7uw0k7298L4YRz_4oB_cQUVoC1Sp78rJzcixfTMv5PbKjr-0dlpHScCD5W9nU2ZPRboEx5FM9CH-t_O6CtpAkmb6DWmyxF3nWEN3WdCGHbGhxFpk2ajuYKKeMuCN3KDQb7frsqPqU8roGvy_x_VAcb2Tjy0BbxaocHErjeqieZ_dYwYC6BFRCDzQcl0vf0wYQZ8NzgiajJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق اعلام سنتکام، محاصره از همین لحظه باید شروع شده باشد.
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18099" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18098" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) امروز (۲۲:۳۰ به وقت تهران)، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده…</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18097" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یاشار بهبهان بازم صدای انفجار اومد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18096" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اهواز همینجور میزنه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18095" target="_blank">📅 23:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بندر عباس جدیددددد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18094" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سه انفجار سریع و رعد آسا به نوع پله ای سمت صنایع بسیار دهشتناک
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18093" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آی‌۲۴نیوز: مقامات اسرائیلی معتقدند که ایالات متحده در حال افزایش آمادگی‌ها برای یک درگیری تمام‌عیار احتمالی با ایران است، با منابعی که با واشنگتن در تماس هستند و برنامه‌ریزی گسترده‌ای برای بازگشت به درگیری‌های با شدت بالا را توصیف می‌کنند که ممکن است در عرض چند هفته رخ دهد.
یک منبع اسرائیلی گفت: «یک جنگ وجود خواهد داشت. تنها سوال این است که چه زمانی.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18092" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اهواز رگباری میزنهههههه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18091" target="_blank">📅 23:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پدافند بوشهر درگیر شد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18090" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvIktTCEtr3TpyxDhbhpD2Xtr-8D4EtXSO89HU239ESfQQzjM8grrCg7MmiqOrPD7om7OMAmDePdL8yE2XX3OPVeq_Lb1d9EqAlUFwYhSyji1W7h1LHqvlh5gFjI3Wl7x-mn_GaDJT1Z7vLJeH0yyZ9X32RNvsB_gucRy0xbMffEW1pUSxY9O_aQD7GGlKItIV6IrWWcNN7sydufq9WTkdwk8mmh69jT_yp1nvkQ1AacTLekGDf5ocsKuC2v5FgR_SDlXE_uTmWAZ9g0fttgmzMyXfGyIrSWy6T8k42ZnIwPq_i-xccqsXP-hKkeoRUp7Pd-k6YuRLcYj4pIkXJ2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین عکس ارسالی شب سوم حمله : سمت شهرک پیامبراعظم بندرعباس
از لحظه ای که علام کردی تا الان
۱۰ تا انفجارو رد کرده
لعنتی معلوم نیست چیه پشت اون تپه
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18089" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سیریک رگباری‌ میزنه با صدا فوتبال میکس شده
🥲
قوی باشید</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18088" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فیلم و عکس هم بدیدددد</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18087" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجاررر سیریک
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18086" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۳-۵ انفجار جدید بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18085" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اهواز چند انفجار جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18084" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnTLegt-LD7EZla1vZbbMGpn-RpT1tnSPut4eRkdMLmVTby8-4XlApH5otfe40kw-oAiZATAbDjxvxPYX_hnIjqEJwl4K-akSE3mTu6fg-v3b98riislfboL9dignz2eC5Re2CntH2PJJm_mK4tUomvPO-f0Ip_MPu3jJYDKs3SRWSGOxkb_brq7IGZdVpA7k6NE8TKWqcsCSyB8_1lsCkKFGNp1aQ5mKUrqbSuWfyGKap6Tfs08xyYlVY2xoCRzlE5LaEy5Un5j4oa4iVmAZxAAm4VdSE1vMFzK4YdGeyYW7TH0IwXt2xMrvOiXM5US1PitsUL-bG0r5B3wZfahPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۲:۳۰ به وقت تهران)
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده قرار می‌گیرد، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری
محاصره دریایی
بنادر و مناطق ساحلی ایران آماده می‌کنند.
قرار است این محاصره دریایی از ساعت
۴:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۳:۳۰ به وقت تهران)
به اجرا گذاشته شود
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18083" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سنتکام:
دور جدیدی از حملات هوایی علیه ایران را آغاز کرده‌ایم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18082" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش کویت: یک شناور متعلق به نیروی دریایی کویت امشب مورد هدف ایران قرار گرفت که در نتیجه، چهار نفر از نیروهای مسلح مجروح شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18081" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شمارش معکوس و لحظه‌شماری رسانه‌ها برای آغاز محاصره دریایی امریکا علیه جمهوری اسلامی ایران:
55 دقیقه تا از سرگیری محاصره دریایی آمریکا بر تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18080" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۴ انفجار بندرررر ر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18079" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لشکر 192 اهوازو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18078" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18077" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۵ انفجار اهواز
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18076" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18075" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار در کیانشهر اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18074" target="_blank">📅 22:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وای نت : فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود! @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18073" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۲ انفجار دمشق
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18072" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش های بسیار از‌ درگیری پدافند شهر اسلام آباد غرب در استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18070" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رسانه های رژیم : دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18069" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqt-TJq_ao-lPuHuaA6eXiI6_BJVUuRQKN56X0jskz7ePb0njnc2ivC19az5ogedFay3SNP8IRY8XM_W9hPRI1SZA35nI2ejTKR_JPlyWxpu_4XDMJnWqBoT0wVoBZi3meEhibvcTWb4lmiEv03-uWkZ92MHEZLE-S55Xfk-MhbgeGu8XHTy47sRN0bvzQs6iaghgJ0L8oWlYF89uuqPF0EVpqm5PJAKcz71j6VhXBq-C-MY6-6_ozTd9UAYOpSClmUCLM6Owl_GJEs2xNgwfNPZfDyiKtxB1axaRBAR7NwaNeHzpzISzJP9DB0vUq0-lg8Mb20eNYpENBcRmQ_I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار در‌
تاریخ
!!!
یه کبوتر جای درستی میرینه
@WarRoom
🚨
🚨
🚨
🚨
😂</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18068" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آموزش‌وپرورش : دانش آموزا به هیچ وجه نگران نباشند ،حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن ، با خیال آسوده امتحانتونو بدید.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18067" target="_blank">📅 21:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کابینه امنیتی-سیاسی فردا ساعت ۲۰:۰۰ تشکیل جلسه خواهد داد. @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18066" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سی‌ان‌ان : حداقل ۲۲ کشتی تجاری در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18065" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=d4UXgYkFbGGoSmzTuSJsKPYdyFiXrFfRU3QinR8fvMIUzbomLKAmY_JAkwQgTdwBuhdEEWtuK4Z34r-3_UgGyDJgFRmYg8cFE5DoX4GGa5il7a-BUSWeT5NEkzJBOdqiwpYB7tRmqjwe5DK0EM5IqVdZfxBhFpznA9Mq-DjhXv6ez7N0eHmmRfK3Nwv7al7LxzrLrF-t0gG0xuOBpvaHGjllcvVLIX4xhkNhr4s5q6cMtyf_T8jGv1ntm9xbggXUTCyKly2qBn8Zx0JGFtqEB4sZCTKLeHEiDw_ijl9kP238EfS2GfVOt0iOGxBmi1zyceFpMXtPqTSKRUScF1tdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=d4UXgYkFbGGoSmzTuSJsKPYdyFiXrFfRU3QinR8fvMIUzbomLKAmY_JAkwQgTdwBuhdEEWtuK4Z34r-3_UgGyDJgFRmYg8cFE5DoX4GGa5il7a-BUSWeT5NEkzJBOdqiwpYB7tRmqjwe5DK0EM5IqVdZfxBhFpznA9Mq-DjhXv6ez7N0eHmmRfK3Nwv7al7LxzrLrF-t0gG0xuOBpvaHGjllcvVLIX4xhkNhr4s5q6cMtyf_T8jGv1ntm9xbggXUTCyKly2qBn8Zx0JGFtqEB4sZCTKLeHEiDw_ijl9kP238EfS2GfVOt0iOGxBmi1zyceFpMXtPqTSKRUScF1tdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لانچر مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18064" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فوری | شبکه ABC به نقل از یک مسئول آمریکایی: نیروهای آمریکایی در حال حاضر هم حملات هوایی را در ايران انجام می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18063" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: حملات آمریکا به ايران همچنان از چند ساعت پیش ادامه دارد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
یاشار : بابا من میگم میزنند! بعضی نمیفهمند !</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18062" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
