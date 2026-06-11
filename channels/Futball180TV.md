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
<img src="https://cdn5.telesco.pe/file/m7C5MkWIvgY_2OSkIc2S5LWwZzmxepfG_r5vhUHNV-ZLeWKAKULt7jwxK40y5OuFioqr1mKyhDXv2-Edh2SZaJRGXBprZElMeguQ_38XBNBVr9UxKE5JbnaOkNtqN55RaF1yv7UsJGihDH9zwpaC1BgHXo0nk0VDQKccryTX8pdNSgpv0Zp0EPsaiKm82K7dPmKyccU7OQ4_M3_1SCXloFJ78LSExnm0H8S6hfDk3QYYo16jS7it4HsoX-HSzhrI_CNTIr6LPObh0xCMfwi1I1qp3hnJ8vIo0uJq-7TwYpA4X35nREfBO1BcORgxfnbgBVgeKwVZLQF0ERTtT1USTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 338K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-92069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnBE_82cETwQahl20FrdA-rjYLxFfIrZXFFY1ogs2ArlSM14TbdpV4IYTCQ5DN18F69p25Zx30XZH5SeoTssEA8GBdlUqjdqxRJD5o-NHdrB2fIaBMTvCBbb3L95vmhhJpmJIkCXv7rtOHIGn5FB4IHqNR_vtRLl8sisCXs56NJgGO12eaAY3yhROZZLD_5PxcYDGKPsRTTigMZyPv2k-G4Z9TZyhDzRhZKKfkaAGTq867o_4_xme9zl2DZZ9JW3Mnh9iWEnmMQGJYGr0FrulAfwDdXnflDhDQ1ymaDRXUjip6vA0NVzh4ApTrUI9o78KpsIP7BCdTncjqzwTSKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
بر عکس آمریکا بنظرم مکزیک دقیقا روح فوتبال توش جریان داره!
هم میزبان پله بوده هم مارادونا و اصلا انگار گره خورده به جام جهانی
پ ن : عکس از افتتاحیه جام جهانی 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/92069" target="_blank">📅 19:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjGKWaTE6MvsAu6eDVJcL_m2-pDVHjKB2KH6fBy3512koYwrc9iAxc6QloLxYj5v5P4zkiRqzhnCuK22U74u6KsCvomDtDOC3JoVHtAdIw_kVerEzJUyMbb31as5WNHLQFtS6oswmI-J6gz_Cy0kJ-J-rpzNLG37lam0Sd--mhE-2ZEM6ypD2VEumcXVtKSagdELWh1X4eRPX5h952FDpFcwwxpqWpt2Mc6KlXzMTusPZiGOh4ZgomIAEkR2z1oI1Phud5-bzSUD1zQDyxi2gT11gxNehZh1TARmbwki_K-TiTPar4WLSjF_B9vCwLSRiCI4vWbCG9A043qIZSmerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">17 سال پیش تو چنین روزی، رونالدو به رئال مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92068" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92067" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyAldP380a2KmthzkrQ207vt3fsrBJerv7kotWKICFuUDKCixTGW5FkoG7ZxSAvaq-vcbQmVLrluWzAVy5vFPv9PvHHa9Ua0-gd49uee0KP5bwq_-cg0x0AXbXKO-hwRClGt1NUrWXckIpdTjOJL5_YsIoiYA3s-MJswgKLMffKSCaQbKXlv0JfYNXbnyITVJ6OjJZf6naHcBiwUNodxNA2yBpegNtQB2H-3ShzavkwwoQWJMTcdD2Qq71wbMZ4GtHzdindf8KovBmGpn0E2RsORGHppXOfSXG2LwoDHOLcVjCBVPf65CcsoKeGzfs32s7UWo3K5Z8DpsQICm_kqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/92066" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
🏆
💥
ده سوپرگل تماشایی در ادوار جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/92065" target="_blank">📅 18:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKVAu4i8nOige4PxC6erqlihT3i-E7ZFZfN3Mc7DrQoJ_ybUyIKbSDjMnHQ3Kj1Uhtg-wAPeYGX2GzjutVECl475f7BJ3ZzET9th_kLhKHHVelu7SLJ_hr9qqcu_eoMqWniUJN5ZUmBRHHxEn2yfhddFH07pJ0TPFZupxJsPB5KyQKowNf_0TsjLWConrwYh5tEhUHicad7iLmTmkwiot-0IT7Ce3ppmNSbuDFtrDFL-tO-zJ1kr8F3r-S1MeVpUtdLKFwu1g_jkZbs8Sz2XWeAL9tWB59UfKTCW1H1ShFezgjzA_Cj91ggHdW9gPiBt5AlDW9f-aNLPz5ggJhmO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
ارزشمندترین بازیکنان جام جهانی ۲۰۲۶ با حضور یامال و هالند در صدر با ۲۰۰ میلیون یورو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/92064" target="_blank">📅 18:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81506eae7c.mp4?token=v6S_weTY7y8ON2j9wY_ISWAMer3nxiD1QlsuwyxEUNv9Tv128ugRaUXV2e5tjm9n2CggLBEKjNAjtlLaURmnM4kxjCz0Q6oLGVbyFHPBn5jtp6nDisKHS7d58G81jIn6qeAEEJB51MdlezaWhsMRPIEkCio--ZXPZZwFr0sYgUTO5Xa5KG6dwMMMWufOjYrQ5_FXvIUGquCMJcAqtJ9gHJA4IQj2n7UxlvhhhFGnC8Yz0RC661V33vdz9Ypq8M6L9AOz-U7u1rTQA_T4RsED_UqtNVveVlC4CsLhzSwPhEPP3LLZ8HMnkK2kGN0Y3xpexmWn7oZIdegtW-ZVdFsiTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81506eae7c.mp4?token=v6S_weTY7y8ON2j9wY_ISWAMer3nxiD1QlsuwyxEUNv9Tv128ugRaUXV2e5tjm9n2CggLBEKjNAjtlLaURmnM4kxjCz0Q6oLGVbyFHPBn5jtp6nDisKHS7d58G81jIn6qeAEEJB51MdlezaWhsMRPIEkCio--ZXPZZwFr0sYgUTO5Xa5KG6dwMMMWufOjYrQ5_FXvIUGquCMJcAqtJ9gHJA4IQj2n7UxlvhhhFGnC8Yz0RC661V33vdz9Ypq8M6L9AOz-U7u1rTQA_T4RsED_UqtNVveVlC4CsLhzSwPhEPP3LLZ8HMnkK2kGN0Y3xpexmWn7oZIdegtW-ZVdFsiTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇲🇽
🇿🇦
جمعیت عظیم تماشاگران مکزیکی از دقایقی‌پیش و با باز شدن درهای استادیوم وارد محل برگزاری افتتاحیه شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92063" target="_blank">📅 18:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIWWofzJ4KzyWqBz5J_I-cqZRyDy6xM1c9y4jNdpSbpzIxgKoSlk4UEae9tg0aMdO2GEgQy37pk3qlHIR-dVEBZu-shdQUlV-UOD6H3eZBg-wA-y1hUuQJIEJSNLJ0vZwqegLX3SWRtIqYcOOtlrsJ_GLcjl7rPsLCzUM6FqU96T5DJtTFMCTSR7dYWjCdgJg3-syAxhmva-q_lG4fbUO8knz3dR1pgamV-GkrU_3TGpzlsqX8-BwOv-J5MuLxjT-s7I1EkedOLJjP932K1-M1A792heGq5rN8xdL7n3eR5Z7uheBRdm4HlbGdjGFjA-9eV-DJLpTYEOmfcbqg76WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نخست وزیر مکزیک به دلیل ترس از هو شدن توسط هواداران در ورزشگاه آزتکا، در بازی افتتاحیه جام جهانی شرکت نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/92062" target="_blank">📅 18:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beMpvZRM0V9bUoFAoEUbeochWajNBttzgtJCVOjAcDNMvnH5C03okhAJBDJAnPRvaAwkzE1snJvSLIkqe-C5qhZbtNxWxRhsKgsAzXCP7HygSZe9lG8pzQuP6rQ9RSsbQYxX8_sK88FVtXk5sMHFNKdhTX2ceNtOYne0BPlPSkbj2XQlLUFMqpcTfjJon4JlXQj5uNyrKEzKDK0EEnqmsg66o8T_YxIBSa1UZ_w7d1pVQdzi4CRuuhzWaO3wydzEGZtQR_eN0fn8O3wpp23WZFFwuiD_0oLcMImlXp3EZ508pRb498WPc3_Cl4cALfra3SApDraxvuhV54sIBWVa6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آلوارو موراتا: "کریستیانو همیشه با من به شکلی استثنایی رفتار می‌کرد، یادم می‌آید وقتی برای خرید بیرون می‌رفتیم، با هدایایی مثل آیپد، تلفن‌های همراه و عطرها ما را غافلگیر می‌کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/92061" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c5dd1e48.mp4?token=MyGjXH8wWHBQ-DbNN165Ed9OezsEkBMHljf-wkEue4RJBRg7ItUnkc6RqNDGAVCuAdV7RyK87XiXdVR5w_Qs71XGHIJSzsFwdSxTANY3dy5891AQB_VocwkGR5XszZnm_GgLhFVcYdpAiBIEmurrVUPKyiRktMV8wpiXxOHBgjuhCKywKK3Yg1IHFjCf0Uo1I3sIVUCOkINNzd9eYKHSmw4NSrVuHcAkCmTYNoijG7gK6cQbWnL4A_YR-WhcPb5LGQ0wvXcCB6QeZ47Io7teNNzvfvYWJ0UmCPGiN9lRad2P9DReZxCmMIsZGyHQHA5MyJw6Phb_iwTQZ5IawveSRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c5dd1e48.mp4?token=MyGjXH8wWHBQ-DbNN165Ed9OezsEkBMHljf-wkEue4RJBRg7ItUnkc6RqNDGAVCuAdV7RyK87XiXdVR5w_Qs71XGHIJSzsFwdSxTANY3dy5891AQB_VocwkGR5XszZnm_GgLhFVcYdpAiBIEmurrVUPKyiRktMV8wpiXxOHBgjuhCKywKK3Yg1IHFjCf0Uo1I3sIVUCOkINNzd9eYKHSmw4NSrVuHcAkCmTYNoijG7gK6cQbWnL4A_YR-WhcPb5LGQ0wvXcCB6QeZ47Io7teNNzvfvYWJ0UmCPGiN9lRad2P9DReZxCmMIsZGyHQHA5MyJw6Phb_iwTQZ5IawveSRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی : این آبه ؟
مک آلیستر : نه احمق اون آب نیست بده من
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/92060" target="_blank">📅 17:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0db4c3221.mp4?token=nNBDfXDutfdoAQDDVXVjX0mRpXuyZrglgaw1hqitGSSIFzUEOypLq2KesKP8Ygoys4hp8GXDUgcA1lCmpA1FaCQThKvjc-j3uxowE01gyIB7hRwD0ETrMwmlQxZWPTCoym2_k6FYOWkBRsl4ujrje1yPdudIZ8aGcZn3f4jGXkcZQrsEAfc_LO9qc9JkJN2a76abcg1YTcbA7Pp_tE1k2ZKLx9l5XmOuH0euBnTxRzDXKBmdrMsgnbj0nF63WX8Y9-AiCNofnwU11quUp4dR6I6AWRMg9VAALJYA0mqNiWLjacEA-X-uYzqP-BFVFuw_J7eI-X4U_11l9YYE6-8qmL98Nn5T1Us91S8dDh4h6IT_fdGHI7YaeeRGbTNqg4t8wwKi5zHM6V8aiTbbvVPL00EEVEiL7E2UIaE8So-9lUK1L46rnoi7e5Xg6u_akF2JqzkxONrypXp9xxK1dGYKykOsGvE5_ltRxOsDHw3_-lB-KiFgszy4sQfelnomokbXZ9z_yjd374M3ljLj5EcEnNThdSBS8AEv-FiEtB-I_R-aTTDhWa039nX9SH3d_AJInzyaJt4oy-f7Mz3Ic-oxJwlgam-ueVBx4Ep3BSBO2VEqNDWOf2kPNBRMGCX636BJcW9HoVMRPewohJV2-xl9qn8kGfSshK4fJfprqAD_Vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0db4c3221.mp4?token=nNBDfXDutfdoAQDDVXVjX0mRpXuyZrglgaw1hqitGSSIFzUEOypLq2KesKP8Ygoys4hp8GXDUgcA1lCmpA1FaCQThKvjc-j3uxowE01gyIB7hRwD0ETrMwmlQxZWPTCoym2_k6FYOWkBRsl4ujrje1yPdudIZ8aGcZn3f4jGXkcZQrsEAfc_LO9qc9JkJN2a76abcg1YTcbA7Pp_tE1k2ZKLx9l5XmOuH0euBnTxRzDXKBmdrMsgnbj0nF63WX8Y9-AiCNofnwU11quUp4dR6I6AWRMg9VAALJYA0mqNiWLjacEA-X-uYzqP-BFVFuw_J7eI-X4U_11l9YYE6-8qmL98Nn5T1Us91S8dDh4h6IT_fdGHI7YaeeRGbTNqg4t8wwKi5zHM6V8aiTbbvVPL00EEVEiL7E2UIaE8So-9lUK1L46rnoi7e5Xg6u_akF2JqzkxONrypXp9xxK1dGYKykOsGvE5_ltRxOsDHw3_-lB-KiFgszy4sQfelnomokbXZ9z_yjd374M3ljLj5EcEnNThdSBS8AEv-FiEtB-I_R-aTTDhWa039nX9SH3d_AJInzyaJt4oy-f7Mz3Ic-oxJwlgam-ueVBx4Ep3BSBO2VEqNDWOf2kPNBRMGCX636BJcW9HoVMRPewohJV2-xl9qn8kGfSshK4fJfprqAD_Vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
صحبت‌های جالب مجتبی پوربخش راجب افتخار تاریخ داوری ایران‌ و‌ آسیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/92059" target="_blank">📅 17:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهایپراستار ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5kedM18a701wYEe8pgnxx3aGkpsYXyKibqweWFayHSWU6CePE13pNiWnIthEGblwhuBPJVl0VCnCaIqsbfk4LQZXgHJw0KZ_RUkl4lxcfyxfqYykDLY_jnFNQIb2ex2AswrJmBHwtrZVVaySDjxZQwlMIgVhkwxXVjU3SRR7VOCJMPVcgkQ43eWuyA6szerjoSUyMHpzws_3pDvlR2mTMjLlVS3_EA8talRnjsXwt9TQh82_eljS_UZ3vJRKjPXar1q9Wp5FenWnvlr1J5c4Pt-Cl4tygoyb1PwiX-4hVHrC3PI3fM06DrVnr2dKT59fWnIhim648rjr-UqLOLohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی کن، پلی‌استیشن ببر!
🏆
قهرمان رو پیش‌بینی کن و هر روز بیا تو ربات تا یکی از جوایز رو تو ببری!
🤑
ورود به ربات پیش‌بینی:
🔃
@hyperstariranofficialbot
🔃
@hyperstariranofficialbot
🔃
@hyperstariranofficialbot
بازی امشب:
مکزیک
🇲🇽
- آفریقای جنوبی
🇿🇦
بازی‌های فردا:
کره جنوبی
🇰🇷
- جمهوری چک
🇨🇿
کانادا
🇨🇦
- بوسنی و هرزگوین
🇧🇦
کانال رسمی هایپراستار ایران:
🔤
@Hyperstarofficial</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/92058" target="_blank">📅 17:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خایه‌نیست که ماشالا. پیکنیکههههههه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/92057" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFGjej0Wei7xq0p1mLucyISc9VtJvAbN_hjZZFtcmKajiqj5eMmNTJUobKm8SPWtkZ8q_LJfWxu5zjohab2G-S15PKoOY2kYFuv2Gg1UdNgJKEh4g-xB2wM5dDWbMx-a-UAPX7DxdfwArZhUFlHmsywVWgIhbbuV_W-BapIpjVypEP_3Mw0nIzkw-NXDdmmmz8EBVjk7ctclp4Rldnoa4qBjG6mzkUfMcKjSUtp_sie9uCNDLo5FgnAsRdeGsf4MyFMZVfG_y07r1D6Fnf1lOQpfbhqCG7ybpkOBuaRHB3XrCmqcu0PWlUvN44X-16xqHuAi6DgrLGM74-7zam2N_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏟
وضعیت ورزشگاه میزبان افتتاحیه جام‌جهانی چند ساعت قبل از مراسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/92056" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKxkPhsguUfNYhaxStLYnf_NmHMQKTMlgBSnbKtoz-0t8ygf71Wq65uisPT4dCKVAmfivitFEE-IqB-nPqcCIpszNpa3G46jPsodHLwEGWdjyV81FDM6lWzP96fofdRUeQdN_UUbLjeMQCNqOXWo2V41rvSJkXQOOdhftwT4ITF4cwskq3Gnp_kEMimwmIF7ufOafN0ILCUMrajBGlUIhRxrvLfTIRfv3zI15lmOw0iAZOHPN00BA3gPuJ4OTAxVUJu_dsEf_2JzSxHHn-uPdAtWemyGz-9Wk8tzu0q0GjBA-ICV0rxc1hP4C0X6T_TRnZ0zyewDcF3AN-Q-A-LfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب ستارگان جام‌جهانی که آخرین دوره حضور خود را سپری خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/92055" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnmxnLtVCVF9l6sWUM8ucz_E485_njDBeqqSx6vIla5A7wE6r2CX6RsLFHby2ebiWt_DNv_TjR_nIq8DniLcknRzpxyRYknnkbhM5fmu8mZakjPou2jNzpT3YJ0wt-yRMyif9Gtc8cvmyueJQg-ZW3an9XC2mZik5K-6IW3LhXQF7jCuKBRKeNRaOEqyPql279_NJQEzmkVov8zZzVhbRCMP7xJR89CG0pSMGtET5kyGBurs7hbyofCOxXbfvJ7hOnTQIdEFT3JiQw1MoDYqF7pq26NgnWjY10rF3oExEHLBhcQJpmwz_GmZ4mM22zboKgf8rKRBsr0DGAhrAvfruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین پیش‌بینی بزرگ جام جهانی
همراه اولی‌ها جام را به چه کسی می‌دهند؟
🔹
همراه اول همزمان با آغاز لیگ پیش‌بینی جام جهانی در «همراه من» این فرصت را در اختیار کاربران قرار داده تا پیش از شروع مسابقات، قهرمان مورد نظر خود را انتخاب کنند و پیش‌بینی‌شان را با سایر فوتبال‌دوستان به اشتراک بگذارند.
🔹
در لیگ پیش‌بینی جام جهانی، کاربران علاوه بر پیش‌بینی نتایج مسابقات، می‌توانند تیم قهرمان را نیز انتخاب کنند و بر اساس عملکرد خود در طول مسابقات امتیاز بگیرند.
🔹
برای شرکت در این پیش‌بینی
اینجا
کلیک کنید.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/92054" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32b927065.mp4?token=DXFEV6A-zuhyULK-xcOn91g3tJvG7kjo84-IbsWzjl3cxPGx2OaggAt4dA0QmTcKtn-w4ZGmOeWA6xE6BhI4NGux38qnpNqaMQTEMuQSzxhQYs1U8v09qSZuv7Tf8rKGjQQmJ6hKOjh8ju9xXxerqJTG0Js0thp_c-Qjr1GG_lqZUidiDqf9rfGPBv2cONC74qDzTW6NynlFeeKcp3JyYpGaqJv-Bg1ep6_LSI09QdzV7NfqQSfvFG1l86zSOI7E5QyU4p6eh8yCq-7mhu-L3iYOGjV8Sb15L991H4JeQ35jRl16dSUR5pxqE0KnWalK8LHBVvWdmwwcpKHZY_an3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32b927065.mp4?token=DXFEV6A-zuhyULK-xcOn91g3tJvG7kjo84-IbsWzjl3cxPGx2OaggAt4dA0QmTcKtn-w4ZGmOeWA6xE6BhI4NGux38qnpNqaMQTEMuQSzxhQYs1U8v09qSZuv7Tf8rKGjQQmJ6hKOjh8ju9xXxerqJTG0Js0thp_c-Qjr1GG_lqZUidiDqf9rfGPBv2cONC74qDzTW6NynlFeeKcp3JyYpGaqJv-Bg1ep6_LSI09QdzV7NfqQSfvFG1l86zSOI7E5QyU4p6eh8yCq-7mhu-L3iYOGjV8Sb15L991H4JeQ35jRl16dSUR5pxqE0KnWalK8LHBVvWdmwwcpKHZY_an3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
اجرای شکیرا دیروز‌ روی استیج با موزیک دای‌دای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/92053" target="_blank">📅 17:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: ایالات متحده از این پس «هر شب» به ایران حمله خواهد کرد، تا زمانی که به توافق برسد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92052" target="_blank">📅 16:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYZhFBe42qjAJ0Uns7NlKT-l9i4a65MiVHcyOlQvxu3_di0IdU7fTawPFAlHZV_U8S-Ny_T-tbLwWnBsyMuTqcaGOD5Z_bYXMlMOgIKk37vW1nNX7R3ddbyMTofWoL6iVck84GLkj6yZb590LAMsz-kzGDVTQtT9e5Mr4MuVS-lY6vhW7goR7BuYJDGOm0jteuajpQ7Q3Ma584gQYDMMCjWa2qSKjgRLzRnvG4UJROo1Lt9JG3PVKwzMOhSy3wECQzk6VkakQ8ivPjeocb7XIF3w8Ki56bnP8AqNBaKUwZqSZWiercTWRQkf1VnLX18YVZdfHka83v4hodEyFH2_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤝
🇫🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتحادیه اروپا عمر ارتان سومالیایی را که از جام‌جهانی منع شده بود، به عنوان داور بازی سوپرکاپ اروپا بین پاری سن ژرمن و استون ویلا منصوب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92051" target="_blank">📅 16:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1c02dd8f.mp4?token=fGEf93b_GZltKPOhjeshyFoVy-OMKJQRA_3KSSp1Xj_IAf8gGzrv_ryiaeCHRqnu7tbwUpCG2UkBGOikPN18xfSpGOQaax4pZ-x3ITth6q9eSSyQLS3SuZskrVOHq9oCYUhXSS2YKNbiL7GtwqOvGlfNX9ocA9JsqAyFSBE2tIvfp9iT3qJ18E5BaNpq32umPz1Nk06GorOqspocqS-_qCZWlyRs8gGlEKqsRd3c_F3OR7Bgwf2Wd0YHllNHvthayGhJ1-uCCzVYJonFoO58-AAKR2CJ_LFJS4gtIPXaunaxFq9PbGdvQtT-1h1mh4vIerOHjGdjKLUCYwA6Vdm_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1c02dd8f.mp4?token=fGEf93b_GZltKPOhjeshyFoVy-OMKJQRA_3KSSp1Xj_IAf8gGzrv_ryiaeCHRqnu7tbwUpCG2UkBGOikPN18xfSpGOQaax4pZ-x3ITth6q9eSSyQLS3SuZskrVOHq9oCYUhXSS2YKNbiL7GtwqOvGlfNX9ocA9JsqAyFSBE2tIvfp9iT3qJ18E5BaNpq32umPz1Nk06GorOqspocqS-_qCZWlyRs8gGlEKqsRd3c_F3OR7Bgwf2Wd0YHllNHvthayGhJ1-uCCzVYJonFoO58-AAKR2CJ_LFJS4gtIPXaunaxFq9PbGdvQtT-1h1mh4vIerOHjGdjKLUCYwA6Vdm_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من از این به بعد فن پاراگوئه هستم دلیلش هم به خودم مربوطه هرکی مشکل داره میتونه از ایران بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92050" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhKBR9C9TWbpEhxHF6aa30wF_xUYfu6U5S9okCHcMf3a_yOofMjkhV-JVrUBjw60SOZe62CvhK-m6gF-nkcpfsB62tJnt5lnOqNV9lXvHfbuP3x6PUWS99nSw7RG5qUv9Beyozzd-oBtuU-M7_dULMCV8O0JERgpb1qtbeiMNSxX6HHMeQcXYrTpbXdFuj8IFwbsbAC7PETs7VZKuU8GhPk8IM1D9WKieEbjYpMD-fOZ_8GWR_KrUROGz2JoKkJiCE__MJ7yDu9-HvuicwRsZEgeFIXwVBYlNYD21n_B7qlCfSCxyJyexxMpeeZx9RkF2CSAMTgD09YFxVoEWYDDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز : برناردو سیلوا به شدت به پیوستن به رئال مادرید نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92049" target="_blank">📅 16:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c32ac0cc6.mp4?token=Dn-h5AAv5QUzd3-zBma4Gii-hfFiFGjVUCypQQE591o40UrAf3G_Xk-qIa3RKikjLxiQflHbQsMDwCuhgK8YINMrNsaZx80LGLjpcKH6kV1WT9FUop2htYthzq6g7xmDk_yF6DAXOzU_1_wCdol2vuVtUGvyaXbs8wJa-jdwxLGjKN155cqle7IBIxh1ST4k7K1eeaKELUmSt1mFc25NIxFFoskZRr2ZnbJZVocptJfd8z1M2ykssn9NnNBWhqnujmofPulqbIg6LYghrJ6D93LtE7e86vRZeDXB8NmcjUk8g7rNhwqwEcR3xiIet3du6E07ZUfjPvRUDinYi0xK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c32ac0cc6.mp4?token=Dn-h5AAv5QUzd3-zBma4Gii-hfFiFGjVUCypQQE591o40UrAf3G_Xk-qIa3RKikjLxiQflHbQsMDwCuhgK8YINMrNsaZx80LGLjpcKH6kV1WT9FUop2htYthzq6g7xmDk_yF6DAXOzU_1_wCdol2vuVtUGvyaXbs8wJa-jdwxLGjKN155cqle7IBIxh1ST4k7K1eeaKELUmSt1mFc25NIxFFoskZRr2ZnbJZVocptJfd8z1M2ykssn9NnNBWhqnujmofPulqbIg6LYghrJ6D93LtE7e86vRZeDXB8NmcjUk8g7rNhwqwEcR3xiIet3du6E07ZUfjPvRUDinYi0xK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇭
🇶🇦
نمایش‌تمرینی کادر برگزاری بازی قطر و سوئیس در فاصله چند روز‌ مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92048" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ: من ترجیح خودم اینه که پل‌ها و نیروگاه‌ها رو هدف قرار ندم چون مردم نمیتونن آب بنوشند و رنج می‌برن، من نمیخوام این کار رو کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92047" target="_blank">📅 16:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به فاکس نیوز : ایران الان داره با ما مذاکره میکنه  ترجیح شخصی من اینه که جزیره خارک رو بگیریم. فقط مطمئن نیستم آمریکا آمادگی یا تمایلش رو داشته باشه که چنین کاری انجام بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92046" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5ubhACXr0TmUIwXIlxUUhEKz_aT5_5-7VRfFvPJlYu12bFIDJsBw-Z10AEzxfVnemDuXzKxlVSgQzx0MhcFeNI4WjkcI_Oqo8CW-Dw_fkGJP8iJibDqfvQuSdDrJn4PcEOi0ByVN87hhfppedOyvJHccyF5GWHzhnHYSp4_3PpF35jj9LVLe-CgPdwxY4VnKUo28pIq85zMFk7hAkrbs6T5HD9utJqttn3TlrUzy7E4yGEI_PTrA22wWIvX7OEw9mKC7_HPdlZICp7ba-tAePZ9P7fcxhI_xHQUTwzPt-hQIUfcLrrtxbbvBpfiDXC6y4swIB_QoJ5TqApFCOUZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ به فاکس نیوز : ایران الان داره با ما مذاکره میکنه
ترجیح شخصی من اینه که جزیره خارک رو بگیریم.
فقط مطمئن نیستم آمریکا آمادگی یا تمایلش رو داشته باشه که چنین کاری انجام بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92045" target="_blank">📅 16:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787198f5a5.mp4?token=pE4vJxI81pMR_TRsl94okURH-L9fKZTC5gKnmhZHYyRBj112T7B5MLhWYB9b97a4Eq7FYUNXGCT_cGpfhfq4VCQaKrkEFvV_X3spkSMH9reunTVmIwFU0z2uVlSMUgWX-5sbGapKDi3J-t9wsTtTFMJr6lSNMuBnmbYp8Yv8IsIsSW2jAE77aGOWuorDM54Gmx6ZwP_1C63xIRGdB2-fRjAkoFNiW4ECQE7rd47Qw84odH9SpLMlEUFrij6A0BFYl6lQ8RtctoLCN6z1Q5FcAGwabfsAiv0dwjXjA_d-Qj9UyHEP14od9hlgAq6jAgY5iCqEJSgkHoQx1eJ06LWikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787198f5a5.mp4?token=pE4vJxI81pMR_TRsl94okURH-L9fKZTC5gKnmhZHYyRBj112T7B5MLhWYB9b97a4Eq7FYUNXGCT_cGpfhfq4VCQaKrkEFvV_X3spkSMH9reunTVmIwFU0z2uVlSMUgWX-5sbGapKDi3J-t9wsTtTFMJr6lSNMuBnmbYp8Yv8IsIsSW2jAE77aGOWuorDM54Gmx6ZwP_1C63xIRGdB2-fRjAkoFNiW4ECQE7rd47Qw84odH9SpLMlEUFrij6A0BFYl6lQ8RtctoLCN6z1Q5FcAGwabfsAiv0dwjXjA_d-Qj9UyHEP14od9hlgAq6jAgY5iCqEJSgkHoQx1eJ06LWikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
☔️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت استادیوم بازی دیشب انگلیس و کاستاریکا تو کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92044" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
🔴
ترامپ :
🔻
ایالات متحده امشب حمله بسیار شدیدی به ایران انجام خواهد داد.
🔻
در مقطعی در آینده‌ای نه‌چندان دور، ما کنترل جزیره خارک و سایر زیرساخت‌های نفتی را به دست خواهیم گرفت و تسلط کامل بر بازارهای نفت و گاز آن‌ها پیدا می‌کنیم
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92043" target="_blank">📅 15:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU-Iz-4tFjSZBeZUkM0Ft65UAWyL6165sEcfVuh1gSVDQ7U6EdWQKjntz2axBgA443jqX5W-Bf1PisQ-ApgweupLSmVCkndjQN6KTfuHfC1g0ZTteB5Od6_FPNTP909Kuzi5lmAO8Qp_O1JeQ732i0ghCnBqlwpVcYN1rgzdZz9ryUeZBgaKAozOAR5DcFZIXFgPxzl9iTK86z3TwD_W1cnBPJSo6tnG2q1OlM8yTdjs5b038MtuGk1UZZfDKwaVJXFsLG6nuoko-Pd1CenBYV430kv2NCuj_uEj9nMaItUon6VUv_moWwZlVcQDseSug7WuqbKtB6CcKKL29dCXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز : برناردو سیلوا به شدت به پیوستن به رئال مادرید نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92041" target="_blank">📅 15:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f53efb98.mp4?token=sndVT_ko7_mTM3kl91kBmlXgwAwHodR0P8f3A33CFI6ev2RJ-xeFNLC7RZVBY7uKgc6mAt2RnNp8yhPu-gnDQo5Bi9kW7_BA12vzQ8kiXlYbiBMy-mOurZv1qy1QWmjc7ss9MbYT2DpOE4j7PhivrCg_oF3G7fEKFavoKNn3h97QhY4glp49TO6a-bmoumoYu3YcRKbCXIXIoI1L9fEWPwtz87D7okpUSj9pAUl4Gs4bsaanuorQ6u5FuFFp7KIiXtNkCklZ5wW4p3mOD7xanUnBVronVX6JVRdWM_GkDcG-5Z-BiubBHldiSFI9HDcpjLDgX-sXorCZtma-JzdMYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f53efb98.mp4?token=sndVT_ko7_mTM3kl91kBmlXgwAwHodR0P8f3A33CFI6ev2RJ-xeFNLC7RZVBY7uKgc6mAt2RnNp8yhPu-gnDQo5Bi9kW7_BA12vzQ8kiXlYbiBMy-mOurZv1qy1QWmjc7ss9MbYT2DpOE4j7PhivrCg_oF3G7fEKFavoKNn3h97QhY4glp49TO6a-bmoumoYu3YcRKbCXIXIoI1L9fEWPwtz87D7okpUSj9pAUl4Gs4bsaanuorQ6u5FuFFp7KIiXtNkCklZ5wW4p3mOD7xanUnBVronVX6JVRdWM_GkDcG-5Z-BiubBHldiSFI9HDcpjLDgX-sXorCZtma-JzdMYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
چالش‌دختران‌ایرانی با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92040" target="_blank">📅 15:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
همچنان از بانوان ایرانی با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92039" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAOUk_xvuUWC803wCVMmw-Y3WV0eiooZ-f7-XakqVZjvdB_Ei1MNyffdqj320gA4-qjk81VwOOUuJfHVm2yWiBYGWuGk1tS7FIIBAcNXDwv54BhV0UOl5szfAViDV-o2F_l24UQqiwqddd7urrtcFf-06rDEBdAevTeeocSveV02h0vZhIS_QAoyJdCT4PK1nz8zZXlvYhBAS8MGbUoXws9D582l1jCIoR-1vcJKUalmBZsN0u8XHSuFJeZmUnoQu7HqNIqcDijdy8E5k6R6_fy4Uwu_mJFazAqnXw3I3sa0TN6ydydLUprlNyODWXGtKHdkdaNH8q6o3PheT0LNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم های منتخب جام جهانی ۲۰۲۶ با قوی‌ترین خط هافبک سه‌نفره
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92038" target="_blank">📅 15:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td2Vq3a6clHO2qQJThPDiesHHVpw2TrNOxt2x4Oc_mFTaDd7TsQnFdO7CJgXstC0mNEt8VRP7iCLnihgfrzQTZzSaf9xzqpmx5IhyUBKlJuPVfwm_LKJT0O4q3SMwuSUcFO98EwiLI83PKGrlLfhC-40wJhI1fuHZ-IX0nYgMqAF2OWGHUgXRohpgjWCZVkFzxtDpPfm_o7wVjCbDhg_kPA7ut7jT3Rf5HswsCpDpeYwtxuBf_fAi7r2CZjss6_yw1SOA_7j20cAGRXZsiOmsHFg7ozluAgBY2A-PaDeNzBITYYyfM9XCmXU5YPj_7eIoZFzRXKkAqUrZ_sYP0XyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر غم پشت اون لایکی‌ که شکیری کرده هست
هر جام جهانی میومد یه سوپر گل میزد می‌رفت چهار سال دیگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92037" target="_blank">📅 15:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✨
ورزشگاه خاطره‌انگیز آزتکا؛ محل افتتاحیه جام‌جهانی فوتبال بین‌مکزیک و آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92036" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که جام جهانی ۲۰۱۰ بازیای اروگوئه رو میدیدن یادشونه فورلان تو نسخه پرایمش یه تنه کون همه تیما گذاشته بود، آخرم جایزه بهترین بازیکن اون جام جهانی رو گرفت
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92035" target="_blank">📅 14:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDZKmeHScKqePK09h34Yitu3wKkNBhfZcEURgD7iEUFx7X8kmfWxBi-CWKZjzQHaTKlhuuVj96vXCDoSGoqfgGhfwoO640WUKBDtqS-E0ajIABwefglr37QZlJu5hE4QXz1EC13sawh18J6-N2Gg9pH8N3YlpgdGxlabvvtbbaE5lJUA-vPHayFPfjy-6cbNBr37TANslRiSNWKNgJ0bBUuSXyxrqOirjYCEb6F5zGAFeID5goMbDg7g4uKUPBeGW0cfZWkvLXG5_8bL1MT-ThJLZ2x4iViVwM_Gln3Vk4G5m4NUs660IR-uz_VFOOIcDCnEoHSTMU0fwyKo_4xP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نویر از جام جهانی 2010 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92034" target="_blank">📅 14:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0LOqq5mVYYGAheyo9Sec1ImUD_ERTqNj_rAAu53M0xZI4WHP3VXVBmucgEiAEBP-MNrixA5Cjvc9gdfzVyl-qkDIP63bJTa_KBjjwjvsUAtpRTkXIl9hgmw6z8PlDsZO-Yl1nj5QSmtiCcYbPHZF1AX94HzZ8mnQwktYTjYL8OlKPmMSr39SbcYEzvH5aekUSXTth1n1CY405NU2ZYXns79hRs7_8OeFy8LvHmd8eaVuEwTVv-mTk1tUmDH5afeYxUuhTWa-VCFEYAyOGbmZW7PLtMiN9WcBomlTbN3QdwKdL4r6PW4PZXY6TVN1NShLXfx1jrJNtrF9JMvj7wSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس‌های اصلی قهرمانی جام جهانی ۲۰۲۶ براساس آمار اپتا تا این لحظه؛
اسپانیا شانس اول قهرمانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92033" target="_blank">📅 14:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdWVrE85iwLV5BIgdAJfZIWKY7CHT82l_DpXAB446aBcK0b42sulgYWIk1ieIqiA8MhtTe7eUWpe0W2iCDNOdcqnXijrIztAP6bEonHzoau4WzNP420SgruK7YzBiXPjzc_Vy5pSo6huJqX82OLPqcLIXHetD1t-CJ8YKJIrJ7RIdSaWv1pKclAp5v7NdU8rwn-uIQcHAfSE5ohGmUQmp2grXAIPQC_3VODbyUd3cc2fHjnTNj7IlPcRIHozAyN_2WqquOQHmULlcFmgyBY67hG9gaOOTdDvv04dxUczSEVC-gUnas_HC_Ok1CwsFuV5OgxB4lbBC69wpEnKowqVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtRDnSoeYPxaxi9JiuJZwsRXD5nc3P8zYuFTFxCxtxgF-gGinPY2PCqDfLWMrlldmAh1XFBlR_JnVgGtb89AD7MWXJPvREOIj2ezS31MZ6rW7-xbXHCW4f0nq2ffYYNQJhN07fCf_Zbquxwnojpo00Gh361kVvPvFl7ZPp6jSV4IJ8e2svRezo_F-qBeZSbN07UJn8khV4097KBRWnFOpNk6BWW-7r5mWG1YkczzbqCCi3pa3M59pgFD1Osjs6cWPaVfTmcdftmCub1WxTrnfRJT5kU3G-Q1sOKdwTnHHrpW2oOt34EHP1nIkcu31XKDDY46U3jZI-8eaHCfQ0ozww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکوردهایی که کیلیان امباپه در این جام جهانی به دنبال شکستن آن‌هاست:
🔹
اگر دو گل بزند با عبور از ژیرو با 57 گل بهترین گلزن تیم ملی فرانسه خواهد شد.
🔺
اگر دو گل بزند، بهترین گلزن فرانسه در تاریخ جام جهانی خواهد شد و رکورد فونتین با ۱۳ گل را خواهد شکست.
🔻
اگر پنج گل بزند، بهترین گلزن تاریخ جام جهانی خواهد شد و از کلوزه با ۱۶ گل پیشی خواهد گرفت.
🔸
اگر به فینال برسد و در آن گل بزند، اولین فوتبالیستی خواهد بود که در فینال‌های جام جهانی ۵ گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92031" target="_blank">📅 14:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🏆
تمرینات شکیرا و تیمش برای اجرای مراسم در افتتاحیه امشب جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92029" target="_blank">📅 14:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92027">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
ستاره‌های جام‌جهانی اگه زن‌بودن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92027" target="_blank">📅 14:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92026">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🏆
🇲🇽
برگزاری تمرینی مراسم افتتاحیه جام‌جهانی در استادیوم آزتکا مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92026" target="_blank">📅 14:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZ9eO7ztf99Xo5uUrc68ZcCUD4CaMR4mjGjcuocZbaLVLY4v-tBqpaZIp3vMAuXqc7KTX25zp5AJ_0-XMymjDt5HT8IuLUD2ZAp1dRht_3sIpgs83ftbmTVwFl6VQ5a2UAwOGXjeLjPoPxIIQFE9lBhNmibIvwAIIneBSitI0ZIfQ1vKwT9u87ozEZMItH3Xjc6o40_MJSNJWCauoAhJ0i3TQ-_Z0Z_cUOmUhhpXtWiNzy7prXyl0D-qtLggxSfiEnOwBJCNmLyPB6qtGcrIol2aBL7LoBE2PEy9Ju5h7nH1dydcavpFCdnQypOIg5j6mV7VhS9VCJTDJHJgfkSKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تابلو رسمی نتایج‌ بازی‌های جام‌جهانی که از تلویزیون نمایش داده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/92025" target="_blank">📅 13:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92024">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇺🇸
واکنش بازیکنان‌ تیم‌ملی فوتبال آمریکا به کامبک باورنکردنی نیویورک‌نیکس مقابل سن‌آنتونیو در بازی دیشب فینال لیگ NBA!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92024" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
توضیحات‌جالب و دیدنی محمدرضا فغانی در خصوص تکنولوژی توپ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92022" target="_blank">📅 13:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n64-hMNgf-JUp6imbTsk95kyB8IqzBsuIesgi-VhdTuuFypbzgcqikvhfYV1guaK_gT8ijngO0yAKAC6ji-Sh523R-EG9i88i46Jka61tjJSfKCs-naA_9Tja216OIkIsd0NB9P0B9JomCZK-9aF-ffDrIpMNFpd1I5m6_vkTYiE7DgUosZya9dCipVwwRPZGunmWsbP3HCBNE_as3_r_w5xjGvdT7DFtqVGYzTL1FhWoqPbtubijby7iv8Q_8hBsmYh8FjqD_VgEdEth0YEO1U7bD4Fo78M5swAT-qny2V_pdotikmN6l5UdSHM3uSNUE02dd8WQu3UJuxxTi2DFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/92021" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_53cufKO9TEZ71oD9CWg8b752WJqJcLAsrUKjSNh1ZczEuuBeuZjTVMJJRwtJJ4QQ4Hfr3Pc7tUZAtxZaKlPkD8DJmgOK0Cfh0TyRLhsDW0RC6v8IvVoi5q02AIKAkrPhYcL1-u93FQKwMFLrL7xDd6qNKYj0Q5WCQXNme1T-ETu8mp7pVGbhFuaJlngCMrnAawMRqMqyqNmPVf3UrFnFFGIn3tOktahhditEGO5BZU61iT1JGNB-eqF3v38J-dYew9wgwPZXWV1Mk71Etfutset06IF1-2riFk7VahfGZGJQyWukxYP9rgMA1nlatoYIAsg-v27wQU0Iio37uEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇧🇷
رافینیا:
احساس می‌کنم در این جام جهانی نسبت به ۲۰۲۲ بسیار بالغ‌تر و کمتر تحت فشار هستم و میتونم عملکرد خیلی بهتری ارائه بدم.
به نظرم وینیسیوس جونیور اون بازیکنیه که میتونه گره بازی‌ها رو باز کنه و ستاره ششم رو برای برزیل بیاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92020" target="_blank">📅 13:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92017">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3kc1znd3FvFS9EY4xLQvyYcl9Dh0_QjwZkeng_Jqn0rD_EcOxNnmu9n6Pb9IHCqs_4Y3fEynr4Qxw_WMjPH0niW03AmL-AEDeiTvVd23uceP6J0TnmnUQE4KxoMgkdi55aA6lx1T_UWJwVVI_L_UvTg0PskOpqFobPCl4w-6QVSxN6IC-Kpedrj54VrNKffeAAMZV5CbR--7tHadIoYfiB1kG--cRieyHFFI6thxmE1oDvLgiNi9H7x5fD7KHR91ztNtDkLWESsrYxdk1FLqHm0_KfcLgX-MMXFzGz26BlJLAWFQUmILi8zwa99KZbIHGhuF9GcG9p27hU-5YhzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyEylk2rM3-ZV9fk_ll4VOH8xjblwQpASfkRR8z0ks7Wr44-GNVykeZl7r-XQnhooDklKTGZvf1UJqGPx5kuIZE8LzP1UVY40u_oq8UDaLfEYDICHLs-HuKfJdgcWpQ_U0QHvfvdCkgTta0zbppFxRPm_g66_CMrSgZSp9DhjUzRlYFdJc1-axO89oPzIlbSsp1S8E-br7DI6rZDbc86L2IEpAVGYGxibXY3i807V1lBX1Hq41dk1xfm_y72jUgVo4t4FzaVwgAYNGLMwHYSuIOQwpEsda7sChh1Aum-7BGmG4UUX40ah9nuaYzlB2yqNzo4dmO7x0jWHlh26PSllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyQY1lMsG7jNA9nybKkmSyi9WqUsxYT_auPXOAk6w5nU9aSliIFQAWeE1c2BwcG0h6imfGrkM198vwABG3pY25KPi5CyQa2VfGdxorVWFFg_y6LSHw5pLBp-CjKG7FgVz4cl6dzXZnghATHzqTLfWP5qIvsww7hBhFebg7VG5Kt3lehjF9Sie6VofjlCKvKG3if7jGRtNRFzZEa3RRvPlKLlb3yA6M5N-siZDxqOJu1-OH3eqBVZzgK1sEPmS3zEuq48ziIwiTb-vr5USmpedixKlFXyEXzabEti9R0yww3S22Vah__eL5fVzBMmorOvJfopfZtpgkPqKZRG06qnKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شوخی‌شوخی با مسی هم شوخی؟
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92017" target="_blank">📅 13:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92016">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjOSvizLwPlCdWa93OobU8LQH_NgEXJL8cvcTf_sKkJBcIn9rSs7yo0oGQCE0smfyhwi4tp2E8mOjOaoL4L7iZBDyoAZuV-t7-fifbZQ0CyFO6_69Dya6ULiPa8KpT1qXKbtYA88X_Q_MWBsU9C1hJBWQTQVs0wZIRydb42pZdeQG07oozehr8GMw34MF_2EbK-JNDAOjlGXteVOkikp7DcaZ_5QN_eP1i81o3A-x8HnQZqwNJD95-lINMcy7Sdx8-aukUYB86iilicT3XiyWEG56FMfSGNrp4RJq09UOEbjKJq8P36htN2zKYRVljxwxdDkOKdc1ibTh60jaOtMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
👀
مسی یا رونالدو؟
🚨
🚨
🗣
زلاتان ابراهیموویچ:
- آیا این بحث هنوز ادامه دارد؟ در سال ۲۰۲۲، مسی در را به روی همه بست
🥶
❓
خبرنگار: یکی را انتخاب کن
🚨
🚨
زلاتان ابراهیموویچ: زلاتان
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92016" target="_blank">📅 13:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92015">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxAtSm_08DHa-fz7ubGBSelZ8oyaspXa6EVRgjUP0QMjNIAVumHroa1-TsZtzPSbbiX09lFmThjcnd9an12G7l48LrfSimZhdKMgJd4-vMNyGuh17DljtcjD-smuQKUFld1h9-78ZW4anmg3ihSBd3F3kWnDYyqD_ChRd8b3sQHAh6fUyBh4f4pv5rhqmDeBvEQtOP0D60caI2MyQ-9CeUr_K5Q_MSBxCh9Pw27Z4QQ9KlxjsLCQptJWcfCA5lWXHtBk5b0MHG781c-jVfL6JnpWhPT-PxISbZRdd7BQyJtS-wThgEPjZBNAVlLhYBaTgD-UioAu-eefiaI_Jyu0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
شانس‌های‌اصلی کسب توپ‌طلا جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92015" target="_blank">📅 13:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92013">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bogyyPYpqejOtbb9eHLH2AGLVE4Vp3-j4oZ5I_l1ybhLXa85b0ubXBBpdE4uYQQgXDM55JR19t4Nwtm_uRLVnFjqvpL0nR_ALey5r5rs7QyauLvTjhU7yYwopqPYtXqHTKNTDcY9ydjpBWDei1V5fbbG2D-AfWcDxiY55QYv8W3tAIPXjbaEFGyEqSSp5rgBcnaJxK2wngIHj1-Ut6nUX3S9WGGYLde2RJh2Llnx0_yyGnPCUPnq-A-I3pExy1rr9v6Ug8Boe3oTmlcGZA_kgHEn7lBm4R2oKM-aZVPYwAczP6oiqntn2LKk7vrqoBqeTli4El_T4Q-tjriuHhh2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcJhZhhGw94h2mUXfEoC0EUxZufm156H_hoejB26c9dMknBf0C4vRbUUnb-FF1B5D1S4ddDuAJ-YNAiYPThzgH722IO7emcCm-qROElWs-3VIm5rgK1TJ9ojVTYD9OP9KP19__wl81n5wbi21i9y8WZyJ2Dl6eEwxUfZ0jEwq-32m83jhX4HEKHPtXC_vQXRNWsbEClZAGQwvcz7UMlQn_WknT-K4avegPevKbTmLU-vxG7_Ab1IjBtZu1Me53mCcCjkxmlGjB10cVZ5MZDDHA7hrki-atYY6rqaPIDtx11mg4iVcayp6aXiNa8MGwZ3fkFxPwR0x7RIT-qC5axelA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏅
🏅
🏅
نظمی گریپشی مهاجم آلبانیایی روبین کازان به ۳ تیم استقلال پرسپولیس تراکتور پیشنهاد شد.
روبین کازان با این عملکرد نچندان خوب ۲ میلیون گفته میخوام
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92013" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92012">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsTXxOoO8EOD_NcUiNLfIBySVu6ys564-ZAXnDGkcc820m9n8m-vpQbZn-5_MwbPs2-XftbWn_Tlub7a-KbPRozvvYaJbkQ8zNxas2wKzB6BAi2PlBebq74d3AlYdWcL1SAZMvhVe6cQcyUZKqMseEbM8G82pOENO6-8klI9haHQTd1lAwchxOjRdlWKhAGaM6cxUqQK7yymSACwzgDuDClIoTu7nft1fO6wkTvr89I8FHdpY8hl_QMU-S-wsYqm-ffxhMc3leUxvqrJ7_56bb7UeM4GNzmu1JD4eVDmfqqCTH5WiliG2cGEn0XDAHPMzgSmPa8dooxzGZToixILHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه بانوان برزیل و آمریکا:))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92012" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92011">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhJQBPLXy4gXpb7mW48i3RrnwEloYdBK_-_D_oKaqGCz78eQniEPl0_8vr-3YaOYgRwfJ6mt1qGjUD92CI14sWVfIljbRElUhUV2FJsb38xg5w9plAYhWMR5Vsi0o395usNYaWY1mCesBoSlPxzWpAlP6-ai17_K8IbBlbc3ugideoRghxrbe16_uk1PaKqq0W_g5uEekkgPt_fSTXn_d8pOlBJLJqvBZqr6Y6pSDjh9T62qjhnVO8w1TePtcuvS8Em4pABxVr-7ZGH0QFnDd8CMruWB-8VCUqcIaJHr2LsyAp1vPo9DDGuW8V8loD7rKyCZOEfLcV5Ek0DPT3mnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
🇩🇪
🔥
تصویر‌رسمی‌تیم‌ملی‌آلمان‌برای‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92011" target="_blank">📅 12:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92010">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔵
تاجرنیا مدیرعامل استقلال: پول یاسر‌آسانی فراهم شده و تا اوایل هفته بهش میدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92010" target="_blank">📅 12:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92009">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین ویدیو نسبت به تیم‌فوتبال ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92009" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92008">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92008" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92007">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92007" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92006">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAJfbQHjkm_QZxGVdgeRA_JNugjCqDCfntpVekY890xxWBOLP_oqaQKoFfS24UajWRCTYdtxsACfNRKn4Q4IvN7LiAkUzGbL8Cc_9M3E7dODkUZIwXKgoQ-9R8Fzw-c4RYomsc3_df5p56mVTcOjbQYxca1kLJ5FGpJ0tiTEA9SyYoRlWmGrdNmJYxRMfM-TdL47E7qQUoAG25dU5kNK7Gzv78HVNQxmJWHuBc2I1fFnLLGSiOOXwUYSwDVuLNMDo1s3uVQgS6ut1O9aaDCUN1Rp_Jt1LanW4mT65Ih3blsjw3_7GxzdRgZibnvm3dVxyRrOpZP4GsWTiHizAV7X9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇨🇴
خامس‌رودریگز
: چرا شما رسانه‌ها فکر می‌کنید کلمبیا شانس قهرمانی نداره؟ اتفاقا تیم ما ستاره‌های زیادی داره و باید مارو جدی بگیرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92006" target="_blank">📅 12:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92005">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b35afcdb3.mp4?token=eLUp-8BlvFk23XU3Kt5D5kWjx7lau3WG4Wy_qKS2Lp5Wty3BjeIJCCUIz_nCp0zMj8xZzP8Ca4GgfHig2LaC9f_sjIlt97AVR2RKiGtUwbAUYUVPP98dScn1re72REH5IHQBAkMbbntz9Zf8ehBU2gUVlwxy1lPXgfuNHOyQljFVSOLTDCP8gX_G4VJxR9RDj6_y4D-KUuTMvVikf5PCdHNesKFZXl5FNQwhsdaAwtKfMcihqwFIH_dFA5EIBTGF31AGiEOkMoJ_jE0xlsKyBja3KpgIlyofhS6FP9DdJFHF_5Na4Y71T9-UhtROP4TYd8A1ye78Id97XqwU-UAgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b35afcdb3.mp4?token=eLUp-8BlvFk23XU3Kt5D5kWjx7lau3WG4Wy_qKS2Lp5Wty3BjeIJCCUIz_nCp0zMj8xZzP8Ca4GgfHig2LaC9f_sjIlt97AVR2RKiGtUwbAUYUVPP98dScn1re72REH5IHQBAkMbbntz9Zf8ehBU2gUVlwxy1lPXgfuNHOyQljFVSOLTDCP8gX_G4VJxR9RDj6_y4D-KUuTMvVikf5PCdHNesKFZXl5FNQwhsdaAwtKfMcihqwFIH_dFA5EIBTGF31AGiEOkMoJ_jE0xlsKyBja3KpgIlyofhS6FP9DdJFHF_5Na4Y71T9-UhtROP4TYd8A1ye78Id97XqwU-UAgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
رایان‌سرلک بازیگر نوجوانان سینما: طرفدار پرسپولیس هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92005" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HAmxP1L30it1BdGRsbF7qqODHmU651McFwiqVy6FwEbPT9KSoKYWwTEtMccisqJ9tb_lQT9f_OPjeMF7gxa6oVxtgO2d6s-SzwF2KWhHlHAfQFUAMOT6Y709edpfSs87PJY45ks0wTT6si_l6ojmYGoOYtnWYw_8Z5IDtJoLJT7vQdj0Si7COZBIBY1pyVqvfed9QlnbnHJPnqLD0uPChxN__gnhke6SbChNBNnNvKOLfMiqCG-_-La0rc2YYRFdXBEr_VyU_yrd6oTh8HMir2zbfaau_a66uhP7pBOQofDRRvxlUCQErneeAykqzYXy9USUl5rgO1DDdS1LmhKMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇽
تصویری از استادیوم آزتکا درحال تدارک مراسم افتتاحیه جام‌جهانی که به وقت ایران از ساعت ۹ شب آغاز میشه و یه برنامه ۹۰ دقیقه‌ای قراره برگزار بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/92003" target="_blank">📅 12:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijQ_UuD8b1FKz4vJIwElsMGC5JT0viGXCrKM7qfNq5qY5Jw2k6zt46NRhQIeaJBjwntOfU5pRF-C-9JlTFbIHpm8z6XiGJB4Mdr2KIsisGdocUQtwezBBR_TInSOP3FIEpM_q9dEm9AqFCe5H2T2a95rgV_nPJFmNjiedbrNEPEIGBEKAU6Jds9568LB4c5yKKj9ZsbyJKuEjcMRptiuhz5dLeBDzaPpxxDkScsGe9oLzAG89Sa1_ADKrhfd5pV4cylKLZxS1biaWz5UxidGU3cxt7aZ1kpCJuH7IdKS5_E74NU8DEalr-lj_cHgIP4N2bm8dBQb4Mtt5Q36ucezNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇮🇷
🇪🇬
فیفا به‌صورت رسمی از مهمان افتخاری دیدار ایران و مصر که بازی نمادین حمایت از همجنسگرایان است، رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/92002" target="_blank">📅 12:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LQPJy-RqIzR7M1nh0SkB2GzRVlU7AQtCWR_HwlkY2UEY1XTJ7ZcpQXrXx15YhoQOUv6y-Dhq-Cmi3OY5AisVC5w70GgltwWEQkalZiZz9Jtc_LVTfz-p564OZrD-NOg15NpyVMrE6tXmaGJTLCIlWgtsA-k8py7BApHkyn3J2Qi81kh48PD-4hnFaN7v_F1rIYZh_SF1EzOFCVOkicAnrPC_yNtqAj-j8jahw-kOjSTXtkux_ljJ5t3xZEXZRnj0K2IzcEKO0YZQ6NCAAzZT9anELaQm2dfaEomz2LeMNRSOcNYCkPqsYziUOK12ZL0fuIt1RRIpHpQHXh3c24JztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
رونمایی‌فیفا از کفش‌طلا، توپ‌طلا و دستکش طلایی برترین‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/92001" target="_blank">📅 11:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab1767abe.mp4?token=i2wWbDT9KYRx-9hnpzr8q9TVaXzsrSl5XP2XvzxL04x2zFnw16YapZy6t-lLUmWrF9AR1f2msk80LtmSiA8MkUVOChgiqW2qppoVFlNjBCdjl9N4V60EXylu5EXHWHa-WoknVCi6EMRhwhxo8f-pwqMemIA5nmSK69XK5fZSIqT6rNs1hhO2w2zFlaxRvtfHBUIlOPAOSoN6kc11EDh0vk_U8OJ1mSdxv5NpmPvPkwa4RRguthIML19Cu0rXIW94MGnhj71GacAOl85FGL4p9vpMeCQtOP7W11SQWskU2aH0SRmCnp8rtkLt8em5qtMFrqZJfs9pY5q67xXB49_zqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab1767abe.mp4?token=i2wWbDT9KYRx-9hnpzr8q9TVaXzsrSl5XP2XvzxL04x2zFnw16YapZy6t-lLUmWrF9AR1f2msk80LtmSiA8MkUVOChgiqW2qppoVFlNjBCdjl9N4V60EXylu5EXHWHa-WoknVCi6EMRhwhxo8f-pwqMemIA5nmSK69XK5fZSIqT6rNs1hhO2w2zFlaxRvtfHBUIlOPAOSoN6kc11EDh0vk_U8OJ1mSdxv5NpmPvPkwa4RRguthIML19Cu0rXIW94MGnhj71GacAOl85FGL4p9vpMeCQtOP7W11SQWskU2aH0SRmCnp8rtkLt8em5qtMFrqZJfs9pY5q67xXB49_zqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هندی‌های دیوانه‌مسی دیروز اومدن قبل آغاز جام‌جهانی یه ماکت غول‌پیکر از لئو رو تو یکی از شهراشون نصب کردن
🐸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/92000" target="_blank">📅 11:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac930c836f.mp4?token=qooP_bHkDsHYNdsOhToruanjKAS8-VBmfpdS19Z_ZTkWI_LGSDkAluErgzb_UNBIlzKxYNgKifZg85ehE8K6WaAPckW-Ngogw7_KNrAIy2VLkrrEGZU1l9yv_Ilbtwit2nSGGw2HbBgWrWWLeW4oewnkaenjf29PHjCZ9dSPn-l5aa8M3bXGhNYLdb6f5ljZ8riTV_pxZFn4shWTxWA0LkLjMs5N41FyooUkL1H9RgHxng91tF4CDAlzA2DouLoG2xyorjyhCFoUn-Xfot5ma-qwzSHB9F5Rn5x3U8YeNkCscDJmxzERl8eU3DtzpD3lkCSJgwQGdcVntmaDSOSLtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac930c836f.mp4?token=qooP_bHkDsHYNdsOhToruanjKAS8-VBmfpdS19Z_ZTkWI_LGSDkAluErgzb_UNBIlzKxYNgKifZg85ehE8K6WaAPckW-Ngogw7_KNrAIy2VLkrrEGZU1l9yv_Ilbtwit2nSGGw2HbBgWrWWLeW4oewnkaenjf29PHjCZ9dSPn-l5aa8M3bXGhNYLdb6f5ljZ8riTV_pxZFn4shWTxWA0LkLjMs5N41FyooUkL1H9RgHxng91tF4CDAlzA2DouLoG2xyorjyhCFoUn-Xfot5ma-qwzSHB9F5Rn5x3U8YeNkCscDJmxzERl8eU3DtzpD3lkCSJgwQGdcVntmaDSOSLtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظارها به پایان رسید...
امروز افتتاحیه جام جهانی
🔥
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91999" target="_blank">📅 11:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJCZDnKppJTWeTBZJqttPdo8JeJGrT250u9izovetQNnEEQG1RAYYmC_g5PAh8NuEEEGHwx0I6sCEXjWlWDBowKII2fh8vVJNAXd8hsXc5B7lXvIboTo8k-7h1gQH327rpQNuSv2Ap5TYEqgxMw77NxvLzQS6bYVpYUxGIzyZnNo1WEFW5ochARtPXSY2AkNAQdb9a9u5t4d94NMNG9BDcY-soeqJNgPfN4F9jTeiw2W2dz0VhM0mTnqc4MpO53ij8LF1Jo9pwTq3BAM3R9by-8K-Wu5iRkP3f1QtLzOZqYH1aYszGtmkWoNyPaw7Xj1iulI1cdtOopq6oo8uyq-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال روز؛ آیا لامین‌یامال اسکینی پسنده؟
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91997" target="_blank">📅 11:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f7abba26.mp4?token=oeIOyPEdl-_hlhSpzOtJZ28bfU3cREeKIVNmQQ61GeQpqnlIag6Cv79882WvVApSb9QazvG73K-dIkz0Ke9JH9mMeE_SYtpDmdRJu1trJnkK0dFisOj18Nq6akjvTwnXQXHTbOJVtPsrXqXAdihajcDaKENAIUtzv-JlM6GA3nzUjg4VxiB9C5ajNp6jsLoZ0NSccvdyolEl_d-JxTFbOERuRTEYIn3Oi2jia1jVsc9iysXiLSNNqxDfwCv7dOTgaVGCCONuubO3wmAXaPMl5B1FuztgKWbHySQ3h7d1-4KdHYiRlR1DjGW2qnGc36a0o1-mGXE-SNpklaQWPp0irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f7abba26.mp4?token=oeIOyPEdl-_hlhSpzOtJZ28bfU3cREeKIVNmQQ61GeQpqnlIag6Cv79882WvVApSb9QazvG73K-dIkz0Ke9JH9mMeE_SYtpDmdRJu1trJnkK0dFisOj18Nq6akjvTwnXQXHTbOJVtPsrXqXAdihajcDaKENAIUtzv-JlM6GA3nzUjg4VxiB9C5ajNp6jsLoZ0NSccvdyolEl_d-JxTFbOERuRTEYIn3Oi2jia1jVsc9iysXiLSNNqxDfwCv7dOTgaVGCCONuubO3wmAXaPMl5B1FuztgKWbHySQ3h7d1-4KdHYiRlR1DjGW2qnGc36a0o1-mGXE-SNpklaQWPp0irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
تمجید ناصر الخلیفی از تعهد بینظیر انریکه به کارش در تیم‌فوتبال پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91996" target="_blank">📅 11:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینی رونالدو اما با کیت اشتباهی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91995" target="_blank">📅 10:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=rYPLCskh0bgS2DKFayDpL1EK9hVFRjMjkV2j9AuVbrrcP16SQ0Wf3V-F9G_7wWM0ZK4XwlYTcGxruV4u7SdSVjdobocx52-Tdd4N7dj3uZJwSEnP1ukzhomitMOfqWaKrLM605F3gF3wSzAaYYFj_u5USe48xcpfZQo_Gdq2zB5c3HXM7IIrLkO0xbIJ22LNsHRpue4MaCticZgwhM_RzlMoS5QMO6x6kKfvDHl_khseED3zDKhL7Wo88nU4_9o0RjKY4Jp_4XqH_xgldwZxdPMfC-0HjZOIfLAepFiSS4WKwWuNQTjm2O2uivJRr2nBYTKutWvMUq55X4CZ1ve6Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=rYPLCskh0bgS2DKFayDpL1EK9hVFRjMjkV2j9AuVbrrcP16SQ0Wf3V-F9G_7wWM0ZK4XwlYTcGxruV4u7SdSVjdobocx52-Tdd4N7dj3uZJwSEnP1ukzhomitMOfqWaKrLM605F3gF3wSzAaYYFj_u5USe48xcpfZQo_Gdq2zB5c3HXM7IIrLkO0xbIJ22LNsHRpue4MaCticZgwhM_RzlMoS5QMO6x6kKfvDHl_khseED3zDKhL7Wo88nU4_9o0RjKY4Jp_4XqH_xgldwZxdPMfC-0HjZOIfLAepFiSS4WKwWuNQTjm2O2uivJRr2nBYTKutWvMUq55X4CZ1ve6Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رفیقم یه دست شانسی منو تو (Fifa/Pes) میبره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91994" target="_blank">📅 10:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=vCVd6dMoKiOcYwqz2oRKbhwS2ny0qzdafKNjMmnCECppn88inglt8OzYG3TQ5C6d4HyEdpX1Yzz_iQeI9qDWMWaAGZJ_y331dhu1ixDxwzRmJt2qK0VeyJyIQM-w83Au2rdBu8owgKLYT-GzjJyq8IMUcsNYXfkMrfb3w4BOxrW3pyTLehW_12Fhcw4DO4bOOiE6-ucqZ366U5mHToEcknfJcBuclhvZYUHu-j5IYQW7qjSCbabTBwYDjhFwCCj4xFoqLCQaED60Jy-F8UIgNfEijeullWdxvjR_7JP-A9eu-EzUpxhTjbOAiGlZ-5VkQ7yIE9-liKcYSiNw4REwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=vCVd6dMoKiOcYwqz2oRKbhwS2ny0qzdafKNjMmnCECppn88inglt8OzYG3TQ5C6d4HyEdpX1Yzz_iQeI9qDWMWaAGZJ_y331dhu1ixDxwzRmJt2qK0VeyJyIQM-w83Au2rdBu8owgKLYT-GzjJyq8IMUcsNYXfkMrfb3w4BOxrW3pyTLehW_12Fhcw4DO4bOOiE6-ucqZ366U5mHToEcknfJcBuclhvZYUHu-j5IYQW7qjSCbabTBwYDjhFwCCj4xFoqLCQaED60Jy-F8UIgNfEijeullWdxvjR_7JP-A9eu-EzUpxhTjbOAiGlZ-5VkQ7yIE9-liKcYSiNw4REwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از مقایسه نحوه استقبال دو کشور آمریکا و مکزیک از تیم‌های حاضر در جام جهانی حسابی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91993" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVadnQC6IbBlgNN66kbK3qcLXq6qH7SdduRVWNcjRjlPzwr3XjdqCUhHt5-t9XproC_Lgx5RNTMKQuFF95YRX_88PjT0moZ9EmDPr__g23YZoUmFFqP2UgoSDzBh5xo9NzudAUQok-vi1N7nSxpGRRYHCszEar3kOz4GDRffCDJL-ATAhQygO3jNg2jQ3UT9DaNxIBk67iy96e41TCOPmOdobx5kKIuJoKaOSFqFNbOM72PR9auCMWEsnCC-ht7Rdlt0XGN2T-9DXxY8iOLBbpD75Zp1r6qv01Ud3cL9_Zx6JWzw7e6ADNSC2jERSE_VoIPcp8gnl2b-JNYgSs2RTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
امیلیانو مارتینز درباره افسانه مسی:
"اگر الان بازنشسته شوم، وظیفه‌ام را انجام داده‌ام چون به بهترین بازیکن تاریخ، لیونل مسی، کمک کردم تا فوتبال را به پایان برساند".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91992" target="_blank">📅 10:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=GiT1RpxxWul48v-jDaklmMcEnpCCRyDTJEjVg_NhLyzjpYIbCQb6KdvNwhpa1LId3pGS79_5lL_QiDaZAguen3Ww19OiLvnlPIVse7pnn1yGK7d6ba2cPPF9iGbBfdN82QrSIBSu96LPhZXqP0JHv6ZTdXWDVoiJ0o9kqVDeQymU43e1i0n7PAR_mtnbdMLf1QvzF8kUFP1wzi4ANbrpQ7NiF9Fb82IlziPn4MfqN_Y06KV_Q1V7NemUpnYG-YuW88ZB05_-u16x--obKYE5nOheCdA3-_TgOl3FFG5vCTONSwR0g0rdoyvhKE0B46QfpI7m05LyNeGwc_kyrknigA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=GiT1RpxxWul48v-jDaklmMcEnpCCRyDTJEjVg_NhLyzjpYIbCQb6KdvNwhpa1LId3pGS79_5lL_QiDaZAguen3Ww19OiLvnlPIVse7pnn1yGK7d6ba2cPPF9iGbBfdN82QrSIBSu96LPhZXqP0JHv6ZTdXWDVoiJ0o9kqVDeQymU43e1i0n7PAR_mtnbdMLf1QvzF8kUFP1wzi4ANbrpQ7NiF9Fb82IlziPn4MfqN_Y06KV_Q1V7NemUpnYG-YuW88ZB05_-u16x--obKYE5nOheCdA3-_TgOl3FFG5vCTONSwR0g0rdoyvhKE0B46QfpI7m05LyNeGwc_kyrknigA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهار فرصت‌سوزی باورنکردنی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91991" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91990">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Cherki Core
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91990" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=qjCR2km9HLTbPUp-_U--gfPKvl1_wHIcAZgGA5XtFJs8l7XwoLVn_TPJrPzHpUYGxzCmy6_zJiRnJai9lgLPZlW1pM14N3uu47w60nu26-Rs-hzuf1W0rgaFvIfYHRoysmqfaOAF-vU7cmVvaKoi-476P8sk7kmxwlkqV-X3crxbUbkGs6OOCURsgS_rqhFxJP6US9TNDU8drsz-fdUgoFhsn3xYHgTtrU7pFQ0Kr5AZtCafayZZqL794bAZKsC4tm2FJZphXJ4qIDUwniSXBtS9eBRxrXlaAr1MDyeSTmvh00id6z8okMRhFsWT83BkpZX_z5W8fXpfks5utOZpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=qjCR2km9HLTbPUp-_U--gfPKvl1_wHIcAZgGA5XtFJs8l7XwoLVn_TPJrPzHpUYGxzCmy6_zJiRnJai9lgLPZlW1pM14N3uu47w60nu26-Rs-hzuf1W0rgaFvIfYHRoysmqfaOAF-vU7cmVvaKoi-476P8sk7kmxwlkqV-X3crxbUbkGs6OOCURsgS_rqhFxJP6US9TNDU8drsz-fdUgoFhsn3xYHgTtrU7pFQ0Kr5AZtCafayZZqL794bAZKsC4tm2FJZphXJ4qIDUwniSXBtS9eBRxrXlaAr1MDyeSTmvh00id6z8okMRhFsWT83BkpZX_z5W8fXpfks5utOZpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
خبرنگار: چه پیغامی برای مردم آرژانتین داری؟
لیونل مسی: «هیچی، راستش فکر می‌کنم مثل همیشه، هر وقت که یه تورنمنت رسمی شروع میشه، مخصوصاً وقتی پای جام جهانی وسط باشه، آدم خیلی هیجان‌زده و امیدوار میشه. قبلاً هم گفتم، این تیم هیچ‌وقت کم نمیذاره و پا پس نمیکشه. طول این سال هم نشون دادیم که فرقی نمیکنه جلو چه تیمی بازی کنیم یا تو چه رقابتی باشیم، تا آخرش میجنگیم.
این تیم هنوزم با همون انگیزه و امید قبلی داره جلو میره و همه دلشون می‌خواد تو زمین رقابت کنن و برنده باشن. ما یه تیم برنده داریم که همیشه بیشتر از اینا رو می‌خواد. خلاصه که مثل همیشه بازی به بازی جلو میریم، ولی با کلی انگیزه، امید و این باور که می‌تونیم موفق بشیم.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91989" target="_blank">📅 09:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9iA8cAWEgJdwWOdN_RHddN-Vn_c9k2wK9CbKc_THI1DxM3SuKhAKxWVN-j3QMBZhgXiYpZSge3LQKiggd-SXQ8_mjInAzd6GaQeXpDviQ01GioX3qvGZrTZ9SAGkA_cZkp9DX7px5ZM4IsnJXZy6ElqRS46ouWlJQrG4oa-0hd0v76-JFBJncXZF4wo2zbfvpIt8Ut4fynOOoKsrq1hKZFFXMlGSaRcYtZ1gjaL0jnmiWwElOXOITIalmSmBkpNC_jUMieET_N-EIfmVRkBJ-ZqbE0dknoteIXP2P2CF9hxe8hSDfWi_DACs5jibV7xhhr7JJN3wR8-5i_3tCEGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل جام‌جهانی در مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91988" target="_blank">📅 09:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91985">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyPyeNZxByEo6s8-IqxOtQ0btwIzJk8q0pDyDwNpWsWsXbKN7L13pDQMgA1L610zP1JZ2w69JpfKxDp_-_aWnJBSZ2PEnXlGam8S1_-vnyMvbILxPmE5HeKJ4VYmeRsOQ5nf-G4zVT-h7TBUFezC8cFBSu9CN6-MmwtGGzlAvf2msEZlf8XwbiEsgmyLGC4gsxdLe8GA5Tb2kHET8O7XAD0yDPuYXLeLr6tInlaGLkm9bRIzA41oboL5WUfV0RGhSqvGmd1pxBByEkl0FUI0ZYvMnZUGTD-arv7qM79QFKGKVfR3-evCK5ReHMAAd0l_5vkbCLUpQtEkC3GMY7tcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uySVAT7LPhJamjBZUgbDBCmunCWtADtWAaaaWsLPfk_2rf_CU9uAYIs5cHSMm0Jd8TCc6JswnnoNe3ANwAJ32tYHsx5rJTGEGjJYkRAISyO5t5n8Jwk-WN8KSvK0Ybw-IUrikTEkgHJb8T62oogeIE7F22KMrCtWWEfhqqC7IJRlq-IzqPH7e0Fg41eiRprVQtOJxKIBa1yG_ZDvptsvz_vZTfDv1YRxCVtUUiNqF5AL54S-yMaPQ9bp-kynq4z0AO-chQ5Zv4FYIzKVRgJ7DK3QGjJ-FhXJLRMUiLXlc5uq0elFHs5xBJ8PeEO2IUWVYKsC03uWMzVCsu3K4wN0Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛ آغاز حملات موشکی سپاه پاسداران از شهر های مختلف ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91985" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91984">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=QvQ8tcr6MCQqAAuXuV6EG5uUlLIAFPv8qw91IEIW39WqHEvvXjAqHmsU6C80_t0I3MW28t4-XER1DT6IDpqc1i0v4Y0KUy8VnUDYsI9Al7VLLxVxs-bV5eP1VyPmIr03fugIscXCLkph3ljKUxPOIDBpPQbj99Eh_k6YH5zIP7HBgDH95hPD0TMDWhyggn0n93Dp1D2ARbndi5oFugj2u8nHQjkx91QfT53l9TzCt83BZuEYq6Qb2NPeD0aUfKI9FQMGvxVhdae3nLePHcxlZozVpa6Yp8fqwqrdC11lz4G7es61dWuchBLQpHbUiZIJgC5WCQcvlJ0_1ACKAtE0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=QvQ8tcr6MCQqAAuXuV6EG5uUlLIAFPv8qw91IEIW39WqHEvvXjAqHmsU6C80_t0I3MW28t4-XER1DT6IDpqc1i0v4Y0KUy8VnUDYsI9Al7VLLxVxs-bV5eP1VyPmIr03fugIscXCLkph3ljKUxPOIDBpPQbj99Eh_k6YH5zIP7HBgDH95hPD0TMDWhyggn0n93Dp1D2ARbndi5oFugj2u8nHQjkx91QfT53l9TzCt83BZuEYq6Qb2NPeD0aUfKI9FQMGvxVhdae3nLePHcxlZozVpa6Yp8fqwqrdC11lz4G7es61dWuchBLQpHbUiZIJgC5WCQcvlJ0_1ACKAtE0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سنتکام: به دستور رئیس‌جمهور ترامپ، دور جدید حملاتمون به چند هدف تو ایران انجام شد و درحال حاضر عملیاتمون به اتمام رسید ولی همچنان در حالت آماده باش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/91984" target="_blank">📅 04:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91983">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏐
🔻
پایان ست سوم دیدار ایران و برزیل:
🇮🇷
ایران : 15
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91983" target="_blank">📅 04:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91982">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🇺🇸
فوووری از سنتکام :
عملیات های امشب تمومه و کارمون رو انجام دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91982" target="_blank">📅 04:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91981">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:   تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91981" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7DSu8PE1UHFuLvCn3jMbRyancKk-Couoo9e8Lcgy-eqacg5dFz9rlamvQcI38dHlpnW9s8bG3QJLw4KTZLUAwt4vCM8XkAJoClLsTngeT5vOzY0Wq-JQ3oqXsecwk7MCURg0DIsl0N9yNlTo55vA4clm7EXnjZqV-2s_cVzue8cg1VznW_8G-_TpWdy2RC0zDEDeWtgeb_zeUQkZWdiRgJZ_KJBHwQKqecfdbTKJdWl9AZ7M6PCU6bAo7_GKMaPw-WpWHLedb__hLhPr2BhDOY6XP3tJsdHj0lCYTHNHmhmo6KGDMiXMN5cc1GMUjRRY73wS4_tfWiHgNBOdans9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:
تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91979" target="_blank">📅 04:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993f547a79.mp4?token=plYDBr37sZnwCd4ZdXMXcI663Fq9FSLvI8dX57bNyOjBtzVwy0u-Rq6-M3KlOpWstiGnvW_VhtpHjNF36HIt8YYFXk8AVVcAjXK-zhFz-oijhm1vVYHngjo_HaptzoSHiSiM9ixUe4JlpK9QeQl1kyTJw6TvZBTihgEGC1EL8cS_3AEUPmOk2B77iGBf3v48QCCmgIPuPKmr9yjpPHbU3mB9EbvPlMJX2MLriyAQK-yNStE2Frj5IEIwEohc6SPotVF8O5SGf_8wmRcmTYDocPGgHHMK9uHd0ah_zFRVn31g_da2x43bU8zP3e_nrdOAvQMWNzqm3ZvE4SLZt-NstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993f547a79.mp4?token=plYDBr37sZnwCd4ZdXMXcI663Fq9FSLvI8dX57bNyOjBtzVwy0u-Rq6-M3KlOpWstiGnvW_VhtpHjNF36HIt8YYFXk8AVVcAjXK-zhFz-oijhm1vVYHngjo_HaptzoSHiSiM9ixUe4JlpK9QeQl1kyTJw6TvZBTihgEGC1EL8cS_3AEUPmOk2B77iGBf3v48QCCmgIPuPKmr9yjpPHbU3mB9EbvPlMJX2MLriyAQK-yNStE2Frj5IEIwEohc6SPotVF8O5SGf_8wmRcmTYDocPGgHHMK9uHd0ah_zFRVn31g_da2x43bU8zP3e_nrdOAvQMWNzqm3ZvE4SLZt-NstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در کرج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91978" target="_blank">📅 04:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9b5my7tfZrKlsb7aWuLhy08HynivJu111XW3QFXPcrXZs6qV5oO0qOagfZj8dnQng6yiTeb3S8iicBbdyMgOdTC9cIO_zkt1gG7UoW2Tc8-DygDcIjDW7BRpwOvT5H9W-U6SWu-iboc4PUFJqxLsTa430J-cvu-iJ9HdYmE1i2Y6zhHkXP0CyHpDL2F-3oNeLA0rWuDiZspXBuG1Bw9cokdOUYiHYonHwNBoydv_oKNFKO-gIAHhFW4iGhSwoS6711MAbgsafYRtTKTrTlCv7zBfJ0o7M3GaSjc2x_PT_n1KxjymAPnnDgya0h3-SuydUbcwLUss6b5JqJekBzd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqj_wRHfAlgfT0R__1NNeeKrz1g2iZZCjuqoXzk1AqtogM4OgKHERse87HmueL9eP-U5FhXVxn1xSYY1L09FOA09onWpjYqH2GuTtfv_ozbL_UBKWdzuhRMutPE2yiHAvDEs_ZAHWz1MRObrhcsibSAwhdGniFRj1BwihOQouxPF7ZZKvGE3S9BsaqDTf7EL_nvYNookk8ldi-yZj112QFiBwPIaRxFM0MkXxroBgYNjMHnGSqoS07n3B8MfCItrwFEVkeOz7Q8y9CCMu6aYYuGNYFbbBzrWqwkwOa5aOUl-OxtfiYeWFjzF4TPoDVPHxtSsIinConKpL1ap0BynUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqIYrJX3hHuMi7VxmIDyf5LRx0-0FGAkUQK55TGX5yQ7Gtdoe061ig54_cdx9m310it8WUkaWYunobNw6IZ1grwv6ksT5FMvPam97WexmpZ3ncgE_4KpY33fGT_L0ko7CArLVuDGSmFN94OPlgZAeygkzWGebhFN9LDw-bpAFHRU6DKrqpJPlEjQ5P6IyVPdphxuTQVH6rs6PSLlhIDxwpIFX-YjldwQtg060fEHyve-8WlY8DYK-odR9tQDVTPPPgGTrlYhe8zPkg_26miaXH4bC3P8Gl02yDrD2MR-Pqv-wu4k_mZIE0AXA25-epqoUChf2B2jKAS2726iB0-m_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش مناطقی از کرج هدف حمله قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91975" target="_blank">📅 04:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏐
🔻
پایان ست دوم دیدار ایران و برزیل:
🇮🇷
ایران : 25
🇧🇷
برزیل : 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91974" target="_blank">📅 04:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران : 21
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91973" target="_blank">📅 03:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=O9r58HAkXsE4oEBJPxuj2pOqvvD2mLQhiBr6cyp1c6-ppvMx1Zi6yrZxwMgqblanXgayU11Getlq5klPgOrSpDxuc1KIHMb6ed3T4G6RNKSGkSbpInk_mQLlDORbA-X1nMHKR9bM_bpJn48q025vUsv-4hOG1dMsuem2cOpB4z9LWHmwgR6h6Uu2J6A0dtu3EINp0j2YEYxiV5aHG-pWzOKqzykNvzN2cicHoRebMN0vT35MfxdkljRDbhvu3bhcR_79603Y6R_g736j8Wl3t8i1UJ5K0KpFZxDlRkqpqE77HPAfOYLx29Hu92_Nx7ydPOumCRnnTeO0yQuclG4qDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=O9r58HAkXsE4oEBJPxuj2pOqvvD2mLQhiBr6cyp1c6-ppvMx1Zi6yrZxwMgqblanXgayU11Getlq5klPgOrSpDxuc1KIHMb6ed3T4G6RNKSGkSbpInk_mQLlDORbA-X1nMHKR9bM_bpJn48q025vUsv-4hOG1dMsuem2cOpB4z9LWHmwgR6h6Uu2J6A0dtu3EINp0j2YEYxiV5aHG-pWzOKqzykNvzN2cicHoRebMN0vT35MfxdkljRDbhvu3bhcR_79603Y6R_g736j8Wl3t8i1UJ5K0KpFZxDlRkqpqE77HPAfOYLx29Hu92_Nx7ydPOumCRnnTeO0yQuclG4qDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
کارشناس فاکس نیوز:
اگر ایرانی‌ها توافقی را که مذاکره‌کنندگان آمریکایی ارائه کرده‌اند امضا نکنند، چه اتفاقی خواهد افتاد؟
🇺🇸
ترامپ:
فردا شب حسابی بمبارانشان خواهیم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91972" target="_blank">📅 03:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91971">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران
:
21
🇧🇷
برزیل
:
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91971" target="_blank">📅 03:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
بمباران بزودی متوقف خواهد شد و مستقیما با مسئولین ایرانی صحبت کردم.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91970" target="_blank">📅 02:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⭕️
🇵🇰
پاکستان:
میانجی‌گری ما میان جمهوری اسلامی و آمریکا به‌پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/91969" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری؛ قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91968" target="_blank">📅 02:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwC19WMnoNIfQXIRVlRa9RBdoIVkAYIsooTycHvsV5mm7I2AByiVhuEpeQoP_DKw_UJPfwbojP7_5u_oeqEbNn3szhhpKoXb9sKHLrhlRr6lYfo4v_MmbplmwFZIS7gHmvf7W3F9QibUlVfjzynb_guO3NS8t8PmDAeXs8A1APVw8bS-a5VNWYTVWWEpsp3Eujb_Rsz_LGCrwNzs0P7zskvUV59oCnrMl4Lw3GY1pZq2ZY9taS8P586NKf3P5W9YEMhK1JOpXwx_OyGFe5duCaIQfsi2o6-L_fAbHXzckZeJdwiH0pEx-vVoGMyCqC-CH7lyoHJsru7pvh2fxiEUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
صداوسیما: تنگه هرمز مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91967" target="_blank">📅 02:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری
؛
قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔸
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91966" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc_o_i-djTKjaHn5V2_v6yrWQD5QYyLApu1BvMe9UGH7wh9Xd7m5wOsbflIkYCIZk-Q9BERiIlXAiMbWS9Y94poiN_f4ogMqiiWOma0RTOXUoGEyzUmF0Yn_q-HQldotPoD_1nne70QBkNU1HC26wzVVZ1PMD8tGJmmUspOmmA-d5fix-Qeiqz_TriO2ntB0smdFAXg80A4p2VzqKZgUwCo40U_R5xgM06tCwBpq8OPTxtsKjNcpkfP8eCyspi-YRXnVpprXGCrYOfyPRGTChSdKgiIKdpOrRMFF4pvgMfcDH76F62X7fDsxbxTrTije7uLRZFHjJ-MkwR8y0nAMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورررررررری
؛
پرواز دو سوخترسان آمریکایی در نزدیکی مرز های آبی و خاکی کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91965" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انگلیس یکی زد به کاستاریکا   عشقم گوردون پاسگل داد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91964" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
روابط عمومی سپاه به خبرگزاری صداوسیما:درپی تجاوز جنگنده F۱۶ به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91963" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری؛ فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91962" target="_blank">📅 02:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری
؛
فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91961" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91960">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYTc086qpaBg3uypK9hsPlF3MVe7YBQclyBG6E2wH1gz_etylhWCyKstisXGRBeEBIyQL7jHFQuny9bPFIyRWqeTrmD7v8G7R-c7jXmtyy0fL5aNAzZ1pbe618LqxK2p8w_0BTzSr1cdQPdYD5Xhznx3Oqnk9X5VGwgvCzufr_mvOsU2mMxSHAyCzfvi43lxb7v4vH18RxONWQ4Cf49g34OVEeWVNUY_Bf4E2G_4jKyZSd0DmKMITF6vlcLfnaFtAqPFO_njda-REwCbSooRjwWPgfZiXCHECF4NPm5cnielgJsPE-JJXpz9mAMFA6ocO-ZecCgd0SPC4gSxUzhTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
شیراز وضعیت یه پمپ بنزین بعد از خبر اینکه به عسلویه رو زدن شلوغ شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91960" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91959">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
لحظاتی دیگر تا سخنرانی دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91959" target="_blank">📅 01:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇮🇱
⭕️
مقام‌ارشد اسرائیل: در حملات امشب‌ به ایران تا این لحظه حضور نداشته‌ایم و در صورت نیاز اقدام‌فوری انجام خواهيم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91958" target="_blank">📅 01:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#فوووووووری؛ صابرین‌نیوز رسانه سپاه: الله اکبر. یه ناو آمریکایی رو با موشک زدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91957" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ برخی منابع خبری از حمله به پتروشیمی کنگان و‌ عسلویه خبر دادند. امیدواریم تکذیب بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91956" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
صابرین‌نیوز رسانه سپاه: اختلالی در اینترنت بین‌الملل دیده نمیشه و وضعیت پایداره. نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/91955" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
