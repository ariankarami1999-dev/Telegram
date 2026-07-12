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
<img src="https://cdn4.telesco.pe/file/O_5R1VxoJwHHpPyHiBZWQwDdYeiB6LkgetkJemPDZNoPmJ06JefkeicR0BqDiBOHhPeOIXeeUSTA24k4FzPM5nd7i7UBuvh3b_G1U59QTl0HVMpXQ2_P5QCVM-7O-d9q4miWJ9qTMH0aYMbnXYuF5HkXOQIFqX0N_-_0M68x04WiC9ufbxnZXDk5GPUePC5sDbUyB2RlcNraWOvvIcG3h2wDdkBU41Ph0u6Ymj2UUAS5tONxBTUlojpJhrrda84V1JhKycXBnAQFkwG5gu9521uNOv2t02rycHZS0ARoV0IIoPcSXqBb6bxhPDxDMldsgbehpn0XbAhTizpj7avnnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 15:41:54</div>
<hr>

<div class="tg-post" id="msg-449396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/449396" target="_blank">📅 15:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7UDH8j855aqRChRH8LVA4BHgaRKSMtndizkPS5jn2tcbwgUjoK4K3dJQdTBHq1DUoI3Tw4bpq4FztIDsLyv3xjBQD6psTV-ZjJU0bLEq5j-yAgCYgdZSiQsmnbbGja2fPDusDcLCfrn4b8NMhVjI0RhLf6chV_XOVxjnsO4bj1PL23jGm5e9HxMbaby0Pfa8-L0jfhARZtzh7JIdjsBd3j3-kdNAS9D85daO59aSpf0jrt8tOdoF10CX5BlMJQ3SsabJA-5p_WJOyqVxqWjUaJXEXRHqo8I7Sj5fKZ58gYrPd_gZ2l5-gwjQVCnttLVQHWXliwlSJX-MiLTkgIBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: اهمیت تنگهٔ هرمز از ده‌ها بمب اتم بیشتر است
🔹
اگر دشمنان بتوانند فرهنگ رهبرکشی را در منطقه نهادینه کنند، امنیت هیچ کشوری تضمین نخواهد بود و به همین دلیل باید در برابر این اقدام ایستاد.
🔹
ترامپ و نتانیاهو از مهم‌ترین خطوط قرمز جمهوری اسلامی عبور کرده‌اند و باید پاسخ متناسب با این اقدام را دریافت کنند.
🔹
پس‌از این همه دشمنی و جنایت، سخن گفتن از دوستی با آمریکا معنایی ندارد و ملت ایران باید با قدرت از حقوق و عزت خود دفاع کند.
🔹
تنگهٔ هرمز همانند یک عامل بازدارندهٔ راهبردی عمل می‌کند؛ این گذرگاه راهبردی از ده‌ها بمب اتم نیز اهمیت بیشتری دارد و ایران از آن حفاظت خواهد کرد.
عکس: خدابخش مالمیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/449395" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
عمان از حمله پهپادی به چندین هدف در استان مسندم خبر داد
🔹
خبرگزاری رسمی عمان به نقل از یک منبع امنیتی اعلام کرد: چندین نقطه در استان مسندم هدف حملات پهپادی قرار گرفته است.
🔸
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/449394" target="_blank">📅 15:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKvaFiRRZM1ZF4eJcYPXHGtk2oUEokq1sCReoR7yk2x6Uep2imTVZCn88SbBZt8JCxcQ-kFYTBg9Rp1DFs0E5QHs_HCdofDcEJFH0OA_2cVyQFpQONGJaABZrClhPhdhcvV8guL5KYbl-7ayMXVu1GDgBc6coaE4l9t8uCJNDJpeqAaJ6ikwT4s7Y12fVDIZHl4gABQUCR2kOFSSVrGV0i5WmNg8_07zMOmfhJBt7SyfByYsMlurJBEGkn9ybhl7ecEJs7O_rS5sFrOfOak3edNhLlsTFr7G2xgd0A6cj_thefogxYpVqSAYY4tFEDjvWSocpFfGEuywK2yJP69Nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروریست‌ها با هوش مصنوعی بمب ساختند!
🔹
پژوهشی از دانشگاه کمبریج نشان می‌دهد اعضای گروه تروریستی بوکوحرام از چت‌بات‌های هوش مصنوعی برای برنامه‌ریزی عملیات، عیب‌یابی سلاح‌ها و حتی دریافت دستورالعمل‌های ساخت بمب استفاده کرده‌اند.
🔹
براساس این پژوهش، مدل‌هایی مانند ChatGPT، Gemini، Claude، Grok، Meta AI و DeepSeek برای دریافت اطلاعات فنی و طراحی حملات مورد استفاده قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/449393" target="_blank">📅 15:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltipGyBkmbmleQsm2Dg86aWEiMe7TSq4UjNjfltX1dB5lz9UNiy8MmNiQd43Qk2dEVPGQy-Lkg_DaTMMJnt7xUs0-f-3FoIoaROYY8VM7TQapXzmCe6Jhdk9H7nlAJWXcqjrp5XyB5cjayUWGK0r9WYwvEGbzgqA6qfn1s2jxi-C_O05sRUJWOnDk2s1jvfwCRXd8Ijw9IdPvZOPk8H2TkAHbpBC_-2DjLqxqZ3qL6sW5WY1MVZ4u35iKP6wcje3zEQpYqZbSto6W1J9FgdO8L8rBGb_2LdfhQRXSj4UZzT0MyhdLnTtk0xFex7f_-ICVOUe73KKJwHi1w_poORnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است
🔹
شناورها باید با نیروی دریایی سپاه هماهنگ باشند تا از تنگۀ هرمز عبور کنند.
🔹
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/449392" target="_blank">📅 15:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522a1a11b3.mp4?token=VfCTx-5IQ_kebr0teZCWRIJiim0w7kBVBEiolaWcVP4C7O6VkJuspNtY4BuZ6ICMGriLQHx3PpConZSdqm3CCuLkDbrNmjZG4q20E7DHpB7DbNX2HjVw_IsSDFoMX2UuspJOn-7Nyu0PWvr0qw_jXqvs_tBPOIRrhwLfYJ0jTKEfFsGkTfk6v9ZbZVobyDma1kf7qVH9CjpjHC97GwMZMDTOas3d_BSCXnp5CvXf3zQzh10Cc36t_ODrN0K81EuuW48tkaxHlXQ88nbwe62chDd6bjhWbggUcvAIsoN4bVkzRCjpcNI2Mc-ghkMmRt6rBWGNOgtMep7812Hu0pfR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522a1a11b3.mp4?token=VfCTx-5IQ_kebr0teZCWRIJiim0w7kBVBEiolaWcVP4C7O6VkJuspNtY4BuZ6ICMGriLQHx3PpConZSdqm3CCuLkDbrNmjZG4q20E7DHpB7DbNX2HjVw_IsSDFoMX2UuspJOn-7Nyu0PWvr0qw_jXqvs_tBPOIRrhwLfYJ0jTKEfFsGkTfk6v9ZbZVobyDma1kf7qVH9CjpjHC97GwMZMDTOas3d_BSCXnp5CvXf3zQzh10Cc36t_ODrN0K81EuuW48tkaxHlXQ88nbwe62chDd6bjhWbggUcvAIsoN4bVkzRCjpcNI2Mc-ghkMmRt6rBWGNOgtMep7812Hu0pfR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
صف طولانی زائران حرم رضوی برای حضور بر مزار مطهر «آقای شهید ایران» در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/449391" target="_blank">📅 15:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449390">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8qjlWTJUDfH9X0XYsYZ2sv33w6YpaX0LNGzuGNEn5FEgOs3iBRSDSC7nCHP3Jf0Y04J77Uusd7eMdl9UD6l2tGtoPfAhbbPmAkNwZFnMEVsWTm2dKokEYfGuCNhFbVMstpOr9Nb9ooeUVqBBdktdBw272IyQe_RGOyjM0GWRHat-_GRi5x68GzIbkf-tR8vQ0rsN046098-wC2x_E0ZDA84TDFU6T3G2uYOpQFYsdahQKQPRT8OnhcnrqHRqqsCm8-WM2LO1hPghZqJsFpJ7svkdHWdT-pWH6qFrI6qaFoEi4hKblWH0_krAI62-glgX2Xo6PYhrlyQNiP5sFxkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز فرماندهی نگهداری جنگنده‌ها در هم کوبیده شد
🔹
در پاسخ به ادامۀ تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/449390" target="_blank">📅 15:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cdb876f3.mp4?token=gVdKMG21xh_3h6bSy-kx0xaKI-RjKLlpRCVTLVZem0ZYGHL9HRqTmSUcQ6CHXkt5uVtfzIumud4ogBbRySCrhNi-TWQZfZRKUBxoWXkZUpZp3Lb2ZUXiEo45C5ok78qBbnpvLCecQpnIMzoj4goZTjWk2HojHvSdUp2ZMqRgglydCJNaFg56GbEwQAubJ0AiGPfHgRjhDCNiSWdo7SbAQDtzhEB6d1yeDlkJv9pHaXjUlgBJnQuw2QvrW_FjNEXSn-QgpMPAWRQcA0LwlJcoVxvBEa6tdEoYlD9ByAsAuSwryepxhEGorEzKV3ka5kmt9JB0aub3FsaI0Ws1h5XbxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cdb876f3.mp4?token=gVdKMG21xh_3h6bSy-kx0xaKI-RjKLlpRCVTLVZem0ZYGHL9HRqTmSUcQ6CHXkt5uVtfzIumud4ogBbRySCrhNi-TWQZfZRKUBxoWXkZUpZp3Lb2ZUXiEo45C5ok78qBbnpvLCecQpnIMzoj4goZTjWk2HojHvSdUp2ZMqRgglydCJNaFg56GbEwQAubJ0AiGPfHgRjhDCNiSWdo7SbAQDtzhEB6d1yeDlkJv9pHaXjUlgBJnQuw2QvrW_FjNEXSn-QgpMPAWRQcA0LwlJcoVxvBEa6tdEoYlD9ByAsAuSwryepxhEGorEzKV3ka5kmt9JB0aub3FsaI0Ws1h5XbxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقش رهبر شهید در جایگاه ایران و ایرانی در جهان از نگاه مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/449389" target="_blank">📅 15:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIANFFpIDeEklaDDwnagYR7KD9TKTtv6Am9BSJZptkyTYMCy_1TGC4f0kya7yDHZ90B6jKKutuJkA3yXvt1xUN_sXSXK95IRHXouXkWWbc4BCyTdV3nV603tOCdHOlZg8wpbFpQsLNyyxHxAjWe0se5yyd2HEvFgBS3mYXWdE_zVzAyzO9nhUxKsSwEpHAk5nkPKTuvctBrPxCmupl2GsbC0AcabY2_qgtXQ-vsvZmSdqP3pDt85E0TXGuUZDZFZSYphMA_1zmipM6ZStsfWPmdGCOtXw5Z0XEr_4YDtIuNmdmkDweNNRhbVl9-jDFPMr9Q5YtibBmttGUVb9ymesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت بانکی جای پول نقد را گرفت
🔹
براساس گزارش جدید شاپرک، در خرداد امسال حدود ۹۸.۸۲ درصد از تعداد تراکنش‌های شبکهٔ پرداخت و ۹۰.۳۳ درصد از ارزش آن‌ها به خرید کالا و خدمات اختصاص داشته که نشان‌دهندهٔ تبدیل‌شدن کارت‌های بانکی به ابزار اصلی خریدهای روزمره است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/449388" target="_blank">📅 15:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5c1155f2.mp4?token=XqXJxMEjKuaOHvRdvrJUy6kDR8-OC7nnfUBZTnuRN1n1auFDdVHCxHTA_Q2GoGj8M7tI7PV47Z38H7yc6hP_9DtJF0kol5Xylr88Haidm13SBkmXgVvkO5wcEixGatn2p3Hf9laHLzTiJ03uPlfE-BelqWyZ2yV-6jiptUTF7WVpHLOdRYZYHOZkg7Iu9p8Dajih1VfYFMaurBWa_zLh3Aetaliruwgapwln_KptJeU77iUCFya6IEKeE3kmi7FqkkxtrIQT-4F257mwF2viur8Uv5Yv5AP2a7ai15b7C4L9sW95tiYZGvceT4Vh-_D-WxHsjdni9Ked8HE07L1fAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5c1155f2.mp4?token=XqXJxMEjKuaOHvRdvrJUy6kDR8-OC7nnfUBZTnuRN1n1auFDdVHCxHTA_Q2GoGj8M7tI7PV47Z38H7yc6hP_9DtJF0kol5Xylr88Haidm13SBkmXgVvkO5wcEixGatn2p3Hf9laHLzTiJ03uPlfE-BelqWyZ2yV-6jiptUTF7WVpHLOdRYZYHOZkg7Iu9p8Dajih1VfYFMaurBWa_zLh3Aetaliruwgapwln_KptJeU77iUCFya6IEKeE3kmi7FqkkxtrIQT-4F257mwF2viur8Uv5Yv5AP2a7ai15b7C4L9sW95tiYZGvceT4Vh-_D-WxHsjdni9Ked8HE07L1fAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است
🔹
شناورها باید با نیروی دریایی سپاه هماهنگ باشند تا از تنگۀ هرمز عبور کنند.
🔹
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/449387" target="_blank">📅 14:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8604121fb0.mp4?token=BqGqvm85UfeJYp0HvBiCC7bKNvEw2O91xnsFtZrFuX6xcfQxHAsn5L2D9rbpxSsw2_5CAQsvpqquXlF7Xt2YhwNwHV9J7_fxXV4s-C1npTDCIMOwuAFXRIVm7DQLw2dwtJhuL4xKPKVzklpabP5FnRseeOtlNAPTfU4nKpigdUVRzgFL3XdZ-ft5RtONFU7tmKtE8c1X-_4UO4CuG1SBAqXOfiVZzqc8s1OYHybTs3zk0LYNke4s5unqQirCIAEXA6k5W429pv9GddRnd9Pz296xyWJivXa94VPpWP_E4NzVi3YqJhV-LxqALf0vvsFr6Fc9G5eY9pmTJccBJwiPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8604121fb0.mp4?token=BqGqvm85UfeJYp0HvBiCC7bKNvEw2O91xnsFtZrFuX6xcfQxHAsn5L2D9rbpxSsw2_5CAQsvpqquXlF7Xt2YhwNwHV9J7_fxXV4s-C1npTDCIMOwuAFXRIVm7DQLw2dwtJhuL4xKPKVzklpabP5FnRseeOtlNAPTfU4nKpigdUVRzgFL3XdZ-ft5RtONFU7tmKtE8c1X-_4UO4CuG1SBAqXOfiVZzqc8s1OYHybTs3zk0LYNke4s5unqQirCIAEXA6k5W429pv9GddRnd9Pz296xyWJivXa94VPpWP_E4NzVi3YqJhV-LxqALf0vvsFr6Fc9G5eY9pmTJccBJwiPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرکجا که گره فراوان شد؛ ذکر یا مرتضی علی گفتیم
🔸
لحظاتی از شعرخوانی محمد رسولی‌ در کنار پیکر مطهر رهبر شهید انقلاب در پرواز تهران به نجف اشرف.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/449386" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCLBksB7049-fsL5TYGsvADtjfAdrIS5Y59LUy_sTrp1TReR2Q5upz4VB5ddy50armWmx3WgUle358fm2hCr0m6-h119l2yZJ4LuC7c7fOx88RniXekwSCiUr59GouxYSvzq6JOX265eSg5pphYx0fasTvMjuNnzD0XskeohV-JXiWa0RD1Sfc6eJ0OWzO1P4dMBfPBOm70NZJx3KUXk2O6Av47RKLeH1f3klZ8Vu3bflf626821AJxr0aMnqrv-a2mhzlC1wieVgjLqxQx1YXR7sFBlCSSv5XK0q39_6xUCmoN5Zt0LzjxByilAE3I3YlKlyeAcFYsjoYuwS07Eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ پیام عملیات امروز ایران علیه اهداف آمریکایی
🔸
سیمیاری، کارشناس مسائل سیاسی: نخستین پیام عملیات امروز ایران، اشراف کامل نیروهای ایرانی بر تحرکات دریایی و نظامی آمریکا در خلیج فارس و رصد دقیق تمامی تحرکات دشمن است.
🔸
دومین پیام را ناکارآمدی اقدامات و استقرارهای آمریکا در برخی پایگاه‌های منطقه‌ای از جمله رأس‌الخیمه و کویت عنوان کرد.
🔸
سومین پیام این است که هرچه آمریکا سطح تنش را افزایش دهد، جمهوری اسلامی ایران نیز با دامنه‌ای گسترده‌تر و پاسخ‌هایی متنوع‌تر به آن واکنش نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/449385" target="_blank">📅 14:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibkv8bG2ZVabn7PnTqveFpg_XXTL49RLMk0YLe8mDeEv8XVZcdcNjGEjMO3SF9y6LbLlVWoePk7IRwDSfB3zlUxhOBG6TIlRVcM7mEyvcTYmmCUrPwLZy4UdUprBh50oImBVI7WqyajJMo5WrOVn45S_P1ovYIzbYv1P9GEfUbdDGNKbnAmC2v9NhvAffLYsI-1Hqd-i3Kf3dPb1NQrTAgGRdq3Deq9uFurL5tOhaPyqo9t0DiRkYHqk0uwwbjkKk0IRTJzbKoKKAdsUAN1aU3vheQINw3ZjME9qQY1QIupUxJ8bDtxWzvlQ5_Kvz6_wmWvwVb_BluDCctV5s_meYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیۀ خطرناک انگلیس به دریانوردان در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس به کشتی‌ها توصیه کرده با وجود اعلام بسته‌بودن تنگۀ هرمز از سوی نیروی دریایی سپاه، از مسیر جنوبی تنگه تردد کنند.
🔹
این توصیه درحالی مطرح شده که نیروی دریایی سپاه اعلام کرده «تا اطلاع ثانوی تنگۀ هرمز بسته است» و شب گذشته نیز دو کشتی که به اخطارها توجه نکردند هدف قرار گرفتند.
🔹
به‌گفتۀ منابع ردیابی دریایی، یکی از این کشتی‌ها در معرض غرق‌شدن قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/449384" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OadQkPRgh1qHA0jNTS2b69AtD2xvo8evMKmX7VEIek-CydQAvQMO2Ns6ohya1J5XY04vg9c2ynU2r8__Chv_7PHf6kvW7uJZqCSQyU0WZgZUFR2NSiMP7tjrU9ho-_8K8JrCg8ntObJkYTmW3Mdrm_xIVKdbojJB6tkA62YZJcg3hU1KsOKDnm1AbKl09k9n9mcvSWCuHvW1uKDVGKOgI-PDsyJx0tpJUqQaTxFV_KlTFRuqik4vszzRbGcUi2h68kAZNTykAilmLjyXqJkwHuKKq5TV-nPUUaacMAoUxJdZ1UBkzftlMSGscWqLTtaIM4HxaiDR1oM_dJgszFJ0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ تأخیر در اتصال کارت سوخت به کارت بانکی
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد مرحلهٔ آزمایشی اتصال کارت‌های سوخت به کارت‌های بانکی درحال انجام است و سوخت‌گیری با کارت بانکی به‌صورت محدود و ایزوله انجام می‌شود، اما زمان اجرای کامل طرح هنوز مشخص نیست.
🔹
افشین، معاون علمی رئیس‌جمهور، می‌گوید برخی مقاومت‌های مدیریتی ناشی از نگرانی دربارهٔ تبعات امنیتی احتمالی اجرای طرح است.
🔹
او می‌گوید که مدیران تصور می‌کنند اگر «تغییری در سیستم فعلی ایجاد کنند و حادثه‌ای رخ دهد»، مسئولیت آن متوجه آن‌ها خواهد بود.
🔸
اتصال کارت سوخت به‌کارت بانکی قرار بود اسفند ۱۴۰۴ آغاز شود، اما با شروع جنگ و احتمال حملات سایبری به‌تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/449383" target="_blank">📅 14:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBi7eHolJtcsaHn15pShALMm-0tCmOK5RVPIpghhhcZdDv2n2AGUbqtnrW00wXvVWTlYGkegMRmbOyGI6KG0OAQVMtzIuiyQqJqw6Kj17MunyTrbtolCKSzUqbMWag2W-_4xJtvE09kEfwAiFKlPNVv5VrNm0tict-HRLL2waeBrtbFeL5oZR-TnYkXpXiPkN0vBYNtbS8i6ZB49qoKAQgacnquRQzNBquRXhRHLxX5D1-i26h7aLg-7E1HR8_RlRahIZXmuyyrv12scnEJLXnXkpjS5IQpUm8t6OphOeBS-hGAP79zmSoITE9haXgFXRSKVpNFhAhBgCroO5Xc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی یک موشک کروز توسط هوافضای سپاه
🔹
صبح امروز در جریان تجاوز ارتش تروریستی آمریکا یک موشک کروز توسط سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در حومهٔ خرم‌آباد سرنگون شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/449382" target="_blank">📅 14:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDLhxOzw7IHy0wfUwa0gVB4cTxKhRxWx9gPQgbShzFu71I4AJSnYvGTK42aHq-RT96Y5NZnB6K9tHEHmSJ3URhduMNhZpP51Bh4PifzTd32lSJzpeyVYSubjpZZxVYbwY2I8HWE3I-8J4q70Zobl9uk-v83YKUwgbUWH42O5CYCFuBv1c5eA1O_s0jPrQZ5rCLP4-R_9JS3zsdqWZSmZFPacHPJxurou-OBr6Tu0SV2xO-ETD6sutRMcUzMyWJLMTUyJ2HlKdLOB1z8TD8i607d8XDloKyzwoESlGXPH9AspZUaevCB3mx05e64r-WJpJxHjoS2wNx2mqz227xrdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه در پاسخ به تجاوز ارتش تروریستی آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/449381" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f78a41745.mp4?token=FgLNg2ao4a_6GdPE_Q3NpWA0_29suqBu7THK7Q0tMrGiHFHRq1YL5NoXQm56t1tkqS_bsMDdmsKwaK-7uEANKHJHUhQLYQfwVAeaN4MpNwvLy66GQfZXN48XCqTx6HNpvVEHHjteua-pFurYT5PcpGk0I76gQSzBve0BAu6FE7K2eGyseZi_UpP_Pu4aVfGPBj8Ba0qyCo2Jkn6PDaJ0lHXWFsJwAaL9WEt4u73tlITAnNh_cz6Bnfhw1W2AhbdpfGkFGweXYE32Czy8AVfXLwSTBG8eChKeedO6I00cQeJ9UjcggTcdnDgDlQp1AC-5L4swJa5weGqMXEpaexQr-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f78a41745.mp4?token=FgLNg2ao4a_6GdPE_Q3NpWA0_29suqBu7THK7Q0tMrGiHFHRq1YL5NoXQm56t1tkqS_bsMDdmsKwaK-7uEANKHJHUhQLYQfwVAeaN4MpNwvLy66GQfZXN48XCqTx6HNpvVEHHjteua-pFurYT5PcpGk0I76gQSzBve0BAu6FE7K2eGyseZi_UpP_Pu4aVfGPBj8Ba0qyCo2Jkn6PDaJ0lHXWFsJwAaL9WEt4u73tlITAnNh_cz6Bnfhw1W2AhbdpfGkFGweXYE32Czy8AVfXLwSTBG8eChKeedO6I00cQeJ9UjcggTcdnDgDlQp1AC-5L4swJa5weGqMXEpaexQr-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ اوکراین به یک پالایشگاه روسیه
🔹
رسانه‌های اوکراینی اعلام کردند پالایشگاه نفت سیزران در روسیه هدف حمله پهپادی شبانه قرار گرفته و دچار آتش‌سوزی شده است.
🔹
این پالایشگاه در فاصله حدود ۸۰۰ کیلومتری مرز اوکراین قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/449380" target="_blank">📅 14:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtj4fbuwrQjyjoChsWBJqgtDqtjMlUsVXhBRv7z3IAPK3KL-KDgJAPqupxsdvJBRQUj3jqMAGpTD8A6RYNzwbo4V6z_MympsH5BZAyxfI18wczl6qLiPRNie9CHuDiq6Ht3ZUrhSfedwRQerbzCkrXOX3YoW0UtYQkcTzb2kp_zCpUEkFvfl0EtgQlXKgjlf5PR5X9NZ_UCjBFGrRm8cXiimw1gfjPRTnwF9kaRxHOoVJft3O09RYBxIaKfb4BpMlzW62dd0WzvBqJoxMzxThO1-h5-3fBK4KJMwmAv035SsQsejaXFOFB6c_fm_-uZzplNA2RNSTcTvGvoAXAE-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تأمین اجتماعی: پیشنهاد دادیم مبنای حقوق بازنشستگی تغییر کند
🔹
سالاری: در حال حاضر مبنای محاسبهٔ مستمری، ۲ سال پایانی خدمت است؛ درحالی‌که ممکن است یک بیمه‌شده ۳۵ سال حق بیمه پرداخت کرده باشد اما تنها ۲ سال پایانی خدمت او در تعیین مستمری اثرگذار باشد.
🔹
این روش باعث شده که ۲۷ درصد افراد در ۲ سال پایانی خدمت با افزایش قابل‌توجه حقوق مواجه شوند و مستمری آن‌ها بر همان اساس محاسبه شود.
🔹
پیشنهاد سازمان تأمین اجتماعی این است که برای بیمه‌شدگان جدید، مبنای محاسبهٔ حقوق بازنشستگی براساس یک دورهٔ بلندمدت‌تر تعیین شود؛ به‌شکلی که حقوق هر فرد در هر سال نسبت به حداقل دستمزد همان سال سنجیده و میانگین این نسبت‌ها در زمان بازنشستگی مبنای محاسبهٔ مستمری قرار بگیرد.
🔹
اگر مبنای محاسبهٔ مستمری براساس کل سنوات بیمه‌پردازی تعیین شود، هم بیمه‌شده و هم کارفرما انگیزهٔ بیشتری خواهند داشت تا حق بیمه براساس دستمزد واقعی پرداخت شود. برآورد سازمان این است که اجرای این اصلاح می‌تواند حدود ۳۰ درصد از فرار بیمه‌ای را از نظر مبلغ کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449379" target="_blank">📅 13:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5ZCeHVw7P_DoUajulHA8kWtE3b4Ww8-T0_Dja4BpbDQ4TFUfa7MmG-1rCyap4LSGLqozR12Wkdu1gNJtXtMbj89peJTwmnj6jreJ0i3bmilyqwqO5aYDLlLXLtiGKzPwa2NkJgG4fe4jYpahuepxUrMkgGujLX5joUxQtZ1CVwSRdrSVilYHhxeGzSeT-NMPQbNibCNiIermT3aKw7Me-ylJF5axKVWUdzqP2bToXT0URtbhQBRmu0X6Wb2DIHV48tZzGRZGgJQXYsaThnB5I6n8EKARoUlIC3psc9PpUUjNvf8-QYbL5hrg03nCH9QmTDvm7v3gnUgv5DpygLqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449378" target="_blank">📅 13:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رایگان بودن مترو همچنان در هاله‌ای از ابهام
🔹
در حالی که قرار بود از امروز طرح رایگان بودن مترو و اتوبوس‌های بی‌آرتی به پایان برسد، مشاهدات میدانی از برخی ایستگاه‌های مترو نشان می‌دهد که همچنان هزینه‌ای از مسافران دریافت نمی‌شود.
🔹
درنتیجه به‌نظر می‌رسد وضعیت…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/449377" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im1eTW6ZymUtCA-Csg6kKNkqIGg0gz3SMmjJWZgiFx0QY0WBTavJM5UiRPBJ6eMuecjqObHPNrgb8Q5fhg254jlQI13r8a_Vo9RAJ5wPvNpHj0lyvhDVVknlyApl_Nj1FzepgBk1AUfp9U50_7BseTyfZE86T-xfA-Ksnf0AAyJTAo0FmwWH3cRGxq8_WQYbQFphFfffWHUSUGmb_dUUW6eBMw7ViBPTubu7opwFv9gJQKjktZKGuxQfHyemoywI6Vy4z2vRKfZpm-uENoWvBFu6Ceep2w6mICwaxshBpi1cFKX56dK-Sl24NF2PfwcX4AdnE7s_Ujy3BGJzgX8rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449376" target="_blank">📅 12:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اولویت ثبت‌نام حج با چه کسانی است؟  براساس اعلام سازمان حج، از فردا دارندگان قبض‌های ودیعه‌گذاری به‌ترتیب اولویت‌های تعیین‌شده می‌توانند برای ثبت‌نام اقدام کنند.
🔹
کسانی که در کاروان‌های حج سال ۱۴۰۵ نام‌نویسی کردند اما موفق به تشرف نشده‌اند از ساعت ۱۰ صبح…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449375" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK3HmgWdnPxFHku_V79Z14EMZAVzlFeAB5yExrFSDr0lkgaDmNzGECbB83WpVFansFZl2qWZ2awPbaesnpciD-N6SyMOcbV5CFH-ZW2XG5bc_oVv5ySGbMKbAfquba5Hgo-tGiJYqnEHiryjVkLYsyobh_bz7WUADSw3fCSg1fo7hAkggn-IE64Z8PZAghJeECmtnl2I0h5R63OMaHzLtudfuJcM4km78UiN8G0hB4AdavO4FCUxm6jG5ok8nS7HkNxfQzzC8FTEkP2-uhGLWjbu-EcHw8ZT3j6EHDUK68X30_ixrIlVlCR4GPBA0QE4njw5q_-rcAzj_QRDRTClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی برای مرگ سناتور ضدایرانی هم عزادار شد!
🔹
فرزند شاه مخلوع از مرگ سناتور آمریکایی که یکی از حامیان اصلی تجاوز نظامی به ایران بود ابراز تأسف کرد.
🔸
رضا پهلوی پیش‌تر هم پس‌از حملهٔ آمریکا به میناب و لامرد و شهادت صدها کودک و نوجوان ایرانی، مرگ چند سرباز آمریکایی در حملات ایران را تسلیت گفته بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/449374" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصاحبهٔ لیندسی گراهام در روز آغاز حملهٔ تجاوزکارانهٔ آمریکا و رژیم صهیونیستی به ایران: «رژیم ایران» ۲ هفته دیگر به زانو درخواهد آمد و سقوط خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449373" target="_blank">📅 11:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XubkKTv-VNG6gcEJMm3SVe_ZbRjgPuzoeqbM9CACmdTYsjekrrY9rykRKWmsAPtK0i9mgS2rvXovKTPc_m3Y1nX0Vns_hwkz5cJqEftTIKyi--uG-wdCS_t9gvq0wFrVFgCD_rfEQb5uME3-QQM2ZTc7XELQ6GXUgB8z6Sst-LFw187zzF94q74CBMtf1hzxEgsx_H2LSf6puVmQs__NQQaoeHJWzxckdKU1iT5mZx7DaXlkT2t4PsxQkHi3_0vJV9el4jR86RYakO71skanvEVuDQcxmK4Fn2RGd3rT0yDoWF50Ru2yH2amW05zPKIfZ3TJ-QmLN2a8W5y07sCf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش کنایه‌آمیز مرندی به مرگ گراهام: حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449372" target="_blank">📅 11:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FRwHFJhf5uMRUWOQsLmybjF0EvrIltgqHvS8NOrESiq-TsoyFk_M5ofZFcJK17abHP2vI-pZVai6WdZ2zqY8eNE6YLOxCTBc-AgKzEbhSBQ2ZIuyScISUPV8JLgD19_fgovZbgQzYPx3vl5NsDhFm9BtmPz2b19kTmEtFOxM9j6HydCryg27R-g4VEexpxByHfMSEsdMbeSPsIt33o9VcUYTXBeh8_7ZZ83KqQufR830SOF93fFIBQAHUzYaLz6OIDwjKhHIauKf97ky9Vy6R2_-aNwW4h38b0DvBO4sY_1mBdAMIv1uO9aRd4xX1qdYKk-m45jLjHxOus8BZTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449371" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIEzsydbf-4TNd5C6BxLQ5nuTbD1uy--6glVpU6LiS8qBtJk5PC7vXjsxQ-0tCDRyT_1X41fUDom1YkuwsIhfp6hOYVU_HRoJpbkKCtvVHMaW3-U24TxbKPjkcC-MOtPO3fpeHf7fUdSl_IHUySKNUDmzbEYKcs3pH3dlmyTpK1Aurtfs1FY7SYosCnCJHxXeAsFwy6Jo4cyvk9aICyQ3pVBoit07sGzCk3aJ-8JwjP4FpDKNzzYJAMwwYzLtJdMEmpezkdNZCmIr5taDlIHoaRWRmr5SItYKC9K-Zw-OZwR0962YlG7g-nT6HqEXZ2Ej7L5DBGszZnUP2j48X7S-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449370" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449367">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449367" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449366">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین از فعال‌شدن مجدد آژیرهای هشدار خبر داد.
🔹
برخی منابع هم شنیده‌شدن صدای چند انفجار در بحرین را گزارش کردند. @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449366" target="_blank">📅 10:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449365">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o83mtPLzoJ_LHo8TIBHULAldPZYNfvIEH6BTxOkDeJaVU5G5m6zYo8b909L4wEXHITM8Agg9yqDp0oxkflLCA_SWEZZJx3Bo61FWlMLRt3qYglZRq-GY3kokfuG7Rviiz1xjCdx-2dt8M23di0NeNgsXXZ6aCgfBDT6U-TjWKu0NC-eoCl9K_3prj83hHRihP-sEktm9dH3kV6-hwMcGb29knxcueUTjgn1FAIvbdNNZ0ddzdAE17H1uiz05vnX2Tv00RvxEdE-MOZ2wLFc77v9b2HtR40nlSXkEkI7gSRzpquxz1ffCduq9HqEbSNdSVbGKYj3nCQZp0ofdOsEj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات ان‌بی‌سی نیوز از مرگ لیندسی گراهام
🔹
شبکه ان بی سی نیوز با انتشار جزئیاتی از مرگ سناتور لیندسی گراهام گزارش داد، نیروهای امدادی شامگاه شنبه پس از دریافت گزارشی مبنی بر «ایست قلبی» به منزل وی در منطقه کاپیتول‌هیل واشنگتن اعزام شدند. تصاویر منتشرشده نیز انتقال او با برانکارد به آمبولانس را در حالی نشان می‌دهد که خودروهای پلیس و آتش‌نشانی در محل حضور داشتند.
🔹
در همین حال، این خبر در شرایطی منتشر می‌شود که میچ مک‌کانل، دیگر سناتور جمهوری‌خواه و رهبر پیشین اکثریت سنا، همچنان پس از انتقال به بیمارستان به دلیل ایست قلبی تحت درمان قرار دارد. سخنگوی مک‌کانل اعلام کرده است که روند بهبودی وی ادامه دارد، اما جزئیات بیشتری از وضعیت جسمانی او ارائه نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449365" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449364" target="_blank">📅 10:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJnFlbitho-rYZUIIrjHra5ynG8PCr57F5H9vkS75sLszQYTOVgYuaGz_V8D-4z2_exD5Ez5TrIG7MEsZPn1CWxpQhNUjxOHhEqzfdRGYZjm8eUZi-jlspycBZoyNTl6ox09D3HXdxuYZM93PYNB3q4CHfc0qjDpunSaaJt47BC7aBo3Zj0CGLoV2EM7mU2sJr4e7j8OXVaOKEWPBFmwr1uX9gc0bjr4R8OJgUsKw1c5NLopI2l1KU-GsHJdEvV1sgPiFJuVljK2pE57Hr-m2EyLoQjTeAv-Bd85vGpfjwSWqxWAAqPtNrb65kUG0s9lwA7Mdx_Qn035m9ruVPgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوهن، وزیر صهیونیست: سناتور گراهام یکی از بزرگترین دوستان اسرائیل در واشنگتن بود. او مواضع قاطعی علیه محور ایران و نقش مهمی در تقویت پیوند اسرائیل و آمریکا داشت.  @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449363" target="_blank">📅 10:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ9a_Y_lSMEitz1XAswqveqzPOGwQab0s7-GSQ3KP-zduyZjM8rZlRrt4EhZ4ta3G9FZSI9v6z6lxteWkHWlKkZktP3MzgRccbwlKQQNwP0VeDQkZqb1M16x7UrXesnHJvrzVTSV3OWc-UdpUsHU4mbj1iCTfeUemBOuwXNMNMShQwjcdHP9zqCniZIrK8XP_uJo3R3hsiAhkC_pEkgk9p47JJKTqaLGNZDNoNxapSdhd1WE3M7NmaTprcfdnsYEEExq77jbLzPxyLY9GU9QxD2_pi7oAfEiGWryc8yp-bivjQx1OhH_lAP4pjDNhPdldYmgzxbfCp4M8gPs6Ik_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم صهیونیستی: دوست صمیمی اسرائیل و یکی از قوی‌ترین و پایدارترین حامیان آن را از دست دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449362" target="_blank">📅 10:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzXvogkkdFqfZoQ-C9dHnP1kmHf6b5j21fyWEyY8fcEuFnsoYVlfZBxgK7_7VvHfFbMhWGGpcngb-hEcapgPesFN76wjU8qVSLB1DKp1WKvQEA59-OiK1-t-oEG8DSCLxsWLnL-nVMtDuMQvY3paNQ5fNfCg3pF5-4B3bMdB9zpBbXp1tTuTtXg46UGKVVeqo03HDkdklUjUR8Tok5VYpQLGGaVmhvr1HdT_tADWME5bnRrex-eOWoris8WO4Eh3k4H5koTKWybG3AgRTqIv584Gsm8yOncpVnpe9cZ7kylnLd_LfD2KoXD5ScKShMjKmpXottsSjy0cLo6v5-2iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بنت، نخست‌وزیر اسبق رژیم صهیونیستی: قلبم از شنیدن خبر مرگ دوستم شکست؛ اسرائیل یکی از بزرگترین دوستانش را از دست داده است.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449361" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449360">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3SSpv8Z9d0JMKK50x-PRoMAEwUBeUFy9KnQKxABUE83_BUS2lUa3Z-AE9MHLSrldhoQHV68o6Hh4hvJQ1DQE2sY9E0eqAfLS_ipcV7pS_9QnpN6rQb8DTLjix6_dcJy_RJ1x--Nc3iEun4GNMGLwYOqhMwXO-mcmzxPhopLsPdOdLFwpq2Y29Oi9ZjWXsuQ2pqSaTrHegkzEkXpKH0OHqo5zuaKo6wHu15Qsfr45rWc2_0NotzWDTxbNwyRox0hJ5if3tH2DjGiZ8CCc3zFulGP_db5Vy5urhSgOnP95wAExr5N65Vs-XESg4SrhYlRSKJg5MaVtUJhQJuS-ojTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بن‌گویر، وزیر تندروی صهیونیست: اسرائیل یکی از بزرگترین دوستانش را از دست داد.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449360" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449359">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز
🔹
استانداری آذربایجان‌شرقی: امروز تا ساعت ۱۲ به‌دلیل پاکسازی منطقه از مواد منفجرهٔ باقی‌مانده از تهاجم دشمن، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449359" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449358">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXsWuHLK9_pnKYQs8bG5oaRJ7xx3neJKRsAGIcGWJk_-8uf-AjZhcCTR2MzYO2aygzXZXJNQT1EaiSygH4XEJF3Nq9dJr3e7vBb0RbrgLXkpixaXPN1-soWMuySNzaqt7Hve5JThgp4eBU-PLxPgzKE7WgagMGBVfr0fMcOhP1qGM_gC1cQgUmeoff6OGHU7Rc4d_-PStfa7xlDqQtR35wLayZ1OLWpMQ7K38wlwo2DOadDKL7aWryA_HhR0WrdYkskum2Q-D8N3svcIwNzMQl_HE8sCgl3SnGHEXPV7lVxxagQcwDZwMFc5lfjh6i-Q6aE52_n54EHdX_eD6lBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ارائه ارز اربعین از سوی شعب منتخب بانک شهر
🔹
فروش ارز اربعین در شعب منتخب بانک شهر آغاز شد و تا هفته اول مردادماه ادامه خواهد داشت.
🔹
به گزارش روابط عمومی بانک شهر، فروش ارز اربعین امسال نیز همانند سال گذشته به صورت دینار عراق انجام می‌شود و نرخ آن بر اساس نرخ اعلامی از سوی بانک شهر خواهد بود. بر این اساس، به هر زائر واجد شرایط، تا سقف۲۰۰ هزار دینار اختصاص می‌یابد.
🔹
در راستای ارائه خدمات هرچه مطلوب‌تر به زائران اربعین حسینی(ع)، بیش از ۱۱۰ شعبه منتخب بانک شهر در سراسر کشور مسئولیت عرضه ارز اربعین را بر عهده دارند.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449358" target="_blank">📅 10:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449357">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmEBAXSyCkhDUZWLbtCd0tcUznWrdwowuUPBfaw8ybrT8YdU5_F1qPGQLwuJ5dGIp4ZrM5v2Gv_jEOdLI38nD3cP6kTeEmKbF4wEymF7a2NTYbMe3Fu-FIP8OzzICXT5XKoJy9-gtR6buM_kB1OA0TvVZMLGKppqac8abfFliKT5Q9V03B-cUd7DkIbxr29pjC9KDdAgt25Rfo80e_eA-aW4-riapR_BExVI3dfMV-RmBTGDsVOoR8qIpIwNgZxswRQPhnMpplZOGLF07sg4umfOSULGMkOabKFvFC_4Jm5Pz4A41kINJ4eJ9h1Ty0S_SWtsPa1sOOuL3OyuUf_0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449357" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449356">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449356" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaEq5BUeqBbPmsEFm6CZiNIpMjfUsGjKrzXdJEvS7OtR_xarMIuOYb5tsJGam1n-1G1yB5_ro79ZJGL_MMdsgrNNWPSW4034c6NpnxJgjwt_Y2SlHy_6OoSiTKijglRZEZRNex1_7GvjN5O2lMgxBIGF7K6JVN-_zkpzl2qu3NP2ni0rW-kF9zQ1YSCUrNhev46kUfsu86Z8Qiaaz63LB3NG7hcvGu_XfGledqvoQj0PPuqVv5kTgj3EttG_JXUNNZ4u1OHz3l7O1Xm9cZQ2Ir6rEjkA_8wGoD-IomM4_WiTeLvFG09iEPxDgI7og1TeSOc8n3IUJwpNtMr0dAmz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE5rUd4qBd8w2YfCWjVo00ATU8Er_7wi3V9N-HcTWv2CfM9pEgyPOA8iYcZ_7M9nH5kAY-Cz7TNgQNapPCnYpRa8mcy51BuYPIxpXWvP8t3xAonfKJlwXJvdudarcYRfHeznBlP2mf71Rtg5WVxUxswUELBLufRQ8UHf274CifgLVncu5bRS7U5d1Pe0ZIGM02tXN66w_F4rOiA-I7CvwBU_OqXacPFC7Kn_3Lk-WL9PaR-VclJOb-0BE4srSHnk6gmDbpRimffUxvYMSimrivwvlxxgfXrwdPheeFCcUqo9dai07FvCpvWxv-pGIU2ANldqQzB0zTau9ImaRJniqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjtvofmuxNvqYE1wo08MRuetgWznp8jzeTfhUpIU9Uf2gCWuwYrOThjASGgcnL13MbPrEmiY49GBsCxOt-dFVyfcN32qFxqwoVZTuB2oIA6qUUJ25mS___qH2_C_jtuH_3Jpi9cdzIsmwCutzCOZ5-IsompFJdvOepj5tLeYjF4QV1pB-JlKy-KjN3GOqQwoosEVp4YmJAblcLgdx8ClrNumLfnloCDVf9_QzWNapEDxzbiC_axL99neh2pO5-Xe6jczGsc9fs2PNwhFvLdhODx-tdwL2wYBEa2mVOdzRgr9rHlcHq3K_BRwNnDInR2UOct_P__x57zx8eMYx5CmvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخرین اقدامات علنی گراهام قبل از مرگ: دیدار روز جمعه با ولودیمیر زلنسکی و بازدید از تاسیسات پهپادی اوکراین
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449353" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iehb-917iqEgb6WBajOTh4MFErQTdeLq2-MMToTxKaDruS_Z2TR93irWcMLjPrjPgHC_8z3lxuvo2gdJY1FNzi_Vx5Ns0Tc8qC9eNzGOtVRut0UROJgoa4JnsjGSwMmwfgO6MqX031qGoLanvLYufyEPLfwq-DGHk9rHTlKtn-UNPPx5bgLYPgsm4qtc-TLGPOyXIbqXEl87U5Z_6aR5sF7nxVvVlKrLIaNDsr-fq1nkmIeWgEt0p310G4IyXEe1jmFomhxihzOBwH4bx_cdP9zjv6LC9hXqqD_jZKij06S7In7r-vsuLqVNgEiR_t6YCZPoUnVcbCBDThOIdpcJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449352" target="_blank">📅 10:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن انفجارهای شدید در کویت و بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449351" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5KL7727YVFxVVXSgVNeWIuQ69fpTrs5v24bMdbeXaQH4smICMpiQ75M8m3W5HtzhWQMxcvS31IOHj0HyLOUvkT8_N4rLVuqEzsvZh_SY4QnvCC30z3v7ErSP6hYaVoXI0US2GQezPjKUF8fCeKU9bMJ5Igfn5XJPY15v26Nt61eL1CkpAeYESOVxagQB1vuf0tfLl29aiimcY7AR8ZwN896Fq-DDXovQEyx2FHdAeyVmmTCRoAsa-_Hzml0xyOVBpUjg6n06LcLLsWF2HRduk3GpdWw69Py6UxyEzAbkSXc0tHmadi5dEYLiuusi0hOQQ_RZQmAGAgBpVEiWiG42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449350" target="_blank">📅 09:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2DYP48onq11QaN8ClRVmkuCXZ9ZLhwOeSXnkN9_9QlY2QpkPFFdm09cTDUgwAkpbijBIu48OM8JA8S236gpHVjbNTgvR8c0_8f53PCzqLCWjRjDnC9yPFBOUFEqbr7RimylnZS5NGr5Pe1d_V4Jyh6juR9f8PcVHDbnzdntX9XrzwQH5f7G1NzTYOF5qWYFEiJ3zHY6fmNqZINhW1fR_i_EK43rcaLdwJTcfkj3zngMV3cLQ98xb86m5YE6nm2c4p0e6qJPp0f08Ks0yv7tAEJqGeCpFyp-BArzkHNJ7OEsmxJOtlw2CfcmllINM09rr8E3B7G3PM-YBEJDZmZbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
@Farsna</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farsna/449348" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449347">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyRM3BxGk0gp4b0XE_RwdWu6fTiGS-n2-jvqmPL6zvX2cJIY54ZXZoukBuhOEepUrl-T9ev7lmbiab3IHVChCFtUDQQttSf949ubGxfc_OFuVAsUCgHseRureUS40-HcbF4wCJ0d-EHff9p8biTpDUoSoeevlUfD3uqdWihB1-von-r7SK7J8MQ55ED8-mgA_DbxDAQXvjy3xx-dTjDaO5banbLSPpxrRv7Naic4gRJLHEQ6DBipRbKTaWyvdEk_xZ37KJbaM5JTfyKfCrNg0SDyOzE609iS3j3bVqdi-y8Zuf1YzVcEVl_r09GEmGRcVO41a75dITIMIloxMXNVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با استقبال مقامات عمانی وارد مسقط شد.  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/449347" target="_blank">📅 09:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک نقطه در خنداب هدف حملهٔ دشمن قرار گرفت
🔹
معاون امنیتی استانداری مرکزی: صبح امروز یک منطقه در خنداب، مورد اصابت پرتابه‌های دشمن قرار گرفته است.
🔹
برآورد دقیق خسارت‌های جانی و مالی در دست بررسی کارشناسان مربوطه است؛ جزئیات تکمیلی متعاقباً اطلاع‌رسانی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449346" target="_blank">📅 09:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مراسم بزرگداشت امام مجاهد شهید در مصلای تهران از سوی رهبر معظم انقلاب سه‌شنبه برگزار می‌شود
🔹
دفتر مقام معظم رهبری در اطلاعیه‌ای اعلام کرد: به‌مناسبت شهادت قائد عظیم‌الشأن انقلاب اسلامی و اعضای خانوادهٔ عزیز ایشان و همچنین با خضوع و خشوع در برابر عظمت و شکوه تاریخی ملت مبعوث‌شده در بدرقهٔ آقای شهید ایران، مراسم بزرگداشتی از جانب رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مُدَّ ظلُّهُ العالی) سه‌شنبه ۲۳ تیر ۱۴۰۵ از ساعت ۱۷ تا ۱۹ در شبستان مصلای امام خمینی(ره) تهران برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/449345" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCnYBQtlkaFw1G11qV4J5E-qBKLZF_UxqwSsNRLQ5vilce5pTT5TaeiaX-NS0oNcMQJZtqmUKQQhZVvNBCFRPACn6ZRYj8enjBEAYcXHi12DcfwFqli-_0AmMChzcqMdfH9Gm8rCFIn_I6qhnmCbfHI9lN8lTB8opBJ37niYsX9I_6Zt3kDckQuO5wuy4ep8ud1Z14w0XZOXMEsHGXrM044Vt4ghsApNZAQwTbRoKCXQaHJ8WF98mTN_llniyYubwopu7-SX5M8jvMs4qep29gTTDTnYVOSJa9q0LN-yXGUwbAYr0PeNyTh_T7hWwnFIFTpwZi72PXEj9B8OMAJOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوت امیر سابق قطر
🔹
دیوان امیری قطر، نهاد عالی دولتی این کشور، روز یکشنبه اعلام کرد که امیر سابق این کشور شیخ حمد بن خلیفه آل ثانی،  در سن ۷۴ سالگی درگذشت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/449344" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449343" target="_blank">📅 09:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449342" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اصابت پرتابهٔ دشمن به ویسیان در لرستان
🔹
استانداری لرستان از حملهٔ هوایی صبح امروز دشمن آمریکایی-صهیونی به ویسیان، از توابع شهرستان چگنی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/449341" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/449340" target="_blank">📅 08:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449339" target="_blank">📅 08:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449337">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سخنگوی ارتش: آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
🔹
امیر سرتیپ اکرمی‌نیا: مداخلات آمریکا برای ایجاد مسیر غیرقانونی در جنوب تنگۀ هرمز باعث ناامنی شده است.
🔹
ما موظفیم برای تأمین امنیت منطقه و تأمین امنیت عبورومرور کشتی‌ها تلاش کنیم.
🔹
نیروهای مسلح مقتدرانه از حقوق مردم ایران در تنگۀ هرمز دفاع می‌کنند.
🔹
بانک اهداف نیروهای مسلح دائما درحال بروزرسانی است.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/449337" target="_blank">📅 08:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449336" target="_blank">📅 08:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8QN1oWo8S8mmXso3uYRXbE6GZHKVucuabI04t7-0sByKpVca9ctTUm8jWscLMtrQA2p7mABn0TYa70NPx4dBRGLLE1RXUh2g_xZ2LQhn6fRK4rxW72hn33SiD2HzO26VgfPdi8RxZuFa2lSH3p3QXxW8Ljd3b1ewtA93qJ3dCoIsiY-Y-pFYt54iuUJeoyOSNPcmHu5TAMfOKlR27ATVaiwPi8y6Sv14GWbtINintHDjlkhgIX2sKR-BkIY6iSxF67UmgcFrnuPUefHMrSCiAz375Kwmy90WHn2x8uK3dd4tfWxe_gulItJOo0p7cjxZs2fVK9dLvD-P35UMM_UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلند شدن دود از پایگاه دریایی آمریکا در بحرین، در پی حملات ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449335" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر از ادامه‌دار بودن حملات موشکی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449334" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار مجدد در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449333" target="_blank">📅 08:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449332">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE-BCY_y11UCut-v53QS1keBV8rBj5-oGNqijT65OPYT1yGLU_x20J4El5BqmC-gU8oAfCTc2XZhFK7HnZGPvclMiyr4OIQighxW2Bv2QIjkGjTCa5PwR34UzUCfJ1ZNU2byjU5p3wjhXwDUhNj97hCNRJezcYqHXKEth8vUNK4cHrDI6BLFuJmeBli7AH5PDbGFulnbtATPSe_dHDFy-OEJEML5lcBc2Y91M5y1FfAlgFtU5EcoOWa_MR0qW3VNEi_pwq3_Ral_PjFG0ZbSWLS82jIF_qaCFRMzmYmHdBaBW1HLIw5kuiUVs7nCYwMnumGwW0EutqcnX1xKEj8nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم به قول و تعهداتتان عمل کنید وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبه‌رو شوید
.
🔸
همچنین او بخشی از بند پنجم تفاهمنامۀ ۱۴ بندی را که در آن بر بازگشایی تنگهٔ هرمز با رعایت «ترتیبات ایرانی» تاکید شده است، در ضمیمۀ توییت خود منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449332" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449331" target="_blank">📅 07:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449330" target="_blank">📅 07:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
آژیرهای هشدار در کویت به صدا درآمدند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449329" target="_blank">📅 07:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/449328" target="_blank">📅 07:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار پی‌درپی در قطر
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449327" target="_blank">📅 07:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
منابع خبری از شلیک موشک به سمت ناوهای آمریکایی در دریای عمان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/449326" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای انفجار در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449325" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWhYM8yzYYBfJgDtQGw68dAng0nXmwxAcOiv0ayyNqabVETlyL2jLrWjp2SEFIoZTI7UgBmGaan9yIMLrSzvFEFfPteqKpe2rTk0cVK62qndpUjQKMMaidnw-4JPMnNBTKbtT2I3yPqW7lvdp1WdDrkP1oTQEJo2XSHHQsiSyFES5BxiRtNXAW_Zzvb6shnDVE62z8ltVCb4vhW1ysWCSy9-CojZRch0LR_z6AALIeHBZ65nAIg3dZqVxCbgesi-aubWbUBGHyags7mCcsIwHV67mseptIfXVf1OtccQ9MLQ8MS7HCoUu-FBcU50ulRjKf5-vTZFYRWgkHKRSQlSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با عبور از سوئیس به نیمه‌نهایی رسید
⚽️
آرژانتین ۳ - ۱ سوئیس
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449324" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز فرماندهی نگهداری جنگنده‌ها در هم کوبیده شد
🔹
در پاسخ به ادامۀ تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگۀ هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحلۀ دوم عملیات مقابله به‌مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های مرکز فرماندهی این پادگان درهم کوبیده شد.
🔹
دشمن آمریکایی-صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت. بجنگ تا بجنگیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449323" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/449322" target="_blank">📅 07:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449321" target="_blank">📅 06:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449320" target="_blank">📅 06:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449319" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی در جنوب تنگۀ هرمز ایجاد کند، که با پاسخ قاطع نیروی دریایی متوقف شد.
🔹
ارتش کودک‌کش آمریکا برای جبران این شکست دست به حملۀ هوایی علیه تعدادی از پایگاه‌های ساحلی و دکل‌های مخابراتی در سواحل جنوبی زد. همانطور که وعده داده بودیم بلافاصله پاسخ کوبنده تجاوز خود را دریافت کرد.
🔹
رزمندگان غیور هوافضای سپاه پایگاه‌های نظامی آمریکا را هدف قرار دادند. در مرحلۀ اول این پاسخ زیرساخت‌ها و تاسیسات مهم نظامی در پایگاه هوایی پرنس حسن اردن را هدف قرار دادند و مرکز فرماندهی و کنترل این پایگاه و آشیانه‌های پهپادهای MQ9 را با چند فروند موشک بالستیک در هم کوبیدند.
🔹
ادامۀ تجاوز آمریکای عهدشکن پاسخ های شدیدتر را به دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449318" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449317" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">قطر هشدار امنیتی صادر کرد
🔹
وزارت کشور قطر اعلام کرد: سطح تهدید امنیتی هم اکنون بالا است و همه شهروندان باید در خانه‌ها و مناطق امن باقی بمانند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449316" target="_blank">📅 06:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449315">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی: انفجارهای متعدد در پایگاه‌های نظامی آمریکایی امارات و قطر همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449315" target="_blank">📅 06:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449314">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449314" target="_blank">📅 06:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449312" target="_blank">📅 06:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌ وزارت کشور امارات: پدافند هوایی در حال مقابله با تهدیدات موشکی است.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449311" target="_blank">📅 06:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات   منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/449310" target="_blank">📅 06:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449309" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449308" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449307" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449306" target="_blank">📅 05:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449305" target="_blank">📅 05:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
برخی منابع از فعال شدن سامانه‌های پدافند هوایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449304" target="_blank">📅 05:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
معاون استانداری خوزستان از اصابت پرتابه‌های دشمن به مناطقی از استان خبر داد
🔹
تا این لحظه شهرستان‌های هندیجان، ماهشهر و آبادان مورد اصابت پرتابه‌های دشمن قرار گرفته‌اند.
🔹
تیم‌های امدادی و کارشناسی در حال ارزیابی ابعاد حادثه هستند و اخبار تکمیلی پیرامون جزئیات این حملات، میزان خسارت‌های مادی و آمار مجروحین احتمالی، متعاقباً و پس از جمع‌بندی دقیق به اطلاع عموم خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/449303" target="_blank">📅 05:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پول و مقام لایق هدف‌شدن برای زندگی نیستند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/449302" target="_blank">📅 04:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جاسک
🔹
دقایقی پیش مردم جاسک صدای چند انفجار شنیدند، که منشأ آن هنوز مشخص نیست.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/449301" target="_blank">📅 04:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
معاون سیاسی امنیتی استاندار بوشهر: در حملات دشمن تروریستی امریکایی-صهیونی به شهرهای استان بوشهر شامل شهرهای بوشهر، عسلویه و دیر تاکنون گزارشی مبنی بر مجروحیت و شهادت مخابره نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/449300" target="_blank">📅 04:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صدا‌وسیما از جزئیات و تعداد حملات به شهرهای بوشهر، کنگان، دیر و عسلویه   @Farsna</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/449299" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/449298" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4iWDXDIk6kCb5WtPZo7YflLlYlkR1c6B6NVxvZs-8L3vw5lwp5GJApujAD8K_MzypnZ0qK-1btZDCLueO98dGGOSpct5DLS1nh9pcN4yhTk7zhOPcFcL51mCRnzemWwwFZM7_3AIjiMinbvJL4EGeOwcMC8GKtgKTVKQ6jXE-CXdphW6Eaps4AHTMKTIURBRvcaUsgq4SMYXckBpLDfEvz8f02I0PLz_5fnOEWKYyulFegfN7sUCHC8XUTLRvNqLJZnWuW1j3neZ66L0t061w6xwgpA92Xd0S2k9xfgc0ehh0mdRMudFzbILsZaSNC6F32PkHp6mSugyy1uvpXMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/449297" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
تکذیب شایعه حمله به اهواز و آبادان
🔹
معاون امنیتی استانداری خوزستان اخبار منتشر شده مبنی بر وقوع انفجار در شهرهای اهواز و آبادان را به شدت تکذیب کرد و آن را شایعه‌ای بی‌اساس و ناشی از عملیات روانی رسانه‌های معاند دانست.
🔹
وی با تأکید بر پایداری کامل امنیت در استان، اظهار داشت: نیروهای امنیتی و نظامی در آماده‌باش کامل هستند و هیچ رخداد خاصی در استان تا این لحظه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/449296" target="_blank">📅 03:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار از سواحل هرمزگان
🔹
دقایقی پیش مردم از سمت نوار ساحلی سیریک و میناب و بندرعباس صدای چند انفجار شنیدند.
🔹
هنوز منشا انفجارها مشخص نیست و اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/449295" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/449294" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLl9WjHs4HTwnELA6Vd1qx6xv56LT6munC26z7T1ZmfQ86ErwY6ijPoDVn2KdE6zAyIOugOSTmapidrMGUaM0ZcS_mR61UXy6xg_9nLwcuRVmXToH2ydrkyCWS3vB5ev6RS30IDG5358AyUuH_MKa7rMANDD-79mVHFSQXQN-_OLl1XL5lNsWmw9cucuvbnzs_No_mwk2GCDawEQXHjaIAPkXFWqY9ZYnyltAyHYDZxw5tG8QJQHLa02fu6FK70idq2knv4548m-OUHr47C49waNaqei3q2cLYOGq-zr-scrYz9XnGqbsjDn77ZoTyMGzpkxS8XsU3-TOuMRa4WEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/449293" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/449292" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
برخی منابع محلی عراقی از وقوع انفجارهایی در اطراف اربیل در کردستان عراق خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/449291" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFTb94rJAPQWFQIkq-LFMiML1_nmc4a7_An3bJ_v5-UykKGnH-NrgzQhcIFRbvMh6jMMX_Ynh4PqWi_Nvikn1A344iyf-hVX5L8ZJFaZwSjj4uWboOu00H1JIdUTsj2LVA0CqpSeWKKebmw9LDSwraJ5HKPbEnBI6o98iKGM_7GdYIARfJCumr7VlUgdmlI_rFYo9DYO3U3bnqKspVUFS8FT64e7CY1rLAsu91eJ_eT5h_cnR8uqSFqBM6K9U2hz9GEKkstcGF5a1k5TEhxgK-BTs4cWkAMTbvzM9fK0q5YzCij-Z5iP8kVA1M9vVATojNYxsDegFTdjjDG_T47nRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bA43NFfK7H6A8o62RNPvPJcCTg_9uj6rKUojzHVV75AtXdn5IfTJUKSindSpXm-_-CjdybctadK_NywRr5Ky7lIlWR3zduqaNUxnOP68JgDYZt7t8aE-qHsjOVoie5dyOYXwVWtsAgISt7FOiyDkOOmRVTZmIA6QW8px36SYEGaJkse440LqEKhLMkRExGwngy0EatxU-7_XLt4aPTXzbl3x0ZjKV0dSVF9ByXGxh45nip07UuofID4ZOfY8GHxw1n5RNXF8IL46j6VLoZKuJWzsk8sz0-mlyTHetJHCpqws5GV2gsr3j1jeHF0QjPDSf4YmjtwmpevdaZhIvNArRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Tli7xBj3OmSI0Os3ov2E5TxhLfWsKfscce7TIgPyh2Bin-uedY7p-QCMhgLllZXfB5wkkoidSI_I6FMiq9282ZROD3rsCnWix3dlRZRMtBo0CwO572QaKrEJGSZPA5HlEuPiqRdpIEXjFYLPWEsQjrRaN1LaJvgj-NOz82hjVLs_SJtUNdUi5B2nM1KMWPYtaP4jJwbQDWe4gP2XNvmqcICfS821mbyQs_syVQrh-a7amOydOkDcrbJUfeHOGMMczJnbo0dDVBM7POa8j4XJlp6DjkUx29fSzA7gRi1IlT5KRJAAJ2StkyvzA6Cp4QU1HR9NyBesLslctVBIS01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGAo22yr7eDOOU0Jiov3lxsfy9j8pmh3a2wV1VGiJ-LIlmO-kiK5TJ-qEuJZs_7iUOgxkv1wRE-vkxAvyTUxmFCwuMT0UdMM5D3h5sqe7xaWYpFCfiZA7hx1OMkgSaBBQTUq1P3DlDCdEnQb8XtsUoGQOWn2eufUcpezYMiK6C5yPvhS_lyTwIndxkkqJvcshEJEaXGrA0hpWb_M6Wsq2_1Y61LH9T_kJfOMMF_cjmaC4196BZQsH8lZhEZroUIcFkAS8XJfott4cDBF5UwiwqwGusly-Ve3uorD1g7sSzTYsyCoAV-xQCY2WzGrHy2lHDIXSgDwnvnzBkxX6KpBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3om-7f_wOyFlMy71R3o7y71TlUk-qRBy6DRUL9Qk8E6rRdcGQl5A2I8Kq507cTbRNu5NqrsXTn5VDdgq1_P6Ykamfupg3wwDrtwBH0_01iGPbhzmrb4oX2aPJzDI0zY2Ft4iJZBEs6OYfAjrTdIURWBzrn9MEBXz2ZpWdXJWdpFp3ISzmRC2MkEKOyYHa--kPPhxhy4h7ai7rdgAYn4OSChfo0fj9qKvo7dkQOpJYlrrZ_P9YPpjA8huVJnAYXdGP5XGEVuX70ohjouLkyuHnMR5YpkkHuuXxjx-Lh9tcuctUoxsmhLuq4Wk25mPeGvYN3LY23uucasdxx-KYIVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNKlKeQG6oo0Jp8YuY6DCoJAZoy23lQoh1bgUChbLsV84k_0T6sJpVejh0W9ymvDF9_dN0FjFuyNdb629oUaRHl2zruRVsDOYVAVA8Qorr6XBJ08-59x9ay0pnyUu6cnFqBXo0VVIkXmr7fRNNWJJd1fXP9jYyuIp7osR9FwMPDFl3Gsa8l6RZmJHf5VEFsWl0yoxOxPgIvDvfTTFuWaGACLRwzcdZi7x_D0QBcm6zG9gUPGP7KvMeVADg8iaY5tmMJXrUUIJ3BivOWIaaOY88Edg_CE-ZvN403V1wH321uWWUvZhAppPtC0k5MdTzKNFDj5n-30sNKY9_YllqdrTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت آقای شهید ایران از سوی آیت‌الله سید مجتبی خامنه‌ای، رهبر معظم انقلاب در حرم امام‌رضا(ع) برگزار شد.
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/449285" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
