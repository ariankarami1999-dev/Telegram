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
<img src="https://cdn4.telesco.pe/file/Kf6X10OmpU7k1z3AVH3pgA-EZOwDlkelak9C82BUzd5M0V0_QWNdF6B841ZM8Exp56nSN5GUO5EN1jknCiXOkWwRYbz6gjWzokedGtaVLHA6PArgEVx5RsvZqQKPJt2VfB1uxhbz6owrGcMU7nkuiRP8TVham-H_M8kBJpSXvJmoqlMX-vxbzM-E-eGy01iWYN-yhiaSsUU7W-3U4fE22LqDd_s0Qub_tZFYXYRWoac7LlXhEPyC33XEnmn7NaW9rCvN6NDw99jCKMO69U1XiHpRH58_XYqiiaU255FS2DPI7bti6KtsMg2yDvEoMi3KVQ8qWbfXwDnkEoRCCAxM4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.87M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-466806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtKL0_5ZF8xo1aCc0sG5xmaeFNa6StRHJ4b73A9_X7kySlvqFyj-WIvAvyZ_XTu_dwl4qpWwUtHsNPXYXOA_nv7BMa2MdIhEsjZNPxanWjeSNZ46RlI6zXNavlOKLrvlN_LPt0mOPikqf0XgTJvdbS295S00JRVQL7_D9NFNTExp-hqEw-gbem3MHXVBS-2t_cbjfyykvfkOUxmT0_GYy94he3VSNWB0IxsZ8dbhHZWenTF0PJ5fELNbMMeYpOYB5DcTM1IYq7kXSotewbEcuNB6RVHPH0xL8OaLlhLCGEThveND6bIGKtHyqmXg4BY5N5YImLLHvrXpCeT0lV_xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم نیروهای ویژۀ نیروی زمینی سپاه برای شرکت در رزمایش ضدتروریستی شانگهای وارد بلاروس شد
🔹
روابط‌عمومی نیروی زمینی سپاه: تیم نیروی زمینی سپاه پاسداران، به نمایندگی از نیروهای مسلح کشورمان، برای شرکت در رزمایش مشترک ضدتروریستی کشورهای عضو سازمان همکاری شانگهای،…</div>
<div class="tg-footer">👁️ 322 · <a href="https://t.me/farsna/466806" target="_blank">📅 13:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ماجرای حکم ۱۰ ماه حبس برای رسایی چه بود؟
🔹
حمید رسایی، نماینده تهران در مجلس، در پروندۀ شکایت محمدباقر قالیباف، رئیس مجلس، به ۱۰ ماه حبس محکوم شده است.
🔹
موضوع اصلی این محکومیت، مطلب منتشرشده در نشریۀ «۹ دی» در دی‌ماه ۱۴۰۲ با تیتر «دستکاری قالیباف در اسناد…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/466805" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwcdvuWz7M0vbX1LQXctenqwSEJn3hKmUmTAl0dSY-8jJL_NsIr3cBsSMc2eay4Ql_HG5ergEeZiyK-t3me0F5EASxXI8IKgCL9Ld1EGDSlVDby8aBu5jWIp7AfDjGKe7sETGBzxW0Pje1MfJYiG6tmU6II9wauyZhj_6mPqoeOEqpcQmW-wrqHKYvTAX0RHfMK_Al0NV6R359ym1REbt5OAdRwQceZXwVd9kjnoAz1-P5fRp1YaVR8qhuSM4mh0orI5G-WzgcyQsl86rkWv22l5xKEF_zaf0gI8yl4kz0lljp38m7lZYYg5bBI4H3zbU4yeBFtu5C2hPKLs56blzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف ۱۵ شوتی سوختی در میناب
🔹
فرمانده انتظامی مینابِ هرمزگان: درپی توقیف ۱۵ خودروی شوتی، بیش‌از ۳ هزار لیتر بنزین کشف و ۱۵ متهم دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/farsna/466804" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b9357478.mp4?token=YpTjeq3RbrtTXbgv8mw_1ryyjfJnUC8lpXKDEBE1djbvhmV2JoMx1cAy51YecS5InG4VSRM3qVKsI-bn98a-PRnV5Qv1ReevNcJGgp2qeYYZNRdQa_RktHzMu-sLP4y6J3q92KU6AL2FS--obrRjpkh264QtdWWul_OZw0aQTfA4I3KwXWxIC9Y0UzWtCqJ5OYTtVIc0fdDJaIsmLKhMYbIr7p4FgWMeSnQrdse48hypaIgg0tklSWkZksnUCUHFxWDPi6g12Oj4vhfK6mduT-SNJXXb0Yqe9CD0EbtI0c0gkx7WVdWAgsBcKVzkLvp3slmTh40VVHqcEa_mcG7u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b9357478.mp4?token=YpTjeq3RbrtTXbgv8mw_1ryyjfJnUC8lpXKDEBE1djbvhmV2JoMx1cAy51YecS5InG4VSRM3qVKsI-bn98a-PRnV5Qv1ReevNcJGgp2qeYYZNRdQa_RktHzMu-sLP4y6J3q92KU6AL2FS--obrRjpkh264QtdWWul_OZw0aQTfA4I3KwXWxIC9Y0UzWtCqJ5OYTtVIc0fdDJaIsmLKhMYbIr7p4FgWMeSnQrdse48hypaIgg0tklSWkZksnUCUHFxWDPi6g12Oj4vhfK6mduT-SNJXXb0Yqe9CD0EbtI0c0gkx7WVdWAgsBcKVzkLvp3slmTh40VVHqcEa_mcG7u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: ۸۰ میلیون دلار برای پوشش خسارات واردشده به کشتی‌ها و هواپیماها توسط صنعت بیمه پرداخت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/466803" target="_blank">📅 12:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پلمب تالار متخلف در قم به‌خاطر هنجارشکنی همسر علی دایی
🔹
پس‌از حضور علی دایی پیشکوست فوتبال و همسر وی بدون رعایت حجاب در همایش مرتبط با یک شرکت خصوصی در تالار کهکشان غدیر قم، با درخواست مردم و دستور دادستان قم، صنف برگزارکننده پلمب و برای عوامل برگزارکننده پروندهٔ قضایی تشکیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/466802" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkVyclI9CnvQ5XdFeVOKWwbbrS7QaDmumkYBRlzqgOEyRAR7Ew-Y09IaOs7Syly2vHETvt8cFwV05egRTamvmJFCkrUnvbsUjzHF0ZyyAmeY1zwXHF1pahjiqVBaWT17mmb-4mgsHdKH38ueJv2QuTT0lMCELVWhSR6hLiazS0GHZONUSRdolyrYcz9jPevWYGjtCRn0_knxe0iR4cMYk-SJJptHP-nWGLA7wFUmOTdAMOL8joctS6WoDjO2cNU5fghJx21poA_skPr-W4sGSDzi97_5E5FUtQR2CKSAlRsB3QSDn7i__ZR9WAj1QzaWdNKuL8IRWoLs9WRe2qfxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
🔹
طبق اظهارات وزیر رفاه و رئیس سازمان برنامه‌وبودجه، قرار بوده اعتبار برخی دهک‌های درآمدی از این ماه بین ۳۰۰ تا ۵۰۰ هزار تومان…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/466801" target="_blank">📅 12:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دستگیری شرور گروهک تجزیه‌طلب در ترکیه
🔹
یکی از اعضای گروهک تروریستی تجزیه‌طلب که قصد پناهندگی به اروپا را داشته، در کشور ترکیه توسط نیروهای امنیتی دستگیر شده و به ایران بازگردانده خواهد شد.
🔹
فرد دستگیرشده سالهاست به گروهک تجزیه‌طلب کردی پیوسته و فعالیت زیاد و تبلیغات گسترده‌ای علیه جمهوری اسلامی داشته.
🔹
خط‌دهی به عوامل داخلی جهت آتش‌زدن و پرتاب کوکتل‌مولوتف و مواد محترقه، شعارنویسی و سنگ‌پراکنی به مغازه و منازل از دیگر اقدامات مخرب این عنصر گروهک تروریستی است.
🔹
همچنین گفته شده او از عوامل اصلی آموزش و سازماندهی و هدایت اغتشاشگران به‌ویژه در فتنۀ ۱۴۰۱ بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/466800" target="_blank">📅 12:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH-pJqMdDfau1HOHC_qYSS4ta_WwEsRZfN5PFrcB-E0Nb8elQPDCB5Uo2Hf-lAlKE1IUCoIMS0J1Ws_Qxh0qpQoeJv4sf8obfKFa-7_0w6SrgBfwvoqTcWjUkEWnrlFB7ej0raLT7VjxJytyh_yfoCS8QkshuqFti6DzV_RRiPBPRpzMySH8qJmZxLahdOLQoACQagH_aIN1hSI7PP7T1JZ0DvRuCZ-qnSb3Pq7Zg_h2CMLqHeCjpkAi7UsDtdvufkMDFb2uASRb4s6CoJJlsDLcFKAhzs4AyMYJfbE_w7hB2ErziMfFqhz3_lKOMdrWiQQ43PwgTuxCc-1--ddGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادری که قدس را حمل می‌کند
🔹
طرحی هنری با موضوع فلسطین و قدس، با عنوان «مادری که قدس را حمل می‌کند»، در تهران اجرا شد.
🔹
این اثر با اجرای نقاشی بهزاد حق‌گویی، نقاش برجسته با الهام از شهادت مادر فلسطینی باردار در جریان جنگ طراحی شده است.
🔹
قدومی، نمایندۀ حماس در ایران: پیام این اثر و ایده‌ای که در تهران اجرا شده، قابلیت آن را دارد که در شهرهای کشورهای عربی و دیگر کشورها نیز اجرا شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/466799" target="_blank">📅 11:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در خمین
🔹
به‌دنبال اجرای عملیات کنترل‌شده، احتمال شنیده‌شدن صدای انفجار طی فردا در خمینِ استان مرکزی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/466798" target="_blank">📅 11:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzJIi8R1PTTy3sMzSzkyPTL42M_sl6-YFBgZdcrWwNfLKren-MwJapT_Q66-QPizW6o3xfnkIpCRZgtH2N7EEJwi51Z83NEj2z_Jic8PBAZUJ4So7TQA5DCp138_YtMw0r1UVB5BSrwt64QX8nHfNuPpkabDdzzykRVu2CGy_XbHt1fsNhxlz53MdQ5MlTuDsk_IDJ9KDgQ9xkUxEbEQDtRdJbVta2MP280Z_sms02Trv1eHeghXunreCD8Om_vHDo4-Z-hPoyZE8-ban_Q1bfqNwaRIlDamOjdUtIkBoi6MBPyWRVkqe3y2VI5HgYGr236LPAqNsC81C67tJcIr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: مقاومت همچنان می‌تازد
🔹
حزب‌الله لبنان در بیانیه‌ای به‌مناسبت سالروز طوفان‌الاقصی: ۳ سال پس‌از عملیات طوفان‌الاقصی، جدل دربارهٔ روایت‌های آن همچنان پایان نیافته است؛ اما آنچه بر همگان محرز شده، این است که دشمن صهیونیستی نتوانست به اهدافش برسد.
🔹
در…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/466797" target="_blank">📅 11:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69090f317.mp4?token=kgSRHc5NIszKcVGpSIZZKlBKdTlqc3EOC36oVP4UGyGryO9l3kR0-aGB2BYXOxILTe8s3Rw3UH9eQObE0C6VojAokUVWImcQt1VthuB0pbZSt4FSyNrfJslUdoVBD4DKcKPzVR3jnjGGJ4J7iH57_mSKVN-4vgkJ7JoBaoErjyY1V5yN0g0f4fqPc_aEWr2x2anLjeSMY1y9WrzHDHaazjLiRjSe1-XwojmQtH-FSpjjeRWqwR3e4snp8HdM_URb9Fo21nF_qPgmt0PwGdr4PM01DhB2aWdpGzuf_5A5aR9c0FC2HivHp73UK0y2_mMmdCKmZdc_KXDiEJ56KDH6gUhesMTkH_q0-vds8hcjSwaZq59GvJivwpBKLGNPEulVOmj29XheBhEKwqEj_ld_I9srcQlOiSZfWu_N0ftecqoVB2A22XMzVtft02ujgNMbRZw49TUcTKnKImXtx_DT-vmvnG9hABfbqDggn3GzR6LINtgbM1HTp6Y7WuzG4Kpu609fDn2cW05dsbrWPYKL_Fsr8rTDRgVL3hFleg6x_XNKSHZF8rOurpWyA2_YGPEHTsD3AuhZhSWdXDkxJLBYMpK3kZZZ6jX6FypJcJbLWfyLNaPZ1IRxjxuj_NUhXVeGUbdcwyvVPp0-O-yH6zWQOnv_6HeqqGyeg-YS0NBbEI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69090f317.mp4?token=kgSRHc5NIszKcVGpSIZZKlBKdTlqc3EOC36oVP4UGyGryO9l3kR0-aGB2BYXOxILTe8s3Rw3UH9eQObE0C6VojAokUVWImcQt1VthuB0pbZSt4FSyNrfJslUdoVBD4DKcKPzVR3jnjGGJ4J7iH57_mSKVN-4vgkJ7JoBaoErjyY1V5yN0g0f4fqPc_aEWr2x2anLjeSMY1y9WrzHDHaazjLiRjSe1-XwojmQtH-FSpjjeRWqwR3e4snp8HdM_URb9Fo21nF_qPgmt0PwGdr4PM01DhB2aWdpGzuf_5A5aR9c0FC2HivHp73UK0y2_mMmdCKmZdc_KXDiEJ56KDH6gUhesMTkH_q0-vds8hcjSwaZq59GvJivwpBKLGNPEulVOmj29XheBhEKwqEj_ld_I9srcQlOiSZfWu_N0ftecqoVB2A22XMzVtft02ujgNMbRZw49TUcTKnKImXtx_DT-vmvnG9hABfbqDggn3GzR6LINtgbM1HTp6Y7WuzG4Kpu609fDn2cW05dsbrWPYKL_Fsr8rTDRgVL3hFleg6x_XNKSHZF8rOurpWyA2_YGPEHTsD3AuhZhSWdXDkxJLBYMpK3kZZZ6jX6FypJcJbLWfyLNaPZ1IRxjxuj_NUhXVeGUbdcwyvVPp0-O-yH6zWQOnv_6HeqqGyeg-YS0NBbEI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/466796" target="_blank">📅 11:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxzN4FShU69mmZyTS6Q3tSO_eWBHrsK3lS9l9JyUnjKiUajN1jI2Z_xq7BzMfBt8nf6BtjfrFNTeuEyPSiOwW58AJ4Tali-bwJg8dFDlys6-gF9V2i6G8pkFWapdoSDunjlERFkBJGSyTcRrXyc71RjuL3pplVoRxUSkl_k-2Wx6G6i1-OM3YO7Ff0bzMCD-rHmYY1v0KVbis6MGiJO8RJOyiN2CVHpX4AkHgPaKqBmTFUhVVwRg4JPSf9WNV9OpvMkkTl0LBB4ngWJM-8ZIZX2xkqLqNwWycnoOKaG4-4hwH06PzLT5WpOS4Jq654ka7RFbeCUa49sR8S3UskMRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: مقاومت همچنان می‌تازد
🔹
حزب‌الله لبنان در بیانیه‌ای به‌مناسبت سالروز طوفان‌الاقصی: ۳ سال پس‌از عملیات طوفان‌الاقصی، جدل دربارهٔ روایت‌های آن همچنان پایان نیافته است؛ اما آنچه بر همگان محرز شده، این است که دشمن صهیونیستی نتوانست به اهدافش برسد.
🔹
در حمایت از ملت مظلوم و مقاومت‌کننده تردیدی نداریم و محکومیت شدید خود را نسبت به نسل‌کشی صهیونیستی تجدید می‌کنیم.
🔹
سکوت و چاپلوسی برای دشمن، چیزی جز تضعیف حاکمیت آن‌ها و توانمندسازی دشمن برای تصمیم‌گیری درباره آیندهٔ کشورها و ملت‌هایشان نخواهد داشت.
🔹
دشمن صهیونیستی با وجود تمام موفقیت‌های تاکتیکی، در باتلاق شکست گرفتار است و مقاومت همچنان به مسیر خود ادامه می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/466795" target="_blank">📅 11:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466788">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JooX7BHRyh_tLA0UO4dFYnNlFwGpLYdH1GTJrFwBb2JV3NPPbgXh9LULVsDS8HH-W3PCoHGgHEXNsLPEsZjkoHLhwQzLM6NfKREbm6oIis-_KpK_Zv3nV_4nd08HRgqyRvuwGDiakbGpfRtdICWEZA6P_YXlgOn7WviObDYuRSp7oCrY78MpY-jC2MhWUmIGHNNshS_lweS5rwg-WuOMldl50FQmpXfArEymMWalj4xbFRZBrfabRYIIDIGdehnqbIgoTZKMvs7TCTVDW_qSGdeyM2noqK28pFNnqAVjezM1IB3YBxlBd_QpD1aPkuoRmiGYzRK-cRjdgKORSVYxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGki_eLItaR8icVShA4-Qh_h2OjCg6J4YLdLNPtMYzfl0heuy16z09cMee48uJOVlYB2FE0eg7ufsFI3wUSFrsC5i4Zh99zoySAjL8OkMRFgX8c0_b2RJs1_RxrFsaPnBbN6MGJrGbUsfFZu6rKZ8-VTT4ni787Qk6zGSKo_YnIyO_l7le4AGr794Ultneo8_iCWZ6cl-nS--XmC4U6_4RcWIR2qZhcYbS2zh8cP-CO9zyMdg8N1bKi04MK5sl6rLIQwsCltU6Md02XouxLBo8JbXCiAyLTsQkzFUs9Lm0isYlZc9Hc6KoGVU314LVv_tVuXL4DY4GnRLIlCyDeAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3Ruy6TiLEvb6q01jgfbaHYFkWnRHbVNGs8XMgYRqQsVCikJS_bJKAdGyufY1YSdtFoYFKVUMEvHYs_2bZQ6vrtK9IkodUY0jOjrJKmxPAoF_j5XT2OZ8s4NCZNGtYhdivdrwrFPPQJPLzYcSUc6QCvXNTGP_idcdckwtkmzQ_uv6q7Z69YuSGv-sn6Dy-J1XdwrvYanmDd4mVC0zTbHKISP0XXWO5eNH2pl-QfIChru53nKFuA0MVUK0OizaSs-_sIsK6UZLUIpxKFe7TyAdjC3jSUAZxIYxU-sT8zDYNFC7wJyyz-rqsaE7udTyJH7-3j5rHOkrfab3iNaeTE_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my_jFa5CgLO1g-NR2on3_ncKsdBBWwz58zf8KXdBw4PF2B2Kp2jH_qtMt8x8gb_Nd-Z9PXuZLmZyQwkanmSnB-YQmY3hCJJbxjtcRQxYA-_SEXFGPN3nc9aVvfzppV49X46IVqNprJ9ByeTfddgfH9_Ay_XNn1b2XSB25uEaM36HCH0olG0KT72WhegaGQp2vucxuhmJPortjddgLG_EFE4ze27I3LVZGeAqRPNfXjBVB6wafM3f5XpMy5Jy3jYqcpdcJmyKZ_Ri-OMujl_0OI1f1R-18Lt7L7HUfhd-eOAn7cBfx3aQXdn0lSF2c0PqeoOKhSbCAt-tdfRbxM8xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_8SdUcft7uHG0m8AG4t8T_nuhB6dROVnG7YD5zI-Jfa9zixy1ZWI9aVEGzKxbAFcbX600xHwO0EvDI9ryVa0fc9VYizxAoZMOwjfbC8lBTFEOIb8movyEJd5M_h6ev42hooO-JosHTJnxjOMD1qGsO6De7XECxzPnh2uxMWCgqbcOZuLeBVd4sL5LXeBQ1OR86W2hPYIWiE2aArC0fHxVajSInBsZIWgS3731oRAJELUo9k2W231QcJTf-4mZCSJG26h7VDF6aT3H7raEM-d3RbdyCEo8ocqRPGSI1S6JCco1IgVgCLVaT2nt09NDliTATAPl5W8IJ3lo0pGkAW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvYNrwsNfD2HOCZioCmlpxTJnMq1ZbElYbVB_aOg_e81M_XHXb1RxnDPw7LfAVbwcygLMaLZoZdGC2K9gQpx9mB8AABkTZBXCCYLadDkbjE20YhiGcxwb32-LcsZslMX5Z5O_GoRXVNLeqXG4dED-oUA4yQj0-KKyEmaF_h7BlO2U8zt36bMnNWt1xL_WH_Pwaymt4Cj_za2gQooUyjBLuuYRl6Yn4IKOBJEYtBKRmpI4toRhrCPD0eqpcYldp7KOdFcZF-Uj4UX5gPynALwDJmAjyAeKy5TZyTr_giOMspqiYBCI5bWgVaujf4fo349DyExsHBS7LYQNIg7P7vUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-yAmE0YLNS1NpoBJnb1wY8ycxsJZrRi46WQFMuLNo_ywdv8OGynjp9i8h7k12OO1mjcHN0MeiQrfQrPlVkxUoJP4E74ZcABN-9v26LGQaowV_7HlmuF_1UBjWSL90707616PKSzcRFIYTI7GsRSkXss8UY464qni5Q6bf6ygwgaovFnHnSSK1MHYShrHr2KxdW2kvSGYczuj37h1WcAL3dDUUblRee9-qX2CchH54H_weiqLFek03wEUDV0aHsDNou6SZ1cjV1nnj8r5xY4nMj0Locx2_IoULlPTm9bquoCADTRSvdPd1sgcWRk-ZtCgo24YQQuz7e-XZHsiAUaug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کردستان را از دریچهٔ روستاهایش ببیینید
🗓
۱۵ مهر روز بزرگداشت روستا است.
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/466788" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466787">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d43d555f7.mp4?token=GpQsBCI6Zgvg0KoFa1ChguvMzITWapdubpuqElR8vUIXWVLu4UCq7X0ubKPMEg6B6q2PCO8pOPyd0SzTj1dPlbMiSeYJX422OZPuxz2tdWh53I8Fiq_UlfmI1LGMHhMBNDnUREoJz-_lZ_NFhMbOkpZkS56m342qBQhuQ_7u2hHk3WdEhs0hb7W4Q6oa94_vS6kZBqvgAfnqI5GpxnCM02JtjIbgfhvCjGcxW3KhMsXTzLdL0GfLjuNKMpYdXdkEUGGfFQ4ElEVKoPz4o_3GjV64JkTo-Wcee6zzpunXxY9SbH0TiL9A2gMnZ5GrHMByLnoxq-sFUIBD7IRXh7dJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d43d555f7.mp4?token=GpQsBCI6Zgvg0KoFa1ChguvMzITWapdubpuqElR8vUIXWVLu4UCq7X0ubKPMEg6B6q2PCO8pOPyd0SzTj1dPlbMiSeYJX422OZPuxz2tdWh53I8Fiq_UlfmI1LGMHhMBNDnUREoJz-_lZ_NFhMbOkpZkS56m342qBQhuQ_7u2hHk3WdEhs0hb7W4Q6oa94_vS6kZBqvgAfnqI5GpxnCM02JtjIbgfhvCjGcxW3KhMsXTzLdL0GfLjuNKMpYdXdkEUGGfFQ4ElEVKoPz4o_3GjV64JkTo-Wcee6zzpunXxY9SbH0TiL9A2gMnZ5GrHMByLnoxq-sFUIBD7IRXh7dJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/466787" target="_blank">📅 11:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466786">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بازداشت یکی از مدیران نفتی خوزستان
🔹
یکی از مدیران صنعت نفت در خوزستان به‌اتهام ارتشا و تخلفات مالی بازداشت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/466786" target="_blank">📅 11:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466785">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کشف محمولۀ مواد منفجره قبل از ورود به مشهد
🔹
فرمانده انتظامی خراسان‌رضوی: یک خودروی حامل مواد منفجره قبل‌از ورود به مشهد توقیف و رانندهٔ خودرو دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/466785" target="_blank">📅 11:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466784">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکان خواستار رعایت پوشش حرفه‌ای در کنگره‌ها شدند
🔹
انتشار تصاویری از برخی کنگره‌ها و همایش‌های پزشکی که به گفتۀ جمعی از استادان، پزشکان و کادر درمان با شأن محافل علمی و حرفه پزشکی هم‌خوانی ندارد، مطالبه رعایت جدی‌تر قوانین و پوشش حرفه‌ای در محیط‌های آموزشی، درمانی و علمی را به‌دنبال داشته است.
🔹
جمعی از استادان علوم پزشکی، پزشکان و کادر درمان با اشاره به انتشار برخی تصاویر از کنگره‌ها و همایش‌های پزشکی، خواستار رعایت قوانین کشور و پوشش حرفه‌ای در مراکز درمانی، دانشگاه‌ها، کنگره‌ها و سایر محافل علمی و صنفی شدند.
🔗
متن نامه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466784" target="_blank">📅 10:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466783">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d99b27551.mp4?token=PP6alEozESVsnOx3QOT3hLvx2MNrWgqoV7fI3W_1wV-2ME-hlnYRRkOeiATZxdWY8VsWHxSSCeKx89ZpNlcVkQucb6M-HlmMmizjx_0a6L2GxPWa4iO-K5vtNZh1y7d1v7uLTEQ02HMUX67-eaLuyTv1_-RGdXunjNM54QZjSoM83wgif55A7NLjwsNwOo2yQ_Q3H7YsyYTtu6PBGqdT-NUX5r8k3XMgfsHABtHLpLLPadxcaCBtRmcRMLTfluLQj9y_vZXVyEwySr-0O8MehBYGQjrW6fQNT8eAp2iMyYFikuEkAKtKeTdiDogsraoinz8oPjDsxQcj8fkpWUTU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d99b27551.mp4?token=PP6alEozESVsnOx3QOT3hLvx2MNrWgqoV7fI3W_1wV-2ME-hlnYRRkOeiATZxdWY8VsWHxSSCeKx89ZpNlcVkQucb6M-HlmMmizjx_0a6L2GxPWa4iO-K5vtNZh1y7d1v7uLTEQ02HMUX67-eaLuyTv1_-RGdXunjNM54QZjSoM83wgif55A7NLjwsNwOo2yQ_Q3H7YsyYTtu6PBGqdT-NUX5r8k3XMgfsHABtHLpLLPadxcaCBtRmcRMLTfluLQj9y_vZXVyEwySr-0O8MehBYGQjrW6fQNT8eAp2iMyYFikuEkAKtKeTdiDogsraoinz8oPjDsxQcj8fkpWUTU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از روزی می‌ترسم که خدا از من سوال کند که چه‌ کار کردی
؟
🔹
همۀ کارها را برای خدا می‌کنم و دنبال پاداش نیستم؛ از روزی می‌ترسم که خدا از من سوال کند که چه‌ کار کردی.
🔹
اگر کسی که ادعای مسلمانی کند ولی دروغ بگوید و به داد مردم نرسد، مسلمان نیست.
🔹
از خدا می‌خواهیم کمک کند تا به‌جای اینکه بیگانگان را ببینیم، مردم‌مان را ببینیم؛ متاسفانه در خیلی جاها قصور داریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/466783" target="_blank">📅 10:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466782">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7JRlpyf_Odyf8cBBTiN5yZ_LlTbW_fOWi3HB9PXOcCM9iVkBia1DzpEcPgJphGalNQB3ZeRMDQ5qd-0GXTeADXnbIjCH7FSXLyGn5vdiwCBJ-fRfMyatuPMHNtnk4k7oPhimor-IWIx4EbX2_gA8kUpMrj13B5Y3aiQdaqvsUhfpvPpH99XHFy-3n9OMpYAtbUInA626QFlwSIKT-SV1zxpSmgbp8Een97SAPn9gzypVSHy5UW7ThvEAOkzqs96MIW55z-eIVGDBNqbehv8F8O0xcCi77dyp_7w39fQwspuRkodZXc4Ef2PmQt6GzjrQoOq2Tr3CfnCd4ctGRogzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/466782" target="_blank">📅 10:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466781">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6144b045a6.mp4?token=C76hujmq-jopSEccGnEY6ECFbJCLMwbHGGET78z7Prxbfi46DPrPJh3leYRiYoEixieVcBL4Tas-eQ9ECAfSdMKE3luTvx8GUWGNbRgYhC3O3MHhrPCSucq9v8eSaUI6d3IuVsEZ4fSMYr6cWc1gQ1NY299pGlR8znNK3lhB5mfYBsoflQ7VMprXYgEsgM9EUh9jhvheU9SaG26CeN8k5oIHHtk0CCjzYt-jJLug2UzvPjWNNXCzoYAOhDXUnw6iSVhjJDol98SN7CdB4WwUURfunbAwYUFXKxPdXLrLE1Yw3PSM8ediw17_-aSB4Avbr_NlwNrd8vsK-W0GuZjOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6144b045a6.mp4?token=C76hujmq-jopSEccGnEY6ECFbJCLMwbHGGET78z7Prxbfi46DPrPJh3leYRiYoEixieVcBL4Tas-eQ9ECAfSdMKE3luTvx8GUWGNbRgYhC3O3MHhrPCSucq9v8eSaUI6d3IuVsEZ4fSMYr6cWc1gQ1NY299pGlR8znNK3lhB5mfYBsoflQ7VMprXYgEsgM9EUh9jhvheU9SaG26CeN8k5oIHHtk0CCjzYt-jJLug2UzvPjWNNXCzoYAOhDXUnw6iSVhjJDol98SN7CdB4WwUURfunbAwYUFXKxPdXLrLE1Yw3PSM8ediw17_-aSB4Avbr_NlwNrd8vsK-W0GuZjOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دستگاه قضا: در کشور سند کم نداریم اما درصد قابل توجهی از این اسناد محقق نمی‌شوند.  @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/466781" target="_blank">📅 10:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b6d54fd.mp4?token=TPl9sKflgYrPNnO2Lse1ZViY7sYOZR8FmKXLe8z7a5tN3RIT0C0bsxJdKLaAmfIM3E9Q3LvtcCRWaTuc7tEUdVCP50L6yWSWu6ayiaBf71YB54G2XkaI4pVJbLt9koFVGPt5HxgePuCz9W7SwFnHIijuhY-h1za7kHQQBEQ-aitIYCy8eSIPW1QdCF_dq-RVaWTsX03xqLLNBbDCcbBQhmS3_pMmEQK4nsDJjtn2Yz_Op1BAtUh_E2My2VODg_21Q_BmHFiNp7bVYW5mYorMtuUKdIpKag28qJM77W_sUaiKguOtNMxROoNeXwGpBtzN2ZkBRiw-t6FnuhgngikfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b6d54fd.mp4?token=TPl9sKflgYrPNnO2Lse1ZViY7sYOZR8FmKXLe8z7a5tN3RIT0C0bsxJdKLaAmfIM3E9Q3LvtcCRWaTuc7tEUdVCP50L6yWSWu6ayiaBf71YB54G2XkaI4pVJbLt9koFVGPt5HxgePuCz9W7SwFnHIijuhY-h1za7kHQQBEQ-aitIYCy8eSIPW1QdCF_dq-RVaWTsX03xqLLNBbDCcbBQhmS3_pMmEQK4nsDJjtn2Yz_Op1BAtUh_E2My2VODg_21Q_BmHFiNp7bVYW5mYorMtuUKdIpKag28qJM77W_sUaiKguOtNMxROoNeXwGpBtzN2ZkBRiw-t6FnuhgngikfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دستگاه قضا: در کشور سند کم نداریم اما درصد قابل توجهی از این اسناد محقق نمی‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/466780" target="_blank">📅 10:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2722ca14de.mp4?token=Kgla3Y84p57ghXokBEkXYQ64z9qqD0pu6Zh-Ns7Lszsf33jrjRXQhJNvqiPP_CSaQZ4VTXLtJdnANfXiiLZiy2JGSq4eoCro8lXW7hK4FfKLdpVHcXDdnHsML3UkIfyrdxMI1ZQXrU41HELhoWR7CZltse_R2tU_rTobOqk4IWCvZ3DQir8sNzNzZtt3btlc5yRRPPx4tH-JanIjoh6jQd-DmPzNY4slufwDaiLHmiP9XQEW_OOkyZfci1aF8ogAyQRCkt5O0pOIbihQtl-l6fWBSijC2xEd-5gNG97NJGFWhrFN5YtTI-Y52Pdu8O0W4NQdYiS6epGumjNFP97nkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2722ca14de.mp4?token=Kgla3Y84p57ghXokBEkXYQ64z9qqD0pu6Zh-Ns7Lszsf33jrjRXQhJNvqiPP_CSaQZ4VTXLtJdnANfXiiLZiy2JGSq4eoCro8lXW7hK4FfKLdpVHcXDdnHsML3UkIfyrdxMI1ZQXrU41HELhoWR7CZltse_R2tU_rTobOqk4IWCvZ3DQir8sNzNzZtt3btlc5yRRPPx4tH-JanIjoh6jQd-DmPzNY4slufwDaiLHmiP9XQEW_OOkyZfci1aF8ogAyQRCkt5O0pOIbihQtl-l6fWBSijC2xEd-5gNG97NJGFWhrFN5YtTI-Y52Pdu8O0W4NQdYiS6epGumjNFP97nkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان:…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/466779" target="_blank">📅 10:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81db205b.mp4?token=ODZnWjx1Uo7HlaYeZ-Lz4Xk5nmKJU_aoItm4DMKbHsy3gZzarNo_HpbW86OBKklRpVrsFs-f4do7EIzVgz4K1Z_xsyfalFTjieMGcHVJbcPeoiz3m8PZYv0Uq3B8yBlyBqUJlm1GS8Zb9EGoyg2_pjMY98LSlCPu_g7XPFN10ESCx-HZAgea1_3hKUfnS8e2bh294aouX2Krr3gyoDYrGYwggyGxwhK1ySN4MXuHZRPwXm6V4HZcTU-0lKcZgIatlSxPI5TRk1wpE09NWcXY1zDCmY-oiu8f-mMNa9z7zWHO1lqH81LVkC_TxyrSXSuAeIfFV873GCKzq7KdvWlRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81db205b.mp4?token=ODZnWjx1Uo7HlaYeZ-Lz4Xk5nmKJU_aoItm4DMKbHsy3gZzarNo_HpbW86OBKklRpVrsFs-f4do7EIzVgz4K1Z_xsyfalFTjieMGcHVJbcPeoiz3m8PZYv0Uq3B8yBlyBqUJlm1GS8Zb9EGoyg2_pjMY98LSlCPu_g7XPFN10ESCx-HZAgea1_3hKUfnS8e2bh294aouX2Krr3gyoDYrGYwggyGxwhK1ySN4MXuHZRPwXm6V4HZcTU-0lKcZgIatlSxPI5TRk1wpE09NWcXY1zDCmY-oiu8f-mMNa9z7zWHO1lqH81LVkC_TxyrSXSuAeIfFV873GCKzq7KdvWlRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازداشت ۴۸۸ نفر در اعتراضات دانش‌آموزی فرانسه
🔹
وزارت کشور فرانسه از بازداشت ۴۸۸ نفر در چهاردهمین روز اعتراضات خبر داد. شمار بازداشت‌شدگان از آغاز اعتراضات نیز به بیش از ۵ هزار نفر رسیده است.
🔹
در جریان این اعتراضات، شماری از معترضان نیز مجروح شده‌اند؛ از…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/466778" target="_blank">📅 10:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGqgE2HUNilhP3d0An-_uBtpCkwoqiDk99PMU7FmH3aGOquFIGCJFC5SvCduoI5bcOz-j-Sd-T-SZ8DGFM94sSE5-DrUvznmAXXaODLOR4jRP7ZQArIZ8ZI0LCklL_w15JX5PZxEMWKjRIEJQL5hKp3IraUCvQYmFoGspJf0GlSkCuI2q-FhFnjLwoTE2ArtpUEIkRSi1Ebp5eHVGkLjaFSaI7Z-xbLR_whYjH3PUSuTa7uZHXTIOS69Ju0YG5kmaekayRqLZAuB1W-9KYxmkisTvor2TxbG_50AgmG-GB5aBNYtNT0W4WhJUVQh-PSa_XwuUuuBpWA4btVW6iJz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ طلا برای دوومیدانی‌کاران ناشنوای ایران در آسیا
🔹
در مسابقات دوومیدانی ناشنوایان قهرمانی آسیا در مالزی، امیرحسین زارع در پرتاب دیسک به مدال طلا دست ‌یافت.
🔹
علی علیزاده هم در دوی ۸۰۰ متر صاحب مدال طلا شد. علیزاده دیروز هم مدال نقره دوی ۱۵۰۰ را نیز کسب کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/466777" target="_blank">📅 09:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S70CBMSKp0DUzqqRPIqakHl495iQ_zWeCJ27mFsMzGxgUNGCuCPWxWl9NNog8SMcqub06OOxsLTh8yS3qOYX7H3_tlpGcE4KcOoSVT_WE67aFT13TAXCRFJKw48TnoqfWYZQeOjZQ5lSUSIY1eUNeIABRn422qyHJ430cvAbvgpQWTvq98dODDgyERO2mLKAwDkAqRnw8402BnmLvp7FqveuB_VrF9JEZp2IG4irNW5yJqNqL9QDf4EUBb_nq83nAFinWzoQHM9jnPpSUlR2Hkkw2jLNShSmPIlL_tWyi3syeZWh9TWC9_V8gledTGP-NxUXsZzYZg4vSePPAUlSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی: دوست داشتم تا آخر عمرم کنار آرژانتین باشم
مسی در آخرین بازی ملی:
🎙
دوست داشتم برای همیشه، تا آخر عمرم، کنار آرژانتین باشم اما وقت خداحافظی و بازنشستگی فرا رسیده است.
🎙
بعد از آخرین جام جهانی، زمان آن رسیده که خداحافظی کنم. ممنونم از همه، چون بازی کردن برای آرژانتین، بهترین چیزی بود که می‌توانستم تجربه کنم.
🎙
هیچ‌وقت برای این پیراهن تسلیم نشدم. همیشه جنگیدم، ادامه دادم و تمام توانم را گذاشتم. برای ۲۰ سال، تمام تلاشم را برای آرژانتین کردم.
🎙
دیگر کاری جز تشکر از این پیراهن برایم باقی نمانده. من همه وجودم را برای آرژانتین گذاشتم.
🎙
احساساتی که امشب دارم، باورنکردنی است. از همه شما ممنونم و اولین کسی که همین حالا به او فکر می‌کنم، پدرم است.
@Sportfars</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/466776" target="_blank">📅 09:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466774">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCztQD41ivqYyHYnJ-YnGk1wOc9VvWuPe2xKCtP8s5v8tr7aj5IdaCJhaULn1wmode3yL9VhAuoETwzkW7WWT2Qt1Zp5ehwzAdT7gz_mG9u63WI37OQoSkVKTsxk7-OzZTT63inlh89buLZnbCBcF991qhOuYspNByYFYhTRy6u4U9uGTvg3MRXEtPuL75inMItvxpl2o61zQU8AZ2Fs7zxVQYlYwltxV_kVWvdt7FQCZSDmnPsoAIgkEHANfAzCnSAzevkbWdONnlSCY_C6Ovfq3-nShMNg10K560XL8NLshLcSDo-yxScPy37Ri1k86ZqF7lSmQw3CxXj3gPCEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به رکورد ۸ میلیون رسید
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۴۱ هزار واحدی با ثبت رکورد جدید، به ۸ میلیون و ۱۱۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/466774" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466773">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moDuBhySQtnBURFYGFcfD_IoZHLUkEhaqSz2Vl8OMgfS_GebvCGhKoX2Km64GBvCm77uYi2kgJ8AyF6vskpZHNSmtt0LFqY_zeMQqfeKhle7NTINF4DZYvRU0MEkJNd1lVeSHunbmTxVg7yeWi7KtwZFqBzzdx8BtgEIiZ8lgIS8lsaK0vpLF0UTfAeV48kQlnuxZsJ5UHqHew6ABai6vz_m59vCjE-J82XrmkYiSVfO5dixaklrMEq65fg4qcmN9RuI_bM0Vg8qHSvVh4lw7J53bOfzzxbD8jXtAg7gBToFslnqlGkdJ3VsmBqFQZ1y31FndofdlkJ8nhAKcseeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/466773" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466772">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b443b53971.mp4?token=ESzb1ajJuDaZgxnwSAXcz8UmyJpX3947ZWbNSXU3VDInEiBSrDf8StTG3Fi841rOKh1R9nINArHE4Rp3c_Rg182xeLvCbdg_GEXZw1VLlct4VPzBU6gV0XxGWiMUu5Cec2aydY6aOPZrJPHJCQXSsVWmrbz407PeWHdoCk74Vs3ppbl7Ooi0NbLViDbS4uzkdV9Rb8NEOO4iohs-0Aiv7TS3j6eaVBYwzLYcLIdVwiQQbLVCfnhEGRiKs2nHnXvuItSpiS-GioLb_d1leYbJKBrzLrrff4jO2Ih6eQaT6PIzymbGwocjymNZd4zH7g-vjCyK86xg4ganlRHL8lj5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b443b53971.mp4?token=ESzb1ajJuDaZgxnwSAXcz8UmyJpX3947ZWbNSXU3VDInEiBSrDf8StTG3Fi841rOKh1R9nINArHE4Rp3c_Rg182xeLvCbdg_GEXZw1VLlct4VPzBU6gV0XxGWiMUu5Cec2aydY6aOPZrJPHJCQXSsVWmrbz407PeWHdoCk74Vs3ppbl7Ooi0NbLViDbS4uzkdV9Rb8NEOO4iohs-0Aiv7TS3j6eaVBYwzLYcLIdVwiQQbLVCfnhEGRiKs2nHnXvuItSpiS-GioLb_d1leYbJKBrzLrrff4jO2Ih6eQaT6PIzymbGwocjymNZd4zH7g-vjCyK86xg4ganlRHL8lj5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/466772" target="_blank">📅 09:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466771">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11569a18b.mp4?token=T7LQ_mm0WoDpflhRogHK2QW7fSVe9bRbOaeuvFWP7KKR_bBECr7Ts_rMaiDx0qnZD4UMaKWMCLRWcUeqMrt9XxMTiGzZ4XLyjReIbiwVblnBhnoM5MLjQYFyorCA8mkDOg82Dx8vPFqo6Dqv6MXmhP1QJGX5wfNRgLolRyb5PWO3Z7BnpJwO3fGg-tPwDYmX-Bste8vinvOldBEdG1I8t0oCTLWBCl4qb68gac4d07iOpQWygDDc393wpwXnQ-8p9xcaRNf79fLhzpXBdB3AdiDlA1EvhlOAb7X_Z5FtAGdzkuMlMLxX2ZHVU57WZjMlO0DY0GKAMjM_JzISmLY8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11569a18b.mp4?token=T7LQ_mm0WoDpflhRogHK2QW7fSVe9bRbOaeuvFWP7KKR_bBECr7Ts_rMaiDx0qnZD4UMaKWMCLRWcUeqMrt9XxMTiGzZ4XLyjReIbiwVblnBhnoM5MLjQYFyorCA8mkDOg82Dx8vPFqo6Dqv6MXmhP1QJGX5wfNRgLolRyb5PWO3Z7BnpJwO3fGg-tPwDYmX-Bste8vinvOldBEdG1I8t0oCTLWBCl4qb68gac4d07iOpQWygDDc393wpwXnQ-8p9xcaRNf79fLhzpXBdB3AdiDlA1EvhlOAb7X_Z5FtAGdzkuMlMLxX2ZHVU57WZjMlO0DY0GKAMjM_JzISmLY8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/466771" target="_blank">📅 09:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466770">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd10a25b4.mp4?token=Y7lg4hEBVVoUn14A6WTjJ5S5YEn4Nu3yaRidghjZpnaMQFXTrtqJjUrUB4IPhnIRLENyR631UHszdC6_F7OW4iHm5jyWiyS_TgSTF4nAdaibYtlm-vyiG3N_p2hHdeXaceY0Fbb5I5Se-J-D5NaQwJJANeEajDwAjQFNeVGPrGFsFMCVKjHKANf-zLlN3Ab4DggmP9CFbzlxdGDpVnqUKyYgsfff_rOjtRKCtcPzfwCKu6DJe44IvFxLfrwkn2qKQVuOz0z3VvsiG62Mo8J5SIdsGwk8-htCwFiH8Bs-U-FJvEbuu1v-86VgjHojjLUm34HDbtc9InpJ-4KcCLUyhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd10a25b4.mp4?token=Y7lg4hEBVVoUn14A6WTjJ5S5YEn4Nu3yaRidghjZpnaMQFXTrtqJjUrUB4IPhnIRLENyR631UHszdC6_F7OW4iHm5jyWiyS_TgSTF4nAdaibYtlm-vyiG3N_p2hHdeXaceY0Fbb5I5Se-J-D5NaQwJJANeEajDwAjQFNeVGPrGFsFMCVKjHKANf-zLlN3Ab4DggmP9CFbzlxdGDpVnqUKyYgsfff_rOjtRKCtcPzfwCKu6DJe44IvFxLfrwkn2qKQVuOz0z3VvsiG62Mo8J5SIdsGwk8-htCwFiH8Bs-U-FJvEbuu1v-86VgjHojjLUm34HDbtc9InpJ-4KcCLUyhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/466770" target="_blank">📅 09:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc2m4H7DFVCUR03KwSW2IGg_yPxfTvcw2VKNnWBiAIuCuBJWVdl-EFzogYh_NvaFu_HUq7xXlJrvt77sRPkLOh738cfSq3Atg0DJK_wu7I6Q6cU6bBdZYJz8oBVD7CTYpFrwtYtjJmeymeYuf6lwZYePJmGmWhCkXdF_g9znHCSBFVVV-yEA6i2pABxnbaB5mUdQ7qpORjY5J1RRnIJI7LTmJ8lRFUsPenOuEjovvoe8xI-zir-eHCmn1-ZDwvmmk48X1Wuj3Hz5sM4HMsaysbmIhrQCG6MT7YlEhXqYQf0gJW1gURmlpZ3MDi_qZ3ZA82q5C8fhwQstHsJ4w1QXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سدهای تهران ۱۵۵ میلیون مترمکعب پُرآب‌تر از پارسال
🔹
مدیرعامل آبفای تهران: ذخایر سدهای تهران نسبت به سال گذشته ۱۵۵ میلیون مترمکعب افزایش داشته است.
🔹
این افزایش درحالی رقم خورده که برای عبور از یک سال آبی نرمال، ذخیره ۸۰۰ تا ۸۵۰ میلیون مترمکعبی در ۵ سد تأمین‌کنندهٔ آب تهران مورد نیاز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466769" target="_blank">📅 09:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4096a7c0d.mp4?token=jtWM22kOMSS2xkOQ4jKkaZY9o7cPYcPc2XpTpDxEapT8MOzOUmDLfxH0AhqZ5iU4FAyXEr-rWvC5C4KZ40Gt-LVDj7EB59NNCi1Uamo_4zf7rFwromW--uptzO7NYjDb5kIDFTtmXsN2ni3cLrXTy0Yk3ItKWeThCvUOO7jC_rul433hSRfYawqHUzhIYFzV-qu5WJ9CP-xttMn0mhwW33iStTyJc3k4HmBB42dTxX0aKWVSQc0Z4BPpAH6NbzigeDgte2Rb2qw_AlIeC0gT9_FvoFFQybaTu0KyQckHVCBTfL0IevSdm4zM02cpxEjaf3GC0V2uPypwUU_oBDMyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4096a7c0d.mp4?token=jtWM22kOMSS2xkOQ4jKkaZY9o7cPYcPc2XpTpDxEapT8MOzOUmDLfxH0AhqZ5iU4FAyXEr-rWvC5C4KZ40Gt-LVDj7EB59NNCi1Uamo_4zf7rFwromW--uptzO7NYjDb5kIDFTtmXsN2ni3cLrXTy0Yk3ItKWeThCvUOO7jC_rul433hSRfYawqHUzhIYFzV-qu5WJ9CP-xttMn0mhwW33iStTyJc3k4HmBB42dTxX0aKWVSQc0Z4BPpAH6NbzigeDgte2Rb2qw_AlIeC0gT9_FvoFFQybaTu0KyQckHVCBTfL0IevSdm4zM02cpxEjaf3GC0V2uPypwUU_oBDMyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌ها به‌صورت پراکنده در بخش‌هایی از کشور طی ساعت‌های آینده اتفاق می‌افتد
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/466768" target="_blank">📅 08:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ7SYK8S8lYjH2yVRywInIgmXiImyl7vzxgu42aTmyVhAzP_gtZrgZY8ODCuwkjUtz7z8cs78FrmgfKnHDkvgEJvLnAsjfhlNC7WU8J9edpVS8wduEQ6z69FqJsAG1JWShgGbDLl4Jhl3pxHjTjGe0tcBLlfPcvJuExDW99KqZfm84nq2T-CZ3ej8ilgNVUHCcAimQAnKWAXHdrGq7-kOiDzVF83FlLxY6AldiblwoODBrwwpj3IMbsAnM3sr1Z_BdAmYoJhAMQdN42-lYCFeqNxcnZX8fABzT2Bzr-Ugmx1820j8TXraWb9CECe9rd9LF5b-zz_Z4ZolqybN_MZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
🔹
طبق اظهارات وزیر رفاه و رئیس سازمان برنامه‌وبودجه، قرار بوده اعتبار برخی دهک‌های درآمدی از این ماه بین ۳۰۰ تا ۵۰۰ هزار تومان افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/466767" target="_blank">📅 08:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هوای تهران همچنان «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۴، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/466766" target="_blank">📅 07:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466765">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نخستین آزمون تبدیل وضعیت کارکنان پیمانی برگزار می‌شود
🔹
سخنگوی سازمان اداری و استخدامی کشور: کارکنان پیمانی که در زمان استخدام بدون آزمون استخدامی و با نشر عمومی به‌کارگیری شده‌اند، با شرکت در این آزمون و کسب حد نصاب نمره، می‌توانند برای تبدیل وضعیت استخدامی خود اقدام کنند.
🔸
ثبت‌نام آزمون از ۱۶ تا ۲۵ مهرماه به نشانی
www.hrtc.ir
انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466765" target="_blank">📅 07:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
سخنگوی انصارالله یمن: فرودگاه ملک خالد عربستان را با چندین فروند پهپاد هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466764" target="_blank">📅 07:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در ریاض
🔹
منابع محلی از شنیده‌شدن صدای انفجارهایی در پایتخت عربستان سعودی خبر دادند.
🔹
همزمان گفته می‌شود فعالیت فرودگاه بین‌المللی «ملک خالد» در ریاض متوقف شده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/466763" target="_blank">📅 07:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
آمریکا ۱۲ بمب‌افکن B-1 را از انگلیس خارج کرد
🔹
پس‌از وقوع حادثه‌ای در پایگاه هوایی فرفورد انگلیس، آمریکا تمام بمب‌افکن‌های راهبردیB-1 مستقر در این پایگاه را به آمریکا بازگرداند.
🔹
این پایگاه محل فرود بمب‌افکن‌های آمریکایی برای انجام حملات علیه ایران بود.…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466762" target="_blank">📅 06:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN_K50Kt0FOYvj2qqu2HpbVmtnMdfoFflXcwPJ_oVj3i0sLsU87VJO_I11O_ehDYFkiV-q4iNSxMuDfQnKhTqr8nIi6pUng3h2YIWG1YPMxc_ac3OzmUfbVaxlb6D3UedrRmd8si5fXQfRYkiRYshsHGs1GyrcZHNYnZmLocF-R4UC20T-wvDInXjyeWrt2bdJ6RvEGz_YxnH4Ydc5DxBmVaz7248eIQimF65zumogAyquMiHj1y6VElsbFK0ap55ngKCQSNDnlaagiuf8FRSIR56gIoOkuw4bNHcMcGZgLDVEUFad8Uzn6hXdlJUC22J2NQk5Y94IKHX6zUfkTVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی رئیس مجلس نمایندگان آمریکا از استیضاح ترامپ
🔹
رئیس مجلس نمایندگان آمریکا هشدار داد که در صورت پیروزی دموکرات‌ها در انتخابات میان‌دوره‌ای، در اولین روز کاری‌شان، ترامپ، رئیس‌جمهور این کشور را استیضاح می‌کنند.
🔹
این انتخابات که ترکیب جدید مجلس نمایندگان و سرنوشت ۳۵ کرسی سنا را تعیین خواهد کرد، ۳ نوامبر (۱۲ آبان) برگزار خواهد شد.
🔹
هم‌اکنون جمهوری‌خواهان با اختلاف کمی کنترل هر دو مجلس کنگرهٔ آمریکا را در اختیار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466761" target="_blank">📅 06:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انهدام پهپاد ارتش سعودی بر فراز یمن
🔹
یحیی سریع، سخنگوی نیروهای مسلح یمن: پهپاد شناسایی-رزمی «CH-4» عربستان را در حالی که مشغول انجام مأموریت‌ بر فراز استان «الجوف» بود، سرنگون کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/466760" target="_blank">📅 05:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در ریاض
🔹
منابع محلی از شنیده‌شدن صدای انفجارهایی در پایتخت عربستان سعودی خبر دادند.
🔹
همزمان گفته می‌شود فعالیت فرودگاه بین‌المللی «ملک خالد» در ریاض متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466759" target="_blank">📅 04:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebb55f5d6.mp4?token=RoZ_QYUvHxkrn62eyWkjNQwNmELMKEKFHzQD5CQbHALCBJ8faI_HVQsPAOzWYERAuRdo7w9BQp9_565NCYWcerQl3EXH2SslvIZggtAaYEsgjP19xGvZHlqfp7TjhOiHUrbaxVKnmNTnQci_NeRHo-Qi0zbK8GE3Vy1WlETI-A9kSVgBAqrYgRCfURkyeQEUJ871YPuuBAKwC4ZxcCjDm0Fgc5Yw6n7pLqCwWWOP3DBtyds16c-KziHj8KLprD0MKrp-PPh0yadJXKLV3mzGzsnGVKZj8676lcKr9jhi9xch9-eUBapDkgGIwNAeZN0PE0nsUhLUMNOnAC0F0fZaHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebb55f5d6.mp4?token=RoZ_QYUvHxkrn62eyWkjNQwNmELMKEKFHzQD5CQbHALCBJ8faI_HVQsPAOzWYERAuRdo7w9BQp9_565NCYWcerQl3EXH2SslvIZggtAaYEsgjP19xGvZHlqfp7TjhOiHUrbaxVKnmNTnQci_NeRHo-Qi0zbK8GE3Vy1WlETI-A9kSVgBAqrYgRCfURkyeQEUJ871YPuuBAKwC4ZxcCjDm0Fgc5Yw6n7pLqCwWWOP3DBtyds16c-KziHj8KLprD0MKrp-PPh0yadJXKLV3mzGzsnGVKZj8676lcKr9jhi9xch9-eUBapDkgGIwNAeZN0PE0nsUhLUMNOnAC0F0fZaHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملهٔ یمن به مقر نیروهای سعودی در فرودگاه عدن
🔹
رسانه‌های عربی گزارش دادند که نیروهای مسلح یمن با موشک‌های بالستیک، مواضع تیپ ۲۲ ارتش سعودی در فرودگاه عدن را هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466758" target="_blank">📅 04:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twYUwWeskviNChtrGNmS0K71pCYHjnjlSoAdCo_9PmosOmKM3OGHibclFWYG73qKFW8jNFk8k0kMnYBOaRDyv6muTSnRIKKse5TFGWZZwgQNXxraM1ZAjAqxGE_hRNvReHtbRmpGmfmjd-n8wQ0_-8AlH4YKomTfJMyxibLISeYNXNXsDLKFtJr2ROQi1AyV_lMPBocy820MM3zOBMuJS7Ozm0i_2yQIgrdggtVQ3ej6KW0bSwakIECo4bTImVhyFLC6LC6-JVHXv7kLpStmUEfYcZcpVlGCNZXlwEo5BdDFR5YbGt-CtdXq3bqkIZodtQXxFBWThR-HRC7OaiDBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انبارها برای «تورم صفر» پر شد
🔹
سخنگوی شهرداری تهران: با مجوزهایی که از دولت دریافت شده، واردات مستقیم کالا برای اجرای طرح «تورم صفر» انجام، و انبارها از کالاهای مورد نیاز پر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466757" target="_blank">📅 03:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac33a63d28.mp4?token=a32foYzpNfSF0CqftEBz6LH_keuMvzuiTGdwM7M-hx_JV2KVQCpaeEXK96vGhV0R6Cnq8mDOCEuvDFOMrjDZ1zJneyjyCRos-jXpmGe_zVlZXiVah3pSuiUl9RPK-4zyzL2g1cABAYXdQp2i6X8QVUxzcuowzm5C9FUBWTHftKwu0pez_J3TnpxA2kONetJVuhRjB0P-ELJngB9KEy8UMRCBkfw1YPAx7vskbzmymB0Xg8HMSVjoGqSSpWgmMIUPfriM3OmbM6Bpq4GkRNjkueYmwwBro6apKT_-PRNfKquWRcE0rJxr7sqcJfGiq-7S4yEGV2LlGRTViFpdV9tBplQeASqKQD9H4TVtKNYJA83eWEXUZ9eus0ScqxAkHT6-8Jlx7L9w04oa7v4MZnWkb3-kNrTG2bCZqTR0awwJPUZa4Dtt7SgnR3O5mJZ-Q0084IKYBiSJxGYlY8JRFluM1VtdzM0LuokDmTLMuf7-VjfKCA9THOZI9Vk-rM5vrUOINThTdx9MIG97ucwdogxlSqPeasi5-FKmqnILMgedMaGHyqCf6mosa0Up-kk7VrV6CUsBI3XjCHgx0xc6_eDzGyMllcXoyVly6WXkxW1dQcm-IWZA9PMrHAgu1FtYHupCJzPj1Kxa7eowrvTNqFRhYkm9HkO2AiV5AESR9SkgMr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac33a63d28.mp4?token=a32foYzpNfSF0CqftEBz6LH_keuMvzuiTGdwM7M-hx_JV2KVQCpaeEXK96vGhV0R6Cnq8mDOCEuvDFOMrjDZ1zJneyjyCRos-jXpmGe_zVlZXiVah3pSuiUl9RPK-4zyzL2g1cABAYXdQp2i6X8QVUxzcuowzm5C9FUBWTHftKwu0pez_J3TnpxA2kONetJVuhRjB0P-ELJngB9KEy8UMRCBkfw1YPAx7vskbzmymB0Xg8HMSVjoGqSSpWgmMIUPfriM3OmbM6Bpq4GkRNjkueYmwwBro6apKT_-PRNfKquWRcE0rJxr7sqcJfGiq-7S4yEGV2LlGRTViFpdV9tBplQeASqKQD9H4TVtKNYJA83eWEXUZ9eus0ScqxAkHT6-8Jlx7L9w04oa7v4MZnWkb3-kNrTG2bCZqTR0awwJPUZa4Dtt7SgnR3O5mJZ-Q0084IKYBiSJxGYlY8JRFluM1VtdzM0LuokDmTLMuf7-VjfKCA9THOZI9Vk-rM5vrUOINThTdx9MIG97ucwdogxlSqPeasi5-FKmqnILMgedMaGHyqCf6mosa0Up-kk7VrV6CUsBI3XjCHgx0xc6_eDzGyMllcXoyVly6WXkxW1dQcm-IWZA9PMrHAgu1FtYHupCJzPj1Kxa7eowrvTNqFRhYkm9HkO2AiV5AESR9SkgMr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رمضانی: کارهایی که ترک کردی تا برایت کف بزنند را ترک کن
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466756" target="_blank">📅 03:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfR6krAFYfQ010FPDTcPB9GxA5hxTMaJ0x-Orc5DaBw8MA22IpU80Y5l8eEWrE7a1wf328Snhdwg2IhJlLr0LMEOV9cTiMUJf39bTpipJTVGipFXBfTnwaUQzgZb2hu1ikFlsNCAkM7qk1N42DmnRYc3Wl_84WS51LA9gnclgcnyqdaF9tNTFnmGpra2TXKotMJsAj_UVoxi7ZnQH4bksF6uCo6-YcZo60u0sDifNZK4QSnm6ovm1sHYu80MaR_IO5R6rsJ7RSyC0hIHbjanQcbi8GGLRoQ1HETmGl72yNBbhWoe90nzFwdcepuYQ_vHgIF4MRDgxSwko6_FLA-jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: ایران باید امتیازات هسته‌ای ملموس بدهد
🔹
معاون رئیس‌جمهور تروریست آمریکا بار دیگر خواستار تن‌دادن جمهوری اسلامی ایران به شرط واشنگتن دربارهٔ غنی‌سازی اورانیوم شد.
🔹
ونس مدعی شد که برای پایان دادن به جنگ، ایران باید توانایی غنی‌سازی اورانیوم خود را به شکل ملموسی کاهش دهد.
🔹
او که این بار به‌جای کلمه «توقف» غنی‌سازی، از عبارت «کاهش توانایی» غنی‌سازی استفاده کرد، گفت مشخص نیست ایران چگونه تصمیم خواهد گرفت.
🔹
معاون رئیس‌جمهور تروریست آمریکا ادعا کرد واشنگتن همچنان پذیرای توافق بوده، اما خواستار امتیازات هسته‌ای ملموس از سوی ایران است.
🔹
ونس در ادامۀ یاوه‌گویی‌هایش گفت، اگر ایران می‌خواهد تعهد خود را به عدم ساخت سلاح هسته‌ای نشان دهد، باید کاری معنادار درمورد ظرفیت غنی‌سازی خود انجام دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466755" target="_blank">📅 02:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466754" target="_blank">📅 02:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملات رژیم سعودی به یمن
🔹
رسانه‌های یمنی گزارش دادند که رژیم سعودی در حال هدف قرار دادن استان‌های صنعا، عمران، صعده و الجوف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466753" target="_blank">📅 02:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdOM1moW2iI-z9WrmH5U38jpsDZH-pPDYI3UH5V0GZPmopOst1BDrisuzyaSY7yl4DLQUgTEzhT1WFy3vPjNpTFLzqcBGiapg8BTPy90cOL2fuxgiqFakyK9vCSxs12-NLpR4S7_QQOo0xKAD15e4BszACw_uCoJ3NhL9rTUnt3NjSR8KPuJC3GNc-ZaJlS_RfRUzECBhPdIXj_NSsuHVcrKNERElu0GtwCj6h9MbyhBQkBMyQrQnbkQn9mMtWBLdsItqbvpazOhuX-Xb6X-ZjugOiBAedCGjEpDzw9qgJ_KAmUfahchIK0fF1t1fOyVTFKccDOEgJ6H2kozuBcTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش‌مصنوعی که اطرافیانتان را زیر نظر دارد
🔹
دستیار هوش مصنوعی «میوز» متا قرار است کارهایی مثل ارسال ایمیل، رزرو سفر و مدیریت برخی امور دیجیتال را انجام دهد؛ اما گزارش‌های اخیر نگرانی‌هایی دربارهٔ دامنهٔ اطلاعاتی که این سامانه از کاربران و اطرافیان آن‌ها جمع‌آوری می‌کند، ایجاد کرده است.
🔹
بر اساس بررسی یک پژوهشگر ایمنی هوش مصنوعی، میوز می‌تواند برای افراد حاضر در زندگی کاربر، از اعضای خانواده و دوستان گرفته تا همکاران، اطلاعاتی را جمع‌آوری و به‌روزرسانی کند؛ حتی اگر این افراد خودشان میوز را نصب نکرده باشند.
🔹
نگرانی دیگر به امنیت این عامل مربوط می‌شود. گزارش‌هایی از مشکلات امنیتی در محیط اجرای میوز پیش از عرضه منتشر شده و این پرسش را مطرح کرده است که اگر یک عامل هوش مصنوعی دچار خطا یا نفوذ شود، دامنهٔ دسترسی آن تا کجا خواهد بود.
🔹
مسئلهٔ اصلی دربارهٔ نسل جدید عامل‌های هوش مصنوعی فقط این نیست که «چه چیزهایی می‌دانند»، بلکه این است که با این اطلاعات چه کارهایی می‌توانند انجام دهند؛ موضوعی که می‌تواند تعریف حریم خصوصی در عصر دستیارهای هوشمند را تغییر دهد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466752" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466750">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0a780202.mp4?token=uFtIIwzZ6NirB49FYp_Wb6CL5afgYNg69t8kxY700gEMI2ToMqSF5VBOAL_dOr_vIG6IZu_ZUjgmuPcyvfdl2A7SQGB8ao6PI46dhdSeqfmCHsdn60VQMTD63vvXY_rMAHJs_2OAawxhiereIRQuEKrhtGqqH--cBl5HkaWsViNh9hdatV3BgWmAD3wny5ZBgteUkdP_p3aewrI3S7BJtLvkc6hc5HBggjxE1ej1OIeZKQLNdu5Dipwh5AFkHVSSqNTk6NOX3UHt0KEwrEO2bwBZT4UGkQKxzLULNKHQGBJZuUcnbpVxk-gmvDiNuNQokjnodqRk3SeKRKr7GxJizg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0a780202.mp4?token=uFtIIwzZ6NirB49FYp_Wb6CL5afgYNg69t8kxY700gEMI2ToMqSF5VBOAL_dOr_vIG6IZu_ZUjgmuPcyvfdl2A7SQGB8ao6PI46dhdSeqfmCHsdn60VQMTD63vvXY_rMAHJs_2OAawxhiereIRQuEKrhtGqqH--cBl5HkaWsViNh9hdatV3BgWmAD3wny5ZBgteUkdP_p3aewrI3S7BJtLvkc6hc5HBggjxE1ej1OIeZKQLNdu5Dipwh5AFkHVSSqNTk6NOX3UHt0KEwrEO2bwBZT4UGkQKxzLULNKHQGBJZuUcnbpVxk-gmvDiNuNQokjnodqRk3SeKRKr7GxJizg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار و آتش‌سوزی در دومین پالایشگاه بزرگ ونزوئلا
🔹
منابع محلی از وقوع آتش‌سوزی و انفجار در تأسیسات نفتی «کاردون» خبر دادند. این حادثه دومین پالایشگاه بزرگ ونزوئلا با ظرفیت روزانه ۳۱۰ هزار بشکه را تعطیل کرد.
🔹
به نوشتهٔ رویترز، آتش‌سوزی در یکی از خطوط انتقال گاز متصل به هیدروتریتر دیزل در این تأسیسات آغاز شد و سپس کل تأسیسات را از مدار خارج کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466750" target="_blank">📅 01:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466749">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56e57bd15.mp4?token=o4SMwDFmMGH1PwllBcMRks1nFZnbfydrSaukb5vqWQp1f3L3wGDIIzGiY0qvNkC-qor5cZKskbu0Qw4Y4QYwDEDMBJ-FUhLdxuNjJyO7PXcZFOlFy3PCxb5YRteRM_V3-elqed02eYohOH5RL_qFBkrCdXSFvHVXk_lDnGVFt2dXIX4ALpEC_K1ofK1P6HJJhU5VJ2Ihu0X6_BA_xxqSmroymonzqiJ0rJu6HsQObMh_fXgt3uZzhdW5ohAfaXqCevy0vCHkTbUXXev3T03Ylp_HK1GMJNBHv4hDQ6tcjbWxn2XVSBS2p57-mBvNoCvBQJJImA1A1izHG6eT9JNqLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56e57bd15.mp4?token=o4SMwDFmMGH1PwllBcMRks1nFZnbfydrSaukb5vqWQp1f3L3wGDIIzGiY0qvNkC-qor5cZKskbu0Qw4Y4QYwDEDMBJ-FUhLdxuNjJyO7PXcZFOlFy3PCxb5YRteRM_V3-elqed02eYohOH5RL_qFBkrCdXSFvHVXk_lDnGVFt2dXIX4ALpEC_K1ofK1P6HJJhU5VJ2Ihu0X6_BA_xxqSmroymonzqiJ0rJu6HsQObMh_fXgt3uZzhdW5ohAfaXqCevy0vCHkTbUXXev3T03Ylp_HK1GMJNBHv4hDQ6tcjbWxn2XVSBS2p57-mBvNoCvBQJJImA1A1izHG6eT9JNqLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشن لگویی به‌مناسبت ۷ اکتبر، سالروز عملیات طوفان‌الاقصی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466749" target="_blank">📅 01:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466748">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjd4ExSq9J7FG9lrfIP1F4qkQcBgENCV_Sxfkm1mP7q4gvZYA_gytWQsOqh9a_1foe2rymKriWG71uhXOPHsrIhI1JRIwApcRt3ackE4WQkN-Ol7IXGuPO7bLQadrJcpODIOLc3Z-KZn9J_t8qnb5j1kwEzh9ez6zl3D67UW7z9IsPnsY5xE9REeixku-NUu7b0pT-z81AYupBXlrxQvgpeFwd6T9H0sZSfhczWKAKMMFAcD_sECvRAqzohoJJSqEOuBddS4_K9ZxuA-ZbVRi4RsZ8K61fJO8s4KkLjkPBNXZrO89L3gg9CiRArHIYs3KYTq66kk5Smg3uK_BVDXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین گرا برای جدایی از پرسپولیس
🔹
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از دنیل گرا در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
🔹
در این‌ بین، گرا برای جدایی از پرسپولیس خواهان دریافت ۶۰ درصد…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466748" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466742">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1km7iWG87ARZS4HakIOo92rbtgtdP-JH5fn1_BHas_Di_9e62lYLSY320sPAswTjUOSlDzfKkCuv8xPDATzQE_vyrTGVIPsx3xrEi8vSTt31roA0FLg4oFQJ1kXfObgGG0n9FFJm8zzIfBCngv3o5MX6yaD7HKwO9MgMCQeQI3HcagxuINiBM-UlKsAUsRiewT99gpBayWmnpuSJeaOOyJFRRByGPkVUcITp5oFM257oaJj8BX8njQ2yKuoncjKUpdEhx050UTTpdy_-4KQv-11UrA9E2y3si50NyrUX_d4mc91pHLg9zM3Y8Luli4vbg06QTvlGha1Qh1wGOId6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxXgjtWjNvlDzbR_0QBHb9yIVCEfGtZ0GuoJdc4MpNEWMZ7fqmrLNqMBI4qGizpIz3wjrsk4LkaKZiDYu5Bo88KKpMxbsXxWPll7F14hZlMbKa8lq4Uhm7abJ7BdBFVDaADJjAPIg4nZZiLf0Svxqgjm2HQdqIrKfLFN5ytw_0p3AhaV_Oodud3k77YiIdhySWW5J57WeO6yqZHgiEwLJoIW2PCnoAaXIrnRRCEoDwkD0YnytOe2Vsdang5AUBkax070YR-tFqJy0lE_u3rhnmm1a0TxRK82-9KGoN-QmKMI7bTCRviovdArHqqb5gRX-qUthVNEkYqkRhiflrJJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2c6ALSJGqrcy0gmJOjuJpWywnHvGVgfDbeVt8b8VQZRWh8g218C4k8Ljmmm2dN--feqRKRulzds8LaUeJpcmvREmE-AU4EHrijdkrY6TJ_A7PTfmPH_T1tHs-wa2ORkpgm8o_W2pMyqP6Za6AE4RIAeM_acgargteS-GlyarOXLTc1uAEm9QZpJPbmwXdWSx9LeIwcom0eKEL_P1_QERPIvEdNQUlbXeiIY9wI12HUu3Pi7Yw9gHEV8NdpGlbJCdSSqAHblYd5OAWTYZTuTHuVNaqT4PejM2YdhER69CeyovWc_kf_PjBvISjzOafb__ZxcykekYPmnp303oDoSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNOXYSpTpyyZo_flomOHCBfNNdhvgLM_Nuzl7oAIXCLuRhi1bSPypb0JBcwUizPXLeJfNiIRSwhCwzB9rsE8pPRJh7NnWX6vx9w8SdrjSU8iSye25M1lwflUUZzsACbdkVDW0gtQZFDNdKvz356o2ZbeqlcICppaMFFitHnnIwqMxb0UC_z8SUG9mxDxpVRv2VWj4s63HyYZNE9HkWZlyxWmBI5lSOMpjGqW99MYp7im4cNMlzrdHPNhZL_nKrZb7mFsDCKjfOXKu-yKCswgMySkarSsyOjlxHOoKaj3fnqlo6QBLjO6prqOOZuWpq3fsuqrxEU4HO-uyDrobFxCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmWSOOPhtxlMoLSCZe6AnHqzfiu9jFduwzzxR039X0Fgb0GMjmYfxiHlwFNVZ-y4jSBnlMsaLE1J0uXZXuAsrL_kY-wOX_IB9wSXhoPq5ZWSTKiqFr0UbohosBYdUOflEu4ps04Lg5XHg2Xy1GwkVrut4fZw8BAza5im2EzMmMI_WvriHDjCH2jTQkQ_VYeN5TqYnobkZgen5yg3t-pOiazC1dC5kWNN6hSSnDtnC_dPpSkm8t95M-GYRJEtxobaXD_4Jn0WeLLPe8jAkaADr9MBvrpJinTP6Rm197JKaKhTUhfIk7V_LgkuKeOQ5VtBTn99DNb0U_q2xWWrSvnUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkUpmf3Xb0lrofzVLR937qM0O-HUwNBToey2gS67_c3d1phChJ2GKALW3XZrtRv558jERqJMMFf6adt2oL_Ypn-BznrN4ZtvjdZRgN3DbpDKK1L4K4cIlveu6uAucDUsDRNyVjQTM-0YuYeyxlYv_wrYcg2Z-fSFcTp-cWKOKQB9d8BEQoqFFJwYdN48fL5v6iJI89_WjtQ6jVFbj5uo059B3r3xeQH9-xhOO0vSa6eN3oJVYaFUbZoh7kLpgvSnBqB2Idj-VNOq-km0odWQut6LjtYL4lLR0Rv7cgAifWB99ZR1bhBuFcim9sSInDwBSzxlUs4XWvwg_R04RIw0hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجمع امشب باقرشهر را بانوان اداره کردند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466742" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466741">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
هذیان‌گویی جدید ترامپ: تنگهٔ هرمز متعلق به آمریکاست؛ جایش همان‌جاست و همین الان هم در همان‌جا قرار دارد.  @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/466741" target="_blank">📅 00:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466740">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr1Fp39uD2rseuaNbNEDrnmPx3JFl8L--ZFohqmL54lpXU5Pak1ANr7SEQ3dFVnKLOdOHlXk_BxI-Dz2ycm6gq-yKegsgJMLIcVLt6ozB196FEwt8-tSFP6_kpgcmLIbRYvn6YQgmg4nNz0huwafNyJy6zezDNfxogGX43DTGXag5QuH4EDaecSg1DgJW1oINonc5de6zbCIkqXjhXH8FocDAe9tLt1M8xpPA9XwkzNlJ6G_s9r3PSnwo4EekTZ2oJ8_aJQmGILW85LkBeEdUKKAuq8_GiCz0ZJtboArEMHjihOyKSdqEvXiQ_pLC6M5n5ZYAYM6Lf4GH6268h-8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
از شایعه تا واقعیت خبر عفو امیر تتلو
✅
ویدیویی که از خواهر امیرحسین مقصودلو در دقایق گذشته با موضوع عفو تتلو منتشر شده قدیمی و مربوط به یک سال قبل است.
⚠️
او سال گذشته در همین ایام در یک ویدیو خبر از عفو امیر تتلو داده بود.
@Fals_News</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466740" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466739">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تمساح</div>
  <div class="tg-doc-extra">قسمت آخر</div>
