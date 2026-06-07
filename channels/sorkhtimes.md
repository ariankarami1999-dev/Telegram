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
<img src="https://cdn4.telesco.pe/file/EVyY9FpJgJGsTG7rkTULSTTbqt79er8EkN5CjuE5UM6P6yx1bDd8cXF-akdGsdf5uqL61tlTdfv29NlQ_Z-rg5ci1591GMKCaUc3EMkEAVtNMeMn4X9XbOHFE0AIS2Jv6uafwj9QTQ6x3DIOqfGVwXq23MJyVid9OgZSpa85-oh85U7dbHupPtFoh3o-dlqL-S9wwSZFGqmPfqgYHwPl2kdvhZ5wKa_uECSTAS4ssmR4AgnTv_Fh8u-8bzY1yWwhgs9qmXRjw8rOPQjfiw_x2tZKmCXRIs6hllGKdMEbKQykJrfxKVKmzFooVU428o6Xo3z2VsQOOdNc1n-X4VfcWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-132963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 518 · <a href="https://t.me/SorkhTimes/132963" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
سروش رفیعی به تمرینات پرسپولیس فراخوانده شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/SorkhTimes/132962" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 250T کاربر نامحدود
30 گیگ 300T کاربر نامحدود
35 گیگ 350T کاربر نامحدود
55 گیگ 450T کاربر نامحدود
100 گیگ 650T کاربر نامحدود
دوماهه
50 گیگ430T تومن کاربر نامحدود
70 گیگ 500T تومن کاربر نامحدود
150 گیگ 750T تومن کاربر نامحدود
200 گیگ 800T تومن کاربر نامحدود
سه ماهه:
120 گیگ 730T تومن کاربر نامحدود
160 گیگ 780T تومن کاربر نامحدود
230 گیگ 850T تومن کاربر نامحدود
320 گیگ 1T تومن کاربر نامحدود
400 گیگ 1.2T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/SorkhTimes/132961" target="_blank">📅 19:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27207295.mp4?token=T9a1RP2eM8Uhu0QqBuknHatm1jN8IC9RQOwHh9527rZznzRHBEbwwQ_TZtVAC2z_PseWUMuqXZ6W5QZBOaM0d_NOGucqgrqGhyZXE9jc3v77F_9-yYwfOqHdYLIyqqoMvOIIQf17LPVGIpXiiPw6-tp54RXFrBAca8suGg1uymQCCd2hL7umzVLhlh9xlF7pszG-LoAMnCn_KOm8Byqd4Zbx9uAM922h_pZ5k1uoYjSl1vz8vlRxPv-5gzb1C_1r9HxPxMLTh05VitRHlykj8UWeUqFhSuSl0QDQuCgBEgwvF7BcM4dYCkzVtBGjTe2wYyqL-J2QE84KPmFETDAktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27207295.mp4?token=T9a1RP2eM8Uhu0QqBuknHatm1jN8IC9RQOwHh9527rZznzRHBEbwwQ_TZtVAC2z_PseWUMuqXZ6W5QZBOaM0d_NOGucqgrqGhyZXE9jc3v77F_9-yYwfOqHdYLIyqqoMvOIIQf17LPVGIpXiiPw6-tp54RXFrBAca8suGg1uymQCCd2hL7umzVLhlh9xlF7pszG-LoAMnCn_KOm8Byqd4Zbx9uAM922h_pZ5k1uoYjSl1vz8vlRxPv-5gzb1C_1r9HxPxMLTh05VitRHlykj8UWeUqFhSuSl0QDQuCgBEgwvF7BcM4dYCkzVtBGjTe2wYyqL-J2QE84KPmFETDAktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
🎥
ویدیویی از ورود تیم ملی ایران به هتل محل اقامت خود در تیخوانا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132959" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132958" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
شورای صنفی نمایش، با پخش سه بازی ایران تو جام جهانی در سینماها موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132957" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASj8a-XBK6b_RRc9Aevc_nXaIHKlJVwzRRIBtjK_e6R0GCWuIqUc6tl0pJirr1zP-20Grh9pydGm3C6zlwfwy73YzwnhhgGt8BH-neXpm1ADM37661YBWZ37ZK5psF0CXiTKNlDeLsJ0-B1f3_3RBV7-nAQtLhpR2QXHpbPDcbUnU_NGRIpqTSnu-KCFjpmfPJUL5mupFRusWOOQwO5ehsPIkcfl9rwgyIr_Nv16KhRHWb901pIgKz84qYaXLLjGCEHfDmtDiUNB1YNm8-q9k32ov9YskeMgvCYmeiPsRFf6ZGOvkQc0FF0jLbUzXDjomSeK0lBtEYBFAbXJmQWeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132956" target="_blank">📅 18:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132955" target="_blank">📅 18:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132954" target="_blank">📅 18:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5WNCb3kWk05PLS7lEf0XpEvjrAoRWDJXVX_Z1E7CFT9yQJ4CSaVmtNm3E2V-wwgr6iCH1lOJiY_ihY2EzQoJnTYDbdP8UDUAKe8YIQz5DZqegQC2nw_N3XQJozaqhB8lbma2jBM06ixGZuP08vDgcJitluv3vCgX7mmp5TA8wGSXr42Fa7YOL5wHvDWi8-uo8KIBOVhVqOoXsY3uwRiCDewcVW-9mHFKA29a94rBn9-8F64kCnDL9XbApVflHAhjS93ESPpPz4n32pv-YRBuzcolpKlextX6Vq0puQimTg4I4DdedYZ55auNqTuU8FYotEIObf1qmrPOFemZK3G-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:
اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/132953" target="_blank">📅 18:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته
است/شاهین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132952" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
🚨
برخی منابع معتبر:   خداداد عزیزی حتی قرارداد هم بسته!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/132951" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/132950" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
یه سری منابع معتبر اعلام کردن که با وجود اینکه محسن خلیلی سرپرست موقت شده، خداداد عزیزی افغانی سرپرست قطعی پرسپولیس میشه!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/132948" target="_blank">📅 18:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrggkItKdfpdh9bnsEy16qjOpM9bdNXfgcZtRSFlRblYRUtinrwc4OhmYQzzrO7XXOW7w8TfxetYyjf2aGgiZW4kGypVY6XsmTyhQXaJudcU0jltsw4AmXmLEd0_ocuurjrsq3yByck2l7HkqPaj25qTuqBdn1wSvtMUVzmokfWj4-_OoytttkZ4eKBNdagF-Sh9bR5jI_Glu1jeFxmDI5ESfXXfXOWjY_qrdr2PZWp8RiClolpUMmfg9C6Ugyz8sagcDZOSreFr699wEavYWm24bzALkHoIhK7kXxJ29v6NtdImyG4U8wo1idGY_IDRcNzgpKCxnCCu36-tn7mrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری منابع معتبر اعلام کردن که با وجود اینکه محسن خلیلی
سرپرست موقت شده، خداداد عزیزی افغانی سرپرست قطعی پرسپولیس میشه!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132947" target="_blank">📅 18:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHfEOSqskYHMKyCcfYctLMJWasJUehanVQHOMyZ4G3xhB7dvNnPzFzW0c8DMxuY2MbMcX7y_2WZcABnOwtMkTJp3CmJMGvSUfdPV905_wLUbjl8GW2ypnXA_mRnUhzjXMb2kiOH4GbAIr-QtPtqQ6q2q56iP8i-K2xD_JlblVMac6qyw6ny9EDNMSNxlI6Q2dJ_Ix56NAv2dtlW6JX5q08OZiPQTCSPtjtzcGXFQ6qBgcDeeGM0Wylcf0zj2snIq20fu2CUAcVr8yV6uGRN6T4lBmBHJCZSQpIPBmi6XFRp6orwU9KGF098V7ns-nnYTkhYJngboA-c5JA4eBvwu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مارکو باکیچ در حال گذروندن کلاس مربیگری در سوئیس هستش تا مدرک A اروپا رو کسب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/132946" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
👈
دونالد ترامپ به NBC گفت: اگر با ایران به توافق برسیم و روابط دوستانه‌ای داشته باشیم، با همکاری یکدیگر اورانیوم با غنای بالا را جمع‌آوری و نابود خواهیم کرد. تجهیزات متعلق به ما خواهد بود و این مواد را یا در همان محل از بین می‌بریم یا به جای دیگری منتقل کرده…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/132945" target="_blank">📅 17:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/132944" target="_blank">📅 17:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
🔴
ترامپ به NBC
🚨
:
🔴
مجتبی خامنه‌ ای بسیار زخمی شده پس شجاعت خاصی در این است. بسیاری از مردم ، اگر آنقدر زخمی شده بودند ، درباره این که وضعیت ما با ایالات متحده چگونه است؟ صحبت نمیکردند. ذهنشان به چیز های دیگری مشغول بود. پس شجاعت خاصی در این است. اما او…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/132943" target="_blank">📅 17:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/132942" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
👈
ترامپ درباره‌ مجتبی خامنه‌ای : اون منطقی‌تر از پدرشهِ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/132941" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/132940" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فووووووری و پشم ریزون
😐
🔺
به نقل از فرشید حقیری: با تصمیم بانک شهر خداداد عزیزی به عنوان سرپرست پرسپولیس انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/132939" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
باشگاه پرسپولیس معتقده مجوز حرفه‌ای چادرملو مورد داره و تایید شده .نیست و با چادرملو بازی نمیکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/132938" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
ترامپ به خبرگزاری ان بی سی: ما می‌دانیم رهبر ایران کجاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/132937" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/132936" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/132935" target="_blank">📅 16:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❗️
شایعات؛ خبیری به عنوان سرپرست پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/132934" target="_blank">📅 15:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
با اعلام مهدی تاج ویزای ساعتی ایران بدین شکل است که یک روز قبل بازی وارد آمریکا میشوند و بعد از مسابقه خاک این کشور رو ترک میکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/132933" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
✅
حسین خبیری مدیرعامل خیبر شد و خبری  از اومدن به پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/132932" target="_blank">📅 15:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/132931" target="_blank">📅 15:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💢
شاهکار پلنگ مازندران مقابل شمیل ممدوف را ببینید؛
رحمان تا ۴۰ ثانیه مانده به پایان مبارزه، با نتیجه ۱۰ بر ۳ از حریف خودش عقب بود ولی در نهایت ۱۷-۱۰ پیزوز شد!
✔️
🥇
رحمان با بی‌رحمی طلایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/132930" target="_blank">📅 15:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/132929" target="_blank">📅 15:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❤️
تمامی بازیکنان باید تا فردا خود را به محل تمرینات برسانند و در صورت غیبت غیر موجه بازیکنان با جریمه انضباطی مواجه خواهند شد.
👍
دنیل گرا و باکیچ دو بازیکن خارجی پرسپولیس هم فردا و سه شنبه وارد تهران خواهند شد و برای این نفرات نیز بلیت تهیه شده است
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/132928" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgUr08yPg1Uc11ZENVD1tTXgABUWBMXlD5kLQKSw21tGkqMZjCanY_jJ9ItL8J8ybKcja7nP0s3NexjrhMhsxuVVD-_YRAXVBs4euF3caT6z1z-bgXh6NZNkuiriGRmTY7SA9vTxHofKviZ2mC8KWgoYLvhNN3g4zY0MXFt3Stzp7AkTYbFYsegZosDzDh6c2yPc2mLoLBx_r0M_db9aAUyZTZM75DsCFJ6yiLgAwcpy0Ldqr_VcuHWk3Dw-KNIqXXZ3OSraWJXyO0N8vIi9RbYKRLsN_CX-3cozy4hRMwxDUTFep9MOJwI55Im7hDfB2txaUF5CbptKcDB9mfalfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132927" target="_blank">📅 15:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132926" target="_blank">📅 15:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎙
🔴
بادامکی: دوست دارم به پرسپولیس برگردم و کمک کنم؛ تیم ملی توانایی صعود به مرحله بعدی جام جهانی را دارد
‼️
پیشکسوت و مدیر سابق پرسپولیس:
🔺
با پایان بازی‌ها، قراردادم با باشگاه خیبر خرم‌آباد به اتمام رسیده و در حال حاضر مربی آزاد هستم.
🔺
تمایل زیادی برای بازگشت…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/132925" target="_blank">📅 15:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎙
🔴
بادامکی: دوست دارم به پرسپولیس برگردم و کمک کنم؛ تیم ملی توانایی صعود به مرحله بعدی جام جهانی را دارد
‼️
پیشکسوت و مدیر سابق پرسپولیس:
🔺
با پایان بازی‌ها، قراردادم با باشگاه خیبر خرم‌آباد به اتمام رسیده و در حال حاضر مربی آزاد هستم.
🔺
تمایل زیادی برای بازگشت به پرسپولیس و کمک به این باشگاه وجود دارد و هر زمان که مدیران صلاح بدانند، این اتفاق با کمال میل خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132924" target="_blank">📅 15:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎙
🔴
پیمان حدادی مدیرعامل پرسپولیس :
🔺
با سروش رفیعی در تماس هستیم به معاون باشگاه اعلام کرده هر زمان که تمرینات شروع بشه به ایران خواهد آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/132923" target="_blank">📅 15:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMRyfiF-n1xyi4K6q8O_8oCB5lV0pjrDf_yWcEH0BXzXdM1s-lRgMvLVPQFSMEcwxCJjm2uV3UUewPIC18ctNCU5JvFj8jbP2SVzFPj5OSwE0GpWO4tV2gvy6TDMBoYm_IwGRvoOEvEs27AgcWjISurnNNon1fHVCnt7FzPyhKKpia_AXDcKUwAn1LNFhwWZFviLhDGwnT-uu2nOcrZB_h3aGI9c_imT3jVc6yhRLwMJlkDDQ8e4Rsj50ycYdWXswDyCkV-lJQVFVsq69gXbWPJA7cq1fCQt3RYcmXOToXDwjuqFvEYPo8eBPDf1Tv0XlXX7Ihdghp5Tzvp8pg4KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس فینال رولان‌گاروس بین
فلاویو کوبولی
و
الکساندر
زورف
از راه رسید، این دیدار
هیجان‌انگیز رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132922" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
باکیچ و بیفوما هم برمیگردند  باشگاه براشون بلیط تهیه کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/132921" target="_blank">📅 14:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
زمان بازگشت اوسمار به ایران مشخص شد   باشگاه پرسپولیس در تلاش است تا شرایط را برای بازگشت اوسمار ویرا ظرف یک هفته اخیر را فراهم کند و اگر چنانچه مشکلی رخ ندهد او در این هفته به ایران باز خواهد گشت.
✍
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132920" target="_blank">📅 13:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132919" target="_blank">📅 13:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GknrXBcABMQ0_wGvdNBrFQPqttJR0YKrNcuKxVf_WpPhh8KfW-UhsJV-oThRfHbuapbzArdiTHeHUVZjzmm-lo7lO43KGnOr2DP8ICxr4sUvXVefON5kUJU5MMhWgeZ6PCNgYbv0VgvtxBJJscYFOshpk_jriDc1qTVh1jcZNNJayEaPzpzT897fBE0GcMoe22S6tYFqkraCwJzZUkEv-0LMTLZt0zi2DSb8CluQ0BRdxt5MQhd6nVdatNPnn5zUxKL6NGNsbFzELnE_kukoGdfVdjbykk63BJQOdNqMeQDgAX9a3DeQBUEqtQe1vpMjqpK1S4-RQ7iHJno4Z-L3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
نامه ویژه پاکستان به آیت‌الله خامنه‌ای‌تحویل عراقچی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132918" target="_blank">📅 13:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
رویترز:
✅
کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
🔴
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132917" target="_blank">📅 13:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#تلنگر
🚨
‼️
اینکه سه ماهه هئیت مدیره جلسه ای تشکیل نداده و‌ از زیر بارش در میره به کنار به گوشم رسیده دوتا از این بزرگواران بیشتر از اینکه کارهایی که مسئولیت شو بر عهده دارن انجام بدن به دنبال لابی کردن،زیر آب زدن و به نوعی خارک…. بازی هستن تا زیر پای حدادی…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132916" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#تلنگر
🚨
‼️
اینکه سه ماهه هئیت مدیره جلسه ای تشکیل نداده و‌ از زیر بارش در میره به کنار به گوشم رسیده دوتا از این بزرگواران بیشتر از اینکه کارهایی که مسئولیت شو بر عهده دارن انجام بدن به دنبال لابی کردن،زیر آب زدن و به نوعی خارک…. بازی هستن تا زیر پای حدادی رو بکشن به نوعی چشم دیدن این بابا رو ندارن که پله های ترقی رو طی کرده و به گواه اکثریت بشدت پیگیر و مسئولیت پذیره و دلسوزه و از جنس هواداره و خودش یه روزی رو سکو های آزادی این تیمو تشویق میکرده و الان در قامت مدیرعاملی بزرگترین باشگاه ایران قرار گرفته
❌
♨️
این کوتوله ها بنظرم بهتره ماست هاشونو کیسه کنن و بدونن به قول گفتنی مسجد جا گوزیدن نیست، یهو نسخه همه تون رو هوادار میپیچه و به سرنوشت بقیه هم کیش هاتون دچار میشید از ما گفتن بود.
💯
یهو یه چیزایی میاد بیرون که پس فردا دهیاری شاغالو رو هم دستتون ندن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132915" target="_blank">📅 12:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
تمرینات تیم از فردا استارت میخوره تا برای پلی آفی که اصلا معلوم نیست برگزار شه یا نه اماده شیم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132914" target="_blank">📅 11:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132912" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132911" target="_blank">📅 11:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
قدوسی: اوسمار احتمالاً چهارشنبه یا اواخر هفته به تهران برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132910" target="_blank">📅 09:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
رونالدو بعد از 3 سال و از دست دادن 14 جاممممم بالاخره با قهرمانی تو لیگ عربستان اولین جام خودش رو با النصر به دست آورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132909" target="_blank">📅 09:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
رویترز:
✅
کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
🔴
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132908" target="_blank">📅 09:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwaSi3S5UChOsITOCvFH2gKUUkRVC__-X92gOPA65chEi8y-qpxvGeqv0DLVpiS-dDgJa54wNuUgfN-AFrhVCPiCO7MPHczRIkbX8Z-fbMG3weRCYF3etQ0_iy9jJsYwKlU94WoAwM86WrhSCldJVETHS1BdZWh6gLOU18LHhn2PANK74Y1mSh3HcJPXTildhRT3WhVzLOKela9O-rqcznOcJkdYKdHXOouA-Y9b3oJIYGN8IOhbAq9oPGw2APBPgaE79iqLdXxkNUmDWobYvKoiE3TXLMlKozOI7-XPrslsqi8E1axtUJkGRnXwaLsD3opYwC4SYiGM_-oibGSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عارف حاجی عیدی به دلیل قرارداد بالای که برای فصل آینده داره در لیست خروج سپاهان قرار گرفته
/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132907" target="_blank">📅 09:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
آقای پیاتزا ازت ممنونیم چه تیمی درست کردی ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132906" target="_blank">📅 09:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132905">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
خیلی از هوادارا پیام دادن که ما کارت ملی مون نیومده نمیتونیم ثبت نام کنیم چون شماره سریال کارت ملی میخاد….و کارت ملی خیلی ها از جمله نسل z هنوز به دستشون نرسیده و با کد رهگیری کارهاشونو انجام میدن
🔺
بخاطر این موضوع با باشگاه صحبت کردیم که پیگیری کنن حل بشه…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132905" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd44R0LUMihFCzH9FCR7KsqgrBbO1uJAiMZ1JyL75_nllZLATqY6JiY0EjZZVvXbY_807dzQa5TJpC1x7eNoIUkZBBlOiK8Nf_U56gIhv7a76Ki80KTqzdXtN5qFaa5hRB-smPtBbOYaZ4mcTkdHSifPdDDsy7bSGTqVl0_zkBkJuQW_67tIqtc5xjjh_fP8WQEEuQMkQnvXWt1X0QNAw2BogZ3frY9-juETWBp7B-Sru_V__tBwzC2EYhdvamuQ44FaTF41gX1yWr5BiZH9qp3OEMUXsrHyRLClaKX7tG2aqnQanHobwAD6Sja1Ens9MPLN4t0ok_oNrMpWtELS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132904" target="_blank">📅 01:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OesdnI4fb9XqVMiGCscSWMCNZ7AGBRzfIkx_S5kumsoayCh5zQdT5AhvWq3W7hptLJFO8c0vA1Lbb3u5pr_M-fCSTqiaWTySSZre1DSsk46x62ORmQ4c0t1Q2F4KEbC6CTpIAzfKg0BioyLBso1NEWq72puq5vVKZMC7PM5hIO4-y4ovuegisCrUGP0-C25xugtYLn571TJd0uNCFJMsIOfFcN0W-FtxSKcINjbUUdbzTwtfNGH0t1Vx9GCqlDVh2On3srXEc2pBzfx32z6CzE5BE9qeEYorPT5ZmT8GpiXkMqK3XjD-4IgPH-BP_txmiGjP_Fsw3RK7lJ5HqGViGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132903" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132902" target="_blank">📅 00:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mITg_veiwYQJ-pSpMj1kNNW6_YdhooX-cpoEaQCeGSYMbH56YcAYE5iJg8htAp9qB1cU-HakWGHPds_gIo4nps_C8I4iHTzk3T71W-K0baGLfyWCng-ca_WFPoD0vQp6pOdOhFOM-mEtd2vEXWV-uWVwk4z_oVf5XxgJXlBbgJtkt8tGhXKS66ZzOXMIgiSZh2VOaU2eKry1hdXl64I3LTQTEOVreWL8RrzLjU8Qm_jBMyb51Bx1PWnjhZQrJoS1JmuI5YjvM165Bfk8tV3WP_SgQoPUlMHeUDeJm8rCR8hQcDDG_bTG7TFW6gHjQ9xWuV6TMPZmae11FI4bGQRm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اسفندیارپور، مدیرعامل گل‌گهر: «تورنمنت ۳ جانبه من‌درآوردی است و در آن شرکت نمی‌کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132901" target="_blank">📅 00:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
🔴
برگشتن سروش رفیعی به پرسپولیس خیلی محتمل نیست. او با چند تیم کانادایی مذاکره کرده، ولی هنوز به توافق نرسیده. اگر مشکل‌هایش حل شود، فصل بعد در ایران بازی می‌کند و دوست دارد فوتبالش را در پرسپولیس به پایان برساند.
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132900" target="_blank">📅 00:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_me0XKKebEAMfcQaWvcTsa6xwmXDwvWSgVWWENBqv62EEUAPS0_bEzJ2cxbGewmJHEfepLvQFtpzCdAkBO9z8JvSJfmn1qH0ux4Z5wRx2aJmpJU9lQUDsPEISPTf7SYsAZnGU0e4_7FaYsA8AB7eS9LnZwYxHZhewyP8dCzHFtEILZI7i3zqT0cMBAmgIprrtGtK7iZinFTPMC94AM14IvWgosstBFCcXi3FOQKJTsdA3rgaEKL_uB_6Zw0N13fonaJrkpKd8FlpeF8eWQ0CPQQbqholUFyIALGmVLuViV3oS8B2nPHeEvDx0PBZxfEg0fF68v5igpMR5ymnIDNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فدراسیون فوتبال عراق به دلیل همزمانی بازی‌اش با سنگال در جام جهانی با شب شهادت امام حسین(ع)، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی را برای این مسابقه صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132898" target="_blank">📅 00:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
قدوسی: اوسمار احتمالاً چهارشنبه یا اواخر هفته به تهران برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132897" target="_blank">📅 00:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132896" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
🔴
امید عالیشاه، علی علیپور و میلاد محمدی شانس بسیار خوبی برای تمدید قرارداد با پرسپولیس دارند
✍
خبرگزاری فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132895" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
🚨
#شنیده‌ها
💵
پیشنهاد مالی جدید علیپور به پرسپولیس برای تمدید قرارداد: ۲۵۰ میلیارد برای ۲ فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132894" target="_blank">📅 23:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
همه تیم در جام جهانی هستند تو این دو تاریخ  ..و باید بگردیم یازده نفر و پیدا کنیم و بتوانیم این دو باری سخت و بگذرونیم و جواز رفتن به سطح دو آسیا رو کسب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132892" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
🖍
غایبان احتمالی پرسپولیس در صورت برگزاری تورنمنت سه جانبه برای کسب سهمیه سطح دو آسیا
▪️
ارونوف
▪️
سرگیف
▪️
علیپور
▪️
کنعانی
▪️
محمودی
▪️
سروش رفیعی
▪️
میلاد محمدی
▪️
پیام نیازمند
▪️
دنیل گرا
▪️
تیوی بیفوما
▪️
مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132891" target="_blank">📅 22:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132889" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132888" target="_blank">📅 22:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132887" target="_blank">📅 21:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132885" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
از عصر دوشنبه تمرینات پرسپولیس شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132883" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132882" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
کسری طاهری تا سال 2028 با روبین کازان قرارداد داره و الان قرضی توی پیکان بازی میکنه، هر تیمی بخوادش باید با کازان مذاکره کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132881" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132880" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132879" target="_blank">📅 19:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=cdWA5-04jtyqFbBZWihqG5N2yqL7GtNmQjsrfPIZaAEMmWA2wHYoIEaia-5kuil6W_ZOMSNP3-E_HTanU4qWiHZ3FKw61i3ub6QVzTro1uh_0Xg7Ly4EVT_frT5LTIQK891MuDuDt49DfVQM0-0VTQfEv0ZE-dANha8lC_UygXyPEQZwi8N34NSqnplt8Txiz0rf-Ov75AhosLzEXXnfk_au2LJju9LOXPye7U8eNf3FcWnWff47OTrV0pxT_awbnTxEtFD0QBNJZ3Tw0Dzpa9aJ8AUi8oZUFIMiEmNOFYWp50Qbqy7opkxhKurCj-9SjSl5KoRlWA9-PrUoO4k8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=cdWA5-04jtyqFbBZWihqG5N2yqL7GtNmQjsrfPIZaAEMmWA2wHYoIEaia-5kuil6W_ZOMSNP3-E_HTanU4qWiHZ3FKw61i3ub6QVzTro1uh_0Xg7Ly4EVT_frT5LTIQK891MuDuDt49DfVQM0-0VTQfEv0ZE-dANha8lC_UygXyPEQZwi8N34NSqnplt8Txiz0rf-Ov75AhosLzEXXnfk_au2LJju9LOXPye7U8eNf3FcWnWff47OTrV0pxT_awbnTxEtFD0QBNJZ3Tw0Dzpa9aJ8AUi8oZUFIMiEmNOFYWp50Qbqy7opkxhKurCj-9SjSl5KoRlWA9-PrUoO4k8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حضور علیرضا عنایت‌زاده هافبک جوان سرخپوشان مقابل فدراسیون فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132878" target="_blank">📅 18:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQcTywSU9HUkJP5X_SAN1pkUYNl_QQY_7ffEDWZcwbuRTbpbB11XfNUJHhTtrz7GH8jH-mgxeoWBPuu2x2TxevhL-19xEsR4ImFG1pFOgf_gXySJZjZLVgF3kRMWqdWbKe9EsjLXVVzpxstC5gaxhRb1lfz4m3QL1LMTZIHPT-Q-N-JqITnfcEzegIMbdVfW0rp1Oo1u493VWvoj9USEuatBn84KzCdNyOU2qOXQaVs9-XnochYeLjRml_knrphSfWfEp4HyGMlVMspnTI-E220q38LDFOUJKL634BKVgAVzBNQmRtogynViv5TLXamlFCevXGYKyzJB1iLyiquumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132877" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132875" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132874" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132873" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132872" target="_blank">📅 16:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
پایان دعوای سهمیه سوم؟
🔸
امروز جلسه‌ای برای تعیین‌تکلیف نماینده سوم ایران در فصل جدید مسابقات آسیایی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132871" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
باشگاه پرسپولیس پیگیر پرونده سینا خادم پور و دریافت 2 امتیاز به علت غیر مجاز بازی کردن این بازیکن می باشد
❌
یا در غیر این صورت کسر شدن امتیاز این بازیکن که به استقلال و تراکتور داده شده
3⃣
احتمال تورنومنت 3 جانبه وجود دارد و طی جلساتی سهمیه سوم آسیایی…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132869" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQCBIUSuFfBUqRML3YD7sQ0iX9kDqR-5wdTeTQoezJgJIkprromODCFLCZca8a4hdsCg2Fj89A0Q_U7D0nZD3tx8luSR1Lc7TFiZikyseCidWi5gG3sgqI8jrDWnoYmE_x9x3IdJJV_vOnIZkPGDupwzaOD1vEkbO6196bMf_VZJw1lPNKHYpwqa9hLSlQ8nyuVC6kBCa2DWz_ChJQN23feBge-DYJnleL23JQl1M5eCNLoi93bAN6RNFq9jvIKPQSLKU3fb6SrnInS1WDHGkhcU2P9i036ug69d1PGxAjLnNFn4iNnFaIXueMXcPyiNlZFgxjA5JqGtKZ4krZVhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۸ جفت برادر تو جام جهانی ۲۰۲۶ حضور دارن:
- گیلا دوئه (ساحل عاج) و دزیره دوئه (فرانسه)
- اینیاکی ویلیامز (غنا) و نیکو ویلیامز (اسپانیا)
- دریک برابی (غنا) و برایان برابی (هلند)
- جان سوتار (اسکاتلند) و هری سوتار (استرالیا)
- لوکاس هرناندز و تئو هرناندز (فرانسه)
- کوئنتین تیمبر و یورین تیمبر (هلند)
- لاروس دوارته و دروی دوارته (کیپ ورد)
- لئاندرو باکونا و جونینیو باکونا (کوراسائو)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132868" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132867" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132866" target="_blank">📅 15:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132865" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
با رفتن سروش رفیعی شرایط تغییر نمیکنه امید عالیشا هم باید بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132864" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132863" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
❗️
پل پرسپولیس برای صعود به آسیا
🔴
باشگاه پرسپولیس در روزهای اخیر پیگیری‌های خود را برای رسیدگی به پرونده دیدار این تیم مقابل ملوان افزایش داده و امیدوار است با استناد به موضوع استفاده از سینا خادم‌پور، بتواند ۳ امتیاز این مسابقه را به دست آورد.
🔴
برخی منابع…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132862" target="_blank">📅 15:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=XdDirEMddhistykMLQelccsabdNuGt_QQAEyF6WEpWQ86ag_amKyh-XgPOMYgkl87PN9boLsswGSw-K-18Fn7Xnku8RkUuVoVC4cwqaKyG-MS7AjenXXxybUmc9l7U0JuJT01-YhgkOWLlLRj-BHDSvICz0VbhLOvCpbcyVGs_HXauSRkXqz6b9JRikhRHziaKDfUGjrG8w5v2HA9uQvy119OWekoJKFzmi_PtMrUGGL-XYivv2uVO2VcGX-8RmFvru14_wmXWAy9I_VsdFKAuZaXIzM9xvw1CcE4D1J83LKHjSeLLP-1UNHqMaG2qopyJxi6KE-zNMigMEzI6GrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=XdDirEMddhistykMLQelccsabdNuGt_QQAEyF6WEpWQ86ag_amKyh-XgPOMYgkl87PN9boLsswGSw-K-18Fn7Xnku8RkUuVoVC4cwqaKyG-MS7AjenXXxybUmc9l7U0JuJT01-YhgkOWLlLRj-BHDSvICz0VbhLOvCpbcyVGs_HXauSRkXqz6b9JRikhRHziaKDfUGjrG8w5v2HA9uQvy119OWekoJKFzmi_PtMrUGGL-XYivv2uVO2VcGX-8RmFvru14_wmXWAy9I_VsdFKAuZaXIzM9xvw1CcE4D1J83LKHjSeLLP-1UNHqMaG2qopyJxi6KE-zNMigMEzI6GrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132861" target="_blank">📅 15:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132860" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132859" target="_blank">📅 15:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132858" target="_blank">📅 14:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132856" target="_blank">📅 13:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚡️
⚡️
۴ بازیکن استقلال از حضور در تمرین منع شدند
⚡️
⚡️
عارف غلامی، ابوالفضل جلالی، آرمین سهرابیان و موسی جنپو با تصمیم سهراب بختیاری‌زاده سرمربی استقلال از حضور در تمرین آبی‌پوشان منع شدند.
⚡️
⚡️
آن طور که پیگیری ایسنا نشان می‌دهد، دلیل کنار گذاشتن غلامی و جلالی…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132855" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132854" target="_blank">📅 13:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
پرسپولیس نمی تواند نسبت به رای بازی گل گهر و چادر ملو به cas اعتراض کند چون فقط دو طرف دعوی همان پرونده حق اعتراض دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132853" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
