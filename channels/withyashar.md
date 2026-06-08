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
<img src="https://cdn4.telesco.pe/file/LPcUEakLM79Uzdvf1TOP76-d1FQAtjWtGae-boeEeNEnkuZOEnLmuhanKFhMgV5RtE7_Yn89b-01BEn-SuseRP395NoS2SjhFom1AqTW6OKl_L7tTYdAongDL4QHg5TeXdieUMtBbBB9mPCda6LuUViJxBksHlc_UDi1zUsTZN3LS7gPm7ulCusY7k_x65XheQGlof47A_6vLGxKsjzxF5-lFdidBrPaUtpRJ2SG7m2BasUYnRFONH75URv1rkZ_yzBLce0_WKlgXT2rI0vAidDkkW5PWka-vJBGKjxvY0Mw9rU_UwHiXFbwpuLVYKBOXiTObn9m4L2eE3P-7LaL8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 299K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-13906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نقاطی که تایید شده توسط اسرائیل مورد هدف قرار گرفته :
پتروشیمی کارون ماهشهر ٫ سایت راداری تبریز ، سایت های نظامی سپاه در نجف آباد و اسلام آباد غرب و فرودگاه مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/withyashar/13906" target="_blank">📅 09:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13905">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmU_hECkMSfXZeHKEwubvoLg6EQNTWjxmHRQMK_xYXUA4Svs0L_AGRMl-B2rbuXgT0kLApPD2l8g0DhSMptnQLkTEAeOfJV1sW8gwzOixXRaY-_ROWknB3hqVplmczqf4q7MoAfSvshJyFznuXgoFSwkS3mraCUl6zSakZBbmv-KHELcnWuMnQ2Z0oyVdP8by8cvJgrdGfwM1exZq-ENCdsltSHvafgFR7f6BathJ0Re-vzo3K3Gc7_WuMAaqdm4pds22AoDdm1zSWiXeTIBmDz4DuAdOX9hy_DWKmN6uyrvzklfAmfY4XAFNaevKI4Eu0CVn6p3T-b4vxzbEGXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه الان
@withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/13905" target="_blank">📅 09:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13904">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنگه باب المندب توسط یمن بسته شد
یمن تردد شناورهای اسرائیل در دریای سرخ را ممنوع اعلام کرد
سخنگوی نیروهای مسلح یمن:‌ از این لحظه تردد کشتی‌های اسرائیلی در دریای سرخ ممنوع است.
@withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/13904" target="_blank">📅 09:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پدافند کرمانشاه فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/13903" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13902">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسرائیل برخورد موشک @withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/13902" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13901">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رادیو ارتش اسرائیل: تمامی موشک‌های شلیک‌شده از سوی ایران رهگیری شده و یا در مناطق باز و غیرمسکونی سقوط کردند. این رسانه از یک انفجار در شهرک ایتمار ناشی از ترکش موشک‌های رهگیری شده خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13901" target="_blank">📅 08:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13900">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">۳پا ایران: مراکز مهمی را در پایگاه‌های هوایی نواتیم و تل نوف در اسرائیل را هدف قرار دادیم.
@withyashat</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13900" target="_blank">📅 08:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13899">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رسانه های عبری :
در اسرائیل دستورات داده شده برای چند روز جنگ آماده شوید
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13899" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معاریو : اسرائیل حملِه‌های جدیدی تو ایران رو شروع کرد
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/13898" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روابط عمومی سازمان منطقه ویژه‌اقتصادی پتروشیمی اعلام کرد:
بر اساس تصمیم فرماندهی ارشد پدافند غیرعامل، دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13897" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : نیروی هوایی اسرائیل ۲۰ تا هدف تو ایران رو زده که شامل فرودگاه مهر آباد هم میشده
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13896" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانال 12 اسرائیل
🇮🇱
:
کابینه امنیتی اسرائیل برای ساعت 11 صبح یه جلسه اضطراری فراخوندن تا درباره اتفاقات اخیر و واکنش بعدی به حمله ایران تصمیم بگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13895" target="_blank">📅 08:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">منابع عبری اعلام کردند حمله موشکی اخیر علیه اسرائیل به صورت
مشترک
از سوی
ایران و یمن
انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13894" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055b784f0d.mp4?token=W0ETkn4BNwhN2-w0IJeojRXKT7zHhgwN1coEZ5RuFmLkaOrKoXiFnhYqgfZWesFIcj7pCtkzsY61DAbfYGvvFv3idQ4ffehQxamblxpOs6DzcX9HKXyN9Wn-h3pc02khg03PhQe93ulZ-9oyF1Ncjbt_8vmuL_iFIeH7PdoLJq_0iOEoNY9jYCNT_-hMfQiBFcPZfZHqgHv45b7rteNGL0dzmht2TEzSAVPvCwzZWmHt4AUt6tWj6NqvFY8mbZ5a28Wo6M4r5YNUg3IMXuvQnZ3XZ-igI59izltz_cX0dpgLr0BivVVqbh27gYZeWSkCedLtnprABBIw7RzEhog01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055b784f0d.mp4?token=W0ETkn4BNwhN2-w0IJeojRXKT7zHhgwN1coEZ5RuFmLkaOrKoXiFnhYqgfZWesFIcj7pCtkzsY61DAbfYGvvFv3idQ4ffehQxamblxpOs6DzcX9HKXyN9Wn-h3pc02khg03PhQe93ulZ-9oyF1Ncjbt_8vmuL_iFIeH7PdoLJq_0iOEoNY9jYCNT_-hMfQiBFcPZfZHqgHv45b7rteNGL0dzmht2TEzSAVPvCwzZWmHt4AUt6tWj6NqvFY8mbZ5a28Wo6M4r5YNUg3IMXuvQnZ3XZ-igI59izltz_cX0dpgLr0BivVVqbh27gYZeWSkCedLtnprABBIw7RzEhog01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصویر از
حملات به پتروشیمی خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13893" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانال ۱۲ عبری: قیمت نفت در ساعات اخیر ۴٪ افزایش یافته و اکنون حدود ۹۷ دلار برای هر بشکه است
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/13892" target="_blank">📅 08:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12e8692ad.mp4?token=vSn2o2TwS8C8Xb_zf6VEpG_ZxOMr69B71O6lpE3HYpiFM_DlVVurrMkPAtPILXKeYzFn9L9um3MSlp-j2GycryXSfpcnMk5blRnv1480Lh5ogWAsG4BdlqE6L9rNO0GYHJG_EqG_WTJlg-s93681wPzIuSZvn_j5aWeyNpA45VoEthbG-Xl1lenrd3SlT3-EXqQzklBSRBz-mvyg1Uyt_6zqijNc_DDwEf-qY1ucJFDoRWpR98vtpX-_JiJ4PdQxMpau_PDmuggiurCTG_AmHnxrLasQ8ULTwCgtSF9J2Zy6dpeK8XoZ76H7udrmeBRP8qltDpcwwfnaoMEQmMR6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12e8692ad.mp4?token=vSn2o2TwS8C8Xb_zf6VEpG_ZxOMr69B71O6lpE3HYpiFM_DlVVurrMkPAtPILXKeYzFn9L9um3MSlp-j2GycryXSfpcnMk5blRnv1480Lh5ogWAsG4BdlqE6L9rNO0GYHJG_EqG_WTJlg-s93681wPzIuSZvn_j5aWeyNpA45VoEthbG-Xl1lenrd3SlT3-EXqQzklBSRBz-mvyg1Uyt_6zqijNc_DDwEf-qY1ucJFDoRWpR98vtpX-_JiJ4PdQxMpau_PDmuggiurCTG_AmHnxrLasQ8ULTwCgtSF9J2Zy6dpeK8XoZ76H7udrmeBRP8qltDpcwwfnaoMEQmMR6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل برخورد موشک
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/13891" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f25d56c33.mp4?token=RzneR0X4v5uyuPdCxmfRvgTsUiUck078pEINb3uf1m8plfCViDFG2hQdBrHep76IhgxqagJaSe8XadVKUV-TE33tlkgAPNqXe09gAgv338pO0FMs9h2vrgQ7xBimjDlMglom2od3tG4WbVgVMkzN3331t8yNOMwrFREyAamcmNU2OK5Amq9pUssiJi5uAxFVqoYU3GVvFh3tia3NEKRqkyki8qdhGEz59nwK-JsoSe9mpFYJ7sp1EGiIm3ZQKNPnem7mwv35mNfBN2y98NJM94BL3ub4f2rCr4t2lA9b0Tq8SF3RGBqZAgVjCsIc9rS_4XsGJ8X51X0Shw6cfegK_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f25d56c33.mp4?token=RzneR0X4v5uyuPdCxmfRvgTsUiUck078pEINb3uf1m8plfCViDFG2hQdBrHep76IhgxqagJaSe8XadVKUV-TE33tlkgAPNqXe09gAgv338pO0FMs9h2vrgQ7xBimjDlMglom2od3tG4WbVgVMkzN3331t8yNOMwrFREyAamcmNU2OK5Amq9pUssiJi5uAxFVqoYU3GVvFh3tia3NEKRqkyki8qdhGEz59nwK-JsoSe9mpFYJ7sp1EGiIm3ZQKNPnem7mwv35mNfBN2y98NJM94BL3ub4f2rCr4t2lA9b0Tq8SF3RGBqZAgVjCsIc9rS_4XsGJ8X51X0Shw6cfegK_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسمان اسرائیل هم اکنون
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13890" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بچه های‌ توییتر X</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/13889" target="_blank">📅 08:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.و این اخبار‌فیک نیوزه
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/13888" target="_blank">📅 08:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تایید کردند رسانه های داخلی ، پتروشیمی کارون تو خرمشهر رو با موشک زدن
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/13887" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4857e26854.mp4?token=rVskG8JVNXHGGUdK5r8IyrJNEw4z3SArpNXP8WYE5dNAK2WNd-yxSgReFo0K0yV6q8kItwzB4Zp3CNY04D0-1Hgk7FLbX6GVUI5J_yh9kzos7IyUjL7hbeKCcd5-zXbCCzQAmhy8WdsZXD9O5HVdAgYOuHf2vkyiYq6yxa4GoiJIHgrI28gNSjxmaQK2_fBuV5s0UJ9jMj9b6J0Cqzy22ILiw4xhi1onQNpLXVGH26gPTgw13b6J5izp7NIIk1pwmSKOG9jp5eWC1bTNShjqj27c1h3rhFAyYHcHgRvk41ycS3Osqfp4xd3ZusU9Y11UbhDuUuEjmWUQ0F4u6lOmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4857e26854.mp4?token=rVskG8JVNXHGGUdK5r8IyrJNEw4z3SArpNXP8WYE5dNAK2WNd-yxSgReFo0K0yV6q8kItwzB4Zp3CNY04D0-1Hgk7FLbX6GVUI5J_yh9kzos7IyUjL7hbeKCcd5-zXbCCzQAmhy8WdsZXD9O5HVdAgYOuHf2vkyiYq6yxa4GoiJIHgrI28gNSjxmaQK2_fBuV5s0UJ9jMj9b6J0Cqzy22ILiw4xhi1onQNpLXVGH26gPTgw13b6J5izp7NIIk1pwmSKOG9jp5eWC1bTNShjqj27c1h3rhFAyYHcHgRvk41ycS3Osqfp4xd3ZusU9Y11UbhDuUuEjmWUQ0F4u6lOmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهران ، ملارد
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/13886" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با شما : همین الان صدای چندتا انفجار از دور میاد. فکر کنم اسرائیل داره پادگان های اطراف رو می زنه. کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13885" target="_blank">📅 08:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13884" target="_blank">📅 08:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
انفجار شدید خوزستان پتروشیمی کارون ماهشهر
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13883" target="_blank">📅 07:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c56584ea.mp4?token=b46Zt9VkV8SUCDOJW7Q2XSd9oX_jipWQZlW4z-5XGRKEPNsBmkpA4pfj1-xCtZDPWDVlI8PDdoh-yJZtSLVuFemRq3X7WK58gNL6btZfW-ss-I5Nv7JkJLkS7TCmPOyE_SgkM2RRW5OjnEQ1kIHtJWapf-LJ46CXtSOcMedl-MwSZmzsuJqmZk_QcXerO4ANzMRl6IhINOQGWmpE5TSedNkGyOiLgg9_GI-Iz26_-rh_Y3wyIdNLIQ6eb2Y_mv6ACKKLwm5pZSWAaONSveIChEiWcG9DK5GarCBR1fxSV3cqn8puSZyPibfB0Q4awpm5f8mwAxPI7pQN8Q-iyjpyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c56584ea.mp4?token=b46Zt9VkV8SUCDOJW7Q2XSd9oX_jipWQZlW4z-5XGRKEPNsBmkpA4pfj1-xCtZDPWDVlI8PDdoh-yJZtSLVuFemRq3X7WK58gNL6btZfW-ss-I5Nv7JkJLkS7TCmPOyE_SgkM2RRW5OjnEQ1kIHtJWapf-LJ46CXtSOcMedl-MwSZmzsuJqmZk_QcXerO4ANzMRl6IhINOQGWmpE5TSedNkGyOiLgg9_GI-Iz26_-rh_Y3wyIdNLIQ6eb2Y_mv6ACKKLwm5pZSWAaONSveIChEiWcG9DK5GarCBR1fxSV3cqn8puSZyPibfB0Q4awpm5f8mwAxPI7pQN8Q-iyjpyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه همین الان
💥
💥
💥
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13882" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23c442104.mp4?token=h1idfBsoLASpghsix2Ln79ODfPjQRywMzBE7R7ageMUArBaMBFy-XT9Miq3fP6kHR-zq428lfaMyuX-zLPEd_aYE0-UJA8j55uQcxOn_kKzqho69OSTvT8GrTu9EFSMWVeZjlDhm_1SJQnTF36W67tGfQNhOefqUbtm4ceJXHGiT-AVW6MCuj5rKOq3w-j5RfpUQV6V5LuKbEyy2BZazlNJlmAPIsdZrnA-SwR4Ngc62kfzAFBaycEk8uk1DdUSLB36QiQwVp8NZN1-YLSSpKa40fggXu2NywkBYJhqr4XnwvNHSI9zvFFAYq3oVO0TyEPwsFIX7ZX-lK9FaVadHuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23c442104.mp4?token=h1idfBsoLASpghsix2Ln79ODfPjQRywMzBE7R7ageMUArBaMBFy-XT9Miq3fP6kHR-zq428lfaMyuX-zLPEd_aYE0-UJA8j55uQcxOn_kKzqho69OSTvT8GrTu9EFSMWVeZjlDhm_1SJQnTF36W67tGfQNhOefqUbtm4ceJXHGiT-AVW6MCuj5rKOq3w-j5RfpUQV6V5LuKbEyy2BZazlNJlmAPIsdZrnA-SwR4Ngc62kfzAFBaycEk8uk1DdUSLB36QiQwVp8NZN1-YLSSpKa40fggXu2NywkBYJhqr4XnwvNHSI9zvFFAYq3oVO0TyEPwsFIX7ZX-lK9FaVadHuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک از اصفهان نجف آباد
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/13881" target="_blank">📅 07:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همین الان از بیدگنه ملارد هم موشک شلیک شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13880" target="_blank">📅 07:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef3a93ff3e.mp4?token=Jx4Ma1NnsTujV8cfXw_jy9DPqdTHHG4TL-Xd-autCnaG6a4YCHsnYZc1UP3dJdzb4M-YeI27hJIgEiuyr8GdmXf5HtWU82izvCpr_gswGk0MnKDtLIUPkK0Ozj9T3O1sVPf_gOfGCiWCW6IaEX72bL0p2XnkzzCbT87ULjNjdC5pAuqu76BtiixYhHbWzgyQaZjKsxl19EQE95vq1LcIIUffr-te8PVhccDPiV78OqE_wUFoc3h8LGvhsyTnTi8L4Yo55o1h1KYzhWm7HFaYSmSDlOM0HtFFpKfrYrzezKhjTy0ZuPsV8ocKQUQ1hnXjCGq0fStlxwprEMl0y2SWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef3a93ff3e.mp4?token=Jx4Ma1NnsTujV8cfXw_jy9DPqdTHHG4TL-Xd-autCnaG6a4YCHsnYZc1UP3dJdzb4M-YeI27hJIgEiuyr8GdmXf5HtWU82izvCpr_gswGk0MnKDtLIUPkK0Ozj9T3O1sVPf_gOfGCiWCW6IaEX72bL0p2XnkzzCbT87ULjNjdC5pAuqu76BtiixYhHbWzgyQaZjKsxl19EQE95vq1LcIIUffr-te8PVhccDPiV78OqE_wUFoc3h8LGvhsyTnTi8L4Yo55o1h1KYzhWm7HFaYSmSDlOM0HtFFpKfrYrzezKhjTy0ZuPsV8ocKQUQ1hnXjCGq0fStlxwprEMl0y2SWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرمانشاه الان
💥
💥
💥
💥
💥
عجب فیلمی
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13879" target="_blank">📅 07:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxHZoMm2h44521yZZXHhIHIVotvxnA7NHe5UkDqPxy200qVzfqWwRFY3iQZCoqVI3XZn4GDQAV1lsN3hqhuPLOw9hU4EsJ4iGP5zjP2_jfCn_GfRA2JyPnLt47v2OFoTblst_Sj6bpxRteQORDsGXyHOepSvbEzn-N09R5weVRtcTHpYZHd_vIRPoFqUCy5qlFeaSEf9NWk5Sb9jPxf62gQMRDGlhjj1KEd68wRXsiEbmGSibl0enAL5hBUy3ATfSNjiRoqtqeAA9ft_F1TrB3CYQy-G71G7VWaklOrIroLoK1xth8NyEWWFVKbRqnmO2Rpt4E6H3V7ioVwY_05kCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارومیه الان ، پرتاب موشک
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13878" target="_blank">📅 07:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
جنگ ادامه دارد
از کرمانشاه و ارومیه و نجف آباد اصفهان موشک پرتاب شد
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13877" target="_blank">📅 07:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253ecda636.mp4?token=J9b24eYulsZlrkRlxPw91ket4RbCcLtwnu3nOIw0NaE-Trs_UUD7MpM8FBvhAOp7lHdYfN9mfvtzbUwKAVbV8AQdcWWJ36FFFTyKziRVgfpbooG2hOwfCSv5zetAMPyfLYMbF9U4dhuHA_CxHH0Yvoq8Ac894v-Dm45BL2n7bujUTmi7JW69eOZnAqDFhRTGo03Mpm9NkG0bZGimrhMv3RMeXYGUHgQhave4hMjNnOZhT_5w1t2erFoEiAmfqmeah1al7ksVjd9tk-8iiL1De9PfF--7zRS-1l3n7UaE_EjdZX5ZzPdizh6H9OsiPfSNAdO0ScYUdePMq4Vdq1wsMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253ecda636.mp4?token=J9b24eYulsZlrkRlxPw91ket4RbCcLtwnu3nOIw0NaE-Trs_UUD7MpM8FBvhAOp7lHdYfN9mfvtzbUwKAVbV8AQdcWWJ36FFFTyKziRVgfpbooG2hOwfCSv5zetAMPyfLYMbF9U4dhuHA_CxHH0Yvoq8Ac894v-Dm45BL2n7bujUTmi7JW69eOZnAqDFhRTGo03Mpm9NkG0bZGimrhMv3RMeXYGUHgQhave4hMjNnOZhT_5w1t2erFoEiAmfqmeah1al7ksVjd9tk-8iiL1De9PfF--7zRS-1l3n7UaE_EjdZX5ZzPdizh6H9OsiPfSNAdO0ScYUdePMq4Vdq1wsMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غرب تهران همین الان
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13876" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62915c8412.mp4?token=pe4LD7zZbeLHvlLjXKaGPLvv1-mutbp8kn4-Uc6Q2fpS0tzuJsSMHf4OfR98Lfa0WdNYFzphShxyJDx9us56s6YYIjceY2gj3TgNxEXzckcg9dvkiDlwKVS-02UgKSn4Vm56sMu_szEuPTEYU2V6BCljanudZtNQggWYTBMtNHKSNgBd6bP3LhxBySUc6EF1f0BYbA3F1R8kqsKzU-lvlttuqs9M8Np9RRqC6qdQv5zWvO7VVqFKsvvGHar913SNCVxRHl3uZU4SxxR2_59RVZYUOII2jIJKnLIPB3uxPGeAmXOZ4KQdMQjd8Q5Qulfitn4WfIaGYu-4jRQMuZPcSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62915c8412.mp4?token=pe4LD7zZbeLHvlLjXKaGPLvv1-mutbp8kn4-Uc6Q2fpS0tzuJsSMHf4OfR98Lfa0WdNYFzphShxyJDx9us56s6YYIjceY2gj3TgNxEXzckcg9dvkiDlwKVS-02UgKSn4Vm56sMu_szEuPTEYU2V6BCljanudZtNQggWYTBMtNHKSNgBd6bP3LhxBySUc6EF1f0BYbA3F1R8kqsKzU-lvlttuqs9M8Np9RRqC6qdQv5zWvO7VVqFKsvvGHar913SNCVxRHl3uZU4SxxR2_59RVZYUOII2jIJKnLIPB3uxPGeAmXOZ4KQdMQjd8Q5Qulfitn4WfIaGYu-4jRQMuZPcSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجف اباد اصفهان
صبح ساعت یک ربع به ۵
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13875" target="_blank">📅 07:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسرائیل حدوداً ساعت 4:43 دقیقه به 15 الی 20 نقطه در تهران (فرودگاه مهراباد)، سایت‌ها و کارخانه‌های موشکی و پهبادی در کرمانشاه و اصفهان و تبریز حمله کرد. جنگنده‌ای هم وارد خاک ایران نشد و پشت مرزها از عراق به داخل ایران شلیک کردن.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13874" target="_blank">📅 07:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106a64a308.mp4?token=EcxNZHopd8mBrlzKASAzkG8fnyLIBoP_qf7zcuStDzBRQS7ng6mwsZ5eAGHOMl78nlxhN7h3p6dN7XX6ox12EwqSlffeiAIsuSYG-DokqzCatdcwL8tbTDqvHUjGu7yaX_kO9G9Qw-SyRbf-5R_98n9qIvoadBXMh8_92haum4Zpug8TDybIsmenkGcruXymXMLGDn_qB__rebjG362oj-1XhVnzsAoHm3lZa3Y0REDAcHuZNX-YZ3PYajhVUN9_WWcifiz4C_IMcG5V9yy9wB5w8OPHhep8VFOZlpkFohQUlQy7qIhCiDtgsTl8YMvEvLEJ3HEgQKVxKrodS4DNSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106a64a308.mp4?token=EcxNZHopd8mBrlzKASAzkG8fnyLIBoP_qf7zcuStDzBRQS7ng6mwsZ5eAGHOMl78nlxhN7h3p6dN7XX6ox12EwqSlffeiAIsuSYG-DokqzCatdcwL8tbTDqvHUjGu7yaX_kO9G9Qw-SyRbf-5R_98n9qIvoadBXMh8_92haum4Zpug8TDybIsmenkGcruXymXMLGDn_qB__rebjG362oj-1XhVnzsAoHm3lZa3Y0REDAcHuZNX-YZ3PYajhVUN9_WWcifiz4C_IMcG5V9yy9wB5w8OPHhep8VFOZlpkFohQUlQy7qIhCiDtgsTl8YMvEvLEJ3HEgQKVxKrodS4DNSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13873" target="_blank">📅 07:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1447170a.mp4?token=p3UcWcCh2tDOKHA5HYIKx_-T7PuS7L-smTs0hDEh_EZVHIJBpFXAyeETz2XvZGLeKGDVJN0GaBqtmwcEZ1aw6Sa4gRWvf4aSaFiTAXxgXSps6uFAO_6PhnnEJgadzN37chKG3bRhDQHp3NOhFg6tiPMVWqXLolH5oYcRBQzInDa6a1IqqHfGRRwyr85LnPXlSmzx6zG0bc1exd9UDkSXsphczrh77fiRqAG9KKjggHcRPNRhRXO5QCF7vLccdQbgmxeoicFyYdgsWmq2JtYcHjIIwCpWk4UJrs8tdZggiICiw3JQZg1ptUd9og7cetBYbPm4ZUGKBZCr9EGHYF2nOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1447170a.mp4?token=p3UcWcCh2tDOKHA5HYIKx_-T7PuS7L-smTs0hDEh_EZVHIJBpFXAyeETz2XvZGLeKGDVJN0GaBqtmwcEZ1aw6Sa4gRWvf4aSaFiTAXxgXSps6uFAO_6PhnnEJgadzN37chKG3bRhDQHp3NOhFg6tiPMVWqXLolH5oYcRBQzInDa6a1IqqHfGRRwyr85LnPXlSmzx6zG0bc1exd9UDkSXsphczrh77fiRqAG9KKjggHcRPNRhRXO5QCF7vLccdQbgmxeoicFyYdgsWmq2JtYcHjIIwCpWk4UJrs8tdZggiICiw3JQZg1ptUd9og7cetBYbPm4ZUGKBZCr9EGHYF2nOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملارد ، تهران
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13872" target="_blank">📅 07:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRDZPCQPChi7gBVspOGnU5uYBJHE5Z_qJoVb8ABrH0TCOvZgrITTTZrC4lb1NlcBnK24GT06WsAq-qbMetGw6HPzXgUp3A7Dy9VJRlm-RGht9syS16NA3xIO5ampwk6AfkgcL-IekvgnMd3_Z9M-vTuh6zU4BhRP_PewucXCMItmD5RqTQZAQtcSgfZuPd2taJMDlIRnjIQ9gTPzumLpSx6ZZ0XYo0ukIMJuzcZa3DDKJq5GZJ8kS0rPX-V9sOxjSsvoQyIC0YKSl5KcshKrTOeSW2Chu2mHATWz3egF-UwInAzd58BH6jMcn3xlDTzigh6zh4ca49LPEJbKn8n_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13871" target="_blank">📅 07:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5O9mqPb9g4TzvKkdpkEirVzRcy8kSmbPvhjtJ5dIco6Hmt2xW6OcZIr53unNIjTVeF966QjgTKOcTqPnTKGjhpgdMaRF-fcCzAYJyMHEEqoxxfdISjJgujX20oYBhbEpvoI5DSAGQEkBvpRuNLAsVM6QOLglVvaXRJW1haOCAEifqqQwwVJPb386Qnm9ic5hXoA1ggKo_oXc5TgJ6IKKc2Pla835Jfhit6uXHqbadZP0BPn6lF4UUUHTP2Nv13nar_YmU6_N50vrQvQ2v3SDWYi9iDd9-qDaiaueY_nv_1E9G8VNjdKfuT2GvcPq3dtI60jw1KgzAl5a3985IOo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13870" target="_blank">📅 07:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از یک مقام ارشد اسرائیلی: ما در آغاز نبرد چند روزه علیه ایران و دست نشاندگان آنها در خاورمیانه هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/13869" target="_blank">📅 07:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اکسیوس به نقل از یک مقام آمریکایی:
حملات اسرائیل به ایران محدود بود.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13868" target="_blank">📅 06:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به گزارش ایسنا، سازمان آتش‌نشانی تهران می‌گوید هیچ منطقه شهری در پایتخت هدف قرار نگرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13867" target="_blank">📅 06:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۳پا: دشمن اسرائیلی با استفاده از موشک های بالستیک هواپرتاب اقدام به حمله به اهدافی در خاک کشورمان کرده است
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13866" target="_blank">📅 06:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">استوری اخر اینستاگرام رو دیدید ؟! سیگنالو دادم که دم صب میزنه !</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13865" target="_blank">📅 06:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زلزله ۸.۳ ریشتری در فیلیپین
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13864" target="_blank">📅 03:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اکسیوس، به نقل از یک مقام آمریکایی: مذاکرات با ایران به سه ماهه پایانی رسیده است و به خطر انداختن توافق احتمالی در این برهه حساس، عاقلانه نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13863" target="_blank">📅 03:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0bf5cd579.mp4?token=h9fNaQPhnSpWYf74xmfzR6xLjbyOfxz3FsKoTxER6XJ9fjCyjK9S4pJeShV4IpximVOf3Udm2uKYz9_Im8z-YH23HpVHqDpUYBZGe9PYBwCgOqGeh3OM1vVFvUSF_-mPsEjPhM7BjOFiZixa5m8nGr2H948EQc29Lc75cm9oUQITB4-qoNp4Thac7oAYGy67-qSnly4LCryv9hqdkiwzERw4zJkQFOdzkMkPwtgYI3nm5CKjMAXNW-dBZITxo6HEpzWGvFtZuvtrugdPjGa-ETiUkK4FHpktTadCnjVU98YuDgUs651VVQvkNYtxgGXL6dPVUDfshF7JMzIX-1Z_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0bf5cd579.mp4?token=h9fNaQPhnSpWYf74xmfzR6xLjbyOfxz3FsKoTxER6XJ9fjCyjK9S4pJeShV4IpximVOf3Udm2uKYz9_Im8z-YH23HpVHqDpUYBZGe9PYBwCgOqGeh3OM1vVFvUSF_-mPsEjPhM7BjOFiZixa5m8nGr2H948EQc29Lc75cm9oUQITB4-qoNp4Thac7oAYGy67-qSnly4LCryv9hqdkiwzERw4zJkQFOdzkMkPwtgYI3nm5CKjMAXNW-dBZITxo6HEpzWGvFtZuvtrugdPjGa-ETiUkK4FHpktTadCnjVU98YuDgUs651VVQvkNYtxgGXL6dPVUDfshF7JMzIX-1Z_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ از مرکز تهران، آسمان شلوغ، پهپاد / جنگنده، گشتزنی بر فراز تهران، همه منتظر و چشم به آسمان.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13862" target="_blank">📅 03:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13861" target="_blank">📅 02:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXSh87JMQoub1cqWb56j--JXAywHxhFmhivMCUcnUDaUzB48qaaXtb2nWu4okPO39nmEAz7iy0h9aLitDnYxhFwcE6Vldk6Nkuj2Ym5r10sFdAf9-dja5hwEUU0RNJgj8C13-ReMmwt22i6q-nDr8qbzdJXq1TmTGrvOXtWjp-bVVndqgfXESLLVhi2HKbQkppA2Ljupw1NDnLHfKwlzDg-oqamXNrJYo8WS4ShHwZ3Eisn_Lqh_0lyR9vt1KJlJGNgAYmViXFcP-SwoTAaaYzM41LpQeEFbSonbvOZ1ILVHwpstTnAiXpYefxn9FtKSNkKGYtDaQRyqq8lGCTDplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت من هم اکنون
😹
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13860" target="_blank">📅 02:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران به سمت گروه های کرد مخالف ایرانی در سلیمانیه عراق پهپاد شلیک کرده است @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13859" target="_blank">📅 02:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه رسمی فیفا:
دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13858" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce56e7367.mp4?token=esJond8UHBswB4eByMAP0uD814OF8FpLwi9GHyGj2LOvFlpop9H0CGKn4eYLU_EBQ7r4ZYhwIkiaxTKkptUK5TZHX6h8UlL5fVVYT6PrtNl_GgyUDJcoSsoHLRVrfpdltSOIk6es43-amZwfqckCW1X_yZoLd8m5oPNtRcJYgo7hnyhXGbdlY4L4q_97sRygCKjq-V7d-MD6--4hdvFX6Pu7zdx8_EmGa9pRHS_3ZiddeJoQLwxPYr7FDhFbLspgF78Wi-MIHkmE_3ClHEYedunlUFs9VaNfei2EceVN9c_ixXeDtVAH-HL00nxGDMHR-b0uX-evmmSLr2v-BCCsfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce56e7367.mp4?token=esJond8UHBswB4eByMAP0uD814OF8FpLwi9GHyGj2LOvFlpop9H0CGKn4eYLU_EBQ7r4ZYhwIkiaxTKkptUK5TZHX6h8UlL5fVVYT6PrtNl_GgyUDJcoSsoHLRVrfpdltSOIk6es43-amZwfqckCW1X_yZoLd8m5oPNtRcJYgo7hnyhXGbdlY4L4q_97sRygCKjq-V7d-MD6--4hdvFX6Pu7zdx8_EmGa9pRHS_3ZiddeJoQLwxPYr7FDhFbLspgF78Wi-MIHkmE_3ClHEYedunlUFs9VaNfei2EceVN9c_ixXeDtVAH-HL00nxGDMHR-b0uX-evmmSLr2v-BCCsfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
Israeli Medley (Hebrew) by Leila Forouhar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/13857" target="_blank">📅 02:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک مقام آمریکایی به کانال ۱۲ تلویزیون اسرائیل گفت: نتانیاهو به نوعی موافقت کرده است که پاسخ اسرائیل به ایران را به تعویق بیندازد.
@withyashar
یاشار: اسرائیل همانطور که گفتم فقط کارش قافلگیری ‌است و هیچی نشون نمیده ! هر لحظه ممکنه برنه !</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/13856" target="_blank">📅 02:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تسنیم: ایران از یک‌ پهپاد ناشناخته جدید در حملات اخیر علیه اسرائیل استفاده کرد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13855" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رسانه وابسته به سپاه گزارش داده که در تهران، هواپیماهای مسافربری غیرنظامی به‌دلیل انتظار حملات اسرائیل در حال جابه‌جایی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13854" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13853" target="_blank">📅 02:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دادگاه فردا نتانیاهو لغو شد!
جلسه‌ای که قرار بود فردا در چارچوب بررسی پرونده‌های قضایی بنیامین نتانیاهو برگزار شود، به دلیل وضعیت امنیتی و شرایط جاری در منطقه لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13852" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">من یه بیت رهبری برم بیام
😹</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13851" target="_blank">📅 02:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: محاصره ممکن است قوی تر از هر حمله ای باشد که به ایران آغاز شده است‌‌
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13850" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">همه رسانه های عبری دسته جمعی از تصمیم نتانیاهو مبنی بر حمله گسترده به ایران ، خبر میدهند
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13849" target="_blank">📅 01:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625147ce42.mp4?token=jVsQ5sszH8jf9SoqXm0Ym5jPQNEOp5R1nnTjVcmaf51ZXv9TeRXtqZ-7OMOn6DPt71emYahw9RpDSnX0W3spi3-ns6wd5-8tN89Xri53FHxvB5fRIlU_yr2mDikR7ymeTwAwIjYqZkr3OwJSWZF21b70UvBSRlTk0v9RucFZtWbv9KMCyV3_PuQOxUquxuJ5Xt_7qeFDgsl1pBqOR0yT98rKydSSd4_o2LV3rVMwBncTGZk-2hFYjbjTg7NIx5YaU3mLvyxj14-IBOL1WsNRsuLLohNAOiEN_3bMfeEyprjROA4_UVWk8OyaO9E_wCgXVTuP3Km0JRcc7VStHZp14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625147ce42.mp4?token=jVsQ5sszH8jf9SoqXm0Ym5jPQNEOp5R1nnTjVcmaf51ZXv9TeRXtqZ-7OMOn6DPt71emYahw9RpDSnX0W3spi3-ns6wd5-8tN89Xri53FHxvB5fRIlU_yr2mDikR7ymeTwAwIjYqZkr3OwJSWZF21b70UvBSRlTk0v9RucFZtWbv9KMCyV3_PuQOxUquxuJ5Xt_7qeFDgsl1pBqOR0yT98rKydSSd4_o2LV3rVMwBncTGZk-2hFYjbjTg7NIx5YaU3mLvyxj14-IBOL1WsNRsuLLohNAOiEN_3bMfeEyprjROA4_UVWk8OyaO9E_wCgXVTuP3Km0JRcc7VStHZp14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13848" target="_blank">📅 01:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: اگر توافق به دلیل بندهاش فرو بپاشه، ما گزینه انجام یک حمله کماندویی به ایران رو بررسی خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13846" target="_blank">📅 01:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هشدار آمریکا برای شهروندان خارج از کشور: احتیاط کنید , از جا به جایی بپرهیزید
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13845" target="_blank">📅 01:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ:
نتانیاهو «چاره‌ای نخواهد داشت» جز اینکه توافق با ایران را بپذیرد.
من فرمان‌ها را صادر می‌کنم. من همه فرمان‌ها را صادر می‌کنم. نتانیاهو فرمان‌ها را صادر نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13844" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسانه‌های اسرائیلی : ایستگاه‌های مترو در خط قرمز تمام شب باز خواهند بود و طبق دستور فرماندهی جبهه داخلی اسرائیل، به‌عنوان پناهگاه برای ساکنان مورد استفاده قرار می‌گیرن.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13843" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو وارد یه جلسه امنیتی گسترده با وزیر جنگ، فرماندهان ارتش و موساد شده
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13842" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر کشور پاکستان از تهران در رفت
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13841" target="_blank">📅 01:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس: شلیک‌ها از آن جایی انجام شد که ترامپ می‌گفت نابودشان کرده است
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13840" target="_blank">📅 01:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل هیوم به نقل از یک مقام امنیتی: اسرائیل احتمالا حمله ایران را فوری پاسخ نمی‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13839" target="_blank">📅 01:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امشب ایران پس از ۶۱ روز اولین حمله موشکی خود به اسرائیل را انجام داد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13838" target="_blank">📅 01:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شبکه کان اسرائیل:
نتانیاهو هم‌اکنون پس از تماس تلفنی با ترامپ در حال برگزاری مشورت‌های امنیتیه.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13837" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اتاق جنگ با شما: سمت تهرانپارس صدای خیلی خیلی وحشتناک
از تمام صداهای تو این مدت بدتر
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13836" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منابع العربیه: عراقچی به پاکستان اطلاع داد که لبنان بخش جدایی‌ناپذیری از پرونده مذاکره است
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13835" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13834" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جمهوری اسلامی شدیداً در حال جابهجایی های استراتژیک هست تا در برابر حمله احتمالی اسرائیل کمترین آسیب را ببیند.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13833" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13832" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">منابع عبری : نیروی هوایی اسرائیل آماده پرواز میشود  @withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13831" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9v5DuiPNaKtEGMyfiXZ-NoxEXtsO8qijHRNo0xi5eK8GpUbSMqKjoy4XvnlNCBbLAqNtFg1Dah08GTJUTWThNFgOjb8I-lYMdaDM3kLEeUH3BEiEQXn2fjgQmY88ZOBhSzum99da_UQG1WgPhmjfL-AGw3-4PU40Esq1eZcgoC5Xgb9kptq_N9gpaoSossiho8GNWsKzVLS59a0NuphbAKazf9AqiK5f7UHKltazvtmHl8_UAdk_S2kj4Zxd8IG7PUC9o5JbYRVqQ3KNXmWzOaBJ0jSg5YVKi-OAPx82t8YKqxCV_kchId6eldoKCnKvVgClTZnsWUlUIL52Y_8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ میلیون ویو چنل تازه تا این لحظه … و زدن رکورد بازدید… مرسی از شما
🙌🏾</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13830" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایران به سمت گروه های کرد مخالف ایرانی در سلیمانیه عراق پهپاد شلیک کرده است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13829" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13828" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13827" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13826" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13825" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یدیعوت آحارونوت: بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که قصد حمله‌ای قدرتمند به ایران را دارد. رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13824" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق جنگ با شما : همین جوری هواپیما داره میاد بجنورد میشینه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13823" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تاکنون آمریکا برای اجرای حمله علیه ایران موافقت نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13822" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">والا به نقل از یک مقام ارشد اسرائیلی: پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13821" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صداوسیما : امشب از موشکهای سوخت مایع و جامد استفاده کردیم و معروفترین آنها موشک خیبر شکن بود.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13820" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه های‌داخلی : «معادله ۲ در برابر ۴» وارد فاز عملیاتی شده است
آنچه که از مرکز فرماندهی و کنترل سپاه به گوش می رسد
معادله دو در برابر چهار
، عملیاتی شده است.
فرماندهان ایرانی تصمیم خود را گرفته اند اول زدن اسرائیل، دوم انسداد باب المندب، سوم حفظ هرمز و چهارم رفع حصر با ناامن سازی کشتی های تجاری آمریکا و متحدانش.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13819" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رسانه های داخلی : پروازهای فرودگاه امام(ره) تا اطلاع ثانوی متوقف شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13818" target="_blank">📅 00:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو :
تصمیم گرفته شد حمله امشب انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/13817" target="_blank">📅 00:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منابع عبری : نیروی هوایی اسرائیل آماده پرواز میشود
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13816" target="_blank">📅 00:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس: ما بخشی از این عملیات نیستیم.
اما هنوز مشخص نیست که آیا دونالد ترامپ به ارتش آمریکا دستور خواهد داد که در صورت حمله احتمالی اسرائیل به ایران، هیچ کمکی به اسرائیل نکند یا نه؛ به‌ویژه در زمینه‌هایی مانند سوخت‌رسانی هوایی و سایر هماهنگی‌های نظامی.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13815" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منابع عبری : تماس تلفنی ترامپ ‌و نتانیاهو تموم شد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13814" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">«رئیس ستاد ارتش اسرائیل می‌گوید ارتش به محض صدور دستور، با قاطعیت «دشمن» را هدف قرار خواهد داد.»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13813" target="_blank">📅 00:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13812">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۵ اسرائیل:
پس از پایان گفتگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13812" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13811">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13811" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13810">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری وای نت اسرائیل: آمریکا پیامی به اسرائیل فرستاده و گفته چند روز صبر کنه تا ببینه آیا میشه به توافقی دست یافت یا نه.
اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد و ارزش نداره که این فرصت رو با درگیر شدن در تبادل ضربات محدود هدر بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13810" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13809">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به باراک راوید خبرنگار آکسیوس : هر کدام از آنها خوش گذراندند. اسرائیل حمله خود را داشت و ایران هم حمله خود را.
مابه حمله دیگری نیازنداریم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13809" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۴ اسرائیل :«نتانیاهو باید حتی به قیمت رویارویی با ترامپ به بمباران ایرانی پاسخ دهد.»
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13808" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13807" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13806">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فاکس نیوز: با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13806" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