</div>
<a href="https://t.me/farsna/466739" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱ – تمساح</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/466739" target="_blank">📅 00:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466737">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx5F1pN5xuK-o6UnO4gXpRb0nu57N5ZpAP9vVRNtFweRO_n7QWZQSIBdTF408K9bf0jO6Xs-wCjBrqcDJekrCtw_OgMSWTGrG_wNTSwGItgoaVaeZQ5uTdWQ6RS4QpTGV53FgkyNpKl56Ke5H4CIDsToKilrYpujs-mvK-i_2NF_Fkev3bazbjSQaYnDzQJHnp4Kz23hEV3CAxpcWjkBUFWMtwGe5wJ0Qba2Q6jhZQfg3BBFBdWqSVv-ywRt7MwUODTZ0ws30dOzuVx8s2dGlIXObcO4DGuA-sst5WTepBseJtUGbE22N9KTVHDuRyabg9yfX4hYrLXWCvhP8Lqfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خری که نه گوش داشت و نه دل!
🔹
شیری بیمار شد و طبیبان گفتند درمانش فقط خوردن «گوش و دل خر» است. روباهی که در خدمت او بود، یک خر را با وعدهٔ مرغزاری سرسبز و جفتی زیبا فریب داد و به بیشه آورد.
🔹
شیر به‌دلیل ناتوانی نتوانست در حملهٔ اول خر را از پا بیندازد و خر گریخت.
🔹
روباه دوباره به سراغ خر رفت و با ادعای اینکه آن حیوانِ جهنده فقط از سرِ شوق می‌خواست تو را در آغوش بگیرد، او را خام کرد و برگرداند.
🔹
این‌بار شیر خر را کشت و برای تمیزکردن خودش کنار چشمه رفت. در غیاب شیر، روباه دل و گوش خر را خورد.
🔹
وقتی شیر بازگشت و سراغ سهمش را گرفت، روباه گفت: «اگر این حیوان ذره‌ای گوش شنوا و دلی فهمیده داشت، بعد از یک‌بار گریختن از چنگال مرگ، هرگز با پای خودش بازنمی‌گشت؛ پس از اول هم گوش و دلی نداشت!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466737" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8daec564f0.mp4?token=oR_FNoqkDTVkG4lUDHo6V_EC7b_7ENVl0FoaE67F4ihI23Keh_irlq_XEJwMrjnS1KI5B9c0k9lRnIi9eEO7Dd-xjtyUdEMcyGnfmaIopNX_IbMo65DvJYlV0-at2Zg9zjZ8vOFGu5SiWyWv_uRwqOMKLYcLn9gZf8U3nFbb-_m6mrIlE2vxMi6jLKEGGn43JmZOQnNcP1TZ-Gq1dHrQCuJ8prV_IW8q1rfPIPK_y00_0gQIA_1yfGKF7PSrMhQz9gLMlVA-IFnETpxJJQJduVqfXnXkzhhvOIb1VHMBWqfZVd6hPojnEm3nb6v1ZGIk-MeJPI0aR8D_Ue2i__Ippg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8daec564f0.mp4?token=oR_FNoqkDTVkG4lUDHo6V_EC7b_7ENVl0FoaE67F4ihI23Keh_irlq_XEJwMrjnS1KI5B9c0k9lRnIi9eEO7Dd-xjtyUdEMcyGnfmaIopNX_IbMo65DvJYlV0-at2Zg9zjZ8vOFGu5SiWyWv_uRwqOMKLYcLn9gZf8U3nFbb-_m6mrIlE2vxMi6jLKEGGn43JmZOQnNcP1TZ-Gq1dHrQCuJ8prV_IW8q1rfPIPK_y00_0gQIA_1yfGKF7PSrMhQz9gLMlVA-IFnETpxJJQJduVqfXnXkzhhvOIb1VHMBWqfZVd6hPojnEm3nb6v1ZGIk-MeJPI0aR8D_Ue2i__Ippg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هذیان‌گویی جدید ترامپ: تنگهٔ هرمز متعلق به آمریکاست؛ جایش همان‌جاست و همین الان هم در همان‌جا قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466736" target="_blank">📅 00:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET7jAvdCV82QS0VkoURt5h5rj2CLC9bZrMbuOx9-FWCRPMylvqMe7jp4IPHn4cBct1v17FLWz1jl499qETwLA_0vn4diWU_ZaVJlbLXqWvEZm4voQ81iRiigHqCPcHO_w-gvYHLN-mzVqpk5zRqeCqbr-QUs3HQSehZmM3ficXXAPnkGP87vq-wIfXUdAuZMJtYrn7gVbbDQRFbxenB91ItZZfWutOKQiyXGjSKc9SsQpoomgGD7PdonHEoWsIrAH1R34eHtTet3QNEKkgqIht9-YGfTcXqXRknj-pfhz5O6Xu-lgr_cJxydX-9_kSz2b2Bvrb7owaOWL7yPiy06vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت عجیب مسجد مکی در مقابل جنایات گروه‌های تروریستی تجزیه‌طلب
🔹
زخمی‌شدن یک نوجوان ۱۵ ساله بلوچ در یکی از حملات تروریستی و سکوت برخی خواص و چهره‌های مذهبی جنوب‌شرق کشور در قبال این موضوع، انتقاداتی را به دنبال داشته است.
🔹
منتقدان می‌پرسند چرا صدای محکومیت این حملات تروریستی توسط برخی از خواص سیستان و بلوچستان شنیده نمی‌شود؟
🔹
مرتضی سیمیاری کارشناس مسائل سیاسی می‌گوید: هنوز موضعی ازسوی مولوی عبدالحمید و تریبون مسجد مکی در محکومیت اقدام تروریستی اخیر در منطقه مشاهده نشده است.
🔹
زمانی که گروه‌های مسلح تروریستی، امنیت مردم و نیروهای امنیتی را هدف قرار می‌دهند، سکوت یا اظهارات مبهم می‌تواند از سوی جامعه به‌عنوان نداشتن «مرزبندی روشن با تروریسم» برداشت شود.
🔹
انتظار می‌رود خواص مذهبی و اجتماعی با مواضع روشن علیه تروریسم، اجازه ندهند خون مردم و حافظان امنیت دستمایه پروژه‌های ناامن‌سازی قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466734" target="_blank">📅 00:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">دو شناور جنگی مهم آمریکا منطقه را ترک کردند
🔹
شبکه فاکس‌نیوز گزارش داد دو فروند از تجهیزات و شناورهای مهم نظامی آمریکا که در خاورمیانه مستقر بودند، این منطقه را ترک کرده‌اند.
🔸
ناو هواپیمابر
«یو‌اس‌اس جورج اچ. دبلیو. بوش» (USS George H.W. Bush)
که از ماه فروردین در خاورمیانه مستقر بود به همراه ناوشکن موشک‌انداز «یواس‌اس دلبرت دی» که از ابتدای سال جاری در منطقه حضور داشت به سمت تایلند رفته‌اند.
🔹
طبق گزارش فاکس‌نیوز در حال حاضر، ناو هواپیمابر
«یو‌اس‌اس جورج واشنگتن
» تنها ناو هواپیمابر آمریکایی باقی‌مانده در خاورمیانه است.
🔸
این ناو هم‌اکنون در دریای عرب قرار دارد و در ماه اوت وارد منطقه شد تا جایگزین ناو هواپیمابر
«یو‌اس‌اس آبراهام لینکلن»
شود؛ ناوی که قرار است این هفته به بندر خانگی خود در سن‌دیگو بازگردد.
🔹
در مجموع، در حال حاضر حدود
۱۷ شناور نظامی آمریکایی
در خاورمیانه حضور دارند. این رقم اندکی کمتر از تعداد شناورهایی است که از روزهای منتهی به آغاز جنگ با ایران در هشت ماه گذشته در منطقه مستقر بوده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466733" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پرواز تهران-تبریز قشم‌ایر به‌دلیل شرایط جوی به مهرآباد بازگشت
🔹
این پرواز با یک فروند هواپیمای فوکر F100 در مسیر تهران به تبریز درحال انجام بود که به دلیل شرایط نامساعد جوی، کاهش دید افقی و رعدوبرق، امکان فرود در فرودگاه تبریز برایش فراهم نشد و به مهرآباد بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466732" target="_blank">📅 23:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec1106eb2d.mp4?token=ZNV4w6siAWYzTkp-X8sh3GtSd9ZoVGGLOkEutlQunNr-09hVw1N2cXDAYAZmVPxpjvLPMb-er7pDpEo1wkziq-J9K5VmZ7vGoybsc4no5zpLtPc0wnbNBGIQ4sAAFjNZCZt683VdSpbb5M0Ht_Z0UIeEo5bv_fFQDMsRRW6A_rH2L-bT-7V48ndPVf3fPHV1g-9_xVEKn0veVk4HaiyWef-9GMaRCWmbngMpK4CgySkhJ2qcr0nQMWN2eg4FrhMSUDBv6fezTVTGWjGAMO3E4ENKgrvsagQ8-WbDRjWoUjrqJ2Gq2VRsblgd46Q-7mY3ikNgAZ-odMyyEW_h8d8WaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec1106eb2d.mp4?token=ZNV4w6siAWYzTkp-X8sh3GtSd9ZoVGGLOkEutlQunNr-09hVw1N2cXDAYAZmVPxpjvLPMb-er7pDpEo1wkziq-J9K5VmZ7vGoybsc4no5zpLtPc0wnbNBGIQ4sAAFjNZCZt683VdSpbb5M0Ht_Z0UIeEo5bv_fFQDMsRRW6A_rH2L-bT-7V48ndPVf3fPHV1g-9_xVEKn0veVk4HaiyWef-9GMaRCWmbngMpK4CgySkhJ2qcr0nQMWN2eg4FrhMSUDBv6fezTVTGWjGAMO3E4ENKgrvsagQ8-WbDRjWoUjrqJ2Gq2VRsblgd46Q-7mY3ikNgAZ-odMyyEW_h8d8WaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرکرد پای کارزار؛ «جنگ هنوز ادامه دارد»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466731" target="_blank">📅 23:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36dc1e1bf3.mp4?token=foeQi1pTP82heGc5yaHTu2gx0t91uI0EE8cqLLGEEWCY2iQ8tlSQAEjkr8ONbresvg4Pnxt6LVph5Y6JXFs9OnwXabJMqLWdTA-oF5eYMAqun1OqBp6AMWw2j3vD9_6aumZvNmp74ZX09Jv3EsjXMD7PoddhYo3oDErqtiWtRN_PZmk99nJMkzCH_1gCvQ69VKMEA4XcWo4LYiY7ilKRQSFnWYQ18IFyWd6M16esui4gFfhhi5aWy7N3A6cRjyZZIl_OtB59qRbGyIoKvGxel9mRO4AlZ0x0YSS4Q48xCZHQBGA7PlXwh4SRRzJ-JnfyfWzyGyN0s44HlurfAJjGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36dc1e1bf3.mp4?token=foeQi1pTP82heGc5yaHTu2gx0t91uI0EE8cqLLGEEWCY2iQ8tlSQAEjkr8ONbresvg4Pnxt6LVph5Y6JXFs9OnwXabJMqLWdTA-oF5eYMAqun1OqBp6AMWw2j3vD9_6aumZvNmp74ZX09Jv3EsjXMD7PoddhYo3oDErqtiWtRN_PZmk99nJMkzCH_1gCvQ69VKMEA4XcWo4LYiY7ilKRQSFnWYQ18IFyWd6M16esui4gFfhhi5aWy7N3A6cRjyZZIl_OtB59qRbGyIoKvGxel9mRO4AlZ0x0YSS4Q48xCZHQBGA7PlXwh4SRRzJ-JnfyfWzyGyN0s44HlurfAJjGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دوگانۀ اینترنشنال؛ از پلیس تهران تا پلیس پاریس
🔹
اینترنشنال که همواره با تخریب پلیس و نیروهای امنیتی ایران، هرگونه حضور آن‌ها رامساوی ترس، اضطراب و تجاوز به حریم افراد می‌خواند، این‌بار حضور گسترده و برخوردهای وحشیانۀ نیروهای امنیتی در مدارس فرانسه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/466730" target="_blank">📅 23:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e6463543.mp4?token=D4jgiCn0SSs31t0SGvYx8tFWW830XzbcUvYUgE189wm3HVQ2WvDI2qVyyt6JkjjORgblXM4KcfHnJ76kKIytRY10pViiuxjmGLhFHt74CJuUhQFl-a36hPjr_3tLKepVYqqplpAtQGyJAi06D3KtE9k8sQu1XuHWU6k9inD0ZUegTm3sOyZIFDMa3Abl7SmxSfF8VcodwJLJnuFNkh5fE6N485noJ-bu_IqTi3AfU-s1He_sXuFCx8jM1BgkrXohiwE5X9lss8EDeKacocFPfNt1QGNeO2nXv_R2BfQPMFQiJnnoFbbLZku5fM0hkmkZlYeILToM8dmNkf8mAv--xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e6463543.mp4?token=D4jgiCn0SSs31t0SGvYx8tFWW830XzbcUvYUgE189wm3HVQ2WvDI2qVyyt6JkjjORgblXM4KcfHnJ76kKIytRY10pViiuxjmGLhFHt74CJuUhQFl-a36hPjr_3tLKepVYqqplpAtQGyJAi06D3KtE9k8sQu1XuHWU6k9inD0ZUegTm3sOyZIFDMa3Abl7SmxSfF8VcodwJLJnuFNkh5fE6N485noJ-bu_IqTi3AfU-s1He_sXuFCx8jM1BgkrXohiwE5X9lss8EDeKacocFPfNt1QGNeO2nXv_R2BfQPMFQiJnnoFbbLZku5fM0hkmkZlYeILToM8dmNkf8mAv--xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک‌ها باید از بنگاه‌داری دست بردارند و املاک غیربانکی خود را واگذار کنند
🔹
سامانه ثبت اموال و املاک بانک‌ها ایجاد شده و بانک‌‌ها باید اموال غیربانکی خود را با ۸۵ درصد قیمت به صندوق بانک مرکزی واگذار کنند.
🔹
اگر تعلل کنند و خودشان اموالشان را واگذار…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466729" target="_blank">📅 22:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Yx5VlklwDLhwuQTAXaw6Zubn8S1WhfuJiOW6cNI8sJ-BG228QbIgP-tueQp33jZcHfB-cZMDA0tz4AiZYo7gfsXfuzPexdQjQf2zFUTwUrGum9fTJcedfeiO6AeguyABYJVntsSEBzxUeNMuJa8BRFC4bwn4GxaqilewbkcGXMY1RcRDv6cCbFwkE4BS-ifTxj6hY_V1cjqDcPZ0ogTWC_AIwqdryfuEi50GJ_clyJ2pRhXZOYSBVgZ0BJFaQjpWYBnxX4b9I3tXsZQX29JZwMJWDe8pfgaFgGM9ZY_hiRJhEDh5Hr_o4vjqmvyFPtL74aMIAenhB1G7FCwX_mtozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b034b2d.mp4?token=Yx5VlklwDLhwuQTAXaw6Zubn8S1WhfuJiOW6cNI8sJ-BG228QbIgP-tueQp33jZcHfB-cZMDA0tz4AiZYo7gfsXfuzPexdQjQf2zFUTwUrGum9fTJcedfeiO6AeguyABYJVntsSEBzxUeNMuJa8BRFC4bwn4GxaqilewbkcGXMY1RcRDv6cCbFwkE4BS-ifTxj6hY_V1cjqDcPZ0ogTWC_AIwqdryfuEi50GJ_clyJ2pRhXZOYSBVgZ0BJFaQjpWYBnxX4b9I3tXsZQX29JZwMJWDe8pfgaFgGM9ZY_hiRJhEDh5Hr_o4vjqmvyFPtL74aMIAenhB1G7FCwX_mtozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بانک‌ها سهم زیادی در تولید تورم دارند
🔹
نکته اینجاست که ما نمی‌توانیم تمام بانک‌های متخلف و ناتراز را باهم منحل کنیم زیرا باعث التهاب و هجوم بانکی می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/466728" target="_blank">📅 22:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581638275d.mp4?token=DhaIMp4eAAApP5g530jplGKqhqebsJ9NOY8r3XkF5Eyrg3dFFOuRdZWJQvCUiR4OGT_zXQXvq7W9395b_GX3_jL3R6Kw_hz5KtNFU7s9Qc5iNlydcQZsv7DI_XNTl7TJCeBYKYrA7vjyPYTuePkn_UEufclDVWPy0Xa4tYobvthglOAdwjXz6_K9eZFlD6Y-CNVJUdUMPjNxFLJmaa6TyJVbd5fGB4z6NeTnyAwcC4RTN58luSu8sp8hc_8jA0qdptxGpMf5iYRHEuaa8el_eFiTTPOY_WxPD0oQnE8G_85ZEeMhvlrcxij1nD_Ek9_RbgmbSTVbXLj_r7NhPq5x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581638275d.mp4?token=DhaIMp4eAAApP5g530jplGKqhqebsJ9NOY8r3XkF5Eyrg3dFFOuRdZWJQvCUiR4OGT_zXQXvq7W9395b_GX3_jL3R6Kw_hz5KtNFU7s9Qc5iNlydcQZsv7DI_XNTl7TJCeBYKYrA7vjyPYTuePkn_UEufclDVWPy0Xa4tYobvthglOAdwjXz6_K9eZFlD6Y-CNVJUdUMPjNxFLJmaa6TyJVbd5fGB4z6NeTnyAwcC4RTN58luSu8sp8hc_8jA0qdptxGpMf5iYRHEuaa8el_eFiTTPOY_WxPD0oQnE8G_85ZEeMhvlrcxij1nD_Ek9_RbgmbSTVbXLj_r7NhPq5x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466727" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcscpaCoxHV1v0CRXiwQFwubDq84MJeKwkfzEHuvgaIqYyn6opqdiXRrYnA356VBgngHm9UST9jF8ADLXOJUUq36pENgtuWTf9CaxRN5LjOQ66tYdLaAwyWq2pGCP6UckOYT4ckdWiAF8keTkKqMOKe9zG2zl21IJ6QjsZBaVXV1AlwdOhmH2bUTPA_LpZz2mcX0aG0jnZ7hZNGeHZ7MiecvIqNRreDLEMkzbPhqve9z3joXyEZ5rX62n_p4xc-eZDNiPhIH5fAZ4Q_HhWZ3IsTTjWAplm9RnTVGW2D-URohMW3UgbgDzdLXECrMq1ang3V0nADv0mAwPW9putLhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساقدوشی سلبریتی‌ها برای یک قاتل وحشی
🔹
برخی سلبریتی‌ها با انتشار مطالبی در صفحات خود، به حمایت از علیرضا سپاهی، قاتل جنایتکار میدان علیخانی اصفهان پرداختند.
🔹
«مهشاد و علیرضای عزیز پیوندتان مبارک.» این متنی است که حامد بهداد به تازگی در صفحه شخصی خود منتشر کرده است. شاید تصور کنید که او این متن را در واکنش به ازدواج یکی از بستگان نزدیکانش به اشتراک گذاشته است اما این‌طور نیست.
🔹
استوری بهداد هم، پیام تبریکی برای علیرضا سپاهی، قاتل قسی‌القلب میدان علیخانی اصفهان است؛ آن هم برای خبر کذبی که روی خروجی رسانه‌های معاند قرار گرفت و از ازدواج علیرضا سپاهی معدوم با زنی به نام مهشاد در زندان حکایت داشت.
🔸
علیرضا سپاهی به عنوان یکی از عناصر اصلی جنایت در اصفهان، یک مامور امنیت را از موتور پیاده کرد، بعد چاقویش را در کتف او فرو برد؛ او را وحشیانه روی زمین کشید و بعد، لباس‌هایش را از تن درآورد، در همان اثنا، همسر مامور امنیت که ازقضا باردار هم بود، با شوهرش تماس گرفت، علیرضا سپاهی تلفن مامور را جواب داد و گفت داریم همسرت را سلاخی می‌کنیم.
🔸
این پایان ماجرا نبود، علیرضا سپاهی بطری بنزینی که همراه داشت را روی مامور مجروح ریخت، فندکی زد و آن شهید را زنده زنده سوزاند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466726" target="_blank">📅 22:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9e04075e.mp4?token=qqe_5AUBdCe9kQOIJ8QPAxRrKxbnn3WIPhBWii2W1seMiz2AIURvfX0_vokPVX7do1Wu0wqtOrgbKEev-IrFkqFafN_gxOhCG1YigNUpS5xoWfZXA-wgEKgd2kdfOwq7oG0y6eSt-hnMkLKAJmCWGUicoQWJ4BE7oHErUXjYOe4kC51xvwyN4w5Uu6AVZbIVZZKVmT21zciERgxP3N9VE9f-taIJ8nRoeai7WK3nkfv90f9zgmST2ra3TMDDdamIsYxEz3KjloXGhR3VkPCoJpl9bagOS1KL7BOqOWs4h8vtIkRiIXVM1EbQhGavv_pEsVmNLH3ovq68g5E0amq2ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9e04075e.mp4?token=qqe_5AUBdCe9kQOIJ8QPAxRrKxbnn3WIPhBWii2W1seMiz2AIURvfX0_vokPVX7do1Wu0wqtOrgbKEev-IrFkqFafN_gxOhCG1YigNUpS5xoWfZXA-wgEKgd2kdfOwq7oG0y6eSt-hnMkLKAJmCWGUicoQWJ4BE7oHErUXjYOe4kC51xvwyN4w5Uu6AVZbIVZZKVmT21zciERgxP3N9VE9f-taIJ8nRoeai7WK3nkfv90f9zgmST2ra3TMDDdamIsYxEz3KjloXGhR3VkPCoJpl9bagOS1KL7BOqOWs4h8vtIkRiIXVM1EbQhGavv_pEsVmNLH3ovq68g5E0amq2ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: به رهبر انقلاب پیام دادیم که خیال شما از تامین کالاهای اساسی برای مردم راحت باشد  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466725" target="_blank">📅 22:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8807350c2b.mp4?token=UHnr2V8Avzkh3S8oNhAhVnMnAHiFkqMwTJOh_vDC21MIC5RyqpYSWL24dLVtKByDfBdrsy_Zk51TGfRCXovMcCmVbsK6kA0VxCXz1ySaANABHH9e0QL9oY7PbGyXftiRDijg9b6ZlUMXLM0CHJfTG7zs7umc-j-KP1uTNlYBSOOE0bACn3QMqQ-y6vfQEaIqc1rym32mlkLowmpYJ4Jby8tuwuuKLqSlSsu6SzrRLqIN4aqTdP2DSwJgQS_BIPkEJP9boyqmFOi6F0mTYJATYir_fB6QBGmTyuQtZhrgN4DmCP4wGY_zPx7lg1Lg8Ygx8Zuf25aneHvaaQ56eoc36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8807350c2b.mp4?token=UHnr2V8Avzkh3S8oNhAhVnMnAHiFkqMwTJOh_vDC21MIC5RyqpYSWL24dLVtKByDfBdrsy_Zk51TGfRCXovMcCmVbsK6kA0VxCXz1ySaANABHH9e0QL9oY7PbGyXftiRDijg9b6ZlUMXLM0CHJfTG7zs7umc-j-KP1uTNlYBSOOE0bACn3QMqQ-y6vfQEaIqc1rym32mlkLowmpYJ4Jby8tuwuuKLqSlSsu6SzrRLqIN4aqTdP2DSwJgQS_BIPkEJP9boyqmFOi6F0mTYJATYir_fB6QBGmTyuQtZhrgN4DmCP4wGY_zPx7lg1Lg8Ygx8Zuf25aneHvaaQ56eoc36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: مردم مطمئن باشند ما برای اقتصاد کشور برنامه داریم
🔹
بانک مرکزی در مقابل سناریوهایی که دشمن علیه اقتصاد ما به‌کار می‌گیرد توابع واکنش دارد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466724" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbac7b4685.mp4?token=ZFt3yG5Z8QbUbrI1SM4R1AsOlSJXCpKWaGIhmctug1--p7LR88r5lwdml4ZRoTl3qW0DStrBx4hKZFHuNLFR4CTcutYJAyZ13YVq-si97xu9UNhkBnYKuzsKLOBCpq69DFlKqVlDgqzMc8UFDIZjZ7uarNdzF_hBDn6tTTUrH5Rhty2Vy52ynKoliBxu8qb921hN-2OlV0GQHWzXXdJM9gxAWrWMFuARdKj3BRZ8U3NV1IRJcTJf4TYYBIGg-CdDgB1MEzH1S8JFs4gpdpmZ6dGY83iu99PVUJpU2S2bY5A2G3ObdvkP90eIO32_-FnURqh1SwcoujqT5eyw1cDMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbac7b4685.mp4?token=ZFt3yG5Z8QbUbrI1SM4R1AsOlSJXCpKWaGIhmctug1--p7LR88r5lwdml4ZRoTl3qW0DStrBx4hKZFHuNLFR4CTcutYJAyZ13YVq-si97xu9UNhkBnYKuzsKLOBCpq69DFlKqVlDgqzMc8UFDIZjZ7uarNdzF_hBDn6tTTUrH5Rhty2Vy52ynKoliBxu8qb921hN-2OlV0GQHWzXXdJM9gxAWrWMFuARdKj3BRZ8U3NV1IRJcTJf4TYYBIGg-CdDgB1MEzH1S8JFs4gpdpmZ6dGY83iu99PVUJpU2S2bY5A2G3ObdvkP90eIO32_-FnURqh1SwcoujqT5eyw1cDMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: رشد نقدینگی در نیمۀ نخست سال کاهش یافت
🔹
رشد نقدینگی ماه شهریور تنها ۱.۳ درصد بوده است. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466723" target="_blank">📅 22:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ec0eb94d.mp4?token=Qvh5S6bdaot0B-QBW3toBOCniJ7td3Op2vYx67Zrq0B2tsZABQ1Kmvmm6vUqp0rDL_bLfGPysIf7z6vSmxl2PtY1fUT-0UDSA0yjSsUkdXILFn4xIaSegvP1ztKjbtxmiQKaKkTb8RDcEiPTYCcQ6qp69gFcJpiQEv9N9VY4tUXRIfWkDev2Fuukyx2cJRH-6aMtrr4LeWoa5gfk6WLwgc6u2Pv8nYXrfug0W-pBFsP2ZZ3F6L0eXOJ-iXB_kj1olGjV5myITa3xMi0eaujNefk42l4SILrrqiWhXQoRzJqJrJ4_YDTJyIiXRr0ouSOsd6cOt7EIQ7khg_QN29j-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ec0eb94d.mp4?token=Qvh5S6bdaot0B-QBW3toBOCniJ7td3Op2vYx67Zrq0B2tsZABQ1Kmvmm6vUqp0rDL_bLfGPysIf7z6vSmxl2PtY1fUT-0UDSA0yjSsUkdXILFn4xIaSegvP1ztKjbtxmiQKaKkTb8RDcEiPTYCcQ6qp69gFcJpiQEv9N9VY4tUXRIfWkDev2Fuukyx2cJRH-6aMtrr4LeWoa5gfk6WLwgc6u2Pv8nYXrfug0W-pBFsP2ZZ3F6L0eXOJ-iXB_kj1olGjV5myITa3xMi0eaujNefk42l4SILrrqiWhXQoRzJqJrJ4_YDTJyIiXRr0ouSOsd6cOt7EIQ7khg_QN29j-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: رشد نقدینگی در نیمۀ نخست سال کاهش یافت
🔹
رشد نقدینگی ماه شهریور تنها ۱.۳ درصد بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466722" target="_blank">📅 22:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pacjebBEdvUmxPnaVVuXxphNITv88_uqiwCiHYf2NilsqkUuFNlZnrrmWz4CocayEr1sv4b1edB-Ext2ObiVZWdvIIFjAFcW8GU1ovJjVkIOjXENDpgpshiw7jqz_xbJnuxbAvdYIgVDFQ1IWD5fqKm29PF30CpLRZ40d4Z3E0Hb-C-QM4q3bHivlx9Y3AL-16CjUy2ZkYaisBpBiH5uiIy5C7x9IrCnXfUAlLjAcXGkHHzH19PYyF0_pqNDZXXwkcf3A09-ZHHaeKYrgN8FsZh5etnjYAnPUT-AhpA9af5jb2tR_6VEF3r-vvRAVFYhLmj0zt4DWfYf3At-jOFARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب کج آقای مدیر در هفته فرهنگی پایتخت
🔹️
انتشار تصویر یک زن بدون حجاب در صفحه عبدالرضا چراغعلی سرپرست مرکز امور اجتماعی استانداری تهران، آن‌هم در آستانه «هفته فرهنگی تهران»، تناقض آشکار عملکرد یک مقام ارشد با برنامه‌ریزی‌ های فرهنگی و اجتماعی را به نمایش گذاشته و موجی از انتقادات را درباره رویکرد دوگانه مدیران دولتی را به راه انداخته است.
🔹️
این اقدام دقیقاً در مقطعی رخ داده که مساله حجاب به یکی از دغدغه‌های مردم بدل شده است، مخابره چنین قابی از خروجی عالی‌ترین مقام اجتماعی استانداری تهران، این پیام مخرب را القا کرده که در درون ساختار اجرایی، مدیرانی با نگاه و استانداردهایی کاملاً در تضاد با گفتمان انقلاب اسلامی بر کرسی‌های حساس تکیه زده‌اند.
متن کامل خبر را
اینجا
بخوانید
@TehranFarsnews</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466721" target="_blank">📅 22:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhgC_A-kaaFOqBQPEysuQ2WFiWcUvIir-TzKuMTS1fiIMPFR4hoR8_dIVHrXAyP_WcTngx9HQtbx3n9VIpSS80gZOFxzWBORm9OByXu-8RlA-teavZjKU7624asnmTa9bXAF0W5xr16alaa6TRHWZuBpB36l2YAsmPnUxgDQWQj6jZwrAPv9oR3iyz63WuGG2aKkQfpwb8Ts7ojBHivggwHyIdqS8WLObcifQuUY8ebWmPv9ErtLa-UMGy-9UZCkXb5wtBjhTm7IBQZCYXwdpMgDRgkMzfFpV3lLFEqLoc5U9PmgwrMFf71KL_phtJREsmsElELGz7NMph4P8HzxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روی هم، اندازه ایران نیستند!  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466720" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hkEy3Xjazhk6PARhy8qnkkrxlfg5DA-eRGzhQE4-T1giDPcNX05oxfeWknShkIcMBtWRdWCwY6KdwPAWbVeiYX1588sN6jRJALYx4Dg_UbkfZ9FwGpEyptKbwELssT6SZb1bDeEWgmgmzf7KuU6WyuBTHy3a1As7wVY3O6WK4kDsX4i_xkxwAej3y1CdYp83r_F_4otTwlsrpSTx6xztQiyjm15v_8iY7OorQseKd5WstKAa5JkpSAYK-e7iK-4Odu_zYrhPjxVZQpddsJ-OQTeKJnZza7EKVRTURIseUHoW_t3v5C3FlBw3qBeVWrUSCKCqWvmjISiCgmNYc57CZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hkEy3Xjazhk6PARhy8qnkkrxlfg5DA-eRGzhQE4-T1giDPcNX05oxfeWknShkIcMBtWRdWCwY6KdwPAWbVeiYX1588sN6jRJALYx4Dg_UbkfZ9FwGpEyptKbwELssT6SZb1bDeEWgmgmzf7KuU6WyuBTHy3a1As7wVY3O6WK4kDsX4i_xkxwAej3y1CdYp83r_F_4otTwlsrpSTx6xztQiyjm15v_8iY7OorQseKd5WstKAa5JkpSAYK-e7iK-4Odu_zYrhPjxVZQpddsJ-OQTeKJnZza7EKVRTURIseUHoW_t3v5C3FlBw3qBeVWrUSCKCqWvmjISiCgmNYc57CZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466719" target="_blank">📅 22:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56020e833f.mp4?token=s0c35VAfc3UiwvgAcgkvyll0xo1amUooJCwRDUofkzr2XmFwvs9tMpqM2JTfw2xU0K0ZXoEOlWcNynm_GFxeFI9iVxzH6UioiFcbJKtE6NMFfQI3dvSpLzRBQKljgefndJijngYpXHdKBD0K8hlZmSDIsViIUeiesHVknWn3_0EP2LEi0e2lfi6gBp6tgIKKbXYpqXhpvux9kCl-UGoZJRMtzyFCD1BpoBrqx6-0nhOy3Jl0NOeTFAn0P0VSH_AUyuFAOQEpeV-6UWKYpHtik4f-pWXpuzEHpWAeKbSPgU4N4wSBDa8I9JkguRr5ZdnCCmPMYcpf8hfxSVC7X4YA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56020e833f.mp4?token=s0c35VAfc3UiwvgAcgkvyll0xo1amUooJCwRDUofkzr2XmFwvs9tMpqM2JTfw2xU0K0ZXoEOlWcNynm_GFxeFI9iVxzH6UioiFcbJKtE6NMFfQI3dvSpLzRBQKljgefndJijngYpXHdKBD0K8hlZmSDIsViIUeiesHVknWn3_0EP2LEi0e2lfi6gBp6tgIKKbXYpqXhpvux9kCl-UGoZJRMtzyFCD1BpoBrqx6-0nhOy3Jl0NOeTFAn0P0VSH_AUyuFAOQEpeV-6UWKYpHtik4f-pWXpuzEHpWAeKbSPgU4N4wSBDa8I9JkguRr5ZdnCCmPMYcpf8hfxSVC7X4YA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت آرژانتینی‌ها برای خداحافظی با مسی
⚽️
لیونل مسی بامداد فردا آخرین بازی خود با پیراهن آرژانتین را مقابل بنین انجام خواهد داد و پس‌از آن برای همیشه از فوتبال ملی خداحافظی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466718" target="_blank">📅 22:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdWLA_7ClEg3cv2Y852aZF5051526WckwKuAG0CaL3G-9pgsbmoZQ36hMNhIBoI_cNkbJ7sXqMbEJatzC3binceQ6S7Xajs7xiGptR4MjPjkQreRJHmRuV7cLDnIZU5iy3Wi71s6mW5P88xvKud0jXB7fKLEp3iUXD7j2jtJWmDAKOspPRP4iO_zNjjfrTr2ErLXO0TqlMXnk2EA7Czysh-gZB4SVpxrliEeae9z40hiEUAKjYrSjArugHfE2meT8IRN-7Pc_iRxHcDakVnfOfPPM9GTEcCwa1rJ5hhrMrckNcctHyNOQy8Nw2N6ILNdNGYONkEfFGo1TnT-ENi0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: شبح وحشت در انتظار اقتصاد امریکاست
🔹
قالیباف در واکنش به اظهارات وزیر خزانه‌داری آمریکا، با انتشار یک میم اقتصادی نوشت: «آماده‌ای تا روح تو را تسخیر کند؟»
🔹
در این تصویر، نمودارهایی از قیمت نفت و گازوئیل تا اعتماد مصرف‌کنندگان و توان خرید مسکن، کنار هم شکل یک شبح را ساخته‌اند؛ با این کنایه که برای ترسیدن، لازم نیست منتظر هالووین بمانید؛ گاهی کافی است صفحه اقتصاد را باز کنید!
🔹
در تصویر دیوید زرووس، مشاور ویژه جدید بسنت و حامی کاهش نرخ بهره، دیده می‌شود؛ همان کسی که گفته بود تا فدرال‌رزرو نرخ بهره را پایین نیاورد، موهایش را کوتاه نمی‌کند!
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466717" target="_blank">📅 21:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466715">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyAN_JuY8S6mTI2VDpzoWxuK1v7sVF-XB2feBRLu2swcEVxMC-0t2e9m7Ge0YDJDFUT22MxdmvBm8opc08uGFcSf6v9ClMIkImaVjA0iSKH2ziirNyhkwv-fSG0_sk-TmLHRMNoV3aZ1_coBVCwODgbyPgVtC0llINpZXe7_bpH_aZA0YTKnKMGuc5mvPPTC71D5lLmoCkpe1Jx0J3RUum9xIcZA3yBqRbtycF6uNuIatMZeQtGMT-eJugqb32X8tzFRxCVjDeSZxNbvSOG_E9mAkiFiq8B0B05g6gLt_X7hNzcai05CtZWVZebXMupHIVZ9KcjR2XB0jqp3bip7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنهان‌کاری جنگی آمریکا؛ وزارت جنگ آمریکا کریس مورفی را به العدید راه نداد
🔹
کریس مورفی، سناتور دموکرات آمریکایی گفت وزارت دفاع آمریکا در جریان سفرش به خاورمیانه مانع دسترسی او به یکی از پایگاه‌های مهم نظامی آمریکا در قطر شده است.
🔹
او این اقدام را بخشی از…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466715" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/allfikjMlIEqBc3cClMDxNIZoh01qqGzEdf6fCBqGfxNrWeAtFd4FZfE-2dSIZPDsYunFiB8C0MDE74mUpn8jR49UBvbpLupifECia7FvDHcXg1fSFtNO6QBWuBvgDi6Df8OGe-J7FiQjVha8GVjc62yW45SjQxt8kEiKMAHLrfI9R_nCNYBST3DR6GxDoQg1u_VUjAleHtpOiZww__rkitZs4K50bJXalZYPbal920CETxA8IMXnljqQi7M2Bvsj51qbvaEeQo7wPouah_IzC3BNfgAbjopDeFQg3h5x6mNUC2V1zSCIPgUieuK4FGovG7BAf3saQBx8AsNKKGOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت صدها اختلال اینترنت و موبایل در فرانسه
🔹
براساس داده‌های سامانه پایش اختلال دگروپ‌تست، امروز ۴۲ اختلال اینترنت، ۱۲۰۱ اختلال موبایل و یک اختلال تلویزیونی در فرانسه ثبت شده است.
🔹
در میان اپراتورها، «فری» شمار قابل‌توجهی اختلال در خدمات اینترنت و موبایل خود ثبت کرده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/466714" target="_blank">📅 21:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4TIFZ6KNayZVz-s81w05vAjOZZt22zMtXgRee9EoSqY0iJDr8mUMyXBvVwvWakNJMa9CVSLBUMSqOiiMfpCiCIlVuFlt3OFJhKcoNQZW86Czi4or3eWkixEiHGVkNteVJY80cOKN7RW3J9IKo-7UZq0ZzKhMLbvX0F0Q-oTM5CvIBi2l7rrwnns9TOI8-rqkxLJ0Qgzf01J7eQZHNeIdvsCunrcsYwgrsY-9w7HdOz6GEWM8bhigCbhoz4pKY-O0yDNCHxxkMV-JnxL2rf2IZmW_mxg381g4z2MA_i19RLggvyuOudsgPTG8SZ_U8uRxj2CU1od-vYGC8I4IzAY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای «طاعون» در روسیه چیست؛ آیا باید نگران باشیم؟
🔹
در روزهای اخیر، گزارش‌هایی درباره مرگ یک کارمند آزمایشگاه در منطقه ایرکوتسک روسیه و احتمال ابتلا به طاعون منتشر شده و نگرانی‌هایی درباره احتمال شیوع این بیماری ایجاد کرده است.
🔹
با اینکه اطلاعات قطعی اندک…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466713" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466712">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
سپاه: هرگونه خطای محاسباتی و تجاوز مجدد علیه ایران پاسخی دردناک و ویرانگر خواهد داشت
🔹
آمریکا و رژیم صهیونیستی در همه جبهه‌ها شکست خورده و در دستیابی به هدف کلیدی خود یعنی تضعیف، شکست و تجزیه ایران به عنوان قدرت منطقه‌ای، ناکام مانده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/466712" target="_blank">📅 21:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iksO6j3QTpQB8ZXVxHyU02siPJ2_IogokR8Dy6w7ADkZ6QqZAxCo10hoqrUdQiKZyBl5-dJ46Q7Yo3uDLKpF3kENBl0SHaGvUoEs8w1Bxrk0O5mc5y3bzPwT9-EygtGeVUXZmJfT3Vk2vK9c-buo2pjoPY6K4hZPRu2B5HYsViA7GudIRxQahlNtKahCwIIxxWgJ9coAR-NttvpdZHOGRVRXDqkMCMB7XYeOYYmpQppR4BbbD-f1CigzgMDyhIGgmGV4fMdPYfJj3MwPQIpkmTW9kPWsKGZsHo-j9jJ8Jz1LgDw9ZzWQ-9WaNhoN4T_63OHB5Rqe84FKy3l20Qm-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ درصد کاهش مصرف، ثمرۀ تغییر نرخ سوم بنزین
🔹
مدیرعامل شرکت پخش و پالایش فرآورده‌های نفتی: اعمال نرخ سوم بنزین باعث رشد ۱۲ درصدی مصرف سی‌ان‌جی و کاهش ۳ درصدی مصرف بنزین نسبت به بازه مشابه سال قبل شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466711" target="_blank">📅 21:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466710" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGOk1ZwwjJy_3eunN3bD-Kgl8isadXMaOztg4_HCMVCTRp_ZbPhq5udn9BlGsntBluonUaxtdBVoz9lSSe9hAuGqxv0G9k_04C4oEFx6-EdmMOlNzbscIxGaI6xsWfNcNby5ELAh5WxT_Oowel1_pdkkQbvA9GXauVw9PeKhkQEd9xaMUm8r5k2k-l50T5noN9R7_nTzZ2vAGImqBSahyLhOIkL0HnGGWWz0FZPyoNCA9R-XQxrSm_jPh8Feh5WVFwaigix4sbPSUie7LjohFZf7gH9AdGf0TEtwS2vIJDBFGr4Pl05UPnncT7D5Ix_ifxUbl2ZUScH-_kNCUZUoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466709" target="_blank">📅 21:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466708">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b03d96f4.mp4?token=JrAScbT0T3X-RwMgtvsBU5JpvpmaipIt0LmOnsxzqGl79CyDswnzo8HbeIS3jm24lZDEsb27erdFz_Lb5zXmnBSxQk1HeOQtSrfv5OUzWfdVPzqm6vXFLxrQppSn7R8F34931bJ1KUmf7tdxoXq3ygBe3qb2iaAyPniO8fY-ymtz9UthuX0iHE81S0ZJG1SyfUD7SSLrXBu4D3DNdYhNZ-DnuC8XJ24zVgYt4TJYnOsLKurJS9F28mHcdjcky81gFLA6-CFaBRUyWXHGglmJs4n7lnGaOMi7WwjSeV_SmtGs9CWori3oJP2PV-To3V-FL8iH8wNaudyh0iZEaQpPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b03d96f4.mp4?token=JrAScbT0T3X-RwMgtvsBU5JpvpmaipIt0LmOnsxzqGl79CyDswnzo8HbeIS3jm24lZDEsb27erdFz_Lb5zXmnBSxQk1HeOQtSrfv5OUzWfdVPzqm6vXFLxrQppSn7R8F34931bJ1KUmf7tdxoXq3ygBe3qb2iaAyPniO8fY-ymtz9UthuX0iHE81S0ZJG1SyfUD7SSLrXBu4D3DNdYhNZ-DnuC8XJ24zVgYt4TJYnOsLKurJS9F28mHcdjcky81gFLA6-CFaBRUyWXHGglmJs4n7lnGaOMi7WwjSeV_SmtGs9CWori3oJP2PV-To3V-FL8iH8wNaudyh0iZEaQpPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نخبگان نجوم، مسافران هواپیما را به وجد آوردند
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/466708" target="_blank">📅 21:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mab30xsw9UTMLFw1cm8Q2Ud0Y1qo8Lc2IQlOwUyC4Yl72eTMnv2Pphg72aFs7Mqb5jj3BmGhKY0TTtX3qI_nkLks34JvpWrNm6uwPCyi1TTuie-eXRz73QY_cDU2XcGR668d1nsJP25mJsJju4N2O2XHIZd2r35Rfq_7e2GO1LI7ufGJ7pNkfJ9YcOSOsmnwywEwjuremAPudLw9uil4HVQcPU0VLZfCL3C1ICuamJzih2d5CdSwEBcrGV67PH_b3QttKHYDcBR--fOhynpYLFZUxISUCeJ85qGJsKc91v9VWddJ6zMnnCRw409sI1Uj52NCPxxhTF4jYJGsh1wPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان: یک کشتی در مسندم هدف حمله قرار گرفت
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466707" target="_blank">📅 21:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466706">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTPCQ1Y2hvD5-E50S7uMPyPJdqMSsBwHuC6NPaF3r65Ub7bHK6nPcmmfh_jTfakVwOupKgUZb_1v_thlontDaAxI4yhqeLLDrpsSYKJcQWpEs6MtbPgqsErgjoYJEnlqERFmGpI9ZNH6WbJ9vbkizqu-qY9L_L0FeFyrOUK4ETmsgaI1O5ehR5-6zqC3jGCC00klWPyWaZ6wf3ctb0OQIJyWAoJlgoWZr3iG9kMSvwSEBcADnEIean-jMrKx2Z2esiyJ9qCU_S9uBfEgRaOs5JcXPuT4PkRGQ26JHSWlgRxMJONYdru4mM6VFDDsB2l2TxeNVXucQsbBd970sqS3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تورم صفر به اصفهان هم می‌رسد
🔹
رئیس شورای شهر اصفهان اجرای طرح تثبیت قیمت کالاهای اساسی در این شهر را منوط به تأمین سازوکارهای لازم و حمایت دستگاه‌های حاکمیتی دانست فروشگاه‌های کوثر نیز می‌توانند یکی از ظرفیت‌های اجرای این طرح باشند.
🔹
مدیریت شهری اصفهان با تشکیل کارگروهی راهکارهای کاهش فشار معیشتی بر مردم را بررسی می‌کند و امکان اجرای طرح تورم صفر برای کالاهای اصلی و ضروری سبد خانوار را نیز در دستور کار قرار داده است.
🔗
متن کامل خبر
«
تورم صفر به اصفهان هم برسد
» را اینجا بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/466706" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
روایت یک طوفان تاریخ‌ساز
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/466705" target="_blank">📅 21:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDyELkmcG8ovLSHnRyGxKETcy2XpX_PsEPHNlqe6-2ws73GVzZQvvlElwqCK1FQDBd_bMx3aVtWrYuD6ew8-s1CqMme-KuBu8gRUqWC89sanO2AZTo2PWa-YyusGZ72NTjYb8D0_j_CP9HYtUcvhOa2dH5thBCfeF4XrKbbrRuloB8RSt-EJTxN73RTZ1ttZORgEQSkZpJq4g-QhLDCBNAULpUWd2vwCC1JHPT7Wq9eIdPRnmTrEKdehx63GWmbetVdHayQ2O5XU7pjpmmbcXb_x2Xfhmt2gQ5l23Q2cCfOaOWvKttbznX7y_JPH7jeyZZ_iI7mGILK1A3o2KpXiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ای ستمگران صهیونیست! عامل طوفان‌الاقصی خود شما هستید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466704" target="_blank">📅 21:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/435c6bd438.mp4?token=XNdRDhTKsCANUwIn1Rc1m2sHm0VFiAZ_yewqmNcuq4-mWBj3l5Tq4vLnca3JyH8NJg7lob5GgghZAhkKlmDwIyhX2aaR3b8EB0BO1vdESP5T98uuRboMkmGJkMtfK9MCg7SQeuGHkksN96OFIUKKherZj0vvv7dToHQoPCkxx6fgtBe4GspI-UQcbMPgFSKDni17BIIg2MmWepeSn-0UeBRmEcZDLlJRFskpH3g_1UmezrDFDK5dUlfmyp1SSM_CpShjxo5Bmd7F9pwXSx_UI6zRJ7dwMle5O-8imaye8Wd5HyISD6fbvQ9xCAob8KmvAHuLJBtpS65E1svkQdVyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/435c6bd438.mp4?token=XNdRDhTKsCANUwIn1Rc1m2sHm0VFiAZ_yewqmNcuq4-mWBj3l5Tq4vLnca3JyH8NJg7lob5GgghZAhkKlmDwIyhX2aaR3b8EB0BO1vdESP5T98uuRboMkmGJkMtfK9MCg7SQeuGHkksN96OFIUKKherZj0vvv7dToHQoPCkxx6fgtBe4GspI-UQcbMPgFSKDni17BIIg2MmWepeSn-0UeBRmEcZDLlJRFskpH3g_1UmezrDFDK5dUlfmyp1SSM_CpShjxo5Bmd7F9pwXSx_UI6zRJ7dwMle5O-8imaye8Wd5HyISD6fbvQ9xCAob8KmvAHuLJBtpS65E1svkQdVyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: چرا هنگام دریافت حق بیمه قانون اجرا می‌شود اما در پرداخت خسارت و دیه نادیده گرفته می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466703" target="_blank">📅 20:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e8b9f39.mp4?token=g4VTPn0JUVKYSO6OFxO5hAvrXoqUCeWtyoajPvV7joHfKKnIjvhk4rwv3bg2DQ0eZ1TqAhcjL1iRf9qYGfEiL7CsII6r8OxuTnul7Yls9rUKkozuOQBE1Vyu7KTsmMrl_57E6yMENrR_SSeM2odZ27U6gyRBftHbGPAftfQchq4CHklyyZcfjgI7-F0AjCwAA0Yh9tOSfwxZpxyFWUlL4fug-yPUrwXN1HFiT2MsqSg_zFgWaTDzo5TL3CylTbRp0tEixHFJuG-rSa2m0Hx9ZotG6xQm-rtvkbumUHZJIG74rAl-1iZ1BPH6xvBghLa4lMvFEJfXt2CrlwgxWQtpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e8b9f39.mp4?token=g4VTPn0JUVKYSO6OFxO5hAvrXoqUCeWtyoajPvV7joHfKKnIjvhk4rwv3bg2DQ0eZ1TqAhcjL1iRf9qYGfEiL7CsII6r8OxuTnul7Yls9rUKkozuOQBE1Vyu7KTsmMrl_57E6yMENrR_SSeM2odZ27U6gyRBftHbGPAftfQchq4CHklyyZcfjgI7-F0AjCwAA0Yh9tOSfwxZpxyFWUlL4fug-yPUrwXN1HFiT2MsqSg_zFgWaTDzo5TL3CylTbRp0tEixHFJuG-rSa2m0Hx9ZotG6xQm-rtvkbumUHZJIG74rAl-1iZ1BPH6xvBghLa4lMvFEJfXt2CrlwgxWQtpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دوگانۀ اینترنشنال؛ از پلیس تهران تا پلیس پاریس
🔹
اینترنشنال که همواره با تخریب پلیس و نیروهای امنیتی ایران، هرگونه حضور آن‌ها رامساوی ترس، اضطراب و تجاوز به حریم افراد می‌خواند، این‌بار حضور گسترده و برخوردهای وحشیانۀ نیروهای امنیتی در مدارس فرانسه را «مایه آرامش و امنیت» معرفی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466701" target="_blank">📅 20:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCPfv0pumOa8Mp6QJe4CBpArMUZjhun-uZq4F0h9ng-yBq3O8jBfjk_Uy5iNHQNU3BmED_Yt5fMDWWKr5Fs6OvtKkxXRq0n9NuYMGEW2kriHy83lXAZgiLsPSQ5gwJQ4B3x8mpX9blWaPA7vm4BZ5B85EFW2bCIjAjlR_D98C9AVGNifyV2IYGy1aAeo8ZD1Qzs2qIRVPfi9IqR7f3EuF0qzsGQ2-PAepCFj6u4ohd7FdnYGzSMr00JMbl0b6CsmxdUXc4ymhXCgn-X52WyXrWowUNpx_X1HKMDWAxr1tysVO9hISHk321QOJYnZR6dze4gbYjA5oqhl9ABaWE-9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار حسرت‌برانگیز هواداران استقلال و پرسپولیس در آسیا
⚽️
کنفدراسیون فوتبال آسیا آمار میانگین تماشاگران در فصول ۲۰۲۴ و ۲۰۲۵ را در غرب و شرق آسیا منتشر کرده است.
⚽️
در بین ۱۰ مسابقه پرتماشاگر آسیا دو دیدار استقلال و النصر عربستان با ۷۵ هزار و ۱۳۰ نفر و پرسپولیس و النصر عربستان با ۷۰ هزار و ۳۵۰ نفر پرتماشاگرترین بازی‌های قاره آسیا در این ۲ فصل شده‌اند.
🔸
این آمار افسوس فوتبال‌دوستان ایرانی را در این فصل بیشتر می‌کند چون ۳ تیم استقلال، تراکتور و گل گهر، به‌عنوان نمایندگان فعلی ایران در آسیا از میزبانی در کشورمان محروم هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466700" target="_blank">📅 20:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5219cb68c.mp4?token=OdYJTQvW-ehZPeVTKva08n-KKvYI_kJ3uuJjBxfPWhu212f3rN9fSvhleSRpbAq75Bn_m7dGqABX9-0U2bI0ZlBpMfG4hdMqAoF3J5rbgaW8-VD-y3ipwBMOfaZKOblr1IYCDOFXS3zRA2N-D9FZp4-ONI_QOoiDx4Luaubv7pVtglH1AsfHyEub1OF7GZVBOyr0PCrI7G1sXNnMs3UVfhyKFoTufTRPg5QuUOex4Zwp0goWDky4Z6HLnip0tSotRvK1ZQVK24arNEFOAT-au5NMz1MESpwwuU_3JWIp92I5OHxVKUtozpbRWMo3iOduA6C-CkPhAGBwICIIxjDblaiWPg-trZ-SyigE-H6Gg-QZW7nLAVLmiWN8nzoH0swupYu7pI_jDhLS3cJ4MbbmTGBDydyphEy0fHqQBiAxjiNldZP4dwdgOSxpScSs_CQLCKaoJwiycuNh6gP03lz5ddVpmNlv24FhHgQLN-sf7P7dkxZjKhZwSZNGyQzNfme9E1xja6BQXZCRukopVo4q8y1hI2AGzieM2eQU2of9ytTvDO2QkWGpDGV3VpuQRBFh2S1GIm216ufIrYqvdj0bEI2q0AkVyjtWSj5xbk9ggiyl70WYrlt2JUOBhbwcqXUDqRw3GRmjgEeiH2TXqOzq84hU9C5Xh2gMu3YIAJJznp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5219cb68c.mp4?token=OdYJTQvW-ehZPeVTKva08n-KKvYI_kJ3uuJjBxfPWhu212f3rN9fSvhleSRpbAq75Bn_m7dGqABX9-0U2bI0ZlBpMfG4hdMqAoF3J5rbgaW8-VD-y3ipwBMOfaZKOblr1IYCDOFXS3zRA2N-D9FZp4-ONI_QOoiDx4Luaubv7pVtglH1AsfHyEub1OF7GZVBOyr0PCrI7G1sXNnMs3UVfhyKFoTufTRPg5QuUOex4Zwp0goWDky4Z6HLnip0tSotRvK1ZQVK24arNEFOAT-au5NMz1MESpwwuU_3JWIp92I5OHxVKUtozpbRWMo3iOduA6C-CkPhAGBwICIIxjDblaiWPg-trZ-SyigE-H6Gg-QZW7nLAVLmiWN8nzoH0swupYu7pI_jDhLS3cJ4MbbmTGBDydyphEy0fHqQBiAxjiNldZP4dwdgOSxpScSs_CQLCKaoJwiycuNh6gP03lz5ddVpmNlv24FhHgQLN-sf7P7dkxZjKhZwSZNGyQzNfme9E1xja6BQXZCRukopVo4q8y1hI2AGzieM2eQU2of9ytTvDO2QkWGpDGV3VpuQRBFh2S1GIm216ufIrYqvdj0bEI2q0AkVyjtWSj5xbk9ggiyl70WYrlt2JUOBhbwcqXUDqRw3GRmjgEeiH2TXqOzq84hU9C5Xh2gMu3YIAJJznp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این افتخار همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466699" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAjt9BlpIeFxJTR31KqcT-J_EFlCqXlwO-dfAt4rPA0UGh_1DXXf9Bu0SideRcnE7cA_6OgbAZ4Ixh1vIYi1Lyf7PFngifl-IwOMKBErHNbTY7FhGh87JDHoe_T_fzGvoNmkhZOwBXpo4MtMb5YUNedMh2yZZxaEducc_S7E3fF1NXHyMjmhOgvGg8Y80PrD1AsiaSsV35E6KLt-Rjsc_S4aGy0FdIYA15wWC7CdqQQpFZWjOVDEwWipf_LJ-wSg5KpGnKQA4jXMABJDHD7WYLS9RxJXoaObhcWy29gmvw8cEDCRQ4PESMP-ng5VZD3EsKdR_y-eWz4UEOHhKk_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه: ولادیمیر پوتین در جریان سفر خود به ترکمنستان در ۹ اکتبر با رئیس‌جمهور ایران، دیدار خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466698" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466696">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqvM-pwaVztfYCDoGz5Yl2X4537jvvW9jBkkP0euKbCiNoNuVlNW6hN3etjlww2oeaIAdfRhciPS5AtNtfbjof787DF0_cF2sv0yqA6GICqK-H3-oXaU3HdwSS_cs0P0sER8yTH2TP49978zI15xHIwnu98QhXgkvqup3wgKbTcyMcr2NQ3_WCr3e0it9_UAgYdnsq7Zi5o-owcM3ea0oCGA1pNggkTynVZetoz-nfe7YfvuH0SjNbENehwcSdP5HzkSZ5Q21ZjX5mPl-Qr5NETcJ9W_7ztyoc0MbmScu0h9zQ0mY3uq_1YXbdIW5PD4Jujbc2YUZX9znSD8CEcEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید دبیر در مورد ویزای آمریکا کارساز شد
همه ویزا گرفتند
🔹
فدراسیون کشتی اعلام کرد که آمریکا ویزای ۳۷ نفر از کشتی‌گیران مربیان، داوران، فیزیوتراپ، ماساژور و همراهان را برای حضور تیم ملی امید در مسابقات جهانی کشتی آزاد و فرنگی امیدهای جهان صادر کرده.
🎙
پیش‌تر دبیر، رئیس فدراسیون گفته بود:
اگر حتی یک نفر از اعضای تیم، به‌ویژه کشتی‌گیران، ویزا نداشته باشد، قطعاً تیم را اعزام نمی‌کنیم.
🔹
به جز کمک مربی که مدارکش ناقص بود، ویزای همه صادر شده است. اعلام شده آمریکا تلاش می‌کند تا ۴۸ ساعت آینده ویزای این کمک مربی را هم صادر کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466696" target="_blank">📅 20:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466695">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: چند نقطۀ تجمع نیروهای دشمن سعودی با موشک‌های بالستیک منهدم شده و شماری از مزدوران در این حملات به هلاکت رسیده و یا زخمی شدند.
🔹
در الوازعیه نیز پیش‌روی دشمن ناکام ماند و تلفات چشمگیری به تجهیزات زرهی و نیروهای مزدور سعودی تحمیل…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/466695" target="_blank">📅 20:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEglamYnT0n-DvcbbGm7hhkG7HOSQycPER2-xu7v1UQ0B3MXbTkiHO4wAbqEsV71oBYzM1arBwheSWAkODDTvA0UuKVXgzHZEqEGTHLyY8lrrjvuiaryJkHdMzlubvf5nHQ_lBoZtAJQ-qs0678RsgoT83f0CFya1ilkA9_5rIZpbCiZJGbf8hAMmwiHfXpZ9eKpcS0_FkKKkIREDtAtiKArugfeBJjc0RLNDjJCc2Eh-pXZh65S2d3qIdo-N7JC2myuk1A85HRvxDeRGknfKb6jm9M1yZPWUGrXhN2KYKB5rkr8o64gIl60TVt5IvTgcYDDAtOacZ8x6og3qjERJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق «وِیز» را ممنوع می‌کند
🔹
وزیر ارتباطات عراق از تصمیم این کشور برای ممنوعیت استفاده از اپلیکیشن مسیریابی ویز Waze از ابتدای سال ۲۰۲۷ خبر داد.
🔹
تصمیمی که بغداد دلیل آن را ارتباط این اپلیکیشن با رژیم صهیونیستی عنوان کرده و هم‌زمان از وجود جایگزین‌هایی مانند گوگل‌مپ و یک اپلیکیشن مسیریابی عراقی خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466692" target="_blank">📅 20:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkXHC5z4vZwtUjljahD8iugEZ-Uym7VWgfdednmGfI4w936_34uWIej_fXNd-6uI-VDjnQ0HIoZCk5_NUdDx14RB4MeY5rvSMIha3-7_Wv7jCGxx5Wbq1lpznA67ps8qvof3IGPKOMO-SZHyf_JYmppHK3wd1tJES0sa098TMFM4jeqGJW5niuViRK1lGKZK2QjAdhY94HhFoMFlLYZFPBKirqsS-ygngF7wPhEyy3QxVr-Ob5_2IF1FSDuSlIpiGnbWGPU-vwXfYsghqdGuvz5Q5OFKSfoWQ26j1imPe2wBOIesJbDZX4iDmngUYzSZGQ-3CeNe6GZYi2-_129ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایتل به فروش گذاشته شد
🔹
شرکت سرمایه‌گذاری تأمین اجتماعی با انتشار فراخوان مزایده، از واگذاری ۱۰۰ درصد سهام رایتل خبر داد. قیمت پایه ۱۳۰ هزار میلیارد تومان اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466691" target="_blank">📅 20:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌  عضو دفتر سیاسی انصارالله یمن: توانایی بستن تمام فرودگاه‌ها و بنادر عربستان سعودی را داریم
🔹
البخیتی: عربستان نمی‌تواند با گسترش دامنۀ جنگ و ورود سایر کشورها به جایی برسد و ما آماده‌ایم با هر دشمنی مواجه شویم.
🔹
جنگ علیه یمن هزینه‌های بسیار سنگینی خواهد…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/466690" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">البخیتی، عضو دفتر سیاسی انصارالله یمن: زمانی که سعودی اخبار پیشروی در تعز را منتشر می‌کرد مزدورانش در محاصرۀ نیروهای مسلح یمن قرار داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466689" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUtthH6BUIWphrwzJ1M1AhiFDOfPcW6042_4ZEpaP761rFmzX0tW-q2aRXaOIsWG4ZFhbX3T_U3KX6j043WYupdjzqZw6y0yMKROPgA1GQrwu5VadgvdtzuP7GfpABY_3E0JXOP9ngJBLSHS7N0KmJBcVNWUKlrIMGDmfXIdkQLM3oGTOpIeyZ1V6Pm4cAzM79YVLB4IaVouADNMp4IV4_pqShM5notrpuXQTq5QTRxkqtBAzMYoC5hjWPT-vyBuAI7XpRayYFJJfD64MhvJKTqjb90pbqkspNM4Oulu9zG7q19BiZj2DYc0gSmVc9ebIkZ2d3Ls_n9iFYXfKRlB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466688" target="_blank">📅 19:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7295eb324d.mp4?token=HLl_yDFf8PxvNcqX7JDrpOJAHm9NP1RtE9_zGO9926LwKLNoexxaDTv4oEEqECFlRZwLlMyND36kZiQk9sHDwVTeMvRlS7g5JSPslmikuqqQhDrIhp_gHR9XY3PV4Ajqv70yhliSh_71RU_F_HtKIDOIQLPqgyhJ2IgPtkcLRWo1PaucdVEc5yO_iZnGRszEC8RY4A6imyCFl3_7AC422r_5FibaPboNrgb20dOQzDs9Kvx1v3ok0oZHA-PK8Zz1Y3dWuJd4W1Nm-BRxXIVzNtkej6b403uLyOHJCz2cZN2DIbDmGJ7iYZP80A6S5LSwviptbk3DPuL5MUaFBJVIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7295eb324d.mp4?token=HLl_yDFf8PxvNcqX7JDrpOJAHm9NP1RtE9_zGO9926LwKLNoexxaDTv4oEEqECFlRZwLlMyND36kZiQk9sHDwVTeMvRlS7g5JSPslmikuqqQhDrIhp_gHR9XY3PV4Ajqv70yhliSh_71RU_F_HtKIDOIQLPqgyhJ2IgPtkcLRWo1PaucdVEc5yO_iZnGRszEC8RY4A6imyCFl3_7AC422r_5FibaPboNrgb20dOQzDs9Kvx1v3ok0oZHA-PK8Zz1Y3dWuJd4W1Nm-BRxXIVzNtkej6b403uLyOHJCz2cZN2DIbDmGJ7iYZP80A6S5LSwviptbk3DPuL5MUaFBJVIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبۀ ۷ کنکور انسانی ۱۴۰۵: از دفتر رهبر انقلاب تماس گرفتند و مرا مورد لطف و تفقد قرار دادند
🔹
گفته بودم موفقیت خود را به رهبر شهید تقدیم می‌کنم و ادامۀ‌ راه ایشان و شهدا را وظیفه خود می‌دانم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466687" target="_blank">📅 19:42 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
