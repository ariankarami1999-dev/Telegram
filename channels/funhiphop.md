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
<img src="https://cdn4.telesco.pe/file/cCXHbVNfqJ9VsxeFPYe-IvD4Qe3VOS4jXvdyWF0HzcR2jgzWTym9HQ06CetLUXse8qQAHM33icDfptHZtAC9B2SbctYcLMzpaK4qPIeN6Z0QOjN2akOSiaxb7ZaCOKu3gJYUq19rtIN8ZB_71QPAo0RAjJCjGwfAIwgkNc1fzDNUfg4TUremzU33yXenLCN-cSmJCmbmJ9kqdQgpjpqdzkknePMvQc5p7DK_2SRboRAiO_wZeGUxl2-R7Y0WC9AOZsmps_xUaLRi9SE6oXRc4bfx3Lf57-kEcBQu4LN05pLyFDSJGWlzHXMZ16by9KwTYMunyRfdzCqKrtHo7a3ADQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 203K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بارسا لاپورتو گرفت</div>
<div class="tg-footer">👁️ 556 · <a href="https://t.me/funhiphop/80954" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/funhiphop/80953" target="_blank">📅 15:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/80952" target="_blank">📅 14:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A37-FfLFaE7O_VAuLFE9oOhyYpL0wU7V39hhJ2MOKauXjX9ZGcEslgFeymgf8v2IuJxrM9IysH5hsqwmqkvrcVNxabQGWVi3r4MsmENi22rfE5sXDjRX5hLaobSVbHlqhbQO2cLARARJi3AqJi-G6suJjCtoPypn22-Z2VuyUcNiV4S6Q2c6HIw1edP-WEVyJocN1pq25fL9JDiq88kfzVw6OwlSgO9fW6NIb41KwPX-__NOQN7y7T3SwjZEgDAVyH6UY9TtX9o3BFVQ_HgooQWyP9aJ4KYT2qRTr-2bK-DGPJAwjlD24_44xBiZunsdJQRveF5rzYSEx5RkbnftpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A37-FfLFaE7O_VAuLFE9oOhyYpL0wU7V39hhJ2MOKauXjX9ZGcEslgFeymgf8v2IuJxrM9IysH5hsqwmqkvrcVNxabQGWVi3r4MsmENi22rfE5sXDjRX5hLaobSVbHlqhbQO2cLARARJi3AqJi-G6suJjCtoPypn22-Z2VuyUcNiV4S6Q2c6HIw1edP-WEVyJocN1pq25fL9JDiq88kfzVw6OwlSgO9fW6NIb41KwPX-__NOQN7y7T3SwjZEgDAVyH6UY9TtX9o3BFVQ_HgooQWyP9aJ4KYT2qRTr-2bK-DGPJAwjlD24_44xBiZunsdJQRveF5rzYSEx5RkbnftpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/80951" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قاطی "همون همیشگی" امشب یه همون همیشگی دیگه هم هست و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/80950" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/80949" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/80948" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxOdsZR-FaOrQ3ryRR6RWtsZFHR_Nb1BuUr-jWZ4mnz-bTOgzFhuHoTOWwTZsGe94-eSiWOL2ikpOWtvC4EYOxca2fFwVc64qRRPSXzrnWV59Hm2_XLFIWrXzPy-ojVuYDg_jH6m_IohqUSv_hfT1catjMTRlZ4L-35FUdKtHtjo8ApgjDmseKOGDno_brB8xyZFrtDUfWaWKuemaavPq6_4ulxEjO1dN21zKkWnrvbhuNeAGq_12Y34gyKYFql99uHIIL1h4GjfADcN_RjjYVxa4Men5s-8ZoA3ljMFRtAGnefrx1FFeebORsZ2KXSDe2QzwMUB_iy5wJbJ9DLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید چه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80947" target="_blank">📅 13:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شات جدید یاس.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/80946" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شات جدید یاس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/80945" target="_blank">📅 12:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGloriø</strong></div>
<div class="tg-text">رنگ پوست رو میخوای چیکار کنی داداش؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80944" target="_blank">📅 11:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVBqEdEn7yjjHNLFcR8tupu7CL6En-bviqkLSm6imLhgZgKuEfnxDo_2se-EB7vJDRB2Fqn13MNTV4bMch63kePdbVQfIHocIojQmsrK_89EL6M4ofarXQUHYD1xZuemhpludRtDLmgPPsjFQsUmovleVJQu9qgjPvMJxbfbAtRlCttDiLqdZUk1uKvL1LB-uHMDcKssSnZRc1VAxF0gFSqd4bLpTCbKCjscOVIEFCDrIt6FicVUwoUZXNmDF1D3uLr-lm3yfGAY1pd9Yo_dUloLDNZ7QSRoBYGN4J01gB9dhBI9FH1cmdjKf2Am32Ooj8AFswJKoijLQbfj2-BCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی، فقط همینو بگم وینیسیوس رفته عمل زیبایی انجام داده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80943" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=XpUxIBvA51aggdEeh4J4AK5UOBlZ0zVuS5_U8BeRtrz3CH74l8SfRO_N7bugTQq7JObBBkIKoxwIQfON6Lr6XfZpdqrsg0-poo1WYrkSdKHr3ny1ZkboUbqcxqL9SCUalXfUEKpQ6C0HNSOi0UC034cGYrFTgJ2ipdAKoVrPsqCSNOAz5WTRqV1F6ebNpoFunhdHGxZcb8PBTFBnOSOyDNgPs8WvX7BiuSjhjIfX9Gz0WmBi9iUicIxtXJlnz-XVU4c0EBrVhlq0YvOD0jy4Qfz136oMIeM_0Vubx4kE-HNQjXyKBjRz0E1UUwgXkupA_U_edp5ASxqeyoHUt7jinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=XpUxIBvA51aggdEeh4J4AK5UOBlZ0zVuS5_U8BeRtrz3CH74l8SfRO_N7bugTQq7JObBBkIKoxwIQfON6Lr6XfZpdqrsg0-poo1WYrkSdKHr3ny1ZkboUbqcxqL9SCUalXfUEKpQ6C0HNSOi0UC034cGYrFTgJ2ipdAKoVrPsqCSNOAz5WTRqV1F6ebNpoFunhdHGxZcb8PBTFBnOSOyDNgPs8WvX7BiuSjhjIfX9Gz0WmBi9iUicIxtXJlnz-XVU4c0EBrVhlq0YvOD0jy4Qfz136oMIeM_0Vubx4kE-HNQjXyKBjRz0E1UUwgXkupA_U_edp5ASxqeyoHUt7jinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی عذر می‌خوام بابت تاخیر ولی سلام صبح زیباتون بخیر. 7
اجرای جدید پروردگار و غول ادبیات فارسی.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80942" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8g3Dk2UwNPNbCA-QXt1OgzETqv3dyare84ZYF5M7ZV_ZiHgHMuBoTSEtW4Qt8DXtkq79MvGQJJEqrqYvRKoS11VvYgFa4jvcNlfdkRf8btYM1QdKyQAfaHCIrVBv8psiWm08xvGT88iC83HBpcDw4wHQkM11J_nWl8dB3DgqAMl0Ur3QFBI7cfkTqW5LS26tApTGeNr_pKwoB2riW8WFkQ_IeiKZzyw7AgexKgVtq729CGUPbAafhn8ybzzeUUo2sdyzsZwj6c1UZ06keZnlB8J25A1ompGaRnaJT28nk7botvCyBQ6DpGFLVPInu9f3bdJVyW5dt8NkGovKt_SEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
29
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80941" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هووففف عجب امتحان عربی زبان قرآن سختی بود.
احساس می‌کنم تازه عمق جمله‌ی عرب هر چه باشد مرا دشمن است رو درک کردم.
@FunHipHop</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80939" target="_blank">📅 10:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80938">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpk5m-3YyzAUBeunkRjJ_IRYTvXa-nc0qJQpQGNl_WBnut5yLjLvwxdq_dJoXRTUwFSgEqYV_pRQc3UB5LnNByEsviObuiFOF3jfZxMT-008ZBwWotkQlOXw9LRFUpfuql93GSDl-Bpgk8BjCTtWZkwQURcHUCZzYTNO8_JcDVAcgt3kQLJHYSTUrB5lxo62-aNxdCTPv-1FEGbm4MUmB7gOu8UlgJcP2O-rOXF3nG5um43eAuXv-FV4I_9sWBie9-TpLdiEZo4GqCMG2LMe2h67r0Ynkv__9GAmw0hrMjTc8Dg6NSjYGU42fCbeThFQgMhuLt_J43x2Q-DyxJ3gRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند سوخت رسان به همراه چندین جنگنده و بمب‌افکن حامل میز و صندلی‌های بسیار بزرگ برای برگزاری مراسم تاجگذاری محمد سامتینگ شاه در حال حرکت به سمت خاورمیانه هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80938" target="_blank">📅 10:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY1CbA5rCvXpxQFbRHILHGebkVubTb0kLPeI9GGZVFbaP6S0FqTPGTEgyaHsPNmYae3x9QmUCzUgcUKV_3GcncuLjoAoAoAIvnvn5xDvRfT2AjtEXQn011XmWnlliuc3Z08Kh7dD7cjOhjUcqZlqPDD_KxpBCu0u2AS2jIxQbIvPg_DyObAbRwnIeUIfOYGfxU4d7y9cRsP1DDgtZhxgAsiyKwLl5C_XqfBE9QzNJ143EXJls31mbys9nNawrcrjeNbApb40MDf111psM9nIBgPxT-IhL2RkHIdXq-NtKCAxe5lS1JwHoIiCB2Y7o_ya7gP45dC5NRtwkU734jyn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی چیکار کردی ایکس هم دیگ سالم نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80937" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apX8w9ZUdNbiEv5ZmlMw7uw29oIlTy3uq7FgXDxU6R6U-D7CwSqa4txix8ngcXBKKqfYKJH7RBzPQjl9vOT8aliIXkoeAEO4wBlo-7s2gZoOy0ueMSnWNzy7VW29e08KdKBS0jCqOVBjIxFzrkeZUYX1o5qBjr9Ax2oiSm3sp1MKGqYW7_vwl9yAMXpyhM_GXogsj_LruxvquSZPDiapfoVaCiVhH7cp2Lz-kWUJhkoPC73ySMB_phYwzAGQQ-BdMKRe5Jbo-Sl2m8Yu6Cl-wDi3otoO2al4JPRx2h9z6lkdMOck3l1U4EaOyFouFKTybWgUe2y5Xw8dkX2hT1Uwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuhXtd1oaGpLWhEiZXIjEtpHzORyBehQZIRcBcqABGh4rux43EWeK5GTxrawcDILpHws34ztBGFNq0Z6pcb7KJt1Te1_6r6OyIYgQHociEWF7qW6V6DoHY4-7RvZKU6IZVn4P-gmzARfOwKqbwPl2292CUXmwH5px28NYM1cbqYmpEsIj26xzzSE3_lPsx9O8h119Xh-8geo-sfpKC2hBCbJ9yVaaJD1gzVeK-Y9XWbF3GL5Nno0iHNQZcAhI38u9t8SgUg3HrMnzyfcG-1eZn-mkjZ-36jhBxzCOCW2efWBDLXcDeLjF-IYtYL0ERYCidVOGVjf9IZjU237guDnNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنده به عنوان ادمین یه رسانه شرقی در برابر رسانه های غربی می ایستم تا حق ملت بزرگ تورک خورده نشه
✊🏿
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80935" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXEObjwFR_PM0ObVsNyp_gJIBJHk14jcg0QNoAYELYPZY1blEDcod3YyT9VD_LXvhec6nIQCOROBGxB4fdoDsGH7ljFJEPTIkFniWcNSahir0EDUy2I3fxX5Tvxm0OKivBXlDuQnXCG2JEVzxOj4GATDy_mMaOJHMYw8jqZpqyvsEOnOAh--BIsyYIdKODtQ06Katm_VLHmGaqWvgQKhgWzY_obWUKf9lSLeiJcCOISUccVprIyzqHCoj5sqrkoy5a5wKOz3RRGK6fEECFa4GJyxCHG8d4TUptPcgunZC7JX27AHkYA_dVPfN1JIGGO7eb4ktPNy8zAruz242QIZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا دید دیگه کار از هشدار به آمریکایی‌های ساکن ایران یا خاورمیانه گذشته، یه هشدار امنیتی جهانی برا تمام آمریکایی تو سراسر جهان به دلیل «افزایش تنش در خاورمیانه» صادر کرد و بهشون گفت مراقب خودتون باشید خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80934" target="_blank">📅 05:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYyzgzsueNRFMaxhWYvTsVhhHIQidJQRKWgrHKgQgLPCH_Lvslo7q62NJX5W3AMoPZ8l9gsXpSYXlwOYSz-NYager9DYr-NoHIb7VMEip9rd6L6YU7FW78j-u2FU5Ud4RC8pkRk5tjl8t1sR_nxWkneonFOxs3JYPnl2v_S9rmy2U7qTrhnbwK2MawwIsEl3DlksDO79J3pq1EE0gMeH72kW2n-HkTapDwY7WNLIkqlLFRTlC6FR1SJvBuVsJ7bQEmDoshjiSabJpPL3biZ2n-DUQbLDp3tTH0_moY23rsnJAMo459S8BkEZrdhK_U7NGGEc7FMa2KmMZO0GyMpn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ترامپ از ایفانتینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80933" target="_blank">📅 03:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چرا قبل مهاجرت کسی نگفت که خارجی ها چیزی به نام تعارف ندارن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80932" target="_blank">📅 02:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تا اینجارو هم نبستن هرچی گیف از ژنرال ساخته شده بفرستید
ما تو این جام 3 تا زدیم و 3 تا خوردیم و من تو کل گل‌ها آروم بودم؛ حالا سرمربی آرژانتین همین کار رو می‌کنه و واسش کلی کلیپ می‌سازن، پس چرا واسه من نمی‌سازید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80931" target="_blank">📅 02:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جنوب
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80929" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">برنامه عادل فوتبال ۳۶۰ بخاطر انتقاد از تنها دو تیم شکست نخورده جام تیم ملی ایران بسته شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80928" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شیراز و اصفهانو زدن
انفجار در شیراز خیلی شدید بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80927" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار فاکس: احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه داره بیشتر می‌شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80926" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یادش بخیر پزشکیان میگفت پایتختو تغییر بدیم و ببریمش تو جنوب به یه استانی که نزدیک به دریا باشه
خواستم بگم سلام دکتر مسعود پزشکیان، برو دست اونی که باعث شد از این تصمیمت منصرف شی رو ببوس وگرنه الان بگا رفتن تمام امورات اداری مملکتم مینداختن گردن این تصمیم تو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80925" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب خیلی بد داره میزنه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80924" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آمریکا بدبخت فکر کرده مثل همیشه با آدمیزاد طرفه
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80923" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سنتکام: همون همیشگی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80922" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قاطی "همون همیشگی" امشب
یه همون همیشگی دیگه هم هست
و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80921" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه سری منابع نسبتا معتبر عربی خبری کار کردن مربوط به اینکه ایران میخواد یا خودش یا به پشتیبانی یکی از گروه های نیابتیش به کویت حمله زمینی بکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80920" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80919" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سنتکام: همون همیشگی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80918" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBWM6j3D8NrvQbC5rWJ7C8VFqAqltm8lKiWRNUMkM4n3q0ozw9M62T0jwcMsuuuGjuK1YQapa6xYXrc7ZYupOgGg9oGDwmFYgmfN-Ngotwu6nZfNUU0qgTuXuHacHIfPZoMQnl5aE9zCksyHoQSbGa9biuSVpXkpMcJxzCZz5f3CHSYBoDKCJfBLwlDxl7PPjN5ZFrVCMXaiR2wkgrLb9R8O29d_GXRid404quRyzVMvFwS2NvFXuT2ztRplfRpvEa_x8JZhUBpsBi3QP7GOez-pnyHPNMHfwvU7dr1mvY_zVjgtB4Cy4zCYBznqvwH5OipIdCyWEaRUKEqA0cRpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور آرات حسینی تو جام جهانی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80917" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSd8JGnj5lZQ4HHfK5eUN13ejgKk1tO37YTq9HB3yzdjCTHo__-HErCm4HMKZkSiD_NAmrDgw2YpC23pF5FkYIKENMr6T8ZbryY0bry0UBEtZHJQhsqcKydVMoC_9_bu8OFviU9Gl1WD4B8xmfme2bPwepmUJ6kUHINv2rrro4VrTbNVqi6_yoiOLDoyDYFPW7vYHKlmrEJXqmsymhsc8QBhs9X9sP7KYf0XCE89ykslpJgQIe3XJexamuy2c4KRIOy5eORRtmdPNX59ssdAfEDZ5TQSY7kPyi7SsZhEnxE0Ai2LN6vLDm5YUzRJuukoXy64rjZYLJPBb8ThvHryiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز بدون نیاز به تهیه اشتراک، فیلم و سریال مورد علاقتو تماشا یا دانلود کن!
🎥
توی ربات نایت موویز هم میتونی جستجو کنی، هم تماشا و هم دانلود، تازه مینی‌اپ هم داره که اگه به فضای سایتی علاقه داری میتونی از اون هم استفاده کنی همشم رایگانه :)
🍿
@NightMoviezBot
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80916" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onv4DWzpEqz5UIYbh3wWqZcN4AYpfoVPHUCmwgO60Qgn8h6fMAdXshlSCYb2kwYFJ4SBv4nFyx-GO0gs-PdxKxfa_uk6kXo0j9dAoZW2-PBqVA_Ye1ylRq9_eeWvgfu8u23LsjrzxEYjUB9yD_J28OMoYWc6RuDD9k4K8KR9_LPaG7KumWC4zBamxnZM1_QMpEx_idICTo33NkgbvBVJr0zdqta9xUkNneWu4_a_fM7wqfPFDr-H_64PIwm4MMHlRTUb0P5PqIh5ZwpoVTBMT9D0eQY_QvGwchhret7iQGcQKOMkIKUJSxp6XGu9v1LvSq8SEiaT01s0tUE0xuAUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که یامال گرفته دستش
شب هفتم سال :
پارادس
🆚️
گاوی
(این به یک رویداد خاص اشاره داره که در اسپانیا برگزار میشه و شامل مبارزات بوکس نمایشیه)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80915" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNslTQdxNFS28vn5o009F7LQeHuRP5caURrJi4N_BtSwgdfibpFnCeydmbazYyt4HALy8PHmxR50v05W8PgTq66pGLPgO1U3Z24RkBl_biV1ySAJUSuaZ52gUm0JKf75stjsCv68NNx6FSJye9AWTlBZ57IpR_wApxVvUcrADw9gw-nPc9BwUpX8kdKq6HKCnMjsjgCtHINx7mBLNETuLvVdPT3SN_rsO15Y7O75pZ_B7GgWNc2Szvc2jfzOjWQfslc3ppg8baMpMXBZUzCdpp87CYxHm4PHqyAQq9Jd5ZBvRpU8jGII8CJaWttVjV-v8_L3cOVuctB7inTdOv74sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پروردگار و برترین اسطوره تاریخ فوتبال:
شکست دردناک بود و زخم‌ها دیر خوب می‌شوند، اما با تمام وجودمان نتیجه را عوض کردیم. حمایت هموطنان و تلاش تیم باعث شد دوباره جزو بهترین‌های جهان باشیم. امروز قدر کارمان را بدانیم؛ این تیم دو بار پشت‌سرهم به فینال جام جهانی رسید. از ته دل از تک‌تک تبریک‌ها و پیام‌ها متشکرم. توانستیم مثل یک کشور متحد باشیم و افتخار آرژانتینی بودن را با هم تقسیم کنیم. همین‌طور به اسپانیا بابت قهرمانی در تورنمنت تبریک می‌گویم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80914" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جام جهانی 2030 با 64 تیم برگزار خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80913" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یچی میگم به اروم ترین حالت ممکن بخندید
یک مقام  در سپاه‌ پاسداران:
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80912" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80910" target="_blank">📅 20:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=kYIaqNJC_k0SfcOxWZyrZAjCjm41dNKiLijV2bZauGZ2oblypf0CyWXXpVuoIjhkCXhF9efpZmp9AAQUi4Ga-596fXRgQw3jEDGRaQEePcBF7rKX9LWu_cmBpoNE1chGS8jjXq4leRauA_-VO59aMlmVNW2g2SjbbN1P-jsUJdVDI_WrEFPXvIHNPInFh-hXORYUf-y9cfPRziloB_Bs3rtobukcgU5LrmW7ofO0DddU9626zkIABAn4eX3chg7l5K_JOC9eHAqz0tMIpTJOY6mgYG29_7BkvPdDFS2jKiyiYFOei1fd8j0oS9_ZdnfoBwtgnbD-qUtZ3QZwDZW13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=kYIaqNJC_k0SfcOxWZyrZAjCjm41dNKiLijV2bZauGZ2oblypf0CyWXXpVuoIjhkCXhF9efpZmp9AAQUi4Ga-596fXRgQw3jEDGRaQEePcBF7rKX9LWu_cmBpoNE1chGS8jjXq4leRauA_-VO59aMlmVNW2g2SjbbN1P-jsUJdVDI_WrEFPXvIHNPInFh-hXORYUf-y9cfPRziloB_Bs3rtobukcgU5LrmW7ofO0DddU9626zkIABAn4eX3chg7l5K_JOC9eHAqz0tMIpTJOY6mgYG29_7BkvPdDFS2jKiyiYFOei1fd8j0oS9_ZdnfoBwtgnbD-qUtZ3QZwDZW13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیوت خر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80909" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بچه ها جی جی آهنگ داد
دیدم سولو موزیک میده باباشم نمیفهمه خواستم دلش نشکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80908" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پائولو مالدینی و گواردیولا در بارسلون باهمدیگه دیدار داشتند
فدراسیون فوتبال ایتالیا میخواد تمام تلاشش رو بکنه تا پپ گواردیولا سرمربی تیم ملی ایتالیا شه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80907" target="_blank">📅 19:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxCovgB0rynwMV7z_XukpFqg8lmtmsYlNVz00SNsRMi8XN4awMXVvMzvfPtSHRQRgq0DO5z9HULl9nC6uJv1XRjl6OlPXbEu1uipAHKMNm2O7jHLbIK6H4lUfoN0qN8p0IKuMo3j98Vd0_91vBgQPAEXXiPWwH6AZPDlggX9Yb5l_oncTwEuLw-QhHrJZ8xkGKYVt40tTlQrv04AsP8RqQENYjozTysrEJT0_1hRM_syuHf_-nQuVt6BOsKRUbdnDgq5T9pBLshAFG59kML8cxjtEIJdYLWoUJSH282KKKbJG7Vkpu13SPY3Y_DGdAmVCbCQ1H8-DoYPmBY-wtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب راموس تو زمین بود یکی از بین راموس و پارادس زنده بیرون نمیرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80906" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m59FwFxWCTRokOosRxLdFcpnxLnC0nBeOg4CwXqVXqniC0RWWp-78QtsI09u8vcr3RYIpQN5FwpoN0R9TC94lJ33GrmkLp96NmFdnEEjokQ2LRy3942vs_SGRCOixZFQ-0uCsD3ml_S_5fSSD08gveHs-sM9PzDSXIJipyMWFqNgErrror0fRgnb5IqpBOSgJQAcOI55inlrgBGzNh8d3HVOKwesRkKG986F5m7tiFJMR_JV46YS_PPPxLAaN3k5ydjCpvR0sw3nANrsnQmU18jWxygcJvUNYxlqGQEk13ndcUaRlnphiKD7JVduZyYP3tT-VC0dzEv3nYa9jMmUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب اسلام هم به خطر افتاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80905" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حقیقتا انتخاب بهترین از تیمی مثل اسپانیا که روی تاکتیک مشخصی بازی میکنه و هر بازیکن وظیفه خودشو داره اشتباه ترین کار ممکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80902" target="_blank">📅 18:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftu-ZTPxDNVWIh93tbK-yb_oEjugBEXAoK9aqlFxfgWVTu6Qini-scAQ6rGfPBFtJ8TAwcGFUibtnwuXZrw4mBa9CqZRkpXHGXJ4E0smm-w8S-zh-FKNNh3hUVG829te44-TIgZOTsxgg35HAa1M0oQ5Klea1SVNNe4-ZGDSjyowb7V66xkcRmc3fAOtIZHD9Hv1ePwod3COUVs6SBcqvZOUfQQZAOZv77nw9cRy75mktdqPncTcezcwhUn1ZA07IjyAZziiVz3S-vvZU3c6YFgx7kL8iSlpsp3PwyEHHUsLUUwFrtBJjKeXPuPQa5IsY-nwVHj2kcAkIb1lHOaGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80901" target="_blank">📅 17:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4kQxkrCfk1F0cz-x5O1Z1hfHKJP49GzsBg_YR6dd_eS4SuK8dIGFEINQD6yxyKSbiOeZo1n6Pka6-7zKRmfUA4p-kqPg60AI5oyw6fH66_TNCPpX2UPUWw7k9HvK_LHjJ249CFJwynRM1_abhiNus3fJKDx1lbEaMbyDXua6Kr6GmwQoHVnjuLwUpUAUi7m-wPVmXdo8G1chvL6d_MaQ_e8-BKS3SXKVXbY26rbKLvWs1Fx5yUlXBzAdIxQcHKbmnBumtL71zhLDV9GpbPpX2kVftNP8Duql0Or7w8pQjsh5OKfhjKflujxLvxwoZVHZaTbls0ETRBQBuAKAr3d_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا: یکی از قربانیان حمله موشکی ایران به پایگاه در اردن، ایزابلا گونزالس ۱۹ ساله، اهل تگزاس بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80900" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvOta2p-KtnkOdieaj9v58p4MT3QGJlMgdTUxDUE14NXApHfJmv1b71s2EVYFHB661Gzq51-BydfJp17zcO3CwU_lazez3mi3mHsxu_5alYBe91VtVlDrBqPreXkcb56HogOXbFjBlLL5iBPxqVidZLN6JQiYEAy334S9XujInFIlsR50TEkBu81_URqI0dfq27xGAcuxAgXQVCC8e_mY2WEScvNctysoEoSA5CHRzHcMgewBj1-YQK5YHFKOGlszVJF9hidIQu8uFvaDNk-4BESY7Qf_lyTHUSMlPZfuRh9pUtUNGxPNTxiRfTOGxb2aAvdSpXcSald37uDREphew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام دلو هم زنده اس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80898" target="_blank">📅 17:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCUVIdnVFpH6G0TvkDpOgkonPrSzgL69a7AMUKzoov_u6whfmgmyrlCTDv_U-QZIWY4QmOWflfbtH-B59yyffP089VlFocsKwXbHl1sFVoqPIMXuHEysX6YVa8mNXipFTr4T-0HQkcMZAkS47wynPRJoJrBtF3gCtNcCh6OiiF2S7De9p9b4hvtHV8-AVxBFu_6KmnGDpUWGsV2rG71TxVEDlACyb0aJOeBGSki4YA4VE4n3kmH3Z-EIO8l_wi4qa8ieuS0EVEjFfz_lGudfMOGJIwalcfRIlJQC94AEXy8F78EsuGlwtM2XA6ansaSHZxamBdx5HXjwqDyXYcBn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های مسی برای رهبر شهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80897" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80896">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp5la4DVE1DmKO27We3-r_ekCGGhFzfxT85tG04ohQ3NC0_YRKndwTMgTujQRybIQE-1U-rD7rYBExTmKbU6xNHo3jHgZHeh7bxIzv8W0tu61CzvC55SEKmmr9ESyefPWtpQrUKiRzUOk0_K-Whrp8lXT2E2NIIm-LoOEpoJfc80zPTl2krStPELq_LCrXbAJ1raem_1T4ovxd_WPuhE2EeSkZAXj7taBA4kxE_JISjgBIQ1cPAG9lTGQYwFEAYFWCWzMp5fFs5PObGUcSdQ-eC4QPSaCDzV0z-tUs8pFI8qhPMSyRBIetHKVGQ1lUFv4OLu-qNmlUdR1O6jxa7oPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه :
نقشه دانش آموزان برای تعویق شکست خورد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80896" target="_blank">📅 16:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uG-AQsWatvJkNWqU13zSjuA_cyGI-I_SRjfny9rK_A_B8e0Oh-gcKOSC60RWUse6YFU3xON4fQG0qfOjnaJ1sra5V2KzqYQJ2Biu0euS74B87Ssq9OmMIc2hytHm-kEiqjQk3QV_6Ox5OJMTUS9rcx7HQYNAsCJWtOdRkU-f2Kz5a-1fEyKPI9CkLMsyN5uiUnFyBHKvmQRZ-C1BIOsN8j0Kc5MZmEPBaVVlE2uNyNA2EDwwdtwYfDtkgQ2TIcxNdDDnu33nDV9l_fpWr2izoJa50DnlKABnCHkADRvt5N65DBoWk3N0Jmcazx-8Dfwnu2iWVbDkZ3M0B9YWr462Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvF57laADHufPKK06Wj8Wf9AiLlKirUueyYxiq9YlAMbK13q7szbNEROLYZLZFX-pJxbs5n6iX_IIs01Nxy-S1oNEfqHG8Q674kRlUOKPADIZ03dczq7dPqGu7YQJrAn0_gvGbdRqN_sNnVQTp14VbqJk0YiTYnq40CG3ktUCNVaigRkpuJXq12POc77LkjuxWbOjaJsWgjtzHNvbGrgfwJFxEmcdwIpMebXTQ_ogCirfRhzyQ0YgY1gOfz2AAZN2RQP_e5G1AWuWjsx3hVGGJo6ZLea7mFlKQYIqIB3nmnJqCio640tw47veIXBB3lrUSAv_jFm3X8MaZY5E2jIRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دکی و صدف در حال عشق و حال با پولای ویناک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80894" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHF5OCAkRI57OeEJVEZsKO8D1P4McUBswNWcAG_GFjNlLyQIgJWKABUKj_1uxgRZypt9xZLSZYGR7mlxlQhtD9390wd1onW33HrBInkCuiUsLvEsTJiMcnQE3JR_h33vAr_14TRMn10pw5ybObJy7NILVh-NyDxnzxQMrm4wic-ga7eeWEGvfD1lkIyx5PyVuxO-iYlLvqoobW4KVFCWcaACTAYi0gyto1TtIMblEOrHQGRpI46Cx_qrCQrQgx9fIBuHm2UFmbWZaaTCruoIWiCpbQ_E_AG1qx248Doys7fvHVxh-8AVIWy9oy9to_tMu-l59CByGKOLvdiIdAnGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80893" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یکی رو گوشی این رپرا کیبورد فارسی نصب کنه تا گوشیو نکردم تو کونشون نچسبارو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80892" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80891" target="_blank">📅 15:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAKpIQ5163LdBfZuq4G1pMAGmtzyPbRx3_io1tGlFv6WkVwddLdZj5Lw2EgttrZFvNLHufo5j7tbiP0aRwZnbI-O6SBYAM4rMTuTHiLd3ZnkaYFpEb1TOlxgu1AUV_Unq_NLTp_7zt-aBMBYBdp7vnU971EsTmDg1S7mu7o2uvQmK8rGNKCvSNAp60TD-4UtcE95AAaxiIh50tVnLIUjTRnep86kcVvU0_YD_KrZdVttZ0Vd5ic2lhzqvOz-29Aj6ntBBSk5ozpNisAahmBRVVuecNedTQX9uc5JVMDvoHLXQQ2z90eCzY69VMmoESDqYbsEUKvCDMEWQSHawrOnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80890" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmlxkILeibYUuUYoKUh2Yb9bEX0pFjDa08sNCI1Ud50Tm-Wp8ZukibeIx-rPPgkpyY6AitQtYWlby16oyg6_WNodM9sMVtTXnP75jQvcPJLqfdoOe53zbmKny6c20yfbAAgskrbSKyn-hxMhZqUinUHAgE6wkoiPb55bnfGpbZGBgaesQLfKIZEgjp4GpWqdU970R1lOxAZ-P49fUISQt3kjOMBxOPNMb68ja7ja_1o-zBEVwC0L07WVOnZK55nQVwyFcZtjHfPvQtrFzy8GXkqCXeIutO_m-Lgz2hHGUYtJxuVr75XCV7GeyatyOZSdn4WtpuMcjGeWkR3aqUSUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80889" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bguuKmhpGAAhAHEoQWcyxeTKUYl7XAw7ZPeE99g_ujE8cDlfv3SMBT7-ijuWeluS2B18yKqdu748aWWyidsL2wGmnebBU5ki5Fvz-I7bompegxT9zbOKeCEHRsTK2Mma5AoX5SLR9hyqQUoYbD8yRbomVapAsMKAB4IUcaXENG1UUD7GvQf_IyzwWl0hH5RcDz2wZVIgScylZOUHNpSIb0CyEH8_w2YQ1tI93pmIRNmaZY8aheCB2vRM32cFI1buScJyN7rmOKE1SFD0sekOnqtOiHMdnrTtHFWEaZxCAhq3NZuqkodBpCwN4KXyjDCOEjK3eedJa2ZEVnXy_GMmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین همینجا بازیو باخت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80888" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد پس</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80887" target="_blank">📅 14:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اصلا وایب خوبی نداشت امسال</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80885" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آقا من هنوز سیر نشدم، از اول برگذار کنید جام جهانی رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80884" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbtVjn4kb22NUmRrtm01BLPbR9-boytJZdBLFRJxkB8Y8jc0EIzLmTtjfR7sbBYOgfo0MvTFgqhI7KM6fGyHI2hwaRrjV6hPuDZrfyjorYvJ00LJYps-YaSJlu79rPyaebkyJCi2bBuVzD3LYsQAxp5nrZRBzxK2cftHAkXPrPmqh89uUL-xxoeixkKpDN1UjCcGgtSpUXf88ZiZm2MBTagq0FdOkhaaV1QsCITRI5yevRWAu2m1A_d6SOu-I8ZGG_12MNuxcL-q_qULOnK2hinIpHui7jD96M91rXEXQPkuE_QnNd4yK9m4pXjSvABaPzqiCPTSweoG12k16_WlEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فواید رابطه با اسب.
#بخوانیم_و_بدانیم
#اطلاعات_عمومی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80883" target="_blank">📅 14:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عه ۲۰۰ کا شدیم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80880" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmYtFOpF1WvwwplNdeZj1HXu1BoAlGkdUewBLnteH9Tt95a7La7MVjzmfJRuhvIdft7u_7qZ9nHYL3J_BSv4eTcL_U1Mtv5FJtvyOnrIonLpuTHJrZGb_EssQYXn2nvuKq-b0-2QMyuEcEMRjUM20RMXk-b-8gnBk7UDQPsbum8CFzXaxlp_kfO0VFkGC5U4UFxMBR8wEvrQvTEXCsNSHguZ2gl34LT5snFnLaBXQpWLqOqH8Kd0HMYcMg8LYm28BdLOrJabeLYHRvuw0sbNqbfPpg36CNj5HP1lajx6rlyX8jss7QVMZ8I1BG-WOeIHvlNa6iaQsdVkoZgmiBBB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال باحال ترین اتفاق این جام جهانی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80879" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل هیوم: نتانیاهو امروز بعد از ظهر جلسه‌ای اضطراری با هیئت وزیران امنیتی خود درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80878" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5k9lg1gq5HYhAX_lMzdKD8kJYDx_Hgs7gK1gMpki4LxYEYXhlwUKHAgS7ur2Py7wl1bJWJfeh3TaPMFVQCU8-M-J_yIPi2SqK14Hs664CttFVI2y73qWRecqocoQmRwJt4M4V6uWawzWCvWh4gL2xERjRATY1E6CDtGsf0UPcQHPtvqY5Zjq3jJooDGE6yz5b2sYbz8fUteUTcflDnvIGXxs8WmR-Z4r2HmqqbMI5ZXGFZDXpTL0yHDXCYzKpUFx-ASK3kl58jN-Xf5KRwGHTSjmGG-lqv-adoRHuInIJgwpqhKsN5ZN2gDdEnKyiqawvZNEhr8ApTT-Crd7gnmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPAJdnxm7sGkiBrBRZFVN2Du_8bndKjTG1Ucyoq5RqmxCSPqMyX8h-LOOwGY_kdaExtv1lb00fjm9Ge1FttITGTDpUwdQpmQldkTNshJtHUsbo-x3JuS98i4HwBIPjrQX6y03GdqEIM1QlKszwNqGthHbf3HhDUutgQ6JdOhQIOou0Z936h5QpHRcq03_s4EIPqF81tZsxPeYaUe6JpskbeXygGELMtA57uD4YsG2nsYfvUHUmzx8PPaN8k4zK6J7xnrwi8sBZGF91GVJZeXyBLuqGTd_n50IUOHxwUEqLsZ8dV_3Xpd2LtAU8BVITJJ1wFAUuc2nf9QjT6RESKxbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا اجازه؟ امروز میخواستید امتحان بگیرید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80876" target="_blank">📅 13:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkRcvYoUAbrZCiDMICfvvdzNO7o1sfbgu-uRLcRMu6tc_FZzOrTP4wDvoYM0LXuNjbxod0OBaIAgIwGd5jyrwvkWzYQlXYJfIOcFEZWR22TdXglMwyhknexafqsP57-_8qwAQOszjrYr1Mhs0h-lAREPo3gyQKZW0PgK6fEZ-tspBXUeAVJ-31xEplUOnv93psSgyxeqxURitDTzZefhrMlUIlu694xGSfHkpln4aSj9p8CwZIZ4gLgPIxwONxf4ThJdRj7sF4HPpnhj8-xhtl6P0d0a6K4_21tV2kugQxB8F1pHo1VG7kI9wNOnx9FFbiqMaCk9JMkVCGNkgJakOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟ این دستشو گذاشت جلو دهنش به ما فحش داد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80875" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIBn3VE4YcPc-3lEPSPbXqHb281-ckJYyuvx9_6O6cfX8XRzETTEyD-53g70o4hufD__9gV1afBRE0PeHJ2QIQHMdAsbdRu9pd4NMcS-iH28CZ0WHWpe_C4jE4k1fZPnqWNXzGF4Gk1tdEil-8U8kJWq-3FLS4IOHMZFXQYl5NcSau1_p_ysgPhTEEz3C3vfCVDgajRnVmErFIi60Z6RzxkNCOaLE18w8gsmb4iJDTC6bYkqQvJuOCFixqQFNiiEdenivm8eyXYKsR-JOiIJZtRPgN6yq3jYDq2DXYyLSJsgEFXdHYF1sArt8s5nZWTm2M5f0Y2aS5ZKjZOa0L6b-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم های یامال احساس تنفر به ترامپ کودک کش را فریاد میزنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80874" target="_blank">📅 12:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzHR7Zva2TucIr5NBf_0z7OioG4ppAUzAv2WR15LY0fb-3ks0QnIPtYqaW9FQykfQ7uAQNWDS0CRyM5pkKnFpQuBaWFODm5VjpWC-Sb3qcJFSogSalC_OJBmLoWUKFLl_a0asQQsswtG0vgUhsZZb2h1hNtczKSvoznfStMKW3YH0I2iU2HIUwzVmN-m215x0b0G1Kme7GtEi-rKol_epn7c9rHEwzc2qW4ALhwrfjGTykdQ9dEetk7dZRlUEnTZoVG6v5tRI66sNdx27VkVCW_7fk8693tXvv5SWwxix0gqOg22jqaS3wBNBJb-4JD3paVaC_y4jjxPEApg5eS5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به اسپانیا بابت قهرمانی و افتخار آفرینی برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80873" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدا هایی که شرق تهران میشنوید مربوط به خنثی سازی بمبه خوشحال نشید، امتحاناتون کنسل نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80872" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbDG9_1atAK1g6VJM_LXoyyIaqmWR9uhoK4ZRTUaOtb8QioBvooko8vgp8tzox3AfyclpQQm7UbxavJUOZDeE4V8uO9bDoeZbgu2HNR6tpAX-1AEedSBr8F0YjDfrzniwEkAitROpTSUsVscTfFh7fiNc3fJTkT0uFCrfiGlZoRn8V2SJ39BVFD2kUR74YSajIRm4Ap6k_AuG46hxWwoLNvtXvPykTIlltzuVoi6ghv8DFQGaebfekRz5i-hCNEPkPuPAEaffEKnZgQHfI4jHQo5iLgRUK-lRrnGEAyI5n-Yk78qMAR4RjIWiXRUZTWn2nopfwpxgOVq8xwIEqaTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80871" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKto-a-eO4lu1tXCpA3GsAb2zQUDMMywGOkU_fHrc0BZY72Izkkxa5nAQiI6BSvFphdg33KQ7jFZJ5wj3Mn2m4MHPl6g_XemVCuBcRWFRbitSTDQQGq3WCtgoL9LKVtHszHmq9Mqv0SgbV1SyobsoaApa9AkyPU0HD0EE08WxvndvhERBXq9SiFyzO0FYuzPNnKmdUxu1bUpq4Gix0oGZ663zPL3DFrVz0gFglR9bWxvqff1x2HTFiGIn7gRayGkpPx6b4o9mJx-xC8lwk63cB-vlgbxIfVRPluTb6DixJAo6iHpYbxaz8oGcTpIgR1Kp2ii_XMK_QenusVIQuR7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی این توپ طلا حق مسی یا امباپه بود کصکشا
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80870" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/low8Rnt4nwGUQrsLYEezjkPygybE8OZ5eJfy82qj8AueFTTbhJrH4YQ8jev0B2hYUxA6ECEHkkGEwUvIdB0eMYfZxyEcQzyjLXD9mi6pbemmU7b2tTWCvbutG6ZezM-r8EIztyHFgCnvIHRLG84KRdbKasDWVJ96Fy5yBzlxP-qekUyBXQh3jAHckyNm56Gzx0RoaUGOWYW1HK4kJDIfqyZ3lDExJvWQARSPcXMZV3VopC-MzVSDHON9g3nXzRdnjmmQYysekD22IvS_N9nElQkuRrnGEloELpjVI-6k0LnvOWVyyYWc0pRJkz64rVtKpSxjR24N5PEPNnaKuQXs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80868" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc2sEuoApW1M-11Vh8Z6ep5cs0gMEbWEYMvXXXd52eEsUH_qvvr6D5C9C4QVfIEacg4ni1uDexUYG0T_4wf1gswrMSVx-l8gEnjESKKA2fgIKZ1prEbaQ4OUMmjxeBqHMhOc8UeRniUHmVC4pHBYQplrNgzE795K4xlll6Vy5-_A1ZQFkXhCtDYQkD8KyhMp9BdC2jlv9tMv2g4G2fuNnpsfJIouAy9FbhwIf2e2EpymP3lfm9uqJcveKiAgM6JTZrkomylgoTj3g6eNW9PN7DReoLtnZQhHdNRLpZF3YP1hj8c64anH1rMMr8Lm430J0I0Hov9M6P2cHOStujxdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس شوهرعمم بعد از ریدن به عکس های خونوادگی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80867" target="_blank">📅 10:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_7z1FoujGbvQI5x3C_YXY_1FMvd1tt8zHmZbTKkmdSxoRaZIrOER4xbflqYMZHYzmIQh93pmcC8hPI0bhWlcYEUfkujIuSKd1IgC9vFieDakMqkrGxPW6bC2aQtnjHjFeKYTt6YZxyCNbmfqlaReGOXK8cxxfTB67NJgfByyq-8gORZR3cmn6_HGs8xQEhET_S27sMRqqmJqnJVxfvi0ylstPYg_KlaJiknLS19pgDyvj_4ZpuMy3VdAx_4o7vc4kfCOVjRumFsv3gwJ4NuefHz0QdSmaAqVTRxy3FpmQ_MRboV9lZ8TtHI-7aPDrnXyXOqVnpPk6mPMHsOIc70FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۷ و ۱۸ دقیقه صبح تو کرمانشاه یه زلزله ۵.۷ ریشتری اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80866" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExiYB7r5c8riopn0icE0mS_FvQa6MT0eVw_51BA1HiOhQ53GSz8fk4dqw8y4x1jxKSj2vSNcDk5JE1G0YZmyu5ASxlrBMq6s2E2774XHANpv8dPEV9s6WB2jNkhcI9yuFzvqkzt_DBmShi77mwb3b5j16YLMg3uuvLs1t7U3XDIx_skSZXTe-FAIYThC_Ken16AcLTgW3CsJvluU-vnTg5EWUAeR12bkArJzM_H-70Rre3-L5r4-YvMkBhRGrTE2ugd6Z1k-KcS0lZnxLYkeqjwb9NMBfExUYsY_7lDb2V7eK7I2z4MolQQtZ6mZ_xNmmHhgGDnKlZHXkZymdmW-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکی Dior از استایل ایرانیای دهه شصت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80865" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmGCP0YJovUge11xO6w18NYorYTfTZVKndaS8W7l2Byf0ZAezvEGOmtLlWCxD_iENuyvlS29n26qmVuMdKPWiFm47pPuANBVZpizi7v_rp8rroZL5Jdc0zzC1DKuf68StEfmN2ATif4mHxVdTKEcVEsFFwIjP2U5IE3aTXWFniTkqk-e0PjV1DrCPLFeRjwz46KmTbNaI7-Nqa7NFZpeU84OUcjvn1mVEJ3qjFp-6bu-M5P_xYaBX3CC9IqnN35Yb-e0A6YXTlTHWx-GWSI3_SbQhqkXsuvFOIK7MmoCsLQuP5ll8a5WTDr7yCzAz8p-G9EMUTY3eSeKN_fMfa4tOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام بار این سفر جذاب و فراموش نشدنی روی دوش تو بود
خسته نباشی مرد
🩵
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80861" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حالا که جام تموم شد، رونالدو جان تو کارتو کرده بودی، اون "i'm back" گفتنت برا چی بود آخه مرد مومن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80859" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ آخر نزاشت تیم ملی اسپانیا یه عکس ملی بگیره تو همه عکسا هست کصکش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80858" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ti9jQfp_vLLQJWYl3Wqi6yQMOd8RwgZrXJ6eN4h7PP6H7EekzolAoFlTB9xOG0lQGGTXG55LpxBw7aPQElg8PDWjqwE_PdYbUDUXXKd47ymGd5sFaS1wvZdLxml3ZmxCAKM2SXWBF0jGpHLQKUa6kwXs6IFshfAhvLj9_m1eIqvnJRBaRYOQ-zZvWYAH0jiLVoa3eldV-sEsVx4nBpsB4cwwiiL_hpXa2TaW8J_ldboHyj6U2T6o-WMaiCECLWti07koodFTv3TaG2FY6TrP3tcUsx54AzCpV5X4a9x8qdx5qKZcLyvJR-D9DuaPvUoRVt7NRg43xbnLrXCIc9h1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر خوشگل و کون بچه بودنت به ایران 2 هفته دیگه مهلت میدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80857" target="_blank">📅 02:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علی دایی اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80856" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب دیگه جام جهانی تموم شد ترامپ زنجنده حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80855" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بارسا بلد نیست سی ال بزنه چطوری جام جهانیو برد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80854" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپو یکی‌ بکشه کنار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80853" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_-OLuG5y5LYuTSPzpmT-AZ5ernpQwu9A0Ace29YOJZSvURI5UyglkELNFeseY4utz1nTBfW583T2Uxgxw6hpsE2RU6lNxJeiIXncKAOzeAHxv5d6q75eCLZ_YWDSK-zsAj6hBn7RMQ6nbt5gLaik2KQmAR5IAzbX4a81GE916J7MFRaNWY9-banckPg1Z-jGoq3NR6OPJelZKXcZPxAt2yOPsMWCrHeDvC2OQpTBo1wuztezggDWemGVv7ew_lIqRTU12zcKqMGe3mQgiZfrt37YLdHkKC3BlbZsiKLna566Osbpb_MmeCkG-GVZpUdVUoq2ke1CYFtbuE7fK93wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80852" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رودری هم به عنوان بهترین بازیکن جام انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80851" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اونای سیمون هم بهترین گلر جام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80850" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کوبارسی به عنوان بهترین بازیکن جوان تورنمت انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80849" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNr6vnGaRCsf0BhTvFLpe6lYRInkWSDhV7MsrMpnmXk9zxm78GzdB9dUTnuzK2eX4Skc22RsTtFG2G-zfreN1UUMzOreRzuvVR1DD9OMaVTzMvXkmmDH_Gg2ccXKzSO8DMb4Agtq9B2D0Ui5eCLQz5VW4gHvpJHj1VUi8ubnKKjS9ZVMIEVtvEBgnsUOTb20JIxPnnKPiTFQXXQQicrIGm0hw0wXwWYQXvpLhDtMK3gkV8FGAoWN775qZc_XGfRVpiZxdWZY4UFK2ZOZpBpOHgbeTu4oyFVfSBetxp7Jahng8XxyuhdRPXcl53Z3ncvLrxxq-pKOmzCaZGqgefc2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخاری دیگر برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80848" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY1EaXveQC18k_NnmV1Tpr1aT6iZyiyTKLk4Pg2RnY4w-uAcjApp0q9vnjLU3RFjlWABXcZnH_tDrUBHt-_dJlm47jJToONDuXlhroSd3vRt89h-S73lhM_F1jcnVg3kT5ZJb1_pA2wplPKYpah-M2IjSNDTaMuIWot7d1nqp1VVOIKXDN7bZJWzH9RXv6DD2FiyAgt0SEEBimC94MvXETkZn8xdei1JZ5ku8xRs-ueVzY-K6WET4HTKJnhTQJ36jtv6eVoFUBc3fC5y25wkOtgc820I-wjc7H8J8SK0TqTIHcTdy5gi8AxVuTxztiqSJBWstGfxNrh12Alo1yN-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80847" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80846" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpaD_n0ZFDiZlsGTKNFsbMNkCUe7pnwpNWsg5-xYRKLq6kKILYKhjx7_hUi2xzxISPF1jKNIS9nYiv0wKmMTH5rRc2HbtNgry0ilcxzbzaIxiyEngMdtD2PzkR2VRVqoSlZK5i34Pxa5VLaFUmgSqPVcFqOKYh95n9hBapC2ODHTSYibRWp-8WvZodcs1LgmsaL_YEIJ3VJBWc4_pfjaDXYT5izysgpcHFXox0AuUYS8UJU8dpNfZ-0PPx9oarvjJIP2mLEwzbhWfa8ZH_cb5qlJ2DkcU81EfPqI5ePN-AONKHk-Y9pdw6EdIcpvJ07NTUvx1TyasX03q-FyvkrDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIMgY0y8G5DEm9y9Ik7orkmSoZf8HhfCvv3QjLW7Vy8CExFckjpO58rvsuL35E2nnGSWv4nrX7MnEDrClQL3zqs5HDW617JUJUtkvrk5_COxhJkraINk5qtuY0SFGAcAfcNrtJYzrT5R-PaW85rpFKw-Wp7CqKSTCj1zROaSdhhZDIVXnxDKX8t_RgqrAYkGoQcg3addp_Ys1xU8Hh2QYTvi8dWpGXavOgFtM7Vj_pESRXo0qxQvb-_CiiKK2DcqcDdi5-fGYQTcRgc3IAvRPMDrp694S6vIIjoG_xKNaSDT-xb5RiZ-CZJtfDn39zNHb1XR_4lmSfA85DkhJ6qZjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پارادس چیکار گاوی بنده خدا داشت
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80843" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب بارسا فنا حالا وقتشه خیلی سوسکی پرچم آرژانتینو بردارید بجاش اسپانیا بزارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80842" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپانیا آورده میگه ببر، صد بار گفتم فقط مصر و کیپ ورد و سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80841" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voTrvd6ogq4yqvMLhJbh4Hft008Rq-oQNJNSBjCrj1iR_AQRB763_y-DYwZnSnIhKOHit516jdKLRRNwIfE5DVTC03sz-0be0pFeHw78wzm5_f8t4w_QVPoilM9H6MpUq8EjFM-F8T4SjCw-mLqCc3KuB6u4KrIUVHyWMqSSEI8iym-4JXjVbtYhLGIgL3ygh9gqhA_t8HOY8SA-Xt3BlI4LYyKxBQEcuLnw5sgMopzndu1SRw9zImiXjlK5sbVxsph4WZEgjFg8B2l3T9jfmKl-BudTawIIUO6O9jir4GVRNpantLiQpjlxlJ7vKnLnFYLq5-53wkokolVSHbAJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟
این دستشو گذاشت جلو دهنش به ما فحش داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80840" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دریک جان کیرم تو ناموست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80839" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">لامین یه جام جهانی
مسی یه جام جهانی
رونالدو : I'm back
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80838" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9xkWShfiWJtyr2R68krOddKg96L458dYMjNBrwce6rv3A-5jU99aQa3l5wtLNUF69rLNPVbXu-hbn7FbgnwpMcm4cEOQv3-vvg_acbUlF7-Jxy8zc8a39kRyov3j7FLK-YE9IL9vWtMEVGHWfOCfhdBpCpM8_P-PEKqYFp4oMEYODNX5rdaNU7Q25ZkrvsF7ZPzh2VszEUHCpeh04vpBlTPYxFvhvEiDjDnckFvlbHpzgo__itECOP5kexNqtRkwurde7Z5oAY0uFN-PBlKvGN04ANkpx7l8HQaYImVw8ALEsBNEE8iRqMqgB-nCd97150xk3wDTwnMlXkr2H1HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غروب یک سلطنت همراه شد با طلوع یک سلطنت دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=MuKpjScl9Ku9QLFtu0g3NH8GcbHzwAvtc17hFGm3UOiVpUuo-bF7Z1j8Z_nPgpYfPt-T4dyPy2Ose62i_RKSBoYB_HJJiQI847zzNEZqupzXZwVotxb9xqqA2WEDILFcakHSdO4KTW1w78B8eVkbx65LV0MT4b4XQnTVLgXMGxfcA7CteVdjsQjWOerHv-bt3toXPxeVSF8EDcQM9ZlBC7AV17BobhLWBqaU2nAu8wQN_FZAQbt57vc-VCayb8Cl_fTXpBa4V62T3PsMxPupc08-F-bpckS9YW-fJi6e8clsPXf2DjpRQJzHYVJNM0IBh6paDAhYjq6fXsLIG14L1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=MuKpjScl9Ku9QLFtu0g3NH8GcbHzwAvtc17hFGm3UOiVpUuo-bF7Z1j8Z_nPgpYfPt-T4dyPy2Ose62i_RKSBoYB_HJJiQI847zzNEZqupzXZwVotxb9xqqA2WEDILFcakHSdO4KTW1w78B8eVkbx65LV0MT4b4XQnTVLgXMGxfcA7CteVdjsQjWOerHv-bt3toXPxeVSF8EDcQM9ZlBC7AV17BobhLWBqaU2nAu8wQN_FZAQbt57vc-VCayb8Cl_fTXpBa4V62T3PsMxPupc08-F-bpckS9YW-fJi6e8clsPXf2DjpRQJzHYVJNM0IBh6paDAhYjq6fXsLIG14L1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
