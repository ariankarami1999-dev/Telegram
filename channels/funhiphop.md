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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 18:01:04</div>
<hr>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خب دیگه چخبر</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/80970" target="_blank">📅 17:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/80965" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/80964" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عادل با شرف
❤️</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/80963" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ما کی باشیم نظر بدیم اصلا، ولش کن</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/80962" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/80961" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/funhiphop/80960" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGw4YeJnEW6OvmlsbfFLkWlo2asYvKjjGqy2WjW6GZF_svk4zur381NcEEB-4TUUXlU33DTIwWubcQXoVL60d3Lv-Z5If5ndTW_WiFD8O4LBKO3Y4drLb703EiCsAXtHIoWxGkYW_Wf7Snc85sEL-CZNniJ1wRFaZV1m3AtKcZtMRKLj94MSmxwzouFlcwlthhjMFrWgxoO7t9BC0HlDjeLlpFtC4nYrBLnCu8UAMY721LRjDkYgddPI8-x3D4B85r1JGQp9fNXqpZtsakcA1HdZEKRdj4-D6pIv6j1zVnwbQdEOxsGvzMecusMuGcSKeiEs6Uj49PWCMdWHaeBywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/80959" target="_blank">📅 16:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTfZR-Rcj3FWp2sTOWx9Q08sgd1c3bEvMbQFgLNYb_AWt0JUuJXZ5ETgr-ZIdU7h9u0eo3dPPfXJHxo3lB2PetDQPsGr6CukPiCQdDe8XQ7H2TdC37eFn_VXMVkOJZJ4ULN6L6ACh0t07rrRj3qHoEKgy2V1gcVdF-PcxnM9QtduTPxtBFbS1dph-OYhBp-V06pFDdrK2KmRlU7L9mX0rFNLr4kcKbgg2bX4qVGg3PeTvuSTfqzDzDbkN-_NrdG0kLZPSQOyKU8lA2Y0wl94BDtkOA45kMWIl8zrV-TnW9I8rBw1lApIpLVuyWHkfXMZqz8BcwT8ZdkrfXxF3V08JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم ناجی و تتویی که خیلی وقت پیش از چشماش زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/80958" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انقدر هوا گرمه که هر روز از دیروز آدم پخته تری میشم.
پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/80957" target="_blank">📅 16:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80955" target="_blank">📅 15:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بارسا لاپورتو گرفت</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80954" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80953" target="_blank">📅 15:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80952" target="_blank">📅 14:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80951">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80951" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قاطی "همون همیشگی" امشب یه همون همیشگی دیگه هم هست و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80950" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80949" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80948" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxOdsZR-FaOrQ3ryRR6RWtsZFHR_Nb1BuUr-jWZ4mnz-bTOgzFhuHoTOWwTZsGe94-eSiWOL2ikpOWtvC4EYOxca2fFwVc64qRRPSXzrnWV59Hm2_XLFIWrXzPy-ojVuYDg_jH6m_IohqUSv_hfT1catjMTRlZ4L-35FUdKtHtjo8ApgjDmseKOGDno_brB8xyZFrtDUfWaWKuemaavPq6_4ulxEjO1dN21zKkWnrvbhuNeAGq_12Y34gyKYFql99uHIIL1h4GjfADcN_RjjYVxa4Men5s-8ZoA3ljMFRtAGnefrx1FFeebORsZ2KXSDe2QzwMUB_iy5wJbJ9DLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید چه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80947" target="_blank">📅 13:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شات جدید یاس.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80946" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شات جدید یاس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80945" target="_blank">📅 12:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGloriø</strong></div>
<div class="tg-text">رنگ پوست رو میخوای چیکار کنی داداش؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80944" target="_blank">📅 11:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVBqEdEn7yjjHNLFcR8tupu7CL6En-bviqkLSm6imLhgZgKuEfnxDo_2se-EB7vJDRB2Fqn13MNTV4bMch63kePdbVQfIHocIojQmsrK_89EL6M4ofarXQUHYD1xZuemhpludRtDLmgPPsjFQsUmovleVJQu9qgjPvMJxbfbAtRlCttDiLqdZUk1uKvL1LB-uHMDcKssSnZRc1VAxF0gFSqd4bLpTCbKCjscOVIEFCDrIt6FicVUwoUZXNmDF1D3uLr-lm3yfGAY1pd9Yo_dUloLDNZ7QSRoBYGN4J01gB9dhBI9FH1cmdjKf2Am32Ooj8AFswJKoijLQbfj2-BCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی، فقط همینو بگم وینیسیوس رفته عمل زیبایی انجام داده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80943" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80942" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80941" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80939">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هووففف عجب امتحان عربی زبان قرآن سختی بود.
احساس می‌کنم تازه عمق جمله‌ی عرب هر چه باشد مرا دشمن است رو درک کردم.
@FunHipHop</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80939" target="_blank">📅 10:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpk5m-3YyzAUBeunkRjJ_IRYTvXa-nc0qJQpQGNl_WBnut5yLjLvwxdq_dJoXRTUwFSgEqYV_pRQc3UB5LnNByEsviObuiFOF3jfZxMT-008ZBwWotkQlOXw9LRFUpfuql93GSDl-Bpgk8BjCTtWZkwQURcHUCZzYTNO8_JcDVAcgt3kQLJHYSTUrB5lxo62-aNxdCTPv-1FEGbm4MUmB7gOu8UlgJcP2O-rOXF3nG5um43eAuXv-FV4I_9sWBie9-TpLdiEZo4GqCMG2LMe2h67r0Ynkv__9GAmw0hrMjTc8Dg6NSjYGU42fCbeThFQgMhuLt_J43x2Q-DyxJ3gRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند سوخت رسان به همراه چندین جنگنده و بمب‌افکن حامل میز و صندلی‌های بسیار بزرگ برای برگزاری مراسم تاجگذاری محمد سامتینگ شاه در حال حرکت به سمت خاورمیانه هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80938" target="_blank">📅 10:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY1CbA5rCvXpxQFbRHILHGebkVubTb0kLPeI9GGZVFbaP6S0FqTPGTEgyaHsPNmYae3x9QmUCzUgcUKV_3GcncuLjoAoAoAIvnvn5xDvRfT2AjtEXQn011XmWnlliuc3Z08Kh7dD7cjOhjUcqZlqPDD_KxpBCu0u2AS2jIxQbIvPg_DyObAbRwnIeUIfOYGfxU4d7y9cRsP1DDgtZhxgAsiyKwLl5C_XqfBE9QzNJ143EXJls31mbys9nNawrcrjeNbApb40MDf111psM9nIBgPxT-IhL2RkHIdXq-NtKCAxe5lS1JwHoIiCB2Y7o_ya7gP45dC5NRtwkU734jyn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی چیکار کردی ایکس هم دیگ سالم نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80937" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apX8w9ZUdNbiEv5ZmlMw7uw29oIlTy3uq7FgXDxU6R6U-D7CwSqa4txix8ngcXBKKqfYKJH7RBzPQjl9vOT8aliIXkoeAEO4wBlo-7s2gZoOy0ueMSnWNzy7VW29e08KdKBS0jCqOVBjIxFzrkeZUYX1o5qBjr9Ax2oiSm3sp1MKGqYW7_vwl9yAMXpyhM_GXogsj_LruxvquSZPDiapfoVaCiVhH7cp2Lz-kWUJhkoPC73ySMB_phYwzAGQQ-BdMKRe5Jbo-Sl2m8Yu6Cl-wDi3otoO2al4JPRx2h9z6lkdMOck3l1U4EaOyFouFKTybWgUe2y5Xw8dkX2hT1Uwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuhXtd1oaGpLWhEiZXIjEtpHzORyBehQZIRcBcqABGh4rux43EWeK5GTxrawcDILpHws34ztBGFNq0Z6pcb7KJt1Te1_6r6OyIYgQHociEWF7qW6V6DoHY4-7RvZKU6IZVn4P-gmzARfOwKqbwPl2292CUXmwH5px28NYM1cbqYmpEsIj26xzzSE3_lPsx9O8h119Xh-8geo-sfpKC2hBCbJ9yVaaJD1gzVeK-Y9XWbF3GL5Nno0iHNQZcAhI38u9t8SgUg3HrMnzyfcG-1eZn-mkjZ-36jhBxzCOCW2efWBDLXcDeLjF-IYtYL0ERYCidVOGVjf9IZjU237guDnNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنده به عنوان ادمین یه رسانه شرقی در برابر رسانه های غربی می ایستم تا حق ملت بزرگ تورک خورده نشه
✊🏿
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80935" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXEObjwFR_PM0ObVsNyp_gJIBJHk14jcg0QNoAYELYPZY1blEDcod3YyT9VD_LXvhec6nIQCOROBGxB4fdoDsGH7ljFJEPTIkFniWcNSahir0EDUy2I3fxX5Tvxm0OKivBXlDuQnXCG2JEVzxOj4GATDy_mMaOJHMYw8jqZpqyvsEOnOAh--BIsyYIdKODtQ06Katm_VLHmGaqWvgQKhgWzY_obWUKf9lSLeiJcCOISUccVprIyzqHCoj5sqrkoy5a5wKOz3RRGK6fEECFa4GJyxCHG8d4TUptPcgunZC7JX27AHkYA_dVPfN1JIGGO7eb4ktPNy8zAruz242QIZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا دید دیگه کار از هشدار به آمریکایی‌های ساکن ایران یا خاورمیانه گذشته، یه هشدار امنیتی جهانی برا تمام آمریکایی تو سراسر جهان به دلیل «افزایش تنش در خاورمیانه» صادر کرد و بهشون گفت مراقب خودتون باشید خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80934" target="_blank">📅 05:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYyzgzsueNRFMaxhWYvTsVhhHIQidJQRKWgrHKgQgLPCH_Lvslo7q62NJX5W3AMoPZ8l9gsXpSYXlwOYSz-NYager9DYr-NoHIb7VMEip9rd6L6YU7FW78j-u2FU5Ud4RC8pkRk5tjl8t1sR_nxWkneonFOxs3JYPnl2v_S9rmy2U7qTrhnbwK2MawwIsEl3DlksDO79J3pq1EE0gMeH72kW2n-HkTapDwY7WNLIkqlLFRTlC6FR1SJvBuVsJ7bQEmDoshjiSabJpPL3biZ2n-DUQbLDp3tTH0_moY23rsnJAMo459S8BkEZrdhK_U7NGGEc7FMa2KmMZO0GyMpn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ترامپ از ایفانتینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80933" target="_blank">📅 03:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چرا قبل مهاجرت کسی نگفت که خارجی ها چیزی به نام تعارف ندارن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80932" target="_blank">📅 02:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تا اینجارو هم نبستن هرچی گیف از ژنرال ساخته شده بفرستید
ما تو این جام 3 تا زدیم و 3 تا خوردیم و من تو کل گل‌ها آروم بودم؛ حالا سرمربی آرژانتین همین کار رو می‌کنه و واسش کلی کلیپ می‌سازن، پس چرا واسه من نمی‌سازید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80931" target="_blank">📅 02:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جنوب
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80929" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برنامه عادل فوتبال ۳۶۰ بخاطر انتقاد از تنها دو تیم شکست نخورده جام تیم ملی ایران بسته شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80928" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شیراز و اصفهانو زدن
انفجار در شیراز خیلی شدید بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80927" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار فاکس: احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه داره بیشتر می‌شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80926" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یادش بخیر پزشکیان میگفت پایتختو تغییر بدیم و ببریمش تو جنوب به یه استانی که نزدیک به دریا باشه
خواستم بگم سلام دکتر مسعود پزشکیان، برو دست اونی که باعث شد از این تصمیمت منصرف شی رو ببوس وگرنه الان بگا رفتن تمام امورات اداری مملکتم مینداختن گردن این تصمیم تو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80925" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امشب خیلی بد داره میزنه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80924" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آمریکا بدبخت فکر کرده مثل همیشه با آدمیزاد طرفه
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80923" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سنتکام: همون همیشگی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80922" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قاطی "همون همیشگی" امشب
یه همون همیشگی دیگه هم هست
و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80921" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه سری منابع نسبتا معتبر عربی خبری کار کردن مربوط به اینکه ایران میخواد یا خودش یا به پشتیبانی یکی از گروه های نیابتیش به کویت حمله زمینی بکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80920" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80919" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام: همون همیشگی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80918" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBWM6j3D8NrvQbC5rWJ7C8VFqAqltm8lKiWRNUMkM4n3q0ozw9M62T0jwcMsuuuGjuK1YQapa6xYXrc7ZYupOgGg9oGDwmFYgmfN-Ngotwu6nZfNUU0qgTuXuHacHIfPZoMQnl5aE9zCksyHoQSbGa9biuSVpXkpMcJxzCZz5f3CHSYBoDKCJfBLwlDxl7PPjN5ZFrVCMXaiR2wkgrLb9R8O29d_GXRid404quRyzVMvFwS2NvFXuT2ztRplfRpvEa_x8JZhUBpsBi3QP7GOez-pnyHPNMHfwvU7dr1mvY_zVjgtB4Cy4zCYBznqvwH5OipIdCyWEaRUKEqA0cRpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور آرات حسینی تو جام جهانی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80917" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80916">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80916" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onv4DWzpEqz5UIYbh3wWqZcN4AYpfoVPHUCmwgO60Qgn8h6fMAdXshlSCYb2kwYFJ4SBv4nFyx-GO0gs-PdxKxfa_uk6kXo0j9dAoZW2-PBqVA_Ye1ylRq9_eeWvgfu8u23LsjrzxEYjUB9yD_J28OMoYWc6RuDD9k4K8KR9_LPaG7KumWC4zBamxnZM1_QMpEx_idICTo33NkgbvBVJr0zdqta9xUkNneWu4_a_fM7wqfPFDr-H_64PIwm4MMHlRTUb0P5PqIh5ZwpoVTBMT9D0eQY_QvGwchhret7iQGcQKOMkIKUJSxp6XGu9v1LvSq8SEiaT01s0tUE0xuAUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که یامال گرفته دستش
شب هفتم سال :
پارادس
🆚️
گاوی
(این به یک رویداد خاص اشاره داره که در اسپانیا برگزار میشه و شامل مبارزات بوکس نمایشیه)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80915" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80914">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNslTQdxNFS28vn5o009F7LQeHuRP5caURrJi4N_BtSwgdfibpFnCeydmbazYyt4HALy8PHmxR50v05W8PgTq66pGLPgO1U3Z24RkBl_biV1ySAJUSuaZ52gUm0JKf75stjsCv68NNx6FSJye9AWTlBZ57IpR_wApxVvUcrADw9gw-nPc9BwUpX8kdKq6HKCnMjsjgCtHINx7mBLNETuLvVdPT3SN_rsO15Y7O75pZ_B7GgWNc2Szvc2jfzOjWQfslc3ppg8baMpMXBZUzCdpp87CYxHm4PHqyAQq9Jd5ZBvRpU8jGII8CJaWttVjV-v8_L3cOVuctB7inTdOv74sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پروردگار و برترین اسطوره تاریخ فوتبال:
شکست دردناک بود و زخم‌ها دیر خوب می‌شوند، اما با تمام وجودمان نتیجه را عوض کردیم. حمایت هموطنان و تلاش تیم باعث شد دوباره جزو بهترین‌های جهان باشیم. امروز قدر کارمان را بدانیم؛ این تیم دو بار پشت‌سرهم به فینال جام جهانی رسید. از ته دل از تک‌تک تبریک‌ها و پیام‌ها متشکرم. توانستیم مثل یک کشور متحد باشیم و افتخار آرژانتینی بودن را با هم تقسیم کنیم. همین‌طور به اسپانیا بابت قهرمانی در تورنمنت تبریک می‌گویم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80914" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80913">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جام جهانی 2030 با 64 تیم برگزار خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80913" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80912">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یچی میگم به اروم ترین حالت ممکن بخندید
یک مقام  در سپاه‌ پاسداران:
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80912" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80910" target="_blank">📅 20:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=X_JbAxol68wxlVXyk5z7L3j3rz2bEKCN8OI_SU-7NnsoJpv3Zui0jzFIhtvuTF9ai-VuVeBqFGcRTk_H49CQ4zwjE4GtmQLE8NKJjVnUkFPbHGLDRXYfaJjIzLYvGUc_CeiA5AYz1QwDm4j_32SetQSPnMXC0jXJk-AruQC4FVo1qddwVPVXuSd0r5UTXaPdgdN3RyjS75FZGroOHeqfR6oIyPFR9VmnazDhqSSzEjNexlpljgO7FPlTC6YYwbCG5Wv8k-8A5bzD4avQgvTi3inuVVAzVHYxF8pB7tvn__kxNXOpuz2VymdkM5X6cWPkT25aFJgHSJLaKW6xmEXwFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbd065f52.mp4?token=X_JbAxol68wxlVXyk5z7L3j3rz2bEKCN8OI_SU-7NnsoJpv3Zui0jzFIhtvuTF9ai-VuVeBqFGcRTk_H49CQ4zwjE4GtmQLE8NKJjVnUkFPbHGLDRXYfaJjIzLYvGUc_CeiA5AYz1QwDm4j_32SetQSPnMXC0jXJk-AruQC4FVo1qddwVPVXuSd0r5UTXaPdgdN3RyjS75FZGroOHeqfR6oIyPFR9VmnazDhqSSzEjNexlpljgO7FPlTC6YYwbCG5Wv8k-8A5bzD4avQgvTi3inuVVAzVHYxF8pB7tvn__kxNXOpuz2VymdkM5X6cWPkT25aFJgHSJLaKW6xmEXwFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیوت خر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80909" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بچه ها جی جی آهنگ داد
دیدم سولو موزیک میده باباشم نمیفهمه خواستم دلش نشکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80908" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پائولو مالدینی و گواردیولا در بارسلون باهمدیگه دیدار داشتند
فدراسیون فوتبال ایتالیا میخواد تمام تلاشش رو بکنه تا پپ گواردیولا سرمربی تیم ملی ایتالیا شه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80907" target="_blank">📅 19:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvEgzVXgZ3Q_fhe4GGLupdLDNtyVD3yxwQ_LYjY-PVocTD2PhPxLaYZ_aCzfTL1T3zqSl9CIqPoWKBwSdHqmWxLyDKAcw1z0h4BbfroyVmSEDzinCfLQZL8ywMpMQG58taegkPxBqKIuBEmPSeCOyXUUr5x78UohNQ7GElnkL3D_mVgAhhDjbqEWYrF2xJY3Q_qqHiwn5l09wVXuKtZYOmJiuLj4eTH-Q3U0EQ9ST9HEaaTJSNe4aR5NgoK4RrATQp4gVKghzxOoTBo-4FZWLXv4g8KuuCerbBkMt-s3i68n8g8AVhR6fii6Fh4-Pgmr9q8YPMYhVQYhh2eJt1oHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب راموس تو زمین بود یکی از بین راموس و پارادس زنده بیرون نمیرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80906" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JreVjdK3f37S6LNytJMU9nkiEwtckfR1ZYqAQ0l8aP1XyHiSuqt5SRjn6OUbCCK45QUCqSzx8NZpdyIuYCuq96IvDxXu-UjwzwSNQBMwZuM1fzt_4CVr-xBwT5Pc6gTlxessknWUZ65BgjzulZMI4WFCEGJmU1c0-8yLrPrUKpEUCRkKT_bkhisFrgW_YKMDT4doR_UZD1dm7D3LsM-2VcUcg0umXQfiQY93O0fzGaHwvN_aU7XaXfhfOr4OX3xs5MNjYEk_E4QP7FEVfLhpZDEuI9t4BoJzWVvFiXMj3wi4MugQObRdgtMM-7r1AigCSPz9d0zxsw2rjdDRJkRFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب اسلام هم به خطر افتاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80905" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حقیقتا انتخاب بهترین از تیمی مثل اسپانیا که روی تاکتیک مشخصی بازی میکنه و هر بازیکن وظیفه خودشو داره اشتباه ترین کار ممکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80902" target="_blank">📅 18:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axVIHvWWmqHFQvioFMzkdcfjMaEsbLgVRtmZHKgNognOXYHUUDk7HSFUPItMzdotq8C7h8CMEBe02j0_EoDQjUpFi6qsGuD7NJpqED5m8nbD8-_Z9cd1e0gArG7hlNFqYCetkkRwQYBjVQbLauhYYhO9oQlq4b9_MXt6bQNqhCc12t7CIHO_GevRS27r7Sgsc-7Njk_mLL1-vvbcEdNjiB6bM3gM-6SRwqOvpcaPi0lfd0I60WDjHRk3qE18Kr-UlivqVKkypFv201L1tb8toPuzVf9xUYOkL-2rQ7oc0vMoV-LdInC8BHLK6sPMV9xyI_i-87L3JJu5EAQ6G-RumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80901" target="_blank">📅 17:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omz-yoQtNzd3jDfaVjXNvPwjq6zCd4TIA0L3VX7bQpV99WiGuS8Esri-y7AIXAvUbc9UqbuLdRmzKbkIZi19TLmAtHysHvSDMPmnLKlwOKWglGtVWe3XACvLamf1ApniIVZjTj_OYns1dFkJa36q1Sfw4wRmLeW7SkpiLQkSBrQebFw5jhpBuI8I4w3bq7tjTRNhSPh3Sl4M1GVf77wG0n5OM2_APhSQgYc_7G-9sGasd-ezW-g2smaJJP6v_toYbyplpOX8hH2ba75WmP0LYIV6XC-278iOCkrHokV2hIX-N8VqCt-GI_jKoSfA79Y_v1T9Rn_SXuogKqHnCzrUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا: یکی از قربانیان حمله موشکی ایران به پایگاه در اردن، ایزابلا گونزالس ۱۹ ساله، اهل تگزاس بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80900" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC3Ai72et3eJoO4RfXXaA8X1S70vGg93NutSyLdflejAA_6FQUirmm6RNyEeZGgwQaFMy2YsOBLOVHkmbyGz7LvnweI1h7oM0_gRyWzCF39jCWEI7YOl8VqRAA0a9BQpc5_UcaveSJdPHKm8LvLKb2fYv9UryvbDBYmyEdkEpTsJEVhaMvFBxe1MudCYoLYcIH2I8jprxtWjiWmAxSNEUKsa0rDCesMUsA38tqu8whywNfgD5hn7ZZ_Lj-VAOKSHD3vDKkxHLtNvSJYwlt6HHJOliNn-5arK6SoLzpO8UqmVpYCjBEKfca5aS2L42CDZs7ng_TYd9OOtcZ3XJiZ89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام دلو هم زنده اس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80898" target="_blank">📅 17:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80897">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lM7pO8ivOzPcoupJhfQqfYnjo2uLYMRZfINco_t-CGQaW-4SmtxSA9hHVyb18ddKulgHnyxAcI5xDFj7G5Hq8mhLv1UvzMPUoav8VMm9XglgElB7XOuauYDKl739d-d9a5IFe98vbWBc3PTJSpXmwfu2QQa-BUEpMmwzBCtbOVDwLi96M2RYKNmoiRGo8nvVYEvd7vx8sXB0vxenpNML3HiiZX9eVHS7Gnf3-WNAU3_WPaofeVVMLvKyF-m4eYyEE55KmI6vy7cLJ9JLByJlRS27T3VeUqoK835Gf57IpN1g2vaekbWxQtBLUXCftJ8DQgFLj2svupT2JCgC5gug5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های مسی برای رهبر شهید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80897" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80896">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_2ePylTOqdmf9EcTRDgIEFeW_g_G-xCMLIRVYgxPVi0YMDoWb5lbDPxMgD38Rx4Fz1Uv-8kl3eR90QFCovsobBSrFz6JhWDIlaI40lCkxorMQ6aRbP0md8mAhc0RtifQ5mbo9PxFDTYBFiBHLq_33GIyH1NS1Tk1WORecdz5hnc36f9fW1vvh2k2IZA9_kA2_vv3XSTfpe1-1-Yztd73Dz7oPcjOYICxwuodByzufnwUWmm52fPlujV5mfTc6K1lyessPDCASoHVI5QayRW5nJaguTRUJ_vn11KmbhSWdQV348SBPoaPuSd-vhxuzD34U7l1C3I42kJfNMu4FcJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه :
نقشه دانش آموزان برای تعویق شکست خورد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80896" target="_blank">📅 16:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMvRkvTFCGtaygbxjrkUICKJxkUS6Ph5Q9ZvdzPw1-mpBk-mWnxEeQgBvrs-Q0zRVaF6ZwKDX0_IEwqd5PjuE_eUPDqwlho2N_aEykOPQKKcQz5RwqGP1OhKFWj_xUuwcx5gR56TN8YjYRImEnPzXYKucJD6Rq0PbeMIx6EZs2vJvuNaiHA8EIUhqNN0L96zFUbVIPk3cO3lbLVnozZSM0REZ7cOiqkDxNKMPjwc-FHHVp4xW9lbMD2xr6QrLGqfHvPxZPt68k2VqQGJjqfh8ZolJPz0E1JzBbYvHavHTrDe4Cve5VRc8TE5cUlQo435q2rcIZpdaa4qQXMLwmknBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJjZzn7OnmHQMsdyuOvkilSTsZw_IrkofkVG69iNMakBX9mwQ7EJ1WApze1FTdBdaflvhEGSeFe4kZxwLjBKAVhVUr5eEEaLYnKRo0yz7H7yG6fOJ-jXh4gCzriyltHxQ3ZbU2wCYkv7kfkAfj5c2TkOP_YibwRbsW6hNMIaykdqsLJgUnsyrzKeQmhnmRC1moHGgpIpqdVHAmHu-bKkaqeo1QyDJNlqwo1dsEwchbsnu5h3bDa8UWu88cnUAaL3Bf9b7IuNaNBtz7s1TsEyhPArRMyCvKCVysQ5crPpUz7OHYkJMWqF_YgaijuPnP-gYYsn0tkqPQs1CL7pSAphTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دکی و صدف در حال عشق و حال با پولای ویناک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80894" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9pKbg-6plW6e_pkYuxV2BssXP7prc_WA1UFkUsT8jw7cqAGkiLz4_rd2wIwPHK3dFXcAuGOxHre7fxaoZ5EsW-e53k07a4jmhuD34WM7WB31JTEfciuzWvZgTRlpLudpm5HDO2ITcFQf1oAXh3jtxIyF3Zg8tXHEUnRbf9Oxt9YmaramgYe7O8NVKRUg3tqU98QYl0mZUfZ0WMIYIx7MNZCtgejJcaLZfNTO9yGBJXndsQVft5SnTYBbGaiE1C1OGFVy8G5fvXIFVe42QWnPiw_fTQTxJszwG1cn3AdU5Ibh7LPPdx-7EB1vz3OZx_uUpoWNmQHb1Vv_n_CAfvPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80893" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی رو گوشی این رپرا کیبورد فارسی نصب کنه تا گوشیو نکردم تو کونشون نچسبارو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80892" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80891" target="_blank">📅 15:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a85LqU-wbC-rwVnpkZmctOY9fuB8uuhKWwtojCTiQwRdmyT1b4pKi8C1gPGZDLgxGGQleYcFlUqbXB1uR6TFUzkBJw4N10gy95M0i1zdQv8CwpspSkDnUWdhuZ7OSmfIAAL2u4jOBflzSRnvpoV0fdapRrjBFkhsfZ9fp8fCQAGclkt-qfLCbAppPN7yIOPOsjJUAhdU4MM_hzcAY0Y3aAQ5nmqUupMSSkRIqLkIgUAlF62STTyZJzcCgfYr9bcA1Vu7Xu1niceEX-6G9o1UlFA-Lf3ZGTXefj0dRSDZx2hvMUb_flpogAy_WPidPuje-nBlfYuRp8sZ0jeEoMUqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80890" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttwBgd96NePGhC3i0NbEbc7zOKvhjwoF3W5DKyicoh9vR6pffDhFRKZDZzcUuAM9tjA8vmmUE8WYBJFIvWhOUBs4ozgv7QzXP4uMoyIiIqtFUx_79Ic9wM2sbSTd2vslSunzgfZ2u1gFIkfyieMeqDYgJRs6ysgD4jfA6Kwm2J6t2mcbGwtURRWhnmqqD378p-JdoNpLmjuDPMaYz4CJrzZRB4BE-j8pB0MWROvC8bOaJpXJ_FLLxTlL9V3hAg9BitU0SvUlTwpsIx0T4OIzyGzGnoaW2CUf3-oEvvdPWX0HXVYvzsp8kK7okF_lH4scOhTGc7p54JLuSBiLXYQiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80889" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEjYt5NxiqAp6d5EdAikldwmgTSGaBBvSGp1G4Zc2nAPvbUysY7azvhjoB_ZRrhs4DxBnJBQ4VvYa9BWs3ag_Fkc_kFBuZhwHsPpeTopyInvRgkjOuPxlUSPWdEBaYfF19RzRxc_fmVqV6pQ_Q4i7C5N4iowkloYtc0fTA_1SqrcnOftIFmWn6Apm4pprpBU8uCjpq9gUmYz0FipunOQPqlZ-37Lcb7VMc48fg1-D-mQAqwerbcEFulTQAULupzuStq1bNtObmZOXGdvQwxdJTRD4X3puKGy1r8hub4oCFJfJXnEazku0Ekddk2V_WzC3NUQYpUETzg6uwrU65LEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین همینجا بازیو باخت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80888" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد پس</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80887" target="_blank">📅 14:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اصلا وایب خوبی نداشت امسال</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80885" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آقا من هنوز سیر نشدم، از اول برگذار کنید جام جهانی رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80884" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_MCcbgXU3vGoVp_WiAtz2gWl2dl0zOjACpsLtqDYM4S9zgiwzArjPkzxI96fZWmnp6V6uTbGB_DpS97Yhzt6XGgApkiJbNboQusMrqwPNpT5IUs2rvoCN79AIXTmVGyvX36ej-4BnwVQAIVBYyxwCH0S38Jm7MufmTvRHbuVpiDccQt6BzjeG3TJzh_TPc2nY3AjjLfUzAZuIhMfhCzNWZOZIQ13DDm7_KpFp6DXbjTaKIFpwxR6Sj4D_XBVo613E3YKBlynfGedM1DKMei7SpM9sEKUThxyr8Xt6_Hh0Rhya-lPBF8vxbLKWO7BWGeYYLrdohPB7izZwgKpxmNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فواید رابطه با اسب.
#بخوانیم_و_بدانیم
#اطلاعات_عمومی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80883" target="_blank">📅 14:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عه ۲۰۰ کا شدیم</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80880" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4l-eQZM2tSQls3yoGnpbNsnAVU-Euo_TuOnTWnl-nzqNMs2wSHfoqUW0I374RmQ_cqi5I3NR4EnD_hp87NuCLrE5WrUiubP0jLm4NUJ_hafxw5IeDPkMl7YUa_Ma-C3Nw_zUpj70mt19mvA74I-Sv8zqJvRhMVkpHH3jrwYsajR-Msv6An3DwwZmKN-WC-6VFoxe3VlT3HlpUSiuSF-uIaNnpda2SxwdLW0TP87fwF5sqPcc8D3KQZ5iywOozcfPPx012PUb1hL9tVDJkR4XwY1WAm5lHhxtAC3u3btBlMh0Wguohouf_U16yUsh7SRzl-IhGUzDryZ3sg6qKsvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال باحال ترین اتفاق این جام جهانی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80879" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیل هیوم: نتانیاهو امروز بعد از ظهر جلسه‌ای اضطراری با هیئت وزیران امنیتی خود درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80878" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVMPIZdRzRX-PtXHwaEEokSATOgnNyLiRksWvLNPQ6wvo3VMtOYSG0RaX7qBBAOpcilh3gEaljwyyIqjhVcXs4Nyoh68TSUZr4JanFXu5d_mw_if-6Kj9Wx5Gp-d6Gy65yInI_c3pLi5Xo7lWr3dMwZxQDUjsHGEM2iRDbVPSxutXvwOB2mUGPztfOfFM3nd9Avzz1DWNwFGvqISDEv6TEAKuHQ6lsJeaoof4WeaqOnmu9Ryr8r6zF3uRzjxoO1qcQ13PF0PfD9u_utLm3lsxFnPPXNT1FcsiiwNG3pbWbaJ-efZu95s2hEJcx4cfBHom4Om9DB2UsMU9LEzlVL-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a23PMtvQ3_KmNr9NSBCjKxtsXpmfZH8sPcjn0Mv2A9S_tU-HOduMjUrcA9fvqzexz4oiNq-6QTqeKr7-_mQ2UvIZo7rkfgXwlTyoiljSaM3WrEBRzQHjTkwvcmamAjNZon90xRdtRv014XBBX5k7QzAVZ6csPurndpc1RwYctjd58mOKcR11qt-unIm5een6xKqNYzqXx9l557kXiN87vzHXNAHDlspAVson9FSbrOjomEDCtS8-ZfbU8wF7gE5Jg87uVf7TvWVt-LjWJq1eUQcgRE8Sune9lvkvMtux2zIAl28x5JKhB3Mw9ecc-D0eMLtp3zokrLROrTrsQRx1aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا اجازه؟ امروز میخواستید امتحان بگیرید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80876" target="_blank">📅 13:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqy9oLrqmPOuEvF_IP8Olnbis6Rt3tu0ufyig0GxTm_W_NKFK0a4dfPu8Ms96kk0FX3S0VKlDIQCik1CQlnJoV7_a7tcztlYMbKOXw_O9ZL-RD2ZHOTRfiqRrioPvr66e8E6u1zxoBhaL3Ycrjrl-FV6HXZYUctEb7YXdeP1UJ43dd96UCQriD6D9R-L4A5PJO4_syP_AvIrqnmSspTHRRywwyRxNeaVM5n6-rLaWs0sqp4SrnVUewbgz-MqhjrL2e9eBlN5w7ML1l0SZVlAyL0YzvJwlVJWc7xqYxuCyHoOTp_UySKaOa0YTWCadV1QPdPM-lWigQd0HWZ__iInXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟ این دستشو گذاشت جلو دهنش به ما فحش داد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80875" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwtQ_20ferkcdkf6QlEGVwkk5PYJKX0z3qkK_nE8GAP8a79k6tF8kdvjnSXgVG6HS7cvI04veu3uC1bJoytUdxECR6uSue_RwmHIeZ9H66WgcuLg2sZ8qJFpTygahzhdnDuf2W4biNeRD05jRzAH3ewnaiMjfA9MnOTZzek6RPG0yAqNAr6EqdTImcKjPlS7yIE3h3m2JVf5Pn5f6DHdcY0eP0lKlIryNoSS55-horkEo-CE4qItSjTEfNTIj6wZmk_ikoWKbzB9FqE7-kGUBjZSuzEpWxvi5XvQnLLlW34Ij6lmaSbSL7bvel7am1y11Ux3JpaF8DkEDr83GBsG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم های یامال احساس تنفر به ترامپ کودک کش را فریاد میزنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80874" target="_blank">📅 12:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxDFT9B9oJBjbDjcy55UH32r-tC19ot1ri6--Zr80bjsgGHWy5W8kpOPBzbRlltE-5V8IzZxJLimwzrBE5yFr8_NwmPgHhqwJidb_1veIYtMrCi1RGVw2rx_yL0Mn-B7h-mk5g_4ebs8tGEk7dnzASotF7XPh58mfDqDQ8rkVS0TUmBB2S9M1Zx6cBiFY2JQfC41hMQ1S8oyDbGkrsP1MZr8H4EoP1L8vyPz1oaxMKxvxKULDVReEk4Eot-pqAVQqL9BhTMFLdRpyTxTNA-ail1iVwXBLs_QiLzZLOfZbWZ6VkNCo7gyyvY1cYjJ8gjEaDTtLZ0rt1W9wWXzSOFcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به اسپانیا بابت قهرمانی و افتخار آفرینی برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80873" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صدا هایی که شرق تهران میشنوید مربوط به خنثی سازی بمبه خوشحال نشید، امتحاناتون کنسل نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80872" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZVudLqJMf1C1D_OiYvsw2cFygG4Cud23pRiDHn90E-W36QkfBPDELNY1eu6exwOV2FozYzouA3LOaXFwZmPt892pVCNGu9KSl9KgYwqO58ZB0sV5fGLHwBzwgGU7L1_fNHGcd2xfFukTeQrZ1raFOcRmA6axQJc8zdQU43Bo_jVsTJlSWa6kRoCx8akx9usYOgd-khoO1JTueQOxsewANSfM7v6B829OPMcPy4DCrhJSFlsTQnVKmND7fdLUtx6cqXDLPAlnpfR2VHKn4KunXapp-UYYM_2bMV32kAHi5SuLp60jnNfUPK4skFw10YxNJQ2D8JYrlYiTBHZgpwznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80871" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPiWbR1RVmdk8YgrsAkGj6cj2w1aKE7X1YwSyND-JuWuIUZ9tsd2cs3DihDWKEiwZH4pDa1NwZayxW2_vBi409XD4iwpuHiND3M0MnPwiFk9SkxkXioAhswGxmN14_BFPzixR1Ja3ZRN05iSEpxvWfDly50lgapII_R277hAd-FqCS0deM8lxbDGSfKHKu4Qa0dlx410Xc9RWBdxQIrlus2sZJMhvdJcd52DbEshZJJ4ZGYDFU1DAFD8-HNJ06jUskcHtZWNJ-vMRGBZrcVLGNGgt7-CIgYmkCxHqSaQdfli-Kpt7yw81Gkjza5rsXb1wrfDMcFObS7bvrIe_MeTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی این توپ طلا حق مسی یا امباپه بود کصکشا
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80870" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm2h0Hi6Ze5JUr8fCodxeNkP1yb9hhy1qGdR8OKrjBLehprovOrvSEoI9FTrMzcDaf-cQ3z_W4mCP4kesMuBosTkBjC-vfXKDeaUBmDtOjlx5F5aguXpCiLJ_k9wE7Fo_biCxcDSWyKN382qHdBaT73hUcl7f3bCNCICVxL8FNmfDhMS-K_5R9jrXMKGCPdRd1HJ_ZKrvcOIrX3dnOyDNfUj9okakXg2ZB2j9lGUh7WwSV9U6-wWInRQEJtZMmf7pGlbvdtr1bvmmMg-oRCKidqN2LAhKKAi9P6Lf3urlravD7FlYhC68LlaKTa-M49DZBQJayER2kXlp5gczTDqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80868" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtjdpAs6miUuwdnRAltmFdktaT4c8Iz1l8veQZrX4rugi15557P5s-cMTNezjleszXCapNGm1SVBxVrwyGfMrYx46bpmIh8UhQlJShzK9E0PlapnpcETIPZCwqvaW_QfiBaYoNqpCqiqugACZMympweqGIkswwq51oj2uMZq4qWKdu5w9EX9OA9xq8pmDN3oKZvaQF6_1CV9aR1zvgsIRpIcDy2s5Mab6PmEL5D8uCbZvhetejQghv2QrzNpj-jl1XD6ZhVgAYUgkJo25IQgEu7itCKHFzYqbwDyHZN4I1IV2teD6Yw0tjEA_UbRkA1jfOmF-i1kWI_MNW7XhAZb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس شوهرعمم بعد از ریدن به عکس های خونوادگی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80867" target="_blank">📅 10:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGdRN6gSA5cGrvEzKcR4MPS0ugU6OTaWXkGCJu2VTy253ISlJ-O9V3f5XLIT1cKWPKNg4K6J19RHWqs-FTQ01sPVZ2G_JE7pZ4pI22CBpwQd4Q3jhVIUyIKZpSD_qysyb1ahk-dwd0xe0NlD-rPolUyQ5VdUFZF03OZAjPcW71wXpXAEsMFfBrNRiXMDcKryBb2uyCWyiO9UHid4GmIFmNEcuzMAWjLAlNKF_d1wYtxd8VmstO0g0jCPcR3kLKsnDZvqUd77rkaJlbj0kYyrM105xQoWl71QDWg9Whukq_Obn-gbRiz6hGWIa5wewPVB--pa7AZ-JM0KSioQ_y43kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۷ و ۱۸ دقیقه صبح تو کرمانشاه یه زلزله ۵.۷ ریشتری اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80866" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIzuXDAinCw1o1qZ3jBvNsqpsvaesfyQRcnV2P-WqAKnlaYH7EXIZEKuMMdrikpU555OJNykTvRVDY-DqsNtMqYTkkMJgkBgDUhItArcY671VvHt4EVoS6UgbAbF5jHCfe1U9iQjp7qgIQq9ta3yu-I3ssgT7djyQJGl7c3ROEFOubiRyGeUKB3VFqJz5Qt_Ys8SUhv6XWKB0NvqLoZQJDzC7LQxONKFjg9j0zhrfOhAASfZhqIiwxOgVkCKbGyJ-JS-1u9anFXHdWAMEgQdgrjtxdCDUEhLihJh-K0zIjuZGLCXQywZAXq_gFUIeK_f44ZTQ_sOMXUxY-pvYNMEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکی Dior از استایل ایرانیای دهه شصت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80865" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoGBkYdt0NlGrjDVxCouAw5vlnvUKOW3Cu0nDwhZ-VJpxQuG-JuB17ljFes-_dyKZ_uAG754VDop-5Ct0jjpeunIaexAjckrigqqtBMWQZwq892BjzgNWAnCOh1LhjQASMLc6kcpEsERdlBxY-lU0jfxPM54xu0D1CAEV38EoMR9Ddd4svvGx3wZekyc_Qd5Zis1EyFSoMly0EnEGf5JFg3rEliwAvQdx6tZdvmWdQMDLJ5rU8mkJeXEibleWbnijP6IN34UIcp5pe1xeEEFV7-Q0GXAbVU7FXh3Xk9Y6maMkd9QidYzt7uURaYlNLHwj2YSJPyNGxQByxjmyPWF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام بار این سفر جذاب و فراموش نشدنی روی دوش تو بود
خسته نباشی مرد
🩵
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80861" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حالا که جام تموم شد، رونالدو جان تو کارتو کرده بودی، اون "i'm back" گفتنت برا چی بود آخه مرد مومن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80859" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ آخر نزاشت تیم ملی اسپانیا یه عکس ملی بگیره تو همه عکسا هست کصکش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80858" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-DBQ1enS3E1w9qRoScgaYlBhjYCX2rJOeZxaOSIud2ULD6nJqvwEGt2sRjUIRbKq8WHZEQXEaJBiv54L5I-F2tiGODfdEgAO3H9Y1ekBA2eLILEJq66Hlt5odL8Z_PcxIguPRPVyP7PrcwVZXnbl8eb67kkw-o067rRR9jXEUwcFYx9f9T1toCVmrJxIOS41OmTGblWmVFadmolfisCAmoV7KFG0bOp_2ABqxWLDOYcnhQb_CtmUWDVDM40_yIC9dAxuo81rYJf8WLaTkl13rdtcC1v9hSW7n1AKoqO4OP4sH5wW7QP45zBIHXOpG_iilEqYIggkXT9jRNFZPg0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر خوشگل و کون بچه بودنت به ایران 2 هفته دیگه مهلت میدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80857" target="_blank">📅 02:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">علی دایی اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80856" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب دیگه جام جهانی تموم شد ترامپ زنجنده حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80855" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بارسا بلد نیست سی ال بزنه چطوری جام جهانیو برد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80854" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپو یکی‌ بکشه کنار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80853" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtzd7yXyo7w3jP96kxKUsdWQogIudBzrORi87M1FmxgvbeM7YzaVj4miAf07oJksP_bRqv30LOPxDMZYBxO0fUpcBTjjTcvb2qn0S0AKSs_XgYhusjPNfOaqbP4DTWrlyVJp-c2r9gAhSlUXaHhgXPKGRKe6GD2rYCcE48DciI0RDz5eijNThRhP5vcySE_O_lGhx9OLmiDkypgRcZHgDYaZEPhXMCcVFFg_0xzbvp7a7Bp-rn3Evn4I7t9uh7zMKttiVBUo_wL0R8byqjHywpH27C2YXMp57w60atMN0YJiUumR4DMMuFjzoh08UjBn64O2RtZF5LsJmMVXELL5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80852" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رودری هم به عنوان بهترین بازیکن جام انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80851" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اونای سیمون هم بهترین گلر جام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80850" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کوبارسی به عنوان بهترین بازیکن جوان تورنمت انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80849" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
