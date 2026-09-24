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
<img src="https://cdn1.telesco.pe/file/aAIPYp73_FmxNCdL4iYnWczLMmmqUyYG4GL0pNPJOHhTSYQkE90gNKkltN5gIt80WGGY9ssyfr-uEj4sYlBKxA07b6MUJKXXWNkucjNorlV_M-lOnoWH6FUAdvBI72pJ4FXCrgAvU4QX82CIBcS7o_KHPeLAtUOO5kFL7omSwKxj6riwbHGjiau5z7Q3rm9aj_InGdYXD6BQ13CA1sJZ06KceHluzViLX2qNf5jF1qYFneJBl3y9l_Fa_vjKD5kJrAku_gVf-jQ-tz9AnseYNz6boUEaaM9t-BUkqrW1eF7k_y9YRKspkbSs-_5iKkfRs1DWfjW-5J9cyAKydZ72aA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترجمه ماشین:
"قرار است مسعود پزشکیان، رئیس‌جمهور ایران، امروز ساعت ۶ عصر به وقت شرق آمریکا (ET) در مصاحبه‌ای با برت بایر از شبکه فاکس‌نیوز گفت‌وگو کند."
Polymarket
۱:۳۰ بامداد جمعه به وقت تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=Ukrk0JxX8dF4ltdiqv18jVXVksE-Tei9DoRUPLVpvMJsvWieLiTZ5SRoKY16F7NwsNGx5kKNLTAb0rrJTpAzAZoH5HUwbiOoFaMuxB7aZ8Tac3O-_qM44-auN-K66p1mfD54J-Wtj-3QNgnPm0VUMQxEKMj8FqvhPKhzNxEJuA3RQaBorRWfodOdzFPMsOgRUP25hccxJVs95qxlnIBnxr0gZyrWIQEPNNP8Llr_QFwvfBFIL-IXh9XLT-vBNYH5OetBJHtt-hKoVDKbtdVQGGHabavO0j-QW3euC_yLhFqBqMWMa-mX7tW1UJYaU_mtoY-2K-xSl4NE3ttcw3Vx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=Ukrk0JxX8dF4ltdiqv18jVXVksE-Tei9DoRUPLVpvMJsvWieLiTZ5SRoKY16F7NwsNGx5kKNLTAb0rrJTpAzAZoH5HUwbiOoFaMuxB7aZ8Tac3O-_qM44-auN-K66p1mfD54J-Wtj-3QNgnPm0VUMQxEKMj8FqvhPKhzNxEJuA3RQaBorRWfodOdzFPMsOgRUP25hccxJVs95qxlnIBnxr0gZyrWIQEPNNP8Llr_QFwvfBFIL-IXh9XLT-vBNYH5OetBJHtt-hKoVDKbtdVQGGHabavO0j-QW3euC_yLhFqBqMWMa-mX7tW1UJYaU_mtoY-2K-xSl4NE3ttcw3Vx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/254900429c.mp4?token=PhrEcB7WcOtuKFUenaf2mT6LKd7TKYonK9wDhJu44qzmWz3Q_jsB75lukDMZedUc7x_qB8iHKbS3fV02vEzSuzLZvX4v2upGXoVsHkYP6jpNIuNbZYNEp9u7Xl03a7OAPMCQTs8aEd4L_XVZpnxuCxS0CTNuC55OlLS4WgQSKgptFNMd_jwmTnBoDGHSWKRbdpZgRMjeZgxz2d2I7QQuZNYIyUOSoSHysZwNkVAWAUe9vXMxpLqeraeMELaoUbSp79bAKocwb3Y23ZKsds0X7Gcj_jElHNP8O-TW4Q2RMUWiMJzH7FgXnecZm-4tjpiioiQAhCOF-ABTo-0eIxq9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/254900429c.mp4?token=PhrEcB7WcOtuKFUenaf2mT6LKd7TKYonK9wDhJu44qzmWz3Q_jsB75lukDMZedUc7x_qB8iHKbS3fV02vEzSuzLZvX4v2upGXoVsHkYP6jpNIuNbZYNEp9u7Xl03a7OAPMCQTs8aEd4L_XVZpnxuCxS0CTNuC55OlLS4WgQSKgptFNMd_jwmTnBoDGHSWKRbdpZgRMjeZgxz2d2I7QQuZNYIyUOSoSHysZwNkVAWAUe9vXMxpLqeraeMELaoUbSp79bAKocwb3Y23ZKsds0X7Gcj_jElHNP8O-TW4Q2RMUWiMJzH7FgXnecZm-4tjpiioiQAhCOF-ABTo-0eIxq9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز صبح پنجشنبه دوم مهر شرکت هواپیمایی وارش از تهران به دوشنبه، پایتخت تاجیکستان، پس از برخاستن مجوز عبور از حریم هوایی ترکمنستان و جمهوری آذربایجان را دریافت نکرد و ناچار به فرودگاه خمینی بازگشت.
این اتفاق در پی دور تازه تحریم‌های آمریکا علیه شرکت‌های هواپیمایی ایران و افزایش محدودیت‌های پروازی در کشورهای منطقه رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvHatdy8NeyF9kUnn3Qp_XQbQwuDvntKeOCE35zcIbv3ULvdg27S_DaHR1g3Jf7kNCROQLjrX3xFDGDYGSR1zWyVmxYkwH0yeuZCXTz7mUzIpuP0AV5ZwKO5YrVmhEmfwQ68OQwev0vub4EyODo9cdyZvchbIc1MCd0vMdO5dV_q1sWIahMHfqMZTQP-h5OYzzCzC115N94lHQ8IdE6p7dNepwt8MVxMcd0jQbtOn4C2qjOiXi5bklj-niApfLtNC8Yjyqjpg4B6y7wxkaDK0zVKTWzJKae-OY038B-FPhPUONBQBZiCfGEDPsMTvbLNbeq0Pwtf4GjQPdrphGp37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXvBmt0yusVm7S2lxk3ec4yuHMqqncO2RwXjUhbZ8QNXy_gwP5CW2XGPunxiAinDKkUtkP2HBfND7x1aaRScgx8JPdOAmCBWxXC8JPUzcknfj2iJKdE3maGje6BJ0ZK1sA8_ZiAZ2onZUjtJu428q3yKNrP3ByU64VWiAzdHkbp6InkupFOcu6nVSmh25ACFU-mvtiW12F0n_AKvnOaw7SHOa_ZJ47elENH0ZRCs2XCstC56g0F7rwk6m-eDFYB6u8oZPxVYzs_v0kluS1HImcun8SY8-8DjWDdttpCNOzmYC37VwDhSakGxJpEJ0NAHskZBrct9s7ljAV74UqYTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgn9lhzv77nFPMvZu4dlNVbB86knbdrBxIgyXr0PzJTXoGLs2YrinI382Jddzm__7zQSnHN8fVIC4k9oUET1G_n76WPEjsExfeb9u45NeT6kQyYg4eRzUfjl6dtTpEHOlnhHkuAdMOn_x2_pN7LqUzJC7K0npTWjshyuCefxLXbQHoeY4zbgYDLfGY9sG8mOngg0sRcnN_2V8KXCNl_YwbLBryr5f_GHQodj7brj4S0ZuacMYrE7D3NQ6YaU_323khhCwkygxGjhGfw25QmzDY7WTIFcRrBPTQzZ3VEmqyItTDieOA92z3upqJUHDKSXdtOG5Qy14HNpUaEJooT7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJyybGNmtQzptOLX-6DiI61G5bDjmlbmJ-Gy7eYHwl1AFAa9LsAgRMTtpKaUNROlcFGiUUzxF7eVYaSfkPVO4vSY1mZZKaWfGUq9YmiPKGNyzSZgNGyVqvt_0nEPNppAnJsUhv4_idKEMkLP0M2iT6UgSxpJEp2Pf6rNyndahCSFvBOCnclA5bjjGaBinTWPZYfW9V8x8GfGv0a1wF9V-O19TD2iUtSiXwfZjwAiDCMm5mHEM3r761QzftilyE7TTzlkADi9k6cZs-m4ibvJPXqNguoTDPr7hcRovrIw1-OHsQFpob8srSTWaeMJQIid2T6rT19EznRanHXfaPoyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEe9r_gdWNtcVwRN07nm1AMAAC68Rw8968PcGR_PqewIErYswx13GCa3iWuH6W_sqjgnu-CTyK1Ys5rKfTV_615KYN4zZAhyckgBg74GcwlUc6DIcgQJZ6xLqB4Y-UEhzzS-chc5qQXwpKhhGEDO7nMvyM5FxPExkL7d9V7ajhaOXmak2EgaVfeFMH59VDlGREax6hCKoWsUhN_4ye8_7O0LsICKsO7RjJSHTUhXgDuO9Vx8tGzHei_-SMuD1OYVExIEqAYnPMZA_LqlTreed5HFb06gwFk-9T42Jj1XTQcnavA2l9uxYcdBxEudKKAsxT1fW6V6Vv0MQ6ygiBALdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7DHLrHpHaQtOgbkg77C4MJGenGvSUSaZF1kBI-LspI6e8lSoAXNup3wwAgVsdRNABhoiJNZOc5W4Hokyqwn7P3WqbFr9V4VYU7S9kL_tYnoSESQ6eIVw_ztsqsE0m6lznjdluGkFDWd5W3MVbqHsWDnyyR2zhc7l_F6kGRy1D-tDw4E2Pez8gG9K5mDYyj0xnkncIGew2uq1BxkeL88wZsSOI82KrCtPnMVC63eX37q3srZnWQY1aR4eg0dvZLgAPq5v3QfAX2zw0T4qym4Lndk-Hjj5TRPoqd6vGnaVaU5rn_nXmoIukNssfjROxLMYDz6vxAEObVWFuXnBF5_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lV9rvtUT2J86Wt5FIMY2Kqns1clk-lvcM9QMQrjGD-UllF_SjLfQ5X26A-23cqtnJ_JXTmqK82OvzZDdU5HhrfviHZPdLK6IHsCROAw__AtGor_8QMqzljfsGd9gd7WCqgxEm92tcP-HIETLQSVnIkMtAy2-gGXXVe7k70DwzeupNHBj5diGEnqWoL_RqavCf9ZB-gW-h413iXEcXKabgsVsZtQ91thI66zFKDXT7G7SOhfDVBRIpeoXJTuOoHZ3_a-Q7BYWj9xgwFwWidaW3NjsqH-WxemnTqyxTCKQvfmDs8LOSzktT_xCOt9g9pvJNmxAF-5EIXCMs_IR0VVghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=QOnmH0pARQQT5Eq5rNghVb7BSPISRefJcivLL5qRFi91rVPKW4RFY7UsE0wpsIi9Zo_5BvnUAuAzHtjCPvMMfgQeQUKRWGcS7SfWYM9Nz4wHqyVpufz7FxKi9VJrt6JRZpW_Opyjx6WP_plTpDJXBrkMvaywb9ry_Aln3mICQ10Z0x18tvYhP6yy_dHhd2aByHj2n5fgQ2bWrhxreWDfT6JPHVJGcJzJKw1NmyFe2lBnljx8p4ckLsYiyFVcd-gGPB7fR7JyXukBpS75tUWQ43N8urfNPZpIOeKvl8Mt3ZY1j83KZVdMhWy3GOA5gI-I6fOG4MPq_mOllVm_L5aYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=QOnmH0pARQQT5Eq5rNghVb7BSPISRefJcivLL5qRFi91rVPKW4RFY7UsE0wpsIi9Zo_5BvnUAuAzHtjCPvMMfgQeQUKRWGcS7SfWYM9Nz4wHqyVpufz7FxKi9VJrt6JRZpW_Opyjx6WP_plTpDJXBrkMvaywb9ry_Aln3mICQ10Z0x18tvYhP6yy_dHhd2aByHj2n5fgQ2bWrhxreWDfT6JPHVJGcJzJKw1NmyFe2lBnljx8p4ckLsYiyFVcd-gGPB7fR7JyXukBpS75tUWQ43N8urfNPZpIOeKvl8Mt3ZY1j83KZVdMhWy3GOA5gI-I6fOG4MPq_mOllVm_L5aYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4DoWykfClIbxpnrVAalim_otTXWL8V1G-fGdXj_B2rawpKsmUvpynhy1zPDty-wofAbcN601Mo3D_fnn_sABvt9LAgXutCMm2CHAlCgaGlYjUgfn6_ptTHI_s3LKnBhCrVe937KZhmPAWJLtkiexgEr9D4YaQod4X95mMq14kl6rBOytX1Ej8u3mcNE4vrGMFGlwp2pVl3NdcowsQ8-alnL2e_uFPmd5AFAmKlW21KoFfx5JkoHXz1NyGVygkfC66Fma1JzCwO9SykmSQmla4rRk16_xj2A25ZnDp0cPm9lv0lBa4SHZ3OW5Ft6JBKrp2dUWHxt5_crnk7S9qVspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=rGAwdgSzL92gDpWvf9mJZgjccSEAEPFXH9TxW7OFMy2AcDYk8fxaIQ9knhzGDollpyHIeoV6H0gBcKuxtkHfdrpmcJBeg9-VXxDxZxqBmVFF__vtfywjgwx4SJu0lw_bRSp3q3yogjbs_QEKLiIP6A89_o03OUDAvTR8jOe5LC2ML3iWsSk8pmABE_0PsQ6EzD-aHGKWf8NXh62jn5EfjRMuvxVUS1SEBlF6DPm8pvYoc_uc5GkkdKlBS5qibKw_FXCDGIbw7sSYVtsnzrMucT8yIPZz9HMHUr0UBq4HdDyCFsOah8XErojXPxGutl5uyT2NggQnLlVWIxzF_MLEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=rGAwdgSzL92gDpWvf9mJZgjccSEAEPFXH9TxW7OFMy2AcDYk8fxaIQ9knhzGDollpyHIeoV6H0gBcKuxtkHfdrpmcJBeg9-VXxDxZxqBmVFF__vtfywjgwx4SJu0lw_bRSp3q3yogjbs_QEKLiIP6A89_o03OUDAvTR8jOe5LC2ML3iWsSk8pmABE_0PsQ6EzD-aHGKWf8NXh62jn5EfjRMuvxVUS1SEBlF6DPm8pvYoc_uc5GkkdKlBS5qibKw_FXCDGIbw7sSYVtsnzrMucT8yIPZz9HMHUr0UBq4HdDyCFsOah8XErojXPxGutl5uyT2NggQnLlVWIxzF_MLEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=M1ve2HeywhwPmks2AKZeTPHkoZRYBG0M8TGuoKYKBdeXiefWf9bHCfMXByoadTur7uMh5CguBqjMVoSXXnpub_oPP1168Ud4q-T7ctJ4jbUGeh_lUeB-orkgndjC7tK9mp2TH_4Vsweqmbj2DypxKXP_Aart1DEc3Ej9RTJ7r-j742SanmTn3JoSoXdEtvYWl9F3npTe2jLDD5YfWHZxc05xLsBZiTjP4TUUAayOTEB8d2u6jTd8HtUcHjqFK0SXG7D8nnF5-QU8s4lD4A3-P7_ZVwRoe758sOxqsTc2WvAdI9Wbdv-yD_j8FYOs7-XPda8ErmU1nPvh_qTaiC43WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=M1ve2HeywhwPmks2AKZeTPHkoZRYBG0M8TGuoKYKBdeXiefWf9bHCfMXByoadTur7uMh5CguBqjMVoSXXnpub_oPP1168Ud4q-T7ctJ4jbUGeh_lUeB-orkgndjC7tK9mp2TH_4Vsweqmbj2DypxKXP_Aart1DEc3Ej9RTJ7r-j742SanmTn3JoSoXdEtvYWl9F3npTe2jLDD5YfWHZxc05xLsBZiTjP4TUUAayOTEB8d2u6jTd8HtUcHjqFK0SXG7D8nnF5-QU8s4lD4A3-P7_ZVwRoe758sOxqsTc2WvAdI9Wbdv-yD_j8FYOs7-XPda8ErmU1nPvh_qTaiC43WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEw7lZujmxkPk17fLOU7L53u08FbW-WpJNrjzcedFPq83uxu0cBDthYRb_0YDUh7F2qSYFyGz6LVo2ZyAi8i0JPXgCBc1E9zIuC7WTKTF5DOQIFOMIKyS5Nm5UWJSchpIlEGv_8n1xlP6uoVoBO3g9b3tk4QP_A2ExXxWpijnfLAgnXdAOCFQ3T57t2riF41eaKdXUqmToGh4OdCydCANS03gxvEDX6fugM3w-O_dxXdpAiCt3_SNsCgftbNelqemV2JmBv5OQdYaGBIWnWOtn0et8YDbBIPggEWAvKMWBFI9w0xUjB8L765xMNGVEL-iYXZp3BeJ2uGDRJ0DyGLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=Wkwk4gh88cOKFINSLzdIYRbI4wCHszcLmXkADf-awrSkRbBfed8CHbP-abnZqerKqWfJ5A6Q8oQuup8ONr0yWkcMiA9p7_IWvCe1x73XC-kZpfgr3OAjizmGwi3-3pkZGij-6jNneYwB5sjYmonjMsBHXuyEXXv19gVZE4I8Z6gnjg-Ff_EWi13SMvphUvOfiN01zwkm3yLlzZlocRX60oDpnYDxWcfuT7e16Gxq65410kltsz5Y13YvQDk3nN61Qbg8TbCH6a-f0UzaxXcifLQ-0LeOGaCcZZDEgSuJG4b3xJL3bX7TIK6Q6lQmPLR_3Xgn_VrbA01UOzegDlV39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=Wkwk4gh88cOKFINSLzdIYRbI4wCHszcLmXkADf-awrSkRbBfed8CHbP-abnZqerKqWfJ5A6Q8oQuup8ONr0yWkcMiA9p7_IWvCe1x73XC-kZpfgr3OAjizmGwi3-3pkZGij-6jNneYwB5sjYmonjMsBHXuyEXXv19gVZE4I8Z6gnjg-Ff_EWi13SMvphUvOfiN01zwkm3yLlzZlocRX60oDpnYDxWcfuT7e16Gxq65410kltsz5Y13YvQDk3nN61Qbg8TbCH6a-f0UzaxXcifLQ-0LeOGaCcZZDEgSuJG4b3xJL3bX7TIK6Q6lQmPLR_3Xgn_VrbA01UOzegDlV39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e93voClfXXmcSRFql2jxEi3Zih4vPZxqrfV6FaPNoASezPE1D0t7xL0_0O29uFguc3I_f-OFeP2gHac1YbfA6UwsNfD5uwAXTg4djltWlYUbfXH4AxnMfvEoXIgmaGpOfHgCWeM1GzChA6Nome6hwEIodCrTQVHV1tqELh_5fXDe08Zk-zNdLQ5TkjfhHPGqiADkStTimyHj_R7dO9trGYsZ4KhTXc-lrlOtQW_2FAni7Kjf0r7M47yLbqBWupArWc0vgMO1kzW4lm_sXQbMg6DKIHQeMks96ckJZbXhI82mxnO1rm-pu0_PdPX_400XJ6gprD4LaK09SkGiHnxE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=PSHm5jR5DNo3qM_GgIbGz7n2EDL_u8htyeBbiYr8Dq4G4x4cay-0zWXNZtDLsB9XJAvPC7DD-Yq2L0c1ibyrVAVPIUKSJ5QIqTHy_9-Lf0djzDcz7b2Yad0moFfRQCGPGwKvh89PL_-GXDSRvhUUaLFP_bWDMogWb2ZvZ4oq9OiYIJIG-TW6Ni4U3pAMjoQ72Jkz4ti39eVSvHEiIheO0YqdU3cCbAA7MDTKz5k0o9SsKzjkGZorFg8DynByEToMTfN781xzMh8MbgMgY1e__Q1qQ_H8lj1oQTwvPdHGHB_m6EeHx7aFmC4sdxNon2XCd18iiAsJNrHDS2uoNRLnxj4NumJEg_YtKuriOcs-JlZaM_9gTnv1032pUS9vhhZ_4f_l-Rm4ulD6fD188-Bte1TLWrGAgoBN4KFLe0EYZD0Id6ZJa2R9ts7dx8NhMEudYeFwil2hSEVWx5tn3kqsS1lPYWtk8MbOBbTsWFDlLniWp_5UXNOoGU5KM5TpmpS2kgDkyw3nUcb_gXgYALjuec9AkOP6WZc4lfQ0pxUxKU71NsFnLFlj01ou5TbGXBJYMfiLxYjXIzMmhqScU18YuCWyDe9v8Mac-76h-at84E49i0Q1c3XmVVPz8SOSx6FHWM6NJXwbKWR2dlsnK1vhI3Gt40KZorMi8Q7BUML8kGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=PSHm5jR5DNo3qM_GgIbGz7n2EDL_u8htyeBbiYr8Dq4G4x4cay-0zWXNZtDLsB9XJAvPC7DD-Yq2L0c1ibyrVAVPIUKSJ5QIqTHy_9-Lf0djzDcz7b2Yad0moFfRQCGPGwKvh89PL_-GXDSRvhUUaLFP_bWDMogWb2ZvZ4oq9OiYIJIG-TW6Ni4U3pAMjoQ72Jkz4ti39eVSvHEiIheO0YqdU3cCbAA7MDTKz5k0o9SsKzjkGZorFg8DynByEToMTfN781xzMh8MbgMgY1e__Q1qQ_H8lj1oQTwvPdHGHB_m6EeHx7aFmC4sdxNon2XCd18iiAsJNrHDS2uoNRLnxj4NumJEg_YtKuriOcs-JlZaM_9gTnv1032pUS9vhhZ_4f_l-Rm4ulD6fD188-Bte1TLWrGAgoBN4KFLe0EYZD0Id6ZJa2R9ts7dx8NhMEudYeFwil2hSEVWx5tn3kqsS1lPYWtk8MbOBbTsWFDlLniWp_5UXNOoGU5KM5TpmpS2kgDkyw3nUcb_gXgYALjuec9AkOP6WZc4lfQ0pxUxKU71NsFnLFlj01ou5TbGXBJYMfiLxYjXIzMmhqScU18YuCWyDe9v8Mac-76h-at84E49i0Q1c3XmVVPz8SOSx6FHWM6NJXwbKWR2dlsnK1vhI3Gt40KZorMi8Q7BUML8kGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4EnDiFgYdpsjnoPUcTcFhMKHLYnPvnsqj9vwAtkLWHEWCmjodN8k6hc-EPSaBlM6nBMdaR-7-jpTY3wP64MD4sWDGgvD6--q5Q8BL0I_RinEwLYiMrusquDPeVvl80iV3wGT2NKC7R5lW4hOxkDnvyoL3Zq68w-rrEM_IeJMo-TarbHUlnM94l63KtjWrPkCRhTvZFfZETI8FXzwxdxNmZ1t-aa9ipgcCnZ2rwIb71NH9wYz68A9BmaqxFvlF7bGnROFqG4AUCf6jxwvG-BwL1tBo3rsF-qoCgyA1Y-MSOXJ9QeWf4xC9vYpdrRQToAdsCcCP7uOWZ3NkyOPIPEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=VHddQUgBdpoXIUCYdZErb8pFSwd4G-h_vr_6ihDD89k7PA51zM6DuxIILxVhtttVGeIdSLGf7adJSBi-9Rq6W2fScLVac9nH9IijxWRtXv48BbOoosT_ByWIAfwdK5w9wPSvdhk1Sh7GvNhFtm55jWBpBxU6W786OwaBfwKTSwXIHz_KuQiiGaMJtzOtD-erVn28duuInYZb4u_yABGJaVWTNiDCUc8FgHhKxFKspLcc9E8xfGAocgdC-2VqvJf_6fCm2mzAxl0Tt5WqjvuiUqgV5-TTTaruYZ6KAG7DG3ocxRULybFl7uSU5HDSMkOdGP5KLzMc_SqzXduMbJ6Uqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=VHddQUgBdpoXIUCYdZErb8pFSwd4G-h_vr_6ihDD89k7PA51zM6DuxIILxVhtttVGeIdSLGf7adJSBi-9Rq6W2fScLVac9nH9IijxWRtXv48BbOoosT_ByWIAfwdK5w9wPSvdhk1Sh7GvNhFtm55jWBpBxU6W786OwaBfwKTSwXIHz_KuQiiGaMJtzOtD-erVn28duuInYZb4u_yABGJaVWTNiDCUc8FgHhKxFKspLcc9E8xfGAocgdC-2VqvJf_6fCm2mzAxl0Tt5WqjvuiUqgV5-TTTaruYZ6KAG7DG3ocxRULybFl7uSU5HDSMkOdGP5KLzMc_SqzXduMbJ6Uqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmLK7UUAfNNNJuarLGfbvnwVNYwOQaK9LPsl28W9g3dFfcUzPPTN1FlmEe_IIDtHHcwRc8ecMDAIhRO6hxsG-VVOwXuSGEkBBvEvZbLiattTjhzx5yJFt1RpmrVaAKzgGjhUdQX7P4FlYABZIpvDyvod2EqpmR3c80paH9oyvs_B0s001crNpJyMjVer7IOi-k2Rm0HbEnE5KKHw8AGLHxS-0V8PBIx5Ze-p5pGn6Fs6edOE2M4R8RAjyJU1Hc3LtojESQc9_BQAJgaI1ZZzq32Ri2NVVc0ygrKm1qsQjlI75WpCK3xy83Rk_bF2wM_wsaJuSYMlm4R62MUDXvSpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TTXTlP0lnDrn9THUH6dsAymOroyf2EcBwnYDR7Ib3DKHEcuYGqtRHtfqzaxntVQF1o-Z06eqha7DZHx7OmjNalReFCHQPnZoQU7VH-F4-z-XALWO00qed_40y9oMuzRp3I_XnZU_taqxBOYWxe5xUxFBVrkhuVwWig8DCgsWKXPYK03Q5Wmn-EDehiMY7-sbQu1dqR8zfg5uEAJRR_STwEsQIz_bsjUTMvYhDLZVyEMgwuMxdYM9W54vFBXgRu3CgAO6Kbl4HR9w_mKIYtwZB_ONcUS6Ed512DPO0TRV4UkKQffPeoN5zxqSbwAqWLi_tZSOPVTBx8VB6mVheX0kQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKisYlfddgxUbqJjF7GVYiKQzoV_60adzXXm1GnXMGS8WkB82LHy5sdtXOLjG6CDtWmkEj21L87baS-yAmZT_yOrnJWhCeRDIYHHDuepuMczJyPkrRFo9ViyIoBuuaH-8QQvXL7H4wT3aJMz8J9wPW3TSmGKBsJl-xpJtvShxelo9-6qg13oxK2PqMasCdm89OCfO8289qnSLqIu3S2ECzP_AD1WRENZ0Y-fLZSSzLexWHiw3LBOXWHwRGeVGwS1fH3iO07z7cxYPqEGdaRFrZPX4efjO8rQsHNV7d1np5tjZQARlOrEbp_HL-qg1iFLOFb-JeWIp0PegXnEE0agAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UBQqPW90Eb8akmJbwnBfRViPxOL-TdWZQqdC3VKMkwJUsQ9qWxl7JchOB72phZScKSVhnz04xzNyQIhsJcvyf81ZI5S3wrB4Z4dNjKkIzizolCdJDMlJrDtCXqGK43NTRN85ZXy804Zs17nqK5F54Bc3C18nObMnx6dr_Fb8p5jlb7e0KpAeCFzVJtPK8AHMwRMm_nsTQ9zyHhUZkzMDM0So8fyPE8lZsrFo7mX5oSa4zGQ5GuANkyaltdeSZsrqsY9PEykH3RLCSfoIFA6dnIVS4k75wNEaMtr9KtPH5RZXruDnvykrxCKdDJtevC9j6bMr__mAzsB59cqkTFKwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTA2vQgXQA4uddJ0jpL15ONuNiYxwqsYYBw4qV550ZeAZ4CPkVSk7LkE_vJ2IrfjO0Bp1wUONt3XW1E4-Nq8_T-TdwzOzCeWszN7qCXftfnFuk8fO_u6lp33Db4CMi_OQTL4VYugdmhd5LmH-qW6QwDkNHLRcG7dISTofo_qbvP3nHr8ofSIBNLUaknuIK7JFA-yeQfX3FdGTV3l1SyAqDK405JLyQ54MSHbFhy5B4ZSbMARTcKS5M9fnnl6Wo0zMXUcWmzPM2JtTPr7K7S0UePxUjtxH238bbrVdZzkrh8gq1c0Vn1GIXmu5WLeMErAJN8I8P2JKMgplvYfwNN0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPp426F3_EsC33qzJ5WTvd5tid_O6gfPg1xsmHm0t6PQnVvzuNfv6P1NQiAW_9YuenNpDFMPhu1CzMdu6pCKz-3TCAUVAWLlsLnmhWtqatmmHQ3-bWVpG-lKKcZVl-fGFuF8q20X0pSUJs8J1curyCwD5iQRzvfuPa780pejswK2udUPA0tvgbGbG_-2xcbqQg76XMFwHpY4XHMg8GnR3PPUEcFfYapN-mPbWKiA89OiSBqqwqf8yU9n_i4-6EfoFY0dZAUygugHCKr_KkENsHzHNvUzRRfVvopwV9FR86iXdPSpN92hh6Q8nMKOAfmYVN4VVuxvzdTfWsyH0P2OdpmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPp426F3_EsC33qzJ5WTvd5tid_O6gfPg1xsmHm0t6PQnVvzuNfv6P1NQiAW_9YuenNpDFMPhu1CzMdu6pCKz-3TCAUVAWLlsLnmhWtqatmmHQ3-bWVpG-lKKcZVl-fGFuF8q20X0pSUJs8J1curyCwD5iQRzvfuPa780pejswK2udUPA0tvgbGbG_-2xcbqQg76XMFwHpY4XHMg8GnR3PPUEcFfYapN-mPbWKiA89OiSBqqwqf8yU9n_i4-6EfoFY0dZAUygugHCKr_KkENsHzHNvUzRRfVvopwV9FR86iXdPSpN92hh6Q8nMKOAfmYVN4VVuxvzdTfWsyH0P2OdpmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=QONTTAiPeXZE1fhTFkfAYFCQJjO_jCB8vDkXu1Uk6dd0pusqN28x1sIy6Yb7uy6o8psbrA28WQ-oIIFqU1PsMDYTjU-_qG1xVAvhW-US3CvL7y_gQ51z8wuwKrJUJ4DnHPNeVD5OdNrxMaFyB_oFJSKwCdUmSGqZUUx_ncm3I3OjPwQLTyM_k2s7ZHB2GEdiYviXKNE85jEFBgloDccxZu0m99m13DmORD5LR0z7EtHXBrgumbCJmnmEHMxAu4s1XH2iflj92e_6nEiSZfM82xTgIYjkfWolux9BQrUwprCJColK53Au1Y_DOIheiSqTS5WlR8u8-t2OQs_a_UVnnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=QONTTAiPeXZE1fhTFkfAYFCQJjO_jCB8vDkXu1Uk6dd0pusqN28x1sIy6Yb7uy6o8psbrA28WQ-oIIFqU1PsMDYTjU-_qG1xVAvhW-US3CvL7y_gQ51z8wuwKrJUJ4DnHPNeVD5OdNrxMaFyB_oFJSKwCdUmSGqZUUx_ncm3I3OjPwQLTyM_k2s7ZHB2GEdiYviXKNE85jEFBgloDccxZu0m99m13DmORD5LR0z7EtHXBrgumbCJmnmEHMxAu4s1XH2iflj92e_6nEiSZfM82xTgIYjkfWolux9BQrUwprCJColK53Au1Y_DOIheiSqTS5WlR8u8-t2OQs_a_UVnnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e61BxzIwb8wRlHDdy8UGhN9qZR7HFqcm6DNPzAF7xBSLKQ50Lb0P-Ynh8stAgFh-EdCj-BaxuGkhQKZsTlwjmObCs7UC0qbpXs1D4skrR5e9fvt97QZgP8sZxsh4DK3tIHoDnJ7hZgHTN8OZZfBaDUAc2zvdryqsAtgZy-XTsjrs2b15FMCrbzggyDAqweBpAyQI8saALZopLDk6Rj99yXyAR5Ty-btfZEX4AoyASUQdV8sE0XOlbJhZz0Y9zsi26-AN0xUTn20muSqCxsmvjSgZOTmeRvcXmb37QWfwMRi8spNe1LkWPgSl8t4nuLbxg2K_ovwcvlJcu2XiQNU6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVMAzlZd1seFfLumnd_KvQwkKHiRqR0qN_kYonsHxTqiDNFj08qtVyCyqbvW5padyaYVz5m9JMn3f2yH8tg43FFsUfNiFoLf0fOvc96IRtwbdBKZablUyUEYKb3BPUqFfnUWHqkesPG4PzCiLC9lYGsldDiGPFHAGofe0VkqCOW1Xy_2nq3Vw7n_wvfgNSwHWDUw6SRAYxqSMdqmEptNmc5Wczl2ce8kFMHanbwsKNXx5r3j7x3U9xIReLngO4yl2MCLH2bWe4j64NYQV_iGIGuY3B1A11BjVwRM2uy7FoC3sCsQqho4UO-4zXH8mhPjYxlp7snjJILE0g7zePNocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LDMQB2Yis5ab4Zwy6487wAaoNYowlxM44BPfSIrwz-3qN-30j6fjJS9aetISkD5_dG6K72lAGGFRvyioMbGkOkjAWbzTD2jTnPXtujYxyR0pfGm7XNCHZMjwcOnqfvx9QFJjH79eV43U5WHB6Uk_zjJgZHbNFQ0eolPjTZKlQh428t8_nraGwciOuovBH9m11jehCxXutyV76Uq4T5faHp6HGI1egY8IEe4-tH8ShJHJ41dso1fYGlS66lTTHNZ9IsIchUw2Hshq-h-QX-ZxDtJQg2bx0bMOJqBRbim1GyyUZA-dvTN8gAejBSi2lKEYdrDhZ1-Gl3kCnXR_DjWcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd0yLk_vvTxxlcV8E0A_oAhNDbmG4yTTMlGWUEgCbIYM_LYirVwRr7sPd4oDCQZemdBALZjGjeQ0EvXgT66CoiXou4a-lRXDDM-EAyOFoFlITI-nEziogZa2S7IHAXNDI27caOFNUTBxQsLNqZAIo8J31Qz4SFMGUg2SDqxQOxE2pWQ8hpTAuLt5RrXtg8kUpjtpStpIDjHlg0nbbOcACV_fHE1bM-GL_iJum78EjWRZ7WsfrHF5QQqQtl6cDYRX2bYLQCODkg469zWvOB0VD8dfwMOv8PmDv0JL8oDf0zIUJZ6Vh214rNSy5q0JAk8E591TTePZRfSaHNm71q-ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzAPOiFSZfJMmvr7BG-_jUJjSfdFDBwq9_Ko64oYCjbzLbMBoJPq_uFIMId0R933L5k1gpmR9EE94rn_Cz04wl_lCy21JDA9xl5tpbCzrLu6drsm_eUFsCVT2NQ0lJVF2cH56SGksXnOZVNI3J_rnmThXI4F0sa1UHsw_mY9gyrvRkBoM9dTLoSYFLTn3CMBIfItmbC08QhtOuApJnu8Thf3ldu24H251uNIR0iP__S0H-Xhnpdeye7JZzCYx_88SMFVbeMlvN5lK5AFC0C8alMsGE08p7AVlgKUZTIT1ibWTC3kJkmFNmUqP4l1X7jsqZN5qzOpWkbMDaCeZXQ7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSSnvQR_PMC_CM6SZD4Nduc6n2zBzoIuPKfILzzzZjF9DImaJ3p3V7_wC2Nre-jz8sEo7obw15CTfUNExOT79vkYjXgmOUM6z-i7QtBBTEXB3C1SzRVOwgM6Bl-721afiLmNPaNfk_2wDEGuggRdmUNqRkboIkMHtddYe2Ezr7dLx-Fj8nIxV67qrFTEzFaCfcWHubee3gIr_m1bF_2ghPwUWVnVUT5GmsQdP8WnOc051zJ_JNEIGVukDTwKGomYUGVZIGpozxMuPT28GwX_fflF8_-0l7NntZoyjIiytadjuxB4qRECuCvzFtmAfF1o3XnDcLl_l2wA112CHyHz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tixPlD_YX_lTL3zjMrhGjT3Ee6w_Hya3Vd_L0O56oLXMGInqWDcnKo2-mJSDXqLtgjQ5vfRxqmDULyj-rulhqdHuu-x_l4fOFgc19PVtvhg61txIUA1sHU3OCvXB6p5f-oVRMMldMghTfEluREaluhnoEHn_0lVg6zYByc2B6Be8HAra1wMGZCO3-gX4vmvfeus5WIXUmJ2AYcwxm1EbMNNUkrp2jD2Lf15_97JbG3rfsJ0mm5tip9msz0eaHqtnwUt5VI6Trg9WbO9LbUD7nEz1v3pUd3lfl8IIhA-M5hgd26FfFEBLd2QQGNDtpegxHcT75hM43T9f0hamUCngBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNdY4sPEFsQCRkcAJMssY1HFOF8Ku3_aIi2KthMP_omYkrm41o4AKzWe53tE5hENZyhehl-Vsh6jjyaK2PlOWQB2tMQj16F-jT3jRWgg7FtKKkx_Ed8Arcj2jW1rSzrvRlxnWVnhMN8k7yWn84mRB9oP40EDsf8rgLnjYBBx9ECAOI3rIsQyCphH20Z90JFGSELIbu7hmm1cgnhNGH0XA53n7I5sKT9n6K_bXMKo42bkXjqCMCik7Rjgxs3Oh1iCPjNR6oi16mgw2A0pKYYpZORcm3LMmALPKd39s7KezbH8VW8qt1YI_XRG9pBSwxZ-g6g2CJFuKnV9CIkrVzBWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9GoSkuBRaB5Rkm46bDOHpU_dmFYAdMgvXQmMkZroKaygyyXgBYzoOJqcZUJNMTZ-YGG9hN0zGm6rsiQZ72X6latKev4__F_qMt9rWj30ofZIdwJTiH2HDFB0qWKLrhU9AyeR4ia-e5mM0GUXeNU9gs9L89z4RbAhQ6Bwk4cdzg2uTaWFqNc3eTUREn6Ltz38s7w3XGCZ3qKGTjdYubVL6xxr4--kNIZJORFm9QfC42E7EoW_I97JjY4wkD_qdk0--topklrTq_WB1BIytpeq3ew51Q4ZzErcta-V7GRGwUm1UEQ5Vr7Cc0D01NLtP6zZdBoSBJ7I8QWkhhldyMV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNSn4X2UKBVgSrIyoueTMed4GZlxN3yyhT014P7wyBCPisBLxPvXNlz_fgXL9nD4XYP_MWoqQHempJFr-eE1iSq41hnGC6O0x68FKV9EUFRco0-8CUkA7Hcco_pHtM-ITnLjLaDgDZpfvHi5_-kJjJURp2z8yM8IsZE5lEPOaM-In-Jfj7FBbC2zdZBM43S_MJGKSz9ilzCfb_9eR2omytXKdk4Kbsz3SHzZdgN81x83p9rwJm6KJ7FvEna2ogGpoHE6uqYhVvgsAS9wbhVboa2y1u_fddi5yPnn4yxb-WyQnZk9ILFCjqmTMyy_GqOWe8wfPQUnYxG5RPshrdlsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0-93poZZ8BxdLzrIfhW5EEn3_cPtSaVhNw2ybh5cXW00Z8kFkjdDSi3y-kXkScxBzgpsiOJC8pVW_l-sEIpykgEtkWurcaS2Su6-QEiEQUkXUvYfeXUrver99MHFrMCfWz8n6DfUD7MnkHoXJhNHfgHKiIpFIV_DjK6YjI5405uPPnixfck9ykcwW8r2Ou6AZxkSYQBfCehmVntUlHki-HPkZnG53PYeVjL_1IM6w8SMJzwrNL0rSp5xoLySUBw2FI5Jv-ED2ebnRg3OTNjTlbyMhQMRvgvMYudBHbMs_fQCgxPeq_OOrfB9VU4JCZpSxwKUDMru0JtPIh62J0UsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=v1AbTQqjV0iWOKHc_lKw3Nvh2oCS_cxJ3CYYtVZEszSTURpkKiV24MBDtNrHjux0MA3iI5Bjtqq_8aLheH1pDOvdaeYOJQwwe8fP2vbFkYC98oE8tx3AZaxKaENFihaaN7hRFGXV8fKRMUdsQDXeRCYqqQkSs83IQTqbS2urMB5x2DgRFL2hMZZRWZrhzoMZHL1C_QjcfVtk8JlDFvalBUlAkFMFTU5oSPDpD4VULLjdgwRaQEAuFOGxSH3f3ZEo54WrqoHUtT8Y1tX5DvXr1C6TjtGQCw37BR7wUQa6Q5u6Naa5PUwKbNNdHxDrnWJh4PX_bxbbOYEWmE6O2z5IzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=v1AbTQqjV0iWOKHc_lKw3Nvh2oCS_cxJ3CYYtVZEszSTURpkKiV24MBDtNrHjux0MA3iI5Bjtqq_8aLheH1pDOvdaeYOJQwwe8fP2vbFkYC98oE8tx3AZaxKaENFihaaN7hRFGXV8fKRMUdsQDXeRCYqqQkSs83IQTqbS2urMB5x2DgRFL2hMZZRWZrhzoMZHL1C_QjcfVtk8JlDFvalBUlAkFMFTU5oSPDpD4VULLjdgwRaQEAuFOGxSH3f3ZEo54WrqoHUtT8Y1tX5DvXr1C6TjtGQCw37BR7wUQa6Q5u6Naa5PUwKbNNdHxDrnWJh4PX_bxbbOYEWmE6O2z5IzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oNzQgRNJ99Glm2vY0ypdAPDaBmHdVykIlv5xb75Lfc2vXxK5wAUK0tfR0t8Bskdi2noZPX51elT_rUGY0AncTjI8vmQUii8qCOwu1PD1CztGNdo3WSR742yn71S9p-hkT3g4XlA7l9--gJWkmAUEuD4vLR9Xz6pjGQUSQ6XcKnCidAe8uHhLq47S853vDu-0CDAlo2_8sjNhtXi-_fl09fZi8PWDEU0nhwz2tK951Kq5rSSkVd3L0DyY7suAM3ognVozvs_uH6JbC4hgOgL3Ixdm5gyU_VPXol1itFnIvAzd-RAnFJUonJHbZjeaNExtGEHMhk64jhdxj6uabA7bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gWTPTxK6Tr5WB0c84xJsuvI7D9OsKjSaCRxvt-BE9uRe8Mx50QsqRfoItraL-E1Rl2V2j6ITRI_jZMVzO9Wl5zlbQ9yVRTJJ7_Js8pVoq6GuLWlngZUmsp96FYH4eY87odtdc4CtOZd3zamL8JU2Oi1kBxeD-Kh24h9Yftji3ssrYe1KL_KZetkP9QK0uJSNcHuogq60GqodgB4SO8owaou3PKmS4t_21ELyBBebLbbQcE4Wxwrw7Kju62nR2suuZODWH8L6_yhCe9j223rf8mox4sv_GIHr4XoUJGwu45esZTvjVdzH1teK7Rjh239ik8lOo7ZJydtZ943ciulg8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ck1QXoDf86QorncPA3deKOLMYO_XJY870C0llvE5Akzmg9FsTV1K6iMqK_lSzqo8fmHqpmB_mPmJtHMQGkOy15VW_C-4A5d_bfdPqvqt-YwaBMhnJ-3Monk5iSioBGFKHNa9sPBKJZv6FjAefGsPIhAAHRNqXwI-LWxFJp2C4Gw-hE4LJOR4LXGKwVu5lZx5siZuDm5i2E0IcJE58pbH_aS6MQPsic_s2BBo4r1Z2FtaiKxMmWoH8gJUCprjH-LZVqdzUgeiQlzj5heSjtiO6cZ85yTzuh-VguH2UgBOO62uFoJVpmdFDwZ73Tblb4XG77-23ZkJJkixUcbTzIPQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O7BhW2_jdaZvJfc3VRbB9HYRiQopd9wejI5MVqpbcZ7rjdbIwrLVDhpqxzAMx2kjUhOrHAvBvEOU6g9Vj64ghZc_VlnGbeDaMYMlEDglVI21NAzsRQMVS_HDMKNF_jMB_X4h2ADp3_Ixpgj8L2sqVXwq15DKtTEN_f8s_sgvA_Qe3kSUSnXEXO4dgbxxQil9vEOvZ_iPJnzBq197STiw0ZsrSJBpUiB3rPjND_2qA87UMNpKgOWrTPh5gJMGsqtAhgcVuWiBR2pN-_cAdJaxqElpy5HCR8P1RqY13yDMbcgQFmDTsdse8SSvKxlZc6QgCgYLMR2-vbbaidTOKcqjSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-wpVlBSxfKxYx2zefcHAfc9el1dh3vOGizaw2aX2v50trhDjsfo-m5_QSQltpGsh3rLozmVibY73DTc3YzV4-hg9ahTwRY-5NtDQLf6gpdub9fGA60pV4RBh-Re93eS_ekBf2Y6b-mGgmwXi1pOLVSp2HFkUs0qOj5zeGq9dgZC-zDluyo4FZq9pynY8w2KRSUw4pUyW6TvZiaCAL7PVPQXcQlCrNmkVifapEhoKE1kjxKX6ZYKHLL8J6oaaSpxWsGQbkY89-KSl9A-jj71YbuIOljAP8DWVuwo2IOEboYdUuDYjAxsfL3b36-Hn_sCEHDb8-Qss7YzCUmNYmS2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8QOodJdaiKqJWOtlevqe1zmoKLJmtp4cpOLKJ-Txv1uqibEbWlaPrF4z8rVfw9ApmQzzKwvaDFVoMOXcPF9u37Lot__eq9Kczsnrmd7AfcOdX7QP0rUS8amTwUyLp9v5TtIpm1mQaccYPXn-bFWykp_KMnCO_kbEuQaNc9lb2-ml9KmGNQI-rEYw5FlMq8Dt2HvocEqaI6iLqAy5cmy1LRI0qMVO8CD9LTiADE718zNEDR-B-G0IutfLk3EblIvcgbKiofbQGupwdy7L_K-yW0bxTkERIT-Bf0ZQLQ7cw26zulbxfgqXUABhD68hekPE5C_qKFYKw1Fj2wsAKNn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUBtC8h09vzyoCFZw4e3rPjBooyOcVNXtf8brcbBg6ieUURw5Mjy8a1lYupOpdtdBDQLy16mKuOmvH8uE1w9gKop2VZ3RK8uWoSVO6jW7hHxO7QcFvN9f_LttEcjJdEHkeM5gStkQSXJaNf4Xd1J0JE0_5Iz3EcsIravi7uOlgAQtlbB8gdOD0-re1hUkmX_K822LycfIDuQjsxkmJBIvIFPKcW-u2-m7iUZ_n-H7EwYWmwN1xXlfJfnaQjZtYsJelzGwJsCJQDVOqVcGUbKgLBlBsmORn1okFI0tieFGQYl63VQ-CGeI-Y1ZoBpRtyee8zOsYPoagD1Ar0pXeMjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uydwihswnWtr6rFlv_X9AMzwPp-AZZbHTsOHNqBRZVloYQCCSNDUJa2x9XO3m3bOaKbvH3rA-HXy4LN4jNNJ3z2JRMIVGaEMHAEXIDc0Eb1bWkn46jrH8gBsvLJzTMJ_A3L1UVGCPoSilmPJlCXMNvCET-waK_8-jNG3oS8wmYkh180i4g3u3AKJxAeODrXsVuLnd0_WYWnUXu5SezFz9z34C_mW188UQDcwVE4VAuNyJxqu7QNjwLDV_EAy81GuiJlVKwAoaFkcKmiyxGC_H6lN8ZOLFwPVtOkQi8gurDWt2mxia0qZBlJaCc9Nx0ULJim4Wv7DEuRBiwZKMHOqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tM5EniXhhYwuWzMgNok0cdlDglZIbH1qR7vg5PbSM9MElopv-QWkzUEf63PPqhNva4u5pbedDAMO-vvno5NcLLE_PKMqQWjiyG3ZKrR3Dp3hA6PWG8KeO6Q8zakeMsQHlokH9FTnrB1D2lnuvCHiUW3jQxsqPwBsgerjtXFFr5yfl5kmoUnK789aQk4bYU3xXM3qa2tS7JOEhWrBJTrM8k806TdiyKd02aGuyjqC7wo4AWdzIAcDe5fEl_SvSEKq0rkkMQ-9icg27QpNDI_2SQTfkPXW6JifMkY9KsAjESxFteJNs96gbFlq9xiaxb5Y1-bw_vz3PpwR8NlnRRlrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQBppvGhbyUtx1nBHWlzd9UOmN30pgj2bmC8FpS5RV2tV8JZjVNQ3CwtUUE0krmi4jfvuwv_zEaXW7_R5IT7HdkTx-xMAOoeuUXwOp4kzx5uYCp5O-6LGFGCqimKcRhnS6ku6Ru7EgU-yjZ4cpmF5Xb0zVVDWu4nxq__qv_I2bKJHJ2P4z30liZYhTyi6Mq3bIdOAPow5YM5kNxruItHhfF56YkOWwvI6Y9cbs6AFZOhUAUYj6WptfcH04ZcGZSi9o4RlBYJM_q4eZhcf0TkQrj_D6uRrtUR-ZPwK2krXhyXE5yMlOjI74r81shUBsnOnxhYOedJGoY5mMiuibaacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0cOsAwGYMH-FNTqib-mfCRm4lCb8Egbc-Xkp37f5mVCtQmL9ydFLOPWcu7V0i9k9ZGnS25H2Kwk_9Czk1FqRE9w9Qn_2OuXqoCz4GjHYMTGE7bkqDo75d1tAE1N40-m__8cid6dnk9WLlrz96MNdGfnkCDzMZuyolf2epDuEsoICkTEqssICOfCyL5oP1Gufmm4_JShmyUGaV75fLYZB24J3rDH56hM-bGGMGo7hcbHImB-WUNP9LfawlFN8OVnosSF30voqjC206m18ylct9V3R40LMZykAi7fcb9qfPzqDrihQtfmVGD08ZXWkbNi9pxgYpbqqc_6YqS8DY1tug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZSmrZdWrK2U_x_QvCyU2_9VcrYeYvR-KIqKpR_IjdzpgsZZhGz4dFh2PuIWpQXLnLku1j_o4Q4U6xot_n4G-q7T1VM2m2X1XvAsH53ZklBzn4lMfRs-AyCUw-gvg30E_e-YspPhpaujNU_JURhERpV21fdaA9okoxDwIiz3PVA3bQ1lQ_ZAKwW116ebkHgLrnks-Egk7JkokVVLzw7sizhpRaMmyh7jNlKOsAHL86VXAsIC9uemJBDN4LR3UIIvkdkFeO9aPnwWMmyltj6cRvt75_7EVKLKiZ2IL1df79u_DVlX24yXJIsN8qGQxM9_6hU6s4S8IsyODj7X8PPfbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGJuc7jfH-RnKBAmxzbCFfIyB7DgTFCTp6fRfn26U6U1TLM6wYYyFk7r_Xp2VE9OCCO5MRxYDAYpT4zfHfaI6jtplvRv1wXCrjUwLMs40MUf_uywaOcrC8t4ZIkwgaplhmNyje4vhQxRc3VsN3U-7JdkTNHqisY-AQLTekBuGthVsivekNJTr_wNFx5Rm0-vnazIcd-9TzZ2Bx10PdEIpemSdFwHh-iHQtA58V1-oKigx154M7h5DNVT6l1Sf4t5BMCFfdy4vIKrcxlJx8J1wb-YC-FiFHPsr4LiMTbHvWtg42VW3Hs09NmoHp-0aLuqyNElgs0NM-oyBY7BDlRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgNbnnBTLgHxj4Dpj51vQq1wpJd9lWgPmb2IMxnO0ioF2valRDBtQWrdD65_c9KJgmUxnLOyydTEDHobkJiLaz2XHShPs9h6ctJzsWAtI-XLr9xHUt6GoKXSID3M77wLlZASCfihMiBoy4-nmgCVFORLYxJ9NJ8WXENUncEA6eloEm_k4x1uiWnW7Gl3CIuxMejHqkQrB2-fDddWNSgMgjqxVLMT6akA1DLlvSgC29xLHQF9-Rr2cVHIKh4QRQWSsdSvkekl4RrfRshCzP8B4dPZfGuQ1hC5ez-GWvuslOl4CS3TBhLVIkd1qJLWCjbmgJyXgIu_WrQgXbRxdyp_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=gj9NqgF_MUpqtN20uiSoJGsW-RVjFaGzNQRuYxPqOZzd7WVKNchXrx6a9W_uO_E5YurOGwh-ki98kmsQ8vr6wZCjfjDt7dyaKCkC-pCoNezlJiRsXRdnsBhAX42GhqSlRB2BKUzELjDpm_8PiOlcacUP0ueF8s58bwPp9vznhXyVnubTfbNVwjR2YkEqNMXKMn_-R9_mcqmkTTcDtr2XEPkmwwXz48q6FAx2KY5Ae0Fc8H2IHmlbPheMGk5iSYvUO6svA3Ys_m5tzuv1X7Z-gUHLdmQaApb7WiluHOwv-cMkkvNmUrGGkMs57p6N-NBWqGK4aJL6vXl1-WHa_9xTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=gj9NqgF_MUpqtN20uiSoJGsW-RVjFaGzNQRuYxPqOZzd7WVKNchXrx6a9W_uO_E5YurOGwh-ki98kmsQ8vr6wZCjfjDt7dyaKCkC-pCoNezlJiRsXRdnsBhAX42GhqSlRB2BKUzELjDpm_8PiOlcacUP0ueF8s58bwPp9vznhXyVnubTfbNVwjR2YkEqNMXKMn_-R9_mcqmkTTcDtr2XEPkmwwXz48q6FAx2KY5Ae0Fc8H2IHmlbPheMGk5iSYvUO6svA3Ys_m5tzuv1X7Z-gUHLdmQaApb7WiluHOwv-cMkkvNmUrGGkMs57p6N-NBWqGK4aJL6vXl1-WHa_9xTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg6rC9ZotUzgBv8g2XrWEjKu7yEf8HN_YlE2dM_YXTA_YeGk7hL-IBfwI9tVPr5L3bw6KIfnCFgC-Go8YrXxTNcnrheUsd9TsLCi_9XhD3IS9tKjrmNpmO_XJKoesO7mh2YX43Lg28BBUbfcugi6F2LbdfzV69q8pFBqOoA_N2iuiTCf17Y2_UMgyt0_dkO9ojchIvCilCKJEAKRr41LoJjQssj_4LrcaZPnCciM_II_BPhDBcq-N_oIIVBswQNRlfuXk486M8HGzf6aoGpwZ6BSgP0aHBxmdpbLQ5lEfh8klk967FDsy_5YcU-9GijoSTVH9OzY2wgh9ynNgZTKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVMxXkwuXFuLw9NzOMZvpxRSLOMxZUOD_MXJMB_0FdrHgeiHMWA09XIswS-af_Z5YFzh8BZbUcfW6KrMPeAPRPtzboDKBKWC1pHqqXUDqRZ1xWT8Bi-XifBnITFnsEAwQwIx7R2WerrOQnT366bJl5IvrcEnGhVqWT3T_f8tXTNpLLbdNARGbN1vKMFikzxWiSBI7wPLzLIJSVBI7yCjF32hA2w9xantEGfgo1sTDPhFZKyZozgLsm6gum4IsLRkhyeSl8tFhHWp84FWC66MebNwtVjgEQ_IzKxD6PA2VYbci2EdvU16uZSBL4K5BdY15TAvAEMd_qT81epWNnDf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEOwJx1N3ynJz-vWKrLfzCQtmzU7XWmZYGwUCbOqEscigCyAk-RGkeZ_pcEI18mPD14tUGJ6Om9arBBEw5TB5JwzbUXqv9QwsRzE9xiXGfjPQH2zz3gNn1ctiGz7nK_QmcaOIjdrvk3pNF5zFmPn9hkuHZYFSe3GS0XBWn61sVnhGYSCEfE1JdljB5f1cFMqrpb_hoMahEqwplDpP9mOLq4s28Ftdxr2mjrcTwCLuxRNWvjMurRbzyDAK1dXotimWKmYxXAcNBw-9ZZuYsFSpW38aRc3BHtGDwuUVXVwnZdPImdSLQ_6ClbKqoc_2JWTnce4hbMFxAGJTvP51iwn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeEyHaphwPVtJjvA0IiWYM0irPtMCL6zLsIs0ltCkk5CwFGpms4BnqOmNRPt4u6R-8Ky6XWTAuohZ3XV-d173EChTy11hGOK3H_TbZ4V8Vf5rtWgwb_YvSFVGa4IcnN_dIf5G-i0Q6CCtN7EVvGMp-fSLxabJb4CV692IRBGcYEmTPLpnFWZO_5viINRiUyizrfCEy-38VzaaL1-kjoQoTaq7sMlVvmrHQQpt4VepcGODMKUEhAr9A5FNamHwn35j0OGOBSZ0vOpx81CnF18oWYWLIP8pOFhF6s2f8PpcPp_5d1pYC7Lly6Uq8uPioIFocizRsVK38Xn21t5VvANYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=Y_NzYNNaywYnFsxuDxIjBNxitSwCbQWYIVARVARCbtMpLZohHTXea7H173TZUNOSCqG2QSvgnCSz0p0cNw7fayOtiTEuNnSaIwPCPrEjjJTC-Ht36sq5D4KoGoTdPwd_MnGfl9awIeWxYfdjtz9J84CC53EijREBBqj7OFlIRzdSnO8H4I6BzvwzlPZiUCjv-TmvLzkXdrdLOllj2xwrQWNWc0Iwx2yUBsw16r2xpjQCbE3Btc3HvverT8Nl703EnVFFdwXABQbDCJmnYlnj-QO0P224XxbZ-r4xURi8FlRghzSwSyNX1DC6J8nKG0iyEMaMuq8U2BJeZQ3SnM2onQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=Y_NzYNNaywYnFsxuDxIjBNxitSwCbQWYIVARVARCbtMpLZohHTXea7H173TZUNOSCqG2QSvgnCSz0p0cNw7fayOtiTEuNnSaIwPCPrEjjJTC-Ht36sq5D4KoGoTdPwd_MnGfl9awIeWxYfdjtz9J84CC53EijREBBqj7OFlIRzdSnO8H4I6BzvwzlPZiUCjv-TmvLzkXdrdLOllj2xwrQWNWc0Iwx2yUBsw16r2xpjQCbE3Btc3HvverT8Nl703EnVFFdwXABQbDCJmnYlnj-QO0P224XxbZ-r4xURi8FlRghzSwSyNX1DC6J8nKG0iyEMaMuq8U2BJeZQ3SnM2onQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keQMPVQf32X1zRrFxAto_d0nE_L-oM5WUUT6jgrfLGlZiDqO3OUKMyTwFrUjN19Q_ERNbMsUgYbNFuZ8CFiQ8bEUU0oT3-6PHtIi1AbteEwYV2vfJHjaLSYGc_hK4XHNMRtm0_qP66qC04LBwh8m9LAB6_YtSGWupoGOpv7PRvr3iwt5f3bW4Mkns2aU7jVDb3Jg5F4PEW5QrloPpUCcxD7Ym0ixVXdcEOQMOWvDdgSVQS1B8pHdYVHbxKnAeHYj5a_gQcs8tLb4VNKGULYVmMx43N2ApLBFIpdcw4cR7TW3fhTUyvYfva-6_j4wOcqFlf15jsLbWVYnK-aBP6V-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyKunlhOsNf-5Dc1jpjMdzA5ZtjZz1kg2Rfp-mBrH9zgab_YYEVlgvOFITbY4AiZidbmU9QO08JU3mg_Jc4RztGd0pNIOzQ8uiqZYjD7019r4N8Zrtsb0sfRtpbniD8x95pgOaUBkasv-ujqxcASeE2FT7AgpoarK-HCFCmUqNEBTuzBfgrDv5zm1y4FcRJSCeRT0XEbPNaZEUylWFk9Sh2hnWAbZPoo1-un3A79pwSuw6UlXXjcJUAceB-Z_8C_GnJIzKCy_n0ZTE0aDnu3iwL7Isyi0enW9oxAwN72E2bKQL-LJu6-_2-I8pBEaDQTzJez4yrqDVHDvugvJQ6xlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=STw4_BilF4dYX_S8xx3QlXceMoXPTZwHS7R8847V9J8gMFE-xFUYGMOTD5FIoB3umVr7I-9sSXmZcJC13rL0QMRuX8vJeap-nyHELj_CAFwplsXvJVbZoQMSysiR3WIAHpXlpeNyMVUT9roHQIpQG8csssvDQPYaRYhu3m5Wp1cs5YwEoudtbDvbv6hQ6FDe1TntQxz64mZ7OL-lvDiQX7FLPhPE8r8jyhMfetolgtQq4lUOX-Ywjju7XtMNyIwjiHwpTLZmRyZCVt5FOqPWxHekfIXy4KlO5Zr66Z-0cmGXY92gtJs8qGmDE8GOGaUJjawyqSJA9OMpDlgHtyIxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=STw4_BilF4dYX_S8xx3QlXceMoXPTZwHS7R8847V9J8gMFE-xFUYGMOTD5FIoB3umVr7I-9sSXmZcJC13rL0QMRuX8vJeap-nyHELj_CAFwplsXvJVbZoQMSysiR3WIAHpXlpeNyMVUT9roHQIpQG8csssvDQPYaRYhu3m5Wp1cs5YwEoudtbDvbv6hQ6FDe1TntQxz64mZ7OL-lvDiQX7FLPhPE8r8jyhMfetolgtQq4lUOX-Ywjju7XtMNyIwjiHwpTLZmRyZCVt5FOqPWxHekfIXy4KlO5Zr66Z-0cmGXY92gtJs8qGmDE8GOGaUJjawyqSJA9OMpDlgHtyIxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQSnDk9ic7ofNT_J16bqa8oX5lIvh_cDYEyslroqtisEfjwY2oARo1Yj9xv1LCykZHGaEA2hMdgG89dI_6-yfjEr3tU76HAbLQ8hYAZR8KIdrixnXffkcM7nMtBfpCECBkufgw7XJMRdWPfbQMtnB0SgP228AyM_ud4Rvu4b1kBdQyS1qWNEUHqyGr42SDubyu2WU0c8OUsSkzX6YertWcI-pVO2FAtOiL5KxDLo-Z_L55ClXyy72MWSEAplugjrykKc6ZsnWpm51a1tOiyZD-3dD_bTzorHkaMNHrjtsoGtuO2FHTMjX-DjZY-kVNEen9bPshuiNM7TZzI6T0hkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7ptV4Egk5u517wudCA1mnrMENROvN8mdNiQGemEytYAQ4LOt4pUGb7ZXI2EAKlkuyUTtbxOpeCey0uP9HQ3QeGyONz9jJPytLqJ308XJmlyBXu5pHJbQZZwFW89er2fogF5vj0-_3i8TrArq6xPOkWJceq9bvtw_3WAZoPbs-Omi39mkSrPImIvMIUmHFrtDiDK3BJ0kazZDMaE1zNOV5WlxCWUQ7HNxeNRiP9ZQTbuE5qnHoXZdXH_f6b9N_8pQbiIqcWuAZEA0b4-GTFv0bGfNf7geUdhIvd-L2Cv0_C8CvMbuoKe6H40xK6hlr3IWxig1pn6B-kw1lf6724IuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR7KIwGLPEQKF2Oq0_ypEoAR8hhea2xOGVUInj1qq87Ko8Jqo4htvZ5GngKXkDoo4W-lhtGzLvYpxov4ScKZSZTwPB7z2J_6BqG1Fb_9OUprcVQN5XQzjOAgk72n4_ApT-08UxfeOlj7w71tXjpKfxQ5uEpd4RInFxYiE8F-Oub7kE6JAVr3T-Blfem4mc1WOmMLwrd5dg34SEgCJkGoHD27CXf0q0XIXVc-DTedi0TC0d4zblZxex__cDwE3ei3Kcck29EjCXvm5JcbYBJOPJ0pzQHa8pLlclShmKg-AryupJsgDtfCH5Di1Jxnat4IIQm6tO1Q7f8xAitzAUkXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzYZti0KUx7rp-Qc19sT4H4km304-XiuMAlA2nh9CTgRKlltPzDJUQl11fvbddPLRgD4eFCLI2ECdBZ7olqE_w66aVFGuAvksMJdEkFkYYFsy1BoUiSJ6aR4oxhQjZE8qHFMYEX9LkCpmFJe_HwMAP8wy7fggn_jb_U09Dv2eNvtIrXwXVzsnZZ5qvunePaoIWb2gTcGpdRPaa4-7AL58eJtImjLEP7BGFYAJTUEULL_n7O1XSJtChYvqiqepfDQvHbsGRLtY4SdA5YcfwcSMk5hfbS6j6ET_nyY3hkSQifUsRufYcSAyuOtsOfvcUXdmp3u7Tblvx0CokVJzh4jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiGn0PahqbRBexEaBt8Vetnn6VoymhOlhEJOfLSKG3kee34RlLAW9ZB6UmP1nlyM-hoRBRoBjPvE-bmVcFVKs7u5ZpIdsHQq_k75yQqBFMkOkTnRkgy7GWcYsbB7ANbwjblhFv93-wx6Ww5SKTn174S3upxW3YmDUuUi9QFUEZQ3Lq2Oly0MQ6GsCu9ebKQt-rPhVhJlfmBjhlbP9b5pHba3vIkV6zOTnxTg88UqiURD0S72rKunpf_LNvNrM12VXtcQHa_WWkOA4_jwnp8UM9MaUDeV2lgxbEtfuzAUFSOIdvWVIwDOSeGICHJM9W-_96wpMy8zpPKuNexSJXRpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=MHFjOY0ZB2xZZG7LvueWyjA1zfrB8ToPm8c5cHDq1ySRP47yGQ2xGQM3WA9SBu-JJxLYDuajBAbeCj499Cdbvs2Gdl5i_tgaIdYpdBsvkDT0k703iJYM9nxIOpBjThSlpbpJxeGFPugmq0R0-zUJDCm9zKB5yvt_T3G6e9kl7lIcL_6PgBmrINDDuwon46HgUprSDZjFRwboR6HCaVUJijUUcTiJq67rIa-R1jxjiOONKILR97ofRz2UCnlkO6wAEU7tNAYM1Oytf0Gqgm-dYhI6f2rQw0C926aceIXMe_xQJxv5-jAh4CtPN4tLa9cxlhI2Oou-1EXQaz1W6568dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=MHFjOY0ZB2xZZG7LvueWyjA1zfrB8ToPm8c5cHDq1ySRP47yGQ2xGQM3WA9SBu-JJxLYDuajBAbeCj499Cdbvs2Gdl5i_tgaIdYpdBsvkDT0k703iJYM9nxIOpBjThSlpbpJxeGFPugmq0R0-zUJDCm9zKB5yvt_T3G6e9kl7lIcL_6PgBmrINDDuwon46HgUprSDZjFRwboR6HCaVUJijUUcTiJq67rIa-R1jxjiOONKILR97ofRz2UCnlkO6wAEU7tNAYM1Oytf0Gqgm-dYhI6f2rQw0C926aceIXMe_xQJxv5-jAh4CtPN4tLa9cxlhI2Oou-1EXQaz1W6568dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=vxrYO3qTdvGTgrf9PwhyvcXISIT2qA-jj_x1xKO-_elxeMM9to7TQkbjnUKKqAkUk242_pYnlLH7eeIThA2rvS1Rd6qPAP1tEKYLiH_1T09HBMytOL35hjbysEfEWLzDjM3QBbfzUCtnlcVA4SRSg_V88XxeN52vguG7d5a_fZ0cpuQH0K1p1zkleRcONwTQjp7UCKgw4YMit2kFTCe_pgAcFOFJi96WuCssmSBSx89OeBoPnFStGxeBvdv2Wix8jJsWQHQ--aNjlhT9hE2ddjXTuLIexp0bCzN_aB9dsvx8YmFgx7BgRs45ioOFTPd6H0Zr0JfdgfYqt0I_b9RWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=vxrYO3qTdvGTgrf9PwhyvcXISIT2qA-jj_x1xKO-_elxeMM9to7TQkbjnUKKqAkUk242_pYnlLH7eeIThA2rvS1Rd6qPAP1tEKYLiH_1T09HBMytOL35hjbysEfEWLzDjM3QBbfzUCtnlcVA4SRSg_V88XxeN52vguG7d5a_fZ0cpuQH0K1p1zkleRcONwTQjp7UCKgw4YMit2kFTCe_pgAcFOFJi96WuCssmSBSx89OeBoPnFStGxeBvdv2Wix8jJsWQHQ--aNjlhT9hE2ddjXTuLIexp0bCzN_aB9dsvx8YmFgx7BgRs45ioOFTPd6H0Zr0JfdgfYqt0I_b9RWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nGknIybbkj_tjbvnsRpwn-SYK2wh2src8nVpUk4VFkSTx3C6fXALsCXQVA98u4y5Qc0JaOqsbhb19ENsyOCKgj1_SiOd7FmB_AZtesGci-bJxpMFP_1WWb1fyqPEGNrrwjTSF0JWyrz84noEpcW0BfeG0f6xoprkSGjs0h7PH9fdAroq-MFU05yYDHadVNJMWEKiTVXOMAdrhwVA7nEuXMjwGVeAR1uITfD3rOyZNWsWAzhGlpBc3C5AipBdkERu8DpWyonAeZ6c2VC06A8rzPO3rz4qyRxgELbjhjohpO3lJskSj7ylh6u8PBjQgHrZM8GwNWOGFw8Y1VOm2MXZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EWDK9s2-DyV4Qqm1A8du07V70rfWK57hFWTfpOBwfHT9NpMkp01LAHpMinx3iU68fQn8cSjmTZimIpcJIv9dF1EeYmIm6Dw364n_buBDpTMEWJlI69xwhBR0TXDAD-7YY2sp-cpGEMv88TmqIhqgrntuwpZLfQlhkQZ77auHcBY00ajPV36pWPg85eSLXsSuCEivjCCUrMBcTxzyn_Tpw1rDem1i1tqzI_BAspCpFwS-ZRuywegVeWiV7g6Vcu5zE3NF6HMbxp7z08CUhzSMQyq_Hl9kNCdnX2KAP5PKq1O9AIozJzb01dzci17tUnBFLJ_AvdOwqd16oHBvVUA-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZzdmjVTyJhrI4m5aReYorAlEh6UrBIDkzSq-BJWFceW5GjRnDMFZWS_KBuNgr9bdYLDOAiDKcb19ZuWAHufwDZzDOIDbS1l6hr_a0xMQFjnv_NI6uURGI-Vq6VLv4MMO41GpgGOxefb78cx168S8vXjI2qpIdFedUpzESirtN_F3CZMb0uIJf_Zsr-fYme6kdbyjre924dL3hNYaBxanhCf-vAmwd2ej32W39RVd6PrFMvik_Oy_n-MmNOGhOcgMNRNhcmf2ZVSQbvGCzdvBfEvpRL1_yMa2e0ALy-VkfEg8eeiT7q_ICMoMtONvFB-FOJ4AvLAcsdY-FxIlePJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c2XQRaXA1sDqWK3bqitXyYDLDXe6kI2xxVQKPu3RkrVeT8kVFuccZz7LboCNs1PWSXk3z94z_lgQJsO_A_0z4SA_INbnISE0bLCvWg5WyC2eXUGbm0oh_szMOWEOrbrvVaXqqMW-BTAj9zPmLuWqqKIveRpyDq3ZADGU5XPn12O4VdHzYHQYQr2a80QN6DHTOFp7RtsQdGcPfCLBGSeWoannQiV-livlLevVocl2SBWPKJZAD8H1BJHunKnv01HR-Sq0J00P8AFSR5q-Jxy_80OdS4gaLrCaR3vSBYqHY8Ey8NmBoLaB97Yd_Q6fhlx8xj0N73A5gUUau8Ne7acRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X2Wye1Gu2QNOouf_kzsxK0DZ_DdE6bDdTPa43LKxeVbP4p2zg5lgB1wKa9eHlWp05WOk-yLYZWl45HMlH1t2l1MmJQ-Co90Ioy_T3VxhZ9cQrPaXGWcxFe1vCz0jjbPBWh7RPCqLRnNqTU0PbolhL8kV0041kp3D4T3kYIRfj6FDDV72SbHvCzQRIhoFCK1kOaNpl0eisVbZ1nyI09zhLMGLZvkCOee4iCjsgJl-BoGOw4BmX8To2om3KqEHEIKLCR8k1njOP-cyKVm0rdsfVRRBN12Sf-ZV_DrLRYBs0UISTeMNoiGFxiQGHpKqVMfrLn9jilbRboeQ4Q6dVfoOzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=GyTwqoPF0ERe6mRzq-5vpTK_VcICpi6O_pi76ynUrHP-63gOA2UbEiqKGYZW5FcHIr-RmrbeLLJ8Jfi2i0iAbjK_PTvj5nlqpq2WOU43aaMiB5QVvU-xsqLIXgLCWVnBzWYHKo78nJx15obIBxnYuPuBhdXkgEUcIpRZyWjdGbEsBXLnaSR3pninQ-4Ld-5HuUV1yeT80wb4jW3Ra9ZsSzg_nxQz2jrK7VT1MIsYtKmS-r2O08zL9xvO9Jz-Ptt3mauIGPKRkYbUjBGUfVbJCGai5c7bJWtdtBSpJmfvda1zL_CSTgPD7-Ln8Sn2vRmZ-9XCykuVczBX2sGKx_feEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=GyTwqoPF0ERe6mRzq-5vpTK_VcICpi6O_pi76ynUrHP-63gOA2UbEiqKGYZW5FcHIr-RmrbeLLJ8Jfi2i0iAbjK_PTvj5nlqpq2WOU43aaMiB5QVvU-xsqLIXgLCWVnBzWYHKo78nJx15obIBxnYuPuBhdXkgEUcIpRZyWjdGbEsBXLnaSR3pninQ-4Ld-5HuUV1yeT80wb4jW3Ra9ZsSzg_nxQz2jrK7VT1MIsYtKmS-r2O08zL9xvO9Jz-Ptt3mauIGPKRkYbUjBGUfVbJCGai5c7bJWtdtBSpJmfvda1zL_CSTgPD7-Ln8Sn2vRmZ-9XCykuVczBX2sGKx_feEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWggwPDnU0eiInggliJ1x07oMq9AZ5ehtLfNKaugrgai2l9nf6e8Xv8l8BF9GaD97zETIU5ZWt7X_l6Vgi1I5lQwK-D9dlxBWjANPV0AJSYttK78NBWgD1_n6dijp6jUTb0UrS0Nzo81RVCmAWe1TiMrNC_2YCUBcV_zkJduSzHixfvq91mmYVoucjIxAZoy5MgIbdHLL6fMT_MALjic4hnxjEpL_Vs0vcqh5ywc7rW9JBFWywlEgY0PG_aBbiW8m8Ft3jF6SnwohwkHcP_y2vGCBztjr9UOsMqGBbzu-xp4ccStA4fiGk_h_zidfqdND1bQzTg3dbI8n6ReCvTWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZcOWsp5EMhDFVZn_U8o_KDpg1MFnORTPqC4tnOnMF0cuz7miKOvXwewvm5nOBBQX4J10L_q7QMrPmHGbeDgY3lkirmo4u03vWZCqLuTRv-MXtXvrcLCkSt_g2w-O-hPpF0caQuB6kjP8Sml1mNzfLZ3kqWdg3BMbxCp5vTv5JUChdagWeqVVRBBIuui6MoQ68z5cpC1Q6f0huRLYO0EFmUwmrfy20gwCHU8VXDYVEhx4vr2ob-AeBLDjg5gYBvJUTTMCehlD2nHV_V4u6JJk7ycnJPm4B0weT5K6ahNOQzY0mpC4QpQpHpsEJafIxnXFQAjNrYmK0GWCySCsgrSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt5mnDpeC93Ebt5RrEin0FtpRziZyhT22o865e3TxAdAXhRNZxtU8HeD-ecyF_wxQ-Xy590Kc4_PCljqJeXqbtRvUAkoVK89P4FI1BNvc5uIhnbq7ofwrd8d3YQtzQk4rYb55ESYcf4AztBn9VxcsqwvLjAcQECbf4hEPMowkfA2DbX6yXRfZflGU1WqYhzE2erzO5EeLCNkX7Wy-vNAsW2rhV1QrGW5iAamoIIBVAdOJoYTn9TRcrG6_CHT0ByS8BPmDlmNv2p7ZBkHGOfdDRqEObGpAvqNLFvb9gRPjUAuRXOqbAkYd_AsopZ_4co3M_jkkO0W64XeB9PB0uaTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJEsHWaafNW5j4ib_kFm7g1_kqQnmUeb-nVc6i-lRm-fhYQnE14-wQ0jJrtoyY1hnUQ4A2t3ogU59NAbx0QJlueL3k9PqIemAxYL7hthJIEDstPl1BxPPl0P-uj9I_MckWdjklGJLg-KjKSMvgNcjS4XpL7KpRVe4TowU2Ktaeif6M9ZYFWKZHda7onu_V3Es7chqLmpuj2eKLR4Ayyqf6wNafrdTIdNWapmrO3_8_9ULGZM0NRs69zKQsiMHXsKGs32pAEjAttTvgg2d6wVb6ezm44jciHXPZ8Y3NjRqKTriliO5KETSy6mHOGt_6nw3nqSKjC-COOrK_838ciSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=sJfzMs-jokmYHwbVw--a13Z3U9TO-doBT_qTl2jT8DCXoZ-LLOR-LJ3Wf7e4Ow_MoWRibKpTAg0M25f7Z696eK75CylyDkkeBCVCRWJEsc13TvEHjx850TTcH3VMiMdBmiR2ISjNedlwOmSQ1A-SL91Iuxsj4gO6LtTRbG-npQ1_Xtxu8tvzI_wfQlGWRQvPCNqbd_OCiC3H6cbvThUOLiYA2iOljNETyiPRUbfIigLEIGRH_2jYtCrca4QcfgMi3PMs34aPcafWp3C3Thi5xgJ6xf-goN18e1tdyh3FxOGHgOE2y0VcFnR8M3k5O1N-CAKsuga7JtLdT6Nlac45sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=sJfzMs-jokmYHwbVw--a13Z3U9TO-doBT_qTl2jT8DCXoZ-LLOR-LJ3Wf7e4Ow_MoWRibKpTAg0M25f7Z696eK75CylyDkkeBCVCRWJEsc13TvEHjx850TTcH3VMiMdBmiR2ISjNedlwOmSQ1A-SL91Iuxsj4gO6LtTRbG-npQ1_Xtxu8tvzI_wfQlGWRQvPCNqbd_OCiC3H6cbvThUOLiYA2iOljNETyiPRUbfIigLEIGRH_2jYtCrca4QcfgMi3PMs34aPcafWp3C3Thi5xgJ6xf-goN18e1tdyh3FxOGHgOE2y0VcFnR8M3k5O1N-CAKsuga7JtLdT6Nlac45sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApUAN1YLupB-8P35Mb4PRXM2hNZgxcNrPg26iVmzWpKNnKqnN4k-3fut_uFh7XDVi59NjNP9djxCb3IPE13EvwvyfO6mQtBvj4okgCCpp8EzGw4WfowyL3pJHviVC9bZoynnkRkouoYZUgrUOD5V-egl8IdcPYtPac-Lvlbsp32ZSotZhV5kCU1rzvl7-eMVP81hhbEBuzZOVxl8Q8GYVgySILigNyLrgG7yHee82hpW3tOSmz8XthZZk0K9cPMzD0kP2vTi1tG53GiuZBQrCzJysSkOte4T5E4CaUzkSrRv-oqS9q7WuVd58b6Al5G5oKh5bWx927Utnaf6i2V9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rV861O_DZG6589tFnXP0aEnpBO6_8A7epuM0VcKBGYzEgUaXjIfgUjIDxc_qF3nngKZa19iboGNimSonpT-QTdPK85onp0r1RR-5K2EvjoFYMZDb7_sLo7JCoPKFP1mqRcSS4VjJeKnAsPcA7M0c3GzAoNFWK835-H2Mzs_dblpP9PUvLkY_20z7yp8PzE94bZqFQzuGZPKtn9ClhqMKYpbkqL20PE6-8-f0T7aL7x-rzFKmJ5yuQV2B8y81KhD9kxbE1oMF2g27B6i19pQkryOzvpON5MGwC9VxppvF1MZyN7Fl0X0TaQPzDBmZZBy726mhvWQMXnwcrZqpJBbS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pe7vszIdsizGon-uLMVuuuPmL7eTHi6l5yDDuZmGNQ-Xcy6y6vDp5j1xzV9R9aG-KGYFOika7l1ZGrVRUkGyR10pMT7PmzZcbAYXY39MQnw6OV5534QVzzJO0vklkawEVhO3UACMiZDS0EQjmHzhFDhYP_F8pvVzGjkhIAofK5KwjBGWALscFdwk2Ym6Hlhc6_sX6zvtwuOSb-HgTELA-8UOlw99Gr_bLseKEfIKzVWmVaiZZ171vk-MqPUugN-kWI6TUXdsopx57i7zoDLHQTzEX6HaNCK6y3BpX7k4TlP7T-FZIy2zbQr4ZRINfoirZj6ZdT1GdfOBy6IMEF5U0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaRteDqTyQUf_6NCdwjLOxW2We85CM5lE3K3Ck6n3DR5iq7DXyWJuh2QFcWFYM0dMebsKg2VOUA8DIxnDi4yhrkugaavsl0eFn7qbJQBgg8R4VkmZRTLDb75aQl9CZIKvBMAepr7488lsFKyPIQ_0nLN6UejCV6N9PvzBbAmcDudO1dmMlQbSZllP7Witan8JIKsE7hAuSZdDhX3ti3wyyUALdfKwh990bMxs4f4XBSRLoSpHZPkVuTCLYrBdSlECa4ot_2A2h9tw2GJ1rcXy2aKs_EpRWFbLlZRGjHFt5SVk3vK7ln2dsYg6jtxP1lcf9CPQFyA_m2PXv7kvzPhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYjAoMRjtKRRp22GdQADxaHyG2nQlmYTob6LT46jTe3go48Vm0le_6zRECYPJGdjdTMbYGTCsZjGUKiOlG0fn2mby33MjTvKt3I38hbsfl0Xa4mizP2nTyAIG38209IzRKeI2MRatHMFC8gvEPC91RRRRbvheac8Xl9X202b-rjXRtturiCFtfBA_o3nCoe40c_sl9A4HeUS-pBmPV9VuF24OACXmTP_6XOhT6eCqgg2q5hb2fCCUMbUJrSNIPnHONkJJpdONmCuJuQDY5iD4d4r3mmJYXSPwSanotH8PfkHbnPKh3ySXRsaHaFO6sQNRmZS2CvspYE7ihOPHjQkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=Nm8bCHvehHr0wH8ZinwOxlImYHgKZlbnhXQ-5VClM-h_EPWhorU-EuZjyKhqNUPzU-aONYMp35tL_7S9d5YHBWpFissCRw9jL7B4dGF7vFapuu7vzaBZ1F9L_1eKw1fq1eG-NTV8oZvh1tc5pPSNo557Kotz6f5I48GPR85GsF1QUpG1M26_7SzcDBSY_0Vl96Mbcq9emjqN3XP0VY2MOXmvN7_fJNfKx07JjmludILdbdkRjfo-eOs-ahXEl29EDeBLmKPX2xV2cp-nDXsxfltNZGTumzNc_vuHWInikcpsTNBM9Y6Xc0Le6b4cE6P9-S-TEbAR4LWmOweXhud92w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=Nm8bCHvehHr0wH8ZinwOxlImYHgKZlbnhXQ-5VClM-h_EPWhorU-EuZjyKhqNUPzU-aONYMp35tL_7S9d5YHBWpFissCRw9jL7B4dGF7vFapuu7vzaBZ1F9L_1eKw1fq1eG-NTV8oZvh1tc5pPSNo557Kotz6f5I48GPR85GsF1QUpG1M26_7SzcDBSY_0Vl96Mbcq9emjqN3XP0VY2MOXmvN7_fJNfKx07JjmludILdbdkRjfo-eOs-ahXEl29EDeBLmKPX2xV2cp-nDXsxfltNZGTumzNc_vuHWInikcpsTNBM9Y6Xc0Le6b4cE6P9-S-TEbAR4LWmOweXhud92w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S19RWEdTuQEukshOwVBo3Ddc_iPrr6-BcT0U_XeS_f5AsuBW58kdEIoODrnMjQYt5C0-h8q-CuCfCxin4i9rE_KtE8zWfhXI96SGiY5DBOk77CnZ6Yxy0iaOC0z9ISWOTY1AJcWa0HwbUk72Bu0fwVYvKuIA0J0Hvwnav-JL4JqxS5TXp_a86yq3TUtrjBA5XlwIkhoPi7k8jKr00Mex1ZFSkRtSJ7SenXCpbexsNyB-dTNIENzWU-OX-P0PrtEXXOqPhdvrQnyKvsMnj8_wL3fftoafDL0dEJCviixqeZCj7z6Fw931yawp3WRSxVaWv5-_ReOJNCBlR8UZEpoYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laFh5idXY52YYY8Seuhc3n3YHM-M6KZSyRgxc2OKDVS5AqL0fFldX-RjpSPZsjcL64kfWotXD5SZ1gFWljK3u3t_INRIYjikDc6-r8fsaIPEj0xWAIU5o7YpoTWE0jlg9HjGHaTEDBvW-yPr1Dw68GAYrOo73ZFHXmOmqrzL3_3SNuHWwZJY1HKMS76D5FioGVddfpoL_Er08rUgn4OCveR5pJn4FCAi2KEP4LkH3de3H349R9TQUoDrHNIuSqxuUQ6J_8OE6LgEMAAyeRaGp7XwV3C3kDo5GEUTjyy5lB8fBpPU27A1NJ-m2LCpL4LTAiCnk9CtAD58klqwqOwHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=iqHzu4jWxsS3LCf5gAIRchzYaZV5jZT-FhxSBbDa8FVo_DmaPNmUtGJCJ0StFNVJPqLjnvrYtv3ru0FB4Po4h9ofQCFnx0LXyvigEjbSxGkiSHdNXBp3LLO-N7iUeyVEyBurSxBKSoOE6RhR_la2SEGvTNStd5JTpkWSC-hl1r-1YX_bVyzXE2wXjGmu0iVqWaICnLg1b2_SxchtHS9ikVsSVgEoA4HLgcHLap1q6M31P5Eapk5Fl87GKJYeh5b5MPhEACybUoABuda4U910XgExZXM7sRczCfMqIeq-664NG7aZHVBJVLw-LaIC_yaopwXCSwKkyh9wln2iqohTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=iqHzu4jWxsS3LCf5gAIRchzYaZV5jZT-FhxSBbDa8FVo_DmaPNmUtGJCJ0StFNVJPqLjnvrYtv3ru0FB4Po4h9ofQCFnx0LXyvigEjbSxGkiSHdNXBp3LLO-N7iUeyVEyBurSxBKSoOE6RhR_la2SEGvTNStd5JTpkWSC-hl1r-1YX_bVyzXE2wXjGmu0iVqWaICnLg1b2_SxchtHS9ikVsSVgEoA4HLgcHLap1q6M31P5Eapk5Fl87GKJYeh5b5MPhEACybUoABuda4U910XgExZXM7sRczCfMqIeq-664NG7aZHVBJVLw-LaIC_yaopwXCSwKkyh9wln2iqohTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDWOp8bN81ftAsmwE5aAcglfZdhkqEZa4AS4Ex9RRP1Iu2JZZHHXqSPB9aLmreGvcESReQkSfTZHt5H0lb_N1SVStPWJ2qLYx2Vle8RwPgf7clF6PW1iHgdkr2qW4nfHDbp_M-8yDBI-jQtaB0G6lwPOBNwPE6c73LHpQEjAon3-uxpjnEaakoNGx5qQRPger1bvPujd3sVPAQ9VOM7tc-DhSEuWr_DraeXx10y3kApJpRsFLuwYDxW5D2D6ZaSE4Ib3ofT3tpheBACMKmAMJIn5N7UnTCvseEploEkkvCwLfhtW3s125bQ1Gg_S2M2CVVDfNTrXVIbyEb5s9H0xhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/prt3_TF0b0s7avYe2rI-Z2V3SvvXWdNpXJqk-fQydYP-6MbCrTuGralxwKY7lRCADMLDDVHQINSONeNfPRDdazSTHOOQGGU3y0f1aOG02y1YcgHwmjhXHUV-ufJ76m1j-BMSC3IfnrOGA2ld0ZJ4wlqFKujP9rzjR7ONp-uS5t3gTGFP161FSI7l7ZOConUr0FfRR1ah3YUbFVEuQVBiErPe5RITqGJGu2DhxK-cLZDNobdE4k3V8MbSZB3if1bCrgcVCSiSebiTYgwvmhSE-fBB5BQLmc4JiKiczqUe_ooUy9PLweNsK4E9MjBRY3J71Py7q19q1LVuH0KOhoZiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LzgVNdsyonQwbmhKHQCGkHYEQv3lOSC86rS1_ymr1x-g4fhdT5pCpZkeewZh15DDPK7Q9Z5UetCH4zK8l9gFHf5X-BlXLuEdZR-PCuFhz9FH0pUkDa5v6OGAlEfulweJHIiJ9LRx3UpOAJk3yRxYifdP17NITIK5rI8kuuWNRMoOlJUiU8lO5alZcWzOnzrrMDOlaIH7rhaUEf-3hQS5eHGTX5HkdobbuVcNF8Ds8aV3-hpJEvUpIF1OMsPYSQjyLOBVA6A-KTMJqn7cqpvMhCK2P5BT1JyU_L_fxKyHs9waWTTbnJ0REU0a11i-PNGbCJR11B-LXysF9a679G1Fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4olAY7s1fuXmqLOEr1lHVqczmakxAtfgOyQjBA_GPofMA_S0HkK6APCs2QeVrfCASBblVvJWgRjL4CgYmwyjIFW_L5hf_BRC5E4whKR6q-WjEXzIbHk_2xBnL4AWFBHqG2mhww9NJEUUUvtSxxsPraIT_WV0KJqByojMKQnMI-M5SMzPf-5L5b0j9GJft7vjSyuzui2m7fZSp2rjewgM-qQsBQ6jcxoc-cvRuNDMERo8MLzRyqI_uyIF7sKQa_AS129_lAD6sqAw0bpwkS-T3adTp5-YQzYggsQaOHSD3N5koLPjLdfR5a5ABNeFNpuvwCPLAVPcmHo7EgC0F-PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZQughQxDKD-MvjyiiB2y9by8dNfwGQnVl_yW1Y3C6hz8Hm3DtC77U222AOIZfwgOTru8O3pvdnAwsCh6rQA4qgEzj8Ln4UxS3JqRzoBZfNAsr1DnOhE5bSyGzMG21OMvvYD7dJ-llmt5iVdNo5ou_VgiWZLmuFYK98jkF8QhaJuXPzDvXVjdZRevCrXZJckRPy_-MZRvkhzZ7ir3Nt32ytUX4mqom6vtIK_Vk6g2isLyKp-bCgrEQ4iHYMnv5YxXC4-cIo0vImrMwSwQlUBMRTqw2132N5VywVgN0Eeqv-gHDzKgz_ra-fzLCM51VeMiUYWfmjFEQjh3awlfSyuoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9M_xIgO6c67chwr_FjEvRpb9kiaO0or8_B0Ai3qdXrca36jCF7c3kGew4AhPjpc1zng5NE6riwACLsBpMVA0i68id74UvUtOehNVxB7Y-CurvGd1Y0M3O-4NKj1k1BKr0IGePEOvAXgo7vASlMTwCmduC6Ow2P8ePHRhNdj7GzZgPnQsxFpaPq0QbT-8g3ZaQRRqM9biR6J2exJWTkSZdTBw5XvvwC0ewynZvJgPfeKNYIgY2Lh4mhqOAeb7HTJ0ybSyOMPWR2Quq6QB3iRqhml6COiEcVDAkader8VOeRz12Tnr6iVdESt9qHUBzJ8ej94xgK9oNy2ByUpOa8vww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kof4r-i6_ToJilk8Ik5OTId38-1pZDtTIGpcMz_iod7dyuajqL9iwCAp7JNvY27cUiEr18ai23YP5RH7Qq-3Hh3w5XDbHth_YlE4Z8oN102yphsB7u-exOGAx3_kuL88INY7KRCzCPloIvdMrilGydckcoYhXVvGDL3iriqZAUNVXDbkaxfAt0X6a5DAytfA0CXKcIRegDn8YiBnrmyy9iNu5lnBDLZs-dETTtMJIF06UXDjFAM0FedoJbol_6Ha2i0gz-UKwdiMYA8cvgWkaEDetEu_J0Fg1Ig9zMsLaZHc7FqG3vHRRz_NS0YNOO4cyDnXXEiNMfQUU-PYS4nlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=g_KSlNa-sn7aa0J7lvbMgxTm06E2cl22Jm1YNVULy_7K2XXYTDrWFW-jDT0xoOznJkHltVNQWHy0Kv-KUaeETsLGViqW3-_zTHBKAKm_PfWEweZd-GhWoXWNw2Vc2jF8W7b75_g3ShmQBdlmbj92gx2u_PCcQtVFmm2D9GtpPCmSx32jQRgKfAcj02AB95zghG67q_y6u3zOYX9ZNYcOwTPF3dHAJ9oauJfyXOV05CiaqP8Vht1N8XUPtHE3oO50vkyTw3ALBvM-AWR1-4Ufydhs7OfA2cra4BShNqU25E5JmwPe2E2ylREDYY_T_gykhpv2X9VhuosaG8NYHG3kK66Q3gLNkUI8O9GBkvlVK-kSENWKfayNz7zpnpA9iy7UnYZ5XytAJk8E0DBoGLIi8GBEOz8Ocft3I5L3ESkRf79sqsO-g0GqeT8faukCQW5BooCDzTUPoH5t5UzouXf4_I-161QK1JUNdOWc3sSn1IHk3ahsg4dSp6GhUBxJZrkVBt1KVOUQQ29_jRvOzES0CmfXaoXGTFyjhNUsYkXPD-L7sHpveKzR9DHdrXcrnrzPhCw6HuyHVm6nERe79Nd3VOZakfJFcAsBUZt5Vgd-e2ilW9JIy02Sdx6qrSS1Iys3OpMVm30ojJiZ9mtDF9U3WT7xxNbk3sE_71btEVuDOpI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=g_KSlNa-sn7aa0J7lvbMgxTm06E2cl22Jm1YNVULy_7K2XXYTDrWFW-jDT0xoOznJkHltVNQWHy0Kv-KUaeETsLGViqW3-_zTHBKAKm_PfWEweZd-GhWoXWNw2Vc2jF8W7b75_g3ShmQBdlmbj92gx2u_PCcQtVFmm2D9GtpPCmSx32jQRgKfAcj02AB95zghG67q_y6u3zOYX9ZNYcOwTPF3dHAJ9oauJfyXOV05CiaqP8Vht1N8XUPtHE3oO50vkyTw3ALBvM-AWR1-4Ufydhs7OfA2cra4BShNqU25E5JmwPe2E2ylREDYY_T_gykhpv2X9VhuosaG8NYHG3kK66Q3gLNkUI8O9GBkvlVK-kSENWKfayNz7zpnpA9iy7UnYZ5XytAJk8E0DBoGLIi8GBEOz8Ocft3I5L3ESkRf79sqsO-g0GqeT8faukCQW5BooCDzTUPoH5t5UzouXf4_I-161QK1JUNdOWc3sSn1IHk3ahsg4dSp6GhUBxJZrkVBt1KVOUQQ29_jRvOzES0CmfXaoXGTFyjhNUsYkXPD-L7sHpveKzR9DHdrXcrnrzPhCw6HuyHVm6nERe79Nd3VOZakfJFcAsBUZt5Vgd-e2ilW9JIy02Sdx6qrSS1Iys3OpMVm30ojJiZ9mtDF9U3WT7xxNbk3sE_71btEVuDOpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rRKOkP8-R4Yq3k7KnJYF7jLgfYh2hvBrl72skv41_BJtx5ho7reAvaZOC-2fEuR4sX63PEAHW2CL-X_Hcz09EEVGPNO1eqHHsS1JAaVO8PLD32SmVQUq1Ha21sgP63IH3fMU5qZiTiUt09iOlDM-r-A5zbTITM0gtl_G62FXZ_k2d9MwMv3VzThjEUtYi2vyBtANW5oAxJLyFEkWPhB64zDJsoexV9efvKPUmNyV93mmodnM9rez25z6XzrSgyJUnX7FI-7D7ZM5UBJhZ5lMF-mELtTVdICNedof6Mtt2MQL7RN6FaJ3mgUGxg2imhccsh0-gaHwTSu824-ztptNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qj-3F0Bd8cL998vQDXe2zurALxW29MHhXw7qCJEA2R5SrvoNEJagubZ1-wR9lOhCQFPSKZJeKGOCxQY7IvM-Qz0bJdvFUujEHLHKnXk9uh2ZpF24ym5uKh3C8e5u3-9Q5NRjBbQw1fPX7qiqsctpEUlV7JVrfQwyasYeFUGDGX3Wid26fK_BYumiKNz3scButRhQNVI6Z1toEsr-XvgIQCTn1mjIHh4MuMnAcam1kg5SI45K20B1Q_DLDGWQH_H7LIorXpiGq6UZHlX4ZbsAYJIqka1LhvPMi-S_SiR43twD4GUyQK9CThlYJZg1AlD6QSVdU-yYid30BN5npoCKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JJ9tUnly9AkKNrSQN-e_mgDfObzIvpPa0A1-qNa9T5j0ztPA86rrD_iobuMXWOV2bjj8VDIafjfzQRTyMbEc6Tx4WPnNChlbXL3IlwDOenaIPVrsNWYYydbXMbu86kQU4QUGRtY3zeghzZjvlIBAsh9ObUNfauqYWwGXaSgoZQy64hvHUz0L-1_saWFvNPfsNKS8pbzaRJNSOTjdGs7RxlUVFWTOz6827c0OVQ0CgL2YdfOFXSbfCP3YmWsZ0RSpMJnh-EktQgBnXx717hHLidympdhszS5TV8_1jdqnQ5UsTn5MPCx56_Lu1uc2ejEwMNN3mMkxzk1VR89HDIeulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/boOD6CUjoc4g8lTEaoAGXlaa4-eSny6XcymNDkN2ZDy5n1NeIZ79jk_4TgWLIy1ZMcnfU0DNDLmHOHqLBOw-mTEQi2fAX4lVy3cNc-0fVp9Bg3QvejSTsJGpeNYxq1nIgEfGkDWWXkO2xsKtj4BXpOszWqYynBRQRGWv9vX_SByENBrP40ksiSsbyjk3MGaASdsgJhGjIuM2gtlv_sXDqM-uDFeBCL_YXlpnHOFemT_6XIJbZXEy_qoMSaxbwJmrK-xxeA8pLjO1rV690ip2M6d7WhxQmCU4RBqBfaVw4ePq6od0-ti2JWuOtsw2hMMHEnDBeZr7lEIOjfF5w8W3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bsuckNUVUQRIbjWbNmtIC87o4XDpmVCjnO9FnAWxsrFun6PkAhyY_vVegQOLZdKLq6nMzGNny_4yqPG_S8Lq76PwMATNxP3qduo1LtKj9ekPGaLjYkX3aDlB8V10Oj2HkufDOamA8icxduYSj_2qRt6fhCPJklK65g26sCVQtzapdn6jc1_0KBKw3YopnGrrVzc867PduJKMha8KCvpsVn7JXlkMWpZvyP5pyKFtajFC4TOQvx3xqJJUr0JuYGtvS_9u3Av2S1IbJkwcDcLrzsdrRPl2ESyKwvqiLtwxyRicAn7xvmhSsd843mDsdQMB3BWc-YfACag5fe8JdyQuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XSZc1vQeGDt8HfX3oNFtcSyVnd__jkKgjmoo5ZyeRwt0XRF8zK0nos0DRdRTogN2lveNDJbcas0kNVTgxSPkbxCt2Ilr67LMe5KLnL7i6pWjn23NwowAtwPFxu1QAiBTqgcHv3pHL0p5enCtgsV1Le9BtUtdAUr0xCIIP7FasU_fj-j-m_hidXprzvKQTTkLtd1F4hw7tPy8_LJqZjVK3w6Os5d-xcgobNv5eKVVUQtAAwHN_E5R55XAHh5glUcfCtY3pG4socyo-hAk6DOOCj29PSaY07ATBZ-QAyrSPJXWUkjQ9yqurvVkEAJX0S6zpyRxl8M4mbHKM7TndFpUpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkxjvBUmqw0NlqTW7P8uXAU6CS9laTvBB4LvyVIHchL17PhAw7XvS3pLcA8rpcCKwg7B0rm6q4_iIbcsM25QaBlW6-wCrM_96A_-S0yXo8gyPOJ0cQidqQTleLm87XdvmRNLknh8TEb21uOwWefK8jqWDbYPx3A5x2vYw9RMpql-i4YitemgEijEiE3HxUpgHgAW8Yg8GnbtJIhiqfZGYhkvC5QBUP8IZ53OWjAlBu47x070H7DNPEU8qsRmQmWZpxR70sfgwYRFW-j2jCaYKvFX6jKln96Hr-wsPzjTD9XgH_ouzueYC4D6vQLgwexqvCW0Nhmooe1oU5HnfMcR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5o_708zhh7KvD4fZa474ssPX5JUUHtOY3D1m92FsVMCBqcDSUMDTWT5Y7ivAJ_TmqmIyI3TzO7r_6xmJj33iBUL_YEmy5TbJdN00EvbtvWtwH96jw1_uRPTKJ6Tl9X33sDK_Sz8PCLXT_32QRtQti5mkms0l031OsqodAkjgDVPmqTl6tXrHLa5tWfIEyc1Ljlzo73HbhWSJUQ3lWCp1ZHzhJZpdBbDqzx08O3rJoSVvbgNYOgAJgj1dSMmAk5g5lTApDd2oxpdNO3v5ZZULOYNeqCE45FE4glK8Xem17YOMayluIabqOfVmssNUbxXAZ76PiKTc20C655ViUQGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=KnNyu7_zbDovlwIpIa7Is2Jt3JTgTPlchYCLwrGIhwZzQpHYKL2MlrPUdg_tsZqPnnM-t3exhKsscjUlfLqhAAZZmTf6AYumzrkHCTgLSKEsNZn2ndNF6Nc3bVVyB6UeGEGWmImhriHp0M3mJeeSw5sHv_bZyi39Sj6o6M1a3u26b0uz4jYBdPZCw5jyzLJqh3BQRw7tuWcYlVuWGtY_OqMywFj2dm3bwMbI4u6CcI0vzaHLGdGHs4DG1rNh8cWd5zwHshBo6QoFRPty851mQJaA7_OkUM2EYOOWehT1_lHT75JCuYhrpx_a18AwH6IIOC3RCJuja3834OxjHcxUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=KnNyu7_zbDovlwIpIa7Is2Jt3JTgTPlchYCLwrGIhwZzQpHYKL2MlrPUdg_tsZqPnnM-t3exhKsscjUlfLqhAAZZmTf6AYumzrkHCTgLSKEsNZn2ndNF6Nc3bVVyB6UeGEGWmImhriHp0M3mJeeSw5sHv_bZyi39Sj6o6M1a3u26b0uz4jYBdPZCw5jyzLJqh3BQRw7tuWcYlVuWGtY_OqMywFj2dm3bwMbI4u6CcI0vzaHLGdGHs4DG1rNh8cWd5zwHshBo6QoFRPty851mQJaA7_OkUM2EYOOWehT1_lHT75JCuYhrpx_a18AwH6IIOC3RCJuja3834OxjHcxUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JyiG1N-8J6NrSUoJBaBFGty4LgcoADrcz6yYnS6N0gy_6s-G0ckCPWIYUoqEB_p5Hpbf6_qByZck5f6sIOovIltCkEZQlbFILUUrArfnUyBg8H5dIzSl4iZOAYSOXT0a-RmFacmxoMU7oen1P48jZMuIUd6CKV-BAb9RizROVijfPQX-olqA72oi4ZxGfWimkhU4NTVzhUmGPfiRKejpKyEXlYk2ohpw5CQb_9HLK7DoMp4iOhhRY-JKboxpn_nBDQuaCLj9QYt3d4nughvU3NAWEakO90978-Ily91yBJih_HKV8A_62vusCvWzENlR6EKzNHr9EDarZyR1qz6yyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=f-z6PakR4eZJBGISHB-_1diPRmD22K1Ol8WhFkk43RBWW3vAXXmelDi6B5JOOnUkA0JQejE9xzrEEPM5Oi8wQK-2_1Z-IgqyrWTWdmyX0xvRfHXVHKewRBradWNYqHwNWULRP5BN5W25vC2H9ntCYAWoT1OwJfkEaOsAn5a14_PpgdvMLGyG_F6Es59uCVEcTFq3-1hY3DLf9Zs-u-BX4diZV3p5NmDIQBLkaTG41QLToBMI-Apcs7-WRawDebOqtBha7fTVL-lko0dStGutq9PRWoTVdE6hGdeTy1kBv5YgmCDhnUJWNKofz9IDTR-Vtpo_dftuGcO-GB27xXuKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=f-z6PakR4eZJBGISHB-_1diPRmD22K1Ol8WhFkk43RBWW3vAXXmelDi6B5JOOnUkA0JQejE9xzrEEPM5Oi8wQK-2_1Z-IgqyrWTWdmyX0xvRfHXVHKewRBradWNYqHwNWULRP5BN5W25vC2H9ntCYAWoT1OwJfkEaOsAn5a14_PpgdvMLGyG_F6Es59uCVEcTFq3-1hY3DLf9Zs-u-BX4diZV3p5NmDIQBLkaTG41QLToBMI-Apcs7-WRawDebOqtBha7fTVL-lko0dStGutq9PRWoTVdE6hGdeTy1kBv5YgmCDhnUJWNKofz9IDTR-Vtpo_dftuGcO-GB27xXuKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L2SaEF2uXBbhP3D2GXcyrBPk-PLZUqyj2OwYJGqtcn9d3qlDRgUUQqIfFg4zsnaVWFn9dnmzT25UiOdTL6bKQZZBFWUfLzGvv0MS4dp2xhcNsecWi7oc1Evbh2RuP9j0br70ObdJ8Ot4GKSkNrvu6kQA4iwneGs7G-6I5Hv97A7ShZwDTwu6HvRJoyrL2BOlN9oZyH4UYasXSHS5X1_5pYcBljkG1MCvvBi7-y--LsLvpbfGt_mYz2wzD9uoqSxsv4E-G7pA2saVuCAl6BOmZc0Kj44ji4DWpTpRQf2C5K5sEP-amM4W695R8_3SwGcytk-DivVfqayW7GAeZEG3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPFUdaxquJ6p3-TYjOAGHdTPYVErWTdpfHHhOgofJukLnIsq_6KtlwhJ1c6nSJssJhbtwU-eurjhGFGt7EanAkaZzwXXBRNVCfx0Mk6IFlsEvIz-4eK0Qjsj2MijE0qekS3BxTf8KmEm1PKIlmSTFXZ-EWio3xDBJApIRtfQbD6XYhu-j_rXx-2bwzU7bKfMuaiLRN-HFpeq69ADbqS7j_ube2RzfAVs6GobMHgpKnTt7dKnRwpOFSIpdItBrnluwZySBkm1IaEJb38NC8NLTGCKLCtBv21NjES9lMEr4tUE3gvdzM3fL4-PNq7QHa_4lETyOVON0Za2bMk_urMhJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGFINoNzR5vD-TFl3Kbwx39jVoRB9BAdWcFh6Rwx4ZMhCjQK5JdelZS_YrAwFtI6TchgaYPVzDaspVwhJf42_vM3zwutJZKZjLz0IsyUEgQNhq7sFHbrv5nL2_AKHbm9RBqzYVnhZRcWqgQJ2FM_UTJZ9eoP08XceNzkaOzzo3opS__iSKbfx3G3URd8IT1sZMsNX8adgB1AXdrUPv65N3pwq8vWmsqlJlzTIQIlH82Hw6BpHVIOAR7ztb9fSEhIkxUJaIM0bnxbj0U5qCrHy-42ENrtdcrVa4IZXrugtmcB3UApAQffHbpDsN9uXz8itrlZXYhAFC5sJfVe8tVvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lyc-aUbWMl_a9_g-z9mvpVeKjxEtbllVGVyFF-uESP2ZvMj9HEdebgTvBiIabi6t8gg4KBri1tSg9m5v-NhqFbG7w-z0KV_tncXUkQ1zYLfdTGJ7scqmnY5CTRjWFcrRb5v0hy4xQrvcfYhGUBoEH2Fw88CffaoeSPPXkzbxzuengayfNOE_8ZoEPEMIdwwwvX-n7AT68gxSytpi3DItS22W8pKsnOsoWQiDgEoGSTgKIfSt4V1KgjumaD9j6mhY4Cvw5W1OqCdqLfBNrNXL3hmexxPRiSSPMN0HS5GoQO_ep1Q73cfZCuKnB3RyNztw7uHGAyWHOv54kxNCpRJcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDcmq6_ZL7OBfS2UukLTc3AYUcqiW9QxVL-ofEZEEJkv3KeMh-WUUB4f2uEsrNM9xiaDCMEFBX0NroIZFfSjEYrukKQgvLmVbdewbjiXXtgQ8nctW9pw3t5DmxaBwcFkqT7LZBwbuU2ydd3zPEr3SZWP6BENrTmA4UGFWuqC34LkhgsJUNDh-nklGF9_sd31By4d_m0vO2gQwUQ69XjYJSv9cO16LPsdfxU6E8KdTPRZ4R0NeJ1czhyfK9gkMy0XdUrkhgxvOdxb_gOXv-rcUmixDgKl9QhwwkuS26lZ1nEHvkGHFc-UfAhlXkyUF7bsysG6fPbUuB0-C6_6m6j8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ll26ipeOllFviWL0sU0lD453xCeGdZAPBpB3u1n2ZTncVvQ8-yxH7Xn0X4JiPtgTi1-WNJx4m-ZiL2NvwpyZvfa-KIxPPoSy_jLqiaXt6gDI7pTVfeiKjJAWCYudyF54XRJ7OdZ3yW_kfh5iSXodofvQLSEWOi68qi5zoLj06ycCitFYK5WuJD4zIZNHpBZ9HIMAdvrTedMsqHw9qSoijlyXgEJmX7yXlRKNjgklT3k_eFjrk-3TtD5_XqwB9oxBYXve5MKpo6VDSaK1LmKO22fjI6RpEbXUQnjn_PYy61fPZA5tsvIprT8zk3evoQKrteR0ICPxzzFXbdWFbiCD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cpXUBZdHMrqT1PdsYJV0_ZN4pyJxrA7dLJ00N0Q6OsKdkyM0xh_GtRstEgPs-AoeBbo_RY4C5f9JNyDs7LdfZHeCjC8Q8Zustf-PgJuFIAcwBNNlXBSfurbJIEv3glv_gyR6j8pFjeHi_RLBEH4y21HZo8CDi27MxmHFrRgFSico7gWSfHdRAMaOpo8DASwoK0uYKmMFLHWmPnGiRC6SxGKOf4Gn5_yXw2XzoE3jSoG3YZgp6SbVMhlCcqfABJeKUS757yNg9ptbRmbCNgamzyQl7kHV9qq_MZd-HK_W1zVut7gI9g4XkKbI8bZQCEpMsicvkONd7jkQSzaUVxyTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KlJ1Si1qOFZqqaCtnztMjq1Tzv5TNw7FSVImMSCa_G9mx-_T7jeVD1gh-4u1qNWYRjYzaafV5CkTa3cGIeVyIgtGITfUxp5kHUrrDNAcm97p98YNKd2uD-HQZpG_9pJdXgSOzPkgaL4zvX3Dbf_CQW3pWg1OAfaBqvCQDsM9pLSbM-Uc8Qd1BfUM3RsFKLYJUdU-M5d49yM_ME9gy2rnN44OviTgM8Huupo57F0DxxjhBpRGZ0No4TzwQfVelFpJ2Zj7Kh-RAKy4XkCWzttdChKPLlW_34_gO0RtuwozkuQqHEH-zvLmO8LIlc3Asj3JSAME8hIKK4ccQDY8OYoOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HfwD2l7VA8XEegHa9yt_nAH1p-N62wKP84Tz4xunPDz9xJDCZBIVRC2CyHP9MdtXB_ga81kiO_nAA9uZ6vS6nldUZdaCJF5bqOrsde0uiLYBFLkP0j01OIR3cy86igqjr8X29dAdRgeYbX6zV7daswFjm_v3iZiUZo1xye92-vAfpfrI3aXvmxjoDGbE8bsuPLKcH2UkLVO7YlKW5AHfVQ48HH3eqQjXlGt0QleBUlZ18elmhBWBQbznpiCf25BrMosHOaUPKXqKh9PkbV3N7jgMJqkDx4hxPLul9Zj8IeO0ZjpGCvv5_toy4HUB4wd2J0faWIN0p4LJjjITJpLhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g9L9DM8dZadNx3uh0mMb9V4D0tvtmiG7DASFa-nr56ni9BGaBjTHXtWSaDE_kut3I-ZprzyoZpLDITmKpgNph9VOlu1SEA8TH-fSbxz5H4VVtTtF47TOKIM2H7KENfW2Fth1KsN7Ko2wmEyFkcplT0M7gKy2MeQmUWzSFuPMlHo6TDw9XZX9RvnpVB7S5DZUOAYA0VPcFf9-UpD_WG8j-eUlID8yeAc5pMWdTOd8crQJ_ScEpwhIfkmIen7yHdIu24L3UJ2XlGvEX8XtgW38wSIElQ7bmlrhwFJosKguwkzTdOC-0FDcu6QZnKHi2z3_xSUbRUuxyTiB8KYplUvYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bpg1APEIMYJOBegEARt2wIzKYcAB3cGz1KuZzWsZJYzp3VfCt5Rox446Nt-HnLCIFufNsS20-prEbnxgsSIihahNDAgascmBEh23pYhntpHVZbte-_P2P40u279CUuFMt6S2KS4UbpyyNpp8lZ7QqjEomhE8kNn0566cmDIWcx8q5HwzN3UXtNOnEm5LCSs4TtZKtLsBFru3V8HZE3ogG3aeCNiMyUqs8ZRZxOdBcAIaU8Gafb90EiBsJn2XHfFPk4-VLuT4jYU0IjiI8UAO4xV1bJdb0jBTjODMNFpscNfnkMzHDWXTnGBx4Fmz_QMO01KCkfmwsSfgbqxiiuikDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE49LqUXKHk9HonSdAT_MkVGCTj145tQANTMgSZFhawMQ8s1BMmveCBO_phJT_MCVUk27wYGwB-DH0G-kygFn5I32rbtPfnLNmBpxgZ7ia-4E4A_AP3k4bQn45XP2DuXmk_jOAFmXfczISeChxR39ow3KqvS0v5nFeNSsNUQyV2OvD0A7xD5sD2tjcPLSjlW1k-RcWApJlghOhsL8aDiQndcwAEro-f2uJ7YMRJiDEFx8AeFwWm1_T9pgCWzU6IVNUrlzEp9WYFlV8k0FmCg2cpDZ3IOywjIIIMPV2BDeO_jI8Tftp-5YDxeyp3Gd_XqST2nrzDNQHCyRcNtsT1UzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8s3gIoOt4r9fFHB7LNHogLSbT2h2FfcXqNZsb9x4qnAu2TnohQi2oTFiOSgb6afb4pUBRbKJhLjznNeCUasjzTQMkfTrMrVYdgZoHXSfZYMDbB14uyJHq1Ch68j-c5DBL4yLnrm3UGdFxuPRTQ0p_-uyEO__zuhB6zrEhqxUHkTg_2zLbMiI43uIBIcIE0MjMLK7qonyRIErtUtYugzoMvLxn7mjDPuoHV7SQXNVia2UzUOBbLdTwreE6Roh7lAfCrp6cHEwAGVZhOdfDVaRlhGkFW5GIAaA4228XzQtzN69P4ckB6PGKBOo5KsMhXsQMB5QuEqMwmR0SsAx_hIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
