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
<img src="https://cdn4.telesco.pe/file/JI9FzIr-8Vmh9ACDwmBaOWxaVxmjYLmuTwAlJGyk1e4kYnuNgCxPMD628W1I4O12_UklTbV3aXMwllqF5zBuWOqYCxpIGubDK2bIhx-zvX8-3zz0qpyPp3pYuPpvZz10i9WJvLoCI_xPD60XIp2btMaXli7O1T4FY7Ax6HUSkrEw621PvIdDPWM5FqKw81STcUikf3LugpUrD-NYIWtjme7HvZ086pubjhiZhCzaz1CxLGNZqxf9uyoTNLfxVTwZwz6PtpYFHn1tbasOZCq9sETnaa26zhuwp20pcnn0-tLcxNmznlLRlDFd9J9YSCQ4fIYxQMepk0vQnLDSGfY-ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 23:31:05</div>
<hr>

<div class="tg-post" id="msg-439094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این عاقبت بی‌وطن‌هاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/439094" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
نوجوانان مشهدی سنگربانان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/farsna/439092" target="_blank">📅 23:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
بروجردی‌ها: مسئولان بسم‌الله حمایت از حزب‌الله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/439091" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خلاصه جلسه 1</div>
  <div class="tg-doc-extra">Ostad Khamenei - استاد خامنه ای</div>
