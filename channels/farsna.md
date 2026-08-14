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
<img src="https://cdn4.telesco.pe/file/dp49eiLJMFpgbyo1QJnCPOCdYSnHWDV-zu07svBQh9B3nghO1vZsMqTtTSfrSXJBGdSdkMZTbQYelBVwQJA90Jz4NCvHSmDxTc9QUjHYjqqc-zUmLRJji-qZXgCsYFeKdh9ZTzMe0zmyaKmVt36O9QV0s8wuN5-jNlmN5jka4uD3B8nE6VCoAzFFCvGrOmDGiQwziPKK6Ru5HApk_bSQr5RSNP3swIb4ianoxFcMJ_FQcK_pYpnW_BU0UTYovixYB8EbrCMG5fK0RDnvaiK7Pr0KjMlGFclaMM2uXHtC3ofQ-PzANIgYi_-MIUtS0pjBEf8DFeN7cvglNYKVMP4fow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 22:55:34</div>
<hr>

<div class="tg-post" id="msg-456106">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
@Farsna</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/farsna/456106" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456105">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/456105" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456104">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVPHj1bPDoFxEd2XXWZoT7Gsg6_UiT3p1D7MTqqrqiUPzYKXCOEGrCAdXm6gbWicEmnY3Fh64Xuva3dCuuhv2VzHF53hEccDsv_VQz0zCn3Bvg8K1-_SeV-zZM-y_oIzvBo8ZhkhWCOKUK4s0guQA5ChwXpfBs9ka8TYaZ2MCH-UapAQfGlNCFpERgyc54j9b-RTBYz52Xll46cFQlcTqxNcaMQxB9QfaFtLBeyZ6BVNiXMbf8lcGYm_8UFq7CAo0yYDml0ivgR4qghu6VvskI3wTtY7FXatGs38X7C2h9u2wwLSzChxLWZ41n_DNzl_6ZEfhfI8dR9o_CMFuuWxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیروهای مسلح یمن: تأسیسات آرامکو در نجران را هدف قرار دادیم
🔹
یک منبع نظامی یمنی از حملۀ پهپادی نیروهای مسلح این کشور به تأسیسات شرکت نفتی آرامکو در نجران عربستان سعودی خبر داد.
🔹
این منبع نظامی به خبرگزاری سبأ گفت: «نیروهای مسلح یمن، آرامکو در نجران را…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/456104" target="_blank">📅 22:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش پنتاگون برای پنهان کردن اقدام به خودکشی یک ملوان در ناو لینلکن
🔹
همسر یکی از نظامیان مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» که هفته گذشته اقدام به خودکشی کرده و خود را به دریا انداخته بود در گفتگویی اختصاصی با رسانه «ام‌اس ناو» به افشاگری درباره…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/456103" target="_blank">📅 22:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین گل‌به‌خودی فصل را علیرضا آرتا وارد دروازۀ چادرملو کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/456102" target="_blank">📅 22:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDyTVe7g62v2qBQY58itp9DXqTNwd17OjwkQ5EkmDBjI5pr_dN2j3LeTPr4eBmwz25wt5wD6y9lj0GLpxXKJMQo2hCsyRCzsjnvspKcofby9qph324ZqaIKTjUbU3KyoxExmoWClnEyidZ5qZgPmjm1F2093E29ygn0JcDLQuyT-NiMauZn1CLMwYU_2HkX-VaiYhp3GdmOyC5RuUvoN3CNfR9XNYaOaocyd6TopgA1wTKqA37hcpI69bunBUjQOQFAt2WLBqF6qrehZWBLrlA-drNn6yMk14xcUyGWl5S-bRBdymSs3bh2PHXVCraKqCqZOouH3lOruVz5hfkcVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsc1peZ_5VxnMtkyBFLAcol8XlHRL09wyuOguxfilRwEGCoowGcYeihTmSl6-HcD99DFzcK7Sl3bpjptD19tK_ZObY6DT0xu-ZEGwNKEGrs0Jb5N2pQogKaNWe5tjkR45vPAkJ-iu0bJwuoXQU1el7M_f4zZJxCsU2r2exAYWP7PFkkhrIwQkEUklucWdKrOmeKwr49GUIc9JfFqeQ7gvFUWOzjFT4jGjoFUS6LIV38Cm2s7sbxWML_5rqSKEeAzSOuBWXOCGiVrwOXZAdLMS9n1azXNWENANb5vGfWfYRxQqIFgbLbYZ4J0ggMHsmgyRBuXSlfH0GlqfMs2giDK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg-U9_OsDVToRowXw88iXisN1jo6Ogsbd1i2rUpDhq9IK3lZiaveTqK-fybxhDQU365IhBQzP9lKj4-j1axX7WuExRRFJWOu_ACcmXYbr2XVn1R7cpqKiaLBo2pO7sxntdz21XLIzJaAi_iT2wY_KXDx7ly_bvDqGVcf_xHg7yzPezJLjFVrINpE9-Uii35PdQmIY6pp_SjjKukoLMRphpZo5yA1mm__Qig_GVGzKRmUstYSa5SwH6SA4qFKX0Xx9E1eEpO-Ubr4LnnalSSZMSxuD6HT_GlIm7feHKBxB_z5-PHrhz67ScZXu77SkkZa7A-wPpv0Ba0CkA7iflhdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4imfBvKOuvox411t7br_TL52SCqwV7-c15G1dFyrmFzLNLjeekTooRumoz1-kTZLdObcw7tVjEdeBFAX01xrcrV4wPPnx7wvJo79eMWr_aJe5A9wobUueNwZKhH-juh-9vNGIMWXHXz2YF98oFyNHjS8ila_X3h418ALlZ3JX-gJPKxlvSPUQ2RMl50pkTtKPeKyImh_sAUlHt9jitk_kArozqmyfYfAM215rd6PoOdhD9a8MP0QiWDrqTUn7cCVH0mwadJTQy-Y6mRmYKQsR_vBZwTW8oreRwBMEWgrzqEt0MbbW-HEUrp-L2bmmv-UTSl0GXcSpkTIkSnBV3V4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل چهارم استقلال توسط قلی‌زاده دقیقه ۹۲
⚽️
استقلال ۴ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/456098" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم استقلال توسط اسلامی در دقیقۀ ۸۸
⚽️
استقلال ۳ - ۰ مس شهر بابک @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/456097" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سحرخیزان در دقیقۀ ۵۵ دبل کرد
⚽️
استقلال ۲ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/456096" target="_blank">📅 21:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456090">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHNyBYelj0cL_MDIe-DXgZXiE-14H5rVDg1Le-13gYuw6iyjxfW8oqVo4etj9VdKg1cCZ6KqmQb-_u1b4WOkrYDR_EQhy8N5ZTlaZesfJmd4qM2ZmB3WhcgTc6pEAN58hcXmm5wIMc-e6d9JBUqnCVzKkKfm0nKRme5EZI_lbS8lFid3AGnkFOLOIpXHkN-l9sRkz1JtIH8lHmlzEY5LNYfc5OtNP_1K1ldJ19EH1Hfzasn3zMU4kZYBU-wGfF1OtJTgbS5RQhWmrsZI_jhERVtdXfbMcC0XQ43v9gC4pjBO_KHojWTvrjz8P0qCSk9VnFzP2C_N9VauHESXv5OANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vu6jKLDsHs0o-HRHjvO0Kitn8t1WMYsRFCtUIpv9M-Rk18mhrQAoykV2mpQmplyjqtmf7A_T2Unb7a-1lH7KTV8IJ_NtPoKlHpWNYVBF3fO8gDJ-445UgZFWDGB8d07khZtmlfdFkcNC0Lj0ek7JFt_MHW2dPQ8lGnvt6oQ7V1hN4iu7h1bddmYN6pdtZxWa1cWUS5rGPtjofmaLaB8XY0CmLQuUWbJUxnT6PLC4G1awe9JWyDJ9v59hxq5_Vgtd78mhGX0OHpusjFfO4-nK6bMC8-v9SEltPKx2T10Qo1G0HgjWzkehOVGe-lLAhZuELumWwmfinWV6Ena0I4cJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brCOf3LAuet8fxZHaPBWP3wkntsPXd_Hd2wlupcy6hsoIqOAzMgEnKZV0wGw-PmHoYKkNeR-C20h0XxzZGGQDO1DOhml7Srucj9WNj43jPWZwOyXUAXVQyH2LOTzWLtzYuYOEyDmYikgQM7-EfrrYpa5rGlA4UopU5Cbz1K4WMLVTH7kdFVrUJzgVcYPXZMpImcSaoUD6WWn40Wpi3Y1wQZKmsF1atSikREBwhr4TtpPY84HOnJe3RebYV1BaaHl3k2KftgS0nZ1UwVhXSZA0mv56zO8NzygJk-lP8_kpumiZS9f5mNIf7topQoiNf_prnZA1gwU9Fu3AlHgqST1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_UmH4V_FFan7YB6nDkqq-jIHaLn7MMRQLdsp6T2EPgg95LqHsQzGsXUAtnp3EO6RbPa0GIP4b-jJeMYf-bbesg4RNjdinPowM7G8BGm-qlCvL6fuJDJ7RCgSkExeDR6IYxIyUBqibm4KMPUlvSTP9mvs3LE2aBU4FAtCp4AvcRj248CZwEzNHu0ERLJ5iSED3BUstge9OP3c0a9f63uMi0SkUfULSgqqlnc8j99bJMKZW5RBEg90eudSbGQyYxILfiAiKZy55gaLi9q5l3v35-h_puZP4gkKUHLhQriI8U8Z4p5ym4PlyKmdDfkTkS2SniFNvY9ul2iGa2HDv1x-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaHMZrMyG39T7dAkjBiIN0PCMXqg6NZj7jovS62_8rpgi_GzwXZSYefLgBIXn2L1tydwmpRCBlDH7jKql7ufEfJOb3_yxb_9LznyOocOp0m95sNCNy6vMrUakh0_-fyfvgdN5EgPqyVsiUDxC65vscFmG9WchtpoYK0pQdDzuvkGdkdEKgz_ytBEYZfOvAXOt585xR0gdOYQu2fn17WjdNyquMMQA16WzzMlTv0QK9Awsivi13Z2UNpYDWAmCWHp5HEvZpegQUU4yl4QrASuopG3Ybuj2HAc3WrFtZ-XF5lmz0ZUqlKohku9tV7YpqoPI-NqagHdWYWkUTyNvoZsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxoQMh00fk3lC1GIJcckt2VQqnnOr4j3m8Pqm3FYKFYqf6xK9NCLJMvIc02CrhYyFu73X7r5i_Lz7is9-77OJquls45E-kOCBLLXnaslIgbvWiys4HUniA-Bqa4dMU9bPE_77RlG1mudyxNCFq9B9JPx9ZwxNou_WVNLHChqaj5PTAETugct_xNpzfAPksblYwpCqtzSpvDYsugHrfvYHHNCsjxCmZPDN8DzJHSsEWcgWO5wctACMCMQVSytv20YA9CqEZETLQwqtF0lNAULC432_5vSIIhGZxyci_C1NyIzlP1xriYm4hya2KR6Fro1pDkquHE93x3HdnULM8R5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب خلیج فارس در ساحل بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/456090" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/456089" target="_blank">📅 21:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/456088" target="_blank">📅 20:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای قانون جدید فیفا در لیگ ایران
🔹
به‌دلیل تعلل دروازه‌بان فجر در بازی با خیبر، ضربۀ دروازه تبدیل به کرنر شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/456087" target="_blank">📅 20:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/456086" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456085">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/456085" target="_blank">📅 20:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456084">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حادثه در کارخانۀ سیمان در تبریز جان ۲ کارگر را گرفت
🔹
استانداری آذربایجان‌شرقی: بر اثر نشت و ریزش مواد اولیۀ سیمان در کارخانۀ سیمان صوفیان ۲ کارگر حدود ۴۰ و ۲۳ ساله زیر مواد گرفتار شدند و جان خود را از دست دادند.
🔹
بررسی‌های اولیه نشان می‌دهد بازشدن اشتباه دریچۀ مواد اولیه موجب ریزش مواد داغ و وقوع این حادثه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/456084" target="_blank">📅 19:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456083">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456083" target="_blank">📅 19:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456082">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnpCkgnpEkjZiZ31-m6qZn7Gb95be4lpjYJ-lkMIjLryKJG-Yr9FHDZskBfXGav2RLcM8FeycGwBfeFiCBEQLX9lz5UTdlaoMDzgIRmwKYyt9vJYSWzPli9U4kY8zuQlYRRd4lQ0wbph4Eg4vLFnTayrK4FVc3XW2RLPDY3B77qSWzSI6I2s4UrpzcAXs8OQd_agxig6OJ-eFS14zLIDYoQl_VCc-WP8EN-YGeAro1eBTxCSokCLoZSE6U2P0G-zAaVwWM9GkxaedDz2xdYStv20Gq5kW9L8N1xvmu8VINrFdaD3nBytBhnQ8LnvzPl-NqmlkMu1-HfsCcFlv3HeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳ روزه این بود که بازدارندگی در برابر دشمن از سال ۲۰۰۶ تا ۲۰۲۳ حفظ شد. دشمن در برابر این مقاومت، این ملت و لبنان مقاوم تسلیم شد.
🔹
آنچه در پیروزی سال ۲۰۰۶ رخ داد، نشان داد که مقاومت می‌تواند معادلات را تغییر دهد و به تسلیم واداشتن مقاومت سرابی بیش نیست.
🔹
حاکمیت لبنان با مقاومت همکاری نکرد. متأسفانه مسئولان محاسبات دیگری داشتند و تعهدات دیگری بر عهده گرفته بودند و تحت قیمومیتی قرار داشتند که نتایج آن بعدها آشکار شد.
🔹
شیخ نعیم قاسم همچنین خطاب به دولت لبنان گفت: چگونه می‌پذیرید که به ارتش اهانت شود درحالی‌که باید از آن حمایت و حفاظت کنید؟!
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/456082" target="_blank">📅 19:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456081">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehwWrv5mBA-Eyo8o_4j0pePirc6JKiQusQgngTFJcuOUQPm1OznwBZd9H6TdoXv949o2lUx1ZDMqwKecHlL-ziFDEOHjLCDSNvs6WJMa_KZPzkgd7QaZOegMlY3W8no_0uTy_gaziejKhaIy3jTkC8rUAJ6q3X32NS62oNQA1m5RygJXJdyfxH4VdATntKuMiVa4K0dCU0tiYBXQlcvTdUwSodC4B9JdX48Agrq2dd9jXMMxXOcXE7CXr_h14zapPiwTE22KLUf_JXGE_WVjjGcGKf2fc09C5EC5OsEoev4o5Ty7GvJxPbJ-R23kQL5XNzkMgXR5wEXDAnZik4yBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مشاور امنیتی ارشد ترامپ در میانه بن‌بست در جنگ با ایران
🔹
همزمان با بن‌بست در تلاش‌های دونالد ترامپ برای بازگشایی تنگه هرمز یکی از مشاوران ارشد امنیتی او از سمتش کناره‌گیری کرده است.
🔹
پایگاه آکسیوس گزارش داده اندی بیکر که از مشاوران قدیمی جی دی ونس، معاون رئس‌جمهور آمریکا است طی هفته‌های آینده از دولت جدا خواهد شد.
🔹
بیکر در ۱۸ ماه گذشته نقش مهمی در شکل‌دهی و اجرای سیاست خارجی آمریکا به عهده داشته و یکی از اعضای تیم مذاکره‌کننده آمریکا در گفت‌وگوهای غیرمستقیم با ایران بوده است.
🔹
خروج او از دولت در شرایطی اعلام می‌شود که کارولین لویت، سخنگوی کاخ سفید نیز از سمتش استعفا کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/456081" target="_blank">📅 19:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456080">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مغانلو اولین گل‌زن فصل جدید لیگ برتر شد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456080" target="_blank">📅 18:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456078">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0vFyZ4Fi5joh1wVENc6iazt7tN0vFkUrQz4hJqjPFp9t1pQrh3fVCLikzkbbbBLHSMrogNN2GwaHUU9v-Kror5oPYwzyumcolg2ndiNgAhKe6S7r9Alfq_oj1rGHEvt5sDcb0n0Msjm1Q3krvwcy0Kkj_E5FcwjdpMf516mpe3poAHzSZ58Km7kbvyQAjaQ2kc8kPAuMWeg73VUvXDOQNtOGZ8TJeSqpciVCSMOD-fT5oEZBQL3mLW4dP4EVALtK3gyPzIxeXjwU5OFnEnQ4ykW0dM12TAXfiwlwXnS7CknXP4CiWEP5nzkfmVy1WhUVDpBZ8IpzfUZ_ZhnqznWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-rRvhyVnkFybehH73LqJZkeeHtlT_hb8EzkfMMMjXpYzkA4hmIUcYd6DufMxZHAVEkbmocmn9JzghXT8_qVg0ZATDVNEycPKkvuAGzJxu0ZOBDFqgQzS091NsEmo3ZdWsZDUwE1xRAUK3OFDsjdljV0jqzrOTWeNYFaOFUsP6sX2NxsQVKUuG7E6Ht0V4Dkx76-1OHlDVeFk1CqJpeo2DSeNgOqnNvfCYf4FevD-HvAr82QZM8xEXxBQ0gNGn7zNGjswLI1L-55cL8gWBUQ47u7CPMe8nmi5rPMW5egoeNAi1_pmT4gybmxSgOkRg27GDr2FRzzUigj2i4ucPJ3kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جدیدترین تصاویر بارگیری نفت در خارگ
🔹
شرکت رهیابی محموله‌های نفتی «تنکرتِرکِرز» گزارش کرد: داده‌های ماهواره‌ای نشان می‌دهد یک نفتکش غول‌پیکر «شرکت ملی نفتکش ایران» امروز در حال بارگیری ۲ میلیون بشکه نفت در اسکلۀ آذرپاد جزیرۀ خارک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456078" target="_blank">📅 18:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqE6ZncD7rOZp9h4pXah-5KHtMgPWRs33Hid_TnImbRsJ7z7fxEiodEe3EY0Tsc9xAc2SQ_kylqUIeOpWMx8_fY2oO7-195Qekw7UlogvnU9nJ8UTH9iFsE8NsmjWgNA89NQKFpD0xhLw8ZABULQCJNOKOXowIwiKVWUL_Mp6BHth4erotXvKyehRukuJQrrcf0Rxl225DKzyLBmeXAPuzP0lRlMBJggsyCj8DRnavoIoHzqwJEGOwdMJWC2OsXDye1imuPfqf1AZkoi5znsz6p73cI8Cu6PBcxadV5SCC9nH7EwAKulJgUm2wEN1zggnl-qQiKbvurynHW5f247bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO04gDgNYN53lvmpj8QslGHGrcUjWeWQ4D-Z7vZOznwX1_KEgi80GYYuwng4OmWy2K1jMTavkNa9kWwDokbNrpJrdUEbD8awnnCMBXsmm9MNo8a1UTSf9Z4Li4Dnc_vlArSKZvGlE2gEwACBY67MhSF8AFNkySXq025VrTeNtIYi4SeWk_upCKv453AIHsKGwTtFA_2bQFsgCAb3j5nklof4uJEvI2w4E3sExODaBIruuoH5PR1VR7ziCgjsiizuVxwOM-2Oz8g8lCVWQzeu82bUsYlscFTZ-EipMr8OKe05sbacn2Ffa_nMSsozSA5cyxESo-bMBI0rm4re4gGn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmCWt3uMCrIR19F6eAALce22IDnqgpiJDjIACR4H1bGXfB6ACBfkfuT0TBF5TyRwTKgZAIfh9srd9Io5ZVgqqaDL_cAtmp1P6xC_K0Et5dxzV9z7AXeyWs2ebbaelMHfVGssWwOTW2EHeetSwkpCu3Kw3OLwm1CNx_y__InFzrQRr9vHCqDaEqhKpNOvRrOEbPhTuPXKP7pJhKsYalBUNWI2WRHYYDQ_WR5Y4dGR0N6bG36JfetVM6b176yUptaLLIrl1Lr7xTl1Dwqp7wG7VqHCbQeFlH9Q9_H2elNjR37CGOrRiFmxzSU3W1TBN2fXozuY9N0COUYaVrO-LbIqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdu39GsTS12lQiFf03M3W-lrSy1G8ZLr2UEGHV7G9tf41BqcetIxjBhvVCaGV4rVaO44AGI5mHMNB9a0RK-GhmMNpllS_tITjSgOItIRWXhWyvGJwjSAJ28OyxGBJTw0xqx-c9wi2F6pIqHjwiRPpKk_CkonQ18hCNnxevZ-aJlhjtDoBrcYoVQJPcjU0RlJkQyfCQuy-Fjx-AuuujiXgChuPCxmckHg1iSL-I4poE8KK3L8-ohte5s3gxSxADbTv-yO5plcC6o2lCcr8ygOotdi_qKbKeks59wnRhqJFE-GckegUu_w8mYk9OSze1G1G9bIDePHbjbckKOsk-0LiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعۀ گل آفتابگردان خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456074" target="_blank">📅 17:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrFG_WgkHh8FnpjzuNFxantsfIHKoRTVpjSNkJO8ZROBeBFnalddzxQFX1BLu7lcLdtPGhHAYFJ7NF3ylTt4PYFzk_cU05xUv7WpUN8qaXL0nPa7Kk-CZ9AJGLU_Ci9ETtWnwgGtIgL-ZhL-TtsD_174uPkqN1QEAirONBA37gITCQYdm9ZfC0r_b6MepYiROFCgCm8OFhMUhGxWl7YQUTJYWVjJjVfyo8JZiT76ItaYTLxBUvSPXfhj_tqN84FWeW4Hv31ggwOAhaG8omXpoKEBLWkQt93YxuunbthLYDq277VE3C4k_V1WzLUWo1_7E4tj2eIm_zqBTqhqrOzMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez1PLyLT_K4UbQogJu9kaJbKTXUNMKPbo41rEnfPRIpHZQD9uAlj5uxhIE_d67JvtdplUPIJdHW3KiictnKbqBPa8BsHZrNimp9WRQlhAxQXsgOQR8l53oqYUke57eKdaslw_3cFpuGHLJzkorgA0qqsWgAfSdgoAxIDejHQ9X4oQCtdzLxeIxWUv7ODzS86FXkSG-UwJ7yr6xo1WePxw--_yh3B9dn2a0SsVH-ya92N3gtKGxELwSHFdG873LJ5WctUCCOiBZefb4djsDTl3nPAIipvHAxBhNdO-EwwFfKcZsEtz6rkcR_5tDatu9fOV-eRojRUHi8egBOTiOqcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7HU1fGmEUV2pRsN76s7RdA0gy0FRYm7TuyaA4A1iz7vYbuHtBHqP_CQlWs2RJTkUdFRPDdiw_zwcmI_KLIFf3BdmVG-XAc0D7VinDOgfi_17MOUku8q0AagPkKgd-V5RB0X7RXB6-beukC1kil2T0oZJq-u_Mq9XZvah0S8VTt0px0vQCiKUbuBOmfX97zD5JsYC17-_xa_vfi0jELISSqCChM58OseEYD4-if2zR01iVEC3jVzYeVmoAkIIEfbOgDXApFX_btYqMmXYW3hZG0VIHd_vb7N0s66wgjqetDnbHGFQQ1zQnXFSoWQ4rrUtLpp2nE1TDzL9n4PaAlkZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌ ایران در دست هواداران تراکتور روی سکوهای ورزشگاه یادگار امام
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456071" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
🎥
تحقیر تاریخی آمریکا به‌روایت نظامی آمریکایی
🔹
ریتر، افسر و بازرس سابق تسلیحات سازمان ملل: یکی از دلایلی که ایران ما را جدی نمی‌گیرد این است که ما هیچ‌چیز جدی‌ای برای ارائه در میز مذاکره نداریم.
🔹
از نظر نظامی، ما شکست خورده‌ایم. ما توان ادامه‌دادن این درگیری را نداریم.
🔹
از نظر اقتصادی، تهدیدهای ما دربارهٔ اعمال تحریم به سوژهٔ خندهٔ جهان تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456070" target="_blank">📅 17:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZS_-Z9asVwQHsEq3nchtta3mOo5djUfitUPBn4DpC7mU3kUHAVQUwlyLUMv8dqzm_kAED7piVsomRlJn-BbSLRmxaKYK_Z-xwyfI_JJIlKbbgC6ncd6RJ7Q6hjssrYuC_X66CeYbECHZCloazeoKZkAj7HHr7syaxGO_f3rtZi-pLPxf1QDKnhrfP5B3wQeWWMxnwM-a5ThEiHCLju1LnAM-VWcoGltd0TaDCDRHiUOU4Gb2jNA73SOrPlLRHbWe_TXLuQTEX5-TaK8v3qDnYhS9TaZWqtBX7Movn_PcImQrxEkLQLW6vneHKekANZBnbh1Kh48KQhyg5sDFPHAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باد شدید و گردوخاک در راه ۲۳ استان
🔹
هواشناسی: از امروز تا دوشنبه، وزش باد شدید، خیزش گردوخاک، کاهش دید افقی و افت کیفیت هوا در ۲۳ استان پیش‌بینی شده و احتمال خسارت به سازه‌های موقت، شکستن شاخهٔ درختان و اختلال در ترددهای جاده‌ای وجود دارد.
🔗
اسامی این استان‌ها را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456069" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456068">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2V-Q5apXwaT_R29dAr76S2nXPw3ARkzKetjqdkw_3WOvlZcdHB-1YkARyttnY9UwPEZ1J_tUm1MusMpq3F15HO4Tc8I2OBLq489a43B3GJQ_qNJC-NJfihBfXNowNZAhCsMhJYVHkcPbZsYjCAswbxvlA3k_UcTqQkprh34a-qjqCs9lQghGuG0MznpSbp9Mat0B3W1x6xM9dCYbN-ZzUcCprT8gREfJDmnsLAlyxtppPDRqDXkjGlgBU2RFdf4gC-9N6h-QH3NZDOaBhAsRMHlpzc8FuPH4SYlgwuE3NoHYYC3azSeujfi9CaH2R-ceYpsN4oWMW-env7igtP5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناظمی اردکانی: بررسی لایحهٔ خزر به بعد از جنگ موکول شود
🔹
دبیرکل جبههٔ مردمی ایران قوی: اکنون زمان مناسبی برای بررسی لایحهٔ نیست و تصمیم‌گیری دربارهٔ آن باید به بعد از جنگ موکول شود.
🔹
سهم ایران در تقسیم‌بندی مطرح‌شده حدود ۱۳ درصد است، درحالی‌که پیش‌از این…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456068" target="_blank">📅 16:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456067">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سفر رئیس سازمان بسیج مستضعفان به قم  عکس: حسین شاه‌بداغی @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/456067" target="_blank">📅 16:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456066">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii4lQA7e423T-MQBc-U1l6C87S7E0enJ7KI_ul2jsy5M7zpsLG1YT1vvdgOVifJWMMkcaJosFWi4uSrdrElFFD806Prhk8HMbn8FlqcoO2VakVEZqkpmDcbx5-B7R_6zyKoPjMICJfRWFfuxJF7L5q_fSHKVKc50EkCK6qsEc6fYhxucuiZ5IK38hZLYGYxKDL-E9DunfLtmz8tO57uLHukZZKZV9_cBCWl3NLeBdDLV2_f7NhK5YTYkolVdrrgqk-Cr9ipwyah6mPUW8Uh-JK_DMsrhsfyf_ImDSNhSbVxMANX-CsbO87DLSxCffEW5Bl1Jt4Ok04NNI1UKmWiu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ ۳۰۰ کیلویی تریاک در اصفهان
🔹
فرمانده انتظامی اصفهان: در یک عملیات ۳۰۰ کیلوگرم تریاک در جادهٔ ورودی اردستان کشف شد؛ یک متهم در این رابطه دستگیر و خودروی حامل مواد مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456066" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456065">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2N93xDo8j-b3yOHJV1WgSrh0Ic19MTNWLgki-2ADyw475smNx8KrQn8qRDYug4fHwPD2ftWxO5CUaXszz56ytxMrTbp-hIGhc6sH8kPhtu5yJzSUZUckhsGtnCj2PQr6peC-GH91n7IiZ-dbxvgDHaeIr8YQ5SO7Gd-EZdIqbtWW2jD2VOdQ4S_EZgGwjDJabqGhLUZ5eielDiOYrYk27QRINCj-9uTVloDp0FQV4-OM2XltZOpLC5SuAzt1Qyg9t45z1uIy09mA4bY1a7Ja6rqfXhn2dUcccmmqfXe8q4ajJ5D0-LnIZiReNJIuIT0XGA4hzCmTzgdHPKWRQgYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: رزمایش تایوان صحنه‌سازی برای جنگ است
🔹
وزارت دفاع چین: رزمایش «هان کوانگ» تایوان نمایشی پرهزینه و بیهوده است که هراس جنگی ایجاد می‌کند.
🔹
مقامات حزب پیشروی دموکراتیک نیز بی‌محابا به هراس جنگی دامن زده‌اند و تلاش برای تبدیل شهرها به میدان نبرد و کشاندن مردم عادی به خط مقدم را شتاب بخشیده‌اند.
🔹
ارتش چین در حالت آماده‌باش کامل به سر می‌برد و به‌طور مستمر توانمندی‌های رزم واقعی خود را برای مقابله با تجزیه‌طلبی و مداخلهٔ خارجی تقویت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/456065" target="_blank">📅 16:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456063">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4JHNKj-stdxexbqFh32FyUxgBCPGGmu2yju0nNSXzk4zMHRyHh6a0u1eZTa3DMh30TujR8J9rClDum3Q82hsIXkiZeBUzZGI_5oGWLHQnzY3a03a_qhpS_jiT2HQ986S2B2ynW7wyv2kZYx5dJBIpPvIYp1KNDRYX20C1WAkHciESGx14JR0bsPaAgJo-eVIYJKaXf04Hb1w43n1Q1BU_w5mwCg6XJzZycntWRurUBYr6IIuY7N5WYh9KLCpqrObvyvU9fWXfMIJk4W59KoB7QD5TTB2efoL_8wiWlL4KPmAJIzlqzSdpVn5rd3rD5Xa8iH7hAhketiL65is15DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/456063" target="_blank">📅 15:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456062">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFOddxujZ5jtAqYGaGnIHPj_NOkaZsCmq2H1LZ8KEW85IQDCFNQJXvUK3JilrTqtoYXE2aJUprZ4VHNuwirxfukuOMKFpuThrqEr3UmGqe9nIs9BZ44I5HKOZxgfYlY162sQLk0g_mi8vmdyUR0vCYHebVNknZq52Lx2SHr4x9mjb8i-dS_DKJABVD6ZQqlQFm9VE9_LfrwM3IaWi-RWw1W0W98wWUkb7_3dYPxmO_NgrI6j9NFEK6JojduNmhrLG69nOr6KioRfecJ5-N9ejdepkgy2cdjIBw464RcVC2hhF2DtI5q5GVhqRzMALdDtU6c2Jg-1YP5EXZiRmBTreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر، ترکیه و عربستان در رستوران تحولات منطقه را بررسی کردند
!
🔹
وزرای خارجهٔ مصر، ترکیه و عربستان سعودی در شهر ساحلی العلمین مصر دیدار و دربارهٔ آخرین تحولات منطقه از جمله تنش بین ایران-آمریکا، راه‌های کاهش تنش‌ها و تقویت همکاری‌های امنیتی و سیاسی گفت‌وگو کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/456062" target="_blank">📅 15:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456061">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5-Q5NjjiLREGSatihJvbpJbqspI09RHVmjNIhOSq2LjuovWj_2OzTpV6ZMf6ryJvTMnzP6M-GRqOmAsTqnxzn7lmibW6hhJ1Fx3sELBVOI14NNBt1hsydDRoB1wcCS9Wagt88RRto_I-5PxyZoLn_wJmc61eAOcAcBji3iPmN0Z91FfMMGwsFU085_hz7WgIQizwdY_gk_P_Fv3BVgH0pxEHDNRrb_wmgJXXo1suicHvMKiWEnU8bvpslwAnHLwDhlINj_7DsgsefmlSWZoyf57yKhqIllJY4E_TWdTQtJuOYDeNOfrFjVdW0363TwIQFXbgXfN1jCMgTuCQHZEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج تازهٔ جهش هزینهٔ مسکن در آمریکا با بسته‌ماندن تنگهٔ هرمز
🔹
فایننشال تایمز امروز گزارش داد، تنش‌های نظامی و دیپلماتیک میان آمریکا و ایران در هفته‌های اخیر، موج جدیدی از افزایش هزینه‌های استقراض را در بازار مسکن آمریکا و چندین اقتصاد بزرگ اروپایی به‌همراه داشته است.
🔹
این افزایش ناشی از واکنش بانک‌های تجاری به افزایش هزینه‌های استقراض دولتی و تشدید نگرانی‌ها نسبت به بازگشت فشارهای تورمی است که ریشه در تنش‌های ژئوپلیتیکی، به‌ویژه تقابل نظامی و سیاسی میان واشنگتن و تهران دارد.
🔹
همچنین نرخ بهرهٔ وام‌های مسکن در آمریکا به‌عنوان بزرگترین اقتصاد جهان، بار دیگر به سطح ۶.۳۶ درصد برای وام‌های ۳۰ ساله با نرخ ثابت صعود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456061" target="_blank">📅 15:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roArX45KqZf9vFBYEaWHDRJQWXwZIl6CgeSVQHtA5ysIv7ierQq0RftinHxVnPHG1z6nMPjW9bVOZHIk2q0daUOmseYq91eYM2zhS8kxrrMMwVQEkVDajJBHa21LHBOUdEeiZKekA2WD1AbiDgpFVsGXhpeDhhuXUCTOkoL4vXINFfmPsY4RQdRiZW9k5pjO6bWDvgDWkl3RxNq-Zi9BHWu6bI15PNUe414PPkh5NQ596zJ_-rLmhJDt2WyYXdjFXCI9WmcAvQQWeXE6xyOOKqkd87Goh8Z2-QKEaw4yPD07mp_hF_vQw9A3k3uyLlGjWVZHzvdQUDYA2EpHGf3amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqf9CcaOWc59-x_qLAxCueOo0ecw2cnOOm2NE4qRAbmL76Q4_SpxpuJrDgXBVT8dsguDpsWHwB_g_mIGtdfWPg-bk4d1Pbg7h7jfMkbP-2vqRjhT6-8eG6RkNRqBtqc2pWz19Tyc88kMV1SeGBiUTE_-0TkCg76F4T8niJS14tRyThASkYl3POOuHqFcWbUvn5TlNP43Wd1xljvBc5bg_Yj3NduXmlUBJ4eZn62-mbWdBKXiYCfdFZlQKGe4vfdfWtTLiF5tmAVYLtNpCE1_otv3fxylffRToX4D1sMT1ccj16-JkJc_zMJwaarSyO6I4Q_2Vh1X9cAPDDta3yuViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBvPJWiqhVSTeu6TR2x5gIqN-mdcSyIggd66HsNJj4E9y_7NVuaWsrDT7Gcm3AqB6j1CCjSEAyw21OTygpTi9LeG4ACy2dlg5l6scImz4CrAByd80DPvKtTiagFKYHnb8Mj4lrba2Xh1UDcEGUS1FVZno78YA2AZmwMZnRVLwoFYuoaa_cC8qKA_ZCzTExCwF-qT6kZdWKed1fpDtiCTMr2Zet1muqUW3ETg7n-EDxEtaassvnnM7cOZSzD54Bh9D_J2_91c5djkY5TbIQzmJlAsOAjpB-0vGLY5dJ9ieAW6bB5e4-1NyiAqWCF0O8_XF_ujregr76I_yk9zyF7yQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9IY4qygm4CvrCCOSTx-yErTf6_Y45paiCOL20S6cPiJp7U0h2KaS-_cDOrSvvoeLlYCGN0twxv5l552BH2O9mfMelg8Jjb7iHfyjW_3TX23wfdZ167f42WIr3PyClgpifzxvtTofldizT6ie3ybxeO1G0aBxzeA8LWYvWbSceyE6CuaoD1k_rMTvaLNN06XMb0XMbzWEF9G-Tl_taGOldeafw2kcNFxJ785ofHBt0VDveZmI8qfE-IYISmkT6KCAkj0yMNQ19m_OF0tp6QCUdBVIBisdIOzPv62R5niilI6RWNFelaT_TDlDoGP4pNmAiO9QsIDUuzfXtLYb0ur2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpOPCdPxDblSjFdzyNreImIyd12g2iW7BBIZPB3-nur8qm7vHpl5aD2hHYI9l_P0bjX_POytO7Im2YB99h-m6-Xc1l3QtzlNmEb_Sp856tUtMcSMYc3eOxv80aucNU1wLzul7Qy6ccm8bfpmU-zqvJpZn7rYuNPRxGvCaP40vIYfR3QYXg_0kCtO4OJYLxgzP5BBXthVkxkY9O61HdLNLvHayfoNNhH6Qj5AtgpA3JlZ-tEvqSJAPYWjHRdFnCAcipjlufv8ot0xpafL2guUPZf8O3bDI0rzFFJISe4pVBVP2x6iDsLOXuHuUOq603nh-w3sOR-HojMKz4_F3IJaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovAnmqJiINsGQhKDRR35ajWIPeBzmf3Mj2jWSTcjJjYK1gpCRXBlIMdGJvp2ZiA7KUXHNEyXlZdoaeKw2D-rCRNNux43-A_xivUVwQk2Rk9fzNsSy5ucr9QxHGRySqk4DV0plm5VQdyGYRKPIkHieyky6wODDWLJW9-q_hqn1FAyt6m2m29B9wLpl5CO5f-SReIaGkv2Em69bm8x_DCGLAj-Jz_znJ-NOBPhX7Fj7p6iAUrRDoSHS3_Yax6bngjIq2snZeFIlSCBCdtJY-RZ6HNb2couD1Ffa8mMXaUWeGCcUpTT40J95_dL-raN79rlkdpPkKjWxb8M5rAedyXJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoSHOp1t6oP01aSsUt9NA_MKH-XRgKz0SUJjJhoK_aDRsao04Ji1azuR49MXkDY3A_rF3nRUO-dow3u1tHinJL5TlTPkDoJqbi_RUydUGbfsIAGB936NzkS9RFcjieKvch8ts4AT6zyjMQgWhmVUvLes1ixU_IXRYbuUx4bRX8bcnukV95FXio223hpAkUqn8W1OpouuCgPoMTKm_IDOXItSnrXHhRx99XdTu9av3T0O3Juni4MBcoggMloO-LuKbma6Aw6fIrB-JWcUVHM9HntTmky3RLdZkAclXHy92P8TmW5oxpdQUJu--MKAG9w2DGXyNpz3RoacGboDzs9Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pImYVWa3rTjslvG9yUwlFJzUvqcRgKRAHm26B6FCBPu33ce7mg4HPxF5u_T91V297xWftvhfRjlxfsj1BV8TKmaBc_1C8wlw9znrgyaNZj9GE6qTik0EL9whsh2jmQwLXhi7KW_JnSqXWLC6-CgN1CBWxBbo3e_BnHA9zcXf6YmWLJf6HSBHj3HzyakdhoaC19mTtRykGUhVPb33NZJpqE8zzu7EGQg1qCXE9zkVY-VluEEu4biRTbjqlk3d1nXYgNmu4zsIzMRvczlNQUcXoyRHdRciFqiNwUy0eIK9SUFKzUp1D2P6VkK9xOZJTzbyL_eNPKPZQwA8tT2HN3w3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBAMvb0jxeaD3IKs-HpbGyA1Xkt-vatM64RMRd-ylVGHVwTnO-f9hlQOrDN3o132HU7uTwk1v8Zji-S4tXd9lHxVHIcWbufjGYehNwcdDHj6oJL01571clvU8ttgJvF8oyMpkqQfcLIIMVSy58-3G9W0sqjgWg3RNwiPnS7TkGR4aieDMYElxUyqvI_EJzrYXJ0MGRWHgffndKYe5ovDGBG3QZLReDAyQdqi9mTgw2Y3wKz-Oje7wct_E1YhsWdnOK8z3NnOeaPo772t3o8CqM5lPWCkmYW-JBfrPphP6yYKMx8Crp87r4mQu4QAb6AmiduXT0LyrpA6TLIH7ilQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK6kvRiJB2CDHRkJGHtWvOcjKkWed_06k_fkRkz-mTUKIXOU-mpH-QL0M7ZIehYOpqby8EPirDwdlRoBG8OS_7aIMmslkX4g7D32yJQS_7hxLdgG0eRHUSnGUX6kSu24vR_99lt157BrHd9ufigvHOa5AQaPel9ix8D9Ir3iu8seC8y0urDkblTzEPljsHxvuHjk_T996qTE8lxMYd-YCMmA6aQGyA1Gx4STu6HSojCyHBiFKJBB17M05WzoDnn8_S6QOssNfH-LUskIOZcPERUBjK30_OaeA0dCFZkmQ8yx4_gYZ6hC6Nn39Hta_LTTzrh3y1NeTPrYM0jMFIc8qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
زنگ اول لیگ برتر فوتبال به یاد «ماکان» و شهدای میناب
🔹
بیست‌وششمین دوره لیگ برتر فوتبال ایران عصر امروز با برگزاری ۶ دیدار و پس از ۱۳ دوره، با حضور ۱۸ تیم آغاز می‌شود.
🔹
بر همین اساس، برخی باشگاه‌های لیگ برتر در آغاز فصل جدید تصمیم گرفته‌اند با طراحی پوستر و انتشار ویدئوهایی، یاد و خاطره شهدای گرانقدر میناب را گرامی بدارند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/456051" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohcMlk0XXSIarfiTPdEf5jFB-SwitzwaMBvhV3NyDf9waT-iNgJI8x2FiUavlyHuawYpkoA2V3neZZcNi68vhpa0TX2ZjttH9t_HUp5qgJqBvVoshQxWM4FUL_pfyxgKk7iLI-GivcEdBhyVzGI4PxmO8QBdWuIHoBrjTBev_VK537wsTOpsAOG8du6K6IjOPpYM341Cycrnx8FnPcXjnydKojl66jCGs3W-4pgbhaQ7oelQnZEp7ANEcnyxKsL-pVHzzmCCvRv8EG4EwzN5fIk8I5ftsliKJrb8AtiUP_a_Tgyfz0qXdmr2CqXhvDIj20rwH1FX88gYSWrrcH_CWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت‌سازی رسانه‌های ضدانقلاب از اتفاق حاشیه‌ای مشهد
🔹
روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد.
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام رضا(ع) رخ داده است.
🔹
بررسی میدانی نشان می‌دهد که این ویدیوها مربوط به فضای بیرون از حرم مطهر است. در داخل حرم رضوی، اساساً اجازه حمل هرگونه چوب داده نمی‌شود و محیط با بازرسی دقیق کنترل می‌شود؛ بنابراین، نسبت‌دادن این اتفاق به درون حرم، تحریف آشکار واقعیت است.
🔹
هرچند اینگونه تنش‌ها میان هیئات مذهبی رفتاری پسندیده نیست و انتظار می‌رود عزاداران با رعایت بیشتر اخلاق از هرگونه تنش پرهیز کنند، اما در هیئات و دسته‌های بزرگ بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
🔹
عزاداران و دست‌اندرکاران هیئات باید بیشتر مراقب باشند تا این حواشی، اصل عزاداری را تحت‌الشعاع قرار ندهد.
🔹
با این حال نکته مهم‌تر که باید مورد توجه همه مردم قرار گیرد، دلبستگی شدید رسانه‌های ضدانقلاب به بزرگ‌نمایی همین اتفاقات ساده است.
🔹
دشمن به‌دنبال بهانه‌ای می‌گردد تا اختلافات را نه فقط میان عزاداران، بلکه میان همه اقشار مردم دامن بزند؛ هر جا که وحدت و همدلی باشد، سعی در تضعیف آن دارد و هر جا نقطه‌ای هرچند کوچک از اختلاف ببیند، با تمام توان آن را به رخ می‌کشد.
🔹
این رویکرد دشمن نشان می‌دهد که درد اصلی او وحدت ملی و آرامش در جامعه است؛ وظیفه ماست که با هوشیاری، این بزرگ‌نمایی‌ها را بی‌اثر کنیم و با پرهیز از دامن‌زدن به حواشی، اجازه ندهیم تصویر زیبای وحت و همدلی زیر سوال برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456050" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
انهدام پهپاد MQ9 در آسمان هرمزگان
🔹
یک پهپاد MQ9 توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان هرمزگان منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456049" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456048" target="_blank">📅 14:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NARuTTFG23iRsucc8HuKqbRaERrn1GsIan1E5sSzMJ--ayRw91UVv-XKoFumIqmEino9hahwcmshgPRQdHCUO5fBK-EPLgs3hY7kxve1kYMExL_5-tYkbuZgRjAdhHH4JkPNmh17h_62RBjS2P_H0Iab4IXOrQilp06q6Pe9IKGBJMbr-nrN1s0Xi_L5zYOgRwAK82fqc8q1tRh29WyGAMWkYKnk5APeLRvh5-4kiUjj-2f2OBMmwHLUhu_0_Z63SK6svYLlu4lpR5DR4QgWJ4kxtjf6Y6dupSC-TvW3Bv709-LQZrfOqBA0HMvzUnqa0N7qhNgTmNVBga37VGj3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه طرح توقف حملات در دریای سیاه را رد کرد
🔹
روسیه پیشنهاد توقف حملات به کشتی‌های تجاری در دریای سیاه را که از سوی اوکراین و با میانجی‌گری یک کشور ثالث مطرح شده، رد کرد و گفت مسکو حاضر نیست به توافق‌هایی بازگردد که به باور کرملین صرفاً به کی‌یف فرصت تجدید قوا می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456047" target="_blank">📅 14:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2252485e79.mp4?token=e3jQ_TZ9SSBv7axovLVifc6liETZAGlICqt9N-nJQNsxwolVjDjb5pBqNdN_vSUkjYgDAgltuwRszOVdcjpGcj3Ltwv14YVYjiz0ZKUjXNgACAFW7tqshayQ9RU2FIpnOOPDotvx4J8Grl1EsBSVZjcJAvwTdL-xgDkXizNAyimrGB0VtwxDphZhNfCdNZEiSc7f7eoxcBx38FYPRQl3VAASuEQht6kGSnKkFlxB4briq4WPj0AE479APKgx_4Hz1GO5ea0_ZHU7v5dfaTifqsAKoqIgjWt9KXLzj_snbzfEmFCPKl20Ccj8N8zLKOMm11PsUgX78rwkrX34mVLRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2252485e79.mp4?token=e3jQ_TZ9SSBv7axovLVifc6liETZAGlICqt9N-nJQNsxwolVjDjb5pBqNdN_vSUkjYgDAgltuwRszOVdcjpGcj3Ltwv14YVYjiz0ZKUjXNgACAFW7tqshayQ9RU2FIpnOOPDotvx4J8Grl1EsBSVZjcJAvwTdL-xgDkXizNAyimrGB0VtwxDphZhNfCdNZEiSc7f7eoxcBx38FYPRQl3VAASuEQht6kGSnKkFlxB4briq4WPj0AE479APKgx_4Hz1GO5ea0_ZHU7v5dfaTifqsAKoqIgjWt9KXLzj_snbzfEmFCPKl20Ccj8N8zLKOMm11PsUgX78rwkrX34mVLRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456046" target="_blank">📅 14:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c86100247.mp4?token=pNdpzAjeVdmR3JJpki5ZP6BGeFEXI8YZzz4r4XhJxTGU4VRDLcWzVbcSpsNP-7vVr0Sl0vyLcIzDz-ecbZgL2EZ3_NnZ2EGCJMp3eqw8bsM5q_Uq6H6oFEn4K-tiA1abSEDrJSss-vVuqZ5bunVEntJ4EVrYfahySCBAIUNksgRzLLYTXxaHihjbIg8M6Oqa7yNCGsCOz-RHYwWBEfN_5izSzgihTYVzVWDpGX6zzeysL_EevA60eS77G1KMEgPtNA6kuik6odfmYl2r9-03Kox2HrMESLKC4WDnFgyChBypeGebZouqn27XUxIJMLoCbD1jPiLBjH-BoY2Fv_vKlCL2V_JwTDtOS9tkJpPkqQln0rAxr37F15gkTjiQe7TDwfXv5KRKGgknGf3eWA3lpuuRCHgtZCtmjm6tr1ZsNr4iAfAivb6lgErKifq3vYvd9zJQTV3ElIndByz90Ty2lSLCnBTlqN-zG7QaKwWUPjlJOVsoNeM1BnwfDHRqRZCl2jXnqPpF4SEg1mTkgwuoWkxpZEYudp1tGoFiO2sZ-5j8pAoxKCuJ939p9jm60tS93hfO0jIMEoS9lztqmTBOnbpo2W4uvJ0zip4UvgMBDNCk2PTszv4ApjQsJegc_Vt_K38eZcGK1vRaaOpV_0WhDMgY_TfDbedPI39wPgbIvho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c86100247.mp4?token=pNdpzAjeVdmR3JJpki5ZP6BGeFEXI8YZzz4r4XhJxTGU4VRDLcWzVbcSpsNP-7vVr0Sl0vyLcIzDz-ecbZgL2EZ3_NnZ2EGCJMp3eqw8bsM5q_Uq6H6oFEn4K-tiA1abSEDrJSss-vVuqZ5bunVEntJ4EVrYfahySCBAIUNksgRzLLYTXxaHihjbIg8M6Oqa7yNCGsCOz-RHYwWBEfN_5izSzgihTYVzVWDpGX6zzeysL_EevA60eS77G1KMEgPtNA6kuik6odfmYl2r9-03Kox2HrMESLKC4WDnFgyChBypeGebZouqn27XUxIJMLoCbD1jPiLBjH-BoY2Fv_vKlCL2V_JwTDtOS9tkJpPkqQln0rAxr37F15gkTjiQe7TDwfXv5KRKGgknGf3eWA3lpuuRCHgtZCtmjm6tr1ZsNr4iAfAivb6lgErKifq3vYvd9zJQTV3ElIndByz90Ty2lSLCnBTlqN-zG7QaKwWUPjlJOVsoNeM1BnwfDHRqRZCl2jXnqPpF4SEg1mTkgwuoWkxpZEYudp1tGoFiO2sZ-5j8pAoxKCuJ939p9jm60tS93hfO0jIMEoS9lztqmTBOnbpo2W4uvJ0zip4UvgMBDNCk2PTszv4ApjQsJegc_Vt_K38eZcGK1vRaaOpV_0WhDMgY_TfDbedPI39wPgbIvho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از پهپادها و جنگنده‌های شکارشدهٔ آمریکا توسط سامانهٔ نوین پدافند نیروی هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/456045" target="_blank">📅 14:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456042">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146f452f88.mp4?token=DiRRdDyFKdBQcl84uHxGab-ro47t5E6I5coE38e5N0lS7jLJ9YY0wQpppKa9dFBC2sleZpYrm-sgx8eurLy73HJqhNJYyYyR7C1TaqkwUrPDBWGeF-6wOMBxw1N9kR5Dc4ofd3_MDqiXdNC-5cV_kWJwpa2thCxHWGNxQEWBhYPDpLkCxcZQlt-jnKQkwyInjznGPS5wgItmKdubLE2JgXH5WLryilF9cmgDY6a0HAz2xdrfUl0X7JCicwThsC5RAOffgcNYURORt0FQV_UUUreYKPP7dYLtmwHm7SFLd-zJN41fNuZ-3BBi0c8IgIY2rW-_7SfvElA3t3llGv5okoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146f452f88.mp4?token=DiRRdDyFKdBQcl84uHxGab-ro47t5E6I5coE38e5N0lS7jLJ9YY0wQpppKa9dFBC2sleZpYrm-sgx8eurLy73HJqhNJYyYyR7C1TaqkwUrPDBWGeF-6wOMBxw1N9kR5Dc4ofd3_MDqiXdNC-5cV_kWJwpa2thCxHWGNxQEWBhYPDpLkCxcZQlt-jnKQkwyInjznGPS5wgItmKdubLE2JgXH5WLryilF9cmgDY6a0HAz2xdrfUl0X7JCicwThsC5RAOffgcNYURORt0FQV_UUUreYKPP7dYLtmwHm7SFLd-zJN41fNuZ-3BBi0c8IgIY2rW-_7SfvElA3t3llGv5okoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریزش تونل در هند ۷ کشته برجا گذاشت
🔹
دست کم هفت کارگر بر اثر ریزش تونل در ایالت اوتاراکند در شمال هند جان باختند و سه نفر دیگر همچنان در تونل گرفتار هستند و خبری از سرنوشت آنها نیست.
🔹
به گفته مقامات، در زمان وقوع فاجعه ۲۲ کارگر در داخل تونل بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/456042" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456041">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=XjRLreM36s6a7QKprBF2TKOrzSeeZKy6V7EYu8z3iR_cpHfWh867EZqKQy9VfsNMO6g4WPqNP4b_j5Jiqz4GodA_-3Ub8sSrXQJNEH_MBjyGXZg1cG9M4p4RMRe11BC-6vc6uePumJRwbiNJzg0IxVtc055d7FxRDv-m0AYYGl2kFxjTERFWzetC1OW1naycTunxMqOH0Om6yTUWAaGQbsAsh40rvbMrar5mh1VxdPjmuyTAb2IwI9-b59E_YHhMo5sd0O0PGgtXsFfIxQRV727Jw38xCEmzPah5UoEK0NHEg5OljU7_F86--UJR1SDgXi6MTebvem6RT7FsCFP9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=XjRLreM36s6a7QKprBF2TKOrzSeeZKy6V7EYu8z3iR_cpHfWh867EZqKQy9VfsNMO6g4WPqNP4b_j5Jiqz4GodA_-3Ub8sSrXQJNEH_MBjyGXZg1cG9M4p4RMRe11BC-6vc6uePumJRwbiNJzg0IxVtc055d7FxRDv-m0AYYGl2kFxjTERFWzetC1OW1naycTunxMqOH0Om6yTUWAaGQbsAsh40rvbMrar5mh1VxdPjmuyTAb2IwI9-b59E_YHhMo5sd0O0PGgtXsFfIxQRV727Jw38xCEmzPah5UoEK0NHEg5OljU7_F86--UJR1SDgXi6MTebvem6RT7FsCFP9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور دستهٔ آهو از مسیر پیاده‌روی مردم شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456041" target="_blank">📅 14:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456040">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d3c41147.mp4?token=WURhRAI9Y5lo6BZ7kr3cmLQPuR-ITsicoZ0qqHTO1kfNC53E1xxgPGVyQ7aN8VCUNLkHeuU3rofzJWzhGbyWhC0m--amAjKa1H-UGWqLEHX0epIqzxK0rmx9JeBMp3YKMkgi4He2pC8gZxHS-3Ym6briXAPuJmacOQJwcHf_nTo0lCSjZvPK7vg2k0NuiWxeRNUJ4gs8tegTRPXasvI9SW463qWar2OSVCBP020_aNZhaA_GyrW3lOwmjTVY1WIMawO82IIcorhCuRiLIF7Z62YUBu3-BRXIBALNVZcGtbcRm23MiXUVm8Binh0ikOK4PuCnUVE2fN6bijnoTSt3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d3c41147.mp4?token=WURhRAI9Y5lo6BZ7kr3cmLQPuR-ITsicoZ0qqHTO1kfNC53E1xxgPGVyQ7aN8VCUNLkHeuU3rofzJWzhGbyWhC0m--amAjKa1H-UGWqLEHX0epIqzxK0rmx9JeBMp3YKMkgi4He2pC8gZxHS-3Ym6briXAPuJmacOQJwcHf_nTo0lCSjZvPK7vg2k0NuiWxeRNUJ4gs8tegTRPXasvI9SW463qWar2OSVCBP020_aNZhaA_GyrW3lOwmjTVY1WIMawO82IIcorhCuRiLIF7Z62YUBu3-BRXIBALNVZcGtbcRm23MiXUVm8Binh0ikOK4PuCnUVE2fN6bijnoTSt3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استانداری آذربایجان‌غربی: حجم آب دریاچهٔ ارومیه نسبت به سال گذشته افزایش ۷ برابری داشته است.  عکس: مینا نوعی @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456040" target="_blank">📅 13:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456039">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPbkGKILxJo7pIdxmXkcFIakXdsKsubO_uflKz2AGLp-cA60027BO7sm_bjnBc7D2BHPv7JrMqik_W7g3-2GYQ42sf5-5lqfsoxeAPNSHa1HgxMxhxCK9eKKpbRzJQvo_DUIl_zjCU4qZt_Qxg335qxh5a9LN2is72LjKqlFq5ynnbKvwONrRnuOr2jiBr1H8-rzrUuwywPMOmogqQNQ6y5mYoBM_dlYLmolGDm6DQtedBgeby-61h8kv8Ypt31bwQ9RJjWDBb6SSMpJALq593NsjhWVu7NwLqwzCXs4J3IDva_uL_90U8sYAmh8UFhYnKYgNoSYRfJfj4HhWr1yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام تاریخ بازی روسیه و ایران
⚽️
تیم ملی فوتبال ایران ۷ مهر در ورزشگاه «کازان آرنا» به‌مصاف روسیه خواهد رفت.
🔸
فدراسیون فوتبال روسیه اعلام کرده است که این مسابقه به‌عنوان یک دیدار ملی رسمی در نظر گرفته می‌شود و نتیجهٔ آن در رنکینگ فیفا محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456039" target="_blank">📅 13:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8Lx0KVI5_UQWOKMfgXvSu_nI7PyKurREJ3c-O7ehB_cdePi0RlZ-cLpCJ4l6dha1Bbw_mEb3IU6O6FfnKPzMfIc0wtXblzf-WKqHTCwJOkEq1yE7t-hL3EMuuXf0GmW3ioDs5aqtaD2t8C7XC5Z3L78LWMuFGzyrqpwrp-i494dpYPRS2UqoyLmjhOvt2jGcgzwnd6JJX2Aqh7DnsASg8EZqXQLJeAfcEBbhexH7pDLMxwrnPHRVFNGBb8vFGlQTojcodIozhU1QyIzsGDOTuNrDi4768CTImaQwmeW6IR0Bb-fB_nWzn319pkE7VNz2XBpVYQowNQkBr23WU-Stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۹ ریشتر در عمق ۱۱ کیلومتری زمین، همت‌آباد خراسان‌رضوی را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456038" target="_blank">📅 13:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztVSWhf4Vqq6FTD4cwWGt_c8Y27Wkz1BY-Ig9ZfP4ArxKjMiLcEzRlz7lD0GVFp61PuzUPBEI_ZvmZAfr75G6NdE_mnLyk48aKdTu5AKCXx7mW_J33MamffqRF6c5Sei0FcQvLwoJrpF637n6wIbG8R5EpaLRVDokKq3tqa4qc0cti4tE4I4cfa3XWHnuOkwmtCz9iFxk6NHQZx7TCWl8VvHeEgfSgC6DuP2QbNBptfIFflMFKVusBBMaO-NDwYzpCBLHcO768ivelm3x6Wkdnc7_kJSsxIvhmOOS2hkqPu2KsHUWUcMgnA1AC2M9alNfdmOp8J9mCWEk3q3coyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهرم راهبردی ایران در خزر که نباید از دست برود
🔹
با توجه به فشارهای ایجادشده بر مسیرهای دریایی جنوب، اهمیت بنادر شمالی و اتصال ایران به روسیه، آسیای مرکزی و کریدور شمال-جنوب بیش از گذشته شده است.
🔹
بنادر شمالی می‌توانند هم در تأمین کالاهای اساسی و هم در صادرات…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456037" target="_blank">📅 13:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roYWPLH5xc11vPOnpoySE42_GvENIWSD2pBtKh0v6JoR872snolDIivn9EV1FgF6ppDk5mR3lFVj0oHfTXn5mFR-43AGHrdRgdaOA3RHwuoptx8J_ggbA2gf9fn7WSBAaguNWiWHsSNYeYcJWj8Ikj8KlIjx9DLE-M-PVF5Z_hP4P0QEMWEo8HzbNT4OYhqz_o9kd_BQrxjx21FgN7_TgqyGvQYD8oaclBdxQjR40eSyBR4C9NE_q7wRPa0CFUB28Zyt7eEMOUEVtbP_KdXSfw-nxXf74c_IeEoN53unWs5h3syi-gjJhqqlCRnZgi0hdETXgOjSHcAqUVX0QMVbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعتراف اعضای باند شرارت از اقدامات خود در خاش سیستان‌و‌بلوچستان  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456036" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456035">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234be4c0d1.mp4?token=PCwqt4OLoS-GbWIw6FVZPxcT00u8Z4gF8ezY8GVSgSwyssCInhUSGvplemNO1F_ynIrATBnCSGf6Pl7nJLWPjwKqm4YXa0OD46zb_8qvC6z5NMb7opNuIGJwIBjKN3BiZM-zXG3qrwaOfCeAUGHasAZh4MMiETMvwnjV74OkXHfj-od8JtYnxZKgu90dM8ybLocIR4sLjNP0T2hGcLH-_28Up1YpZEIn9RR172NWVNpQjPGDxoiMIKNP7L9oDM7zquTBOTM3MRf2alpou31GGPC-u8AH5vvlAYr2Cv0SQ0ByVeOrR3qQFbVkFB0dT8OSrp_waCeTBpUX5NIMfSJwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234be4c0d1.mp4?token=PCwqt4OLoS-GbWIw6FVZPxcT00u8Z4gF8ezY8GVSgSwyssCInhUSGvplemNO1F_ynIrATBnCSGf6Pl7nJLWPjwKqm4YXa0OD46zb_8qvC6z5NMb7opNuIGJwIBjKN3BiZM-zXG3qrwaOfCeAUGHasAZh4MMiETMvwnjV74OkXHfj-od8JtYnxZKgu90dM8ybLocIR4sLjNP0T2hGcLH-_28Up1YpZEIn9RR172NWVNpQjPGDxoiMIKNP7L9oDM7zquTBOTM3MRf2alpou31GGPC-u8AH5vvlAYr2Cv0SQ0ByVeOrR3qQFbVkFB0dT8OSrp_waCeTBpUX5NIMfSJwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدهٔ مدیر استقلال: پنجرهٔ نقل‌و‌انتقالات تیم ۴ شهریور باز می‌شود و ۳ سهمیهٔ بازیکن از فیفا می‌گیریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456035" target="_blank">📅 13:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456034">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منبع دولتی: افزایش قیمت بنزین فعلاً منتفی شد
🔹
یک منبع در دولت در گفت‌وگو با فارس اعلام کرد که موضوع افزایش قیمت بنزین فعلاً منتفی و اجرای هرگونه تصمیم در این زمینه متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456034" target="_blank">📅 13:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456033">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
انفجار بمب در میان نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های لبنانی خبر دادند که یک بمب ضدنفری در داخل یکی از منازل در جنوب لبنان به هنگام حضور نظامیان صهیونیست در آن منفجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456033" target="_blank">📅 12:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoEcyKi6IWwsBg1ftLSq7XbQCzqN5vx1XFyBF590-a8vQyxsFNeOUD_dYbFg_M5eILgEVEQaLWWubpxYPzVr0NEhymn45BcbJNoWugTcrwv0KEk2MRF7Bb6p4OSKYmEs9DFdirl9OWSK8tElzqky3eJIt8qieMZu1-UCGfyljXH08X5LW4CtkXIUhNyTIuwnKUpHsn8XpxlNRwnohFbwcc2PZ9MJ1zbZ82SiFOm1IZdBILZ33-w8wlnKGU89cmLw6QEyyxgcx2mf5waqAVNPUzJNSpNSh6b_zm2G50wqbFL3NMXaKK6c8g9JJgkkxeP7_InAv-17qdsv3eTt0S5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه کاروان تسلیحاتی اوکراین را در دریای سیاه منهدم کرد
🔹
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور شب گذشته با پهپادهای تهاجمی، ۲ شناور اسکورت‌کنندهٔ کاروان تسلیحاتی اوکراین را در دریای سیاه هدف قرار داده‌اند.
🔹
این وزارتخانه همچنین تأکید کرده…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456032" target="_blank">📅 12:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ionuZoa65VDXprWoXysix72aslYTaGX-RK6qn8yXNWzEOvtEvReUYYfRcqQIC_N4DKvrEw6Z9t37zN-GewGZqOZWTjoGs4KwNIsiilNg8-rIuyLJGG52JPLf5fnkQbUj21jvcxDid1J9RMQeU-WqfijSpzkhtPKBPz-GzWBodwUjdLbEdE4xJAP0Sy6oQQ0CUWDV24euQ6HbSNFW8IXPkP0O6DO6GpqZGoRq7bt8my05p_U5HGtmBmsA-EWc25IR-u_D8zowTsABnnvZrcX-My6y0SvzJofi4R9xLvLi9otlwncXpYtKEii9Jdf3U5NYskR459yk9MY5G5RK4wXGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۳۰۰ درصدی صادرات ایران به اروپا از مرز رازی
🔹
سرپرست گمرک رازی خوی: در ۴ ماههٔ امسال ۲۱۷ میلیون دلار کالا به وزن ۴۴۰ هزار تن از مرز رازی صادر شده که ارزش صادرات با رشد ۳۰۰ درصدی و وزن کالاهای صادراتی با افزایش ۲۹۳ درصدی همراه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456031" target="_blank">📅 12:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456030">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خنثی‌سازی ۴ روزه مهمات در سیستان‌وبلوچستان
🔹
فرمانداری کنارک: عملیات خنثی‌سازی مهمات عمل‌نکرده در محدوده نظامی بندر کنارک از عصر امروز آغاز و تا ۲۶ مرداد در نوبت‌های صبح و عصر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456030" target="_blank">📅 12:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456029">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=RKnYypsFlv3v4qmBP-nCzQwhf7RMp1vKOUQaIC6kgAwPs0IrnuXWyPpeuSTZTpqED07U0bDblQJKj4vKJ1ImcuTsqACPJTgP7n2wp6ily7G0MITqr5gNzjSTb7A6ldZ8UDibgjZZ76GbJN7VbXiqi0R-_XQnLgjobsZrSw4t_DmV7wbHRDXkzGF4bgIldYgZhqG9IhpkwwIlfPSpAW_0Jr6JQKS6uTbVu6IjPyRdeqdW0ig-vtJWR74iilBocgu8zmmS3pCUpEoJjYE55Y7-L7vfJ_ADwH81iHQkYsjid5XaKQncRwKQ9SUUuu8vC_0tuGw4mhuTcSYq8S_v7Hy9XzF-Rk9ztYJ32gFt1dGcBIidE_BZ2DJ1-7GBIoxg6-s9YHLMvZ7HFledjFGo9vJDcQmpijY6kb-r97NVzX_SagmTP8imMQJS-T8YMKhR-2hi79Z-myPSMuZVlipuh__dlQvO-yZ2kxyCUTTD2Phksd49Sg6OXDXoSbbZiyHHyKH-gNJbDfJs1Vle55AEJx00mkt_TlHGBkOGNUhISgv8YpI_6OaiURSfYbuD-o9ou8wa58KxVqLAWeos2Lwcv0zpusJdvuyqBcmod0MPyRYO-Xd8-lhmAKGY4EWwkcm_rO0zVT33DbEhWtC6Gcp0i1GkME-W9nXgXwtz2-VxOfv1Nj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=RKnYypsFlv3v4qmBP-nCzQwhf7RMp1vKOUQaIC6kgAwPs0IrnuXWyPpeuSTZTpqED07U0bDblQJKj4vKJ1ImcuTsqACPJTgP7n2wp6ily7G0MITqr5gNzjSTb7A6ldZ8UDibgjZZ76GbJN7VbXiqi0R-_XQnLgjobsZrSw4t_DmV7wbHRDXkzGF4bgIldYgZhqG9IhpkwwIlfPSpAW_0Jr6JQKS6uTbVu6IjPyRdeqdW0ig-vtJWR74iilBocgu8zmmS3pCUpEoJjYE55Y7-L7vfJ_ADwH81iHQkYsjid5XaKQncRwKQ9SUUuu8vC_0tuGw4mhuTcSYq8S_v7Hy9XzF-Rk9ztYJ32gFt1dGcBIidE_BZ2DJ1-7GBIoxg6-s9YHLMvZ7HFledjFGo9vJDcQmpijY6kb-r97NVzX_SagmTP8imMQJS-T8YMKhR-2hi79Z-myPSMuZVlipuh__dlQvO-yZ2kxyCUTTD2Phksd49Sg6OXDXoSbbZiyHHyKH-gNJbDfJs1Vle55AEJx00mkt_TlHGBkOGNUhISgv8YpI_6OaiURSfYbuD-o9ou8wa58KxVqLAWeos2Lwcv0zpusJdvuyqBcmod0MPyRYO-Xd8-lhmAKGY4EWwkcm_rO0zVT33DbEhWtC6Gcp0i1GkME-W9nXgXwtz2-VxOfv1Nj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشستهٔ ارتش اردن از بحران‌ها و معضلات آمریکا در جنگ‌افروزی علیه ایران روایت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456029" target="_blank">📅 12:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM547UppkE1YR2oRHU_wiGkE-jIRcEjnQ2BhbG4mFStpAlgrrNTOxcRfKnDOa-0D7rtUVUXy-6YXcJkJppo8ZvhjSIWH_z2C_WuYNcykzR-7BVB1Quo0v96Djh_F8oxN8gcAypx2B2DguX5VrWZ0zjeEvON7e9ExFBbwkUSX87lUG2yeMUTzyz25-bbBpRg65fjN5O_ct3nFR58FZj9L3HGS7ntBYhkfUvBpWhJcJzde2A5uu63kdcJyFBNnmK1AipSylWG1NmQH20qBsP913XvPgdh1kEc1wnJufA40zuJCRCoPgCNaq260JUgFZb5mCw9LP4dPDDjLHXkjZC9BDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش در تنگهٔ هرمز
🔹
به‌گزارش سازمان عملیات دریایی انگلیس یک نفتکش حین خروج از تنگهٔ هرمز در آب‌های نزدیک شرق شهرک بندری «الخصب» مورد اصابت یک پهپاد قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456027" target="_blank">📅 11:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اطلاعیهٔ جدید وزارت رفاه در مورد احراز افراد غیرمقیم
🔹
وزارت رفاه: افرادی که پیامک احراز سکونت دریافت کرده‌اند و مشکل دسترسی به دفاتر پیشخوان دولت دارند تا پنجم شهریور، ۲ اقدام زیر را انجام دهند:
‌
🔹
با استفاده از خط موبایل متعلق به سرپرست خانوار کد دستوری #1463*500* را شماره‌گیری کرده و  پس‌از ارسال کد ملی سرپرست خانوار، کدملی اعضای خانوار که پیامک احراز دریافت کرده‌اند را ثبت نموده و متعهد شود که ایشان در کشور حضور دارند.
‌
🔹
سرپرست خانوار اگر آخرین محل سکونت خانواده را در سامانهٔ ملی املاک و اسکان ثبت نکرده، به‌صورت خوداظهاری و اینترنتی تا آخر مرداد محل سکونت و حساب شخصی خود را در سامانهٔ ملی املاک و اسکان کشور تکمیل کند.
🔹
پس‌از ۲ اقدام بالا و تایید سامانهٔ املاک و اسکان، شارژ مرداد کالابرگ این افراد در پنجم شهریور پرداخت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456026" target="_blank">📅 11:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dfe94e92.mp4?token=Q3OWkiq2kl-ljmgTkLxsyiss4es3IE0kPQMRkizW1LZmAPCQbswbkRYdybBv9PQinbZGzPueD7YugBAeMAwpMkJwo3Fi-6NhzGDFTXB_miBm_eDzC--fLw-Z3l2avyTA0wt7-dk7lA6WffoxhGBbxFl5l8XzPo8U4OPJe6B1Egg_N6_sXvEAg8nvdM1kzwVTSm6z8K5wp4XnOztZs0Gjv1y7Sm2B9FqbTwBMEaqI2rx6If_WI2ivcgVqldwsz_MWg7S7Eb3k7NeVcS15SxVJECIGrZKjWB6OKvnbXheD__K_ieQt_3A9jHpcCjhYlLXnsr5Ia96N5w4vKNJ30vDHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dfe94e92.mp4?token=Q3OWkiq2kl-ljmgTkLxsyiss4es3IE0kPQMRkizW1LZmAPCQbswbkRYdybBv9PQinbZGzPueD7YugBAeMAwpMkJwo3Fi-6NhzGDFTXB_miBm_eDzC--fLw-Z3l2avyTA0wt7-dk7lA6WffoxhGBbxFl5l8XzPo8U4OPJe6B1Egg_N6_sXvEAg8nvdM1kzwVTSm6z8K5wp4XnOztZs0Gjv1y7Sm2B9FqbTwBMEaqI2rx6If_WI2ivcgVqldwsz_MWg7S7Eb3k7NeVcS15SxVJECIGrZKjWB6OKvnbXheD__K_ieQt_3A9jHpcCjhYlLXnsr5Ia96N5w4vKNJ30vDHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طفره‌رفتن وزیر آمریکایی از پاسخ به سوالی دربارهٔ کنترل تنگهٔ هرمز
🔹
مجری فاکس‌نیوز در مصاحبه با وزیر انرژی آمریکا از او پرسید: «آقای وزیر، شما می‌توانید اذعان کنید که آمریکا کنترل کامل تنگهٔ هرمز را در دست ندارد، غیر از این است؟»
🔹
وزیر انرژی آمریکا اما در پاسخ گفت: «ایران تلاش می‌کند تا اقتصاد جهانی را گروگان بگیرد و همسایگان خود را مرعوب کند. آنها یک زرادخانه عظیم ایجاد کرده‌اند، بنابراین آیا در منطقه مشکل ایجاد می‌کنند؟ کاملاً. اما توانایی آنها برای ایجاد مشکلات رو به کاهش است. توانایی ما برای اسکورت و خارج کردن محصولات از آن منطقه درحال افزایش است. آنها تقریباً یک برگ برنده دارند و فایدهٔ آن درحال کاهش است».
🔹
مجری شبکه فاکس‌نیوز نیز در واکنش به این جملات مبهم و متناقض وزیر آمریکایی تصریح کرد: «این اصلا به معنای کنترل کامل [بر تنگهٔ هرمز] نیست!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456025" target="_blank">📅 11:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روسیه کاروان تسلیحاتی اوکراین را در دریای سیاه منهدم کرد
🔹
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور شب گذشته با پهپادهای تهاجمی، ۲ شناور اسکورت‌کنندهٔ کاروان تسلیحاتی اوکراین را در دریای سیاه هدف قرار داده‌اند.
🔹
این وزارتخانه همچنین تأکید کرده است که نیروهای مسلح این کشور به حملات خود علیه زیرساخت‌های بندری اوکراین و شناورهای دریایی که در خدمت منافع نیروهای مسلح اوکراین به‌کار گرفته می‌شوند، ادامه می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456024" target="_blank">📅 11:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE5-Srx1KUW11ofG_jyPzZt7_6zsuFrORo1NpYygq8d92WAfv_odaDEYtKqjm0gBcBpHpojR-O3GbbbCKNsP1Swf_zzlk7UGVMW-f3jbUcIIGZ9zcRJIGprMAUrIRXei8JPETQ-XA-inJJkVV3ZnMm7kqUImmBDPv1doUI-L6RWn2l6VVZje7oiOUUXdb4IDzXhvqF2yqkFExlcbtfQGlJOGXEaU9wRbG7ZON63oqIJ4BYKvb7f2RyH14ZylhJUfXnw_XG60LlK2HJNfFqR8mZ6bCB8q9W912fiZe-07vQE8GRIXnYQb-L3NfX-SM_dsWB7TBlBXEHP9G77yftXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار فرماندهٔ سنتکام با ولیعهد سعودی دربارهٔ تحولات منطقه
🔹
به گزارش خبرگزاری رسمی عربستان سعودی، فرماندهٔ سنتکام با بن‌سلمان امروز در شهر جده دیدار کردند و دو طرف در جریان آن، روابط و همکاری‌های دفاعی میان ریاض و واشنگتن را مورد بررسی قرار دادند.
🔹
براساس این گزارش، آخرین تحولات منطقه و تلاش‌های مشترک برای کاهش تنش‌ها نیز از دیگر محورهای این گفت‌وگو بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456023" target="_blank">📅 10:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456022">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ec695dbb.mp4?token=U9mqqDILfkwobgopRU5cHRA_Icl0TJ9PL9ECPZz3sUD8kroVmpz55bFZXJqz4Pr_kukGD8fnjwxCU-wVuHe9GfaXc0_D3uXDQaYpqRd6UXv_r93-IgC6TwRkIYKF4ZpSm6mEXHl93xoIpL391vjloFnrQMCUhGqEqNh9m7lFTMF8kSdoEQ9kHK6AOi4dsPbsVwfEU8CAJVXKS2zXbu8f6trLhhtrFphD-jeInhIC5oOqR82dg7En14AyJhy_-MZlEG9nnMYAeKqufQacOkt_3MaMPGBtXEnN9k5UuB3qDjAGR48A-NV0e_J3S7nMjtA-1TFjnqlo7wpnf9pw1_38hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ec695dbb.mp4?token=U9mqqDILfkwobgopRU5cHRA_Icl0TJ9PL9ECPZz3sUD8kroVmpz55bFZXJqz4Pr_kukGD8fnjwxCU-wVuHe9GfaXc0_D3uXDQaYpqRd6UXv_r93-IgC6TwRkIYKF4ZpSm6mEXHl93xoIpL391vjloFnrQMCUhGqEqNh9m7lFTMF8kSdoEQ9kHK6AOi4dsPbsVwfEU8CAJVXKS2zXbu8f6trLhhtrFphD-jeInhIC5oOqR82dg7En14AyJhy_-MZlEG9nnMYAeKqufQacOkt_3MaMPGBtXEnN9k5UuB3qDjAGR48A-NV0e_J3S7nMjtA-1TFjnqlo7wpnf9pw1_38hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات ثروتش را به آتش کشید
🔹
تصاویر ماهواره‌ای نشان می‌دهد امارات گاز طبیعی که تا قبل از این صادر می‌کرد را در دودکش‌های فلر می‌سوزاند.
🔸
به‌دنبال ناتوانی امارات در گذر امن از تنگهٔ هرمز، صادرات گاز این کشور به صفر رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456022" target="_blank">📅 10:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVr2YnNQI0ORvaEIpkI7eaUeMFjK-nKpojNJOZe4mYcAw3WyKi_dzpRd8V-kLxrlKsZK75kJgr3ZZGA0nu-sB4yODJSxbj4S9jZVyUT4GPeFSQieSQFGWxP9siZWRVdrkVXL3qcUT4hgkFfJ12VBoRDwZd1QnBI6wl6Qicqu7A3TmP8K4tpcNUlY7K3seb_ovM3tTth-qUbn4QpiooeDqcBp2lV1f3rGx05cnC5nl6N_HVEEg3jMQqU5fg8mcLHiRZcY2aRi3plL_njKmlhgqcIEFqOCUpNAZmxWgHDGQ8aZG8MQBxugZz-1RDos5BSEQZxqnTcM65uSieg4mNBJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9o1k4EgRCmFgb0yGGbvz6JilouI25nh-E3V82u3HPfCv3vNNkAmll96DQwUT9VTqgUsPDOcKD_KVAF2WupbRv1bxb0dgQ_rsaEUaq78F69M_ACbnWSGPp5N76AkWY5lrp0n4S7tEwOwXzvNqJP2C-5CP7j-QGA3A8wC_QxwS2u8DC80Rvz9UA4jA-s71GxwgC5REu95KMEvimGQOVvCUgjNkurMQ93ipJtGHJOsJd_okr0sXA324E00ASrbHP4Kqro6dNmq4JZrFgmCh8WcwRzo4-xQdLlxL61VnGetAe0euC9R2FawI1QRMvv_RyiJEZm2_tasW4GOPT4W8_INKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gC1tJ_2d9kEacGG3Di9vsnXomP0qQnoFxs6k7R1BTcYLDKRYFLHQyNwf8HSx0IKg7afh9pmdq3I1r-jMiQnVDl0-x4-UbqsKV0rblLsgSNKoC0yJHhWO9oXBM8M4VBdCuIrvP0Rpl5I7UQmY9OMim5Z3qGVto3-na9VuK9kQdSD2CoqUnTH-OdSwRAN_dnFFmjF1TEtKSd7Lu2OHVQObpHERrP1QHTK4_K6AWGR9_dSqp3Zdd0WvTXDFIClBVuhCgturm68D3GV6V_ukBi6GLOgAHzQMWJbF4M6vcOO7hWCT07VCAAu5spY3NTfDnzTGTklc8nuYu_JGDqxke8n1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLEeSO9QEcKf_pe9vLelFWs_2iFLgp5qd6nA5IDO2U3wc0itwXNk6ZUgbFQ6q7qvbAro7kjOwbzSXhiwXJLRGTGrcEuVlRJ4uQaM4Gx7ymEnlhgntgb7QAJ3DuQEw11ygx8Pmh7KPJPwvN9TlH__dqvoUFhzD9OAiAr8kZ-Mz-hJRRQHdG4mVadouhEH10a5QBBFWkmtNwHYIgYAGW6CQqvPL_NUqZkiRbpxuZPgzeOrkIJBwBA-krjcbmS7i0PEOPYfcc5xxDurNVwDpaPHqD0f_9eYXXru6x_dZcNGY09Bg7GT9KC_w47hbm0GGgacFLAg7Q5Xb77nmag6s66jRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vautql-UKTPxVVvGiPXeWZUK4cIKpiftdsjQT4FbZXq2qqcJXTL7FaqUpsrP6wRCgPOhRb0TPMGacgRvqkY5PRwW999lAX8F4nQ4K2yBdxBJ4QpyCLXqhUe7W-GCmZmG5PCvwhf6Y1CSTIYaBytxVUp81gjsVnBMwGEj7IpyPnzJzCgVht2U0a4YSSJM4xEq3kTBOUP8aMT0JNySyVRel61Vlv4jG4Zo1iChjJQMUhpmR5VE3OTMuej9uHaa4UN8Ji69ZR5BPhHACzFoW7Csn8NQ2q6vsJh9hD7750hc-a8mue5EfOpeFo1oXgHsz0T7bWnvrDN4Ugrul9vufm_IeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7R2kaz7qvMWTqlJMFqYOODy7N3VEkhkjNThesl_2GtNvRApBY2CmRCNmTxtAHOsbPDHzMw-x2fdnGuODq712B6MXcBJV-G-JIYId2U-HVLR7aivYSK_KK24Oljoy4L-iI-FjUqVfogzxv7orNqDZfpA0dnNFEGUgJ3XvgsXbDFprymiU9TssR1yTkFL1O9gjlFlq9awtR1qqh59jsghxON-dtaBNt9Hzt11-gWVxvg32NOP6EKYAQFpPct2RSHQy81Yex4aN1ChZKRH0gRhJkvbb-vCeJYCKoFA8IsMkuUeTM8P-8Mwt1bxrnNYmTXQCBNZxpYm9DOmbVZeGIinFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaf8EBxdUHZ75nPSzJcZ2I50tS4iBdW_GIj5t7UKlNg4g6aTU6zT0SwVRyVfvETtVhrcTI8Rgu0t2BtslA-uaSZNA-gnC-2_2Vcw53BXxy0j1A0WLz81PYG17n2-UV763UDpnw4Rg4Wtuyaxff5L19hucLAyEfet2HvtDSKZMIBVpsHRicnul5ZEPzv9yVfM43q6cJ0XrR1VvB4nHoN9yvcEvFvtT7Eq7tEc35yC9MadGu7L2fiY37UObD4wLYDsA1xEdxvFO89tSatbJIezSfxBWP1lkBP1i7pspS6gnfLFYaLf6tR-A6ZeeINay3EbplhHci4xxZeK-Ld3DCFC8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علما و مراجع تقلید در دیدار با رئیس سازمان بسیج چه گفتند
🔸
آیت‌الله مکارم شیرازی: بسیج شجره طیبه‌ای است که مردم و کشور در طول سال‌ها از ثمرات آن بهره‌مند شده‌اند.
🔹
آیت‌الله سبحانی: ثبت‌نام ده‌ها میلیونی «جانفدا» تنها یک عدد نیست؛ نشانه‌ای از ظرفیتی عظیم است…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456015" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SflckSNqUh4yqTJrA29AKXt3yfNeOqgAQ3VccF50cOK5GrnhWoUyEuf71F784hhJP9SAFaAw64JlMvye1uIY38iwc-Mj76jV1mUI-fzYe7Lq8mspcBJ0vCQzAwZdUprcc2zLNHGONDL-rc0Qe3JnxwKKgjiExtHbgXoCg56tGEtBzQzqKY5TB1vHvZOtoD8a3bg77VOaSmbJaD5PJcAelG4XxGLVzv4le92LAuSlYvHBT3nVWDfDEdl4M7QK3Z9-eGIyKmJwTSK3623FOH5ch9ozEPot1tM115hljs02WQmmeU8C-ikoq3MKKZmfT2cbw5EPRJrnB1hXqhVpFf2CDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تبریک پزشکیان به‌مناسبت سالگرد استقلال پاکستان
🔹
رئیس‌جمهور در پیامی فرارسیدن هفتادونهمین سالگرد استقلال جمهوری اسلامی پاکستان را به نخست‌وزیر، دولت و ملت این کشور تبریک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456014" target="_blank">📅 10:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GODe0y8V7PCI3Fb_WdzXqJS7gGmHBUjiuhDyx8RwjApekDR9FnxZ8LqcWtAIjOHu0TBCk3UobF9dyXRLQQ7FcBjV_dcxTVzSsIDLAAwIk9WXr8tZTNbMawwOz9Pc41Ql6qxFqKghwefsftmZDoJisP8dpOGolg8A4gE9eYxlE1hsKN_vzadFuZfoeN027PhewHpAvtw166yjpjfoEn_io6IEj0621qvRn-j-fnXLCnQc5YpO2Lp27PmhkIdiKvPPpiCnWs3g6FJXl6iuvpUVXBAqt6B-SwuF9yhE4QsuS1fhVue55lf-qrYDAm4SDXM4h3qcQpslx89XfkPKpItt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار قاطع ایران به الجولانی
🔹
پایگاه خبری لبنانی «یونیوز» به نقل از منابع مطلع اعلام کرد ایران سناریوی مداخله نظامی شورشیان سوری در لبنان را که بنا بر درخواست آمریکا در حال تدارک بود، خنثی ساخت و با ارسال هشداری مستقیم به دمشق اعلام کرد که هرگونه ورود نظامی به خاک لبنان، با فعال‌سازی جبهه‌های متعدد در داخل سوریه و در مرزهای آن مواجه خواهد شد.
🔹
یونیوز افزود: هشدار ایران شامل تهدید به فعال‌سازی مرزهای سوریه و عراق، گشودن خط درگیری در حمص، حمایت از تحرکات علوی‌ها در ساحل سوریه و تشویق کُردها برای بازگشت میدانی به پیرامون حلب بود و این هشدار  فقط خطاب به دمشق نبود، بلکه به آنکارا، بغداد، دوحه و ریاض نیز منتقل شد. این هشدار حامل این پیام بود که هرگونه ماجراجویی سوریه علیه حزب‌الله در لبنان، محدود به دشت بقاع  نخواهد ماند و ممکن است به رویارویی منطقه‌ای گسترده‌ای در داخل جغرافیای سوریه تبدیل شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456013" target="_blank">📅 10:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456012" target="_blank">📅 09:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7TGEUTg42NdYZacTxTCvPlVgMpphWpkCvTvFJ4CyKABgwXCJ0rm746-OibNEXeZ41_az2MG3AC243cpbAUoo1ikJt2ChIOuNh2kF6agBajSzGc8-hSC_eZi6yy97Dp3Uhb9Wa_dF0PucYdzzsBOYHqBG3Ns9AvZWDY186T337HAa21lG3O96B5EGXZgj-X-nr84FzIKh-UMUENUyVQjSnSFqTLVkqjpskqc34bz8o9TgSWiF-i7NNRzzsS0WJkzYroGMmWKnNH-xNbLzD3APt73tUVl9_2GEmDLlSVGgriEGmnir2rmH-rcKbLzJyh-t31h0QbU0_dhtujOYb_KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کرهٔ شمالی به واشنگتن و سئول: پاسخ ما قاطعانه خواهد بود
🔹
وزارت خارجهٔ کرهٔ شمالی: رزمایش مشترک آمریکا و کرهٔ جنوبی تمرین یک جنگ تجاوزکاران است؛ این مانورها سطح متفاوتی از بی‌ثباتی را در منطقه ایجاد می‌کند.
🔹
اصل همیشگی ما برای تأمین امنیت این است که به تهدید در سطح جدید، با بازدارندگی در سطح جدید پاسخ دهیم.
🔹
موضع خود در برابر دشمنان را برای مقابله با هرگونه تهدید و چالشی از طریق اعمال مسئولانه و قاطعانه حق دفاع مشروع از خود، با وضوح بیشتری بیان خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456011" target="_blank">📅 09:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2e9e57b6.mp4?token=chhMpVgr8T9qSos4adA0zjlBldyfdVQHfoq1wQ2twP-LA9ZvUHRZZUjW8-nti9ecQFsj3k_98avtOV9IC6gxBgj3dsMBC-G7kOw12YH7jasv6WIhMYNsW90j846VAtLXjxXZEvpfH8nYuKpFnmVhI2xLL098HMXjp_-WtFscN0I_5G0-oxVviENXKc2yy-_rzydvszanwRob5PvQrZvTizz1Ulkr9NW8Ynt6xUEUpTA74ZsMWeNCcArpgpVho7yvWoxl2d_bbwAYnQw14oSR0pblTXMlJBPLM994V0msBxuNH05TrqUJUIQ6iI0WuMtNjNRaQuFZH0Ucp1-EiSZawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2e9e57b6.mp4?token=chhMpVgr8T9qSos4adA0zjlBldyfdVQHfoq1wQ2twP-LA9ZvUHRZZUjW8-nti9ecQFsj3k_98avtOV9IC6gxBgj3dsMBC-G7kOw12YH7jasv6WIhMYNsW90j846VAtLXjxXZEvpfH8nYuKpFnmVhI2xLL098HMXjp_-WtFscN0I_5G0-oxVviENXKc2yy-_rzydvszanwRob5PvQrZvTizz1Ulkr9NW8Ynt6xUEUpTA74ZsMWeNCcArpgpVho7yvWoxl2d_bbwAYnQw14oSR0pblTXMlJBPLM994V0msBxuNH05TrqUJUIQ6iI0WuMtNjNRaQuFZH0Ucp1-EiSZawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنجکاوی خرس قهوه‌ای در جنگل‌های رامسر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456010" target="_blank">📅 09:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyeHzO5gUkg8wTlCM-XdDy4ynG9ajR1FqTib5gPTh4JL1qE3-V9VNsYu7lj0Zq7qoCusp3rtnJHWUu2V13hUlUMT6iGUyUWn1ICETHgZeRKZ4fWOvQiJoxeFB4Geri0JK0swC5sB1E5IqH--sHiDgC0UJQGEEG67PaoNbn4DJjADgR_VmvJ5yyv8veHnJmWv_NVkhEK_y9lUj7EiS4fOc5--U4TuGZb1cd-ABOhnfGCe0s0QWczXzCskog_W4YDTBsPedbTv2tNn14B6cuOfhqc6rYhy7tfIjDw0dljV-YpiCn58MUWH-SgLst5tJSQkJqZqIfKW2KvGcvFbXqoxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل قبول هوا در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۱ قرار گرفته و در وضعیت قابل قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456009" target="_blank">📅 09:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_OWb9EOU_-Ez09SP_DLWVPEq23K9bBb_PwkuniWjFQQZ2fNiYVAcKlsZmcMD5bRWoRApzmsK2_KM4vWNb8MZ5PL86DVcetoPiKkAgu3zTqI1M1EegXco9OlGa1EmhCCLOP8PYvtZ8lXIWiD_ybAwFqEMH5ZqeMmTpii2xTlE6mU4jrOhUcayTJ6CTViISvfiPzsgYVKk3qeyRalTgcWLW07L4CPpHVJtZK_U2pNSSR6PMQPw68KwA9KJ4YYcKjPu4B3UNHpJn2P60QV-ciep5etMRLqsw-ZM-S7lZ19NSfJGdzjZNa3UuHyw4o0JurMtNQ0P6GoNJlQ_h5_9ZoRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۳ ریشتر در عمق ۱۵ کیلومتری زمین، مورموری ایلام را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456008" target="_blank">📅 09:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جزئیات محدودیت یک‌طرفه در جاده‌های شمال
🔹
پلیس‌راه مازندران: باتوجه به افزایش حجم تردد، از ساعت ۸ امروز  محدودیت تردد تمامی وسایل نقلیه در مسیر جنوب به شمال آزادراه و جادهٔ کندوان اجرا شد.
🔹
حدود ساعت ۱۱ از مسیر شمال به جنوب خروجی مرزن‌آباد نیز محدودیت یک‌طرفه اجرا خواهد شد.
🔹
جادهٔ هراز هم به‌صورت مقطعی در محدوده‌های تونل سپاسد، پليس‌راه لاریجان و گزنگ تا لاسم یک‌طرفه می‌شود.
🔹
با اعلام مرکز مدیریت راه، تردد در مسیر جنوب به شمال آزادراه جادهٔ چالوس نیز ممنوع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456007" target="_blank">📅 08:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ1LdllN58jNUVFSRM3W3ZAecZfii69b89AN4pJtn4q4hcldyeXFqzcfTCPhNCS6OmdFS0ZOqWQJcGrhISY-IN_W0VY1nzCBuf6QaauiXzGmMecpxX_hWayQk59R5O0X2T6M1S4A18393seTSsudYMktlGlePQi_BN_1h3-Fwf6P5njL-pXGxvXTs5o6x6xL5xUZNYu3i-K_rAn-E9NKHVybi9oox3pU6OQsRANkc1OqHTnydHq8YriYTeRG4K8E20dWKLnlH86kRqRUf_U_mHxz6iiMrOeVohdDP_1tSYf4xqQpKF9SGY2km3SYfghGULAUASzkVNg4IXc8hyInBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثر وارونۀ حمایت ترامپ از رئیس فیفا
🔹
«حمایت ترامپ از اینفانتینو باعث تسریع برکناری رئیس فیفا شد»؛ این محتوای گزارش امروز(چهارشنبه) گاردین از نتیجه حمایت علنی ترامپ از اینفانتینو در سخت‌ترین دوران ریاست ١٠ ساله‌اش است.  ترامپ روز گذشته علناً در صفحه خود نوشت:…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456006" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVdjBu91eJUgjefvP09UUwfyEb7Qh5dOSJ4bOnyGJsyQYzmFAJTM1vJSobBFj6yq3YzfNqIw6uj9KqsqRN5NKl_vhwOa3Amak5va-5BaLmCCmaajBtUfoebkQfbbotVSPLTf7fWaS_y_cNjFmjwdCaak7T6f4plrG4T-lIJ0RNXeQy7CrxDNwdndybAe8tARDUJIG5-0h8klHmEeSw9ygY3oV8rJ9YSw2BWvM6RuDBeFZTMT2Oi-gtcFkpDuMCajhIGC-UueQ6HqdmpjUs-_lI59jfwQYhvh5dOCaehm-ATq0JpVNqZDuvEkA-lGtqOqAyGCpxuvCZGLQF69r9GWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمنی‌ها قفل باب‌المندب را محکم زدند
🔹
شرکت انگلیسی ویندوارد امروز گزارش داد که ۴ روز است که تهدیدهای یمنی به عمق آب‌های سرزمینی عربستان نفوذ کرده تا تنها راه باقی‌مانده برای فرار کشتی‌های سعودی با دورزدن قارهٔ آفریقا هم بسته شود.
🔹
طبق گزارش‌های کپلر، صادرات…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456005" target="_blank">📅 08:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلاش پنتاگون برای پنهان کردن اقدام به خودکشی یک ملوان در ناو لینلکن
🔹
همسر یکی از نظامیان مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» که هفته گذشته اقدام به خودکشی کرده و خود را به دریا انداخته بود در گفتگویی اختصاصی با رسانه «ام‌اس ناو» به افشاگری درباره تلاش پنتاگون جهت مخفی نگاه داشتن این حادثه پرداخته است.
🔹
وی که خواسته نامش فاش نشود تا جزئیات مربوط به سلامت روانی همسرش محفوظ بماند گفت مقامات نیروی دریایی آمریکا تا چهار روز پس از اقدام به خودکشی همسرش هیچ تماسی با او نگرفته بودند.
🔹
او تصریح کرده که همسرش به مدت یک ساعت در آب بوده اما در نهایت نجات داده شده و اکنون تحت مداوا است.
🔹
وی گفت: «به نظرم برخورد آن‌ها بسیار ضعیف بود، چون نه به من اطلاع دادند و نه می‌خواستند من چیزی بفهمم؛ آن‌ها فقط تلاش می‌کردند موضوع را مخفی نگه دارند.»
🔹
همسر این نظامی آمریکایی افزود از طریق پیام یکی از دوستان همسرش روی کشتی متوجه این اقدام به خودکشی شده است؛ دوستی که ابتدا خبر داد فردی از گردان آن‌ها به دریا افتاده و سپس تأیید کرد که آن فرد همسر او بوده است.
🔹
وی پس از عدم موفقیت در برقراری تماس با همسرش، به نماینده خانواده‌های کشتی مراجعه کرد تا اطلاعات بیشتری به دست آورد.
🔹
در نشستی با حضور نزدیک به ۲۰۰ نفر در تالاری در پایگاه هوایی دریایی «نورث آیلند» در سان‌دیه‌گو در تاریخ ۶ اوت، خانواده‌ها بارها «هونگ کائو»، سرپرست وزارت نیروی دریایی آمریکا و دیگر فرماندهان را درباره گزارش‌های سقوط یک ملوان به دریا مورد بازخواست قرار دادند.
🔹
یکی از فرماندهان در پاسخ گفت که از موضوع مطلع است و تحقیقات جریان دارد، اما افزود در آن زمان مشخص نبود که ملوان خود را به دریا انداخته یا سقوط کرده است.
🔹
به گفته دو تن از حاضران، این سخن با خشم شدید حاضرین روبه‌رو شد. این مقام سپس ادعا کرد ملوان به کشتی بازگردانده شده و به نظر می‌رسد «حالش خوب است» که این جمله نیز با اعتراض و استهزای حاضرین همراه شد.
🔹
روز جمعه ۷ اوت، یک روز پس از آن نشست پرتنش، همسر ملوان مورد نظر بالاخره یک پیام رسمی از نیروی دریایی آمریکا دریافت کرد که به او اطلاع داده شده بود همسرش اقدام به خودکشی کرده اما اکنون صحیح و سالم است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456004" target="_blank">📅 07:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aea5d5547.mp4?token=EvOf5VYWutjWr-oRS1tNYEVCMEzVuYDNLKvcbAzBzNQSvye-3x3Tqz0oqq6zljmuLJi2gINvquQxNHJCeBukus3o15FvFCXzTJeVevpq7Jh-KhHyaUy1gxRIu1bbrKOV7IIHRnSQTZ5kyoqjsFGQgUKJ6VVVhOGjj-ljA7CGtvaMlUGShQ897S0tHASD_WM4EhsCWc5XayurgeSbVOTXObDHxQeLELIcjZgxvY_b19y_YGuIpHUSma3HQXISPu7zjTHfBQd4oYjGYcS9K0SFaeLyTCKVMTpwZtHHNoN-yRDi1bxGSD8Wz0HDlb5UP_xBuhqwkFf1YitZ2M_6w5LiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aea5d5547.mp4?token=EvOf5VYWutjWr-oRS1tNYEVCMEzVuYDNLKvcbAzBzNQSvye-3x3Tqz0oqq6zljmuLJi2gINvquQxNHJCeBukus3o15FvFCXzTJeVevpq7Jh-KhHyaUy1gxRIu1bbrKOV7IIHRnSQTZ5kyoqjsFGQgUKJ6VVVhOGjj-ljA7CGtvaMlUGShQ897S0tHASD_WM4EhsCWc5XayurgeSbVOTXObDHxQeLELIcjZgxvY_b19y_YGuIpHUSma3HQXISPu7zjTHfBQd4oYjGYcS9K0SFaeLyTCKVMTpwZtHHNoN-yRDi1bxGSD8Wz0HDlb5UP_xBuhqwkFf1YitZ2M_6w5LiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456003" target="_blank">📅 06:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دستور ترامپ برای بازگشت ناوهای هواپیمابر به فناوری قدیمی
🔹
ترامپ به نیروی دریایی دستور داده است سامانۀ پیچیده پرتاب جنگنده‌ها را از روی ناوهای هواپیمابر جمع‌آوری کرده و به استفاده از منجنیق‌های بخار بازگردد.
🔹
وال‌استریت‌ژورنال با گزارش این خبر نوشت که مقامات نیروی دریایی آمریکا سال‌ها با این اقدام که احتمالاً میلیاردها دلار هزینه برجای خواهد گذاشت مخالفت کرده بودند.
🔹
به گفته مقامات آمریکایی، ترامپ روز پنجشنبه یادداشت امنیت ملی را امضا کرد که این تغییر را الزامی می‌سازد. طبق این دستور، سامانه پرتاب الکترومغناطیسی که در ناوهای کلاس «جرج راجرز فورد» استفاده می‌شد، جمع‌آوری خواهد شد.
🔹
این دستور، نیروی دریایی را ملزم می‌سازد که ساختار چهارمین ناو از این کلاس به نام «یواس‌اس دوریس میلر»  و تمامی ناوهای بعدی را مجدداً طراحی کند.
🔹
سه ناو اول این کلاس، یعنی ناوهای «فورد»، «جان اف کندی» و «اینترپرایز»، سامانۀ الکترومغناطیسی خود را حفظ خواهند کرد.
🔹
ترامپ ماه گذشته در کنفرانسی در پنسیلوانیا دربارۀ سامانۀ الکترومغناطیسی گفته بود: «آن‌ها اصلاً به درد نمی‌خورند و بسیار پیچیده‌اند.»
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/456002" target="_blank">📅 05:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujlhiKgpFETUJlJcscvIZ-CHBff_WBywuR-riGxmTD_aBrVK_NdhW0bK2UlyAa1kupNfd1o5LNpFzAo3StENZ6Tlz0u7khvCJeVK7ppSnrEL1E1DeOZl3rQwDqnlGwae7WRCBZG0CBDITzvMlk4Pg-bjv61pFztGU-HYnMoHV75FcEzuiTg1xdSRFSTWKTTTUAHTllEQdgCDmFhzawTyWJmnyiDs97-LDbxexHEcxWpYQuMpq8jS3NP1VjtpCfwX7JJsmuwY-zvTQ6AHxDiNTYFVNMQvekJMAyIHaVx7tz7ToW2sqiQY-Zk1g9OEzeMEQGDZz3zf6scSDnN04YbRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: دولت روی واردات پهپاد تعرفۀ گمرکی وضع می‌کند
🔹
رئیس‌جمهور آمریکا اعلام کرد که روی واردات پهپادها و قطعات آن‌ها حتی از مبدأ برخی از متحدان کلیدی ایالات متحده تعرفۀ گمرکی وضع خواهد کرد.
🔹
دولت ترامپ علت این تصمیم را وابستگی «بیش از حد» این کشور به تامین‌کنندگان خارجی پهپاد اعلام کرده است.
🔹
کاخ سفید اعلام کرد طبق فرمانی که به امضای ترامپ رسیده، برای پهپادهایی با اندازۀ خاص یا دارای قابلیت‌های ویژه‌ای که اهمیت بالایی برای امنیت ملی دارند، ۱۰۰ درصد، و برای پهپادهای کوچک‌تر، تعرفۀ ۲۵ درصدی در نظر گرفته شده است.
🔹
همچنین تعرفۀ ۱۵ درصدی روی پهپادها و قطعات وارداتی از اتحادیۀ اروپا، ژاپن، لیختن‌اشتاین، کرۀ جنوبی، سوئیس و تایوان وضع خواهد شد و پهپادهای وارداتی از بریتانیا نیز مشمول ۱۰ درصد تعرفه بر اساس ارزش کالا می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/456001" target="_blank">📅 04:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392c1a051b.mp4?token=ppUJ2Kh13ilbweqSima2kKl8YP1Ui9wrd85VL5Ht_JkiUcsYuCNkizJ9bfyKltxcDwzVry2vKxgjnZmDZETOjF0l_NrDkTFO04R3we6oECxYgoaAemjAtSg4dGB48U4cVCXJ4cxVDKFSLgyNgoqh8xR56hFsJTrBvHQLllGc9sxSLXlX0cmNsy6QYPq7m5nYwTPzDaeegELw4MHNu0ChNtpWgICYdpltKQ_iS3S1cFvQmO4hM9m4KacJRQE5nMWrOsUPFs5pRpA4MLjOJXFTPWMrG2UhVWpcEhO_RQtfXZceag6HKzsT0bGFabLztDY4ZVOL048A9fWtU5TG1b3LUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392c1a051b.mp4?token=ppUJ2Kh13ilbweqSima2kKl8YP1Ui9wrd85VL5Ht_JkiUcsYuCNkizJ9bfyKltxcDwzVry2vKxgjnZmDZETOjF0l_NrDkTFO04R3we6oECxYgoaAemjAtSg4dGB48U4cVCXJ4cxVDKFSLgyNgoqh8xR56hFsJTrBvHQLllGc9sxSLXlX0cmNsy6QYPq7m5nYwTPzDaeegELw4MHNu0ChNtpWgICYdpltKQ_iS3S1cFvQmO4hM9m4KacJRQE5nMWrOsUPFs5pRpA4MLjOJXFTPWMrG2UhVWpcEhO_RQtfXZceag6HKzsT0bGFabLztDY4ZVOL048A9fWtU5TG1b3LUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا کشور امام رضاست
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456000" target="_blank">📅 03:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4UBFwiAjSagL0aKe_itQHYNxLZN6qgcccl6v67eqsSHCih-WcH8MW5STTJM0gd_-6uoNZx9iH-HX9nFHTwt8_VfCRuyXjDUSc9mHSuQEBRa_zvW1Ph9uxQbLe1XboKLRbGIm1yRGfzReX8etBePc6AJ1cxsFurSBwPA0VP8bd5uu_0l6pps20U7XGfPyxKNFZoTPRYGRK_4BKrKADBLIR4UDu4jPsyBAeyhIjTrPsPC3eRZa1Gqlg_0vt63TgpfuLk10mZABMdlKrf_eQxuSVlzppYd9R3uYqouE1N2aeBMBT3cdf_itu2S4mV7Tve5IwMk-aBtRSrZQG38Bqxzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل خبر مرگ خالق چت‌جی‌پی‌تی را منتشر کرد
🔹
گوگل برای مدتی کوتاه و به اشتباه در نتایج جست‌وجوی خود، سم آلتمن، مدیرعامل اپن‌ای‌آی را مرده نشان داد؛ بررسی‌ها نشان داد یک فرد با دستکاری صفحۀ آلتمن در ویکی‌پدیا، اطلاعات جعلی دربارۀ مرگ او وارد کرده و سیستم‌های خودکار گوگل پیش از اصلاح صفحه، این اطلاعات را در نتایج نمایش داده‌اند.
🔹
گوگل و بنیاد ویکی‌مدیا این خطا را تأیید و اطلاعات جعلی را حذف کردند؛ اتفاقی که بار دیگر آسیب‌پذیری نتایج خودکار موتورهای جست‌وجو در برابر خرابکاری و اطلاعات نادرست در منابع عمومی را نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/455999" target="_blank">📅 03:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d869c619.mp4?token=hdB7fq6Fx3CbQ9Ek6-WDcN3G7ltHzpf-IGRyISxzL0uF-HkQoEa0IP4_In6yvsFPgF5RaQYWqx7w-Lx6JuZufl7uq220AdUSdRnjxMghxzlqH6dUEgqUlzHx3DSwZoRmSWfCVujzfu_WQHCtYRFRl2tNzjPXRNEKlIzV175dHFvOWlNXZSoHDP3ir6IKOPsburTDUBVuh4HZOBHoGJWXFN4_KuxBcEHKv7mZlb65LT7UWSQd5L9fqltAGMf-TBiRiJ1mKvmElBBXKqY9dFQn8DMic5YeRTqIgmVwQzGS26v5c4B6iBpvxUESWCHs8F8HMrq17ahCCBW3BvTLUwlh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d869c619.mp4?token=hdB7fq6Fx3CbQ9Ek6-WDcN3G7ltHzpf-IGRyISxzL0uF-HkQoEa0IP4_In6yvsFPgF5RaQYWqx7w-Lx6JuZufl7uq220AdUSdRnjxMghxzlqH6dUEgqUlzHx3DSwZoRmSWfCVujzfu_WQHCtYRFRl2tNzjPXRNEKlIzV175dHFvOWlNXZSoHDP3ir6IKOPsburTDUBVuh4HZOBHoGJWXFN4_KuxBcEHKv7mZlb65LT7UWSQd5L9fqltAGMf-TBiRiJ1mKvmElBBXKqY9dFQn8DMic5YeRTqIgmVwQzGS26v5c4B6iBpvxUESWCHs8F8HMrq17ahCCBW3BvTLUwlh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از حمله به پایگاه‌های تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455997" target="_blank">📅 03:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
منابع عراقی از حمله به پایگاه‌های تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455996" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbJ-IkXOs0CHvDscZQj_FvUe8SVebJ_I8Agcnj1oqOK8DJjMFGcww_nx_xqy73W2MmjUpdkhT3W2UW4_7WZ9eAtfs-wuTTiAXGcbadP0_t4p3rGjmYz7aZWqGyIKKpCqVRs_U8N-LgJxNfh21V-ZNmgAvLpMpLN3Mk0ompnn8Qb5cm083IT9vyZ1W-TNpjUrtKDU637BMaeMo-nP8mVEoyRFObBovLfp9am9eULLg0FNMsEcOPjtAPP0StVsNL1D5Ebssck8_WEnjPmt2AxZO-efitgiziqjl-lR5GJZrBX9ZPmXjXVnJ4BtevSh5KobOcP3Pj8xOS_d75akZ7Cr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F__uW2Guv1zTcSmWggMzkKoE76JYaZs4qdWpgaxGIwoM6I8PKlxGWgfubLZ2LUGYupMHNY5mK0bn3J8GxKewEjMZgZ1QpEjtrcG08UxacM2taqm48V18fiifyuaNJ4UtD6AS6Iits_ogbrUCvPnMgj_tyEb8WLGkK2kvy1eMAVPH5ZlqxxC6VZmKlDakTcZL04DZLF_ksejhVuRlga_hrrbMbcnU20yp1f3FFO2dmpStgJon9GUyKVyboWW7i_fh69B7ykjcYBR5HuPP9VcLc32hFgvv_9RY3G97IyrUr3P4fnNLYSqNG1DfhHj6XgcmvR91rfQfOnYpfMxfqmqBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLs0UU2UbI587pfWVPfLebLejNHwNajqAZ2QzfdOcSoad8JW9vMf9j8q82ezf64fIXMB2NZWYdMlUrcw3wQjQoLznUGVnIWTsaGVW_d-rbFyaWZKaBoNi1LL44JWGvf882mfKBS6Fd-Owj9c82M0YAxaT9dKVXYfFw8VrjA1DAnbd5nls5QYw-E6J4lerYy0mLKvqhrBJ9hh8MqE7ce_O0O8xjOHDGvyqQGmMrwTHhu-jnSyh_lvQQAf3G893PjJfP3x-hCvd3eqcAPVQNB3o6Hf-9s8SIyVUbT25R_QhMMERF23kMeCqZUbOyVgBd5u7RDOLAfzTCzBRXsajkqrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZX7bBP0TE9PPhcYFsPSRVj4s_NAOkXuYu96XWyTiI5bYCtKaznoq1VRyrHL3GA5A3STl3v0i-niQ7g18FuciDEbSldIjGVVxkhcZbbhS3TO5Cm8tAadYhOxSg1DSw1hcW4V3Wbj-jX_rxNP7KU74DLA6lxIUdJhep9a3s2j3kC0mLTfeRgQQEQAkdSJqjIBFAJxJgkSjyO-8JOfmJndIk-7K3xUe5ooI8FrftK8E88SejXXPnJ6fZBY45cfzG3AaCzMphmnSysXQEIOxsadca-d0UX9NdDx8Li5INmydIzG1juUPREqfLkhNAYhpLBT13cwXh7L0WP6vyXMoJnpyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbcJIV9ZWbxI2RqaQufJL72CQmyieUNSQN2fv0pfr9ryTBf1WpGU_NDHo1dMr1bak1A_DCwIwzu1WTqsVsnEZA4OCfzzikQ-SpTu_vmjPlud5Phg-gBBBGqH3aFPPE9j-TGZoRfvn86ydRHDqmH0m69yxsPdZxVIq6-XP4VFKKbbYa24Cqh6dLOoeoS9zAh1Ee6eVAbE2-IdERz5tTijbpsoyP7B9xiJ4lnafAzQOjECz24puUEgDah5tMsOalIj7yJaFuMOR8_ijItmZAQD5yUHMrdoT1KMCEDji3sA30pxAUWOves_lb3ssmfpGHkkWqS58j4ExAbROZpZafJz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7AiPmtN4a3dKUTqL0FUzfmI6BMzQmq6l_hbbLWyPaY08r4og9wb6RZpz8K1dDRX3niMXRCel3toPDDHarIe8XaWMRGBwBRPuj7NaHWN3ht2cdIlXk93R9lfVw3KB2GKrbVo6hgMiGxU2SABdu7L23a5pZBJ9ICthVELDKs5Ecs1Dpp9hSrNOFmSOwtcVlKAcNBUkzqiwtetviw7lb6N6qVeNPPg69bABSiIRVc18u68htyW5Tgy3fMdGTOerhqmIN43vomNtD_0h4asoKk4B598yT_POZ7Jn7ME3CK5Qhnra-XKs1DAwPqpk96SrYAjsZ2B4Q0AAWN6S4X-gNb4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPacDd1vu6Yb_uFEOtbrfyB62n-5Yk9QLwib3Y3vNRHVlABlHL6qHRqN8rCIt08_gALKQNC-R_PMTBe8bgpcCt8f6I0Kp-ERUM6mSMefexepV4eCceY5Iqw65W0ehNkaZaBcd5wZp2Fa6rUWOyF8PI7viM8DYcZF_aUafJzp_s9XwUfbYUjtJnPZPSbCBjkJGQFqx-zb2rmvvSZesH41EmW97AcgoroAWnp7Jc2qOzRRr70FEHeOddiqJutc6dNDPKc49nAW0O_xK0vYfxGZGly2T9f5wR5bWIyvto90IkiWcsp-aaN-lKRcZZZqp-UOpa2OhHzuFg3yzu42o5BqhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین شام غریبان شهادت امام‌رضا(ع) در حرم مطهر رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455989" target="_blank">📅 02:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منابع فلسطینی از حملۀ ارتش رژیم صهیونیستی به نقاطی در شرق غزه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455988" target="_blank">📅 02:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر انرژی آمریکا باز هم فاز کنترل بر تنگۀ هرمز برداشت
🔹
در حالی که روزنامۀ وال‌استریت‌ژورنال با ارائه آمارهای جدید ادعاهای دولت دونالد ترامپ در خصوص کنترل این کشور بر تنگۀ هرمز را به چالش کشید وزیر انرژی او بار دیگر ادعاها در این راستا را تکرار کرد.
🔹
او مدعی شد: «ما با تمام کشتی‌هایی که از تنگۀ هرمز عبور می‌کنند هماهنگ هستیم و تعداد دقیق کشتی‌هایی که روزانه از این تنگۀ عبور می‌کنند را می‌دانیم.»
🔸
ترامپ بارها مدعی شده که کنترل تنگۀ هرمز در دست آمریکا است اما وال‌استریت‌ژورنال روز گذشته گزارش داد از میان ۱۶۶ شناور که در ماه اوت از تنگۀ هرمز عبور کرده‌اند تنها دو مورد عبور از مسیر تحت حمایت آمریکا در امتداد عمان انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455987" target="_blank">📅 02:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">واشنگتن‌پست: یک‌چهارم پهپادهای MQ-9 آمریکا در جنگ با ایران نابود شد
🔹
واشنگتن‌پست به‌نقل از ۳ مقام آمریکایی: ارتش آمریکا در جریان جنگ با ایران دست‌کم ۴۵ فروند پهپاد MQ-9 ریپر از دست داده که می‌شود معادل حدود ۲۵ درصد ناوگان این پهپادها.
🔹
ارزش هر فروند MQ-9،…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455986" target="_blank">📅 02:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برخی گزارش‌ها از حملات رژیم صهیونیستی به مناطقی از جنوب لبنان حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455985" target="_blank">📅 02:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZZi8JzdWYPudMzM70JHnumkxI6AbU-uUTS27Ekv_hkuI5WmOmC0SDeVj_aPTCrxNij-CSe_9CDHuXH3yXGzQSEU_fTgoNYfjuUvqDf95s4aenitDravOXa7xQ4iPsuSQxsT9pbZ0kn4Irf3G0-MxP9Q3LCY9ZM5n__2ckpoElu4AtgMveatgXc7La-GSgqzecHNfFInYBsYY7ThjuW75ertySTxcUuBk4dm12qKCLoT9elHs6szkk3sqIDXTYt0u1mlYVt5a6IRuVlNtlSGbf42gh92l38CyonwCPBDw1eK7H-iGEXtQzPrxikCFvdKR1DGY8e3ISzaLQ4HSsRlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGA2Zs1X3OauTTxe1K0E1hDUl19Ju9P_2jt3yHlpwjLcyPE61AL3VJDTeKUmVM78rlml8mtro3GTACXuCyf9_uTuC75im4DyMD8ralzeiMxsyvRcFJuFWYO_dHlqhgJYupDhOqDAyY4MX3f-J-uzplrQuj5MuWe36z3QxR-3-BCcqxyaJgq4unsnqrSDR5JUiaJcueTj_aYKkjhH7D9scxktUhZn5AqYYC5z2-Y1abrsA_yTQ_l--TA6qVEATj7sY-AxjBjNMCytvnHdp7y16xUl-gS7S-hkcXEbMpsU3_06zXIbjvLt-3nV1hvCNqXioBmRqINGAW4FfXnwqMcupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnzQkAcHWlr8sYKtBvawhxCWAtEtF1NxszUeep08A1TL40Cr1EA852S57udrAreoqYar-YS9vIrZDoHInhY1h8mGtk46UPrdrcmFunhx4LOU7IMFOBa2xwbNQFNDeO0RLA-P9Ly3jDLa5qMmo_GKGktjbxk-S0T-35hs-4jXAK2zew5FTNRJnuhVNP5W5X3VYfAQPAJ_XXrRKGTYfEIOMIrXBeNF6a71NgvojtvziNrK5asQTyyRkfM1yMpRHJ7dg_gHCJxW3ONLXRmdKHnrn2ZHFjp7pjwrPkBBQNBPk5P7oZNtZKZXJ6L-xKZ_2MU-_1sHY5S-Ydp9ueY00rLC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfTRGr46GtfFVxECxumWCcQAwfy5jrLSUUz-Zi_zlWx20ceqg1wbSc7H9Gx1vm8NvkoixLZYbBk3i3WBXHa3R5UWfGTMsaDzVQuj_p8BC5Cgenw4Ol3VLaA6_4GRzUQXMX4xgBmHFRL22YOvsOpUVQ7RIllB57SRD6B9GJdTgnDGa9De7P_1D8ZJ986j8VyPUX3uNJrEcm2OMG4Gru9hDozQV9vbE-7Fo2GVK3HLNDbEcSh0q9iajk8SbgMWn0WDMfsjdMwPfO0ITctAxx2l-GrLwpoMFSkT0lxo_9VWXot8e6XUqyzNmB4MpcqW93HCnZElp3gJyZAS-Fi9mD-JfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1CAR1kHdh6ozjffFAz-qTObvWfBVLCUTjxs1ttsgnDiMeW4Qe1jbifWi1tH-wiZFmzquxio1yyZczp0sxuMasnw49E4XEqpHwnoaWHrgJ1F2E31CfJ-_8fpwoOM8659W5_C5fkUpsCSYY9qBFJiNODuEnGzSTXFs5we4yORLTq2uaUl7CbC7SMGdiF5ygUTFQd0EYjNyk9GZ0GYuNpp4eqan6BNtjjaPY95z1FF21jeS4lee8xRRE80Wg_JDmFbkdkCCgnqHVR83UrPa8Hxus0vuyCEZtL-KofbkFbuw2BrrTCmdNhkck3ZKpIBoTyPYaqE-fTfeXXpthnvx7NhxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزای بوشهری‌ها در شام شهادت امام‌رضا(ع)
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455980" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هدف نخست ترامپ از جنگ با ایران: بازگشت به قبل از جنگ!
🔹
جی‌دی‌ونس، معاون رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز گفته که نخستین هدف کنونی دولت ترامپ، حتی قبل از توافق هسته‌ای با ایران پایین آوردن قیمت نفت و بنزین است.
🔹
چندماه قبل‌تر سخنان مارکو روبیو، وزیر خارجۀ ترامپ هنگامی که گفت هدف نخست جنگ در حال حاضر بازگرداندن تنگۀ هرمز به وضعیت سابق است با موجی از تمسخر و انتقادات تند همراه شد.
🔹
حالا هم انتظار می‌رود این اظهارات ونس با واکنش‌های تند از سوی محافل سیاسی در آمریکا مواجه شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455979" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjmI-fzKT7gdm8EEQrNjFg9pyiO7BVy077Hq8qIFs8SCYohGSjcpOYkoJD70iN14m99sCPIpBuE5rlUtWFeraLzW8vVPk45nFLiPOfD6W1RrGmIwYV5ZaiSVyMceA2gQ0Jh6vFokxNaJIiFAJw3FxqeKDHMwLq5U_SBveMJ1m5r5Km4haZogzMOOWw-OXKHr15p2SVDmbaaXABCads0SmVK9P0SOXNvb7WlmAo5d2CV5wW_K1rzmGUaP-zGicFeP1GeHxPdIvw-4BTj7GhHBTLcsw0RiNrvftsb4XA7Qt7FIFJESn04LViKlo5Z_CTEgC1v9zgaDNKlB283kzDLePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxkSSTlVXfI6PUmRaHLIA0OPZKgMCZieYEBZE0vIjF5nn3g3DEZaJ5bg_FXE3YF0N_8CVbT5Af5fgUmgRFnXHTkKrn1-hDQdFmkK6upPo9vJ_4KEPqum4wDDfsnq4FG8iBw879B0ZvzIdazNs7eINRxy4DKnKr3nFjbjpKE0-5F4h8n6wu1-wZDkNGCES-zQR17ZK_DMEIopRIUGd9QTIgTyvUdzVhHokiW9s1zb1ODXZmY_YBIkQwEDlFPoA8eCzsU1RrCiMxoojR1zUTeGBWGZVCxBE5W1uze-vsOW-VpttNPrGO2dCSPJcFARhvtzIeQpWPo5gcKhHvdn8EhdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIA4xCLQVA9orPYzBE5ctU0NKPEppnEjSalk-4z3FbHFIJa85zxIXq7CFuc19ZjntbG30sBOJ8Ivn7VbKjTYYHJKiEJ9imvVLyiWtI0G9pViiI4Zr_UwKD5jCWJAzRz-B3NTrtMHeo6YVAQZwYYAZWjCED-YM2IShR-alJwW4Qd6f3FCEU2RGJ0tejfdlMFN9LxIT0Q6PJDjHqc4Nwrs3XOiHm4MocBwGcjUfpzc8ZclUHEEWW0EhXEK9OO7-PEZuDcar09fGrsgwTBLg6xZdThELUTib4sSYRPVLJVylKiB_yX6_GYmFM_vMlKInrbLKfX4QRzlSh79QGqaMBF_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNzA0NMcycnr2u35HGPPi8sGbZjsgJ2E2VSmiIewVkiebblW379A1lpVwJNIgZ0pdqmQWF0DuBwK75WEzykVyDVnOSQrRkQzxvzjqlEKUwYr1dRa_K2kgF5lNgkqUx8frI4LUzgBByOADY6up92NKUODOo1tJ5sfpavcsKf4fdawYY6TL8Q4hq5LnauvGdf1M1ii2iY6sOEDwDEw4hQ3MOd6zfHA6pdt1eaWD3-cm9BzAyyobEozxt8Oj8UEe6TL8WAGkZrP3CKimmMkqNPC504n7VOoecyWnpK6Lqo4PMYMInZ8J4Ak_iuiqgPyVm5OrwuGulxlU8cVgGhDyFIXYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d93L_O7rjgcmPL-j-S3SzufM7gLXTnlb98e4hxkae8-YpuaVMRQgHtfF9uTMEvnidnNeGFFhGsGS1tGD48z-jqU0TZw5oZDDb1-DL7p36c2ffMBTHhiSZKW0gjoTPNcfHyK_WPZugVhwIHD1AZfjtbAz6LK3CzIFmTgq3AfsUtt6AUKD4RFWUt6VNavTDk_IBGx6WR6SBzZOdok-GeyJBx92RFcN05FwFWxR8fmuL2OI4QtJK-0r3h7GGtxvpOmddcC82c1uDxJbXIH2s40Je7Me94D9aAeio4u8OF4UPFBIn09Yi16dmlv60hRBZKy39fGdrnAOeqj38FkfHeVSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nczt0mPLFQo3DvqA8M9Mi4HP-sxtR4nVoMjRgbAwp3aumakHYxt6yrxTZWsO1IFA581JkdbwvPCJbZFLSUxZ3ry2Kg2gLFvCkJzzA_8Q5iidxxXwW_xGjGFBc-eKaL9l6PoAN1hESD-3RpcBVddawBY4OvpA66h28ViIEfVMIfVs62yKv76GKyz7dDKurX0KHTXqtU6MWgvDdLFYoMxfd_ZkQZPzIbJn3SDUDU8lELlA3_-3KfFEZ96CqlbheZSIXGx7q8DmW6fxDa28dYG0GOcm7SjKVpHmGns39R-_i6y8Y-xowHplFFJzJJ_eN-j9ETBGun2fWzYwIaHz3FnYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYUodJCHCExDgL2mLeaBBHBtxO5u-IOZRfEVBp-VlXvwXTu7ngTLHOVOqcyEGDQ22yuNtqN9joaQcvJed10Xin-tHQON2zJDzByzSw4MjXNJq-BtAUAc4VvMlM8J_XulQ5pqY94rZP9e1Kk4e96rX_dBPB40t4KaQLc3O7m3MZXDZ71a6h_CqW2pNmNZwnfY-2sunmfzhqFuva1NZLSoKK047tmEz0OPAkMAvbQJLVr_4w4cHBxA7O0SfVI85nkPxHtkrsHE5CW76qMPPiieWjhLu7Wj-BVq_f4fP-YhLbyp1bMQ0kQR_UJykgaAID7Qju8faHh301f-VrrvpXOq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jg_aF2sunNdvwYWuVZ4QWDBsG5H1sdNq5eXDiIlj1_RanZMUJKImsBtlwwcMnpSG1HnyHpgWVyAut8Y4-reOJbKGS4p_pOU3lYHmsJhva_2Alj9-MUX-SkFR3LoQZgqsQ_vIoaU9tp9IfHHlbSmDXj_oK7x_fn84rXLnmZat_pGu09nDrYFfelhyZFGY0TxO2AMN7bLj0YpYWZ28feVCwEQ8bpIqgNTuA784cll0pJ0kw1R9uSpX18mYL_evZ2ksbkdsTvuDBR5Qr-P_21aeC9h4IO9WRIKE-CU_Mbnlp-ISgygdRsL_FhTHV7LKEMZcKwJvtdMiN4lL3iijD0paUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dleJVwthfAAuqLpWBMaWC-cSaUVpSKl2GWOla6twu1wlSr4S9_gc3PBdzKl1FxaiC7LfRjHL_eUwdX_C8NHBbBv09Zwz6y6QO6FYx-LaovRnODaLlgmSfgj4SWsn-iebn75CS4njqW6oD3jbYdSp0yEOJa-KWUqr5-5W1StWVKGInqbXsxe57FBb0EMSRmQ3I_HVxRaCHJlUSzOYd0rPz5m1WW511rlCcKRKqbdUsBlap2WaseYnQhqYUF0Fgb2kCqYMhaTOFFNgUaj5a4LQeX6Cc4X2ktB6rVaN9QORe9Sk2o6V1SXgFm8ihzsi-hzW1XMfw9ldQ_WJk-ONg3wvRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نذر داغ موکب محبان‌الصادق(ع) در سالروز شهادت امام رئوف
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455970" target="_blank">📅 01:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/752176bc48.mp4?token=FsyD90Lz2GB9W2lbyZsnzyMRNuexbywgUY1OmKLywdIYAX6hJNljvWrOD1EIKuwqyj4SfO-ncxwSUcWNOooXIjHkf6MtL4bL8UaP78gza0HNuXxJn0Lao9vfczdSQm0Rjm5SrZqNh8hqywTZL3II2R_pWEQOjmRoF3YA9PMzfd2XEjThMLoxb8fkmcwvlht0aqRjhYiKbDb4IQ3L_ETyznNP2bAv9GjA_ldAkNx9RtAXIORjWRQ6voDkOBIdxY1yWvSDM7LnsWcckf4Dj3cQbPNw8xZ5QUxRtRxsS6NGVdCprR95I2tEeTrKj62mwlJTyRTvu20zELc7J957eJNtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/752176bc48.mp4?token=FsyD90Lz2GB9W2lbyZsnzyMRNuexbywgUY1OmKLywdIYAX6hJNljvWrOD1EIKuwqyj4SfO-ncxwSUcWNOooXIjHkf6MtL4bL8UaP78gza0HNuXxJn0Lao9vfczdSQm0Rjm5SrZqNh8hqywTZL3II2R_pWEQOjmRoF3YA9PMzfd2XEjThMLoxb8fkmcwvlht0aqRjhYiKbDb4IQ3L_ETyznNP2bAv9GjA_ldAkNx9RtAXIORjWRQ6voDkOBIdxY1yWvSDM7LnsWcckf4Dj3cQbPNw8xZ5QUxRtRxsS6NGVdCprR95I2tEeTrKj62mwlJTyRTvu20zELc7J957eJNtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر جدید نقاشی با شن فاطمه عبادی از چهرۀ شهید حاج قاسم سلیمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455969" target="_blank">📅 01:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ81a6v6hq_5xZhUrdMN2_3MgHjaxqCG0OYPxxnxUR3nb9SUT7-SBHCYTByipS6FRMy6ZTH-E5EEh6USijVMWNgaqxa83arEpvJXvxyl68e7CPmXoNrr8rJEOAvwSp06Sm1YyEOi656ao6k8SKsWdtjVB-9_KxRIMtMSZqAcIgq7Qnqn_wpizhpLsWibuhQdsXb-mWr1RXyVOiolnkPSqbpVnc9X0Rbbn3-ULyqd-yAJC_wTLxO7Z7rkE_WPvSlar_Rdp2sbUP2y3wn7PllGWK4NC-z-BYKWnLMD_LObi36bo9ZtNZGstRHLt6UBzE5rhJiJQOBmR10ZNyrU1LWJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۴.۵ ریشتری در حسینیۀ اندیمشک
🔹
ساعت ۰۰:۵۳ بامداد، زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر حوالی حسینیه و اندیمشک در استان خوزستان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455968" target="_blank">📅 01:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مقام لبنانی: با فهرست نهایی کشورها برای راستی‌آزمایی خلع سلاح حزب‌الله موافقت نکرده‌ایم
🔹
یک مقام لبنانی در گفت‌وگو با المانیتور گزارش خبرگزاری رویترز مبنی بر توافق بیروت با اسرائیل درباره فهرست نهایی کشورهایی که می‌توانند برای راستی‌آزمایی خلع سلاح گروه شبه‌نظامی حزب‌الله نیرو به لبنان اعزام کنند را تکذیب کرد و گفت بیروت همچنان در حال پیگیری این موضوع با واشنگتن است.
🔹
طبق توافق ۲۶ ژوئن که با میانجی‌گری آمریکا به دست آمد، خروج مرحله‌ای نیروهای اسرائیلی از جنوب لبنان به «راستی‌آزمایی خلع سلاح» تمامی گروه‌های مسلح غیردولتی توسط دولت لبنان مشروط شده است.
🔹
حزب‌الله که طرف این توافق نیست هر گونه توافق برای خلع سلاح را رد کرده است.
🔹
خبرگزاری رویترز هفته گذشته گزارش داده بود که لبنان و اسرائیل بر سر یک فهرست نهایی به توافق رسیده‌اند.
🔹
این خبرگزاری روز چهارشنبه نیز به نقل از سه منبع آگاه اعلام کرد این فهرست شامل بریتانیا، ایتالیا، سوئیس و اندونزی به عنوان کشورهای مشارکت‌کننده در سازوکار راستی‌آزمایی است.
🔹
با این حال، یک مقام لبنانی روز پنجشنبه تأکید کرد که چنین توافقی وجود ندارد و بیروت همچنان در حال گفتگو با ایالات متحده در این زمینه است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455967" target="_blank">📅 01:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa90ac5dc.mp4?token=Z3GBZ6Zf4Dv2PRxnMmmpeGyePNQPpzAhSygwmJX2XlB_gnb_N9sJ_rIJg1Ju__gkBcECkagiMSGNB6qhzlYNcacGYvVMCCfYf7P5DZIxOYYMKLggYuFY0k3dgpLSE8fDjNlnJBxzunbowokH0pzME3355io6bv9NKfYEBIUXPREmDVkNBSEYuxYVIL7Y9D6Qzted4tfieK-qkoJOpGtCnLHhEeEqCe2SJdwA0dB_POHO8uW2iX3dRxkGSsqtnWSJJ7wYu16TwKcRu6GqMhPgom9nW3TLlk1g8NCLwkMZyCFxbY8HVdZIQRK6D2pHaf5bV_jbD0nI6G0d6Z8TRwhs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa90ac5dc.mp4?token=Z3GBZ6Zf4Dv2PRxnMmmpeGyePNQPpzAhSygwmJX2XlB_gnb_N9sJ_rIJg1Ju__gkBcECkagiMSGNB6qhzlYNcacGYvVMCCfYf7P5DZIxOYYMKLggYuFY0k3dgpLSE8fDjNlnJBxzunbowokH0pzME3355io6bv9NKfYEBIUXPREmDVkNBSEYuxYVIL7Y9D6Qzted4tfieK-qkoJOpGtCnLHhEeEqCe2SJdwA0dB_POHO8uW2iX3dRxkGSsqtnWSJJ7wYu16TwKcRu6GqMhPgom9nW3TLlk1g8NCLwkMZyCFxbY8HVdZIQRK6D2pHaf5bV_jbD0nI6G0d6Z8TRwhs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم رضوی در شام شهادت امام مهربانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455966" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7VKj3xBEImNjJJeRpvK1aV5DRH8697hzhBLoc_RBkz_hz_8q0arFhkoX0YTrIr4224PZyfYRQ-A32ntGKULvmQF1tEnF4sdA4fvuX8MJ72-yoXpEnYKZHK-Y-I-ucWIn5nBg2iTIZCCIealbQmuqt3GkurfHvKeOpVm4s7tYZ-pvHtS3aEhELzca1Hza5F-rCbbOsHGN96Dn308SpoWhbJjp0M8Nc5h7Ir004-lDmLyV_YYNmLxQHNSgVMDum1fv4oCj9PVodmCU4tvOfRS-nLgfEieSHFfpmZWfTz7RrzpBDqZQ16UwgFqJkmGoILaP-J6yQ6FsmANUvwWhE6h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت باکیچ برای همراهی پرسپولیس
🔹
مارکو باکیچ، هافبک تیم فوتبال پرسپولیس که طی یکی دو روز گذشته با آسیب‌دیدگی جزئی مواجه شده بود، مشکلی برای همراهی سرخپوشان در دیدار مقابل شمس‌آذر ندارد.
🔹
پیگیری‌ها نشان می‌دهد باکیچ در تمرینات گروهی پرسپولیس حضور داشته و شرایط مناسبی برای بازی روز شنبه دارد. این بازیکن امروز در آخرین تمرین تیم پیش از مسابقه، تحت بررسی نهایی کادر پزشکی قرار خواهد گرفت اما به احتمال فراوان مشکلی برای همراهی پرسپولیس نخواهد داشت.
🔹
با توجه به شرایط این بازیکن، مهدی تارتار نیز قصد دارد در صورت تأیید نهایی کادر پزشکی، از باکیچ در ترکیب اصلی پرسپولیس مقابل شمس‌آذر استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455965" target="_blank">📅 00:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Mmw6nNct2n7I8M2WzXf0RrstxeXHxoJpf8ypS_9s655uL3XCecuYLCS2cYsa2VkbXwfc8dca_sZuiXGKSBqmg4HhRs1LMa3inLg-fP8944YnksGdqSS-m2ZM02kCUqftLqXGZM1eAxHNGGeiyal8R9zDD6K7_x3F6XSn0UbzHwEyTyiPYm4wtnET_92ccXkbtlVDdiwIHv_O9k7RWnKQ2sIvQWjvVijqDb23_CPt8LbtFzLcJYxuA2CRZibnZRajxutQDCxOdN_7dXTqGKahfxYnIz3KrlvFjefy5VqOmeuAIy8kCILdaja4HE4zpwg5OyJuJmGAJPjCSIV2Inhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت آلودگی نفتی سواحل قشم از زبان رئیس سازمان محیط‌زیست
🔹
آلودگی از ۳ روز پیش وارد سواحل قشم شده و مناطق سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام را درگیر کرده است. هم‌زمان عملیات مهار و پاک‌سازی با استفاده از شناور، تجهیزات تخصصی و بوم‌های حائل درحال…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/455964" target="_blank">📅 00:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455954">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8uzEbTKpt3Ocs5W1Mxa_9U0r0nZ7WuRnBFoVucvYJe9CM9QHz1u-6CsUqPoCrY_1ZCOkgTeZIaDg5zIiGItJ91wGT02MQjPaxf6U1cSimLFagiHG-larZ8Lz3uiZgba4tG8IjmrDy4eBPlUT1pCKYa1Givp8VsbxcIBNEAhI3u79qOZ9JnJ_d90Z644Qiq5Hqr0vZRU8SuwFh12G6TuTt1OSa0zslqUzqJAN3CEtAB7FsNwEWx3IUz49mkjzm8NGXexX4HGY9ZfVeJ0FPiMGdTUlGZ4jOjh5CBjaSvs9urOwPCuP0DTmrnmuxcJggAmsV6RLdm8kyvyg-j-aB09Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEUdZSvG4aJ1G4vr7Og3E4RppM0JmSCZcjkq7R7wy4_lpDv1I3ZOIQk57kmEPvvzgyOtxGSshyN15Fv-vpj--vavooSEja8aosjb-18q1oHwCQQ5_SAfOn7kdyRibNLJwLn12zmF6ScBcw31a9UlgZRfQnEh06WKA8GafYftcOj1aE_sUWFkrpagg7KLG29VMc49Bm7jNvC035jSKGRnDCoYbjrC9nk2JxtxsBUu0r7BoQ976syDdAXnKHRFoO6MpBI6f6-L5GuyaFWSZXLfhu5j66f73NVCvIr9oTrpIrtOb5Hjf3LrL1bJxsk6bbRG68kLttt4beVkWqHODfLzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAS7ZL4dlufIXDH0kL7p3qQvyKp80SCpP5wURiwmEV6mdR91f9MX7fVFSNaUoobaHKcwHywxNB8VjF4l0L1i9K0jGpOuXGIN2G6vQsDXPI0zm4XNFKs0ttPAHc8JTEtBE8A-vPa0hIDM7YEj4__lsY_hZXsMYZAj-DW8MonWMDY76KGBRWizf5H1_epODomhtu5R0cvccpIj1QjXpA7cw6X03rOf2FNZWP-ncxvnbuDjPV08pRFyUMs8PR_tzF_av86IKTM6Heuuk95eI9NR4GFGuRp6YAEjpGS1tVW_czyw6nWH11HloGfKcOrvTSG9t0Uw1Mak468pF0xOuwTFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxwqzmhXYubptpbb9m4-KC6zeQ6SMBQR1xC7coyK-6VEMiDSgyO9QAn1b6-tfDNEf_KTJZOqPXUWxOaVcUWA30sqJT8hEFhEjhU7NgJnunSSIunkapIu9KXMoi1ETcQzqxwv0oxpUYJnlU4C92N21CiabDWtS5sc3LFYETihW1Bn4u2UKSEzreekod3Gz-Kh56Y2HNbqN0I4uKhnPjW6PN7P-yK88YCWaj79LNRxp_vLta-B0hLTLUMMx8aNzmRj_VSg8DtJa_1krwqEl6g2uCnHtTIvCTzvzS8cGdpEZB8uxEBvGR0THR64fDoKSzVX0Gfzaw6KQRwlhg0S5bILVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LREGzsleFs81lVdvT3cNIs5-A6LXY_gypGRYEJ92otZJmzdZCLvdMSh1U7k-3MI4Y6YncQ-2xj_RpniLZX3lmbtGHUJAUR_4pG3fo9JjuuJX2JveTtBGfJlBO0Xy6pWWm6llZXrqKeSc7QP4Wl0QoZouF1gFEJ2KtGauh01ztq8HCcixr_Z36j_e1XDWiSxbo9C4rTipUKXGzKLo2Js9e1EUcU5n7d0sXlCI2pAzwVpJ2uoCngZyyOKZaj-Bxctv8u8rkmMxE9jfzKNoD9I2r5_nq6xMgptmqEwY90z8bQ64ojD0T9h7rFi3GuaEr1ZWr0K4P3GID2JADXhmpeqxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2jGOaiPRlseD2Pcb5QDVrJBsknwve2PPKCE_P8uXAele344f0qqob_RS3DhhBNd4yDYFLaIxQlS2MtSLYzW8DcO80EBO6GQE1DQuRrjms9OyA7wmWrPn4UWGQFPk4oB_it6Pojfy9yTIV6D4Xu8xnqkTV2YgtDOUp1TVIUdeiDRkJamlgaQeC_fP9h8xo3hX5SxmTr5uqwVAElPFrc39H5aX1SKyDkalg0pjkeWUNM8J9IQPoq1d_OKn4c7iIUT5gsDapAMBmnfU3YRqWddbsg5cKGRS8IoPLP8Aa8BW1awo8RC_ehKzvZDnnKFSI3SbRYSv3VkopWihAm3QxAv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZ2UM8w_pJrWET0snezBLbvWZhRwMH2XNt-iqbxmYskZQyz-ndLq5IaTpXxU1s3wvHymoKh_DPepXm1HpOGTlo1ugKCURvwmEyXSmAp4Vz7B_LcoBsamcybFiiYMmErNvFklyQ6Kvo7AbdGUKI8WFdIPoTA2tNEqg7_7DZNwfGZyv9v5G0tqw9HWZ_fij_dVT4XB8x0GEk3p00QLhvk9SlESDoAyrK2JKlyiX3eJBxOpzry33akikdDF3gRQLa_qS1r-qRPpGr7_yxmTp_THBtNPre4RRuOsc9gsKn0yRQBN6fcTIGlyICN7h6YjBXgEXPbv6ydt7AjSWUUiZf2jqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su0wkSC6911q2N_HWf8WWCVzOAqlfOwXagO5viHyORpNckKBrwRx3dgQsZt4suLM6z3vko7cTgVsQfySz12KIQoq7QzVDpO6IDWlIjXCMMMh8ThP7tcbro17nT3Tovga3UiuwJJwTU0NZLSGRoh_Z89zVadjqGv3jLi7PNnd38Aj8rqeBmeZS2dHzwgmpI7VDqXArAqP-ZghYkpEBkdwL-oLp8qYLhhLu-_zf3Ia4pjcowiG0N3Z_rrsBPeJPKnDTWqFWUaEO1jeEwvntwGBZCViHOx_iwHgvL7HSrQ8IpDpdtMXsTCwUWOcK5Y9eXabhxne6UQug0gDvupGDZ-kAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5LyYhsLz4-e0Io0FXGCjRvegE_mqn8TKf1u3iDqlg1y4dYZf4iE4Pks7-wPJrBoLmA-H9N8yCUCQ_qUlfypfyLPnl-DnuzpgTuYBib7qwUtSSup9a7bfVG6TOVr3bRMx7c5dglJIdRjhETGZPbqTAaTecJzDMCzIZqIb0uGLOkdsX6FmiPBkMvxdvMNQ1n650j5lVBmjtvRwSRk6ExFiooVZHbEYdLRJ5kC3BsqBATvFEQJBj5ojH5Pnm6SmbTqMoBcikRjcnERJ2NRhwf3sCB864eC3mUYDKuqG4FHM8M4ijX7hQaWWZ1sexAI-HAkD60WQlqxbPgpEYcvhDXi6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpRfhmChOw4uQEDn3_f_W7RNBs1ikpGZSWwI8kiS54bYrw4bkFgaC9rSITjKdCQcKYrSXlc29tq2MCa8QySMZGdeKpQENhCy_WIk_4yDrkDhGYKJQYJGqFAxnCoLjuaxql42bYLQKPMZ_9z2c0P5MrKUtNbnTpbgeXa4kCY98uTS8mN_B0W4T4YLRuBs7-tf7kjJDQ24ZeqQKb7WCi_9IHzdiWXrqGd6Plo3hXKiVhT3QO5WUZvmUl1WF7E4GuclfEI8OzabZkpwmfv8tlgDIjEdzLZpvZ4vmo_aXefxMzU86LsZwCHpTsWACgLdHZmLdyqBAfUilcfWL39zYQUH6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ردپای شهاب‌ها بر آسمان
بارش شهابی برساوشی یکی از تماشایی‌ترین پدیده‌های آسمانی سال است؛ رویدادی که در شرایط مناسب، ده‌ها شهاب را در هر ساعت به نمایش می‌گذارد.
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455954" target="_blank">📅 00:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455953">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کنگره از ترامپ بابت شرایط بحرانی در ناو لینلکن توضیح خواست
🔹
قانون‌گذاران حزب دموکرات آمریکا از وزارت جنگ این کشور خواسته‌اند دربارۀ شرایط داخل ناو هواپیمابر «یواس‌اس آبراهام لینکلن» توضیح دهد.
🔹
این درخواست پس از انتشار گزارش‌های متعددی مطرح می‌شود که نشان می‌دهد فشار ناشی از ماموریتِ طولانی‌مدت، سلامت روانی حدود ۵۰۰۰ ملوان و تفنگدار دریایی حاضر در این ناو را به‌شدت تحت تأثیر قرار داده و باعث اقدام به خودکشی بعضی از آنها شده است.
🔹
روز سه‌شنبه، روزنامۀ نیو تایمز گزارش داد که حداقل جلوی دو ملوان برای جلوگیری از پرتاب کردن خود به داخل آب گرفته شده است.
🔹
همچنین اعضای خانوادۀ برخی دیگر از نظامیان در گفت‌وگو با این رسانه تأکید کرده‌اند که سربازان روی این ناو دچار افسردگی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455953" target="_blank">📅 00:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455952">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
ادعای امارات دربارۀ حمله به ۲ کشتی در تنگۀ هرمز
🔹
امارات متحده عربی مدعی شده که دو کشتی متعلق به شرکت ملی نفت ابوظبی (ادنوک) که یکی از بزرگ‌ترین تولیدکنندگان انرژی در جهان است، در تنگۀ هرمز مورد حمله قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455952" target="_blank">📅 00:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455951">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طرح سناتورها برای جلوگیری از پنهان‌کاری دولت ترامپ دربارۀ تلفات جنگ با ایران
🔹
گروهی از سناتورهای آمریکایی طرحی را پیشنهاد داده‌اند که هدف آن جلوگیری از پنهان‌کاری دولت ترامپ در زمینۀ هزینه‌های جنگ با ایران است.
🔹
این قانون «ادای احترام به فداکاری‌های نیروهای ما در جنگ» نام گرفته و در شرایطی ارائه شده که گزارش‌های مختلف حاکی است دولت ترامپ تلفات و خسارات واقعی جنگ با ایران را پنهان کرده است.
🔹
دو سناتور ارائه‌کنندۀ این طرح در بیانیه‌ای به مناسبت رونمایی از این طرح گفته‌اند: «قانون ادای احترام به فداکاری‌های نیروهای ما در جنگ وزیر دفاع را از دستکاری در سوابق تلفات و به خطر انداختن مزایای نظامیان و کارکنان بخش عمومی منع می‌کند.»
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455951" target="_blank">📅 00:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455949">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KByeIsohPwF374Ax5LnVa8pTui2JdxZzgf-8iim2qGfN0bzx7Hj16H3WsNSgTYmFpfxL270UbQpaGk_6HzaGletVXBxa0PN7B-Y7YvCPYj7-0BzBhLhwT6GNviAT9xrf_1uvKkl2laU3sva9CzFMcIOAVslsYUHCB9rJ9kqTYepHou-bYTSUndi9Nzu7eEDXuWnuT-UpaXd_ET-3FdOvINSPB3pzaGapvWy-iJcbag-0NeItQQwHj27MMr9kt2_f6Ai3wupOrLx19yWn0i4NBmcHyGdVqR-ADD2SicuK2GwcfuCd8ZqQKMDLA3I2UV8AmAztHV0bdnytYBIy7P22VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌فشانی در تاریکی
🔹
در سال سیزدهم بعثت، سران قریش که از گسترش اسلام در یثرب (مدینه) به تنگ آمده بودند، در «دارالندوه» گرد هم آمدند. طرح آنان، نقشه‌ای شوم و حساب‌شده بود: از هر قبیله جوانی انتخاب شود تا همگی دسته‌جمعی به خانه پیامبر(ص) هجوم ببرند و او را در خواب بکشند. با این کار، خون پیامبر میان تمام قبایل تقسیم می‌شد و خاندان بنی‌هاشم توان جنگ با همه قبایل را نداشتند و مجبور به پذیرش دیه می‌شدند.
🔹
چون وحی بر پیامبر نازل شد و او را از این توطئه آگاه ساخت، فرمان هجرت به یثرب صادر شد. اما خروج پیامبر از خانه، نیازمند پوششی بود تا ردپای خروجش پنهان بماند.
🔹
پیامبر راز را با علی(ع) در میان گذاشت و از او خواست تا آن شب در بسترش بخوابد و روانداز سبزِ او را بر سر بکشد. علی(ع) بی‌تردید و تنها با یک پرسش گفت: «ای رسول خدا، اگر من آنجا بخوابم، جان شما سالم می‌ماند؟» و پس از شنیدن پاسخ مثبت، پیشنهاد را با جان و دل پذیرفت.
🔹
با تاریک شدن هوا، کمین‌کنندگان قریش خانه را محاصره کردند. آنان از روزنه‌ها نگاه می‌کردند و کسی را می‌دیدند که با روانداز سبزِ پیامبر خفته است؛ پس آسوده‌خاطر منتظر سپیده‌دم ماندند تا طبق نقشه حمله کنند.
🔹
در این میان، پیامبر(ص) با استفاده از تاریکی شب و غفلت مهاجمان، از خانه خارج شد و به سمت غار ثور حرکت کرد.
🔹
با طلوع سپیده‌دم، مردان قریش با شمشیرهای کشیده به درون خانه یورش بردند. اما وقتی پارچه از روی صورت کسی‌که خوابیده کنار زده شد، به‌جای پیامبر، با علی(ع) مواجه شدند که آرام و بی‌باک برپاست! نقشه قریش نقش بر آب شد و پیامبر فرصت کافی برای دور شدن از مکه را پیدا کرد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455949" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455948">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f485f9a09f.mp4?token=ItgqkJA9tzzVCScHtOsccA5M8enc-RRV_cx8nt3v5e97CX3PMp37YTYLwWPZHzH1weAJ1NAcsq_EJSyC6huJZxMRhJNLFpYWsReF3BGbMXayqqw85t0hiT1LKX3q7JxFJMLwOpSyvQBvfa1Efdq1N_j5pRJalLJMGU4waMpQX4WSBDzYW8Qa-_LNM42FAI8Yn5wnpQ5Nlon24JOMFEzlWixzGhTXwWzkV98jN_M4t0PUqzOzDXWZjGfVEiLhv-vTrMI01evBAJoOo-d77KEaQqW7YPPrXi29ZbiRd_VMboS-9NUCr4KsutSeqPfjt5GOuPp_0h3FvCjVcPjzuVX3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f485f9a09f.mp4?token=ItgqkJA9tzzVCScHtOsccA5M8enc-RRV_cx8nt3v5e97CX3PMp37YTYLwWPZHzH1weAJ1NAcsq_EJSyC6huJZxMRhJNLFpYWsReF3BGbMXayqqw85t0hiT1LKX3q7JxFJMLwOpSyvQBvfa1Efdq1N_j5pRJalLJMGU4waMpQX4WSBDzYW8Qa-_LNM42FAI8Yn5wnpQ5Nlon24JOMFEzlWixzGhTXwWzkV98jN_M4t0PUqzOzDXWZjGfVEiLhv-vTrMI01evBAJoOo-d77KEaQqW7YPPrXi29ZbiRd_VMboS-9NUCr4KsutSeqPfjt5GOuPp_0h3FvCjVcPjzuVX3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانۀ ۱۶۶ کاشمری‌ها در شام شهادت حضرت رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455948" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455947">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۲۰ درصدِ ناترازی تولید و مصرف بنزین به‌خاطر ترافیک، خودروهای تک‌سرنشین و یک‌سرخالی‌بودن خودروهای باری است.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455947" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455946">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1754162d0.mp4?token=Wky3C3o0qvesTqDbIO8ZM0ZnEkF85wiIfZyr-UkEFq6hhTirWoPURljmmPWhNhO8hXi5ggAYczDZYVesNsaJCWOsJbZa4jI3bhDVdSNsZcMEAbR7tWDhvBvclkljS0DBGyPNpimzwfxxcKL6O0aCjfXl9Je2QuoSLStUxOLx7WKWz3hwp2mncqFn64xD0DsXedq4xCbM1vgliiqUKxk9angVo9CaD_vIyIVj5btG5NMXigMXQ2a7JAVSOR_zcYaTKmwDwWMmZHoNw7mM580L3BCgoLfOyAO_JYNsk0iTMfFM7sCIeyTMZUVhtIvqfLK9hcXSKQnI3nE0QReNKZakm4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1754162d0.mp4?token=Wky3C3o0qvesTqDbIO8ZM0ZnEkF85wiIfZyr-UkEFq6hhTirWoPURljmmPWhNhO8hXi5ggAYczDZYVesNsaJCWOsJbZa4jI3bhDVdSNsZcMEAbR7tWDhvBvclkljS0DBGyPNpimzwfxxcKL6O0aCjfXl9Je2QuoSLStUxOLx7WKWz3hwp2mncqFn64xD0DsXedq4xCbM1vgliiqUKxk9angVo9CaD_vIyIVj5btG5NMXigMXQ2a7JAVSOR_zcYaTKmwDwWMmZHoNw7mM580L3BCgoLfOyAO_JYNsk0iTMfFM7sCIeyTMZUVhtIvqfLK9hcXSKQnI3nE0QReNKZakm4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: دلیل ۵۰ درصد شکاف بین تولید و مصرف بنزین، خودروهای داخلی هستند
🔹
شاید در دولت هیچ‌کس مثل من از این خودروها آسیب نخورده است. این خودروها جز مصرف زیاد بنزین، ده‌ها مشکل دیگر دارند. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455946" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455945">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa53a50025.mp4?token=XGAMIcIZnYwPjcdxMWRWHg26YSet6RtgYh7wTPlhBD0wRRaYVfHfpPSH42O3SyLw1_McfPHiGcgsEscHHCiSUYPNqKFV-qqBfJaKHPRyvrsty-02oetDMcc7-_tR3ursaSoepxz9h39gVeL1BBmnQUWSbMbmLCpMzr4672gu1XqcmOVX2_acIihFdOD2LllKCIeDY0A1gyC9wrx_3Yz1hkzUUiPlBv8JBtxQxyb-y4UPMSL9zDJLzz3xFd_lKIqjo5NCRyvMPmBBpcT9h4zxWHOhSlLMo2V73qtSjWYgB4yyv8IlNi-Dmxj2UxMZ2zmMsFFr2sjqufr3uigWVHGWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa53a50025.mp4?token=XGAMIcIZnYwPjcdxMWRWHg26YSet6RtgYh7wTPlhBD0wRRaYVfHfpPSH42O3SyLw1_McfPHiGcgsEscHHCiSUYPNqKFV-qqBfJaKHPRyvrsty-02oetDMcc7-_tR3ursaSoepxz9h39gVeL1BBmnQUWSbMbmLCpMzr4672gu1XqcmOVX2_acIihFdOD2LllKCIeDY0A1gyC9wrx_3Yz1hkzUUiPlBv8JBtxQxyb-y4UPMSL9zDJLzz3xFd_lKIqjo5NCRyvMPmBBpcT9h4zxWHOhSlLMo2V73qtSjWYgB4yyv8IlNi-Dmxj2UxMZ2zmMsFFr2sjqufr3uigWVHGWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: مصرف بنزین در کشور ما نسبت به دیگر کشورها روزانه ۷۰-۸۰ میلیون لیتر بیشتر است
🔹
مصرف بهینۀ بنزین در ایران باید روزانه ۵۰-۶۰ میلیون لیتر باشد نه ۱۳۵ میلیون لیتر.
🔹
باید کاری کنیم تقاضای مصرف بنزین کنترل شود. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455945" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
