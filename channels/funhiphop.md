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
<img src="https://cdn4.telesco.pe/file/svl3zbtzpya8HQi56RyvSy-_YUHFq4HkZI2bIfCxLOE7e4etYp_4ks0tlFZG9ZdDvwWslLV-EHcNB8JxpCY748D0kThn5WV64GrH9MYDh1bwx5jg7xGpEL1Eq5Wi3ZKhepddP4IsH-FulLlqCw-y-XdBzrgpPpX_aNW57WQOQVm90Qw1PFZ4HS-tywHp9b5uPaNgP2aDLiv4C1C7EmINjPLte-wQn4IIdYP8duQLKTc8kkXBRAgP7aaXyoEqtIyIVkxDdF0HWjOdskeYm087QNxaCInuJaLCcOXzj6XMfh0yueCldjVNfQLQaOs_OwKPsfDgPy2Gf2okIB5bdqirpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 145K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 02:15:29</div>
<hr>

<div class="tg-post" id="msg-75042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.  @Funhiphop | reza</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/funhiphop/75042" target="_blank">📅 02:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75040">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه
جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/funhiphop/75040" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUyoKTqEsNtnyYH_GRKKq4irBh05tjef548IqXrSxTqMbNVA9OCZ0hwXbY5FuKTKidl1Ns__4CM03iRBkI-OTbO3u8KJZETfvcdA-sxbGZo2BZdyA-_DEha3mufKUuNZHXt_gx_IRmJlARmq9P_zj9HbyYA1BvesK3TQo1ojeDA6TGQhLBoVPEdxeb_JRtoW_Zpw8Wuz-yvWnIRvwAKVKsWdhujQkbzZnEs1qg--G49D9xkxiDXtpe2L7NrNUp-mxFdVs2pGWmjIv4gFK5M6IiCPBu1HQWn-HE2_vmzaRAH2dStxwKHQ9FV2wq7H68hT45l8AWOpdzdf0e4sXntmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید از آلبوم دریک حمایت کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/funhiphop/75039" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دست مغول‌ها چهارتا آجر میدادن تا الان اسرائیلو نابود کرده بودن
😁</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/75038" target="_blank">📅 01:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تایوانم پوشش بدیم؟
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/funhiphop/75037" target="_blank">📅 01:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مورینیو:
سری آخری که سرمربی رئال در الکلاسیکو بودم ۲۵ تا موقعیت پنالتی داشتیم هیچکدوم رو نگرفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/75036" target="_blank">📅 00:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مورینیو:
خیلی خوشحالم که این افتخار نصیبم شده که سرمربی وینیسیوس باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/funhiphop/75035" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فوری از فرید رومانو:
مورینیو سرمربی رئال شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/funhiphop/75034" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">[ Fun HipHop ]
pinned «
رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop | Farid
»</div>
<div class="tg-footer"><a href="https://t.me/funhiphop/75033" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCL3KGC2G9XO63gKImQ8iZuQ8joO5g2CVL0ozO4XJHllyvHBq5HhlXZXsTeJU_BhEE4hNsNgZx-mooht4Yr84yJQTSCapjnvrHS3iDVaUcENR7V61c2lo6Pu3qVJIZJ8TYteiml4FZknKzUQzfgeuI4uad6xWXOWfRPWrkRXLfH9ThGEdllqh2G2laimf03Go88vglL0FZ_IplE-8-g988LFxBl0-wXVNj60CoZur3iHL2MYnn7WdFbWPP_AZJT2xBsQV66-FRn_scR5zdeh5mRLIl62f9XJNARWlMakwe0oxpk1p7lBim9Hs7i4eVyJJn0mpGoAtsJCoGiAmc_SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">د اتلتیک: راب دیپرینک هلندی که قرار بود یکی از داور های VAR جام جهانی باشه به دلیل تجاوز به یک پسر 17 ساله دستگیر شده و از لیست داوران جام جهانی هم خط خورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75032" target="_blank">📅 22:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بیایید بالا دلقک شدیم.
هادی چوپان: ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75031" target="_blank">📅 22:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/75030" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6p1BFlKyx1LkkjXKLJqyNI-2IlvdhdkHviVxbwoqU134Oypu6mkPfWWgxqX8LmwSvdCaUS-90vNHimLzGg7ve0tsRvBQwu8r-Bb0kfJrqMFBv8_iQ095buJBciCnqXNvdnlafFR26yMz6bdHmp-lPHaM8DdAjosg0AOnGJtf0NeVZqOcDjBmKLM57mzWZ5zYxjp5kWL8lQFSOvNTMqXmD_se3NHRLb0y-BsxVglCRGKvUziQyAI4JT4exgHjs4CHE37Www8krj1hZiUdpsIdoUo170knzTeZfSdYW8SdulRwZLZuiRTd6kDtpuffDLHvXfNDlho2qjvUvVU5LbLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری دائمی ما باشید
👇
👩‍💻
@ConfigRahNet</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/75029" target="_blank">📅 22:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd67VsawsojBitvGptVY6B9SISb-AObG_MWC61hiFU5J312lSHU5vB6U_-8DKMzPqgIJY45OdZO7cRJESNFacnUGmN7KbETgRVqygnjLWasu5U849OxUKp-GglzgbgNkiRr5PdBgsnXjLukKER5oPXe_CXfhT8zeUnuuRK0uhubE8Tncw_JlqAYl1-1VgdQYaKHN9-y8mDIteXSatEAW1L-MBQ-zz1ufMo4Bk2Q1g-EIx1-B6osnBtcvWyVqwerbCDjGruz6DWPrX6vFvMf8m306arTCeAUibFb7ay5qqOtVrTLXIVEuKHotNDDwtLlTjSD8B780m44-wa48wwZEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/75028" target="_blank">📅 21:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/75027" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/75026" target="_blank">📅 20:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/75025" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تحلیلگر های بازار های مالی نسبت به
قیمت نفت
یک دید
صعودی
دارن و تو تحلیل هاشون
راجب جنگ دارن سناریو نویسی میکنن
که با از سرگیری درگیری های
خاورمیانه
قیمت نفت میتونه تا
بشکه ای 140 دلار
رشد داشته باشه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/75024" target="_blank">📅 20:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نشد یبار یه سامسونگ بگیرم دستم داغ نکرده باشه</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/75023" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-CkkhxtQUlxYRpxZIXGG5LxEfrd90RmN1eUSG89HFoFfTWt5AS9AEVw25B-o_8i131WfJ01ikRlHm3N646_c33fwoVaYIPLNYneqQOTBny33VscEHVkgqUvCs84QS94yj-H_h_fEaTBHjiNI_pFB8JlDTdnxuO6aBzfsmq6Zwu2uSemHkxKf2H5PFbwEuTX52ye1NYu8Rcu1WkgTXt4m7WiXKbWi2Y-Vnw3OC39Te51slidSA4P75E46Qk1N9OmuPRsZC9hE9bz38eumGtgeo70F3rqC0StjvSUEO0KMEWqlmVyA_GYUQjjgneo5QyO_0OgPzQwkMAla4Cqhnw1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا وضعیت اقتصادی خیلی خراب شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/75022" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پشمام دریک میخواد برا تیم ملی ایران سرود بخونه</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/75021" target="_blank">📅 20:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cASMbRbrLL674ihkqSi6ZalS4L_-HQISqCUSPqj4mPhgQROP8aerReSlN7GH6GJcTmRlZpnxsWYLojypvp58QriE1ZCvS7dDP32P3luWGfv2pKrYvj949nHKbv-h3IkF6MNNytgTt7KytYHmRsstrzGfWDussI6x0_X1f_Snhnpt8suqecf6T_Td0ofDLAN6k2cO554MpST4Qubo_ryjN1l0nEzqsb3m9-VTgBnwsHxkbt93ntdF8ZtEIJKJkNbSbO-uWy01-UNpK1e9ZOJ0Sw6ogML4Bi-MiCyBiTZkfZmisBXehSFtR7q-4L4v9gKxK7soaua4pLmJuykNwW0bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/75020" target="_blank">📅 18:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزارت نیروهای مسلح فرانسه:
ناو هواپیمابر شارل دوگل در دریای عرب است و احتمالاً ماموریت آن بازگرداندن ناوبری در تنگه هرمز است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/75018" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-msQ3FsW608Gst3CamI-fLtpa_2qr9wIe2qDVyfJBeuSb0ya8v6PaSB9zIHdn_lRe5S6XylJhTvlp1nKpcMgap5_kGtuijjbNv9yvA-wWC-H73J1op0YkKCH4BNB6ejdDQhHChav8ENNpx1cKlcRfGNsKmhRY8bCLJ2P6bA-0aj-4-6_TXnY7TPDfzLisyc5tnV7R4uGjLhbd9UMvHR7VQqsMvwCU0YOiCclMk9C4qs0z2ngHeeip_xnark6JtGToTQc_L7gNbi3lnpjQsYH24bnXH_2Xns1eTKWhhSvR4GCWvW2hizIUMmG8Zkpkh_z172NxjBnNsieeLkG5I55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/75017" target="_blank">📅 18:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTlCxohNsPwRiwI41GyECK6oOl1v7i5g6e9YD5YagmEwsKkjybqSZo6urBDhWVekNmM0UB5-RQRgv3FxZXylnlJO6vsfZsPjeYLBViQzdk8NHW6wuAPsA43ZjUjB3ew6EInYpFT1zRh2tQ83ldmlyAm_zCOZJ9DzarbYJ9mc07no8tw9A0ww3TXgAItl61NFAjNS54wBi_WaGX1L3qCXDznXlQWtBkng4GSsjG7DiGJRfOlJAO7i6bdp6wNqc3KL4T3XytSdYYg0r9cR2qmF30AWCB-bhBOI3A3qeHtEBxdtIqjcqU2E-cAvgMvhughQjCCemQ2nqYZvVRdHl-k7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیتکوین بگا رفت
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75016" target="_blank">📅 17:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75012">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNbQOyXN7IE6gKQC9b49TOFsllchiTPbjmfismMAtp5U8pCg2k1OlUlTxk48KOT67Ta1pFnsIx-5e8fGxSfKd1f06mxUL7stWcDGnj6Yecs4TbFR_u5DdBHNN28fsYXjiv5S_Q7xOVauAvRZI4oVNbLWPchidl3FNdQD_sFWoaQY-VgA3Axb_6dXTCob9J9oZheqMuk82SQRyybcME7ogZhPU1zxeFzuZSOlyHBt1DOBCmaGHb_Q9CJdanAZtH7Eu5T6NHYKQ-W4hHcynjqnqoQosTplrnKiYdA5HkSDpY2qRy4jVQkEsa9PEl_0qkR4fGDIV01ErV0-A87YLxEFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک Little Birdie  "همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75012" target="_blank">📅 17:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75010">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">موزیک Little Birdie
"همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/75010" target="_blank">📅 17:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حس میکنم تو پکن ترامپو دزدیدن یه نسخه چینی‌اش رو ساختن فرستادن آمریکا</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75008" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546804485e.mp4?token=cZS3lbA7qBSKLNXA3DboCro9SLZf0Ld9MX5pZRwIiZjJTV-s7pNY_WDPTUxkoeTouw5Z2PAs_rYPgh0W27l2EKEX4DXfciu82T6PBxb5pcAJJzyZB0AuWvbbxnHgmXvxR1_GhpC-jxACISwmgLJN1qv_Q2DO_kIPgjqGPc9h6BjGzdRgu2pjG6x6Z5qL-oZcqdFwxVAXN1JkuOIR8QZ3wIhFPAnh9amYh1JrGa2Ca_bay2C0J3GNrPDPTj7MVeDYn7q7QPHDkiezG510eAmeJST9yvh1Krynm3nB_M-91bvlRogmG1zuD6YjzbEbyomxVW_7rf5o5ZEmn-cwCHTSnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546804485e.mp4?token=cZS3lbA7qBSKLNXA3DboCro9SLZf0Ld9MX5pZRwIiZjJTV-s7pNY_WDPTUxkoeTouw5Z2PAs_rYPgh0W27l2EKEX4DXfciu82T6PBxb5pcAJJzyZB0AuWvbbxnHgmXvxR1_GhpC-jxACISwmgLJN1qv_Q2DO_kIPgjqGPc9h6BjGzdRgu2pjG6x6Z5qL-oZcqdFwxVAXN1JkuOIR8QZ3wIhFPAnh9amYh1JrGa2Ca_bay2C0J3GNrPDPTj7MVeDYn7q7QPHDkiezG510eAmeJST9yvh1Krynm3nB_M-91bvlRogmG1zuD6YjzbEbyomxVW_7rf5o5ZEmn-cwCHTSnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا درباره حملات سایبری علیه آمریکا با شی جین‌پینگ حرف زده یا نه:
'آره، بهش گفتم. اونم شروع کرد درباره کارایی که ما تو چین کردیم حرف زدن.
خب می‌دونی، هر کاری اونا بکنن ما هم می‌کنیم. ما هم حسابی ازشون جاسوسی می‌کنیم.
بهش گفتم ما یه عالمه کارها علیه شما می‌کنیم که اصلاً خبر ندارین.'
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75007" target="_blank">📅 16:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agvao3_BIlJcTUVKTGvp3lUsLwdgUADgTKuPzLNLoKut8Nt6bHlSU7wvOagNpRrP4ERROj8rAhGw2EBKVraIFEXdgL2KQUsuiqMc7OKbQBgKu6lZRfD8gwD8DWD-UEPUJ3b46dGZhqi1M7jhW4g3isa9hRHP5yBk_sTuKW2hZh4Y8RuQMise_o6EVeBWup8Bk77Mxi-hbVQ-gUzL31r6_6IdcXH8uzuQ3_zDOXhR_bfMlHVl0bXjIFtXiaIy6oqaoOUQ6TvI50KFsXIKWo1Sm02IJeJBOTB7jCYKr2Zk6VgNMOCjcabtuNby_qMgv77wjJ3SGBG2tsnXJyxnsDMOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتلو داره برا جام جهانی آماده میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/75006" target="_blank">📅 16:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/75005" target="_blank">📅 16:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8V2SS2D14f7a3S-k3CuREosUVlZbF-IxXgc5eIrH_0zlP-pTYGqQOiCQa7qW4QqB6P2Y_nIwjx0t1vbb_T38biscl7gbvRcAC9jCY8EbDxs57CiDFBCsvhVuMhFa7ipAva2SJutN-C7DFJCN5fAKg_QS3VIl65m_ycpM7L190zQt8o9Lghc8uakrT3V9DhGRJ3IT7uLfuKYFGnQiMnMQfu9RuyByxbmww-SWEbxo5bNqHXKLtGfkzElpt5WaJUrQwOtp3xs6OjxnVLmwyw2nNObZD754XHmxgGqeXSOvB-rjmKhHP2VWrBO1K2f3s7henD9nRLIAwf7FBPxoRMOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری
همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
مناسب تمامی اپراتورها
💡
مناسب آیفون، اندروید، ویندوز، مک و...
🎮
خرید و دریافت کاملاً اتوماتیک از طریق:
🔒
@NETSPEEDxBot</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/75004" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فریدریش مرز، صدراعظم آلمان:
من یک تماس تلفنی بسیار خوب با دونالد ترامپ در راه بازگشت از چین داشتم.
ما توافق کردیم:
ایران باید اکنون به میز مذاکره بیاید.
باید تنگه هرمز را باز کند.
نباید اجازه داده شود تهران سلاح هسته‌ای داشته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/funhiphop/75002" target="_blank">📅 15:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بیایید از تأثیرات محاصره تو بازار الکل بهتون بگم
آبجو کرونا تو بندر عباس شده ۲ تومن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/75001" target="_blank">📅 15:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب دیگه ترامپ بسه. ادامه‌ی سخنان قصار دکتر عراقچی: بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند. گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم. البته این وسط جنگ طلبانی وجود دارند…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/75000" target="_blank">📅 15:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=VqkWLxaLHOe-_-DrmIpkrZTnzq2DW3qFpfQ2ssX6R-dqzYCvvnoLa1ltQKfJb_l0LlndF0BqVucx3_RwSy6f19epy42uZMh9zCBdX7YMWefGWcsGfOAkfM-G9j5W2j4o0EYgXSyJakdyXNwcklG9sQGDzUxMsh7euH1UvARyKXJalOQIiKloFQEyYYxoqu9jc4M-gvjpMFxxMgcbMuzBKxBeW4kMcdHlQ4GmQlA7FB9PwHmM-aifMhvSbR6ViGiJdH7DWD6XpDZAt0_iPN2FHZXBskl2IoClwrXXO6TsudI2JvZ5pka7zlRTO2Xm3-1gbL3J03lnmUgKA-hgj_v_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=VqkWLxaLHOe-_-DrmIpkrZTnzq2DW3qFpfQ2ssX6R-dqzYCvvnoLa1ltQKfJb_l0LlndF0BqVucx3_RwSy6f19epy42uZMh9zCBdX7YMWefGWcsGfOAkfM-G9j5W2j4o0EYgXSyJakdyXNwcklG9sQGDzUxMsh7euH1UvARyKXJalOQIiKloFQEyYYxoqu9jc4M-gvjpMFxxMgcbMuzBKxBeW4kMcdHlQ4GmQlA7FB9PwHmM-aifMhvSbR6ViGiJdH7DWD6XpDZAt0_iPN2FHZXBskl2IoClwrXXO6TsudI2JvZ5pka7zlRTO2Xm3-1gbL3J03lnmUgKA-hgj_v_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه ترامپ بسه.
ادامه‌ی سخنان قصار دکتر عراقچی:
بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند.
گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم.
البته این وسط جنگ طلبانی وجود دارند که می‌خواهند ایالات متحده را دوباره به یک جنگ دیگری بکشند.
ما عمیقا امیدوارم که آمریکا این اشتباه را دوباره تکرار نکند.
ما معتقدیم در نهایت این دیپلماسی است که پیروز خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/74999" target="_blank">📅 15:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74998" target="_blank">📅 15:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مارکو روبیو:
اگر ایرانی‌ها تصور می‌کنند که ما برای رسیدن به یک توافق امتیازاتی خواهيم داد، سخت در اشتباه هستند.
تحت هیچ شرایطی یک توافق بد با ایران را نخواهیم پذیرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/74997" target="_blank">📅 15:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/funhiphop/74996" target="_blank">📅 14:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:  آخرین چیزی که الان نیاز داریم یک جنگ است. در چند روز آینده درباره رفع تحریم‌های اعمال شده بر شرکت‌های نفتی چینی که نفت ایران را می‌خرند، تصمیم خواهم گرفت. اورانیوم غنی شده ایران می‌تواند به چین یا ایالات متحده تحویل داده شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/74995" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">طبق گزارش خبرنگار الجزیره، انگار واقعا اون ۵ تا شرط پایان جنگ فقط برا مصرف داخلی نبوده و جدی جدی اون ۵ تا شرط رو به صورت رسمی و مودبانه به آمریکا داده بودن و آمریکا هم به صورت رسمی و مودبانه یه تک تک اون شرط‌ها قهقهه زده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/74994" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:  من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، اما این باید یک تعهد واقعی باشد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/74993" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترلمپ:
هیچ پیشنهادی مبنی بر تعلیق ۲۰ ساله‌ هسته‌ای وجود ندارد،</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/74992" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بخشی از ریلیز جدید رهبر جدید انقلاب: همه‌ی اقوام و اقشار ایران را در حفظ هویت، اصالت و استقلال خود و مبارزه با «ضحّاک‌» متجاوز، همدل و همراه و همساز هستند. از سوی دیگر مقاومت غیورانه و پیروزی افتخارآمیز در برابر تهاجم دیوسیرتان و شیاطین جهان، ملت را برای پاسداری…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/74991" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بِعَون‌ِ الله تعالی.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/74990" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/74989" target="_blank">📅 14:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74986">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/74986" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVAHID</strong></div>
<div class="tg-text">عشقم لبات مزه دموکراسی میده</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/74985" target="_blank">📅 13:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74984">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGlHKFvArZq1gYD8354I1SHCx012fPc_OIPfc1StJIvAXBKX-kPYu7gnOSMSYU5Jy_fRWwPyFN_MBtCVyqwNldRj5sb-ZVJpeVA718xNXl0Mk78yPilbLhX7cPFk-_KgASpOOB489YCfUddGwQ4_umtD1vf6NSpcakK-QWFXRiFvKjXrIH9zblOCqjfcwloFFkVPF5_zr2vhJnycdRMPP27FQ5dRScXmKaUXSzNIibGvgcVSe8T7GxnAhcmjNm63b4xm3gd9-tOt7JSUX-Tf-n7WuuPjeVKN4CRy7YFzMLsT7OBGz9H2vU6RorApTptQsLQI5nLEVuvKlj8RRv8-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/74984" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74983">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دکتر عباس عراقچی:
آتش‌بس بسیار شکننده است.
هیچ راه‌حل نظامی در مورد هر چیزی که به ایران مربوط باشد وجود ندارد.
ما فقط در صورتی به مذاکره علاقه‌مندیم که طرف مقابل جدی باشد.
ما به طور جد به آمریکایی‌ها اعتماد نداریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/74983" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74981">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرهایی به گوش میرسه که ایلان ماسک با بریکس حساب می‌کنه پول جنده هارو.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/74981" target="_blank">📅 13:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRn-bntOWKFQ50PNv-Uv2Xc7qnEkU-FvuV7vk8BNC98J03ycvmwLmZm7rUXZua0YgGNihZBhVt1fPYNoxyEPwZSikJlDZFumoiQl21ODZMAKc5yRs1yiYIYhBZ8GkixA22nFREE_pq2SbBDGvOdqUvEEICKMR2tRH4YERpR574Oqitg08GTNDs8PcL7XJxvwW2s4dHNkDj3m7WYJ9XVr1p4jqLCwOkUK92dXr9cbyb3b5MrcjkdQ1EUoG5wiXr9csSKco1cAefUcOXVaec8FfZ4OEKMievpGg0G6Fy79whFSdLVPa-x53KzSMJUkv8PWqNjCXhgScz2tLzyAy8mVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس تو چین فیلتره
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/74980" target="_blank">📅 13:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEzy8F1gjEV6pWrkFk1IaiBpfoZ8TBQcEg5DHc2i7JIS8iK0NAFs5PK-phcwQ4QTP3iHCGoOG68-K7Iu4DDQnMQhq5Du83BjAkQj0uzE_gjbDuQ9zLoDCrTUpNxEeGCX3POfn5yBFQwsUb9h7dg6Mjr6w6Q3smMN6l5sWRz9VCJ_Z5vVGu4A1Rez5I9_UF2Kyvm_OSxPH1Ed5iw9jBWLN_D40xh2Y8v-WW-eAbWXevg-K1Zyxdz2T5NtoDYlfM8T8iR88-WLO7iDTMvQLjiOYnrinfvzH9UzOAqueYudcZpUkz0jrrZXHDNFXVAtifBmXNVB21gLckEVH2ZeKS81cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/74979" target="_blank">📅 13:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دریک تو آلبومش: ایسپ راکی، ریانا، بچه ی ایسپ و ریانا، کندریک لامار، دی‌جی خالد، پلی بوی کارتی، جی‌زی، لبران جیمز و پسرش رو دیس کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/74978" target="_blank">📅 12:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">از سیاست چخبر؟
دریک تو آلبوم آیس‌من خایه مالی فلسطینو کرد، خایه مالی ایرانو کرد، خایه مالی کانادا رو هم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/74977" target="_blank">📅 12:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جمهوری اسلامی به مناسبت سه تا آلبوم جدید دریک در سه موج به مقر های گروه های کرد عراق حمله پهپادی و موشکی کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/74976" target="_blank">📅 12:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/74975" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۳۰ اردیبهشت پوتین به چین میره و با رئیس جمهور این کشور دیدار میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/74973" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بخاطر آلبوما امروز دریک اسپاتیفای بخاطر هجوم مردم چندبار از دسترس خارج شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/74972" target="_blank">📅 11:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قیمت اشتراکشم نسبت به شرایط اقتصادی هر کشور تعیین میکنن، اگه تو ایران آزاد بود و قیمت براش تعیین میکردن احتمالا ماهانه زیر ۱۰ دلار میفتاد</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/74971" target="_blank">📅 11:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قیمت جهانی دیش مینی استارلینک شده ۲۰۰ دلار  تو ایران چنده؟ زیر ۳ هزار دلار پیدا نمیکنی  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/74970" target="_blank">📅 11:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR_8bgiv3WXop5wForW4ahyF3kSQQ5qug_NzRn7YB65TFcIQVnaTH9s7CMQKkOM1AS9-vBuCZwuUJeXHxxySuofFEtcD7Cp2RdJSPvVoKZCHyZueUpCpTYqSlxuE1h8ULeBHan2qi8zFCHfEDOfuwqVD3cnAKJxsvKqPnMRc-DKrt9blBROPjskBmXohQzf7r5nJmcGMHSWAcl94ji6_63CHFqep8Du8HkkkKLyxqlGI0s8CXyxVwmO47rTabzMYyj5QW-YRgLc1g8uB2Lyxj7FxkzCmItGNir0fITrGNE20gFWrx8ookQX2dCd29nIETAI2B5VQCvUlQ7HZU-PpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی دیش مینی استارلینک شده ۲۰۰ دلار
تو ایران چنده؟ زیر ۳ هزار دلار پیدا نمیکنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/funhiphop/74969" target="_blank">📅 11:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMEjYocqbbcdopZNcAj_5NrnOnEapt0acapay66anEeKwLDIpNbGs3wxJU88Q1GjHsvweXONPiBGbfu9Br9SKYv4xs48fhRydwwEuKv8DJvOXeGArXZMtpASlGtPc4_Tf_1a9nPBgws_EsHf0h-j1gmrJZ25PJsXwPt5vZr74Lmq6kGFtZB5EJsL2LRkbF9ytmqkzYHsaCDS2tD4EjYU3u_pl04X43uH-1JPqiZ8t4alw-oXcXPPPEIvo-RGKvubM_HisRmfhGMVRm13p8274FsrTf_DeboPzSNO8T3POSnky2VDRLa9YAbmCTsdwXvsnsdB6pgyhWVbREknpw5T6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دختره تا دیروز توییت میزد رضا پهلوی کنار بیت رهبری میخواد فراخوان بده
بعد الان همین دختره فهمید ولی شما نه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/funhiphop/74963" target="_blank">📅 10:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBM9-dcq2da00smaKf9UXXqxhafQdj8Qjb7cGxcbWp7w_KMTx8mgWWqSZioYo1JQIMvIEqGIFOwpclmZbiyBtPtm671VqRPuJ3kdfi_H7yryacqmlw9YoTQxMCQBXGAlTUBS5b7mFqYVbn0LV9F9xbBvqsRQxGMCznT9o2z-BjcxQlsKnq7LuZv0wWDL7W8xIPV_mkRgbWagNWf6of33CpOUuFi4IIeGo4AzS5IhlRZbc_EwgzBbD4S3roSvi8vMXRZ3GFYIQ3mEbg8uKskphB-bZGMfGioQgAXJvtQ22ORZTV2FVbrT6oXBfNbDSJalaHBSY8vd8mBl_hmM1TWcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title: Habibti
🛑
Featured: PartyNextDoor, SeXxy Red
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/74962" target="_blank">📅 10:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7omm4lx3DENnmjNg9U7RfzfMtNPxWJWvCTjMYRQZ-4GM10owXCfnllr1vk7Iq3h1hBE1BTiIGnpEEQ2WQ-2w0tGtsCRhvpBmHPrsOyidHdubd8XSDf_RQlR6LxFnNT6Y4TmCOf6IhJU8uBhMGxtAH6vAX05Omovi1O7iJd5prWHIS8EeW2eLps0EEjrlOOIhLOZlJFBB1q156VGfd4DjIyOU02TeySqUj_jPVkbi7Oe33fivF1843xGIzAG1e9NInkydfobY13ehvDwQCsUKyzam4Xpi69BR-Dm7YJLPjlo3HikketnwulwZTNl1s6enBURKe8SiQbCjt4EFt1yQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
Maid Of Honour
🛑
Featured: Central Cee, Sexxy Red
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/74961" target="_blank">📅 10:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNORIM5slDZjXML6F8mq-NH198T43B_JcpIOS8oTfvobYPRJL6YXp1gODJo_N9xFT1_HuaP2KaEzzv917kCXz8v90ND6uZJG5pWBHaYZwtSdvVuIPl7LMKhqLeheQFhhjzJ-0qNd5sXVVtaPMIY1RnGFSZD7bGp0glF-6xY9-ru2MO9YzYLsS3J8CVt2LsABu9L2yH9aURXPQuf_py3zAshHpSS-5bMvxI7Upna1wuyb2Vu_LfYasnZXkyfK79eQRV6LmvTvoy3NokVHtLy6hA_hXFP97WHBINe4YGnctAUE1CiYC3-maSH_4P-ceceGAGptSntkARym-OVd1nGy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
ICEMAN
🛑
Featured:
Future, 21Savage
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/74955" target="_blank">📅 10:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/74954" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2d7d91b2.mp4?token=nIO-S0qKhOYFpPeHXSPvnxVDkF2L0rAYXqiIR1xvBae7WUu0FiaAEWfxhBg9XcgAivoOIWtuvvJy45Odh3dOgHXVa7r5nPbQ-tWbhz4cSW_6zjm0Pk9_CsM4EvF_n9ePZHUeoWygPnPYnabHxUPOMOz_0j5aFQPVbl7kkz9pWDdAgMaPJI1M_ltreVrB9gYpEx-0U0Ygxw-4gKWtPDYJi-S6tEf0xzSjvHFXx3M-NhWT4sEHhkvSMns-BRoFSlSNI8GS4sqwHJ-w-DuAnBd3mgrO_RMFb_Ygg7Xgk-LZ9Y5G9LT0wbRfx6YrRDvbEvkMBipchjUcDzXNBdKM8ab1RYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2d7d91b2.mp4?token=nIO-S0qKhOYFpPeHXSPvnxVDkF2L0rAYXqiIR1xvBae7WUu0FiaAEWfxhBg9XcgAivoOIWtuvvJy45Odh3dOgHXVa7r5nPbQ-tWbhz4cSW_6zjm0Pk9_CsM4EvF_n9ePZHUeoWygPnPYnabHxUPOMOz_0j5aFQPVbl7kkz9pWDdAgMaPJI1M_ltreVrB9gYpEx-0U0Ygxw-4gKWtPDYJi-S6tEf0xzSjvHFXx3M-NhWT4sEHhkvSMns-BRoFSlSNI8GS4sqwHJ-w-DuAnBd3mgrO_RMFb_Ygg7Xgk-LZ9Y5G9LT0wbRfx6YrRDvbEvkMBipchjUcDzXNBdKM8ab1RYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتما ببینید بلکه عاقل شدید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/funhiphop/74950" target="_blank">📅 09:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74949">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دریک همزمان سه تا آلبوم ریلیز کرد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/74949" target="_blank">📅 08:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توییترو باز کردم دیدم یکی توییت زده اپ شیر خورشید رو گارد جاویدان ساخته، بستمش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74948" target="_blank">📅 08:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74947">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توییترو باز کردم دیدم یکی توییت زده اپ شیر خورشید رو گارد جاویدان ساخته، بستمش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/74947" target="_blank">📅 08:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74946">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzOil4jwcCs0HH3PBJUJyOxBLhHo0d7DpQj2o89rcDQ8fYezAK--z2m2lOqrO9YZV4qz5XrI8wnoAzLdf1W24p1VDaKufR44I0CtrQdU6cVDEAguxER3TXu-7tgFAllTkX8F8RgHPtm_LztzwEMwzpCBS2r3y_5vlmL68SzWCXXhbFJthIQIkKQ2PZx90___Uy5gFvh9EcUINC3XYdiKK-QWkGJ1jRY21pNpVYjcB3kdPSivYc8eBF4qBGLE1l0UPbGilegx4bgHJskxCL3nmAn7q0HNchARj0-Fv-b_RXHrWyn20IpZtSN0sjgXUybvXd4521I2K55TVGU6o1i-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗿
وزارت امور خارجه آمریکا
اعلام کرد که در اواخر ماه آوریل، ونزوئلا
بیش از ۷۳۴۰ کیلوگرم اورانیوم با غنای بالا
را از راکتور هسته‌ای RV-1 در منطقه آلتوس
میراندینوس
به مرکز
ساوانا
ریور در
کارولینای
جنوبی
آمریکا
منتقل کرده است.
این محموله اورانیوم با یک کشتی
بریتانیایی
جابه‌جا شد و آژانس بین‌المللی انرژی اتمی نیز ضمن نظارت بر تمام مراحل،
حمایت‌های فنی لازم را ارائه داد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/74946" target="_blank">📅 06:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74945">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😠
دونالد ترامپ
فکر نمی‌کنم گرفتن این اورانیوم جز از جنبه تبلیغاتی ضرورتی داشته باشد. به نظرم این کار بیشتر برای رسانه‌های دروغ‌پرداز مهم است. من همان کسی هستم که گفتم اورانیوم را پس می‌گیریم و
حتماً هم این کار را خواهیم کرد
.
ما کاملاً چشممان به آن است و زیر نظرش داریم.
به آن‌ها گفتم اگر بخواهند نیرویی به آنجا بفرستند تا شانسی برای خارج کردنش امتحان کنند، یا اگر ببینم کسی دارد تلاشی می‌کند،
فقط با چند تا بمب آنجا را می‌زنیم
و همه‌چیز تمام می‌شود؛
آن‌ها جرأت این کار را نخواهند داشت.
ما در آن سه سایت، ۲۴ ساعته با نُه دوربین همه چیز را کنترل می‌کنیم.
راستش را بخواهید،
اگر اورانیوم را بگیریم خودم هم حس بهتری دارم
، اما معتقدم این کار بیشتر از هر چیز دیگری جنبه تبلیغاتی و رسانه‌ای دارد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/74945" target="_blank">📅 05:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">😠
دونالد
ترامپ
به نظرم آن‌ها اتفاقاً از خیلی جهات خیلی منطقی‌تر شده‌اند. از آن رده‌بالایی‌ها و رده‌دومی‌هایی که دیگر بین‌مان نیستند، باهوش‌ترند.»
هنیتی:
پس چرا مدام شل‌کن‌سفت‌کن در می‌آورند؟
یک توافقی می‌کنند و بعد فردایش زیرش می‌زنند... مثلاً ما پنج روز منتظر نامه‌ای ماندیم که باید یک‌ساعته می‌رسید.
داخل کشورشان بدجوری به هم ریخته و آشفته است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/funhiphop/74944" target="_blank">📅 05:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤑
دونالد ترامپ
در حال حاضر، هیچ نفتی از جزیره خارگ صادر نمی‌شود؛ هیچی، صفر.
مردم دارند جاهای دیگری را برای خرید نفت پیدا می‌کنند، مثلاً تگزاس. بنابراین، نمی‌خواهم بگویم که داریم ثروت هنگفتی به جیب می‌زنیم. اگر این را بگویم، آن‌ها می‌گویند: «اوه، او آدم‌های معمولی (قشر ضعیف) را فراموش کرده است.»
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74943" target="_blank">📅 05:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صحبت ها مقداری زیاد هست
بابت حجم زیاد مسیج ها پوزش مطلبم
❤️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/74942" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">😠
دونالد ترامپ
من به شی جین‌پینگ گفتم شما نیازی ندارید که ایران سلاح هسته‌ای داشته باشد.
هانیتی: او چه جوابی داد؟
🤨
ترامپ: او خیلی واکنش نشان نمی‌دهد. آدم بسیار خونسردی است. قرار نیست بگوید «بله، حرف خوبی زدی».
هانیتی: فکر می‌کنید موافق بود؟
ترامپ:
فکر می‌کنم بله.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/74941" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">😠
در ادامه
مجری فاکس نیوز، هانیتی: فکر می‌کنید شی جین‌پینگ و چین توانایی تاثیرگذاری روی ایران را دارند؟ با توجه به اینکه چین یکی از بزرگ‌ترین خریداران نفت ایران است؟
ترامپ: احتمالاً… ببینید، او با تهدید و جنگ وارد نمی‌شود. تا الان خیلی خوب عمل کرده است.
هانیتی: منظورم تاثیرگذاری بود…
ترامپ:
آن‌ها می‌خواهند از آمریکا نفت بخرند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/74940" target="_blank">📅 05:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">😠
دونالد ترامپ
امیدوارم ایران این حرف‌ها را ببیند.
ما
دقیقاً
می‌دانیم چه چیزهایی مستقر کرده‌اند.
آن‌ها یک فرصت کوتاه پیدا کردند و حالا سعی می‌کنند دوباره بعضی تجهیزات را
جمع‌آوری
کنند. چند
موشک را هم از زیر زمین بیرون آورده‌اند
، اما همه این‌ها در عرض یک روز از بین خواهد رفت.
تمام کارهایی که طی چهار هفته گذشته انجام داده‌اند،
در یک روز نابود می‌شود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/74939" target="_blank">📅 05:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😠
دونالد ترامپ
جنگ ویتنام ۱۹ سال طول کشید. فکر می‌کنم جنگ عراق هم حدود ۱۰ سال بود… در ویتنام هزاران نفر کشته شدند. اما متأسفانه در این دو جنگ، ما ۱۳ نفر را از دست دادیم.
13 نفر در مقایسه با 75 هزار نفر و یا حتی 50 هزار نفر.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/74938" target="_blank">📅 05:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">😠
دونالد ترامپ
قیمت نفت نسبت به چیزی که بیشتر مردم، حتی خود من، انتظار داشتیم خیلی کم افزایش پیدا کرد.
😶
فکر می‌کردیم بیشتر بالا برود، اما برای یک دوره کوتاه این موضوع قابل قبول بود؛ چون ما نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/funhiphop/74937" target="_blank">📅 05:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😠
دونالد ترامپ
اگر بایدن به چین می‌رفت، حتی فکر هم نمی‌کنم می‌توانست با رئیس‌جمهور چین دیدار کند.
من فکر می‌کنم شی جین‌پینگ آدمی گرم و محترم است، اما کاملاً روی کار تمرکز دارد. اهل بازی و حرف‌های حاشیه‌ای نیست؛ درباره آب‌وهوا یا چیزهای بی‌اهمیت صحبت نمی‌کند و من این ویژگی را دوست دارم.
اگر قرار بود برای نقش رهبر چین در یک فیلم بازیگر انتخاب کنند، دقیقاً باید کسی شبیه او را پیدا می‌کردند. واقعاً فردی مثل او کم پیدا می‌شود؛ مخصوصاً با آن شخصیت و قد بلندش.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/74936" target="_blank">📅 05:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm_Tyfbn5GTY-zQi7bIksh9BWNINpEAnFw9dzfqPn-uEvodh_dWyQEnTM6_NeKVfke-UvsBu_r-gGrP4VigkJB8Bh7p7mm7rUoYo3YyYlseg3xaSFDK7jl5a8mlTUuK8ofDrWdCJaiRn9ZNq-ADhRm0-FJ9Q8op0p5IBgMj6ZzMlW7nae4mPsMudbRyWsn5H-jtWYHDwRoV6S5sVAk9CKcajxpb8lGXdbhk7iNIi7xa1rnXGKu2nSO3ax3pO57QycGdd32b6i-87HTinnGAoDSMjMPaEvU2RAJZnq6MZY3a0L9cxnQBowLNODMGRyzVCV9hZaXFYvq08DP7zYT4Hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.  الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/74935" target="_blank">📅 04:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در حال آماده‌سازی برای احتمال جنگی تازه با ایران پس از سفر رئیس‌جمهور ترامپ به چین است.
مقامات اسرائیلی تخمین می‌زنند که پنجره احتمالی برای اقدام نظامی آمریکا ممکن است از فردا آغاز شده و تا شروع جام جهانی ادامه یابد، و انتظار می‌رود ارتش اسرائیل در صورت از سرگیری درگیری‌ها درگیر شود.
هنوز نشانه قطعی وجود ندارد که رئیس‌جمهور ترامپ تصمیم نهایی را گرفته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/74934" target="_blank">📅 03:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74933">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ابی ناموسا تو دیگه چرا</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/74933" target="_blank">📅 02:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74932">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بابک زنجانی یا همون ایلان ماسک ایرانی
🔜
یه زیر ساخت بومی بلاکچین ( ارز دیحیتال ) برای اپلیکیشن خودش یا همون
پیامرسان دات
وان تاسیس کرده.
مثال
: پاول هم برای
تلگرام
اومده
تون
و تاسیس کرده.
البته با این تفاوت که تون یک سیستم بلاکچین معتبر و زنجیره وار درون قلب سیستم بلاکچین جهانی هست و بر خلاف پروژه بابک زنجانی یک چیز معتبر هست!
پروژه بابک زنجانی و حتی نمیشه جایی پیگیری کرد که ببینی معتبر هست یا نیست
که به نوبه خودش بسیار بسیار جالب هست.
خوب حالا اگه یادتون باشه با اون حرکت
توییتر
و حذف شدن
تیک
مقامات
, بابک زنجانی اومد گفت که دیگه چنین وضعی و تحمل نمیکنه و میره سراغ اینکه اپلیکیشن خودشو بیاد تاسیس کنه و خوب تیک ابی کسی و هم حذف نمیکنه و از قوانین
دموکراسی
پیروی میکنه.
این وسط یک چیزی که
شفاف نیست
این هست که ایشون میخواد یک
شبکه بلاکچینی بزرگ با ظرفیت 90 میلیون ایرانی
بسازه ولی در صورتی که بزرگترین خزانه داری کل روی کره زمین که تو آمریکا هست ایشون و به
پولشویی و همکاری با سپاه پاسداران انقلاب اسلامی
متهم کرده و چند وقت پیش هم کامل این شخص توی
لیست تحریم های کشور آمریکا
قرار گرفته.
تا اینجا اگه خوندی دمت گرم باقیشو هم بخون که مطلع بشی
❤️‍🔥
حالا اپلیکیشن دات وان چیه؟
🤨
یه اپلیکیشن شبیه اینستاگرام هست که مثل تلگرام یه ارز دیجیتال مخصوص به خودشو داره که با تولید محتوا و فعالیت بهت از اون ارز دیجیتاله میده و تو عملا میتونی توی این پیامرسان کسب درآمد کنی.
این اپلیکیشن با اینترنت ملی بالا میاد و یک ترافیک نیم بهارو هم شامل میشه
بدین شکل که شما اگه 10 گیگ بگیری 20 گیگشو میتونی تو اپ بابک جون مصرف کنی و حتی درآمد زایی هم داشته باشی.
البته اینو تا یادم نرفته بگم که این پیامرسان تضمین 100% بابت این داده که
تحت هر شرایطی کاربر هاشو آنلاین نگه میداره و نمیزاره کسی از اینترنت و فضای آزاد و شفاف دات وان دور بمونه!
😶
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/74932" target="_blank">📅 02:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بابک زنجانی یه پروژه کریپتویی داره با همون پیامرسانش ( دات وان ) میاره بالا که به شدت مشکوک هست
اطلاعات تکمیلیشو حتما اینجا قرار میدم براتون
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/74927" target="_blank">📅 01:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74925">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ
رییس جمهور چین برای مدت کوتاهی بهم گفت نابغه
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/74925" target="_blank">📅 01:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74924">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/74924" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74923">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUxIlsXsatuwBs69iOi62k0Sm7df-J2AAFL9Grp8LpmbUWUXmzYeHSjcj3Xe7IPl-z8DpaBtbMTexyTXrv1d67uj9DWLV48Co6R59dFXgspt688eO9RIOFVuWsH-dDjl_0oMB6nYQvrqF6rVK2npqWpH9p3ZTnYhV3Qi-dzVlt94Ho9TaguJPeZYiXkkEWpP4CBpCTQp_PgLesZ7z2CG5hHdynOAWUKOOz2g77a53n6tutvK5Wy6l9Xpilx6_dPr-2VMkYpxpvAb8YnWg1bT7KpydgGlvLFDRLKlUXx4TtSnaVP3OHWbhfA86pnaPSp5kfGMaG35-YdCEcbovdvkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار بورس اوراق بهادار تهران در ۷۵ امین روز بسته بودنش رکورد تاریخی‌ای را شکست و با ۲۰ درصد رشد، قله‌ی جدیدی را در تاریخ کشورمان ثبت کرد.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/74923" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74922">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فاکس‌نیوز:
ترامپ و همراهانش از ترس اینکه مبادا چینیا لپتاپ و گوشی‌هاشونو هک کنن یا نرم‌افزار جاسوسی روشون نصب کنن، همگی از گوشی و لپتاپ‌های جایگزین برای سفر به چین استفاده کردن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/74922" target="_blank">📅 00:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74921">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی‌بی‌اس:
رئیس سازمان CIA امروز تو هاوانای کوبا حضور داشته و با اعضای دولت این کشور مذاکره کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/74921" target="_blank">📅 00:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کان نیوز:
اسرائیل معتقد است که رئیس‌جمهور ترامپ پس از بازگشت از چین در پایان هفته درباره آینده جنگ ایران تصمیم خواهد گرفت.
مقامات اسرائیلی می‌گویند گزینه‌های اصلی مورد بحث، از سرگیری درگیری‌ها یا از سرگیری عملیات نظامی در تنگه هرمز تحت «پروژه آزادی» است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/74920" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/74918" target="_blank">📅 23:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میگم مگه مجلس تعطیل شده؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74917" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: کوبا بعدیه.  اوه، لطفاً وانمود کنید که من این را نگفتم، لطفاً.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/74916" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی: پیش بینی کردیم که هرکس که ترامپ رو به هلاکت برسونه، 50 میلیون یورو پاداش دریافت کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74915" target="_blank">📅 23:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستان این رفیقمون که چند روزه تبلیغشو میزاریم تا حالا هیچ شاکی ای نداشته، اگه نیاز به کانفیگ دارید بهش پیام بدید ازش تهیه کنید با قیمت خوب
ایدیش برای خرید
@r_downey_jr
ایدی چنلش
@suii_vpn</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/funhiphop/74914" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کان نیوز به نقل از دو منبع اسرائیلی و آمریکایی:
تو هفته اخیر جلسه مهمی بین ارتش اسرائیل و سنتکام برگزار شده و همه منتظر تصمیم ترامپ بعد از پایان سفرش به چین هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/74911" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ی زمان اینجا پست جهاد خامنه ای علیه کشور های بیگانه ۶۰۰ تا ری‌اکشن قلب می‌گرفت
یادش بخیر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74910" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