</div>
<a href="https://t.me/farsna/439090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
جلسهٔ اول اندیشه اسلام از زبان رهبر شهید
🔹
این صوت، خلاصه‌ای از اولین جلسهٔ سخنرانی رهبر شهید انقلاب در سال ۱۳۵۳ دربارهٔ طرح کلی اندیشهٔ اسلام در قرآن است.
🔹
هر روز یک قسمت از این جلسات به همراه متن خلاصه در فارس معارف منتشر خواهد شد.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/439090" target="_blank">📅 22:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برترین‌های ورزش ایران در سال ۱۴۰۴ معرفی شدند
🔹
بانوی ورزش ایران: زهرا کیانی
🔸
آقای ورزش ایران: امیرحسین زارع
🔹
بهترین فدراسیون ورزشی: فدراسیون کشتی
🔸
بهترین تیم سال: تیم ملی فوتسال
🔹
سرمربی سال ورزش: پژمان درستکار، سرمربی تیم ملی کشتی آزاد
🔸
زننده گل سال: مهدی طارمی
🔹
قهرمان فردای ایران: مبینا نعمت‌زاده
🔸
بانوی پارالمپیک ایران: هاجر صفرزاده
🔹
آقای پارالمپیک ایران: علی‌اکبر غریب‌شاهی
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/439089" target="_blank">📅 22:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439086">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFGORqXHaGDaVy37VkAeLKUKVH8GKnIPxpSB4IfcuenLnK-yKuh5ymjWAtChmop6nDAFfLK0FguTlsKsJGCmEf9vPaS6z8FaLgNgH7UlUqF9yprMnPIaVVW6emL_3ugEVdUUUWNCi8zXYCcOBjPtOBrd_AyEhnMtI5zSG5IVHeBfiz5-gX0ZFeV4Rev6AaJaMBl0yFwAXxiPf4Sg1LSck1iZYVTCURohcB6idv4scp0alve528bVbqs2kLlkUdZ_eS1UPCVmlZNMEA91l4ogfNWC7ZWP5O88JCkTuMgHO72lJEH1R3okHMY77bd8gIi4o_GUEaQ2SPY3Rt0jn7wBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwPdARTuOSaaZlW6ZflZSdpo0tocwXQpSbpHsaCqx4aFOB0VYOIDihK-8U1-D3HLkDEWzkI97_9lxonS-CAK5w_CrNe_lc_S0nNlbo1l3sLJjSMVE3NT6EmWM2VF7uw55ujDsI_u1xuuHJEkGuK0sZ37Z7aaVCboVruWFZKvX3pFwfE-0ZgGVgcwhS2HmdtZE7t3zId8z6hCeCierksQNaXdsbG3e8kKaaIVtCbEmJIpncAg0iTYSlGVeKcdhSoaPlZwuJU1v82s8NE1ah3izHfGkxBo5oePUpG_kgZ5_167FXFZeqKjE8A9IJGRph3iMk76-BgwUY3ZIHsF6GcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWpuKHB6Khj7CtY9k6yGLbv-h7QYnnbpxGBV1SRJ93f1sGV3lssDXwATVBVajtHN66Og6nkyedFH1rIAzeDQAte7YYb4dMlSfQEBdySpZ2VhVDX-9xggBX764BGsJGRoU_JyiCusj-6lyzcZs2SdIcpMqztueWkxPQGrpSylsh6gEJPrpTUZ7T49d4O2y8IKnIRaYMX2x_Xvgt710Uq_ZbrdVUyBgJ6GPQiT3auKykRwxrrcmETL__FLjjC5gUe_ke10JDpW7IVY8CBlOeQ-PFgsfpSLOdXOLjmych3t7hFPQqq9ZwG8-LrGNwDXqrbeJybOJHiR4ky_hZd2w5W-Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: روند را با قدرت و با صلابت تا جایی که جان در بدن داریم ادامه خواهیم داد
🔹
یا با قدرت مدیریت را ادامه می‌دهیم یا شهید می‌شویم؛ جان ما که از رهبر شهیدمان بالاتر نیست. @Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/439086" target="_blank">📅 22:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها ۹۲ شب در خط مقدم خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/439085" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439084">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
حزب‌الله: ‌۲ خودروی هامر ارتش دشمن اسرائیلی در اطراف قلعۀ تاریخی الشقیف در جنوب لبنان با پهپادهای ابابیل مورد اصابت قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/439084" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439083">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«امیرحسین زارع» آقای ورزش ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/439083" target="_blank">📅 22:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439082">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهروز رهبری‌فر، بازیکن سابق پرسپولیس: من خودم را فرزند شهید می‌دانم؛ چون پدرمان امام خامنه‌ای را از دست دادیم
🔹
۳ ماه است مردم هرشب به خیابان می‌آیند و نشان دادند که همه‌شان تختی و پوریای ولی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/439082" target="_blank">📅 22:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرمانده‌ای که‌‌ از جنگ ۳۳ روزه کابوس اسرائیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/439081" target="_blank">📅 21:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439080">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زهرا کیانی، بانوی ورزش ایران در سال ۱۴۰۴: عنوان خودم را تقدیم می‌کنم به دختران شهید مدرسهٔ میناب و خانواده‌های داغدارشان.
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/439080" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439079">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebEo7XCvdoZEgrK_juh3JspjU0im10_lFXGNEMgGnjbPcEtkfJ5R_iI8JCY88RnY9odBlnfEwTD3q7kdJoNqjBhBzQ-x2qTKq8Nny4Cmq7kiouZOhZrO-xkdtYUhjYlcvJqqOIt4Lwq6fd7gV7SWAiV4SgNl3lTOKhBF9gQBAIKJxnK28Qy48egYkMe-zGPM2fiy32fs_cX5DmfZXw4Wf83zLIE_JaTXN2nv8EIOx-6h4gI7QzschD_kCbrhduNEkNgfCV2pbx4pLpsQcVFRuGyekMM7dklO6Vi6rmn6Ti-E5RF1JO-p5f-KO6wmDsONhMFNmVi9IcsaRcjQHtaBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: در جنگ رمضان به فناوری‌ای دست‌پیداکردیم که حدود ۲۱۰ پرندۀ دشمن را هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/439079" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439078">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پژمان درستکار، سرمربی تیم ملی کشتی آزاد: اگر ما اینجا ایستادیم و پرچم و خاک ایران استوار است دلیلش رشادت‌های شهدا و مدافعان میهن است.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/439078" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439077">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هاشمی‌طبا: تمام سال‌های خدمتم در برابر یک لحظه فداکاری رزمندگان ما بسیار ناچیز است.
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439077" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439076">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6AxmUycal2TBhvn1KnFcrFqbMw66m57Jvk8WmpwAnRAPoXRvAwJ5SZ3BqqY2gmj4cHciTK4xCxcgiTTfQlkEK5VIyyW-qp16YBGBPuSkEzl6Kk-ZtfOQN88axNPu_GMdcXeqSGIK5ypGGGr_Yz1HJSuIh_6yhQiYekYUSKWMYbfQpFZq3cuTn0h2ocRge-kYASnXfz7XoI6m6l0uFApkYBwJl4-_uLao4UlfIpS5_tmzggsgdrId0bH02cNobUHhdgE7lNEGxhhmhOexdZwkWhIZfsRvQlc50Xs5dBQD0hJvvX8P8utkeYLjn4V_qKzjWN-aiYTRwsmYANbBl0D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: مصرف برق ۱۰ تا ۱۵ درصد کاهش یافته است
🔹
با وجود اینکه با توجه به شرایط موجود باید انتظار افزایش مصرف را داشته باشیم، در حال حاضر کاهش ۱۰ تا ۱۵ درصدی مصرف را مشاهده می‌کنیم.
🔹
مردم در مدیریت مصرف همراهی خوبی داشته‌اند و این همکاری در کاهش میزان مصرف کاملاً مشهود است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/439076" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439075">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: به آقای پزشکیان می‌گویم از وقتی شما رئیس‌جمهور شدید دیگر کسی به ما گیر نمی‌دهد که چرا کت‌وشلوار نمی‌پوشید
🔹
دیروز هم که رئیس‌جمهور کت را درآورد و آستین کوتاه پوشید و ما راحت‌تر شدیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/439075" target="_blank">📅 21:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439074">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست. @Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/439074" target="_blank">📅 21:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439073">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌  فدراسیون فوتبال: شایعۀ رد درخواست ویزای بازیکنان تیم ملی برای جام جهانی ۲۰۲۶ کذب است
🔹
فرایند اداری مربوط به دریافت ویزا طبق روال انجام گرفته. @Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439073" target="_blank">📅 21:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439072">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qV_8fBmIF1ZosPLPbS-zvjwIk4kyQqgxtpT4drb6byArdW9AMus8oPCu4yLDsfm_kmKpzP1mEHjAXV_4Ax2IUUnaFJgg2vY4BqBdk2-Dm6LG6gJ7KzS1RMDI1T_qbz4FhI6T-sdedxrs3rdplAzLnXC_2o0GyhU28uDyNBHyl1FYaL6URclK7kQQLmXuugB5bnMsAwS9ZxfBe6qDyirSx6c4p1qDNQhLNbkd8VzLJsE84VuRC8N5NTgg34xGrQ4b6C9cDwn-BlkscQh8P0UvRRMPL_gqsXbTAt_DCskiSy0EF40eRtCdz9RODqvvbTRPwuKhKeYPcxhQLTc97S-Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/439072" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زخمی شدن چند صهیونیست در عملیات ضد اسرائیلی در کرانهٔ باختری
🔹
روزنامه معاریو: در این عملیات ۴ صهیونیست زخمی شده و وضعیت دو نفر از آنان وخیم است.
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/439070" target="_blank">📅 21:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
اصابت پهپاد حزب‌الله به یک مقر نظامی ارتش اسرائیل
🔹
وبسایت عبری حدشوت بزمان: در حمله به یک پایگاه ارتش اسرائیل در شهرک «بیت هلیل» ۵ نظامی اسرائیلی زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/439069" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم قهرمان ایران
@Sportfars</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/439068" target="_blank">📅 21:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439067">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عراقچی: تبادل پیام‌ها در جریان است اما تا زمانی که به نتیجهٔ مشخصی نرسد نمی‌توان در مورد آن قضاوت کرد
🔹
به گمانه‌زنی‌هایی که صورت می‌گیرد تا زمانی که به قطعیت برسد نباید اهمیت داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/439067" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjmA0WmNFlA4Wx5ivon7AO0bq_DgWJR0_UL058yI52meUOE95brEUIcO4QA2boRtgTlfC931MqguXwkAJrFMU1U7f1lgV1ms4meaqkVyHdQJPaVGEWdEsr1aODXh1IPs1jfy2Y4dCJM7fYhTc9AP6jbGf8_k41w9GpHemuvXnhzYW7eX2dpgp-TdJHW2rv_-VramFvOh631fP2pBreie-yJ0TkNZMZ68zJR9vPkRDaunWV77KItPctX7xRERKid_WL2hxHDWKGnNXSyrtqF5K_f_896cEBUkZBs7yFRh56tmPchnZ3xkSEKZWIO_ArGFdo6EruMRrhjbfwIy4hKYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ فرودگاه کشور میزبان حاجیان می‌شوند
🔹
در عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور، نزدیک به ۳۱ هزار زائر ایرانی طی ۱۱ روز و با بهره‌گیری از ۹ فروند هواپیما به کشور بازگردانده می‌شوند.
🔹
براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/439065" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا به زخمی شدن نظامیانش در پاسخ ایران به نقض آتش‌بس اعتراف کرد
🔹
سی‌بی‌اس به نقل از مقامات آمریکایی گزارش داد که در حملات موشکی ایران در واکنش به نقض آتش‌بس توسط آمریکا، چهار نظامی آمریکایی و سه پیمانکار زخمی‌ شده‌اند؛ درحالی‌که ارتش آمریکا مدعی شده بود که موشک بالستیک ایران را رهگیری کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/439064" target="_blank">📅 20:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خطاب به دیپلمات‌ها: صدای رسای اقتدار ایران در جهان باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439063" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMyZ9xn4UyYFKMilIfvJwaMxBTkA-C0pkfiSzO-eRWHFx6Dm928nM51SM0K5hhuLuytpra8cVTkjvcQYOhh7hc-ngHRSCURUt3hhNkj-Bo21_NUf5bj-7oolXTC2Gj8bDycMSxSpZHOrP8jx2FQO8zEFWmZyCKsZC2YAdp_3Bvt09cMXDm6QhXLdtuk4_oh8SssIYyOB7yEXd6okS7SbLzcuq48Pwx2uYf-GHjFWG4OtrQooQXuHN1Q8eJF3DsM6gfSKKlcduaj_xTmmQguwNxTzg5jPG43Qc1ATlTl7fyd7Xd3rOtcfMgiOgAuu2pvLsmypUCtkDhHCVS2fbDRDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت دولت الجولانی در برابر پیشروی‌های اسرائیل در سوریه
🔹
شبکهٔ روسی آرتی: یک گشت نظامی متشکل از ۴ خودرو در میانه نگرانی و اضطراب شهروندان سوری و بدون هیچ گونه دستگیری به سمت حوض یرموک در حومه غربی درعا حرکت کرد.
🔹
روز گذشته هم گروهی از نظامیان صهیونیست متشکل از ۳ خودروی نظامی به عمق حومهٔ جنوبی استان قنیطره در نزدیکی نوار مرزی با جولان اشغالی سوریه پیشروی کردند
🔹
تجاوزات ارتش رژیم صهیونیستی در جنوب سوریه در حالی انجام می‌شود که دولت الجولانی در قبال این اقدامات سکوت کرده و در حال انجام مذاکرات مستقیم با صهیونیست‌ها است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/439062" target="_blank">📅 20:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkfnZ7mk9lNF7IJxretAMo6t9fV7zhv_e6ojGM15F-yDOgcMgWdfjOEELZRpcRcxVmQ9JVATkYqGTjeWRW6DQ2ojwKEjpR95XFgj2OiRPPwRMfcH6fq66U1OsYyHMXYyFLLZ5uToC5ToJwiiVwtZ273GcXritWuECWaGUEgjHpzzggAjQ3O2KeXXA_Z_WcGw2l8HrdWmCb6NQ2qkZpcnr74AXP8kaBBJxdIkPN3s6GQa3Su6JPmz28NFQVTFWj46-ppVxobeW8GyvK8gkDE-q0XFpztlyHYRfjQNRx0z83xUFpeb8jSs6CIn67UnT-C-uTGKeIwn4dd5rMm5F7QDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ تلویزیونی «ثریا» فعلا پخش نمی‌شود
🔹
برنامۀ تلویزیونی «ثریا» که با اجرای محسن مقصودی تا امروز به صورت زنده پخش می‌شد،‌ در صفحه مجازی خود اعلام کرد که امشب روی آنتن نخواهد رفت. و تا اطلاع ثانوی پخش زنده نخواهد داشت.
🔹
صفحۀ مجازی این برنامه نوشت: «امیدواریم با تغییر شرایط و بهبود فضای رسانه‌ای، امکان پخش زنده این برنامه به‌ویژه در این روزها و شب‌های حساس و تاریخی ملت ایران فراهم گردد».
🔸
بنابر اطلاع خبرنگار فارس گرچه این برنامه فعلا روی آنتن نمی‌رود اما مستندهای تولیدی این تیم همچنان به پخش ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/439060" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVb_eigUIy8Xtgj0VDDgSXVjBrKs-PQ5Z4mPsXV7RPEIpbJ_nuNIcrbkZITjD_zIjrauTXmMK1bENLSGkNGzIqz75HXJmOtIKJ8zTGrqmzDvaL9yXgQgTdESR4lz53KDbzLfqNgOH5wmeLS-EYZNWRsXWBC2SudcjkZbxG41SO7Th72Ts4P59IUK4NtmYl8ykbhyt5sINabfwclcU5xOdQa07NSX8R2ddPFo1ct0xk8mlH2Vf8JYqcmQobCxDgAyjR7emaL7rNUpgWgblPqoYOIHGwYDktGQ2iqzRimOPNDsAfGx1hgMbnrGS4gKvLgheId91wK2EEMnmllJfQhK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439058" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sskH-2TVxmD-itMxamvPxHoeqBDVW-Vfg57r6gZ_iR5MUcW4YnRW3h8sKgiji2JtVDnhNWbUaTBTa1kW0lnzaw4w_q-Z7SqwyUqyO8bctStEkXSRXBQl-gJJFvV5yLp4MXx2Qed4P3daCjM-HlCaf8v9iaCtLncgP0GLYbBxq_WaTs-qO8QTUT3UvWqUYxFQ0JA37nJ3jiLGj3DR1Ed_aYyG_HLQcBLxaxFQo0okfpLnvXLTEl1_V9LoUsMC3AOAIlFR3qS3vOfM-jmIzigh5eN9R0qFCe9BLczVksR1oMBmi_kGZ8WiTEATCA3wwBgUtl3KkH2ENirezTpTR_E3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از حملهٔ هوایی اسرائیل به یک بیمارستان در جنوب لبنان  @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/439057" target="_blank">📅 20:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ امروز اقتصادی، اجتماعی و فرهنگی است
🔹
اگر به داخل کشور برسیم، نقشهٔ دشمن نقش‌برآب می‌شود. نباید اجازه دهیم که جوان ایرانی بیکار و بی‌هدف بماند.
🔹
همان‌طور که می‌گوییم «بزن که خوب می‌زنی» باید بگوییم «بساز که خوب می‌سازی».
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/439056" target="_blank">📅 20:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: در برابر زیاده‌خواهی‌های دشمن خواهیم جنگید
🔹
ما تا آخرین لحظه در برابر هرگونه زیاده‌خواهی، پنجه‌درپنجهٔ دشمن خواهیم جنگید و خیال ملت شریف ایران راحت باشد که فرزندان شما در نیروهای مسلح، با سلاح‌های آماده و انگشتانی روی ماشه، حافظ امنیت و عزت این مرز و بوم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/439055" target="_blank">📅 19:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eChWbMqyIbcW0HIADq-FcNk3nkp0vj7AxGLDBJ7LjxDmG0tKJNn2rSyvSM5G3sHjV04aFaaiQPqwfXozuQUvELK13wAh6sLYaWOBkQFHR4aRgNPcXRwdkOFDy_Wiq_6pRPcFrwtCkdjqkMy-JP2cTj09jfnGOOmYc9MEEk0ebKdsGzteikdf4eMJBSAVKIk1wDszMk-hWURac8P-7UzDKmL3a6RmrqwVtDvqWoXv3O3Ud_vphpCXFTNHV3l58iIQK0uRNnQ63IeODbC3k-BINvQ6iHfBpvduHojvfgElrC6hr9uBFLguJZxwOzWlf3eUCDU9gQKXTdCu2dvc4hHpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکرار زیاده‌خواهی‌های آمریکا از زبان وزیر ترامپ
🔹
وزیر خزانه‌داری آمریکا در مصاحبه با فاکس‌نیوز با تکرار ادعاهای آمریکا دربارهٔ ایران، ۳ مسئله را برای «پایان کار» در مذاکرات مطرح کرد.
🔹
او در این‌باره مدعی شد: پایان کار یعنی چه؟ چون اگر تمام.کردن کار به معنای اطمینان از بازبودن تنگهٔ هرمز، گرفتن اورانیوم غنی‌شده با خلوص بالا و نداشتن سلاح هسته‌ای توسط ایران باشد، این یعنی تمام کردن کار.
🔹
این درحالی است که ایران بر حق حاکمیت خود بر تنگهٔ هرمز تأکید کرده و با تحویل اورانیوم با غنای بالا به آمریکا نیز مخالفت نموده است.
🔸
وزیر خزانه‌داری آمریکا درحالی این اظهارات را مطرح می‌کند که رسانه‌های آمریکایی سی‌ان‌ان و سی‌بی‌اس پیش از این از زیاده‌خواهی ترامپ در آخرین دور مذاکرات از طریق میانجی‌ها و «اصلاحات قابل‌توجه» در متن تفاهم‌نامه خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/439054" target="_blank">📅 19:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651087d349.mp4?token=d6YCUBj77wLgzjygvEOPt0PtBwqy3gyE22r4mKeq58GQQOCcjtEzup-xRg83jA2PPcvbDNUn6CjvXx8g4_xZkZ_3TGfiZgK9K8xwUxMvvCkaBfPdC73rHEOnsrJhTjg4uv4YJuwOiEGQooWsdcTge-ux5E7IN4UCDX7SGIT5ICiOQfypKeHXH2rDJ6CGaggflIVBV72VgzFN8OmIlaMEc5zrAytPV0bcxJMh3YnS2tJoN26qRDNoc3bMA7japX7oFY1FP-W5l-yG51Ewt5UCCdjDpBF6xy_tLYpPtHTkKp7bjlO3ajBPH1fnw9X6_EMVmlVeqN9BdaGLzr44L5pbpl3KpMUoBXzuQIE6vSxjqvsZw6BdYtHkWBNcK2sPbojgzSGV2VZAF7_Kjgghrp9_lk_k7v4WDHahEon10zmvvNntCopVgYooLVxfYHuQ7DZuC9K-SvMDiOODEunsMGmbjV8xS_hVq7PgWtM7ElBEdqYgUxfBqBzv8COmX8ZBV1sdWaErc3xVEJyV6c_kwIEDCd1i5jGEYLWeiG55rq4AnifLq5U801i-lFeL065xrTkn14Cp2gwfDDLVYVL2NlysDu2BKnolxtFBEv-_YC_2UCdqLNA56JXWtMSReUgLXGq3cOEPBCx73uCGkNP7PGHmTp_MVEBC-6wj76ntbA666QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651087d349.mp4?token=d6YCUBj77wLgzjygvEOPt0PtBwqy3gyE22r4mKeq58GQQOCcjtEzup-xRg83jA2PPcvbDNUn6CjvXx8g4_xZkZ_3TGfiZgK9K8xwUxMvvCkaBfPdC73rHEOnsrJhTjg4uv4YJuwOiEGQooWsdcTge-ux5E7IN4UCDX7SGIT5ICiOQfypKeHXH2rDJ6CGaggflIVBV72VgzFN8OmIlaMEc5zrAytPV0bcxJMh3YnS2tJoN26qRDNoc3bMA7japX7oFY1FP-W5l-yG51Ewt5UCCdjDpBF6xy_tLYpPtHTkKp7bjlO3ajBPH1fnw9X6_EMVmlVeqN9BdaGLzr44L5pbpl3KpMUoBXzuQIE6vSxjqvsZw6BdYtHkWBNcK2sPbojgzSGV2VZAF7_Kjgghrp9_lk_k7v4WDHahEon10zmvvNntCopVgYooLVxfYHuQ7DZuC9K-SvMDiOODEunsMGmbjV8xS_hVq7PgWtM7ElBEdqYgUxfBqBzv8COmX8ZBV1sdWaErc3xVEJyV6c_kwIEDCd1i5jGEYLWeiG55rq4AnifLq5U801i-lFeL065xrTkn14Cp2gwfDDLVYVL2NlysDu2BKnolxtFBEv-_YC_2UCdqLNA56JXWtMSReUgLXGq3cOEPBCx73uCGkNP7PGHmTp_MVEBC-6wj76ntbA666QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بازدید سخنگوی سپاه از خبرگزاری فارس  عکس: هادی هیربدوش @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439053" target="_blank">📅 19:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIRaeWAw48Cxkoh6nmtdkpZSXACaT_zNJd0XGTPbfYr1oUtR7wFRdCrB9A0xq4r8ooNcJWgsBkFU_fvPoeTovy7NcV7nIDdave8Ozzw9lF5jqrR58R8k2SuRy_eEzUvq5dryXCKKmbNSRhsHiLtYDvfZWiDoOHuTyfrQdKUfzBqVal3rMtr_3NT2iGcSgacbbivR_tGiKvtHRYagVmFEjBsjdoGzyirs1MzRHyFdAxu7i57vC4wVoYVcuWO2Svwc7MX1T-lkTct4_PBIB3BYU3gLPjqozwVBdIDRr5O9wy7w_KlCIGialY-TJvhQY6bTdlpTKkMEk8iTpEhCdvTdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8eb409d44.mp4?token=EQ_gYkuN0v2v8TsH_38EcNQ1pwHEFokj09RiDpzXLxW1Ns1nEqrpmJKHxruik7dBg6IzWaQ2qYRoNw6v3XquGzyXPLWCWG-RSWJBaxa87wSj2m9EMwHrdO44U52AjvS_qKAndKeFhY3IAXaVGX-epFWNleDOu1_SXaEhgvGbcVPSlgheM7hOz-hdF0Ripdmp6Lrb-5NyVAmsNQonaaWlMBRiOPmHtS9GsN8ISNSlPjde9GmpE46X0DYIMVWlSpfbxOhhpYquLnTgPPKB6bOWlVi_AbLVO4SAxgiJ2gksVhRKDzJUINgpRTf6wXnXlCzUXDVWM2RhL49tJVS6CIg5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8eb409d44.mp4?token=EQ_gYkuN0v2v8TsH_38EcNQ1pwHEFokj09RiDpzXLxW1Ns1nEqrpmJKHxruik7dBg6IzWaQ2qYRoNw6v3XquGzyXPLWCWG-RSWJBaxa87wSj2m9EMwHrdO44U52AjvS_qKAndKeFhY3IAXaVGX-epFWNleDOu1_SXaEhgvGbcVPSlgheM7hOz-hdF0Ripdmp6Lrb-5NyVAmsNQonaaWlMBRiOPmHtS9GsN8ISNSlPjde9GmpE46X0DYIMVWlSpfbxOhhpYquLnTgPPKB6bOWlVi_AbLVO4SAxgiJ2gksVhRKDzJUINgpRTf6wXnXlCzUXDVWM2RhL49tJVS6CIg5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد حزب‌الله به یک مقر نظامی ارتش اسرائیل
🔹
وبسایت عبری حدشوت بزمان: در حمله به یک پایگاه ارتش اسرائیل در شهرک «بیت هلیل» ۵ نظامی اسرائیلی زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/439051" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLQza-_uoMqcTz9p4Z-RTwdZC9EWB9BId_VHXZgdSK1t92416aKncV9PO3DbUDLVv_9JVxy9ZWfP0wQKBi-qXS2aFBd2y2UTROW5yoaK2iVNb0VAmlYW_yLniUHXKZISnVYZR345O8Qg-W-WUwLmPQCMpgprd5ZiCAoqPKRq2C66jeptMtXryw2kc9x0DLLRT83AKRgokwdgSdvIIOzOiYOW1HZb-Zm49Kcw8RWQh6LYASj-1f0RWJQDvVLsy-tSibkvCD3sPizaHxHKJq6zDi3Siea7K8S7DqOfW_4gszW6kpd7afY5AGJvF9ytFvTAVTp1IOgSODCX436Sh8wz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رؤسای ۵ شهرک اسرائیلی با گسترش حملات حزب‌الله
🔹
رسانهٔ ‌عبری واللا:  ۵ نفر از روسای شوراهای محلی و شهرداران مناطقی که تحت تهدید مستقیم حزب‌الله قرار دارند، برای مأموریت‌ها یا بازدیدهای «غیر فوری» به خارج از این رژیم سفر کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/439050" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d41eb6ba2.mp4?token=IEZ4w6vbcR7a5fG6pAcMeVpPBE9hlrwhjLfws0OH0QfFYF3RIlPam2mjrVLMdV7sJcyRyln8z4dQhQ8SdGZ_7_x1aU-Cop-AO3kNeorJUGN2MmCpZnR-_nRIINEDxM2kvRyyHAhJXxHXPymVEhz_R9KdfIPKudeOVToLxq_up8xyVCWSygb3ziWr1U086s9YK72e4rkeANTwuROhXBtr69hnvibJXb5t6PyTwIz9GzVDtdegW6zfTOO71H_3y9Sv_BHVO8twjg-wTY7pG8Triwwsb26o4ssOEUL93aO7Q0kobWA_Xq51Owe9Xj1Kg88dKin88EgbgaqxkEUUmT2lFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d41eb6ba2.mp4?token=IEZ4w6vbcR7a5fG6pAcMeVpPBE9hlrwhjLfws0OH0QfFYF3RIlPam2mjrVLMdV7sJcyRyln8z4dQhQ8SdGZ_7_x1aU-Cop-AO3kNeorJUGN2MmCpZnR-_nRIINEDxM2kvRyyHAhJXxHXPymVEhz_R9KdfIPKudeOVToLxq_up8xyVCWSygb3ziWr1U086s9YK72e4rkeANTwuROhXBtr69hnvibJXb5t6PyTwIz9GzVDtdegW6zfTOO71H_3y9Sv_BHVO8twjg-wTY7pG8Triwwsb26o4ssOEUL93aO7Q0kobWA_Xq51Owe9Xj1Kg88dKin88EgbgaqxkEUUmT2lFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد انتحاری حزب‌الله به خودروی ارتش اسرائیل در الجلیل در شمال فلسطین اشغالی   @Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/439049" target="_blank">📅 19:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن خواهند بود.
@Sportfars</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/439048" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66ba635ed.mp4?token=rjDEJv5314R4BEPJwbuG2zWS-k9YQ3qNPOphKaPdbEx5RL5WSWuyO_t5VOahaAJaN8uyP6x6Ip58FGTyb8cimvkJs-eBpXd3jV4JRrfi0iZdH0Kd2lKAYqoSTj_L7YSnWwTCyMDEYQRZuENeAT-Ae8ya-D9fhn4xfEgOuj-SnjZ6qxsN0XLsT2IZhgAfY5UqXBY1VQ1L6SiFzCQ9Uv79HviVKQfjKh1N9sPIZylNTroOUzI4YlT3rzzDYqBKvjFVZLLE088oC3q2a4DDdM4tRoZv1t64TGriyLXhrKvY5dzZUDcY6oeE2pV718lmYWxWYIBIvLgesWQkirQfO5YPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66ba635ed.mp4?token=rjDEJv5314R4BEPJwbuG2zWS-k9YQ3qNPOphKaPdbEx5RL5WSWuyO_t5VOahaAJaN8uyP6x6Ip58FGTyb8cimvkJs-eBpXd3jV4JRrfi0iZdH0Kd2lKAYqoSTj_L7YSnWwTCyMDEYQRZuENeAT-Ae8ya-D9fhn4xfEgOuj-SnjZ6qxsN0XLsT2IZhgAfY5UqXBY1VQ1L6SiFzCQ9Uv79HviVKQfjKh1N9sPIZylNTroOUzI4YlT3rzzDYqBKvjFVZLLE088oC3q2a4DDdM4tRoZv1t64TGriyLXhrKvY5dzZUDcY6oeE2pV718lmYWxWYIBIvLgesWQkirQfO5YPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای برق‌کاری که در زمان حمله به پل B1 کار خود را ترک نکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/439047" target="_blank">📅 19:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ac1caf9e.mp4?token=jiLX7UwPY6IV5OcJiyGdgIhAnBZKiobILUptYysDbz_oPyRe7OHKaERMyb_gSM4NorBsKIsorXW0v41z1MqVd4npQXdRllddPHvzajp8OuFk9NLxhO-VvwqzcGf9cVgLYI2tiCSDn_YDJrODz0boLx9HCr-zGrc_YVcdn3JKQ9r5wk1kcIBF_g6mx5CAM4xFcdu79ZlZCF3tbJA4ZKyUK45rb6SFRRcg2xI3LVBW61HN0pJuJhpeQVzucuPuHESdCqhj6AURtf6efAmMvnaXlFmOtBSejvxGWz8OuWId6Oi6vZEfgtbWUjW3GxCGGW6DRtdBWBmW2uyg0KJ6d5mE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ac1caf9e.mp4?token=jiLX7UwPY6IV5OcJiyGdgIhAnBZKiobILUptYysDbz_oPyRe7OHKaERMyb_gSM4NorBsKIsorXW0v41z1MqVd4npQXdRllddPHvzajp8OuFk9NLxhO-VvwqzcGf9cVgLYI2tiCSDn_YDJrODz0boLx9HCr-zGrc_YVcdn3JKQ9r5wk1kcIBF_g6mx5CAM4xFcdu79ZlZCF3tbJA4ZKyUK45rb6SFRRcg2xI3LVBW61HN0pJuJhpeQVzucuPuHESdCqhj6AURtf6efAmMvnaXlFmOtBSejvxGWz8OuWId6Oi6vZEfgtbWUjW3GxCGGW6DRtdBWBmW2uyg0KJ6d5mE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع ۳ نفره که هزار نفره شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/439046" target="_blank">📅 18:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439045">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eef00ec67.mp4?token=FJ6fQrnRrGCX5RY4ZoXMEtGj_a-n6Z4ecCmrLDh6O1-a3SyPUPiFLrw7egsdbhZWuSr0AiZbCTr4fF3C6fQryPvQ9aeP-7LgrWC_1LsvsmgcOX9V7uBStz7HA-YzjEtLrr2F089II2nxRahpNGEKbBhRCsAfFQpIH-WCosOQVnUvUImupI2H1kt4Xk7cq3R0GWFa9oT5lVYnPaN5wTQEqr8LO1ZrWmWWPLmQcCn_bEVSeXouozVq0AsDnvwwIIX1n9mcJsdhq5l8NY9EWZF9IxGFqr7udo3kU4-Y7g2L0wHhOrJcZfdLmfZMn4Yu1UDO4SmDcXqIST-AZHJNmBQ9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eef00ec67.mp4?token=FJ6fQrnRrGCX5RY4ZoXMEtGj_a-n6Z4ecCmrLDh6O1-a3SyPUPiFLrw7egsdbhZWuSr0AiZbCTr4fF3C6fQryPvQ9aeP-7LgrWC_1LsvsmgcOX9V7uBStz7HA-YzjEtLrr2F089II2nxRahpNGEKbBhRCsAfFQpIH-WCosOQVnUvUImupI2H1kt4Xk7cq3R0GWFa9oT5lVYnPaN5wTQEqr8LO1ZrWmWWPLmQcCn_bEVSeXouozVq0AsDnvwwIIX1n9mcJsdhq5l8NY9EWZF9IxGFqr7udo3kU4-Y7g2L0wHhOrJcZfdLmfZMn4Yu1UDO4SmDcXqIST-AZHJNmBQ9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما نیز می‌توانید سفره‌دار مهمانی بزرگ غدیر باشید
🔹
در هر شهری که هستید، در مهمانی‌های کیلومتری غدیر و اگر در تهران حضور دارید، در جشن ۱۰ کیلومتری غدیر، با هر میزان توان و وسعی که دارید، حتی با تهیه یک لقمه ساده، در اطعام جمعیت میلیونی مهمانان غدیر سهیم شوید.
🔹
برای ثبت‌نام و پیوستن به پویش «لقمه میلیونی» از طریق راه‌های زیر اقدام کنید:
ghadiryar.ir
ارسال عدد ۱ به ۳۰۰۰۶۰۳۰
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/439045" target="_blank">📅 18:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNtm6uwUvH-H9B9ftVr1xxflJ2204Jv9F399JybprNaXaRjJVm-cNlMEZRRcM-IXkDQtIMWj_XkHuRdgfajkxB_-1EhIuWYKhi6VdfzER3AR5O-RxF8UtxoFc-5fe0-6qbLdiXicLOCSUjrIpQB4WFe-2bR-aVjPjoUtfotUv6vzwoend2FLMTo1DFnQ9PuBfNzHoCGTaRxkv9JwrcfWcj4oozUGDYrfVS5OEyMS7d8As3A8O6H2oo79qBBwWc6H_F5R5b8pm0RL1FBGzwZn6_A9EzPeUXhn_Eae0BySUa4fS5TAaWiuV9g8HTVA54rh0iz6_u14QvljiDYczTOKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuI6YZHLxoqRk9N-UKlccLFwsVFmoyyLQcQEauKmCGEilVH5ba9zlzAaoyXir9vBsH1KB2ddopEf6NkTPnK3Eb6PM9By0jpWa4hxiz6QXpsK-TJr9544ZM6QHVgKOitjuXCbWeKtrTLrbZWycNPZ3CM9DfiukShpi46TBMJAte5sV_pGOW9ILK_TAwUCtPv64TA41fObDUs9NepRlVWS2nlBfXCMqhhIQdBwkU0KE89Iu6W9HpZekSa0IEaU0aS0XAoI4fHJddWQdQEMroj2UmOtHQ5Ai8oR3ipXrnRL5b3wNZgPVBzo_nTMAMSe0y-SS2QWFuh8_L8sN_hhHeVjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAa3zzVmRJRuLBXlV-7fJ3HKeawAJnCZNCHqghSnMGj5gtk5l9UWwgYFJh8UY6X91LvluFcuwZZ3BJ8u_YM-T_6xbDzjNZogYoWMDK-0VLFXvfFCHnlZ8U8ttQ3rpaIOMt2Tc90j58bz_ksB_6AaO-PEqS8uoEit7FOx0ZtYJtQ71f-iiQAaLwJodROkPol4eu0gJkZkKlv4kHWYDt8G0P5BTCaAcuD8vp2-BgzeZHyZM_Q4cxlKMULSrXXE7YuSPpSNUP4CKq6u8Y8OoSPn1SNICYHeAZVeiaTDrDLqa2JMaadur8swgi3Wa_3wflCRlqxMh65uJk8AD4yapYsGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fl7mhTVKsvrNcVfLyz_slL7YLmG7De0BmCGcru-B-YtHghA-chThzK8HEOX3DtCTZEp91J_VXscH_-o0fbTM6Rvtdwqn7z_JlpgnarMB1OdeNyM89vvpCC9OtRIk3GoVEFX173GmC0by4XM5UyFFcZc5RkggP5iZQrVIZAI05Ixv4Yj_7E-2d6JJIZ29wqwQ92wOsdHVvNGzy48m00ymiS1JzskShwKTjTo_KoIAwgJ2dYaOskoewubif6imzgVsEOjEWm2IiuJB6KOPsFk_vL1gXVpnHVMWL_4ZiK_Bq63JwoafGcPNkcdbp9bHbi2qeR3M9vS8ObhgqhPghQ_APw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzY7J4HLQv7GxRLOiMiaIWT62vkLI6tK4iW4_X3yxVQNAotDqgC_ZyTzE3Xo6ni9lDyfAVBoDKZikmWoWPM5mIKI4x9AM0GI1XODjYx6VseLyDfafm81O8cy7I8bQEJ7ui_ZRKS2uZ02mJxIeHeGSH_PQofIzFFQKrrHx9B8i-x7Npj0EO5RLSb2FowfnQjGVL6bslcqlu_ed3N-hejk4scsyEV7-jiFNJ2mhSkeWQ_N-2U5ONEQ6Tla5jAPpepoVsA4eNFZKWUaDGKORinwF8nuOFparWF1fYHVieBfShRezkf398hSQt6cna917Q3nWJ8IG_ZGf5C8tZXzLrIEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOXQJItWGi5oVqPYrb1EOZ6k66ds5qi52roWax6zXzTnOWTO_Qyr7AuBhjHbQG3KKb38Lsk1dzd_b1w860bolfucnndosM2IrEs1g8Gh_AEyRamApC8_gv6UkuPBWb9zzgDz1uTi2YfGPGzzQ_ZVuF2S2mhsixeggGClpqsJTb_Ff-PDZrvLTed7oZsZ_DQLQf6wUR5Tf80_-hH9vPtP3O_kFWFOpmhuD_EZlSL6wDJHbwaAMIJrJrALBsrlmGoDALRaSnnPb3VAuCi1ZPK8w_DToakOVoLhlF3zbj6nHsX--67yhd0-XjYygsahkPxe9D0NSpDnB4-BOUW1tY27oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O09wR69YRyRDeB0Tjm0PvxRg4eASDEMXSVP0-rM8EiIgbBI4JJd-FRD5T4jTPyuZUdYhd45gASMVoBb2_PlkPl7GRq19pJYbNJCWZSwG48x2WwsOjdiyi83zF9oMBoYyeqO7tv3VfDDcXle28EeRP0rLBiDLh0dxJtVwS9BVQRoeSkcsyX-isItxfbpHnllue26zPsaYpE1t0dBTergQ7OPQjwr-0dOgygY6ned1TgUrKLhh3Bj9C7O7wzi6UvEcGI3HP4F5eIoVN5ybE6l_ed41Mmzk-t4qdLDlZzt-yLe8JPhf-tXP3C8X66KYaN8-iKVRwGk6yJh0vlqM7t6aQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی سپاه از خبرگزاری فارس
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/439038" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5bb3d4e6.mp4?token=v2XFZuOAB714eyG61eb1IWUXk9guMoZCb9FgAPOffLHQww2jIIcELkecM3nF8XSs0SwwH7gCBk0FneQPVbvzl8rNxqaggYvHPjnvv0P3685du_sDSpc5WCCwAUut1puICQq8Blp0MGUojMJSQLwCCiUNLG_IegPHdZsdHYb79LrU8DDsNkeJhaGT_BApoPR0hUxBz5wjMjzTY8CZtkp2eBoXaZ6hwFQ46o2Ai6Lx7YGt38UZtHGpkWfUSK0V6vwDbnwKHkJKkvxSx2QJkzrujXV3IUsKrsEZDNFq7gSSg86M4EMQuJFgCM8qiROooWu7WwZCOYsfGtfsJ63KkH_NrCa2RAc9KMcYhYjg5Hxicp6MrOboJeciI63nrKF8HZnaqvi0CpqkBtfRwUuQmPQYGxnBfoDMsJNDuakFKn7e1TfdVPmlmm8BoDKT3vAKAkdA52FdsZKTJJJXXGFERG05amcQxjuk7L5335pLz_IBGVUweygcSkC5Rqd6epbl6ZTg-L0gEz_7uNFKYoi4jzTYcN5mgq7R9UoLRIVMjwM4R-lj1vwvWey0GTycw2GxpBw7Im0iIqMrwFTLa_gcXEiKDxqAM9ILJRgVfJX0eMENM3rbAmw3rKUfnWRNfRk3QYK2e5SYr4e1-7ZA750mcCrTCix1PW5HLNXNP4-RuXQDMZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5bb3d4e6.mp4?token=v2XFZuOAB714eyG61eb1IWUXk9guMoZCb9FgAPOffLHQww2jIIcELkecM3nF8XSs0SwwH7gCBk0FneQPVbvzl8rNxqaggYvHPjnvv0P3685du_sDSpc5WCCwAUut1puICQq8Blp0MGUojMJSQLwCCiUNLG_IegPHdZsdHYb79LrU8DDsNkeJhaGT_BApoPR0hUxBz5wjMjzTY8CZtkp2eBoXaZ6hwFQ46o2Ai6Lx7YGt38UZtHGpkWfUSK0V6vwDbnwKHkJKkvxSx2QJkzrujXV3IUsKrsEZDNFq7gSSg86M4EMQuJFgCM8qiROooWu7WwZCOYsfGtfsJ63KkH_NrCa2RAc9KMcYhYjg5Hxicp6MrOboJeciI63nrKF8HZnaqvi0CpqkBtfRwUuQmPQYGxnBfoDMsJNDuakFKn7e1TfdVPmlmm8BoDKT3vAKAkdA52FdsZKTJJJXXGFERG05amcQxjuk7L5335pLz_IBGVUweygcSkC5Rqd6epbl6ZTg-L0gEz_7uNFKYoi4jzTYcN5mgq7R9UoLRIVMjwM4R-lj1vwvWey0GTycw2GxpBw7Im0iIqMrwFTLa_gcXEiKDxqAM9ILJRgVfJX0eMENM3rbAmw3rKUfnWRNfRk3QYK2e5SYr4e1-7ZA750mcCrTCix1PW5HLNXNP4-RuXQDMZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسول نجفیان، بازیگر: خائنین در شاهنامه همگی نابود می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/439037" target="_blank">📅 18:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bb02bb85.mp4?token=I94HjAGGN7y_-0QGPda5En6Xqc9SC1poXDaNz04_A4k16QsgO94G7z7EAcS2awPhnT0xBI3ZA2eOOSBLPoWbMitMnqXJQgAM2E40btIQuPnR-yJtH5ucWYjj10NUCba9IE4nOFBfihzPcE5GiHjcW6mkC_O1--Nn-IwLYnYhmZvzUI11g_I5BXIahDASS2BopQtKaX79p_JG_lOjS91CVul0nEffogfVmr2IcQcMDAXfMLacUaPhwQp07zP1PKeySJTRk5qcqpKbhEQ8rKwSN78OOIWgwphnI0MgSwoqAwQHPMo_qdZ4YezGeg0hPyKj4tP2n5xZ-BpSapIFM6HRIUSCkRF2crfiRleu0-AY1rNg3d-n9PcMBsobpX6wK2-d8x55B5Tnv8PxhCmxQ79xlrDe9Lbmmcs2PT6y6vK9-_ug-mEmEK7jNBGu84nZ1P2vztoMEQ4vGnzlvRJgZyzHmr2poX-7i97UMMbCcChOk82QvTdfYhZEKhAqa52ojkfSmJaiW-LEH6A8sa1l0CO8HeotSP9IS8e53BJC_MHSvW4rT7C0JhevDB-RpvuZzaz7YhdSzVXwWwJ3HO05HJpODm0Yz7Ij8NpY1KFhV92ngOI3efGbCETkzNzOQien2yvWv8mzbdEsM7u4ZdLeKLT2XT2ZgtLtV6gdZMcWgE8hTF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bb02bb85.mp4?token=I94HjAGGN7y_-0QGPda5En6Xqc9SC1poXDaNz04_A4k16QsgO94G7z7EAcS2awPhnT0xBI3ZA2eOOSBLPoWbMitMnqXJQgAM2E40btIQuPnR-yJtH5ucWYjj10NUCba9IE4nOFBfihzPcE5GiHjcW6mkC_O1--Nn-IwLYnYhmZvzUI11g_I5BXIahDASS2BopQtKaX79p_JG_lOjS91CVul0nEffogfVmr2IcQcMDAXfMLacUaPhwQp07zP1PKeySJTRk5qcqpKbhEQ8rKwSN78OOIWgwphnI0MgSwoqAwQHPMo_qdZ4YezGeg0hPyKj4tP2n5xZ-BpSapIFM6HRIUSCkRF2crfiRleu0-AY1rNg3d-n9PcMBsobpX6wK2-d8x55B5Tnv8PxhCmxQ79xlrDe9Lbmmcs2PT6y6vK9-_ug-mEmEK7jNBGu84nZ1P2vztoMEQ4vGnzlvRJgZyzHmr2poX-7i97UMMbCcChOk82QvTdfYhZEKhAqa52ojkfSmJaiW-LEH6A8sa1l0CO8HeotSP9IS8e53BJC_MHSvW4rT7C0JhevDB-RpvuZzaz7YhdSzVXwWwJ3HO05HJpODm0Yz7Ij8NpY1KFhV92ngOI3efGbCETkzNzOQien2yvWv8mzbdEsM7u4ZdLeKLT2XT2ZgtLtV6gdZMcWgE8hTF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناکامی‌های آمریکا در جنگ تحمیلی سوم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/439036" target="_blank">📅 18:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8847b20aea.mp4?token=NasFRiLu4XMIeLdbUQmgYG4__yvOBZ8srr26FyXEqfOT1E8BBtGLFM_z-QSjfV656MNYBebGvmHXl-V8P40urd2gnMhL20M4NiN_fHERWNBTIPzBc-3a_xtqC3B-Km-1dlNVuKj6j7uCdTeIbC8cqCer5Fh9Ensot5z0HSjpDyypvPWcr3edZMZADpwSokc4-GeNa4pNmbkI4O0-8K-TNvRn2jG4a7zwXbbfDlhhVRE2Mg5BxX9G1WyaOLX9aJmh_6ddGWu-eWzTibMwvLs3pvaeSaAIsbuR1akfaXEFygsi3t05gIJJTz4RGEpm8hCVwFbvOwaPQyDjvcBmIcGn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8847b20aea.mp4?token=NasFRiLu4XMIeLdbUQmgYG4__yvOBZ8srr26FyXEqfOT1E8BBtGLFM_z-QSjfV656MNYBebGvmHXl-V8P40urd2gnMhL20M4NiN_fHERWNBTIPzBc-3a_xtqC3B-Km-1dlNVuKj6j7uCdTeIbC8cqCer5Fh9Ensot5z0HSjpDyypvPWcr3edZMZADpwSokc4-GeNa4pNmbkI4O0-8K-TNvRn2jG4a7zwXbbfDlhhVRE2Mg5BxX9G1WyaOLX9aJmh_6ddGWu-eWzTibMwvLs3pvaeSaAIsbuR1akfaXEFygsi3t05gIJJTz4RGEpm8hCVwFbvOwaPQyDjvcBmIcGn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین ویدیو از خلبانِ شهیدِ جنگ رمضان قبل از شروع ماموریت
🔸
شهید جابر طاهریان از شهدای جنگ تحمیلی سوم است؛ که در ۷ فروردین به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/439035" target="_blank">📅 18:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4849a3.mp4?token=oXX0fajICprh7yn_rnKEjVV1X9eQRS_P0GPSD22Fo5E2dyE5hlxqYHEKvCLkBkynsLs0VrF40JcdL_lOS-_Yl6V0W1mJx2qXI3kNbsBqsVRz4IpZ6V_B-uDXstgbDcv66z6dZMeCtH20-vFrE6Aku0bKWSKLTmIPc5OUl7N3MFK9sGymgghrlq7CGcX9rwdXG_AWl_ugFnLjzgAXH-0R50SR2380gMXU6ZLNeWWc6SG-UvdOS7hPuv3-6Dx1vrHHfPxNMNSegKYzUGmbA-UvyPydTYxS9liqJm5NvQfF_KKp5GywDABeghCkIA1Ad8S0VRare01Q06tpRrqEwgK1CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4849a3.mp4?token=oXX0fajICprh7yn_rnKEjVV1X9eQRS_P0GPSD22Fo5E2dyE5hlxqYHEKvCLkBkynsLs0VrF40JcdL_lOS-_Yl6V0W1mJx2qXI3kNbsBqsVRz4IpZ6V_B-uDXstgbDcv66z6dZMeCtH20-vFrE6Aku0bKWSKLTmIPc5OUl7N3MFK9sGymgghrlq7CGcX9rwdXG_AWl_ugFnLjzgAXH-0R50SR2380gMXU6ZLNeWWc6SG-UvdOS7hPuv3-6Dx1vrHHfPxNMNSegKYzUGmbA-UvyPydTYxS9liqJm5NvQfF_KKp5GywDABeghCkIA1Ad8S0VRare01Q06tpRrqEwgK1CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات بازندهٔ رقابت کریدورها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/439034" target="_blank">📅 18:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yuiz7OBjF8dgQMOwYP5QmDmfE0mtekdQpV9sxtJEk8iglLW6bkOk_vInCJ-2PREM6VW9MlSXHYWwpbb3G9g5S5_S1GshglFu8dX9LDMKHIUCK-MoywYbJPMP3uBE-ViMiJ8W4MN2F2W__Zihsw4tdkaNoTgeI4iYTSqej3KLOi0ju76Nzu9WzsSsEH29wQxrZl6FqtuEsLj4Xsyqg_tdBBFWocAImFqdXzPTsLWxKof09ir2Hyo1Jc6vppVCku26AhDp2Cv6RmkQdfx_eos6uxUqMLYLVKNMKmRQefKn6WBCGJayTbnRZuuQNkQjHxg_I6KgjgDAJSEOF7miWtAztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سکوی پارس جنوبی به مدار تولید بازگشت
🔹
مدیرعامل شرکت نفت‌وگاز پارس: بازیابی ظرفیت تولید و فرآورش گاز غنی در میدان مشترک پارس جنوبی با اتکا به توان فنی داخلی روند مطلوبی دارد و تاکنون ۳ سکوی فراساحلی پارس جنوبی به مدار تولید بازگشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/439033" target="_blank">📅 18:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE6PM-Zc7-pxdtzsVVQsag-6tXUAyk8gRE5iM8v7Jsqt_MnmXlvLzZ1zsafbkdr1lsRpKyMpqRpU26rX3UtBUBybeL9XCi2sKFKtIyy7MR8eWCZ4MdfpOMohB4YrIJFpjDL_9ilUrQjUXlGT8ZLClgi1ectoxzZ-Q8fkQ5OQ8YurybQ8gGlW5B6wL2IeNORalJEwBmrfbTcxKCcu8JnthZ9MvqfrO7HpuTsSxJ7iD67hPS-qorebJzR31Utek24HFNx84TBMDSwgkcEz58IAKvQc_M-xSryvCFF6M06mL7jrIpIjZoRThOXuqjAJGBdeNN7BVpuS8tFX5hMfe8ggCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فراخوان پانزدهمین دوره
#جشنواره_بین‌المللی_فیلم_۱۰۰
منتشر شد
🔸
این دوره از جشنواره در بخش‌های «
نبرد برای آینده
»، «
نبرد برای کودکان جهان
» و «
نبرد برای وطن
» برگزار می‌شود.
🔸
آثار کوتاه برای راه‌یابی به سه بخش جشنواره باید
حداکثر ۱۰۰ ثانیه
باشند. تنها در بخش «نبرد برای وطن»، آثار
تا سقف ۳۰۰ ثانیه
نیز امکان حضور خواهند داشت.
🔸
مهلت ارسال آثار به جشنواره فیلم ۱۰۰ تا پایان روز
دهم مرداد ماه
بوده و زمان برگزاری جشنواره نیز
شهریور ماه
است.
🔸
پانزدهمین دوره این جشنواره به دبیری
#محدثه_پیرهادی
، شهریور ماه ۱۴۰۵ برگزار می‌شود.
📰
جزئیات بیشتر و نحوه ارسال اثر به جشنواره را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/439032" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
🙏
دکتراخلاقی در نشست بررسی راهکارهای گسترش تأمین مالی غیرنقد عنوان کرد:
✨
بانک تجارت با تکیه بر تأمین مالی زنجیره‌ای و به‌کارگیری ترکیب ابزارهای نوین، آماده همراهی با مسیر جدید تأمین مالی کشور است.
💠
دکتر اخلاقی با تأکید بر ضرورت عبور از الگوهای سنتی و حرکت به سمت ابزارهای نوین مالی، گفت: بانک تجارت با ظرفیت بالای تأمین مالی گسترده و بهره‌گیری هم‌زمان از ترکیب ابزارها، می‌تواند نقش مؤثری در هدایت منابع به سمت تولید و پایداری بنگاه‌های اقتصادی ایفا کند.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/439031" target="_blank">📅 18:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/439030" target="_blank">📅 18:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-52.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439029" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-50.pdf</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/439029" target="_blank">📅 18:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
پزشکیان: اگر می‌خواهیم ایران با عزت، اقتدار و ثبات مسیر پیشرفت خود را ادامه دهد، باید همۀ ظرفیت‌های کشور را به میدان بیاوریم
🔹
ادارۀ کشور صرفاً با اتکا به گروهی محدود از مدیران و مسئولان امکان‌پذیر نیست. همه اقشار، نهادها، گروه‌های اجتماعی، نخبگان، فعالان…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/439028" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
پزشکیان: مسئولان کشور باید در کنار مردم، در متن مسائل و چالش‌ها حضور داشته باشند
🔹
مدیریت کشور در شرایط دشوار نیازمند حضور میدانی، مسئولیت‌پذیری و همراهی با مردم است. اگر مردم با دشواری‌ها مواجه باشند، مدیران نیز باید در کنار آنان حضور داشته باشند و برای…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/439027" target="_blank">📅 18:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
پزشکیان: جان و مسئولیت ما از رهبر عزیز و شهید و مردمی که در راه دفاع از کشور و آرمان‌های خود جانشان را فدا کرده‌اند، بالاتر نیست
🔹
آنچه اهمیت دارد حضور در میدان، پذیرش مسئولیت و ایستادگی در کنار مردم است. @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/439026" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت و مسئولان کشور خود را برای هر شرایطی، اعم از استمرار مقاومت و تحمل دشواری‌ها یا پرداخت بالاترین هزینه‌ها در مسیر دفاع از عزت و منافع ملی، آماده می‌دانند. @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/439025" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
پزشکیان: خدمات‌رسانی دولت در هر شرایطی ادامه خواهد داشت
🔹
دولت با تمام توان و ظرفیت خود مسیر خدمت به مردم را ادامه خواهد داد و ادارۀ امور کشور با قدرت و صلابت دنبال خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/439024" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت درحال برنامه‌ریزی برای تحولات پیش‌بینی‌نشده است
🔹
عبور از فصل تابستان ممکن است با مدیریت‌های کوتاه‌مدت امکان‌پذیر باشد، اما برای ماه‌های آینده و به‌ویژه فصل زمستان باید از هم‌اکنون برنامه‌ریزی دقیق و آینده‌نگرانه صورت گیرد.
🔹
همچنین در صورت…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/439023" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
پزشکیان: مدیریت مصرف انرژی ضروری است
🔹
اگر در حوزه مصرف برق، گاز و سایر حامل‌های انرژی نتوانیم الگوی مصرف را اصلاح کنیم، ناگزیر بخشی از ظرفیت‌های تولیدی کشور تحت تأثیر قرار خواهد گرفت.
🔹
کاهش فعالیت واحدهای تولیدی به معنای کاهش درآمد، افزایش فشارهای اقتصادی…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/439022" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
پزشکیان: جامعه باید نسبت به الزامات و هزینه‌های مقاومت آگاه باشد
🔹
اگر قرار است کشور با اقتدار مسیر خود را ادامه دهد، باید واقعیت‌های موجود برای مردم تبیین شود و همه بخش‌های جامعه در این مسیر مشارکت داشته باشند.
🔹
رسانه ملی و دیگر رسانه‌ها در کنار تحلیل…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/439021" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
پزشکیان: هیچ جامعه‌ای نمی‌تواند در شرایط رویارویی با چالش‌های بزرگ، انتظار داشته باشد که بدون تحمل سختی‌ها مسیر خود را ادامه دهد
🔹
مهم آن است که این مسیر با آگاهی، همبستگی و مشارکت عمومی طی شود. @Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/439020" target="_blank">📅 17:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
پزشکیان: مردم باید نسبت به واقعیت‌های موجود آگاهی داشته باشند
🔹
بخشی از مشکلات اقتصادی کشور ناشی از محدودیت‌های بیرونی و بخشی نیز ناشی از فشارهایی است که در نتیجه شرایط خاص کشور ایجاد شده است.
🔹
دولت و تمامی دستگاه‌های اجرایی با تمام توان در تلاش هستند…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/439019" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/439018" target="_blank">📅 17:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های خاصی را برای ادارۀ کشور ایجاد کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/439017" target="_blank">📅 17:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f774ef204.mp4?token=OUdW-TFK7GcAyf5qS9pR4S1fquUGRQSnhxwCfu8RGHHh-GkUpiFNNaiXD5z1tBGfsaRCmNEhZfNpPqT03lLNyM99k1yuyEJcW0q4rh_Z2YFhsQA4IY3Fn9VmBbybZN5mcll8jbTZhDxpe4yCulTGyNmAGbLewMEO8bXHOKk1-SVy_Ce7VPPiS1Pe9GGCR9203aMNtyE3Y0XGdqdz0CNgbE1MZGKYnY4RtsmA6Kx1sFHn2uUR5_TiLNua2Oh7cIgDVLso-PdWE-c-tWKNhOyEXtA0EUX10_Rqqd6wZj_jUlurM2dwekNIrMZgoV3x2bbrbEK16PrqaD0sSkbkUPnoeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f774ef204.mp4?token=OUdW-TFK7GcAyf5qS9pR4S1fquUGRQSnhxwCfu8RGHHh-GkUpiFNNaiXD5z1tBGfsaRCmNEhZfNpPqT03lLNyM99k1yuyEJcW0q4rh_Z2YFhsQA4IY3Fn9VmBbybZN5mcll8jbTZhDxpe4yCulTGyNmAGbLewMEO8bXHOKk1-SVy_Ce7VPPiS1Pe9GGCR9203aMNtyE3Y0XGdqdz0CNgbE1MZGKYnY4RtsmA6Kx1sFHn2uUR5_TiLNua2Oh7cIgDVLso-PdWE-c-tWKNhOyEXtA0EUX10_Rqqd6wZj_jUlurM2dwekNIrMZgoV3x2bbrbEK16PrqaD0sSkbkUPnoeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد انتحاری حزب‌الله به خودروی ارتش اسرائیل در الجلیل در شمال فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/439016" target="_blank">📅 17:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onbEIwAWVNTZIX6dMw2bfm3D579EGRIgQVlmC8mo7Reoz8V9hsdebTno7Gk6xFimG9tzkiq6FPgQIehj7BsjB6vZhL0QcrwAm34XjzOIEpF4VUB8ribE0ioSssmsp_E2yxr-l8Skw4HREowDqBA4gmbEVIJyrwScfJyTZHWHUO5-XlO1Iu00c850pW-6J61QQqep1MbEOe15N2a_PSGuAbFzfGyAz_zV5tSGnbK6qUR8UeSwCFUnM8js2BYa_gSemoYk2rWZxgXBSoHTKTZS506Yg2JEkGkhK3ATrPU6aq0mVHMLlmq6qXrjeT33FAB-B0jAs-xSHCMCMGpamb-KyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیعت بزرگ ایران در مهمونی ۱۰ کیلومتری
🔹
عید غدیر، عید ولایت و امامت است؛ عیدی که بر محور پذیرش ولایت شکل گرفته است.
🔹
ولایت، یعنی پیوندی آگاهانه، عمیق و استوار با امام جامعه. پیوندی که در میان مردم ایران ریشه‌دار و مستحکم است، هرچند ممکن است در برخی بخش‌های حاکمیت هنوز به استحکام مطلوب نرسیده باشد.
🔹
جشن‌های کیلومتری غدیر امسال، جلوه‌ای از بیعت بزرگ مردم ایران با ولی‌امر خود، امام سیدمجتبی خامنه‌ای است.
🔹
تجربه تلخ تنهایی امیرالمؤمنین(ع) در ۱۴۰۰ سال پیش، نباید تکرار شود. از همین رو، مهمونی ۱۰ کیلومتری غدیر امسال بیش از هر زمان دیگری اهمیت و معنا پیدا کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439015" target="_blank">📅 17:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=c96kowPVj-trPATXmwPkrzRxMVPi8DYiuC5lBI_HFNje8K8sE4HTQB-zribNdbRAcyy7tQiC0bjf36d5jeAfBUNw4OR-YWj_b3zF3T2PuSzaAlS2qClScT2UYBUDaMuoG19-KwJC9eTGodLohLgjegeb-shBqNQoLWjl3UJr3MI15OinA7tt8NduAU3pe35oe9-Hqcs88c-06tWjv7ekB-QkiVnYOXC6en8iH5JLHK1QTvvz2UAAtmQCDdHEXAgL00D_PPXq27HznkByDWEjVXNEajOt51Xw9Cqj72REH_lO_S03sKp85PEmLd5APzPr-9nNhg04it4uy9WHZLgr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=c96kowPVj-trPATXmwPkrzRxMVPi8DYiuC5lBI_HFNje8K8sE4HTQB-zribNdbRAcyy7tQiC0bjf36d5jeAfBUNw4OR-YWj_b3zF3T2PuSzaAlS2qClScT2UYBUDaMuoG19-KwJC9eTGodLohLgjegeb-shBqNQoLWjl3UJr3MI15OinA7tt8NduAU3pe35oe9-Hqcs88c-06tWjv7ekB-QkiVnYOXC6en8iH5JLHK1QTvvz2UAAtmQCDdHEXAgL00D_PPXq27HznkByDWEjVXNEajOt51Xw9Cqj72REH_lO_S03sKp85PEmLd5APzPr-9nNhg04it4uy9WHZLgr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: همهٔ کسانی‌که درگیر مذاکرات هستند، آدم‌هایی‌اند که میدان را به‌خوبی درک می‌کنند
🔹
آقای قالیباف فرمانده میدان بوده‌اند و آقای عراقچی رزمندۀ زمان جنگ.
🔹
نیروهای مسلح دست‌به‌ماشه هستند و تیم دیپلماسی با همین نگاه مذاکرات را دنبال می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/439014" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af89c9ac9c.mp4?token=p-Q0nu5LcGCAgzBSkE6RDE_vHRptyzxhxwLhMLViXm79EAaYNsvdWvRz-b68vMnylV_Jtxlp5hJo87xJvKHckLcx-R-GnGWLzU4FxoMD3x46-v2tmFRGzCSFSxfveQoU9rf4KMja73ehwqzGO2-ctbBPmw6-Xla4QYWaSa2NEf2PKpC_uEDjc-SX0KDmOW6UPu1cf-8dMOSiofbS8KliFjsOinUPiestt_YnnAfe1tqs5LiC-I_9eVwolbQrmrRA5gu17L03EMmj8ijQGaU-dBk4ywp_OgxMNBZ8Za6iccWI92gReUrdeSEt2USEWRYanKvICfYBLCbKhFDdRCyvuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af89c9ac9c.mp4?token=p-Q0nu5LcGCAgzBSkE6RDE_vHRptyzxhxwLhMLViXm79EAaYNsvdWvRz-b68vMnylV_Jtxlp5hJo87xJvKHckLcx-R-GnGWLzU4FxoMD3x46-v2tmFRGzCSFSxfveQoU9rf4KMja73ehwqzGO2-ctbBPmw6-Xla4QYWaSa2NEf2PKpC_uEDjc-SX0KDmOW6UPu1cf-8dMOSiofbS8KliFjsOinUPiestt_YnnAfe1tqs5LiC-I_9eVwolbQrmrRA5gu17L03EMmj8ijQGaU-dBk4ywp_OgxMNBZ8Za6iccWI92gReUrdeSEt2USEWRYanKvICfYBLCbKhFDdRCyvuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
🔹
افزایش مبلغ کالابرگ جزو مطلوبات دولت است اما واقعیت این است که باید خواسته‌ها را با داشته‌ها هماهنگ کنیم.
🔹
باید در این زمینه، مطلوب را با مقدور هماهنگ کنیم. باید بررسی‌ها انجام شود و امیدوار هستیم که…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/439013" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی دولت:‌ افزایش مبلغ کالابرگ در دست بررسی است
🔹
یکی از مهم‌ترین وظایف دولت‌ها این است که تورم را مهار کنند؛ این کار را با نظم مالی و بودجه‌ای که دولت پیشه کرده است دنبال می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/439012" target="_blank">📅 17:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439011">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag4hHsJKEIDqbWFbSaGO0o-ANpenZfnRLDfJoxF-3p1_0CpNOWwJ-eM1V35kSePTrAPhknQTfgJ9G9snpKCzEnI7EKoKRlCVnLsWLQdfbfoWEm0sCnXZqOjWC02bo4gvJ3i77LJ9N58mHVlmLc9dfrW5DxpQSJN6Vt3trSCecYmCT-d2D_guChUdojvwfzy2Oso-3g9F7CrI_g2vpMJbgyNRSsWb1UUz1oD8qMe2Bk7Oi7Xz2tqMTkqFoOJlvc0F3bIE7QE_iNQplutNw8pndsr5AxIr_wcaVtUZXkErg9tQ1x-kTZhQaR0XBoMnc9GqEdQUXyFISdAOEYKki-JWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم ترانزیت کالا به ۲۰.۵ میلیون تن رسید
🔹
براساس جدیدترین آمار گمرک، در سال ۱۴۰۴ مجموع ترانزیت کالا از طریق ایران به ۲۰ میلیون و ۵۱۶ هزار تن رسید که نسبت به ۲ سال قبل خود افزایش نشان می‌دهد.
🔹
عمدهٔ ترانزیت کشور از مسیر ریلی و سپس جاده‌ای انجام می‌شود که کالاهای هند از مسیر ایران به کشورهای ارمنستان، ترکیه و آذربایجان منتقل می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/439011" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9894ffd5.mp4?token=SR5W_f86Ul5W5K4dTaYfXaleEUtRPBvNjqAaJ2k93VheIs7YUypoga9-4kfcCiyCr6GkYz4NsczpxUNwYvEjW5Gp0IFYh38O3C08masRt9y9onlFsemp0lOb6rpjUJ7Hx8fclywXP5ASp47nx9rsHAo9pZsYsbYqIsTXO3KLttvZ2L1pXntZQVQR4oFd084WcOWIFuthN1n5dW4i06K-jgzNKjycMtl9AKWkmAlQfWJeKwT9TTJiDgv3x4UoqWMUDCMnyCo_Gb2Kw4XW3sC_QII7iVYryS-DYSVyOF5sNdYAPW0486qjoq_KrS4cGPEYVd4rb_D0wiEGVR9JNmfw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9894ffd5.mp4?token=SR5W_f86Ul5W5K4dTaYfXaleEUtRPBvNjqAaJ2k93VheIs7YUypoga9-4kfcCiyCr6GkYz4NsczpxUNwYvEjW5Gp0IFYh38O3C08masRt9y9onlFsemp0lOb6rpjUJ7Hx8fclywXP5ASp47nx9rsHAo9pZsYsbYqIsTXO3KLttvZ2L1pXntZQVQR4oFd084WcOWIFuthN1n5dW4i06K-jgzNKjycMtl9AKWkmAlQfWJeKwT9TTJiDgv3x4UoqWMUDCMnyCo_Gb2Kw4XW3sC_QII7iVYryS-DYSVyOF5sNdYAPW0486qjoq_KrS4cGPEYVd4rb_D0wiEGVR9JNmfw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات جنگنده‌های اسرائیلی به یک بیمارستان در جنوب لبنان
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات هوایی اسرائیل به شهر «صور»، ۱۳ نفر از کادر درمان یکی از بیمارستان‌های این شهر زخمی شدند.
🔹
در حال حاضر، حملات هوایی صهیونیست‌ها به «النبطیه» در جنوب لبنان،…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/439009" target="_blank">📅 16:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کشف محمولۀ تجهیزات ضدامنیتی اپتیکی در منطقۀ مرزی ارومیه
🔹
قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه: محمولۀ تجهیزات اپتیکی شامل مقادیر قابل توجهی انواع دوربین‌های پیشرفته و تجهیزات شناسایی با کاربردهای نظامی از گروهک‌های تجزیه‌طلب در روستاهای مرزی ارومیه کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/439008" target="_blank">📅 16:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBjFuuU-Z2V7xvqvBFj9MAddVd1L-RFNWaO8GY-tlBBaYsdlSLn_FamQfzWPifnQgIigrnH8_Qh6dsQzUoF4OFvhnoz0gIlpavrMjozTDGglpEa6KhqwUTDdCFGBwKUUXeLG3JEBcL097uTQpBltQ7WVW73NXBu7rGT3YjP83IBrblPLDrLMWDtAi8ictPj4F4s2eSzbMyFnKfJNeXJEeiMjknTBLvqTaJAUx23514JtWOEi-ZO_GJWXqp9NZK1FNn-5gGtxUjDCI5XbF0x6Zv-ntu3EWZqg-7ZKMW5K3T1Y0ScVv2escFHh6f9cW5nysaPSbBGBUK5IWC608abukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTql2iDfBGMolbHJAQZnuAI_St8mEZ4h1deUAY4E2czFOph6m29owSLhTcR93-FNYMWH_LQ-VSnG54fYknnC1g9wiGAA4qI814YLxEjqYUAUctcageuDkkBLD_a1gcLKii6AGv5POeR_XdcRz_3pNAKVJF3XvRRXKBngQxrwmCUhXFNsZWQejAMnpHaMgyd4k-zwJ05ghufH9NcQfGQk7yR4431gwHxByz6fwvD2Fm22Nn8lVMzWlRm1nhUF5kc08o7kJv9Cj2Rawu9VrIN6pM_dX-hQ3dnL0OTbmh1n6XK5j2ukrmQ9dL-U73jCo2zwDCLhn8ns8cdqILBKvPEriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYrX-HeV9OQ2-T6U_z3KloYBJbVCj5lsJqURzleyT-yR-gurgTA2NWAx0_K5cA_6-c1HVXM1FHURruISrmLR1TiIExiTZJ4xaIWsTeRNYsI11ODTJGLVNNDqvplOZHdr4Wj70Rsu2dd1qKL8GtKhB4FW911LH-hZj3eu70a4TsBvyV6GIL6Y-fb_VZCEL2YYKs4-QVCrancltGpsY1a-l9eWxWdAv0hbsv3rI2HpzeD4wnGHcYC71K3DxVHxNedLtOtSvk1-qqpW9IQx55acneBI8A3GAg3rlR1-WF_l-VmB73-QUHEEPoCD4ksaZvLC8ZVxF_3hWazd_o9uV3Q_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Woci0KQLuEmCE18Sg3FjfJnpm6v1lxMAhqy8MysBcK7Kwr8STaGcU7jFda-sMFuIwUnED8XVmoWsSrbmq1FVeD4AW3nJVvlLtX2BcQBQN_hFijXJo6h9XHIdRV7fec_dALHVjt-mtnYGD1maV6UzqEanQMB-_Jht_Hz_N09Hx5r1Cd33EyrcdaNfw1rzZngWvE0Be0t0VZ_HIlE1VxMRq4JIDOtNDUQpwWbySOFxRaBxGCndoB7ocT3VMsB9rvW6JTnKmU5SvA76ciWQ4s1_xSA33hQo9aEneOTw90I96J57lx2iqmY6WCCDUBFbR4bdoqQUU1PUFSrbSLlUJSClMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_xjFJ0x7myFu6dIk9XWBej_c4AWc4TptLl9xojmnC2T4OzRTApSo1h5N1i7GcVWKUZs4jWLqVaZV1fBM4oRl635W_0Lk9Pf4xMpgTtaBTpiUJsth8wY8zuvPfYsRKlOBP-tjzp-k41C9CtNXWqiI3QLCJcDg9b0x52a1yQey6YGMIYEch7-VInMxvBjeLUw-lYsGAz0tQsqqIwxyDOwlhsD3FWFL2atoMRMucvB4rZR1raCZshRnnh3u3-h6XTz1FHXf3clB5z5l3llUd9qN95ZCzZhMjU1m4aNRhGA-zLu6ef2AHRsh5IQ-OI_WkGxqoPmNXPoJCVqkIJYi5-RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Auc800Kl3sBmUU322PutjS3aZ9_5qY46_A3PVUbJdBoS2jOc3jFSjCVFPPG_1ZAbgmfbxlB7tSFKZZr54Ey05SbVwcF8YQNrhPh3Anm1_tPOYNW_dq-ebAyeAAza8mBwpIrhNNIM5JQ4_dSjqMFRcvDN5__dlqC7ymuFP94h6IaEmDfk-HxBi84DwL8jglZENlDTuXmLG_00PM1UE2QVGEbtRmPxBRiPn_LLEPZebOrCkpRR44LpamCuVvY2RnwIrifP-ptGgleEQ45ThK3JHS0Yx3eQLpNzvN31vK5i7seLpY6_E8FIPQFHsW2YcJCA0-zBRA06qEsHAM1A9caXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSU8rVyllEcGW27LaHYb8J1_8HKjIHgpNSm4ROzrYBtdN3mdZF3VgkanQRsuVFHsd4Rcpb420obOnpiS2aBpcfsAtkuyOOo87Uze0pWOSoz-0TEEEPK_5gC7JVAi2Nj-8h9mbxyTGtw1i0uuHPqoSXPvybpRq648_vgdEbRFwHwjQijNUL71MAoy03OB-3JzIeDAXFDEJW2jf90DqDXSxtmQm0-DHYLDVfPZclgdSH9ohBp_il3XpoVTpBTiQIIkddK4fOFQYULt51a1xyFX7-IgThY8U__GuypNzcFdcTBS4uEFPQZBUEp78Q17-Wz7G1Y-yVgU-PFXhAiwHAVMEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماسوله؛ نگین سبز گردشگری گیلان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/439001" target="_blank">📅 16:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
حملات جنگنده‌های اسرائیلی به یک بیمارستان در جنوب لبنان
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات هوایی اسرائیل به شهر «صور»، ۱۳ نفر از کادر درمان یکی از بیمارستان‌های این شهر زخمی شدند.
🔹
در حال حاضر، حملات هوایی صهیونیست‌ها به «النبطیه» در جنوب لبنان، ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/439000" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pw0zHzXPTWLRqGBXP3Nny2ED_IJAMEBo6Oz3WgG9zI76byRMS2KUSbNY5WqPgBAI0O-aW13GedX7Eq1GS7yUkRQRu6tqYAY35yn7mbf54IZJcD9ohq23GM9GmTReQ7KAkr8trLPcDA-4tZfeKXJiL1i86GAAeTbwf7RwQlGFcawJO1MTgUgBhrDcc1GBqsFCmytFF8tWewi6L6b6JXP2WVXB8FrOO3_dHCKdkbv8MPg6JauRq5XpK0iMnHxepJqaf3ln__CeOV4SUWr8FfaXCgMKKhT9xL-7M_z7yg6I4ZWcAyhIhZqGInudEauunj5w_2eNrXjt4NWw0xFEV_UE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvW6imRHLzFe-FeZbEj9aQzG7OtPIkBJ4mrC_IKEfMAPPwIGTi7w295S_efqhM68PpRjCf_juNNykrrpvlxlJSGh5KmXM_0QOt8GXvzrT41Seuy6KV_roTZh8ZaGGhIeRNQSiBcRj7sLxXeGJvSClxw4qtqe8AK1ZkCNKarTerO_T8BbZc-6GbaWu7VdBMtZkKxiYvhVNarTWgOb2dscpE_0ofkYELpkUKkNJXlI1JVLp4BycRRMQubBD4HyDroQ3aKRFyL0JUQoBMg6M1vb4Ps8YA5l2y00wkmDm40aGUd5aL78Dsqm4SoLwzovUHOyprcR2bG7BIlW3ck7Egqj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpWvhJxyYGFyUomXuGU-eSeowlFg_iDhNciNQe-yz7x51P4WXhMymI0FxVFfJNyQtK9GFbsNPlQt9jXm4-OiOdMytGF4eJrDMMb-GbTYIVvFv9er8dqidaKpu0Cf9PKNSvLJ_8I2xaTja37qBfvPJsa1ho9fFeIGb4TDr1O8kPjbUBGZ3MgiXSJqA9IINePImjmPRiIWwcFADYq54819eJDLola2G80UICi_h2IlvgSi-dbD5qyfa6RiFCCG8AkgCp0-WEsIQJTfhNKmTkg5-dhQHbfp0UaIrI3uIetNlw6eQQF4DuiP3FgQTeB3FlTIs38SeMNwNsOd3K9oh2CHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7WFPYCzQSnaK8atO4GFE92xWIWPYDaNGR-kfRCrBEvHPFqOkCTYQ77BwRQftfFzAcYwla7-2PM5kJPQCQEEKZdHd4L7xitDypBXfzS_kgKqpqlz5CjX76YnE0FAPgPfn2dRDfjsA_QTZ-TMr-oPOTsBpCvaSY8ZWLLdxuZBvAnTHoCpxxMpOB0e65XgLTQ6602fM8kyAfrNhLKmwwMM1LKteGoHULxwSqlb8YAZiKRO5acZ3a9bjFUhdx0TCxJwIq_YOt2_HRhhvEJLyoX1G-B8h4R0b9-hLpizvyEeag7ZBs7XpCTJC-3-1-8u3mNILzuKgvmV6DduRrTV-hskmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنایهٔ حنظله به رئیس اف‌بی‌آی با انتشار تصاویر هک شده
🔹
گروه هکری حنظله در تازه‌ترین اطلاعیه خود، با انتشار تصاویری هک شده از «کاش پاتل» رئیس اف‌بی‌آی، به موضوع جایزهٔ ۱۰ میلیون دلاری تعیین‌شده برای شناسایی و دستگیری اعضای این گروه واکنش نشان داد.
🔹
در این پیام آمده است: کاش پاتل عزیز، بی‌خیال دیدارهایت با یوسی؛ جدی بگو، آن جایزهٔ ۱۰ میلیون دلاری که برای دستگیری اعضای حنظله تعیین کرده بودی را چه زمانی قرار است پرداخت کنی؟
🔹
در پایان این پیام نیز تأکید شده است: ما همچنان منتظریم؛ فقط وعده‌هایت را فراموش نکن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/438996" target="_blank">📅 16:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1lz9dzuHmjX5MKwyqk5kUIiyaFVEHXM6i4lGTMB5dDuO9ErwmqgLu4V9kurHWNfAEQT6BzgRniMtviwRPOBXjSmMhuIY9AAu_AtmOjk4D_OHa3Me1-zfWhN0NfsG_NhwrUTg19I-LrxpDAO4K_3vjMTJ7SSV1RFap7H5Rdps-um_h6gaiBiuPOMsfiLuJMUQECPtcNakSUjYZ8PowN0Hff1Yl2Yrcc55OzlUgivwcAZ38mdg4-KKaD6SVuB0Aqz9x8sxZzIZ7v8itV_xTdPEVO8uZgm4Nyu3K05ucUv4A12MJCpMtoEEXKbnkvs_g3Lj4-3QsCEPi8QmpNQ0OfXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ازای هر ایرانی روزانه ۲ نخ سیگار دود می‌شود!
🔹
معاون وزیر بهداشت: در ایران سالانه حدود ۷۷ میلیارد نخ سیگار مصرف می‌شود؛ یعنی به‌طور متوسط روزانه به ازای هر ایرانی حدود ۲ نخ سیگار.
🔹
چیزی به‌نام سیگار تفننی وجود ندارد؛ حتی یک‌بار مصرف به‌خصوص در نوجوانان می‌تواند زمینه وابستگی و اعتیاد به سیگار را ایجاد کند.
مصرف دخانیات در گروه‌های سنی مختلف چقدر رشد داشته؟
۱۸ تا ۲۴ سال:
🔸
مصرف دخانیات در مردان: ۳۴٪ افزایش
🔸
مصرف دخانیات در زنان: ۹۰٪ افزایش
۲۵ تا ۳۴ سال:
🔹
مصرف دخانیات در مردان: ۱۹.۶٪ افزایش
🔹
مصرف دخانیات در زنان: ۹۰.۸٪ افزایش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/438995" target="_blank">📅 16:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnHKrVbGLsJanI8NjJsX1Rn9z7Ew92aGM6WdTuImInhvAB8jIEbtibW6bWfZn3CwuB1VmJjETNU9hsIlIvquh89cBZoCgUkpGjMl3tDh1lQOKdSYQGI6H1UvmmcTe3hwtML4H3MvtaW93kkawg0xOMf7I9L-sbMNXc60L2jOj7x8Og-9JDJa5VyhzMVbDOsFWyFa9z154IBoiDSQ2LrL_OY-759tX6yu3MQLSYgixb_hRtXsqryh5PbcOrkA9KVjcNnIxYRoKeYGAgaInDu3cBu_olZHYNliTFrvO5qzFnT5w7cDeqK6Hggo_0m10vhlTKwQzTQgMKAdEbVR82h3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogJYZpm6CfVUKea-rGPYA61x6tG_L_kMKSefPe6Lhn2Ypzft3Mf5GyZ1JvwLedTH1OEIIsdtHyU_X9jvxfiJv7hNeWyzvNH_jfA0sLAu9LmNzc_CbKX5iIzuPJH8cLVk0FeI9OSHI9_ZeKCHjmgTtgA4hTrfE_zTHvRdknMYYZJK3pCSSX-ggTLm7n2irdU8o8HxQUDRNXK4C4qy37t8Le1NVF90RjEV1qwrD9f2p9RTOJk9gjS1mS5IqkNCr5KhvcRpP2vfddeC39b75olLh7GeJP4BQbv1aXNGXU_dgxu1y_-GzQPRZIcsLDAsmZPMsu7E22UXd4stluUx4WOLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdMPZqkLGNbGPt2oWZ2FUz3C56bAZtkhW9IcEravvEQMv5RoZw4LU2ExWL1eOJnyBoXlvw-sLKGhlKy-q71Nm05i5uHRj4Kr9ZcrbDmCKsU1gM9-Gzjd494Zhyn3muxB6E_jbieSzZ4iZcPBKCdDwYalGyBWxRUA69mhJ2wTKXh90ZyNHb0MfFSDcEpQCFwVct62QC08XliVIzpb4Ux0LXp3RJI_TCVzz_RGXWtKRrYRbdEQ8QX9b8tOJtbd_IiNjMF6AvqJClEvJ2Nd1pPuPq-6EC9JZKBuopd3Q-_ybJ8349I34Pc0jmV4dochVhjcD46vJ_NRGXEDqqNh5eF8sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسب ۳ مدال توسط آزادکاران ایران
🔹
مهدی دمیرچلی در وزن ۴۵ کیلوگرم و بنیامین آشفته در وزن ۵۱ کیلوگرم کشتی آزاد نوجوانان آسیا موفق به کسب مدال طلا شدند.
🔹
امیرعلی راغب نیز در وزن ۴۸ کیلوگرم با شکست مقابل رغیب ازبکستانی در فینال، به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/438992" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edae0f30ff.mp4?token=eJriAfnylaN2i6-LWaFh-hpPLgH5_Cz8gBtZqXfDtFU9sETFBi_eeBRjZYDXEqJUPfixBAbzEnzk76o7CF0NACRWXJJf3jYBZXyIYQbbfSKhGE8Rqfd0w_5T5HlnaVo4IwAxOQOmx6ayWUDUWd-6UiVNje6NkLao0vFaQtAWHDKzAMV4vKM8n9khxBNjAM8ptjzp_2s5kVqm1En5okJT5frotFs1TTmXyB71NJyX1FzYMDrztun4N4Zb7dt4Df6w-8hkhKR2fU3RCNUwHocdBopv9jzNHcHR7tMhJlerp0Q2J_wNsAUQmIiLVyoF2_cSoKHhYAiwFpx8EyeYCRTdkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edae0f30ff.mp4?token=eJriAfnylaN2i6-LWaFh-hpPLgH5_Cz8gBtZqXfDtFU9sETFBi_eeBRjZYDXEqJUPfixBAbzEnzk76o7CF0NACRWXJJf3jYBZXyIYQbbfSKhGE8Rqfd0w_5T5HlnaVo4IwAxOQOmx6ayWUDUWd-6UiVNje6NkLao0vFaQtAWHDKzAMV4vKM8n9khxBNjAM8ptjzp_2s5kVqm1En5okJT5frotFs1TTmXyB71NJyX1FzYMDrztun4N4Zb7dt4Df6w-8hkhKR2fU3RCNUwHocdBopv9jzNHcHR7tMhJlerp0Q2J_wNsAUQmIiLVyoF2_cSoKHhYAiwFpx8EyeYCRTdkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گنجی: حاکم‌شدن نگاه عیسی ‌کلانتری در حاکمیت «سم» است
🔹
کارشناس ارشد مسائل سیاسی: کوچک کردن نگاه به آمریکا در شخص ترامپ، یک کج‌فهمی سیاسی آشکار است. مسئله ما با آمریکا مادیات  نیست، بلکه مسئله بر سر «وجود» است.
🔹
کسی که می‌گوید «در حلقوم ترامپ پول بریزیم تا پی کارش برود»، مسئله ایران با غرب را به شدت ساده‌اندیشانه می‌بیند
🔹
برجام سال‌ها پیش اثبات کرد که موضوع هسته‌ای صرفاً یک بهانه بوده و مسئله آمریکا با ما یک مسئله وجودی است.
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/438991" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbd9b8a8e.mp4?token=utFyYU0A7tPCCacNz2Ltxycnq88KmFN4_4B_rrIE5uT5HuLoFaxULWu-aOmkTORPK__TMjHp5ObY6JcXuLme4cyiQGz9M9-hAyHq6W35xPQTyr2q8tWU_AURLrqeC_7UNmVjlHPD-fcwRqbW8He1hiEo4kGav33QR2GgN6-r5sunAh-Uop3oM86YteTi7ZVT-LoeStwHqR94-UBUoeat1-29BpGZR-cwqiTAIdCTKO0j0XAWTbujbxQargSL7GQCM03XwIi9wZchX0fvY-sS9P8ZHB3QAfFDUjsZZyZri8tTLFBzEWKB7mj91M3OPHc6yHfzHacpHa695nSeEDWcEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbd9b8a8e.mp4?token=utFyYU0A7tPCCacNz2Ltxycnq88KmFN4_4B_rrIE5uT5HuLoFaxULWu-aOmkTORPK__TMjHp5ObY6JcXuLme4cyiQGz9M9-hAyHq6W35xPQTyr2q8tWU_AURLrqeC_7UNmVjlHPD-fcwRqbW8He1hiEo4kGav33QR2GgN6-r5sunAh-Uop3oM86YteTi7ZVT-LoeStwHqR94-UBUoeat1-29BpGZR-cwqiTAIdCTKO0j0XAWTbujbxQargSL7GQCM03XwIi9wZchX0fvY-sS9P8ZHB3QAfFDUjsZZyZri8tTLFBzEWKB7mj91M3OPHc6yHfzHacpHa695nSeEDWcEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از دیدار اهالی رسانه با خانوادهٔ سردار شهید سیدعلی موسوی از پیشکسوتان گردان تخریب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/438990" target="_blank">📅 15:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159b83282d.mp4?token=LZdQ7UHEpdYA90FjQU10VHmetEuY9zckW0oQHLDx8tkBSo2TZGqm443Rp0FQ69jOSgcL9wD1Wsl6vVfTEyXXNGPuy3pIvEEIDHp_Y_5sCDTalo0Nxtk3595oicybTDeKS1-n1VBF42rgYp2lol_SzQgksAAkobzSn_evvCAGdZcCvo5hWBJSYnk4Pr5uNaHccWvX5EkXaGbzsWjr15thqSweks51PQedme_F8hFJcfqqBc2_dNFdSKOSafWvlZhena_PxQeEJRQif6ycLcQRwB_5s2ZV34siu7ZBwIpRMKvX5qZVbhmUPT2F4DUVqSLFHhLabI76u42g4Q6Gvt2z5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159b83282d.mp4?token=LZdQ7UHEpdYA90FjQU10VHmetEuY9zckW0oQHLDx8tkBSo2TZGqm443Rp0FQ69jOSgcL9wD1Wsl6vVfTEyXXNGPuy3pIvEEIDHp_Y_5sCDTalo0Nxtk3595oicybTDeKS1-n1VBF42rgYp2lol_SzQgksAAkobzSn_evvCAGdZcCvo5hWBJSYnk4Pr5uNaHccWvX5EkXaGbzsWjr15thqSweks51PQedme_F8hFJcfqqBc2_dNFdSKOSafWvlZhena_PxQeEJRQif6ycLcQRwB_5s2ZV34siu7ZBwIpRMKvX5qZVbhmUPT2F4DUVqSLFHhLabI76u42g4Q6Gvt2z5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی: برای شادی دل مردم سخت تلاش کردم و مدال طلا را به شهدای مظلوم میناب تقدیم می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/438989" target="_blank">📅 15:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOVHGcrCrS4qFaBlIdKgjXxHjBFCmi2guc5AXDMB_-cDzlScPKHm1X6apad2oh8V8s5vaMpj-rEjLOyU-AhO09OG1rNcp7FMgdeTPXf2YSlODoZ4bS5DSwvX1iT03yTR961vRNsuseC1IiYw7YE1_FqDTY0z_kgrni-TD80r9_tUYnslxn0oqwhHCIQWFVNnMj4WuddGXlj1SEdOs1gGKHQFOf_bnMrHgioF_ulVfz__WBnuYiUvzTwWHCHD1nUtrvKNs-Koy6X2so8dFBC-5FFykVWyExgna3h3u6TB_YvwMcQD84_5SGo6YczUKMsTawzWEeIJqzbImqzXCw0Zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامهٔ مجید واشقانی توقیف شد
🔹
برنامه «به من چه؟» با اجرای مجید واشقانی که در سکوی روبیکا منتشر می‌شد، از دسترس کاربران خارج شد.
🔸
این برنامه در روزهای گذشته به‌دلیل محتوای ارائه‌شده و پوشش برخی شرکت‌کنندگان حاشیه‌ساز شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/438988" target="_blank">📅 15:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nllKq95XiUrXbUHqBVIYhydU66KEYjc19nLrJ-0GBqdJAUpH_NZwQc7zaC235_JkJDF39ODlO4YcqfEKi8wDcmwzpi707fSYkgbwms0tInX8Q9Z8y82W-LKND9cmG4wRzKfYF-spWdayEWtcXVqp0Y9wQAoBfQq69NubqUKEj58s4B1jT7zK0UVz5YiozRCQjmz5DkEdqJVZd4-g2SP9pKjQ2_27fR6GW4xmufqRZFJwyiItxZVAUgP1iKstNToTrcRBIWLAC_dSS-OAvQZxuamfv-FqVI1PZ3fznvLQ6xgbxh2uHtj4WIVDhdplE3vSXE2hz0iRg949n1770Us8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع برق ۱۴۲ ادارۀ پرمصرف در خوزستان
🔹
شرکت توزیع برق خوزستان: برق ۱۴۲ ادارۀ پرمصرف در سطح استان از طریق کنتورهای هوشمند قطع شد.
🔸
ادارات موظف‌اند در ساعات کاری ۲۵ درصد و پس از ساعات اداری ۶۰ درصد نسبت به حداکثر مصرف در ساعات اداری همان روز، مصرف برق خود را کاهش دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/438987" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=MfFAQeXUEkhzrTU28lLJjIR4Xl_97HWojJkVFWgvEKfyQJlqrzP_nIKjRysGX4fOiPYnaZhh75R8K1HUMffGhSvfQT6SefbCNv-dwrkafCPnT7aaV7R4rAqZSfYrJ8msCQe7M7Uo1Z1kc401XGGu_0RZ3L-tMlkknF8pcTi_mOuBZU6nvCqszUS24pxIlvgdUHOcVzhRpKAhTCcSnVOgXyo64b7OqmG-NKNxDXfcIEKSaMroEiAVDWjQ-4U_g_khNmerv_uqt0YgUXzOo9e9sVlDaJqmIdqOoF13Z1lrRkmdBhb7NeQXOyus6W33OSgTsIJgDGBxN7DipZmFOjFuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=MfFAQeXUEkhzrTU28lLJjIR4Xl_97HWojJkVFWgvEKfyQJlqrzP_nIKjRysGX4fOiPYnaZhh75R8K1HUMffGhSvfQT6SefbCNv-dwrkafCPnT7aaV7R4rAqZSfYrJ8msCQe7M7Uo1Z1kc401XGGu_0RZ3L-tMlkknF8pcTi_mOuBZU6nvCqszUS24pxIlvgdUHOcVzhRpKAhTCcSnVOgXyo64b7OqmG-NKNxDXfcIEKSaMroEiAVDWjQ-4U_g_khNmerv_uqt0YgUXzOo9e9sVlDaJqmIdqOoF13Z1lrRkmdBhb7NeQXOyus6W33OSgTsIJgDGBxN7DipZmFOjFuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) مهیای عید غدیر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/438986" target="_blank">📅 14:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51caaa430e.mp4?token=Un2-HAjjUHJ1Sjiu2by7cqKgvUTV6Zq3zZvX4zr3hsfwSF8O1uYKK1ZTPoQCH5mMrixMoEOA613uOa4w84a_9D89t-Q4ljfrr-x4ZHLPMAeEdHG1GKJYIpkCA4wepddKMQPOm8jpzVoFaBqeyIbWDMD383rxQUbTJuENAX9vEqbdp5kakkgEd0d1zEKfEHGu8pUncnGonlMAY7e4woft3igi_utiIegVGIZAfxMFDY4MDlbdIBRVMS0tMolqbsWJWormClMwVR_XcQmiD_AVbbSoQRvsS3xYE7xV7zPcdryz81XmQvBpihjNE4uDRvw9T1uh54Y4-sc7HXorkZopcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51caaa430e.mp4?token=Un2-HAjjUHJ1Sjiu2by7cqKgvUTV6Zq3zZvX4zr3hsfwSF8O1uYKK1ZTPoQCH5mMrixMoEOA613uOa4w84a_9D89t-Q4ljfrr-x4ZHLPMAeEdHG1GKJYIpkCA4wepddKMQPOm8jpzVoFaBqeyIbWDMD383rxQUbTJuENAX9vEqbdp5kakkgEd0d1zEKfEHGu8pUncnGonlMAY7e4woft3igi_utiIegVGIZAfxMFDY4MDlbdIBRVMS0tMolqbsWJWormClMwVR_XcQmiD_AVbbSoQRvsS3xYE7xV7zPcdryz81XmQvBpihjNE4uDRvw9T1uh54Y4-sc7HXorkZopcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای شهید بارها درباره جشن ۱۰ کیلومتری صحبت کردند
🔹
جشن‌های کیلومتری عید غدیر جزو معدود رویدادهای ایران بود که بارها و بارها در میان کلام رهبر شهید به آن اشاره شد و مورد تاکید قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/438985" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvbLSIUNzAVVCh_XcHuIGrzRFtq67CdI7MbOOJu-P7wcBeB5fH7rUAgG_2FMogepEOQJ6F2VR40gYY7DWW7y_-ZOSBRr1VnaaexYrBRFFuL_mzLFuUFiiV0dBFrxACNi4XEanHyAU6ZRbbmzawo5P-P3RP3fak8rOljpsN45SdCYZqEtkUWVFE0LEACWpDoimxZC2AxYXesf1HUlp7OyEJPYK5O1P07JFJ6Hr6toTDn_6S9wdb8WhZ7s0FfvDzwHJo9dnxS0AmJrvHBSYkfme-Hsp7OuhZSg4Wj1wdNa8638lmAzMlSpGpSo60qaUUY8g_RSWwW-yM6GAvLzK1nzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک صادرات ایران؛ پیشران تأمین مالی توسعه زنجیره سلامت در اقتصاد بازسازی و جهش پساجنگ
🔹
در چارچوب گذار اقتصاد ایران از شرایط جنگی به اقتصاد بازسازی و توسعه، بانک صادرات ایران با حضور راهبردی و فراگیر در زنجیره‌های حیاتی کشور، نقش خود را به عنوان موتور محرک تأمین مالی ایران تثبیت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/438984" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9Hm8jjbfYbkJAoAKZbK3an57O-WW4Qt8wXCJzvVYzibSK4PTvPNC4AXqSOdwF6wmUCDSemFwmXq5OTZdvPjJHf6DNkT5b-KuMNZl1VtoLV7J9JPtJoKoF3m1EfWkskqssHHY3UOfXTnqVXwlVdOWBavf0y8IBuuWv7Jr4pfXBMN_-ChpxwjbTmOPBC9MPFMgh1nryx65L7QwMVgDqQx9QsacJx1R2XndQT6T1k6KoaWC5mU_5toFcNWVdHRzY3ZNmoqyTDI0i8ABweI3vzW2-zGd6xHRALrA8od4D2b7UwAHSC3vPqOiucbw300bYOyjuQ8f8JdMYteJTSFVd38FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ماشینت رو 1 روزه بفروش
🔴
بدون دوندگی ، بدون معطلی و کار اداری
👌🏻
فقط کافیه اطلاعات ماشینتون رو اینجا وارد کنید.
👇🏻
👇🏻
https://ck.chavosh.org/click/03b3be14-2aa0-482f-b9d8-2dd6bc031d03</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/438983" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/438982" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردهٔ دشمن در بندرعباس از فردا به‌مدت ۳ روز آغاز می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/438981" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0kgLbFs2Vz9edpFwSUBq54Cc-VLEJt2wqI0R3uYzjJnDlBqEm_DwWwSoIatdku7HVuLNfwr5Gqn41q0yQS5scXneeuFLslD-Q9TLvKZcKIcxTa9Bo0405VdEZBSXphReoqAdRg7U5tzMeQRfioOC7jGMxsfAZs-aZzldC3tYum6Xak29BamCJkml-zYwCgpjB9IJeUoeQ6p8hSelSTEfVEp-6ZTa4PqK2kqY5OsVnavetbQUSgstsO4BvYVn5sq8TdO4NOPK-YnyMQFiCqI9AAAFxP2_IiwcexC9Z8zF5v8tHzKwSfcBHf_GvPwmUkEVm2Xl4cB_861csGd0vh2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودرو با پلاک مناطق آزاد در سراسر کشور مجاز شد
🔹
رئیس پلیس راهور فراجا: خودروهای دارای پلاک مناطق آزاد ماکو، کیش، قشم، چابهار و اروند که در شرایط خاص عملیاتی قرار داشتند، فعلاً بدون نیاز به تبدیل پلاک به پلاک ملی و در قالب «گذر موقت» می‌توانند در سراسر کشور تردد کنند.
🔹
این مجوز که قرار بود تا اردیبهشت‌ اعتبار داشته باشد، به‌دلیل ضرورت حفظ ثبات پس از برقراری آتش‌بس، تا زمان عادی‌سازی کامل شرایط کشور تمدید شده است.
🔹
با این حال، این خودروها از قوانین راهنمایی و رانندگی مستثنی نیستند و در صورت تخلف یا وقوع تصادف، مانند سایر وسایل نقلیه مشمول جریمه و مسئولیت‌های قانونی خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/438980" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf800ac63.mp4?token=Qxjx8rKQVmP0eUTAZ70zlHpxpaScOcR6hcFKfqqW96STkm7xaLL4_Xpk7ErJKVDOaJUIHxw-Cnh63VUrlg0kvL8SCDaSq-6O_Srkdyc8bXjtqKu-bM0aylo2dhirHI6mp0ZAWwFS3G_buzkCyO2pi_f6wr4nM4OL8bPnpwy8wSqlin7sQ3_Tc3UP7a3vfApy4pOZfgpb3hAbeR-UMoZJzlB9eMyNFruQVGROVYoMPKaAXRBApAnqNskBaTQ15Dl6a9V00T7Euw1NhIAtA86bwcTyA1y47h3qf16tHEpxSCJSIQ4zOpWpw9EPTBnBk59T6T3RxpqIZ-2rpni5WeacEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf800ac63.mp4?token=Qxjx8rKQVmP0eUTAZ70zlHpxpaScOcR6hcFKfqqW96STkm7xaLL4_Xpk7ErJKVDOaJUIHxw-Cnh63VUrlg0kvL8SCDaSq-6O_Srkdyc8bXjtqKu-bM0aylo2dhirHI6mp0ZAWwFS3G_buzkCyO2pi_f6wr4nM4OL8bPnpwy8wSqlin7sQ3_Tc3UP7a3vfApy4pOZfgpb3hAbeR-UMoZJzlB9eMyNFruQVGROVYoMPKaAXRBApAnqNskBaTQ15Dl6a9V00T7Euw1NhIAtA86bwcTyA1y47h3qf16tHEpxSCJSIQ4zOpWpw9EPTBnBk59T6T3RxpqIZ-2rpni5WeacEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
رفتار وحشیانهٔ پلیس هلند با یک پناهجوی باردار
🔹
انتشار تصاویر برخورد خشن پلیس هلند با یک زن باردار در مرکز پناهجویان شهر «زایست» موجی از خشم و انتقاد را در این کشور برانگیخته است.
🔹
در تصاویر منتشرشده، یک مأمور پلیس این زن باردار را با خشونت به زمین می‌اندازد و چند مأمور پلیس همسر او را که تلاش کرده بود از او دفاع کند، با ضرب‌وشتم دستگیر می‌کنند.
🔹
این زن اعلام کرده که نیروهای پلیس در یک مرکز مهاجرتی که شوهر فلسطینی‌اش در آن بازداشت شده بود، به او حمله کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/438979" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438977">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59279530e.mp4?token=p9Tv3uoKsy3F5KJhAZWNoOlGu2v1DqM3_Va0mWrG1b3PWYTpuQ8LTakGJiaVpRWgGSsgEFE8yIVHm6_JgyLJpcdEzvy4kyttQrJQRoaNUJ0qDNy-lAOovruptkjih5WkuGSIKrRTFoN20jAJn1elupK7nUfZPfEva9h0JCu1r66sz6FZ3BpJsTe0OHL5iu1vRjcbXl8pjDblz18vGUEQArKzCB0UUmJyxgBZ945GwVr-Q7MeL0pHSRDMm0AE9PTl3mdy9dH99bLHk5coqZ-wStUbDtDNxZ9Gc1uIb7n4Mr6s_lq6NUjdE5NYhQKEaO4WLO77GJVPa6YKFVLd-j04vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59279530e.mp4?token=p9Tv3uoKsy3F5KJhAZWNoOlGu2v1DqM3_Va0mWrG1b3PWYTpuQ8LTakGJiaVpRWgGSsgEFE8yIVHm6_JgyLJpcdEzvy4kyttQrJQRoaNUJ0qDNy-lAOovruptkjih5WkuGSIKrRTFoN20jAJn1elupK7nUfZPfEva9h0JCu1r66sz6FZ3BpJsTe0OHL5iu1vRjcbXl8pjDblz18vGUEQArKzCB0UUmJyxgBZ945GwVr-Q7MeL0pHSRDMm0AE9PTl3mdy9dH99bLHk5coqZ-wStUbDtDNxZ9Gc1uIb7n4Mr6s_lq6NUjdE5NYhQKEaO4WLO77GJVPa6YKFVLd-j04vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس فردا میزبان‌ وزیر راه خواهد بود
🔹
سخنگوی هیئت‌رئیسۀ مجلس: یکشنبه نشست وبیناری مجلس با حضور وزیر راه و شهرسازی با محوریت بازسازی اماکن خسارت‌دیدۀ ناشی از جنگ تحمیلی سوم برگزار می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/438977" target="_blank">📅 14:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438976">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8977a3e4cb.mp4?token=OhmeIMQpASlyvwbWkWVYYd7xLcD1EUX-xZDX8TM3epKSLRsPzfHZWDgjdoIHJvWy8f1iVIz9LAoyOjgdHq2DAu0qHU17GZuIO-XIszWZDu-V0lW9c45K544_KsgmFPOmkYWOdjEUUMQct7i8Ypm7zd0ML3XfX_JaIwCTepaIdOwsRy9WGXTSd4oXkZDXR6JnrhcHQzq927sGWqA83jzJtRxImICpnsN0PkvSttVAuUkHoHFxEUgkZOG3ZspOCkijhOrQ3IlvslT3aIBz5LdBqiM8CHcjemhC7i4uPC-lkKzEHKHKP5STpBchXwFPwJsMtD7tukxGTJApwjb2j1r2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8977a3e4cb.mp4?token=OhmeIMQpASlyvwbWkWVYYd7xLcD1EUX-xZDX8TM3epKSLRsPzfHZWDgjdoIHJvWy8f1iVIz9LAoyOjgdHq2DAu0qHU17GZuIO-XIszWZDu-V0lW9c45K544_KsgmFPOmkYWOdjEUUMQct7i8Ypm7zd0ML3XfX_JaIwCTepaIdOwsRy9WGXTSd4oXkZDXR6JnrhcHQzq927sGWqA83jzJtRxImICpnsN0PkvSttVAuUkHoHFxEUgkZOG3ZspOCkijhOrQ3IlvslT3aIBz5LdBqiM8CHcjemhC7i4uPC-lkKzEHKHKP5STpBchXwFPwJsMtD7tukxGTJApwjb2j1r2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که ترامپ از تاریخ نگرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/438976" target="_blank">📅 14:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438975">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw9SBof92-qFRiI2EtKrnlZlL-UfFUM5SOgxRDIdAwVWbuL7v3KaLeYnc-iiDCdHtzA-YtmScrTN4xZOoFNvbQbrHpZb1WODsEQst1iTYzCRmGRvpe9VCgD_hM82gWAHt-vq74RlueH_qiFF7kgHCHlIb9h3xe0HDiu_GEn_8b0MLLkGHhS_PNcl8R8PErrM1ne9toBqlft3teVsFJme5T6-bhoRkkgx_FN3l0Ebojko_Ozuk-P54aOWLrPBr1fNUIqnLb4lfDPJWQg4UwEOLOomxHLLy_mp7bodxH-qDcn7V_goc8ZcxFcD5b3AU7c6Pi1TqSyl-cq9n6MG9bQ9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز هم مثبت بود
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۳ هزار واحدی به ۴ میلیون و ۲۳۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/438975" target="_blank">📅 13:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438974">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=Azk-97FnvMXjCMqfM-d2L9SCq3Z7li1NMOb_M-ayZzVLqwezDgE5YTzM0CMlPg9Zy4wMVvg2OwSrwElTL34NdkSqGzcJXz3dgMGbN3XLrqrI1d2pws-hCvJA5d6Y24-lYWd1t5aJw1L6ft7J1c4wfVZmVpRKOP7ltce350rpR89H3Cp3aQLUeYLvZBjXi6NeWFIadkQqsY51MrKwNgtdc_3svA2krCOdkysZBewWukGNwwDSEr-aPH7x-imyq1RbSjmT5MpaBeZ0pSxgOfmbG47OuCzXp70_GqC3xcTk-16YVXlcf2AveIIMms8lfyQ2eV84PHn7AyuhFIB8vmOGHSKOPVNhPKXXWSjTdB6GR_MJHnb_UV18KPE9Ftl7sTKg-3m53aEbWL1744u8IkEMc6bd8qQcoVVa25WXFga_anExnR5TdO7hNrwnHD8g3tNjxUR14RXXnipsbh5siDo7oMf2vlkty4XfL79oIGkfep4Tw817t2XL7uMRH9LwXF8g1RzyNM_Fq27xh323nynibkJDMtVa_3pAxrqWsPDMETc2zLnXLst0EJdXOTgJvfBwl9EYtECeenYWmd9H4jp5qmsvuQumLjgndgfrBApMQ71meYaRvCaupw9y0Ti0mmSKsnIkLzatSldwzzMPRfSHZgPIAjzWQtY3gzK5KLsAzg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=Azk-97FnvMXjCMqfM-d2L9SCq3Z7li1NMOb_M-ayZzVLqwezDgE5YTzM0CMlPg9Zy4wMVvg2OwSrwElTL34NdkSqGzcJXz3dgMGbN3XLrqrI1d2pws-hCvJA5d6Y24-lYWd1t5aJw1L6ft7J1c4wfVZmVpRKOP7ltce350rpR89H3Cp3aQLUeYLvZBjXi6NeWFIadkQqsY51MrKwNgtdc_3svA2krCOdkysZBewWukGNwwDSEr-aPH7x-imyq1RbSjmT5MpaBeZ0pSxgOfmbG47OuCzXp70_GqC3xcTk-16YVXlcf2AveIIMms8lfyQ2eV84PHn7AyuhFIB8vmOGHSKOPVNhPKXXWSjTdB6GR_MJHnb_UV18KPE9Ftl7sTKg-3m53aEbWL1744u8IkEMc6bd8qQcoVVa25WXFga_anExnR5TdO7hNrwnHD8g3tNjxUR14RXXnipsbh5siDo7oMf2vlkty4XfL79oIGkfep4Tw817t2XL7uMRH9LwXF8g1RzyNM_Fq27xh323nynibkJDMtVa_3pAxrqWsPDMETc2zLnXLst0EJdXOTgJvfBwl9EYtECeenYWmd9H4jp5qmsvuQumLjgndgfrBApMQ71meYaRvCaupw9y0Ti0mmSKsnIkLzatSldwzzMPRfSHZgPIAjzWQtY3gzK5KLsAzg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌مجلس: خود و همکارانم را به پرهیز از اختلافات پوچ سیاسی که مورد تاکید رهبر انقلاب است توصیه می‌کنم
🔹
تعریف رعایت نعمت عظیم وحدت ملی به‌عنوان یکی ‌از مصادیق ‌تقوای ‌فردی، نشانۀ نگاه عمیق ایشان به پیوند ملاحظات اجتماعی و سیاسی با الزامات دینی است.
🔹
ایشان…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/438974" target="_blank">📅 13:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438973">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
هشدارهای حملهٔ موشکی هم در نهاریا فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/438973" target="_blank">📅 13:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438972">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ae4f51b4.mp4?token=dY4gxoZK8iWTL0XUQHstlBMp7c4n10KiMqhhw5A6fEmGDwE_DG4ZXC9r8YTk0_12mihHfGTLl5dZRkUK8uoAb9F8hzE9kKxbtc2Ns99g9tHvaJua425ewAx2gAtNwZzeAY1sVh1yZ2B5R0mr3Pjlz-vcfDBGa8BZNAVYrFDW-rP3VaajProjeP81zvMUcGeH-InzuSAI04Qq8aj-MrzuPwRDA0sqEtp81OuJvlowYZ_TQRw_rdsZqJV5Agp-5waYpbj1pPlHf73mZohnxJWpRlY3H9GSX2n0UZtrjmB0Pwr1XOwCdm3FFEFTjCLQlkjEPbabE_6qORRooQ6K9_iTZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ae4f51b4.mp4?token=dY4gxoZK8iWTL0XUQHstlBMp7c4n10KiMqhhw5A6fEmGDwE_DG4ZXC9r8YTk0_12mihHfGTLl5dZRkUK8uoAb9F8hzE9kKxbtc2Ns99g9tHvaJua425ewAx2gAtNwZzeAY1sVh1yZ2B5R0mr3Pjlz-vcfDBGa8BZNAVYrFDW-rP3VaajProjeP81zvMUcGeH-InzuSAI04Qq8aj-MrzuPwRDA0sqEtp81OuJvlowYZ_TQRw_rdsZqJV5Agp-5waYpbj1pPlHf73mZohnxJWpRlY3H9GSX2n0UZtrjmB0Pwr1XOwCdm3FFEFTjCLQlkjEPbabE_6qORRooQ6K9_iTZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی شهرداری تهران: در واحدهایی که نیاز به «تخریب و نوسازی» دارند حدود ۴۰ درصد پیشرفت حاصل شده است.
🔹
اینجا، پیشرفت به‌معنای انعقاد تفاهم‌نامه میان مالکان و پیمانکار، صدور پروانۀ ساختمانی و قرار داشتن بخشی از پرونده‌ها در مرحلۀ تأیید نقشه است.
🔹
۶۰ درصد…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/438972" target="_blank">📅 13:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438971">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3425e9770.mp4?token=DO1o6rT2fOeyjUueOpalLNj-eeyvRF4-diwsRxnMk55phSUKoR-dODZXXh65i9rHzXfrOYnUrqNe9cGxZPHgf7HN-_Y5u8833EAzg8ZSU6qpHKAF_p6t2NVAxZocGIHyEyKw4vmbAyT_QEL6GtKMfjRtUtpk6gfYALeH7GZJzeJA07WNJgwEfiV9zM4g6F-gilJYX_rSiXLHyQeIUvZ8Bwut0m4r8XfK4XXtpZ7OG0-JTZz_RpJGyunc7OB9MwJkxKerU98egazpQxU8sBt96FGDMoWWaO_ekZLcKTuBk8GTCIvGY9yQup0yT0Zn8mwRIX-WWjzHaz1SWHJyeNUAXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3425e9770.mp4?token=DO1o6rT2fOeyjUueOpalLNj-eeyvRF4-diwsRxnMk55phSUKoR-dODZXXh65i9rHzXfrOYnUrqNe9cGxZPHgf7HN-_Y5u8833EAzg8ZSU6qpHKAF_p6t2NVAxZocGIHyEyKw4vmbAyT_QEL6GtKMfjRtUtpk6gfYALeH7GZJzeJA07WNJgwEfiV9zM4g6F-gilJYX_rSiXLHyQeIUvZ8Bwut0m4r8XfK4XXtpZ7OG0-JTZz_RpJGyunc7OB9MwJkxKerU98egazpQxU8sBt96FGDMoWWaO_ekZLcKTuBk8GTCIvGY9yQup0yT0Zn8mwRIX-WWjzHaz1SWHJyeNUAXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اگرچه از دست دادن امام شهید برایمان سخت است ولی دلگرم به مدیریت و رهبری خلف صالح ایشان هستیم
🔹
هر سال این روزها که می‌شد دل به دیدار صمیمانه و راهبردی با ایشان خوش می‌کردیم و برای یک سال تلاش و مجاهدت در سنگر قانون‌گذاری آماده می‌شدیم اما هرقدر…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/438971" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438970">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e83b13a7.mp4?token=hDU8zuu4CnWpOuv7Dzt4V3B-bi5VhWUQlblo5sZmSrDpMwyDSmwU8alacEIJQRrRU5iEs42mi6gK0aMYci_9OPdrBIPAlklrLOJWN_dbjTq5lapILZ_L2sPUHc1KLY3PmGrBbzTlgYovpzFj_-goT7HL5rHMwaGiWjAHcsdUCjmIcJFLM8fP45GukpOo9B-ZbhsvR3Prbo9jqi-13pB8YEsXa0lhBp-iw99TOEmiuAysg30u8WN-Zch0iz0lUsrEV1RZW4vfXq9S9pzGmZIxWvw7nkZWz9WI-hfnjdbLYwTd63pCXTgm9Bb131g0V5518McMZ3p_6szOukcnUMkt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e83b13a7.mp4?token=hDU8zuu4CnWpOuv7Dzt4V3B-bi5VhWUQlblo5sZmSrDpMwyDSmwU8alacEIJQRrRU5iEs42mi6gK0aMYci_9OPdrBIPAlklrLOJWN_dbjTq5lapILZ_L2sPUHc1KLY3PmGrBbzTlgYovpzFj_-goT7HL5rHMwaGiWjAHcsdUCjmIcJFLM8fP45GukpOo9B-ZbhsvR3Prbo9jqi-13pB8YEsXa0lhBp-iw99TOEmiuAysg30u8WN-Zch0iz0lUsrEV1RZW4vfXq9S9pzGmZIxWvw7nkZWz9WI-hfnjdbLYwTd63pCXTgm9Bb131g0V5518McMZ3p_6szOukcnUMkt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌مجلس: در حال عقب‌نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم
🔹
سخنی عرض کنم خدمت ولی نعمتان خود. ملت عزیز و بزرگ ایران! شما بهتر از من می‌دانید که ما در حال عقب‌نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم.
🔹
همان‌طور که رهبر انقلاب هم تاکید فرمودند،…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/438970" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438969">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b880b794.mp4?token=QeVj5arbkfeRnXaYMRU42HGO9xpJGp-AUzmhsQt0Ndyxtr0h04NiZlBLJ5XRkLco5jehpgiDhzkCxJUmB5z9uP4z3Vzb_Z7n7ZdzSAPMRje7Pb1e6QB4fZGa2lYfV74a54iQo58CJdBNwigMIeHyDNE-IvY88YdWIFYP5Al5TtY7qKRt4m7-lGUHxejCupMJTcObOxfxOY2F1sA-VHUvsZfi6-SQ6mbpTKqP-tD0yFiEX2cTB_m4MaseFXljVJb8eBksWYMFVZKhsKxGlPihyNCnEPhakkQbEOSfKTRc8PtemdiAGN4eddm_d8ISBfFz6GFYIXg96rwWNJRcjl3tM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b880b794.mp4?token=QeVj5arbkfeRnXaYMRU42HGO9xpJGp-AUzmhsQt0Ndyxtr0h04NiZlBLJ5XRkLco5jehpgiDhzkCxJUmB5z9uP4z3Vzb_Z7n7ZdzSAPMRje7Pb1e6QB4fZGa2lYfV74a54iQo58CJdBNwigMIeHyDNE-IvY88YdWIFYP5Al5TtY7qKRt4m7-lGUHxejCupMJTcObOxfxOY2F1sA-VHUvsZfi6-SQ6mbpTKqP-tD0yFiEX2cTB_m4MaseFXljVJb8eBksWYMFVZKhsKxGlPihyNCnEPhakkQbEOSfKTRc8PtemdiAGN4eddm_d8ISBfFz6GFYIXg96rwWNJRcjl3tM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: چک سفید امضا به کسی نمی‌دهیم
🔹
ما فراموش نمی کنیم که در شرایط کنونی کشور، دولت در میانه‌ میدان مدیریت مسائل و مشکلات ایستاده و نیاز به کمک همه از جمله مجلس دارد. توصیه‌ رهبر معظم انقلاب اسلامی نیز همچون قائد شهید، هم افزایی با دولت و سایر دستگاه‌ها…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/438969" target="_blank">📅 12:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438968">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc18d99fc.mp4?token=ncPDJrCZogJ8njm8nbuOItP-P_QOlKj1UHkRcXPr6JAR2OcNN07xcL05EHkIqLqoPHvWplVVBfVFDdLr3qc0NuOycmtFWXZmgelHf7Wn0EvyOJ2oP1p9vdAmSRR5ICbcJEpvf28j_RJKw3S2C_02W8_akqaE_U6Q5gfNaaq2qu5UhRstQ7Jl4AqsTzLGLvgd9aThMBkDXuxpm7fszQM-7Qho9guphnvN_h2Z7oMOXW1d-5HKH0E2G0cVJHpWc0GStpb2OzPDL28AllTdEz8KcG4BTN-_9V___lAkvSGe3ocOLea_H4EOUdgoX2V_wikM3Ydq9Sg45AthU0A20Y6a_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc18d99fc.mp4?token=ncPDJrCZogJ8njm8nbuOItP-P_QOlKj1UHkRcXPr6JAR2OcNN07xcL05EHkIqLqoPHvWplVVBfVFDdLr3qc0NuOycmtFWXZmgelHf7Wn0EvyOJ2oP1p9vdAmSRR5ICbcJEpvf28j_RJKw3S2C_02W8_akqaE_U6Q5gfNaaq2qu5UhRstQ7Jl4AqsTzLGLvgd9aThMBkDXuxpm7fszQM-7Qho9guphnvN_h2Z7oMOXW1d-5HKH0E2G0cVJHpWc0GStpb2OzPDL28AllTdEz8KcG4BTN-_9V___lAkvSGe3ocOLea_H4EOUdgoX2V_wikM3Ydq9Sg45AthU0A20Y6a_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌ مجلس: اصلاح برنامه‌ هفتم با تمرکز بر بازسازی خسارات جنگ در دستور کار کمیسیون‌های تخصصی قرار گیرد
🔹
توجه دادن مجلس به مسائل پساجنگ توسط رهبر معظم انقلاب حاکی از دقت نظر ایشان به شرایط سخت پیش روی کشور است.
🔹
از همۀ‌ ‌کمیسیون‌های‌ تخصصی ‌مرتبط مجلس ‌می‌خواهم…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/438968" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
