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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2zXmYv4UNtVEVlNhs7y2epldHE7SvdkJ-RzVXBtb6UnYpSciEwg4jPaGRiQ7ldKeXDe7Fa7IaAH8Y0lDGYhd2XVa5o5om087yzOU-loOtdo4XVfVjtHKDguBa0jpSd_Uifcv4ADwF94P46K815bnXL34AKCjJn8hEkTa2hkzLge9ug3Pt874L23y3sw2JXC2Vw98B_Eabf-4Iy8Sfa3hwyd6SPyEKWCarhx-j6iBKXl74Tff5V7OagExX8fVpi0ubsDQhnE1dSOPy7js-fgomlAms5wmn9taifH-VIAQRFb5eEBpEqHa0PgaEv-ulOOzdW1WUSAU4rEYHi92iSXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZR0u8nTo_tmX9BxagFy2VNmiBjC9RuBxOhyPKDYjHq29SRPzw8ek3n_vJWi52HFtWoD3D37rRvJzOwKvuuAZLxxSWvYNBrJVzRhSqSObdzp7g6zepGw6KD595V_BQqHbptD7D0260Z7ukq9GlqUYo5pxIUggHA0U2q9ucxfu_iBR02rbtose9c2ANiz3EptvFn4IWUF4ZHhIgAdGQZsOt3jDBrEO3Ezt6GVa6sHhuT3rIGVUGssgUKt2JxJgJ2go7tF7Oj23xDxK75N5IYYz7h5pWlt7GiHOVjnwn9RBWsqDO3lcXbxFcnPtIa7YvRXueP_rZnygprJ6fCxU_vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین‌انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22773" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsElsNA9V7CFN2_D7p9Rx0q3xo2ibCxGzG_Gv3axFj2_bkd8rMRNg0q_5iJntNqOdb5WyVzyzWyNSKB3efJN_DuFDgyXagrb2TbUQaieq2Zx-oKJcp4z2JWGZ2GX-Oc59Nc-rblOye9RsfpX2XOeue0znSoJ2L-1XGNbhQe5HzTeei8TU-wXBcUiRjs0uHWsmKd6TRyvIf8xl3gPlkCc27M3Be6xHeX-d_7spde4A3VrWcGa4Tsa4tP66ulSGM6qAfw1iXhPt9_AcKHuf9hdFsZg2NfLYZsq5GmU63j3UtsOpdJKWQtzFUnlUkUC8YSg_eUajZOayVFShyM3VJalaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJY7nXhfLduGfduPaTBgxVjLVqoaC8LG_o5Q3eYLUxNL47dyBntYGpDAmIzN8V8WQL3hnW6UDY5_ERppSYqs0_1c3HAkrFToOQ7EVpgMzDEjh92kR2SlVouUx5bFDjh0mUXcNeZvG7m7MqQhuiQ5gVWrsUjvwQacsRIEjmpgWZCkqYg8hhO--EmaEg4I6m6Bb-TyDkw4OMYD8OJ3NyZ5l3vDj2bCs9-cnHfKejd9pD0bQeuuSkILb4mC8gPzA_waWPyUaIjRBMRRRs_HXNpboCqatqgH1xNHfo4kyn4NSreorTZOesMANOBXsaHT23jhGbn01vLAGmdQEeSRW6cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI5vC0zcRhMAnsxHcqvlrO3_2codGMWwNKMqBSmKomy2ote9pSxxlLHTMDuoW-pQZmiO0saogGu4dU8_O_q9Gincki02rMtoYx4bDpYa9gXPD2ecnlSnZ5QdolNkd7TfPg9uWecvDDANE2K0OpsE5Uyw3-3QhK8bVEN0_UGvwA2cMwBsPjfkcP4qPoKQ5xlCF7w9ZYOmkgeEQcABZ8qybxj8OwDNTTP_cZwMGDFC_ymKh-WlqM6HDP9VLpai66Uz6VG5q7T-1RpUQJXKarvixGhkLcDzMvtA8pWFk0t3Zh8Dnya3Inidb8oS5nKVjnAuKUpxxG3T6nPEn9sPTNcw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etwe8mqwMf5FRXkAeU2N1wIlWHFGfdNE4sJXz69Sn9ubIqo2_h0DA_eCjINIqNuDUL1Eo6L_qhkdDlfBLbisbOA2FQIZvup0-fHSjuFA4H9jJvAK3kmpDwm98pegXohD3U_cVa5J1p7mHfZnbn4guApqPCKxz9keECOAarZ2t3VcO5naksex6K077Js2MZc4jpR8T1ByLuec3WxUjAI7av_BwTZr7OF2OcQUEmhCwODIZtn265DKPidWOnlMZVGkP5Rfa9BUhe6WYp3E0rfPH_L4Kx0CKKPf6fTROkpJTMeLATku0hLbgi4XCgf8FGRXd1d8hl-2nycmM9J3cEV5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq_yUa7D6ejNJxOLsZy1JbpayxQ-amh3xGMJ0-tfsZoc3vzl5YcVZgSu13rpZK6PEt2LJOf7gO2Cp70j6--nH6mD8QTzYJBhOVOynHOeU7bffMIl_seF5rC_obEWfF6rw04CZGyKSVWouXDmoJ3kNR-st9q5Jxl63v6yphsndGlLtoP8RxiQsenVuSxlzHbJQJ_x-EgUHqkF1lpNXlXRyjwCDI543y0hFSdnxrUlytQQ_-dwiiSBHJLUyF6mIyrpCXx4YZLJfkIi71-3OL1s3xbNyQVke7LZd6jpXdMHz2vbPCFRM2i08g0QugEF6gdbTfHwniuFRlA6XsSpanVKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlXjk_e5mI_VvSFCG-Obpn-RVz9PQN9UnCGVP5l-7bscJnfv452doLKLGUvaB8auPEQnTN_L8sZWpTfxEZDRP9Xx6VqGrOquSpan5PLUldtdJgZz2iaxiq1LgLA4ukn8b1UN-h4lTnMl06IW3U7pXyf-BKBQdm5jnZkg4Zz11wiTdNO7Lxc8UMMWBVAtsGRtKXo9DpexDdBbM6mGD5wuTsXgeUSFaI29HFbXgln5j88dyFukTZQo117MrxV4ILCW-PwAz5Lg1BU9sRsVmS0aiZDPbdnKWs3kfXj0iDKjt-b-fXMII__qf7KFkEBDXOV9D2ppDIWokjIEskhPskaLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRIEXAYc0iqbFMf5M8T3-y9yvaSANFJ3jtscrD70QLK_h65aWnrGU736a-jWWEDaWDHIY82NwPymt7SnaJ1C7Y-eVOU0nTnx-L2L1QUEnF5-zmOtnJS5XexrXsJYeHQKkdxXEHte19lizjhJduQk_k_d1DKd1WeXHWm4zIUs9PSjCC4z9GxJg9RqQ3lzjK-wtjTLbjWSkFvsTmfx_G9EUP2Stl2jpDAw18TQF1fCnJl67uv_4YV_NNt7Faf8G5F6dAey6xbjZP7CCvQMgzhFk4XRKP1DZ2fEwXcwpNtySQDPJ6tgCfrRvetDDdmIvgzoVhsTBXjjFx2xlWubTnQZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5-D6zbGpzQOD8TnOusEVY7X_oYiXxO_YMMFwfCSw4FRuFRy9FJSY0BJlVaB6JsibrEvIRxmzN0MvbnMMDj-lmbIJkg7z_wW5XV1ZtriKhxX_9N7SSSMCjg_f4t1-vN3UwBehxbOEBTulYc6bNI36IamhagE7fNNIO7KB5EQI8HshPeoQ7Exx5hexxS1_DFHfItepbIkVhQpAusBB-G2AIggWpakchu4JbtHNQ13rZKmxADOm-Mdonds_QDx4LQHRcO7V4yvZyxw8S_R5XvgyBZ3VsQ7Ce93A-6uHdwzNDk-2zt6sonyt0G3IaPx5D-P8vKA9ZsRpfMogdHFTkGPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=pf_8wgVXGcKU9SvtgndGVaqWway17EnoqOLz9jH3lOKp9fXpN3d0V4iAgUcPrV0-mcBAD6If2Ne-uj02lYT2ZcWLbh-WJbOzScAOIYNITRJWttlu1zFFchr-3E0VyLxETocR68-7jQXp_awHp7-dTbv6m23nEdWqpoCke0K5NWTg8F_s57vEnNbboUMSmIk5YZwq8YJ18o_7-Rc5wMZ5L0zV8JUn5a07KVJfMMfEGRiS1lJTBuOtsiMKnjSYliav8VlYhvEaAiMDJQrljFF8HYmOTzPNaXcdJPWJVlIVYbY4npxcKAd3ux4OY_ANNvEifWsD0RAxTFWbeKO54HpUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=pf_8wgVXGcKU9SvtgndGVaqWway17EnoqOLz9jH3lOKp9fXpN3d0V4iAgUcPrV0-mcBAD6If2Ne-uj02lYT2ZcWLbh-WJbOzScAOIYNITRJWttlu1zFFchr-3E0VyLxETocR68-7jQXp_awHp7-dTbv6m23nEdWqpoCke0K5NWTg8F_s57vEnNbboUMSmIk5YZwq8YJ18o_7-Rc5wMZ5L0zV8JUn5a07KVJfMMfEGRiS1lJTBuOtsiMKnjSYliav8VlYhvEaAiMDJQrljFF8HYmOTzPNaXcdJPWJVlIVYbY4npxcKAd3ux4OY_ANNvEifWsD0RAxTFWbeKO54HpUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8YLvBTeOREj69O-r5p-gpMYJDTOW3wjdMbH-BF2LBIu2h1oK3I4IQx9PQ7h4y5ovHsz54xFQkSUdwlIrZL1oZ4MnTnoMrK6x-o2Xc2tJg35AuthAP_SQLWl-CnO-OF6wqPYngtoYkRA6X3Qbu0VHU_K6rQTM8rHnnQEUswCuc5jfIZHSoilZ2J6NcuyjBBylxtYExlIq_qX9kG5sB33e-_aZsE4AaftZS2AH5Mxzane2WHk_O3FE1m8ekUvD_bivyqtZyHQLs_Axi8MzDrUggaANImmlsvYwBGEX83oyC5x9A5i4RAwhBh1saVPfknnJ4N8FsYX07m6oVYaximc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqU0SdUj8bAOoPIrWecE3q2O6hXkj0gq5jnFbhw07Kdpjc7jrJkw9QV_hX7s_DKwkKKt3T1iyoi8HXmfAwvIOORGR7IxhaGcg-2gkN9Tg1K_WCbMCLZO-mZp7uI1Cw_-xMMISfwHnvwc-lCLDz4HSb91bNB89LYOgCpZ9v3LEylRFeIvDeTrd_Zba8CuAVadARj_Ny6F4L0NK6XNtQfaDbGmrKSSsCD5qtIUtnsNwiVFFBIKeYkgTOUL_6VmM27bQ4S_qhCfk1-L4lurTqiLv1xs-7eSTTT-31aHSFrIfwXkjeAdaeOnr35X_VXZXC-3gJjHyBcIX3y498an4zp5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izpCxORfiHSSCdYM8_pYS55rNIwuw0i7LxxtWTohthhKf9PTfmCJKDlh-ah5f8-jDMXZaDjCAxotfZMOB4rdDi49rKji9B2W5kzhQdRs94sk7P-fRFVUCEurBUwnS_yfqN9JAuwW6UXniS5uWjYmpNxGAbsSuKy3QuAUca896Y2ABC4Xyqho0ndQlDInYwEmRVrZWqXMMNnhQAa0Sru9cQvMprlIyfAmJvmmLH7t0VgmuCGPr5PxcTpYE0WvUMhklxpcyaM039B6_NEIPKBkim_Ll02VweZfGmxAmb1qNwhTRWSwqCWf4gUkctmGDGA3C75XFdKEoY4E3wqbWVnnrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpBx_-tphgRAucMo4yt9hPBgmSfl6Vb0JkuESILKlnZh7n6DdgMMiIcLXHRviNY0oFEj06fMJTD9Deo7Pzj6dldc6avARfEOPlK9egrYaHWRLslksD3xaU3OTbFux7iDts-yUAmK03L_WL7xCb76De8AL2F3LUAik5lMxfB60-ksT5YV4O6zAer3kQgBEInJ01k-RnVGgPa0WuRZX8qxNcx-LVLTXLYrzLnrrz-IuApQ7c_L5Y3d3tArcXi-ugr6AZ_4WAIvJHoRXQkjJktm2qhD5fyzigZUZRhf8AduNJ4c-mzjGkg8itbj4-mWSuVUEOE2l8iaVXevf9nlfWYMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onQLbnu-UE9wG5xRf5QgL_KUghLO7Z_BIMVCRKxqR1WXRMX73fH3EnA2Gr3xLazbx50088lb3o_0hB_NAuvOO0ODdNTkV1LP2rq5MIYiPN-LOqn0_YRwMmlfI7p0zyF1YzXeIVeZUpGCtg6qLrxb_abPWDUu7WUE31oTzi5FFeOp54GWTGgF5uPj0NOTUxfJHoEOhwn503lCH7nmHuWUzxJP_FElmNn8dRMyI57ql0DVqJvZTwjvTgIL7jJMDsWbcRuVfPgDHAqxjmRqZnOxc5UUzv8lPQPo8IIQbzBHlm64nrTgySHstmQWXJ3It4qJ-Rt__VTj_wAtsoHR1DTPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftFLiX0iB_TYawSVdlQkraHKfOG9bGJXEbv51ndGj6JC0jXRCkEcLVc4Hy2dh1PVEdQ-cJ3oK56lDg4R3WbtMFUmVxplgIj8IZELfqVYytsiUUpVk6IOfBueLrhv__naJCXorUD8L0qP28FB196hoUIoVMq6nPgf3hpZX0XW8oWaalGdWnbvNcj8Wzkggs7YX7_OJuRoa8Qo1V3QxYUN7vyWYPJHhwzrmF8OgUBxwEbemcye8R2fzK5z__LV4n-iFwv5XAU807yH66qfdEaU8I0__yCAtuBegUIW1hQbT6vQAkX53MJW6xZLwQSrdSmfzBnifBY4VOSl5BaljzADsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN0aU4gSyOFiV3h0siBjdbaonbWzhkoE-g8c1V5D5Y3bApmRmYUkdZHI7clUSBCgv5_-b1mTveGJr4aSw5SguUXIOk8YH4HIhkyBVTrqWnjc7FFgprsM8WQamcpjO9BKFZ9KeLslwYF5pudVl137OEh72ScqCcqUujkQJoADvKuvl_XQOnAuMFaaxEryruOOEIZRnfTW8yN5gEPRB7vf8TSnBOLg-KDIlgldVV2E-hp-RXDcmFg6LVVEYGX9IIwTRZBigCIdqbQ2fyK0Br5pmTqvPsfsMBkgQVAM85o94-v6XyHMGOjZ122SVg67JhXAGh2tfZreVjRNrC_on8x_xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=QeyXbkjHLYFTTW5ddD7YZHF_SIEWvsfYbENkkQZGQTrHEML2pqkk0V0xVSoWw2BajBBbLJNX1pu2uRFE-Oq4EZM1tMMrx2bNowQoFeT7KPOwdC2osZk_oznt89dra4iafFPNHL-jP8jxacwel4jYT9LiZ6Y-vcaNlbtvAnrMh-Ygff3Eu0b_WoG8XE2UytOt8HGA10K2AsnwMjhi6SUnRDeOTsoriRUr9I6Dk2uznsVTU10H6cZllMPow8gYm6W4aPv1hkdzeAntJCxgQW594zmgzvgn9mf2TIE4zw6aW2tw6PuV4hetMhQMRbgUpr79XiIDREuomi66qpVuUCz6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=QeyXbkjHLYFTTW5ddD7YZHF_SIEWvsfYbENkkQZGQTrHEML2pqkk0V0xVSoWw2BajBBbLJNX1pu2uRFE-Oq4EZM1tMMrx2bNowQoFeT7KPOwdC2osZk_oznt89dra4iafFPNHL-jP8jxacwel4jYT9LiZ6Y-vcaNlbtvAnrMh-Ygff3Eu0b_WoG8XE2UytOt8HGA10K2AsnwMjhi6SUnRDeOTsoriRUr9I6Dk2uznsVTU10H6cZllMPow8gYm6W4aPv1hkdzeAntJCxgQW594zmgzvgn9mf2TIE4zw6aW2tw6PuV4hetMhQMRbgUpr79XiIDREuomi66qpVuUCz6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpAxYvfOI3UTUhnO2VraLhTtkPAtVyYPY2hXio-sjs-tfFui950Zu9cU9_-b_x7m0Aps_zx2fBbxMyzvxmoG0IZbMxnTRFWbMItq3Ry0vtZM88eK4UPdjLZAYrBktGRovgDudYyytGDDGXVSLw_1oW0dA2kzm1AXaMYmOqrU7Tumfwvvr20qkWSKXw0o4h_whnV-a1eHT-NveAZ1uib9__yQKKTLlbr_47aR3M_ICVjKAT4eqRe6pYSGTqOd-sQJnL8ARBEF3yuUDYzYvjoa6MWZKtfPv6cHQMPlpVOjvFznS1Q_xskzFWq5bHcoiYYugzdUTuZhnIfPRNq60PSCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2x50O43PCYtfKIPkXJ6WatYXc0ixyWdA3sg1KvDmVY15m_jVLQAgrrGXtJVgh4EUgrDWwlm0d_b-1_tZVeRm3lqIRCHEMO4Vhe-cV5pyf7FH79dqj69ZQ7-I_LmEAjtdzZg88i-URARqiRims37ortpbS3KxavgscD-NpA5MeUqQ8MdS1Nu2jYD-B9HX2H5GR6JEECJ3chj8nxHqU1Idg42XYTjynO4h2Ow2SevjSFQ7AkmRrcUwCFojpWY6sN47f-1NOaDzqjjtKbhX__BhpEOd4oQ9lKRMXu9-Lqv_cWbcuhUZTf4fztB39NYzYFiK8s5GDC0Pv4nsZw3WNa2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEqn14QKzLZ5ntWtTwV9SS1vFpf_UQ4wrRi9hXYY5zIjgRq9SN8BeWFOFuTRf8d9X25f7seISKLmra3j-a_6IyIoJp2dN0i6OvKWLAIYz3SeZnjlLwTNF7poSrcfGtfeXxEiiU6cdZAZAf_p-74voHYJEIBZccHwRVZl9aKG-eb8u_XH1-d5OKXYOWrFWACuiqlPEQYVRe-9_qVlSg76a-cLCX0m7b_kfUr0F-ra_MS9FgLRMeIXZroqHoNZ-GDvFX-6I7-jxAllo6Uv9c7-z3Wrg_Z-WwFYnYPBqk5oq5BJj4lDXPSPYrmnvpR9JVH9diOG0ph37p0Bt71aOWjZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6D3du11Nyg6wAvO1nKkOdQTKsQS_rOPXdKAY6-N6o7zMZ8XBjOWt7LCz4tKPTZ2TGbS2Qk4cIE9xtauK8SMCqRcqnTUXWB1kIde0jMLj5Ku0HNN1ZjPVhJcwn7KMmGsGq8Mr-0z1e8lQOO_4h-GnygdeijqZfP8lWKm2r74-Z8TrjK6jrxf4ZZnC9ribDYcnprper8r5XfrySPo41arfRXC3BLk1wutYh8PC_2lT8FsEtoby1koMzVYDtE9GnBGq-2z-ow62u3y8ye3_JBdcetEfNZPmP6uhAw9AkQ1eQHGxCzT5IcabhH1MnIzl5PrDYvh1qrIBGFBmcH49Xcrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAqMrJcn13Qr4NE8B6zYcUlpWb7mApJakbU5uQHlCPCeRILoO6WJAlRZKlwYHb3UNDbhVQFnpe5hAFs3Zt77ezzLHOq3aZcc-w9ou-c3N-Oxoljeph8D7OTHKe-dKad67Kbi1Q4srV2XzuawxsVIQBYbJweTpdG4TGV2w0JBck1j_kXTbdL9xwj5c8q7nRaAQpXEurTItRg6cIY7i-jbeuXU2DSyqpadgFDKR4AWP6E1ThmylOKWzpU7meVOlb-fIapp9OxIET2K9nraMnAJ5Z35lEtXZcPIlbTNPZV0XmOeEcA-hVfLCphy81YY4kBueFIYdWgKfRZCR8sWazqpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvHHY8nfQe4w0xfMc7Ef2qllXVj-G4_ZpgSjuqm9N58U--iVA5QD5OfSSRP3q_BvbsZeHCIFWELjEtxX4fWL3gppg5YdcEBf8tIKw8QhAEEIEykU-IhhR5Oq-ShXED_zrd228M0PcGe8KAVqUY4EVeum6EKV3bYxtQ5tTYxCA8n_LXEE41ain7pAKAsiG0_kDwYEPgDrrRPUoz2whyYiJB0ErW0DhhkL0cb9-ZBBogEgXnR-zpEalPWKzqbJWjHE85yCnbjLgxopkjBG6UCqDWAWQmxym2EZ2mzE5Yi-zcyBqc8EC-uJG1uL-gdhQp8m_vs49cb-rFgGJiSomD5qjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=SYC4RFPFMNpbb5785b08BwU-CY87XCTq7dZpFI04_uFrx34-Y9YagSe-ENv0MYITcMT9BBN22-QGWMlvutH2mm3vsrF1THhJhuQqod6ZmGP3GSe5CrGULSXqKkZRoAEg3NfES9ncS8B4Vrg_DwW0Ws1y-rOi0ZeH1GQf-_e9bHv1lLm0yT8o2rbzccyD0eBAuwX8KloeFHpY7OCqyubLTrN1CmEb6-288GqEJvhFJCp8CW26nLy0OXCjgyckB93s3ikITMRawQWyT64T9ysPA1yZ6AzNVd-y7Io300dG9ea4-N_SalgJeIxNijTonx2-50ETV6BeTQq7f-w5vUbroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=SYC4RFPFMNpbb5785b08BwU-CY87XCTq7dZpFI04_uFrx34-Y9YagSe-ENv0MYITcMT9BBN22-QGWMlvutH2mm3vsrF1THhJhuQqod6ZmGP3GSe5CrGULSXqKkZRoAEg3NfES9ncS8B4Vrg_DwW0Ws1y-rOi0ZeH1GQf-_e9bHv1lLm0yT8o2rbzccyD0eBAuwX8KloeFHpY7OCqyubLTrN1CmEb6-288GqEJvhFJCp8CW26nLy0OXCjgyckB93s3ikITMRawQWyT64T9ysPA1yZ6AzNVd-y7Io300dG9ea4-N_SalgJeIxNijTonx2-50ETV6BeTQq7f-w5vUbroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=jRfOfkAB31OElBOiNUKM4FsJGxFQIbnIJ_oGbcgfRK6Ib9wv84fhyU2d6y7mIPY0qAS8j45DATnGgd5Iiv42klQzTslkNdpm5y2_Q6KQ_QvSWQq39mPOHCkIXjCZ4ZnnSu_BOF1bKjubMRp6_bZ2WcuKNwv7LGSqri7benXTF_qXSauKJLAuvh88r4oGBmYk3UuTup5dy9wY-efJi1oHZSvzYKH41xRkR06oXUuDrzjmh7NcN9VENkEX24qsdSJIXMtVK3MFhEoMe94Zd4I45va1v_6TpEhx3y-VRFLIwFeKbybygSnAWPYCRmcZB_x028F58uOROOmTxdfI35mzC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=jRfOfkAB31OElBOiNUKM4FsJGxFQIbnIJ_oGbcgfRK6Ib9wv84fhyU2d6y7mIPY0qAS8j45DATnGgd5Iiv42klQzTslkNdpm5y2_Q6KQ_QvSWQq39mPOHCkIXjCZ4ZnnSu_BOF1bKjubMRp6_bZ2WcuKNwv7LGSqri7benXTF_qXSauKJLAuvh88r4oGBmYk3UuTup5dy9wY-efJi1oHZSvzYKH41xRkR06oXUuDrzjmh7NcN9VENkEX24qsdSJIXMtVK3MFhEoMe94Zd4I45va1v_6TpEhx3y-VRFLIwFeKbybygSnAWPYCRmcZB_x028F58uOROOmTxdfI35mzC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNaTGNlah6IpPDaAEOX1XLSJbh3_F3drPt875VsyY1s_iRgUpAcyxmAVD9jVviiHhI33UX6n7JwsXY0N8jJm9hFZTS6Btli3WzC36H_ULoC1LTfHQfirCVhJ1-_zPb4zhmuGtnOmPhPc57cE9Ed7Ey4pcR0BqqBSrElQY-nzuMdSV_6T78kyPleK-53NwHaKEI_iccIYSOKQW7vY1Y5vlgOKoJcZ2RfmLCFVX0vfUXnfNzQwzrfvhzkaupvA_ZfHYHotgeT_dfEIxBjQO9KE8xgUxqzCbUjr_RPZwsHjdEB51o0seHbHXna2_oxXlspkIZcIhWjDwlTZWwaaOtkgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3KTCPABDDvlxi16uC6hPVnCyP6HExiQBY16NMJkzuQ2q2evuKPoq9HB3ySMiCvl2Zt3NBMCBcFeyVMUOd8h1_DnAO6vXPoTdxt4Fkc0MHXRqHQhSS5Fxe6xuOMSk3C3Rkn7WLdGx6glwUNa2S1M5INqqEv19hYXILK4nA5da7WnrUY8rcFMpxq3HUqV1XaosbXE_8X__JfPzpizRcKXRWtcqWDRg_PqHJ9D6VrjkjHnN_DZJivStADcf66mFsws0hAThh5FDgEM8T3uv4R7kK6C0ZYqU1p96_95UcwfmJDHrXIYwtYX-OAN1gydGHfX8dGKGNr95A_UUy6VSeOUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaAgWNbjyKGeFgoAqS3wam_p_uxIoV3xlL6O89TUQvADUNdCgVSqPFz9I_gOS0AAPAQpcIkz2hv_TLRfex4olL6TwMdZsyUp65A5vwLlW7d9-3LGo0ldkW3T2Tvj8F7-HpV47zaNRvquxztdjpyceIxD27LsoIgDp8bJd3hQuMSjiJ_ZyGWYmQAQx1dUTJBupZYPAUVTUt6SEJJy7ii30IPu04xkxIYtWUmTvzyrXXvZtcEqIE4FRKRoaFnCjpkK7E8IGQZo0kYNWtu6wj2P1yhciL7KWebGAgG6n23ZLz_fM4k7YOIF9OsP9OQBU2s-Behyh9fFDsVG4611mnYs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=b5cCIC2BVJqOQA0yWrdJuTjh6KXkflzdYU62vkpjbXepKPZUSS1GJ3WAsndsOEJV6Q-txOnRwyyQ6y0MRXPsv0ZQe-FWR6BhR4tnsZVxJwNJc-8S3murFQ1p5Y0aJCi4KYU7HNGer7pmG32mDmOzskIwEKdzGGmqP6FNQaW1JFEGIHelxJBTec2ag5H-hh68vx7COyokFU2nMVZrrRl4JrpGgT4rOOAGeEKMFg4Ox8GRdBbRqQMdXOjzrgNzj_u_KQY-z75TrmM1F1KJJjvAYA53Bbb9m5aVTA_eiM9WgbzWr7rJNQVsQtSHVcryGcKvnEVdiuP2E7RhqKjXpx6kcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=b5cCIC2BVJqOQA0yWrdJuTjh6KXkflzdYU62vkpjbXepKPZUSS1GJ3WAsndsOEJV6Q-txOnRwyyQ6y0MRXPsv0ZQe-FWR6BhR4tnsZVxJwNJc-8S3murFQ1p5Y0aJCi4KYU7HNGer7pmG32mDmOzskIwEKdzGGmqP6FNQaW1JFEGIHelxJBTec2ag5H-hh68vx7COyokFU2nMVZrrRl4JrpGgT4rOOAGeEKMFg4Ox8GRdBbRqQMdXOjzrgNzj_u_KQY-z75TrmM1F1KJJjvAYA53Bbb9m5aVTA_eiM9WgbzWr7rJNQVsQtSHVcryGcKvnEVdiuP2E7RhqKjXpx6kcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXSEdZIEVzTrYYsWex6OowMXyid-H7axlGBlr5UHdGvZu4bgSFcO32ygGWYXbZPxeD9XDcNrNSqdGbPslhW_Nu-csc6bLSv66acW92szlP_3pGdCKCc2QMSxIE1gPeGjS_yQ-UGZMJeg6E1RqEdLEOwIKJIlRgi10AGbMN7HOU6Oiq3x1bDpxnYpqwGjkNM7Wr1vkKZSAPQcc0iW9GRb4oUtCCs4U9HTQZEck3vUse6Bi64Vqs57zEc4ldjI8wq8xT19S7-T6HWY3bLpmg0Bv5dTee8Rd9eZHxx7KxjybW9TiqJ7pY5F87SqRpwLflpCjdI1lerVxTzFvG7ktNWhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvztqQu8RkPwXUO8xFzDI8AzrhGBkKg6hxqoO3Fh_4jV_UOgvUc79J_iwuitupw-W01Al_Q4xkYY8ExTENKOfB5e9O5JOSgOfgEvUK88KPSyiJzPP8dxwnRM11UNucw8dUGrPkxA9l1Jxz7KTlCSFTfDjESb4r-hQ-iY8JoECdTSkWar7tDmL8tqitwE0RsKd6Ey5-DZOE8AfQupnG0NmX-yGa6r1kNf1kxL-acv6_yy7480ENocaItQM5WuEf3Fqhaoa5sckyupsjE0qd-hQT-FGHGVfXdjnua-tzkNF6BhFbrBEAChiRhtW_DcvWpDtLRUvlxf0sS8-dPON-K8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re4KIXQ1e_ieCHoN4vLcZ0KPkkGaG4kWRG44UBn-zOGv1uSrMNq1oYBSQli5nu5B9RlrjXh-MfEr6tojDbYmrw6jMxkjai0yV5pDToAbLYGnLrEll-JKUDY5dw9kiujJ_AyAMNIl5AmCN5RVk_xN3wir4IMu-9WAtqjSiY27j9gfXzLpmqXYnl8x1RVQvulKrnVk8w33AQJT3NMA6TPRt0Iw5slUsso8psKZZdC9SfnI7z--r8EKH1WgZxEIzta4hULgAY26SmpXU9NpY41GaQyUZJOyCMMCn_4sq5eL_KgfWjY_xWXCDCbronn6IRH6O935whXdQvHZ_gL1sZxYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUuJAynEmYMY1ekysYomRUX6jVhqVV5iew8Te0IOKsri6_T1hpZzLIMVpoCPaEKDQOdoQLWa_AeaEE7VKZbg12lH0K2hL5LGUhv37bnhxuCkoHEUsFMF4E5pEMQ0GTKizyDfqG2cfmbNCj9Zc126h7kTBxsa354cwtEKOwdpmeTh2UT4xCyCp0iVhGR6lJkuG80bkK7y7gJYTf4HJPms2kCFFmGe_C8r-DPicsDNrjFb0I4MBuanqzGiYJp4v3dHPKwBut73zRaRoo37tCpmMYh7-PAPhxw5BJ1AAZyfOSJFnevLcOqhTt-_dHAn74B5v_klUOx09sWUbFT0jMN7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqBlBC11mMUqboVyvHezE74nZW7YoILp0zbu4glLLZyHHsgRXBhbXcbpWta0qSJqGGQ_txQqn1J1t-toSd0p2_IaoR8o2RYpojVpBITfIifij_Nt7Db_3ZrFJgijZ7A3gWTxFe63Y-8dRhcubA3JOOJZ1Cj2gdTK-bkhp5yIRdTK4jXU9oVVYW9W1RKFiCQmB_B6VEg2HmvsLQbquKdfWOJLdhddz3zMNS6xcQYvgyc6SChvmUCuNeK_3DkUrKPUXLGOm3ddQktzHarCO8svsX-cf0miKgMGnBwx3u2zE8cxaET-inPggezUpjg48a26HGUVzIw_Dj5EMiJNclQJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue98RfCPM-GEPhx_Gz21I1phj4g3QXpOdxkKLuazmzLeKC5Azb8YqHNFQwSCisfGg84Ijld6naIFQWUPGHwfZCerEj0Mw3kJJlBHwZ4Uma4QrHHhYCcOeAq4j18rD2YIwLvY9glqmnn3Ubrk0zW0e0yWSVSw195THUKMpYZXJx410EMi3eS_LGMGJy-Vn0mF-n68aKRiLRNyXFKqm1vciIvVJSS5AWGma8xTh-Y6SET2uHM5m7sCvwOX56qlCj02YGGGgK0QBnAZ9-O4jSl66bFzz0lhNTWv-6gQH05Oti1mNxHFojzx8491ukGLcMg63Tl7OCUnzmZkhq87SS_HTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGSD-Sa9xXTa7S2rdpLARXC5O7li2k5-jTOIEKIrFZ0FrJns8EEhYaHAFC0lCkq_gXojrAhNUa4dFLlMHVQ04sh7X1h55X_0yIOJdP9cYZrPwIrtphpcO6swr7mPEsMkpC038j9ZQ8G_XkpOLLX5XhYEzi6KbxmZhXgPXvX8xHn3Abtkdyz_SFGUQmbXkdVD95Cj5WtTjITkL4PAEohsP3dYwZWAQY9XOZOnK0W9Rxl-MWI6LPKD_Gr6it2NSDLJDosXJkv9ILHeKIpLaH35hi_8A0o8mQ3BgAwiuZPeczFVqmA8RiunzJ3oneZIIaG4Sjm7y2DLO4UARqgktrP2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLPO-oq_Hyps-7fHf8eIAQ8iH_VeDSKL7rZJqGsxkqXiyBMq47qI_utuS4tsG-HXdd5WDjZ4ytXDvlhC9CeZg3-eDFD2ae3hn-EcXrU5YbJua3WYtxcHwhGDwz7wdczyI8TzJgn_nbd8FXS3IL4PQvCt69A1XqzBhfiqsE54r_FRYI2A6OunjXQTukHbxx3i_ph2Y73qZKYCDWIH4x1PTgPm3QmNmK-kfXMmu1imkYRNwc5PtO_lj833jIQLMV7vD1tMiO5K22pwFVF2JTk5YY6bHN3W3kJKCzdF0-ICyj-l8SUeEMJI9Xg9E9mz3S0u4qf1xsZfnHkycKcYNprMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUZiMSv-Pg5qXIrUvIBBek5FYTsPEi9THu1hp78h2wEEjPwPzJ2FPnv5PVNm-2CbB_sbDQw8KVx20ui2t2w3597mv2UcvVwWdOlwTneKrI5e_11Uh1RFdhSuqQOF8n8insKCTMSGrkS1c7DS4oIz8BoUKsAj6gLcix3gJWdUGMegNFyPd6LZ5y_5SrsvTtAvuutpFbreZfCfYsLoIEvizIYxLZ1a8hrup9NVA5u1f1WXRVXTRIc2SCzxJlUQYqNhENbKpz0V_juGElfcxKLZ9U-I6aDEU8V1Vz7-3cBqqMQLZWoDOymxJCB7DfuRQR1GnwH9e-flFaVsFlSnl-tmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkVYEz00-yzc107RXiRqtYRoQUAKgpl9YIkCs_JNhqEGI0efWcfpTZEuFtd7RkSoV-6Wp15sSKhxhkHLAj_Fgl7iC6S9l3lQWJqmDR8Bwqp3tZKvrx06xfaSuZJo3xRZkK_9CIGjcH-afWRWYlR-8Lhrdbxd761A8flpqv0w-enDzFzqgHingmdyZAOdSA7oYyUzzPyarkjmJPe2E3LM2Y7Jhy2wtuJ_nbAgpRntwXC6JtXs6N94_jksJjET177SQKgnccvMAlobsMvyeA2T31U3T2_lqmZV3agw-TONhka0uXcy3ipbTgql4c8Hsv_UIBAiZAqrwGEmIizgJZQAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwUDB0IFCJV9wxI0TxgWMxQc_-_rxII-YJo_vX0xlRmkwtQDP0nodPmZLvBZHSXhKACMR23uE9tIY7v0djuJI_0gxLlm3Y4vkH-CWVZEB6991XdqHowL5lJjSj21G0PqiV6YUrSh7TQDfHve7SWRhsJ3d5G3wrHPscx9-0cIn6Tp5tHJ0y8Qr-2CNE3zK6c0LhzdqoBPdW2_k6oyzsDV5eJWN8WLbXlRbX4V4q7l9iCiLcS7bz1y_cmv7SyRwUv0xUL00pqaDgLgYZO__TonPJ94eDkK1W2t1_8URwU13JtZ8OCAwEj0i2oxewz8utw9ZB8l_mfPwGlAiZxwYDuvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiUjoIt8CiGyXwOxpdEJY95Wv3vhJirTT2nvFQKpP9tc6qtozEjDqPnTufR0Wp8IHpve5dsxXaXLYyTZ-FTwF_SwQ7EIyo2rK6MYFGCEb87vmW6vrH9SZkWT94GLUwTWUEYXtzNmZ6UYJaF4KXnDdfj5Dy6jMMt3UXv546yYPkSTNO4F0FvIVQsNKlar4Xwf2WN56vxnt4UVe4C_Q4v_cdaq6As0l5ReckM0ODwb5MOLVKyekuxlKZb3BmT3WABeRyJRuCf5PLH73yFcXdJPCEvf5HaACMGvch7Ez3LjOb_RPs4qMA1oaIR9ZQFrSTs-X58YcTNxhCbpA9Z9gT6xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0YZVQYAZ1DegpVFndeb20NMF3Opycr5Q81DeGF4kk3C4MG6oJhEbbSt2937_5SmwrfNiRE9yiuxRLgJkKjQEvWZWvYrTDwsggIxyMdskjVq5QOE8ADEiQLusKkLCwv3eISrm07bl9QJo5NT9FafXhqEdY_Cm-isdIQuYE9heAtPxCVJSmOnIGwNsDlnW8d4_W6luNFp7QR71BxJ_QK0qVl0gP_sjcZOCcux6KsprSqRjlTGu_PFkg1oireurhl1b11NJEVUJwpuFCVA-OMjVXXE1UepTDqBRjUkQ5aWt1AiIAWdOiyeFd--BaqW70wdEOhcTtcXaNNkcGfeIszbyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=bFDk-T_o-oFJOkTR0van-MbS-tm8UCLgr5cMROZu9Mt7kULzZOShftwXitnSWhPxpyqGN7nac6ItTn40MS1x17Vx5EbOli8_lwW_ogJnf8y6IIljmgFhySxCz8QBpmLNe_bNmBcYIs1MT6OcCoQPFY7EGTaFliAWbJBfOsb4BT3_wg38EyFoyATUVTPw8fF3cqLwiXjElrqPd1HPzhJ7ahEbHkeOC7RiaXYc6ttNkx3zRru6bQx5cxBk0nRyiFMVwBQcWwNFUltIH7PBM142QTZBFdye3sgndCcSqsW3mL6BBvmOyVw1eQnLchfwOatVreSWOTWzdnFgt5_jLqwHuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=bFDk-T_o-oFJOkTR0van-MbS-tm8UCLgr5cMROZu9Mt7kULzZOShftwXitnSWhPxpyqGN7nac6ItTn40MS1x17Vx5EbOli8_lwW_ogJnf8y6IIljmgFhySxCz8QBpmLNe_bNmBcYIs1MT6OcCoQPFY7EGTaFliAWbJBfOsb4BT3_wg38EyFoyATUVTPw8fF3cqLwiXjElrqPd1HPzhJ7ahEbHkeOC7RiaXYc6ttNkx3zRru6bQx5cxBk0nRyiFMVwBQcWwNFUltIH7PBM142QTZBFdye3sgndCcSqsW3mL6BBvmOyVw1eQnLchfwOatVreSWOTWzdnFgt5_jLqwHuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrkz4ZAnaczPdyXK_nl0T47fNajHdY3Mx2PrUmoAjelQbdqKdH1vFwLJVZbSrzhUiz19V-qlGX9UjKmCYT4anJ40LSyWxLsrvQZNb8iSMz9bbUdwj4tEh4xQO_mTSxWJMSYWV_NdrbENTLwrIBDGQjZTNV28DWhSARfgF5UZD-g43nOCKOuAtJ16O_xYTF4jZ21WzfIQtruaoTlQq8jHrx2eijcMYWyf6wOsat41KmAeQNBn2enGZn84cG7fsuKDN1Bi0qwoqICkWuCLB9dEKQasCbznKr_u-7VO-yBfg28YlpYGz3Y5wLb9GF8NQmHzzNV8QCdbxE0Ry7mxLMgnWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKQHteWw4Z6Y2XZc1gcqiHFhyVb9IiTHeDpt1IUcQrxvd2uiE9Zw0lbb6WlOF-5sfZDBb1TJSj43qVC_s2M1aw1giCVuWcowVaukZBJoTYhVRw-1KhpO6tAw1O-TEs6nqLgjVA7MbRlWD9M_JzkGoWY1M35TJnCc84tNxON3RpxxKmKpicBK6fo8fzWOrtvpqXgAd2FxmPzsBUnjk1xvZj3NmZvIueqvd1-4_tpTe2AQHH0spqLSivZbb5QEy2NMlI-8RMbpDdPmx62CqVrX8Cu8n4QIaPsTKSsDNHYtsFESykyAhSDPLa1LX42xNLwhXMMvQIQMLghmb4zMiBXn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=cNjZ1nCLKXLOdRaVj2Ep-7zBmoGcdQbLckrGC4YPATu0oDvMFDuShIsr8wWCYgeBfWeu0tltlT5nF4duFXuLJOVuUwtL46yZtaax0KxLJFMi8RytiDH7_nqHYLhTcdXCfEieTYqJTQu9CZ5qOVUNi5xNgM_FEfe4If4YdmCleqOZokkR9PFkXX-lj_j5SLJ_7gXvb1CUNcSOIb_J_6V2yeBNQTMMNlxa3aQUaS8JgPoNOMKVt50dwKSX4lH30Cdy0QdZ2o0JFkElft719nyrPjS2iQtbJICDmP2iIiT5YLSeGrXViSptawMudMcCPg_Cgf58dDUSLsXF9e-tHa1eEIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=cNjZ1nCLKXLOdRaVj2Ep-7zBmoGcdQbLckrGC4YPATu0oDvMFDuShIsr8wWCYgeBfWeu0tltlT5nF4duFXuLJOVuUwtL46yZtaax0KxLJFMi8RytiDH7_nqHYLhTcdXCfEieTYqJTQu9CZ5qOVUNi5xNgM_FEfe4If4YdmCleqOZokkR9PFkXX-lj_j5SLJ_7gXvb1CUNcSOIb_J_6V2yeBNQTMMNlxa3aQUaS8JgPoNOMKVt50dwKSX4lH30Cdy0QdZ2o0JFkElft719nyrPjS2iQtbJICDmP2iIiT5YLSeGrXViSptawMudMcCPg_Cgf58dDUSLsXF9e-tHa1eEIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS5be3YF9oQkrOelYYxmjHwd1rdBGek_hqYwvAa1CpjsV85ixzQm2CLntZ8kkxuXH5W0l-F4g_kI_ImB17zqk9t2uJUrfL3hU6dyDIxV44pgivN73BqWIGlU3qu0eRpgrQdpdNSce2iPetp0jAlFT-uq-6pNqX_xTF8JB7ZQo6AaDt6RHiaUYP6vA8KFHo0R2zHW7GuNsuT9FNH7_FRpmwmJm-a9HjyXXzex3tJp6kONeYz-SLsP0hfTRQbWnxW90oDE5K61Hf2YLvMqyEr2rK96IOq0R9VKOM-jGcpp-0mjH3NBIQKsKu8obXh3PhRMruaRU22c56cGl7Yc7QjpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7bOwPybm9EZXZZdYHlw4rADskpmJqSQyWD4U5nJz6qVw4InGyHY1RCQl77o6Ku3kDej4sLzE12Alwp7vLYE0VZyTppiMumYO_DChp9k7G_8Vr7i71E9PzlC28a6aOWCSUW7iY4I0eBfdvITefAeJLKBwJjvO3WyoimwtCBwaGym-dfkE_Fi0Fz5_LWP41b5W2Dnl90W5NoMfj6U3MxR7SGe8VTLY7slLb-VVpLLkeQVlqctFnkZOwckj-x5fyE_4pCv29sTJKjxlv-lvdn5L1aT6mNGk_sAejvpHR3LsTPGJUUmoBlE4dcH5gwwTbJ-LiFJlLB28SiwlyMBwQOH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKY8aHh2qFsrP2utLMx4ygFcGRRVzBooMOFE9nwtiAZQ-MFtg-jz-ebH0XLNdbuhScGSeHMXHP7d58CURc40BLI1gU-fxcyKO7cxCDnDWgPsp6X2YyETmAMLkif6ulaRXC1IAuHZHErF8_KKyJa6Rn2RRBUDcz8NzLZl7pfQ1DducP4Dfo7FKI_j7oTN4NoaG7xTmoo0Sdk_ZTHUVM-HipFQoZCXthFjjsGC73lTyuWfkzz_xgBMCdArLAC5fN83hIk2Xc05zUTRQbGIdAkz6Zgz_c_Uvat91AhyjAEmeMe-NQlYiCt7A59t_AKSueQaGEv3C54pwT4ipwLFUJ7yKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovxrtq3F74y2vrkOJbITcLxgKR6OiUot5YJCnBMSx8-Gtp2jA9V_CcJxLn4UMJ97tF_UzRZddKPKn5PvZvRxsziXRzghNXjNex-NE66QX775jUGliXhD1fcfYstF9RwBQfUsls5AziXZA_8IXrqn3G10FPUy1iHjwHxXjz92ooHZLB_4t5G3lGaHYorRVMLhBzR3DSezhihP7kCgE78p3yxqQ8jU65rM10LAEPuWZ0ue-_jpvN8pd2I8OWwOFWuyBCGgyPHiOxAVy_YjbtXvorPTm9uphhDGsAyhKK4gF9sGiyRHGv6qxlzvDmp5972OxMUSoYC14gHEg8vV4fsU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL20ZJRGA98x9zwxpdd610ibEb8I6owT8TxCTCEzfAFWWpeM_Q_H-XzbCiIWxnnsxitrrduwZeZ77apVDrq40NOl5cPL5sScpIWqTUFzkfTgGza0fmpGeovAhhnP1uOks94-cR30XnUsozy938ympkzod2tcFuQCJG6CgRJv-x4pbx6aZloyuOuNblRBwjmforYq6W7LExoHqkn9chou6A15Dpso-5yn-yWrsRnE9YlVrmD3mpaiKwSY2iVeWpI0oFfMf-v8_wJKY1q0wYH9tzAPCktGEJannTZw61w0uV3WZs6gNhAvMRVifzJgWkdEH9SutW4bIwPTpRa2WQuDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=TYciiwYW-o4uqsw21PU3Mt-lI-tcPLoNfNun4lWzJ9qTTcyhDFMFv9RZLHbpN5G-57OqMEjmnOkgR92U9pOVwTx6RdLN1odbsOClsVyOLPIiI3t3pnIxi2OLKuXFuZZI8ZK24rYthg0zgYsUoiLtwLENSVTgEa7Q7NqcrCXB88mDZhx5McYK22BAZnny8Odg4ICVoO_rLjeCG_zFKomwc3EV0AilFxysRHrlYarauSN8-w9vdUGNS3XrALZtHJCyHkwJaPGgiamtBUDB7BdCCNUG8JeL9dl2_5c6Zm07rJIN1sEYOPeuV8TejiPBkwSOIgvF4mls-NYeGbEciwUKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=TYciiwYW-o4uqsw21PU3Mt-lI-tcPLoNfNun4lWzJ9qTTcyhDFMFv9RZLHbpN5G-57OqMEjmnOkgR92U9pOVwTx6RdLN1odbsOClsVyOLPIiI3t3pnIxi2OLKuXFuZZI8ZK24rYthg0zgYsUoiLtwLENSVTgEa7Q7NqcrCXB88mDZhx5McYK22BAZnny8Odg4ICVoO_rLjeCG_zFKomwc3EV0AilFxysRHrlYarauSN8-w9vdUGNS3XrALZtHJCyHkwJaPGgiamtBUDB7BdCCNUG8JeL9dl2_5c6Zm07rJIN1sEYOPeuV8TejiPBkwSOIgvF4mls-NYeGbEciwUKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T61mEMV3lNTBgG5LoKn6O3toEar3qPOwIviRH9S0HWCJNpYQutxkiLHXjrGlynsnPvMZiqQyWUpTGHtfK50-UleonbMB-6icmUm5O2Epuh_l7HHWJIU3WJ1d64Ubl1WPGGPb_BsqrGBBZ_nmldI25DX9UwA64rN-tNTvW8NzKNQiPien9lc4YBcNI2wl5mT3-Kbh56zFcprwTIqN8XM7GiyktpQ6gF9xxhVEWwJ3CRV-MEZ4OnwS2hZqizivueZhM5dOT9mRxHSlJ0X7pOshXx0FxcE9oTB6g1CxFHToMkvDoEebIy4pRc8hKKpBFBfutkYzLQvSzzLFQHftCRiAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K22kgbHwAsPrsZzkygsiB46ltk9gmGj9z2Chqf0UyUx8r4C17CF6zRvUEk90ly1enn2_Gyvu2JYNexIr2tigFpLv4fnCWOnYhopStOFWYp8P6HPdLqq4_KcXvCbLcbcz6QOvxSz3kLlwKVTmS1FnpgVTqftoTeoetr9QMYvLyxGumSei2qIIYGleFdT5wZPLCibNW-uPA-j5IhneMlF6bQWMfTEzonLVt5UgSTrrZvfC7YKU2DgN3aq9cMz8sMyWpLySJjZM6yDCjSqydBiSrtQkZK0d0oSAe1SvInN-tXkrcIYcKIMU3JSmBYkAtokpRxjubhWH_lW-2ch-cLe8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbW_i6kvZUuNsSWFwPtvNv8uR45Ku6WyEQ3_zbQaXcB3idU0DwZZLTmW4GQtM6RXyQrM_ieIjQK1HdWA-P3f1HwPmyEnKHVSE-Wz4jqp-xHdGDYQKn8vfkvIp5udH10syIcR_XHFEs_WN5RsqcwcKpGRzAQKMl9Ben5BuaOGQgN_vtwqtceCPbWsuuQX9QrwogjF1OBQVdKm3w3-gxmXMkebaz3swengtfVoa0RUNk1v9r-o-7xLKeUzHp02S1GEoMGBnZXGxG0E1Se4hFN7emTlAHbVD3Jerv_MObISGA2V_7Uwe9nrsmyVa0kMrU2-ebZD4jqGeSVkOXLoAkOc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8Sq3VbLPoMdJ946vh62Hs7Hc5eW55yLN4kZx_ij5VW_rv5WZdmIK6KXEFthEc1x1CAej5cvPRPonWjpvORJRVVPAcN7CF1iA9xAI9lYkVl9MfnIITN_NMTNo2jsIN2TBhUx4bTQg7sfBBG70Kv3-KNbkUQTTJJ-3_YsybjI6sOqorONAJfk_32zTDxz1QQSy-6Zayc0bL-678yatRakLDXts2CPLXCgHjGq08lBjoeNJ1wZZfJ_A642l1NsjYhMbKHCAeX3ltpKNE3zXtw0qVLxJU1E2SqKiffDyZTJnjrwYuvOINRw-EJTuJPLuQ3DR-LeZ8_C9gH3j1AXs0r0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=qBMpZRO17CxGdyMu8pXYOSa3icQCoj5Ez8rGyON_lbSbq8UPnr4I83-mdc057oV0WBy1hlO_c9yR7IUC_Pnk65YY4YUzyfvQbICC9q1V__cWM9pqNVbPp1pvPZzATQW4TdQj3vA3yPwoNIGOmqxEowTDCstPt6ICL_T17pM10txSRoCN37Sn-GehVLZu1_MXn8cc2ZC-MI8N9fYbsCjKtWqF55td2HKwit-qMqttUHiCPg3Jsce3Vrc74vj8oXbkYNXN15HrfpHJ8vL8XEgpSGhqF8V0wwiQYO-8XZP1EkFkUuUoLKRGdevx5YDNx8Gs9h5NLV2v9UwdS7yE3WttIRTLD6aYyssLNFNipO4gw9CtK2ZMJdvaOCrv9lUF2n_6VHSvWGCkYI-vVVsfPzxE8Jq168ZHWBVSNYYoVdfgzYWaezE9mj8Wbos7C4al--HtJciZtV-tiFL-dyQscy1mz3Nv7jLSRjNBjyHxpmmnGJQImh6Kp_iumoWMfjVzo1iysRHq1gMH0pknaxh7ntKeW4xX-oIU5m274JyZdLSr5DjCe5EpKLcx_w2vkmUDHs4ugjqQ-8L47NIFJCivwgAQIR2ZUba77X0byYSw2E5o5aqRfGAAnCFVj1A1yiX67G5GPBkfeNMx0eGa9-RMn3OeKdbZoOZ3_08ZhZtC_ujji-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=qBMpZRO17CxGdyMu8pXYOSa3icQCoj5Ez8rGyON_lbSbq8UPnr4I83-mdc057oV0WBy1hlO_c9yR7IUC_Pnk65YY4YUzyfvQbICC9q1V__cWM9pqNVbPp1pvPZzATQW4TdQj3vA3yPwoNIGOmqxEowTDCstPt6ICL_T17pM10txSRoCN37Sn-GehVLZu1_MXn8cc2ZC-MI8N9fYbsCjKtWqF55td2HKwit-qMqttUHiCPg3Jsce3Vrc74vj8oXbkYNXN15HrfpHJ8vL8XEgpSGhqF8V0wwiQYO-8XZP1EkFkUuUoLKRGdevx5YDNx8Gs9h5NLV2v9UwdS7yE3WttIRTLD6aYyssLNFNipO4gw9CtK2ZMJdvaOCrv9lUF2n_6VHSvWGCkYI-vVVsfPzxE8Jq168ZHWBVSNYYoVdfgzYWaezE9mj8Wbos7C4al--HtJciZtV-tiFL-dyQscy1mz3Nv7jLSRjNBjyHxpmmnGJQImh6Kp_iumoWMfjVzo1iysRHq1gMH0pknaxh7ntKeW4xX-oIU5m274JyZdLSr5DjCe5EpKLcx_w2vkmUDHs4ugjqQ-8L47NIFJCivwgAQIR2ZUba77X0byYSw2E5o5aqRfGAAnCFVj1A1yiX67G5GPBkfeNMx0eGa9-RMn3OeKdbZoOZ3_08ZhZtC_ujji-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcUUVOJr3YdZ0ly25Ef3jR_dl8rWl-G8GTzB_wu1TxLNjWzlvoIDjaudR6e744iojP_Byl0JkErjO8p65v-NL2xIfMT41DvanElPBHcMUg61yExuXd-sSvENpCl4zfYv4f90Vyszh2uHhzFrOxQTWlN1QUEnBk8CxTGb-OA9l-l6zjGnc9gOqzRFBbkgEeVqDCSfsntCz_XJKKuy15OQE9RF1dHFt95sXL4DDqj8zeJaDhdLxclac2aDPlo3IxmqS4E4NpZMuBSJLILWrsY7wMTXxgJsgeCqnB1iEadWV20JUOz6kiPpUHhOiDLPFmB0Uvt0hszwpdpC9t56qB9RCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQpr8taKlhyeJU9W7DW8Op-UY1373feFY813m01f51X86ckuWsXkMl7JgaLbfhzZ3UG2-2oh4yha5KUuQeNQ_GjtS1evGMmBXdx0aqK3o46h1BfDHeLV6CcyBtIq3vHXAwcN5Cf6WrAlKScCcYzdECUxDsDe_OrOOvZYtmIyyUUoDkZEPzhUhAoTLBgcqN9VAN6TwIAfhcVjBISzbv1URheMeC18xbay9lf3T-0I0v2AB1GAzE0uwF1LpQWQ6dbwzHO0XwkGPyE6h_GLvL5XnWNqcuYnWDKecBXqNM2thDttmgYRjc_ejKv1hq1H6WfyEnUOx99TobnkOXJN2xHkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee4gawwB9xszLxYweZn_8HHE8e7b0EQw9r_6MZkVCHCpgcD4TR8YqiWPWexwSzy908N5mcztyeH5G-jRvCHLXk-HTYYcKBKQ2Y7iBt5RHtqsLzQ7SnzM2Ct1WyIsqSW0SjTAO54ajUQrcuIaRd_6kRgr59TKc8YaIk1BuSlLW0-sHYyfLXqSkaaLg1oP4yFbnvm4c1WS7n7Xx5-jKeD-DGmgCfIBt4AC8L4gDWVeYIprPmowXqPs8knS_EkUSc4uRJgH_m6lVe3drKc2PjCAj2TyqkJ_92azce4EAHbPS3OwtUedot4vd3yh_4c0hzXFaKmUblrQ8yxQ9MgmN5ZOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuGw8ziQ-yBCWB4r69_gCZX0u5NznIe32qd2CylyrwHFnQHr4zhJPDe3l4voM_C4fHeOYAs0b8FfchAlW6-cWVnlfd_5U04keU46EwZal1HqT-hFWyX-XjHLxMv0juzfwR7YoHI76IXi-FCPr82KNmcou5wbqK50T98ulEsuEP_jczg9abty6u4otCbcmK7gp7Mt0OLIBV0KZxaRKPicN8a9RteY28mC4zFq0pWmKadvrNJ8qTIwMEpeWzP4fOGGZSV3GS_HKdtwkToftcToE2oPi-cC33h74dn-VSEFMSUNSH3MRUiBT84Lv6yVX4nzZ3lBcRUpgyAy8J-M3T_aVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNPd5uf_P_P1b8IVAf9wOI1OCRbOQbJH8rHiNuwhvrhW3yj5I9R-t4seIxUzQvyjd367bUTqlsdGn5QBIIoMn3torTUzlsRqrmEuBqt3ESkB23QUOn1NnU5gh2kaSK7e3EGVuYgPhGfFmDh0WAjTc-Y7yEKNTqJvY2ihQlpFr63N1KsLojLbQkM8X6yYJ2V9lXxMIDDPFAvZQGSvSx0YkiVWPB4b3n9WosPIVf8SdzkFO3Y3iw0i-c9WLr5AmhsxDJM1pHDRpO9FsB_XoPv09mCiLsqrlGGXT0DsFA5GOWReZNOhUyWuDSYhnb9FhYeJYhn_9mli6R-YIeIfAMx6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBKvvc9WaX_omagi7JHKiZeI7Rdlwuc59v1Wpbe6ncEirdz1-5udmtTyAig2fRjjPwImNWb3zmnDyWkavH6naP-R2LAwCRnAYDgSRBch0lQ1SmwQJ6oRK2bjihLu6NF3zx7sGjUJ2iFQWY1vAIetJtAkgusjl7fF2Q7L7OJ6B4Wmd182X5SZwalNXR4-HRbAgDhJuIebYckrnhV5IE96NVAzuh_uQO3e2qaRQYS0Lr66F3vI2-LjriODDIMnZHjBy1C1c2yEcLvLSQp6SsJlxOLm-skZF82MSuEMFT7OCkhteMkui-MGes1gduxUS7oIv81xsNXsO75k25gsgVMU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8lBfUiMf7AqL7eD2ArU_NXrZgdGoW8rxPKVFKa9lHSF7A9KFCic3k6UrNXOelt0u8vfVEx66Q4fS3GRhhVYvYNlep8_izsHCOHPE28mCNnWZZc8S8Siis2oVjZjlZouTaeEHfW6llXUxnGjQDbxvZAxFLE_lAFUX4fF3xNL-zhqnIFt_lfY_BaiplrTWa7p7wgbUKltt618JU347igFZbOKnyw_roVQeJuY86A4Q1DUhHle7ZAFK7rNbFbZsrbY0Ux65d98m6sRi0twgqF5oaRHZ7uYziVS7FzMYsTXeDjQ00-qH0IrLZX3gCULQKd59dLZnDBscPNFHNNLnA-fbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=AhvvLkwrypqcr_mszMu4ctgAYeNouPh-fXe2IRkHdDvK5dR-32pViZULlvQqIc9SSAOD4_LLoB9QvS5FXuYb1tW2OsuhIzui0tr-d2ndFwFd1QJuggRZWGc2yGkXn6ayEMr3Ie7ui1Vjtfn5uH4f-R7wUbgN_VRS1qNixbqt7usvX1zyye1YPDTDtHzOfPc39QntFKeAG93UYGeqOxx4g7ZL7_J2Fr7VWsKxCtX1-Ex8jABq-L1mi9YWWdVf_UzT2WJJK6glbO3IpQUIllT9eUFjatApA0b8VJpCWO3_uG3n-1VyrW6NCyX4qJ1ds7fHMX1MsUpdyO05Wcra6rI1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=AhvvLkwrypqcr_mszMu4ctgAYeNouPh-fXe2IRkHdDvK5dR-32pViZULlvQqIc9SSAOD4_LLoB9QvS5FXuYb1tW2OsuhIzui0tr-d2ndFwFd1QJuggRZWGc2yGkXn6ayEMr3Ie7ui1Vjtfn5uH4f-R7wUbgN_VRS1qNixbqt7usvX1zyye1YPDTDtHzOfPc39QntFKeAG93UYGeqOxx4g7ZL7_J2Fr7VWsKxCtX1-Ex8jABq-L1mi9YWWdVf_UzT2WJJK6glbO3IpQUIllT9eUFjatApA0b8VJpCWO3_uG3n-1VyrW6NCyX4qJ1ds7fHMX1MsUpdyO05Wcra6rI1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AywceYev7VqdxNsnFDsemWkqYdT8YU5JoP4Ouq6qSYD_Ddbeq8-TO3PbGDXiHyYHtM-uYofwXALWY0zbKCS02rv0ThpWmeS80N0sbas7F_Pu4-ks-VHSA4kAN47Ix6z8qyu7YrdrUmxXIVnMb1dHiodvJm1g6KKmR5Ork-66nSWwVUgi0N8upKqCHqf6d1k5IxZ3r7BxcJBZp9qBT1dL6VIeGf6x4BaVCXxNgvc0gnmqvFFG4ndungJR06R2u8QOfYjVIIzN-H_M5NufV7IRAFKRcHTra-JXwIudFvAm-BD1bpwOz4oy2RhcKq94ol9S2M-iXaQA0ZQgokWJAeOfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnq0SEeBLnU8CrZRZr5kvF-YtC3Ivx7IVzFO4IhkVSeUQr-qh-tVumBJ1L3S6NrTHwQoAxfoFGLQbli7vDPYdn2HFXEhsHdEnNbX7HJlPTXxVVr1Ec9Wio3h5PYzrQkv5gojtIkJoB1USenZBy8j56J4vOX45N7W0_wFIGjoiZnVnBapp_PfMYB8nXr8djVLMNfwbAIMVMggoKwRXlY3bhbByaf_i3iLmyJM980CTIiGnAz5kNKqKFlI-6gjhn3UUzr8Scd7MqD0N_jUQnQoFJ2hcOGpJpZpP-WVq64MGFBPfDGNVtva4qLtPXbpyVToqdaNFpHYvWtWvywdWwyNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gb8-gjbD1nps_uwGy29u5QizLmt-zQ76cJsV2UdbGHVj4lGBHJ-D0S-jVfdkjNNqGizpXIVbr4j8n3pp-VGXFQc3BhqiioB0UnKVuC1mFKHIbFcK8mwqGTpikDuA2HVZmEV8jYl558qd-4qS-ZjM8ZVFab1-sPOVIHjAsnjX0Cv5DIDrHhP3ZK-Dim_zzLBxBdPn8GjSWcno4JxF188T9czMYJoKRZiy1Df2t5jL_i9WOahMU4NVurD07ARmV-R0Py0jK96aexUCxrQ3JZcNawjcKarc92cZrv9i3uzCYG75DwomUfFGgqxHElPeFpk2XkiC4pBFyW5N_C5-NsCpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=nXQBxZn_Q7QuXlgEqOPmwTaBZenHRaDMuRYHqb4Axh0JGx6WEJpyBd0MwtEvhmH2XYLFE0Hq0JYuK73B8tIlu0gVD77ChaIKi7yj6L1Pyh0R8LUAjwa93UMGIDGUujqy-80Aqj-8XRE4PIJc0u4sN65CNu9_Ycc7o1hpBWGhMilStOWZzK_UD-0dOnbTgzGzUnfzEokMXjA63ryJLuRf2mhl87fkw3nWCOjyFW_IapXSEXEYo2CDPD0b_D-s0NKcznsx7V1e37hMKLB4qxD33k2AwgnmaIsRAdwydW4hAknGtL1fP0-SvkhH6Y7ttmoQL0iRCxQP-vYBS4CSUhTOQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=nXQBxZn_Q7QuXlgEqOPmwTaBZenHRaDMuRYHqb4Axh0JGx6WEJpyBd0MwtEvhmH2XYLFE0Hq0JYuK73B8tIlu0gVD77ChaIKi7yj6L1Pyh0R8LUAjwa93UMGIDGUujqy-80Aqj-8XRE4PIJc0u4sN65CNu9_Ycc7o1hpBWGhMilStOWZzK_UD-0dOnbTgzGzUnfzEokMXjA63ryJLuRf2mhl87fkw3nWCOjyFW_IapXSEXEYo2CDPD0b_D-s0NKcznsx7V1e37hMKLB4qxD33k2AwgnmaIsRAdwydW4hAknGtL1fP0-SvkhH6Y7ttmoQL0iRCxQP-vYBS4CSUhTOQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEWTpma7axuLP3Aq5J9qoIwDFtfMP436A_0WCbc2lM45ihI3CMm0mdFuE3MzE5GCSybfNCgUek47-ep7BQmw6c6JA6CWG2n5StESV_xsHbaSs6VJkOhYwN2He2jwT89gBqG1fpUpuGriT3icdMNpl3GLdzhaQRtjvL4-jb_8-WmKP7AuinAv8rAj4FujAsez_zTfBn-gSehfFQuJ3U7FofPj4r5m7QezF80pqnhYpU1Kkf9LuzPE3UzIkDeo7Ne10EiBWS5e9aaaCYhmhE2fbzOWz_XDmCL8e1vxU-IYHjG49h1wSvyIqSPNNV_hAqGnWK1BF7qiYvbt7d-XdAo7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=p0nKj0P_nnivqqo9OdcBWILwwA68IRo0JHmfjwg-JUAjVJxDRCYKQxKLtSmsrIrDd7NfVYuXoDNZDCD1B_Q4Wl0OKFLrOxqOt6g7-AS8NFdCjvZTz_NtH5X_NL6O_eZb226ShxkvBKS5oaMf1fvpca2sYZ64jmJ3YoqUf5_085iWybOcXVDGC5oIdzALC5carQlN5sUclAuNWU12Gdg-gfPJAQmAbCd4xD2GxYkhcMoXEqsHhusZ5aGUP4QM0g9FDWS1xvZO25rvQrscxcZ7YG7cbgOBzxXxf3JCjEV5Q5hoX9pPOY82w0VIZsoIdh_-D_I7Mxlvr1r8byTh8G3ysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=p0nKj0P_nnivqqo9OdcBWILwwA68IRo0JHmfjwg-JUAjVJxDRCYKQxKLtSmsrIrDd7NfVYuXoDNZDCD1B_Q4Wl0OKFLrOxqOt6g7-AS8NFdCjvZTz_NtH5X_NL6O_eZb226ShxkvBKS5oaMf1fvpca2sYZ64jmJ3YoqUf5_085iWybOcXVDGC5oIdzALC5carQlN5sUclAuNWU12Gdg-gfPJAQmAbCd4xD2GxYkhcMoXEqsHhusZ5aGUP4QM0g9FDWS1xvZO25rvQrscxcZ7YG7cbgOBzxXxf3JCjEV5Q5hoX9pPOY82w0VIZsoIdh_-D_I7Mxlvr1r8byTh8G3ysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMKTtSCtmvUi0U-pjPLygjGC1UQKBH4Loc0wMKipeGQes05mF9G_tE0ti4R-1YN9_0gbhwYRFh5r-3VBlzys1mBD99aSyOrLUcK5_WA9u4lv-x_7RO48RZq02bCCEYC-ItdqH0DNevEyOunyrVtmh11j4LdSgqc5HE1b0iX1EyntgVy9nbKsZEZ0k3GPD9Vbs1jmi5fXAX7wP8tvAwzwahKPp7OUIMyfR_C3HtBzsfoBkHoQd789qkV6kAy-BR_fVKe1M5V-Cvo_ZuOGREfsR8QMdNdeVy4SzJkyOrHOgp_TlicH7IAIg6VE7v4K4uT2TJTcKX4oGp27up5Qbp21KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=FXiRiQfAm3o798E19aYngiLQFxZqEV34WxMH60xiiXGA9Nzjg7qlyEaEGopIou87NzSHGywv57tMxGi6yOWAxInONBu3MumWmTIcivP0YAlfR-Do7jp3joeA2r2VqfAJLsVGb_vKAew8fFMtHxGoY046F0P67N0aCSkgwUz3AZO7Z1qlnPqvtEJh6ckrOHki3o8vowM0q1QD4NOff4Rv5H_EXMmY5SLoe-Xf2J8pqR-umlL1njmQxGLvPe5Wx18J6CovMXmqmIOWHBcwrrCi1XYxa6lwB4rdfvGAk8MO805w-SX4x02cYuwZvviH6Epye9illjVc7I1S58Ry3DbEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=FXiRiQfAm3o798E19aYngiLQFxZqEV34WxMH60xiiXGA9Nzjg7qlyEaEGopIou87NzSHGywv57tMxGi6yOWAxInONBu3MumWmTIcivP0YAlfR-Do7jp3joeA2r2VqfAJLsVGb_vKAew8fFMtHxGoY046F0P67N0aCSkgwUz3AZO7Z1qlnPqvtEJh6ckrOHki3o8vowM0q1QD4NOff4Rv5H_EXMmY5SLoe-Xf2J8pqR-umlL1njmQxGLvPe5Wx18J6CovMXmqmIOWHBcwrrCi1XYxa6lwB4rdfvGAk8MO805w-SX4x02cYuwZvviH6Epye9illjVc7I1S58Ry3DbEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU3NYzh__Ojs0o7evORRlT8kjnR7CpGZsYfl5uP47RWhdPBJg2vHd4q4GESnmQZyCWJO1qwKZRFA0It0ZX6QXHooLZ_ZzFCrXCRg_2JLem-7kK6n3pJKCIeb4PHChuUXeF-R3cBDBvLLYw3BFGrMi0zrT_XZ7i3mTFl3wU7H9G5_9s9DihhLVJn5SX0Qve2210wV0rMR_F5iZv03hYnqSXeWl8GybOzx6pCFGqWX05QDpV1-lLhZ2m5Ez0miq_bYF_btnNyRS2rMsaitQopeT7ABiCo0f3Ayt2ir_4SALKJBNpEakMbhkXJrMn2PWThCA17e5jhqABhRN4ogtgIzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd_gkRBtG5pYQmNxi4rW6iLCuPj6UlpsLhtRv1aGQuTsUjAh1qrEYbcKvp-D_c7Pit05Y2B35uC_bR7OUPNpgFFKs5p2wxYRQvOYpDyBymIy9caXdYk93T3eUWlmim0YTtJhcI7zZ8oI5_WP1_bVtg2Obe-uwQuYHAVM3_vd1u7rmPXqoNF-bqj6fzs_1xa8GQFKgRooKGq5Gm5kVlmS13gKY0OQv6ho1WrDZjMGNUhhen4Dlz_4zRIwz4vPmOZ65ZVImoyaKDQj5ddW0D9QG7QocpNoXE7msq0rHEIJl1Dfm0-ZmVu5flg2uIostfw0fI5mv6IUkPs9BFpSheMkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFmyZRdkMG_hGmYH2ADYMxAaqnHBjeh_bGbG03_GgQTFdpd5CwZY8QFb-3oIWrNejt0xeSgkYUKkQc-vj7pnCf7KrJQ0X2VH7gpCU6x4IxBHVCNgdCTkjmvJoAWvhD4dQzjE75MYmbHbYCmMZG17cyJGFQof-sFbI8lmamz-Ctkhdb3cPB74CqgxZ1QEwCYVeY2xWJ6K-MoXidTRDxxKENklj5Hhnhytullw_hYvmt26LMARSL8sD8M12skBt3DSeRuJdf_s9paY1qBcAXBxMwAAxQgQ_iT_9Lviq1bpsFFjeKWPUfyEWHfSEcVRPZiwYQj6cZk4wtBa8c-MfiO6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLXUCqFxjMCWpexxp4Xdr9sVdZTu4qMiy0-xWj2vKBu5Z4z05vE1wiZ3CUfd43aJgMQjYLHeUO-apibpAiOhjSiMq8iq0AfiB7wC78Xw5oS5_3l6FSpCoxvCajhwZtn0JB5bAxzk4MzgrarSMtlGXy788TomJlg1r4w2Bem9-x6hPC-X5wEBwxfBR8GgznVZWWllTJIfR6r7gjzdwdm39EOx-agEmY5RBDUPhHQLhNc5YdS6vIM9ZrHn1jyu3w8Ys-PZDeuuj_sWHBJ_vBmK6B7fhlaHwx6zXxL3rrQeAZ1do9mDEhmntyFtZ0O3bRkjAeqMmtQ1tXZz9JP44h2m6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=oevwwJfJiRnBYoMMICZ8dzE1u0SDO_NsOOmlOscLH9bIqA_P-yO95fRd9jBooa3YnnZkbH4oUJL03pNno8xoqSaUmrsKr4T4w48wuhoiJd8XFu1fJpGxPzEHGsnEPkFl-s-BZdFhlmuSsJec_6GrsrUlnG5vrgf-iZXaT_5GefpW3dOUg86yI8Rlfmx_qB6A0CKSOKmHMh5S9mkfhkGoRb62qKauTDMhn1LBtVl7ki-vJaXSenmCiShwJGswNp9M5vd2R0EtiKFZ7P2C22wWIl2B6SAVg1erOLyMrffS0HDYYNdLPAWogTN7q_GxCWboRS1R20iZ55qCe6tbIKBCwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=oevwwJfJiRnBYoMMICZ8dzE1u0SDO_NsOOmlOscLH9bIqA_P-yO95fRd9jBooa3YnnZkbH4oUJL03pNno8xoqSaUmrsKr4T4w48wuhoiJd8XFu1fJpGxPzEHGsnEPkFl-s-BZdFhlmuSsJec_6GrsrUlnG5vrgf-iZXaT_5GefpW3dOUg86yI8Rlfmx_qB6A0CKSOKmHMh5S9mkfhkGoRb62qKauTDMhn1LBtVl7ki-vJaXSenmCiShwJGswNp9M5vd2R0EtiKFZ7P2C22wWIl2B6SAVg1erOLyMrffS0HDYYNdLPAWogTN7q_GxCWboRS1R20iZ55qCe6tbIKBCwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0lG2U1lMLozR0H1UO7UOxnUOJO1FTLdjhdm9Vzo21JGm6z9Hw8dR9kxdEujBWx0RfAOBV-_BLwRkwxcZjatLEv8acU_Ue7NWMvKhB5xKEEALy0f02lB12FLlfbxncyCBO7E31RsgLwsjDIbhWK_UyDmRqesRSrapZDEPF7V2inI1f0RRGC7RUC4Y1TApdiJXmLkwDogQZnPnVA4M8kSttkllD5kZSFJoVPKraOjMJWqVtZDT3W-0KpCoatZ2pffke_jd4anJMVVn51kcx23vb5xnSSZWOtWJrMEJ4T74YG-Z-khMmBVMxfoyc8cwoyuqTBWPJ7LtxcI1pKn90vFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFO5CTeSEJ9ycT0Y2DROwrmFLyB4kc5BEhs1wrGbj3I2KRay19Kwe6qH8aRpVR9EF5zivu2Vlfc70QFF6pHIMYcvHcmG8DLtj3tKzLHiS14y-8ypbN4eIzfTUC4cfZWXaA-5q0IvE3iX9OtubLd7sIEtzUlyb8PU8bdIIftVYAP0Xcuwq1j0LMaw_5KJMclsRwyL7EVUaTsxXi69XqzbpfU8CDyKMKeeTX4VPKUV0po6dBuUG_PSZpEqudWYVP5Z4v_oWzGCkJNGcdTLAKxBmO0DTCHa5bmbAcGld-h8zUs_vm3OuQW5qF5HggSK87yEqadzvgFRTbqagUdjjT5-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyGyxI_uuPEIwdDlECK4AiWBstK-0Pwlo3liDsG_wAfXdlb4VV52-98PGcXaajy0QQ2NunPr4ljuILyxGobYU5wMJmhxFzHnXxDbUwguWNd4UZqqcl84OPjGEyu-YwuyN7V7cBdYMFAe4WtHmBvX-4k4eLB-7R_xUuOxce87ROaWbrz0Rj2Whlhgstc6JyhnZYJfYHOFC-p2YTDQHUtcIwG_2x7kc5BUjaVQeQJYJihL4ro0ogbR76N-XQufscREiv_HQ7blxenhW_Ynyupio2Y91mBHvDdrev55S0Y_ErFxB_yJaVYIrl6Ls_q3C7mN4POehmj7ZAJoaunTG3ujUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXOlXK6g__P4wYVs_u2aGOmDQuw9hUdbqGave4HGiAFbzK62drRImbjdoCcSh40Q163oPx72eeCszZs8Cb353mLeX37gM44xAdqRNh440maIOCAyAP4DKQaQOjuk2jLnfVWuVGMRtr-P7WPVjcifA0CMqk1kffv7idtkHUEMcLHq2p3NpQwuNrdWsY4JAWjrIDEvG2JCGw6WwYuW616tMILi0U3hSfZa8eYV1C-1_CfEgfOCkflrWn0H0PC_ACcwapq9oQWXQPqTUjhaSCgdjmCQmMwClteLyB5VpQX6x4bgAf_w5M7qkA3uMVeD5o-Bwe093Br22ho23Nmh0ya-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFuUYVZmqLJ0SL2CtHRvCny0bcaGZAKTCo5oTTOYvrtHx3inRqTiKzGLNk4krTNGZ-zDLlZW1L0t59RZPkZcuCwidjwpNWmB2ju-8vW3vJdt1Qts4Xch8yC8_LXnm6SRiQ7656Nq0OoF5IoQsGrWd2eCcyfRcoVsFp1vZddtQiV_hUbef6Mzuz2r2UwPyVzPlTGFutWNIBkX-XqzmzRZc9gnSv2jgjQeOV8yvKXE1kyUOa2uOPZaZey9cOu-fzjFk6i-Ix0ojLCky5c9rDFvohiES2gSsyjDapsPHaQnbHIW8Bf5cQhdtN9OyfplkJ8JcI4ehEWHBB-uYA38Yq-6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
