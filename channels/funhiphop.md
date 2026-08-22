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
<img src="https://cdn4.telesco.pe/file/arCAShy06VdqPrHH3UjHBF737GlIA4sWqjwjjYawJ1N6D477FoSOyRCCuW05ZYSCjAPLmZ6Kz8FxrmSX_7YKerlJN34CyQ5-AZTz5jNRpK-BbOjjgnyQEx6sU-cLVZIbgxoXD3ywUJez_Vr7nQUIyYsODyJ760JjXXnc_paqcw7FfUsvrO_FUL8tdlsOLICE5a5BZxJVdr53DardWax50nBtWPIeud3fxcuWTFMd3NebKwxYBHFNXlv7TiVE_49HElyZk0H3cbO0qmon0rxB2bwLH6yT9KOiM-pkJPewK3X0juNd2wjE0vZAoBPSDzsS4RhCfwAYhTumDrKHTlMM8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 22:25:11</div>
<hr>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txNCDVNKUZ87_FR24z7iacSla-QM6JDAVT4bOi2p3Jn0cyGAvhOE1EoBYQkQ__oRaN-zONLc-7Z-ivMwROubAc0xQnHAnZrq1gpwUqdF2pa6V8xxxxMIpugfq2cDhnmr5bld5sMaejlIs5XTTf9jHTFdBk-SNIQKUeSMuqcs42gv71yoH83t0hYE5S8T3HkIaVwZ3_gnrsP22baXglGIWpe5ehCNyBO_Nr6EMAVaX5cphOeO7OROp1g91xFBZ7d5qtWpUsDPDBfh0dhBZROHjuhbBVmZW0_xRMyabsiUNl_GUocgUcd9S9EYINh7W1GUUgy1MasR1fyfAX3r5BqYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه برا خودت ارزش قائلی از تلگرام دور بمون دادا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/funhiphop/82470" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان که با کد تخفیف (
bakei
) میتونید تا 20 درصد تخفیف بگیرید
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/funhiphop/82469" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdjFnmJdKMd_aHU4mJYwaGicZbhfIf8S63favHHZPpfh1d6DtKRQdZU6x9wrOpZGr9seIfoUhJmQ-CMd4_GEf-FLhbBr1MxA0PtcdsRlmJpVvalBSMiqwU89q6GpVvWy82DDJGBl8w2JEmswHLH-HfFa4PoDJnCeo-bg9Ddt24TiGT_OxgP-JFFZ0FspHh3qC1aQ6IdHOqkOiVeHSG5UI492uk7y60hC2SGMNgvxS9J_tpan7tuSdUzD7Fy0rApXB_KXUARZcqFHq0XPhjaSx_r-dgAY6ru2MZ83LgdJjQHqfRouKNHR2TMmTCKrEScCYVx3hAlRFKvTBKlkV_kVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتنهام چقد پلشته، با اینهمه خرج بازم گوهی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/82468" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/82467" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82466">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/82466" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPj3M0FypASU5Q2ir9lz6_iXvY-YqM3oSb5BOnyUUn5BV_Ua830bPQ1xg9cdOrV0hXVlaQWqb273GDNVPYwQGkRzBxCtb7tXmDYH0NrPhGXJpKEIhEyZ9y_OkS-WpUpAxBM7VZlNzKuE1GEfekWAjxy8XjMlSVxaRtiFvRK2lp90DqQS3yN9SUe8hlmT7Va4Uo62QmH-tr4Ons9QDMLtbwKjsUYwHDDr25sT_XrHvKdQl5bxcjSdxkr7ef6gOfu18WS76wRhA9zyPdD9pKQpKjdUmaLNCGjPKdMU3FxX4azE2HujGgj6r0lxZh0HP8gCHePgEKjuBI_94-cgvrIV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/funhiphop/82465" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=XandRmKg0U4CpUeTc4_n14PS7LUaP8FHW0eYlt46WHem89WXLnFTGQ3n65YuLHtQg8_LfCSA0-Kbyon4ZNZ0o40zIOSII76zTDuZblSDZ24oCCMdBmYua7hfi6f4kEl0jgLGimmf34KyRKhpGyBH4IQIf4R_3X9Rx60-MAkRmG5y1Rutye-40IKs7J8quxJQWh64EGCYMDg3TYQxAv0XtdZnpyWxsUO_az-6cxLvUGWBRZ9Stk8SUMfRBlmM9jSyMsfFk4QCupC-Vqjq6ZVzal10_0MRZOkx69DMKGSP59l7vqRD5dRNBMg6idTod3Ysjo2-Y6kxnKRmGTrFH-y2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=XandRmKg0U4CpUeTc4_n14PS7LUaP8FHW0eYlt46WHem89WXLnFTGQ3n65YuLHtQg8_LfCSA0-Kbyon4ZNZ0o40zIOSII76zTDuZblSDZ24oCCMdBmYua7hfi6f4kEl0jgLGimmf34KyRKhpGyBH4IQIf4R_3X9Rx60-MAkRmG5y1Rutye-40IKs7J8quxJQWh64EGCYMDg3TYQxAv0XtdZnpyWxsUO_az-6cxLvUGWBRZ9Stk8SUMfRBlmM9jSyMsfFk4QCupC-Vqjq6ZVzal10_0MRZOkx69DMKGSP59l7vqRD5dRNBMg6idTod3Ysjo2-Y6kxnKRmGTrFH-y2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرمال ترین حرکت پسرا تو جمع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/82464" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sufs7RPBV7DVzd5VgEPPSw9Z8-WF6JfVIH5jy3hCUvOEcHZeiKEl0pTbAmfazMJD8Hp7m1DATfil-_mrPxl5S0QsGTaU2lXRezFV4AXdZGDJmzxbVZnA71b8tctxCBOp8CtRspU2Wq84oRtNedyBRCwmAuLXOWFrSJFmu_EycJybuC0QzV3ioqZUNdcLZiQu4HFJwCiO_uYYZQlvD3E1YiLenFIyddHmDR61VgiK4FYC8YCLOjdRoS3tQcPleQuk6uD3CS41iGOHnfSM31R3PI9OBPwCq9yGxCV2M_ekcjpoLisl_S1ONaew1JXFMXgP0hJLQHBdDAAHH9Pp_Ku-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم برا گیر کردن سوزن حافظه‌ی تاریخی رو رضا پیشرو، دو تا کلیه‌هام رو بدم تا قبل از مرگ بهترین محتواهای تاریخ بشریت رو تجربه کرده باشم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/82463" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB9rHhKUomj3gTygM2HgSSPRx9YAWTQv0VXbhcRUJiIx12-KLwITThcXHmSe60e_TCyFts9OgGiL5q7fbyM6RVZfwasFXAGImGLdnKQsBpdVdW-zen_K8VyUyvbMAEwr55200BxLcqwHaJYeNgsGUj3dU0ZP6teu_dutnGa-D3sk63l4Z7LhNlfknTkRQygu-gbUIZHZyYY43gtNC7NTuZ_F_f2Cfimox4r3QxoN6OgCh0yCSrQKyFxhXy_THuUF4ySDA3Ao2K7GV8nG0c5bINRrjnlPBeSo303j6hk6eSenqcwrPfQVh1XriibOo04QE2yRKLbaD5J8LAB8IJxvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به رضا پهلوی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82462" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li_YFka3JGLOErd2JvarQZ9T8efhx0pLIFznq3j6QXHuRM5j4IXfrxT7un-bkRwsN_6WzIpJsoWXpfyX9qoe-5wnzq7QlWmoIj_1TP7CY4c0gJBotB5qVUf5xCN0GvdMncRknBmjtMYm4_QGGeNGdjVRAL33rFHu7i2iBtp01823xR13cObTyLRaVrpG1nRcig_zmqjlUDVMi8bDD29zou2WpoXP1FruDypuGHtmGp4vW0blGGC-BjVusxkECTMnmM9AL-qw5iFx89RZz4JvNVoRDCcKe9LA70YKNRWMYTFZvgqla-oxk-V8ZpK9-ti77NeHPA1qUMggKKS2-2VxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بروسیا دورتموند
🇩🇪
-
🇩🇪
بایرن مونیخ
🏆
فینال سوپر جام آلمان
🇩🇪
🕔
شنبه ساعت ۲۲:۰۰
🏟
ورزشگاه سیگنال ایدونا پارک
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
دورتموند در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
✅
بایرن در ۱۰
دیدار اخیر خود، ۸ برد و ۱ تساوی کسب کرده و در ۱ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر دورتموند ۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر بایرن ۴.۶ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g31
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/82461" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=Wpek8DI9BOpydpoIX_A2aJfsCJnPoEk5e-3H36bukS8JTuZjLa8hjkZG82Mts_MqF58RX1Y65yxnQk77D7iosUNXYRb_VPWwj3HpPxEhofihmfGIwZtRiZs919wlgm8rjRQFyiqk3262iKXRQM6OzzAEtdVZHT8ataILZ355my02bYnAAdtyKiUyybzqBodqpCYDkzFfTtZu_m1D6h5QC6h4eVtfeQ4m7IP2BMsLu-ckvv_ewW2IBiCP9Hgl4BTOW34NSocWv4U7kM_lQG00tjaiQ9lAhdB2W_9DSWIDqPvCdZa6ojs9BiVrKwLnfuIFBAaCod0BOb8p_KrdD_aDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=Wpek8DI9BOpydpoIX_A2aJfsCJnPoEk5e-3H36bukS8JTuZjLa8hjkZG82Mts_MqF58RX1Y65yxnQk77D7iosUNXYRb_VPWwj3HpPxEhofihmfGIwZtRiZs919wlgm8rjRQFyiqk3262iKXRQM6OzzAEtdVZHT8ataILZ355my02bYnAAdtyKiUyybzqBodqpCYDkzFfTtZu_m1D6h5QC6h4eVtfeQ4m7IP2BMsLu-ckvv_ewW2IBiCP9Hgl4BTOW34NSocWv4U7kM_lQG00tjaiQ9lAhdB2W_9DSWIDqPvCdZa6ojs9BiVrKwLnfuIFBAaCod0BOb8p_KrdD_aDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وطندار عربستانی اولین موزیک رسمی خودشو منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82460" target="_blank">📅 16:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9Rm357HFoGJJX6gSQfzDaBDbFIwDWGqVro8_RJg4uIbjbIPnmfOCCo3cB4iEmMsyndlZHFKba8COxtZpCz9xBY1wAgt5TsZ_w_T5WHK_brj0Jws8wzL0ljuK_NIAhNDiucsZzGBBOTdHkfHbkyEi0Nk-vi27vVa6MulDNrR0IBZwO0bevX7tFYN1iMuN7-4KlW26TLSNt_EzYfxcm8fIE6YQCCLvXiZVCYaXVm4-lalXaPNuNbgKmFKKoPMDhtZ7E6P6VwkR8xIi3jgh51mXTMsxAM0dyzaT0h_ak9aTE7oNS7mW80hK3qcBPFznXS-cPRN8HD2DVNXsk8_px0Jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدسامتینگشاه:
تو چند وقت اخیر کشورهای همسایه از ما خواهش و التماس کردن که باهاشون قرارداد دفاعی و نظامی ببندیم؛
چون براشون مثل روز روشن شده که وعده محافظت‌ها و قدرت آمریکا دروغی بیش نیست جوری که حتی اسرائیل رو هم تو خطر نابودی کامل انداختن؛
پس فقط یه قدرت مستقل و مقتدر مثل ما می‌تونه از صلح و کشورهای منطقه به صورت واقعی محافظت کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82459" target="_blank">📅 15:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsN67Jdgw5IE7Qjd627C6MJD_uRTcsRO6SekBSdLCtUj7tXySvTj9pOSpi7pyQZ421T9YiRXai1rKrtZwNcotMnh5yXhhglXM5-HMQvQDsg-86Pp6Nqr6eB6EvXNCu5d326uuUhu3YuEjJxcn1VU574bQ5QuUAZahjrqWLXXwv7SxR78rIp1rFSqUZ1KGMQfcuXh6JIRTpXJUYA-HC88PtjFo4Sa3oec7lkiosIsXatS6iwA6HktpqdP45mpVDjDLsrR1dJa7UssspK-nYJVbFedLFkX71pHWSC0yVoiILvlf1zxjxjCyttP68X0CVDfo-V0F2ProlXhOQYQf2IfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این دالگ شامپانزه رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82458" target="_blank">📅 15:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=PFMxFThodwSG-7ZeMUgiNLbJvM-3xg5_H4rdgcYCTbtVfes8Qqi_-TOUFadK7QPLMtfQj2Q9-7Y9E9r3bY2GmTYJS87MayYDMa-atf02NWcqRl0n2L-Ik8F0QW6Ik0Sms23fCYShwuPKdhyOROFpUyl2rA1RCuUKT2ydwgDZ7SZB35sSizglYBGHGPkvruepl4enQfE9sEA8HD9bq-V3srQJ6gGjUPsBJqKU5EiOrvPBbzLXTqSUI-GywLmyoEfH13gOTKkpp1MNqmyYndUHOPbMtYJqwx6Zv71yy9H-wL3bpUEm8bffQ2LGJLwv7RFOXMqx2C7ZfWP_-FZTdpznXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=PFMxFThodwSG-7ZeMUgiNLbJvM-3xg5_H4rdgcYCTbtVfes8Qqi_-TOUFadK7QPLMtfQj2Q9-7Y9E9r3bY2GmTYJS87MayYDMa-atf02NWcqRl0n2L-Ik8F0QW6Ik0Sms23fCYShwuPKdhyOROFpUyl2rA1RCuUKT2ydwgDZ7SZB35sSizglYBGHGPkvruepl4enQfE9sEA8HD9bq-V3srQJ6gGjUPsBJqKU5EiOrvPBbzLXTqSUI-GywLmyoEfH13gOTKkpp1MNqmyYndUHOPbMtYJqwx6Zv71yy9H-wL3bpUEm8bffQ2LGJLwv7RFOXMqx2C7ZfWP_-FZTdpznXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است  ده‌ها راننده کامیون تاکنون جان باخته‌اند  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82457" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIi4JLL6gZ2CBWhReuowZ4edzNHtPS_10xDoOb2gicMX3ly-jZTeKS-f4ahZkGDb9BPAa-MKumeigzmjE9S9t0e-vXsivWNCL0aALOismXrhShxNOZT-Kzie_bKA3rrTrpBjo3CdEUlC0myh_UynOnBrmCp_dH2hgLbYnymkOjDa_HvWyQAtzEH8utqYm94gCHl-l3EwryBMrYLkd1OiBD73H3mCzWVLoT0ezgMb5jEdU3qVUeaKUiQZ9lA4jfq5rn7BUG33YWpUf5iWBwDyUnQNdG4oh5pe7AQAgSpsFS_6W9_y9JcX4UK-UaqIyMCppZ3DLEmKvXhysfOv0vIwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم بعد از موفقیت ژانر «پشمام داریوش تبهکار بالاخره ترک کرد چقدر خوب شده»، الان وقتشه با ژانر ««پشمام رها وانتونز بالاخره غذا خورد چقدر خوب شده» چنلای رپی رو به دوران اوجشون برگردونیم.
#MFGA
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82456" target="_blank">📅 14:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp9vvesyTWl1vkje31tUlL4WHjwNJDBSojBbUNFIXB4iX0jWmwdhcyuRUg-whmpJGZhuar-dq_0pj09HDc3MxKCS1Cg3u9Vv7BDSHJxibgwAeLqc-Y3uWZqXU-lPhK5q37vs-0BHZtxmrFINCXOujv6IPn_Tym9CaQ2C23H2c24-3ibHWoJdw6uC0vtQxzVMbKOgXWsnjTYmFGjf3R33R0FaWDHTzM7qz0ck4ctd58kn9osOY8i7Bi0uJUS58meYib-mKdMcaWwH5SNQ1gZPJUNXtiPLaREtEOxVuFKePRU8YdmuOtq1-Cj-zAj-MS4LEcFL-6zBbHJmeB3uuWNiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مرحله‌ای از رپفارسی هستیم که خود رپرای مملکت به یه همچین فلاکتی افتادن بعد یه سریا جدی زیر کامنتای این چنل درخواست محتوای ۱۰۰ درصد رپی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82455" target="_blank">📅 14:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgee47piXkpexmyqGXRYAwM1xFVKzuCC_k9KCz6OC-icjK3-xQFOpbnga5rq7yF_nUawzF4AUR7eyEA0n5EPy3y-c5soe15v--uyot3hoKZSJSjOA_t5x4LGdQLbjCYFsN8LsHo87K2L2VxOkjRG-3uNYHvjfDQh5qEVyaICfYTvIffYXL9jbfCuAS2TQzGZS6AAV02lGeTlJInk-s65IU-lfXlk8o10VOrNgfmeZ16UWrwW3_qVGOOIjQPrc5d8KOdvxE_QqafCSGF0Qcw-GvSShC91KAUKSDsThIJi_Ln-LfE2VEK5HMiTTWxxijzGbdNsXcEJbC-zRMuIANZQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خو کصخلا چون عقایدش کیریه دلیل نمیشه هنر طرفم زیر سوال ببرید که.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82454" target="_blank">📅 12:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسطوره تاکتیک های ناشناخته ژنرال محسن گواردیولا: با ادامه محاصره دریایی، ممکن است از پیمان منع سلاح های هسته‌ای خارج شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82453" target="_blank">📅 12:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82451">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGOvMeBK2M3X8vUithTar3eG-el8ryxlu5KxztFWN-lk2hbzje5CSvc2yBsubYIcq6HHBE3IB4BpgCLHRgXNtI_Ux6VQjDX4LFgfd2rGrwiFMt30t_16DHZC7MlOZ5Wp_RTlYrwfKIizi0F6FyJ3moie_wJDA9Fgf5T5OCHM87mSu8hjxY3u3gIfa19-ZUyfNsMOnW2WJvurwB9VF9W-5jnoioDHfRG2N2e1a3-nPGFee_nZEA2k-ah3HRuRqsio_V1ByZIfmu7XZMfBDA48dWq9PJoDgn6-Q7vndRIYEmGQ0-lvkQGFIBFwEl2_L5EsTpz132mmf6HVohiBQySRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=fWga2uDSc-I8hLrVKmK0f-3OF3flvHGAhjXH-BblyBuNXRmJMj5PP0kyBJ4EN9ru3EwW8TQUpGnS3KFJPBQeo8WMoB6RXclnWM8HSgZ0Ti0WYcEgWY-r4LsZjsLqxcgVjfoi_Yw_LwdtwhRtyHjrV2I-ygLFS6Klmlz9bev_twHy78r3IDQXx41XGRRs0z3wifCrPh3IIgB8Y1qavfdN6gD52ylkrm5LiXelg9iL2LRTknLmGSZ1KzanT8Yn3FGb79UeYzhN-0FppLD--TJ68vG6SvwQhrfE1aTTmmRSIlKVF8SbeVBPPHPrKhO9uLVwSHcBCMgvfzXuFI50lqEcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=fWga2uDSc-I8hLrVKmK0f-3OF3flvHGAhjXH-BblyBuNXRmJMj5PP0kyBJ4EN9ru3EwW8TQUpGnS3KFJPBQeo8WMoB6RXclnWM8HSgZ0Ti0WYcEgWY-r4LsZjsLqxcgVjfoi_Yw_LwdtwhRtyHjrV2I-ygLFS6Klmlz9bev_twHy78r3IDQXx41XGRRs0z3wifCrPh3IIgB8Y1qavfdN6gD52ylkrm5LiXelg9iL2LRTknLmGSZ1KzanT8Yn3FGb79UeYzhN-0FppLD--TJ68vG6SvwQhrfE1aTTmmRSIlKVF8SbeVBPPHPrKhO9uLVwSHcBCMgvfzXuFI50lqEcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینا نامداری با حجاب رفته تو یه برنامه داخلی و مصاحبه کرده
تو یه قسمتشم داره میگه پوتک بهم پول داد که آلبومشو هایپ کنم، اینم واکنش پوتک به این حرفاشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82451" target="_blank">📅 11:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=NLNTUOOBaLzPXtSV0HqGmizZudYPeL8cwUBLDrCDCCfVzST2FEN-DpTMOZwe1BWC2cS_U-ZKNLCQYm0pGyAFlWuNhrnMZvIht2e8uXr4Z9xbES3b3nGEmORv_CizbtV8uIrKtFiOlV7zgHfPLf7xiBHeus569LyJThOIAxCY_mq6_lQW8Chwemcba38jUpeQalaYipDrquCFJiCXVFlPwfmh1ohXCtn0QZGcqD3rsewr-dsLErkn8ufDYjs0iWUnGGMEaD21DCsWXx7Xe07JqJ_Wx3LisojrobMaqGVIMHlUonR3QlKSRrSr_Nlc1iz-3m1TCJVDb2pgbXD8SknPAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=NLNTUOOBaLzPXtSV0HqGmizZudYPeL8cwUBLDrCDCCfVzST2FEN-DpTMOZwe1BWC2cS_U-ZKNLCQYm0pGyAFlWuNhrnMZvIht2e8uXr4Z9xbES3b3nGEmORv_CizbtV8uIrKtFiOlV7zgHfPLf7xiBHeus569LyJThOIAxCY_mq6_lQW8Chwemcba38jUpeQalaYipDrquCFJiCXVFlPwfmh1ohXCtn0QZGcqD3rsewr-dsLErkn8ufDYjs0iWUnGGMEaD21DCsWXx7Xe07JqJ_Wx3LisojrobMaqGVIMHlUonR3QlKSRrSr_Nlc1iz-3m1TCJVDb2pgbXD8SknPAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی اتوبان بابایی تهران، یه پسر داشت با پژو پارس لایی میکشید، که این شکلی بگا رفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82450" target="_blank">📅 11:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=fObHa0t0FKXAyk2w6eIVUIELSEkMYu02zx-KOb1a9OR9Whu0TR3jqpP7Mw_YHjEtXlopEfPrnK8LTWDYPFA5V9QTs8TQ3o5z3nqk0TOnWRI6PnGxrLezqT-eN6O2mHoOc3BCBJqYoEpCNqDz3hMl5HthIkzKhs-oKClT2PtiUnmu60R6rAFr0JCxwCINTn-Z0k48aT9Yn_8-lpCKokq8eZ94co2oS_ZhTRbBmQb_qdm2CBhTjVaE6nxV_gylBS321-wbnZKTa_Mv-08VqJ5GjXyK4LtYX32j4hjPO4v9SaOq9YQgFcFlaNayUiHE-sQOiophexNgVfuXNDZxfjx9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=fObHa0t0FKXAyk2w6eIVUIELSEkMYu02zx-KOb1a9OR9Whu0TR3jqpP7Mw_YHjEtXlopEfPrnK8LTWDYPFA5V9QTs8TQ3o5z3nqk0TOnWRI6PnGxrLezqT-eN6O2mHoOc3BCBJqYoEpCNqDz3hMl5HthIkzKhs-oKClT2PtiUnmu60R6rAFr0JCxwCINTn-Z0k48aT9Yn_8-lpCKokq8eZ94co2oS_ZhTRbBmQb_qdm2CBhTjVaE6nxV_gylBS321-wbnZKTa_Mv-08VqJ5GjXyK4LtYX32j4hjPO4v9SaOq9YQgFcFlaNayUiHE-sQOiophexNgVfuXNDZxfjx9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است
ده‌ها راننده کامیون تاکنون جان باخته‌اند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82449" target="_blank">📅 10:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82448">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxPlqmO2oWCgd1EQhfbmriGwMPh93RZX9eakZXLzVIfW89elEuXnKdrzfOIO81ePIxjYRXjpPclQqwKWrMVMksbj4e5WEIwYZbigJsrvitLZWrEhPJo1BC8h9VuUEOYgYBVFyYNub6CaNar2rPyFa8otHrskrmqHgd-quZGYeDpjHnmX0lTqxO0MnLxkEMCG7Siqrb3DxnSmyvPJSTzZjqj9IqvQJNvZ5G-0ebXvIsVQofpNZWGxnBHFqZIn7pIbzft2eo2Bzq7s7hqCu2ZWz24OIwXt5wqkeWp9m3NsbTxMLi5FB-8YOKt11B1R0eI8rhe6TuPiJ6fPuFq-2gnziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بروسیا دورتموند
🇩🇪
-
🇩🇪
بایرن مونیخ
🏆
فینال سوپر جام آلمان
🇩🇪
🕔
شنبه ساعت ۲۲:۰۰
🏟
ورزشگاه سیگنال ایدونا پارک
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
دورتموند در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
✅
بایرن در ۱۰
دیدار اخیر خود، ۸ برد و ۱ تساوی کسب کرده و در ۱ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر دورتموند ۳ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر بایرن ۴.۶ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r31
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82448" target="_blank">📅 10:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82447">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=DL9sAsf4jt3U0lw0aCuf8S1Nkto0JFFuPSOK493ZN_Va6dvV-nGWGDXsk0YTBQfqKemKeGOYXUOYhVLMN8dogHAplkBHpCk8zOudxM-ym6_1xsfW8WcdDxendxSwzgQTP8X6sKOYEq2o8zAPfTKZpvrWRrzdOWiZhOuF-4TJTnbZkH7hCf3exMMTHeMq0Bn9xdYmbx5AhGDR9ItfRTvwpQTVYKsLnEu3WhySmnOrsj6h9uMs3s9T9IrfZVpT6HBZg9IUmdqexbtO1-ZoIulIQDQfTDHU-IZxj3QgmjuIs44kJ5_awp1ZW0KOrtgG5ORionhzHwAn72HKgy7HPlIcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=DL9sAsf4jt3U0lw0aCuf8S1Nkto0JFFuPSOK493ZN_Va6dvV-nGWGDXsk0YTBQfqKemKeGOYXUOYhVLMN8dogHAplkBHpCk8zOudxM-ym6_1xsfW8WcdDxendxSwzgQTP8X6sKOYEq2o8zAPfTKZpvrWRrzdOWiZhOuF-4TJTnbZkH7hCf3exMMTHeMq0Bn9xdYmbx5AhGDR9ItfRTvwpQTVYKsLnEu3WhySmnOrsj6h9uMs3s9T9IrfZVpT6HBZg9IUmdqexbtO1-ZoIulIQDQfTDHU-IZxj3QgmjuIs44kJ5_awp1ZW0KOrtgG5ORionhzHwAn72HKgy7HPlIcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوید محمدزاده داره تمرین میکنه اعزام شه فلسطین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82447" target="_blank">📅 10:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این کصشرایی که عرشیاس و چارتا پاپ خون شبیه‌ به اون میخونن رو میبینم به رپفارسی امیدوار میشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82446" target="_blank">📅 01:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlDUPN4fJYYVNfLbB8b6mBFMZ-Juhko_cgoJz5HHGqY61gVzldgE9TUtB2A-7LlNeyoCRr2ZIHkS52G88Sg_b_pyuJalU8pogFecJRN_Qn1qqeEW3h2aif8wBHcIIx0F8O6e3yW0EL1KMxqPuXWcg4rekXCfVyeOdeEZFhIEku5q2rx1qsNH5mK3MAXLq_BfwT1hQebkoYzSa4onvdm6XgJdTTnwy5VgtCp-XNFVIwyei3QG2d2yOrRId4aZPrjYx7F7LrhuS_cOcLTrwcKDyDkR35Acq8bXsGiK88Avm-hpw-BkD86yn4UQ7VxFQDKqJFTxKLCgNBZ-r45L4AWJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوتا بدبخت رو نیمکت آرسنال تلف شدن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82445" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از ترند امشب جا نمونیم
صدای انفجار در امیرآباد، تهران
احتمالاً فعالیت پدافند هوایی
مرکز تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82444" target="_blank">📅 23:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrVoRiUEYY5w5QGIXS6bQjCtKwMP9Udlv0Aex2XL7lWcjrsKdn4FgeaHUZLixY_3hj2KGhg8MXKTwuG01T52qfi-JD8TkJJaAGDv5IoWUXpQk88A5rX9GQWCe2lS-VActEAi5m4SL7KUMItofaripj-I1fG3bhSbkx0BPQFMQ46j1nTI2FaNxHOUemyYBh58Goo4wBIQJr2i8B2K_X721phNr9PVO1aUpmmRxRWW87XrIFGU6S2DJu2ea1_vHDqPtyijNAg_DtBJY8wTz0wlj7B99BGBHfSOZ2A_-UT4aaZEzPqsMnoGzrkwlu1vzaohXSBzs5quOxLm2IJQ79NZ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور نزن مشتی جام جهانی تموم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82443" target="_blank">📅 22:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEyagZKJ00G8sMzHwfHaMM87KXvrHXiOuHA78KDRciM_jfk8qaNrvIsAWvRyhvyQIcuT8IdnPfvawV_2wjsf6UFqErBp329nCVEwevdd8-no4Hv_3XBDQsYc7aODmrDZO7FamwN_Cvs_dDt-1CSHfVPMOQdmBLQwwpwgwxPopNIerIbOxpXg_uLE56hU-mD0mFW1-y-hpDUbkSLiLN0uPHHY0WCmah0MDrUSMSLCRX-OJH7bX9XQJMCjLrStOQkFEi_b_MnbaSXIBWJbuBzK1mxLVtyYWD1gxJMZPgbyooPtJZbJEzz0XDArHBgQZB9r4ehvO4bH0tk-8jrfCCXnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخی، قانون اجازه نمیده کلاغ نگه داری؟
🥺
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82442" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN1iPdWJezWhH09DsqLNQsj7rMMF_0TLSmrPqlT_gRmjSb6Mgped8F2cR-oxBdzfMVAvefmoKz16MOogu_mZaqPUH57VeeaGHVGjnBMYiFdmccnqH-UXTVcHJkGBudVexftdKzwvDv3eWfSSW0mGl4FOSQK_ILUAa9G-MSBcFr6nwXbO2241LnpLSBhgkHoqgNEqPw0Gvl_5MUqNUlxXhdwcvvyI_ksw34qrl3FSelg8UsmGqa-1eUySHGTngkDPRnblo2P63jDtIA-NG-7xi8qolfAWBHECm9wlnluBZwPRkf7wKFYmp0CkuRTm8iDfLcHw1Z4-6z-Jm0iYf7V57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82441" target="_blank">📅 21:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82440">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4QP5SNPscEXlumLHHpa4p8TO3QwYL2xT9KCbLQ0DyJVBuRViubM-BVjXXzZLD0T2pN_UpMmsGjEaVXHN5zSa8uz2BHOzu33WXXzfHgTcuexEKhMDfTJLRbsTsSLz8O7FM2c4iOO6Z5eDytbbir-ighIOVSGivn6vAPi2vkh0u5mQh8l2Qj80UUWIswfk5_rh2BGn5qvUsEq6NhCKnbCwYbz1Feog1Uw29lqhVLvkLZviDz7UwABQZruE3Bopd203x5G7VSjIw4VX1Nz00uLk5kSMrWFGd0GgV2VfJbund_c4xbpOpE0W623vyarIoafInbytHEkSqndAkWmPMXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این همه واسه پوری کیر گوزیدی که تهش با مجهول کار کنی، دسخووووش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82440" target="_blank">📅 21:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مثل اینکه یه تیم خلاق و با تجربه یه چیزی شبیه پورتال و مارکت ساخته که میتونید ازش گیفت nft با پرداخت ریالی بخرین استارز و پرمیوم هم داره
ایدیش
@premium_grams_bot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82439" target="_blank">📅 20:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82438">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایده ی فیت پیشرو با سارن رو کی داد اولین نفر پیداش کنید واسم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82438" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9p83fELd8gmcrzfbBc8y51JPEp4orA6aWjZdUC7P4-RSXqfiPbUIiD5b97M12ZyDM0DLkDPAf6DlJNo-psDnVaPi6-XzZoWacxJyMDYIUs_3WgN5JYqC3DX-GCyHWHd639TLDQ0g0_3oEGVN4yadSd16CmCRjMIiVslpfYLfQAaNuSAaeSiivym89TgmzuNRbTVmNsvPRkphT48VxXAGE0hwFGZtyptMjWbjo5fvg6evCflp0MyF0TYA8GEllWG1yWAHq0qa-AngPDK8HKux2pEeqvn5kfcywwAJJ57dIZJdqpV_4CYFo2Esj9rxEVRffEjjzPOZdqakDs25AAf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید این دو تا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82437" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قالیباف:
ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
امنیت و اقتصاد لازم و ملزوم یکدیگر هستند؛ اگر امنیت را برقرار کنیم و تداومش را با اقتصاد پیش نبریم پایدار نخواهد بود
ما به عنوان یک رزمنده، بیش از آنهایی که حرف از صلح می‌زنند، قدر صلح را می‌دانیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82436" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw-lLOU0KPYnkHLamZ9HI9eoTE-JTjdaXT5qYbBnWn7iaGVkvq0-adYCb3q-14yZTAiwK4xeCVEevQQucOvRYCNHQv7cZAjo8DTo8js1iFa8uDUWv8Ez3UUP515CFXw7EKRKFEBRPVBB7e2lN8RjB9jh5_r4QuwL5z69lqtaUhbZqgSeQTWAVxO-73vZeh1PdXum-yc2T4tPiWyxOupgXTKstS6gWTGG-MJbZEXcPMHa8yL_qndE2OhGh1-qDPEtTwVIYayK1UhtoXIo2vZ_QCqDRDq6--kcGwssztnc2D5KsAcpx0uSbs61_iJ_VAbbK0b3-UfNlQtWq3h2irUlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82434" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یکی راکستار رو هک کرده و داره تهدیدشون میکنه که یه ویدیو میدم بالا تا مرحله آخر بازی اسپویل شه
تا الان هم چندتا ویدیو از بازی بیرون داده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82433" target="_blank">📅 17:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82431">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSfVIeu3n1xQvMWGobCP-Rv0nqjSPs4jEc8YN3QFh8pqZ1Vr0zr-e6214Q0ZaVtsqd4gslZd_yWAv1GWjpFKsYBuNyZZv2mjUznkOhLD9TGwDuaSZOIyKjV5IsYor76a9mgx0RvWqGq0umr2AFDR55Ng1kkfTtX4Cn4tV32IyscaBqGeVScV-8vTQAxtI8UXn-GflVuQglWf1937d629kTugcVg0jxAHoWTiB8R9l-nDcygr58XK_D-CLwENB33aX6BmEFOqetTofOpATCMHMZUe9-wujnvDxUii0FqJTbweVlgO6dZ4zx0wCxLUo9IRxsY7BjNrEKJcoPKPM6KhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHBtxEX5dxh25tmwQ2Ct0gVQD_Wqh2lIZX7KgBd9msxWV7ZkHKwk_fhQ_soma04rDtYwLnTxPL73tCNskn4kLR7eEPRU_Tqr_PU8thWJA8fid9mrWp2QEmLuJkpJK9ulHHWITq3W8B3joDup5SObZXtATzRo9l7roW3nr7l9bZ1YCu4Px7EbmhbE9hvEEM-lQ-u4RKArvZrLB8oOZX02fgWKHUoAXTIqLCTiwzz_jU_paDDxf6xAsBydtTg9i7f-HbPkBU7UZKZoKFY45fJelJxvGvDZaKG3IEtAZTo73aykyoN1K3MyqKVEamXWQ2ZhUFEuvby5OiWsZ_uSuBANyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز عقاب نیروهوایی ایران، امیرسرتیپ مصطفی روستایی در گذشت
وی خلبان F-14 و F-4 بود و در جنگ موفق شد ۵ جنگنده بعثی را ساقط کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82431" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82430">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj5PhcSPJft_MJJ7jbkUxf43f65MwujlbuOu8xI5wBj5Zf7M6tDmxlz0EVkuH_d29G4H_7OQEHBcvuhH2ODxkZrP4noiO6G9e7DiZ40Z7H2PPZQkve1Jt4ptxEUahvrsTH5xFKrTYS-AhWqD0kge-C3fcplIfrq_eYf1qhkyqVTJ5Ued8z-mZp8RWFADrvJwCUSajo0RYmflvgxznN2NGWKRTTVEO5pFDe3LKs6w_xvLnwEQVX4nJ38UTtsReigwaK4JfvFT_GXUmrPRA-X-OpVcY-49W7OhlYDvX_49QpZMb6Q5yDdQhfkSU2PehUheJgIagxaSJi54sCHZPSvYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لیگ برتر انگلیس
💯
⚽️
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r30
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82430" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82429">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyIGIG5mZibbVMcIgpQvhQDjKxRagpjeWAWOGAo7XB-4jWZCLHs02SBFvaeMPbJC3ylrtMHveyBYYLsDCjdo0C2xBlQPQ7sUE4mP5BRr2Hn3YZAacYsMVG2itFEzjwyWDyVSAiYOAufEoNwWaW4vC5nn_snZfY-bEPQaIcudjHTbMC7GiODXhTfLLZYY4_7G1P7vPeGX0OXxPx2ErfLcTuJumNoMZGLYnjlKmL5Z5Qv85oawXhgpiBhNqs5UpRr3XgoUNmN9zei2EqJLJJw4pRayNVI9A8vYPt2y810p3SYvDgW34GKxdXx15gfIwBjYeU8-z9i28Bqro1gDXtNnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالا مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82429" target="_blank">📅 17:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82428" target="_blank">📅 17:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82427">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=lWlENcG5ORCh49dfsCnAHsFDHep0hRu3bKbGoY3U80p1vdpHd90By7wB6kNrVR3dCRuC6mYRUnrvBQDVmY1A-qZeafwbj1fP9l8RgHbmBMJN5BaetsU7ut4ba7KnIB_e5T65Q_lpGcpN2EUBfnoS_lbuco3mBcYbkjkm0L-cnq8K5OcLRqorWFDGaBLpMtPJapVyqC7hEa2B60jlxCiEEJio6e3yTGFvVQhDneO7YaWbgBOSLTkfmx9j0xSIprAJVGMuOP7BGSgVWt2IcdqW-E_36N-WpBDsxVgMAVflo7i81gin0Di37lkWOdzQiYNtqZVDXbg9C_V0ubLb9_tctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=lWlENcG5ORCh49dfsCnAHsFDHep0hRu3bKbGoY3U80p1vdpHd90By7wB6kNrVR3dCRuC6mYRUnrvBQDVmY1A-qZeafwbj1fP9l8RgHbmBMJN5BaetsU7ut4ba7KnIB_e5T65Q_lpGcpN2EUBfnoS_lbuco3mBcYbkjkm0L-cnq8K5OcLRqorWFDGaBLpMtPJapVyqC7hEa2B60jlxCiEEJio6e3yTGFvVQhDneO7YaWbgBOSLTkfmx9j0xSIprAJVGMuOP7BGSgVWt2IcdqW-E_36N-WpBDsxVgMAVflo7i81gin0Di37lkWOdzQiYNtqZVDXbg9C_V0ubLb9_tctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشبختانه خبر رسید که عبدلله امروز یکم ریده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82427" target="_blank">📅 16:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
دسخوووووش
باشگاه خبرنگاران جوان: مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین تولیدی این پالایشگاه رو تأیید کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82426" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTkdoqkdH14IwaBFTS5kgGA-DFX0pGGFYvehQs8UAlIbEmdLc-wktwOWRdLV0K5ozoZkdRZH-a7w7xSQ_0IBeW1mMNbX7YDQL80WDoyi8ihviud7vKxyBtJ9RIYjDnL3sAwQTTja958NItf1P4mJVYkmOjpE6Htsqwu0utt30N5KPRrL3OQX22_k6gGpl3HZFuaNAYJhYUoP2UmEll3fV6Vi9h9dOd0iUz0C0i4fTIWxyUE6wm536kpPAwnVm_jWef0YB1gxlt-_M8b_MRgjBN5N9cykNtb_tmO__CicxdVyA954l3bi9h7gFvAXqtNhZiEY3T_reRSGXOR-VR-NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کدوم رپر میشه ربطش داد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82425" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان : جنگ باید در یه زمانی بلاخره به پایان برسه، بهتره امروز که در قدرت و عزت هستیم و تمام دنیا باور دارن که ما توی این جنگ پیروز شدیم و آمریکا در دنیا منفوره، به جنگ پایان بدیم
پ.ن:
😭
😭
😭
😭
😭
😭
😭
😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82424" target="_blank">📅 15:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJhXK4OtgI39YrmTjeSHDSJOTtk2b2zMO6j0NVxHnEcbTmzPGH7L8kBVNFsJUhQNpPdX_NpS3Zd1OJiq1TPSo-6WGCZQEm0Xx5nCb6JSc7OkHqFL0AFgK3wblgVN4hmgJlH6bKcLLAzs-6O2ku6HLpvwwrQqKXJLlPwI7G1KOC4Pb5G9K6No4TQaoxwK0I_ga7qFYQXHfgNwUAoISVx-BAA_rWht5mkLp9kGVizjgew0XjODhSObLG-CoxCYOrWQogn6FwMt-xDwKMW6HB9_Dg_BoiPa_L9TtOoXYEKphymVy2DHN7EElGrnMdR6H5wOb_L9OmEqmmSmrBTbiFiwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82423" target="_blank">📅 14:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کنکورو چطور دادید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82422" target="_blank">📅 14:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0m4rheXCCfd3Cumbnmmr1MPH61-oLxvedZDB5vZobMxe_Fke8h4HY8puCcXiKfmG_8fzH8pqzj2ye6B3kiZuGrGbiDMHEyuXtY3XhgfuMELpxA7EbfC4EqNBWtlm02WWNyb-plN9m6cIl2krgSmxcxVjtiZ8Yn6srcqr_fraXHJhCIqeStnbhgWWF9A-s55yZLuZ9d7MgCuiLUDB3K5qbDgUxoBXCKVsaybOX_KclMs-IZn-U6o3N8_uUxCZ5YIKREmGEGBT4I3av55ekdZu1KhXZ-v5TCfmiPUFBuDMa6-hkca_T-zYnEhSO9AmZ3wVXAg_cgzr-6Ty0GSAIx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیشرو و سارن به نام Mirrors منتشر شد(لیک)
Download
(حمایت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82421" target="_blank">📅 13:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bajyU0WRKe3BAPIVQX5wOL8aCb7pTsWMiwmh73WsB88u6HJB73vnumWA9Q37CE7E_8HFtQNfbNcJzYtg7YU9Sk8mF1uBxXQqCmoQX3dS5nI03-IbVHMUGsHVMzRuVIAPa-hOE4dNlDimAgPUoi7DiE4x003_RI0sgbK26ktjrEarsYyT2vZqSljmK9BU_drae0u1bbNejAF1JrgWCmuCuzE4MMlXe81tc6WPC81GGsSadSZgicIpLGNjFp6hYb6oLr8CKgX-RZrAJFZVTkysP08HvMbfDVQE4S8Q4lM9gKPRb5DbGqT_AKyL-rd913B-1rgHA4qH7hLu1BZyEFKXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تست کردم مثل یویو کش اومد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82420" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا تسنیم اومده نوشته اقدام ضد انسانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82419" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=cGoJnf1UiTdqhQPaseLkfwOhOPHySTBLxAy57iv_3GoOtVN3_S8zD1pL6rYKmSEr4yACVlBbEGhJ6zuDxUH3q5vqCxIZguHOpubeVF8hH1Y2Kzma5UemChMYZhBlfDnbMfSnPLuk8_dbWGV0l77BaUx_8wmwXebWjvU2NUXuTDpe0LQhyKRPykwTQKAJt5k8rTdPPCZanMXokuLs-Aaa6XRTbT9RgrRx1mdR59h7Lm9hN1fngZnqTnY2PdHM8ZydWzfOstmopALoIN8h0kcSol0qVcVX13Nq-Jw5ZE3dUw7_lO60gPZZw4SKswqPFn2C79MN2uxMWTw0HJ116L_hpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=cGoJnf1UiTdqhQPaseLkfwOhOPHySTBLxAy57iv_3GoOtVN3_S8zD1pL6rYKmSEr4yACVlBbEGhJ6zuDxUH3q5vqCxIZguHOpubeVF8hH1Y2Kzma5UemChMYZhBlfDnbMfSnPLuk8_dbWGV0l77BaUx_8wmwXebWjvU2NUXuTDpe0LQhyKRPykwTQKAJt5k8rTdPPCZanMXokuLs-Aaa6XRTbT9RgrRx1mdR59h7Lm9hN1fngZnqTnY2PdHM8ZydWzfOstmopALoIN8h0kcSol0qVcVX13Nq-Jw5ZE3dUw7_lO60gPZZw4SKswqPFn2C79MN2uxMWTw0HJ116L_hpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره با دوست دخترش قهر کرده، دوست دخترش هم برای اینکه از دلش در بیاره براش بنز خریده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82418" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فنای پیشرو جان جدتون دست از سر این سامان ویلسون بردارید، از وقتی یادم میاد هی داره تو چنلش میگه فنای پیشرو بیکارن علافن بدبختن هی به من زنگ میزنن مزاحم میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82417" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=sj9-RciaW65Mg0zDKrYf94i9m6q_kS7utsiRStgqAu55AnHZ8yymFFoLYNjAXiOOKDSF_gfpK3Q-STZp_5ARuZPLh9PCxNrmb5MJHeKpJ1kObeto_AiUJONYtJpuenDZbbzEsOLa90Xqq9MemjsFmxRxWYox-6QyoCIpm5YbnsRNpUug7p_0oZm3vzLxsnbWWLCJSTRQ1Negxn8PsENR00YhykonXMgBC8pvA_LeU76mTtvzvC1iY_BZ43qpT23IwYMhokwoc3gwY2evf71wr6kmYyA-_JBvSPwjzNTrJe2H_yIE6UMZDCJ1hNbYRXZZP-RxlWZaQ6QC4tf85hRw8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=sj9-RciaW65Mg0zDKrYf94i9m6q_kS7utsiRStgqAu55AnHZ8yymFFoLYNjAXiOOKDSF_gfpK3Q-STZp_5ARuZPLh9PCxNrmb5MJHeKpJ1kObeto_AiUJONYtJpuenDZbbzEsOLa90Xqq9MemjsFmxRxWYox-6QyoCIpm5YbnsRNpUug7p_0oZm3vzLxsnbWWLCJSTRQ1Negxn8PsENR00YhykonXMgBC8pvA_LeU76mTtvzvC1iY_BZ43qpT23IwYMhokwoc3gwY2evf71wr6kmYyA-_JBvSPwjzNTrJe2H_yIE6UMZDCJ1hNbYRXZZP-RxlWZaQ6QC4tf85hRw8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخت و پز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82416" target="_blank">📅 10:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swGzk3MzpZ4lasbExu90zQnaFkUJyMTfYBbX8rODx8qEdwwdccQCF6big6XwVArk_MgDcblXh82L-LmzjZ_1PVDpLCchno8cP9Tk6vr3HvJ0SGFXessVMrD4QnD-uOWFNhKEy3zRoqr3h_eo_MKs3WhzhvaQDh1QA2M4zmOk9kXM0gVHldGSSvdmcCj-Gma6aAkaamVdw5by8kvHnrNcMTCUk37rhZblQvGvXujlXDByc863ZhgyDFvXSybvqzRFO32Op3dncgC-0CC78RFd_dDkULHt9o5ah8y1k3CnzAt__ZBKJCyBZOdsofe7Uxip72j0NxssxRBGDdMc7Eeh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید آرتا و سمی لو به نام Azizam منتشر شد
🟢
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82415" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9pcfFd0HAbHcyWyXv7IU2mcU1fleZXCY8gjv4vfAhDTu7f010BxgZQThTK8JN3SXd5d3W9kcItKA0qbV6NubkjZc5TlEFE-VtJQWHc4j3lNTpxBBvzQjcHEG7aT7K3Gj5Os9Aoe7MCQJa-v9VEB2BuWEJuxdxUuxLc1yyGogtDw5vYfIo_2SrejzAC9ZFbN6pXRmqEUuBtOY9ZW183bnGIjFBXPGuYWyYE03bpzK2rf31t4jiwEdVi7QCXHkg1qM2x4he2kBM26zkoo6L96BAfBmE8QZ8jk3dSfro7E5EbJgjHIxoTyFhkaR8V-ZP3twevoXeVMkXWVzgU_oKa56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی ویژه هفته نخست لیگ برتر انگلیس
💯
⚽️
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته نخست لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r30
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82414" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=X7yl1vXjR-cKwjSKQ1WCaOw0VQdT7e8-MzSOz8c6jkDTnYGIy5xvKpZ26oPQE78CQe6KnkUsnVteFzBn6HRNKF09I-Ba7XNbdk58ka2L56qOLviqn1-3Keu4KfKm8OIrDmJfXt0V9MULDrEZtHICkNE6lP0q9MBleRt9JWHq4v4iWXVTzmBwju8nKmWrGG1aDwzXC0xeTazLUDy5P2FqeKteriZUmF0xvAMBjBtdCCy5IXlD8Jl_OAVVs08Cxx80i8vLVc_pTTK2yV-kZumoBB0m3J0y_Uo0ARu2L5M4sbPNpUG5A_mlDMfnqu1ri-PcDHCuLgCp31-7ucJHdnWDCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=X7yl1vXjR-cKwjSKQ1WCaOw0VQdT7e8-MzSOz8c6jkDTnYGIy5xvKpZ26oPQE78CQe6KnkUsnVteFzBn6HRNKF09I-Ba7XNbdk58ka2L56qOLviqn1-3Keu4KfKm8OIrDmJfXt0V9MULDrEZtHICkNE6lP0q9MBleRt9JWHq4v4iWXVTzmBwju8nKmWrGG1aDwzXC0xeTazLUDy5P2FqeKteriZUmF0xvAMBjBtdCCy5IXlD8Jl_OAVVs08Cxx80i8vLVc_pTTK2yV-kZumoBB0m3J0y_Uo0ARu2L5M4sbPNpUG5A_mlDMfnqu1ri-PcDHCuLgCp31-7ucJHdnWDCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این لحظه به بعد کیرم تو استقلال، ملوان عشق.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82413" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWvtU6qSjJ7qJtmjbwEGvTFVlE36HDEIOUUwFb4Se7uraMrqJ3pi0KuLEpBWr3BpG0Q6dc8s6io0eWYa5RDWl6K3lWDjwQ_TIJ8RaqveS0BkwRPYAvDD_EA4gk-_gxGehXmwztMuwvWjLpPnHs2YTiAdlwBlhS68zr2ApIs7Ud_iBg4OX-Yb53eTLDu8cvPuMzsg9IfvQc8oGqMMqXExOeKHdH2pxlQnhajxdBc1cqVvjQsWwHg0kt8sf9N3dmgkDKJGkiZhv6yD_x8Uagp_Nv35twq3GMV6EyoN5bUkdofpJFOWW8W5Vb1MOK5OAZR45ZzUl871P65HZC_lEghlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارسا یکم بی ادب بود ولی بیس حرفش درست بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82412" target="_blank">📅 09:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN0dHE3sZCWXpZIKAx0gkQUOYi_h7k8j4wh08WkVzR5dzElrfXshFhBVkvyz7Wv_k1EPjZ3iapk5TslZD2mhQbhf8MNPJE5X6a0Vv94yfBe6Bkeiye_NLUyihx_VRTypvnGwT6XCk3FMeVJ8zYfTUFhRoOr_zoxRnLwRzGk4oK2czqxgw4vGI2M5-PGYg3K1coHi55upGEYpDdFhOCEFRWR_9eBfvcwiTbe-h-w5KKRU0kI5wOQ8r-TGBbeiYgXs-P7OA7KyTSLug_3Y4t2efA380azWaxOO8icwzHB6Mo1wEqvftJK2-zcYRDT7gTWum7E_GhXmUKy4-VzfPZqhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
💙
با این وضعیت تورم و گرونی دیگه سخت میشه کیت استقلال خرید
ولی این ربات هر هفته کلی کیت استقلال هدیه میده
👇
☑️
@F00TiBot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82411" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvow3e6UR2nJCTZtyYHfwTKa7CZ1yBTRNzFN_jGoERB68gEf4MdvSR2Q9z3E_6PNOUWlUiIczwc5pspOOwpZsEn5AWBeMQutKUQw2mb4A8EvWR33YavfYmsvV9aTx1Q6hw6OD1VprdZ1HadKLxaQjqjy1GSaVEMI8ukEXDUG4f-FoPzwHyKVAW9hlkz_d_jAZ1gm8WrKMT0tB0jEkskgeSnaLDoeOgq3fKucW_H9P6EMy1mEhKqlVbHOhsGDCA6pHQWbLU2HfJE4RNxTHPxyBtiqsrzqfkytTYj8MEw39sF6n0ihnMgIHgiQFkJl9pawDrVv75wLH4JH_MULU82zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82410" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=Nl8oo2IUMHzktkRAEeTlbLwvCcPSmlvd0Q30pzw5sCIAuuA7_STglWqzXyhZjrqSev1OZM2ru1oNIcOyO7WG39ivBIKQDpzDuCY_Whkh9pAIyWq46plvxr9NIiH4oQhLefpJU_D47LG3yFcW7FzbsCKyIk1mRRRIC6zw2i6MCKop-97keILTNe079l4T718NoPSYADpnlkC8t2sEqsTkVFQJeOk5fxTgi97A-Ayzwl1Cegzyy4ViFj9miJ8LaMYDUrKart6W9cBxYTOiQ3UNINQHNf39vVvP3UlBG2_ah9xYJPCWrOZZj1ahxWdpLbA9n5awXEvt-FGH2gNDdRvU_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=Nl8oo2IUMHzktkRAEeTlbLwvCcPSmlvd0Q30pzw5sCIAuuA7_STglWqzXyhZjrqSev1OZM2ru1oNIcOyO7WG39ivBIKQDpzDuCY_Whkh9pAIyWq46plvxr9NIiH4oQhLefpJU_D47LG3yFcW7FzbsCKyIk1mRRRIC6zw2i6MCKop-97keILTNe079l4T718NoPSYADpnlkC8t2sEqsTkVFQJeOk5fxTgi97A-Ayzwl1Cegzyy4ViFj9miJ8LaMYDUrKart6W9cBxYTOiQ3UNINQHNf39vVvP3UlBG2_ah9xYJPCWrOZZj1ahxWdpLbA9n5awXEvt-FGH2gNDdRvU_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینو میخواستی بشنوی کصکش؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82409" target="_blank">📅 23:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW1EwYSHHhx3kp-sgxnjVliOyXDYEond1VSKvfJ7x5MdEctbx2EfdFlf2cqlucYV84JyVdWYQ7-q9HVgklYqhRBTYNzlGoPdnzVAvxWsJQ8NTd3SZ2oxoBdX2p_ZGUDvlVRDk_LQG4AbMHcV6gn5auz-e3-O9z8_IsQ77V5tyWqEdRdIjOwoBXvHw4SKB8x0vDRsurPoUzR6odvKM11IY3eqsN7NzYSk9enP2cj4BPsxqzSJMla_vNdWFenP8ChL5s6QUKVofz9YwuF7SKcN7CWD5Z_7nnEnZp_R6B3kyMwgd-ndF3VN3rkl7mfCVoJzSfz4hhRHQc7fFGqnnyXVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا برای عبدالله دعا کنید  @FuunHipHop | TemSah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82408" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پسر ایران فوق العادس
غریب آبادی، معاون وزیرخارجه:
آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82407" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=LHREmXCtej7eN3IvzAh0G649Kc192hWyyuqGuIw_C_-EMmLvb-ZC0ITVP82foCfLC-VS7uRSMjDpAonlu0Tt9nRCDDO2PIW2dgOYHP3bjoIR1ca4RQIKSIk3PXClLH3EvSeTd3DtRHMHjfsv9L_EYiET6z7LiBhOdjmu8L8WJmu5dH4jAkVD6HCPCE71EKWTQq-2bQIeRARbj7_-orP5-elmQ0Wx7hvzqsEa2mYGf3wUOt6yyEHuyr_JAB8TdLu730M9twYMxztFtPs9TzdjyvEjTYIR-dCdxWSMjehByWOPr1yELmJT14mGcvCExssqrQ8VlxtfvZfvaXLFlqVplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=LHREmXCtej7eN3IvzAh0G649Kc192hWyyuqGuIw_C_-EMmLvb-ZC0ITVP82foCfLC-VS7uRSMjDpAonlu0Tt9nRCDDO2PIW2dgOYHP3bjoIR1ca4RQIKSIk3PXClLH3EvSeTd3DtRHMHjfsv9L_EYiET6z7LiBhOdjmu8L8WJmu5dH4jAkVD6HCPCE71EKWTQq-2bQIeRARbj7_-orP5-elmQ0Wx7hvzqsEa2mYGf3wUOt6yyEHuyr_JAB8TdLu730M9twYMxztFtPs9TzdjyvEjTYIR-dCdxWSMjehByWOPr1yELmJT14mGcvCExssqrQ8VlxtfvZfvaXLFlqVplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید با خودتون بگید این کسشر چیه ولی این اثر هنری با ۲۰۰ دلار بودجه ساخته شده و تو بازار چین ۴ میلیون دلار فروخته
پ.ن: ممبرا نجاتمون دادن محتوا فرستادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82406" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محتوا با تایتل "عاقبت اعتباد" میخواید برید اجرای جدید علی گرامیو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82405" target="_blank">📅 21:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82404" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82403" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH47MzDbYKWYG7weiBEgz-_3BUWHjiK2rJck903tBw8keCoCsY6G1XbB1W6Z6B-XIZNK7ZGLt8qbsxCbgA_bFGQqx-lFEnFohk2cU7V9oOg54-1mniw33_cxzD5Ac5NbtUeA08nJVtb7KYzIxpYf0wS3UhrAhKz54uXTMGDpjWBdv52a30bG8Tl9MvZ7bnIeTp7mg5prORMUukij0IlmIBhsSl097SLaLfO4hMfwY8TbKsjVkaWhzna85UwM56xMYGMVZAZwCmuGCEzocaCVJiCoTW5GPsEBK2UgqP2vEnJdyLaviIHiAhef_JBFZxAepbCygSC8WYGF_Wrkew590g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود ببخشید یادم رفت وجود داری
موزیک جدید ویناک به نام باور کن منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82402" target="_blank">📅 20:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بسنت، وزیر خزانه داری آمریکا:
ما قرار است سخت‌ترین تحریم‌ها را در تاریخ اعمال کنیم، و من به شما می‌گویم، این کارساز خواهد بود.
این روش قبلاً در ونزوئلا زمانی که ما محاصره اقتصادی را اعمال کردیم، موثر بود. در حال حاضر در کوبا نیز در حال کار است، و در ایران نیز موثر خواهد بود، و ما این رژیم را سرنگون خواهیم کرد.
وزارت خارجه ایران:
اعلام تحریم‌های جدید علیه ایران از سوی آمریکا، اقدامی پیشاپیش شکست خورده است که نتیجه‌ای جز تکرار ناکامی‌های گذشته نخواهد داشت.
با در نظر داشتن تجارب ۷ دهه مقاومت همه جانبه، از همه ظرفیت‌ها برای دفع شرارت دشمن بهره می‌گیریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82401" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زندگی پر از آزمونای بزرگ تر و مهم تر از کنکوره، فداسرتون که خراب کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82400" target="_blank">📅 18:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cukJhs7QyC3xrK0MAxQQ9KC38lkHBoihzcgOUBhcZVuC-_yiaHTCtzxyYx952uIQsM_Q02Kl6YD0tG-oRy8kUMAs-4nMeN_zTz0DQK_26O-Ji1yWHrl-wv5N-VPt_S7RZayorlXXqpUCHGWaD7qV4bRA7nPNU9LxKs_O2KWhX9CWDwy5gWKPWZdFfmTTGoWVbUzp9tGWPi1JhxFgzpi7ipwwUxuv0LJFcNT4RzKFxpAjhG2k3M2R1N8nrgXxka5N9AzWNfKF1ZSQELXvXbrCq-YTlTUs4-nq9P34NZ6_pfdB-0GHUg8ot48rosW9IyXiHxiEC1s3Fl9LtXt_zj4uOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابامیخواستیم اقامت و حقوق پایه چند هزار دلاری رو ول کنیم بیایم واس ماهی ۲۰ تومن کار کنیما
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82399" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPKlfmQYoWCJ9ksC6Z07bvjSOvdBTOFuVmDZoi1IQ9gmJMk3RxFhyDVf0YrrwdkoB5aN4lFoLHfQUbDjfcpmC7Hb2JWmX83i76fLrIf8IPKEds3Vk-8kYPH1bFcdVlC0ephk-OI8fBSlfN6K2OIf9tqj6zyyH3yBpLQypGIVZsd-hiSsCHKlDDiI_Wb8D72_kqSpkTkOG7W0jxCUl7cuALd06_l_OCT_2BYLwJFgtJ7MQhDbwFos4zmyQqPm0utDH0iaM9bHSamQByHNp6aNNwNmmsqh8DQkhSZc-IITWFjd54gEPari-CtCa1TUeYzksqVryfoBEs3zjbrR99gt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا شما راحت باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82398" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ویلسون چرا مست میکنه فاز رگنار میگیره
😂
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82397" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=plSGpfOuD2Ze_VyiRQTnqrUfDUcNJKT5lWAj5hG5dvINcibaJXnIju6ICi6auHstS84uOT_fc697AudQmY2Hw3Hyng6ONUeEHNVVgmcGT5pIHHjRr1-fzcJmphXP9GAFKUvhbKKDINl2PrGjWRpKICEoZgExyssXztLgpTv3-92kkLlicioLwSHaobhgkggyxyoY-c0UVa9VfguhZ-r_eUFuL1KIHs9DdK92cJ8erRrPVolABwdJ1dKER1zUNFWunf1vpKY1qqIUere7RkgWwlhRZjE0WF91X7zrc4OAlAIt2lex-m4UQcj98GUcb-ebGNemGK52ms2ps9PlqXzgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=plSGpfOuD2Ze_VyiRQTnqrUfDUcNJKT5lWAj5hG5dvINcibaJXnIju6ICi6auHstS84uOT_fc697AudQmY2Hw3Hyng6ONUeEHNVVgmcGT5pIHHjRr1-fzcJmphXP9GAFKUvhbKKDINl2PrGjWRpKICEoZgExyssXztLgpTv3-92kkLlicioLwSHaobhgkggyxyoY-c0UVa9VfguhZ-r_eUFuL1KIHs9DdK92cJ8erRrPVolABwdJ1dKER1zUNFWunf1vpKY1qqIUere7RkgWwlhRZjE0WF91X7zrc4OAlAIt2lex-m4UQcj98GUcb-ebGNemGK52ms2ps9PlqXzgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82395" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دلو دیگه نخون لطفا، برگرد همون دوتا۲ ات رو بازی کن(
منم دارم میرم مچ بعدیو فایند کنم
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82393" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9grESuanDftt9e7a77ydFScqo6g1r55LZNxSifDwa0PEY6DAeKTmNZbdwKAwVJJW0CHz--rsDeKveLmxUWL22PpkMYykyeH3AyNbvoXzZW13SS1oRpnlOSvMA1pYpP4QAQRK_X3mPOA_tv4VGuPxDT4rnIukJCCU6ERA0kV2y7d2n9Yoq_G2a3S9WxidYxatqYjcqKPJFHoUFXgsUcuNTaWRwqnM5-Ka5PhXSNCXOYumcm14aJCDmie9BpFy7gH6TYPIB4uiXe7DAt6V0FSM4JNFVr5QHJNu1sJBCS7m8UEGyy7Trqxx8m0sArzJxpGviQD3O6T2qYBsoScs3Rx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دونالد، ترکوندی دونالد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82392" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82391" target="_blank">📅 15:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر خارجه مصر تاکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد نمی‌توان اجازه داد مانع دریانوری شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82390" target="_blank">📅 15:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بچه های کنکوری بیاید بگید ببینم تو کدوم پادگان قبول میشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82389" target="_blank">📅 14:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPUqPPZedUdoIVJFiNGDSzBcHkbZ1fJbFcm9Fzex_5Y4j3xddAtnruSULugmnfGXYLuA3XQKv8MOk8c0oRbf0jFlDdzSdaONkIbPePrSwo1-hbNqtssTY83d3gZteX8DI9W3yjzsZMH8bhj7qjiTBSLPzwILOmOEownITi4rIWMh5bIVwgIB24Kxk6FwodwnX7qs2P_8s49OQ9I-TyxQNorcynH7aKYDKR4HBDjbEPZ-7zxz_qwF5jNHUPu7XZEz0FzkJ-iY--MdjUQhSW0I0CxIJYR8xOfRqaq6MmdQ8GludqzyjvZyIq27hRmgfUxYay7OjJn3JWqqpWs1TfzWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رو به جلو اگه جواب میداد دیگه کسی قد کاگانو مسخره نمیکرد اردلان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82388" target="_blank">📅 14:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=LoPNkZaEWZ40RmBe-ZlZ6AkZdZPHj2-pO5NZ2jmORFDR4ddm0BDMuvAkF9jIFSzS-0T_ofaOd4RE36OjGCUIIDNWQy0l_VAFxxNFgoKwfFC2rnmZbhUXQKwEE01VcXuYHi993Xt3fcgSWU_AIfhLTnZEnVhx0Vyy-3CpNajsm3vrjmVWcQIDWMHPf_WWQmxG40CTCpFTeHt-KzLbk-RLY982Kzt4l5_RMG8Tw-824JsQkHV5EexPr5-kQoLZzC6DucwNwwbpYcjizAYREETRaOLEF9kgRf94I99sdbvWR3BfRvwipIJ-bDa0fqBCV0Ui9LgUuaRvUWaywqnwQaeC_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=LoPNkZaEWZ40RmBe-ZlZ6AkZdZPHj2-pO5NZ2jmORFDR4ddm0BDMuvAkF9jIFSzS-0T_ofaOd4RE36OjGCUIIDNWQy0l_VAFxxNFgoKwfFC2rnmZbhUXQKwEE01VcXuYHi993Xt3fcgSWU_AIfhLTnZEnVhx0Vyy-3CpNajsm3vrjmVWcQIDWMHPf_WWQmxG40CTCpFTeHt-KzLbk-RLY982Kzt4l5_RMG8Tw-824JsQkHV5EexPr5-kQoLZzC6DucwNwwbpYcjizAYREETRaOLEF9kgRf94I99sdbvWR3BfRvwipIJ-bDa0fqBCV0Ui9LgUuaRvUWaywqnwQaeC_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه میفهمم احمدشاه اون زمان چرا این حرفو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82387" target="_blank">📅 14:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جواب کنکوراتون کی میاد، کد واسه شارژ ایرانسل لازم دارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82386" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g70iE1bsx4bCeht92m_y5niLQafAL5CK3OS2MHTJ3e0FgV0c6npPuCy8bhmJtnR56LYuch5LCTSWUqsFDYOz20wkhfe1hUIVJ9rGi2fnjRlvPnPu8-CpJfgI3XZFRfGZOqJXi_Bzo0wBYlhP7GkTZPSTrMMFuV8HtdfbmJqeIJRtfomf6YVZ6qcz1-cyp1VSuqqM5UGANLJ_duUFw15B1hKgyinMcEw52fNC1FYRRULAQUpY_S3OXbtQh1_8NNgDn2jIUcFzVPTbq75M0kgdReyrT76h2hCdQg0dbQoXWJZlAACrqHMPrQFlze0xCZAJFXCjlLoIwuFjjR7kLLIKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی ایرانی هعی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82385" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کره شمالی حدود ۱۰ تا موشک به سمت دریای ژاپن ول داده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82384" target="_blank">📅 13:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به چین بگید یه کپی از اقتصادمون بگیره، آمریکا میخواد اصلشو پاره کنه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82383" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=LMLvjvIpA0p3VPLqmfnSPIFak6Fw7Y7skA-QswxhspRjir3SRVYVQdxLPKnfxMjNFS_7BqAub0JnhCPprKF7zaS7o46CUY8LMaIIDQcZf0AlggsJIdLDqxYkOpYYoCLdLQ_IX6QE2Ono-Tf88B0tw8Jmp1rvg__oP2ZXhahDPK3XcK99nvpxH65ycdTlWKpZsB3RWE5-tZvXV1Q0-S_VuRvPGuz9ff3yWddEYqSc_QY2Ajq-YkiMvOMJVvw4r-JWmDvI_wnqBA6ubVjycVkm0JTYHQtSs4dSCfrOLwgCruDjwX0YwO2pvMZXvooJUIzXYLdUctTO3vd-bMk26FspMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b86b48a5c.mp4?token=LMLvjvIpA0p3VPLqmfnSPIFak6Fw7Y7skA-QswxhspRjir3SRVYVQdxLPKnfxMjNFS_7BqAub0JnhCPprKF7zaS7o46CUY8LMaIIDQcZf0AlggsJIdLDqxYkOpYYoCLdLQ_IX6QE2Ono-Tf88B0tw8Jmp1rvg__oP2ZXhahDPK3XcK99nvpxH65ycdTlWKpZsB3RWE5-tZvXV1Q0-S_VuRvPGuz9ff3yWddEYqSc_QY2Ajq-YkiMvOMJVvw4r-JWmDvI_wnqBA6ubVjycVkm0JTYHQtSs4dSCfrOLwgCruDjwX0YwO2pvMZXvooJUIzXYLdUctTO3vd-bMk26FspMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر زن شایع ازش درخواست آهنگ میکنه، شایع هم تصمیم گرفته این صحنه به شدت فان رو فیلم‌برداری کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82382" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX7m8rNsLkDgYK6fyQtIePHgDJmGdw3lJSElqUEGQkEUSNDLlsBJIiG1fOm5JmVK3PO7PsfmU2E2Yk_DWukDPea8sqPb1GPeBAsgrv3dJHE2UgPJXQUtW1SC9D-ixoT-ObcMpNalGJyufksYPYTDAxU1Aun1HFq-gm12P5qKi8AyFFn8xUOLy-_sS4vMi7ry-2rj_WyPzQo5BEb4sqBFGYeNV7GBYvhdCcJ7oDH0TjnWi8Srpe8M6N2_iofqLNBQla5PWjv7Oj_0oT_eyymssiWypsjL4AGiZg8CVrIxkNjANXxCg3zGciA4JArGbZhzDCOagTXWuMlvUQiJjCbP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر پر کار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82381" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عارف، معاون اول پزشکیان: قیمت بنزین تا محدوده ۸۰ هزار تومان افزایش پیدا می‌کند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82380" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XioXm_hFj-XLRTEogUYPVgK25cvQL15fElrQ0QfRt3mTRO_B4J9RqTTAeixVGSScbAwPLaqsdp9et5YJmNd7xs8HW8h1pqu-I6F4s2pXfFqlf97S7AEmOF0KNvBsQ5GaLM-TwF1OEjjuY6tv_lQWk3CWJMuj_K_OCOMjA_U7hAQyPLKTb31H8ERXhcbGQVKjqCJyav-nAHs8aKXYQLgTS6Z8Q8j5sDlVRgaZCayjwVVZkIA2zF-kAF9QEsGyDSvtB8YbMPJNWh6UtVYd72fnez1q2AmD_kzipxAO96x2QcnYet5VdeHT_7W4zPLjaXYWDRChoZ5pKvhUt-IqqmImIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رضا علیپور :
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82379" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45111cea33.mp4?token=o1l7Ti3vsqgd6ocL0HyAZ7YP32uXLo65haBjQLT1CVLDsBVC19g28L5oUB8O14kEtSmlSgwtE11hj-GoyyEv7Jr8ubkF8LYycGu45ayRddLIguiuYS8D36EL4gewwGwt34dGBrquqkgfBriR-IGt9TgOEMt0bsVpE9wZMFfdicSpODiiKcW8ddpsjeLdXTZQuz_4sritn9p6BM9JE0UF5YIb0eAMD0ZuZtmKuG9b_dp5xUWWhQcZ_VzSfQWKlwNYvrx1Tfd2dTmXnfKK-dAAzAjEzQ6aBPf7DvRdtJ0Hvkyvq1h49hR-xrxkhhOVnnDm2LQwRrKTjxhOLZPK6FI8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45111cea33.mp4?token=o1l7Ti3vsqgd6ocL0HyAZ7YP32uXLo65haBjQLT1CVLDsBVC19g28L5oUB8O14kEtSmlSgwtE11hj-GoyyEv7Jr8ubkF8LYycGu45ayRddLIguiuYS8D36EL4gewwGwt34dGBrquqkgfBriR-IGt9TgOEMt0bsVpE9wZMFfdicSpODiiKcW8ddpsjeLdXTZQuz_4sritn9p6BM9JE0UF5YIb0eAMD0ZuZtmKuG9b_dp5xUWWhQcZ_VzSfQWKlwNYvrx1Tfd2dTmXnfKK-dAAzAjEzQ6aBPf7DvRdtJ0Hvkyvq1h49hR-xrxkhhOVnnDm2LQwRrKTjxhOLZPK6FI8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشته شدم
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82378" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دکی هرسال یه نصیحتی چیزی میکرد برا کنکوریا امسال انگار یادش رفته دکتره
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82376" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSFyK83Re6Nuu5c7tLX7zJQmXd52yKTIkCKZTZMDlP9umKH9W1O9QVjuVhwpSJ7nrRs8N0UgbSOAfiggRetp3pY0rVn3p9JDMOz37X1OyMmONFwIJVMjhaSGJ81f8LMWyfPX4vZXTSn0LKUW6gkeRwbYPLVYVScE1XX7K4GP1pCcQDW3anA2SzVXEeeNBWhB02jHEPg4O_Mr4ttd1xZuz-vbAkjqkoRDvkFVoxrVA64yyXk2s0R6o-eoyRtD7dnxt4Y8fW6vx2iO1UjSCm5oZNgqABiGUd9RreLVL6XFuTX_vF7VSqR2u_3h6MxNxUVpA8UOZhyENe7qK8N8mReoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا قبل از فروختن یه آلبومی که هیچوقت قرار نیست منتشر شه(پول ملتم پس داده نمیشه):
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82375" target="_blank">📅 00:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=N56rpNO5ie1czPABuQIXc5UbNIM4K0cPmgR9SnJLs9GF5INDQfJ2OYpcu1eqSAAGIZt_-RJ7XtpzCqHNk8RCSTt68khsgo87SngWU3QXdZMLv4Vw_NtDmgnMUxSD4k_O4IWd6HD_cwY0DbBgkhFX5mjsS_X5SbhgSV0Yvbd24SnxbYSTZ6QZ93Wg9ETkUB8NlaSH1J-ElOpwY4u3lmR8eyamrrSeRJKAeM80DqPl4NiedGh-77AWRBsQW9gzB02QtqehjyD0BOOXWxCdQGdeQ8SzlvTfvIBQOS9tYO8-sPpEwtIVcQTSDZc3cCe6BzQg3dWbrQSVcU45dZsu2KrcL2mh1TVhoYvDTPDat_onu8UbIKZSVE1sivf6g9Mdw5YX2GMEPC6U94WDh_-I8WWFAqKAUJcwy-JdBPADHjEf1QNlIboqgoSuS7tjbU7jZcu8gAYNEL5TwLnciBaSVnqx7XZZIsE8Ou5SiVjNeQw6yv6hKdNy15WUscuKJF3ZQiOOnOMnA2EsSSsv9_B5Qe_mW4yAFxEFLtphdFhjkGwSXjLKaR1nqbr9ewC7tQxF6pQApvn_XAx_hlfqNytmKcfJGvO4-lJIBp4ZtZajTEErPx9kj06NjbhtGbGD-q-W5sm1VByrGuarKTxkhFdFMl7SaM8EZDifak5XzfjISJUee4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9019847c.mp4?token=N56rpNO5ie1czPABuQIXc5UbNIM4K0cPmgR9SnJLs9GF5INDQfJ2OYpcu1eqSAAGIZt_-RJ7XtpzCqHNk8RCSTt68khsgo87SngWU3QXdZMLv4Vw_NtDmgnMUxSD4k_O4IWd6HD_cwY0DbBgkhFX5mjsS_X5SbhgSV0Yvbd24SnxbYSTZ6QZ93Wg9ETkUB8NlaSH1J-ElOpwY4u3lmR8eyamrrSeRJKAeM80DqPl4NiedGh-77AWRBsQW9gzB02QtqehjyD0BOOXWxCdQGdeQ8SzlvTfvIBQOS9tYO8-sPpEwtIVcQTSDZc3cCe6BzQg3dWbrQSVcU45dZsu2KrcL2mh1TVhoYvDTPDat_onu8UbIKZSVE1sivf6g9Mdw5YX2GMEPC6U94WDh_-I8WWFAqKAUJcwy-JdBPADHjEf1QNlIboqgoSuS7tjbU7jZcu8gAYNEL5TwLnciBaSVnqx7XZZIsE8Ou5SiVjNeQw6yv6hKdNy15WUscuKJF3ZQiOOnOMnA2EsSSsv9_B5Qe_mW4yAFxEFLtphdFhjkGwSXjLKaR1nqbr9ewC7tQxF6pQApvn_XAx_hlfqNytmKcfJGvO4-lJIBp4ZtZajTEErPx9kj06NjbhtGbGD-q-W5sm1VByrGuarKTxkhFdFMl7SaM8EZDifak5XzfjISJUee4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاش بعد از انحلال گروه تیک تاک منحل میشدی مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82374" target="_blank">📅 00:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رضا پیشرو داره رو یه آموزش جنگیری جدید(موزیک) کار میکنه که معلوم نیست کی میخواد بدتش بیرون  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82373" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqRb-_tmzrRtp5cxBivGsNW0jyJkh9PcuTBzchDI7DP26dXxipLVW6aESnVSbe_VUdlwGBbsBhTjIPrnXcVs-qoAd6Eefob2AyzYGNhi0p9Q7Eh4JhUb7m9y4KAtc0ZSBMJIrDraPqV_l9w9Dq1Wc4Vk12TP69ovV0NPY_dnaa780sZQfccJ5QyL0y_SPd0GDhdoEItTefsReLQT3ESMJ0fE78i6rhI2aN6oqes4q4mYfclZ0JxD-LzGeuiFxMPe_LCf3AWt_0BwjNCdwnCmW7e_ewLnZVCiCsxz3wYd383eXci6uyNoI4_jRvj0g4P_5UQyYZ-gTKZghFIKJV3NpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82372" target="_blank">📅 00:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=nyI5hlF8K9aW3iFVMsal-86Cv43-hrDnuFornxSajIMu5jZglEsPiQA4ePHpySA4vBusaY15G4TQOPeUoRhJQbSWocRu2822HRHHPajm6xMKz5TPa_4lgh1bYDxpugOywxqBOsWmeoM80YLyklYtcLuEQfJAAMlM1_4qghxI7BZsvp7q_yyVIG0Dxt7xXxTXjVADSGWb09O-d8QL-1iBVDwbauFytS_K6rPvI6jJmEk4QGFuN0bh_vufvhITrcnmgjhLC5i1CevdkQN9vyvhd30etvb4eojHIXJgJDbHfb_2bsB27b3hct7OWBjt-k-IIo24ikGL9s568fTR3mTt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6215c87b9a.mp4?token=nyI5hlF8K9aW3iFVMsal-86Cv43-hrDnuFornxSajIMu5jZglEsPiQA4ePHpySA4vBusaY15G4TQOPeUoRhJQbSWocRu2822HRHHPajm6xMKz5TPa_4lgh1bYDxpugOywxqBOsWmeoM80YLyklYtcLuEQfJAAMlM1_4qghxI7BZsvp7q_yyVIG0Dxt7xXxTXjVADSGWb09O-d8QL-1iBVDwbauFytS_K6rPvI6jJmEk4QGFuN0bh_vufvhITrcnmgjhLC5i1CevdkQN9vyvhd30etvb4eojHIXJgJDbHfb_2bsB27b3hct7OWBjt-k-IIo24ikGL9s568fTR3mTt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم تو اینستا تموم تلاششون رو کردن که همه فکر کنن این پسره واسه عربستان سعودیه که آبرومون نره، بعد از این ویدیو فکر میکنن افغانیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82371" target="_blank">📅 23:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpJN9XboYXnHKk0Gowqi3fIptiI3KgHQ1biyG_s9M3fHtKcU1TjtZVc62eyz_-aaIHUxCpYzpSZSemldaGAAowV3XKxVHHw1b4WjkYFj1aJsbevi_efWR9dmjw1S3jkDGMhk7MzcEwvwMazvpfgEwYpYWqhScB548g_Gz_9CxBzaVrm-P0XuqQ1UK7iAZ3nt5opIqTn1W26Vp7wG25sY13_VmdN63e52Gj3I8SppKIIUJTah8gbufIcnHqGwqU2eRzA8DHGbwS8zjH9m9e1SJgoRzBgEqAsaYXlisjv55ci92o_RQBBoDVAPrpL9J_9SV3zQVDSMnrAsouhvq14lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82370" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
نه خارکصه خجالت نکش بیا اونم بزن
ترامپ :حمله اتمی به ایران؟ نه ما حمله اتمی انجام نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82368" target="_blank">📅 21:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سینا ساعی هم زندس بچه ها</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82367" target="_blank">📅 21:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e080993.mp4?token=sHNVgv6AqM_xPLhlMaTlPG0z3yW0sMaDobunzojlcKD2ADW4hnL0cF3wguvWVbEtlgEmEPUjVxm1nP1cvxbPcFFvSVR8JUaUqi_FLP8dt6pU0ZMnDXoPKT0x9y1Sv7HWecIN8lWFksNz94ILdT8UuIUgzumCfzCkHyWAv-SQZ27mcz0ORmZ4oqVZcm8i4Ejq9hZG45Vos6HmoTrpYLwLCNTUi6cQ6rhNzAnduDtUTQSVZ3BILESB1cWddU8XUM0sKFBP4osxJY2W6ahOARUmXS-LeDIhrYazF1F-LvK46BccIaozdIh8iciml9XYFB1o72RXxjGK3IMvpG96eiYFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e080993.mp4?token=sHNVgv6AqM_xPLhlMaTlPG0z3yW0sMaDobunzojlcKD2ADW4hnL0cF3wguvWVbEtlgEmEPUjVxm1nP1cvxbPcFFvSVR8JUaUqi_FLP8dt6pU0ZMnDXoPKT0x9y1Sv7HWecIN8lWFksNz94ILdT8UuIUgzumCfzCkHyWAv-SQZ27mcz0ORmZ4oqVZcm8i4Ejq9hZG45Vos6HmoTrpYLwLCNTUi6cQ6rhNzAnduDtUTQSVZ3BILESB1cWddU8XUM0sKFBP4osxJY2W6ahOARUmXS-LeDIhrYazF1F-LvK46BccIaozdIh8iciml9XYFB1o72RXxjGK3IMvpG96eiYFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران آپدیت جدید داده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82366" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هیچوقت واکنش بیش از حد ملت به یک سری چیز هارو درک نمیکنم، مثلا وینیسیوس جونیور ریش گذاشته ملت یجور رفتار میکنن انگار فیلم کون دادنش درومده، والا بخدا قیافش بهترم شده دیگه شبیه میمون نیست، چرا نمیکشید بیرون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82365" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پوریا آدرویت از وقتی نصیحت داداشو جدی گرفتی رو آوردی به ساخت کلیپ طنز و از رپ کشیدی بیرون همش تو اکسپلوری، همین فرمونو ادامه بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82364" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
